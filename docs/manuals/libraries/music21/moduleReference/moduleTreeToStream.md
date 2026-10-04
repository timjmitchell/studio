Source: https://music21.org/music21docs/moduleReference/moduleTreeToStream.html

# music21.tree.toStream

Tools for generating new Streams from trees (fast, manipulable objects)

None of these things work acceptably yet. This is super beta.

## Functions

music21.tree.toStream.chordified(*timespans*, *templateStream=None*)[[source]](../_modules/music21/tree/toStream.html#chordified)
:   DEPRECATED – DO NOT USE. Use stream.chordify() instead.

    Creates a score from the PitchedTimespan objects stored in this
    offset-tree.

    A “template” score may be used to provide measure and time-signature
    information.

    ```python
    >>> score = corpus.parse('bwv66.6')
    >>> scoreTree = score.asTimespans()
    >>> chordifiedScore = tree.toStream.chordified(scoreTree, templateStream=score)
    >>> chordifiedScore.show('text')
    {0.0} <music21.instrument.Instrument 'P1: Soprano: Instrument 1'>
    {0.0} <music21.stream.Measure 0 offset=0.0>
        {0.0} <music21.clef.TrebleClef>
        {0.0} <music21.key.Key of f# minor>
        {0.0} <music21.meter.TimeSignature 4/4>
        {0.0} <music21.chord.Chord A3 E4 C#5>
        {0.5} <music21.chord.Chord G#3 B3 E4 B4>
    {1.0} <music21.stream.Measure 1 offset=1.0>
        {0.0} <music21.chord.Chord F#3 C#4 F#4 A4>
        {1.0} <music21.chord.Chord G#3 B3 E4 B4>
        {2.0} <music21.chord.Chord A3 E4 C#5>
        {3.0} <music21.chord.Chord G#3 B3 E4 E5>
    {5.0} <music21.stream.Measure 2 offset=5.0>
        {0.0} <music21.chord.Chord A3 E4 C#5>
        {0.5} <music21.chord.Chord C#3 E4 A4 C#5>
        {1.0} <music21.chord.Chord E3 E4 G#4 B4>
        {1.5} <music21.chord.Chord E3 D4 G#4 B4>
        {2.0} <music21.chord.Chord A2 C#4 E4 A4>
        {3.0} <music21.chord.Chord E#3 C#4 G#4 C#5>
    {9.0} <music21.stream.Measure 3 offset=9.0>
        {0.0} <music21.layout.SystemLayout>
    ...
    ```

music21.tree.toStream.partwise(*tsTree: [music21.tree.timespanTree.TimespanTree](moduleTreeTimespanTree.html#music21.tree.timespanTree.TimespanTree "music21.tree.timespanTree.TimespanTree")*, *templateStream: music21.stream.Score*)[[source]](../_modules/music21/tree/toStream.html#partwise)
:   DEPRECATED in v7 – use chordify()
