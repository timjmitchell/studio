Source: https://music21.org/music21docs/moduleReference/moduleStreamStreamStatus.html

# music21.stream.streamStatus

## StreamStatus

class music21.stream.streamStatus.StreamStatus(*client=None*)[[source]](../_modules/music21/stream/streamStatus.html#StreamStatus)
:   An object that stores the current notation state for the client stream.

    Separates out tasks such as whether notation has been made, etc.

    ```python
    >>> s = stream.Stream()
    >>> ss = s.streamStatus
    >>> ss
    <music21.stream.streamStatus.StreamStatus object at 0x...>
    >>> s.streamStatus.client is s
    True
    ```

    Copying of StreamStatus and surrounding Streams

    ```python
    >>> import copy
    >>> ss2 = copy.deepcopy(ss)
    >>> ss2.client is None
    True
    ```

    ```python
    >>> s2 = copy.deepcopy(s)
    >>> s2.streamStatus
    <music21.stream.streamStatus.StreamStatus object at 0x...>
    >>> s2.streamStatus is ss
    False
    >>> s2.streamStatus.client is s2
    True
    ```

[`StreamStatus`](#music21.stream.streamStatus.StreamStatus "music21.stream.streamStatus.StreamStatus") bases

* [`SlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.SlottedObjectMixin "music21.common.objects.SlottedObjectMixin")

[`StreamStatus`](#music21.stream.streamStatus.StreamStatus "music21.stream.streamStatus.StreamStatus") read/write properties

StreamStatus.accidentals

StreamStatus.beams

StreamStatus.tuplets

[`StreamStatus`](#music21.stream.streamStatus.StreamStatus "music21.stream.streamStatus.StreamStatus") methods

StreamStatus.haveAccidentalsBeenMade()[[source]](../_modules/music21/stream/streamStatus.html#StreamStatus.haveAccidentalsBeenMade)
:   If Accidentals.displayStatus is None for all contained pitches, it as
    assumed that accidentals have not been set for display and/or
    makeAccidentals has not been run. If any Accidental has displayStatus
    other than None, this method returns True, regardless of if
    makeAccidentals has actually been run.

StreamStatus.haveBeamsBeenMade()[[source]](../_modules/music21/stream/streamStatus.html#StreamStatus.haveBeamsBeenMade)
:   If any Note in this Stream has .beams defined, it as assumed that Beams
    have not been set and/or makeBeams has not been run. If any Beams
    exist, this method returns True, regardless of if makeBeams has
    actually been run.

StreamStatus.haveTupletBracketsBeenMade()[[source]](../_modules/music21/stream/streamStatus.html#StreamStatus.haveTupletBracketsBeenMade)
:   If any GeneralNote in this Stream is a tuplet, then check to
    see if any of them have a first Tuplet with type besides None
    return True. Otherwise, return False if there is a tuplet. Return None if
    no Tuplets.

    ```python
    >>> s = stream.Stream()
    >>> s.streamStatus.haveTupletBracketsBeenMade() is None
    True
    >>> s.append(note.Note())
    >>> s.streamStatus.haveTupletBracketsBeenMade() is None
    True
    >>> nTuplet = note.Note(quarterLength=1/3)
    >>> s.append(nTuplet)
    >>> s.streamStatus.haveTupletBracketsBeenMade()
    False
    >>> nTuplet.duration.tuplets[0].type = 'start'
    >>> s.streamStatus.haveTupletBracketsBeenMade()
    True
    ```
