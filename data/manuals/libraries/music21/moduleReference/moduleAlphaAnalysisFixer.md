Source: https://music21.org/music21docs/moduleReference/moduleAlphaAnalysisFixer.html

# music21.alpha.analysis.fixer

## DeleteFixer

class music21.alpha.analysis.fixer.DeleteFixer(*changes*, *midiStream*, *omrStream*)[[source]](../_modules/music21/alpha/analysis/fixer.html#DeleteFixer)
:   The DeleteFixer was designed to fit the specifications of the OpenScore project.
    The goal of the OpenScore project is to open-source music with open source software
    (like music21!). OpenScore will use a combination of computer and human power
    to digitize classical music scores and put them in the public domain. One idea is
    that software can identify wrong recognized notes in a scanned score and mark or
    delete the entire measure that that note is in and pass it off to a human corrector to
    re-transcribe the entire measure. The DeleteFixer could be the computer power in
    this method of score correction that OpenScore is using.

    CAUTION: this does really weird things still.

[`DeleteFixer`](#music21.alpha.analysis.fixer.DeleteFixer "music21.alpha.analysis.fixer.DeleteFixer") bases

* [`OMRMidiFixer`](#music21.alpha.analysis.fixer.OMRMidiFixer "music21.alpha.analysis.fixer.OMRMidiFixer")

[`DeleteFixer`](#music21.alpha.analysis.fixer.DeleteFixer "music21.alpha.analysis.fixer.DeleteFixer") methods

DeleteFixer.fix()[[source]](../_modules/music21/alpha/analysis/fixer.html#DeleteFixer.fix)

Methods inherited from [`OMRMidiFixer`](#music21.alpha.analysis.fixer.OMRMidiFixer "music21.alpha.analysis.fixer.OMRMidiFixer"):

|  |  |  |
| --- | --- | --- |
| * [`checkIfNoteInstance()`](#music21.alpha.analysis.fixer.OMRMidiFixer.checkIfNoteInstance "music21.alpha.analysis.fixer.OMRMidiFixer.checkIfNoteInstance") |  |  |

## EnharmonicFixer

class music21.alpha.analysis.fixer.EnharmonicFixer(*changes*, *midiStream*, *omrStream*)[[source]](../_modules/music21/alpha/analysis/fixer.html#EnharmonicFixer)
:   Fixes incorrectly spelled enharmonics
    initialized with self.changes – a list of tuples in this form:
    (MIDIReference, OMRReference, op)
    MIDIReference and OMRReference are actual note/rest/chord object in some stream
    op is a ChangeOp that relates the two references

    TEST 1, no changes in OMR stream

    ```python
    >>> omrStream1 = stream.Stream()
    >>> midiStream1 = stream.Stream()
    ```

    ```python
    >>> omrNote1 = note.Note('A#4')
    >>> omrNote2 = note.Note('A#4')
    >>> midiNote1 = note.Note('B-4')
    >>> midiNote2 = note.Note('B-4')
    ```

    ```python
    >>> omrStream1.append([omrNote1, omrNote2])
    >>> midiStream1.append([midiNote1, midiNote2])
    >>> subOp = alpha.analysis.aligner.ChangeOps.Substitution
    ```

    ```python
    >>> ct1 = (midiNote1, omrNote1, subOp)
    >>> ct2 = (midiNote2, omrNote2, subOp)
    >>> changes1 = [ct1, ct2]
    ```

    ```python
    >>> fixer1 = alpha.analysis.fixer.EnharmonicFixer(changes1, None, None)
    >>> fixer1.fix()
    >>> omrStream1[0]
    <music21.note.Note A#>
    >>> omrStream1[1]
    <music21.note.Note A#>
    ```

    TEST 2, no changes in OMR stream

    ```python
    >>> omrStream2 = stream.Stream()
    >>> midiStream2 = stream.Stream()
    ```

    ```python
    >>> omr2Note1 = note.Note('A#4')
    >>> omr2Note2 = note.Note('A#4')
    >>> midi2Note1 = note.Note('A#4')
    >>> midi2Note2 = note.Note('A#4')
    ```

    ```python
    >>> omrStream2.append([omr2Note1, omr2Note2])
    >>> midiStream2.append([midi2Note1, midi2Note2])
    >>> ncOp = alpha.analysis.aligner.ChangeOps.NoChange
    ```

    ```python
    >>> ct2_1 = (midi2Note1, omr2Note1, ncOp)
    >>> ct2_2 = (midi2Note2, omr2Note2, ncOp)
    >>> changes2 = [ct2_1, ct2_2]
    ```

    ```python
    >>> fixer2 = alpha.analysis.fixer.EnharmonicFixer(changes2, None, None)
    >>> fixer2.fix()
    >>> omrStream2[0]
    <music21.note.Note A#>
    >>> omrStream1[1]
    <music21.note.Note A#>
    ```

    TEST 3 (case 1)

    ```python
    >>> midiNote3 = note.Note('A4')
    >>> omrNote3 = note.Note('An4')
    ```

    ```python
    >>> subOp = alpha.analysis.aligner.ChangeOps.Substitution
    ```

    ```python
    >>> ct3 = (midiNote3, omrNote3, subOp)
    >>> changes3 = [ct3]
    >>> omrNote3.pitch.accidental
    <music21.pitch.Accidental natural>
    >>> fixer3 = alpha.analysis.fixer.EnharmonicFixer(changes3, None, None)
    >>> fixer3.fix()
    >>> omrNote3.pitch.accidental
    ```

    TEST 4 (case 2-1) e.g MIDI = g#, ground truth = a-, OMR = an

    ```python
    >>> midiNote4 = note.Note('G#4')
    >>> omrNote4 = note.Note('An4')
    ```

    ```python
    >>> subOp = alpha.analysis.aligner.ChangeOps.Substitution
    ```

    ```python
    >>> ct4 = (midiNote4, omrNote4, subOp)
    >>> changes4 = [ct4]
    >>> omrNote4.pitch.accidental
    <music21.pitch.Accidental natural>
    >>> fixer4 = alpha.analysis.fixer.EnharmonicFixer(changes4, None, None)
    >>> fixer4.fix()
    >>> omrNote4.pitch.accidental
    <music21.pitch.Accidental flat>
    ```

    TEST 5 (case 2-2) e.g midi = g-, gt = f#, omr = fn

    ```python
    >>> midiNote5 = note.Note('G-4')
    >>> omrNote5 = note.Note('Fn4')
    ```

    ```python
    >>> subOp = alpha.analysis.aligner.ChangeOps.Substitution
    ```

    ```python
    >>> ct5 = (midiNote5, omrNote5, subOp)
    >>> changes5 = [ct5]
    >>> omrNote5.pitch.accidental
    <music21.pitch.Accidental natural>
    >>> fixer5 = alpha.analysis.fixer.EnharmonicFixer(changes5, None, None)
    >>> fixer5.fix()
    >>> omrNote5.pitch.accidental
    <music21.pitch.Accidental sharp>
    ```

    TEST 6.1 (case 3) e.g. midi = g#, gt = g#, omr = gn or omr = g-

    ```python
    >>> midiNote6_1 = note.Note('G#4')
    >>> midiNote6_2 = note.Note('G#4')
    >>> omrNote6_1 = note.Note('Gn4')
    >>> omrNote6_2 = note.Note('G-4')
    ```

    ```python
    >>> subOp6_1 = alpha.analysis.aligner.ChangeOps.Substitution
    >>> subOp6_2 = alpha.analysis.aligner.ChangeOps.Substitution
    >>> ct6_1 = (midiNote6_1, omrNote6_1, subOp6_1)
    >>> ct6_2 = (midiNote6_2, omrNote6_2, subOp6_2)
    >>> changes6 = [ct6_1, ct6_2]
    ```

    ```python
    >>> omrNote6_1.pitch.accidental
    <music21.pitch.Accidental natural>
    >>> omrNote6_2.pitch.accidental
    <music21.pitch.Accidental flat>
    >>> fixer6 = alpha.analysis.fixer.EnharmonicFixer(changes6, None, None)
    >>> fixer6.fix()
    >>> omrNote6_1.pitch.accidental
    <music21.pitch.Accidental sharp>
    >>> omrNote6_2.pitch.accidental
    <music21.pitch.Accidental sharp>
    ```

    TEST 7 (case 4-1, 4-2) notes are on different step, off by an interval of 2:
    \* 4-1: e.g. midi = g#, gt = a-, omr = a#
    \* 4-2: e.g. midi = a-, gt = g#, omr = g-

    ```python
    >>> midiNote7_1 = note.Note('G#4')
    >>> omrNote7_1 = note.Note('A#4')
    ```

    ```python
    >>> midiNote7_2 = note.Note('A-4')
    >>> omrNote7_2 = note.Note('G-4')
    ```

    ```python
    >>> subOp7_1 = alpha.analysis.aligner.ChangeOps.Substitution
    >>> subOp7_2 = alpha.analysis.aligner.ChangeOps.Substitution
    >>> ct7_1 = (midiNote7_1, omrNote7_1, subOp7_1)
    >>> ct7_2 = (midiNote7_2, omrNote7_2, subOp7_2)
    >>> changes7 = [ct7_1, ct7_2]
    ```

    ```python
    >>> omrNote7_1.pitch.accidental
    <music21.pitch.Accidental sharp>
    >>> omrNote7_2.pitch.accidental
    <music21.pitch.Accidental flat>
    >>> fixer7 = alpha.analysis.fixer.EnharmonicFixer(changes7, None, None)
    >>> fixer7.fix()
    ```

    ```python
    >>> omrNote7_1.pitch.step
    'A'
    >>> omrNote7_1.pitch.accidental
    <music21.pitch.Accidental flat>
    ```

    ```python
    >>> omrNote7_2.pitch.step
    'G'
    >>> omrNote7_2.pitch.accidental
    <music21.pitch.Accidental sharp>
    ```

[`EnharmonicFixer`](#music21.alpha.analysis.fixer.EnharmonicFixer "music21.alpha.analysis.fixer.EnharmonicFixer") bases

* [`OMRMidiFixer`](#music21.alpha.analysis.fixer.OMRMidiFixer "music21.alpha.analysis.fixer.OMRMidiFixer")

[`EnharmonicFixer`](#music21.alpha.analysis.fixer.EnharmonicFixer "music21.alpha.analysis.fixer.EnharmonicFixer") methods

EnharmonicFixer.fix()[[source]](../_modules/music21/alpha/analysis/fixer.html#EnharmonicFixer.fix)
:   Fixes the enharmonic errors in the OMR by changing the pitch of the note.

EnharmonicFixer.hasAcc(*omrRef*)[[source]](../_modules/music21/alpha/analysis/fixer.html#EnharmonicFixer.hasAcc)
:   Returns True if the omrRef has an accidental, False otherwise

EnharmonicFixer.hasNatAcc(*omrRef*)[[source]](../_modules/music21/alpha/analysis/fixer.html#EnharmonicFixer.hasNatAcc)
:   Returns True if the omrRef has a natural accidental, False otherwise

EnharmonicFixer.hasSharpFlatAcc(*omrRef*)[[source]](../_modules/music21/alpha/analysis/fixer.html#EnharmonicFixer.hasSharpFlatAcc)
:   Returns True if the omrRef has a sharp or flat accidental, False otherwise

EnharmonicFixer.intervalTooBig(*midiRef*, *omrRef*, *setInt=5*)[[source]](../_modules/music21/alpha/analysis/fixer.html#EnharmonicFixer.intervalTooBig)
:   Returns True if the intervalClass between the two notes is greater than setInt.

    Note that intervalClass and not actual interval size is used.

EnharmonicFixer.isEnharmonic(*midiRef*, *omrRef*)[[source]](../_modules/music21/alpha/analysis/fixer.html#EnharmonicFixer.isEnharmonic)
:   Returns True if the omrRef is enharmonic to the midiRef, False otherwise

EnharmonicFixer.stepEq(*midiRef*, *omrRef*)[[source]](../_modules/music21/alpha/analysis/fixer.html#EnharmonicFixer.stepEq)
:   Returns True if the steps are equal, False otherwise

EnharmonicFixer.stepNotEq(*midiRef*, *omrRef*)[[source]](../_modules/music21/alpha/analysis/fixer.html#EnharmonicFixer.stepNotEq)
:   Returns True if the steps are not equal, False otherwise

Methods inherited from [`OMRMidiFixer`](#music21.alpha.analysis.fixer.OMRMidiFixer "music21.alpha.analysis.fixer.OMRMidiFixer"):

|  |  |  |
| --- | --- | --- |
| * [`checkIfNoteInstance()`](#music21.alpha.analysis.fixer.OMRMidiFixer.checkIfNoteInstance "music21.alpha.analysis.fixer.OMRMidiFixer.checkIfNoteInstance") |  |  |

## OMRMidiFixer

class music21.alpha.analysis.fixer.OMRMidiFixer(*changes*, *midiStream*, *omrStream*)[[source]](../_modules/music21/alpha/analysis/fixer.html#OMRMidiFixer)
:   Base class for future fixers
    changes is a list of changes associated with the midiStream and omrStream,
    not a list of lists

[`OMRMidiFixer`](#music21.alpha.analysis.fixer.OMRMidiFixer "music21.alpha.analysis.fixer.OMRMidiFixer") methods

OMRMidiFixer.checkIfNoteInstance(*midiRef*, *omrRef*)[[source]](../_modules/music21/alpha/analysis/fixer.html#OMRMidiFixer.checkIfNoteInstance)

OMRMidiFixer.fix()[[source]](../_modules/music21/alpha/analysis/fixer.html#OMRMidiFixer.fix)

## OrnamentFixer

class music21.alpha.analysis.fixer.OrnamentFixer(*changes*, *midiStream*, *omrStream*, *recognizers*, *markChangeColor='blue'*)[[source]](../_modules/music21/alpha/analysis/fixer.html#OrnamentFixer)
:   Fixes missed ornaments in OMR using expanded ornaments in MIDI
    initialized with self.changes – a list of tuples in this form:
    (MIDIReference, OMRReference, op)
    MIDIReference and OMRReference are actual note/rest/chord object in some stream
    op is a ChangeOp that relates the two references

    recognizers can be a single recognizer or list of recognizers,
    but self.recognizers is always a list.
    recognizers take in stream of busy notes and optional stream of simple note(s)
    and return False or an instance of the ornament recognized

[`OrnamentFixer`](#music21.alpha.analysis.fixer.OrnamentFixer "music21.alpha.analysis.fixer.OrnamentFixer") bases

* [`OMRMidiFixer`](#music21.alpha.analysis.fixer.OMRMidiFixer "music21.alpha.analysis.fixer.OMRMidiFixer")

[`OrnamentFixer`](#music21.alpha.analysis.fixer.OrnamentFixer "music21.alpha.analysis.fixer.OrnamentFixer") methods

OrnamentFixer.addOrnament(*selectedNote: [Note](moduleNote.html#music21.note.Note "music21.note.Note")*, *ornament: [Ornament](moduleExpressions.html#music21.expressions.Ornament "music21.expressions.Ornament")*, *\**, *show=False*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/alpha/analysis/fixer.html#OrnamentFixer.addOrnament)
:   Adds the ornament to the selectedNote when selectedNote has no ornaments already.

    * selectedNote: Note.note to add ornament to
    * ornament: Expressions.ornament to add to note
    * show: True when note should be colored blue

    Returns True if added successfully, or False if there was already an
    ornament on the note and it wasn’t added.

OrnamentFixer.findOrnament(*busyNotes*, *simpleNotes*) → [Ornament](moduleExpressions.html#music21.expressions.Ornament "music21.expressions.Ornament") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/alpha/analysis/fixer.html#OrnamentFixer.findOrnament)
:   Finds an ornament in busyNotes based from simpleNote
    using provided recognizers.

    Parameters:
    :   * **busyNotes** – stream of notes
        * **simpleNotes** – stream of notes

    Tries the recognizers in order, returning the result of the first
    one to successfully recognize an ornament.

OrnamentFixer.fix(*\**, *show=False*, *inPlace=True*) → [OMRMidiFixer](#music21.alpha.analysis.fixer.OMRMidiFixer "music21.alpha.analysis.fixer.OMRMidiFixer") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/alpha/analysis/fixer.html#OrnamentFixer.fix)
:   Corrects missed ornaments in omrStream according to midiStream
    :param show: Whether to show results
    :param inPlace: Whether to make changes to own omr stream or
    return a new OrnamentFixer with changes

Methods inherited from [`OMRMidiFixer`](#music21.alpha.analysis.fixer.OMRMidiFixer "music21.alpha.analysis.fixer.OMRMidiFixer"):

|  |  |  |
| --- | --- | --- |
| * [`checkIfNoteInstance()`](#music21.alpha.analysis.fixer.OMRMidiFixer.checkIfNoteInstance "music21.alpha.analysis.fixer.OMRMidiFixer.checkIfNoteInstance") |  |  |

## TrillFixer

class music21.alpha.analysis.fixer.TrillFixer(*changes*, *midiStream*, *omrStream*)[[source]](../_modules/music21/alpha/analysis/fixer.html#TrillFixer)
:   Fixes missed trills in OMR using expanded ornaments in MIDI.
    initialized with self.changes – a list of tuples in this form:
    (MIDIReference, OMRReference, op)
    MIDIReference and OMRReference are actual note/rest/chord object in some stream
    op is a ChangeOp that relates the two references

[`TrillFixer`](#music21.alpha.analysis.fixer.TrillFixer "music21.alpha.analysis.fixer.TrillFixer") bases

* [`OrnamentFixer`](#music21.alpha.analysis.fixer.OrnamentFixer "music21.alpha.analysis.fixer.OrnamentFixer")
* [`OMRMidiFixer`](#music21.alpha.analysis.fixer.OMRMidiFixer "music21.alpha.analysis.fixer.OMRMidiFixer")

[`TrillFixer`](#music21.alpha.analysis.fixer.TrillFixer "music21.alpha.analysis.fixer.TrillFixer") methods

Methods inherited from [`OrnamentFixer`](#music21.alpha.analysis.fixer.OrnamentFixer "music21.alpha.analysis.fixer.OrnamentFixer"):

|  |  |  |
| --- | --- | --- |
| * [`addOrnament()`](#music21.alpha.analysis.fixer.OrnamentFixer.addOrnament "music21.alpha.analysis.fixer.OrnamentFixer.addOrnament") | * [`findOrnament()`](#music21.alpha.analysis.fixer.OrnamentFixer.findOrnament "music21.alpha.analysis.fixer.OrnamentFixer.findOrnament") | * [`fix()`](#music21.alpha.analysis.fixer.OrnamentFixer.fix "music21.alpha.analysis.fixer.OrnamentFixer.fix") |

Methods inherited from [`OMRMidiFixer`](#music21.alpha.analysis.fixer.OMRMidiFixer "music21.alpha.analysis.fixer.OMRMidiFixer"):

|  |  |  |
| --- | --- | --- |
| * [`checkIfNoteInstance()`](#music21.alpha.analysis.fixer.OMRMidiFixer.checkIfNoteInstance "music21.alpha.analysis.fixer.OMRMidiFixer.checkIfNoteInstance") |  |  |

## TurnFixer

class music21.alpha.analysis.fixer.TurnFixer(*changes*, *midiStream*, *omrStream*)[[source]](../_modules/music21/alpha/analysis/fixer.html#TurnFixer)
:   Fixes missed turns/inverted turns in OMR using expanded ornaments in MIDI.
    initialized with self.changes – a list of tuples in this form:
    (MIDIReference, OMRReference, op)
    MIDIReference and OMRReference are actual note/rest/chord object in some stream
    op is a ChangeOp that relates the two references

[`TurnFixer`](#music21.alpha.analysis.fixer.TurnFixer "music21.alpha.analysis.fixer.TurnFixer") bases

* [`OrnamentFixer`](#music21.alpha.analysis.fixer.OrnamentFixer "music21.alpha.analysis.fixer.OrnamentFixer")
* [`OMRMidiFixer`](#music21.alpha.analysis.fixer.OMRMidiFixer "music21.alpha.analysis.fixer.OMRMidiFixer")

[`TurnFixer`](#music21.alpha.analysis.fixer.TurnFixer "music21.alpha.analysis.fixer.TurnFixer") methods

Methods inherited from [`OrnamentFixer`](#music21.alpha.analysis.fixer.OrnamentFixer "music21.alpha.analysis.fixer.OrnamentFixer"):

|  |  |  |
| --- | --- | --- |
| * [`addOrnament()`](#music21.alpha.analysis.fixer.OrnamentFixer.addOrnament "music21.alpha.analysis.fixer.OrnamentFixer.addOrnament") | * [`findOrnament()`](#music21.alpha.analysis.fixer.OrnamentFixer.findOrnament "music21.alpha.analysis.fixer.OrnamentFixer.findOrnament") | * [`fix()`](#music21.alpha.analysis.fixer.OrnamentFixer.fix "music21.alpha.analysis.fixer.OrnamentFixer.fix") |

Methods inherited from [`OMRMidiFixer`](#music21.alpha.analysis.fixer.OMRMidiFixer "music21.alpha.analysis.fixer.OMRMidiFixer"):

|  |  |  |
| --- | --- | --- |
| * [`checkIfNoteInstance()`](#music21.alpha.analysis.fixer.OMRMidiFixer.checkIfNoteInstance "music21.alpha.analysis.fixer.OMRMidiFixer.checkIfNoteInstance") |  |  |

## Functions

music21.alpha.analysis.fixer.getNotesWithinDuration(*startingGeneralNote*, *totalDuration*, *referenceStream=None*)[[source]](../_modules/music21/alpha/analysis/fixer.html#getNotesWithinDuration)
:   Returns maximal stream of deepcopies of notes, rests, and chords following
    (and including) startingNote which occupy no more than totalDuration combined.

    * startingGeneralNote is a GeneralNote (could be a note, rest, or chord)
    * totalDuration is a duration
    * referenceStream is optionally a stream which the startingGeneralNote’s
      :   active site should be set to when provided
