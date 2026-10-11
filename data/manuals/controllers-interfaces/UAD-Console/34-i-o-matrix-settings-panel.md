Source: https://help.uaudio.com/hc/en-us/articles/25403673923220-I-O-Matrix-Settings-Panel
Updated: 2025-03-31T22:23:52Z

# I/O Matrix Settings Panel

The I/O Matrix panel is where customized I/O routings for Core Audio (Mac) or ASIO (Windows) are managed at the driver level.

**Note:** The I/O Matrix and its associated features are only available with Thunderbolt-connected Apollo models.

# I/O Matrix Columns

In addition to the switches at the top of the panel, two columns are displayed. The INPUTS column on the left displays all available Apollo inputs. The OUTPUTS column on the right displays all available Apollo outputs.

# I/O Matrix Rows

Each row in the panel represents a single Apollo audio channel. The currently assigned input and output route for each channel is displayed within a single row. By clicking any assign switch, a different route can be mapped to the channel.

**Tip:** To view more channels simultaneously, increase the vertical size of the UAD Console Settings window.

![](https://help.uaudio.com/hc/article_attachments/25403673917716)

*The I/O Matrix Panel*

# I/O Matrix Panel Elements

![](https://help.uaudio.com/hc/article_attachments/25403673917972)

*The main I/O Matrix panel elements*

**Note:** Channels in gray italic text in the output column can be reassigned by disabling the feature that is currently using the route. These features are:

* Flex Routes
* DSP Pairs
* Cue Outputs
* Cue Output Mirrors
* Digital (S/PDIF) Mirror
* ALT monitoring
* Surround Sound

# Mode Menu

![](https://help.uaudio.com/hc/article_attachments/25403688812052)

*Mode menu*

This menu provides a quick method to return to Apollo's default Core Audio / ASIO driver settings. When any settings within the I/O Matrix panel are not the default value, this menu displays "Custom."

To return to the factory default settings, choose "Default" from the MODE drop menu.

**Important:** Any customized settings within the I/O Matrix panel will be lost when the mode is changed to Default unless the custom settings are saved first via the I/O Preset controls.

If the mode is switched from Default to Custom, the I/O Preset Display shows "(Untitled)" indicating the current settings have not yet been saved.

# I/O Presets Overview

The I/O presets controls provide methods for managing complete I/O Matrix panel configurations as I/O preset files. When an I/O preset file is saved, the current I/O Matrix panel configuration is written to disk.

When an I/O preset file is subsequently reloaded, the I/O Matrix panel is returned to the exact same routing state, regardless of any changes to I/O Matrix settings that were made in the interim.

## I/O Preset Files Location

I/O preset files are saved to, and loaded from, the user's home folder at:

* Mac: Users/[UserName]/Documents/Universal Audio/IOPresets/
* Windows: C:\Users\[UserName]\Documents\Universal Audio\IOPresets\

**Note:** I/O preset files must reside in the default location to appear in the Route Presets popover window within UAD Console.

## I/O Preset Files Suffix

I/O preset files have the ".uadio" suffix. The suffix is added to I/O preset files automatically when saving to disk; however, the suffix is not displayed in the file save dialog (the suffix should not be manually typed when saving a I/O preset file).

**Note:** Without the .uadio suffix, I/O preset files will not be visible in the load preset window.

## Factory I/O Presets

A variety of I/O presets are pre-installed with the software. The factory I/O presets are provided for backwards compatibility with Apollo sessions created with UAD Console v1.

To take advantage of all of the features in the I/O Matrix and UAD Console, the Default mode Custom modes may prove more appropriate in order to take advantage of the features (such as limiting the driver to 32 I/O channels, arranging the I/O in any desired order, using up to 4 CUE mixes, or using up to 8 Virtual I/O channels).

**Note:** If older DAW sessions were saved using previous versions of Apollo's driver and the I/O Matrix features are used upon reload, the Input/Output configuration tools in the DAW software may need to be modified.

# I/O Presets Menu

![](https://help.uaudio.com/hc/article_attachments/25403673919124)

The currently loaded I/O preset name is displayed on top of the menu switch, as shown at right. If the I/O preset has not yet been saved, then "(Untitled)" appears in the display.

If a loaded I/O preset has been modified since it was saved, the I/O preset name is displayed in italics, as shown at right.

Clicking the I/O Presets display opens the I/O Presets Popover, where various I/O preset functions can be performed.

## Save Switch

![](https://help.uaudio.com/hc/article_attachments/25403673919508)

*Save I/O preset window*

This switch saves the current state of the I/O Matrix panel to disk as an I/O preset file. If the I/O preset already exists, the existing I/O preset file is overwritten with the current settings. If the I/O preset has never been saved, the Save I/O preset window (shown at right) appears so the preset can be named.

**Important:** Settings will not be properly saved if the "/" (forward slash) or "?" (question mark) characters are in the filename. Avoid these and other special characters when saving I/O preset files.

# I/O Presets Popover

The I/O Presets popover window is where various functions can be performed on I/O preset files. To open the I/O Presets popover, click the I/O Presets Menu.

![](https://help.uaudio.com/hc/article_attachments/25403673920276)

*The I/O Presets popover*

All existing I/O preset files at the I/O Preset Files Location are displayed in a list within the I/O Presets popover. Available functions at the bottom of the popover can be performed on the selected I/O preset (a preset is selected when it is highlighted in gray).

## I/O Presets Functions

The following I/O preset functions are available:

**Open –** Opens the operating system's standard "Open File" dialog for loading existing I/O preset files from disk.

**Save –** Saves the current modified I/O preset file in place. If the preset was not previously saved (if the file doesn't exist), the Save window appears so it can be named.

**Save As –** Opens the Save window so the current settings can be named and saved to disk as a new I/O preset file.

**Load –** Loads the I/O preset that is currently selected (highlighted gray) within the I/O Presets popover.

**Rename –** Allows you to rename the selected I/O preset.

**Delete –** Allows you to delete the I/O preset that is currently selected within the I/O Presets popover (a preset is selected when highlighted in blue).

**Tip:** An I/O preset can also be loaded by double-clicking the preset or typing Return (or Enter) when the preset is selected.

# Channel Count Menus

![](https://help.uaudio.com/hc/article_attachments/25403673920660)

*Channel Count menu*

The Channel Count menus (one each for number of inputs and number of outputs) are used to change the number of Apollo I/O channels used by Core Audio / ASIO.

By default, the total number of available input and output channels, for all detected Apollo devices, are displayed.

The primary reason to change the channel counts is to accommodate the 64 I/O channels available within Pro Tools. When 64 channels are selected for Apollo I/O (PT Mode), any Apollo I/O can still be used by virtually remapping the I/O so the desired channels fit within the available channel count.

**Important:** These menus change the driver I/O complement. Quit all DAW applications before changing the Channel Count settings.

**# Inputs –** The number of active Apollo input channels used by Core Audio / ASIO is displayed here. Click the display to select a different input channel count from the menu.

**# Outputs –** The number of active Apollo output channels used by Core Audio / ASIO is displayed here. Click the display to select a different output channel count from the menu.

**Note:** Each Core Audio / ASIO stream uses host computer CPU resources. To maximize CPU performance, do not set the channel counts higher than the number of channels actually needed.

# Device Name Display

The Device Name of the Apollo device is displayed in the INPUT and OUTPUT columns so each Apollo unit can be readily identified in multi-unit setups. Each device is color-coded for easier identification.

# Cascade Switch

The Cascade switch is used to quickly assign continuous I/O channels if routings have been changed from default values.

**Note:** Cascade doesn't do anything when the Mode Menu displays "Default" because all channels are already continuous in default mode.

When you click Cascade, the Cascade switch and all channel numbers are illuminated. Click+hold any channel number, then swipe down adjacent channel numbers to quickly assign the channel(s) to the next available channel(s) in the device.

**Tip:** Increase the vertical size of the UAD Console screen to view more channels simultaneously, so more channels can be swiped.

![](https://help.uaudio.com/hc/article_attachments/25403688813460)

*Using Cascade to quickly assign multiple channels. In this example, ADAT 2 – 8 have been reassigned in a different order. With Cascade engaged (right side), swiping the ADAT outputs starting with ADAT 1 reassigns the ADAT outputs to the original order.*

# Assign Switches

![](https://help.uaudio.com/hc/article_attachments/25403673921684)

*Two assign switches*

Each input and output channel has an assign switch. The assign switches are indicated by disclosure triangles at the lower right of each switch. The currently assigned route is displayed in the switch.

Default input and output routes can be remapped using the assign switches. Clicking an assign switch opens the Route Assign Popover for mapping a different route to the channel.

# Custom Name Field

![](https://help.uaudio.com/hc/article_attachments/25403688813972)

*Example of customized driver names*

Each Core Audio / ASIO channel includes a name. This name is displayed wherever Core Audio / ASIO channel names are shown, such as I/O channel assignments within a DAW.

Apollo's Core Audio / ASIO channel names can be customized by simply entering a different name in the Custom Name field. All custom name changes are instantly reflected in the application that displays channel names.

## To restore the default driver name

1. Click a customized name in the CUSTOM NAME column. The custom name text is highlighted.

2. Press the Delete key to remove the customized text from the field.

3. Press Return/Enter.

## Routed Channels (gray italics)

Channels that appear as dimmed gray italics text in the output column are in use by a channel assignment. These channels can be reassigned after disabling the feature that is currently using the route. Features that use gray assignments include Flex Routes, DSP Pairs, Cue Outputs, Cue Output Mirrors, Digital (S/PDIF) Mirror, ALT monitoring, and Surround Sound.

# Route Assign Popover

The Route Assign popover window is where Apollo I/O routes can be virtually re-mapped. To open the Route Assign popover, click any assign switch.

**Important:** Custom driver I/O routing changes the driver I/O complement. Quit all audio applications before changing driver I/O assignments.

![](https://help.uaudio.com/hc/article_attachments/25403673922324)

*The Route Assign popover*

## Popover Title Bar Elements

### Previous / Next Channel

Switches the window to display the previous or next Apollo channel.

### Input / Output Channel

Switches the window to display the input or output of the same Apollo channel.

**Tip:** The popover moves from channel to channel with these switches. To prevent the popover from moving when these switches are used, drag the window to any location other than its default position.

### Apollo Hardware Channel

The name of the Apollo hardware channel that is being reassigned is displayed at the top of the window.

## Route Assign Columns

The Device, Inputs, and Outputs columns are displayed in the Route Assign popover.

### Apollo Device

The DEVICE column on the left displays all detected Apollo devices and the NONE switch. Click a device to select it for channel assignments in the other two columns. Click NONE to remove all I/O assignments from the channel.

### Channel Type

The TYPE column in the middle displays all available channel types for the selected Apollo device. Click a channel type to select it and display all channels available for assignment in the INPUT/OUTPUT column.

### Available Routes

The column on the right displays all available routes for the selected channel type. Click an available route to assign the input or output. The assigned route is highlighted in blue.

**Note:** Channels in gray italic text in the output column can be reassigned by disabling the feature that is currently using the route. These features are:

* Flex Routes
* DSP Pairs
* Cue Outputs
* Cue Output Mirrors
* Digital (S/PDIF) Mirror
* ALT monitoring
* Surround Sound
