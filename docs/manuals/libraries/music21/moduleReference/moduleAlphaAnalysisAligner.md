Source: https://music21.org/music21docs/moduleReference/moduleAlphaAnalysisAligner.html

# music21.alpha.analysis.aligner

## ChangeOps

class music21.alpha.analysis.aligner.ChangeOps(*\*values*)[[source]](../_modules/music21/alpha/analysis/aligner.html#ChangeOps)
:   ```python
    >>> ins = alpha.analysis.aligner.ChangeOps.Insertion
    >>> ins.color
    'green'
    ```

    ```python
    >>> deletion = alpha.analysis.aligner.ChangeOps.Deletion
    >>> deletion.color
    'red'
    ```

    ```python
    >>> subs = alpha.analysis.aligner.ChangeOps.Substitution
    >>> subs.color
    'purple'
    ```

    ```python
    >>> noChange = alpha.analysis.aligner.ChangeOps.NoChange
    >>> noChange.color is None
    True
    ```

## StreamAligner

class music21.alpha.analysis.aligner.StreamAligner(*targetStream=None*, *sourceStream=None*, *hasher\_func=None*, *preHashed=False*)[[source]](../_modules/music21/alpha/analysis/aligner.html#StreamAligner)
:   Stream Aligner is a dumb object that takes in two streams and forces them to align
    without any thought to any external variables

    These terms are associated with the Target stream are:
    - n, the number of rows in the distance matrix, the left-most column of the matrix
    - i, the index into rows in the distance matrix
    - the first element of tuple

    These terms are associated with the Source stream are:
    - m, the number of columns in the distance matrix, the top-most row of the matrix
    - j, the index into columns in the distance matrix
    - the second element of tuple

[`StreamAligner`](#music21.alpha.analysis.aligner.StreamAligner "music21.alpha.analysis.aligner.StreamAligner") methods

StreamAligner.align()[[source]](../_modules/music21/alpha/analysis/aligner.html#StreamAligner.align)

StreamAligner.calculateChangesList()[[source]](../_modules/music21/alpha/analysis/aligner.html#StreamAligner.calculateChangesList)
:   Traverses through self.distanceMatrix from the bottom right corner to top left looking at
    bestOp at every move to determine which change was most likely at any point. Compiles
    the list of changes in self.changes. Also calculates some metrics like self.similarityScore
    and self.changesCount.

    ```python
    >>> note1 = note.Note('C#4')
    >>> note2 = note.Note('C4')
    ```

    test 1: one insertion, one no change. Target stream has one more note than
    source stream, so source stream needs an insertion to match target stream.
    should be 0.5 similarity between the two

    ```python
    >>> targetA = stream.Stream()
    >>> sourceA = stream.Stream()
    >>> targetA.append([note1, note2])
    >>> sourceA.append(note1)
    >>> saA = alpha.analysis.aligner.StreamAligner(targetA, sourceA)
    >>> saA.makeHashedStreams()
    >>> saA.setupDistanceMatrix()
    >>> saA.populateDistanceMatrix()
    >>> saA.calculateChangesList()
    >>> saA.changesCount[alpha.analysis.aligner.ChangeOps.Insertion]
    1
    >>> saA.changesCount[alpha.analysis.aligner.ChangeOps.NoChange]
    1
    >>> saA.similarityScore
    0.5
    ```

    test 2: one deletion, one no change. Target stream has one fewer note than
    source stream, so source stream needs a deletion to match target stream.
    should be 0.5 similarity between the two

    ```python
    >>> targetB = stream.Stream()
    >>> sourceB = stream.Stream()
    >>> targetB.append(note1)
    >>> sourceB.append([note1, note2])
    >>> saB = alpha.analysis.aligner.StreamAligner(targetB, sourceB)
    >>> saB.makeHashedStreams()
    >>> saB.setupDistanceMatrix()
    >>> saB.populateDistanceMatrix()
    >>> saB.calculateChangesList()
    >>> saB.changesCount[alpha.analysis.aligner.ChangeOps.Deletion]
    1
    >>> saB.changesCount[alpha.analysis.aligner.ChangeOps.NoChange]
    1
    >>> saB.similarityScore
    0.5
    ```

    test 3: no changes

    ```python
    >>> targetC = stream.Stream()
    >>> sourceC = stream.Stream()
    >>> targetC.append([note1, note2])
    >>> sourceC.append([note1, note2])
    >>> saC = alpha.analysis.aligner.StreamAligner(targetC, sourceC)
    >>> saC.makeHashedStreams()
    >>> saC.setupDistanceMatrix()
    >>> saC.populateDistanceMatrix()
    >>> saC.calculateChangesList()
    >>> saC.changesCount[alpha.analysis.aligner.ChangeOps.NoChange]
    2
    >>> saC.similarityScore
    1.0
    ```

    test 4: 1 no change, 1 substitution

    ```python
    >>> targetD = stream.Stream()
    >>> sourceD = stream.Stream()
    >>> note3 = note.Note('C4')
    >>> note3.quarterLength = 2  # same pitch and offset as note2
    >>> targetD.append([note1, note2])
    >>> sourceD.append([note1, note3])
    >>> saD = alpha.analysis.aligner.StreamAligner(targetD, sourceD)
    >>> saD.makeHashedStreams()
    >>> saD.setupDistanceMatrix()
    >>> saD.populateDistanceMatrix()
    >>> saD.calculateChangesList()
    >>> saD.changesCount[alpha.analysis.aligner.ChangeOps.Substitution]
    1
    >>> saD.changesCount[alpha.analysis.aligner.ChangeOps.NoChange]
    1
    >>> saD.similarityScore
    0.5
    ```

StreamAligner.calculateNumSimilarities(*targetTup*, *sourceTup*)[[source]](../_modules/music21/alpha/analysis/aligner.html#StreamAligner.calculateNumSimilarities)
:   Returns the number of attributes that two tuples have that are the same

    ```python
    >>> target = stream.Stream()
    >>> source = stream.Stream()
    ```

    ```python
    >>> note1 = note.Note('D1')
    >>> target.append([note1])
    >>> source.append([note1])
    >>> sa = alpha.analysis.aligner.StreamAligner(target, source)
    ```

    ```python
    >>> from collections import namedtuple
    >>> NoteHash = namedtuple('NoteHash', ['Pitch', 'Duration'])
    >>> nh1 = NoteHash(60, 4)
    >>> nhwr1 = alpha.analysis.hasher.NoteHashWithReference(nh1)
    >>> nhwr1.reference = note.Note('C4')
    >>> nhwr1
    NoteHashWithReference(Pitch=60, Duration=4)
    ```

    ```python
    >>> nh2 = NoteHash(60, 4)
    >>> nhwr2 = alpha.analysis.hasher.NoteHashWithReference(nh2)
    >>> nhwr2.reference = note.Note('C4')
    >>> nhwr2
    NoteHashWithReference(Pitch=60, Duration=4)
    ```

    ```python
    >>> sa.calculateNumSimilarities(nhwr1, nhwr2)
    2
    ```

    ```python
    >>> nh3 = NoteHash(61, 4)
    >>> nhwr3 = alpha.analysis.hasher.NoteHashWithReference(nh3)
    >>> nhwr3.reference = note.Note('C#4')
    >>> nhwr3
    NoteHashWithReference(Pitch=61, Duration=4)
    ```

    ```python
    >>> sa.calculateNumSimilarities(nhwr1, nhwr3)
    1
    ```

    ```python
    >>> nh4 = NoteHash(59, 1)
    >>> nhwr4 = alpha.analysis.hasher.NoteHashWithReference(nh4)
    >>> nhwr4.reference = note.Note('B3')
    >>> nhwr4
    NoteHashWithReference(Pitch=59, Duration=1)
    ```

    ```python
    >>> sa.calculateNumSimilarities(nhwr2, nhwr4)
    0
    ```

StreamAligner.deleteCost(*tup*)[[source]](../_modules/music21/alpha/analysis/aligner.html#StreamAligner.deleteCost)
:   Cost of deleting an extra hashed item.
    For now, it’s just the size of the keys of the NoteHashWithReference

    ```python
    >>> target = stream.Stream()
    >>> source = stream.Stream()
    ```

    ```python
    >>> note1 = note.Note('C4')
    >>> note2 = note.Note('D4')
    >>> note3 = note.Note('C4')
    >>> note4 = note.Note('E4')
    ```

    ```python
    >>> target.append([note1, note2, note3, note4])
    >>> source.append([note1, note2, note3])
    ```

    This is a StreamAligner with default hasher settings

    ```python
    >>> sa0 = alpha.analysis.aligner.StreamAligner(target, source)
    >>> sa0.align()
    >>> tup0 = sa0.hashedSourceStream[0]
    >>> sa0.deleteCost(tup0)
    2
    ```

    This is a StreamAligner with a modified hasher that doesn’t hash pitch at all

    ```python
    >>> sa1 = alpha.analysis.aligner.StreamAligner(target, source)
    >>> sa1.hasher.hashPitch = False
    >>> sa1.align()
    >>> tup1 = sa1.hashedSourceStream[0]
    >>> sa1.deleteCost(tup1)
    1
    ```

    This is a StreamAligner with a modified hasher that hashes 3 additional properties

    ```python
    >>> sa2 = alpha.analysis.aligner.StreamAligner(target, source)
    >>> sa2.hasher.hashOctave = True
    >>> sa2.hasher.hashIntervalFromLastNote = True
    >>> sa2.hasher.hashIsAccidental = True
    >>> sa2.align()
    >>> tup2 = sa2.hashedSourceStream[0]
    >>> sa2.deleteCost(tup2)
    5
    ```

StreamAligner.getDefaultHasher()[[source]](../_modules/music21/alpha/analysis/aligner.html#StreamAligner.getDefaultHasher)
:   returns a default hasher.Hasher object
    that does not hashOffset or include the reference.

    called by \_\_init\_\_ if no hasher is passed in.

    ```python
    >>> sa = alpha.analysis.aligner.StreamAligner()
    >>> h = sa.getDefaultHasher()
    >>> h
    <music21.alpha.analysis.hasher.Hasher object at 0x1068cf6a0>
    >>> h.hashOffset
    False
    >>> h.includeReference
    True
    ```

StreamAligner.getOpFromLocation(*i*, *j*)[[source]](../_modules/music21/alpha/analysis/aligner.html#StreamAligner.getOpFromLocation)
:   Insert, Delete, Substitution, No Change = range(4)

    return the direction that traceback moves
    0: vertical movement, insertion
    1: horizontal movement, deletion
    2: diagonal movement, substitution
    3: diagonal movement, no change

    raises a ValueError if i == 0 and j == 0.
    >>> target = stream.Stream()
    >>> source = stream.Stream()

    ```python
    >>> note1 = note.Note('C4')
    >>> note2 = note.Note('D4')
    >>> note3 = note.Note('C4')
    >>> note4 = note.Note('E4')
    ```

    ```python
    >>> target.append([note1, note2, note3, note4])
    >>> source.append([note1, note2, note3])
    ```

    ```python
    >>> sa = alpha.analysis.aligner.StreamAligner(target, source)
    >>> sa.makeHashedStreams()
    >>> sa.setupDistanceMatrix()
    >>> sa.populateDistanceMatrix()
    >>> sa.distanceMatrix
    array([[0, 2, 4, 6],
           [2, 0, 2, 4],
           [4, 2, 0, 2],
           [6, 4, 2, 0],
           [8, 6, 4, 2]])
    ```

    ```python
    >>> sa.getOpFromLocation(4, 3)
    <ChangeOps.Insertion: 0>
    ```

    ```python
    >>> sa.getOpFromLocation(2, 2)
    <ChangeOps.NoChange: 3>
    ```

    ```python
    >>> sa.getOpFromLocation(0, 2)
    <ChangeOps.Deletion: 1>
    ```

    ```python
    >>> sa.distanceMatrix[0][0] = 1
    >>> sa.distanceMatrix
    array([[1, 2, 4, 6],
           [2, 0, 2, 4],
           [4, 2, 0, 2],
           [6, 4, 2, 0],
           [8, 6, 4, 2]])
    ```

    ```python
    >>> sa.getOpFromLocation(1, 1)
    <ChangeOps.Substitution: 2>
    ```

    ```python
    >>> sa.getOpFromLocation(0, 0)
    Traceback (most recent call last):
    ValueError: No movement possible from the origin
    ```

StreamAligner.getPossibleMovesFromLocation(*i*, *j*)[[source]](../_modules/music21/alpha/analysis/aligner.html#StreamAligner.getPossibleMovesFromLocation)
:   i and j are current row and column indices in self.distanceMatrix
    returns all possible moves (0 up to 3)
    vertical, horizontal, diagonal costs of adjacent entries in self.distMatrix

    ```python
    >>> target = stream.Stream()
    >>> source = stream.Stream()
    ```

    ```python
    >>> note1 = note.Note('C4')
    >>> note2 = note.Note('D4')
    >>> note3 = note.Note('C4')
    >>> note4 = note.Note('E4')
    ```

    ```python
    >>> target.append([note1, note2, note3, note4])
    >>> source.append([note1, note2, note3])
    >>> sa = alpha.analysis.aligner.StreamAligner(target, source)
    >>> sa.makeHashedStreams()
    >>> sa.setupDistanceMatrix()
    >>> for i in range(4+1):
    ...     for j in range(3+1):
    ...         sa.distanceMatrix[i][j] = i * j
    ```

    ```python
    >>> sa.distanceMatrix
    array([[ 0,  0,  0,  0],
           [ 0,  1,  2,  3],
           [ 0,  2,  4,  6],
           [ 0,  3,  6,  9],
           [ 0,  4,  8, 12]])
    ```

    ```python
    >>> sa.getPossibleMovesFromLocation(0, 0)
    [None, None, None]
    ```

    ```python
    >>> sa.getPossibleMovesFromLocation(1, 1)
    [0, 0, 0]
    ```

    ```python
    >>> sa.getPossibleMovesFromLocation(4, 3)
    [9, 8, 6]
    ```

    ```python
    >>> sa.getPossibleMovesFromLocation(2, 2)
    [2, 2, 1]
    ```

    ```python
    >>> sa.getPossibleMovesFromLocation(0, 2)
    [None, 0, None]
    ```

    ```python
    >>> sa.getPossibleMovesFromLocation(3, 0)
    [0, None, None]
    ```

StreamAligner.insertCost(*tup*)[[source]](../_modules/music21/alpha/analysis/aligner.html#StreamAligner.insertCost)
:   Cost of inserting an extra hashed item.
    For now, it’s just the size of the keys of the NoteHashWithReference

    ```python
    >>> target = stream.Stream()
    >>> source = stream.Stream()
    ```

    ```python
    >>> note1 = note.Note('C4')
    >>> note2 = note.Note('D4')
    >>> note3 = note.Note('C4')
    >>> note4 = note.Note('E4')
    ```

    ```python
    >>> target.append([note1, note2, note3, note4])
    >>> source.append([note1, note2, note3])
    ```

    This is a StreamAligner with default hasher settings

    ```python
    >>> sa0 = alpha.analysis.aligner.StreamAligner(target, source)
    >>> sa0.align()
    >>> tup0 = sa0.hashedTargetStream[0]
    >>> sa0.insertCost(tup0)
    2
    ```

    This is a StreamAligner with a modified hasher that doesn’t hash pitch at all

    ```python
    >>> sa1 = alpha.analysis.aligner.StreamAligner(target, source)
    >>> sa1.hasher.hashPitch = False
    >>> sa1.align()
    >>> tup1 = sa1.hashedTargetStream[0]
    >>> sa1.insertCost(tup1)
    1
    ```

    This is a StreamAligner with a modified hasher that hashes 3 additional properties

    ```python
    >>> sa2 = alpha.analysis.aligner.StreamAligner(target, source)
    >>> sa2.hasher.hashOctave = True
    >>> sa2.hasher.hashIntervalFromLastNote = True
    >>> sa2.hasher.hashIsAccidental = True
    >>> sa2.align()
    >>> tup2 = sa2.hashedTargetStream[0]
    >>> sa2.insertCost(tup2)
    5
    ```

StreamAligner.makeHashedStreams()[[source]](../_modules/music21/alpha/analysis/aligner.html#StreamAligner.makeHashedStreams)
:   Hashes streams if not pre-hashed

    ```python
    >>> tStream = stream.Stream()
    >>> sStream = stream.Stream()
    ```

    ```python
    >>> note1 = note.Note('C4')
    >>> note2 = note.Note('D4')
    >>> note3 = note.Note('C4')
    >>> note4 = note.Note('E4')
    ```

    ```python
    >>> tStream.append([note1, note2])
    >>> sStream.append([note3, note4])
    >>> sa1 = alpha.analysis.aligner.StreamAligner(tStream, sStream)
    ```

    ```python
    >>> h = alpha.analysis.hasher.Hasher()
    >>> h.includeReference = True
    ```

    ```python
    >>> toBeHashedTarStream = stream.Stream()
    >>> toBeHashedSouStream = stream.Stream()
    ```

    ```python
    >>> note5 = note.Note('A4')
    >>> note6 = note.Note('B4')
    >>> note7 = note.Note('A4')
    >>> note8 = note.Note('G4')
    ```

    ```python
    >>> toBeHashedTarStream.append([note5, note6])
    >>> toBeHashedSouStream.append([note7, note8])
    >>> hashedTarStr = h.hashStream(toBeHashedTarStream)
    >>> hashedSouStr = h.hashStream(toBeHashedSouStream)
    >>> sa2 = alpha.analysis.aligner.StreamAligner(
    ...             hashedTarStr, hashedSouStr, preHashed=True)
    ```

    ```python
    >>> sa2.makeHashedStreams()
    >>> sa1.makeHashedStreams()
    ```

    ```python
    >>> sa1.hashedTargetStream
    [NoteHashWithReference(Pitch=60, Duration=1.0),
     NoteHashWithReference(Pitch=62, Duration=1.0)]
    >>> sa1.hashedSourceStream
    [NoteHashWithReference(Pitch=60, Duration=1.0),
     NoteHashWithReference(Pitch=64, Duration=1.0)]
    ```

    ```python
    >>> sa2.hashedTargetStream
    [NoteHashWithReference(Pitch=69, Duration=1.0, Offset=0.0),
     NoteHashWithReference(Pitch=71, Duration=1.0, Offset=1.0)]
    >>> sa2.hashedSourceStream
    [NoteHashWithReference(Pitch=69, Duration=1.0, Offset=0.0),
     NoteHashWithReference(Pitch=67, Duration=1.0, Offset=1.0)]
    ```

StreamAligner.populateDistanceMatrix()[[source]](../_modules/music21/alpha/analysis/aligner.html#StreamAligner.populateDistanceMatrix)
:   Sets up the distance matrix for back-tracing

    ```python
    >>> note1 = note.Note('C#4')
    >>> note2 = note.Note('C4')
    ```

    Test 1: similar streams

    ```python
    >>> targetA = stream.Stream()
    >>> sourceA = stream.Stream()
    >>> targetA.append([note1, note2])
    >>> sourceA.append([note1, note2])
    >>> saA = alpha.analysis.aligner.StreamAligner(targetA, sourceA)
    >>> saA.makeHashedStreams()
    >>> saA.setupDistanceMatrix()
    >>> saA.populateDistanceMatrix()
    >>> saA.distanceMatrix
    array([[0, 2, 4],
           [2, 0, 2],
           [4, 2, 0]])
    ```

    Second Test

    ```python
    >>> targetB = stream.Stream()
    >>> sourceB = stream.Stream()
    >>> targetB.append([note1, note2])
    >>> sourceB.append(note1)
    >>> saB = alpha.analysis.aligner.StreamAligner(targetB, sourceB)
    >>> saB.makeHashedStreams()
    >>> saB.setupDistanceMatrix()
    >>> saB.populateDistanceMatrix()
    >>> saB.distanceMatrix
    array([[0, 2],
           [2, 0],
           [4, 2]])
    ```

    Third Test

    ```python
    >>> note3 = note.Note('D5')
    >>> note3.quarterLength = 3
    >>> note4 = note.Note('E3')
    >>> targetC = stream.Stream()
    >>> sourceC = stream.Stream()
    >>> targetC.append([note1, note2, note4])
    >>> sourceC.append([note3, note1, note4])
    >>> saC = alpha.analysis.aligner.StreamAligner(targetC, sourceC)
    >>> saC.makeHashedStreams()
    >>> saC.setupDistanceMatrix()
    >>> saC.populateDistanceMatrix()
    >>> saC.distanceMatrix
    array([[0, 2, 4, 6],
       [2, 2, 2, 4],
       [4, 4, 3, 3],
       [6, 6, 5, 3]])
    ```

StreamAligner.setupDistanceMatrix()[[source]](../_modules/music21/alpha/analysis/aligner.html#StreamAligner.setupDistanceMatrix)
:   Creates a distance matrix of the right size after hashing

    ```python
    >>> note1 = note.Note('C4')
    >>> note2 = note.Note('D4')
    >>> note3 = note.Note('C4')
    >>> note4 = note.Note('E4')
    ```

    Test for streams of length 3 and 4

    ```python
    >>> target0 = converter.parse('tinyNotation: C4 D C E')
    >>> source0 = converter.parse('tinyNotation: C4 D C')
    ```

    ```python
    >>> sa0 = alpha.analysis.aligner.StreamAligner(target0, source0)
    >>> sa0.setupDistanceMatrix()
    >>> sa0.distanceMatrix.size
    20
    >>> sa0.distanceMatrix.shape
    (5, 4)
    ```

    Test for empty target stream

    ```python
    >>> target1 = stream.Stream()
    >>> source1 = stream.Stream()
    >>> source1.append(note1)
    >>> sa1 = alpha.analysis.aligner.StreamAligner(target1, source1)
    >>> sa1.makeHashedStreams()
    >>> sa1.setupDistanceMatrix()
    Traceback (most recent call last):
    music21.alpha.analysis.aligner.AlignerException:
    Cannot perform alignment with empty target stream.
    ```

    Test for empty source stream

    ```python
    >>> target2 = stream.Stream()
    >>> source2 = stream.Stream()
    >>> target2.append(note3)
    >>> sa2 = alpha.analysis.aligner.StreamAligner(target2, source2)
    >>> sa2.makeHashedStreams()
    >>> sa2.setupDistanceMatrix()
    Traceback (most recent call last):
    music21.alpha.analysis.aligner.AlignerException:
        Cannot perform alignment with empty source stream.
    ```

StreamAligner.showChanges(*show=False*)[[source]](../_modules/music21/alpha/analysis/aligner.html#StreamAligner.showChanges)
:   Visual and debugging feature to display which notes are changed.
    Will open in MuseScore, unless show is set to False

StreamAligner.substitutionCost(*targetTup*, *sourceTup*)[[source]](../_modules/music21/alpha/analysis/aligner.html#StreamAligner.substitutionCost)
:   Finds the cost of substituting the targetTup with the sourceTup.
    For now, it’s just an interpolation of how many things they have in common

    Example: equality testing, both streams made from same note
    targetA will not have the same reference as sourceA
    but their hashes will be equal, which makes for their hashed objects to be
    able to be equal.

    ```python
    >>> note1 = note.Note('C4')
    >>> targetA = stream.Stream()
    >>> sourceA = stream.Stream()
    >>> targetA.append(note1)
    >>> sourceA.append(note1)
    >>> targetA == sourceA
    False
    ```

    ```python
    >>> saA = alpha.analysis.aligner.StreamAligner(targetA, sourceA)
    >>> saA.align()
    >>> hashedItem1A = saA.hashedTargetStream[0]
    >>> hashedItem2A = saA.hashedSourceStream[0]
    >>> print(hashedItem1A)
    NoteHashWithReference(Pitch=60, Duration=1.0)
    ```

    ```python
    >>> print(hashedItem2A)
    NoteHashWithReference(Pitch=60, Duration=1.0)
    ```

    ```python
    >>> saA.tupleEqualityWithoutReference(hashedItem1A, hashedItem2A)
    True
    >>> saA.substitutionCost(hashedItem1A, hashedItem2A)
    0
    ```

    ```python
    >>> note2 = note.Note('D4')
    >>> targetB = stream.Stream()
    >>> sourceB = stream.Stream()
    >>> targetB.append(note1)
    >>> sourceB.append(note2)
    >>> saB = alpha.analysis.aligner.StreamAligner(targetB, sourceB)
    >>> saB.align()
    >>> hashedItem1B = saB.hashedTargetStream[0]
    >>> hashedItem2B = saB.hashedSourceStream[0]
    ```

    hashed items only differ in 1 spot

    ```python
    >>> print(hashedItem1B)
    NoteHashWithReference(Pitch=60, Duration=1.0)
    ```

    ```python
    >>> print(hashedItem2B)
    NoteHashWithReference(Pitch=62, Duration=1.0)
    ```

    ```python
    >>> saB.substitutionCost(hashedItem1B, hashedItem2B)
    1
    ```

    ```python
    >>> note3 = note.Note('E4')
    >>> note4 = note.Note('E#4')
    >>> note4.duration = duration.Duration('half')
    >>> targetC = stream.Stream()
    >>> sourceC = stream.Stream()
    >>> targetC.append(note3)
    >>> sourceC.append(note4)
    >>> saC = alpha.analysis.aligner.StreamAligner(targetC, sourceC)
    >>> saC.align()
    >>> hashedItem1C = saC.hashedTargetStream[0]
    >>> hashedItem2C = saC.hashedSourceStream[0]
    ```

    hashed items should differ in 2 spots

    ```python
    >>> print(hashedItem1C)
    NoteHashWithReference(Pitch=64, Duration=1.0)
    ```

    ```python
    >>> print(hashedItem2C)
    NoteHashWithReference(Pitch=65, Duration=2.0)
    ```

    ```python
    >>> saC.substitutionCost(hashedItem1C, hashedItem2C)
    2
    ```

StreamAligner.tupleEqualityWithoutReference(*tup1*, *tup2*)[[source]](../_modules/music21/alpha/analysis/aligner.html#StreamAligner.tupleEqualityWithoutReference)
:   Returns whether two hashed items have the same attributes,
    even though their references are different?

    ```python
    >>> target = stream.Stream()
    >>> source = stream.Stream()
    ```

    ```python
    >>> note1 = note.Note('D1')
    >>> target.append([note1])
    >>> source.append([note1])
    >>> sa = alpha.analysis.aligner.StreamAligner(target, source)
    ```

    ```python
    >>> from collections import namedtuple
    >>> NoteHash = namedtuple('NoteHash', ['Pitch', 'Duration'])
    >>> nh1 = NoteHash(60, 4)
    >>> nhwr1 = alpha.analysis.hasher.NoteHashWithReference(nh1)
    >>> nhwr1.reference = note.Note('C4')
    >>> nhwr1
    NoteHashWithReference(Pitch=60, Duration=4)
    ```

    ```python
    >>> nh2 = NoteHash(60, 4)
    >>> nhwr2 = alpha.analysis.hasher.NoteHashWithReference(nh2)
    >>> nhwr2.reference = note.Note('B#3')
    >>> nhwr2
    NoteHashWithReference(Pitch=60, Duration=4)
    ```

    ```python
    >>> sa.tupleEqualityWithoutReference(nhwr1, nhwr2)
    True
    ```

    This is a very difference has

    ```python
    >>> nh3 = NoteHash(61, 4)
    >>> nhwr3 = alpha.analysis.hasher.NoteHashWithReference(nh3)
    >>> nhwr3.reference = note.Note('C#4')
    >>> nhwr3
    NoteHashWithReference(Pitch=61, Duration=4)
    ```

    ```python
    >>> sa.tupleEqualityWithoutReference(nhwr1, nhwr3)
    False
    ```
