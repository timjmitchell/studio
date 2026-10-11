Source: https://help.uaudio.com/hc/en-us/articles/25357506048020-Console-Sessions
Updated: 2026-03-03T18:00:04Z

# Console Sessions

The Sessions controls provide methods for managing complete UAD Console configurations as session preset files.

**Note:** Monitor settings and hardware settings are global parameters that are not saved in UAD Console session files.

# Content of Session Files

UAD Console session files contain most, but not all, UAD Console settings. The specific parameters saved and not saved are listed below:

## Items saved in the session file

* **Plug-in data:** All inserted UAD plug-ins and the specific settings contained within them.
* **Controls:** All knob, slider, and menu values.
* **Interface customization:** Input labels and channel show/hide status.
* **Console settings:** Settings in the UAD Console Settings window, excluding global parameters.

## Items not saved in the session file

* **Hardware gains:** All Monitor Gain and Line Input Gain.
* **Signal levels and routing:** Line Output Reference Levels, Monitor Outputs Digital Mirror, and Cue Outputs.
* **Clocking and rate:** Clock Source and Sample Rate.
* **Global configuration:** I/O Matrix settings.

**Note:** Items that are not saved are global parameters managed in the UAD Console Settings window; they remain constant across different sessions rather than being session-specific.

**Tip:** Core Audio / ASIO settings can be saved separately in the I/O Matrix.

# Session Files Location

By default, session files are saved to, and loaded from, the user's home folder at:

* Mac: Users/UserName/Documents/Universal Audio/Sessions/
* Windows: C:\Users\[UserName]\AppData\Roaming\Universal Audio\Sessions

Although session files can be saved to (and loaded from) any location on disk, using the default location is the most convenient, because UAD Console always uses this location for the Session Browser and any Open/Save dialogs presented by the OS.

**Note:** Session files must reside in the default location to appear in session lists within UAD Console.

# Session Sub-Folders

The Sessions folder can contain one level of sub-folders for additional session organization capability. The contents of sub-folders (if any) are displayed in blue text, with a disclosure triangle that you can click to expand or close each sub-folder.

# Session Files Suffix

UAD Console's session files have the ".uadmix" suffix for Apollo, and the ".volt876" prefix for Volt 876 sessions. The suffix is added to session files automatically when saving to disk; however, the suffix is not displayed in the file save dialog (the suffix should not be manually typed when saving a session file).

**Note:** Without the suffix, the session files will not be visible in the "Open" file dialogs or the Session Browser, and they won't be opened when they are double-clicked in the OS file system.

# Session Files Access

Session files can be saved and loaded via several methods: the [Session Browser](#h_01HTS1V6Z851SKREFWTQSTHTP4), the [Modified Session Dialog](#h_01HTS1V6Z85Y7EP00S2C5Q1YH7), the [Sessions menu](#h_01HTS1V6Z8GPRT5E573BX3J5BK), and the File menu.

# Session Name

![session-name.png](https://help.uaudio.com/hc/article_attachments/46835318634132)

Session names are displayed in the Meter Bridge, in device tabs at the top of the main UAD Console window ("live-session-ii" in the screenshot above), below the word SESSIONS above the Mixer Navigation panel, and at the top of the Session Browser. Session names are created when the file is saved; they can also be renamed via the OS file system.

# Modified Session Name

![sesssion-name-edited.png](https://help.uaudio.com/hc/article_attachments/46835318638612)

When any UAD Console setting is changed after the session is saved, an asterisk (\*) appears after the session name. This is a convenient visual reminder that the session is modified and may need to be saved for future use. To clear the asterisk, save the session or create a new session.

# SYNC Session Name

![session-name-sync-session.png](https://help.uaudio.com/hc/article_attachments/46835318642324)

When a DAW project containing the UAD Console Recall plug-in is opened that has the SYNC function in the plug-in enabled, the session name changes to "- Sync Session -" indicating that the DAW has sent session settings to UAD Console. For complete Sync details, see [SYNC](https://help.uaudio.com/hc/en-us/articles/26489269396116#h_01HXHYD7277MFKPPCBS3NRJQDB).

# Modified Session Dialog

![](https://help.uaudio.com/hc/article_attachments/25357506041492)

If the current UAD Console session has been modified and a new UAD Console session is loaded, a dialog displaying the current session name in quotes appears with options (note that the session name idoes not appear if the session has never been saved). The behavior of the options in this dialog are detailed below.

**Important:** This dialog does not appear when a UAD Console session is loaded via the UAD Console Recall plug-in's SYNC function. For complete Sync details, see [SYNC](https://help.uaudio.com/hc/en-us/articles/26489269396116#h_01HXHYD7277MFKPPCBS3NRJQDB).

**Don't Save:** All modifications to the current UAD Console session are discarded and the session is loaded (or created, if new session).

**Cancel:** The current UAD Console session remains active and the attempt to load the UAD Console session file is canceled.

**Save:** The current session is saved to disk and the session is loaded. If the session has never been saved to disk, this switch displays "Save As..." which opens the file save dialog.

# Session Browser

The Session Browser opens to the left of the UAD Console screen. The Browser provides methods for managing UAD Console configurations as session preset files. When a UAD Console session file is saved, the current UAD Console configuration is written to disk.

When a session file is subsequently reloaded, UAD Console is returned to the same configuration state, regardless of any changes to UAD Console that were made in the interim.

![](https://help.uaudio.com/hc/article_attachments/25357506041748)

*The Session Browser*

## Session Browser Access

![session-browser-open.png](https://help.uaudio.com/hc/article_attachments/27432191172756)

*Click to open the Session Browser*

To access the Sessions Browser, single-click the area at the top of the Mixer Navigation section.

**Note:** Mixer Navigation (View > Section > Mixer Navigation) must be shown to access the Session Browser.

## Sessions Folder Contents

The contents of the session folder include the list of saved sessions and any sub-folders.

* **Session List:** All items within the default Sessions file folder are displayed in the Session list. If more sessions or folders reside in the column than are currently within view, a scroll bar appears. Double-click any session to load it, or click the disclosure triangle to the left of a sub-folder (if any) to display sessions within the sub-folder.Note that sub-folders are indicated in the Session List with small disclosure triangles near the left side of the Session List.
* **Sub-Folders:** If the Session Browser contains one or more folders, expanding a folder by clicking the disclosure triangle displays its contents in the list.

![](https://help.uaudio.com/hc/article_attachments/25357495213332)

*Sessions folder contents shown in macOS Finder*

## Session Browser Function Switches

The Session Browser contains switches that perform file management tasks. Click a switch to perform the operation on the currently selected preset or sub-folder.

### New

Creates a new UAD Console session with default settings (default settings cannot be changed). If the current session has been modified, a dialog appears allowing you to save it first.

### Open...

Opens the operating system's standard "Open File" dialog for loading existing session files from disk.

**Tip:** Session files can also be opened by double-clicking .uadmix files from within the operating system's file system.

### Save

Opens the Save Session dialog, in which you can save the file, or the current modified preset file in place. If the preset was not previously saved (if the file doesn't exist), or if you type a new name for the file, the Save button changes to Save As.

![](https://help.uaudio.com/hc/article_attachments/25357495213972)

### Save As

This option appears when you type a new name for the session, after clicking Save.

![](https://help.uaudio.com/hc/article_attachments/25357495214996)

**Important:** Session settings will not be properly saved if the "/" (forward slash) or "?" (question mark) characters are in the filename. Avoid these and other special characters when saving session files.

# Sessions Menu

The Sessions Menu provides quick access to Session management functions without opening the Sessions Browser. Click any item in the menu to perform the function.

Items in the menu are divided into three sections. File management options are in the top section, existing session files and folders that reside on disk are listed in the center section, and cached (overwritten) sessions are listed in the bottom section.

## Open Sessions Menu

To access the Sessions menu, right-click or Control-click the Sessions area located at the top of the Mixer Navigation area. When the menu is displayed, clicking an item in the menu chooses that item.

![](https://help.uaudio.com/hc/article_attachments/25357495215508)

*Display the Sessions Menu*

![](https://help.uaudio.com/hc/article_attachments/25357506046100)

*The Sessions Menu*

## Sessions Menu File Functions

The New, Open, Save, and Save As functions in the Sessions menu have the same functionality as the [Session Browser function switches](#h_01HTS1V6Z85S28EFXSSQDHWRFT).

## Sessions List

Existing session files that reside in the Default Session Files Location are displayed in the center section of the Sessions menu. (Session names in the diagram are examples only.)

Select a session from the list to load the session file. If the current session has been modified, the Modified Session Dialog appears.

**Note:** Session files must reside in the default session files location and have the .uadmix suffix to be visible in the Sessions menu.

## Sub-Folders

Sub-folder names in the Sessions menu are displayed in blue. Session files within the sub-folder are displayed beneath the blue sub-folder name (session files not within sub-folders appear at the top of the sessions list).

## Cached Sessions

Cached sessions appear in the bottom section of the Sessions menu. Cached sessions are session files that aren't saved on disk. Instead, these sessions are automatically created and stored in a temporary cache.

### Why Cached Sessions Exist

When a DAW project containing the UAD Console Recall plug-in is opened and the plug-in's SYNC function is enabled, the UAD Console settings contained in the DAW project overwrite the current UAD Console settings. The cached sessions are used to recover the overwritten data if desired. For complete Sync details, see [SYNC](https://help.uaudio.com/hc/en-us/articles/26489269396116#h_01HXHYD7277MFKPPCBS3NRJQDB).

### When Cached Sessions Appear

A cached session is automatically created every time a DAW project containing the UAD Console Recall plug-in is opened and the plug-in's SYNC function is enabled. In this scenario, the SYNC function loads the UAD Console session contained in the DAW project, and the previously-active UAD Console settings are moved into the cached sessions menu.

The previously-saved UAD Console session's filename is retained in the cached session, and a timestamp is prefixed so it can be easily distinguished from other sessions. The five most-recently cached sessions appear in the list.
