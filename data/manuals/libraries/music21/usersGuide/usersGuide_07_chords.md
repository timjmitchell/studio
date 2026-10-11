Source: https://music21.org/music21docs/usersGuide/usersGuide_07_chords.html

# User’s Guide, Chapter 7: Chords

Chords, as the name might suggest, are objects that combine multiple
[`Pitch`](../moduleReference/modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") objects on a single stem. They can be
found in the [music21.chord](../moduleReference/moduleChord.html#modulechord) module. The most general way to create
a [`Chord`](../moduleReference/moduleChord.html#music21.chord.Chord "music21.chord.Chord") object is by passing in a list of
pitch names you want in the chord:

```python
from music21 import *
cMinor = chord.Chord(['C4','G4','E-5'])
```

`Note` and `Chord` objects, since both are subclasses of the
[`GeneralNote`](../moduleReference/moduleNote.html#music21.note.GeneralNote "music21.note.GeneralNote") object share many features in
common:

```python
cMinor.duration.type = 'half'
cMinor.quarterLength
```

```python
 2.0
```

But since a `Chord` contains many pitches, it does not have a
`.pitch` attribute:

```python
cMinor.pitch
```

```python
---------------------------------------------------------------------------

AttributeError                            Traceback (most recent call last)

<ipython-input-3-e8314cc72a18> in <module>
----> 1 cMinor.pitch

AttributeError: 'Chord' object has no attribute 'pitch'
```

Instead it has a [`.pitches`](../moduleReference/moduleChord.html#music21.chord.Chord.pitches "music21.chord.Chord.pitches")
attribute which returns a Tuple of pitches in the Chord.

```python
cMinor.pitches
```

```python
 (<music21.pitch.Pitch C4>, <music21.pitch.Pitch G4>, <music21.pitch.Pitch E-5>)
```

A little bit more about Python. `.pitches` returns a tuple, what’s
that? A tuple is like a list, except that unlike a list which has square
brackets around it, a tuple has parentheses around it:

```python
baroqueTuple = ('Strozzi', 'Bach', 'Handel', 'Telemann')
classicalList = ['Mozart', 'Haydn', 'Saint-George', 'Beethoven']

baroqueTuple
```

```python
 ('Strozzi', 'Bach', 'Handel', 'Telemann')
```

```python
classicalList
```

```python
 ['Mozart', 'Haydn', 'Saint-George', 'Beethoven']
```

Both tuples and lists can find members by accessing them with numbers in
square brackets:

```python
baroqueTuple[0]
```

```python
 'Strozzi'
```

```python
classicalList[0]
```

```python
 'Mozart'
```

But the biggest difference between the two is that you can manipulate a
list, but not a tuple. If we try to add someone to the classicalList,
using `.append` it works great.

```python
classicalList.append('Ella Fitzgerald') # she's a classic to me...

classicalList
```

```python
 ['Mozart', 'Haydn', 'Saint-George', 'Beethoven', 'Ella Fitzgerald']
```

```python
classicalList.remove('Mozart')

classicalList
```

```python
 ['Haydn', 'Saint-George', 'Beethoven', 'Ella Fitzgerald']
```

But a tuple can’t be changed:

```python
baroqueTuple.append('Miles Davis')
```

```python
---------------------------------------------------------------------------

AttributeError                            Traceback (most recent call last)

<ipython-input-17-fd7e965db659> in <module>
----> 1 baroqueTuple.append('Miles Davis')

AttributeError: 'tuple' object has no attribute 'append'
```

In this case, that’s a shame, because Miles belongs with Bach! So we
shouldn’t have used a tuple there.

But in the class of `.pitches` it makes sense that it returns a tuple,
since changing the result `.pitches` separate from the Chord could be
ambiguous – did you mean to change the result of `.pitches` or to
change the pitches in the chord itself? `music21` will often return
tuples in places where manipulating the result could cause headaches or
bugs down the line. In any case, it’s easy to turn a tuple into a list
or vice versa:

```python
baroqueList = list(baroqueTuple)
baroqueList.append('Miles Davis')
baroqueList
```

```python
 ['Strozzi', 'Bach', 'Handel', 'Telemann', 'Miles Davis']
```

```python
classicalTuple = tuple(classicalList)
classicalTuple
```

```python
 ('Haydn', 'Saint-George', 'Beethoven', 'Ella Fitzgerald')
```

Okay, back to chord, where we left off:

```python
cMinor.pitches
```

```python
 (<music21.pitch.Pitch C4>, <music21.pitch.Pitch G4>, <music21.pitch.Pitch E-5>)
```

But you already knew what pitches were in the `Chord` since you just
created it! What else can you do with it?

How about determining if it is a
[`major`](../moduleReference/moduleChord.html#music21.chord.Chord.isMajorTriad "music21.chord.Chord.isMajorTriad") or a
[`minor`](../moduleReference/moduleChord.html#music21.chord.Chord.isMinorTriad "music21.chord.Chord.isMinorTriad") triad?

```python
cMinor.isMajorTriad()
```

```python
 False
```

```python
cMinor.isMinorTriad()
```

```python
 True
```

You can also figure out if it is in inversion or not:

```python
cMinor.inversion()
```

```python
 0
```

Chords in root position have inversion of 0. But consider this other
chord:

```python
cMajor = chord.Chord(['E3','C4','G4'])
cMajor.inversion()
```

```python
 1
```

With this chord, two other methods become important:

```python
cMajor.root()
```

```python
 <music21.pitch.Pitch C4>
```

```python
cMajor.bass()
```

```python
 <music21.pitch.Pitch E3>
```

You can find the third and fifth of the `Chord` with `.third` and
`.fifth`. Note that these properties do not have `()` after them.
This was a mistake in how we created `music21` and hopefully this will
all be fixed and consistent soon:

```python
cMajor.third
```

```python
 <music21.pitch.Pitch E3>
```

```python
cMajor.fifth
```

```python
 <music21.pitch.Pitch G4>
```

There is also a .seventh property, but it won’t do anything here:

```python
cMajor.seventh
```

The result of that is `None` which we can test like so…

```python
cMajor.seventh is None
```

```python
 True
```

We can append or remove notes from a chord, just like in a set:

```python
dMaj = chord.Chord('D4 F#4')
dMaj.add('A5')
dMaj
```

```python
 <music21.chord.Chord D4 F#4 A5>
```

```python
dMaj.remove('D4')
dMaj
```

```python
 <music21.chord.Chord F#4 A5>
```

```python
dMaj.add(pitch.Pitch('D3'))
dMaj.add(note.Note('F#5'))
dMaj
```

```python
 <music21.chord.Chord D3 F#4 F#5 A5>
```

## Displaying Chords

We can display the `Chord` object just like any
[`Note`](../moduleReference/moduleNote.html#music21.note.Note "music21.note.Note") (Don’t worry if this isn’t working for you
yet…we’ll get this set up in Chapter 8)

```python
cMinor.show()
```

[![../_images/usersGuide_07_chords_48_0.png](../_images/usersGuide_07_chords_48_0.png)](../_images/usersGuide_07_chords_48_0.png)

```python
cMajor.show()
```

[![../_images/usersGuide_07_chords_49_0.png](../_images/usersGuide_07_chords_49_0.png)](../_images/usersGuide_07_chords_49_0.png)

These chords are a bit “spacey”, so let’s get `c` in
[`closedPosition()`](../moduleReference/moduleChord.html#music21.chord.Chord.closedPosition "music21.chord.Chord.closedPosition"):

```python
cClosed = cMinor.closedPosition()
cClosed.show()
```

[![../_images/usersGuide_07_chords_51_0.png](../_images/usersGuide_07_chords_51_0.png)](../_images/usersGuide_07_chords_51_0.png)

Notice that `cMinor` is unchanged. The closed position chord is only
`cClosed`:

```python
cMinor.show()
```

[![../_images/usersGuide_07_chords_53_0.png](../_images/usersGuide_07_chords_53_0.png)](../_images/usersGuide_07_chords_53_0.png)

If we wanted to change the Chord object itself, we call
`.closedPosition(inPlace=True)` which alters the original. Since the
original is altered, we don’t put `x = ...` in front of it.

```python
cMajor.closedPosition(inPlace=True)
cMajor.show()
```

[![../_images/usersGuide_07_chords_55_0.png](../_images/usersGuide_07_chords_55_0.png)](../_images/usersGuide_07_chords_55_0.png)

There is also a method,
[`semiClosedPosition()`](../moduleReference/moduleChord.html#music21.chord.Chord.semiClosedPosition "music21.chord.Chord.semiClosedPosition") which acts like
`.closedPosition` except that if there is already a pitch at that step
(i.e., D-flat and D-sharp are both step “D”), then the note is moved up
an octave. This is useful for displaying complex, post tonal chords in
the most compact form possible:

```python
c1 = chord.Chord(['C4', 'E5', 'C#6', 'E-7', 'G8', 'C9', 'E#9'])
c2 = c1.semiClosedPosition()
c2.show()
```

[![../_images/usersGuide_07_chords_57_0.png](../_images/usersGuide_07_chords_57_0.png)](../_images/usersGuide_07_chords_57_0.png)

We can get the [`common name`](../moduleReference/moduleChord.html#music21.chord.Chord.commonName "music21.chord.Chord.commonName") of
each of these Chords:

```python
cn1 = cMinor.commonName
print(cn1)
```

```python
 minor triad
```

```python
print(cMajor.commonName)
```

```python
 major triad
```

More complex chords have less common “commonNames”. Here’s one that the
American composer Elliott Carter liked a lot.

```python
elliottCarterChord = chord.Chord(['C4','D-4','E4','F#4'])
elliottCarterChord.commonName
```

```python
 'all-interval tetrachord'
```

```python
elliottCarterChord.show()
```

[![../_images/usersGuide_07_chords_63_0.png](../_images/usersGuide_07_chords_63_0.png)](../_images/usersGuide_07_chords_63_0.png)

## More ways of creating chords; Chords and Streams

There are other ways of creating a Chord if you’d like. One way is from
a bunch of already created `Note` objects:

```python
d = note.Note('D4')
fSharp = note.Note('F#4')
a = note.Note('A5')
dMajor = chord.Chord([d, fSharp, a])

dMajor.show()
```

[![../_images/usersGuide_07_chords_66_0.png](../_images/usersGuide_07_chords_66_0.png)](../_images/usersGuide_07_chords_66_0.png)

Or we can pass a string with note names separated by spaces:

```python
e7 = chord.Chord('E4 G#4 B4 D5')
e7.show()
```

[![../_images/usersGuide_07_chords_68_0.png](../_images/usersGuide_07_chords_68_0.png)](../_images/usersGuide_07_chords_68_0.png)

The octaves are optional, especially if everything is within an octave:

```python
es = chord.Chord('E- G B-')
es.show()
```

[![../_images/usersGuide_07_chords_70_0.png](../_images/usersGuide_07_chords_70_0.png)](../_images/usersGuide_07_chords_70_0.png)

But you will definitely want them if a chord crosses the boundary of an
octave (between B and C). Unless you love 6-4 chords, this is probably
not what you want:

```python
fMajor = chord.Chord('F A C')
fMajor.show()
```

[![../_images/usersGuide_07_chords_72_0.png](../_images/usersGuide_07_chords_72_0.png)](../_images/usersGuide_07_chords_72_0.png)

Notice that because C sorts before F and A that the chord is in second
inversion, or 64. We can figure out the inversion of a `Chord` like
so:

```python
print(fMajor.inversion(), fMajor.inversionName())
```

```python
 2 64
```

In addition to .commonName, there are a few other “name” properties that
might be interesting:

```python
fMajor.fullName
```

```python
 'Chord {F | A | C} Quarter'
```

```python
fMajor.pitchedCommonName
```

```python
 'F-major triad'
```

Like `Note` objects, we can put `Chord` objects inside a
`Stream`:

```python
stream1 = stream.Stream()
stream1.append(cMinor)
stream1.append(fMajor)
stream1.append(es)
stream1.show()
```

[![../_images/usersGuide_07_chords_79_0.png](../_images/usersGuide_07_chords_79_0.png)](../_images/usersGuide_07_chords_79_0.png)

We can mix and match `Notes`, [`Rests`](../moduleReference/moduleNote.html#music21.note.Rest "music21.note.Rest"),
and `Chords`:

```python
rest1 = note.Rest()
rest1.quarterLength = 0.5
noteASharp = note.Note('A#5')
noteASharp.quarterLength = 1.5

stream2 = stream.Stream()
stream2.append(cMinor)
stream2.append(rest1)
stream2.append(noteASharp)
stream2.show()
```

[![../_images/usersGuide_07_chords_81_0.png](../_images/usersGuide_07_chords_81_0.png)](../_images/usersGuide_07_chords_81_0.png)

## Post-tonal chords (in brief)

There are a lot of methods for dealing with post-tonal aspects of
chords. If you’re not interested in twentieth century music, go ahead
and skip to the next chapter, but, here are some fun things.

The `intervalVector` of a chord is a list of the number of
`[semitones, whole-tones, minor-thirds/augmented-seconds, major-thirds, perfect fourths, and tritones]`
in the chord or inversion. A minor triad, for instance, has one minor
third (C to E-flat), one major third (E-flat to G), and one perfect
fourth (G to C above, since octave does not matter):

```python
cMinor.intervalVector
```

```python
 [0, 0, 1, 1, 1, 0]
```

A major triad has the same interval vector:

```python
cMajor.intervalVector
```

```python
 [0, 0, 1, 1, 1, 0]
```

The elliottCarterChord is unique in that it has an `.intervalVector`
of all 1’s:

```python
elliottCarterChord.intervalVector
```

```python
 [1, 1, 1, 1, 1, 1]
```

Well, it’s almost unique: there is another chord with the same
`.intervalVector`. That Chord is called its Z-relation or Z-pair.

```python
elliottCarterChord.hasZRelation
```

```python
 True
```

```python
otherECChord = elliottCarterChord.getZRelation()
otherECChord
```

```python
 <music21.chord.Chord C D- E- G>
```

```python
otherECChord.show()
```

[![../_images/usersGuide_07_chords_92_0.png](../_images/usersGuide_07_chords_92_0.png)](../_images/usersGuide_07_chords_92_0.png)

```python
otherECChord.intervalVector
```

```python
 [1, 1, 1, 1, 1, 1]
```

The other post-tonal tools you might be interested in are given below.
We’ll return to them in a later chapter, but here are three important
ones:

```python
print(elliottCarterChord.primeForm)
```

```python
 [0, 1, 4, 6]
```

```python
print(elliottCarterChord.normalOrder)
```

```python
 [0, 1, 4, 6]
```

```python
print(elliottCarterChord.forteClass)
```

```python
 4-15A
```

If you really only care about semitones, you can create a chord just
with the pitchClasses:

```python
oddChord = chord.Chord([1, 3, 7, 9, 10])
oddChord.show()
```

[![../_images/usersGuide_07_chords_99_0.png](../_images/usersGuide_07_chords_99_0.png)](../_images/usersGuide_07_chords_99_0.png)

There’s a little problem with the A and A# being on the same space that
makes it hard to read. Let’s flip the A# to Bb:

```python
oddChord.pitches[-1].getHigherEnharmonic(inPlace=True)
oddChord.show()
```

[![../_images/usersGuide_07_chords_101_0.png](../_images/usersGuide_07_chords_101_0.png)](../_images/usersGuide_07_chords_101_0.png)

If you use pitchClasses above 11, then they are treated as MIDI numbers,
where 60 = MiddleC, 72 = C5, etc. Enharmonic spelling is chosen
automatically.

```python
midiChordType = chord.Chord([60, 65, 70, 75])
midiChordType.show()
```

[![../_images/usersGuide_07_chords_103_0.png](../_images/usersGuide_07_chords_103_0.png)](../_images/usersGuide_07_chords_103_0.png)

Okay, so now you’ve learned the basics (and more!) of Notes and Chords.
If you haven’t been able to see them on your own,
[Chapter 8: Installing MusicXML Readers](usersGuide_08_installingMusicXML.html#usersguide-08-installingmusicxml)
will fix it. It’s also going to cover the basic file formats of
`music21`.
