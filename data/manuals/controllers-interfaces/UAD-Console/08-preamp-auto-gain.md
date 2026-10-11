Source: https://help.uaudio.com/hc/en-us/articles/30921736610836-Preamp-Auto-Gain
Updated: 2026-01-15T18:52:51Z

# Preamp Auto-Gain

Auto-Gain automatically adjusts gain on Apollo’s preamp inputs (mic, line, and Hi-Z), according to detected input levels. To use Auto-Gain, you play audio sources at your loudest volume levels while running Auto-Gain in UAD Console, and the gain on all selected Apollo preamps is automatically adjusted.

**Note:** To get the most accurate levels for guitar amp and bass amp plug-ins, do not use Auto-Gain to set gain levels on electric guitar Hi-Z inputs. Set preamp gain at the minimum level when using the Hi-Z inputs with amp plug-ins.

![](https://help.uaudio.com/hc/article_attachments/30992585584660)

# Auto-Gain Requirements

Auto-Gain is available on all Apollo X Gen 2 preamp channels, including rack and desktop models. The following Apollo X Gen 2 interfaces have preamps:

* Apollo Twin X Gen 2
* Apollo x4 Gen 2
* Apollo x6 Gen 2
* Apollo x8 Gen 2
* Apollo x8p Gen 2

# Using Auto-Gain

**CAUTION:** Auto-Gain automatically adjusts preamp levels for recording. To avoid damage to your hearing, confirm your monitor levels are set safely before proceeding.

1. On any preamp channel, press the Auto-Gain button under the gain knob. The Auto-Gain floating window opens.  
     
       ![](https://help.uaudio.com/hc/article_attachments/30992574617236)
2. By default, Auto-Gain listens and adjusts levels for 10 seconds. To increase or decrease the duration by ±5 seconds, press the -5 or +5 buttons. You can adjust the duration while Auto-Gain is listening.
3. To detect gain levels, press the Start button and input your audio source at its loudest level. Auto-Gain is adjusted during or after listening, depending on the Apply Gain option under Show More.
4. The Auto-Gain floating window closes after the listening duration completes. To close the Auto-Gain window, click Done.

**Note:** When using Auto-Gain with stereo linked inputs, the same gain amount is applied to both inputs. Auto-Gain sets the level based on the peak information from the loudest input.

**Tip:** You can set Auto-Gain on multiple preamps simultaneously. Simply click the Auto-Gain button for each preamp you want to adjust. The Auto-Gain options in the floating window apply to all Auto-Gain-enabled preamps.

## Auto-Gain options

In the Auto-Gain floating window, click Show More to see all Auto-Gain options.

**Tip:** To return Duration, Listening Threshold, and Peak Target to their default values, Option-click (macOS) or Alt-click (Windows).

![](https://help.uaudio.com/hc/article_attachments/30992574617620)

### Duration

Sets the amount of time that Auto-Gain listens while setting gain levels.

The default setting is 10 seconds, which may be too short. To set a different duration, click and drag up or down in the box, or click the -5 or +5 buttons to adjust the duration. You can also click in the box and type a new value, then press Enter.

**Note:** The maximum duration is 90 seconds.

### Apply Gain

Sets the Auto-Gain adjustment behavior.

* WHILE LISTENING applies gain changes every two seconds for the Auto-Gain duration. You can only use WHILE LISTENING with one or two preamps enabled for Auto-Gain.
* AFTER LISTENING applies the gain change after the Auto-Gain listening duration is complete.

### Listening Threshold

The Listening Threshold determines the lowest level at which Auto-Gain detects a signal and begins adjusting gain. This setting ensures that Auto-Gain doesn’t set very loud gains when no detectable signal is available. The default setting is -50 dBFS, which may be too quiet for low level sources. To set a different threshold, click and drag up or down in the box, or click in the box and type a new value, then press Enter.

### Peak Target

The Peak Target determines the maximum peak level that Auto-Gain should set for your material. The default setting is -8 dBFS, but you can adjust it higher or lower. Be aware that higher settings (less headroom) increase the risk of digital clipping. To set a different peak target, click and drag up or down in the box, or click in the box and type a new value, then press Enter.

## Auto-Gain with Unison plug-ins

The following UAD plug-ins can be used in the Unison insert with Auto-Gain:

* API Preamp
* API Vision Channel Strip
* API Vision Channel Strip Legacy
* Neve 1073
* Neve 1084
* Neve 88RS
* Neve Preamp
* SSL 4000 E Channel Strip

If a Unison plug-in doesn’t support Auto-Gain, the Auto-Gain button is grayed out after the Unison plug-in is inserted.

260115
