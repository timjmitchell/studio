Source: https://music21.org/music21docs/moduleReference/moduleAlphaAnalysisOrnamentRecognizer.html

# music21.alpha.analysis.ornamentRecognizer

## OrnamentRecognizer

class music21.alpha.analysis.ornamentRecognizer.OrnamentRecognizer[[source]](../_modules/music21/alpha/analysis/ornamentRecognizer.html#OrnamentRecognizer)
:   An object to identify if a stream of notes is an expanded ornament.
    Busy notes refer to the expanded ornament notes.
    Simple note(s) refer to the base note of ornament which is often shown
    with the ornament marking on it.

[`OrnamentRecognizer`](#music21.alpha.analysis.ornamentRecognizer.OrnamentRecognizer "music21.alpha.analysis.ornamentRecognizer.OrnamentRecognizer") methods

OrnamentRecognizer.calculateOrnamentNoteQl(*busyNotes*, *simpleNotes=None*)[[source]](../_modules/music21/alpha/analysis/ornamentRecognizer.html#OrnamentRecognizer.calculateOrnamentNoteQl)
:   Finds the quarter length value for each ornament note
    assuming busy notes all are an expanded ornament.

    Expanded ornament total duration is time of all busy notes combined or
    duration of the first note in simpleNotes when provided.

OrnamentRecognizer.calculateOrnamentTotalQl(*busyNotes: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[GeneralNote](moduleNote.html#music21.note.GeneralNote "music21.note.GeneralNote")]*, *simpleNotes: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[GeneralNote](moduleNote.html#music21.note.GeneralNote "music21.note.GeneralNote")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [Fraction](https://docs.python.org/3/library/fractions.html#fractions.Fraction "(in Python v3.14)")[[source]](../_modules/music21/alpha/analysis/ornamentRecognizer.html#OrnamentRecognizer.calculateOrnamentTotalQl)
:   Returns total length of trill assuming busy notes are all an expanded trill.
    This is either the time of all busy notes combined or
    duration of the first note in simpleNotes when provided.

## TrillRecognizer

class music21.alpha.analysis.ornamentRecognizer.TrillRecognizer(*checkNachschlag=False*)[[source]](../_modules/music21/alpha/analysis/ornamentRecognizer.html#TrillRecognizer)
:   An object to identify if a stream of (“busy”) notes is an expanded trill.

    By default, does not consider Nachschlag trills, but setting checkNachschlag will consider.

    When optional stream of simpleNotes are provided, considers if busyNotes are
    an expansion of a trill which would be denoted on the first note in simpleNotes.

[`TrillRecognizer`](#music21.alpha.analysis.ornamentRecognizer.TrillRecognizer "music21.alpha.analysis.ornamentRecognizer.TrillRecognizer") bases

* [`OrnamentRecognizer`](#music21.alpha.analysis.ornamentRecognizer.OrnamentRecognizer "music21.alpha.analysis.ornamentRecognizer.OrnamentRecognizer")

[`TrillRecognizer`](#music21.alpha.analysis.ornamentRecognizer.TrillRecognizer "music21.alpha.analysis.ornamentRecognizer.TrillRecognizer") methods

TrillRecognizer.recognize(*busyNotes*, *simpleNotes=None*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [Trill](moduleExpressions.html#music21.expressions.Trill "music21.expressions.Trill")[[source]](../_modules/music21/alpha/analysis/ornamentRecognizer.html#TrillRecognizer.recognize)
:   Tries to identify the busy notes as a trill.

    When simple notes is provided, tries to identify busy notes
    as the trill shortened by simple notes.
    Currently only supports one simple note in simple notes.

    Only when checkNachschlag is true, allows last few notes to break trill rules.

    Trill interval size is interval between busy notes.

    Returns: False if not possible or the Trill Expression

Methods inherited from [`OrnamentRecognizer`](#music21.alpha.analysis.ornamentRecognizer.OrnamentRecognizer "music21.alpha.analysis.ornamentRecognizer.OrnamentRecognizer"):

|  |  |  |
| --- | --- | --- |
| * [`calculateOrnamentNoteQl()`](#music21.alpha.analysis.ornamentRecognizer.OrnamentRecognizer.calculateOrnamentNoteQl "music21.alpha.analysis.ornamentRecognizer.OrnamentRecognizer.calculateOrnamentNoteQl") | * [`calculateOrnamentTotalQl()`](#music21.alpha.analysis.ornamentRecognizer.OrnamentRecognizer.calculateOrnamentTotalQl "music21.alpha.analysis.ornamentRecognizer.OrnamentRecognizer.calculateOrnamentTotalQl") |  |

## TurnRecognizer

class music21.alpha.analysis.ornamentRecognizer.TurnRecognizer[[source]](../_modules/music21/alpha/analysis/ornamentRecognizer.html#TurnRecognizer)

[`TurnRecognizer`](#music21.alpha.analysis.ornamentRecognizer.TurnRecognizer "music21.alpha.analysis.ornamentRecognizer.TurnRecognizer") bases

* [`OrnamentRecognizer`](#music21.alpha.analysis.ornamentRecognizer.OrnamentRecognizer "music21.alpha.analysis.ornamentRecognizer.OrnamentRecognizer")

[`TurnRecognizer`](#music21.alpha.analysis.ornamentRecognizer.TurnRecognizer "music21.alpha.analysis.ornamentRecognizer.TurnRecognizer") methods

TurnRecognizer.isAcceptableInterval(*intervalToCheck: [Interval](moduleInterval.html#music21.interval.Interval "music21.interval.Interval")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/alpha/analysis/ornamentRecognizer.html#TurnRecognizer.isAcceptableInterval)
:   Returns whether that interval can occur in a turn

TurnRecognizer.recognize(*busyNotes*, *simpleNotes=None*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [Turn](moduleExpressions.html#music21.expressions.Turn "music21.expressions.Turn") | [InvertedTurn](moduleExpressions.html#music21.expressions.InvertedTurn "music21.expressions.InvertedTurn")[[source]](../_modules/music21/alpha/analysis/ornamentRecognizer.html#TurnRecognizer.recognize)
:   Tries to identify the busy notes as a turn or inverted turn.

    When simple notes is provided, tries to identify busy notes
    as the turn shortened by simple notes.
    Currently only supports one simple note in simple notes.

    Turns and inverted turns have four notes separated by m2, M2, A2.

    Turns:
    start above base note
    go down to base note,
    go down again,
    and go back up to base note

    Inverted Turns:
    start below base note
    go up to base note,
    go up again,
    and go back down to base note

    When going up or down, must go to the adjacent note name,
    so A goes down to G, G#, G flat, G##, etc

    Returns: False if not possible or the Turn/Inverted Turn Expression

Methods inherited from [`OrnamentRecognizer`](#music21.alpha.analysis.ornamentRecognizer.OrnamentRecognizer "music21.alpha.analysis.ornamentRecognizer.OrnamentRecognizer"):

|  |  |  |
| --- | --- | --- |
| * [`calculateOrnamentNoteQl()`](#music21.alpha.analysis.ornamentRecognizer.OrnamentRecognizer.calculateOrnamentNoteQl "music21.alpha.analysis.ornamentRecognizer.OrnamentRecognizer.calculateOrnamentNoteQl") | * [`calculateOrnamentTotalQl()`](#music21.alpha.analysis.ornamentRecognizer.OrnamentRecognizer.calculateOrnamentTotalQl "music21.alpha.analysis.ornamentRecognizer.OrnamentRecognizer.calculateOrnamentTotalQl") |  |

## Functions

music21.alpha.analysis.ornamentRecognizer.calculateTrillNoteDuration(*numTrillNotes*, *totalDuration*)[[source]](../_modules/music21/alpha/analysis/ornamentRecognizer.html#calculateTrillNoteDuration)
