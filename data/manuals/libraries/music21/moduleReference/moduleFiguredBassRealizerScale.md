Source: https://music21.org/music21docs/moduleReference/moduleFiguredBassRealizerScale.html

# music21.figuredBass.realizerScale

## FiguredBassScale

class music21.figuredBass.realizerScale.FiguredBassScale(*scaleValue='C'*, *scaleMode='major'*)[[source]](../_modules/music21/figuredBass/realizerScale.html#FiguredBassScale)
:   Acts as a wrapper for [`Scale`](moduleScale.html#music21.scale.Scale "music21.scale.Scale"). Used to represent the
    concept of a figured bass scale, with a scale value and mode.

    Accepted scale types: major, minor, dorian, phrygian, and hypophrygian.
    A FiguredBassScaleException is raised if an invalid scale type is provided.

    ```python
    >>> from music21.figuredBass import realizerScale
    >>> fbScale = realizerScale.FiguredBassScale()
    >>> fbScale.realizerScale
    <music21.scale.MajorScale C major>
    >>> fbScale.keySig
    <music21.key.KeySignature of no sharps or flats>
    ```

    ```python
    >>> fbScale = realizerScale.FiguredBassScale('d', 'minor')
    >>> fbScale.realizerScale
    <music21.scale.MinorScale D minor>
    >>> fbScale.keySig
    <music21.key.KeySignature of 1 flat>
    ```

[`FiguredBassScale`](#music21.figuredBass.realizerScale.FiguredBassScale "music21.figuredBass.realizerScale.FiguredBassScale") methods

FiguredBassScale.getPitchNames(*bassPitch*, *notationString=None*)[[source]](../_modules/music21/figuredBass/realizerScale.html#FiguredBassScale.getPitchNames)
:   Takes a bassPitch and notationString and returns a list of corresponding
    pitch names based on the scale value and mode above and inclusive of the
    bassPitch name.

    ```python
    >>> from music21.figuredBass import realizerScale
    >>> fbScale = realizerScale.FiguredBassScale()
    >>> fbScale.getPitchNames('D3', '6')
    ['D', 'F', 'B']
    >>> fbScale.getPitchNames('G3')
    ['G', 'B', 'D']
    >>> fbScale.getPitchNames('B3', '6,#5')
    ['B', 'D', 'F#', 'G']
    >>> fbScale.getPitchNames('C#3', '-7')  # Fully diminished seventh chord
    ['C#', 'E', 'G', 'B-']
    ```

FiguredBassScale.getPitches(*bassPitch*, *notationString=None*, *maxPitch=None*)[[source]](../_modules/music21/figuredBass/realizerScale.html#FiguredBassScale.getPitches)
:   Takes in a bassPitch, a notationString, and a maxPitch representing the highest
    possible pitch that can be returned. Returns a sorted list of pitches which
    correspond to the pitches of each specific pitch name found through getPitchNames
    that fall between the bassPitch and the maxPitch, inclusive of both.

    if maxPitch is None, then B5 s used instead.

    ```python
    >>> from music21.figuredBass import realizerScale
    >>> fbScale = realizerScale.FiguredBassScale()
    ```

    Root position triad

    ```python
    >>> [str(p) for p in fbScale.getPitches('C3') ]
    ['C3', 'E3', 'G3', 'C4', 'E4', 'G4', 'C5', 'E5', 'G5']
    ```

    First inversion triad

    ```python
    >>> [str(p) for p in fbScale.getPitches('D3', '6') ]
    ['D3', 'F3', 'B3', 'D4', 'F4', 'B4', 'D5', 'F5', 'B5']
    ```

    Root position seventh chord, showing MaxPitch

    ```python
    >>> fbScale.getPitches(pitch.Pitch('G3'), '7', 'F4')
    [<music21.pitch.Pitch G3>, <music21.pitch.Pitch B3>,
     <music21.pitch.Pitch D4>, <music21.pitch.Pitch F4>]
    ```

FiguredBassScale.getSamplePitches(*bassPitch*, *notationString=None*)[[source]](../_modules/music21/figuredBass/realizerScale.html#FiguredBassScale.getSamplePitches)
:   Returns all pitches for a bassPitch and notationString within
    an octave of the bassPitch, inclusive of the bassPitch but
    exclusive at the upper bound. In other words, this method
    returns the most compact complete chord implied by the bassPitch
    and its figures.

    ```python
    >>> from music21.figuredBass import realizerScale
    >>> fbScale = realizerScale.FiguredBassScale()
    ```

    ```python
    >>> fbScale.getSamplePitches('D3', '6')  # First inversion triad
    [<music21.pitch.Pitch D3>, <music21.pitch.Pitch F3>, <music21.pitch.Pitch B3>]
    ```

    Root position triad

    ```python
    >>> [str(p) for p in fbScale.getSamplePitches('G3') ]
    ['G3', 'B3', 'D4']
    ```

    First inversion seventh chord

    ```python
    >>> [str(p) for p in fbScale.getSamplePitches('B3', '6,5') ]
    ['B3', 'D4', 'F4', 'G4']
    ```

    Neapolitan chord

    ```python
    >>> [str(p) for p in fbScale.getSamplePitches('F3', '-6,-') ]
    ['F3', 'A-3', 'D-4']
    ```

    Second inversion seventh chord

    ```python
    >>> [str(p) for p in fbScale.getSamplePitches('C5', '4,3') ]
    ['C5', 'E5', 'F5', 'A5']
    ```

    Fully diminished seventh chord

    ```python
    >>> [str(p) for p in fbScale.getSamplePitches('C#3', '-7') ]
    ['C#3', 'E3', 'G3', 'B-3']
    ```

[`FiguredBassScale`](#music21.figuredBass.realizerScale.FiguredBassScale "music21.figuredBass.realizerScale.FiguredBassScale") instance variables

FiguredBassScale.keySig
:   A [`KeySignature`](moduleKey.html#music21.key.KeySignature "music21.key.KeySignature") corresponding to
    the scale value and mode.

FiguredBassScale.realizerScale
:   A [`Scale`](moduleScale.html#music21.scale.Scale "music21.scale.Scale") based on the
    desired value and mode.
