# Fix My Frother

Diagnosing and repairing a handheld, USB-C–rechargeable milk frother that stopped powering on after moisture got inside.

## Device

**Frother**:
The whole handheld device being repaired.
_Avoid_: Whisk, mixer, device

**Handle**:
The black outer housing with the button window and LED indicators.
_Avoid_: Body, shell, case

**End cap**:
The small oval cap that closes the motor end of the Handle.
_Avoid_: Bottom cover, lid

**Whisk**:
The removable steel rod with the spiral coil that goes into the milk.
_Avoid_: Frother head, spring, wand

## Internals

**Board**:
The `KD-F316-V1.0` circuit board carrying the USB-C port, button, LEDs, and the single chip that charges the Cell and drives the Motor.
_Avoid_: PCB, controller, circuit

**Cell**:
The single unprotected Li-ion cell (believed 14500) that powers the Frother.
_Avoid_: Battery

**Tab**:
One of the two metal strips spot-welded to the Cell and soldered to the Board's BAT+/BAT− pads.
_Avoid_: Terminal, lead, strip

**Motor**:
The small brushed DC motor that spins the Whisk.

**Coupler**:
The white plastic fitting on the Motor shaft that the Whisk plugs into.
_Avoid_: Adapter, socket

## Work

**Board study**:
The separate effort to trace, identify, and redraw the Board as a KiCad schematic in order to understand how it works.
_Avoid_: Teardown, reverse engineering, clone

## Use

**Speed mode**:
One of the Frother's three Motor speeds, changed by pressing the button in quick succession and shown by one lit dot; mode 1 is the slowest and the default at switch-on, mode 3 the fastest.
_Avoid_: Speed setting, speed level, gear

**Session**:
One frothing run of about 30 seconds; five consecutive Sessions on a full charge is the bar for calling the Frother fixed.
_Avoid_: Cycle, run
