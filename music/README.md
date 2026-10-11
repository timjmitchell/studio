# music/

My projects and their songs. This is where I work.

```text
music/
  <project>/                 hot-fog, one-man-band, …
    README.md                the project: what it is, links, song list
    <song>/                  one folder per song, named with a slug (the-killing-moon)
      <song>.md              the song doc: frontmatter + links (source of truth)
      lyrics.md              lyrics, if any
      *-chords.md, *-tab.md  charts and tabs
      midi/                  MIDI and MusicXML, with readable text dumps
      session-notes.md       notes from working sessions (dated observations)
    _inbox/                  files not yet sorted into a song
```

## The song doc

Every song folder has `<song>.md` with YAML frontmatter:

| Field | Meaning |
|---|---|
| `type` | `song` |
| `title` | The song's title |
| `artist` | Covers: the original artist. Originals: the project |
| `project` | `hot-fog`, `one-man-band`, … |
| `version` | `cover` or `original` (our take on the song; see the [model](../docs/studio/model.md) §5) |
| `status` | `idea` · `demo` · `arranging` · `tracking` · `mixing` · `done` |
| `key`, `tuning`, `capo`, `tempo`, `time_signature` | The musical facts of *our* version |
| `logic`, `drive`, `lyrics` | Where the session, the Drive folders and the canonical lyrics live (Hot Fog) |

The song doc wins over session notes or the Logic project if they disagree.

## Adding a song

1. Make a folder: `music/<project>/<song-slug>/`.
2. Copy an existing song doc into it as `<song-slug>.md` and fill in what you know. Leave
   blanks blank.
3. Drop lyrics, charts and MIDI next to it.
4. Add it to the project's `README.md`.
