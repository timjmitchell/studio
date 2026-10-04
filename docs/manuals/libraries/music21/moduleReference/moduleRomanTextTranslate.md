Source: https://music21.org/music21docs/moduleReference/moduleRomanTextTranslate.html

# music21.romanText.translate

Translation routines for roman numeral analysis text files, as defined
and demonstrated by Dmitri Tymoczko. Also used for the ClercqTemperley
format which is similar but a little different.

This module is really only needed for people extending the parser,
for others it’s simple to get Harmony, RomanNumeral, Key (or KeySignature)
and other objects out of an rntxt file by running this:

```python
>>> monteverdi = corpus.parse('monteverdi/madrigal.3.1.rntxt')
>>> monteverdi.show('text')
{0.0} <music21.metadata.Metadata object at 0x...>
{0.0} <music21.stream.Part ...>
    {0.0} <music21.stream.Measure 1 offset=0.0>
        {0.0} <music21.key.KeySignature of 1 flat>
        {0.0} <music21.meter.TimeSignature 4/4>
        {0.0} <music21.roman.RomanNumeral vi in F major>
        {3.0} <music21.roman.RomanNumeral V[no3] in F major>
    {4.0} <music21.stream.Measure 2 offset=4.0>
        {0.0} <music21.roman.RomanNumeral I in F major>
        {3.0} <music21.roman.RomanNumeral IV in F major>
    ...
```

Then the stream can be analyzed with something like this, storing
the data to make a histogram of scale degree usage within a key:

```python
>>> degreeDictionary = {}
>>> for el in monteverdi.recurse():
...    if isinstance(el, roman.RomanNumeral):
...         print(f'{el.figure} {el.key}')
...         for p in el.pitches:
...              degree, accidental = el.key.getScaleDegreeAndAccidentalFromPitch(p)
...              if accidental is None:
...                   degreeString = str(degree)
...              else:
...                   degreeString = str(degree) + str(accidental.modifier)
...              if degreeString not in degreeDictionary:
...                   degreeDictionary[degreeString] = 1
...              else:
...                   degreeDictionary[degreeString] += 1
...              degTuple = (str(p), degreeString)
...              print(degTuple)
    vi F major
    ('D5', '6')
    ('F5', '1')
    ('A5', '3')
    V[no3] F major
    ('C5', '5')
    ('G5', '2')
    I F major
    ('F4', '1')
    ('A4', '3')
    ('C5', '5')
    ...
    V6 g minor
    ('F#5', '7#')
    ('A5', '2')
    ('D6', '5')
    i g minor
    ('G4', '1')
    ('B-4', '3')
    ('D5', '5')
    ...
```

Now if we’d like we can get a Histogram of the data.
It’s a little complex, but worth seeing in full:

```python
>>> import operator
>>> histogram = graph.primitives.GraphHistogram()
>>> i = 0
>>> data = []
>>> xLabels = []
>>> values = []
>>> ddList = list(degreeDictionary.items())
>>> for deg,value in sorted(ddList, key=operator.itemgetter(1), reverse=True):
...    data.append((i, degreeDictionary[deg]), )
...    xLabels.append((i+.5, deg), )
...    values.append(degreeDictionary[deg])
...    i += 1
>>> histogram.data = data
```

These commands give nice labels for the data; optional:

```python
>>> histogram.setIntegerTicksFromData(values, 'y')
>>> histogram.setTicks('x', xLabels)
>>> histogram.setAxisLabel('x', 'ScaleDegree')
```

Now generate the histogram:

[![../_images/romanTranslatePitchDistribution.png](../_images/romanTranslatePitchDistribution.png)](../_images/romanTranslatePitchDistribution.png)

## PartTranslator

class music21.romanText.translate.PartTranslator(*md=None*)[[source]](../_modules/music21/romanText/translate.html#PartTranslator)
:   A refactoring of the previously massive romanTextToStreamScore function
    to allow for more fine-grained testing (eventually), and to
    get past the absurdly high number of nested blocks (the previous translator
    was written under severe time constraints).

[`PartTranslator`](#music21.romanText.translate.PartTranslator "music21.romanText.translate.PartTranslator") methods

PartTranslator.fillMeasureFromPreviousRn(*mFill: [Measure](moduleStreamBase.html#music21.stream.base.Measure "music21.stream.base.Measure")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/romanText/translate.html#PartTranslator.fillMeasureFromPreviousRn)

PartTranslator.fillToMeasureToken(*measureToken: [RTMeasure](moduleRomanTextRtObjects.html#music21.romanText.rtObjects.RTMeasure "music21.romanText.rtObjects.RTMeasure")*)[[source]](../_modules/music21/romanText/translate.html#PartTranslator.fillToMeasureToken)
:   Create a series of measures which extend the previous RN until the measure number
    implied by measureToken.

PartTranslator.parseKeySignatureTag(*rtTagged: [RTTagged](moduleRomanTextRtObjects.html#music21.romanText.rtObjects.RTTagged "music21.romanText.rtObjects.RTTagged")*)[[source]](../_modules/music21/romanText/translate.html#PartTranslator.parseKeySignatureTag)
:   Parse a key signature tag which has already been determined to
    be a key signature.

    ```python
    >>> tag = romanText.rtObjects.RTTagged('KeySignature: -4')
    >>> tag.isKeySignature()
    True
    >>> tag.data
    '-4'
    ```

    ```python
    >>> pt = romanText.translate.PartTranslator()
    >>> pt.keySigCurrent is None
    True
    >>> pt.setKeySigFromFirstKeyToken
    True
    >>> pt.foundAKeySignatureSoFar
    False
    ```

    ```python
    >>> pt.parseKeySignatureTag(tag)
    >>> pt.keySigCurrent
    <music21.key.KeySignature of 4 flats>
    >>> pt.setKeySigFromFirstKeyToken
    False
    >>> pt.foundAKeySignatureSoFar
    True
    ```

    ```python
    >>> tag = romanText.rtObjects.RTTagged('KeySignature: xyz')
    >>> pt.parseKeySignatureTag(tag)
    Traceback (most recent call last):
    music21.romanText.translate.RomanTextTranslateException:
        Cannot parse key signature: 'xyz'
    ```

PartTranslator.processRTChord(*a: [RTChord](moduleRomanTextRtObjects.html#music21.romanText.rtObjects.RTChord "music21.romanText.rtObjects.RTChord")*, *m: [Measure](moduleStreamBase.html#music21.stream.base.Measure "music21.stream.base.Measure")*, *currentOffset: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [Fraction](https://docs.python.org/3/library/fractions.html#fractions.Fraction "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/romanText/translate.html#PartTranslator.processRTChord)
:   Process a single RTChord atom.

PartTranslator.setAnalyticKey(*a*)[[source]](../_modules/music21/romanText/translate.html#PartTranslator.setAnalyticKey)
:   Indicates a change in the analyzed key, not a change in anything
    else, such as the keySignature.

PartTranslator.setMinorRootParse(*rtTagged: [RTTagged](moduleRomanTextRtObjects.html#music21.romanText.rtObjects.RTTagged "music21.romanText.rtObjects.RTTagged")*)[[source]](../_modules/music21/romanText/translate.html#PartTranslator.setMinorRootParse)
:   Set Roman Numeral parsing standards from a token.

    ```python
    >>> pt = romanText.translate.PartTranslator()
    >>> pt.sixthMinor
    <Minor67Default.CAUTIONARY: 2>
    ```

    ```python
    >>> tag = romanText.rtObjects.RTTagged('SixthMinor: Flat')
    >>> tag.isSixthMinor()
    True
    >>> pt.setMinorRootParse(tag)
    >>> pt.sixthMinor
    <Minor67Default.FLAT: 4>
    ```

    Harmonic sets to FLAT for sixth and SHARP for seventh

    ```python
    >>> for config in 'flat sharp quality cautionary harmonic'.split():
    ...     tag = romanText.rtObjects.RTTagged('Seventh Minor: ' + config)
    ...     pt.setMinorRootParse(tag)
    ...     print(pt.seventhMinor)
    Minor67Default.FLAT
    Minor67Default.SHARP
    Minor67Default.QUALITY
    Minor67Default.CAUTIONARY
    Minor67Default.SHARP
    ```

    ```python
    >>> tag = romanText.rtObjects.RTTagged('Sixth Minor: harmonic')
    >>> pt.setMinorRootParse(tag)
    >>> print(pt.sixthMinor)
    Minor67Default.FLAT
    ```

    Unknown settings raise a RomanTextTranslateException

    ```python
    >>> tag = romanText.rtObjects.RTTagged('Seventh Minor: asdf')
    >>> pt.setMinorRootParse(tag)
    Traceback (most recent call last):
    music21.romanText.translate.RomanTextTranslateException:
        Cannot parse setting vi or vii parsing: 'asdf'
    ```

PartTranslator.translateMeasureLineToken(*measureLineToken: [RTMeasure](moduleRomanTextRtObjects.html#music21.romanText.rtObjects.RTMeasure "music21.romanText.rtObjects.RTMeasure")*)[[source]](../_modules/music21/romanText/translate.html#PartTranslator.translateMeasureLineToken)
:   Translate a measure token consisting of a single line such as:

    ```python
    m21 b3 V b4 C: IV
    ```

    Or it might be a variant measure, or a copy instruction.

PartTranslator.translateOneLineToken(*lineToken: [RTTagged](moduleRomanTextRtObjects.html#music21.romanText.rtObjects.RTTagged "music21.romanText.rtObjects.RTTagged")*)[[source]](../_modules/music21/romanText/translate.html#PartTranslator.translateOneLineToken)
:   Translates one line token and set the current settings.

    A token in this case consists of an entire line’s worth.
    It might be a token such as ‘Title: Neko Funjatta’ or
    a composite token such as ‘m23 b4 IV6’

PartTranslator.translateSingleMeasure(*measureToken*)[[source]](../_modules/music21/romanText/translate.html#PartTranslator.translateSingleMeasure)
:   Given a measureToken, return a stream.Measure object with
    the appropriate atoms set.

PartTranslator.translateSingleMeasureAtom(*a: [RTAtom](moduleRomanTextRtObjects.html#music21.romanText.rtObjects.RTAtom "music21.romanText.rtObjects.RTAtom")*, *m: [Measure](moduleStreamBase.html#music21.stream.base.Measure "music21.stream.base.Measure")*, *\**, *isLastAtomInMeasure: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/romanText/translate.html#PartTranslator.translateSingleMeasureAtom)
:   Translate a single atom in a measure token.

    a is the Atom
    m is a stream.Measure object.

    Uses coreInsert and coreAppend methods, so must have m.coreElementsChanged()
    called afterward.

PartTranslator.translateTokens(*tokens*)[[source]](../_modules/music21/romanText/translate.html#PartTranslator.translateTokens)

## RomanTextUnprocessedMetadata

class music21.romanText.translate.RomanTextUnprocessedMetadata(*tag=''*, *data=''*, *\*\*keywords*)[[source]](../_modules/music21/romanText/translate.html#RomanTextUnprocessedMetadata)

[`RomanTextUnprocessedMetadata`](#music21.romanText.translate.RomanTextUnprocessedMetadata "music21.romanText.translate.RomanTextUnprocessedMetadata") bases

* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`RomanTextUnprocessedMetadata`](#music21.romanText.translate.RomanTextUnprocessedMetadata "music21.romanText.translate.RomanTextUnprocessedMetadata") read-only properties

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`RomanTextUnprocessedMetadata`](#music21.romanText.translate.RomanTextUnprocessedMetadata "music21.romanText.translate.RomanTextUnprocessedMetadata") read/write properties

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`RomanTextUnprocessedMetadata`](#music21.romanText.translate.RomanTextUnprocessedMetadata "music21.romanText.translate.RomanTextUnprocessedMetadata") methods

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`RomanTextUnprocessedMetadata`](#music21.romanText.translate.RomanTextUnprocessedMetadata "music21.romanText.translate.RomanTextUnprocessedMetadata") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## RomanTextUnprocessedToken

class music21.romanText.translate.RomanTextUnprocessedToken(*obj: [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)") = None*, *\*\*keywords*)[[source]](../_modules/music21/romanText/translate.html#RomanTextUnprocessedToken)

[`RomanTextUnprocessedToken`](#music21.romanText.translate.RomanTextUnprocessedToken "music21.romanText.translate.RomanTextUnprocessedToken") bases

* [`ElementWrapper`](moduleBase.html#music21.base.ElementWrapper "music21.base.ElementWrapper")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`RomanTextUnprocessedToken`](#music21.romanText.translate.RomanTextUnprocessedToken "music21.romanText.translate.RomanTextUnprocessedToken") read-only properties

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`RomanTextUnprocessedToken`](#music21.romanText.translate.RomanTextUnprocessedToken "music21.romanText.translate.RomanTextUnprocessedToken") read/write properties

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`RomanTextUnprocessedToken`](#music21.romanText.translate.RomanTextUnprocessedToken "music21.romanText.translate.RomanTextUnprocessedToken") methods

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`RomanTextUnprocessedToken`](#music21.romanText.translate.RomanTextUnprocessedToken "music21.romanText.translate.RomanTextUnprocessedToken") instance variables

Instance variables inherited from [`ElementWrapper`](moduleBase.html#music21.base.ElementWrapper "music21.base.ElementWrapper"):

|  |  |  |
| --- | --- | --- |
| * [`obj`](moduleBase.html#music21.base.ElementWrapper.obj "music21.base.ElementWrapper.obj") |  |  |

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## Functions

music21.romanText.translate.appendMeasureToRepeatEndingsDict(*rtMeasureObj: [RTMeasure](moduleRomanTextRtObjects.html#music21.romanText.rtObjects.RTMeasure "music21.romanText.rtObjects.RTMeasure")*, *m: [Measure](moduleStreamBase.html#music21.stream.base.Measure "music21.stream.base.Measure")*, *repeatEndings: [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")*, *measureNumber=None*)[[source]](../_modules/music21/romanText/translate.html#appendMeasureToRepeatEndingsDict)
:   Takes an RTMeasure object (which might represent one or more
    measures; but currently only one) and a music21 stream.Measure object and
    store it as a tuple in the repeatEndings dictionary to mark where the
    translator should later mark for adding endings.

    If the optional measureNumber is specified, we use that rather than the
    token number to add to the dict.

    This does not yet work for skipped measures.

    ```python
    >>> rtm = romanText.rtObjects.RTMeasure('m15a V6 b1.5 V6/5 b2 I b3 viio6')
    >>> rtm.repeatLetter
    ['a']
    >>> rtm2 = romanText.rtObjects.RTMeasure('m15b V6 b1.5 V6/5 b2 I')
    >>> rtm2.repeatLetter
    ['b']
    >>> repeatEndings = {}
    >>> m1 = stream.Measure()
    >>> m2 = stream.Measure()
    >>> romanText.translate.appendMeasureToRepeatEndingsDict(rtm, m1, repeatEndings)
    >>> repeatEndings
    {1: [(15, <music21.stream.Measure 0a offset=0.0>)]}
    >>> romanText.translate.appendMeasureToRepeatEndingsDict(rtm2, m2, repeatEndings)
    >>> repeatEndings[1], repeatEndings[2]
    ([(15, <music21.stream.Measure 0a offset=0.0>)],
     [(15, <music21.stream.Measure 0b offset=0.0>)])
    >>> repeatEndings[2][0][1] is m2
    True
    ```

music21.romanText.translate.fixPickupMeasure(*partObject*)[[source]](../_modules/music21/romanText/translate.html#fixPickupMeasure)
:   Fix a pickup measure if any.

    We determine a pickup measure by being measure 0 and not having an RN
    object at the beginning. Will also pad the last measure right and
    cut the duration of the final chord to match.

    Demonstration: an otherwise incorrect part

    ```python
    >>> p = stream.Part()
    >>> m0 = stream.Measure()
    >>> m0.number = 0
    >>> k0 = key.Key('G')
    >>> m0.insert(0, k0)
    >>> m0.insert(0, meter.TimeSignature('4/4'))
    >>> m0.insert(3, roman.RomanNumeral('I', k0, quarterLength=1.0))
    >>> m1 = stream.Measure()
    >>> m1.number = 1
    >>> m1.append(roman.RomanNumeral('V', k0, quarterLength=4.0))
    >>> m2 = stream.Measure()
    >>> m2.number = 2
    >>> m2.append(roman.RomanNumeral('I', k0, quarterLength=4.0))
    >>> p.insert(0, m0)
    >>> p.insert(4, m1)
    >>> p.insert(8, m2)
    ```

    After running fixPickupMeasure()

    ```python
    >>> romanText.translate.fixPickupMeasure(p)
    >>> p.show('text')
    {0.0} <music21.stream.Measure 0 offset=0.0>
        {0.0} <music21.key.Key of G major>
        {0.0} <music21.meter.TimeSignature 4/4>
        {0.0} <music21.roman.RomanNumeral I in G major>
    {1.0} <music21.stream.Measure 1 offset=1.0>
        {0.0} <music21.roman.RomanNumeral V in G major>
    {5.0} <music21.stream.Measure 2 offset=5.0>
        {0.0} <music21.roman.RomanNumeral I in G major>
    ```

    ```python
    >>> m0.paddingLeft
    3.0
    >>> m2.paddingRight
    1.0
    >>> m2[roman.RomanNumeral].last().duration
    <music21.duration.Duration 3.0>
    ```

music21.romanText.translate.romanTextToStreamOpus(*rtHandler*, *inputM21=None*)[[source]](../_modules/music21/romanText/translate.html#romanTextToStreamOpus)
:   The main processing routine for RomanText objects that may or may not
    be multi movement.

    Takes in a romanText.rtObjects.RTFile() object, or a string as rtHandler.

    Runs romanTextToStreamScore() as its main work.

    If inputM21 is None then it will create a Score or Opus object.

    Return either a Score object, or, if a multi-movement work is defined, an
    Opus object.

music21.romanText.translate.romanTextToStreamScore(*rtHandler*, *inputM21=None*)[[source]](../_modules/music21/romanText/translate.html#romanTextToStreamScore)
:   The main processing module for single-movement RomanText works.

    Given a romanText handler or string, return or fill a Score Stream.
