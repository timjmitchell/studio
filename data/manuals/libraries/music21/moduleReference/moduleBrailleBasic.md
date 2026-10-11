Source: https://music21.org/music21docs/moduleReference/moduleBrailleBasic.html

# music21.braille.basic

Basic tools for working with Braille in music21. Most users will not need to
use these. Simply call .show(‘braille’) or .show(‘braille.ascii’)

```python
>>> soprano = corpus.parse('bwv66.6').parts[0]
>>> soprano.show('braille.ascii')
                     %%%.C
    #J .DJ [W?<L$ ?W[<L? IJ\]<L[ WW]$ [W?<L?
      "[W?[ \]R<L Q]]@C ]G%F]<L<K
```

Normally this would open up in a new window. But to store the data, use
converter.toData(…, ‘braille’). Here we show this in Unicode braille
(the default for format braille)

```python
>>> data = converter.toData(soprano, 'braille')
>>> print(data)
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠩⠩⠩⠨⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠼⠚⠀⠨⠙⠚⠀⠪⠺⠹⠣⠇⠫⠀⠹⠺⠪⠣⠇⠹⠀⠊⠚⠳⠻⠣⠇⠪⠀⠺⠺⠻⠫⠀⠪⠺⠹⠣⠇⠹
    ⠀⠀⠐⠪⠺⠹⠪⠀⠳⠻⠗⠣⠇⠀⠟⠻⠻⠈⠉⠀⠻⠛⠩⠋⠻⠣⠇⠣⠅
```

Any [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object") which cannot be transcribed in
[`basic`](#module-music21.braille.basic "music21.braille.basic") returns a braille literary question mark
and outputs a warning to the console, rather than raising an exception.
This is so that a transcription of a `Stream` in
[`translate`](moduleBrailleTranslate.html#module-music21.braille.translate "music21.braille.translate") is completed as thoroughly as possible.

## Functions

music21.braille.basic.barlineToBraille(*music21Barline*)[[source]](../_modules/music21/braille/basic.html#barlineToBraille)
:   Takes in a [`Barline`](moduleBar.html#music21.bar.Barline "music21.bar.Barline") and returns its representation
    as a braille string in UTF-8 unicode.

    Note

    Only dashed, double barlines, and final barlines can be transcribed.

    ```python
    >>> from music21.braille.basic import barlineToBraille
    >>> doubleBarline = bar.Barline('double')
    >>> print(barlineToBraille(doubleBarline))
    ⠣⠅⠄
    >>> finalBarline = bar.Barline('final')
    >>> print(barlineToBraille(finalBarline))
    ⠣⠅
    ```

    Heavy gives an “unusual barline” symbol

    ```python
    >>> heavyBarline = bar.Barline('heavy')
    >>> print(barlineToBraille(heavyBarline))
    ⠇
    ```

music21.braille.basic.brailleAsciiToBrailleUnicode(*brailleAscii: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](../_modules/music21/braille/basic.html#brailleAsciiToBrailleUnicode)
:   translates a braille ASCII string to braille UTF-8 unicode, which
    can then be displayed on-screen in braille on compatible systems.

    Note

    The function works by corresponding ASCII symbols to braille
    symbols in a very direct fashion. It is not a translator from plain
    text to braille, because ASCII symbols may not correspond to their
    equivalents in braille. For example, a literal period is a 4 in
    braille ASCII. Also, all letters are translated into their lowercase
    equivalents, and any capital letters are indicated by preceding them
    with a comma.

    ```python
    >>> t1 = braille.basic.brailleAsciiToBrailleUnicode(',ANDANTE ,MAESTOSO4')
    >>> t1
    '⠠⠁⠝⠙⠁⠝⠞⠑⠀⠠⠍⠁⠑⠎⠞⠕⠎⠕⠲'
    >>> t2 = braille.basic.tempoTextToBraille(tempo.TempoText('Andante Maestoso'))
    >>> t1 == t2
    True
    ```

music21.braille.basic.brailleUnicodeToBrailleAscii(*brailleUnicode*)[[source]](../_modules/music21/braille/basic.html#brailleUnicodeToBrailleAscii)
:   translates a braille UTF-8 unicode string into braille ASCII,
    which is the format compatible with most braille embossers.

    Note

    The function works by corresponding braille symbols to ASCII symbols.
    The table which corresponds to said values can be found
    [here](https://en.wikipedia.org/wiki/Braille_ASCII#Braille_ASCII_values).
    Because of the way in which the braille symbols translate, the resulting
    ASCII string will look to a non-reader as gibberish. Also, the eighth-note notes
    in braille music are one-off their corresponding letters
    in both ASCII and written braille.
    The written D is really a C eighth-note, the written E is really a
    D eighth note, etc.

    ```python
    >>> from music21.braille.basic import brailleUnicodeToBrailleAscii, noteToBraille
    >>> brailleUnicodeToBrailleAscii('\u2800')
    ' '
    >>> Cs8 = note.Note('C#4', quarterLength=0.5)
    >>> Cs8_braille = noteToBraille(Cs8)
    >>> brailleUnicodeToBrailleAscii(Cs8_braille)
    '%"D'
    >>> Eb8 = note.Note('E-4', quarterLength=0.5)
    >>> Eb8_braille = noteToBraille(Eb8)
    >>> brailleUnicodeToBrailleAscii(Eb8_braille)
    '<"F'
    ```

music21.braille.basic.brailleUnicodeToSymbols(*brailleUnicode*, *filledSymbol='o'*, *emptySymbol='·'*)[[source]](../_modules/music21/braille/basic.html#brailleUnicodeToSymbols)
:   translates a braille unicode string into symbols (unicode) – for debugging.

    ```python
    >>> print(braille.basic.brailleUnicodeToSymbols('⠜'))
    ·o
    ·o
    o·
    ```

music21.braille.basic.chordToBraille(*music21Chord*, *descending=True*, *showOctave=True*)[[source]](../_modules/music21/braille/basic.html#chordToBraille)
:   Takes in a [`Chord`](moduleChord.html#music21.chord.Chord "music21.chord.Chord") and returns its representation
    as a braille string in UTF-8 unicode.

    In braille, only one pitch of a chord is brailled, with the rest represented
    as numeric intervals from that one pitch. If descending is True, the highest
    (sounding) pitch is brailled, and intervals are labeled in descending order;
    if descending is False, the lowest (sounding) pitch is brailled, and the
    intervals are labeled in ascending order. Convention dictates that chords
    found in the treble clef are brailled descending, and those found in the bass
    clef are brailled ascending.

    If showOctave is True, the octave of the brailled pitch is shown. Other
    octave marks are shown in context relative to the brailled pitch.

    ```python
    >>> from music21.braille.basic import chordToBraille
    >>> gMajorTriadA = chord.Chord(['G4', 'B4', 'D5', 'G5'], quarterLength=4.0)
    >>> print(chordToBraille(gMajorTriadA, descending=True))
    ⠨⠷⠼⠴⠤
    >>> gMajorTriadB = chord.Chord(['G2', 'B2', 'D3', 'G3'], quarterLength=4.0)
    >>> print(chordToBraille(gMajorTriadB, descending=False))
    ⠘⠷⠬⠔⠤
    >>> gMajorTriadRightHand = chord.Chord(['D4', 'B4', 'G5'], quarterLength=4.0)
    >>> print(chordToBraille(gMajorTriadRightHand, descending=True))
    ⠨⠷⠴⠼
    >>> gMajorTriadLeftHand = chord.Chord(['G2', 'D3', 'B3'], quarterLength=4.0)
    >>> print(chordToBraille(gMajorTriadLeftHand, descending=False))
    ⠘⠷⠔⠬
    >>> cMajorTriadRightHand = chord.Chord(['C4', 'E5'], quarterLength=4.0)
    >>> print(chordToBraille(cMajorTriadRightHand, descending=True))
    ⠨⠯⠐⠬
    >>> cMajorTriadLeftHand = chord.Chord(['C2', 'E3'], quarterLength=4.0)
    >>> print(chordToBraille(cMajorTriadLeftHand, descending=False))
    ⠘⠽⠸⠬
    >>> cMajorSeventhRightHand = chord.Chord(['C6', 'E5', 'B4'], quarterLength=4.0)
    >>> print(chordToBraille(cMajorSeventhRightHand, descending=True))
    ⠰⠽⠴⠌
    >>> cMajorSeventhLeftHand = chord.Chord(['G2', 'E3', 'E4'], quarterLength=4.0)
    >>> print(chordToBraille(cMajorSeventhLeftHand, descending=False))
    ⠘⠷⠴⠐⠴
    ```

    ```python
    >>> chordWithoutAccidentals = chord.Chord(['C4', 'E4', 'F4'], quarterLength=4.0)
    >>> print(chordToBraille(chordWithoutAccidentals, descending=True))
    ⠐⠿⠌⠼
    ```

    ```python
    >>> chordWithAccidentals = chord.Chord(['C4', 'E-4', 'F#4'], quarterLength=4.0)
    >>> chordWithAccidentals.pitches[0].accidental = 'natural'
    >>> print(chordToBraille(chordWithAccidentals, descending=True))
    ⠩⠐⠿⠣⠌⠡⠼
    ```

music21.braille.basic.clefToBraille(*music21Clef*, *keyboardHandSwitched=False*)[[source]](../_modules/music21/braille/basic.html#clefToBraille)
:   Takes in a [`Clef`](moduleClef.html#music21.clef.Clef "music21.clef.Clef") and returns its representation
    as a braille string in UTF-8 unicode.

    Only [`GClef`](moduleClef.html#music21.clef.GClef "music21.clef.GClef"), [`CClef`](moduleClef.html#music21.clef.CClef "music21.clef.CClef"),
    [`FClef`](moduleClef.html#music21.clef.FClef "music21.clef.FClef"), [`NoClef`](moduleClef.html#music21.clef.NoClef "music21.clef.NoClef") and
    their subclasses (such as [`TrebleClef`](moduleClef.html#music21.clef.TrebleClef "music21.clef.TrebleClef"),
    [`BassClef`](moduleClef.html#music21.clef.BassClef "music21.clef.BassClef")) can be transcribed.

    If keyboardHandSwitched is True, the suffix of the brailled clef changes from dots
    1-2-3 to dots 1-3. In scores of keyboard instruments, this change indicates
    that the playing hand differs from which implied by the clef. (E.g. A G clef
    in the left-hand part of a piano score needs the change of suffix.) Note
    that changeSuffix works only for G and F clefs.

    ```python
    >>> from music21.braille.basic import clefToBraille
    >>> trebleClef = clef.TrebleClef()
    >>> print(clefToBraille(trebleClef))
    ⠜⠌⠇
    >>> print(clefToBraille(trebleClef, keyboardHandSwitched=True))
    ⠜⠌⠅
    >>> bassClef = clef.BassClef()
    >>> print(clefToBraille(bassClef))
    ⠜⠼⠇
    >>> print(clefToBraille(bassClef, keyboardHandSwitched=True))
    ⠜⠼⠅
    ```

    ```python
    >>> altoClef = clef.AltoClef()
    >>> print(clefToBraille(altoClef))
    ⠜⠬⠇
    >>> tenorClef = clef.TenorClef()
    >>> print(clefToBraille(tenorClef))
    ⠜⠬⠐⠇
    >>> noClef = clef.NoClef()
    >>> clefToBraille(noClef) == ''
    True
    >>> sopranoClef = clef.SopranoClef()
    >>> print(f'{sopranoClef.sign}, {sopranoClef.line}, {clefToBraille(sopranoClef)}')
    C, 1, ⠜⠬⠈⠇
    ```

music21.braille.basic.dynamicToBraille(*music21Dynamic*, *precedeByWordSign=True*)[[source]](../_modules/music21/braille/basic.html#dynamicToBraille)
:   Takes in a [`Dynamic`](moduleDynamics.html#music21.dynamics.Dynamic "music21.dynamics.Dynamic") and returns its
    [`value`](moduleDynamics.html#music21.dynamics.Dynamic.value "music21.dynamics.Dynamic.value") as a braille string in
    UTF-8 unicode.

    If precedeByWordSign is True, the value is preceded by a word
    sign (⠜).

    ```python
    >>> from music21.braille.basic import dynamicToBraille
    >>> print(dynamicToBraille(dynamics.Dynamic('f')))
    ⠜⠋
    >>> print(dynamicToBraille(dynamics.Dynamic('pp')))
    ⠜⠏⠏
    ```

music21.braille.basic.handleArticulations(*music21Note*, *noteTrans: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*, *upperFirstInFingering=True*)[[source]](../_modules/music21/braille/basic.html#handleArticulations)

music21.braille.basic.handleExpressions(*music21Note: [GeneralNote](moduleNote.html#music21.note.GeneralNote "music21.note.GeneralNote")*, *noteTrans: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*)[[source]](../_modules/music21/braille/basic.html#handleExpressions)
:   Transcribe the expressions for a note.GeneralNote.

music21.braille.basic.handlePitchWithAccidental(*music21Pitch*, *pitchTrans*, *brailleEnglish*)[[source]](../_modules/music21/braille/basic.html#handlePitchWithAccidental)

music21.braille.basic.instrumentToBraille(*music21Instrument*)[[source]](../_modules/music21/braille/basic.html#instrumentToBraille)
:   Takes in a [`Instrument`](moduleInstrument.html#music21.instrument.Instrument "music21.instrument.Instrument") and returns its “best name”
    as a braille string in UTF-8 unicode.

    ```python
    >>> from music21.braille.basic import instrumentToBraille
    >>> print(instrumentToBraille(instrument.Bassoon()))
    ⠠⠃⠁⠎⠎⠕⠕⠝
    >>> print(instrumentToBraille(instrument.BassClarinet()))
    ⠠⠃⠁⠎⠎⠀⠉⠇⠁⠗⠊⠝⠑⠞
    ```

music21.braille.basic.keySigToBraille(*music21KeySignature*, *outgoingKeySig=None*)[[source]](../_modules/music21/braille/basic.html#keySigToBraille)
:   Takes in a [`KeySignature`](moduleKey.html#music21.key.KeySignature "music21.key.KeySignature") and returns its representation
    in braille as a string in UTF-8 unicode.

    ```python
    >>> from music21.braille.basic import keySigToBraille
    >>> print(keySigToBraille(key.KeySignature(4)))
    ⠼⠙⠩
    ```

    If given an old key signature, then its cancellation will be applied before
    and in relation to the new key signature.

    ```python
    >>> print(keySigToBraille(key.KeySignature(0), outgoingKeySig = key.KeySignature(-3)))
    ⠡⠡⠡
    ```

music21.braille.basic.metronomeMarkToBraille(*music21MetronomeMark*)[[source]](../_modules/music21/braille/basic.html#metronomeMarkToBraille)
:   Takes in a [`MetronomeMark`](moduleTempo.html#music21.tempo.MetronomeMark "music21.tempo.MetronomeMark") and returns it as a
    braille string in UTF-8 unicode.
    The format is (note C with duration of metronome’s referent)(metronome symbol)(number/bpm).

    ```python
    >>> from music21.braille.basic import metronomeMarkToBraille
    >>> mm1 = tempo.MetronomeMark(number=80, referent=note.Note(type='half'))
    >>> print(metronomeMarkToBraille(mm1))
    ⠝⠶⠼⠓⠚
    >>> mm2 = tempo.MetronomeMark(number=135, referent=note.Note(quarterLength=0.5))
    >>> print(metronomeMarkToBraille(mm2))
    ⠙⠶⠼⠁⠉⠑
    ```

    ```python
    >>> mm3 = tempo.MetronomeMark(numberSounding=80)
    >>> metronomeMarkToBraille(mm3)
    ''
    ```

music21.braille.basic.noteToBraille(*music21Note: [Note](moduleNote.html#music21.note.Note "music21.note.Note")*, *\**, *showOctave=True*, *upperFirstInFingering=True*)[[source]](../_modules/music21/braille/basic.html#noteToBraille)
:   Given a [`Note`](moduleNote.html#music21.note.Note "music21.note.Note"), returns the appropriate braille
    characters as a string in UTF-8 unicode.

    The format for note display in braille is the accidental (if necessary)
    + octave (if necessary) + pitch name with length.

    If the note has an [`Accidental`](modulePitch.html#music21.pitch.Accidental "music21.pitch.Accidental"), the accidental is always
    displayed unless its [`displayStatus`](modulePitch.html#music21.pitch.Accidental.displayStatus "music21.pitch.Accidental.displayStatus") is set to
    False. The octave of the note is only displayed if showOctave is set to True.

    ```python
    >>> from music21.braille.basic import noteToBraille
    >>> C4 = note.Note('C4')
    >>> print(noteToBraille(C4))
    ⠐⠹
    >>> C4.quarterLength = 2.0
    >>> print(noteToBraille(C4))
    ⠐⠝
    >>> Ds4 = note.Note('D#4')
    >>> print(noteToBraille(Ds4))
    ⠩⠐⠱
    >>> print(noteToBraille(Ds4, showOctave=False))
    ⠩⠱
    >>> Ds4.pitch.accidental.displayStatus=False
    >>> print(noteToBraille(Ds4))
    ⠐⠱
    >>> A2 = note.Note('A2')
    >>> A2.quarterLength = 3.0
    >>> print(noteToBraille(A2))
    ⠘⠎⠄
    ```

    ```python
    >>> B = note.Note('B4')
    >>> f = expressions.Fermata()
    >>> B.expressions.append(f)
    >>> print(noteToBraille(B))
    ⠐⠺⠣⠇
    >>> for x in B.editorial.brailleEnglish:
    ...     print(x)
    Octave 4 ⠐
    B quarter ⠺
    Note-fermata: Shape normal: ⠣⠇
    ```

    ```python
    >>> f.shape = 'square'
    >>> print(noteToBraille(B))
    ⠐⠺⠰⠣⠇
    >>> for x in B.editorial.brailleEnglish:
    ...     print(x)
    Octave 4 ⠐
    B quarter ⠺
    Note-fermata: Shape square: ⠰⠣⠇
    ```

    ```python
    >>> C4 = note.Note('C4')
    >>> print(noteToBraille(C4))
    ⠐⠹
    >>> C4.duration.appendTuplet(duration.Tuplet(3, 2))  # triplet
    >>> print(noteToBraille(C4))
    ⠐⠹
    >>> C4.beamStart = True
    >>> print(noteToBraille(C4))
    ⠆⠐⠹
    >>> for x in C4.editorial.brailleEnglish:
    ...     print(x)
    Triplet ⠆
    Octave 4 ⠐
    C quarter ⠹
    ```

    ```python
    >>> C4 = note.Note('C4')
    >>> C4.duration.appendTuplet(duration.Tuplet(7, 4))  # septuplet
    >>> C4.beamStart = True
    >>> print(noteToBraille(C4))
    ⠸⠶⠄⠐⠹
    >>> for x in C4.editorial.brailleEnglish:
    ...     print(x)
    Septuplet ⠸⠶⠄
    Octave 4 ⠐
    C quarter ⠹
    ```

music21.braille.basic.numberToBraille(*sampleNumber: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *withNumberSign=True*, *lower=False*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](../_modules/music21/braille/basic.html#numberToBraille)
:   Transcribes a number to UTF-8 braille. By default, the result number
    occupies the upper two thirds of braille cells with a leading number sign.
    If withNumberSign is set to False, the leading number sign will be removed.
    If lower is set to True, the position will be changed from the upper (1245
    dots) to the lower (2356 dots).

    ```python
    >>> from music21.braille.basic import numberToBraille
    >>> print(numberToBraille(12))
    ⠼⠁⠃
    >>> print(numberToBraille(7))
    ⠼⠛
    >>> print(numberToBraille(37))
    ⠼⠉⠛
    ```

music21.braille.basic.pitchToOctave(*music21PitchOrInt*)[[source]](../_modules/music21/braille/basic.html#pitchToOctave)
:   takes a pitch object and returns the brailling for the octave.

    Can also be given an int specifying the octave.

    Expands the definition given in Degarmo Ch 7 to allow even less commonly used octaves such
    as -1, and > 8 by tripling, etc. the number of octave marks.

    ```python
    >>> pitchToOctave = braille.basic.pitchToOctave
    >>> print(pitchToOctave(pitch.Pitch('C4')))
    ⠐
    >>> print(pitchToOctave(pitch.Pitch('B-4')))
    ⠐
    >>> print(pitchToOctave(4))
    ⠐
    >>> print(pitchToOctave(3))
    ⠸
    >>> print(pitchToOctave(2))
    ⠘
    >>> print(pitchToOctave(1))
    ⠈
    >>> print(pitchToOctave(0))
    ⠈⠈
    >>> print(pitchToOctave(-1))
    ⠈⠈⠈
    >>> print(pitchToOctave(5))
    ⠨
    >>> print(pitchToOctave(6))
    ⠰
    >>> print(pitchToOctave(7))
    ⠠
    >>> print(pitchToOctave(8))
    ⠠⠠
    >>> print(pitchToOctave(9))
    ⠠⠠⠠
    ```

music21.braille.basic.restToBraille(*music21Rest*)[[source]](../_modules/music21/braille/basic.html#restToBraille)
:   Given a [`Rest`](moduleNote.html#music21.note.Rest "music21.note.Rest"), returns the appropriate braille
    characters as a string in UTF-8 unicode.

    Currently, only supports single rests with or without dots.
    Complex rests are not supported.

    ```python
    >>> from music21.braille.basic import restToBraille
    >>> dottedQuarter = note.Rest(quarterLength=1.5)
    >>> print(restToBraille(dottedQuarter))
    ⠧⠄
    >>> whole = note.Rest(quarterLength=4.0)
    >>> print(restToBraille(whole))
    ⠍
    ```

    This would give a warning and gives the basic\_exception symbol:

    quarterPlusSixteenth = note.Rest(quarterLength=1.25)
    print(restToBraille(quarterPlusSixteenth))
    ⠜⠦

music21.braille.basic.showOctaveWithNote(*previousNote*, *currentNote*)[[source]](../_modules/music21/braille/basic.html#showOctaveWithNote)
:   Determines whether a currentNote carries an octave designation
    in relation to a previous Note.

    Rules:

    * If currentNote is found within a second or third
      of previousNote, currentNote does not
      carry an octave designation.
    * If currentNote is found a sixth or
      more away from previousNote, currentNote does carry
      an octave designation.
    * If currentNote is found within a fourth or fifth
      of previousNote, currentNote carries
      an octave designation if and only if currentNote and
      previousNote are not found in the
      same octave.

    Of course, these rules cease to apply in quite a few cases,
    which are not directly reflected
    in the results of this function:

    1. If a braille measure goes to a new line, the first note in the measure carries an
       octave designation regardless of what the previous note was.
    2. If a braille measure contains a new key or time signature, the first note carries
       an octave designation regardless of what the previous note was.
    3. If a new key or time signature occurs in the middle of a measure, or if a double bar
       line is encountered, both of which would necessitate a music hyphen, the next note after
       those cases needs an octave marking.

    If any special case happens, previousNote can be set to None and the function will return
    True.

    ```python
    >>> from music21.braille.basic import showOctaveWithNote
    >>> showOctaveWithNote(note.Note('C4'), note.Note('E4'))
    False
    >>> showOctaveWithNote(note.Note('C4'), note.Note('F4'))
    False
    >>> showOctaveWithNote(note.Note('C4'), note.Note('F3'))
    True
    >>> showOctaveWithNote(note.Note('C4'), note.Note('A4'))
    True
    ```

    If previousNote is None, it is always True

    ```python
    >>> showOctaveWithNote(None, note.Note('A4'))
    True
    ```

music21.braille.basic.tempoTextToBraille(*music21TempoText: [tempo.TempoText](moduleTempo.html#music21.tempo.TempoText "music21.tempo.TempoText")*, *\**, *maxLineLength=40*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](../_modules/music21/braille/basic.html#tempoTextToBraille)
:   Takes in a [`TempoText`](moduleTempo.html#music21.tempo.TempoText "music21.tempo.TempoText") and returns its representation in braille
    as a string in UTF-8 unicode. The tempo text is returned uncentered, and is split around
    the comma, each split returned on a separate line. The literary period required at the end
    of every tempo text expression in braille is also included.

    ```python
    >>> from music21.braille.basic import tempoTextToBraille
    >>> print(tempoTextToBraille(tempo.TempoText('Lento assai, cantante e tranquillo')))
    ⠠⠇⠑⠝⠞⠕⠀⠁⠎⠎⠁⠊⠂
    ⠉⠁⠝⠞⠁⠝⠞⠑⠀⠑⠀⠞⠗⠁⠝⠟⠥⠊⠇⠇⠕⠲
    >>> print(tempoTextToBraille(tempo.TempoText('Andante molto grazioso')))
    ⠠⠁⠝⠙⠁⠝⠞⠑⠀⠍⠕⠇⠞⠕⠀⠛⠗⠁⠵⠊⠕⠎⠕⠲
    ```

    ```python
    >>> print(tempoTextToBraille(tempo.TempoText('Andante molto grazioso ma cantabile')))
    ⠠⠁⠝⠙⠁⠝⠞⠑⠀⠍⠕⠇⠞⠕⠀⠛⠗⠁⠵⠊⠕⠎⠕⠀⠍⠁⠀
    ⠉⠁⠝⠞⠁⠃⠊⠇⠑⠲
    ```

    ```python
    >>> print(tempoTextToBraille(tempo.TempoText('Andante molto grazioso ma cantabile'),
    ...                          maxLineLength=20))
    ⠠⠁⠝⠙⠁⠝⠞⠑⠀
    ⠍⠕⠇⠞⠕⠀
    ⠛⠗⠁⠵⠊⠕⠎⠕⠀⠍⠁⠀
    ⠉⠁⠝⠞⠁⠃⠊⠇⠑⠲
    ```

music21.braille.basic.textExpressionToBraille(*music21TextExpression*, *precedeByWordSign=True*)[[source]](../_modules/music21/braille/basic.html#textExpressionToBraille)
:   Takes in a [`TextExpression`](moduleExpressions.html#music21.expressions.TextExpression "music21.expressions.TextExpression") and returns its
    representation in UTF-8 unicode.

    From the lookup table:

    ```python
    >>> from music21.braille.basic import textExpressionToBraille
    >>> print(textExpressionToBraille(expressions.TextExpression('cresc.')))
    ⠜⠉⠗⠄
    ```

    Single word expression has word symbol (⠜) only at beginning:

    ```python
    >>> print(textExpressionToBraille(expressions.TextExpression('dolce')))
    ⠜⠙⠕⠇⠉⠑
    ```

    Multiple word expression has word symbol at beginning and end.

    ```python
    >>> print(textExpressionToBraille(expressions.TextExpression('dim. e rall.')))
    ⠜⠙⠊⠍⠄⠀⠑⠀⠗⠁⠇⠇⠄⠜
    ```

music21.braille.basic.timeSigToBraille(*m21TimeSignature*)[[source]](../_modules/music21/braille/basic.html#timeSigToBraille)
:   Takes in a `TimeSignature` and returns its
    representation in braille as a string in UTF-8 unicode.

    ```python
    >>> from music21.braille.basic import timeSigToBraille
    >>> print(timeSigToBraille(meter.TimeSignature('4/4')))
    ⠼⠙⠲
    >>> print(timeSigToBraille(meter.TimeSignature('3/4')))
    ⠼⠉⠲
    >>> print(timeSigToBraille(meter.TimeSignature('12/8')))
    ⠼⠁⠃⠦
    >>> print(timeSigToBraille(meter.TimeSignature('c')))
    ⠨⠉
    ```

music21.braille.basic.transcribeHeading(*music21KeySignature=None*, *music21TimeSignature=None*, *music21TempoText=None*, *music21MetronomeMark=None*, *maxLineLength=40*)[[source]](../_modules/music21/braille/basic.html#transcribeHeading)
:   Takes in a [`KeySignature`](moduleKey.html#music21.key.KeySignature "music21.key.KeySignature"), `TimeSignature`,
    [`TempoText`](moduleTempo.html#music21.tempo.TempoText "music21.tempo.TempoText"), and
    [`MetronomeMark`](moduleTempo.html#music21.tempo.MetronomeMark "music21.tempo.MetronomeMark") and returns its representation in braille as a
    string in UTF-8 unicode. The contents
    are always centered on a line, whose width is 40 by default.

    In most cases, the format is (tempo text)(space)(metronome mark)(space)(key/time signature),
    centered, although all of
    these need not be included. If all the contents do not fit on one line with at
    least 3 blank characters on each side, then
    the tempo text goes on the first line (and additional lines if necessary),
    and the metronome mark + key and time signature
    goes on the last line.

    If the resulting heading is of length zero, a BrailleBasicException is raised.

    ```python
    >>> from music21.braille.basic import transcribeHeading
    >>> print(transcribeHeading(
    ...         key.KeySignature(5),
    ...         meter.TimeSignature('3/8'),
    ...         tempo.TempoText('Allegretto'),
    ...         tempo.MetronomeMark(number=135, referent=note.Note(type='eighth'))))
    ⠀⠀⠀⠀⠀⠀⠀⠠⠁⠇⠇⠑⠛⠗⠑⠞⠞⠕⠲⠀⠙⠶⠼⠁⠉⠑⠀⠼⠑⠩⠼⠉⠦⠀⠀⠀⠀⠀⠀⠀
    >>> print(transcribeHeading(
    ...          key.KeySignature(-2),
    ...          meter.TimeSignature('common'),
    ...          tempo.TempoText('Lento assai, cantante e tranquillo'),
    ...          None))
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠇⠑⠝⠞⠕⠀⠁⠎⠎⠁⠊⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠝⠞⠁⠝⠞⠑⠀⠑⠀⠞⠗⠁⠝⠟⠥⠊⠇⠇⠕⠲⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠣⠣⠨⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    >>> print(transcribeHeading(
    ...          key.KeySignature(-2),
    ...          meter.TimeSignature('common'),
    ...          tempo.TempoText('Lento assai, cantante e tranquillo'),
    ...          None,
    ...          maxLineLength=10))
    ⠀⠠⠇⠑⠝⠞⠕⠀⠀⠀
    ⠀⠀⠁⠎⠎⠁⠊⠂⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠉⠁⠝⠞⠁⠝⠞⠑⠀⠀
    ⠀⠀⠀⠀⠑⠀⠀⠀⠀⠀
    ⠞⠗⠁⠝⠟⠥⠊⠇⠇⠕⠲
    ⠀⠀⠀⠣⠣⠨⠉⠀⠀⠀
    ```

music21.braille.basic.transcribeNoteFingering(*sampleNoteFingering='1'*, *upperFirstInFingering=True*)[[source]](../_modules/music21/braille/basic.html#transcribeNoteFingering)
:   Takes in a note fingering and returns its correct transcription to braille.

    ```python
    >>> from music21.braille.basic import transcribeNoteFingering
    >>> print(transcribeNoteFingering('4'))
    ⠂
    ```

    A change of fingering:

    ```python
    >>> print(transcribeNoteFingering('2-1'))
    ⠃⠉⠁
    ```

    A choice of fingering, both on either the top or bottom of the staff:

    ```python
    >>> print(transcribeNoteFingering('5|4', upperFirstInFingering=True))
    ⠅⠂
    >>> print(transcribeNoteFingering('5|4', upperFirstInFingering=False))
    ⠂⠅
    ```

    A choice of fingering, one on top and one below the staff:

    ```python
    >>> print(transcribeNoteFingering('2,1', upperFirstInFingering=True))
    ⠃⠁
    >>> print(transcribeNoteFingering('2,1', upperFirstInFingering=False))
    ⠁⠃
    ```

    A choice of fingering, first set missing fingermark:

    ```python
    >>> print(transcribeNoteFingering('2,x'))
    ⠃⠄
    ```

    A choice of fingering, second set missing fingermark:

    ```python
    >>> print(transcribeNoteFingering('x,2'))
    ⠠⠃
    ```

    Missing fingermarks change with upperFirstInFingering

    ```python
    >>> print(transcribeNoteFingering('x,4', upperFirstInFingering=True))
    ⠠⠂
    >>> print(transcribeNoteFingering('x,4', upperFirstInFingering=False))
    ⠂⠄
    >>> print(transcribeNoteFingering('4,x', upperFirstInFingering=True))
    ⠂⠄
    >>> print(transcribeNoteFingering('4,x', upperFirstInFingering=False))
    ⠠⠂
    ```

    A change of fingering and a choice of fingering combined (thanks to Bo-cheng Jhan
    for the patch):

    ```python
    >>> print(transcribeNoteFingering('1-2|3-4'))
    ⠁⠉⠃⠇⠉⠂
    ```

    Incorrect fingerings raise a BrailleBasicException:

    ```python
    >>> transcribeNoteFingering('6')
    Traceback (most recent call last):
    music21.braille.basic.BrailleBasicException: Cannot translate note fingering: 6
    ```

music21.braille.basic.transcribeSignatures(*music21KeySignature*, *music21TimeSignature*, *outgoingKeySig=None*)[[source]](../_modules/music21/braille/basic.html#transcribeSignatures)
:   Takes in a [`KeySignature`](moduleKey.html#music21.key.KeySignature "music21.key.KeySignature") and
    `TimeSignature` and returns its representation
    in braille as a string in UTF-8 unicode. If given an old key signature,
    then its cancellation will be applied before
    and in relation to the new key signature.

    Raises a BrailleBasicException if the resulting key and time signature is
    empty, which happens if the time signature
    is None and (a) the key signature is None or (b) the key signature has
    zero sharps and there is no previous key signature.

    ```python
    >>> from music21.braille.basic import transcribeSignatures
    >>> print(transcribeSignatures(key.KeySignature(5), meter.TimeSignature('3/8'), None))
    ⠼⠑⠩⠼⠉⠦
    >>> print(transcribeSignatures(key.KeySignature(0), None, key.KeySignature(-3)))
    ⠡⠡⠡
    ```

music21.braille.basic.wordToBraille(*sampleWord: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *isTextExpression=False*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](../_modules/music21/braille/basic.html#wordToBraille)
:   Transcribes a word to UTF-8 braille.

    ```python
    >>> from music21.braille.basic import wordToBraille
    >>> print(wordToBraille('Andante'))
    ⠠⠁⠝⠙⠁⠝⠞⠑
    ```

    Try the German for violin.

    ```python
    >>> print(wordToBraille('Geige'))
    ⠠⠛⠑⠊⠛⠑
    ```

    Tests number symbol at beginning, punctuation in number
    and switch back to letters.

    ```python
    >>> print(wordToBraille('25.4cm'))
    ⠼⠃⠑⠲⠙⠰⠉⠍
    ```

music21.braille.basic.yieldBrailleArticulations(*noteEl*)[[source]](../_modules/music21/braille/basic.html#yieldBrailleArticulations)
:   Generator that yields braille before note articulations from a given note.
    Might yield nothing.

    “When a staccato or staccatissimo is shown with any of the other
    [before note expressions], it is brailled first.”

    “The up-bow and down-bow marks for bowed string instruments are brailled before any other
    signs from Column A and before an ornament.” (BMTM, 114)

    Beyond that, we yield in alphabetical order, which happens to satisfy this:
    “When an accent is shown with a tenuto, the accent is brailled first.” (BMTM, 113)

    For reference:

    ```python
    >>> brailleArt = braille.lookup.beforeNoteExpr
    >>> print(brailleArt['tenuto'])
    ⠸⠦
    >>> print(brailleArt['staccato'])
    ⠦
    >>> print(brailleArt['accent'])
    ⠨⠦
    ```

    ```python
    >>> brailleBowings = braille.lookup.bowingSymbols
    >>> print(brailleBowings['down bow'])
    ⠣⠃
    >>> print(brailleBowings['up bow'])
    ⠣⠄
    ```

    ```python
    >>> n = note.Note()
    >>> n.articulations.append(articulations.DownBow())
    >>> n.articulations.append(articulations.Tenuto())
    >>> n.articulations.append(articulations.Staccato())
    >>> n.articulations.append(articulations.Accent())
    >>> n.articulations.append(articulations.Scoop())  # example unsupported articulation
    ```

    This will yield in order: DownBow, Staccato, Accent, Tenuto.

    ```python
    >>> for brailleArt in braille.basic.yieldBrailleArticulations(n):
    ...     print(brailleArt)
    ⠣⠃
    ⠦
    ⠨⠦
    ⠸⠦
    ```

music21.braille.basic.yieldDots(*brailleCharacter*)[[source]](../_modules/music21/braille/basic.html#yieldDots)
:   Generator that yields symbol[‘dot’] characters for each row of a
    braille character that where the left dot is filled. These
    are used in many places in Braille Music Code.

    ```python
    >>> B = braille.lookup.brailleDotDict
    >>> gen = braille.basic.yieldDots(B[1])
    >>> gen
    <generator object yieldDots at 0x10aee5f68>
    >>> for dot in gen:
    ...     print(dot)
    ⠄
    >>> gen = braille.basic.yieldDots(B[1235])
    >>> for dot in gen:
    ...     print(dot)
    ⠄
    ⠄
    ⠄
    ```
