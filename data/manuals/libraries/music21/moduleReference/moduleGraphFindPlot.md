Source: https://music21.org/music21docs/moduleReference/moduleGraphFindPlot.html

# music21.graph.findPlot

Functions that find appropriate plots for graph.plot.

## Functions

music21.graph.findPlot.axisMatchesValue(*axisClass: [type](moduleBar.html#music21.bar.Barline.type "music21.bar.Barline.type")[[Axis](moduleGraphAxis.html#music21.graph.axis.Axis "music21.graph.axis.Axis")] | [Axis](moduleGraphAxis.html#music21.graph.axis.Axis "music21.graph.axis.Axis")*, *axisValue: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/graph/findPlot.html#axisMatchesValue)
:   Returns Bool about whether axisValue.lower() is anywhere in axisClass.quantities

    ```python
    >>> ax = graph.axis.CountingAxis
    >>> graph.findPlot.axisMatchesValue(ax, 'counting')
    True
    >>> graph.findPlot.axisMatchesValue(ax, 'count')
    True
    >>> graph.findPlot.axisMatchesValue(ax, 'offset')
    False
    ```

    Works on an instantiated object as well:

    ```python
    >>> ax = graph.axis.CountingAxis()
    >>> graph.findPlot.axisMatchesValue(ax, 'counting')
    True
    >>> graph.findPlot.axisMatchesValue(ax, 'flute')
    False
    ```

    * Changed in v8: Must send a subclass of axis.Axis or an instance.
      :   None is no longer supported.

music21.graph.findPlot.getAxisClassFromValue(*axisValue: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [type](moduleBar.html#music21.bar.Barline.type "music21.bar.Barline.type")[[Axis](moduleGraphAxis.html#music21.graph.axis.Axis "music21.graph.axis.Axis")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/graph/findPlot.html#getAxisClassFromValue)
:   given an axis value return the single best axis for the value, or None

    uses Axis.quantities

    ```python
    >>> getAxis = graph.findPlot.getAxisClassFromValue
    ```

    ```python
    >>> getAxis('counting')
    <class 'music21.graph.axis.CountingAxis'>
    ```

    ```python
    >>> getAxis('pc')
    <class 'music21.graph.axis.PitchClassAxis'>
    ```

    ```python
    >>> print(getAxis('boogie'))
    None
    ```

music21.graph.findPlot.getAxisClasses() → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[type](moduleBar.html#music21.bar.Barline.type "music21.bar.Barline.type")[[Axis](moduleGraphAxis.html#music21.graph.axis.Axis "music21.graph.axis.Axis")]][[source]](../_modules/music21/graph/findPlot.html#getAxisClasses)
:   return a list of all Axis subclasses. Returns a list sorted by name

    ```python
    >>> graph.findPlot.getAxisClasses()
    [<class 'music21.graph.axis.Axis'>,
     <class 'music21.graph.axis.CountingAxis'>,
     <class 'music21.graph.axis.DynamicsAxis'>,
     <class 'music21.graph.axis.OffsetAxis'>,
     ...]
    ```

music21.graph.findPlot.getAxisQuantities(*synonyms=False*, *axesToCheck=None*)[[source]](../_modules/music21/graph/findPlot.html#getAxisQuantities)
:   ```python
    >>> graph.findPlot.getAxisQuantities()
    ['generic', 'count', 'dynamic', 'offset', 'offsetEnd',
     'pitchGeneric', 'pitchClass', 'pitchSpace', 'octave', 'position', 'quarterLength']
    ```

    ```python
    >>> graph.findPlot.getAxisQuantities(synonyms=True)
    ['generic', 'one', 'nothing', 'blank', 'count', 'quantity', 'frequency', ...]
    ```

    ```python
    >>> theseAxes = [graph.axis.CountingAxis, graph.axis.OffsetAxis]
    >>> graph.findPlot.getAxisQuantities(axesToCheck=theseAxes)
    ['count', 'offset']
    ```

    ```python
    >>> graph.findPlot.getAxisQuantities(True, axesToCheck=theseAxes)
    ['count', 'quantity', 'frequency', 'counting',
     'offset', 'measure', 'offsets', 'measures', 'time']
    ```

music21.graph.findPlot.getPlotClasses() → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[type](moduleBar.html#music21.bar.Barline.type "music21.bar.Barline.type")[[PlotStreamMixin](moduleGraphPlot.html#music21.graph.plot.PlotStreamMixin "music21.graph.plot.PlotStreamMixin")]][[source]](../_modules/music21/graph/findPlot.html#getPlotClasses)
:   return a list of all PlotStreamMixin subclasses. Returns a list sorted by name

    ```python
    >>> graph.findPlot.getPlotClasses()
    [<class 'music21.graph.plot.Dolan'>,
     <class 'music21.graph.plot.Features'>,
     <class 'music21.graph.plot.Histogram'>,
     <class 'music21.graph.plot.HistogramPitchClass'>,
     <class 'music21.graph.plot.HistogramPitchSpace'>,
     ...]
    ```

music21.graph.findPlot.getPlotClassesFromFormat(*graphFormat*, *checkPlotClasses=None*)[[source]](../_modules/music21/graph/findPlot.html#getPlotClassesFromFormat)
:   Given a graphFormat, find a list of plots that match:

    ```python
    >>> graph.findPlot.getPlotClassesFromFormat('scatterweighted')
    [<class 'music21.graph.plot.ScatterWeighted'>,
     <class 'music21.graph.plot.ScatterWeightedPitchClassQuarterLength'>,
     <class 'music21.graph.plot.ScatterWeightedPitchSpaceDynamicSymbol'>,
     <class 'music21.graph.plot.ScatterWeightedPitchSpaceQuarterLength'>]
    ```

    Or give a list of plot classes to check:

    ```python
    >>> pcs = [graph.plot.ScatterWeighted, graph.plot.Dolan]
    >>> graph.findPlot.getPlotClassesFromFormat('scatterweighted', pcs)
    [<class 'music21.graph.plot.ScatterWeighted'>]
    ```

music21.graph.findPlot.getPlotsToMake(*graphFormat: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *xValue=None*, *yValue=None*, *zValue=None*)[[source]](../_modules/music21/graph/findPlot.html#getPlotsToMake)
:   Returns either a list of plot classes to make if there is a predetermined class

    or a list of tuples where the first element of each tuple is the plot class
    and the second is a dict of {‘x’: axisXClass, ‘y’: axisYClass} etc.

    Default is pianoroll

    ```python
    >>> graph.findPlot.getPlotsToMake()
    [<class 'music21.graph.plot.HorizontalBarPitchSpaceOffset'>]
    ```

    ```python
    >>> graph.findPlot.getPlotsToMake('scatter')
    [<class 'music21.graph.plot.Scatter'>,
     <class 'music21.graph.plot.ScatterPitchClassOffset'>,
     <class 'music21.graph.plot.ScatterPitchClassQuarterLength'>,
     <class 'music21.graph.plot.ScatterPitchSpaceDynamicSymbol'>,
     <class 'music21.graph.plot.ScatterPitchSpaceQuarterLength'>]
    ```

    ```python
    >>> graph.findPlot.getPlotsToMake('scatter', 'offset', 'pitchClass')
    [<class 'music21.graph.plot.ScatterPitchClassOffset'>]
    ```

    Try in wrong order:

    ```python
    >>> graph.findPlot.getPlotsToMake('scatter', 'pitchClass', 'offset')
    [<class 'music21.graph.plot.ScatterPitchClassOffset'>]
    ```

    Try giving just one value:

    ```python
    >>> graph.findPlot.getPlotsToMake('scatter', 'offset')
    [<class 'music21.graph.plot.ScatterPitchClassOffset'>]
    ```

    ```python
    >>> graph.findPlot.getPlotsToMake('scatter', 'ql')  # abbreviation
    [<class 'music21.graph.plot.ScatterPitchClassQuarterLength'>,
     <class 'music21.graph.plot.ScatterPitchSpaceQuarterLength'>]
    ```

    Just one value, but it is in the wrong axis:

    ```python
    >>> graph.findPlot.getPlotsToMake('scatter', 'pitchClass')
    [<class 'music21.graph.plot.ScatterPitchClassOffset'>,
     <class 'music21.graph.plot.ScatterPitchClassQuarterLength'>]
    ```

    Create a graph that does not exist:

    ```python
    >>> graph.findPlot.getPlotsToMake('scatter', 'offset', 'dynamics')
    [(<class 'music21.graph.plot.Scatter'>,
      OrderedDict([('x', <class 'music21.graph.axis.OffsetAxis'>),
                   ('y', <class 'music21.graph.axis.DynamicsAxis'>)]))]
    ```

    Just a couple of values:

    ```python
    >>> graph.findPlot.getPlotsToMake('offset', 'dynamics')
    [(<class 'music21.graph.plot.Scatter'>,
      OrderedDict([('x', <class 'music21.graph.axis.OffsetAxis'>),
                   ('y', <class 'music21.graph.axis.DynamicsAxis'>)]))]
    ```

    Just one value:

    ```python
    >>> graph.findPlot.getPlotsToMake('octave')
    [(<class 'music21.graph.plot.Histogram'>,
      OrderedDict([('x', <class 'music21.graph.axis.PitchSpaceOctaveAxis'>)]))]
    ```

    Three values:

    ```python
    >>> graph.findPlot.getPlotsToMake('offset', 'dynamics', 'count')
    [(<class 'music21.graph.plot.ScatterWeighted'>,
      OrderedDict([('x', <class 'music21.graph.axis.OffsetAxis'>),
                   ('y', <class 'music21.graph.axis.DynamicsAxis'>),
                   ('z', <class 'music21.graph.axis.CountingAxis'>)]))]
    ```

music21.graph.findPlot.userFormatsToFormat(*userFormat*)[[source]](../_modules/music21/graph/findPlot.html#userFormatsToFormat)
:   Replace possible user format strings with defined format names as used herein.
    Returns string unaltered if no match.

    ```python
    >>> graph.findPlot.userFormatsToFormat('horizontal')
    'horizontalbar'
    >>> graph.findPlot.userFormatsToFormat('Weighted Scatter')
    'scatterweighted'
    >>> graph.findPlot.userFormatsToFormat('3D')
    '3dbars'
    ```

    Unknown formats pass through unaltered.

    ```python
    >>> graph.findPlot.userFormatsToFormat('4D super chart')
    '4dsuperchart'
    ```
