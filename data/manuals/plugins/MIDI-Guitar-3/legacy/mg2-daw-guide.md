Source: https://www.jamorigin.com/docs/daw/

# MIDI Guitar & MIDI Bass

#### FOR WINDOWS & MAC

MIDI Guitar turns any guitar into a true polyphonic MIDI Guitar, with latency and accuracy comparable to expensive and inconvenient hardware MIDI-Guitar solutions. This is achieved by connecting your guitar to your computer and letting MIDI Guitar use its polyphonic (multi-note) pitch detection algorithm to convert your guitars signal to MIDI that can be used to play a soft synth or virtual instrument or as a plugin in your Digital Audio Workstation

MIDI Guitar is available as both a VST/Audio Unit plugin, but also a standalone application that can transfer MIDI to your Digital Audio Workstation using Virtual MIDI on Mac OS X and a virtual MIDI cable driver on Windows.

The free trial of MIDI Guitar allows you to evaluate the recognition technology without any interruptions when using the Test Piano and with interruptions when hosting plugins or using MIDI output.

[How do I install MIDI Guitar?](https://www.jamorigin.com/docs/daw/#install)  
[How do I buy and activate the license?](https://www.jamorigin.com/docs/daw/#license)  
[How to use in your DAW](https://www.jamorigin.com/docs/daw/#plugin)

### Installing the plugins

After downloading the latest MIDI Guitar installers from [jamorigin.com/download](https://www.jamorigin.com/download), you can install the standalone app and plugins. This is done by an installer on windows and manually on macOS.  
(for MIDI Bass the steps are the same, but read MIDI Bass instead of MIDI Guitar)

#### Windows users:

Running the installer will ask you where to install the plugins. You need to put them in the plugin folder where your DAW expects to find them. If you don’t know where your plugins folder is, use the most commonly used location, given below:

The default plugin folder for most **32bit** hosts is **c:/program files (x86)/Steinberg/VstPlugins/**

The default plugin folder for most **64bit** hosts  is **c:/program files/Steinberg/VstPlugins/**

However, some DAWs use another VSTs folder. Sonar and Mixcraft for example use c:/Program files/Cakewalk/VstPlugins for 64-bit plugins and c:/Program files (x86)/Cakewalk/VstPlugins for 32-bit plugins.

Most DAWs allow you to set your VST or plugin folder. You may have to add the VST folder above to the list in which your DAW search for plugins inside your DAWs preferences window.

#### Mac users:

Open the DMG installer image find the two plugins: MIDI Guitar 2.vst and MIDI Guitar 2.component.  
*NOTE: AU (Audio Unit) plugins have a .component extension.*

Copy **MIDIGuitar2 .vst** file to your VST plugins folder **/Library/Audio/Plug-Ins/VST/**

Copy **MIDIGuitar2 .component** file to your AudioUnit plugins folder:**/Library/Audio/Plug-Ins/Components/**

If you cant find these folders, open Finder and hold “cmd” and “shift” keys and press “G”. Now copy the above path into the dialog that pops up.

In order for your DAW to discover the new MIDI Guitar plugins you sometimes need to make it rescan your plugins folder for plugins or restart the Mac.

### How to buy and apply license

* Our shop is at <http://jamorigin.com/products/midi-guitar/buy>
* MIDI Bass is only available bundled with MIDI Guitar 2. The MIDI Guitar 2 license allways includes MIDI Bass for free.
* *At checkout, please make sure the VAT-id field is empty. Only if you own a VAT-id, this field should be used*

After a succesfull  purchase, a download link for your license will be send to your emailaddress.

Those license links expire within a week

**Please keep a copy of your downloaded license somewhere safe.**

**A simple way to do this, is to send it as an email attachment to yourself.**

**Installing the license for MIDI Guitar:**Open the standalone MIDI Guitar app, play with any other patch than “test piano”, when interruption comes, choose “apply license”, point to the downloaded .license file in your downloads folder

**Installing the license for MIDI Bass:**

Open the standalone MIDI Bass app, play with any other patch than “rhodes”, when interruption comes, choose “apply license”, point to the downloaded .license file in your downloads folder

### How to use in your DAW

After copying the VST/AU to your plugin folders, MIDI Guitar should work with almost any DAW.

* In general: our plugins need a short buffersetting. 256 is for the most systems a good place to start.
* VST is the preferred plugin format: unless noted otherwise allways choose the VST format instead of the AU version!  
  (Logic X, Garageband and Mainstage only work with AU )
* Allthough our plugins can load plugins itself, this does not provide for recording of the midi: therefore the midi is send to another DAW instrument track. Some DAWs also reportedly are unstable when our plugin loads bigger synths itself.

Since DAWs are usually complex applications with lots of options, we try to keep a list of tutorials and videos for setting up a DAW project with MIDI Guitar. Please locate your DAW below.  
[What if my DAW is not (yet) here in the list?](https://www.jamorigin.com/docs/daw/#otherdaw)

### Getting started with MIDI Guitar in your DAW

Ableton Live

## Ableton Live 9

*IMPORTANT: if you installed the VST, but it doesn’t show up in Live, try the following:*  
*1) goto Live / Preferences / Plugins*  
*2) Hit “rescan” with the “alt” key pressed. This will force Live to evaluate all plugins.*

Here is another video that shows the basics of using MIDI Guitar as a plugin in Ableton Live 9, but is also slightly misleading. Please see the comment below.

In this video, the MIDI Guitar 2 AudioUnit is loaded and it outputs MIDI with the V-MIDI option, which works, but cause a latency overhead. Please don’t use the AudioUnit with Ableton. Instead, load the MIDI Guitar 2 VST plugin and use the direct midi output (which is enabled by default). In your MIDI/instrument track, go to “MIDI From” and select the audio track on which the MIDI Guitar VST is loaded. Now, when recording, you get MIDI into the piano roll of that MIDI track.

## Ableton Live 8

1. In Preferences / Audio, check that Audio Input Device and Audio Output Device are correct.
2. In Preferences / Audio, check that In/Out Sample Rate is 44100
3. In Preferences / Audio, check that Buffer Size is 256 or 128 samples
4. In Preferences / File Folder, set “Use VST Plug-in System Folders” to Yes on Mac OS X and make sure the MIDI Guitar VST is found on Windows.
5. Press Tab key to access Arrangement View
6. Check menu “options”. Latency compensation should be OFF!
7. Click “I-O” button to show In/Out section
8. Click “M” button to show Mixer section
9. Make sure you have an Audio Track named “1 Audio” and a MIDI track named “2 MIDI”
10. Add MIDI Guitar VST to “1 Audio” track
11. Click “In” button on the “1 Audio track” to verify that MIDI Guitar works with your audio interface.
12. Select “1 Audio” as “Input Type” for “2 MIDI” track to redirect MIDI from MIDI Guitar to your MIDI track.
13. Arm recording for “2 MIDI” track to record MIDI from MIDI Guitar.
14. Click Record and then Play to start recording MIDI from MIDI Guitar.

[![](https://www.jamorigin.com/jo/images/daw-setup/midi-out-ableton-small.png)](https://www.jamorigin.com/jo/images/daw-setup/midi-out-ableton.png)

Acoustica MIxcraft (not compatible)

Mixcraft (windows only app) does not support standard midirouting and therefore does not work with our plugin out of the box. Workarounds are theoretically possible but not for the faint of heart!

Apple GarageBand

Video tutorial for GarageBand:

Apple Logic Pro X

## 

## Apple Logic Pro X

Logic will use MIDI Guitar’s virtual midi output to get MIDI from your guitar and its simple to setup.

First, make sure you apply Logic’s [low latency mode](https://support.apple.com/en-us/HT207527#:~:text=Low%20Latency%20Mode%20bypasses%20plug,Audio%20preferences%20of%20Logic%20Pro). Also see [Apple’s general advice for low latency processing](https://support.apple.com/guide/logicpro/work-with-plug-in-latencies-lgcpe11997ba/10.6.2/mac/10.15.7).

**Recommended setup:**

The best way to use MG with Logic is using the MG AudioUnit (customers only):

1. Make sure you place the MIDI Guitar 2.component in your plugins folder (typically thats /Library/audio/plugins/Components/) as described above.
2. Restart your computer so that Logic Pro will scan the new files you have installed.
3. Next, open Logic Pro on your Mac and create two tracks…  The first track should be an “audio track” for the audio from your guitar. On the channel fader of this “first” track, activate Midi Guitar 2  in the audio FX slot. Make sure you don’t use any other effects before MIDI Guitar (as MIDI Guitar needs a completely dry input).
4. Now, create a second track. This new “second” track should be an “instrument track” for the “midi information” that will automatically come from the Midi Guitar 2 plugin on the first guitar track you created…  These two tracks will work together!  
   On the second track you created,  do not call up Midi Guitar 2 in the channel fader slots.  
   When you create an “instrument track” in Logic Pro, it automatically installs an instrument in a midi instrument slot…  That is the instrument that will be activated and played by the midi information recorded on the track.. you can of course change it to any instrument.

The following video shows how to use MG in Logic Pro X

**This video shows how to use both internal sounds and midi in a simple studio setup:**

**Using only the MIDI Guitar standalone:**

* Instead of using the MIDI Guitar Audio Unit, you can simply run the MIDI Guitar standalone and select the MIDI Output Route: “MIDI Guitar Virtual MIDI Out”. Now “MIDI Guitar” appears in Logic as a MIDI input without any additional work. That’s it. It’s just there. This method will add a bit of latency compared to recommended approach described above.

Apple Mainstage 3

Ardour / Linux

Although it would be great to have a LinuxVST version of this plugin, it seems to run OK in Linux using WINE.

The following notes explain how to get it running in AVLinux 21  (<http://www.bandshed.net/avlinux>) using the Ardour DAW ([https://ardour.org](https://ardour.org/)).  Other Linux distributions should also work, but setting up WINE may differ. Sadly, the plugin is too expensive for me to justify buying it (I’m just a hobbyist), but these notes may help other users running Linux who do want to buy it.

After installing the download with WINE, the MIDI Guitar VST is in ~/.wine/drive\_c/Program Files/Steinberg/VSTPlugins/.  
Copy that MIDIGuitar2-64bit.dll to /usr/local/lib/vst (the suggested folder for Windows VST plugins in AVLinux).

Convert the .dll to .so using Yabridge: AVL → Settings → AVL-MXE WINE-Staging Setup → double-click on YADbridge → double-click on Synchronize VST Plugins.

Rescan the plugins: in Ardour: Window → Plugin Manager → Rescan All.

Jam Origin says (<https://www.jamorigin.com/docs/daw>): ” Intuitively most people think of MIDI Guitar as a virtual instrument (VSTi), but try to think of it as an effect first: it has an audio input (your guitar sound) and audio output (the synth or virtual instrument you load into MIDI Guitar).”  
So what we need to do is run MIDI Guitar in an audio track, and pipe the MIDI output from that into another MIDI track.

Add a new audio track in Ardour.  Name it (for instance) MGaudio and select Flexible-I/O as the Pin Mode – according to Robin Gareus, and Ardour developer, (<https://discourse.ardour.org/t/routing-midi-from-vst-on-audio-track-to-midi-track/103989>): “This allows plugins to change the available track output ports [so loading] your plugin should automatically add a MIDI output.”

View → Show Editor Mixer to bring up the mixer strip for each track.

Right-click the mixer → New Plugin → Plugin Selector… → search for “guitar” → double-click “MIDI Guitar 2” in the list → Insert Plugin(s).

The MIDI GUITAR interface will open.  If using the paid version, you can (presumably) close it, but if you are using the demo version, you need to keep it open, because every 2 minutes or so it pops up a “Trial Interruption” screen, and unless you press Continue on this, the plugin will not work.

Ensure that MIDI Guitar is listed above Fader in the Mixer – if not drag it up.

If you are using a USB input box for the guitar, it’s easiest to set it as the input device in QJackCtl Setup.  This means that it will already be the default input to the MGaudio track.

Add a new MIDI track in Ardour.  Name it (for instance) MGmidi and select Strict-I/O as the Pin Mode.

Connect the output of MGaudio to the input of MGmidi:  
Right-click the MGaudio track → Outputs → Ardour Tracks → click the cell under 1 opposite MGmidi in so that a green dot appears.  
Right-click the MGmidi track → Inputs → Ardour Tracks → click the cell above 1 opposite MGaudio out so that a green dot appears.

Arm BOTH tracks.  If the MGmidi track is not armed, it will not record the MIDI output from the MGaudio track.  Also, ensure that the MGaudio track is not muted, otherwise it will produce no MIDI output to be piped into the MGmidi track.

Press Continue on the Trial Interruption screen if it has come up.  
Arm the session, and press the play button.

Play the guitar.  You will see  content appearing on both tracks: the piano default from MIDI Guitar on the MGaudio track, and the MIDI output on the MGmidi track.

After playing the guitar, mute the MGaudio track so you can hear the MGmidi content alone (but remember to unmute it if recording additional material).  
Adjust the plugin on the MGmidi track to give the sound you want.

AVID ProTools (only via extra bridging plugin and midi loopback)

## AVID ProTools

**Since ProTools does not support VST or AU plugins you need to use MIDI Guitar standalone and a virtual midi driver.** The idea is that you connect MIDI Guitar to ProTools though a virtual cable (in much the same way you would connect a physical midi keyboard controller though its software driver). Its fairly simple:

1. If you are using Windows you need a virtual midi loop driver, such as [loopMidi](http://www.tobias-erichsen.de/software/loopmidi.html) or [loopBe1](http://www.nerds.de/en/loopbe1.html) (both freeware). Mac users can skip this step as Apple operating systems already include a virtual midi standard.

2. Make sure MIDI Guitar works in standalone mode, i.e. you can play the Test Piano.

3. In MIDI Guitar select the virtual midi loop driver as MIDI Output (bottom left). On Windows that is a loopMidi/loopBe1 device. On Mac its the “MIDI Guitar Virtual MIDI Out”.

4. In ProTools,  enable the same device as input.  (Setup > MIDI >Input Devices > Check the box next to the MIDI Guitar loop output). Mac users just select the built in “MIDI Guitar Virtual MIDI Out”.

5. Thats it. Your guitar is now connected to ProTools, just like a midi keyboard.

Note that virtual midi is not ideal in terms of latency, although usually the impact is unnoticeable. We will consider an AAX plugin in the future.

Note for Windows users: Since most ASIO drivers only works with one application at a time you might also need a second interface.

### Using BlueCat VST wrapper ( this works only on macOS)

As an alternative to the above, you can use the BlueCat VST wrapper.  
**You have to load the MIDI Guitar AU audio unit: that plugin will create a virtual midi port.**

The following is based upon a user report:

1. Use Blue Cat audio MB& in broadband mode with MIDI Guitar AU as the only plugin inserted.

2. Put any VI next in the chain.

3. My guitar is plugged into a DI into an input channel on my interface.

4. Go to setup/Midi input devices and make sure to select “Midi Guitar #1 out”. This seems like you may have to do this each time you open a session ( will need to check further)

5. Set your track input to “midi guitar #1 out”

![](https://www.jamorigin.com/wp-content/uploads/2018/05/BlueCat-888x1030.png)

Bitwig

Our plugins work in Bitwig, and the MIDI is routable from our plugin to other tracks.  
there is a quirk however with getting Bitwig to be able to record the MIDI onto a pianoroll.  
We contacted Bitwig but still havent got an answer yet

Cakewalk by Bandlab

## Cakewalk Sonar

Starting with Sonar X3 and any newer versions works great with MIDI Guitar:

1. Copy the MIDI Guitar plug-in to the VST folder
2. Launch SONAR. If the plug-in is no listed in the Audio FX list, run the VST scanner.
3. Create or open a project.
4. Add new audio track, set the input to a mono source (or use an existing mono track). Insert MIDI Guitar into FX bin or ProChannel. To record MIDI data from MIDI Guitar MIDI, using the VST2 drop down in the plug-in header click “Enable MIDI Output” otherwise load a synth plug-in directly into the instrument output of MIDI Guitar, enable input echo on and skip step 5.
5. Add a new synh or change the input to an existing synth to MIDI Guitar. Make sure both the MIDI Guitar audio track and the synth (Instrument or MIDI) track have input echo enabled.

### Old versions of Sonar:

In older versions of Sonar (version X1, X2) there are issues with MIDI Guitar. The Sonar addressed these issues in version X3, but some have found a workaround for old versions Sonar that apparently works in X1 and X2.

( Quoted from MoreK at KVR Forum: RE Sonar X2 & MIDI Guitar )

What I missed was the MIDI Guitar pop-up menu in the Synth rack. Clicking the keyboard icon with right mouse button gives a menu with no “Enable MIDI Output” option. You have to click grey area of the synth and you’ll get a different menu with the MIDI output option.

So, to summarize the whole setup:

1. Copy VST plugin to your VST folder
2. Launch Sonar. It should automatically recognize the new plug-in and create needed registry entries (ie you should see the plug-in as an effect in Audio FX menu). If not, use Plug-in Manager to scan new plug-ins.
3. Use Cakewalk Plug-in Manager, find MIDI Guitar in Effects section and open “Plug-in Properties”. Enable “Configure as synth” option.
4. Close Sonar and use Regedit to change generateEvents key from “0” to “1” in HKEY\_CURRENT\_USERSoftwareCakewalk Music SoftwareSONAR ProducerCakewalk VST X64Inventory -> MIDI Guitar
5. Launch Sonar. Add new audio track. Insert MIDI Guitar (now found in Soft Synths menu) to FX bin.
6. Go to Synth rack view. Right click grey area of the MIDI Guitar synth block and click “Enable MIDI Output”.

That’s it. Add your favourite synth to a new track and route MIDI input from MIDI Guitar, which should be visible in MIDI input menu.

Thanks again, works like a charm now.

Cockos Reaper

## Cockos Reaper

Reaper 5.2

Reaper 4.2

Add MIDI Guitar as a FX plugin and click on the record field and select “Record: Output” and then “Record: MIDI Ouput”

[![](https://www.jamorigin.com/jo/images/daw-setup/midi-out-reaper-small.png)](https://www.jamorigin.com/jo/images/daw-setup/midi-out-reaper.png)

Steinberg Cubase

## Steinberg Cubase 11

Please see [this page](https://www.jamorigin.com/docs/cubase-11/).

## Steinberg Cubase 9 & 10

Windows users:  
Please **deactivate/uncheck the “ASIO guard“** in Cubase audio settings!!  
For further helpseeCubase 8 video

## Steinberg Cubase 8

### Cubase 7

Add an audio track and an instrument/MIDI track. Add MIDI Guitar as an Effect plugin to the Audio track and select MIDI Guitar as input on the Instrument/MIDI track

[![](https://www.jamorigin.com/jo/images/daw-setup/midi-out-cubase-small.png)](https://www.jamorigin.com/jo/images/daw-setup/midi-out-cubase.png)

FL Studio 20 (unconfirmed performance)

## FL Studio 20

.. is available for both windows and macos now!  
The internal routing allows for connecting the loaded MIDI Guitar plugin to purchased FL synths and none-FL synths.  
Note 1: MIDI Guitar is not made with variable buffersize in mind. The display of buffersize and cpu load are erratic.  
Note 2: as for now, we dont really know how well it works latency and stabilitywise. It may be so that the standalone/virtual midi is more stable, especially on macos.

## 

## FL Studio (before  version 20)

You have two options:

1. You can use the MIDI Guitar VST plugin inside FL Studio. This is optimal in terms of latency but unfortunately FL Studio does not currently support routing midi from VST plugins to its piano roll. Thus, you will be limited to hosting synths and instruments inside MIDI Guitars internal plugin host.  
**If using this option you need to make sure FL process audio in fixed size buffers.** Please see the FL docs: <http://www.image-line.com/support/FLHelp/html/plugins/wrapper_2_processing.htm>

2. The other option is to use a virtual midi loop and the MIDI Guitar standalone. This is detailed below.

Install [loopMIDI](http://www.tobias-erichsen.de/software/loopmidi.html). Start loopMIDI and add a MIDI port.

![](https://www.jamorigin.com/jo/images/daw-setup/loopMidi.png)

In FL Studio MIDI Settings, Enable the loopMIDI Input MIDI device and set the loopMIDI Output MIDI device port number to 0

![](https://www.jamorigin.com/jo/images/daw-setup/fl-studio-midi-settings.png)

In the Mixer add MIDI Guitar plugin to an available channel other than Master. In MIDI Guitar plugin settings set MIDI Output port to 0. In the step sequencer select and enable a synth such a DX10.

[![](https://www.jamorigin.com/jo/images/daw-setup/midi-out-fl-studio-small.png)](https://www.jamorigin.com/jo/images/daw-setup/midi-out-fl-studio.png)

MOTU Digital Performer

## MOTU Digital Performer 8 & 9

1. In Preferences / Audio Plugins, make sure MIDI Guitar VST is enabled.
2. In Setup / Configure Audio System / Configure Hardware Driver, check that Master Device is correct.
3. In Setup / Configure Audio System / Configure Hardware Driver, check that Sample Rate is 44100
4. In Setup / Configure Audio System / Configure Hardware Driver, check that Buffer Size is 256 or 128
5. In Setup / Configure Audio System / Input Monitoring Mode, make sure that “Monitor record-enabled tracks through effects” is selected.
6. Select Sequence tab
7. Add a Audio Track
8. Select Audio Input for the Audio Track.
9. Enable Input Monitor and Record for the audio track.
10. Select Mixing Board tab
11. Add MIDI Guitar VST to audio track.  
    In MIDI Guitar, set Patch to “Test Piano” and strum your guitar to test MIDI Guitar.
12. Select Sequence tab.
13. Add a MIDI track
14. Arm MIDI track for recording
15. Click record.

Magix Samplitude

## Magix Samplitude

Very nice video introduction to MIDI Guitar using Samplitude by Kraznet.

Propellerhead Reason

## See [this forum thread](https://jamosapien.com/t/reason-11-2-with-midi-out/1540/9).

## Propellerhead Reason 11.2

## Propellerhead Reason 10

From Reason 9.5 on, VST plugins are supported, but the midi output from a VST is still not routed in Reason 10.

## Propellerhead Reason 9.5

From Reason 9.5 on, VST plugins are supported, but the midi output from a VST is not routed yet.  
We’ve notified Propellerhead of this, hopefully they add the functionality soon. You still need the use the standalone via virtual midi route now.  
https://www.propellerheads.se/reason-95

## Propellerhead Reason below 9.5

Since Reason does not support VST or AU plugins you need to use MIDI Guitar standalone and a virtual midi driver. Its fairly simple:

1. First make sure MIDI Guitar works in standalone mode. If you are using Windows you need to install a virtual midi loop driver (such as loopMidi or loopBe1, both freeware). Select the virtual midi driver as output route in MIDI Guitar. Mac users simply select the MIDI output route: “MIDI Guitar Virtual MIDI Out”.

2. In Reason you must register the virtual MIDI driver as a MIDI Control Keyboard/surface. See the image below.

Note that virtual midi is not ideal in terms of latency. We do not know yet if there is has any real impact or not on latency. We will consider Reason Rack Extension in the future.

[![](https://www.jamorigin.com/jo/images/daw-setup/midi-out-reason.jpeg)](https://www.jamorigin.com/jo/images/daw-setup/midi-out-reason.jpeg)

PreSonus Studio One

### Studio One Professional ***IMPORTANT:*** ***turn down dropout protection under Options->Audio Setup->DropoutProtection.*** ***It cannot be set to maximum. Any other setting should be okay.***

### Studio One Prime

This free version of Studio One does not support VST plugins.

You can still use MIDI Guitar with it, using a virtual midi loop connection. On Mac its built in. On Windows you need loopMidi (freeware). Then select the virtual device as output route in MG and input in Sutiod One Prime.

### Studio One Artist

This version supports VSTs with an extra add one that can be purchased from Presonus.

You can still use MIDI Guitar with it, using a virtual midi loop connection. On Mac its built in. On Windows you need loopMidi (freeware). Then select the virtual device as output route in MG and input in Sutiod One Prime.

### Older versions of Studio One

Makes sure your samplerate is set to 44.1Khz and buffersize 256 or 128 samples.

Add track 1 (mono audio). Arm it for recording so you have your guitar here. Add the MIDI Guitar VST to this track. Adjust sensitivity.

Add track 2 (instrument track). Change instrument input to “MIDI Guitar”, “CH1”. Arm it for recording so you have your guitar MIDI here.

Record audio and midi by pressing record.

[![](https://www.jamorigin.com/jo/images/daw-setup/midi-out-studio-one-small.png)](https://www.jamorigin.com/jo/images/daw-setup/midi-out-studio-one.png)

Sensomusic Usine

## Sensomusic Usine

Video introduction to MIDI Guitar using Usine by Nay-Seven.

Traktion 7

## Using another DAW?

The very first thing to try is to use it in your DAW just like you would use any other audio effect (say a reverb or compressor). Intuitively most people think of MIDI Guitar as a virtual instrument (VSTi), but try to think of it as an effect first: It has an audio input (your guitar sound) and audio output (the synth or virtual instrument you load into MIDI Guitar). Used this way as an audio effect it should work with any DAW that supports VST or AudioUnit effects.

After using it as an effect you will probably start to wonder how to get the MIDI output from MIDI guitar into your DAW and into its piano roll. Most DAWs have ways to route the midi output from MIDI Guitar to other places and if not you can always fall back to using the standalone version with a virtual MIDI loop. On Mac OS X, virtual MIDI is built in. On Windows you need to install a virtual midi driver, of which several options are freely available. Please see the “Connect To DAW” option in the MIDI Output section of MIDI Guitar for instructions.

## Compatibility with popular DAWs

# 

Please find guides for each DAW above.

| Name |  | VST | Audio Unit | Plugin Host | MIDI Out | Windows | Mac OS X |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Ableton **Live** |  | Yes | Yes | Yes | Yes | Yes | Yes |
| Apple **GarageBand** |  | N/A | Yes | Yes | Yes | N/A | Yes |
| Apple **Logic** |  | N/A | Yes | Yes | Yes/V-MIDI | N/A | Yes |
| AVID **Pro Tools** |  | N/A | N/A | N/A | Standalone | Yes | Yes |
| Cakewalk **Sonar** |  | Yes | Yes | Yes | Yes | Yes | Yes |
| Cockos **Reaper** |  | Yes | Yes | Yes | Yes | Yes | Yes |
| ImageLine **FL Studio** |  | Yes | N/A | Yes | Standalone | Yes | N/A |
| Magix **Samplitude** |  | Yes | Yes | Yes | Yes | Yes | Yes |
| MOTU **Digital Performer** |  | Yes | Yes | Yes | Yes | Yes | Yes |
| Propellerhead **Reason** |  | N/A | N/A | N/A | Standalone | Yes | Yes |
| PreSonus **Studio One** |  | Yes | Yes | Yes | Yes | Yes | Yes |
| Sensomusic **Usine** |  | Yes | Yes | Yes | Yes | Yes | Yes |
| Steinberg **Cubase** |  | Yes | ? | Yes | Yes | Yes | Yes |

\* On Windows it requires a virtual midi driver such as the free loopMIDI

## Recommended DAW settings

Its recommended you run your DAW at 44100Hz using 128 or 256 samples pr audio buffer. Its important to understand that running at too high samplerates will cause latency and unresponsive tracking.

MIDI Guitar should work fine at high samplerates as well (88.2K, 96K, 192K, etc..), but it will cause additional CPU load and have no quality benefits as for MG concerned.

## Processing old recordings

MIDI Guitar will generally process anyting on a track in a DAW, and this can be used to process old recordings in you DAW, in the same was as it can be used on live tracks, as long as those tracks are dry guitar recordings.

This means you can convert dry guitar audio recordings to MIDI, and have endless creative use cases. For inspiration please see this video:
