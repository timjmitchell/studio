Source: https://ableset.com/docs/multi-file-projects

# Multi-File Projects

AbleSet's multi-file project feature allows you to split your Ableton Live
project into one project file per song. This is especially useful if you have a
lot of songs and handling them all in one session either gets too messy or you
notice Live struggling to keep up.

To enable the multi-file project mode, go to AbleSet's settings menu and click
on *Multi-File Project -> Choose Project Folder...*

You can then select a folder containing all songs that should be loaded into the
setlist. This could be a Live project folder containing multiple project files,
or a normal folder containing multiple Live projects – the folder structure
doesn't really matter.

The filename of your songs can contain [cue notation](https://ableset.com/docs/locator-notation) like
notes, colors, and the song duration – for example:
`Why We Are {some notes} [blue] [3.42].als`

Since file systems don't support the `:` character in filenames, it can be
replaced with a `.` for durations, as shown in the example above.

Here's an example:

![Example Folder Structure](https://ableset.com/images/docs/16-multi-file-projects/example-structure.png)

Each project file needs to contain at least one [locator](https://ableset.com/docs/locator-notation)
at the start of the song and one Ableton Locator IconSONG END or Ableton Locator IconSTOP locator at
the end of the song.

## Options

The *Save Changes Before Loading Project* option allows you to decide whether
the current project file should be saved when loading a new song. By default,
this is enabled to prevent data loss, but if you're sure you don't want any
changes to be saved, you can disable this to speed up switching between songs.

## The ableset.json File

This file is stored in the folder you selected as the multi-file project root
and contains information about the current setlist, e.g. the order of songs, the
setlist name, etc.

## Caveats

* One project file can currently only contain one song
