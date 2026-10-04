Source: https://music21.org/music21docs/moduleReference/moduleLanguageExcerptsNaturalLanguageObjects.html

# music21.languageExcerpts.naturalLanguageObjects

Multilingual conversion of pitch, etc. objects

## Functions

music21.languageExcerpts.naturalLanguageObjects.generateLanguageDictionary(*languageString*)[[source]](../_modules/music21/languageExcerpts/naturalLanguageObjects.html#generateLanguageDictionary)

music21.languageExcerpts.naturalLanguageObjects.toChord(*pitchArray*, *languageString*)[[source]](../_modules/music21/languageExcerpts/naturalLanguageObjects.html#toChord)
:   Converts a list of strings to a [`music21.chord.Chord`](moduleChord.html#music21.chord.Chord "music21.chord.Chord") object given a language

    Supported languages are French, German, Italian, and Spanish

    Unsupported strings default to pitch C Natural

    ```python
    >>> languageExcerpts.naturalLanguageObjects.toChord(['Es', 'E', 'Eis'], 'de')
    <music21.chord.Chord E- E E#>
    ```

music21.languageExcerpts.naturalLanguageObjects.toNote(*pitchString*, *languageString*)[[source]](../_modules/music21/languageExcerpts/naturalLanguageObjects.html#toNote)
:   Converts a string to a [`music21.note.Note`](moduleNote.html#music21.note.Note "music21.note.Note") object given a language

    Supported languages are French, German, Italian, and Spanish

    Defaults to C Natural

    ```python
    >>> languageExcerpts.naturalLanguageObjects.toNote('Es', 'de')
    <music21.note.Note E->
    ```

    ```python
    >>> languageExcerpts.naturalLanguageObjects.toNote('H', 'de')
    <music21.note.Note B>
    >>> for i in ['As', 'A', 'Ais']:
    ...     print(languageExcerpts.naturalLanguageObjects.toNote(i, 'de'))
    <music21.note.Note A->
    <music21.note.Note A>
    <music21.note.Note A#>
    ```

music21.languageExcerpts.naturalLanguageObjects.toPitch(*pitchString*, *languageString*)[[source]](../_modules/music21/languageExcerpts/naturalLanguageObjects.html#toPitch)
:   Converts a string to a [`music21.pitch.Pitch`](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") object given a language.

    Supported languages are French, German, Italian, and Spanish

    Defaults to C natural

    ```python
    >>> languageExcerpts.naturalLanguageObjects.toPitch('Es', 'de')
    <music21.pitch.Pitch E->
    ```

    ```python
    >>> languageExcerpts.naturalLanguageObjects.toPitch('H', 'de')
    <music21.pitch.Pitch B>
    >>> for i in ['As', 'A', 'Ais']:
    ...     print(languageExcerpts.naturalLanguageObjects.toPitch(i, 'de'))
    A-
    A
    A#
    ```
