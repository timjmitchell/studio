Source: https://help.uaudio.com/hc/en-us/articles/28349656196500-Apollo-x16D-Networked-Audio
Updated: 2026-03-03T18:00:02Z

# Apollo x16D Networked Audio

## In this article

* [Apollo x16D Connections](#h_01J2MBZ6WV9CDXPK70RDNHH4Z0)
* [Setting up x16D with UAD Console and Dante Controller software](#h_01J2MBZ6WVW4HH70AZ1MQA5DA5)
* [Apollo x16D Clocking](#h_01J2MBZ6WV4GK9R25R2WNYXN4C)
* [Apollo x16D Use Cases](#h_01J2MBZ6WVPVWK8N3HSR3BTBMN)
* [Dante-Capable Ethernet Switches](#h_01J2MBZ6WV29KT9C6RG4C2MNXC)
* [Switched Mode and Redundant Mode with Apollo x16D](#h_01J2MBZ6WVHJ2N2CNBPTNV3V5G)
* [Clocking Use Case Tables](#h_01J2MBZ6WV3VN4D132YQYMJ2YY)
* [Dante Device Lock](#h_01J2MBZ6WVM11JB5Y0ZJ9JK1EA)
* [Monitor Modes & Channel Assignments](#h_01J2MBZ6WVWVJDW8NBCZCXBGAB)
* [Apollo x16D Driver Channels](#01J954GWBCAWY4P33R8GKTCHN3)

Apollo x16D brings all the power of Realtime UAD Processing into your Dante® network, allowing you to process audio with UAD-2 plug-ins in real time across up to four networked x16Ds. An Apollo x16D has the following features:

* 16x16 channels of Dante/AES67 digital audio
* 2x2 AES/EBU digital I/O
* 2 analog monitor outputs
* UAD HEXA DSP processing
* Surround monitoring capability for formats up to 9.1.6
* Up to 4 stereo cue buses
* Built-in Talkback mic

## About Apollo x16D Documentation

This article is one component of complete Apollo x16D documentation. The related components are linked below:

* [Apollo x16D Hardware Manual](https://help.uaudio.com/hc/en-us/articles/13446310879892-Apollo-Hardware-Manuals)
* [Apollo Thunderbolt Software Manual](https://help.uaudio.com/hc/en-us/articles/13445960631700-Apollo-Software-Manuals)
* [UAD Console Manual](https://help.uaudio.com/hc/en-us/sections/25052396869908-UAD-Console-Manual)
* [UAD Plug-Ins Manual](https://help.uaudio.com/hc/en-us/articles/13443257772436-UAD-Plug-Ins-Manual)
* [UAD System Manual](https://help.uaudio.com/hc/en-us/articles/13444697234196-UAD-System-Manual)

## Networked Audio System Requirements

Please see [this article](https://help.uaudio.com/hc/en-us/articles/360015483551-Apollo-X-Series-System-Requirements) for Apollo x16D technical requirements.

* Apollo x16D Thunderbolt Audio Interface with Dante
* Dante Controller software ([download the latest version](https://my.audinate.com/support/downloads/dante-controller))
* Dante-compatible hardware

## Download Dante Controller

To use Dante digital audio features, you must [download and install Dante Controller software from Audinate](https://my.audinate.com/support/downloads/dante-controller).

## Dante Firmware Updates

Dante firmware in your Apollo x16D may be updated through the Apollo firmware update process, when you install a newer version of UAD software. Follow the on-screen instructions if you are prompted to update the firmware.

### Firmware Update Notes

* A network connection is required to update firmware. You may be prompted to select a network interface if your network connection to the x16D is not your default network connection.
* Dante firmware updates are not managed through the Dante updater. All Apollo firmware updates are exclusively performed through the UAD Meter firmware update process.
* Any firmware update will cause an interruption in audio processing.

---

# Apollo x16D Connections

Apollo x16D requires two connections to your computer:

* **A Thunderbolt connection.** Your Apollo x16D(s) must be connected via Thunderbolt to your computer. Apollo devices, including Apollo x16Ds, can be daisy-chained to the host computer in any order.  
  **Note:** The Apollo daisy chain must be connected to only one Thunderbolt port on the host computer.
* **An Ethernet network connection.** Your Apollo x16D must be connected from one of the network ports via an Ethernet cable to your computer, either directly, or through a [Dante-capable Ethernet switch](#h_01J2MBZ6WV29KT9C6RG4C2MNXC). You might need an Ethernet adapter for the host computer connection.

See [Apollo x16D Use Cases](#h_01J2MBZ6WVPVWK8N3HSR3BTBMN) for more information on these network connections.

Apollo x16D can be operated in Switched mode or Redundant mode. This operating mode is set in the Dante Controller software. Use of these modes changes the operation of the Ethernet ports. Consider Redundant Mode when you require real-time failover capabilities. See [Switched Mode and Redundant Mode with Apollo x16D](#h_01J2MBZ6WVHJ2N2CNBPTNV3V5G) for more information.

---

# Setting up x16D with UAD Console and Dante Controller software

## Configure your Apollo x16D in UAD Console

1. Launch UAD Console.
2. If an Apollo x16D is your Monitor system, set the x16D Clock Source to DANTE.
3. If the Apollo is not your Monitor system, set the clock source according to your requirements. See [Clocking Use Case Tables](#h_01J2MBZ6WV3VN4D132YQYMJ2YY) for more details.

## Configure your system in Dante Controller software

As a brief overview, a Dante system comprises transmitters and receivers. Transmitters transmit audio to the Dante network, and Receivers receive audio from the Dante network. A transmitted audio stream can be received by multiple device channels. When a transmitter and receiver are paired, that pairing is called a *subscription*. Multiple receivers can subscribe to a transmitted audio stream.

For more information, see Audinate's [Routing Media](https://dev.audinate.com/GA/dante-controller/userguide/webhelp/content/routing_media.htm) documentation.

1. Launch Dante Controller software.
2. If you are prompted to select a network interface, select the primary network interface (and secondary interface, if applicable) with which your computer communicates with the Dante network.
3. The Dante Controller device view opens. If it is not visible, click the Routing tab.
4. Expand Receivers and Transmitters to see the devices from which the x16D(s) can receive audio (transmitters) and to which the x16D(s) can send audio (receivers).
5. To configure audio subscriptions between receivers and transmitters, click in the boxes in the rows (receivers) and columns (transmitters) in Routing view. A green checkbox appears when a subscription is successful.
6. To remove an audio subscription, click a checkmarked subscription.

![](https://help.uaudio.com/hc/article_attachments/28421205049492)

*Routing example: Dante 1–2 channels on the unit "x16D–293bea" receive audio streams from the device "AllenHth-8aaed7" and CH1–2 on "AVIOAO2-54f642" receives audio streams from Dante 1–2 outputs of "x16D–293bea"*

**Note:** You may need to adjust the sample rate for other devices on your network. The Apollo x16D sample rate is set in UAD Console, but sample rates for other devices may require manual intervention. You can adjust a device's sample rate in the Device View screen on the Device Config tab.

## Set Dante network latency

You can set Dante network latency, which defines the allowable network latency.

In Device View, choose the latency setting in the Device Latency section. For most networks the default setting of 1.0 msec is adequate.

**Note:** Changing device latency will cause audio to be interrupted.

![](https://help.uaudio.com/hc/article_attachments/28421209824660)

To view latency statistics for a device, click the Latency tab in the Device Config view. For more information on how to interpret the latency data, see [Latency Tab](https://dev.audinate.com/GA/dante-controller/userguide/webhelp/content/latency_tab.htm) in the Dante Controller user guide.

---

# Apollo x16D Clocking

The x16D provides a flexible clocking mechanism that allows for clocking to the internal device clock, the network-distributed Dante clock, or external clock sources such as Word Clock or AES/EBU. It is important to understand the requirements of the various clock sources and how they interact with your Apollo system to avoid audio issues and ensure system stability.

## Apollo x16D Clock Settings

The Apollo x16D defaults to:

* Clock source = DANTE
* Sample rate = 48 kHz

In general, having the clock source set to DANTE on an x16D monitor unit is the most flexible option, as the device can adapt to become a clock leader or clock follower without audio issues.

The UA Mixer Engine, which runs in the background and is controlled by UAD Console, automatically manages the sample rate of multiple connected Apollos so they always match each other, and manages other settings such as "Preferred Leader" and "Enable Sync to External", to guarantee proper clock synchronization.

**Important:** When an Apollo x16D is locked with Dante Device Lock, it will not respond to automatic sample rate management or configuration changes. If you intend to use Dante Device Lock, it is recommended to first connect your system as desired and configure the system sample rate and clock settings, then apply Dante Device lock.

---

# Apollo x16D Use Cases

The following examples present use cases that leverage the Apollo x16D for existing Dante systems.

## Adding Apollo x16D to your live sound rig or live console

You can add an Apollo x16D to your live sound mixing console for effects processing.

In this scenario it is expected that the Dante Clock Leader of the system is the Dante-enabled FOH (front of house) console. In this scenario, the FOH Console is using a built-in clock not furnished by external Word Clock or AES/EBU.

### Connection Diagram

Connect Apollo x16Ds to the mixing console according to the diagram below.

![](https://help.uaudio.com/hc/article_attachments/28421209829012)

*Single Apollo x16D connected to one Dante device*

![](https://help.uaudio.com/hc/article_attachments/28421209833620)

*Multiple Apollo x16Ds connected to one Dante device*

* If only one Apollo x16D and one Dante-equipped mixing console are connected, you can connect the Apollo x16D directly to the mixing console using the available primary network port, or optionally connect both the x16D's primary network port and mixing console to a [Dante-capable Ethernet switch](#h_01J2MBZ6WV29KT9C6RG4C2MNXC).
* If multiple Dante devices are connected, connect all Dante devices including the Apollos and the mixing console to a [Dante-capable Ethernet switch](#h_01J2MBZ6WV29KT9C6RG4C2MNXC). Note that you can connect each Apollo to another device in Switched mode, via the network ports.
* In either scenario above, the host computer running UAD Console requires a network connection to the primary network of the x16D.

Use the following settings.

#### In UAD Console

* Set the Apollo x16D(s) clock source to DANTE.

#### In Dante Controller

1. For the FOH mixing console, enable the "Preferred Leader" setting.
2. For the connected Apollo x16D monitor unit, disable the "Preferred Leader" setting.
3. Observe that the connected Apollo x16D(s) are assigned as Dante clock followers.

## Using Apollo x16Ds in a recording studio

In a scenario where one or more Apollo x16D devices are connected to multiple devices and/or in multiple rooms, connect all Dante devices including the Apollos to a [Dante-capable Ethernet switch](#h_01J2MBZ6WV29KT9C6RG4C2MNXC).

![](https://help.uaudio.com/hc/article_attachments/28421205082772)

### Recommended settings

Use the following settings:

1. Set the x16D(s) clock source to INTERNAL, DANTE, or AES/EBU
2. Enable "Preferred Leader" on the monitor unit x16D (this is automatically deployed when the clock source is Internal, but optional when the clock source is DANTE or AES/EBU).
3. Disable "Preferred Leader" on all other devices on the Dante network.

---

Apollo x16D Network Settings

![](https://help.uaudio.com/hc/article_attachments/28421209850772)

The Apollo x16D includes network settings in the UAD Console Settings window, on the Network tab.

For the most part, these settings are informational.

## Network Interface

This displays the network interface which your computer uses to connect to the Dante network.

## Dante Network Settings

The Dante Network Settings row shows information about the network settings for all connected Apollo x16D devices. These network settings are also displayed in Dante Controller. All fields in this display are read-only, except Reset.

## Reset

If you need to reset your network settings for an Apollo x16D, click Reset. When you tap the Reset button, a warning appears that audio will be interrupted. All network settings are reset after you click OK.

**Tip:** For example, if the IP address of your x16D has been set to a static IP address that you don't know, you can reset the network settings.

![](https://help.uaudio.com/hc/article_attachments/28421205103508)

---

# Dante-Capable Ethernet Switches

Dante devices can work over a wide variety of commonly available Ethernet switches. Gigabit switches are recommended.

Your switch must meet the following requirements:

* Gigabit ports for inter-switch connections
* Quality of Service (QoS) with 4 queues
* Diffserv (DSCP) QoS, with strict priority
* A managed switch is also recommended, to provide detailed information about the operation of each network link: port speed, error counters, bandwidth used, etc.

For more information, see the [Audinate Networks and Switches FAQ](https://my.audinate.com/networks-and-switches).

---

# Switched Mode and Redundant Mode with Apollo x16D

Apollo x16D can be operated in Switched mode or Redundant mode. Use of these modes changes the operation of the Ethernet ports. Consider Redundant Mode when you require real-time failover capabilities. Redundant or Switched mode is set in Dante Controller software's Device View > Network Config, in the Dante Redundancy section.

## x16D Switched Mode

In (default) Switched mode, the secondary Ethernet port will behave as a standard switch port, allowing daisy-chaining through the device. In this network topology, the x16D only requires a connection from the network device to one of the x16D Ethernet ports. You can connect a network port to your computer and the other port to a Dante device, or connect your computer and the x16D to an Ethernet switch. If the second network port is connected, it must be connected to another IP-addressable device and not the same network switch as the first Ethernet port. Do not connect both x16D network ports to the same network switch or device.

![](https://help.uaudio.com/hc/article_attachments/28421205110804)

## x16D Redundant Mode

In Redundant Mode, the device duplicates Dante media traffic to both Ethernet ports, allowing the implementation of a redundant network via the secondary port. In this mode, Apollo x16D's Ethernet ports function as connections to separate, isolated networks. In a redundant configuration, the primary Ethernet port is connected to the primary Dante network, and the secondary Ethernet port is connected to the secondary (redundant) Dante network. This scenario provides automated failover protection. The Dante configuration is mirrored on both Ethernet ports so that if one fails, the other will immediately resume audio transmission tasks.

![](https://help.uaudio.com/hc/article_attachments/28421209871508)

### Redundancy notes

* Dante redundancy requires that both the primary and secondary interfaces on any redundant device are connected using the same link speed. For example, if the primary interface is connected to a 1 Gbps switch port, the secondary interface must also be connected to a 1 Gbps switch port.
* Dante devices that do not support redundancy must be connected to the primary network only. See the example above.

## Using multiple Apollo x16Ds on the same network with different UAD Consoles and computers

In a scenario where multiple Apollo x16D devices are configured on the same network, but used with different computers and UAD Console connections (for example, a computer lab), the UAD Console clock source should be set to DANTE. This setting will prevent clocking issues between the separate devices. In this configuration, any one of the x16Ds on the network, or another Dante device, can be the clock leader.

---

# Clocking Use Case Tables

The following tables describe settings for the x16D(s) in your system in several scenarios.

**Important:** As a general rule, if you set an Apollo x16D as the Preferred Leader, we recommend that you do not enable the Preferred Leader option for any other device in the Dante configuration, so that the network leadership assignment is predictable. This is especially important when the clock source for the x16D is set to Internal.

## Apollo x16D is the monitor unit

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | **Clock Source = Dante** | **Clock Source = Internal** | **Clock Source = Word Clock or AES/EBU** |
| **Monitor Unit** | **Dante Clock Leadership requirements** | The x16D monitor unit or another Dante device on the network can be the Dante clock leader. | The x16D monitor unit must be the Dante clock leader, otherwise audio issues will occur. | Either the external clock device or the x16D monitor unit must be the Dante clock leader, otherwise audio issues will occur. |
| **Automatic Dante Controller settings** | "Enable Sync to External" is forced OFF. | "Preferred Leader" is forced ON  "Enable Sync to External" is forced ON. | "Enable Sync to External" is forced ON. |
| **Expander Unit(s)** | **Dante Clock Leadership requirements** | An expander unit x16D cannot be the Dante clock leader. | | |
| **Automatic Dante Controller settings** | "Preferred Leader" is forced OFF. "Enable Sync to External" is forced OFF. | | |

## Apollo x16D is NOT the monitor unit

Note that when Apollo x16D is not the monitor unit, you cannot select DANTE as the clock source in UAD Console. Clock settings are managed by the Dante network in this scenario.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | **Clock Source = Dante** | **Clock Source = Internal** | **Clock Source = Word Clock, AES/EBU, ADAT, or SPDIF** |
| **Monitor Unit** | **Dante Clock Leadership requirements** | N/A | N/A | N/A |
| **Automatic Dante Controller settings** | N/A | N/A | N/A |
| **Expander Unit(s)** | **Dante Clock Leadership requirements** | N/A (Dante clock not available) | One of the expander unit x16Ds must be the Dante clock leader, otherwise audio issues will occur. | Either the external clock device or an expander unit x16D must be the Dante clock leader, otherwise audio issues will occur. |
| **Automatic Dante Controller settings** | N/A | "Preferred Leader" is forced ON.  "Enable Sync to External" is forced ON. | "Enable Sync to External" is forced ON. |

---

# Dante Device Lock

Device Lock is a Dante feature that allows you to lock a supported Dante device so it cannot be reconfigured without first explicitly unlocking. When a device is locked, audio continues to flow according to its existing configuration, but the configuration cannot be changed, and Dante Controller settings for the device are read-only.

**Note:** If you lose your device PIN, you can reset it to unlock your device. See "Unlocking a Device When You Have Forgotten the PIN" in the [Device Lock chapter](https://dev.audinate.com/GA/dante-controller/userguide/webhelp/content/device_lock.htm) of the Dante Controller User Guide.

## Device Lock behavior within UAD Console

When Device Lock is enabled on any Apollo through the Dante Controller software, the following changes appear in UAD Console.

* **Sample Rate –** The "Sample Rate" setting is grayed out and unavailable. You cannot make changes to the sample rate when a device is locked, as doing so would cause audio issues.
* **Clock Source –** The Clock Source menu is grayed out and unavailable. Changes to the Clock Source setting could require other changes to devices in Dante Controller, to which any locked devices may not be able to adapt.
* **Network Reset –** The Network Reset switches grayed out and unavailable. Network settings cannot be changed when one or more devices are locked.
* **Monitor Unit Assignment –** You cannot change the monitor unit or device ordering when a device is locked.

---

# Monitor Modes & Channel Assignments

Apollo x16D use the following monitor and channel assignments. In most cases (unlike other Apollo devices), the ALT monitor outputs are on the MON L/R outputs.

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | **Analog Mon outputs** | **Dante outputs** | | | | | | | |
|  | MON L/R | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| Stereo | L/R | ALT L | ALT R | ALT 2 L | ALT 2 R |  |  |  |  |
| 2.1 | ALT L/R | L | R | – | LFE |  |  |  |  |
| LCR | ALT L/R | L | R | C |  |  |  |  |  |
| LCRS | ALT L/R | L | R | C | – | S |  |  |  |
| QUAD | ALT L/R | L | R | – | – | Ls | Rs |  |  |
| 5.1 | ALT L/R | L | R | C | LFE | Ls | Rs |  |  |
| 6.1 | ALT L/R | L | R | C | LFE | Ls | Rs | Cs |  |
| 7.1 | ALT L/R | L | R | C | LFE | Lrs | Rrs | Lss | Rss |
| 5.1.4 | ALT L/R | L | R | C | LFE | Ls | Rs | – | – |
| 7.1.4 | ALT L/R | L | R | C | LFE | Lss | Rss | Lrs | Rrs |
| 9.1.6 | ALT L/R | L | R | C | LFE | Lss | Rss | Lrs | Rrs |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | **Dante Outputs (cont'd)** | | | | | | | |
|  | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 |
| Stereo |  |  |  |  |  |  |  |  |
| 2.1 |  |  |  |  |  |  |  |  |
| LCR |  |  |  |  |  |  |  |  |
| LCRS |  |  |  |  |  |  |  |  |
| QUAD |  |  |  |  |  |  |  |  |
| 5.1 |  |  |  |  |  |  |  |  |
| 6.1 |  |  |  |  |  |  |  |  |
| 7.1 |  |  |  |  |  |  |  |  |
| 5.1.4 | Ltf | Rtf | Ltr | Rtr |  |  |  |  |
| 7.1.4 | Ltf | Rtf | Ltr | Rtr |  |  |  |  |
| 9.1.6 | Ltf | Rtf | Ltr | Rtr | Lw | Rw | Ltm | Rtm |

---

# Apollo x16D Driver Channels

This table lists the I/O numbers and names for all Core Audio / ASIO streams available at the default I/O Matrix Panel settings.

**Notes**

* In multi-unit systems, channels marked with (m) are available on the monitor unit only.
* At 176.4 kHz and 192 kHz sample rates, channels marked with † are unavailable.

## Apollo x16D Driver Default I/O Table

|  |  |  |  |
| --- | --- | --- | --- |
| **INPUTS** | | **OUTPUTS** | |
| 1 | DANTE 1 | 1 | MON L |
| 2 | DANTE 2 | 2 | MON R |
| 3 | DANTE 3 | 3 | DANTE 1 |
| 4 | DANTE 4 | 4 | DANTE 2 |
| 5 | DANTE 5 | 5 | DANTE 3 |
| 6 | DANTE 6 | 6 | DANTE 4 |
| 7 | DANTE 7 | 7 | DANTE 5 |
| 8 | DANTE 8 | 8 | DANTE 6 |
| 9 | DANTE 9 | 9 | DANTE 7 |
| 10 | DANTE 10 | 10 | DANTE 8 |
| 11 | DANTE 11 | 11 | DANTE 9 |
| 12 | DANTE 12 | 12 | DANTE 10 |
| 13 | DANTE 13 | 13 | DANTE 11 |
| 14 | DANTE 14 | 14 | DANTE 12 |
| 15 | DANTE 15 | 15 | DANTE 13 |
| 16 | DANTE 16 | 16 | DANTE 14 |
| 17 | AES/EBU L | 17 | DANTE 15 |
| 18 | AES/EBU R | 18 | DANTE 16 |
| 19† | VIRTUAL 1\* | 19 | AES/EBU L |
| 20† | VIRTUAL 2\* | 20 | AES/EBU R |
| 21† | VIRTUAL 3\* | 21† | VIRTUAL 1\* |
| 22† | VIRTUAL 4\* | 22† | VIRTUAL 2\* |
| 23† | VIRTUAL 5\* | 23† | VIRTUAL 3\* |
| 24† | VIRTUAL 6\* | 24† | VIRTUAL 4\* |
| 25† | VIRTUAL 7\* | 25† | VIRTUAL 5\* |
| 26† | VIRTUAL 8\* | 26† | VIRTUAL 6\* |
| 27† | MON L\* (m) | 27† | VIRTUAL 7\* |
| 28† | MON R\* (m) | 28† | VIRTUAL 8\* |
| 29† | AUX1 L\* (m) | 29 | CUE1 L |
| 30† | AUX1 R\* (m) | 30 | CUE1 R |
| 31† | AUX2 L\* (m) | 31 | CUE2 L |
| 32† | AUX2 R\* (m) | 32 | CUE2 R |
| 33 | TALKBACK 1 | 33† | CUE3 L |
| 34 | TALKBACK 2 | 34† | CUE3 R |
|  | | 35† | CUE4 L |
| 36† | CUE4 R |
| \*Software Outputs (for DAW inputs) | | \*Software Inputs (for UAD Console inputs) | |
