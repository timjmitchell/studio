Source: https://help.uaudio.com/hc/en-us/articles/25349542599956-Preamp-Controls
Updated: 2025-03-31T22:23:52Z

# Preamp Controls

UAD Console's preamp controls correspond to the equivalent preamp controls on the Apollo front/top panel. Adjusting Apollo's front/top panel updates UAD Console (and vice versa); see [Interactions Between UAD Console and Apollo](https://help.uaudio.com/hc/en-us/articles/25347160337556#h_01HTY75BBWZSHYPGF8YPW4JFYB) for details.

**Note:** The preamp controls are not available with Apollo 16, Apollo x16 Gen 1 & 2, or Apollo x16D, which do not feature mic preamps.

![preamp-callouts.png](https://help.uaudio.com/hc/article_attachments/31944466615956)

# Unison Controls

![unison-icon1.png](https://help.uaudio.com/hc/article_attachments/25350010789652)

Some preamp hardware controls (Gain, Low Cut, 48V, Pad, Polarity) are Unison parameters that interact with Unison plug-ins placed in the Unison insert slot.

Unison preamp controls in this section are indicated by the Unison icon in the above paragraph. For complete Unison details, see [Unison](https://help.uaudio.com/hc/en-us/articles/26485044036756).

## Preamp Gain

|  |  |
| --- | --- |
| unison-icon1.png | input-preamp-gain-knob.png |
| The channel's preamp gain is adjusted with this knob. The input to be adjusted (Mic, Line, or Hi-Z) is determined by the state of the channel's Mic/Line switch or the Hi-Z input (if connected).  Rotating the knob clockwise increases the preamp gain for the channel. The available gain range for all preamp channels is 10 dB to 65 dB for the Mic, Line, and Hi-Z inputs.  **Tip:** This control can be adjusted with Apollo's hardware knob. For complete details, see [Unison](https://help.uaudio.com/hc/en-us/articles/26485044036756). | |

## Gain Value

|  |  |
| --- | --- |
| unison-icon1.png | input-preamp-gain-knob.png |
| The specific amount of preamp gain in decibels is displayed in gray text below the gain control. The relative amount of preamp gain is indicated by the green LED ring surrounding the gain control in UAD Console. The LED ring is a different color when Unison is active in the channel. | |

## Line Input Gain Bypass

|  |  |
| --- | --- |
| unison-icon1.png | preamp-line-input-bypass.png |
| When a preamp channel's line input is selected and its Line Input Gain is bypassed, the Gain Value field displays BYP, its gain cannot be adjusted, and the Unison plug-in (if inserted) is disabled. For related details, see [Line Input Gain](https://help.uaudio.com/hc/en-us/articles/25403573794836#h_01HTY5D6CW58X0RBF0CKEY4H9F). | |

**Note:** Line Input Gain availability depends on the Apollo model.

| **Available** | | **Unavailable** | |
| --- | --- | --- | --- |
| Apollo 8 Apollo 8p Apollo x6 Apollo x8 Apollo x8p | Apollo x6 Gen 2 Apollo x8 Gen 2 Apollo x8p Gen 2 Apollo Twin X Gen 2 Apollo x4 Gen 2 | Apollo FireWire Apollo Twin Apollo Twin X Apollo x4  Apollo Twin USB | Apollo Twin X USB Apollo SOLO Apollo SOLO USB Arrow |

## Front Panel Channel Selection Indicator Dot

|  |  |
| --- | --- |
| unison-icon1.png | input-preamp-selected.png |
| Apollo's channel selection can be changed using the hardware's PREAMP switch. The small colored dot that appears next to the gain control (as shown at right, outlined in red) indicates the preamp channel that is currently selected on the Apollo hardware panel.  **Tip:** The indicator dot in UAD Console changes channels when the channel selection is changed with Apollo's PREAMP switch. | |

## Input Select

|  |  |
| --- | --- |
| unison-icon1.png | input-preamp-select-highlighted.png |
| This switch switches between the mic and line inputs on Apollo's rear panel. Click the Input Select switch or Input Select display to change the input type. The currently selected input type is highlighted.  **Note:** Input Select has no effect if the channel's Hi–Z input is connected, because preamp channels are automatically switched to the Hi-Z input when a ¼" mono (tip-sleeve only) cable is connected to Apollo's front panel Hi-Z input jack. | |

## Low Cut Filter

|  |  |
| --- | --- |
| unison-icon1.png |  |
| When enabled, the channel's input signal passes through a low cut (high pass) filter. This 2nd-order coincident-pole filter has a cutoff frequency of 75 Hz with a slope of 12 dB per octave by default (the filter can change when a Unison plug-in is active in the channel).  The Low Cut filter is applied to the Mic, Line, and Hi-Z inputs. Low Cut is typically used to eliminate rumble and other unwanted low frequencies from the input signal. | |

## 48V Phantom Power

|  |  |
| --- | --- |
| unison-icon1.png |  |
| When enabled, the 48V switch is red and 48 volts of phantom power is supplied to the Apollo channel's rear panel Mic input. Most modern condenser microphones require 48V phantom power to operate. This option can only be activated when the Mic/Line switch is set to Mic.  **Caution:** Activate 48V only with compatible equipment such as phantom powered microphones. Incompatible equipment may be damaged by the applied voltage.  Depending on the current configuration of the Apollo and UAD Console, there may be a delay when changing the 48V state to minimize the clicks/pops that are inherent when engaging phantom power. The +48V LED on Apollo's front panel will flash during any delay. | |

## Pad

|  |  |
| --- | --- |
| unison-icon1.png |  |
| When enabled, the PAD switch is yellow and the channel's microphone input signal level is attenuated by 20 dB. Pad does not apply to the Line or Hi-Z inputs.  Pad is used to reduce signal levels when overload distortion is present at low preamp gain levels, such as when particularly sensitive microphones are used on loud instruments, and/or if the A/D converter is clipping.  **Tip:** Activate PAD when the input is clipping but preamp gain is at minimum. Alternately, reduce the output level (if available) of the device connected to Apollo's input. | |

## Polarity

|  |  |
| --- | --- |
| unison-icon1.png |  |
| When enabled, the polarity (aka phase) switch is yellow and the input channel's signal is inverted. Polarity applies to the Mic, Line, and Hi-Z inputs.  **Tip:** Polarity inversion can help reduce phase cancellations when more than one microphone is used to record a single source. | |

# Reference Level

![](https://help.uaudio.com/hc/article_attachments/25349542594580)

The signal reference level for analog line inputs without preamps can be switched between -10 dBV and +4 dBu. Click the level display to toggle the setting.

The setting controls an attenuation pad for the input channel. When set to +4 dBu, the pad is engaged and the channel can accept a higher signal level before the A/D converter clips. Select -10 dBV when lower input signal levels are used.

## Tips

* To adjust signal incoming levels for Apollo's line inputs that don't have preamps, use the output level controls of the devices that are connected to those inputs.
* Additional gain can be added to input signals by inserting UAD plug-ins and adjusting the gain structure within the plug-ins.

The availability and behavior of the reference level control depends on the hardware model, as described below.

**Apollo –** The reference level for line input channels 5 & 6 and 7 & 8 are linked in Apollo's hardware. Therefore, the reference level in UAD Console can only be switched according to these stereo pairs.

**Apollo 8, x8 (Gen 1 & 2) –** The reference level for line input channels 5 – 8 **can** be individually switched.

**Apollo 16 –** The reference level for all analog line input channels **can** be individually switched.

**Apollo 8p, x8p (Gen 1 & 2)  –** The reference level for line input channels cannot be switched.

# Sample Rate Convert

![](https://help.uaudio.com/hc/article_attachments/25349542596372)

Realtime sample rate conversion ("SR CONVERT") is available on  
S/PDIF and AES/EBU inputs. This feature eliminates audio artifacts (clicks, distortion, etc) that can occur when the sample rate of external digital devices connected to the S/PDIF or AES/EBU inputs do not match Apollo's internal sample rate.

To enable real time sample rate conversion on Apollo's S/PDIF or AES/EBU inputs, click the SR Convert switch in UAD Console's associated channel strip. Click again to disable the feature.

#### *Sample Rate Conversion notes:*

* Available on S/PDIF or AES/EBU inputs only
* Applies to both L/R inputs (they can't be individually enabled)
* Applies to both L/R inputs whether or not they are stereo linked
* Unavailable when Apollo's clock source is set to S/PDIF or AES/EBU
* Unavailable on digital outputs
