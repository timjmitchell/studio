Source: https://music21.org/music21docs/moduleReference/moduleAnalysisMetrical.html

# music21.analysis.metrical

Various tools and utilities for doing metrical or rhythmic analysis.

See the chapter [User’s Guide Chapter 14: Time Signatures](../usersGuide/usersGuide_14_timeSignatures.html#usersguide-14-timesignatures)
for more information on defining
metrical structures in music21.

## Functions

music21.analysis.metrical.labelBeatDepth(*streamIn*)[[source]](../_modules/music21/analysis/metrical.html#labelBeatDepth)
:   Modify a Stream in place by annotating metrical analysis symbols.

    This assumes that the Stream is already partitioned into Measures.

    ```python
    >>> s = stream.Stream()
    >>> ts = meter.TimeSignature('4/4')
    >>> s.insert(0, ts)
    >>> n = note.Note(type='eighth')
    >>> s.repeatAppend(n, 8)
    >>> s.makeMeasures(inPlace=True)
    >>> post = analysis.metrical.labelBeatDepth(s)
    >>> sOut = []
    >>> for n in s.flatten().notes:
    ...     stars = "".join([l.text for l in n.lyrics])
    ...     sOut.append(f'{n.beatStr:8s} {stars}')
    >>> print("\n".join(sOut))
    1        ****
    1 1/2    *
    2        **
    2 1/2    *
    3        ***
    3 1/2    *
    4        **
    4 1/2    *
    ```

music21.analysis.metrical.thomassenMelodicAccent(*streamIn: [Stream](moduleStreamBase.html#music21.stream.base.Stream "music21.stream.base.Stream")*)[[source]](../_modules/music21/analysis/metrical.html#thomassenMelodicAccent)
:   Adds an attribute, ‘melodicAccent’ to each note’s .editorial
    within a `Stream` object
    according to the method postulated in Joseph M. Thomassen, “Melodic accent: Experiments and
    a tentative model,” ‘’Journal of the Acoustical Society of America’’, Vol. 71, No. 6 (1982) pp.
    1598-1605; with, Erratum, ‘’Journal of the Acoustical Society of America’’, Vol. 73,
    No. 1 (1983) p.373, and in David Huron and Matthew Royal,
    “What is melodic accent? Converging evidence
    from musical practice.” ‘’Music Perception’’, Vol. 13, No. 4 (1996) pp. 489-516.

    Similar to the humdrum [melac](https://www.humdrum.org/Humdrum/commands/melac.html) tool.

    Takes in a Stream of [`Note`](moduleNote.html#music21.note.Note "music21.note.Note") objects (use .flatten().notes to get it, or
    better .flatten().getElementsByClass(note.Note) to filter out chords)
    and adds the attribute to
    each. Note that Huron and Royal’s work suggests that melodic accent has a correlation
    with metrical accent only for solo works/passages; even treble passages do not have a
    strong correlation. (Gregorian chants were found to have a strong ‘’negative’’ correlation
    between melodic accent and syllable onsets)

    Following Huron’s lead, we assign a melodicAccent of 1.0 to the first note in a piece
    and take the accent marker of the first interval alone to the second note and
    of the last interval alone to be the accent of the last note.

    Example from Thomassen, figure 5:

    ```python
    >>> s = converter.parse('tinynotation: 7/4 c4 c c d e d d')
    >>> analysis.metrical.thomassenMelodicAccent(s.flatten().notes)
    >>> for n in s.flatten().notes:
    ...    (n.pitch.nameWithOctave, n.editorial.melodicAccent)
    ('C4', 1.0)
    ('C4', 0.0)
    ('C4', 0.0)
    ('D4', 0.33)
    ('E4', 0.5561)
    ('D4', 0.17)
    ('D4', 0.0)
    ```
