Source: https://music21.org/music21docs/moduleReference/moduleHumdrumSpineParser.html

# music21.humdrum.spineParser

music21.humdrum.spineParser is a collection of utilities for changing
native humdrum code into music21 streams. Most music21 users will
simply want to call:

```python
>>> myFile = converter.parse('myFile.krn')
>>> myFile.show()
```

The methods in here are documented for developers wishing to expand
music21’s ability to parse humdrum.

SpineParsing consists of several steps.

* The data file is read in and all events are sliced horizontally (EventCollections)
  :   and vertically (Protospines)
* Protospines are parsed into HumdrumSpines by following Spine Path Indicators
  :   (`*^` and `*v` especially)
      Protospines that separate become new Protospines with their parentSpine indicated. Protospines
      that merge again then followed by the same Protospine as before. This will cause problems if
      a voice re-merges with another staff, but in practice I have not
      seen a .krn file that does this and
      should be avoided in any case.
* HumdrumSpines are reclassed according to their exclusive definition.
  :   `**kern` becomes KernSpines, etc.
* All reclassed HumdrumSpines are filled with music21 objects in their .stream property.
  :   Measures are put into the spine but are empty containers. The resulting
      HumdrumSpine.stream objects
      look like Stream.flatten(retainContainers=True) versions in many ways.
* For HumdrumSpines with parent spines their .stream contents are then
  :   inserted into their parent spines with
      voice tagged as a music21 Group property.
* Lyrics and Dynamics are placed into their corresponding HumdrumSpine.stream objects.
* Stream elements are moved into their measures within a Stream.
* Measures are searched for elements with voice groups and Voice objects are created.
* Changed in v10: flag attributes isSpineLine, isComment, isGlobal, isReference have been
  :   removed from HumdrumLine and all subclasses. isinstance(…) is a bit slower than
      checking these, but adds correct typing. Nothing is stored with weakrefs. .iterIndex
      and hand roled iterator/generators are gone now (could’ve gone when Python 2.4 became
      the minimum version). HumdrumDataCollection.parsePositionInStream is gone (was
      duplicating numLines); HumdrumDataCollection.fileLength is now the read-only
      property numLines (= len(self.dataStream)); HumdrumLine.position and
      SpineEvent.position were both renamed to lineNumber and now hold the 1-based
      source line number (was eventList index for SpineEvent),
      advancing on blank lines too. Blank lines now produce BlankLine HumdrumLine
      entries rather than being skipped, so eventList[lineNumber - 1] always
      resolves to the line at that source position.

## BlankLine

class music21.humdrum.spineParser.BlankLine(*lineNumber: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*)[[source]](../_modules/music21/humdrum/spineParser.html#BlankLine)
:   A blank line in a humdrum source. Humdrum forbids blank lines, but
    they appear in the wild. Storing them as BlankLine objects keeps
    eventList aligned with the source: eventList[lineNumber - 1] is
    always the HumdrumLine at that 1-based source line.

    Treated as a global event by parseProtoSpinesAndEventCollections
    (no SpineEvent is created at this line for any spine).

    ```python
    >>> b = humdrum.spineParser.BlankLine(lineNumber=12)
    >>> b
    <music21.humdrum.spineParser.BlankLine line 12>
    >>> b.lineNumber
    12
    ```

[`BlankLine`](#music21.humdrum.spineParser.BlankLine "music21.humdrum.spineParser.BlankLine") bases

* [`HumdrumLine`](#music21.humdrum.spineParser.HumdrumLine "music21.humdrum.spineParser.HumdrumLine")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`BlankLine`](#music21.humdrum.spineParser.BlankLine "music21.humdrum.spineParser.BlankLine") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

## DynamSpine

class music21.humdrum.spineParser.DynamSpine(*spineId: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*, *eventList: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[SpineEvent](#music21.humdrum.spineParser.SpineEvent "music21.humdrum.spineParser.SpineEvent")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *streamClass: [type](moduleBar.html#music21.bar.Barline.type "music21.bar.Barline.type")[[Stream](moduleStreamBase.html#music21.stream.base.Stream "music21.stream.base.Stream")] = <class 'music21.stream.base.Stream'>*, *parentSpineCollection: [SpineCollection](#music21.humdrum.spineParser.SpineCollection "music21.humdrum.spineParser.SpineCollection") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](../_modules/music21/humdrum/spineParser.html#DynamSpine)
:   A DynamSpine is a type of humdrum spine with the \*\*dynam
    attribute set and thus events are processed as if they
    are dynamics.

[`DynamSpine`](#music21.humdrum.spineParser.DynamSpine "music21.humdrum.spineParser.DynamSpine") bases

* [`HumdrumSpine`](#music21.humdrum.spineParser.HumdrumSpine "music21.humdrum.spineParser.HumdrumSpine")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`DynamSpine`](#music21.humdrum.spineParser.DynamSpine "music21.humdrum.spineParser.DynamSpine") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`DynamSpine`](#music21.humdrum.spineParser.DynamSpine "music21.humdrum.spineParser.DynamSpine") read/write properties

Read/write properties inherited from [`HumdrumSpine`](#music21.humdrum.spineParser.HumdrumSpine "music21.humdrum.spineParser.HumdrumSpine"):

|  |  |  |
| --- | --- | --- |
| * [`spineType`](#music21.humdrum.spineParser.HumdrumSpine.spineType "music21.humdrum.spineParser.HumdrumSpine.spineType") |  |  |

[`DynamSpine`](#music21.humdrum.spineParser.DynamSpine "music21.humdrum.spineParser.DynamSpine") methods

DynamSpine.parse() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/humdrum/spineParser.html#DynamSpine.parse)
:   Dummy method that pushes all these objects to HumdrumSpine.stream
    as ElementWrappers. Should be overridden in
    specific Spine subclasses.

Methods inherited from [`HumdrumSpine`](#music21.humdrum.spineParser.HumdrumSpine "music21.humdrum.spineParser.HumdrumSpine"):

|  |  |  |
| --- | --- | --- |
| * [`append()`](#music21.humdrum.spineParser.HumdrumSpine.append "music21.humdrum.spineParser.HumdrumSpine.append") | * [`moveElementsIntoMeasures()`](#music21.humdrum.spineParser.HumdrumSpine.moveElementsIntoMeasures "music21.humdrum.spineParser.HumdrumSpine.moveElementsIntoMeasures") |  |

## EventCollection

class music21.humdrum.spineParser.EventCollection(*maxSpines: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*, *lineNumber: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*)[[source]](../_modules/music21/humdrum/spineParser.html#EventCollection)
:   An EventCollection holds every event that appears on a single source line
    of a humdrum file – one cell per spine, in their events array.

    If a spine’s cell on this line is ‘.’ or a comment (no new event), use
    lastEvents[spineNum] to retrieve the previous event still sounding.
    getSpineOccurring returns either the current event or the last event
    that’s still active.

    Theses events should happen at the same time (offset)
    but they are not necessarily the only events to happen at that same time.
    E.g. a clef change and the note that follows it on the next line take place at
    the same musical time but live in different EventCollections.

    These objects normally get created by
    [`parseProtoSpinesAndEventCollections()`](#music21.humdrum.spineParser.HumdrumDataCollection.parseProtoSpinesAndEventCollections "music21.humdrum.spineParser.HumdrumDataCollection.parseProtoSpinesAndEventCollections")
    so you won’t need to do all the setup.

    Assume that ec1 is

    > C4 pp

    on source line 4, and ec2 is

    > D4 .

    on source line 5:

    ```python
    >>> SE = humdrum.spineParser.SpineEvent
    >>> eventList1 = [SE('C4', lineNumber=4), SE('pp', lineNumber=4)]
    >>> eventList2 = [SE('D4', lineNumber=5), SE('.', lineNumber=5)]
    >>> ec1 = humdrum.spineParser.EventCollection(maxSpines=2, lineNumber=4)
    >>> ec1.events = eventList1
    >>> ec2 = humdrum.spineParser.EventCollection(maxSpines=2, lineNumber=5)
    >>> ec2.events = eventList2
    >>> ec2.lastEvents[1] = eventList1[1]
    >>> ec2.maxSpines
    2
    >>> ec2.lineNumber
    5
    >>> ec2.getAllOccurring()
    [<music21.humdrum.spineParser.SpineEvent D4>, <music21.humdrum.spineParser.SpineEvent pp>]
    ```

    If there were spine path markers this next boolean would be true:

    ```python
    >>> ec2.spinePathData
    False
    ```

    In the future, EventCollection may enforce that all events have the same lineNumber

    * New in v10: lineNumber

[`EventCollection`](#music21.humdrum.spineParser.EventCollection "music21.humdrum.spineParser.EventCollection") bases

* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`EventCollection`](#music21.humdrum.spineParser.EventCollection "music21.humdrum.spineParser.EventCollection") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`EventCollection`](#music21.humdrum.spineParser.EventCollection "music21.humdrum.spineParser.EventCollection") methods

EventCollection.addGlobalEvent(*globalEvent: [HumdrumLine](#music21.humdrum.spineParser.HumdrumLine "music21.humdrum.spineParser.HumdrumLine")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/humdrum/spineParser.html#EventCollection.addGlobalEvent)

EventCollection.addLastSpineEvent(*spineNum: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *spineEvent: [SpineEvent](#music21.humdrum.spineParser.SpineEvent "music21.humdrum.spineParser.SpineEvent")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/humdrum/spineParser.html#EventCollection.addLastSpineEvent)

EventCollection.addSpineEvent(*spineNum: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *spineEvent: [SpineEvent](#music21.humdrum.spineParser.SpineEvent "music21.humdrum.spineParser.SpineEvent")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/humdrum/spineParser.html#EventCollection.addSpineEvent)

EventCollection.getAllOccurring() → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[SpineEvent](#music21.humdrum.spineParser.SpineEvent "music21.humdrum.spineParser.SpineEvent") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][[source]](../_modules/music21/humdrum/spineParser.html#EventCollection.getAllOccurring)

EventCollection.getSpineEvent(*spineNum: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [SpineEvent](#music21.humdrum.spineParser.SpineEvent "music21.humdrum.spineParser.SpineEvent") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/humdrum/spineParser.html#EventCollection.getSpineEvent)

EventCollection.getSpineOccurring(*spineNum: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [SpineEvent](#music21.humdrum.spineParser.SpineEvent "music21.humdrum.spineParser.SpineEvent") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/humdrum/spineParser.html#EventCollection.getSpineOccurring)

## GlobalComment

class music21.humdrum.spineParser.GlobalComment(*comment: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*, *\*\*keywords*)[[source]](../_modules/music21/humdrum/spineParser.html#GlobalComment)
:   A Music21Object that represents a comment for the whole score

    ```python
    >>> sc = humdrum.spineParser.GlobalComment('!! this is a global comment')
    >>> sc
    <music21.humdrum.spineParser.GlobalComment 'this is a global comment'>
    >>> sc.comment
    'this is a global comment'
    ```

[`GlobalComment`](#music21.humdrum.spineParser.GlobalComment "music21.humdrum.spineParser.GlobalComment") bases

* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`GlobalComment`](#music21.humdrum.spineParser.GlobalComment "music21.humdrum.spineParser.GlobalComment") read-only properties

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`GlobalComment`](#music21.humdrum.spineParser.GlobalComment "music21.humdrum.spineParser.GlobalComment") read/write properties

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`GlobalComment`](#music21.humdrum.spineParser.GlobalComment "music21.humdrum.spineParser.GlobalComment") methods

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`GlobalComment`](#music21.humdrum.spineParser.GlobalComment "music21.humdrum.spineParser.GlobalComment") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## GlobalCommentLine

class music21.humdrum.spineParser.GlobalCommentLine(*lineNumber: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*, *contents: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*)[[source]](../_modules/music21/humdrum/spineParser.html#GlobalCommentLine)
:   A GlobalCommentLine is a humdrum comment that pertains to all spines
    In humdrum it is represented by two exclamation points (and usually one space)

    The GlobalComment object takes two inputs and stores them as attributes:

    ```python
    lineNumber (1-based line number in the humdrum file)
    contents   (string of contents)
    value      (contents minus !!)
    ```

    The constructor can be passed (lineNumber, contents); if contents begins with
    bangs, they are removed along with up to one space directly afterwards.

    ```python
    >>> com1 = humdrum.spineParser.GlobalCommentLine(
    ...          lineNumber=4, contents='!! this comment is global')
    >>> com1
    <music21.humdrum.spineParser.GlobalCommentLine 'this comment is global'>
    >>> com1.lineNumber
    4
    >>> com1.contents
    '!! this comment is global'
    >>> com1.value
    'this comment is global'
    ```

[`GlobalCommentLine`](#music21.humdrum.spineParser.GlobalCommentLine "music21.humdrum.spineParser.GlobalCommentLine") bases

* [`HumdrumLine`](#music21.humdrum.spineParser.HumdrumLine "music21.humdrum.spineParser.HumdrumLine")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`GlobalCommentLine`](#music21.humdrum.spineParser.GlobalCommentLine "music21.humdrum.spineParser.GlobalCommentLine") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

## GlobalReference

class music21.humdrum.spineParser.GlobalReference(*codeOrAll: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*, *valueOrNone: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\*\*keywords*)[[source]](../_modules/music21/humdrum/spineParser.html#GlobalReference)
:   A Music21Object that represents a reference in the score, called a “reference record”
    in Humdrum. See Humdrum User’s Guide Chapter 2.

    ```python
    >>> sc = humdrum.spineParser.GlobalReference('!!!REF:this is a global reference')
    >>> sc
    <music21.humdrum.spineParser.GlobalReference REF 'this is a global reference'>
    >>> sc.code
    'REF'
    >>> sc.value
    'this is a global reference'
    ```

    Alternate form:

    ```python
    >>> sc = humdrum.spineParser.GlobalReference('REF', 'this is a global reference')
    >>> sc
    <music21.humdrum.spineParser.GlobalReference REF 'this is a global reference'>
    >>> sc.code
    'REF'
    >>> sc.value
    'this is a global reference'
    ```

    Language codes are parsed:

    ```python
    >>> sc = humdrum.spineParser.GlobalReference('!!!OPT@@RUS: Vesna svyashchennaya')
    >>> sc.code
    'OPT'
    >>> sc.language
    'RUS'
    >>> sc.isPrimary
    True
    ```

    ```python
    >>> sc = humdrum.spineParser.GlobalReference('!!!OPT@FRE: Le sacre du printemps')
    >>> sc.code
    'OPT'
    >>> sc.language
    'FRE'
    >>> sc.isPrimary
    False
    ```

[`GlobalReference`](#music21.humdrum.spineParser.GlobalReference "music21.humdrum.spineParser.GlobalReference") bases

* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`GlobalReference`](#music21.humdrum.spineParser.GlobalReference "music21.humdrum.spineParser.GlobalReference") read-only properties

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`GlobalReference`](#music21.humdrum.spineParser.GlobalReference "music21.humdrum.spineParser.GlobalReference") read/write properties

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`GlobalReference`](#music21.humdrum.spineParser.GlobalReference "music21.humdrum.spineParser.GlobalReference") methods

GlobalReference.updateMetadata(*md: [Metadata](moduleMetadata.html#music21.metadata.Metadata "music21.metadata.Metadata")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/humdrum/spineParser.html#GlobalReference.updateMetadata)
:   update a metadata object according to information in this GlobalReference

    See humdrum guide Appendix I for information

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`GlobalReference`](#music21.humdrum.spineParser.GlobalReference "music21.humdrum.spineParser.GlobalReference") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## GlobalReferenceLine

class music21.humdrum.spineParser.GlobalReferenceLine(*lineNumber: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*, *contents: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = '!!! NUL: None'*)[[source]](../_modules/music21/humdrum/spineParser.html#GlobalReferenceLine)
:   A GlobalReferenceLine is a type of HumdrumLine that contains
    information/metadata about the humdrum document.

    In humdrum it is represented by three exclamation points
    followed by non-whitespace followed by a colon. Examples:

    ```python
    !!!COM: Stravinsky, Igor Fyodorovich
    !!!CDT: 1882/6/17/-1971/4/6
    !!!ODT: 1911//-1913//; 1947//
    !!!OPT@@RUS: Vesna svyashchennaya
    !!!OPT@FRE: Le sacre du printemps
    ```

    The GlobalReferenceLine object takes two inputs:

    ```python
    lineNumber   1-based line number in the humdrum file
    contents     string of contents
    ```

    And stores them as three attributes:

    ```python
    lineNumber: as above
    code:       non-whitespace code (usually three letters)
    value:      its value
    ```

    ```python
    >>> gr = humdrum.spineParser.GlobalReferenceLine(
    ...        lineNumber=20, contents='!!!COM: Stravinsky, Igor Fyodorovich\n')
    >>> gr
    <music21.humdrum.spineParser.GlobalReferenceLine COM: 'Stravinsky, Igor Fyodorovich'>
    >>> gr.lineNumber
    20
    >>> gr.code
    'COM'
    >>> gr.value
    'Stravinsky, Igor Fyodorovich'
    ```

    TODO: add parsing of three-digit Kern comment codes into fuller metadata
    TODO: parse `@`/`@@` language tags here (e.g. `!!!OPT@@RUS:`, `!!!OPT@FRE:`)
    and propagate language/isPrimary so that GlobalReference.updateMetadata
    can attach `metadata.Text(value, language=...)` instead of bare strings.

[`GlobalReferenceLine`](#music21.humdrum.spineParser.GlobalReferenceLine "music21.humdrum.spineParser.GlobalReferenceLine") bases

* [`HumdrumLine`](#music21.humdrum.spineParser.HumdrumLine "music21.humdrum.spineParser.HumdrumLine")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`GlobalReferenceLine`](#music21.humdrum.spineParser.GlobalReferenceLine "music21.humdrum.spineParser.GlobalReferenceLine") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

## HarmSpine

class music21.humdrum.spineParser.HarmSpine(*spineId: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*, *eventList: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[SpineEvent](#music21.humdrum.spineParser.SpineEvent "music21.humdrum.spineParser.SpineEvent")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *streamClass: [type](moduleBar.html#music21.bar.Barline.type "music21.bar.Barline.type")[[Stream](moduleStreamBase.html#music21.stream.base.Stream "music21.stream.base.Stream")] = <class 'music21.stream.base.Stream'>*, *parentSpineCollection: [SpineCollection](#music21.humdrum.spineParser.SpineCollection "music21.humdrum.spineParser.SpineCollection") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](../_modules/music21/humdrum/spineParser.html#HarmSpine)
:   A HarmSpine is a type of humdrum spine with the \*\*harm
    attribute set and thus events are processed as if they
    are harmonic analysis annotations in the “harm” syntax.

    The harm roman numeral annotations are parsed using
    a superset of the original \*\*harm Humdrum representation, written
    for python and extending the syntax based on other projects like the
    RomanText and the MuseScore roman numeral notations.

[`HarmSpine`](#music21.humdrum.spineParser.HarmSpine "music21.humdrum.spineParser.HarmSpine") bases

* [`HumdrumSpine`](#music21.humdrum.spineParser.HumdrumSpine "music21.humdrum.spineParser.HumdrumSpine")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`HarmSpine`](#music21.humdrum.spineParser.HarmSpine "music21.humdrum.spineParser.HarmSpine") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`HarmSpine`](#music21.humdrum.spineParser.HarmSpine "music21.humdrum.spineParser.HarmSpine") read/write properties

Read/write properties inherited from [`HumdrumSpine`](#music21.humdrum.spineParser.HumdrumSpine "music21.humdrum.spineParser.HumdrumSpine"):

|  |  |  |
| --- | --- | --- |
| * [`spineType`](#music21.humdrum.spineParser.HumdrumSpine.spineType "music21.humdrum.spineParser.HumdrumSpine.spineType") |  |  |

[`HarmSpine`](#music21.humdrum.spineParser.HarmSpine "music21.humdrum.spineParser.HarmSpine") methods

HarmSpine.parse() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/humdrum/spineParser.html#HarmSpine.parse)
:   Dummy method that pushes all these objects to HumdrumSpine.stream
    as ElementWrappers. Should be overridden in
    specific Spine subclasses.

Methods inherited from [`HumdrumSpine`](#music21.humdrum.spineParser.HumdrumSpine "music21.humdrum.spineParser.HumdrumSpine"):

|  |  |  |
| --- | --- | --- |
| * [`append()`](#music21.humdrum.spineParser.HumdrumSpine.append "music21.humdrum.spineParser.HumdrumSpine.append") | * [`moveElementsIntoMeasures()`](#music21.humdrum.spineParser.HumdrumSpine.moveElementsIntoMeasures "music21.humdrum.spineParser.HumdrumSpine.moveElementsIntoMeasures") |  |

## HumdrumDataCollection

class music21.humdrum.spineParser.HumdrumDataCollection(*dataStream: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*)[[source]](../_modules/music21/humdrum/spineParser.html#HumdrumDataCollection)
:   Note

    Most users should not need to be here. Just run converter.parse(‘file.krn’)
    and it will give you a stream.Score instead.
    Intermediate users who want to get into the guts of Humdrum are still
    probably better off running humdrum.parseFile(“filename”)
    which returns a humdrum.SpineCollection directly.

    A HumdrumDataCollection takes in a mandatory list where each element
    is a line of humdrum data. Together this list represents a collection
    of spines. Essentially it’s the contents of a humdrum file.

    Usually you will probably want to use HumdrumFile which can read
    in a file directly. This class exists in case you have your Humdrum
    data in another format (database, from the web, etc.) and already
    have it as a string.

    LIMITATIONS:
    (1) Spines cannot change definition (\*\*exclusive interpretations) mid-spine.

    > So if you start off with \*\*kern, the rest of the spine needs to be
    > \*\*kern (actually, the first exclusive interpretation for a spine is
    > used throughout).
    >
    > Note that, even though changing exclusive interpretations mid-spine
    > seems to be legal by the humdrum definition, it looks like none of the
    > conventional humdrum parsing tools allow for changing
    > definitions mid-spine, so I don’t think this limitation is a problem.
    > (Craig Stuart Sapp confirmed this to me.)
    >
    > The Aarden/Miller Palestrina dataset uses \*- followed by \*\*kern
    > at the changes of sections thus some parsing of multiple exclusive
    > interpretations in a protospine may be necessary. But none change definition.

    2. Split spines are assumed to be voices in a single spine staff.

[`HumdrumDataCollection`](#music21.humdrum.spineParser.HumdrumDataCollection "music21.humdrum.spineParser.HumdrumDataCollection") bases

* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`HumdrumDataCollection`](#music21.humdrum.spineParser.HumdrumDataCollection "music21.humdrum.spineParser.HumdrumDataCollection") read-only properties

HumdrumDataCollection.numLines
:   The number of lines in self.dataStream, including blank lines.

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`HumdrumDataCollection`](#music21.humdrum.spineParser.HumdrumDataCollection "music21.humdrum.spineParser.HumdrumDataCollection") methods

HumdrumDataCollection.createHumdrumSpines(*protoSpines: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[ProtoSpine](#music21.humdrum.spineParser.ProtoSpine "music21.humdrum.spineParser.ProtoSpine")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *eventCollections: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[EventCollection](#music21.humdrum.spineParser.EventCollection "music21.humdrum.spineParser.EventCollection")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [SpineCollection](#music21.humdrum.spineParser.SpineCollection "music21.humdrum.spineParser.SpineCollection")[[source]](../_modules/music21/humdrum/spineParser.html#HumdrumDataCollection.createHumdrumSpines)
:   Takes the data from the object’s protoSpines and eventCollections
    and returns a [`SpineCollection`](#music21.humdrum.spineParser.SpineCollection "music21.humdrum.spineParser.SpineCollection")
    object that contains HumdrumSpine() objects.

    A HumdrumSpine object differs from a ProtoSpine in that it follows
    spinePathData – a ProtoSpine records all data in a given tab
    position, and thus might consist of data from several
    spines that move around. HumdrumSpines are smart enough not to
    have this limitation.

    When we check for spinePathData we look for the following spine
    path indicators (from HumdrumDoc):

    ```python
    *+    add a new spine (to the right of the current spine)
    *-    terminate a current spine
    *^    split a spine (into two)
    *v    join (two or more) spines into one
    *x    exchange the position of two spines
    *     do nothing
    ```

HumdrumDataCollection.determineIfDataStreamIsOpus(*dataStream: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)"), [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][[source]](../_modules/music21/humdrum/spineParser.html#HumdrumDataCollection.determineIfDataStreamIsOpus)
:   Some Humdrum files contain multiple pieces in one file
    which are better represented as `Opus`
    file containing multiple scores.

    This method examines that dataStream (or self.dataStream) and
    if it only has a single piece then it returns (False, None).

    If it has multiple pieces, it returns True and a list of dataStreams.

    ```python
    >>> from pprint import pprint as pp
    ```

    ```python
    >>> mps = humdrum.testFiles.multipartSanctus
    >>> hdc = humdrum.spineParser.HumdrumDataCollection(mps)
    >>> (hasOpus, dataCollections) = hdc.determineIfDataStreamIsOpus()
    >>> hasOpus
    True
    >>> pp(dataCollections)
    [['!!!COM: Palestrina, Giovanni Perluigi da',
      '**kern\t**kern\t**kern\t**kern',
      '*Ibass\t*Itenor\t*Icalto\t*Icant',
      '!Bassus\t!Tenor\t!Altus\t!Cantus',
      '*clefF4\t*clefGv2\t*clefG2\t*clefG2',
      '*M4/2\t*M4/2\t*M4/2\t*M4/2',
      '=1\t=1\t=1\t=1',
      '0r\t0r\t1g\t1r',
      '.\t.\t1a\t1cc',
      '=2\t=2\t=2\t=2',
      '0r\t0r\t1g\t1dd',
      '.\t.\t1r\t1cc',
      '*-\t*-\t*-\t*-'],
     ['!! Pleni',
      '**kern\t**kern\t**kern',
      '*Ibass\t*Itenor\t*Icalto',
      '*clefF4\t*clefGv2\t*clefG2',
      '*M4/2\t*M4/2\t*M4/2',
      '=3\t=3\t=3',
      '1G\t1r\t0r',
      '1A\t1c\t.',
      '=4\t=4\t=4',
      '1B\t1d\t1r',
      '1c\t1e\t1g',
      '*-\t*-\t*-'],
     ['!! Hosanna',
      '**kern\t**kern\t**kern\t**kern',
      '*Ibass\t*Itenor\t*Icalto\t*Icant',
      '*clefF4\t*clefGv2\t*clefG2\t*clefG2',
      '*M3/2\t*M3/2\t*M3/2\t*M3/2',
      '=5\t=5\t=5\t=5',
      '1r\t1r\t1g\t1r',
      '2r\t2r\t[2a\t[2cc',
      '=5\t=5\t=5\t=5',
      '1r\t1r\t2a]\t2cc]',
      '.\t.\t2f\t1dd',
      '2r\t2r\t2g\t.',
      '*-\t*-\t*-\t*-']]
    ```

HumdrumDataCollection.insertGlobalEvents() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/humdrum/spineParser.html#HumdrumDataCollection.insertGlobalEvents)
:   Insert the Global Events (GlobalReferenceLines and GlobalCommentLines) into an appropriate
    place in the outer Stream.

    Run after self.spineCollection.createMusic21Streams().
    Is run automatically by self.parse().
    uses self.spineCollection.getOffsetsAndPrioritiesByLineNumber()

HumdrumDataCollection.parse() → [Score](moduleStreamBase.html#music21.stream.base.Score "music21.stream.base.Score") | [Opus](moduleStreamBase.html#music21.stream.base.Opus "music21.stream.base.Opus")[[source]](../_modules/music21/humdrum/spineParser.html#HumdrumDataCollection.parse)
:   Parse self.dataStream into music21 objects, returning the resulting
    `Score` (or `Opus`
    for multipart files like the Palestrina dataset).

    The parsed stream is also stored on self.stream.

HumdrumDataCollection.parseEventListFromDataStream(*dataStream: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[HumdrumLine](#music21.humdrum.spineParser.HumdrumLine "music21.humdrum.spineParser.HumdrumLine")][[source]](../_modules/music21/humdrum/spineParser.html#HumdrumDataCollection.parseEventListFromDataStream)
:   Sets self.eventList from a dataStream (that is, a
    list of lines). It sets self.maxSpines to the
    largest number of spine events found on any line
    in the file.

    The difference between the dataStream and self.eventList
    are the following:

    > * Blank lines are skipped.
    > * !!! lines become [`GlobalReferenceLine`](#music21.humdrum.spineParser.GlobalReferenceLine "music21.humdrum.spineParser.GlobalReferenceLine") objects
    > * !! lines become [`GlobalCommentLine`](#music21.humdrum.spineParser.GlobalCommentLine "music21.humdrum.spineParser.GlobalCommentLine") objects
    > * all other lines become [`SpineLine`](#music21.humdrum.spineParser.SpineLine "music21.humdrum.spineParser.SpineLine") objects

    Returns eventList in addition to setting it as self.eventList.

    ```python
    >>> eventString = ('!!! COM: Beethoven, Ludwig van\n' +
    ...                '!! Not really a piece by Beethoven\n' +
    ...                '**kern\t**dynam\n' +
    ...                'C4\tpp\n' +
    ...                'D8\t.\n')
    >>> hdc = humdrum.spineParser.HumdrumDataCollection(eventString)
    >>> hdc.maxSpines = 2
    >>> eList = hdc.parseEventListFromDataStream()
    >>> eList is hdc.eventList
    True
    >>> for e in eList:
    ...     print(e)
    <music21.humdrum.spineParser.GlobalReferenceLine COM: 'Beethoven, Ludwig van'>
    <music21.humdrum.spineParser.GlobalCommentLine 'Not really a piece by Beethoven'>
    <music21.humdrum.spineParser.SpineLine line 3 (2 spines)>
    <music21.humdrum.spineParser.SpineLine line 4 (2 spines)>
    <music21.humdrum.spineParser.SpineLine line 5 (2 spines)>
    >>> print(eList[0].value)
    Beethoven, Ludwig van
    ```

    Print line number 4 (which is eList[3] in zero indexed)

    ```python
    >>> print(eList[3].spineData)
    ['C4', 'pp']
    ```

HumdrumDataCollection.parseMetadata(*s: [Stream](moduleStreamBase.html#music21.stream.base.Stream "music21.stream.base.Stream") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/humdrum/spineParser.html#HumdrumDataCollection.parseMetadata)
:   Create a metadata object for the file.

HumdrumDataCollection.parseNonOpus(*dataStream: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*) → [Score](moduleStreamBase.html#music21.stream.base.Score "music21.stream.base.Score")[[source]](../_modules/music21/humdrum/spineParser.html#HumdrumDataCollection.parseNonOpus)
:   The main parse function for non-opus data collections.

    Populates self.stream (a `Score`) and returns it.

HumdrumDataCollection.parseOpusDataCollections(*dataCollections: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*) → [Opus](moduleStreamBase.html#music21.stream.base.Opus "music21.stream.base.Opus")[[source]](../_modules/music21/humdrum/spineParser.html#HumdrumDataCollection.parseOpusDataCollections)
:   Take a dataCollection from determineIfDataStreamIsOpus
    and set self.stream to be an Opus instead.

    ```python
    >>> mps = humdrum.testFiles.multipartSanctus
    >>> hdc = humdrum.spineParser.HumdrumDataCollection(mps)
    >>> (hasOpus, dataCollections) = hdc.determineIfDataStreamIsOpus()
    >>> if hasOpus is True:
    ...     op = hdc.parseOpusDataCollections(dataCollections)
    ...     print(len(op.scores))
    ...     for sc in op.scores:
    ...        print(sc)
    3
    <music21.stream.Score section_1>
    <music21.stream.Score section_2>
    <music21.stream.Score section_3>
    ```

HumdrumDataCollection.parseProtoSpinesAndEventCollections() → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[ProtoSpine](#music21.humdrum.spineParser.ProtoSpine "music21.humdrum.spineParser.ProtoSpine")], [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[EventCollection](#music21.humdrum.spineParser.EventCollection "music21.humdrum.spineParser.EventCollection")]][[source]](../_modules/music21/humdrum/spineParser.html#HumdrumDataCollection.parseProtoSpinesAndEventCollections)
:   Run after
    [`parseEventListFromDataStream()`](#music21.humdrum.spineParser.HumdrumDataCollection.parseEventListFromDataStream "music21.humdrum.spineParser.HumdrumDataCollection.parseEventListFromDataStream")
    to take self.eventList and slice it horizontally
    to get self.eventCollections, which is a list of
    EventCollection objects, or things that happen simultaneously.

    And, more importantly, this method slices self.eventList
    vertically to get self.protoSpines which is a list
    of ProtoSpines, that is a vertical slice of everything that
    happens in a column, regardless of spine-path indicators.

    EventCollection objects store global events. ProtoSpines do not.

    So self.eventCollections and self.protoSpines can each be
    thought of as a two-dimensional sheet of cells, but where
    the first index of the former is the vertical index in
    the dataStream and the first index of the latter is the
    horizontal index in the dataStream. The contents of
    each cell is a SpineEvent object or None (if there’s no
    data at that point). Even ‘.’ (continuation events) get
    translated into SpineEvent objects.

    Calls `parseEventListFromDataStream()`
    if it hasn’t already been called.

    Returns a tuple of protoSpines and eventCollections in addition to
    setting it in the calling object.

    ```python
    >>> eventString = ('!!!COM: Beethoven, Ludwig van\n' +
    ...                '!! Not really a piece by Beethoven\n' +
    ...                '**kern\t**dynam\n' +
    ...                'C4\tpp\n' +
    ...                'D8\t.\n')
    >>> hdc = humdrum.spineParser.HumdrumDataCollection(eventString)
    >>> hdc.maxSpines = 2
    >>> protoSpines, eventCollections = hdc.parseProtoSpinesAndEventCollections()
    >>> protoSpines is hdc.protoSpines
    True
    >>> eventCollections is hdc.eventCollections
    True
    ```

    Looking at individual slices is unlikely to tell you much:

    ```python
    >>> for thisSlice in eventCollections:
    ...    print(thisSlice)
    <music21.humdrum.spineParser.EventCollection line 1, 2 events, 2 spines>
    <music21.humdrum.spineParser.EventCollection line 2, 2 events, 2 spines>
    <music21.humdrum.spineParser.EventCollection line 3, 2 events, 2 spines>
    <music21.humdrum.spineParser.EventCollection line 4, 2 events, 2 spines>
    <music21.humdrum.spineParser.EventCollection line 5, 2 events, 2 spines>
    ```

    ```python
    >>> for thisSlice in protoSpines:
    ...    print(thisSlice)
    <music21.humdrum.spineParser.ProtoSpine 5 events>
    <music21.humdrum.spineParser.ProtoSpine 5 events>
    ```

    But looking at the individual slices is revealing:

    ```python
    >>> eventCollections[4].getAllOccurring()
    [<music21.humdrum.spineParser.SpineEvent D8>, <music21.humdrum.spineParser.SpineEvent pp>]
    ```

    ```python
    >>> for protoEvent in protoSpines[0]:
    ...    print(repr(protoEvent))
    None
    None
    <music21.humdrum.spineParser.SpineEvent **kern>
    <music21.humdrum.spineParser.SpineEvent C4>
    <music21.humdrum.spineParser.SpineEvent D8>
    ```

## HumdrumFile

class music21.humdrum.spineParser.HumdrumFile(*filename: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [pathlib.Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")*)[[source]](../_modules/music21/humdrum/spineParser.html#HumdrumFile)
:   A HumdrumFile is a HumdrumDataCollection which takes
    as a mandatory argument a filename to be opened and read.

[`HumdrumFile`](#music21.humdrum.spineParser.HumdrumFile "music21.humdrum.spineParser.HumdrumFile") bases

* [`HumdrumDataCollection`](#music21.humdrum.spineParser.HumdrumDataCollection "music21.humdrum.spineParser.HumdrumDataCollection")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`HumdrumFile`](#music21.humdrum.spineParser.HumdrumFile "music21.humdrum.spineParser.HumdrumFile") read-only properties

Read-only properties inherited from [`HumdrumDataCollection`](#music21.humdrum.spineParser.HumdrumDataCollection "music21.humdrum.spineParser.HumdrumDataCollection"):

|  |  |  |
| --- | --- | --- |
| * [`numLines`](#music21.humdrum.spineParser.HumdrumDataCollection.numLines "music21.humdrum.spineParser.HumdrumDataCollection.numLines") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`HumdrumFile`](#music21.humdrum.spineParser.HumdrumFile "music21.humdrum.spineParser.HumdrumFile") methods

HumdrumFile.parseFileHandle(*fileHandle: [Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*) → [Score](moduleStreamBase.html#music21.stream.base.Score "music21.stream.base.Score") | [Opus](moduleStreamBase.html#music21.stream.base.Opus "music21.stream.base.Opus")[[source]](../_modules/music21/humdrum/spineParser.html#HumdrumFile.parseFileHandle)
:   Read all lines from fileHandle into `self.dataStream`, then call
    `parse()` and return its result (a `Score`
    or `Opus`).

HumdrumFile.parseFilename(*filename: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [pathlib.Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/humdrum/spineParser.html#HumdrumFile.parseFilename)

Methods inherited from [`HumdrumDataCollection`](#music21.humdrum.spineParser.HumdrumDataCollection "music21.humdrum.spineParser.HumdrumDataCollection"):

|  |  |  |
| --- | --- | --- |
| * [`createHumdrumSpines()`](#music21.humdrum.spineParser.HumdrumDataCollection.createHumdrumSpines "music21.humdrum.spineParser.HumdrumDataCollection.createHumdrumSpines") * [`determineIfDataStreamIsOpus()`](#music21.humdrum.spineParser.HumdrumDataCollection.determineIfDataStreamIsOpus "music21.humdrum.spineParser.HumdrumDataCollection.determineIfDataStreamIsOpus") * [`insertGlobalEvents()`](#music21.humdrum.spineParser.HumdrumDataCollection.insertGlobalEvents "music21.humdrum.spineParser.HumdrumDataCollection.insertGlobalEvents") | * [`parse()`](#music21.humdrum.spineParser.HumdrumDataCollection.parse "music21.humdrum.spineParser.HumdrumDataCollection.parse") * [`parseEventListFromDataStream()`](#music21.humdrum.spineParser.HumdrumDataCollection.parseEventListFromDataStream "music21.humdrum.spineParser.HumdrumDataCollection.parseEventListFromDataStream") * [`parseMetadata()`](#music21.humdrum.spineParser.HumdrumDataCollection.parseMetadata "music21.humdrum.spineParser.HumdrumDataCollection.parseMetadata") | * [`parseNonOpus()`](#music21.humdrum.spineParser.HumdrumDataCollection.parseNonOpus "music21.humdrum.spineParser.HumdrumDataCollection.parseNonOpus") * [`parseOpusDataCollections()`](#music21.humdrum.spineParser.HumdrumDataCollection.parseOpusDataCollections "music21.humdrum.spineParser.HumdrumDataCollection.parseOpusDataCollections") * [`parseProtoSpinesAndEventCollections()`](#music21.humdrum.spineParser.HumdrumDataCollection.parseProtoSpinesAndEventCollections "music21.humdrum.spineParser.HumdrumDataCollection.parseProtoSpinesAndEventCollections") |

## HumdrumLine

class music21.humdrum.spineParser.HumdrumLine[[source]](../_modules/music21/humdrum/spineParser.html#HumdrumLine)
:   HumdrumLine is a dummy class for subclassing
    [`SpineLine`](#music21.humdrum.spineParser.SpineLine "music21.humdrum.spineParser.SpineLine"),
    [`GlobalCommentLine`](#music21.humdrum.spineParser.GlobalCommentLine "music21.humdrum.spineParser.GlobalCommentLine"), and
    [`GlobalReferenceLine`](#music21.humdrum.spineParser.GlobalReferenceLine "music21.humdrum.spineParser.GlobalReferenceLine") classes
    all of which represent one horizontal line of
    text in a [`HumdrumDataCollection`](#music21.humdrum.spineParser.HumdrumDataCollection "music21.humdrum.spineParser.HumdrumDataCollection")
    that is aware of its
    position in the file.

    See the documentation for the specific classes mentioned above
    for more details.

[`HumdrumLine`](#music21.humdrum.spineParser.HumdrumLine "music21.humdrum.spineParser.HumdrumLine") bases

* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`HumdrumLine`](#music21.humdrum.spineParser.HumdrumLine "music21.humdrum.spineParser.HumdrumLine") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

## HumdrumSpine

class music21.humdrum.spineParser.HumdrumSpine(*spineId: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*, *eventList: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[SpineEvent](#music21.humdrum.spineParser.SpineEvent "music21.humdrum.spineParser.SpineEvent")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *streamClass: [type](moduleBar.html#music21.bar.Barline.type "music21.bar.Barline.type")[[Stream](moduleStreamBase.html#music21.stream.base.Stream "music21.stream.base.Stream")] = <class 'music21.stream.base.Stream'>*, *parentSpineCollection: [SpineCollection](#music21.humdrum.spineParser.SpineCollection "music21.humdrum.spineParser.SpineCollection") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](../_modules/music21/humdrum/spineParser.html#HumdrumSpine)
:   A HumdrumSpine is a representation of a generic HumdrumSpine
    regardless of \*\*definition after spine path indicators have
    been simplified.

    A subclass of HumdrumSpine should be defined for each \*\*type. Those
    subclasses cannot redefine \_\_init\_\_()

    A HumdrumSpine is a collection of events arranged vertically that have a
    connection to each other.
    Each HumdrumSpine MUST have an id (numeric or string) attached to it.

    ```python
    >>> SE = humdrum.spineParser.SpineEvent
    >>> spineEvents = [SE('**kern'), SE('c,4'), SE('d#8')]
    >>> spine1Id = 5
    >>> spine1 = humdrum.spineParser.HumdrumSpine(spine1Id, spineEvents)
    >>> spine1.insertPoint = 5
    >>> spine1.endingPoint = 6
    >>> spine1.parentSpine = 3  # spine 3 is the previous spine leading to this one
    >>> spine1.childSpines = [7, 8]  # the spine ends by being split into spines 7 and 8
    ```

    A spine knows the SpineCollection it belongs to:

    ```python
    >>> spineCollection1 = humdrum.spineParser.SpineCollection()
    >>> spine1.parentSpineCollection = spineCollection1
    ```

    The spineType property searches the EventList or parentSpine to
    figure out the spineType.

    ```python
    >>> spine1.spineType
    'kern'
    ```

    Spines can be iterated through:

    ```python
    >>> for e in spine1:
    ...    print(e)
    **kern
    c,4
    d#8
    ```

    If you’d eventually like this spine to be converted to a class
    other than `Stream`, pass its classname in
    as the streamClass argument:

    ```python
    >>> spine2 = humdrum.spineParser.HumdrumSpine(streamClass=stream.Part)
    >>> spine2.stream
    <music21.stream.Part ...>
    ```

[`HumdrumSpine`](#music21.humdrum.spineParser.HumdrumSpine "music21.humdrum.spineParser.HumdrumSpine") bases

* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`HumdrumSpine`](#music21.humdrum.spineParser.HumdrumSpine "music21.humdrum.spineParser.HumdrumSpine") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`HumdrumSpine`](#music21.humdrum.spineParser.HumdrumSpine "music21.humdrum.spineParser.HumdrumSpine") read/write properties

HumdrumSpine.spineType
:   searches the current and parent spineType for a search

[`HumdrumSpine`](#music21.humdrum.spineParser.HumdrumSpine "music21.humdrum.spineParser.HumdrumSpine") methods

HumdrumSpine.append(*event: [SpineEvent](#music21.humdrum.spineParser.SpineEvent "music21.humdrum.spineParser.SpineEvent")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/humdrum/spineParser.html#HumdrumSpine.append)
:   add an item to this Spine

HumdrumSpine.moveElementsIntoMeasures(*streamIn: [Stream](moduleStreamBase.html#music21.stream.base.Stream "music21.stream.base.Stream")*) → [Stream](moduleStreamBase.html#music21.stream.base.Stream "music21.stream.base.Stream")[[source]](../_modules/music21/humdrum/spineParser.html#HumdrumSpine.moveElementsIntoMeasures)
:   Takes a parsed stream and moves the elements inside the
    measures. Works with pickup measures, etc. Does not
    automatically create ties, etc.

    Why not just use Stream.makeMeasures()? because
    humdrum measures contain extra information about barlines
    etc. and pickups are explicitly defined.

    ```python
    >>> s1 = stream.Stream()
    >>> s1.append(meter.TimeSignature('2/4'))
    >>> m1 = stream.Measure()
    >>> m1.number = 1
    >>> s1.append(m1)
    >>> s1.append(note.Note('C4', type='quarter'))
    >>> m2 = stream.Measure()
    >>> m2.number = 2
    >>> s1.append(m2)
    >>> s1.append(note.Note('D4', type='half'))
    >>> s1.show('text')
    {0.0} <music21.stream.Measure 1 offset=0.0>

    {0.0} <music21.meter.TimeSignature 2/4>
    {0.0} <music21.note.Note C>
    {1.0} <music21.stream.Measure 2 offset=1.0>

    {1.0} <music21.note.Note D>
    ```

    ```python
    >>> hds = humdrum.spineParser.HumdrumSpine()
    >>> s2 = hds.moveElementsIntoMeasures(s1)
    >>> s2.show('text')
    {0.0} <music21.stream.Measure 1 offset=0.0>
        {0.0} <music21.meter.TimeSignature 2/4>
        {0.0} <music21.note.Note C>
    {1.0} <music21.stream.Measure 2 offset=1.0>
        {0.0} <music21.note.Note D>
    ```

    The first measure is correctly identified as a pickup!

    ```python
    >>> s2.measure(1).paddingLeft
    1.0
    ```

HumdrumSpine.parse() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/humdrum/spineParser.html#HumdrumSpine.parse)
:   Dummy method that pushes all these objects to HumdrumSpine.stream
    as ElementWrappers. Should be overridden in
    specific Spine subclasses.

## KernSpine

class music21.humdrum.spineParser.KernSpine(*spineId: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*, *eventList: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[SpineEvent](#music21.humdrum.spineParser.SpineEvent "music21.humdrum.spineParser.SpineEvent")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *streamClass: [type](moduleBar.html#music21.bar.Barline.type "music21.bar.Barline.type")[[Stream](moduleStreamBase.html#music21.stream.base.Stream "music21.stream.base.Stream")] = <class 'music21.stream.base.Stream'>*, *parentSpineCollection: [SpineCollection](#music21.humdrum.spineParser.SpineCollection "music21.humdrum.spineParser.SpineCollection") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](../_modules/music21/humdrum/spineParser.html#KernSpine)
:   A KernSpine is a type of humdrum spine with the \*\*kern
    attribute set and thus events are processed as if they
    are kern notes.

    Instances are not constructed directly; reclassSpines reassigns
    \_\_class\_\_ from HumdrumSpine to KernSpine once the spine’s
    exclusive interpretation is known. All KernSpine-specific state
    is initialized at the top of parse().

    * Changed in v10: currentTupletDuration / desiredTupletDuration
      :   renamed to currentTupletQL / desiredTupletQL.

[`KernSpine`](#music21.humdrum.spineParser.KernSpine "music21.humdrum.spineParser.KernSpine") bases

* [`HumdrumSpine`](#music21.humdrum.spineParser.HumdrumSpine "music21.humdrum.spineParser.HumdrumSpine")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`KernSpine`](#music21.humdrum.spineParser.KernSpine "music21.humdrum.spineParser.KernSpine") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`KernSpine`](#music21.humdrum.spineParser.KernSpine "music21.humdrum.spineParser.KernSpine") read/write properties

Read/write properties inherited from [`HumdrumSpine`](#music21.humdrum.spineParser.HumdrumSpine "music21.humdrum.spineParser.HumdrumSpine"):

|  |  |  |
| --- | --- | --- |
| * [`spineType`](#music21.humdrum.spineParser.HumdrumSpine.spineType "music21.humdrum.spineParser.HumdrumSpine.spineType") |  |  |

[`KernSpine`](#music21.humdrum.spineParser.KernSpine "music21.humdrum.spineParser.KernSpine") methods

KernSpine.parse() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/humdrum/spineParser.html#KernSpine.parse)
:   Dummy method that pushes all these objects to HumdrumSpine.stream
    as ElementWrappers. Should be overridden in
    specific Spine subclasses.

KernSpine.processChordEvent(*eventC: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [Chord](moduleChord.html#music21.chord.Chord "music21.chord.Chord")[[source]](../_modules/music21/humdrum/spineParser.html#KernSpine.processChordEvent)
:   Process a single chord event

    Like processNoteEvent, stores information about current beam and tuplet state.

KernSpine.processNoteEvent(*eventC: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [GeneralNote](moduleNote.html#music21.note.GeneralNote "music21.note.GeneralNote")[[source]](../_modules/music21/humdrum/spineParser.html#KernSpine.processNoteEvent)
:   similar to hdStringToNote, this method processes a string representing a single
    note, but stores information about current beam and tuplet state.

KernSpine.setBeamsForNote(*n: [GeneralNote](moduleNote.html#music21.note.GeneralNote "music21.note.GeneralNote")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/humdrum/spineParser.html#KernSpine.setBeamsForNote)
:   sets the beams for a Note (or Chord) given self.currentBeamNumbers
    and updates self.currentBeamNumbers based on stop beams.

    Safe enough to use on elements such as rests that don’t have beam info.

KernSpine.setTupletTypeForNote(*n: [GeneralNote](moduleNote.html#music21.note.GeneralNote "music21.note.GeneralNote")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/humdrum/spineParser.html#KernSpine.setTupletTypeForNote)

Methods inherited from [`HumdrumSpine`](#music21.humdrum.spineParser.HumdrumSpine "music21.humdrum.spineParser.HumdrumSpine"):

|  |  |  |
| --- | --- | --- |
| * [`append()`](#music21.humdrum.spineParser.HumdrumSpine.append "music21.humdrum.spineParser.HumdrumSpine.append") | * [`moveElementsIntoMeasures()`](#music21.humdrum.spineParser.HumdrumSpine.moveElementsIntoMeasures "music21.humdrum.spineParser.HumdrumSpine.moveElementsIntoMeasures") |  |

## MiscTandem

class music21.humdrum.spineParser.MiscTandem(*tandem: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*, *\*\*keywords*)[[source]](../_modules/music21/humdrum/spineParser.html#MiscTandem)

[`MiscTandem`](#music21.humdrum.spineParser.MiscTandem "music21.humdrum.spineParser.MiscTandem") bases

* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`MiscTandem`](#music21.humdrum.spineParser.MiscTandem "music21.humdrum.spineParser.MiscTandem") read-only properties

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`MiscTandem`](#music21.humdrum.spineParser.MiscTandem "music21.humdrum.spineParser.MiscTandem") read/write properties

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`MiscTandem`](#music21.humdrum.spineParser.MiscTandem "music21.humdrum.spineParser.MiscTandem") methods

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`MiscTandem`](#music21.humdrum.spineParser.MiscTandem "music21.humdrum.spineParser.MiscTandem") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## ProtoSpine

class music21.humdrum.spineParser.ProtoSpine(*eventList: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[SpineEvent](#music21.humdrum.spineParser.SpineEvent "music21.humdrum.spineParser.SpineEvent") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](../_modules/music21/humdrum/spineParser.html#ProtoSpine)
:   A ProtoSpine is a collection of events arranged vertically.
    It differs from a HumdrumSpine in that spine paths are not followed.
    So ProtoSpine(1) would be everything in the 2nd column
    of a Humdrum file regardless of whether the 2nd column
    was at some point an independent Spine
    or if it later became a split from the first spine.

    See `parseProtoSpinesAndEventCollections()`
    for more details on how ProtoSpine objects are created.

    * Changed in v10: ProtoSpines now iterate over their eventLists and are ProtoM21Objects

[`ProtoSpine`](#music21.humdrum.spineParser.ProtoSpine "music21.humdrum.spineParser.ProtoSpine") bases

* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`ProtoSpine`](#music21.humdrum.spineParser.ProtoSpine "music21.humdrum.spineParser.ProtoSpine") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

## SpineCollection

class music21.humdrum.spineParser.SpineCollection[[source]](../_modules/music21/humdrum/spineParser.html#SpineCollection)
:   A SpineCollection is a set of HumdrumSpines with relationships to each
    other and where their position attributes indicate
    simultaneous onsets.

    When you iterate over a SpineCollection, it goes from right to
    left, since that’s the order that humdrum expects.

[`SpineCollection`](#music21.humdrum.spineParser.SpineCollection "music21.humdrum.spineParser.SpineCollection") bases

* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`SpineCollection`](#music21.humdrum.spineParser.SpineCollection "music21.humdrum.spineParser.SpineCollection") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`SpineCollection`](#music21.humdrum.spineParser.SpineCollection "music21.humdrum.spineParser.SpineCollection") methods

SpineCollection.addSpine(*streamClass: [type](moduleBar.html#music21.bar.Barline.type "music21.bar.Barline.type")[[Stream](moduleStreamBase.html#music21.stream.base.Stream "music21.stream.base.Stream")] = <class 'music21.stream.base.Part'>*) → [HumdrumSpine](#music21.humdrum.spineParser.HumdrumSpine "music21.humdrum.spineParser.HumdrumSpine")[[source]](../_modules/music21/humdrum/spineParser.html#SpineCollection.addSpine)
:   creates a new spine in the collection and returns it.

    By default, the underlying music21 class of the spine is
    `Part`. This can be overridden
    by passing in a different streamClass.

    Automatically sets the id of the Spine.

    ```python
    >>> hsc = humdrum.spineParser.SpineCollection()
    >>> newSpine = hsc.addSpine()
    >>> newSpine.id
    0
    >>> newSpine.stream
    <music21.stream.Part ...>
    >>> newSpine2 = hsc.addSpine(streamClass=stream.Stream)
    >>> newSpine2.id
    1
    >>> newSpine2
    <music21.humdrum.spineParser.HumdrumSpine: 1>
    >>> newSpine2.stream
    <music21.stream.Stream ...>
    ```

SpineCollection.appendSpine(*spine: [HumdrumSpine](#music21.humdrum.spineParser.HumdrumSpine "music21.humdrum.spineParser.HumdrumSpine")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/humdrum/spineParser.html#SpineCollection.appendSpine)
:   appendSpine(spine) – appends an already existing HumdrumSpine
    to the SpineCollection. Returns void

SpineCollection.assignIds() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/humdrum/spineParser.html#SpineCollection.assignIds)
:   Assign an ID based on the instrument, or just a string of a number
    if there is no instrument.

    ```python
    >>> hsc = humdrum.spineParser.SpineCollection()
    >>> newSpineDefault = hsc.addSpine()
    >>> newSpineDefault2 = hsc.addSpine()
    >>> newSpineOboe1 = hsc.addSpine()
    >>> newSpineOboe2 = hsc.addSpine()
    >>> newSpineTrumpet = hsc.addSpine()
    >>> newSpineOboe1.stream.append(instrument.Oboe())
    >>> newSpineOboe2.stream.append(instrument.Oboe())
    >>> newSpineTrumpet.stream.append(instrument.Trumpet())
    >>> hsc.assignIds()
    >>> for sp in hsc.spines:
    ...     print(sp.stream.id)
    1
    2
    Oboe-1
    Oboe-2
    Trumpet
    ```

SpineCollection.attachNonKernEvents() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/humdrum/spineParser.html#SpineCollection.attachNonKernEvents)
:   move `**dynam` and `**lyrics/**text` information to the appropriate staff.

    Assumes that `*staff` is consistent through the spine.

    TODO: misaligned events (a \*\*dynam or \*\*harm whose source line has ‘.’
    in the kern column) are silently dropped because the matcher only accepts
    exact `el.priority == event.lineNumber`. Desired: when no kern note
    sits on the same line, attach to the stream at the offset of the most
    recently-sounding kern note (ideal: between current and next note’s
    offsets). Lyrics/text continue to attach to notes only.
    See humdrum.tests.Test.testDynamAttachedMisaligned /
    testHarmAttachedMisaligned.

SpineCollection.createMusic21Streams() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/humdrum/spineParser.html#SpineCollection.createMusic21Streams)
:   Create Music21 Stream objects from spineCollections by running:

    > self.reclassSpines()
    > self.parseMusic21()
    > self.performInsertions()
    > self.moveObjectsToMeasures()
    > self.attachNonKernEvents()
    > self.makeVoices()
    > self.assignIds()

SpineCollection.getOffsetsAndPrioritiesByLineNumber() → [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [Fraction](https://docs.python.org/3/library/fractions.html#fractions.Fraction "(in Python v3.14)"), [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")]]][[source]](../_modules/music21/humdrum/spineParser.html#SpineCollection.getOffsetsAndPrioritiesByLineNumber)
:   Iterates through the spines by location
    and records the offset and priority for each element in the spines.

    Returns a dictionary keyed by humdrum line number whose values are
    two-element tuples: (music21 offset, list of Music21Objects at that line).

SpineCollection.getSpineById(*spineId: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [HumdrumSpine](#music21.humdrum.spineParser.HumdrumSpine "music21.humdrum.spineParser.HumdrumSpine")[[source]](../_modules/music21/humdrum/spineParser.html#SpineCollection.getSpineById)
:   returns the HumdrumSpine with the given id.

    raises a HumdrumException if the spine with a given id is not found

SpineCollection.makeVoices() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/humdrum/spineParser.html#SpineCollection.makeVoices)
:   make voices for each kernSpine – why not just run
    stream.makeVoices() ? because we have more information
    here that lets us make voices more intelligently

    Should be done after measures have been made.

SpineCollection.moveObjectsToMeasures() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/humdrum/spineParser.html#SpineCollection.moveObjectsToMeasures)
:   run moveElementsIntoMeasures for each HumdrumSpine
    that is not a sub-spine.

    Also fixes up the tuplets using duration.TupletFixer

SpineCollection.parseMusic21() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/humdrum/spineParser.html#SpineCollection.parseMusic21)
:   runs spine.parse() for each Spine.
    thus populating the spine.stream for each Spine

SpineCollection.performInsertions() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/humdrum/spineParser.html#SpineCollection.performInsertions)
:   Take a parsed spineCollection as Music21Objects and take
    sub-spines and put them in their proper location.

SpineCollection.performSpineInsertion(*thisSpine: [HumdrumSpine](#music21.humdrum.spineParser.HumdrumSpine "music21.humdrum.spineParser.HumdrumSpine")*, *newStream: [Stream](moduleStreamBase.html#music21.stream.base.Stream "music21.stream.base.Stream")*, *insertionPoint: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/humdrum/spineParser.html#SpineCollection.performSpineInsertion)
:   Insert all the spines into newStream that should be
    inserted into thisSpine at insertionPoint.

SpineCollection.reclassSpines() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/humdrum/spineParser.html#SpineCollection.reclassSpines)
:   Changes the classes of HumdrumSpines to more specific types
    (KernSpine, DynamicSpine)
    according to their spineType (e.g., \*\*kern, \*\*dynam)

SpineCollection.removeSpineById(*spineId: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/humdrum/spineParser.html#SpineCollection.removeSpineById)
:   Deletes a spine from the SpineCollection (after inserting, integrating, etc.)

    ```python
    >>> hsc = humdrum.spineParser.SpineCollection()
    >>> newSpine = hsc.addSpine()
    >>> newSpine.id
    0
    >>> newSpine2 = hsc.addSpine()
    >>> newSpine2.id
    1
    >>> hsc.spines
    [<music21.humdrum.spineParser.HumdrumSpine: 0>,
     <music21.humdrum.spineParser.HumdrumSpine: 1>]
    >>> hsc.removeSpineById(newSpine.id)
    >>> hsc.spines
    [<music21.humdrum.spineParser.HumdrumSpine: 1>]
    ```

    raises a HumdrumException if the spine with a given id is not found

## SpineComment

class music21.humdrum.spineParser.SpineComment(*comment: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*, *\*\*keywords*)[[source]](../_modules/music21/humdrum/spineParser.html#SpineComment)
:   A Music21Object that represents a comment in a single spine.

    ```python
    >>> sc = humdrum.spineParser.SpineComment('! this is a spine comment')
    >>> sc
    <music21.humdrum.spineParser.SpineComment 'this is a spine comment'>
    >>> sc.comment
    'this is a spine comment'
    ```

[`SpineComment`](#music21.humdrum.spineParser.SpineComment "music21.humdrum.spineParser.SpineComment") bases

* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`SpineComment`](#music21.humdrum.spineParser.SpineComment "music21.humdrum.spineParser.SpineComment") read-only properties

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`SpineComment`](#music21.humdrum.spineParser.SpineComment "music21.humdrum.spineParser.SpineComment") read/write properties

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`SpineComment`](#music21.humdrum.spineParser.SpineComment "music21.humdrum.spineParser.SpineComment") methods

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`SpineComment`](#music21.humdrum.spineParser.SpineComment "music21.humdrum.spineParser.SpineComment") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## SpineEvent

class music21.humdrum.spineParser.SpineEvent(*contents: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*, *lineNumber: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*)[[source]](../_modules/music21/humdrum/spineParser.html#SpineEvent)
:   A SpineEvent is an event in a HumdrumSpine or ProtoSpine.

    It’s .contents property contains the contents of the spine, or
    it could be ‘.’, in which case it means that a
    particular event appears after the last event in a different spine.
    It could also be “None” indicating that there is no event at all
    at this moment in the humdrum file. Happens if no ProtoSpine exists
    at this point in the file in this tab position.

    Should be initialized with its contents and 1-based source line number.

    These attributes are optional but likely to be very helpful:

    ```python
    lineNumber -- 1-based source line number in the humdrum file
    protoSpineId -- ProtoSpine id (0 to N)
    spineId -- id of HumdrumSpine actually attached to (after SpinePaths are parsed)
    ```

    The toNote() method converts the contents into a music21 note as
    if it’s kern – useful to have in all spine types.

    ```python
    >>> se1 = humdrum.spineParser.SpineEvent('EEE-8')
    >>> se1.lineNumber = 40
    >>> se1.contents
    'EEE-8'
    >>> se1
    <music21.humdrum.spineParser.SpineEvent EEE-8>
    >>> n = se1.toNote()
    >>> n
    <music21.note.Note E->
    ```

[`SpineEvent`](#music21.humdrum.spineParser.SpineEvent "music21.humdrum.spineParser.SpineEvent") bases

* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`SpineEvent`](#music21.humdrum.spineParser.SpineEvent "music21.humdrum.spineParser.SpineEvent") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`SpineEvent`](#music21.humdrum.spineParser.SpineEvent "music21.humdrum.spineParser.SpineEvent") methods

SpineEvent.toNote(*convertString: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [GeneralNote](moduleNote.html#music21.note.GeneralNote "music21.note.GeneralNote")[[source]](../_modules/music21/humdrum/spineParser.html#SpineEvent.toNote)
:   parse the object as a \*\*kern note and return a
    [`Note`](moduleNote.html#music21.note.Note "music21.note.Note") object (or Rest, or Chord)

    ```python
    >>> se = humdrum.spineParser.SpineEvent('DD#4')
    >>> n = se.toNote()
    >>> n
    <music21.note.Note D#>
    >>> n.octave
    2
    >>> n.duration.type
    'quarter'
    ```

## SpineLine

class music21.humdrum.spineParser.SpineLine(*lineNumber: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*, *contents: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*)[[source]](../_modules/music21/humdrum/spineParser.html#SpineLine)
:   A SpineLine is any horizontal line of a Humdrum file that
    contains one or more spine elements (separated by tabs)
    and not Global elements.

    Takes in a 1-based line number in the file and a string of contents.

    ```python
    >>> hsl = humdrum.spineParser.SpineLine(
    ...         lineNumber=7, contents='C4\t!local comment\t*M[4/4]\t.\n')
    >>> hsl
    <music21.humdrum.spineParser.SpineLine line 7 (4 spines)>
    >>> hsl.lineNumber
    7
    >>> hsl.numSpines
    4
    >>> hsl.spineData
    ['C4', '!local comment', '*M[4/4]', '.']
    ```

[`SpineLine`](#music21.humdrum.spineParser.SpineLine "music21.humdrum.spineParser.SpineLine") bases

* [`HumdrumLine`](#music21.humdrum.spineParser.HumdrumLine "music21.humdrum.spineParser.HumdrumLine")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`SpineLine`](#music21.humdrum.spineParser.SpineLine "music21.humdrum.spineParser.SpineLine") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

## Functions

music21.humdrum.spineParser.hdStringToMeasure(*contents: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *previousMeasure: [Measure](moduleStreamBase.html#music21.stream.base.Measure "music21.stream.base.Measure") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [Measure](moduleStreamBase.html#music21.stream.base.Measure "music21.stream.base.Measure")[[source]](../_modules/music21/humdrum/spineParser.html#hdStringToMeasure)
:   kern uses an equals sign followed by processing instructions to
    create new measures.

    Changed in v10: repeat dots are encoded as [`Repeat`](moduleBar.html#music21.bar.Repeat "music21.bar.Repeat")
    objects instead of being stuffed into a non-existent `Barline.repeatDots`
    attribute. `:|:` now produces an end-Repeat on the previous measure’s
    right barline AND a start-Repeat on the new measure’s left barline.

music21.humdrum.spineParser.hdStringToNote(*contents: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [GeneralNote](moduleNote.html#music21.note.GeneralNote "music21.note.GeneralNote")[[source]](../_modules/music21/humdrum/spineParser.html#hdStringToNote)
:   returns a [`Note`](moduleNote.html#music21.note.Note "music21.note.Note") (or Rest or Unpitched, etc.)
    matching the current SpineEvent.
    Does not check to see that it is sane or part of a `**kern` spine, etc.

    New rhythmic extensions formerly defined in
    wiki.humdrum.org/index.php/Rational\_rhythms
    and now at <https://extras.humdrum.org/man/rscale/>
    are fully implemented:

    ```python
    >>> n = humdrum.spineParser.hdStringToNote('CC3%2')
    >>> n.duration.quarterLength
    Fraction(8, 3)
    >>> n.duration.fullName
    'Whole Triplet (2 2/3 QL)'
    ```

    ```python
    >>> n = humdrum.spineParser.hdStringToNote('e-00.')
    >>> n.pitch
    <music21.pitch.Pitch E-4>
    >>> n.duration.quarterLength
    24.0
    >>> n.duration.fullName
    'Perfect Longa'
    ```

    ```python
    >>> n = humdrum.spineParser.hdStringToNote('F#000')
    >>> n.duration.quarterLength
    32.0
    >>> n.duration.fullName
    'Imperfect Maxima'
    ```

    Note that the following example is interpreted as one note in the time of a
    double-dotted quarter not a double-dotted quarter-note triplet.

    I believe that the latter definition, though used in
    <https://kern.humdrum.org/cgi-bin/ksdata?l=musedata/mozart/quartet&file=k421-01.krn&f=kern>
    and the Josquin Research Project [JRP] is incorrect, seeing as it
    contradicts the specification in
    <https://web.archive.org/web/20100203144730/http://www.music-cog.ohio-state.edu/Humdrum/representations/kern.html#N-Tuplets>

    This is the default:

    ```python
    >>> humdrum.spineParser.flavors['JRP'] = False
    ```

    ```python
    >>> n = humdrum.spineParser.hdStringToNote('6..fff')
    >>> n.duration.quarterLength
    Fraction(7, 6)
    ```

    ```python
    >>> n.duration.dots
    0
    ```

    ```python
    >>> n.duration.tuplets[0].durationNormal.dots
    2
    ```

    If you want the JRP definition, set humdrum.spineParser.flavors[‘JRP’] = True
    before calling converter.parse() or anything like that:

    ```python
    >>> humdrum.spineParser.flavors['JRP'] = True
    >>> n = humdrum.spineParser.hdStringToNote('6..fff')
    >>> n.duration.quarterLength
    Fraction(7, 6)
    >>> n.duration.dots
    2
    >>> n.duration.tuplets[0].durationNormal.dots
    0
    ```

    ```python
    >>> n = humdrum.spineParser.hdStringToNote('gg#q/LL')
    >>> n.duration
    <music21.duration.GraceDuration unlinked type:eighth quarterLength:0.0>
    >>> n.duration.isGrace
    True
    ```

music21.humdrum.spineParser.kernTandemToObject(*tandem: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/humdrum/spineParser.html#kernTandemToObject)
:   Kern uses symbols such as `*M5/4` and `*clefG2`, etc., to control processing

    This method converts them to music21 objects.

    ```python
    >>> m = humdrum.spineParser.kernTandemToObject('*M3/1')
    >>> m
    <music21.meter.TimeSignature 3/1>
    ```

    Unknown objects are converted to MiscTandem objects:

    ```python
    >>> m2 = humdrum.spineParser.kernTandemToObject('*TandyUnk')
    >>> m2
    <music21.humdrum.spineParser.MiscTandem *TandyUnk>
    ```
