Source: https://music21.org/music21docs/usersGuide/usersGuide_32_articulations.html

# User’s Guide, Chapter 32: Articulations

Articulations are elements attached usually to Notes that specify how
the note should be played. In `music21` we use the term articulation
also to refer to indications that are specific to instruments, such as
bowing or fingering information. They all live in the
[music21.articulations](../moduleReference/moduleArticulations.html#modulearticulations) module and start with the class
[`Articulation`](../moduleReference/moduleArticulations.html#music21.articulations.Articulation "music21.articulations.Articulation").

```python
from music21 import *

art = articulations.Articulation()
art
```

```python
 <music21.articulations.Articulation>
```

All articulations have a `.placement` attribute which can be ‘above’,
‘below’, or None.

```python
print(art.placement)
```

```python
 None
```

```python
art.placement = 'above'
art.placement
```

```python
 'above'
```

All articulations have additional `.style` information, which we will
discuss in more depth later:

```python
art.style.absoluteX = 20
```

Now, most of the time you won’t want *any* articulation, you will want
*the* specific articulation such as `Staccato`, `Accent`, etc. So
there are classes for each of them:

```python
stac = articulations.Staccato()
acc = articulations.Accent()
```

To make an articulation display, attach it to the `.articulations`
list on a Note:

```python
n1 = note.Note('A4')
n1.articulations
```

```python
 []
```

```python
n1.articulations.append(stac)
n1.articulations
```

```python
 [<music21.articulations.Staccato>]
```

```python
n1.show()
```

[![../_images/usersGuide_32_articulations_12_0.png](../_images/usersGuide_32_articulations_12_0.png)](../_images/usersGuide_32_articulations_12_0.png)

Because `.articulations` is a list, a note may have multiple
articulations:

```python
n1.articulations.append(acc)
n1.show()
```

[![../_images/usersGuide_32_articulations_14_0.png](../_images/usersGuide_32_articulations_14_0.png)](../_images/usersGuide_32_articulations_14_0.png)

```python
doit = articulations.Doit()
n1.articulations.append(doit)
n1.show()
```

[![../_images/usersGuide_32_articulations_15_0.png](../_images/usersGuide_32_articulations_15_0.png)](../_images/usersGuide_32_articulations_15_0.png)

Some articulations affect the length of the note:

```python
stac.lengthShift
```

```python
 0.7
```

The `0.7` in this case indicates that the note should be played for
70% of its normal length.

Others affect the volume:

```python
acc.volumeShift
```

```python
 0.1
```

Here, instead of 10% of the normal volume (that’d be a weird accent), it
means 10% more than its normal volume. This inconsistency may be fixed
in a later version.

Many articulations have additional parameters.
[`StrongAccent`](../moduleReference/moduleArticulations.html#music21.articulations.StrongAccent "music21.articulations.StrongAccent") for instance can point up
or down:

```python
sacc = articulations.StrongAccent()
sacc.pointDirection
```

```python
 'up'
```

```python
sacc.placement = 'above'

n2 = note.Note('A4')
n2.articulations.append(sacc)

sacc2 = articulations.StrongAccent()
sacc2.pointDirection = 'down'
sacc2.placement = 'below'

n3 = note.Note('A4')
n3.articulations.append(sacc2)

m = stream.Measure()
m.append([n2, n3])
m.show()
```

[![../_images/usersGuide_32_articulations_24_0.png](../_images/usersGuide_32_articulations_24_0.png)](../_images/usersGuide_32_articulations_24_0.png)

Unfortunately, neither MuseScore (which generates these images) nor
Finale respect `.placement` or `pointDirection` at this time.

As we saw in [Chapter 13](usersGuide_13_music21object2.html#usersguide-13-music21object2), when a
note is split, its articulations go either on the first note of the
split, the last, or all the notes:

```python
n12, n22 = n1.splitAtQuarterLength(0.5)
m2 = stream.Measure()
m2.append([n12, n22])
m2.show()
```

[![../_images/usersGuide_32_articulations_26_0.png](../_images/usersGuide_32_articulations_26_0.png)](../_images/usersGuide_32_articulations_26_0.png)

This property is determined by the `.tieAttach` value for an
articulation:

```python
acc.tieAttach, stac.tieAttach
```

```python
 ('first', 'last')
```

Breath marks can have a `.symbol` of ‘comma’ or ‘tick’:

```python
bm2 = articulations.BreathMark()
bm2.symbol = 'comma'
n2.articulations.append(bm2)

bm3 = articulations.BreathMark()
bm3.symbol = 'tick'
n3.articulations.append(bm3)

m.show()
```

[![../_images/usersGuide_32_articulations_30_0.png](../_images/usersGuide_32_articulations_30_0.png)](../_images/usersGuide_32_articulations_30_0.png)

Again, unfortunately, some MusicXML readers do not respect this value.

MusicXML distinguishes articulations from technical indications, but in
`music21` these are all in the `articulations` module and stored in
the `.articulations` list. They do, however, have
`TechnicalIndication` in their classes. A Fingering is something that
MusicXML considers a TechnicalIndication:

```python
f = articulations.Fingering(5)
f.classes
```

```python
 ('Fingering',
  'TechnicalIndication',
  'Articulation',
  'Music21Object',
  'ProtoM21Object',
  'object')
```

```python
f.fingerNumber
```

```python
 5
```

```python
n3.articulations = []
n3.articulations.append(f)
m.show()
```

[![../_images/usersGuide_32_articulations_34_0.png](../_images/usersGuide_32_articulations_34_0.png)](../_images/usersGuide_32_articulations_34_0.png)

`Music21` can represent all the information in MusicXML articulations,
and every MusicXML technical indication with the exception of guitar
information, arrows, and woodwind/brass fingering.

This is a short chapter, because once you know a bit about
articulations, you’ll just want to spend your time in the
[music21.articulations](../moduleReference/moduleArticulations.html#modulearticulations) module reference to learn more about them.
But there is a related concept called “expressions” that we will learn
about in `Chapter 33: Expressions and Ornaments` when it is completed.

For now, the next completed chapter is
[Chapter 44: Advanced Graphing (Axes, Plots, and Graphs)](usersGuide_44_advancedGraphing.html#usersguide-44-advancedgraphing).
