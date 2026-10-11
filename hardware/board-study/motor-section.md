# Motor drive section

Part of the Board study ([#10](https://github.com/robintomar1/fix_my_frother/issues/10)). Covers the path from the Cell (BAT+) through the Motor (M+ / M−), D2 and C3, to whichever U1 pin switches the Motor.

**Status: traced from photos only, nothing verified yet.** Conventions (confidence levels, `?` placeholders, the Verified box) are the same as in [power-section.md](power-section.md#how-to-read-this). The back of the Board carries nothing but the Cell: no parts (owner's inspection, 2026-10-11) and, in IMG_7894, bare board with no visible copper, so every trace is on the front.

## Parts in this section

Package sizes are estimates from the photos.

| Ref | Part | Marking | Value | Notes |
|---|---|---|---|---|
| M1 | The Motor (off-Board), small brushed DC | — | — | Soldered directly to the M+ / M− pads at the end of the Board |
| D2 | Diode, 2-terminal, ~SOD-123 | not readable | — | One pad sits right at the M− pad; the other points toward M+ / BAT+ (IMG_7895, IMG_7898). Polarity band not visible |
| C3 | Capacitor, ~0603 | — | unknown, rated 50 V (silkscreen) | Beside D2's M− end, next to the BAT+ pad (IMG_7895, IMG_7898) |
| BT1 | The Cell | — | — | Shared with the power section; only `BT1.1` (BAT+) matters here |

**No switching transistor is visible anywhere on the front of the Board.** Every other part is accounted for, and the back carries nothing but the Cell, so U1 must switch the Motor with a transistor built into the chip.

## Connections

| Pad | Net | Evidence | Confidence | Verified |
|---|---|---|---|---|
| M1.1 | BAT+ | Typical arrangement: Motor's + side tied to the Cell, − side switched. M+ is the pad nearest BAT+ | inferred | [ ] |
| M1.2 | M- | M− pad, labelled on the silkscreen (IMG_7895, IMG_7898) | seen-2 | [ ] |
| D2.2 | M- | One D2 pad sits right at the M− pad (IMG_7895, IMG_7898); that it's the anode is inferred from the flyback role | inferred | [ ] |
| D2.1 | BAT+ | A diode across the Motor clamps the voltage spike when the Motor is switched off; its cathode goes to the + side | inferred | [ ] |
| C3.1 | BAT+ | 50 V-rated capacitor beside the Motor pads: typical noise suppression across the Motor | inferred | [ ] |
| C3.2 | M- | As above | inferred | [ ] |

`M-` is a single-ended net in the drawing until the U1 pin that switches it is found.

## Meter checklist

**Power fully off**: USB unplugged *and* the Cell disconnected. Lift the BAT+ Tab at the Board end; the Tab repair ([#7](https://github.com/robintomar1/fix_my_frother/issues/7)) is the natural time, since the Tab comes off then anyway. With the Cell soldered on, the Board is powered and continuity readings are unreliable. Meter in continuity (beep) mode for steps 1–4, resistance for step 5. Never bridge BAT+ to GND with the probes.

1. **M+ ↔ BAT+**: expect a beep. If not, find which net M+ is on.
2. **D2**: put the meter in **diode mode** across D2 both ways; one direction reads roughly 0.2–0.7 V, the other open. The end that's negative in the conducting direction is the anode. Confirm the anode is on M− and the cathode on M+ / BAT+.
3. **C3**: which nets each end beeps to (expect one on BAT+, one on M−).
4. **M− ↔ U1**: which U1 pin beeps to M−. With no other switching part on the Board, one should. If none does, re-check D2 and C3: one of them would then have to be something other than a diode or capacitor.
5. **Motor coil**: resistance across M+ / M− with power fully off, **red probe on M+, black on M−**. That way D2, which sits across the Motor, is reverse-biased and doesn't skew the reading. A few ohms is healthy; near 0 Ω means shorted, no reading means open. (This is also the repair's diagnostic step in #5.)

Post each result as a comment on #10, tick the row above, and re-run `check_netlist.py` after updating the schematic.

## How the Motor drive probably works

Hypotheses only, each tied to rows above:

- **The Motor is switched on its low side.** M+ sits on BAT+ permanently; U1 connects M− to GND to run the Motor. (Rows `M1.*`.)
- **Speed modes are PWM.** With one switch and no other parts in the path, the only practical way to give three Motor speeds is to switch M− on and off rapidly and vary the on-time. (Rows `M1.2`.)
- **D2 protects U1 from the Motor's switch-off spike.** A motor coil produces a voltage spike every time it's switched off, which PWM does thousands of times a second. D2 gives that current a path back to BAT+. (Rows `D2.*`.)
- **C3 suppresses brush noise.** Brushed motors spark at their brushes; a capacitor across the terminals absorbs that noise before it reaches U1. The 50 V rating covers the spikes. (Rows `C3.*`.)
