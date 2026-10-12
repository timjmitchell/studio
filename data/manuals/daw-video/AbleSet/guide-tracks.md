Source: https://ableset.com/docs/guide-tracks

# Guide Tracks

AbleSet supports managing your guide tracks. There are three types of supported
guide tracks:

* `+GUIDE`
  + Tracks containing the `+GUIDE` flag are active by default and only muted
    when you're jumping to another section or the current section is being
    looped
* `+LOOPGUIDE`
  + Tracks containing the `+LOOPGUIDE` flag are muted by default and only
    unmuted when you loop the current section. This allows you to add an audio
    cue announcing that the same section will be played again
* `+JUMPGUIDE`
  + Tracks containing the `+JUMPGUIDE` flag are muted by default and only
    unmuted while a section other than the one following the current section
    is cued

Please note that these flags are case-sensitive and need to be added to the
track name exactly as shown here.

Both audio and MIDI tracks can be marked as guide tracks. Just add one of the
guide track flags to the track's name to let AbleSet manage it.

Here's a video showing the feature in action:

[Open YouTube Video](https://youtu.be/u0Zd9RX5rKA?t=357)
