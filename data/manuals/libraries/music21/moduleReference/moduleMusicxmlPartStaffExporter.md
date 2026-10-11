Source: https://music21.org/music21docs/moduleReference/moduleMusicxmlPartStaffExporter.html

# music21.musicxml.partStaffExporter

A mixin to ScoreExporter that includes the capabilities for producing a single
MusicXML <part> from multiple music21 PartStaff objects.

## PartStaffExporterMixin

class music21.musicxml.partStaffExporter.PartStaffExporterMixin[[source]](../_modules/music21/musicxml/partStaffExporter.html#PartStaffExporterMixin)

[`PartStaffExporterMixin`](#music21.musicxml.partStaffExporter.PartStaffExporterMixin "music21.musicxml.partStaffExporter.PartStaffExporterMixin") methods

PartStaffExporterMixin.addStaffTagsMultiStaffParts(*group: [StaffGroup](moduleLayout.html#music21.layout.StaffGroup "music21.layout.StaffGroup")*)[[source]](../_modules/music21/musicxml/partStaffExporter.html#PartStaffExporterMixin.addStaffTagsMultiStaffParts)
:   Create child <staff> tags under each <note>, <direction>, and <forward> element
    in the <part>s being joined.

    Called by [`joinPartStaffs()`](#music21.musicxml.partStaffExporter.PartStaffExporterMixin.joinPartStaffs "music21.musicxml.partStaffExporter.PartStaffExporterMixin.joinPartStaffs").

    ```python
    >>> from music21.musicxml import testPrimitive
    >>> s = converter.parse(testPrimitive.pianoStaff43a)
    >>> SX = musicxml.m21ToXml.ScoreExporter(s)
    >>> root = SX.parse()
    >>> m1 = root.find('part/measure')
    >>> SX.dump(m1)
    <measure implicit="no" number="1">
    ...
      <note>
        <pitch>
          <step>F</step>
          <octave>4</octave>
        </pitch>
        <duration>40320</duration>
        <voice>1</voice>
        <type>whole</type>
        <staff>1</staff>
      </note>
      <backup>
        <duration>40320</duration>
      </backup>
      <note>
        <pitch>
          <step>B</step>
          <octave>2</octave>
        </pitch>
        <duration>40320</duration>
        <voice>2</voice>
        <type>whole</type>
        <staff>2</staff>
      </note>
    </measure>
    ```

PartStaffExporterMixin.cleanUpSubsequentPartStaffs(*group: [StaffGroup](moduleLayout.html#music21.layout.StaffGroup "music21.layout.StaffGroup")*)[[source]](../_modules/music21/musicxml/partStaffExporter.html#PartStaffExporterMixin.cleanUpSubsequentPartStaffs)
:   Now that the contents of all PartStaffs in group have been represented
    by a single [`PartExporter`](moduleMusicxmlM21ToXml.html#music21.musicxml.m21ToXml.PartExporter "music21.musicxml.m21ToXml.PartExporter"), remove any
    obsolete PartExporter from self.partExporterList.

    Called by [`joinPartStaffs()`](#music21.musicxml.partStaffExporter.PartStaffExporterMixin.joinPartStaffs "music21.musicxml.partStaffExporter.PartStaffExporterMixin.joinPartStaffs")

    ```python
    >>> from music21.musicxml import testPrimitive
    >>> s = converter.parse(testPrimitive.pianoStaff43a)
    >>> SX = musicxml.m21ToXml.ScoreExporter(s)
    >>> SX.scorePreliminaries()
    >>> SX.parsePartlikeScore()
    >>> len(SX.partExporterList)
    2
    >>> SX.postPartProcess()
    >>> len(SX.partExporterList)
    1
    ```

PartStaffExporterMixin.getRootForPartStaff(*partStaff: [PartStaff](moduleStreamBase.html#music21.stream.base.PartStaff "music21.stream.base.PartStaff")*) → [Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")[[source]](../_modules/music21/musicxml/partStaffExporter.html#PartStaffExporterMixin.getRootForPartStaff)
:   Look up the <part> Element being used to represent the music21 partStaff.

    ```python
    >>> from music21.musicxml import testPrimitive
    >>> s = converter.parse(testPrimitive.pianoStaff43a)
    >>> SX = musicxml.m21ToXml.ScoreExporter(s)
    >>> SX.scorePreliminaries()
    >>> SX.parsePartlikeScore()
    >>> SX.getRootForPartStaff(s.parts[0])
    <Element 'part' at 0x...
    ```

    ```python
    >>> other = stream.PartStaff()
    >>> other.id = 'unrelated'
    >>> SX.getRootForPartStaff(other)
    Traceback (most recent call last):
    music21.musicxml.xmlObjects.MusicXMLExportException:
        <music21.stream.PartStaff unrelated> not found in self.partExporterList
    ```

PartStaffExporterMixin.joinPartStaffs()[[source]](../_modules/music21/musicxml/partStaffExporter.html#PartStaffExporterMixin.joinPartStaffs)
:   Collect <part> elements exported from
    `PartStaff` objects under a single
    <part> element using <staff> and <voice> subelements.

    Here we load in a simple 2-staff piano piece. Note that they
    are both elements of the `PartStaff`
    Stream subclass.

    ```python
    >>> from music21.musicxml import testPrimitive
    >>> s = converter.parse(testPrimitive.pianoStaff43a)
    >>> s.show('text')
    {0.0} <music21.metadata.Metadata object at 0x107d6a100>
    {0.0} <music21.stream.PartStaff P1-Staff1>
        {0.0} <music21.instrument.Instrument 'P1: MusicXML Part: '>
        {0.0} <music21.stream.Measure 1 offset=0.0>
            {0.0} <music21.clef.TrebleClef>
            {0.0} <music21.key.KeySignature of no sharps or flats>
            {0.0} <music21.meter.TimeSignature 4/4>
            {0.0} <music21.note.Note F>
    {0.0} <music21.stream.PartStaff P1-Staff2>
        {0.0} <music21.instrument.Instrument 'P1: MusicXML Part: '>
        {0.0} <music21.stream.Measure 1 offset=0.0>
            {0.0} <music21.clef.BassClef>
            {0.0} <music21.key.KeySignature of no sharps or flats>
            {0.0} <music21.meter.TimeSignature 4/4>
            {0.0} <music21.note.Note B>
    {0.0} <music21.layout.StaffGroup
             <music21.stream.PartStaff P1-Staff1><music21.stream.PartStaff P1-Staff2>>
    ```

    Now these get joined into a single part in the parse() process:

    ```python
    >>> SX = musicxml.m21ToXml.ScoreExporter(s)
    >>> root = SX.parse()
    >>> parts = root.findall('part')
    >>> len(parts)
    1
    ```

    ```python
    >>> clefs = root.findall('.//clef')
    >>> len(clefs)
    2
    ```

    Note that there are exactly two notes (an F and B) in the original score,
    so there are exactly two staff tags in the output.

    ```python
    >>> staffTags = root.findall('part/measure/note/staff')
    >>> len(staffTags)
    2
    ```

PartStaffExporterMixin.joinableGroups() → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[StaffGroup](moduleLayout.html#music21.layout.StaffGroup "music21.layout.StaffGroup")][[source]](../_modules/music21/musicxml/partStaffExporter.html#PartStaffExporterMixin.joinableGroups)
:   Returns a list of [`StaffGroup`](moduleLayout.html#music21.layout.StaffGroup "music21.layout.StaffGroup") objects that
    represent [`PartStaff`](moduleStreamBase.html#music21.stream.base.PartStaff "music21.stream.base.PartStaff") objects that can be
    joined into a single MusicXML <part>, so long as there exists a
    PartExporter for it in ScoreExporter.partExporterList.

    Sets [`previousPartStaffInGroup`](moduleMusicxmlM21ToXml.html#music21.musicxml.m21ToXml.PartExporter.previousPartStaffInGroup "music21.musicxml.m21ToXml.PartExporter.previousPartStaffInGroup").

    ```python
    >>> s = stream.Score()
    ```

    Group 1: three staves.

    ```python
    >>> p1a = stream.PartStaff(id='p1a')
    >>> p1a.insert(0, stream.Measure())
    >>> p1b = stream.PartStaff(id='p1b')
    >>> p1b.insert(0, stream.Measure())
    >>> p1c = stream.PartStaff(id='p1c')
    >>> p1c.insert(0, stream.Measure())
    >>> sg1 = layout.StaffGroup([p1a, p1b, p1c])
    ```

    Group 2: two staves.

    ```python
    >>> p2a = stream.PartStaff(id='p2a')
    >>> p2a.insert(0, stream.Measure())
    >>> p2b = stream.PartStaff(id='p2b')
    >>> p2b.insert(0, stream.Measure())
    >>> sg2 = layout.StaffGroup([p2a, p2b])
    ```

    Group 3: one staff – will not be merged.

    ```python
    >>> p3a = stream.PartStaff(id='p3a')
    >>> p3a.insert(0, stream.Measure())
    >>> sg3 = layout.StaffGroup([p3a])
    ```

    Group 4: two staves, but no measures, will not be merged:

    ```python
    >>> p4a = stream.PartStaff(id='p4a')
    >>> p4b = stream.PartStaff(id='p4b')
    >>> sg4 = layout.StaffGroup([p4a, p4b])
    ```

    Group 5: two staves, but no staff group

    ```python
    >>> p5a = stream.PartStaff(id='p5a')
    >>> p5a.insert(0, stream.Measure())
    >>> p5b = stream.PartStaff(id='p5b')
    >>> p5b.insert(0, stream.Measure())
    ```

    Group 6: same as Group 2, just to show that valid groups can come later

    ```python
    >>> p6a = stream.PartStaff(id='p6a')
    >>> p6a.insert(0, stream.Measure())
    >>> p6b = stream.PartStaff(id='p6b')
    >>> p6b.insert(0, stream.Measure())
    >>> sg6 = layout.StaffGroup([p6a, p6b])
    ```

    Group 7: same as Group 6, but with Parts instead of PartStaffs

    ```python
    >>> p7a = stream.Part(id='p7a')
    >>> p7a.insert(0, stream.Measure())
    >>> p7b = stream.Part(id='p7b')
    >>> p7b.insert(0, stream.Measure())
    >>> sg7 = layout.StaffGroup([p7a, p7b])
    ```

    Group 8: encloses same objects as Group 6, just to show it’s gracefully ignored

    ```python
    >>> sg8 = layout.StaffGroup([p6a, p6b])
    ```

    ```python
    >>> for el in (p1a, p1b, p1c, sg1, p2a, p2b, sg2, p3a, sg3,
    ...            p4a, p4b, sg4, p5a, p5b, p6a, p6b, sg6, p7a, p7b, sg7, sg8):
    ...     s.insert(0, el)
    ```

    ```python
    >>> SX = musicxml.m21ToXml.ScoreExporter(s)
    >>> SX.scorePreliminaries()
    >>> SX.parsePartlikeScore()  # populate .partExporterList
    >>> SX.joinableGroups()
    [<music21.layout.StaffGroup <... p1a><... p1b><... p1c>>,
     <music21.layout.StaffGroup <... p2a><... p2b>>,
     <music21.layout.StaffGroup <... p6a><... p6b>>]
    ```

static PartStaffExporterMixin.moveMeasureContents(*measure: [Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")*, *otherMeasure: [Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")*, *staffNumber: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*)[[source]](../_modules/music21/musicxml/partStaffExporter.html#PartStaffExporterMixin.moveMeasureContents)
:   Move the child elements of measure into otherMeasure;
    create voice numbers if needed;
    bump voice numbers if they conflict;
    account for <backup> and <forward> tags;
    skip <print> tags;
    set “number” on midmeasure clef changes;
    replace existing <barline> tags.

    ```python
    >>> from xml.etree.ElementTree import fromstring as El
    >>> measure = El('<measure><note /></measure>')
    >>> otherMeasure = El('<measure><note /></measure>')
    >>> SX = musicxml.m21ToXml.ScoreExporter
    >>> SX.moveMeasureContents(measure, otherMeasure, 2)
    >>> SX().dump(otherMeasure)
    <measure>
      <note>
        <voice>1</voice>
      </note>
      <note>
        <voice>2</voice>
      </note>
    </measure>
    ```

    ```python
    >>> SX.moveMeasureContents(El('<junk />'), otherMeasure, 2)
    Traceback (most recent call last):
    music21.musicxml.xmlObjects.MusicXMLExportException:
        moveMeasureContents() called on <Element 'junk'...
    ```

    Only one <barline> should be exported per merged measure:

    ```python
    >>> from music21.musicxml import testPrimitive
    >>> s = converter.parse(testPrimitive.mixedVoices1a)
    >>> SX = musicxml.m21ToXml.ScoreExporter(s)
    >>> root = SX.parse()
    >>> root.findall('part/measure/barline')
    [<Element 'barline' at 0x...]
    ```

PartStaffExporterMixin.movePartStaffMeasureContents(*group: [StaffGroup](moduleLayout.html#music21.layout.StaffGroup "music21.layout.StaffGroup")*)[[source]](../_modules/music21/musicxml/partStaffExporter.html#PartStaffExporterMixin.movePartStaffMeasureContents)
:   For every <part> after the first, find the corresponding measure in the initial
    <part> and merge the contents by inserting all contained elements.

    Called by [`joinPartStaffs()`](#music21.musicxml.partStaffExporter.PartStaffExporterMixin.joinPartStaffs "music21.musicxml.partStaffExporter.PartStaffExporterMixin.joinPartStaffs")

    StaffGroup must be a valid one from
    [`joinableGroups()`](#music21.musicxml.partStaffExporter.PartStaffExporterMixin.joinableGroups "music21.musicxml.partStaffExporter.PartStaffExporterMixin.joinableGroups").

PartStaffExporterMixin.processSubsequentPartStaff(*target: [Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")*, *source: [Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")*, *staffNum: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")]][[source]](../_modules/music21/musicxml/partStaffExporter.html#PartStaffExporterMixin.processSubsequentPartStaff)
:   Move elements from subsequent PartStaff’s measures into target: the <part>
    element representing the initial PartStaff that will soon represent the merged whole.

    Called by
    [`movePartStaffMeasureContents()`](#music21.musicxml.partStaffExporter.PartStaffExporterMixin.movePartStaffMeasureContents "music21.musicxml.partStaffExporter.PartStaffExporterMixin.movePartStaffMeasureContents"),
    which is in turn called by
    [`joinPartStaffs()`](#music21.musicxml.partStaffExporter.PartStaffExporterMixin.joinPartStaffs "music21.musicxml.partStaffExporter.PartStaffExporterMixin.joinPartStaffs").

PartStaffExporterMixin.setEarliestAttributesAndClefsPartStaff(*group: [StaffGroup](moduleLayout.html#music21.layout.StaffGroup "music21.layout.StaffGroup")*)[[source]](../_modules/music21/musicxml/partStaffExporter.html#PartStaffExporterMixin.setEarliestAttributesAndClefsPartStaff)
:   Set the <staff>, <key>, <time>, and <clef> information on the earliest
    measure <attributes> tag in the <part> representing the joined PartStaffs.

    Need the earliest <attributes> tag, which may not exist in the merged <part>
    until moved there by movePartStaffMeasureContents() –
    e.g. RH of piano doesn’t appear until m. 40, and earlier music for LH needs
    to be merged first in order to find earliest <attributes>.

    Called by [`joinPartStaffs()`](#music21.musicxml.partStaffExporter.PartStaffExporterMixin.joinPartStaffs "music21.musicxml.partStaffExporter.PartStaffExporterMixin.joinPartStaffs")

    Multiple keys:

    ```python
    >>> from music21.musicxml import testPrimitive
    >>> xmlDir = common.getSourceFilePath() / 'musicxml' / 'lilypondTestSuite'
    >>> s = converter.parse(xmlDir / '43b-MultiStaff-DifferentKeys.xml')
    >>> SX = musicxml.m21ToXml.ScoreExporter(s)
    >>> root = SX.parse()
    >>> m1 = root.find('part/measure')
    >>> SX.dump(m1)
    <measure implicit="no" number="1">
      <attributes>
        <divisions>10080</divisions>
        <key number="1">
          <fifths>0</fifths>
        </key>
        <key number="2">
          <fifths>2</fifths>
        </key>
        <time>
          <beats>4</beats>
          <beat-type>4</beat-type>
        </time>
        <staves>2</staves>
        <clef number="1">
          <sign>G</sign>
          <line>2</line>
        </clef>
        <clef number="2">
          <sign>F</sign>
          <line>4</line>
        </clef>
      </attributes>
    ...
    </measure>
    ```

    Multiple meters (not very well supported by MusicXML readers):

    ```python
    >>> from music21.musicxml import testPrimitive
    >>> s = converter.parse(testPrimitive.pianoStaffPolymeterWithClefOctaveChange)
    >>> SX = musicxml.m21ToXml.ScoreExporter(s)
    >>> root = SX.parse()
    >>> m1 = root.find('part/measure')
    >>> SX.dump(m1)
    <measure implicit="no" number="1">
        <attributes>
        <divisions>10080</divisions>
        <key>
            <fifths>0</fifths>
        </key>
        <time number="1">
            <beats>4</beats>
            <beat-type>4</beat-type>
        </time>
        <time number="2">
            <beats>2</beats>
            <beat-type>2</beat-type>
        </time>
        <staves>2</staves>
        <clef number="1">
            <sign>G</sign>
            <line>2</line>
        </clef>
        <clef number="2">
            <sign>G</sign>
            <line>2</line>
            <clef-octave-change>-1</clef-octave-change>
        </clef>
        </attributes>
    ...
    </measure>
    ```

## Functions

music21.musicxml.partStaffExporter.addStaffTags(*measure: [Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")*, *staffNumber: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *tagList: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*)[[source]](../_modules/music21/musicxml/partStaffExporter.html#addStaffTags)
:   For a <measure> tag measure, add a <staff> grandchild to any instance of
    a child tag of a type in tagList.

    ```python
    >>> from xml.etree.ElementTree import fromstring as El
    >>> from music21.musicxml.partStaffExporter import addStaffTags
    >>> from music21.musicxml.helpers import dump
    >>> elem = El("""
    ...     <measure number="1">
    ...        <note>
    ...          <rest measure="yes" />
    ...          <duration>8</duration>
    ...        </note>
    ...      </measure>"""
    ...     )
    >>> addStaffTags(elem, 2, tagList=['note', 'forward', 'direction', 'harmony'])
    >>> dump(elem)
    <measure number="1">
      <note>
        <rest measure="yes" />
        <duration>8</duration>
        <staff>2</staff>
      </note>
    </measure>
    ```

    Raise if a <staff> grandchild is already present:

    ```python
    >>> addStaffTags(elem, 2, tagList=['note', 'forward', 'direction'])
    Traceback (most recent call last):
    music21.musicxml.xmlObjects.MusicXMLExportException:
        In part (), measure (1): Attempted to create a second <staff> tag
    ```

    The function doesn’t accept elements other than <measure>:

    ```python
    >>> addStaffTags(elem.find('note'), 2, tagList=['direction'])
    Traceback (most recent call last):
    music21.musicxml.xmlObjects.MusicXMLExportException:
        addStaffTags() only accepts <measure> tags
    ```
