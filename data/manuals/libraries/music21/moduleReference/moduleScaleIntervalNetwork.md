Source: https://music21.org/music21docs/moduleReference/moduleScaleIntervalNetwork.html

# music21.scale.intervalNetwork

An IntervalNetwork defines a scale or harmonic unit as a (weighted)
digraph, or directed graph, where pitches are nodes and intervals are
edges. Nodes, however, are not stored; instead, an ordered list of edges
(Intervals) is provided as an archetype of adjacent nodes.

IntervalNetworks are unlike conventional graphs in that each graph must
define a low and high terminus. These points are used to create a cyclic
graph and are treated as point of cyclical overlap.

IntervalNetwork permits the definition of conventional octave repeating
scales or harmonies (abstract chords), non-octave repeating scales and
chords, and ordered interval sequences that might move in multiple
directions.

A scale or harmony may be composed of one or more IntervalNetwork objects.

Both nodes and edges can be weighted to suggest tonics, dominants,
finals, or other attributes of the network.

Changed in v8: nodeId and nodeName standardized. TERMINUS and DIRECTION
are now Enums.

## IntervalNetwork

class music21.scale.intervalNetwork.IntervalNetwork(*edgeList: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[Interval](moduleInterval.html#music21.interval.Interval "music21.interval.Interval") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] = ()*, *octaveDuplicating=False*, *deterministic=True*, *pitchSimplification='maxAccidental'*)[[source]](../_modules/music21/scale/intervalNetwork.html#IntervalNetwork)
:   A graph of undefined Pitch nodes connected by a defined,
    ordered list of [`Interval`](moduleInterval.html#music21.interval.Interval "music21.interval.Interval") objects as edges.

    An octaveDuplicating boolean, if defined, can be used
    to optimize pitch realization routines.

    The deterministic boolean, if defined, can be used to declare that there
    is no probabilistic or multi-pathway segments of this network.

    The pitchSimplification method specifies how to simplify the pitches
    if they spiral out into double and triple sharps, etc. The default is
    ‘maxAccidental’ which specifies that each note can have at most one
    accidental; double-flats and sharps are not allowed. The other choices
    are ‘simplifyEnharmonic’ (which also converts C-, F-, B#, and E# to
    B, E, C, and F respectively, see [`simplifyEnharmonic()`](modulePitch.html#music21.pitch.Pitch.simplifyEnharmonic "music21.pitch.Pitch.simplifyEnharmonic")),
    ‘mostCommon’ (which adds to simplifyEnharmonic the requirement that the
    most common accidental forms be used, so A# becomes B-, G- becomes
    F#, etc. the only ambiguity allowed is that both G# and A- are acceptable),
    and None (or ‘none’) which does not do any simplification.

[`IntervalNetwork`](#music21.scale.intervalNetwork.IntervalNetwork "music21.scale.intervalNetwork.IntervalNetwork") read-only properties

IntervalNetwork.degreeMax
:   Return the largest degree value.

    ```python
    >>> edgeList = ['M2', 'M2', 'm2', 'M2', 'M2', 'M2', 'm2']
    >>> net = scale.intervalNetwork.IntervalNetwork()
    >>> net.fillBiDirectedEdges(edgeList)
    >>> net.degreeMax    # returns eight, as this is the last node
    8
    ```

IntervalNetwork.degreeMaxUnique
:   Return the largest degree value that represents a pitch level
    that is not a terminus of the scale.

    ```python
    >>> edgeList = ['M2', 'M2', 'm2', 'M2', 'M2', 'M2', 'm2']
    >>> net = scale.intervalNetwork.IntervalNetwork()
    >>> net.fillBiDirectedEdges(edgeList)
    >>> net.degreeMaxUnique
    7
    ```

IntervalNetwork.degreeMin
:   Return the lowest degree value.

    ```python
    >>> edgeList = ['M2', 'M2', 'm2', 'M2', 'M2', 'M2', 'm2']
    >>> net = scale.intervalNetwork.IntervalNetwork()
    >>> net.fillBiDirectedEdges(edgeList)
    >>> net.degreeMin
    1
    ```

IntervalNetwork.terminusHighNodes
:   Return a list of last Nodes, or Nodes that contain Terminus.HIGH.

    ```python
    >>> edgeList = ['M2', 'M2', 'm2', 'M2', 'M2', 'M2', 'm2']
    >>> net = scale.intervalNetwork.IntervalNetwork()
    >>> net.fillBiDirectedEdges(edgeList)
    >>> net.terminusHighNodes
    [<music21.scale.intervalNetwork.Node id=Terminus.HIGH>]
    ```

IntervalNetwork.terminusLowNodes
:   Return a list of first Nodes, or Nodes that contain Terminus.LOW.

    ```python
    >>> edgeList = ['M2', 'M2', 'm2', 'M2', 'M2', 'M2', 'm2']
    >>> net = scale.intervalNetwork.IntervalNetwork()
    >>> net.fillBiDirectedEdges(edgeList)
    >>> net.terminusLowNodes
    [<music21.scale.intervalNetwork.Node id=Terminus.LOW>]
    ```

    Note that this list currently always has one element.

[`IntervalNetwork`](#music21.scale.intervalNetwork.IntervalNetwork "music21.scale.intervalNetwork.IntervalNetwork") methods

IntervalNetwork.\_\_eq\_\_(*other*)[[source]](../_modules/music21/scale/intervalNetwork.html#IntervalNetwork.__eq__)
:   ```python
    >>> edgeList1 = ['M2', 'M2', 'm2', 'M2', 'M2', 'M2', 'm2']
    >>> edgeList2 = ['M2', 'M2', 'm2', 'M2', 'A3', 'm2']
    ```

    ```python
    >>> net1 = scale.intervalNetwork.IntervalNetwork()
    >>> net1.fillBiDirectedEdges(edgeList1)
    ```

    ```python
    >>> net2 = scale.intervalNetwork.IntervalNetwork()
    >>> net2.fillBiDirectedEdges(edgeList1)
    ```

    ```python
    >>> net3 = scale.intervalNetwork.IntervalNetwork()
    >>> net3.fillBiDirectedEdges(edgeList2)
    ```

    ```python
    >>> net1 == net2
    True
    >>> net1 == net3
    False
    ```

IntervalNetwork.clear()[[source]](../_modules/music21/scale/intervalNetwork.html#IntervalNetwork.clear)
:   Remove and reset all Nodes and Edges.

IntervalNetwork.degreeModulus(*degree: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](../_modules/music21/scale/intervalNetwork.html#IntervalNetwork.degreeModulus)
:   Return the degree modulus degreeMax - degreeMin.

    ```python
    >>> edgeList = ['M2', 'M2', 'm2', 'M2', 'M2', 'M2', 'm2']
    >>> net = scale.intervalNetwork.IntervalNetwork()
    >>> net.fillBiDirectedEdges(edgeList)
    >>> net.degreeModulus(3)
    3
    >>> net.degreeModulus(8)
    1
    >>> net.degreeModulus(9)
    2
    >>> net.degreeModulus(0)
    7
    ```

IntervalNetwork.fillArbitrary(*nodes*, *edges*)[[source]](../_modules/music21/scale/intervalNetwork.html#IntervalNetwork.fillArbitrary)
:   Fill any arbitrary network given node and edge definitions.

    Nodes must be defined by a dictionary of id and degree values.
    There must be a terminusLow and terminusHigh id as string:

    ```python
    nodes = ({'id': Terminus.LOW, 'degree': 1},
             {'id': 0, 'degree': 2},
             {'id': Terminus.HIGH, 'degree': 3},
            )
    ```

    Edges must be defined by a dictionary of [`Interval`](moduleInterval.html#music21.interval.Interval "music21.interval.Interval")
    strings and connections. Values for id will be automatically assigned.
    Each connection must define direction and pairs of valid node ids:

    ```python
    edges = ({'interval': 'm2',
              'connections': ([Terminus.LOW, 0, Direction.BI],)
              },
             {'interval': 'M3',
              'connections': ([0, Terminus.HIGH, Direction.BI],)
              },
            )
    ```

    ```python
    >>> nodes = ({'id': scale.Terminus.LOW, 'degree': 1},
    ...          {'id': 0, 'degree': 2},
    ...          {'id': scale.Terminus.HIGH, 'degree': 3})
    >>> edges = ({'interval': 'm2',
    ...           'connections': ([scale.Terminus.LOW, 0, scale.Direction.BI],)},
    ...          {'interval': 'M3',
    ...           'connections': ([0, scale.Terminus.HIGH, scale.Direction.BI],)},)
    ```

    ```python
    >>> net = scale.intervalNetwork.IntervalNetwork()
    >>> net.fillArbitrary(nodes, edges)
    >>> net.realizePitch('c4', 1)
    [<music21.pitch.Pitch C4>, <music21.pitch.Pitch D-4>, <music21.pitch.Pitch F4>]
    ```

IntervalNetwork.fillBiDirectedEdges(*edgeList: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[Interval](moduleInterval.html#music21.interval.Interval "music21.interval.Interval") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*)[[source]](../_modules/music21/scale/intervalNetwork.html#IntervalNetwork.fillBiDirectedEdges)
:   Given an ordered list of bi-directed edges given as [`Interval`](moduleInterval.html#music21.interval.Interval "music21.interval.Interval")
    specifications, create and define appropriate Nodes. This
    assumes that all edges are bi-directed and all edges are in order.

    ```python
    >>> edgeList = ['M2', 'M2', 'm2', 'M2', 'M2', 'M2', 'm2']
    >>> net = scale.intervalNetwork.IntervalNetwork()
    >>> net.nodes
    OrderedDict()
    >>> net.edges
    OrderedDict()
    ```

    ```python
    >>> net.fillBiDirectedEdges(edgeList)
    >>> net.nodes
    OrderedDict([(Terminus.LOW, <music21.scale.intervalNetwork.Node id=Terminus.LOW>),
                 (0, <music21.scale.intervalNetwork.Node id=0>),
                 (1, <music21.scale.intervalNetwork.Node id=1>),
                 ...
                 (5, <music21.scale.intervalNetwork.Node id=5>),
                 (Terminus.HIGH, <music21.scale.intervalNetwork.Node id=Terminus.HIGH>)])
    >>> net.edges
    OrderedDict([(0, <music21.scale.intervalNetwork.Edge Direction.BI M2
                        [(Terminus.LOW, 0), (0, Terminus.LOW)]>),
                 (1, <music21.scale.intervalNetwork.Edge Direction.BI M2 [(0, 1), (1, 0)]>),
                 (2, <music21.scale.intervalNetwork.Edge Direction.BI m2 [(1, 2), (2, 1)]>),
                 ...
                 (5, <music21.scale.intervalNetwork.Edge Direction.BI M2 [(4, 5), (5, 4)]>),
                 (6, <music21.scale.intervalNetwork.Edge Direction.BI m2
                        [(5, Terminus.HIGH), (Terminus.HIGH, 5)]>)])
    ```

    ```python
    >>> [str(p) for p in net.realizePitch('g4')]
    ['G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F#5', 'G5']
    >>> net.degreeMin, net.degreeMax
    (1, 8)
    ```

    Using another fill method creates a new network

    ```python
    >>> net.fillBiDirectedEdges(['M3', 'M3', 'M3'])
    >>> [str(p) for p in net.realizePitch('g4')]
    ['G4', 'B4', 'D#5', 'G5']
    >>> net.degreeMin, net.degreeMax
    (1, 4)
    ```

    ```python
    >>> net.fillBiDirectedEdges([interval.Interval('M3'),
    ...                          interval.Interval('M3'),
    ...                          interval.Interval('M3')])
    >>> [str(p) for p in net.realizePitch('c2')]
    ['C2', 'E2', 'G#2', 'B#2']
    ```

IntervalNetwork.fillDirectedEdges(*ascendingEdgeList*, *descendingEdgeList*)[[source]](../_modules/music21/scale/intervalNetwork.html#IntervalNetwork.fillDirectedEdges)
:   Given two lists of edges, one for ascending [`Interval`](moduleInterval.html#music21.interval.Interval "music21.interval.Interval")
    objects and
    another for descending, construct appropriate Nodes and Edges.

    Note that the descending [`Interval`](moduleInterval.html#music21.interval.Interval "music21.interval.Interval") objects
    should be given in ascending form.

IntervalNetwork.fillMelodicMinor()[[source]](../_modules/music21/scale/intervalNetwork.html#IntervalNetwork.fillMelodicMinor)
:   A convenience routine for testing a complex, bi-directional scale.

    ```python
    >>> net = scale.intervalNetwork.IntervalNetwork()
    >>> net.fillMelodicMinor()
    >>> [str(p) for p in net.realizePitch('c4')]
    ['C4', 'D4', 'E-4', 'F4', 'G4', 'A4', 'B4', 'C5']
    ```

static IntervalNetwork.filterPitchList(*pitchTarget: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] | [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")] | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")], [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch"), [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")][[source]](../_modules/music21/scale/intervalNetwork.html#IntervalNetwork.filterPitchList)
:   Given a list or one pitch, check if all are pitch objects; convert if necessary.
    Return a 3-tuple: a list of all pitches, the min value and the max value.

    ```python
    >>> Net = scale.intervalNetwork.IntervalNetwork
    >>> Net.filterPitchList(['c#4', 'f5', 'd3'])
    ([<music21.pitch.Pitch C#4>, <music21.pitch.Pitch F5>, <music21.pitch.Pitch D3>],
     <music21.pitch.Pitch D3>,
     <music21.pitch.Pitch F5>)
    ```

    A single string or pitch can be given.

    ```python
    >>> Net.filterPitchList('c#')
    ([<music21.pitch.Pitch C#>],
     <music21.pitch.Pitch C#>,
     <music21.pitch.Pitch C#>)
    ```

    Empty lists raise value errors:

    ```python
    >>> Net.filterPitchList([])
    Traceback (most recent call last):
    ValueError: There must be at least one pitch given.
    ```

    * Changed in v8: staticmethod. Raise value error on empty

IntervalNetwork.find(*pitchTarget*, *resultsReturned=4*, *comparisonAttribute='pitchClass'*, *alteredDegrees=None*)[[source]](../_modules/music21/scale/intervalNetwork.html#IntervalNetwork.find)
:   Given a collection of pitches, test all transpositions of a realized
    version of this network, and return the number of matches in each for
    each pitch assigned to the first node.

    ```python
    >>> edgeList = ['M2', 'M2', 'm2', 'M2', 'M2', 'M2', 'm2']
    >>> net = scale.intervalNetwork.IntervalNetwork(edgeList)
    ```

    a network built on G or D as

    ```python
    >>> net.find(['g', 'a', 'b', 'd', 'f#'])
    [(5, <music21.pitch.Pitch G>), (5, <music21.pitch.Pitch D>),
     (4, <music21.pitch.Pitch A>), (4, <music21.pitch.Pitch C>)]
    ```

    ```python
    >>> net.find(['g', 'a', 'b', 'c', 'd', 'e', 'f#'])
    [(7, <music21.pitch.Pitch G>), (6, <music21.pitch.Pitch D>),
     (6, <music21.pitch.Pitch C>), (5, <music21.pitch.Pitch A>)]
    ```

    If resultsReturned is None then return every such scale.

IntervalNetwork.findMissing(*pitchReference: [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *nodeId*, *pitchTarget*, *comparisonAttribute='pitchClass'*, *minPitch=None*, *maxPitch=None*, *direction: [Direction](#music21.scale.intervalNetwork.Direction "music21.scale.intervalNetwork.Direction") = Direction.ASCENDING*, *alteredDegrees=None*)[[source]](../_modules/music21/scale/intervalNetwork.html#IntervalNetwork.findMissing)
:   Find all pitches in the realized scale that are not in the
    pitch target network based on the comparison attribute.

    ```python
    >>> edgeList = ['M2', 'M2', 'm2', 'M2', 'M2', 'M2', 'm2']
    >>> net = scale.intervalNetwork.IntervalNetwork(edgeList)
    >>> [str(p) for p in net.realizePitch('G3')]
    ['G3', 'A3', 'B3', 'C4', 'D4', 'E4', 'F#4', 'G4']
    >>> net.findMissing('g', 1, ['g', 'a', 'b', 'd', 'f#'])
    [<music21.pitch.Pitch C5>, <music21.pitch.Pitch E5>]
    ```

IntervalNetwork.getNeighborNodeIds(*pitchReference: [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *nodeName: [Node](#music21.scale.intervalNetwork.Node "music21.scale.intervalNetwork.Node") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Terminus](#music21.scale.intervalNetwork.Terminus "music21.scale.intervalNetwork.Terminus") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *pitchTarget: [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *direction: [Direction](#music21.scale.intervalNetwork.Direction "music21.scale.intervalNetwork.Direction") = Direction.ASCENDING*, *alteredDegrees=None*)[[source]](../_modules/music21/scale/intervalNetwork.html#IntervalNetwork.getNeighborNodeIds)
:   Given a reference pitch assigned to a node id, determine the node ids
    that neighbor this pitch.

    Returns None if an exact match.

    ```python
    >>> edgeList = ['M2', 'M2', 'm2', 'M2', 'M2', 'M2', 'm2']
    >>> net = scale.intervalNetwork.IntervalNetwork(edgeList)
    >>> net.getNeighborNodeIds('c4', 1, 'b-')
    (4, 5)
    >>> net.getNeighborNodeIds('c4', 1, 'b')
    (5, Terminus.HIGH)
    ```

IntervalNetwork.getNext(*nodeStart*, *direction*)[[source]](../_modules/music21/scale/intervalNetwork.html#IntervalNetwork.getNext)
:   Given a Node, get two lists, one of next Edges, and one of next Nodes,
    searching all Edges to find all matches.

    There may be more than one possibility. If so, the caller must look
    at the Edges and determine which to use

    ```python
    >>> edgeList = ['M2', 'M2', 'm2', 'M2', 'M2', 'M2', 'm2']
    >>> net = scale.intervalNetwork.IntervalNetwork()
    >>> net.fillBiDirectedEdges(edgeList)
    >>> net.nodeNameToNodes(1)[0]
    <music21.scale.intervalNetwork.Node id=Terminus.LOW>
    ```

IntervalNetwork.getNodeDegreeDictionary(*equateTermini: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*)[[source]](../_modules/music21/scale/intervalNetwork.html#IntervalNetwork.getNodeDegreeDictionary)
:   Return a dictionary of node-id, node-degree pairs.
    The same degree may be given for each node

    There may not be an unambiguous way to determine the degree.
    Or, a degree may have different meanings when ascending or descending.

    If equateTermini is True, the terminals will be given the same degree.

IntervalNetwork.getPitchFromNodeDegree(*pitchReference: [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *nodeName: [Node](#music21.scale.intervalNetwork.Node "music21.scale.intervalNetwork.Node") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Terminus](#music21.scale.intervalNetwork.Terminus "music21.scale.intervalNetwork.Terminus") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *nodeDegreeTarget*, *direction: [Direction](#music21.scale.intervalNetwork.Direction "music21.scale.intervalNetwork.Direction") = Direction.ASCENDING*, *minPitch=None*, *maxPitch=None*, *alteredDegrees=None*, *equateTermini=True*)[[source]](../_modules/music21/scale/intervalNetwork.html#IntervalNetwork.getPitchFromNodeDegree)
:   Given a reference pitch assigned to node id,
    determine the pitch for the target node degree.

    ```python
    >>> edgeList = ['M2', 'M2', 'm2', 'M2', 'M2', 'M2', 'm2']
    >>> net = scale.intervalNetwork.IntervalNetwork(edgeList)
    >>> [str(p) for p in net.realizePitch(pitch.Pitch('e-2')) ]
    ['E-2', 'F2', 'G2', 'A-2', 'B-2', 'C3', 'D3', 'E-3']
    >>> net.getPitchFromNodeDegree('e4', 1, 1)
    <music21.pitch.Pitch E4>
    >>> net.getPitchFromNodeDegree('e4', 1, 7)  # seventh scale degree
    <music21.pitch.Pitch D#5>
    >>> net.getPitchFromNodeDegree('e4', 1, 8)
    <music21.pitch.Pitch E4>
    >>> net.getPitchFromNodeDegree('e4', 1, 9)
    <music21.pitch.Pitch F#4>
    >>> net.getPitchFromNodeDegree('e4', 1, 3, minPitch='c2', maxPitch='c3')
    <music21.pitch.Pitch G#2>
    ```

    This will always get the lowest pitch:

    ```python
    >>> net.getPitchFromNodeDegree('e4', 1, 3, minPitch='c2', maxPitch='c10')
    <music21.pitch.Pitch G#2>
    ```

    ```python
    >>> net.fillMelodicMinor()
    >>> net.getPitchFromNodeDegree('c', 1, 5)
    <music21.pitch.Pitch G4>
    >>> net.getPitchFromNodeDegree('c', 1, 6, scale.Direction.ASCENDING)
    <music21.pitch.Pitch A4>
    >>> net.getPitchFromNodeDegree('c', 1, 6, scale.Direction.DESCENDING)
    <music21.pitch.Pitch A-4>
    ```

IntervalNetwork.getRelativeNodeDegree(*pitchReference: [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *nodeId*, *pitchTarget: [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *comparisonAttribute='ps'*, *direction: [Direction](#music21.scale.intervalNetwork.Direction "music21.scale.intervalNetwork.Direction") = Direction.ASCENDING*, *alteredDegrees=None*)[[source]](../_modules/music21/scale/intervalNetwork.html#IntervalNetwork.getRelativeNodeDegree)
:   Given a reference pitch assigned to node id,
    determine the relative node degree of pitchTarget,
    even if displaced over multiple octaves

    Comparison Attribute determines what will be used to determine
    equality. Use ps (default) for post-tonal uses. name for
    tonal, and step for diatonic.

    ```python
    >>> edgeList = ['M2', 'M2', 'm2', 'M2', 'M2', 'M2', 'm2']
    >>> net = scale.intervalNetwork.IntervalNetwork(edgeList)
    >>> [str(p) for p in net.realizePitch(pitch.Pitch('e-2')) ]
    ['E-2', 'F2', 'G2', 'A-2', 'B-2', 'C3', 'D3', 'E-3']
    ```

    ```python
    >>> net.getRelativeNodeDegree('e-2', 1, 'd3')  # if e- is tonic, what is d3
    7
    ```

    For an octave repeating network, the neither pitch’s octave matters:

    ```python
    >>> net.getRelativeNodeDegree('e-', 1, 'd5')  # if e- is tonic, what is d3
    7
    >>> net.getRelativeNodeDegree('e-2', 1, 'd')  # if e- is tonic, what is d3
    7
    ```

    ```python
    >>> net.getRelativeNodeDegree('e3', 1, 'd5') is None
    True
    >>> net.getRelativeNodeDegree('e3', 1, 'd5', comparisonAttribute='step')
    7
    >>> net.getRelativeNodeDegree('e3', 1, 'd', comparisonAttribute='step')
    7
    ```

    ```python
    >>> net.getRelativeNodeDegree('e-3', 1, 'b-3')
    5
    ```

    ```python
    >>> net.getRelativeNodeDegree('e-3', 1, 'e-5')
    1
    >>> net.getRelativeNodeDegree('e-2', 1, 'f3')
    2
    >>> net.getRelativeNodeDegree('e-3', 1, 'b6') is None
    True
    ```

    ```python
    >>> net.getRelativeNodeDegree('e-3', 1, 'e-2')
    1
    >>> net.getRelativeNodeDegree('e-3', 1, 'd3')
    7
    >>> net.getRelativeNodeDegree('e-3', 1, 'e-3')
    1
    >>> net.getRelativeNodeDegree('e-3', 1, 'b-1')
    5
    ```

    ```python
    >>> edgeList = ['p4', 'p4', 'p4']  # a non octave-repeating scale
    >>> net = scale.intervalNetwork.IntervalNetwork(edgeList)
    >>> [str(p) for p in net.realizePitch('f2')]
    ['F2', 'B-2', 'E-3', 'A-3']
    >>> [str(p) for p in net.realizePitch('f2', 1, 'f2', 'f6')]
    ['F2', 'B-2', 'E-3', 'A-3', 'D-4', 'G-4', 'C-5', 'F-5', 'A5', 'D6']
    ```

    ```python
    >>> net.getRelativeNodeDegree('f2', 1, 'a-3')  # could be 4 or 1
    1
    >>> net.getRelativeNodeDegree('f2', 1, 'd-4')  # 2 is correct
    2
    >>> net.getRelativeNodeDegree('f2', 1, 'g-4')  # 3 is correct
    3
    >>> net.getRelativeNodeDegree('f2', 1, 'c-5')  # could be 4 or 1
    1
    >>> net.getRelativeNodeDegree('f2', 1, 'e--6')  # could be 4 or 1
    1
    ```

    ```python
    >>> [str(p) for p in net.realizePitch('f6', 1, 'f2', 'f6')]
    ['G#2', 'C#3', 'F#3', 'B3', 'E4', 'A4', 'D5', 'G5', 'C6', 'F6']
    ```

    ```python
    >>> net.getRelativeNodeDegree('f6', 1, 'd5')
    1
    >>> net.getRelativeNodeDegree('f6', 1, 'g5')
    2
    >>> net.getRelativeNodeDegree('f6', 1, 'a4')
    3
    >>> net.getRelativeNodeDegree('f6', 1, 'e4')
    2
    >>> net.getRelativeNodeDegree('f6', 1, 'b3')
    1
    ```

IntervalNetwork.getRelativeNodeId(*pitchReference: [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *nodeId: [Node](#music21.scale.intervalNetwork.Node "music21.scale.intervalNetwork.Node") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Terminus](#music21.scale.intervalNetwork.Terminus "music21.scale.intervalNetwork.Terminus") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *pitchTarget: [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") | [Note](moduleNote.html#music21.note.Note "music21.note.Note") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *\**, *comparisonAttribute: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = 'ps'*, *direction: [Direction](#music21.scale.intervalNetwork.Direction "music21.scale.intervalNetwork.Direction") = Direction.ASCENDING*, *alteredDegrees=None*)[[source]](../_modules/music21/scale/intervalNetwork.html#IntervalNetwork.getRelativeNodeId)
:   Given a reference pitch assigned to node id, determine the
    relative node id of pitchTarget, even if displaced over multiple octaves

    The nodeId parameter may be
    a [`Node`](#music21.scale.intervalNetwork.Node "music21.scale.intervalNetwork.Node") object, a node degree,
    a terminus string, or a None (indicating Terminus.LOW).

    Returns None if no match.

    If getNeighbor is True, or direction, the nearest node will be returned.

    If more than one node defines the same pitch, Node weights are used
    to select a single node.

    ```python
    >>> edgeList = ['M2', 'M2', 'm2', 'M2', 'M2', 'M2', 'm2']
    >>> net = scale.intervalNetwork.IntervalNetwork(edgeList)
    >>> net.getRelativeNodeId('a', 1, 'a4')
    Terminus.LOW
    >>> net.getRelativeNodeId('a', 1, 'b4')
    0
    >>> net.getRelativeNodeId('a', 1, 'c#4')
    1
    >>> net.getRelativeNodeId('a', 1, 'c4', comparisonAttribute='step')
    1
    >>> net.getRelativeNodeId('a', 1, 'c', comparisonAttribute='step')
    1
    >>> net.getRelativeNodeId('a', 1, 'b-4') is None
    True
    ```

IntervalNetwork.getUnalteredPitch(*pitchObj*, *nodeObj*, *\**, *direction=Direction.BI*, *alteredDegrees=None*) → [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")[[source]](../_modules/music21/scale/intervalNetwork.html#IntervalNetwork.getUnalteredPitch)
:   Given a node and alteredDegrees get the unaltered pitch, or return the current object

IntervalNetwork.match(*pitchReference: [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *nodeId*, *pitchTarget*, *comparisonAttribute='pitchClass'*, *alteredDegrees=None*)[[source]](../_modules/music21/scale/intervalNetwork.html#IntervalNetwork.match)
:   Given one or more pitches in pitchTarget, return a
    tuple of a list of matched pitches, and a list of unmatched pitches.

    ```python
    >>> edgeList = ['M2', 'M2', 'm2', 'M2', 'M2', 'M2', 'm2']
    >>> net = scale.intervalNetwork.IntervalNetwork(edgeList)
    >>> [str(p) for p in net.realizePitch('e-2')]
    ['E-2', 'F2', 'G2', 'A-2', 'B-2', 'C3', 'D3', 'E-3']
    ```

    ```python
    >>> net.match('e-2', 1, 'c3')  # if e- is tonic, is 'c3' in the scale?
    ([<music21.pitch.Pitch C3>], [])
    ```

    ```python
    >>> net.match('e-2', 1, 'd3')
    ([<music21.pitch.Pitch D3>], [])
    ```

    ```python
    >>> net.match('e-2', 1, 'd#3')
    ([<music21.pitch.Pitch D#3>], [])
    ```

    ```python
    >>> net.match('e-2', 1, 'e3')
    ([], [<music21.pitch.Pitch E3>])
    ```

    ```python
    >>> pitchTarget = [pitch.Pitch('b-2'), pitch.Pitch('b2'), pitch.Pitch('c3')]
    >>> net.match('e-2', 1, pitchTarget)
    ([<music21.pitch.Pitch B-2>, <music21.pitch.Pitch C3>], [<music21.pitch.Pitch B2>])
    ```

    ```python
    >>> pitchTarget = ['b-2', 'b2', 'c3', 'e-3', 'e#3', 'f2', 'e--2']
    >>> (matched, unmatched) = net.match('e-2', 1, pitchTarget)
    >>> [str(p) for p in matched]
    ['B-2', 'C3', 'E-3', 'E#3', 'F2', 'E--2']
    >>> unmatched
    [<music21.pitch.Pitch B2>]
    ```

IntervalNetwork.nextPitch(*pitchReference: [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *nodeName: [Node](#music21.scale.intervalNetwork.Node "music21.scale.intervalNetwork.Node") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Terminus](#music21.scale.intervalNetwork.Terminus "music21.scale.intervalNetwork.Terminus") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *pitchOrigin: [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *\**, *direction: [Direction](#music21.scale.intervalNetwork.Direction "music21.scale.intervalNetwork.Direction") = Direction.ASCENDING*, *stepSize=1*, *alteredDegrees=None*, *getNeighbor: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [Direction](#music21.scale.intervalNetwork.Direction "music21.scale.intervalNetwork.Direction") = True*)[[source]](../_modules/music21/scale/intervalNetwork.html#IntervalNetwork.nextPitch)
:   Given a pitchReference, nodeName, and a pitch origin, return the next pitch.

    The nodeName parameter may be a [`Node`](#music21.scale.intervalNetwork.Node "music21.scale.intervalNetwork.Node") object,
    a node degree, a Terminus Enum, or a None (indicating Terminus.LOW).

    ```python
    >>> edgeList = ['M2', 'M2', 'm2', 'M2', 'M2', 'M2', 'm2']
    >>> net = scale.intervalNetwork.IntervalNetwork()
    >>> net.fillBiDirectedEdges(edgeList)
    >>> net.nextPitch('g', 1, 'f#5', direction=scale.Direction.ASCENDING)
    <music21.pitch.Pitch G5>
    >>> net.nextPitch('g', 1, 'f#5', direction=scale.Direction.DESCENDING)
    <music21.pitch.Pitch E5>
    ```

    The stepSize parameter can be configured to permit different sized steps
    in the specified direction.

    ```python
    >>> net.nextPitch('g', 1, 'f#5',
    ...               direction=scale.Direction.ASCENDING,
    ...               stepSize=2)
    <music21.pitch.Pitch A5>
    ```

    Altered degrees can be given to temporarily change the pitches returned
    without affecting the network as a whole.

    ```python
    >>> alteredDegrees = {2: {'direction': scale.Direction.BI,
    ...                       'interval': interval.Interval('-a1')}}
    >>> net.nextPitch('g', 1, 'g2',
    ...               direction=scale.Direction.ASCENDING,
    ...               alteredDegrees=alteredDegrees)
    <music21.pitch.Pitch A-2>
    >>> net.nextPitch('g', 1, 'a-2',
    ...               direction=scale.Direction.ASCENDING,
    ...               alteredDegrees=alteredDegrees)
    <music21.pitch.Pitch B2>
    ```

IntervalNetwork.nodeIdToDegree(*nId*)[[source]](../_modules/music21/scale/intervalNetwork.html#IntervalNetwork.nodeIdToDegree)
:   Given a strict node id (the .id attribute of the Node), return the degree.

    There may not be an unambiguous way to determine the degree.
    Or, a degree may have different meanings when ascending or descending.

IntervalNetwork.nodeIdToEdgeDirections(*nId*)[[source]](../_modules/music21/scale/intervalNetwork.html#IntervalNetwork.nodeIdToEdgeDirections)
:   Given a Node id, find all edges associated
    with this node and report on their directions

    ```python
    >>> net = scale.intervalNetwork.IntervalNetwork()
    >>> net.fillMelodicMinor()
    >>> net.nodeIdToEdgeDirections(scale.Terminus.LOW)
    [Direction.BI]
    >>> net.nodeIdToEdgeDirections(0)
    [Direction.BI, Direction.BI]
    >>> net.nodeIdToEdgeDirections(6)
    [Direction.ASCENDING, Direction.ASCENDING]
    >>> net.nodeIdToEdgeDirections(5)
    [Direction.DESCENDING, Direction.DESCENDING]
    ```

    This node has bi-directional (from below),
    ascending (to above), and descending (from above)
    edge connections connections

    ```python
    >>> net.nodeIdToEdgeDirections(3)
    [Direction.BI, Direction.ASCENDING, Direction.DESCENDING]
    ```

IntervalNetwork.nodeNameToNodes(*nodeId: [Node](#music21.scale.intervalNetwork.Node "music21.scale.intervalNetwork.Node") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Terminus](#music21.scale.intervalNetwork.Terminus "music21.scale.intervalNetwork.Terminus") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *\**, *equateTermini=True*, *permitDegreeModuli=True*)[[source]](../_modules/music21/scale/intervalNetwork.html#IntervalNetwork.nodeNameToNodes)
:   The nodeId parameter may be a [`Node`](#music21.scale.intervalNetwork.Node "music21.scale.intervalNetwork.Node") object,
    a node degree (as a number), a terminus string, or a None (indicating Terminus.LOW).

    Return a list of Node objects that match this identification.

    If equateTermini is True, and the name given is a degree number,
    then the first terminal will return both the first and last.

    ```python
    >>> edgeList = ['M2', 'M2', 'm2', 'M2', 'M2', 'M2', 'm2']
    >>> net = scale.intervalNetwork.IntervalNetwork()
    >>> net.fillBiDirectedEdges(edgeList)
    >>> net.nodeNameToNodes(1)[0]
    <music21.scale.intervalNetwork.Node id=Terminus.LOW>
    >>> net.nodeNameToNodes(scale.Terminus.HIGH)
    [<music21.scale.intervalNetwork.Node id=Terminus.HIGH>]
    >>> net.nodeNameToNodes(scale.Terminus.LOW)
    [<music21.scale.intervalNetwork.Node id=Terminus.LOW>]
    ```

    Test using a nodeStep, or an integer nodeName

    ```python
    >>> net.nodeNameToNodes(1)
    [<music21.scale.intervalNetwork.Node id=Terminus.LOW>,
     <music21.scale.intervalNetwork.Node id=Terminus.HIGH>]
    >>> net.nodeNameToNodes(1, equateTermini=False)
    [<music21.scale.intervalNetwork.Node id=Terminus.LOW>]
    >>> net.nodeNameToNodes(2)
    [<music21.scale.intervalNetwork.Node id=0>]
    ```

    With degree moduli, degree zero is the top-most non-terminal
    (since terminals are redundant)

    ```python
    >>> net.nodeNameToNodes(0)
    [<music21.scale.intervalNetwork.Node id=5>]
    >>> net.nodeNameToNodes(-1)
    [<music21.scale.intervalNetwork.Node id=4>]
    >>> net.nodeNameToNodes(8)
    [<music21.scale.intervalNetwork.Node id=Terminus.LOW>,
     <music21.scale.intervalNetwork.Node id=Terminus.HIGH>]
    ```

IntervalNetwork.processAlteredNodes(*alteredDegrees*, *n*, *p*, *\**, *direction*)[[source]](../_modules/music21/scale/intervalNetwork.html#IntervalNetwork.processAlteredNodes)
:   Return an altered pitch for given node, if an alteration is specified
    in the alteredDegrees dictionary

IntervalNetwork.realize(*pitchReference: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")*, *nodeId: [Node](#music21.scale.intervalNetwork.Node "music21.scale.intervalNetwork.Node") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Terminus](#music21.scale.intervalNetwork.Terminus "music21.scale.intervalNetwork.Terminus") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *minPitch: [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *maxPitch: [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *direction: [Direction](#music21.scale.intervalNetwork.Direction "music21.scale.intervalNetwork.Direction") = Direction.ASCENDING*, *alteredDegrees=None*, *reverse=False*)[[source]](../_modules/music21/scale/intervalNetwork.html#IntervalNetwork.realize)
:   Realize the nodes of this network based on a pitch assigned to a
    valid nodeId, where nodeId can be specified by integer
    (starting from 1) or key (a tuple of origin, destination keys).

    Without a min or max pitch, the given pitch reference is assigned
    to the designated node, and then both ascends to the terminus and
    descends to the terminus.

    The alteredDegrees dictionary permits creating mappings between
    node degree and direction and [`Interval`](moduleInterval.html#music21.interval.Interval "music21.interval.Interval")
    based transpositions.

    Returns two lists, a list of pitches, and a list of Node keys.

    ```python
    >>> edgeList = ['M2', 'M2', 'm2', 'M2', 'M2', 'M2', 'm2']
    >>> net = scale.intervalNetwork.IntervalNetwork()
    >>> net.fillBiDirectedEdges(edgeList)
    >>> (pitches, nodeKeys) = net.realize('c2', 1, 'c2', 'c3')
    >>> [str(p) for p in pitches]
    ['C2', 'D2', 'E2', 'F2', 'G2', 'A2', 'B2', 'C3']
    >>> nodeKeys
    [Terminus.LOW, 0, 1, 2, 3, 4, 5, Terminus.HIGH]
    ```

    ```python
    >>> alteredDegrees = {7: {'direction': scale.Direction.BI,
    ...                       'interval': interval.Interval('-a1')}}
    >>> (pitches, nodeKeys) = net.realize('c2', 1, 'c2', 'c4', alteredDegrees=alteredDegrees)
    >>> [str(p) for p in pitches]
    ['C2', 'D2', 'E2', 'F2', 'G2', 'A2', 'B-2', 'C3',
     'D3', 'E3', 'F3', 'G3', 'A3', 'B-3', 'C4']
    >>> nodeKeys
    [Terminus.LOW, 0, 1, 2, 3, 4, 5, Terminus.HIGH, 0, 1, 2, 3, 4, 5, Terminus.HIGH]
    ```

IntervalNetwork.realizeAscending(*pitchReference: [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *nodeId: [Node](#music21.scale.intervalNetwork.Node "music21.scale.intervalNetwork.Node") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Terminus](#music21.scale.intervalNetwork.Terminus "music21.scale.intervalNetwork.Terminus") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *minPitch: [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *maxPitch: [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\**, *alteredDegrees=None*, *fillMinMaxIfNone=False*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")], [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Terminus](#music21.scale.intervalNetwork.Terminus "music21.scale.intervalNetwork.Terminus") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]][[source]](../_modules/music21/scale/intervalNetwork.html#IntervalNetwork.realizeAscending)
:   Given a reference pitch, realize upwards to a maximum pitch.

    ```python
    >>> edgeList = ['M2', 'M2', 'm2', 'M2', 'M2', 'M2', 'm2']
    ```

    ```python
    >>> net = scale.intervalNetwork.IntervalNetwork()
    >>> net.fillBiDirectedEdges(edgeList)
    >>> (pitches, nodeKeys) = net.realizeAscending('c2', 1, 'c5', 'c6')
    >>> [str(p) for p in pitches]
    ['C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5', 'C6']
    >>> nodeKeys
    [Terminus.HIGH, 0, 1, 2, 3, 4, 5, Terminus.HIGH]
    ```

    ```python
    >>> net = scale.intervalNetwork.IntervalNetwork(octaveDuplicating=True)
    >>> net.fillBiDirectedEdges(edgeList)
    >>> (pitches, nodeKeys) = net.realizeAscending('c2', 1, 'c5', 'c6')
    >>> [str(p) for p in pitches]
    ['C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5', 'C6']
    >>> nodeKeys
    [Terminus.LOW, 0, 1, 2, 3, 4, 5, Terminus.HIGH]
    ```

IntervalNetwork.realizeDescending(*pitchReference: [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *nodeId: [Node](#music21.scale.intervalNetwork.Node "music21.scale.intervalNetwork.Node") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Terminus](#music21.scale.intervalNetwork.Terminus "music21.scale.intervalNetwork.Terminus") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *minPitch: [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *maxPitch: [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\**, *alteredDegrees=None*, *includeFirst=False*, *fillMinMaxIfNone=False*, *reverse=True*)[[source]](../_modules/music21/scale/intervalNetwork.html#IntervalNetwork.realizeDescending)
:   Given a reference pitch, realize downward to a minimum.

    If no minimum is given, the terminus is used.

    If includeFirst is False, the starting (highest) pitch will not be included.

    If fillMinMaxIfNone is True, a min and max will be artificially
    derived from an ascending scale and used as min and max values.

    ```python
    >>> edgeList = ['M2', 'M2', 'm2', 'M2', 'M2', 'M2', 'm2']
    >>> net = scale.intervalNetwork.IntervalNetwork()
    >>> net.fillBiDirectedEdges(edgeList)
    >>> net.realizeDescending('c2', 1, 'c3')  # minimum is above ref
    ([], [])
    >>> (pitches, nodeKeys) = net.realizeDescending('c3', 1, 'c2')
    >>> [str(p) for p in pitches]
    ['C2', 'D2', 'E2', 'F2', 'G2', 'A2', 'B2']
    >>> nodeKeys
    [Terminus.LOW, 0, 1, 2, 3, 4, 5]
    >>> (pitches, nodeKeys) = net.realizeDescending('c3', 1, 'c2', includeFirst=True)
    >>> [str(p) for p in pitches]
    ['C2', 'D2', 'E2', 'F2', 'G2', 'A2', 'B2', 'C3']
    >>> nodeKeys
    [Terminus.LOW, 0, 1, 2, 3, 4, 5, Terminus.LOW]
    ```

    ```python
    >>> (pitches, nodeKeys) = net.realizeDescending('a6', scale.Terminus.HIGH)
    >>> [str(p) for p in pitches]
    ['A5', 'B5', 'C#6', 'D6', 'E6', 'F#6', 'G#6']
    >>> nodeKeys
    [Terminus.LOW, 0, 1, 2, 3, 4, 5]
    ```

    ```python
    >>> (pitches, nodeKeys) = net.realizeDescending('a6', scale.Terminus.HIGH,
    ...                                             includeFirst=True)
    >>> [str(p) for p in pitches]
    ['A5', 'B5', 'C#6', 'D6', 'E6', 'F#6', 'G#6', 'A6']
    >>> nodeKeys
    [Terminus.LOW, 0, 1, 2, 3, 4, 5, Terminus.HIGH]
    ```

    ```python
    >>> net = scale.intervalNetwork.IntervalNetwork(octaveDuplicating=True)
    >>> net.fillBiDirectedEdges(edgeList)
    >>> (pitches, nodeKeys) = net.realizeDescending('c2', 1, 'c0', 'c1')
    >>> [str(p) for p in pitches]
    ['C0', 'D0', 'E0', 'F0', 'G0', 'A0', 'B0']
    >>> nodeKeys
    [Terminus.LOW, 0, 1, 2, 3, 4, 5]
    ```

IntervalNetwork.realizeIntervals(*nodeId: [Node](#music21.scale.intervalNetwork.Node "music21.scale.intervalNetwork.Node") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Terminus](#music21.scale.intervalNetwork.Terminus "music21.scale.intervalNetwork.Terminus") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *minPitch: [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *maxPitch: [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *direction: [Direction](#music21.scale.intervalNetwork.Direction "music21.scale.intervalNetwork.Direction") = Direction.ASCENDING*, *alteredDegrees=None*, *reverse=False*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Interval](moduleInterval.html#music21.interval.Interval "music21.interval.Interval")][[source]](../_modules/music21/scale/intervalNetwork.html#IntervalNetwork.realizeIntervals)
:   Realize the sequence of intervals between the specified pitches, or the termini.

    ```python
    >>> edgeList = ['M2', 'M2', 'm2', 'M2', 'M2', 'M2', 'm2']
    >>> net = scale.intervalNetwork.IntervalNetwork()
    >>> net.fillBiDirectedEdges(edgeList)
    >>> net.realizeIntervals()
    [<music21.interval.Interval M2>, <music21.interval.Interval M2>,
     <music21.interval.Interval m2>, <music21.interval.Interval M2>,
     <music21.interval.Interval M2>, <music21.interval.Interval M2>,
     <music21.interval.Interval m2>]
    ```

IntervalNetwork.realizeMinMax(*pitchReference: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")*, *nodeId: [Node](#music21.scale.intervalNetwork.Node "music21.scale.intervalNetwork.Node") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Terminus](#music21.scale.intervalNetwork.Terminus "music21.scale.intervalNetwork.Terminus") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *alteredDegrees=None*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch"), [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")][[source]](../_modules/music21/scale/intervalNetwork.html#IntervalNetwork.realizeMinMax)
:   Realize the min and max pitches of the scale, or the min and max values
    found between two termini.

    This suggests that min and max might be beyond the terminus.

    ```python
    >>> edgeList = ['M2', 'M2', 'm2', 'M2', 'M2', 'M2', 'm2']
    >>> net = scale.intervalNetwork.IntervalNetwork()
    >>> net.fillBiDirectedEdges(edgeList)
    ```

    ```python
    >>> net.realizeMinMax(pitch.Pitch('C4'))
    (<music21.pitch.Pitch C4>, <music21.pitch.Pitch C6>)
    >>> net.realizeMinMax(pitch.Pitch('B-5'))
    (<music21.pitch.Pitch B-5>, <music21.pitch.Pitch B-7>)
    ```

    Note that it might not always be two octaves apart

    # s = scale.AbstractDiatonicScale(‘major’)
    # s.\_net.realizeMinMax(pitch.Pitch(‘D2’))
    # (<music21.pitch.Pitch D2>, <music21.pitch.Pitch D3>)

IntervalNetwork.realizePitch(*pitchReference: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")*, *nodeId: [Node](#music21.scale.intervalNetwork.Node "music21.scale.intervalNetwork.Node") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Terminus](#music21.scale.intervalNetwork.Terminus "music21.scale.intervalNetwork.Terminus") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *minPitch: [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *maxPitch: [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *direction: [Direction](#music21.scale.intervalNetwork.Direction "music21.scale.intervalNetwork.Direction") = Direction.ASCENDING*, *alteredDegrees=None*, *reverse=False*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")][[source]](../_modules/music21/scale/intervalNetwork.html#IntervalNetwork.realizePitch)
:   Realize the native nodes of this network based on a pitch
    assigned to a valid nodeId, where nodeId can be specified by integer
    (starting from 1) or key (a tuple of origin, destination keys).

    The nodeId, when a simple, linear network, can be used as a scale degree
    value starting from one.

    ```python
    >>> edgeList = ['M2', 'M2', 'm2', 'M2', 'M2', 'M2', 'm2']
    >>> net = scale.intervalNetwork.IntervalNetwork()
    >>> net.fillBiDirectedEdges(edgeList)
    >>> [str(p) for p in net.realizePitch(pitch.Pitch('G3'))]
    ['G3', 'A3', 'B3', 'C4', 'D4', 'E4', 'F#4', 'G4']
    ```

    G3 is the fifth (scale) degree

    ```python
    >>> [str(p) for p in net.realizePitch(pitch.Pitch('G3'), 5)]
    ['C3', 'D3', 'E3', 'F3', 'G3', 'A3', 'B3', 'C4']
    ```

    G3 is the seventh (scale) degree

    ```python
    >>> [str(p) for p in net.realizePitch(pitch.Pitch('G3'), 7) ]
    ['A-2', 'B-2', 'C3', 'D-3', 'E-3', 'F3', 'G3', 'A-3']
    ```

    ```python
    >>> [str(p) for p in net.realizePitch(pitch.Pitch('f#3'), 1, 'f2', 'f3') ]
    ['E#2', 'F#2', 'G#2', 'A#2', 'B2', 'C#3', 'D#3', 'E#3']
    ```

    ```python
    >>> [str(p) for p in net.realizePitch(pitch.Pitch('a#2'), 7, 'c6', 'c7')]
    ['C#6', 'D#6', 'E6', 'F#6', 'G#6', 'A#6', 'B6']
    ```

    Circle of fifths

    ```python
    >>> edgeList = ['P5'] * 6 + ['d6'] + ['P5'] * 5
    >>> net5ths = scale.intervalNetwork.IntervalNetwork()
    >>> net5ths.fillBiDirectedEdges(edgeList)
    >>> [str(p) for p in net5ths.realizePitch(pitch.Pitch('C1'))]
    ['C1', 'G1', 'D2', 'A2', 'E3', 'B3', 'F#4', 'D-5', 'A-5', 'E-6', 'B-6', 'F7', 'C8']
    >>> [str(p) for p in net5ths.realizePitch(pitch.Pitch('C2'))]
    ['C2', 'G2', 'D3', 'A3', 'E4', 'B4', 'F#5', 'D-6', 'A-6', 'E-7', 'B-7', 'F8', 'C9']
    ```

IntervalNetwork.realizePitchByDegree(*pitchReference: [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *nodeId: [Node](#music21.scale.intervalNetwork.Node "music21.scale.intervalNetwork.Node") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Terminus](#music21.scale.intervalNetwork.Terminus "music21.scale.intervalNetwork.Terminus") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *nodeDegreeTargets=(1,)*, *minPitch: [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *maxPitch: [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *direction: [Direction](#music21.scale.intervalNetwork.Direction "music21.scale.intervalNetwork.Direction") = Direction.ASCENDING*, *alteredDegrees=None*)[[source]](../_modules/music21/scale/intervalNetwork.html#IntervalNetwork.realizePitchByDegree)
:   Realize the native nodes of this network based on
    a pitch assigned to a valid nodeId, where nodeId can
    be specified by integer (starting from 1) or key
    (a tuple of origin, destination keys).

    The nodeDegreeTargets specifies the degrees to be
    included within the specified range.

    Example: build a network of the Major scale:

    ```python
    >>> edgeList = ['M2', 'M2', 'm2', 'M2', 'M2', 'M2', 'm2']
    >>> net = scale.intervalNetwork.IntervalNetwork()
    >>> net.fillBiDirectedEdges(edgeList)
    ```

    Now for every “scale” where G is the 3rd degree, give me the
    tonic if that note is between C2 and C3.
    (There’s only one such note: E-2).

    ```python
    >>> net.realizePitchByDegree('G', 3, [1], 'c2', 'c3')
    [<music21.pitch.Pitch E-2>]
    ```

    But between c2 and f3 there are two, E-2 and E-3 (it doesn’t matter that the G
    which is scale degree 3 for E-3 is above F3):

    ```python
    >>> net.realizePitchByDegree('G', 3, [1], 'c2', 'f3')
    [<music21.pitch.Pitch E-2>, <music21.pitch.Pitch E-3>]
    ```

    Give us nodes 1, 2, and 5 for scales where G is node 5 (e.g., C major’s dominant)
    where any pitch is between C2 and F4

    ```python
    >>> pitchList = net.realizePitchByDegree('G', 5, [1, 2, 5], 'c2', 'f4')
    >>> print(' '.join([str(p) for p in pitchList]))
    C2 D2 G2 C3 D3 G3 C4 D4
    ```

    There are no networks based on the major scale’s edge-list where
    with node 1 (i.e. “tonic”) between C2 and F2 where
    G is scale degree 7

    ```python
    >>> net.realizePitchByDegree('G', 7, [1], 'c2', 'f2')
    []
    ```

IntervalNetwork.realizeTermini(*pitchReference: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")*, *nodeId: [Node](#music21.scale.intervalNetwork.Node "music21.scale.intervalNetwork.Node") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Terminus](#music21.scale.intervalNetwork.Terminus "music21.scale.intervalNetwork.Terminus") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *alteredDegrees=None*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch"), [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")][[source]](../_modules/music21/scale/intervalNetwork.html#IntervalNetwork.realizeTermini)
:   Realize the pitches of the ‘natural’ terminus of a network. This (presently)
    must be done by ascending, and assumes only one valid terminus for both extremes.

    This suggests that in practice termini should not be affected by directionality.

    ```python
    >>> edgeList = ['M2', 'M2', 'm2', 'M2', 'M2', 'M2', 'm2']
    >>> net = scale.intervalNetwork.IntervalNetwork()
    >>> net.fillBiDirectedEdges(edgeList)
    >>> net.realizeTermini(pitch.Pitch('G3'))
    (<music21.pitch.Pitch G3>, <music21.pitch.Pitch G4>)
    >>> net.realizeTermini(pitch.Pitch('a6'))
    (<music21.pitch.Pitch A6>, <music21.pitch.Pitch A7>)
    ```

IntervalNetwork.transposePitchAndApplySimplification(*intervalObj: [Interval](moduleInterval.html#music21.interval.Interval "music21.interval.Interval")*, *pitchObj: [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")*) → [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")[[source]](../_modules/music21/scale/intervalNetwork.html#IntervalNetwork.transposePitchAndApplySimplification)
:   transposes the pitch according to the given interval object and
    uses the simplification of the pitchSimplification property
    to simplify it afterwards.

    ```python
    >>> b = scale.intervalNetwork.IntervalNetwork()
    >>> b.pitchSimplification  # default
    'maxAccidental'
    >>> i = interval.Interval('m2')
    >>> p = pitch.Pitch('C4')
    >>> allPitches = []
    >>> for j in range(15):
    ...    p = b.transposePitchAndApplySimplification(i, p)
    ...    allPitches.append(p.nameWithOctave)
    >>> allPitches
    ['D-4', 'D4', 'E-4', 'F-4', 'F4', 'G-4', 'G4', 'A-4', 'A4',
     'B-4', 'C-5', 'C5', 'D-5', 'D5', 'E-5']
    ```

    ```python
    >>> b.pitchSimplification = 'mostCommon'
    >>> p = pitch.Pitch('C4')
    >>> allPitches = []
    >>> for j in range(15):
    ...    p = b.transposePitchAndApplySimplification(i, p)
    ...    allPitches.append(p.nameWithOctave)
    >>> allPitches
    ['C#4', 'D4', 'E-4', 'E4', 'F4', 'F#4', 'G4', 'A-4', 'A4', 'B-4',
     'B4', 'C5', 'C#5', 'D5', 'E-5']
    ```

    PitchSimplification can also be specified in the creation of the IntervalNetwork object

    ```python
    >>> b = scale.intervalNetwork.IntervalNetwork(pitchSimplification=None)
    >>> p = pitch.Pitch('C4')
    >>> allPitches = []
    >>> for j in range(5):
    ...    p = b.transposePitchAndApplySimplification(i, p)
    ...    allPitches.append(p.nameWithOctave)
    >>> allPitches
    ['D-4', 'E--4', 'F--4', 'G---4', 'A----4']
    ```

    Note that beyond quadruple flats or sharps, pitchSimplification is automatic:

    ```python
    >>> p
    <music21.pitch.Pitch A----4>
    >>> b.transposePitchAndApplySimplification(i, p)
    <music21.pitch.Pitch F#4>
    ```

IntervalNetwork.weightedSelection(*edges*, *nodes*)[[source]](../_modules/music21/scale/intervalNetwork.html#IntervalNetwork.weightedSelection)
:   Perform weighted random selection on a parallel list of
    edges and corresponding nodes.

    ```python
    >>> n1 = scale.intervalNetwork.Node(id=1, degree=1, weight=1000000)
    >>> n2 = scale.intervalNetwork.Node(id=2, degree=1, weight=1)
    >>> e1 = scale.intervalNetwork.Edge(interval.Interval('m3'), id=1)
    >>> e2 = scale.intervalNetwork.Edge(interval.Interval('m3'), id=2)
    >>> net = scale.intervalNetwork.IntervalNetwork()
    >>> e, n = net.weightedSelection([e1, e2], [n1, n2])
    ```

    Note: this may fail as there is a slight chance to get 2

    ```python
    >>> e.id
    1
    >>> n.id
    1
    ```

## Node

class music21.scale.intervalNetwork.Node(*id: [Terminus](#music21.scale.intervalNetwork.Terminus "music21.scale.intervalNetwork.Terminus") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *degree: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *weight: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") = 1.0*)[[source]](../_modules/music21/scale/intervalNetwork.html#Node)
:   Abstraction of an unrealized Pitch Node.

    The Node id is used to store connections in Edges and has no real meaning.

    Terminal Nodes have special ids: Terminus.LOW, Terminus.HIGH

    The Node degree is translated to scale degrees in various applications,
    and is used to request a pitch from the network.

    The weight attribute is used to probabilistically select between
    multiple nodes when multiple nodes satisfy either a branching option in a pathway
    or a request for a degree.

    TODO: replace w/ NamedTuple; eliminate id, and have a terminus: low, high, None

[`Node`](#music21.scale.intervalNetwork.Node "music21.scale.intervalNetwork.Node") bases

* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")
* [`SlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.SlottedObjectMixin "music21.common.objects.SlottedObjectMixin")

[`Node`](#music21.scale.intervalNetwork.Node "music21.scale.intervalNetwork.Node") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`Node`](#music21.scale.intervalNetwork.Node "music21.scale.intervalNetwork.Node") methods

Node.\_\_eq\_\_(*other*)[[source]](../_modules/music21/scale/intervalNetwork.html#Node.__eq__)
:   Nodes are equal if everything in the object.\_\_slots\_\_ is equal.

    ```python
    >>> n1 = scale.intervalNetwork.Node(id=3, degree=1)
    >>> n2 = scale.intervalNetwork.Node(id=3, degree=1)
    >>> n3 = scale.intervalNetwork.Node(id=2, degree=1)
    >>> n1 == n2
    True
    >>> n1 == n3
    False
    >>> n2.weight = 2.0
    >>> n1 == n2
    False
    ```

    ```python
    >>> n4 = scale.intervalNetwork.Node(id=scale.Terminus.LOW, degree=1)
    >>> n5 = scale.intervalNetwork.Node(id=scale.Terminus.LOW, degree=1)
    >>> n4 == n5
    True
    ```

## Edge

class music21.scale.intervalNetwork.Edge(*intervalData: [Interval](moduleInterval.html#music21.interval.Interval "music21.interval.Interval") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *id=None*, *direction=Direction.BI*)[[source]](../_modules/music21/scale/intervalNetwork.html#Edge)
:   Abstraction of an Interval as an Edge.

    Edges store an Interval object as well as a pathway direction specification.
    The pathway is the route through the network from terminus to terminus,
    and can either by ascending or descending.

    For directed Edges, the direction of the Interval may be used to
    suggest non-pitch ascending movements (even if the pathway direction is ascending).

    Weight values, as well as other attributes, can be stored.

    ```python
    >>> i = interval.Interval('M3')
    >>> e = scale.intervalNetwork.Edge(i)
    >>> e.interval is i
    True
    >>> e.direction
    Direction.BI
    ```

    Return the stored Interval object

    ```python
    >>> i = interval.Interval('M3')
    >>> e1 = scale.intervalNetwork.Edge(i, id=0)
    >>> n1 = scale.intervalNetwork.Node(id=0, degree=0)
    >>> n2 = scale.intervalNetwork.Node(id=1, degree=1)
    >>> e1.addDirectedConnection(n1, n2, scale.Direction.ASCENDING)
    >>> e1.interval
    <music21.interval.Interval M3>
    ```

    Return the direction of the Edge.

    ```python
    >>> i = interval.Interval('M3')
    >>> e1 = scale.intervalNetwork.Edge(i, id=0)
    >>> n1 = scale.intervalNetwork.Node(id=0, degree=0)
    >>> n2 = scale.intervalNetwork.Node(id=1, degree=1)
    >>> e1.addDirectedConnection(n1, n2, scale.Direction.ASCENDING)
    >>> e1.direction
    Direction.ASCENDING
    ```

[`Edge`](#music21.scale.intervalNetwork.Edge "music21.scale.intervalNetwork.Edge") bases

* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`Edge`](#music21.scale.intervalNetwork.Edge "music21.scale.intervalNetwork.Edge") read-only properties

Edge.connections

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`Edge`](#music21.scale.intervalNetwork.Edge "music21.scale.intervalNetwork.Edge") methods

Edge.\_\_eq\_\_(*other*)[[source]](../_modules/music21/scale/intervalNetwork.html#Edge.__eq__)
:   ```python
    >>> i1 = interval.Interval('M3')
    >>> i2 = interval.Interval('M3')
    >>> i3 = interval.Interval('m3')
    >>> e1 = scale.intervalNetwork.Edge(i1)
    >>> e2 = scale.intervalNetwork.Edge(i2)
    >>> e3 = scale.intervalNetwork.Edge(i3)
    >>> e1 == e2
    True
    >>> e1 == e3
    False
    ```

Edge.addBiDirectedConnections(*node1*, *node2*)[[source]](../_modules/music21/scale/intervalNetwork.html#Edge.addBiDirectedConnections)
:   Provide two Edge objects that pass through
    this Node, in the direction from the first to the second.

    ```python
    >>> i = interval.Interval('M3')
    >>> e1 = scale.intervalNetwork.Edge(i, id=0)
    >>> n1 = scale.intervalNetwork.Node(id=scale.Terminus.LOW, degree=0)
    >>> n2 = scale.intervalNetwork.Node(id=1, degree=1)
    ```

    ```python
    >>> e1.addBiDirectedConnections(n1, n2)
    >>> e1.connections
    [(Terminus.LOW, 1), (1, Terminus.LOW)]
    >>> e1
    <music21.scale.intervalNetwork.Edge Direction.BI M3
        [(Terminus.LOW, 1), (1, Terminus.LOW)]>
    ```

Edge.addDirectedConnection(*node1: [Node](#music21.scale.intervalNetwork.Node "music21.scale.intervalNetwork.Node") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Terminus](#music21.scale.intervalNetwork.Terminus "music21.scale.intervalNetwork.Terminus")*, *node2: [Node](#music21.scale.intervalNetwork.Node "music21.scale.intervalNetwork.Node") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Terminus](#music21.scale.intervalNetwork.Terminus "music21.scale.intervalNetwork.Terminus")*, *direction=None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/scale/intervalNetwork.html#Edge.addDirectedConnection)
:   Provide two Node objects that are connected by this Edge,
    in the direction from the first to the second.

    When calling directly, a direction, either
    ascending or descending, should be set here;
    this will override whatever the interval is.
    If None, this will not be set.

    ```python
    >>> i = interval.Interval('M3')
    >>> e1 = scale.intervalNetwork.Edge(i, id=0)
    ```

    ```python
    >>> n1 = scale.intervalNetwork.Node(id=0, degree=0)
    >>> n2 = scale.intervalNetwork.Node(id=1, degree=1)
    ```

    ```python
    >>> e1.addDirectedConnection(n1, n2, scale.Direction.ASCENDING)
    >>> e1.connections
    [(0, 1)]
    >>> e1
    <music21.scale.intervalNetwork.Edge Direction.ASCENDING M3 [(0, 1)]>
    ```

Edge.getConnections(*direction: [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [Direction](#music21.scale.intervalNetwork.Direction "music21.scale.intervalNetwork.Direction") = None*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Terminus](#music21.scale.intervalNetwork.Terminus "music21.scale.intervalNetwork.Terminus"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Terminus](#music21.scale.intervalNetwork.Terminus "music21.scale.intervalNetwork.Terminus")]][[source]](../_modules/music21/scale/intervalNetwork.html#Edge.getConnections)
:   Callable as a property (.connections) or as a method
    (.getConnections(direction)):

    Return a list of connections between Nodes, represented as pairs
    of Node ids. If a direction is specified, and if the Edge is
    directional, only the desired directed values will be returned.

    ```python
    >>> i = interval.Interval('M3')
    >>> e1 = scale.intervalNetwork.Edge(i, id=0)
    >>> n1 = scale.intervalNetwork.Node(id=scale.Terminus.LOW, degree=1)
    >>> n2 = scale.intervalNetwork.Node(id=1, degree=2)
    ```

    ```python
    >>> e1.addBiDirectedConnections(n1, n2)
    >>> e1.connections
    [(Terminus.LOW, 1), (1, Terminus.LOW)]
    >>> e1.getConnections(scale.Direction.ASCENDING)
    [(Terminus.LOW, 1)]
    >>> e1.getConnections(scale.Direction.DESCENDING)
    [(1, Terminus.LOW)]
    ```

## BoundIntervalNetwork

class music21.scale.intervalNetwork.BoundIntervalNetwork(*edgeList: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[Interval](moduleInterval.html#music21.interval.Interval "music21.interval.Interval") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] = ()*, *octaveDuplicating=False*, *deterministic=True*, *pitchSimplification='maxAccidental'*)[[source]](../_modules/music21/scale/intervalNetwork.html#BoundIntervalNetwork)
:   This class is kept only because of the ICMC Paper. Just use IntervalNetwork instead.

[`BoundIntervalNetwork`](#music21.scale.intervalNetwork.BoundIntervalNetwork "music21.scale.intervalNetwork.BoundIntervalNetwork") bases

* [`IntervalNetwork`](#music21.scale.intervalNetwork.IntervalNetwork "music21.scale.intervalNetwork.IntervalNetwork")

[`BoundIntervalNetwork`](#music21.scale.intervalNetwork.BoundIntervalNetwork "music21.scale.intervalNetwork.BoundIntervalNetwork") read-only properties

Read-only properties inherited from [`IntervalNetwork`](#music21.scale.intervalNetwork.IntervalNetwork "music21.scale.intervalNetwork.IntervalNetwork"):

|  |  |  |
| --- | --- | --- |
| * [`degreeMax`](#music21.scale.intervalNetwork.IntervalNetwork.degreeMax "music21.scale.intervalNetwork.IntervalNetwork.degreeMax") * [`degreeMaxUnique`](#music21.scale.intervalNetwork.IntervalNetwork.degreeMaxUnique "music21.scale.intervalNetwork.IntervalNetwork.degreeMaxUnique") | * [`degreeMin`](#music21.scale.intervalNetwork.IntervalNetwork.degreeMin "music21.scale.intervalNetwork.IntervalNetwork.degreeMin") * [`terminusHighNodes`](#music21.scale.intervalNetwork.IntervalNetwork.terminusHighNodes "music21.scale.intervalNetwork.IntervalNetwork.terminusHighNodes") | * [`terminusLowNodes`](#music21.scale.intervalNetwork.IntervalNetwork.terminusLowNodes "music21.scale.intervalNetwork.IntervalNetwork.terminusLowNodes") |

[`BoundIntervalNetwork`](#music21.scale.intervalNetwork.BoundIntervalNetwork "music21.scale.intervalNetwork.BoundIntervalNetwork") methods

Methods inherited from [`IntervalNetwork`](#music21.scale.intervalNetwork.IntervalNetwork "music21.scale.intervalNetwork.IntervalNetwork"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](#music21.scale.intervalNetwork.IntervalNetwork.__eq__ "music21.scale.intervalNetwork.IntervalNetwork.__eq__") * [`clear()`](#music21.scale.intervalNetwork.IntervalNetwork.clear "music21.scale.intervalNetwork.IntervalNetwork.clear") * [`degreeModulus()`](#music21.scale.intervalNetwork.IntervalNetwork.degreeModulus "music21.scale.intervalNetwork.IntervalNetwork.degreeModulus") * [`fillArbitrary()`](#music21.scale.intervalNetwork.IntervalNetwork.fillArbitrary "music21.scale.intervalNetwork.IntervalNetwork.fillArbitrary") * [`fillBiDirectedEdges()`](#music21.scale.intervalNetwork.IntervalNetwork.fillBiDirectedEdges "music21.scale.intervalNetwork.IntervalNetwork.fillBiDirectedEdges") * [`fillDirectedEdges()`](#music21.scale.intervalNetwork.IntervalNetwork.fillDirectedEdges "music21.scale.intervalNetwork.IntervalNetwork.fillDirectedEdges") * [`fillMelodicMinor()`](#music21.scale.intervalNetwork.IntervalNetwork.fillMelodicMinor "music21.scale.intervalNetwork.IntervalNetwork.fillMelodicMinor") * [`filterPitchList()`](#music21.scale.intervalNetwork.IntervalNetwork.filterPitchList "music21.scale.intervalNetwork.IntervalNetwork.filterPitchList") * [`find()`](#music21.scale.intervalNetwork.IntervalNetwork.find "music21.scale.intervalNetwork.IntervalNetwork.find") * [`findMissing()`](#music21.scale.intervalNetwork.IntervalNetwork.findMissing "music21.scale.intervalNetwork.IntervalNetwork.findMissing") * [`getNeighborNodeIds()`](#music21.scale.intervalNetwork.IntervalNetwork.getNeighborNodeIds "music21.scale.intervalNetwork.IntervalNetwork.getNeighborNodeIds") | * [`getNext()`](#music21.scale.intervalNetwork.IntervalNetwork.getNext "music21.scale.intervalNetwork.IntervalNetwork.getNext") * [`getNodeDegreeDictionary()`](#music21.scale.intervalNetwork.IntervalNetwork.getNodeDegreeDictionary "music21.scale.intervalNetwork.IntervalNetwork.getNodeDegreeDictionary") * [`getPitchFromNodeDegree()`](#music21.scale.intervalNetwork.IntervalNetwork.getPitchFromNodeDegree "music21.scale.intervalNetwork.IntervalNetwork.getPitchFromNodeDegree") * [`getRelativeNodeDegree()`](#music21.scale.intervalNetwork.IntervalNetwork.getRelativeNodeDegree "music21.scale.intervalNetwork.IntervalNetwork.getRelativeNodeDegree") * [`getRelativeNodeId()`](#music21.scale.intervalNetwork.IntervalNetwork.getRelativeNodeId "music21.scale.intervalNetwork.IntervalNetwork.getRelativeNodeId") * [`getUnalteredPitch()`](#music21.scale.intervalNetwork.IntervalNetwork.getUnalteredPitch "music21.scale.intervalNetwork.IntervalNetwork.getUnalteredPitch") * [`match()`](#music21.scale.intervalNetwork.IntervalNetwork.match "music21.scale.intervalNetwork.IntervalNetwork.match") * [`nextPitch()`](#music21.scale.intervalNetwork.IntervalNetwork.nextPitch "music21.scale.intervalNetwork.IntervalNetwork.nextPitch") * [`nodeIdToDegree()`](#music21.scale.intervalNetwork.IntervalNetwork.nodeIdToDegree "music21.scale.intervalNetwork.IntervalNetwork.nodeIdToDegree") * [`nodeIdToEdgeDirections()`](#music21.scale.intervalNetwork.IntervalNetwork.nodeIdToEdgeDirections "music21.scale.intervalNetwork.IntervalNetwork.nodeIdToEdgeDirections") * [`nodeNameToNodes()`](#music21.scale.intervalNetwork.IntervalNetwork.nodeNameToNodes "music21.scale.intervalNetwork.IntervalNetwork.nodeNameToNodes") | * [`processAlteredNodes()`](#music21.scale.intervalNetwork.IntervalNetwork.processAlteredNodes "music21.scale.intervalNetwork.IntervalNetwork.processAlteredNodes") * [`realize()`](#music21.scale.intervalNetwork.IntervalNetwork.realize "music21.scale.intervalNetwork.IntervalNetwork.realize") * [`realizeAscending()`](#music21.scale.intervalNetwork.IntervalNetwork.realizeAscending "music21.scale.intervalNetwork.IntervalNetwork.realizeAscending") * [`realizeDescending()`](#music21.scale.intervalNetwork.IntervalNetwork.realizeDescending "music21.scale.intervalNetwork.IntervalNetwork.realizeDescending") * [`realizeIntervals()`](#music21.scale.intervalNetwork.IntervalNetwork.realizeIntervals "music21.scale.intervalNetwork.IntervalNetwork.realizeIntervals") * [`realizeMinMax()`](#music21.scale.intervalNetwork.IntervalNetwork.realizeMinMax "music21.scale.intervalNetwork.IntervalNetwork.realizeMinMax") * [`realizePitch()`](#music21.scale.intervalNetwork.IntervalNetwork.realizePitch "music21.scale.intervalNetwork.IntervalNetwork.realizePitch") * [`realizePitchByDegree()`](#music21.scale.intervalNetwork.IntervalNetwork.realizePitchByDegree "music21.scale.intervalNetwork.IntervalNetwork.realizePitchByDegree") * [`realizeTermini()`](#music21.scale.intervalNetwork.IntervalNetwork.realizeTermini "music21.scale.intervalNetwork.IntervalNetwork.realizeTermini") * [`transposePitchAndApplySimplification()`](#music21.scale.intervalNetwork.IntervalNetwork.transposePitchAndApplySimplification "music21.scale.intervalNetwork.IntervalNetwork.transposePitchAndApplySimplification") * [`weightedSelection()`](#music21.scale.intervalNetwork.IntervalNetwork.weightedSelection "music21.scale.intervalNetwork.IntervalNetwork.weightedSelection") |

## Direction

class music21.scale.intervalNetwork.Direction(*\*values*)[[source]](../_modules/music21/scale/intervalNetwork.html#Direction)
:   An enumerated Direction for a scale, either Direction.ASCENDING,
    Direction.DESCENDING, or Direction.BI (bidirectional)

## Terminus

class music21.scale.intervalNetwork.Terminus(*\*values*)[[source]](../_modules/music21/scale/intervalNetwork.html#Terminus)
:   One of the two Termini of a scale, either Terminus.LOW or
    Terminus.HIGH
