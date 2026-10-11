Source: https://music21.org/music21docs/moduleReference/moduleMeiBase.html

# music21.mei.base

These are the public interfaces for the MEI module by Christopher Antila

To convert a string with MEI markup into music21 objects,
use `convertFromString()`.

In the future, most of the functions in this module should be moved to a separate, import-only
module, so that functions for writing music21-to-MEI will fit nicely.

**Simple “How-To”**

Use [`MeiToM21Converter`](#music21.mei.base.MeiToM21Converter "music21.mei.base.MeiToM21Converter") to convert a string to a set of music21 objects. In the future, the
`M21ToMeiConverter` class will convert a set of music21 objects into a string with an MEI
document.

```python
>>> meiString = """<?xml version="1.0" encoding="UTF-8"?>
... <mei xmlns="http://www.music-encoding.org/ns/mei" meiversion="2013">
...     <music>
...     <score>
...         <scoreDef meter.count="6" meter.unit="8">
...             <staffGrp>
...                 <staffDef n="1" clef.shape="F" clef.line="4"/>
...             </staffGrp>
...         </scoreDef>
...         <section>
...             <scoreDef key.sig="1f" key.mode="major"/>
...             <measure n="1">
...                 <staff n="1">
...                     <layer n="1">
...                         <beam>
...                             <note pname="E" oct="3" dur="8" artic="stacc"/>
...                             <note pname="E" oct="3" dur="8"/>
...                             <note pname="E" oct="3" dur="8"/>
...                         </beam>
...                         <chord dur="4" dots="1">
...                             <note pname="F" oct="2"/>
...                             <note pname="A" oct="2" accid="f"/>
...                         </chord>
...                     </layer>
...                 </staff>
...             </measure>
...         </section>
... </score>
...     </music>
... </mei>
... """
>>> conv = mei.MeiToM21Converter(meiString)
>>> result = conv.run()
>>> result
<music21.stream.Score 0x10ee474f0>
```

**Terminology**

This module’s documentation adheres to the following terminology regarding XML documents, using
this snippet, `<note pname="C"/>` as an example:

* the entire snippet is an *element*.
* the word `note` is the *tag*.
* the word `pname` is an *attribute*.
* the letter `C` is a *value*.

Because Python also uses “attributes,” an XML attribute is always preceded by an “at sign,” as in
@pname, whereas a Python attribute is set as `pname`.

**Ignored Elements**

The following elements are not yet imported, though you might expect they would be:

* <sb>: a system break, since this is not usually semantically significant
* <lb>: a line break, since this is not usually semantically significant
* <pb>: a page break, since this is not usually semantically significant

**Where Elements Are Processed**

Most elements are processed in functions called `tagFromElement()`, where “tag” is replaced by
the element’s tag name (e.g., [`staffDefFromElement()`](#music21.mei.base.staffDefFromElement "music21.mei.base.staffDefFromElement") for <staffDef> elements). These functions
convert from a Python [`xml.etree.ElementTree.Element`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")
object to the appropriate music21 object.

However, certain elements are processed primarily in
another way, by “private” functions that are not
documented in this API. Rather than converting an `Element` object into a music21 object,
these functions modify the MEI document tree by adding instructions for the `tagFromElement()`
functions. The elements processed by private functions include:

* <slur>
* <tie>
* <beamSpan>
* <tupletSpan>

Whereas you can expect functions like [`clefFromElement()`](#music21.mei.base.clefFromElement "music21.mei.base.clefFromElement")
to convert a <clef> into a `Clef`
with no loss of information. Because we cannot provide a simple one-to-one conversion for slurs,
ties, and tuplets, we have kept their conversion functions “private,”
to emphasize the fact that you
must use the [`MeiToM21Converter`](#music21.mei.base.MeiToM21Converter "music21.mei.base.MeiToM21Converter") to process them properly.

**Guidelines for Encoders**

While we aim for the best possible compatibility, the MEI
specification is very large. The following
guidelines will help you produce a file that this MEI-to-music21 module will import correctly and
in the most efficient way. These should not necessarily be considered recommendations when using
MEI in any other context.

* Tuplets indicated only in a @tuplet attribute do not work.
* For elements that allow @startid, @endid, and @plist attributes,
  use all three for faster importing.
* For a <tupletSpan> that does not specify a @plist attribute, a tuplet spanning more than two
  measures will always and unavoidably be imported incorrectly.
* For any tuplet, specify at least @num and @numbase. The module refuses to import a tuplet that
  does not have the @numbase attribute.
* Retain consistent @n values for the same layer, staff, and instrument throughout the score.
* Always indicate the duration of <mRest> and <mSpace> elements.
* Avoid using the <barLine> element if you require well-formatted output from music21, since (as of
  January 2015) the music21-to-something converters will only output a `Barline` that is
  part of a `Measure`.

**List of Supported Elements**

Alphabetical list of the elements currently supported by this module:

* [`accidFromElement()`](#music21.mei.base.accidFromElement "music21.mei.base.accidFromElement")
* [`articFromElement()`](#music21.mei.base.articFromElement "music21.mei.base.articFromElement")
* [`barLineFromElement()`](#music21.mei.base.barLineFromElement "music21.mei.base.barLineFromElement")
* [`beamFromElement()`](#music21.mei.base.beamFromElement "music21.mei.base.beamFromElement")
* [`chordFromElement()`](#music21.mei.base.chordFromElement "music21.mei.base.chordFromElement")
* [`clefFromElement()`](#music21.mei.base.clefFromElement "music21.mei.base.clefFromElement")
* [`dotFromElement()`](#music21.mei.base.dotFromElement "music21.mei.base.dotFromElement")
* [`instrDefFromElement()`](#music21.mei.base.instrDefFromElement "music21.mei.base.instrDefFromElement")
* [`layerFromElement()`](#music21.mei.base.layerFromElement "music21.mei.base.layerFromElement")
* [`measureFromElement()`](#music21.mei.base.measureFromElement "music21.mei.base.measureFromElement")
* [`noteFromElement()`](#music21.mei.base.noteFromElement "music21.mei.base.noteFromElement")
* [`restFromElement()`](#music21.mei.base.restFromElement "music21.mei.base.restFromElement")
* [`mRestFromElement()`](#music21.mei.base.mRestFromElement "music21.mei.base.mRestFromElement")
* [`spaceFromElement()`](#music21.mei.base.spaceFromElement "music21.mei.base.spaceFromElement")
* [`mSpaceFromElement()`](#music21.mei.base.mSpaceFromElement "music21.mei.base.mSpaceFromElement")
* [`scoreFromElement()`](#music21.mei.base.scoreFromElement "music21.mei.base.scoreFromElement")
* [`scoreDefFromElement()`](#music21.mei.base.scoreDefFromElement "music21.mei.base.scoreDefFromElement")
* [`sectionFromElement()`](#music21.mei.base.sectionFromElement "music21.mei.base.sectionFromElement")
* [`staffFromElement()`](#music21.mei.base.staffFromElement "music21.mei.base.staffFromElement")
* [`staffDefFromElement()`](#music21.mei.base.staffDefFromElement "music21.mei.base.staffDefFromElement")
* [`staffGrpFromElement()`](#music21.mei.base.staffGrpFromElement "music21.mei.base.staffGrpFromElement")
* [`sylFromElement()`](#music21.mei.base.sylFromElement "music21.mei.base.sylFromElement")
* [`tupletFromElement()`](#music21.mei.base.tupletFromElement "music21.mei.base.tupletFromElement")
* [`verseFromElement()`](#music21.mei.base.verseFromElement "music21.mei.base.verseFromElement")

To know which MEI attributes are known to import correctly, read the documentation for the relevant
element. For example, to know whether the @color attribute on a <note> element is supported, read
the “Attributes/Elements Implemented” section of the [`noteFromElement()`](#music21.mei.base.noteFromElement "music21.mei.base.noteFromElement") documentation.

**List of Ignored Elements**

The following elements are (silently) ignored by the MEI-to-music21 converter because they primarily
affect the layout and typesetting of a musical score. We may choose to implement these elements in
the future, but they are a lower priority because music21 is not primarily a layout or typesetting
tool.

* <multiRest>: a multi-measure rest (these will be “converted” to single-measure rests)
* <pb>: a page break
* <lb>: a line break
* <sb>: a system break

## MeiToM21Converter

class music21.mei.base.MeiToM21Converter(*theDocument=None*)[[source]](../_modules/music21/mei/base.html#MeiToM21Converter)
:   A [`MeiToM21Converter`](#music21.mei.base.MeiToM21Converter "music21.mei.base.MeiToM21Converter") instance manages the conversion of an MEI document into music21
    objects.

    If `theDocument` does not have <mei> as the root element, the class raises an
    `MeiElementError`. If `theDocument` is not a valid XML file, the class raises an
    `MeiValidityError`.

    Parameters:
    :   **theDocument** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – A string containing an MEI document.

    Raises:
    :   `MeiElementError` when the root element is not <mei>

    Raises:
    :   `MeiValidityError` when the MEI file is not valid XML.

[`MeiToM21Converter`](#music21.mei.base.MeiToM21Converter "music21.mei.base.MeiToM21Converter") methods

MeiToM21Converter.run() → [Stream](moduleStreamBase.html#music21.stream.base.Stream "music21.stream.base.Stream")[[source]](../_modules/music21/mei/base.html#MeiToM21Converter.run)
:   Run conversion of the internal MEI document to produce a music21 object.

    Returns a `Stream` subclass, depending on the MEI document.

## Functions

music21.mei.base.accidFromElement(*elem*, *slurBundle=None*)[[source]](../_modules/music21/mei/base.html#accidFromElement)
:   <accid> Records a temporary alteration to the pitch of a note.

    In MEI 2013: pg.248 (262 in PDF) (MEI.shared module)

    Returns:
    :   A string indicating the music21 representation of this accidental.

    **Examples**

    Unlike most of the \_\_\_FromElement() functions, this does not return any music21 object—just
    a string. Accidentals up to triple-sharp and triple-flat are supported.

    ```python
    >>> from xml.etree import ElementTree as ET
    >>> meiSnippet = '<accid accid="s" xmlns="http://www.music-encoding.org/ns/mei"/>'
    >>> meiSnippet = ET.fromstring(meiSnippet)
    >>> mei.base.accidFromElement(meiSnippet)
    '#'
    >>> meiSnippet = '<accid accid="tf" xmlns="http://www.music-encoding.org/ns/mei"/>'
    >>> meiSnippet = ET.fromstring(meiSnippet)
    >>> mei.base.accidFromElement(meiSnippet)
    '---'
    ```

    **Attributes/Elements Implemented:**

    * @accid (from att.accid.log)
    * @accid.ges (from att.accid.ges)

    Note

    If set, the @accid.ges attribute is always imported as the music21 `Accidental`
    for this note. We assume it corresponds to the accidental implied by a key signature.

    **Attributes/Elements in Testing:** none

    **Attributes not Implemented:**

    * att.common (@label, @n, @xml:base) (att.id (@xml:id))
    * att.facsimile (@facs)
    * att.typography (@fontfam, @fontname, @fontsize, @fontstyle, @fontweight)
    * att.accid.log (@func)

      > + (att.controlevent
      >
      >   > - (att.plist (@plist, @evaluate))
      >   > - (att.timestamp.musical (@tstamp))
      >   > - (att.timestamp.performed (@tstamp.ges, @tstamp.real))
      >   > - (att.staffident (@staff)) (att.layerident (@layer)))
    * att.accid.vis (all)
    * att.accid.anl (all)

    **Contained Elements not Implemented:** none

music21.mei.base.articFromElement(*elem*, *slurBundle=None*)[[source]](../_modules/music21/mei/base.html#articFromElement)
:   <artic> An indication of how to play a note or chord.

    In MEI 2013: pg.259 (273 in PDF) (MEI.shared module)

    Returns:
    :   A list of [`Articulation`](moduleArticulations.html#music21.articulations.Articulation "music21.articulations.Articulation") objects.

    **Examples**

    This function is normally called by, for example, [`noteFromElement()`](#music21.mei.base.noteFromElement "music21.mei.base.noteFromElement"), to determine the
    `Articulation` objects that will be assigned to the
    [`articulations`](moduleNote.html#music21.note.GeneralNote.articulations "music21.note.GeneralNote.articulations") attribute.

    ```python
    >>> from xml.etree import ElementTree as ET
    >>> meiSnippet = '<artic artic="acc" xmlns="http://www.music-encoding.org/ns/mei"/>'
    >>> meiSnippet = ET.fromstring(meiSnippet)
    >>> mei.base.articFromElement(meiSnippet)
    [<music21.articulations.Accent>]
    ```

    A single <artic> element may indicate many `Articulation` objects.

    ```python
    >>> meiSnippet = '<artic artic="acc ten" xmlns="http://www.music-encoding.org/ns/mei"/>'
    >>> meiSnippet = ET.fromstring(meiSnippet)
    >>> mei.base.articFromElement(meiSnippet)
    [<music21.articulations.Accent>, <music21.articulations.Tenuto>]
    ```

    **Attributes Implemented:**

    * @artic

    **Attributes/Elements in Testing:** none

    **Attributes not Implemented:**

    * att.common (@label, @n, @xml:base) (att.id (@xml:id))
    * att.facsimile (@facs)
    * att.typography (@fontfam, @fontname, @fontsize, @fontstyle, @fontweight)
    * att.artic.log

      > + (att.controlevent
      >
      >   > - (att.plist (@plist, @evaluate))
      >   > - (att.timestamp.musical (@tstamp))
      >   > - (att.timestamp.performed (@tstamp.ges, @tstamp.real))
      >   > - (att.staffident (@staff))
      >   > - (att.layerident (@layer)))
    * att.artic.vis (all)
    * att.artic.gesatt.artic.anl (all)

    **Contained Elements not Implemented:** none

music21.mei.base.beamFromElement(*elem*, *slurBundle=None*)[[source]](../_modules/music21/mei/base.html#beamFromElement)
:   <beam> A container for a series of explicitly beamed events that begins and ends entirely
    :   within a measure.

    In MEI 2013: pg.264 (278 in PDF) (MEI.cmn module)

    Parameters:
    :   **elem** ([`Element`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")) – The `<beam>` element to process.

    Returns:
    :   An iterable of all the objects contained within the `<beam>` container.

    Return type:
    :   list of [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")

    **Example**

    Here, three `Note` objects are beamed together. Take note that the function returns
    a list of three objects, none of which is a `Beam` or similar.

    ```python
    >>> from xml.etree import ElementTree as ET
    >>> meiSnippet = """<beam xmlns="http://www.music-encoding.org/ns/mei">
    ...     <note pname='A' oct='7' dur='8'/>
    ...     <note pname='B' oct='7' dur='8'/>
    ...     <note pname='C' oct='6' dur='8'/>
    ... </beam>"""
    >>> meiSnippet = ET.fromstring(meiSnippet)
    >>> result = mei.base.beamFromElement(meiSnippet)
    >>> isinstance(result, list)
    True
    >>> len(result)
    3
    >>> result[0].pitch.nameWithOctave
    'A7'
    >>> result[0].beams
    <music21.beam.Beams <music21.beam.Beam 1/start>>
    >>> result[1].pitch.nameWithOctave
    'B7'
    >>> result[1].beams
    <music21.beam.Beams <music21.beam.Beam 1/continue>>
    >>> result[2].pitch.nameWithOctave
    'C6'
    >>> result[2].beams
    <music21.beam.Beams <music21.beam.Beam 1/stop>>
    ```

    **Attributes/Elements Implemented:**

    * <clef>, <chord>, <note>, <rest>, <space>, <tuplet>, <beam>, <barLine>

    **Attributes/Elements Ignored:**

    * @xml:id

    **Attributes/Elements in Testing:** none

    **Attributes not Implemented:**

    * att.common (@label, @n, @xml:base)
    * att.facsimile (@facs)
    * att.beam.log

      > + (att.event
      >
      >   > - (att.timestamp.musical (@tstamp))
      >   > - (att.timestamp.performed (@tstamp.ges, @tstamp.real))
      >   > - (att.staffident (@staff))
      >   > - (att.layerident (@layer)))
      > + (att.beamedwith (@beam.with))
    * att.beam.vis (all)
    * att.beam.gesatt.beam.anl (all)

    **Contained Elements not Implemented:**

    * MEI.cmn: bTrem beatRpt fTrem halfmRpt meterSig meterSigGrp
    * MEI.critapp: app
    * MEI.edittrans: (all)
    * MEI.mensural: ligature mensur proport
    * MEI.shared: clefGrp custos keySig pad

music21.mei.base.chordFromElement(*elem*, *slurBundle=None*)[[source]](../_modules/music21/mei/base.html#chordFromElement)
:   <chord> is a simultaneous sounding of two or
    more notes in the same layer with the same duration.

    In MEI 2013: pg.280 (294 in PDF) (MEI.shared module)

    **Attributes/Elements Implemented:**

    * @xml:id (or id), an XML id (submitted as the Music21Object “id”)
    * <note> contained within
    * @dur, from att.duration.musical: (via \_qlDurationFromAttr())
    * @dots, from att.augmentdots: [0..4]
    * @artic and <artic>
    * @tie, (many of “[i|m|t]”)
    * @slur, (many of “[i|m|t][1-6]”)
    * @grace, from att.note.ges.cmn: partial implementation (notes marked as grace, but the
      :   duration is 0 because we ignore the question of which neighbouring note to borrow time from)

    **Attributes/Elements in Testing:** none

    **Attributes not Implemented:**

    * att.common (@label, @n, @xml:base)
    * att.facsimile (@facs)
    * att.chord.log

      > + (att.event
      >
      >   > - (att.timestamp.musical (@tstamp))
      >   > - (att.timestamp.performed (@tstamp.ges, @tstamp.real))
      >   > - (att.staffident (@staff))
      >   > - (att.layerident (@layer)))
      > + (att.fermatapresent (@fermata))
      > + (att.syltext (@syl))
      > + (att.chord.log.cmn
      >
      >   > - (att.tupletpresent (@tuplet))
      >   > - (att.beamed (@beam))
      >   > - (att.lvpresent (@lv))
      >   > - (att.ornam (@ornam)))
    * att.chord.vis (all)
    * att.chord.ges

      > + (att.articulation.performed (@artic.ges))
      > + (att.duration.performed (@dur.ges))
      > + (att.instrumentident (@instr))
      > + (att.chord.ges.cmn (att.graced (@grace, @grace.time))) <– partially implemented
    * att.chord.anl (all)

    **Contained Elements not Implemented:**

    * MEI.edittrans: (all)

music21.mei.base.clefFromElement(*elem*, *slurBundle=None*)[[source]](../_modules/music21/mei/base.html#clefFromElement)
:   <clef> Indication of the exact location of a particular note on the staff and, therefore,
    the other notes as well.

    In MEI 2013: pg.284 (298 in PDF) (MEI.shared module)

    **Attributes/Elements Implemented:**

    * @xml:id (or id), an XML id (submitted as the Music21Object “id”)
    * @shape, from att.clef.gesatt.clef.log
    * @line, from att.clef.gesatt.clef.log
    * @dis, from att.clef.gesatt.clef.log
    * @dis.place, from att.clef.gesatt.clef.log

    **Attributes/Elements Ignored:**

    * @cautionary, since this has no obvious implication for a music21 Clef
    * @octave, since this is likely obscure

    **Attributes/Elements in Testing:** none

    **Attributes not Implemented:**

    * att.common (@label, @n, @xml:base)
    * att.event

      > + (att.timestamp.musical (@tstamp))
      > + (att.timestamp.performed (@tstamp.ges, @tstamp.real))
      > + (att.staffident (@staff))
      > + (att.layerident (@layer))
    * att.facsimile (@facs)
    * att.clef.anl (all)
    * att.clef.vis (all)

    **Contained Elements not Implemented:** none

music21.mei.base.dotFromElement(*elem*, *slurBundle=None*)[[source]](../_modules/music21/mei/base.html#dotFromElement)
:   Returns `1` no matter what is passed in.

    <dot> Dot of augmentation or division.

    In MEI 2013: pg.304 (318 in PDF) (MEI.shared module)

    Returns:
    :   1

    Return type:
    :   [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

    **Attributes/Elements Implemented:** none

    **Attributes/Elements in Testing:** none

    **Attributes not Implemented:**

    * att.common (@label, @n, @xml:base) (att.id (@xml:id))
    * att.facsimile (@facs)
    * att.dot.log (all)
    * att.dot.vis (all)
    * att.dot.gesatt.dot.anl (all)

    **Elements not Implemented:** none

music21.mei.base.instrDefFromElement(*elem*, *slurBundle=None*)[[source]](../_modules/music21/mei/base.html#instrDefFromElement)
:   <instrDef> (instrument definition)—MIDI instrument declaration.

    In MEI 2013: pg.344 (358 in PDF) (MEI.midi module)

    Returns:
    :   An `Instrument`

    **Attributes/Elements Implemented:**

    * @midi.instrname (att.midiinstrument)
    * @midi.instrnum (att.midiinstrument)

    **Attributes/Elements in Testing:** none

    **Attributes/Elements Ignored:**

    * @xml:id

    **Attributes not Implemented:**

    * att.common (@label, @n, @xml:base)
    * att.channelized (@midi.channel, @midi.duty, @midi.port, @midi.track)
    * att.midiinstrument (@midi.pan, @midi.volume)

    **Contained Elements not Implemented:** none

music21.mei.base.layerFromElement(*elem*, *overrideN=None*, *slurBundle=None*)[[source]](../_modules/music21/mei/base.html#layerFromElement)
:   <layer> An independent stream of events on a staff.

    In MEI 2013: pg.353 (367 in PDF) (MEI.shared module)

    Note

    The `Voice` object’s `id` attribute must be set
    properly in order to ensure continuity of voices between measures. If the `elem` does not
    have an @n attribute, you can set one with the `overrideN` parameter in this function. If
    you provide a value for `overrideN`, it will be used instead of the `elemn` object’s
    @n attribute.

    Because improperly-set `id` attributes nearly guarantees errors
    in the imported `Score`, either `overrideN` or @n must be specified.

    Parameters:
    :   * **elem** ([`Element`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")) – The `<layer>` element to process.
        * **overrideN** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – The value to be set as the `id`
          attribute in the outputted `Voice`.

    Returns:
    :   A `Voice` with the objects found in the provided `Element`.

    Return type:
    :   `music21.stream.Voice`

    Raises:
    :   `MeiAttributeError` if neither `overrideN` nor @n are specified.

    **Attributes/Elements Implemented:**

    * <clef>, <chord>, <note>, <rest>, <mRest>, <beam>, <tuplet>, <space>, <mSpace> , and
      <barLine> contained within
    * @n, from att.common

    **Attributes Ignored:**

    * @xml:id

    **Attributes/Elements in Testing:** none

    **Attributes not Implemented:**

    * att.common (@label, @xml:base)
    * att.declaring (@decls)
    * att.facsimile (@facs)
    * att.layer.log (@def) and (att.meterconformance (@metcon))
    * att.layer.vis (att.visibility (@visible))
    * att.layer.gesatt.layer.anl (all)

    **Contained Elements not Implemented:**

    * MEI.cmn: arpeg bTrem beamSpan beatRpt bend breath fTrem fermata gliss hairpin halfmRpt
      :   harpPedal mRpt mRpt2 meterSig meterSigGrp multiRest multiRpt octave pedal
          reh slur tie tuplet tupletSpan
    * MEI.cmnOrnaments: mordent trill turn
    * MEI.critapp: app
    * MEI.edittrans: (all)
    * MEI.harmony: harm
    * MEI.lyrics: lyrics
    * MEI.mensural: ligature mensur proport
    * MEI.midi: midi
    * MEI.neumes: ineume syllable uneume
    * MEI.shared: accid annot artic barLine clefGrp custos dir dot dynam keySig pad pb phrase sb
      :   scoreDef staffDef tempo
    * MEI.text: div
    * MEI.usersymbols: anchoredText curve line symbol

music21.mei.base.measureFromElement(*elem*, *backupNum*, *expectedNs*, *slurBundle=None*, *activeMeter=None*)[[source]](../_modules/music21/mei/base.html#measureFromElement)
:   <measure> Unit of musical time consisting of a fixed number of note-values of a given type, as
    determined by the prevailing meter, and delimited in musical notation by two bar lines.

    In MEI 2013: pg.365 (379 in PDF) (MEI.cmn module)

    Parameters:
    :   * **elem** ([`Element`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")) – The `<measure>` element to process.
        * **backupNum** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) – A fallback value for the resulting
          `Measure` objects’ number attribute.
        * **expectedNs** (*iterable* *of* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – A list of the expected @n attributes for the <staff> tags in this <measure>.
          If an expected <staff> isn’t in the <measure>, it will be created with a full-measure rest.
        * **activeMeter** – The `TimeSignature` active in this <measure>. This is
          used to adjust the duration of an <mRest> that was given without a @dur attribute.

    Returns:
    :   A dictionary where keys are the @n attributes for <staff> tags found in this
        <measure>, and values are `Measure` objects that should be appended
        to the `Part` instance with the value’s @n attributes.

    Return type:
    :   dict of `Measure`

    Note

    When the right barline is set to `'rptboth'` in MEI, it requires adjusting the left
    barline of the following <measure>. If this happens, the `Repeat` object is assigned
    to the `'next @left'` key in the returned dictionary.

    **Attributes/Elements Implemented:**

    * contained elements: <staff> and <staffDef>
    * @right and @left (att.measure.log)
    * @n (att.common)

    **Attributes Ignored:**

    * @xml:id (att.id)
    * <slur> and <tie> contained within. These spanners will usually be attached to their starting
      and ending notes with @xml:id attributes, so it’s not necessary to process them when
      encountered in a <measure>. Furthermore, because the possibility exists for cross-measure
      slurs and ties, we can’t guarantee we’ll be able to process all spanners until all
      spanner-attachable objects are processed. So we manage these tags at a higher level.

    **Attributes/Elements in Testing:** none

    **Attributes not Implemented:**

    * att.common (@label, @xml:base)
    * att.declaring (@decls)
    * att.facsimile (@facs)
    * att.typed (@type, @subtype)
    * att.pointing (@xlink:actuate, @xlink:role, @xlink:show, @target, @targettype, @xlink:title)
    * att.measure.log (att.meterconformance.bar (@metcon, @control))
    * att.measure.vis (all)
    * att.measure.ges (att.timestamp.performed (@tstamp.ges, @tstamp.real))
    * att.measure.anl (all)

    **Contained Elements not Implemented:**

    * MEI.cmn: arpeg beamSpan bend breath fermata gliss hairpin harpPedal octave ossia pedal reh
      :   tupletSpan
    * MEI.cmnOrnaments: mordent trill turn
    * MEI.critapp: app
    * MEI.edittrans: add choice corr damage del gap handShift orig reg restore sic subst supplied
      :   unclear
    * MEI.harmony: harm
    * MEI.lyrics: lyrics
    * MEI.midi: midi
    * MEI.shared: annot dir dynam pb phrase sb tempo
    * MEI.text: div
    * MEI.usersymbols: anchoredText curve line symbol

music21.mei.base.noteFromElement(*elem*, *slurBundle=None*)[[source]](../_modules/music21/mei/base.html#noteFromElement)
:   <note> is a single pitched event.

    In MEI 2013: pg.382 (396 in PDF) (MEI.shared module)

    Note

    If set, the @accid.ges attribute is always imported as the music21 `Accidental`
    for this note. We assume it corresponds to the accidental implied by a key signature.

    Note

    If `elem` contains both <syl> and <verse> elements as immediate children, the lyrics
    indicated with <verse> element(s) will always obliterate those given indicated with <syl>
    elements.

    **Attributes/Elements Implemented:**

    * @accid and <accid>
    * @accid.ges for key signatures
    * @pname, from att.pitch: [a–g]
    * @oct, from att.octave: [0..9]
    * @dur, from att.duration.musical: (via \_qlDurationFromAttr())
    * @dots: [0..4], and <dot> contained within
    * @xml:id (or id), an XML id (submitted as the Music21Object “id”)
    * @artic and <artic>
    * @tie, (many of “[i|m|t]”)
    * @slur, (many of “[i|m|t][1-6]”)
    * @grace, from att.note.ges.cmn: partial implementation (notes marked as grace, but the
      :   duration is 0 because we ignore the question of which neighbouring note to borrow time from)
    * <syl> and <verse>

    **Attributes/Elements in Testing:** none

    **Attributes not Implemented:**

    * att.common (@label, @n, @xml:base)
    * att.facsimile (@facs)
    * att.note.log

      > + (att.event
      >
      >   > - (att.timestamp.musical (@tstamp))
      >   > - (att.timestamp.performed (@tstamp.ges, @tstamp.real))
      >   > - (att.staffident (@staff))
      >   > - (att.layerident (@layer)))
      > + (att.fermatapresent (@fermata))
      > + (att.syltext (@syl))
      > + (att.note.log.cmn
      >
      >   > - (att.tupletpresent (@tuplet))
      >   > - (att.beamed (@beam))
      >   > - (att.lvpresent (@lv))
      >   > - (att.ornam (@ornam)))
      > + (att.note.log.mensural (@lig))
    * att.note.vis (all)
    * att.note.ges

      > + (@oct.ges, @pname.ges, @pnum)
      > + att.articulation.performed (@artic.ges))
      > + (att.duration.performed (@dur.ges))
      > + (att.instrumentident (@instr))
      > + (att.note.ges.cmn (@gliss)
      >
      >   > - (att.graced (@grace, @grace.time))) <– partially implemented
      > + (att.note.ges.mensural (att.duration.ratio (@num, @numbase)))
      > + (att.note.ges.tablature (@tab.fret, @tab.string))
    * att.note.anl (all)

    **Contained Elements not Implemented:**

    * MEI.critapp: app
    * MEI.edittrans: (all)

music21.mei.base.spaceFromElement(*elem*, *slurBundle=None*)[[source]](../_modules/music21/mei/base.html#spaceFromElement)
:   <space> A placeholder used to fill an incomplete measure, layer, etc. most often so that the
    combined duration of the events equals the number of beats in the measure.

    Returns a Rest element with hideObjectOnPrint = True

    In MEI 2013: pg.440 (455 in PDF) (MEI.shared module)

music21.mei.base.mSpaceFromElement(*elem*, *slurBundle=None*)[[source]](../_modules/music21/mei/base.html#mSpaceFromElement)
:   <mSpace/> A measure containing only empty space in any meter.

    In MEI 2013: pg.377 (391 in PDF) (MEI.cmn module)

    This is a function wrapper for [`spaceFromElement()`](#music21.mei.base.spaceFromElement "music21.mei.base.spaceFromElement").

    Note

    If the <mSpace> element does not have a @dur attribute, it will have the default
    duration of 1.0. This must be fixed later, so the `Space` object returned from this
    method is given the `m21wasMRest` attribute, set to True.

music21.mei.base.restFromElement(*elem*, *slurBundle=None*)[[source]](../_modules/music21/mei/base.html#restFromElement)
:   <rest/> is a non-sounding event found in the source being transcribed

    In MEI 2013: pg.424 (438 in PDF) (MEI.shared module)

    **Attributes/Elements Implemented:**

    * xml:id (or id), an XML id (submitted as the Music21Object “id”)
    * dur, from att.duration.musical: (via \_qlDurationFromAttr())
    * dots, from att.augmentdots: [0..4]

    **Attributes/Elements in Testing:** none

    **Attributes not Implemented:**

    * att.common (@label, @n, @xml:base)
    * att.facsimile (@facs)
    * att.rest.log

      > + (att.event
      >
      >   > - (att.timestamp.musical (@tstamp))
      >   > - (att.timestamp.performed (@tstamp.ges, @tstamp.real))
      >   > - (att.staffident (@staff))
      >   > - (att.layerident (@layer)))
      > + (att.fermatapresent (@fermata))
      >
      >   > - (att.tupletpresent (@tuplet))
      >   > - (att.rest.log.cmn (att.beamed (@beam)))
    * att.rest.vis (all)
    * att.rest.ges (all)
    * att.rest.anl (all)

    **Contained Elements not Implemented:** none

music21.mei.base.mRestFromElement(*elem*, *slurBundle=None*)[[source]](../_modules/music21/mei/base.html#mRestFromElement)
:   <mRest/> Complete measure rest in any meter.

    In MEI 2013: pg.375 (389 in PDF) (MEI.cmn module)

    This is a function wrapper for [`restFromElement()`](#music21.mei.base.restFromElement "music21.mei.base.restFromElement").

    Note

    If the <mRest> element does not have a @dur attribute, it will have the default
    duration of 1.0. This must be fixed later, so the `Rest` object returned from this
    method is given the `m21wasMRest` attribute, set to True.

music21.mei.base.scoreFromElement(*elem*, *slurBundle*)[[source]](../_modules/music21/mei/base.html#scoreFromElement)
:   <score> Full score view of the musical content.

    In MEI 2013: pg.430 (444 in PDF) (MEI.shared module)

    Parameters:
    :   * **elem** ([`Element`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")) – The <score> element to process.
        * **slurBundle** ([`music21.spanner.SpannerBundle`](moduleSpanner.html#music21.spanner.SpannerBundle "music21.spanner.SpannerBundle")) – This `SpannerBundle` holds the [`Slur`](moduleSpanner.html#music21.spanner.Slur "music21.spanner.Slur") objects
          created during pre-processing. The slurs are attached to their respective `Note` and
          `Chord` objects as they are processed.

    Returns:
    :   A completed `Score` object.

    **Attributes/Elements Implemented:**

    **Attributes Ignored:**

    **Attributes/Elements in Testing:**

    * contained <section>, <scoreDef>, and <staffDef>

    **Attributes not Implemented:**

    * att.common (@label, @n, @xml:base) (att.id (@xml:id))
    * att.declaring (@decls)
    * att.typed (@type, @subtype)
    * att.score.anl (att.common.anl (@copyof, @corresp, @next, @prev, @sameas, @synch)
      :   (att.alignment (@when)))

    **Contained Elements not Implemented:**

    * MEI.critapp: app
    * MEI.edittrans: add choice corr damage del gap handShift orig
      :   reg restore sic subst supplied unclear
    * MEI.shared: annot ending pb sb
    * MEI.text: div
    * MEI.usersymbols: anchoredText curve line symbol

music21.mei.base.sectionFromElement(*elem*, *allPartNs*, *activeMeter*, *nextMeasureLeft*, *backupMeasureNum*, *slurBundle*)[[source]](../_modules/music21/mei/base.html#sectionFromElement)
:   <section> Segment of music data.

    In MEI 2013: pg.432 (446 in PDF) (MEI.shared module)

    Note

    The parameters and return values are exactly the same for [`sectionFromElement()`](#music21.mei.base.sectionFromElement "music21.mei.base.sectionFromElement")
    and [`sectionScoreCore()`](#music21.mei.base.sectionScoreCore "music21.mei.base.sectionScoreCore"), so refer to the latter function’s documentation for more
    information.

    **Attributes/Elements Implemented:**

    **Attributes Ignored:**

    **Attributes/Elements in Testing:**

    * @label
    * contained <measure>, <scoreDef>, <staffDef>, <section>

    **Attributes not Implemented:**

    * att.common (@n, @xml:base) (att.id (@xml:id))
    * att.declaring (@decls)
    * att.facsimile (@facs)
    * att.typed (@type, @subtype)
    * att.pointing (@xlink:actuate, @xlink:role, @xlink:show, @target, @targettype, @xlink:title)
    * att.section.vis (@restart)
    * att.section.anl (att.common.anl (@copyof, @corresp, @next, @prev, @sameas, @synch)
      :   (att.alignment (@when)))

    **Contained Elements not Implemented:**

    * MEI.critapp: app
    * MEI.edittrans: add choice corr damage del gap handShift orig reg
      :   restore sic subst supplied unclear
    * MEI.shared: annot ending expansion pb sb section staff
    * MEI.text: div
    * MEI.usersymbols: anchoredText curve line symbol

music21.mei.base.scoreDefFromElement(*elem*, *slurBundle=None*)[[source]](../_modules/music21/mei/base.html#scoreDefFromElement)
:   <scoreDef> Container for score meta-information.

    In MEI 2013: pg.431 (445 in PDF) (MEI.shared module)

    This function returns a dictionary with objects that may relate to the entire score, to all
    parts at a particular moment, or only to a specific part at a particular moment. The dictionary
    keys determine the object’s scope. If the key is:

    * `'whole-score objects'`, it applies to the entire score (e.g., page size);
    * `'all-part objects'`, it applies to all parts at the moment this <scoreDef> appears;
    * the @n attribute of a part, it applies only to
      that part at the moment this <scoreDef> appears.

    While the multi-part objects will be held in a list, the single-part objects will be in a dict
    like that returned by [`staffDefFromElement()`](#music21.mei.base.staffDefFromElement "music21.mei.base.staffDefFromElement").

    Note that it is the caller’s responsibility to determine the right action if there are
    conflicting objects in the returned dictionary.

    For example:

    ```python
    >>> meiDoc = """<?xml version="1.0" encoding="UTF-8"?>
    ... <scoreDef meter.count="3" meter.unit="4" xmlns="http://www.music-encoding.org/ns/mei">
    ...     <staffGrp>
    ...         <staffDef n="1" label="Clarinet"/>
    ...         <staffGrp>
    ...             <staffDef n="2" label="Flute"/>
    ...             <staffDef n="3" label="Violin"/>
    ...         </staffGrp>
    ...     </staffGrp>
    ... </scoreDef>
    ... """
    >>> from xml.etree import ElementTree as ET
    >>> scoreDef = ET.fromstring(meiDoc)
    >>> result = mei.base.scoreDefFromElement(scoreDef)
    >>> len(result)
    5
    >>> result['1']
    {'instrument': <music21.instrument.Clarinet '1: Clarinet'>}
    >>> result['3']
    {'instrument': <music21.instrument.Violin '3: Violin'>}
    >>> result['all-part objects']
    [<music21.meter.TimeSignature 3/4>]
    >>> result['whole-score objects']
    []
    ```

    Parameters:
    :   **elem** ([`Element`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")) – The `<scoreDef>` element to process.

    Returns:
    :   Objects from the `<scoreDef>`, as described above.

    Return type:
    :   [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")

    **Attributes/Elements Implemented:**

    * (att.meterSigDefault.log (@meter.count, @meter.unit))
    * (att.keySigDefault.log (@key.accid, @key.mode, @key.pname, @key.sig))
    * contained <staffGrp>

    **Attributes/Elements in Testing:** None

    **Attributes not Implemented:**

    * att.common (@label, @n, @xml:base) (att.id (@xml:id))
    * att.scoreDef.log

      > + (att.cleffing.log (@clef.shape, @clef.line, @clef.dis, @clef.dis.place))
      > + (att.duration.default (@dur.default, @num.default, @numbase.default))
      > + (att.keySigDefault.log (@key.sig.mixed))
      > + (att.octavedefault (@octave.default))
      > + (att.transposition (@trans.diat, @trans.semi))
      > + (att.scoreDef.log.cmn (att.beaming.log (@beam.group, @beam.rests)))
      > + (att.scoreDef.log.mensural
      >
      >   > - (att.mensural.log (@mensur.dot, @mensur.sign,
      >   >   :   @mensur.slash, @proport.num, @proport.numbase)
      >   > - (att.mensural.shared (@modusmaior, @modusminor, @prolatio, @tempus))))
    * att.scoreDef.vis (all)
    * att.scoreDef.ges (all)
    * att.scoreDef.anl (none exist)

    **Contained Elements not Implemented:**

    * MEI.cmn: meterSig meterSigGrp
    * MEI.harmony: chordTable
    * MEI.linkalign: timeline
    * MEI.midi: instrGrp
    * MEI.shared: keySig pgFoot pgFoot2 pgHead pgHead2
    * MEI.usersymbols: symbolTable

music21.mei.base.staffFromElement(*elem*, *slurBundle=None*)[[source]](../_modules/music21/mei/base.html#staffFromElement)
:   <staff> A group of equidistant horizontal lines on which notes are placed in order to
    represent pitch or a grouping element for individual ‘strands’ of notes, rests, etc. that may
    or may not actually be rendered on staff lines; that is, both diastematic and non-diastematic
    signs.

    In MEI 2013: pg.444 (458 in PDF) (MEI.shared module)

    Parameters:
    :   **elem** ([`Element`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")) – The `<staff>` element to process.

    Returns:
    :   The `Voice` classes corresponding to the `<layer>` tags in `elem`.

    Return type:
    :   list of `music21.stream.Voice`

    **Attributes/Elements Implemented:**

    * <layer> contained within

    **Attributes Ignored:**

    * @xml:id

    **Attributes/Elements in Testing:** none

    **Attributes not Implemented:**

    * att.common (@label, @n, @xml:base)
    * att.declaring (@decls)
    * att.facsimile (@facs)
    * att.staff.log (@def) (att.meterconformance (@metcon))
    * att.staff.vis (att.visibility (@visible))
    * att.staff.gesatt.staff.anl (all)

    **Contained Elements not Implemented:**

    * MEI.cmn: ossia
    * MEI.critapp: app
    * MEI.edittrans: (all)
    * MEI.shared: annot pb sb scoreDef staffDef
    * MEI.text: div
    * MEI.usersymbols: anchoredText curve line symbol

music21.mei.base.staffDefFromElement(*elem*, *slurBundle=None*)[[source]](../_modules/music21/mei/base.html#staffDefFromElement)
:   <staffDef> Container for staff meta-information.

    In MEI 2013: pg.445 (459 in PDF) (MEI.shared module)

    Returns:
    :   A dict with various types of metadata information, depending on what is specified in
        this <staffDef> element. Read below for more information.

    Return type:
    :   [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")

    **Possible Return Values**

    The contents of the returned dictionary depend on the contents of the <staffDef> element. The
    dictionary keys correspond to types of information. Possible keys include:

    * `'instrument'`: for a [`music21.instrument.Instrument`](moduleInstrument.html#music21.instrument.Instrument "music21.instrument.Instrument") subclass
    * `'clef'`: for a [`music21.clef.Clef`](moduleClef.html#music21.clef.Clef "music21.clef.Clef") subclass
    * `'key'`: for a [`music21.key.Key`](moduleKey.html#music21.key.Key "music21.key.Key") or [`KeySignature`](moduleKey.html#music21.key.KeySignature "music21.key.KeySignature") subclass
    * `'meter'`: for a `music21.meter.TimeSignature`

    **Examples**

    This <staffDef> only returns a single item.

    ```python
    >>> meiDoc = """<?xml version="1.0" encoding="UTF-8"?>
    ... <staffDef n="1" label="Clarinet" xmlns="http://www.music-encoding.org/ns/mei"/>
    ... """
    >>> from xml.etree import ElementTree as ET
    >>> staffDef = ET.fromstring(meiDoc)
    >>> result = mei.base.staffDefFromElement(staffDef)
    >>> len(result)
    1
    >>> result
    {'instrument': <music21.instrument.Clarinet '1: Clarinet'>}
    >>> result['instrument'].partId
    '1'
    >>> result['instrument'].partName
    'Clarinet'
    ```

    This <staffDef> returns many objects.

    ```python
    >>> meiDoc = """<?xml version="1.0" encoding="UTF-8"?>
    ... <staffDef n="2" label="Tuba" key.pname="B" key.accid="f" key.mode="major"
    ...  xmlns="http://www.music-encoding.org/ns/mei">
    ...     <clef shape="F" line="4"/>
    ... </staffDef>
    ... """
    >>> from xml.etree import ElementTree as ET
    >>> staffDef = ET.fromstring(meiDoc)
    >>> result = mei.base.staffDefFromElement(staffDef)
    >>> len(result)
    3
    >>> result['instrument']
    <music21.instrument.Tuba '2: Tuba'>
    >>> result['clef']
    <music21.clef.BassClef>
    >>> result['key']
    <music21.key.Key of B- major>
    ```

    **Attributes/Elements Implemented:**

    * @label (att.common) as Instrument.partName
    * @label.abbr (att.labels.addl) as Instrument.partAbbreviation
    * @n (att.common) as Instrument.partId
    * (att.keySigDefault.log (@key.accid, @key.mode, @key.pname, @key.sig))
    * (att.meterSigDefault.log (@meter.count, @meter.unit))
    * (att.cleffing.log (@clef.shape, @clef.line, @clef.dis, @clef.dis.place))
      (via [`clefFromElement()`](#music21.mei.base.clefFromElement "music21.mei.base.clefFromElement"))
    * @trans.diat and @trans.demi (att.transposition)
    * <instrDef> held within
    * <clef> held within

    **Attributes/Elements Ignored:**

    * @key.sig.mixed (from att.keySigDefault.log)

    **Attributes/Elements in Testing:** none

    **Attributes not Implemented:**

    * att.common (@n, @xml:base) (att.id (@xml:id))
    * att.declaring (@decls)
    * att.staffDef.log

      > + (att.duration.default (@dur.default, @num.default, @numbase.default))
      > + (att.octavedefault (@octave.default))
      > + (att.staffDef.log.cmn (att.beaming.log (@beam.group, @beam.rests)))
      > + (att.staffDef.log.mensural
      >
      >   > - (att.mensural.log (@mensur.dot, @mensur.sign, @mensur.slash,
      >   >   :   @proport.num, @proport.numbase)
      >   > - (att.mensural.shared (@modusmaior, @modusminor, @prolatio, @tempus))))
    * att.staffDef.vis (all)
    * att.staffDef.ges (all)
    * att.staffDef.anl (none exist)

    **Contained Elements not Implemented:**

    * MEI.cmn: meterSig meterSigGrp
    * MEI.mensural: mensural support
    * MEI.shared: clefGrp keySig label layerDef

music21.mei.base.staffGrpFromElement(*elem*, *slurBundle=None*, *staffDefDict=None*)[[source]](../_modules/music21/mei/base.html#staffGrpFromElement)
:   <staffGrp> A group of bracketed or braced staves.

    In MEI 2013: pg.448 (462 in PDF) (MEI.shared module)

    For now, this function is merely a container-processor for <staffDef> elements contained
    in this <staffGrp> element given as the “elem” argument. That is, the function does not yet
    create the brackets/braces and labels expected of a staff group.
    Note however that all <staffDef>
    elements will be processed, even if they’re contained within several layers of <staffGrp>.

    Parameters:
    :   **elem** ([`Element`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")) – The `<staffGrp>` element to process.

    Returns:
    :   Dictionary where keys are the @n attribute on a contained <staffDef>, and values are
        the result of calling [`staffDefFromElement()`](#music21.mei.base.staffDefFromElement "music21.mei.base.staffDefFromElement") with that <staffDef>.

    **Attributes/Elements Implemented:**

    * contained <staffDef>
    * contained <staffGrp>

    **Attributes/Elements in Testing:** none

    **Attributes not Implemented:**

    * att.common (@label, @n, @xml:base) (att.id (@xml:id))
    * att.declaring (@decls)
    * att.facsimile (@facs)
    * att.staffGrp.vis (@barthru)

      > + (att.labels.addl (@label.abbr))
      > + (att.staffgroupingsym (@symbol))
      > + (att.visibility (@visible))
    * att.staffGrp.ges (att.instrumentident (@instr))

    **Contained Elements not Implemented:**

    * MEI.midi: instrDef
    * MEI.shared: grpSym label

music21.mei.base.tupletFromElement(*elem*, *slurBundle=None*)[[source]](../_modules/music21/mei/base.html#tupletFromElement)
:   <tuplet> A group of notes with “irregular” (sometimes called “irrational”) rhythmic values,
    for example, three notes in the time normally occupied by two or nine in the time of five.

    In MEI 2013: pg.473 (487 in PDF) (MEI.cmn module)

    Parameters:
    :   **elem** ([`Element`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")) – The `<tuplet>` element to process.

    Returns:
    :   An iterable of all the objects contained within the `<tuplet>` container.

    Return type:
    :   tuple of [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")

    **Attributes/Elements Implemented:**

    * <tuplet>, <beam>, <note>, <rest>, <chord>, <clef>, <space>, <barLine>
    * @num and @numbase

    **Attributes/Elements in Testing:** none

    **Attributes not Implemented:**

    * att.common (@label, @n, @xml:base) (att.id (@xml:id))
    * att.facsimile (@facs)
    * att.tuplet.log

      > + (att.event
      >
      >   > - (att.timestamp.musical (@tstamp))
      >   > - (att.timestamp.performed (@tstamp.ges, @tstamp.real))
      >   > - (att.staffident (@staff))
      >   > - (att.layerident (@layer)))
      > + (att.beamedwith (@beam.with))
      > + (att.augmentdots (@dots))
      > + (att.duration.additive (@dur))
      > + (att.startendid (@endid) (att.startid (@startid)))
    * att.tuplet.vis (all)
    * att.tuplet.ges (att.duration.performed (@dur.ges))
    * att.tuplet.anl (all)

    **Contained Elements not Implemented:**

    * MEI.cmn: bTrem beatRpt fTrem halfmRpt meterSig meterSigGrp
    * MEI.critapp: app
    * MEI.edittrans: (all)
    * MEI.mensural: ligature mensur proport
    * MEI.shared: clefGrp custos keySig pad

music21.mei.base.addSlurs(*elem*, *obj*, *slurBundle*)[[source]](../_modules/music21/mei/base.html#addSlurs)
:   If relevant, add a slur to an `obj` (object) that was created from an `elem` (element).

    Parameters:
    :   * **elem** ([`xml.etree.ElementTree.Element`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")) – The `Element` that caused creation of the `obj`.
        * **obj** ([`music21.base.Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")) – The musical object (`Note`, `Chord`, etc.) created from `elem`, to
          which a slur might be attached.
        * **slurBundle** ([`music21.spanner.SpannerBundle`](moduleSpanner.html#music21.spanner.SpannerBundle "music21.spanner.SpannerBundle")) – The `Slur`-holding `SpannerBundle` associated with the
          `Stream` that holds `obj`.

    Returns:
    :   Whether at least one slur was added.

    Return type:
    :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    **A Note about Importing Slurs**

    Because of how the MEI format specifies slurs, the strategy required for proper import to
    music21 is not obvious. There are two ways to specify a slur:

    1. With a `@slur` attribute, in which case [`addSlurs()`](#music21.mei.base.addSlurs "music21.mei.base.addSlurs") reads the attribute and manages
       creating a `Slur` object, adding the affected objects to it, and storing the
       `Slur` in the `slurBundle`.
    2. With a `<slur>` element, which requires pre-processing. In this case, `Slur` objects
       must already exist in the `slurBundle`, and special attributes must be added to the
       affected elements (`@m21SlurStart` to the element at the start of the slur and
       `@m21SlurEnd` to the element at the end). These attributes hold the `id` of a
       `Slur` in the `slurBundle`, allowing [`addSlurs()`](#music21.mei.base.addSlurs "music21.mei.base.addSlurs") to find the slur and add
       `obj` to it.

    Caution

    If an `elem` has an @m21SlurStart or @m21SlurEnd attribute that refer to an
    object not found in the `slurBundle`, the slur is silently dropped.

music21.mei.base.allPartsPresent(*scoreElem*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), ...][[source]](../_modules/music21/mei/base.html#allPartsPresent)
:   Find the @n values for all <staffDef> elements in a <score> element. This assumes that every
    MEI <staff> corresponds to a music21 `Part`.

    scoreElem is the <score> Element in which to find the part names.
    Returns all the unique @n values associated with a part in the <score>.

    **Example**

    ```python
    >>> meiDoc = """<?xml version="1.0" encoding="UTF-8"?>
    ... <score xmlns="http://www.music-encoding.org/ns/mei">
    ...     <scoreDef>
    ...         <staffGrp>
    ...             <staffDef n="1" clef.shape="G" clef.line="2"/>
    ...             <staffDef n="2" clef.shape="F" clef.line="4"/>
    ...         </staffGrp>
    ...     </scoreDef>
    ...     <section>
    ...         <!-- ... some music ... -->
    ...         <staffDef n="2" clef.shape="C" clef.line="4"/>
    ...         <!-- ... some music ... -->
    ...     </section>
    ... </score>"""
    >>> import xml.etree.ElementTree as ETree
    >>> meiDoc = ETree.fromstring(meiDoc)
    >>> mei.base.allPartsPresent(meiDoc)
    ('1', '2')
    ```

    Even though there are three <staffDef> elements in the document, there are only two unique @n
    attributes. The second appearance of <staffDef> with @n=”2” signals a change of clef on that
    same staff—not that there is a new staff.

music21.mei.base.barLineFromElement(*elem*, *slurBundle=None*)[[source]](../_modules/music21/mei/base.html#barLineFromElement)
:   <barLine> Vertical line drawn through one or more staves that divides musical notation into
    metrical units.

    In MEI 2013: pg.262 (276 in PDF) (MEI.shared module)

    Returns:
    :   A [`music21.bar.Barline`](moduleBar.html#music21.bar.Barline "music21.bar.Barline") or [`Repeat`](moduleBar.html#music21.bar.Repeat "music21.bar.Repeat"), depending on the
        value of @rend. If @rend is `'rptboth'`, a 2-tuplet of `Repeat` objects will be
        returned, represented an “end” and “start” barline, as specified in the [`music21.bar`](moduleBar.html#module-music21.bar "music21.bar")
        documentation.

    Note

    The music21-to-other converters expect that a `Barline` will be attached to a
    `Measure`, which it will not be when imported from MEI as a <barLine> element.
    However, this function does import correctly to a `Barline` that you can access from
    Python in the `Stream` object as expected.

    **Attributes/Elements Implemented:**

    * @rend from att.barLine.log

    **Attributes/Elements in Testing:** none

    **Attributes not Implemented:**

    * att.common (@label, @n, @xml:base) (att.id (@xml:id))
    * att.facsimile (@facs)
    * att.pointing (@xlink:actuate, @xlink:role, @xlink:show, @target, @targettype, @xlink:title)
    * att.barLine.log

      > + (att.meterconformance.bar (@metcon, @control))
    * att.barLine.vis

      > + (att.barplacement (@barplace, @taktplace))
      > + (att.color (@color))
      > + (att.measurement (@unit))
      > + (att.width (@width))
    * att.barLine.ges (att.timestamp.musical (@tstamp))
    * att.barLine.anl

      > + (att.common.anl
      >
      >   > - (@copyof, @corresp, @next, @prev, @sameas, @synch)
      >   > - (att.alignment (@when)))

    **Contained Elements not Implemented:** none

music21.mei.base.beamTogether(*someThings*)[[source]](../_modules/music21/mei/base.html#beamTogether)
:   Beam some things together. The function beams every object that has a
    [`beams`](moduleNote.html#music21.note.NotRest.beams "music21.note.NotRest.beams") attribute,
    leaving the other objects unmodified.

    Parameters:
    :   **someThings** (iterable of [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")) – An iterable of things to beam together.

    Returns:
    :   `someThings` with relevant objects beamed together.

    Return type:
    :   same as `someThings`

music21.mei.base.getVoiceId(*fromThese*)[[source]](../_modules/music21/mei/base.html#getVoiceId)
:   From a list of objects with mixed type, find the “id” of the `music21.stream.Voice`
    instance.

    Parameters:
    :   **fromThese** ([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")) – A list of objects of any type, at least one of which must be a
        `Voice` instance.

    Returns:
    :   The `id` of the `Voice` instance.

    Raises:
    :   [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "(in Python v3.14)") if zero or many `Voice` objects are found.

music21.mei.base.makeDuration(*base: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | Fraction = 0.0*, *dots: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*) → [duration.Duration](moduleDuration.html#music21.duration.Duration "music21.duration.Duration")[[source]](../_modules/music21/mei/base.html#makeDuration)
:   Given a `base` duration and a number of `dots`, create a [`Duration`](moduleDuration.html#music21.duration.Duration "music21.duration.Duration")
    instance with the
    appropriate `quarterLength` value.

    Returns a `Duration` corresponding to the fully-augmented value.

    **Examples**

    ```python
    >>> from fractions import Fraction
    >>> mei.base.makeDuration(base=2.0, dots=0).quarterLength  # half note, no dots
    2.0
    >>> mei.base.makeDuration(base=2.0, dots=1).quarterLength  # half note, one dot
    3.0
    >>> mei.base.makeDuration(base=2, dots=2).quarterLength  # 'base' can be an int or float
    3.5
    >>> mei.base.makeDuration(2.0, 10).quarterLength  # you want ridiculous dots? Sure!
    3.998046875
    >>> mei.base.makeDuration(0.33333333333333333333, 0).quarterLength  # works with fractions too
    Fraction(1, 3)
    >>> mei.base.makeDuration(Fraction(1, 3), 1).quarterLength
    0.5
    ```

music21.mei.base.makeMetadata(*documentRoot*)[[source]](../_modules/music21/mei/base.html#makeMetadata)
:   Produce metadata objects for all the metadata stored in the MEI header.

    Parameters:
    :   **documentRoot** ([`Element`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")) – The MEI document’s root element.

    Returns:
    :   A `Metadata` object with some of the metadata stored in the MEI document.

    Return type:
    :   [`music21.metadata.Metadata`](moduleMetadata.html#music21.metadata.Metadata "music21.metadata.Metadata")

music21.mei.base.metaSetComposer(*work*, *meta*)[[source]](../_modules/music21/mei/base.html#metaSetComposer)
:   From a <work> element, find the composer(s) and store the values in a `Metadata` object.

    Parameters:
    :   * **work** – A <work> [`Element`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)") with metadata you want to find.
        * **meta** – The [`Metadata`](moduleMetadata.html#music21.metadata.Metadata "music21.metadata.Metadata") object in which to store the metadata.

    Returns:
    :   The `meta` argument, having relevant metadata added.

music21.mei.base.metaSetDate(*work*, *meta*)[[source]](../_modules/music21/mei/base.html#metaSetDate)
:   From a <work> element, find the date (range) of composition and store the values in a
    `Metadata` object.

    Parameters:
    :   * **work** – A <work> [`Element`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)") with metadata you want to find.
        * **meta** – The [`Metadata`](moduleMetadata.html#music21.metadata.Metadata "music21.metadata.Metadata") object in which to store the metadata.

    Returns:
    :   The `meta` argument, having relevant metadata added.

music21.mei.base.metaSetTitle(*work*, *meta*)[[source]](../_modules/music21/mei/base.html#metaSetTitle)
:   From a <work> element, find the title, subtitle, and movement name (<tempo> element) and store
    the values in a `Metadata` object.

    Parameters:
    :   * **work** – A <work> [`Element`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)") with metadata you want to find.
        * **meta** – The [`Metadata`](moduleMetadata.html#music21.metadata.Metadata "music21.metadata.Metadata") object in which to store the metadata.

    Returns:
    :   The `meta` argument, having relevant metadata added.

music21.mei.base.removeOctothorpe(*xmlid*)[[source]](../_modules/music21/mei/base.html#removeOctothorpe)
:   Given a string with an @xml:id to search for, remove a leading octothorpe, if present.

    ```python
    >>> from music21.mei.base import removeOctothorpe
    >>> removeOctothorpe('110a923d-a13a-4a2e-b85c-e1d438e4c5d6')
    '110a923d-a13a-4a2e-b85c-e1d438e4c5d6'
    >>> removeOctothorpe('#e46cbe82-95fc-4522-9f7a-700e41a40c8e')
    'e46cbe82-95fc-4522-9f7a-700e41a40c8e'
    ```

music21.mei.base.safePitch(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *accidental: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *octave: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = ''*) → [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")[[source]](../_modules/music21/mei/base.html#safePitch)
:   Safely build a [`Pitch`](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") from a string.

    When `__init__()` is given an empty string,
    it raises a `PitchException`. This
    function instead returns a default [`Pitch`](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") instance.

    name: Desired name of the [`Pitch`](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch").

    accidental: (Optional) Symbol for the accidental.

    octave: (Optional) Octave number.

    Returns A [`Pitch`](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") with the appropriate properties.

music21.mei.base.scaleToTuplet(*objs*, *elem*)[[source]](../_modules/music21/mei/base.html#scaleToTuplet)
:   Scale the duration of some objects by a ratio indicated by a tuplet. The `elem` must have the
    @m21TupletNum and @m21TupletNumbase attributes set, and optionally the @m21TupletSearch or
    @m21TupletType attributes.

    The @m21TupletNum and @m21TupletNumbase attributes should be equal to the @num and @numbase
    values of the <tuplet> or <tupletSpan> that indicates this tuplet.

    The @m21TupletSearch attribute, whose value must either be `'start'` or `'end'`, is required
    when a <tupletSpan> does not include a @plist attribute. It indicates that the importer must
    “search” for a tuplet near the end of the import process, which involves scaling the durations
    of all objects discovered between those with the “start” and “end” search values.

    The @m21TupletType attribute is set directly as the `type`
    attribute of the music21 object’s `Tuplet` object.
    If @m21TupletType is not set, the @tuplet attribute will be
    consulted. Note that this attribute is ignored if the @m21TupletSearch attribute is present,
    since the `type` will be set later by the tuplet-finding algorithm.

    Note

    Objects without a [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") attribute will be
    skipped silently, unless they
    will be given the @m21TupletSearch attribute.

    Parameters:
    :   * **objs** ((list of) [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")) – The object(s) whose durations will be scaled.
          You may provide either a single object
          or an iterable; the return type corresponds to the input type.
        * **elem** ([`xml.etree.ElementTree.Element`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")) – An `Element` with the appropriate attributes (as specified above).

    Returns:
    :   `objs` with scaled durations.

    Return type:
    :   (list of) [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")

music21.mei.base.sectionScoreCore(*elem*, *allPartNs*, *slurBundle*, *\**, *activeMeter=None*, *nextMeasureLeft=None*, *backupMeasureNum=0*)[[source]](../_modules/music21/mei/base.html#sectionScoreCore)
:   This function is the “core” of both [`sectionFromElement()`](#music21.mei.base.sectionFromElement "music21.mei.base.sectionFromElement") and [`scoreFromElement()`](#music21.mei.base.scoreFromElement "music21.mei.base.scoreFromElement"),
    since both elements are treated quite similarly (though not identically). It’s a separate and
    shared function to reduce code duplication and
    increase ease of testing. It’s a “public” function
    to help spread the burden of API documentation complexity: while the parameters and return
    values are described in this function, the compliance with the MEI Guidelines is described in
    both [`sectionFromElement()`](#music21.mei.base.sectionFromElement "music21.mei.base.sectionFromElement") and [`scoreFromElement()`](#music21.mei.base.scoreFromElement "music21.mei.base.scoreFromElement"), as expected.

    **Required Parameters**

    Parameters:
    :   * **elem** ([`xml.etree.ElementTree.Element`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")) – The <section> or <score> element to process.
        * **allPartNs** (*iterable* *of* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – A list or tuple of the expected @n attributes for the <staff> tags in this
          <section>. This tells the function how many parts there are and what @n values they use.
        * **slurBundle** ([`music21.spanner.SpannerBundle`](moduleSpanner.html#music21.spanner.SpannerBundle "music21.spanner.SpannerBundle")) – This `SpannerBundle` holds the [`Slur`](moduleSpanner.html#music21.spanner.Slur "music21.spanner.Slur") objects
          created during pre-processing. The slurs are attached to their respective `Note` and
          `Chord` objects as they are processed.

    **Optional Keyword Parameters**

    The following parameters are all optional, and must be specified as a keyword argument (i.e.,
    you specify the parameter name before its value).

    Parameters:
    :   * **activeMeter** (`music21.meter.TimeSignature`) – The `TimeSignature` active at the start of this
          <section> or <score>. This is updated automatically as the music is processed, and the
          `TimeSignature` active at the end of the element is returned.
        * **nextMeasureLeft** ([`music21.bar.Barline`](moduleBar.html#music21.bar.Barline "music21.bar.Barline") or [`music21.bar.Repeat`](moduleBar.html#music21.bar.Repeat "music21.bar.Repeat")) – The @left attribute to use for the next <measure> element encountered.
          This is used for situations where one <measure> element specified a @right attribute that
          must be imported by music21 as *both* the right barline of one measure and the left barline
          of the following; at the moment this is only @rptboth, which requires a `Repeat` in
          both cases.
        * **backupMeasureNum** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) – In case a <measure> element is missing its @n attribute,
          [`measureFromElement()`](#music21.mei.base.measureFromElement "music21.mei.base.measureFromElement") will use this automatically-incremented number instead. The
          `backupMeasureNum` corresponding to the final <measure> in this <score> or <section> is
          returned from this function.

    Returns:
    :   Four-tuple with a dictionary of results, the new value of `activeMeter`, the new
        value of `nextMeasureLeft`, and the new value of `backupMeasureNum`.

    Return type:
    :   (dict, `TimeSignature`, [`Barline`](moduleBar.html#music21.bar.Barline "music21.bar.Barline"), int)

    **Return Value**

    In short, it’s `parsed`, `activeMeter`, `nextMeasureLeft`, `backupMeasureNum`.

    * `'parsed'` is a dictionary where the keys are the values in `allPartNs` and the values are
      :   a list of all the `Measure` objects in that part, as found in this <section> or
          <score>.
    * `'activeMeter'` is the `TimeSignature` in effect at the end of this
      :   <section> or <score>.
    * `'nextMeasureLeft'` is the value that should be
      :   assigned to the `leftBarline` attribute
          of the first `Measure` found in the next <section>. This will almost always be None.
    * `'backupMeasureNum'` is equal to the `backupMeasureNum` argument plus the number of
      :   <measure> elements found in this <score> or <section>.

music21.mei.base.sylFromElement(*elem*, *slurBundle=None*)[[source]](../_modules/music21/mei/base.html#sylFromElement)
:   <syl> Individual lyric syllable.

    In MEI 2013: pg.454 (468 in PDF) (MEI.shared module)

    Returns:
    :   An appropriately-configured [`music21.note.Lyric`](moduleNote.html#music21.note.Lyric "music21.note.Lyric").

    **Attributes/Elements Implemented:**

    * @con and @wordpos (from att.syl.log)

    **Attributes/Elements in Testing:** none

    **Attributes not Implemented:**

    * att.common (@label, @n, @xml:base) (att.id (@xml:id))
    * att.facsimile (@facs)
    * att.syl.vis (att.typography (@fontfam, @fontname, @fontsize, @fontstyle, @fontweight))

      > + (att.visualoffset (att.visualoffset.ho (@ho))
      >
      >   > - (att.visualoffset.to (@to))
      >   > - (att.visualoffset.vo (@vo)))
      > + (att.xy (@x, @y))
      > + (att.horizontalalign (@halign))
    * att.syl.anl (att.common.anl (@copyof, @corresp, @next, @prev, @sameas, @synch)

      > + (att.alignment (@when)))

    **Contained Elements not Implemented:**

    * MEI.edittrans: (all)
    * MEI.figtable: fig
    * MEI.namesdates: corpName geogName periodName persName styleName
    * MEI.ptrref: ptr ref
    * MEI.shared: address bibl date identifier lb name num rend repository stack title

music21.mei.base.verseFromElement(*elem*, *backupN=None*, *slurBundle=None*)[[source]](../_modules/music21/mei/base.html#verseFromElement)
:   <verse> Lyric verse.

    In MEI 2013: pg.480 (494 in PDF) (MEI.lyrics module)

    Parameters:
    :   **backupN** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) – The backup verse number to use if no @n attribute exists on `elem`.

    Returns:
    :   The appropriately-configured `Lyric` objects.

    Return type:
    :   list of [`music21.note.Lyric`](moduleNote.html#music21.note.Lyric "music21.note.Lyric")

    **Attributes/Elements Implemented:**

    * @n and <syl>

    **Attributes/Elements in Testing:** none

    **Attributes not Implemented:**

    * att.common (@label, @n, @xml:base) (att.id (@xml:id))
    * att.facsimile (@facs)
    * att.lang (@xml:lang)
    * att.verse.log (@refrain, @rhythm)
    * att.verse.vis (att.typography (@fontfam, @fontname, @fontsize, @fontstyle, @fontweight))

      > + (att.visualoffset.to (@to))
      > + ((att.visualoffset.vo (@vo))
      >
      >   > - (att.xy (@x, @y))
    * att.verse.anl (att.common.anl (@copyof, @corresp, @next, @prev, @sameas, @synch)

      > + (att.alignment (@when)))

    **Contained Elements not Implemented:**

    * MEI.shared: dir dynam lb space tempo
