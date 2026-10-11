# Board study

Tracing, identifying, and redrawing the Board (`KD-F316-V1.0`) as a KiCad schematic, to understand how it works. Separate from the repair: see the spec in [#1](https://github.com/robintomar1/fix_my_frother/issues/1) and terms in [`CONTEXT.md`](../../CONTEXT.md).

## Sections

| Section | Issue | Document | Status |
|---|---|---|---|
| Power and charging | [#9](https://github.com/robintomar1/fix_my_frother/issues/9) | [power-section.md](power-section.md) | Drafted from photos; **unverified**, waiting on the meter |
| Motor drive | [#10](https://github.com/robintomar1/fix_my_frother/issues/10) | — | Not started |
| Button and LEDs | [#11](https://github.com/robintomar1/fix_my_frother/issues/11) | — | Not started |
| U1 identity and how the Board works | [#12](https://github.com/robintomar1/fix_my_frother/issues/12) | — | Not started |

## Files

- `frother-board.kicad_pro` / `frother-board.kicad_sch`: the KiCad 9 project and schematic. Open the `.kicad_pro` in KiCad.
- `frother.kicad_sym` + `sym-lib-table`: project symbols for parts with no standard symbol (the 6-pin USB-C receptacle and the unmarked SOP-8 U1).
- `<section>.md`: one per section. Each has a **Connections** table (one row per pad, with evidence, confidence, and a Verified box), a meter checklist, and hypotheses about how the section works.
- `check_netlist.py`: checks the schematic against the Connections tables.

## The check

```
python3 hardware/board-study/check_netlist.py [section.md ...]
```

Exports the schematic's netlist with `kicad-cli` (KiCad 9) and compares every pad's net with the Connections table(s); defaults to `power-section.md`. Prints `OK` or lists each disagreement. Run it after every schematic edit and every table update.

It proves **the drawing matches the table**. Only continuity checks with the meter prove **the table matches the Board**.

## Workflow per section

1. Trace from photos into the section's Connections table, with evidence and confidence for each pad.
2. Draw it in KiCad, using net labels that match the table; run the check until it says `OK`.
3. With the meter, work through the section's checklist on the unpowered Board. Post readings as comments on the section's issue, tick Verified, and replace any `?` placeholder net with the real connection, in both the table and the schematic.
4. Re-run the check. The section is done when every row is verified and the check passes.

## Known ERC results

KiCad's electrical rules check is expected to report, for the power section:

- **U1 pins 3–8 not connected**: deliberate. Their destinations aren't known yet, and marking them "no connect" would hide that. (Pins 1 and 2 carry inferred links to C2 and C1.)
- **Dangling labels** on `BAT+`, `R7_TO_U1?`, `R6_A?` and `R6_B?`: each is a single-ended connection whose other end, almost certainly a U1 pin, is unknown.
- **"Library 'Device' not in configuration"**: only when run headless before KiCad has been opened once; the GUI's global library table resolves it.
