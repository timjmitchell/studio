Source: https://music21.org/music21docs/moduleReference/moduleGraphPlot.html

# music21.graph.plot

Object definitions for plotting `Stream` objects.

The [`PlotStream`](#music21.graph.plot.PlotStream "music21.graph.plot.PlotStream")
object subclasses combine a Graph object with the PlotStreamMixin to give
reusable approaches to graphing data and structures in
`Stream` objects.

## HistogramPitchSpace

class music21.graph.plot.HistogramPitchSpace(*streamObj=None*, *\*\*keywords*)[[source]](../_modules/music21/graph/plot.html#HistogramPitchSpace)
:   A histogram of pitch space.

    ```python
    >>> s = corpus.parse('bach/bwv57.8')
    >>> p = graph.plot.HistogramPitchSpace(s)
    >>> p.id
    'histogram-pitchSpace-count'
    >>> p.run()  # with defaults and proper configuration, will open graph
    ```

    [![../_images/HistogramPitchSpace.png](../_images/HistogramPitchSpace.png)](../_images/HistogramPitchSpace.png)

[`HistogramPitchSpace`](#music21.graph.plot.HistogramPitchSpace "music21.graph.plot.HistogramPitchSpace") bases

* [`Histogram`](#music21.graph.plot.Histogram "music21.graph.plot.Histogram")
* [`GraphHistogram`](moduleGraphPrimitives.html#music21.graph.primitives.GraphHistogram "music21.graph.primitives.GraphHistogram")
* [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph")
* [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`HistogramPitchSpace`](#music21.graph.plot.HistogramPitchSpace "music21.graph.plot.HistogramPitchSpace") read-only properties

Read-only properties inherited from [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin"):

|  |  |  |
| --- | --- | --- |
| * [`allAxes`](#music21.graph.plot.PlotStreamMixin.allAxes "music21.graph.plot.PlotStreamMixin.allAxes") | * [`id`](#music21.graph.plot.PlotStreamMixin.id "music21.graph.plot.PlotStreamMixin.id") |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`HistogramPitchSpace`](#music21.graph.plot.HistogramPitchSpace "music21.graph.plot.HistogramPitchSpace") read/write properties

Read/write properties inherited from [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph"):

|  |  |  |
| --- | --- | --- |
| * [`doneAction`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.doneAction "music21.graph.primitives.Graph.doneAction") |  |  |

[`HistogramPitchSpace`](#music21.graph.plot.HistogramPitchSpace "music21.graph.plot.HistogramPitchSpace") methods

Methods inherited from [`Histogram`](#music21.graph.plot.Histogram "music21.graph.plot.Histogram"):

|  |  |  |
| --- | --- | --- |
| * [`remapXTicksData()`](#music21.graph.plot.Histogram.remapXTicksData "music21.graph.plot.Histogram.remapXTicksData") | * [`run()`](#music21.graph.plot.Histogram.run "music21.graph.plot.Histogram.run") |  |

Methods inherited from [`GraphHistogram`](moduleGraphPrimitives.html#music21.graph.primitives.GraphHistogram "music21.graph.primitives.GraphHistogram"):

|  |  |  |
| --- | --- | --- |
| * [`renderSubplot()`](moduleGraphPrimitives.html#music21.graph.primitives.GraphHistogram.renderSubplot "music21.graph.primitives.GraphHistogram.renderSubplot") |  |  |

Methods inherited from [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph"):

|  |  |  |
| --- | --- | --- |
| * [`applyFormatting()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyFormatting "music21.graph.primitives.Graph.applyFormatting") * [`applyFormattingToOneAxis()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyFormattingToOneAxis "music21.graph.primitives.Graph.applyFormattingToOneAxis") * [`applyGrid()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyGrid "music21.graph.primitives.Graph.applyGrid") * [`callDoneAction()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.callDoneAction "music21.graph.primitives.Graph.callDoneAction") * [`hideAxisSpines()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.hideAxisSpines "music21.graph.primitives.Graph.hideAxisSpines") | * [`nextColor()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.nextColor "music21.graph.primitives.Graph.nextColor") * [`process()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.process "music21.graph.primitives.Graph.process") * [`setAxisLabel()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setAxisLabel "music21.graph.primitives.Graph.setAxisLabel") * [`setAxisRange()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setAxisRange "music21.graph.primitives.Graph.setAxisRange") | * [`setIntegerTicksFromData()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setIntegerTicksFromData "music21.graph.primitives.Graph.setIntegerTicksFromData") * [`setTicks()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setTicks "music21.graph.primitives.Graph.setTicks") * [`show()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.show "music21.graph.primitives.Graph.show") * [`write()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.write "music21.graph.primitives.Graph.write") |

Methods inherited from [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin"):

|  |  |  |
| --- | --- | --- |
| * [`extractChordDataMultiAxis()`](#music21.graph.plot.PlotStreamMixin.extractChordDataMultiAxis "music21.graph.plot.PlotStreamMixin.extractChordDataMultiAxis") * [`extractChordDataOneAxis()`](#music21.graph.plot.PlotStreamMixin.extractChordDataOneAxis "music21.graph.plot.PlotStreamMixin.extractChordDataOneAxis") * [`extractData()`](#music21.graph.plot.PlotStreamMixin.extractData "music21.graph.plot.PlotStreamMixin.extractData") | * [`fillValueLists()`](#music21.graph.plot.PlotStreamMixin.fillValueLists "music21.graph.plot.PlotStreamMixin.fillValueLists") * [`postProcessData()`](#music21.graph.plot.PlotStreamMixin.postProcessData "music21.graph.plot.PlotStreamMixin.postProcessData") * [`postProcessElement()`](#music21.graph.plot.PlotStreamMixin.postProcessElement "music21.graph.plot.PlotStreamMixin.postProcessElement") | * [`processOneElement()`](#music21.graph.plot.PlotStreamMixin.processOneElement "music21.graph.plot.PlotStreamMixin.processOneElement") * [`setAxisKeywords()`](#music21.graph.plot.PlotStreamMixin.setAxisKeywords "music21.graph.plot.PlotStreamMixin.setAxisKeywords") |

[`HistogramPitchSpace`](#music21.graph.plot.HistogramPitchSpace "music21.graph.plot.HistogramPitchSpace") instance variables

Instance variables inherited from [`GraphHistogram`](moduleGraphPrimitives.html#music21.graph.primitives.GraphHistogram "music21.graph.primitives.GraphHistogram"):

|  |  |  |
| --- | --- | --- |
| * [`binWidth`](moduleGraphPrimitives.html#music21.graph.primitives.GraphHistogram.binWidth "music21.graph.primitives.GraphHistogram.binWidth") |  |  |

## HistogramPitchClass

class music21.graph.plot.HistogramPitchClass(*streamObj=None*, *\*\*keywords*)[[source]](../_modules/music21/graph/plot.html#HistogramPitchClass)
:   A histogram of pitch class

    ```python
    >>> s = corpus.parse('bach/bwv57.8')
    >>> p = graph.plot.HistogramPitchClass(s)
    >>> p.id
    'histogram-pitchClass-count'
    >>> p.run()  # with defaults and proper configuration, will open graph
    ```

    [![../_images/HistogramPitchClass.png](../_images/HistogramPitchClass.png)](../_images/HistogramPitchClass.png)

[`HistogramPitchClass`](#music21.graph.plot.HistogramPitchClass "music21.graph.plot.HistogramPitchClass") bases

* [`Histogram`](#music21.graph.plot.Histogram "music21.graph.plot.Histogram")
* [`GraphHistogram`](moduleGraphPrimitives.html#music21.graph.primitives.GraphHistogram "music21.graph.primitives.GraphHistogram")
* [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph")
* [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`HistogramPitchClass`](#music21.graph.plot.HistogramPitchClass "music21.graph.plot.HistogramPitchClass") read-only properties

Read-only properties inherited from [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin"):

|  |  |  |
| --- | --- | --- |
| * [`allAxes`](#music21.graph.plot.PlotStreamMixin.allAxes "music21.graph.plot.PlotStreamMixin.allAxes") | * [`id`](#music21.graph.plot.PlotStreamMixin.id "music21.graph.plot.PlotStreamMixin.id") |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`HistogramPitchClass`](#music21.graph.plot.HistogramPitchClass "music21.graph.plot.HistogramPitchClass") read/write properties

Read/write properties inherited from [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph"):

|  |  |  |
| --- | --- | --- |
| * [`doneAction`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.doneAction "music21.graph.primitives.Graph.doneAction") |  |  |

[`HistogramPitchClass`](#music21.graph.plot.HistogramPitchClass "music21.graph.plot.HistogramPitchClass") methods

Methods inherited from [`Histogram`](#music21.graph.plot.Histogram "music21.graph.plot.Histogram"):

|  |  |  |
| --- | --- | --- |
| * [`remapXTicksData()`](#music21.graph.plot.Histogram.remapXTicksData "music21.graph.plot.Histogram.remapXTicksData") | * [`run()`](#music21.graph.plot.Histogram.run "music21.graph.plot.Histogram.run") |  |

Methods inherited from [`GraphHistogram`](moduleGraphPrimitives.html#music21.graph.primitives.GraphHistogram "music21.graph.primitives.GraphHistogram"):

|  |  |  |
| --- | --- | --- |
| * [`renderSubplot()`](moduleGraphPrimitives.html#music21.graph.primitives.GraphHistogram.renderSubplot "music21.graph.primitives.GraphHistogram.renderSubplot") |  |  |

Methods inherited from [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph"):

|  |  |  |
| --- | --- | --- |
| * [`applyFormatting()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyFormatting "music21.graph.primitives.Graph.applyFormatting") * [`applyFormattingToOneAxis()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyFormattingToOneAxis "music21.graph.primitives.Graph.applyFormattingToOneAxis") * [`applyGrid()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyGrid "music21.graph.primitives.Graph.applyGrid") * [`callDoneAction()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.callDoneAction "music21.graph.primitives.Graph.callDoneAction") * [`hideAxisSpines()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.hideAxisSpines "music21.graph.primitives.Graph.hideAxisSpines") | * [`nextColor()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.nextColor "music21.graph.primitives.Graph.nextColor") * [`process()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.process "music21.graph.primitives.Graph.process") * [`setAxisLabel()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setAxisLabel "music21.graph.primitives.Graph.setAxisLabel") * [`setAxisRange()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setAxisRange "music21.graph.primitives.Graph.setAxisRange") | * [`setIntegerTicksFromData()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setIntegerTicksFromData "music21.graph.primitives.Graph.setIntegerTicksFromData") * [`setTicks()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setTicks "music21.graph.primitives.Graph.setTicks") * [`show()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.show "music21.graph.primitives.Graph.show") * [`write()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.write "music21.graph.primitives.Graph.write") |

Methods inherited from [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin"):

|  |  |  |
| --- | --- | --- |
| * [`extractChordDataMultiAxis()`](#music21.graph.plot.PlotStreamMixin.extractChordDataMultiAxis "music21.graph.plot.PlotStreamMixin.extractChordDataMultiAxis") * [`extractChordDataOneAxis()`](#music21.graph.plot.PlotStreamMixin.extractChordDataOneAxis "music21.graph.plot.PlotStreamMixin.extractChordDataOneAxis") * [`extractData()`](#music21.graph.plot.PlotStreamMixin.extractData "music21.graph.plot.PlotStreamMixin.extractData") | * [`fillValueLists()`](#music21.graph.plot.PlotStreamMixin.fillValueLists "music21.graph.plot.PlotStreamMixin.fillValueLists") * [`postProcessData()`](#music21.graph.plot.PlotStreamMixin.postProcessData "music21.graph.plot.PlotStreamMixin.postProcessData") * [`postProcessElement()`](#music21.graph.plot.PlotStreamMixin.postProcessElement "music21.graph.plot.PlotStreamMixin.postProcessElement") | * [`processOneElement()`](#music21.graph.plot.PlotStreamMixin.processOneElement "music21.graph.plot.PlotStreamMixin.processOneElement") * [`setAxisKeywords()`](#music21.graph.plot.PlotStreamMixin.setAxisKeywords "music21.graph.plot.PlotStreamMixin.setAxisKeywords") |

[`HistogramPitchClass`](#music21.graph.plot.HistogramPitchClass "music21.graph.plot.HistogramPitchClass") instance variables

Instance variables inherited from [`GraphHistogram`](moduleGraphPrimitives.html#music21.graph.primitives.GraphHistogram "music21.graph.primitives.GraphHistogram"):

|  |  |  |
| --- | --- | --- |
| * [`binWidth`](moduleGraphPrimitives.html#music21.graph.primitives.GraphHistogram.binWidth "music21.graph.primitives.GraphHistogram.binWidth") |  |  |

## HistogramQuarterLength

class music21.graph.plot.HistogramQuarterLength(*streamObj=None*, *\*\*keywords*)[[source]](../_modules/music21/graph/plot.html#HistogramQuarterLength)
:   A histogram of pitch class.

    ```python
    >>> s = corpus.parse('bach/bwv57.8')
    >>> p = graph.plot.HistogramQuarterLength(s)
    >>> p.id
    'histogram-quarterLength-count'
    >>> p.run()  # with defaults and proper configuration, will open graph
    ```

    [![../_images/HistogramQuarterLength.png](../_images/HistogramQuarterLength.png)](../_images/HistogramQuarterLength.png)

[`HistogramQuarterLength`](#music21.graph.plot.HistogramQuarterLength "music21.graph.plot.HistogramQuarterLength") bases

* [`Histogram`](#music21.graph.plot.Histogram "music21.graph.plot.Histogram")
* [`GraphHistogram`](moduleGraphPrimitives.html#music21.graph.primitives.GraphHistogram "music21.graph.primitives.GraphHistogram")
* [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph")
* [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`HistogramQuarterLength`](#music21.graph.plot.HistogramQuarterLength "music21.graph.plot.HistogramQuarterLength") read-only properties

Read-only properties inherited from [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin"):

|  |  |  |
| --- | --- | --- |
| * [`allAxes`](#music21.graph.plot.PlotStreamMixin.allAxes "music21.graph.plot.PlotStreamMixin.allAxes") | * [`id`](#music21.graph.plot.PlotStreamMixin.id "music21.graph.plot.PlotStreamMixin.id") |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`HistogramQuarterLength`](#music21.graph.plot.HistogramQuarterLength "music21.graph.plot.HistogramQuarterLength") read/write properties

Read/write properties inherited from [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph"):

|  |  |  |
| --- | --- | --- |
| * [`doneAction`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.doneAction "music21.graph.primitives.Graph.doneAction") |  |  |

[`HistogramQuarterLength`](#music21.graph.plot.HistogramQuarterLength "music21.graph.plot.HistogramQuarterLength") methods

Methods inherited from [`Histogram`](#music21.graph.plot.Histogram "music21.graph.plot.Histogram"):

|  |  |  |
| --- | --- | --- |
| * [`remapXTicksData()`](#music21.graph.plot.Histogram.remapXTicksData "music21.graph.plot.Histogram.remapXTicksData") | * [`run()`](#music21.graph.plot.Histogram.run "music21.graph.plot.Histogram.run") |  |

Methods inherited from [`GraphHistogram`](moduleGraphPrimitives.html#music21.graph.primitives.GraphHistogram "music21.graph.primitives.GraphHistogram"):

|  |  |  |
| --- | --- | --- |
| * [`renderSubplot()`](moduleGraphPrimitives.html#music21.graph.primitives.GraphHistogram.renderSubplot "music21.graph.primitives.GraphHistogram.renderSubplot") |  |  |

Methods inherited from [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph"):

|  |  |  |
| --- | --- | --- |
| * [`applyFormatting()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyFormatting "music21.graph.primitives.Graph.applyFormatting") * [`applyFormattingToOneAxis()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyFormattingToOneAxis "music21.graph.primitives.Graph.applyFormattingToOneAxis") * [`applyGrid()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyGrid "music21.graph.primitives.Graph.applyGrid") * [`callDoneAction()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.callDoneAction "music21.graph.primitives.Graph.callDoneAction") * [`hideAxisSpines()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.hideAxisSpines "music21.graph.primitives.Graph.hideAxisSpines") | * [`nextColor()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.nextColor "music21.graph.primitives.Graph.nextColor") * [`process()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.process "music21.graph.primitives.Graph.process") * [`setAxisLabel()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setAxisLabel "music21.graph.primitives.Graph.setAxisLabel") * [`setAxisRange()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setAxisRange "music21.graph.primitives.Graph.setAxisRange") | * [`setIntegerTicksFromData()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setIntegerTicksFromData "music21.graph.primitives.Graph.setIntegerTicksFromData") * [`setTicks()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setTicks "music21.graph.primitives.Graph.setTicks") * [`show()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.show "music21.graph.primitives.Graph.show") * [`write()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.write "music21.graph.primitives.Graph.write") |

Methods inherited from [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin"):

|  |  |  |
| --- | --- | --- |
| * [`extractChordDataMultiAxis()`](#music21.graph.plot.PlotStreamMixin.extractChordDataMultiAxis "music21.graph.plot.PlotStreamMixin.extractChordDataMultiAxis") * [`extractChordDataOneAxis()`](#music21.graph.plot.PlotStreamMixin.extractChordDataOneAxis "music21.graph.plot.PlotStreamMixin.extractChordDataOneAxis") * [`extractData()`](#music21.graph.plot.PlotStreamMixin.extractData "music21.graph.plot.PlotStreamMixin.extractData") | * [`fillValueLists()`](#music21.graph.plot.PlotStreamMixin.fillValueLists "music21.graph.plot.PlotStreamMixin.fillValueLists") * [`postProcessData()`](#music21.graph.plot.PlotStreamMixin.postProcessData "music21.graph.plot.PlotStreamMixin.postProcessData") * [`postProcessElement()`](#music21.graph.plot.PlotStreamMixin.postProcessElement "music21.graph.plot.PlotStreamMixin.postProcessElement") | * [`processOneElement()`](#music21.graph.plot.PlotStreamMixin.processOneElement "music21.graph.plot.PlotStreamMixin.processOneElement") * [`setAxisKeywords()`](#music21.graph.plot.PlotStreamMixin.setAxisKeywords "music21.graph.plot.PlotStreamMixin.setAxisKeywords") |

[`HistogramQuarterLength`](#music21.graph.plot.HistogramQuarterLength "music21.graph.plot.HistogramQuarterLength") instance variables

Instance variables inherited from [`GraphHistogram`](moduleGraphPrimitives.html#music21.graph.primitives.GraphHistogram "music21.graph.primitives.GraphHistogram"):

|  |  |  |
| --- | --- | --- |
| * [`binWidth`](moduleGraphPrimitives.html#music21.graph.primitives.GraphHistogram.binWidth "music21.graph.primitives.GraphHistogram.binWidth") |  |  |

## WindowedKey

class music21.graph.plot.WindowedKey(*streamObj=None*, *\*\*keywords*)[[source]](../_modules/music21/graph/plot.html#WindowedKey)
:   Stream plotting of windowed version of Krumhansl-Schmuckler analysis routine.
    See [`KrumhanslSchmuckler`](moduleAnalysisDiscrete.html#music21.analysis.discrete.KrumhanslSchmuckler "music21.analysis.discrete.KrumhanslSchmuckler") for more details.

    ```python
    >>> s = corpus.parse('bach/bwv66.6')
    >>> p = graph.plot.WindowedKey(s.parts[0])
    >>> p.run()  # with defaults and proper configuration, will open graph
    ```

    [![../_images/WindowedKrumhanslSchmuckler.png](../_images/WindowedKrumhanslSchmuckler.png)](../_images/WindowedKrumhanslSchmuckler.png)
    ![../_images/legend-WindowedKrumhanslSchmuckler.png](../_images/legend-WindowedKrumhanslSchmuckler.png)

    Set the processor class to one of the following for different uses:

    ```python
    >>> p = graph.plot.WindowedKey(s.parts.first())
    >>> p.processorClass = analysis.discrete.AardenEssen
    >>> p.processorClass = analysis.discrete.SimpleWeights
    >>> p.processorClass = analysis.discrete.BellmanBudge
    >>> p.processorClass = analysis.discrete.TemperleyKostkaPayne
    >>> p.run()
    ```

[`WindowedKey`](#music21.graph.plot.WindowedKey "music21.graph.plot.WindowedKey") bases

* [`WindowedAnalysis`](#music21.graph.plot.WindowedAnalysis "music21.graph.plot.WindowedAnalysis")
* [`GraphColorGrid`](moduleGraphPrimitives.html#music21.graph.primitives.GraphColorGrid "music21.graph.primitives.GraphColorGrid")
* [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph")
* [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`WindowedKey`](#music21.graph.plot.WindowedKey "music21.graph.plot.WindowedKey") read-only properties

Read-only properties inherited from [`WindowedAnalysis`](#music21.graph.plot.WindowedAnalysis "music21.graph.plot.WindowedAnalysis"):

|  |  |  |
| --- | --- | --- |
| * [`processor`](#music21.graph.plot.WindowedAnalysis.processor "music21.graph.plot.WindowedAnalysis.processor") |  |  |

Read-only properties inherited from [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin"):

|  |  |  |
| --- | --- | --- |
| * [`allAxes`](#music21.graph.plot.PlotStreamMixin.allAxes "music21.graph.plot.PlotStreamMixin.allAxes") | * [`id`](#music21.graph.plot.PlotStreamMixin.id "music21.graph.plot.PlotStreamMixin.id") |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`WindowedKey`](#music21.graph.plot.WindowedKey "music21.graph.plot.WindowedKey") read/write properties

Read/write properties inherited from [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph"):

|  |  |  |
| --- | --- | --- |
| * [`doneAction`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.doneAction "music21.graph.primitives.Graph.doneAction") |  |  |

[`WindowedKey`](#music21.graph.plot.WindowedKey "music21.graph.plot.WindowedKey") methods

Methods inherited from [`WindowedAnalysis`](#music21.graph.plot.WindowedAnalysis "music21.graph.plot.WindowedAnalysis"):

|  |  |  |
| --- | --- | --- |
| * [`extractData()`](#music21.graph.plot.WindowedAnalysis.extractData "music21.graph.plot.WindowedAnalysis.extractData") | * [`run()`](#music21.graph.plot.WindowedAnalysis.run "music21.graph.plot.WindowedAnalysis.run") | * [`write()`](#music21.graph.plot.WindowedAnalysis.write "music21.graph.plot.WindowedAnalysis.write") |

Methods inherited from [`GraphColorGrid`](moduleGraphPrimitives.html#music21.graph.primitives.GraphColorGrid "music21.graph.primitives.GraphColorGrid"):

|  |  |  |
| --- | --- | --- |
| * [`renderSubplot()`](moduleGraphPrimitives.html#music21.graph.primitives.GraphColorGrid.renderSubplot "music21.graph.primitives.GraphColorGrid.renderSubplot") |  |  |

Methods inherited from [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph"):

|  |  |  |
| --- | --- | --- |
| * [`applyFormatting()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyFormatting "music21.graph.primitives.Graph.applyFormatting") * [`applyFormattingToOneAxis()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyFormattingToOneAxis "music21.graph.primitives.Graph.applyFormattingToOneAxis") * [`applyGrid()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyGrid "music21.graph.primitives.Graph.applyGrid") * [`callDoneAction()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.callDoneAction "music21.graph.primitives.Graph.callDoneAction") | * [`hideAxisSpines()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.hideAxisSpines "music21.graph.primitives.Graph.hideAxisSpines") * [`nextColor()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.nextColor "music21.graph.primitives.Graph.nextColor") * [`process()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.process "music21.graph.primitives.Graph.process") * [`setAxisLabel()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setAxisLabel "music21.graph.primitives.Graph.setAxisLabel") | * [`setAxisRange()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setAxisRange "music21.graph.primitives.Graph.setAxisRange") * [`setIntegerTicksFromData()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setIntegerTicksFromData "music21.graph.primitives.Graph.setIntegerTicksFromData") * [`setTicks()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setTicks "music21.graph.primitives.Graph.setTicks") * [`show()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.show "music21.graph.primitives.Graph.show") |

Methods inherited from [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin"):

|  |  |  |
| --- | --- | --- |
| * [`extractChordDataMultiAxis()`](#music21.graph.plot.PlotStreamMixin.extractChordDataMultiAxis "music21.graph.plot.PlotStreamMixin.extractChordDataMultiAxis") * [`extractChordDataOneAxis()`](#music21.graph.plot.PlotStreamMixin.extractChordDataOneAxis "music21.graph.plot.PlotStreamMixin.extractChordDataOneAxis") * [`fillValueLists()`](#music21.graph.plot.PlotStreamMixin.fillValueLists "music21.graph.plot.PlotStreamMixin.fillValueLists") | * [`postProcessData()`](#music21.graph.plot.PlotStreamMixin.postProcessData "music21.graph.plot.PlotStreamMixin.postProcessData") * [`postProcessElement()`](#music21.graph.plot.PlotStreamMixin.postProcessElement "music21.graph.plot.PlotStreamMixin.postProcessElement") | * [`processOneElement()`](#music21.graph.plot.PlotStreamMixin.processOneElement "music21.graph.plot.PlotStreamMixin.processOneElement") * [`setAxisKeywords()`](#music21.graph.plot.PlotStreamMixin.setAxisKeywords "music21.graph.plot.PlotStreamMixin.setAxisKeywords") |

[`WindowedKey`](#music21.graph.plot.WindowedKey "music21.graph.plot.WindowedKey") instance variables

Instance variables inherited from [`GraphColorGrid`](moduleGraphPrimitives.html#music21.graph.primitives.GraphColorGrid "music21.graph.primitives.GraphColorGrid"):

|  |  |  |
| --- | --- | --- |
| * [`hideLeftBottomSpines`](moduleGraphPrimitives.html#music21.graph.primitives.GraphColorGrid.hideLeftBottomSpines "music21.graph.primitives.GraphColorGrid.hideLeftBottomSpines") |  |  |

## WindowedAmbitus

class music21.graph.plot.WindowedAmbitus(*streamObj=None*, *\*\*keywords*)[[source]](../_modules/music21/graph/plot.html#WindowedAmbitus)
:   Stream plotting of basic pitch span.

    ```python
    >>> s = corpus.parse('bach/bwv66.6')
    >>> p = graph.plot.WindowedAmbitus(s.parts.first())
    >>> p.run()  # with defaults and proper configuration, will open graph
    ```

    [![../_images/WindowedAmbitus.png](../_images/WindowedAmbitus.png)](../_images/WindowedAmbitus.png)
    ![../_images/legend-WindowedAmbitus.png](../_images/legend-WindowedAmbitus.png)

[`WindowedAmbitus`](#music21.graph.plot.WindowedAmbitus "music21.graph.plot.WindowedAmbitus") bases

* [`WindowedAnalysis`](#music21.graph.plot.WindowedAnalysis "music21.graph.plot.WindowedAnalysis")
* [`GraphColorGrid`](moduleGraphPrimitives.html#music21.graph.primitives.GraphColorGrid "music21.graph.primitives.GraphColorGrid")
* [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph")
* [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`WindowedAmbitus`](#music21.graph.plot.WindowedAmbitus "music21.graph.plot.WindowedAmbitus") read-only properties

Read-only properties inherited from [`WindowedAnalysis`](#music21.graph.plot.WindowedAnalysis "music21.graph.plot.WindowedAnalysis"):

|  |  |  |
| --- | --- | --- |
| * [`processor`](#music21.graph.plot.WindowedAnalysis.processor "music21.graph.plot.WindowedAnalysis.processor") |  |  |

Read-only properties inherited from [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin"):

|  |  |  |
| --- | --- | --- |
| * [`allAxes`](#music21.graph.plot.PlotStreamMixin.allAxes "music21.graph.plot.PlotStreamMixin.allAxes") | * [`id`](#music21.graph.plot.PlotStreamMixin.id "music21.graph.plot.PlotStreamMixin.id") |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`WindowedAmbitus`](#music21.graph.plot.WindowedAmbitus "music21.graph.plot.WindowedAmbitus") read/write properties

Read/write properties inherited from [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph"):

|  |  |  |
| --- | --- | --- |
| * [`doneAction`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.doneAction "music21.graph.primitives.Graph.doneAction") |  |  |

[`WindowedAmbitus`](#music21.graph.plot.WindowedAmbitus "music21.graph.plot.WindowedAmbitus") methods

Methods inherited from [`WindowedAnalysis`](#music21.graph.plot.WindowedAnalysis "music21.graph.plot.WindowedAnalysis"):

|  |  |  |
| --- | --- | --- |
| * [`extractData()`](#music21.graph.plot.WindowedAnalysis.extractData "music21.graph.plot.WindowedAnalysis.extractData") | * [`run()`](#music21.graph.plot.WindowedAnalysis.run "music21.graph.plot.WindowedAnalysis.run") | * [`write()`](#music21.graph.plot.WindowedAnalysis.write "music21.graph.plot.WindowedAnalysis.write") |

Methods inherited from [`GraphColorGrid`](moduleGraphPrimitives.html#music21.graph.primitives.GraphColorGrid "music21.graph.primitives.GraphColorGrid"):

|  |  |  |
| --- | --- | --- |
| * [`renderSubplot()`](moduleGraphPrimitives.html#music21.graph.primitives.GraphColorGrid.renderSubplot "music21.graph.primitives.GraphColorGrid.renderSubplot") |  |  |

Methods inherited from [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph"):

|  |  |  |
| --- | --- | --- |
| * [`applyFormatting()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyFormatting "music21.graph.primitives.Graph.applyFormatting") * [`applyFormattingToOneAxis()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyFormattingToOneAxis "music21.graph.primitives.Graph.applyFormattingToOneAxis") * [`applyGrid()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyGrid "music21.graph.primitives.Graph.applyGrid") * [`callDoneAction()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.callDoneAction "music21.graph.primitives.Graph.callDoneAction") | * [`hideAxisSpines()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.hideAxisSpines "music21.graph.primitives.Graph.hideAxisSpines") * [`nextColor()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.nextColor "music21.graph.primitives.Graph.nextColor") * [`process()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.process "music21.graph.primitives.Graph.process") * [`setAxisLabel()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setAxisLabel "music21.graph.primitives.Graph.setAxisLabel") | * [`setAxisRange()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setAxisRange "music21.graph.primitives.Graph.setAxisRange") * [`setIntegerTicksFromData()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setIntegerTicksFromData "music21.graph.primitives.Graph.setIntegerTicksFromData") * [`setTicks()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setTicks "music21.graph.primitives.Graph.setTicks") * [`show()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.show "music21.graph.primitives.Graph.show") |

Methods inherited from [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin"):

|  |  |  |
| --- | --- | --- |
| * [`extractChordDataMultiAxis()`](#music21.graph.plot.PlotStreamMixin.extractChordDataMultiAxis "music21.graph.plot.PlotStreamMixin.extractChordDataMultiAxis") * [`extractChordDataOneAxis()`](#music21.graph.plot.PlotStreamMixin.extractChordDataOneAxis "music21.graph.plot.PlotStreamMixin.extractChordDataOneAxis") * [`fillValueLists()`](#music21.graph.plot.PlotStreamMixin.fillValueLists "music21.graph.plot.PlotStreamMixin.fillValueLists") | * [`postProcessData()`](#music21.graph.plot.PlotStreamMixin.postProcessData "music21.graph.plot.PlotStreamMixin.postProcessData") * [`postProcessElement()`](#music21.graph.plot.PlotStreamMixin.postProcessElement "music21.graph.plot.PlotStreamMixin.postProcessElement") | * [`processOneElement()`](#music21.graph.plot.PlotStreamMixin.processOneElement "music21.graph.plot.PlotStreamMixin.processOneElement") * [`setAxisKeywords()`](#music21.graph.plot.PlotStreamMixin.setAxisKeywords "music21.graph.plot.PlotStreamMixin.setAxisKeywords") |

[`WindowedAmbitus`](#music21.graph.plot.WindowedAmbitus "music21.graph.plot.WindowedAmbitus") instance variables

Instance variables inherited from [`GraphColorGrid`](moduleGraphPrimitives.html#music21.graph.primitives.GraphColorGrid "music21.graph.primitives.GraphColorGrid"):

|  |  |  |
| --- | --- | --- |
| * [`hideLeftBottomSpines`](moduleGraphPrimitives.html#music21.graph.primitives.GraphColorGrid.hideLeftBottomSpines "music21.graph.primitives.GraphColorGrid.hideLeftBottomSpines") |  |  |

## ScatterPitchSpaceQuarterLength

class music21.graph.plot.ScatterPitchSpaceQuarterLength(*streamObj=None*, *\*\*keywords*)[[source]](../_modules/music21/graph/plot.html#ScatterPitchSpaceQuarterLength)
:   A scatter plot of pitch space and quarter length

    ```python
    >>> s = corpus.parse('bach/bwv324.xml')
    >>> p = graph.plot.ScatterPitchSpaceQuarterLength(s)
    >>> p.id
    'scatter-quarterLength-pitchSpace'
    >>> p.run()
    ```

    [![../_images/ScatterPitchSpaceQuarterLength.png](../_images/ScatterPitchSpaceQuarterLength.png)](../_images/ScatterPitchSpaceQuarterLength.png)

[`ScatterPitchSpaceQuarterLength`](#music21.graph.plot.ScatterPitchSpaceQuarterLength "music21.graph.plot.ScatterPitchSpaceQuarterLength") bases

* [`Scatter`](#music21.graph.plot.Scatter "music21.graph.plot.Scatter")
* [`GraphScatter`](moduleGraphPrimitives.html#music21.graph.primitives.GraphScatter "music21.graph.primitives.GraphScatter")
* [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph")
* [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`ScatterPitchSpaceQuarterLength`](#music21.graph.plot.ScatterPitchSpaceQuarterLength "music21.graph.plot.ScatterPitchSpaceQuarterLength") read-only properties

Read-only properties inherited from [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin"):

|  |  |  |
| --- | --- | --- |
| * [`allAxes`](#music21.graph.plot.PlotStreamMixin.allAxes "music21.graph.plot.PlotStreamMixin.allAxes") | * [`id`](#music21.graph.plot.PlotStreamMixin.id "music21.graph.plot.PlotStreamMixin.id") |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`ScatterPitchSpaceQuarterLength`](#music21.graph.plot.ScatterPitchSpaceQuarterLength "music21.graph.plot.ScatterPitchSpaceQuarterLength") read/write properties

Read/write properties inherited from [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph"):

|  |  |  |
| --- | --- | --- |
| * [`doneAction`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.doneAction "music21.graph.primitives.Graph.doneAction") |  |  |

[`ScatterPitchSpaceQuarterLength`](#music21.graph.plot.ScatterPitchSpaceQuarterLength "music21.graph.plot.ScatterPitchSpaceQuarterLength") methods

Methods inherited from [`GraphScatter`](moduleGraphPrimitives.html#music21.graph.primitives.GraphScatter "music21.graph.primitives.GraphScatter"):

|  |  |  |
| --- | --- | --- |
| * [`renderSubplot()`](moduleGraphPrimitives.html#music21.graph.primitives.GraphScatter.renderSubplot "music21.graph.primitives.GraphScatter.renderSubplot") |  |  |

Methods inherited from [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph"):

|  |  |  |
| --- | --- | --- |
| * [`applyFormatting()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyFormatting "music21.graph.primitives.Graph.applyFormatting") * [`applyFormattingToOneAxis()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyFormattingToOneAxis "music21.graph.primitives.Graph.applyFormattingToOneAxis") * [`applyGrid()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyGrid "music21.graph.primitives.Graph.applyGrid") * [`callDoneAction()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.callDoneAction "music21.graph.primitives.Graph.callDoneAction") * [`hideAxisSpines()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.hideAxisSpines "music21.graph.primitives.Graph.hideAxisSpines") | * [`nextColor()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.nextColor "music21.graph.primitives.Graph.nextColor") * [`process()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.process "music21.graph.primitives.Graph.process") * [`setAxisLabel()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setAxisLabel "music21.graph.primitives.Graph.setAxisLabel") * [`setAxisRange()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setAxisRange "music21.graph.primitives.Graph.setAxisRange") | * [`setIntegerTicksFromData()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setIntegerTicksFromData "music21.graph.primitives.Graph.setIntegerTicksFromData") * [`setTicks()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setTicks "music21.graph.primitives.Graph.setTicks") * [`show()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.show "music21.graph.primitives.Graph.show") * [`write()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.write "music21.graph.primitives.Graph.write") |

Methods inherited from [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin"):

|  |  |  |
| --- | --- | --- |
| * [`extractChordDataMultiAxis()`](#music21.graph.plot.PlotStreamMixin.extractChordDataMultiAxis "music21.graph.plot.PlotStreamMixin.extractChordDataMultiAxis") * [`extractChordDataOneAxis()`](#music21.graph.plot.PlotStreamMixin.extractChordDataOneAxis "music21.graph.plot.PlotStreamMixin.extractChordDataOneAxis") * [`extractData()`](#music21.graph.plot.PlotStreamMixin.extractData "music21.graph.plot.PlotStreamMixin.extractData") | * [`fillValueLists()`](#music21.graph.plot.PlotStreamMixin.fillValueLists "music21.graph.plot.PlotStreamMixin.fillValueLists") * [`postProcessData()`](#music21.graph.plot.PlotStreamMixin.postProcessData "music21.graph.plot.PlotStreamMixin.postProcessData") * [`postProcessElement()`](#music21.graph.plot.PlotStreamMixin.postProcessElement "music21.graph.plot.PlotStreamMixin.postProcessElement") | * [`processOneElement()`](#music21.graph.plot.PlotStreamMixin.processOneElement "music21.graph.plot.PlotStreamMixin.processOneElement") * [`run()`](#music21.graph.plot.PlotStreamMixin.run "music21.graph.plot.PlotStreamMixin.run") * [`setAxisKeywords()`](#music21.graph.plot.PlotStreamMixin.setAxisKeywords "music21.graph.plot.PlotStreamMixin.setAxisKeywords") |

## ScatterPitchClassQuarterLength

class music21.graph.plot.ScatterPitchClassQuarterLength(*streamObj=None*, *\*\*keywords*)[[source]](../_modules/music21/graph/plot.html#ScatterPitchClassQuarterLength)
:   A scatter plot of pitch class and quarter length

    ```python
    >>> s = corpus.parse('bach/bwv57.8')
    >>> p = graph.plot.ScatterPitchClassQuarterLength(s)
    >>> p.id
    'scatter-quarterLength-pitchClass'
    >>> p.run()
    ```

    [![../_images/ScatterPitchClassQuarterLength.png](../_images/ScatterPitchClassQuarterLength.png)](../_images/ScatterPitchClassQuarterLength.png)

[`ScatterPitchClassQuarterLength`](#music21.graph.plot.ScatterPitchClassQuarterLength "music21.graph.plot.ScatterPitchClassQuarterLength") bases

* [`ScatterPitchSpaceQuarterLength`](#music21.graph.plot.ScatterPitchSpaceQuarterLength "music21.graph.plot.ScatterPitchSpaceQuarterLength")
* [`Scatter`](#music21.graph.plot.Scatter "music21.graph.plot.Scatter")
* [`GraphScatter`](moduleGraphPrimitives.html#music21.graph.primitives.GraphScatter "music21.graph.primitives.GraphScatter")
* [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph")
* [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`ScatterPitchClassQuarterLength`](#music21.graph.plot.ScatterPitchClassQuarterLength "music21.graph.plot.ScatterPitchClassQuarterLength") read-only properties

Read-only properties inherited from [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin"):

|  |  |  |
| --- | --- | --- |
| * [`allAxes`](#music21.graph.plot.PlotStreamMixin.allAxes "music21.graph.plot.PlotStreamMixin.allAxes") | * [`id`](#music21.graph.plot.PlotStreamMixin.id "music21.graph.plot.PlotStreamMixin.id") |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`ScatterPitchClassQuarterLength`](#music21.graph.plot.ScatterPitchClassQuarterLength "music21.graph.plot.ScatterPitchClassQuarterLength") read/write properties

Read/write properties inherited from [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph"):

|  |  |  |
| --- | --- | --- |
| * [`doneAction`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.doneAction "music21.graph.primitives.Graph.doneAction") |  |  |

[`ScatterPitchClassQuarterLength`](#music21.graph.plot.ScatterPitchClassQuarterLength "music21.graph.plot.ScatterPitchClassQuarterLength") methods

Methods inherited from [`GraphScatter`](moduleGraphPrimitives.html#music21.graph.primitives.GraphScatter "music21.graph.primitives.GraphScatter"):

|  |  |  |
| --- | --- | --- |
| * [`renderSubplot()`](moduleGraphPrimitives.html#music21.graph.primitives.GraphScatter.renderSubplot "music21.graph.primitives.GraphScatter.renderSubplot") |  |  |

Methods inherited from [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph"):

|  |  |  |
| --- | --- | --- |
| * [`applyFormatting()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyFormatting "music21.graph.primitives.Graph.applyFormatting") * [`applyFormattingToOneAxis()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyFormattingToOneAxis "music21.graph.primitives.Graph.applyFormattingToOneAxis") * [`applyGrid()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyGrid "music21.graph.primitives.Graph.applyGrid") * [`callDoneAction()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.callDoneAction "music21.graph.primitives.Graph.callDoneAction") * [`hideAxisSpines()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.hideAxisSpines "music21.graph.primitives.Graph.hideAxisSpines") | * [`nextColor()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.nextColor "music21.graph.primitives.Graph.nextColor") * [`process()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.process "music21.graph.primitives.Graph.process") * [`setAxisLabel()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setAxisLabel "music21.graph.primitives.Graph.setAxisLabel") * [`setAxisRange()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setAxisRange "music21.graph.primitives.Graph.setAxisRange") | * [`setIntegerTicksFromData()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setIntegerTicksFromData "music21.graph.primitives.Graph.setIntegerTicksFromData") * [`setTicks()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setTicks "music21.graph.primitives.Graph.setTicks") * [`show()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.show "music21.graph.primitives.Graph.show") * [`write()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.write "music21.graph.primitives.Graph.write") |

Methods inherited from [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin"):

|  |  |  |
| --- | --- | --- |
| * [`extractChordDataMultiAxis()`](#music21.graph.plot.PlotStreamMixin.extractChordDataMultiAxis "music21.graph.plot.PlotStreamMixin.extractChordDataMultiAxis") * [`extractChordDataOneAxis()`](#music21.graph.plot.PlotStreamMixin.extractChordDataOneAxis "music21.graph.plot.PlotStreamMixin.extractChordDataOneAxis") * [`extractData()`](#music21.graph.plot.PlotStreamMixin.extractData "music21.graph.plot.PlotStreamMixin.extractData") | * [`fillValueLists()`](#music21.graph.plot.PlotStreamMixin.fillValueLists "music21.graph.plot.PlotStreamMixin.fillValueLists") * [`postProcessData()`](#music21.graph.plot.PlotStreamMixin.postProcessData "music21.graph.plot.PlotStreamMixin.postProcessData") * [`postProcessElement()`](#music21.graph.plot.PlotStreamMixin.postProcessElement "music21.graph.plot.PlotStreamMixin.postProcessElement") | * [`processOneElement()`](#music21.graph.plot.PlotStreamMixin.processOneElement "music21.graph.plot.PlotStreamMixin.processOneElement") * [`run()`](#music21.graph.plot.PlotStreamMixin.run "music21.graph.plot.PlotStreamMixin.run") * [`setAxisKeywords()`](#music21.graph.plot.PlotStreamMixin.setAxisKeywords "music21.graph.plot.PlotStreamMixin.setAxisKeywords") |

## ScatterPitchClassOffset

class music21.graph.plot.ScatterPitchClassOffset(*streamObj=None*, *\*\*keywords*)[[source]](../_modules/music21/graph/plot.html#ScatterPitchClassOffset)
:   A scatter plot of pitch class and offset

    ```python
    >>> s = corpus.parse('bach/bwv57.8')
    >>> p = graph.plot.ScatterPitchClassOffset(s)
    >>> p.id
    'scatter-offset-pitchClass'
    >>> p.run()
    ```

    [![../_images/ScatterPitchClassOffset.png](../_images/ScatterPitchClassOffset.png)](../_images/ScatterPitchClassOffset.png)

[`ScatterPitchClassOffset`](#music21.graph.plot.ScatterPitchClassOffset "music21.graph.plot.ScatterPitchClassOffset") bases

* [`Scatter`](#music21.graph.plot.Scatter "music21.graph.plot.Scatter")
* [`GraphScatter`](moduleGraphPrimitives.html#music21.graph.primitives.GraphScatter "music21.graph.primitives.GraphScatter")
* [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph")
* [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`ScatterPitchClassOffset`](#music21.graph.plot.ScatterPitchClassOffset "music21.graph.plot.ScatterPitchClassOffset") read-only properties

Read-only properties inherited from [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin"):

|  |  |  |
| --- | --- | --- |
| * [`allAxes`](#music21.graph.plot.PlotStreamMixin.allAxes "music21.graph.plot.PlotStreamMixin.allAxes") | * [`id`](#music21.graph.plot.PlotStreamMixin.id "music21.graph.plot.PlotStreamMixin.id") |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`ScatterPitchClassOffset`](#music21.graph.plot.ScatterPitchClassOffset "music21.graph.plot.ScatterPitchClassOffset") read/write properties

Read/write properties inherited from [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph"):

|  |  |  |
| --- | --- | --- |
| * [`doneAction`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.doneAction "music21.graph.primitives.Graph.doneAction") |  |  |

[`ScatterPitchClassOffset`](#music21.graph.plot.ScatterPitchClassOffset "music21.graph.plot.ScatterPitchClassOffset") methods

Methods inherited from [`GraphScatter`](moduleGraphPrimitives.html#music21.graph.primitives.GraphScatter "music21.graph.primitives.GraphScatter"):

|  |  |  |
| --- | --- | --- |
| * [`renderSubplot()`](moduleGraphPrimitives.html#music21.graph.primitives.GraphScatter.renderSubplot "music21.graph.primitives.GraphScatter.renderSubplot") |  |  |

Methods inherited from [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph"):

|  |  |  |
| --- | --- | --- |
| * [`applyFormatting()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyFormatting "music21.graph.primitives.Graph.applyFormatting") * [`applyFormattingToOneAxis()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyFormattingToOneAxis "music21.graph.primitives.Graph.applyFormattingToOneAxis") * [`applyGrid()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyGrid "music21.graph.primitives.Graph.applyGrid") * [`callDoneAction()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.callDoneAction "music21.graph.primitives.Graph.callDoneAction") * [`hideAxisSpines()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.hideAxisSpines "music21.graph.primitives.Graph.hideAxisSpines") | * [`nextColor()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.nextColor "music21.graph.primitives.Graph.nextColor") * [`process()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.process "music21.graph.primitives.Graph.process") * [`setAxisLabel()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setAxisLabel "music21.graph.primitives.Graph.setAxisLabel") * [`setAxisRange()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setAxisRange "music21.graph.primitives.Graph.setAxisRange") | * [`setIntegerTicksFromData()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setIntegerTicksFromData "music21.graph.primitives.Graph.setIntegerTicksFromData") * [`setTicks()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setTicks "music21.graph.primitives.Graph.setTicks") * [`show()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.show "music21.graph.primitives.Graph.show") * [`write()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.write "music21.graph.primitives.Graph.write") |

Methods inherited from [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin"):

|  |  |  |
| --- | --- | --- |
| * [`extractChordDataMultiAxis()`](#music21.graph.plot.PlotStreamMixin.extractChordDataMultiAxis "music21.graph.plot.PlotStreamMixin.extractChordDataMultiAxis") * [`extractChordDataOneAxis()`](#music21.graph.plot.PlotStreamMixin.extractChordDataOneAxis "music21.graph.plot.PlotStreamMixin.extractChordDataOneAxis") * [`extractData()`](#music21.graph.plot.PlotStreamMixin.extractData "music21.graph.plot.PlotStreamMixin.extractData") | * [`fillValueLists()`](#music21.graph.plot.PlotStreamMixin.fillValueLists "music21.graph.plot.PlotStreamMixin.fillValueLists") * [`postProcessData()`](#music21.graph.plot.PlotStreamMixin.postProcessData "music21.graph.plot.PlotStreamMixin.postProcessData") * [`postProcessElement()`](#music21.graph.plot.PlotStreamMixin.postProcessElement "music21.graph.plot.PlotStreamMixin.postProcessElement") | * [`processOneElement()`](#music21.graph.plot.PlotStreamMixin.processOneElement "music21.graph.plot.PlotStreamMixin.processOneElement") * [`run()`](#music21.graph.plot.PlotStreamMixin.run "music21.graph.plot.PlotStreamMixin.run") * [`setAxisKeywords()`](#music21.graph.plot.PlotStreamMixin.setAxisKeywords "music21.graph.plot.PlotStreamMixin.setAxisKeywords") |

## ScatterPitchSpaceDynamicSymbol

class music21.graph.plot.ScatterPitchSpaceDynamicSymbol(*streamObj=None*, *\*\*keywords*)[[source]](../_modules/music21/graph/plot.html#ScatterPitchSpaceDynamicSymbol)
:   A graph of dynamics used by pitch space.

    ```python
    >>> s = corpus.parse('schumann_robert/opus41no1/movement2.xml')
    >>> p = graph.plot.ScatterPitchSpaceDynamicSymbol(s)
    >>> p.run()
    ```

    [![../_images/ScatterPitchSpaceDynamicSymbol.png](../_images/ScatterPitchSpaceDynamicSymbol.png)](../_images/ScatterPitchSpaceDynamicSymbol.png)

[`ScatterPitchSpaceDynamicSymbol`](#music21.graph.plot.ScatterPitchSpaceDynamicSymbol "music21.graph.plot.ScatterPitchSpaceDynamicSymbol") bases

* [`Scatter`](#music21.graph.plot.Scatter "music21.graph.plot.Scatter")
* [`GraphScatter`](moduleGraphPrimitives.html#music21.graph.primitives.GraphScatter "music21.graph.primitives.GraphScatter")
* [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph")
* [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`ScatterPitchSpaceDynamicSymbol`](#music21.graph.plot.ScatterPitchSpaceDynamicSymbol "music21.graph.plot.ScatterPitchSpaceDynamicSymbol") read-only properties

Read-only properties inherited from [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin"):

|  |  |  |
| --- | --- | --- |
| * [`allAxes`](#music21.graph.plot.PlotStreamMixin.allAxes "music21.graph.plot.PlotStreamMixin.allAxes") | * [`id`](#music21.graph.plot.PlotStreamMixin.id "music21.graph.plot.PlotStreamMixin.id") |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`ScatterPitchSpaceDynamicSymbol`](#music21.graph.plot.ScatterPitchSpaceDynamicSymbol "music21.graph.plot.ScatterPitchSpaceDynamicSymbol") read/write properties

Read/write properties inherited from [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph"):

|  |  |  |
| --- | --- | --- |
| * [`doneAction`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.doneAction "music21.graph.primitives.Graph.doneAction") |  |  |

[`ScatterPitchSpaceDynamicSymbol`](#music21.graph.plot.ScatterPitchSpaceDynamicSymbol "music21.graph.plot.ScatterPitchSpaceDynamicSymbol") methods

ScatterPitchSpaceDynamicSymbol.extractData()[[source]](../_modules/music21/graph/plot.html#ScatterPitchSpaceDynamicSymbol.extractData)

Methods inherited from [`GraphScatter`](moduleGraphPrimitives.html#music21.graph.primitives.GraphScatter "music21.graph.primitives.GraphScatter"):

|  |  |  |
| --- | --- | --- |
| * [`renderSubplot()`](moduleGraphPrimitives.html#music21.graph.primitives.GraphScatter.renderSubplot "music21.graph.primitives.GraphScatter.renderSubplot") |  |  |

Methods inherited from [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph"):

|  |  |  |
| --- | --- | --- |
| * [`applyFormatting()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyFormatting "music21.graph.primitives.Graph.applyFormatting") * [`applyFormattingToOneAxis()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyFormattingToOneAxis "music21.graph.primitives.Graph.applyFormattingToOneAxis") * [`applyGrid()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyGrid "music21.graph.primitives.Graph.applyGrid") * [`callDoneAction()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.callDoneAction "music21.graph.primitives.Graph.callDoneAction") * [`hideAxisSpines()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.hideAxisSpines "music21.graph.primitives.Graph.hideAxisSpines") | * [`nextColor()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.nextColor "music21.graph.primitives.Graph.nextColor") * [`process()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.process "music21.graph.primitives.Graph.process") * [`setAxisLabel()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setAxisLabel "music21.graph.primitives.Graph.setAxisLabel") * [`setAxisRange()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setAxisRange "music21.graph.primitives.Graph.setAxisRange") | * [`setIntegerTicksFromData()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setIntegerTicksFromData "music21.graph.primitives.Graph.setIntegerTicksFromData") * [`setTicks()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setTicks "music21.graph.primitives.Graph.setTicks") * [`show()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.show "music21.graph.primitives.Graph.show") * [`write()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.write "music21.graph.primitives.Graph.write") |

Methods inherited from [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin"):

|  |  |  |
| --- | --- | --- |
| * [`extractChordDataMultiAxis()`](#music21.graph.plot.PlotStreamMixin.extractChordDataMultiAxis "music21.graph.plot.PlotStreamMixin.extractChordDataMultiAxis") * [`extractChordDataOneAxis()`](#music21.graph.plot.PlotStreamMixin.extractChordDataOneAxis "music21.graph.plot.PlotStreamMixin.extractChordDataOneAxis") * [`fillValueLists()`](#music21.graph.plot.PlotStreamMixin.fillValueLists "music21.graph.plot.PlotStreamMixin.fillValueLists") | * [`postProcessData()`](#music21.graph.plot.PlotStreamMixin.postProcessData "music21.graph.plot.PlotStreamMixin.postProcessData") * [`postProcessElement()`](#music21.graph.plot.PlotStreamMixin.postProcessElement "music21.graph.plot.PlotStreamMixin.postProcessElement") * [`processOneElement()`](#music21.graph.plot.PlotStreamMixin.processOneElement "music21.graph.plot.PlotStreamMixin.processOneElement") | * [`run()`](#music21.graph.plot.PlotStreamMixin.run "music21.graph.plot.PlotStreamMixin.run") * [`setAxisKeywords()`](#music21.graph.plot.PlotStreamMixin.setAxisKeywords "music21.graph.plot.PlotStreamMixin.setAxisKeywords") |

## HorizontalBarPitchSpaceOffset

class music21.graph.plot.HorizontalBarPitchSpaceOffset(*streamObj=None*, *\**, *colorByPart=False*, *\*\*keywords*)[[source]](../_modules/music21/graph/plot.html#HorizontalBarPitchSpaceOffset)
:   A graph of events, sorted by pitch space, over time, generally called
    a “piano roll”.

    ```python
    >>> s = corpus.parse('bach/bwv57.8')
    >>> p = graph.plot.HorizontalBarPitchSpaceOffset(s)
    >>> p.run()  # with defaults and proper configuration, will open graph
    ```

    [![../_images/HorizontalBarPitchSpaceOffset.png](../_images/HorizontalBarPitchSpaceOffset.png)](../_images/HorizontalBarPitchSpaceOffset.png)

[`HorizontalBarPitchSpaceOffset`](#music21.graph.plot.HorizontalBarPitchSpaceOffset "music21.graph.plot.HorizontalBarPitchSpaceOffset") bases

* [`HorizontalBar`](#music21.graph.plot.HorizontalBar "music21.graph.plot.HorizontalBar")
* [`GraphHorizontalBar`](moduleGraphPrimitives.html#music21.graph.primitives.GraphHorizontalBar "music21.graph.primitives.GraphHorizontalBar")
* [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph")
* [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`HorizontalBarPitchSpaceOffset`](#music21.graph.plot.HorizontalBarPitchSpaceOffset "music21.graph.plot.HorizontalBarPitchSpaceOffset") read-only properties

Read-only properties inherited from [`GraphHorizontalBar`](moduleGraphPrimitives.html#music21.graph.primitives.GraphHorizontalBar "music21.graph.primitives.GraphHorizontalBar"):

|  |  |  |
| --- | --- | --- |
| * [`barHeight`](moduleGraphPrimitives.html#music21.graph.primitives.GraphHorizontalBar.barHeight "music21.graph.primitives.GraphHorizontalBar.barHeight") |  |  |

Read-only properties inherited from [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin"):

|  |  |  |
| --- | --- | --- |
| * [`allAxes`](#music21.graph.plot.PlotStreamMixin.allAxes "music21.graph.plot.PlotStreamMixin.allAxes") | * [`id`](#music21.graph.plot.PlotStreamMixin.id "music21.graph.plot.PlotStreamMixin.id") |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`HorizontalBarPitchSpaceOffset`](#music21.graph.plot.HorizontalBarPitchSpaceOffset "music21.graph.plot.HorizontalBarPitchSpaceOffset") read/write properties

Read/write properties inherited from [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph"):

|  |  |  |
| --- | --- | --- |
| * [`doneAction`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.doneAction "music21.graph.primitives.Graph.doneAction") |  |  |

[`HorizontalBarPitchSpaceOffset`](#music21.graph.plot.HorizontalBarPitchSpaceOffset "music21.graph.plot.HorizontalBarPitchSpaceOffset") methods

Methods inherited from [`HorizontalBar`](#music21.graph.plot.HorizontalBar "music21.graph.plot.HorizontalBar"):

|  |  |  |
| --- | --- | --- |
| * [`assignColorsToParts()`](#music21.graph.plot.HorizontalBar.assignColorsToParts "music21.graph.plot.HorizontalBar.assignColorsToParts") * [`postProcessData()`](#music21.graph.plot.HorizontalBar.postProcessData "music21.graph.plot.HorizontalBar.postProcessData") | * [`postProcessElement()`](#music21.graph.plot.HorizontalBar.postProcessElement "music21.graph.plot.HorizontalBar.postProcessElement") | * [`run()`](#music21.graph.plot.HorizontalBar.run "music21.graph.plot.HorizontalBar.run") |

Methods inherited from [`GraphHorizontalBar`](moduleGraphPrimitives.html#music21.graph.primitives.GraphHorizontalBar "music21.graph.primitives.GraphHorizontalBar"):

|  |  |  |
| --- | --- | --- |
| * [`renderSubplot()`](moduleGraphPrimitives.html#music21.graph.primitives.GraphHorizontalBar.renderSubplot "music21.graph.primitives.GraphHorizontalBar.renderSubplot") |  |  |

Methods inherited from [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph"):

|  |  |  |
| --- | --- | --- |
| * [`applyFormatting()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyFormatting "music21.graph.primitives.Graph.applyFormatting") * [`applyFormattingToOneAxis()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyFormattingToOneAxis "music21.graph.primitives.Graph.applyFormattingToOneAxis") * [`applyGrid()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyGrid "music21.graph.primitives.Graph.applyGrid") * [`callDoneAction()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.callDoneAction "music21.graph.primitives.Graph.callDoneAction") * [`hideAxisSpines()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.hideAxisSpines "music21.graph.primitives.Graph.hideAxisSpines") | * [`nextColor()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.nextColor "music21.graph.primitives.Graph.nextColor") * [`process()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.process "music21.graph.primitives.Graph.process") * [`setAxisLabel()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setAxisLabel "music21.graph.primitives.Graph.setAxisLabel") * [`setAxisRange()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setAxisRange "music21.graph.primitives.Graph.setAxisRange") | * [`setIntegerTicksFromData()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setIntegerTicksFromData "music21.graph.primitives.Graph.setIntegerTicksFromData") * [`setTicks()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setTicks "music21.graph.primitives.Graph.setTicks") * [`show()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.show "music21.graph.primitives.Graph.show") * [`write()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.write "music21.graph.primitives.Graph.write") |

Methods inherited from [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin"):

|  |  |  |
| --- | --- | --- |
| * [`extractChordDataMultiAxis()`](#music21.graph.plot.PlotStreamMixin.extractChordDataMultiAxis "music21.graph.plot.PlotStreamMixin.extractChordDataMultiAxis") * [`extractChordDataOneAxis()`](#music21.graph.plot.PlotStreamMixin.extractChordDataOneAxis "music21.graph.plot.PlotStreamMixin.extractChordDataOneAxis") | * [`extractData()`](#music21.graph.plot.PlotStreamMixin.extractData "music21.graph.plot.PlotStreamMixin.extractData") * [`fillValueLists()`](#music21.graph.plot.PlotStreamMixin.fillValueLists "music21.graph.plot.PlotStreamMixin.fillValueLists") | * [`processOneElement()`](#music21.graph.plot.PlotStreamMixin.processOneElement "music21.graph.plot.PlotStreamMixin.processOneElement") * [`setAxisKeywords()`](#music21.graph.plot.PlotStreamMixin.setAxisKeywords "music21.graph.plot.PlotStreamMixin.setAxisKeywords") |

[`HorizontalBarPitchSpaceOffset`](#music21.graph.plot.HorizontalBarPitchSpaceOffset "music21.graph.plot.HorizontalBarPitchSpaceOffset") instance variables

Instance variables inherited from [`GraphHorizontalBar`](moduleGraphPrimitives.html#music21.graph.primitives.GraphHorizontalBar "music21.graph.primitives.GraphHorizontalBar"):

|  |  |  |
| --- | --- | --- |
| * [`barSpace`](moduleGraphPrimitives.html#music21.graph.primitives.GraphHorizontalBar.barSpace "music21.graph.primitives.GraphHorizontalBar.barSpace") | * [`margin`](moduleGraphPrimitives.html#music21.graph.primitives.GraphHorizontalBar.margin "music21.graph.primitives.GraphHorizontalBar.margin") |  |

## HorizontalBarPitchClassOffset

class music21.graph.plot.HorizontalBarPitchClassOffset(*streamObj=None*, *\**, *colorByPart=False*, *\*\*keywords*)[[source]](../_modules/music21/graph/plot.html#HorizontalBarPitchClassOffset)
:   A graph of events, sorted by pitch class, over time.

    ```python
    >>> s = corpus.parse('bach/bwv57.8')
    >>> p = graph.plot.HorizontalBarPitchClassOffset(s)
    >>> p.run()  # with defaults and proper configuration, will open graph
    ```

    [![../_images/HorizontalBarPitchClassOffset.png](../_images/HorizontalBarPitchClassOffset.png)](../_images/HorizontalBarPitchClassOffset.png)

[`HorizontalBarPitchClassOffset`](#music21.graph.plot.HorizontalBarPitchClassOffset "music21.graph.plot.HorizontalBarPitchClassOffset") bases

* [`HorizontalBar`](#music21.graph.plot.HorizontalBar "music21.graph.plot.HorizontalBar")
* [`GraphHorizontalBar`](moduleGraphPrimitives.html#music21.graph.primitives.GraphHorizontalBar "music21.graph.primitives.GraphHorizontalBar")
* [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph")
* [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`HorizontalBarPitchClassOffset`](#music21.graph.plot.HorizontalBarPitchClassOffset "music21.graph.plot.HorizontalBarPitchClassOffset") read-only properties

Read-only properties inherited from [`GraphHorizontalBar`](moduleGraphPrimitives.html#music21.graph.primitives.GraphHorizontalBar "music21.graph.primitives.GraphHorizontalBar"):

|  |  |  |
| --- | --- | --- |
| * [`barHeight`](moduleGraphPrimitives.html#music21.graph.primitives.GraphHorizontalBar.barHeight "music21.graph.primitives.GraphHorizontalBar.barHeight") |  |  |

Read-only properties inherited from [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin"):

|  |  |  |
| --- | --- | --- |
| * [`allAxes`](#music21.graph.plot.PlotStreamMixin.allAxes "music21.graph.plot.PlotStreamMixin.allAxes") | * [`id`](#music21.graph.plot.PlotStreamMixin.id "music21.graph.plot.PlotStreamMixin.id") |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`HorizontalBarPitchClassOffset`](#music21.graph.plot.HorizontalBarPitchClassOffset "music21.graph.plot.HorizontalBarPitchClassOffset") read/write properties

Read/write properties inherited from [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph"):

|  |  |  |
| --- | --- | --- |
| * [`doneAction`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.doneAction "music21.graph.primitives.Graph.doneAction") |  |  |

[`HorizontalBarPitchClassOffset`](#music21.graph.plot.HorizontalBarPitchClassOffset "music21.graph.plot.HorizontalBarPitchClassOffset") methods

Methods inherited from [`HorizontalBar`](#music21.graph.plot.HorizontalBar "music21.graph.plot.HorizontalBar"):

|  |  |  |
| --- | --- | --- |
| * [`assignColorsToParts()`](#music21.graph.plot.HorizontalBar.assignColorsToParts "music21.graph.plot.HorizontalBar.assignColorsToParts") * [`postProcessData()`](#music21.graph.plot.HorizontalBar.postProcessData "music21.graph.plot.HorizontalBar.postProcessData") | * [`postProcessElement()`](#music21.graph.plot.HorizontalBar.postProcessElement "music21.graph.plot.HorizontalBar.postProcessElement") | * [`run()`](#music21.graph.plot.HorizontalBar.run "music21.graph.plot.HorizontalBar.run") |

Methods inherited from [`GraphHorizontalBar`](moduleGraphPrimitives.html#music21.graph.primitives.GraphHorizontalBar "music21.graph.primitives.GraphHorizontalBar"):

|  |  |  |
| --- | --- | --- |
| * [`renderSubplot()`](moduleGraphPrimitives.html#music21.graph.primitives.GraphHorizontalBar.renderSubplot "music21.graph.primitives.GraphHorizontalBar.renderSubplot") |  |  |

Methods inherited from [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph"):

|  |  |  |
| --- | --- | --- |
| * [`applyFormatting()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyFormatting "music21.graph.primitives.Graph.applyFormatting") * [`applyFormattingToOneAxis()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyFormattingToOneAxis "music21.graph.primitives.Graph.applyFormattingToOneAxis") * [`applyGrid()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyGrid "music21.graph.primitives.Graph.applyGrid") * [`callDoneAction()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.callDoneAction "music21.graph.primitives.Graph.callDoneAction") * [`hideAxisSpines()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.hideAxisSpines "music21.graph.primitives.Graph.hideAxisSpines") | * [`nextColor()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.nextColor "music21.graph.primitives.Graph.nextColor") * [`process()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.process "music21.graph.primitives.Graph.process") * [`setAxisLabel()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setAxisLabel "music21.graph.primitives.Graph.setAxisLabel") * [`setAxisRange()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setAxisRange "music21.graph.primitives.Graph.setAxisRange") | * [`setIntegerTicksFromData()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setIntegerTicksFromData "music21.graph.primitives.Graph.setIntegerTicksFromData") * [`setTicks()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setTicks "music21.graph.primitives.Graph.setTicks") * [`show()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.show "music21.graph.primitives.Graph.show") * [`write()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.write "music21.graph.primitives.Graph.write") |

Methods inherited from [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin"):

|  |  |  |
| --- | --- | --- |
| * [`extractChordDataMultiAxis()`](#music21.graph.plot.PlotStreamMixin.extractChordDataMultiAxis "music21.graph.plot.PlotStreamMixin.extractChordDataMultiAxis") * [`extractChordDataOneAxis()`](#music21.graph.plot.PlotStreamMixin.extractChordDataOneAxis "music21.graph.plot.PlotStreamMixin.extractChordDataOneAxis") | * [`extractData()`](#music21.graph.plot.PlotStreamMixin.extractData "music21.graph.plot.PlotStreamMixin.extractData") * [`fillValueLists()`](#music21.graph.plot.PlotStreamMixin.fillValueLists "music21.graph.plot.PlotStreamMixin.fillValueLists") | * [`processOneElement()`](#music21.graph.plot.PlotStreamMixin.processOneElement "music21.graph.plot.PlotStreamMixin.processOneElement") * [`setAxisKeywords()`](#music21.graph.plot.PlotStreamMixin.setAxisKeywords "music21.graph.plot.PlotStreamMixin.setAxisKeywords") |

[`HorizontalBarPitchClassOffset`](#music21.graph.plot.HorizontalBarPitchClassOffset "music21.graph.plot.HorizontalBarPitchClassOffset") instance variables

Instance variables inherited from [`GraphHorizontalBar`](moduleGraphPrimitives.html#music21.graph.primitives.GraphHorizontalBar "music21.graph.primitives.GraphHorizontalBar"):

|  |  |  |
| --- | --- | --- |
| * [`barSpace`](moduleGraphPrimitives.html#music21.graph.primitives.GraphHorizontalBar.barSpace "music21.graph.primitives.GraphHorizontalBar.barSpace") | * [`margin`](moduleGraphPrimitives.html#music21.graph.primitives.GraphHorizontalBar.margin "music21.graph.primitives.GraphHorizontalBar.margin") |  |

## Dolan

class music21.graph.plot.Dolan(*streamObj=None*, *\*\*keywords*)[[source]](../_modules/music21/graph/plot.html#Dolan)
:   A graph of the activity of a parameter of a part (or a group of parts) over time.
    The default parameter graphed is Dynamics. Dynamics are assumed to extend activity
    to the next change in dynamics.

    Numerous parameters can be configured based on functionality encoded in
    the [`PartReduction`](moduleAnalysisReduction.html#music21.analysis.reduction.PartReduction "music21.analysis.reduction.PartReduction") object.

    If the fillByMeasure parameter is True, and if measures are available, each part
    will segment by Measure divisions, and look for the target activity only once per
    Measure. If more than one target is found in the Measure, values will be averaged.
    If fillByMeasure is False, the part will be segmented by each Note.

    The segmentByTarget parameter is True, segments, which may be Notes or Measures,
    will be divided if necessary to show changes that occur over the duration of the
    segment by a target object.

    If the normalizeByPart parameter is True, each part will be normalized within the
    range only of that part. If False, all parts will be normalized by the max of all parts.
    The default is True.

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> dyn = ['p', 'mf', 'f', 'ff', 'mp', 'fff', 'ppp']
    >>> i = 0
    >>> for p in s.parts:
    ...     for m in p.getElementsByClass(stream.Measure):
    ...         m.insert(0, dynamics.Dynamic(dyn[i % len(dyn)]))
    ...         i += 1
    ...
    >>> s.plot('dolan', fillByMeasure=True, segmentByTarget=True)
    ```

    [![../_images/Dolan.png](../_images/Dolan.png)](../_images/Dolan.png)

[`Dolan`](#music21.graph.plot.Dolan "music21.graph.plot.Dolan") bases

* [`HorizontalBarWeighted`](#music21.graph.plot.HorizontalBarWeighted "music21.graph.plot.HorizontalBarWeighted")
* [`GraphHorizontalBarWeighted`](moduleGraphPrimitives.html#music21.graph.primitives.GraphHorizontalBarWeighted "music21.graph.primitives.GraphHorizontalBarWeighted")
* [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph")
* [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`Dolan`](#music21.graph.plot.Dolan "music21.graph.plot.Dolan") read-only properties

Read-only properties inherited from [`GraphHorizontalBarWeighted`](moduleGraphPrimitives.html#music21.graph.primitives.GraphHorizontalBarWeighted "music21.graph.primitives.GraphHorizontalBarWeighted"):

|  |  |  |
| --- | --- | --- |
| * [`barHeight`](moduleGraphPrimitives.html#music21.graph.primitives.GraphHorizontalBarWeighted.barHeight "music21.graph.primitives.GraphHorizontalBarWeighted.barHeight") |  |  |

Read-only properties inherited from [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin"):

|  |  |  |
| --- | --- | --- |
| * [`allAxes`](#music21.graph.plot.PlotStreamMixin.allAxes "music21.graph.plot.PlotStreamMixin.allAxes") | * [`id`](#music21.graph.plot.PlotStreamMixin.id "music21.graph.plot.PlotStreamMixin.id") |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`Dolan`](#music21.graph.plot.Dolan "music21.graph.plot.Dolan") read/write properties

Read/write properties inherited from [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph"):

|  |  |  |
| --- | --- | --- |
| * [`doneAction`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.doneAction "music21.graph.primitives.Graph.doneAction") |  |  |

[`Dolan`](#music21.graph.plot.Dolan "music21.graph.plot.Dolan") methods

Methods inherited from [`HorizontalBarWeighted`](#music21.graph.plot.HorizontalBarWeighted "music21.graph.plot.HorizontalBarWeighted"):

|  |  |  |
| --- | --- | --- |
| * [`extractData()`](#music21.graph.plot.HorizontalBarWeighted.extractData "music21.graph.plot.HorizontalBarWeighted.extractData") |  |  |

Methods inherited from [`GraphHorizontalBarWeighted`](moduleGraphPrimitives.html#music21.graph.primitives.GraphHorizontalBarWeighted "music21.graph.primitives.GraphHorizontalBarWeighted"):

|  |  |  |
| --- | --- | --- |
| * [`renderSubplot()`](moduleGraphPrimitives.html#music21.graph.primitives.GraphHorizontalBarWeighted.renderSubplot "music21.graph.primitives.GraphHorizontalBarWeighted.renderSubplot") |  |  |

Methods inherited from [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph"):

|  |  |  |
| --- | --- | --- |
| * [`applyFormatting()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyFormatting "music21.graph.primitives.Graph.applyFormatting") * [`applyFormattingToOneAxis()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyFormattingToOneAxis "music21.graph.primitives.Graph.applyFormattingToOneAxis") * [`applyGrid()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyGrid "music21.graph.primitives.Graph.applyGrid") * [`callDoneAction()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.callDoneAction "music21.graph.primitives.Graph.callDoneAction") * [`hideAxisSpines()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.hideAxisSpines "music21.graph.primitives.Graph.hideAxisSpines") | * [`nextColor()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.nextColor "music21.graph.primitives.Graph.nextColor") * [`process()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.process "music21.graph.primitives.Graph.process") * [`setAxisLabel()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setAxisLabel "music21.graph.primitives.Graph.setAxisLabel") * [`setAxisRange()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setAxisRange "music21.graph.primitives.Graph.setAxisRange") | * [`setIntegerTicksFromData()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setIntegerTicksFromData "music21.graph.primitives.Graph.setIntegerTicksFromData") * [`setTicks()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setTicks "music21.graph.primitives.Graph.setTicks") * [`show()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.show "music21.graph.primitives.Graph.show") * [`write()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.write "music21.graph.primitives.Graph.write") |

Methods inherited from [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin"):

|  |  |  |
| --- | --- | --- |
| * [`extractChordDataMultiAxis()`](#music21.graph.plot.PlotStreamMixin.extractChordDataMultiAxis "music21.graph.plot.PlotStreamMixin.extractChordDataMultiAxis") * [`extractChordDataOneAxis()`](#music21.graph.plot.PlotStreamMixin.extractChordDataOneAxis "music21.graph.plot.PlotStreamMixin.extractChordDataOneAxis") * [`fillValueLists()`](#music21.graph.plot.PlotStreamMixin.fillValueLists "music21.graph.plot.PlotStreamMixin.fillValueLists") | * [`postProcessData()`](#music21.graph.plot.PlotStreamMixin.postProcessData "music21.graph.plot.PlotStreamMixin.postProcessData") * [`postProcessElement()`](#music21.graph.plot.PlotStreamMixin.postProcessElement "music21.graph.plot.PlotStreamMixin.postProcessElement") * [`processOneElement()`](#music21.graph.plot.PlotStreamMixin.processOneElement "music21.graph.plot.PlotStreamMixin.processOneElement") | * [`run()`](#music21.graph.plot.PlotStreamMixin.run "music21.graph.plot.PlotStreamMixin.run") * [`setAxisKeywords()`](#music21.graph.plot.PlotStreamMixin.setAxisKeywords "music21.graph.plot.PlotStreamMixin.setAxisKeywords") |

[`Dolan`](#music21.graph.plot.Dolan "music21.graph.plot.Dolan") instance variables

Instance variables inherited from [`GraphHorizontalBarWeighted`](moduleGraphPrimitives.html#music21.graph.primitives.GraphHorizontalBarWeighted "music21.graph.primitives.GraphHorizontalBarWeighted"):

|  |  |  |
| --- | --- | --- |
| * [`barSpace`](moduleGraphPrimitives.html#music21.graph.primitives.GraphHorizontalBarWeighted.barSpace "music21.graph.primitives.GraphHorizontalBarWeighted.barSpace") | * [`margin`](moduleGraphPrimitives.html#music21.graph.primitives.GraphHorizontalBarWeighted.margin "music21.graph.primitives.GraphHorizontalBarWeighted.margin") |  |

## ScatterWeightedPitchSpaceQuarterLength

class music21.graph.plot.ScatterWeightedPitchSpaceQuarterLength(*streamObj=None*, *\*\*keywords*)[[source]](../_modules/music21/graph/plot.html#ScatterWeightedPitchSpaceQuarterLength)
:   A graph of event, sorted by pitch, over time.

    ```python
    >>> s = corpus.parse('bach/bwv57.8')
    >>> p = graph.plot.ScatterWeightedPitchSpaceQuarterLength(s)
    >>> p.run()  # with defaults and proper configuration, will open graph
    ```

    [![../_images/ScatterWeightedPitchSpaceQuarterLength.png](../_images/ScatterWeightedPitchSpaceQuarterLength.png)](../_images/ScatterWeightedPitchSpaceQuarterLength.png)

[`ScatterWeightedPitchSpaceQuarterLength`](#music21.graph.plot.ScatterWeightedPitchSpaceQuarterLength "music21.graph.plot.ScatterWeightedPitchSpaceQuarterLength") bases

* [`ScatterWeighted`](#music21.graph.plot.ScatterWeighted "music21.graph.plot.ScatterWeighted")
* [`GraphScatterWeighted`](moduleGraphPrimitives.html#music21.graph.primitives.GraphScatterWeighted "music21.graph.primitives.GraphScatterWeighted")
* [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph")
* [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`ScatterWeightedPitchSpaceQuarterLength`](#music21.graph.plot.ScatterWeightedPitchSpaceQuarterLength "music21.graph.plot.ScatterWeightedPitchSpaceQuarterLength") read-only properties

Read-only properties inherited from [`GraphScatterWeighted`](moduleGraphPrimitives.html#music21.graph.primitives.GraphScatterWeighted "music21.graph.primitives.GraphScatterWeighted"):

|  |  |  |
| --- | --- | --- |
| * [`rangeDiameter`](moduleGraphPrimitives.html#music21.graph.primitives.GraphScatterWeighted.rangeDiameter "music21.graph.primitives.GraphScatterWeighted.rangeDiameter") |  |  |

Read-only properties inherited from [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin"):

|  |  |  |
| --- | --- | --- |
| * [`allAxes`](#music21.graph.plot.PlotStreamMixin.allAxes "music21.graph.plot.PlotStreamMixin.allAxes") | * [`id`](#music21.graph.plot.PlotStreamMixin.id "music21.graph.plot.PlotStreamMixin.id") |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`ScatterWeightedPitchSpaceQuarterLength`](#music21.graph.plot.ScatterWeightedPitchSpaceQuarterLength "music21.graph.plot.ScatterWeightedPitchSpaceQuarterLength") read/write properties

Read/write properties inherited from [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph"):

|  |  |  |
| --- | --- | --- |
| * [`doneAction`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.doneAction "music21.graph.primitives.Graph.doneAction") |  |  |

[`ScatterWeightedPitchSpaceQuarterLength`](#music21.graph.plot.ScatterWeightedPitchSpaceQuarterLength "music21.graph.plot.ScatterWeightedPitchSpaceQuarterLength") methods

Methods inherited from [`GraphScatterWeighted`](moduleGraphPrimitives.html#music21.graph.primitives.GraphScatterWeighted "music21.graph.primitives.GraphScatterWeighted"):

|  |  |  |
| --- | --- | --- |
| * [`renderSubplot()`](moduleGraphPrimitives.html#music21.graph.primitives.GraphScatterWeighted.renderSubplot "music21.graph.primitives.GraphScatterWeighted.renderSubplot") |  |  |

Methods inherited from [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph"):

|  |  |  |
| --- | --- | --- |
| * [`applyFormatting()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyFormatting "music21.graph.primitives.Graph.applyFormatting") * [`applyFormattingToOneAxis()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyFormattingToOneAxis "music21.graph.primitives.Graph.applyFormattingToOneAxis") * [`applyGrid()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyGrid "music21.graph.primitives.Graph.applyGrid") * [`callDoneAction()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.callDoneAction "music21.graph.primitives.Graph.callDoneAction") * [`hideAxisSpines()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.hideAxisSpines "music21.graph.primitives.Graph.hideAxisSpines") | * [`nextColor()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.nextColor "music21.graph.primitives.Graph.nextColor") * [`process()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.process "music21.graph.primitives.Graph.process") * [`setAxisLabel()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setAxisLabel "music21.graph.primitives.Graph.setAxisLabel") * [`setAxisRange()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setAxisRange "music21.graph.primitives.Graph.setAxisRange") | * [`setIntegerTicksFromData()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setIntegerTicksFromData "music21.graph.primitives.Graph.setIntegerTicksFromData") * [`setTicks()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setTicks "music21.graph.primitives.Graph.setTicks") * [`show()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.show "music21.graph.primitives.Graph.show") * [`write()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.write "music21.graph.primitives.Graph.write") |

Methods inherited from [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin"):

|  |  |  |
| --- | --- | --- |
| * [`extractChordDataMultiAxis()`](#music21.graph.plot.PlotStreamMixin.extractChordDataMultiAxis "music21.graph.plot.PlotStreamMixin.extractChordDataMultiAxis") * [`extractChordDataOneAxis()`](#music21.graph.plot.PlotStreamMixin.extractChordDataOneAxis "music21.graph.plot.PlotStreamMixin.extractChordDataOneAxis") * [`extractData()`](#music21.graph.plot.PlotStreamMixin.extractData "music21.graph.plot.PlotStreamMixin.extractData") | * [`fillValueLists()`](#music21.graph.plot.PlotStreamMixin.fillValueLists "music21.graph.plot.PlotStreamMixin.fillValueLists") * [`postProcessData()`](#music21.graph.plot.PlotStreamMixin.postProcessData "music21.graph.plot.PlotStreamMixin.postProcessData") * [`postProcessElement()`](#music21.graph.plot.PlotStreamMixin.postProcessElement "music21.graph.plot.PlotStreamMixin.postProcessElement") | * [`processOneElement()`](#music21.graph.plot.PlotStreamMixin.processOneElement "music21.graph.plot.PlotStreamMixin.processOneElement") * [`run()`](#music21.graph.plot.PlotStreamMixin.run "music21.graph.plot.PlotStreamMixin.run") * [`setAxisKeywords()`](#music21.graph.plot.PlotStreamMixin.setAxisKeywords "music21.graph.plot.PlotStreamMixin.setAxisKeywords") |

[`ScatterWeightedPitchSpaceQuarterLength`](#music21.graph.plot.ScatterWeightedPitchSpaceQuarterLength "music21.graph.plot.ScatterWeightedPitchSpaceQuarterLength") instance variables

Instance variables inherited from [`GraphScatterWeighted`](moduleGraphPrimitives.html#music21.graph.primitives.GraphScatterWeighted "music21.graph.primitives.GraphScatterWeighted"):

|  |  |  |
| --- | --- | --- |
| * [`maxDiameter`](moduleGraphPrimitives.html#music21.graph.primitives.GraphScatterWeighted.maxDiameter "music21.graph.primitives.GraphScatterWeighted.maxDiameter") | * [`minDiameter`](moduleGraphPrimitives.html#music21.graph.primitives.GraphScatterWeighted.minDiameter "music21.graph.primitives.GraphScatterWeighted.minDiameter") |  |

## ScatterWeightedPitchClassQuarterLength

class music21.graph.plot.ScatterWeightedPitchClassQuarterLength(*streamObj=None*, *\*\*keywords*)[[source]](../_modules/music21/graph/plot.html#ScatterWeightedPitchClassQuarterLength)
:   A graph of event, sorted by pitch class, over time.

    ```python
    >>> s = corpus.parse('bach/bwv57.8')
    >>> p = graph.plot.ScatterWeightedPitchClassQuarterLength(s)
    >>> p.run()  # with defaults and proper configuration, will open graph
    ```

    [![../_images/ScatterWeightedPitchClassQuarterLength.png](../_images/ScatterWeightedPitchClassQuarterLength.png)](../_images/ScatterWeightedPitchClassQuarterLength.png)

[`ScatterWeightedPitchClassQuarterLength`](#music21.graph.plot.ScatterWeightedPitchClassQuarterLength "music21.graph.plot.ScatterWeightedPitchClassQuarterLength") bases

* [`ScatterWeighted`](#music21.graph.plot.ScatterWeighted "music21.graph.plot.ScatterWeighted")
* [`GraphScatterWeighted`](moduleGraphPrimitives.html#music21.graph.primitives.GraphScatterWeighted "music21.graph.primitives.GraphScatterWeighted")
* [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph")
* [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`ScatterWeightedPitchClassQuarterLength`](#music21.graph.plot.ScatterWeightedPitchClassQuarterLength "music21.graph.plot.ScatterWeightedPitchClassQuarterLength") read-only properties

Read-only properties inherited from [`GraphScatterWeighted`](moduleGraphPrimitives.html#music21.graph.primitives.GraphScatterWeighted "music21.graph.primitives.GraphScatterWeighted"):

|  |  |  |
| --- | --- | --- |
| * [`rangeDiameter`](moduleGraphPrimitives.html#music21.graph.primitives.GraphScatterWeighted.rangeDiameter "music21.graph.primitives.GraphScatterWeighted.rangeDiameter") |  |  |

Read-only properties inherited from [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin"):

|  |  |  |
| --- | --- | --- |
| * [`allAxes`](#music21.graph.plot.PlotStreamMixin.allAxes "music21.graph.plot.PlotStreamMixin.allAxes") | * [`id`](#music21.graph.plot.PlotStreamMixin.id "music21.graph.plot.PlotStreamMixin.id") |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`ScatterWeightedPitchClassQuarterLength`](#music21.graph.plot.ScatterWeightedPitchClassQuarterLength "music21.graph.plot.ScatterWeightedPitchClassQuarterLength") read/write properties

Read/write properties inherited from [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph"):

|  |  |  |
| --- | --- | --- |
| * [`doneAction`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.doneAction "music21.graph.primitives.Graph.doneAction") |  |  |

[`ScatterWeightedPitchClassQuarterLength`](#music21.graph.plot.ScatterWeightedPitchClassQuarterLength "music21.graph.plot.ScatterWeightedPitchClassQuarterLength") methods

Methods inherited from [`GraphScatterWeighted`](moduleGraphPrimitives.html#music21.graph.primitives.GraphScatterWeighted "music21.graph.primitives.GraphScatterWeighted"):

|  |  |  |
| --- | --- | --- |
| * [`renderSubplot()`](moduleGraphPrimitives.html#music21.graph.primitives.GraphScatterWeighted.renderSubplot "music21.graph.primitives.GraphScatterWeighted.renderSubplot") |  |  |

Methods inherited from [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph"):

|  |  |  |
| --- | --- | --- |
| * [`applyFormatting()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyFormatting "music21.graph.primitives.Graph.applyFormatting") * [`applyFormattingToOneAxis()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyFormattingToOneAxis "music21.graph.primitives.Graph.applyFormattingToOneAxis") * [`applyGrid()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyGrid "music21.graph.primitives.Graph.applyGrid") * [`callDoneAction()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.callDoneAction "music21.graph.primitives.Graph.callDoneAction") * [`hideAxisSpines()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.hideAxisSpines "music21.graph.primitives.Graph.hideAxisSpines") | * [`nextColor()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.nextColor "music21.graph.primitives.Graph.nextColor") * [`process()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.process "music21.graph.primitives.Graph.process") * [`setAxisLabel()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setAxisLabel "music21.graph.primitives.Graph.setAxisLabel") * [`setAxisRange()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setAxisRange "music21.graph.primitives.Graph.setAxisRange") | * [`setIntegerTicksFromData()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setIntegerTicksFromData "music21.graph.primitives.Graph.setIntegerTicksFromData") * [`setTicks()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setTicks "music21.graph.primitives.Graph.setTicks") * [`show()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.show "music21.graph.primitives.Graph.show") * [`write()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.write "music21.graph.primitives.Graph.write") |

Methods inherited from [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin"):

|  |  |  |
| --- | --- | --- |
| * [`extractChordDataMultiAxis()`](#music21.graph.plot.PlotStreamMixin.extractChordDataMultiAxis "music21.graph.plot.PlotStreamMixin.extractChordDataMultiAxis") * [`extractChordDataOneAxis()`](#music21.graph.plot.PlotStreamMixin.extractChordDataOneAxis "music21.graph.plot.PlotStreamMixin.extractChordDataOneAxis") * [`extractData()`](#music21.graph.plot.PlotStreamMixin.extractData "music21.graph.plot.PlotStreamMixin.extractData") | * [`fillValueLists()`](#music21.graph.plot.PlotStreamMixin.fillValueLists "music21.graph.plot.PlotStreamMixin.fillValueLists") * [`postProcessData()`](#music21.graph.plot.PlotStreamMixin.postProcessData "music21.graph.plot.PlotStreamMixin.postProcessData") * [`postProcessElement()`](#music21.graph.plot.PlotStreamMixin.postProcessElement "music21.graph.plot.PlotStreamMixin.postProcessElement") | * [`processOneElement()`](#music21.graph.plot.PlotStreamMixin.processOneElement "music21.graph.plot.PlotStreamMixin.processOneElement") * [`run()`](#music21.graph.plot.PlotStreamMixin.run "music21.graph.plot.PlotStreamMixin.run") * [`setAxisKeywords()`](#music21.graph.plot.PlotStreamMixin.setAxisKeywords "music21.graph.plot.PlotStreamMixin.setAxisKeywords") |

[`ScatterWeightedPitchClassQuarterLength`](#music21.graph.plot.ScatterWeightedPitchClassQuarterLength "music21.graph.plot.ScatterWeightedPitchClassQuarterLength") instance variables

Instance variables inherited from [`GraphScatterWeighted`](moduleGraphPrimitives.html#music21.graph.primitives.GraphScatterWeighted "music21.graph.primitives.GraphScatterWeighted"):

|  |  |  |
| --- | --- | --- |
| * [`maxDiameter`](moduleGraphPrimitives.html#music21.graph.primitives.GraphScatterWeighted.maxDiameter "music21.graph.primitives.GraphScatterWeighted.maxDiameter") | * [`minDiameter`](moduleGraphPrimitives.html#music21.graph.primitives.GraphScatterWeighted.minDiameter "music21.graph.primitives.GraphScatterWeighted.minDiameter") |  |

## ScatterWeightedPitchSpaceDynamicSymbol

class music21.graph.plot.ScatterWeightedPitchSpaceDynamicSymbol(*streamObj=None*, *\*\*keywords*)[[source]](../_modules/music21/graph/plot.html#ScatterWeightedPitchSpaceDynamicSymbol)
:   A graph of dynamics used by pitch space.

    ```python
    >>> s = corpus.parse('schumann_robert/opus41no1/movement2.xml')
    >>> p = graph.plot.ScatterWeightedPitchSpaceDynamicSymbol(s)
    >>> p.run()  # with defaults and proper configuration, will open graph
    ```

    [![../_images/ScatterWeightedPitchSpaceDynamicSymbol.png](../_images/ScatterWeightedPitchSpaceDynamicSymbol.png)](../_images/ScatterWeightedPitchSpaceDynamicSymbol.png)

[`ScatterWeightedPitchSpaceDynamicSymbol`](#music21.graph.plot.ScatterWeightedPitchSpaceDynamicSymbol "music21.graph.plot.ScatterWeightedPitchSpaceDynamicSymbol") bases

* [`ScatterWeighted`](#music21.graph.plot.ScatterWeighted "music21.graph.plot.ScatterWeighted")
* [`GraphScatterWeighted`](moduleGraphPrimitives.html#music21.graph.primitives.GraphScatterWeighted "music21.graph.primitives.GraphScatterWeighted")
* [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph")
* [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`ScatterWeightedPitchSpaceDynamicSymbol`](#music21.graph.plot.ScatterWeightedPitchSpaceDynamicSymbol "music21.graph.plot.ScatterWeightedPitchSpaceDynamicSymbol") read-only properties

Read-only properties inherited from [`GraphScatterWeighted`](moduleGraphPrimitives.html#music21.graph.primitives.GraphScatterWeighted "music21.graph.primitives.GraphScatterWeighted"):

|  |  |  |
| --- | --- | --- |
| * [`rangeDiameter`](moduleGraphPrimitives.html#music21.graph.primitives.GraphScatterWeighted.rangeDiameter "music21.graph.primitives.GraphScatterWeighted.rangeDiameter") |  |  |

Read-only properties inherited from [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin"):

|  |  |  |
| --- | --- | --- |
| * [`allAxes`](#music21.graph.plot.PlotStreamMixin.allAxes "music21.graph.plot.PlotStreamMixin.allAxes") | * [`id`](#music21.graph.plot.PlotStreamMixin.id "music21.graph.plot.PlotStreamMixin.id") |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`ScatterWeightedPitchSpaceDynamicSymbol`](#music21.graph.plot.ScatterWeightedPitchSpaceDynamicSymbol "music21.graph.plot.ScatterWeightedPitchSpaceDynamicSymbol") read/write properties

Read/write properties inherited from [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph"):

|  |  |  |
| --- | --- | --- |
| * [`doneAction`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.doneAction "music21.graph.primitives.Graph.doneAction") |  |  |

[`ScatterWeightedPitchSpaceDynamicSymbol`](#music21.graph.plot.ScatterWeightedPitchSpaceDynamicSymbol "music21.graph.plot.ScatterWeightedPitchSpaceDynamicSymbol") methods

ScatterWeightedPitchSpaceDynamicSymbol.extractData()[[source]](../_modules/music21/graph/plot.html#ScatterWeightedPitchSpaceDynamicSymbol.extractData)

Methods inherited from [`GraphScatterWeighted`](moduleGraphPrimitives.html#music21.graph.primitives.GraphScatterWeighted "music21.graph.primitives.GraphScatterWeighted"):

|  |  |  |
| --- | --- | --- |
| * [`renderSubplot()`](moduleGraphPrimitives.html#music21.graph.primitives.GraphScatterWeighted.renderSubplot "music21.graph.primitives.GraphScatterWeighted.renderSubplot") |  |  |

Methods inherited from [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph"):

|  |  |  |
| --- | --- | --- |
| * [`applyFormatting()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyFormatting "music21.graph.primitives.Graph.applyFormatting") * [`applyFormattingToOneAxis()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyFormattingToOneAxis "music21.graph.primitives.Graph.applyFormattingToOneAxis") * [`applyGrid()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyGrid "music21.graph.primitives.Graph.applyGrid") * [`callDoneAction()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.callDoneAction "music21.graph.primitives.Graph.callDoneAction") * [`hideAxisSpines()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.hideAxisSpines "music21.graph.primitives.Graph.hideAxisSpines") | * [`nextColor()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.nextColor "music21.graph.primitives.Graph.nextColor") * [`process()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.process "music21.graph.primitives.Graph.process") * [`setAxisLabel()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setAxisLabel "music21.graph.primitives.Graph.setAxisLabel") * [`setAxisRange()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setAxisRange "music21.graph.primitives.Graph.setAxisRange") | * [`setIntegerTicksFromData()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setIntegerTicksFromData "music21.graph.primitives.Graph.setIntegerTicksFromData") * [`setTicks()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setTicks "music21.graph.primitives.Graph.setTicks") * [`show()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.show "music21.graph.primitives.Graph.show") * [`write()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.write "music21.graph.primitives.Graph.write") |

Methods inherited from [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin"):

|  |  |  |
| --- | --- | --- |
| * [`extractChordDataMultiAxis()`](#music21.graph.plot.PlotStreamMixin.extractChordDataMultiAxis "music21.graph.plot.PlotStreamMixin.extractChordDataMultiAxis") * [`extractChordDataOneAxis()`](#music21.graph.plot.PlotStreamMixin.extractChordDataOneAxis "music21.graph.plot.PlotStreamMixin.extractChordDataOneAxis") * [`fillValueLists()`](#music21.graph.plot.PlotStreamMixin.fillValueLists "music21.graph.plot.PlotStreamMixin.fillValueLists") | * [`postProcessData()`](#music21.graph.plot.PlotStreamMixin.postProcessData "music21.graph.plot.PlotStreamMixin.postProcessData") * [`postProcessElement()`](#music21.graph.plot.PlotStreamMixin.postProcessElement "music21.graph.plot.PlotStreamMixin.postProcessElement") * [`processOneElement()`](#music21.graph.plot.PlotStreamMixin.processOneElement "music21.graph.plot.PlotStreamMixin.processOneElement") | * [`run()`](#music21.graph.plot.PlotStreamMixin.run "music21.graph.plot.PlotStreamMixin.run") * [`setAxisKeywords()`](#music21.graph.plot.PlotStreamMixin.setAxisKeywords "music21.graph.plot.PlotStreamMixin.setAxisKeywords") |

[`ScatterWeightedPitchSpaceDynamicSymbol`](#music21.graph.plot.ScatterWeightedPitchSpaceDynamicSymbol "music21.graph.plot.ScatterWeightedPitchSpaceDynamicSymbol") instance variables

Instance variables inherited from [`GraphScatterWeighted`](moduleGraphPrimitives.html#music21.graph.primitives.GraphScatterWeighted "music21.graph.primitives.GraphScatterWeighted"):

|  |  |  |
| --- | --- | --- |
| * [`maxDiameter`](moduleGraphPrimitives.html#music21.graph.primitives.GraphScatterWeighted.maxDiameter "music21.graph.primitives.GraphScatterWeighted.maxDiameter") | * [`minDiameter`](moduleGraphPrimitives.html#music21.graph.primitives.GraphScatterWeighted.minDiameter "music21.graph.primitives.GraphScatterWeighted.minDiameter") |  |

## Plot3DBarsPitchSpaceQuarterLength

class music21.graph.plot.Plot3DBarsPitchSpaceQuarterLength(*streamObj=None*, *\*\*keywords*)[[source]](../_modules/music21/graph/plot.html#Plot3DBarsPitchSpaceQuarterLength)
:   A scatter plot of pitch and quarter length

    ```python
    >>> from music21.musicxml import testFiles
    >>> s = converter.parse(testFiles.mozartTrioK581Excerpt)
    >>> p = graph.plot.Plot3DBarsPitchSpaceQuarterLength(s)
    >>> p.id
    '3DBars-quarterLength-pitchSpace-count'
    >>> p.run()  # with defaults and proper configuration, will open graph
    ```

    [![../_images/Plot3DBarsPitchSpaceQuarterLength.png](../_images/Plot3DBarsPitchSpaceQuarterLength.png)](../_images/Plot3DBarsPitchSpaceQuarterLength.png)

[`Plot3DBarsPitchSpaceQuarterLength`](#music21.graph.plot.Plot3DBarsPitchSpaceQuarterLength "music21.graph.plot.Plot3DBarsPitchSpaceQuarterLength") bases

* [`Plot3DBars`](#music21.graph.plot.Plot3DBars "music21.graph.plot.Plot3DBars")
* [`Graph3DBars`](moduleGraphPrimitives.html#music21.graph.primitives.Graph3DBars "music21.graph.primitives.Graph3DBars")
* [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph")
* [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`Plot3DBarsPitchSpaceQuarterLength`](#music21.graph.plot.Plot3DBarsPitchSpaceQuarterLength "music21.graph.plot.Plot3DBarsPitchSpaceQuarterLength") read-only properties

Read-only properties inherited from [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin"):

|  |  |  |
| --- | --- | --- |
| * [`allAxes`](#music21.graph.plot.PlotStreamMixin.allAxes "music21.graph.plot.PlotStreamMixin.allAxes") | * [`id`](#music21.graph.plot.PlotStreamMixin.id "music21.graph.plot.PlotStreamMixin.id") |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`Plot3DBarsPitchSpaceQuarterLength`](#music21.graph.plot.Plot3DBarsPitchSpaceQuarterLength "music21.graph.plot.Plot3DBarsPitchSpaceQuarterLength") read/write properties

Read/write properties inherited from [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph"):

|  |  |  |
| --- | --- | --- |
| * [`doneAction`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.doneAction "music21.graph.primitives.Graph.doneAction") |  |  |

[`Plot3DBarsPitchSpaceQuarterLength`](#music21.graph.plot.Plot3DBarsPitchSpaceQuarterLength "music21.graph.plot.Plot3DBarsPitchSpaceQuarterLength") methods

Methods inherited from [`Graph3DBars`](moduleGraphPrimitives.html#music21.graph.primitives.Graph3DBars "music21.graph.primitives.Graph3DBars"):

|  |  |  |
| --- | --- | --- |
| * [`process()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph3DBars.process "music21.graph.primitives.Graph3DBars.process") | * [`renderSubplot()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph3DBars.renderSubplot "music21.graph.primitives.Graph3DBars.renderSubplot") |  |

Methods inherited from [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph"):

|  |  |  |
| --- | --- | --- |
| * [`applyFormatting()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyFormatting "music21.graph.primitives.Graph.applyFormatting") * [`applyFormattingToOneAxis()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyFormattingToOneAxis "music21.graph.primitives.Graph.applyFormattingToOneAxis") * [`applyGrid()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyGrid "music21.graph.primitives.Graph.applyGrid") * [`callDoneAction()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.callDoneAction "music21.graph.primitives.Graph.callDoneAction") | * [`hideAxisSpines()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.hideAxisSpines "music21.graph.primitives.Graph.hideAxisSpines") * [`nextColor()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.nextColor "music21.graph.primitives.Graph.nextColor") * [`setAxisLabel()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setAxisLabel "music21.graph.primitives.Graph.setAxisLabel") * [`setAxisRange()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setAxisRange "music21.graph.primitives.Graph.setAxisRange") | * [`setIntegerTicksFromData()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setIntegerTicksFromData "music21.graph.primitives.Graph.setIntegerTicksFromData") * [`setTicks()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setTicks "music21.graph.primitives.Graph.setTicks") * [`show()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.show "music21.graph.primitives.Graph.show") * [`write()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.write "music21.graph.primitives.Graph.write") |

Methods inherited from [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin"):

|  |  |  |
| --- | --- | --- |
| * [`extractChordDataMultiAxis()`](#music21.graph.plot.PlotStreamMixin.extractChordDataMultiAxis "music21.graph.plot.PlotStreamMixin.extractChordDataMultiAxis") * [`extractChordDataOneAxis()`](#music21.graph.plot.PlotStreamMixin.extractChordDataOneAxis "music21.graph.plot.PlotStreamMixin.extractChordDataOneAxis") * [`extractData()`](#music21.graph.plot.PlotStreamMixin.extractData "music21.graph.plot.PlotStreamMixin.extractData") | * [`fillValueLists()`](#music21.graph.plot.PlotStreamMixin.fillValueLists "music21.graph.plot.PlotStreamMixin.fillValueLists") * [`postProcessData()`](#music21.graph.plot.PlotStreamMixin.postProcessData "music21.graph.plot.PlotStreamMixin.postProcessData") * [`postProcessElement()`](#music21.graph.plot.PlotStreamMixin.postProcessElement "music21.graph.plot.PlotStreamMixin.postProcessElement") | * [`processOneElement()`](#music21.graph.plot.PlotStreamMixin.processOneElement "music21.graph.plot.PlotStreamMixin.processOneElement") * [`run()`](#music21.graph.plot.PlotStreamMixin.run "music21.graph.plot.PlotStreamMixin.run") * [`setAxisKeywords()`](#music21.graph.plot.PlotStreamMixin.setAxisKeywords "music21.graph.plot.PlotStreamMixin.setAxisKeywords") |

## Features

class music21.graph.plot.Features(*streamList*, *featureExtractors*, *labelList=None*, *\*\*keywords*)[[source]](../_modules/music21/graph/plot.html#Features)
:   Plots the output of a set of feature extractors.

    FeatureExtractors can be ids or classes.

[`Features`](#music21.graph.plot.Features "music21.graph.plot.Features") bases

* [`MultiStream`](#music21.graph.plot.MultiStream "music21.graph.plot.MultiStream")
* [`GraphGroupedVerticalBar`](moduleGraphPrimitives.html#music21.graph.primitives.GraphGroupedVerticalBar "music21.graph.primitives.GraphGroupedVerticalBar")
* [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph")
* [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`Features`](#music21.graph.plot.Features "music21.graph.plot.Features") read-only properties

Read-only properties inherited from [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin"):

|  |  |  |
| --- | --- | --- |
| * [`allAxes`](#music21.graph.plot.PlotStreamMixin.allAxes "music21.graph.plot.PlotStreamMixin.allAxes") | * [`id`](#music21.graph.plot.PlotStreamMixin.id "music21.graph.plot.PlotStreamMixin.id") |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`Features`](#music21.graph.plot.Features "music21.graph.plot.Features") read/write properties

Read/write properties inherited from [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph"):

|  |  |  |
| --- | --- | --- |
| * [`doneAction`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.doneAction "music21.graph.primitives.Graph.doneAction") |  |  |

[`Features`](#music21.graph.plot.Features "music21.graph.plot.Features") methods

Features.extractData()[[source]](../_modules/music21/graph/plot.html#Features.extractData)

Features.run(*\**, *callProcess: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *\*\*keywords*)[[source]](../_modules/music21/graph/plot.html#Features.run)
:   main routine to extract data, set axis labels, run process() on the underlying
    Graph object, and if self.doneAction is not None, either write or show the graph.

Methods inherited from [`MultiStream`](#music21.graph.plot.MultiStream "music21.graph.plot.MultiStream"):

|  |  |  |
| --- | --- | --- |
| * [`parseStreams()`](#music21.graph.plot.MultiStream.parseStreams "music21.graph.plot.MultiStream.parseStreams") |  |  |

Methods inherited from [`GraphGroupedVerticalBar`](moduleGraphPrimitives.html#music21.graph.primitives.GraphGroupedVerticalBar "music21.graph.primitives.GraphGroupedVerticalBar"):

|  |  |  |
| --- | --- | --- |
| * [`labelBars()`](moduleGraphPrimitives.html#music21.graph.primitives.GraphGroupedVerticalBar.labelBars "music21.graph.primitives.GraphGroupedVerticalBar.labelBars") | * [`renderSubplot()`](moduleGraphPrimitives.html#music21.graph.primitives.GraphGroupedVerticalBar.renderSubplot "music21.graph.primitives.GraphGroupedVerticalBar.renderSubplot") |  |

Methods inherited from [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph"):

|  |  |  |
| --- | --- | --- |
| * [`applyFormatting()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyFormatting "music21.graph.primitives.Graph.applyFormatting") * [`applyFormattingToOneAxis()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyFormattingToOneAxis "music21.graph.primitives.Graph.applyFormattingToOneAxis") * [`applyGrid()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyGrid "music21.graph.primitives.Graph.applyGrid") * [`callDoneAction()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.callDoneAction "music21.graph.primitives.Graph.callDoneAction") * [`hideAxisSpines()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.hideAxisSpines "music21.graph.primitives.Graph.hideAxisSpines") | * [`nextColor()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.nextColor "music21.graph.primitives.Graph.nextColor") * [`process()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.process "music21.graph.primitives.Graph.process") * [`setAxisLabel()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setAxisLabel "music21.graph.primitives.Graph.setAxisLabel") * [`setAxisRange()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setAxisRange "music21.graph.primitives.Graph.setAxisRange") | * [`setIntegerTicksFromData()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setIntegerTicksFromData "music21.graph.primitives.Graph.setIntegerTicksFromData") * [`setTicks()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setTicks "music21.graph.primitives.Graph.setTicks") * [`show()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.show "music21.graph.primitives.Graph.show") * [`write()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.write "music21.graph.primitives.Graph.write") |

Methods inherited from [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin"):

|  |  |  |
| --- | --- | --- |
| * [`extractChordDataMultiAxis()`](#music21.graph.plot.PlotStreamMixin.extractChordDataMultiAxis "music21.graph.plot.PlotStreamMixin.extractChordDataMultiAxis") * [`extractChordDataOneAxis()`](#music21.graph.plot.PlotStreamMixin.extractChordDataOneAxis "music21.graph.plot.PlotStreamMixin.extractChordDataOneAxis") * [`fillValueLists()`](#music21.graph.plot.PlotStreamMixin.fillValueLists "music21.graph.plot.PlotStreamMixin.fillValueLists") | * [`postProcessData()`](#music21.graph.plot.PlotStreamMixin.postProcessData "music21.graph.plot.PlotStreamMixin.postProcessData") * [`postProcessElement()`](#music21.graph.plot.PlotStreamMixin.postProcessElement "music21.graph.plot.PlotStreamMixin.postProcessElement") | * [`processOneElement()`](#music21.graph.plot.PlotStreamMixin.processOneElement "music21.graph.plot.PlotStreamMixin.processOneElement") * [`setAxisKeywords()`](#music21.graph.plot.PlotStreamMixin.setAxisKeywords "music21.graph.plot.PlotStreamMixin.setAxisKeywords") |

## Histogram

class music21.graph.plot.Histogram(*streamObj=None*, *\*\*keywords*)[[source]](../_modules/music21/graph/plot.html#Histogram)
:   Base class for histograms that plot one axis against its count

[`Histogram`](#music21.graph.plot.Histogram "music21.graph.plot.Histogram") bases

* [`GraphHistogram`](moduleGraphPrimitives.html#music21.graph.primitives.GraphHistogram "music21.graph.primitives.GraphHistogram")
* [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph")
* [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`Histogram`](#music21.graph.plot.Histogram "music21.graph.plot.Histogram") read-only properties

Read-only properties inherited from [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin"):

|  |  |  |
| --- | --- | --- |
| * [`allAxes`](#music21.graph.plot.PlotStreamMixin.allAxes "music21.graph.plot.PlotStreamMixin.allAxes") | * [`id`](#music21.graph.plot.PlotStreamMixin.id "music21.graph.plot.PlotStreamMixin.id") |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`Histogram`](#music21.graph.plot.Histogram "music21.graph.plot.Histogram") read/write properties

Read/write properties inherited from [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph"):

|  |  |  |
| --- | --- | --- |
| * [`doneAction`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.doneAction "music21.graph.primitives.Graph.doneAction") |  |  |

[`Histogram`](#music21.graph.plot.Histogram "music21.graph.plot.Histogram") methods

Histogram.remapXTicksData()[[source]](../_modules/music21/graph/plot.html#Histogram.remapXTicksData)
:   Changes the ticks and data so that they both run
    1, 2, 3, 4, etc.

Histogram.run(*\**, *callProcess: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *\*\*keywords*)[[source]](../_modules/music21/graph/plot.html#Histogram.run)
:   Override run method to remap X data into individual bins.

Methods inherited from [`GraphHistogram`](moduleGraphPrimitives.html#music21.graph.primitives.GraphHistogram "music21.graph.primitives.GraphHistogram"):

|  |  |  |
| --- | --- | --- |
| * [`renderSubplot()`](moduleGraphPrimitives.html#music21.graph.primitives.GraphHistogram.renderSubplot "music21.graph.primitives.GraphHistogram.renderSubplot") |  |  |

Methods inherited from [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph"):

|  |  |  |
| --- | --- | --- |
| * [`applyFormatting()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyFormatting "music21.graph.primitives.Graph.applyFormatting") * [`applyFormattingToOneAxis()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyFormattingToOneAxis "music21.graph.primitives.Graph.applyFormattingToOneAxis") * [`applyGrid()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyGrid "music21.graph.primitives.Graph.applyGrid") * [`callDoneAction()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.callDoneAction "music21.graph.primitives.Graph.callDoneAction") * [`hideAxisSpines()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.hideAxisSpines "music21.graph.primitives.Graph.hideAxisSpines") | * [`nextColor()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.nextColor "music21.graph.primitives.Graph.nextColor") * [`process()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.process "music21.graph.primitives.Graph.process") * [`setAxisLabel()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setAxisLabel "music21.graph.primitives.Graph.setAxisLabel") * [`setAxisRange()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setAxisRange "music21.graph.primitives.Graph.setAxisRange") | * [`setIntegerTicksFromData()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setIntegerTicksFromData "music21.graph.primitives.Graph.setIntegerTicksFromData") * [`setTicks()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setTicks "music21.graph.primitives.Graph.setTicks") * [`show()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.show "music21.graph.primitives.Graph.show") * [`write()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.write "music21.graph.primitives.Graph.write") |

Methods inherited from [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin"):

|  |  |  |
| --- | --- | --- |
| * [`extractChordDataMultiAxis()`](#music21.graph.plot.PlotStreamMixin.extractChordDataMultiAxis "music21.graph.plot.PlotStreamMixin.extractChordDataMultiAxis") * [`extractChordDataOneAxis()`](#music21.graph.plot.PlotStreamMixin.extractChordDataOneAxis "music21.graph.plot.PlotStreamMixin.extractChordDataOneAxis") * [`extractData()`](#music21.graph.plot.PlotStreamMixin.extractData "music21.graph.plot.PlotStreamMixin.extractData") | * [`fillValueLists()`](#music21.graph.plot.PlotStreamMixin.fillValueLists "music21.graph.plot.PlotStreamMixin.fillValueLists") * [`postProcessData()`](#music21.graph.plot.PlotStreamMixin.postProcessData "music21.graph.plot.PlotStreamMixin.postProcessData") * [`postProcessElement()`](#music21.graph.plot.PlotStreamMixin.postProcessElement "music21.graph.plot.PlotStreamMixin.postProcessElement") | * [`processOneElement()`](#music21.graph.plot.PlotStreamMixin.processOneElement "music21.graph.plot.PlotStreamMixin.processOneElement") * [`setAxisKeywords()`](#music21.graph.plot.PlotStreamMixin.setAxisKeywords "music21.graph.plot.PlotStreamMixin.setAxisKeywords") |

[`Histogram`](#music21.graph.plot.Histogram "music21.graph.plot.Histogram") instance variables

Instance variables inherited from [`GraphHistogram`](moduleGraphPrimitives.html#music21.graph.primitives.GraphHistogram "music21.graph.primitives.GraphHistogram"):

|  |  |  |
| --- | --- | --- |
| * [`binWidth`](moduleGraphPrimitives.html#music21.graph.primitives.GraphHistogram.binWidth "music21.graph.primitives.GraphHistogram.binWidth") |  |  |

## HorizontalBar

class music21.graph.plot.HorizontalBar(*streamObj: [Stream](moduleStreamBase.html#music21.stream.base.Stream "music21.stream.base.Stream") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\**, *colorByPart=False*, *\*\*keywords*)[[source]](../_modules/music21/graph/plot.html#HorizontalBar)
:   A graph of events, sorted by pitch, over time.

    If colorByPart is True, then each part will get its own color from
    self.colors (unless there are more parts than colors).

[`HorizontalBar`](#music21.graph.plot.HorizontalBar "music21.graph.plot.HorizontalBar") bases

* [`GraphHorizontalBar`](moduleGraphPrimitives.html#music21.graph.primitives.GraphHorizontalBar "music21.graph.primitives.GraphHorizontalBar")
* [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph")
* [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`HorizontalBar`](#music21.graph.plot.HorizontalBar "music21.graph.plot.HorizontalBar") read-only properties

Read-only properties inherited from [`GraphHorizontalBar`](moduleGraphPrimitives.html#music21.graph.primitives.GraphHorizontalBar "music21.graph.primitives.GraphHorizontalBar"):

|  |  |  |
| --- | --- | --- |
| * [`barHeight`](moduleGraphPrimitives.html#music21.graph.primitives.GraphHorizontalBar.barHeight "music21.graph.primitives.GraphHorizontalBar.barHeight") |  |  |

Read-only properties inherited from [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin"):

|  |  |  |
| --- | --- | --- |
| * [`allAxes`](#music21.graph.plot.PlotStreamMixin.allAxes "music21.graph.plot.PlotStreamMixin.allAxes") | * [`id`](#music21.graph.plot.PlotStreamMixin.id "music21.graph.plot.PlotStreamMixin.id") |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`HorizontalBar`](#music21.graph.plot.HorizontalBar "music21.graph.plot.HorizontalBar") read/write properties

Read/write properties inherited from [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph"):

|  |  |  |
| --- | --- | --- |
| * [`doneAction`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.doneAction "music21.graph.primitives.Graph.doneAction") |  |  |

[`HorizontalBar`](#music21.graph.plot.HorizontalBar "music21.graph.plot.HorizontalBar") methods

HorizontalBar.assignColorsToParts() → [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[Part](moduleStreamBase.html#music21.stream.base.Part "music21.stream.base.Part"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")][[source]](../_modules/music21/graph/plot.html#HorizontalBar.assignColorsToParts)
:   Give a different color for each part, if self.colorByPart is True.

    Returns the assignment for any further manipulation.

    Currently, two piano hands (PartStaff objects) get different colors.

    ```python
    >>> bach = corpus.parse('bwv66.6')
    >>> plot = graph.plot.HorizontalBar(bach, colorByPart=True)
    >>> plot.assignColorsToParts()
    {<music21.stream.Part Soprano>: '#605c7f',
     <music21.stream.Part Alto>: '#5c7f60',
     <music21.stream.Part Tenor>: '#988969',
     <music21.stream.Part Bass>: '#628297'}
    ```

HorizontalBar.postProcessData()[[source]](../_modules/music21/graph/plot.html#HorizontalBar.postProcessData)
:   Call any post data processing routines here and on any axes.

HorizontalBar.postProcessElement(*el: [Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")*, *formatDict: [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)"), [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")]*, *\*values: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Real](https://docs.python.org/3/library/numbers.html#numbers.Real "(in Python v3.14)")]*)[[source]](../_modules/music21/graph/plot.html#HorizontalBar.postProcessElement)
:   Assign colors to each element if colorByPart is True.

HorizontalBar.run(*\**, *callProcess: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *\*\*keywords*)[[source]](../_modules/music21/graph/plot.html#HorizontalBar.run)
:   Optionally assign colors to Part objects and then do the normal run.

Methods inherited from [`GraphHorizontalBar`](moduleGraphPrimitives.html#music21.graph.primitives.GraphHorizontalBar "music21.graph.primitives.GraphHorizontalBar"):

|  |  |  |
| --- | --- | --- |
| * [`renderSubplot()`](moduleGraphPrimitives.html#music21.graph.primitives.GraphHorizontalBar.renderSubplot "music21.graph.primitives.GraphHorizontalBar.renderSubplot") |  |  |

Methods inherited from [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph"):

|  |  |  |
| --- | --- | --- |
| * [`applyFormatting()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyFormatting "music21.graph.primitives.Graph.applyFormatting") * [`applyFormattingToOneAxis()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyFormattingToOneAxis "music21.graph.primitives.Graph.applyFormattingToOneAxis") * [`applyGrid()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyGrid "music21.graph.primitives.Graph.applyGrid") * [`callDoneAction()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.callDoneAction "music21.graph.primitives.Graph.callDoneAction") * [`hideAxisSpines()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.hideAxisSpines "music21.graph.primitives.Graph.hideAxisSpines") | * [`nextColor()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.nextColor "music21.graph.primitives.Graph.nextColor") * [`process()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.process "music21.graph.primitives.Graph.process") * [`setAxisLabel()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setAxisLabel "music21.graph.primitives.Graph.setAxisLabel") * [`setAxisRange()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setAxisRange "music21.graph.primitives.Graph.setAxisRange") | * [`setIntegerTicksFromData()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setIntegerTicksFromData "music21.graph.primitives.Graph.setIntegerTicksFromData") * [`setTicks()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setTicks "music21.graph.primitives.Graph.setTicks") * [`show()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.show "music21.graph.primitives.Graph.show") * [`write()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.write "music21.graph.primitives.Graph.write") |

Methods inherited from [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin"):

|  |  |  |
| --- | --- | --- |
| * [`extractChordDataMultiAxis()`](#music21.graph.plot.PlotStreamMixin.extractChordDataMultiAxis "music21.graph.plot.PlotStreamMixin.extractChordDataMultiAxis") * [`extractChordDataOneAxis()`](#music21.graph.plot.PlotStreamMixin.extractChordDataOneAxis "music21.graph.plot.PlotStreamMixin.extractChordDataOneAxis") | * [`extractData()`](#music21.graph.plot.PlotStreamMixin.extractData "music21.graph.plot.PlotStreamMixin.extractData") * [`fillValueLists()`](#music21.graph.plot.PlotStreamMixin.fillValueLists "music21.graph.plot.PlotStreamMixin.fillValueLists") | * [`processOneElement()`](#music21.graph.plot.PlotStreamMixin.processOneElement "music21.graph.plot.PlotStreamMixin.processOneElement") * [`setAxisKeywords()`](#music21.graph.plot.PlotStreamMixin.setAxisKeywords "music21.graph.plot.PlotStreamMixin.setAxisKeywords") |

[`HorizontalBar`](#music21.graph.plot.HorizontalBar "music21.graph.plot.HorizontalBar") instance variables

Instance variables inherited from [`GraphHorizontalBar`](moduleGraphPrimitives.html#music21.graph.primitives.GraphHorizontalBar "music21.graph.primitives.GraphHorizontalBar"):

|  |  |  |
| --- | --- | --- |
| * [`barSpace`](moduleGraphPrimitives.html#music21.graph.primitives.GraphHorizontalBar.barSpace "music21.graph.primitives.GraphHorizontalBar.barSpace") | * [`margin`](moduleGraphPrimitives.html#music21.graph.primitives.GraphHorizontalBar.margin "music21.graph.primitives.GraphHorizontalBar.margin") |  |

## HorizontalBarWeighted

class music21.graph.plot.HorizontalBarWeighted(*streamObj=None*, *\*\*keywords*)[[source]](../_modules/music21/graph/plot.html#HorizontalBarWeighted)
:   A base class for plots of Scores with weighted (by height) horizontal bars.
    Many weighted segments represent a dynamic parameter of a Part.

[`HorizontalBarWeighted`](#music21.graph.plot.HorizontalBarWeighted "music21.graph.plot.HorizontalBarWeighted") bases

* [`GraphHorizontalBarWeighted`](moduleGraphPrimitives.html#music21.graph.primitives.GraphHorizontalBarWeighted "music21.graph.primitives.GraphHorizontalBarWeighted")
* [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph")
* [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`HorizontalBarWeighted`](#music21.graph.plot.HorizontalBarWeighted "music21.graph.plot.HorizontalBarWeighted") read-only properties

Read-only properties inherited from [`GraphHorizontalBarWeighted`](moduleGraphPrimitives.html#music21.graph.primitives.GraphHorizontalBarWeighted "music21.graph.primitives.GraphHorizontalBarWeighted"):

|  |  |  |
| --- | --- | --- |
| * [`barHeight`](moduleGraphPrimitives.html#music21.graph.primitives.GraphHorizontalBarWeighted.barHeight "music21.graph.primitives.GraphHorizontalBarWeighted.barHeight") |  |  |

Read-only properties inherited from [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin"):

|  |  |  |
| --- | --- | --- |
| * [`allAxes`](#music21.graph.plot.PlotStreamMixin.allAxes "music21.graph.plot.PlotStreamMixin.allAxes") | * [`id`](#music21.graph.plot.PlotStreamMixin.id "music21.graph.plot.PlotStreamMixin.id") |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`HorizontalBarWeighted`](#music21.graph.plot.HorizontalBarWeighted "music21.graph.plot.HorizontalBarWeighted") read/write properties

Read/write properties inherited from [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph"):

|  |  |  |
| --- | --- | --- |
| * [`doneAction`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.doneAction "music21.graph.primitives.Graph.doneAction") |  |  |

[`HorizontalBarWeighted`](#music21.graph.plot.HorizontalBarWeighted "music21.graph.plot.HorizontalBarWeighted") methods

HorizontalBarWeighted.extractData()[[source]](../_modules/music21/graph/plot.html#HorizontalBarWeighted.extractData)
:   Extract the data from the Stream.

Methods inherited from [`GraphHorizontalBarWeighted`](moduleGraphPrimitives.html#music21.graph.primitives.GraphHorizontalBarWeighted "music21.graph.primitives.GraphHorizontalBarWeighted"):

|  |  |  |
| --- | --- | --- |
| * [`renderSubplot()`](moduleGraphPrimitives.html#music21.graph.primitives.GraphHorizontalBarWeighted.renderSubplot "music21.graph.primitives.GraphHorizontalBarWeighted.renderSubplot") |  |  |

Methods inherited from [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph"):

|  |  |  |
| --- | --- | --- |
| * [`applyFormatting()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyFormatting "music21.graph.primitives.Graph.applyFormatting") * [`applyFormattingToOneAxis()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyFormattingToOneAxis "music21.graph.primitives.Graph.applyFormattingToOneAxis") * [`applyGrid()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyGrid "music21.graph.primitives.Graph.applyGrid") * [`callDoneAction()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.callDoneAction "music21.graph.primitives.Graph.callDoneAction") * [`hideAxisSpines()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.hideAxisSpines "music21.graph.primitives.Graph.hideAxisSpines") | * [`nextColor()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.nextColor "music21.graph.primitives.Graph.nextColor") * [`process()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.process "music21.graph.primitives.Graph.process") * [`setAxisLabel()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setAxisLabel "music21.graph.primitives.Graph.setAxisLabel") * [`setAxisRange()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setAxisRange "music21.graph.primitives.Graph.setAxisRange") | * [`setIntegerTicksFromData()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setIntegerTicksFromData "music21.graph.primitives.Graph.setIntegerTicksFromData") * [`setTicks()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setTicks "music21.graph.primitives.Graph.setTicks") * [`show()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.show "music21.graph.primitives.Graph.show") * [`write()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.write "music21.graph.primitives.Graph.write") |

Methods inherited from [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin"):

|  |  |  |
| --- | --- | --- |
| * [`extractChordDataMultiAxis()`](#music21.graph.plot.PlotStreamMixin.extractChordDataMultiAxis "music21.graph.plot.PlotStreamMixin.extractChordDataMultiAxis") * [`extractChordDataOneAxis()`](#music21.graph.plot.PlotStreamMixin.extractChordDataOneAxis "music21.graph.plot.PlotStreamMixin.extractChordDataOneAxis") * [`fillValueLists()`](#music21.graph.plot.PlotStreamMixin.fillValueLists "music21.graph.plot.PlotStreamMixin.fillValueLists") | * [`postProcessData()`](#music21.graph.plot.PlotStreamMixin.postProcessData "music21.graph.plot.PlotStreamMixin.postProcessData") * [`postProcessElement()`](#music21.graph.plot.PlotStreamMixin.postProcessElement "music21.graph.plot.PlotStreamMixin.postProcessElement") * [`processOneElement()`](#music21.graph.plot.PlotStreamMixin.processOneElement "music21.graph.plot.PlotStreamMixin.processOneElement") | * [`run()`](#music21.graph.plot.PlotStreamMixin.run "music21.graph.plot.PlotStreamMixin.run") * [`setAxisKeywords()`](#music21.graph.plot.PlotStreamMixin.setAxisKeywords "music21.graph.plot.PlotStreamMixin.setAxisKeywords") |

[`HorizontalBarWeighted`](#music21.graph.plot.HorizontalBarWeighted "music21.graph.plot.HorizontalBarWeighted") instance variables

Instance variables inherited from [`GraphHorizontalBarWeighted`](moduleGraphPrimitives.html#music21.graph.primitives.GraphHorizontalBarWeighted "music21.graph.primitives.GraphHorizontalBarWeighted"):

|  |  |  |
| --- | --- | --- |
| * [`barSpace`](moduleGraphPrimitives.html#music21.graph.primitives.GraphHorizontalBarWeighted.barSpace "music21.graph.primitives.GraphHorizontalBarWeighted.barSpace") | * [`margin`](moduleGraphPrimitives.html#music21.graph.primitives.GraphHorizontalBarWeighted.margin "music21.graph.primitives.GraphHorizontalBarWeighted.margin") |  |

## MultiStream

class music21.graph.plot.MultiStream(*streamList*, *labelList=None*, *\*\*keywords*)[[source]](../_modules/music21/graph/plot.html#MultiStream)
:   Approaches to plotting and graphing multiple Streams.
    A base class from which Stream plotting Classes inherit.

    Not yet integrated into the 2017 system, unfortunately.

    Provide a list of Streams as an argument. Optionally
    provide an additional list of labels for each list.

[`MultiStream`](#music21.graph.plot.MultiStream "music21.graph.plot.MultiStream") bases

* [`GraphGroupedVerticalBar`](moduleGraphPrimitives.html#music21.graph.primitives.GraphGroupedVerticalBar "music21.graph.primitives.GraphGroupedVerticalBar")
* [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph")
* [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`MultiStream`](#music21.graph.plot.MultiStream "music21.graph.plot.MultiStream") read-only properties

Read-only properties inherited from [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin"):

|  |  |  |
| --- | --- | --- |
| * [`allAxes`](#music21.graph.plot.PlotStreamMixin.allAxes "music21.graph.plot.PlotStreamMixin.allAxes") | * [`id`](#music21.graph.plot.PlotStreamMixin.id "music21.graph.plot.PlotStreamMixin.id") |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`MultiStream`](#music21.graph.plot.MultiStream "music21.graph.plot.MultiStream") read/write properties

Read/write properties inherited from [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph"):

|  |  |  |
| --- | --- | --- |
| * [`doneAction`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.doneAction "music21.graph.primitives.Graph.doneAction") |  |  |

[`MultiStream`](#music21.graph.plot.MultiStream "music21.graph.plot.MultiStream") methods

MultiStream.parseStreams(*streamList*)[[source]](../_modules/music21/graph/plot.html#MultiStream.parseStreams)

Methods inherited from [`GraphGroupedVerticalBar`](moduleGraphPrimitives.html#music21.graph.primitives.GraphGroupedVerticalBar "music21.graph.primitives.GraphGroupedVerticalBar"):

|  |  |  |
| --- | --- | --- |
| * [`labelBars()`](moduleGraphPrimitives.html#music21.graph.primitives.GraphGroupedVerticalBar.labelBars "music21.graph.primitives.GraphGroupedVerticalBar.labelBars") | * [`renderSubplot()`](moduleGraphPrimitives.html#music21.graph.primitives.GraphGroupedVerticalBar.renderSubplot "music21.graph.primitives.GraphGroupedVerticalBar.renderSubplot") |  |

Methods inherited from [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph"):

|  |  |  |
| --- | --- | --- |
| * [`applyFormatting()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyFormatting "music21.graph.primitives.Graph.applyFormatting") * [`applyFormattingToOneAxis()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyFormattingToOneAxis "music21.graph.primitives.Graph.applyFormattingToOneAxis") * [`applyGrid()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyGrid "music21.graph.primitives.Graph.applyGrid") * [`callDoneAction()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.callDoneAction "music21.graph.primitives.Graph.callDoneAction") * [`hideAxisSpines()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.hideAxisSpines "music21.graph.primitives.Graph.hideAxisSpines") | * [`nextColor()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.nextColor "music21.graph.primitives.Graph.nextColor") * [`process()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.process "music21.graph.primitives.Graph.process") * [`setAxisLabel()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setAxisLabel "music21.graph.primitives.Graph.setAxisLabel") * [`setAxisRange()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setAxisRange "music21.graph.primitives.Graph.setAxisRange") | * [`setIntegerTicksFromData()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setIntegerTicksFromData "music21.graph.primitives.Graph.setIntegerTicksFromData") * [`setTicks()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setTicks "music21.graph.primitives.Graph.setTicks") * [`show()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.show "music21.graph.primitives.Graph.show") * [`write()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.write "music21.graph.primitives.Graph.write") |

Methods inherited from [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin"):

|  |  |  |
| --- | --- | --- |
| * [`extractChordDataMultiAxis()`](#music21.graph.plot.PlotStreamMixin.extractChordDataMultiAxis "music21.graph.plot.PlotStreamMixin.extractChordDataMultiAxis") * [`extractChordDataOneAxis()`](#music21.graph.plot.PlotStreamMixin.extractChordDataOneAxis "music21.graph.plot.PlotStreamMixin.extractChordDataOneAxis") * [`extractData()`](#music21.graph.plot.PlotStreamMixin.extractData "music21.graph.plot.PlotStreamMixin.extractData") | * [`fillValueLists()`](#music21.graph.plot.PlotStreamMixin.fillValueLists "music21.graph.plot.PlotStreamMixin.fillValueLists") * [`postProcessData()`](#music21.graph.plot.PlotStreamMixin.postProcessData "music21.graph.plot.PlotStreamMixin.postProcessData") * [`postProcessElement()`](#music21.graph.plot.PlotStreamMixin.postProcessElement "music21.graph.plot.PlotStreamMixin.postProcessElement") | * [`processOneElement()`](#music21.graph.plot.PlotStreamMixin.processOneElement "music21.graph.plot.PlotStreamMixin.processOneElement") * [`run()`](#music21.graph.plot.PlotStreamMixin.run "music21.graph.plot.PlotStreamMixin.run") * [`setAxisKeywords()`](#music21.graph.plot.PlotStreamMixin.setAxisKeywords "music21.graph.plot.PlotStreamMixin.setAxisKeywords") |

## Plot3DBars

class music21.graph.plot.Plot3DBars(*streamObj=None*, *\*\*keywords*)[[source]](../_modules/music21/graph/plot.html#Plot3DBars)
:   Base class for Stream plotting classes.

[`Plot3DBars`](#music21.graph.plot.Plot3DBars "music21.graph.plot.Plot3DBars") bases

* [`Graph3DBars`](moduleGraphPrimitives.html#music21.graph.primitives.Graph3DBars "music21.graph.primitives.Graph3DBars")
* [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph")
* [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`Plot3DBars`](#music21.graph.plot.Plot3DBars "music21.graph.plot.Plot3DBars") read-only properties

Read-only properties inherited from [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin"):

|  |  |  |
| --- | --- | --- |
| * [`allAxes`](#music21.graph.plot.PlotStreamMixin.allAxes "music21.graph.plot.PlotStreamMixin.allAxes") | * [`id`](#music21.graph.plot.PlotStreamMixin.id "music21.graph.plot.PlotStreamMixin.id") |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`Plot3DBars`](#music21.graph.plot.Plot3DBars "music21.graph.plot.Plot3DBars") read/write properties

Read/write properties inherited from [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph"):

|  |  |  |
| --- | --- | --- |
| * [`doneAction`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.doneAction "music21.graph.primitives.Graph.doneAction") |  |  |

[`Plot3DBars`](#music21.graph.plot.Plot3DBars "music21.graph.plot.Plot3DBars") methods

Methods inherited from [`Graph3DBars`](moduleGraphPrimitives.html#music21.graph.primitives.Graph3DBars "music21.graph.primitives.Graph3DBars"):

|  |  |  |
| --- | --- | --- |
| * [`process()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph3DBars.process "music21.graph.primitives.Graph3DBars.process") | * [`renderSubplot()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph3DBars.renderSubplot "music21.graph.primitives.Graph3DBars.renderSubplot") |  |

Methods inherited from [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph"):

|  |  |  |
| --- | --- | --- |
| * [`applyFormatting()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyFormatting "music21.graph.primitives.Graph.applyFormatting") * [`applyFormattingToOneAxis()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyFormattingToOneAxis "music21.graph.primitives.Graph.applyFormattingToOneAxis") * [`applyGrid()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyGrid "music21.graph.primitives.Graph.applyGrid") * [`callDoneAction()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.callDoneAction "music21.graph.primitives.Graph.callDoneAction") | * [`hideAxisSpines()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.hideAxisSpines "music21.graph.primitives.Graph.hideAxisSpines") * [`nextColor()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.nextColor "music21.graph.primitives.Graph.nextColor") * [`setAxisLabel()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setAxisLabel "music21.graph.primitives.Graph.setAxisLabel") * [`setAxisRange()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setAxisRange "music21.graph.primitives.Graph.setAxisRange") | * [`setIntegerTicksFromData()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setIntegerTicksFromData "music21.graph.primitives.Graph.setIntegerTicksFromData") * [`setTicks()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setTicks "music21.graph.primitives.Graph.setTicks") * [`show()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.show "music21.graph.primitives.Graph.show") * [`write()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.write "music21.graph.primitives.Graph.write") |

Methods inherited from [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin"):

|  |  |  |
| --- | --- | --- |
| * [`extractChordDataMultiAxis()`](#music21.graph.plot.PlotStreamMixin.extractChordDataMultiAxis "music21.graph.plot.PlotStreamMixin.extractChordDataMultiAxis") * [`extractChordDataOneAxis()`](#music21.graph.plot.PlotStreamMixin.extractChordDataOneAxis "music21.graph.plot.PlotStreamMixin.extractChordDataOneAxis") * [`extractData()`](#music21.graph.plot.PlotStreamMixin.extractData "music21.graph.plot.PlotStreamMixin.extractData") | * [`fillValueLists()`](#music21.graph.plot.PlotStreamMixin.fillValueLists "music21.graph.plot.PlotStreamMixin.fillValueLists") * [`postProcessData()`](#music21.graph.plot.PlotStreamMixin.postProcessData "music21.graph.plot.PlotStreamMixin.postProcessData") * [`postProcessElement()`](#music21.graph.plot.PlotStreamMixin.postProcessElement "music21.graph.plot.PlotStreamMixin.postProcessElement") | * [`processOneElement()`](#music21.graph.plot.PlotStreamMixin.processOneElement "music21.graph.plot.PlotStreamMixin.processOneElement") * [`run()`](#music21.graph.plot.PlotStreamMixin.run "music21.graph.plot.PlotStreamMixin.run") * [`setAxisKeywords()`](#music21.graph.plot.PlotStreamMixin.setAxisKeywords "music21.graph.plot.PlotStreamMixin.setAxisKeywords") |

## PlotStream

class music21.graph.plot.PlotStream(*streamObj=None*, *\*\*keywords*)[[source]](../_modules/music21/graph/plot.html#PlotStream)
:   A generic stream plotter.

[`PlotStream`](#music21.graph.plot.PlotStream "music21.graph.plot.PlotStream") bases

* [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph")
* [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`PlotStream`](#music21.graph.plot.PlotStream "music21.graph.plot.PlotStream") read-only properties

Read-only properties inherited from [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin"):

|  |  |  |
| --- | --- | --- |
| * [`allAxes`](#music21.graph.plot.PlotStreamMixin.allAxes "music21.graph.plot.PlotStreamMixin.allAxes") | * [`id`](#music21.graph.plot.PlotStreamMixin.id "music21.graph.plot.PlotStreamMixin.id") |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`PlotStream`](#music21.graph.plot.PlotStream "music21.graph.plot.PlotStream") read/write properties

Read/write properties inherited from [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph"):

|  |  |  |
| --- | --- | --- |
| * [`doneAction`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.doneAction "music21.graph.primitives.Graph.doneAction") |  |  |

[`PlotStream`](#music21.graph.plot.PlotStream "music21.graph.plot.PlotStream") methods

Methods inherited from [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph"):

|  |  |  |
| --- | --- | --- |
| * [`applyFormatting()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyFormatting "music21.graph.primitives.Graph.applyFormatting") * [`applyFormattingToOneAxis()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyFormattingToOneAxis "music21.graph.primitives.Graph.applyFormattingToOneAxis") * [`applyGrid()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyGrid "music21.graph.primitives.Graph.applyGrid") * [`callDoneAction()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.callDoneAction "music21.graph.primitives.Graph.callDoneAction") * [`hideAxisSpines()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.hideAxisSpines "music21.graph.primitives.Graph.hideAxisSpines") | * [`nextColor()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.nextColor "music21.graph.primitives.Graph.nextColor") * [`process()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.process "music21.graph.primitives.Graph.process") * [`renderSubplot()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.renderSubplot "music21.graph.primitives.Graph.renderSubplot") * [`setAxisLabel()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setAxisLabel "music21.graph.primitives.Graph.setAxisLabel") * [`setAxisRange()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setAxisRange "music21.graph.primitives.Graph.setAxisRange") | * [`setIntegerTicksFromData()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setIntegerTicksFromData "music21.graph.primitives.Graph.setIntegerTicksFromData") * [`setTicks()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setTicks "music21.graph.primitives.Graph.setTicks") * [`show()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.show "music21.graph.primitives.Graph.show") * [`write()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.write "music21.graph.primitives.Graph.write") |

Methods inherited from [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin"):

|  |  |  |
| --- | --- | --- |
| * [`extractChordDataMultiAxis()`](#music21.graph.plot.PlotStreamMixin.extractChordDataMultiAxis "music21.graph.plot.PlotStreamMixin.extractChordDataMultiAxis") * [`extractChordDataOneAxis()`](#music21.graph.plot.PlotStreamMixin.extractChordDataOneAxis "music21.graph.plot.PlotStreamMixin.extractChordDataOneAxis") * [`extractData()`](#music21.graph.plot.PlotStreamMixin.extractData "music21.graph.plot.PlotStreamMixin.extractData") | * [`fillValueLists()`](#music21.graph.plot.PlotStreamMixin.fillValueLists "music21.graph.plot.PlotStreamMixin.fillValueLists") * [`postProcessData()`](#music21.graph.plot.PlotStreamMixin.postProcessData "music21.graph.plot.PlotStreamMixin.postProcessData") * [`postProcessElement()`](#music21.graph.plot.PlotStreamMixin.postProcessElement "music21.graph.plot.PlotStreamMixin.postProcessElement") | * [`processOneElement()`](#music21.graph.plot.PlotStreamMixin.processOneElement "music21.graph.plot.PlotStreamMixin.processOneElement") * [`run()`](#music21.graph.plot.PlotStreamMixin.run "music21.graph.plot.PlotStreamMixin.run") * [`setAxisKeywords()`](#music21.graph.plot.PlotStreamMixin.setAxisKeywords "music21.graph.plot.PlotStreamMixin.setAxisKeywords") |

## PlotStreamMixin

class music21.graph.plot.PlotStreamMixin(*streamObj=None*, *recurse=True*, *\*\*keywords*)[[source]](../_modules/music21/graph/plot.html#PlotStreamMixin)
:   This Mixin adds Stream extracting and Axis holding features to any
    class derived from Graph.

[`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin") bases

* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin") read-only properties

PlotStreamMixin.allAxes
:   return a list of axisX, axisY, axisZ if any are defined in the class.

    Some might be None.

    ```python
    >>> s = stream.Stream()
    >>> p = graph.plot.ScatterPitchClassOffset(s)
    >>> p.allAxes
    [<music21.graph.axis.OffsetAxis: x axis for ScatterPitchClassOffset>,
     <music21.graph.axis.PitchClassAxis: y axis for ScatterPitchClassOffset>]
    ```

PlotStreamMixin.id
:   Each PlotStream has a unique id that consists of its class name and
    the class names of the axes:

    ```python
    >>> s = stream.Stream()
    >>> pScatter = graph.plot.ScatterPitchClassQuarterLength(s)
    >>> pScatter.id
    'scatter-quarterLength-pitchClass'
    ```

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin") methods

PlotStreamMixin.extractChordDataMultiAxis(*c*, *formatDict*)[[source]](../_modules/music21/graph/plot.html#PlotStreamMixin.extractChordDataMultiAxis)
:   Returns a list of lists of values for each axis.

static PlotStreamMixin.extractChordDataOneAxis(*ax*, *c*, *formatDict*)[[source]](../_modules/music21/graph/plot.html#PlotStreamMixin.extractChordDataOneAxis)
:   Look for Note-like attributes in a Chord. This is done by first
    looking at the Chord, and then, if attributes are not found, looking at each pitch.

    Returns a list of values.

PlotStreamMixin.extractData()[[source]](../_modules/music21/graph/plot.html#PlotStreamMixin.extractData)

static PlotStreamMixin.fillValueLists(*elementValues*, *nullFillValue=0*)[[source]](../_modules/music21/graph/plot.html#PlotStreamMixin.fillValueLists)
:   pads a list of lists so that each list has the same length.
    Pads with the first element of the list or nullFillValue if
    the list has no elements. Modifies in place so returns None

    Used by extractChordDataMultiAxis

    ```python
    >>> l0 = [2, 3, 4]
    >>> l1 = [10, 20, 30, 40, 50]
    >>> l2 = []
    >>> listOfLists = [l0, l1, l2]
    >>> graph.plot.PlotStream.fillValueLists(listOfLists)
    >>> listOfLists
    [[2,   3,  4,  2,  2],
     [10, 20, 30, 40, 50],
     [0,   0,  0,  0,  0]]
    ```

PlotStreamMixin.postProcessData()[[source]](../_modules/music21/graph/plot.html#PlotStreamMixin.postProcessData)
:   Call any post data processing routines here and on any axes.

PlotStreamMixin.postProcessElement(*el: [Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")*, *formatDict: [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)"), [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")]*, *\*values: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Real](https://docs.python.org/3/library/numbers.html#numbers.Real "(in Python v3.14)")]*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/graph/plot.html#PlotStreamMixin.postProcessElement)
:   Any processing that needs to take place for each element, independent
    of what the axis is finding can go here. For chords, a single
    formatDict applies to all pitches/notes in the chord.

PlotStreamMixin.processOneElement(*el: [Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")*)[[source]](../_modules/music21/graph/plot.html#PlotStreamMixin.processOneElement)
:   Get a list of data from a single element (generally a Note or chord):

    ```python
    >>> n = note.Note('C#4')
    >>> n.offset = 10.25
    >>> s = stream.Stream([n])
    >>> pl = graph.plot.ScatterPitchClassOffset(s)
    >>> pl.processOneElement(n)
    [(10.25, 1, {})]
    ```

    ```python
    >>> c = chord.Chord(['D4', 'E5'])
    >>> s.insert(5.0, c)
    >>> pl.processOneElement(c)
    [(5.0, 2, {}), (5.0, 4, {})]
    ```

PlotStreamMixin.run(*\**, *callProcess: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *\*\*keywords*)[[source]](../_modules/music21/graph/plot.html#PlotStreamMixin.run)
:   main routine to extract data, set axis labels, run process() on the underlying
    Graph object, and if self.doneAction is not None, either write or show the graph.

PlotStreamMixin.setAxisKeywords()[[source]](../_modules/music21/graph/plot.html#PlotStreamMixin.setAxisKeywords)
:   Configure axis parameters based on keywords given when creating the Plot.

    Looks in self.savedKeywords, in case any post creation manipulation needs
    to happen.

    Finds keywords that begin with x, y, z and sets the remainder of the
    keyword (lowercasing the first letter) as an attribute. Does not
    set any new attributes, only existing ones.

    ```python
    >>> b = corpus.parse('bwv66.6')
    >>> hist = graph.plot.HistogramPitchSpace(b, xHideUnused=False)
    >>> hist.axisX.hideUnused
    True
    >>> hist.setAxisKeywords()
    >>> hist.axisX.hideUnused
    False
    ```

## Scatter

class music21.graph.plot.Scatter(*streamObj=None*, *\*\*keywords*)[[source]](../_modules/music21/graph/plot.html#Scatter)
:   Base class for 2D scatter plots.

[`Scatter`](#music21.graph.plot.Scatter "music21.graph.plot.Scatter") bases

* [`GraphScatter`](moduleGraphPrimitives.html#music21.graph.primitives.GraphScatter "music21.graph.primitives.GraphScatter")
* [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph")
* [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`Scatter`](#music21.graph.plot.Scatter "music21.graph.plot.Scatter") read-only properties

Read-only properties inherited from [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin"):

|  |  |  |
| --- | --- | --- |
| * [`allAxes`](#music21.graph.plot.PlotStreamMixin.allAxes "music21.graph.plot.PlotStreamMixin.allAxes") | * [`id`](#music21.graph.plot.PlotStreamMixin.id "music21.graph.plot.PlotStreamMixin.id") |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`Scatter`](#music21.graph.plot.Scatter "music21.graph.plot.Scatter") read/write properties

Read/write properties inherited from [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph"):

|  |  |  |
| --- | --- | --- |
| * [`doneAction`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.doneAction "music21.graph.primitives.Graph.doneAction") |  |  |

[`Scatter`](#music21.graph.plot.Scatter "music21.graph.plot.Scatter") methods

Methods inherited from [`GraphScatter`](moduleGraphPrimitives.html#music21.graph.primitives.GraphScatter "music21.graph.primitives.GraphScatter"):

|  |  |  |
| --- | --- | --- |
| * [`renderSubplot()`](moduleGraphPrimitives.html#music21.graph.primitives.GraphScatter.renderSubplot "music21.graph.primitives.GraphScatter.renderSubplot") |  |  |

Methods inherited from [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph"):

|  |  |  |
| --- | --- | --- |
| * [`applyFormatting()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyFormatting "music21.graph.primitives.Graph.applyFormatting") * [`applyFormattingToOneAxis()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyFormattingToOneAxis "music21.graph.primitives.Graph.applyFormattingToOneAxis") * [`applyGrid()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyGrid "music21.graph.primitives.Graph.applyGrid") * [`callDoneAction()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.callDoneAction "music21.graph.primitives.Graph.callDoneAction") * [`hideAxisSpines()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.hideAxisSpines "music21.graph.primitives.Graph.hideAxisSpines") | * [`nextColor()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.nextColor "music21.graph.primitives.Graph.nextColor") * [`process()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.process "music21.graph.primitives.Graph.process") * [`setAxisLabel()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setAxisLabel "music21.graph.primitives.Graph.setAxisLabel") * [`setAxisRange()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setAxisRange "music21.graph.primitives.Graph.setAxisRange") | * [`setIntegerTicksFromData()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setIntegerTicksFromData "music21.graph.primitives.Graph.setIntegerTicksFromData") * [`setTicks()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setTicks "music21.graph.primitives.Graph.setTicks") * [`show()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.show "music21.graph.primitives.Graph.show") * [`write()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.write "music21.graph.primitives.Graph.write") |

Methods inherited from [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin"):

|  |  |  |
| --- | --- | --- |
| * [`extractChordDataMultiAxis()`](#music21.graph.plot.PlotStreamMixin.extractChordDataMultiAxis "music21.graph.plot.PlotStreamMixin.extractChordDataMultiAxis") * [`extractChordDataOneAxis()`](#music21.graph.plot.PlotStreamMixin.extractChordDataOneAxis "music21.graph.plot.PlotStreamMixin.extractChordDataOneAxis") * [`extractData()`](#music21.graph.plot.PlotStreamMixin.extractData "music21.graph.plot.PlotStreamMixin.extractData") | * [`fillValueLists()`](#music21.graph.plot.PlotStreamMixin.fillValueLists "music21.graph.plot.PlotStreamMixin.fillValueLists") * [`postProcessData()`](#music21.graph.plot.PlotStreamMixin.postProcessData "music21.graph.plot.PlotStreamMixin.postProcessData") * [`postProcessElement()`](#music21.graph.plot.PlotStreamMixin.postProcessElement "music21.graph.plot.PlotStreamMixin.postProcessElement") | * [`processOneElement()`](#music21.graph.plot.PlotStreamMixin.processOneElement "music21.graph.plot.PlotStreamMixin.processOneElement") * [`run()`](#music21.graph.plot.PlotStreamMixin.run "music21.graph.plot.PlotStreamMixin.run") * [`setAxisKeywords()`](#music21.graph.plot.PlotStreamMixin.setAxisKeywords "music21.graph.plot.PlotStreamMixin.setAxisKeywords") |

## ScatterWeighted

class music21.graph.plot.ScatterWeighted(*streamObj=None*, *\*\*keywords*)[[source]](../_modules/music21/graph/plot.html#ScatterWeighted)
:   Base class for histograms that plot one axis against its count.

    The count is stored as the Z axis, though it is represented as size.

[`ScatterWeighted`](#music21.graph.plot.ScatterWeighted "music21.graph.plot.ScatterWeighted") bases

* [`GraphScatterWeighted`](moduleGraphPrimitives.html#music21.graph.primitives.GraphScatterWeighted "music21.graph.primitives.GraphScatterWeighted")
* [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph")
* [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`ScatterWeighted`](#music21.graph.plot.ScatterWeighted "music21.graph.plot.ScatterWeighted") read-only properties

Read-only properties inherited from [`GraphScatterWeighted`](moduleGraphPrimitives.html#music21.graph.primitives.GraphScatterWeighted "music21.graph.primitives.GraphScatterWeighted"):

|  |  |  |
| --- | --- | --- |
| * [`rangeDiameter`](moduleGraphPrimitives.html#music21.graph.primitives.GraphScatterWeighted.rangeDiameter "music21.graph.primitives.GraphScatterWeighted.rangeDiameter") |  |  |

Read-only properties inherited from [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin"):

|  |  |  |
| --- | --- | --- |
| * [`allAxes`](#music21.graph.plot.PlotStreamMixin.allAxes "music21.graph.plot.PlotStreamMixin.allAxes") | * [`id`](#music21.graph.plot.PlotStreamMixin.id "music21.graph.plot.PlotStreamMixin.id") |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`ScatterWeighted`](#music21.graph.plot.ScatterWeighted "music21.graph.plot.ScatterWeighted") read/write properties

Read/write properties inherited from [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph"):

|  |  |  |
| --- | --- | --- |
| * [`doneAction`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.doneAction "music21.graph.primitives.Graph.doneAction") |  |  |

[`ScatterWeighted`](#music21.graph.plot.ScatterWeighted "music21.graph.plot.ScatterWeighted") methods

Methods inherited from [`GraphScatterWeighted`](moduleGraphPrimitives.html#music21.graph.primitives.GraphScatterWeighted "music21.graph.primitives.GraphScatterWeighted"):

|  |  |  |
| --- | --- | --- |
| * [`renderSubplot()`](moduleGraphPrimitives.html#music21.graph.primitives.GraphScatterWeighted.renderSubplot "music21.graph.primitives.GraphScatterWeighted.renderSubplot") |  |  |

Methods inherited from [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph"):

|  |  |  |
| --- | --- | --- |
| * [`applyFormatting()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyFormatting "music21.graph.primitives.Graph.applyFormatting") * [`applyFormattingToOneAxis()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyFormattingToOneAxis "music21.graph.primitives.Graph.applyFormattingToOneAxis") * [`applyGrid()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyGrid "music21.graph.primitives.Graph.applyGrid") * [`callDoneAction()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.callDoneAction "music21.graph.primitives.Graph.callDoneAction") * [`hideAxisSpines()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.hideAxisSpines "music21.graph.primitives.Graph.hideAxisSpines") | * [`nextColor()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.nextColor "music21.graph.primitives.Graph.nextColor") * [`process()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.process "music21.graph.primitives.Graph.process") * [`setAxisLabel()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setAxisLabel "music21.graph.primitives.Graph.setAxisLabel") * [`setAxisRange()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setAxisRange "music21.graph.primitives.Graph.setAxisRange") | * [`setIntegerTicksFromData()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setIntegerTicksFromData "music21.graph.primitives.Graph.setIntegerTicksFromData") * [`setTicks()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setTicks "music21.graph.primitives.Graph.setTicks") * [`show()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.show "music21.graph.primitives.Graph.show") * [`write()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.write "music21.graph.primitives.Graph.write") |

Methods inherited from [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin"):

|  |  |  |
| --- | --- | --- |
| * [`extractChordDataMultiAxis()`](#music21.graph.plot.PlotStreamMixin.extractChordDataMultiAxis "music21.graph.plot.PlotStreamMixin.extractChordDataMultiAxis") * [`extractChordDataOneAxis()`](#music21.graph.plot.PlotStreamMixin.extractChordDataOneAxis "music21.graph.plot.PlotStreamMixin.extractChordDataOneAxis") * [`extractData()`](#music21.graph.plot.PlotStreamMixin.extractData "music21.graph.plot.PlotStreamMixin.extractData") | * [`fillValueLists()`](#music21.graph.plot.PlotStreamMixin.fillValueLists "music21.graph.plot.PlotStreamMixin.fillValueLists") * [`postProcessData()`](#music21.graph.plot.PlotStreamMixin.postProcessData "music21.graph.plot.PlotStreamMixin.postProcessData") * [`postProcessElement()`](#music21.graph.plot.PlotStreamMixin.postProcessElement "music21.graph.plot.PlotStreamMixin.postProcessElement") | * [`processOneElement()`](#music21.graph.plot.PlotStreamMixin.processOneElement "music21.graph.plot.PlotStreamMixin.processOneElement") * [`run()`](#music21.graph.plot.PlotStreamMixin.run "music21.graph.plot.PlotStreamMixin.run") * [`setAxisKeywords()`](#music21.graph.plot.PlotStreamMixin.setAxisKeywords "music21.graph.plot.PlotStreamMixin.setAxisKeywords") |

[`ScatterWeighted`](#music21.graph.plot.ScatterWeighted "music21.graph.plot.ScatterWeighted") instance variables

Instance variables inherited from [`GraphScatterWeighted`](moduleGraphPrimitives.html#music21.graph.primitives.GraphScatterWeighted "music21.graph.primitives.GraphScatterWeighted"):

|  |  |  |
| --- | --- | --- |
| * [`maxDiameter`](moduleGraphPrimitives.html#music21.graph.primitives.GraphScatterWeighted.maxDiameter "music21.graph.primitives.GraphScatterWeighted.maxDiameter") | * [`minDiameter`](moduleGraphPrimitives.html#music21.graph.primitives.GraphScatterWeighted.minDiameter "music21.graph.primitives.GraphScatterWeighted.minDiameter") |  |

## WindowedAnalysis

class music21.graph.plot.WindowedAnalysis(*streamObj=None*, *\*\*keywords*)[[source]](../_modules/music21/graph/plot.html#WindowedAnalysis)
:   Base Plot for windowed analysis routines such as Key Analysis or Ambitus.

[`WindowedAnalysis`](#music21.graph.plot.WindowedAnalysis "music21.graph.plot.WindowedAnalysis") bases

* [`GraphColorGrid`](moduleGraphPrimitives.html#music21.graph.primitives.GraphColorGrid "music21.graph.primitives.GraphColorGrid")
* [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph")
* [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`WindowedAnalysis`](#music21.graph.plot.WindowedAnalysis "music21.graph.plot.WindowedAnalysis") read-only properties

WindowedAnalysis.processor

Read-only properties inherited from [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin"):

|  |  |  |
| --- | --- | --- |
| * [`allAxes`](#music21.graph.plot.PlotStreamMixin.allAxes "music21.graph.plot.PlotStreamMixin.allAxes") | * [`id`](#music21.graph.plot.PlotStreamMixin.id "music21.graph.plot.PlotStreamMixin.id") |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`WindowedAnalysis`](#music21.graph.plot.WindowedAnalysis "music21.graph.plot.WindowedAnalysis") read/write properties

Read/write properties inherited from [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph"):

|  |  |  |
| --- | --- | --- |
| * [`doneAction`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.doneAction "music21.graph.primitives.Graph.doneAction") |  |  |

[`WindowedAnalysis`](#music21.graph.plot.WindowedAnalysis "music21.graph.plot.WindowedAnalysis") methods

WindowedAnalysis.extractData()[[source]](../_modules/music21/graph/plot.html#WindowedAnalysis.extractData)
:   Extract data actually calls the processing routine.

    Returns two element tuple of the data (colorMatrix) and the yTicks list

WindowedAnalysis.run(*\**, *callProcess: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *\*\*keywords*)[[source]](../_modules/music21/graph/plot.html#WindowedAnalysis.run)
:   Actually creates the graph.

WindowedAnalysis.write(*fp=None*)[[source]](../_modules/music21/graph/plot.html#WindowedAnalysis.write)
:   Overrides the normal write method here to add a legend.

Methods inherited from [`GraphColorGrid`](moduleGraphPrimitives.html#music21.graph.primitives.GraphColorGrid "music21.graph.primitives.GraphColorGrid"):

|  |  |  |
| --- | --- | --- |
| * [`renderSubplot()`](moduleGraphPrimitives.html#music21.graph.primitives.GraphColorGrid.renderSubplot "music21.graph.primitives.GraphColorGrid.renderSubplot") |  |  |

Methods inherited from [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph"):

|  |  |  |
| --- | --- | --- |
| * [`applyFormatting()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyFormatting "music21.graph.primitives.Graph.applyFormatting") * [`applyFormattingToOneAxis()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyFormattingToOneAxis "music21.graph.primitives.Graph.applyFormattingToOneAxis") * [`applyGrid()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.applyGrid "music21.graph.primitives.Graph.applyGrid") * [`callDoneAction()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.callDoneAction "music21.graph.primitives.Graph.callDoneAction") | * [`hideAxisSpines()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.hideAxisSpines "music21.graph.primitives.Graph.hideAxisSpines") * [`nextColor()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.nextColor "music21.graph.primitives.Graph.nextColor") * [`process()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.process "music21.graph.primitives.Graph.process") * [`setAxisLabel()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setAxisLabel "music21.graph.primitives.Graph.setAxisLabel") | * [`setAxisRange()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setAxisRange "music21.graph.primitives.Graph.setAxisRange") * [`setIntegerTicksFromData()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setIntegerTicksFromData "music21.graph.primitives.Graph.setIntegerTicksFromData") * [`setTicks()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.setTicks "music21.graph.primitives.Graph.setTicks") * [`show()`](moduleGraphPrimitives.html#music21.graph.primitives.Graph.show "music21.graph.primitives.Graph.show") |

Methods inherited from [`PlotStreamMixin`](#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin"):

|  |  |  |
| --- | --- | --- |
| * [`extractChordDataMultiAxis()`](#music21.graph.plot.PlotStreamMixin.extractChordDataMultiAxis "music21.graph.plot.PlotStreamMixin.extractChordDataMultiAxis") * [`extractChordDataOneAxis()`](#music21.graph.plot.PlotStreamMixin.extractChordDataOneAxis "music21.graph.plot.PlotStreamMixin.extractChordDataOneAxis") * [`fillValueLists()`](#music21.graph.plot.PlotStreamMixin.fillValueLists "music21.graph.plot.PlotStreamMixin.fillValueLists") | * [`postProcessData()`](#music21.graph.plot.PlotStreamMixin.postProcessData "music21.graph.plot.PlotStreamMixin.postProcessData") * [`postProcessElement()`](#music21.graph.plot.PlotStreamMixin.postProcessElement "music21.graph.plot.PlotStreamMixin.postProcessElement") | * [`processOneElement()`](#music21.graph.plot.PlotStreamMixin.processOneElement "music21.graph.plot.PlotStreamMixin.processOneElement") * [`setAxisKeywords()`](#music21.graph.plot.PlotStreamMixin.setAxisKeywords "music21.graph.plot.PlotStreamMixin.setAxisKeywords") |

[`WindowedAnalysis`](#music21.graph.plot.WindowedAnalysis "music21.graph.plot.WindowedAnalysis") instance variables

Instance variables inherited from [`GraphColorGrid`](moduleGraphPrimitives.html#music21.graph.primitives.GraphColorGrid "music21.graph.primitives.GraphColorGrid"):

|  |  |  |
| --- | --- | --- |
| * [`hideLeftBottomSpines`](moduleGraphPrimitives.html#music21.graph.primitives.GraphColorGrid.hideLeftBottomSpines "music21.graph.primitives.GraphColorGrid.hideLeftBottomSpines") |  |  |
