Source: https://music21.org/music21docs/moduleReference/moduleTreeExamples.html

# music21.tree.examples

## Functions

music21.tree.examples.makeExampleScore()[[source]](../_modules/music21/tree/examples.html#makeExampleScore)
:   Makes example score for use in stream-to-tree conversion docs.

    ```python
    >>> sc = tree.examples.makeExampleScore()
    >>> sc.show('text')
    {0.0} <music21.stream.Part ...>
        {0.0} <music21.instrument.Instrument 'PartA: : '>
        {0.0} <music21.stream.Measure 1 offset=0.0>
            {0.0} <music21.clef.BassClef>
            {0.0} <music21.meter.TimeSignature 2/4>
            {0.0} <music21.note.Note C>
            {1.0} <music21.note.Note D>
        {2.0} <music21.stream.Measure 2 offset=2.0>
            {0.0} <music21.note.Note E>
            {1.0} <music21.note.Note F>
        {4.0} <music21.stream.Measure 3 offset=4.0>
            {0.0} <music21.note.Note G>
            {1.0} <music21.note.Note A>
        {6.0} <music21.stream.Measure 4 offset=6.0>
            {0.0} <music21.note.Note B>
            {1.0} <music21.note.Note C>
            {2.0} <music21.bar.Barline type=final>
    {0.0} <music21.stream.Part ...>
        {0.0} <music21.instrument.Instrument 'PartB: : '>
        {0.0} <music21.stream.Measure 1 offset=0.0>
            {0.0} <music21.clef.BassClef>
            {0.0} <music21.meter.TimeSignature 2/4>
            {0.0} <music21.note.Note C#>
        {2.0} <music21.stream.Measure 2 offset=2.0>
            {0.0} <music21.note.Note G#>
        {4.0} <music21.stream.Measure 3 offset=4.0>
            {0.0} <music21.note.Note E#>
        {6.0} <music21.stream.Measure 4 offset=6.0>
            {0.0} <music21.note.Note D#>
            {2.0} <music21.bar.Barline type=final>
    ```
