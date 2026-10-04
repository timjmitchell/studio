Source: https://music21.org/music21docs/usersGuide/usersGuide_22_graphing.html

# User’s Guide, Chapter 22: Graphing and plotting

Music notation isn’t the only way to understand music visually.
Sometimes a plot of a musical score can reveal relationships across a
piece that are hard to understand otherwise. `music21` includes a lot
of ways to visualize notes, scores, and measures, and in this chapter we
will see some of the most common ones.

## Piano Rolls!

The easiest way to see how pitches evolve over the course of a piece is
to create a virtual representation of a piano roll. Unlike a traditional
piano roll, time is usually represented on the horizontal axis and pitch
height along the vertical. The easiest way to see how this works is
simply to create one of these graphs, so we can get started. Let’s load
up some Verdi:

```python
from music21 import *
```

```python
verdi = corpus.parse('verdi/laDonnaEMobile')
verdi.id = 'verdi'
verdi.measures(1, 10).show()
```

[![../_images/usersGuide_22_graphing_6_0.png](../_images/usersGuide_22_graphing_6_0.png)](../_images/usersGuide_22_graphing_6_0.png)

First, let’s visualize the vocal part alone:

```python
voice = verdi.parts[0]
voice.measures(1, 10).plot()
```

[![../_images/usersGuide_22_graphing_8_0.png](../_images/usersGuide_22_graphing_8_0.png)](../_images/usersGuide_22_graphing_8_0.png)

The default here is to plot pitch against time, calculated in measures.

If you are following along with these examples in a Jupyter or Google
notebook, and you’re not on the latest matplotlib/JupyterLab be sure to
execute the magic command:

```python
%matplotlib inline
```

To ensure that the graphs show up inside your notebook.

`music21` takes care of some of the hard things that can make
visualizing music in most data visualization software (such as Microsoft
Excel) difficult. For instance, measure numbers are used directly as
they appear in the score; pitches are labeled with names only when they
appear (including the choosing most commonly appearing enharmonic
spelling, using proper sharp and flat signs instead of “b” and “#”). We
can make a fake piece to see how this works:

```python
fakePiece = converter.parse("tinyNotation: 1/4 c#4 2/4 d-4 e#4 3/4 e#2 f4 4/4 c#4 d'--2")
fakePiece.id = 'fake'
fakePiece.show()
```

[![../_images/usersGuide_22_graphing_10_0.png](../_images/usersGuide_22_graphing_10_0.png)](../_images/usersGuide_22_graphing_10_0.png)

```python
fakePiece.plot()
```

[![../_images/usersGuide_22_graphing_11_0.png](../_images/usersGuide_22_graphing_11_0.png)](../_images/usersGuide_22_graphing_11_0.png)

(This was hard to do! And we’re, I hope justifiably, proud of getting
things like this right. Major shoutout to Christopher Ariza who wrote
90% of the graphing code).

We can make other types of graphs just as easily. For instance, plotting
lengths of notes against their position in space. For this one, a little
piece by Schoenberg (Opus 19, no. 2) is great, since the repetition of
G4 + B4 as eighth notes becomes clear:

```python
schoenberg = corpus.parse('schoenberg/opus19', 2)
schoenberg.id = 'schoenberg'
schoenberg.measures(1, 4).show()
```

[![../_images/usersGuide_22_graphing_13_0.png](../_images/usersGuide_22_graphing_13_0.png)](../_images/usersGuide_22_graphing_13_0.png)

Let’s do a scatter plot of quarterLength against pitch:

```python
schoenberg.plot('scatter', 'quarterLength', 'pitch', title='See the G and B!')
```

[![../_images/usersGuide_22_graphing_15_0.png](../_images/usersGuide_22_graphing_15_0.png)](../_images/usersGuide_22_graphing_15_0.png)

It’s a little small on this website (you can make it as big as you want
on your own with the keyword `dpi=400` or so), so maybe just a
histogram of pitch would be better:

```python
schoenberg.plot('histogram', 'octave', xHideUnused=False, yAxisLabel='Number of Pitches')
```

[![../_images/usersGuide_22_graphing_17_0.png](../_images/usersGuide_22_graphing_17_0.png)](../_images/usersGuide_22_graphing_17_0.png)

Or even just pitch classes:

```python
schoenberg.plot('histogram', 'pitchClass')
```

[![../_images/usersGuide_22_graphing_19_0.png](../_images/usersGuide_22_graphing_19_0.png)](../_images/usersGuide_22_graphing_19_0.png)

Okay, so we’ve gotten a taste for graphs, let’s look more closely at how
to make them:

## Installing graphing software

All plots require installing the `matplotlib` and `numpy` libraries.
You should have them installed when you installed music21.

## Where are graphs located?

Graphing functions are located in the [music21.graph](../moduleReference/moduleGraph.html#modulegraph) modules,
specifically: [music21.graph.primitives](../moduleReference/moduleGraphPrimitives.html#modulegraphprimitives), [music21.graph.plot](../moduleReference/moduleGraphPlot.html#modulegraphplot)
and [music21.graph.axis](../moduleReference/moduleGraphAxis.html#modulegraphaxis). With some utility functions located in
[music21.graph.utilities](../moduleReference/moduleGraphUtilities.html#modulegraphutilities) and [music21.graph.findPlot](../moduleReference/moduleGraphFindPlot.html#modulegraphfindplot).

## What sorts of graphs are there?

We can look in `graph.findPlot.FORMATS` for the list of possible
graphs:

```python
graph.findPlot.FORMATS
```

```python
 ['horizontalbar',
  'histogram',
  'scatter',
  'scatterweighted',
  '3dbars',
  'colorgrid',
  'horizontalbarweighted']
```

We might as well start by trying them!

```python
verdi.plot('horizontalbar')
```

[![../_images/usersGuide_22_graphing_24_0.png](../_images/usersGuide_22_graphing_24_0.png)](../_images/usersGuide_22_graphing_24_0.png)

There are three types of `horizontalbar` types defined, so we got all
of them. For the next we’ll be more picky…

This one we’ve already seen. Same with the next one:

```python
verdi.plot('histogram', 'pitch')
```

[![../_images/usersGuide_22_graphing_26_0.png](../_images/usersGuide_22_graphing_26_0.png)](../_images/usersGuide_22_graphing_26_0.png)

```python
schoenberg.plot('scatter', 'pitch', 'quarterLength')
```

[![../_images/usersGuide_22_graphing_27_0.png](../_images/usersGuide_22_graphing_27_0.png)](../_images/usersGuide_22_graphing_27_0.png)

There were two kinds of scatter plots – one that plotted quarter length
against pitch and one that plotted pitch against dynamics. We’ll figure
out how to get the one we want later. Let’s keep going:

```python
excerpt = verdi.measures(1, 10)
excerpt.plot('scatterweighted', 'pitch', 'quarterLength')
```

[![../_images/usersGuide_22_graphing_29_0.png](../_images/usersGuide_22_graphing_29_0.png)](../_images/usersGuide_22_graphing_29_0.png)

Because this next one returns two graphs, inside a notebook you may need
to add `returnInNotebook=True` if you are running these commands in a
notebook to see the map of colors to keys:

```python
verdi.plot('colorgrid', returnInNotebook=True)
```

```python
 <music21.graph.plot.WindowedKey for <music21.stream.Score verdi>>
```

[![../_images/usersGuide_22_graphing_31_1.png](../_images/usersGuide_22_graphing_31_1.png)](../_images/usersGuide_22_graphing_31_1.png)
[![../_images/usersGuide_22_graphing_31_2.png](../_images/usersGuide_22_graphing_31_2.png)](../_images/usersGuide_22_graphing_31_2.png)

(The attribute `returnInNotebook=True` is one way to make graphs
appear better in notebooks. Another is assigning the output of the plot
to a dummy variable like `_`. These docs have secretly been doing both
above.)

Here we can see each part plotted when it plays and with dynamics:

```python
schoenberg.plot('horizontalbarweighted')
```

[![../_images/usersGuide_22_graphing_33_0.png](../_images/usersGuide_22_graphing_33_0.png)](../_images/usersGuide_22_graphing_33_0.png)

and we’ve saved the silliest for last:

```python
verdi.plot('3dbars')
```

[![../_images/usersGuide_22_graphing_35_0.png](../_images/usersGuide_22_graphing_35_0.png)](../_images/usersGuide_22_graphing_35_0.png)

The 3D aspect looks pretty cool, but I have a hard time learning from
it.

Each of these plots also has a bunch of synonyms in case you want to use
other terms:

```python
graph.findPlot.FORMAT_SYNONYMS
```

```python
 [('horizontalbar', 'bar', 'horizontal', 'pianoroll', 'piano'),
  ('histogram', 'histo', 'count'),
  ('scatter', 'point'),
  ('scatterweighted', 'weightedscatter', 'weighted'),
  ('3dbars', '3d'),
  ('colorgrid', 'grid', 'window', 'windowed'),
  ('horizontalbarweighted', 'barweighted', 'weightedbar')]
```

For completeness, there are a couple of shortcuts you can use also:

```python
graph.findPlot.PLOTCLASS_SHORTCUTS
```

```python
 {'ambitus': music21.graph.plot.WindowedAmbitus,
  'dolan': music21.graph.plot.Dolan,
  'instruments': music21.graph.plot.Dolan,
  'key': music21.graph.plot.WindowedKey,
  'pianoroll': music21.graph.plot.HorizontalBarPitchSpaceOffset}
```

Okay, so now you know what types of graphs you can make. The next
arguments determine what sorts of things you can put on the axes:

```python
verdi.plot('scatter', 'pitchClass', 'quarterLength')
```

[![../_images/usersGuide_22_graphing_41_0.png](../_images/usersGuide_22_graphing_41_0.png)](../_images/usersGuide_22_graphing_41_0.png)

```python
verdi.plot('scatter', 'dynamics')
```

[![../_images/usersGuide_22_graphing_42_0.png](../_images/usersGuide_22_graphing_42_0.png)](../_images/usersGuide_22_graphing_42_0.png)

We can see all the different things that we can put as an axis via
[`music21.graph.findPlot.getAxisQuantities()`](../moduleReference/moduleGraphFindPlot.html#music21.graph.findPlot.getAxisQuantities "music21.graph.findPlot.getAxisQuantities"):

```python
graph.findPlot.getAxisQuantities()
```

```python
 ['generic',
  'count',
  'dynamic',
  'offset',
  'offsetEnd',
  'pitchGeneric',
  'pitchClass',
  'pitchSpace',
  'octave',
  'position',
  'quarterLength']
```

Some of these have synonyms that you can use instead:

```python
graph.findPlot.getAxisQuantities(synonyms=True)
```

```python
 ['generic',
  'one',
  'nothing',
  'blank',
  'count',
  'quantity',
  'frequency',
  'counting',
  'dynamic',
  'dynamics',
  'volume',
  'offset',
  'measure',
  'offsets',
  'measures',
  'time',
  'offsetEnd',
  'timespans',
  'timespan',
  'pitchGeneric',
  'pitchClass',
  'pitchclass',
  'pc',
  'pitchSpace',
  'pitch',
  'pitchspace',
  'ps',
  'octave',
  'octaves',
  'position',
  'positions',
  'quarterLength',
  'ql',
  'quarterlengths',
  'durations',
  'duration']
```

## Application – pitchSpace counting

Both Robert Schumann and Frederic Chopin were composers living in the
first half of the nineteenth century, both working in the tonal
tradition. Their music sounds similar but strikingly different. Does
their distribution of pitches have something to do with it? Let’s
compare a Schumann piece in the corpus (String Quartet opus 41, no. 1,
movement 3) with a Chopin piece in the corpus (Mazurka in C# minor, opus
6, no. 2):

```python
schumann = corpus.parse('schumann/opus41no1', 3)
schumann.plot('histogram', 'pitch')
```

[![../_images/usersGuide_22_graphing_48_0.png](../_images/usersGuide_22_graphing_48_0.png)](../_images/usersGuide_22_graphing_48_0.png)

Schumann’s piece has a sort of bell-curve shaped distribution. Yes, some
notes stand out, A2, E3, and E4–it is in a-minor after all…

```python
schumann.analyze('key')
```

```python
 <music21.key.Key of a minor>
```

but for the most part, it’s pretty nicely shaped. Compare it to the work
by Chopin:

```python
chopin = corpus.parse('chopin/mazurka')
chopin.plot('histogram', 'pitch')
```

[![../_images/usersGuide_22_graphing_52_0.png](../_images/usersGuide_22_graphing_52_0.png)](../_images/usersGuide_22_graphing_52_0.png)

Chopin’s piece has jagged points everywhere like a poorly planned city
(Abu Dhabi?) with a few notes, especially G#4 sticking out. Does this
say something different about Chopin as a composer? Or is it a function
of the fact that the Chopin piece is for piano and the Schumann piece is
for a group of four instruments, three of which have different ranges?
We can’t compare Chopin’s string quartets–he didn’t write any–and
unfortunately, we can’t compare Robert Schumann’s piano music, since I
don’t know any pieces except for very short ones and excerpts that have
been entered into musicxml. But we can compare *Clara* Schumann’s pitch
usage, since a freely available transcription of her four Polonaises,
op. 1 has been encoded by
[“Cypressdome”](https://imslp.org/wiki/4_Polonaises,_Op.1_%28Schumann,_Clara%29).
Let’s check out the first of these:

```python
cs = corpus.parse('schumann_clara/polonaise_op1n1')
cs.id = 'Clara_Schumann'
cs.measures(1, 7).show()
```

[![../_images/usersGuide_22_graphing_54_0.png](../_images/usersGuide_22_graphing_54_0.png)](../_images/usersGuide_22_graphing_54_0.png)

```python
cs.plot('histogram', 'pitchSpace')
```

[![../_images/usersGuide_22_graphing_55_0.png](../_images/usersGuide_22_graphing_55_0.png)](../_images/usersGuide_22_graphing_55_0.png)

It’s one piece, and we’d love to have much more (in fact, the other
three Polonaises are in the corpus as well), but it looks promising!

(Oh, and in case you’re seeing lots of
`<music21.graph.plot.Histohooyet for <music21.stream...` garbage when
plotting, just assign the result of the plot to a variable like `_` as
we did above)

There’s a lot more that can be done with graphing, but that’s a topic
for later. If we’re going to do traditional analysis we’ve got to know
where our Is and Vs are, and for that, we’ll need
[Chapter 23: Roman Numeral Analysis](usersGuide_23_romanNumerals.html#usersguide-23-romannumerals)
