Source: https://help.uaudio.com/hc/en-us/articles/26489269396116-Console-Recall-Plug-In
Updated: 2025-03-31T22:23:52Z

# Console Recall Plug-In

# Console Recall Overview

Console Recall is a DAW plug-in supplied in VST, AAX 64, and Audio Units formats. It is inserted and used within host DAWs as with any other plug-in.

**Note:** The Console Recall plug-in is not required to use the Apollo interface hardware, the UAD Console application, or a DAW.

The primary function of the Console Recall plug-in is to store the current UAD Console configuration within the DAW via the SYNC (synchronize) switch in the plug-in. It can also be used to view and adjust Apollo's monitor output level, mono, and mute states without having to leave the DAW.

## SYNC

The SYNC switch is not available in UAD Console. When a DAW project containing the Console Recall plug-in is saved and the SYNC switch is enabled in the plug-in, the current state of the UAD Console application is stored within the Console Recall plug-in.

When the DAW project file is subsequently reloaded, UAD Console is automatically restored to the previous settings state, regardless of any changes to UAD Console or Apollo that were made in the interim.

Since plug-in settings are saved within DAW project files, using SYNC enables UAD Console's current state to be stored within the DAW project file without saving or loading UAD Console sessions presets via the UAD Console Sessions functions.

This feature ensures the DAW project will sound exactly the same when reloaded at a later date, even if UAD Console contains customized settings that might affect the audio, such as send mixes, signal routings, and/or Realtime UAD Processing.

![](https://help.uaudio.com/hc/article_attachments/26489288839572)

Console Recall plug-in window

# Console Recall Controls

Most Console Recall plug-in controls are duplicates of those found in UAD Console. The exceptions are the SYNC switch, and the CONSOLE switch, which opens the UAD Console application.

![](https://help.uaudio.com/hc/article_attachments/26489269382164)

Console Recall plug-in controls

## Monitor Controls

The same control descriptions in UAD Console apply to the Console Recall plug-in controls. Refer to the [Monitor Column](https://help.uaudio.com/hc/en-us/articles/25351900668564) article for descriptions of the duplicated controls:

* Monitor Meters
* Monitor Level
* Monitor Output Options

## Console Switch

UAD Console can be opened by clicking the CONSOLE switch. Note that UAD Console does not need to be open when using the DAW with the Console Recall plug-in; UAD Console settings are always captured by the Console Recall plug-in as long as the SYNC switch is engaged.

# How To Use Console Recall

To use Console Recall, simply place one instance of the Console Recall plug-in into any insert slot in the DAW project. The plug-in is installed in the same location as all other UAD-2 plug-ins, but the name of the plug-in is "Console Recall" (without the UAD prefix).

**Important:** To avoid unpredictable results, do not insert more than one occurrence of the Console Recall plug-in within any single DAW project.

Because the plug-in does not process audio in any way, the insert location isn't critical. Although it can be placed on any audio track, virtual instrument track, aux bus, output, etc, placing it on the master output is recommended for consistency since projects usually contain an output channel.

Upon instantiation of the plug-in, the Monitor Level, Mono, and Mute controls mirror the equivalent controls in UAD Console. Enabling SYNC causes the current UAD Console settings to be stored within the DAW project.

## Enabling SYNC

When Console Recall is first loaded, the SYNC switch is disabled (gray). To activate SYNC, click the switch so it is engaged (lit).

![](https://help.uaudio.com/hc/article_attachments/26489288843028)

SYNC switch when disabled (top) and enabled (bottom)

Enabling SYNC does not change the UAD Console settings; SYNC doesn't do anything until the DAW project file is saved and subsequently reloaded.

**Important:** SYNC saves the UAD Console settings within the DAW file, not the UAD Console application. Therefore the DAW project file must be saved to disk to retain the UAD Console settings in the project.

## Effect on Session Name in UAD Console

When a DAW project is loaded that contains the Console Recall plug-in with SYNC enabled, the Session Name in UAD Console displays "- Sync Session -" and the display is dimmed.

![](https://help.uaudio.com/hc/article_attachments/26489288846100)

UAD Console session name when SYNC is enabled in DAW

## Loading Synchronized DAW Projects

If SYNC was active when a DAW project file containing Console Recall was saved, then loading that DAW project will load the UAD Console settings saved in the plug-in, and the settings that were active before the DAW project was loaded are overwritten.

**Important:** The UAD Console settings that were active before the DAW project was loaded can be easily recovered if desired using the [Cached Sessions feature](https://help.uaudio.com/hc/en-us/articles/25357506048020#h_01HTS1V6Z8XNABJYHC988WGTZD) in the Sessions Menu within UAD Console.

If SYNC was inactive when a DAW project file containing Console Recall was saved, then loading that project will not change the UAD Console settings that were active before the DAW project was loaded.

## Session State Parameter

The Console Recall plug-in has a parameter called "Session State" that is exposed for DAW automation but is not in the plug-in interface. Session State ensures all changes to UAD Console settings and the DAW session are captured by the Console Recall plug-in. If something related to Session State appears in the DAW, it's best to just ignore it.

**Important:** To ensure proper functionality when SYNC is enabled in Console Recall, do not create or edit DAW automation with the Session State parameter.
