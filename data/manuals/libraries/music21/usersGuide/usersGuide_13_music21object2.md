Source: https://music21.org/music21docs/usersGuide/usersGuide_13_music21object2.html

# User’s Guide, Chapter 13: More Music21Object Attributes and Properties

At this point you know how to find a `Music21Object`, how to name them
and group them (with `.id` and `.groups`) and how to position them
in Streams (with `.offset`, `.priority`, `.classSortOrder` and the
`.activeSite`). This section gets first into some more advanced things
that Music21Objects have, then some more fun things.

## Sites and the storing of elements

All `Music21Objects` (i.e., elements) have a `.sites` property which
is a [`Sites`](../moduleReference/moduleSites.html#music21.sites.Sites "music21.sites.Sites") object which holds information
about all the places the `Music21Object` is stored in. At its
simplest, it’s something that can be iterated over:

```python
from music21 import *

n = note.Note()
s1 = stream.Stream(id='s1')
s2 = stream.Stream(id='s2')
s1.insert(10, n)
s2.insert(20, n)

for s in n.sites:
    print(s, s.elementOffset(n))
```

```python
 <music21.stream.Stream s1> 10.0
 <music21.stream.Stream s2> 20.0
```

Note that the order of the Streams in `.sites` is guaranteed to be the
order in which the note was inserted into the site.

There’s a lot more that `.sites` can do, but primarily for developers.
We will get back to sites later.

## Derivations

We will talk about derivations more in a future chapter, but we alluded
to them in the Example in chapter 10, so let’s say a few words about
this advanced feature. A [`Derivation`](../moduleReference/moduleDerivation.html#music21.derivation.Derivation "music21.derivation.Derivation")
object is a pointer to an object that this object is derived from in
some way. They’ve gone their separate ways to an extent, but may want to
talk to each other later. A `Music21Object` starts out with no useful
Derivation:

```python
c = note.Note('C4')
c.derivation
```

```python
 <Derivation of <music21.note.Note C> from None>
```

But we can create new notes from it and they’re not totally connected,
but show their connection through `.derivation`:

```python
f = c.transpose('P4')
f
```

```python
 <music21.note.Note F>
```

```python
f.derivation
```

```python
 <Derivation of <music21.note.Note F> from <music21.note.Note C> via 'transpose'>
```

Now `c` has a life of its own from `f`. We can add a sharp to C and
the transpose relationship of F to C does not affect it:

```python
c.pitch.accidental = pitch.Accidental('sharp')
(c, f)
```

```python
 (<music21.note.Note C#>, <music21.note.Note F>)
```

But if `f` wants to do something to `c`, it can by changing itself
and every element of its `.derivation.chain()`:

```python
f.notehead = 'diamond'
for n in f.derivation.chain():
    n.notehead = 'diamond'

(f.notehead, c.notehead)
```

```python
 ('diamond', 'diamond')
```

While `f` can search upwards in its `.derivation.chain()` and find
`c`, `c` cannot find `f` in its derivation; it is a connection
that is designed to be one-way only.

Setting derivations can be done manually, but it’s an advanced enough
topic that we will get to it later.

## Context attributes

Several attributes of `Music21Objects` only work after the object has
been placed inside a Stream that has certain features of their own.

An easy one to understand is `.measureNumber` which finds the
`.number` value of the measure that an object is placed in:

```python
n = note.Note('C')
m = stream.Measure()
m.number = 7
m.append(n)
n.measureNumber
```

```python
 7
```

This works even if a note is inside a voice inside a measure:

```python
v = stream.Voice()
n2 = note.Note('D')
v.append(n2)
m.insert(0, v)
n2.measureNumber
```

```python
 7
```

Without a context, you’ll get None

```python
n3 = note.Note()
n3.measureNumber is None
```

```python
 True
```

The second context attribute is, appropriately, called `.seconds`. It
requires a tempo.MetronomeMark() to be placed into the Stream before the
object and will calculate how many seconds the object (note, etc.) lasts
at that tempo:

```python
m.insert(0, tempo.MetronomeMark('Allegro', 120))
print (n.quarterLength, n.seconds)
```

```python
 1.0 0.5
```

Unlike `.measureNumber` and the rest of the attributes we will see
below, you can change `.seconds` to reflect exact timing you might
have from audio or MIDI data.

```python
n.seconds = 0.6
n.seconds
```

```python
 0.6
```

An object with no tempo information in its surrounding context returns
the special `nan` meaning “not a number” for `.seconds`

```python
n3 = note.Note('E')
n3.seconds
```

```python
 nan
```

So use `math.isnan()` to catch this:

```python
from math import isnan

for el in (n, n2, n3):
    seconds = el.seconds
    if isnan(seconds):
        seconds = 'No information'
    print(el.step, seconds)
```

```python
 C 0.6
 D 0.5
 E No information
```

The last three context attributes, `.beat`, `.beatStr` (beat
string), and `.beatStrength`, all require
`TimeSignature` contexts or they return `nan`
or “nan”. Since they’re the topic of
[our next chapter](usersGuide_14_timeSignatures.html#usersguide-14-timesignatures) we’ll put them
off until then.

Most `Music21Objects` such as `Notes` have many additional
attributes, but these are all the ones that are common to every object
that can go in a `Stream` (after all, what would `.step` mean for a
[`MetronomeMark`](../moduleReference/moduleTempo.html#music21.tempo.MetronomeMark "music21.tempo.MetronomeMark")?)

Note

You may find other attributes on your base.Music21Object, especially if you are running
an older version of music21. They are all deprecated most have been removed in
recent versions; programmers are advised to stick to the safe list of attributes described here.

Before v6.2, .seconds without a TimeSignature in contexts raised an exception.

### Methods on `Music21Objects`

Attributes and properties are aspects of an object that are lightweight
and have no configuration options, so they are accessed without `()`.
Methods tend to do more work and have more options, so they will always
be called with `()` signs.

Unlike attributes, where we have documented all of them, only a subset
of the methods on `Music21Objects` are listed below. All of them can
be found in the documentation to [`Music21Object`](../moduleReference/moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"),
but many of them have obscure uses and might be moved later to not
clutter up what is really important! And those are…

## .getOffsetBySite and .setOffsetBySite

These methods work as the `.offset` attribute but can work on any site
where the object is a part of.

```python
n = note.Note()
s1 = stream.Stream(id='s1')
s1.insert(10, n)
s2 = stream.Stream(id='s2')
s2.insert(20, n)
n.getOffsetBySite(s1)
```

```python
 10.0
```

```python
n.setOffsetBySite(s1, 15.0)
n.getOffsetBySite(s1)
```

```python
 15.0
```

There is one extra possible attribute on `.getOffsetBySite`,
“returnSpecial=True” which will say whether or not an element has a
shifting offset. Right barlines have one:

```python
s3 = stream.Measure()
n3 = note.Note(type='whole')
s3.append(n3)
rb = bar.Barline()
s3.rightBarline = rb
rb.getOffsetBySite(s3)
```

```python
 4.0
```

```python
rb.getOffsetBySite(s3, returnSpecial=True)
```

```python
 <OffsetSpecial.AT_END>
```

And in fact if we change the duration of `n3` the position of the
barline will shift along with it:

```python
n3.duration.type = 'half'
rb.getOffsetBySite(s3)
```

```python
 2.0
```

## getContextByClass()

This is an extremely powerful tool – you might not use it often, but be
assured that `music21` is using it on your behalf all the time when
sophisticated analysis is involved. It finds the active element matching
a certain class preceding the element. Let me demonstrate:

```python
bach = corpus.parse('bwv66.6')
lastNote = bach.recurse().getElementsByClass(note.Note).last()
lastNote
```

```python
 <music21.note.Note F#>
```

What part is it in?

```python
lastNote.getContextByClass(stream.Part)
```

```python
 <music21.stream.Part Bass>
```

What was the Key at that moment?

```python
lastNote.getContextByClass(key.KeySignature)
```

```python
 <music21.key.Key of f# minor>
```

What is the TimeSignature at that moment?

```python
lastNote.getContextByClass(meter.TimeSignature)
```

```python
 <music21.meter.TimeSignature 4/4>
```

Why is this such a sophisticated method? It knows about the differences
in different types of Streams. If the key signature changes in a
different part then it doesn’t affect the notes of the current part, but
if it changes in a previous measure in the same part, then that matters.
Furthermore, the caching mechanism via something called `Timespans` is
amazingly fast, so that running through an entire score getting the
context for each object doesn’t take long at all.

We demonstrate here on an early 15th-century Mass piece that uses four
different time singatures:

```python
gloria = corpus.parse('luca/gloria')
soprano = gloria.parts[0]

lastTimeSignature = None
for n in soprano.recurse().getElementsByClass(note.Note):
    thisTimeSignature = n.getContextByClass(meter.TimeSignature)
    if thisTimeSignature is not lastTimeSignature:
        lastTimeSignature = thisTimeSignature
        print(thisTimeSignature, n.measureNumber)
```

```python
 <music21.meter.TimeSignature 6/8> 1
 <music21.meter.TimeSignature 2/4> 28
 <music21.meter.TimeSignature 6/8> 80
 <music21.meter.TimeSignature 3/4> 110
```

As you might expect, the `.measureNumber` routine uses
`.getContextByClass(stream.Measure)` internally. What is also
interesting is that `.getContextByClass` is smart enough to search out
derivation chains to find what it is looking for. For instance, this
flat stream has only notes, no time signatures. But it can still find
each note’s time signature and measure number context.

Here we will use the string `('TimeSignature')` form of
getContextByClass instead of the class name `(meter.TimeSignature)`

```python
lastTimeSignature = None
for n in soprano.flatten().notes:
    thisTimeSignature = n.getContextByClass('TimeSignature')
    if thisTimeSignature is not lastTimeSignature:
        lastTimeSignature = thisTimeSignature
        print(thisTimeSignature, n.measureNumber)
```

```python
 <music21.meter.TimeSignature 6/8> 1
 <music21.meter.TimeSignature 2/4> 28
 <music21.meter.TimeSignature 6/8> 80
 <music21.meter.TimeSignature 3/4> 110
```

Internally `.getContextByClass` uses another `Music21Object` method
called `.contextSites()` which is a generator that tells the system
where to search next:

```python
for cs in lastNote.contextSites():
    print(cs)
```

```python
 ContextTuple(site=<music21.stream.Measure 9 offset=33.0>, offset=2.0, recurseType=<RecursionType.ELEMENTS_FIRST>)
 ContextTuple(site=<music21.stream.Part Bass>, offset=35.0, recurseType=<RecursionType.FLATTEN>)
 ContextTuple(site=<music21.stream.Score bach/bwv66.6.mxl>, offset=35.0, recurseType=<RecursionType.ELEMENTS_ONLY>)
```

`.contextSites` returns a “ContextTuple” which is a lightweight
namedtuple that has three attributes, `site`, `offset`, and
`recurseType`.

The first ContextTuple says that first the elements of `site`: Measure
9 should be searched, beginning at `offset` 2.0 and (because
`recurseType` is
[`RecursionType`](../moduleReference/moduleStreamEnums.html#music21.stream.enums.RecursionType "music21.stream.enums.RecursionType").ELEMENTS\_FIRST) working
backwards to the beginning of the measure, then if the matching context
isn’t found, the measure will be flattened (in case there are other
voices in the measure) and anything from before offset 2.0 of that
flattened stream will be searched.

If that fails, then the Bass part as a whole will be searched, with all
elements flattened, beginning at offset 35 and working backwards. That
way if the context is in another measure it will be found.

Then if that fails, it will look at the score as a whole, beginning at
offset 35 and working backwards, but only looking at things that are at
the score level, not looking at elements within other parts. There may
be scores where for instance, expressive markings appear at the Score
level. This will find them.

Related to `.getContextByClass()` is `.getAllContextsByClass()`
which is a generator that returns each preceding context.

Note

Two known bugs that we hope to get fixed soon: if there are two or more
contexts at the same offset, .getAllContextsByClass() will skip over
all but one of them. Using Music21Object as a class list can create infinite loops.

```python
lastGloriaNote = soprano.recurse().notes.last()

for ts in lastGloriaNote.getAllContextsByClass(meter.TimeSignature):
    print(ts, ts.measureNumber)
```

```python
 <music21.meter.TimeSignature 3/4> 110
 <music21.meter.TimeSignature 6/8> 80
 <music21.meter.TimeSignature 2/4> 28
 <music21.meter.TimeSignature 6/8> 1
```

Similar to `.getContextByClass()` are the `.next(class)` and
`.previous(class)` methods which move to the next or previous element
of the same class at the same (or a higher) hierarchical level. They’re
designed to be really easy to use, but so far, I’ve failed at achieving
that. Hopefully in the next few versions I’ll be able to demonstrate in
practice how these commands were designed to work. For now, I’d suggest
avoiding them.

## Splitting methods

`Music21` has three methods on `Music21Object`s for splitting
them. Eventually the plan is to unite them into a single `.split()`
method, but we’re not there yet.

The three methods are:

* `.splitAtQuarterLength` – splits an object into two objects at the
  given quarter length
* `.splitByQuarterLengths` – splits an object into two or more objects
  according to a list of quarter lengths
* `.splitAtDurations` – takes an object with a complex duration (such
  as 5.0 quarters) and splits it into notatable units.

These all work rather similarly. Behind their seeming simplicity are a
host of complex musical decisions that are being made. Take this rather
complex note (we’re introducing `expressions` and `articulations`
softly here, so that you don’t need to wait for
[Chapter 32](usersGuide_32_articulations.html#usersguide-32-articulations) to encounter them):

```python
n = note.Note('C#5')
n.duration.type = 'whole'
n.articulations = [articulations.Staccato(), articulations.Accent()]
n.lyric = 'hi!'
n.expressions = [expressions.Mordent(), expressions.Trill(), expressions.Fermata()]
n.show()
```

[![../_images/usersGuide_13_music21object2_57_0.png](../_images/usersGuide_13_music21object2_57_0.png)](../_images/usersGuide_13_music21object2_57_0.png)

Now let’s split this note just before beat 4:

```python
splitTuple = n.splitAtQuarterLength(3.0)
s = stream.Stream()
s.append(splitTuple)
s.show()
```

[![../_images/usersGuide_13_music21object2_59_0.png](../_images/usersGuide_13_music21object2_59_0.png)](../_images/usersGuide_13_music21object2_59_0.png)

Notice the choices that `music21` made – the two notes are tied, the
lyrics are sung at the beginning, the accent and mordent appear at the
beginning of the note while the staccato and fermata(!) appear on the
second note, while trill mark gets put onto the first note only. This is
part of the “batteries included” `music21` approach – try to do
something musically smart in most cases. In fact, it’s even a bit
smarter – the `splitTuple` knows that there’s something called a
TrillExtension spanner in it which should be put into the Stream:

```python
splitTuple.spannerList
```

```python
 [<music21.expressions.TrillExtension <music21.note.Note C#><music21.note.Note C#>>]
```

```python
for thisSpanner in splitTuple.spannerList:
    s.insert(0, thisSpanner)
s.show()
```

[![../_images/usersGuide_13_music21object2_62_0.png](../_images/usersGuide_13_music21object2_62_0.png)](../_images/usersGuide_13_music21object2_62_0.png)

## Showing and Writing

The two last methods are almost certainly the most important:
`.show()` and `.write()`. We’ve been using `.show()` throughout
the User’s Guide, so it’s familiar. It usually takes a single argument
which is the format (default is `'musicxml'` except on IPython where
it is `'musicxml.png'`. `.write()` by contrast writes out the file
to disk. The first argument is again the format. The second argument,
optional, is the filename with path. If omitted then a temporary file is
written (and the filename is returned).

We’ll see enough about `.show()` and `.write()` later, so that’s
enough for now on this long chapter. Let’s return to the `.beat`
related function in
[Chapter 14, Time Signatures](usersGuide_14_timeSignatures.html#usersguide-14-timesignatures).
