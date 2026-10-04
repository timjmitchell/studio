Source: https://music21.org/music21docs/moduleReference/moduleGraphPrimitives.html

# music21.graph.primitives

Object definitions for graphing and plotting `Stream` objects.

The [`Graph`](#music21.graph.primitives.Graph "music21.graph.primitives.Graph") object subclasses primitive,
abstract fundamental graphing archetypes using the matplotlib library.

From the highest level to the lowest level of usage, ways of graphing are as follows:

> 1. streamObj.plot(‘graphName’)
> 2. graph.plot.Class(streamObj).run()
> 3. plotter = graph.primitives.Class(); plotter.data = …; plotter.process()
> 4. Use matplotlib directly to create your graph.

## Graph

class music21.graph.primitives.Graph(*\*\*keywords*)[[source]](../_modules/music21/graph/primitives.html#Graph)
:   A music21.graph.primitives.Graph is an object that represents a visual graph or
    plot, automating the creation and configuration of this graph in matplotlib.
    It is a low-level object that most music21 users do not need to call directly;
    yet, as most graphs will take keyword arguments that specify the
    look of graphs, they are important to know about.

    The keyword arguments can be provided for configuration are:

    * doneAction (see below)
    * alpha (which describes how transparent elements of the graph are)
    * dpi
    * colorBackgroundData
    * colorBackgroundFigure
    * colorGrid,
    * title (a string)
    * figureSize (a tuple of two ints)
    * colors (a list of colors to cycle through)
    * tickFontSize
    * tickColors (a dict of ‘x’: ‘#color’, ‘y’: ‘#color’)
    * titleFontSize
    * labelFontSize
    * fontFamily
    * hideXGrid
    * hideYGrid
    * xTickLabelRotation
    * marker
    * markersize

    Graph objects do not manipulate Streams or other music21 data; they only
    manipulate raw data formatted for each Graph subclass, hence it is
    unlikely that users will call this class directly.

    The doneAction argument determines what happens after the graph
    has been processed. Currently, there are three options, ‘write’ creates
    a file on disk (this is the default), while ‘show’ opens an
    interactive GUI browser. The
    third option, None, does the processing but does not write any output.

    figureSize:

    > A two-element iterable.
    >
    > Scales all graph components but because of matplotlib limitations
    > (esp. on 3d graphs) no all labels scale properly.
    >
    > defaults to .figureSizeDefault

    ```python
    >>> a = graph.primitives.Graph(title='a graph of some data to be given soon', tickFontSize=9)
    >>> a.data = [[0, 2], [1, 3]]
    >>> a.graphType
    'genericGraph'
    ```

[`Graph`](#music21.graph.primitives.Graph "music21.graph.primitives.Graph") bases

* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`Graph`](#music21.graph.primitives.Graph "music21.graph.primitives.Graph") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`Graph`](#music21.graph.primitives.Graph "music21.graph.primitives.Graph") read/write properties

Graph.doneAction
:   returns or sets what should happen when the graph is created (see docs above)
    default is ‘write’.

[`Graph`](#music21.graph.primitives.Graph "music21.graph.primitives.Graph") methods

Graph.applyFormatting(*subplot: [matplotlib.axes.Axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "(in Matplotlib v3.10.9)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/graph/primitives.html#Graph.applyFormatting)
:   Apply formatting to the Subplot (Axes) container and Figure instance.

    ax should be an AxesSubplot object or
    an Axes3D object or something similar.

Graph.applyFormattingToOneAxis(*subplot: [matplotlib.axes.Axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "(in Matplotlib v3.10.9)")*, *axis: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/graph/primitives.html#Graph.applyFormattingToOneAxis)
:   Given a matplotlib.Axes object (a subplot) and a string of
    ‘x’, ‘y’, or ‘z’, set the Axes object’s xlim (or ylim or zlim or xlim3d, etc.) from
    self.axis[axis][‘range’], Set the label from self.axis[axis][‘label’],
    the scale, the ticks, and the ticklabels.

    Returns the matplotlib Axis object that has been modified

Graph.applyGrid(*subplot: [matplotlib.axes.Axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "(in Matplotlib v3.10.9)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/graph/primitives.html#Graph.applyGrid)
:   Apply the Grid to the subplot such that it goes below the data.

Graph.callDoneAction(*fp: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/graph/primitives.html#Graph.callDoneAction)
:   Implement the desired doneAction, after data processing

static Graph.hideAxisSpines(*subplot: [matplotlib.axes.Axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "(in Matplotlib v3.10.9)")*, *leftBottom: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/graph/primitives.html#Graph.hideAxisSpines)
:   Remove the right and top spines from the diagram.

    If leftBottom is True, remove the left and bottom spines as well.

    Spines are removed by setting their colors to ‘none’ and every other
    tick line set\_visible to False.

Graph.nextColor() → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](../_modules/music21/graph/primitives.html#Graph.nextColor)
:   Utility function that cycles through the colors of self.colors.

    ```python
    >>> g = graph.primitives.Graph()
    >>> g.colors = ['#605c7f', '#5c7f60', '#715c7f']
    ```

    ```python
    >>> g.nextColor()
    '#605c7f'
    ```

    ```python
    >>> g.nextColor()
    '#5c7f60'
    ```

    ```python
    >>> g.nextColor()
    '#715c7f'
    ```

    ```python
    >>> g.nextColor()
    '#605c7f'
    ```

Graph.process() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/graph/primitives.html#Graph.process)
:   Creates the figure and subplot, calls renderSubplot to get the
    subclass specific information on the data, runs hideAxisSpines,
    applyFormatting, and then calls the done action. Returns None,
    but the subplot is available at self.subplot

Graph.renderSubplot(*subplot: [matplotlib.axes.Axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "(in Matplotlib v3.10.9)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/graph/primitives.html#Graph.renderSubplot)
:   Calls the subclass specific information to get the data

Graph.setAxisLabel(*axisKey: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *label: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *conditional: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/graph/primitives.html#Graph.setAxisLabel)

Graph.setAxisRange(*axisKey: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *valueRange: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")]*, *paddingFraction: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") = 0.1*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/graph/primitives.html#Graph.setAxisRange)
:   Set the range for the axis for a given axis key
    (generally, ‘x’, or ‘y’)

    ValueRange is a two-element tuple of the lowest
    number and the highest.

    By default, there is a padding of 10% of the range
    in either direction. Set paddingFraction = 0 to
    eliminate this shift

Graph.setIntegerTicksFromData(*unsortedData: [Sequence](https://docs.python.org/3/library/typing.html#typing.Sequence "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")]*, *axisKey: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = 'y'*, *dataSteps: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 8*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/graph/primitives.html#Graph.setIntegerTicksFromData)
:   Set the ticks for an axis (usually ‘y’) given unsorted data.

    Data steps shows how many ticks to make from the data.

    ```python
    >>> g = graph.primitives.GraphHorizontalBar()
    >>> g.setIntegerTicksFromData([10, 5, 3, 8, 20, 11], dataSteps=4)
    >>> g.axis['y']['ticks']
    ([0, 5, 10, 15, 20], ['0', '5', '10', '15', '20'])
    ```

    TODO: should this not also use min? instead of always starting from zero?

Graph.setTicks(*axisKey: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *pairs: [Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "(in Python v3.14)")[[Sequence](https://docs.python.org/3/library/typing.html#typing.Sequence "(in Python v3.14)")[[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")]] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/graph/primitives.html#Graph.setTicks)
:   Set the tick-labels for a given graph or plot’s axisKey
    (generally ‘x’, and ‘y’) with a set of pairs

    Pairs are iterables of positions and labels.

    N.B. – both ‘x’ and ‘y’ ticks have to be set in
    order to get matplotlib to display either (and presumably ‘z’ for 3D graphs).

    ```python
    >>> g = graph.primitives.GraphHorizontalBar()
    >>> g.axis['x']['ticks']
    Traceback (most recent call last):
    KeyError: 'ticks'
    >>> g.axis['x']
    {'range': None}
    ```

    ```python
    >>> g.setTicks('x', [(0, 'a'), (1, 'b')])
    >>> g.axis['x']['ticks']
    ([0, 1], ['a', 'b'])
    ```

    ```python
    >>> g.setTicks('m', [('a', 'b')])
    Traceback (most recent call last):
    music21.graph.utilities.GraphException: Cannot find key 'm' in self.axis
    ```

    ```python
    >>> g.setTicks('x', [])
    >>> g.axis['x']['ticks']
    ([], [])
    ```

Graph.show() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/graph/primitives.html#Graph.show)
:   Calls the show() method of the matplotlib plot.
    For most matplotlib back ends, this will open
    a GUI window with the desired graph.

Graph.write(*fp: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [pathlib.Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [matplotlib.figure.Figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "(in Matplotlib v3.10.9)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/graph/primitives.html#Graph.write)
:   Writes the graph to a file. If no file path is given, a temporary file is used.

## Graph3DBars

class music21.graph.primitives.Graph3DBars(*\**, *alpha: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") = 0.8*, *barWidth: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *barDepth: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\*\*keywords*)[[source]](../_modules/music21/graph/primitives.html#Graph3DBars)
:   Graph multiple parallel bar graphs in 3D.

    Data definition:
    A list of lists where the inner list of
    (x, y, z) coordinates.

    For instance, a graph where the x values increase
    (left to right), the y values increase in a step
    pattern (front to back), and the z values decrease
    (top to bottom):

    ```python
    >>> g = graph.primitives.Graph3DBars()
    >>> data = []
    >>> for i in range(1, 10 + 1):
    ...    q = [i, i//2, 10 - i]
    ...    data.append(q)
    >>> g.data = data
    >>> g.process()
    ```

    When creating the graph these keyword arguments can be used (in addition to any
    such as colors that all Graph classes can use).

    * `alpha` – opacity of each bar, from 0.0 (transparent) to 1.0 (opaque).
      Defaults to 0.8.
    * `barWidth` – width of each bar along the x-axis. When `None`
      (default) the width is computed automatically.
      Individual data points may also override this
      via a `'barWidth'` key in their per-point format dict.
    * `barDepth` – depth of each bar along the y-axis. When `None`
      (default) the depth is computed automatically.
      Individual data points may also override this
      via a `'barDepth'` key in their per-point format dict.

[`Graph3DBars`](#music21.graph.primitives.Graph3DBars "music21.graph.primitives.Graph3DBars") bases

* [`Graph`](#music21.graph.primitives.Graph "music21.graph.primitives.Graph")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`Graph3DBars`](#music21.graph.primitives.Graph3DBars "music21.graph.primitives.Graph3DBars") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`Graph3DBars`](#music21.graph.primitives.Graph3DBars "music21.graph.primitives.Graph3DBars") read/write properties

Read/write properties inherited from [`Graph`](#music21.graph.primitives.Graph "music21.graph.primitives.Graph"):

|  |  |  |
| --- | --- | --- |
| * [`doneAction`](#music21.graph.primitives.Graph.doneAction "music21.graph.primitives.Graph.doneAction") |  |  |

[`Graph3DBars`](#music21.graph.primitives.Graph3DBars "music21.graph.primitives.Graph3DBars") methods

Graph3DBars.process() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/graph/primitives.html#Graph3DBars.process)
:   Creates the figure and subplot, calls renderSubplot to get the
    subclass specific information on the data, runs hideAxisSpines,
    applyFormatting, and then calls the done action. Returns None,
    but the subplot is available at self.subplot

Graph3DBars.renderSubplot(*subplot: [matplotlib.axes.Axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "(in Matplotlib v3.10.9)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/graph/primitives.html#Graph3DBars.renderSubplot)
:   Calls the subclass specific information to get the data

Methods inherited from [`Graph`](#music21.graph.primitives.Graph "music21.graph.primitives.Graph"):

|  |  |  |
| --- | --- | --- |
| * [`applyFormatting()`](#music21.graph.primitives.Graph.applyFormatting "music21.graph.primitives.Graph.applyFormatting") * [`applyFormattingToOneAxis()`](#music21.graph.primitives.Graph.applyFormattingToOneAxis "music21.graph.primitives.Graph.applyFormattingToOneAxis") * [`applyGrid()`](#music21.graph.primitives.Graph.applyGrid "music21.graph.primitives.Graph.applyGrid") * [`callDoneAction()`](#music21.graph.primitives.Graph.callDoneAction "music21.graph.primitives.Graph.callDoneAction") | * [`hideAxisSpines()`](#music21.graph.primitives.Graph.hideAxisSpines "music21.graph.primitives.Graph.hideAxisSpines") * [`nextColor()`](#music21.graph.primitives.Graph.nextColor "music21.graph.primitives.Graph.nextColor") * [`setAxisLabel()`](#music21.graph.primitives.Graph.setAxisLabel "music21.graph.primitives.Graph.setAxisLabel") * [`setAxisRange()`](#music21.graph.primitives.Graph.setAxisRange "music21.graph.primitives.Graph.setAxisRange") | * [`setIntegerTicksFromData()`](#music21.graph.primitives.Graph.setIntegerTicksFromData "music21.graph.primitives.Graph.setIntegerTicksFromData") * [`setTicks()`](#music21.graph.primitives.Graph.setTicks "music21.graph.primitives.Graph.setTicks") * [`show()`](#music21.graph.primitives.Graph.show "music21.graph.primitives.Graph.show") * [`write()`](#music21.graph.primitives.Graph.write "music21.graph.primitives.Graph.write") |

## GraphColorGrid

class music21.graph.primitives.GraphColorGrid(*\*\*keywords*)[[source]](../_modules/music21/graph/primitives.html#GraphColorGrid)
:   Grid of discrete colored “blocks” to visualize results of a windowed analysis routine.

    Data is provided as a list of lists of colors, where colors are specified as a hex triplet,
    or the common HTML color codes, and based on analysis-specific mapping of colors to results.

    ```python
    >>> g = graph.primitives.GraphColorGrid()
    >>> data = [['#55FF00', '#9b0000', '#009b00'],
    ...         ['#FFD600', '#FF5600'],
    ...         ['#201a2b', '#8f73bf', '#a080d5', '#403355', '#999999']]
    >>> g.data = data
    >>> g.process()
    ```

    [![../_images/GraphColorGrid.png](../_images/GraphColorGrid.png)](../_images/GraphColorGrid.png)

[`GraphColorGrid`](#music21.graph.primitives.GraphColorGrid "music21.graph.primitives.GraphColorGrid") bases

* [`Graph`](#music21.graph.primitives.Graph "music21.graph.primitives.Graph")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`GraphColorGrid`](#music21.graph.primitives.GraphColorGrid "music21.graph.primitives.GraphColorGrid") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`GraphColorGrid`](#music21.graph.primitives.GraphColorGrid "music21.graph.primitives.GraphColorGrid") read/write properties

Read/write properties inherited from [`Graph`](#music21.graph.primitives.Graph "music21.graph.primitives.Graph"):

|  |  |  |
| --- | --- | --- |
| * [`doneAction`](#music21.graph.primitives.Graph.doneAction "music21.graph.primitives.Graph.doneAction") |  |  |

[`GraphColorGrid`](#music21.graph.primitives.GraphColorGrid "music21.graph.primitives.GraphColorGrid") methods

GraphColorGrid.renderSubplot(*subplot: [matplotlib.axes.Axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "(in Matplotlib v3.10.9)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/graph/primitives.html#GraphColorGrid.renderSubplot)
:   Calls the subclass specific information to get the data

Methods inherited from [`Graph`](#music21.graph.primitives.Graph "music21.graph.primitives.Graph"):

|  |  |  |
| --- | --- | --- |
| * [`applyFormatting()`](#music21.graph.primitives.Graph.applyFormatting "music21.graph.primitives.Graph.applyFormatting") * [`applyFormattingToOneAxis()`](#music21.graph.primitives.Graph.applyFormattingToOneAxis "music21.graph.primitives.Graph.applyFormattingToOneAxis") * [`applyGrid()`](#music21.graph.primitives.Graph.applyGrid "music21.graph.primitives.Graph.applyGrid") * [`callDoneAction()`](#music21.graph.primitives.Graph.callDoneAction "music21.graph.primitives.Graph.callDoneAction") * [`hideAxisSpines()`](#music21.graph.primitives.Graph.hideAxisSpines "music21.graph.primitives.Graph.hideAxisSpines") | * [`nextColor()`](#music21.graph.primitives.Graph.nextColor "music21.graph.primitives.Graph.nextColor") * [`process()`](#music21.graph.primitives.Graph.process "music21.graph.primitives.Graph.process") * [`setAxisLabel()`](#music21.graph.primitives.Graph.setAxisLabel "music21.graph.primitives.Graph.setAxisLabel") * [`setAxisRange()`](#music21.graph.primitives.Graph.setAxisRange "music21.graph.primitives.Graph.setAxisRange") | * [`setIntegerTicksFromData()`](#music21.graph.primitives.Graph.setIntegerTicksFromData "music21.graph.primitives.Graph.setIntegerTicksFromData") * [`setTicks()`](#music21.graph.primitives.Graph.setTicks "music21.graph.primitives.Graph.setTicks") * [`show()`](#music21.graph.primitives.Graph.show "music21.graph.primitives.Graph.show") * [`write()`](#music21.graph.primitives.Graph.write "music21.graph.primitives.Graph.write") |

[`GraphColorGrid`](#music21.graph.primitives.GraphColorGrid "music21.graph.primitives.GraphColorGrid") instance variables

GraphColorGrid.hideLeftBottomSpines
:   bool to hide the left and bottom axis spines; default True

## GraphColorGridLegend

class music21.graph.primitives.GraphColorGridLegend(*\*\*keywords*)[[source]](../_modules/music21/graph/primitives.html#GraphColorGridLegend)
:   Grid of discrete colored “blocks” where each block can be labeled

    Data is provided as a list of lists of colors, where colors are specified as a hex triplet,
    or the common HTML color codes, and based on analysis-specific mapping of colors to results.

    ```python
    >>> g = graph.primitives.GraphColorGridLegend()
    >>> data = [
    ...         ('Major', [('C#', '#00aa55'), ('D-', '#5600ff'), ('G#', '#2b00ff')]),
    ...         ('Minor', [('C#', '#004600'), ('D-', '#00009b'), ('G#', '#00009b')])
    ... ]
    >>> g.data = data
    >>> g.process()
    ```

    [![../_images/GraphColorGridLegend.png](../_images/GraphColorGridLegend.png)](../_images/GraphColorGridLegend.png)

[`GraphColorGridLegend`](#music21.graph.primitives.GraphColorGridLegend "music21.graph.primitives.GraphColorGridLegend") bases

* [`Graph`](#music21.graph.primitives.Graph "music21.graph.primitives.Graph")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`GraphColorGridLegend`](#music21.graph.primitives.GraphColorGridLegend "music21.graph.primitives.GraphColorGridLegend") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`GraphColorGridLegend`](#music21.graph.primitives.GraphColorGridLegend "music21.graph.primitives.GraphColorGridLegend") read/write properties

Read/write properties inherited from [`Graph`](#music21.graph.primitives.Graph "music21.graph.primitives.Graph"):

|  |  |  |
| --- | --- | --- |
| * [`doneAction`](#music21.graph.primitives.Graph.doneAction "music21.graph.primitives.Graph.doneAction") |  |  |

[`GraphColorGridLegend`](#music21.graph.primitives.GraphColorGridLegend "music21.graph.primitives.GraphColorGridLegend") methods

GraphColorGridLegend.makeOneRowOfGraph(*figure: [matplotlib.figure.Figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "(in Matplotlib v3.10.9)")*, *rowIndex: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *rowLabel: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *rowData: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*) → [matplotlib.axes.Axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "(in Matplotlib v3.10.9)")[[source]](../_modules/music21/graph/primitives.html#GraphColorGridLegend.makeOneRowOfGraph)
:   Makes a subplot for one row of data (such as for the Major label)
    and returns a matplotlib.axes.AxesSubplot instance representing the subplot.

    Here we create an axis with a part of Scriabin’s mapping of colors
    to keys in Prometheus: The Poem of Fire.

    ```python
    >>> import matplotlib.pyplot
    ```

    ```python
    >>> colorLegend = graph.primitives.GraphColorGridLegend()
    >>> rowData = [('C', '#ff0000'), ('G', '#ff8800'), ('D', '#ffff00'),
    ...            ('A', '#00ff00'), ('E', '#4444ff')]
    >>> colorLegend.data = [['Scriabin Mapping', rowData]]
    ```

    ```python
    >>> fig = matplotlib.pyplot.figure()
    >>> subplot = colorLegend.makeOneRowOfGraph(fig, 0, 'Scriabin Mapping', rowData)
    >>> subplot
    <Axes: >
    ```

GraphColorGridLegend.renderSubplot(*subplot: [matplotlib.axes.Axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "(in Matplotlib v3.10.9)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/graph/primitives.html#GraphColorGridLegend.renderSubplot)
:   Calls the subclass specific information to get the data

Methods inherited from [`Graph`](#music21.graph.primitives.Graph "music21.graph.primitives.Graph"):

|  |  |  |
| --- | --- | --- |
| * [`applyFormatting()`](#music21.graph.primitives.Graph.applyFormatting "music21.graph.primitives.Graph.applyFormatting") * [`applyFormattingToOneAxis()`](#music21.graph.primitives.Graph.applyFormattingToOneAxis "music21.graph.primitives.Graph.applyFormattingToOneAxis") * [`applyGrid()`](#music21.graph.primitives.Graph.applyGrid "music21.graph.primitives.Graph.applyGrid") * [`callDoneAction()`](#music21.graph.primitives.Graph.callDoneAction "music21.graph.primitives.Graph.callDoneAction") * [`hideAxisSpines()`](#music21.graph.primitives.Graph.hideAxisSpines "music21.graph.primitives.Graph.hideAxisSpines") | * [`nextColor()`](#music21.graph.primitives.Graph.nextColor "music21.graph.primitives.Graph.nextColor") * [`process()`](#music21.graph.primitives.Graph.process "music21.graph.primitives.Graph.process") * [`setAxisLabel()`](#music21.graph.primitives.Graph.setAxisLabel "music21.graph.primitives.Graph.setAxisLabel") * [`setAxisRange()`](#music21.graph.primitives.Graph.setAxisRange "music21.graph.primitives.Graph.setAxisRange") | * [`setIntegerTicksFromData()`](#music21.graph.primitives.Graph.setIntegerTicksFromData "music21.graph.primitives.Graph.setIntegerTicksFromData") * [`setTicks()`](#music21.graph.primitives.Graph.setTicks "music21.graph.primitives.Graph.setTicks") * [`show()`](#music21.graph.primitives.Graph.show "music21.graph.primitives.Graph.show") * [`write()`](#music21.graph.primitives.Graph.write "music21.graph.primitives.Graph.write") |

[`GraphColorGridLegend`](#music21.graph.primitives.GraphColorGridLegend "music21.graph.primitives.GraphColorGridLegend") instance variables

GraphColorGridLegend.hideLeftBottomSpines
:   bool to hide the left and bottom axis spines; default True

## GraphGroupedVerticalBar

class music21.graph.primitives.GraphGroupedVerticalBar(*\*\*keywords*)[[source]](../_modules/music21/graph/primitives.html#GraphGroupedVerticalBar)
:   Graph the count of one or more elements in vertical bars.

    The .data is simply a list of x and y pairs, where there
    is only one of each x value, and y value is a list of values.

    ```python
    >>> from collections import OrderedDict
    >>> g = graph.primitives.GraphGroupedVerticalBar()
    >>> lengths = OrderedDict( [('a', 3), ('b', 2), ('c', 1)] )
    >>> data = [('bar' + str(x), lengths) for x in range(3)]
    >>> data
    [('bar0', OrderedDict([('a', 3), ('b', 2), ('c', 1)])),
     ('bar1', OrderedDict([('a', 3), ('b', 2), ('c', 1)])),
     ('bar2', OrderedDict([('a', 3), ('b', 2), ('c', 1)]))]
    >>> g.data = data
    >>> g.process()
    ```

[`GraphGroupedVerticalBar`](#music21.graph.primitives.GraphGroupedVerticalBar "music21.graph.primitives.GraphGroupedVerticalBar") bases

* [`Graph`](#music21.graph.primitives.Graph "music21.graph.primitives.Graph")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`GraphGroupedVerticalBar`](#music21.graph.primitives.GraphGroupedVerticalBar "music21.graph.primitives.GraphGroupedVerticalBar") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`GraphGroupedVerticalBar`](#music21.graph.primitives.GraphGroupedVerticalBar "music21.graph.primitives.GraphGroupedVerticalBar") read/write properties

Read/write properties inherited from [`Graph`](#music21.graph.primitives.Graph "music21.graph.primitives.Graph"):

|  |  |  |
| --- | --- | --- |
| * [`doneAction`](#music21.graph.primitives.Graph.doneAction "music21.graph.primitives.Graph.doneAction") |  |  |

[`GraphGroupedVerticalBar`](#music21.graph.primitives.GraphGroupedVerticalBar "music21.graph.primitives.GraphGroupedVerticalBar") methods

GraphGroupedVerticalBar.labelBars(*subplot: [matplotlib.axes.Axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "(in Matplotlib v3.10.9)")*, *rects*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/graph/primitives.html#GraphGroupedVerticalBar.labelBars)

GraphGroupedVerticalBar.renderSubplot(*subplot: [matplotlib.axes.Axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "(in Matplotlib v3.10.9)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/graph/primitives.html#GraphGroupedVerticalBar.renderSubplot)
:   Calls the subclass specific information to get the data

Methods inherited from [`Graph`](#music21.graph.primitives.Graph "music21.graph.primitives.Graph"):

|  |  |  |
| --- | --- | --- |
| * [`applyFormatting()`](#music21.graph.primitives.Graph.applyFormatting "music21.graph.primitives.Graph.applyFormatting") * [`applyFormattingToOneAxis()`](#music21.graph.primitives.Graph.applyFormattingToOneAxis "music21.graph.primitives.Graph.applyFormattingToOneAxis") * [`applyGrid()`](#music21.graph.primitives.Graph.applyGrid "music21.graph.primitives.Graph.applyGrid") * [`callDoneAction()`](#music21.graph.primitives.Graph.callDoneAction "music21.graph.primitives.Graph.callDoneAction") * [`hideAxisSpines()`](#music21.graph.primitives.Graph.hideAxisSpines "music21.graph.primitives.Graph.hideAxisSpines") | * [`nextColor()`](#music21.graph.primitives.Graph.nextColor "music21.graph.primitives.Graph.nextColor") * [`process()`](#music21.graph.primitives.Graph.process "music21.graph.primitives.Graph.process") * [`setAxisLabel()`](#music21.graph.primitives.Graph.setAxisLabel "music21.graph.primitives.Graph.setAxisLabel") * [`setAxisRange()`](#music21.graph.primitives.Graph.setAxisRange "music21.graph.primitives.Graph.setAxisRange") | * [`setIntegerTicksFromData()`](#music21.graph.primitives.Graph.setIntegerTicksFromData "music21.graph.primitives.Graph.setIntegerTicksFromData") * [`setTicks()`](#music21.graph.primitives.Graph.setTicks "music21.graph.primitives.Graph.setTicks") * [`show()`](#music21.graph.primitives.Graph.show "music21.graph.primitives.Graph.show") * [`write()`](#music21.graph.primitives.Graph.write "music21.graph.primitives.Graph.write") |

## GraphHistogram

class music21.graph.primitives.GraphHistogram(*\**, *binWidth: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") = 0.8*, *alpha: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") = 0.8*, *\*\*keywords*)[[source]](../_modules/music21/graph/primitives.html#GraphHistogram)
:   Graph the count of a single element.

    Data set is simply a list of x and y pairs, where there
    is only one of each x value, and y value is the count or magnitude
    of that value

    ```python
    >>> import random
    >>> g = graph.primitives.GraphHistogram()
    >>> g.graphType
    'histogram'
    ```

    ```python
    >>> data = [(x, random.choice(range(30))) for x in range(50)]
    >>> g.data = data
    >>> g.process()
    ```

    [![../_images/GraphHistogram.png](../_images/GraphHistogram.png)](../_images/GraphHistogram.png)

[`GraphHistogram`](#music21.graph.primitives.GraphHistogram "music21.graph.primitives.GraphHistogram") bases

* [`Graph`](#music21.graph.primitives.Graph "music21.graph.primitives.Graph")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`GraphHistogram`](#music21.graph.primitives.GraphHistogram "music21.graph.primitives.GraphHistogram") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`GraphHistogram`](#music21.graph.primitives.GraphHistogram "music21.graph.primitives.GraphHistogram") read/write properties

Read/write properties inherited from [`Graph`](#music21.graph.primitives.Graph "music21.graph.primitives.Graph"):

|  |  |  |
| --- | --- | --- |
| * [`doneAction`](#music21.graph.primitives.Graph.doneAction "music21.graph.primitives.Graph.doneAction") |  |  |

[`GraphHistogram`](#music21.graph.primitives.GraphHistogram "music21.graph.primitives.GraphHistogram") methods

GraphHistogram.renderSubplot(*subplot: [matplotlib.axes.Axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "(in Matplotlib v3.10.9)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/graph/primitives.html#GraphHistogram.renderSubplot)
:   Calls the subclass specific information to get the data

Methods inherited from [`Graph`](#music21.graph.primitives.Graph "music21.graph.primitives.Graph"):

|  |  |  |
| --- | --- | --- |
| * [`applyFormatting()`](#music21.graph.primitives.Graph.applyFormatting "music21.graph.primitives.Graph.applyFormatting") * [`applyFormattingToOneAxis()`](#music21.graph.primitives.Graph.applyFormattingToOneAxis "music21.graph.primitives.Graph.applyFormattingToOneAxis") * [`applyGrid()`](#music21.graph.primitives.Graph.applyGrid "music21.graph.primitives.Graph.applyGrid") * [`callDoneAction()`](#music21.graph.primitives.Graph.callDoneAction "music21.graph.primitives.Graph.callDoneAction") * [`hideAxisSpines()`](#music21.graph.primitives.Graph.hideAxisSpines "music21.graph.primitives.Graph.hideAxisSpines") | * [`nextColor()`](#music21.graph.primitives.Graph.nextColor "music21.graph.primitives.Graph.nextColor") * [`process()`](#music21.graph.primitives.Graph.process "music21.graph.primitives.Graph.process") * [`setAxisLabel()`](#music21.graph.primitives.Graph.setAxisLabel "music21.graph.primitives.Graph.setAxisLabel") * [`setAxisRange()`](#music21.graph.primitives.Graph.setAxisRange "music21.graph.primitives.Graph.setAxisRange") | * [`setIntegerTicksFromData()`](#music21.graph.primitives.Graph.setIntegerTicksFromData "music21.graph.primitives.Graph.setIntegerTicksFromData") * [`setTicks()`](#music21.graph.primitives.Graph.setTicks "music21.graph.primitives.Graph.setTicks") * [`show()`](#music21.graph.primitives.Graph.show "music21.graph.primitives.Graph.show") * [`write()`](#music21.graph.primitives.Graph.write "music21.graph.primitives.Graph.write") |

[`GraphHistogram`](#music21.graph.primitives.GraphHistogram "music21.graph.primitives.GraphHistogram") instance variables

GraphHistogram.binWidth
:   Size of each bin; if the bins are equally spaced at intervals of 1,
    then 0.8 is a good default to allow a little space. 1.0 will give no
    space.

## GraphHorizontalBar

class music21.graph.primitives.GraphHorizontalBar(*\*\*keywords*)[[source]](../_modules/music21/graph/primitives.html#GraphHorizontalBar)
:   Numerous horizontal bars in discrete channels, where bars
    can be incomplete and/or overlap.

    Data provided is a list of pairs, where the first value becomes the key,
    the second value is a list of x-start, x-length values.

    Note how the second element in each data point is the length, so
    subtracting death year from birth year gives the appropriate length.

    Example: Plot the life-span of four composers whose lives were intertwined:
    Chopin, Robert and Clara Schumann, and Brahms.

    ```python
    >>> a = graph.primitives.GraphHorizontalBar()
    >>> data = [('Chopin', [(1810, 1849-1810)]),
    ...         ('Schumanns', [(1810, 1856-1810), (1819, 1896-1819)]),
    ...         ('Brahms', [(1833, 1897-1833)])]
    >>> a.data = data
    >>> a.process()
    ```

    [![../_images/GraphHorizontalBar.png](../_images/GraphHorizontalBar.png)](../_images/GraphHorizontalBar.png)

    Data is a list of tuples in the form, where each entry represents a space on the
    Y axis:

    > * Label
    > * List of tuples of numeric data where each tuple has two or three elements:
    >   :   + Start x-position
    >       + Length of bar
    >       + Optional: dictionary of format information about this point.
    > * Optional: dictionary of format information for all points at this level.
    >   (this will be overridden by any information for the particular point)

    To make an equally spaced plot, like in a Pitch Space plot, leave empty data in the form:

    > (‘’, [], {})

[`GraphHorizontalBar`](#music21.graph.primitives.GraphHorizontalBar "music21.graph.primitives.GraphHorizontalBar") bases

* [`Graph`](#music21.graph.primitives.Graph "music21.graph.primitives.Graph")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`GraphHorizontalBar`](#music21.graph.primitives.GraphHorizontalBar "music21.graph.primitives.GraphHorizontalBar") read-only properties

GraphHorizontalBar.barHeight

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`GraphHorizontalBar`](#music21.graph.primitives.GraphHorizontalBar "music21.graph.primitives.GraphHorizontalBar") read/write properties

Read/write properties inherited from [`Graph`](#music21.graph.primitives.Graph "music21.graph.primitives.Graph"):

|  |  |  |
| --- | --- | --- |
| * [`doneAction`](#music21.graph.primitives.Graph.doneAction "music21.graph.primitives.Graph.doneAction") |  |  |

[`GraphHorizontalBar`](#music21.graph.primitives.GraphHorizontalBar "music21.graph.primitives.GraphHorizontalBar") methods

GraphHorizontalBar.renderSubplot(*subplot: [matplotlib.axes.Axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "(in Matplotlib v3.10.9)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/graph/primitives.html#GraphHorizontalBar.renderSubplot)
:   Calls the subclass specific information to get the data

Methods inherited from [`Graph`](#music21.graph.primitives.Graph "music21.graph.primitives.Graph"):

|  |  |  |
| --- | --- | --- |
| * [`applyFormatting()`](#music21.graph.primitives.Graph.applyFormatting "music21.graph.primitives.Graph.applyFormatting") * [`applyFormattingToOneAxis()`](#music21.graph.primitives.Graph.applyFormattingToOneAxis "music21.graph.primitives.Graph.applyFormattingToOneAxis") * [`applyGrid()`](#music21.graph.primitives.Graph.applyGrid "music21.graph.primitives.Graph.applyGrid") * [`callDoneAction()`](#music21.graph.primitives.Graph.callDoneAction "music21.graph.primitives.Graph.callDoneAction") * [`hideAxisSpines()`](#music21.graph.primitives.Graph.hideAxisSpines "music21.graph.primitives.Graph.hideAxisSpines") | * [`nextColor()`](#music21.graph.primitives.Graph.nextColor "music21.graph.primitives.Graph.nextColor") * [`process()`](#music21.graph.primitives.Graph.process "music21.graph.primitives.Graph.process") * [`setAxisLabel()`](#music21.graph.primitives.Graph.setAxisLabel "music21.graph.primitives.Graph.setAxisLabel") * [`setAxisRange()`](#music21.graph.primitives.Graph.setAxisRange "music21.graph.primitives.Graph.setAxisRange") | * [`setIntegerTicksFromData()`](#music21.graph.primitives.Graph.setIntegerTicksFromData "music21.graph.primitives.Graph.setIntegerTicksFromData") * [`setTicks()`](#music21.graph.primitives.Graph.setTicks "music21.graph.primitives.Graph.setTicks") * [`show()`](#music21.graph.primitives.Graph.show "music21.graph.primitives.Graph.show") * [`write()`](#music21.graph.primitives.Graph.write "music21.graph.primitives.Graph.write") |

[`GraphHorizontalBar`](#music21.graph.primitives.GraphHorizontalBar "music21.graph.primitives.GraphHorizontalBar") instance variables

GraphHorizontalBar.barSpace
:   Amount of vertical space each bar takes; default 8

GraphHorizontalBar.margin
:   Vertical space above and below the bars, default 2 (= total4 space between bars)

## GraphHorizontalBarWeighted

class music21.graph.primitives.GraphHorizontalBarWeighted(*\*\*keywords*)[[source]](../_modules/music21/graph/primitives.html#GraphHorizontalBarWeighted)
:   Numerous horizontal bars in discrete channels,
    where bars can be incomplete and/or overlap, and
    can have different heights and colors within their
    respective channel.

[`GraphHorizontalBarWeighted`](#music21.graph.primitives.GraphHorizontalBarWeighted "music21.graph.primitives.GraphHorizontalBarWeighted") bases

* [`Graph`](#music21.graph.primitives.Graph "music21.graph.primitives.Graph")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`GraphHorizontalBarWeighted`](#music21.graph.primitives.GraphHorizontalBarWeighted "music21.graph.primitives.GraphHorizontalBarWeighted") read-only properties

GraphHorizontalBarWeighted.barHeight

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`GraphHorizontalBarWeighted`](#music21.graph.primitives.GraphHorizontalBarWeighted "music21.graph.primitives.GraphHorizontalBarWeighted") read/write properties

Read/write properties inherited from [`Graph`](#music21.graph.primitives.Graph "music21.graph.primitives.Graph"):

|  |  |  |
| --- | --- | --- |
| * [`doneAction`](#music21.graph.primitives.Graph.doneAction "music21.graph.primitives.Graph.doneAction") |  |  |

[`GraphHorizontalBarWeighted`](#music21.graph.primitives.GraphHorizontalBarWeighted "music21.graph.primitives.GraphHorizontalBarWeighted") methods

GraphHorizontalBarWeighted.renderSubplot(*subplot: [matplotlib.axes.Axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "(in Matplotlib v3.10.9)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/graph/primitives.html#GraphHorizontalBarWeighted.renderSubplot)
:   Calls the subclass specific information to get the data

Methods inherited from [`Graph`](#music21.graph.primitives.Graph "music21.graph.primitives.Graph"):

|  |  |  |
| --- | --- | --- |
| * [`applyFormatting()`](#music21.graph.primitives.Graph.applyFormatting "music21.graph.primitives.Graph.applyFormatting") * [`applyFormattingToOneAxis()`](#music21.graph.primitives.Graph.applyFormattingToOneAxis "music21.graph.primitives.Graph.applyFormattingToOneAxis") * [`applyGrid()`](#music21.graph.primitives.Graph.applyGrid "music21.graph.primitives.Graph.applyGrid") * [`callDoneAction()`](#music21.graph.primitives.Graph.callDoneAction "music21.graph.primitives.Graph.callDoneAction") * [`hideAxisSpines()`](#music21.graph.primitives.Graph.hideAxisSpines "music21.graph.primitives.Graph.hideAxisSpines") | * [`nextColor()`](#music21.graph.primitives.Graph.nextColor "music21.graph.primitives.Graph.nextColor") * [`process()`](#music21.graph.primitives.Graph.process "music21.graph.primitives.Graph.process") * [`setAxisLabel()`](#music21.graph.primitives.Graph.setAxisLabel "music21.graph.primitives.Graph.setAxisLabel") * [`setAxisRange()`](#music21.graph.primitives.Graph.setAxisRange "music21.graph.primitives.Graph.setAxisRange") | * [`setIntegerTicksFromData()`](#music21.graph.primitives.Graph.setIntegerTicksFromData "music21.graph.primitives.Graph.setIntegerTicksFromData") * [`setTicks()`](#music21.graph.primitives.Graph.setTicks "music21.graph.primitives.Graph.setTicks") * [`show()`](#music21.graph.primitives.Graph.show "music21.graph.primitives.Graph.show") * [`write()`](#music21.graph.primitives.Graph.write "music21.graph.primitives.Graph.write") |

[`GraphHorizontalBarWeighted`](#music21.graph.primitives.GraphHorizontalBarWeighted "music21.graph.primitives.GraphHorizontalBarWeighted") instance variables

GraphHorizontalBarWeighted.barSpace
:   Amount of vertical space each bar takes; default 8

GraphHorizontalBarWeighted.margin
:   Space around the bars, default 2

## GraphScatter

class music21.graph.primitives.GraphScatter(*\*\*keywords*)[[source]](../_modules/music21/graph/primitives.html#GraphScatter)
:   Graph two parameters in a scatter plot.
    Data representation is a list of points of values.

    ```python
    >>> g = graph.primitives.GraphScatter()
    >>> data = [(x, x * x) for x in range(50)]
    >>> g.data = data
    >>> g.process()
    ```

    [![../_images/GraphScatter.png](../_images/GraphScatter.png)](../_images/GraphScatter.png)

[`GraphScatter`](#music21.graph.primitives.GraphScatter "music21.graph.primitives.GraphScatter") bases

* [`Graph`](#music21.graph.primitives.Graph "music21.graph.primitives.Graph")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`GraphScatter`](#music21.graph.primitives.GraphScatter "music21.graph.primitives.GraphScatter") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`GraphScatter`](#music21.graph.primitives.GraphScatter "music21.graph.primitives.GraphScatter") read/write properties

Read/write properties inherited from [`Graph`](#music21.graph.primitives.Graph "music21.graph.primitives.Graph"):

|  |  |  |
| --- | --- | --- |
| * [`doneAction`](#music21.graph.primitives.Graph.doneAction "music21.graph.primitives.Graph.doneAction") |  |  |

[`GraphScatter`](#music21.graph.primitives.GraphScatter "music21.graph.primitives.GraphScatter") methods

GraphScatter.renderSubplot(*subplot: [matplotlib.axes.Axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "(in Matplotlib v3.10.9)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/graph/primitives.html#GraphScatter.renderSubplot)
:   Calls the subclass specific information to get the data

Methods inherited from [`Graph`](#music21.graph.primitives.Graph "music21.graph.primitives.Graph"):

|  |  |  |
| --- | --- | --- |
| * [`applyFormatting()`](#music21.graph.primitives.Graph.applyFormatting "music21.graph.primitives.Graph.applyFormatting") * [`applyFormattingToOneAxis()`](#music21.graph.primitives.Graph.applyFormattingToOneAxis "music21.graph.primitives.Graph.applyFormattingToOneAxis") * [`applyGrid()`](#music21.graph.primitives.Graph.applyGrid "music21.graph.primitives.Graph.applyGrid") * [`callDoneAction()`](#music21.graph.primitives.Graph.callDoneAction "music21.graph.primitives.Graph.callDoneAction") * [`hideAxisSpines()`](#music21.graph.primitives.Graph.hideAxisSpines "music21.graph.primitives.Graph.hideAxisSpines") | * [`nextColor()`](#music21.graph.primitives.Graph.nextColor "music21.graph.primitives.Graph.nextColor") * [`process()`](#music21.graph.primitives.Graph.process "music21.graph.primitives.Graph.process") * [`setAxisLabel()`](#music21.graph.primitives.Graph.setAxisLabel "music21.graph.primitives.Graph.setAxisLabel") * [`setAxisRange()`](#music21.graph.primitives.Graph.setAxisRange "music21.graph.primitives.Graph.setAxisRange") | * [`setIntegerTicksFromData()`](#music21.graph.primitives.Graph.setIntegerTicksFromData "music21.graph.primitives.Graph.setIntegerTicksFromData") * [`setTicks()`](#music21.graph.primitives.Graph.setTicks "music21.graph.primitives.Graph.setTicks") * [`show()`](#music21.graph.primitives.Graph.show "music21.graph.primitives.Graph.show") * [`write()`](#music21.graph.primitives.Graph.write "music21.graph.primitives.Graph.write") |

## GraphScatterWeighted

class music21.graph.primitives.GraphScatterWeighted(*\*\*keywords*)[[source]](../_modules/music21/graph/primitives.html#GraphScatterWeighted)
:   A scatter plot where points are scaled in size to
    represent the number of values stored within.

    ```python
    >>> g = graph.primitives.GraphScatterWeighted()
    >>> data = [(23, 15, 234), (10, 23, 12), (4, 23, 5), (15, 18, 120)]
    >>> g.data = data
    >>> g.process()
    ```

    [![../_images/GraphScatterWeighted.png](../_images/GraphScatterWeighted.png)](../_images/GraphScatterWeighted.png)

[`GraphScatterWeighted`](#music21.graph.primitives.GraphScatterWeighted "music21.graph.primitives.GraphScatterWeighted") bases

* [`Graph`](#music21.graph.primitives.Graph "music21.graph.primitives.Graph")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`GraphScatterWeighted`](#music21.graph.primitives.GraphScatterWeighted "music21.graph.primitives.GraphScatterWeighted") read-only properties

GraphScatterWeighted.rangeDiameter

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`GraphScatterWeighted`](#music21.graph.primitives.GraphScatterWeighted "music21.graph.primitives.GraphScatterWeighted") read/write properties

Read/write properties inherited from [`Graph`](#music21.graph.primitives.Graph "music21.graph.primitives.Graph"):

|  |  |  |
| --- | --- | --- |
| * [`doneAction`](#music21.graph.primitives.Graph.doneAction "music21.graph.primitives.Graph.doneAction") |  |  |

[`GraphScatterWeighted`](#music21.graph.primitives.GraphScatterWeighted "music21.graph.primitives.GraphScatterWeighted") methods

GraphScatterWeighted.renderSubplot(*subplot: [matplotlib.axes.Axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "(in Matplotlib v3.10.9)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/graph/primitives.html#GraphScatterWeighted.renderSubplot)
:   Calls the subclass specific information to get the data

Methods inherited from [`Graph`](#music21.graph.primitives.Graph "music21.graph.primitives.Graph"):

|  |  |  |
| --- | --- | --- |
| * [`applyFormatting()`](#music21.graph.primitives.Graph.applyFormatting "music21.graph.primitives.Graph.applyFormatting") * [`applyFormattingToOneAxis()`](#music21.graph.primitives.Graph.applyFormattingToOneAxis "music21.graph.primitives.Graph.applyFormattingToOneAxis") * [`applyGrid()`](#music21.graph.primitives.Graph.applyGrid "music21.graph.primitives.Graph.applyGrid") * [`callDoneAction()`](#music21.graph.primitives.Graph.callDoneAction "music21.graph.primitives.Graph.callDoneAction") * [`hideAxisSpines()`](#music21.graph.primitives.Graph.hideAxisSpines "music21.graph.primitives.Graph.hideAxisSpines") | * [`nextColor()`](#music21.graph.primitives.Graph.nextColor "music21.graph.primitives.Graph.nextColor") * [`process()`](#music21.graph.primitives.Graph.process "music21.graph.primitives.Graph.process") * [`setAxisLabel()`](#music21.graph.primitives.Graph.setAxisLabel "music21.graph.primitives.Graph.setAxisLabel") * [`setAxisRange()`](#music21.graph.primitives.Graph.setAxisRange "music21.graph.primitives.Graph.setAxisRange") | * [`setIntegerTicksFromData()`](#music21.graph.primitives.Graph.setIntegerTicksFromData "music21.graph.primitives.Graph.setIntegerTicksFromData") * [`setTicks()`](#music21.graph.primitives.Graph.setTicks "music21.graph.primitives.Graph.setTicks") * [`show()`](#music21.graph.primitives.Graph.show "music21.graph.primitives.Graph.show") * [`write()`](#music21.graph.primitives.Graph.write "music21.graph.primitives.Graph.write") |

[`GraphScatterWeighted`](#music21.graph.primitives.GraphScatterWeighted "music21.graph.primitives.GraphScatterWeighted") instance variables

GraphScatterWeighted.maxDiameter
:   the maximum diameter of any ellipse, default 1.25

GraphScatterWeighted.minDiameter
:   the minimum diameter of any ellipse, default 0.25
