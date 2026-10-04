Source: https://music21.org/music21docs/moduleReference/moduleGraphAxis.html

# music21.graph.axis

Definitions for extracting data from a Stream to place on one axis of a
[`PlotStream`](moduleGraphPlot.html#music21.graph.plot.PlotStream "music21.graph.plot.PlotStream") or similar object.

## Axis

class music21.graph.axis.Axis(*client=None*, *axisName='x'*)[[source]](../_modules/music21/graph/axis.html#Axis)
:   An Axis is an easier way of specifying what to plot on any given axis.

    Client should be a .plot.PlotStream or None. Eventually a Stream may be allowed,
    but not yet.

[`Axis`](#music21.graph.axis.Axis "music21.graph.axis.Axis") bases

* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`Axis`](#music21.graph.axis.Axis "music21.graph.axis.Axis") read-only properties

Axis.stream
:   Returns a reference to the client’s .streamObj (or None if client is None)

    If the client is itself a stream, return it.

    Read-only

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`Axis`](#music21.graph.axis.Axis "music21.graph.axis.Axis") read/write properties

Axis.client
:   The client stores a reference to the Plot that
    makes reference to this axis.

    (Like all music21 clients, It is normally stored internally as a weakref,
    so no need for garbage collecting)

Axis.label
:   Returns self.label or class.labelDefault if not set:

    ```python
    >>> ax = graph.axis.Axis(axisName='y')
    >>> ax.label
    'an axis'
    >>> ax.label = 'velocity'
    >>> ax.label
    'velocity'
    ```

[`Axis`](#music21.graph.axis.Axis "music21.graph.axis.Axis") methods

Axis.extractOneElement(*n: [note.GeneralNote](moduleNote.html#music21.note.GeneralNote "music21.note.GeneralNote")*, *formatDict: [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), t.Any]*) → t.Any[[source]](../_modules/music21/graph/axis.html#Axis.extractOneElement)
:   Override in subclasses

Axis.postProcessData(*dataList=None*)[[source]](../_modules/music21/graph/axis.html#Axis.postProcessData)
:   Routine to be called after data has been extracted to
    do any cleanup, etc. Defaults to doing nothing, but
    see CountingAxis for an example of how this works.

Axis.setBoundariesFromData(*values*)[[source]](../_modules/music21/graph/axis.html#Axis.setBoundariesFromData)
:   If self.minValue is not set,
    then set self.minValue to be the minimum of these values.

    Same with maxValue

    ```python
    >>> ax = graph.axis.Axis()
    >>> print(ax.minValue)
    None
    ```

    ```python
    >>> values = [10, 0, 3, 5]
    >>> ax.setBoundariesFromData(values)
    >>> ax.minValue
    0
    >>> ax.maxValue
    10
    ```

    If a boundary is given or .setXXXFromData is False then no changes are made

    ```python
    >>> ax = graph.axis.Axis()
    >>> ax.minValue = -1
    >>> ax.setBoundariesFromData(values)
    >>> ax.minValue
    -1
    >>> ax.maxValue
    10
    ```

Axis.ticks()[[source]](../_modules/music21/graph/axis.html#Axis.ticks)
:   Get a set of ticks for this data. Used by several numeric axes
    to make a reasonable number of ticks.

    ```python
    >>> cax = graph.axis.Axis()
    >>> cax.minValue = 1
    >>> cax.maxValue = 9
    >>> cax.ticks()
    [(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'),
     (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')]
    ```

    For larger data, the ticks are farther apart.

    ```python
    >>> cax.minValue = 7
    >>> cax.maxValue = 80
    >>> cax.ticks()
    [(0, '0'), (10, '10'), (20, '20'), (30, '30'), (40, '40'),
     (50, '50'), (60, '60'), (70, '70'), (80, '80'), (90, '90')]
    ```

    ```python
    >>> cax.minValue = 712
    >>> cax.maxValue = 2213
    >>> cax.ticks()
    [(600, '600'), (700, '700'), (800, '800'), (900, '900'), (1000, '1000'),
     ...
     (2100, '2100'), (2200, '2200'), (2300, '2300')]
    ```

[`Axis`](#music21.graph.axis.Axis "music21.graph.axis.Axis") instance variables

Axis.axisDataMap
:   a dict of {‘x’: 0, ‘y’: 1, ‘z’: 2} mapping where an axis’s data can
    be found in self.client.data after extract data is run:

    ```python
    >>> b = corpus.parse('bwv66.6')
    >>> plot = graph.plot.ScatterPitchClassOffset(b)
    >>> pcAxis = plot.axisY
    >>> pcAxis.axisName
    'y'
    >>> pcAxisDataIndex = pcAxis.axisDataMap[pcAxis.axisName]
    >>> pcAxisDataIndex
    1
    >>> plot.extractData()
    >>> pcValues = [dataTuple[pcAxisDataIndex] for dataTuple in plot.data]
    >>> pcValues[0:2]
    [1, 11]
    ```

Axis.axisName
:   the name of the axis. One of “x” or “y” or for 3D Plots, “z”

Axis.maxValue
:   None or number representing the axis maximum. Default None.

Axis.minValue
:   None or number representing the axis minimum. Default None.

Axis.quantities
:   a tuple of strings representing the quantities the axis can plot.
    The first element of the tuple is the authoritative name.

    ```python
    >>> ax = graph.axis.DynamicsAxis()
    >>> ax.quantities
    ('dynamic', 'dynamics', 'volume')
    ```

## CountingAxis

class music21.graph.axis.CountingAxis(*client=None*, *axisName='y'*)[[source]](../_modules/music21/graph/axis.html#CountingAxis)
:   Axis subclass for counting data in another Axis.

    Used for histograms, weighted scatter, etc.

    ```python
    >>> bach = corpus.parse('bwv66.6')
    >>> plotS = graph.plot.PlotStream(bach)
    >>> plotS.axisX = graph.axis.PitchSpaceAxis(plotS, 'x')
    >>> plotS.axisY = graph.axis.CountingAxis(plotS)
    >>> plotS.doneAction = None
    >>> plotS.run()
    >>> plotS.data
    [(42.0, 1, {}), (45.0, 1, {}), (46.0, 1, {}), (47.0, 5, {}), (49.0, 6, {}), ...]
    ```

[`CountingAxis`](#music21.graph.axis.CountingAxis "music21.graph.axis.CountingAxis") bases

* [`Axis`](#music21.graph.axis.Axis "music21.graph.axis.Axis")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`CountingAxis`](#music21.graph.axis.CountingAxis "music21.graph.axis.CountingAxis") read-only properties

Read-only properties inherited from [`Axis`](#music21.graph.axis.Axis "music21.graph.axis.Axis"):

|  |  |  |
| --- | --- | --- |
| * [`stream`](#music21.graph.axis.Axis.stream "music21.graph.axis.Axis.stream") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`CountingAxis`](#music21.graph.axis.CountingAxis "music21.graph.axis.CountingAxis") read/write properties

Read/write properties inherited from [`Axis`](#music21.graph.axis.Axis "music21.graph.axis.Axis"):

|  |  |  |
| --- | --- | --- |
| * [`client`](#music21.graph.axis.Axis.client "music21.graph.axis.Axis.client") | * [`label`](#music21.graph.axis.Axis.label "music21.graph.axis.Axis.label") |  |

[`CountingAxis`](#music21.graph.axis.CountingAxis "music21.graph.axis.CountingAxis") methods

CountingAxis.postProcessData()[[source]](../_modules/music21/graph/axis.html#CountingAxis.postProcessData)
:   Replace client.data with a list that only includes each key once.

Methods inherited from [`Axis`](#music21.graph.axis.Axis "music21.graph.axis.Axis"):

|  |  |  |
| --- | --- | --- |
| * [`extractOneElement()`](#music21.graph.axis.Axis.extractOneElement "music21.graph.axis.Axis.extractOneElement") | * [`setBoundariesFromData()`](#music21.graph.axis.Axis.setBoundariesFromData "music21.graph.axis.Axis.setBoundariesFromData") | * [`ticks()`](#music21.graph.axis.Axis.ticks "music21.graph.axis.Axis.ticks") |

[`CountingAxis`](#music21.graph.axis.CountingAxis "music21.graph.axis.CountingAxis") instance variables

CountingAxis.countAxes
:   a string or tuple of strings representing an axis or axes to use in counting

Instance variables inherited from [`Axis`](#music21.graph.axis.Axis "music21.graph.axis.Axis"):

|  |  |  |
| --- | --- | --- |
| * [`axisDataMap`](#music21.graph.axis.Axis.axisDataMap "music21.graph.axis.Axis.axisDataMap") * [`axisName`](#music21.graph.axis.Axis.axisName "music21.graph.axis.Axis.axisName") | * [`maxValue`](#music21.graph.axis.Axis.maxValue "music21.graph.axis.Axis.maxValue") * [`minValue`](#music21.graph.axis.Axis.minValue "music21.graph.axis.Axis.minValue") | * [`quantities`](#music21.graph.axis.Axis.quantities "music21.graph.axis.Axis.quantities") |

## DynamicsAxis

class music21.graph.axis.DynamicsAxis(*client=None*, *axisName='x'*)[[source]](../_modules/music21/graph/axis.html#DynamicsAxis)
:   Axis subclass for dealing with Dynamics

[`DynamicsAxis`](#music21.graph.axis.DynamicsAxis "music21.graph.axis.DynamicsAxis") bases

* [`Axis`](#music21.graph.axis.Axis "music21.graph.axis.Axis")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`DynamicsAxis`](#music21.graph.axis.DynamicsAxis "music21.graph.axis.DynamicsAxis") read-only properties

Read-only properties inherited from [`Axis`](#music21.graph.axis.Axis "music21.graph.axis.Axis"):

|  |  |  |
| --- | --- | --- |
| * [`stream`](#music21.graph.axis.Axis.stream "music21.graph.axis.Axis.stream") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`DynamicsAxis`](#music21.graph.axis.DynamicsAxis "music21.graph.axis.DynamicsAxis") read/write properties

Read/write properties inherited from [`Axis`](#music21.graph.axis.Axis "music21.graph.axis.Axis"):

|  |  |  |
| --- | --- | --- |
| * [`client`](#music21.graph.axis.Axis.client "music21.graph.axis.Axis.client") | * [`label`](#music21.graph.axis.Axis.label "music21.graph.axis.Axis.label") |  |

[`DynamicsAxis`](#music21.graph.axis.DynamicsAxis "music21.graph.axis.DynamicsAxis") methods

DynamicsAxis.setBoundariesFromData(*values=None*)[[source]](../_modules/music21/graph/axis.html#DynamicsAxis.setBoundariesFromData)
:   If self.minValue is not set,
    then set self.minValue to be the minimum of these values.

    Same with maxValue

    ```python
    >>> ax = graph.axis.Axis()
    >>> print(ax.minValue)
    None
    ```

    ```python
    >>> values = [10, 0, 3, 5]
    >>> ax.setBoundariesFromData(values)
    >>> ax.minValue
    0
    >>> ax.maxValue
    10
    ```

    If a boundary is given or .setXXXFromData is False then no changes are made

    ```python
    >>> ax = graph.axis.Axis()
    >>> ax.minValue = -1
    >>> ax.setBoundariesFromData(values)
    >>> ax.minValue
    -1
    >>> ax.maxValue
    10
    ```

DynamicsAxis.ticks()[[source]](../_modules/music21/graph/axis.html#DynamicsAxis.ticks)
:   Utility method to get ticks in dynamic values:

    ```python
    >>> ax = graph.axis.DynamicsAxis()
    >>> ax.ticks()
    [(0, '$pppppp$'), (1, '$ppppp$'), (2, '$pppp$'), (3, '$ppp$'), (4, '$pp$'),
     (5, '$p$'), (6, '$mp$'), (7, '$mf$'), (8, '$f$'), (9, '$fp$'), (10, '$sf$'),
     (11, '$ff$'), (12, '$fff$'), (13, '$ffff$'), (14, '$fffff$'), (15, '$ffffff$')]
    ```

    A minimum and maximum dynamic index can be specified as minValue and maxValue

    ```python
    >>> ax.minValue = 3
    >>> ax.maxValue = 6
    >>> ax.ticks()
    [(3, '$ppp$'), (4, '$pp$'), (5, '$p$'), (6, '$mp$')]
    ```

Methods inherited from [`Axis`](#music21.graph.axis.Axis "music21.graph.axis.Axis"):

|  |  |  |
| --- | --- | --- |
| * [`extractOneElement()`](#music21.graph.axis.Axis.extractOneElement "music21.graph.axis.Axis.extractOneElement") | * [`postProcessData()`](#music21.graph.axis.Axis.postProcessData "music21.graph.axis.Axis.postProcessData") |  |

[`DynamicsAxis`](#music21.graph.axis.DynamicsAxis "music21.graph.axis.DynamicsAxis") instance variables

Instance variables inherited from [`Axis`](#music21.graph.axis.Axis "music21.graph.axis.Axis"):

|  |  |  |
| --- | --- | --- |
| * [`axisDataMap`](#music21.graph.axis.Axis.axisDataMap "music21.graph.axis.Axis.axisDataMap") * [`axisName`](#music21.graph.axis.Axis.axisName "music21.graph.axis.Axis.axisName") | * [`maxValue`](#music21.graph.axis.Axis.maxValue "music21.graph.axis.Axis.maxValue") * [`minValue`](#music21.graph.axis.Axis.minValue "music21.graph.axis.Axis.minValue") | * [`quantities`](#music21.graph.axis.Axis.quantities "music21.graph.axis.Axis.quantities") |

## OffsetAxis

class music21.graph.axis.OffsetAxis(*client=None*, *axisName='x'*)[[source]](../_modules/music21/graph/axis.html#OffsetAxis)
:   Axis subclass for dealing with Offsets

[`OffsetAxis`](#music21.graph.axis.OffsetAxis "music21.graph.axis.OffsetAxis") bases

* [`PositionAxis`](#music21.graph.axis.PositionAxis "music21.graph.axis.PositionAxis")
* [`Axis`](#music21.graph.axis.Axis "music21.graph.axis.Axis")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`OffsetAxis`](#music21.graph.axis.OffsetAxis "music21.graph.axis.OffsetAxis") read-only properties

Read-only properties inherited from [`Axis`](#music21.graph.axis.Axis "music21.graph.axis.Axis"):

|  |  |  |
| --- | --- | --- |
| * [`stream`](#music21.graph.axis.Axis.stream "music21.graph.axis.Axis.stream") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`OffsetAxis`](#music21.graph.axis.OffsetAxis "music21.graph.axis.OffsetAxis") read/write properties

OffsetAxis.label
:   Return an axis label for measure or offset, depending on if measures are available.

    ```python
    >>> a = graph.axis.OffsetAxis()
    >>> a.label
    'Offset'
    >>> a.useMeasures = True
    >>> a.label
    'Measure Number'
    ```

Read/write properties inherited from [`Axis`](#music21.graph.axis.Axis "music21.graph.axis.Axis"):

|  |  |  |
| --- | --- | --- |
| * [`client`](#music21.graph.axis.Axis.client "music21.graph.axis.Axis.client") |  |  |

[`OffsetAxis`](#music21.graph.axis.OffsetAxis "music21.graph.axis.OffsetAxis") methods

OffsetAxis.extractOneElement(*n*, *formatDict*)[[source]](../_modules/music21/graph/axis.html#OffsetAxis.extractOneElement)
:   Override in subclasses

OffsetAxis.getOffsetMap()[[source]](../_modules/music21/graph/axis.html#OffsetAxis.getOffsetMap)
:   Find the first partlike object and get the measureOffsetMap from it, or an
    empty-dict if not.

    ```python
    >>> b = corpus.parse('bwv66.6')
    >>> p = graph.plot.PlotStream(b)
    >>> ax = graph.axis.OffsetAxis(p, 'x')
    >>> om = ax.getOffsetMap()
    >>> om
    OrderedDict([(0.0, [<music21.stream.Measure 0 offset=0.0>]),
                 (1.0, [<music21.stream.Measure 1 offset=1.0>]),
                 (5.0, [<music21.stream.Measure 2 offset=5.0>]),
                 ...])
    ```

    Same if called on a single part:

    ```python
    >>> p = graph.plot.PlotStream(b.parts[0])
    >>> ax = graph.axis.OffsetAxis(p, 'x')
    >>> om2 = ax.getOffsetMap()
    >>> om2
    OrderedDict([(0.0, [<music21.stream.Measure 0 offset=0.0>]),
                 (1.0, [<music21.stream.Measure 1 offset=1.0>]),
                 (5.0, [<music21.stream.Measure 2 offset=5.0>]),
                 ...])
    ```

    But empty if called on a single Measure …

    ```python
    >>> p = graph.plot.PlotStream(b.parts[0].getElementsByClass(stream.Measure)[2])
    >>> ax = graph.axis.OffsetAxis(p, 'x')
    >>> om3 = ax.getOffsetMap()
    >>> om3
    {}
    ```

OffsetAxis.setBoundariesFromData(*values=None*)[[source]](../_modules/music21/graph/axis.html#OffsetAxis.setBoundariesFromData)
:   If self.minValue is not set,
    then set self.minValue to be the minimum of these values.

    Same with maxValue

    ```python
    >>> ax = graph.axis.Axis()
    >>> print(ax.minValue)
    None
    ```

    ```python
    >>> values = [10, 0, 3, 5]
    >>> ax.setBoundariesFromData(values)
    >>> ax.minValue
    0
    >>> ax.maxValue
    10
    ```

    If a boundary is given or .setXXXFromData is False then no changes are made

    ```python
    >>> ax = graph.axis.Axis()
    >>> ax.minValue = -1
    >>> ax.setBoundariesFromData(values)
    >>> ax.minValue
    -1
    >>> ax.maxValue
    10
    ```

OffsetAxis.setUseMeasuresFromOffsetMap(*offsetMap=None*)[[source]](../_modules/music21/graph/axis.html#OffsetAxis.setUseMeasuresFromOffsetMap)
:   Given an offsetMap and .useMeasures=None return
    True or False based on whether the offsetMap or self.getOffsetMap() is
    non-empty.

    ```python
    >>> b = corpus.parse('bwv66.6')
    >>> p = graph.plot.PlotStream(b)
    >>> ax = graph.axis.OffsetAxis(p, 'x')
    >>> print(ax.useMeasures)
    None
    >>> ax.setUseMeasuresFromOffsetMap()
    True
    ```

    Sets .useMeasures as a side effect:

    ```python
    >>> ax.useMeasures
    True
    ```

    same as:

    ```python
    >>> ax = graph.axis.OffsetAxis(p, 'x')
    >>> om = ax.getOffsetMap()
    >>> ax.setUseMeasuresFromOffsetMap(om)
    True
    ```

    If .useMeasures is set explicitly, then
    we return that

    ```python
    >>> ax.useMeasures = False
    >>> ax.setUseMeasuresFromOffsetMap()
    False
    ```

    Returns False if the offsetMap is empty

    ```python
    >>> p = graph.plot.PlotStream(b.parts[0].getElementsByClass(stream.Measure)[2])
    >>> axMeasure = graph.axis.OffsetAxis(p, 'x')
    >>> axMeasure.setUseMeasuresFromOffsetMap()
    False
    >>> axMeasure.useMeasures
    False
    ```

OffsetAxis.ticks()[[source]](../_modules/music21/graph/axis.html#OffsetAxis.ticks)
:   Get offset or measure ticks

    ```python
    >>> bach = corpus.parse('bach/bwv281.xml')
    >>> plotS = graph.plot.PlotStream(bach)
    >>> ax = graph.axis.OffsetAxis(plotS)
    >>> ax.setBoundariesFromData()
    >>> ax.ticks()  # on whole score, showing anacrusis spacing
    [(0.0, '0'), (1.0, '1'), (5.0, '2'), (9.0, '3'), (13.0, '4'), (17.0, '5'),
     (21.0, '6'), (25.0, '7'), (29.0, '8')]
    ```

    We can reduce the number of ticks shown:

    ```python
    >>> ax.mostMeasureTicksToShow = 4
    >>> ax.ticks()
    [(0.0, '0'), (9.0, '3'), (21.0, '6'), (29.0, '8')]
    ```

    We can also plot on a part:

    ```python
    >>> soprano = bach.parts.first()
    >>> plotSoprano = graph.plot.PlotStream(soprano)
    >>> ax = graph.axis.OffsetAxis(plotSoprano)
    >>> ax.setBoundariesFromData()
    >>> ax.ticks()  # on whole score, showing anacrusis spacing
    [(0.0, '0'), (1.0, '1'), (5.0, '2'), (9.0, '3'), (13.0, '4'), (17.0, '5'),
     (21.0, '6'), (25.0, '7'), (29.0, '8')]
    ```

    Now we will show just the first and last measure:

    ```python
    >>> ax.minMaxMeasureOnly = True
    >>> ax.ticks()
    [(0.0, '0'), (29.0, '8')]
    ```

    Only show ticks between minValue and maxValue (in offsets):

    ```python
    >>> ax.minMaxMeasureOnly = False
    >>> ax.minValue = 8
    >>> ax.maxValue = 12
    >>> ax.ticks()
    [(9.0, '3')]
    ```

    Double bars and other heavy bars always show up.
    (Let’s get a new axis object to see.)

    ```python
    >>> ax = graph.axis.OffsetAxis(plotSoprano)
    >>> ax.setBoundariesFromData()
    >>> ax.mostMeasureTicksToShow = 4
    >>> ax.ticks()
    [(0.0, '0'), (9.0, '3'), (21.0, '6'), (29.0, '8')]
    >>> m5 = soprano.getElementsByClass(stream.Measure)[5]
    >>> m5.number
    5
    >>> m5.rightBarline = bar.Barline('double')
    >>> ax.ticks()
    [(0.0, '0'), (13.0, '4'), (17.0, '5'), (29.0, '8')]
    ```

    Future improvements might make the spacing around the double bars
    a bit better. It’d be nice to see measure 2 or 3 ticked rather
    than measure 4.

    On a raw collection of notes with no measures, offsets are used:

    ```python
    >>> n = note.Note('a')
    >>> s = stream.Stream()
    >>> s.repeatAppend(n, 20)
    >>> plotS = graph.plot.PlotStream(s)
    >>> ax = graph.axis.OffsetAxis(plotS)
    >>> ax.setBoundariesFromData()
    >>> ax.ticks()
    [(0, '0'), (10, '10'), (20, '20')]
    ```

    The space between offsets is configured by .offsetStepSize. At
    present mostMeasureTicksToShow to does affect streams without measures.

    ```python
    >>> ax.offsetStepSize = 5
    >>> ax.ticks()
    [(0, '0'), (5, '5'), (10, '10'), (15, '15'), (20, '20')]
    ```

Methods inherited from [`Axis`](#music21.graph.axis.Axis "music21.graph.axis.Axis"):

|  |  |  |
| --- | --- | --- |
| * [`postProcessData()`](#music21.graph.axis.Axis.postProcessData "music21.graph.axis.Axis.postProcessData") |  |  |

[`OffsetAxis`](#music21.graph.axis.OffsetAxis "music21.graph.axis.OffsetAxis") instance variables

OffsetAxis.maxValue
:   The highest ending position (as an offset). Will be set automatically.

OffsetAxis.minMaxMeasureOnly
:   If True then only the first and last values will be used to
    create ticks for measures. Default False.

OffsetAxis.minValue
:   The lowest starting position (as an offset). Will be set automatically.

OffsetAxis.mostMeasureTicksToShow
:   When plotting measures, will limit the number of ticks given to at most
    this number. Note that since all double/final/heavy bars are show, this number
    may be exceeded if there are more that this number of double bars. Default: 20.

OffsetAxis.offsetStepSize
:   If measures are not used then this number is used to create the number
    of steps between an axis tick. Currently the default is 10, but it
    might become a function of the length of the stream eventually.

OffsetAxis.useMeasures
:   bool or None for whether offsets (False) or measure numbers (True) should be used
    in the case of an offset access. Default, None, meaning to check whether
    the stream has measures first.

Instance variables inherited from [`PositionAxis`](#music21.graph.axis.PositionAxis "music21.graph.axis.PositionAxis"):

|  |  |  |
| --- | --- | --- |
| * [`graceNoteQL`](#music21.graph.axis.PositionAxis.graceNoteQL "music21.graph.axis.PositionAxis.graceNoteQL") |  |  |

Instance variables inherited from [`Axis`](#music21.graph.axis.Axis "music21.graph.axis.Axis"):

|  |  |  |
| --- | --- | --- |
| * [`axisDataMap`](#music21.graph.axis.Axis.axisDataMap "music21.graph.axis.Axis.axisDataMap") * [`axisName`](#music21.graph.axis.Axis.axisName "music21.graph.axis.Axis.axisName") | * [`maxValue`](#music21.graph.axis.Axis.maxValue "music21.graph.axis.Axis.maxValue") * [`minValue`](#music21.graph.axis.Axis.minValue "music21.graph.axis.Axis.minValue") | * [`quantities`](#music21.graph.axis.Axis.quantities "music21.graph.axis.Axis.quantities") |

## OffsetEndAxis

class music21.graph.axis.OffsetEndAxis(*client=None*, *axisName='x'*, *noteSpacing=-1*)[[source]](../_modules/music21/graph/axis.html#OffsetEndAxis)
:   An Axis that gives beginning and ending values for each element

[`OffsetEndAxis`](#music21.graph.axis.OffsetEndAxis "music21.graph.axis.OffsetEndAxis") bases

* [`OffsetAxis`](#music21.graph.axis.OffsetAxis "music21.graph.axis.OffsetAxis")
* [`PositionAxis`](#music21.graph.axis.PositionAxis "music21.graph.axis.PositionAxis")
* [`Axis`](#music21.graph.axis.Axis "music21.graph.axis.Axis")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`OffsetEndAxis`](#music21.graph.axis.OffsetEndAxis "music21.graph.axis.OffsetEndAxis") read-only properties

Read-only properties inherited from [`Axis`](#music21.graph.axis.Axis "music21.graph.axis.Axis"):

|  |  |  |
| --- | --- | --- |
| * [`stream`](#music21.graph.axis.Axis.stream "music21.graph.axis.Axis.stream") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`OffsetEndAxis`](#music21.graph.axis.OffsetEndAxis "music21.graph.axis.OffsetEndAxis") read/write properties

Read/write properties inherited from [`OffsetAxis`](#music21.graph.axis.OffsetAxis "music21.graph.axis.OffsetAxis"):

|  |  |  |
| --- | --- | --- |
| * [`label`](#music21.graph.axis.OffsetAxis.label "music21.graph.axis.OffsetAxis.label") |  |  |

Read/write properties inherited from [`Axis`](#music21.graph.axis.Axis "music21.graph.axis.Axis"):

|  |  |  |
| --- | --- | --- |
| * [`client`](#music21.graph.axis.Axis.client "music21.graph.axis.Axis.client") |  |  |

[`OffsetEndAxis`](#music21.graph.axis.OffsetEndAxis "music21.graph.axis.OffsetEndAxis") methods

OffsetEndAxis.extractOneElement(*n*, *formatDict*)[[source]](../_modules/music21/graph/axis.html#OffsetEndAxis.extractOneElement)
:   Override in subclasses

Methods inherited from [`OffsetAxis`](#music21.graph.axis.OffsetAxis "music21.graph.axis.OffsetAxis"):

|  |  |  |
| --- | --- | --- |
| * [`getOffsetMap()`](#music21.graph.axis.OffsetAxis.getOffsetMap "music21.graph.axis.OffsetAxis.getOffsetMap") * [`setBoundariesFromData()`](#music21.graph.axis.OffsetAxis.setBoundariesFromData "music21.graph.axis.OffsetAxis.setBoundariesFromData") | * [`setUseMeasuresFromOffsetMap()`](#music21.graph.axis.OffsetAxis.setUseMeasuresFromOffsetMap "music21.graph.axis.OffsetAxis.setUseMeasuresFromOffsetMap") | * [`ticks()`](#music21.graph.axis.OffsetAxis.ticks "music21.graph.axis.OffsetAxis.ticks") |

Methods inherited from [`Axis`](#music21.graph.axis.Axis "music21.graph.axis.Axis"):

|  |  |  |
| --- | --- | --- |
| * [`postProcessData()`](#music21.graph.axis.Axis.postProcessData "music21.graph.axis.Axis.postProcessData") |  |  |

[`OffsetEndAxis`](#music21.graph.axis.OffsetEndAxis "music21.graph.axis.OffsetEndAxis") instance variables

OffsetEndAxis.noteSpacing
:   amount in QL to leave blank between untied notes.
    (default = self.graceNoteQL)

Instance variables inherited from [`OffsetAxis`](#music21.graph.axis.OffsetAxis "music21.graph.axis.OffsetAxis"):

|  |  |  |
| --- | --- | --- |
| * [`maxValue`](#music21.graph.axis.OffsetAxis.maxValue "music21.graph.axis.OffsetAxis.maxValue") * [`minMaxMeasureOnly`](#music21.graph.axis.OffsetAxis.minMaxMeasureOnly "music21.graph.axis.OffsetAxis.minMaxMeasureOnly") | * [`minValue`](#music21.graph.axis.OffsetAxis.minValue "music21.graph.axis.OffsetAxis.minValue") * [`mostMeasureTicksToShow`](#music21.graph.axis.OffsetAxis.mostMeasureTicksToShow "music21.graph.axis.OffsetAxis.mostMeasureTicksToShow") | * [`offsetStepSize`](#music21.graph.axis.OffsetAxis.offsetStepSize "music21.graph.axis.OffsetAxis.offsetStepSize") * [`useMeasures`](#music21.graph.axis.OffsetAxis.useMeasures "music21.graph.axis.OffsetAxis.useMeasures") |

Instance variables inherited from [`PositionAxis`](#music21.graph.axis.PositionAxis "music21.graph.axis.PositionAxis"):

|  |  |  |
| --- | --- | --- |
| * [`graceNoteQL`](#music21.graph.axis.PositionAxis.graceNoteQL "music21.graph.axis.PositionAxis.graceNoteQL") |  |  |

Instance variables inherited from [`Axis`](#music21.graph.axis.Axis "music21.graph.axis.Axis"):

|  |  |  |
| --- | --- | --- |
| * [`axisDataMap`](#music21.graph.axis.Axis.axisDataMap "music21.graph.axis.Axis.axisDataMap") * [`axisName`](#music21.graph.axis.Axis.axisName "music21.graph.axis.Axis.axisName") | * [`maxValue`](#music21.graph.axis.Axis.maxValue "music21.graph.axis.Axis.maxValue") * [`minValue`](#music21.graph.axis.Axis.minValue "music21.graph.axis.Axis.minValue") | * [`quantities`](#music21.graph.axis.Axis.quantities "music21.graph.axis.Axis.quantities") |

## PitchAxis

class music21.graph.axis.PitchAxis(*client=None*, *axisName='x'*)[[source]](../_modules/music21/graph/axis.html#PitchAxis)
:   Axis subclass for dealing with Pitches

[`PitchAxis`](#music21.graph.axis.PitchAxis "music21.graph.axis.PitchAxis") bases

* [`Axis`](#music21.graph.axis.Axis "music21.graph.axis.Axis")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`PitchAxis`](#music21.graph.axis.PitchAxis "music21.graph.axis.PitchAxis") read-only properties

Read-only properties inherited from [`Axis`](#music21.graph.axis.Axis "music21.graph.axis.Axis"):

|  |  |  |
| --- | --- | --- |
| * [`stream`](#music21.graph.axis.Axis.stream "music21.graph.axis.Axis.stream") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`PitchAxis`](#music21.graph.axis.PitchAxis "music21.graph.axis.PitchAxis") read/write properties

Read/write properties inherited from [`Axis`](#music21.graph.axis.Axis "music21.graph.axis.Axis"):

|  |  |  |
| --- | --- | --- |
| * [`client`](#music21.graph.axis.Axis.client "music21.graph.axis.Axis.client") | * [`label`](#music21.graph.axis.Axis.label "music21.graph.axis.Axis.label") |  |

[`PitchAxis`](#music21.graph.axis.PitchAxis "music21.graph.axis.PitchAxis") methods

static PitchAxis.makePitchLabelsUnicode(*ticks: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]][[source]](../_modules/music21/graph/axis.html#PitchAxis.makePitchLabelsUnicode)
:   Given a list of ticks, replace all labels with alternative/unicode symbols where necessary.

    ```python
    >>> ticks = [(60, 'C4'), (61, 'C#4'), (62, 'D4'), (63, 'E-4')]
    >>> t2 = graph.axis.PitchAxis.makePitchLabelsUnicode(ticks)
    >>> len(t2)
    4
    >>> [num for num, label in t2]
    [60, 61, 62, 63]
    >>> t2[0]
    (60, 'C4')
    >>> for num, label in t2:
    ...     label
    'C4'
    'C♯4'
    'D4'
    'E♭4'
    ```

Methods inherited from [`Axis`](#music21.graph.axis.Axis "music21.graph.axis.Axis"):

|  |  |  |
| --- | --- | --- |
| * [`extractOneElement()`](#music21.graph.axis.Axis.extractOneElement "music21.graph.axis.Axis.extractOneElement") * [`postProcessData()`](#music21.graph.axis.Axis.postProcessData "music21.graph.axis.Axis.postProcessData") | * [`setBoundariesFromData()`](#music21.graph.axis.Axis.setBoundariesFromData "music21.graph.axis.Axis.setBoundariesFromData") | * [`ticks()`](#music21.graph.axis.Axis.ticks "music21.graph.axis.Axis.ticks") |

[`PitchAxis`](#music21.graph.axis.PitchAxis "music21.graph.axis.PitchAxis") instance variables

PitchAxis.blankLabelUnused
:   bool on whether to hide labels for unused pitches, default True.

PitchAxis.hideUnused
:   bool on whether not to even show a tick when a pitch doesn’t exist.
    default True.

PitchAxis.showEnharmonic
:   bool on whether to show both common enharmonics in labels, default True

PitchAxis.showOctaves
:   bool or ‘few’ about whether to show octave numbers. If ‘few’ then
    only the first pitch in each octave is shown. Default ‘few’

Instance variables inherited from [`Axis`](#music21.graph.axis.Axis "music21.graph.axis.Axis"):

|  |  |  |
| --- | --- | --- |
| * [`axisDataMap`](#music21.graph.axis.Axis.axisDataMap "music21.graph.axis.Axis.axisDataMap") * [`axisName`](#music21.graph.axis.Axis.axisName "music21.graph.axis.Axis.axisName") | * [`maxValue`](#music21.graph.axis.Axis.maxValue "music21.graph.axis.Axis.maxValue") * [`minValue`](#music21.graph.axis.Axis.minValue "music21.graph.axis.Axis.minValue") | * [`quantities`](#music21.graph.axis.Axis.quantities "music21.graph.axis.Axis.quantities") |

## PitchClassAxis

class music21.graph.axis.PitchClassAxis(*client=None*, *axisName='x'*)[[source]](../_modules/music21/graph/axis.html#PitchClassAxis)
:   Axis subclass for dealing with PitchClasses

    By default, axis is not set from data, but set to 0, 11

[`PitchClassAxis`](#music21.graph.axis.PitchClassAxis "music21.graph.axis.PitchClassAxis") bases

* [`PitchAxis`](#music21.graph.axis.PitchAxis "music21.graph.axis.PitchAxis")
* [`Axis`](#music21.graph.axis.Axis "music21.graph.axis.Axis")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`PitchClassAxis`](#music21.graph.axis.PitchClassAxis "music21.graph.axis.PitchClassAxis") read-only properties

Read-only properties inherited from [`Axis`](#music21.graph.axis.Axis "music21.graph.axis.Axis"):

|  |  |  |
| --- | --- | --- |
| * [`stream`](#music21.graph.axis.Axis.stream "music21.graph.axis.Axis.stream") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`PitchClassAxis`](#music21.graph.axis.PitchClassAxis "music21.graph.axis.PitchClassAxis") read/write properties

Read/write properties inherited from [`Axis`](#music21.graph.axis.Axis "music21.graph.axis.Axis"):

|  |  |  |
| --- | --- | --- |
| * [`client`](#music21.graph.axis.Axis.client "music21.graph.axis.Axis.client") | * [`label`](#music21.graph.axis.Axis.label "music21.graph.axis.Axis.label") |  |

[`PitchClassAxis`](#music21.graph.axis.PitchClassAxis "music21.graph.axis.PitchClassAxis") methods

PitchClassAxis.extractOneElement(*n*, *formatDict*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/graph/axis.html#PitchClassAxis.extractOneElement)
:   Override in subclasses

PitchClassAxis.ticks()[[source]](../_modules/music21/graph/axis.html#PitchClassAxis.ticks)
:   Get ticks and labels for pitch classes.

    If showEnharmonic is True (default) then
    when choosing whether to display as sharp or flat use
    the most commonly used enharmonic.

    ```python
    >>> s = corpus.parse('bach/bwv324.xml')
    >>> s.analyze('key')
    <music21.key.Key of G major>
    ```

    ```python
    >>> plotS = graph.plot.PlotStream(s)
    >>> ax = graph.axis.PitchClassAxis(plotS)
    >>> ax.hideUnused = True
    ```

    Ticks returns a list of two-element tuples:

    ```python
    >>> ax.ticks()
    [(0, 'C'), (2, 'D'), ..., (11, 'B')]
    ```

    ```python
    >>> for position, noteName in ax.ticks():
    ...            print(str(position) + ' ' + noteName)
    0 C
    2 D
    3 D♯
    4 E
    6 F♯
    7 G
    9 A
    11 B
    ```

    ```python
    >>> s = corpus.parse('bach/bwv281.xml')
    >>> plotS = graph.plot.PlotStream(s)
    >>> ax = graph.axis.PitchClassAxis(plotS)
    >>> ax.hideUnused = True
    >>> ax.showEnharmonic = True
    ```

    ```python
    >>> for position, noteName in ax.ticks():
    ...            print(str(position) + ' ' + noteName)
    0 C
    2 D
    3 E♭
    4 E
    5 F
    7 G
    9 A
    10 B♭
    11 B
    ```

    ```python
    >>> ax.blankLabelUnused = True
    >>> ax.hideUnused = False
    >>> for position, noteName in ax.ticks():
    ...            print(str(position) + ' ' + noteName)
    0 C
    1
    2 D
    3 E♭
    4 E
    5 F
    6
    7 G
    8
    9 A
    10 B♭
    11 B
    ```

    .showEnharmonic will change here:

    ```python
    >>> s.append(note.Note('A#4'))
    >>> s.append(note.Note('G#4'))
    >>> s.append(note.Note('A-4'))
    >>> s.append(note.Note('A-4'))
    >>> for position, noteName in ax.ticks():
    ...            print(str(position) + ' ' + noteName)
    0 C
    1
    2 D
    3 E♭
    4 E
    5 F
    6
    7 G
    8 G♯/A♭
    9 A
    10 A♯/B♭
    11 B
    ```

    Make sure that Ab shows since there are two of them and only one G#

    ```python
    >>> ax.showEnharmonic = False
    >>> for position, noteName in ax.ticks():
    ...            print(str(position) + ' ' + noteName)
    0 C
    1
    2 D
    3 E♭
    4 E
    5 F
    6
    7 G
    8 A♭
    9 A
    10 B♭
    11 B
    ```

Methods inherited from [`PitchAxis`](#music21.graph.axis.PitchAxis "music21.graph.axis.PitchAxis"):

|  |  |  |
| --- | --- | --- |
| * [`makePitchLabelsUnicode()`](#music21.graph.axis.PitchAxis.makePitchLabelsUnicode "music21.graph.axis.PitchAxis.makePitchLabelsUnicode") |  |  |

Methods inherited from [`Axis`](#music21.graph.axis.Axis "music21.graph.axis.Axis"):

|  |  |  |
| --- | --- | --- |
| * [`postProcessData()`](#music21.graph.axis.Axis.postProcessData "music21.graph.axis.Axis.postProcessData") | * [`setBoundariesFromData()`](#music21.graph.axis.Axis.setBoundariesFromData "music21.graph.axis.Axis.setBoundariesFromData") |  |

[`PitchClassAxis`](#music21.graph.axis.PitchClassAxis "music21.graph.axis.PitchClassAxis") instance variables

Instance variables inherited from [`PitchAxis`](#music21.graph.axis.PitchAxis "music21.graph.axis.PitchAxis"):

|  |  |  |
| --- | --- | --- |
| * [`blankLabelUnused`](#music21.graph.axis.PitchAxis.blankLabelUnused "music21.graph.axis.PitchAxis.blankLabelUnused") * [`hideUnused`](#music21.graph.axis.PitchAxis.hideUnused "music21.graph.axis.PitchAxis.hideUnused") | * [`showEnharmonic`](#music21.graph.axis.PitchAxis.showEnharmonic "music21.graph.axis.PitchAxis.showEnharmonic") | * [`showOctaves`](#music21.graph.axis.PitchAxis.showOctaves "music21.graph.axis.PitchAxis.showOctaves") |

Instance variables inherited from [`Axis`](#music21.graph.axis.Axis "music21.graph.axis.Axis"):

|  |  |  |
| --- | --- | --- |
| * [`axisDataMap`](#music21.graph.axis.Axis.axisDataMap "music21.graph.axis.Axis.axisDataMap") * [`axisName`](#music21.graph.axis.Axis.axisName "music21.graph.axis.Axis.axisName") | * [`maxValue`](#music21.graph.axis.Axis.maxValue "music21.graph.axis.Axis.maxValue") * [`minValue`](#music21.graph.axis.Axis.minValue "music21.graph.axis.Axis.minValue") | * [`quantities`](#music21.graph.axis.Axis.quantities "music21.graph.axis.Axis.quantities") |

## PitchSpaceAxis

class music21.graph.axis.PitchSpaceAxis(*client=None*, *axisName='x'*)[[source]](../_modules/music21/graph/axis.html#PitchSpaceAxis)
:   Axis subclass for dealing with PitchSpace (MIDI numbers)

[`PitchSpaceAxis`](#music21.graph.axis.PitchSpaceAxis "music21.graph.axis.PitchSpaceAxis") bases

* [`PitchAxis`](#music21.graph.axis.PitchAxis "music21.graph.axis.PitchAxis")
* [`Axis`](#music21.graph.axis.Axis "music21.graph.axis.Axis")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`PitchSpaceAxis`](#music21.graph.axis.PitchSpaceAxis "music21.graph.axis.PitchSpaceAxis") read-only properties

Read-only properties inherited from [`Axis`](#music21.graph.axis.Axis "music21.graph.axis.Axis"):

|  |  |  |
| --- | --- | --- |
| * [`stream`](#music21.graph.axis.Axis.stream "music21.graph.axis.Axis.stream") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`PitchSpaceAxis`](#music21.graph.axis.PitchSpaceAxis "music21.graph.axis.PitchSpaceAxis") read/write properties

Read/write properties inherited from [`Axis`](#music21.graph.axis.Axis "music21.graph.axis.Axis"):

|  |  |  |
| --- | --- | --- |
| * [`client`](#music21.graph.axis.Axis.client "music21.graph.axis.Axis.client") | * [`label`](#music21.graph.axis.Axis.label "music21.graph.axis.Axis.label") |  |

[`PitchSpaceAxis`](#music21.graph.axis.PitchSpaceAxis "music21.graph.axis.PitchSpaceAxis") methods

PitchSpaceAxis.extractOneElement(*n*, *formatDict*)[[source]](../_modules/music21/graph/axis.html#PitchSpaceAxis.extractOneElement)
:   Override in subclasses

PitchSpaceAxis.ticks(*dataMin=36*, *dataMax=100*)[[source]](../_modules/music21/graph/axis.html#PitchSpaceAxis.ticks)
:   ```python
    >>> ax = graph.axis.PitchSpaceAxis()
    >>> ax.hideUnused = False
    >>> ax.blankLabelUnused = False
    >>> ax.minValue = 20
    >>> ax.maxValue = 24
    >>> for ps, label in ax.ticks():
    ...     print(str(ps) + ' ' + label)
    20 G♯0
    21 A
    22 B♭
    23 B
    24 C1
    ```

    ```python
    >>> ax.showOctaves = False
    >>> for ps, label in ax.ticks():
    ...     print(str(ps) + ' ' + label)
    20 G♯
    21 A
    22 B♭
    23 B
    24 C
    ```

    ```python
    >>> ax.showOctaves = True
    >>> for ps, label in ax.ticks():
    ...     print(str(ps) + ' ' + label)
    20 G♯0
    21 A0
    22 B♭0
    23 B0
    24 C1
    ```

    ```python
    >>> ax.minValue = 60
    >>> ax.maxValue = 72
    >>> [x for x, y in ax.ticks()]
    [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72]
    ```

    ```python
    >>> bach = corpus.parse('bwv66.6')
    >>> plotS = graph.plot.PlotStream(bach.parts[-1])
    >>> ax = graph.axis.PitchSpaceAxis(plotS)
    >>> ax.hideUnused = False
    >>> ax.minValue = 36
    >>> ax.maxValue = 100
    >>> ticks = ax.ticks()
    >>> ticks[0]  # blank because no note 36 in data
    (36, '')
    >>> ticks[21]
    (57, 'A')
    ```

Methods inherited from [`PitchAxis`](#music21.graph.axis.PitchAxis "music21.graph.axis.PitchAxis"):

|  |  |  |
| --- | --- | --- |
| * [`makePitchLabelsUnicode()`](#music21.graph.axis.PitchAxis.makePitchLabelsUnicode "music21.graph.axis.PitchAxis.makePitchLabelsUnicode") |  |  |

Methods inherited from [`Axis`](#music21.graph.axis.Axis "music21.graph.axis.Axis"):

|  |  |  |
| --- | --- | --- |
| * [`postProcessData()`](#music21.graph.axis.Axis.postProcessData "music21.graph.axis.Axis.postProcessData") | * [`setBoundariesFromData()`](#music21.graph.axis.Axis.setBoundariesFromData "music21.graph.axis.Axis.setBoundariesFromData") |  |

[`PitchSpaceAxis`](#music21.graph.axis.PitchSpaceAxis "music21.graph.axis.PitchSpaceAxis") instance variables

Instance variables inherited from [`PitchAxis`](#music21.graph.axis.PitchAxis "music21.graph.axis.PitchAxis"):

|  |  |  |
| --- | --- | --- |
| * [`blankLabelUnused`](#music21.graph.axis.PitchAxis.blankLabelUnused "music21.graph.axis.PitchAxis.blankLabelUnused") * [`hideUnused`](#music21.graph.axis.PitchAxis.hideUnused "music21.graph.axis.PitchAxis.hideUnused") | * [`showEnharmonic`](#music21.graph.axis.PitchAxis.showEnharmonic "music21.graph.axis.PitchAxis.showEnharmonic") | * [`showOctaves`](#music21.graph.axis.PitchAxis.showOctaves "music21.graph.axis.PitchAxis.showOctaves") |

Instance variables inherited from [`Axis`](#music21.graph.axis.Axis "music21.graph.axis.Axis"):

|  |  |  |
| --- | --- | --- |
| * [`axisDataMap`](#music21.graph.axis.Axis.axisDataMap "music21.graph.axis.Axis.axisDataMap") * [`axisName`](#music21.graph.axis.Axis.axisName "music21.graph.axis.Axis.axisName") | * [`maxValue`](#music21.graph.axis.Axis.maxValue "music21.graph.axis.Axis.maxValue") * [`minValue`](#music21.graph.axis.Axis.minValue "music21.graph.axis.Axis.minValue") | * [`quantities`](#music21.graph.axis.Axis.quantities "music21.graph.axis.Axis.quantities") |

## PitchSpaceOctaveAxis

class music21.graph.axis.PitchSpaceOctaveAxis(*client=None*, *axisName='x'*)[[source]](../_modules/music21/graph/axis.html#PitchSpaceOctaveAxis)
:   An axis similar to pitch classes, but just shows the octaves

[`PitchSpaceOctaveAxis`](#music21.graph.axis.PitchSpaceOctaveAxis "music21.graph.axis.PitchSpaceOctaveAxis") bases

* [`PitchSpaceAxis`](#music21.graph.axis.PitchSpaceAxis "music21.graph.axis.PitchSpaceAxis")
* [`PitchAxis`](#music21.graph.axis.PitchAxis "music21.graph.axis.PitchAxis")
* [`Axis`](#music21.graph.axis.Axis "music21.graph.axis.Axis")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`PitchSpaceOctaveAxis`](#music21.graph.axis.PitchSpaceOctaveAxis "music21.graph.axis.PitchSpaceOctaveAxis") read-only properties

Read-only properties inherited from [`Axis`](#music21.graph.axis.Axis "music21.graph.axis.Axis"):

|  |  |  |
| --- | --- | --- |
| * [`stream`](#music21.graph.axis.Axis.stream "music21.graph.axis.Axis.stream") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`PitchSpaceOctaveAxis`](#music21.graph.axis.PitchSpaceOctaveAxis "music21.graph.axis.PitchSpaceOctaveAxis") read/write properties

Read/write properties inherited from [`Axis`](#music21.graph.axis.Axis "music21.graph.axis.Axis"):

|  |  |  |
| --- | --- | --- |
| * [`client`](#music21.graph.axis.Axis.client "music21.graph.axis.Axis.client") | * [`label`](#music21.graph.axis.Axis.label "music21.graph.axis.Axis.label") |  |

[`PitchSpaceOctaveAxis`](#music21.graph.axis.PitchSpaceOctaveAxis "music21.graph.axis.PitchSpaceOctaveAxis") methods

PitchSpaceOctaveAxis.ticks()[[source]](../_modules/music21/graph/axis.html#PitchSpaceOctaveAxis.ticks)
:   This class does not currently take into account whether the octaves themselves
    are found in the Stream.

    ```python
    >>> ax = graph.axis.PitchSpaceOctaveAxis()
    >>> ax.minValue = 36
    >>> ax.maxValue = 100
    >>> ax.ticks()
    [(36, 'C2'), (48, 'C3'), (60, 'C4'), (72, 'C5'), (84, 'C6'), (96, 'C7')]
    ```

    ```python
    >>> ax.startNameWithOctave = 'A2'
    >>> ax.ticks()
    [(45, 'A2'), (57, 'A3'), (69, 'A4'), (81, 'A5'), (93, 'A6')]
    ```

Methods inherited from [`PitchSpaceAxis`](#music21.graph.axis.PitchSpaceAxis "music21.graph.axis.PitchSpaceAxis"):

|  |  |  |
| --- | --- | --- |
| * [`extractOneElement()`](#music21.graph.axis.PitchSpaceAxis.extractOneElement "music21.graph.axis.PitchSpaceAxis.extractOneElement") |  |  |

Methods inherited from [`PitchAxis`](#music21.graph.axis.PitchAxis "music21.graph.axis.PitchAxis"):

|  |  |  |
| --- | --- | --- |
| * [`makePitchLabelsUnicode()`](#music21.graph.axis.PitchAxis.makePitchLabelsUnicode "music21.graph.axis.PitchAxis.makePitchLabelsUnicode") |  |  |

Methods inherited from [`Axis`](#music21.graph.axis.Axis "music21.graph.axis.Axis"):

|  |  |  |
| --- | --- | --- |
| * [`postProcessData()`](#music21.graph.axis.Axis.postProcessData "music21.graph.axis.Axis.postProcessData") | * [`setBoundariesFromData()`](#music21.graph.axis.Axis.setBoundariesFromData "music21.graph.axis.Axis.setBoundariesFromData") |  |

[`PitchSpaceOctaveAxis`](#music21.graph.axis.PitchSpaceOctaveAxis "music21.graph.axis.PitchSpaceOctaveAxis") instance variables

Instance variables inherited from [`PitchAxis`](#music21.graph.axis.PitchAxis "music21.graph.axis.PitchAxis"):

|  |  |  |
| --- | --- | --- |
| * [`blankLabelUnused`](#music21.graph.axis.PitchAxis.blankLabelUnused "music21.graph.axis.PitchAxis.blankLabelUnused") * [`hideUnused`](#music21.graph.axis.PitchAxis.hideUnused "music21.graph.axis.PitchAxis.hideUnused") | * [`showEnharmonic`](#music21.graph.axis.PitchAxis.showEnharmonic "music21.graph.axis.PitchAxis.showEnharmonic") | * [`showOctaves`](#music21.graph.axis.PitchAxis.showOctaves "music21.graph.axis.PitchAxis.showOctaves") |

Instance variables inherited from [`Axis`](#music21.graph.axis.Axis "music21.graph.axis.Axis"):

|  |  |  |
| --- | --- | --- |
| * [`axisDataMap`](#music21.graph.axis.Axis.axisDataMap "music21.graph.axis.Axis.axisDataMap") * [`axisName`](#music21.graph.axis.Axis.axisName "music21.graph.axis.Axis.axisName") | * [`maxValue`](#music21.graph.axis.Axis.maxValue "music21.graph.axis.Axis.maxValue") * [`minValue`](#music21.graph.axis.Axis.minValue "music21.graph.axis.Axis.minValue") | * [`quantities`](#music21.graph.axis.Axis.quantities "music21.graph.axis.Axis.quantities") |

## PositionAxis

class music21.graph.axis.PositionAxis(*client=None*, *axisName='x'*)[[source]](../_modules/music21/graph/axis.html#PositionAxis)
:   Axis subclass for dealing with Positions

[`PositionAxis`](#music21.graph.axis.PositionAxis "music21.graph.axis.PositionAxis") bases

* [`Axis`](#music21.graph.axis.Axis "music21.graph.axis.Axis")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`PositionAxis`](#music21.graph.axis.PositionAxis "music21.graph.axis.PositionAxis") read-only properties

Read-only properties inherited from [`Axis`](#music21.graph.axis.Axis "music21.graph.axis.Axis"):

|  |  |  |
| --- | --- | --- |
| * [`stream`](#music21.graph.axis.Axis.stream "music21.graph.axis.Axis.stream") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`PositionAxis`](#music21.graph.axis.PositionAxis "music21.graph.axis.PositionAxis") read/write properties

Read/write properties inherited from [`Axis`](#music21.graph.axis.Axis "music21.graph.axis.Axis"):

|  |  |  |
| --- | --- | --- |
| * [`client`](#music21.graph.axis.Axis.client "music21.graph.axis.Axis.client") | * [`label`](#music21.graph.axis.Axis.label "music21.graph.axis.Axis.label") |  |

[`PositionAxis`](#music21.graph.axis.PositionAxis "music21.graph.axis.PositionAxis") methods

Methods inherited from [`Axis`](#music21.graph.axis.Axis "music21.graph.axis.Axis"):

|  |  |  |
| --- | --- | --- |
| * [`extractOneElement()`](#music21.graph.axis.Axis.extractOneElement "music21.graph.axis.Axis.extractOneElement") * [`postProcessData()`](#music21.graph.axis.Axis.postProcessData "music21.graph.axis.Axis.postProcessData") | * [`setBoundariesFromData()`](#music21.graph.axis.Axis.setBoundariesFromData "music21.graph.axis.Axis.setBoundariesFromData") | * [`ticks()`](#music21.graph.axis.Axis.ticks "music21.graph.axis.Axis.ticks") |

[`PositionAxis`](#music21.graph.axis.PositionAxis "music21.graph.axis.PositionAxis") instance variables

PositionAxis.graceNoteQL
:   length to substitute a grace note or other Zero-length element for.
    Default is the length of a 64th note (1/16 of a QL)

Instance variables inherited from [`Axis`](#music21.graph.axis.Axis "music21.graph.axis.Axis"):

|  |  |  |
| --- | --- | --- |
| * [`axisDataMap`](#music21.graph.axis.Axis.axisDataMap "music21.graph.axis.Axis.axisDataMap") * [`axisName`](#music21.graph.axis.Axis.axisName "music21.graph.axis.Axis.axisName") | * [`maxValue`](#music21.graph.axis.Axis.maxValue "music21.graph.axis.Axis.maxValue") * [`minValue`](#music21.graph.axis.Axis.minValue "music21.graph.axis.Axis.minValue") | * [`quantities`](#music21.graph.axis.Axis.quantities "music21.graph.axis.Axis.quantities") |

## QuarterLengthAxis

class music21.graph.axis.QuarterLengthAxis(*client=None*, *axisName='x'*)[[source]](../_modules/music21/graph/axis.html#QuarterLengthAxis)
:   Axis subclass for dealing with QuarterLengths

[`QuarterLengthAxis`](#music21.graph.axis.QuarterLengthAxis "music21.graph.axis.QuarterLengthAxis") bases

* [`PositionAxis`](#music21.graph.axis.PositionAxis "music21.graph.axis.PositionAxis")
* [`Axis`](#music21.graph.axis.Axis "music21.graph.axis.Axis")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`QuarterLengthAxis`](#music21.graph.axis.QuarterLengthAxis "music21.graph.axis.QuarterLengthAxis") read-only properties

Read-only properties inherited from [`Axis`](#music21.graph.axis.Axis "music21.graph.axis.Axis"):

|  |  |  |
| --- | --- | --- |
| * [`stream`](#music21.graph.axis.Axis.stream "music21.graph.axis.Axis.stream") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`QuarterLengthAxis`](#music21.graph.axis.QuarterLengthAxis "music21.graph.axis.QuarterLengthAxis") read/write properties

QuarterLengthAxis.label

Read/write properties inherited from [`Axis`](#music21.graph.axis.Axis "music21.graph.axis.Axis"):

|  |  |  |
| --- | --- | --- |
| * [`client`](#music21.graph.axis.Axis.client "music21.graph.axis.Axis.client") |  |  |

[`QuarterLengthAxis`](#music21.graph.axis.QuarterLengthAxis "music21.graph.axis.QuarterLengthAxis") methods

QuarterLengthAxis.dataFromQL(*ql*)[[source]](../_modules/music21/graph/axis.html#QuarterLengthAxis.dataFromQL)

QuarterLengthAxis.extractOneElement(*n*, *formatDict*)[[source]](../_modules/music21/graph/axis.html#QuarterLengthAxis.extractOneElement)
:   Override in subclasses

QuarterLengthAxis.labelLogTag()[[source]](../_modules/music21/graph/axis.html#QuarterLengthAxis.labelLogTag)
:   Returns a TeX formatted tag to the axis label depending on whether
    the scale is logarithmic or not. Checks .useLogScale

    ```python
    >>> a = graph.axis.QuarterLengthAxis()
    >>> a.useLogScale
    True
    >>> a.labelLogTag()
    ' ($log_2$)'
    ```

    ```python
    >>> a.useLogScale = False
    >>> a.labelLogTag()
    ''
    ```

    ```python
    >>> a.useLogScale = 10
    >>> a.labelLogTag()
    ' ($log_10$)'
    ```

QuarterLengthAxis.remapQuarterLength(*x*)[[source]](../_modules/music21/graph/axis.html#QuarterLengthAxis.remapQuarterLength)
:   Remap a quarter length as its log2. Essentially it’s
    just math.log2(x), but x=0 is replaced with self.graceNoteQL.

QuarterLengthAxis.ticks()[[source]](../_modules/music21/graph/axis.html#QuarterLengthAxis.ticks)
:   Get ticks for quarterLength.

    If remap is True (the default), the remapQuarterLength()
    method will be used to scale displayed quarter lengths
    by log base 2.

    Note that mix and max do nothing, but must be included
    in order to set the tick style.

    ```python
    >>> s = stream.Stream()
    >>> for t in ['32nd', '16th', 'eighth', 'quarter', 'half']:
    ...     n = note.Note()
    ...     n.duration.type = t
    ...     s.append(n)
    ```

    ```python
    >>> plotS = graph.plot.PlotStream(s)
    >>> ax = graph.axis.QuarterLengthAxis(plotS)
    >>> ax.ticks()
    [(-3.0, '0.12'), (-2.0, '0.25'), (-1.0, '0.5'), (0.0, '1.0'), (1.0, '2.0')]
    ```

    ```python
    >>> ax.useLogScale = False
    >>> ax.ticks()
    [(0.125, '0.12'), (0.25, '0.25'), (0.5, '0.5'), (1.0, '1.0'), (2.0, '2.0')]
    >>> ax.useDurationNames = True
    >>> ax.ticks()
    [(0.125, '32nd'), (0.25, '16th'), (0.5, 'Eighth'), (1.0, 'Quarter'), (2.0, 'Half')]
    ```

    ```python
    >>> nGrace = note.Note()
    >>> nGrace.getGrace(inPlace=True)
    >>> s.append(nGrace)
    >>> plotS = graph.plot.PlotStream(s)
    >>> ax = graph.axis.QuarterLengthAxis(plotS)
    >>> ax.ticks()[0]
    (-4.0, '0.0')
    ```

    ```python
    >>> ax.useLogScale = False
    >>> ax.ticks()[0]
    (0.0625, '0.0')
    ```

Methods inherited from [`Axis`](#music21.graph.axis.Axis "music21.graph.axis.Axis"):

|  |  |  |
| --- | --- | --- |
| * [`postProcessData()`](#music21.graph.axis.Axis.postProcessData "music21.graph.axis.Axis.postProcessData") | * [`setBoundariesFromData()`](#music21.graph.axis.Axis.setBoundariesFromData "music21.graph.axis.Axis.setBoundariesFromData") |  |

[`QuarterLengthAxis`](#music21.graph.axis.QuarterLengthAxis "music21.graph.axis.QuarterLengthAxis") instance variables

QuarterLengthAxis.useDurationNames
:   If used then duration names replace numbers for ticks.
    If set, probably will want to change tickFontSize in the graph object

QuarterLengthAxis.useLogScale
:   bool or int for whether to scale numbers logarithmically. Adds (log2) to the
    axis label if used. If True (default) then log2 is assumed. If an int, then
    log the int (say, 10) is used. instead.

Instance variables inherited from [`PositionAxis`](#music21.graph.axis.PositionAxis "music21.graph.axis.PositionAxis"):

|  |  |  |
| --- | --- | --- |
| * [`graceNoteQL`](#music21.graph.axis.PositionAxis.graceNoteQL "music21.graph.axis.PositionAxis.graceNoteQL") |  |  |

Instance variables inherited from [`Axis`](#music21.graph.axis.Axis "music21.graph.axis.Axis"):

|  |  |  |
| --- | --- | --- |
| * [`axisDataMap`](#music21.graph.axis.Axis.axisDataMap "music21.graph.axis.Axis.axisDataMap") * [`axisName`](#music21.graph.axis.Axis.axisName "music21.graph.axis.Axis.axisName") | * [`maxValue`](#music21.graph.axis.Axis.maxValue "music21.graph.axis.Axis.maxValue") * [`minValue`](#music21.graph.axis.Axis.minValue "music21.graph.axis.Axis.minValue") | * [`quantities`](#music21.graph.axis.Axis.quantities "music21.graph.axis.Axis.quantities") |
