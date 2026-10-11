Source: https://music21.org/music21docs/moduleReference/moduleSearchBase.html

# music21.search.base

base classes for searching scores.

See User’s Guide, Chapter 43: Searching in and Among Scores for details.

## SearchMatch

class music21.search.base.SearchMatch(*elStart*, *els*, *index*, *iterator*)[[source]](../_modules/music21/search/base.html#SearchMatch)
:   A lightweight object representing the match (if any) for a search. Derived from namedtuple

[`SearchMatch`](#music21.search.base.SearchMatch "music21.search.base.SearchMatch") bases

* [`SearchMatch`](#music21.search.base.SearchMatch "music21.search.base.SearchMatch")

[`SearchMatch`](#music21.search.base.SearchMatch "music21.search.base.SearchMatch") instance variables

SearchMatch.elStart
:   The first element that matches the list.

SearchMatch.els
:   A tuple of all the matching elements.

SearchMatch.index
:   The index in the iterator at which the first element can be found

SearchMatch.iterator
:   The iterator which produced these elements.

## StreamSearcher

class music21.search.base.StreamSearcher(*streamSearch: [Stream](moduleStreamBase.html#music21.stream.base.Stream "music21.stream.base.Stream")*, *searchList: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")]*)[[source]](../_modules/music21/search/base.html#StreamSearcher)
:   An object that can search through streams for a set of elements
    or notes or something of that sort.

    Create a basic Stream first:

    ```python
    >>> thisStream = converter.parse('tinynotation: 3/4 c4. d8 e4 g4. a8 f4. c4. d4')
    >>> thisStream.show('text')
    {0.0} <music21.stream.Measure 1 offset=0.0>
        {0.0} <music21.clef.TrebleClef>
        {0.0} <music21.meter.TimeSignature 3/4>
        {0.0} <music21.note.Note C>
        {1.5} <music21.note.Note D>
        {2.0} <music21.note.Note E>
    {3.0} <music21.stream.Measure 2 offset=3.0>
        {0.0} <music21.note.Note G>
        {1.5} <music21.note.Note A>
        {2.0} <music21.note.Note F>
    {6.0} <music21.stream.Measure 3 offset=6.0>
        {0.5} <music21.note.Note C>
        {2.0} <music21.note.Note D>
        {3.0} <music21.bar.Barline type=final>
    ```

    Let’s create something to search for:

    ```python
    >>> c = note.Note('C', quarterLength=1.5)
    >>> d = note.Note('D', quarterLength=0.5)
    >>> searchList = [c, d]
    ```

    Now create a StreamSearcher:

    ```python
    >>> ss = search.StreamSearcher(thisStream, searchList)
    ```

    searchList could also be a Stream in itself.

    Let’s configure it for recursive search and to filter so only notes are there:

    ```python
    >>> ss.recurse = True
    >>> ss.filterNotes = True  # or `.filterNotesAndRests`
    ```

    Alternatively, we could have passed in a StreamIterator instead of thisStream.

    Now let’s configure the algorithms:

    ```python
    >>> ss.algorithms
    [<function StreamSearcher.wildcardAlgorithm at 0x111b6e340>]
    ```

    Wildcard search is a default algorithm that lets you use wildcards.
    I suggest you leave it in place and add to the algorithms list. We can add the
    rhythmAlgorithm to it:

    ```python
    >>> ss.algorithms.append(search.StreamSearcher.rhythmAlgorithm)
    >>> ss.algorithms
    [<function StreamSearcher.wildcardAlgorithm at 0x111b6e340>,
     <function StreamSearcher.rhythmAlgorithm at 0x11200000>]
    ```

    Now run it:

    ```python
    >>> results = ss.run()
    >>> results
    [SearchMatch(elStart=<music21.note.Note C>, els=len(2), index=0, iterator=[...]),
     SearchMatch(elStart=<music21.note.Note G>, els=len(2), index=3, iterator=[...])]
    ```

    ```python
    >>> results[0].elStart.measureNumber
    1
    >>> results[1].elStart.measureNumber
    2
    ```

    Wildcards can be useful:

    ```python
    >>> searchStream2 = stream.Stream()
    >>> searchStream2.append(note.Note(quarterLength=0.5))
    >>> searchStream2.append(search.Wildcard())
    >>> searchStream2.append(note.Note(quarterLength=1.5))
    ```

    ```python
    >>> ss.searchList = searchStream2
    >>> results = ss.run()
    >>> results
    [SearchMatch(elStart=<music21.note.Note D>, els=len(3), index=1, iterator=[...]),
     SearchMatch(elStart=<music21.note.Note A>, els=len(3), index=4, iterator=[...])]
    >>> results[0].els
    (<music21.note.Note D>, <music21.note.Note E>, <music21.note.Note G>)
    >>> [n.duration.quarterLength for n in results[0].els]
    [0.5, 1.0, 1.5]
    ```

[`StreamSearcher`](#music21.search.base.StreamSearcher "music21.search.base.StreamSearcher") methods

StreamSearcher.noteNameAlgorithm(*streamEl: [Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")*, *searchEl: [Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")*)[[source]](../_modules/music21/search/base.html#StreamSearcher.noteNameAlgorithm)

StreamSearcher.rhythmAlgorithm(*streamEl: [Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")*, *searchEl: [Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")*)[[source]](../_modules/music21/search/base.html#StreamSearcher.rhythmAlgorithm)

StreamSearcher.run() → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[SearchMatch](#music21.search.base.SearchMatch "music21.search.base.SearchMatch")][[source]](../_modules/music21/search/base.html#StreamSearcher.run)

StreamSearcher.wildcardAlgorithm(*streamEl: [Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")*, *searchEl: [Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")*)[[source]](../_modules/music21/search/base.html#StreamSearcher.wildcardAlgorithm)
:   An algorithm that supports Wildcards – added by default to the search function.

## Wildcard

class music21.search.base.Wildcard(*\*\*keywords*)[[source]](../_modules/music21/search/base.html#Wildcard)
:   An object that may have some properties defined, but others not that
    matches a single object in a music21 stream. Equivalent to the
    regular expression “.”

    ```python
    >>> wc1 = search.Wildcard()
    >>> wc1.pitch = pitch.Pitch('C')
    >>> st1 = stream.Stream()
    >>> st1.append(note.Note('D', type='half'))
    >>> st1.append(wc1)
    ```

[`Wildcard`](#music21.search.base.Wildcard "music21.search.base.Wildcard") bases

* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`Wildcard`](#music21.search.base.Wildcard "music21.search.base.Wildcard") read-only properties

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`Wildcard`](#music21.search.base.Wildcard "music21.search.base.Wildcard") read/write properties

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`Wildcard`](#music21.search.base.Wildcard "music21.search.base.Wildcard") methods

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`Wildcard`](#music21.search.base.Wildcard "music21.search.base.Wildcard") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## WildcardDuration

class music21.search.base.WildcardDuration(*typeOrDuration: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | OffsetQLIn | [DurationTuple](moduleDuration.html#music21.duration.DurationTuple "music21.duration.DurationTuple") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, */*, *\**, *type: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *dots: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = 0*, *quarterLength: OffsetQLIn | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *durationTuple: [DurationTuple](moduleDuration.html#music21.duration.DurationTuple "music21.duration.DurationTuple") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *components: Iterable[[DurationTuple](moduleDuration.html#music21.duration.DurationTuple "music21.duration.DurationTuple")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *client: [base.Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\*\*keywords*)[[source]](../_modules/music21/search/base.html#WildcardDuration)
:   a wildcard duration (it might define a duration
    in itself, but the methods here will see that it
    is a wildcard of some sort)

    No difference from any other duration.

[`WildcardDuration`](#music21.search.base.WildcardDuration "music21.search.base.WildcardDuration") bases

* [`Duration`](moduleDuration.html#music21.duration.Duration "music21.duration.Duration")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")
* [`SlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.SlottedObjectMixin "music21.common.objects.SlottedObjectMixin")

[`WildcardDuration`](#music21.search.base.WildcardDuration "music21.search.base.WildcardDuration") read-only properties

Read-only properties inherited from [`Duration`](moduleDuration.html#music21.duration.Duration "music21.duration.Duration"):

|  |  |  |
| --- | --- | --- |
| * [`fullName`](moduleDuration.html#music21.duration.Duration.fullName "music21.duration.Duration.fullName") * [`isComplex`](moduleDuration.html#music21.duration.Duration.isComplex "music21.duration.Duration.isComplex") | * [`ordinal`](moduleDuration.html#music21.duration.Duration.ordinal "music21.duration.Duration.ordinal") | * [`quarterLengthNoTuplets`](moduleDuration.html#music21.duration.Duration.quarterLengthNoTuplets "music21.duration.Duration.quarterLengthNoTuplets") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`WildcardDuration`](#music21.search.base.WildcardDuration "music21.search.base.WildcardDuration") read/write properties

Read/write properties inherited from [`Duration`](moduleDuration.html#music21.duration.Duration "music21.duration.Duration"):

|  |  |  |
| --- | --- | --- |
| * [`components`](moduleDuration.html#music21.duration.Duration.components "music21.duration.Duration.components") * [`dotGroups`](moduleDuration.html#music21.duration.Duration.dotGroups "music21.duration.Duration.dotGroups") * [`dots`](moduleDuration.html#music21.duration.Duration.dots "music21.duration.Duration.dots") | * [`linked`](moduleDuration.html#music21.duration.Duration.linked "music21.duration.Duration.linked") * [`quarterLength`](moduleDuration.html#music21.duration.Duration.quarterLength "music21.duration.Duration.quarterLength") | * [`tuplets`](moduleDuration.html#music21.duration.Duration.tuplets "music21.duration.Duration.tuplets") * [`type`](moduleDuration.html#music21.duration.Duration.type "music21.duration.Duration.type") |

[`WildcardDuration`](#music21.search.base.WildcardDuration "music21.search.base.WildcardDuration") methods

Methods inherited from [`Duration`](moduleDuration.html#music21.duration.Duration "music21.duration.Duration"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleDuration.html#music21.duration.Duration.__eq__ "music21.duration.Duration.__eq__") * [`addDurationTuple()`](moduleDuration.html#music21.duration.Duration.addDurationTuple "music21.duration.Duration.addDurationTuple") * [`aggregateTupletMultiplier()`](moduleDuration.html#music21.duration.Duration.aggregateTupletMultiplier "music21.duration.Duration.aggregateTupletMultiplier") * [`appendTuplet()`](moduleDuration.html#music21.duration.Duration.appendTuplet "music21.duration.Duration.appendTuplet") * [`augmentOrDiminish()`](moduleDuration.html#music21.duration.Duration.augmentOrDiminish "music21.duration.Duration.augmentOrDiminish") | * [`clear()`](moduleDuration.html#music21.duration.Duration.clear "music21.duration.Duration.clear") * [`componentIndexAtQtrPosition()`](moduleDuration.html#music21.duration.Duration.componentIndexAtQtrPosition "music21.duration.Duration.componentIndexAtQtrPosition") * [`componentStartTime()`](moduleDuration.html#music21.duration.Duration.componentStartTime "music21.duration.Duration.componentStartTime") * [`consolidate()`](moduleDuration.html#music21.duration.Duration.consolidate "music21.duration.Duration.consolidate") * [`currentComponents()`](moduleDuration.html#music21.duration.Duration.currentComponents "music21.duration.Duration.currentComponents") | * [`getGraceDuration()`](moduleDuration.html#music21.duration.Duration.getGraceDuration "music21.duration.Duration.getGraceDuration") * [`informClient()`](moduleDuration.html#music21.duration.Duration.informClient "music21.duration.Duration.informClient") * [`sliceComponentAtPosition()`](moduleDuration.html#music21.duration.Duration.sliceComponentAtPosition "music21.duration.Duration.sliceComponentAtPosition") * [`splitDotGroups()`](moduleDuration.html#music21.duration.Duration.splitDotGroups "music21.duration.Duration.splitDotGroups") |

[`WildcardDuration`](#music21.search.base.WildcardDuration "music21.search.base.WildcardDuration") instance variables

Instance variables inherited from [`Duration`](moduleDuration.html#music21.duration.Duration "music21.duration.Duration"):

|  |  |  |
| --- | --- | --- |
| * [`client`](moduleDuration.html#music21.duration.Duration.client "music21.duration.Duration.client") | * [`expressionIsInferred`](moduleDuration.html#music21.duration.Duration.expressionIsInferred "music21.duration.Duration.expressionIsInferred") |  |

## Functions

music21.search.base.approximateNoteSearch(*thisStream*, *otherStreams*)[[source]](../_modules/music21/search/base.html#approximateNoteSearch)
:   searches the list of otherStreams and returns an ordered list of matches
    (each stream will have a new property of matchProbability to show how
    well it matches)

    ```python
    >>> s = converter.parse("tinynotation: 4/4 c4 d8 e16 FF a'4 b-")
    >>> o1 = converter.parse("tinynotation: 4/4 c4 d8 e GG a' b-4")
    >>> o1.id = 'o1'
    >>> o2 = converter.parse("tinynotation: 4/4 d#2 f A a' G b")
    >>> o2.id = 'o2'
    >>> o3 = converter.parse("tinynotation: 4/4 c8 d16 e32 FF32 a'8 b-8")
    >>> o3.id = 'o3'
    >>> l = search.approximateNoteSearch(s, [o1, o2, o3])
    >>> for i in l:
    ...     print(f'{i.id} {i.matchProbability!r}')
    o1 0.666666...
    o3 0.333333...
    o2 0.083333...
    ```

music21.search.base.approximateNoteSearchNoRhythm(*thisStream*, *otherStreams*)[[source]](../_modules/music21/search/base.html#approximateNoteSearchNoRhythm)
:   searches the list of otherStreams and returns an ordered list of matches
    (each stream will have a new property of matchProbability to show how
    well it matches)

    ```python
    >>> s = converter.parse("tinynotation: 4/4 c4 d8 e16 FF a'4 b-")
    >>> o1 = converter.parse("tinynotation: 4/4 c4 d8 e GG a' b-4")
    >>> o1.id = 'o1'
    >>> o2 = converter.parse("tinynotation: 4/4 d#2 f A a' G b")
    >>> o2.id = 'o2'
    >>> o3 = converter.parse("tinynotation: 4/4 c4 d e GG CCC r")
    >>> o3.id = 'o3'
    >>> l = search.approximateNoteSearchNoRhythm(s, [o1, o2, o3])
    >>> for i in l:
    ...     print(f'{i.id} {i.matchProbability!r}')
    o1 0.83333333...
    o3 0.5
    o2 0.1666666...
    ```

music21.search.base.approximateNoteSearchOnlyRhythm(*thisStream*, *otherStreams*)[[source]](../_modules/music21/search/base.html#approximateNoteSearchOnlyRhythm)
:   searches the list of otherStreams and returns an ordered list of matches
    (each stream will have a new property of matchProbability to show how
    well it matches)

    ```python
    >>> s = converter.parse("tinynotation: 4/4 c4 d8 e16 FF a'4 b-")
    >>> o1 = converter.parse("tinynotation: 4/4 c4 d8 e GG a' b-4")
    >>> o1.id = 'o1'
    >>> o2 = converter.parse("tinynotation: 4/4 d#2 f A a' G b")
    >>> o2.id = 'o2'
    >>> o3 = converter.parse("tinynotation: 4/4 c4 d e GG CCC r")
    >>> o3.id = 'o3'
    >>> l = search.approximateNoteSearchOnlyRhythm(s, [o1, o2, o3])
    >>> for i in l:
    ...     print(f'{i.id} {i.matchProbability!r}')
    o1 0.5
    o3 0.33...
    o2 0.0
    ```

music21.search.base.approximateNoteSearchWeighted(*thisStream*, *otherStreams*)[[source]](../_modules/music21/search/base.html#approximateNoteSearchWeighted)
:   searches the list of otherStreams and returns an ordered list of matches
    (each stream will have a new property of matchProbability to show how
    well it matches)

    ```python
    >>> s = converter.parse("tinynotation: 4/4 c4 d8 e16 FF a'4 b-")
    >>> o1 = converter.parse("tinynotation: 4/4 c4 d8 e GG2 a' b-4")
    >>> o1.id = 'o1'
    >>> o2 = converter.parse("tinynotation: 4/4 AAA4 AAA8 AAA16 AAA16 AAA4 AAA4")
    >>> o2.id = 'o2'
    >>> o3 = converter.parse("tinynotation: 4/4 c8 d16 e32 FF32 a'8 b-8")
    >>> o3.id = 'o3'
    >>> o4 = converter.parse("tinynotation: 4/4 c1 d1 e1 FF1 a'1 b-1")
    >>> o4.id = 'o4'
    >>> l = search.approximateNoteSearchWeighted(s, [o1, o2, o3, o4])
    >>> for i in l:
    ...     print(f'{i.id} {i.matchProbability!r}')
    o3 0.83333...
    o1 0.75
    o4 0.75
    o2 0.25
    ```

music21.search.base.mostCommonMeasureRhythms(*streamIn*, *transposeDiatonic=False*)[[source]](../_modules/music21/search/base.html#mostCommonMeasureRhythms)
:   returns a sorted list of dictionaries
    of the most common rhythms in a stream where
    each dictionary contains:

    number: the number of times a rhythm appears
    rhythm: the rhythm found (with the pitches of the first instance of the rhythm transposed to C5)
    measures: a list of measures containing the rhythm
    rhythmString: a string representation of the rhythm (see translateStreamToStringOnlyRhythm)

    ```python
    >>> bach = corpus.parse('bwv1.6')
    >>> sortedRhythms = search.mostCommonMeasureRhythms(bach)
    >>> for in_dict in sortedRhythms[0:3]:
    ...     number = in_dict['number']
    ...     rhythmString = in_dict['rhythmString']
    ...     measures = in_dict['measures']
    ...     print(
    ...         f'no: {number} '
    ...         f'rhythmString: {rhythmString}'
    ...     )
    ...     bars = [
    ...         (m.number, str(m.getContextByClass(stream.Part).id))
    ...         for m in measures
    ...     ]
    ...     print(f'bars: {bars!r}')
    ...     in_dict['rhythm'].show('text')
    ...     print('-----')
    no: 34 rhythmString: PPPP
    bars: [(1, 'Soprano'), (2, 'Soprano'), (3, 'Soprano'), ..., (1, 'Alto'), ..., (10, 'Bass')]
    {0.0} <music21.note.Note C>
    {1.0} <music21.note.Note A>
    {2.0} <music21.note.Note F>
    {3.0} <music21.note.Note C>
    -----
    no: 7 rhythmString: ZZ
    bars: [(13, 'Soprano'), (14, 'Soprano'), ..., (14, 'Bass')]
    {0.0} <music21.note.Note C>
    {2.0} <music21.note.Note A>
    -----
    no: 6 rhythmString: ZPP
    bars: [(6, 'Soprano'), (12, 'Soprano'), ..., (18, 'Tenor'), ... (12, 'Bass')]
    {0.0} <music21.note.Note C>
    {2.0} <music21.note.Note B->
    {3.0} <music21.note.Note B->
    -----
    ```

    * Changed in v7: bars are ordered first by number, then by part.

music21.search.base.noteNameRhythmicSearch(*thisStreamOrIterator*, *searchList*)[[source]](../_modules/music21/search/base.html#noteNameRhythmicSearch)
:   ```python
    >>> thisStream = converter.parse('tinynotation: 3/4 c4 d8 e c d e f c D E c c4 d# e')
    >>> searchList = [note.Note('C'), note.Note('D'), note.Note('E')]
    >>> for n in searchList:
    ...     n.duration.type = 'eighth'
    >>> thisStreamIter = thisStream.recurse().notes
    ```

    ```python
    >>> search.noteNameRhythmicSearch(thisStreamIter, searchList)
    [3, 7]
    ```

    ```python
    >>> searchList[0].duration = search.WildcardDuration()
    >>> search.noteNameRhythmicSearch(thisStreamIter, searchList)
    [0, 3, 7]
    ```

music21.search.base.noteNameSearch(*thisStreamOrIterator*, *searchList*)[[source]](../_modules/music21/search/base.html#noteNameSearch)
:   ```python
    >>> thisStream = converter.parse('tinynotation: 3/4 c4 d8 e c d e f c D E c c4 d# e')
    >>> searchList = [note.Note('C'), note.Note('D'), note.Note('E')]
    >>> thisStreamIter = thisStream.recurse().notes
    ```

    ```python
    >>> search.noteNameSearch(thisStreamIter, searchList)
    [0, 3, 7]
    >>> searchList2 = [note.Note('C'), search.Wildcard(), note.Note('E')]
    >>> search.noteNameSearch(thisStreamIter, searchList2)
    [0, 3, 7, 11]
    ```

music21.search.base.rhythmicSearch(*thisStreamOrIterator*, *searchList*)[[source]](../_modules/music21/search/base.html#rhythmicSearch)
:   Takes two streams – the first is the stream to be searched and the second
    is a stream of elements whose rhythms must match the first. Returns a list
    of indices which begin a successful search.

    searches are made based on quarterLength.
    thus a dotted sixteenth-note and a quadruplet (4:3) eighth
    will match each other.

    Example 1: First we will set up a simple stream for searching:

    ```python
    >>> thisStream = converter.parse('tinynotation: 3/4 c4. d8 e4 g4. a8 f4. c4. r4')
    >>> thisStream.show('text')
    {0.0} <music21.stream.Measure 1 offset=0.0>
        {0.0} <music21.clef.TrebleClef>
        {0.0} <music21.meter.TimeSignature 3/4>
        {0.0} <music21.note.Note C>
        {1.5} <music21.note.Note D>
        {2.0} <music21.note.Note E>
    {3.0} <music21.stream.Measure 2 offset=3.0>
        {0.0} <music21.note.Note G>
        {1.5} <music21.note.Note A>
        {2.0} <music21.note.Note F>
    {6.0} <music21.stream.Measure 3 offset=6.0>
        {0.5} <music21.note.Note C>
        {2.0} <music21.note.Rest quarter>
        {3.0} <music21.bar.Barline type=final>
    ```

    Now we will search for all dotted-quarter/eighth elements in the Stream:

    ```python
    >>> thisStreamIter = thisStream.recurse().notes
    ```

    ```python
    >>> searchStream1 = stream.Stream()
    >>> searchStream1.append(note.Note(quarterLength=1.5))
    >>> searchStream1.append(note.Note(quarterLength=0.5))
    ```

    ```python
    >>> l = search.rhythmicSearch(thisStreamIter, searchStream1)
    >>> l
    [0, 3]
    >>> stream.Stream(thisStreamIter[3:5]).show('text')
    {0.0} <music21.note.Note G>
    {1.5} <music21.note.Note A>
    ```

    Slightly more advanced search: we will look for any instances of eighth,
    followed by a note (or other element) of any length, followed by a dotted quarter
    note. Again, we will find two instances; this time we will tag them both with
    a TextExpression of “\*” and then show the original stream:

    ```python
    >>> searchStream2 = stream.Stream()
    >>> searchStream2.append(note.Note(quarterLength=0.5))
    >>> searchStream2.append(search.Wildcard())
    >>> searchStream2.append(note.Note(quarterLength=1.5))
    >>> l = search.rhythmicSearch(thisStreamIter, searchStream2)
    >>> l
    [1, 4]
    >>> for found in l:
    ...     thisStreamIter[found].lyric = '*'
    >>> thisStream.show()
    ```

    [![../_images/searchRhythmic1.png](../_images/searchRhythmic1.png)](../_images/searchRhythmic1.png)

    Now we can test the search on a real dataset and show the types
    of preparation that are needed to make it most likely a success.
    We will look through the first movement of Corelli Trio Sonata op. 3 no. 1 (F major)
    looking to see how much more common the first search term (dotted-quarter, eighth)
    is than the second (eighth, anything, dotted-quarter). In fact, my hypothesis
    was wrong, and the second term is actually more common than the first! (n.b. rests
    are being counted here as well as notes)

    ```python
    >>> grave = corpus.parse('corelli/opus3no1/1grave')
    >>> term1results = []
    >>> term2results = []
    >>> for p in grave.parts:
    ...    pf = p.flatten().stripTies().notesAndRests  # consider tied notes as one long note
    ...    temp1 = search.rhythmicSearch(pf, searchStream1)
    ...    temp2 = search.rhythmicSearch(pf, searchStream2)
    ...    for found in temp1:
    ...        term1results.append(found)
    ...    for found in temp2:
    ...        term2results.append(found)
    >>> term1results
    [0, 7, 13, 21, 42, 57, 64, 66, 0, 5, 7, 19, 21, 40, 46, 63, 0, 8, 31, 61, 69, 71, 73, 97]
    >>> term2results
    [5, 29, 95]
    >>> float(len(term1results)) / len(term2results)
    8.0
    ```

music21.search.base.streamSearchBase(*thisStreamOrIterator*, *searchList*, *algorithm=None*)[[source]](../_modules/music21/search/base.html#streamSearchBase)
:   A basic search function that is used by other search mechanisms,
    which takes in a stream or StreamIterator and a searchList or stream
    and an algorithm to run on each pair of elements to determine if they match.

music21.search.base.translateDiatonicStreamToString(*inputStreamOrIterator*, *returnMeasures=False*)[[source]](../_modules/music21/search/base.html#translateDiatonicStreamToString)
:   Translates a Stream or StreamIterator of Notes and Rests only into a string,
    encoding only the .step (no accidental or octave) and whether
    the note is slower, faster, or the same speed as the previous
    note.

    Skips all but the first note of tie. Skips multiple rests in a row

    Each note gets one byte:

    A-G = note of same length as previous
    H-N = note of longer length than previous
    O-U = note of shorter length than previous
    Z = rest

    ```python
    >>> s = converter.parse("tinynotation: 3/4 c4 d8~ d16 r16 FF8 F#8 a'8 b-2.")
    >>> streamString = search.translateDiatonicStreamToString(s.recurse().notesAndRests)
    >>> print(streamString)
    CRZFFAI
    >>> len(streamString)
    7
    ```

    If returnMeasures is True, returns an array of measureNumbers where each entry represents
    the measure number of the measure of the object at that character position :

    ```python
    >>> streamString2, measures = search.translateDiatonicStreamToString(s.recurse().notesAndRests,
    ...                                    returnMeasures=True)
    >>> streamString == streamString2
    True
    >>> measures
    [1, 1, 1, 1, 1, 2, 2]
    ```

music21.search.base.translateDurationToBytes(*n: [GeneralNote](moduleNote.html#music21.note.GeneralNote "music21.note.GeneralNote")*)[[source]](../_modules/music21/search/base.html#translateDurationToBytes)
:   takes a note.Note object and translates it to a two-byte representation

    currently returns the chr() for the note’s midi number. or chr(127) for rests
    followed by the log of the quarter length (fitted to 1-127, see formula below)

    ```python
    >>> n = note.Note('C4')
    >>> n.duration.quarterLength = 3  # dotted half
    >>> trans = search.translateDurationToBytes(n)
    >>> trans
    '_'
    >>> (2 ** (ord(trans[0]) / 10)) / 256  # approximately 3
    2.828...
    ```

music21.search.base.translateIntervalsAndSpeed(*inputStream*, *returnMeasures=False*)[[source]](../_modules/music21/search/base.html#translateIntervalsAndSpeed)
:   Translates a Stream (not StreamIterator) of Notes and Rests only into a string,
    encoding only the chromatic distance from the last note and whether
    the note is slower, faster, or the same speed as the previous
    note.

    Skips all but the first note of tie. Skips multiple rests in a row

    Each note gets one byte and encodes up from -13 to 13 (all notes > octave are 13 or -13)

    ```python
    >>> s = converter.parse("tinynotation: 3/4 c4 d8~ d16 r16 F8 F#8 F8 a'8 b-2")
    >>> sn = s.flatten().notesAndRests.stream()
    >>> streamString = search.translateIntervalsAndSpeed(sn)
    >>> print(streamString)
    Ib RHJ<9
    >>> print([ord(x) for x in streamString])
    [73, 98, 32, 82, 72, 74, 60, 57]
    >>> len(streamString)
    8
    ```

    If returnMeasures is True, returns a triplet of whether the last note
    was a rest, whether the last note was tied, what the last quarterLength was, and what the
    last pitches’ midi number was

    which can be fed back into this algorithm:

    ```python
    >>> streamString2, measures = search.translateIntervalsAndSpeed(sn, returnMeasures=True)
    >>> streamString == streamString2
    True
    >>> measures
    [1, 1, 1, 1, 1, 2, 2, 2]
    ```

music21.search.base.translateNoteTieToByte(*n: [GeneralNote](moduleNote.html#music21.note.GeneralNote "music21.note.GeneralNote")*)[[source]](../_modules/music21/search/base.html#translateNoteTieToByte)
:   takes a note.Note object and returns a one-byte representation
    of its tie status.
    ‘s’ if start tie, ‘e’ if stop tie, ‘c’ if continue tie, and ‘’ if no tie

    ```python
    >>> n = note.Note('E')
    >>> search.translateNoteTieToByte(n)
    ''
    ```

    ```python
    >>> n.tie = tie.Tie('start')
    >>> search.translateNoteTieToByte(n)
    's'
    ```

    ```python
    >>> n.tie.type = 'continue'
    >>> search.translateNoteTieToByte(n)
    'c'
    ```

    ```python
    >>> n.tie.type = 'stop'
    >>> search.translateNoteTieToByte(n)
    'e'
    ```

music21.search.base.translateNoteToByte(*n: [GeneralNote](moduleNote.html#music21.note.GeneralNote "music21.note.GeneralNote")*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](../_modules/music21/search/base.html#translateNoteToByte)
:   takes a note.Note object and translates it to a single byte representation in a string.

    currently returns the chr() for the note’s midi number. or chr(127) for rests
    and unpitched.

    ```python
    >>> n = note.Note('C4')
    >>> b = search.translateNoteToByte(n)
    >>> b
    '<'
    >>> ord(b)
    60
    >>> ord(b) == n.pitch.midi
    True
    ```

    Chords are currently just searched on the first Note (or treated as a Rest if None)

music21.search.base.translateNoteWithDurationToBytes(*n: [GeneralNote](moduleNote.html#music21.note.GeneralNote "music21.note.GeneralNote")*, *includeTieByte: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](../_modules/music21/search/base.html#translateNoteWithDurationToBytes)
:   takes a note.Note object and translates it to a three-byte representation as a string.

    currently returns the chr() for the note’s midi number. or chr(127) for rests
    followed by the log of the quarter length (fitted to 1-127, see
    [`translateDurationToBytes()`](#music21.search.base.translateDurationToBytes "music21.search.base.translateDurationToBytes"))
    followed by ‘s’, ‘c’, or ‘e’ if includeTieByte is True and there is a tie.

    ```python
    >>> n = note.Note('C4')
    >>> n.duration.quarterLength = 3  # dotted half
    >>> trans = search.translateNoteWithDurationToBytes(n)
    >>> trans
    '<_'
    >>> (2**(ord(trans[1])/10.0))/256  # approximately 3
    2.828...
    ```

    ```python
    >>> n.tie = tie.Tie('stop')
    >>> trans = search.translateNoteWithDurationToBytes(n)
    >>> trans
    '<_e'
    ```

    ```python
    >>> trans = search.translateNoteWithDurationToBytes(n, includeTieByte=False)
    >>> trans
    '<_'
    ```

music21.search.base.translateStreamToString(*inputStreamOrIterator*, *returnMeasures=False*)[[source]](../_modules/music21/search/base.html#translateStreamToString)
:   takes a stream (or streamIterator) of notesAndRests only and returns
    a string for searching on.

    ```python
    >>> s = converter.parse("tinynotation: 3/4 c4 d8 r16 FF8. a'8 b-2.")
    >>> sn = s.flatten().notesAndRests
    >>> streamString = search.translateStreamToString(sn)
    >>> print(streamString)
    <P>F<)KQFF_
    >>> len(streamString)
    12
    ```

    Chords give the pitch only of the first note and Unpitched objects are
    treated as rests:

    ```python
    >>> s = stream.Stream([note.Note('C4'), note.Rest(),
    ...                    chord.Chord(['C4', 'E4']), note.Unpitched()])
    >>> streamString = search.translateStreamToString(s)
    >>> list(streamString.encode('utf-8'))
    [60, 80, 127, 80, 60, 80, 127, 80]
    ```

music21.search.base.translateStreamToStringNoRhythm(*inputStream*, *returnMeasures=False*)[[source]](../_modules/music21/search/base.html#translateStreamToStringNoRhythm)
:   takes a stream or streamIterator of notesAndRests only and returns
    a string for searching on, using translateNoteToByte.

    ```python
    >>> s = converter.parse("tinynotation: 4/4 c4 d e FF a'2 b-2")
    >>> sn = s.flatten().notesAndRests
    >>> search.translateStreamToStringNoRhythm(sn)
    '<>@)QF'
    ```

    With returnMeasures, will return a tuple of bytes and a list of measure numbers:

    ```python
    >>> search.translateStreamToStringNoRhythm(sn, returnMeasures=True)
    ('<>@)QF', [1, 1, 1, 1, 2, 2])
    ```

music21.search.base.translateStreamToStringOnlyRhythm(*inputStream*, *returnMeasures=False*)[[source]](../_modules/music21/search/base.html#translateStreamToStringOnlyRhythm)
:   takes a stream or streamIterator of notesAndRests only and returns
    a string for searching on.

    ```python
    >>> s = converter.parse("tinynotation: 3/4 c4 d8 e16 FF8. a'8 b-2.")
    >>> sn = s.flatten().notesAndRests
    >>> streamString = search.translateStreamToStringOnlyRhythm(sn)
    >>> print(streamString)
    PF<KF_
    >>> len(streamString)
    6
    ```
