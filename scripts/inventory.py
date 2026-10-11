# /// script
# requires-python = ">=3.11"
# ///
"""Query and validate the structured studio inventory in inventory/*.toml.

Units (with ports), connections (one file per rig) and scenarios are loaded together.
Port specs may use ranges, which are expanded:
    { id = "in-{n}", range = [1, 4], label = "MIC/LINE {n}" }  → in-1 … in-4
    { id = "monitor-{ch}", channels = ["L", "R"] }              → monitor-L, monitor-R

Usage:
    uv run scripts/inventory.py check                 # validate refs, port use, duplicates
    uv run scripts/inventory.py units [--kind K]      # list units
    uv run scripts/inventory.py ports <unit>          # a unit's ports and what's on them
    uv run scripts/inventory.py trace <unit[:port]>   # follow signal upstream and downstream
    uv run scripts/inventory.py find <text>           # search ids, names, labels, notes
    uv run scripts/inventory.py scenarios             # intents and preferred realizations
"""
from __future__ import annotations

import argparse
import sys
import tomllib
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INV = ROOT / "inventory"


def expand(spec: dict) -> list[dict]:
    if "range" in spec:
        lo, hi = spec["range"]
        keys = [("n", n) for n in range(lo, hi + 1)]
    elif "channels" in spec:
        keys = [("ch", c) for c in spec["channels"]]
    else:
        return [dict(spec)]
    out = []
    for var, val in keys:
        p = {k: v for k, v in spec.items() if k not in ("range", "channels")}
        p["id"] = spec["id"].replace("{%s}" % var, str(val))
        p["label"] = spec.get("label", "").replace("{%s}" % var, str(val))
        out.append(p)
    return out


def load():
    units, conns, scenarios, errors = {}, [], [], []
    for f in sorted(INV.glob("*.toml")):
        data = tomllib.loads(f.read_text())
        for u in data.get("unit", []):
            if u["id"] in units:
                errors.append(f"duplicate unit id {u['id']} ({f.name})")
            ports = {}
            for spec in u.get("ports", []):
                for p in expand(spec):
                    if p["id"] in ports:
                        errors.append(f"duplicate port {u['id']}:{p['id']}")
                    ports[p["id"]] = p
            u["ports"], u["_file"] = ports, f.name
            units[u["id"]] = u
        for c in data.get("connections", []):
            c["rig"], c["_file"] = data.get("rig", "?"), f.name
            conns.append(c)
        scenarios += data.get("scenario", [])
    return units, conns, scenarios, errors


def port_of(units, ref):
    unit, _, port = ref.partition(":")
    u = units.get(unit)
    return u, (u["ports"].get(port) if u and port else None)


def check(units, conns, scenarios, errors) -> int:
    used_out, used_in = defaultdict(list), defaultdict(list)
    for c in conns:
        for end in ("from", "to"):
            u, p = port_of(units, c[end])
            if not u:
                errors.append(f"unknown unit in {end}: {c[end]} ({c['_file']})")
            elif not p:
                errors.append(f"unknown port in {end}: {c[end]} ({c['_file']})")
        fu, fp = port_of(units, c["from"])
        tu, tp = port_of(units, c["to"])
        if fp and fp.get("direction") == "in":
            errors.append(f"connection starts at an input: {c['from']}")
        if tp and tp.get("direction") == "out":
            errors.append(f"connection ends at an output: {c['to']}")
        if c.get("medium", "physical") == "physical" and c.get("signal") != "data":
            used_out[c["from"]].append(c["to"])
            used_in[c["to"]].append(c["from"])
    for port, srcs in used_in.items():
        if len(srcs) > 1:
            errors.append(f"input {port} has several physical sources: {srcs}")
    for port, dsts in used_out.items():
        if len(dsts) > 1:
            errors.append(f"output {port} feeds several physical cables: {dsts}")
    unknown = [
        f"{u['id']}: {k}"
        for u in units.values()
        for k, v in {**u, **u.get("product", {})}.items()
        if v in ("?", "owned?") or (isinstance(v, str) and v.endswith("?"))
    ]
    nports = sum(len(u["ports"]) for u in units.values())
    print(f"{len(units)} units, {nports} ports, {len(conns)} connections, {len(scenarios)} scenarios")
    if unknown:
        print(f"\nopen values ({len(unknown)}):")
        print("  " + "\n  ".join(unknown))
    if errors:
        print(f"\nerrors ({len(errors)}):")
        print("  " + "\n  ".join(errors))
        return 1
    print("\nno errors")
    return 0


def describe_conn(c, other):
    bits = [c.get("medium", "physical")]
    if c.get("notes"):
        bits.append(c["notes"])
    return f"{other}  [{', '.join(bits)}; {c.get('confidence', '?')}]"


def ports(units, conns, unit_id):
    u = units.get(unit_id)
    if not u:
        sys.exit(f"no unit {unit_id}")
    print(f"{u['id']} — {u['name']} ({u.get('kind')}, {u.get('status')})")
    for pid, p in u["ports"].items():
        ref = f"{unit_id}:{pid}"
        links = [describe_conn(c, "→ " + c["to"]) for c in conns if c["from"] == ref]
        links += [describe_conn(c, "← " + c["from"]) for c in conns if c["to"] == ref]
        arrow = {"in": "in ", "out": "out", "bidirectional": "i/o"}.get(p.get("direction"), "   ")
        print(f"  {arrow} {pid:<16} {p.get('label', ''):<24} " + ("; ".join(links) if links else "—"))


def trace(units, conns, ref):
    unit, _, port = ref.partition(":")
    if unit not in units:
        sys.exit(f"no unit {unit}")
    starts = [ref] if port else [f"{unit}:{p}" for p in units[unit]["ports"]]
    by_from, by_to = defaultdict(list), defaultdict(list)
    for c in conns:
        if c.get("signal") == "data":
            continue
        by_from[c["from"]].append(c)
        by_to[c["to"]].append(c)

    def walk(node, index, key, arrow, depth, seen):
        for c in index.get(node, []):
            nxt = c[key]
            print("  " * depth + f"{arrow} {describe_conn(c, nxt)}")
            if nxt in seen:
                continue
            seen.add(nxt)
            nu = nxt.split(":")[0]
            if "mix" in units.get(nu, {}).get("functions", []):
                # A mixer can route any input to any output; what actually flows is live
                # state (e.g. Console sends and mirrors), not cabling. Stop and say so.
                print("  " * (depth + 1) + f"⋯ mixed inside {nu}: check its live routing state")
                continue
            # passive or single-path unit: continue through any port on the far side
            for p in units.get(nu, {}).get("ports", {}):
                walk(f"{nu}:{p}", index, key, arrow, depth + 1, seen)

    for s in starts:
        if not (by_from.get(s) or by_to.get(s)):
            continue
        print(s)
        walk(s, by_to, "from", "←", 1, {s})
        walk(s, by_from, "to", "→", 1, {s})


def find(units, conns, text):
    t = text.lower()
    for u in units.values():
        hay = " ".join(str(v) for k, v in u.items() if k != "ports").lower()
        if t in hay:
            print(f"unit  {u['id']} — {u['name']}")
        for pid, p in u["ports"].items():
            if t in " ".join(str(v) for v in p.values()).lower():
                print(f"port  {u['id']}:{pid} — {p.get('label')}")
    for c in conns:
        if t in " ".join(str(v) for v in c.values()).lower():
            print(f"conn  {c['from']} → {c['to']} ({c.get('notes', '')})")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cmd", choices=["check", "units", "ports", "trace", "find", "scenarios"])
    ap.add_argument("arg", nargs="?")
    ap.add_argument("--kind")
    a = ap.parse_args()
    units, conns, scenarios, errors = load()
    if a.cmd == "check":
        return check(units, conns, scenarios, errors)
    if a.cmd == "units":
        for u in units.values():
            if not a.kind or u.get("kind") == a.kind:
                print(f"{u['id']:<18} {u.get('kind', ''):<22} {u.get('status', ''):<8} {u['name']}")
    elif a.cmd == "ports":
        ports(units, conns, a.arg)
    elif a.cmd == "trace":
        trace(units, conns, a.arg)
    elif a.cmd == "find":
        find(units, conns, a.arg)
    elif a.cmd == "scenarios":
        for s in scenarios:
            print(f"{s['id']} [{s.get('status')}] — {s['intent']}")
            print(f"  hears: {s.get('mix')} on {s.get('transducer')}")
            for r in s.get("realization", []):
                print(f"  · {r}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
