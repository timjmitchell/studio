Source: https://ableset.com/docs/osc

# Controlling AbleSet via OSC

AbleSet Standard and Pro listens to OSC commands on port `39051`, so you can
remote-control it from any other app that supports OSC.

AbleSet announces its OSC server on the network using [Bonjour](https://developer.apple.com/bonjour/). Apps like
TouchOSC can find it automatically using the "Browse" function so you don't have
to enter the IP address and port manually.

If you're writing your own OSC client, you can use any Bonjour library to look
for `_osc._udp.` on the network. AbleSet's OSC server has a TXT value of
`server=ableset`, so in case there are other applications announcing their OSC
servers on the network as well, you can look for that value to find AbleSet.

## Available Commands

### Global

* `/global/play` starts playback
* `/global/pause` pauses playback
* `/global/stop` stops playback
* `/global/startPlaying` starts playback from the last cursor position
* `/global/continuePlaying` continues playing from the current playhead position
* `/global/playPause` toggles playback between play and pause
* `/global/playStop` toggles playback between play and stop
* `/global/startRecording` starts recording, and starts playback when Live isn't already playing
* `/global/stopRecording` stops recording, but doesn't stop playback
* `/global/toggleRecording` starts recording and playing, or stops recording
* `/global/reEnableAutomation` re-enables all disabled automation in Live
* `/global/backToArrangement` re-enables all arrangement clips in Live
* `/global/quantization [quantization]` sets the global quantization of your project
  + Allowed values: `8`, `4`, `2`, `1`, `1/2`, `1/2T`, `1/4`, `1/4T`, `1/8`, `1/8T`, `1/16`, `1/16T`, `1/32`, `none`
* `/global/tempo [tempo]` sets the tempo of your project, overriding any automation
* `/global/tempo/adjust [delta]` adjusts the tempo by the given number of BPM
  + The delta can be positive to increase the tempo or negative to decrease it
* `/global/tempo/reset` resets the tempo to the automation of your project

### Loop

* `/loop/enable` enables Live's loop bracket
* `/loop/escape` disables Live's loop bracket
  + if the current loop was enabled using the `+LOOP` flag, this will also jump
    to the next section
* `/loop/toggle` toggles Live's loop bracket

### Setlist

* `/setlist/jumpToTime [time]` jumps to the given time, in beats
* `/setlist/jumpToSong [number, name, or RANDOM]` jumps to the song at the given
  position in the setlist
  + `/setlist/jumpToSong 2` jumps to the 2nd song
  + `/setlist/jumpToSong -2` jumps to the 2nd-last song
  + `/setlist/jumpToSong SongTitle` jumps to the first song named "SongTitle"
  + `/setlist/jumpToSong RANDOM` jumps to a random song
* `/setlist/jumpBySongs [steps]` jumps by given number of songs
  + `/setlist/jumpBySongs 1` jumps to the next song, `/setlist/jumpBySongs -1`
    jumps to the previous one or to the beginning of the current song when the
    playhead isn't at the start of the song
  + Adding a `force=true` parameter when jumping back a song (e.g.
    `/setlist/jumpBySongs -1 force=true`) ignores the playhead's current
    position inside the song and always jumps to the previous song
* `/setlist/jumpToSection [number or name]` jumps to the section at the given
  position in the current song
  + `/setlist/jumpToSection 2` jumps to the 2nd section
  + `/setlist/jumpToSection -2` jumps to the 2nd-last section
  + `/setlist/jumpToSection Chorus` jumps to the first section named "Chorus"
  + `/setlist/jumpToSection Chorus true` jumps to the first section whose name
    includes the word "Chorus"
* `/setlist/jumpToQuickPlaySection [number]` jumps to the nth quick play section
  of the current song
  + `/setlist/jumpToQuickPlaySection 2` jumps to the 2nd quick play section
  + `/setlist/jumpToQuickPlaySection -2` jumps to the 2nd-last quick play section
* `/setlist/jumpBySections [number] [boolean]` jumps by a given number of sections
  + `/setlist/jumpBySections 1` jumps to the next section in the current song
  + By default, AbleSet prevents you from jumping beyond the bounds of the
    current song. To override this, set the 2nd argument to `true`. For example,
    `/setlist/jumpBySections 1 true` will jump to the first section of the next
    song when the playhead is positioned in the last section of the current song
  + Adding a `force=true` parameter when jumping back a section (e.g.
    `/setlist/jumpBySongs -1 force=true`) ignores the playhead's current
    position inside the section and always jumps to the previous one
* `/setlist/jumpByBeats [number] [boolean]` jumps forward or backward by a
  given number of beats
  + By default, AbleSet prevents you from jumping beyond the bounds of the
    current song. To override this, set the 2nd argument to `true`.
* `/setlist/jumpByBars [number] [boolean]` jumps forward or backward by a
  given number of bars
  + By default, AbleSet prevents you from jumping beyond the bounds of the
    current song. To override this, set the 2nd argument to `true`.
* `/setlist/jumpByMeasures [number] [boolean]` jumps forward or backward by a
  given number of measures, always snapping to the beginning of the measure
  + This requires a [Measure track](https://ableset.com/docs/measure-track) in your project, and
    only works while playback is stopped. For jumping while playing,
    use `/setlist/jumpByBars` instead.
  + By default, AbleSet prevents you from jumping beyond the bounds of the
    current song. To override this, set the 2nd argument to `true`.
  + When jumping back one measure while the playhead isn't at the beginning of a
    measure, AbleSet jumps to the beginning of the current measure first. To
    override this, add a `force=true` argument.
* `/setlist/jumpToQueued [boolean]` jumps to the queued song or section
  + if the first argument is `true`, AbleSet jumps instantly, without respecting
    Live's global quantization
* `/setlist/clearQueuedJump` clears the currently queued jump
* `/setlist/playCuedSong` plays the next song after the current song has
  finished
  + if autoplay is disabled, this will jump to the next song first, and start
    playback when it's called again
* `/setlist/go` is a command that does different things based on the current
  state of your set:
  + When stopped at the end of a song, jumps to the next song
  + When stopped at the beginning of a song, starts playback
  + When playing in a loop, escapes the loop
  + When playing while a song or section is queued, instantly jumps to it
* `/setlist/setLocatorsFromClips` places a locator at each section clip
* `/setlist/removeClipLocators` removes automatically placed locators at section
  clips
* `/setlist/load [string]` loads a saved setlist by its name
* `/setlist/removeSong [string]` removes a song from the setlist by its name
* `/setlist/toggleStop` toggles whether AbleSet should stop at the end of the
  current song
  + This only works for songs that end with a Ableton Locator IconSONG END locator

### Lyrics

* `/lyrics/jumpByLines [string] [integer]` jumps by the given number of lines
  + The first parameter is the slug of the lyrics track, the second defines the
    number of lines AbleSet should jump by.
  + `/lyrics/jumpByLines leo 2` jumps ahead two lyrics lines in the lyrics track
    called "Leo +LYRICS"
  + `/lyrics/jumpByLines backing-vox -2` jumps back two lyrics lines in the lyrics
    track called "Backing Vox +LYRICS"

### Mixer

For more information about track groups, see the [mixer documentation](https://ableset.com/docs/mixer).

* `/click/mute [boolean or toggle]` mutes or unmutes all click tracks
* `/click/solo [boolean or toggle]` soloes or unsoloes all click tracks
* `/mixer/[group name]/mute [boolean or toggle]` mutes or unmutes all
  tracks in the given track group
* `/mixer/[group name]/solo [boolean or toggle]` soloes or unsoloes all
  tracks in the given track group
* `/mixer/[group name]/volume [number]` sets the track group's volume
  + The volume can be between 0 and 1, with 0 being all group tracks at -Inf dB
    and 1 being all tracks at their maximum of 6dB
* `/mixer/[group name]/fadeTo [volume] [speed]` fades the given track group out
  + The volume can either be a number between 0 and 1, or "previous" if you want
    to undo the previous fade
  + The speed is an optional multiplier. By default (1), it takes 5 seconds to
    fade from -Inf to +6dB. Higher values are faster, lower values are slower.

### Cues

* `/cues/say [message] [voice]` generates the given message if needed and plays
  it through the [AbleSet Cues](https://ableset.com/docs/cues) plugin.

### Audio Interfaces

For more information about audio interfaces, see the [audio interfaces documentation](https://ableset.com/docs/audio-interfaces).

* `/audioInterfaces/setScene [1, 2, A, or B]` sets the active scene on the connected
  audio interfaces
  + `/audioInterfaces/setScene 1` sets the active scene to scene A
  + `/audioInterfaces/setScene B` sets the active scene to scene B
* `/audioInterfaces/toggleScene` toggles the active scene between A and B on the
  connected audio interfaces
* `/audioInterfaces/arm` arms the failover system of all audio interfaces
  + For iConnectivity devices, this enables the "Arm" mode
  + For DirectOut devices, this sets the port priority to Auto and resets all force settings

#### Commands for iConnectivity PlayAUDIO Devices

* `/audioInterfaces/playaudio/setScene [serial] [scene]` sets active scene of the device
  + `scene` can be either 1 or 2
* `/audioInterfaces/playaudio/setArmed [serial] [armed]` sets whether the failover system is armed
  + `armed` can be either 0 or 1

You can find the serial number of your PlayAUDIO devices in Auracle.

#### Commands for DirectOut EXBOX.MD Devices

* `/audioInterfaces/exbox/setPriority [host] [port] [priority]` sets the priority of a port on the given host
  + `priority` can be either `Inactive`, `Main`, `Backup`, or `Auto`
* `/audioInterfaces/exbox/setForce [host] [port] [force]` sets the priority of a port on the given host
  + `force` can be either `None`, `Main`, or `Backup`

For both commands, `host` is the hostname of your EXBOX.MD, and `port` can be
either `SFP`, `BNC`, `SC`, or `NET`. All values are case-sensitive.

#### Commands for DirectOut PRODIGY/ANDIAMO Devices

* `/audioInterfaces/prodigy/setPriority [host] [port] [priority]` sets the priority of a port on the given host
  + `priority` can be either Inactive, Main, Backup, or Auto
* `/audioInterfaces/prodigy/setForce [host] [port] [force]` sets the priority of a port on the given host
  + `force` can be either `None`, `Main`, `Backup`, or `Disaster Recovery`

For both commands, `host` is the hostname of your EXBOX.MD, and `port` can be
either `MADI 1`, `MADI 2`, `NET 1 A`, `NET 1 B`, `NET 2 A`, or `NET 2 B`.
All values are case-sensitive.

#### Commands for DAD Devices

* `/audioInterfaces/dad/setOverride [serial] [preset ID] [override ID]` overrides the active source set for a given preset
  + The override ID can be 1-4 for a source set or 0 to disable the override

### Floating Setlist Window

* `/floatingWindow [show|hide|toggle]` shows, hides, or toggles the floating setlist window

### Settings

You can find a list of all settings [here](https://ableset.com/docs/osc#settings-values). Boolean values can
be an actual boolean or `0` / `1`. You can also set them to `toggle` to toggle
the setting.

### AbleNet

To enable or disable AbleNet or the automatic drift correction, see settings OSC commands.

* `/ableNet/syncToRemote` brings this machine back in sync with others on the network
  if it's paused, see [AbleNet docs](https://ableset.com/docs/ablenet/#sync-playback-now)

### Device Control

You can use these OSC commands to control the AbleSet web app in the browser.
If you'd like a command to run on all devices, pass `all` as the first parameter.
Otherwise, set the first parameter to either the IP address or name of the
device you'd like to control. The device name is case-insensitive. Multiple
devices can be passed separated by commas.

Each device can have multiple names, separated by commas, which allows you to
tag devices. For example, my iPad on stage could be called "ipad-1, stage", and
my other iPad on stage could be called "ipad-2, stage". When I target "stage",
both iPads will receive the command.

* `/devices/showPage [devices] [page]` navigates to the given page
  + The page parameter corresponds to the path you see in the browser's URL bar
  + `/devices/showPage all performance` navigates to the performance page on all connected devices
  + `/devices/showPage leos-ipad lyrics/leo` opens the lyrics page for the lyrics track called Leo on the device called leos-ipad
  + `/devices/showPage 192.168.1.10 setlist` opens the setlist page on the device with the IP address 192.168.1.10
* `/devices/reload [devices]` reloads the current page on the browser
* `/devices/setSetting [devices] [setting] [value]` sets a device-specific setting
  + Settings can be viewed by going to Settings -> Debug -> Device Settings
  + `/devices/setSetting all performance.showSectionProgress true` enables the section progress bar on all devices
  + For boolean settings, you can send `toggle` instead of the value to toggle the setting
* `/devices/lock [devices]` locks the given device
* `/devices/unlock [devices]` unlocks the given device
* `/devices/toggleLock [devices]` toggles the lock on the given device
* `/devices/pressKey [devices] [key]` simulates a keypress on the given devices
  + This is experimental and doesn't cover all cases yet
  + Use [this website](https://keycode.info) to get the code of any pressed key
  + To add Shift or CMD/CTRL modifiers, prepend them to the key code
  + `/devices/pressKey all Shift+M` presses Shift + M, which toggles pinning in
    the lyrics view on all devices
* `/devices/showSections [devices] [boolean or toggle]` shows or hides the sections
  of the current song in the setlist
* `/devices/showAllSections [devices]` shows the sections of all songs in the setlist
* `/devices/hideAllSections [devices]` hides the sections of all songs in the setlist
* `/devices/setLineOverride [devices] [boolean or toggle]` enables or disables
  the line override function in lyrics
* `/devices/showSongAddDialog [devices]` shows the "Add a Song" dialog
* `/devices/showSongJumpDialog [devices]` shows the "Jump to Song" dialog
* `/devices/hideSongDialog [devices]` hides the current song dialog

### Notifications

These OSC commands display a notification on one or more devices. If you'd like
the notification to be displayed on all devices, pass `all` as the first parameter.
Otherwise, set the first parameter to either the IP address or host name of the
device you'd like to control. The host name is case-insensitive. Multiple devices
can be passed separated by commas.

* `/notify/toast [devices] [title] [description] [duration]` displays a toast notification on all browsers
  + Description and duration are both optional parameters
  + The toast duration is specified in milliseconds
* `/notify/big [devices] [message] [duration] [color]` displays a message that fills the entire screen on all browsers
  + Duration can be omitted and will default to 5000 ms
  + The message duration is specified in milliseconds, but users can also hide it by tapping on it
  + The color can be any of the [supported colors](https://ableset.com/docs/locator-notation/#colors) in AbleSet
  + The message can contain simple markdown for bold, italic, and underlined text
* `/notify/cue [devices] [duration] [color]` displays a colored cue light along the edge of the screen
  + The cue duration is specified in milliseconds
  + The color can be any of the [supported colors](https://ableset.com/docs/locator-notation/#colors) in AbleSet

You can also clear notifications:

* `/notify/big/clear [devices]` clears a big notification
* `/notify/cue/clear [devices]` clears a cue light

### Sending MIDI

AbleSet can send MIDI data to any output port using OSC. You can use these
commands to send notes:

* `/midi/send/note [output] [channel] [note] [velocity] [duration]` sends a note on followed by a note off to the specified output
  + Velocity is optional, the default value is 127
  + Duration is specified in milliseconds, the default value is 100
* `/midi/send/noteOn [output] [channel] [note] [velocity]` sends a note on with the given velocity to the specified output
  + Velocity is optional, the default value is 127
* `/midi/send/noteOff [output] [channel] [note] [velocity]` sends a note off with the given velocity to the specified output
  + Velocity is optional, the default value is 0

The note can either be a number between 0 and 127, or a string like `E#0` or `Cb-1`.

To send CC and PC, you can use these commands:

* `/midi/send/cc [output] [channel] [controller] [value]` sends a CC to the given output
  + Controller and value must both be numbers between 0 and 127
* `/midi/send/pc [output] [channel] [program]` sends a PC to the given output
  + Program must be between 0 and 127

You can also send raw MIDI data to any output, for example for SysEx:

* `/midi/send/raw [output] [data]`
  + Data can either be a list of numbers, or a string like `F0 03 A3 F7`

### Shared Variables

AbleSet allows you to set shared variables which are accessible from all devices
and optionally persisted across restarts. This is especially useful for setting
state via [MIDI mapping](https://ableset.com/docs/midi-mapping) or in [canvases](https://ableset.com/docs/canvas).

To set a shared variable, send an OSC command to `/shared/[variable name]` with
its value or values. For example:

* `/shared/controlsEnabled true` sets the `controlsEnabled` variable to `true`
* `/shared/items 1 2` sets the shared `items` variable to an array of `[1, 2]`

Variable names can contain slashes as well:

* `/shared/canvas/color blue` sets the `canvas/color` variable to `blue`

## Control Flow Statements

When writing OSC commands in AbleSet's [MIDI mapping](https://ableset.com/docs/midi-mapping) and
[Canvas](https://ableset.com/docs/canvas), you can use control flow statements to delay or skip
the next commands. Here's a list of all available control flow statements:

* `//sleep [duration]` sleeps for the given duration in milliseconds before running the next commands
* `//awaitJump` waits for Live to jump to the queued section before running the next commands
* `//awaitFileLoad` waits for Live to load the project file before running the next commands
* `//if [condition]` only runs the next commands if the condition is met
  + Currently, the condition can be either `playing`, `recording`, or `looping`
  + You can negate a condition by adding a `!` at the beginning, e.g. `!playing`
  + If the condition isn't met, all following commands are skipped until an `//endif` or another `//if` statement
  + You can't combine multiple conditions at this time
  + To make the command a bit easier to read, you can use a colon (`//if playing:`)
    instead of a semicolon (`//if playing;`) to delimit it from the next command
  + Example: `//if !playing: /setlist/jumpBySections 1` only jumps to the next
    section if Live isn't currently playing

## AbleNet Parameters

If you're using OSC commands in a setup with multiple computers connected via
[AbleNet](https://ableset.com/docs/ablenet), AbleSet automatically forwards commands to all other
connected computers. For additional redundancy, you should send the same command
to all computers.

For this to work well, each command you send to AbleSet via OSC should have its own
UUID. You can append it as a string parameter to any OSC command, for example
`uuid=1234abcd` where "1234abcd" is a random string for each command.

When AbleSet receives multiple commands with the same UUID, it will only execute the
first one and discard all others.

If you don't want AbleSet to forward OSC commands, you can add the string `ableNet=false`
to any OSC command that you send to AbleSet. In that case, the UUID parameter isn't necessary.

## Receiving Updates from AbleSet

AbleSet can send updates on its current state to other OSC clients. This can be
used to update the state of your control surfaces in real time.

To register your OSC clients with AbleSet, send the `/subscribe` command with
the IP address and port, and optionally a name – e.g.:

```
/subscribe 127.0.0.1 8000 TouchOSC
```

If you set the IP address to `auto` or omit the parameter, AbleSet will use the
IP address the request came from to register the OSC client, e.g.:

```
/subscribe 8000 TouchOSC
```

or

```
/subscribe auto 8000 TouchOSC
```

This is useful for setups where you don't always know your IP address, like
using TouchOSC on a machine that gets a new IP every time it connects to the
network.

To receive fine value updates, e.g. for the playhead position or song/section
progress, add an additional argument to the call:

```
/subscribe 8000 TouchOSC true
```

Please note that these fine updates are sent up to 100 times per second and
might be taxing on low-end devices receiving them. If you'd like to throttle the
frequency of fine updates, you can send a number instead of a boolean that
specifies the frequency in milliseconds:

```
/subscribe 8000 TouchOSC 250
```

You can update this frequency by subscribing again with a different value.

After subscribing, you'll see a notification that the device has been connected,
and from this point on, AbleSet will send updates for all events to your client.
You can register multiple clients with AbleSet if you want to connect multiple
control surfaces. To unsubscribe from events, send `/unsubscribe` to AbleSet.

If you'd only like to receive updates for specific values, you can add those to
the `/subscribe` command as well:

```
/subscribe 8000 TouchOSC true /global/isPlaying /setlist/activeSongName
```

This reduces the network traffic and is especially useful for OSC clients that
can't handle a lot of messages at once.

The value filter supports excludes and wildcards using the [glob syntax](https://github.com/micromatch/picomatch?tab=readme-ov-file#basic-globbing). For
example, `/mixer/*/volume` would include `/mixer/click/volume`,
`/mixer/bass/volume`, etc. while `/mixer/**` would include all values starting
with `/mixer`.

To exclude values from updates, prepend an exclamation mark to the filter, e.g.
`!/setlist/**` to exclude all updates from values starting with `/setlist`.

These filters can be combined so you can tune the updates to your liking.

In addition to value events, AbleSet will send a `/heartbeat` every 2 seconds.
You can use this to check if the connection is still up. If you'd like to
trigger a heartbeat yourself, you can send a `/getHeartbeat` command to AbleSet.

### Requesting Values

To get the current state of all values, send `/getValues` to AbleSet. If you've
already subscribed to value updates, this sends results to the same port as
these updates.

```
/getValues 8000
```

You can override this by providing a port or a host and a port:

```
/getValues 127.0.0.1 8000
```

If you've set up a filter when subscribing, you only get the values that are
included in this filter. You can override this by adding the addresses of values
you'd like to receive to the command:

```
/getValues /global/* /setlist/activeSongName
```

You can find a list of all values that get sent to registered clients
[below](https://ableset.com/docs/osc#available-osc-values).

### Customizing the OSC Client in AbleSet

AbleSet lists all connected OSC clients on its Devices page. You can modify the
way your client is displayed using these two OSC commands:

```
/setStatus "My custom status"
```

```
/setWebLink "http://example.local/link"
```

If you'd like to override the host or port of these commands, you can do so
by adding them to the beginning of the arguments, just like you would with
`/getValues`:

```
/setStatus 8000 "My status"
/setStatus 127.0.0.1 8000 "My status"
```

## Available OSC Values

These values are available via OSC, in scripts, and in Canvas. To see a live
list of all values, go to Settings -> OSC Settings -> View All OSC Values.

### Global

* `/global/isConnected [0|1]` whether AbleSet is connected to Live
* `/global/isLoadingFile [0|1]` whether Live is loading a new song file
* `/global/projectName [string]` the name of the current project file
* `/global/loadingProjectName [string]` the name of the project file that is
  currently being loaded
* `/global/beatsPosition [float]` the current position in beats, floored to
  whole numbers while Live is playing
* `/global/finePosition [float]` the current position
  + Requires the `fine` flag to be set when subscribing to updates
* `/global/humanPosition [float] [float]` the current position in bars and beats
* `/global/currentMeasure [string] [float] [float]` the current measure from a
  measure track, if available, along with the current beat and the total number
  of beats in the current measure
  + This requires a [Measure track](https://ableset.com/docs/measure-track) in your project
* `/global/tempo [float]` the current tempo
* `/global/isPlaying [0|1]` whether Live is currently playing
* `/global/isRecording [0|1]` whether Live is currently recording
* `/global/isPaused [0|1]` whether Live is currently paused
* `/global/isAtPauseLocator [0|1]` whether Live is currently paused at
  a +PAUSE locator
* `/global/timeSignature [integer] [integer]` the time signature
* `/global/quantization [quantization]` the global quantization of your project
  + Possible values: `8`, `4`, `2`, `1`, `1/2`, `1/2T`, `1/4`, `1/4T`, `1/8`, `1/8T`, `1/16`, `1/16T`, `1/32`, `none`
* `/global/canReEnableAutomation` whether any automation in Live is currently disabled
* `/global/canGoBackToArrangement` whether any arrangement clips are currently
  overridden by session clips
* `/global/metronome [integer] [integer]` the current metronome pattern, either
  from a [Measure track](https://ableset.com/docs/measure-track), or from the project file
* `/global/measureOrPosition [string] [integer]` the current measure and beat
* `/global/cpuAverage` Live's average CPU usage
* `/global/cpuPeak` Live's peak CPU usage
* `/global/isSyncingToRemoteTick` whether AbleSet is currently syncing to another
  computer on the network via AbleNet

### Setlist

* `/setlist/name [string]` the setlist name
* `/setlist/songs [...string]` a list of all song names in the setlist
* `/setlist/songCount [float]` the number of songs in the setlist
* `/setlist/songColors [...string]` a list of all songs' colors in the setlist
* `/setlist/songDurations [...float]` a list of all songs' durations in the
  setlist in seconds
* `/setlist/songDescriptions [...string]` a list of all songs' descriptions in
  the setlist
* `/setlist/songTempos [...float]` a list of all songs' tempos in the setlist
* `/setlist/files [...string]` a list of all saved setlist file names
* `/setlist/sections [...string]` a list of all sections of the current song
* `/setlist/sectionCount [float]` the number of sections in the current song
* `/setlist/quickPlaySections [...string]` a list of all quick play sections of
  the current song
* `/setlist/quickPlaySectionCount [float]` the number of quick play sections in
  the current song
* `/setlist/sectionDescriptions [...string]` a list of all section descriptions
  of the current song
* `/setlist/sectionColors [...string]` a list of all sections' colors of the
  current song
* `/setlist/activeSongName [string]` the name of the current song
* `/setlist/activeSongDescription [string]` the description of the current song
* `/setlist/activeSongStopDescription [string]` the stop description of the current song
* `/setlist/activeSongTags [...string]` the tags of the current song
* `/setlist/activeSongIndex [float]` the index of the current song in the setlist
* `/setlist/activeSongStart [float]` the song's start position in beats
* `/setlist/activeSongEnd [float]` the song's end position in beats
* `/setlist/activeSongDuration [float]` the song's duration in seconds
* `/setlist/activeSongColor [string] [string]` the color of the song, as a color
  name and as a hex string
* `/setlist/activeSongProgress [float]` the song's progress from 0 to 1
  + Requires the `fine` flag to be set when subscribing to updates
* `/setlist/activeSongStopDescription [string]` the song's stop description
* `/setlist/activeSectionName [string]` the name of the current section
* `/setlist/activeSectionDescription [string]` the description of the current section
* `/setlist/activeSectionIndex [float]` the index of the current section in the
  current song
* `/setlist/activeSectionStart [float]` the section's start position in beats
* `/setlist/activeSectionEnd [float]` the section's end position in beats
* `/setlist/activeSectionColor [string] [string]` the color of the section, as a
  color name and as a hex string
* `/setlist/activeSectionLoopMode [loop|loopfull]` the section's loop mode
* `/setlist/activeSectionLoopCount [integer]` the pre-defined number of loops
* `/setlist/activeSectionDuration [float]` the section's duration in seconds
* `/setlist/activeSectionProgress [float]` the section's progress from 0 to 1
  + Requires the `fine` flag to be set when subscribing to updates
* `/setlist/nextSectionName [string]` the name of the next section
* `/setlist/nextSectionDescription [string]` the description of the next section
* `/setlist/nextSectionIndex [float]` the index of the next section in the
  current song
* `/setlist/nextSectionStart [float]` the next section's start position in beats
* `/setlist/nextSectionEnd [float]` the next section's end position in beats
* `/setlist/nextSectionColor [string] [string]` the color of the next section,
  as a color name and as a hex string
* `/setlist/nextSectionDuration [float]` the next section's duration in seconds
* `/setlist/queuedName [string] [string]` the name of the queued song and
  section
* `/setlist/queuedIndex [float] [float]` the index of the queued song and
  section
* `/setlist/queuedType [string]` the type of the queued jump – `song` or
  `section`
* `/setlist/isJumpingToQueued [0|1]` whether AbleSet is currently jumping to
  the queued song or section
* `/setlist/songCountdownMs [float]` the remaining song countdown in
  milliseconds, if a countdown is active
* `/setlist/nextSongName [string]` the next song's name
* `/setlist/nextSongDescription [string]` the next song's description
* `/setlist/nextSongStopDescription [string]` the next song's stop description
* `/setlist/nextSongTags [...string]` the next song's tags
* `/setlist/nextSongIndex [float]` the next song's index
* `/setlist/nextSongDuration [float]` the next song's duration in seconds
* `/setlist/nextSongColor [string] [string]` the color of the next song, as a
  color name and as a hex string
* `/setlist/loopEnabled [0|1]` whether the loop bracket is enabled
* `/setlist/loopStart [float]` the loop's start position in beats
* `/setlist/loopEnd [float]` the loop's end position in beats
* `/setlist/loopCounter [integer]` the current number of repetitions in the loop
* `/setlist/isInActiveSectionLoop [0|1]` whether the playhead is currently in an
  active section loop
* `/setlist/isCountingIn [0|1]` whether AbleSet is currently counting in
* `/setlist/remainingTimeInSong [float]` remaining time in the current song, in seconds
* `/setlist/remainingTimeInSet [float]` remaining time in the set, in seconds

### Lyrics

* `/lyrics/[slug]/previous` the previous lyrics line's text
* `/lyrics/[slug]/current` the current lyrics line's text
* `/lyrics/[slug]/next` the next lyrics line's text

### Mixer

* `/mixer/names [...string]` a list of all track group names in the mixer
* `/mixer/[group name]/muted` whether the track group is currently muted
* `/mixer/[group name]/soloed` whether the track group is currently soloed
* `/mixer/[group name]/volume` the track group's current volume between 0 and 1
* `/mixer/[group name]/isFading` whether the track group is currently fading in or out
* `/mixer/[group name]/meter` the current level of the group's meter, between
  0 and 1 with 0.125 precision

### Cues

* `/cues/generating [integer]` the number of cues that are currently being
  generated
* `/cues/[slug]/name [string]` the name of the [AbleSet Cues](https://ableset.com/docs/cues) output
  with the given slug
* `/cues/[slug]/id [string]` the ID of the AbleSet Cues output
* `/cues/[slug]/phrase [string]` the phrase currently being spoken

### Shared Variables

When you set a shared variable via OSC or scripting, that variable is forwarded
to all subscribed OSC clients with a `/shared` prefix.

### Audio Interfaces

* `/audioInterfaces/connected [0|1]` whether an audio interface is connected
* `/audioInterfaces/count [integer]` the number of connected audio interfaces
* `/audioInterfaces/all/scene [1|2]` the current scene – `1` for the main and `2`
  for the backup computer
* `/audioInterfaces/names [...string]` the names of all connected audio interfaces
* `/audioInterfaces/scenes [...1|2]` the interfaces' current scenes – `1` for the
  main and `2` for the backup computer
* `/audioInterfaces/status [...string]` the status of each connected audio interface
  + Can be `armed`, `sceneA`, `sceneB`, or `alarm`

#### Updates for iConnectivity PlayAUDIO Devices

* `/audioInterfaces/playaudio/[serial]/scene` the active scene – `1` for the
  main and `2` for the backup computer
* `/audioInterfaces/playaudio/[serial]/armed` whether the failover system is
  armed to automatically switch – can be `0` or `1`
* `/audioInterfaces/playaudio/[serial]/alarm` whether the failover system is
  currently in alarm mode
* `/audioInterfaces/playaudio/serial/main/signal` the signal state of the main input
* `/audioInterfaces/playaudio/serial/backup/signal` the signal state of the backup input

Signal values are as follows:

* `0`: Not connected
* `1`: Connected
* `2`: Sending audio
* `3`: Sending audio & sine

#### Updates for DirectOut EXBOX.MD Devices

* `/audioInterfaces/exbox/[host]/[port]/backupPort` the selected backup port
* `/audioInterfaces/exbox/[host]/[port]/priority` the selected port priority
  + Can be either `Inactive`, `Main`, `Backup`, or `Auto`. If the priority is
    `Inactive`, EARS for this port is disabled
* `/audioInterfaces/exbox/[host]/[port]/force` the forced port
  + Can be either `None`, `Main`, or `Backup`
* `/audioInterfaces/exbox/[host]/[port]/active` the port that is currently active
  + Can be either `Main` or `Backup`
* `/audioInterfaces/exbox/[host]/[port]/signal` the kind of signal received on the port
  + Can be either `BLDS`, `Pilot`, or `None`

The `host` is your EXBOX's hostname on the network. The `port` can be `SFP`, `BNC`,
`SC`, or `NET`. For `signal`, the `NET` port is split into `NET1` and `NET2`.

#### Updates for DirectOut PRODIGY/ANDIAMO Devices

* `/audioInterfaces/prodigy/[host]/[port]/backupPort` the selected backup port
* `/audioInterfaces/prodigy/[host]/[port]/priority` the selected port priority
  + Can be either `Inactive`, `Main`, `Backup`, or `Auto`. If the priority is
    `Inactive`, EARS for this port is disabled
* `/audioInterfaces/prodigy/[host]/[port]/force` the forced port
  + Can be either `None`, `Main`, `Backup`, or `Disaster Recovery`
* `/audioInterfaces/prodigy/[host]/[port]/active` the port that is currently active
  + Can be either `Main`, `Backup`, or `Disaster Recovery`
* `/audioInterfaces/prodigy/[host]/[port]/signal` the kind of signal received on the port
  + Can be either `BLDS`, `Pilot`, or `None`

For all updates, `host` is the hostname of your PRODIGY or ANDIAMO, and `port`
can be either `MADI 1`, `MADI 2`, `NET 1 A`, `NET 1 B`, `NET 2 A`, or `NET 2 B`.
All values are case-sensitive.

#### Updates for DAD Devices

* `/audioInterfaces/dad/[serial]/[preset ID]/name` the name of the preset
* `/audioInterfaces/dad/[serial]/[preset ID]/activeSourceSet` the currently active source set
  + If this is 0, no source set is selected
* `/audioInterfaces/dad/[serial]/[preset ID]/sourceSetOverride` the source set override
  + If this is 0, the source set override is disabled
* `/audioInterfaces/dad/[serial]/[preset ID]/sourceSets/[set ID]/name` the source set's name
* `/audioInterfaces/dad/[serial]/[preset ID]/sourceSets/[set ID]/triggers/[trigger ID]/signal` the signal state of a trigger's input

### Devices

* `/devices/names [...string]` a list of all available device names

These per-device values are only sent for devices that have a unique name. If two
or more devices share the same name, their statuses won't be available under that
shared name.

* `/devices/[name]/connected` whether this browser is currently connected
* `/devices/[name]/names` a list of all names for this browser
* `/devices/[name]/cueLight` the color of the current cue light
* `/devices/[name]/bigNotification` the current big notification
* `/devices/[name]/isLocked` whether the browser is currently locked
* `/devices/[name]/isLockButtonHidden` whether the lock button is currently hidden
* `/devices/[name]/isNavigationLocked` whether navigation is locked on the browser
* `/devices/[name]/page/path` the path of the current page for this browser
* `/devices/[name]/page/title` the title of the current page for this browser
* `/devices/[name]/battery/percentage [float]` the device's battery level from 0
  to 100, requires [AbleSet Connect](https://ableset.com/docs/connect)
* `/devices/[name]/battery/isOnCharger [0|1]` whether the device is currently
  charging, requires [AbleSet Connect](https://ableset.com/docs/connect)
* `/devices/[name]/screenBrightness [float]` the device's screen brightness from
  0 to 1, requires [AbleSet Connect](https://ableset.com/docs/connect)
* `/devices/[name]/latencyMs` the latency to this browser in milliseconds
* `/devices/[name]/lastPing` the timestamp of the last ping in milliseconds

### MIDI

* `/midi/outputs` a list of all available MIDI outputs

### Computer

* `/computer/onBattery [0|1]` whether the computer running AbleSet is currently
  running on battery power

### Oaktone Controllers

* `/oaktoneControllers/isConnected [0|1]` whether an Oaktone controller is
  connected
* `/oaktoneControllers/count [integer]` the number of connected Oaktone
  controllers

### Settings Values

These values reflect the current app settings. You can change many of them by
sending OSC commands – see the **Settings** section in the command list above.
Boolean values are sent as `0` or `1`.

#### AbleNet

* `/settings/ableNet [0|1]` whether AbleNet is enabled
* `/settings/ableNetDriftCorrection [0|1]` whether automatic drift correction is
  enabled
* `/settings/ableNetCustomAddresses [...string]` a list of custom AbleNet peer
  addresses
* `/settings/connectedInterfaceScene [A|B]` the scene of the connected audio
  interface
* `/settings/preferredNetwork [string]` the preferred network interface for
  AbleNet, e.g. `en0`

#### Playback & Setlist

* `/settings/autoplay [0|1]` whether autoplay is enabled
* `/settings/autoJumpToNextSong [0|1]` whether AbleSet automatically jumps to the
  next song at the end of a song
* `/settings/alwaysStopOnSongEnd [0|1]` whether AbleSet stops playback at the end
  of all songs
* `/settings/alwaysPlayQueuedSongs [0|1]` whether queued songs are played
  automatically
* `/settings/allowJumpBackToBeginning [0|1]` whether AbleSet jumps to the
  beginning of the current song before jumping to the previous song
* `/settings/autoReEnableAutomationOnSongJump [0|1]` whether automation is
  re-enabled when jumping to a new song
* `/settings/autoBackToArrangementOnSongJump [0|1]` whether arrangement view is
  restored when jumping to a new song
* `/settings/disableLoopWhenJumping [0|1]` whether the loop bracket is disabled
  when jumping to another song or section
* `/settings/removePlayedSongs [0|1]` whether played songs are removed from the
  setlist automatically
* `/settings/jumpMode [string]` the jump mode – `quantized`, `end-of-section`,
  `end-of-song`, `dynamic`, or `manual`
* `/settings/songJumpDelay [string]` the delay before jumping to a new song, in
  milliseconds
* `/settings/safeMode [0|1]` whether Safe Mode is enabled
* `/settings/projectsFolder [string]` the folder used for multi-file project files
* `/settings/saveProjectOnSwitch [0|1]` whether the project is saved when
  loading a new project file in multi-file projects
* `/settings/countIn [0|1]` whether count-in is enabled
* `/settings/countInSoloClick [0|1]` whether the click track is soloed during
  count-in
* `/settings/countInDuration [1|2|4]` the count-in duration in bars
* `/settings/displayLtc [0|1]` whether LTC is displayed

#### Speech & Cues

* `/settings/autoSpeakSongs [0|1]` whether song names are spoken automatically
* `/settings/autoSpeakSongDescriptions [0|1]` whether song descriptions are
  spoken automatically
* `/settings/autoSpeakStopDescriptions [0|1]` whether stop descriptions are
  spoken automatically
* `/settings/autoSpeakSections [0|1]` whether section names are spoken
  automatically
* `/settings/autoSpeakSectionDescriptions [0|1]` whether section descriptions
  are spoken automatically
* `/settings/autoSpeakSectionCountIns [0|1]` whether section count-ins are spoken
  automatically
* `/settings/autoSpeakLoopCountIns [0|1]` whether loop count-ins are spoken
  automatically
* `/settings/speakLongSectionCountIn [0|1]` whether section count-ins should be
  two bars long
* `/settings/speakSectionOnSecondBar [0|1]` whether the section name is spoken
  on the second bar of a two-bar count-in
* `/settings/speakCountInNumbers [0|1]` whether count-in numbers are spoken
* `/settings/cuesDefaultVoiceModel [string]` the default voice model for
  generated cues

#### Mixer

* `/settings/mixerIncludeMainTrack [0|1]` whether the main track is included in
  the mixer
* `/settings/mixerTransferGroupStates [0|1]` whether mute and solo states are
  transferred between track groups when switching songs
* `/settings/mixerTransferGroupVolumes [0|1]` whether volumes are transferred
  between track groups when switching songs

#### UI & Windows

* `/settings/showStopButton [0|1]` whether AbleSet stops by default instead of pausing
* `/settings/show24HourClock [0|1]` whether the clock uses 24-hour format
* `/settings/defaultView [string]` the default view path, e.g. `/lyrics`
* `/settings/showInDock [0|1]` whether AbleSet is shown in the Dock
* `/settings/openAbleSetInFloatingWindow [0|1]` whether AbleSet opens in a
  floating window
* `/settings/openAbleSetOnStart [0|1]` whether AbleSet opens automatically on
  start
* `/settings/autoOpenLastProjectFile [0|1]` whether the last project file is
  opened automatically

#### App & Hardware

* `/settings/warnOnBattery [0|1]` whether AbleSet warns when running on battery
  power
* `/settings/disarmAudioInterfacesWhileLoadingProject [0|1]` whether audio
  interfaces are disarmed while loading a project
* `/settings/persistSharedVariables [0|1]` whether shared variables are
  persisted across restarts

### Network

* `/network/ip` the IP of the computer running AbleSet
* `/network/host` the hostname of the computer running AbleSet

### Versions

* `/version/app` the version of AbleSet
* `/version/live` the version of Ableton Live
* `/version/plugin` the version of the AbleSet plugin
