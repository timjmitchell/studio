Source: https://music21.org/music21docs/usersGuide/usersGuide_55_advancedMeter.html

# User’s Guide, Chapter 55: Advanced Meter Topics

## Objects for Organizing Hierarchical Partitions

Hierarchical metrical structures can be described as a type of
fractional, space-preserving tree structure. With such a structure we
partition and divide a single duration into one or more parts, where
each part is a fraction of the whole. Each part can, in turn, be
similarly divided. The objects for configuring this structure are the
MeterTerminal and the MeterSequence objects.

MeterTerminal and the MeterSequence objects are for advanced
configuration. For basic data access about common meters, see the
discussion of TimeSignature, below.

## Creating and Editing MeterTerminal Objects

A MeterTerminal is a node of the metrical tree structure, defined as a
duration expressed as a fraction of a whole note. Thus, 1/4 is 1 quarter
length (QL) duration; 3/8 is 1.5 QL; 3/16 is 0.75 QL. For this model,
denominators are limited to *n* = 2 :superscript:`x`, for *x* between
1 and 7 (e.g. 1/1 to 1/128).

MeterTerminals can additionally store a weight, or a numerical value
that can be interpreted in a variety of different ways.

The following examples in the Python interpreter demonstrate creating a
MeterTerminal and accessing the
`numerator` and
`denominator`
attributes. The
`duration` attribute
stores a [`Duration`](../moduleReference/moduleDuration.html#music21.duration.Duration "music21.duration.Duration") object.

```python
from music21 import *
mt = meter.MeterTerminal('3/4')
mt
```

```python
 <music21.meter.core.MeterTerminal 3/4>
```

```python
mt.numerator, mt.denominator
```

```python
 (3, 4)
```

```python
mt.duration.quarterLength
```

```python
 3.0
```

A MeterTerminal can be broken into an ordered sequence of MeterTerminal
objects that sum to the same duration. This new object, to be discussed
below, is the MeterSequence. A MeterTerminal can be broken into these
duration-preserving components with the
`subdivide()` method. An argument for
subdivision can be given as a desired number of equal-valued components,
a list of numerators assuming equal-denominators, or a list of string
fraction representations.

```python
mt.subdivide(3)
```

```python
 <music21.meter.core.MeterSequence {1/4+1/4+1/4}>
```

```python
mt.subdivide([3, 3])
```

```python
 <music21.meter.core.MeterSequence {3/8+3/8}>
```

```python
mt.subdivide(['1/4', '4/8'])
```

```python
 <music21.meter.core.MeterSequence {1/4+4/8}>
```

## Creating and Editing MeterSequence Objects

A MeterSequence object is a sub-class of a MeterTerminal. Like a
MeterTerminal, a MeterSequence has a
`numerator`, a
`denominator`, and a
`duration` attribute. A
MeterSequence, however, can be a hierarchical tree or sub-tree,
containing an ordered sequence of MeterTerminal and/or MeterSequence
objects.

The ordered collection of MeterTerminal and/or MeterSequence objects can
be accessed like Python lists. MeterSequence objects, like MeterTerminal
objects, store a weight that by default is the sum of constituent
weights.

The `partition()` and
`subdivide()` methods can be used to
configure the nested hierarchical structure.

The `partition()` method replaces
existing MeterTerminal or MeterSequence objects in place with a new
arrangement, specified as a desired number of equal-valued components, a
list of numerators assuming equal-denominators, or a list of string
fraction representations.

The `subdivide()` method returns a
new MeterSequence (leaving the source MeterSequence unchanged) with an
arrangement of MeterTerminals as specified by an argument in the same
form as for the `partition()` method.

Note that MeterTerminal objects cannot be partitioned in place. A common
way to convert a MeterTerminal into a MeterSequence is to reassign the
returned MeterSequence from the
`subdivide()` method to the position
occupied by the MeterTerminal.

The following example creates and partitions a MeterSequence by
re-assigning subdivisions to MeterTerminal objects. The use of Python
list-like index access is also demonstrated.

```python
ms = meter.MeterSequence('3/4')
ms
```

```python
 <music21.meter.core.MeterSequence {3/4}>
```

```python
ms.partition([3,3])
ms
```

```python
 <music21.meter.core.MeterSequence {3/8+3/8}>
```

```python
ms[0]
```

```python
 <music21.meter.core.MeterTerminal 3/8>
```

```python
ms[0] = ms[0].subdivide([3,3])
ms[0]
```

```python
 <music21.meter.core.MeterSequence {3/16+3/16}>
```

```python
ms
```

```python
 <music21.meter.core.MeterSequence {{3/16+3/16}+3/8}>
```

```python
ms[1] = ms[1].subdivide([1,1,1])
ms[1][0]
```

```python
 <music21.meter.core.MeterTerminal 1/8>
```

```python
ms[1]
```

```python
 <music21.meter.core.MeterSequence {1/8+1/8+1/8}>
```

```python
ms
```

```python
 <music21.meter.core.MeterSequence {{3/16+3/16}+{1/8+1/8+1/8}}>
```

The resulting structure can be graphically displayed with the following
diagram:

```python
# 3/8 divisions
```

![../_images/usersGuide_55_advancedMeter_23_0.png](../_images/usersGuide_55_advancedMeter_23_0.png)

Numerous MeterSequence attributes provide convenient ways to access
information about, or new objects from, the nested tree structure. The
`depth` attribute returns
the depth count at any node within the tree structure; the
`flat` property returns a
new, flat MeterSequence constructed from all the lowest-level
MeterTerminal objects (all leaf nodes).

```python
ms.depth
```

```python
 2
```

```python
ms[0].depth
```

```python
 1
```

```python
ms.flatten()
```

```python
 <music21.meter.core.MeterSequence {3/16+3/16+1/8+1/8+1/8}>
```

Numerous methods provide ways to access levels (slices) of the
hierarchical structure, or all nodes found at a desired hierarchical
level. As all components preserve the duration of their container, all
levels have the same total duration. The
`getLevel()` method returns, for a
given depth, a new, flat MeterSequence. The
`getLevelSpan()` method returns, for
a given depth, the time span of each node as a list of start and end
values.

```python
ms.getLevel(0)
```

```python
 <music21.meter.core.MeterSequence {3/8+3/8}>
```

```python
ms.getLevel(1)
```

```python
 <music21.meter.core.MeterSequence {3/16+3/16+1/8+1/8+1/8}>
```

```python
ms.getLevelSpan(1)
```

```python
 [(0.0, 0.75), (0.75, 1.5), (1.5, 2.0), (2.0, 2.5), (2.5, 3.0)]
```

```python
ms[1].getLevelSpan(1)
```

```python
 [(0.0, 0.5), (0.5, 1.0), (1.0, 1.5)]
```

Finally, numerous methods provide ways to find and access the relevant
nodes (the MeterTerminal or MeterSequence objects) active given a
quarter length position into the tree structure. The
`offsetToIndex()` method returns, for
a given QL, the index of the active node. The
`offsetToSpan()` method returns, for
a given QL, the span of the active node. The
`offsetToDepth()` method returns, for
a given QL, the maximum depth at this position.

```python
ms.offsetToIndex(2.5)
```

```python
 1
```

```python
ms.offsetToSpan(2.5)
```

```python
 (1.5, 3.0)
```

```python
ms.offsetToDepth(.5)
```

```python
 2
```

```python
ms[0].offsetToDepth(.5)
```

```python
 1
```

```python
ms.getLevel(1).offsetToSpan(.5)
```

```python
 (0, 0.75)
```

## Advanced Time Signature Configuration

The music21 `TimeSignature` object contains four
parallel MeterSequence objects, each assigned to the attributes
`displaySequence`,
`beatSequence`,
`beamSequence`,
`accentSequence`.
The following displays a graphical realization of these four
MeterSequence objects.

```python
# four MeterSequence objects
```

[![../_images/usersGuide_55_advancedMeter_41_0.png](../_images/usersGuide_55_advancedMeter_41_0.png)](../_images/usersGuide_55_advancedMeter_41_0.png)

The TimeSignature provides a model of all common hierarchical structures
contained within a bar. Common meters are initialized with expected
defaults; however, full MeterSequence customization is available.

## Configuring Display

The TimeSignature
`displaySequence`
MeterSequence employs the highest-level partitions to configure the
displayed time signature symbol. If more than one partition is given,
those partitions will be interpreted as additive meter components. If
partitions have a common denominator, a summed numerator (over a single
denominator) can be displayed by setting the TimeSignature
`summedNumerator`
attribute to True. Lower-level subdivisions of the TimeSignature
MeterSequence are not employed.

Note that a new MeterSequence instance can be assigned to the
`displaySequence`
attribute with a duration and/or partitioning completely independent
from the
`beatSequence`,
`beamSequence`, and
`accentSequence`
MeterSequences.

The following example demonstrates setting the display MeterSequence for
a TimeSignature. NOTE that there is currently a bug in the first one
that is showing 5/16 instead of 5/8. We hope to fix this soon.

```python
from music21 import stream, note
ts1 = meter.TimeSignature('5/8') # assumes two partitions
ts1.displaySequence.partition(['3/16', '1/8', '5/16'])
ts2 = meter.TimeSignature('5/8') # assumes two partitions
ts2.displaySequence.partition(['2/8', '3/8'])
ts2.summedNumerator = True
s = stream.Stream()
for ts in [ts1, ts2]:
    m = stream.Measure()
    m.timeSignature = ts
    n = note.Note('b')
    n.quarterLength = 0.5
    m.repeatAppend(n, 5)
    s.append(m)

s.show()
```

[![../_images/usersGuide_55_advancedMeter_45_0.png](../_images/usersGuide_55_advancedMeter_45_0.png)](../_images/usersGuide_55_advancedMeter_45_0.png)

## Configuring Beam

The TimeSignature
`beamSequence`
MeterSequence employs the complete hierarchical structure to configure
the single or multi-level beaming of a bar. The outer-most partitions
can specify one or more top-level partitions. Lower-level partitions
subdivide beam-groups, providing the appropriate beam-breaks when
sufficiently small durations are employed.

The `beamSequence`
MeterSequence is generally used to create and configure
`Beams` objects stored in
[`Note`](../moduleReference/moduleNote.html#music21.note.Note "music21.note.Note") objects. The TimeSignature
`getBeams()` method, given a list of
[`Duration`](../moduleReference/moduleDuration.html#music21.duration.Duration "music21.duration.Duration") objects, returns a list of
`Beams` objects based on the TimeSignature
`beamSequence`
MeterSequence.

Many users may find the Stream
`makeBeams()` method the most convenient
way to apply beams to a Measure or Stream of Note objects. This method
returns a new Stream with created and configured Beams.

The following example beams a bar of 3/4 in four different ways. The
diversity and complexity of beaming is offered here to illustrate the
flexibility of this model.

```python
ts1 = meter.TimeSignature('3/4')
ts1.beamSequence.partition(1)
ts1.beamSequence[0] = ts1.beamSequence[0].subdivide(['3/8', '5/32', '4/32', '3/32'])

ts2 = meter.TimeSignature('3/4')
ts2.beamSequence.partition(3)

ts3 = meter.TimeSignature('3/4')
ts3.beamSequence.partition(3)

for i in range(len(ts3.beamSequence)):
    ts3.beamSequence[i] = ts3.beamSequence[i].subdivide(2)

ts4 = meter.TimeSignature('3/4')
ts4.beamSequence.partition(['3/8', '3/8'])
for i in range(len(ts4.beamSequence)):
    ts4.beamSequence[i] = ts4.beamSequence[i].subdivide(['6/32', '6/32'])
    for j in range(len(ts4.beamSequence[i])):
        ts4.beamSequence[i][j] = ts4.beamSequence[i][j].subdivide(2)

s = stream.Stream()
for ts in [ts1, ts2, ts3, ts4]:
    m = stream.Measure()
    m.timeSignature = ts
    n = note.Note('b')
    n.quarterLength = 0.125
    m.repeatAppend(n, 24)
    s.append(m.makeBeams())

s.show()
```

[![../_images/usersGuide_55_advancedMeter_48_0.png](../_images/usersGuide_55_advancedMeter_48_0.png)](../_images/usersGuide_55_advancedMeter_48_0.png)

The following is a fractional grid representation of the four beam
partitions created.

```python
# four beam partitions
```

![../_images/usersGuide_55_advancedMeter_50_0.jpg](../_images/usersGuide_55_advancedMeter_50_0.jpg)

## Configuring Beat

The TimeSignature
`beatSequence`
MeterSequence employs the hierarchical structure to define the beats and
beat divisions of a bar. The outermost partitions can specify one or
more top level beats. Inner partitions can specify the beat division
partitions. For most common meters, beats and beat divisions are
preconfigured by default.

In the following example, a simple and a compound meter is created, and
the default beat partitions are examined. The
`getLevel()` method can be used to
show the beat and background beat partitions. The timeSignature
`beatDuration`,
`beat`, and
`beatCountName`
properties can be used to return commonly needed beat information. The
TimeSignature
`beatDivisionCount`,
and
`beatDivisionCountName`
properties can be used to return commonly needed beat division
information. These descriptors can be combined to return a string
representation of the TimeSignature classification with
`classification`
property.

```python
ts = meter.TimeSignature('3/4')
ts.beatSequence.getLevel(0)
```

```python
 <music21.meter.core.MeterSequence {1/4+1/4+1/4}>
```

```python
ts.beatSequence.getLevel(1)
```

```python
 <music21.meter.core.MeterSequence {1/8+1/8+1/8+1/8+1/8+1/8}>
```

```python
ts.beatDuration
```

```python
 <music21.duration.Duration 1.0>
```

```python
ts.beatCount
```

```python
 3
```

```python
ts.beatCountName
```

```python
 'Triple'
```

```python
ts.beatDivisionCount
```

```python
 2
```

```python
ts.beatDivisionCountName
```

```python
 'Simple'
```

```python
ts.classification
```

```python
 'Simple Triple'
```

```python
ts = meter.TimeSignature('12/16')
ts.beatSequence.getLevel(0)
```

```python
 <music21.meter.core.MeterSequence {3/16+3/16+3/16+3/16}>
```

```python
ts.beatSequence.getLevel(1)
```

```python
 <music21.meter.core.MeterSequence {1/16+1/16+1/16+1/16+1/16+1/16+1/16+1/16+1/16+1/16+1/16+1/16}>
```

```python
ts.beatDuration
```

```python
 <music21.duration.Duration 0.75>
```

```python
ts.beatCount
```

```python
 4
```

```python
ts.beatCountName
```

```python
 'Quadruple'
```

```python
ts.beatDivisionCount
```

```python
 3
```

```python
ts.beatDivisionCountName
```

```python
 'Compound'
```

```python
ts.classification
```

```python
 'Compound Quadruple'
```

## Annotating Found Notes with Beat Count

The `getBeat()` method returns the
currently active beat given a quarter length position into the
TimeSignature.

In the following example, all leading tones, or C#s, are collected into
a new Stream and displayed with annotations for part, measure, and beat.

```python
score = corpus.parse('bach/bwv366.xml')
ts = score[meter.TimeSignature].first()
ts.beatSequence.partition(3)

found = stream.Stream()
offsetQL = 0
for part in score.parts:
    found.insert(offsetQL, part[clef.Clef].first())
    for i in range(len(part.getElementsByClass(stream.Measure))):
        m = part[stream.Measure][i]
        for n in m.notesAndRests:
            if n.name == 'C#':
                n.addLyric(f'{part.id[0]}, m. {m.number}')
                n.addLyric(f'beat {ts.getBeat(n.offset)}')
                found.insert(offsetQL, n)
                offsetQL += 4

found.show()
```

[![../_images/usersGuide_55_advancedMeter_71_0.png](../_images/usersGuide_55_advancedMeter_71_0.png)](../_images/usersGuide_55_advancedMeter_71_0.png)

## Using Beat Depth to Provide Metrical Analysis

Another application of the
`beatSequence`
MeterSequence is to define the hierarchical depth active for a given
note found within the TimeSignature.

The `getBeatDepth()` method, when set
with the optional parameter `align` to “quantize”, shows the number of
hierarchical levels that start at or before that point. This value is
described by Lerdahl and Jackendoff as metrical analysis.

In the following example,
`beatSequence`
MeterSequence is partitioned first into one subdivision, and then each
subsequent subdivision into two, down to four layers of partitioning.

The number of hierarchical levels, found with the
`getBeatDepth()` method, is appended
to each note with the [`addLyric()`](../moduleReference/moduleNote.html#music21.note.GeneralNote.addLyric "music21.note.GeneralNote.addLyric")
method.

```python
score = corpus.parse('bach/bwv281.xml')
partBass = score.getElementById('Bass')
ts = partBass[meter.TimeSignature].first()
ts.beatSequence.partition(1)
for h in range(len(ts.beatSequence)):
    ts.beatSequence[h] = ts.beatSequence[h].subdivide(2)
    for i in range(len(ts.beatSequence[h])):
        ts.beatSequence[h][i] = ts.beatSequence[h][i].subdivide(2)
        for j in range(len(ts.beatSequence[h][i])):
            ts.beatSequence[h][i][j] = ts.beatSequence[h][i][j].subdivide(2)

for m in partBass.getElementsByClass(stream.Measure):
    for n in m.notesAndRests:
        for i in range(ts.getBeatDepth(n.offset)):
            n.addLyric('*')

partBass.measures(0, 7).show()
```

[![../_images/usersGuide_55_advancedMeter_74_0.png](../_images/usersGuide_55_advancedMeter_74_0.png)](../_images/usersGuide_55_advancedMeter_74_0.png)

Alternatively, this type of annotation can be applied to a Stream using
the [`labelBeatDepth()`](../moduleReference/moduleAnalysisMetrical.html#music21.analysis.metrical.labelBeatDepth "music21.analysis.metrical.labelBeatDepth") function.

## Configuring Accent

The TimeSignature
`accentSequence`
MeterSequence defines one or more levels of hierarchical accent levels,
where quantitative accent value is encoded in MeterTerminal or
MeterSequence with a number assigned to the
`weight` attribute.

## Applying Articulations Based on Accent

The `getAccentWeight()` method
returns the currently active accent weight given a quarter length
position into the TimeSignature. Combined with the
`getBeatProgress()` method, Notes
that start on particular beat can be isolated and examined.

The following example extracts the Bass line of a Bach chorale in 3/4
and, after repartitioning the beat and accent attributes, applies
accents to reflect a meter of 6/8.

```python
score = corpus.parse('bach/bwv366.xml')
partBass = score.getElementById('Bass')
ts = partBass[meter.TimeSignature].first()
ts.beatSequence.partition(['3/8', '3/8'])
ts.accentSequence.partition(['3/8', '3/8'])
ts.setAccentWeight([1, .5])
for m in partBass[stream.Measure]:
    lastBeat = None
    for n in m.notesAndRests:
        beat, progress = ts.getBeatProgress(n.offset)
        if beat != lastBeat and progress == 0:
            if n.tie is not None and n.tie.type == 'stop':
                continue
            if ts.getAccentWeight(n.offset) == 1:
                mark = articulations.StrongAccent()
            elif ts.getAccentWeight(n.offset) == .5:
                mark = articulations.Accent()
            n.articulations.append(mark)
            lastBeat = beat
        m = m.sorted()

partBass.measures(0, 8).show()
```

[![../_images/usersGuide_55_advancedMeter_80_0.png](../_images/usersGuide_55_advancedMeter_80_0.png)](../_images/usersGuide_55_advancedMeter_80_0.png)

This is probably more depth to the concept of meter than anyone would
ever want! But hope that it has whetted your appetite for jucier
concepts still to come!

The next chapters are not yet complete, so let’s jump head to
[Chapter 58: Understanding Sites and Contexts](usersGuide_58_sitesContext.html#usersguide-58-sitescontext)
