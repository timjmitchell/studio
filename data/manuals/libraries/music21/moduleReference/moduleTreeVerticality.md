Source: https://music21.org/music21docs/moduleReference/moduleTreeVerticality.html

# music21.tree.verticality

Object for dealing with vertical simultaneities in a fast way w/o Chord’s overhead.

## Verticality

class music21.tree.verticality.Verticality(*offset: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [Fraction](https://docs.python.org/3/library/fractions.html#fractions.Fraction "(in Python v3.14)") = 0.0*, *overlapTimespans: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[ElementTimespan](moduleTreeSpans.html#music21.tree.spans.ElementTimespan "music21.tree.spans.ElementTimespan"), ...] = ()*, *startTimespans: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[ElementTimespan](moduleTreeSpans.html#music21.tree.spans.ElementTimespan "music21.tree.spans.ElementTimespan"), ...] = ()*, *stopTimespans: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[ElementTimespan](moduleTreeSpans.html#music21.tree.spans.ElementTimespan "music21.tree.spans.ElementTimespan"), ...] = ()*, *timespanTree=None*)[[source]](../_modules/music21/tree/verticality.html#Verticality)
:   A collection of information about elements that are sounding at a given
    offset or just finished at that offset or are continuing from before, etc..

    Create a timespan-stream from a score:

    ```python
    >>> score = corpus.parse('bwv66.6')
    >>> scoreTree = tree.fromStream.asTimespans(score, flatten=True,
    ...        classList=(note.Note, chord.Chord))
    ```

    Find the verticality at offset 6.5, or beat 2.5 of measure 2 (there’s a one
    beat pickup)

    ```python
    >>> verticality = scoreTree.getVerticalityAt(6.5)
    >>> verticality
    <music21.tree.verticality.Verticality 6.5 {E3 D4 G#4 B4}>
    ```

    The representation of a verticality gives the pitches from lowest to
    highest (in sounding notes).

    A verticality knows its offset, but because elements might end at
    different times, it doesn’t know its endTime

    ```python
    >>> verticality.offset
    6.5
    >>> verticality.endTime
    Traceback (most recent call last):
    AttributeError: 'Verticality' object has no attribute 'endTime'
    ```

    However, we can find when the next verticality starts by looking at the nextVerticality

    ```python
    >>> nv = verticality.nextVerticality
    >>> nv
    <music21.tree.verticality.Verticality 7.0 {A2 C#4 E4 A4}>
    >>> nv.offset
    7.0
    ```

    Or more simply:

    ```python
    >>> verticality.nextStartOffset
    7.0
    ```

    (There is also a previousVerticality, but not a previousStartOffset)

    What we just demonstrated is actually very powerful: a Verticality keeps a
    record of exactly where it is in the timespanTree – scores can be
    recreated with this information.

    Getting back to the task at hand, we can find all the PitchedTimespans (and
    from there the elements) that start at exactly 6.5. There’s one, it’s a
    passing tone D in the tenor. It lasts from offset 6.5 to offset 7.0,
    with respect to the beginning of the score, not to the beginning of the
    measure. That is to say, it’s an eighth note.

    ```python
    >>> verticality.startTimespans
    (<PitchedTimespan (6.5 to 7.0) <music21.note.Note D>>,)
    ```

    And we can get all the PitchedTimespans that were already sounding at the
    moment (that is to say, the non-passing tones):

    ```python
    >>> verticality.overlapTimespans
    (<PitchedTimespan (6.0 to 7.0) <music21.note.Note B>>,
     <PitchedTimespan (6.0 to 7.0) <music21.note.Note G#>>,
     <PitchedTimespan (6.0 to 7.0) <music21.note.Note E>>)
    ```

    And we can get all the things that stop right at this moment. It’s the E
    in the tenor preceding the passing tone D:

    ```python
    >>> verticality.stopTimespans
    (<PitchedTimespan (6.0 to 6.5) <music21.note.Note E>>,)
    ```

[`Verticality`](#music21.tree.verticality.Verticality "music21.tree.verticality.Verticality") bases

* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`Verticality`](#music21.tree.verticality.Verticality "music21.tree.verticality.Verticality") read-only properties

Verticality.bassTimespan
:   Gets the bass timespan in this verticality.

    ```python
    >>> score = corpus.parse('bwv66.6')
    >>> scoreTree = tree.fromStream.asTimespans(score, flatten=True,
    ...            classList=(note.Note, chord.Chord))
    >>> verticality = scoreTree.getVerticalityAt(1.0)
    >>> verticality
    <music21.tree.verticality.Verticality 1.0 {F#3 C#4 F#4 A4}>
    ```

    ```python
    >>> verticality.bassTimespan
    <PitchedTimespan (1.0 to 2.0) <music21.note.Note F#>>
    ```

Verticality.beatStrength
:   Gets the beat strength of a verticality.

    ```python
    >>> score = corpus.parse('bwv66.6')
    >>> scoreTree = tree.fromStream.asTimespans(score, flatten=True,
    ...            classList=(note.Note, chord.Chord))
    >>> verticality = scoreTree.getVerticalityAt(1.0)
    >>> verticality.beatStrength
    1.0
    ```

    Note that it will return None if there are no startTimespans at this point:

    ```python
    >>> verticality = scoreTree.getVerticalityAt(1.25)
    >>> verticality
    <music21.tree.verticality.Verticality 1.25 {F#3 C#4 F#4 A4}>
    >>> verticality.startTimespans
    ()
    >>> verticality.beatStrength is None
    True
    ```

Verticality.measureNumber
:   Gets the measure number of the verticality’s starting elements.

    ```python
    >>> score = corpus.parse('bwv66.6')
    >>> scoreTree = tree.fromStream.asTimespans(score, flatten=True,
    ...            classList=(note.Note, chord.Chord))
    >>> verticality = scoreTree.getVerticalityAt(7.0)
    >>> verticality.measureNumber
    2
    ```

Verticality.nextStartOffset
:   Gets the next start-offset in the verticality’s offset-tree.

    ```python
    >>> score = corpus.parse('bwv66.6')
    >>> scoreTree = tree.fromStream.asTimespans(score, flatten=True,
    ...            classList=(note.Note, chord.Chord))
    >>> verticality = scoreTree.getVerticalityAt(1.0)
    >>> verticality.nextStartOffset
    2.0
    ```

    If a verticality has no tree attached, then it will return None

Verticality.nextVerticality
:   Gets the next verticality after a verticality.

    ```python
    >>> score = corpus.parse('bwv66.6')
    >>> scoreTree = tree.fromStream.asTimespans(score, flatten=True,
    ...            classList=(note.Note, chord.Chord))
    >>> verticality = scoreTree.getVerticalityAt(1.0)
    >>> print(verticality)
    <music21.tree.verticality.Verticality 1.0 {F#3 C#4 F#4 A4}>
    ```

    ```python
    >>> nextVerticality = verticality.nextVerticality
    >>> print(nextVerticality)
    <music21.tree.verticality.Verticality 2.0 {G#3 B3 E4 B4}>
    ```

    Verticality objects created by an offset-tree hold a reference back to
    that offset-tree. This means that they determine their next or previous
    verticality dynamically based on the state of the offset-tree only when
    asked. Because of this, it is safe to mutate the offset-tree by
    inserting or removing timespans while iterating over it.

    ```python
    >>> scoreTree.removeTimespanList(nextVerticality.startTimespans)
    >>> verticality.nextVerticality
    <music21.tree.verticality.Verticality 3.0 {A3 E4 C#5}>
    ```

Verticality.pitchClassSet
:   Gets a set of all pitches in a verticality with distinct pitchClasses

    ```python
    >>> n1 = note.Note('C4')
    >>> n2 = note.Note('B#5')
    >>> s = stream.Stream()
    >>> s.insert(4.0, n1)
    >>> s.insert(4.0, n2)
    >>> scoreTree = s.asTimespans()
    >>> verticality = scoreTree.getVerticalityAt(4.0)
    >>> pitchSet = verticality.pitchSet
    >>> list(sorted(pitchSet))
    [<music21.pitch.Pitch C4>, <music21.pitch.Pitch B#5>]
    ```

    PitchClassSet will return only one pitch. Which of these
    is returned is arbitrary.

    ```python
    >>> pitchClassSet = verticality.pitchClassSet
    >>> list(sorted(pitchClassSet))
    [<music21.pitch.Pitch B#5>]
    ```

Verticality.pitchSet
:   Gets the pitch set of all elements in a verticality.

    ```python
    >>> score = corpus.parse('bwv66.6')
    >>> scoreTree = tree.fromStream.asTimespans(score, flatten=True,
    ...            classList=(note.Note, chord.Chord))
    >>> verticality = scoreTree.getVerticalityAt(1.0)
    >>> for pitch in sorted(verticality.pitchSet):
    ...     pitch
    ...
    <music21.pitch.Pitch F#3>
    <music21.pitch.Pitch C#4>
    <music21.pitch.Pitch F#4>
    <music21.pitch.Pitch A4>
    ```

Verticality.previousVerticality
:   Gets the previous verticality before a verticality.

    ```python
    >>> score = corpus.parse('bwv66.6')
    >>> scoreTree = tree.fromStream.asTimespans(score, flatten=True,
    ...            classList=(note.Note, chord.Chord))
    >>> verticality = scoreTree.getVerticalityAt(1.0)
    >>> print(verticality)
    <music21.tree.verticality.Verticality 1.0 {F#3 C#4 F#4 A4}>
    ```

    ```python
    >>> previousVerticality = verticality.previousVerticality
    >>> print(previousVerticality)
    <music21.tree.verticality.Verticality 0.5 {G#3 B3 E4 B4}>
    ```

    Continue it:

    ```python
    >>> v = scoreTree.getVerticalityAt(1.0)
    >>> while v is not None:
    ...     print(v)
    ...     v = v.previousVerticality
    <music21.tree.verticality.Verticality 1.0 {F#3 C#4 F#4 A4}>
    <music21.tree.verticality.Verticality 0.5 {G#3 B3 E4 B4}>
    <music21.tree.verticality.Verticality 0.0 {A3 E4 C#5}>
    ```

    Verticality objects created by an offset-tree hold a reference back to
    that offset-tree. This means that they determine their next or previous
    verticality dynamically based on the state of the offset-tree only when
    asked. Because of this, it is safe to mutate the offset-tree by
    inserting or removing timespans while iterating over it.

    ```python
    >>> scoreTree.removeTimespanList(previousVerticality.startTimespans)
    >>> verticality.previousVerticality
    <music21.tree.verticality.Verticality 0.0 {A3 E4 C#5}>
    ```

Verticality.startAndOverlapTimespans
:   Return a tuple adding the start and overlap timespans into one.

    ```python
    >>> n1 = note.Note('C4')
    >>> n2 = note.Note('D4')
    >>> s = stream.Stream()
    >>> s.insert(4.0, n1)
    >>> s.insert(4.5, n2)
    >>> scoreTree = s.asTimespans()
    >>> verticality = scoreTree.getVerticalityAt(4.5)
    >>> verticality.startTimespans
    (<PitchedTimespan (4.5 to 5.5) <music21.note.Note D>>,)
    ```

    ```python
    >>> verticality.overlapTimespans
    (<PitchedTimespan (4.0 to 5.0) <music21.note.Note C>>,)
    ```

    ```python
    >>> verticality.startAndOverlapTimespans
    (<PitchedTimespan (4.5 to 5.5) <music21.note.Note D>>,
     <PitchedTimespan (4.0 to 5.0) <music21.note.Note C>>)
    ```

    ```python
    >>> verticality = scoreTree.getVerticalityAt(4.0)
    >>> verticality.startAndOverlapTimespans
    (<PitchedTimespan (4.0 to 5.0) <music21.note.Note C>>,)
    ```

Verticality.timeToNextEvent
:   Returns a float or Fraction of the quarterLength to the next
    event (usually the next Verticality, but also to the end of the piece).

    Returns None if there is no next event, such as when the verticality
    is divorced from its tree.

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`Verticality`](#music21.tree.verticality.Verticality "music21.tree.verticality.Verticality") methods

Verticality.getAllVoiceLeadingQuartets(*\**, *includeRests=True*, *includeOblique=True*, *includeNoMotion=False*, *returnObjects: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[False]*, *partPairNumbers: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[PitchedTimespan](moduleTreeSpans.html#music21.tree.spans.PitchedTimespan "music21.tree.spans.PitchedTimespan"), [PitchedTimespan](moduleTreeSpans.html#music21.tree.spans.PitchedTimespan "music21.tree.spans.PitchedTimespan")], [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[PitchedTimespan](moduleTreeSpans.html#music21.tree.spans.PitchedTimespan "music21.tree.spans.PitchedTimespan"), [PitchedTimespan](moduleTreeSpans.html#music21.tree.spans.PitchedTimespan "music21.tree.spans.PitchedTimespan")]]][[source]](../_modules/music21/tree/verticality.html#Verticality.getAllVoiceLeadingQuartets)

Verticality.getAllVoiceLeadingQuartets(*\**, *includeRests=True*, *includeOblique=True*, *includeNoMotion=False*, *returnObjects: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[True] = True*, *partPairNumbers: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[VoiceLeadingQuartet](moduleVoiceLeading.html#music21.voiceLeading.VoiceLeadingQuartet "music21.voiceLeading.VoiceLeadingQuartet")]
:   ```python
    >>> c = corpus.parse('luca/gloria').measures(1, 8)
    >>> tsCol = tree.fromStream.asTimespans(c, flatten=True,
    ...            classList=(note.Note, chord.Chord))
    >>> verticality22 = tsCol.getVerticalityAt(22.0)
    ```

    ```python
    >>> from pprint import pprint as pp
    >>> for vlq in verticality22.getAllVoiceLeadingQuartets():
    ...     pp(vlq)
    <music21.voiceLeading.VoiceLeadingQuartet
        v1n1=G4, v1n2=C4, v2n1=E4, v2n2=F4>
    <music21.voiceLeading.VoiceLeadingQuartet
        v1n1=G4, v1n2=C4, v2n1=A3, v2n2=A3>
    <music21.voiceLeading.VoiceLeadingQuartet
        v1n1=E4, v1n2=F4, v2n1=A3, v2n2=A3>
    ```

    ```python
    >>> for vlq in verticality22.getAllVoiceLeadingQuartets(includeRests=False):
    ...     pp(vlq)
    <music21.voiceLeading.VoiceLeadingQuartet
        v1n1=E4, v1n2=F4, v2n1=A3, v2n2=A3>
    >>> for vlq in verticality22.getAllVoiceLeadingQuartets(includeOblique=False):
    ...     pp(vlq)
    <music21.voiceLeading.VoiceLeadingQuartet
        v1n1=G4, v1n2=C4, v2n1=E4, v2n2=F4>
    >>> verticality22.getAllVoiceLeadingQuartets(includeOblique=False, includeRests=False)
    []
    ```

    Raw output, returns a 2-element tuple of 2-element tuples of PitchedTimespans

    ```python
    >>> for vlqRaw in verticality22.getAllVoiceLeadingQuartets(returnObjects=False):
    ...     pp(vlqRaw)
    ((<PitchedTimespan (19.5 to 21.0) <music21.note.Note G>>,
      <PitchedTimespan (22.0 to 22.5) <music21.note.Note C>>),
     (<PitchedTimespan (21.0 to 22.0) <music21.note.Note E>>,
      <PitchedTimespan (22.0 to 23.0) <music21.note.Note F>>))
    ((<PitchedTimespan (19.5 to 21.0) <music21.note.Note G>>,
      <PitchedTimespan (22.0 to 22.5) <music21.note.Note C>>),
     (<PitchedTimespan (21.5 to 22.5) <music21.note.Note A>>,
      <PitchedTimespan (21.5 to 22.5) <music21.note.Note A>>))
    ((<PitchedTimespan (21.0 to 22.0) <music21.note.Note E>>,
      <PitchedTimespan (22.0 to 23.0) <music21.note.Note F>>),
     (<PitchedTimespan (21.5 to 22.5) <music21.note.Note A>>,
      <PitchedTimespan (21.5 to 22.5) <music21.note.Note A>>))
    ```

    ```python
    >>> for vlq in verticality22.getAllVoiceLeadingQuartets(partPairNumbers=[(0, 1)]):
    ...     pp(vlq)
    <music21.voiceLeading.VoiceLeadingQuartet
        v1n1=G4, v1n2=C4, v2n1=E4, v2n2=F4>
    ```

    ```python
    >>> for vlq in verticality22.getAllVoiceLeadingQuartets(partPairNumbers=[(0, 2), (1, 2)]):
    ...     pp(vlq)
    <music21.voiceLeading.VoiceLeadingQuartet
        v1n1=G4, v1n2=C4, v2n1=A3, v2n2=A3>
    <music21.voiceLeading.VoiceLeadingQuartet
        v1n1=E4, v1n2=F4, v2n1=A3, v2n2=A3>
    ```

    * Changed in v8: all parameters are keyword only.

Verticality.getPairedMotion(*\**, *includeRests: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *includeOblique: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[PitchedTimespan](moduleTreeSpans.html#music21.tree.spans.PitchedTimespan "music21.tree.spans.PitchedTimespan"), [PitchedTimespan](moduleTreeSpans.html#music21.tree.spans.PitchedTimespan "music21.tree.spans.PitchedTimespan")]][[source]](../_modules/music21/tree/verticality.html#Verticality.getPairedMotion)
:   Get a list of two-element tuples that are in the same part
    [TODO: or containing stream??]
    and which move at this verticality.

    ```python
    >>> c = corpus.parse('luca/gloria').measures(1, 8)
    >>> tsCol = tree.fromStream.asTimespans(c, flatten=True,
    ...            classList=(note.Note, chord.Chord))
    >>> verticality22 = tsCol.getVerticalityAt(22.0)
    >>> for pm in verticality22.getPairedMotion():
    ...     print(pm)
    (<PitchedTimespan (19.5 to 21.0) <music21.note.Note G>>,
     <PitchedTimespan (22.0 to 22.5) <music21.note.Note C>>)
    (<PitchedTimespan (21.0 to 22.0) <music21.note.Note E>>,
     <PitchedTimespan (22.0 to 23.0) <music21.note.Note F>>)
    (<PitchedTimespan (21.5 to 22.5) <music21.note.Note A>>,
     <PitchedTimespan (21.5 to 22.5) <music21.note.Note A>>)
    ```

    Note that the second pair contains a one-beat rest at 21.0-22.0;
    so includeRests=False will
    get rid of that:

    ```python
    >>> for pm in verticality22.getPairedMotion(includeRests=False):
    ...     print(pm)
    (<PitchedTimespan (21.0 to 22.0) <music21.note.Note E>>,
     <PitchedTimespan (22.0 to 23.0) <music21.note.Note F>>)
    (<PitchedTimespan (21.5 to 22.5) <music21.note.Note A>>,
     <PitchedTimespan (21.5 to 22.5) <music21.note.Note A>>)
    ```

    Oblique here means a pair that does not move (it could be called noMotion,
    because there’s no motion
    here in a two-note pair, but we still call it includeOblique so it’s consistent with
    getAllVoiceLeadingQuartets).

    ```python
    >>> for pm in verticality22.getPairedMotion(includeOblique=False):
    ...     print(pm)
    (<PitchedTimespan (19.5 to 21.0) <music21.note.Note G>>,
     <PitchedTimespan (22.0 to 22.5) <music21.note.Note C>>)
    (<PitchedTimespan (21.0 to 22.0) <music21.note.Note E>>,
     <PitchedTimespan (22.0 to 23.0) <music21.note.Note F>>)
    ```

    ```python
    >>> for pm in verticality22.getPairedMotion(includeOblique=False, includeRests=False):
    ...     print(pm)
    (<PitchedTimespan (21.0 to 22.0) <music21.note.Note E>>,
     <PitchedTimespan (22.0 to 23.0) <music21.note.Note F>>)
    ```

    Changed in v9.3 – arguments are keyword only

Verticality.makeElement(*quarterLength: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [Fraction](https://docs.python.org/3/library/fractions.html#fractions.Fraction "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\**, *addTies=True*, *addPartIdAsGroup=False*, *removeRedundantPitches=True*, *gatherArticulations='single'*, *gatherExpressions='single'*, *copyPitches=True*) → [Rest](moduleNote.html#music21.note.Rest "music21.note.Rest") | [Chord](moduleChord.html#music21.chord.Chord "music21.chord.Chord")[[source]](../_modules/music21/tree/verticality.html#Verticality.makeElement)
:   Makes a Chord or Rest from this verticality and quarterLength.

    ```python
    >>> score = tree.examples.makeExampleScore()
    >>> scoreTree = tree.fromStream.asTimespans(score, flatten=True,
    ...            classList=(note.Note, chord.Chord))
    >>> verticality = scoreTree.getVerticalityAt(4.0)
    >>> verticality
    <music21.tree.verticality.Verticality 4.0 {E#3 G3}>
    >>> verticality.startTimespans
    (<PitchedTimespan (4.0 to 5.0) <music21.note.Note G>>,
     <PitchedTimespan (4.0 to 6.0) <music21.note.Note E#>>)
    ```

    ```python
    >>> el = verticality.makeElement(2.0)
    >>> el
    <music21.chord.Chord E#3 G3>
    >>> el.duration.quarterLength
    2.0
    >>> el.duration.type
    'half'
    ```

    If there is nothing there, then a Rest is created

    ```python
    >>> verticality = scoreTree.getVerticalityAt(400.0)
    >>> verticality
    <music21.tree.verticality.Verticality 400.0 {}>
    >>> el = verticality.makeElement(1/3)
    >>> el
    <music21.note.Rest 1/3ql>
    >>> el.duration.fullName
    'Eighth Triplet (1/3 QL)'
    ```

    ```python
    >>> n1 = note.Note('C4')
    >>> n2 = note.Note('C4')
    >>> s = stream.Score()
    >>> s.insert(0, n1)
    >>> s.insert(0.5, n2)
    >>> scoreTree = s.asTimespans()
    >>> verticality = scoreTree.getVerticalityAt(0.5)
    >>> c = verticality.makeElement(0.5)
    >>> c
    <music21.chord.Chord C4>
    ```

    ```python
    >>> c = verticality.makeElement(0.5, removeRedundantPitches=False)
    >>> c
    <music21.chord.Chord C4 C4>
    ```

    Generally the pitches of the new element are not connected to the original pitch:

    ```python
    >>> c[0].pitch.name = 'E'
    >>> c[1].pitch.name = 'F'
    >>> (n1.name, n2.name)
    ('C', 'C')
    ```

    But if copyPitches is False then the original pitch will be used:

    ```python
    >>> n1.name = 'D'
    >>> n2.name = 'E'
    >>> c = verticality.makeElement(0.5, removeRedundantPitches=False, copyPitches=False)
    >>> c
    <music21.chord.Chord D4 E4>
    ```

    ```python
    >>> c[0].pitch.name = 'F'
    >>> c[1].pitch.name = 'G'
    >>> (n1.name, n2.name)
    ('F', 'G')
    ```

    gatherArticulations and gatherExpressions can be True, False, or (default) ‘single’.

    * If False, no articulations (or expressions) are transferred to the chord.
    * If True, all articulations are transferred to the chord.
    * If ‘single’, then no more than one articulation of each class
      (chosen from the lowest note) will be added.
      This way, the chord does not get 4 fermatas, etc.

    ```python
    >>> n1 = note.Note('C4')
    >>> n2 = note.Note('D4')
    >>> s = stream.Stream()
    >>> s.insert(0, n1)
    >>> s.insert(0.5, n2)
    ```

    ```python
    >>> class AllAttachArticulation(articulations.Articulation):
    ...     def __init__(self):
    ...         super().__init__()
    ...         self.tieAttach = 'all'
    ```

    ```python
    >>> class OtherAllAttachArticulation(articulations.Articulation):
    ...     def __init__(self):
    ...         super().__init__()
    ...         self.tieAttach = 'all'
    ```

    ```python
    >>> n1.articulations.append(articulations.Accent())
    >>> n1.articulations.append(AllAttachArticulation())
    >>> n1.expressions.append(expressions.Fermata())
    ```

    ```python
    >>> n2.articulations.append(articulations.Staccato())
    >>> n2.articulations.append(AllAttachArticulation())
    >>> n2.articulations.append(OtherAllAttachArticulation())
    >>> n2.expressions.append(expressions.Fermata())
    ```

    ```python
    >>> scoreTree = s.asTimespans()
    ```

    ```python
    >>> verticality = scoreTree.getVerticalityAt(0.0)
    >>> c = verticality.makeElement(1.0)
    >>> c.expressions
    [<music21.expressions.Fermata>]
    >>> c.articulations
    [<music21.articulations.Accent>, <...AllAttachArticulation>]
    ```

    ```python
    >>> verticality = scoreTree.getVerticalityAt(0.5)
    ```

    Here there will be no expressions, because there is no note ending
    at 0.75 and Fermatas attach to the last note:

    ```python
    >>> c = verticality.makeElement(0.25)
    >>> c.expressions
    []
    ```

    ```python
    >>> c = verticality.makeElement(0.5)
    >>> c.expressions
    [<music21.expressions.Fermata>]
    ```

    Only two articulations, since accent attaches to beginning
    and staccato attaches to last
    and we are beginning after the start of the first note (with an accent)
    and cutting right through the second note (with a staccato)

    ```python
    >>> c.articulations
    [<...AllAttachArticulation>,
     <...OtherAllAttachArticulation>]
    ```

    ```python
    >>> c = verticality.makeElement(0.5, gatherArticulations=True)
    >>> c.articulations
    [<...AllAttachArticulation>,
     <...AllAttachArticulation>,
     <...OtherAllAttachArticulation>]
    ```

    ```python
    >>> c = verticality.makeElement(0.5, gatherArticulations=False)
    >>> c.articulations
    []
    ```

    ```python
    >>> verticality = scoreTree.getVerticalityAt(1.0)
    >>> c = verticality.makeElement(0.5)
    >>> c.expressions
    [<music21.expressions.Fermata>]
    >>> c.articulations
    [<music21.articulations.Staccato>,
     <...AllAttachArticulation>,
     <...OtherAllAttachArticulation>]
    ```

    * New in v6.3: copyPitches option

Verticality.toChord()[[source]](../_modules/music21/tree/verticality.html#Verticality.toChord)
:   Creates a chord.Chord object of default length (1.0 or
    the duration of some note object) from the verticality.

    Does nothing about ties, etc. – it’s a very dumb chord, but useful
    for querying consonance, etc. See makeElement() for the smart version.

    It may be a zero- or one-pitch chord.

    ```python
    >>> score = corpus.parse('bwv66.6')
    >>> scoreTree = score.asTimespans()
    >>> verticality = scoreTree.getVerticalityAt(4.0)
    >>> verticality.toChord()
    <music21.chord.Chord G#3 B3 E4 E5>
    ```

[`Verticality`](#music21.tree.verticality.Verticality "music21.tree.verticality.Verticality") instance variables

Verticality.offset
:   Gets the start offset of a verticality.

    ```python
    >>> score = corpus.parse('bwv66.6')
    >>> scoreTree = tree.fromStream.asTimespans(score, flatten=True,
    ...            classList=(note.Note, chord.Chord))
    >>> verticality = scoreTree.getVerticalityAt(1.0)
    >>> verticality
    <music21.tree.verticality.Verticality 1.0 {F#3 C#4 F#4 A4}>
    >>> verticality.offset
    1.0
    ```

Verticality.offsetTree
:   Returns the tree initially set else None

Verticality.overlapTimespans
:   Gets timespans overlapping the start offset of a verticality.

    ```python
    >>> score = corpus.parse('bwv66.6')
    >>> scoreTree = tree.fromStream.asTimespans(score, flatten=True,
    ...            classList=(note.Note, chord.Chord))
    >>> verticality = scoreTree.getVerticalityAt(0.5)
    >>> verticality
    <music21.tree.verticality.Verticality 0.5 {G#3 B3 E4 B4}>
    >>> verticality.overlapTimespans
    (<PitchedTimespan (0.0 to 1.0) <music21.note.Note E>>,)
    ```

Verticality.startTimespans
:   Gets the timespans starting at a verticality’s start offset.

    ```python
    >>> score = corpus.parse('bwv66.6')
    >>> scoreTree = tree.fromStream.asTimespans(score, flatten=True,
    ...            classList=(note.Note, chord.Chord))
    >>> verticality = scoreTree.getVerticalityAt(1.0)
    >>> verticality
    <music21.tree.verticality.Verticality 1.0 {F#3 C#4 F#4 A4}>
    >>> for timespan in verticality.startTimespans:
    ...     timespan
    ...
    <PitchedTimespan (1.0 to 2.0) <music21.note.Note A>>
    <PitchedTimespan (1.0 to 2.0) <music21.note.Note F#>>
    <PitchedTimespan (1.0 to 2.0) <music21.note.Note C#>>
    <PitchedTimespan (1.0 to 2.0) <music21.note.Note F#>>
    ```

Verticality.stopTimespans
:   Gets the timespans stopping at a verticality’s start offset.

    ```python
    >>> score = corpus.parse('bwv66.6')
    >>> scoreTree = tree.fromStream.asTimespans(score, flatten=True,
    ...                classList=(note.Note, chord.Chord))
    >>> verticality = scoreTree.getVerticalityAt(1.0)
    >>> verticality
    <music21.tree.verticality.Verticality 1.0 {F#3 C#4 F#4 A4}>
    ```

    Note that none of the elements in the stopTimespans are listed in
    the repr for the Verticality

    ```python
    >>> for timespan in verticality.stopTimespans:
    ...     timespan
    ...
    <PitchedTimespan (0.0 to 1.0) <music21.note.Note E>>
    <PitchedTimespan (0.5 to 1.0) <music21.note.Note B>>
    <PitchedTimespan (0.5 to 1.0) <music21.note.Note B>>
    <PitchedTimespan (0.5 to 1.0) <music21.note.Note G#>>
    ```

Verticality.timespanTree
:   Returns the tree initially set if it was a TimespanTree, else None

## VerticalitySequence

class music21.tree.verticality.VerticalitySequence(*verticalities: [Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "(in Python v3.14)")[[Verticality](#music21.tree.verticality.Verticality "music21.tree.verticality.Verticality")]*)[[source]](../_modules/music21/tree/verticality.html#VerticalitySequence)
:   A segment of verticalities.

[`VerticalitySequence`](#music21.tree.verticality.VerticalitySequence "music21.tree.verticality.VerticalitySequence") bases

* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`VerticalitySequence`](#music21.tree.verticality.VerticalitySequence "music21.tree.verticality.VerticalitySequence") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`VerticalitySequence`](#music21.tree.verticality.VerticalitySequence "music21.tree.verticality.VerticalitySequence") methods

VerticalitySequence.\_\_getitem\_\_(*item*)[[source]](../_modules/music21/tree/verticality.html#VerticalitySequence.__getitem__)

VerticalitySequence.unwrap()[[source]](../_modules/music21/tree/verticality.html#VerticalitySequence.unwrap)
