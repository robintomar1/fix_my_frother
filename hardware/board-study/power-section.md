# Power and charging section

Part of the Board study ([#9](https://github.com/robintomar1/fix_my_frother/issues/9)). Covers the path from the USB-C port (USB1), through U1, to the Cell's pads (BAT+ / BAT−).

**Status: traced from photos only, nothing verified yet.** Every row below is a hypothesis until it has been checked with the multimeter's continuity mode on the real Board, with power fully off (USB unplugged and the Cell disconnected). The back of the Board carries nothing but the Cell: no parts (owner's inspection, 2026-10-11) and, in IMG_7894, bare board with no visible copper, so every trace is on the front.

## How to read this

- **Confidence**: of the whole row, including the net name.
  - `seen-2`: the connection is visible in two or more photos.
  - `seen-1`: visible in one photo only.
  - `inferred`: not visible; follows from part values, position, or standard practice. A row can have a visible trace and still be `inferred` if the net's identity isn't visible.
- **Verified** is ticked only after a continuity check on the real Board. Record the reading in a comment on #9.
- The **Connections** table is the expected netlist: `check_netlist.py` compares it against the KiCad schematic. One row per pad; `Net` names are the schematic's net labels. A net name ending in `?` is a placeholder for a connection whose identity isn't known yet.

## U1 orientation

U1 is an unmarked SOP-8. **Pin 1 is the pin in the corner nearest C2**, on the row that faces C1/C2 (the USB-C side). Evidence: the moulded dimple on the package is in that corner, and the silkscreen has a dot beside that pin (IMG_7895, IMG_7899). Pins are numbered counter-clockwise viewed from above: 1–4 along the USB-C-side row, then 5–8 along the LED-side row.

If the meter session shows this is wrong, every U1 pin number below shifts, so it's the first item on the checklist.

## Parts in this section

Package sizes are estimates from the photos, scaled against U1's 1.27 mm pin pitch.

| Ref | Part | Marking | Value | Notes |
|---|---|---|---|---|
| USB1 | USB-C receptacle, 6-pin power-only | — | — | Pins: GND, VBUS, CC1, CC2, VBUS, GND, plus shell lugs |
| R8 | Resistor, ~0603 | `512` | 5.1 kΩ | Beside USB1 |
| R9 | Resistor, ~0603 | `512` | 5.1 kΩ | Beside USB1 |
| R7 | Resistor, ~0603 | `102` | 1 kΩ | Between USB1 and U1 |
| R6 | 0 Ω link, ~1206 | `0` | 0 Ω | Above C1; role unknown |
| C1 | Capacitor, ~1206 | — | unknown | Lower pad between U1 pins 2 and 3, nearer 2 |
| C2 | Capacitor, ~0603 | — | unknown | One pad directly over U1 pin 1 |
| U1 | Unmarked SOP-8 IC | none visible | — | Identity is #12's job |
| BT1 | The Cell (off-Board) | — | ~3.7 V Li-ion | Soldered via Tabs to BAT+ / BAT− |

The pad by USB1 is silkscreened `BAT` with no sign visible (solder may cover it). Calling it **BAT−** is an inference from it sharing the ground pour with USB1's shell, and from the other pad being labelled `BAT+`.

### Parts not yet assigned to a section

These may belong to the Cell side of this section or to another section. They're listed here so nothing is silently skipped; the meter session decides. (R1, R3 and R5 are in [button-led-section.md](button-led-section.md) by position.)

| Ref | Part | Marking | Value | Why it might be here |
|---|---|---|---|---|
| R2 | Resistor, ~0603 | `103` (low-confidence read) | 10 kΩ? | Beside C4 on U1's LED-side row: a typical spot for a charge-current-setting resistor |
| C4 | Capacitor, ~0603 | — | unknown | Beside R2 on U1's LED-side row: possibly a capacitor on the Cell's supply |
| R4 | 0 Ω link, ~1206 | `0` | 0 Ω | Jumper between the LED row and BAT+; may carry any section's net |

They're drawn in the schematic with their pins open.

## Connections

| Pad | Net | Evidence | Confidence | Verified |
|---|---|---|---|---|
| USB1.S1 | GND | Shell lugs sit inside the large copper pour that also holds the BAT− pad (IMG_7895, IMG_7899) | seen-2 | [ ] |
| USB1.A12 | GND | Outer USB-C pins are GND by the standard; pour reaches the connector | inferred | [ ] |
| USB1.B12 | GND | As above | inferred | [ ] |
| BT1.2 | GND | BAT− pad sits in the same pour as USB1's shell lugs (IMG_7895, IMG_7899); net name is an inference (see above) | seen-2 | [ ] |
| USB1.A9 | VBUS | VBUS by the USB-C standard | inferred | [ ] |
| USB1.B9 | VBUS | VBUS by the USB-C standard | inferred | [ ] |
| USB1.A5 | CC1 | Traces run from the connector to R8/R9 (IMG_7895, IMG_7899), but which pin lands on which resistor isn't visible | inferred | [ ] |
| USB1.B5 | CC2 | As above | inferred | [ ] |
| R8.1 | CC1 | 5.1 kΩ is the standard USB-C "sink" pull-down on a CC pin | inferred | [ ] |
| R8.2 | GND | Pull-down's other end goes to GND by definition | inferred | [ ] |
| R9.1 | CC2 | As R8 | inferred | [ ] |
| R9.2 | GND | As R8 | inferred | [ ] |
| R7.1 | VBUS | A trace runs from the connector to R7 (IMG_7895, IMG_7899); that it's the VBUS pin is an inference | inferred | [ ] |
| R7.2 | R7_TO_U1? | Runs toward U1; destination pin unknown | inferred | [ ] |
| R6.1 | R6_A? | Unknown | inferred | [ ] |
| R6.2 | R6_B? | Unknown | inferred | [ ] |
| C1.1 | U1_PIN2? | Lower pad sits against U1 pin 2 (IMG_7895); no trace visible | inferred | [ ] |
| U1.2 | U1_PIN2? | As above | inferred | [ ] |
| C1.2 | GND | Decoupling capacitors return to GND | inferred | [ ] |
| C2.1 | U1_PIN1? | Left pad sits directly over U1 pin 1 (IMG_7895); no trace visible | inferred | [ ] |
| U1.1 | U1_PIN1? | As above | inferred | [ ] |
| C2.2 | GND | Decoupling capacitors return to GND | inferred | [ ] |
| BT1.1 | BAT+ | BAT+ pad, labelled on the silkscreen | seen-2 | [ ] |

U1 pins 3–8 are deliberately left unconnected in the schematic: their destinations aren't known yet. KiCad's electrical rules check reports them as unconnected, which keeps them visible as open questions.

## Meter checklist

**Power fully off**: USB unplugged *and* the Cell disconnected. Lift the BAT+ Tab at the Board end; the Tab repair ([#7](https://github.com/robintomar1/fix_my_frother/issues/7)) is the natural time, since the Tab comes off then anyway. With the Cell soldered on, the Board is powered and continuity readings are unreliable. Meter in continuity (beep) mode. Never bridge BAT+ to GND with the probes.

1. **Confirm U1 pin 1.** Probe C2's pad nearest U1 against each U1 pin: it should beep on the pin called 1 here. Then C1's U1-side pad: it should beep on pin 2. If either lands elsewhere, re-number U1 before anything else.
2. **Find GND**: BAT− pad ↔ USB-C shell. Expect a beep. Note which U1 pins beep to GND.
3. **CC pins**: each of R8 and R9 should beep from one end to GND, and from the other end to one of USB1's two middle pins. Note which.
4. **VBUS**: find which USB1 pin R7's connector-side end beeps to, then which U1 pin(s) beep to R7's other end, to each end of R6, and to that USB1 VBUS pin directly.
5. **BAT+**: which U1 pin(s) beep to the BAT+ pad. (BAT+ to M+ belongs to #10.)
6. **Unassigned parts**: for R2, R4 and C4, note which nets each end beeps to, and move each part into the section it belongs to.

Post each result as a comment on #9, tick the row above, replace any `?` net with the real one, and re-run `check_netlist.py` after updating the schematic.

## How charging probably works

Hypotheses only, each tied to rows above:

- **The Board declares itself as a sink.** R8/R9 (5.1 kΩ to GND on CC1/CC2) tell a USB-C power source that a sink wants 5 V. Without them, a USB-C-to-C charger would supply nothing; with them, the Frother should charge from both USB-A-to-C and C-to-C cables. That's a prediction, not something observed yet. (Rows `R8.*`, `R9.*`.)
- **U1 both charges the Cell and drives the Motor.** No separate charging chip is visible, so U1 most likely takes 5 V from VBUS, charges the Cell through BAT+, and also handles the button, LEDs, and Motor. (Rows `BT1.1`, `R7.*`, `R6.*`.)
- **R7 is not the charging path.** At 1 kΩ, R7 can pass only a few milliamps from 5 V, far below a charging current. It more likely feeds U1 a small supply or a "USB present" signal. Charging current would then flow through R6 (a 0 Ω link) or a trace not yet seen. (Rows `R7.*`, `R6.*`.)
- **C1/C2 smooth U1's supply** against the Motor's electrical noise. (Rows `C1.*`, `C2.*`.)
- **BAT− is the Board's ground.** The Cell's negative side, the USB ground, and the shell share one copper pour, so charging current returns straight through it. (Rows `BT1.2`, `USB1.S1`.)
