# Button and LED section

Part of the Board study ([#11](https://github.com/robintomar1/fix_my_frother/issues/11)). Covers the power button (K1), the four indicator LEDs (LED1–4), and the parts clustered around them.

**Status: traced from photos only, nothing verified yet.** Conventions (confidence levels, `?` placeholders, the Verified box) are the same as in [power-section.md](power-section.md#how-to-read-this). A net of `—` means the pad's connection hasn't been traced at all: the part is drawn, its pins are left open. Back-side photos ([#3](https://github.com/robintomar1/fix_my_frother/issues/3)) are still missing.

## What the Handle shows

The front panel (IMG_7890) has the power button and **four indicator windows** below it: one slightly larger window nearest the button, possibly marked with a lightning bolt (low-confidence read), then three small dots.

On the Board, LED4 sits on its own beside K1, and LED1, LED2, LED3 form a row running away from it (IMG_7895, IMG_7898). That matches the panel's order, so the likely mapping is:

| Window (from the button down) | LED |
|---|---|
| Larger window, possibly a bolt | LED4 |
| Dot 1 | LED1 |
| Dot 2 | LED2 |
| Dot 3 | LED3 |

The three dots show the speed mode while running and the charge level while charging (see Observed behaviour below). Whether the larger window or the power symbol is the fourth light isn't known yet, so the LED4 row of this mapping is the least certain.

## Parts in this section

Package sizes are estimates from the photos.

| Ref | Part | Marking | Value | Notes |
|---|---|---|---|---|
| K1 | Tactile switch, 4-pin, ~6 × 6 mm | — | — | The power button. Its 4 pins are two internally joined pairs |
| LED1 | LED, ~0603 | — | colour unknown | Row nearest U1 |
| LED2 | LED, ~0603 | — | colour unknown | Middle of the row |
| LED3 | LED, ~0603 | — | colour unknown | Row end, nearest the BAT+ end |
| LED4 | LED, ~0603 | — | colour unknown | Alone beside K1 and R5 |
| R1 | Resistor, ~0603 | unreadable | unknown | Beside LED3: possibly a current-limiting resistor for the LEDs |
| R3 | 0 Ω link, ~1206 | `0` | 0 Ω | Beside LED4 and K1: a jumper |
| R5 | 0 Ω link, ~1206 | `0` | 0 Ω | Between LED1 and LED4: a jumper |

R2, R4 and C4 are still unassigned; see [power-section.md](power-section.md#parts-not-yet-assigned-to-a-section).

## Connections

| Pad | Net | Evidence | Confidence | Verified |
|---|---|---|---|---|
| K1.1 | GND | A button usually pulls a U1 input to GND when pressed | inferred | [ ] |
| K1.2 | KEY? | The other side goes to a U1 input; pin unknown | inferred | [ ] |
| LED1.1 | — | Not traced | — | [ ] |
| LED1.2 | — | Not traced | — | [ ] |
| LED2.1 | — | Not traced | — | [ ] |
| LED2.2 | — | Not traced | — | [ ] |
| LED3.1 | — | Not traced | — | [ ] |
| LED3.2 | — | Not traced | — | [ ] |
| LED4.1 | — | Not traced | — | [ ] |
| LED4.2 | — | Not traced | — | [ ] |
| R1.1 | — | Not traced | — | [ ] |
| R1.2 | — | Not traced | — | [ ] |
| R3.1 | — | Not traced | — | [ ] |
| R3.2 | — | Not traced | — | [ ] |
| R5.1 | — | Not traced | — | [ ] |
| R5.2 | — | Not traced | — | [ ] |

## Meter checklist

Board **unpowered**. Meter in continuity (beep) mode unless noted. Never bridge BAT+ to GND with the probes.

1. **K1**: find the two pin pairs (pins that always beep together). Then check which pair beeps to GND, and which U1 pin the other pair reaches. Press the button while probing across the pairs: it should beep only while pressed.
2. **LED polarity**: in **diode mode**, probe each LED both ways; in the conducting direction the LED often glows faintly. Note which pad is the anode.
3. **LED connections**: for each LED pad, note every U1 pin, R1 end, R3/R5 end, GND, or BAT+ it beeps to.
4. **R1**: measure its resistance (out of circuit readings may differ slightly) and note both ends' nets.
5. **R3, R5**: note which nets each jumper joins; they carry another section's trace across this one.

Post each result as a comment on #11, replace `—` rows with real nets, tick Verified, and re-run `check_netlist.py` after updating the schematic.

## Observed behaviour

How the Frother behaved before it died, as remembered by its owner (2026-10-11). The schematic has to explain these.

- [x] **Button**: one press turns the Frother on; another press some time later turns it off. Presses in quick succession change the speed mode.
- [x] **Three dots**: while running, they show the speed mode; while charging, they show the charge level.
- [ ] **Larger window** (the first circle under the power symbol): not yet known whether it lights, or whether the power symbol itself is the fourth light.
- [x] **Colour**: all lights are blue.
- [ ] How many speed modes there are, and how the dots show each one.

## How the button and LEDs probably work

Hypotheses only:

- **U1 is a programmed chip, not a fixed-function one.** Telling a single press (on/off) from quick repeated presses (change speed mode) needs timing, and the same three dots show the speed mode while running but the charge level while charging. Both need a program, so U1 is most likely a small microcontroller with its program built in. This points #12's search toward the cheap 8-pin microcontrollers used in small appliances. (Observed behaviour.)
- **K1 is a single input to U1.** U1 times the presses to tell "on/off" from "change speed mode". (Rows `K1.*`.)
- **The three dots are U1 outputs it reuses for two jobs:** speed mode while running, charge level while charging. That suggests U1 senses the Cell's voltage (for charge level) and USB power being present (to switch the dots' meaning). The latter fits R7 feeding U1 a "USB present" signal. (Rows `LED1`–`LED3`; power section `R7.*`.)
- **All the LEDs are blue.** Blue LEDs need about 2.7–3.2 V to light, close to the Cell's own voltage. So the LEDs are probably driven straight from U1's pins at the Cell's voltage, with little or no resistor. That's consistent with only one small resistor (R1) being near the LEDs. (Rows `LED*`, `R1.*`.)
- **The LEDs may be "charlieplexed".** U1 has only 8 pins. Supply, Cell, GND, Motor and the button plausibly use five, leaving about three for four LEDs. Three pins can drive up to six LEDs if each LED sits *between* two U1 pins instead of between a pin and GND. If so, the meter will show LED pads beeping to U1 pins at **both** ends. (Rows `LED*`.)
- **R3 and R5 are jumpers.** On a Board with copper on one side only, a 0 Ω link lets one trace hop over another. They probably carry power or GND past the LEDs. (Rows `R3.*`, `R5.*`.)
