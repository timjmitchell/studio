# Arbitrary Overlord — Session Notes

Notes from probing the open Logic session via Claude Code + AppleScript (2026-10-06).
Doubles as groundwork for a `/session <song>` skill that prepares the machine for a song.

## Session snapshot (2026-10-06)

| | |
|---|---|
| Logic project | `/Volumes/Samsung_X5/Hot Fog/arbitrary-overlord.logicx` |
| Project alternative | `arb-overlord-feb` |
| Tempo | 122.02 BPM |
| Time signature | 4/4 |
| Key | C♯ minor |
| Playhead | bar 63 |

### Tracks

| # | Name | Notes |
|---|---|---|
| 1 | Abitrary_Overlord_2_28_26 | 2/28/26 bounce |
| 2 | Abitrary_Overlord_2_28_26 (Stems) | stem folder |
| 3 | … (Drums) | stem |
| 4 | … (Vocals) | stem, **muted** |
| 5 | … (Bass) | stem |
| 6 | … (Guitar) | stem |
| 7 | vox | |
| 8 | vox | |
| 9 | Inst 1 | |
| 10 | Guittim | |
| 11 | Guittim | |

Note: track names spell it "Abitrary" (missing r).

### Apps running alongside

UAD Console, UAD Meter & Control Panel, Native Access, Kontakt 8, VE-500 Editor,
Fastmail, Obsidian, Safari, Chrome, System Settings, Claude, VS Code.

## What automation can do

Logic Pro has almost no AppleScript dictionary. Everything below goes through
**System Events / Accessibility** (UI scripting), so VS Code needs Accessibility
permission (granted) and Automation permission per target app.

| Capability | Works | Method |
|---|---|---|
| Open a project | ✅ | `open "/Volumes/Samsung_X5/Hot Fog/<song>.logicx"` |
| Confirm which project is open | ✅ | window title, or `AXDocument` attribute of window 1 (returns file URL) |
| Read tempo / time sig / key / position | ✅ | Control Bar elements (`Tempo`, `Time Signature`, `Key Signature`, bar/beat sliders) |
| Read transport state (play, record, cycle, click, count-in) | ✅ | Control Bar checkboxes, value 0/1 |
| Read master volume | ✅ | `Master Volume` slider |
| List tracks + mute state | ✅ | `AXLayoutItem` elements with description `Track N “Name”[, mute]` in the Tracks split group |
| Press transport buttons | ✅ | `click` the Control Bar checkbox/button (preferred over keystrokes, see below). Tested 2026-10-06: Metronome Click 0 → 1 → 0, Logic in background |
| Quit other apps | ✅ (expected) | `osascript -e 'quit app "Name"'` — not yet tested |
| Open Google Docs/Drive | ✅ | `open "<url>"` |
| Edit regions, plugin params, routing | ⚠️ | possible via UI clicking but fragile — use templates/screensets instead |

### Keyboard shortcuts

Three ways to trigger Logic commands, most to least robust:

1. **Click the menu item by name.** `click menu item "Create Marker" of menu 1 of menu bar item "Navigate" of menu bar 1`.
   Works no matter what the key command is bound to or which pane has focus.
2. **Send the keystroke.** `keystroke "k"` / `key code 49` (space) with `using {command down, …}`.
   Simple, and covers commands that have no menu item (Play, Stop, Record, Metronome). But it fires into whatever pane has focus, and it breaks if the key commands get remapped.
3. **Control Surface / MIDI** (e.g. send MIDI CC via an IAC bus mapped in Logic). Most reliable for transport, but needs setup.

Bound shortcuts are readable from the menus via the `AXMenuItemCmdChar` and
`AXMenuItemCmdModifiers` attributes, so the skill can discover the current mapping rather than hardcoding it.
Modifier bitmask: `0` = ⌘, `+1` Shift, `+2` Option, `+4` Control, `+8` *no* ⌘.
Examples read 2026-10-06: Create Marker = ⌥' (10), New Audio Track = ⌥⌘A (2), Create Track Stack = ⇧⌘D (1).
Special keys (Delete, Return, arrows) show an empty char. They live in `AXMenuItemCmdVirtualKey`.
The Record menu reported no bindings this way. Transport keys (Space, R, K) are bound outside the menus.

#### Local key command state (checked 2026-10-06)

From `defaults read com.apple.logic10`:
- `lastSelectedKeyCommandsPath` = stock **U.S.** preset (`…/Resources/Key Commands/U.S..logikcs`)
- `lastSelectedKeyCommandsTouched = 0` and `…DeviateFromPreset… = 0`, so **no custom key commands**. The manual defaults apply.
- The path still says `Logic Pro X.app`, but the installed app is `Logic Pro.app`. This is a stale pref and looks harmless.
- `~/Music/Audio Music Apps/Key Commands/` (where saved/exported sets go) is empty.
- `~/Library/Preferences/com.apple.logic.pro.cs` (~75 KB, modified today) holds **control surface / controller assignments**. It wasn't inspected yet.

#### What the manual says (logic-pro-mac-user-guide.md)

- Default transport keys: **Space** = play/stop, **Return** = play/stop/go to start (§ Control bar buttons, line ~3473), **R** = record (~7237), **C** = cycle (~3797). Metronome is **K** by Logic convention (not confirmed in this manual).
- "Most of these transport key commands have no default assignment, and need to be assigned manually" (§ Use transport key commands, line 3565). Extras like Stop and Go to Left Locator need binding first.
- **Full dump:** Key Commands window (⌥K) → Action menu → *Copy Key Commands to Clipboard* gives every command and its binding as a spreadsheet-pasteable list (§ Export key commands to a spreadsheet, line ~40248). Do this once and save it here to get the authoritative map.
- **Learn New Assignment** (§ Learn a controller assignment): in the Key Commands window, select a command and send a MIDI message, and Logic binds it. This is the route for MIDI-over-IAC transport control from scripts.

#### Recommendation

For transport, **press the Control Bar buttons via accessibility** (`click checkbox "Play"`, `"Metronome Click"`, `"Cycle"` …). It doesn't depend on focus or key bindings, and the same element gives back its state for verification. Use menu-item clicks for menu commands. Use raw keystrokes only for commands that have neither.

Gotchas:
- `entire contents` on the whole window is slow; scope it to the Tracks split group.
- Finder aliases in song folders couldn't be resolved via AppleScript — store real paths in each song README.
- All Logic projects live on the external drive `Samsung_X5` (`/Volumes/Samsung_X5/Hot Fog/`); the skill should check it's mounted first.

## Snippets

Read the Control Bar:

```applescript
tell application "System Events" to tell process "Logic Pro"
	set cb to (first UI element of window 1 whose description is "Control Bar")
	-- tempo: value of (first slider of group 1 of cb whose description is "Tempo")
end tell
```

Project file path of the frontmost Logic window:

```applescript
tell application "System Events" to tell process "Logic Pro"
	value of attribute "AXDocument" of window 1
end tell
```

List tracks:

```applescript
tell application "System Events" to tell process "Logic Pro"
	repeat with g in (UI elements of window 1 whose role is "AXGroup")
		try
			set h to first UI element of g whose description is "Tracks"
			set s to first UI element of h whose role is "AXSplitGroup"
			-- filter entire contents of s: role "AXLayoutItem", description starts with "Track "
		end try
	end repeat
end tell
```

## Open questions

- Which apps should a session always keep (UAD Console, VE-500 Editor?) vs. quit (Fastmail, Obsidian?)
- Should the skill write a fresh snapshot here each session (tempo/key/tracks) to track how the song evolves?
