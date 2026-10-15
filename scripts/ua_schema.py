# /// script
# requires-python = ">=3.11"
# ///
"""Dump the UA Mixer Engine's self-described schema (read-only).

Every engine node reports its properties with type, range / enum values, default and a
`readonly` flag, and the root node lists the engine's commands with their arguments. This
walks the tree with `get` only, descending into the first child of each repeated list
(inputs/0, sends/0, …) so the walk stays small (~50 requests).

Writes data/snapshots/ua-console/engine-schema.json: {"protocol", "version", "nodes": {path:
{prop: {type, min, max, default, values, readonly}}}, "commands": {name: args}}. Current
values are left out, except on the root, where they show what is selected.

Usage:
    uv run scripts/ua_schema.py
"""
from __future__ import annotations

import json
import re
import socket
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "snapshots" / "ua-console" / "engine-schema.json"
HOST, PORT = "127.0.0.1", 4710
THROTTLE_S = 0.08   # one connection, paced: a burst crashed the engine once (inventory.md R15)
MAX_VALUES = 8      # long enum lists (sessions, plugins) are truncated


_sock: socket.socket | None = None


def get(path: str) -> dict:
    global _sock
    if _sock is None:
        _sock = socket.create_connection((HOST, PORT), timeout=5)
    time.sleep(THROTTLE_S)
    _sock.sendall(f"get {path}\0".encode())
    buf = b""
    while not buf.endswith(b"\0"):
        chunk = _sock.recv(65536)
        if not chunk:
            raise ConnectionError("engine closed the connection")
        buf += chunk
    return json.loads(buf.rstrip(b"\0").decode())


def describe(prop: dict, keep_value: bool) -> dict:
    out = {k: v for k, v in prop.items() if k != "value" or keep_value}
    if isinstance(out.get("values"), list) and len(out["values"]) > MAX_VALUES:
        out["values"] = out["values"][:MAX_VALUES] + [f"… {len(prop['values'])} total"]
    return out


def walk(path: str, nodes: dict) -> dict:
    data = get(path).get("data", {})
    nodes[re.sub(r"/(\d+)(?=/|$)", "/N", path)] = {
        k: describe(v, keep_value=path == "/") for k, v in data.get("properties", {}).items()}
    children = data.get("children", {})
    numeric_seen = False
    for name in (children if isinstance(children, (dict, list)) else []):
        if str(name).isdigit():
            if numeric_seen:
                continue
            numeric_seen = True
        walk(path.rstrip("/") + "/" + str(name), nodes)
    return data


def main() -> None:
    nodes: dict = {}
    root = walk("/", nodes)
    props = root.get("properties", {})
    schema = {
        "protocol": props.get("ProtocolVersion", {}).get("value"),
        "version": props.get("Version", {}).get("value"),
        "nodes": nodes,
        "commands": root.get("commands", {}),
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(schema, indent=1) + "\n")
    n_props = sum(len(p) for p in nodes.values())
    print(f"{len(nodes)} node types, {n_props} properties, {len(schema['commands'])} commands → {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
