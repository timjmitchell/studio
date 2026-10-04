Source: https://music21.org/music21docs/moduleReference/moduleMusicxmlM21ToXml.html

# music21.musicxml.m21ToXml

Converters for music21 objects to musicxml using ElementTree

## GeneralObjectExporter

class music21.musicxml.m21ToXml.GeneralObjectExporter(*obj: [ProtoM21Object](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](../_modules/music21/musicxml/m21ToXml.html#GeneralObjectExporter)
:   Packs any Music21Object into a well-formed score and exports
    a bytes object MusicXML representation.

[`GeneralObjectExporter`](#music21.musicxml.m21ToXml.GeneralObjectExporter "music21.musicxml.m21ToXml.GeneralObjectExporter") methods

GeneralObjectExporter.fromDiatonicScale(*diatonicScaleObject*)[[source]](../_modules/music21/musicxml/m21ToXml.html#GeneralObjectExporter.fromDiatonicScale)
:   Return a complete musicxml of the DiatonicScale

    Overrides the general scale behavior to highlight
    the tonic and dominant.

    ```python
    >>> cMaj = scale.MajorScale('C')
    >>> GEX = musicxml.m21ToXml.GeneralObjectExporter()
    >>> m = GEX.fromDiatonicScale(cMaj)
    >>> m
    <music21.stream.Score 0x11d4f17b8>
    ```

    ```python
    >>> m.show('text')
    {0.0} <music21.stream.Part 0x116a04b38>
        {0.0} <music21.stream.Measure 1 offset=0.0>
            {0.0} <music21.clef.TrebleClef>
            {0.0} <music21.meter.TimeSignature 11/4>
            {0.0} <music21.note.Note C>
            {4.0} <music21.note.Note D>
            {5.0} <music21.note.Note E>
            {6.0} <music21.note.Note F>
            {7.0} <music21.note.Note G>
            {9.0} <music21.note.Note A>
            {10.0} <music21.note.Note B>
    ```

GeneralObjectExporter.fromDuration(*d*)[[source]](../_modules/music21/musicxml/m21ToXml.html#GeneralObjectExporter.fromDuration)
:   Translate a music21 [`Duration`](moduleDuration.html#music21.duration.Duration "music21.duration.Duration") into
    a complete MusicXML representation.

    Rarely, rarely used. Only if you call .show() on a duration object

GeneralObjectExporter.fromDynamic(*dynamicObject*)[[source]](../_modules/music21/musicxml/m21ToXml.html#GeneralObjectExporter.fromDynamic)
:   Provide a complete MusicXML string from a single dynamic by
    putting it into a Stream first.

GeneralObjectExporter.fromGeneralNote(*n*)[[source]](../_modules/music21/musicxml/m21ToXml.html#GeneralObjectExporter.fromGeneralNote)
:   Translate a music21 [`Note`](moduleNote.html#music21.note.Note "music21.note.Note") into an object
    ready to be parsed.

    An attempt is made to find the best TimeSignature for quarterLengths
    <= 6:

    ```python
    >>> n = note.Note('c3')
    >>> n.quarterLength = 3
    >>> GEX = musicxml.m21ToXml.GeneralObjectExporter()
    >>> sc = GEX.fromGeneralNote(n)
    >>> sc.show('t')
    {0.0} <music21.stream.Part 0x1046afa90>
        {0.0} <music21.stream.Measure 1 offset=0.0>
            {0.0} <music21.clef.BassClef>
            {0.0} <music21.meter.TimeSignature 6/8>
            {0.0} <music21.note.Note C>
            {3.0} <music21.bar.Barline type=final>
    ```

    But longer notes will be broken into tied components placed in
    4/4 measures:

    ```python
    >>> long_note = note.Note('e5', quarterLength=40)
    >>> GEX = musicxml.m21ToXml.GeneralObjectExporter()
    >>> sc = GEX.fromGeneralNote(long_note)
    >>> sc[meter.TimeSignature].first()
    <music21.meter.TimeSignature 4/4>
    >>> len(sc[stream.Measure])
    10
    ```

GeneralObjectExporter.fromGeneralObject(*obj: [ProtoM21Object](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")*)[[source]](../_modules/music21/musicxml/m21ToXml.html#GeneralObjectExporter.fromGeneralObject)
:   Converts any Music21Object (or a duration or a pitch) to something that
    can be passed to [`ScoreExporter`](#music21.musicxml.m21ToXml.ScoreExporter "music21.musicxml.m21ToXml.ScoreExporter").

    ```python
    >>> GEX = musicxml.m21ToXml.GeneralObjectExporter()
    >>> s = GEX.fromGeneralObject(duration.Duration(3.0))
    >>> s
    <music21.stream.Score 0x...>
    >>> s.show('t')
    {0.0} <music21.stream.Part 0x...>
        {0.0} <music21.stream.Measure 1 offset=0.0>
            {0.0} <music21.clef.TrebleClef>
            {0.0} <music21.meter.TimeSignature 6/8>
            {0.0} <music21.note.Note C>
            {3.0} <music21.bar.Barline type=final>
    >>> s[note.NotRest].first().duration
    <music21.duration.Duration 3.0>
    ```

    * Changed in v8: fills gaps with rests before calling makeNotation
      to avoid duplicating effort with [`PartExporter.fixupNotationMeasured()`](#music21.musicxml.m21ToXml.PartExporter.fixupNotationMeasured "music21.musicxml.m21ToXml.PartExporter.fixupNotationMeasured").

    ```python
    >>> v = stream.Voice(note.Note())
    >>> m = stream.Measure([meter.TimeSignature(), v])
    >>> GEX = musicxml.m21ToXml.GeneralObjectExporter(m)
    >>> out = GEX.parse()  # out is bytes
    >>> outStr = out.decode('utf-8')  # now is string
    >>> '<note print-object="no" print-spacing="yes">' in outStr
    True
    >>> len(v[note.Rest])  # original stream unchanged
    0
    ```

GeneralObjectExporter.fromMeasure(*m*)[[source]](../_modules/music21/musicxml/m21ToXml.html#GeneralObjectExporter.fromMeasure)
:   Translate a music21 Measure into a
    complete MusicXML string representation.

    Note: this method is called for complete MusicXML
    representation of a Measure, not for partial
    solutions in Part or Stream production.

GeneralObjectExporter.fromMusic21Object(*obj*)[[source]](../_modules/music21/musicxml/m21ToXml.html#GeneralObjectExporter.fromMusic21Object)
:   return a single TimeSignature as a musicxml document

GeneralObjectExporter.fromPart(*p*)[[source]](../_modules/music21/musicxml/m21ToXml.html#GeneralObjectExporter.fromPart)
:   From a part, put it in a new score.

GeneralObjectExporter.fromPitch(*p: [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")*)[[source]](../_modules/music21/musicxml/m21ToXml.html#GeneralObjectExporter.fromPitch)
:   Translate a music21 [`Pitch`](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") into an object
    ready to be parsed.

    ```python
    >>> p = pitch.Pitch('c#3')
    >>> GEX = musicxml.m21ToXml.GeneralObjectExporter()
    >>> sc = GEX.fromPitch(p)
    >>> sc.show('t')
    {0.0} <music21.stream.Part 0x1046afa90>
        {0.0} <music21.stream.Measure 1 offset=0.0>
            {0.0} <music21.clef.BassClef>
            {0.0} <music21.meter.TimeSignature 1/4>
            {0.0} <music21.note.Note C#>
    ```

GeneralObjectExporter.fromScale(*scaleObject*)[[source]](../_modules/music21/musicxml/m21ToXml.html#GeneralObjectExporter.fromScale)
:   Generate the pitches from this scale
    and put it into a stream.Measure, then call
    fromMeasure on it.

    ```python
    >>> cMaj = scale.MajorScale('C')
    >>> GEX = musicxml.m21ToXml.GeneralObjectExporter()
    >>> m = GEX.fromScale(cMaj)
    >>> m
    <music21.stream.Score 0x11d4f17b8>
    ```

    ```python
    >>> m.show('text')
    {0.0} <music21.stream.Part 0x116a04b38>
        {0.0} <music21.stream.Measure 1 offset=0.0>
            {0.0} <music21.clef.TrebleClef>
            {0.0} <music21.meter.TimeSignature 10/4>
            {0.0} <music21.note.Note C>
            {4.0} <music21.note.Note D>
            {5.0} <music21.note.Note E>
            {6.0} <music21.note.Note F>
            {7.0} <music21.note.Note G>
            {8.0} <music21.note.Note A>
            {9.0} <music21.note.Note B>
    ```

GeneralObjectExporter.fromScore(*sc*)[[source]](../_modules/music21/musicxml/m21ToXml.html#GeneralObjectExporter.fromScore)
:   Runs `makeNotation()` on the copy.

GeneralObjectExporter.fromStream(*st*)[[source]](../_modules/music21/musicxml/m21ToXml.html#GeneralObjectExporter.fromStream)

GeneralObjectExporter.fromVoice(*v*)[[source]](../_modules/music21/musicxml/m21ToXml.html#GeneralObjectExporter.fromVoice)

GeneralObjectExporter.parse(*obj: [ProtoM21Object](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")[[source]](../_modules/music21/musicxml/m21ToXml.html#GeneralObjectExporter.parse)
:   Return a bytes object representation of anything from a
    Score to a single pitch.

    When `makeNotation` is True (default), wraps obj in a well-formed
    Score, makes a copy, and runs [`makeNotation()`](moduleStreamBase.html#music21.stream.base.Stream.makeNotation "music21.stream.base.Stream.makeNotation")
    on each of the parts. To skip copying and making notation, set .makeNotation
    on this instance to False.

    ```python
    >>> p = pitch.Pitch('D#4')
    >>> GEX = musicxml.m21ToXml.GeneralObjectExporter(p)
    >>> out = GEX.parse()  # out is bytes
    >>> outStr = out.decode('utf-8')  # now is string
    >>> print(outStr.strip())
    <?xml version="1.0" encoding="utf-8"?>
    <!DOCTYPE score-partwise
      PUBLIC "-//Recordare//DTD MusicXML ... Partwise//EN"
      "http://www.musicxml.org/dtds/partwise.dtd">
    <score-partwise version="...">
      <movement-title>Music21 Fragment</movement-title>
      <identification>
        <creator type="composer">Music21</creator>
        <encoding>
          <encoding-date>...</encoding-date>
          <software>music21 v...</software>
          <supports element="beam" type="yes" />
          <supports element="stem" type="yes" />
          <supports element="accidental" type="yes" />
        </encoding>
      </identification>
      <defaults>
        <scaling>
          <millimeters>7</millimeters>
          <tenths>40</tenths>
        </scaling>
      </defaults>
      <part-list>
        <score-part id="...">
          <part-name />
        </score-part>
      </part-list>
      <!--=========================== Part 1 ===========================-->
      <part id="...">
        <!--========================= Measure 1 ==========================-->
        <measure implicit="no" number="1">
          <attributes>
            <divisions>10080</divisions>
            <time>
              <beats>1</beats>
              <beat-type>4</beat-type>
            </time>
            <clef>
              <sign>G</sign>
              <line>2</line>
            </clef>
          </attributes>
          <note>
            <pitch>
              <step>D</step>
              <alter>1</alter>
              <octave>4</octave>
            </pitch>
            <duration>10080</duration>
            <type>quarter</type>
            <accidental>sharp</accidental>
          </note>
        </measure>
      </part>
    </score-partwise>
    ```

GeneralObjectExporter.parseWellformedObject(*sc: [Score](moduleStreamBase.html#music21.stream.base.Score "music21.stream.base.Score")*) → [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")[[source]](../_modules/music21/musicxml/m21ToXml.html#GeneralObjectExporter.parseWellformedObject)
:   Parse an object that has already gone through the
    .fromGeneralObject conversion, which has produced a copy with
    `makeNotation()` run on it
    (unless `makeNotation` is False).

    Returns bytes.

## MeasureExporter

class music21.musicxml.m21ToXml.MeasureExporter(*measureObj: [Measure](moduleStreamBase.html#music21.stream.base.Measure "music21.stream.base.Measure") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *parent: [PartExporter](#music21.musicxml.m21ToXml.PartExporter "music21.musicxml.m21ToXml.PartExporter") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](../_modules/music21/musicxml/m21ToXml.html#MeasureExporter)

[`MeasureExporter`](#music21.musicxml.m21ToXml.MeasureExporter "music21.musicxml.m21ToXml.MeasureExporter") bases

* [`XMLExporterBase`](#music21.musicxml.m21ToXml.XMLExporterBase "music21.musicxml.m21ToXml.XMLExporterBase")

[`MeasureExporter`](#music21.musicxml.m21ToXml.MeasureExporter "music21.musicxml.m21ToXml.MeasureExporter") methods

MeasureExporter.appendArpeggioMarkSpannersToNotations(*obj: [Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")*, *noteIndexInChord: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *notations: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")]*, *sb: [SpannerBundle](moduleSpanner.html#music21.spanner.SpannerBundle "music21.spanner.SpannerBundle")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/musicxml/m21ToXml.html#MeasureExporter.appendArpeggioMarkSpannersToNotations)

MeasureExporter.arpeggioMarkToMxExpression(*arpeggioMark*, *chordOrNote*, *noteIndexInChord*)[[source]](../_modules/music21/musicxml/m21ToXml.html#MeasureExporter.arpeggioMarkToMxExpression)

MeasureExporter.articulationToXmlArticulation(*articulationMark: [Articulation](moduleArticulations.html#music21.articulations.Articulation "music21.articulations.Articulation")*) → [Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")[[source]](../_modules/music21/musicxml/m21ToXml.html#MeasureExporter.articulationToXmlArticulation)
:   Returns a class (mxArticulationMark) that represents the
    MusicXML structure of an articulation mark.

    ```python
    >>> a = articulations.Accent()
    >>> a.placement = 'below'
    ```

    ```python
    >>> MEX = musicxml.m21ToXml.MeasureExporter()
    >>> mxArticulationMark = MEX.articulationToXmlArticulation(a)
    >>> MEX.dump(mxArticulationMark)
    <accent placement="below" />
    ```

    ```python
    >>> a = articulations.Staccatissimo()
    >>> a.placement = 'below'
    ```

    ```python
    >>> mxArticulationMark = MEX.articulationToXmlArticulation(a)
    >>> MEX.dump(mxArticulationMark)
    <staccatissimo placement="below" />
    ```

    Articulations can have style attached to them:

    ```python
    >>> a = articulations.Doit()
    >>> a.style.lineShape = 'curved'
    >>> a.style.lineType = 'dashed'
    >>> a.style.dashLength = 2
    >>> a.style.spaceLength = 1
    >>> a.style.absoluteX = 5
    >>> a.style.absoluteY = 2
    ```

    ```python
    >>> mxArticulationMark = MEX.articulationToXmlArticulation(a)
    >>> MEX.dump(mxArticulationMark)
    <doit dash-length="2" default-x="5" default-y="2"
        line-shape="curved" line-type="dashed" space-length="1" />
    ```

MeasureExporter.articulationToXmlTechnical(*articulationMark: [Articulation](moduleArticulations.html#music21.articulations.Articulation "music21.articulations.Articulation")*)[[source]](../_modules/music21/musicxml/m21ToXml.html#MeasureExporter.articulationToXmlTechnical)
:   Returns a tag that represents the
    MusicXML structure of an articulation mark that is primarily a TechnicalIndication.

    ```python
    >>> MEX = musicxml.m21ToXml.MeasureExporter()
    ```

    ```python
    >>> a = articulations.UpBow()
    >>> a.placement = 'below'
    ```

    ```python
    >>> mxTechnicalMark = MEX.articulationToXmlTechnical(a)
    >>> MEX.dump(mxTechnicalMark)
    <up-bow placement="below" />
    ```

    ```python
    >>> f = articulations.Fingering(4)
    >>> f.substitution = True
    >>> mxFingering = MEX.articulationToXmlTechnical(f)
    >>> MEX.dump(mxFingering)
    <fingering alternate="no" substitution="yes">4</fingering>
    ```

    Technical marks too specific to express in musicxml just get other-technical.

    ```python
    >>> g = articulations.OrganIndication()
    >>> g.displayText = 'unda maris'
    >>> mxOther = MEX.articulationToXmlTechnical(g)
    >>> MEX.dump(mxOther)
    <other-technical>unda maris</other-technical>
    ```

    Same with technical marks not yet supported.
    TODO: support HammerOn, PullOff, Hole, Arrow.

    ```python
    >>> h = articulations.HammerOn()
    >>> mxOther = MEX.articulationToXmlTechnical(h)
    >>> MEX.dump(mxOther)
    <other-technical />
    ```

MeasureExporter.barlineToXml(*barObject*)[[source]](../_modules/music21/musicxml/m21ToXml.html#MeasureExporter.barlineToXml)
:   Translate a music21 bar.Bar object to an mxBar
    while making two substitutions: double -> light-light
    and final -> light-heavy as shown below.

    ```python
    >>> b = bar.Barline('final')
    >>> MEX = musicxml.m21ToXml.MeasureExporter()
    >>> mxBarline = MEX.barlineToXml(b)
    >>> MEX.dump(mxBarline)
    <barline>
      <bar-style>light-heavy</bar-style>
    </barline>
    ```

    ```python
    >>> b.location = 'right'
    >>> mxBarline = MEX.barlineToXml(b)
    >>> MEX.dump(mxBarline)
    <barline location="right">
      <bar-style>light-heavy</bar-style>
    </barline>
    ```

MeasureExporter.beamToXml(*beamObject*)[[source]](../_modules/music21/musicxml/m21ToXml.html#MeasureExporter.beamToXml)
:   Returns an ElementTree Element from a [`Beam`](moduleBeam.html#music21.beam.Beam "music21.beam.Beam") object

    ```python
    >>> a = beam.Beam()
    >>> a.type = 'start'
    >>> a.number = 1
    ```

    ```python
    >>> MEX = musicxml.m21ToXml.MeasureExporter()
    >>> b = MEX.beamToXml(a)
    >>> b
    <Element 'beam' at 0x104f3a728>
    >>> MEX.dump(b)
    <beam number="1">begin</beam>
    ```

    ```python
    >>> a.type = 'continue'
    >>> b = MEX.beamToXml(a)
    >>> MEX.dump(b)
    <beam number="1">continue</beam>
    ```

    ```python
    >>> a.type = 'stop'
    >>> b = MEX.beamToXml(a)
    >>> MEX.dump(b)
    <beam number="1">end</beam>
    ```

    ```python
    >>> a.type = 'partial'
    >>> a.direction = 'left'
    >>> b = MEX.beamToXml(a)
    >>> MEX.dump(b)
    <beam number="1">backward hook</beam>
    ```

    ```python
    >>> a.direction = 'right'
    >>> a.id = 'beam1'
    >>> b = MEX.beamToXml(a)
    >>> MEX.dump(b)
    <beam id="beam1" number="1">forward hook</beam>
    ```

    ```python
    >>> a.direction = None
    >>> b = MEX.beamToXml(a)
    Traceback (most recent call last):
    music21.musicxml.xmlObjects.MusicXMLExportException: partial beam defined
        without a proper direction set (set to None)
    ```

    ```python
    >>> a.type = 'crazy'
    >>> b = MEX.beamToXml(a)
    Traceback (most recent call last):
    music21.musicxml.xmlObjects.MusicXMLExportException: unexpected beam type
        encountered (crazy)
    ```

MeasureExporter.beamsToXml(*beams*)[[source]](../_modules/music21/musicxml/m21ToXml.html#MeasureExporter.beamsToXml)
:   Returns a list of <beam> tags
    from a [`Beams`](moduleBeam.html#music21.beam.Beams "music21.beam.Beams") object

    ```python
    >>> a = beam.Beams()
    >>> a.fill(2, type='start')
    ```

    ```python
    >>> MEX = musicxml.m21ToXml.MeasureExporter()
    >>> mxBeamList = MEX.beamsToXml(a)
    >>> len(mxBeamList)
    2
    >>> for b in mxBeamList:
    ...     MEX.dump(b)
    <beam number="1">begin</beam>
    <beam number="2">begin</beam>
    ```

MeasureExporter.chordSymbolToXml(*cs: [ChordSymbol](moduleHarmony.html#music21.harmony.ChordSymbol "music21.harmony.ChordSymbol")*, *\**, *append: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*) → [Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)") | [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")][[source]](../_modules/music21/musicxml/m21ToXml.html#MeasureExporter.chordSymbolToXml)
:   Convert a ChordSymbol object to either a chord (if .writeAsChord is True)
    or a Harmony XML Element.

    ```python
    >>> cs = harmony.ChordSymbol()
    >>> cs.root('E-')
    >>> cs.bass('B-', allow_add=True)
    >>> cs.inversion(2, transposeOnSet=False)
    >>> cs.chordKind = 'major'
    >>> cs.chordKindStr = 'M'
    >>> cs
    <music21.harmony.ChordSymbol E-/B->
    ```

    ```python
    >>> MEX = musicxml.m21ToXml.MeasureExporter()
    >>> MEX.currentDivisions = 10
    ```

    ```python
    >>> mxHarmony = MEX.chordSymbolToXml(cs)
    >>> MEX.dump(mxHarmony)
    <harmony>
      <root>
        <root-step>E</root-step>
        <root-alter>-1</root-alter>
      </root>
      <kind text="M">major</kind>
      <inversion>2</inversion>
      <bass>
        <bass-step>B</bass-step>
        <bass-alter>-1</bass-alter>
      </bass>
    </harmony>
    ```

    Now give function:

    ```python
    >>> cs.romanNumeral = 'I64'
    >>> mxHarmony = MEX.chordSymbolToXml(cs)
    >>> MEX.dump(mxHarmony)
    <harmony>
      <function>I64</function>
      <kind text="M">major</kind>
      <inversion>2</inversion>
      <bass>
        <bass-step>B</bass-step>
        <bass-alter>-1</bass-alter>
      </bass>
    </harmony>
    ```

    ```python
    >>> hd = harmony.ChordStepModification()
    >>> hd.modType = 'alter'
    >>> hd.interval = -1
    >>> hd.degree = 3
    >>> cs.addChordStepModification(hd)
    ```

    ```python
    >>> mxHarmony = MEX.chordSymbolToXml(cs)
    >>> MEX.dump(mxHarmony)
    <harmony>
      <function>I64</function>
      <kind text="M">major</kind>
      <inversion>2</inversion>
      <bass>
        <bass-step>B</bass-step>
        <bass-alter>-1</bass-alter>
      </bass>
      <degree>
        <degree-value>3</degree-value>
        <degree-alter>-1</degree-alter>
        <degree-type>alter</degree-type>
      </degree>
    </harmony>
    ```

    Test altered chords:

    ```python
    >>> f = harmony.ChordSymbol('F sus add 9')
    >>> f
    <music21.harmony.ChordSymbol F sus add 9>
    >>> mxHarmony = MEX.chordSymbolToXml(f)
    >>> MEX.dump(mxHarmony)
    <harmony>
      <root>
        <root-step>F</root-step>
      </root>
      <kind>suspended-fourth</kind>
      <degree>
        <degree-value>9</degree-value>
        <degree-alter>0</degree-alter>
        <degree-type>add</degree-type>
      </degree>
    </harmony>
    ```

    MusicXML uses “dominant” for “dominant-seventh” so check aliases back…

    ```python
    >>> dom7 = harmony.ChordSymbol('C7')
    >>> dom7.chordKind
    'dominant-seventh'
    >>> mxHarmony = MEX.chordSymbolToXml(dom7)
    >>> MEX.dump(mxHarmony)
    <harmony>
      <root>
        <root-step>C</root-step>
      </root>
      <kind>dominant</kind>
    </harmony>
    ```

    set writeAsChord to not get a symbol, but the notes. Will return a list of notes.

    ```python
    >>> dom7.writeAsChord = True
    >>> harmonyList = MEX.chordSymbolToXml(dom7)
    >>> len(harmonyList)
    4
    >>> MEX.dump(harmonyList[0])
    <note>
      <pitch>
        <step>C</step>
        <octave>3</octave>
      </pitch>
      <duration>10</duration>
      <type>quarter</type>
    </note>
    ```

MeasureExporter.chordToXml(*c: [ChordBase](moduleChord.html#music21.chord.ChordBase "music21.chord.ChordBase")*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")][[source]](../_modules/music21/musicxml/m21ToXml.html#MeasureExporter.chordToXml)
:   Returns a list of <note> tags, all but the first with a <chord/> tag on them.
    And appends them to self.xmlRoot

    Attributes of notes are merged from different locations: first from the
    duration objects, then from the pitch objects. Finally, GeneralNote
    attributes are added.

    ```python
    >>> ch = chord.Chord()
    >>> ch.quarterLength = 2
    >>> b = pitch.Pitch('A-2')
    >>> c = pitch.Pitch('D3')
    >>> d = pitch.Pitch('E4')
    >>> e = [b, c, d]
    >>> ch.pitches = e
    ```

    ```python
    >>> len(ch.pitches)
    3
    >>> MEX = musicxml.m21ToXml.MeasureExporter()
    >>> len(MEX.xmlRoot)
    0
    >>> mxNoteList = MEX.chordToXml(ch)
    >>> len(mxNoteList)  # get three mxNotes
    3
    >>> len(MEX.xmlRoot)
    3
    ```

    ```python
    >>> MEX.dump(mxNoteList[0])
    <note>
      <pitch>
        <step>A</step>
        <alter>-1</alter>
        <octave>2</octave>
      </pitch>
      <duration>20160</duration>
      <type>half</type>
      <accidental>flat</accidental>
    </note>
    ```

    ```python
    >>> MEX.dump(mxNoteList[1])
    <note>
      <chord />
      <pitch>
        <step>D</step>
        <octave>3</octave>
      </pitch>
      <duration>20160</duration>
      <type>half</type>
    </note>
    ```

    ```python
    >>> MEX.dump(mxNoteList[2])
    <note>
      <chord />
      <pitch>
        <step>E</step>
        <octave>4</octave>
      </pitch>
      <duration>20160</duration>
      <type>half</type>
    </note>
    ```

    Test that notehead and style translation works:

    ```python
    >>> g = pitch.Pitch('g3')
    >>> h = note.Note('b4')
    >>> h.notehead = 'diamond'
    >>> h.style.color = 'gold'
    >>> h.style.absoluteX = 176
    >>> ch2 = chord.Chord([g, h])
    >>> ch2.quarterLength = 2.0
    >>> mxNoteList = MEX.chordToXml(ch2)
    >>> MEX.dump(mxNoteList[1])
    <note color="#FFD700" default-x="176">
      <chord />
      <pitch>
        <step>B</step>
        <octave>4</octave>
      </pitch>
      <duration>20160</duration>
      <type>half</type>
      <notehead color="#FFD700" parentheses="no">diamond</notehead>
    </note>
    ```

    And unpitched chord members:

    ```python
    >>> perc = percussion.PercussionChord([note.Unpitched(), note.Unpitched()])
    >>> for n in MEX.chordToXml(perc):
    ...     MEX.dump(n)
    <note>
      <unpitched>
        <display-step>B</display-step>
        <display-octave>4</display-octave>
      </unpitched>
      <duration>10080</duration>
      <type>quarter</type>
    </note>
    <note>
      <chord />
      <unpitched>
        <display-step>B</display-step>
        <display-octave>4</display-octave>
      </unpitched>
      <duration>10080</duration>
      <type>quarter</type>
    </note>
    ```

    Test articulations of chords with fingerings. Superfluous fingerings will be ignored.

    ```python
    >>> testChord = chord.Chord('E4 C5')
    >>> testChord.articulations = [articulations.Fingering(1),
    ...        articulations.Accent(), articulations.Fingering(5), articulations.Fingering(3)]
    >>> for n in MEX.chordToXml(testChord):
    ...     MEX.dump(n)
    <note>
      ...
      <notations>
        <articulations>
          <accent />
        </articulations>
        <technical>
          <fingering alternate="no" substitution="no">1</fingering>
        </technical>
      </notations>
    </note>
    <note>
      <chord />
      ...
      <notations>
        <technical>
          <fingering alternate="no" substitution="no">5</fingering>
        </technical>
      </notations>
    </note>
    ```

MeasureExporter.chordWithFretBoardToXml(*cwf: [tablature.ChordWithFretBoard](moduleTablature.html#music21.tablature.ChordWithFretBoard "music21.tablature.ChordWithFretBoard")*) → Element[[source]](../_modules/music21/musicxml/m21ToXml.html#MeasureExporter.chordWithFretBoardToXml)
:   Deals with both chords and frets.
    Generate harmony and append xml to it.

MeasureExporter.clefToXml(*clefObj*)[[source]](../_modules/music21/musicxml/m21ToXml.html#MeasureExporter.clefToXml)
:   Given a music21 Clef object, return a MusicXML clef
    tag.

    ```python
    >>> gc = clef.GClef()
    >>> gc
    <music21.clef.GClef>
    >>> MEX = musicxml.m21ToXml.MeasureExporter()
    >>> mxc = MEX.clefToXml(gc)
    >>> MEX.dump(mxc)
    <clef>
      <sign>G</sign>
    </clef>
    ```

    ```python
    >>> b = clef.Treble8vbClef()
    >>> b.octaveChange
    -1
    >>> mxc2 = MEX.clefToXml(b)
    >>> MEX.dump(mxc2)
    <clef>
      <sign>G</sign>
      <line>2</line>
      <clef-octave-change>-1</clef-octave-change>
    </clef>
    ```

    ```python
    >>> pc = clef.PercussionClef()
    >>> mxc3 = MEX.clefToXml(pc)
    >>> MEX.dump(mxc3)
    <clef>
      <sign>percussion</sign>
    </clef>
    ```

    Clefs without signs get exported as G clefs with a warning

    ```python
    >>> generic = clef.Clef()
    >>> mxc4 = MEX.clefToXml(generic)
    Clef with no .sign exported; setting as a G clef
    >>> MEX.dump(mxc4)
    <clef>
      <sign>G</sign>
    </clef>
    ```

MeasureExporter.codaToXml(*coda: [Coda](moduleRepeat.html#music21.repeat.Coda "music21.repeat.Coda")*) → [Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")[[source]](../_modules/music21/musicxml/m21ToXml.html#MeasureExporter.codaToXml)
:   returns a coda inside a direction-type inside a direction IF coda.useSymbol is
    True; otherwise returns a TextExpression and appends to score:

    ```python
    >>> c = repeat.Coda()
    >>> MEX = musicxml.m21ToXml.MeasureExporter()
    >>> mxCodaDir = MEX.codaToXml(c)
    >>> MEX.dump(mxCodaDir)
    <direction>
      <direction-type>
        <coda default-y="20" />
      </direction-type>
    </direction>
    ```

    turn coda.useSymbol to False to get a text expression instead,
    and set enclosure to NO\_ENCLOSURE to explicitly generate
    enclosure=”none”.

    ```python
    >>> c.useSymbol = False
    >>> c.style.enclosure = style.Enclosure.NO_ENCLOSURE
    >>> MEX = musicxml.m21ToXml.MeasureExporter()
    >>> mxCodaText = MEX.codaToXml(c)
    >>> MEX.dump(mxCodaText)
    <direction>
      <direction-type>
        <words default-y="20" enclosure="none"
            justify="center">Coda</words>
      </direction-type>
    </direction>
    ```

MeasureExporter.dealWithNotehead(*mxNote: [Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")*, *n: [GeneralNote](moduleNote.html#music21.note.GeneralNote "music21.note.GeneralNote")*, *chordParent: [Chord](moduleChord.html#music21.chord.Chord "music21.chord.Chord") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/musicxml/m21ToXml.html#MeasureExporter.dealWithNotehead)
:   Determine if an <notehead> element needs to be added to this <note>
    element (mxNote) and if it does then get the <notehead> element from
    noteheadToXml and add it to mxNote.

    Complicated because the chordParent might have notehead
    set, which would affect every note along the way.

    Returns nothing. The mxNote is modified in place.

MeasureExporter.durationXml(*dur: [Duration](moduleDuration.html#music21.duration.Duration "music21.duration.Duration")*)[[source]](../_modules/music21/musicxml/m21ToXml.html#MeasureExporter.durationXml)
:   Convert a duration.Duration object to a <duration> tag using self.currentDivisions

    ```python
    >>> d = duration.Duration(1.5)
    >>> MEX = musicxml.m21ToXml.MeasureExporter()
    >>> MEX.currentDivisions = 10
    >>> mxDuration = MEX.durationXml(d)
    >>> MEX.dump(mxDuration)
    <duration>15</duration>
    ```

MeasureExporter.dynamicToXml(*d: [Dynamic](moduleDynamics.html#music21.dynamics.Dynamic "music21.dynamics.Dynamic")*) → [Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")[[source]](../_modules/music21/musicxml/m21ToXml.html#MeasureExporter.dynamicToXml)
:   return a nested tag:
    <direction><direction-type><dynamic><ff>
    or whatever:

    ```python
    >>> ppp = dynamics.Dynamic('ppp')
    >>> print(f'{ppp.volumeScalar:.2f}')
    0.15
    >>> ppp.style.relativeY = -10
    ```

    ```python
    >>> MEX = musicxml.m21ToXml.MeasureExporter()
    >>> mxDirection = MEX.dynamicToXml(ppp)
    >>> MEX.dump(mxDirection)
    <direction>
      <direction-type>
        <dynamics default-x="-36" default-y="-80" relative-y="-10">
          <ppp />
        </dynamics>
      </direction-type>
      <sound dynamics="19" />
    </direction>
    ```

    appends to score.

    Now with offset not zero.

    ```python
    >>> MEX = musicxml.m21ToXml.MeasureExporter()
    >>> ppp.offset = 1.0
    >>> mxDirection = MEX.dynamicToXml(ppp)
    >>> MEX.dump(mxDirection)
    <direction>
      <direction-type>
        <dynamics default-x="-36" default-y="-80" relative-y="-10">
          <ppp />
        </dynamics>
      </direction-type>
      <offset sound="yes">10080</offset>
      <sound dynamics="19" />
    </direction>
    ```

MeasureExporter.expressionToXml(*expression: [Expression](moduleExpressions.html#music21.expressions.Expression "music21.expressions.Expression")*) → [Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")[[source]](../_modules/music21/musicxml/m21ToXml.html#MeasureExporter.expressionToXml)
:   Convert a music21 Expression (expression or ornament)
    to a musicxml tag;
    return None if no conversion is possible.

    Expressions apply only to the first note of chord.

    ```python
    >>> invTurn = expressions.InvertedTurn()
    >>> MEX = musicxml.m21ToXml.MeasureExporter()
    >>> mxExpression = MEX.expressionToXml(invTurn)
    >>> MEX.dump(mxExpression)
    <inverted-turn placement="above" />
    ```

    ```python
    >>> invDelayedTurn = expressions.InvertedTurn(delay=1.0)
    >>> invDelayedTurn.placement = 'below'
    >>> MEX = musicxml.m21ToXml.MeasureExporter()
    >>> mxExpression = MEX.expressionToXml(invDelayedTurn)
    >>> MEX.dump(mxExpression)
    <delayed-inverted-turn placement="below" />
    ```

    Some special types:

    ```python
    >>> f = expressions.Fermata()
    >>> MEX = musicxml.m21ToXml.MeasureExporter()
    >>> mxExpression = MEX.expressionToXml(f)
    >>> MEX.dump(mxExpression)
    <fermata type="inverted" />
    >>> f.shape = 'angled'
    >>> mxExpression = MEX.expressionToXml(f)
    >>> MEX.dump(mxExpression)
    <fermata type="inverted">angled</fermata>
    ```

    ```python
    >>> trem = expressions.Tremolo()
    >>> trem.numberOfMarks = 4
    >>> MEX = musicxml.m21ToXml.MeasureExporter()
    >>> mxExpression = MEX.expressionToXml(trem)
    >>> MEX.dump(mxExpression)
    <tremolo type="single">4</tremolo>
    ```

    ```python
    >>> arp = expressions.ArpeggioMark()
    >>> MEX = musicxml.m21ToXml.MeasureExporter()
    >>> mxExpression = MEX.expressionToXml(arp)
    >>> MEX.dump(mxExpression)
    <arpeggiate />
    >>> arp.type = 'down'
    >>> mxExpression = MEX.expressionToXml(arp)
    >>> MEX.dump(mxExpression)
    <arpeggiate direction="down" />
    ```

    ```python
    >>> nonArp = expressions.ArpeggioMark('non-arpeggio')
    >>> MEX = musicxml.m21ToXml.MeasureExporter()
    >>> mxExpression = MEX.expressionToXml(nonArp)
    >>> MEX.dump(mxExpression)
    <non-arpeggiate />
    ```

MeasureExporter.fretBoardToXml(*fretBoard*) → [Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/musicxml/m21ToXml.html#MeasureExporter.fretBoardToXml)
:   The ChordWithFretBoard Object combines chord symbols with FretNote objects.

    ```python
    >>> myFretNote1 = tablature.FretNote(1, 2, 2)
    >>> myFretNote2 = tablature.FretNote(2, 3, 3)
    >>> myFretNote3 = tablature.FretNote(3, 2, 1)
    >>> guitarChord = tablature.ChordWithFretBoard('DM', numStrings=6,
    ...                    fretNotes=[myFretNote1, myFretNote2, myFretNote3])
    >>> guitarChord.tuning = tablature.GuitarFretBoard().tuning
    >>> guitarChord.getPitches()
    [None, None, None,
     <music21.pitch.Pitch A3>, <music21.pitch.Pitch D4>, <music21.pitch.Pitch F#4>]
    >>> MEX = musicxml.m21ToXml.MeasureExporter()
    >>> MEXChordWithFret = MEX.fretBoardToXml(guitarChord)
    >>> MEX.dump(MEXChordWithFret)
    <frame>
        <frame-strings>6</frame-strings>
        <frame-frets>4</frame-frets>
        <frame-note>
            <string>3</string>
            <fret>2</fret>
            <fingering>1</fingering>
        </frame-note>
        <frame-note>
            <string>2</string>
            <fret>3</fret>
            <fingering>3</fingering>
        </frame-note>
        <frame-note>
            <string>1</string>
            <fret>2</fret>
            <fingering>2</fingering>
        </frame-note>
    </frame>
    ```

MeasureExporter.fretNoteToXml(*fretNote*) → [Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")[[source]](../_modules/music21/musicxml/m21ToXml.html#MeasureExporter.fretNoteToXml)
:   Converts a FretNote Object to MusicXML readable format.

    Note that, although music21 is referring to FretNotes as FretNotes,
    musicxml refers to them as frame notes. To convert between the two formats,
    each ‘Fret-Note’ must be converted to ‘Frame-Note’.

    ```python
    >>> fn = tablature.FretNote(string=3, fret=1, fingering=2)
    >>> MEX = musicxml.m21ToXml.MeasureExporter()
    >>> MEXFretNote = MEX.fretNoteToXml(fn)
    >>> MEX.dump(MEXFretNote)
    <frame-note>
        <string>3</string>
        <fret>1</fret>
        <fingering>2</fingering>
    </frame-note>
    ```

    Without fingering!

    ```python
    >>> fn2 = tablature.FretNote(string=5, fret=2)
    >>> MEX = musicxml.m21ToXml.MeasureExporter()
    >>> MEXOtherFretNote = MEX.fretNoteToXml(fn2)
    >>> MEX.dump(MEXOtherFretNote)
    <frame-note>
        <string>5</string>
        <fret>2</fret>
    </frame-note>
    ```

MeasureExporter.getArpeggioNumber(*arp: [ArpeggioMarkSpanner](moduleExpressions.html#music21.expressions.ArpeggioMarkSpanner "music21.expressions.ArpeggioMarkSpanner")*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](../_modules/music21/musicxml/m21ToXml.html#MeasureExporter.getArpeggioNumber)

MeasureExporter.intervalToXmlTranspose(*i=None*)[[source]](../_modules/music21/musicxml/m21ToXml.html#MeasureExporter.intervalToXmlTranspose)
:   ```python
    >>> ME = musicxml.m21ToXml.MeasureExporter()
    >>> i = interval.Interval('P5')
    >>> mxTranspose = ME.intervalToXmlTranspose(i)
    >>> ME.dump(mxTranspose)
    <transpose>
      <diatonic>4</diatonic>
      <chromatic>7</chromatic>
    </transpose>
    ```

    ```python
    >>> i = interval.Interval('A13')
    >>> mxTranspose = ME.intervalToXmlTranspose(i)
    >>> ME.dump(mxTranspose)
    <transpose>
      <diatonic>5</diatonic>
      <chromatic>10</chromatic>
      <octave-change>1</octave-change>
    </transpose>
    ```

    ```python
    >>> i = interval.Interval('-M6')
    >>> mxTranspose = ME.intervalToXmlTranspose(i)
    >>> ME.dump(mxTranspose)
    <transpose>
      <diatonic>-5</diatonic>
      <chromatic>-9</chromatic>
    </transpose>
    ```

    ```python
    >>> i = interval.Interval('-M9')
    >>> mxTranspose = ME.intervalToXmlTranspose(i)
    >>> ME.dump(mxTranspose)
    <transpose>
      <diatonic>-1</diatonic>
      <chromatic>-2</chromatic>
      <octave-change>-1</octave-change>
    </transpose>
    ```

MeasureExporter.keySignatureToXml(*keyOrKeySignature*)[[source]](../_modules/music21/musicxml/m21ToXml.html#MeasureExporter.keySignatureToXml)
:   returns a key tag from a music21
    key.KeySignature or key.Key object

    ```python
    >>> ks = key.KeySignature(-3)
    >>> ks
    <music21.key.KeySignature of 3 flats>
    ```

    ```python
    >>> MEX = musicxml.m21ToXml.MeasureExporter()
    >>> mxKey = MEX.keySignatureToXml(ks)
    >>> MEX.dump(mxKey)
    <key>
      <fifths>-3</fifths>
    </key>
    ```

    ```python
    >>> ks.mode = 'major'
    >>> mxKey = MEX.keySignatureToXml(ks)
    >>> MEX.dump(mxKey)
    <key>
      <fifths>-3</fifths>
      <mode>major</mode>
    </key>
    ```

    ```python
    >>> ksNonTrad = key.KeySignature(sharps=None)
    >>> ksNonTrad.alteredPitches = ['C#', 'E-4']
    >>> ksNonTrad
    <music21.key.KeySignature of pitches: [C#, E-4]>
    ```

    ```python
    >>> mxKeyNonTrad = MEX.keySignatureToXml(ksNonTrad)
    >>> MEX.dump(mxKeyNonTrad)
    <key>
      <key-step>C</key-step>
      <key-alter>1</key-alter>
      <key-step>E</key-step>
      <key-alter>-1</key-alter>
      <key-octave number="2">4</key-octave>
    </key>
    ```

MeasureExporter.lyricToXml(*ly: [Lyric](moduleNote.html#music21.note.Lyric "music21.note.Lyric")*)[[source]](../_modules/music21/musicxml/m21ToXml.html#MeasureExporter.lyricToXml)
:   Translate a music21 [`Lyric`](moduleNote.html#music21.note.Lyric "music21.note.Lyric") object
    to a <lyric> tag.

    Lyrics have attribute list %justify, %position, %placement, %color, %print-object

MeasureExporter.mainElementsParse()[[source]](../_modules/music21/musicxml/m21ToXml.html#MeasureExporter.mainElementsParse)
:   deals with parsing all the elements in a stream, whether it has voices or not.

MeasureExporter.makePedalResumeLineXml(*pm: [PedalMark](moduleExpressions.html#music21.expressions.PedalMark "music21.expressions.PedalMark")*) → [Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")[[source]](../_modules/music21/musicxml/m21ToXml.html#MeasureExporter.makePedalResumeLineXml)

MeasureExporter.measureStyle()[[source]](../_modules/music21/musicxml/m21ToXml.html#MeasureExporter.measureStyle)
:   return a <measure-style> Element or None according to the contents of the Stream.

    Currently, only multiple-rest is supported.

MeasureExporter.moveBackward(*byOffset: OffsetQL*)[[source]](../_modules/music21/musicxml/m21ToXml.html#MeasureExporter.moveBackward)
:   Moves self.offsetInMeasure backward by an OffsetQL, appending the appropriate
    <backup> tag (expressed in divisions) to self.xmlRoot.

    ```python
    >>> MEX = musicxml.m21ToXml.MeasureExporter()
    >>> len(MEX.xmlRoot)
    0
    >>> MEX.moveBackward(2)
    >>> MEX.dump(MEX.xmlRoot)
    <measure>
      <backup>
        <duration>20160</duration>
      </backup>
    </measure>
    >>> len(MEX.xmlRoot)
    1
    ```

MeasureExporter.moveForward(*byOffset: OffsetQL*)[[source]](../_modules/music21/musicxml/m21ToXml.html#MeasureExporter.moveForward)
:   Moves self.offsetInMeasure forward by an OffsetQL, appending the appropriate
    <forward> tag (expressed in divisions) to self.xmlRoot.

    ```python
    >>> MEX = musicxml.m21ToXml.MeasureExporter()
    >>> len(MEX.xmlRoot)
    0
    >>> MEX.moveForward(1)
    >>> MEX.dump(MEX.xmlRoot)
    <measure>
      <forward>
        <duration>10080</duration>
      </forward>
    </measure>
    >>> len(MEX.xmlRoot)
    1
    ```

MeasureExporter.noChordToXml(*cs: [NoChord](moduleHarmony.html#music21.harmony.NoChord "music21.harmony.NoChord")*) → [Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")[[source]](../_modules/music21/musicxml/m21ToXml.html#MeasureExporter.noChordToXml)
:   Convert a NoChord object to an mxHarmony object (or a rest
    if .writeAsChord = True).

    Expected attributes of the NoChord object:

    ```python
    >>> nc = harmony.NoChord()
    >>> nc.chordKind
    'none'
    ```

    ```python
    >>> nc.chordKindStr
    'N.C.'
    ```

    Other values may not export:

    ```python
    >>> nc.chordKindStr = ''
    >>> nc.write()
    Traceback (most recent call last):
    music21.musicxml.xmlObjects.MusicXMLExportException:
         In part (None), measure (1): NoChord object's chordKindStr must be non-empty
    ```

    ```python
    >>> nc.chordKind = None
    >>> nc.write()
    Traceback (most recent call last):
    music21.musicxml.xmlObjects.MusicXMLExportException:
         In part (None), measure (1): NoChord object's chordKind must be 'none'
    ```

    To realize the NoChord as a rest:

    ```python
    >>> nc2 = harmony.NoChord()
    >>> nc2.writeAsChord = True
    >>> MEX = musicxml.m21ToXml.MeasureExporter()
    >>> mxNote = MEX.noChordToXml(nc2)
    >>> MEX.dump(mxNote)
    <note>
        <rest />
        <duration>10080</duration>
        <type>quarter</type>
    </note>
    ```

MeasureExporter.noteToNotations(*n: [GeneralNote](moduleNote.html#music21.note.GeneralNote "music21.note.GeneralNote")*, *noteIndexInChord: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*, *chordParent: [Chord](moduleChord.html#music21.chord.Chord "music21.chord.Chord") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")][[source]](../_modules/music21/musicxml/m21ToXml.html#MeasureExporter.noteToNotations)
:   Take information from .expressions,
    .articulations, and spanners to
    make the <notations> tag for a note.

MeasureExporter.noteToXml(*n: [GeneralNote](moduleNote.html#music21.note.GeneralNote "music21.note.GeneralNote")*, *noteIndexInChord=0*, *chordParent=None*)[[source]](../_modules/music21/musicxml/m21ToXml.html#MeasureExporter.noteToXml)
:   Translate a music21 [`Note`](moduleNote.html#music21.note.Note "music21.note.Note") or a Rest into a
    ElementTree, note element.

    Note that, some note-attached spanners, such
    as octave shifts, produce direction (and direction types)
    in this method.

    ```python
    >>> n = note.Note('D#5')
    >>> n.quarterLength = 3
    >>> n.volume.velocityScalar = 0.5
    >>> n.style.color = 'silver'
    ```

    ```python
    >>> MEX = musicxml.m21ToXml.MeasureExporter()
    >>> len(MEX.xmlRoot)
    0
    >>> mxNote = MEX.noteToXml(n)
    >>> mxNote
    <Element 'note' at 0x10113cb38>
    >>> MEX.dump(mxNote)
    <note color="#C0C0C0" dynamics="70.56">
      <pitch>
        <step>D</step>
        <alter>1</alter>
        <octave>5</octave>
      </pitch>
      <duration>30240</duration>
      <type>half</type>
      <dot />
      <accidental>sharp</accidental>
      <notehead color="#C0C0C0" parentheses="no">normal</notehead>
    </note>
    >>> len(MEX.xmlRoot)
    1
    ```

    ```python
    >>> r = note.Rest()
    >>> r.quarterLength = 1/3
    >>> r.duration.tuplets[0].type = 'start'
    >>> mxRest = MEX.noteToXml(r)
    >>> MEX.dump(mxRest)
    <note>
      <rest />
      <duration>3360</duration>
      <type>eighth</type>
      <time-modification>
        <actual-notes>3</actual-notes>
        <normal-notes>2</normal-notes>
        <normal-type>eighth</normal-type>
      </time-modification>
      <notations>
        <tuplet bracket="yes" number="1" placement="above" type="start">
          <tuplet-actual>
            <tuplet-number>3</tuplet-number>
            <tuplet-type>eighth</tuplet-type>
          </tuplet-actual>
          <tuplet-normal>
            <tuplet-number>2</tuplet-number>
            <tuplet-type>eighth</tuplet-type>
          </tuplet-normal>
        </tuplet>
      </notations>
    </note>
    >>> len(MEX.xmlRoot)
    2
    ```

    ```python
    >>> n.notehead = 'diamond'
    >>> n.articulations.append(articulations.Pizzicato())
    >>> mxNote = MEX.noteToXml(n)
    >>> MEX.dump(mxNote)
    <note color="#C0C0C0" dynamics="70.56" pizzicato="yes">
      ...
      <notehead color="#C0C0C0" parentheses="no">diamond</notehead>
    </note>
    ```

    Notes with complex durations need to be simplified before coming here
    otherwise they raise `MusicXMLExportException`:

    ```python
    >>> nComplex = note.Note()
    >>> nComplex.duration.quarterLength = 5.0
    >>> mxComplex = MEX.noteToXml(nComplex)
    Traceback (most recent call last):
    music21.musicxml.xmlObjects.MusicXMLExportException:
    Cannot convert complex durations to MusicXML.
    Try exporting with makeNotation=True or manually running splitAtDurations()
    ```

    TODO: Test with spanners

MeasureExporter.noteheadToXml(*n: [NotRest](moduleNote.html#music21.note.NotRest "music21.note.NotRest")*) → [Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")[[source]](../_modules/music21/musicxml/m21ToXml.html#MeasureExporter.noteheadToXml)
:   Translate a music21 [`NotRest`](moduleNote.html#music21.note.NotRest "music21.note.NotRest") object
    such as a Note, or Chord into a <notehead> tag.

    ```python
    >>> n = note.Note('C#4')
    >>> n.notehead = 'diamond'
    >>> MEX = musicxml.m21ToXml.MeasureExporter()
    >>> mxN = MEX.noteheadToXml(n)
    >>> MEX.dump(mxN)
    <notehead parentheses="no">diamond</notehead>
    ```

    ```python
    >>> n1 = note.Note('c3')
    >>> n1.style.color = 'red'
    >>> n1.notehead = 'diamond'
    >>> n1.noteheadParenthesis = True
    >>> n1.noteheadFill = False
    >>> mxN = MEX.noteheadToXml(n1)
    >>> MEX.dump(mxN)
    <notehead color="#FF0000" filled="no" parentheses="yes">diamond</notehead>
    ```

    ```python
    >>> n1 = note.Note('c3')
    >>> n1.style.color = 'red'
    >>> n1.notehead = 'diamond'
    >>> n1.noteheadParenthesis = True
    >>> n1.noteheadFill = False
    >>> mxN = MEX.noteheadToXml(n1)
    >>> MEX.dump(mxN)
    <notehead color="#FF0000" filled="no" parentheses="yes">diamond</notehead>
    ```

MeasureExporter.objectAttachedSpannersToNotations(*obj: [Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")*, *noteIndexInChord: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*, *objectSpannerBundle: [SpannerBundle](moduleSpanner.html#music21.spanner.SpannerBundle "music21.spanner.SpannerBundle") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")][[source]](../_modules/music21/musicxml/m21ToXml.html#MeasureExporter.objectAttachedSpannersToNotations)
:   return a list of <notations> from spanners related to the object that should appear
    in the notations tag (slurs, slides, etc.)

    ```python
    >>> n0 = note.Note('C')
    >>> n1 = note.Note('D')
    >>> trem = expressions.TremoloSpanner([n0, n1])
    >>> m = stream.Measure()
    >>> m.insert(0, trem)
    >>> m.append(n0)
    >>> m.append(n1)
    >>> mex = musicxml.m21ToXml.MeasureExporter(m)
    >>> out = mex.objectAttachedSpannersToNotations(n0, objectSpannerBundle=m.spannerBundle)
    >>> out
    [<Element 'ornaments' at 0x1114d9408>]
    >>> mex.dump(out[0])
    <ornaments>
      <tremolo type="start">3</tremolo>
    </ornaments>
    ```

    ```python
    >>> out = mex.objectAttachedSpannersToNotations(n1, objectSpannerBundle=m.spannerBundle)
    >>> mex.dump(out[0])
    <ornaments>
      <tremolo type="stop">3</tremolo>
    </ornaments>
    ```

MeasureExporter.objectAttachedSpannersToTechnicals(*obj*, *objectSpannerBundle=None*)[[source]](../_modules/music21/musicxml/m21ToXml.html#MeasureExporter.objectAttachedSpannersToTechnicals)
:   return a list of <technical> from spanners related to the object that should appear
    in the technical tag of the notations tag (hammer-on, pull-off etc.)

    ```python
    >>> n0 = note.Note('C')
    >>> n1 = note.Note('D')
    >>> n2 = note.Note('F')
    >>> n3 = note.Note('E')
    >>> hammerOn01 = articulations.HammerOn([n0, n1])
    >>> pullOff23 = articulations.PullOff([n2, n3])
    >>> m = stream.Measure()
    >>> m.insert(0, hammerOn01)
    >>> m.insert(0, pullOff23)
    >>> m.append(n0)
    >>> m.append(n1)
    >>> m.append(n2)
    >>> m.append(n3)
    >>> mex = musicxml.m21ToXml.MeasureExporter(m)
    >>> out = mex.objectAttachedSpannersToTechnicals(n0, m.spannerBundle)
    >>> out
    [<Element 'hammer-on' at 0x102857f40>]
    >>> mex.dump(out[0])
    <hammer-on number="1" type="start">H</hammer-on>
    >>> out = mex.objectAttachedSpannersToTechnicals(n3, m.spannerBundle)
    >>> mex.dump(out[0])
    <pull-off number="1" type="stop" />
    ```

MeasureExporter.ornamentToMxAccidentalMarks(*ornamentObj: [Ornament](moduleExpressions.html#music21.expressions.Ornament "music21.expressions.Ornament")*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")][[source]](../_modules/music21/musicxml/m21ToXml.html#MeasureExporter.ornamentToMxAccidentalMarks)

MeasureExporter.parse()[[source]](../_modules/music21/musicxml/m21ToXml.html#MeasureExporter.parse)
:   main parse call.

    deals with transposing, repeat brackets, setting measureNumber and width,
    the first mxPrint, the first <attributes> tag, the left barline, parsing all internal
    elements, setting the right barline, then returns the root <measure> tag.

MeasureExporter.parseFlatElements(*m: [Measure](moduleStreamBase.html#music21.stream.base.Measure "music21.stream.base.Measure") | [Voice](moduleStreamBase.html#music21.stream.base.Voice "music21.stream.base.Voice")*, *\**, *backupAfterwards: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/musicxml/m21ToXml.html#MeasureExporter.parseFlatElements)
:   Deals with parsing all the elements in .elements, assuming that .elements is flat.

    m here can be a Measure or Voice, but it must be flat.

    If m is a ‘Voice’ class, we use the .id element to set self.currentVoiceId and then
    send a backup tag to go back to the beginning of the measure.

    Note that if the .id is high enough to be an id(x) memory location, then a small
    voice number is used instead.

MeasureExporter.parseOneElement(*obj*, *appendSpanners: [AppendSpanners](moduleCommonEnums.html#music21.common.enums.AppendSpanners "music21.common.enums.AppendSpanners") = <AppendSpanners.NORMAL>*)[[source]](../_modules/music21/musicxml/m21ToXml.html#MeasureExporter.parseOneElement)
:   parse one element completely and add it to xmlRoot, updating
    offsetInMeasure, etc.

MeasureExporter.pedalObjectToXml(*po: [PedalObject](moduleExpressions.html#music21.expressions.PedalObject "music21.expressions.PedalObject")*) → [Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/musicxml/m21ToXml.html#MeasureExporter.pedalObjectToXml)
:   Convert a PedalObject object (i.e. PedalBounce, PedalGapStart,
    PedalGapEnds) to a MusicXML <direction> tag with a <pedal> tag
    inside it. Attributes like pedalForm are stored in the enclosing
    PedalMark spanner.

    ```python
    >>> pm = expressions.PedalMark()
    >>> po = expressions.PedalBounce()
    >>> pm.addSpannedElements(po)
    >>> pm.pedalForm = expressions.PedalForm.Line
    >>> pm.pedalType = expressions.PedalType.Sustain
    >>> MEX = musicxml.m21ToXml.MeasureExporter()
    >>> mxPedal = MEX.pedalObjectToXml(po)
    >>> MEX.dump(mxPedal)
    <direction>
      <direction-type>
        <pedal line="yes" type="change" />
      </direction-type>
    </direction>
    ```

    ```python
    >>> pm = expressions.PedalMark()
    >>> po = expressions.PedalGapStart()
    >>> pm.addSpannedElements(po)
    >>> pm.pedalForm = expressions.PedalForm.Line
    >>> pm.pedalType = expressions.PedalType.Sustain
    >>> po.placement = 'above'
    >>> MEX = musicxml.m21ToXml.MeasureExporter()
    >>> mxPedal = MEX.pedalObjectToXml(po)
    >>> MEX.dump(mxPedal)
    <direction placement="above">
      <direction-type>
        <pedal line="yes" type="discontinue" />
      </direction-type>
    </direction>
    ```

    ```python
    >>> pm = expressions.PedalMark()
    >>> po = expressions.PedalGapEnd()
    >>> pm.addSpannedElements(po)
    >>> pm.pedalForm = expressions.PedalForm.Line
    >>> pm.pedalType = expressions.PedalType.Sustain
    >>> po.placement = 'below'
    >>> MEX = musicxml.m21ToXml.MeasureExporter()
    >>> mxPedal = MEX.pedalObjectToXml(po)
    >>> MEX.dump(mxPedal)
    <direction placement="below">
      <direction-type>
        <pedal line="yes" type="resume" />
      </direction-type>
    </direction>
    ```

MeasureExporter.pitchToXml(*p: [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")*)[[source]](../_modules/music21/musicxml/m21ToXml.html#MeasureExporter.pitchToXml)
:   Convert a [`Pitch`](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") to xml.
    Does not create the <accidental> tag.

    ```python
    >>> p = pitch.Pitch('D#5')
    >>> MEX = musicxml.m21ToXml.MeasureExporter()
    >>> mxPitch = MEX.pitchToXml(p)
    >>> MEX.dump(mxPitch)
    <pitch>
      <step>D</step>
      <alter>1</alter>
      <octave>5</octave>
    </pitch>
    ```

MeasureExporter.placeInDirection(*mxObj: [Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")*, *m21Obj: [Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\**, *setSound: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*) → [Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")[[source]](../_modules/music21/musicxml/m21ToXml.html#MeasureExporter.placeInDirection)
:   Places the mxObj <element> inside <direction><direction-type>
    and sets <offset> if needed.

    * Changed in v8: added setSound keyword (see [`setOffsetOptional()`](#music21.musicxml.m21ToXml.MeasureExporter.setOffsetOptional "music21.musicxml.m21ToXml.MeasureExporter.setOffsetOptional")).

MeasureExporter.rehearsalMarkToXml(*rm: [RehearsalMark](moduleExpressions.html#music21.expressions.RehearsalMark "music21.expressions.RehearsalMark")*) → [Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")[[source]](../_modules/music21/musicxml/m21ToXml.html#MeasureExporter.rehearsalMarkToXml)
:   Convert a RehearsalMark object to a MusicXML <direction> tag with a <rehearsal> tag
    inside it.

    ```python
    >>> rm = expressions.RehearsalMark('II')
    >>> rm.style.enclosure = 'square'
    >>> MEX = musicxml.m21ToXml.MeasureExporter()
    >>> mxRehearsal = MEX.rehearsalMarkToXml(rm)
    >>> MEX.dump(mxRehearsal)
    <direction>
      <direction-type>
        <rehearsal enclosure="square" halign="center" valign="middle">II</rehearsal>
        </direction-type>
      </direction>
    ```

MeasureExporter.relatedSpanners(*target: [Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[Sequence](https://docs.python.org/3/library/typing.html#typing.Sequence "(in Python v3.14)")[[Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")], [Sequence](https://docs.python.org/3/library/typing.html#typing.Sequence "(in Python v3.14)")[[Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")]][[source]](../_modules/music21/musicxml/m21ToXml.html#MeasureExporter.relatedSpanners)
:   return two lists or empty tuples:
    (1) spanners related to the object that should appear before the object
    in the <measure> tag. (2) spanners related to the object that should appear after the
    object in the <measure> tag.

MeasureExporter.repeatToXml(*r*)[[source]](../_modules/music21/musicxml/m21ToXml.html#MeasureExporter.repeatToXml)
:   returns a <repeat> tag from a barline object.

    ```python
    >>> b = bar.Repeat(direction='end')
    >>> MEX = musicxml.m21ToXml.MeasureExporter()
    >>> mxRepeat = MEX.repeatToXml(b)
    >>> MEX.dump(mxRepeat)
    <repeat direction="backward" />
    ```

    ```python
    >>> b.times = 3
    >>> mxRepeat = MEX.repeatToXml(b)
    >>> MEX.dump(mxRepeat)
    <repeat direction="backward" times="3" />
    ```

MeasureExporter.restToXml(*r: [Rest](moduleNote.html#music21.note.Rest "music21.note.Rest")*)[[source]](../_modules/music21/musicxml/m21ToXml.html#MeasureExporter.restToXml)
:   Convert a Rest object to a <note> with a <rest> tag underneath it.

    ```python
    >>> MEX = musicxml.m21ToXml.MeasureExporter()
    >>> r = note.Rest(quarterLength=2.0)
    ```

    Give the rest some context:

    ```python
    >>> m = stream.Measure()
    >>> m.timeSignature = meter.TimeSignature('4/4')
    >>> m.append(r)
    >>> mxNoteRest = MEX.restToXml(r)
    >>> MEX.dump(mxNoteRest)
    <note>
      <rest />
      <duration>20160</duration>
      <type>half</type>
    </note>
    ```

    Now it is a full measure:

    ```python
    >>> m.timeSignature = meter.TimeSignature('2/4')
    >>> mxNoteRest = MEX.restToXml(r)
    >>> MEX.dump(mxNoteRest)
    <note>
      <rest measure="yes" />
      <duration>20160</duration>
    </note>
    ```

    Unless we specify that it should not be converted to a full measure:

    ```python
    >>> r.fullMeasure = False
    >>> mxNoteRest = MEX.restToXml(r)
    >>> MEX.dump(mxNoteRest)
    <note>
      <rest />
      <duration>20160</duration>
      <type>half</type>
    </note>
    ```

    With True or “always” it will be converted to full measure even if
    it does not match:

    ```python
    >>> m.timeSignature = meter.TimeSignature('4/4')
    >>> r.duration.dots = 1
    >>> r.fullMeasure = True
    >>> mxNoteRest = MEX.restToXml(r)
    >>> MEX.dump(mxNoteRest)
    <note>
      <rest measure="yes" />
      <duration>30240</duration>
    </note>
    ```

    Note that if a measure has paddingLeft/paddingRight (such as a pickup)
    then a fullMeasure duration might not match the TimeSignature duration.

    The display-step and display-octave are set from a Rest’s stepShift:

    ```python
    >>> r = note.Rest()
    >>> r.stepShift = 1
    >>> mxNoteRest = MEX.restToXml(r)
    >>> MEX.dump(mxNoteRest)
    <note>
      <rest>
        <display-step>C</display-step>
        <display-octave>5</display-octave>
      </rest>
      <duration>10080</duration>
      <type>quarter</type>
    </note>
    ```

    Clef context matters:

    ```python
    >>> m = stream.Measure()
    >>> m.clef = clef.BassClef()
    >>> m.append(r)
    >>> mxNoteRest = MEX.restToXml(r)
    >>> MEX.dump(mxNoteRest)
    <note>
      <rest>
        <display-step>E</display-step>
        <display-octave>3</display-octave>
      </rest>
      <duration>10080</duration>
      <type>quarter</type>
    </note>
    ```

MeasureExporter.romanNumeralToXml(*rn: [roman.RomanNumeral](moduleRoman.html#music21.roman.RomanNumeral "music21.roman.RomanNumeral")*) → Element | [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[Element][[source]](../_modules/music21/musicxml/m21ToXml.html#MeasureExporter.romanNumeralToXml)
:   Convert a RomanNumeral object to either a chord (if .writeAsChord is True)
    or a Harmony XML Element.

    ```python
    >>> rnI = roman.RomanNumeral('I', 'C')
    >>> MEX = musicxml.m21ToXml.MeasureExporter()
    >>> MEX.currentDivisions = 10
    ```

    ```python
    >>> listMxChords = MEX.romanNumeralToXml(rnI)
    >>> len(listMxChords)
    3
    >>> MEX.dump(listMxChords[1])
    <note>
      <chord />
      <pitch>
        <step>E</step>
        <octave>4</octave>
      </pitch>
      <duration>10</duration>
      <type>quarter</type>
    </note>
    ```

    If writeAsChord is False, we create a MusicXML 4.0 <numeral> tag.
    This does not work in the current version of MuseScore (which only
    supports MusicXML 3.1) but outputs decently well in Finale.

    ```python
    >>> rnI.writeAsChord = False
    >>> mxHarmonyFromRN = MEX.romanNumeralToXml(rnI)
    >>> MEX.dump(mxHarmonyFromRN)
    <harmony>
      <numeral>
        <numeral-root text="I">1</numeral-root>
        <numeral-key print-object="no">
          <numeral-fifths>0</numeral-fifths>
          <numeral-mode>major</numeral-mode>
        </numeral-key>
      </numeral>
      <kind>major</kind>
    </harmony>
    ```

    ```python
    >>> complexRn = roman.RomanNumeral('#iio65', 'e-')
    >>> complexRn.followsKeyChange = True
    >>> complexRn.writeAsChord = False
    >>> mxHarmonyFromRN = MEX.romanNumeralToXml(complexRn)
    >>> MEX.dump(mxHarmonyFromRN)
    <harmony>
      <numeral>
        <numeral-root text="#iio65">2</numeral-root>
        <numeral-alter location="left">1.0</numeral-alter>
        <numeral-key>
          <numeral-fifths>-6</numeral-fifths>
          <numeral-mode>minor</numeral-mode>
        </numeral-key>
      </numeral>
      <kind>diminished-seventh</kind>
      <inversion>1</inversion>
    </harmony>
    ```

    ```python
    >>> maj6 = roman.RomanNumeral('VI7', 'd')
    >>> maj6.writeAsChord = False
    >>> mxHarmonyFromRN = MEX.romanNumeralToXml(maj6)
    >>> MEX.dump(mxHarmonyFromRN)
    <harmony>
      <numeral>
        <numeral-root text="VI7">6</numeral-root>
        <numeral-key print-object="no">
          <numeral-fifths>-1</numeral-fifths>
          <numeral-mode>natural minor</numeral-mode>
        </numeral-key>
      </numeral>
      <kind>major-seventh</kind>
    </harmony>
    ```

    ```python
    >>> min6 = roman.RomanNumeral('vi', 'd')
    >>> min6.writeAsChord = False
    >>> mxHarmonyFromRN = MEX.romanNumeralToXml(min6)
    >>> mxHarmonyFromRN.find('.//numeral-mode').text
    'melodic minor'
    ```

    ```python
    >>> dim7 = roman.RomanNumeral('viiø65', 'd')
    >>> dim7.writeAsChord = False
    >>> mxHarmonyFromRN = MEX.romanNumeralToXml(dim7)
    >>> mxHarmonyFromRN.find('.//numeral-mode').text
    'harmonic minor'
    >>> mxHarmonyFromRN.find('kind').text
    'half-diminished'
    ```

    ```python
    >>> maj7 = roman.RomanNumeral('VII64', 'd')
    >>> maj7.writeAsChord = False
    >>> mxHarmonyFromRN = MEX.romanNumeralToXml(maj7)
    >>> mxHarmonyFromRN.find('.//numeral-mode').text
    'natural minor'
    ```

MeasureExporter.segnoToXml(*segno: [Segno](moduleRepeat.html#music21.repeat.Segno "music21.repeat.Segno")*) → [Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")[[source]](../_modules/music21/musicxml/m21ToXml.html#MeasureExporter.segnoToXml)
:   returns a segno inside a direction-type inside a direction.

    appends to score

    ```python
    >>> s = repeat.Segno()
    >>> MEX = musicxml.m21ToXml.MeasureExporter()
    >>> mxSegnoDir = MEX.segnoToXml(s)
    >>> MEX.dump(mxSegnoDir)
    <direction>
      <direction-type>
        <segno default-y="20" />
      </direction-type>
    </direction>
    ```

    ```python
    >>> s.id = 'segno0'
    >>> s.style.alignHorizontal = 'left'
    >>> MEX = musicxml.m21ToXml.MeasureExporter()
    >>> mxSegnoDir = MEX.segnoToXml(s)
    >>> MEX.dump(mxSegnoDir)
    <direction>
      <direction-type>
        <segno default-y="20" halign="left" id="segno0" />
      </direction-type>
    </direction>
    ```

MeasureExporter.setBarline(*barline*, *position*)[[source]](../_modules/music21/musicxml/m21ToXml.html#MeasureExporter.setBarline)
:   sets either a left or right barline from a
    bar.Barline() object or bar.Repeat() object

static MeasureExporter.setBend(*mxh: [Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")*, *bend: [FretBend](moduleArticulations.html#music21.articulations.FretBend "music21.articulations.FretBend")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/musicxml/m21ToXml.html#MeasureExporter.setBend)
:   Sets the bend-alter SubElement and the pre-bend,
    release and with-bar SubElements when present.

    Called from articulationToXmlTechnical

    ```python
    >>> from xml.etree.ElementTree import Element
    >>> from fractions import Fraction
    ```

    ```python
    >>> MEXclass = musicxml.m21ToXml.MeasureExporter
    ```

    ```python
    >>> a = articulations.FretBend(bendAlter=interval.Interval(2))
    >>> mxh = Element('bend')
    >>> MEXclass.setBend(mxh, a)
    >>> MEXclass.dump(mxh)
    <bend>
      <bend-alter>2</bend-alter>
    </bend>
    >>> mxh = Element('bend')
    >>> a = articulations.FretBend(bendAlter=interval.Interval(2))
    >>> a.preBend = True
    >>> MEXclass.setBend(mxh, a)
    >>> MEXclass.dump(mxh)
    <bend>
      <bend-alter>2</bend-alter>
      <pre-bend />
    </bend>
    >>> mxh = Element('bend')
    >>> a = articulations.FretBend(bendAlter=interval.Interval(-2), release=Fraction(1, 10080))
    >>> MEXclass.setBend(mxh, a)
    >>> MEXclass.dump(mxh)
    <bend>
      <bend-alter>-2</bend-alter>
      <release offset="1" />
    </bend>
    >>> mxh = Element('bend')
    >>> a = articulations.FretBend(bendAlter=interval.Interval(-2), withBar='scoop')
    >>> MEXclass.setBend(mxh, a)
    >>> MEXclass.dump(mxh)
    <bend>
      <bend-alter>-2</bend-alter>
      <with-bar>scoop</with-bar>
    </bend>
    ```

static MeasureExporter.setHarmonic(*mxh: [Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")*, *harm: [StringHarmonic](moduleArticulations.html#music21.articulations.StringHarmonic "music21.articulations.StringHarmonic")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/musicxml/m21ToXml.html#MeasureExporter.setHarmonic)
:   Sets the artificial or natural tag (or no tag) and
    zero or one of base-pitch, sounding-pitch, touching-pitch

    Called from articulationToXmlTechnical

    ```python
    >>> MEXClass = musicxml.m21ToXml.MeasureExporter
    ```

    ```python
    >>> a = articulations.StringHarmonic()
    >>> a.harmonicType = 'artificial'
    >>> a.pitchType = 'sounding'
    ```

    ```python
    >>> from xml.etree.ElementTree import Element
    >>> mxh = Element('harmonic')
    ```

    ```python
    >>> MEXClass.setHarmonic(mxh, a)
    >>> MEXClass.dump(mxh)
    <harmonic>
      <artificial />
      <sounding-pitch />
    </harmonic>
    ```

    [`Harmonic`](moduleArticulations.html#music21.articulations.Harmonic "music21.articulations.Harmonic") is probably too general for most uses,
    but if you use it, you get a harmonic tag with no details:

    ```python
    >>> b = articulations.Harmonic()
    >>> mxh2 = Element('harmonic')
    >>> MEXClass.setHarmonic(mxh2, b)
    >>> MEXClass.dump(mxh2)
    <harmonic />
    ```

MeasureExporter.setLeftBarline()[[source]](../_modules/music21/musicxml/m21ToXml.html#MeasureExporter.setLeftBarline)
:   Calls self.setBarline for the left side if the measure has a .leftBarline set.

MeasureExporter.setLineStyle(*mxObject*, *m21Object*)[[source]](../_modules/music21/musicxml/m21ToXml.html#MeasureExporter.setLineStyle)
:   Sets four additional elements for line elements, conforms to entity
    %line-shape, %line-type, %dashed-formatting (dash-length and space-length)

MeasureExporter.setMxAttributes()[[source]](../_modules/music21/musicxml/m21ToXml.html#MeasureExporter.setMxAttributes)
:   sets the attributes (x=y) for a measure,
    that is, number, implicit, and layoutWidth

    Does not create the <attributes> tag. That’s elsewhere.

MeasureExporter.setMxAttributesObjectForStartOfMeasure()[[source]](../_modules/music21/musicxml/m21ToXml.html#MeasureExporter.setMxAttributesObjectForStartOfMeasure)
:   creates an <attributes> tag at the start of the measure.

    We create one for each measure unless it is identical to self.parent.mxAttributes

MeasureExporter.setMxPrint()[[source]](../_modules/music21/musicxml/m21ToXml.html#MeasureExporter.setMxPrint)
:   Creates a <print> element and appends it to root, if one is needed.

MeasureExporter.setNoteInstrument(*n: [NotRest](moduleNote.html#music21.note.NotRest "music21.note.NotRest")*, *mxNote: [Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")*, *chordParent: [Chord](moduleChord.html#music21.chord.Chord "music21.chord.Chord") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*)[[source]](../_modules/music21/musicxml/m21ToXml.html#MeasureExporter.setNoteInstrument)
:   Insert <instrument> tags if necessary, that is, when there is more than one
    instrument anywhere in the same musicxml <part>.

MeasureExporter.setOffsetOptional(*m21Obj: [Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")*, *mxObj: [Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\**, *setSound: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*) → [Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/musicxml/m21ToXml.html#MeasureExporter.setOffsetOptional)
:   If this object has an offset different from self.offsetInMeasure,
    then create and return an offset Element.

    If mxObj is not None then the offset element will be appended to it.

MeasureExporter.setRbSpanners()[[source]](../_modules/music21/musicxml/m21ToXml.html#MeasureExporter.setRbSpanners)
:   Makes a set of spanners from repeat brackets

MeasureExporter.setRightBarline()[[source]](../_modules/music21/musicxml/m21ToXml.html#MeasureExporter.setRightBarline)
:   Calls self.setBarline for the right side if the measure has a .rightBarline set.

MeasureExporter.setTranspose()[[source]](../_modules/music21/musicxml/m21ToXml.html#MeasureExporter.setTranspose)
:   Set the transposition interval based on whether the active
    instrument for this period has a transposition object.

    Stores in self.transpositionInterval. Returns None

MeasureExporter.staffLayoutToXmlPrint(*staffLayout*, *mxPrint=None*)[[source]](../_modules/music21/musicxml/m21ToXml.html#MeasureExporter.staffLayoutToXmlPrint)

MeasureExporter.staffLayoutToXmlStaffDetails(*staffLayout*)[[source]](../_modules/music21/musicxml/m21ToXml.html#MeasureExporter.staffLayoutToXmlStaffDetails)
:   Convert a [`StaffLayout`](moduleLayout.html#music21.layout.StaffLayout "music21.layout.StaffLayout") object to a
    <staff-details> element.

    ```python
    >>> MEX = musicxml.m21ToXml.MeasureExporter()
    >>> sl = layout.StaffLayout()
    >>> sl.staffLines = 3  # tenor drums?
    >>> sl.staffType = stream.enums.StaffType.CUE
    >>> sl.hidden = True
    >>> mxDetails = MEX.staffLayoutToXmlStaffDetails(sl)
    >>> MEX.dump(mxDetails)
    <staff-details print-object="no">
          <staff-type>cue</staff-type>
          <staff-lines>3</staff-lines>
    </staff-details>
    ```

MeasureExporter.tempoIndicationToXml(*ti: [TempoIndication](moduleTempo.html#music21.tempo.TempoIndication "music21.tempo.TempoIndication")*) → [Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")[[source]](../_modules/music21/musicxml/m21ToXml.html#MeasureExporter.tempoIndicationToXml)
:   returns a <direction> tag for a single tempo indication.

    note that **two** direction tags may be added to xmlroot, the second one
    as a textExpression, but only the first will be returned.

    ```python
    >>> mm = tempo.MetronomeMark('slow', 40, note.Note(type='half'))
    >>> mm.style.justify = 'left'
    ```

    ```python
    >>> MEX = musicxml.m21ToXml.MeasureExporter()
    >>> mxDirection = MEX.tempoIndicationToXml(mm)
    >>> MEX.dump(mxDirection)
    <direction>
      <direction-type>
        <metronome parentheses="no">
          <beat-unit>half</beat-unit>
          <per-minute>40</per-minute>
        </metronome>
      </direction-type>
      <sound tempo="80" />
    </direction>
    ```

    In this case, two directions were added to xmlRoot. Here is the other one:

    ```python
    >>> MEX.dump(MEX.xmlRoot.findall('direction')[1])
    <direction>
      <direction-type>
        <words default-y="45" font-weight="bold"
            justify="left">slow</words>
      </direction-type>
    </direction>
    ```

    ```python
    >>> mm = tempo.MetronomeMark('slow', 40, duration.Duration(quarterLength=1.5))
    >>> mxDirection = MEX.tempoIndicationToXml(mm)
    >>> MEX.dump(mxDirection)
    <direction>
      <direction-type>
        <metronome parentheses="no">
          <beat-unit>quarter</beat-unit>
          <beat-unit-dot />
          <per-minute>40</per-minute>
        </metronome>
      </direction-type>
      <sound tempo="60" />
    </direction>
    ```

    ```python
    >>> mmod1 = tempo.MetricModulation()
    >>> mmod1.oldReferent = 0.75  # quarterLength
    >>> mmod1.newReferent = 'quarter'  # type
    >>> mxDirection = MEX.tempoIndicationToXml(mmod1)
    >>> MEX.dump(mxDirection)
    <direction>
      <direction-type>
        <metronome parentheses="no">
          <beat-unit>eighth</beat-unit>
          <beat-unit-dot />
          <beat-unit>quarter</beat-unit>
        </metronome>
      </direction-type>
    </direction>
    ```

    ```python
    >>> mmod1.newReferent = 'longa'  # music21 type w/ different musicxml name
    >>> mxDirection = MEX.tempoIndicationToXml(mmod1)
    >>> MEX.dump(mxDirection)
    <direction>
      <direction-type>
        <metronome parentheses="no">
          <beat-unit>eighth</beat-unit>
          <beat-unit-dot />
          <beat-unit>long</beat-unit>
        </metronome>
      </direction-type>
    </direction>
    ```

    This is the case where only a sound tag is added and no metronome mark

    ```python
    >>> mm = tempo.MetronomeMark()
    >>> mm.numberSounding = 60
    ```

    ```python
    >>> MEX = musicxml.m21ToXml.MeasureExporter()
    >>> mxDirection = MEX.tempoIndicationToXml(mm)
    >>> MEX.dump(mxDirection)
    <direction>
      <direction-type>
        <words />
      </direction-type>
      <sound tempo="60" />
    </direction>
    ```

    This is the case of a TempoText.

    ```python
    >>> tt = tempo.TempoText('Andante')
    >>> mxDirection = MEX.tempoIndicationToXml(tt)
    >>> MEX.dump(mxDirection)
    <direction>
      <direction-type>
        <words default-y="45" font-weight="bold">Andante</words>
      </direction-type>
    </direction>
    ```

MeasureExporter.textExpressionToXml(*teOrRe: [TextExpression](moduleExpressions.html#music21.expressions.TextExpression "music21.expressions.TextExpression") | [RepeatExpression](moduleRepeat.html#music21.repeat.RepeatExpression "music21.repeat.RepeatExpression")*) → [Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")[[source]](../_modules/music21/musicxml/m21ToXml.html#MeasureExporter.textExpressionToXml)
:   Convert a TextExpression or RepeatExpression to a MusicXML mxDirection type.
    returns a musicxml.mxObjects.Direction object

MeasureExporter.tieToXmlTie(*m21Tie: [Tie](moduleTie.html#music21.tie.Tie "music21.tie.Tie")*)[[source]](../_modules/music21/musicxml/m21ToXml.html#MeasureExporter.tieToXmlTie)
:   returns a list of ties from a Tie object.

    A ‘continue’ tie requires two <tie> tags to represent.

    ```python
    >>> tieObj = tie.Tie('continue')
    >>> MEX = musicxml.m21ToXml.MeasureExporter()
    >>> tieList = MEX.tieToXmlTie(tieObj)
    >>> for mxT in tieList:
    ...     MEX.dump(mxT)
    <tie type="stop" />
    <tie type="start" />
    ```

MeasureExporter.tieToXmlTied(*m21Tie: [Tie](moduleTie.html#music21.tie.Tie "music21.tie.Tie")*)[[source]](../_modules/music21/musicxml/m21ToXml.html#MeasureExporter.tieToXmlTied)
:   In musicxml, a tie is represented in sound
    by the tie tag (near the pitch object), and
    the <tied> tag in notations. This
    creates the <tied> tag.

    Returns a list since a music21 “continue” tie type needs two tags
    in musicxml. List may be empty if tie.style == “hidden”

    ```python
    >>> tieObj = tie.Tie('continue')
    >>> tieObj.id = 'tied1'
    ```

    ```python
    >>> MEX = musicxml.m21ToXml.MeasureExporter()
    >>> tiedList = MEX.tieToXmlTied(tieObj)
    >>> for mxT in tiedList:
    ...     MEX.dump(mxT)
    <tied id="tied1" type="stop" />
    <tied type="start" />
    ```

    ```python
    >>> tieObj.style = 'hidden'
    >>> tiedList = MEX.tieToXmlTied(tieObj)
    >>> len(tiedList)
    0
    ```

MeasureExporter.timeSignatureToXml(*ts: [TimeSignature](moduleMeterBase.html#music21.meter.base.TimeSignature "music21.meter.base.TimeSignature") | [SenzaMisuraTimeSignature](moduleMeterBase.html#music21.meter.base.SenzaMisuraTimeSignature "music21.meter.base.SenzaMisuraTimeSignature")*)[[source]](../_modules/music21/musicxml/m21ToXml.html#MeasureExporter.timeSignatureToXml)
:   Returns a single <time> tag from a meter.TimeSignature object.

    Compound meters are represented as multiple pairs of beat
    and beat-type elements

    ```python
    >>> MEX = musicxml.m21ToXml.MeasureExporter()
    >>> a = meter.TimeSignature('3/4')
    >>> b = MEX.timeSignatureToXml(a)
    >>> MEX.dump(b)
    <time>
      <beats>3</beats>
      <beat-type>4</beat-type>
    </time>
    ```

    ```python
    >>> a = meter.TimeSignature('3/4+2/4')
    >>> b = MEX.timeSignatureToXml(a)
    >>> MEX.dump(b)
    <time>
      <beats>3</beats>
      <beat-type>4</beat-type>
      <beats>2</beats>
      <beat-type>4</beat-type>
    </time>
    ```

    ```python
    >>> a.setDisplay('5/4')
    >>> b = MEX.timeSignatureToXml(a)
    >>> MEX.dump(b)
    <time>
      <beats>5</beats>
      <beat-type>4</beat-type>
    </time>
    ```

    ```python
    >>> a = meter.TimeSignature('4/4')
    >>> a.symbol = 'common'
    >>> b = MEX.timeSignatureToXml(a)
    >>> MEX.dump(b)
    <time symbol="common">
      <beats>4</beats>
      <beat-type>4</beat-type>
    </time>
    ```

    ```python
    >>> a.symbol = ''
    >>> a.symbolizeDenominator = True
    >>> b = MEX.timeSignatureToXml(a)
    >>> MEX.dump(b)
    <time symbol="note">
      <beats>4</beats>
      <beat-type>4</beat-type>
    </time>
    ```

    ```python
    >>> sm = meter.SenzaMisuraTimeSignature('free')
    >>> b = MEX.timeSignatureToXml(sm)
    >>> MEX.dump(b)
    <time>
      <senza-misura>free</senza-misura>
    </time>
    ```

MeasureExporter.tupletToTimeModification(*tup*) → [Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")[[source]](../_modules/music21/musicxml/m21ToXml.html#MeasureExporter.tupletToTimeModification)
:   ```python
    >>> tup = duration.Tuplet(11, 8)
    >>> MEX = musicxml.m21ToXml.MeasureExporter()
    >>> mxTimeMod = MEX.tupletToTimeModification(tup)
    >>> MEX.dump(mxTimeMod)
    <time-modification>
      <actual-notes>11</actual-notes>
      <normal-notes>8</normal-notes>
    </time-modification>
    ```

    ```python
    >>> tup.setDurationType('eighth', dots=2)
    >>> mxTimeMod = MEX.tupletToTimeModification(tup)
    >>> MEX.dump(mxTimeMod)
    <time-modification>
      <actual-notes>11</actual-notes>
      <normal-notes>8</normal-notes>
      <normal-type>eighth</normal-type>
      <normal-dot />
      <normal-dot />
    </time-modification>
    ```

MeasureExporter.tupletToXmlTuplet(*tuplet*, *tupletIndex=1*)[[source]](../_modules/music21/musicxml/m21ToXml.html#MeasureExporter.tupletToXmlTuplet)
:   In musicxml, a tuplet is represented by
    a timeModification and visually by the
    <notations><tuplet> tag. This method
    creates the latter.

    Returns a list of them because a
    startStop type tuplet needs two tuplet
    brackets.

    TODO: make sure something happens if
    :   makeTupletBrackets is not set.

    ```python
    >>> tup = duration.Tuplet(11, 8)
    >>> tup.type = 'start'
    >>> MEX = musicxml.m21ToXml.MeasureExporter()
    >>> mxTup = MEX.tupletToXmlTuplet(tup)
    >>> len(mxTup)
    1
    >>> MEX.dump(mxTup[0])
    <tuplet bracket="yes" number="1" placement="above" type="start">
      <tuplet-actual>
        <tuplet-number>11</tuplet-number>
      </tuplet-actual>
      <tuplet-normal>
        <tuplet-number>8</tuplet-number>
      </tuplet-normal>
    </tuplet>
    ```

    ```python
    >>> tup.tupletActualShow = 'both'
    >>> tup.tupletNormalShow = 'type'
    >>> mxTup = MEX.tupletToXmlTuplet(tup)
    >>> MEX.dump(mxTup[0])
    <tuplet bracket="yes" number="1" placement="above"
        show-number="actual" show-type="both" type="start">...</tuplet>
    ```

MeasureExporter.unpitchedToXml(*up: [Unpitched](moduleNote.html#music21.note.Unpitched "music21.note.Unpitched")*, *noteIndexInChord: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*, *chordParent: [ChordBase](moduleChord.html#music21.chord.ChordBase "music21.chord.ChordBase") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")[[source]](../_modules/music21/musicxml/m21ToXml.html#MeasureExporter.unpitchedToXml)
:   Convert an [`Unpitched`](moduleNote.html#music21.note.Unpitched "music21.note.Unpitched") to a <note>
    with an <unpitched> subelement.

    ```python
    >>> up = note.Unpitched(displayName='D5')
    >>> MEX = musicxml.m21ToXml.MeasureExporter()
    >>> mxUnpitched = MEX.unpitchedToXml(up)
    >>> MEX.dump(mxUnpitched)
    <note>
      <unpitched>
        <display-step>D</display-step>
        <display-octave>5</display-octave>
      </unpitched>
      <duration>10080</duration>
      <type>quarter</type>
    </note>
    ```

    ```python
    >>> graceUp = up.getGrace()
    >>> mxUnpitched = MEX.unpitchedToXml(graceUp)
    >>> MEX.dump(mxUnpitched)
    <note>
      <grace slash="yes" />
      <unpitched>
        <display-step>D</display-step>
        <display-octave>5</display-octave>
      </unpitched>
      <type>quarter</type>
    </note>
    ```

MeasureExporter.wrapObjectInAttributes(*objectToWrap: [Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")*, *methodToMx: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")], [Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")]*) → [Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/musicxml/m21ToXml.html#MeasureExporter.wrapObjectInAttributes)
:   given a Clef, KeySignature, or TimeSignature which is in .elements and not m.clef,
    etc. insert it in self.xmlRoot as
    part of the current mxAttributes using methodToMx as a wrapper function.

    (or insert into a new mxAttributes if Clef/KeySignature/etc. is not at the beginning
    of the measure and not at the same point as an existing mxAttributes)

    ```python
    >>> MEX = musicxml.m21ToXml.MeasureExporter()
    >>> MEX.offsetInMeasure = 3.0
    >>> cl = clef.BassClef()
    >>> methodToMx = MEX.clefToXml
    >>> mxAttributes = MEX.wrapObjectInAttributes(cl, methodToMx)
    >>> MEX.dump(mxAttributes)
    <attributes>
      <clef>
        <sign>F</sign>
        <line>4</line>
      </clef>
    </attributes>
    ```

    Also puts it in MEX.xmlRoot.

    If offsetInMeasure is 0.0 then nothing is done or returned:

    ```python
    >>> MEX.offsetInMeasure = 0.0
    >>> nothing = MEX.wrapObjectInAttributes(cl, methodToMx)
    >>> nothing is None
    True
    ```

Methods inherited from [`XMLExporterBase`](#music21.musicxml.m21ToXml.XMLExporterBase "music21.musicxml.m21ToXml.XMLExporterBase"):

|  |  |  |
| --- | --- | --- |
| * [`accidentalToMx()`](#music21.musicxml.m21ToXml.XMLExporterBase.accidentalToMx "music21.musicxml.m21ToXml.XMLExporterBase.accidentalToMx") * [`accidentalToMxAccidentalMark()`](#music21.musicxml.m21ToXml.XMLExporterBase.accidentalToMxAccidentalMark "music21.musicxml.m21ToXml.XMLExporterBase.accidentalToMxAccidentalMark") * [`addDividerComment()`](#music21.musicxml.m21ToXml.XMLExporterBase.addDividerComment "music21.musicxml.m21ToXml.XMLExporterBase.addDividerComment") * [`asBytes()`](#music21.musicxml.m21ToXml.XMLExporterBase.asBytes "music21.musicxml.m21ToXml.XMLExporterBase.asBytes") * [`dump()`](#music21.musicxml.m21ToXml.XMLExporterBase.dump "music21.musicxml.m21ToXml.XMLExporterBase.dump") * [`pageLayoutToXmlPageLayout()`](#music21.musicxml.m21ToXml.XMLExporterBase.pageLayoutToXmlPageLayout "music21.musicxml.m21ToXml.XMLExporterBase.pageLayoutToXmlPageLayout") * [`pageLayoutToXmlPrint()`](#music21.musicxml.m21ToXml.XMLExporterBase.pageLayoutToXmlPrint "music21.musicxml.m21ToXml.XMLExporterBase.pageLayoutToXmlPrint") | * [`setColor()`](#music21.musicxml.m21ToXml.XMLExporterBase.setColor "music21.musicxml.m21ToXml.XMLExporterBase.setColor") * [`setEditorial()`](#music21.musicxml.m21ToXml.XMLExporterBase.setEditorial "music21.musicxml.m21ToXml.XMLExporterBase.setEditorial") * [`setFont()`](#music21.musicxml.m21ToXml.XMLExporterBase.setFont "music21.musicxml.m21ToXml.XMLExporterBase.setFont") * [`setPosition()`](#music21.musicxml.m21ToXml.XMLExporterBase.setPosition "music21.musicxml.m21ToXml.XMLExporterBase.setPosition") * [`setPrintObject()`](#music21.musicxml.m21ToXml.XMLExporterBase.setPrintObject "music21.musicxml.m21ToXml.XMLExporterBase.setPrintObject") * [`setPrintStyle()`](#music21.musicxml.m21ToXml.XMLExporterBase.setPrintStyle "music21.musicxml.m21ToXml.XMLExporterBase.setPrintStyle") * [`setPrintStyleAlign()`](#music21.musicxml.m21ToXml.XMLExporterBase.setPrintStyleAlign "music21.musicxml.m21ToXml.XMLExporterBase.setPrintStyleAlign") | * [`setStyleAttributes()`](#music21.musicxml.m21ToXml.XMLExporterBase.setStyleAttributes "music21.musicxml.m21ToXml.XMLExporterBase.setStyleAttributes") * [`setTextFormatting()`](#music21.musicxml.m21ToXml.XMLExporterBase.setTextFormatting "music21.musicxml.m21ToXml.XMLExporterBase.setTextFormatting") * [`staffLayoutToXmlStaffLayout()`](#music21.musicxml.m21ToXml.XMLExporterBase.staffLayoutToXmlStaffLayout "music21.musicxml.m21ToXml.XMLExporterBase.staffLayoutToXmlStaffLayout") * [`systemLayoutToXmlPrint()`](#music21.musicxml.m21ToXml.XMLExporterBase.systemLayoutToXmlPrint "music21.musicxml.m21ToXml.XMLExporterBase.systemLayoutToXmlPrint") * [`systemLayoutToXmlSystemLayout()`](#music21.musicxml.m21ToXml.XMLExporterBase.systemLayoutToXmlSystemLayout "music21.musicxml.m21ToXml.XMLExporterBase.systemLayoutToXmlSystemLayout") * [`xmlHeader()`](#music21.musicxml.m21ToXml.XMLExporterBase.xmlHeader "music21.musicxml.m21ToXml.XMLExporterBase.xmlHeader") |

## PartExporter

class music21.musicxml.m21ToXml.PartExporter(*partObj: [Part](moduleStreamBase.html#music21.stream.base.Part "music21.stream.base.Part") | [Score](moduleStreamBase.html#music21.stream.base.Score "music21.stream.base.Score") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *parent: [ScoreExporter](#music21.musicxml.m21ToXml.ScoreExporter "music21.musicxml.m21ToXml.ScoreExporter") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](../_modules/music21/musicxml/m21ToXml.html#PartExporter)
:   Object to convert one Part stream to a <part> tag on .parse()

[`PartExporter`](#music21.musicxml.m21ToXml.PartExporter "music21.musicxml.m21ToXml.PartExporter") bases

* [`XMLExporterBase`](#music21.musicxml.m21ToXml.XMLExporterBase "music21.musicxml.m21ToXml.XMLExporterBase")

[`PartExporter`](#music21.musicxml.m21ToXml.PartExporter "music21.musicxml.m21ToXml.PartExporter") methods

PartExporter.fixupNotationFlat()[[source]](../_modules/music21/musicxml/m21ToXml.html#PartExporter.fixupNotationFlat)
:   Runs makeNotation on a flatStream, such as one lacking measures.

PartExporter.fixupNotationMeasured()[[source]](../_modules/music21/musicxml/m21ToXml.html#PartExporter.fixupNotationMeasured)
:   Checks to see if there are any attributes in the part stream and moves
    them into the first measure if necessary.

    Checks if makeAccidentals is run, and haveBeamsBeenMade is done, and
    tuplets have been made.

    * Changed in v7: no longer accepts measureStream argument.

PartExporter.getXmlScorePart()[[source]](../_modules/music21/musicxml/m21ToXml.html#PartExporter.getXmlScorePart)
:   make a <score-part> from a music21 Part object and a parsed mxPart (<part>) element.

    contains details about instruments, etc.

    called directly by the ScoreExporter as a late part of the processing.

PartExporter.instrumentSetup()[[source]](../_modules/music21/musicxml/m21ToXml.html#PartExporter.instrumentSetup)
:   Sets self.instrumentStream and self.firstInstrumentObject for the stream,
    checks for a unique midiChannel and then blocks it off from future use.

    ```python
    >>> p = converter.parse('tinyNotation: 4/4 c1 d1 e1')
    >>> p.getElementsByClass(stream.Measure)[0].insert(0, instrument.Clarinet())
    >>> p.getElementsByClass(stream.Measure)[1].insert(0, instrument.BassClarinet())
    >>> PEX = musicxml.m21ToXml.PartExporter(p)
    >>> PEX.instrumentStream is None
    True
    >>> PEX.firstInstrumentObject is None
    True
    >>> PEX.instrumentSetup()
    >>> PEX.instrumentStream
    <music21.stream.Part 0x10ae02780>
    ```

    The “P” signifies that it is the main instrument associated with a Part.

    ```python
    >>> PEX.instrumentStream.show('text')
    {0.0} <music21.instrument.Clarinet 'P...: Clarinet'>
    {4.0} <music21.instrument.BassClarinet 'Bass clarinet'>
    ```

PartExporter.instrumentToXmlMidiInstrument(*i*)[[source]](../_modules/music21/musicxml/m21ToXml.html#PartExporter.instrumentToXmlMidiInstrument)
:   Convert an instrument object to a <midi-instrument> tag and return the element

    ```python
    >>> i = instrument.Clarinet()
    >>> i.instrumentId = 'clarinet1'
    >>> i.midiChannel = 4
    >>> PEX = musicxml.m21ToXml.PartExporter()
    >>> mxMidiInstrument = PEX.instrumentToXmlMidiInstrument(i)
    >>> PEX.dump(mxMidiInstrument)
    <midi-instrument id="clarinet1">
      <midi-channel>5</midi-channel>
      <midi-program>72</midi-program>
    </midi-instrument>
    ```

    ```python
    >>> m = instrument.Maracas()
    >>> m.instrumentId = 'my maracas'
    >>> m.midiChannel  # 0-indexed
    9
    >>> m.percMapPitch
    70
    >>> PEX = musicxml.m21ToXml.PartExporter()
    >>> mxMidiInstrument = PEX.instrumentToXmlMidiInstrument(m)
    >>> PEX.dump(mxMidiInstrument)  # 1-indexed in MusicXML
    <midi-instrument id="my maracas">
      <midi-channel>10</midi-channel>
      <midi-unpitched>71</midi-unpitched>
    </midi-instrument>
    ```

PartExporter.instrumentToXmlScoreInstrument(*i*)[[source]](../_modules/music21/musicxml/m21ToXml.html#PartExporter.instrumentToXmlScoreInstrument)
:   Convert an [`Instrument`](moduleInstrument.html#music21.instrument.Instrument "music21.instrument.Instrument") object to a
    <score-instrument> element and return it.

    ```python
    >>> i = instrument.Clarinet()
    >>> i.instrumentId = 'clarinet1'
    >>> i.midiChannel = 4
    >>> PEX = musicxml.m21ToXml.PartExporter()
    >>> mxScoreInstrument = PEX.instrumentToXmlScoreInstrument(i)
    >>> PEX.dump(mxScoreInstrument)
    <score-instrument id="clarinet1">
      <instrument-name>Clarinet</instrument-name>
      <instrument-abbreviation>Cl</instrument-abbreviation>
    </score-instrument>
    ```

    ```python
    >>> i.instrumentName = "Klarinette 1."
    >>> i.instrumentAbbreviation = 'Kl.1'
    >>> mxScoreInstrument = PEX.instrumentToXmlScoreInstrument(i)
    >>> PEX.dump(mxScoreInstrument)
    <score-instrument id="clarinet1">
      <instrument-name>Klarinette 1.</instrument-name>
      <instrument-abbreviation>Kl.1</instrument-abbreviation>
    </score-instrument>
    ```

PartExporter.mergeInstrumentStreamPartStaffAware() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/musicxml/m21ToXml.html#PartExporter.mergeInstrumentStreamPartStaffAware)
:   Merges instrument streams from subsequent parts in a PartStaff group.

    Does nothing in the normal case of single staves.

    Returns whether instrument processing should short circuit,
    which is False for the general case and True for subsequent
    PartStaff objects after the first in a group.

PartExporter.parse()[[source]](../_modules/music21/musicxml/m21ToXml.html#PartExporter.parse)
:   Set up instruments, convert sounding pitch to written pitch,
    create a partId (if no good one exists) and set it on
    <part>, fixes up the notation
    ([`fixupNotationFlat()`](#music21.musicxml.m21ToXml.PartExporter.fixupNotationFlat "music21.musicxml.m21ToXml.PartExporter.fixupNotationFlat") or [`fixupNotationMeasured()`](#music21.musicxml.m21ToXml.PartExporter.fixupNotationMeasured "music21.musicxml.m21ToXml.PartExporter.fixupNotationMeasured")),
    setIdLocals() on spanner bundle. Run parse() on each measure’s MeasureExporter and
    append the output to the <part> object.

    In other words, one-stop shopping.

    `makeNotation` when False, will avoid running
    [`makeNotation()`](moduleStreamBase.html#music21.stream.base.Stream.makeNotation "music21.stream.base.Stream.makeNotation")
    on the Part. Generally this attribute is set on GeneralObjectExporter
    or ScoreExporter and read from there. Running with makeNotation
    as False will raise MusicXMLExportException if no measures are present.
    If makeNotation is False, the transposition to written pitch is still
    performed and thus will be done in place.

    ```python
    >>> from music21.musicxml.m21ToXml import PartExporter
    >>> noMeasures = stream.Part(note.Note())
    >>> pex = PartExporter(noMeasures)
    >>> pex.makeNotation = False
    >>> pex.parse()
    Traceback (most recent call last):
    music21.musicxml.xmlObjects.MusicXMLExportException:
    Cannot export with makeNotation=False if there are no measures
    ```

Methods inherited from [`XMLExporterBase`](#music21.musicxml.m21ToXml.XMLExporterBase "music21.musicxml.m21ToXml.XMLExporterBase"):

|  |  |  |
| --- | --- | --- |
| * [`accidentalToMx()`](#music21.musicxml.m21ToXml.XMLExporterBase.accidentalToMx "music21.musicxml.m21ToXml.XMLExporterBase.accidentalToMx") * [`accidentalToMxAccidentalMark()`](#music21.musicxml.m21ToXml.XMLExporterBase.accidentalToMxAccidentalMark "music21.musicxml.m21ToXml.XMLExporterBase.accidentalToMxAccidentalMark") * [`addDividerComment()`](#music21.musicxml.m21ToXml.XMLExporterBase.addDividerComment "music21.musicxml.m21ToXml.XMLExporterBase.addDividerComment") * [`asBytes()`](#music21.musicxml.m21ToXml.XMLExporterBase.asBytes "music21.musicxml.m21ToXml.XMLExporterBase.asBytes") * [`dump()`](#music21.musicxml.m21ToXml.XMLExporterBase.dump "music21.musicxml.m21ToXml.XMLExporterBase.dump") * [`pageLayoutToXmlPageLayout()`](#music21.musicxml.m21ToXml.XMLExporterBase.pageLayoutToXmlPageLayout "music21.musicxml.m21ToXml.XMLExporterBase.pageLayoutToXmlPageLayout") * [`pageLayoutToXmlPrint()`](#music21.musicxml.m21ToXml.XMLExporterBase.pageLayoutToXmlPrint "music21.musicxml.m21ToXml.XMLExporterBase.pageLayoutToXmlPrint") | * [`setColor()`](#music21.musicxml.m21ToXml.XMLExporterBase.setColor "music21.musicxml.m21ToXml.XMLExporterBase.setColor") * [`setEditorial()`](#music21.musicxml.m21ToXml.XMLExporterBase.setEditorial "music21.musicxml.m21ToXml.XMLExporterBase.setEditorial") * [`setFont()`](#music21.musicxml.m21ToXml.XMLExporterBase.setFont "music21.musicxml.m21ToXml.XMLExporterBase.setFont") * [`setPosition()`](#music21.musicxml.m21ToXml.XMLExporterBase.setPosition "music21.musicxml.m21ToXml.XMLExporterBase.setPosition") * [`setPrintObject()`](#music21.musicxml.m21ToXml.XMLExporterBase.setPrintObject "music21.musicxml.m21ToXml.XMLExporterBase.setPrintObject") * [`setPrintStyle()`](#music21.musicxml.m21ToXml.XMLExporterBase.setPrintStyle "music21.musicxml.m21ToXml.XMLExporterBase.setPrintStyle") * [`setPrintStyleAlign()`](#music21.musicxml.m21ToXml.XMLExporterBase.setPrintStyleAlign "music21.musicxml.m21ToXml.XMLExporterBase.setPrintStyleAlign") | * [`setStyleAttributes()`](#music21.musicxml.m21ToXml.XMLExporterBase.setStyleAttributes "music21.musicxml.m21ToXml.XMLExporterBase.setStyleAttributes") * [`setTextFormatting()`](#music21.musicxml.m21ToXml.XMLExporterBase.setTextFormatting "music21.musicxml.m21ToXml.XMLExporterBase.setTextFormatting") * [`staffLayoutToXmlStaffLayout()`](#music21.musicxml.m21ToXml.XMLExporterBase.staffLayoutToXmlStaffLayout "music21.musicxml.m21ToXml.XMLExporterBase.staffLayoutToXmlStaffLayout") * [`systemLayoutToXmlPrint()`](#music21.musicxml.m21ToXml.XMLExporterBase.systemLayoutToXmlPrint "music21.musicxml.m21ToXml.XMLExporterBase.systemLayoutToXmlPrint") * [`systemLayoutToXmlSystemLayout()`](#music21.musicxml.m21ToXml.XMLExporterBase.systemLayoutToXmlSystemLayout "music21.musicxml.m21ToXml.XMLExporterBase.systemLayoutToXmlSystemLayout") * [`xmlHeader()`](#music21.musicxml.m21ToXml.XMLExporterBase.xmlHeader "music21.musicxml.m21ToXml.XMLExporterBase.xmlHeader") |

[`PartExporter`](#music21.musicxml.m21ToXml.PartExporter "music21.musicxml.m21ToXml.PartExporter") instance variables

PartExporter.previousPartStaffInGroup
:   If the part being exported is a [`PartStaff`](moduleStreamBase.html#music21.stream.base.PartStaff "music21.stream.base.PartStaff"),
    this attribute will be used to store the immediately previous PartStaff
    in the [`StaffGroup`](moduleLayout.html#music21.layout.StaffGroup "music21.layout.StaffGroup"), if any. (E.g. if this is
    the left hand, store a reference to the right hand.)

## ScoreExporter

class music21.musicxml.m21ToXml.ScoreExporter(*score: [Score](moduleStreamBase.html#music21.stream.base.Score "music21.stream.base.Score") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *makeNotation: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*)[[source]](../_modules/music21/musicxml/m21ToXml.html#ScoreExporter)
:   Convert a Score (or outer stream with .parts) into
    a musicxml Element.

[`ScoreExporter`](#music21.musicxml.m21ToXml.ScoreExporter "music21.musicxml.m21ToXml.ScoreExporter") bases

* [`XMLExporterBase`](#music21.musicxml.m21ToXml.XMLExporterBase "music21.musicxml.m21ToXml.XMLExporterBase")
* [`PartStaffExporterMixin`](moduleMusicxmlPartStaffExporter.html#music21.musicxml.partStaffExporter.PartStaffExporterMixin "music21.musicxml.partStaffExporter.PartStaffExporterMixin")

[`ScoreExporter`](#music21.musicxml.m21ToXml.ScoreExporter "music21.musicxml.m21ToXml.ScoreExporter") methods

ScoreExporter.addStyleToXmlDefaults(*mxDefaults*)[[source]](../_modules/music21/musicxml/m21ToXml.html#ScoreExporter.addStyleToXmlDefaults)
:   Optionally add an <appearance> tag (using styleToXmlAppearance)
    and <music-font>, <word-font>, zero or more <lyric-font> tags,
    and zero or more <lyric-language> tags to mxDefaults

    Demonstrating round tripping:

    ```python
    >>> import xml.etree.ElementTree as ET
    >>> defaults = ET.fromstring('<defaults>'
    ...          + '<music-font font-family="Maestro, Opus" font-weight="bold" />'
    ...          + '<word-font font-family="Garamond" font-style="italic" />'
    ...          + '<lyric-font name="verse" font-size="12" />'
    ...          + '<lyric-font name="chorus" font-size="14" />'
    ...          + '<lyric-language name="verse" xml:lang="fr" />'
    ...          + '<lyric-language name="chorus" xml:lang="en" />'
    ...          + '</defaults>')
    ```

    ```python
    >>> MI = musicxml.xmlToM21.MusicXMLImporter()
    >>> MI.styleFromXmlDefaults(defaults)
    >>> SX = musicxml.m21ToXml.ScoreExporter(MI.stream)
    >>> mxDefaults = ET.Element('defaults')
    >>> SX.addStyleToXmlDefaults(mxDefaults)
    >>> SX.dump(mxDefaults)
    <defaults>
        <music-font font-family="Maestro,Opus" font-weight="bold" />
        <word-font font-family="Garamond" font-style="italic" />
        <lyric-font font-size="12" name="verse" />
        <lyric-font font-size="14" name="chorus" />
        <lyric-language name="verse" xml:lang="fr" />
        <lyric-language name="chorus" xml:lang="en" />
    </defaults>
    ```

ScoreExporter.contributorToXmlCreator(*c*)[[source]](../_modules/music21/musicxml/m21ToXml.html#ScoreExporter.contributorToXmlCreator)
:   Return a <creator> tag from a `Contributor` object.

    ```python
    >>> md = metadata.Metadata()
    >>> md.composer = 'Oliveros, Pauline'
    >>> contrib = md.contributors[0]
    >>> contrib
    <music21.metadata.primitives.Contributor composer:Oliveros, Pauline>
    ```

    ```python
    >>> SX = musicxml.m21ToXml.ScoreExporter()
    >>> mxCreator = SX.contributorToXmlCreator(contrib)
    >>> SX.dump(mxCreator)
    <creator type="composer">Oliveros, Pauline</creator>
    ```

ScoreExporter.emptyObject() → [Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")[[source]](../_modules/music21/musicxml/m21ToXml.html#ScoreExporter.emptyObject)
:   Creates a cheeky “This Page Intentionally Left Blank” for a blank score

    ```python
    >>> emptySX = musicxml.m21ToXml.ScoreExporter()
    >>> mxScore = emptySX.parse()  # will call emptyObject
    >>> emptySX.dump(mxScore)
    <score-partwise version="...">
      <work>
        <work-title>This Page Intentionally Left Blank</work-title>
      </work>
      ...
          <note>
            <rest />
            <duration>40320</duration>
            <type>whole</type>
          </note>
        </measure>
      </part>
    </score-partwise>
    ```

ScoreExporter.getSupports() → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")][[source]](../_modules/music21/musicxml/m21ToXml.html#ScoreExporter.getSupports)
:   return a list of <supports> tags for what this supports. Does not append to
    mxEncoding itself.

    Currently just supports beam, stem, accidental, and
    print’s new-system if s.definesExplicitSystemBreaks is True
    and print’s new-page if s.definesExplicitPageBreaks is True.

    ```python
    >>> SX = musicxml.m21ToXml.ScoreExporter()
    >>> SX.getSupports()
    [<Element 'supports' at 0x...>,
     <Element 'supports' at 0x...>,
     <Element 'supports' at 0x...>]
    >>> for support in SX.getSupports():
    ...     SX.dump(support)
    <supports element="beam" type="yes" />
    <supports element="stem" type="yes" />
    <supports element="accidental" type="yes" />
    ```

    ```python
    >>> SX.stream.definesExplicitSystemBreaks = True
    >>> len(SX.getSupports())
    4
    >>> SX.dump(SX.getSupports()[-1])
    <supports attribute="new-system" element="print" type="yes" value="yes" />
    ```

    ```python
    >>> SX.stream.definesExplicitPageBreaks = True
    >>> SX.dump(SX.getSupports()[-1])
    <supports attribute="new-page" element="print" type="yes" value="yes" />
    ```

ScoreExporter.metadataToMiscellaneous(*md: [Metadata](moduleMetadata.html#music21.metadata.Metadata "music21.metadata.Metadata") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/musicxml/m21ToXml.html#ScoreExporter.metadataToMiscellaneous)
:   Returns an mxMiscellaneous of information from metadata object md or
    from self.scoreMetadata if md is None. If the mxMiscellaneous object
    has any miscellaneous-fields, then it is appended to self.mxIdentification
    if it exists.

    ```python
    >>> SX = musicxml.m21ToXml.ScoreExporter()
    >>> md = metadata.Metadata()
    >>> md.date = metadata.primitives.DateRelative('1689', 'onOrBefore')
    >>> md.localeOfComposition = 'Rome'
    ```

    ```python
    >>> mxMisc = SX.metadataToMiscellaneous(md)
    >>> SX.dump(mxMisc)
    <miscellaneous>
      <miscellaneous-field name="dcterms:created">1689/--/-- or earlier</miscellaneous-field>
      <miscellaneous-field name="humdrum:OPC">Rome</miscellaneous-field>
    </miscellaneous>
    ```

ScoreExporter.parse() → [Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")[[source]](../_modules/music21/musicxml/m21ToXml.html#ScoreExporter.parse)
:   the main function to call.

    If self.stream is empty, call self.emptyObject(). Otherwise,
    convert sounding to written pitch,
    set scorePreliminaries(), call parsePartlikeScore or parseFlatScore, then postPartProcess(),
    clean up circular references for garbage collection, and returns the <score-partwise>
    object.

    ```python
    >>> b = corpus.parse('bwv66.6')
    >>> SX = musicxml.m21ToXml.ScoreExporter(b)
    >>> mxScore = SX.parse()
    >>> SX.dump(mxScore)
    <score-partwise version="...">...</score-partwise>
    ```

ScoreExporter.parseFlatScore() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/musicxml/m21ToXml.html#ScoreExporter.parseFlatScore)
:   creates a single PartExporter for this Stream and parses it.

    Note that the Score does not need to be totally flat, it just cannot have Parts inside it;
    measures are fine.

    ```python
    >>> c = converter.parse('tinyNotation: 3/4 c2. d e')
    >>> SX = musicxml.m21ToXml.ScoreExporter(c)
    >>> SX.parseFlatScore()
    >>> len(SX.partExporterList)
    1
    >>> SX.partExporterList[0]
    <music21.musicxml.m21ToXml.PartExporter object at 0x...>
    >>> SX.dump(SX.partExporterList[0].xmlRoot)
    <part id="...">
      <!--========================= Measure 1 ==========================-->
      <measure implicit="no" number="1">...</measure>
    </part>
    >>> del SX.partExporterList[:]  # for garbage collection
    ```

ScoreExporter.parsePartlikeScore() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/musicxml/m21ToXml.html#ScoreExporter.parsePartlikeScore)
:   Called by .parse() if the score has individual parts.
    Creates a PartExporter for each part, and runs .parse() on that part.
    Appends the PartExporter to self.partExporterList
    and runs .parse() on that part. Appends the PartExporter to self.

ScoreExporter.postPartProcess() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/musicxml/m21ToXml.html#ScoreExporter.postPartProcess)
:   calls .joinPartStaffs() from the
    [`PartStaffExporterMixin`](moduleMusicxmlPartStaffExporter.html#music21.musicxml.partStaffExporter.PartStaffExporterMixin "music21.musicxml.partStaffExporter.PartStaffExporterMixin"),
    then calls .setScoreHeader(),
    then appends each PartExporter’s xmlRoot from
    self.partExporterList to self.xmlRoot.

    Called automatically by .parse().

ScoreExporter.renumberVoicesWithinStaffGroups() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/musicxml/m21ToXml.html#ScoreExporter.renumberVoicesWithinStaffGroups)
:   Renumbers voices (as appropriate) in each StaffGroup, so that
    voices have unique numbers across the entire group.

    Called automatically by .parse()

ScoreExporter.scorePreliminaries() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/musicxml/m21ToXml.html#ScoreExporter.scorePreliminaries)
:   Populate the exporter object with
    meterStream, scoreLayouts, spannerBundle, and textBoxes

    ```python
    >>> emptySX = musicxml.m21ToXml.ScoreExporter()
    >>> emptySX.scorePreliminaries()  # will call emptyObject
    >>> len(emptySX.textBoxes)
    0
    >>> emptySX.spannerBundle
    <music21.spanner.SpannerBundle of size 0>
    ```

ScoreExporter.setDefaults()[[source]](../_modules/music21/musicxml/m21ToXml.html#ScoreExporter.setDefaults)
:   Returns a default object from self.firstScoreLayout or a very simple one if none exists.

    Simple:

    ```python
    >>> SX = musicxml.m21ToXml.ScoreExporter()
    >>> mxDefaults = SX.setDefaults()
    >>> SX.dump(mxDefaults)
    <defaults>
      <scaling>
        <millimeters>7</millimeters>
        <tenths>40</tenths>
      </scaling>
    </defaults>
    ```

    These numbers come from the defaults module:

    ```python
    >>> defaults.scalingMillimeters
    7
    >>> defaults.scalingTenths
    40
    ```

    More complex:

    ```python
    >>> s = corpus.parse('schoenberg/opus19', 2)
    >>> SX = musicxml.m21ToXml.ScoreExporter(s)
    >>> SX.setScoreLayouts()  # necessary to call before .setDefaults()
    >>> mxDefaults = SX.setDefaults()
    >>> mxDefaults.tag
    'defaults'
    >>> mxScaling = mxDefaults.find('scaling')
    >>> SX.dump(mxScaling)
    <scaling>
      <millimeters>6.1472</millimeters>
      <tenths>40</tenths>
    </scaling>
    ```

    ```python
    >>> mxPageLayout = mxDefaults.find('page-layout')
    >>> SX.dump(mxPageLayout)
    <page-layout>
      <page-height>1818</page-height>
      <page-width>1405</page-width>
      <page-margins>
        <left-margin>83</left-margin>
        <right-margin>83</right-margin>
        <top-margin>103</top-margin>
        <bottom-margin>103</bottom-margin>
      </page-margins>
    </page-layout>
    ```

    ```python
    >>> mxSystemLayout = mxDefaults.find('system-layout')
    >>> SX.dump(mxSystemLayout)
    <system-layout>
      <system-margins>
        <left-margin>0</left-margin>
        <right-margin>0</right-margin>
      </system-margins>
      <system-distance>121</system-distance>
      <top-system-distance>70</top-system-distance>
    </system-layout>
    ```

    ```python
    >>> mxStaffLayoutList = mxDefaults.findall('staff-layout')
    >>> len(mxStaffLayoutList)
    1
    >>> SX.dump(mxStaffLayoutList[0])
    <staff-layout>
      <staff-distance>98</staff-distance>
    </staff-layout>
    ```

ScoreExporter.setEncoding()[[source]](../_modules/music21/musicxml/m21ToXml.html#ScoreExporter.setEncoding)
:   Returns an encoding object that might have information about <supports> also.
    and appends to mxIdentification (if any)

    Will use the date of generation as encoding-date.

    ```python
    >>> SX = musicxml.m21ToXml.ScoreExporter()
    >>> mxEncoding = SX.setEncoding()
    >>> SX.dump(mxEncoding)
    <encoding>
      <encoding-date>20...-...-...</encoding-date>
      <software>music21 v...</software>
      <supports element="beam" type="yes" />
      <supports element="stem" type="yes" />
      <supports element="accidental" type="yes" />
    </encoding>
    ```

    Encoding-date is in YYYY-MM-DD format.

ScoreExporter.setIdentification() → [Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")[[source]](../_modules/music21/musicxml/m21ToXml.html#ScoreExporter.setIdentification)
:   Returns an identification object from self.scoreMetadata and appends it to the score.

    For defaults:

    ```python
    >>> SX = musicxml.m21ToXml.ScoreExporter()
    >>> mxIdentification = SX.setIdentification()
    >>> SX.dump(mxIdentification)
    <identification>
      <creator type="composer">Music21</creator>
      <encoding>
        <encoding-date>20...-...-...</encoding-date>
        <software>music21 v...</software>
        <supports element="beam" type="yes" />
        <supports element="stem" type="yes" />
        <supports element="accidental" type="yes" />
      </encoding>
    </identification>
    ```

    More realistic:

    ```python
    >>> md = metadata.Metadata()
    >>> md.composer = 'Francesca Caccini'
    >>> c = metadata.Contributor(role='arranger', name='Aliyah Shanti')
    >>> md.addContributor(c)
    ```

    Need a fresh ScoreExporter, or, it will otherwise append to the existing mxIdentification

    ```python
    >>> SX = musicxml.m21ToXml.ScoreExporter()
    >>> SX.scoreMetadata = md
    >>> mxIdentification = SX.setIdentification()
    >>> SX.dump(mxIdentification)
    <identification>
      <creator type="composer">Francesca Caccini</creator>
      <creator type="arranger">Aliyah Shanti</creator>
      <encoding>
        <encoding-date>...</encoding-date>
        <software>music21 v...</software>
        <supports element="beam" type="yes" />
        <supports element="stem" type="yes" />
        <supports element="accidental" type="yes" />
      </encoding>
    </identification>
    ```

    Overriding the default:

    ```python
    >>> defaults.author = "Batch Conversion March 2022"
    >>> SX = musicxml.m21ToXml.ScoreExporter()
    >>> mxIdentification = SX.setIdentification()
    >>> SX.dump(mxIdentification)
    <identification>
      <creator type="composer">Batch Conversion March 2022</creator>
      <encoding>
        <encoding-date>20...-...-...</encoding-date>
        <software>music21 v...</software>
        <supports element="beam" type="yes" />
        <supports element="stem" type="yes" />
        <supports element="accidental" type="yes" />
      </encoding>
    </identification>
    ```

ScoreExporter.setMeterStream() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/musicxml/m21ToXml.html#ScoreExporter.setMeterStream)
:   sets self.meterStream or uses a default.

    Used in makeNotation in Part later.

    ```python
    >>> b = corpus.parse('bwv66.6')
    >>> SX = musicxml.m21ToXml.ScoreExporter(b)
    >>> SX.setMeterStream()
    >>> SX.meterStream
    <music21.stream.Score bach/bwv66.6.mxl>
    >>> len(SX.meterStream)
    4
    >>> SX.meterStream[0]
    <music21.meter.TimeSignature 4/4>
    ```

ScoreExporter.setPartExporterStaffGroups() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/musicxml/m21ToXml.html#ScoreExporter.setPartExporterStaffGroups)
:   Figures out the containing StaffGroup for every PartExporter that has one.

    Called automatically by .parse()

ScoreExporter.setPartList()[[source]](../_modules/music21/musicxml/m21ToXml.html#ScoreExporter.setPartList)
:   Returns a <part-list> and appends it to self.xmlRoot.

    This is harder than it looks because MusicXML and music21’s idea of where to store
    staff-groups are quite different.

    We find each stream in self.partExporterList, then look at the StaffGroup spanners in
    self.spannerBundle. If the part is the first element in a StaffGroup then we add a
    <staff-group> object with ‘start’ as the starting point (and same for multiple StaffGroups)
    this is in staffGroupToXmlPartGroup(sg).
    then we add the <score-part> descriptor of the part and its instruments, etc. (currently
    just one!), then we iterate again through all StaffGroups and if this part is the last
    element in a StaffGroup we add a <staff-group> descriptor with type=”stop”.

    This Bach example has four parts and one staff-group bracket linking them:

    ```python
    >>> b = corpus.parse('bwv66.6')
    >>> SX = musicxml.m21ToXml.ScoreExporter(b)
    ```

    Needs some strange setup to make this work in a demo. .parse() takes care of all this.

    ```python
    >>> SX.scorePreliminaries()
    >>> SX.parsePartlikeScore()
    ```

    ```python
    >>> mxPartList = SX.setPartList()
    >>> SX.dump(mxPartList)
    <part-list>
      <part-group number="1" type="start">...
      <score-part id="P1">...
      <score-part id="P2">...
      <score-part id="P3">...
      <score-part id="P4">...
      <part-group number="1" type="stop" />
    </part-list>
    ```

    Multi-staff parts (such as piano staves), should NOT receive <part-group> tags,
    since they are joined by <staff> tags:

    ```python
    >>> cpe = corpus.parse('cpebach')
    >>> SX = musicxml.m21ToXml.ScoreExporter(cpe)
    >>> SX.scorePreliminaries()
    >>> SX.parsePartlikeScore()
    >>> SX.joinPartStaffs()
    ```

    ```python
    >>> mxPartList = SX.setPartList()
    >>> SX.dump(mxPartList)
    <part-list>
      <score-part id="P1">...
      </score-part>
    </part-list>
    ```

ScoreExporter.setPartsAndRefStream() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/musicxml/m21ToXml.html#ScoreExporter.setPartsAndRefStream)
:   Transfers the offset of the inner stream to elements and sets self.highestTime

    ```python
    >>> b = corpus.parse('bwv66.6')
    >>> SX = musicxml.m21ToXml.ScoreExporter(b)
    >>> SX.highestTime
    0.0
    >>> SX.setPartsAndRefStream()
    >>> SX.highestTime
    36.0
    >>> SX.refStreamOrTimeRange
    [0.0, 36.0]
    >>> len(SX.parts)
    4
    >>> isinstance(SX.parts[0], stream.Part)
    True
    ```

    ```python
    >>> b.insert(stream.Score())
    >>> SX = musicxml.m21ToXml.ScoreExporter(b)
    >>> SX.setPartsAndRefStream()
    Traceback (most recent call last):
    music21.musicxml.xmlObjects.MusicXMLExportException:
    Exporting scores nested inside scores is not supported
    ```

ScoreExporter.setScoreHeader() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/musicxml/m21ToXml.html#ScoreExporter.setScoreHeader)
:   Sets the group score-header in <score-partwise>. Note that score-header is not
    a separate tag, but just a way of grouping things from the tag.

    runs setTitles(), setIdentification(), setDefaults(), changes textBoxes
    to <credit> and does the major task of setting up the part-list with setPartList().

ScoreExporter.setScoreLayouts() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/musicxml/m21ToXml.html#ScoreExporter.setScoreLayouts)
:   sets self.scoreLayouts and self.firstScoreLayout

    ```python
    >>> b = corpus.parse('schoenberg/opus19', 2)
    >>> SX = musicxml.m21ToXml.ScoreExporter(b)
    >>> SX.setScoreLayouts()
    >>> SX.scoreLayouts
    [<music21.layout.ScoreLayout>]
    >>> len(SX.scoreLayouts)
    1
    >>> SX.firstScoreLayout
    <music21.layout.ScoreLayout>
    ```

ScoreExporter.setTitles() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/musicxml/m21ToXml.html#ScoreExporter.setTitles)
:   puts work (with work-title), movement-number, movement-title into the self.xmlRoot

ScoreExporter.staffGroupToXmlPartGroup(*staffGroup*)[[source]](../_modules/music21/musicxml/m21ToXml.html#ScoreExporter.staffGroupToXmlPartGroup)
:   Create and configure an mxPartGroup object for the ‘start’ tag
    from a staff group spanner. Note that this object
    is not completely formed by this procedure (number isn’t done).

    ```python
    >>> b = corpus.parse('bwv66.6')
    >>> SX = musicxml.m21ToXml.ScoreExporter(b)
    >>> firstStaffGroup = b.spannerBundle.getByClass(layout.StaffGroup)[0]
    >>> mxPartGroup = SX.staffGroupToXmlPartGroup(firstStaffGroup)
    >>> SX.dump(mxPartGroup)
    <part-group type="start">
      <group-symbol>bracket</group-symbol>
      <group-barline>yes</group-barline>
    </part-group>
    ```

    At this point, you should set the number of the mxPartGroup, since it is required:

    ```python
    >>> mxPartGroup.set('number', str(1))
    ```

    What can we do with it?

    ```python
    >>> firstStaffGroup.name = 'Voices'
    >>> firstStaffGroup.abbreviation = 'Ch.'
    >>> firstStaffGroup.symbol = 'brace' # 'none', 'brace', 'line', 'bracket', 'square'
    >>> firstStaffGroup.barTogether = False  # True, False, or 'Mensurstrich'
    >>> mxPartGroup = SX.staffGroupToXmlPartGroup(firstStaffGroup)
    >>> SX.dump(mxPartGroup)
    <part-group type="start">
      <group-name>Voices</group-name>
      <group-abbreviation>Ch.</group-abbreviation>
      <group-symbol>brace</group-symbol>
      <group-barline>no</group-barline>
    </part-group>
    ```

    Now we avoid printing the name of the group:

    ```python
    >>> firstStaffGroup.style.hideObjectOnPrint = True
    >>> mxPartGroup = SX.staffGroupToXmlPartGroup(firstStaffGroup)
    >>> SX.dump(mxPartGroup)
    <part-group type="start">
      <group-name>Voices</group-name>
      <group-name-display print-object="no" />
      <group-abbreviation>Ch.</group-abbreviation>
      <group-symbol>brace</group-symbol>
      <group-barline>no</group-barline>
    </part-group>
    ```

ScoreExporter.styleToXmlAppearance()[[source]](../_modules/music21/musicxml/m21ToXml.html#ScoreExporter.styleToXmlAppearance)
:   Populates the <appearance> tag of the <defaults> with
    information from the stream’s .style information.

    ```python
    >>> s = stream.Score()
    >>> s.style.lineWidths.append(('beam', 5.0))
    >>> s.style.noteSizes.append(('cue', 75))
    >>> s.style.distances.append(('hyphen', 0.1))
    >>> s.style.otherAppearances.append(('flags', 'wavy'))
    >>> SX = musicxml.m21ToXml.ScoreExporter(s)
    >>> mxAppearance = SX.styleToXmlAppearance()
    >>> SX.dump(mxAppearance)
    <appearance>
      <line-width type="beam">5.0</line-width>
      <note-size type="cue">75</note-size>
      <distance type="hyphen">0.1</distance>
      <other-appearance type="flags">wavy</other-appearance>
    </appearance>
    ```

ScoreExporter.textBoxToXmlCredit(*textBox: [TextBox](moduleText.html#music21.text.TextBox "music21.text.TextBox")*) → [Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")[[source]](../_modules/music21/musicxml/m21ToXml.html#ScoreExporter.textBoxToXmlCredit)
:   Convert a music21 TextBox to a MusicXML Credit.

    ```python
    >>> tb = text.TextBox('testing')
    >>> tb.style.absoluteY = 400
    >>> tb.style.absoluteX = 300
    >>> tb.page = 3
    >>> SX = musicxml.m21ToXml.ScoreExporter()
    >>> mxCredit = SX.textBoxToXmlCredit(tb)
    >>> SX.dump(mxCredit)
    <credit page="3">
      <credit-words default-x="300" default-y="400"
           halign="center" valign="top">testing</credit-words>
    </credit>
    ```

    Default of page 1:

    ```python
    >>> tb = text.TextBox('testing')
    >>> tb.page
    1
    >>> mxCredit = SX.textBoxToXmlCredit(tb)
    >>> SX.dump(mxCredit)
    <credit page="1">...</credit>
    ```

    * Changed in v8: Multi-line text now exports as one <credit-words>
      element (preserving newlines).

    ```python
    >>> tb = text.TextBox('Snare\nCymbals')
    >>> mxCredit = SX.textBoxToXmlCredit(tb)
    >>> SX.dump(mxCredit)
    <credit page="1">
        <credit-words default-x="500" default-y="500" halign="center" valign="top"
        xml:space="preserve">Snare
        Cymbals</credit-words>
    </credit>
    ```

Methods inherited from [`XMLExporterBase`](#music21.musicxml.m21ToXml.XMLExporterBase "music21.musicxml.m21ToXml.XMLExporterBase"):

|  |  |  |
| --- | --- | --- |
| * [`accidentalToMx()`](#music21.musicxml.m21ToXml.XMLExporterBase.accidentalToMx "music21.musicxml.m21ToXml.XMLExporterBase.accidentalToMx") * [`accidentalToMxAccidentalMark()`](#music21.musicxml.m21ToXml.XMLExporterBase.accidentalToMxAccidentalMark "music21.musicxml.m21ToXml.XMLExporterBase.accidentalToMxAccidentalMark") * [`addDividerComment()`](#music21.musicxml.m21ToXml.XMLExporterBase.addDividerComment "music21.musicxml.m21ToXml.XMLExporterBase.addDividerComment") * [`asBytes()`](#music21.musicxml.m21ToXml.XMLExporterBase.asBytes "music21.musicxml.m21ToXml.XMLExporterBase.asBytes") * [`dump()`](#music21.musicxml.m21ToXml.XMLExporterBase.dump "music21.musicxml.m21ToXml.XMLExporterBase.dump") * [`pageLayoutToXmlPageLayout()`](#music21.musicxml.m21ToXml.XMLExporterBase.pageLayoutToXmlPageLayout "music21.musicxml.m21ToXml.XMLExporterBase.pageLayoutToXmlPageLayout") * [`pageLayoutToXmlPrint()`](#music21.musicxml.m21ToXml.XMLExporterBase.pageLayoutToXmlPrint "music21.musicxml.m21ToXml.XMLExporterBase.pageLayoutToXmlPrint") | * [`setColor()`](#music21.musicxml.m21ToXml.XMLExporterBase.setColor "music21.musicxml.m21ToXml.XMLExporterBase.setColor") * [`setEditorial()`](#music21.musicxml.m21ToXml.XMLExporterBase.setEditorial "music21.musicxml.m21ToXml.XMLExporterBase.setEditorial") * [`setFont()`](#music21.musicxml.m21ToXml.XMLExporterBase.setFont "music21.musicxml.m21ToXml.XMLExporterBase.setFont") * [`setPosition()`](#music21.musicxml.m21ToXml.XMLExporterBase.setPosition "music21.musicxml.m21ToXml.XMLExporterBase.setPosition") * [`setPrintObject()`](#music21.musicxml.m21ToXml.XMLExporterBase.setPrintObject "music21.musicxml.m21ToXml.XMLExporterBase.setPrintObject") * [`setPrintStyle()`](#music21.musicxml.m21ToXml.XMLExporterBase.setPrintStyle "music21.musicxml.m21ToXml.XMLExporterBase.setPrintStyle") * [`setPrintStyleAlign()`](#music21.musicxml.m21ToXml.XMLExporterBase.setPrintStyleAlign "music21.musicxml.m21ToXml.XMLExporterBase.setPrintStyleAlign") | * [`setStyleAttributes()`](#music21.musicxml.m21ToXml.XMLExporterBase.setStyleAttributes "music21.musicxml.m21ToXml.XMLExporterBase.setStyleAttributes") * [`setTextFormatting()`](#music21.musicxml.m21ToXml.XMLExporterBase.setTextFormatting "music21.musicxml.m21ToXml.XMLExporterBase.setTextFormatting") * [`staffLayoutToXmlStaffLayout()`](#music21.musicxml.m21ToXml.XMLExporterBase.staffLayoutToXmlStaffLayout "music21.musicxml.m21ToXml.XMLExporterBase.staffLayoutToXmlStaffLayout") * [`systemLayoutToXmlPrint()`](#music21.musicxml.m21ToXml.XMLExporterBase.systemLayoutToXmlPrint "music21.musicxml.m21ToXml.XMLExporterBase.systemLayoutToXmlPrint") * [`systemLayoutToXmlSystemLayout()`](#music21.musicxml.m21ToXml.XMLExporterBase.systemLayoutToXmlSystemLayout "music21.musicxml.m21ToXml.XMLExporterBase.systemLayoutToXmlSystemLayout") * [`xmlHeader()`](#music21.musicxml.m21ToXml.XMLExporterBase.xmlHeader "music21.musicxml.m21ToXml.XMLExporterBase.xmlHeader") |

Methods inherited from [`PartStaffExporterMixin`](moduleMusicxmlPartStaffExporter.html#music21.musicxml.partStaffExporter.PartStaffExporterMixin "music21.musicxml.partStaffExporter.PartStaffExporterMixin"):

|  |  |  |
| --- | --- | --- |
| * [`addStaffTagsMultiStaffParts()`](moduleMusicxmlPartStaffExporter.html#music21.musicxml.partStaffExporter.PartStaffExporterMixin.addStaffTagsMultiStaffParts "music21.musicxml.partStaffExporter.PartStaffExporterMixin.addStaffTagsMultiStaffParts") * [`cleanUpSubsequentPartStaffs()`](moduleMusicxmlPartStaffExporter.html#music21.musicxml.partStaffExporter.PartStaffExporterMixin.cleanUpSubsequentPartStaffs "music21.musicxml.partStaffExporter.PartStaffExporterMixin.cleanUpSubsequentPartStaffs") * [`getRootForPartStaff()`](moduleMusicxmlPartStaffExporter.html#music21.musicxml.partStaffExporter.PartStaffExporterMixin.getRootForPartStaff "music21.musicxml.partStaffExporter.PartStaffExporterMixin.getRootForPartStaff") | * [`joinPartStaffs()`](moduleMusicxmlPartStaffExporter.html#music21.musicxml.partStaffExporter.PartStaffExporterMixin.joinPartStaffs "music21.musicxml.partStaffExporter.PartStaffExporterMixin.joinPartStaffs") * [`joinableGroups()`](moduleMusicxmlPartStaffExporter.html#music21.musicxml.partStaffExporter.PartStaffExporterMixin.joinableGroups "music21.musicxml.partStaffExporter.PartStaffExporterMixin.joinableGroups") * [`moveMeasureContents()`](moduleMusicxmlPartStaffExporter.html#music21.musicxml.partStaffExporter.PartStaffExporterMixin.moveMeasureContents "music21.musicxml.partStaffExporter.PartStaffExporterMixin.moveMeasureContents") | * [`movePartStaffMeasureContents()`](moduleMusicxmlPartStaffExporter.html#music21.musicxml.partStaffExporter.PartStaffExporterMixin.movePartStaffMeasureContents "music21.musicxml.partStaffExporter.PartStaffExporterMixin.movePartStaffMeasureContents") * [`processSubsequentPartStaff()`](moduleMusicxmlPartStaffExporter.html#music21.musicxml.partStaffExporter.PartStaffExporterMixin.processSubsequentPartStaff "music21.musicxml.partStaffExporter.PartStaffExporterMixin.processSubsequentPartStaff") * [`setEarliestAttributesAndClefsPartStaff()`](moduleMusicxmlPartStaffExporter.html#music21.musicxml.partStaffExporter.PartStaffExporterMixin.setEarliestAttributesAndClefsPartStaff "music21.musicxml.partStaffExporter.PartStaffExporterMixin.setEarliestAttributesAndClefsPartStaff") |

## XMLExporterBase

class music21.musicxml.m21ToXml.XMLExporterBase[[source]](../_modules/music21/musicxml/m21ToXml.html#XMLExporterBase)
:   contains functions that could be called
    at multiple levels of exporting (Score, Part, Measure).

[`XMLExporterBase`](#music21.musicxml.m21ToXml.XMLExporterBase "music21.musicxml.m21ToXml.XMLExporterBase") methods

XMLExporterBase.accidentalToMx(*a: [Accidental](modulePitch.html#music21.pitch.Accidental "music21.pitch.Accidental")*, *\**, *elName: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = 'accidental'*) → [Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")[[source]](../_modules/music21/musicxml/m21ToXml.html#XMLExporterBase.accidentalToMx)
:   Convert a pitch.Accidental object to a Element of tag ‘accidental’ (or other name)

    ```python
    >>> acc = pitch.Accidental()
    >>> acc.set('half-sharp')
    >>> acc.alter == 0.5
    True
    ```

    ```python
    >>> XB = musicxml.m21ToXml.XMLExporterBase()
    >>> a2m = XB.accidentalToMx
    >>> XB.dump(a2m(acc))
    <accidental>quarter-sharp</accidental>
    ```

    ```python
    >>> acc.set('double-flat')
    >>> XB.dump(a2m(acc))
    <accidental>flat-flat</accidental>
    ```

    ```python
    >>> acc.set('one-and-a-half-sharp')
    >>> XB.dump(a2m(acc, elName='accidental-mark'))
    <accidental-mark>three-quarters-sharp</accidental-mark>
    ```

    ```python
    >>> acc.set('half-flat')
    >>> XB.dump(a2m(acc))
    <accidental>quarter-flat</accidental>
    ```

    ```python
    >>> acc.set('one-and-a-half-flat')
    >>> XB.dump(a2m(acc))
    <accidental>three-quarters-flat</accidental>
    ```

    ```python
    >>> acc.set('sharp')
    >>> acc.displayStyle = 'parentheses'
    >>> XB.dump(a2m(acc))
    <accidental parentheses="yes">sharp</accidental>
    ```

    ```python
    >>> acc.displayStyle = 'bracket'
    >>> XB.dump(a2m(acc))
    <accidental bracket="yes">sharp</accidental>
    ```

    ```python
    >>> acc.displayStyle = 'both'
    >>> XB.dump(a2m(acc))
    <accidental bracket="yes" parentheses="yes">sharp</accidental>
    ```

    ```python
    >>> acc = pitch.Accidental('flat')
    >>> acc.style.relativeX = -2
    >>> XB.dump(a2m(acc))
    <accidental relative-x="-2">flat</accidental>
    ```

    ```python
    >>> acc = pitch.Accidental()
    >>> acc.name = 'double-sharp-down'  # musicxml 3.1
    >>> XB.dump(a2m(acc))
    <accidental>double-sharp-down</accidental>
    ```

    ```python
    >>> acc.name = 'funnyAccidental'  # unknown
    >>> XB.dump(a2m(acc))
    <accidental>other</accidental>
    ```

XMLExporterBase.accidentalToMxAccidentalMark(*a: [Accidental](modulePitch.html#music21.pitch.Accidental "music21.pitch.Accidental")*) → [Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")[[source]](../_modules/music21/musicxml/m21ToXml.html#XMLExporterBase.accidentalToMxAccidentalMark)

XMLExporterBase.addDividerComment(*comment: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/musicxml/m21ToXml.html#XMLExporterBase.addDividerComment)
:   Add a divider to xmlRoot.

    ```python
    >>> from xml.etree.ElementTree import Element
    >>> e1 = Element('accidental')
    >>> e2 = Element('accidental')
    ```

    ```python
    >>> XB = musicxml.m21ToXml.ScoreExporter()
    >>> XB.xmlRoot.append(e1)
    >>> XB.addDividerComment('second accidental below')
    >>> XB.xmlRoot.append(e2)
    >>> XB.dump(XB.xmlRoot)
    <score-partwise version="...">
      <accidental />
      <!--================== second accidental below ===================-->
      <accidental />
      </score-partwise>
    ```

XMLExporterBase.asBytes(*noCopy=True*) → [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")[[source]](../_modules/music21/musicxml/m21ToXml.html#XMLExporterBase.asBytes)
:   returns the xmlRoot as a bytes object. If noCopy is True
    (default), modifies the file for pretty-printing in place. Otherwise,
    make a copy.

static XMLExporterBase.dump(*obj*)[[source]](../_modules/music21/musicxml/m21ToXml.html#XMLExporterBase.dump)

XMLExporterBase.pageLayoutToXmlPageLayout(*pageLayout*, *mxPageLayoutIn=None*)[[source]](../_modules/music21/musicxml/m21ToXml.html#XMLExporterBase.pageLayoutToXmlPageLayout)
:   get a <page-layout> element from a PageLayout

    Called out from pageLayoutToXmlPrint because it
    is also used in the <defaults> tag

XMLExporterBase.pageLayoutToXmlPrint(*pageLayout*, *mxPrintIn=None*)[[source]](../_modules/music21/musicxml/m21ToXml.html#XMLExporterBase.pageLayoutToXmlPrint)
:   Given a PageLayout object, set object data for <print>

    ```python
    >>> pl = layout.PageLayout()
    >>> pl.pageHeight = 4000
    >>> pl.isNew = True
    >>> pl.rightMargin = 30.25
    >>> pl.leftMargin = 20
    >>> pl.pageNumber = 5
    ```

    ```python
    >>> XPBase = musicxml.m21ToXml.XMLExporterBase()
    >>> mxPrint = XPBase.pageLayoutToXmlPrint(pl)
    >>> XPBase.dump(mxPrint)
    <print new-page="yes" page-number="5">
      <page-layout>
        <page-height>4000</page-height>
        <page-margins>
          <left-margin>20</left-margin>
          <right-margin>30.25</right-margin>
        </page-margins>
      </page-layout>
    </print>
    ```

    ```python
    >>> MP = musicxml.xmlToM21.MeasureParser()
    >>> pl2 = MP.xmlPrintToPageLayout(mxPrint)
    >>> pl2.isNew
    True
    >>> pl2.rightMargin
    30.25
    >>> pl2.leftMargin
    20
    >>> pl2.pageNumber
    5
    >>> pl2.pageHeight
    4000
    ```

XMLExporterBase.setColor(*mxObject*, *m21Object*)[[source]](../_modules/music21/musicxml/m21ToXml.html#XMLExporterBase.setColor)
:   Sets mxObject[‘color’] to a normalized version of m21Object.style.color

XMLExporterBase.setEditorial(*mxObject*, *m21Object*)[[source]](../_modules/music21/musicxml/m21ToXml.html#XMLExporterBase.setEditorial)
:   ```python
    >>> from xml.etree.ElementTree import fromstring as El
    >>> XB = musicxml.m21ToXml.XMLExporterBase()
    >>> mxObj = El('<note />')
    >>> n = note.Note('C-5')
    ```

    Most common case: does nothing

    ```python
    >>> XB.setEditorial(mxObj, n)
    >>> XB.dump(mxObj)
    <note />
    ```

    ```python
    >>> fn = editorial.Comment('flat is obvious error for sharp')
    >>> fn.levelInformation = 2
    >>> fn.isFootnote = True
    >>> n.editorial.footnotes.append(fn)
    >>> XB.setEditorial(mxObj, n)
    >>> XB.dump(mxObj)
    <note>
      <footnote>flat is obvious error for sharp</footnote>
      <level reference="no">2</level>
    </note>
    ```

    Placing information in .editorial.comments only puts out the level:

    ```python
    >>> mxObj = El('<note />')
    >>> n = note.Note('C-5')
    >>> com = editorial.Comment('flat is obvious error for sharp')
    >>> com.levelInformation = 'hello'
    >>> com.isReference = True
    >>> n.editorial.comments.append(com)
    >>> XB.setEditorial(mxObj, n)
    >>> XB.dump(mxObj)
    <note>
      <level reference="yes">hello</level>
    </note>
    ```

XMLExporterBase.setFont(*mxObject*, *m21Object*)[[source]](../_modules/music21/musicxml/m21ToXml.html#XMLExporterBase.setFont)
:   sets font-family, font-style, font-size, and font-weight as
    fontFamily (list), fontStyle, fontSize and fontWeight from
    an object into a TextStyle object

    conforms to attr-group %font in the MusicXML DTD

    ```python
    >>> from xml.etree.ElementTree import fromstring as El
    >>> XB = musicxml.m21ToXml.XMLExporterBase()
    >>> mxObj = El('<text>hi</text>')
    >>> te = expressions.TextExpression('hi!')
    >>> te.style.fontFamily = ['Courier', 'monospaced']
    >>> te.style.fontStyle = 'italic'
    >>> te.style.fontSize = 24.0
    >>> XB.setFont(mxObj, te)
    >>> XB.dump(mxObj)
    <text font-family="Courier,monospaced" font-size="24" font-style="italic">hi</text>
    ```

    ```python
    >>> XB = musicxml.m21ToXml.XMLExporterBase()
    >>> mxObj = El('<text>hi</text>')
    >>> te = expressions.TextExpression('hi!')
    >>> te.style.fontStyle = 'bold'
    >>> XB.setFont(mxObj, te)
    >>> XB.dump(mxObj)
    <text font-weight="bold">hi</text>
    ```

    ```python
    >>> te.style.fontStyle = 'bolditalic'
    >>> XB.setFont(mxObj, te)
    >>> XB.dump(mxObj)
    <text font-style="italic" font-weight="bold">hi</text>
    ```

XMLExporterBase.setPosition(*mxObject*, *m21Object*)[[source]](../_modules/music21/musicxml/m21ToXml.html#XMLExporterBase.setPosition)
:   set positioning information for an mxObject from
    default-x, default-y, relative-x, relative-y from
    the .style attribute’s absoluteX, relativeX, etc. attributes.

XMLExporterBase.setPrintObject(*mxObject*, *m21Object*)[[source]](../_modules/music21/musicxml/m21ToXml.html#XMLExporterBase.setPrintObject)
:   sets print-object to ‘no’ if m21Object.style.hideObjectOnPrint is True
    or if m21Object is a StyleObject and has .hideObjectOnPrint set to True.

XMLExporterBase.setPrintStyle(*mxObject*, *m21Object*)[[source]](../_modules/music21/musicxml/m21ToXml.html#XMLExporterBase.setPrintStyle)
:   get position, font, and color information from the mxObject
    into the m21Object, which must have style.TextStyle as its Style class.

    conforms to attr-group %print-style in the MusicXML DTD

XMLExporterBase.setPrintStyleAlign(*mxObject*, *m21Object*)[[source]](../_modules/music21/musicxml/m21ToXml.html#XMLExporterBase.setPrintStyleAlign)
:   runs setPrintStyle and then sets horizontalAlign and verticalAlign, on an
    m21Object, which must have style.TextStyle as its Style class.

    conforms to attr-group %print-style-align in the MusicXML DTD

XMLExporterBase.setStyleAttributes(*mxObject*, *m21Object*, *musicXMLNames*, *m21Names=None*)[[source]](../_modules/music21/musicxml/m21ToXml.html#XMLExporterBase.setStyleAttributes)
:   Sets any attribute from .style, doing some conversions.

    m21Object can also be a style.Style object itself.

XMLExporterBase.setTextFormatting(*mxObject*, *m21Object*)[[source]](../_modules/music21/musicxml/m21ToXml.html#XMLExporterBase.setTextFormatting)
:   sets the justification, print-style-align group, and
    text-decoration, text-rotation,
    letter-spacing, line-height, lang, text-direction, and
    enclosure, on an
    m21Object, which must have style.TextStyle as its Style class,
    and then calls setPrintStyleAlign

    conforms to attr-group %text-formatting in the MusicXML DTD

XMLExporterBase.staffLayoutToXmlStaffLayout(*staffLayout*, *mxStaffLayoutIn=None*)[[source]](../_modules/music21/musicxml/m21ToXml.html#XMLExporterBase.staffLayoutToXmlStaffLayout)
:   get a <staff-layout> tag from a StaffLayout object

    In music21, the <staff-layout> and <staff-details> are
    intertwined in a StaffLayout object.

    ```python
    >>> sl = layout.StaffLayout()
    >>> sl.distance = 40.0
    >>> sl.staffNumber = 1
    >>> XPBase = musicxml.m21ToXml.XMLExporterBase()
    >>> mxSl = XPBase.staffLayoutToXmlStaffLayout(sl)
    >>> XPBase.dump(mxSl)
    <staff-layout number="1">
      <staff-distance>40.0</staff-distance>
    </staff-layout>
    ```

XMLExporterBase.systemLayoutToXmlPrint(*systemLayout*, *mxPrintIn=None*)[[source]](../_modules/music21/musicxml/m21ToXml.html#XMLExporterBase.systemLayoutToXmlPrint)
:   Given a SystemLayout tag, set a <print> tag

    ```python
    >>> sl = layout.SystemLayout()
    >>> sl.distance = 55
    >>> sl.isNew = True
    >>> sl.rightMargin = 30.25
    >>> sl.leftMargin = 20
    ```

    ```python
    >>> XPBase = musicxml.m21ToXml.XMLExporterBase()
    >>> mxPrint = XPBase.systemLayoutToXmlPrint(sl)
    >>> XPBase.dump(mxPrint)
    <print new-system="yes">
      <system-layout>
        <system-margins>
          <left-margin>20</left-margin>
          <right-margin>30.25</right-margin>
        </system-margins>
        <system-distance>55</system-distance>
      </system-layout>
    </print>
    ```

    Test return conversion

    ```python
    >>> MP = musicxml.xmlToM21.MeasureParser()
    >>> sl2 = MP.xmlPrintToSystemLayout(mxPrint)
    >>> sl2.isNew
    True
    >>> sl2.rightMargin
    30.25
    >>> sl2.leftMargin
    20
    >>> sl2.distance
    55
    ```

XMLExporterBase.systemLayoutToXmlSystemLayout(*systemLayout*, *mxSystemLayoutIn=None*)[[source]](../_modules/music21/musicxml/m21ToXml.html#XMLExporterBase.systemLayoutToXmlSystemLayout)
:   get given a SystemLayout object configure <system-layout> or <print>

    Called out from xmlPrintToSystemLayout because it
    is also used in the <defaults> tag

    ```python
    >>> sl = layout.SystemLayout()
    >>> sl.distance = 40.0
    >>> sl.topDistance = 70.0
    >>> XPBase = musicxml.m21ToXml.XMLExporterBase()
    >>> mxSl = XPBase.systemLayoutToXmlSystemLayout(sl)
    >>> XPBase.dump(mxSl)
    <system-layout>
      <system-distance>40.0</system-distance>
      <top-system-distance>70.0</top-system-distance>
    </system-layout>
    ```

    ```python
    >>> sl = layout.SystemLayout()
    >>> sl.leftMargin = 30.0
    >>> mxSl = XPBase.systemLayoutToXmlSystemLayout(sl)
    >>> XPBase.dump(mxSl)
    <system-layout>
      <system-margins>
        <left-margin>30.0</left-margin>
      </system-margins>
    </system-layout>
    ```

XMLExporterBase.xmlHeader() → [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")[[source]](../_modules/music21/musicxml/m21ToXml.html#XMLExporterBase.xmlHeader)

## Functions

music21.musicxml.m21ToXml.getMetadataFromContext(*s: [Stream](moduleStreamBase.html#music21.stream.base.Stream "music21.stream.base.Stream")*) → [Metadata](moduleMetadata.html#music21.metadata.Metadata "music21.metadata.Metadata") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/musicxml/m21ToXml.html#getMetadataFromContext)
:   Get metadata from site or context, so that a Part
    can be shown and have the rich metadata of its Score

    ```python
    >>> s = stream.Score()
    >>> s2 = s.transpose(4)
    >>> md = metadata.Metadata()
    >>> md.title = 'emptiness'
    >>> s.metadata = md
    >>> s2.metadata is None
    True
    >>> musicxml.m21ToXml.getMetadataFromContext(s2).title
    'emptiness'
    >>> musicxml.m21ToXml.getMetadataFromContext(s).title
    'emptiness'
    >>> p = stream.Part()
    >>> s2.insert(0, p)
    >>> musicxml.m21ToXml.getMetadataFromContext(p).title
    'emptiness'
    ```

music21.musicxml.m21ToXml.normalizeColor(*color: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](../_modules/music21/musicxml/m21ToXml.html#normalizeColor)
:   Normalize a css3 name to hex or leave it alone.

    ```python
    >>> musicxml.m21ToXml.normalizeColor('')
    ''
    >>> musicxml.m21ToXml.normalizeColor('red')
    '#FF0000'
    >>> musicxml.m21ToXml.normalizeColor('#00ff00')
    '#00FF00'
    ```

music21.musicxml.m21ToXml.typeToMusicXMLType(*value: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](../_modules/music21/musicxml/m21ToXml.html#typeToMusicXMLType)
:   Convert a music21 type to a MusicXML type or raise a MusicXMLExportException

    ```python
    >>> musicxml.m21ToXml.typeToMusicXMLType('longa')
    'long'
    >>> musicxml.m21ToXml.typeToMusicXMLType('quarter')
    'quarter'
    >>> musicxml.m21ToXml.typeToMusicXMLType('duplex-maxima')
    Traceback (most recent call last):
    music21.musicxml.xmlObjects.MusicXMLExportException:
    Cannot convert "duplex-maxima" duration to MusicXML (too long).
    >>> musicxml.m21ToXml.typeToMusicXMLType('inexpressible')
    Traceback (most recent call last):
    music21.musicxml.xmlObjects.MusicXMLExportException:
    Cannot convert inexpressible durations to MusicXML.
    >>> musicxml.m21ToXml.typeToMusicXMLType('zero')
    Traceback (most recent call last):
    music21.musicxml.xmlObjects.MusicXMLExportException:
    Cannot convert durations without types to MusicXML.
    ```
