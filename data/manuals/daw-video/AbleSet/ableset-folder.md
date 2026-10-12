Source: https://ableset.com/docs/ableset-folder

# The AbleSet Folder

When you open a project in Ableton Live, AbleSet automatically creates a folder
called "AbleSet" in your project directory. This folder contains settings and
resources that can be shared between computers if you ever copy or move your
project over.

The folder contains a number of sub-folders:

![AbleSet Folder with 6 Sub-Folders](https://ableset.com/images/docs/28-ableset-folder/folder-contents@2x.png)

Below, I'll explain each folder and their contents.

## Canvases

This folder contains your [Canvases](https://ableset.com/docs/canvas). If you'd like to share a
Canvas, just copy its file and paste it into the *Canvases* folder of another
project.

If you upload images to a Canvas, AbleSet creates a *Resources* folder inside
this folder and places them there. You can also manually add images to that
folder to use them in your Canvases.

## Cues

This folder contains generated [audio cues](https://ableset.com/docs/cues) for your songs and
sections, grouped by the voice model used to generate them.

## Custom Styles

This folder contains project-specific [Custom Styles](https://ableset.com/docs/custom-styles).
These get applied to the AbleSet web app in addition to the global Custom
Styles.

Any files you place in this folder (e.g. images) can be accessed under
`/custom-styles/project` from the web app.

## Project File Cache

When you open a project file in Live, AbleSet parses that file in the background
to get information about locators, clips, tempo, time signatures, etc. which it
can't access using Live's Control Surface API.

These parsed results are stored in the *Project File Cache* folder so they can
be loaded instantly the next time you open the project.

For [Multi-File Projects](https://ableset.com/docs/multi-file-projects), AbleSet parses all project
files in advance to give you information about sections, durations, etc. before
they're opened in Live.

If the folder becomes too large or you're experiencing issues with outdated
information, feel free to delete it and restart AbleSet.

## Scripting

This folder contains the [Project Script](https://ableset.com/docs/scripting#the-project-script)
and a *shared-variables.json* file containing all persisted
[Shared Variables](https://ableset.com/docs/scripting#shared-variables).

You can edit the Project Script from here, but I'd recommend using the script
editor on the Settings page, as it offers autocomplete and highlights errors.

Deleting the *shared-variables.json* file resets all shared variables.

## Setlists

The *Setlists* folder contains all saved setlists. When you overwrite a saved
setlist, the previous version is stored in a *Backup* folder with a timestamp so
you can restore it if needed.

Files in subfolders are ignored, so you could create an "Archive" folder and
move old, unused setlists there to hide them from the setlist load dialog.

## Settings

This folder contains all of AbleSet's settings. When you create a new Ableton
Live project, AbleSet will copy the settings of the previous project into the
new project's *Settings* folder.

Computer-specific settings, like [AbleNet](https://ableset.com/docs/ablenet) settings and the path
to the [Multi-File Projects](https://ableset.com/docs/multi-file-projects) folder are stored in a
`specific-[hostname].json` file. This avoids issues with apps that automatically
synchronize your project folder between two computers.
