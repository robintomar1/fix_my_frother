#!/usr/bin/env python3
"""Check that the KiCad schematic matches the traced Connections table.

Exports the schematic's netlist with kicad-cli and compares every pad's net
against the `## Connections` table in a section document (default:
power-section.md). Exits non-zero and lists every mismatch if they differ.

This proves the drawing matches the table. Only the meter proves the table
matches the Board.

Usage: python3 check_netlist.py [section.md ...]
"""
import re
import subprocess
import sys
import tempfile
from pathlib import Path

STUDY_DIR = Path(__file__).resolve().parent
SCHEMATIC = STUDY_DIR / "frother-board.kicad_sch"


def table_pads(section: Path) -> dict[str, str]:
    """Map 'REF.PIN' -> net from the section's Connections table."""
    text = section.read_text()
    if "## Connections" not in text:
        sys.exit(f"{section.name} has no '## Connections' table")
    body = text.split("## Connections", 1)[1].split("\n## ", 1)[0]
    pads = {}
    for line in body.splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 2 or not re.fullmatch(r"[A-Z]+\d+\.\w+", cells[0]):
            continue
        pads[cells[0]] = cells[1]
    return pads


def schematic_pads() -> dict[str, str]:
    """Map 'REF.PIN' -> net from the schematic, ignoring unconnected pins."""
    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp) / "netlist.net"
        subprocess.run(
            ["kicad-cli", "sch", "export", "netlist", "--format", "kicadsexpr",
             "--output", str(out), str(SCHEMATIC)],
            check=True, capture_output=True,
        )
        netlist = out.read_text()
    pads = {}
    nets = netlist.split("(nets", 1)[1]
    for block in re.split(r"\(net \(code ", nets)[1:]:
        name = re.search(r'\(name "([^"]*)"\)', block).group(1).lstrip("/")
        if name.startswith("unconnected-"):
            continue
        for ref, pin in re.findall(r'\(node \(ref "([^"]+)"\) \(pin "([^"]+)"', block):
            pads[f"{ref}.{pin}"] = name
    return pads


def main() -> int:
    sections = [Path(a) for a in sys.argv[1:]] or [STUDY_DIR / "power-section.md"]
    expected = {}
    for section in sections:
        expected.update(table_pads(section))
    if not SCHEMATIC.exists():
        print(f"No schematic at {SCHEMATIC.name}")
        return 1
    actual = schematic_pads()

    problems = []
    for pad, net in sorted(expected.items()):
        if pad not in actual:
            problems.append(f"{pad}: table says {net!r}, schematic has it unconnected or missing")
        elif actual[pad] != net:
            problems.append(f"{pad}: table says {net!r}, schematic says {actual[pad]!r}")
    for pad in sorted(set(actual) - set(expected)):
        problems.append(f"{pad}: schematic says {actual[pad]!r}, not in any table")

    if problems:
        print("Schematic and table disagree:")
        print("\n".join(f"  {p}" for p in problems))
        return 1
    print(f"OK: {len(expected)} pads match between schematic and table.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
