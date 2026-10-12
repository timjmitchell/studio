Source: https://ableset.com/docs/lyrics

# Lyrics

[](/images/docs/12-lyrics/lyrics.webm)

AbleSet supports displaying synchronized lyrics with your songs. This requires
Live 11 or higher to work properly.

Each track that contains the `+LYRICS` flag is recognized as a lyrics track. To
get started, create a MIDI track called `Vocals +LYRICS` that contains one clip
per lyrics line. AbleSet will automatically create a synchronized lyrics view
based on this.

Creating these lyrics clips manually can be a chore, so I've created a tool that
allows you to paste your lyrics, synchronize them to your backing track, and
download them as a Live project containing a track with your synchronized
lyrics:

[Open Lyrics Track Generator](https://ableset.com/tools/lyrics)

If you already have LRC files with synchronized lyrics, you can use this tool
to convert them to Ableton project files that can be imported into your project:

[Open LRC Lyrics Track Generator](https://ableset.com/tools/lyrics-lrc)

## Multiple Lyrics Tracks

AbleSet Standard and Pro support multiple lyrics tracks, so you could create a
`Lead Vocals +LYRICS` track for your lead singer, a `Backing Vocals +LYRICS`
track for your backing singers, and a `Chords +LYRICS` track for other
musicians.

AbleSet Intro only supports one lyrics track. If your project contains multiple
lyrics tracks, it will display the first one.

If multiple tracks are available, each device can choose which one they'd like
to see on the web app.

## Styling

The lyrics view supports basic Markdown to make parts of your lyrics bold or
italic. To make a part of your lyrics *italic*, wrap it in single asterisks,
e.g. `*italic line*`. To make a part of your lyrics **bold**, wrap it in double
asterisks, e.g. `**bold line**`.

To give a line a color, you can add it in square brackets to the beginning of
the line, e.g. `[blue] Why We Are`. The following colors are available:

* Gray
* Red
* Orange
* Amber
* Yellow
* Lime
* Green
* Emerald
* Teal
* Cyan
* Sky
* Blue
* Indigo
* Violet
* Purple
* Fuchsia
* Pink
* Rose

If you want all lines of a lyrics track to have the same color, you can add it
to the track name in square brackets, e.g. `Vocals +LYRICS [blue]`.

If you add either the Ableton Locator Icon+CLIPCOLORS or Ableton Locator Icon+CC flag to the lyrics
track name, AbleSet will use the color of your clips for the lines. Each column
of Live's color picker corresponds to one color in AbleSet:

The text size can be changed using `[large]`, `[small]`, or `[tiny]`, and the
alignment can be changed using `[left]` or `[center]`. If you prefer a
monospaced font, you can add the `[mono]` attribute.

Other available styling options include `[nofade]` to disable fading inactive
lines, `[nozoom]` to disable zooming out inactive lines, `[nosections]` to hide
section headers, and `[linemarker]` to show a marker next to the current line.

If you'd like to align the current lyrics line to the top of the page, you can
add the `[top]` attribute. To show a number of lines before the current line,
you add that number to the attribute, e.g. `[top+2]` to show 2 previous lines
before the current line.

You can also use `[progress]` to display a progress bar on each line as it's
playing:

[](/images/docs/12-lyrics/progress-h265.mp4)

You can combine these attributes, e.g: `Vocals +LYRICS [blue] [small] [left]`

## Chords

To add chords to your lyrics, you can use the [ChordPro](https://www.chordpro.org/chordpro/chordpro-chords/) syntax. As soon as one
line contains chords, the entire song's lyrics track is recognized as a
lyrics&chords track which changes the layout of lyrics, automatically aligning
all lines to the left for better readability. For example:

```
[F] I know you tried so many ti[Am]mes
To be [G]who you used to be
[F] I know you tried so many ti[Am]mes [G]
```

Gets turned into:

```
F                            Am
  I know you tried so many times
      G
To be who you used to be
F                            Am  G
  I know you tried so many times
```

These chords can be transposed on a per-song level. Just add the number of
semitones you'd like to transpose to the song's locator, e.g. Ableton Locator IconFollow Night
[+2] or Ableton Locator IconFollow Night [-3].

You can also transpose all chords on a track by adding the number of semitones
to your lyrics track's name in square brackets, e.g. `Vocals +LYRICS [+2]`.

By default, AbleSet will use sharps in transposed chords. If you prefer flats,
you can add that to the transpose attribute as well: `Vocals +LYRICS [+2b]`.
This also works on song locators.

If you'd like to change the color of the chords, you can add a color attribute
to the track name, like `[chords:red]`.

You can also hide all chords on a lyrics track using `[nochords]`, or display
only chords using the `[onlychords]` attribute.

## Images

To insert images into your lyrics, create a "Lyrics" folder in your Ableton
project folder and add some images to it. The folder could look like this:

![Lyrics Folder](https://ableset.com/images/docs/12-lyrics/lyrics-folder.png)

You can then reference those images in your lyrics clips using their relative
path name. For example, you could reference the image located at "atw/atw 1.png"
by creating a lyrics clip named `[img:atw/atw 1.png]`.

By default, images always try to take up as much width as possible without
growing larger than the height of 3 lyrics lines. If you'd like images to fill
the entire screen, you can add the `[full]` attribute, e.g.
`[img:atw/atw-bass-1.png] [full]`. This is useful for displaying sheet music
pages, for example.

If you'd like all images on a lyrics track to fill the entire screen, you can also
add the `[full]` attribute to the lyrics track name, e.g. `Vocals +LYRICS [full]`.

AbleSet can also scale images to fill the entire width of the browser and scroll
them continuously. To enable this, add the `[scroll]` attribute either to an
image clip or a lyrics track.

This feature supports PNG, JPEG, GIF, SVG, and WEBP images.

If you'd like to generate lyrics clips from a PDF, e.g. with sheet music, you
can use the Lyrics Image Generator:

[Open Lyrics Image Generator](https://ableset.com/tools/lyrics-images)

## Line Breaks

You can insert line breaks into lyrics lines using the `\` character – e.g.
`Line 1 \ Line 2`. This allows you to have multiple lines in the same MIDI clip
which all get highlighted at the same time.

## All Songs Mode

By default, AbleSet only displays the lyrics of the current song, but you can
add the `[allsongs]` attribute to your lyrics track name to make it display the
lyrics of all songs on one continuous page.

This can be useful if songs are flowing into each other and you already want to
read the first line of the next song before it starts.

## Lines Crossing Sections

In some cases, a line might cross a section. By default, if more than half of
the line is after the section start, AbleSet will display the line after the
section header. The line will be displayed before the section header.

If you'd like to override this behavior for a line, you can add an attribute to
its name, e.g. `[<] Line` to display the line before the section header and
`[>] Line` to display it after the section header.

## Time Delay

If you know your video or audio signal will have a certain delay, you can add
that to the lyrics track to offset the lyrics display.

For example, if you know that your audio has a delay of 150ms, you can add
`[+150ms]` to the track name which delays lyrics by that time.

If you're streaming the lyrics window over the network and you know there will
be a 200ms video latency, you can add a negative delay, like `[-200ms]` instead
to offset the latency and ensure the lyrics stay in sync with your song.

You can also delay the lyrics track by a number of beats, e.g. `[+1n]` to delay
it by one beat, of `[-2n]` to show the next line two beats earlier.

Delays are only applied while Live is playing.
