Source: https://help.uaudio.com/hc/en-us/articles/25347220842516-Layout-General-Operation
Updated: 2026-03-03T18:00:04Z

# Layout & General Operation

UAD Console’s visual and control elements are designed with a layout similar to that found on typical analog mixers.

UAD Console always shows certain screen elements (the title bar, info bar, meter bridge, and bank bar). Other UAD Console elements can be shown, hidden, resized, or collapsed, with a wide range of flexibility.

![console-callouts.png](https://help.uaudio.com/hc/article_attachments/46835318574356)

# Window Title Bar

The Window Title Bar is the topmost strip in the UAD Console window, as shown below.

![uad-console-top-bar.png](https://help.uaudio.com/hc/article_attachments/46835318576404)

*Console Title Bar*

**Device tabs –** In the UAD Console window, the current session filename is displayed in the device tab. If the session has not yet been saved to disk, “New Session” is displayed here. If you have Volt or Apollo E Series devices, tabs for those devices appear here. Click a tab to switch to another device view, or use the key commands to navigate (Cmd+Ctrl+left arrow / right arrow in macOS, Shift+Ctrl+left arrow / right arrow on Windows).

**Tip:** If the session has been modified, an asterisk\* appears in the name.

**Window Buttons –** In the title bar, the UAD Console window includes standard Close, Minimize, and Maximize buttons.

![](https://help.uaudio.com/hc/article_attachments/25347278139924)

*Close, Minimize, and Maximize buttons*

**Close –** Click the “X” button to close the UAD Console window. Clicking this button quits UAD Console.

**Note:** UAD Console’s current settings are saved to disk when quit. When UAD Console is subsequently launched, those settings are transferred to Apollo.

**Minimize –** Click the “\_” button to reduce the window to the Dock (Mac) or Taskbar (Windows). The window can be restored by clicking the minimized window, or any method detailed in [Accessing UAD Console].

**Maximize –** Click the square button to expand UAD Console to the maximum size available on the screen where the window currently resides.

# Navigating the Mixer

The Mixer Navigation section is visible at the left side of the UAD Console window when View > Section > Mixer Navigation is checked. You can use the Mixer Navigation controls to show and hide rows in the input channel strips and the faders, and to scroll mixer rows to the top of the view area. All Mixer rows are visible at one time in the input channel strips, though you may have to scroll to view them all. Mixer rows can be individually collapsed and expanded, or completely hidden from view.

![mixer-navigation-callouts.png](https://help.uaudio.com/hc/article_attachments/36203800130452)

# Showing & Hiding Channel Strip Rows

Six channel strip rows can be made visible in UAD Console:

* Inputs
* Inserts
* Sends
* Output
* Fader
* Sends Overview\*

**\*Note:** Sends Overview is a separate view for the Sends and Cues row. If the Sends row is not displayed, clicking Sends Overview has no effect.

Each row displays related elements and associated functionality in the main area of the UAD Console window. Currently visible rows are highlighted in the Mixer Navigation panel.

* Click a section in the Mixer Navigation panel to scroll that section into the visible area. Rows that are visible are illuminated in the Mixer Navigation section.
* To hide a row, deselect the circle next to the row name.
* To show only one row, Command+Click (macOS) or Control+Click (Windows) the row name.
* To expand all mixer rows, click Open. To collapse all mixer rows, click Close.
* To show large inserts in the input channel strips, click Large. To show small inserts in the input channel strips, click Small.
* To show all possible insert slots for the input channel strips, click Fixed Slots. Click Fixed Slots again to only show the insert slots that are in use.

**Note:** Row switches and view options do not apply to Aux or Talkback channel strips. Aux and Talkback channel strips use context menus to change view options. See the [Aux Returns](https://help.uaudio.com/hc/en-us/articles/25351771431060) and [Talkback](https://help.uaudio.com/hc/en-us/articles/26489966354836) articles for more information.

## Opening and Closing Individual Channel Strip Rows

Each channel strip row can be opened (expanded) or closed (collapsed). When closed, the disclosure triangle points to the right, and the controls for the row are not available. A closed mixer row remains in the mixer, but is collapsed to a single row with no available controls. When a mixer row is open, the disclosure triangle points down, and the controls for that mixer row are available. Mixer rows can be globally or individually expanded or collapsed.

To open or close a mixer row, click the disclosure triangle at the left of the row in the Options column.

![](https://help.uaudio.com/hc/article_attachments/25347266306580)

*Mixer rows closed (Inserts) and open (Sends)*

## Opening or Closing all Mixer Rows

You can open or close all mixer rows with the global control. In the Mixer Navigation area, click Open or Close to open or close all rows.

![mixer-sections-open-close-all.png](https://help.uaudio.com/hc/article_attachments/36203754298004)

## Resizing Mixer Rows

In the UAD Console mixer, you can show a large or small view for the Inserts, Sends, and Cues rows. The large view generally shows more controls. For example, the large view of the Sends row includes a pan control and a full vertical fader. The Sends Overview shows faders and pan controls for Sends and Cues.

**Note:** The large view for Inserts does not include more controls, but does reveal plug-in icons and the hover option controls. Large view for Inserts also applies to the Unison insert.

### Resizing Individual Mixer Rows

To switch a mixer row to the large size, click the icon at the left of the row in the Options column. When a mixer row is large, the icon to the left of the row is highlighted yellow.

![](https://help.uaudio.com/hc/article_attachments/25347278186516)

*Small and large Inserts section*

### 

*Small and large Sends rows*

### Resizing all Mixer rows

You can resize all mixer rows to small or large view with the global control. In the Mixer Navigation area, click Large or Small to resize all mixer rows.

![mixer-sections-resize-all.png](https://help.uaudio.com/hc/article_attachments/36203754302484)

## Using Fixed Slots

By default, UAD Console shows one Insert row, and expands to show an empty insert row each time an insert effect is added. For example, if you load insert slots into the first two slots, three rows are shown, and so on, until you reach the maximum of four insert slots.

If you want to toggle all insert slots, click Fixed Slots. When highlighted yellow, all insert slots are visible. When gray, only the insert slots currently in use, plus one empty row, are displayed, up to the maximum of four rows.

![](https://help.uaudio.com/hc/article_attachments/25347278214932)

## Viewing the Sends Overview

Click the Sends Overview switch to show the Sends Overview for all mixer channels. See [Sends](https://help.uaudio.com/hc/en-us/articles/25350937974676) for more information.

![sends-overview-switch.png](https://help.uaudio.com/hc/article_attachments/36203800134932)

![](https://help.uaudio.com/hc/article_attachments/31072798643220)

# Global Insert Effects Switch

![](https://help.uaudio.com/hc/article_attachments/31072798646292)

These buttons globally switch all UAD Console’s inserts to either pass all UAD insert effect processing to the DAW (print wet) or not (monitor wet but print dry).

Insert Effects can also be individually switched on a per-channel basis (see [Individual Channel Insert Effects Switch](https://help.uaudio.com/hc/en-us/articles/25350369296660#h_01HTRBHF0F54AHCABAQ3AP7J2D)). The Global Insert Effects switches override all the individual Channel Insert Effects settings.

**Important:** UAD plug-in processing in UAD Console’s Unison and auxiliary inserts is always routed to the DAW (when recording the AUX channels), regardless of the current Insert Effects setting (Unison and aux insert processing is always recorded).

# Options Column

You can reconfigure the UAD Console view options. The Options column includes individual display controls for each input channel row, and the Clear Solo and Clear Over Limit switches.

![](https://help.uaudio.com/hc/article_attachments/25347278223380)

# Popovers

![](https://help.uaudio.com/hc/article_attachments/25347266391060)

Some Console functions that are not visible in the main window are accessed with popovers. Popovers are a special type of overlay that automatically close when any area outside of the popover is clicked.

**Note:** The size of popovers cannot be adjusted.

To close any popover, click anywhere outside of the popover, press the X switch at upper left of the overlay, or type the ESC (escape) key on the computer’s keyboard.

The following functions are accessed via popovers:

* I/O Matrix assign
* Rename/link channel inputs
* Add Device (Console Settings)
* I/O Matrix presets
* Tempo
* Sends Overview
* Surround Monitor\*

\*Apollo X only

# Multiple Undo/Redo

UAD Console supports multiple levels of Undo and Redo for all edit operations. Undo and Redo operations can be performed repeatedly to step backwards and forwards through edit operations as long as the current session is open.

* To step backwards and undo (revert) edit operations, choose Undo from the Edit Menu or type Command+Z (macOS) or Control+Z (Windows).
* To step forwards and re-execute the edit, choose Redo from the Edit Menu or type Command+Shift+Z (macOS) or Control+Shift+Z (Windows) .

## Undo/Redo Cache

Edits are stored in the Undo/Redo cache. Edits within a particular session can be reverted with Undo/Redo until the cache is cleared. Both of these operations will clear the Undo/Redo cache:

* Console is quit
* A different Console session is loaded

**Important:** Prior Undo/Redo operations cannot be performed after the Undo/Redo cache is cleared.

# Keyboard Control

Many Console functions can be controlled without using a mouse. When elements on the screen have keyboard focus, they can be quickly navigated with the computer’s keyboard.

## Focus Control

Focused items can be selected by using the up/down arrow keys and/or the Return/Enter keys.

![](https://help.uaudio.com/hc/article_attachments/26483381494164)

*The preset is focused and can be navigated with the up/down arrow keys on the keyboard.*

# Adjusting UAD Console Controls

UAD Console uses typical software control techniques to adjust parameters.

**Switches:** Click to toggle the state.

**Knobs:** Click+drag to adjust, or use the [Controls Shortcuts]. UAD Console’s rotary controls (and UAD plug-in knobs) can respond to Linear, Circular, or Relative Circular adjustments modes. The CONTROLS MODE preference is set in the Options panel within the Console Settings window.

**Faders:** Click+drag to adjust, or use the Controls Shortcuts.

**Drop Menus:** Click to view the drop menu contents, then click an item in the drop menu to select the item.

**UAD Plug-Ins:** Most UAD plug-in controls use the same methods as above. However, some plug-in parameters may have custom controls that are unfamiliar or not obvious. All custom controls are detailed for individual plug-ins in the UAD Plug-Ins Manual or the individual plug-in manual.

# Controls Shortcuts

In addition to the keyboard shortcuts below, several other shortcuts are available to simplify UAD Console control adjustments:

* **Fine Control:** Continuous controls (knobs and faders) can be adjusted with increased resolution by depressing the Shift key while adjusting these controls.
* **Scroll Wheel:** Continuous controls (knobs and faders) can be adjusted by using the computer input device’s scroll function (e.g., mouse scroll wheel). Hover the cursor over the control and press Option (macOS) or Alt (Windows), and adjust the scroll wheel to modify the parameter value.
* **Adjust All:** If the Command (macOS) or Control key (Windows) is held down while modifying any control, the same control on all inputs (or aux returns) will be simultaneously adjusted. The relative difference is maintained between the same controls until any control reaches its minimum or maximum value.
* **Return To Default:** If the Option key (macOS) or Alt key (Windows) is held when a control is clicked, the control will return to its default value. Command+Option+Click (maOS) or Ctrl+Alt+Click (Windows) will return all controls of the same type to their default value.
* **Mute/Solo All Toggle:** Option-click (macOS) or Alt+click (Windows) a Mute or Solo switch to toggle the state on all channels.
* **Drop Menus:** Menus continue to display after a single right-click. The mouse button does not need to be held down to view the menu.

# Keyboard Shortcuts

Console supports the keyboard shortcuts listed below.

### **Navigation and Windows**

* **Close Console:** Command+W (Mac) | Control+W (Win)
* **Next Window:** Command+` (Mac) | Control+` (Win)
* **Previous Window:** Command+Shift+` (Mac) | Control+Shift+` (Win)
* **Toggle Full Screen:** Command+Shift+F (Mac) | Control+Shift+F (Win)
* **Show Settings:** Command+, (Mac) | Control+, (Win)
* **Show/Hide Floating Windows:** Shift+W (Both)
* **Quit Console:** Command+Q (Mac) | Control+Q (Win)
* **Quit All (Console & Mixer):** Control+Option+Command+Q (Mac only)

### **Mixer Scrolling & Visibility**

* **Scroll One Channel Left/Right:** ← / →
* **Scroll One Bank Left/Right:** Command+← / Command+→ (Mac) | Control+← / Control+→ (Win)
* **Jump to Far Left/Right:** Option+Command+← / Option+Command+→ (Mac) | Alt+Control+← / Alt+Control+→ (Win)
* **Show Aux Strips:** Command+A (Mac) | Control+A (Win)
* **Show Control Room:** Command+R (Mac) | Control+R (Win)
* **Show/Hide Selected Channels:** Command+I (Mac) | Control+I (Win)

### **Session Management**

* **New Session:** Command+N (Mac) | Control+N (Win)
* **Open Session:** Command+O (Mac) | Control+O (Win)
* **Save Session:** Command+S (Mac) | Control+S (Win)
* **Save A Copy As:** Command+Shift+S (Mac) | Control+Shift+S (Win)

### **Editing and Modifiers**

* **Undo:** Command+Z (Mac) | Control+Z (Win)
* **Redo:** Command+Shift+Z (Mac) | Control+Shift+Z (Win)
* **Copy:** Command+C or C (Mac) | Control+C or C (Win)
  + Also activates the COPY modifier in the mixer.
* **Cut:** Command+X or X (Mac) | Control+X or X (Win)
* **Paste:** Command+V or V (Mac) | Control+V or V (Win)

v260122
