# U1 candidates

**Status: research only, nothing has been measured.** Part of the Board study: this file collects public information about chips that could be U1, the unmarked SOP-8 on the Board (`KD-F316-V1.0`). The meter decides what U1 is, in [#12](https://github.com/robintomar1/fix_my_frother/issues/12), not this file. No source found so far is a full manufacturer datasheet for the top candidate. Most evidence comes from distributor-hosted copies of vendor material (Sekorm) or from sales-rep blog posts (CSDN), and each claim below is labelled with which. A pin table marked **unconfirmed** must not be drawn into the schematic.

**Spot-checked 2026-10-11:**
- The CX3320 vendor page [13] confirms the SOP-8L package, the 8-bit OTP MCU, charging up to 600 mA, and Motor drive with stall protection. Its pin table is an image, so the table below is the research agent's reading of that image.
- The WD8001 behaviour post [3] confirms 40 / 70 / 100 % output, the 2 s Speed-mode window, LED4 as the charging light, and auto-off after 10 minutes.

**Behaviour that could tell them apart without a meter:**
- The owner's description matches WD8001's 2 s window: a press some time later turns the Frother off, and quick presses change Speed mode.
- Not known from memory (2026-10-11). Observe once the Frother works again; neither needs a meter:
  - [ ] **Auto-off:** run it for more than 10 minutes, Whisk in water. Does it stop on its own at about 10 minutes? (WD8001 does.)
  - [ ] **Charging light:** while charging (#6), does the first circle light, and does it go out when full? (WD8001's LED4 does.)

## Clues used

- **Package:** SOP-8, 1.27 mm pitch, unmarked. Pin 1 (dimple and dot) is on the USB-C-side row; pins 5–8 face the LEDs. An exposed pad (ESOP-8) can't be seen from the top, so ESOP-8 parts aren't excluded.
- **No inductor, no other IC, no discrete transistor.** U1 must charge the Cell linearly *and* switch the Motor itself. Any chip that needs a boost inductor is out.
- **Pin 1:** C2 (~0603) has a pad on it, which suggests a supply or VIN decoupling cap.
- **Pin 2:** C1 (~1206) has a pad near it, which suggests a VBAT/BAT cap.
- **Far row (pins 5–8):** R2 ("103", 10 kΩ?) and C4 sit beside it. R2 is a candidate charge-current-setting resistor.
- **R7 (1 kΩ):** runs from USB VBUS toward U1. It is too weak to carry charge current. R6 is a 0 Ω link that may carry it.
- **Behaviour:** one button. One press means on/off; quick repeat presses cycle the 3 Speed modes (mode 1 by default). The Motor is switched low-side, with D2 and C3 across its pads.
- **LEDs:** 4 blue LEDs. One is a "power" indicator; 3 dots show the Speed mode while running and the charge level while charging.

## Candidates

Ranked by overall fit. None fits every clue.

### 1. WD8001 (also sold as "WT32160"): milk-frother SoC. Best behavioural fit, pinout unconfirmed, no datasheet found

- **Vendor:** not identified. Every source is a CSDN post by a sales rep, and three rep accounts post near-identical text [1][2][3][6]. A fourth rep posts the same text word for word under the name **WT32160** [7], so these are probably two rebadges of one die.
- **Name clash:** one search result titles a different "WD8001" as a 5 V boost / 4-channel LED / 2S Li-ion chip [8] (title only; not opened). The part number alone is ambiguous.
- **Fit verdict:** the described behaviour matches the Frother almost exactly. The pinout comes only from a garbled list, and there is no datasheet.
- **Package:** ESOP-8 (exposed pad) [1][2].
- **Claimed function:** 8-bit OTP MCU with 1K ROM, a linear charger (trickle/CC/CV) and one 20 V power transistor for "motor and LED" [1][2].
  - Charge current is "110/350/500 mA" [1]. It's unclear whether that is set by a variant, an option or a resistor.
  - Sources disagree on the exact charge rate: one says 5 V/500 mA [3], another says 300 mA or 500 mA [30].
- **Claimed behaviour** [3][30]:
  - Battery-low cut-off at 2.7 V.
  - Speed modes run at 40 / 70 / 100 % output.
  - A press within 2 s steps the Speed mode; after 2 s a press turns the Motor off.
  - Auto-off after 10 min.
  - Three LEDs show charge level as M1 = 40 %, M2 = 70 %, M3 = 100 % [1].
  - A 4th LED ("LED4") is lit while charging and goes off when full [3]. Elsewhere it is called a "red" charging light [1].
  - Optional "shipping lock", unlocked by plugging in USB or by 6 presses within 3 s [6].
- **Reference board:** the rep's 3D render [1] shows the same general arrangement as ours: M−/M+ at one end, USB-C at the other, BAT+/BAT−, KEY1, LED1–LED4, and an SOP-8 U1 with C1–C4 and R1–R4.
  - It is **not the same PCB.** Compared with IMG_7895, U1 is rotated, the LEDs and button are in a different order, the Motor diode is SMA rather than SOD-123, and our Board has more resistors (R1–R9; R8/R9 sit near K1).
  - Boards for this kind of product are heavily templated, so the resemblance is weak evidence.
  - A minor coincidence: our silkscreen also sets LED4 apart from LED1–LED3, matching WD8001's use of "LED4" for the odd one out [3]. This is weak evidence too.
- **Pin list (unconfirmed, garbled):** two posts [4][5] list the pins below. The list numbers 10 pins for an 8-pin part, so the list is wrong somewhere; perhaps pin 9 is the exposed pad and "OUT" is mis-numbered.

| Pin | Name | Function as stated | Status |
|---|---|---|---|
| 1 | VIN | Supply input (USB 5 V) | unconfirmed |
| 2 | BAT | Cell + | unconfirmed |
| 3 | LED | LED (charge status) | unconfirmed |
| 4 | K | Button input | unconfirmed |
| 5 | AGND | Analogue ground | unconfirmed |
| 6, 7 | LED | More LEDs | unconfirmed |
| 8 ("8, 9") | GND | Ground (9 = exposed pad?) | unconfirmed |
| "10" | OUT | Motor output | unconfirmed; doesn't exist on an 8-pin part |

- **Fit for:**
  - Behaviour: 3 Speed modes with mode 1 as default, a single button, 3 dots doubling as a charge gauge, and a 4th LED. That makes 4 LEDs.
  - Topology: integrated charger and power switch, with no inductor.
  - Purpose: marketed specifically for milk frothers.
  - If the list is right: VIN on pin 1 (C2) and BAT on pin 2 (C1) match the cap positions.
- **Fit against:**
  - No datasheet; the pinout is self-contradictory.
  - The 4th LED is described as a *charging* indicator, and red [1][3]. Ours are all blue, and one is reportedly a power-on indicator.
  - No source says which pin, if any, takes a charge-setting resistor. R2's role isn't explained.
  - "1 transistor for motor *and* LED" doesn't say how 4 LEDs are driven.

### 2. CX3320 (诚芯微 / Shenzhen CXW Technology): OTP MCU, linear charger and Motor driver in one SOP-8. Pinout confirmed from vendor material

- **Fit verdict:** the architecture fits, since it is programmable and so could implement any Speed-mode or LED scheme. Pin-1 and R2 placement argue against it.
- **Source quality:** a Sekorm (authorised distributor) reprint of the vendor's product text, with the pin table and application circuit as images [13]. Sekorm also lists the full datasheet [14], but it sits behind a login and was not downloaded.
- **Package:** SOP-8L (no exposed pad stated).
- **Key specs** [13]:
  - 8-bit OTP MCU: 1K×13 ROM, 42 instructions, internal RC oscillator.
  - Linear charger up to 600 mA, set by a resistor on PR (typical app R3 = 2 kΩ), 4.23 V CV.
  - BAT pin max 700 mA.
  - VM− (motor low side) rated −0.3…+15 V, with stall protection at 2.2 A and short-circuit protection at 3.5 A.
  - Undervoltage protection at 3.0 V.
  - Input 4.5–5.5 V.
  - Internal signals IO0 (charge LED status) and IO5 (power switch) are on-die only.

| Pin | Name | Function (per vendor table [13]) |
|---|---|---|
| 1 | PR | Charge-current programming resistor to GND |
| 2 | BAT | Cell + (app: 1 µF to GND) |
| 3 | IO4 | Bidirectional I/O, wake-up; pull-up / open-drain |
| 4 | IO3/RST | I/O, wake-up; optional reset (active low) |
| 5 | IO2 | I/O, wake-up, counter input, PWM0 output |
| 6 | VCC/IO1 | Charge input (USB 5 V; app: 1 µF to GND); also readable as IO1 |
| 7 | GND | Ground |
| 8 | VM− | Motor low-side output (M+ to BAT+) |

- **Fit for:**
  - Low-side motor switch with a BAT pin, a USB VCC pin, and a charge resistor.
  - Needs only 2 caps, a resistor and a diode, which fits our part count.
  - Programmable, so 3 Speed modes by PWM and a charge gauge are possible.
  - BAT on pin 2 matches C1.
- **Fit against:**
  - Pin 1 is PR, which takes a *resistor*, but our pin 1 carries a cap pad (C2).
  - R2 sits on the far row (pins 5–8), but PR is pin 1.
  - Only 3 free I/Os (pins 3–5) must serve the button and 4 LEDs. That needs charlieplexing *and* sharing the button with an LED line, which is possible but tight.
  - Marketed for juicers, shavers and toothbrushes, not frothers.

### 3. CX3358B / CX3318B (CXW): fixed-function "motor-drive SoC" with charger and key detection. Pinouts confirmed; LED count doesn't fit

- **Fit verdict:** the charging, motor-drive and passive layout (VIN→1 kΩ→LED, ISET resistor on the far row) look right. But only one LED pin and fixed logic can't produce 3 Speed-mode dots.
- **Source quality:** Sekorm reprints of the vendor product text with pin tables and application circuits [9][10][12]. The datasheet PDF is listed [11] but sits behind a login.
- **CX3358B** [9][10]:
  - ESOP-8L, with the exposed pad as power ground.
  - Charge current up to 800 mA, set by R3 on ISENT (app 2 kΩ).
  - "Built-in 3-gear output control mode" and low-battery warning [9].
  - Stall protection at 2.2 A, short-circuit at 3.5 A.
  - The application circuit [9] puts **R1 = 1 kΩ from VIN to a red LED** into the LED pin, and a second LED via R2 = 470 Ω.
- **CX3318B** [12]:
  - SOP-8L, charge current up to 600 mA, set by PROG (app 2 kΩ).
  - Tactile-key mode; application R1 = 510 Ω, R2 = 100 Ω.

| Pin | CX3358B [9] | CX3318B [12] |
|---|---|---|
| 1 | VIN (charge input) | VM− (motor −) |
| 2 | LED (charge / work status) | PROG (charge-current R) |
| 3 | NC (must not be grounded) | SEL (GND = 1-cell) |
| 4 | KEY (tactile switch) | BAT |
| 5 | VM− (motor −) | VCC (charge input) |
| 6 | ISENT (charge-current R) | LED |
| 7 | SEL (GND = 1-cell) | KEY |
| 8 | VBAT+ | GND |
| EP | Power ground | none |

- **Fit for, CX3358B:**
  - VIN on pin 1 matches C2.
  - The charge-current resistor on pin 6 (far row) matches R2's position.
  - The vendor's 1 kΩ from VIN to an LED looks like our R7.
  - The low-side VM− matches.
  - "3 gears" is claimed.
- **Fit against:**
  - A single LED pin (two LEDs stacked from VIN) can't show a 3-dot Speed mode plus a power LED.
  - Pin 2 is LED, not a cap node (C1).
  - Fixed function: whether its "3-gear" mode is a press-to-cycle PWM is not stated.
- **CX3318B:** fits worse. Pin 1 is VM− and pin 2 is PROG, so neither of our cap clues fits.

### 4. SS8801 / SS8803 (Sinhmicro 昇生微, now under Southchip): power MCU with linear charger, SOP-8. Weak lead

- **Source:** vendor page [15]. It lists SS8801S08RC and SS8803S08RC in SOP8.
- **Features** [15]:
  - 12 KB OTP and a linear charger with "finely adjustable" voltage and current.
  - VIN rated to 14 V.
  - 6 PWM outputs that "can be bound together to raise drive capability".
  - Listed applications include egg beaters.
- **Fit against:** no integrated motor MOSFET is stated, so the Motor would need an external transistor, which the Board doesn't show. Pinout unknown: the brief datasheet requires a request form [15].

## Ruled out / insufficient

- **LP78070F** (ESOP8, fan chip): includes a DC-DC boost, so it needs an inductor, and the Board has none [17] (search summary).
- **FM5001L** (ESOP8, fan chip): boost with current limit, so it needs an inductor [18] (search summary).
- **FH8A150** (SOP8, fan chip): includes a "boost controller", so it needs an inductor [16].
- **PB1256A** (ESOP8): linear charger plus synchronous boost, so it needs an inductor [19].
- **SM5401** (SOP-8): power-bank charger plus boost, so it needs an inductor [20].
- **FH511:** sources conflict on package, SOT23-6 [21] vs. SOP8 [22], and the SOP8 listing says "boost". Unresolved and low priority.
- **TP4056 / TP4056X** (SOP-8): charger only [23].
- **TP4057** (SOT23-6): charger only, and the wrong package [24].
- **Padauk PFS154 / PFS173 / PMS150C:** MCU only, with no charger or power switch [25][26].
- **TC118S** (SOP-8): H-bridge motor driver only, with no charger or MCU [27] (lead).
- **CX3368:** MCU plus sonic-motor driver for toothbrushes, but SOP-16 per its listing [28] (search summary, not opened).
- **CX3319B** (SOP-8L): a CX3318B sibling built for a *latching slide switch*, not a tactile button [29]. Wrong input type.
- **Holtek, Sinowealth, Chipsea, FMD, Weltrend, SinoMCU, Unisonic, Nanjing Zhongke:** no all-in-one SOP-8 (charger, motor switch and MCU) turned up in searches. Their 8-pin MCUs would need a separate charger IC. Not exhaustively checked.

## Meter checks that tell them apart

Do these on the **unpowered** Board, with the BAT+ Tab unsoldered from the Board, so the Cell can't back-feed the meter readings. Record, for each U1 pin 1–8, every net it beeps to. Pins that beep to each other inside the chip are rare; diode-mode readings of 0.3–0.7 V between pins are normal, so judge only "beep (< ~30 Ω)" as a connection.

1. **Check pin 1** (confirms the orientation in [power-section.md](power-section.md)). Then, for each U1 pin, log its continuity to the reference points in steps 2–9.
2. **GND:** BAT− to each pin.
   - WD8001 predicts 5 and/or 8 (unconfirmed).
   - CX3320 predicts 7.
   - CX3358B predicts 7 (SEL), and ground through the exposed pad; check BAT− to the pad area if exposed.
   - CX3318B predicts 8 and 3.
3. **BAT+:** BAT+ pad to each pin.
   - WD8001: 2 (unconfirmed). CX3320: 2. CX3358B: 8. CX3318B: 4.
4. **Motor switch:** M− pad to each pin.
   - CX3320: 8. CX3358B: 5. CX3318B: 1. WD8001: unknown ("OUT").
   - If no pin beeps to M−, U1 doesn't switch the Motor directly. Look on the back for a transistor.
5. **USB input:** USB VBUS, both directly and through R6 (0 Ω), to each pin.
   - WD8001: 1. CX3320: 6. CX3358B: 1. CX3318B: 5.
6. **R7's U1-side end:** where does it go?
   - **Straight to a U1 pin:** a VIN-sense or supply input.
   - **To an LED's anode:** the CXW-style "VIN → 1 kΩ → charge LED → LED pin" arrangement, as in CX3358B [9]. In that case, check which U1 pin that LED's cathode reaches.
7. **Charge-current resistor:** measure R2 in circuit and note which U1 pin and which net (GND?) its two ends beep to.
   - CX3358B predicts pin 6 to GND. CX3320 predicts pin 1 to GND; CX3318B, pin 2 to GND.
   - If R2 sits between a far-row pin and GND, that favours CX3358B-type parts; CX3320 would need it on pin 1.
8. **Button:** find the pin the button's non-GND side beeps to.
   - WD8001: 4 (unconfirmed). CX3358B: 4. CX3318B: 7. CX3320: one of 3/4/5.
9. **LEDs:** for each LED pad, log which U1 pin(s), resistor or rail it beeps to.
   - **Primary test, continuity:** if *both* pads of an LED beep to U1 pins, rather than to GND, BAT+ or a resistor, that LED sits between two U1 pins, which is charlieplexing. This is the same method as in [button-led-section.md](button-led-section.md).
   - **Optional extra, diode mode:** probing pairs of U1 pins in both directions may make an LED glow faintly. Blue LEDs need about 2.7–3 V and many basic meters' diode test supplies less, so **no glow proves nothing.**
   - Expectation: a 3-pin charlieplex points to a programmable MCU (CX3320 or WD8001); one LED pin points to CX3358B/CX3318B.
10. **Score.** Count how many of steps 2–8 match each column. A candidate that misses on GND, BAT+, M− or VBUS is ruled out outright. If none matches, U1 is something not listed here; post the pin-role map to #12 and search again using it.

## Sources

1. https://blog.csdn.net/WD13729801557/article/details/148109665: CSDN, WD8001 sales-rep post with features and a 3D render of the reference board (lead; read via the r.jina.ai reader because CSDN blocks scripted fetches).
2. https://blog.csdn.net/WD13729801557/article/details/146567222: CSDN, WD8001 rep post with the feature list (lead).
3. https://blog.csdn.net/chunhui886/article/details/145062922: CSDN, WD8001 "function description" covering LED4 charge light, 2.7 V cut-off, 40/70/100 %, the 2 s window and 10 min auto-off (lead).
4. https://blog.csdn.net/chunhui886/article/details/145824108: CSDN, WD8001 pin list (garbled, 10 pins; lead).
5. https://blog.csdn.net/2401_82683268/article/details/145873977: CSDN, the same WD8001 pin list (lead).
6. https://blog.csdn.net/chunhui886/article/details/148633659: CSDN, WD8001 shipping-lock and unlock description (lead).
7. https://blog.csdn.net/ye15012777455/article/details/145010007: CSDN, "WT32160", word-for-word the same text as WD8001 (lead).
8. https://blog.csdn.net/weixin_41141180/article/details/145377833: CSDN title describing a different "WD8001" (boost, 4-LED, 2S); title only, not opened (lead).
9. https://www.sekorm.com/news/12115745.html: Sekorm, CX3358B vendor text with pin table, application circuit and notes (distributor copy of vendor material).
10. https://www.sekorm.com/news/39161327.html: Sekorm, CX3358 vendor text and electrical table (distributor copy).
11. https://www.sekorm.com/doc/523964227.html: Sekorm, CX3358 datasheet listing, V2.3 PDF (login required; not downloaded).
12. https://www.sekorm.com/news/51654796.html: Sekorm, CX3318B vendor text, pin table and application circuit (distributor copy).
13. https://www.sekorm.com/news/67505656.html: Sekorm, CX3320 vendor text, pin table, ratings and application circuit (distributor copy).
14. https://www.sekorm.com/doc/3601503.html: Sekorm, CX3320 datasheet listing (not downloaded).
15. http://sinhmicro.com/index.php/products/power_mcu/ss880x: Sinhmicro vendor page for SS880X, with ordering codes and features.
16. https://www.fansea.cn/h-nd-3274.html: Fansea distributor article on FH8A150.
17. https://www.sekorm.com/news/90293928.html: Sekorm article on LP78070F (seen as a search-result summary only).
18. https://www.btsemi.com/shownews.asp?id=510: distributor page for FM5001L (seen as a search-result summary only).
19. https://www.hotchip.com.cn/pb1256a/: vendor page for PB1256A (search summary).
20. http://www.szyucan.com/article_read_685.html: distributor page for SM5401 (search summary).
21. https://www.cnblogs.com/icaowu/p/17760871.html: blog listing FH511 (SOT23-6) and CX3318B (lead).
22. http://fansea.cn/h-nd-299.html: Fansea page titled "FH511 … boost chip SOP8"; the page didn't render (lead).
23. https://www.toppwr.com/uploadfile/file/20240125/65b1c4fd59b45.pdf: TOPPOWER TP4056X datasheet (manufacturer).
24. https://www.lcsc.com/product-detail/C5380674.html: LCSC page for TP4057S6 (distributor).
25. https://static.chipdip.ru/lib/540/DOC020540070.pdf: Padauk PFS154 datasheet (mirror of the manufacturer PDF).
26. https://wmsc.lcsc.com/wmsc/upload/file/pdf/v2/lcsc/1811301302_PADAUK-Tech-PFS173-S08_C337970.pdf: Padauk PFS173 datasheet (LCSC copy).
27. https://blog.csdn.net/fanhaidz/article/details/135202387: CSDN post on TC118S as a motor driver (lead).
28. https://blog.sina.com.cn/s/blog_16e0d96c40102z91g.html: Sina blog on CX3368 (search summary, lead).
29. https://www.sekorm.com/news/91233648.html: Sekorm, CX3319B vendor text (distributor copy).
30. https://blog.csdn.net/2401_82683268/article/details/145778068: CSDN, WD8001 "function analysis" covering 300/500 mA charging, the 2 s Speed-mode window and 10 min auto-off (lead; partly speculative wording by the rep).
