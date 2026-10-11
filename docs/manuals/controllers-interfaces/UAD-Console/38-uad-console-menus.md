Source: https://help.uaudio.com/hc/en-us/articles/25357516812564-UAD-Console-Menus
Updated: 2026-05-12T16:57:27Z

# UAD Console Menus

UAD Console menus appear at the top of the screen (macOS), or at the top left of the UAD Console window (Windows).

# Application Menus

Various UAD Console functions can be accessed from the Application Menus. Selecting an item from the drop menus performs the function.

![](https://help.uaudio.com/hc/article_attachments/25357537269780)

*UAD Console Application Menus*

**Tip:** Many menu functions can also be accessed using the keyboard shortcuts shown next to the item in the menu.

## File Menu

![](https://help.uaudio.com/hc/article_attachments/25357537270036)

### Session Files Location

By default, all UAD Console session files are stored at the following location within the OS file system (the same location used by the Session Browser):

* Mac: Users/UserName/Documents/Universal Audio/Sessions/
* Windows: C:\Users\UserName\AppData\Roaming\Universal Audio\Sessions  
  **Tip:** UAD Console sessions can be organized via the operating system's file manager. File locations in the OS are reflected within the Sessions Manager.

### New

Creates a new UAD Console session with default settings (default settings cannot be changed). If the current session has been modified, a dialog appears allowing you to save it first.

### Open...

Opens the operating system's standard "Open File" dialog for loading existing session files from disk.

Session files can also be opened by double-clicking .uadmix files from within the OS file system.

### Save

If a session file was previously saved, selecting this option writes the current settings to the file with the same name, overwriting the previously saved file.

If the current session has never been saved, the operating system's standard "Save File" dialog appears so a new session file can be named and saved to disk.

### Save As...

This option opens the operating system's standard "Save File" dialog so the current session can be named and saved to disk as a new session file.

**Important:** Session settings will not be saved if the "/" (forward slash) or "?" (question mark) characters are in the filename. Avoid these and other special characters when saving session files.

## Edit Menu

![](https://help.uaudio.com/hc/article_attachments/25357516809876)

**Note:** See [Multiple Undo/Redo](https://help.uaudio.com/hc/en-us/articles/25347220842516#h_01HXHMZY0TWQ92EQTA1PQ36CG2) for an overview of Undo/Redo.

### Undo

When a parameter value in the UAD Console window is edited, the change can be reverted with the Undo command. By executing Undo again, edits can be stepped backwards repeatedly.

The number of Undo steps is essentially unlimited. The Undo cache is active until a new or different session is loaded or UAD Console is quit.

### Redo

When the Undo function (above) is executed, the original edit can be restored with the Redo command. By executing Redo again, previous Undo's can be restored repeatedly.

The number of Redo steps is essentially unlimited. The Redo cache is active until a new or different session is loaded.

### Remove All

All plug-ins can be categorically deleted from UAD Console by selecting an item from the sub menu.

### Enable All

All plug-ins can be categorically enabled from UAD Console by selecting an item from the sub menu.

### Disable All

All plug-ins can be categorically enabled from UAD Console by selecting an item from the sub menu.

### Remove/Enable/Disable Sub-Menu

![](https://help.uaudio.com/hc/article_attachments/25357537270804)

**Plug-Ins –** The function is performed on all UAD Console plug-ins.

**Insert Plug-Ins –** The function is performed on all channel insert plug-ins. Aux and Unison plug-ins remain inserted.

**Aux Plug-Ins –** The function is performed on all auxiliary plug-ins. Channel and Unison plug-ins remain inserted.

**Unison Plug-Ins –** The function is performed on all Unison plug-ins. Channel and aux plug-ins remain inserted.

## Navigation Menu

![](https://help.uaudio.com/hc/article_attachments/25357537271188)

### Mixer Scroll Left / Right

Scrolls the Mixer section one channel to the left or right, when all mixer channels are not onscreen. You can also scroll the mixer with the left and right arrow keys.

### Mixer Bank Left / Right

Banks the Mixer section one set of channels to the left or right, when all mixer channels are not onscreen. You can also bank the mixer with the Command+left/right arrow keys (macOS) or Alt+left/right arrow keys (Windows).

### Mixer Far Left / Right

Scrolls the mixer channels all the way to the left (first channel) or right (last channel). You can also scroll the mixer with Option+Command+left/right arrow keys (macOS) or Shift+Alt+left/right arrow keys (Windows).

## View Menu

![menu-view.png](https://help.uaudio.com/hc/article_attachments/32067338697748)

### Section > Mixer Navigation

Shows the Mixer Navigation section, or hides it when it is visible.

### Section > Plug-In Scenes

Shows the Plug-In Scenes browser, or hides it when it is visible.

### Section > Auxes

Shows the aux returns when they are hidden, and hides them when they are visible. This item performs the same function as the Show Aux switch in the monitor column.

### Section > Control Room

Shows the Control Room column (when Monitor is shown), or hides it when it is visible. This item performs the same function as the Show Ctrl room switch in the monitor column.

### Section > Monitor

Shows the Monitor column, or hides it when it is visible. The Monitor column must be shown to view Auxes and/or the Control Room column.

### Section > Monitor Correction

Shows the Monitor Correction buttons, or hides them whenthey are visible. Also shows or hides the Monitor Correction panel in the Monitor Controller window.

### Section > Notifications…

Shows the Notifications panel, where you can see any notifications that have occurred in the current session.

### Compact Monitor Faders

Shortens the height of the monitor faders, or returns them to full height if they are compacted. Compacted faders allow more room for viewing Inputs, Inserts, Sends, Cues and the Output row.

**Tip:** You can also click at the top of the monitor faders to compact them, or return them to full height.

![](https://help.uaudio.com/hc/article_attachments/25357516811156)

### Show/Hide Channels

![](https://help.uaudio.com/hc/article_attachments/25357516811284)

Allows unused UAD Console inputs to be hidden from view. For details, see [Show/Hide Inputs](https://help.uaudio.com/hc/en-us/articles/25351484855828#h_01HTRDPRVARVWJ1EAAJY3QBXGA).

### Show All Channels

Shows all channels. This menu item is only available when one or more channels are hidden.

### Show/Hide Floating Windows

When one or more floating windows are open (for example, the Cue Outputs window or plug-in windows), you can Show or Hide these windows with this command, or with the keyboard shortcut Shift+W.

### Preferences

Opens the UAD Console Settings window, where various global parameters are configured. See [UAD Console Settings](https://help.uaudio.com/hc/en-us/articles/25403524417812) for details about the screen.

## Window Menu

![](https://help.uaudio.com/hc/article_attachments/25357516811540)

### New Alternate Window

Creates a new UAD Console window.

### Previous/NextWindow

Use the Previous/Next Window menu items or the key commands (Shit+ Cmd+' and Cmd+' on macOS, Shift+Ctrl+' and Ctrl+' on Windows) to cycle through open UAD Console windows.

### Show/Hide Floating Windows

When one or more floating windows are open (for example, the Cue Outputs window), you can Show or Hide these windows with this command, or with the keyboard shortcut Shift+W.

### Full Screen

Expands the UAD Console window to fill your screen. Use the key command Shift+Command+F (macOS) or Shift+Ctrl+F (Windows) to toggle full screen mode.

**Note:** In full screen mode, you cannot see the UAD Console application menus.

## Help Menu

![menu-help.png](https://help.uaudio.com/hc/article_attachments/49174978260628)

### Documentation

This item opens the UA Knowledge Base section containing the UAD Console Manual. Consult the documentation when you need specific operational information.

### Give Feedback

This item opens the Feedback window to report a bug, request a feature, or give general feedback.
