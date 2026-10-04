Source: https://music21.org/music21docs/moduleReference/moduleBrailleNoteGrouping.html

# music21.braille.noteGrouping

## NoteGroupingTranscriber

class music21.braille.noteGrouping.NoteGroupingTranscriber(*brailleElementGrouping=None*)[[source]](../_modules/music21/braille/noteGrouping.html#NoteGroupingTranscriber)
:   Object that can transcribe note groupings.

[`NoteGroupingTranscriber`](#music21.braille.noteGrouping.NoteGroupingTranscriber "music21.braille.noteGrouping.NoteGroupingTranscriber") read/write properties

NoteGroupingTranscriber.showClefSigns
:   Generally, in Braille, clef signs are not used. However, they
    can be shown for pedagogical purposes or to make a facsimile
    transcription of the sighted text.

    If not set but self.brailleElementGrouping.showClefSigns
    is set, uses that instead.

    ```python
    >>> ngt = braille.noteGrouping.NoteGroupingTranscriber()
    >>> ngt.showClefSigns
    False
    >>> beg = braille.segment.BrailleElementGrouping()
    >>> ngt.brailleElementGrouping = beg
    >>> ngt.showClefSigns
    False
    >>> beg.showClefSigns = True
    >>> ngt.showClefSigns
    True
    >>> ngt.showClefSigns = False
    >>> ngt.showClefSigns
    False
    ```

NoteGroupingTranscriber.upperFirstInFingering
:   When there are multiple fingering patterns listed at the same time,
    should the highest be listed first (default True) or last?

    If not set but self.brailleElementGrouping.upperFirstInNoteFingering
    is set, uses that instead. (note the slight difference in names: NoteFingering)

    ```python
    >>> ngt = braille.noteGrouping.NoteGroupingTranscriber()
    >>> ngt.upperFirstInFingering
    True
    >>> beg = braille.segment.BrailleElementGrouping()
    >>> ngt.brailleElementGrouping = beg
    >>> ngt.upperFirstInFingering
    True
    >>> beg.upperFirstInNoteFingering = False
    >>> ngt.upperFirstInFingering
    False
    >>> ngt.upperFirstInFingering = True
    >>> ngt.upperFirstInFingering
    True
    ```

[`NoteGroupingTranscriber`](#music21.braille.noteGrouping.NoteGroupingTranscriber "music21.braille.noteGrouping.NoteGroupingTranscriber") methods

NoteGroupingTranscriber.optionallyAddDotToPrevious(*el=None*)[[source]](../_modules/music21/braille/noteGrouping.html#NoteGroupingTranscriber.optionallyAddDotToPrevious)
:   if el is None or not a Dynamic or TextExpression, add a dot-3 Dot
    before the current transcription
    under certain circumstances:

    1. self.previousElement exists
    2. the last character in the current transcription (self.trans) fits the criteria for
       basic.yieldDots()
    3. one of these three. PreviousElement was:
       :   1. a Dynamic.
           2. a Clef and clef signs are being transcribed
           3. a TextExpression not ending in “.”

    Returns True if a dot as added, or False otherwise.

NoteGroupingTranscriber.reset()[[source]](../_modules/music21/braille/noteGrouping.html#NoteGroupingTranscriber.reset)

NoteGroupingTranscriber.transcribeGroup(*brailleElementGrouping=None*)[[source]](../_modules/music21/braille/noteGrouping.html#NoteGroupingTranscriber.transcribeGroup)
:   transcribe a group of notes, possibly excluding certain attributes.

    Returns a (unicode) string of brailleElementGrouping transcribed.

NoteGroupingTranscriber.transcribeOneElement(*el*)[[source]](../_modules/music21/braille/noteGrouping.html#NoteGroupingTranscriber.transcribeOneElement)
:   Transcribe a single element and add it to self.trans, setting self.previousElement
    along the way.

    ```python
    >>> ngt = braille.noteGrouping.NoteGroupingTranscriber()
    >>> n = note.Note('C4')
    >>> ngt.transcribeOneElement(n)
    >>> ''.join(ngt.trans)
    '⠐⠹'
    >>> ngt.previousElement
    <music21.note.Note C>
    ```

NoteGroupingTranscriber.translateBarline(*currentBarline*)[[source]](../_modules/music21/braille/noteGrouping.html#NoteGroupingTranscriber.translateBarline)

NoteGroupingTranscriber.translateChord(*currentChord*)[[source]](../_modules/music21/braille/noteGrouping.html#NoteGroupingTranscriber.translateChord)

NoteGroupingTranscriber.translateClef(*currentClef*)[[source]](../_modules/music21/braille/noteGrouping.html#NoteGroupingTranscriber.translateClef)
:   translate Clefs to braille IF self.showClefSigns is True

NoteGroupingTranscriber.translateDynamic(*currentDynamic*)[[source]](../_modules/music21/braille/noteGrouping.html#NoteGroupingTranscriber.translateDynamic)

NoteGroupingTranscriber.translateNote(*currentNote*)[[source]](../_modules/music21/braille/noteGrouping.html#NoteGroupingTranscriber.translateNote)

NoteGroupingTranscriber.translateRest(*currentRest*)[[source]](../_modules/music21/braille/noteGrouping.html#NoteGroupingTranscriber.translateRest)

NoteGroupingTranscriber.translateTextExpression(*currentExpression*)[[source]](../_modules/music21/braille/noteGrouping.html#NoteGroupingTranscriber.translateTextExpression)

## Functions

music21.braille.noteGrouping.transcribeNoteGrouping(*brailleElementGrouping*, *showLeadingOctave=True*)[[source]](../_modules/music21/braille/noteGrouping.html#transcribeNoteGrouping)
:   transcribe a group of notes, possibly excluding certain attributes.

    To be DEPRECATED – called only by BrailleGrandSegment now.
