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

"Fixed" means the original Frother running again: LEDs respond to the button, the Motor runs in all three Speed modes, it charges until the LEDs show full, and it completes **5 consecutive Sessions** on one charge. A multimeter, soldering iron, and isopropyl alcohol are on order; nothing past photography can start until they arrive.

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

## 2026-10-12: The Cell is dead

The multimeter arrived. The **Cell reads 0.0 V**, measured directly on its bare metal ends, and the reading was re-checked: meter on DC volts, probes in the right sockets, and the meter confirmed working on a known battery ([#5](https://github.com/robintomar1/fix_my_frother/issues/5)). The calliper confirms the Cell is **14 × 50 mm, a 14500** ([#3](https://github.com/robintomar1/fix_my_frother/issues/3)).

Under the safety rules (below 2.0 V: never charge), the Cell will be **replaced** with a pre-tabbed 14500 ([#6](https://github.com/robintomar1/fix_my_frother/issues/6)). That fits the likely cause: corrosion from rinse water leaking current until the Cell was completely flat.

Because a Li-ion cell rarely reaches a true 0 V on its own, the Board gets one extra check before the new Cell goes in: with the old Cell disconnected, resistance between the BAT+ and BAT− pads. Near 0 Ω would mean the Board itself is shorting the Cell and has to be fixed first.

Still to measure for the diagnosis: Motor resistance across M+/M−.

### Board photos and markings

New photos: the back of the Board ([1791776091833](../images/1791776091833.jpg), [1791776119984](../images/1791776119984.jpg)) is bare apart from the Cell, and rust is visible where the Tab bends round the Board's edge. Sharper close-ups of the front ([IMG_7909](../images/IMG_7909.jpg), [IMG_7911](../images/IMG_7911.jpg), [IMG_7912](../images/IMG_7912.jpg), [IMG_7913](../images/IMG_7913.jpg)) show the `BAT-` label, R2's `103` marking, D2's `M2` marking and cathode stripe, and a small circled "LN" logo on U1 with no part number. This completes the photo record for [#3](https://github.com/robintomar1/fix_my_frother/issues/3). R8 measured 5.07 kΩ in circuit, matching its `512` marking.

## 2026-10-12: The Cell is off the Board

The Cell has been removed from the Board. Measured on its own it reads **165 mV**, still far below the 2.0 V limit, so it stays a replacement ([#6](https://github.com/robintomar1/fix_my_frother/issues/6)). On the Board it read 0.0 V; the small rise once removed is consistent with the Board (or the corrosion) having been drawing on it, which the BAT+/BAT− short check will confirm or rule out.

With the Cell off and USB unplugged, the Board is now fully unpowered: the right moment for the short check, a clean Motor resistance reading, and the Board study meter checklists.

### Short across the Cell's pads

With the Cell off and USB unplugged, **BAT+ to BAT− reads about 3.6 Ω**, the same with the probes either way round. A healthy, idle Board should read thousands of ohms or more. 3.6 Ω would pull roughly 1 A from a full Cell, which explains how the Cell was drained to almost nothing.

Leading hypothesis: M− is stuck connected to GND, either U1's internal Motor switch has failed closed or corrosion bridges M− to ground, so the Motor's coil (a few ohms) sits permanently across the Cell. Being checked with M−↔BAT−, M+↔M− and M+↔BAT+ readings. **No new Cell goes in until the short is found and fixed.**

### Narrowing the short

The owner remembers the Frother **running on its own** one day before it died.

Readings (Cell off, USB unplugged):

| Between | Reading |
|---|---|
| M+ and BAT+ | 0 Ω (same connection, as expected) |
| M− and BAT− | 30–550 Ω, varying |
| M+ and M− (the Motor) | 80–500 Ω, varying |

The Motor path adds up to well over 100 Ω, so it **can't** explain the steady 3.6 Ω across BAT+/BAT−: there's a **separate short from BAT+ to BAT−**. Candidates: U1 failed internally, a cracked capacitor across the Cell's supply, or corrosion around U1.

Two more findings:
- **The Motor itself is suspect.** A healthy coil reads a few ohms; 80–500 Ω and unstable points to water-corroded brushes or commutator, consistent with the rust on its casing.
- **The leaky M−-to-ground path** (30–550 Ω) is one way the Motor could have run on its own; moisture across the button's pads is another.

Next: map each U1 pin to BAT+ and to BAT−, and measure across each capacitor, to locate the short.

### The short is at U1: pin 2 (Cell) to pin 8 (ground)

Measuring each U1 pin to BAT+ and BAT− (table in [u1-candidates.md](../hardware/board-study/u1-candidates.md#measured-so-far-2026-10-12)) shows **U1 pin 2 is the Cell connection (0.2 Ω to BAT+) and pin 8 is ground (0.0 Ω to BAT−)**, so the 3.6 Ω short sits between those two pins. Three possible culprits: U1 failed internally, C1 (at pin 2) cracked, or corrosion bridging the pads.

Plan to tell them apart: clean (#4) and re-measure; if still shorted, lift one end of C1 and re-measure; if it survives both, U1 has failed and the Board-fault path applies (search for a `KD-F316` replacement, else replace the Frother).

The same readings rule out three of the four U1 candidates; WD8001 remains consistent.

### C1 confirmed across the Cell; Board cleaned

C1's pads measure ≈0 Ω to BAT+ and to BAT− respectively, so C1 sits directly across the Cell's supply, in parallel with the short. In circuit it reads the same 3.6 Ω, which can't distinguish C1 from U1. The whole Board has been cleaned twice with isopropyl alcohol ([#4](https://github.com/robintomar1/fix_my_frother/issues/4)).

### USB power test: U1 heats up immediately

With the Cell removed, the Board was connected to USB. **U1 got hot immediately**; the Motor didn't spin and no LEDs lit. A healthy U1 with no Cell to charge and nothing to run should stay cool, so this strongly suggests **U1 has failed internally**, consistent with the 3.6 Ω between its Cell pin (2) and ground pin (8). A 5.9 MΩ BAT+/BAT− reading was taken with USB connected and is discarded (resistance needs the Board unpowered). USB stays disconnected from now on.

To confirm: re-measure BAT+/BAT− unpowered after cleaning; if still ~3.6 Ω, lift one end of C1 and re-measure. Still 3.6 Ω with C1 out means U1 is the failed part.

### Cleaning didn't clear the short

After cleaning twice and with USB disconnected, BAT+ to BAT− reads **about 3.0 Ω**, essentially the same short as before (3.6 Ω). Corrosion is ruled out; the culprit is C1 or U1. Lifting one end of C1 (next session) decides between them.
