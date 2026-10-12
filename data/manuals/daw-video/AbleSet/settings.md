Source: https://ableset.com/docs/settings

# AbleSet Settings Reference

AbleSet's settings are split across two places. Here's an overview of them:

## Settings Page

### General

#### Show AbleSet in the Dock *(macOS only)*

Shows the AbleSet app icon in your macOS dock when enabled.

#### Default View

The view that will be shown by default when AbleSet is opened. Can be Setlist,
Performance, Lyrics, Canvas, Mixer, or a specific Lyrics or Canvas page.

#### Open AbleSet on Start

Automatically opens AbleSet's default view when a connection to Ableton Live has
been established.

#### Always Open AbleSet in a Floating Window

Opens AbleSet in a floating window instead of the browser.

#### Auto-Launch the Last Live Project

If Live isn't running when you start AbleSet, it will automatically be launched
with the last loaded project file.

### Playback

#### Autoplay

Starts playback when you jump to a song or section.

#### Auto-Jump to the Next Song

Automatically jumps to the next song after reaching the end of a song.

#### Always Stop at the End of Songs

Always stops playback at the end of songs, even if they don't have a stop
locator.

#### Restart Song Before Jumping Back

When this is enabled, jumping back one song will first jump back to the
beginning of the current song.

#### Stop by Default Instead of Pausing

This also means that pressing space in the web app stops playback instead of
pausing.

#### Disable Loop When Jumping

When this is disabled, you can cue another section or song without disabling the
loop.

#### Re-Enable Automation on Song Jump

When this is enabled, AbleSet automatically re-enables all automation when
jumping to a song.

#### Reset Tracks Back to Arrangement on Song Jump

When this is enabled, AbleSet automatically resets all clips that were
temporarily overridden from Session View back to the Arrangement when jumping to
a song.

#### Safe Mode

Prevents jumping to another song and shows a confirmation before pausing while
Live is playing. This does not apply to MIDI mapping and received OSC commands.

#### Jump Mode

Defines when AbleSet will jump to the queued song or section
(see [Jump Modes](https://ableset.com/docs/jump-modes)).

Can be *Quantized*, *End of Section*, *End of Song*, *Dynamic*, or *Manual*

#### Always Keep Playing When Jumping to Queued Songs

*Shown when Jump Mode is End of Song or Dynamic.*

When this is enabled, AbleSet won't stop playback after a song when another song
is queued, even if the song ends with a Ableton Locator IconSTOP locator or
*Always Stop at the End of Songs* is enabled.

#### Delay Before Jumping to Song File

*Shown when using a [Multi-File Project](https://ableset.com/docs/multi-file-projects).*

This delays jumping to a new song when using the jump forward/backwards buttons.
This is especially useful for jumping to a song in multi-file projects where
loading a new song can take a while. Can be *None*, *500ms*, *1s*, *2s*, or *3s*.

### Section Count-In

See the [Count-In documentation](https://ableset.com/docs/count-in) for more details.

#### Enable Section Count-In

This starts playback a few bars before the selected section.

#### Solo the Click Track during Count-In

Solo the click track during the count-in.

#### Count-In Duration

Can be *1 bar*, *2 bars*, or *4 bars*.

### MIDI Mapping, OSC & Scripting

#### Edit MIDI Mapping

Opens the [MIDI mapping](https://ableset.com/docs/midi-mapping) settings.

#### OSC Settings Standard Pro

Opens the OSC settings.

#### Project Script Pro

Opens the [Project Script](https://ableset.com/docs/scripting#the-project-script) editor.

#### Persist Shared Variables Pro

Persists shared variables between AbleSet restarts.

### Audio Interfaces Standard Pro

This shows a list of all connected [Audio Interfaces](https://ableset.com/docs/audio-interfaces),
with the ability to disable specific ones that you don't want to see in AbleSet.

### LTC Timecode Standard Pro

#### Display LTC Timecode

Shows the current timecode in AbleSet. This requires the
[LTC Display](https://ableset.com/link/ltc-display) to be loaded in your project.

A link to download or purchase the LTC Display Plugin is shown in this section.

### Setlist

#### Remove Played Songs Automatically

Automatically removes a song from the setlist after it has been played and jumps
to the next song.

### Mixer Pro

#### Include the Main Track as a Group

When this option is enabled, the Main track will be included on the mixer page.

#### Sync Group Solos & Mutes Between Songs

*Only shown when using a [Multi-File Project](https://ableset.com/docs/multi-file-projects).*

When this option is enabled, the solo and mute states of groups are transferred
between songs in a multi-file project.

#### Sync Group Volumes Between Songs

*Only shown when using a Multi-File Project and when Sync Group Solos & Mutes
Between Songs is enabled.*

When this option is enabled, the volumes of groups are transferred between songs in a multi-file project.

### Tools

These are action buttons rather than toggleable settings:

#### Set Clip Colors from Names

Sets the color of all clips in tracks with the `+CLIPCOLORS` or `+CC` flag to
the color in their name and removes the color from the name.

#### Place Locators on Section Clips

Creates locators for each section clip, allowing you to jump to them while
playback is running. Please reopen your project in Live after running this tool
to avoid audio dropouts and other issues.

#### Remove Automatically Placed Locators

Removes all automatically placed locators from the setlist.

### Debug

#### Connected Devices

Displays a list of all browsers that are connected to AbleSet.

#### Device Settings

Displays all device-specific settings on one page.

#### Debug Logs

Shows AbleSet's internal logs for debugging.

### Redundancy & AbleNet Standard Pro

See the [AbleNet documentation](https://ableset.com/docs/ablenet) for more information.

#### Enable AbleNet

Allows AbleSet to run in a redundant setup with other computers.

#### Follow Current Audio Interface Scene

Automatically switches the browser to the computer that's currently active on the connected audio interface.

### Host-Specific AbleNet Settings Standard Pro

The following settings appear for each connected host. The first host is always
the local computer, followed by any remote hosts.

#### IP Address

Displays this computer's current IP address.

#### Connect to Custom IPs

Connects directly to the given IP addresses of other computers. Don't enter the
computer's own IP. Can be comma-separated if you want to supply multiple
addresses (e.g. 192.168.1.100).

#### Connected Scene

This defines whether this computer is your main or backup computer, or if it's
connected to port A or B of your redundant audio interface.

#### Automatic Drift Correction

Automatically nudge this computer into sync if it has noticeable drift from
others. Don't enable this if you don't need it, and make sure that all audio
clips are warped if you do. Learn more [here](https://ableset.com/docs/ablenet#automatic-drift-correction).

#### Sync Playback Now

Brings this machine back in sync with others on the network if it's paused.
The button is disabled and shows "Live is Playing" when Live is already playing.
Learn more [here](https://ableset.com/docs/ablenet#sync-playback-now).

## Settings Menu

The Settings Menu appears when you click the AbleSet icon in your menu bar.

### Open AbleSet in Browser

Opens the AbleSet web app in your default browser

### Open AbleSet in a Floating Window

Opens AbleSet in a floating window instead of the browser

### Licensed to

Displays the license holder when activated. When AbleSet starts, this might say
"Fetching..." while the license is being checked. If no license is active, this
displays an **Activate or Buy a License** option.

### Manage Licenses

Opens the your AbleSet account in your browser. If your license is locked,
this option isn't shown.

### Deactivate Machine

Deactivates the current machine from your license, freeing up an activation slot
so you can activate it on another computer. If your license is locked, this
option isn't shown.

### Open Settings

Opens the AbleSet web app at the Settings page.

### Web App Password... Standard Pro

If this is activated, you'll have to enter your password to edit the setlist and
control playback using the web app

### Multi-File Project

This menu contains settings for using a
[Multi-File Project](https://ableset.com/docs/multi-file-project).

#### Choose Project Folder... / Change Project Folder...

Select the folder containing your project files.

#### Open Project Folder

When a folder is selected, opens it.

#### Save Changes Before Loading Project

If there are unsaved changes in the current Live project, AbleSet saves the
project instead of discarding them when jumping to another song.

#### Disable Multi-File Project

Clears the project folder.

#### Documentation

Opens the Multi-File Projects documentation.

### Open the Documentation

Opens the AbleSet documentation in your browser.

### Add AbleSet Plugin to Ableton

Opens the plugin installer to add the AbleSet plugin to Ableton Live

### Get AbleSet Controller Standard Pro

Shows the AbleSet Controller Max for Live device in Finder

### Show Global Custom Styles Standard Pro

Opens the folder containing your global Custom Styles file in Finder

### Open AbleSet Folder

Opens the AbleSet folder in your current project directory

### Change Hostname

Opens the the operating system's settings to where you can change your
computer's hostname.

### Preferred Network

Submenu to choose which network interface AbleSet uses.
Each interface is listed with its IP address.

### Version

Displays the installed AbleSet version.

### Check for Updates / Update to [version]

Checks for updates or installs the available update.

### Submit Feedback

Opens your email app with a new message to AbleSet support.

### Create Log Package

Creates a ZIP file of log files and debug information. Prompts whether to
include project files. You might be asked by support to create a log package
for troubleshooting.

### Quit

Quits AbleSet.
