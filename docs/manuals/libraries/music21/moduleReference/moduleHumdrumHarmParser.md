Source: https://music21.org/music21docs/moduleReference/moduleHumdrumHarmParser.html

# music21.humdrum.harmParser

Harmonic annotations from humdrum to music21.

The \*\*harm representation is described here: <https://www.humdrum.org/rep/harm/>

## HarmDefs

class music21.humdrum.harmParser.HarmDefs[[source]](../_modules/music21/humdrum/harmParser.html#HarmDefs)
:   Regular expression definitions for the HarmParser class

## HarmParser

class music21.humdrum.harmParser.HarmParser[[source]](../_modules/music21/humdrum/harmParser.html#HarmParser)
:   Parses an expression in \*\*harm syntax

[`HarmParser`](#music21.humdrum.harmParser.HarmParser "music21.humdrum.harmParser.HarmParser") methods

HarmParser.parse(*harmExpression*) → [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")][[source]](../_modules/music21/humdrum/harmParser.html#HarmParser.parse)

## Functions

music21.humdrum.harmParser.convertHarmToRoman(*harmStr*)[[source]](../_modules/music21/humdrum/harmParser.html#convertHarmToRoman)
:   Converts a \*\*harm string into a string that
    can be used to instantiate a RomanNumeral object.

    This is necessary because the two notations are not
    identical. For example, a “V7b” in \*\*harm turns into “V65”.

    Instantiate a HarmParser to process \*\*harm strings

    ```python
    >>> convertHarmToRoman = humdrum.harmParser.convertHarmToRoman
    ```

    Convert a few \*\*harm strings to music21.roman.RomanNumeral figures

    ```python
    >>> diatonicTriads = ['I', 'Vc', 'Ib', 'iib', 'V', 'viiob', 'vib']
    >>> [convertHarmToRoman(x) for x in diatonicTriads]
    ['I', 'V64', 'I6', 'ii6', 'V', 'viio6', 'vi6']
    ```

    A few seventh-chord inversions
    >>> diatonicSevenths = [‘V7’, ‘viio7c’, ‘V7d’, ‘viio7b’, ‘V7c’]
    >>> [convertHarmToRoman(x) for x in diatonicSevenths]
    [‘V7’, ‘viio43’, ‘V2’, ‘viio65’, ‘V43’]

    Inversion-wise, augmented sixth chords are a bit tricky
    German and French are treated as seventh-chords (4 notes)
    Italians are treated as triads

    ```python
    >>> italianSixths = ['Lt', 'Ltb', 'Ltc']
    >>> [convertHarmToRoman(x) for x in italianSixths]
    ['It', 'It6', 'It64']
    ```

    ```python
    >>> frenchSixths = ['Fr', 'Frb', 'Frc', 'Frd']
    >>> [convertHarmToRoman(x) for x in frenchSixths]
    ['Fr7', 'Fr65', 'Fr43', 'Fr2']
    ```

    ```python
    >>> germanSixths = ['Gn', 'Gnb', 'Gnc', 'Gnd']
    >>> [convertHarmToRoman(x) for x in germanSixths]
    ['Ger7', 'Ger65', 'Ger43', 'Ger2']
    ```
