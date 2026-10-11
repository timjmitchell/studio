## **VUMT deluxe** ^ÄtÇz{xÄÅ 

**==> picture [500 x 371] intentionally omitted <==**

**==> picture [500 x 121] intentionally omitted <==**

_Klanghelm VUMT deluxe - Manual_ 

## **Table of Contents** 

|**Table of Contents**||
|---|---|
|Main Features|3|
|Installation|4|
|Top Bar/Preset System|5|
|Meters|6|
|Main Controls Dual Mode|7|
|Main Controls Single Mode|8|
|Meters Only Option|9|
|Bottom Panel|10|
|Meter Settings|11|
|RMS & K-Meter|12|
|Global Settings|13|
|Standalone Application|14|
|Appendix: Meter Scales|15|
|Appendix: Weighting Curves|16|
|Credits|17|



Page 5 Page 6 Page 7 

**==> picture [436 x 326] intentionally omitted <==**

Page 10 

2 

_Klanghelm VUMT deluxe - Manual_ 

## **Main Features** 

- [painstakingly modeled behavior of classic analog VU and PPM ] meters 

- [available meter types:] 

   - [VU] 

   - [RMS] 

      - incl. option to compensate the RMS scale (+3dB) according to AES-17, so a sine wave at 0dBFS equals 0dBFS RMS 

         - gain staging made easy with separate trim controls for left/right channel 

         - mid-side (sum-diff) matrix with separate trim controls for mid and side 

         - monitor section 

         - polarity reverse 

         - individual mute controls per channel 

      - K-12, K-14, K-20 scales 

      - integrated peak bar-graph 

      - optional frequency weighting (A, B, C, D and K curves - see page 15 for details) 

   - [PPM:] 

      - DIN (Type I) 

      - Nordic (Type I) 

      - BBC (Type IIa) 

      - EBU (Type IIb) 

- highly customizable needle ballistics incl. adjustable needle overshoot for the VU 

- customizable hold needle 

- customizable peak/clip LED 

- single or dual needle display 

   - some useful track-utilities, such as: 

      - [high-pass and low-pass filters (can be set individually to 6, 12, 18 ] or 24 dB steepness) 

      - [a single dynamic EQ band (HPF, LPF or BPF), which can be used ] to remove resonances, simple de-essing, to control the low end of a signal … 

      - [a mono maker which reduces the stereo width of a signal below a ] certain frequency 

   - dedicated standalone app, which.. 

      - [automatically saves its settings on close and restores them on ] relaunch 

      - [can load/save states] 

      - [can be set always-on-top ] 

- 8 different skins to choose from 

- GUI resizing 

- lots of options to show/hide various elements, including the option to show only the meters and hide all controls from the GUI 

- global settings incl. customizable knob behavior and adjustable needle refresh rate 

- preset menu incl. easy copy/paste presets from from instance to another and save as default 

3 

_Klanghelm VUMT deluxe - Manual_ 

## **Installation** 

## **Windows:** 

## **Plugins (64-bit VST, VST3, AAX) and Standalone (64-bit)** 

- download and unzip the installer from the user area 

- run VUMTdeluxe-installer.exe and follow the instructions 

## **Apple macOS:** 

## **Plugins (64-bit AU, VST, VST3, AAX) and Standalone (64-bit)** 

- download and unzip the installer from the user area 

- open the VUMTdeluxe.dmg, run the included VUMTdeluxeinstaller.pkg and follow the instructions. 

## _Troubleshooting:_ 

If you get an error message before or during the installation process, it is very likely due to a false positive from your active virus scanner. In this case either add VUMTdeluxe-installer.exe to your whitelist or temporarily disable the scanning during the install process. 

## _Troubleshooting:_ 

- in case you’re getting a message, that the installer can’t be executed, because it is „not downloaded from the App store“, do the following: 

- Go to System Preferences -> Security & Privacy 

- In the General Tab of the Security & Privacy window click on the lock icon in the bottom left to be able to make changes. 

- select "Anywhere" in the section "Allow applications downloaded from:“ 

- Now install VUMTdeluxe again. 

4 

_Klanghelm VUMT deluxe - Manual_ 

## **Top Bar & Preset System** 

go to previous preset go to next preset click on the Klanghelm logo to enter the click to click to select from click to select the GUI size global settings (see page 13) enter the preset menu. 8 different skins copies the current plugin state to click to load a preset file from disk clipboard. You can use „paste from clipboard“ in another instance of the resets the plugin to its default state plugin to apply these settings to that instance or you can paste that into a text document to share it with other users. saves the current state as a preset onto your hd. Please make sure, that the preset is saved into your click on „paste from clipboard“ to UserPresets-folder in order to make it visible in the USER apply a copied state to the current plugin instance. category factory preset categories saves the current state as the default state, that is recalled whenever you load a new instance of the plugin 

your own presets can be recalled from here. 

In case you want to delete (some of) them, they are located here: macOS: /Users/<username>/Library/Klanghelm/VUMTdeluxe/UserPresets/ Windows: C:/Users/<username>/AppData/Roaming/Klanghelm/VUMTdeluxe/UserPresets/ 

**When loading one of the factory presets, only the parameters, that are necessary for each preset are affected. Parameters such as SKIN and SIZE are excluded. The user presets on the other hand include ALL parameters including SKIN and SIZE.** 

5 

_Klanghelm VUMT deluxe - Manual_ 

## **Meters** 

use this option on show readouts of the enable a mono signals in current meter values. secondary (orange) Peak/Clip-LED as hosts that don’t left side of each hold-needle to defined in the meter differentiate meter: needle value show the current settings. between mono and (depends on the if the LED is lit red, stereo tracks selected metering you can click at the LED to manually type), show Polarity Reverse, Mute show the instance label at reset the LED. and Monitor controls the bottom of the GUI click to enter the meter settings (see page 11) click to switch to a contrasting meter view 

if meter values are if meter values are single or dual if the hold needle is enabled in the visibility enabled in the visibility meter display enabled in the settings, this is a settings, this is a visibility settings, readout for the current readout for the current you can click on max. meter value. peak (dBFS) value. the meter to reset Click to reset the meter Click to reset the the hold needle readouts. meter readouts. 

6 

_Klanghelm VUMT deluxe - Manual_ 

## **Main GUI - Dual Meters Display** 

when lit, the left TRIM knob controls the volume for both channels, the right TRIM control is disabled in this case show meters only and hide all controls from the GUI 

drag or click to set the calibration level of the currently selected metering type. When the meter is set to RMS, you can adjust the frequency weighting curve instead (see page 16). select the meter type determines, if the meters show either left / right  or mid / side information, also sets the functionality of the Trim knobs accordingly 

polarity reverse right channel 

show bottom panel with additional tools: high pass and low pass filters, dynamic EQ and mono maker mutes the mutes the left channel right channel polarity reverse left channel 

depending on the DISPLAY mode, it controls the volume of either the left or the mid channel. 

**Note:** If you’re in LR mode, and you’ve adjusted the mid gain before switching back to LR, a little green indicator is shown around the left Trim, showing the position of the underlying mid Trim. This indicator is also shown for the opposite case, that you’ve adjusted the left gain and then switch back to MS 

selects the output signal: LR: stereo RL: stereo reverse L: left channel only R: right channel only M: mid (mono) channel S: side channel only 

If you click on an already lit button, the monitor selection switches back to „LR“ for quick compare. 

Note: the selected output signal is independent from the selected metering channel mode (Stereo or MidSide) 

monitor left(L), right(R), side/ diff(S) channel options either in place or centered 

depending on the DISPLAY mode, it controls the volume of either the right or the side channel 

**Note:** If you’re in LR mode, and you’ve adjusted the side gain before switching back to LR, a little green indicator is shown around the left Trim, showing the position of the underlying side Trim. 

This indicator is also shown for the opposite case, that you’ve adjusted the right gain and then switch back to MS 

7 

_Klanghelm VUMT deluxe - Manual_ 

## **Main GUI - Single Meter Display** 

drag or click to set the calibration level of the currently selected metering type. When the meter is set to RMS, you can adjust the weighting instead (see page 16). 

select the meter type needle represents the mono signal (or stereo sum on stereo channels) when lit, the main needle represents the left channel, while a secondary (red) needle displays the right channel information 

selects the output signal: LR: stereo RL: stereo reverse L: left channel only (in place) R: right channel only (in place) L (c): left channel only (centered) R (c): right channel only (centered) M: mid (mono) channel S: side channel only S (c): side channel (diff) only (centered) 

**==> picture [337 x 190] intentionally omitted <==**

**----- Start of picture text -----**<br>
polarity reverse left channel<br>p olarity reverse right channel<br>mutes the signal<br>controls the<br>volume (in dB)<br>for both left<br>and right<br>channel<br>**----- End of picture text -----**<br>


when lit, the main needle represents the mid channel, while a secondary red needle displays the side channel information 

8 

_Klanghelm VUMT deluxe - Manual_ 

## **Main GUI - Meters Only Display Mode** 

**==> picture [688 x 412] intentionally omitted <==**

**----- Start of picture text -----**<br>
click on the Klanghelm logo to enter the  click to enter the  is lit if one of  is lit if one of the channel tools<br>global settings (see page 13) preset menu.  the bottom  (mute, polarity reverse, monitor<br>panel tools is<br>(see page 5) section) is in use<br>active<br>see page 6 for details<br>is lit if one of the trim controls is not<br>a t unity<br>click to enter the meter settings<br>(see page 11)<br>Peak/Clip-LED as defined in the<br>meter settings.<br>if the LED is lit red, you can click at<br>click to switch to a contrasting<br>meter view the LED to manually reset the LED.<br>if meter values are enabled in  single or dual meter display<br>the visibility settings, this is a<br>readout for the current meter<br>value.<br>if meter values are enabled in the<br>visibility settings, this is a readout<br>for the current peak (dBFS) value.<br>click to hide all labels and<br>comboboxes from the frame<br>select, wether the VU represents<br>click to make the controls visible<br>the<br>select the meter type •<br>mono sum (single meter only)<br>•<br>stereo (main needle: left, red<br>click to select the GUI size<br>needle: right)<br>drag or click to set the calibration level of the<br>OR<br>currently selected metering type.<br>•<br>mid-side (main needle: mid, red<br>When the meter is set to RMS, you can  click to select from 8 different<br>needle side)<br>adjust the weighting instead (see page 16). skins<br>**----- End of picture text -----**<br>


9 

_Klanghelm VUMT deluxe - Manual_ 

## **Bottom Panel** 

**==> picture [730 x 391] intentionally omitted <==**

**----- Start of picture text -----**<br>
click on the header or on/off switches<br>to enable/disable each section. When<br>disabled, the respective controls are<br>grayed out.<br>click to select the<br>steepness of the<br>LPF or turn it off<br>gain reduction amount<br>of the dynamic<br>click to select the<br>steepness of the<br>HPF or turn it off<br>amount of the effect<br>in %<br>click to edit the<br>instance label<br>cutoff frequency  cutoff  determines the strength  all frequency content below<br>of the high-pass  frequency selected  (depth) of the reduction  the selected frequency is set<br>filter in Hz  to mono<br>click to select the filter  use this switch when<br>type of the dynamic  sweeping through the<br>cutoff frequency  EQ.  frequencies to find the<br>of the lowpass  BPF1: bandpass with  frequency range you<br>filter in Hz  narrow Q  want to reduce<br>BPF2: bandpass with<br>wide Q<br>**----- End of picture text -----**<br>


10 

_Klanghelm VUMT deluxe - Manual_ 

## **Meter Settings** 

choose from 3 different VU-meter implementations: 

VU 1: the same behavior as VUMT version 1.x 

ideal: an idealized (theoretical) VU model 

VU 2: revised, best of both worlds model for VUMT 2 with separate control over Rise and Fall times 

NOTE: all 3 modes are within VU specs, it’s just a matter of personal preference which one you choose 

rise time of the needle depending on the selected meter-type (in ms) 

fall time of the needle depending on the selected meter-type (in ms) 

Needle overshoot in %. Only adjustable when VU is selected 

sets the threshold of the yellow peak LED in dBFS. The LED gradually turns orange the closer the peak level gets to the set CLIP level. 

Select the meter-type, you want to adjust the ballistics for. Changing the meter type here will also temporarily change the meter type in the plugin GUI, so you’re immediately get visual feedback of the changes made here. When closing the meter settings the meter type reverts to the type, that has been selected before entering the meter settings. 

adjusts the hold time of the optional orange hold-needle in sec. 

This control is disabled when the „inf“ box is ticked. 

**==> picture [347 x 254] intentionally omitted <==**

set the hold time of the secondary orange needle to infinity. 

when ticked, the TIME control is disabled. 

adjusts the hold time of the meter value readouts in sec. 

This control is disabled when the „inf“ box is ticked. 

set the hold time of the meter value readouts to infinity. 

when ticked, the TIME control is disabled. 

closes the meter settings. 

set the hold time These meter settings are saved per of the red clip instance. You can use the preset menu sets the adjusts the clip hold time LED to infinity. and save these as default, so these of the red clip LED in sec. threshold settings are applied to every new of the red when ticked, the This control is disabled CLIP HOLD time clip LED in when the „inf“ box is control is dBFS. ticked. disabled. 11 

These meter settings are saved per instance. You can use the preset menu and save these as default, so these settings are applied to every new 

## _Klanghelm VUMT deluxe - Manual_ 

## **RMS and K-Meter** 

**==> picture [698 x 441] intentionally omitted <==**

**----- Start of picture text -----**<br>
Enable analog behavior for<br>smoother needle movement.<br>When disabled, the needle<br>shows the pure calculated RMS<br>value without taking the<br>properties of the needle into<br>account.<br>Size of the RMS-window in ms<br>sets the range of the black zone<br>in dB. This value is also valid for<br>the peak bar graph<br>Sets the threshold of the red zone in dB<br>Bargraph shows the peak level<br>of the signal. If one of the K-<br>scales in used, it reflects the<br>selects dB-offset If one of the K-Scales is<br>selected this value reflects the<br>SCALED  peak-value, shown<br>by the peak-bar-graph<br>Hold-indicator of the peak-bargraph, Its hold<br>Click to select either pure RMS, RMS<br>time is determined by the setting of the hold-<br>+3 (AES-17) or K-12, K14 or K-20<br>needle. Clicking on the meter resets both hold<br>scales<br>needle and the bar-graph-indicator<br>**----- End of picture text -----**<br>


12 

_Klanghelm VUMT deluxe - Manual_ 

## **Global Settings** 

**==> picture [378 x 375] intentionally omitted <==**

Sets the mouse drag behavior when moving a knob on the GUI Sets the mouse drag sensitivity when moving a knob on the GUI 

When set to „fast“ the behavior of the needles is the most fluid and realistic. To ~~sav~~ e CPU cycles, you can select a „medium“ or „slow“ refresh rate.. To apply changes to the refresh-rate, you need to close and re-open the GUI 

Use this option to automatically bypass all audio affecting functions, that aren’t currently visible on the GUI. For instance, when the bottom panel is hidden, the filters, dynamic eq and mono maker are disabled, regardless of their settings. when ticked, an explanation is shown, when hovering over a control Enable OpenGL GUI rendering 

Click to save the global settings and close the menu. Click on the hyperlink to visit The global settings are saved to: the Klanghelm website macOS: /Users/<username>/Library/Klanghelm/VUMTdeluxe/settings.xml Windows: C:/Users/<username>/AppData/Roaming/Klanghelm/VUMTdeluxe/settings.xml If running into issues, simply delete this file and the factory default global settings will be used again. 

13 

_Klanghelm VUMT deluxe - Manual_ 

## **Standalone Application** 

## **What to expect?** 

The Standalone App automatically saves its settings when closing the app and recalls them on its next launch. You can save and recall individual states via the options menu. Furthermore there is an „always-on-top“ option accessible via the options menu. 

If you’re running into issues when relaunching the app, delete the „audioSetup.xml“ and the „standaloneState.xml“ and restart the application. 

## **How to make it work in conjunction with a media player?** 

The VUMTdeluxe standalone needs a physical input to display levels, so you need to use a virtual audio cable such as the free one from jackaudio.org. 

There's a good tutorial in the download, how to connect the output of an audio application (iTunes or Windows Media Player for example) with the input of another program (VUMTdeluxe in this case). 

macOS: /Users/<username>/Library/Klanghelm/VUMTdeluxe 

Windows: C:/Users/<username>/AppData/Roaming/ Klanghelm/VUMTdeluxe 

14 

_Klanghelm VUMT deluxe - Manual_ 

## **Appendix: Meter Scales - Reading and Calibration** 

The chart below compares the different metering scales available in VUMT deluxe. In this case the calibration control in VUMT deluxe is set to „-18“ (the most common setting). 

Now, when feeding a -18dBFS sine wave at 1kHz into the meter you get these readouts: 

**==> picture [730 x 156] intentionally omitted <==**

***available in VUMT deluxe only** 

15 

_Klanghelm VUMT deluxe - Manual_ 

## **Appendix: Weighting Curves** 

***** 

*** according to ITU-R BS.1770-1** 

16 

_Klanghelm VUMT deluxe - Manual_ 

## **Credits** 

Code and GUI: Tony Frenzel 

Manual: Tony Frenzel Special thanks to the beta testers. 

VST and VST3 are trademarks of Steinberg Media Technologies GmbH. 

Audio Unit is a trademark of Apple, Inc. 

AAX is a trademark of Avid, Inc. 

17 

