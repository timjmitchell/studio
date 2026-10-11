Source: https://help.uaudio.com/hc/en-us/articles/25348339047572-Info-Bar
Updated: 2025-03-31T22:23:52Z

# Info Bar

The Info Bar is always visible at the bottom of the UAD Console window. It displays and provides access to several important functions.

The Tempo controls are only available in the Info Bar. The Sample Rate and Clock Source controls are also available in UAD Console Settings. The UAD Resource Gauges have no controls; they are visual indicators only.

![info-bar-callouts.png](https://help.uaudio.com/hc/article_attachments/28841010886932)

*The Info Bar*

# Offline Hardware Display

If the Apollo hardware unit(s) is not properly connected, the sample rate and clock source will display OFFLINE as shown below.

![](https://help.uaudio.com/hc/article_attachments/25348339007380)

*Sample Rate and Clock when Apollo is offline*

# Tempo Display

![](https://help.uaudio.com/hc/article_attachments/25348360225812)

UAD Console's current tempo is displayed here in beats per minute (BPM). UAD Console Tempo is used for time-based UAD plug-ins (such as delays and modulations) within UAD Console that are set to use Tempo Sync. UAD Console Tempo can be modified by typing a text value, tapping a tempo, or via MIDI.

**Note:** UAD Console does not receive tempo information from the DAW.

The tempo value is saved within UAD Console session files, and also within DAW files when the UAD Console Recall plug-in is used within the DAW.

For details about how to use the Tempo Sync feature with UAD plug-ins, see the [UAD System Manual](https://help.uaudio.com/hc/en-us/articles/13444697234196-UAD-System-Manual).

## Tempo Popover

![](https://help.uaudio.com/hc/article_attachments/25348360235540)

To display the Tempo window, click anywhere in the Tempo Display within the Info Bar.

The available tempo range is from 1.00 BPM to 999.00 BPM. The default tempo of a new session is 120 BPM.

## Adjusting Tempo

#### *Text Entry*

1. Open the Tempo window by clicking the Tempo Display in the Info Bar
2. Click the tempo text field, then type a numeric tempo value
3. Press Return or Enter, or click the close button with the mouse.

**Tip:** To leave the tempo unchanged after entering an (unwanted) value in the Tempo window, press the ESC key or close the window with the mouse.

### Tap Tempo

1. Open the Tempo window by clicking the Tempo Display in the Info Bar
2. With the mouse, click the TAP button at least four times to establish the tempo
3. Press the ESC key on the computer keyboard, or click the close button with the mouse.

## Changing tempo via MIDI

Tap tempo can be used to set a new tempo from incoming MIDI data. This method requires any external MIDI hardware and/or MIDI software that is recognized by the OS.

**Note:** MIDI drivers for the MIDI device may need to be installed and/or configured.

### About external MIDI tap tempo control

* The MIDI device must be properly configured before it can be used by UAD Console.
* MIDI note values or MIDI controller values can be used as the data source.
* UAD Console cannot synchronize the tempo to incoming MIDI beat clock.

### MIDI configuration and setup

1. Verify the MIDI output device or MIDI software is properly configured and active.
2. In Settings > MIDI, set the values for DEVICE, TAP TEMPO CHANNEL, and TAP TEMPO EVENT to match the transmitted MIDI data.
3. Transmit the MIDI note or controller (as specified in the previous step) at least four times to establish the tempo. The Tempo Display is RED during this period.
4. After a new tempo value is established, the new tempo is used and the Tempo Display changes back to BLACK. Simply retransmit the MIDI data to apply further tempo updates.  
     
   ![](https://help.uaudio.com/hc/article_attachments/25348360240020)

# Sample Rate Display

Apollo's current sample rate is displayed here. Click this area to select a different sample rate from the drop menu when using UAD Console without a DAW. This area displays the current sample rate used for Apollo's A/D-D/A conversion and UAD Plug-Ins processing. When using UAD Plug-Ins, higher sample rates require more UAD DSP resources.

**Important:** When the Clock Source parameter is set to use any external clock source, the sample rate must be manually set to match the sample rate of the external clock.

## Sample Rate Menu

![](https://help.uaudio.com/hc/article_attachments/25348360245652)

Clicking the Sample Rate Display presents the Sample Rate Menu, where the current sample rate can be changed.

**Important:** When a DAW is used with Apollo, the sample rate is typically changed within the DAW settings. If the sample rate is changed to a different value within UAD Console when a DAW is active, digital artifacts could occur due to a sample rate mismatch.

**Apollo Twin Note:** If the current digital input setting is S/PDIF and the sample rate is changed to a rate higher than 96 kHz, the clock source is changed to Internal and the S/PDIF inputs are no longer available.

## Hardware Clicks

When the sample rate is changed, hardware relays that mute the outputs are temporarily engaged to prevent audio artifacts. This action causes an acoustic clicking sound that can be heard within the hardware. These clicks are by design and can be safely ignored.

**Note:** Hardware clicks are not heard with first-generation (silver) Apollo rack models, which do not feature hardware relay muting.

# Clock Source

The active clock source (Internal, ADAT, S/PDIF, or Word Clock) is displayed here. Click this area to select a different clock source from the drop menu. This area flashes red if the currently selected clock is unresolved (when digital audio is not synchronized).

**Note:** Word Clock is available with Apollo rack models only.

## Clock Source Menu

![](https://help.uaudio.com/hc/article_attachments/25348339027220)

Apollo can synchronize to its internal clock or an external clock (word clock, ADAT, S/PDIF, or AES/EBU; available clock sources depend on the connected Apollo hardware). To select a clock source, click anywhere in the clock display area to view the Clock Source Menu, then select a clock source from the menu.

**Tip:** The clock source can also be specified in Settings > Hardware.

## No External Clock

![](https://help.uaudio.com/hc/article_attachments/25348339030164)

If the Clock Source setting is not set to Internal and the external clock signal cannot be detected and/or resolved, then the text in the Clock Display display flashes RED (as shown at right) until a valid clock is detected and/or an alternate clock source is selected. If this occurs, verify connections and external device settings.

**Important:** Only one device in a digital audio system can be the master clock source. The Apollo clock setting, and the sample rate, must match the master device settings or audio artifacts could occur.

# UAD Resource Display

This area displays DSP and memory resource loads used by all loaded UAD plug-ins (UAD Console and DAW). UAD loads can be monitored as needed, for example when deciding which UAD plug-ins to load, based upon how much DSP is available.

Values displayed here are mirrored in the UAD Meter & Control Panel application. More detailed (per-SHARC) display of DSP usage is available in the System panel within the UAD Meter & Control Panel application.

## Averaged Loads

The load for each gauge represents the average for all UAD devices in use. For example, if one Apollo QUAD unit is connected, the UAD DSP load is an average of the four SHARC DSP processors in the unit. If two QUAD units are connected, then the eight processors are averaged, and so on.

## Individual Loads

Individual DSP loads within a single unit, and the loads of individual devices in a multi-device setup, can be viewed in the System Information panel within the included UAD Meter & Control Panel application.

## UAD Plug-In Loads

The amount of UAD resources used by UAD plug-ins vary with each individual plug-in; more complex algorithms require more resources.

### Instance Chart

The amount of DSP used by each individual UAD plug-in is available in the UAD instance count chart. The chart can help determine which plug-ins to assign with available resources. The chart is published online at:

* [www.uaudio.com/support/uad/compatibility/instance-chart.html](https://www.uaudio.com/support/uad/compatibility/instance-chart.html)

## Static Loads

Apollo uses UAD DSP and memory for its internal DSP mixer, therefore the meters will indicate loads (when the hardware is connected) even if UAD plug-ins are not inserted.

## DSP

The DSP gauge indicates the amount of digital signal processing resources that are being used by all UAD devices in the system.

DSP is the primary hardware resource that powers the UAD Plug-Ins algorithms. When UAD plug-ins are disabled, DSP requirements are decreased.

**Note:** When UAD plug-ins are disabled, DSP requirements are decreased EXCEPT when the plug-in is disabled using the Power control within the plug-in window.

## Program

The Program (PGM) gauge indicates how much UAD program memory (PGM) is in use. Program memory is an on-chip memory that is specific to the UAD-2 DSP processor(s) and is used for certain UAD plug-in resources.

Each unique UAD plug-in uses a bit of program memory. If many different UAD plug-ins are loaded simultaneously, it is possible for this resource to run out before a DSP overload occurs. This point is considered and factored in by the automatic UAD load balancing routines.

## Memory

The Memory (MEM) gauge indicates the percentage of UAD RAM that is currently in use. It indicates the total available UAD memory available, regardless of the number of DSP processors that are installed.

Memory is used for echo, delay lines, reverb, and similar spatial processing. When UAD plug-ins are disabled but not unloaded, memory requirements are not decreased. In this case, the memory remains loaded so that reverb tails and delay lines are not cut off when the plug-in is disabled.

# Plug-In Scenes Display

The Plug-In Scenes display shows the current Plug-In Scene. Click this area to toggle the Plug-In Scenes browser. See [Plug-In Scenes](https://help.uaudio.com/hc/en-us/articles/28354758319892) for more information.
