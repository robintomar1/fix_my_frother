# Power and charging section

Part of the Board study ([#9](https://github.com/robintomar1/fix_my_frother/issues/9)). Covers the path from the USB-C port (USB1), through U1, to the Cell's pads (BAT+ / BAT−).

**Status: traced from photos only, nothing verified yet.** Every row below is a hypothesis until it has been checked with the multimeter's continuity mode on the real, unpowered Board. The back of the Board hasn't been photographed yet ([#3](https://github.com/robintomar1/fix_my_frother/issues/3)), so traces that pass through to the back are invisible.

## How to read this

- **Confidence**
  - `seen-2`: trace or pour visibly connects them in two or more photos.
  - `seen-1`: visible in one photo only.
  - `inferred`: not visible; follows from part values, position, or standard practice.
- **Verified** is ticked only after a continuity check on the real Board. Record the reading in a comment on #9.
- The **Connections** table is the expected netlist: `check_netlist.py` compares it against the KiCad schematic. One row per pad; `Net` names are the schematic's net labels. A net name ending in `?` is a placeholder for a connection whose other end isn't known yet.

## U1 orientation

U1 is an unmarked SOP-8. **Pin 1 is the pin in the corner nearest C2**, on the row that faces C1/C2 (the USB-C side). Evidence: the moulded dimple on the package is in that corner, and the silkscreen has a dot beside that pin (IMG_7895, IMG_7899). Pins are numbered counter-clockwise viewed from above: 1–4 along the USB-C-side row, then 5–8 along the LED-side row.

If the meter session shows this is wrong, every U1 pin number below shifts, so check this first.

## Parts in this section

| Ref | Part | Marking | Value | Notes |
|---|---|---|---|---|
| USB1 | USB-C receptacle, 6-pin power-only | — | — | Pins: GND, VBUS, CC1, CC2, VBUS, GND, plus shell tabs |
| R8 | Resistor, 0603 | `512` | 5.1 kΩ | Beside USB1 |
| R9 | Resistor, 0603 | `512` | 5.1 kΩ | Beside USB1 |
| R7 | Resistor, 0603 | `102` | 1 kΩ | Between USB1 and U1 |
| R6 | 0 Ω link, 1206 | `0` | 0 Ω | Near C1; role unknown |
| C1 | Capacitor, 0805 | — | unknown | Beside U1's USB-C-side row |
| C2 | Capacitor, 0603 | — | unknown | Beside U1 pin 1 |
| U1 | Unmarked SOP-8 IC | none visible | — | Identity is #12's job |
| BT1 | The Cell (off-Board) | — | ~3.7 V Li-ion | Soldered via Tabs to BAT+ / BAT− |

## Connections

| Pad | Net | Evidence | Confidence | Verified |
|---|---|---|---|---|
| USB1.S1 | GND | Shell tabs sit inside the large copper pour that also holds the BAT− pad (IMG_7895, IMG_7899) | seen-2 | [ ] |
| USB1.A12 | GND | Outer USB-C pins are GND by the standard; pour reaches the connector | inferred | [ ] |
| USB1.B12 | GND | As above | inferred | [ ] |
| BT1.2 | GND | BAT− pad sits in the same pour as USB1's shell tabs (IMG_7895, IMG_7899) | seen-2 | [ ] |
| USB1.A9 | VBUS | VBUS by the USB-C standard | inferred | [ ] |
| USB1.B9 | VBUS | VBUS by the USB-C standard | inferred | [ ] |
| USB1.A5 | CC1 | Two traces run from the connector to R8/R9 (IMG_7899) | seen-1 | [ ] |
| USB1.B5 | CC2 | As above | seen-1 | [ ] |
| R8.1 | CC1 | 5.1 kΩ is the standard USB-C "sink" pull-down on a CC pin | inferred | [ ] |
| R8.2 | GND | Pull-down's other end goes to GND by definition | inferred | [ ] |
| R9.1 | CC2 | As R8 | inferred | [ ] |
| R9.2 | GND | As R8 | inferred | [ ] |
| R7.1 | VBUS | A trace runs from the connector to R7 (IMG_7899); which USB pin is unknown | seen-1 | [ ] |
| R7.2 | R7_TO_U1? | Runs toward U1; destination pin unknown | inferred | [ ] |
| R6.1 | R6_A? | Unknown | inferred | [ ] |
| R6.2 | R6_B? | Unknown | inferred | [ ] |
| C1.1 | C1_TOP? | Probably U1's supply pin (decoupling) | inferred | [ ] |
| C1.2 | GND | Decoupling capacitors return to GND | inferred | [ ] |
| C2.1 | C2_TOP? | Sits against U1 pin 1 | inferred | [ ] |
| C2.2 | GND | Decoupling capacitors return to GND | inferred | [ ] |
| BT1.1 | BAT+ | BAT+ pad, labelled on the silkscreen | seen-2 | [ ] |

U1's eight pins are deliberately left unconnected in the schematic: no pin's destination is known yet. KiCad's electrical rules check reports them as unconnected, which keeps them visible as open questions.

## Meter checklist

Board **unpowered**, Cell connected or not (it doesn't matter for continuity, but never short BAT+ to GND). Meter in continuity (beep) mode.

1. **Find GND**: BAT− pad ↔ USB-C shell. Expect a beep. Everything else is measured against this.
2. **U1 pin 1**: check which U1 pins beep to GND; note them.
3. **VBUS**: find which U1 pin(s) beep to R7's far end, to R6's ends, and to C1's U1-side end.
4. **CC pins**: R8 and R9: each should beep from one end to GND.
5. **BAT+**: which U1 pin(s) beep to the BAT+ pad. (BAT+ to M+ belongs to #10.)
6. **C2**: which U1 pin its non-GND end lands on.

Post each result as a comment on #9, tick the row above, replace any `?` net with the real one, and re-run `check_netlist.py` after updating the schematic.

## How charging probably works

Hypotheses only, each tied to rows above:

- **The charger declares itself as a sink.** R8/R9 (5.1 kΩ to GND on CC1/CC2) tell any USB-C charger "a device wants 5 V". Without them, a USB-C-to-C charger would supply nothing. This is why the Frother can charge from both USB-A-to-C and C-to-C cables. (Rows `R8.*`, `R9.*`.)
- **U1 is both the charger and the controller.** No separate charging chip is visible, so U1 most likely takes 5 V from VBUS (through R7 and/or R6), charges the Cell through BAT+, and runs the button, LEDs, and Motor. (Rows `R7.*`, `R6.*`, `BT1.1`.)
- **C1/C2 smooth U1's supply** against the Motor's electrical noise. (Rows `C1.*`, `C2.*`.)
- **BAT− is the Board's ground.** The Cell's negative side, the USB ground, and the shell share one copper pour, so charging current returns straight through it. (Rows `BT1.2`, `USB1.S1`.)
