# /// script
# requires-python = ">=3.11"
# dependencies = ["tomli-w"]
# ///
"""Snapshot the live UAD Console state (read-only) to TOML + a Markdown view.

Talks to the UA Mixer Engine on 127.0.0.1:4710 using only `get` requests, so it never
changes anything. Captures, per Apollo:
  - device roles and monitor section (remote monitor controller, alt, dim, correction profiles)
  - inputs: name, type, fader, mute, hardware preamp (gain, 48V, pad, low cut, phase, Hi-Z),
    Unison preamp plugin, inserts with their parameters, and aux / cue (monitor-mix) sends
  - outputs: monitor and cue outputs with source (main mix vs cue), mirror and mono

Writes data/snapshots/ua-console/<YYYY-MM-DD_HHMM>.toml and .md, plus latest.toml / latest.md.
UAD Console (or the UA Mixer Engine) must be running.

Usage:
    uv run scripts/ua_snapshot.py [--label "before tracking vocals"]
"""
from __future__ import annotations

import argparse
import json
import shutil
import socket
import time
from datetime import datetime
from pathlib import Path

import tomli_w

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "snapshots" / "ua-console"
HOST, PORT = "127.0.0.1", 4710
THROTTLE_S = 0.03   # pause between queries; the engine crashed once under a burst (R15)
SKIP_TYPES = {"ADAT", "S/PDIF", "TalkbackMic"}


_sock: socket.socket | None = None


def get(path: str, retries: int = 3) -> dict:
    """One `get` over a single reused, throttled connection. Never opens a connection per query:
    a burst of new connections crashed the UA Mixer Engine once (docs/studio/inventory.md R15)."""
    global _sock
    for attempt in range(retries):
        try:
            if _sock is None:
                _sock = socket.create_connection((HOST, PORT), timeout=3)
            time.sleep(THROTTLE_S)
            _sock.sendall(f"get {path}\0".encode())
            buf = b""
            while not buf.endswith(b"\0"):
                chunk = _sock.recv(65536)
                if not chunk:
                    raise ConnectionError("closed")
                buf += chunk
            msg = json.loads(buf.rstrip(b"\0").split(b"\0")[-1])
            if msg.get("path") not in (path, None):   # skip any unsolicited message
                continue
            return msg["data"]
        except (ConnectionError, OSError, json.JSONDecodeError):
            if _sock:
                _sock.close()
            _sock = None
            time.sleep(0.2 * (attempt + 1))
    raise ConnectionError(f"UA Mixer Engine did not answer for {path}")


def props(path: str) -> dict:
    return {k: v.get("value") for k, v in get(path).get("properties", {}).items() if "value" in v}


def children(path: str) -> list[str]:
    return list(get(path).get("children", {}))


def clean(d: dict) -> dict:
    """Drop None values (TOML has no null) and round floats."""
    out = {}
    for k, v in d.items():
        if v is None or v == {} or v == []:
            continue
        out[k] = round(v, 2) if isinstance(v, float) else v
    return out


def plugin(path: str) -> dict | None:
    p = props(path)
    if not p.get("EffectName"):
        return None
    params = {}
    if "parameters" in children(path):
        for c in children(f"{path}/parameters"):
            pp = props(f"{path}/parameters/{c}")
            if pp.get("Name"):
                params[pp["Name"]] = pp.get("StringValue", pp.get("NormalizedValue"))
    return clean({"plugin": p["EffectName"], "power": p.get("Power"), "preset": p.get("Preset") or None,
                  "params": params})


def snapshot_input(base: str) -> dict | None:
    p = props(base)
    io = p.get("IOType", "")
    if io in SKIP_TYPES or p.get("Name") in (None, "N/A 1"):
        return None
    if io == "Virtual" and not p.get("Active"):
        return None
    rec = {"name": p.get("Name"), "type": io, "active": p.get("Active"),
           "fader_db": p.get("FaderLevel"), "mute": p.get("Mute"), "stereo": p.get("Stereo")}
    kids = children(base)
    if "preamps" in kids:
        for pc in children(f"{base}/preamps"):
            pre = props(f"{base}/preamps/{pc}")
            rec["preamp"] = clean({"gain": pre.get("Gain"), "phantom_48v": pre.get("48V"), "pad": pre.get("Pad"),
                                   "low_cut": pre.get("LowCut"), "phase": pre.get("Phase"), "hi_z": pre.get("HiZ")})
            if "effects" in children(f"{base}/preamps/{pc}"):
                for e in children(f"{base}/preamps/{pc}/effects"):
                    u = plugin(f"{base}/preamps/{pc}/effects/{e}")
                    if u:
                        rec["unison"] = u
    if "effects" in kids:
        inserts = []
        for e in children(f"{base}/effects"):
            ins = plugin(f"{base}/effects/{e}")
            if ins:
                inserts.append({"slot": int(e) + 1, **ins})
        rec["inserts"] = inserts
    if "sends" in kids:
        sends = {}
        for sc in children(f"{base}/sends"):
            sp = props(f"{base}/sends/{sc}")
            if sp.get("Gain", -144) > -144:
                sends[sp["Name"]] = round(sp["Gain"], 1)
        rec["sends_db"] = sends
    return clean(rec)


def snapshot_output(base: str) -> dict | None:
    p = props(base)
    io = p.get("IOType", "")
    if io not in ("Monitor", "Cue", "Headphone"):
        return None
    return clean({"name": p.get("Name"), "type": io, "active": p.get("Active"),
                  "source": p.get("MixInSource"),            # mon = main mix; cue / cueN = a monitor mix
                  "mirror_to": p.get("OutputDestination"),  # Cue Mirror to (rack units)
                  "mono": p.get("MixToMono"), "level_db": p.get("CRMonitorLevel"), "mute": p.get("Mute"),
                  "dim": p.get("DimOn")})


def snapshot() -> dict:
    devices = []
    for d in children("/devices"):
        p = props(f"/devices/{d}")
        dev = clean({
            "index": int(d), "name": p.get("DeviceName"), "order": p.get("MultiUnitOrder"),
            "remote_monitor_controller": p.get("RemoteMonitorController"),
            "cue_bus_count": p.get("CueBusCount"), "alt_monitor_selection": p.get("AltMonSelection"),
            "dim_db": p.get("DimAttenuation"), "function_switch": p.get("FuncSwitchMode"),
            "speaker_correction": clean({"profile": p.get("SpeakerCorrectionName"), "power": p.get("SpeakerCorrectionPower")}),
            "headphone_correction": clean({"profile": p.get("HeadphoneCorrectionName"), "enabled": p.get("HeadphoneCorrectionEnable")}),
        })
        dev["inputs"] = [r for i in children(f"/devices/{d}/inputs") if (r := snapshot_input(f"/devices/{d}/inputs/{i}"))]
        dev["outputs"] = [r for o in children(f"/devices/{d}/outputs") if (r := snapshot_output(f"/devices/{d}/outputs/{o}"))]
        devices.append(dev)
    return {"devices": devices}


def onoff(b) -> str:
    return "on" if b else "off"


def markdown(data: dict) -> str:
    s = data["snapshot"]
    lines = [f"# UAD Console snapshot: {s['taken']}", ""]
    if s.get("label"):
        lines += [f"**Label:** {s['label']}", ""]
    lines += [f"Read-only from the UA Mixer Engine by `scripts/ua_snapshot.py`. Data: `{s['file']}`.",
              "Terms: *main mix* = MONITOR; a *monitor mix* = a UA cue (see docs/studio/model.md §4.7).", ""]
    for dev in data["devices"]:
        lines += [f"## {dev['name']}", ""]
        roles = []
        if dev.get("remote_monitor_controller"):
            roles.append("remote monitor controller")
        sc, hc = dev.get("speaker_correction", {}), dev.get("headphone_correction", {})
        if sc.get("profile"):
            roles.append(f"speaker correction '{sc['profile']}' ({onoff(sc.get('power'))})")
        if hc.get("profile"):
            roles.append(f"headphone correction '{hc['profile']}' ({onoff(hc.get('enabled'))})")
        if roles:
            lines += ["- " + "\n- ".join(roles), ""]
        lines += ["**Inputs**", "", "| Input | Type | Fader | Preamp | Unison | Inserts | Sends |", "|---|---|---|---|---|---|---|"]
        for i in dev["inputs"]:
            pre = i.get("preamp", {})
            pre_s = ", ".join(x for x in [
                f"gain {pre['gain']:g}" if "gain" in pre else "",
                "48V" if pre.get("phantom_48v") else "", "pad" if pre.get("pad") else "",
                "low cut" if pre.get("low_cut") else "", "Hi-Z" if pre.get("hi_z") else "",
                "phase" if pre.get("phase") else ""] if x)
            uni = i.get("unison")
            uni_s = f"{uni['plugin'].removeprefix('UAD ')} ({onoff(uni.get('power'))})" if uni else ""
            ins_s = "<br>".join(f"{x['plugin'].removeprefix('UAD ')} ({onoff(x.get('power'))})" for x in i.get("inserts", []))
            sends_s = ", ".join(f"{k} {v:g}" for k, v in i.get("sends_db", {}).items())
            fader = f"{i['fader_db']:g} dB" if "fader_db" in i else ""
            if i.get("mute"):
                fader += " (muted)"
            lines.append(f"| {i['name']} | {i.get('type', '')} | {fader} | {pre_s} | {uni_s} | {ins_s} | {sends_s} |")
        lines += ["", "**Outputs (main mix and monitor mixes)**", "",
                  "| Output | Type | Source | Mirror to | Mono | Level | State |", "|---|---|---|---|---|---|---|"]
        for o in dev["outputs"]:
            src = {"mon": "main mix", "cue": "own monitor mix"}.get(o.get("source", ""), o.get("source", ""))
            state = ", ".join(x for x in ["active" if o.get("active") else "inactive",
                                          "muted" if o.get("mute") else ""] if x)
            level = f"{o['level_db']:g} dB" if "level_db" in o else ""
            mirror = "" if o.get("mirror_to") in (None, "None") else o["mirror_to"]
            lines.append(f"| {o['name']} | {o['type']} | {src} | {mirror} | {'yes' if o.get('mono') else ''} | {level} | {state} |")
        loaded = [(i["name"], p) for i in dev["inputs"] for p in ([i["unison"]] if "unison" in i else []) + i.get("inserts", [])]
        if loaded:
            lines += ["", "**Plugin settings**", ""]
            for name, p in loaded:
                params = ", ".join(f"{k} {v}" for k, v in p.get("params", {}).items())
                lines.append(f"- **{name}** · {p['plugin'].removeprefix('UAD ')} ({onoff(p.get('power'))}): {params}")
        lines.append("")
    return "\n".join(lines)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--label", help="short note, e.g. 'before tracking vocals'")
    args = ap.parse_args()
    now = datetime.now()
    stamp = now.strftime("%Y-%m-%d_%H%M")
    OUT.mkdir(parents=True, exist_ok=True)
    toml_path, md_path = OUT / f"{stamp}.toml", OUT / f"{stamp}.md"
    data = {"snapshot": clean({"taken": now.isoformat(timespec="seconds"), "label": args.label,
                               "source": f"UA Mixer Engine {HOST}:{PORT} (read-only get)",
                               "file": str(toml_path.relative_to(ROOT))}), **snapshot()}
    toml_path.write_text(tomli_w.dumps(data))
    md_path.write_text(markdown(data))
    shutil.copyfile(toml_path, OUT / "latest.toml")
    shutil.copyfile(md_path, OUT / "latest.md")
    n_in = sum(len(d["inputs"]) for d in data["devices"])
    print(f"wrote {toml_path.relative_to(ROOT)} and .md ({len(data['devices'])} devices, {n_in} inputs); latest.* updated")


if __name__ == "__main__":
    main()
