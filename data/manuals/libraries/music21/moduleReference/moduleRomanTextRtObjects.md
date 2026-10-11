Source: https://music21.org/music21docs/moduleReference/moduleRomanTextRtObjects.html

# music21.romanText.rtObjects

Translation routines for roman numeral analysis text files, as defined
and demonstrated by Dmitri Tymoczko, Mark Gotham, Michael Scott Cuthbert,
and Christopher Ariza in ISMIR 2019.

## RTAnalyticKey

class music21.romanText.rtObjects.RTAnalyticKey(*src=''*, *container=None*)[[source]](../_modules/music21/romanText/rtObjects.html#RTAnalyticKey)
:   An RTAnalyticKey(RTKeyTypeAtom) only defines a change in the key
    being analyzed. It does not in itself create a [`Key`](moduleKey.html#music21.key.Key "music21.key.Key")
    object.

    ```python
    >>> gMinor = romanText.rtObjects.RTAnalyticKey('g:')
    >>> gMinor
    <music21.romanText.rtObjects.RTAnalyticKey 'g:'>
    >>> gMinor.getKey()
    <music21.key.Key of g minor>
    ```

    ```python
    >>> bMinor = romanText.rtObjects.RTAnalyticKey('bb:')
    >>> bMinor
    <music21.romanText.rtObjects.RTAnalyticKey 'bb:'>
    >>> bMinor.getKey()
    <music21.key.Key of b- minor>
    ```

[`RTAnalyticKey`](#music21.romanText.rtObjects.RTAnalyticKey "music21.romanText.rtObjects.RTAnalyticKey") bases

* [`RTKeyTypeAtom`](#music21.romanText.rtObjects.RTKeyTypeAtom "music21.romanText.rtObjects.RTKeyTypeAtom")
* [`RTAtom`](#music21.romanText.rtObjects.RTAtom "music21.romanText.rtObjects.RTAtom")
* [`RTToken`](#music21.romanText.rtObjects.RTToken "music21.romanText.rtObjects.RTToken")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`RTAnalyticKey`](#music21.romanText.rtObjects.RTAnalyticKey "music21.romanText.rtObjects.RTAnalyticKey") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`RTAnalyticKey`](#music21.romanText.rtObjects.RTAnalyticKey "music21.romanText.rtObjects.RTAnalyticKey") methods

Methods inherited from [`RTKeyTypeAtom`](#music21.romanText.rtObjects.RTKeyTypeAtom "music21.romanText.rtObjects.RTKeyTypeAtom"):

|  |  |  |
| --- | --- | --- |
| * [`getKey()`](#music21.romanText.rtObjects.RTKeyTypeAtom.getKey "music21.romanText.rtObjects.RTKeyTypeAtom.getKey") | * [`getKeySignature()`](#music21.romanText.rtObjects.RTKeyTypeAtom.getKeySignature "music21.romanText.rtObjects.RTKeyTypeAtom.getKeySignature") |  |

Methods inherited from [`RTAtom`](#music21.romanText.rtObjects.RTAtom "music21.romanText.rtObjects.RTAtom"):

|  |  |  |
| --- | --- | --- |
| * [`isAtom()`](#music21.romanText.rtObjects.RTAtom.isAtom "music21.romanText.rtObjects.RTAtom.isAtom") |  |  |

Methods inherited from [`RTToken`](#music21.romanText.rtObjects.RTToken "music21.romanText.rtObjects.RTToken"):

|  |  |  |
| --- | --- | --- |
| * [`isAnalyst()`](#music21.romanText.rtObjects.RTToken.isAnalyst "music21.romanText.rtObjects.RTToken.isAnalyst") * [`isComposer()`](#music21.romanText.rtObjects.RTToken.isComposer "music21.romanText.rtObjects.RTToken.isComposer") * [`isForm()`](#music21.romanText.rtObjects.RTToken.isForm "music21.romanText.rtObjects.RTToken.isForm") * [`isKeySignature()`](#music21.romanText.rtObjects.RTToken.isKeySignature "music21.romanText.rtObjects.RTToken.isKeySignature") * [`isMeasure()`](#music21.romanText.rtObjects.RTToken.isMeasure "music21.romanText.rtObjects.RTToken.isMeasure") | * [`isMovement()`](#music21.romanText.rtObjects.RTToken.isMovement "music21.romanText.rtObjects.RTToken.isMovement") * [`isNote()`](#music21.romanText.rtObjects.RTToken.isNote "music21.romanText.rtObjects.RTToken.isNote") * [`isPedal()`](#music21.romanText.rtObjects.RTToken.isPedal "music21.romanText.rtObjects.RTToken.isPedal") * [`isPiece()`](#music21.romanText.rtObjects.RTToken.isPiece "music21.romanText.rtObjects.RTToken.isPiece") * [`isProofreader()`](#music21.romanText.rtObjects.RTToken.isProofreader "music21.romanText.rtObjects.RTToken.isProofreader") | * [`isTimeSignature()`](#music21.romanText.rtObjects.RTToken.isTimeSignature "music21.romanText.rtObjects.RTToken.isTimeSignature") * [`isTitle()`](#music21.romanText.rtObjects.RTToken.isTitle "music21.romanText.rtObjects.RTToken.isTitle") * [`isVersion()`](#music21.romanText.rtObjects.RTToken.isVersion "music21.romanText.rtObjects.RTToken.isVersion") * [`isWork()`](#music21.romanText.rtObjects.RTToken.isWork "music21.romanText.rtObjects.RTToken.isWork") |

## RTAtom

class music21.romanText.rtObjects.RTAtom(*src=''*, *container=None*)[[source]](../_modules/music21/romanText/rtObjects.html#RTAtom)
:   In RomanText, definitions of chords, phrases boundaries, open/close
    parenthesis, beat indicators, etc. appear within measures (RTMeasure
    objects). These individual elements will be called Atoms, as they are data
    that is not tagged.

    Each atom store a reference to its container (normally an RTMeasure).

    ```python
    >>> chordIV = romanText.rtObjects.RTAtom('IV')
    >>> beat4 = romanText.rtObjects.RTAtom('b4')
    >>> beat4
    <music21.romanText.rtObjects.RTAtom 'b4'>
    >>> beat4.isAtom()
    True
    ```

    However, see RTChord, RTBeat, etc. which are subclasses of RTAtom
    specifically for storing chords, beats, etc.

[`RTAtom`](#music21.romanText.rtObjects.RTAtom "music21.romanText.rtObjects.RTAtom") bases

* [`RTToken`](#music21.romanText.rtObjects.RTToken "music21.romanText.rtObjects.RTToken")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`RTAtom`](#music21.romanText.rtObjects.RTAtom "music21.romanText.rtObjects.RTAtom") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`RTAtom`](#music21.romanText.rtObjects.RTAtom "music21.romanText.rtObjects.RTAtom") methods

RTAtom.isAtom()[[source]](../_modules/music21/romanText/rtObjects.html#RTAtom.isAtom)
:   Atoms are any untagged data; generally only found inside a
    measure definition.

Methods inherited from [`RTToken`](#music21.romanText.rtObjects.RTToken "music21.romanText.rtObjects.RTToken"):

|  |  |  |
| --- | --- | --- |
| * [`isAnalyst()`](#music21.romanText.rtObjects.RTToken.isAnalyst "music21.romanText.rtObjects.RTToken.isAnalyst") * [`isComposer()`](#music21.romanText.rtObjects.RTToken.isComposer "music21.romanText.rtObjects.RTToken.isComposer") * [`isForm()`](#music21.romanText.rtObjects.RTToken.isForm "music21.romanText.rtObjects.RTToken.isForm") * [`isKeySignature()`](#music21.romanText.rtObjects.RTToken.isKeySignature "music21.romanText.rtObjects.RTToken.isKeySignature") * [`isMeasure()`](#music21.romanText.rtObjects.RTToken.isMeasure "music21.romanText.rtObjects.RTToken.isMeasure") | * [`isMovement()`](#music21.romanText.rtObjects.RTToken.isMovement "music21.romanText.rtObjects.RTToken.isMovement") * [`isNote()`](#music21.romanText.rtObjects.RTToken.isNote "music21.romanText.rtObjects.RTToken.isNote") * [`isPedal()`](#music21.romanText.rtObjects.RTToken.isPedal "music21.romanText.rtObjects.RTToken.isPedal") * [`isPiece()`](#music21.romanText.rtObjects.RTToken.isPiece "music21.romanText.rtObjects.RTToken.isPiece") * [`isProofreader()`](#music21.romanText.rtObjects.RTToken.isProofreader "music21.romanText.rtObjects.RTToken.isProofreader") | * [`isTimeSignature()`](#music21.romanText.rtObjects.RTToken.isTimeSignature "music21.romanText.rtObjects.RTToken.isTimeSignature") * [`isTitle()`](#music21.romanText.rtObjects.RTToken.isTitle "music21.romanText.rtObjects.RTToken.isTitle") * [`isVersion()`](#music21.romanText.rtObjects.RTToken.isVersion "music21.romanText.rtObjects.RTToken.isVersion") * [`isWork()`](#music21.romanText.rtObjects.RTToken.isWork "music21.romanText.rtObjects.RTToken.isWork") |

## RTBeat

class music21.romanText.rtObjects.RTBeat(*src=''*, *container=None*)[[source]](../_modules/music21/romanText/rtObjects.html#RTBeat)
:   An RTAtom subclass that defines a beat definition. Also contains a
    reference to the container.

    ```python
    >>> beatFour = romanText.rtObjects.RTBeat('b4')
    >>> beatFour
    <music21.romanText.rtObjects.RTBeat 'b4'>
    ```

[`RTBeat`](#music21.romanText.rtObjects.RTBeat "music21.romanText.rtObjects.RTBeat") bases

* [`RTAtom`](#music21.romanText.rtObjects.RTAtom "music21.romanText.rtObjects.RTAtom")
* [`RTToken`](#music21.romanText.rtObjects.RTToken "music21.romanText.rtObjects.RTToken")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`RTBeat`](#music21.romanText.rtObjects.RTBeat "music21.romanText.rtObjects.RTBeat") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`RTBeat`](#music21.romanText.rtObjects.RTBeat "music21.romanText.rtObjects.RTBeat") methods

RTBeat.getBeatFloatOrFrac()[[source]](../_modules/music21/romanText/rtObjects.html#RTBeat.getBeatFloatOrFrac)
:   Gets the beat number as a float or fraction. Time signature independent

    ```python
    >>> RTB = romanText.rtObjects.RTBeat
    ```

    Simple ones:

    ```python
    >>> RTB('b1').getBeatFloatOrFrac()
    1.0
    >>> RTB('b2').getBeatFloatOrFrac()
    2.0
    ```

    etc.

    with easy float:

    ```python
    >>> RTB('b1.5').getBeatFloatOrFrac()
    1.5
    >>> RTB('b1.25').getBeatFloatOrFrac()
    1.25
    ```

    with harder:

    ```python
    >>> RTB('b1.33').getBeatFloatOrFrac()
    Fraction(4, 3)
    ```

    ```python
    >>> RTB('b2.66').getBeatFloatOrFrac()
    Fraction(8, 3)
    ```

    ```python
    >>> RTB('b1.2').getBeatFloatOrFrac()
    Fraction(6, 5)
    ```

    A third digit of 0.5 adds 1/2 of 1/DENOM of before. Here DENOM is 3 (in 5/3) so
    we add 1/6 to 5/3 to get 11/6:

    ```python
    >>> RTB('b1.66').getBeatFloatOrFrac()
    Fraction(5, 3)
    ```

    ```python
    >>> RTB('b1.66.5').getBeatFloatOrFrac()
    Fraction(11, 6)
    ```

    Similarly 0.25 adds 1/4 of 1/DENOM, to get 21/12 or 7/4 or 1.75:

    ```python
    >>> RTB('b1.66.25').getBeatFloatOrFrac()
    1.75
    ```

    And 0.75 adds 3/4 of 1/DENOM to get 23/12:

    ```python
    >>> RTB('b1.66.75').getBeatFloatOrFrac()
    Fraction(23, 12)
    ```

    A weird way of writing ‘b1.5’:

    ```python
    >>> RTB('b1.33.5').getBeatFloatOrFrac()
    1.5
    ```

RTBeat.getOffset(*timeSignature*)[[source]](../_modules/music21/romanText/rtObjects.html#RTBeat.getOffset)
:   Given a time signature, return the offset position specified by this
    beat.

    ```python
    >>> rtb = romanText.rtObjects.RTBeat('b1.5')
    >>> rtb.getOffset(meter.TimeSignature('3/4'))
    0.5
    >>> rtb.getOffset(meter.TimeSignature('6/8'))
    0.75
    >>> rtb.getOffset(meter.TimeSignature('2/2'))
    1.0
    ```

    ```python
    >>> rtb = romanText.rtObjects.RTBeat('b2')
    >>> rtb.getOffset(meter.TimeSignature('3/4'))
    1.0
    >>> rtb.getOffset(meter.TimeSignature('6/8'))
    1.5
    ```

    ```python
    >>> rtb = romanText.rtObjects.RTBeat('b1.66')
    >>> rtb.getOffset(meter.TimeSignature('6/8'))
    1.0
    >>> rtc = romanText.rtObjects.RTBeat('b1.66.5')
    >>> rtc.getOffset(meter.TimeSignature('6/8'))
    1.25
    ```

Methods inherited from [`RTAtom`](#music21.romanText.rtObjects.RTAtom "music21.romanText.rtObjects.RTAtom"):

|  |  |  |
| --- | --- | --- |
| * [`isAtom()`](#music21.romanText.rtObjects.RTAtom.isAtom "music21.romanText.rtObjects.RTAtom.isAtom") |  |  |

Methods inherited from [`RTToken`](#music21.romanText.rtObjects.RTToken "music21.romanText.rtObjects.RTToken"):

|  |  |  |
| --- | --- | --- |
| * [`isAnalyst()`](#music21.romanText.rtObjects.RTToken.isAnalyst "music21.romanText.rtObjects.RTToken.isAnalyst") * [`isComposer()`](#music21.romanText.rtObjects.RTToken.isComposer "music21.romanText.rtObjects.RTToken.isComposer") * [`isForm()`](#music21.romanText.rtObjects.RTToken.isForm "music21.romanText.rtObjects.RTToken.isForm") * [`isKeySignature()`](#music21.romanText.rtObjects.RTToken.isKeySignature "music21.romanText.rtObjects.RTToken.isKeySignature") * [`isMeasure()`](#music21.romanText.rtObjects.RTToken.isMeasure "music21.romanText.rtObjects.RTToken.isMeasure") | * [`isMovement()`](#music21.romanText.rtObjects.RTToken.isMovement "music21.romanText.rtObjects.RTToken.isMovement") * [`isNote()`](#music21.romanText.rtObjects.RTToken.isNote "music21.romanText.rtObjects.RTToken.isNote") * [`isPedal()`](#music21.romanText.rtObjects.RTToken.isPedal "music21.romanText.rtObjects.RTToken.isPedal") * [`isPiece()`](#music21.romanText.rtObjects.RTToken.isPiece "music21.romanText.rtObjects.RTToken.isPiece") * [`isProofreader()`](#music21.romanText.rtObjects.RTToken.isProofreader "music21.romanText.rtObjects.RTToken.isProofreader") | * [`isTimeSignature()`](#music21.romanText.rtObjects.RTToken.isTimeSignature "music21.romanText.rtObjects.RTToken.isTimeSignature") * [`isTitle()`](#music21.romanText.rtObjects.RTToken.isTitle "music21.romanText.rtObjects.RTToken.isTitle") * [`isVersion()`](#music21.romanText.rtObjects.RTToken.isVersion "music21.romanText.rtObjects.RTToken.isVersion") * [`isWork()`](#music21.romanText.rtObjects.RTToken.isWork "music21.romanText.rtObjects.RTToken.isWork") |

## RTChord

class music21.romanText.rtObjects.RTChord(*src=''*, *container=None*)[[source]](../_modules/music21/romanText/rtObjects.html#RTChord)
:   An RTAtom subclass that defines a chord. Also contains a reference to
    the container.

    ```python
    >>> chordIV = romanText.rtObjects.RTChord('IV')
    >>> chordIV
    <music21.romanText.rtObjects.RTChord 'IV'>
    ```

[`RTChord`](#music21.romanText.rtObjects.RTChord "music21.romanText.rtObjects.RTChord") bases

* [`RTAtom`](#music21.romanText.rtObjects.RTAtom "music21.romanText.rtObjects.RTAtom")
* [`RTToken`](#music21.romanText.rtObjects.RTToken "music21.romanText.rtObjects.RTToken")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`RTChord`](#music21.romanText.rtObjects.RTChord "music21.romanText.rtObjects.RTChord") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`RTChord`](#music21.romanText.rtObjects.RTChord "music21.romanText.rtObjects.RTChord") methods

Methods inherited from [`RTAtom`](#music21.romanText.rtObjects.RTAtom "music21.romanText.rtObjects.RTAtom"):

|  |  |  |
| --- | --- | --- |
| * [`isAtom()`](#music21.romanText.rtObjects.RTAtom.isAtom "music21.romanText.rtObjects.RTAtom.isAtom") |  |  |

Methods inherited from [`RTToken`](#music21.romanText.rtObjects.RTToken "music21.romanText.rtObjects.RTToken"):

|  |  |  |
| --- | --- | --- |
| * [`isAnalyst()`](#music21.romanText.rtObjects.RTToken.isAnalyst "music21.romanText.rtObjects.RTToken.isAnalyst") * [`isComposer()`](#music21.romanText.rtObjects.RTToken.isComposer "music21.romanText.rtObjects.RTToken.isComposer") * [`isForm()`](#music21.romanText.rtObjects.RTToken.isForm "music21.romanText.rtObjects.RTToken.isForm") * [`isKeySignature()`](#music21.romanText.rtObjects.RTToken.isKeySignature "music21.romanText.rtObjects.RTToken.isKeySignature") * [`isMeasure()`](#music21.romanText.rtObjects.RTToken.isMeasure "music21.romanText.rtObjects.RTToken.isMeasure") | * [`isMovement()`](#music21.romanText.rtObjects.RTToken.isMovement "music21.romanText.rtObjects.RTToken.isMovement") * [`isNote()`](#music21.romanText.rtObjects.RTToken.isNote "music21.romanText.rtObjects.RTToken.isNote") * [`isPedal()`](#music21.romanText.rtObjects.RTToken.isPedal "music21.romanText.rtObjects.RTToken.isPedal") * [`isPiece()`](#music21.romanText.rtObjects.RTToken.isPiece "music21.romanText.rtObjects.RTToken.isPiece") * [`isProofreader()`](#music21.romanText.rtObjects.RTToken.isProofreader "music21.romanText.rtObjects.RTToken.isProofreader") | * [`isTimeSignature()`](#music21.romanText.rtObjects.RTToken.isTimeSignature "music21.romanText.rtObjects.RTToken.isTimeSignature") * [`isTitle()`](#music21.romanText.rtObjects.RTToken.isTitle "music21.romanText.rtObjects.RTToken.isTitle") * [`isVersion()`](#music21.romanText.rtObjects.RTToken.isVersion "music21.romanText.rtObjects.RTToken.isVersion") * [`isWork()`](#music21.romanText.rtObjects.RTToken.isWork "music21.romanText.rtObjects.RTToken.isWork") |

## RTCloseParens

class music21.romanText.rtObjects.RTCloseParens(*src=')'*, *container=None*)[[source]](../_modules/music21/romanText/rtObjects.html#RTCloseParens)
:   A simple close parenthesis Atom with a sensible default

    ```python
    >>> romanText.rtObjects.RTCloseParens(')')
    <music21.romanText.rtObjects.RTCloseParens ')'>
    ```

[`RTCloseParens`](#music21.romanText.rtObjects.RTCloseParens "music21.romanText.rtObjects.RTCloseParens") bases

* [`RTAtom`](#music21.romanText.rtObjects.RTAtom "music21.romanText.rtObjects.RTAtom")
* [`RTToken`](#music21.romanText.rtObjects.RTToken "music21.romanText.rtObjects.RTToken")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`RTCloseParens`](#music21.romanText.rtObjects.RTCloseParens "music21.romanText.rtObjects.RTCloseParens") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`RTCloseParens`](#music21.romanText.rtObjects.RTCloseParens "music21.romanText.rtObjects.RTCloseParens") methods

Methods inherited from [`RTAtom`](#music21.romanText.rtObjects.RTAtom "music21.romanText.rtObjects.RTAtom"):

|  |  |  |
| --- | --- | --- |
| * [`isAtom()`](#music21.romanText.rtObjects.RTAtom.isAtom "music21.romanText.rtObjects.RTAtom.isAtom") |  |  |

Methods inherited from [`RTToken`](#music21.romanText.rtObjects.RTToken "music21.romanText.rtObjects.RTToken"):

|  |  |  |
| --- | --- | --- |
| * [`isAnalyst()`](#music21.romanText.rtObjects.RTToken.isAnalyst "music21.romanText.rtObjects.RTToken.isAnalyst") * [`isComposer()`](#music21.romanText.rtObjects.RTToken.isComposer "music21.romanText.rtObjects.RTToken.isComposer") * [`isForm()`](#music21.romanText.rtObjects.RTToken.isForm "music21.romanText.rtObjects.RTToken.isForm") * [`isKeySignature()`](#music21.romanText.rtObjects.RTToken.isKeySignature "music21.romanText.rtObjects.RTToken.isKeySignature") * [`isMeasure()`](#music21.romanText.rtObjects.RTToken.isMeasure "music21.romanText.rtObjects.RTToken.isMeasure") | * [`isMovement()`](#music21.romanText.rtObjects.RTToken.isMovement "music21.romanText.rtObjects.RTToken.isMovement") * [`isNote()`](#music21.romanText.rtObjects.RTToken.isNote "music21.romanText.rtObjects.RTToken.isNote") * [`isPedal()`](#music21.romanText.rtObjects.RTToken.isPedal "music21.romanText.rtObjects.RTToken.isPedal") * [`isPiece()`](#music21.romanText.rtObjects.RTToken.isPiece "music21.romanText.rtObjects.RTToken.isPiece") * [`isProofreader()`](#music21.romanText.rtObjects.RTToken.isProofreader "music21.romanText.rtObjects.RTToken.isProofreader") | * [`isTimeSignature()`](#music21.romanText.rtObjects.RTToken.isTimeSignature "music21.romanText.rtObjects.RTToken.isTimeSignature") * [`isTitle()`](#music21.romanText.rtObjects.RTToken.isTitle "music21.romanText.rtObjects.RTToken.isTitle") * [`isVersion()`](#music21.romanText.rtObjects.RTToken.isVersion "music21.romanText.rtObjects.RTToken.isVersion") * [`isWork()`](#music21.romanText.rtObjects.RTToken.isWork "music21.romanText.rtObjects.RTToken.isWork") |

## RTEllisonStart

class music21.romanText.rtObjects.RTEllisonStart(*src='|\*'*, *container=None*)[[source]](../_modules/music21/romanText/rtObjects.html#RTEllisonStart)
:   ```python
    >>> phrase = romanText.rtObjects.RTEllisonStart('|*')
    >>> phrase
    <music21.romanText.rtObjects.RTEllisonStart '|*'>
    ```

[`RTEllisonStart`](#music21.romanText.rtObjects.RTEllisonStart "music21.romanText.rtObjects.RTEllisonStart") bases

* [`RTPhraseMarker`](#music21.romanText.rtObjects.RTPhraseMarker "music21.romanText.rtObjects.RTPhraseMarker")
* [`RTAtom`](#music21.romanText.rtObjects.RTAtom "music21.romanText.rtObjects.RTAtom")
* [`RTToken`](#music21.romanText.rtObjects.RTToken "music21.romanText.rtObjects.RTToken")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`RTEllisonStart`](#music21.romanText.rtObjects.RTEllisonStart "music21.romanText.rtObjects.RTEllisonStart") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`RTEllisonStart`](#music21.romanText.rtObjects.RTEllisonStart "music21.romanText.rtObjects.RTEllisonStart") methods

Methods inherited from [`RTAtom`](#music21.romanText.rtObjects.RTAtom "music21.romanText.rtObjects.RTAtom"):

|  |  |  |
| --- | --- | --- |
| * [`isAtom()`](#music21.romanText.rtObjects.RTAtom.isAtom "music21.romanText.rtObjects.RTAtom.isAtom") |  |  |

Methods inherited from [`RTToken`](#music21.romanText.rtObjects.RTToken "music21.romanText.rtObjects.RTToken"):

|  |  |  |
| --- | --- | --- |
| * [`isAnalyst()`](#music21.romanText.rtObjects.RTToken.isAnalyst "music21.romanText.rtObjects.RTToken.isAnalyst") * [`isComposer()`](#music21.romanText.rtObjects.RTToken.isComposer "music21.romanText.rtObjects.RTToken.isComposer") * [`isForm()`](#music21.romanText.rtObjects.RTToken.isForm "music21.romanText.rtObjects.RTToken.isForm") * [`isKeySignature()`](#music21.romanText.rtObjects.RTToken.isKeySignature "music21.romanText.rtObjects.RTToken.isKeySignature") * [`isMeasure()`](#music21.romanText.rtObjects.RTToken.isMeasure "music21.romanText.rtObjects.RTToken.isMeasure") | * [`isMovement()`](#music21.romanText.rtObjects.RTToken.isMovement "music21.romanText.rtObjects.RTToken.isMovement") * [`isNote()`](#music21.romanText.rtObjects.RTToken.isNote "music21.romanText.rtObjects.RTToken.isNote") * [`isPedal()`](#music21.romanText.rtObjects.RTToken.isPedal "music21.romanText.rtObjects.RTToken.isPedal") * [`isPiece()`](#music21.romanText.rtObjects.RTToken.isPiece "music21.romanText.rtObjects.RTToken.isPiece") * [`isProofreader()`](#music21.romanText.rtObjects.RTToken.isProofreader "music21.romanText.rtObjects.RTToken.isProofreader") | * [`isTimeSignature()`](#music21.romanText.rtObjects.RTToken.isTimeSignature "music21.romanText.rtObjects.RTToken.isTimeSignature") * [`isTitle()`](#music21.romanText.rtObjects.RTToken.isTitle "music21.romanText.rtObjects.RTToken.isTitle") * [`isVersion()`](#music21.romanText.rtObjects.RTToken.isVersion "music21.romanText.rtObjects.RTToken.isVersion") * [`isWork()`](#music21.romanText.rtObjects.RTToken.isWork "music21.romanText.rtObjects.RTToken.isWork") |

## RTEllisonStop

class music21.romanText.rtObjects.RTEllisonStop(*src='\*|'*, *container=None*)[[source]](../_modules/music21/romanText/rtObjects.html#RTEllisonStop)
:   ```python
    >>> phrase = romanText.rtObjects.RTEllisonStop('*|')
    >>> phrase
    <music21.romanText.rtObjects.RTEllisonStop '*|'>
    ```

[`RTEllisonStop`](#music21.romanText.rtObjects.RTEllisonStop "music21.romanText.rtObjects.RTEllisonStop") bases

* [`RTPhraseMarker`](#music21.romanText.rtObjects.RTPhraseMarker "music21.romanText.rtObjects.RTPhraseMarker")
* [`RTAtom`](#music21.romanText.rtObjects.RTAtom "music21.romanText.rtObjects.RTAtom")
* [`RTToken`](#music21.romanText.rtObjects.RTToken "music21.romanText.rtObjects.RTToken")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`RTEllisonStop`](#music21.romanText.rtObjects.RTEllisonStop "music21.romanText.rtObjects.RTEllisonStop") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`RTEllisonStop`](#music21.romanText.rtObjects.RTEllisonStop "music21.romanText.rtObjects.RTEllisonStop") methods

Methods inherited from [`RTAtom`](#music21.romanText.rtObjects.RTAtom "music21.romanText.rtObjects.RTAtom"):

|  |  |  |
| --- | --- | --- |
| * [`isAtom()`](#music21.romanText.rtObjects.RTAtom.isAtom "music21.romanText.rtObjects.RTAtom.isAtom") |  |  |

Methods inherited from [`RTToken`](#music21.romanText.rtObjects.RTToken "music21.romanText.rtObjects.RTToken"):

|  |  |  |
| --- | --- | --- |
| * [`isAnalyst()`](#music21.romanText.rtObjects.RTToken.isAnalyst "music21.romanText.rtObjects.RTToken.isAnalyst") * [`isComposer()`](#music21.romanText.rtObjects.RTToken.isComposer "music21.romanText.rtObjects.RTToken.isComposer") * [`isForm()`](#music21.romanText.rtObjects.RTToken.isForm "music21.romanText.rtObjects.RTToken.isForm") * [`isKeySignature()`](#music21.romanText.rtObjects.RTToken.isKeySignature "music21.romanText.rtObjects.RTToken.isKeySignature") * [`isMeasure()`](#music21.romanText.rtObjects.RTToken.isMeasure "music21.romanText.rtObjects.RTToken.isMeasure") | * [`isMovement()`](#music21.romanText.rtObjects.RTToken.isMovement "music21.romanText.rtObjects.RTToken.isMovement") * [`isNote()`](#music21.romanText.rtObjects.RTToken.isNote "music21.romanText.rtObjects.RTToken.isNote") * [`isPedal()`](#music21.romanText.rtObjects.RTToken.isPedal "music21.romanText.rtObjects.RTToken.isPedal") * [`isPiece()`](#music21.romanText.rtObjects.RTToken.isPiece "music21.romanText.rtObjects.RTToken.isPiece") * [`isProofreader()`](#music21.romanText.rtObjects.RTToken.isProofreader "music21.romanText.rtObjects.RTToken.isProofreader") | * [`isTimeSignature()`](#music21.romanText.rtObjects.RTToken.isTimeSignature "music21.romanText.rtObjects.RTToken.isTimeSignature") * [`isTitle()`](#music21.romanText.rtObjects.RTToken.isTitle "music21.romanText.rtObjects.RTToken.isTitle") * [`isVersion()`](#music21.romanText.rtObjects.RTToken.isVersion "music21.romanText.rtObjects.RTToken.isVersion") * [`isWork()`](#music21.romanText.rtObjects.RTToken.isWork "music21.romanText.rtObjects.RTToken.isWork") |

## RTFile

class music21.romanText.rtObjects.RTFile[[source]](../_modules/music21/romanText/rtObjects.html#RTFile)
:   Roman Text File access.

[`RTFile`](#music21.romanText.rtObjects.RTFile "music21.romanText.rtObjects.RTFile") bases

* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`RTFile`](#music21.romanText.rtObjects.RTFile "music21.romanText.rtObjects.RTFile") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`RTFile`](#music21.romanText.rtObjects.RTFile "music21.romanText.rtObjects.RTFile") methods

RTFile.close()[[source]](../_modules/music21/romanText/rtObjects.html#RTFile.close)

RTFile.open(*filename*)[[source]](../_modules/music21/romanText/rtObjects.html#RTFile.open)
:   Open a file for reading, trying a variety of encodings and then
    trying them again with an “ignore” flag if it is not possible.

RTFile.openFileLike(*fileLike*)[[source]](../_modules/music21/romanText/rtObjects.html#RTFile.openFileLike)
:   Assign a file-like object, such as those provided by StringIO, as an
    open file object.

RTFile.read()[[source]](../_modules/music21/romanText/rtObjects.html#RTFile.read)
:   Read a file. Note that this calls readstr, which processes all tokens.

    If number is given, a work number will be extracted if possible.

RTFile.readstr(*strSrc*)[[source]](../_modules/music21/romanText/rtObjects.html#RTFile.readstr)
:   Read a string and process all Tokens. Returns a ABCHandler instance.

## RTHandler

class music21.romanText.rtObjects.RTHandler[[source]](../_modules/music21/romanText/rtObjects.html#RTHandler)

[`RTHandler`](#music21.romanText.rtObjects.RTHandler "music21.romanText.rtObjects.RTHandler") read/write properties

RTHandler.tokens
:   Get or set tokens for this Handler.

[`RTHandler`](#music21.romanText.rtObjects.RTHandler "music21.romanText.rtObjects.RTHandler") methods

RTHandler.definesMovement()[[source]](../_modules/music21/romanText/rtObjects.html#RTHandler.definesMovement)
:   Return True if this handler has 1 or more movement.

    ```python
    >>> rth = romanText.rtObjects.RTHandler()
    >>> rth.process('Movement: 1 \n \n m1')
    >>> rth.definesMovements()
    False
    >>> rth.definesMovement()
    True
    ```

RTHandler.definesMovements(*countRequired=2*)[[source]](../_modules/music21/romanText/rtObjects.html#RTHandler.definesMovements)
:   Return True if more than one movement is defined in a RT file.

    ```python
    >>> rth = romanText.rtObjects.RTHandler()
    >>> rth.process('Movement: 1 \n Movement: 2 \n \n m1')
    >>> rth.definesMovements()
    True
    >>> rth.process('Movement: 1 \n m1')
    >>> rth.definesMovements()
    False
    ```

RTHandler.process(*src*)[[source]](../_modules/music21/romanText/rtObjects.html#RTHandler.process)
:   Given an entire specification as a single source string, strSrc, tokenize it.
    This is usually provided in a file.

RTHandler.splitAtHeader(*lines*)[[source]](../_modules/music21/romanText/rtObjects.html#RTHandler.splitAtHeader)
:   Divide string into header and non-header; this is done before
    tokenization.

    ```python
    >>> rth = romanText.rtObjects.RTHandler()
    >>> rth.splitAtHeader(['Title: s', 'Time Signature:', '', 'm1 g: i'])
    (['Title: s', 'Time Signature:', ''], ['m1 g: i'])
    ```

RTHandler.splitByMovement(*duplicateHeader=True*)[[source]](../_modules/music21/romanText/rtObjects.html#RTHandler.splitByMovement)
:   If we have movements defined, return a list of RTHandler rtObjects,
    representing header information and each movement, in order.

    ```python
    >>> rth = romanText.rtObjects.RTHandler()
    >>> rth.process('Title: Test \n Movement: 1 \n m1 \n Movement: 2 \n m1')
    >>> post = rth.splitByMovement(False)
    >>> len(post)
    3
    ```

    ```python
    >>> len(post[0])
    1
    ```

    ```python
    >>> post[0].__class__
    <class 'music21.romanText.rtObjects.RTHandler'>
    >>> len(post[1]), len(post[2])
    (2, 2)
    ```

    ```python
    >>> post = rth.splitByMovement(duplicateHeader=True)
    >>> len(post)
    2
    ```

    ```python
    >>> len(post[0]), len(post[1])
    (3, 3)
    ```

RTHandler.tokenize(*src*)[[source]](../_modules/music21/romanText/rtObjects.html#RTHandler.tokenize)
:   Walk the RT string, creating RT rtObjects along the way.

RTHandler.tokenizeAtoms(*line*, *container=None*)[[source]](../_modules/music21/romanText/rtObjects.html#RTHandler.tokenizeAtoms)
:   Given a line of data stored in measure consisting only of Atoms,
    tokenize and return a list.

    ```python
    >>> rth = romanText.rtObjects.RTHandler()
    >>> rth.tokenizeAtoms('IV b3 ii7 b4 ii')
    [<music21.romanText.rtObjects.RTChord 'IV'>,
     <music21.romanText.rtObjects.RTBeat 'b3'>,
     <music21.romanText.rtObjects.RTChord 'ii7'>,
     <music21.romanText.rtObjects.RTBeat 'b4'>,
     <music21.romanText.rtObjects.RTChord 'ii'>]
    ```

    ```python
    >>> rth.tokenizeAtoms('V7 b2 V13 b3 V7 iio6/5[no5]')
    [<music21.romanText.rtObjects.RTChord 'V7'>,
     <music21.romanText.rtObjects.RTBeat 'b2'>,
     <music21.romanText.rtObjects.RTChord 'V13'>,
     <music21.romanText.rtObjects.RTBeat 'b3'>,
     <music21.romanText.rtObjects.RTChord 'V7'>,
     <music21.romanText.rtObjects.RTChord 'iio6/5[no5]'>]
    ```

    ```python
    >>> tokenList = rth.tokenizeAtoms('I b2 I b2.25 V/ii b2.5 bVII b2.75 V g: IV')
    >>> tokenList
    [<music21.romanText.rtObjects.RTChord 'I'>,
     <music21.romanText.rtObjects.RTBeat 'b2'>,
     <music21.romanText.rtObjects.RTChord 'I'>,
     <music21.romanText.rtObjects.RTBeat 'b2.25'>,
     <music21.romanText.rtObjects.RTChord 'V/ii'>,
     <music21.romanText.rtObjects.RTBeat 'b2.5'>,
     <music21.romanText.rtObjects.RTChord 'bVII'>,
     <music21.romanText.rtObjects.RTBeat 'b2.75'>,
     <music21.romanText.rtObjects.RTChord 'V'>,
     <music21.romanText.rtObjects.RTAnalyticKey 'g:'>,
     <music21.romanText.rtObjects.RTChord 'IV'>]
    ```

    ```python
    >>> tokenList[-2].getKey()
    <music21.key.Key of g minor>
    ```

    ```python
    >>> rth.tokenizeAtoms('= m3')
    []
    ```

    ```python
    >>> tokenList = rth.tokenizeAtoms('g;: ||: V b2 ?(Bb: VII7 b3 III b4 ?)Bb: i :||')
    >>> tokenList
    [<music21.romanText.rtObjects.RTKey 'g;:'>,
     <music21.romanText.rtObjects.RTRepeatStart '||:'>,
     <music21.romanText.rtObjects.RTChord 'V'>,
     <music21.romanText.rtObjects.RTBeat 'b2'>,
     <music21.romanText.rtObjects.RTOptionalKeyOpen '?(Bb:'>,
     <music21.romanText.rtObjects.RTChord 'VII7'>,
     <music21.romanText.rtObjects.RTBeat 'b3'>,
     <music21.romanText.rtObjects.RTChord 'III'>,
     <music21.romanText.rtObjects.RTBeat 'b4'>,
     <music21.romanText.rtObjects.RTOptionalKeyClose '?)Bb:'>,
     <music21.romanText.rtObjects.RTChord 'i'>,
     <music21.romanText.rtObjects.RTRepeatStop ':||'>]
    ```

RTHandler.tokenizeBody(*lines*)[[source]](../_modules/music21/romanText/rtObjects.html#RTHandler.tokenizeBody)
:   In the body, we may have measure, time signature, or note
    declarations, as well as possible other tagged definitions.

RTHandler.tokenizeHeader(*lines*)[[source]](../_modules/music21/romanText/rtObjects.html#RTHandler.tokenizeHeader)
:   In the header, we only have `RTTagged`
    tokens. We can this process these all as the same class.

## RTKey

class music21.romanText.rtObjects.RTKey(*src=''*, *container=None*)[[source]](../_modules/music21/romanText/rtObjects.html#RTKey)
:   An RTKey(RTAtom) defines both a change in KeySignature and a change
    in the analyzed Key.

    They are defined by “;:” after the Key.

    ```python
    >>> gMinor = romanText.rtObjects.RTKey('g;:')
    >>> gMinor
    <music21.romanText.rtObjects.RTKey 'g;:'>
    >>> gMinor.getKey()
    <music21.key.Key of g minor>
    ```

    ```python
    >>> bMinor = romanText.rtObjects.RTKey('bb;:')
    >>> bMinor
    <music21.romanText.rtObjects.RTKey 'bb;:'>
    >>> bMinor.getKey()
    <music21.key.Key of b- minor>
    >>> bMinor.getKeySignature()
    <music21.key.KeySignature of 5 flats>
    ```

    ```python
    >>> eFlatMajor = romanText.rtObjects.RTKey('Eb;:')
    >>> eFlatMajor
    <music21.romanText.rtObjects.RTKey 'Eb;:'>
    >>> eFlatMajor.getKey()
    <music21.key.Key of E- major>
    ```

[`RTKey`](#music21.romanText.rtObjects.RTKey "music21.romanText.rtObjects.RTKey") bases

* [`RTKeyTypeAtom`](#music21.romanText.rtObjects.RTKeyTypeAtom "music21.romanText.rtObjects.RTKeyTypeAtom")
* [`RTAtom`](#music21.romanText.rtObjects.RTAtom "music21.romanText.rtObjects.RTAtom")
* [`RTToken`](#music21.romanText.rtObjects.RTToken "music21.romanText.rtObjects.RTToken")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`RTKey`](#music21.romanText.rtObjects.RTKey "music21.romanText.rtObjects.RTKey") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`RTKey`](#music21.romanText.rtObjects.RTKey "music21.romanText.rtObjects.RTKey") methods

Methods inherited from [`RTKeyTypeAtom`](#music21.romanText.rtObjects.RTKeyTypeAtom "music21.romanText.rtObjects.RTKeyTypeAtom"):

|  |  |  |
| --- | --- | --- |
| * [`getKey()`](#music21.romanText.rtObjects.RTKeyTypeAtom.getKey "music21.romanText.rtObjects.RTKeyTypeAtom.getKey") | * [`getKeySignature()`](#music21.romanText.rtObjects.RTKeyTypeAtom.getKeySignature "music21.romanText.rtObjects.RTKeyTypeAtom.getKeySignature") |  |

Methods inherited from [`RTAtom`](#music21.romanText.rtObjects.RTAtom "music21.romanText.rtObjects.RTAtom"):

|  |  |  |
| --- | --- | --- |
| * [`isAtom()`](#music21.romanText.rtObjects.RTAtom.isAtom "music21.romanText.rtObjects.RTAtom.isAtom") |  |  |

Methods inherited from [`RTToken`](#music21.romanText.rtObjects.RTToken "music21.romanText.rtObjects.RTToken"):

|  |  |  |
| --- | --- | --- |
| * [`isAnalyst()`](#music21.romanText.rtObjects.RTToken.isAnalyst "music21.romanText.rtObjects.RTToken.isAnalyst") * [`isComposer()`](#music21.romanText.rtObjects.RTToken.isComposer "music21.romanText.rtObjects.RTToken.isComposer") * [`isForm()`](#music21.romanText.rtObjects.RTToken.isForm "music21.romanText.rtObjects.RTToken.isForm") * [`isKeySignature()`](#music21.romanText.rtObjects.RTToken.isKeySignature "music21.romanText.rtObjects.RTToken.isKeySignature") * [`isMeasure()`](#music21.romanText.rtObjects.RTToken.isMeasure "music21.romanText.rtObjects.RTToken.isMeasure") | * [`isMovement()`](#music21.romanText.rtObjects.RTToken.isMovement "music21.romanText.rtObjects.RTToken.isMovement") * [`isNote()`](#music21.romanText.rtObjects.RTToken.isNote "music21.romanText.rtObjects.RTToken.isNote") * [`isPedal()`](#music21.romanText.rtObjects.RTToken.isPedal "music21.romanText.rtObjects.RTToken.isPedal") * [`isPiece()`](#music21.romanText.rtObjects.RTToken.isPiece "music21.romanText.rtObjects.RTToken.isPiece") * [`isProofreader()`](#music21.romanText.rtObjects.RTToken.isProofreader "music21.romanText.rtObjects.RTToken.isProofreader") | * [`isTimeSignature()`](#music21.romanText.rtObjects.RTToken.isTimeSignature "music21.romanText.rtObjects.RTToken.isTimeSignature") * [`isTitle()`](#music21.romanText.rtObjects.RTToken.isTitle "music21.romanText.rtObjects.RTToken.isTitle") * [`isVersion()`](#music21.romanText.rtObjects.RTToken.isVersion "music21.romanText.rtObjects.RTToken.isVersion") * [`isWork()`](#music21.romanText.rtObjects.RTToken.isWork "music21.romanText.rtObjects.RTToken.isWork") |

## RTKeySignature

class music21.romanText.rtObjects.RTKeySignature(*src=''*, *container=None*)[[source]](../_modules/music21/romanText/rtObjects.html#RTKeySignature)
:   An RTKeySignature(RTAtom) only defines a change in the KeySignature.
    It does not in itself create a [`Key`](moduleKey.html#music21.key.Key "music21.key.Key") object, nor
    does it change the analysis taking place.

    The number after KS defines the number of sharps (negative for flats).

    ```python
    >>> gMinor = romanText.rtObjects.RTKeySignature('KS-2')
    >>> gMinor
    <music21.romanText.rtObjects.RTKeySignature 'KS-2'>
    >>> gMinor.getKeySignature()
    <music21.key.KeySignature of 2 flats>
    ```

    ```python
    >>> aMajor = romanText.rtObjects.RTKeySignature('KS3')
    >>> aMajor.getKeySignature()
    <music21.key.KeySignature of 3 sharps>
    ```

[`RTKeySignature`](#music21.romanText.rtObjects.RTKeySignature "music21.romanText.rtObjects.RTKeySignature") bases

* [`RTAtom`](#music21.romanText.rtObjects.RTAtom "music21.romanText.rtObjects.RTAtom")
* [`RTToken`](#music21.romanText.rtObjects.RTToken "music21.romanText.rtObjects.RTToken")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`RTKeySignature`](#music21.romanText.rtObjects.RTKeySignature "music21.romanText.rtObjects.RTKeySignature") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`RTKeySignature`](#music21.romanText.rtObjects.RTKeySignature "music21.romanText.rtObjects.RTKeySignature") methods

RTKeySignature.getKeySignature()[[source]](../_modules/music21/romanText/rtObjects.html#RTKeySignature.getKeySignature)

Methods inherited from [`RTAtom`](#music21.romanText.rtObjects.RTAtom "music21.romanText.rtObjects.RTAtom"):

|  |  |  |
| --- | --- | --- |
| * [`isAtom()`](#music21.romanText.rtObjects.RTAtom.isAtom "music21.romanText.rtObjects.RTAtom.isAtom") |  |  |

Methods inherited from [`RTToken`](#music21.romanText.rtObjects.RTToken "music21.romanText.rtObjects.RTToken"):

|  |  |  |
| --- | --- | --- |
| * [`isAnalyst()`](#music21.romanText.rtObjects.RTToken.isAnalyst "music21.romanText.rtObjects.RTToken.isAnalyst") * [`isComposer()`](#music21.romanText.rtObjects.RTToken.isComposer "music21.romanText.rtObjects.RTToken.isComposer") * [`isForm()`](#music21.romanText.rtObjects.RTToken.isForm "music21.romanText.rtObjects.RTToken.isForm") * [`isKeySignature()`](#music21.romanText.rtObjects.RTToken.isKeySignature "music21.romanText.rtObjects.RTToken.isKeySignature") * [`isMeasure()`](#music21.romanText.rtObjects.RTToken.isMeasure "music21.romanText.rtObjects.RTToken.isMeasure") | * [`isMovement()`](#music21.romanText.rtObjects.RTToken.isMovement "music21.romanText.rtObjects.RTToken.isMovement") * [`isNote()`](#music21.romanText.rtObjects.RTToken.isNote "music21.romanText.rtObjects.RTToken.isNote") * [`isPedal()`](#music21.romanText.rtObjects.RTToken.isPedal "music21.romanText.rtObjects.RTToken.isPedal") * [`isPiece()`](#music21.romanText.rtObjects.RTToken.isPiece "music21.romanText.rtObjects.RTToken.isPiece") * [`isProofreader()`](#music21.romanText.rtObjects.RTToken.isProofreader "music21.romanText.rtObjects.RTToken.isProofreader") | * [`isTimeSignature()`](#music21.romanText.rtObjects.RTToken.isTimeSignature "music21.romanText.rtObjects.RTToken.isTimeSignature") * [`isTitle()`](#music21.romanText.rtObjects.RTToken.isTitle "music21.romanText.rtObjects.RTToken.isTitle") * [`isVersion()`](#music21.romanText.rtObjects.RTToken.isVersion "music21.romanText.rtObjects.RTToken.isVersion") * [`isWork()`](#music21.romanText.rtObjects.RTToken.isWork "music21.romanText.rtObjects.RTToken.isWork") |

## RTKeyTypeAtom

class music21.romanText.rtObjects.RTKeyTypeAtom(*src=''*, *container=None*)[[source]](../_modules/music21/romanText/rtObjects.html#RTKeyTypeAtom)
:   RTKeyTypeAtoms contain utility functions for all Key-type tokens, i.e.
    RTKey, RTAnalyticKey, but not KeySignature.

    ```python
    >>> gMinor = romanText.rtObjects.RTKeyTypeAtom('g;:')
    >>> gMinor
    <music21.romanText.rtObjects.RTKeyTypeAtom 'g;:'>
    >>> gMinor.getKey()
    <music21.key.Key of g minor>
    ```

[`RTKeyTypeAtom`](#music21.romanText.rtObjects.RTKeyTypeAtom "music21.romanText.rtObjects.RTKeyTypeAtom") bases

* [`RTAtom`](#music21.romanText.rtObjects.RTAtom "music21.romanText.rtObjects.RTAtom")
* [`RTToken`](#music21.romanText.rtObjects.RTToken "music21.romanText.rtObjects.RTToken")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`RTKeyTypeAtom`](#music21.romanText.rtObjects.RTKeyTypeAtom "music21.romanText.rtObjects.RTKeyTypeAtom") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`RTKeyTypeAtom`](#music21.romanText.rtObjects.RTKeyTypeAtom "music21.romanText.rtObjects.RTKeyTypeAtom") methods

RTKeyTypeAtom.getKey()[[source]](../_modules/music21/romanText/rtObjects.html#RTKeyTypeAtom.getKey)
:   This returns a Key, not a KeySignature object

RTKeyTypeAtom.getKeySignature()[[source]](../_modules/music21/romanText/rtObjects.html#RTKeyTypeAtom.getKeySignature)
:   Get a KeySignature object.

Methods inherited from [`RTAtom`](#music21.romanText.rtObjects.RTAtom "music21.romanText.rtObjects.RTAtom"):

|  |  |  |
| --- | --- | --- |
| * [`isAtom()`](#music21.romanText.rtObjects.RTAtom.isAtom "music21.romanText.rtObjects.RTAtom.isAtom") |  |  |

Methods inherited from [`RTToken`](#music21.romanText.rtObjects.RTToken "music21.romanText.rtObjects.RTToken"):

|  |  |  |
| --- | --- | --- |
| * [`isAnalyst()`](#music21.romanText.rtObjects.RTToken.isAnalyst "music21.romanText.rtObjects.RTToken.isAnalyst") * [`isComposer()`](#music21.romanText.rtObjects.RTToken.isComposer "music21.romanText.rtObjects.RTToken.isComposer") * [`isForm()`](#music21.romanText.rtObjects.RTToken.isForm "music21.romanText.rtObjects.RTToken.isForm") * [`isKeySignature()`](#music21.romanText.rtObjects.RTToken.isKeySignature "music21.romanText.rtObjects.RTToken.isKeySignature") * [`isMeasure()`](#music21.romanText.rtObjects.RTToken.isMeasure "music21.romanText.rtObjects.RTToken.isMeasure") | * [`isMovement()`](#music21.romanText.rtObjects.RTToken.isMovement "music21.romanText.rtObjects.RTToken.isMovement") * [`isNote()`](#music21.romanText.rtObjects.RTToken.isNote "music21.romanText.rtObjects.RTToken.isNote") * [`isPedal()`](#music21.romanText.rtObjects.RTToken.isPedal "music21.romanText.rtObjects.RTToken.isPedal") * [`isPiece()`](#music21.romanText.rtObjects.RTToken.isPiece "music21.romanText.rtObjects.RTToken.isPiece") * [`isProofreader()`](#music21.romanText.rtObjects.RTToken.isProofreader "music21.romanText.rtObjects.RTToken.isProofreader") | * [`isTimeSignature()`](#music21.romanText.rtObjects.RTToken.isTimeSignature "music21.romanText.rtObjects.RTToken.isTimeSignature") * [`isTitle()`](#music21.romanText.rtObjects.RTToken.isTitle "music21.romanText.rtObjects.RTToken.isTitle") * [`isVersion()`](#music21.romanText.rtObjects.RTToken.isVersion "music21.romanText.rtObjects.RTToken.isVersion") * [`isWork()`](#music21.romanText.rtObjects.RTToken.isWork "music21.romanText.rtObjects.RTToken.isWork") |

## RTMeasure

class music21.romanText.rtObjects.RTMeasure(*src=''*)[[source]](../_modules/music21/romanText/rtObjects.html#RTMeasure)
:   In RomanText, measures are given one per line and always start with ‘m’.

    For instance:

    > m4 i b3 v b4 VI
    > m5 b2 g: IV b4 V
    > m6 i
    > m7 D: V

    Measure ranges can be used and copied, such as:

    > m8-m9=m4-m5

    RTMeasure objects can also define variant readings for a measure:

    > m1 ii
    > m1var1 ii b2 ii6 b3 IV

    Variants are not part of the tag, but are read into an attribute.

    Endings are indicated by a single letter after the measure number, such as
    “a” for first ending.

    ```python
    >>> rtm = romanText.rtObjects.RTMeasure('m15a V6 b1.5 V6/5 b2 I b3 viio6')
    >>> rtm.data
    'V6 b1.5 V6/5 b2 I b3 viio6'
    >>> rtm.number
    [15]
    >>> rtm.repeatLetter
    ['a']
    >>> rtm.isMeasure()
    True
    ```

[`RTMeasure`](#music21.romanText.rtObjects.RTMeasure "music21.romanText.rtObjects.RTMeasure") bases

* [`RTToken`](#music21.romanText.rtObjects.RTToken "music21.romanText.rtObjects.RTToken")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`RTMeasure`](#music21.romanText.rtObjects.RTMeasure "music21.romanText.rtObjects.RTMeasure") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`RTMeasure`](#music21.romanText.rtObjects.RTMeasure "music21.romanText.rtObjects.RTMeasure") methods

RTMeasure.getCopyTarget()[[source]](../_modules/music21/romanText/rtObjects.html#RTMeasure.getCopyTarget)
:   If this measure defines a copy operation, return two lists defining
    the measures to copy; the second list has the repeat data.

    ```python
    >>> rtm = romanText.rtObjects.RTMeasure('m35-36 = m29-30')
    >>> rtm.number
    [35, 36]
    >>> rtm.getCopyTarget()
    ([29, 30], ['', ''])
    ```

    ```python
    >>> rtm = romanText.rtObjects.RTMeasure('m4 = m1')
    >>> rtm.number
    [4]
    >>> rtm.getCopyTarget()
    ([1], [''])
    ```

RTMeasure.isMeasure()[[source]](../_modules/music21/romanText/rtObjects.html#RTMeasure.isMeasure)

Methods inherited from [`RTToken`](#music21.romanText.rtObjects.RTToken "music21.romanText.rtObjects.RTToken"):

|  |  |  |
| --- | --- | --- |
| * [`isAnalyst()`](#music21.romanText.rtObjects.RTToken.isAnalyst "music21.romanText.rtObjects.RTToken.isAnalyst") * [`isAtom()`](#music21.romanText.rtObjects.RTToken.isAtom "music21.romanText.rtObjects.RTToken.isAtom") * [`isComposer()`](#music21.romanText.rtObjects.RTToken.isComposer "music21.romanText.rtObjects.RTToken.isComposer") * [`isForm()`](#music21.romanText.rtObjects.RTToken.isForm "music21.romanText.rtObjects.RTToken.isForm") * [`isKeySignature()`](#music21.romanText.rtObjects.RTToken.isKeySignature "music21.romanText.rtObjects.RTToken.isKeySignature") | * [`isMovement()`](#music21.romanText.rtObjects.RTToken.isMovement "music21.romanText.rtObjects.RTToken.isMovement") * [`isNote()`](#music21.romanText.rtObjects.RTToken.isNote "music21.romanText.rtObjects.RTToken.isNote") * [`isPedal()`](#music21.romanText.rtObjects.RTToken.isPedal "music21.romanText.rtObjects.RTToken.isPedal") * [`isPiece()`](#music21.romanText.rtObjects.RTToken.isPiece "music21.romanText.rtObjects.RTToken.isPiece") * [`isProofreader()`](#music21.romanText.rtObjects.RTToken.isProofreader "music21.romanText.rtObjects.RTToken.isProofreader") | * [`isTimeSignature()`](#music21.romanText.rtObjects.RTToken.isTimeSignature "music21.romanText.rtObjects.RTToken.isTimeSignature") * [`isTitle()`](#music21.romanText.rtObjects.RTToken.isTitle "music21.romanText.rtObjects.RTToken.isTitle") * [`isVersion()`](#music21.romanText.rtObjects.RTToken.isVersion "music21.romanText.rtObjects.RTToken.isVersion") * [`isWork()`](#music21.romanText.rtObjects.RTToken.isWork "music21.romanText.rtObjects.RTToken.isWork") |

## RTNoChord

class music21.romanText.rtObjects.RTNoChord(*src=''*, *container=None*)[[source]](../_modules/music21/romanText/rtObjects.html#RTNoChord)
:   An RTAtom subclass that defines absence of a chord. Also contains a
    reference to the container.

    ```python
    >>> chordNC = romanText.rtObjects.RTNoChord('NC')
    >>> chordNC
    <music21.romanText.rtObjects.RTNoChord 'NC'>
    ```

    ```python
    >>> rth = romanText.rtObjects.RTHandler()
    >>> rth.tokenizeAtoms('nc NC N.C.')
    [<music21.romanText.rtObjects.RTNoChord 'nc'>,
     <music21.romanText.rtObjects.RTNoChord 'NC'>,
     <music21.romanText.rtObjects.RTNoChord 'N.C.'>]
    ```

[`RTNoChord`](#music21.romanText.rtObjects.RTNoChord "music21.romanText.rtObjects.RTNoChord") bases

* [`RTAtom`](#music21.romanText.rtObjects.RTAtom "music21.romanText.rtObjects.RTAtom")
* [`RTToken`](#music21.romanText.rtObjects.RTToken "music21.romanText.rtObjects.RTToken")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`RTNoChord`](#music21.romanText.rtObjects.RTNoChord "music21.romanText.rtObjects.RTNoChord") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`RTNoChord`](#music21.romanText.rtObjects.RTNoChord "music21.romanText.rtObjects.RTNoChord") methods

Methods inherited from [`RTAtom`](#music21.romanText.rtObjects.RTAtom "music21.romanText.rtObjects.RTAtom"):

|  |  |  |
| --- | --- | --- |
| * [`isAtom()`](#music21.romanText.rtObjects.RTAtom.isAtom "music21.romanText.rtObjects.RTAtom.isAtom") |  |  |

Methods inherited from [`RTToken`](#music21.romanText.rtObjects.RTToken "music21.romanText.rtObjects.RTToken"):

|  |  |  |
| --- | --- | --- |
| * [`isAnalyst()`](#music21.romanText.rtObjects.RTToken.isAnalyst "music21.romanText.rtObjects.RTToken.isAnalyst") * [`isComposer()`](#music21.romanText.rtObjects.RTToken.isComposer "music21.romanText.rtObjects.RTToken.isComposer") * [`isForm()`](#music21.romanText.rtObjects.RTToken.isForm "music21.romanText.rtObjects.RTToken.isForm") * [`isKeySignature()`](#music21.romanText.rtObjects.RTToken.isKeySignature "music21.romanText.rtObjects.RTToken.isKeySignature") * [`isMeasure()`](#music21.romanText.rtObjects.RTToken.isMeasure "music21.romanText.rtObjects.RTToken.isMeasure") | * [`isMovement()`](#music21.romanText.rtObjects.RTToken.isMovement "music21.romanText.rtObjects.RTToken.isMovement") * [`isNote()`](#music21.romanText.rtObjects.RTToken.isNote "music21.romanText.rtObjects.RTToken.isNote") * [`isPedal()`](#music21.romanText.rtObjects.RTToken.isPedal "music21.romanText.rtObjects.RTToken.isPedal") * [`isPiece()`](#music21.romanText.rtObjects.RTToken.isPiece "music21.romanText.rtObjects.RTToken.isPiece") * [`isProofreader()`](#music21.romanText.rtObjects.RTToken.isProofreader "music21.romanText.rtObjects.RTToken.isProofreader") | * [`isTimeSignature()`](#music21.romanText.rtObjects.RTToken.isTimeSignature "music21.romanText.rtObjects.RTToken.isTimeSignature") * [`isTitle()`](#music21.romanText.rtObjects.RTToken.isTitle "music21.romanText.rtObjects.RTToken.isTitle") * [`isVersion()`](#music21.romanText.rtObjects.RTToken.isVersion "music21.romanText.rtObjects.RTToken.isVersion") * [`isWork()`](#music21.romanText.rtObjects.RTToken.isWork "music21.romanText.rtObjects.RTToken.isWork") |

## RTOpenParens

class music21.romanText.rtObjects.RTOpenParens(*src='('*, *container=None*)[[source]](../_modules/music21/romanText/rtObjects.html#RTOpenParens)
:   A simple open parenthesis Atom with a sensible default

    ```python
    >>> romanText.rtObjects.RTOpenParens('(')
    <music21.romanText.rtObjects.RTOpenParens '('>
    ```

[`RTOpenParens`](#music21.romanText.rtObjects.RTOpenParens "music21.romanText.rtObjects.RTOpenParens") bases

* [`RTAtom`](#music21.romanText.rtObjects.RTAtom "music21.romanText.rtObjects.RTAtom")
* [`RTToken`](#music21.romanText.rtObjects.RTToken "music21.romanText.rtObjects.RTToken")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`RTOpenParens`](#music21.romanText.rtObjects.RTOpenParens "music21.romanText.rtObjects.RTOpenParens") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`RTOpenParens`](#music21.romanText.rtObjects.RTOpenParens "music21.romanText.rtObjects.RTOpenParens") methods

Methods inherited from [`RTAtom`](#music21.romanText.rtObjects.RTAtom "music21.romanText.rtObjects.RTAtom"):

|  |  |  |
| --- | --- | --- |
| * [`isAtom()`](#music21.romanText.rtObjects.RTAtom.isAtom "music21.romanText.rtObjects.RTAtom.isAtom") |  |  |

Methods inherited from [`RTToken`](#music21.romanText.rtObjects.RTToken "music21.romanText.rtObjects.RTToken"):

|  |  |  |
| --- | --- | --- |
| * [`isAnalyst()`](#music21.romanText.rtObjects.RTToken.isAnalyst "music21.romanText.rtObjects.RTToken.isAnalyst") * [`isComposer()`](#music21.romanText.rtObjects.RTToken.isComposer "music21.romanText.rtObjects.RTToken.isComposer") * [`isForm()`](#music21.romanText.rtObjects.RTToken.isForm "music21.romanText.rtObjects.RTToken.isForm") * [`isKeySignature()`](#music21.romanText.rtObjects.RTToken.isKeySignature "music21.romanText.rtObjects.RTToken.isKeySignature") * [`isMeasure()`](#music21.romanText.rtObjects.RTToken.isMeasure "music21.romanText.rtObjects.RTToken.isMeasure") | * [`isMovement()`](#music21.romanText.rtObjects.RTToken.isMovement "music21.romanText.rtObjects.RTToken.isMovement") * [`isNote()`](#music21.romanText.rtObjects.RTToken.isNote "music21.romanText.rtObjects.RTToken.isNote") * [`isPedal()`](#music21.romanText.rtObjects.RTToken.isPedal "music21.romanText.rtObjects.RTToken.isPedal") * [`isPiece()`](#music21.romanText.rtObjects.RTToken.isPiece "music21.romanText.rtObjects.RTToken.isPiece") * [`isProofreader()`](#music21.romanText.rtObjects.RTToken.isProofreader "music21.romanText.rtObjects.RTToken.isProofreader") | * [`isTimeSignature()`](#music21.romanText.rtObjects.RTToken.isTimeSignature "music21.romanText.rtObjects.RTToken.isTimeSignature") * [`isTitle()`](#music21.romanText.rtObjects.RTToken.isTitle "music21.romanText.rtObjects.RTToken.isTitle") * [`isVersion()`](#music21.romanText.rtObjects.RTToken.isVersion "music21.romanText.rtObjects.RTToken.isVersion") * [`isWork()`](#music21.romanText.rtObjects.RTToken.isWork "music21.romanText.rtObjects.RTToken.isWork") |

## RTOptionalKeyClose

class music21.romanText.rtObjects.RTOptionalKeyClose(*src=''*, *container=None*)[[source]](../_modules/music21/romanText/rtObjects.html#RTOptionalKeyClose)
:   Marks the end of an optional Key area which does not affect the roman
    numeral analysis.

    For example, it is possible to analyze in Bb major, while remaining in g
    minor.

    ```python
    >>> possibleKey = romanText.rtObjects.RTOptionalKeyClose('?)Bb:')
    >>> possibleKey
    <music21.romanText.rtObjects.RTOptionalKeyClose '?)Bb:'>
    >>> possibleKey.getKey()
    <music21.key.Key of B- major>
    ```

[`RTOptionalKeyClose`](#music21.romanText.rtObjects.RTOptionalKeyClose "music21.romanText.rtObjects.RTOptionalKeyClose") bases

* [`RTAtom`](#music21.romanText.rtObjects.RTAtom "music21.romanText.rtObjects.RTAtom")
* [`RTToken`](#music21.romanText.rtObjects.RTToken "music21.romanText.rtObjects.RTToken")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`RTOptionalKeyClose`](#music21.romanText.rtObjects.RTOptionalKeyClose "music21.romanText.rtObjects.RTOptionalKeyClose") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`RTOptionalKeyClose`](#music21.romanText.rtObjects.RTOptionalKeyClose "music21.romanText.rtObjects.RTOptionalKeyClose") methods

RTOptionalKeyClose.getKey()[[source]](../_modules/music21/romanText/rtObjects.html#RTOptionalKeyClose.getKey)

Methods inherited from [`RTAtom`](#music21.romanText.rtObjects.RTAtom "music21.romanText.rtObjects.RTAtom"):

|  |  |  |
| --- | --- | --- |
| * [`isAtom()`](#music21.romanText.rtObjects.RTAtom.isAtom "music21.romanText.rtObjects.RTAtom.isAtom") |  |  |

Methods inherited from [`RTToken`](#music21.romanText.rtObjects.RTToken "music21.romanText.rtObjects.RTToken"):

|  |  |  |
| --- | --- | --- |
| * [`isAnalyst()`](#music21.romanText.rtObjects.RTToken.isAnalyst "music21.romanText.rtObjects.RTToken.isAnalyst") * [`isComposer()`](#music21.romanText.rtObjects.RTToken.isComposer "music21.romanText.rtObjects.RTToken.isComposer") * [`isForm()`](#music21.romanText.rtObjects.RTToken.isForm "music21.romanText.rtObjects.RTToken.isForm") * [`isKeySignature()`](#music21.romanText.rtObjects.RTToken.isKeySignature "music21.romanText.rtObjects.RTToken.isKeySignature") * [`isMeasure()`](#music21.romanText.rtObjects.RTToken.isMeasure "music21.romanText.rtObjects.RTToken.isMeasure") | * [`isMovement()`](#music21.romanText.rtObjects.RTToken.isMovement "music21.romanText.rtObjects.RTToken.isMovement") * [`isNote()`](#music21.romanText.rtObjects.RTToken.isNote "music21.romanText.rtObjects.RTToken.isNote") * [`isPedal()`](#music21.romanText.rtObjects.RTToken.isPedal "music21.romanText.rtObjects.RTToken.isPedal") * [`isPiece()`](#music21.romanText.rtObjects.RTToken.isPiece "music21.romanText.rtObjects.RTToken.isPiece") * [`isProofreader()`](#music21.romanText.rtObjects.RTToken.isProofreader "music21.romanText.rtObjects.RTToken.isProofreader") | * [`isTimeSignature()`](#music21.romanText.rtObjects.RTToken.isTimeSignature "music21.romanText.rtObjects.RTToken.isTimeSignature") * [`isTitle()`](#music21.romanText.rtObjects.RTToken.isTitle "music21.romanText.rtObjects.RTToken.isTitle") * [`isVersion()`](#music21.romanText.rtObjects.RTToken.isVersion "music21.romanText.rtObjects.RTToken.isVersion") * [`isWork()`](#music21.romanText.rtObjects.RTToken.isWork "music21.romanText.rtObjects.RTToken.isWork") |

## RTOptionalKeyOpen

class music21.romanText.rtObjects.RTOptionalKeyOpen(*src=''*, *container=None*)[[source]](../_modules/music21/romanText/rtObjects.html#RTOptionalKeyOpen)
:   Marks the beginning of an optional Key area which does not
    affect the roman numeral analysis. (For instance, it is
    possible to analyze in Bb major, while remaining in g minor)

    ```python
    >>> possibleKey = romanText.rtObjects.RTOptionalKeyOpen('?(Bb:')
    >>> possibleKey
    <music21.romanText.rtObjects.RTOptionalKeyOpen '?(Bb:'>
    >>> possibleKey.getKey()
    <music21.key.Key of B- major>
    ```

[`RTOptionalKeyOpen`](#music21.romanText.rtObjects.RTOptionalKeyOpen "music21.romanText.rtObjects.RTOptionalKeyOpen") bases

* [`RTAtom`](#music21.romanText.rtObjects.RTAtom "music21.romanText.rtObjects.RTAtom")
* [`RTToken`](#music21.romanText.rtObjects.RTToken "music21.romanText.rtObjects.RTToken")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`RTOptionalKeyOpen`](#music21.romanText.rtObjects.RTOptionalKeyOpen "music21.romanText.rtObjects.RTOptionalKeyOpen") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`RTOptionalKeyOpen`](#music21.romanText.rtObjects.RTOptionalKeyOpen "music21.romanText.rtObjects.RTOptionalKeyOpen") methods

RTOptionalKeyOpen.getKey()[[source]](../_modules/music21/romanText/rtObjects.html#RTOptionalKeyOpen.getKey)

Methods inherited from [`RTAtom`](#music21.romanText.rtObjects.RTAtom "music21.romanText.rtObjects.RTAtom"):

|  |  |  |
| --- | --- | --- |
| * [`isAtom()`](#music21.romanText.rtObjects.RTAtom.isAtom "music21.romanText.rtObjects.RTAtom.isAtom") |  |  |

Methods inherited from [`RTToken`](#music21.romanText.rtObjects.RTToken "music21.romanText.rtObjects.RTToken"):

|  |  |  |
| --- | --- | --- |
| * [`isAnalyst()`](#music21.romanText.rtObjects.RTToken.isAnalyst "music21.romanText.rtObjects.RTToken.isAnalyst") * [`isComposer()`](#music21.romanText.rtObjects.RTToken.isComposer "music21.romanText.rtObjects.RTToken.isComposer") * [`isForm()`](#music21.romanText.rtObjects.RTToken.isForm "music21.romanText.rtObjects.RTToken.isForm") * [`isKeySignature()`](#music21.romanText.rtObjects.RTToken.isKeySignature "music21.romanText.rtObjects.RTToken.isKeySignature") * [`isMeasure()`](#music21.romanText.rtObjects.RTToken.isMeasure "music21.romanText.rtObjects.RTToken.isMeasure") | * [`isMovement()`](#music21.romanText.rtObjects.RTToken.isMovement "music21.romanText.rtObjects.RTToken.isMovement") * [`isNote()`](#music21.romanText.rtObjects.RTToken.isNote "music21.romanText.rtObjects.RTToken.isNote") * [`isPedal()`](#music21.romanText.rtObjects.RTToken.isPedal "music21.romanText.rtObjects.RTToken.isPedal") * [`isPiece()`](#music21.romanText.rtObjects.RTToken.isPiece "music21.romanText.rtObjects.RTToken.isPiece") * [`isProofreader()`](#music21.romanText.rtObjects.RTToken.isProofreader "music21.romanText.rtObjects.RTToken.isProofreader") | * [`isTimeSignature()`](#music21.romanText.rtObjects.RTToken.isTimeSignature "music21.romanText.rtObjects.RTToken.isTimeSignature") * [`isTitle()`](#music21.romanText.rtObjects.RTToken.isTitle "music21.romanText.rtObjects.RTToken.isTitle") * [`isVersion()`](#music21.romanText.rtObjects.RTToken.isVersion "music21.romanText.rtObjects.RTToken.isVersion") * [`isWork()`](#music21.romanText.rtObjects.RTToken.isWork "music21.romanText.rtObjects.RTToken.isWork") |

## RTPhraseBoundary

class music21.romanText.rtObjects.RTPhraseBoundary(*src='||'*, *container=None*)[[source]](../_modules/music21/romanText/rtObjects.html#RTPhraseBoundary)
:   ```python
    >>> phrase = romanText.rtObjects.RTPhraseBoundary('||')
    >>> phrase
    <music21.romanText.rtObjects.RTPhraseBoundary '||'>
    ```

[`RTPhraseBoundary`](#music21.romanText.rtObjects.RTPhraseBoundary "music21.romanText.rtObjects.RTPhraseBoundary") bases

* [`RTPhraseMarker`](#music21.romanText.rtObjects.RTPhraseMarker "music21.romanText.rtObjects.RTPhraseMarker")
* [`RTAtom`](#music21.romanText.rtObjects.RTAtom "music21.romanText.rtObjects.RTAtom")
* [`RTToken`](#music21.romanText.rtObjects.RTToken "music21.romanText.rtObjects.RTToken")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`RTPhraseBoundary`](#music21.romanText.rtObjects.RTPhraseBoundary "music21.romanText.rtObjects.RTPhraseBoundary") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`RTPhraseBoundary`](#music21.romanText.rtObjects.RTPhraseBoundary "music21.romanText.rtObjects.RTPhraseBoundary") methods

Methods inherited from [`RTAtom`](#music21.romanText.rtObjects.RTAtom "music21.romanText.rtObjects.RTAtom"):

|  |  |  |
| --- | --- | --- |
| * [`isAtom()`](#music21.romanText.rtObjects.RTAtom.isAtom "music21.romanText.rtObjects.RTAtom.isAtom") |  |  |

Methods inherited from [`RTToken`](#music21.romanText.rtObjects.RTToken "music21.romanText.rtObjects.RTToken"):

|  |  |  |
| --- | --- | --- |
| * [`isAnalyst()`](#music21.romanText.rtObjects.RTToken.isAnalyst "music21.romanText.rtObjects.RTToken.isAnalyst") * [`isComposer()`](#music21.romanText.rtObjects.RTToken.isComposer "music21.romanText.rtObjects.RTToken.isComposer") * [`isForm()`](#music21.romanText.rtObjects.RTToken.isForm "music21.romanText.rtObjects.RTToken.isForm") * [`isKeySignature()`](#music21.romanText.rtObjects.RTToken.isKeySignature "music21.romanText.rtObjects.RTToken.isKeySignature") * [`isMeasure()`](#music21.romanText.rtObjects.RTToken.isMeasure "music21.romanText.rtObjects.RTToken.isMeasure") | * [`isMovement()`](#music21.romanText.rtObjects.RTToken.isMovement "music21.romanText.rtObjects.RTToken.isMovement") * [`isNote()`](#music21.romanText.rtObjects.RTToken.isNote "music21.romanText.rtObjects.RTToken.isNote") * [`isPedal()`](#music21.romanText.rtObjects.RTToken.isPedal "music21.romanText.rtObjects.RTToken.isPedal") * [`isPiece()`](#music21.romanText.rtObjects.RTToken.isPiece "music21.romanText.rtObjects.RTToken.isPiece") * [`isProofreader()`](#music21.romanText.rtObjects.RTToken.isProofreader "music21.romanText.rtObjects.RTToken.isProofreader") | * [`isTimeSignature()`](#music21.romanText.rtObjects.RTToken.isTimeSignature "music21.romanText.rtObjects.RTToken.isTimeSignature") * [`isTitle()`](#music21.romanText.rtObjects.RTToken.isTitle "music21.romanText.rtObjects.RTToken.isTitle") * [`isVersion()`](#music21.romanText.rtObjects.RTToken.isVersion "music21.romanText.rtObjects.RTToken.isVersion") * [`isWork()`](#music21.romanText.rtObjects.RTToken.isWork "music21.romanText.rtObjects.RTToken.isWork") |

## RTPhraseMarker

class music21.romanText.rtObjects.RTPhraseMarker(*src=''*, *container=None*)[[source]](../_modules/music21/romanText/rtObjects.html#RTPhraseMarker)
:   A Phrase Marker:

    ```python
    >>> rtPhraseMarker = romanText.rtObjects.RTPhraseMarker('')
    >>> rtPhraseMarker
    <music21.romanText.rtObjects.RTPhraseMarker ''>
    ```

[`RTPhraseMarker`](#music21.romanText.rtObjects.RTPhraseMarker "music21.romanText.rtObjects.RTPhraseMarker") bases

* [`RTAtom`](#music21.romanText.rtObjects.RTAtom "music21.romanText.rtObjects.RTAtom")
* [`RTToken`](#music21.romanText.rtObjects.RTToken "music21.romanText.rtObjects.RTToken")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`RTPhraseMarker`](#music21.romanText.rtObjects.RTPhraseMarker "music21.romanText.rtObjects.RTPhraseMarker") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`RTPhraseMarker`](#music21.romanText.rtObjects.RTPhraseMarker "music21.romanText.rtObjects.RTPhraseMarker") methods

Methods inherited from [`RTAtom`](#music21.romanText.rtObjects.RTAtom "music21.romanText.rtObjects.RTAtom"):

|  |  |  |
| --- | --- | --- |
| * [`isAtom()`](#music21.romanText.rtObjects.RTAtom.isAtom "music21.romanText.rtObjects.RTAtom.isAtom") |  |  |

Methods inherited from [`RTToken`](#music21.romanText.rtObjects.RTToken "music21.romanText.rtObjects.RTToken"):

|  |  |  |
| --- | --- | --- |
| * [`isAnalyst()`](#music21.romanText.rtObjects.RTToken.isAnalyst "music21.romanText.rtObjects.RTToken.isAnalyst") * [`isComposer()`](#music21.romanText.rtObjects.RTToken.isComposer "music21.romanText.rtObjects.RTToken.isComposer") * [`isForm()`](#music21.romanText.rtObjects.RTToken.isForm "music21.romanText.rtObjects.RTToken.isForm") * [`isKeySignature()`](#music21.romanText.rtObjects.RTToken.isKeySignature "music21.romanText.rtObjects.RTToken.isKeySignature") * [`isMeasure()`](#music21.romanText.rtObjects.RTToken.isMeasure "music21.romanText.rtObjects.RTToken.isMeasure") | * [`isMovement()`](#music21.romanText.rtObjects.RTToken.isMovement "music21.romanText.rtObjects.RTToken.isMovement") * [`isNote()`](#music21.romanText.rtObjects.RTToken.isNote "music21.romanText.rtObjects.RTToken.isNote") * [`isPedal()`](#music21.romanText.rtObjects.RTToken.isPedal "music21.romanText.rtObjects.RTToken.isPedal") * [`isPiece()`](#music21.romanText.rtObjects.RTToken.isPiece "music21.romanText.rtObjects.RTToken.isPiece") * [`isProofreader()`](#music21.romanText.rtObjects.RTToken.isProofreader "music21.romanText.rtObjects.RTToken.isProofreader") | * [`isTimeSignature()`](#music21.romanText.rtObjects.RTToken.isTimeSignature "music21.romanText.rtObjects.RTToken.isTimeSignature") * [`isTitle()`](#music21.romanText.rtObjects.RTToken.isTitle "music21.romanText.rtObjects.RTToken.isTitle") * [`isVersion()`](#music21.romanText.rtObjects.RTToken.isVersion "music21.romanText.rtObjects.RTToken.isVersion") * [`isWork()`](#music21.romanText.rtObjects.RTToken.isWork "music21.romanText.rtObjects.RTToken.isWork") |

## RTRepeat

class music21.romanText.rtObjects.RTRepeat(*src=''*, *container=None*)[[source]](../_modules/music21/romanText/rtObjects.html#RTRepeat)
:   ```python
    >>> repeat = romanText.rtObjects.RTRepeat('||:')
    >>> repeat
    <music21.romanText.rtObjects.RTRepeat '||:'>
    ```

[`RTRepeat`](#music21.romanText.rtObjects.RTRepeat "music21.romanText.rtObjects.RTRepeat") bases

* [`RTAtom`](#music21.romanText.rtObjects.RTAtom "music21.romanText.rtObjects.RTAtom")
* [`RTToken`](#music21.romanText.rtObjects.RTToken "music21.romanText.rtObjects.RTToken")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`RTRepeat`](#music21.romanText.rtObjects.RTRepeat "music21.romanText.rtObjects.RTRepeat") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`RTRepeat`](#music21.romanText.rtObjects.RTRepeat "music21.romanText.rtObjects.RTRepeat") methods

Methods inherited from [`RTAtom`](#music21.romanText.rtObjects.RTAtom "music21.romanText.rtObjects.RTAtom"):

|  |  |  |
| --- | --- | --- |
| * [`isAtom()`](#music21.romanText.rtObjects.RTAtom.isAtom "music21.romanText.rtObjects.RTAtom.isAtom") |  |  |

Methods inherited from [`RTToken`](#music21.romanText.rtObjects.RTToken "music21.romanText.rtObjects.RTToken"):

|  |  |  |
| --- | --- | --- |
| * [`isAnalyst()`](#music21.romanText.rtObjects.RTToken.isAnalyst "music21.romanText.rtObjects.RTToken.isAnalyst") * [`isComposer()`](#music21.romanText.rtObjects.RTToken.isComposer "music21.romanText.rtObjects.RTToken.isComposer") * [`isForm()`](#music21.romanText.rtObjects.RTToken.isForm "music21.romanText.rtObjects.RTToken.isForm") * [`isKeySignature()`](#music21.romanText.rtObjects.RTToken.isKeySignature "music21.romanText.rtObjects.RTToken.isKeySignature") * [`isMeasure()`](#music21.romanText.rtObjects.RTToken.isMeasure "music21.romanText.rtObjects.RTToken.isMeasure") | * [`isMovement()`](#music21.romanText.rtObjects.RTToken.isMovement "music21.romanText.rtObjects.RTToken.isMovement") * [`isNote()`](#music21.romanText.rtObjects.RTToken.isNote "music21.romanText.rtObjects.RTToken.isNote") * [`isPedal()`](#music21.romanText.rtObjects.RTToken.isPedal "music21.romanText.rtObjects.RTToken.isPedal") * [`isPiece()`](#music21.romanText.rtObjects.RTToken.isPiece "music21.romanText.rtObjects.RTToken.isPiece") * [`isProofreader()`](#music21.romanText.rtObjects.RTToken.isProofreader "music21.romanText.rtObjects.RTToken.isProofreader") | * [`isTimeSignature()`](#music21.romanText.rtObjects.RTToken.isTimeSignature "music21.romanText.rtObjects.RTToken.isTimeSignature") * [`isTitle()`](#music21.romanText.rtObjects.RTToken.isTitle "music21.romanText.rtObjects.RTToken.isTitle") * [`isVersion()`](#music21.romanText.rtObjects.RTToken.isVersion "music21.romanText.rtObjects.RTToken.isVersion") * [`isWork()`](#music21.romanText.rtObjects.RTToken.isWork "music21.romanText.rtObjects.RTToken.isWork") |

## RTRepeatStart

class music21.romanText.rtObjects.RTRepeatStart(*src='||:'*, *container=None*)[[source]](../_modules/music21/romanText/rtObjects.html#RTRepeatStart)
:   ```python
    >>> repeat = romanText.rtObjects.RTRepeatStart()
    >>> repeat
    <music21.romanText.rtObjects.RTRepeatStart ...'||:'>
    ```

[`RTRepeatStart`](#music21.romanText.rtObjects.RTRepeatStart "music21.romanText.rtObjects.RTRepeatStart") bases

* [`RTRepeat`](#music21.romanText.rtObjects.RTRepeat "music21.romanText.rtObjects.RTRepeat")
* [`RTAtom`](#music21.romanText.rtObjects.RTAtom "music21.romanText.rtObjects.RTAtom")
* [`RTToken`](#music21.romanText.rtObjects.RTToken "music21.romanText.rtObjects.RTToken")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`RTRepeatStart`](#music21.romanText.rtObjects.RTRepeatStart "music21.romanText.rtObjects.RTRepeatStart") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`RTRepeatStart`](#music21.romanText.rtObjects.RTRepeatStart "music21.romanText.rtObjects.RTRepeatStart") methods

Methods inherited from [`RTAtom`](#music21.romanText.rtObjects.RTAtom "music21.romanText.rtObjects.RTAtom"):

|  |  |  |
| --- | --- | --- |
| * [`isAtom()`](#music21.romanText.rtObjects.RTAtom.isAtom "music21.romanText.rtObjects.RTAtom.isAtom") |  |  |

Methods inherited from [`RTToken`](#music21.romanText.rtObjects.RTToken "music21.romanText.rtObjects.RTToken"):

|  |  |  |
| --- | --- | --- |
| * [`isAnalyst()`](#music21.romanText.rtObjects.RTToken.isAnalyst "music21.romanText.rtObjects.RTToken.isAnalyst") * [`isComposer()`](#music21.romanText.rtObjects.RTToken.isComposer "music21.romanText.rtObjects.RTToken.isComposer") * [`isForm()`](#music21.romanText.rtObjects.RTToken.isForm "music21.romanText.rtObjects.RTToken.isForm") * [`isKeySignature()`](#music21.romanText.rtObjects.RTToken.isKeySignature "music21.romanText.rtObjects.RTToken.isKeySignature") * [`isMeasure()`](#music21.romanText.rtObjects.RTToken.isMeasure "music21.romanText.rtObjects.RTToken.isMeasure") | * [`isMovement()`](#music21.romanText.rtObjects.RTToken.isMovement "music21.romanText.rtObjects.RTToken.isMovement") * [`isNote()`](#music21.romanText.rtObjects.RTToken.isNote "music21.romanText.rtObjects.RTToken.isNote") * [`isPedal()`](#music21.romanText.rtObjects.RTToken.isPedal "music21.romanText.rtObjects.RTToken.isPedal") * [`isPiece()`](#music21.romanText.rtObjects.RTToken.isPiece "music21.romanText.rtObjects.RTToken.isPiece") * [`isProofreader()`](#music21.romanText.rtObjects.RTToken.isProofreader "music21.romanText.rtObjects.RTToken.isProofreader") | * [`isTimeSignature()`](#music21.romanText.rtObjects.RTToken.isTimeSignature "music21.romanText.rtObjects.RTToken.isTimeSignature") * [`isTitle()`](#music21.romanText.rtObjects.RTToken.isTitle "music21.romanText.rtObjects.RTToken.isTitle") * [`isVersion()`](#music21.romanText.rtObjects.RTToken.isVersion "music21.romanText.rtObjects.RTToken.isVersion") * [`isWork()`](#music21.romanText.rtObjects.RTToken.isWork "music21.romanText.rtObjects.RTToken.isWork") |

## RTRepeatStop

class music21.romanText.rtObjects.RTRepeatStop(*src=':||'*, *container=None*)[[source]](../_modules/music21/romanText/rtObjects.html#RTRepeatStop)
:   ```python
    >>> repeat = romanText.rtObjects.RTRepeatStop()
    >>> repeat
    <music21.romanText.rtObjects.RTRepeatStop ...':||'>
    ```

[`RTRepeatStop`](#music21.romanText.rtObjects.RTRepeatStop "music21.romanText.rtObjects.RTRepeatStop") bases

* [`RTRepeat`](#music21.romanText.rtObjects.RTRepeat "music21.romanText.rtObjects.RTRepeat")
* [`RTAtom`](#music21.romanText.rtObjects.RTAtom "music21.romanText.rtObjects.RTAtom")
* [`RTToken`](#music21.romanText.rtObjects.RTToken "music21.romanText.rtObjects.RTToken")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`RTRepeatStop`](#music21.romanText.rtObjects.RTRepeatStop "music21.romanText.rtObjects.RTRepeatStop") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`RTRepeatStop`](#music21.romanText.rtObjects.RTRepeatStop "music21.romanText.rtObjects.RTRepeatStop") methods

Methods inherited from [`RTAtom`](#music21.romanText.rtObjects.RTAtom "music21.romanText.rtObjects.RTAtom"):

|  |  |  |
| --- | --- | --- |
| * [`isAtom()`](#music21.romanText.rtObjects.RTAtom.isAtom "music21.romanText.rtObjects.RTAtom.isAtom") |  |  |

Methods inherited from [`RTToken`](#music21.romanText.rtObjects.RTToken "music21.romanText.rtObjects.RTToken"):

|  |  |  |
| --- | --- | --- |
| * [`isAnalyst()`](#music21.romanText.rtObjects.RTToken.isAnalyst "music21.romanText.rtObjects.RTToken.isAnalyst") * [`isComposer()`](#music21.romanText.rtObjects.RTToken.isComposer "music21.romanText.rtObjects.RTToken.isComposer") * [`isForm()`](#music21.romanText.rtObjects.RTToken.isForm "music21.romanText.rtObjects.RTToken.isForm") * [`isKeySignature()`](#music21.romanText.rtObjects.RTToken.isKeySignature "music21.romanText.rtObjects.RTToken.isKeySignature") * [`isMeasure()`](#music21.romanText.rtObjects.RTToken.isMeasure "music21.romanText.rtObjects.RTToken.isMeasure") | * [`isMovement()`](#music21.romanText.rtObjects.RTToken.isMovement "music21.romanText.rtObjects.RTToken.isMovement") * [`isNote()`](#music21.romanText.rtObjects.RTToken.isNote "music21.romanText.rtObjects.RTToken.isNote") * [`isPedal()`](#music21.romanText.rtObjects.RTToken.isPedal "music21.romanText.rtObjects.RTToken.isPedal") * [`isPiece()`](#music21.romanText.rtObjects.RTToken.isPiece "music21.romanText.rtObjects.RTToken.isPiece") * [`isProofreader()`](#music21.romanText.rtObjects.RTToken.isProofreader "music21.romanText.rtObjects.RTToken.isProofreader") | * [`isTimeSignature()`](#music21.romanText.rtObjects.RTToken.isTimeSignature "music21.romanText.rtObjects.RTToken.isTimeSignature") * [`isTitle()`](#music21.romanText.rtObjects.RTToken.isTitle "music21.romanText.rtObjects.RTToken.isTitle") * [`isVersion()`](#music21.romanText.rtObjects.RTToken.isVersion "music21.romanText.rtObjects.RTToken.isVersion") * [`isWork()`](#music21.romanText.rtObjects.RTToken.isWork "music21.romanText.rtObjects.RTToken.isWork") |

## RTTagged

class music21.romanText.rtObjects.RTTagged(*src=''*)[[source]](../_modules/music21/romanText/rtObjects.html#RTTagged)
:   In romanText, some data elements are tags, that is a tag name, a colon,
    optional whitespace, and data. In non-RTTagged elements, there is just
    data.

    All tagged tokens are subclasses of this class. Examples are:

    > Title: Die Jahrzeiten
    > Composer: Fanny Mendelssohn

    ```python
    >>> rtTag = romanText.rtObjects.RTTagged('Title: Die Jahrzeiten')
    >>> rtTag.tag
    'Title'
    >>> rtTag.data
    'Die Jahrzeiten'
    >>> rtTag.isTitle()
    True
    >>> rtTag.isComposer()
    False
    ```

[`RTTagged`](#music21.romanText.rtObjects.RTTagged "music21.romanText.rtObjects.RTTagged") bases

* [`RTToken`](#music21.romanText.rtObjects.RTToken "music21.romanText.rtObjects.RTToken")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`RTTagged`](#music21.romanText.rtObjects.RTTagged "music21.romanText.rtObjects.RTTagged") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`RTTagged`](#music21.romanText.rtObjects.RTTagged "music21.romanText.rtObjects.RTTagged") methods

RTTagged.isAnalyst()[[source]](../_modules/music21/romanText/rtObjects.html#RTTagged.isAnalyst)
:   True if tag represents an analyst, otherwise False.

    ```python
    >>> tag = romanText.rtObjects.RTTagged('Analyst: This is an analyst.')
    >>> tag.isAnalyst()
    True
    ```

    ```python
    >>> tag = romanText.rtObjects.RTTagged('Nothing: Nothing at all.')
    >>> tag.isAnalyst()
    False
    ```

RTTagged.isComposer()[[source]](../_modules/music21/romanText/rtObjects.html#RTTagged.isComposer)
:   True is the tag represents a composer.

    ```python
    >>> rth = romanText.rtObjects.RTTagged('Composer: Claudio Monteverdi')
    >>> rth.isComposer()
    True
    >>> rth.isTitle()
    False
    >>> rth.isWork()
    False
    >>> rth.data
    'Claudio Monteverdi'
    ```

RTTagged.isForm()[[source]](../_modules/music21/romanText/rtObjects.html#RTTagged.isForm)
:   True if tag represents a form, otherwise False.

    ```python
    >>> tag = romanText.rtObjects.RTTagged('Form: This is a form.')
    >>> tag.isForm()
    True
    ```

    ```python
    >>> tag = romanText.rtObjects.RTTagged('Nothing: Nothing at all.')
    >>> tag.isForm()
    False
    ```

RTTagged.isKeySignature()[[source]](../_modules/music21/romanText/rtObjects.html#RTTagged.isKeySignature)
:   True if tag represents a key signature, otherwise False.

    ```python
    >>> tag = romanText.rtObjects.RTTagged('KeySignature: This is a key signature.')
    >>> tag.isKeySignature()
    True
    >>> tag.data
    'This is a key signature.'
    ```

    KeySignatures are a type of tagged data found outside of measures,
    such as “Key Signature: -1” meaning one flat.

    Key signatures are generally numbers representing the number of sharps (or
    negative for flats). Non-standard key signatures are not supported.

    ```python
    >>> tag = romanText.rtObjects.RTTagged('KeySignature: -3')
    >>> tag.data
    '-3'
    ```

    music21 supports one legacy key signature type: KeySignature: Bb which
    represents a one-flat signature. Important to note: no other key signatures
    of this type are supported. (For instance, KeySignature: Ab has no effect)

    ```python
    >>> tag = romanText.rtObjects.RTTagged('KeySignature: Bb')
    >>> tag.data
    'Bb'
    ```

    Testing that .isKeySignature returns False for non-key signatures:

    ```python
    >>> tag = romanText.rtObjects.RTTagged('Nothing: Nothing at all.')
    >>> tag.isKeySignature()
    False
    ```

    N.B.: this is not the same as a key definition found inside a
    Measure. These are represented by RTKey rtObjects, defined below, and are
    not RTTagged rtObjects, but RTAtom subclasses.

RTTagged.isMovement()[[source]](../_modules/music21/romanText/rtObjects.html#RTTagged.isMovement)
:   True if tag represents a movement, otherwise False.

    ```python
    >>> tag = romanText.rtObjects.RTTagged('Movement: This is a movement.')
    >>> tag.isMovement()
    True
    ```

    ```python
    >>> tag = romanText.rtObjects.RTTagged('Nothing: Nothing at all.')
    >>> tag.isMovement()
    False
    ```

RTTagged.isNote()[[source]](../_modules/music21/romanText/rtObjects.html#RTTagged.isNote)
:   True if tag represents a note, otherwise False.

    ```python
    >>> tag = romanText.rtObjects.RTTagged('Note: This is a note.')
    >>> tag.isNote()
    True
    ```

    ```python
    >>> tag = romanText.rtObjects.RTTagged('Nothing: Nothing at all.')
    >>> tag.isNote()
    False
    ```

RTTagged.isPedal()[[source]](../_modules/music21/romanText/rtObjects.html#RTTagged.isPedal)
:   True if tag represents a pedal, otherwise False.

    ```python
    >>> tag = romanText.rtObjects.RTTagged('Pedal: This is a pedal.')
    >>> tag.isPedal()
    True
    ```

    ```python
    >>> tag = romanText.rtObjects.RTTagged('Nothing: Nothing at all.')
    >>> tag.isPedal()
    False
    ```

RTTagged.isPiece()[[source]](../_modules/music21/romanText/rtObjects.html#RTTagged.isPiece)
:   True if tag represents a piece, otherwise False.

    ```python
    >>> tag = romanText.rtObjects.RTTagged('Piece: This is a piece.')
    >>> tag.isPiece()
    True
    ```

    ```python
    >>> tag = romanText.rtObjects.RTTagged('Nothing: Nothing at all.')
    >>> tag.isPiece()
    False
    ```

RTTagged.isProofreader()[[source]](../_modules/music21/romanText/rtObjects.html#RTTagged.isProofreader)
:   True if tag represents a proofreader, otherwise False.

    ```python
    >>> tag = romanText.rtObjects.RTTagged('Proofreader: This is a proofreader.')
    >>> tag.isProofreader()
    True
    ```

    ```python
    >>> tag = romanText.rtObjects.RTTagged('Nothing: Nothing at all.')
    >>> tag.isProofreader()
    False
    ```

RTTagged.isSeventhMinor()[[source]](../_modules/music21/romanText/rtObjects.html#RTTagged.isSeventhMinor)
:   True if tag represents a configuration setting for setting vii/viio/VII in minor

    ```python
    >>> tag = romanText.rtObjects.RTTagged('Seventh Minor: Courtesy')
    >>> tag.isSeventhMinor()
    True
    >>> tag.data
    'Courtesy'
    ```

RTTagged.isSixthMinor()[[source]](../_modules/music21/romanText/rtObjects.html#RTTagged.isSixthMinor)
:   True if tag represents a configuration setting for setting vi/vio/VI in minor

    ```python
    >>> tag = romanText.rtObjects.RTTagged('Sixth Minor: Flat')
    >>> tag.isSixthMinor()
    True
    >>> tag.data
    'Flat'
    ```

RTTagged.isTimeSignature()[[source]](../_modules/music21/romanText/rtObjects.html#RTTagged.isTimeSignature)
:   True if tag represents a time signature, otherwise False.

    ```python
    >>> tag = romanText.rtObjects.RTTagged('TimeSignature: This is a time signature.')
    >>> tag.isTimeSignature()
    True
    ```

    ```python
    >>> tag = romanText.rtObjects.RTTagged('Nothing: Nothing at all.')
    >>> tag.isTimeSignature()
    False
    ```

    TimeSignature header data can be found intermingled with measures.

RTTagged.isTitle()[[source]](../_modules/music21/romanText/rtObjects.html#RTTagged.isTitle)
:   True if tag represents a title, otherwise False.

    ```python
    >>> tag = romanText.rtObjects.RTTagged('Title: This is a title.')
    >>> tag.isTitle()
    True
    ```

    ```python
    >>> tag = romanText.rtObjects.RTTagged('Nothing: Nothing at all.')
    >>> tag.isTitle()
    False
    ```

RTTagged.isVersion()[[source]](../_modules/music21/romanText/rtObjects.html#RTTagged.isVersion)
:   True if tag defines the version of RomanText standard used,
    otherwise False.

    Pieces without the tag are defined to conform to RomanText 1.0,
    the version described in the ISMIR publication.

    ```python
    >>> rth = romanText.rtObjects.RTTagged('RTVersion: 1.0')
    >>> rth.isTitle()
    False
    >>> rth.isVersion()
    True
    >>> rth.tag
    'RTVersion'
    >>> rth.data
    '1.0'
    ```

RTTagged.isWork()[[source]](../_modules/music21/romanText/rtObjects.html#RTTagged.isWork)
:   True if tag represents a work, otherwise False.

    The “work” is not defined as a header tag, but is used to represent
    all tags, often placed after Composer, for the work or pieces designation.

    ```python
    >>> rth = romanText.rtObjects.RTTagged('Work: BWV232')
    >>> rth.isWork()
    True
    >>> rth.tag
    'Work'
    >>> rth.data
    'BWV232'
    ```

    For historical reasons, the tag ‘Madrigal’ also designates a work.

    ```python
    >>> rth = romanText.rtObjects.RTTagged('Madrigal: 4.12')
    >>> rth.isTitle()
    False
    >>> rth.isWork()
    True
    >>> rth.tag
    'Madrigal'
    >>> rth.data
    '4.12'
    ```

Methods inherited from [`RTToken`](#music21.romanText.rtObjects.RTToken "music21.romanText.rtObjects.RTToken"):

|  |  |  |
| --- | --- | --- |
| * [`isAtom()`](#music21.romanText.rtObjects.RTToken.isAtom "music21.romanText.rtObjects.RTToken.isAtom") | * [`isMeasure()`](#music21.romanText.rtObjects.RTToken.isMeasure "music21.romanText.rtObjects.RTToken.isMeasure") |  |

## RTToken

class music21.romanText.rtObjects.RTToken(*src=''*)[[source]](../_modules/music21/romanText/rtObjects.html#RTToken)
:   Stores each linear, logical entity of a RomanText.

    A multi-pass parsing procedure is likely necessary, as RomanText permits
    variety of groupings and markings.

    ```python
    >>> rtt = romanText.rtObjects.RTToken('||:')
    >>> rtt
    <music21.romanText.rtObjects.RTToken '||:'>
    ```

    A standard RTToken returns False for all the following.

    ```python
    >>> rtt.isComposer() or rtt.isTitle() or rtt.isPiece()
    False
    >>> rtt.isAnalyst() or rtt.isProofreader()
    False
    >>> rtt.isTimeSignature() or rtt.isKeySignature() or rtt.isNote()
    False
    >>> rtt.isForm() or rtt.isPedal() or rtt.isMeasure() or rtt.isWork()
    False
    >>> rtt.isMovement() or rtt.isVersion() or rtt.isAtom()
    False
    ```

[`RTToken`](#music21.romanText.rtObjects.RTToken "music21.romanText.rtObjects.RTToken") bases

* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`RTToken`](#music21.romanText.rtObjects.RTToken "music21.romanText.rtObjects.RTToken") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`RTToken`](#music21.romanText.rtObjects.RTToken "music21.romanText.rtObjects.RTToken") methods

RTToken.isAnalyst()[[source]](../_modules/music21/romanText/rtObjects.html#RTToken.isAnalyst)

RTToken.isAtom()[[source]](../_modules/music21/romanText/rtObjects.html#RTToken.isAtom)
:   Atoms are any untagged data; generally only found inside a
    measure definition.

RTToken.isComposer()[[source]](../_modules/music21/romanText/rtObjects.html#RTToken.isComposer)

RTToken.isForm()[[source]](../_modules/music21/romanText/rtObjects.html#RTToken.isForm)
:   Occasionally found in header.

RTToken.isKeySignature()[[source]](../_modules/music21/romanText/rtObjects.html#RTToken.isKeySignature)

RTToken.isMeasure()[[source]](../_modules/music21/romanText/rtObjects.html#RTToken.isMeasure)

RTToken.isMovement()[[source]](../_modules/music21/romanText/rtObjects.html#RTToken.isMovement)

RTToken.isNote()[[source]](../_modules/music21/romanText/rtObjects.html#RTToken.isNote)

RTToken.isPedal()[[source]](../_modules/music21/romanText/rtObjects.html#RTToken.isPedal)

RTToken.isPiece()[[source]](../_modules/music21/romanText/rtObjects.html#RTToken.isPiece)

RTToken.isProofreader()[[source]](../_modules/music21/romanText/rtObjects.html#RTToken.isProofreader)

RTToken.isTimeSignature()[[source]](../_modules/music21/romanText/rtObjects.html#RTToken.isTimeSignature)

RTToken.isTitle()[[source]](../_modules/music21/romanText/rtObjects.html#RTToken.isTitle)

RTToken.isVersion()[[source]](../_modules/music21/romanText/rtObjects.html#RTToken.isVersion)

RTToken.isWork()[[source]](../_modules/music21/romanText/rtObjects.html#RTToken.isWork)
