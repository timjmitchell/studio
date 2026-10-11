Source: https://help.uaudio.com/hc/en-us/articles/25348282201364-Mixer-Navigation-Modifiers
Updated: 2025-03-31T22:23:52Z

# Mixer Navigation Modifiers

Modifiers add several controls to UAD Console that make common workflow tasks much faster and easier to accomplish. With modifiers, you can easily power items on and off, remove items, copy and paste items, isolate channels, and set controls to their defaults. When you click a mixer modifier button, the control latches, and flashes to indicate it is active.

![](https://help.uaudio.com/hc/article_attachments/25348282171540)

# Modifier Latch

![](https://help.uaudio.com/hc/article_attachments/25348286299156)

*Power option latched*

When a Modifier switch is clicked, the switch flashes yellow, indicating that the function is latched and ready to be applied.

# Modifier Unlatch

The latched option is unlatched (the switch stops flashing) when:

* The Modifier switch, or another Modifier switch, is clicked
* No Modifiers are applied within the Modifiers Timeout period

## Modifiers Timeout

![](https://help.uaudio.com/hc/article_attachments/25348282183444)

When a modifier is latched, it is automatically unlatched (times out) after the Modifiers Timeout period to prevent inadvertent modifications.

The Modifiers Timeout is a preference set in the Settings > Options panel. The default Modifiers Timeout period is six seconds/flashes.

## Swiping Across Modifiers

Modifiers can be adjusted quickly across many items in the mixer by swiping. When a Modifier switch is latched, click and hold the mouse, then drag vertically and/or horizontally across highlighted items to perform the function on multiple items.

**Tip:** Modifier swipe shortcuts are the fastest way to perform the same function on multiple items.

![](https://help.uaudio.com/hc/article_attachments/25348286304276)

# Power Modifier

This option toggles a plug-in, send, or cue’s power state, or all plug-ins, sends, or cues on a channel. When disabled, plug-ins no longer use UAD DSP resources, and sends or cues are disabled.

![](https://help.uaudio.com/hc/article_attachments/25348286305556)

#### To power items on/off

1. Click the Power button on the Modifiers panel. Power modifier icons appear on all items that can be powered off or on.
2. Click individual power modifiers, or swipe horizontally or vertically across multiple modifiers, to toggle power on or off.
3. To power on/off all items of the same type for a channel, click the power button next to the item name (Inserts, Sends, or Cues).

**Note:** Toggling power for all inserts on a channel does not toggle power to the Unison insert.

# Remove Modifier

The Remove Modifier removes a plug-in or all plug-ins from a channel.

![](https://help.uaudio.com/hc/article_attachments/25348282191636)

#### To remove plug-ins with the Remove Modifier

1. Click the Remove button on the Modifiers panel. Remove modifier icons appear on plug-ins that can be removed.
2. Click individual remove modifiers, or swipe horizontally across multiple modifiers, to remove plug-ins. To remove all plug-ins from a channel, click the remove icon next to the Inserts label.

# Copy / Paste Modifier

The Copy and Paste Modifiers copy a plug-in, send, cue, or channel and paste it where you choose.

![](https://help.uaudio.com/hc/article_attachments/25348286309012)

#### To copy and paste items

1. Click the Copy button on the Modifiers panel. Copy modifier icons appear on all items that can be copied and pasted, including plug-ins, sends, cues, and entire channels.
2. Click the individual copy modifie for the item you want to copy. After the  modifier is copied, the copy modifier turns to a red Paste modifier. Destinations to which the copied item can be pasted are highlighted.
3. Click individual paste modifiers, or swipe across multiple modifiers to paste multiple items.

#### To copy and paste entire Channel Strips

1. Click the Copy button on the Modifiers panel. Copy modifier icons appear at the bottom of each channel strip.
2. When Copy is latched, click the copy modifier at the bottom the channel strip you want to copy. The Copy button switches to Paste.
3. Click one or more channel strip destination icons to paste to available channel locations.

**Note:** You cannot swipe across multiple channels when pasting a channel strip. To paste multiple channel strips, click each destination individually.

![](https://help.uaudio.com/hc/article_attachments/25348286310932)

# Isolate Modifier

The Isolate modifier allows you to quickly Isolate channels. Isolate allows you to seamlessly monitor live hardware inputs with Realtime UAD Processing, even when changing UAD Console and LUNA sessions. Isolated channels always retain their current settings when different UAD Console and LUNA sessions are loaded. Isolated channels are also not controlled by LUNA.

![](https://help.uaudio.com/hc/article_attachments/25348282194068)

**Tip:** To quickly isolate an individual channel, right-click a channel’s input label then choose Isolate from the Input Label Menu.

# Set Default Modifier

The Set Default modifier returns a parameter to its default value.

![](https://help.uaudio.com/hc/article_attachments/25348286314004)

**Note:** The Set Default modifier is primarily for knob and fader values. It does not apply to any preamp settings, plug-in inserts, SOLO/MUTE switches, monitor levels, customized input names, and similar functions.

1. Click the Set Default switch on the Modifiers panel. The Set Default button blinks.
2. Click a control to return the control to its default value.

# Settings Switch

![](https://help.uaudio.com/hc/article_attachments/25348282195348)

The SETTINGS switch is located at the bottom of the Mixer Navigation column. Click to open the UAD Console Settings window, where many global settings are defined. For complete details, see [UAD Console Settings](https://help.uaudio.com/hc/en-us/articles/25403524417812).

# Clear Switches

![](https://help.uaudio.com/hc/article_attachments/25348286320660)

The Clear switches are located near the bottom of the UAD Console screen, in the Options column.

## Clear Solo

Whenever Solo is engaged on any channel input, the Clear Solo switch is highlighted. Click the Clear Solo switch to deactivate Solo on any channel inputs.

**Tip:** Click Clear Solo again to return all channels to their previous Solo states.

## Clear OL

This switch clears all over limit (clip) indicators and peak hold indicators on all meters.

You can also clear individual meters or all meters by right-clicking/Ctrl-clicking in the meter display, and choosing Meter or All Meters under Clear.

![clear-meters.png](https://help.uaudio.com/hc/article_attachments/25348282196884)
