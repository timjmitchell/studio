Source: https://music21.org/music21docs/moduleReference/moduleMusicxmlXmlToM21.html

# music21.musicxml.xmlToM21

## MeasureParser

class music21.musicxml.xmlToM21.MeasureParser(*mxMeasure: [Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *parent: [PartParser](#music21.musicxml.xmlToM21.PartParser "music21.musicxml.xmlToM21.PartParser") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](../_modules/music21/musicxml/xmlToM21.html#MeasureParser)
:   parser to work with a single <measure> tag.

    called out for simplicity.

    ```python
    >>> from xml.etree.ElementTree import fromstring as EL
    ```

    ```python
    >>> scoreMeasure = '<measure><note><rest/><duration>40320</duration></note></measure>'
    >>> mxMeasure = EL(scoreMeasure)
    >>> mp = musicxml.xmlToM21.MeasureParser(mxMeasure)
    >>> mp.parse()
    >>> mp.restAndNoteCount['rest']
    1
    >>> mp.restAndNoteCount['note']
    0
    ```

    fullMeasureRest indicates that a rest lasts the full measure of the current time signature.

    ```python
    >>> mp.fullMeasureRest
    True
    ```

[`MeasureParser`](#music21.musicxml.xmlToM21.MeasureParser "music21.musicxml.xmlToM21.MeasureParser") bases

* [`SoundTagMixin`](moduleMusicxmlXmlSoundParser.html#music21.musicxml.xmlSoundParser.SoundTagMixin "music21.musicxml.xmlSoundParser.SoundTagMixin")
* [`XMLParserBase`](#music21.musicxml.xmlToM21.XMLParserBase "music21.musicxml.xmlToM21.XMLParserBase")

[`MeasureParser`](#music21.musicxml.xmlToM21.MeasureParser "music21.musicxml.xmlToM21.MeasureParser") methods

MeasureParser.addToStaffReference(*mxObjectOrNumber*, *m21Object*)[[source]](../_modules/music21/musicxml/xmlToM21.html#MeasureParser.addToStaffReference)
:   Utility routine for importing musicXML objects;
    here, we store a reference to the music21 object in a dictionary,
    where keys are the staff values. Staff values may be None, 1, 2, etc.

    ```python
    >>> MP = musicxml.xmlToM21.MeasureParser()
    >>> MP.addToStaffReference(1, note.Note('C5'))
    >>> MP.addToStaffReference(2, note.Note('D3'))
    >>> MP.addToStaffReference(2, note.Note('E3'))
    >>> len(MP.staffReference)
    2
    >>> list(sorted(MP.staffReference.keys()))
    [1, 2]
    >>> MP.staffReference[1]
    [<music21.note.Note C>]
    >>> MP.staffReference[2]
    [<music21.note.Note D>, <music21.note.Note E>]
    ```

    ```python
    >>> from xml.etree.ElementTree import fromstring as EL
    >>> mxNote = EL('<note><staff>1</staff></note>')
    >>> MP.addToStaffReference(mxNote, note.Note('F5'))
    >>> MP.staffReference[1]
    [<music21.note.Note C>, <music21.note.Note F>]
    ```

    No staff reference.

    ```python
    >>> mxNote = EL('<note />')
    >>> MP.addToStaffReference(mxNote, note.Note('G4'))
    >>> len(MP.staffReference)
    3
    >>> MP.staffReference[0]
    [<music21.note.Note G>]
    ```

MeasureParser.findM21VoiceFromXmlVoice(*mxVoice: [Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [Voice](moduleStreamBase.html#music21.stream.base.Voice "music21.stream.base.Voice") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/musicxml/xmlToM21.html#MeasureParser.findM21VoiceFromXmlVoice)
:   Find the stream.Voice object from a <voice> tag or None.

static MeasureParser.getStaffNumber(*mxObjectOrNumber*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](../_modules/music21/musicxml/xmlToM21.html#MeasureParser.getStaffNumber)
:   gets an int representing a staff number, or 0 (representing no staff assigned)
    from an mxObject or a number:

    ```python
    >>> mp = musicxml.xmlToM21.MeasureParser()
    >>> from xml.etree.ElementTree import fromstring as EL
    ```

    ```python
    >>> gsn = mp.getStaffNumber
    >>> gsn(1)
    1
    >>> gsn('2')
    2
    ```

    <note> tags store their staff numbers in a <staff> tag’s text:

    ```python
    >>> gsn(EL('<note><staff>2</staff></note>'))
    2
    ```

    Or if there is no <staff> tag, they get a special NO\_STAFF\_ASSIGNED value.

    ```python
    >>> el = EL('<note><pitch><step>C</step><octave>4</octave></pitch></note>')
    >>> gsn(el) == musicxml.xmlToM21.NO_STAFF_ASSIGNED
    True
    ```

    Clefs, however, store their staff numbers in a number attribute.

    ```python
    >>> gsn(EL('<clef number="2"/>'))
    2
    >>> gsn(None) == musicxml.xmlToM21.NO_STAFF_ASSIGNED
    True
    ```

MeasureParser.handleClef(*mxClef*)[[source]](../_modules/music21/musicxml/xmlToM21.html#MeasureParser.handleClef)
:   Handles a clef object, appending it to the core, and
    setting self.lastClefs for the staff number.

    ```python
    >>> import xml.etree.ElementTree as ET
    >>> mxClef = ET.fromstring('<clef><sign>G</sign><line>2</line></clef>')
    ```

    ```python
    >>> MP = musicxml.xmlToM21.MeasureParser()
    >>> MP.handleClef(mxClef)
    >>> MP.lastClefs
    {0: <music21.clef.TrebleClef>}
    ```

    ```python
    >>> mxClefBC = ET.fromstring('<clef number="2"><sign>F</sign><line>4</line></clef>')
    >>> MP.handleClef(mxClefBC)
    >>> MP.lastClefs[2]
    <music21.clef.BassClef>
    >>> MP.lastClefs[0]
    <music21.clef.TrebleClef>
    ```

MeasureParser.handleFingering(*tech*, *mxObj*)[[source]](../_modules/music21/musicxml/xmlToM21.html#MeasureParser.handleFingering)
:   A few specialized functions for dealing with fingering objects

MeasureParser.handleKeySignature(*mxKey*)[[source]](../_modules/music21/musicxml/xmlToM21.html#MeasureParser.handleKeySignature)
:   convert mxKey to a Key or KeySignature and run insertCoreAndRef on it

MeasureParser.handleMeasureStyle(*mxMeasureStyle*)[[source]](../_modules/music21/musicxml/xmlToM21.html#MeasureParser.handleMeasureStyle)
:   measure + multi-measure repeats, slashed repeats, etc.

    But currently only multiMeasure rests are supported.

    Each of these applies to the entire measure, so there’s
    no need to insert into the stream.

    Does not support multiple staves yet.

MeasureParser.handleStaffDetails(*mxDetails*)[[source]](../_modules/music21/musicxml/xmlToM21.html#MeasureParser.handleStaffDetails)
:   StaffDetails (staff-details) handles attributes about
    the staff itself – its size, number of lines, tuning,
    frets, etc.

    It is different from StaffLayout (staff-layout) which
    only handles relationship of one staff to another (the
    distance)

    Rather than returning a StaffLayout object,
    it adds it to self.staffLayoutObjects checking
    to see if there is already an incomplete
    StaffLayout object for this staff.

MeasureParser.handleTimeSignature(*mxTime*)[[source]](../_modules/music21/musicxml/xmlToM21.html#MeasureParser.handleTimeSignature)
:   Creates a TimeSignature using xmlToTimeSignature and inserts it into
    the stream if it is appropriate to do so (now always yes.)

MeasureParser.insertCoreAndRef(*offset*, *mxObjectOrNumber*, *m21Object*)[[source]](../_modules/music21/musicxml/xmlToM21.html#MeasureParser.insertCoreAndRef)
:   runs addToStaffReference and then insertCore.

    ```python
    >>> from xml.etree.ElementTree import fromstring as EL
    >>> mxNote = EL('<note><staff>1</staff></note>')
    ```

    ```python
    >>> MP = musicxml.xmlToM21.MeasureParser()
    >>> MP.insertCoreAndRef(1.0, mxNote, note.Note('F5'))
    ```

    This routine leaves MP.stream in an unusable state, because
    it runs insertCore. Thus, before querying the stream we need to run at end:

    ```python
    >>> MP.stream.coreElementsChanged()
    >>> MP.stream.show('text')
    {1.0} <music21.note.Note F>
    ```

MeasureParser.insertInMeasureOrVoice(*mxElement*, *el*)[[source]](../_modules/music21/musicxml/xmlToM21.html#MeasureParser.insertInMeasureOrVoice)
:   Adds an object to a measure or a voice. Needs a note element (obviously)
    but also mxNote to get the voice. Uses coreInsert and thus leaves insertStream
    on the inner voice in an unusable state.

MeasureParser.mxKeyOctaves(*mxKey*, *ks*)[[source]](../_modules/music21/musicxml/xmlToM21.html#MeasureParser.mxKeyOctaves)
:   process the <key-octave> tags to potentially change a key signature
    to a non-standard key signature.

    ```python
    >>> import xml.etree.ElementTree as ET
    >>> mxKey = ET.fromstring('<key><fifths>-4</fifths>'
    ...   + '<key-octave number="1">3</key-octave>'
    ...   + '<key-octave number="2">4</key-octave>'
    ...   + '<key-octave number="4">3</key-octave>'
    ...   + '</key>')
    ```

    ```python
    >>> ks = key.KeySignature(-4)
    >>> MP = musicxml.xmlToM21.MeasureParser()
    >>> MP.mxKeyOctaves(mxKey, ks)
    >>> ks.alteredPitches
    [<music21.pitch.Pitch B-3>,
     <music21.pitch.Pitch E-4>,
     <music21.pitch.Pitch A->,
     <music21.pitch.Pitch D-3>]
    ```

MeasureParser.nonTraditionalKeySignature(*mxKey*)[[source]](../_modules/music21/musicxml/xmlToM21.html#MeasureParser.nonTraditionalKeySignature)
:   Returns a KeySignature object that represents a nonTraditional Key Signature

    called by xmlToKeySignature if <fifths> is not present.

    ```python
    >>> import xml.etree.ElementTree as ET
    >>> MP = musicxml.xmlToM21.MeasureParser()
    ```

    ```python
    >>> mxKey = ET.fromstring('<key><key-step>E</key-step><key-alter>-1</key-alter></key>')
    >>> MP.nonTraditionalKeySignature(mxKey)
    <music21.key.KeySignature of pitches: [E-]>
    ```

    Should be the same:

    ```python
    >>> MP.xmlToKeySignature(mxKey)
    <music21.key.KeySignature of pitches: [E-]>
    ```

    Works with key-accidental also:

    ```python
    >>> mxKey = ET.fromstring('<key><key-step>G</key-step><key-alter>1</key-alter>'
    ...                       + '<key-accidental>sharp</key-accidental></key>')
    >>> MP.nonTraditionalKeySignature(mxKey)
    <music21.key.KeySignature of pitches: [G#]>
    ```

MeasureParser.parse()[[source]](../_modules/music21/musicxml/xmlToM21.html#MeasureParser.parse)

MeasureParser.parseAttributesTag(*mxAttributes*)[[source]](../_modules/music21/musicxml/xmlToM21.html#MeasureParser.parseAttributesTag)
:   Parses a single attributes tag (mxAttributes) and sets

    self.attributesAreInternal to False,
    self.activeAttributes to mxAttributes,
    self.parent.activeAttributes to mxAttributes
    and then runs the appropriate attributeTagsToMethods for
    the attribute.

    Also sets self.divisions for the current divisions
    (along with self.parent.lastDivisions)
    and self.transposition and
    to the current transpose.

MeasureParser.parseMeasureAttributes()[[source]](../_modules/music21/musicxml/xmlToM21.html#MeasureParser.parseMeasureAttributes)
:   parses the attributes of the <measure> tag. Not the
    <attributes> tag inside the measure tag.

    calls parseMeasureNumbers(), and gets the width from the width tag.

    # TODO: non-controlling
    # may need to do a format/unit conversion?

MeasureParser.parseMeasureNumbers(*mNumRaw=None*)[[source]](../_modules/music21/musicxml/xmlToM21.html#MeasureParser.parseMeasureNumbers)
:   Gets the measure number from the ‘number’ attribute of the
    <measure> tag. (Or, for testing, from the mNumRaw
    argument). Sets MeasureParser.stream.number and possibly
    MeasureParser.stream.numberSuffix

    ```python
    >>> MP = musicxml.xmlToM21.MeasureParser()
    >>> MP.parseMeasureNumbers('5')
    >>> MP.stream.number
    5
    ```

    Sets not only stream.number, but also MeasureParser.measureNumber and
    MeasureParser.numberSuffix

    ```python
    >>> MP.parseMeasureNumbers('44b')
    >>> MP.stream.number
    44
    >>> MP.stream.numberSuffix
    'b'
    >>> MP.measureNumber
    44
    >>> MP.numberSuffix
    'b'
    ```

    ```python
    >>> MP.parseMeasureNumbers('X1')
    >>> MP.stream.number
    1
    >>> MP.stream.numberSuffix
    'X'
    ```

MeasureParser.setBend(*mxh*, *bend*)[[source]](../_modules/music21/musicxml/xmlToM21.html#MeasureParser.setBend)
:   Gets the bend amplitude from the bend-alter tag,
    then optional pre-bend and with-bar tags are processed,
    as well as release which is converted from divisions to music21 time.

    Called from xmlTechnicalToArticulation

    ```python
    >>> from xml.etree.ElementTree import fromstring as EL
    >>> MP = musicxml.xmlToM21.MeasureParser()
    ```

    ```python
    >>> mxTech = EL('<bend><bend-alter>2</bend-alter></bend>')
    >>> a = MP.xmlTechnicalToArticulation(mxTech)
    >>> a
    <music21.articulations.FretBend 0>
    >>> a.bendAlter.semitones
    2
    >>> a.release
    ```

    ```python
    >>> a.withBar
    ```

    ```python
    >>> a.preBend
    False
    ```

    ```python
    >>> mxTech = EL('<bend><bend-alter>-2</bend-alter><pre-bend/></bend>')
    >>> a = MP.xmlTechnicalToArticulation(mxTech)
    >>> a.bendAlter.semitones
    -2
    >>> a.preBend
    True
    ```

    ```python
    >>> mxTech = EL('<bend><bend-alter>-2</bend-alter><release offset="1"/></bend>')
    >>> a = MP.xmlTechnicalToArticulation(mxTech)
    >>> a.bendAlter.semitones
    -2
    >>> a.release
    Fraction(1, 10080)
    ```

    ```python
    >>> mxTech = EL('<bend><bend-alter>-1</bend-alter><with-bar>dip</with-bar></bend>')
    >>> a = MP.xmlTechnicalToArticulation(mxTech)
    >>> a.bendAlter.semitones
    -1
    >>> a.withBar
    'dip'
    ```

MeasureParser.setDirectionInDirectionType(*mxDir: [Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")*, *mxDirection: [Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")*, *staffKey: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *totalOffset: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*)[[source]](../_modules/music21/musicxml/xmlToM21.html#MeasureParser.setDirectionInDirectionType)

MeasureParser.setDynamicsDirection(*mxDir: [Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")*, *mxDyn: [Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")*, *mxDirection: [Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")*, *staffKey: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *totalOffset: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*)[[source]](../_modules/music21/musicxml/xmlToM21.html#MeasureParser.setDynamicsDirection)
:   Add a single dynamic element to the core and staffReference.

static MeasureParser.setHarmonic(*mxh*, *harm*)[[source]](../_modules/music21/musicxml/xmlToM21.html#MeasureParser.setHarmonic)
:   From the artificial or natural tag (or no tag) and
    zero or one of base-pitch, sounding-pitch, touching-pitch,
    sets .harmonicType and .pitchType on an articulations.Harmonic object

    Called from xmlTechnicalToArticulation

    ```python
    >>> from xml.etree.ElementTree import fromstring as EL
    >>> MP = musicxml.xmlToM21.MeasureParser()
    ```

    ```python
    >>> mxTech = EL('<harmonic><artificial/><sounding-pitch/></harmonic>')
    >>> a = MP.xmlTechnicalToArticulation(mxTech)
    >>> a
    <music21.articulations.StringHarmonic>
    ```

    ```python
    >>> a.harmonicType
    'artificial'
    >>> a.pitchType
    'sounding'
    ```

MeasureParser.updateLyricsFromList(*n*, *lyricList*)[[source]](../_modules/music21/musicxml/xmlToM21.html#MeasureParser.updateLyricsFromList)
:   Takes a list of <lyric> elements and update the
    note’s lyrics from that list.

    ```python
    >>> import xml.etree.ElementTree as ET
    >>> MP = musicxml.xmlToM21.MeasureParser()
    ```

    ```python
    >>> mxLyric1 = ET.fromstring('<lyric><text>Hi</text><elision/><text>There</text></lyric>')
    >>> mxLyric2 = ET.fromstring('<lyric><text>Bye</text></lyric>')
    >>> n = note.Note()
    >>> MP.updateLyricsFromList(n, [mxLyric1, mxLyric2])
    >>> n.lyrics
    [<music21.note.Lyric number=1 syllabic=composite text='Hi There'>,
     <music21.note.Lyric number=2 text='Bye'>]
    ```

MeasureParser.updateVoiceInformation()[[source]](../_modules/music21/musicxml/xmlToM21.html#MeasureParser.updateVoiceInformation)
:   Finds all the “voice” information in <note> and <forward> tags and updates the set of
    .voiceIndices to be a set of all the voice texts, and if there is
    more than one voice in the measure, sets .useVoices to True
    and creates a voice for each.

    ```python
    >>> import xml.etree.ElementTree as ET
    >>> MP = musicxml.xmlToM21.MeasureParser()
    >>> MP.mxMeasure = ET.fromstring('<measure><note><voice>1</voice></note></measure>')
    >>> MP.updateVoiceInformation()
    ```

    Puts a set object in .voiceIndices

    ```python
    >>> MP.voiceIndices
    {'1'}
    >>> MP.useVoices
    False
    ```

    ```python
    >>> MP = musicxml.xmlToM21.MeasureParser()
    >>> MP.mxMeasure = ET.fromstring('<measure><note><voice>1</voice></note>'
    ...                                     + '<note><voice>2</voice></note></measure>')
    >>> MP.updateVoiceInformation()
    >>> sorted(list(MP.voiceIndices))
    ['1', '2']
    >>> MP.useVoices
    True
    >>> len(MP.stream)
    2
    >>> list(MP.stream.getElementsByClass(stream.Voice))
    [<music21.stream.Voice 1>, <music21.stream.Voice 2>]
    >>> MP = musicxml.xmlToM21.MeasureParser()
    >>> MP.mxMeasure = ET.fromstring('<measure><note><voice>1</voice></note>'
    ...                                     + '<forward><voice>2</voice></forward></measure>')
    >>> MP.updateVoiceInformation()
    >>> sorted(list(MP.voiceIndices))
    ['1', '2']
    >>> MP.useVoices
    True
    >>> len(MP.stream)
    2
    >>> list(MP.stream.getElementsByClass(stream.Voice))
    [<music21.stream.Voice 1>, <music21.stream.Voice 2>]
    ```

MeasureParser.xmlBackup(*mxObj: [Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")*)[[source]](../_modules/music21/musicxml/xmlToM21.html#MeasureParser.xmlBackup)
:   Parse a backup tag by changing `offsetMeasureNote`.

    A floor of 0.0 is enforced in case of float rounding issues.

    ```python
    >>> MP = musicxml.xmlToM21.MeasureParser()
    >>> MP.divisions = 100
    >>> MP.offsetMeasureNote = 1.9979
    ```

    ```python
    >>> from xml.etree.ElementTree import fromstring as EL
    >>> mxBackup = EL('<backup><duration>100</duration></backup>')
    >>> MP.xmlBackup(mxBackup)
    >>> MP.offsetMeasureNote
    0.9979
    ```

    ```python
    >>> MP.xmlBackup(mxBackup)
    >>> MP.offsetMeasureNote
    0.0
    ```

MeasureParser.xmlBarline(*mxBarline: [Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/musicxml/xmlToM21.html#MeasureParser.xmlBarline)
:   Handles everything for putting a barline into a Stream
    and updating repeat characteristics.

MeasureParser.xmlDirection(*mxDirection*)[[source]](../_modules/music21/musicxml/xmlToM21.html#MeasureParser.xmlDirection)
:   convert a <direction> tag to one or more expressions, metronome marks, etc.
    and add them to the core and staffReference.

MeasureParser.xmlDirectionTypeToSpanners(*mxObj: ET.Element*, *staffKey: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *totalOffset: OffsetQL | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](../_modules/music21/musicxml/xmlToM21.html#MeasureParser.xmlDirectionTypeToSpanners)
:   Some spanners, such as MusicXML wedge, bracket, dashes, pedal,
    and ottava are encoded as MusicXML directions.

    Parameters:
    :   * **mxObj** – the specific direction element (e.g. <wedge>).
        * **staffKey** – staff number (required for <pedal>)
        * **totalOffset** – offset in measure of this direction (required for <pedal>)

    ```python
    >>> from xml.etree.ElementTree import fromstring as EL
    >>> MP = musicxml.xmlToM21.MeasureParser()
    >>> n1 = note.Note('D4')
    >>> MP.nLast = n1
    ```

    ```python
    >>> len(MP.spannerBundle)
    0
    >>> mxDirectionType = EL('<wedge type="crescendo" number="2"/>')
    >>> retList = MP.xmlDirectionTypeToSpanners(mxDirectionType)
    >>> retList
    [<music21.dynamics.Crescendo>]
    ```

    ```python
    >>> len(MP.spannerBundle)
    1
    >>> sp = MP.spannerBundle[0]
    >>> sp
    <music21.dynamics.Crescendo>
    ```

    ```python
    >>> mxDirectionType2 = EL('<wedge type="stop" number="2"/>')
    >>> retList = MP.xmlDirectionTypeToSpanners(mxDirectionType2)
    ```

    retList is empty because nothing new has been added.

    ```python
    >>> retList
    []
    ```

    ```python
    >>> len(MP.spannerBundle)
    1
    >>> sp = MP.spannerBundle[0]
    >>> sp
    <music21.dynamics.Crescendo <music21.note.Note D>>
    ```

    ```python
    >>> mxDirection = EL('<direction place="below"/>')
    >>> mxDirectionType = EL('<pedal type="sostenuto" sign="yes" number="2"/>')
    >>> retList = MP.xmlDirectionTypeToSpanners(mxDirectionType, 1, 0.5)
    >>> retList
    [<music21.expressions.PedalMark>]
    >>> pedalMark = retList[0]
    >>> pedalMark.pedalType
    <PedalType.Sostenuto>
    >>> pedalMark.pedalForm
    <PedalForm.Symbol>
    ```

    ```python
    >>> mxDirectionType1a = EL('<pedal type="resume" line="yes" number="2"/>')
    >>> retList = MP.xmlDirectionTypeToSpanners(mxDirectionType1a, 1, 0.5)
    >>> retList
    []
    >>> pedalMark.pedalForm
    <PedalForm.SymbolLine>
    ```

    ```python
    >>> mxDirectionType2 = EL('<pedal type="change" line="yes" number="2"/>')
    >>> retList = MP.xmlDirectionTypeToSpanners(mxDirectionType2, 1, 1.0)
    >>> retList
    []
    ```

    ```python
    >>> mxDirectionType3 = EL('<pedal type="discontinue" line="yes" number="2"/>')
    >>> retList = MP.xmlDirectionTypeToSpanners(mxDirectionType3, 1, 2.0)
    >>> retList
    []
    ```

    ```python
    >>> mxDirectionType4 = EL('<pedal type="resume" line="yes" number="2"/>')
    >>> retList = MP.xmlDirectionTypeToSpanners(mxDirectionType4, 1, 3.5)
    >>> retList
    []
    ```

    ```python
    >>> mxDirectionType5 = EL('<pedal type="stop" line="yes" number="2"/>')
    >>> retList = MP.xmlDirectionTypeToSpanners(mxDirectionType5, 1, 4.0)
    >>> retList
    []
    >>> pedalMark.getFirst()
    <music21.expressions.PedalBounce at 1.0>
    >>> pedalMark.getLast() is n1
    True
    >>> MP.stream.elements
    (<music21.expressions.PedalBounce at 1.0>, <music21.expressions.PedalGapStart at 2.0>,
    <music21.expressions.PedalGapEnd at 3.5>)
    ```

MeasureParser.xmlForward(*mxObj: [Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")*)[[source]](../_modules/music21/musicxml/xmlToM21.html#MeasureParser.xmlForward)
:   Parse a forward tag by changing `offsetMeasureNote`.

MeasureParser.xmlGraceToGrace(*mxGrace*, *noteOrChord*)[[source]](../_modules/music21/musicxml/xmlToM21.html#MeasureParser.xmlGraceToGrace)
:   Given a completely formed, non-grace Note or Chord that should become one
    create and return a m21 grace version of the same.

MeasureParser.xmlHarmony(*mxHarmony*)[[source]](../_modules/music21/musicxml/xmlToM21.html#MeasureParser.xmlHarmony)
:   Create a ChordSymbol object and insert it to the core and staff reference.

MeasureParser.xmlNotations(*mxNotations: [Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")*, *n: [GeneralNote](moduleNote.html#music21.note.GeneralNote "music21.note.GeneralNote")*)[[source]](../_modules/music21/musicxml/xmlToM21.html#MeasureParser.xmlNotations)
:   ```python
    >>> from xml.etree.ElementTree import fromstring as EL
    >>> MP = musicxml.xmlToM21.MeasureParser()
    ```

    ```python
    >>> mxNotations = EL('<notations>' +
    ...     '<fermata type="upright">angled</fermata>' +
    ...     '</notations>')
    >>> n = note.Note()
    >>> MP.xmlNotations(mxNotations, n)
    >>> n.expressions
    [<music21.expressions.Fermata>]
    >>> n.expressions[0].type
    'upright'
    >>> n.expressions[0].shape
    'angled'
    ```

MeasureParser.xmlNotationsToSpanners(*mxNotations*, *n*)[[source]](../_modules/music21/musicxml/xmlToM21.html#MeasureParser.xmlNotationsToSpanners)

MeasureParser.xmlNoteToGeneralNoteHelper(*n*, *mxNote*, *freeSpanners=True*)[[source]](../_modules/music21/musicxml/xmlToM21.html#MeasureParser.xmlNoteToGeneralNoteHelper)
:   Combined function to work on all <note> tags, where n can be
    a Note or Rest.

    ```python
    >>> from xml.etree.ElementTree import fromstring as EL
    >>> n = note.Note()
    >>> mxNote = EL('<note color="silver"></note>')
    >>> MP = musicxml.xmlToM21.MeasureParser()
    >>> n = MP.xmlNoteToGeneralNoteHelper(n, mxNote)
    >>> n.style.color
    'silver'
    ```

MeasureParser.xmlNotehead(*n*, *mxNotehead*)[[source]](../_modules/music21/musicxml/xmlToM21.html#MeasureParser.xmlNotehead)
:   Set notehead information from the mxNotehead object

    ```python
    >>> from xml.etree.ElementTree import fromstring as EL
    >>> MP = musicxml.xmlToM21.MeasureParser()
    ```

    ```python
    >>> n = note.Note()
    >>> nh = EL('<notehead color="#FF0000" filled="no" parentheses="yes">'
    ...         + 'diamond</notehead>')
    ```

    ```python
    >>> MP.xmlNotehead(n, nh)
    >>> n.notehead
    'diamond'
    >>> n.noteheadFill
    False
    >>> n.noteheadParenthesis
    True
    >>> n.style.color
    '#FF0000'
    ```

MeasureParser.xmlOneSpanner(*mxObj*, *target*, *spannerClass*, *\**, *allowDuplicateIds=False*)[[source]](../_modules/music21/musicxml/xmlToM21.html#MeasureParser.xmlOneSpanner)
:   Some spanner types do not have an id necessarily, we allow duplicates of them
    if allowDuplicateIds is True. Wedges are one.

    Returns the new spanner created.

MeasureParser.xmlOrnamentToExpression(*mxObj*, *\**, *mostRecentOrnament: [Ornament](moduleExpressions.html#music21.expressions.Ornament "music21.expressions.Ornament") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](../_modules/music21/musicxml/xmlToM21.html#MeasureParser.xmlOrnamentToExpression)
:   Convert mxOrnament into a music21 ornament.

    This only processes non-spanner ornaments.
    Many mxOrnaments are spanners: these are handled elsewhere.

    Returns None if it cannot be converted or is not defined, or if the
    mxObj is an accidental-mark (in which case the accidental is placed
    in the mostRecentOrnament instead).

    Return an articulation from an mxObj, setting placement

    ```python
    >>> from xml.etree.ElementTree import fromstring as EL
    >>> MP = musicxml.xmlToM21.MeasureParser()
    ```

    ```python
    >>> mxOrn = EL('<inverted-turn placement="above" font-size="24"/>')
    >>> a = MP.xmlOrnamentToExpression(mxOrn)
    >>> a
    <music21.expressions.InvertedTurn>
    >>> a.placement
    'above'
    >>> a.style.fontSize
    24
    ```

    If it can’t be converted, return None

    ```python
    >>> mxOrn = EL('<crazy-slide placement="above"/>')
    >>> a = MP.xmlOrnamentToExpression(mxOrn)
    >>> a is None
    True
    ```

    If it is ‘accidental-mark’, add to mostRecentOrnament, and return None

    ```python
    >>> turn = expressions.Turn()
    >>> turn.lowerAccidental is None
    True
    >>> turn.upperAccidental is None
    True
    >>> mxOrn = EL('<accidental-mark placement="below">flat</accidental-mark>')
    >>> a = MP.xmlOrnamentToExpression(mxOrn, mostRecentOrnament=turn)
    >>> a is None
    True
    >>> turn.lowerAccidental
    <music21.pitch.Accidental flat>
    >>> turn.upperAccidental is None
    True
    ```

    Not supported currently: ‘vertical-turn’

MeasureParser.xmlPrint(*mxPrint: [Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")*)[[source]](../_modules/music21/musicxml/xmlToM21.html#MeasureParser.xmlPrint)
:   <print> handles changes in pages, numbering, layout,
    etc. so can generate PageLayout, SystemLayout, or StaffLayout
    objects.

    Should also be able to set measure attributes on self.stream

MeasureParser.xmlStaffLayoutFromStaffDetails(*mxDetails*, *m21staffLayout: [StaffLayout](moduleLayout.html#music21.layout.StaffLayout "music21.layout.StaffLayout") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [StaffLayout](moduleLayout.html#music21.layout.StaffLayout "music21.layout.StaffLayout") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/musicxml/xmlToM21.html#MeasureParser.xmlStaffLayoutFromStaffDetails)
:   Returns a new StaffLayout object from staff-details or sets attributes on an existing one

    ```python
    >>> from xml.etree.ElementTree import fromstring as EL
    >>> MP = musicxml.xmlToM21.MeasureParser()
    >>> mxDetails = EL('<details number="2" print-object="no">'
    ...                + '<staff-size>21.2</staff-size><staff-lines>4</staff-lines>'
    ...                + '</details>')
    >>> stl = MP.xmlStaffLayoutFromStaffDetails(mxDetails)
    >>> stl.staffSize
    21.2
    >>> stl.staffLines
    4
    >>> stl.staffNumber
    2
    >>> stl.hidden
    True
    ```

    staffType defaults to Regular:

    ```python
    >>> stl.staffType
    <StaffType.REGULAR: 'regular'>
    >>> mxDetails2 = EL(r'<details number="2"><staff-type>cue</staff-type></details>')
    >>> MP.xmlStaffLayoutFromStaffDetails(mxDetails2, m21staffLayout=stl)
    >>> stl.staffType
    <StaffType.CUE: 'cue'>
    ```

MeasureParser.xmlTechnicalToArticulation(*mxObj*)[[source]](../_modules/music21/musicxml/xmlToM21.html#MeasureParser.xmlTechnicalToArticulation)
:   Convert an mxArticulationMark to a music21.articulations.Articulation
    object or one of its subclasses.

    ```python
    >>> from xml.etree.ElementTree import fromstring as EL
    >>> MP = musicxml.xmlToM21.MeasureParser()
    ```

    ```python
    >>> mxTech = EL('<down-bow placement="below"/>')
    >>> a = MP.xmlTechnicalToArticulation(mxTech)
    >>> a
    <music21.articulations.DownBow>
    >>> a.placement
    'below'
    ```

    Fingering might have substitution or alternate

    ```python
    >>> mxTech = EL('<fingering substitution="yes">5</fingering>')
    >>> f = MP.xmlTechnicalToArticulation(mxTech)
    >>> f
    <music21.articulations.Fingering 5>
    >>> f.substitution
    True
    >>> f.alternate
    False
    ```

    FingerNumbers get converted to ints if possible

    ```python
    >>> f.fingerNumber
    5
    ```

    ```python
    >>> mxTech = EL('<fingering alternate="yes">4-3</fingering>')
    >>> f = MP.xmlTechnicalToArticulation(mxTech)
    >>>
    <music21.articulations.Fingering 4-3>
    >>> f.alternate
    True
    >>> f.fingerNumber
    '4-3'
    ```

MeasureParser.xmlToAccidental(*mxAccidental: [Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")*, *inputM21: [Accidental](modulePitch.html#music21.pitch.Accidental "music21.pitch.Accidental") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [Accidental](modulePitch.html#music21.pitch.Accidental "music21.pitch.Accidental")[[source]](../_modules/music21/musicxml/xmlToM21.html#MeasureParser.xmlToAccidental)
:   ```python
    >>> from xml.etree.ElementTree import fromstring as EL
    >>> MP = musicxml.xmlToM21.MeasureParser()
    ```

    ```python
    >>> a = EL('<accidental parentheses="yes">sharp</accidental>')
    >>> b = MP.xmlToAccidental(a)
    >>> b.name
    'sharp'
    >>> b.alter
    1.0
    >>> b.displayStyle
    'parentheses'
    ```

    ```python
    >>> a = EL('<accidental>half-flat</accidental>')
    >>> b = pitch.Accidental()
    >>> unused = MP.xmlToAccidental(a, b)
    >>> b.name
    'half-flat'
    >>> b.alter
    -0.5
    ```

    ```python
    >>> a = EL('<accidental bracket="yes">sharp</accidental>')
    >>> b = MP.xmlToAccidental(a)
    >>> b.displayStyle
    'bracket'
    ```

    ```python
    >>> a = EL('<accidental bracket="yes" parentheses="yes">sharp</accidental>')
    >>> b = MP.xmlToAccidental(a)
    >>> b.displayStyle
    'both'
    ```

MeasureParser.xmlToArticulation(*mxObj*)[[source]](../_modules/music21/musicxml/xmlToM21.html#MeasureParser.xmlToArticulation)
:   Return an articulation from an mxObj, setting placement

    ```python
    >>> from xml.etree.ElementTree import fromstring as EL
    >>> MP = musicxml.xmlToM21.MeasureParser()
    ```

    ```python
    >>> mxArt = EL('<spiccato placement="above"/>')
    >>> a = MP.xmlToArticulation(mxArt)
    >>> a
    <music21.articulations.Spiccato>
    >>> a.placement
    'above'
    ```

    ```python
    >>> mxArt = EL('<doit dash-length="2" default-x="5" default-y="2" '
    ...            + 'line-shape="curved" line-type="dashed" space-length="1" />')
    >>> a = MP.xmlToArticulation(mxArt)
    >>> a
    <music21.articulations.Doit>
    >>> a.placement is None
    True
    >>> a.style.dashLength
    2
    >>> a.style.absoluteX
    5
    >>> a.style.lineShape
    'curved'
    ```

MeasureParser.xmlToBarline(*mxBarline*, *inputM21=None*)[[source]](../_modules/music21/musicxml/xmlToM21.html#MeasureParser.xmlToBarline)
:   Given an mxBarline, fill the necessary parameters

    ```python
    >>> import xml.etree.ElementTree as ET
    >>> MP = musicxml.xmlToM21.MeasureParser()
    ```

    ```python
    >>> mxBarline = ET.fromstring(
    ...    '<barline location="right"><bar-style>light-light</bar-style></barline>')
    >>> b = MP.xmlToBarline(mxBarline)
    >>> b
    <music21.bar.Barline type=double>
    >>> b.type  # music21.type is different from musicxml.style
    'double'
    >>> b.location
    'right'
    ```

MeasureParser.xmlToBeam(*mxBeam: [Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")*, *inputM21=None*)[[source]](../_modules/music21/musicxml/xmlToM21.html#MeasureParser.xmlToBeam)
:   given an mxBeam object return a [`Beam`](moduleBeam.html#music21.beam.Beam "music21.beam.Beam") object

    ```python
    >>> from xml.etree.ElementTree import fromstring as EL
    >>> MP = musicxml.xmlToM21.MeasureParser()
    ```

    ```python
    >>> mxBeam = EL('<beam>begin</beam>')
    >>> a = MP.xmlToBeam(mxBeam)
    >>> a.type
    'start'
    ```

    ```python
    >>> mxBeam = EL('<beam>continue</beam>')
    >>> a = MP.xmlToBeam(mxBeam)
    >>> a.type
    'continue'
    ```

    ```python
    >>> mxBeam = EL('<beam>end</beam>')
    >>> a = MP.xmlToBeam(mxBeam)
    >>> a.type
    'stop'
    ```

    ```python
    >>> mxBeam = EL('<beam>forward hook    </beam>')
    >>> a = MP.xmlToBeam(mxBeam)
    >>> a.type
    'partial'
    >>> a.direction
    'right'
    ```

    ```python
    >>> mxBeam = EL('<beam>backward hook</beam>')
    >>> a = MP.xmlToBeam(mxBeam)
    >>> a.type
    'partial'
    >>> a.direction
    'left'
    ```

    ```python
    >>> mxBeam = EL('<beam>crazy</beam>')
    >>> a = MP.xmlToBeam(mxBeam)
    Traceback (most recent call last):
    music21.musicxml.xmlObjects.MusicXMLImportException:
         unexpected beam type encountered (crazy)
    ```

MeasureParser.xmlToBeams(*mxBeamList*, *inputM21=None*)[[source]](../_modules/music21/musicxml/xmlToM21.html#MeasureParser.xmlToBeams)
:   given a list of mxBeam objects, sets the beamsList

    ```python
    >>> from xml.etree.ElementTree import fromstring as EL
    >>> MP = musicxml.xmlToM21.MeasureParser()
    ```

    ```python
    >>> mxBeam1 = EL('<beam>begin</beam>')
    >>> mxBeam2 = EL('<beam>begin</beam>')
    >>> mxBeamList = [mxBeam1, mxBeam2]
    >>> b = MP.xmlToBeams(mxBeamList)
    >>> b
    <music21.beam.Beams <music21.beam.Beam 1/start>/<music21.beam.Beam 2/start>>
    ```

MeasureParser.xmlToChord(*mxNoteList: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")]*) → [ChordBase](moduleChord.html#music21.chord.ChordBase "music21.chord.ChordBase")[[source]](../_modules/music21/musicxml/xmlToM21.html#MeasureParser.xmlToChord)
:   Given a list of mxNotes, fill the necessary parameters

    ```python
    >>> from xml.etree.ElementTree import fromstring as EL
    >>> MP = musicxml.xmlToM21.MeasureParser()
    >>> MP.divisions = 10080
    ```

    ```python
    >>> qnDuration = r'<duration>7560</duration><type>quarter</type>'
    ```

    ```python
    >>> a = EL(r'<note><pitch><step>A</step><octave>3</octave></pitch>'
    ...          + qnDuration + '</note>')
    >>> b = EL(r'<note><chord/><pitch><step>B</step><octave>3</octave></pitch>'
    ...          + qnDuration + '</note>')
    ```

    ```python
    >>> c = MP.xmlToChord([a, b])
    >>> len(c.pitches)
    2
    >>> c.pitches[0]
    <music21.pitch.Pitch A3>
    >>> c.pitches[1]
    <music21.pitch.Pitch B3>
    >>> c.duration
    <music21.duration.Duration unlinked type:quarter quarterLength:0.75>
    ```

    ```python
    >>> a = EL('<note><pitch><step>A</step><octave>3</octave></pitch>'
    ...        + qnDuration
    ...        + '<notehead>diamond</notehead></note>')
    >>> c = MP.xmlToChord([a, b])
    >>> c.getNotehead(c.pitches[0])
    'diamond'
    ```

    ```python
    >>> a = EL('<note><unpitched><display-step>A</display-step>'
    ...        + '<display-octave>3</display-octave></unpitched>'
    ...        + qnDuration
    ...        + '<notehead>diamond</notehead></note>')
    >>> MP.xmlToChord([a, b])
    <music21.percussion.PercussionChord [unpitched[A3] B3]>
    ```

MeasureParser.xmlToChordSymbol(*mxHarmony: [Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")*) → [ChordSymbol](moduleHarmony.html#music21.harmony.ChordSymbol "music21.harmony.ChordSymbol") | [NoChord](moduleHarmony.html#music21.harmony.NoChord "music21.harmony.NoChord") | [ChordWithFretBoard](moduleTablature.html#music21.tablature.ChordWithFretBoard "music21.tablature.ChordWithFretBoard")[[source]](../_modules/music21/musicxml/xmlToM21.html#MeasureParser.xmlToChordSymbol)
:   Convert a <harmony> tag to a harmony.ChordSymbol object:

    ```python
    >>> from xml.etree.ElementTree import fromstring as EL
    >>> MP = musicxml.xmlToM21.MeasureParser()
    ```

    ```python
    >>> elStr = '<harmony><root><root-step>D</root-step><root-alter>-1</root-alter>'
    >>> elStr += '</root><kind>major-seventh</kind></harmony>'
    >>> mxHarmony = EL(elStr)
    ```

    ```python
    >>> cs = MP.xmlToChordSymbol(mxHarmony)
    >>> cs
    <music21.harmony.ChordSymbol D-maj7>
    ```

    ```python
    >>> cs.figure
    'D-maj7'
    ```

    ```python
    >>> cs.pitches
    (<music21.pitch.Pitch D-3>,
     <music21.pitch.Pitch F3>,
     <music21.pitch.Pitch A-3>,
     <music21.pitch.Pitch C4>)
    ```

    ```python
    >>> cs.root()
    <music21.pitch.Pitch D-3>
    ```

    TODO: this is very classically-oriented. Make more Jazz/Rock like possible/default?.

    ```python
    >>> mxHarmony.find('kind').text = 'major-sixth'
    >>> cs = MP.xmlToChordSymbol(mxHarmony)
    >>> cs
    <music21.harmony.ChordSymbol D-6>
    ```

    ```python
    >>> cs.figure
    'D-6'
    ```

    ```python
    >>> cs.pitches
    (<music21.pitch.Pitch D-3>, <music21.pitch.Pitch F3>,
     <music21.pitch.Pitch A-3>, <music21.pitch.Pitch B-3>)
    ```

    ```python
    >>> cs.root()
    <music21.pitch.Pitch D-3>
    ```

MeasureParser.xmlToClef(*mxClef*)[[source]](../_modules/music21/musicxml/xmlToM21.html#MeasureParser.xmlToClef)
:   Returns a music21 Clef object from an mxClef element.

    ```python
    >>> import xml.etree.ElementTree as ET
    >>> mxClef = ET.fromstring('<clef><sign>G</sign><line>2</line></clef>')
    ```

    ```python
    >>> MP = musicxml.xmlToM21.MeasureParser()
    >>> MP.xmlToClef(mxClef)
    <music21.clef.TrebleClef>
    ```

    ```python
    >>> mxClef = ET.fromstring('<clef><sign>G</sign><line>2</line>'
    ...                        + '<clef-octave-change>-1</clef-octave-change></clef>')
    >>> MP.xmlToClef(mxClef)
    <music21.clef.Treble8vbClef>
    ```

    ```python
    >>> mxClef = ET.fromstring('<clef><sign>TAB</sign></clef>')
    >>> MP.xmlToClef(mxClef)
    <music21.clef.TabClef>
    ```

MeasureParser.xmlToDuration(*mxNote*, *inputM21=None*)[[source]](../_modules/music21/musicxml/xmlToM21.html#MeasureParser.xmlToDuration)
:   Translate a MusicXML <note> object’s
    <duration>, <type>, <dot>, tuplets, etc.
    to a music21 [`Duration`](moduleDuration.html#music21.duration.Duration "music21.duration.Duration") object.

    ```python
    >>> from xml.etree.ElementTree import fromstring as EL
    >>> MP = musicxml.xmlToM21.MeasureParser()
    ```

    ```python
    >>> MP.divisions = 10080
    ```

    ```python
    >>> mxNote = EL('<note><pitch><step>D</step>' +
    ...     '<alter>-1</alter><octave>6</octave></pitch>' +
    ...     '<duration>7560</duration>' +
    ...     '<type>eighth</type><dot/></note>')
    ```

    ```python
    >>> c = duration.Duration()
    >>> MP.xmlToDuration(mxNote, c)
    >>> c
    <music21.duration.Duration 0.75>
    >>> c.quarterLength
    0.75
    >>> c.type
    'eighth'
    >>> c.dots
    1
    ```

    If the <duration> doesn’t match the <type> and <dots>,
    an unlinked duration is created so that .quarterLength agrees with
    <duration> but the notated types can still be represented.

    Create a second dot on mxNote and parse again, observing the identical
    quarterLength:

    ```python
    >>> from xml.etree.ElementTree import SubElement
    >>> unused = SubElement(mxNote, 'dot')
    >>> c2 = MP.xmlToDuration(mxNote)
    >>> c2
    <music21.duration.Duration unlinked type:eighth quarterLength:0.75>
    >>> c2.quarterLength
    0.75
    >>> c2.type
    'eighth'
    >>> c2.dots
    2
    ```

    Grace note durations will be converted later to GraceDurations:

    ```python
    >>> mxDuration = mxNote.find('duration')
    >>> mxNote.remove(mxDuration)
    >>> mxGrace = SubElement(mxNote, 'grace')
    >>> MP.xmlToDuration(mxNote, inputM21=c2)
    >>> c2
    <music21.duration.Duration unlinked type:eighth quarterLength:0.0>
    >>> gn1 = note.Note(duration=c2)
    >>> gn2 = MP.xmlGraceToGrace(mxGrace, gn1)
    >>> gn2.duration
    <music21.duration.GraceDuration unlinked type:eighth quarterLength:0.0>
    ```

MeasureParser.xmlToKeySignature(*mxKey*)[[source]](../_modules/music21/musicxml/xmlToM21.html#MeasureParser.xmlToKeySignature)
:   Returns either a KeySignature (traditional or non-traditional)
    or a Key object based on whether fifths and mode is present.

    ```python
    >>> import xml.etree.ElementTree as ET
    >>> mxKey = ET.fromstring('<key><fifths>-4</fifths></key>')
    ```

    ```python
    >>> MP = musicxml.xmlToM21.MeasureParser()
    >>> MP.xmlToKeySignature(mxKey)
    <music21.key.KeySignature of 4 flats>
    ```

    ```python
    >>> mxKey = ET.fromstring('<key><fifths>-4</fifths><mode>minor</mode></key>')
    ```

    ```python
    >>> MP = musicxml.xmlToM21.MeasureParser()
    >>> MP.xmlToKeySignature(mxKey)
    <music21.key.Key of f minor>
    ```

    Invalid modes get ignored and returned as KeySignatures

    ```python
    >>> mxKey = ET.fromstring('<key><fifths>-4</fifths><mode>crazy</mode></key>')
    ```

    ```python
    >>> MP = musicxml.xmlToM21.MeasureParser()
    >>> MP.xmlToKeySignature(mxKey)
    <music21.key.KeySignature of 4 flats>
    ```

MeasureParser.xmlToLyric(*mxLyric*, *inputM21=None*) → [Lyric](moduleNote.html#music21.note.Lyric "music21.note.Lyric") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/musicxml/xmlToM21.html#MeasureParser.xmlToLyric)
:   Translate a MusicXML <lyric> tag to a
    music21 [`Lyric`](moduleNote.html#music21.note.Lyric "music21.note.Lyric") object or return None if no Lyric object
    should be created (empty lyric tags, for instance)

    If inputM21 is a [`Lyric`](moduleNote.html#music21.note.Lyric "music21.note.Lyric") object, then the values of the
    mxLyric are transferred there and nothing returned.

    Otherwise, a new Lyric object is created and returned.

    ```python
    >>> import xml.etree.ElementTree as ET
    >>> MP = musicxml.xmlToM21.MeasureParser()
    ```

    ```python
    >>> mxLyric = ET.fromstring('<lyric number="4" color="red">'
    ...                         + '<syllabic>single</syllabic>'
    ...                         + '<text>word</text></lyric>')
    >>> lyricObj = note.Lyric()
    >>> MP.xmlToLyric(mxLyric, lyricObj)
    >>> lyricObj
    <music21.note.Lyric number=4 syllabic=single text='word'>
    >>> lyricObj.style.color
    'red'
    ```

    Non-numeric MusicXML lyric “number”s are converted to identifiers:

    ```python
    >>> mxLyric.set('number', 'part2verse1')
    >>> l2 = MP.xmlToLyric(mxLyric)
    >>> l2
    <music21.note.Lyric number=0 identifier='part2verse1' syllabic=single text='word'>
    ```

    Multiple texts can be created and result in composite lyrics

    ```python
    >>> mxBianco = ET.fromstring('<lyric>'
    ...                         + '<syllabic>end</syllabic>'
    ...                         + '<text>co</text>'
    ...                         + '<elision>_</elision>'
    ...                         + '<syllabic>single</syllabic>'
    ...                         + '<text>e</text>'
    ...                         + '</lyric>')
    >>> bianco = MP.xmlToLyric(mxBianco)
    >>> bianco
    <music21.note.Lyric number=0 syllabic=composite text='co_e'>
    >>> bianco.components
    [<music21.note.Lyric number=1 syllabic=end text='co'>,
     <music21.note.Lyric number=1 syllabic=single text='e'>]
    ```

MeasureParser.xmlToNote(*mxNote: [Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/musicxml/xmlToM21.html#MeasureParser.xmlToNote)
:   Handles everything for creating a Note or Rest or Chord

    Does not actually return the note, but sets self.nLast to the note.

    This routine uses coreInserts for speed, so it can leave either
    self.stream or a Voice object within self.stream in an unstable state.

MeasureParser.xmlToOffset(*mxObj*)[[source]](../_modules/music21/musicxml/xmlToM21.html#MeasureParser.xmlToOffset)
:   Finds an <offset> inside the mxObj and returns it as
    a music21 offset (in quarterLengths)

    ```python
    >>> from xml.etree.ElementTree import fromstring as EL
    >>> MP = musicxml.xmlToM21.MeasureParser()
    >>> MP.divisions = 40
    >>> off = EL(r'<direction><offset>100</offset></direction>')
    >>> MP.xmlToOffset(off)
    2.5
    ```

    Returns a float, not fraction.

    ```python
    >>> MP.divisions = 30
    >>> off = EL(r'<direction><offset>10</offset></direction>')
    >>> MP.xmlToOffset(off)
    0.33333...
    ```

MeasureParser.xmlToPitch(*mxNote*, *inputM21=None*)[[source]](../_modules/music21/musicxml/xmlToM21.html#MeasureParser.xmlToPitch)
:   Given a MusicXML Note object, set this Pitch object to its values.

    ```python
    >>> from xml.etree.ElementTree import fromstring as EL
    >>> MP = musicxml.xmlToM21.MeasureParser()
    ```

    ```python
    >>> b = EL('<note><pitch><step>E</step><alter>-1</alter>'
    ...        + '<octave>3</octave></pitch></note>')
    >>> a = MP.xmlToPitch(b)
    >>> print(a)
    E-3
    ```

    Conflicting alter and accidental – alter is still stored, but name is :

    ```python
    >>> b = EL('<note><pitch><step>E</step><alter>-1</alter><octave>3</octave></pitch>'
    ...              + '<accidental>sharp</accidental></note>')
    >>> a = MP.xmlToPitch(b)
    >>> print(a)
    E#3
    >>> a.fullName
    'E-sharp in octave 3'
    ```

    ```python
    >>> a.accidental.alter
    -1.0
    ```

    ```python
    >>> a.accidental.name
    'sharp'
    ```

    ```python
    >>> a.accidental.modifier
    '#'
    ```

MeasureParser.xmlToRehearsalMark(*mxRehearsal*)[[source]](../_modules/music21/musicxml/xmlToM21.html#MeasureParser.xmlToRehearsalMark)
:   Return a rehearsal mark from a rehearsal tag.

MeasureParser.xmlToRepeat(*mxBarline*, *inputM21=None*)[[source]](../_modules/music21/musicxml/xmlToM21.html#MeasureParser.xmlToRepeat)
:   Given an mxBarline (not an mxRepeat object) with repeatObj as a parameter,
    file the necessary parameters and return a bar.Repeat() object

    ```python
    >>> import xml.etree.ElementTree as ET
    >>> MP = musicxml.xmlToM21.MeasureParser()
    ```

    ```python
    >>> mxBarline = ET.fromstring('<barline><bar-style>light-heavy</bar-style>' +
    ...       '<repeat direction="backward"/></barline>')
    >>> r = MP.xmlToRepeat(mxBarline)
    >>> r
    <music21.bar.Repeat direction=end>
    ```

    Test that the music21 type for a backwards repeat is called “final”
    (because it resembles a final barline) even though the musicxml style
    is called light-heavy.

    ```python
    >>> r.type
    'final'
    >>> r.direction
    'end'
    ```

    Test that a forward repeat with times doesn’t raise an exception, and
    that the resulting Repeat doesn’t have times set.

    ```python
    >>> mxStartBarline = ET.fromstring('<barline><bar-style>light-heavy</bar-style>' +
    ...       '<repeat direction="forward" times="2"/></barline>')
    >>> rs = MP.xmlToRepeat(mxStartBarline)
    >>> rs
    <music21.bar.Repeat direction=start>
    ```

MeasureParser.xmlToRest(*mxRest*)[[source]](../_modules/music21/musicxml/xmlToM21.html#MeasureParser.xmlToRest)
:   Takes a <note> tag that has been shown to have a <rest> tag in it
    and return a rest.

    ```python
    >>> from xml.etree.ElementTree import fromstring as EL
    >>> MP = musicxml.xmlToM21.MeasureParser()
    >>> MP.divisions = 10
    ```

    ```python
    >>> mxr = EL('<note><rest/><duration>5</duration><type>eighth</type></note>')
    >>> r = MP.xmlToRest(mxr)
    >>> r
    <music21.note.Rest eighth>
    >>> r.duration.quarterLength
    0.5
    ```

    ```python
    >>> mxr = EL('<note><rest><display-step>G</display-step>' +
    ...              '<display-octave>4</display-octave>' +
    ...              '</rest><duration>5</duration><type>eighth</type></note>')
    >>> r = MP.xmlToRest(mxr)
    >>> r
    <music21.note.Rest eighth>
    ```

    A rest normally lies at B4 in treble clef, but here we have put it at
    G4, so we’ll shift it down two steps.

    ```python
    >>> r.stepShift
    -2
    ```

    Clef context matters, here we will set it for notes that don’t specify a staff:

    ```python
    >>> MP.lastClefs[musicxml.xmlToM21.NO_STAFF_ASSIGNED] = clef.BassClef()
    >>> r = MP.xmlToRest(mxr)
    ```

    Now this is a high rest:

    ```python
    >>> r.stepShift
    10
    ```

    Test full measure rest defined with measure=”yes” and a duration indicating
    four quarter notes:

    ```python
    >>> mxr = EL('<note><rest measure="yes"/><duration>40</duration></note>')
    >>> r = MP.xmlToRest(mxr)
    >>> MP.fullMeasureRest
    True
    ```

    Note that here set r’s .fullMeasure to True or always because it has no type.

    ```python
    >>> r.fullMeasure
    True
    ```

    Same goes for rests which define type of whole (or breve), regardless of duration:

    ```python
    >>> mxr = EL('<note><rest measure="yes"/><duration>40</duration><type>whole</type></note>')
    >>> r = MP.xmlToRest(mxr)
    >>> MP.fullMeasureRest
    True
    >>> r.fullMeasure
    True
    ```

    But a rest that defines measure=”yes” but has a type other than whole or breve
    will set MeasureParser to fullMeasureRest but not set fullMeasure = True
    on the music21 Rest object itself because pickup measures often use
    measure=”yes” in Finale, but display as quarter rests, etc.
    See <https://github.com/w3c-cg/musicxml/issues/478>

    ```python
    >>> mxr = EL('<note><rest measure="yes"/><duration>10</duration>'
    ...          + '<type>quarter</type></note>')
    >>> r = MP.xmlToRest(mxr)
    >>> MP.fullMeasureRest
    True
    >>> r.fullMeasure
    'auto'
    ```

MeasureParser.xmlToSimpleNote(*mxNote*, *freeSpanners=True*) → [Note](moduleNote.html#music21.note.Note "music21.note.Note") | [Unpitched](moduleNote.html#music21.note.Unpitched "music21.note.Unpitched")[[source]](../_modules/music21/musicxml/xmlToM21.html#MeasureParser.xmlToSimpleNote)
:   Translate a MusicXML <note> (without <chord/>)
    to a [`Note`](moduleNote.html#music21.note.Note "music21.note.Note").

    The spannerBundle parameter can be a list or a Stream
    for storing and processing Spanner objects.

    if freeSpanners is False then pending spanners will not be freed.

    ```python
    >>> from xml.etree.ElementTree import fromstring as EL
    >>> MP = musicxml.xmlToM21.MeasureParser()
    ```

    ```python
    >>> MP.divisions = 10080
    ```

    ```python
    >>> mxNote = EL('<note pizzicato="yes"><pitch><step>D</step>'
    ...             + '<alter>-1</alter><octave>6</octave></pitch>'
    ...             + '<duration>7560</duration>'
    ...             + '<type>eighth</type><dot/></note>')
    ```

    ```python
    >>> n = MP.xmlToSimpleNote(mxNote)
    >>> n
    <music21.note.Note D->
    >>> n.octave
    6
    >>> n.duration
    <music21.duration.Duration 0.75>
    >>> n.articulations
    [<music21.articulations.Pizzicato>]
    ```

    ```python
    >>> beams = EL('<beam>begin</beam>')
    >>> mxNote.append(beams)
    >>> n = MP.xmlToSimpleNote(mxNote)
    >>> n.beams
    <music21.beam.Beams <music21.beam.Beam 1/start>>
    ```

    ```python
    >>> stem = EL('<stem>up</stem>')
    >>> mxNote.append(stem)
    >>> n = MP.xmlToSimpleNote(mxNote)
    >>> n.stemDirection
    'up'
    ```

    # TODO: beams over rests?

MeasureParser.xmlToTempoIndication(*mxMetronome*, *mxWords=None*)[[source]](../_modules/music21/musicxml/xmlToM21.html#MeasureParser.xmlToTempoIndication)
:   Given an mxMetronome, convert to either a TempoIndication subclass,
    either a tempo.MetronomeMark or tempo.MetricModulation.

    ```python
    >>> from xml.etree.ElementTree import fromstring as EL
    >>> MP = musicxml.xmlToM21.MeasureParser()
    ```

    ```python
    >>> m = EL(r'<metronome><per-minute>125</per-minute>' +
    ...         '<beat-unit>half</beat-unit></metronome>')
    >>> MP.xmlToTempoIndication(m)
    <music21.tempo.MetronomeMark Half=125>
    ```

    Metric modulation:

    ```python
    >>> m = EL(r'<metronome><beat-unit>long</beat-unit><beat-unit>32nd</beat-unit>' +
    ...         '<beat-unit-dot/></metronome>')
    >>> MP.xmlToTempoIndication(m)
    <music21.tempo.MetricModulation
     <music21.tempo.MetronomeMark Imperfect Longa=None>=<music21.tempo.MetronomeMark
               Dotted 32nd=None>>
    ```

MeasureParser.xmlToTextExpression(*mxWords*)[[source]](../_modules/music21/musicxml/xmlToM21.html#MeasureParser.xmlToTextExpression)
:   Given an mxWords, create a `TextExpression`
    and set style attributes, fonts, position, etc.

    Calls setTextFormatting, which calls setPrintStyleAlign.

    ```python
    >>> from xml.etree.ElementTree import fromstring as EL
    >>> MP = musicxml.xmlToM21.MeasureParser()
    >>> m = EL('<words default-y="17" font-family="Courier" ' +
    ... 'font-style="italic" relative-x="-6">a tempo</words>')
    >>> te = MP.xmlToTextExpression(m)
    >>> te.content
    'a tempo'
    >>> te.style.relativeX
    -6
    >>> te.style.fontFamily
    ['Courier']
    ```

MeasureParser.xmlToTie(*mxNote*)[[source]](../_modules/music21/musicxml/xmlToM21.html#MeasureParser.xmlToTie)
:   Translate a MusicXML <note> with <tie> SubElements
    [`Tie`](moduleTie.html#music21.tie.Tie "music21.tie.Tie") object

    ```python
    >>> import xml.etree.ElementTree as ET
    >>> MP = musicxml.xmlToM21.MeasureParser()
    ```

    Create the incomplete part of a Note.

    ```python
    >>> mxNote = ET.fromstring('<note><tie type="start" />'
    ...            + '<notations>'
    ...            + '<tied line-type="dotted" placement="below" type="start" />'
    ...            + '</notations></note>')
    >>> m21Tie = MP.xmlToTie(mxNote)
    >>> m21Tie.type
    'start'
    >>> m21Tie.style
    'dotted'
    >>> m21Tie.placement
    'below'
    ```

    Same thing but with orientation instead of placement, which both get mapped to
    placement in Tie objects

    ```python
    >>> mxNote = ET.fromstring('<note><tie type="start" />'
    ...            + '<notations>'
    ...            + '<tied line-type="dotted" orientation="over" type="start" />'
    ...            + '</notations></note>')
    >>> tieObj = MP.xmlToTie(mxNote)
    >>> tieObj.placement
    'above'
    ```

MeasureParser.xmlToTimeSignature(*mxTime: [Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")*) → [TimeSignature](moduleMeterBase.html#music21.meter.base.TimeSignature "music21.meter.base.TimeSignature") | [SenzaMisuraTimeSignature](moduleMeterBase.html#music21.meter.base.SenzaMisuraTimeSignature "music21.meter.base.SenzaMisuraTimeSignature")[[source]](../_modules/music21/musicxml/xmlToM21.html#MeasureParser.xmlToTimeSignature)
:   Returns a TimeSignature or SenzaMisuraTimeSignature (for senza-misura)
    from a <time> block.

    ```python
    >>> import xml.etree.ElementTree as ET
    >>> MP = musicxml.xmlToM21.MeasureParser()
    ```

    ```python
    >>> mxTime = ET.fromstring('<time><beats>3</beats><beat-type>8</beat-type></time>')
    >>> MP.xmlToTimeSignature(mxTime)
    <music21.meter.TimeSignature 3/8>
    ```

    ```python
    >>> mxTime = ET.fromstring('<time symbol="common"><beats>4</beats>' +
    ...                                              '<beat-type>4</beat-type></time>')
    >>> MP.xmlToTimeSignature(mxTime).symbol
    'common'
    ```

    Multiple times:

    ```python
    >>> mxTime = ET.fromstring('<time><beats>3</beats><beat-type>8</beat-type>' +
    ...                              '<beats>4</beats><beat-type>4</beat-type></time>')
    >>> MP.xmlToTimeSignature(mxTime)
    <music21.meter.TimeSignature 3/8+4/4>
    ```

    ```python
    >>> mxTime = ET.fromstring('<time><beats>3+2</beats><beat-type>8</beat-type></time>')
    >>> ts32 = MP.xmlToTimeSignature(mxTime)
    >>> ts32
    <music21.meter.TimeSignature 3/8+2/8>
    ```

    Senza Misura

    ```python
    >>> mxSenza = ET.fromstring('<time><senza-misura>0</senza-misura></time>')
    >>> MP.xmlToTimeSignature(mxSenza)
    <music21.meter.SenzaMisuraTimeSignature 0>
    ```

    Small Duration Time Signatures

    ```python
    >>> mxTime = ET.fromstring('<time><beats>3</beats><beat-type>32</beat-type></time>')
    >>> MP.xmlToTimeSignature(mxTime)
    <music21.meter.TimeSignature 3/32>
    ```

    ```python
    >>> mxTime = ET.fromstring('<time><beats>3</beats><beat-type>64</beat-type></time>')
    >>> MP.xmlToTimeSignature(mxTime)
    <music21.meter.TimeSignature 3/64>
    ```

    ```python
    >>> mxTime = ET.fromstring('<time><beats>3</beats><beat-type>128</beat-type></time>')
    >>> MP.xmlToTimeSignature(mxTime)
    <music21.meter.TimeSignature 3/128>
    ```

MeasureParser.xmlToTremolo(*mxTremolo*, *n*)[[source]](../_modules/music21/musicxml/xmlToM21.html#MeasureParser.xmlToTremolo)
:   Converts an mxTremolo to either an expression to be added to n.expressions
    or to a spanner, returning either.

MeasureParser.xmlToTuplets(*mxNote: [Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Tuplet](moduleDuration.html#music21.duration.Tuplet "music21.duration.Tuplet")][[source]](../_modules/music21/musicxml/xmlToM21.html#MeasureParser.xmlToTuplets)
:   Given an mxNote, based on mxTimeModification
    and mxTuplet objects, return a list of Tuplet objects

    ```python
    >>> import xml.etree.ElementTree as ET
    >>> MP = musicxml.xmlToM21.MeasureParser()
    ```

    ```python
    >>> mxNote = ET.fromstring('<note><type>16th</type>' +
    ...    '<time-modification><actual-notes>5</actual-notes>' +
    ...    '<normal-notes>4</normal-notes></time-modification></note>')
    >>> tups = MP.xmlToTuplets(mxNote)
    >>> tups
    [<music21.duration.Tuplet 5/4/16th>]
    ```

    ```python
    >>> mxNote = ET.fromstring('<note><type>eighth</type>' +
    ...    '<time-modification><actual-notes>5</actual-notes>' +
    ...    '<normal-notes>3</normal-notes>' +
    ...    '<normal-type>16th</normal-type><normal-dot /><normal-dot />' +
    ...    '</time-modification></note>')
    >>> tup = MP.xmlToTuplets(mxNote)
    >>> tup
    [<music21.duration.Tuplet 5/3/16th>]
    >>> tup[0].durationNormal
    DurationTuple(type='16th', dots=2, quarterLength=0.4375)
    ```

MeasureParser.xmlToUnpitched(*mxUnpitched: [Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")*, *inputM21: [Unpitched](moduleNote.html#music21.note.Unpitched "music21.note.Unpitched") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [Unpitched](moduleNote.html#music21.note.Unpitched "music21.note.Unpitched")[[source]](../_modules/music21/musicxml/xmlToM21.html#MeasureParser.xmlToUnpitched)
:   Set displayStep and displayOctave from mxUnpitched.

    ```python
    >>> from xml.etree.ElementTree import fromstring as EL
    >>> MP = musicxml.xmlToM21.MeasureParser()
    >>> MP.divisions = 10080
    ```

    ```python
    >>> mxNote = EL('<note><duration>7560</duration><type>eighth</type></note>')
    >>> unpitched = EL('<unpitched>'
    ...                + '<display-step>E</display-step>'
    ...                + '<display-octave>5</display-octave>'
    ...                + '</unpitched>')
    >>> mxNote.append(unpitched)
    >>> n = MP.xmlToSimpleNote(mxNote)
    >>> n.displayStep
    'E'
    >>> n.displayOctave
    5
    >>> n.displayPitch().midi
    76
    ```

MeasureParser.xmlTransposeToInterval(*mxTranspose*)[[source]](../_modules/music21/musicxml/xmlToM21.html#MeasureParser.xmlTransposeToInterval)
:   Convert a MusicXML Transpose object to a music21 Interval object.

    ```python
    >>> import xml.etree.ElementTree as ET
    >>> MP = musicxml.xmlToM21.MeasureParser()
    ```

    ```python
    >>> t = ET.fromstring('<transpose><diatonic>-1</diatonic>'
    ...                   + '<chromatic>-2</chromatic></transpose>')
    >>> MP.xmlTransposeToInterval(t)
    <music21.interval.Interval M-2>
    ```

    ```python
    >>> t = ET.fromstring('<transpose><diatonic>-5</diatonic>'
    ...                   + '<chromatic>-9</chromatic></transpose>')
    >>> MP.xmlTransposeToInterval(t)
    <music21.interval.Interval M-6>
    ```

    Not mentioned in MusicXML XSD but supported in (Finale; MuseScore): octave-change
    refers to both diatonic and chromatic, so we will deal:

    ```python
    >>> t = ET.fromstring('<transpose id="x"><diatonic>-1</diatonic><chromatic>-2</chromatic>'
    ...         + '<octave-change>-1</octave-change></transpose>')
    >>> inv = MP.xmlTransposeToInterval(t)
    >>> inv
    <music21.interval.Interval M-9>
    >>> inv.id
    'x'
    ```

Methods inherited from [`SoundTagMixin`](moduleMusicxmlXmlSoundParser.html#music21.musicxml.xmlSoundParser.SoundTagMixin "music21.musicxml.xmlSoundParser.SoundTagMixin"):

|  |  |  |
| --- | --- | --- |
| * [`setSound()`](moduleMusicxmlXmlSoundParser.html#music21.musicxml.xmlSoundParser.SoundTagMixin.setSound "music21.musicxml.xmlSoundParser.SoundTagMixin.setSound") | * [`setSoundTempo()`](moduleMusicxmlXmlSoundParser.html#music21.musicxml.xmlSoundParser.SoundTagMixin.setSoundTempo "music21.musicxml.xmlSoundParser.SoundTagMixin.setSoundTempo") | * [`xmlSound()`](moduleMusicxmlXmlSoundParser.html#music21.musicxml.xmlSoundParser.SoundTagMixin.xmlSound "music21.musicxml.xmlSoundParser.SoundTagMixin.xmlSound") |

Methods inherited from [`XMLParserBase`](#music21.musicxml.xmlToM21.XMLParserBase "music21.musicxml.xmlToM21.XMLParserBase"):

|  |  |  |
| --- | --- | --- |
| * [`setColor()`](#music21.musicxml.xmlToM21.XMLParserBase.setColor "music21.musicxml.xmlToM21.XMLParserBase.setColor") * [`setEditorial()`](#music21.musicxml.xmlToM21.XMLParserBase.setEditorial "music21.musicxml.xmlToM21.XMLParserBase.setEditorial") * [`setFont()`](#music21.musicxml.xmlToM21.XMLParserBase.setFont "music21.musicxml.xmlToM21.XMLParserBase.setFont") * [`setLineStyle()`](#music21.musicxml.xmlToM21.XMLParserBase.setLineStyle "music21.musicxml.xmlToM21.XMLParserBase.setLineStyle") * [`setPlacement()`](#music21.musicxml.xmlToM21.XMLParserBase.setPlacement "music21.musicxml.xmlToM21.XMLParserBase.setPlacement") * [`setPosition()`](#music21.musicxml.xmlToM21.XMLParserBase.setPosition "music21.musicxml.xmlToM21.XMLParserBase.setPosition") | * [`setPrintObject()`](#music21.musicxml.xmlToM21.XMLParserBase.setPrintObject "music21.musicxml.xmlToM21.XMLParserBase.setPrintObject") * [`setPrintStyle()`](#music21.musicxml.xmlToM21.XMLParserBase.setPrintStyle "music21.musicxml.xmlToM21.XMLParserBase.setPrintStyle") * [`setPrintStyleAlign()`](#music21.musicxml.xmlToM21.XMLParserBase.setPrintStyleAlign "music21.musicxml.xmlToM21.XMLParserBase.setPrintStyleAlign") * [`setStyleAttributes()`](#music21.musicxml.xmlToM21.XMLParserBase.setStyleAttributes "music21.musicxml.xmlToM21.XMLParserBase.setStyleAttributes") * [`setTextFormatting()`](#music21.musicxml.xmlToM21.XMLParserBase.setTextFormatting "music21.musicxml.xmlToM21.XMLParserBase.setTextFormatting") | * [`xmlPageLayoutToPageLayout()`](#music21.musicxml.xmlToM21.XMLParserBase.xmlPageLayoutToPageLayout "music21.musicxml.xmlToM21.XMLParserBase.xmlPageLayoutToPageLayout") * [`xmlPrintToPageLayout()`](#music21.musicxml.xmlToM21.XMLParserBase.xmlPrintToPageLayout "music21.musicxml.xmlToM21.XMLParserBase.xmlPrintToPageLayout") * [`xmlPrintToSystemLayout()`](#music21.musicxml.xmlToM21.XMLParserBase.xmlPrintToSystemLayout "music21.musicxml.xmlToM21.XMLParserBase.xmlPrintToSystemLayout") * [`xmlStaffLayoutToStaffLayout()`](#music21.musicxml.xmlToM21.XMLParserBase.xmlStaffLayoutToStaffLayout "music21.musicxml.xmlToM21.XMLParserBase.xmlStaffLayoutToStaffLayout") * [`xmlSystemLayoutToSystemLayout()`](#music21.musicxml.xmlToM21.XMLParserBase.xmlSystemLayoutToSystemLayout "music21.musicxml.xmlToM21.XMLParserBase.xmlSystemLayoutToSystemLayout") |

## MusicXMLImporter

class music21.musicxml.xmlToM21.MusicXMLImporter[[source]](../_modules/music21/musicxml/xmlToM21.html#MusicXMLImporter)
:   Object for importing .xml, .mxl, .musicxml, MusicXML files into music21.

[`MusicXMLImporter`](#music21.musicxml.xmlToM21.MusicXMLImporter "music21.musicxml.xmlToM21.MusicXMLImporter") bases

* [`XMLParserBase`](#music21.musicxml.xmlToM21.XMLParserBase "music21.musicxml.xmlToM21.XMLParserBase")

[`MusicXMLImporter`](#music21.musicxml.xmlToM21.MusicXMLImporter "music21.musicxml.xmlToM21.MusicXMLImporter") methods

MusicXMLImporter.addIdentificationToMetadata(*identification: [Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")*, *md: [Metadata](moduleMetadata.html#music21.metadata.Metadata "music21.metadata.Metadata")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/musicxml/xmlToM21.html#MusicXMLImporter.addIdentificationToMetadata)
:   Given an <identification> tag, , containing <creator> tags, <rights> tags, and
    <miscellaneous> tags etc., add this information to the
    [`Metadata`](moduleMetadata.html#music21.metadata.Metadata "music21.metadata.Metadata") object passed in.

    (Replaces identificationToMetadata which is now deprecated.)

    Not supported: source, relation

    Only the first <rights> tag is supported

    Encoding only parses “supports” and that only has
    new-system (definesExplicitSystemBreaks) and
    new-page (definesExplicitPageBreaks)

MusicXMLImporter.creatorToContributor(*creator: [Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")*, *inputM21: [Contributor](moduleMetadataPrimitives.html#music21.metadata.primitives.Contributor "music21.metadata.primitives.Contributor") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](../_modules/music21/musicxml/xmlToM21.html#MusicXMLImporter.creatorToContributor)
:   Given a <creator> tag, fill the necessary parameters of a Contributor.

    ```python
    >>> import xml.etree.ElementTree as ET
    >>> creator = ET.fromstring('<creator type="composer">Beethoven, Ludwig van</creator>')
    ```

    ```python
    >>> MI = musicxml.xmlToM21.MusicXMLImporter()
    >>> c = MI.creatorToContributor(creator)
    >>> c
    <music21.metadata.primitives.Contributor composer:Beethoven, Ludwig van>
    >>> c.role
    'composer'
    >>> c.name
    'Beethoven, Ludwig van'
    ```

    Pass in a Contributor object and set it:

    ```python
    >>> c2 = metadata.Contributor()
    >>> MI.creatorToContributor(creator, c2)
    >>> c2.role
    'composer'
    ```

MusicXMLImporter.identificationToMetadata(*identification: [Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")*, *inputM21: [Metadata](moduleMetadata.html#music21.metadata.Metadata "music21.metadata.Metadata") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [Metadata](moduleMetadata.html#music21.metadata.Metadata "music21.metadata.Metadata") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/musicxml/xmlToM21.html#MusicXMLImporter.identificationToMetadata)
:   Deprecated – use addIdentificationToMetadata instead and always
    pass in a metadata object.

static MusicXMLImporter.isRecognizableMetadataKey(*miscFieldName: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/musicxml/xmlToM21.html#MusicXMLImporter.isRecognizableMetadataKey)
:   Returns bool on whether miscFieldName is a one of the names
    that is among the list of names we might see in <miscellaneous>,
    that this parser will interpret as supported metadata keys.
    Currently, this is all the uniqueName keys (e.g. ‘dateCreated’),
    the ‘namespace:name’ keys (e.g. ‘dcterms:created’),
    and the pre-v8 music21 workIds (e.g. ‘date’).

    ```python
    >>> MI = musicxml.xmlToM21.MusicXMLImporter()
    >>> MI.isRecognizableMetadataKey('dateCreated')
    True
    >>> MI.isRecognizableMetadataKey('dcterms:created')
    True
    >>> MI.isRecognizableMetadataKey('dateDestroyed')
    False
    ```

MusicXMLImporter.parsePartList(*mxScore*)[[source]](../_modules/music21/musicxml/xmlToM21.html#MusicXMLImporter.parsePartList)
:   Parses the <part-list> tag and adds
    <score-part> entries into self.mxScorePartDict[partId]
    and adds them to any open <part-group> entries,
    stored as PartGroup objects in self.partGroupList

MusicXMLImporter.parseXMLText()[[source]](../_modules/music21/musicxml/xmlToM21.html#MusicXMLImporter.parseXMLText)

MusicXMLImporter.partGroups()[[source]](../_modules/music21/musicxml/xmlToM21.html#MusicXMLImporter.partGroups)
:   set StaffGroup objects from the <part-group> tags.

MusicXMLImporter.processEncoding(*encoding: [Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")*, *md: [Metadata](moduleMetadata.html#music21.metadata.Metadata "music21.metadata.Metadata")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/musicxml/xmlToM21.html#MusicXMLImporter.processEncoding)
:   Process all information in the <encoding> element and put it into the
    Metadata object passed in as md.

    Currently only processes ‘software’ and these supports attributes:

    > * new-system = Metadata.definesExplicitSystemBreaks
    > * new-page = Metadata.definesExplicitPageBreaks

MusicXMLImporter.readFile(*filename*)[[source]](../_modules/music21/musicxml/xmlToM21.html#MusicXMLImporter.readFile)

MusicXMLImporter.rightsToCopyright(*rights*)[[source]](../_modules/music21/musicxml/xmlToM21.html#MusicXMLImporter.rightsToCopyright)
:   Given a <rights> tag, fill the necessary parameters of a
    [`Copyright`](moduleMetadataPrimitives.html#music21.metadata.primitives.Copyright "music21.metadata.primitives.Copyright") object.

    ```python
    >>> import xml.etree.ElementTree as ET
    >>> rights = ET.fromstring('<rights type="owner">CC-SA-BY</rights>')
    ```

    ```python
    >>> MI = musicxml.xmlToM21.MusicXMLImporter()
    >>> c = MI.rightsToCopyright(rights)
    >>> c
    <music21.metadata.primitives.Copyright CC-SA-BY>
    >>> c.role
    'owner'
    >>> str(c)
    'CC-SA-BY'
    ```

MusicXMLImporter.scoreFromFile(*filename*)[[source]](../_modules/music21/musicxml/xmlToM21.html#MusicXMLImporter.scoreFromFile)
:   main program: opens a file given by filename and returns a complete
    music21 Score from it.

MusicXMLImporter.styleFromXmlDefaults(*mxDefaults*)[[source]](../_modules/music21/musicxml/xmlToM21.html#MusicXMLImporter.styleFromXmlDefaults)
:   Set the appearance and font information from mxDefault
    <appearance>, <music-font>, <word-font>, <lyric-font> (multiple),
    and <lyric-language> tags.

    Here the demo does not include the <appearance> tag since that is
    documented in xmlAppearanceToStyle

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
    >>> st = MI.stream.style
    >>> st.musicFont
    <music21.style.TextStyle object at 0x10535c0f0>
    >>> st.musicFont.fontFamily
    ['Maestro', 'Opus']
    >>> st.musicFont.fontWeight
    'bold'
    >>> st.wordFont.fontFamily
    ['Garamond']
    >>> st.wordFont.fontStyle
    'italic'
    >>> len(st.lyricFonts)
    2
    >>> st.lyricFonts[0]
    ('verse', <music21.style.TextStyle object at 0x10535d438>)
    >>> st.lyricFonts[0][1].fontSize
    12
    >>> st.lyricLanguages
    [('verse', 'fr'), ('chorus', 'en')]
    ```

MusicXMLImporter.xmlAppearanceToStyle(*mxAppearance*)[[source]](../_modules/music21/musicxml/xmlToM21.html#MusicXMLImporter.xmlAppearanceToStyle)
:   Parse the appearance tag for information about line widths and note sizes

    ```python
    >>> import xml.etree.ElementTree as ET
    >>> appear = ET.fromstring('<appearance>'
    ...          + '<line-width type="beam">5</line-width>'
    ...          + '<line-width type="ledger">1.5625</line-width>'
    ...          + '<note-size type="grace">60</note-size>'
    ...          + '<distance type="hyphen">0.5</distance>'
    ...          + '<other-appearance type="sharps">dotted</other-appearance>'
    ...          + '</appearance>')
    ```

    ```python
    >>> MI = musicxml.xmlToM21.MusicXMLImporter()
    >>> MI.xmlAppearanceToStyle(appear)
    >>> st = MI.stream.style
    ```

    ```python
    >>> st.lineWidths
    [('beam', 5), ('ledger', 1.5625)]
    ```

    ```python
    >>> st.noteSizes
    [('grace', 60)]
    ```

    ```python
    >>> st.distances
    [('hyphen', 0.5)]
    ```

    ```python
    >>> st.otherAppearances
    [('sharps', 'dotted')]
    ```

MusicXMLImporter.xmlCreditToTextBox(*mxCredit*)[[source]](../_modules/music21/musicxml/xmlToM21.html#MusicXMLImporter.xmlCreditToTextBox)
:   Convert a MusicXML credit to a music21 TextBox

    ```python
    >>> import xml.etree.ElementTree as ET
    >>> credit = ET.fromstring(
    ...               '<credit page="2"><credit-words>Testing</credit-words></credit>')
    ```

    ```python
    >>> MI = musicxml.xmlToM21.MusicXMLImporter()
    >>> tb = MI.xmlCreditToTextBox(credit)
    >>> tb.page
    2
    >>> tb.content
    'Testing'
    ```

MusicXMLImporter.xmlDefaultsToScoreLayout(*mxDefaults*, *inputM21=None*)[[source]](../_modules/music21/musicxml/xmlToM21.html#MusicXMLImporter.xmlDefaultsToScoreLayout)
:   Convert a <defaults> tag to a [`ScoreLayout`](moduleLayout.html#music21.layout.ScoreLayout "music21.layout.ScoreLayout")
    object

MusicXMLImporter.xmlMetadata(*el: [Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *inputM21: [Metadata](moduleMetadata.html#music21.metadata.Metadata "music21.metadata.Metadata") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [Metadata](moduleMetadata.html#music21.metadata.Metadata "music21.metadata.Metadata") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/musicxml/xmlToM21.html#MusicXMLImporter.xmlMetadata)
:   Converts part of the root element into a metadata object

    Supported: work-title, work-number, opus, movement-number,
    movement-title, identification

MusicXMLImporter.xmlPartToPart(*mxPart*, *mxScorePart*)[[source]](../_modules/music21/musicxml/xmlToM21.html#MusicXMLImporter.xmlPartToPart)
:   Given a <part> object and the <score-part> object, parse a complete part.

MusicXMLImporter.xmlRootToScore(*mxScore*, *inputM21=None*)[[source]](../_modules/music21/musicxml/xmlToM21.html#MusicXMLImporter.xmlRootToScore)
:   parse an xml file into a Score() object.

Methods inherited from [`XMLParserBase`](#music21.musicxml.xmlToM21.XMLParserBase "music21.musicxml.xmlToM21.XMLParserBase"):

|  |  |  |
| --- | --- | --- |
| * [`setColor()`](#music21.musicxml.xmlToM21.XMLParserBase.setColor "music21.musicxml.xmlToM21.XMLParserBase.setColor") * [`setEditorial()`](#music21.musicxml.xmlToM21.XMLParserBase.setEditorial "music21.musicxml.xmlToM21.XMLParserBase.setEditorial") * [`setFont()`](#music21.musicxml.xmlToM21.XMLParserBase.setFont "music21.musicxml.xmlToM21.XMLParserBase.setFont") * [`setLineStyle()`](#music21.musicxml.xmlToM21.XMLParserBase.setLineStyle "music21.musicxml.xmlToM21.XMLParserBase.setLineStyle") * [`setPlacement()`](#music21.musicxml.xmlToM21.XMLParserBase.setPlacement "music21.musicxml.xmlToM21.XMLParserBase.setPlacement") * [`setPosition()`](#music21.musicxml.xmlToM21.XMLParserBase.setPosition "music21.musicxml.xmlToM21.XMLParserBase.setPosition") | * [`setPrintObject()`](#music21.musicxml.xmlToM21.XMLParserBase.setPrintObject "music21.musicxml.xmlToM21.XMLParserBase.setPrintObject") * [`setPrintStyle()`](#music21.musicxml.xmlToM21.XMLParserBase.setPrintStyle "music21.musicxml.xmlToM21.XMLParserBase.setPrintStyle") * [`setPrintStyleAlign()`](#music21.musicxml.xmlToM21.XMLParserBase.setPrintStyleAlign "music21.musicxml.xmlToM21.XMLParserBase.setPrintStyleAlign") * [`setStyleAttributes()`](#music21.musicxml.xmlToM21.XMLParserBase.setStyleAttributes "music21.musicxml.xmlToM21.XMLParserBase.setStyleAttributes") * [`setTextFormatting()`](#music21.musicxml.xmlToM21.XMLParserBase.setTextFormatting "music21.musicxml.xmlToM21.XMLParserBase.setTextFormatting") | * [`xmlPageLayoutToPageLayout()`](#music21.musicxml.xmlToM21.XMLParserBase.xmlPageLayoutToPageLayout "music21.musicxml.xmlToM21.XMLParserBase.xmlPageLayoutToPageLayout") * [`xmlPrintToPageLayout()`](#music21.musicxml.xmlToM21.XMLParserBase.xmlPrintToPageLayout "music21.musicxml.xmlToM21.XMLParserBase.xmlPrintToPageLayout") * [`xmlPrintToSystemLayout()`](#music21.musicxml.xmlToM21.XMLParserBase.xmlPrintToSystemLayout "music21.musicxml.xmlToM21.XMLParserBase.xmlPrintToSystemLayout") * [`xmlStaffLayoutToStaffLayout()`](#music21.musicxml.xmlToM21.XMLParserBase.xmlStaffLayoutToStaffLayout "music21.musicxml.xmlToM21.XMLParserBase.xmlStaffLayoutToStaffLayout") * [`xmlSystemLayoutToSystemLayout()`](#music21.musicxml.xmlToM21.XMLParserBase.xmlSystemLayoutToSystemLayout "music21.musicxml.xmlToM21.XMLParserBase.xmlSystemLayoutToSystemLayout") |

## PartGroup

class music21.musicxml.xmlToM21.PartGroup(*mxPartGroup*)[[source]](../_modules/music21/musicxml/xmlToM21.html#PartGroup)
:   Small helper class for keeping track of part-groups from XML since they
    are converted to StaffGroup spanners much later.

[`PartGroup`](#music21.musicxml.xmlToM21.PartGroup "music21.musicxml.xmlToM21.PartGroup") methods

PartGroup.add(*partGroupId*)[[source]](../_modules/music21/musicxml/xmlToM21.html#PartGroup.add)
:   Add a partGroupId to self.partGroupIds

## PartParser

class music21.musicxml.xmlToM21.PartParser(*mxPart: [Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *mxScorePart: [Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *parent: [MusicXMLImporter](#music21.musicxml.xmlToM21.MusicXMLImporter "music21.musicxml.xmlToM21.MusicXMLImporter") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](../_modules/music21/musicxml/xmlToM21.html#PartParser)
:   parser to work with a single <part> tag.

    called out for multiprocessing potential in future

[`PartParser`](#music21.musicxml.xmlToM21.PartParser "music21.musicxml.xmlToM21.PartParser") bases

* [`XMLParserBase`](#music21.musicxml.xmlToM21.XMLParserBase "music21.musicxml.xmlToM21.XMLParserBase")

[`PartParser`](#music21.musicxml.xmlToM21.PartParser "music21.musicxml.xmlToM21.PartParser") methods

PartParser.adjustTimeAttributesFromMeasure(*m: [Measure](moduleStreamBase.html#music21.stream.base.Measure "music21.stream.base.Measure")*)[[source]](../_modules/music21/musicxml/xmlToM21.html#PartParser.adjustTimeAttributesFromMeasure)
:   Adds padAsAnacrusis to pickup measures and other measures that
    do not fill the whole tile, if the first measure of the piece, or
    immediately follows an incomplete measure (such as a repeat sign mid-measure
    in a piece where each phrase begins with a pickup and ends with an
    incomplete measure).

    Fills an empty measure with a measure of rest (bug in PDFtoMusic and
    other MusicXML writers).

    Sets self.lastMeasureWasShort to True or False if it is an incomplete measure
    that is not a pickup and sets paddingRight.

    ```python
    >>> m = stream.Measure([meter.TimeSignature('4/4'), harmony.ChordSymbol('C7')])
    >>> m.highestTime
    0.0
    >>> pp = musicxml.xmlToM21.PartParser()
    >>> pp.setLastMeasureInfo(m)
    >>> pp.adjustTimeAttributesFromMeasure(m)
    >>> m.highestTime
    4.0
    >>> pp.lastMeasureWasShort
    False
    ```

    Incomplete final measure:

    ```python
    >>> m = stream.Measure([meter.TimeSignature('6/8'), note.Note(), note.Note()])
    >>> m.offset = 24.0
    >>> pp = musicxml.xmlToM21.PartParser()
    >>> pp.lastMeasureOffset = 21.0
    >>> pp.setLastMeasureInfo(m)
    >>> pp.adjustTimeAttributesFromMeasure(m)
    >>> m.paddingRight
    1.0
    ```

PartParser.applyMultiMeasureRest(*r: [Rest](moduleNote.html#music21.note.Rest "music21.note.Rest")*)[[source]](../_modules/music21/musicxml/xmlToM21.html#PartParser.applyMultiMeasureRest)
:   If there is an active MultiMeasureRestSpanner, add the Rest, r, to it:

    ```python
    >>> pp = musicxml.xmlToM21.PartParser()
    >>> mmrSpanner = spanner.MultiMeasureRest()
    >>> mmrSpanner
    <music21.spanner.MultiMeasureRest 0 measures>
    ```

    ```python
    >>> pp.activeMultiMeasureRestSpanner = mmrSpanner
    >>> pp.multiMeasureRestsToCapture = 2
    >>> r1 = note.Rest(type='whole', id='r1')
    >>> pp.applyMultiMeasureRest(r1)
    >>> pp.multiMeasureRestsToCapture
    1
    >>> pp.activeMultiMeasureRestSpanner
    <music21.spanner.MultiMeasureRest 1 measure>
    ```

    ```python
    >>> pp.activeMultiMeasureRestSpanner is mmrSpanner
    True
    >>> pp.stream.show('text')  # Nothing shown!
    ```

    ```python
    >>> r2 = note.Rest(type='whole', id='r2')
    >>> pp.applyMultiMeasureRest(r2)
    >>> pp.multiMeasureRestsToCapture
    0
    >>> pp.activeMultiMeasureRestSpanner is None
    True
    ```

    # spanner added to stream

    ```python
    >>> pp.stream.show('text')
    {0.0} <music21.spanner.MultiMeasureRest 2 measures>
    ```

    ```python
    >>> r3 = note.Rest(type='whole', id='r3')
    >>> pp.applyMultiMeasureRest(r3)
    >>> pp.stream.show('text')
    {0.0} <music21.spanner.MultiMeasureRest 2 measures>
    ```

PartParser.getDefaultInstrument(*mxScorePart: [Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [Instrument](moduleInstrument.html#music21.instrument.Instrument "music21.instrument.Instrument")[[source]](../_modules/music21/musicxml/xmlToM21.html#PartParser.getDefaultInstrument)
:   Get a default instrument from the mxScorePart tag.

    ```python
    >>> scorePart = ('<score-part id="P4"><part-name>Bass</part-name>'
    ...     + '<part-abbreviation>B.</part-abbreviation>'
    ...     + '<score-instrument id="P4-I4">'
    ...     + '    <instrument-name>Instrument 4</instrument-name>'
    ...     + '</score-instrument>'
    ...     + '<midi-instrument id="P4-I4">'
    ...     + '   <midi-channel>4</midi-channel>'
    ...     + '<midi-program>1</midi-program>'
    ...     + '</midi-instrument>'
    ...     + '</score-part>')
    >>> from xml.etree.ElementTree import fromstring as EL
    >>> pp = musicxml.xmlToM21.PartParser()
    ```

    ```python
    >>> mxScorePart = EL(scorePart)
    >>> i = pp.getDefaultInstrument(mxScorePart)
    >>> i
    <music21.instrument.Instrument ': Instrument 4'>
    >>> i.instrumentName
    'Instrument 4'
    ```

    Non-default transpositions captured as of v7.3:

    ```python
    >>> scorePart = ('<score-part id="P5"><part-name>C Trumpet</part-name>'
    ...     + '<part-abbreviation>C Tpt.</part-abbreviation>'
    ...     + '<score-instrument id="P5-I5">'
    ...     + '    <instrument-name>C Trumpet</instrument-name>'
    ...     + '</score-instrument>'
    ...     + '<midi-instrument id="P5-I5">'
    ...     + '   <midi-channel>2</midi-channel>'
    ...     + '<midi-program>57</midi-program>'
    ...     + '</midi-instrument>'
    ...     + '</score-part>')
    >>> from xml.etree.ElementTree import fromstring as EL
    >>> pp = musicxml.xmlToM21.PartParser()
    ```

    ```python
    >>> mxScorePart = EL(scorePart)
    >>> i = pp.getDefaultInstrument(mxScorePart)
    >>> i
    <music21.instrument.Trumpet ': C Trumpet'>
    >>> i.instrumentName
    'C Trumpet'
    >>> i.transposition
    <music21.interval.Interval P1>
    ```

PartParser.parse() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/musicxml/xmlToM21.html#PartParser.parse)
:   Run the parser on a single part

PartParser.parseMeasures()[[source]](../_modules/music21/musicxml/xmlToM21.html#PartParser.parseMeasures)
:   Parse each <measure> tag using self.xmlMeasureToMeasure

PartParser.parseXmlScorePart()[[source]](../_modules/music21/musicxml/xmlToM21.html#PartParser.parseXmlScorePart)
:   The <score-part> tag contains a lot of information about the
    Part itself. It was found in the <part-list> in the ScoreParser but
    was not parsed and instead passed into the PartParser as .mxScorePart.

    Sets the stream.partName, stream.partAbbreviation, self.activeInstrument,
    and inserts an instrument at the beginning of the stream.

    The instrumentObj being configured comes from self.getDefaultInstrument.

static PartParser.reclassifyInstrumentFromName(*i: [Instrument](moduleInstrument.html#music21.instrument.Instrument "music21.instrument.Instrument")*, *mxScoreInstrument: [Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")*) → [Instrument](moduleInstrument.html#music21.instrument.Instrument "music21.instrument.Instrument")[[source]](../_modules/music21/musicxml/xmlToM21.html#PartParser.reclassifyInstrumentFromName)

PartParser.removeFinaleIncorrectEndingForwardRest() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/musicxml/xmlToM21.html#PartParser.removeFinaleIncorrectEndingForwardRest)
:   If Finale generated the file AND it ended with an incomplete
    measure (like 4/4 beginning with a quarter pickup and ending
    with a 3-beat measure) then the file might have ended with a
    <forward> tag, which Finale used to create hidden rests.

    If this forward tag is at the end of the piece, then it
    will create rests that “complete” the measure in an incorrect way
    If voices are not involved (e.g., NOT bwv66.6) then we should
    remove this forward tag.

    * New in v7.

PartParser.separateOutPartStaves() → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[PartStaff](moduleStreamBase.html#music21.stream.base.PartStaff "music21.stream.base.PartStaff")][[source]](../_modules/music21/musicxml/xmlToM21.html#PartParser.separateOutPartStaves)
:   Take a Part with multiple staves and make them a set of PartStaff objects.

    There must be more than one staff to do this.

PartParser.setLastMeasureInfo(*m: [Measure](moduleStreamBase.html#music21.stream.base.Measure "music21.stream.base.Measure")*)[[source]](../_modules/music21/musicxml/xmlToM21.html#PartParser.setLastMeasureInfo)
:   Sets self.lastMeasureNumber and self.lastMeasureSuffix from the measure,
    which is used in fixing Finale unnumbered measure issues.

    Also sets self.lastTimeSignature from the timeSignature found in
    the measure, if any.

    ```python
    >>> pp = musicxml.xmlToM21.PartParser()
    ```

    Here are the defaults:

    ```python
    >>> pp.lastMeasureNumber
    0
    >>> pp.lastNumberSuffix is None
    True
    >>> pp.lastTimeSignature is None
    True
    ```

    After setLastMeasureInfo:

    ```python
    >>> m = stream.Measure(number=4)
    >>> m.numberSuffix = 'b'
    >>> ts38 = meter.TimeSignature('3/8')
    >>> m.timeSignature = ts38
    >>> pp.setLastMeasureInfo(m)
    ```

    ```python
    >>> pp.lastMeasureNumber
    4
    >>> pp.lastNumberSuffix
    'b'
    >>> pp.lastTimeSignature
    <music21.meter.TimeSignature 3/8>
    >>> pp.lastTimeSignature is ts38
    True
    ```

    Note that if there was no timeSignature defined in m,
    and no lastTimeSignature exists,
    the PartParser gets a default of 4/4, because
    after the first measure there’s going to be routines
    that need some sort of time signature:

    ```python
    >>> pp2 = musicxml.xmlToM21.PartParser()
    >>> m2 = stream.Measure(number=2)
    >>> pp2.setLastMeasureInfo(m2)
    >>> pp2.lastTimeSignature
    <music21.meter.TimeSignature 4/4>
    ```

    For obscure reasons relating to how Finale gives suffixes
    to unnumbered measures, if a measure has the same number
    as the lastMeasureNumber, the lastNumberSuffix is not updated:

    ```python
    >>> pp3 = musicxml.xmlToM21.PartParser()
    >>> pp3.lastMeasureNumber = 10
    >>> pp3.lastNumberSuffix = 'X1'
    ```

    ```python
    >>> m10 = stream.Measure(number=10)
    >>> m10.numberSuffix = 'X2'
    >>> pp3.setLastMeasureInfo(m10)
    >>> pp3.lastNumberSuffix
    'X1'
    ```

PartParser.updateTransposition(*newTransposition: [Interval](moduleInterval.html#music21.interval.Interval "music21.interval.Interval")*)[[source]](../_modules/music21/musicxml/xmlToM21.html#PartParser.updateTransposition)
:   As one might expect, a measureParser that reveals a change
    in transposition is going to have an effect on the
    Part’s instrument list. This (totally undocumented) method
    deals with it.

    If measureParser.transposition is None, does nothing.

    NOTE: Need to test a change of instrument w/o a change of
    transposition such as: Bb clarinet to Bb Soprano Sax to Eb clarinet?

PartParser.xmlMeasureToMeasure(*mxMeasure: [Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")*) → [Measure](moduleStreamBase.html#music21.stream.base.Measure "music21.stream.base.Measure")[[source]](../_modules/music21/musicxml/xmlToM21.html#PartParser.xmlMeasureToMeasure)
:   Convert a measure element to a Measure, using
    [`MeasureParser`](#music21.musicxml.xmlToM21.MeasureParser "music21.musicxml.xmlToM21.MeasureParser")

    ```python
    >>> from xml.etree.ElementTree import fromstring as EL
    ```

    Full-measure rests get auto-assigned to match the time signature if they
    do not have a type, or have a type of “whole”.

    Here is a measure with a rest that lasts 4 beats, but we will put it in a 3/4 context.

    ```python
    >>> scoreMeasure = '<measure><note><rest/><duration>40320</duration></note></measure>'
    >>> mxMeasure = EL(scoreMeasure)
    >>> pp = musicxml.xmlToM21.PartParser()
    >>> pp.lastDivisions
    10080
    >>> 40320 / 10080
    4.0
    >>> pp.lastTimeSignature = meter.TimeSignature('3/4')
    >>> m = pp.xmlMeasureToMeasure(mxMeasure)
    ```

    Test that the rest lasts three, not four beats:

    ```python
    >>> measureRest = m.notesAndRests[0]
    >>> measureRest
    <music21.note.Rest dotted-half>
    >>> measureRest.duration.type
    'half'
    >>> measureRest.duration.quarterLength
    3.0
    ```

Methods inherited from [`XMLParserBase`](#music21.musicxml.xmlToM21.XMLParserBase "music21.musicxml.xmlToM21.XMLParserBase"):

|  |  |  |
| --- | --- | --- |
| * [`setColor()`](#music21.musicxml.xmlToM21.XMLParserBase.setColor "music21.musicxml.xmlToM21.XMLParserBase.setColor") * [`setEditorial()`](#music21.musicxml.xmlToM21.XMLParserBase.setEditorial "music21.musicxml.xmlToM21.XMLParserBase.setEditorial") * [`setFont()`](#music21.musicxml.xmlToM21.XMLParserBase.setFont "music21.musicxml.xmlToM21.XMLParserBase.setFont") * [`setLineStyle()`](#music21.musicxml.xmlToM21.XMLParserBase.setLineStyle "music21.musicxml.xmlToM21.XMLParserBase.setLineStyle") * [`setPlacement()`](#music21.musicxml.xmlToM21.XMLParserBase.setPlacement "music21.musicxml.xmlToM21.XMLParserBase.setPlacement") * [`setPosition()`](#music21.musicxml.xmlToM21.XMLParserBase.setPosition "music21.musicxml.xmlToM21.XMLParserBase.setPosition") | * [`setPrintObject()`](#music21.musicxml.xmlToM21.XMLParserBase.setPrintObject "music21.musicxml.xmlToM21.XMLParserBase.setPrintObject") * [`setPrintStyle()`](#music21.musicxml.xmlToM21.XMLParserBase.setPrintStyle "music21.musicxml.xmlToM21.XMLParserBase.setPrintStyle") * [`setPrintStyleAlign()`](#music21.musicxml.xmlToM21.XMLParserBase.setPrintStyleAlign "music21.musicxml.xmlToM21.XMLParserBase.setPrintStyleAlign") * [`setStyleAttributes()`](#music21.musicxml.xmlToM21.XMLParserBase.setStyleAttributes "music21.musicxml.xmlToM21.XMLParserBase.setStyleAttributes") * [`setTextFormatting()`](#music21.musicxml.xmlToM21.XMLParserBase.setTextFormatting "music21.musicxml.xmlToM21.XMLParserBase.setTextFormatting") | * [`xmlPageLayoutToPageLayout()`](#music21.musicxml.xmlToM21.XMLParserBase.xmlPageLayoutToPageLayout "music21.musicxml.xmlToM21.XMLParserBase.xmlPageLayoutToPageLayout") * [`xmlPrintToPageLayout()`](#music21.musicxml.xmlToM21.XMLParserBase.xmlPrintToPageLayout "music21.musicxml.xmlToM21.XMLParserBase.xmlPrintToPageLayout") * [`xmlPrintToSystemLayout()`](#music21.musicxml.xmlToM21.XMLParserBase.xmlPrintToSystemLayout "music21.musicxml.xmlToM21.XMLParserBase.xmlPrintToSystemLayout") * [`xmlStaffLayoutToStaffLayout()`](#music21.musicxml.xmlToM21.XMLParserBase.xmlStaffLayoutToStaffLayout "music21.musicxml.xmlToM21.XMLParserBase.xmlStaffLayoutToStaffLayout") * [`xmlSystemLayoutToSystemLayout()`](#music21.musicxml.xmlToM21.XMLParserBase.xmlSystemLayoutToSystemLayout "music21.musicxml.xmlToM21.XMLParserBase.xmlSystemLayoutToSystemLayout") |

## XMLParserBase

class music21.musicxml.xmlToM21.XMLParserBase[[source]](../_modules/music21/musicxml/xmlToM21.html#XMLParserBase)
:   contains functions that could be called
    at multiple levels of parsing (Score, Part, Measure).

[`XMLParserBase`](#music21.musicxml.xmlToM21.XMLParserBase "music21.musicxml.xmlToM21.XMLParserBase") methods

XMLParserBase.setColor(*mxObject*, *m21Object*)[[source]](../_modules/music21/musicxml/xmlToM21.html#XMLParserBase.setColor)
:   Sets m21Object.style.color to be the same as color.

XMLParserBase.setEditorial(*mxObj*, *m21Obj*)[[source]](../_modules/music21/musicxml/xmlToM21.html#XMLParserBase.setEditorial)
:   Set editorial information from an mxObj

    ```python
    >>> from xml.etree.ElementTree import fromstring as El
    >>> XP = musicxml.xmlToM21.XMLParserBase()
    >>> mxObj = El('<a/>')
    >>> n = note.Note('C#4')
    ```

    Most common case:

    ```python
    >>> XP.setEditorial(mxObj, n)
    >>> n.hasEditorialInformation
    False
    ```

    ```python
    >>> mxObj = El('<note><footnote>Sharp is conjectural</footnote>'
    ...            + '<level reference="yes">2</level></note>')
    >>> XP.setEditorial(mxObj, n)
    >>> n.hasEditorialInformation
    True
    >>> len(n.editorial.footnotes)
    1
    >>> fn = n.editorial.footnotes[0]
    >>> fn
    <music21.editorial.Comment 'Sharp is conjectu...'>
    >>> fn.isFootnote
    True
    >>> fn.levelInformation
    '2'
    >>> fn.isReference
    True
    ```

    If no <footnote> tag exists, the editorial information will be found in
    comments:

    ```python
    >>> mxObj = El('<note><level reference="no">ed</level></note>')
    >>> n = note.Note('C#4')
    >>> XP.setEditorial(mxObj, n)
    >>> len(n.editorial.footnotes)
    0
    >>> len(n.editorial.comments)
    1
    >>> com = n.editorial.comments[0]
    >>> com.isReference
    False
    >>> com.text is None
    True
    >>> com.levelInformation
    'ed'
    ```

XMLParserBase.setFont(*mxObject*, *m21Object*)[[source]](../_modules/music21/musicxml/xmlToM21.html#XMLParserBase.setFont)
:   sets font-family, font-style, font-size, and font-weight as
    fontFamily (list), fontStyle, fontSize and fontWeight from
    an object into a TextStyle object

    conforms to attr-group %font in the MusicXML DTD

    ```python
    >>> from xml.etree.ElementTree import fromstring as El
    >>> XP = musicxml.xmlToM21.XMLParserBase()
    >>> mxObj = El('<text font-family="Courier,monospaced" font-style="italic" '
    ...            + 'font-size="24" font-weight="bold" />')
    ```

    ```python
    >>> te = expressions.TextExpression('hi!')
    >>> XP.setFont(mxObj, te)
    >>> te.style.fontFamily
    ['Courier', 'monospaced']
    >>> te.style.fontStyle
    'italic'
    >>> te.style.fontSize
    24
    >>> te.style.fontWeight
    'bold'
    ```

XMLParserBase.setLineStyle(*mxObject*, *m21Object*)[[source]](../_modules/music21/musicxml/xmlToM21.html#XMLParserBase.setLineStyle)
:   Sets four additional elements for line elements, conforms to entity
    %line-shape, %line-type, %dashed-formatting (dash-length and space-length)

XMLParserBase.setPlacement(*mxObject*, *m21Object*)[[source]](../_modules/music21/musicxml/xmlToM21.html#XMLParserBase.setPlacement)
:   Sets the placement for objects that have a .placement attribute
    (most but not all spanners) and sets the style.placement for those
    that don’t.

XMLParserBase.setPosition(*mxObject*, *m21Object*)[[source]](../_modules/music21/musicxml/xmlToM21.html#XMLParserBase.setPosition)
:   get positioning information for an object from
    default-x, default-y, relative-x, relative-y into
    the .style attribute’s absoluteX, relativeX, etc. attributes’

    conforms to attr-group %position in the MusicXML DTD

XMLParserBase.setPrintObject(*mxObject*, *m21Object*)[[source]](../_modules/music21/musicxml/xmlToM21.html#XMLParserBase.setPrintObject)
:   convert ‘print-object=”no”’ to m21Object.style.hideObjectOnPrint = True

XMLParserBase.setPrintStyle(*mxObject*, *m21Object*)[[source]](../_modules/music21/musicxml/xmlToM21.html#XMLParserBase.setPrintStyle)
:   get position, font, and color information from the mxObject
    into the m21Object, which must have style.TextStyle as its Style class.

    conforms to attr-group %print-style in the MusicXML DTD

XMLParserBase.setPrintStyleAlign(*mxObject*, *m21Object*)[[source]](../_modules/music21/musicxml/xmlToM21.html#XMLParserBase.setPrintStyleAlign)
:   runs setPrintStyle and then sets horizontalAlign and verticalAlign, on an
    m21Object, which must have style.TextStyle as its Style class.

    conforms to attr-group %print-style-align in the MusicXML DTD

XMLParserBase.setStyleAttributes(*mxObject*, *m21Object*, *musicXMLNames*, *m21Names=None*)[[source]](../_modules/music21/musicxml/xmlToM21.html#XMLParserBase.setStyleAttributes)
:   Takes an mxObject, a music21Object, and a list/tuple of musicXML names and
    a list/tuple of m21Names, and assigns each of the mxObject’s attributes
    that fits this style name to the corresponding style object’s m21Name attribute.

    ```python
    >>> from xml.etree.ElementTree import fromstring as El
    >>> XP = musicxml.xmlToM21.XMLParserBase()
    >>> mxObj = El('<a x="20.1" y="10.0" z="yes" />')
    >>> m21Obj = base.Music21Object()
    >>> musicXMLNames = ('w', 'x', 'y', 'z')
    >>> m21Names = ('justify', 'absoluteX', 'absoluteY', 'hideObjectOnPrint')
    ```

    ```python
    >>> XP.setStyleAttributes(mxObj, m21Obj, musicXMLNames, m21Names)
    ```

    .justify requires a TextStyle object.

    ```python
    >>> m21Obj.style.justify
    Traceback (most recent call last):
    AttributeError: 'Style' object has no attribute 'justify'
    ```

    ```python
    >>> m21Obj.style.absoluteX
    20.1
    >>> m21Obj.style.absoluteY
    10
    >>> m21Obj.style.hideObjectOnPrint
    True
    ```

XMLParserBase.setTextFormatting(*mxObject*, *m21Object*)[[source]](../_modules/music21/musicxml/xmlToM21.html#XMLParserBase.setTextFormatting)
:   sets the justification, print-style-align group, and
    text-decoration, text-rotation,
    letter-spacing, line-height, lang, text-direction, and
    enclosure, on an
    m21Object, which must have style.TextStyle as its Style class,
    and then calls setPrintStyleAlign

    conforms to attr-group %text-formatting in the MusicXML DTD

XMLParserBase.xmlPageLayoutToPageLayout(*mxPageLayout*, *inputM21=None*)[[source]](../_modules/music21/musicxml/xmlToM21.html#XMLParserBase.xmlPageLayoutToPageLayout)
:   get a PageLayout object from an mxPageLayout

    Called out from mxPrintToPageLayout because it
    is also used in the <defaults> tag

XMLParserBase.xmlPrintToPageLayout(*mxPrint*, *inputM21=None*)[[source]](../_modules/music21/musicxml/xmlToM21.html#XMLParserBase.xmlPrintToPageLayout)
:   Given an mxPrint object, set object data for
    the print section of a layout.PageLayout object

    ```python
    >>> from xml.etree.ElementTree import fromstring as El
    >>> MP = musicxml.xmlToM21.MeasureParser()
    ```

    ```python
    >>> mxPrint = El('<print new-page="yes" page-number="5">'
    ...    + '    <page-layout><page-height>4000</page-height>'
    ...    + '        <page-margins><left-margin>20</left-margin>'
    ...    + '                 <right-margin>30.25</right-margin></page-margins>'
    ...    + '</page-layout></print>')
    ```

    ```python
    >>> pl = MP.xmlPrintToPageLayout(mxPrint)
    >>> pl.isNew
    True
    >>> pl.rightMargin
    30.25
    >>> pl.leftMargin
    20
    >>> pl.pageNumber
    5
    >>> pl.pageHeight
    4000
    ```

XMLParserBase.xmlPrintToSystemLayout(*mxPrint*, *inputM21=None*)[[source]](../_modules/music21/musicxml/xmlToM21.html#XMLParserBase.xmlPrintToSystemLayout)
:   Given an mxPrint object, set object data

    ```python
    >>> from xml.etree.ElementTree import fromstring as El
    >>> MP = musicxml.xmlToM21.MeasureParser()
    ```

    ```python
    >>> mxPrint = El('<print new-system="yes">'
    ...    + '    <system-layout><system-distance>55</system-distance>'
    ...    + '        <system-margins><left-margin>20</left-margin>'
    ...    + '                 <right-margin>30.25</right-margin></system-margins>'
    ...    + '</system-layout></print>')
    >>> sl = MP.xmlPrintToSystemLayout(mxPrint)
    >>> sl.isNew
    True
    >>> sl.rightMargin
    30.25
    >>> sl.leftMargin
    20
    >>> sl.distance
    55
    ```

XMLParserBase.xmlStaffLayoutToStaffLayout(*mxStaffLayout*, *inputM21=None*)[[source]](../_modules/music21/musicxml/xmlToM21.html#XMLParserBase.xmlStaffLayoutToStaffLayout)
:   get a StaffLayout object from an <staff-layout> tag

    In music21, the <staff-layout> and <staff-details> are
    intertwined in a StaffLayout object.

XMLParserBase.xmlSystemLayoutToSystemLayout(*mxSystemLayout*, *inputM21=None*)[[source]](../_modules/music21/musicxml/xmlToM21.html#XMLParserBase.xmlSystemLayoutToSystemLayout)
:   get a SystemLayout object from an <system-layout> element

    Called out from xmlPrintToSystemLayout because it
    is also used in the <defaults> tag

## Functions

music21.musicxml.xmlToM21.musicXMLTypeToType(*value: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](../_modules/music21/musicxml/xmlToM21.html#musicXMLTypeToType)
:   Utility function to convert a MusicXML duration type to a music21 duration type.

    Changes ‘long’ to ‘longa’ and deals with a Guitar Pro 5.2 bug in MusicXML
    export, that exports a 32nd note with the type ‘32th’.

    ```python
    >>> musicxml.xmlToM21.musicXMLTypeToType('long')
    'longa'
    >>> musicxml.xmlToM21.musicXMLTypeToType('32th')
    '32nd'
    >>> musicxml.xmlToM21.musicXMLTypeToType('quarter')
    'quarter'
    >>> musicxml.xmlToM21.musicXMLTypeToType(None)
    Traceback (most recent call last):
    music21.musicxml.xmlObjects.MusicXMLImportException:
        found unknown MusicXML type: None
    ```

music21.musicxml.xmlToM21.strippedText(*mxObj: [Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](../_modules/music21/musicxml/xmlToM21.html#strippedText)
:   Returns the mxObj.text.strip() from an Element (or None)
    taking into account that .text might be None, or the
    Element might be undefined.

    Replacement for the older textStripValid()

    ```python
    >>> from xml.etree.ElementTree import Element
    >>> e = Element('an-element')
    >>> musicxml.xmlToM21.strippedText(e)
    ''
    >>> e.text = '    '
    >>> musicxml.xmlToM21.strippedText(e)
    ''
    >>> e.text = '  hello  '
    >>> musicxml.xmlToM21.strippedText(e)
    'hello'
    ```

    ```python
    >>> musicxml.xmlToM21.strippedText(None)
    ''
    >>> musicxml.xmlToM21.strippedText(440.0)
    ''
    ```

    New in v9.
