Source: https://music21.org/music21docs/moduleReference/moduleMusedataBase40.html

# music21.musedata.base40

Implementation of Walter Hewlett’s base40 system for musical intervals.
(See Hewlett and Ann K. Blombach 1989 article)

## BaseN

class music21.musedata.base40.BaseN(*order=2*)[[source]](../_modules/music21/musedata/base40.html#BaseN)

[`BaseN`](#music21.musedata.base40.BaseN "music21.musedata.base40.BaseN") methods

BaseN.generateLetters()[[source]](../_modules/music21/musedata/base40.html#BaseN.generateLetters)

## Functions

music21.musedata.base40.base40ActualInterval(*base40NumA*, *base40NumB*)[[source]](../_modules/music21/musedata/base40.html#base40ActualInterval)
:   Calculates a music21 Interval between two Base40 pitch
    numbers, as calculated using the music21.interval module.

    Raises a Base40 Exception if (a) Either of the Base40 pitch
    numbers does not correspond to a pitch name or (b) If
    an unusual interval is encountered that can’t be handled
    by music21.

    ```python
    >>> musedata.base40.base40ActualInterval(163, 191)
    <music21.interval.Interval m6>
    >>> musedata.base40.base40ActualInterval(186, 174)  # Descending M3
    <music21.interval.Interval M-3>
    >>> musedata.base40.base40ActualInterval(1, 5)
    <music21.interval.Interval AAAA1>
    >>> musedata.base40.base40ActualInterval(1, 3)
    <music21.interval.Interval AA1>
    >>> musedata.base40.base40ActualInterval(2, 6)
    Traceback (most recent call last):
    music21.musedata.base40.Base40Exception: Pitch name not assigned to this Base40 number 6
    ```

music21.musedata.base40.base40DeltaToInterval(*delta*)[[source]](../_modules/music21/musedata/base40.html#base40DeltaToInterval)
:   Returns a music21 Interval between two Base40 pitch numbers
    given the delta (difference) between them.

    Raises a Base40 Exception if the interval is not handled by Base40.
    Base40 can only handle major, minor, perfect, augmented,
    and diminished intervals. Although not for certain, it seems
    that the engineers that designed this system assumed that
    other intervals (doubly augmented intervals, for instance)
    would be of a very rare occurrence, and extreme intervals
    which would trigger an incorrect answer (C– to C##, for
    instance, would return a diminished second, even though it’s
    a quadruplely augmented unison) just would not occur.

    ```python
    >>> musedata.base40.base40DeltaToInterval(4)
    <music21.interval.Interval d2>
    >>> musedata.base40.base40DeltaToInterval(11)
    <music21.interval.Interval m3>
    >>> musedata.base40.base40DeltaToInterval(23)
    <music21.interval.Interval P5>
    >>> musedata.base40.base40DeltaToInterval(-23)
    <music21.interval.Interval P-5>
    >>> musedata.base40.base40DeltaToInterval(52)
    <music21.interval.Interval M10>
    >>> musedata.base40.base40DeltaToInterval(-52)
    <music21.interval.Interval M-10>
    >>> musedata.base40.base40DeltaToInterval(77)
    Traceback (most recent call last):
    music21.musedata.base40.Base40Exception: Interval not handled by Base40 37
    ```

music21.musedata.base40.base40Interval(*base40NumA*, *base40NumB*)[[source]](../_modules/music21/musedata/base40.html#base40Interval)
:   Returns a music21 Interval between two base40 pitch
    numbers, using their delta (difference) as defined
    in Base40. The interval provided is without direction.

    Raises a Base40 Exception if the delta doesn’t correspond
    to an interval in Base40, or if either base40 pitch
    number doesn’t correspond to a pitch name.

    ```python
    >>> musedata.base40.base40Interval(163, 191)
    <music21.interval.Interval m6>
    ```

    ```python
    >>> musedata.base40.base40Interval(186, 174)      # Descending M3
    <music21.interval.Interval M-3>
    ```

    Base40 has limitations for intervals smaller than diminished or bigger than augmented.

    ```python
    >>> musedata.base40.base40Interval(1, 5)
    Traceback (most recent call last):
    music21.musedata.base40.Base40Exception: Base40 cannot compute interval between 1 and 5.
    ```

    ```python
    >>> musedata.base40.base40Interval(1, 3)
    Traceback (most recent call last):
    music21.musedata.base40.Base40Exception: Interval not handled by Base40 2
    ```

    ```python
    >>> musedata.base40.base40Interval(2, 6)
    Traceback (most recent call last):
    music21.musedata.base40.Base40Exception: Pitch name not assigned to this Base40 number 6
        Interval does not exist
    ```

    ```python
    >>> musedata.base40.base40Interval(12, 6)
    Traceback (most recent call last):
    music21.musedata.base40.Base40Exception: Pitch name not assigned to these Base40 numbers
        12 and 6 Interval does not exist
    ```

music21.musedata.base40.base40ToPitch(*base40Num*)[[source]](../_modules/music21/musedata/base40.html#base40ToPitch)
:   Converts a Base40 pitch number into a music21 Pitch.
    The Base40 number is octave specific.

    Raises a Base40 Exception if the Base40 pitch number given doesn’t
    have an associated pitch name. There is one unassigned number
    each time the interval between two letters is a whole step.

    ```python
    >>> musedata.base40.base40ToPitch(1)
    <music21.pitch.Pitch C--1>
    >>> musedata.base40.base40ToPitch(40)
    <music21.pitch.Pitch B##1>
    >>> musedata.base40.base40ToPitch(23)
    Traceback (most recent call last):
    music21.musedata.base40.Base40Exception: Pitch name not assigned to this Base40 number 23
    >>> musedata.base40.base40ToPitch(186)
    <music21.pitch.Pitch G5>
    ```

music21.musedata.base40.pitchToBase40(*pitchToConvert*)[[source]](../_modules/music21/musedata/base40.html#pitchToBase40)
:   Converts a pitch string or a music21 Pitch into a Base40
    pitch number. The Base40 number is octave specific.

    Raises a Base40 Exception if the pitch to convert is outside the set
    of pitches that Base40 can handle; for example, half flats
    and half sharps or triple flats and triple sharps.

    ```python
    >>> musedata.base40.pitchToBase40(pitch.Pitch('C--5'))
    161
    >>> musedata.base40.pitchToBase40('F##4')
    142
    >>> musedata.base40.pitchToBase40('F###4')
    Traceback (most recent call last):
    music21.musedata.base40.Base40Exception: Base40 cannot handle this pitch F###4
    ```

music21.musedata.base40.quickEnharmonicString(*nameStr*, *allowDoubleAccidentals=True*)[[source]](../_modules/music21/musedata/base40.html#quickEnharmonicString)
:   Takes a name of a string and returns a list of the quick lower and higher enharmonics, limited
    to double sharps and double flats (or to single sharps and single flats if
    allowDoubleAccidentals is False)

    ```python
    >>> musedata.base40.quickEnharmonicString('C')
    ['B#', 'D--']
    >>> musedata.base40.quickEnharmonicString('C', allowDoubleAccidentals=False)
    ['B#']
    >>> musedata.base40.quickEnharmonicString('G')
    ['F##', 'A--']
    ```

music21.musedata.base40.quickHigherEnharmonicString(*nameStr*, *allowDoubleAccidentals=True*)[[source]](../_modules/music21/musedata/base40.html#quickHigherEnharmonicString)
:   Takes a name of a string and returns a list of the quick higher enharmonics, limited
    to double sharps and double flats (or to single sharps and single flats if
    allowDoubleAccidentals is False)

    ```python
    >>> musedata.base40.quickHigherEnharmonicString('F#')
    ['G-']
    >>> musedata.base40.quickHigherEnharmonicString('C##')
    ['D', 'E--']
    >>> musedata.base40.quickHigherEnharmonicString('C##', allowDoubleAccidentals=False)
    ['D']
    >>> musedata.base40.quickHigherEnharmonicString('B#')
    ['C', 'D--']
    ```

music21.musedata.base40.quickLowerEnharmonicString(*nameStr*, *allowDoubleAccidentals=True*)[[source]](../_modules/music21/musedata/base40.html#quickLowerEnharmonicString)
:   Takes a name of a string and returns a list of the quick lower enharmonics, limited
    to double sharps and double flats (or to single sharps and single flats if
    allowDoubleAccidentals is False)

    ```python
    >>> musedata.base40.quickLowerEnharmonicString('B-')
    ['A#']
    >>> musedata.base40.quickLowerEnharmonicString('G-')
    ['F#', 'E##']
    >>> musedata.base40.quickLowerEnharmonicString('G-', allowDoubleAccidentals=False)
    ['F#']
    >>> musedata.base40.quickLowerEnharmonicString('C-')
    ['B', 'A##']
    ```
