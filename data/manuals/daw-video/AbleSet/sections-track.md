Source: https://ableset.com/docs/sections-track

# The Sections Track

You can use a MIDI track to define song sections. This cleans up the session
since you have to use fewer locators.

This feature requires Live 11 or higher to work properly.

To get started, create a MIDI track called "Sections" and add empty MIDI clips
to it where the song sections are. It might look a bit like this:

![MIDI Clips on the Sections Track](https://ableset.com/images/docs/04-sections-track/midi-clips.png)

AbleSet will recognize these clips as section markers and add them to your song.
The clip duration doesn't matter – each section ends where the next one begins.

![Recognized Sections](https://ableset.com/images/docs/04-sections-track/recognized-sections@2x.png)

Alternatively, you can give the track any other name and include a `+SECTIONS`
flag. You can also use the [locator notation](https://ableset.com/docs/locator-notation) syntax to
add comments and set a color for a section.

If you like, you can combine the use of section locator and clips in your songs.
If there's a locator and a section clip at the same time, AbleSet will prioritize
the information stored in the locator.

Due to some limitations with Ableton Live's API, sections defined by clips can
only be jumped to when Live isn't currently playing. If you need that functionality,
you can place locators named Ableton Locator Icon> at the same position as the section clip you'd
like to be able to jump to.

As a workaround, AbleSet offers the ability to automatically place locators at
each section clip. To access it, open the settings page, scroll down to the
"Tools" section, and then click "Place Locators on Section Clips" to start this
process. To reverse it, click "Remove Automatically Placed Locators".

The locators will use Live's default naming, which is just an increasing number.
You can rename the locators to Ableton Locator Icon> for consistency, or Ableton Locator Icon>> if
you'd like to mark the section as a [quick jump](https://ableset.com/docs/locator-notation/#section-cues)
section. You can also rename the locators to the section name, just remember to
add a Ableton Locator Icon> at the beginning, e.g. Ableton Locator Icon> Chorus.

Even with these limitations, section clips are a great way for defining sections
that you want to jump to during rehearsals – combined with the
[count-in](https://ableset.com/docs/count-in) function, this is a great way to practice certain
sections of a song.

## Using Clip Colors For Sections

If you add either the Ableton Locator Icon+CLIPCOLORS or Ableton Locator Icon+CC flag to the section
track name, AbleSet will use the color of your clips for the sections. Each
column of Live's color picker corresponds to one color in AbleSet:
