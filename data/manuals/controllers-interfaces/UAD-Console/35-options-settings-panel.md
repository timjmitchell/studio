Source: https://help.uaudio.com/hc/en-us/articles/25403715826836-Options-Settings-Panel
Updated: 2025-03-31T22:23:52Z

# Options Settings Panel

Various UAD Console options are set within the Options panel.

![](https://help.uaudio.com/hc/article_attachments/30985477523860)

*The Options panel*

# Metering

## Pre-Fader

When set to Pre-Fader, an input's Channel Meter indicates the level at the Apollo input, regardless of the Channel Fader setting. With this setting, changing the fader level will not change the Channel Meter.

**Tip:** When set to Pre-Fader, the Channel Meters mirror the signal level being recorded in the DAW.

## Post-Fader

When set to Post-Fader, changing an input's Channel Fader will change the Channel Meter.

**Note:** The Metering Menu affects the Channel Meters of UAD Console's channel inputs only. It does not affect the Aux Meters or the Monitor Meters.

# Clip/Peak Hold

**Tip:** The Clip and Peak indicators can be cleared at any time with the Clear Clips button.

## Clip Hold Time

This drop menu sets the duration that the red signal clip indicators in the input, send, and monitor meters are displayed before turning off. The available values are None, 1 second, 3 seconds (default), 5 seconds, 10 seconds, or Infinite.

## Peak Hold

This drop menu sets the duration that the signal peak indicators in the input and send meters are displayed before turning off. The available values are None, 1 second, 3 seconds (default), 5 seconds, and 10 seconds.

## Reset Dialogs

This button allows you to reset any dialogs where you have previously clicked "Don't Show Again".

![](https://help.uaudio.com/hc/article_attachments/30985477524756)

# Modifiers Timeout

This option sets the period, in seconds, used for Option Latch operations.

# Controls Mode

This setting determines how UAD plug-in parameter knobs respond to adjustment. Three control modes are offered: Circular, Relative Circular, and Linear. The behavior of each mode is described below.

**Tip**: This setting is also available in the Configuration panel within the UAD Meter & Control Panel application.

**Linear (slider) –** In Linear mode, the knob is adjusted by dragging horizontally or vertically instead of by rotating. This behavior is similar to moving a physical fader.

**Circular (jump) –** In Circular mode, the software knobs behave similar to physical rotary knobs. Values are changed by clicking on the knob then rotating in a circular direction. When the edge of the knob is clicked, the parameter value jumps to the mouse position.

**Relative Circular (grab) –** Relative Circular mode operates similar to Circular mode, but the knob value does not jump to the mouse position when clicked. Instead, the knob value is modified relative to its original value.

In Relative Circular mode, click anywhere on the knob to make an adjustment originating at the original value (it's not necessary to click on the current knob position).

**Tip:** To increase resolution when adjusting rotary controls in circular and relative circular modes, increase the radius of the mouse relative to the knob while dragging (move the mouse farther away from the knob while dragging in a circular motion).
