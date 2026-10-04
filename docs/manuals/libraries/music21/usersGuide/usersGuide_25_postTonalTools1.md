Source: https://music21.org/music21docs/usersGuide/usersGuide_25_postTonalTools1.html

# User’s Guide, Chapter 25: Post-Tonal Tools (1)

The music21 toolkit features many tools for analyzing and creating music
within a post-tonal context. A [`Chord`](../moduleReference/moduleChord.html#music21.chord.Chord "music21.chord.Chord") can be
identified as a Forte class, a list of pitch classes can be used to
create a 12-tone matrix, and many other analytical tools are available.

This overview will illustrate key features of music21’s post-tonal
tools. For complete documentation on post-tonal tools, see the many
methods in [`Chord`](../moduleReference/moduleChord.html#music21.chord.Chord "music21.chord.Chord") as well as the objects in
[music21.serial](../moduleReference/moduleSerial.html#moduleserial), such as
[`TwelveToneMatrix`](../moduleReference/moduleSerial.html#music21.serial.TwelveToneMatrix "music21.serial.TwelveToneMatrix") and
[`TwelveToneRow`](../moduleReference/moduleSerial.html#music21.serial.TwelveToneRow "music21.serial.TwelveToneRow").

## Pitches as Pitch Classes

Any music21 [`Pitch`](../moduleReference/modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch"), or a
[`Note`](../moduleReference/moduleNote.html#music21.note.Note "music21.note.Note") containing Pitch, can be expressed as
pitch class integers using the
[`pitchClass`](../moduleReference/modulePitch.html#music21.pitch.Pitch.pitchClass "music21.pitch.Pitch.pitchClass") and
[`pitchClassString`](../moduleReference/modulePitch.html#music21.pitch.Pitch.pitchClassString "music21.pitch.Pitch.pitchClassString")
properties.

In the following example, the [`parse()`](../moduleReference/moduleCorpus.html#music21.corpus.parse "music21.corpus.parse") function
is used to create a `Score` object. The
[`id`](../moduleReference/moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") attribute of each contained
`Part` is presented in a list.

We’ll start our look at post-tonal music with a most-decidedly tonal
piece, Beethoven’s Opus 59.

```python
from music21 import *
aScore = corpus.parse('beethoven/opus59no2', 3)
[e.id for e in aScore.parts]
```

```python
 ['Violin I.', 'Violin II.', 'Viola.', 'Violoncello.']
```

We can view the fourth and fifth measures of the violin Part by
obtaining the Part from the Stream with
`getElementById()` method. Next, we can
extract the desired measures with the
`measures()` method. Calling the
[`show()`](../moduleReference/moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") method will, assuming correct
setup of your environment, open a display of the extracted measures.

```python
vlnPart = aScore.getElementById('Violin I.')
mRange = vlnPart.measures(4, 7)
mRange.show()
```

[![../_images/usersGuide_25_postTonalTools1_6_0.png](../_images/usersGuide_25_postTonalTools1_6_0.png)](../_images/usersGuide_25_postTonalTools1_6_0.png)

If we want to gather all [`Pitch`](../moduleReference/modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") objects from
this measure range, we can use the
`pitches` property. This returns
a list of all Pitch objects. All pitch objects have
[`pitchClass`](../moduleReference/modulePitch.html#music21.pitch.Pitch.pitchClass "music21.pitch.Pitch.pitchClass") and
[`pitchClassString`](../moduleReference/modulePitch.html#music21.pitch.Pitch.pitchClassString "music21.pitch.Pitch.pitchClassString")
properties, providing either integer or string representations,
respectively.

```python
', '.join([str(p) for p in mRange.pitches])
```

```python
 'A4, F#4, G4, G4, B4, E5, G5, G5, G5, C#6, E6, E6, E6, G6, C#5'
```

```python
[p.pitchClass for p in mRange.pitches]
```

```python
 [9, 6, 7, 7, 11, 4, 7, 7, 7, 1, 4, 4, 4, 7, 1]
```

If we want to label the notes in our measure range with the Note’s pitch
class representation, we can iterate over the notes and assign the pitch
class representation to the Note’s lyric. This is a common way to
annotate Note and Chord objects in music21. The results can be displayed
with the `show()` method.

Here is the image from when we were using a Beethoven Quartet as an
example:

```python
for n in mRange.recurse().notes:
    if n.tie is None or n.tie.type == 'start':
        n.lyric = n.pitch.pitchClassString
mRange.show()
```

[![../_images/usersGuide_25_postTonalTools1_11_0.png](../_images/usersGuide_25_postTonalTools1_11_0.png)](../_images/usersGuide_25_postTonalTools1_11_0.png)

## Chords as Forte Set Classes

Any music21 Chord can be interpreted as a Forte set class. Additionally,
a wide variety of analytical features, derived from the Forte set class,
are available as methods of the chord.

For an example, let’s create a sequence of generated
aggregate-completing trichords stored on a Stream. That is, we will
construct chords with pitch classes, drawing them from a list of all
pitch classes. These pitches will be supplied to a Chord object and
stored on a Stream.

```python
aStream = stream.Stream()
src = list(range(12)) # cheate a list of integers 0 through 11
src = src[2:4] + src[0:2] + src[8:9] + src[4:8] + src[9:12] # recombine
for i in range(0, 12, 3):
    aStream.append(chord.Chord(src[i:i + 3]))

aStream.show()
```

[![../_images/usersGuide_25_postTonalTools1_14_0.png](../_images/usersGuide_25_postTonalTools1_14_0.png)](../_images/usersGuide_25_postTonalTools1_14_0.png)

These Chords, like all Chords in music21, can be interpreted as Forte
set classes. The Chord object offers numerous methods that retrieve data
from the set class representation of the Chord. The following is just a
sampling of some of the many relevant methods.

```python
for c in aStream:
    print(c.orderedPitchClassesString)
```

```python
 <023>
 <148>
 <567>
 <9AB>
```

```python
for c in aStream:
    print(c.forteClass)
```

```python
 3-2B
 3-11A
 3-1
 3-1
```

```python
for c in aStream:
    print(c.forteClassTnI)
```

```python
 3-2
 3-11
 3-1
 3-1
```

```python
for c in aStream:
    print(c.normalOrder)
```

```python
 [0, 2, 3]
 [1, 4, 8]
 [5, 6, 7]
 [9, 10, 11]
```

```python
for c in aStream:
    print(c.primeFormString)
```

```python
 <013>
 <037>
 <012>
 <012>
```

```python
for c in aStream:
    print(c.intervalVector)
```

```python
 [1, 1, 1, 0, 0, 0]
 [0, 0, 1, 1, 1, 0]
 [2, 1, 0, 0, 0, 0]
 [2, 1, 0, 0, 0, 0]
```

To annotate the Chords stored on the Stream with their Forte name, we
can iterate over the Stream and assign the Forte name to each Chord’s
`lyric` attribute.

```python
for c in aStream:
    c.lyric = c.forteClass
aStream.show()
```

[![../_images/usersGuide_25_postTonalTools1_23_0.png](../_images/usersGuide_25_postTonalTools1_23_0.png)](../_images/usersGuide_25_postTonalTools1_23_0.png)

We can use the `itertools.combinations` function to find all possible
subsets of a chord for a given cardinality. (Hat tip to John Chittum for
the hint). Here is the `all tri-chord hexachord` which contains within
it all possible three-note chords under inversion and transposition:

```python
import itertools
c = chord.Chord([0, 1, 2, 4, 7, 8])
c.commonName
```

```python
 'all tri-chord hexachord'
```

Now we’ll test this create a set to hold the Forte number for each
trichord and see that all twelve of them are there:

```python
cc = set()
for i in itertools.combinations(c.pitches, 3):
    cc.add(chord.Chord(i).forteClassNumber)
cc
```

```python
 {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
```

## Creating and Processing Twelve-Tone Matrices

The music21 [music21.serial](../moduleReference/moduleSerial.html#moduleserial) module provides a Stream-based
representation of a 12-Tone row, as well as the ability to view these
rows as a matrix. Additionally, numerous 12-tone rows from works are
available as classes.

For example, we can create an instance of the row from Alban Berg’s
*Violin Concerto*, use the `show()` method to display its contents as
text, and then create and print a
[`TwelveToneMatrix`](../moduleReference/moduleSerial.html#music21.serial.TwelveToneMatrix "music21.serial.TwelveToneMatrix") object.

```python
aRow = serial.getHistoricalRowByName('RowBergViolinConcerto')
aRow.show('text')
```

```python
 {0.0} <music21.note.Note G>
 {1.0} <music21.note.Note B->
 {2.0} <music21.note.Note D>
 {3.0} <music21.note.Note F#>
 {4.0} <music21.note.Note A>
 {5.0} <music21.note.Note C>
 {6.0} <music21.note.Note E>
 {7.0} <music21.note.Note G#>
 {8.0} <music21.note.Note B>
 {9.0} <music21.note.Note C#>
 {10.0} <music21.note.Note E->
 {11.0} <music21.note.Note F>
```

```python
aMatrix = aRow.matrix()
print(aMatrix)
```

```python
   0  3  7  B  2  5  9  1  4  6  8  A
   9  0  4  8  B  2  6  A  1  3  5  7
   5  8  0  4  7  A  2  6  9  B  1  3
   1  4  8  0  3  6  A  2  5  7  9  B
   A  1  5  9  0  3  7  B  2  4  6  8
   7  A  2  6  9  0  4  8  B  1  3  5
   3  6  A  2  5  8  0  4  7  9  B  1
   B  2  6  A  1  4  8  0  3  5  7  9
   8  B  3  7  A  1  5  9  0  2  4  6
   6  9  1  5  8  B  3  7  A  0  2  4
   4  7  B  3  6  9  1  5  8  A  0  2
   2  5  9  1  4  7  B  3  6  8  A  0
```

We might divide this row into trichords, present each of those trichords
as Chords, and label the resulting pitch classes and Forte set class. As
shown above, we can set the `lyric` attribute to assign a single line
of text. If we need to assign multiple lines of text, the Note and Chord
method [`addLyric()`](../moduleReference/moduleNote.html#music21.note.GeneralNote.addLyric "music21.note.GeneralNote.addLyric") can be used to add
successive lines.

```python
bStream = stream.Stream()
for i in range(0, 12, 3):
    c = chord.Chord(aRow[i:i + 3])
    c.addLyric(c.primeFormString)
    c.addLyric(c.forteClass)
    bStream.append(c)
bStream.show()
```

[![../_images/usersGuide_25_postTonalTools1_33_0.png](../_images/usersGuide_25_postTonalTools1_33_0.png)](../_images/usersGuide_25_postTonalTools1_33_0.png)

This should give a decent introduction to working with post-tonal music
– we’ll return to this when we discuss searching for post-tonal
structures, but there’s still a lot to find in a Stream, and we want to
take it one step at a time – the best way to do so is to understand
[Chapter 26, Stream Iteration and Filtering](usersGuide_26_iterators.html#usersguide-26-iterators)
