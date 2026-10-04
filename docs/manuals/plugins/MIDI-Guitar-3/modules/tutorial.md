Source: https://jam.live/modules/tutorial/

This page is under construction!

---

# Getting started with **Jam Origin** software

This tutorial is designed to help new users get started with the **Jam Origin** range of software. We'll begin with [**Guitar Mods**](https://jam.live/products/GM/), as it's very easy to get things up and running in this environment, but everything we present here will also apply directly to [**MIDI Guitar/Bass/Cello 3**](https://jam.live/products/MG3/).

## Prerequisites

To use **Guitar Mods** (and **MIDI Guitar 3**) you'll need the following:

* an electric guitar;
* a USB audio interface;
* a computer (Windows/MacOS) or an iPad.

## Installation and setup

1. Download the **Guitar Mods** installer from the link in [downloads](https://jam.live/downloads/).
2. Install the application.
3. Launch the **Guitar Mods** app. By default, the app will start up with the preset named **"Introduction"** loaded.
4. Click the ⚙️ icon at the top left corner to enter *Preferences*.
5. Select *Audio Devices*.
6. Select either "Same audio device for input and output" or "Dedicate an audio interface exclusively for input" depending on your I/O configuration.
7. Select your audio interface/s in the input and output device lists.
8. Click the *Apply* button twice to confirm your settings and return to the main **Guitar Mods** GUI.
9. Play some notes! You should hear audio from the Cello Mod and the **Guitar Mods** input module should be firing off little colourful laser beams as it processes the notes you play.

Note

**Guitar Mods** can also be loaded as a module inside [**MIDI Guitar/Bass/Cello 3**](https://jam.live/products/MG3/).

## Working with **Modules**

The **"Introduction"** patch consists of a single chain that contains five different **modules**. Let's take a close look at some aspects of the modules.

## Transposer module

Hit the **Transpose** switch/button at the bottom of the **Transposer** module to drop the pitch by one octave. That's a more natural register for a realistic cello-like tone, but you can move the output to a register of your liking by using the **Octaves** dial.

## The Cello Mod's **Morph** parameter

Now, let's look at the **Cello Mod** module, specifically its **Morph** knob.

Adjusting the **Morph** knob changes the audio balance of the guitar versus the cello. The default is 50% guitar/50% cello — a hybrid instrument sound — but be sure to explore the full range from 0-100.

## Controlling parameters in real-time

Many parameters in **Guitar Mods** can be controlled by an external source. Of course, you can easily adjust knobs using a mouse or a touch screen, but when your hands are busy on your instrument, it's handy to be able to make your moves with a MIDI controller, such as an expression pedal.

## Connecting MIDI devices

Take a look in the lower left corner of **Guitar Mods**. This area is called the **MIDI Patchbay**. You can select the connected USB MIDI devices that you want to receive MIDI messages from here. By default, the **MIDI Patchbay** shows **"No MIDI Controller"**. Click here to select a specific device or **"Any MIDI Controller"**, if you want access to messages from all detected MIDI devices.

Let's say you have an expression pedal attached that transmits MIDI CC#01, usually associated with modulation. "CC" stands for continuous controller, which is a common type of MIDI message. The pedal will generate values from 0-127 according to the position of the treadle between the minimum (heel down) and maximum (toe down) positions.

If CC#01 is present in the **MIDI Patchbay** (it is, by default), you will see the dial light up when you move the pedal, indicating the values it is transmitting.

Next, click on a dial in the **MIDI Patchbay** and drag to a parameter you wish to control, e.g. the **Morph** knob. A virtual cable appears, and the connected pedal will now raise or lower this parameter's value!

But even if you do not have any MIDI devices connected, you can still use your computer's numeric keys (1-9) in place of an expression pedal to help get the idea of how these controls work. The numeric keys correspond to MIDI CCs (i.e. 1 = CC#01, 2 = CC#02, etc.) and will alternately send 0 (minimum) and 127 (maximum) values with each tap of a numeric key.

## Modulators

Rather than having a sound that's 50% guitar-like and 50% cello-like, what if we want the guitar notes to morph from 100% guitar into 100% bowed cello strings?

We can't do this with a pedal, not only because that would require a lot of footwork, but also because if we fire six notes, each of these notes can transition at a different time...

Generally, what we really want is a robotic hand to automatically turn the knobs for us, in musically interesting ways, while we play the strings... Imagine the robot hand turns the knobs very precisely, for every note in every chord, to follow aspects of the guitar sound, and the result will be a cello that follows the guitar, in musically interesting ways to help you maintain the "connection" with the new instrument.

This is called *polyphonic modulation* and it's at the core of this software.

So we want to change the modulation source. Click the **CC** below your cable and change its source to **Brightness**. This is still wired to the **Morph** knob so, the "celloness" is now no longer controlled by the pedal, but rather by the **Brightness** of your guitar notes.

Oops, that moves in the opposite direction to the way that we want it to go! It starts with a cello and morphs into a guitar. That's because the **Brightness** modulator measures the brightness of each note and guitar plucks tend to decay in brightness over time, but we want something that rises over time to turn that **Morph** knob up — not down.

In the **MIDI Patchbay**, click **Brightness** to adjust the modulator. Click **Invert** and drag around the curve to scale it to some desired response. You could bend the curve so that it's much steeper.

Your guitar will now morph each note you play on the guitar into a cello. The **Brightness** modulation can be used to create very complex evolving sounds.

## Chains

The **"Introduction"** patch in **Guitar Mods** uses a single *Chain**. Audio flows through a* *Chain* *from top to bottom, and then from left to right:* *Chain* *->* *Mixer* *->* *Master Chain*\*.

... to be continued ...
