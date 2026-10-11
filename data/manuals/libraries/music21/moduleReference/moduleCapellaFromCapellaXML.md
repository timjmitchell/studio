Source: https://music21.org/music21docs/moduleReference/moduleCapellaFromCapellaXML.html

# music21.capella.fromCapellaXML

A beta version of a complete .capx to music21 converter.

Currently only handles one <voice> per <staff> and does not deal with
Slurs, Dynamics, Ornamentation, etc.

Does not handle pickup notes, which are defined simply with an early barline
(same as incomplete bars at the end).

## CapellaImporter

class music21.capella.fromCapellaXML.CapellaImporter[[source]](../_modules/music21/capella/fromCapellaXML.html#CapellaImporter)
:   Object for importing .capx, CapellaXML files into music21 (from which they can be
    converted to musicxml, MIDI, lilypond, etc.)

    Note that Capella stores files closer to their printed versions – that is to say,
    Systems enclose all the parts for that system and have new clefs etc.

[`CapellaImporter`](#music21.capella.fromCapellaXML.CapellaImporter "music21.capella.fromCapellaXML.CapellaImporter") methods

CapellaImporter.accidentalFromAlter(*alterElement*)[[source]](../_modules/music21/capella/fromCapellaXML.html#CapellaImporter.accidentalFromAlter)
:   return a [`Accidental`](modulePitch.html#music21.pitch.Accidental "music21.pitch.Accidental") object from an <alter> tag.

    ```python
    >>> ci = capella.fromCapellaXML.CapellaImporter()
    >>> alter = ci.domElementFromText('<alter step="-1"/>')
    >>> ci.accidentalFromAlter(alter)
    <music21.pitch.Accidental flat>
    ```

    The only known display type is “suppress”

    ```python
    >>> alter = ci.domElementFromText('<alter step="2" display="suppress"/>')
    >>> accidentalObject = ci.accidentalFromAlter(alter)
    >>> accidentalObject
    <music21.pitch.Accidental double-sharp>
    >>> accidentalObject.displayType
    'never'
    ```

CapellaImporter.barlineListFromBarline(*barlineElement*)[[source]](../_modules/music21/capella/fromCapellaXML.html#CapellaImporter.barlineListFromBarline)
:   Indication that the barline at this point should be something other than normal.

    Capella does not indicate measure breaks or barline breaks normally, so the only barlines
    that are indicated are unusual ones.

    Returns a LIST of [`Barline`](moduleBar.html#music21.bar.Barline "music21.bar.Barline") or [`Repeat`](moduleBar.html#music21.bar.Repeat "music21.bar.Repeat") objects
    because the repEndBegin type requires two bar.Repeat objects to encode in music21.

    ```python
    >>> ci = capella.fromCapellaXML.CapellaImporter()
    >>> barlineTag = ci.domElementFromText('<barline type="end"/>')
    >>> ci.barlineListFromBarline(barlineTag)
    [<music21.bar.Barline type=final>]
    ```

    ```python
    >>> repeatTag = ci.domElementFromText('<barline type="repEndBegin"/>')
    >>> ci.barlineListFromBarline(repeatTag)
    [<music21.bar.Repeat direction=end>, <music21.bar.Repeat direction=start>]
    ```

CapellaImporter.chordOrNoteFromChord(*chordElement*)[[source]](../_modules/music21/capella/fromCapellaXML.html#CapellaImporter.chordOrNoteFromChord)
:   returns a [`Note`](moduleNote.html#music21.note.Note "music21.note.Note") or [`Chord`](moduleChord.html#music21.chord.Chord "music21.chord.Chord")
    from a chordElement – a Note
    is returned if the <chord> has one <head> element, a Chord is
    returned if there are multiple <head> elements.

    ```python
    >>> ci = capella.fromCapellaXML.CapellaImporter()
    >>> chordElement = ci.domElementFromText(
    ...     '<chord><duration base="1/1"/><heads><head pitch="G4"/></heads></chord>')
    >>> n = ci.chordOrNoteFromChord(chordElement)
    >>> n
    <music21.note.Note G>
    >>> n.duration
    <music21.duration.Duration 4.0>
    ```

    This one is an actual chord

    ```python
    >>> chordElement = ci.domElementFromText(
    ...        '<chord><duration base="1/8"/>' +
    ...        '<heads><head pitch="G4"/><head pitch="A5"/></heads></chord>')
    >>> c = ci.chordOrNoteFromChord(chordElement)
    >>> c
    <music21.chord.Chord G3 A4>
    >>> c.duration
    <music21.duration.Duration 0.5>
    ```

CapellaImporter.clefFromClefSign(*clefSign*)[[source]](../_modules/music21/capella/fromCapellaXML.html#CapellaImporter.clefFromClefSign)
:   returns a [`Clef`](moduleClef.html#music21.clef.Clef "music21.clef.Clef") object or subclass from a <clefSign> tag.

    ```python
    >>> ci = capella.fromCapellaXML.CapellaImporter()
    >>> clefSign = ci.domElementFromText('<clefSign clef="treble"/>')
    >>> ci.clefFromClefSign(clefSign)
    <music21.clef.TrebleClef>
    ```

    ```python
    >>> clefSign = ci.domElementFromText('<clefSign clef="G2-"/>')
    >>> ci.clefFromClefSign(clefSign)
    <music21.clef.Treble8vbClef>
    ```

    ```python
    >>> clefSign = ci.domElementFromText('<clefSign clef="F1+"/>')
    >>> clefObject = ci.clefFromClefSign(clefSign)
    >>> clefObject
    <music21.clef.FClef>
    >>> clefObject.sign
    'F'
    >>> clefObject.line
    1
    >>> clefObject.octaveChange
    1
    ```

CapellaImporter.domElementFromText(*xmlText=None*)[[source]](../_modules/music21/capella/fromCapellaXML.html#CapellaImporter.domElementFromText)
:   Utility method, especially for the documentation examples/tests, which uses
    xml.etree.ElementTree to parse the string and returns its root object.

    Not used by the main parser

    ```python
    >>> ci = capella.fromCapellaXML.CapellaImporter()
    >>> funnyTag = ci.domElementFromText(
    ...    '<funny yes="definitely"><greg/>hi<greg><ha>ha</ha>' +
    ...    '<greg type="embedded"/></greg></funny>')
    >>> funnyTag
    <Element 'funny' at 0x...>
    ```

    iter searches recursively

    ```python
    >>> len(list(funnyTag.iter('greg')))
    3
    ```

    findall does not:

    ```python
    >>> len(funnyTag.findall('greg'))
    2
    ```

CapellaImporter.durationFromDuration(*durationElement*)[[source]](../_modules/music21/capella/fromCapellaXML.html#CapellaImporter.durationFromDuration)
:   Return a music21.duration.Duration element from an XML Element representing
    a duration.

    ```python
    >>> ci = capella.fromCapellaXML.CapellaImporter()
    >>> durationTag = ci.domElementFromText('<duration base="1/32" dots="1"/>')
    >>> durationObj = ci.durationFromDuration(durationTag)
    >>> durationObj
    <music21.duration.Duration 0.1875>
    >>> durationObj.type
    '32nd'
    >>> durationObj.dots
    1
    ```

    Here with Tuplets

    ```python
    >>> durationTag2 = ci.domElementFromText(
    ...      '<duration base="1/4"><tuplet count="3"/></duration>')
    >>> d2 = ci.durationFromDuration(durationTag2)
    >>> d2
    <music21.duration.Duration 2/3>
    >>> d2.type
    'quarter'
    >>> d2.tuplets
    (<music21.duration.Tuplet 3/2>,)
    ```

    Does not handle noDuration=’true’, display, churchStyle on rest durations

CapellaImporter.keySignatureFromKeySign(*keySign*)[[source]](../_modules/music21/capella/fromCapellaXML.html#CapellaImporter.keySignatureFromKeySign)
:   Returns a [`KeySignature`](moduleKey.html#music21.key.KeySignature "music21.key.KeySignature") object from a keySign tag.

    ```python
    >>> ci = capella.fromCapellaXML.CapellaImporter()
    >>> keySign = ci.domElementFromText('<keySign fifths="-1"/>')
    >>> ci.keySignatureFromKeySign(keySign)
    <music21.key.KeySignature of 1 flat>
    ```

CapellaImporter.lyricFromVerse(*verse*)[[source]](../_modules/music21/capella/fromCapellaXML.html#CapellaImporter.lyricFromVerse)
:   returns a [`Lyric`](moduleNote.html#music21.note.Lyric "music21.note.Lyric") object from a <verse> tag

    ```python
    >>> ci = capella.fromCapellaXML.CapellaImporter()
    >>> verse = ci.domElementFromText('<verse i="0" hyphen="true">di&quot;</verse>')
    >>> ci.lyricFromVerse(verse)
    <music21.note.Lyric number=1 syllabic=begin text='di"'>
    ```

    Does not yet support ‘align’ attribute

    if the text is empty, returns None

CapellaImporter.lyricListFromLyric(*lyricElement*)[[source]](../_modules/music21/capella/fromCapellaXML.html#CapellaImporter.lyricListFromLyric)
:   returns a list of [`Lyric`](moduleNote.html#music21.note.Lyric "music21.note.Lyric") objects from a <lyric> tag

    ```python
    >>> ci = capella.fromCapellaXML.CapellaImporter()
    >>> lyricEl = ci.domElementFromText(
    ...      '<lyric><verse i="0" hyphen="true">di</verse>' +
    ...      '<verse i="1">man,</verse><verse i="2">frau,</verse></lyric>')
    >>> ci.lyricListFromLyric(lyricEl)
    [<music21.note.Lyric number=1 syllabic=begin text='di'>,
     <music21.note.Lyric number=2 syllabic=single text='man,'>,
     <music21.note.Lyric number=3 syllabic=single text='frau,'>]
    ```

CapellaImporter.noteFromHead(*headElement*)[[source]](../_modules/music21/capella/fromCapellaXML.html#CapellaImporter.noteFromHead)
:   return a [`Note`](moduleNote.html#music21.note.Note "music21.note.Note") object from a <head> element. This will become
    part of Chord.\_notes if there are multiple, but in any case, it needs to be a Note
    not a Pitch for now, because it could have Tie information

    ```python
    >>> ci = capella.fromCapellaXML.CapellaImporter()
    >>> headElement = ci.domElementFromText(
    ...      '<head pitch="B7"><alter step="-1"/><tie end="true"/></head>')
    >>> n = ci.noteFromHead(headElement)
    >>> n
    <music21.note.Note B->
    >>> n.octave  # capella octaves are one higher than written
    6
    >>> n.tie
    <music21.tie.Tie stop>
    ```

CapellaImporter.notesFromHeads(*headsElement*)[[source]](../_modules/music21/capella/fromCapellaXML.html#CapellaImporter.notesFromHeads)
:   returns a list of [`Note`](moduleNote.html#music21.note.Note "music21.note.Note") elements for each <head> in <heads>

    ```python
    >>> ci = capella.fromCapellaXML.CapellaImporter()
    >>> headsElement = ci.domElementFromText(
    ...    '<heads><head pitch="B7"><alter step="-1"/></head><head pitch="C2"/></heads>')
    >>> ci.notesFromHeads(headsElement)
    [<music21.note.Note B->, <music21.note.Note C>]
    ```

CapellaImporter.parseXMLText(*xmlText=None*)[[source]](../_modules/music21/capella/fromCapellaXML.html#CapellaImporter.parseXMLText)
:   Takes the string (or unicode string) in xmlText and parses it with xml.etree.
    Sets self.mainDom to the dom object and returns the dom object.

CapellaImporter.partScoreFromSystemScore(*systemScore: [Score](moduleStreamBase.html#music21.stream.base.Score "music21.stream.base.Score")*) → [Score](moduleStreamBase.html#music21.stream.base.Score "music21.stream.base.Score")[[source]](../_modules/music21/capella/fromCapellaXML.html#CapellaImporter.partScoreFromSystemScore)
:   Take a `Score` object which is organized
    by Systems and return a new Score object which is organized by
    Parts.

CapellaImporter.readCapellaXMLFile(*filename*)[[source]](../_modules/music21/capella/fromCapellaXML.html#CapellaImporter.readCapellaXMLFile)
:   Reads in a .capx file at filename, stores it as self.zipFilename, unzips it,
    extracts the score.xml embedded file, sets self.xmlText to the contents.

    Returns self.xmlText

CapellaImporter.restFromRest(*restElement*)[[source]](../_modules/music21/capella/fromCapellaXML.html#CapellaImporter.restFromRest)
:   Returns a `Rest` object from a <rest> tag.

    ```python
    >>> ci = capella.fromCapellaXML.CapellaImporter()
    >>> restElement = ci.domElementFromText('<rest><duration base="1/2"/></rest>')
    >>> r = ci.restFromRest(restElement)
    >>> r
    <music21.note.Rest half>
    >>> r.duration.type
    'half'
    ```

CapellaImporter.scoreFromFile(*filename*, *systemScore=False*)[[source]](../_modules/music21/capella/fromCapellaXML.html#CapellaImporter.scoreFromFile)
:   main program: opens a file given by filename and returns a complete
    music21 Score from it.

    If systemScore is True then it skips the step of making Parts from Systems
    and Measures within Parts.

CapellaImporter.slurFromDrawObjSlur(*drawObj*)[[source]](../_modules/music21/capella/fromCapellaXML.html#CapellaImporter.slurFromDrawObjSlur)
:   not implemented

CapellaImporter.streamFromNoteObjects(*noteObjectsElement*, *streamObj=None*)[[source]](../_modules/music21/capella/fromCapellaXML.html#CapellaImporter.streamFromNoteObjects)
:   Converts a <noteObjects> tag into a `Stream` object
    which is returned.
    A Stream can be given as an optional argument, in which case the objects of this
    Stream are appended to this object.

    ```python
    >>> ci = capella.fromCapellaXML.CapellaImporter()
    >>> noteObjectsString = r"""
    ...           <noteObjects>
    ...                <clefSign clef="G2-"/>
    ...                <keySign fifths="-1"/>
    ...                <chord>
    ...                    <duration base="1/2"/>
    ...                    <lyric>
    ...                        <verse i="0">das,</verse>
    ...                        <verse i="1">scherz,</verse>
    ...                    </lyric>
    ...                    <heads>
    ...                        <head pitch="G4"/>
    ...                    </heads>
    ...                </chord>
    ...                <chord>
    ...                    <duration base="1/2"/>
    ...                    <lyric>
    ...                        <verse i="0">so</verse>
    ...                        <verse i="1">der</verse>
    ...                    </lyric>
    ...                    <heads>
    ...                        <head pitch="A4"/>
    ...                    </heads>
    ...                </chord>
    ...                <barline type="end"/>
    ...            </noteObjects>
    ...            """
    >>> noteObjectsElement = ci.domElementFromText(noteObjectsString)
    >>> streamObj = ci.streamFromNoteObjects(noteObjectsElement)
    >>> streamObj.show('text')
    {0.0} <music21.clef.Treble8vbClef>
    {0.0} <music21.key.KeySignature of 1 flat>
    {0.0} <music21.note.Note G>
    {2.0} <music21.note.Note A>
    {4.0} <music21.bar.Barline type=final>
    ```

    ```python
    >>> streamObj.highestTime
    4.0
    ```

CapellaImporter.systemFromSystem(*systemElement*, *systemObj=None*)[[source]](../_modules/music21/capella/fromCapellaXML.html#CapellaImporter.systemFromSystem)
:   returns a `System` object from a <system> tag.
    The System object will contain `Part` objects
    which will have the notes, etc. contained in it.

    TODO: Handle multiple <voices>

CapellaImporter.systemScoreFromScore(*scoreElement*, *scoreObj=None*)[[source]](../_modules/music21/capella/fromCapellaXML.html#CapellaImporter.systemScoreFromScore)
:   returns an `Score` object from a <score> tag.

    The Score object is not a standard music21 Score object which contains
    parts, then measures, then voices, but instead contains systems which
    optionally contain voices, which contain parts. No measures have yet
    been created.

CapellaImporter.tieFromTie(*tieElement*)[[source]](../_modules/music21/capella/fromCapellaXML.html#CapellaImporter.tieFromTie)
:   returns a [`Tie`](moduleTie.html#music21.tie.Tie "music21.tie.Tie") element from a <tie> tag

    if begin == ‘true’ then Tie.type = start

    ```python
    >>> ci = capella.fromCapellaXML.CapellaImporter()
    >>> tieEl = ci.domElementFromText('<tie begin="true"/>')
    >>> ci.tieFromTie(tieEl)
    <music21.tie.Tie start>
    ```

    if end == ‘true’ then Tie.type = stop

    ```python
    >>> tieEl = ci.domElementFromText('<tie end="true"/>')
    >>> ci.tieFromTie(tieEl)
    <music21.tie.Tie stop>
    ```

    if begin == ‘true’ and end == ‘true’ then Tie.type = continue (is this right???)

    ```python
    >>> tieEl = ci.domElementFromText('<tie begin="true" end="true"/>')
    >>> ci.tieFromTie(tieEl)
    <music21.tie.Tie continue>
    ```

CapellaImporter.timeSignatureFromTimeSign(*timeSign*)[[source]](../_modules/music21/capella/fromCapellaXML.html#CapellaImporter.timeSignatureFromTimeSign)
:   Returns a `TimeSignature` object from a timeSign tag.

    ```python
    >>> ci = capella.fromCapellaXML.CapellaImporter()
    >>> timeSign = ci.domElementFromText('<timeSign time="4/4"/>')
    >>> ci.timeSignatureFromTimeSign(timeSign)
    <music21.meter.TimeSignature 4/4>
    ```

    ```python
    >>> timeSign = ci.domElementFromText('<timeSign time="infinite"/>')
    >>> ci.timeSignatureFromTimeSign(timeSign) is None
    True
    ```

CapellaImporter.tupletFromTuplet(*tupletElement*)[[source]](../_modules/music21/capella/fromCapellaXML.html#CapellaImporter.tupletFromTuplet)
:   Returns a [`Tuplet`](moduleDuration.html#music21.duration.Tuplet "music21.duration.Tuplet") object from a <tuplet> tag.

    ```python
    >>> ci = capella.fromCapellaXML.CapellaImporter()
    >>> tupletTag = ci.domElementFromText('<tuplet count="3"/>')
    >>> ci.tupletFromTuplet(tupletTag)
    <music21.duration.Tuplet 3/2>
    ```

    does not handle ‘tripartite’ = True
