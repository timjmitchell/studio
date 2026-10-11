Source: https://help.uaudio.com/hc/en-us/articles/25350369296660-UAD-Plug-In-Inserts
Updated: 2025-06-16T17:00:01Z

# UAD Plug-In Inserts

The Inserts section of each UAD Console input strip is where UAD-2 plug-ins are selected and used for Realtime UAD Processing. Four standard (non-Unison) insert slots are available per UAD Console channel strip; therefore up to four UAD plug-ins can be serially chained (stacked) per input within the constraints of available DSP resources.

Apollo’s analog preamp inputs have a special dedicated Unison insert in addition to four standard inserts. Line inputs, virtual inputs, and both auxiliary returns also have four standard inserts each. Therefore, up to five UAD plug-ins can be serially chained (stacked) per preamp channel within the constraints of available DSP resources.

**Note:** Only UAD-2 DSP plug-ins can be loaded in UAD Console (not native UADx or 3rd-party plug-ins). However, tracks with any plug-ins used within a DAW can be routed into UAD Console via Virtual I/O.

For more information, see [Using UAD Plug-Ins](https://help.uaudio.com/hc/en-us/articles/5085501350932).

# Inserts Signal Flow

Audio signals in a UAD Console channel flow through the inserts serially from top to bottom, beginning with the Unison insert (if used), then proceeding through the following inserts. Therefore, if more than one plug-in is inserted in a channel, the location of a plug-in within the inserts can change the sound of the channel.

**Tip:** Plug-ins can be reordered by dragging them to change the serial processing order.

![](https://help.uaudio.com/hc/article_attachments/25350369248404)

*Channel Inserts in Large view*

![](https://help.uaudio.com/hc/article_attachments/25350369250068)

*Channel Inserts in Small view*

# Unison Inserts

![input-preamp-unison-highlighted.png](https://help.uaudio.com/hc/article_attachments/31945305828244)

*Click area outlined in red to insert a Unison plug-in*

Apollo’s Unison technology is activated when a Unison-enabled UAD plug-in is loaded in the dedicated Unison insert located above the preamp options (as shown above, outlined in red).

**Note:** Audio on preamp channels is processed by the Unison insert (if active) before the channel inserts.

The Unison insert is only available on Apollo preamp channels. However, Unison inserts are operated exactly the same way as standard channel inserts. For complete Unison details, see [Unison](https://help.uaudio.com/hc/en-us/articles/26485044036756).

# Insert State Indicators

![](https://help.uaudio.com/hc/article_attachments/25350376073108)

*Insert states*

The state of loaded plug-ins within each insert can be determined by the background color of the slot:

**Active (light gray) –** The plug-in is active and processing audio. The UA 1176 Rev A insert in the illustration indicates this state.

**Disabled (dark gray) –** The plug-in has been disabled via the power switch in the header of the plug-in edit window (or via the disable function in the insert options menu). The API 550A insert in the illustration indicates this state.

**Offline (red) –** The plug-in is disabled because there are not enough UAD resources, it is unlicensed and the demo has expired, and/or the UAD authorization needs updating. The C-Suite C-Max insert in the illustration indicates this state.

**Empty (+) –** The insert is not populated with a plug-in. Click the space to open the Insert Browser.

**Yellow outline  –** The plug-in editor is open. The UA 1176 Rev A insert in the illustration indicates this state.

# Insert Hover Options

![plug-in-hover-buttons.png](https://help.uaudio.com/hc/article_attachments/26378128490004)

Three commonly-used plug-in functions become available when the mouse cursor is hovered over any insert containing a plug-in. The function icons appear on top of the plug-in name in Small view, or at the bottom of the plug-in in Large View. To perform the function, click the associated hover switch.

**Assign –** Opens the plug-in browser so you can choose a plug-in. Choosing a different plug-in replaces the current plug-in.

**Open editor –** Opens the plug-in editor window, so you can edit the plug-in parameters.

**Bypass plug-in –** Toggles the plug-in bypass state (yellow when active).

**Show insert options menu –** Right-click to show a menu with insert options.

# Insert Options Menu

![insert-options-menu.png](https://help.uaudio.com/hc/article_attachments/36203799990932)

*Insert Options menu*

To display the Insert Options menu, right-click / control+click any insert.

The options available in the menu vary depending on the state of the insert (e.g., empty or loaded) and contents of the copy/paste clipboard. Each insert option is described below.

The menu has two sections under blue headings: Plug-in options that apply to the individual insert, and Channel options that apply to all channel inserts in the strip.

## Plug-In Options

**Copy –** Copies the plug-in that is in the insert so it can be pasted into another insert. This option does not appear if a plug-in is not loaded in the slot.

**Paste –** Pastes a plug-in that was previously copied into the insert. This option does not appear if a plug-in was not previously copied.

**Note:** All copy/paste functions also copy/paste the current settings of the plug-in.

**Assign... –** Opens the Plug-In Browser where you can select an insert plug-in. If the insert already contains a plug-in, the loaded plug-in is replaced with the newly-assigned plug-in.

**Presets... –** Opens the plug-in's preset browser.

**Remove –** Unloads the plug-in from the insert.

**Disable –** Disables plug-in processing and conserves UAD resources, but the plug-in remains in the insert.

## Channel Options

**Presets... –** Opens the channel preset browser.

**Remove All –** Unloads all plug-ins from all channel inserts in the channel.

**Disable All –** Disables plug-in processing and conserves UAD resources for all plug-ins in the channel inserts, but the plug-ins remain in the inserts.

**Enable All –** Resumes plug-in processing for all disabled plug-ins in the channel inserts.

# Insert Effects Settings

The UAD REC/MON settings are used to specify whether or not Realtime UAD Processing in UAD Console is recorded (printed) in the DAW or just monitored without being recorded

**UAD REC –** UAD Console inputs are recorded with processing (wet). The UAD-processed signals are heard and recorded.

**UAD MON –** UAD Console inputs are recorded without processing (dry). The UAD-processed signals are heard, but not recorded.

**Important:** UAD plug-in processing in UAD Console’s Unison insert and auxiliary inserts are always recorded in the DAW, regardless of the current Insert Effects setting (Unison and aux insert processing is always recorded).

## Individual Channel Insert Effects Switch

This switch determines whether or not Realtime UAD Processing occurring within an individual UAD Console input is routed to the associated DAW input. For additional details, see [Global Insert Effects Switch](https://help.uaudio.com/hc/en-us/articles/25351900668564#h_01HTREAF9F6TPDVKJF7BXC53RK).

**Tip:** Insert Effects can be switched for all channels simultaneously with the Global Insert Effects switch.

![](https://help.uaudio.com/hc/article_attachments/25350376083476)

*Individual Channel Insert Effects Switch (below Inserts)*

![](https://help.uaudio.com/hc/article_attachments/25350376086548)

*Individual Channel Insert Effects Switch (above Inserts)*

Two channel insert effects switches are available in Console’s inputs. Both switches are visible when the Inserts row is open. The smaller indicator switch is visible when the Inserts row is closed. Click either switch to change the REC/MON state.

## Global UAD REC (record with effects)

![](https://help.uaudio.com/hc/article_attachments/25350376090004)

When Insert Effects are record-enabled (UAD REC lit), Apollo’s channel input signals are processed by UAD Console’s standard UAD plug-in inserts before being routed into the DAW.

In this mode, the post-insert (wet) state of all UAD Console inputs with Realtime UAD Processing is routed to the DAW inputs.

**Tip:** Use this setting to record all channels “wet” with Realtime UAD Processing.

## Global UAD MON (monitor with effects)

![](https://help.uaudio.com/hc/article_attachments/25350376093972)

When Insert Effects is not record-enabled (UAD MON lit), Apollo’s channel input signals are routed directly into the DAW before being processed by UAD Console’s standard UAD plug-in inserts.

In this mode, the pre-insert (dry) state of all UAD Console inputs is routed to the DAW inputs, even if Realtime UAD Processing is occurring in the monitor mix.

**Tip:** Use this setting to record “dry” when Realtime UAD Processing is active.

## UAD REC and UAD MON (mixed state)

![](https://help.uaudio.com/hc/article_attachments/25350376097940)

When both switches are lit YELLOW, some individual channels are recorded with insert processing and some are recorded dry, as determined by the individual Channel Insert Effects switches. You can click one of the global insert effects switches to override the individual channel insert effects settings.
