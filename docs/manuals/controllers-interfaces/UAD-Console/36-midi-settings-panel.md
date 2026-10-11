Source: https://help.uaudio.com/hc/en-us/articles/25403799874068-MIDI-Settings-Panel
Updated: 2025-03-31T22:23:52Z

# MIDI Settings Panel

UAD Console supports the ability to use MIDI to remotely set the tempo used for the Tempo Sync feature, and to recall Plug-In Scenes with MIDI messages. The MIDI panel is where the specific MIDI controls are set. MIDI data is received by UAD Console via the operating system.

![plug-in-scenes-midi-settings.png](https://help.uaudio.com/hc/article_attachments/28354856957460)

*The MIDI panel*

# Device

Sets the MIDI device to be used as the source for MIDI control. To set the device, click the MIDI DEVICE menu and choose a new device from the drop menu.

**Note:** Only devices configured in the operating system are available for selection in this menu.

# Tap Tempo Channel

Specifies the MIDI channel to be used for Tape Tempo MIDI control. To set the channel, click the field and enter a numerical value between 1 – 16.

# Tap Tempo Event

UAD Console can receive note or controller data for MIDI control of Tap Tempo. These two settings define the MIDI data type and value used for MIDI control. For instructions, see [Changing tempo via MIDI.](https://help.uaudio.com/hc/en-us/articles/25348339047572#h_01HTR7WHW9TZQ10B8KBCE2SD2T)

## MIDI Type Menu

Sets the MIDI data type to be used as the source for MIDI control. To set the data type, first click the drop menu then choose CONTROLLER or NOTE from the menu, or send the value from the MIDI controller.

## MIDI Value Field

Sets the MIDI data value to be used as the source for MIDI control. To set the data value, first click the field then enter a numerical value between 0 – 127, or send the value from the MIDI controller.

## MIDI Note Table

When NOTE is used as the MIDI type, the table below can be used as a reference for MIDI note values.

![](https://help.uaudio.com/hc/article_attachments/25403814760340)

*MIDI note numbers by note name and octave*

# Plug-In Scenes Channel

For more information on Plug-In Scenes, see [Plug-In Scenes](https://help.uaudio.com/hc/en-us/articles/28354758319892).

Specifies the MIDI channel to be used for Plug-In Scene control. To set the channel, click the field and enter a numerical value between 1 – 16.

# Plug-In Scenes Event

UAD Console can receive Note or Program Change data for Plug-In Scene changes. These two settings define the MIDI data type and value used for MIDI control.

## MIDI Type Menu

Sets the MIDI data type to be used as the source for MIDI control. To set the data type, first click the drop menu then choose NOTE or PROGRAM CHANGE from the menu, or send the value from the MIDI controller.

* If the controller is sending MIDI Program Change messages, Scenes 1–128 correspond to MIDI program change messages 0–127. Your controller may label these as 0–127 or 1–128, so it is important to check that your scenes are switching correctly.
* If the controller is sending Note data, Scenes 1-128 correspond to MIDI notes C(-1)–G(9).
