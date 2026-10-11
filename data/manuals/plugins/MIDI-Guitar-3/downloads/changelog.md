Source: https://jam.live/downloads/changelog/

# Changelog

## 3.0.75 for iOS Sep-30-2026

Small update. iCloud folders and a few fixes.

## 3.0.75 Mac AUv3 version Sep-29-2026

Only available in the forum for now.

## 3.0.74 for Windows Sep-29-2026

Big update. Same as Mac below. Only available in the forum for now.

## 3.0.74 for iOS Sep-10-2026

On pair with the Mac version below.

## 3.0.74 for Mac Aug-31-2026

**IMPORTANT:**

* Due to a change in Apple policy in Tahoe 26.1 about AudioUnits in Logic/MainStage/Garageband, we had to move MIDI Guitar’s data folder from: `~/Library/Group Containers/X6D2Q4W5A8.midiguitargroup/` to `~/Library/Application Support/JamOrigin/`
* **This should all be automatic, and without need to reactivate the license. But you need to run the standalone application once before the AU/VST can see your patches and data. Please don’t manually delete the old App Group folder for now (this will cause reactivation of the license)**
* **When updating to 3.0.7x and beyond, please stop using any previous versions to avoid confusion.**

New **Midi Wind** tracker!

* A generic, monophonic tracker, that hopefully works with most instruments.
* Obviously different kinds of instruments and mic setups vary a lot, please provide feedback on how it works for you.
* Unlike other trackers, it has some knobs to adjust tracking quality/tradeoffs.
* Very fast (even faster than the monophonic guitar tracker when using guitar).
* Very responsive in low-dynamics playing (maybe too much).
* Might have octave errors (which is not common in all the other trackers).

New **Hex Flash** tracker!

* A bit faster than previous Hex tracker.
* Experimental. The previous Hex tracker is set as default and is already very good :)

New **External Tracker** support (JamStik, FTP, Seaboard, Osmose etc):

* It should now be possible to use most hardware controllers with MG3.
* MG3 will use the MIDI note-on, note-off from the controller.
* MG3 will use pressure/aftertouch/brightness from the controller OR alterbnatively can analyze its audio to produce MPE information from non-MPE controllers.
* For stringed controllers it will maintain pr. string mapping similar to MG Hex.
* Safety logic avoid hanging notes when the hardware midi connection is broken, interrupted or corrupt.
* Detects legato note overlaps.

New **Tracking Presets**: (Work-In-Progress)

* Now easier to switch among trackers, for example for two-guitar rigs.
* See [documentation](https://jam.live/docs/trackingpresets).

New **Deep Amp** freebie! (Work-In-Progress)

* **Deep Amp** is a (almost) zero-latency guitar FX/synth module.
* It preserves the guitar attack and transients and clean up the guitar signal in a profound way.
* Go-to solution for that "Metheny synth sound" (with appropriate reverb).
* Also a way to fatten up hex pickups to not sound flimsy.
* For normal pickups, this splits the polyphonic audio into a hex signal, reducing intermodulation distortions.
* **Deep Amp** also makes it possible for some MIDI FXs (eg. Sustainer) to work directly on guitar *audio*!
* Currently only the overdrive module can process such hex audio, but more is coming with the developement of **Guitar MODs** (currently unavailable).
* Since Deep Amp just an audio FX, you can add other FXs before and after it.
* Not entirely clear where this is going...

New **Morphing Chains**:

* Cable two chains in the Mixer will crossfade among them.
* This can be used creatively for adding guitar/audio transients to midi synths for zero latency responses.

New **MPE'izer** (Work-In-Progress)

* At the moment this will create a samplebank based on any VST/AU synth preset. The Sampler module is very limited at the moment though.
* Using **Fat Patches**, this makes it possible to port the exact same sound to iPads and other systems.
* This is a preparation for creating custom **Guitar Mods** audio FXs (not available yet).

New **Fat Patches**:

* The Share button creates a patch file that embed SampleBanks, IRs, NAMs, Backing Tracks, Lua scripts, which should be portable, even to iOS.

New **Patch Repositories**: (Work-In-Progress)

* Allows MG to download factory patches and adding factory patches along the way, without MG software updates, and keep the MG software small in size.
* It’s possible to add other peoples public patch repositories and download them.
* Since we have **Fat Patches** (embedding all external files and lua scripts), this way its possible to distribute highly customized stuff, safely to others, band members or an iPad.

New **NAM A2** support:

* Native support for NAM A2 models.

New **Recording module**:

* Record a wav file of the Chain audio
* "BlackHole" option to easily record any system audio (YouTube, etc), similar to the BlackHole software. Entitlement must be given in Mac => System Settings => Privacy & Security => Screen & System Audio Recording => System Audio Recording Only => Add the MIDI Guitar 3 App. Mac Only.

New **VST/AU Thumbs**:

* MG can show thumb images of AU/VST plugins in the UI.
* This require screen capture entitlement and thus is disabled by default.

New **MG APIs for hackers** (Work-In-Progress):

* [Overview](https://jam.live/developers/)
* [Lua API](https://jam.live/developers/lua)
* [JS API](https://jam.live/developers/websocket)

MIDI Output and Synth modules, **MIDI channel conventions**:

* Flipped the channels to be similar to most hardware midi guitar systems:
* Now it send notes on midi channel 2 (high E) .. channel 7 (low E). Previously it was channel 2 (low E) .. channel 7 (high E)

**UI**:

* Sharper contrasts.
* File based modules (IRs, NAMs, Backing tracks, etc) will list all files in the directory-tree set in preferences. On iOS, due to app sandboxing, we can only use the iOS file browser and otherwise list files that have been previously selected by the user.
* Hold mouse button will disconnect a cable but will also reset the knob to its default value.
* More consistent propagation of reactions when manipulating a complex chain of cables.
* Graphical scroll transitions.

**Bugfixes**:

* Fixed critial issue with Logic/MainState/Garageband arising in MacOS Tahoe 26.1
* Process MIDI Machines before instruments. This avoids issues like Transposer act as pitch shifter when playing a midi based synth.
* Reduced CPU load when a chain has a hex processing module and an instrument.
* 3rd party MIDI FX bypass will actually bypass.
* Fixed issue with using two different interfaces for input and output
* Fixed issue with two interfaces setups, where MG not getting correct samplerate information from the interface resulting in pitch issues and crackles.
* Fixed long standing issue where MG didn’t process things correctly when the DAW track or audio interface have no audio output channels.
* Fixed window resizing in Logic.
* MIDI output module select the direct output pr default on IOS AUv3.
* In Hex mode, MG AU channel layout changed to 8 mono channels.
* Fixed issue with some virtual midi outputs, that could not be reloaded in DAWs.
* Cabinet module save cable state.
* Faster app startup.

---

## 3.0.73 for iOS Jul-11-2026

[Forum post](https://jamosapien.com/t/mg-3-0-73-for-ios-ipados-released-on-testflight/15836)

External Tracker support (JamStick, FTP, Seaboard etc):

* It should now be possible to use most hardware controllers with MG3.
* MG3 will use the MIDI note-on, note-off from the controller.
* MG3 will use pressure/aftertouch/brightness from the controller OR alterbnatively can analyze its audio to produce MPE information from non-MPE controllers.
* For stringed controllers it will maintain pr. string mapping similar to MG Hex.
* Safety logic avoid hanging notes when the hardware midi connection is broken, interrupted or corrupt.
* Detects legato note overlaps.

MIDI Output and Synth modules, MIDI channel conventions:

* Flipped the channels to be similar to most hardware midi guitar systems:
* Now it send notes on midi channel 2 (high E) .. channel 7 (low E). Previously it was channel 2 (low E) .. channel 7 (high E)

Morphing Chains:

* Cable two chains in the Mixer will crossfade among them.
* This can be used creatively for adding guitar/audio transients to midi synths for zero latency responses.

Fat archive patches:

* The Share button creates a patch file that embed IRs, NAMs, SampleBanks, Backing Tracks, Lua scripts, which should be portable, even to iOS.
* There are some limits to how big the files can be, however (especially backing tracks can max be 50Mb).

Patch repositories:

* Allows MG to download factory patches.
* Allows adding factory patches along the way, without MG software updates, and also keeps the MG software small in size.
* Downloads will happen when updating to a new version or when clicking download.
* In settings/patches it’s possible to add other peoples public patch repositories and download them.
* Since patches can be fat (embedding external files and lua scripts), and Lua scripts are very general and safe, this way its possible to distribute highly customized stuff, safely to others, or to another machine.
* However, there are no factory patches yet.

Files:

* File based modules (IRs, NAMs, Backing tracks, etc) will list all files in the directory set in preferences.
* On iOS, due to app sandboxing, we can only use the iOS file browser and otherwise list files that have been previously selected by the user. Still missing some way to organize files.

Cabling/Reset:

* Hold mouse button will disconnect a cable but will also reset the knob to its default value.
* More consistent propagation of reactions when manipulating a complex chain of cables.

Bugfixes:

* Process MIDI Machines before instruments. This avoids issues like Transposer act as pitch shifter when playing a midi based synth.
* Reduced CPU load when a chain has a hex processing module and an instrument.
* 3rd party MIDI FX bypass will actually bypass.
* Fixed issue with using two different interfaces for input and output
* Fixed issue with two interfaces setups, where MG not getting correct samplerate information from the interface resulting in pitch issues and crackles.
* Fixed long standing issue where MG didn’t process things correctly when the DAW track or audio interface have no audio output channels.
* Fixed window resizing in Logic.
* MIDI output module select the direct output pr default on IOS AUv3.
* Fixed issue with some virtual midi outputs, that could not be reloaded in DAWs.
* Cabinet module save cable state.

UI:

* Polishing, sharper contrasts
* Graphical scroll transitions

---

## 3.0.73 Hex AUv3 version May-27-2026

Hex guitarists often run into limitations of enjoying the full power of hex pickups into their favorite DAW. This variation of the MG plugin seeks to make life wonderfully simple by letting the MG plugin open the hex hardware, rather than the DAW. But this AUv3 version still has issues in serveral DAWs (includin Abelton Live).

More information:
[More Details](https://jamosapien.com/t/unofficial-midi-guitar-3-hex-auv3-plugin-macos-is-now-on-testflight/15742)

---

## 3.0.72 for iOS Apr-22-2026

Only minor fixes

## 3.0.68 Jan-23-2026

Just minor fixes from yesterday's version:

Reduced CPU load when a chain has a hex processing module and an instrument.

Process MIDI Machines before instruments. This avoids issues like Transposer act as pitch shifter when playing an Instrument.

MIDI FX and Instruments: when switched off, 3.0.68 would simply pass through MIDI notes, but still process MIDI notes inside the MIDI FX.

Legato module adds 8ms as option.

NAM can process stereo.

NAM tonestack selector.

A potential fix for a strange issue with virtual midi outputs.

## 3.0.67 Jan-21-2026

Hides all experimental modules by default - enable in Settings => Plugins.

New AUv3 version (not quite, but soon) available on TestFlight. Opening dedicated audio (hex) inputs from works on this AUv3 version, but not on the AU and VST versions.

Plugins: New support for MIDI FXs plugins.

Plugins: Fixed MIDI 1.0 aftertouch/channelpressure problem.

Patch Bay: Can now aggregate MIDI controllers, filter MIDI Channel and MIDI Program Change messages.

Neural Amps, Cabinet and Reverb IR improved.

NAM: 10 new tonestack circuits in addition to the NAM official one.

NAM: All 6 knobs works and can be cabled and modulated.

Cabinet: IR-evolver fixed so it can also evolve IR files.

UI: New fretboard and scales visualizations.

UI: Before only the source of a wire could be affected. Now any switch/knob/slider in a wired chain affect all the others.

UI: When searching for plugins textually, sort the search results by name typed.

UI: Show little fire icon on Chain or some modules if they a very CPU intensive.

UI: Resize window is more smooth.

UI: Changing sample rates will reload the patch, rather than the introduction patch.

Lots of minor UI improvements and bug fixes.

## 3.0.66 Nov-3-2025

Dry guitar infinite sustain, piano-like sustain and freeze.
Morph cascading Mods.

## 3.0.64 Oct-22-2025

Preparing MIDI Guitar 3 for integration with other plugins, such as [Guitar Mods](https://jam.live/products/GM/).

## 3.0.63 May 25, 2025

All versions for all platforms milestone:
MIDI Guitar/Bass/Cello 3 for iOS, Mac and Windows.
Substantial CPU performance gains.
[More Details](https://jamosapien.com/t/midi-guitar-3-0-63-beta-release-notes/11110)

## 3.0.62 April-16-2025

MIDI Guitar 3 for iPadOS/iOS update.

## 3.0.61 Feb-21-2025

MIDI Bass 3 tracking update. Fast, reliable, duophonic bass tracking.
[More Details](https://jamosapien.com/t/midi-bass-3-first-beta-is-here/8531)

## 3.0.60 Feb-16-2025

MIDI Guitar 3 for iPadOS/iOS is available!

## 3.0.55 Oct-19-2024

String-to-MIDI mapping, 100% plugin-compatibility, new modules.

## 3.0.53 Oct-07-2024

MIDI Guitar networking.

## 3.0.52 Oct-02-2024

[MIDI Guitar 3 Hex](https://jam.live/products/MG3Hex/) fine tuning.

## 3.0.51 Sep-27-2024

[MIDI Guitar 3 Hex](https://jam.live/products/MG3Hex/) is avaiable!
