Source: https://music21.org/music21docs/usersGuide/usersGuide_27_graceNotes.html

# User’s Guide, Chapter 27: Grace Notes

Grace notes present particular problems for almost all computer
representations of scores. In one way of theorizing them, they take up
no time whatsoever – you can take a full measure of 4/4 and add two
hundred grace notes and the measure is still not overfull. On the other
hand, they need to take up some time, otherwise how would we hear them?

So we have something that takes up no time, but takes up time, at the
same time. Let’s look more closely at them. Along the way we’ll look at
appogiature, which present some issues that are similar and some that
are different.

## Basic Graces

We’ll begin by creating a 4/4 measure of four quarter notes:

```python
from music21 import *

m = stream.Measure()
m.append(meter.TimeSignature('4/4'))
m.repeatAppend(note.Note('C5'), 4)
m.show()
```

[![../_images/usersGuide_27_graceNotes_1_0.png](../_images/usersGuide_27_graceNotes_1_0.png)](../_images/usersGuide_27_graceNotes_1_0.png)

Now let’s insert a D-grace note just before the third quarter note.
First we create a normal note (usually an eighth note) and then we
create a new grace note with the `getGrace` method.

```python
d = note.Note('D5', type='eighth')
dGrace = d.getGrace()
m.insert(2.0, dGrace)
m.show()
```

[![../_images/usersGuide_27_graceNotes_3_0.png](../_images/usersGuide_27_graceNotes_3_0.png)](../_images/usersGuide_27_graceNotes_3_0.png)

If we look at `dGrace` at first it appears to be just a normal Note:

```python
dGrace
```

```python
 <music21.note.Note D>
```

But its `duration` is a subclass called `GraceDuration`.
Importantly, it is an “unlinked” duration, meaning that the `type`
(e.g. “eighth”) of the duration does not say how long it lasts.

```python
dGrace.duration
```

```python
 <music21.duration.GraceDuration unlinked type:eighth quarterLength:0.0>
```

```python
dGrace.duration.linked
```

```python
 False
```

There is one `DurationTuple` in the `.components` of the
GraceDuration object, and it is an eighth note of length 0.

```python
dGrace.duration.components
```

```python
 (DurationTuple(type='eighth', dots=0, quarterLength=0.0),)
```

A GraceDuration has the boolean attribute `.slash` which says whether
or not it receives a slash. By default this is True.

```python
dGrace.duration.slash
```

```python
 True
```

Within a `Stream` grace notes sort before elements of the same class
that have the same priority and offset. Internally, this is done by
setting `isNotGrace` to 0 in the sort tuple. (normally it is 1).

```python
dGrace.sortTuple()
```

```python
 SortTuple(atEnd=0, offset=2.0, priority=0, classSortOrder=20, isNotGrace=0, insertIndex=110)
```

Normally grace notes are slurred to the following note, so let’s add a
slur there.

```python
thirdNote = m.notes[-2]
sl = spanner.Slur(dGrace, thirdNote)
m.insert(0, sl)
m.show()
```

[![../_images/usersGuide_27_graceNotes_16_0.png](../_images/usersGuide_27_graceNotes_16_0.png)](../_images/usersGuide_27_graceNotes_16_0.png)

## Multiple Grace Notes

Multiple grace notes are normally beamed together and generally written
as sixteenth or thirty-second notes. We’ll add two graces to the last C
in the measure:

```python
eGrace = note.Note('E5', type='16th').getGrace()
dGrace2 = note.Note('D5', type='16th').getGrace()
eGrace.beams.fill(2, 'start')
dGrace2.beams.fill(2, 'stop')
m.insert(3.0, eGrace)
m.insert(3.0, dGrace2)
m.show()
```

[![../_images/usersGuide_27_graceNotes_19_0.png](../_images/usersGuide_27_graceNotes_19_0.png)](../_images/usersGuide_27_graceNotes_19_0.png)

Notice that the grace notes are ordered according to the principle,
“first inserted = left-most, last inserted = right-most.” If you know
every note to be inserted in advance, then there’s no problem getting
the order right. But suppose you need to change it later? In this case,
change the priority of the grace notes:

```python
dGrace2.priority = -1
m.show()
```

[![../_images/usersGuide_27_graceNotes_21_0.png](../_images/usersGuide_27_graceNotes_21_0.png)](../_images/usersGuide_27_graceNotes_21_0.png)

Note that the default priority of all objects is 0, so that by giving a
priority higher than 1, the grace notes can be made to follow the main
note:

```python
dGrace2.priority = 1
eGrace.priority = 2
m.show()
```

[![../_images/usersGuide_27_graceNotes_23_0.png](../_images/usersGuide_27_graceNotes_23_0.png)](../_images/usersGuide_27_graceNotes_23_0.png)

This is useful for cases such as putting a “Nachschlag” or
“Nachschlagen” after a trill:

```python
p = stream.Part()
m1 = stream.Measure()
n2 = note.Note('F#5', type='whole')
nach1 = note.Note('E5', type='16th').getGrace()
nach2 = note.Note('F#5', type='16th').getGrace()
nach1.priority = 1
nach2.priority = 2

trMark = expressions.Trill()
n2.expressions.append(trMark)

m1.insert(0, n2)
m1.insert(0, nach1)
m1.insert(0, nach2)

p.append(m1)

m2 = stream.Measure()
nResolve = note.Note('G5', type='whole')
m2.append(nResolve)
p.append(m2)

# nResolve is necessary because
# MuseScore has a bug with spanners that end with grace notes.
nachSlur = spanner.Slur([nach1, nach2, nResolve])
p.insert(0, nachSlur)

# beams are also created automagically on show
p.show()
```

[![../_images/usersGuide_27_graceNotes_25_0.png](../_images/usersGuide_27_graceNotes_25_0.png)](../_images/usersGuide_27_graceNotes_25_0.png)

## Stealing time

`.stealTimePrevious` and `.stealTimeFollowing` are values from 0 to
1 that show what fraction of the previous or following note’s durations
should be allocated to make room for this grace note.

MIDI output does not yet support playing back grace notes.

## Chordify and Grace Notes

By default, music21 includes GraceNotes when creating chords via
`chordify`:

```python
m.chordify().show()
```

[![../_images/usersGuide_27_graceNotes_28_0.png](../_images/usersGuide_27_graceNotes_28_0.png)](../_images/usersGuide_27_graceNotes_28_0.png)

While this behavior may be desirable in some cases, for many uses, it is
unlikely to result in chords that are intended. However, it is easy to
create a Stream that removes the grace notes. First, let’s make a copy
of the measure, so we do not change the original:

```python
import copy
mCopy = copy.deepcopy(m)
```

Next, we will keep track of every grace note to remove:

```python
graceNotes = []
for n in mCopy.recurse().notes:
    if n.duration.isGrace:
        graceNotes.append(n)

graceNotes
```

```python
 [<music21.note.Note D>, <music21.note.Note D>, <music21.note.Note E>]
```

Next remove them from their activeSite (which might be a `Voice`
within a measure, etc.). This is done in a separate step because
removing objects from an iterator during iteration leads to bad
consequences:

```python
for grace in graceNotes:
    grace.activeSite.remove(grace)
```

```python
mCopy.chordify().show()
```

[![../_images/usersGuide_27_graceNotes_35_0.png](../_images/usersGuide_27_graceNotes_35_0.png)](../_images/usersGuide_27_graceNotes_35_0.png)

(Alternatively, this could be done in one step if
`mCopy.recurse().notes` was replaced with
`list(mCopy.recurse().notes)`, but better to be explicit about what we
are doing than implicit.)

## Appogiature

Appogiature are not yet fully supported by music21. Documentation here
is a TODO.

That’s enough on grace notes for now. Let’s move to finding things with
something to say:
[Chapter 28: Lyric Searching](usersGuide_28_lyricSearcher.html#usersguide-28-lyricsearcher)
