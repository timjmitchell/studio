Source: https://ableset.com/docs/flags

# Flags Used in AbleSet

AbleSet uses flags to identify what locators and tracks do. All flags need to be
written in all-caps to be recognized. Here's a list of all available flags:

## Locators

* Ableton Locator Icon+PAUSE [pauses playback](https://ableset.com/docs/locator-notation#pause-locators) when
  the playhead reaches this locator. This is mostly useful on section locators.
* Ableton Locator Icon+LOOP and Ableton Locator Icon+LOOPFULL make AbleSet automatically [activate a
  loop](https://ableset.com/docs/locator-notation#loop-locators) from the current to the next
  section.
* Ableton Locator Icon+SKIP [skips the section](https://ableset.com/docs/locator-notation#skipping-sections).
  The next section must have a locator.
* Ableton Locator Icon+END treats the section and all following sections as skipped for the
  song, useful for defining sections that aren't usually part of the song but
  might need to be played spontaneously. See the
  [docs](https://ableset.com/docs/locator-notation#the-end-flag) for more information.
* Ableton Locator Icon+JUMP and Ableton Locator Icon+STAY are only valid on a Ableton Locator IconSTOP locator
  ([docs](https://ableset.com/docs/locator-notation#stop-locators)) and override AbleSet's default
  behavior after stopping playback.

## Tracks

* `+SECTIONS` marks a track as a [Sections Track](https://ableset.com/docs/sections-track)
  + A track named "Sections" is also interpreted as a Sections Track
  + There can only be one Sections Track per project. If multiple tracks are
    marked as Sections Tracks, AbleSet uses the first one.
* `+LYRICS` marks a track as a [Lyrics Track](https://ableset.com/docs/lyrics).
* `+CLIPCOLORS` or `+CC` can be used on Sections and Lyrics tracks and makes
  AbleSet use the color of the clips on that track to color sections or lyrics.
* `+OSC` marks a track as an [OSC Track](https://ableset.com/docs/osc-tracks).
* `+GUIDE`, `+LOOPGUIDE`, and `+JUMPGUIDE` mark a track as a
  [Guide Track](https://ableset.com/docs/guide-tracks), so AbleSet automatically mutes and unmutes
  it depending on the state of your set.
* `+GROUP` or `+G` adds a track to a [Track Group](https://ableset.com/docs/mixer)
* `+CLICK` marks a track as a click track and adds it to the "Click" Track Group
* `+NEVERMUTE` or `+NM` ensures that a track is never muted, even if other
  tracks are soloed ([docs](https://ableset.com/docs/mixer#the-nevermute-flag)).
* `+FOLLOWSCENE` or `+FS` makes AbleSet automatically mute the track if the
  computer isn't currently selected on the connected
  [redundant audio interface](https://ableset.com/docs/audio-interfaces#the-followscene-flag).
