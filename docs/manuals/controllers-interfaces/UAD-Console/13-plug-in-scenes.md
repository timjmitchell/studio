Source: https://help.uaudio.com/hc/en-us/articles/28354758319892-Plug-In-Scenes
Updated: 2025-03-31T22:23:52Z

# Plug-In Scenes

Plug-In Scenes provide a simple settings management tool that allows you to rapidly change plug-in settings across all of your UAD Console channels. With Plug-In Scenes, you can switch between Plug-In Scenes manually or by sending MIDI messages to UAD Console.

---

# What is a Plug-In Scene?

The main feature of Plug-In Scenes is the ability to recall plug-in settings quickly. A Plug-In Scene is a collection of settings applied across the plug-ins in your UAD Console session. Up to 128 Plug-In Scenes can be saved and recalled to capture and apply plug-in parameter changes across your UAD Console session. A Plug-In Scene can also be Primed (queued) before it is loaded.

When you save a Plug-In Scene, plug-ins that are included in the scene are highlighted with a pink bar under the plug-in icon or nameplate.

![](https://help.uaudio.com/hc/article_attachments/28495788113940)

*Plug-ins without Plug-In-Scenes enabled*

![](https://help.uaudio.com/hc/article_attachments/28495788120212)

*Plug-ins with Plug-In-Scenes enabled*

## Plug-In Scenes features

Plug-In Scenes recall settings within plug-ins. The following items can be saved and recalled with a Plug-In Scene:

* Parameter settings within a plug-in
* On and off or bypass states (with the switch within a plug-in, not the plug-in's global toolbar)
* UAD Console Tempo setting

**Notes**

* Preamp controls for a Unison plug-in in the Unison insert (48v, Pad, Polarity, and Low-Cut Filter) are not saved and recalled within a Plug-In Scene
* Plug-In Scenes don't add or remove plug-ins dynamically. See [Adding and removing plug-ins from Plug-In Scenes](https://help.uaudio.com/hc/en-us/articles/28354758319892#h_01J2VY54VP0QTESEMH98KDXH1Y) for more information.
* UAD Console settings including faders, sends, cues, solos, mutes, and other controls are not recalled in Plug-In Scenes.You can use Console Session files to save and recall complete Console configurations (Console Sessions cannot be recalled via MIDI)

---

# Showing the Plug-In Scenes browser

There are four ways to show the Plug-In Scenes browser.

* Click the PLUG-IN SCENES switch to toggle the Plug-In Scenes browser. Plug-In Scenes are visible when the switch is illuminated. The PLUG-IN SCENES switch is only visible when the Mixer Navigation section is visible (View > Section > Mixer Navigation)  
  ![](https://help.uaudio.com/hc/article_attachments/28495788133524)
* Choose View > Section > Plug-In Scenes from the UAD Console menus
* Press Command + E (macOS) or Ctrl + E (Windows) to toggle the Plug-In Scenes browser
* Click the SCENE area in the info bar at the bottom of the UAD Console screen to toggle the Plug-In Scenes browser  
  ![](https://help.uaudio.com/hc/article_attachments/28495788137108)

---

# Using Plug-In Scenes

Plug-in Scenes initially appear as a list of empty scenes in the Plug-In Scenes browser.

![](https://help.uaudio.com/hc/article_attachments/28495788142484)

## Saving Plug-In Scenes

After you have added the plug-ins you want in your Plug-In Scene configuration, save the first scene. Click on an empty scene, then click Save, or press Option+Command+S (macOS) or Alt+Ctrl+S (Windows). The scene is saved with the name Scene #[number].

![](https://help.uaudio.com/hc/article_attachments/28495796038548)

The plug-ins that are included in the Plug-In Scene are indicated with pink highlights below the insert plates.

![](https://help.uaudio.com/hc/article_attachments/28495796048020)

As you make changes to plug-in settings for different audio scenarios, save those changes in other Plug-In Scenes. When you have made changes to plug-in settings within a Plug-In Scene, the Scene name is italicized and prefixed with an asterisk (\*).

You can save changes to an existing Plug-In Scene or an empty Plug-In Scene with these methods:

* Select a Scene and click Save. The current plug-in settings are saved to the Plug-In Scene you selected
* Select a Scene and Press Command + Option + S (macOS) or Ctrl+Alt+S (Windows)
* Right-click the current (italicized) Plug-In Scene and choose Save Scene
* Right-click an existing Plug-In Scene and choose Overwrite. Overwrite is not available with Empty Scenes. Overwriting a Plug-in Scene also renames it with the current Plug-In Scene name.

After changes are saved to a Plug-In Scene, the Plug-In Scene name is no longer italicized or prefixed with an asterisk.

**Tip:** Remember to select a new Plug-In Scene after you make plug-in parameter changes and before you save, to avoid overwriting your current Plug-In Scene.

## Renaming a Plug-In Scene

You might find it useful to give Plug-In Scenes names to indicate their function, role in a performance, or settings information.

### To rename a Plug-In Scene:

* Right-click the Plug-In Scene, choose Rename, type a new name, then press Enter or Return
* Double-click the Plug-In Scene and type a new name, then press Enter or Return

## Clearing a Plug-In Scene

Clear a Plug-In Scene to remove any plug-in parameters from that scene, and set the scene as an Empty Scene.

### To clear a Plug-In Scene:

* Right-click the Plug-In Scene in the list, and choose Clear

---

# Adding and removing plug-ins from Plug-In Scenes

When you save a Plug-In Scene, all currently instantiated plug-ins are saved in that Plug-In Scene.

![](https://help.uaudio.com/hc/article_attachments/28495796052244)

*Plug-ins saved in a Plug-In Scene*

## Adding a plug-in to a Plug-In Scene

When you add a plug-in to UAD Console after a Plug-In Scene is saved, the new plug-in is not saved in any scene unless the scene is saved again. However, the newly added plug-in and its settings remain in place, even if a different scene is subsequently loaded.

**Important:** You must re-save every Plug-In Scene in which you want to include the added plug-in. Otherwise, the plug-in retains only the settings from the last Plug-In Scene in which it was recalled, or its static settings if it is never saved in a Plug-In Scene.

![](https://help.uaudio.com/hc/article_attachments/28495788167700)

*Mixed saved and not saved plug-ins in a Plug-In Scene*

## Removing a plug-in from a Plug-In Scene

When you remove a plug-in after a Plug-In Scene is saved, that plug-in is removed from every Plug-In Scene in the active Console Session. A warning dialog appears when you attempt to remove any plug-in that is currently used in a Plug-In Scene.

**Note:** The Plug-In Scene continues to recall plug-in parameter changes for any remaining plug-ins. Deleting one or more plug-ins from a Plug-In Scene does not clear the Plug-In Scene.

![](https://help.uaudio.com/hc/article_attachments/28495796062996)

**Tip:** If you choose the "Don't show again" option in this dialog, you can reset these "don't show" options by clicking Reset in Settings > Options > Don't Show Again Dialogs.

---

# Recalling Plug-In Scenes

The main feature of Plug-In Scenes is the ability to recall plug-in settings quickly. To do this, you can recall Plug-In Scenes manually or via MIDI messages.

## Active Plug-In Scene

The Plug-In Scenes browser indicates the active Plug-In Scene in the CURRENT field.

## Primed Plug-In Scene

When you select a Plug-In Scene that is not the current active scene, it appears in the PRIMED field.

## Recalling a Plug-In Scene manually

To recall a Plug-In Scene, select it in the browser. The Plug-In Scene is now listed in the PRIMED field. Press the Recall button to recall the scene, or press Enter or Return on your keyboard.

The new Plug-In Scene is loaded and your plug-in settings are applied, and the PRIMED field now lists (NONE).

You can use the up/down arrow keys on the keyboard, or the up/down buttons on the Plug-In Scene browser, to navigate through the list of Plug-In Scenes.

![](https://help.uaudio.com/hc/article_attachments/28495788175252)

## Recalling Plug-In Scenes with MIDI

You can recall Plug-In Scenes with MIDI messages. When recalling a Plug-In Scene via MIDI, the settings for the selected Plug-In Scene are instantly loaded, and do not need to be primed and recalled.

### To change Plug-In Scenes with a MIDI controller

1. Connect your MIDI controller to your computer.
2. In UAD Console, click the Settings button to open the Settings window, then click the MIDI tab.
3. From the Device list, select the desired MIDI device that will send Plug-In Scene changes.
4. To change the MIDI channel on which MIDI events are sent, type a value in the PLUG-IN SCENES CHANNEL field, then press Enter or Return.  
   ![](https://help.uaudio.com/hc/article_attachments/28495796070804)
5. Select the event that will change Plug-In Scenes from the PLUG-IN SCENES EVENT list. If you select Note and you are using the same MIDI channel for Plug-In Scene Changes as for Tap Tempo Events, a warning message appears.  
   ![](https://help.uaudio.com/hc/article_attachments/28495788184340)

After you have configured MIDI settings, you can send MIDI messages with your controller to quickly change Plug-In Scenes. The Plug-In Scene switches instantly when UAD Console receives the MIDI message, with no need to recall or Prime.

* If the controller is sending MIDI Program Change messages, Scenes 1–128 correspond to MIDI program change messages 0–127. Your controller may label these as 0–127 or 1–128, so it is important to check that your scenes are switching correctly.
* If the controller is sending Note data, Scenes 1-128 correspond to MIDI notes C(-1)–G(9).
