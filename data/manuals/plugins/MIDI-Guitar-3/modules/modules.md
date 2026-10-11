Source: https://jam.live/modules/modules/

# Modules

This page is under construction!

---

[**JAM ORIGIN**](https://jam.live/) plugins are modular systems that enables you to build custom guitar effects called [**Patches**](https://jam.live/modules/patches/). The building blocks of patches are called **Modules** and this page documents all the [**MIDI Guitar/Bass/Cello**](https://jam.live/products/) modules currently available.

---

## Trackers

The trackers listen to your guitar signal and immediately recognize the notes you are playing. This is where the magic happens and your guitar performance is translated into *notes and expressions*.

MIDI Guitar has four different tracker types:

---

### MIDI Guitar 3

OverviewDocumentation

![MG3_Standard_Tracker](https://jam.live/modules/images/320/MG3_Standard_Tracker.png)
Audio-to-MIDI conversion for guitar — no special pickup required.

![MG3_Standard_Tracker](https://jam.live/modules/images/320/MG3_Standard_Tracker.png)
This is the tried-and-true tracker, which is often referred to as the "standard" tracker. But rest assured, there's nothing standard about it!

This tracker is capable of monophonic and polyphonic pitch-to-MIDI transformations.

Please set your tuning, so that **MIDI Guitar 3** knows what to expect from your strings. Standard guitar tuning is (from top to bottom): E4 B3 G3 D3 A2 E2. **MIDI Guitar 3** can track notes down to C2. For lower tunings, [**MIDI Bass 3**](https://jam.live/modules/modules/#midi-bass-3) and [**MIDI Guitar 3 Hex**](https://jam.live/modules/modules/#midi-guitar-3-hex) can reach down to B0.

Make sure you set the input gain on your audio interface for a good dynamic range. Only use the **Input** knob if your audio interface input gain pre-amp is not giving you a suffciiently strong signal.

The **Gate** sets a threshold for how many notes are tracked. Set it low, for high responsiveness.

---

### MIDI Guitar 3 Hex

OverviewDocumentation

![MG3_Hex_Tracker](https://jam.live/modules/images/320/MG3_Hex_Tracker.png)
Audio-to-MIDI conversion for hex pickup-equipped guitars.

![MG3_Hex_Tracker](https://jam.live/modules/images/320/MG3_Hex_Tracker.png)
This enhanced per-string tracker offers maximum pitch-to-MIDI control and requires a hexaphonic pickup system for guitar or bass guitar.

Please set your tuning, so that **MIDI Guitar 3** knows what to expect from your strings. Standard guitar tuning is (from top to bottom): E4 B3 G3 D3 A2 E2.

If you use a custom hex pickup setup, you may have to set the string/audio channel mapping by clicking on *Configure*.

---

### MIDI Bass 3

OverviewDocumentation

![MG3_Bass_Tracker](https://jam.live/modules/images/320/MG3_Bass_Tracker.png)
Built with bass players and extended-range instrumentalists in mind.

![MG3_Bass_Tracker](https://jam.live/modules/images/320/MG3_Bass_Tracker.png)
This tracker is capable of monophonic and polyphonic pitch-to-MIDI transformations for bass and lower tunings.

Please set your tuning, so that **MIDI Bass 3** knows what to expect from your strings. Standard bass tuning is (from top to bottom): G2 D2 A1 E1. [**MIDI Bass 3**](https://jam.live/modules/modules/#midi-bass-3) can track down to B0.

Make sure you set the input gain on your audio interface for a good dynamic range. Only use the **Input** knob if your audio interface input gain pre-amp is not giving you a suffciiently strong signal.

The **Gate** sets a threshold for how many notes are tracked. Set it low, for high responsiveness.

---

### MIDI Cello 3

Audio-to-MIDI conversion for bowed strings — no special pickup required.

---

## Essentials

These four modules are the bread and butter of **MIDI Guitar 3**. **Chain** and **MIDI Patchbay** are fixed parts of the **MIDI Guitar 3** GUI and available in every patch. The **Modulators** and **MIDI Output** modules are user selectable per patch but are key to getting the most out of **MIDI Guitar 3**.

---

### Chain

OverviewDocumentation

![Chain](https://jam.live/modules/images/320/Chain_Empty.png)
Build your signal by placing **Modules** here.

![Chain](https://jam.live/modules/images/320/Chain_Loaded.png)
After being processed by the tracker, the guitar signal is sent into MIDI Guitar 3's chains. A chain is simply a column of **Modules** that flows from top to bottom. The output of each module is sent to the next module, just like a chain of guitar pedals.

Each chain's colour can by customized by clicking the dot at the top right of the chain.

---

### MIDI Patchbay

OverviewDocumentation

![MIDI Patchbay](https://jam.live/modules/images/320/MIDI_Patchbay.png)
Take instant control of MIDI Guitar 3 and loaded 3rd-party plug-in parameters.

![MIDI Patchbay](https://jam.live/modules/images/320/MIDI_Patchbay.png)
Almost anything (knobs or buttons) can be controlled by physical MIDI/expression pedals. The position of MIDI pedals is directly visible in the user interface and virtual cables makes it easy to see what's being controlled.
If you don't have a MIDI controller, you can use the computer keyboard's number keys 1..9 to toggle the min/max vaules on each of the nine automation slots.

The first two slots are dedicated to stepping through patches.

MIDI Guitar 3 also responds to MIDI program change messages. The order of presets follows the order of files in MIDI Guitar 3's preset folder structure. So, the very first preset in the top folder of your user presets will respond to PC#000, the second preset to PC#001, etc.

---

### Modulators

OverviewDocumentationVideo

![Modulators](https://jam.live/modules/images/320/Modulators.png)
Control and shape your sound over time with **Modulators**.

![Modulators](https://jam.live/modules/images/320/Modulators.png)
Almost anything (knobs or buttons) can also be controlled by modulators. **Modulators** are control signals. For example you can control a [Whammy](https://jam.live/modules/modules/#whammy) with a **Wobble**-modulator for an auto-vibrato effect.

There are also **Modulators** that extract signals from your guitar, such as **Loudness**, **Brightness** and **Pitch** envelopes. These are polyphonic — each cable carries 6 independent control signals — one for each note.

**Modulators** can also modulate parameters of other **Modulators**, which makes it possible to make complex or unpredictable control mechanisms.

The **Modulators** module gives you fine-level control of linkable parameters.

MIDI guitar 3 features 10 modulator types. They can be linked to parameters to change or modify their values. Each of the four top-level waveforms can be clicked to select the modulator type. Additional controls become visible when the mouse pointer is hovered over the waveform. Adjusting these transforms the motion of the modulator.

The knobs on the right side of the window give visual feedback on the values the adjacent modulator is creating and can be linked to various parameters.

MIDI controllers can also be linked to parameters in the module for real-time control of a modulator's waveform, generating some interesting possibilities.

* **Modulator types:** OFF, ADSR, STRIKE, PRESSURE, BRIGHTNESS, WOBBLE, MUX, SINE, SAW, SQUARE, INVERT.

---

### MIDI Output

OverviewDocumentationVideo

![MIDI Output](https://jam.live/modules/images/320/MIDI_Output.png)
Send MIDI from **MIDI Guitar 3** to DAWs or external synthesizers.

![MIDI Output](https://jam.live/modules/images/320/MIDI_Output.png)

The **MIDI Output** module is used to send MIDI out from MG3 to external MIDI port destinations rather than internally hosted plugins.

Click on the box under MIDI Output for a menu of selectable MIDI output ports. You can select any port registered under your device’s operating system.

MacOS: When using MG3 as an Audio Unit (AU) plugin, a virtual MIDI port is created that will be visible to your DAW and other applications. You can also select other MIDI outputs seen by the operating system. Do not select Direct MIDI Output when using the AU plugin.

However, when using the VST2/3 versions of the plugin, this device will automatically select Direct MIDI Output (displayed as “Sending MIDI out to the track”), which will change the method of MIDI routing. (See attached image in Ableton Live to compare the difference). No MIDI Output is also selectable.

The left side of the window shows adjustable MPE parameters Strike (velocity), Pressure (aftertouch), Brightness (akin to Slide/CC74), and Glide (Pitch)parameters that directly transmit MIDI data to the output in all modes. They can also be modulated with a linked MIDI control device.

The four boxes below the preset title can be linked via virtual cable to CCs from the MIDI patchbay. Click on the box to open a screen for selecting a MIDI CC number to associate with each box. You can choose to learn a parameter from the plugin’s editor view.

On the right of the window are the device’s MIDI transmission parameters. Be sure to match these settings to the receiving synth’s bend range!

There are three MIDI modes — MIDI MPE (Default), MIDI 1.0 LEGACY and MIDI 1.0 MULTICHANNEL — each with its own unique MIDI output characteristics depending on the output protocol. Each has additional parameters to control parameters including: transmitting MIDI channel; aftertouch/channel pressure; and (pitch) bend range.

* Strike (velocity) —
* Pressure (aftertouch) —
* Brightness (akin to SLIDE/CC74) —
* Release (release velocity) -
* Glide (pitch) —

MIDI MPE (Default): transmits outgoing MIDI notes/data on channels 2-9 (not 8) in a round-robin fashion. When using the Hex tracker, strings map to individual MIDI channels for multichannel mode.

* Channel pressure, Aftertouch, No pressure.
* Bend range: 0,1, 2, 4, 8, 12, 24, 36, 48

MIDI 1.0 Legacy: transmits outgoing MIDI notes/data on the selected channel.

* Channel number: 1-16.
* Channel pressure, Aftertouch, No pressure.
* Bend range: 0,1, 2, 4, 8, 12, 24, 36, 48

MIDI 1.0 Multichannel: transmits outgoing MIDI notes/data on channels 2-9 (not 8) in a round-robin fashion. When using the Hex tracker, strings map to individual MIDI channels for multichannel mode.

* Channel pressure, Aftertouch, No pressure.
* Bend range: 0,1, 2, 4, 8, 12, 24, 36, 48

---

## Articulation

These modules let you take advanced control of the way you shape your sound beyond the realm of "normal" guitar sounds and into the infinite.

---

### Sustainer

OverviewDocumentationVideo

![Sustainer](https://jam.live/modules/images/320/Sustainer.png)
Infinite sustain, frozen chords or piano-like sustain for your guitar.

![Sustainer](https://jam.live/modules/images/320/Sustainer.png)
The **Sustainer** module controls the duration of outgoing MIDI notes to be much longer than physically possible with a guitar string’s natural attack-decay envelope profile.

In three flavors — Infinite Sustain, Freeze Chord and Piano-like Sustain — the module gives users total control over note duration like never before.

* **Infinite Sustain** — Triggers infinite sustain of the most recently played note until a new note is played, at which point the hold retriggers with the new note.
* **Freeze Chord** — Once a freeze begins all active notes are held and no new notes will sound until the hold is released.
* **Piano-like Sustain** — When active, played notes sustain for the selected release time. New notes ring out. Range: 0ms - 10 seconds

---

### Dynamics

OverviewDocumentation

![Dynamics](https://jam.live/modules/images/320/Dynamics.png)
Bring your sound to life, or tone it down

![Dynamics](https://jam.live/modules/images/320/Dynamics.png)
The **Dynamics** module can be used to control velocity (MIDI volume) and pressure (MIDI sustain) values.

* **Compress** — raises the overall velocity level resulting in increased volume.
* **Hold Press** — raises the overall pressure (aftertouch) level.
* **Tone** — center value maintains volume / max. / min. cut volume.

### Legato

OverviewDocumentation

![Legato](https://jam.live/modules/images/320/Legato.png)
More keyboard-esque control over your guitar's note articluation

![Legato](https://jam.live/modules/images/320/Legato.png)
The **Legato** module matches note-on and note-off events and makes legato transitions between them rather than retriggering them.

More legato, less polyphony: No note stealing; Steal note range 1-12. This mode steals notes sounding within a range of 1 to 12 semitones, similar to how a keyboard functions, where you can play legato by pressing a second note, then releasing the first.

More legato, longer notes: No note extension; 1 - 100ms note extension. This mode extends note sustain by 1-100 ms, which increases the likelihood that the next note can be captured and articulated as legato, in which case the first note is turned off.

Polyphony and bends have been improved since MIDI Guitar 2 and both options can be turned off. When a note is captured this way, it’s marked as legato, the subsequent modules (ie. your synth) can react to it.

---

### Gain

OverviewDocumentation

![Gain](https://jam.live/modules/images/320/Gain.png)
Boost or cut input signal

![Gain](https://jam.live/modules/images/320/Gain.png)
The **Gain** module controls the MIDI velocity level (volume) reaching an instrument. The default value is zero.

* **Range**: -40dB (mute) to +10.

### String Gain

OverviewDocumentation

![String Gain](https://jam.live/modules/images/320/String_Gain_Hex.png)
Boost or cut input signal per string in MIDI Guitar 3 Hex

![String Gain](https://jam.live/modules/images/320/String_Gain_Hex.png)
The **String Gain** module controls the MIDI velocity level (volume) of each string's signal reaching an instrument. The default value is zero.

* **Range**: -40dB (mute) to +10.

---

## Pitch

**MIDI Guitar 3** features ultra-high quality, real-time, polyphonic audio pitch shifting. It will also transpose and bend MIDI notes accordingly.

**Guitar Mods** delivers the lowest possible latency and uses pitch shifting with ultra-low latency, but consequently produces lower fidelity than **MIDI Guitar 3**'s pitch shifting.

You can freely cascade different pitch modules without degradation of audio quality or CPU activity.

---

### Chromatic

OverviewDocumentation

![Chromatic](https://jam.live/modules/images/320/Chromatic.png)
Pitch control for fixed-pitch instruments, like piano.

![Chromatic](https://jam.live/modules/images/320/Chromatic.png)
The **Chromatic** module controls the passing of pitch-bend data. Bent notes (and pre-bent release notes) retrigger as a new note-on event occurs. Useful for instruments like pianos that don’t typically use pitch-bend.

* **No bends allowed:** Sends a zero value for all pitch-bend data.
* **Allow bends of 1–4 semitones:** Limits the pitch-bend range up to the selected amount.
* **Reevaluate Strike:** Does not retrigger velocity when note-on occurs.
* **Preserve Strike:** Retriggers the original velocity, giving the note a stronger feel.

---

### Transposer

OverviewDocumentation

![Transposer](https://jam.live/modules/images/320/Transposer.png)
Two octaves up, two octaves down...it's your move.

![Transposer](https://jam.live/modules/images/320/Transposer.png)
The Transposer module globally shifts the tuning in incremental octaves, semitones and cents. This applies for both MIDI notes and audio pitch shifting.

* **Octaves**: -2 to +2 (default -1).
* **Semitones**: -12 to +12 (default 0).
* **Cents**: -50 to +50 (default 0).
* **On/Off**: engages Transposer module (default Off).

---

### Whammy

OverviewDocumentation

![Whammy](https://jam.live/modules/images/320/Whammy.png)
Bend notes to your will.

![Whammy](https://jam.live/modules/images/320/Whammy.png)
The **Whammy** module is a pitch-bend tool for audio and MIDI that simulates the function of a Whammy pedal with a maximum +/- 12 semitone bend range. By assigning this module to a MIDI CC — or modulator — the pitch of an in-line synthesizer or audio signal can be manipulated according to the range limits set.

The default knob value is 50 (no bend).

!!!Note: The bend range is relative to the bend range setting in the target synth, i.e. if the synth is set to +/ -2 semitones PBR, setting the Whammy to +/-12 semitones will provide the full range +/- 2 semitone range. If the Whammy is set to +/-2 semitones, its output will be scaled to 1/6th of the total pitch bend range, effectively becoming a microtonal bender.

* From: -12 to 0
* To: 0 to +12

---

### Vibrato

OverviewDocumentation

![Vibrato](https://jam.live/modules/images/320/Vibrato.png)
Auto vibrato within a set pitch range.

![Vibrato](https://jam.live/modules/images/320/Vibrato.png)
The **Vibrato** module introduces rapid pitch modulation to a sustained MIDI note. It can be used similarly to how a keyboard’s modulation wheel is often used.

* **Onset**: sets the amount of time it takes for the vibrato to reach full speed. Range 0-100 (default 50).
* **Speed**: sets how fast the vibrato cycles.
* **Amount**: sets how much modulation is applied to the pitch over a range of 0-100 (default 50).

---

### Retuning

OverviewOverviewVideo

![Retuning](https://jam.live/modules/images/320/Retuning.png)
Retune your instrument's output any way you wish.

![Retuning](https://jam.live/modules/images/320/Retuning.png)
The Retuning module enables fine-tuning control over specific MIDI pitches produced.

Import of .scl and .kbm files is supported. Please select the folder location of these files within MG3’s settings.

* Octave Division — 6 to 18 (Defaut 12). This number sets the division of the octave, or teh number of notes in each octave. For reference: 6 = the whole-tone scale; 12 = the chromatic scale.
* **Tonic** — E1 to G#6 (Deafault E2). The selected note is the pitch point from where the octave’s division is measured.
* **Import** — click to import scale file.
* **Notes** — drag or modulate to retune. Each note in the Note Wheel can be dragged (or modulated) to be retuned when detected by the tracker.

---

### String Retuning (Hex)

OverviewOverviewVideo

![Retuning](https://jam.live/modules/images/320/String_Retuning.png)
Retune your hex-equiped guitar's tuning without touching the tuning pegs.

![Retuning](https://jam.live/modules/images/320/String_Retuning.png)
The String Retuning module enables the retuning of each string from the hex feed’s outgoing MIDI in semitones and cents.

* **Semitones**: -24 to +24 (default 0).
* **Cents**: -50 to +50 (default 0).
* **On/Off**: engages String Tuning module (default Off).

---

### Chord Shifter (Hex)

OverviewDocumentation

![Chord Shifter](https://jam.live/modules/images/320/Chord_Shifter.png)
Generate string-independent upward and downward polyphonic bends from a central chord.

![Chord Shifter](https://jam.live/modules/images/320/Chord_Shifter.png)
The **Chord Shifter** module makes string-independent upward and downward polyphonic bends from a central chord possible. Think of it like a B-bender on steroids. Each string has individual **Heel**, **Middle** and **Toe** pitch settings so you can create all manner of weird and wonderful pitch movements. Each string has a +/- 1 octave range. Setting **X** will deactivate bending on the given string in the defined direction.

---

## Note Filters

**MIDI Guitar 3** has extensive filtering options to give you maximum control over your guitar signal's effect on virtual instruments.

---

### Auto Bassist

OverviewDocumentation

![Auto Bassist](https://jam.live/modules/images/320/Auto_Bassist.png)
Extract a bass-line that will play along with your chords.

![Auto Bassist](https://jam.live/modules/images/320/Auto_Bassist.png)
The **Auto Bassist** module sets a note filter to restrict the upper-limit range of playable notes. The default setting is A3 (equivalent to the 2nd fret on the G string). Only notes above the limit will sound when played.
<!---
(There should be something more to this, but it's hard to explain: it will extract the lowest notes played at any time, as a bass line. I think it will also legato among notes when possible, and when the synth supports legato, but need to check up on it)

* **Range** — E1 to G6.
  --->

---

### Auto Melody

OverviewDocumentation

![Auto Melody](https://jam.live/modules/images/320/Auto_Melody.png)
Extract a melody-line that will play along with your chords.

![Auto Melody](https://jam.live/modules/images/320/Auto_Melody.png)
The **Auto Melody** module sets a note filter to restrict the lower-limit range of playable notes. The default setting is A3 (equivalent to the 2nd fret on the G string). Only notes below the limit will sound when played.
<!---
(there should be something more to this, but hard to explain: it will extract the highest notes played at any time, as a melody line. I think it will also legato among notes when possible, and when the synth supports legato, but need to check up on it)

* **Range** — E1 to G6.
  --->

---

### Pitch Filter

OverviewDocumentation

![Pitch Filter](https://jam.live/modules/images/320/Pitch_Filter.png)
Filter pitches!

![Pitch Filter](https://jam.live/modules/images/320/Pitch_Filter.png)
Filter pitches!

---

### Scale Filter

OverviewDocumentation

![Scale Filter](https://jam.live/modules/images/320/Scale_Filter.png)
Filter scales!

![Scale Filter](https://jam.live/modules/images/320/Scale_Filter.png)
Filter scales!

---

### Strike Filter

OverviewDocumentation

![Strike Filter](https://jam.live/modules/images/320/Strike_Filter.png)
Control intensity.

![Strike Filter](https://jam.live/modules/images/320/Strike_Filter.png)
The **Strike Filter** module...

---

### String Filter

OverviewDocumentation

![String Filter](https://jam.live/modules/images/320/String_Filter.png)
Select specific strings to target an instrument.

![String Filter](https://jam.live/modules/images/320/String_Filter.png)
The **STring Filter** module enables selection of specific strings to target an instrument....

---

### Mute Open Strings

OverviewDocumentation

![Mute Open Strings](https://jam.live/modules/modules/images/320/Mute_Open_Strings.png)
Block individual open strings from sounding.

![Mute Open Strings](https://jam.live/modules/modules/images/320/Mute_Open_Strings.png)
This filter has no GUI. It simply prevents the execution of open strings.

---

## Sequencers

**MIDI Guitar 3** lets you play evolving rhythmic patterns, tightly synced melodic lines, and complex generative textures—while still performing expressively on the guitar. Because MG3 tracks pitch, dynamics, and articulation, sequencer effects respond musically to your playing rather than feeling rigid or machine-driven, giving you a hybrid workflow that blends guitar feel with electronic sequencing.

---

### Arpeggiator

OverviewDocumentationVideo

![Arpeggiator](https://jam.live/modules/images/320/Arpeggiator.png)
Put more movement in your guitar moves.

![Arpeggiator](https://jam.live/modules/images/320/Arpeggiator.png)
**Arpeggiator** rhythmically splits up the notes of a static chord voicing into steps spread over multiple octaves to add movement to a performance. Playing a single note will also generate a rhythmic event.

Click on a square to highlight it and activate a step in the pattern. The position of a colored square relative to the squares on its left and right will determine the upward or downward movement of the pattern. Leaving blank spaces in the pattern can generate rhythmic interest.

There are four user-configurable pattern presets accessible by clicking on the 4 buttons (labeled 0-3) in the bottom left of the module.

Note: The module’s operation is dependent on the transport’s **Play** control being active. The pattern will cycle at the selected tempo as long as the transport is active, even if the module is in an off state.

* **Steps** — Hover over a box on the grid. It shows as grey until you click to activate a step at which point the box takes on the color of the chain it is instantiated within.
* **Preset** — Click on 0, 1, 2, or 3 to select a user-generated arpeggiator pattern.

---

### Shredder

OverviewDocumentationVideo

![Shredder](https://jam.live/modules/modules/images/320/Shreder.png)
Shred without the RSI risk.

![Shredder](https://jam.live/modules/modules/images/320/Shreder.png)
The Shredder module, different from the Sequencer module, modifies incoming MIDI note data. It chops MIDI note data into finer divisions and repitches them rhythmically over a full two-octave range.

Click on a square to highlight it and activate a step in the pattern. The position of a colored square relative to the squares on its left and right will determine the upward or downward movement of the pattern. Leaving blank spaces in the pattern can generate rhythmic interest.

There are four user-configurable pattern presets accessible by clicking on the 4 buttons (labeled 0-3) in the bottom left of the module.

The scale selector enables the setting of a root note and one of 4 modes: major, minor, chromatic, and drum map. The root note corresponds to the lighter grey lines of the grid. Due to the limited range of the grid, in Chromatic mode the root note sets the pitch at the middle horizontal line.

The selected root/scale will apply to all four presets.

**Note:** This module’s operation is dependent on the transport’s **Play** control being active. The loop will repeat as long as the transport is active at the selected tempo.

---

### Sequencer

OverviewDocumentationVideo

![Sequencer](https://jam.live/modules/images/320/Sequencer.png)

![Sequencer](https://jam.live/modules/images/320/Looper.png)

---

---

### Looper

OverviewDocumentationVideo

![Looper](https://jam.live/modules/images/320/Looper.png)
Round and round we go, cycling your musical ideas.

![Looper](https://jam.live/modules/images/320/Looper.png)
The Looper module records and plays back a looped performance of MIDI notes captured while the record button is engaged.

Press the On/Off button to start recording; press it again to stop recording and automatically start playback.

Each full rotation of the play head is equal to a bar of 4/4

Click on the metronome icon to clear a recorded loop.

Multiple Looper modules can be employed simultaneously in MIDI Guitar 3.

Note: The module’s operation is dependent on the transport’s Play control being active. The loop will repeat as long as the transport is active at the selected tempo.

* **Play** — this must be active to hear playback of the loop.
* **Metronome** — clears loop buffer contents.
* **On/Off** — Must be active to record data into the loop.

---

## Tools

### Poly Tuner

OverviewDocumentation

![Poly Tuner](https://jam.live/modules/modules/images/320/Poly_Tuner.png)
A highly colourful tuning meter

![Poly Tuner](https://jam.live/modules/modules/images/320/Poly_Tuner.png)
The tuner to end all tuners!

### Scales

OverviewDocumentation

![Scales](https://jam.live/modules/modules/images/320/Scales.png)
Visualize scales on a fretboard

![Scales](https://jam.live/modules/modules/images/320/Scales.png)

### Fretboard

OverviewDocumentation

![Fretboard](https://jam.live/modules/modules/images/320/Fretboard.png)
Visualize notes on a fretboard

![Fretboard](https://jam.live/modules/modules/images/320/Fretboard.png)

### Keyboard

OverviewDocumentation

![Keyboard](https://jam.live/modules/modules/images/320/Keyboard.png)
Visualize notes on a keyboard.

![Keyboard](https://jam.live/modules/modules/images/320/Keyboard.png)

### Seeboard

OverviewDocumentation

![Seaboard](https://jam.live/modules/modules/images/320/Seaboard.png)
Visualize notes on a "Seeboard".

![Seaboard](https://jam.live/modules/modules/images/320/Seaboard.png)

---

---

## Instruments

---

### VST/Audio Unit Instruments

OverviewDocumentation

![Instrument](https://jam.live/modules/images/320/Plugin_Loader_Inst_3.png)
Load any third-party synth or plugin.

![Instrument](https://jam.live/modules/images/320/Plugin_Loader_Inst_3.png)

The Instruments device is used to select instrument plugins for loading in chains. Plugins are subcategoried by developer name folders. Selecting an instrument loads a module. Simply put, this device loads software synthesizers.

Once launched, the name of the instantiated plugin will appear at the top of the plugin box. Click on the highlighted name below (“Untitled” in the accompanying example image) to open the plugin’s GUI for parameter editing.

The four boxes below the preset title can be linked via virtual cable to CCs from the **MIDI Patchbay**. Click on the box to open a screen for selecting a parameter or MIDI CC number to associate with each box. You can choose to learn a parameter from the plugin’s editor view.

The device shares common parameters with the [MIDI Output](https://jam.live/modules/modules/#midi-output) module.

---

## MIDI Machines

---

### VST/Audio Unit MIDI Effects

OverviewDocumentation

![Instrument](https://jam.live/modules/images/320/Plugin_Loader_Inst_3.png)
Load any third-party MIDI FX plugin.

![Instrument](https://jam.live/modules/images/320/Plugin_Loader_Inst_3.png)

---

## Mods

Hex pickups and **Mods**

The dry sound of many hexaphonic pickups is comparitively weak and thin, in particular when the pickup sits directly adjacent to the bridge — as typically suggested by manufacturers. For this reason, **Mods** requires the regular guitar pickup signal for optimal function.

When using a GK-5 pickup, a dual jack-cable setup is required. For GK-3 pickups, the patch cable is needed and the GK-3's selector switch should be set to "Guitar".

---

### Bassoon Mod

---

### Cello Mod

---

### Clarinet Mod

---

### Mellow Mod

---

### Sax Mod

---

### Synth Mod

---

### Trombone Mod

---

## Mod effects

Many modules [apply to **Mods**](https://jam.live/modules/), but these three *only* apply to **Mods**.

---

### Unison

---

### Harmonics

---

### Swell

---

## Note Filters

---

### Auto Bassist

OverviewDocumentation

![Auto Bassist](https://jam.live/modules/images/320/Auto_Bassist.png)
Extract a bass-line that will play along with your chords.

![Auto Bassist](https://jam.live/modules/images/320/Auto_Bassist.png)

The Auto Bassist module sets a note filter to restrict the upper-limit range of playable notes. The default setting is A3 (equivalent to the 2nd fret on the G string). Only notes above the limit will sound when played.

* **Range** — E1 to G6.

(there should be something more to this, but hard to explain: it will extract the lowest notes played at any time, as a bass line. I think it will also legato among notes when possible, and when the synth supports legato, but need to check up on it)

---

### Auto Melody

OverviewDocumentation

![Auto Melody](https://jam.live/modules/images/320/Auto_Melody.png)
Extract a melody-line that will play along with your chords.

![Auto Melody](https://jam.live/modules/images/320/Auto_Melody.png)

The Auto Melody module sets a note filter to restrict the lower-limit range of playable notes. The default setting is A3 (equivalent to the 2nd fret on the G string). Only notes below the limit will sound when played.

(there should be something more to this, but hard to explain: it will extract the highest notes played at any time, as a melody line. I think it will also legato among notes when possible, and when the synth supports legato, but need to check up on it)

* **Range** — E1 to G6.

---

### Scale Filter

```
Boost or add ambience to notes in a given scale.
```

---

### Pitch Filter

```
Boost or add ambience to high or low pitched notes.
```

---

### Strike Filter

```
Boost or add ambience to notes based on how hard you hit them.
```

---

## Hexaphonic exclusive

All modules works with hexaphonic pickup systems, but five modules *only* works with hexaphonic systems:

Use the main guitar pickup for audio when possible!

Many hexaphonic pickups sounds quite awful, weak and thin, in particular when they sit right next to the bridge as advertised. For this reason [**MIDI Guitar 3 Hex**](https://jam.live/products/MG3Hex/) defaults to use the main guitar pickup for audio, and only use the hex pickup for tracking. However, when using any of these **Hexaphonic exclusive** effects, **MIDI Guitar 3 Hex** is forced to use the hex pickup for audio in the [**Chain**](https://jam.live/modules/modules/#chain), and you get the hex pickup audio rather than the main pickup audio.

---

### String Retuning

---

### String Filter

---

### Chord Shifter

---

### Open String Mute

---

## Audio Effects

---

### VST/Audio Unit Effects

OverviewDocumentation

![Effects](https://jam.live/modules/images/320/Neural_Amp_Modeler_Standard.png)
Load any 3rd-party audio effect plugin.

![Effects](https://jam.live/modules/images/320/Neural_Amp_Modeler_Standard.png)
The Instruments device is used to select instrument plugins for loading in chains. Plugins are subcategoried by developer name folders. Selecting an instrument loads a module. Simply put, this device loads software synthesizers.

Once launched, the name of the instantiated plugin will appear at the top of the plugin box. Click on the highlighted name below (“60’s Laser Tag” in the accompanying example image) to open the plugin’s GUI for parameter editing.

The four boxes below the preset title can be linked via virtual cable to CCs from the MIDI patchbay. Click on the box to open a screen for selecting a parameter or MIDI CC number to associate with each box. You can choose to learn a parameter from the plugin’s editor view.

Time-based effects will receive tempo messages from the master clock.

---

### Neural Amp Models

OverviewDocumentation

![Neural Amp Models](https://jam.live/modules/images/320/Neural_Amp_Modeler_Standard.png)
NAM's unlimited collection of amps and device models.

![Neural Amp Models](https://jam.live/modules/images/320/Neural_Amp_Modeler_Standard.png)
There are countless Neural Amp Modeler (NAM) captures available that model just about any amp or pedal you can imagine. The NAM module lets you load these (.nam) files directly in MIDI Guitar 3.

**Input** - Pre-Gain before the saturation stage.

**Noise Gate** - Threshold to silence the NAM.

**Output** - Post-Gain after the saturation stage.

---

### Cabinet

OverviewDocumentation

![Cabinet](https://jam.live/modules/images/320/Cabinet.png)

...

![Cabinet](https://jam.live/modules/images/320/Delay.png)

---

### Reverb

OverviewDocumentation

![Reverb](https://jam.live/modules/images/320/Reverb.png)

...

![Reverb](https://jam.live/modules/images/320/Reverb.png)

---

### Delay

OverviewDocumentation

![Delay](https://jam.live/modules/images/320/Delay.png)

The Delay module provides basic echo effect, ranging from very short to 100% feedback-driven repeats.

![Delay](https://jam.live/modules/images/320/Delay.png)

* **Feedback** - Control the decay of the delayed signal.
* **Slapback** - Set a very short single-repeat delay that creates a quick echo resembling a sharp, percussive reflection rather than a long echo tail.
* **Delay Time** - Set the time of the delayed signal in milliseconds.
* **Dry/Wet** - Set the mix of original-to-delayed signal here.

---

## Sources

The main source of everything is your guitar, but you can add one of the following Source modules in a [Chain](https://jam.live/modules/modules/#chain) for processing other sources of audio and MIDI.

---

### Audio Device

OverviewDocumentation

![Audio Device](https://jam.live/modules/images/320/Audio_Device.png)

Add an additional audio input stream, for example, to bring in a microphone.

![Audio Device](https://jam.live/modules/images/320/Audio_Device.png)

The **Audio Device** enables the selection of an additional audio input channel (Ch. 1 or Ch. 2) from a selected audio interface. This setting is independent of the master audio I/O settings. The default device is “Main Audio Device,” which is the same as the device selected in MG3’s global audio settings. This is particularly useful for MG3 Hex where the user wishes to bring a D.I. guitar signal into the audio chain to run parallel to a synth chain. However, all other system audio devices are selectable for maximum flexibility.

* **Device:** Click on “Main audio device” to reveal a menu of connected audio input devices.
* **Channel:** Select the desired audio input channel: (Channel 1 or Channel 2)
* **Gain:** Adjust the gain of the incoming signal (-100dB to +12dB)

---

### Backing Tracks

OverviewDocumentation

![Backing Tracks](https://jam.live/modules/images/320/Backing_Track.png)

![Backing Tracks](https://jam.live/modules/images/320/Backing_Track.png)

---
