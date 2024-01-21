Documentation
=============

$0: Step pulse time in microseconds, min: 2.0

Sets time length per step. Minimum 2 microseconds.

*** DM542T requires 2.5 microseconds

This needs to be reduced from the default value of 10 when max. step rates exceed approximately 80 kHz.

$1: Step idle delay in milliseconds, max: 65535

Sets a short hold delay when stopping to let dynamics settle before disabling steppers. Value 255 keeps motors enabled.

*** 255

$2: Step pulse invert as axismask

Inverts the step signals (active low).

$3: Step direction invert as axismask

Inverts the direction signals (active low).

*** 2 (invert Y)

$4: Invert stepper enable pin(s) as axismask

Inverts the stepper driver enable signals. Most drivers uses active low enable requiring inversion.

NOTE: If the stepper drivers shares the same enable signal only X is used.

*** DM542T interprets enable as disable

$5: Invert limit pins as axismask

Inverts the axis limit input signals.

*** WM3020 needs all axes inverted

$6: Invert probe pin as boolean

Inverts the probe input pin signal.

$9: PWM Spindle as bitfield where setting bit 0 enables the rest:
    0 - Enable (1)
    1 - RPM controls spindle enable signal (2)

Enable controls PWM output availability.
When `RPM controls spindle enable signal` is checked and M3 or M4 is active S0 switches it off and S > 0 switches it on.

*** Needed

$10: Status report options as bitfield:
    0 - Position in machine coordinate (1)
    1 - Buffer state (2)
    2 - Line numbers (4)
    3 - Feed & speed (8)
    4 - Pin state (16)
    5 - Work coordinate offset (32)
    6 - Overrides (64)
    7 - Probe coordinates (128)
    8 - Buffer sync on WCO change (256)
    9 - Parser state (512)
    10 - Alarm substatus (1024)
    11 - Run substatus (2048)

Specifies optional data included in status reports.
If Run substatus is enabled it may be used for simple probe protection.

NOTE: Parser state will be sent separately after the status report and only on changes.

$11: Junction deviation in mm

Sets how fast Grbl travels through consecutive motions. Lower value slows it down.

$12: Arc tolerance in mm

Sets the G2 and G3 arc tracing accuracy based on radial error. Beware: A very small value may effect performance.

$13: Report in inches as boolean

Enables inch units when returning any position and rate value that is not a settings value.

$14: Invert control pins as bitfield:
    0 - Reset (1)
    1 - Feed hold (2)
    2 - Cycle start (4)
    6 - EStop (64)

Inverts the control signals (active low).
NOTE: Block delete, Optional stop, EStop and Probe connected are optional signals, availability is driver dependent.

*** 7

$15: Invert coolant pins as bitfield:
    0 - Flood (1)
    1 - Mist (2)

Inverts the coolant and mist signals (active low).

$16: Invert spindle signals as bitfield:
    0 - Spindle enable (1)
    1 - Spindle direction (2)
    2 - PWM (4)

Reboot required.

Inverts the spindle on, counterclockwise and PWM signals (active low).

NOTE: A hard reset of the controller is required after changing this setting.

$17: Pullup disable control pins as bitfield:
    0 - Reset (1)
    1 - Feed hold (2)
    2 - Cycle start (4)

Disable the control signals pullup resistors. Potentially enables pulldown resistor if available.
NOTE: Block delete, Optional stop and EStop are optional signals, availability is driver dependent.

$18: Pullup disable limit pins as axismask

Disable the limit signals pullup resistors. Potentially enables pulldown resistor if available.

$19: Pullup disable probe pin as boolean

Disable the probe signal pullup resistor. Potentially enables pulldown resistor if available.

$20: Soft limits enable as boolean

Enables soft limits checks within machine travel and sets alarm when exceeded. Requires homing.

*** Enabled

$21: Hard limits enable as bitfield where setting bit 0 enables the rest:
    0 - Enable (1)
    1 - Strict mode (2)

*** Strict mode

When enabled immediately halts motion and throws an alarm when a limit switch is triggered. In strict mode only homing is possible when a switch is engaged.

$22: Homing cycle as bitfield where setting bit 0 enables the rest:
    0 - Enable (1)
    1 - Enable single axis commands (2)
    2 - Homing on startup required (4)
    3 - Set machine origin to 0 (8)
    4 - Two switches shares one input pin (16)
    5 - Allow manual (32)
    6 - Override locks (64)
    7 - Keep homed status on reset (128)

Enables homing cycle. Requires limit switches on axes to be automatically homed.

When `Enable single axis commands` is checked, single axis homing can be performed by $H<axis letter> commands.

When `Allow manual` is checked, axes not homed automatically may be homed manually by $H or $H<axis letter> commands.

`Override locks` is for allowing a soft reset to disable `Homing on startup required`.

*** 1+2+4+8

$23: Homing direction invert as axismask

Homing searches for a switch in the positive direction. Set axis bit to search in negative direction.

*** 1+2 (invert X and Y)

$24: Homing locate feed rate in mm/min

Feed rate to slowly engage limit switch to determine its location accurately.

$25: Homing search seek rate in mm/min

Seek rate to quickly find the limit switch before the slower locating phase.

*** 1000

$26: Homing switch debounce delay in milliseconds

Sets a short delay between phases of homing cycle to let a switch debounce.

$27: Homing switch pull-off distance in mm

Retract distance after triggering switch to disengage it. Homing will fail if switch isn't cleared.

*** 3 seems to be reliable, 1 is too little

$28: G73 Retract distance in mm

G73 retract distance (for chip breaking drilling).

$29: Pulse delay in microseconds, max: 10

Step pulse delay.

Normally leave this at 0 as there is an implicit delay on direction changes when AMASS is active.

$30: Maximum spindle speed in RPM

Maximum spindle speed, can be overridden by spindle plugins.

*** G-Penny spindle max 24000 RPM

$31: Minimum spindle speed in RPM

Minimum spindle speed, can be overridden by spindle plugins.

*** G-Penny spindle min 15000 RPM

$32: Mode of operation:
    0 - Normal
    1 - Laser mode
    2 - Lathe mode

Laser mode: consecutive G1/2/3 commands will not halt when spindle speed is changed.
Lathe mode: allows use of G7, G8, G96 and G97.

$33: Spindle PWM frequency in Hz

Spindle PWM frequency.

$34: Spindle PWM off value in percent, max: 100

Spindle PWM off value in percent (duty cycle).

$35: Spindle PWM min value in percent, max: 100

Spindle PWM min value in percent (duty cycle).

$36: Spindle PWM max value in percent, max: 100

Spindle PWM max value in percent (duty cycle).

$37: Steppers deenergize as axismask

Specifies which steppers not to disable when stopped.

$39: Enable legacy RT commands as boolean

Enables "normal" processing of ?, ! and ~ characters when part of $-setting or comment. If disabled then they are added to the input string instead.

$40: Limit jog commands as boolean

Limit jog commands to machine limits for homed axes.

*** Sound as a good idea

$43: Homing passes, range: 1 - 128

Number of homing passes. Minimum 1, maximum 128.

$44: Axes homing, first pass as axismask

Axes to home in first pass.

*** Home all at once

$45: Axes homing, second pass as axismask

Axes to home in second pass.

$46: Axes homing, third pass as axismask

Axes to home in third pass.

$62: Sleep enable as boolean

Enable sleep mode.

$63: Feed hold actions as bitfield:
    0 - Disable laser during hold (1)
    1 - Restore spindle and coolant state on resume (2)

Actions taken during feed hold and on resume from feed hold.

$64: Force init alarm as boolean

Starts Grbl in alarm mode after a cold reset.

$65: Probing feed override as boolean

Allow feed override during probing.

$100: X-axis travel resolution in step/mm

Travel resolution in steps per millimeter.

$101: Y-axis travel resolution in step/mm

Travel resolution in steps per millimeter.

$102: Z-axis travel resolution in step/mm

Travel resolution in steps per millimeter.

*** 508 @ 2000 pulses/rev

$110: X-axis maximum rate in mm/min

Maximum rate. Used as G0 rapid rate.

*** 2000

$111: Y-axis maximum rate in mm/min

Maximum rate. Used as G0 rapid rate.

*** 2000

$112: Z-axis maximum rate in mm/min

Maximum rate. Used as G0 rapid rate.

*** 1000

$120: X-axis acceleration in mm/sec^2

Acceleration. Used for motion planning to not exceed motor torque and lose steps.

*** 50

$121: Y-axis acceleration in mm/sec^2

Acceleration. Used for motion planning to not exceed motor torque and lose steps.

*** 50

$122: Z-axis acceleration in mm/sec^2

Acceleration. Used for motion planning to not exceed motor torque and lose steps.

*** 10

$130: X-axis maximum travel in mm

Maximum axis travel distance from homing switch. Determines valid machine space for soft-limits and homing search distances.

*** WM3020 290 mm

$131: Y-axis maximum travel in mm

*** WM3020 220 mm

Maximum axis travel distance from homing switch. Determines valid machine space for soft-limits and homing search distances.

$132: Z-axis maximum travel in mm

Maximum axis travel distance from homing switch. Determines valid machine space for soft-limits and homing search distances.

*** WM3020 70 mm

$341: Tool change mode:
    0 - Normal
    1 - Manual touch off
    2 - Manual touch off @ G59.3
    3 - Automatic touch off @ G59.3
    4 - Ignore M6

Normal: allows jogging for manual touch off. Set new position manually.

Manual touch off: retracts tool axis to home position for tool change, use jogging or $TPW for touch off.

Manual touch off @ G59.3: retracts tool axis to home position then to G59.3 position for tool change, use jogging or $TPW for touch off.

Automatic touch off @ G59.3: retracts tool axis to home position for tool change, then to G59.3 position for automatic touch off.

All modes except "Normal" and "Ignore M6" returns the tool (controlled point) to original position after touch off.

$342: Tool change probing distance in mm

Maximum probing distance for automatic or $TPW touch off.

$343: Tool change locate feed rate in mm/min

Feed rate to slowly engage tool change sensor to determine the tool offset accurately.

$344: Tool change search seek rate in mm/min

Seek rate to quickly find the tool change sensor before the slower locating phase.

$345: Tool change probe pull-off rate in mm/min

Pull-off rate for the retract move before the slower locating phase.

$346: Restore position after M6 as boolean

When set the spindle is moved so that the controlled point (tool tip) is the same as before the M6 command, if not the spindle is only moved to the Z home position.

$370: Invert I/O Port inputs as bitfield:
    0 - Aux 0 (1)

Invert IOPort inputs.

$384: Disable G92 persistence as boolean

Disables save/restore of G92 offset to non-volatile storage (NVS).

$398: Planner buffer blocks, range: 30 - 1000, reboot required

Number of blocks in the planner buffer.

NOTE: A hard reset of the controller is required after changing this setting.

$481: Autoreport interval in ms, range: 100 - 1000, reboot required

Interval the real time report will be sent, set to 0 to disable.

NOTE: A hard reset of the controller is required after changing this setting.

$486: Lock coordinate systems as bitfield:
    0 - G59.1 (1)
    1 - G59.2 (2)
    2 - G59.3 (4)

Lock coordinate systems against accidental changes.


Changed
=======

$0=5
$1=255
$3=2
$4=7
$5=7
$9=3
$10=511
$14=70
$20=1
$21=3
$22=15
$23=3
$25=1000
$27=3
$30=24000
$31=15000
$40=1
$44=7
$100=400
$101=400
$102=400
$110=2000
$111=2000
$112=1000
$120=50
$121=50
$122=10.000
$130=290
$131=220
$132=70
