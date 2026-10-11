Source: https://help.uaudio.com/hc/en-us/articles/25347160337556-UAD-Console-Overview
Updated: 2026-03-03T18:00:05Z

# UAD Console Overview

UAD Console is the companion software application for Apollo audio interface hardware. UAD Console's analog-style workflow is designed to provide quick access to the most commonly needed features in a familiar, easy-to-use application.

UAD Console's function is to control up to four Apollo hardware units or up to three Volt 876 hardware units, or Apollo x16D and Apollo | e devices, and their digital mixing and low-latency monitoring capabilities. You can configure Realtime UAD Processing and Unison with UAD plug-ins for Apollo and Apollo x16D in UAD Console or in LUNA.

**Important Fundamental Concept:** The primary function of UAD Console is to control low-latency hardware input monitoring, Unison plug-ins (Apollo devices and Apollo e1x devices when connected to Apollo x16D), and Realtime UAD Processing on Apollo hardware when using third-party DAWs such as Logic Pro, Live, and Pro Tools. UAD Console replaces the software input monitoring feature of the DAW's mixer. UAD Console or LUNA Recording System must be used to take advantage of these Apollo features.

UAD Console remotely controls the digital mixing and signal processing functions that are performed within the Apollo hardware. Although UAD Console runs on the host computer, the computer's CPU is not performing these audio functions. All audio mixing and signal processing occurs on the DSP inside Apollo.

**Note:** Apollo interfaces use UAD DSP and memory resources for the internal DSP mixer. Therefore, the UAD Meters will show DSP and memory usage when Apollo is connected, even if UAD Console and/or Apollo plug-ins are not currently loaded.

![console-icon.png](https://help.uaudio.com/hc/article_attachments/25403934845460)

![console-callouts.png](https://help.uaudio.com/hc/article_attachments/46835318690580)

*UAD Console's application icon and main window*

# How to get UAD Console

1. In UA Connect, click the Apollo & UAD-2 tab.
2. Click the Download button next to UAD Console. If UAD Console is already installed, you can click the Update button (if an update is available).
3. After the software is downloaded, click Install to complete the installation.

# UAD Console Functions

UAD Console enables the following functionality when used with Apollo:

* **Hardware control.** All of Apollo's front or top panel hardware controls (except headphone volume) can be controlled using UAD Console, facilitating easy hardware manipulation even if Apollo is installed in a location out of reach of the computer operator.
* **Low-latency monitoring.** Using UAD Console eliminates the latency associated with DAW I/O buffering that makes monitoring problematic for the performer. By removing the DAW's software input monitoring feature from the monitoring signal flow altogether, the need to adjust I/O buffer sizes and latency is no longer an issue.
* **Apollo Realtime Plug-Ins.** Realtime UAD Processing can be used with all UAD Console inputs and/or auxiliary returns (within available DSP resources), for the ultimate latency-free sonic experience while monitoring and/or tracking live performances. All processed (or unprocessed) inputs and stereo mix buses, including the monitor and auxiliary buses, can be optionally routed into the DAW for recording.
* **Unison.** Apollo's Unison™ technology gives you the tone of the world's most sought-after tube and solid state mic preamps, guitar amps, and pedals — including their all-important impedance, gain stage "sweet spots," and component-level circuit behaviors. Unison also features bidirectional plug-in adjustments using Apollo's hardware controls.
* **Send/Return Auxiliary buses.** UAD Console has two pre/post stereo aux buses, with independent send levels per input, for grouped signal processing (conserving UAD DSP resources) or routing to the DAW.
* **Flexible cue monitor mixing.** Up to four independent stereo cue mix buses are available (two with Apollo Twin) with per-input sends to ensure individual performers are able to hear "more me" if desired. Cue mixes can be easily routed to any available headphone or line outputs.
* **Flexible signal routing.** Using UAD Console, any hardware input can be routed to available hardware outputs (rackmount models only). Additionally, cue mix buses can be optionally mirrored to available hardware outputs.
* **Session management.** UAD Console configurations can be saved and loaded to/from disk as presets, for convenient and unlimited session management. Sessions can also be stored/recalled within the DAW project using the UAD Console Recall plug-in.

## Global Functions

Parameters within UAD Console Settings are available for configuring various global behaviors:

* **Hardware.** Global interface settings such as sample rate, clock source, reference levels, and digital output mirroring.
* **Software.** Global software settings for UAD Console such as metering and plug-in window behaviors.
* **I/O Matrix (Thunderbolt only).** This powerful feature enables customized signal routing and I/O naming at the Core Audio (Mac) and ASIO (Windows) driver level. Custom driver routing tables can be saved and recalled as presets.

# When To Use UAD Console

The UAD Console application can be used without a DAW, simultaneously in conjunction with a DAW, or not at all. These scenarios are covered in greater detail in the [Apollo Software Manuals](https://help.uaudio.com/hc/en-us/articles/13445960631700).

## UAD Console without DAW

UAD Console can be used by itself without the use of a DAW or any other audio software for monitoring live inputs. Using UAD Console without a DAW provides access to all Apollo functionality and simplifies the use of Apollo's digital mixing, monitoring, and realtime processing features when a DAW's recording and playback features are not needed.

## UAD Console with DAW

UAD Console is used at the same time as a DAW when low-latency monitoring and/or recording of Apollo's inputs with (or without) realtime processing is desired. In this scenario, UAD Console is used as a front end to control input monitoring when recording, when the DAW's software input monitoring feature is disabled. This workflow completely eliminates the I/O buffering latencies associated with using software monitoring via the DAW.

**Important:** To eliminate doubled signals, software monitoring in the DAW must be disabled when UAD Console is used for input monitoring. Conversely, UAD Console inputs must be muted if the DAW's software monitoring feature is enabled.

UAD plug-ins can be used within UAD Console and a DAW simultaneously. In this scenario, Apollo's DSP resources are shared between the two applications. Realtime UAD Processing is available via UAD Console, and buffered (non-realtime) UAD processing is available via VST, AAX 64, or Audio Units plug-ins within the DAW. See the [Apollo Software Manuals](https://help.uaudio.com/hc/en-us/articles/13445960631700) for more details about this scenario.

**Tip:** You can open or quit UAD Console at any time, whether or not a DAW is already running. UAD Console's settings and UAD plug-ins remain active after the application is quit.

# Interactions Between UAD Console and Apollo

UAD Console's settings mirror the Apollo hardware. Changes made to one are also made on the other, and vice versa. If changes are made to UAD Console when Apollo is not connected, and Apollo is subsequently connected, the UAD Console settings are sent to the hardware.

**Important:** If UAD Console is launched after changes are made to Apollo using the front panel hardware controls, the current UAD Console settings will overwrite the changes made using the hardware controls.

# Installing UAD Console

By default, UAD Console is not installed. To install UAD Console, click Download in the Apollo & UAD-2 tab within the UA Connect app.

# Accessing UAD Console

Any of the methods below can be used to open the UAD Console application.

#### Mac

* Open UAD Console from the Applications folder
* Click the UAD Console application icon in the Dock
* Click the UA diamond logo in the Menu Bar (upper right of screen) then choose Console from the drop menu

![console-menu.png](https://help.uaudio.com/hc/article_attachments/46835304888212)

*Accessing UAD Console from the macOS Menu Bar*

#### Windows

* Access the program from the Windows Start Menu
* Right-click the UA diamond logo in the Windows System Tray (in taskbar at lower right of screen), then choose Console from the contextual menu

![access-console-windows.png](https://help.uaudio.com/hc/article_attachments/28840829889940)

*Accessing UAD Console from the Windows System Tray*

# Quitting UAD Console

UAD Console can be closed using any of these methods:

#### Mac:

* Select Quit from the macOS Application Menu (upper left of screen) when UAD Console is the foreground application
* Use the standard macOS keyboard shortcut (Command+Q)
* Close the UAD Console window by clicking the "X" Close button in the Window Title Bar

#### Windows:

* Close the UAD Console window by clicking the "X" Close button in the Window Title Bar

# Resizing the UAD Console Window

![console-window-resize.png](https://help.uaudio.com/hc/article_attachments/25403899380884)

The size of UAD Console's high-resolution window can be dynamically adjusted in realtime to fit any workspace. To adjust the window size, click+drag any corner or any edge of the window.

## UAD Console Width

Reducing the UAD Console window width reduces the number of visible input channels. Use the Bank Bar in the Meter Bridge to view input channels that may be currently out of view.

v260122
