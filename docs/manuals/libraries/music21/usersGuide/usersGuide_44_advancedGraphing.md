Source: https://music21.org/music21docs/usersGuide/usersGuide_44_advancedGraphing.html

# User’s Guide, Chapter 44: Advanced Graphing (Axes, Plots, and Graphs)

Previously, in [Chapter 22](usersGuide_22_graphing.html#usersguide-22-graphing), we learned
how to make plots of streams using the `.plot()` method on any stream,
and to specify the type of graph in the first argument, the x axis in
the second argument, and the y axis in the third (and the z in the
fourth, for 3d graphs). Let’s review a simple graph:

```python
from music21 import *
bach = corpus.parse('bwv66.6')
bach.id = 'bwv66'
bach.plot('scatter', 'offset', 'pitchClass')
```

[![../_images/usersGuide_44_advancedGraphing_2_0.png](../_images/usersGuide_44_advancedGraphing_2_0.png)](../_images/usersGuide_44_advancedGraphing_2_0.png)

When we call `s.plot()` we are actually just calling a function in
`music21.graph` called [`plotStream()`](../moduleReference/moduleGraph.html#music21.graph.plotStream "music21.graph.plotStream").

```python
graph.plotStream(bach, 'scatter', 'offset', 'pitchClass')
```

```python
 <music21.graph.plot.ScatterPitchClassOffset for <music21.stream.Score bwv66>>
```

[![../_images/usersGuide_44_advancedGraphing_4_1.png](../_images/usersGuide_44_advancedGraphing_4_1.png)](../_images/usersGuide_44_advancedGraphing_4_1.png)

`plotStream` uses a helper function called
[`music21.graph.findPlot.getPlotsToMake()`](../moduleReference/moduleGraphFindPlot.html#music21.graph.findPlot.getPlotsToMake "music21.graph.findPlot.getPlotsToMake") to get a list of classes
that can successfully plot this relationship:

```python
graph.findPlot.getPlotsToMake('scatter', 'offset', 'pitchClass')
```

```python
 [music21.graph.plot.ScatterPitchClassOffset]
```

A Plot is a class that can take in a stream and when `.run()` is
called, will extract all the data from the stream and show it:

```python
scatter = graph.plot.ScatterPitchClassOffset(bach)
scatter
```

```python
 <music21.graph.plot.ScatterPitchClassOffset for <music21.stream.Score bwv66>>
```

```python
scatter.run()
```

[![../_images/usersGuide_44_advancedGraphing_9_0.png](../_images/usersGuide_44_advancedGraphing_9_0.png)](../_images/usersGuide_44_advancedGraphing_9_0.png)

## Customizing Plots

Well, so far we haven’t done much that we couldn’t do with `.plot()`,
but we can change some things around.

Let’s change the title:

```python
scatter.title = 'Bach uses a lot of pitches'
scatter.run()
```

[![../_images/usersGuide_44_advancedGraphing_11_0.png](../_images/usersGuide_44_advancedGraphing_11_0.png)](../_images/usersGuide_44_advancedGraphing_11_0.png)

We can change the figure size:

```python
scatter.figureSize = (10, 3)
scatter.run()
```

[![../_images/usersGuide_44_advancedGraphing_13_0.png](../_images/usersGuide_44_advancedGraphing_13_0.png)](../_images/usersGuide_44_advancedGraphing_13_0.png)

We can change any of the following:

```python
*    alpha (which describes how transparent elements of the graph are)
*    colorBackgroundData
*    colorBackgroundFigure
*    colorGrid
*    colors (a list of colors to cycle through)
*    tickFontSize
*    titleFontSize
*    labelFontSize
*    fontFamily
*    marker
*    markersize
```

and a bunch more. See `.keywordConfigurables`

```python
scatter.keywordConfigurables
```

```python
 ('alpha',
  'colorBackgroundData',
  'colorBackgroundFigure',
  'colorGrid',
  'colors',
  'doneAction',
  'dpi',
  'figureSize',
  'fontFamily',
  'hideXGrid',
  'hideYGrid',
  'labelFontSize',
  'marker',
  'markersize',
  'tickColors',
  'tickFontSize',
  'title',
  'titleFontSize',
  'xTickLabelHorizontalAlignment',
  'xTickLabelRotation',
  'xTickLabelVerticalAlignment')
```

```python
scatter.fontFamily = 'sans-serif'
scatter.markersize = 12
scatter.colors = ['red', 'green', 'blue'] # will cycle among these
scatter.alpha = 0.9
scatter.colorBackgroundFigure = '#ffddff' # a light purple
scatter.colorBackgroundData = 'yellow'
scatter.titleFontSize = 20
scatter.run()
```

[![../_images/usersGuide_44_advancedGraphing_16_0.png](../_images/usersGuide_44_advancedGraphing_16_0.png)](../_images/usersGuide_44_advancedGraphing_16_0.png)

That’s too garish for me. Let’s go back to our original graph:

```python
scatter = graph.plot.ScatterPitchClassOffset(bach)
scatter.title = 'Bach and his notes'
scatter.figureSize = (10, 3)
scatter.run()
```

[![../_images/usersGuide_44_advancedGraphing_18_0.png](../_images/usersGuide_44_advancedGraphing_18_0.png)](../_images/usersGuide_44_advancedGraphing_18_0.png)

Different graph types have other configurable data. For instance,
Histograms can configure their `barSpace` and `margin`. See the
documentation for [music21.graph.plot](../moduleReference/moduleGraphPlot.html#modulegraphplot) and
[music21.graph.primitives](../moduleReference/moduleGraphPrimitives.html#modulegraphprimitives) for more information.

We can look at the individual data points:

```python
data = scatter.data
len(data)
```

```python
 165
```

```python
data[0]
```

```python
 (0.0, 1, {})
```

Here we see that at X = 0.0, there is a Y value of 1. Since pitchClass 1
is C#, this makes perfect sense. Let’s move it to D# (pitch class 3).
Since it is a tuple, this won’t work:

```python
data[0][1] = 3
```

```python
---------------------------------------------------------------------------

TypeError                                 Traceback (most recent call last)

Cell In[13], line 1
----> 1 data[0][1] = 3

TypeError: 'tuple' object does not support item assignment
```

Tuples are immutable (unchangeable) objects. But we can make a new tuple
and put it back into data:

```python
data[0] = (0.0, 3, {})
```

If we call `.run()` again, however, the stream will be extracted again
and this data point will be lost. Instead we can call `.process()`
which just regenerates the graph:

```python
scatter.process()
```

[![../_images/usersGuide_44_advancedGraphing_27_0.png](../_images/usersGuide_44_advancedGraphing_27_0.png)](../_images/usersGuide_44_advancedGraphing_27_0.png)

Do you see that the first point has moved from C# to D#? Very nice.

In case it’s not clear, we can add an annotation to the plot. After
generating the plot once, it is stored in a variable called
`.subplot`:

```python
scatter.subplot
```

```python
 <Axes: title={'center': 'Bach and his notes'}, xlabel='Measure Number', ylabel='Pitch Class'>
```

On that subplot we can use any of the `Artist` tools found in the
matplotlib toolkit. For more info [click
here](https://matplotlib.org/2.0.2/users/artists.html). For instance,
we can add a circle around that dot to make it clearer:

```python
# it is customary to rename matplotlib.pyplot as plt
from matplotlib import pyplot as plt
center = (0.0, 3) # right on the dot
radius = 1.0
circleDsharp = plt.Circle(center, radius, color='red', alpha=0.5)
scatter.subplot.add_artist(circleDsharp)
```

```python
 <matplotlib.patches.Circle at 0x1160d3850>
```

Of course we can’t call `.run()` any more since that recreates the
data from the stream. But we also can’t call process, since that
recreates the subplot. Instead to reuse the existing `.subplot` we
should call `.write()`

```python
scatter.write()
```

[![../_images/usersGuide_44_advancedGraphing_33_0.png](../_images/usersGuide_44_advancedGraphing_33_0.png)](../_images/usersGuide_44_advancedGraphing_33_0.png)

Because we’ve skewed our figureSize, it might be more of an ellipse than
a circle, but you get the idea. So to review:

* `.run()` the first time, to process the stream and get the data.
* `.process()` when the data has been changed and the figure needs to
  be regenerated from data.
* `.write()` when the figure has been created once, annotated, and
  needs to be seen again.

If you want to do the whole process without showing the figures in the
meantime, then set `.doneAction = None` before calling run the first
time.

**Note:** Unfortunately, in the Jupyter notebook that I use to write
documentation, it’ll generate the images still, but maybe it’ll be fixed
in the future; if you do this outside of a notebook it’ll work.

```python
scatter2 = graph.plot.ScatterPitchClassOffset(bach)
scatter2.doneAction = None
scatter2.run(callProcess=False)

# nothing is generated because of doneAction=None
# and (for Jupyter notebook) callProcess=False

scatterData = scatter2.data
newData = []
for dataPoint in scatterData:
    x, y, somethingElseIWillDiscussSoon = dataPoint

    if y == 6:  # F#
        continue  # F sharp is evil! :-)
    newData.append(dataPoint)

scatter2.data = newData
scatter2.process()  # rewrite the data

xyLowerLeft = (1, 5.75)
boxWidth = bach.highestTime - 1.0
boxHeight = 0.5
fSharpBox = plt.Rectangle(xyLowerLeft, boxWidth, boxHeight, color='green', alpha=0.5)
scatter2.subplot.add_artist(fSharpBox)

textAnnotation = plt.Text(bach.highestTime / 2 - 4, 7, 'F# is gone!')
scatter2.subplot.add_artist(textAnnotation)

unused = scatter2.write()
```

[![../_images/usersGuide_44_advancedGraphing_35_0.png](../_images/usersGuide_44_advancedGraphing_35_0.png)](../_images/usersGuide_44_advancedGraphing_35_0.png)

## Axis (and allies)

When calling `Stream.plot()` or `plotStream(stream)` or using
`getPlotsToMake()` we’ve been passing in two different types of
arguments, the first is the type of Graph primitive to make and the
second and subsequent are the quantities to put on the X and Y axes.
Each quantity has an [`Axis`](../moduleReference/moduleGraphAxis.html#music21.graph.axis.Axis "music21.graph.axis.Axis") object that
generates it. Let’s look more closely at a simple set of axes, the
[`PitchClassAxis`](../moduleReference/moduleGraphAxis.html#music21.graph.axis.PitchClassAxis "music21.graph.axis.PitchClassAxis") and the
[`QuarterLengthAxis`](../moduleReference/moduleGraphAxis.html#music21.graph.axis.QuarterLengthAxis "music21.graph.axis.QuarterLengthAxis"). The others are
similar.

First we’ll create a Plot object that uses these axes, such as
[`ScatterPitchClassQuarterLength`](../moduleReference/moduleGraphPlot.html#music21.graph.plot.ScatterPitchClassQuarterLength "music21.graph.plot.ScatterPitchClassQuarterLength"):

```python
scatter3 = graph.plot.ScatterPitchClassQuarterLength(bach)
scatter3.run()
```

[![../_images/usersGuide_44_advancedGraphing_37_0.png](../_images/usersGuide_44_advancedGraphing_37_0.png)](../_images/usersGuide_44_advancedGraphing_37_0.png)

Now let’s look inside it for the axes:

```python
scatter3.axisX
```

```python
 <music21.graph.axis.QuarterLengthAxis: x axis for ScatterPitchClassQuarterLength>
```

```python
scatter3.axisY
```

```python
 <music21.graph.axis.PitchClassAxis: y axis for ScatterPitchClassQuarterLength>
```

Each axis defines its own label name:

```python
(scatter3.axisX.label, scatter3.axisY.label)
```

```python
 ('Quarter Length ($log_2$)', 'Pitch Class')
```

(The use of ‘$log\_2$’ shows how TeX formatting can be used in labels –
too advanced a subject to discuss here, but something to consider)

Axes also know their axis name, their `client` (the Plot object), and
the stream they are operating on:

```python
(scatter3.axisY.axisName, scatter3.axisY.client, scatter3.axisY.stream)
```

```python
 ('y',
  <music21.graph.plot.ScatterPitchClassQuarterLength for <music21.stream.Score bwv66>>,
  <music21.stream.Score bwv66>)
```

There are three important things that any axis must do:

1. Take in each element and return values
2. Define the extent of the axis (minimum and maximum)
3. Show where “ticks”, that is, the axis value labels and grid lines
   will be.

If the second or third aren’t given then some default values will be
used. The first is the only one that absolutely needs to be defined to
do anything useful, so we’ll look at it first. Axes work on individual
elements through the “extractOneElement” method. A typical
extractOneElement, such as for `PitchClassAxis` looks something like
this:

```python
def extractOneElement(self, n, formatDict_ignore_for_now):
    if hasattr(n, 'pitch'):
        return n.pitch.pitchClass
```

If the element is something that the axis cannot handle (say a Rest)
feel free to return None or just don’t set a return value.

for instance, if there were a ‘Cardinality Axis’ which reported the
number of pitches at that moment, it would look something like this:

```python
class CardinalityAxis(graph.axis.Axis):
    labelDefault = 'Number of Pitches'

    def extractOneElement(self, el, formatDict):
        if hasattr(el, 'pitches'):
            return len(el.pitches)
        else:
            return 0
```

Testing is always important:

```python
ca = CardinalityAxis()
ca.extractOneElement(chord.Chord('C E G'), None)
```

```python
 3
```

```python
ca.extractOneElement(note.Note('D#'), None)
```

```python
 1
```

```python
ca.extractOneElement(note.Rest(), None)
```

```python
 0
```

Here we can rely on the default values for the
[`setBoundariesFromData()`](../moduleReference/moduleGraphAxis.html#music21.graph.axis.Axis.setBoundariesFromData "music21.graph.axis.Axis.setBoundariesFromData") and
[`ticks()`](../moduleReference/moduleGraphAxis.html#music21.graph.axis.Axis.ticks "music21.graph.axis.Axis.ticks") methods since they will get the
minimum and maximum value from the data and give numeric ticks which
seems fine to me. Let’s try this on a Schoenberg piece with a lot of
chords.

```python
schoenberg6 = corpus.parse('schoenberg/opus19', 6)
schoenberg6.measures(1, 4).show()
```

[![../_images/usersGuide_44_advancedGraphing_52_0.png](../_images/usersGuide_44_advancedGraphing_52_0.png)](../_images/usersGuide_44_advancedGraphing_52_0.png)

We’ll chordify the piece so that each chord has all the notes from each
hand:

```python
schChords = schoenberg6.chordify()
schChords.measures(1, 4).show()
```

[![../_images/usersGuide_44_advancedGraphing_54_0.png](../_images/usersGuide_44_advancedGraphing_54_0.png)](../_images/usersGuide_44_advancedGraphing_54_0.png)

Now we’ll create a generic Scatter object to handle it:

```python
plotS = graph.plot.Scatter(schChords)
```

And add a title and two axes, one being our new Cardinality axis:

```python
plotS.title = 'Offset vs Cardinality'
plotS.axisX = graph.axis.OffsetAxis(plotS, 'x')
plotS.axisY = CardinalityAxis(plotS, 'y')
```

Notice that in instantiating an axis, we pass in the plot name and the
axis label. Both are important.

Now let’s run it!

```python
plotS.run()
```

[![../_images/usersGuide_44_advancedGraphing_60_0.png](../_images/usersGuide_44_advancedGraphing_60_0.png)](../_images/usersGuide_44_advancedGraphing_60_0.png)

Pretty cool, eh? Maybe we should customize the tick values:

```python
def cardinalityTicks(self):
    names = ['rest', 'single', 'dyad', 'triad', 'tetrachord',
             'pentachord', 'hexachord', 'septachord', 'octochord']
    ticks = []
    for i in range(int(self.minValue), int(self.maxValue) + 1):
        tickLocation = i
        cardinalityName = names[i]  # ideally, check that names[i] exists
        tickTuple = (tickLocation, cardinalityName)
        ticks.append(tickTuple)
    return ticks

CardinalityAxis.ticks = cardinalityTicks
```

We will set up our Scatter plot so that it gets rests also, reset the
axis minimum to None (so it learns from the data) and we’ll be set to
run.

```python
plotS.classFilterList.append('Rest')
plotS.axisY.minValue = None
plotS.run()
```

[![../_images/usersGuide_44_advancedGraphing_64_0.png](../_images/usersGuide_44_advancedGraphing_64_0.png)](../_images/usersGuide_44_advancedGraphing_64_0.png)

Ideally, we’d set a slightly different minValue in
`.setBoundariesFromData` so that the bottom of the rest dots wasn’t
cut off, etc. but this is pretty good to start.

After all the data has been extracted, each axis gets a chance to
manipulate all the data however it sees fit in the `.postProcessData`
method; the only axis that currently manipulates data is the
`CountingAxis` in its
[`postProcessData()`](../moduleReference/moduleGraphAxis.html#music21.graph.axis.CountingAxis.postProcessData "music21.graph.axis.CountingAxis.postProcessData") routine,
which consolidates duplicate entries and gets a count of them. But for
the most part, setting `.ticks` and `.extractOneElement` will be
enough to make a great new axis.

## Customizing Data Points

Instead of adding things like circles directly to the graph, it’s
possible to manipulate the display attributes of individual data points
directly. To do this, we can manipulate the last element of each piece
of data, called the `formatDict`, which is just a dictionary of
formatting values to pass to matplotlib. Some of the common ones are:

* ‘alpha’ sets transparency, from 0 (transparent) to 1 (opaque).
* ‘color’ gives a color to the data point – specified like “red” or
  “green” or an HTML color like “#ff0044”
* ‘marker’ on a scatter plot will choose a shape for a marker as in
  [this diagram](https://matplotlib.org/stable/api/markers_api.html)
* ‘markersize’ gives the size of the marker – notice that we’re using
  matplotlib names, so the “s” of size is lowercased (in `music21`
  almost everything is camelCase)

Let’s make a new axis class which returns the frequency of each pitch
but also changes its marker according to whether it’s in a certain key
or not:

```python
class FrequencyScaleAxis(graph.axis.Axis):
    labelDefault = 'Frequency'

    def __init__(self, client=None, axisName='y'):
        super().__init__(client, axisName)
        self.scale = scale.MajorScale('C')

    def ticks(self):
        '''
        Only get multiples of 400 as ticks
        '''
        ticks = super().ticks()
        newTicks = [tick for tick in ticks if tick[0] % 400 == 0]
        return newTicks

    def extractOneElement(self, el, formatDict):
        if not hasattr(el, 'pitch'):
            # perhaps a chord?
            # in which case the individual notes
            # will come here later
            return None

        scalePitches = self.scale.pitches
        pitchNames = [p.name for p in scalePitches]

        # modify formatDict in place

        if el.pitch.name in pitchNames:
            formatDict['marker'] = 'o'
            formatDict['color'] = 'red'
            formatDict['markersize'] = 10
        else:
            formatDict['marker'] = 'd'
            formatDict['color'] = 'black'
            formatDict['markersize'] = 8

        return int(el.pitch.frequency)
```

Check to see that it works:

```python
fsa = FrequencyScaleAxis()
formatDict = {}
n = note.Note('A4')
fsa.extractOneElement(n, formatDict)
```

```python
 440
```

```python
formatDict
```

```python
 {'marker': 'o', 'color': 'red', 'markersize': 10}
```

```python
formatDict = {}
n = note.Note('B-4')
fsa.extractOneElement(n, formatDict)
```

```python
 466
```

```python
formatDict
```

```python
 {'marker': 'd', 'color': 'black', 'markersize': 8}
```

Let’s make a stream with some data:

```python
s = stream.Stream()
for ps in range(48, 96):
    n = note.Note()
    n.pitch.ps = ps
    s.append(n)
```

Okay, let’s create a Scatter plot and make it happen:

```python
scatterFreq = graph.plot.Scatter(s, title='frequency in C major')
scatterFreq.figureSize = (10, 5)
scatterFreq.alpha = 1
scatterFreq.axisX = graph.axis.OffsetAxis(scatterFreq, 'x')
scatterFreq.axisY = FrequencyScaleAxis(scatterFreq, 'y')
scatterFreq.run()
```

[![../_images/usersGuide_44_advancedGraphing_76_0.png](../_images/usersGuide_44_advancedGraphing_76_0.png)](../_images/usersGuide_44_advancedGraphing_76_0.png)

## Graph Primitives

Untill now, all our our examples have used Plot classes taken from
[music21.graph.plot](../moduleReference/moduleGraphPlot.html#modulegraphplot) because they were acting on streams to get
their data. If you wanted to make graphs of data not coming from a
Stream you could use matplotlib directly – they have a great tutorial on
using their ``pyplot`
interface <<https://matplotlib.org/2.0.2/users/pyplot_tutorial.html>>`\_\_,
for instance. Or if you want to get some of the advantages of the
`music21` Plot types without going all the way into matplotlib, there
are Graph primitives in the [music21.graph.primitives](../moduleReference/moduleGraphPrimitives.html#modulegraphprimitives) module. Here
are some examples of how those work:

Here is a way of plotting the life and death dates of composers. We will
put both Schumanns on the same line to show how that can be done.

```python
data = [('Chopin', [(1810, 1849-1810)]),
        ('Schumanns', [(1810, 1856-1810), (1819, 1896-1819)]),
        ('Brahms', [(1833, 1897-1833)])]

data
```

```python
 [('Chopin', [(1810, 39)]),
  ('Schumanns', [(1810, 46), (1819, 77)]),
  ('Brahms', [(1833, 64)])]
```

Each box has a starting point (birth date) and length. For the length we
needed to calculate lengths of lives for each composer, and I didn’t
have that information, so I just subtracted the death year from the
birth year.

Because we are creating graphs on our own, we will need to define our
own tick values.

```python
xTicks = [(1810, '1810'),
          (1848, '1848'),
          (1897, '1897')]
```

*Music history/European history Pop Quiz! Why a tick at 1848?* 😊 *Okay,
back to not being a musicologist…*

Now we can create a GraphHorizontalBar and `process` (not `run`) it:

```python
ghb = graph.primitives.GraphHorizontalBar()
ghb.title = 'Romantics live long and not so long'
ghb.data = data
ghb.setTicks('x', xTicks)
ghb.process()
```

[![../_images/usersGuide_44_advancedGraphing_83_0.png](../_images/usersGuide_44_advancedGraphing_83_0.png)](../_images/usersGuide_44_advancedGraphing_83_0.png)

Here is an example that graphs seven major scales next to each other in
terms of frequency showing which notes are present and which notes are
not:

```python
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
data = []

for numSharps in range(0, 7):
    keySig = key.KeySignature(numSharps)
    majScale = keySig.getScale('major')
    tonicPitch = majScale.tonic
    scaleDict = {'color': colors[numSharps]}
    for deg in range(1, 8):
        thisPitch = majScale.pitchFromDegree(deg)
        thisPitch.transposeAboveTarget(tonicPitch, inPlace=True)
        data.append((tonicPitch.pitchClass, thisPitch.pitchClass, thisPitch.frequency, scaleDict))

data[0:10]
```

```python
 [(0, 0, 261.6255653005985, {'color': 'red'}),
  (0, 2, 293.66476791740746, {'color': 'red'}),
  (0, 4, 329.62755691286986, {'color': 'red'}),
  (0, 5, 349.2282314330038, {'color': 'red'}),
  (0, 7, 391.99543598174927, {'color': 'red'}),
  (0, 9, 440.0, {'color': 'red'}),
  (0, 11, 493.8833012561241, {'color': 'red'}),
  (7, 7, 391.99543598174927, {'color': 'orange'}),
  (7, 9, 440.0, {'color': 'orange'}),
  (7, 11, 493.8833012561241, {'color': 'orange'})]
```

```python
a = graph.primitives.Graph3DBars(title='Seven Major Scales',
                                 alpha=0.5,
                                 barWidth=0.2,
                                 useKeyValues=True,
                                 figureSize=(10, 10, 4),
                                )
a.data = data
a.axis['x']['ticks'] = (range(12), ('c c# d d# e f f# g g# a a# b').split())
a.axis['y']['ticks'] = (range(12), ('c c# d d# e f f# g g# a a# b').split())
a.axis['z']['range'] = (0, 1000)

a.setAxisLabel('x', 'Root Notes')
a.setAxisLabel('y', 'Scale Degrees')
a.setAxisLabel('z', 'Frequency in Hz')
a.process()
```

[![../_images/usersGuide_44_advancedGraphing_86_0.png](../_images/usersGuide_44_advancedGraphing_86_0.png)](../_images/usersGuide_44_advancedGraphing_86_0.png)

But sometimes you need to go all the way back to Matplotlib to get the
graph that you want, such as this graph showing the motion of individual
parts in a Bach Chorale. (You’ll need `scipy` to be installed for this
to work)

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
from music21 import corpus

bach = corpus.parse('bwv66.6')

fig = plt.figure()
subplot = fig.add_subplot(1, 1, 1)

for i in range(len(bach.parts)):
    top = bach.parts[i].flatten().notes
    y = [n.pitch.ps for n in top]
    x = [n.offset + n.quarterLength/2.0 for n in top]

    tick = interpolate.splrep(x, y, s=0)
    xnew = np.arange(0, max(x), 0.01)
    ynew = interpolate.splev(xnew, tick, der=0)

    subplot.plot(xnew, ynew)
    subplot.spines['top'].set_color('none')
    subplot.spines['right'].set_color('none')

plt.title('Bach motion')

plt.show()
```

[![../_images/usersGuide_44_advancedGraphing_88_0.png](../_images/usersGuide_44_advancedGraphing_88_0.png)](../_images/usersGuide_44_advancedGraphing_88_0.png)

Well, that’s enough for getting down to details. If it’s all a bit of a
blur, remember that calling `.plot()` with a few parameters on any
stream will usually be enough to be able to visualize a score in
interesting ways.

## Embedding in Apps: Selecting the matplotlib Backend

Most people will graph music21 data using matplotlib’s default system
for rendering and displaying images (called the backend). That default
system is the TkAgg backend or the backend for Jupyter/IPython. But for
embedding music21 in other graphical user interfaces you may want to
choose another backend.

For instance if you wanted to use music21 in a Qt application, or Kivy,
or a web application, you would probably need a different backend.

See the following discussion at [What is a
backend?](https://matplotlib.org/2.0.2/faq/usage_faq.html#what-is-a-backend)
for more information.

Enough with graphs!

The next completed chapter is
[Chapter 53, Advanced Corpus and Metadata Searching](usersGuide_53_advancedCorpus.html#usersguide-53-advancedcorpus)
