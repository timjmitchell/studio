# Logic Pro — Field Notes

Practical notes on Logic Pro: what the manual says, how it plays out in this rig,
and what can be scripted from Claude Code. These fill in the gaps the official
guide leaves out. They were written while working on Hot Fog sessions (see
[arbitrary-overlord session notes](../../../music/hot-fog/arbitrary-overlord/session-notes.md)).

**Sources** (same folder):
- [Logic Pro User Guide](logic-pro-mac-user-guide.md), cited as **UG § Heading (line N)**
- [Effects](logic-pro-mac-effects-user-guide.md) and [Instruments](logic-pro-mac-instruments-user-guide.md) guides

**How much to trust each claim.** Each claim is marked with one of:
- ✅ **Manual**: stated in the manual text.
- 🔶 **Inferred**: worked out from the wording, but not stated directly.
- 🧪 **Tested**: confirmed in Logic on this machine (with date).
- ❓ **To test**: see the [test list](#tests-to-run).

---

## 1. Slowing down playback: Varispeed vs Flex & Follow

Two different tools. Pick by intent:

| Goal | Use | Touches tracks/regions? |
|---|---|---|
| Practice or record at a slower speed; hear the song faster/slower | **Varispeed** (Speed Only) | No. It's global and switches off cleanly |
| Actually change the song's tempo | **Project tempo + Flex & Follow** on audio regions | Yes. Audio gets time-stretched |

### Varispeed

- ✅ Speeds up or slows down the **entire project**, audio and MIDI together, from −50% (half tempo) to +100% (double). It's meant for "checking how a project might sound at a faster or slower tempo, and for practicing or recording a performance at a lower speed" (UG § Use Varispeed in Logic Pro for Mac, line 16650).
- ✅ Modes (click the **upper** part of the Varispeed display):
  - **Speed Only**: pitch-shifts the master output to cancel the pitch change. *Speed changes, pitch doesn't.* ← the practice mode
  - **Varispeed (Speed and Pitch)**: tape-style; pitch follows speed.
  - **Varispeed and MIDI**: tape-style, and also transposes *External* MIDI tracks to match (quantized to semitones).
- ✅ Units (click the **lower** part of the display): % · resulting bpm · detune (st) · tuning reference (Hz). Drag vertically on the value, or double-click to type.
- ✅ The control bar's Tempo display keeps showing the **original** tempo while Varispeed is on.
- 🔶 Speed Only works by pitch-shifting the whole mix, so expect some artifacts at large settings. −10 to −20% is usually fine for practice.

#### Showing the Varispeed button

Varispeed is **hidden by default**. It isn't in the standard control bar LCD display.

🧪 Tested by Tim (2026-10-08):
1. Click the **drop-down menu in the display** (the LCD in the middle of the control bar).
2. Choose **Customize Control Bar and Display…**
3. Under the **Display** checkboxes, choose **Custom**. Only then do Varispeed and the other optional display items become available to tick.
4. Tick **Varispeed**.

✅ The manual's wording of the same path: "Control-click the control bar, choose Customize Control Bar and Display from the shortcut menu, choose Custom from the LCD pop-up menu, then select the Varispeed checkbox."
The non-obvious part is step 3. With the display on a preset (e.g. *Beats & Project*), the extra checkboxes aren't available.

#### Varispeed with a tempo map

- ✅ In **bpm** units, the readout is "the resulting tempo, dependent on the current tempo, which changes along with any tempo changes in the project."
- 🔶 So Varispeed **doesn't flatten or override a tempo map**. It scales the whole map by the same ratio (e.g. −20%: 122 → ~97.6, 130 → 104, 150 → 120). Bars, beats, markers, regions and the click all stay lined up.
- 🔶 **Use % units with a tempo map.** A bpm value only matches one point in the song; a percentage means the same thing everywhere.
- 🔶 The tempo map itself isn't edited. Turning Varispeed off returns everything to normal.

### Flex & Follow (changing the real tempo)

- ✅ Per audio region, in the Region inspector's **Flex & Follow** pop-up (UG § Choose how Flex Time and Follow Tempo adjust individual regions, line 16010):
  - **Off**: region does **not** follow project tempo changes.
  - **On**: follows tempo changes and manual Flex edits.
  - **On + Align Bars**: also conforms to the project tempo at every downbeat, using Smart Tempo beat markers.
  - **On + Align Bars and Beats**: same, at every beat.
- 🔶 MIDI follows tempo changes automatically. Audio only follows if Flex & Follow is on, so check every audio region before changing the tempo or the tempo map.
- ✅ The defaults for new recordings and imported audio are set in **Smart Tempo project settings** (UG line 38827).
- 🔶 Time-stretching artifacts depend on the Flex algorithm and the material (drums, vocals). Varispeed is safer when the goal is only to listen or practice.

---

## 2. Project alternatives (not "workspace")

- ✅ "Workspace" in the manual just means the editing area of a window (e.g. the Tracks area). It isn't a versioning concept (UG line 1107).
- ✅ **Project alternatives** are named versions of a project with their own settings: different cuts, mixes, etc. They're **saved inside the same project and share the same assets**. Find them under File > Project Alternatives (UG § Use project alternatives and backups, line 4163).
- ✅ **Main** always exists and can't be removed. New Alternative creates one; Edit Alternatives renames or removes them.
- ✅ Switching alternatives prompts you to save unsaved changes first. Only one is open at a time.
- ✅ **Backups are per alternative.** Each ⌘S saves one, up to 10 per alternative, listed newest first under File > Revert to.
- 🔶 Arrangement and mix edits stay in their alternative, but the audio files are shared, so destructive audio edits and File > Project Management > Clean Up affect **all** alternatives.
- 🧪 The window title shows the open alternative: `<project> - <alternative> - Tracks` (2026-10-06).
- 🧪 On disk: `<project>.logicx/Alternatives/000, 001, …`. Each has its own `ProjectData`, `Project File Backups/`, `Autosave/`, and `MetaData.plist` (key, signature), but **no name field**. The names only come from Logic's File menu (2026-10-08).

---

## 3. Key commands

- ✅ Key Commands window: **⌥K**, or Logic Pro > Key Commands > Edit Assignments. Control-click any menu command to open the window with that command selected (UG § Open the Key Commands window, line 40138).
- ✅ The **Action pop-up menu** is in the **top-left corner of the Key Commands window**, not in the menu bar. It holds Presets, Import, Save / Save As, Expand/Collapse All, and Copy Key Commands to Clipboard (UG line 40164).
- ✅ **Copy Key Commands to Clipboard** copies every command and its binding, ready to paste into a spreadsheet. If you search first, only the matching commands are copied (UG § Export key commands to a spreadsheet, line 40248).
- ✅ Saved key command sets go in `~/Music/Audio Music Apps/Key Commands/` by default.
- ✅ Default transport keys: **Space** = play/stop, **Return** = play/stop / go to start (UG line 3461), **R** = record, **C** = cycle (UG line 3797).
- ✅ "Most of these transport key commands have no default assignment, and need to be assigned manually." Examples are *Stop and Go to Left Locator* and *Play from Previous Bar* (UG § Use transport key commands, line 3565).
- ✅ **Learn New Assignment** (Key Commands window, bottom right): select a command and send a MIDI message, and Logic binds that message to the command (UG § Learn a controller assignment, line 40328).
- ❓ Metronome = **K** is the long-standing Logic default but wasn't found in the manual text.

🧪 This machine (2026-10-06), from `defaults read com.apple.logic10`:
- The active set is the stock **U.S.** preset (`lastSelectedKeyCommandsPath`), and it's unchanged (`lastSelectedKeyCommandsTouched = 0`). So the manual defaults apply.
- The pref path still says `Logic Pro X.app`, but the installed app is `Logic Pro.app`. This stale path looks harmless.
- `~/Music/Audio Music Apps/Key Commands/` is empty, so no custom sets have been saved.
- `~/Library/Preferences/com.apple.logic.pro.cs` holds the controller/control surface assignments. Not inspected yet.

---

## 4. Scripting Logic from Claude Code

- 🧪 Logic has almost no AppleScript dictionary of its own. Everything works through **System Events / Accessibility** (UI scripting). VS Code needs **Accessibility** permission, plus **Automation** permission for each app it controls.
- 🧪 `open "<path>.logicx"` opens a project. It can't choose an alternative; that takes a File > Project Alternatives menu click.

| Capability | Status | Method |
|---|---|---|
| Which project is open | 🧪 | window title, or `AXDocument` attribute of window 1 (file URL) |
| Tempo / time sig / key / position | 🧪 | Control Bar: `Tempo` slider, `Time Signature` / `Key Signature` pop-ups, bar/beat sliders |
| Transport state | 🧪 | Control Bar checkboxes (`Play`, `Record`, `Cycle`, `Metronome Click`, `Count In`…), value 0/1 |
| Press transport buttons | 🧪 | `click` the checkbox. Metronome Click 0 → 1 → 0 worked with Logic in the background (2026-10-06) |
| Track list + mute state | 🧪 | `AXLayoutItem` elements, description `Track N “Name”[, mute]`, in the Tracks split group |
| Read bound shortcuts | 🧪 | menu items' `AXMenuItemCmdChar` / `AXMenuItemCmdModifiers` (bitmask: 0 = ⌘, +1 ⇧, +2 ⌥, +4 ⌃, +8 no ⌘) |
| Set Varispeed | ❓ | Control Bar element, once the button is shown (see §1) |
| Edit regions, plugins, routing | ⚠️ | possible by clicking through the UI but fragile; use templates/screensets instead |

Order of preference for triggering commands:
1. **Click the control bar button** (transport). Doesn't need focus, and the button reports its state afterwards.
2. **Click the menu item by name**. Works regardless of key bindings or which pane has focus.
3. **Keystroke**, only for commands that have neither. It goes to whichever pane has focus.
4. **MIDI via IAC + Learn New Assignment**. Most robust, but needs setup.

Gotchas:
- 🧪 `entire contents` on the whole window is slow. Scope it to the Tracks split group.
- 🧪 Submenus that Logic fills in when opened (e.g. File > Project Alternatives) read as empty until they're opened.
- 🧪 Finder aliases to `.logicx` projects couldn't be resolved by script. Store real paths.

### 4.1 Reading Logic's audio setup (read-only, 2026-10-11 🧪)

| What | Where | Value now |
|---|---|---|
| Audio device | `defaults read com.apple.logic10 AudioHardwarePreferences` | "Universal Audio Thunderbolt" (in and out) |
| Main output (I/O Assignments, Stereo Output) | `StereoOutputPair` in `com.apple.logic10` | **19**, a 0-based pair: driver outputs 39–40 = **B VIRTUAL 1/2** (Twin X virtual 1/2) |
| Main output mirroring | `StereoOutputMirroring` | 0 (off) |
| Low Latency Mode | `LowLatencyMode` | 0 (off) |
| Project sample rate | `<project>.logicx/Alternatives/NNN/MetaData.plist` `SampleRate` | 48000 (both alternatives of arbitrary-overlord) |
| UAD plugins used | `strings` on `Alternatives/NNN/ProjectData` | alt 001: UAD Teletronix LA-2A Silver, UAD Pure Plate, UAD dbx 160 |
| UAD-2 DSP vs Native | `/Library/Audio/Plug-Ins/Components/` | 224 `UAD …` (DSP) components, 0 `UADx …` (Native): every UAD plugin in Logic runs on Apollo/Satellite DSP |
| Console Recall | the same scans | installed (`Console Recall.component`), **not in this project** 🔶 (no match in ProjectData strings) |

- Logic shows only the **driver names** (I/O Matrix) for inputs and outputs, never Console labels (Tim).
- The new-track defaults are stored in the same plist (`InputIndex`, `OutputIndex`, `InputMonitoring` per track type). For example, Vocals defaults to InputIndex 34 = driver input 35 = B MIC/LINE/HIZ 1 (the Twin X's input 1).
- ❓ **Software Monitoring** (Settings > Audio > Devices) wasn't found in the plist. Read it from the settings UI, or find its key.
- 🔶 The open alternative of arbitrary-overlord ("arb-overlord-feb") is `001`: its folder changed when the project opened (22:59), and it has 17 tracks.
- ⚠️ Counting tracks via `entire contents` of the Tracks splitter group failed this time; the query needs revisiting.

---

## Tests to run

- [ ] Varispeed Speed Only at −20% on a song with a tempo map: confirm every section scales and the click stays in time.
- [ ] Read and set the Varispeed value via Accessibility once the button is shown.
- [ ] Metronome = K with the stock U.S. set.
- [ ] Copy Key Commands to Clipboard and save the output here as the authoritative map.
- [ ] Inspect `com.apple.logic.pro.cs` for existing controller assignments.
- [ ] `quit app` for non-session apps (Fastmail, Obsidian) via osascript.
