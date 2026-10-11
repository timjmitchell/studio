Source: https://help.uaudio.com/hc/en-us/articles/26817449653012-Apollo-X-Surround-Sound
Updated: 2025-04-01T17:00:02Z

# Apollo X Surround Sound

# Create Professional Immersive Audio Mixes

Surround sound is multi-channel audio output that expands on the basic two-channel stereo format. Surround sound with Apollo X is a hardware and software operating mode that is configured within Console. When enabled, Apollo X and Console output features are optimized for the surround environment.

Use Apollo x16 as your all-in-one monitoring hub for mixing formats up to 9.1.6, and easily create 16-channel immersive audio mixes for Dolby Atmos, Auro-3D, Sony 360 Reality Audio, and others.

**Note:** Surround functionality is available with Apollo X rack models only.

## Surround Features

* Eleven available surround modes, up to 9.1.6 channels (up to 5.1 with Apollo x6, up to 7.1 with Apollo x8/x8p, up to 9.1.6 with Apollo x16)
* Control all surround output channel levels simultaneously with Monitor knob
* Monitor knob can be calibrated to absolute dB SPL values
* Surround output channel metering in Console and front panel hardware LEDs
* SMPTE channel ordering eliminates re-patching when changing surround modes
* Individual surround channel offset trim controls for speaker calibration
* Individual surround channel solo and mute controls
* Automatic Core Audio/ASIO surround channel naming and reordering

# Operational Changes

When any surround mode is active, the following Apollo X and Console behaviors are changed from the standard (stereo mode) behavior. These behaviors are explained in greater detail later in this chapter.

**Monitor Mode Menu –** When an Apollo X is recognized, the menu for selecting surround formats appears in the Hardware panel within the Console Settings window.

**Monitor Control –** All surround output channels are simultaneously controlled with Apollo’s front panel hardware Monitor knob and/or the Monitor controls within Console.

**Monitor Controller Window –** Individual surround channel output offset trims, bass management features, and the overall SPL (sound pressure level) are calibrated within this window. This window also provides access to individual surround channel solo and mute controls.

**Calibrated SPL Monitor Level –** Console’s monitor output level is optionally displayed as a calibrated dB SPL (instead of -dBFS value below full output).

**Surround Channel Metering –** The output level of each surround channel is displayed in Console’s Monitor column, in the Console Output Meters window, and optionally on the front panel of Apollo X.

**Fold Down –** Stereo and Mono fold down options in Console’s Monitor Column enable quick switching between full surround and collapsed monitoring.

**I/O Matrix –** Surround output channel and name assignments in Console Settings are automatically updated when a surround mode is activated.

# Hardware Settings

## SMPTE Channel Ordering

Apollo X surround sound uses standard SMPTE output channel ordering. With SMPTE output channel ordering, output channel assignments to each surround speaker remain the same in the various monitor modes.

This feature facilitates the ability to switch between surround formats without having to re-patch physical outputs to the surround speakers. For example, the subwoofer is always assigned to the Line 2 output, regardless of the selected surround mode.

### SMPTE Channels

The SMPTE channel ordering output assignments are shown in the table below. Connect each surround speaker to the physical Apollo X output shown in the table.

**Note:** Analog Line Out 15-16 (Apollo x16) are assigned as Alt L (15) and Alt R (16) outs in Dolby Atmos (5.14, 7.1.4, 9.1.6) modes.

|  |  |  |  |
| --- | --- | --- | --- |
| **APOLLO OUTPUTS** | **SMPTE CHANNEL** **ASSIGNMENTS** | **APOLLO OUTPUTS** | **SMPTE CHANNEL** **ASSIGNMENTS** |
| MON L | L |  |  |
| MON R | R |  |  |
| LINE 1 | C | LINE 9 | Ltr |
| LINE 2 | LFE | LINE 10 | Rtr |
| LINE 3 | Ls, S, Lrs, Lss | LINE 11 | Lw |
| LINE 4 | Rs, Rrs, Rss | LINE 12 | Rw |
| LINE 5 | Cs, Lss, Lrs | LINE 13 | Ltm |
| LINE 6 | Rss, Rrs | LINE 14 | Rtm |
| LINE 7 | Ltf | LINE 15 | ALT L |
| LINE 8 | Rtf | LINE 16 | ALT R |

The standard SMPTE channel output assignments in all surround modes.  
Some channel assignments differ with expanded (beyond 7.1) modes.

## Monitor Modes & Channel Assignments

All available surround modes and their speaker channel assignments are shown in the tables below. Note that due to standard SMPTE channel ordering, the speaker assignment for each physical output channel is essentially the same within a single column.

**Note:** SUB speaker assignment as indicated in the tables below is for Stereo mode with [Apollo X Bass Management](https://help.uaudio.com/hc/en-us/articles/30920209088404).

### Apollo x6 surround modes and channel assignments

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Mode** | **Analog Mon outputs** | | **Analog line outputs** | | | | | |
|  | MON L | MON R | 1 | 2 | 3 | 4 | 5 | 6 |
| Stereo | L | R | ALT L | ALT R | ALT 2 L | ALT 2 R |  | **SUB** |
| 2.1 | L | R | -- | LFE |  |  | ALT L | ALT R |
| LCR | L | R | C |  |  |  | ALT L | ALT R |
| LCRS | L | R | C | -- | S |  | ALT L | ALT R |
| QUAD | L | R | -- | -- | Ls | Rs | ALT L | ALT R |
| 5.1 | L | R | C | LFE | Ls | Rs | ALT L | ALT R |

### Apollo x8/x8p surround modes and channel assignments

|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Mode** | **Analog Mon outputs** | | **Analog line outputs** | | | | | | | |
|  | MON L | MON R | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| Stereo | L | R | ALT L | ALT R | ALT 2 L | ALT 2 R |  |  |  | **SUB** |
| 2.1 | L | R | -- | LFE |  |  |  |  | ALT L | ALT R |
| LCR | L | R | C |  |  |  |  |  | ALT L | ALT R |
| LCRS | L | R | C | -- | S |  |  |  | ALT L | ALT R |
| QUAD | L | R | -- | -- | Ls | Rs |  |  | ALT L | ALT R |
| 5.1 | L | R | C | LFE | Ls | Rs |  |  | ALT L | ALT R |
| 6.1 | L | R | C | LFE | Ls | Rs | Cs |  | ALT L | ALT R |
| 7.1 | L | R | C | LFE | Lrs | Rrs | Lss | Rss | ALT L | ALT R |

### Apollo x16 surround modes and channel assignments

|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Monitor mode** | **Analog Mon outputs** | | **Output channel assignments (Mon-Line 8)** | | | | | | | |
|  | MON L | MON R | LINE 1 | LINE 2 | LINE 3 | LINE 4 | LINE 5 | LINE 6 | LINE 7 | LINE 8 |
| Stereo | L | R | ALT L | ALT R | ALT 2 L | ALT 2 R |  |  |  | **SUB** |
| 2.1 | L | R | – | LFE |  |  |  |  |  |  |
| LCR | L | R | C |  |  |  |  |  |  |  |
| LCRS | L | R | C | – | S |  |  |  |  |  |
| QUAD | L | R | – | – | Ls | Rs |  |  |  |  |
| 5.1 | L | R | C | LFE | Ls | Rs |  |  |  |  |
| 6.1\* | L | R | C | LFE | Ls | Rs | Cs |  |  |  |
| 7.1\* | L | R | C | LFE | Lrs | Rrs | Lss | Rss |  |  |
| 5.1.4† | L | R | C | LFE | Ls | Rs | – | – | Ltf | Rtf |
| 7.1.4† | L | R | C | LFE | Lss | Rss | Lrs | Rrs | Ltf | Rtf |
| 9.1.6† | L | R | C | LFE | Lss | Rss | Lrs | Rrs | Ltf | Rtf |

### 

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Mode** | **Output channel assignments (9-16)** | | | | | | | |
|  | LINE 9 | LINE 10 | LINE 11 | LINE 12 | LINE 13 | LINE 14 | LINE 15 | LINE 16 |
| Stereo |  |  |  |  |  |  |  |  |
| 2.1 |  |  |  |  |  |  | ALT L | ALT R |
| LCR |  |  |  |  |  |  | ALT L | ALT R |
| LCRS |  |  |  |  |  |  | ALT L | ALT R |
| QUAD |  |  |  |  |  |  | ALT L | ALT R |
| 5.1 |  |  |  |  |  |  | ALT L | ALT R |
| 6.1\* |  |  |  |  |  |  | ALT L | ALT R |
| 7.1\* |  |  |  |  |  |  | ALT L | ALT R |
| 5.1.4† | Ltr | Rtr |  |  |  |  | ALT L | ALT R |
| 7.1.4† | Ltr | Rtr |  |  |  |  | ALT L | ALT R |
| 9.1.6† | Ltr | Rtr | Lw | Rw | Ltm | Rtm | ALT L | ALT R |

### Apollo x16D surround modes and channel assignments

Apollo x16D uses the following monitor and channel assignments. In most cases (unlike other Apollo devices), the ALT monitor outputs are on the MON L/R outputs.

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Mode** | **Analog Mon outputs** | **Dante outputs 1-8** | | | | | | | |
|  | MON L/R | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| Stereo | L/R | ALT L | ALT R | ALT 2 L | ALT 2 R |  |  |  | **SUB** |
| 2.1 | ALT L/R | L | R | – | LFE |  |  |  |  |
| LCR | ALT L/R | L | R | C |  |  |  |  |  |
| LCRS | ALT L/R | L | R | C | – | S |  |  |  |
| QUAD | ALT L/R | L | R | – | – | Ls | Rs |  |  |
| 5.1 | ALT L/R | L | R | C | LFE | Ls | Rs |  |  |
| 6.1 | ALT L/R | L | R | C | LFE | Ls | Rs | Cs |  |
| 7.1 | ALT L/R | L | R | C | LFE | Lrs | Rrs | Lss | Rss |
| 5.1.4 | ALT L/R | L | R | C | LFE | Ls | Rs | – | – |
| 7.1.4 | ALT L/R | L | R | C | LFE | Lss | Rss | Lrs | Rrs |
| 9.1.6 | ALT L/R | L | R | C | LFE | Lss | Rss | Lrs | Rrs |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Mode** | **Dante Outputs 9-16 (cont'd)** | | | | | | | |
|  | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 |
| Stereo |  |  |  |  |  |  |  |  |
| 2.1 |  |  |  |  |  |  |  |  |
| LCR |  |  |  |  |  |  |  |  |
| LCRS |  |  |  |  |  |  |  |  |
| QUAD |  |  |  |  |  |  |  |  |
| 5.1 |  |  |  |  |  |  |  |  |
| 6.1 |  |  |  |  |  |  |  |  |
| 7.1 |  |  |  |  |  |  |  |  |
| 5.1.4 | Ltf | Rtf | Ltr | Rtr |  |  |  |  |
| 7.1.4 | Ltf | Rtf | Ltr | Rtr |  |  |  |  |
| 9.1.6 | Ltf | Rtf | Ltr | Rtr | Lw | Rw | Ltm | Rtm |

## Hardware Surround Metering

Surround levels are displayed on the LEDs on the front panel of the Apollo X rack hardware when the meters are set to OUT via the METER button on the front panel.

On the hardware, the output LED meters always reflect signal levels at their associated physical outputs, and the physical outputs always use the SMPTE channel ordering, regardless of the active surround mode. Therefore the hardware MONITOR meters always display L and R levels, the Line 1 meter always displays the Center level, Line 2 always displays the LFE/SUB level, and so forth, according to the SMPTE channel ordering.

### Surround Channel Alignment

Because of standard SMPTE channel ordering, the 2.1, LCRS, QUAD, and 5.1.4 surround modes have non-surround channels between the surround channels. These non-surround channels are indicated by dashes (–) in the Monitor Modes & Channel Assignments table.

When 2.1, LCRS, QUAD, or 5.1.4 surround modes are active, the non-surround channel(s) between the surround channels is automatically placed after the surround channels at the driver level. This feature allows all of the surround channels to exist in consecutive order within the DAW without having to re-patch physical outputs.

The output channel assignments for the 2.1, LCRS, QUAD, and 5.1.4 surround modes are shown in the tables below. The channels where Line 1 and Line 2 would normally appear are modified as needed (shown with red highlight) so the surround mode channels are adjacent in the DAW.

**Note:** These assignments are identical to those in the Monitor Modes & Channel Assignments table. The tables below simply illustrate how those assignments appear within the DAW for these surround modes.

### 2.1 output channel ordering

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MON L | MON R | LINE 2 | LINE 1 | LINE 3 | LINE 4 | LINE 5 | LINE 6 |
| L | R | SUB |  |  |  |  |  |

### LCRS output channel ordering

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MON L | MON R | LINE 1 | LINE 3 | LINE 2 | LINE 4 | LINE 5 | LINE 6 |
| L | R | C | S |  |  |  |  |

### QUAD output channel ordering

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MON L | MON R | LINE 3 | LINE 4 | LINE 1 | LINE 2 | LINE 5 | LINE 6 |
| L | R | Ls | Rs |  |  |  |  |

### 5.1.4 output channel ordering

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MON L | MON R | LINE 3 | LINE 4 | LINE 1 | LINE 2 | LINE 5 | LINE 6 |
| Ltf | Rtf | Ltr | Rtr |  |  |  |  |

# Software Settings

## Monitor Mode Menu

![](https://help.uaudio.com/hc/article_attachments/26909491238292)

Surround is activated by choosing any surround mode (other than STEREO) from the Monitor Mode menu in the Hardware Settings Panel within the Console Settings window, as shown at right.

**Caution****:** Lower speaker volumes before reducing the surround mode to a mode with fewer output channels. When the surround mode is switched to a mode with fewer channels, the channels that are released from monitor control switch to full volume.

### Monitor Mode Notes

* The Monitor Mode menu is available only when one or more Apollo X is recognized.
* In a multi-unit configuration, the Monitor Mode menu is available only when Apollo X has the Monitor Unit Designation. One unit must be designated as the monitor unit. Monitor speakers are attached to the monitor unit only. All other units are expander units.
* Headphone and cue outputs can be assigned to any leader or follower unit. However, mirrored cues can be routed to the monitor unit only.

## Monitor Controller Window

![](https://help.uaudio.com/hc/article_attachments/31072789918100)

The Speaker Utilities tab on the Monitor Controller window is where Apollo X speakers can be soloed muted, and trimmed. This window allows you to calibrate speakers in any Apollo X system and monitoring mode, from Stereo to 7.1.6. See [Speaker Utilities](https://help.uaudio.com/hc/en-us/articles/36177324309140) for more information.

![](https://help.uaudio.com/hc/article_attachments/31072798689428)

To open the Monitor Calibration popover, click the the Monitor Controller button in the Monitor Column, or the button next to the MONITOR MODE menu in Console Settings > Hardware.

Offset trim controls for each output channel in the active surround format are dynamically displayed in the popover, on the Speaker Utilities tab.

See [Calibrating Monitors](#h_01J9CTT7WJKVVP12X2NVE3S9PH) for detailed instructions on how to calibrate the surround system using the functions in this popover.

**Tip:** In addition to surround modes, Monitor Calibration is also available in Stereo mode.

## Surround I/O Matrix

When any surround mode is activated with the Monitor Mode menu:

* Output channel assignments and names are changed to match the mode.
* Physical output assignments and channel names can be customized. However, only the SMPTE Channels are available for assignment.

![](https://help.uaudio.com/hc/article_attachments/26909491280788)

Channel assignments and names in the I/O Matrix when 9.1.6 mode is activated

![](https://help.uaudio.com/hc/article_attachments/26909491296020)

Assigning outputs

# Console Surround Monitoring

![](https://help.uaudio.com/hc/article_attachments/31072798691860)

When a surround mode is active, the Monitor Meters and Monitor output options in Console’s Monitor Column appear as shown.

## Monitor Meters

Surround channel levels are displayed at the top of Console’s Monitor Column. To open a separate large, re-sizable Console Output Meters window, click on the meters or the UA logo. To close the separate output meters window, click the X in its upper left corner.

**Tip:** Drag from the bottom right corner to change the height of the separate output meters window.

### Channel Ordering

In Console, the Monitor Meters use FILM output channel ordering. Unlike SMPTE channel ordering for physical outputs, the software meters change according to the active surround mode.

Console’s surround monitor meter channel ordering for each surround mode is shown in the table below.

|  |  |
| --- | --- |
| MONITOR MODE | CONSOLE OUTPUT METERS |
| STEREO | L - R |
| 2.1 | L - R - LFE |
| LCR | L - C - R |
| LCRS | L - C - R - S |
| QUAD | L - R - Ls - Rs |
| 5.1 | L - C - R - Ls - Rs - LFE |
| 6.1\* | L - C - R - Ls - Cs - Rs - LFE |
| 7.1\* | L - C - R - Lrs - Rrs - Lss - Rss - LFE |
| 5.1.4† | L - C - R - Ls - Rs - Ltf - Rtf - Ltr - Rtr - LFE |
| 7.1.4† | L - C - R - Lss - Rss - Lrs - Rrs - Ltf - Rtf - Ltr - Rtr - LFE |
| 9.1.6† | L - C - R - Lw - Rw - Lss - Rss - Lrs - Rrs - Ltf - Rtf - Ltm - Rtm - Ltr - Rtr - LFE |
| \*Apollo x8, x8p, x16 †Apollo x16 only | |

Console’s monitor meters change with each surround mode

## Speaker Utilities

![](https://help.uaudio.com/hc/article_attachments/31072798693780)

The Speaker Utilities tab on the Monitor Controller window is used to mute, solo, and trim levels for individual output channels. The overall monitor output level can also be adjusted here.

To open Speaker Utilities, click the Monitor Controller button on the Monitor Column, then choose the Speaker utilities tab. For more information, see [Speaker Utilities](https://help.uaudio.com/hc/en-us/articles/36177324309140).

### Speaker Utilities Notes

* The MONITOR button in the Monitor Column blinks when any surround channel is soloed or muted.
* Solo and mute states are reset when the surround format is changed with the Monitor Mode menu or if unit ordering is changed in the DEVICES column in Console Settings > Hardware.

### Mode

Mode switches between SOLO, MUTE, and TRIM modes. The mode can also be switched by clicking its associated LED in the popover.

A blinking Mode LED indicates that a surround channel is in mute or solo mode when the other mode is active. For example, if an output is muted, the red LED will blink when SOLO mode is active.

#### Solo

To solo any surround channel, click its speaker icon in the Monitor popover when the yellow SOLO LED is illuminated. A surround output channel is soloed when its speaker icon is yellow.

**Tip:** Option-click (Mac) or alt-click (Win) to simultaneously change the solo state of all surround channels.

#### Mute

To mute any surround channel, click its speaker icon in the Monitor popover when the red MUTE LED is illuminated. A surround output channel is muted when its speaker icon is red.

**Tip:** Option-click (Mac) or Alt-click (Win) to simultaneously change the mute state of all surround channels.

#### Trim

To trim the level for any output channel, click the speaker icon and drag up or down, or double-click and enter a value.

**Tip:** Option-click (Mac) or Alt-click (Win) on any channel to set the offset trim to 0.

## Surround Fold Down

When a surround mode is active, all surround channels can be folded to a stereo or mono monitor mix. Although not a substitute for true LtRt encoding (which requires specialized hardware), this feature is convenient when all surround speakers are unavailable or when working with headphones.

### Level Compensation

When a surround mode is active and the mix is folded to stereo or mono, combined surround channel signals are attenuated as appropriate to maintain channel balance.

**Note:** Fold down level compensation occurs only when MONITOR MODE is set to a surround mode (levels are not compensated in stereo mode).

### Stereo Fold

Stereo fold down is active when the STER button in the OUTPUT section of the Monitor Column is illuminated. Click SRND to return to surround monitoring mode.

When stereo fold down is active, center channels (including LFE/SUB) are attenuated by -3 dB and surround side channels by -1.5 dB. The main Left and Right channels are not attenuated.

### Mono Fold

Mono fold down is active when the MONO button in the OUTPUT section of the Monitor Column is illuminated. Click MONO to return to surround monitoring mode.

When mono fold down is active, center channels (including LFE/SUB) are attenuated by -3 dB, surround side channels are attenuated by -7.5 dB, and the main Left and Right channels are attenuated by -6 dB.

**Note:** When mono fold down is active, inputs are routed to the Center output channel, except in 2.1 and QUAD surround modes. In 2.1 and QUAD surround modes (which do not feature a center channel), input signals are heard as summed mono in the Left and Right output channels.

# Calibrating Monitors

This procedure details how to calibrate Apollo X surround outputs to a monitor level of 85 dB SPL with a subwoofer boost of +10 dB. You’ll need the following tools:

* SPL Meter and Surround-capable DAW
* Digital audio source files (available at [here](https://help.uaudio.com/hc/articles/360020342832)):
  + 500-2500 Hz pink noise @ -20 dBFS
  + 40-80 Hz pink noise @ -20 dBFS

## Calibration Procedure

1. In the Hardware panel within the Console Settings window, choose the desired surround format from the Monitor Mode menu, then configure the DAW to use the same surround format.
2. In the DAW, play the 500-2500 Hz pink noise @ -20 dBFS audio file from a track that is routed to the front left (L) speaker output channel.
3. Click the Monitor Controller button on the Monitor Column, then click the Speaker Management tab, then click the Set in dB SPL button.
4. Click the Trim button to set speaker trim offsets.
5. From the mix position, point the SPL meter directly at the L channel speaker, then tilt the meter upwards towards the ceiling at an angle approximately 45 degrees from horizontal.
6. In the Speaker Utilities tab, rotate the monitor knob until the SPL meter reads 85 dBC (or other desired SPL value).
7. In the DAW, move the same audio file to the center (C) speaker output channel track. From the mix position, point the SPL meter directly at the C channel speaker, then tilt the meter upwards towards the ceiling at an angle approximately 45 degrees from horizontal.
8. In the Speaker Utilities tab, drag up or down on the C channel, adjusting its offset level until the SPL meter reads 85 dBC.
9. Repeat steps 7 – 8 for the other full range speaker output channels.
10. In the DAW, mute all of the full range speaker output channels.
11. In the DAW, play the 40-80 Hz pink noise @ -20 dBFS audio file from a track that is routed to the subwoofer (LFE) speaker output channel.
12. In the Speaker Utilities tab, drag up or down on the LFE channel, increasing its offset level until the SPL meter reads 95 dBC. Note that in standard practice, the LFE channel is typically boosted by +10 dB in film mixing and +4 dB in TV post production. However, LFE boost levels are not standardized.
13. In the Speaker Utilities window, press the SET dB SPL button. A popover opens
14. Enter a value of 85 (or the desired SPL value from step 6, if different) into the calibration text field, then press SET db SPL again.

The calibration procedure is complete.

## Calibration Notes

* After calibration, the Monitor knob is labeled as dB SPL units and the value displayed below the knob is the calibrated sound pressure level.
* Different standards are used for different applications. The most common standard is 0 dBFS being equal to -20 dB or 85 dB SPL (C-weighted).
* Hearing protection is recommended during the calibration procedure to prevent unnecessary exposure to high volume levels.

# Surround Operation Notes

The following operation notes apply when any Apollo X surround mode is active.

## Input Routing

* Digital Mirror routes always use stereo fold down and include any input signals.
* Apollo input signals are always routed to the Left & Right output channels, including when stereo fold down is active.
* To route an input signal(s) directly to one or more surround output channels, use the DAW.

## Cue & Headphone Mix Buses

* Surround fold down does not affect the cue or headphone mix buses.
* Stereo is always active in the cue and headphone mix buses.
* To monitor the cue and headphone mix buses in mono, use the MONO function in the Cue Outputs popover.

## Operating System Surround Sound

* Surround sound playback from non-DAW applications (DVD players, etc) is routed and folded down to stereo by the operating system (Core Audio or WDM).
* (macOS) Core Audio surround channels can be routed to Apollo X surround channels by choosing the surround mode from the Configuration menu within the Audio MIDI Setup application’s Audio Devices > Output > Configure Speakers popover.
* (Windows) WDM stereo fold down is routed to Apollo X Left & Right Monitor outputs only.

## Flex Routes

* Output channels that are used in surround monitor modes are unavailable for Flex Route assignments.
* If a Flex Route is assigned to a surround channel before entering a surround mode that uses the channel, the Flex Route is reassigned to Monitor, and the assignment remains on Monitor after returning to a mode that does not use the output.

## Console Recall

* Console Recall cannot be inserted on surround tracks. To use Console Recall in a DAW surround session, insert Console Recall on a mono or stereo track.
* Console Recall plug-in operation within the DAW is identical in stereo and surround sessions.
