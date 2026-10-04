Source: https://music21.org/music21docs/moduleReference/moduleGraph.html

# music21.graph

Tools for graphing, plotting, or otherwise visualizing `Stream` objects.

The easiest and most common way of using plotting functions is to call
.plot(‘typeOfGraph’) on a Stream. See `plot()`.
That method uses tools from the music21.graph.findPlot module to map between
names of plots and classes that can show them.

The [`PlotStream`](moduleGraphPlot.html#music21.graph.plot.PlotStream "music21.graph.plot.PlotStream")
subclasses in the music21.graph.plot module give easy to use
and configurable ways of graphing data and structures in
`Stream` objects. These Plot objects use classes from
the music21.graph.axis module to automatically extract relevant data for you.

At a lower level, the [`Graph`](moduleGraphPrimitives.html#music21.graph.primitives.Graph "music21.graph.primitives.Graph") subclasses
in the music21.graph.primitives modules give abstract fundamental
graphing archetypes using the matplotlib library. They are to be used when
you already have data extracted on your own but still want to take advantage
of musically-aware axes and scaling.

From highest level to lowest level usage, ways of graphing are as follows:

> 1. streamObj.plot(‘graphName’)
> 2. graph.plot.Class(streamObj).run()
> 3. plotter = graph.primitives.Class(); plotter.data = …; plotter.process()
> 4. Use matplotlib directly to create any graph, musical or non-musical.

## Functions

music21.graph.plotStream(*streamObj: stream.Stream*, *graphFormat: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *xValue=None*, *yValue=None*, *zValue=None*, *\*\*keywords*)[[source]](../_modules/music21/graph.html#plotStream)
:   Given a stream and any keyword configuration arguments, create and display a plot.

    Note: plots require matplotlib to be installed.

    Plot methods can be specified as additional arguments or by keyword.
    Two keyword arguments can be given: format and values.
    If positional arguments are given, the first is taken as format
    and the rest are collected as values. If format is the class
    name, that class is collected. Additionally, every
    `PlotStream` subclass defines one format
    string and a list of values strings. The format parameter
    defines the type of Graph (e.g. scatter, histogram, colorGrid). The
    values list defines what values are graphed
    (e.g. quarterLength, pitch, pitchClass).

    If a user provides a format and one or more values strings, a plot with
    the corresponding profile, if found, will be generated. If not, the first
    Plot to match any of the defined specifiers will be created.

    In the case of `PlotWindowedAnalysis` subclasses,
    the [`DiscreteAnalysis`](moduleAnalysisDiscrete.html#music21.analysis.discrete.DiscreteAnalysis "music21.analysis.discrete.DiscreteAnalysis")
    subclass `identifiers` list
    is added to the Plot’s values list.

    Available plots include the following:

    * [`HistogramPitchSpace`](moduleGraphPlot.html#music21.graph.plot.HistogramPitchSpace "music21.graph.plot.HistogramPitchSpace")
    * [`HistogramPitchClass`](moduleGraphPlot.html#music21.graph.plot.HistogramPitchClass "music21.graph.plot.HistogramPitchClass")
    * [`HistogramQuarterLength`](moduleGraphPlot.html#music21.graph.plot.HistogramQuarterLength "music21.graph.plot.HistogramQuarterLength")
    * [`ScatterPitchSpaceQuarterLength`](moduleGraphPlot.html#music21.graph.plot.ScatterPitchSpaceQuarterLength "music21.graph.plot.ScatterPitchSpaceQuarterLength")
    * [`ScatterPitchClassQuarterLength`](moduleGraphPlot.html#music21.graph.plot.ScatterPitchClassQuarterLength "music21.graph.plot.ScatterPitchClassQuarterLength")
    * [`ScatterPitchClassOffset`](moduleGraphPlot.html#music21.graph.plot.ScatterPitchClassOffset "music21.graph.plot.ScatterPitchClassOffset")
    * [`ScatterPitchSpaceDynamicSymbol`](moduleGraphPlot.html#music21.graph.plot.ScatterPitchSpaceDynamicSymbol "music21.graph.plot.ScatterPitchSpaceDynamicSymbol")
    * [`HorizontalBarPitchSpaceOffset`](moduleGraphPlot.html#music21.graph.plot.HorizontalBarPitchSpaceOffset "music21.graph.plot.HorizontalBarPitchSpaceOffset")
    * [`HorizontalBarPitchClassOffset`](moduleGraphPlot.html#music21.graph.plot.HorizontalBarPitchClassOffset "music21.graph.plot.HorizontalBarPitchClassOffset")
    * [`ScatterWeightedPitchSpaceQuarterLength`](moduleGraphPlot.html#music21.graph.plot.ScatterWeightedPitchSpaceQuarterLength "music21.graph.plot.ScatterWeightedPitchSpaceQuarterLength")
    * [`ScatterWeightedPitchClassQuarterLength`](moduleGraphPlot.html#music21.graph.plot.ScatterWeightedPitchClassQuarterLength "music21.graph.plot.ScatterWeightedPitchClassQuarterLength")
    * [`ScatterWeightedPitchSpaceDynamicSymbol`](moduleGraphPlot.html#music21.graph.plot.ScatterWeightedPitchSpaceDynamicSymbol "music21.graph.plot.ScatterWeightedPitchSpaceDynamicSymbol")
    * [`Plot3DBarsPitchSpaceQuarterLength`](moduleGraphPlot.html#music21.graph.plot.Plot3DBarsPitchSpaceQuarterLength "music21.graph.plot.Plot3DBarsPitchSpaceQuarterLength")
    * [`WindowedKey`](moduleGraphPlot.html#music21.graph.plot.WindowedKey "music21.graph.plot.WindowedKey")
    * [`WindowedAmbitus`](moduleGraphPlot.html#music21.graph.plot.WindowedAmbitus "music21.graph.plot.WindowedAmbitus")
    * [`Dolan`](moduleGraphPlot.html#music21.graph.plot.Dolan "music21.graph.plot.Dolan")

    ```python
    >>> s = corpus.parse('bach/bwv57.8')
    >>> thePlot = s.plot('histogram', 'pitch')
    ```

    [![../_images/HistogramPitchSpace.png](../_images/HistogramPitchSpace.png)](../_images/HistogramPitchSpace.png)

    ```python
    >>> s = corpus.parse('bach/bwv57.8')
    >>> thePlot = s.plot('pianoroll')
    ```

    [![../_images/HorizontalBarPitchSpaceOffset.png](../_images/HorizontalBarPitchSpaceOffset.png)](../_images/HorizontalBarPitchSpaceOffset.png)
