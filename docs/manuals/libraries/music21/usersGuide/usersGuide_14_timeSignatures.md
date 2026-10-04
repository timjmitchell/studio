Source: https://music21.org/music21docs/usersGuide/usersGuide_14_timeSignatures.html

# User’s Guide: Chapter 14: Time Signatures and Beats

Up until now almost all the music we’ve been working with has been in
4/4. That’s not because we love common time so much, but simply because
as we noted in [Chapter 4](usersGuide_04_stream1.html#usersguide-04-stream1) it’s because
4/4 is the default time signature for `music21`
`Stream` objects that don’t have another time
signature applied to them.

In general, `TimeSignature` objects are found
within `Measure` objects (a Stream subclass).
However, in some cases `TimeSignature` objects
can exist directly on a Stream.

TimeSignature objects, as a subclass of the
[`Music21Object`](../moduleReference/moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"), have an offset and can be
positioned anywhere on a Stream. When placed in a Measure, TimeSignature
objects are often placed at the start, or zero offset position. The
Measure property
`timeSignature` can be
used to set or get a TimeSignature at the zero offset position. If a
Measure does not have a TimeSignature, the
`timeSignature` property
returns None.

Everything that we need to use other time signatures is contained in the
`meter` module, which is imported when you type
`from music21 import *`. There are lots of things in that module, but
the one that we care about most is the
`TimeSignature` object. Let’s create a couple of
notes and a `TimeSignature` object.

```python
from music21 import *

noteC = note.Note('C4', type='half')
noteD = note.Note('D4', type='quarter')
noteE = note.Note('E4', type='quarter')
noteF = note.Note('F4', type='half')

tsThreeFour = meter.TimeSignature('3/4')

print(tsThreeFour.numerator, '/',  tsThreeFour.denominator)
```

```python
 3 / 4
```

There’s also an easy way of getting this string, call `.ratioString`:

```python
tsThreeFour.ratioString
```

```python
 '3/4'
```

Now that we have our objects, let’s create a
`Stream` object that uses these notes and the
TimeSignature object. We’ll append each object in order using a `for`
loop:

```python
stream1 = stream.Stream()

for thisThing in [tsThreeFour, noteC, noteD, noteE, noteF]:
    stream1.append(thisThing)
```

Let’s look at `stream1` using `.show('text')`:

```python
stream1.show('text')
```

```python
 {0.0} <music21.meter.TimeSignature 3/4>
 {0.0} <music21.note.Note C>
 {2.0} <music21.note.Note D>
 {3.0} <music21.note.Note E>
 {4.0} <music21.note.Note F>
```

Wondering why both the time signature and the first note begin at
`offset` 0.0 in the Stream? That’s because by default TimeSignature
objects have no length:

```python
tsThreeFour.duration.quarterLength
```

```python
 0.0
```

If we [`show()`](../moduleReference/moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") the `Stream` without
using `show('text')`, we see that there are two measures of 3/4:

```python
stream1.show()
```

[![../_images/usersGuide_14_timeSignatures_12_0.png](../_images/usersGuide_14_timeSignatures_12_0.png)](../_images/usersGuide_14_timeSignatures_12_0.png)

The `TimeSignature` object helps the display module known how to
divide the Stream into `Measure` objects. We
can see this process directly if we create a new `Stream` from
`stream1` that has measures using the
`makeMeasures()` command:

```python
stream2 = stream1.makeMeasures()
stream2.show('text')
```

```python
 {0.0} <music21.stream.Measure 1 offset=0.0>
     {0.0} <music21.clef.TrebleClef>
     {0.0} <music21.meter.TimeSignature 3/4>
     {0.0} <music21.note.Note C>
     {2.0} <music21.note.Note D>
 {3.0} <music21.stream.Measure 2 offset=3.0>
     {0.0} <music21.note.Note E>
     {1.0} <music21.note.Note F>
     {3.0} <music21.bar.Barline type=final>
```

The makeMeasures command, by the way, also put a TrebleClef into the
`Stream` and set the last barline to “final”, which makes its output a
little prettier in Lilypond (which is what the documentation uses; you
are probably using MusicXML if you’re following along, which gets it
right…)

```python
stream2.show()
```

[![../_images/usersGuide_14_timeSignatures_16_0.png](../_images/usersGuide_14_timeSignatures_16_0.png)](../_images/usersGuide_14_timeSignatures_16_0.png)

Time signatures have a `.symbol` setting that can be used to change
the display of certain common duple signatures:

```python
s = stream.Stream()
ts0 = meter.TimeSignature('4/4')
ts1 = meter.TimeSignature('4/4')
ts1.symbol = 'common'
ts2 = meter.TimeSignature('2/2')
ts3 = meter.TimeSignature('2/2')
ts3.symbol = 'cut'
s.append(ts0)
s.append(note.Note('C5', type='whole'))
s.append(ts1)
s.append(note.Note('B4', type='whole'))
s.append(ts2)
s.append(note.Note('A4', type='whole'))
s.append(ts3)
s.append(note.Note('G4', type='whole'))
s.makeMeasures(inPlace=True)
s.show()
```

[![../_images/usersGuide_14_timeSignatures_18_0.png](../_images/usersGuide_14_timeSignatures_18_0.png)](../_images/usersGuide_14_timeSignatures_18_0.png)

## Working with Beats in TimeSignatures

Beyond just getting nicely formed measures, TimeSignature objects let us
figure out information about what beat each
[`Note`](../moduleReference/moduleNote.html#music21.note.Note "music21.note.Note") (or [`Rest`](../moduleReference/moduleNote.html#music21.note.Rest "music21.note.Rest") or
[`Chord`](../moduleReference/moduleChord.html#music21.chord.Chord "music21.chord.Chord"), etc.) is on. Let’s return to our Stream
without measures and look at each note’s beat:

```python
stream1.notes[0]
```

```python
 <music21.note.Note C>
```

```python
stream1.notes[0].beat
```

```python
 1.0
```

Okay, so the first note is on beat 1 (represented as 1.0 here). That’s
different from its [`offset`](../moduleReference/moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset")
which is 0.0. Remember that the offset is the number of quarter notes
from the beginning of the containing `Stream`. The
[`beat`](../moduleReference/moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") on the other hand uses
notation that is more familiar to musicians. Let’s look at the beat of
all the notes in the Stream:

```python
for n in stream1.notes:
    print(n, n.beat)
```

```python
 <music21.note.Note C> 1.0
 <music21.note.Note D> 3.0
 <music21.note.Note E> 1.0
 <music21.note.Note F> 2.0
```

If we only wanted to find notes that were on the downbeat we could
filter on beats like so:

```python
for n in stream1.notes:
    if n.beat == 1.0:
        print(n)
```

```python
 <music21.note.Note C>
 <music21.note.Note E>
```

What would happen if the time signature were different? We can find out
by changing the TimeSignature object already in the Stream:

```python
tsThreeFour.ratioString
```

```python
 '3/4'
```

```python
tsThreeFour.ratioString = '2/4'
```

Now the variable name of the TimeSignature object makes little sense,
but we do find that the first, second, and fourth notes are on the
downbeat.

```python
for n in stream1.notes:
    print(n, n.beat)
```

```python
 <music21.note.Note C> 1.0
 <music21.note.Note D> 1.0
 <music21.note.Note E> 2.0
 <music21.note.Note F> 1.0
```

If we change the TimeSignature again to 6/8 then the same notes will be
on the downbeat as in the original 3/4 Stream, but they will have
different beat numbers. This time we’ll use the
`numerator` and
`denominator` to
change the meter. (Remember that all these different tricks are
documented in full at `music21.meter.TimeSignature`.

```python
tsThreeFour.numerator = 6
tsThreeFour.denominator = 8
tsThreeFour
```

```python
 <music21.meter.TimeSignature 6/8>
```

```python
stream1.show()
```

[![../_images/usersGuide_14_timeSignatures_33_0.png](../_images/usersGuide_14_timeSignatures_33_0.png)](../_images/usersGuide_14_timeSignatures_33_0.png)

```python
for n in stream1.notes:
    print(n, n.beat)
```

```python
 <music21.note.Note C> 1.0
 <music21.note.Note D> 7/3
 <music21.note.Note E> 1.0
 <music21.note.Note F> 5/3
```

There is also a variation of `.beat` on every `Music21Object` called
`.beatStr` which returns a string which might look more normal to a
musician.

```python
for n in stream1.notes:
    print(n, n.beatStr)
```

```python
 <music21.note.Note C> 1
 <music21.note.Note D> 2 1/3
 <music21.note.Note E> 1
 <music21.note.Note F> 1 2/3
```

Notice that by default 6/8 is assumed to be a “fast” 6/8, that is,
having two beats and not six per measure. That’s because there’s no easy
way to specify the former. We can see how many beats there are per
measure by requesting the
`beatCount` of a
`TimeSignature`:

```python
tsThreeFour.beatCount
```

```python
 2
```

And we can change that and see how it affects the results:

```python
tsThreeFour.beatCount = 6

for n in stream1.notes:
    print(n, n.beat)
```

```python
 <music21.note.Note C> 1.0
 <music21.note.Note D> 5.0
 <music21.note.Note E> 1.0
 <music21.note.Note F> 3.0
```

Using the terminology most musicians use, you can create TimeSignatures
of 6/8 with either beat count directly:

```python
tsFast68 = meter.TimeSignature('fast 6/8')
tsSlow68 = meter.TimeSignature('slow 6/8')

tsFast68.beatCount, tsSlow68.beatCount
```

```python
 (2, 6)
```

## Working with TimeSignatures in scores

We have been dealing with TimeSignature objects that are in a single
Stream. However, in general, `TimeSignature`
objects are found within `Measure` objects
inside a `Part` object. Both
`Measure` and `Part`
are subclasses of `Stream`. Let’s get a Bach
chorale with some nice eighth-note runs from the [music21.corpus](../moduleReference/moduleCorpus.html#modulecorpus)
module’s [`parse()`](../moduleReference/moduleCorpus.html#music21.corpus.parse "music21.corpus.parse") function. It returns a
`Score`, which is also a `Stream` subclass.

```python
myBach = corpus.parse('bach/bwv57.8')

print(myBach.__class__)
```

```python
 <class 'music21.stream.base.Score'>
```

We will get the Alto part using the `Score` object’s
`parts` list:

```python
alto = myBach.parts['Alto']

alto
```

```python
 <music21.stream.Part Alto>
```

When we call `.show()` on this Part (or on `myBach` itself), we can
see that this is one of the few chorales that Bach wrote that is in 3/4:

```python
alto.show()
```

[![../_images/usersGuide_14_timeSignatures_49_0.png](../_images/usersGuide_14_timeSignatures_49_0.png)](../_images/usersGuide_14_timeSignatures_49_0.png)

To examine the `TimeSignature` object active for
this part, there are a few approaches. One method is to simply search
for the class within all objects in the Part, or the flattened Part
Stream representation. Remember that a Part is generally built of
Measures, or Stream-embedded containers. To get all the elements in the
Stream we can use the `recurse`
method, and then search for a class with the
`getElementsByClass()` method. This returns
an iterator containing all found classes. The first element in this
Stream is the TimeSignature.

```python
alto.recurse().getElementsByClass(meter.TimeSignature)[0]
```

```python
 <music21.meter.TimeSignature 3/4>
```

```python
len(alto.recurse().getElementsByClass(meter.TimeSignature))
```

```python
 1
```

We see that there is exactly one TimeSignature in the `Part`.

Alternatively, we can look at the first Measure in the Stream, and
examine the timeSignature property.

```python
alto.measure(1).timeSignature
```

```python
 <music21.meter.TimeSignature 3/4>
```

Other measures don’t have TimeSignature objects:

```python
alto.measure(7).timeSignature is None
```

```python
 True
```

Let’s change that!

```python
alto.measure(7).timeSignature = meter.TimeSignature('6/8')
```

Now we’ll rebeam according to the new TimeSignatures:

```python
alto.makeBeams(inPlace=True)
```

We’ll clear all the stem directions so that we don’t get really screwy
beams, and then show the new score.

```python
for n in alto.recurse().notes:
    n.stemDirection = 'unspecified'

alto.show()
```

[![../_images/usersGuide_14_timeSignatures_62_0.png](../_images/usersGuide_14_timeSignatures_62_0.png)](../_images/usersGuide_14_timeSignatures_62_0.png)

We’ve sort of cheated by changing the TimeSignature to something that
kept all the measure lengths the same. Let’s rebar everything. First
we’ll flatten the alto part and then get everything that is NOT a
TimeSignature. We will use
`getElementsNotOfClass()` and can either
pass it the string “TimeSignature” as we did with “getElementsByClass”
above, or for either method we can pass in a class object, which we’ll
do here:

```python
newAlto = alto.flatten().getElementsNotOfClass([meter.TimeSignature,
                                                layout.LayoutBase]
                                              ).stream()
newAlto.insert(0, meter.TimeSignature('2/4'))
```

If we make some measures from this, we’ll see that there are problems
around mm. 2-3

```python
newAlto.makeMeasures(inPlace=True)
newAlto.measures(1, 4).show('text', addEndTimes=True)
```

```python
 {0.0 - 2.0} <music21.stream.Measure 1 offset=0.0>
     {0.0 - 0.0} <music21.instrument.Instrument 'P2: Alto: '>
     {0.0 - 0.0} <music21.clef.TrebleClef>
     {0.0 - 0.0} <music21.key.Key of B- major>
     {0.0 - 0.0} <music21.meter.TimeSignature 2/4>
     {0.0 - 1.0} <music21.note.Note F>
     {1.0 - 2.0} <music21.note.Note F>
 {2.0 - 4.5} <music21.stream.Measure 2 offset=2.0>
     {0.0 - 1.0} <music21.note.Note F>
     {1.0 - 2.5} <music21.note.Note F>
 {4.0 - 6.0} <music21.stream.Measure 3 offset=4.0>
     {0.5 - 1.0} <music21.note.Note F>
     {1.0 - 2.0} <music21.note.Note G>
 {6.0 - 8.0} <music21.stream.Measure 4 offset=6.0>
     {0.0 - 1.0} <music21.note.Note C>
     {1.0 - 2.0} <music21.note.Note C>
```

Whoops! The last F of measure 2 is actually too long, and the next
measure’s first F begins half a beat later. Let’s run the powerful
command [`makeNotation()`](../moduleReference/moduleStreamBase.html#music21.stream.base.Stream.makeNotation "music21.stream.base.Stream.makeNotation") first before
showing:

```python
newAltoFixed = newAlto.makeNotation()
newAltoFixed.show()
```

[![../_images/usersGuide_14_timeSignatures_68_0.png](../_images/usersGuide_14_timeSignatures_68_0.png)](../_images/usersGuide_14_timeSignatures_68_0.png)

We can continue to add multiple TimeSignature objects to this Stream of
Notes. First, we will replace the 2/4 bar previously added with a new
TimeSignature, using the Stream `replace()`
method. Then, we will insert a number of additional TimeSignature
objects at offsets further into the Stream. We will use a flat stream
that has no measures, so temporary Measures are automatically created
when calling the `show()`method.

```python
newFlatAlto = newAlto.flatten()
ts = newFlatAlto.getTimeSignatures()[0]
ts
```

```python
 <music21.meter.TimeSignature 2/4>
```

```python
newFlatAlto.replace(ts, meter.TimeSignature('5/8'))
newFlatAlto.getTimeSignatures()[0]
```

```python
 <music21.meter.TimeSignature 5/8>
```

```python
newFlatAlto.insert(10.0, meter.TimeSignature('7/8'))
newFlatAlto.insert(17.0, meter.TimeSignature('9/8'))
newFlatAlto.insert(26.0, meter.TimeSignature('3/8'))
```

Now we can `makeNotation()` again and show this wacky interpretation
of Bach:

```python
newFlatAlto.makeNotation().show()
```

[![../_images/usersGuide_14_timeSignatures_74_0.png](../_images/usersGuide_14_timeSignatures_74_0.png)](../_images/usersGuide_14_timeSignatures_74_0.png)

A quick note: If you only want to gather Notes, Rests, or other
subclasses of GeneralNote, but don’t mind losing other information as
such the [`KeySignature`](../moduleReference/moduleKey.html#music21.key.KeySignature "music21.key.KeySignature") and
[`Instrument`](../moduleReference/moduleInstrument.html#music21.instrument.Instrument "music21.instrument.Instrument") objects, then you achieve the
same change in time signature using the notesAndRests property.
(Otherwise, it’s best to stick with the
`getElementsNotOfClass()` method).

```python
newAlto = alto.flatten().notesAndRests.stream()
newAlto.insert(0.0, meter.TimeSignature('5/8'))
newAlto.insert(10.0, meter.TimeSignature('7/8'))
newAlto.insert(17.0, meter.TimeSignature('9/8'))
newAlto.insert(26.0, meter.TimeSignature('3/8'))
newAlto.makeNotation().show()
```

[![../_images/usersGuide_14_timeSignatures_76_0.png](../_images/usersGuide_14_timeSignatures_76_0.png)](../_images/usersGuide_14_timeSignatures_76_0.png)

Let’s see how that looks in all the parts by putting the time signatures
in their “proper” place in every Part. First, lets get all the
TimeSignature objects in the score with
`.getElementsByClass('TimeSignature')` or, even better, the shortcut,
`getTimeSignatures()`. This only works
because we already flattened `Alto` to make `newAlto`

```python
tsList = newAlto.getTimeSignatures()
```

tsList is a `Part` object so we can show it:

```python
print(tsList.__class__)
tsList.show('text')
```

```python
 <class 'music21.stream.base.Part'>
 {0.0} <music21.meter.TimeSignature 5/8>
 {10.0} <music21.meter.TimeSignature 7/8>
 {17.0} <music21.meter.TimeSignature 9/8>
 {26.0} <music21.meter.TimeSignature 3/8>
```

Now we’ll create a new `Score` object and flatten all the parts from
the original `myBach` and get everything but the `TimeSignature`
objects, run `.makeNotation()` and put it in the new score:

```python
newScore = stream.Score()

for part in myBach.parts:
    flatPart = part.flatten()
    noTSPart = flatPart.getElementsNotOfClass('TimeSignature').stream()
    for ts in tsList:
        noTSPart.insert(ts.offset, ts)
    noTSPart.makeNotation(inPlace=True)
    newScore.insert(0, noTSPart)

newScore.measures(1, 10).show()
```

[![../_images/usersGuide_14_timeSignatures_82_0.png](../_images/usersGuide_14_timeSignatures_82_0.png)](../_images/usersGuide_14_timeSignatures_82_0.png)

## Working with Beats in a score

If a Note is in a Measure, and that Measure or a preceding Measure has a
TimeSignature, it is possible to find the beat, or the position of the
Note in terms of the count of whole or fractional subdivisions of
top-level beat partitions.

The Note [`beat`](../moduleReference/moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") property will
return, if available, a numerical representation of the beat, with a
floating point value corresponding to the proportional position through
the beat. The Note
[`beatStr`](../moduleReference/moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") property returns
a string representation, replacing floating point values with fractions
when available.

Let’s see what we can do with beats in our same Bach score. Let’s use
the [`beatStr`](../moduleReference/moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") for “beat
string” tag to get a nicely formatted measure of the beat for each note
in the Soprano part:

```python
sopr = myBach.parts['Soprano'].measures(1,2)

for n in sopr.recurse().notes:
    print(n, n.beatStr)
```

```python
 <music21.note.Note B-> 1
 <music21.note.Note B-> 2
 <music21.note.Note F> 3
 <music21.note.Note D> 1
 <music21.note.Note C> 2 1/2
 <music21.note.Note B-> 3
```

Instead of just printing that though, let’s put the beatStr as a lyric
on each note:

```python
for n in sopr.recurse().notes:
    n.addLyric(n.beatStr)

sopr.show()
```

[![../_images/usersGuide_14_timeSignatures_87_0.png](../_images/usersGuide_14_timeSignatures_87_0.png)](../_images/usersGuide_14_timeSignatures_87_0.png)

If we change the TimeSignature in a Part, the beat counts will reflect
this change. For example, if the Bass part of the same chorale is
re-barred in 6/8, new, syncopated beat counts will be given.

```python
bass = myBach.getElementById('Bass')
newBass = bass.flatten().getElementsNotOfClass(meter.TimeSignature).stream()
newMeasures = newBass.makeMeasures(meter.TimeSignature('6/8'))
newMeasures.makeTies(inPlace=True)
for n in newMeasures.recurse().notesAndRests:
    n.addLyric(n.beatStr)
newMeasures.show()
```

[![../_images/usersGuide_14_timeSignatures_89_0.png](../_images/usersGuide_14_timeSignatures_89_0.png)](../_images/usersGuide_14_timeSignatures_89_0.png)

Each note also has a particular
[`beatStrength`](../moduleReference/moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") that
shows how metrically accented `music21` thinks it is, with 1.0 being
most accented and 0 being least.

```python
for n in sopr.recurse().notes:
    print(n, n.beatStrength)
```

```python
 <music21.note.Note B-> 1.0
 <music21.note.Note B-> 0.5
 <music21.note.Note F> 0.5
 <music21.note.Note D> 1.0
 <music21.note.Note C> 0.25
 <music21.note.Note B-> 0.5
```

This chapter gives a solid introduction to the types of things you can
do with TimeSignatures and beats. We will return again to this topic
later in the User’s Guide to show how beaming, accentuation, and other
elements can be controlled through meter and `TimeSignature` objects.
But time is not the only thing to have a signature.
[Chapter 15, Keys and Key Signatures](usersGuide_15_key.html#usersguide-15-key) will
guide you through working with [`KeySignature`](../moduleReference/moduleKey.html#music21.key.KeySignature "music21.key.KeySignature") and
[`Key`](../moduleReference/moduleKey.html#music21.key.Key "music21.key.Key") objects.
