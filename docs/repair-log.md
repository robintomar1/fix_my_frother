# Repair log

The story of repairing the Frother, newest entries at the bottom. Terms are defined in [`CONTEXT.md`](../CONTEXT.md); the full plan is the spec in [#1](https://github.com/robintomar1/fix_my_frother/issues/1).

Each repair step is its own GitHub issue (a sub-issue of #1). When a step is done, add a dated entry here that says what was done and found, and links to that step's issue. Measurements and photos go in the issue comments; this log tells the story.

## Care note

Moisture inside the Handle is what most likely killed the Frother. To stop it happening again:

- Rinse **only the Whisk**.
- Keep water away from the Motor shaft and the **End cap**.

## Safety rules

These apply to every step that touches the Cell, an unprotected Li-ion cell:

- **No charging before the Cell voltage has been measured** with a multimeter.
- **Cell voltage limits:**

  | Cell reading | Action |
  |---|---|
  | 3.0 V or more | Charge normally |
  | 2.5–3.0 V | Charge; stay with it for the first 30 minutes, checking for warmth |
  | 2.0–2.5 V | **One** attended recovery charge; replace the Cell if it gets warm or doesn't exceed 3.0 V within 30 minutes |
  | Below 2.0 V | **Never charge.** Replace with a pre-tabbed Cell of the confirmed size |

- **Every charge** is attended, on a tile or metal tray. Unplug at the first sign of warmth, a smell, or swelling.
- **Soldering heat goes only into the Tabs**, at the Board end, never into the Cell itself.
- A dead Cell goes to battery recycling, not household trash.

---

## 2026-10-11: Fault, disassembly, and plan

### The fault

The Frother was last known working about two weeks ago. On 2026-10-10 it did nothing at all when the button was pressed: **no LEDs, no Motor**. It is routinely rinsed after frothing.

### Disassembly findings

The Handle was opened and the internals slid out on their frame. Photos:

| Photo | Shows |
|---|---|
| [IMG_7890](../images/IMG_7890.jpg) | Handle with the internals partly out, the Whisk, and the End cap with grime inside it |
| [IMG_7891](../images/IMG_7891.jpg) | Board front in the frame, Motor below |
| [IMG_7892](../images/IMG_7892.jpg), [IMG_7893](../images/IMG_7893.jpg) | Back of the frame, Motor and Coupler |
| [IMG_7894](../images/IMG_7894.jpg) | Cell on the back of the Board, frame removed |
| [IMG_7895](../images/IMG_7895.jpg) | Board front close-up, markings readable |
| [IMG_7896](../images/IMG_7896.jpg) | Tab at the Motor end of the Cell, brown corrosion |
| [IMG_7897](../images/IMG_7897.jpg) | Tab at the USB-C end of the Cell, rust where it meets the Board |
| [IMG_7898](../images/IMG_7898.jpg), [IMG_7899](../images/IMG_7899.jpg) | Board front at an angle |

What the photos show:

- **Board** marked `KD-F316-V1.0`, dated 2025-04-09, maker 康图电器. It carries the USB-C port, button K1, LED1–LED4, a single unmarked 8-pin chip U1, resistors R1–R9, capacitors C1–C4, D2 and C3 near the Motor pads, and pads BAT+/BAT− and M+/M−.
- **Cell**: a single unprotected Li-ion cell, believed to be a 14500 (size not yet measured), with two Tabs spot-welded to the Cell and soldered to the Board.
- **Corrosion**: rust and brown residue on **both Tabs** where they meet the Board, a rust patch on the Motor's metal casing ([IMG_7894](../images/IMG_7894.jpg)), and grime inside the End cap.
- **Motor**: a small brushed DC motor with the white Coupler on its shaft.

### Likely cause

Rinse water got in around the Motor shaft and corroded the Tabs. Two possible faults, which may both be true:

1. The corroded Tabs no longer connect the Cell to the Board, so the Board gets no power.
2. The Cell has drained itself flat, through leakage across the corrosion, below the level the Board will charge it from.

Preventing this in future is down to how the Frother is rinsed (see the care note), not a hardware change.

### The plan

"Fixed" means the original Frother running again: LEDs respond to the button, the Motor runs at every speed setting, it charges until the LEDs show full, and it completes **5 consecutive Sessions** on one charge. A multimeter, soldering iron, and isopropyl alcohol are on order; nothing past photography can start until they arrive.

| Step | Issue |
|---|---|
| Start this log | [#2](https://github.com/robintomar1/fix_my_frother/issues/2) |
| Photograph the Board before cleaning, and measure the Cell | [#3](https://github.com/robintomar1/fix_my_frother/issues/3) |
| Clean the corrosion and dry for 24 hours or more | [#4](https://github.com/robintomar1/fix_my_frother/issues/4) |
| Diagnose: Cell voltage → BAT+/BAT− → USB-C 5 V → M+/M− resistance | [#5](https://github.com/robintomar1/fix_my_frother/issues/5) |
| Recover or replace the Cell | [#6](https://github.com/robintomar1/fix_my_frother/issues/6) |
| Repair the Tabs | [#7](https://github.com/robintomar1/fix_my_frother/issues/7) |
| Acceptance: reassemble and run 5 Sessions | [#8](https://github.com/robintomar1/fix_my_frother/issues/8) |

If diagnosis finds the Motor is dead, it gets a same-size replacement. If the Board is dead, a `KD-F316` replacement is searched for, and the Frother is replaced if none turns up.

Separately, the **Board study** ([#9](https://github.com/robintomar1/fix_my_frother/issues/9)–[#12](https://github.com/robintomar1/fix_my_frother/issues/12)) traces the Board and redraws it as a KiCad schematic, to understand how it works. It doesn't hold up the repair, but moves to the front of the queue if the Board turns out to be the fault.
