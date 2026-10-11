Source: https://help.uaudio.com/hc/en-us/articles/26817742017684-Multi-Unit-Cascading
Updated: 2025-03-31T22:23:52Z

# Multi-Unit Cascading

# Apollo Expanded Overview

Up to four Apollo Thunderbolt units of any model type (Apollo rack and desktop models) can be connected and used together as a single consolidated multi-unit system via Thunderbolt. When multiple Apollo units are connected via Thunderbolt, all units are controlled within a single Console window, and the I/O complement of all devices is available within the DAW. Operating a multi-unit system is nearly identical to that of a single-unit system for seamless expansion when more I/O is needed.

**Note:** A total of six UAD-2 devices can be used together in a single system.

## Console Integration

When multi-unit cascading, the number of Console inputs is increased to match the increased hardware inputs. All Apollo units share the same monitor, auxiliary, and cue mix buses for integrated mixing convenience.

## Monitor and Expander Units

To facilitate the mix bus integration within Console, one unit must be designated as the monitor (leader) unit. Monitor speakers are attached to the monitor unit only. All other units are expander (follower) units. For details, see Monitor Unit Designation.

**Note:** Headphone and cue outputs can be assigned to any leader or follower unit. However, mirrored cues can be routed to the monitor unit only.

## Hardware Setup

In multi-unit systems, all Apollo devices are interconnected via a single Thunderbolt cable per unit, with a single Thunderbolt connection to the host computer. The host computer port, as well as any Thunderbolt devices on the bus (including Apollo), can be Thunderbolt 1, Thunderbolt 2, or Thunderbolt 3 (Windows systems require built-in Thunderbolt 3 for the host computer connection).

## Constraints

Depending on the specific configuration, certain features and/or I/O streams are reduced when multi-unit cascading. See Multi-Unit Constraints for details.

## Driver I/O

Apollo I/O availability and numbering changes when multi-unit cascading. I/O routes can be virtually remapped via Apollo’s I/O Matrix Panel. For a list of default I/O states, see the Driver I/O Tables.

# Multi-Unit Wiring

**Note:** Visit [help.uaudio.com](https://help.uaudio.com) for complete compatibility information and the latest technical updates.

## Apollo Expanded Wiring Notes

Follow the guidelines below when combining multiple Apollo Thunderbolt units.

### All Multi-Unit Systems

* Up to four Apollo units and six UAD devices total can be combined within the same system.
* A maximum of one desktop interface model (Arrow, Apollo SOLO, Apollo Twin, Apollo Twin MkII, Apollo Twin X, Apollo x4) can be combined within the same system.
* When connecting multiple Thunderbolt Apollo/Arrow/Satellite devices, they must all be daisy-chained to the same Thunderbolt port on the computer.
* Apollo X Series Thunderbolt 3 models can be mixed with prior Apollo Thunderbolt models via compatible Thunderbolt 3 to Thunderbolt 2 adapters.
* A single Thunderbolt cable is required for all Apollo unit interconnections. Connect one cable to the host computer and one cable between each Apollo unit.
* The Thunderbolt protocol is bidirectional. Do not connect more than one Thunderbolt cable between the same two devices.
* All Apollo clocking is automatically managed via Thunderbolt. Do not interconnect any Word Clock, FireWire, ADAT, or MADI ports between any Apollo units.
* Apollo/UAD device ordering and Thunderbolt ports used (such as which port on Apollo racks and Satellites, placements within daisy chain, etc) is not important.
* Monitor speakers (including ALT speakers) and any cue outputs must be connected to the designated monitor unit only.
* All Apollo units must be connected via Thunderbolt. Apollo Thunderbolt models cannot be combined with Apollo models that use FireWire or USB connections.

### Windows Multi-Unit Systems

* A Windows 10 or 11 PC with a Thunderbolt 3 port is required.
* A compatible Thunderbolt 3 to Thunderbolt 2 adapter is required when connecting to older Apollo Thunderbolt models without Thunderbolt 3.
* Connections to Thunderbolt 1 and Thunderbolt 2 computer ports are not supported.

### Mac Multi-Unit Systems

* Thunderbolt 1, Thunderbolt 2, or Thunderbolt 3 ports may be mixed and used for any/all connections.
* Apollo X Series can be connected to Thunderbolt 1 and Thunderbolt 2 Macs via the Apple Thunderbolt 3 to Thunderbolt 2 adapter.

# Multi-Unit Wiring Example

Two typical examples of mixed multi-unit Apollo/UAD systems are illustrated below. See the wiring notes on the previous page for additional details.

![](https://help.uaudio.com/hc/article_attachments/26909105971988)

*Connecting multiple Apollo units via Thunderbolt 3*

![](https://help.uaudio.com/hc/article_attachments/26909118503060)

*Connecting multiple Apollo units via Thunderbolt 2*

# Multi-Unit Operation

## Power On Sequence

Thunderbolt devices may be connected and/or disconnected when the computer and/or devices are powered on (hot plugging). The order in which the Apollo units are connected and/or powered on is not important. Apollo units are automatically detected a few moments after connection.

## Multi-Unit Monitoring

To facilitate the mix bus integration within Console, one unit must be designated as the monitor (leader) unit. All other units are expander (follower) units.

### Monitor Unit Designation

The Apollo unit at the top of the Devices column in the Hardware panel within the Console Settings window is the designated monitor unit. The monitor unit is indicated by a small orange speaker icon and the letter “A” to the left of the unit’s icon.

A different unit is designated as the monitor unit by dragging the unit to the top of the Devices Column, as shown in the screenshots below. The monitor/expander designations can be changed at any time.

**Note:** Designating Apollo Twin as the monitor unit is not a recommended configuration. Instead, designating an Apollo rack model or Apollo x4 as the monitor unit is recommended in order to take advantage of their additional outputs for CUE routing and ALT monitoring.

**Important:** Lower all speaker and headphone volumes before changing the monitor unit designation. Changing the monitor unit designation changes the driver I/O configuration. Quit all audio applications before performing this action. Additionally, wait for this operation to complete before making further adjustments.

![](https://help.uaudio.com/hc/article_attachments/26909118505492)

*Designating the monitor unit in the Hardware panel within Console Settings. In this example, Apollo 8 is the monitor unit (left) before designating Apollo 8p as the monitor unit (right).*

### Multi-Unit Monitor Outputs

When multi-unit cascading, all units share the same monitor mix bus. The monitor speaker system (including ALT monitors, if configured) must be connected to the monitor outputs of the monitor unit only.

Note: After changing the monitor unit designation, the monitor speakers must be physically connected to the new monitor unit to hear the monitor outputs.

#### Monitor Outputs on Expander Units

When multi-unit cascading, the monitor outputs of all expander units are available as additional line outputs via the I/O Matrix panel within the Console Settings window. In this configuration, the monitor outputs of the expander units are not affected by the Monitor Level knob.

### Multi-Unit Headphone Outputs

All headphone outputs for all connected Apollo units (monitor and expander) are available to output the monitor or cue mix buses via the Cue Outputs Popover.

### Multi-Unit Cue Outputs

Cue mix buses can be routed to physical outputs (line, ADAT, etc) on the monitor unit only. However, cues mix buses can be sent to any available headphone output via the Cue Outputs window.

### Multi-Unit Monitor Control

#### Monitor Knobs

The monitor knob on the front panel of expander units (except Apollo desktop models, as below), and its surrounding green LED indicator ring, are disabled. To adjust the monitor output level, the front panel monitor knob on the monitor unit, the desktop remote unit, or the monitor level controls in Console or the Console Recall plug-in must be used.

#### Apollo Desktop Remote

When an Apollo desktop model is connected in a multi-unit system, its monitor knob mirrors that of the monitor unit for volume and mute control. This feature offers convenient desktop control of the monitor and ALT speakers.

#### Apollo Desktop Talkback

When an Apollo desktop model with a Talkback mic is connected in a system with an Apollo X rack model, the Apollo desktop model is the talkback unit. For additional details, see the [Talkback](https://help.uaudio.com/hc/en-us/articles/26489966354836) article.

### Multi-Unit Unison Gain Stage Mode

To control a Unison plug-in with Gain Stage Mode, the hardware controls on the unit containing the preamp channel must be used.

For example, to control a Unison plug-in in an Apollo x8p preamp channel, the Apollo x8p hardware must be used. To control a Unison plug-in in an Apollo Twin preamp channel, the Apollo Twin hardware must be used, and so forth.

## Multi-Unit Clocking

All multi-unit clocking is carried via Thunderbolt. All connected Apollo units always clock (follow) from the monitor (leader) unit, whether set to internal or external clock.

**Important:** Do not interconnect any FireWire, ADAT, Word Clock, or MADI ports between any Apollo units connected via Thunderbolt.

### Internal

When multiple units are connected via Thunderbolt, all system clocking and clock settings are automatically configured by Apollo’s device drivers. The clock setting in Console’s Info Bar (and its mirrored setting in the Hardware panel within the Console Settings window) must remain on INTERNAL unless specifically clocking to an external (non-Apollo) device.

**Note:** When Apollo’s clock source is set to INTERNAL, “EXT” will illuminate on the front panel hardware of the expander units.

### External

When using an external (non-Apollo) clock, connect the external clock to the monitor unit only. All connected Apollo units are automatically configured to use the external clock when Apollo’s Clock is set to EXTERNAL.

**Important:** When synchronizing to an external clock, connect the external clock source to the monitor unit only. The expander units always synchronize to the monitor unit.

## Multi-Unit Flex Routing

When two or more Apollo rack models are connected, Flex Routing can be used within each unit. Up to 16 output routes can be assigned for each connected Apollo rack model.

**Note:** Inputs can only be routed to the outputs of the same unit. It’s not possible to cross-route from one unit to another.

## Distinguishing Multiple Units

### Device Color

Each unit in the Devices list is color coded for enhanced identification. These colors are used in the Meter Bridge and the I/O Matrix Panel when multi-unit cascading to differentiate between devices. The device colors cannot be modified.

### Device Name

When using multiple devices of the same type, it may be helpful to give each device a unique Device Name instead of the default names. The Show Device Names setting is particularly useful with multiple devices.

![](https://help.uaudio.com/hc/article_attachments/26909118512916)

*The Meter Bridge with Apollo x8p and Apollo x4, showing and hiding device colors and names*

### Device Letter

Each unit in the Devices list is designated with a sequential letter. These letters are used in the I/O Matrix Panel when multi-unit cascading to differentiate between Apollo devices. The device letters cannot be modified.

![](https://help.uaudio.com/hc/article_attachments/26909106008852)

*Device letters & colors correspond in the Hardware panel (left) and I/O Matrix panel (right)*

### Talkback

When multiple units with talkback mics are connected, the active talkback unit has an orange mic icon in the Devices Column within Console Settings > Hardware, as shown in these two examples.

![](https://help.uaudio.com/hc/article_attachments/26909106014868)

![](https://help.uaudio.com/hc/article_attachments/26909118570900)

# Console Session Management

## Console 1 to Console 2 / UAD Console Session

If a Console session was created and saved with Console 1 (UAD v8.0.0 and earlier) and the session is subsequently opened with a multi-unit Thunderbolt setup in Console 2 (UAD v8.0.1 or later Thunderbolt software) or UAD Console, the previous Console 1 configuration is retained, with the exceptions noted below.

**Note:** Cue and headphone management settings are now handled differently than Console 1 sessions. These settings are not retained when updating a Console 1 session.

## Single-to-Multi Session

If a Console session was created and saved with a single-unit setup and the session is subsequently opened with a multi-unit setup, the expander unit(s) is automatically added to the session and the number of Console inputs expands accordingly. All settings from the single-unit session are maintained.

## Multi-to-Single Session

If a Console session was created and saved with a multi-unit setup and the session is subsequently opened with a single-unit setup, the expander unit(s) settings are retained in the session for offline configuration. If desired, expander unit(s) can be removed from the session via the Device Options in the Hardware panel within the Console Settings window.

# Multi-Unit Constraints

Certain Apollo features are reduced when multi-unit cascading to maintain integrated mix buses with Realtime UAD Processing capabilities. These constraints are listed below.

* Cue buses can be routed to the line and/or digital outputs of the monitor unit only. This constraint does not apply when routing cues to headphone outputs.
* Flex Routing destinations can only be assigned to outputs on the same unit as the input. It’s not possible to cross-route from one unit to another.
* Apollo uses Thunderbolt for inter-unit clocking when multiple Apollo devices are connected. Because the host computer is the lead Thunderbolt controller, inter-unit clocking, and therefore standalone use, is not possible with Apollo multi-unit cascading.
* When Apollo Twin is connected in a multi-unit system, the Line 3/4 and Headphone outputs on the Twin are not available for signal routing within the DAW. However, Apollo Twin’s Line 3/4 and Headphone outputs can be routed within Console by assigning the output(s) as a destination in the Cue Outputs window.
* Only one desktop interface model (Arrow, Apollo SOLO, Apollo Twin, Apollo Twin MkII, Apollo x4) can be combined in single system.
* Apollo Thunderbolt models cannot be combined with Apollo models that use FireWire or USB connections.
