1 

< 

> M A N U A L Start 

**==> picture [199 x 42] intentionally omitted <==**

2 

< 

> 

## CONTENTS 

**Introduction** .................................................................................................... **3** Getting Started ...............................................................................................3 Load Scaler in your favourite software ..........................................3 Scaler & ScalerControl ......................................................................3 Controlling an external instrument ..................................................3 Scaler ........................................................................................................3 ScalerControl........................................................................................ 4 Triggering Scaler with MIDI ................................................................ 4 Ableton Live ............................................................................................... 4 Triggering another instrument from Scaler (VST) ............. 4 Logic Pro.......................................................................................................5 Triggering another instrument from Scaler (ScalerControl) .....................................................................................5 Resizing the UI .......................................................................................... 6 The Control Bar .............................................................................................. 6 The status bar ........................................................................................... 6 The option buttons ................................................................................. 6 Volume and sound selection ........................................................ 6 Tooltips and embedded guide ..................................................... 6 The Help and Registration buttons ..................................................7 The keyboard ...................................................................................................7 The Browser ..................................................................................................... 8 MIDI Detection mode ............................................................................. 8 Scale Finder ................................................................................................ 8 Chord Sets Selector ............................................................................... 8 Transposition controls ..................................................................... 8 The Scale Explorer ........................................................................................ 8 

The Progression Builder ............................................................................. 8 **Identify the scale of your tune** ............................................................. **9** Start the analysis ........................................................................................... 9 Select a scale................................................................................................... 9 **Find chords that fits your mood** ........................................................ **10** The scale explorer ........................................................................................10 Diatonic Chords view .................................................................................10 Chord Variations view ................................................................................10 Voicings view .................................................................................................10 **Create Chord Progressions** .................................................................... **11** Using the progression builder ................................................................. 11 Octave and inversion controls........................................................... 11 Export to your DAW .............................................................................. 11 Create your own Chord Sets ................................................................... 11 Save a Chord Set ..................................................................................... 11 Import a Chord Set ................................................................................. 11 Export a Chord Set ................................................................................. 11 Delete a Chord Set .................................................................................. 11 **Appendix** ......................................................................................................... **12** Musical notation ............................................................................................12 Chord degree ............................................................................................12 Chord quality ............................................................................................12 **Troubleshooting** .......................................................................................... **13** No MIDI input ............................................................................................13 No sound ....................................................................................................13 License registration issue ...................................................................13 Legal .............................................................................................................14 

3 

< 

> 

## INTRODUCTION 

Scaler is a composition assistant which identifies the scales of your tune to help you build powerful chord progressions. Built to keep you in charge of the creative process, it helps you compose in a faster and more efficient way. Scaler also comes complete with hundreds of chord progressions made by world famous artists across various musical genres. 

Developed by music industry professionals and refined by a team of producers and artists, Scaler defines a new and efficient workflow and helps you leverage the power of music theory in your own production. 

## **GETTING STARTED** 

## **LOAD SCALER IN YOUR FAVOURITE SOFTWARE** 

Scaler is an audio plugin compatible with most Digital Audio Workstations and is available in multiple formats: VST, Audio Units (AU) and AAX. 

To start using Scaler you need to load it on a software instrument track in your favorite Digital Audio Workstation (DAW). Follow the guides below to use Scaler with Ableton Live or Logic Pro or refer to your DAW manual if you need more information on how to load a virtual instrument on a track. 

If your DAW organises your audio plugins by vendor, you will find Scaler under _Plugin Boutique > Scaler_ . 

## Scaler & ScalerControl 

Scaler is packaged with ScalerControl, a version specifically built for DAWs supporting AU MIDI Controlled Effect plugins. Both plugins contains the same detection features and exclusive content. The main difference between the two plugins is how you configure them to trigger external instruments. 

**==> picture [344 x 236] intentionally omitted <==**

If you use a DAW only compatible with AU plugins like Logic Pro for example, you might consider using ScalerControl if you wish to control an external instrument from Scaler. 

## **CONTROLLING AN EXTERNAL INSTRUMENT** 

Because of differences in implementation, VST plugins can have their MIDI output routed to other tracks whereas AU plugins lack this ability. Scaler overcomes this limitation by offering ScalerControl as an AU MIDI effect. 

## Scaler 

When using the VST version of Scaler you can control external instruments by routing the MIDI output of the Scaler track to the input of the track with the instrument you want to control. Refer to the manual of your DAW for more information on how to route MIDI in your software. 

_Continues..._ 

4 

< 

> 

## ScalerControl 

ScalerControl must be loaded as a MIDI effect plugin in a DAW that supports this feature. A MIDI effect does not have the ability to output sound so you need to load another instrument on the same track. 

Refer to the manual of your DAW for more information on how to use MIDI effect plugins. 

## **TRIGGERING SCALER WITH MIDI** 

You can trigger chords and notes generated in Scaler using MIDI. To do so you need to bind the MIDI signal to the area of Scaler you want to control. 

Click on one of the BIND MIDI buttons located in the browser, the scaler explorer or the progression builder to start triggering Scaler with MIDI. 

## **ABLETON LIVE** 

Load Scaler on a MIDI track. Navigate to your plugin list and drag Scaler to the MIDI track of your choice. 

Arm the track Scaler has been loaded on and press a key on the piano roll or your MIDI controller. 

Scaler should identify the name of the note in the status bar: 

**==> picture [337 x 28] intentionally omitted <==**

If the sound output of Scaler is enabled you should hear the note you just played through Scaler’s integrated sound. 

## Triggering another instrument from Scaler (VST) 

Because of limitations in the Audio Unit plugin format, it is not possible to trigger another instrument using the AU version of Scaler. 

After loading Scaler on a MIDI track, load the instrument you wish to control on another track. 

In the In/Out section of the track, select “Scaler” in the MIDI From dropdown and set the Input Channel to “Scaler”. Arm both tracks and start triggering chord from Scaler, the sound should now be rendered using the instrument you’ve been configuring. 

**==> picture [140 x 383] intentionally omitted <==**

_Continues..._ 

5 

< 

> 

## **LOGIC PRO** 

Load Scaler on a MIDI track by selecting it from the instrument dropdown menu. 

Select the track to ensure that the MIDI signal is sent to Scaler and start pressing keys on the piano roll or your MIDI controller. Scaler should identify the name of the notes in the status bar: 

**==> picture [337 x 28] intentionally omitted <==**

Triggering another instrument from Scaler (ScalerControl) Load ScalerControl on a MIDI track as a MIDI FX and on the same track load the instrument you wish to control as a standard MIDI instrument. 

Start triggering notes or chords from Scaler, the sound is now rendered through the instrument you have selected. 

**==> picture [219 x 334] intentionally omitted <==**

6 

> 

## INTERFACE 

< 

There are 5 main areas in Scaler: 

**==> picture [397 x 243] intentionally omitted <==**

## **RESIZING THE UI** 

To resize the UI click on one of the resizing corners located at the top and bottom right of the Scaler window and adjust the window to the desired size. 

## **THE CONTROL BAR** 

The Control Bar located at the top of Scaler’s window displays real time information and allows you to control Scaler settings. 

## **THE STATUS BAR** 

The Note(s) and Chord(s) status bar displays a live feedback of the MIDI input. They display the notes played on the midi channel and/or chords if detected. 

**==> picture [338 x 29] intentionally omitted <==**

You can use the status bars to test your MIDI configuration. try to play a note on your keyboard, the name of the note played should be indicated in the status bar. 

## **THE OPTION BUTTONS** 

Click on the options icons to enable or disable Scaler’s features. 

**==> picture [127 x 32] intentionally omitted <==**

## Volume and Sound Selection 

Click on the sound icon to enable or disable Scaler’s sound output. Click the dropdown menu to select one of Scaler’s built in sounds. 

## Tooltips and Embedded Guide 

Click on the info icon to show or hide tooltips when you hover over an interface element. Click on the help icon to enable or disable the embedded guide. 

To help you quickly discover Scaler’s ability, a tutorial will start when you launch Scaler for the first time. The guide will be disabled once you’ve gone through each of the steps. 

You can use the help icon to disable or restart it at any time. 

_Continues..._ 

7 

> 

## **THE HELP AND REGISTRATION BUTTONS** 

**==> picture [163 x 29] intentionally omitted <==**

## < 

n Click the Help button to access the manual, video guides and tutorials directly from Scaler in your DAW. 

**==> picture [264 x 282] intentionally omitted <==**

n Click on the registration button to register your Scaler license or check how many days you have left on your trial. 

**==> picture [221 x 132] intentionally omitted <==**

## **THE KEYBOARD** 

Scaler’s keyboard has multiple functions. You can use it as an input device, it displays the notes you are playing on your midi device and, if a scale is selected, it shows information about the notes contained in that scale. 

**==> picture [338 x 39] intentionally omitted <==**

When a scale is selected, the keyboard adds a blue marker on the notes contained in the scale. 

The keyboard will overlay in grey any note played on your MIDI device that isn’t part of the selected scale. 

8 

< 

> 

## **THE BROWSER** 

The Browser allows you to navigate between the MIDI Detection mode, the scale finder, and the chord sets navigator. 

**==> picture [337 x 40] intentionally omitted <==**

## **MIDI DETECTION MODE** 

In this mode, Scaler detects the scales compatible with what you are playing. The detection is based on the MIDI signal. You can play something on your keyboard or analyse a piece of MIDI on the Scaler track in your DAW. 

## **SCALE FINDER** 

To quickly find a specific scale, click the “Scales” button in the browser. Every scale supported by Scaler is listed here and you can filter by note or type in order to find the scale you are looking for. 

## **CHORD SETS SELECTOR** 

A chord set can be either a list of chords, a chord progression or a song saved in Scaler. 

Chord sets help you find inspiration, discover chord voicings and understand how progressions and songs works. 

You can choose a chord set by selecting it from one of the 3 menus representing the different types of chord sets: 

n Song sets, organised by genre. 

- n Artists sets, crafted by artists. 

## Transposition controls 

You can easily transpose the selected chord set using the transposition controls located on the left side of the browser. 

**==> picture [98 x 41] intentionally omitted <==**

## **THE SCALE EXPLORER** 

The Scale Explorer let you discover a scale in depth by showing you the notes and chords it contains. You can explore the chords of the scale and discover chord substitutions to easily create variations in your compositions. 

**==> picture [338 x 53] intentionally omitted <==**

Refer to the section _“Find chords that fits your mood”_ for a detailed guide on how to use the Scale Explorer. 

## **THE PROGRESSION BUILDER** 

The Progression Builder gives you the tools to create your own chord progressions and export it to your DAW or save it as a chord set. 

**==> picture [338 x 42] intentionally omitted <==**

- n User sets, created by users. 

Refer to the section _“Create Chord Progressions”_ for a detailed guide on how to use the progression builder. 

9 

< 

> 

## IDENTIFY THE SCALE OF YOUR TUNE 

## **START THE ANALYSIS** 

To begin detection click on the “Detect” button in the browser. 

**==> picture [337 x 46] intentionally omitted <==**

Press “Start”, the button turns red, it is now listening to the MIDI signal. Start playing notes or chords on your MIDI device or hit “Play” in your DAW if you wish to analyse MIDI already on the Scaler track. 

The notes and chords detected are listed in the browser. 

**==> picture [337 x 46] intentionally omitted <==**

Every note played on Scaler’s MIDI channel will be recorded. The notes are evaluated against hundreds of scales and modes to find which ones match your tune. 

You can play back a note or chord from your progression by clicking on it. You can also use the Bind MIDI button and replay your progression using your MIDI controller. 

If you wish to modify the detection, you can remove items by using a _“right click -> remove”_ . 

You can reset the detection by clicking the “Clear” button. 

## **SELECT A SCALE** 

Every time the content of the detection changes, the results list updates automatically and Scaler selects the scale most compatible with the notes or chords played. 

**==> picture [338 x 91] intentionally omitted <==**

More than one scale can apply to a given tune or chord progression. Some scales can work better for specific styles or moods. It is up to you to select the scale you want to use. 

You can see how closely your current analysis matches the notes of the scale in the “Matches” column which represents how many notes and chords of your tune are present in the scale. 

You can find some information about the style and mood of the scale next to its name. 

Press the icon next to a scale name to hear all the notes it contains. 

For scales starting on an accidental note (sharp or flat notes) you can switch to the alternative name by clicking the note in the scale name. This will rename the notes and chords of the scale accordingly. 

10 

< 

> 

## FIND CHORDS THAT FIT YOUR MOOD 

## **THE SCALE EXPLORER** 

When you select a scale, the scale explorer window appears its window can be dismissed by clicking on the close button located at the top right of the window. 

The scale explorer allows you to navigate within the scale to find any chord variation from the most basic to the most complex one. 

Three different views are available: 

## Diatonic Chords view 

This view is the first one you see when you select a scale. It shows the harmonized triads of the scale usually referred to as diatonic chords, they are derived from the notes of the scale. 

**==> picture [337 x 53] intentionally omitted <==**

The chord variation views contains suggestions of substitutions for each degree. You can use substitution to give your chord progression more character. Click on the substitution button on the right hand side of the Chord Variation view to view the suggested substitution for each degree of the scale. 

## Voicings view 

This view allows you to navigate predefined voicings that fit the selected scale. Click on the voicings dropdown menu to select a voicing. 

**==> picture [338 x 52] intentionally omitted <==**

## Chord Variations view 

This more advanced view allows you to navigate through the degrees of the scale. It displays all the chord variations by note. Click the note buttons to display the chords available on each notes of the scale. 

**==> picture [337 x 53] intentionally omitted <==**

11 

< 

> 

## CREATE CHORD PROGRESSIONS 

The real power of Scaler comes from its integrated progression builder. It is designed to help you create chord progressions from scratch or to enrich your existing progression with variations and substitutions. 

**==> picture [337 x 42] intentionally omitted <==**

## **USING THE PROGRESSION BUILDER** 

You can “Drag and Drop” chords to any slot on the progression builder to start creating your progression. 

Press the Play button to hear  your progression. 

Press the Loop button to hear your progression repeated in a loop. Press the Clear button to remove all chords from your progression. You can remove an individual chord from your progression by using _“Right-Click -> Remove”_ on the chord. 

## Octave and inversion controls 

Scaler allows you to finely tune your chord progression by selecting the octave and inversion you want to play each chord at. 

Click on the - or + button to select the octave and inversion you would like to use. 

**==> picture [94 x 39] intentionally omitted <==**

## Export to your DAW 

You can drag the MIDI of your progression 

straight into your DAW in order to hear it on a different track or further refine your progression in a fully featured MIDI editing interface. 

Click and drag the Export MIDI button to a track in you DAW to export your progression. 

**==> picture [105 x 26] intentionally omitted <==**

## **CREATE YOUR OWN CHORD SETS** 

You can create your own chord sets and export them to share your best creations with other users. 

## Save a Chord Set 

When building a progression in the Progression Builder, you can press the “Save as Chord Set” button. You will then be prompted to name the chord set, once you have named your new creation it will be added to the “User Sets” menu. 

## Import a Chord Set 

Press the User Sets menu, select “Import chord set” and then select the file of the chord set you wish to import. You can now select it from the “User Sets” menu. 

**==> picture [105 x 23] intentionally omitted <==**

## Export a Chord Set 

Select the chord set you wish to export from the User Chord Set dropdown menu. On the left side of the screen over the transposition control click the “Export Chord Set” button then select the location where you wish to save your chord set. 

## Delete a Chord Set 

Select the chord set you wish to delete from the User Chord Set dropdown menu. On the left side of the screen over the transposition control click the “Delete” button represented by a trash bin icon. 

**==> picture [35 x 34] intentionally omitted <==**

12 

< 

> 

## APPENDIX 

## **MUSICAL NOTATION** 

Scaler uses a compact notation to quickly identify a chord position and its quality in a given scale. 

## Chord degree 

For each chord, its position in the scale is indicated with roman numerals. 

## Chord quality 

The different qualities of the chords are represented on each chords using one or a combination of the following symbols: 

**==> picture [339 x 23] intentionally omitted <==**

**----- Start of picture text -----**<br>
Chord Quality Symbol<br>**----- End of picture text -----**<br>


|Chord Quality|Symbol|
|---|---|
|Major|UPPERCASE NUMERALS orM_[degree]_|
|Minor|Lowercase numerals orm_[degree]_|
|Diminished|°_[degree]_|
|Augmented|+|
|Suspended|sus_[degree]_|
|Added note|add_[degree]_or space separated_[degree]_|
|Sharpened|#_[degree]_|
|Flattened|b_[degree]_|
|Dominant|_[degree]_|



13 

< 

> 

## TROUBLESHOOTING 

## **NO MIDI INPUT** 

Check that your DAW is configured to send a MIDI signal to the track on which you loaded Scaler. Depending on your software you might need to select or arm the track you wish to send MIDI to. 

## **NO SOUND** 

Check that the sound output in Scaler is enabled. 

Check that the channel on which you loaded Scaler is not muted in your DAW. 

If you are using ScalerControl, ensure that an instrument with a sound output enabled is loaded on the same track as the MIDI effect plugin. 

## **LICENSE REGISTRATION ISSUE** 

If you have any issue trying to register your license file, please contact us at: **support@pluginboutique.com** 

14 

## LEGAL 

## VST PlugIn Technology 

VST PlugIn Technology by Steinberg Media Technologies 

## DAWGDIC 

Copyright © 2009-2012, Susumu Yata All rights reserved. 

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met: 

< 

- Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer. 

- Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution. 

- Neither the name of the University of Tokushima nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission. 

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS “AS IS” AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE. 

