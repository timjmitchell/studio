# Arbitrary Overlord — Session Notes

Song-specific notes from probing the open Logic session via Claude Code + AppleScript.
Doubles as groundwork for a `/session <song>` skill that prepares the machine for a song.

General Logic knowledge (Varispeed, Flex & Follow, project alternatives, key commands,
scripting Logic) lives in [Logic Pro Field Notes](../../../data/manuals/daw-video/Logic-Pro-Field-Notes.md).

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

## Project alternatives (checked 2026-10-08)

On disk (`arbitrary-overlord.logicx/Alternatives/`):

| Folder | Likely name | Key | Last saved |
|---|---|---|---|
| `000` | Main | C major (template default?) | 2026-02-27 |
| `001` | arb-overlord-feb (open now) | C♯ minor | 2026-10-06 |

The names are inferred from key and date. The folder metadata has no name field.
See [Field Notes §2](../../../data/manuals/daw-video/Logic-Pro-Field-Notes.md#2-project-alternatives-not-workspace) for how alternatives work.

## For the `/session` skill

- All Logic projects live on the external drive `Samsung_X5` (`/Volumes/Samsung_X5/Hot Fog/`). Check it's mounted first.
- Store real project paths in each song README. Finder aliases couldn't be resolved by script.
- Opening `arbitrary-overlord.logicx` loads the last-used alternative. To get `arb-overlord-feb` for certain, pick it from File > Project Alternatives.
- Scripting methods and snippets are in [Field Notes §4](../../../data/manuals/daw-video/Logic-Pro-Field-Notes.md#4-scripting-logic-from-claude-code) and the snippets below.

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

Toggle the click (tested 2026-10-06):

```applescript
tell application "System Events" to tell process "Logic Pro"
	set cb to (first UI element of window 1 whose description is "Control Bar")
	click (first checkbox of cb whose name is "Metronome Click")
end tell
```

## Open questions

- Which apps should a session always keep (UAD Console, VE-500 Editor?) vs. quit (Fastmail, Obsidian?)
- Should the skill write a fresh snapshot here each session (tempo/key/tracks) to track how the song evolves?
