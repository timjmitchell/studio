Source: https://help.uaudio.com/hc/en-us/articles/25351900668564-Monitor-Column
Updated: 2026-03-03T18:00:02Z

# Monitor Column

The Monitor Column is visible at the right side of the UAD Console window, when View > Section > Monitor is selected from the UAD Console menus. The Monitor Column contains elements related to monitor outputs, cue outputs, and insert effect printing.

**Important:** The Monitor column must be shown to view Auxes and/or the Control Room strip.

**Note:** Settings in the Monitor Column are global functions. They are not saved with individual UAD Console session files.

![monitor-column-callouts.png](https://help.uaudio.com/hc/article_attachments/31072789813780)

*The Monitor Column*

# Monitor Meters

The Monitor Meters display the levels of Apollo's monitor mix bus. Levels displayed here mirror the state of the Monitor 1 – 2 LED meters on Apollo.

These meters are before the monitor output level control (pre-fader) and reflect the level of the D/A converters at the monitor outputs.

**Important:** If clipping occurs, reduce levels feeding the monitor bus by lowering the channel faders and/or output gain(s) of UAD plug-ins within UAD Console to eliminate undesirable D/A clipping distortion.

## Separate UAD Console Output Meters Window

To open a separate larger, resizable UAD Console Output Meters window, click on the meters or the UA logo. To close the output meters window, click the X in its upper left corner.

**Tip:** Drag from the bottom right corner to change the height of the separate output meters window.

![](https://help.uaudio.com/hc/article_attachments/25351860734612)

## Meter Source

When the monitor output signals are changed with the [Monitor Output Options](#h_01HTREAF9F0MTT1KXRHHCAVT3C), the levels displayed by the monitor meters reflect the changed monitor outputs source signal.

### Monitor Level Scale

The numerical labels represent digital signal levels. "0" represents 0 dBFS (digital full scale, the maximum level before undesirable A/D clipping). If the level of the monitor bus exceeds 0 dBFS, the meter's clip indicator(s) illuminates.

### Peak Hold

The monitor meters also have a peak hold feature, which holds signal peak values for a specified period of time. The clip and peak hold times can be adjusted in Settings > Options.

# Show/Hide Strips

These switches show and hide the visibility of the auxiliary return strips and/or the control room options strip. By default, these strips are not visible. The strips are visible when a SHOW switch is lit.

|  |  |
| --- | --- |
| show-aux-ctrlrm-off.png | show-aux-ctrlrm-on.png |

*The SHOW switches off (left) and on (right)*

# Cue Outputs

# 

The Cue Outputs window is where the cue bus returns are configured. To open the Cue Outputs window, click the CUE OUTPUTS button in the Monitor Column. See [Cues](https://help.uaudio.com/hc/en-us/articles/25351037512340) for more information.

# Monitor Controller

![](https://help.uaudio.com/hc/article_attachments/31072798579604)

The Monitor Controller switch opens the Monitor Controller floating window, where you can configure Bass Management and access Speaker Utilities. See [Apollo X Bass Management](https://help.uaudio.com/hc/en-us/articles/30920209088404) for more information on Bass Management, and [Speaker Utilities](https://help.uaudio.com/hc/en-us/articles/36177324309140) for more information on the Monitor Controller window functions. Note that the Speaker Utilities function apply to stereo monitor mode and surround modes.

# Monitor Output Options

![](https://help.uaudio.com/hc/article_attachments/25351860744852)

Various monitor options are controlled with the switches in the OUTPUT section.

## ALT 1, ALT 2

When ALT monitoring is enabled in Settings > Hardware, ALT switches appear here to control which hardware outputs the monitor mix is routed to.

Apollo features ALT (alternate) monitoring capabilities. ALT monitoring can be used to control alternate pair(s) of monitor speakers, which is convenient for quickly comparing how a mix sounds through a different set of speakers. Up to two pairs of ALT monitors can be used (one pair with Apollo Twin).

ALT monitoring is enabled in Settings > Hardware by increasing the ALT Count setting to a non-zero value.

**Note:** ALT monitoring is not available on Apollo Solo, which only features one pair of outputs.

### ALT Monitor Connections

**Note:** The ALT channel output assignments cannot be modified.

**Apollo rack models and Apollo x4 –** The ALT 1 monitor signal is routed to line outputs 1-2, and the ALT 2 monitor signal is routed to line outputs 3-4.

**Apollo Twin –** The ALT monitor signal is routed to line outputs 3-4.

## ALT Monitor Select

![](https://help.uaudio.com/hc/article_attachments/25351900635028)

ALT selector

The ALT monitors are selected in the OUTPUT section of the Monitor Column. The number of ALT output switches that appear here depends on the ALT Count setting.

## ALT Monitor Volume & Mute

The monitor level knob adjusts the output volume and muting of both the ALT monitors and the main monitors.

## ALT Monitor Knob Color

![](https://help.uaudio.com/hc/article_attachments/25351900636436)

The colored ring around the Monitor Level knob indicates the active ALT selection, as shown at right.

**Green –** Main monitor outputs are active.

**Orange –** ALT 1 outputs are active.

**Yellow –** ALT 2 outputs are active.

## ALT Monitor Trims

![](https://help.uaudio.com/hc/article_attachments/25351860749076)

*ALT trims*

Each pair of ALT outputs has its own trim (gain) setting, which is used to offset any volume level differences with the volume level of the main monitor speakers.

As the monitor level is adjusted, these offsets are maintained so speakers can be accurately compared at any volume. The ALT trims are located in the Control Room Column.

**ALT Level –** Adjusts the output level of the main monitor mix when it is routed to a different pair of Apollo line outputs via the ALT monitoring function. The default value is 0 dB with an available range of ±30 dB.

**ALT Value –** The current ALT level value in dB is displayed.

## Monitor Mono

![](https://help.uaudio.com/hc/article_attachments/25351860752148)

This switch sums the left and right channels of the stereo monitor mix into a monophonic signal. The monitor output is stereo when the button is gray and mono when the button is lit.

## Monitor Mute

![](https://help.uaudio.com/hc/article_attachments/25351900640788)

This switch mutes Apollo's monitor outputs and stops monitor meters activity. The monitor outputs are muted when the switch is lit. This switch performs the same function as pressing the MONITOR knob on Apollo. The Monitor Level Indicator (the ring around the level knob) is red when the monitor outputs are muted.

# Monitor Level

This is the master level control for monitor outputs. It performs the same function as the MONITOR hardware knob. When the ring around the knob is RED, the monitor outputs are muted.

The specific monitor output attenuation value in dB is displayed beneath the Monitor Level control. The relative monitor output level is indicated by the colored ring around the Level control (as with the MONITOR knob's LED ring on Apollo).

## Adjusting and muting Monitor Level on macOS

You can use function keys to adjust Apollo's Monitor level and mute. The key combinations depend on a macOS setting. Note that system volume settings don't change with key commands when Apollo (Universal Audio Thunderbolt) is specified as the system sound driver.

Check this macOS setting:

MacOS System Settings > Keyboard > Keyboard Shortcuts > Function Keys > **Use F1, F2, etc. keys as standard function keys**

If this setting is **enabled**:

* Fn + F10: Mac  mute
* Fn + F11: Mac volume down
* Fn + F12: Mac volume up
* Cmd + F10: Apollo monitor mute
* Cmd + F11: Apollo monitor volume down
* Cmd + F12: Apollo monitor volume up

If this setting is **disabled**:

* F10: Mac  mute
* F11: Mac volume down
* F12: Mac volume up
* Cmd + Fn + F10: Apollo monitor volume mute
* Cmd + Fn + F11: Apollo monitor volume down
* Cmd + Fn + F12: Apollo monitor volume up

## Monitor Output Gain Bypass (Apollo 8, Apollo 8p, Apollo 16 MkII)

![](https://help.uaudio.com/hc/article_attachments/25351900643476)

*Monitor Output Gain bypassed*

When Monitor Output Gain in the Settings > Hardware is set to BYPASS, the Monitor Level Value field displays BYP, the monitor level cannot be adjusted, and ALT monitoring and assignable FCN switch features are disabled. For related details, see [Monitor Output Gain (Apollo 8, 8p, 16 MkII)](https://help.uaudio.com/hc/en-us/articles/25403573794836#h_01HTY5D6CW9ZW6JDY8NTSDDEDB).

## Monitor Level Indicator

In addition to indicating the relative signal level of the monitor outputs, the state of several other functions is indicated by the color of the ring around the monitor level control:

**Green –** The main monitor outputs are active with variable level control (normal).

**Green (fixed at maximum) –** Monitoring is bypassed in UAD Console Settings.

**Red –** The main monitor outputs (and ALT monitor outputs, if configured) are muted.

**Orange –** The ALT 1 monitor outputs are active.

**Yellow –** The ALT 2 monitor outputs are active.

**Flashing –** The monitor DIM, MONO, and/or TALKBACK functions are active.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

*Monitor level indications (from left to right): Normal, Bypass, Mute, ALT 1, ALT 2, and DIM/MONO*

## Apollo Twin Dot (Apollo Twin only)

![](https://help.uaudio.com/hc/article_attachments/25351860764180)

*Apollo Twin's MONITOR dot*

When the Monitor Level function is active on Apollo Twin's hardware (when its white MONITOR indicator is lit), a green dot is visible in UAD Console adjacent to the MONITOR text label, as circled in red.

The dot provides a visual indication that the MONITOR level adjust function is active on the Apollo Twin hardware. When the dot is not visible, adjusting Apollo Twin's hardware level knob will not adjust the monitor level, but instead adjusts preamp gain.

# Control Room Column

![control-room-column-callouts.png](https://help.uaudio.com/hc/article_attachments/27505319604884)

*Control Room column*

The control room column is where various options for the monitor outputs are configured and selected.

# Show Column

By default, the control room column is not visible. To show the column, enable the CTRL ROOM switch in the SHOW section of the monitor column, or choose View > Section > Control Room from the UAD Console menus.

**Tip:** When Apollo X Series and/or Apollo Twin MkII is connected and CTRL ROOM is enabled, the Talkback Input Strip is also visible. For complete Talkback details, see [Talkback](https://help.uaudio.com/hc/en-us/articles/26489966354836).

![](https://help.uaudio.com/hc/article_attachments/25351900650004)

*The Show CTRL ROOM switch in the monitor column*

# DIM Controls

DIM is used to quickly reduce the listening volume in the control room by a set amount and quickly return to the prior volume.

**DIM Amount –** This control adjusts the amount of attenuation level that is applied to the main monitor mix when the DIM switch is engaged. The available values are -9, -17 (default), -26, -34, -43, -51, and -60 dB.

**DIM Enable –** When engaged (lit), the monitor outputs (and ALT outputs, when active) are attenuated by the DIM Amount.

**Tip:** Press DIM quickly to latch the function. Press and hold DIM for 0.5 seconds to momentarily engage the function and deactivate DIM when the button is released.

# Monitor Source Select

These switches select the mix bus that is sent to Apollo's monitor outputs. The source is selected when its switch is lit.

## MIX

When MIX is selected, the main monitor mix, summed with any DAW outputs assigned monitor outputs (if applicable), is routed to the monitor outputs.

## Cue 1, 2, 3, 4 (Apollo rack models, Apollo x4)

When a CUE is selected, that cue mix (the mix created from cue sends in UAD Console), summed with any DAW outputs assigned to the cue (if applicable), is routed to the monitor outputs.

## HP, LINE 3/4 (Apollo Twin)

When HP or LINE 3/4 is selected, the respective cue mix, summed with any DAW outputs assigned to the respective HP or LINE 3/4 outputs (if applicable), is routed to the monitor outputs.

## HP (Apollo Solo)

When HP is selected, its cue mix, summed with any DAW outputs assigned to the respective HP outputs (if applicable), is routed to the monitor outputs.

## CUE INACTIVE Dialog

![](https://help.uaudio.com/hc/article_attachments/25351860769300)

CUE, HP, or LINE 3/4 can be selected as a monitor source only if its respective source in the Cue Outputs window is not set to MIX.

Allowing those settings would be the same as simply selecting MIX as the source with the monitor source switch, except that you wouldn't be able to determine the current cue routing without opening the cue outputs window.

If the CUE INACTIVE dialog appears when attempting to enable a cue as the monitor source:

1. Close the CUE INACTIVE dialog window by clicking OK.
2. Open the CUE OUTPUTS window by clicking its button in the Monitor Column.
3. Switch the cue source from MIX to an available CUE output.
