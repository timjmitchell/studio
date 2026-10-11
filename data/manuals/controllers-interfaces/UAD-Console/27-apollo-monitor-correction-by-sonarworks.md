Source: https://help.uaudio.com/hc/en-us/articles/31655084572820-Apollo-Monitor-Correction-by-Sonarworks
Updated: 2025-10-09T17:58:31Z

# Apollo Monitor Correction by Sonarworks

Apollo Monitor Correction by Sonarworks® brings seamless realtime SoundID Reference integration to Apollo X Gen 1 and Gen 2 interfaces. Harness Apollo Monitor Correction to apply custom profiles to your reference headphones or studio monitors to correct your room's acoustics. Your calibration profiles run in realtime on Apollo's DSP using studio-grade precision filters and alignment delays for stereo or multi-channel speaker systems. [Learn more at sonarworks.com](https://www.sonarworks.com/soundid-reference/integrations/ua-apollo-x).

![amc-7-1.png](https://help.uaudio.com/hc/article_attachments/36203754202004)

## Contents

* [What is Apollo Monitor Correction?](#h_01JCESVHAB8M1YRX31J596SAE0)
* [Important Operation Notes](#h_01JCESVHABPVQSX4D4XK5GPVES)
* [Licensing Apollo Monitor Correction](#h_01JCESVHAB6JAVQSG1R83377R1)
* [Calibrating Outputs with Apollo Monitor Correction](#h_01JCESVHABK712C28TBMW32097)
* [Create a speaker calibration profile](#h_01JCESVHAB6D4KRP2B5P8ZM6YN)
* [Monitor and Headphone Correction Controls](#h_01JCESVHABJD8FDYMD05PEPMH1)
* [More Information](#h_01JCESVHACEAT22QZF3XDQH2N6)

---

# What is Apollo Monitor Correction?

Apollo Monitor Correction works in conjunction with Sonarworks' SoundID Reference software to measure and correct inaccuracies in your monitoring systems. After creating calibration profiles of your listening environment with the SoundID Reference software and applying them to Apollo X, Apollo's onboard DSP delivers consistent and accurate studio reference sound to your speakers and headphones in realtime.

After your profiles are applied (transferred) to Apollo, DSP correction is controlled by UAD Console. Correction is always available at the monitor and headphone outputs of your Apollo X monitor unit, so the SoundID Reference app and plug-in are no longer needed.

* **Monitor correction –** Achieved by measuring your speakers and room response (using the SoundID Reference Measure app) with a measurement microphone to create a calibration profile, and applying that profile to your Apollo so it runs on DSP in realtime.
* **Headphone correction –** Achieved by applying headphone calibration profiles to your Apollo headphone output(s). Headphone profiles are predefined by Sonarworks, for correcting the inherent response curves of more than 500 popular headphone models.
* **Target mode –** SoundID Reference calibrates the output of your speakers and headphones to specific reference targets. You can choose from predefined targets (such as Flat Target, Dolby Atmos Music, or car audio) or create your own before applying the profile to Apollo.

**Critical:** Apollo Monitor Correction is controlled by UAD Console and runs on Apollo DSP. To prevent double-processing when Apollo Monitor Correction is active, do not use the SoundID Reference DAW plug-in or enable calibration in the SoundID Reference app.

See [Important Operation Notes](#h_01JCESVHABPVQSX4D4XK5GPVES) for more.

## Apollo Monitor Correction system requirements

### Sonarworks requirements

* macOS 11 Big Sur or newer
* Sonarworks SoundID Reference software version 5.12.1 or newer ([download](https://www.sonarworks.com/soundid-reference/download))
* Sonarworks SoundID Reference software license ([buy](https://www.sonarworks.com/soundid-reference/pricing))
* Sonarworks Apollo Monitor Correction Add-on license ([buy](https://www.sonarworks.com/soundid-reference/integrations/ua-apollo-x))
* Supported [measurement microphones](https://support.sonarworks.com/hc/en-us/articles/4409355630738-System-and-hardware-requirements-for-SoundID-Reference#01HSXKPXVQWVTTSPK87A43R4D5) for speaker calibration
* Supported [headphone models](https://www.sonarworks.com/soundid-reference/supported-headphones) for headphones calibration
* Internet connection for licensing (on startup, or every 24 hours) and to apply calibration profiles in Stereo mode with Bass Management enabled

### Apollo requirements

* UAD Software v11.5.1 and UAD Console v1.2.1 or newer — get from [UA Connect](https://www.uaudio.com/downloads/uad)
* Apollo X Series desktop or rack model — Gen 1 or Gen 2

|  |  |  |
| --- | --- | --- |
| **Supported Models** | **Gen 1** | **Gen 2** |
| **Desktop** | Apollo x4  Twin X Duo/Quad  Twin X USB Duo | Apollo x4  Twin X Duo/Quad |
| **Rack** | Apollo x6  Apollo x8  Apollo x8p  Apollo x16 | Apollo x6  Apollo x8  Apollo x8p  Apollo x16  Apollo x16D |

## Supported Apollo X monitor modes

Apollo Monitor Correction supports stereo monitoring mode, and all available [Apollo X Surround Sound](https://help.uaudio.com/hc/en-us/articles/26817449653012-Apollo-X-Surround-Sound) monitoring modes except LCRS.

---

# Important Operation Notes

* To use Apollo Monitor Correction, select the **Speakers**, **Headphones 1**, or **Headphones 2** (if available) output under the name of your Apollo monitor unit adjacent to the link icon (🔗) in SoundID Reference. Then choose a calibration profile and target mode for the output, and click the Apply profile to Apollo X button.
* After a calibration profile is applied to Apollo X in the SoundID Reference app, Apollo Monitor Correction always remains active unless it is bypassed or disabled in UAD Console. Apollo Monitor Correction cannot be disabled from within the SoundID Reference app.
* Because Apollo Monitor Correction only calibrates your monitor and headphone outputs, it can remain active when you export or bounce audio in your DAW (set and forget).
* Apollo Monitor Correction is enabled, disabled, and bypassed with UAD Console, and runs on Apollo DSP.
* SoundID Reference standalone cannot detect that Apollo Monitor Correction is active. To prevent double processing when Apollo Monitor Correction is active, do not use the SoundID Reference DAW plug-in, or enable calibration in the SoundID Reference app when Universal Audio Thunderbolt is selected as the standalone output device. If you do choose to use SoundID Reference for standalone processing with the Universal Audio Thunderbolt output, be sure to disable Apollo Monitor Correction in UAD Console. See [SoundID Reference processing](#h_01JCESVHABSR1X4D7AB3FQ8PXN) for more information.
* When Apollo Monitor Correction is active, UAD Console's output meters reflect the calibrated monitor output levels, so they won't match the signal levels in your DAW.
* Apollo Monitor Correction is not applied to Apollo ALT monitor outputs, digital mirror outputs, cues, cue mirrors, or the headphone outputs of non-monitor unit Apollos in a multi-unit setup.
* SoundID Reference software must be installed to use Apollo Monitor Correction. Do not uninstall SoundID Reference software. However, Apollo Monitor Correction does not require any of the following SoundID Reference software to be active to process audio:
  + SoundID Reference standalone app and driver
  + SoundID Reference DAW plug-ins
  + SoundID Reference Measure app

---

# About Sonarworks SoundID Reference Software

SoundID Reference is an independent software product that is developed and sold by Sonarworks. Universal Audio has partnered with Sonarworks to bring SoundID Reference integration to Apollo X.

This manual describes how to use the Apollo Monitor Correction feature with Apollo X and UAD Console. SoundID Reference has its own system and licensing requirements (in addition to Apollo X requirements). Sonarworks provides [complete documentation](https://www.sonarworks.com/soundid-reference/resources) and [support](https://support.sonarworks.com/hc/en-us) for their SoundID Reference software products.

## What is SoundID Reference integration?

Apollo Monitor Correction is a SoundID Reference add-on integration license that runs calibration profiles directly on Apollo's internal DSP, instead of being processed by the SoundID Reference app or plug-in.

## SoundID Reference license types

Sonarworks provides various [licensing options](https://www.sonarworks.com/soundid-reference/pricing) for SoundID Reference to meet your monitoring correction needs. Licenses are available for headphones, stereo, and multichannel systems.

**Note:** The stereo license includes subwoofer support. For true 2.1 channel systems, a multichannel license is required.

Although you can use SoundID Reference on its own with any Apollo (or other audio interface), for the best experience you'll need the Apollo Monitor Correction add-on license for hardware DSP integration with Apollo X.

## SoundID Reference functions

**Note:** Adjust these settings before you apply your calibration profile to Apollo X.

* **Calibration target modes –** When you apply a correction profile, you can adjust the output of your speakers or headphones to match a target mode. The default target mode for SoundID Reference is the Flat target, which provides an extremely flat and accurate mix target. However, many other target modes (such as Dolby) are available, which allow you to listen and mix to specific environments, EQ curves, or speakers. See [Calibration target modes](https://support.sonarworks.com/hc/en-us/articles/4411891303442-Calibration-target-modes) in the Sonarworks documentation for details.
* **Listening spot –** Adjusts the level of your speakers to compensate for the differences you hear at your listening position, as determined by the calibration measurements. When the Listening spot feature is disabled, the default stereo image is restored. See [What is the Listening Spot feature?](https://support.sonarworks.com/hc/en-us/articles/20367193341074-What-is-the-Listening-Spot-feature) in the Sonarworks documentation for details.
* **Limit controls –** Used to set a range on which calibration is applied, and the maximum levels of adjustment. With this feature, you can choose the ceiling for the maximum boost applied by calibration, along with some settings for the bass and treble ranges. See [Limit Controls](https://support.sonarworks.com/hc/en-us/articles/9639393569170-Limit-Controls) in the Sonarworks documentation for details.
* **Dry/Wet mix –** You can configure the Dry/Wet mix of your calibration target. The Dry/Wet mix gives you the option to hear the audio target in a "less corrected" state, effectively reducing the amount of correction applied to your speakers or headphones to match the target mode.
* **Apply Profile to Apollo X –** When you have adjusted settings for your calibration profile, this button sends the profile to your Apollo X, where it is loaded into the DSP on the selected outputs, and processes your audio.

## Already using SoundID Reference standalone?

**Tip:** See [Important Operation Notes](#h_01JCESVHABPVQSX4D4XK5GPVES).

### If you already have speaker calibration profiles

If you've already used SoundID Reference without Apollo Monitor Correction and have existing speaker calibration profiles created in SoundID Reference 4 or newer, you can [apply them to your Apollo X monitor unit](#h_01JCESVHABGSQ53N25NT2ZEB8V) for realtime DSP processing without remeasuring your speakers and room.

### If you don't have a speaker calibration profile, or are now using Apollo X Bass Management

If you don't already have a speaker calibration profile, or you previously measured a profile without Apollo X Bass Management, you should [remeasure your speakers and room](#h_01JCESVHAB6D4KRP2B5P8ZM6YN) with the SoundID Reference Measure app.

## Apollo Monitor Correction and SoundID Reference apps

When using Apollo Monitor Monitor Correction, you configure calibration features in different apps, as listed in this table.

|  |  |  |  |
| --- | --- | --- | --- |
| **Feature** | **Apollo X****& UAD Console** | **Sonarworks SoundID Reference app** | **Sonarworks SoundID Reference Measure app** |
| Create calibration profiles for your speakers and room |  |  | ✓ |
| Select calibration profiles for speakers and headphones |  | ✓ |  |
| Select target modes for different reference listening scenarios |  | ✓ |  |
| Enable/disable Listening Spot control |  | ✓ |  |
| Adjust Limit Controls |  | ✓ |  |
| Adjust dry/wet mix of a calibration profile |  | ✓ |  |
| Apply calibration profiles to the Apollo X monitor unit |  | ✓ |  |
| Enable/disable monitor correction and headphone correction (unloads DSP) | ✓ |  |  |
| Enable and disable Safe Headroom | ✓ |  |  |
| Soft bypass of Monitor / Headphone corrections | ✓ |  |  |
| UAD Console monitor meter displays results of realtime DSP monitor correction | ✓ |  |  |

## Apollo and SoundID Reference app presets

Sonarworks refers to processing outputs in SoundID Reference as *Presets*. Presets are displayed in the left panel of SoundID Reference. Presets contain the calibration profiles and target modes for each device output.

### Apollo DSP integration processing

Settings listed under your Apollo monitor unit are Apollo Monitor Correction presets. The SoundID Reference app transfers those settings directly to the hardware when you press the "Apply profile to Apollo X" button, after which the calibration profile runs on Apollo realtime DSP. Sonarworks refers to Apollo DSP processing as *Integration Mode*.

Your Apollo X monitor unit, along with its available outputs, automatically appears in the Presets panel when all system requirements are met.

**Tip:** The link icon (🔗) displayed next to the Apollo monitor unit name indicates that this Apollo is the integrated DSP hardware output device.

### SoundID Reference processing

Other audio device outputs in the left panel of SoundID Reference, which are displayed beneath your Apollo monitor unit and its outputs, are native SoundID Reference presets. These presets are processed by the SoundID Reference software using your computer's CPU. Sonarworks refers to this native processing as *SoundID Reference standalone*.

**Note:** When you enable SoundID Reference standalone processing, your system's sample rate may change.

SoundID Reference standalone processing does not have the same realtime advantages as the Apollo hardware DSP integration offered by Apollo Monitor Correction.

**Important:** Standalone device outputs should be deleted from SoundID Reference when using Apollo Monitor Correction, because SoundID Reference standalone does not recognize when Apollo Monitor Correction is active. To prevent double processing, don't manually add any device, including the "Universal Audio Thunderbolt" device, as a standalone output when using the Apollo Monitor Correction add-on.

**Tip:** Standalone device outputs don't have the integrated hardware link icon 🔗.

![](https://help.uaudio.com/hc/article_attachments/32051116544020)

*Don't enable SoundID standalone calibration when using* *Apollo Monitor Correction (causes double processing)*

### Don't enable SoundID Reference standalone

When a SoundID Reference standalone preset is enabled, you see the green "Calibration Enabled" button in the lower right corner of the SoundID Reference window. Don't enable this button when Apollo Monitor Correction is enabled in UAD Console! If a non-integrated preset is selected, you can disable it by deactivating this button, or by selecting one of the Apollo presets under your Apollo monitor unit

**Tip:** All standalone output devices can be removed from SoundID Reference without impacting Apollo Monitor Correction.

![](https://help.uaudio.com/hc/article_attachments/32051116547860)

If you enable a native SoundID Reference audio output, a warning dialog appears that explains how to prevent double processing. If you see this dialog, either disable calibration in SoundID Reference, or disable Apollo Monitor Correction in UAD Console.

![](https://help.uaudio.com/hc/article_attachments/32051132989204)

### Differences between Apollo Monitor Correction and SoundID Reference software

Apollo Monitor Correction, Sonarworks SoundID standalone (native CPU) and the Sonarworks SoundID plug-in all offer different features for audio correction, as shown in the table below..

|  |  |  |  |
| --- | --- | --- | --- |
| **Feature** | **Apollo Monitor Correction****(DSP)** | **Sonarworks SoundID Reference standalone (CPU)** | **Sonarworks SoundID Reference plug-in (CPU)** |
| Lowest possible latency | ✓ |  |  |
| Processed by Apollo DSP | ✓ |  |  |
| Runs natively on your computer's CPU |  | ✓ | ✓ |
| Record while hearing corrected audio in realtime | ✓ |  |  |
| Calibrated audio for speakers and headphones at the same time | ✓ |  |  |
| Multichannel calibrated playback | ✓ |  | ✓ |
| Virtual Monitoring Add-on (simulate spatial speakers on headphones) |  | ✓ | ✓ |
| Requires use of SoundID Reference audio driver |  | ✓ |  |

---

# Licensing Apollo Monitor Correction

Apollo Monitor Correction requires both a Sonarworks SoundID Reference license and the Apollo Monitor Correction Add-on license. When you open Monitor Correction windows in UAD Console, you are reminded to start a trial or obtain licenses if you do not have them.

![](https://help.uaudio.com/hc/article_attachments/32051116553492)

## Purchasing licenses

* Purchase the SoundID Reference license [here](https://www.sonarworks.com/soundid-reference/pricing). Note that you can purchase several different versions of SoundID Reference, including headphones only, stereo for speakers and headphones (includes subwoofer), and multichannel (includes 2.1), with or without included measurement microphones.
* Purchase the Apollo Monitor Correction Add-on license [here](https://www.sonarworks.com/soundid-reference/integrations/ua-apollo-x). The Apollo Monitor Correction Add-on supports headphones, stereo, and multi-channel profiles, depending on your SoundID Reference license.

There are two scenarios for Apollo Monitor Correction licensing.

1. **You have not licensed Sonarworks SoundID Reference software.** Add a Sonarworks SoundID Reference license, and the Apollo Monitor Correction Add-on license.
2. **You have licensed Sonarworks SoundID Reference software.** Add the Apollo Monitor Correction Add-on license.

## Activating Sonarworks licenses

1. Log in to your [Sonarworks account](https://www.sonarworks.com). If you don't have an account, you can create one there.
2. Hover over My Account, then click Licenses & Devices.
3. Click Register a new license.  
   ![](https://help.uaudio.com/hc/article_attachments/32051132993172)
4. Type or paste the license for the SoundID Reference or Apollo Monitor Correction Add-on license, and click Register.
5. When the license appears on your license page, click Activate on this device.

You will perform this procedure for each license (SoundID Reference and the Apollo Monitor Correction Add-on). Each license can be activated on up to three computers.

---

# Calibrating Outputs with Apollo Monitor Correction

**Tip:** See [Important Operation Notes](#h_01JCESVHABPVQSX4D4XK5GPVES).

Apollo Monitor Correction controls appear in the Monitor Column in UAD Console, and in the Monitor Controller window (for Main Monitor correction). To show or hide Apollo Monitor Correction controls, choose View > Section > Monitor Correction from the menus in UAD Console.

![](https://help.uaudio.com/hc/article_attachments/32051116556564)

*Show/Hide Monitor Correction options in UAD Console*

|  |  |
| --- | --- |
| amc-7-1.png | monitor-correction-no-amc.png |

*Monitor Correction shown (left) and not shown (right)* *in UAD Console's Monitor Controller wIndow*

Apollo Monitor Correction allows you to correct audio from your headphones, speakers, or both, depending on your license and the Apollo model used.

**Important:** After a calibration profile is applied to Apollo X in the SoundID Reference app, Apollo Monitor Correction always remains active unless it is bypassed or disabled in UAD Console. It cannot be disabled from within the SoundID Reference app.

**Jump to:**

* [Apply a speaker calibration profile to your Apollo](#h_01JCESVHABPV936E7WHDQAWE2G)
* [Apply a headphone calibration profile to your Apollo](#h_01JCESVHABXD6253TNQK14SJB9)
* [Metering with Apollo Monitor Correction](#h_01JCESVHAB6193BD8FZD35NK2C)

## Apply a speaker calibration profile to your Apollo

1. In UAD Console, in the Monitor Column, click Main Mon under Monitor Correction. The Monitor Controller window opens.  
     
   ![](https://help.uaudio.com/hc/article_attachments/32051116570772)  ![amc-7-1.png](https://help.uaudio.com/hc/article_attachments/36203754202004)
2. Click OPEN SoundID. The SoundID Reference app opens.
3. Under the name of your Apollo X monitor unit on the left side of the SoundID Reference window, **Speakers** should be selected.  
     
   ![](https://help.uaudio.com/hc/article_attachments/32051116577812)
4. Click Select your calibration profile to select a profile from the drop menu. Any calibration profiles you have created appear in this list.
5. Select a calibration profile. (If you haven't defined a speaker calibration profile yet, see [Create a speaker calibration profile](#h_01JCESVHAB6D4KRP2B5P8ZM6YN).)
6. Configure your calibration target mode and settings. See [Calibration target modes](https://support.sonarworks.com/hc/en-us/articles/4411891303442-Calibration-target-modes) for information.
7. Click Apply profile to Apollo X.

The calibration profile is applied and enabled on the corrected outputs of your Apollo X monitor unit.

### Default profile file locations

By default, calibration profiles are saved to and loaded from the following locations:

* **macOS:** ~/Library/Application Support/Sonarworks/SoundID Reference/Sonarworks Projects
* **Windows:** [system drive]:\Users\your username\AppData\Local\Sonarworks\SoundID Reference\Sonarworks Projects

**Note:** The *User/Library* and *user\AppData* folders on macOS and Windows are hidden by default. To access them, you will need to allow showing hidden files. Learn more here: [Where can I find my speaker profile?](https://support.sonarworks.com/hc/en-us/articles/360019882460)

## Apply a headphone calibration profile to your Apollo

Headphone calibration is applied only to headphone outputs on the Apollo X monitor unit. On a rack Apollo, you can apply two different headphone calibration profiles. On a desktop Apollo, you can apply a headphone correction profile only to HP1.

1. In UAD Console, in the Monitor Column, click Headphones under Monitor Correction. The Headphone Correction window opens.  
     
   ![](https://help.uaudio.com/hc/article_attachments/32051116584084)  **![](https://help.uaudio.com/hc/article_attachments/32051133007124)**
2. Under Calibration Profile, click Open SoundID.
3. Under the name of your Apollo monitor unit on the left side of the SoundID Reference window, **Headphones 1** should be selected.
4. Click Select your calibration profile to select a profile.
5. Select a calibration profile. (If you haven't defined a headphone calibration profile yet, see [Adding a new headphone profile](#h_01JCESVHABK4JHARVM7QET2TY7).)
6. Configure your calibration target mode and settings. See [Calibration target modes](https://support.sonarworks.com/hc/en-us/articles/4411891303442-Calibration-target-modes) for information.
7. Click Apply profile to Apollo X.

The calibration profile is applied and enabled to the headphones on your Apollo X monitor unit.

### Adding a new headphone profile

1. In SoundID Reference, click Select your calibration profile, or the current calibration profile.
2. Click Add a new headphone profile.
3. Select from the list of brands and models, or type to search for a brand or model.
4. Select the model, and when prompted, confirm the headphones.
5. Configure your calibration target mode and settings. See [Calibration target modes](https://support.sonarworks.com/hc/en-us/articles/4411891303442-Calibration-target-modes) for information.
6. Click Apply profile to Apollo X.

## Metering with Apollo Monitor Correction

* Output metering in UAD Console is adjusted to reflect the actual output post-processing (after any speaker correction, Bass Management, and Safe Headroom are applied). For this reason, UAD Console's output meters may not match your DAW level meters. Refer to your DAW's level meters when mixing.
* The left and right meters may not appear to be balanced when the Listening Spot feature is enabled. This is due to the measured level differences at your listening position.
* UAD Console's input channel meter levels are unchanged.
* When multi-unit cascading, monitor metering on expander units does not reflect speaker correction, Bass Management, or Safe Headroom adjustments.

---

# Create a speaker calibration profile

On your computer, open the SoundID Reference Measure app and click Get Started. To Open SoundID Reference Measure from within the SoundID Reference app, click Select your calibration profile (or the current calibration profile name) at the top of the window, and choose Create a new speaker profile. The app guides you through the process of measuring the frequency response of your room and speakers to create a monitor calibration profile.

For complete information, refer to Sonarworks' [Speaker measurements documentation](https://support.sonarworks.com/hc/en-us/sections/20338352751762-Speaker-measurements).

**Important:** When creating speaker calibration profile measurements, disable all plug-in processing on the microphone input, including any Unison plug-in, and don't add or remove plug-ins on other channels if Input Delay Compensation is enabled (or simply create a new UAD Console session).

## Apollo output settings

Set your output settings (in UAD Console Settings > Hardware) before you create and apply the calibration profile, then do not change them after the profile is created. Changing these settings after the calibration profile is measured will affect the accuracy of speaker corrections.

These settings are:

* Monitor levels (-10 dBv or +4 dBu for rack models, and 20 dBu or 14 dBu for desktop models)
* Output reference levels (-10 dBv or +4 dBu)
* Headroom (+20 dBu or +24 dBu)

**Note:** These settings are read-only while the speaker measurement process is occurring.

### Speaker trim settings

When creating a multichannel speaker calibration profile, you may be prompted by the SoundID Reference Measure app to adjust speaker trims for individual speakers in your room. The Speaker Utilities panel in the Monitor Controller window remains active while you are creating your speaker calibration profile for this purpose.

After a speaker calibration profile is applied to Apollo in SoundID Reference, individual speaker trims in the Speaker Utilities panel of UAD Console's Monitor Controller window cannot be adjusted.

## Apollo X Bass Management notes

* If you are using [Apollo X Bass Management](https://help.uaudio.com/hc/en-us/articles/30920209088404-Apollo-X-Bass-Management), make sure Bass Management is enabled when you measure your calibration profile. All Bass Management settings are retained when you apply the profile, and automatically managed by Apollo Monitor Correction. You cannot adjust Bass Management settings when Apollo Monitor Correction is enabled.
* If you currently use Apollo X Bass Management, but your monitor calibration profile was measured without Bass Management enabled, Bass Management is not used in the profile. Remeasure your profile to incorporate Bass Management.
* In Stereo mode with a subwoofer, Apollo Monitor Correction does not apply level adjustments or time alignment to the subwoofer in relation to the main L/R speaker levels. If the profile you measure with Bass Management enabled requires ±6 dB or more of correction in the bass frequencies covered by the subwoofer, we recommend that you adjust your speaker and subwoofer levels to compensate, then remeasure the profile. See [this Sonarworks article](https://support.sonarworks.com/hc/en-us/articles/22127922069138-Calibrated-bass-management-for-stereo-setups-with-UA-Apollo-X-integration) for more information.

---

# Monitor and Headphone Correction Controls

The Monitor Correction and Headphone Correction buttons are located in the UAD Console Monitor column. Click the MAIN MON button to open the Monitor Correction floating window, and the HEADPHONES button to open the Headphone Correction floating window.

**Tip:** You can show and hide these buttons with the UAD Console menu commands View > Section > Monitor Correction.

## Monitor Correction buttons (Monitor Column)

You can open Apollo Monitor Correction windows with the buttons in the Monitor Column for HEADPHONES and MAIN MON.

![](https://help.uaudio.com/hc/article_attachments/32051133008788)

You can toggle bypass of the Main Monitor corrections by hovering your mouse over the Main Mon button and clicking the IN button. When bypassed, the Main Mon button is dimmed and its label is italicized.

![](https://help.uaudio.com/hc/article_attachments/32051116587156)

## Monitor Correction windows

Both Apollo Monitor Correction windows (Main Monitor and Headphone Correction) include the same SoundID correction controls, as described below.

The Monitor Correction window also includes [Apollo X Bass Management](https://help.uaudio.com/hc/en-us/articles/30920209088404-Apollo-X-Bass-Management) features and Speaker Utilities.

The Headphone Correction window includes two tabs for HP1 and HP2 if the monitor unit is an Apollo X rack model, and HP1 only if the monitor unit is an Apollo Twin X or Apollo x4 desktop model.

**Note:** You cannot adjust Bass Management settings or use Speaker Utilities when a calibration profile is enabled. All monitor correction is controlled by the calibration profile, including any bass management and speaker trims that were active when the calibration profile was measured.

### Main Monitor Controller panel

![amc-7-1.png](https://help.uaudio.com/hc/article_attachments/36203754202004)

The Main Monitor Calibration profile area shows the calibration profile name and an image of the corrections that are applied by the profile.

### Headphone Correction panel

**![](https://help.uaudio.com/hc/article_attachments/32051116593428)**

The Headphone Calibration profile area shows the calibration profile name and an image of the corrections that are applied by the profile. Click the HP1 or HP2 tabs to show the calibration profiles for the two headphone outputs. On an Apollo desktop model, only HP1 appears.

## Calibration Profile / Open SoundID

Click the calibration profile name to open the SoundID app, where you can select another calibration profile, make target mode changes, and apply profiles to the Apollo.

## Main Monitor / Headphone Correction Enable

Click to toggle the main monitor or headphone corrections. There is a slight pause in audio output when the correction is applied or removed. Disabling processing is a hard bypass that unloads Apollo's DSP, so audible artifacts are more pronounced than the Bypass control.

**Tip:** Use Bypass to quickly toggle between corrected and uncorrected audio.

## Safe Headroom

![](https://help.uaudio.com/hc/article_attachments/32051116594580)

Click to enable Safe Headroom. The feature is enabled when the switch is lit. Safe Headroom prevents digital clipping in the frequencies that are boosted by the SoundID Reference profile. The Safe Headroom value is calculated from the maximum peak EQ level applied by a profile, and reduces the output level by this amount (indicated on the Safe Headroom button) when enabled.

Enabling Safe Headroom can cause very large reductions in output level if calibration files have large peaks.

## Bypass

![](https://help.uaudio.com/hc/article_attachments/32051133027732)

Click this switch to toggle speaker or headphone correction without disabling the features. This is a soft bypass that has minimal audio artifacts (DSP remains active), so you can quickly alternate between corrected and uncorrected audio.

You can also toggle the bypass for speaker corrections by hovering your mouse over the Main Mon button in UAD Console's monitor column, and clicking the IN button.

## Additional Controls in Monitor Controller window

When Apollo Monitor Correction is enabled, all features in the Bass Management panel of the Monitor Controller floating window are disabled. Bass Management controls are accounted for when you create your calibration profile, and managed by the profile. To configure Apollo X Bass Management (before you create a calibration profile) see [this article](https://help.uaudio.com/hc/en-us/articles/30920209088404-Apollo-X-Bass-Management).

## Apollo Monitor Correction latency

The following additional latency is incurred at the Apollo outputs when Apollo Monitor Correction is enabled on speakers or headphones.

* 1.5 ms at 44.1 and 48 kHz
* 0.75 ms at 88.2 and 96 kHz
* 0.7 ms at 176.4 and 192 kHz

## Apollo Monitor Correction DSP & filters

Apollo Monitor Correction uses 24 minimum phase biquad filters per channel for all satellite speakers, and 5 filters for the LFE/Sub channel.

### UAD-2 DSP Loads

* On a 9.1.6 surround system, the processing load is less than one DSP core.
* On an Apollo Twin X DUO when Bass Management, Monitor correction, and Headphone correction are active, the processing load is approximately 13% of one DSP core.

---

# More Information

## SoundID Reference system menu

You can access the SoundID Reference system menu from the macOS menu bar or the Windows system tray when SoundID Reference is running. The SoundID Reference system menu provides links to work with some SoundID Reference features, including updates, support, and preferences.

If you can't adjust target mode calibration controls in the SoundID Reference app, enable calibration from this menu. (Calibration controls are enabled when the menu says "Disable calibration').

![](https://help.uaudio.com/hc/article_attachments/32051116595732)

When using Apollo Monitor Correction, don't enable SoundID Reference standalone processing. You can see if a SoundID Reference standalone output is enabled in this menu.

![](https://help.uaudio.com/hc/article_attachments/32051133031444)

## Related Sonarworks support articles

* [Sonarworks setup guide](https://link.sonarworks.com/ua-setup-guide)
* [About the SoundID Apollo Integration](https://www.sonarworks.com/soundid-reference/integrations/ua-apollo-x)
* [Applying calibration on UA Apollo X devices (profile integration)](https://support.sonarworks.com/hc/en-us/articles/21839183300114)
* [Using third-party measurement microphones](https://support.sonarworks.com/hc/en-us/articles/360020099259-Using-third-party-measurement-microphones)
* [Sonarworks Reference 4 support](https://support.sonarworks.com/hc/en-us/articles/21839183300114)
