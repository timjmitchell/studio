Source: https://help.uaudio.com/hc/en-us/articles/25351771431060-Aux-Returns
Updated: 2025-03-31T22:23:52Z

# Aux Returns

![aux-returns.png](https://help.uaudio.com/hc/article_attachments/27430589820052)

*Aux returns*

UAD Console has two stereo aux (auxiliary) mix buses. Signals are sent to the aux buses via the aux sends in UAD Console’s channel input strips. UAD Console’s aux returns are used to control and process the signals that are received from those sends.

The controls in UAD Console’s aux return strips are similar to the channel input strips, but instead of controlling a channel input, they control the output of the aux mix bus. Both stereo aux returns have four plug-in inserts for Realtime UAD Processing.

The aux sends can be post-fader and post-mute (channel faders must be raised and un-muted to be routed to the aux bus, and the send levels will reflect channel fader changes), or pre-fader and pre-mute (channel faders and mutes do not affect the aux bus).

The aux buses in UAD Console are designed primarily for send/return processing using UAD plug-ins. Using aux buses for effects is a great way to conserve UAD resources. For example, by using an aux for reverb processing, only one reverb plug-in is needed on the aux return instead of putting a reverb plug-in on each individual channel.

# Aux Notes

* Aux 2 is unavailable at sample rates of 176.4 kHz and 192 kHz.
* The outputs of the aux buses have 72 samples of additional latency compared to the monitor outputs. This is necessary to maintain the lowest possible latency for the channel input signals.
* You can only show Auxes if the Monitor column is shown. Show the Monitor column with View > Section > Monitor before you attempt to show Auxes.

# Show Aux Returns

By default, the aux returns are not visible. To show the aux returns, enable the AUX switch in the SHOW section of the monitor column, or select View > Section > Auxes from the UAD Console menus.

![](https://help.uaudio.com/hc/article_attachments/25351771421204)

*The Show Aux switch in the monitor column*

# Aux Return Strips

![aux-callouts.png](https://help.uaudio.com/hc/article_attachments/27430556770068)

*Aux return strip*

Both of UAD Console’s aux return strips are identical. Most of the controls have identical functionality as their equivalent control in the channel input strips.

## Channel Presets

Click the plus symbol (+) to open the Channel Presets browser. From the Channel Presets browser, you can load complete preconfigured plug-in chains created for specific recording and monitoring purposes.

## Aux Inserts

The aux inserts are operated using the same methods as the insert controls in the channel input strips. See [UAD Plug-In Inserts](https://help.uaudio.com/hc/en-us/articles/25350369296660) for complete descriptions of the aux insert controls.

### Aux Inserts Context Menu

The Aux Inserts context menu allows you to adjust inserts for the aux returns.

![aux-inserts-menu.png](https://help.uaudio.com/hc/article_attachments/27553350552084)

* To toggle large or small aux inserts view, right-click or control-click on the Inserts label, and select or deselect View Large Icon. Note that this also changes the view for the Talkback channel strip.
* To disable all plug-ins on an aux return, select Disable All.
* To enable all plug-ins on an aux return, select Enable All.
* To remove all plug-ins from an aux return, select Remove All.

**Important:** UAD plug-in processing in the aux inserts is always routed to the DAW (if the aux buses are routed as DAW inputs), regardless of the Insert Effects setting (aux insert processing is always recorded).

## Aux Cue Sends

The aux returns can be routed to any available cue mix buses using the cue sends on the aux returns. There is no cue pan control on the aux returns, because the aux returns are stereo.

### Aux Cue Sends Context Menu

The Aux Cue sends context menu allows you to adjust sends and cue views for the aux returns.

![aux-sends-menu.png](https://help.uaudio.com/hc/article_attachments/27553487137940)

* To toggle Sends Overview, right-click or control-click on the Sends label, and select or deselect Overview. Note that this changes the view for all channels.
* To view a large or small icon for any cues, select or deselect Send # - View Large Icon. Note that this changes the view of that cue for the talkback channel and the aux returns.

The aux cue sends are operated using the same methods as the send controls in the channel input strips. See [Cues](https://help.uaudio.com/hc/en-us/articles/25351037512340) for complete descriptions of the aux send controls.

**Tip:** When a Cue Source is set to cue, aux returns must be sent to the cue mix bus via these controls for the aux to be heard in the cue mix.

## Aux Pre

When the PRE switch is engaged (lit), the aux mix bus is pre-fader and pre-mute. In PRE mode, the channel faders and mutes do not affect the aux bus.

**Tip:** Pre-fader mode is useful for configuring a mix bus that is independent of the monitor mix controls (for example, when creating a cue mix).

## Aux Post

Post-fader is the default setting for Aux 1 and Aux 2. When the POST switch is engaged (lit), the aux mix bus is post-fader and post-mute. In POST mode, the channel faders must be up and un-muted to be routed to the aux bus, and the aux send levels will reflect channel fader changes.

**Tip:** Post-fader mode is typically used when configuring an effect send mix so the effect send levels will interact with the input channel fader.

## Aux Mono

This switch sums the left and right channels of the stereo aux mix bus output into a monophonic signal. The aux return output is stereo when the button is gray and mono when the button is lit.

## Aux Mute

The aux mute switch stops the aux return’s signal from being routed to the monitor mix. The aux return output is active when the button is gray and muted when the button is lit.

**Note:** Aux mute does not mute the aux cue sends.

## Aux Fader

This is the master signal level control for the aux bus return to the main monitor mix. It does not affect the aux bus return’s cue sends. Up to 12 dB of gain above 0 dB is available.

## Aux Meter

The aux meter displays the signal level of the aux return after UAD plug-in processing in the aux inserts. Depending on the state of the METERING option in Settings > Options, (either pre-fader or post-fader), this meter will display the aux bus output level routed into the monitor mix bus (post-fader/post-inserts), or the level of the aux mix bus itself (pre-fader/post inserts).

### Input Level Scale

The numerical labels represent digital signal levels. “0” represents 0 dBFS (digital full scale, the maximum level before undesirable A/D clipping). If the level of the aux bus exceeds 0 dBFS, the meter’s clip indicator illuminates. If clipping occurs, reduce the aux sends from the input channels and/or the output gain(s) of UAD plug-in processing in the aux inserts.

### Peak Hold

The aux meters also have a peak hold feature, which holds signal peak values for a specified period of time. The clip and peak hold times can be adjusted in Settings > Options.

**Tip:** When recording into a DAW, it’s typically best to keep the metering set to pre-fader so meters accurately represent the signal level at the DAW inputs.
