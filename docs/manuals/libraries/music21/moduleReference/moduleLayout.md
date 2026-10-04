Source: https://music21.org/music21docs/moduleReference/moduleLayout.html

# music21.layout

The layout.py module contains two types of objects that specify the layout on
page (or screen) for Scores and other Stream objects. There are two main types
of Layout objects: (1) layout describing elements and (2) layout defining Streams.

(1) ScoreLayout, PageLayout, SystemLayout, and StaffLayout objects describe the size of
pages, the geometry of page and system margins, the distance between staves, etc.
The model for these layout objects is taken directly (perhaps too directly?)
from MusicXML. These objects all inherit from a BaseLayout class, primarily
as an aid to finding all of these objects as a group. ScoreLayouts give defaults
for each page, system, and staff. Thus, they contain PageLayout, SystemLayout, and
currently one or more StaffLayout objects (but probably just one. MusicXML allows more than
StaffLayout object because multiple staves can be in a Part. Music21 uses
the concept of a PartStaff for a Part that is played by the same performer as another.
e.g., the left hand of the Piano is a PartStaff paired with the right hand).

PageLayout and SystemLayout objects also have a property, ‘isNew’,
which, if set to True, signifies that a new page
or system should begin here. In theory, one could define new dimensions for a page
or system in the middle of the system or page without setting isNew to True, in
which case these measurements would start applying on the next page. In practice,
there’s really one good place to use these Layout objects and that’s in the first part
in a score at offset 0 of the first measure on a page or system
(or for ScoreLayout, at the beginning
of a piece outside any parts). But it’s not an
error to put them in other places, such as at offset 0 of the first measure of a page
or system in all the other parts. In fact, MusicXML tends to do this, and it ends up
not being a waste if a program extracts a single part from the middle of a score.

These objects are standard [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object") types, but many
properties such as .duration, .beat, will probably not apply.

When exporting to MusicXML (which is currently the only format in which music21 can and
does preserve these markings), many MusicXML readers will ignore these tags (or worse,
add a new page or system when PageLayout and SystemLayout objects are found but also
add theme wherever they want). In Finale, this behavior disappears if the MusicXML
document notes that it <supports> new-page and new-system markings. Music21 will add
the appropriate <supports> tags if the containing Stream has .definesExplicitPageBreaks
and .definesExplicitSystemBreaks set to True. When importing a score that has the
<supports> tag set, music21 will set .definesExplicitXXXXBreaks to True for the
outer score and the inner parts. However, this means that if the score is manipulated
enough that the prior layout information is obsolete, programs will need to set these
properties to False or move the Layout tags accordingly.

(2) The second set of objects are Stream subclasses that can be employed when a program
needs to easily iterate around the systems and pages defined through the layout objects
just described, or to get the exact position on a page (or a graphical representation
of a page) for a particular measure or system. (Individual notes coming soon). Normal
Score streams can be changed into LayoutStreams by calling divideByPages(s) on them.
A Score that was organized: Score->Part->Measure would then become:
LayoutScore->Page->System->Staff->Measure.

The new LayoutScore has methods that enable querying what page or system a measure is in, and
specifically where on a page a measure is (or the dimensions
of every measure in the piece). However
do not call .show() on a LayoutScore – the normal score it’s derived from will work just fine.
Nor does calling .show() on a Page or System work yet, but once the LayoutStream has been created,
code like this can be done:

> s = stream.Stream(…)
> ls = layout.divideByPages(s)
> pg2sys3 = ls.pages[1].systems[2] # n.b.! 1, 2
> measureStart, measureEnd = pg2sys3.measureStart, pg2sys3.measureEnd
> scoreExcerpt = s.measures(measureStart, measureEnd)
> scoreExcerpt.show() # will show page 2, system 3

Note that while the coordinates given by music21 for a musicxml score (based on margins,
staff size, etc.)
generally reflect what is actually in a musicxml producer, unfortunately, x-positions are
far less accurately
produced by most editors. For instance, Finale scores with measure sizes that have been
manually adjusted tend to show their
unadjusted measure width and not their actual measure width in the MusicXML.

SmartScore Pro tends to produce very good MusicXML layout data.

## ScoreLayout

class music21.layout.ScoreLayout(*\**, *scalingMillimeters: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *scalingTenths: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *musicFont: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *wordFont: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *pageLayout: [PageLayout](#music21.layout.PageLayout "music21.layout.PageLayout") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *systemLayout: [SystemLayout](#music21.layout.SystemLayout "music21.layout.SystemLayout") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *staffLayoutList: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[StaffLayout](#music21.layout.StaffLayout "music21.layout.StaffLayout")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\*\*keywords*)[[source]](../_modules/music21/layout.html#ScoreLayout)
:   Parameters for configuring a score’s layout.

    PageLayout objects may be found on Measure or Part Streams.

    ```python
    >>> pl = layout.PageLayout(pageNumber=4, leftMargin=234, rightMargin=124,
    ...                        pageHeight=4000, pageWidth=3000, isNew=True)
    >>> pl.pageNumber
    4
    >>> pl.rightMargin
    124
    >>> pl.leftMargin
    234
    >>> pl.isNew
    True
    ```

    This object represents both <print new-page> and <page-layout>
    elements in musicxml. The appearance tag is handled in the .style
    for the stream (it was here in v7 and before, but did nothing).

    Note that the appearance and style elements are subject to change during
    and after the v8 releases.

[`ScoreLayout`](#music21.layout.ScoreLayout "music21.layout.ScoreLayout") bases

* [`LayoutBase`](#music21.layout.LayoutBase "music21.layout.LayoutBase")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`ScoreLayout`](#music21.layout.ScoreLayout "music21.layout.ScoreLayout") read-only properties

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`ScoreLayout`](#music21.layout.ScoreLayout "music21.layout.ScoreLayout") read/write properties

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`ScoreLayout`](#music21.layout.ScoreLayout "music21.layout.ScoreLayout") methods

ScoreLayout.tenthsToMillimeters(*tenths: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")[[source]](../_modules/music21/layout.html#ScoreLayout.tenthsToMillimeters)
:   given the scalingMillimeters and scalingTenths,
    return the value in millimeters of a number of
    musicxml “tenths” where a tenth is a tenth of the distance
    from one staff line to another.

    returns 0.0 if either of scalingMillimeters or scalingTenths
    is undefined.

    ```python
    >>> sl = layout.ScoreLayout(scalingMillimeters=2.0, scalingTenths=10)
    >>> sl.tenthsToMillimeters(10)
    2.0
    ```

    Numbers are rounded to a maximum of 6 digits (but because they are floats,
    there may be inaccuracies.

    ```python
    >>> sl.tenthsToMillimeters(17)
    3.4
    ```

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`ScoreLayout`](#music21.layout.ScoreLayout "music21.layout.ScoreLayout") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## PageLayout

class music21.layout.PageLayout(*\**, *pageNumber: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *leftMargin: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *rightMargin: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *topMargin: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *bottomMargin: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *pageHeight: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *pageWidth: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *isNew: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\*\*keywords*)[[source]](../_modules/music21/layout.html#PageLayout)
:   Parameters for configuring a page’s layout.

    PageLayout objects may be found on Measure or Part Streams.

    ```python
    >>> pl = layout.PageLayout(pageNumber=4, leftMargin=234, rightMargin=124,
    ...                        pageHeight=4000, pageWidth=3000, isNew=True)
    >>> pl.pageNumber
    4
    >>> pl.rightMargin
    124
    >>> pl.leftMargin
    234
    >>> pl.isNew
    True
    ```

    This object represents both <print new-page> and <page-layout>
    elements in musicxml.

[`PageLayout`](#music21.layout.PageLayout "music21.layout.PageLayout") bases

* [`LayoutBase`](#music21.layout.LayoutBase "music21.layout.LayoutBase")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`PageLayout`](#music21.layout.PageLayout "music21.layout.PageLayout") read-only properties

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`PageLayout`](#music21.layout.PageLayout "music21.layout.PageLayout") read/write properties

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`PageLayout`](#music21.layout.PageLayout "music21.layout.PageLayout") methods

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`PageLayout`](#music21.layout.PageLayout "music21.layout.PageLayout") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## SystemLayout

class music21.layout.SystemLayout(*\**, *leftMargin: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *rightMargin: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *distance: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *topDistance: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *isNew: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\*\*keywords*)[[source]](../_modules/music21/layout.html#SystemLayout)
:   Object that configures or alters a system’s layout.

    SystemLayout objects may be found on Measure or
    Part Streams.

    Importantly, if isNew is True then this object
    indicates that a new system should start here.

    ```python
    >>> sl = layout.SystemLayout(leftMargin=234, rightMargin=124, distance=3, isNew=True)
    >>> sl.distance
    3
    >>> sl.rightMargin
    124
    >>> sl.leftMargin
    234
    >>> sl.isNew
    True
    ```

[`SystemLayout`](#music21.layout.SystemLayout "music21.layout.SystemLayout") bases

* [`LayoutBase`](#music21.layout.LayoutBase "music21.layout.LayoutBase")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`SystemLayout`](#music21.layout.SystemLayout "music21.layout.SystemLayout") read-only properties

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`SystemLayout`](#music21.layout.SystemLayout "music21.layout.SystemLayout") read/write properties

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`SystemLayout`](#music21.layout.SystemLayout "music21.layout.SystemLayout") methods

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`SystemLayout`](#music21.layout.SystemLayout "music21.layout.SystemLayout") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## StaffLayout

class music21.layout.StaffLayout(*\**, *distance: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *staffNumber: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *staffSize: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *staffLines: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *hidden: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *staffType: [StaffType](moduleStreamEnums.html#music21.stream.enums.StaffType "music21.stream.enums.StaffType") = StaffType.REGULAR*, *\*\*keywords*)[[source]](../_modules/music21/layout.html#StaffLayout)
:   Object that configures or alters the distance between
    one staff and another in a system.

    StaffLayout objects may be found on Measure or
    Part Streams.

    The musicxml equivalent <staff-layout> lives in
    the <defaults> and in <print> attributes.

    ```python
    >>> sl = layout.StaffLayout(distance=3, staffNumber=1, staffSize=113, staffLines=5)
    >>> sl.distance
    3
    ```

    The “number” attribute refers to which staff number
    in a part group this refers to. Thus, it’s not
    necessary in music21, but we store it if it’s there.
    (defaults to None)

    ```python
    >>> sl.staffNumber
    1
    ```

    staffLines specifies the number of lines for a non 5-line staff.

    ```python
    >>> sl.staffLines
    5
    ```

    staffSize is a percentage of the base staff size, so
    this defines a staff 13% larger than normal. Note that it is always converted to
    a floating point number.

    ```python
    >>> sl.staffSize
    113.0
    >>> sl
    <music21.layout.StaffLayout distance 3, staffNumber 1, staffSize 113.0, staffLines 5>
    ```

    StaffLayout can also specify the staffType:

    ```python
    >>> sl.staffType = stream.enums.StaffType.OSSIA
    ```

    There is one other attribute, ‘.hidden’ which has three settings:

    * None - inherit from previous StaffLayout object, or False if no object exists
    * False - not hidden – show as a default staff
    * True - hidden – for playback only staves, or for a hidden/optimized-out staff

    Note: (TODO: .hidden None is not working; always gives False)

[`StaffLayout`](#music21.layout.StaffLayout "music21.layout.StaffLayout") bases

* [`LayoutBase`](#music21.layout.LayoutBase "music21.layout.LayoutBase")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`StaffLayout`](#music21.layout.StaffLayout "music21.layout.StaffLayout") read-only properties

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`StaffLayout`](#music21.layout.StaffLayout "music21.layout.StaffLayout") read/write properties

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`StaffLayout`](#music21.layout.StaffLayout "music21.layout.StaffLayout") methods

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`StaffLayout`](#music21.layout.StaffLayout "music21.layout.StaffLayout") instance variables

StaffLayout.staffType
:   What kind of staff is this as a stream.enums.StaffType.

    ```python
    >>> sl = layout.StaffLayout()
    >>> sl.staffType
    <StaffType.REGULAR: 'regular'>
    >>> sl.staffType = stream.enums.StaffType.CUE
    >>> sl.staffType
    <StaffType.CUE: 'cue'>
    ```

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## LayoutBase

class music21.layout.LayoutBase(*id: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *groups: [Groups](moduleBase.html#music21.base.Groups "music21.base.Groups") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *sites: [Sites](moduleSites.html#music21.sites.Sites "music21.sites.Sites") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *duration: [Duration](moduleDuration.html#music21.duration.Duration "music21.duration.Duration") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *activeSite: stream.Stream | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *style: [Style](moduleStyle.html#music21.style.Style "music21.style.Style") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *editorial: [Editorial](moduleEditorial.html#music21.editorial.Editorial "music21.editorial.Editorial") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *offset: OffsetQL = 0.0*, *quarterLength: OffsetQLIn | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\*\*keywords*)[[source]](../_modules/music21/layout.html#LayoutBase)
:   A base class for all Layout objects, defining a classSortOrder
    and also an inheritance tree.

    ```python
    >>> scoreLayout = layout.ScoreLayout()
    >>> isinstance(scoreLayout, layout.LayoutBase)
    True
    ```

[`LayoutBase`](#music21.layout.LayoutBase "music21.layout.LayoutBase") bases

* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LayoutBase`](#music21.layout.LayoutBase "music21.layout.LayoutBase") read-only properties

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LayoutBase`](#music21.layout.LayoutBase "music21.layout.LayoutBase") read/write properties

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`LayoutBase`](#music21.layout.LayoutBase "music21.layout.LayoutBase") methods

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`LayoutBase`](#music21.layout.LayoutBase "music21.layout.LayoutBase") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## LayoutScore

class music21.layout.LayoutScore(*givenElements=None*, *\*\*keywords*)[[source]](../_modules/music21/layout.html#LayoutScore)
:   Designation that this Score is
    divided into Pages, Systems, Staves (=Parts),
    Measures, etc.

    Used for computing location of notes, etc.

    If the score does not change between calls to the various getPosition calls,
    it is much faster as it uses a cache.

[`LayoutScore`](#music21.layout.LayoutScore "music21.layout.LayoutScore") bases

* [`Opus`](moduleStreamBase.html#music21.stream.base.Opus "music21.stream.base.Opus")
* [`Stream`](moduleStreamBase.html#music21.stream.base.Stream "music21.stream.base.Stream")
* [`StreamCore`](moduleStreamCore.html#music21.stream.core.StreamCore "music21.stream.core.StreamCore")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LayoutScore`](#music21.layout.LayoutScore "music21.layout.LayoutScore") read-only properties

LayoutScore.pages

Read-only properties inherited from [`Opus`](moduleStreamBase.html#music21.stream.base.Opus "music21.stream.base.Opus"):

|  |  |  |
| --- | --- | --- |
| * [`scores`](moduleStreamBase.html#music21.stream.base.Opus.scores "music21.stream.base.Opus.scores") |  |  |

Read-only properties inherited from [`Stream`](moduleStreamBase.html#music21.stream.base.Stream "music21.stream.base.Stream"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleStreamBase.html#music21.stream.base.Stream.beat "music21.stream.base.Stream.beat") * [`beatDuration`](moduleStreamBase.html#music21.stream.base.Stream.beatDuration "music21.stream.base.Stream.beatDuration") * [`beatStr`](moduleStreamBase.html#music21.stream.base.Stream.beatStr "music21.stream.base.Stream.beatStr") * [`beatStrength`](moduleStreamBase.html#music21.stream.base.Stream.beatStrength "music21.stream.base.Stream.beatStrength") * [`highestOffset`](moduleStreamBase.html#music21.stream.base.Stream.highestOffset "music21.stream.base.Stream.highestOffset") | * [`highestTime`](moduleStreamBase.html#music21.stream.base.Stream.highestTime "music21.stream.base.Stream.highestTime") * [`isGapless`](moduleStreamBase.html#music21.stream.base.Stream.isGapless "music21.stream.base.Stream.isGapless") * [`lowestOffset`](moduleStreamBase.html#music21.stream.base.Stream.lowestOffset "music21.stream.base.Stream.lowestOffset") * [`notes`](moduleStreamBase.html#music21.stream.base.Stream.notes "music21.stream.base.Stream.notes") * [`notesAndRests`](moduleStreamBase.html#music21.stream.base.Stream.notesAndRests "music21.stream.base.Stream.notesAndRests") | * [`pitches`](moduleStreamBase.html#music21.stream.base.Stream.pitches "music21.stream.base.Stream.pitches") * [`secondsMap`](moduleStreamBase.html#music21.stream.base.Stream.secondsMap "music21.stream.base.Stream.secondsMap") * [`spanners`](moduleStreamBase.html#music21.stream.base.Stream.spanners "music21.stream.base.Stream.spanners") * [`voices`](moduleStreamBase.html#music21.stream.base.Stream.voices "music21.stream.base.Stream.voices") |

Read-only properties inherited from [`StreamCore`](moduleStreamCore.html#music21.stream.core.StreamCore "music21.stream.core.StreamCore"):

|  |  |  |
| --- | --- | --- |
| * [`spannerBundle`](moduleStreamCore.html#music21.stream.core.StreamCore.spannerBundle "music21.stream.core.StreamCore.spannerBundle") |  |  |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") | * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LayoutScore`](#music21.layout.LayoutScore "music21.layout.LayoutScore") read/write properties

Read/write properties inherited from [`Stream`](moduleStreamBase.html#music21.stream.base.Stream "music21.stream.base.Stream"):

|  |  |  |
| --- | --- | --- |
| * [`atSoundingPitch`](moduleStreamBase.html#music21.stream.base.Stream.atSoundingPitch "music21.stream.base.Stream.atSoundingPitch") * [`clef`](moduleStreamBase.html#music21.stream.base.Stream.clef "music21.stream.base.Stream.clef") * [`duration`](moduleStreamBase.html#music21.stream.base.Stream.duration "music21.stream.base.Stream.duration") * [`elements`](moduleStreamBase.html#music21.stream.base.Stream.elements "music21.stream.base.Stream.elements") | * [`finalBarline`](moduleStreamBase.html#music21.stream.base.Stream.finalBarline "music21.stream.base.Stream.finalBarline") * [`keySignature`](moduleStreamBase.html#music21.stream.base.Stream.keySignature "music21.stream.base.Stream.keySignature") * [`metadata`](moduleStreamBase.html#music21.stream.base.Stream.metadata "music21.stream.base.Stream.metadata") | * [`seconds`](moduleStreamBase.html#music21.stream.base.Stream.seconds "music21.stream.base.Stream.seconds") * [`staffLines`](moduleStreamBase.html#music21.stream.base.Stream.staffLines "music21.stream.base.Stream.staffLines") * [`timeSignature`](moduleStreamBase.html#music21.stream.base.Stream.timeSignature "music21.stream.base.Stream.timeSignature") |

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`LayoutScore`](#music21.layout.LayoutScore "music21.layout.LayoutScore") methods

LayoutScore.getAllMeasurePositionsInDocument(*returnFormat='tenths'*, *printUpdates=False*)[[source]](../_modules/music21/layout.html#LayoutScore.getAllMeasurePositionsInDocument)
:   returns a list of dictionaries, where each dictionary gives the measure number
    and other information, etc. in the document.

    # >>> g = corpus.parse(‘luca/gloria’)
    # >>> gl = layout.divideByPages(g)
    # >>> gl.getAllMeasurePositionsInDocument()

LayoutScore.getMarginsAndSizeForPageId(*pageId*)[[source]](../_modules/music21/layout.html#LayoutScore.getMarginsAndSizeForPageId)
:   return a namedtuple of (top, left, bottom, right, width, height)
    margins for a given pageId in tenths

    Default of (100, 100, 100, 100, 850, 1100) if undefined

    ```python
    >>> g = corpus.parse('luca/gloria')
    >>> m22 = g.parts[0].getElementsByClass(stream.Measure)[22]
    >>> m22.getElementsByClass(layout.PageLayout).first().leftMargin = 204.0
    >>> gl = layout.divideByPages(g)
    >>> gl.getMarginsAndSizeForPageId(1)
    PageSize(top=171.0, left=204.0, right=171.0, bottom=171.0, width=1457.0, height=1886.0)
    ```

LayoutScore.getPageAndSystemNumberFromMeasureNumber(*measureNumber*)[[source]](../_modules/music21/layout.html#LayoutScore.getPageAndSystemNumberFromMeasureNumber)
:   Given a layoutScore from divideByPages and a measureNumber returns a tuple
    of (pageId, systemId). Note that pageId is probably one less than the page number,
    assuming that the first page number is 1, the pageId for the first page will be 0.

    Similarly, the first systemId on each page will be 0

    ```python
    >>> lt = corpus.parse('demos/layoutTest.xml')
    >>> l = layout.divideByPages(lt, fastMeasures=True)
    >>> l.getPageAndSystemNumberFromMeasureNumber(80)
    (3, 3)
    ```

LayoutScore.getPositionForStaff(*pageId*, *systemId*, *staffId*)[[source]](../_modules/music21/layout.html#LayoutScore.getPositionForStaff)
:   return a tuple of (top, bottom) for a staff, specified by a given pageId,
    systemId, and staffId in tenths of a staff-space.

    This distance is specified with respect to the top of the system.

    Staff scaling (<staff-details> in musicxml inside an <attributes> object) is
    taken into account, but not non-five-line staves. Thus, a normally sized staff
    is always of height 40 (4 spaces of 10-tenths each)

    ```python
    >>> lt = corpus.parse('demos/layoutTest.xml')
    >>> ls = layout.divideByPages(lt, fastMeasures=True)
    ```

    The first staff (staff 0) of each page/system always begins at height 0 and should end at
    height 40 if it is a 5-line staff (not taken into account) with no staffSize changes

    ```python
    >>> ls.getPositionForStaff(0, 0, 0)
    (0.0, 40.0)
    >>> ls.getPositionForStaff(1, 0, 0)
    (0.0, 40.0)
    ```

    The second staff (staff 1) begins at the end of staff 0 (40.0) +
    the appropriate staffDistance
    and adds the height of the staff. Staff 1 here has a size of 80 which means
    80% of the normal staff size. 40 \* 0.8 = 32.0:

    ```python
    >>> ls.getPositionForStaff(0, 0, 1)
    (133.0, 165.0)
    ```

    The third staff (staff 2) begins after the second staff (staff 1) but is a normal
    size staff

    ```python
    >>> ls.getPositionForStaff(0, 0, 2)
    (266.0, 306.0)
    ```

    The first staff (staff 0) of the second system (system 1) also begins at 0
    and as a normally-sized staff, has height of 40:

    ```python
    >>> ls.getPositionForStaff(0, 1, 0)
    (0.0, 40.0)
    ```

    The spacing between the staves has changed in the second system, but the
    staff height has not:

    ```python
    >>> ls.getPositionForStaff(0, 1, 1)
    (183.0, 215.0)
    >>> ls.getPositionForStaff(0, 1, 2)
    (356.0, 396.0)
    ```

    In the third system (system 2), the staff distance reverts to the distance
    of system 0, but the staffSize is now 120 or 48 tenths (40 \* 1.2 = 48)

    ```python
    >>> ls.getPositionForStaff(0, 2, 1)
    (117.0, 165.0)
    ```

    Page 1 (0), System 4 (3), Staff 2 (1) is a hidden (“optimized”) system.
    Thus, its staffLayout notes this:

    ```python
    >>> staffLayout031 = ls.pages[0].systems[3].staves[1].staffLayout
    >>> staffLayout031
    <music21.layout.StaffLayout distance None, staffNumber None, staffSize 80, staffLines None>
    >>> staffLayout031.hidden
    True
    ```

    Thus, the position for this staff will have the same top and bottom, and the
    position for the next staff will have the same top as the previous staff:

    ```python
    >>> ls.getPositionForStaff(0, 3, 0)
    (0.0, 40.0)
    >>> ls.getPositionForStaff(0, 3, 1)
    (40.0, 40.0)
    >>> ls.getPositionForStaff(0, 3, 2)
    (133.0, 173.0)
    ```

    Tests for a score with PartStaff objects:
    >>> lt = corpus.parse(‘demos/layoutTestMore.xml’)
    >>> ls = layout.divideByPages(lt, fastMeasures = True)
    >>> ls.getPositionForStaff(0, 0, 0)
    (0.0, 40.0)
    >>> ls.getPositionForStaff(0, 0, 1)
    (133.0, 173.0)
    >>> ls.getPositionForStaff(0, 0, 2)
    (235.0, 275.0)

    ```python
    >>> ls.getPositionForStaff(0, 2, 0)
    (0.0, 40.0)
    >>> ls.getPositionForStaff(0, 2, 1)
    (40.0, 40.0)
    >>> ls.getPositionForStaff(0, 2, 2)
    (40.0, 40.0)
    ```

    System 4 has the top staff hidden, which has been causing problems:

    ```python
    >>> ls.getPositionForStaff(0, 4, 0)
    (0.0, 0.0)
    >>> ls.getPositionForStaff(0, 4, 1)
    (0.0, 40.0)
    ```

LayoutScore.getPositionForStaffMeasure(*staffId*, *measureNumber*, *returnFormat='tenths'*)[[source]](../_modules/music21/layout.html#LayoutScore.getPositionForStaffMeasure)
:   Given a layoutScore from divideByPages, a staffId, and a measureNumber,
    returns a tuple of ((top, left), (bottom, right), pageId)
    allowing an exact position for the measure on the page.
    If returnFormat is “tenths”, then it will be returned in tenths.

    If returnFormat is “float”, returns each as a number from 0 to 1 where 0 is the
    top or left of the page, and 1 is the bottom or right of the page.

    ```python
    >>> lt = corpus.parse('demos/layoutTest.xml')
    >>> ls = layout.divideByPages(lt, fastMeasures = True)
    ```

    The first measure of staff one begins at 336 tenths from the top (125 for the
    margin top and 211 for the top-staff-distance). It begins 170.0 from the
    left (100 for the page-margin-left, 70 for staff-margin-left). It ends
    40.0 below that (staffHeight) and 247.0 to the right (measure width)

    ```python
    >>> ls.getPositionForStaffMeasure(0, 1)
    ((336.0, 170.0), (376.0, 417.0), 0)
    ```

    The other staves for the same measure are below this one:

    ```python
    >>> ls.getPositionForStaffMeasure(1, 1)
    ((469.0, 170.0), (501.0, 417.0), 0)
    >>> ls.getPositionForStaffMeasure(2, 1)
    ((602.0, 170.0), (642.0, 417.0), 0)
    ```

    If float is requested for returning, then the numbers are the fraction of
    the distance across the page.

    ```python
    >>> ls.getPositionForStaffMeasure(0, 1, returnFormat='float')
    ((0.152..., 0.0996...), (0.170..., 0.244...), 0)
    ```

    Moving over the page boundary:

    ```python
    >>> ls.getPositionForStaffMeasure(0, 23)
    ((1703.0, 1345.0), (1743.0, 1606.0), 0)
    >>> ls.getPositionForStaffMeasure(1, 23)  # hidden
    ((1743.0, 1345.0), (1743.0, 1606.0), 0)
    >>> ls.getPositionForStaffMeasure(0, 24)
    ((195.0, 100.0), (235.0, 431.0), 1)
    >>> ls.getPositionForStaffMeasure(1, 24)
    ((328.0, 100.0), (360.0, 431.0), 1)
    ```

LayoutScore.getPositionForSystem(*pageId: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *systemId: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [SystemSize](#music21.layout.SystemSize "music21.layout.SystemSize")[[source]](../_modules/music21/layout.html#LayoutScore.getPositionForSystem)
:   first systems on a page use a different positioning.

    returns a Named tuple of the (top, left, right, and bottom) where each unit is
    relative to the page margins

    N.B. right is NOT the width – it is different. It is the offset to the right margin.
    weird, inconsistent, but most useful. Bottom, however, is the hard part to compute.

    ```python
    >>> lt = corpus.parse('demos/layoutTestMore.xml')
    >>> ls = layout.divideByPages(lt, fastMeasures = True)
    >>> ls.getPositionForSystem(0, 0)
    SystemSize(top=211.0, left=70.0, right=0.0, bottom=696.0)
    >>> ls.getPositionForSystem(0, 1)
    SystemSize(top=810.0, left=0.0, right=0.0, bottom=1173.0)
    >>> ls.getPositionForSystem(0, 2)
    SystemSize(top=1340.0, left=67.0, right=92.0, bottom=1610.0)
    >>> ls.getPositionForSystem(0, 3)
    SystemSize(top=1724.0, left=0.0, right=0.0, bottom=2030.0)
    >>> ls.getPositionForSystem(0, 4)
    SystemSize(top=2144.0, left=0.0, right=0.0, bottom=2583.0)
    ```

LayoutScore.getStaffDistanceFromPrevious(*pageId*, *systemId*, *staffId*)[[source]](../_modules/music21/layout.html#LayoutScore.getStaffDistanceFromPrevious)
:   return the distance of this staff from the previous staff in the same system

    for staffId = 0, this is always 0.0

    TODO:tests, now that this is out from previous

LayoutScore.getStaffHiddenAttribute(*pageId: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *systemId: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *staffId: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/layout.html#LayoutScore.getStaffHiddenAttribute)
:   returns the staffLayout.hidden attribute for a staffId, or if it is not
    defined, recursively search through previous staves until one is found.

    ```python
    >>> lt = corpus.parse('demos/layoutTestMore.xml')
    >>> ls = layout.divideByPages(lt, fastMeasures = True)
    >>> ls.getStaffHiddenAttribute(0, 0, 0)
    False
    >>> ls.getStaffHiddenAttribute(0, 0, 1)
    False
    >>> ls.getStaffHiddenAttribute(0, 1, 1)
    True
    >>> ls.getStaffHiddenAttribute(0, 2, 1)
    True
    >>> ls.getStaffHiddenAttribute(0, 3, 1)
    False
    ```

LayoutScore.getStaffSizeFromLayout(*pageId: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *systemId: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *staffId: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")[[source]](../_modules/music21/layout.html#LayoutScore.getStaffSizeFromLayout)
:   Get the currently active staff-size for a given pageId, systemId, and staffId.

    Note that this does not take into account the hidden state of the staff, which,
    if True, makes the effective size 0.0 – see getStaffHiddenAttribute

    ```python
    >>> lt = corpus.parse('demos/layoutTest.xml')
    >>> ls = layout.divideByPages(lt, fastMeasures=True)
    >>> ls.getStaffSizeFromLayout(0, 0, 0)
    40.0
    >>> ls.getStaffSizeFromLayout(0, 0, 1)
    32.0
    >>> ls.getStaffSizeFromLayout(0, 0, 2)
    40.0
    >>> ls.getStaffSizeFromLayout(0, 1, 1)
    32.0
    >>> ls.getStaffSizeFromLayout(0, 2, 1)
    48.0
    >>> ls.getStaffSizeFromLayout(0, 3, 1)
    32.0
    ```

LayoutScore.getSystemBeforeThis(*pageId: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *systemId: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][[source]](../_modules/music21/layout.html#LayoutScore.getSystemBeforeThis)
:   given a pageId and systemId, get the (pageId, systemId) for the previous system.

    return (None, None) if it’s the first system on the first page

    This test score has five systems on the first page,
    three on the second, and two on the third

    ```python
    >>> lt = corpus.parse('demos/layoutTestMore.xml')
    >>> ls = layout.divideByPages(lt, fastMeasures = True)
    >>> systemId = 1
    >>> pageId = 2  # last system, last page
    >>> while pageId is not None:
    ...    pageId, systemId = ls.getSystemBeforeThis(pageId, systemId)
    ...    (pageId, systemId)
    (2, 0) (1, 2) (1, 1) (1, 0) (0, 4) (0, 3) (0, 2) (0, 1) (0, 0) (None, -1)
    ```

LayoutScore.measurePositionWithinSystem(*measureNumber*, *pageId=None*, *systemId=None*)[[source]](../_modules/music21/layout.html#LayoutScore.measurePositionWithinSystem)
:   Given a measure number, find the start and end X positions (with respect to
    the system margins) for the measure.

    if pageId and systemId are given, then it will speed up the search. But not necessary

    no staffId is needed since (at least for now) all measures begin and end at the same
    X position

    ```python
    >>> l = corpus.parse('demos/layoutTest.xml')
    >>> ls = layout.divideByPages(l, fastMeasures = True)
    >>> ls.measurePositionWithinSystem(1, 0, 0)
    (0.0, 247.0)
    >>> ls.measurePositionWithinSystem(2, 0, 0)
    (247.0, 544.0)
    >>> ls.measurePositionWithinSystem(3, 0, 0)
    (544.0, 841.0)
    ```

    Measure positions reset at the start of a new system

    ```python
    >>> ls.measurePositionWithinSystem(6)
    (0.0, 331.0)
    >>> ls.measurePositionWithinSystem(7)
    (331.0, 549.0)
    ```

LayoutScore.show(*fmt=None*, *app=None*, *\*\*keywords*)[[source]](../_modules/music21/layout.html#LayoutScore.show)
:   Borrows stream.Score.show

    ```python
    >>> lp = layout.Page()
    >>> ls = layout.LayoutScore()
    >>> ls.append(lp)
    >>> ls.show('text')
    {0.0} <music21.layout.Page p.1>
    ```

Methods inherited from [`Opus`](moduleStreamBase.html#music21.stream.base.Opus "music21.stream.base.Opus"):

|  |  |  |
| --- | --- | --- |
| * [`getNumbers()`](moduleStreamBase.html#music21.stream.base.Opus.getNumbers "music21.stream.base.Opus.getNumbers") * [`getScoreByNumber()`](moduleStreamBase.html#music21.stream.base.Opus.getScoreByNumber "music21.stream.base.Opus.getScoreByNumber") | * [`getScoreByTitle()`](moduleStreamBase.html#music21.stream.base.Opus.getScoreByTitle "music21.stream.base.Opus.getScoreByTitle") * [`mergeScores()`](moduleStreamBase.html#music21.stream.base.Opus.mergeScores "music21.stream.base.Opus.mergeScores") | * [`write()`](moduleStreamBase.html#music21.stream.base.Opus.write "music21.stream.base.Opus.write") |

Methods inherited from [`Stream`](moduleStreamBase.html#music21.stream.base.Stream "music21.stream.base.Stream"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleStreamBase.html#music21.stream.base.Stream.__eq__ "music21.stream.base.Stream.__eq__") * [`__getitem__()`](moduleStreamBase.html#music21.stream.base.Stream.__getitem__ "music21.stream.base.Stream.__getitem__") * [`activateVariants()`](moduleStreamBase.html#music21.stream.base.Stream.activateVariants "music21.stream.base.Stream.activateVariants") * [`addGroupForElements()`](moduleStreamBase.html#music21.stream.base.Stream.addGroupForElements "music21.stream.base.Stream.addGroupForElements") * [`allPlayingWhileSounding()`](moduleStreamBase.html#music21.stream.base.Stream.allPlayingWhileSounding "music21.stream.base.Stream.allPlayingWhileSounding") * [`analyze()`](moduleStreamBase.html#music21.stream.base.Stream.analyze "music21.stream.base.Stream.analyze") * [`append()`](moduleStreamBase.html#music21.stream.base.Stream.append "music21.stream.base.Stream.append") * [`attachIntervalsBetweenStreams()`](moduleStreamBase.html#music21.stream.base.Stream.attachIntervalsBetweenStreams "music21.stream.base.Stream.attachIntervalsBetweenStreams") * [`attachMelodicIntervals()`](moduleStreamBase.html#music21.stream.base.Stream.attachMelodicIntervals "music21.stream.base.Stream.attachMelodicIntervals") * [`augmentOrDiminish()`](moduleStreamBase.html#music21.stream.base.Stream.augmentOrDiminish "music21.stream.base.Stream.augmentOrDiminish") * [`beatAndMeasureFromOffset()`](moduleStreamBase.html#music21.stream.base.Stream.beatAndMeasureFromOffset "music21.stream.base.Stream.beatAndMeasureFromOffset") * [`chordify()`](moduleStreamBase.html#music21.stream.base.Stream.chordify "music21.stream.base.Stream.chordify") * [`clear()`](moduleStreamBase.html#music21.stream.base.Stream.clear "music21.stream.base.Stream.clear") * [`cloneEmpty()`](moduleStreamBase.html#music21.stream.base.Stream.cloneEmpty "music21.stream.base.Stream.cloneEmpty") * [`containerInHierarchy()`](moduleStreamBase.html#music21.stream.base.Stream.containerInHierarchy "music21.stream.base.Stream.containerInHierarchy") * [`elementOffset()`](moduleStreamBase.html#music21.stream.base.Stream.elementOffset "music21.stream.base.Stream.elementOffset") * [`expandRepeats()`](moduleStreamBase.html#music21.stream.base.Stream.expandRepeats "music21.stream.base.Stream.expandRepeats") * [`explode()`](moduleStreamBase.html#music21.stream.base.Stream.explode "music21.stream.base.Stream.explode") * [`extendDuration()`](moduleStreamBase.html#music21.stream.base.Stream.extendDuration "music21.stream.base.Stream.extendDuration") * [`extendTies()`](moduleStreamBase.html#music21.stream.base.Stream.extendTies "music21.stream.base.Stream.extendTies") * [`extractContext()`](moduleStreamBase.html#music21.stream.base.Stream.extractContext "music21.stream.base.Stream.extractContext") * [`findConsecutiveNotes()`](moduleStreamBase.html#music21.stream.base.Stream.findConsecutiveNotes "music21.stream.base.Stream.findConsecutiveNotes") * [`findGaps()`](moduleStreamBase.html#music21.stream.base.Stream.findGaps "music21.stream.base.Stream.findGaps") * [`first()`](moduleStreamBase.html#music21.stream.base.Stream.first "music21.stream.base.Stream.first") * [`flatten()`](moduleStreamBase.html#music21.stream.base.Stream.flatten "music21.stream.base.Stream.flatten") * [`flattenUnnecessaryVoices()`](moduleStreamBase.html#music21.stream.base.Stream.flattenUnnecessaryVoices "music21.stream.base.Stream.flattenUnnecessaryVoices") * [`getElementAfterElement()`](moduleStreamBase.html#music21.stream.base.Stream.getElementAfterElement "music21.stream.base.Stream.getElementAfterElement") * [`getElementAtOrBefore()`](moduleStreamBase.html#music21.stream.base.Stream.getElementAtOrBefore "music21.stream.base.Stream.getElementAtOrBefore") * [`getElementBeforeOffset()`](moduleStreamBase.html#music21.stream.base.Stream.getElementBeforeOffset "music21.stream.base.Stream.getElementBeforeOffset") * [`getElementById()`](moduleStreamBase.html#music21.stream.base.Stream.getElementById "music21.stream.base.Stream.getElementById") * [`getElementsByClass()`](moduleStreamBase.html#music21.stream.base.Stream.getElementsByClass "music21.stream.base.Stream.getElementsByClass") * [`getElementsByGroup()`](moduleStreamBase.html#music21.stream.base.Stream.getElementsByGroup "music21.stream.base.Stream.getElementsByGroup") * [`getElementsByOffset()`](moduleStreamBase.html#music21.stream.base.Stream.getElementsByOffset "music21.stream.base.Stream.getElementsByOffset") * [`getElementsNotOfClass()`](moduleStreamBase.html#music21.stream.base.Stream.getElementsNotOfClass "music21.stream.base.Stream.getElementsNotOfClass") * [`getInstrument()`](moduleStreamBase.html#music21.stream.base.Stream.getInstrument "music21.stream.base.Stream.getInstrument") * [`getInstruments()`](moduleStreamBase.html#music21.stream.base.Stream.getInstruments "music21.stream.base.Stream.getInstruments") | * [`getOverlaps()`](moduleStreamBase.html#music21.stream.base.Stream.getOverlaps "music21.stream.base.Stream.getOverlaps") * [`getTimeSignatures()`](moduleStreamBase.html#music21.stream.base.Stream.getTimeSignatures "music21.stream.base.Stream.getTimeSignatures") * [`hasElement()`](moduleStreamBase.html#music21.stream.base.Stream.hasElement "music21.stream.base.Stream.hasElement") * [`hasElementOfClass()`](moduleStreamBase.html#music21.stream.base.Stream.hasElementOfClass "music21.stream.base.Stream.hasElementOfClass") * [`hasMeasures()`](moduleStreamBase.html#music21.stream.base.Stream.hasMeasures "music21.stream.base.Stream.hasMeasures") * [`hasPartLikeStreams()`](moduleStreamBase.html#music21.stream.base.Stream.hasPartLikeStreams "music21.stream.base.Stream.hasPartLikeStreams") * [`hasVoices()`](moduleStreamBase.html#music21.stream.base.Stream.hasVoices "music21.stream.base.Stream.hasVoices") * [`haveAccidentalsBeenMade()`](moduleStreamBase.html#music21.stream.base.Stream.haveAccidentalsBeenMade "music21.stream.base.Stream.haveAccidentalsBeenMade") * [`index()`](moduleStreamBase.html#music21.stream.base.Stream.index "music21.stream.base.Stream.index") * [`insert()`](moduleStreamBase.html#music21.stream.base.Stream.insert "music21.stream.base.Stream.insert") * [`insertAndShift()`](moduleStreamBase.html#music21.stream.base.Stream.insertAndShift "music21.stream.base.Stream.insertAndShift") * [`insertIntoNoteOrChord()`](moduleStreamBase.html#music21.stream.base.Stream.insertIntoNoteOrChord "music21.stream.base.Stream.insertIntoNoteOrChord") * [`invertDiatonic()`](moduleStreamBase.html#music21.stream.base.Stream.invertDiatonic "music21.stream.base.Stream.invertDiatonic") * [`isSequence()`](moduleStreamBase.html#music21.stream.base.Stream.isSequence "music21.stream.base.Stream.isSequence") * [`isTwelveTone()`](moduleStreamBase.html#music21.stream.base.Stream.isTwelveTone "music21.stream.base.Stream.isTwelveTone") * [`isWellFormedNotation()`](moduleStreamBase.html#music21.stream.base.Stream.isWellFormedNotation "music21.stream.base.Stream.isWellFormedNotation") * [`iter()`](moduleStreamBase.html#music21.stream.base.Stream.iter "music21.stream.base.Stream.iter") * [`last()`](moduleStreamBase.html#music21.stream.base.Stream.last "music21.stream.base.Stream.last") * [`lyrics()`](moduleStreamBase.html#music21.stream.base.Stream.lyrics "music21.stream.base.Stream.lyrics") * [`makeAccidentals()`](moduleStreamBase.html#music21.stream.base.Stream.makeAccidentals "music21.stream.base.Stream.makeAccidentals") * [`makeBeams()`](moduleStreamBase.html#music21.stream.base.Stream.makeBeams "music21.stream.base.Stream.makeBeams") * [`makeImmutable()`](moduleStreamBase.html#music21.stream.base.Stream.makeImmutable "music21.stream.base.Stream.makeImmutable") * [`makeMeasures()`](moduleStreamBase.html#music21.stream.base.Stream.makeMeasures "music21.stream.base.Stream.makeMeasures") * [`makeMutable()`](moduleStreamBase.html#music21.stream.base.Stream.makeMutable "music21.stream.base.Stream.makeMutable") * [`makeNotation()`](moduleStreamBase.html#music21.stream.base.Stream.makeNotation "music21.stream.base.Stream.makeNotation") * [`makeRests()`](moduleStreamBase.html#music21.stream.base.Stream.makeRests "music21.stream.base.Stream.makeRests") * [`makeTies()`](moduleStreamBase.html#music21.stream.base.Stream.makeTies "music21.stream.base.Stream.makeTies") * [`makeVoices()`](moduleStreamBase.html#music21.stream.base.Stream.makeVoices "music21.stream.base.Stream.makeVoices") * [`measure()`](moduleStreamBase.html#music21.stream.base.Stream.measure "music21.stream.base.Stream.measure") * [`measureOffsetMap()`](moduleStreamBase.html#music21.stream.base.Stream.measureOffsetMap "music21.stream.base.Stream.measureOffsetMap") * [`measures()`](moduleStreamBase.html#music21.stream.base.Stream.measures "music21.stream.base.Stream.measures") * [`melodicIntervals()`](moduleStreamBase.html#music21.stream.base.Stream.melodicIntervals "music21.stream.base.Stream.melodicIntervals") * [`mergeAttributes()`](moduleStreamBase.html#music21.stream.base.Stream.mergeAttributes "music21.stream.base.Stream.mergeAttributes") * [`mergeElements()`](moduleStreamBase.html#music21.stream.base.Stream.mergeElements "music21.stream.base.Stream.mergeElements") * [`metronomeMarkBoundaries()`](moduleStreamBase.html#music21.stream.base.Stream.metronomeMarkBoundaries "music21.stream.base.Stream.metronomeMarkBoundaries") * [`offsetMap()`](moduleStreamBase.html#music21.stream.base.Stream.offsetMap "music21.stream.base.Stream.offsetMap") | * [`playingWhenAttacked()`](moduleStreamBase.html#music21.stream.base.Stream.playingWhenAttacked "music21.stream.base.Stream.playingWhenAttacked") * [`plot()`](moduleStreamBase.html#music21.stream.base.Stream.plot "music21.stream.base.Stream.plot") * [`pop()`](moduleStreamBase.html#music21.stream.base.Stream.pop "music21.stream.base.Stream.pop") * [`quantize()`](moduleStreamBase.html#music21.stream.base.Stream.quantize "music21.stream.base.Stream.quantize") * [`recurse()`](moduleStreamBase.html#music21.stream.base.Stream.recurse "music21.stream.base.Stream.recurse") * [`recurseRepr()`](moduleStreamBase.html#music21.stream.base.Stream.recurseRepr "music21.stream.base.Stream.recurseRepr") * [`remove()`](moduleStreamBase.html#music21.stream.base.Stream.remove "music21.stream.base.Stream.remove") * [`removeByClass()`](moduleStreamBase.html#music21.stream.base.Stream.removeByClass "music21.stream.base.Stream.removeByClass") * [`removeByNotOfClass()`](moduleStreamBase.html#music21.stream.base.Stream.removeByNotOfClass "music21.stream.base.Stream.removeByNotOfClass") * [`repeatAppend()`](moduleStreamBase.html#music21.stream.base.Stream.repeatAppend "music21.stream.base.Stream.repeatAppend") * [`repeatInsert()`](moduleStreamBase.html#music21.stream.base.Stream.repeatInsert "music21.stream.base.Stream.repeatInsert") * [`replace()`](moduleStreamBase.html#music21.stream.base.Stream.replace "music21.stream.base.Stream.replace") * [`scaleDurations()`](moduleStreamBase.html#music21.stream.base.Stream.scaleDurations "music21.stream.base.Stream.scaleDurations") * [`scaleOffsets()`](moduleStreamBase.html#music21.stream.base.Stream.scaleOffsets "music21.stream.base.Stream.scaleOffsets") * [`setDerivationMethod()`](moduleStreamBase.html#music21.stream.base.Stream.setDerivationMethod "music21.stream.base.Stream.setDerivationMethod") * [`setElementOffset()`](moduleStreamBase.html#music21.stream.base.Stream.setElementOffset "music21.stream.base.Stream.setElementOffset") * [`shiftElements()`](moduleStreamBase.html#music21.stream.base.Stream.shiftElements "music21.stream.base.Stream.shiftElements") * [`showVariantAsOssialikePart()`](moduleStreamBase.html#music21.stream.base.Stream.showVariantAsOssialikePart "music21.stream.base.Stream.showVariantAsOssialikePart") * [`simultaneousAttacks()`](moduleStreamBase.html#music21.stream.base.Stream.simultaneousAttacks "music21.stream.base.Stream.simultaneousAttacks") * [`sliceAtOffsets()`](moduleStreamBase.html#music21.stream.base.Stream.sliceAtOffsets "music21.stream.base.Stream.sliceAtOffsets") * [`sliceByBeat()`](moduleStreamBase.html#music21.stream.base.Stream.sliceByBeat "music21.stream.base.Stream.sliceByBeat") * [`sliceByGreatestDivisor()`](moduleStreamBase.html#music21.stream.base.Stream.sliceByGreatestDivisor "music21.stream.base.Stream.sliceByGreatestDivisor") * [`sliceByQuarterLengths()`](moduleStreamBase.html#music21.stream.base.Stream.sliceByQuarterLengths "music21.stream.base.Stream.sliceByQuarterLengths") * [`sort()`](moduleStreamBase.html#music21.stream.base.Stream.sort "music21.stream.base.Stream.sort") * [`sorted()`](moduleStreamBase.html#music21.stream.base.Stream.sorted "music21.stream.base.Stream.sorted") * [`splitAtDurations()`](moduleStreamBase.html#music21.stream.base.Stream.splitAtDurations "music21.stream.base.Stream.splitAtDurations") * [`splitAtQuarterLength()`](moduleStreamBase.html#music21.stream.base.Stream.splitAtQuarterLength "music21.stream.base.Stream.splitAtQuarterLength") * [`splitByClass()`](moduleStreamBase.html#music21.stream.base.Stream.splitByClass "music21.stream.base.Stream.splitByClass") * [`storeAtEnd()`](moduleStreamBase.html#music21.stream.base.Stream.storeAtEnd "music21.stream.base.Stream.storeAtEnd") * [`stripTies()`](moduleStreamBase.html#music21.stream.base.Stream.stripTies "music21.stream.base.Stream.stripTies") * [`template()`](moduleStreamBase.html#music21.stream.base.Stream.template "music21.stream.base.Stream.template") * [`toSoundingPitch()`](moduleStreamBase.html#music21.stream.base.Stream.toSoundingPitch "music21.stream.base.Stream.toSoundingPitch") * [`toWrittenPitch()`](moduleStreamBase.html#music21.stream.base.Stream.toWrittenPitch "music21.stream.base.Stream.toWrittenPitch") * [`transferOffsetToElements()`](moduleStreamBase.html#music21.stream.base.Stream.transferOffsetToElements "music21.stream.base.Stream.transferOffsetToElements") * [`transpose()`](moduleStreamBase.html#music21.stream.base.Stream.transpose "music21.stream.base.Stream.transpose") * [`voicesToParts()`](moduleStreamBase.html#music21.stream.base.Stream.voicesToParts "music21.stream.base.Stream.voicesToParts") |

Methods inherited from [`StreamCore`](moduleStreamCore.html#music21.stream.core.StreamCore "music21.stream.core.StreamCore"):

|  |  |  |
| --- | --- | --- |
| * [`asTimespans()`](moduleStreamCore.html#music21.stream.core.StreamCore.asTimespans "music21.stream.core.StreamCore.asTimespans") * [`asTree()`](moduleStreamCore.html#music21.stream.core.StreamCore.asTree "music21.stream.core.StreamCore.asTree") * [`coreAppend()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreAppend "music21.stream.core.StreamCore.coreAppend") * [`coreCopyAsDerivation()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreCopyAsDerivation "music21.stream.core.StreamCore.coreCopyAsDerivation") | * [`coreElementsChanged()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreElementsChanged "music21.stream.core.StreamCore.coreElementsChanged") * [`coreGatherMissingSpanners()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreGatherMissingSpanners "music21.stream.core.StreamCore.coreGatherMissingSpanners") * [`coreGetElementByMemoryLocation()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreGetElementByMemoryLocation "music21.stream.core.StreamCore.coreGetElementByMemoryLocation") * [`coreGuardBeforeAddElement()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreGuardBeforeAddElement "music21.stream.core.StreamCore.coreGuardBeforeAddElement") | * [`coreInsert()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreInsert "music21.stream.core.StreamCore.coreInsert") * [`coreSelfActiveSite()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreSelfActiveSite "music21.stream.core.StreamCore.coreSelfActiveSite") * [`coreSetElementOffset()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreSetElementOffset "music21.stream.core.StreamCore.coreSetElementOffset") * [`coreStoreAtEnd()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreStoreAtEnd "music21.stream.core.StreamCore.coreStoreAtEnd") |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") | * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") | * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") |

[`LayoutScore`](#music21.layout.LayoutScore "music21.layout.LayoutScore") instance variables

Instance variables inherited from [`Stream`](moduleStreamBase.html#music21.stream.base.Stream "music21.stream.base.Stream"):

|  |  |  |
| --- | --- | --- |
| * [`autoSort`](moduleStreamBase.html#music21.stream.base.Stream.autoSort "music21.stream.base.Stream.autoSort") * [`definesExplicitPageBreaks`](moduleStreamBase.html#music21.stream.base.Stream.definesExplicitPageBreaks "music21.stream.base.Stream.definesExplicitPageBreaks") | * [`definesExplicitSystemBreaks`](moduleStreamBase.html#music21.stream.base.Stream.definesExplicitSystemBreaks "music21.stream.base.Stream.definesExplicitSystemBreaks") * [`isFlat`](moduleStreamBase.html#music21.stream.base.Stream.isFlat "music21.stream.base.Stream.isFlat") | * [`isSorted`](moduleStreamBase.html#music21.stream.base.Stream.isSorted "music21.stream.base.Stream.isSorted") * [`recursionType`](moduleStreamBase.html#music21.stream.base.Stream.recursionType "music21.stream.base.Stream.recursionType") |

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## Page

class music21.layout.Page(*givenElements=None*, *\*\*keywords*)[[source]](../_modules/music21/layout.html#Page)
:   Designation that all the music in this Stream
    belongs on a single notated page.

[`Page`](#music21.layout.Page "music21.layout.Page") bases

* [`Opus`](moduleStreamBase.html#music21.stream.base.Opus "music21.stream.base.Opus")
* [`Stream`](moduleStreamBase.html#music21.stream.base.Stream "music21.stream.base.Stream")
* [`StreamCore`](moduleStreamCore.html#music21.stream.core.StreamCore "music21.stream.core.StreamCore")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`Page`](#music21.layout.Page "music21.layout.Page") read-only properties

Page.systems

Read-only properties inherited from [`Opus`](moduleStreamBase.html#music21.stream.base.Opus "music21.stream.base.Opus"):

|  |  |  |
| --- | --- | --- |
| * [`scores`](moduleStreamBase.html#music21.stream.base.Opus.scores "music21.stream.base.Opus.scores") |  |  |

Read-only properties inherited from [`Stream`](moduleStreamBase.html#music21.stream.base.Stream "music21.stream.base.Stream"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleStreamBase.html#music21.stream.base.Stream.beat "music21.stream.base.Stream.beat") * [`beatDuration`](moduleStreamBase.html#music21.stream.base.Stream.beatDuration "music21.stream.base.Stream.beatDuration") * [`beatStr`](moduleStreamBase.html#music21.stream.base.Stream.beatStr "music21.stream.base.Stream.beatStr") * [`beatStrength`](moduleStreamBase.html#music21.stream.base.Stream.beatStrength "music21.stream.base.Stream.beatStrength") * [`highestOffset`](moduleStreamBase.html#music21.stream.base.Stream.highestOffset "music21.stream.base.Stream.highestOffset") | * [`highestTime`](moduleStreamBase.html#music21.stream.base.Stream.highestTime "music21.stream.base.Stream.highestTime") * [`isGapless`](moduleStreamBase.html#music21.stream.base.Stream.isGapless "music21.stream.base.Stream.isGapless") * [`lowestOffset`](moduleStreamBase.html#music21.stream.base.Stream.lowestOffset "music21.stream.base.Stream.lowestOffset") * [`notes`](moduleStreamBase.html#music21.stream.base.Stream.notes "music21.stream.base.Stream.notes") * [`notesAndRests`](moduleStreamBase.html#music21.stream.base.Stream.notesAndRests "music21.stream.base.Stream.notesAndRests") | * [`pitches`](moduleStreamBase.html#music21.stream.base.Stream.pitches "music21.stream.base.Stream.pitches") * [`secondsMap`](moduleStreamBase.html#music21.stream.base.Stream.secondsMap "music21.stream.base.Stream.secondsMap") * [`spanners`](moduleStreamBase.html#music21.stream.base.Stream.spanners "music21.stream.base.Stream.spanners") * [`voices`](moduleStreamBase.html#music21.stream.base.Stream.voices "music21.stream.base.Stream.voices") |

Read-only properties inherited from [`StreamCore`](moduleStreamCore.html#music21.stream.core.StreamCore "music21.stream.core.StreamCore"):

|  |  |  |
| --- | --- | --- |
| * [`spannerBundle`](moduleStreamCore.html#music21.stream.core.StreamCore.spannerBundle "music21.stream.core.StreamCore.spannerBundle") |  |  |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") | * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`Page`](#music21.layout.Page "music21.layout.Page") read/write properties

Read/write properties inherited from [`Stream`](moduleStreamBase.html#music21.stream.base.Stream "music21.stream.base.Stream"):

|  |  |  |
| --- | --- | --- |
| * [`atSoundingPitch`](moduleStreamBase.html#music21.stream.base.Stream.atSoundingPitch "music21.stream.base.Stream.atSoundingPitch") * [`clef`](moduleStreamBase.html#music21.stream.base.Stream.clef "music21.stream.base.Stream.clef") * [`duration`](moduleStreamBase.html#music21.stream.base.Stream.duration "music21.stream.base.Stream.duration") * [`elements`](moduleStreamBase.html#music21.stream.base.Stream.elements "music21.stream.base.Stream.elements") | * [`finalBarline`](moduleStreamBase.html#music21.stream.base.Stream.finalBarline "music21.stream.base.Stream.finalBarline") * [`keySignature`](moduleStreamBase.html#music21.stream.base.Stream.keySignature "music21.stream.base.Stream.keySignature") * [`metadata`](moduleStreamBase.html#music21.stream.base.Stream.metadata "music21.stream.base.Stream.metadata") | * [`seconds`](moduleStreamBase.html#music21.stream.base.Stream.seconds "music21.stream.base.Stream.seconds") * [`staffLines`](moduleStreamBase.html#music21.stream.base.Stream.staffLines "music21.stream.base.Stream.staffLines") * [`timeSignature`](moduleStreamBase.html#music21.stream.base.Stream.timeSignature "music21.stream.base.Stream.timeSignature") |

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`Page`](#music21.layout.Page "music21.layout.Page") methods

Page.show(*fmt=None*, *app=None*, *\*\*keywords*)[[source]](../_modules/music21/layout.html#Page.show)
:   Borrows stream.Score.show

    ```python
    >>> ls = layout.System()
    >>> lp = layout.Page()
    >>> lp.append(ls)
    >>> lp.show('text')
    {0.0} <music21.layout.System 0: p.0, sys.0>
    ```

Methods inherited from [`Opus`](moduleStreamBase.html#music21.stream.base.Opus "music21.stream.base.Opus"):

|  |  |  |
| --- | --- | --- |
| * [`getNumbers()`](moduleStreamBase.html#music21.stream.base.Opus.getNumbers "music21.stream.base.Opus.getNumbers") * [`getScoreByNumber()`](moduleStreamBase.html#music21.stream.base.Opus.getScoreByNumber "music21.stream.base.Opus.getScoreByNumber") | * [`getScoreByTitle()`](moduleStreamBase.html#music21.stream.base.Opus.getScoreByTitle "music21.stream.base.Opus.getScoreByTitle") * [`mergeScores()`](moduleStreamBase.html#music21.stream.base.Opus.mergeScores "music21.stream.base.Opus.mergeScores") | * [`write()`](moduleStreamBase.html#music21.stream.base.Opus.write "music21.stream.base.Opus.write") |

Methods inherited from [`Stream`](moduleStreamBase.html#music21.stream.base.Stream "music21.stream.base.Stream"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleStreamBase.html#music21.stream.base.Stream.__eq__ "music21.stream.base.Stream.__eq__") * [`__getitem__()`](moduleStreamBase.html#music21.stream.base.Stream.__getitem__ "music21.stream.base.Stream.__getitem__") * [`activateVariants()`](moduleStreamBase.html#music21.stream.base.Stream.activateVariants "music21.stream.base.Stream.activateVariants") * [`addGroupForElements()`](moduleStreamBase.html#music21.stream.base.Stream.addGroupForElements "music21.stream.base.Stream.addGroupForElements") * [`allPlayingWhileSounding()`](moduleStreamBase.html#music21.stream.base.Stream.allPlayingWhileSounding "music21.stream.base.Stream.allPlayingWhileSounding") * [`analyze()`](moduleStreamBase.html#music21.stream.base.Stream.analyze "music21.stream.base.Stream.analyze") * [`append()`](moduleStreamBase.html#music21.stream.base.Stream.append "music21.stream.base.Stream.append") * [`attachIntervalsBetweenStreams()`](moduleStreamBase.html#music21.stream.base.Stream.attachIntervalsBetweenStreams "music21.stream.base.Stream.attachIntervalsBetweenStreams") * [`attachMelodicIntervals()`](moduleStreamBase.html#music21.stream.base.Stream.attachMelodicIntervals "music21.stream.base.Stream.attachMelodicIntervals") * [`augmentOrDiminish()`](moduleStreamBase.html#music21.stream.base.Stream.augmentOrDiminish "music21.stream.base.Stream.augmentOrDiminish") * [`beatAndMeasureFromOffset()`](moduleStreamBase.html#music21.stream.base.Stream.beatAndMeasureFromOffset "music21.stream.base.Stream.beatAndMeasureFromOffset") * [`chordify()`](moduleStreamBase.html#music21.stream.base.Stream.chordify "music21.stream.base.Stream.chordify") * [`clear()`](moduleStreamBase.html#music21.stream.base.Stream.clear "music21.stream.base.Stream.clear") * [`cloneEmpty()`](moduleStreamBase.html#music21.stream.base.Stream.cloneEmpty "music21.stream.base.Stream.cloneEmpty") * [`containerInHierarchy()`](moduleStreamBase.html#music21.stream.base.Stream.containerInHierarchy "music21.stream.base.Stream.containerInHierarchy") * [`elementOffset()`](moduleStreamBase.html#music21.stream.base.Stream.elementOffset "music21.stream.base.Stream.elementOffset") * [`expandRepeats()`](moduleStreamBase.html#music21.stream.base.Stream.expandRepeats "music21.stream.base.Stream.expandRepeats") * [`explode()`](moduleStreamBase.html#music21.stream.base.Stream.explode "music21.stream.base.Stream.explode") * [`extendDuration()`](moduleStreamBase.html#music21.stream.base.Stream.extendDuration "music21.stream.base.Stream.extendDuration") * [`extendTies()`](moduleStreamBase.html#music21.stream.base.Stream.extendTies "music21.stream.base.Stream.extendTies") * [`extractContext()`](moduleStreamBase.html#music21.stream.base.Stream.extractContext "music21.stream.base.Stream.extractContext") * [`findConsecutiveNotes()`](moduleStreamBase.html#music21.stream.base.Stream.findConsecutiveNotes "music21.stream.base.Stream.findConsecutiveNotes") * [`findGaps()`](moduleStreamBase.html#music21.stream.base.Stream.findGaps "music21.stream.base.Stream.findGaps") * [`first()`](moduleStreamBase.html#music21.stream.base.Stream.first "music21.stream.base.Stream.first") * [`flatten()`](moduleStreamBase.html#music21.stream.base.Stream.flatten "music21.stream.base.Stream.flatten") * [`flattenUnnecessaryVoices()`](moduleStreamBase.html#music21.stream.base.Stream.flattenUnnecessaryVoices "music21.stream.base.Stream.flattenUnnecessaryVoices") * [`getElementAfterElement()`](moduleStreamBase.html#music21.stream.base.Stream.getElementAfterElement "music21.stream.base.Stream.getElementAfterElement") * [`getElementAtOrBefore()`](moduleStreamBase.html#music21.stream.base.Stream.getElementAtOrBefore "music21.stream.base.Stream.getElementAtOrBefore") * [`getElementBeforeOffset()`](moduleStreamBase.html#music21.stream.base.Stream.getElementBeforeOffset "music21.stream.base.Stream.getElementBeforeOffset") * [`getElementById()`](moduleStreamBase.html#music21.stream.base.Stream.getElementById "music21.stream.base.Stream.getElementById") * [`getElementsByClass()`](moduleStreamBase.html#music21.stream.base.Stream.getElementsByClass "music21.stream.base.Stream.getElementsByClass") * [`getElementsByGroup()`](moduleStreamBase.html#music21.stream.base.Stream.getElementsByGroup "music21.stream.base.Stream.getElementsByGroup") * [`getElementsByOffset()`](moduleStreamBase.html#music21.stream.base.Stream.getElementsByOffset "music21.stream.base.Stream.getElementsByOffset") * [`getElementsNotOfClass()`](moduleStreamBase.html#music21.stream.base.Stream.getElementsNotOfClass "music21.stream.base.Stream.getElementsNotOfClass") * [`getInstrument()`](moduleStreamBase.html#music21.stream.base.Stream.getInstrument "music21.stream.base.Stream.getInstrument") * [`getInstruments()`](moduleStreamBase.html#music21.stream.base.Stream.getInstruments "music21.stream.base.Stream.getInstruments") | * [`getOverlaps()`](moduleStreamBase.html#music21.stream.base.Stream.getOverlaps "music21.stream.base.Stream.getOverlaps") * [`getTimeSignatures()`](moduleStreamBase.html#music21.stream.base.Stream.getTimeSignatures "music21.stream.base.Stream.getTimeSignatures") * [`hasElement()`](moduleStreamBase.html#music21.stream.base.Stream.hasElement "music21.stream.base.Stream.hasElement") * [`hasElementOfClass()`](moduleStreamBase.html#music21.stream.base.Stream.hasElementOfClass "music21.stream.base.Stream.hasElementOfClass") * [`hasMeasures()`](moduleStreamBase.html#music21.stream.base.Stream.hasMeasures "music21.stream.base.Stream.hasMeasures") * [`hasPartLikeStreams()`](moduleStreamBase.html#music21.stream.base.Stream.hasPartLikeStreams "music21.stream.base.Stream.hasPartLikeStreams") * [`hasVoices()`](moduleStreamBase.html#music21.stream.base.Stream.hasVoices "music21.stream.base.Stream.hasVoices") * [`haveAccidentalsBeenMade()`](moduleStreamBase.html#music21.stream.base.Stream.haveAccidentalsBeenMade "music21.stream.base.Stream.haveAccidentalsBeenMade") * [`index()`](moduleStreamBase.html#music21.stream.base.Stream.index "music21.stream.base.Stream.index") * [`insert()`](moduleStreamBase.html#music21.stream.base.Stream.insert "music21.stream.base.Stream.insert") * [`insertAndShift()`](moduleStreamBase.html#music21.stream.base.Stream.insertAndShift "music21.stream.base.Stream.insertAndShift") * [`insertIntoNoteOrChord()`](moduleStreamBase.html#music21.stream.base.Stream.insertIntoNoteOrChord "music21.stream.base.Stream.insertIntoNoteOrChord") * [`invertDiatonic()`](moduleStreamBase.html#music21.stream.base.Stream.invertDiatonic "music21.stream.base.Stream.invertDiatonic") * [`isSequence()`](moduleStreamBase.html#music21.stream.base.Stream.isSequence "music21.stream.base.Stream.isSequence") * [`isTwelveTone()`](moduleStreamBase.html#music21.stream.base.Stream.isTwelveTone "music21.stream.base.Stream.isTwelveTone") * [`isWellFormedNotation()`](moduleStreamBase.html#music21.stream.base.Stream.isWellFormedNotation "music21.stream.base.Stream.isWellFormedNotation") * [`iter()`](moduleStreamBase.html#music21.stream.base.Stream.iter "music21.stream.base.Stream.iter") * [`last()`](moduleStreamBase.html#music21.stream.base.Stream.last "music21.stream.base.Stream.last") * [`lyrics()`](moduleStreamBase.html#music21.stream.base.Stream.lyrics "music21.stream.base.Stream.lyrics") * [`makeAccidentals()`](moduleStreamBase.html#music21.stream.base.Stream.makeAccidentals "music21.stream.base.Stream.makeAccidentals") * [`makeBeams()`](moduleStreamBase.html#music21.stream.base.Stream.makeBeams "music21.stream.base.Stream.makeBeams") * [`makeImmutable()`](moduleStreamBase.html#music21.stream.base.Stream.makeImmutable "music21.stream.base.Stream.makeImmutable") * [`makeMeasures()`](moduleStreamBase.html#music21.stream.base.Stream.makeMeasures "music21.stream.base.Stream.makeMeasures") * [`makeMutable()`](moduleStreamBase.html#music21.stream.base.Stream.makeMutable "music21.stream.base.Stream.makeMutable") * [`makeNotation()`](moduleStreamBase.html#music21.stream.base.Stream.makeNotation "music21.stream.base.Stream.makeNotation") * [`makeRests()`](moduleStreamBase.html#music21.stream.base.Stream.makeRests "music21.stream.base.Stream.makeRests") * [`makeTies()`](moduleStreamBase.html#music21.stream.base.Stream.makeTies "music21.stream.base.Stream.makeTies") * [`makeVoices()`](moduleStreamBase.html#music21.stream.base.Stream.makeVoices "music21.stream.base.Stream.makeVoices") * [`measure()`](moduleStreamBase.html#music21.stream.base.Stream.measure "music21.stream.base.Stream.measure") * [`measureOffsetMap()`](moduleStreamBase.html#music21.stream.base.Stream.measureOffsetMap "music21.stream.base.Stream.measureOffsetMap") * [`measures()`](moduleStreamBase.html#music21.stream.base.Stream.measures "music21.stream.base.Stream.measures") * [`melodicIntervals()`](moduleStreamBase.html#music21.stream.base.Stream.melodicIntervals "music21.stream.base.Stream.melodicIntervals") * [`mergeAttributes()`](moduleStreamBase.html#music21.stream.base.Stream.mergeAttributes "music21.stream.base.Stream.mergeAttributes") * [`mergeElements()`](moduleStreamBase.html#music21.stream.base.Stream.mergeElements "music21.stream.base.Stream.mergeElements") * [`metronomeMarkBoundaries()`](moduleStreamBase.html#music21.stream.base.Stream.metronomeMarkBoundaries "music21.stream.base.Stream.metronomeMarkBoundaries") * [`offsetMap()`](moduleStreamBase.html#music21.stream.base.Stream.offsetMap "music21.stream.base.Stream.offsetMap") | * [`playingWhenAttacked()`](moduleStreamBase.html#music21.stream.base.Stream.playingWhenAttacked "music21.stream.base.Stream.playingWhenAttacked") * [`plot()`](moduleStreamBase.html#music21.stream.base.Stream.plot "music21.stream.base.Stream.plot") * [`pop()`](moduleStreamBase.html#music21.stream.base.Stream.pop "music21.stream.base.Stream.pop") * [`quantize()`](moduleStreamBase.html#music21.stream.base.Stream.quantize "music21.stream.base.Stream.quantize") * [`recurse()`](moduleStreamBase.html#music21.stream.base.Stream.recurse "music21.stream.base.Stream.recurse") * [`recurseRepr()`](moduleStreamBase.html#music21.stream.base.Stream.recurseRepr "music21.stream.base.Stream.recurseRepr") * [`remove()`](moduleStreamBase.html#music21.stream.base.Stream.remove "music21.stream.base.Stream.remove") * [`removeByClass()`](moduleStreamBase.html#music21.stream.base.Stream.removeByClass "music21.stream.base.Stream.removeByClass") * [`removeByNotOfClass()`](moduleStreamBase.html#music21.stream.base.Stream.removeByNotOfClass "music21.stream.base.Stream.removeByNotOfClass") * [`repeatAppend()`](moduleStreamBase.html#music21.stream.base.Stream.repeatAppend "music21.stream.base.Stream.repeatAppend") * [`repeatInsert()`](moduleStreamBase.html#music21.stream.base.Stream.repeatInsert "music21.stream.base.Stream.repeatInsert") * [`replace()`](moduleStreamBase.html#music21.stream.base.Stream.replace "music21.stream.base.Stream.replace") * [`scaleDurations()`](moduleStreamBase.html#music21.stream.base.Stream.scaleDurations "music21.stream.base.Stream.scaleDurations") * [`scaleOffsets()`](moduleStreamBase.html#music21.stream.base.Stream.scaleOffsets "music21.stream.base.Stream.scaleOffsets") * [`setDerivationMethod()`](moduleStreamBase.html#music21.stream.base.Stream.setDerivationMethod "music21.stream.base.Stream.setDerivationMethod") * [`setElementOffset()`](moduleStreamBase.html#music21.stream.base.Stream.setElementOffset "music21.stream.base.Stream.setElementOffset") * [`shiftElements()`](moduleStreamBase.html#music21.stream.base.Stream.shiftElements "music21.stream.base.Stream.shiftElements") * [`showVariantAsOssialikePart()`](moduleStreamBase.html#music21.stream.base.Stream.showVariantAsOssialikePart "music21.stream.base.Stream.showVariantAsOssialikePart") * [`simultaneousAttacks()`](moduleStreamBase.html#music21.stream.base.Stream.simultaneousAttacks "music21.stream.base.Stream.simultaneousAttacks") * [`sliceAtOffsets()`](moduleStreamBase.html#music21.stream.base.Stream.sliceAtOffsets "music21.stream.base.Stream.sliceAtOffsets") * [`sliceByBeat()`](moduleStreamBase.html#music21.stream.base.Stream.sliceByBeat "music21.stream.base.Stream.sliceByBeat") * [`sliceByGreatestDivisor()`](moduleStreamBase.html#music21.stream.base.Stream.sliceByGreatestDivisor "music21.stream.base.Stream.sliceByGreatestDivisor") * [`sliceByQuarterLengths()`](moduleStreamBase.html#music21.stream.base.Stream.sliceByQuarterLengths "music21.stream.base.Stream.sliceByQuarterLengths") * [`sort()`](moduleStreamBase.html#music21.stream.base.Stream.sort "music21.stream.base.Stream.sort") * [`sorted()`](moduleStreamBase.html#music21.stream.base.Stream.sorted "music21.stream.base.Stream.sorted") * [`splitAtDurations()`](moduleStreamBase.html#music21.stream.base.Stream.splitAtDurations "music21.stream.base.Stream.splitAtDurations") * [`splitAtQuarterLength()`](moduleStreamBase.html#music21.stream.base.Stream.splitAtQuarterLength "music21.stream.base.Stream.splitAtQuarterLength") * [`splitByClass()`](moduleStreamBase.html#music21.stream.base.Stream.splitByClass "music21.stream.base.Stream.splitByClass") * [`storeAtEnd()`](moduleStreamBase.html#music21.stream.base.Stream.storeAtEnd "music21.stream.base.Stream.storeAtEnd") * [`stripTies()`](moduleStreamBase.html#music21.stream.base.Stream.stripTies "music21.stream.base.Stream.stripTies") * [`template()`](moduleStreamBase.html#music21.stream.base.Stream.template "music21.stream.base.Stream.template") * [`toSoundingPitch()`](moduleStreamBase.html#music21.stream.base.Stream.toSoundingPitch "music21.stream.base.Stream.toSoundingPitch") * [`toWrittenPitch()`](moduleStreamBase.html#music21.stream.base.Stream.toWrittenPitch "music21.stream.base.Stream.toWrittenPitch") * [`transferOffsetToElements()`](moduleStreamBase.html#music21.stream.base.Stream.transferOffsetToElements "music21.stream.base.Stream.transferOffsetToElements") * [`transpose()`](moduleStreamBase.html#music21.stream.base.Stream.transpose "music21.stream.base.Stream.transpose") * [`voicesToParts()`](moduleStreamBase.html#music21.stream.base.Stream.voicesToParts "music21.stream.base.Stream.voicesToParts") |

Methods inherited from [`StreamCore`](moduleStreamCore.html#music21.stream.core.StreamCore "music21.stream.core.StreamCore"):

|  |  |  |
| --- | --- | --- |
| * [`asTimespans()`](moduleStreamCore.html#music21.stream.core.StreamCore.asTimespans "music21.stream.core.StreamCore.asTimespans") * [`asTree()`](moduleStreamCore.html#music21.stream.core.StreamCore.asTree "music21.stream.core.StreamCore.asTree") * [`coreAppend()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreAppend "music21.stream.core.StreamCore.coreAppend") * [`coreCopyAsDerivation()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreCopyAsDerivation "music21.stream.core.StreamCore.coreCopyAsDerivation") | * [`coreElementsChanged()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreElementsChanged "music21.stream.core.StreamCore.coreElementsChanged") * [`coreGatherMissingSpanners()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreGatherMissingSpanners "music21.stream.core.StreamCore.coreGatherMissingSpanners") * [`coreGetElementByMemoryLocation()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreGetElementByMemoryLocation "music21.stream.core.StreamCore.coreGetElementByMemoryLocation") * [`coreGuardBeforeAddElement()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreGuardBeforeAddElement "music21.stream.core.StreamCore.coreGuardBeforeAddElement") | * [`coreInsert()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreInsert "music21.stream.core.StreamCore.coreInsert") * [`coreSelfActiveSite()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreSelfActiveSite "music21.stream.core.StreamCore.coreSelfActiveSite") * [`coreSetElementOffset()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreSetElementOffset "music21.stream.core.StreamCore.coreSetElementOffset") * [`coreStoreAtEnd()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreStoreAtEnd "music21.stream.core.StreamCore.coreStoreAtEnd") |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") | * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") | * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") |

[`Page`](#music21.layout.Page "music21.layout.Page") instance variables

Instance variables inherited from [`Stream`](moduleStreamBase.html#music21.stream.base.Stream "music21.stream.base.Stream"):

|  |  |  |
| --- | --- | --- |
| * [`autoSort`](moduleStreamBase.html#music21.stream.base.Stream.autoSort "music21.stream.base.Stream.autoSort") * [`definesExplicitPageBreaks`](moduleStreamBase.html#music21.stream.base.Stream.definesExplicitPageBreaks "music21.stream.base.Stream.definesExplicitPageBreaks") | * [`definesExplicitSystemBreaks`](moduleStreamBase.html#music21.stream.base.Stream.definesExplicitSystemBreaks "music21.stream.base.Stream.definesExplicitSystemBreaks") * [`isFlat`](moduleStreamBase.html#music21.stream.base.Stream.isFlat "music21.stream.base.Stream.isFlat") | * [`isSorted`](moduleStreamBase.html#music21.stream.base.Stream.isSorted "music21.stream.base.Stream.isSorted") * [`recursionType`](moduleStreamBase.html#music21.stream.base.Stream.recursionType "music21.stream.base.Stream.recursionType") |

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## System

class music21.layout.System(*givenElements=None*, *\*\*keywords*)[[source]](../_modules/music21/layout.html#System)
:   Designation that all the music in this Stream
    belongs on a single notated system.

    Attribute systemNumbering says at what point the numbering of
    systems resets. It can be either “Score” (default), “Opus”, or “Page”.

[`System`](#music21.layout.System "music21.layout.System") bases

* [`Score`](moduleStreamBase.html#music21.stream.base.Score "music21.stream.base.Score")
* [`Stream`](moduleStreamBase.html#music21.stream.base.Stream "music21.stream.base.Stream")
* [`StreamCore`](moduleStreamCore.html#music21.stream.core.StreamCore "music21.stream.core.StreamCore")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`System`](#music21.layout.System "music21.layout.System") read-only properties

System.staves

Read-only properties inherited from [`Score`](moduleStreamBase.html#music21.stream.base.Score "music21.stream.base.Score"):

|  |  |  |
| --- | --- | --- |
| * [`parts`](moduleStreamBase.html#music21.stream.base.Score.parts "music21.stream.base.Score.parts") |  |  |

Read-only properties inherited from [`Stream`](moduleStreamBase.html#music21.stream.base.Stream "music21.stream.base.Stream"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleStreamBase.html#music21.stream.base.Stream.beat "music21.stream.base.Stream.beat") * [`beatDuration`](moduleStreamBase.html#music21.stream.base.Stream.beatDuration "music21.stream.base.Stream.beatDuration") * [`beatStr`](moduleStreamBase.html#music21.stream.base.Stream.beatStr "music21.stream.base.Stream.beatStr") * [`beatStrength`](moduleStreamBase.html#music21.stream.base.Stream.beatStrength "music21.stream.base.Stream.beatStrength") * [`highestOffset`](moduleStreamBase.html#music21.stream.base.Stream.highestOffset "music21.stream.base.Stream.highestOffset") | * [`highestTime`](moduleStreamBase.html#music21.stream.base.Stream.highestTime "music21.stream.base.Stream.highestTime") * [`isGapless`](moduleStreamBase.html#music21.stream.base.Stream.isGapless "music21.stream.base.Stream.isGapless") * [`lowestOffset`](moduleStreamBase.html#music21.stream.base.Stream.lowestOffset "music21.stream.base.Stream.lowestOffset") * [`notes`](moduleStreamBase.html#music21.stream.base.Stream.notes "music21.stream.base.Stream.notes") * [`notesAndRests`](moduleStreamBase.html#music21.stream.base.Stream.notesAndRests "music21.stream.base.Stream.notesAndRests") | * [`pitches`](moduleStreamBase.html#music21.stream.base.Stream.pitches "music21.stream.base.Stream.pitches") * [`secondsMap`](moduleStreamBase.html#music21.stream.base.Stream.secondsMap "music21.stream.base.Stream.secondsMap") * [`spanners`](moduleStreamBase.html#music21.stream.base.Stream.spanners "music21.stream.base.Stream.spanners") * [`voices`](moduleStreamBase.html#music21.stream.base.Stream.voices "music21.stream.base.Stream.voices") |

Read-only properties inherited from [`StreamCore`](moduleStreamCore.html#music21.stream.core.StreamCore "music21.stream.core.StreamCore"):

|  |  |  |
| --- | --- | --- |
| * [`spannerBundle`](moduleStreamCore.html#music21.stream.core.StreamCore.spannerBundle "music21.stream.core.StreamCore.spannerBundle") |  |  |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") | * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`System`](#music21.layout.System "music21.layout.System") read/write properties

Read/write properties inherited from [`Stream`](moduleStreamBase.html#music21.stream.base.Stream "music21.stream.base.Stream"):

|  |  |  |
| --- | --- | --- |
| * [`atSoundingPitch`](moduleStreamBase.html#music21.stream.base.Stream.atSoundingPitch "music21.stream.base.Stream.atSoundingPitch") * [`clef`](moduleStreamBase.html#music21.stream.base.Stream.clef "music21.stream.base.Stream.clef") * [`duration`](moduleStreamBase.html#music21.stream.base.Stream.duration "music21.stream.base.Stream.duration") * [`elements`](moduleStreamBase.html#music21.stream.base.Stream.elements "music21.stream.base.Stream.elements") | * [`finalBarline`](moduleStreamBase.html#music21.stream.base.Stream.finalBarline "music21.stream.base.Stream.finalBarline") * [`keySignature`](moduleStreamBase.html#music21.stream.base.Stream.keySignature "music21.stream.base.Stream.keySignature") * [`metadata`](moduleStreamBase.html#music21.stream.base.Stream.metadata "music21.stream.base.Stream.metadata") | * [`seconds`](moduleStreamBase.html#music21.stream.base.Stream.seconds "music21.stream.base.Stream.seconds") * [`staffLines`](moduleStreamBase.html#music21.stream.base.Stream.staffLines "music21.stream.base.Stream.staffLines") * [`timeSignature`](moduleStreamBase.html#music21.stream.base.Stream.timeSignature "music21.stream.base.Stream.timeSignature") |

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`System`](#music21.layout.System "music21.layout.System") methods

Methods inherited from [`Score`](moduleStreamBase.html#music21.stream.base.Score "music21.stream.base.Score"):

|  |  |  |
| --- | --- | --- |
| * [`expandRepeats()`](moduleStreamBase.html#music21.stream.base.Score.expandRepeats "music21.stream.base.Score.expandRepeats") * [`implode()`](moduleStreamBase.html#music21.stream.base.Score.implode "music21.stream.base.Score.implode") * [`makeNotation()`](moduleStreamBase.html#music21.stream.base.Score.makeNotation "music21.stream.base.Score.makeNotation") | * [`measure()`](moduleStreamBase.html#music21.stream.base.Score.measure "music21.stream.base.Score.measure") * [`measureOffsetMap()`](moduleStreamBase.html#music21.stream.base.Score.measureOffsetMap "music21.stream.base.Score.measureOffsetMap") * [`measures()`](moduleStreamBase.html#music21.stream.base.Score.measures "music21.stream.base.Score.measures") | * [`partsToVoices()`](moduleStreamBase.html#music21.stream.base.Score.partsToVoices "music21.stream.base.Score.partsToVoices") * [`sliceByGreatestDivisor()`](moduleStreamBase.html#music21.stream.base.Score.sliceByGreatestDivisor "music21.stream.base.Score.sliceByGreatestDivisor") |

Methods inherited from [`Stream`](moduleStreamBase.html#music21.stream.base.Stream "music21.stream.base.Stream"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleStreamBase.html#music21.stream.base.Stream.__eq__ "music21.stream.base.Stream.__eq__") * [`__getitem__()`](moduleStreamBase.html#music21.stream.base.Stream.__getitem__ "music21.stream.base.Stream.__getitem__") * [`activateVariants()`](moduleStreamBase.html#music21.stream.base.Stream.activateVariants "music21.stream.base.Stream.activateVariants") * [`addGroupForElements()`](moduleStreamBase.html#music21.stream.base.Stream.addGroupForElements "music21.stream.base.Stream.addGroupForElements") * [`allPlayingWhileSounding()`](moduleStreamBase.html#music21.stream.base.Stream.allPlayingWhileSounding "music21.stream.base.Stream.allPlayingWhileSounding") * [`analyze()`](moduleStreamBase.html#music21.stream.base.Stream.analyze "music21.stream.base.Stream.analyze") * [`append()`](moduleStreamBase.html#music21.stream.base.Stream.append "music21.stream.base.Stream.append") * [`attachIntervalsBetweenStreams()`](moduleStreamBase.html#music21.stream.base.Stream.attachIntervalsBetweenStreams "music21.stream.base.Stream.attachIntervalsBetweenStreams") * [`attachMelodicIntervals()`](moduleStreamBase.html#music21.stream.base.Stream.attachMelodicIntervals "music21.stream.base.Stream.attachMelodicIntervals") * [`augmentOrDiminish()`](moduleStreamBase.html#music21.stream.base.Stream.augmentOrDiminish "music21.stream.base.Stream.augmentOrDiminish") * [`beatAndMeasureFromOffset()`](moduleStreamBase.html#music21.stream.base.Stream.beatAndMeasureFromOffset "music21.stream.base.Stream.beatAndMeasureFromOffset") * [`chordify()`](moduleStreamBase.html#music21.stream.base.Stream.chordify "music21.stream.base.Stream.chordify") * [`clear()`](moduleStreamBase.html#music21.stream.base.Stream.clear "music21.stream.base.Stream.clear") * [`cloneEmpty()`](moduleStreamBase.html#music21.stream.base.Stream.cloneEmpty "music21.stream.base.Stream.cloneEmpty") * [`containerInHierarchy()`](moduleStreamBase.html#music21.stream.base.Stream.containerInHierarchy "music21.stream.base.Stream.containerInHierarchy") * [`elementOffset()`](moduleStreamBase.html#music21.stream.base.Stream.elementOffset "music21.stream.base.Stream.elementOffset") * [`explode()`](moduleStreamBase.html#music21.stream.base.Stream.explode "music21.stream.base.Stream.explode") * [`extendDuration()`](moduleStreamBase.html#music21.stream.base.Stream.extendDuration "music21.stream.base.Stream.extendDuration") * [`extendTies()`](moduleStreamBase.html#music21.stream.base.Stream.extendTies "music21.stream.base.Stream.extendTies") * [`extractContext()`](moduleStreamBase.html#music21.stream.base.Stream.extractContext "music21.stream.base.Stream.extractContext") * [`findConsecutiveNotes()`](moduleStreamBase.html#music21.stream.base.Stream.findConsecutiveNotes "music21.stream.base.Stream.findConsecutiveNotes") * [`findGaps()`](moduleStreamBase.html#music21.stream.base.Stream.findGaps "music21.stream.base.Stream.findGaps") * [`first()`](moduleStreamBase.html#music21.stream.base.Stream.first "music21.stream.base.Stream.first") * [`flatten()`](moduleStreamBase.html#music21.stream.base.Stream.flatten "music21.stream.base.Stream.flatten") * [`flattenUnnecessaryVoices()`](moduleStreamBase.html#music21.stream.base.Stream.flattenUnnecessaryVoices "music21.stream.base.Stream.flattenUnnecessaryVoices") * [`getElementAfterElement()`](moduleStreamBase.html#music21.stream.base.Stream.getElementAfterElement "music21.stream.base.Stream.getElementAfterElement") * [`getElementAtOrBefore()`](moduleStreamBase.html#music21.stream.base.Stream.getElementAtOrBefore "music21.stream.base.Stream.getElementAtOrBefore") * [`getElementBeforeOffset()`](moduleStreamBase.html#music21.stream.base.Stream.getElementBeforeOffset "music21.stream.base.Stream.getElementBeforeOffset") * [`getElementById()`](moduleStreamBase.html#music21.stream.base.Stream.getElementById "music21.stream.base.Stream.getElementById") * [`getElementsByClass()`](moduleStreamBase.html#music21.stream.base.Stream.getElementsByClass "music21.stream.base.Stream.getElementsByClass") * [`getElementsByGroup()`](moduleStreamBase.html#music21.stream.base.Stream.getElementsByGroup "music21.stream.base.Stream.getElementsByGroup") * [`getElementsByOffset()`](moduleStreamBase.html#music21.stream.base.Stream.getElementsByOffset "music21.stream.base.Stream.getElementsByOffset") * [`getElementsNotOfClass()`](moduleStreamBase.html#music21.stream.base.Stream.getElementsNotOfClass "music21.stream.base.Stream.getElementsNotOfClass") * [`getInstrument()`](moduleStreamBase.html#music21.stream.base.Stream.getInstrument "music21.stream.base.Stream.getInstrument") * [`getInstruments()`](moduleStreamBase.html#music21.stream.base.Stream.getInstruments "music21.stream.base.Stream.getInstruments") | * [`getOverlaps()`](moduleStreamBase.html#music21.stream.base.Stream.getOverlaps "music21.stream.base.Stream.getOverlaps") * [`getTimeSignatures()`](moduleStreamBase.html#music21.stream.base.Stream.getTimeSignatures "music21.stream.base.Stream.getTimeSignatures") * [`hasElement()`](moduleStreamBase.html#music21.stream.base.Stream.hasElement "music21.stream.base.Stream.hasElement") * [`hasElementOfClass()`](moduleStreamBase.html#music21.stream.base.Stream.hasElementOfClass "music21.stream.base.Stream.hasElementOfClass") * [`hasMeasures()`](moduleStreamBase.html#music21.stream.base.Stream.hasMeasures "music21.stream.base.Stream.hasMeasures") * [`hasPartLikeStreams()`](moduleStreamBase.html#music21.stream.base.Stream.hasPartLikeStreams "music21.stream.base.Stream.hasPartLikeStreams") * [`hasVoices()`](moduleStreamBase.html#music21.stream.base.Stream.hasVoices "music21.stream.base.Stream.hasVoices") * [`haveAccidentalsBeenMade()`](moduleStreamBase.html#music21.stream.base.Stream.haveAccidentalsBeenMade "music21.stream.base.Stream.haveAccidentalsBeenMade") * [`index()`](moduleStreamBase.html#music21.stream.base.Stream.index "music21.stream.base.Stream.index") * [`insert()`](moduleStreamBase.html#music21.stream.base.Stream.insert "music21.stream.base.Stream.insert") * [`insertAndShift()`](moduleStreamBase.html#music21.stream.base.Stream.insertAndShift "music21.stream.base.Stream.insertAndShift") * [`insertIntoNoteOrChord()`](moduleStreamBase.html#music21.stream.base.Stream.insertIntoNoteOrChord "music21.stream.base.Stream.insertIntoNoteOrChord") * [`invertDiatonic()`](moduleStreamBase.html#music21.stream.base.Stream.invertDiatonic "music21.stream.base.Stream.invertDiatonic") * [`isSequence()`](moduleStreamBase.html#music21.stream.base.Stream.isSequence "music21.stream.base.Stream.isSequence") * [`isTwelveTone()`](moduleStreamBase.html#music21.stream.base.Stream.isTwelveTone "music21.stream.base.Stream.isTwelveTone") * [`isWellFormedNotation()`](moduleStreamBase.html#music21.stream.base.Stream.isWellFormedNotation "music21.stream.base.Stream.isWellFormedNotation") * [`iter()`](moduleStreamBase.html#music21.stream.base.Stream.iter "music21.stream.base.Stream.iter") * [`last()`](moduleStreamBase.html#music21.stream.base.Stream.last "music21.stream.base.Stream.last") * [`lyrics()`](moduleStreamBase.html#music21.stream.base.Stream.lyrics "music21.stream.base.Stream.lyrics") * [`makeAccidentals()`](moduleStreamBase.html#music21.stream.base.Stream.makeAccidentals "music21.stream.base.Stream.makeAccidentals") * [`makeBeams()`](moduleStreamBase.html#music21.stream.base.Stream.makeBeams "music21.stream.base.Stream.makeBeams") * [`makeImmutable()`](moduleStreamBase.html#music21.stream.base.Stream.makeImmutable "music21.stream.base.Stream.makeImmutable") * [`makeMeasures()`](moduleStreamBase.html#music21.stream.base.Stream.makeMeasures "music21.stream.base.Stream.makeMeasures") * [`makeMutable()`](moduleStreamBase.html#music21.stream.base.Stream.makeMutable "music21.stream.base.Stream.makeMutable") * [`makeRests()`](moduleStreamBase.html#music21.stream.base.Stream.makeRests "music21.stream.base.Stream.makeRests") * [`makeTies()`](moduleStreamBase.html#music21.stream.base.Stream.makeTies "music21.stream.base.Stream.makeTies") * [`makeVoices()`](moduleStreamBase.html#music21.stream.base.Stream.makeVoices "music21.stream.base.Stream.makeVoices") * [`melodicIntervals()`](moduleStreamBase.html#music21.stream.base.Stream.melodicIntervals "music21.stream.base.Stream.melodicIntervals") * [`mergeAttributes()`](moduleStreamBase.html#music21.stream.base.Stream.mergeAttributes "music21.stream.base.Stream.mergeAttributes") * [`mergeElements()`](moduleStreamBase.html#music21.stream.base.Stream.mergeElements "music21.stream.base.Stream.mergeElements") * [`metronomeMarkBoundaries()`](moduleStreamBase.html#music21.stream.base.Stream.metronomeMarkBoundaries "music21.stream.base.Stream.metronomeMarkBoundaries") * [`offsetMap()`](moduleStreamBase.html#music21.stream.base.Stream.offsetMap "music21.stream.base.Stream.offsetMap") * [`playingWhenAttacked()`](moduleStreamBase.html#music21.stream.base.Stream.playingWhenAttacked "music21.stream.base.Stream.playingWhenAttacked") * [`plot()`](moduleStreamBase.html#music21.stream.base.Stream.plot "music21.stream.base.Stream.plot") * [`pop()`](moduleStreamBase.html#music21.stream.base.Stream.pop "music21.stream.base.Stream.pop") | * [`quantize()`](moduleStreamBase.html#music21.stream.base.Stream.quantize "music21.stream.base.Stream.quantize") * [`recurse()`](moduleStreamBase.html#music21.stream.base.Stream.recurse "music21.stream.base.Stream.recurse") * [`recurseRepr()`](moduleStreamBase.html#music21.stream.base.Stream.recurseRepr "music21.stream.base.Stream.recurseRepr") * [`remove()`](moduleStreamBase.html#music21.stream.base.Stream.remove "music21.stream.base.Stream.remove") * [`removeByClass()`](moduleStreamBase.html#music21.stream.base.Stream.removeByClass "music21.stream.base.Stream.removeByClass") * [`removeByNotOfClass()`](moduleStreamBase.html#music21.stream.base.Stream.removeByNotOfClass "music21.stream.base.Stream.removeByNotOfClass") * [`repeatAppend()`](moduleStreamBase.html#music21.stream.base.Stream.repeatAppend "music21.stream.base.Stream.repeatAppend") * [`repeatInsert()`](moduleStreamBase.html#music21.stream.base.Stream.repeatInsert "music21.stream.base.Stream.repeatInsert") * [`replace()`](moduleStreamBase.html#music21.stream.base.Stream.replace "music21.stream.base.Stream.replace") * [`scaleDurations()`](moduleStreamBase.html#music21.stream.base.Stream.scaleDurations "music21.stream.base.Stream.scaleDurations") * [`scaleOffsets()`](moduleStreamBase.html#music21.stream.base.Stream.scaleOffsets "music21.stream.base.Stream.scaleOffsets") * [`setDerivationMethod()`](moduleStreamBase.html#music21.stream.base.Stream.setDerivationMethod "music21.stream.base.Stream.setDerivationMethod") * [`setElementOffset()`](moduleStreamBase.html#music21.stream.base.Stream.setElementOffset "music21.stream.base.Stream.setElementOffset") * [`shiftElements()`](moduleStreamBase.html#music21.stream.base.Stream.shiftElements "music21.stream.base.Stream.shiftElements") * [`show()`](moduleStreamBase.html#music21.stream.base.Stream.show "music21.stream.base.Stream.show") * [`showVariantAsOssialikePart()`](moduleStreamBase.html#music21.stream.base.Stream.showVariantAsOssialikePart "music21.stream.base.Stream.showVariantAsOssialikePart") * [`simultaneousAttacks()`](moduleStreamBase.html#music21.stream.base.Stream.simultaneousAttacks "music21.stream.base.Stream.simultaneousAttacks") * [`sliceAtOffsets()`](moduleStreamBase.html#music21.stream.base.Stream.sliceAtOffsets "music21.stream.base.Stream.sliceAtOffsets") * [`sliceByBeat()`](moduleStreamBase.html#music21.stream.base.Stream.sliceByBeat "music21.stream.base.Stream.sliceByBeat") * [`sliceByQuarterLengths()`](moduleStreamBase.html#music21.stream.base.Stream.sliceByQuarterLengths "music21.stream.base.Stream.sliceByQuarterLengths") * [`sort()`](moduleStreamBase.html#music21.stream.base.Stream.sort "music21.stream.base.Stream.sort") * [`sorted()`](moduleStreamBase.html#music21.stream.base.Stream.sorted "music21.stream.base.Stream.sorted") * [`splitAtDurations()`](moduleStreamBase.html#music21.stream.base.Stream.splitAtDurations "music21.stream.base.Stream.splitAtDurations") * [`splitAtQuarterLength()`](moduleStreamBase.html#music21.stream.base.Stream.splitAtQuarterLength "music21.stream.base.Stream.splitAtQuarterLength") * [`splitByClass()`](moduleStreamBase.html#music21.stream.base.Stream.splitByClass "music21.stream.base.Stream.splitByClass") * [`storeAtEnd()`](moduleStreamBase.html#music21.stream.base.Stream.storeAtEnd "music21.stream.base.Stream.storeAtEnd") * [`stripTies()`](moduleStreamBase.html#music21.stream.base.Stream.stripTies "music21.stream.base.Stream.stripTies") * [`template()`](moduleStreamBase.html#music21.stream.base.Stream.template "music21.stream.base.Stream.template") * [`toSoundingPitch()`](moduleStreamBase.html#music21.stream.base.Stream.toSoundingPitch "music21.stream.base.Stream.toSoundingPitch") * [`toWrittenPitch()`](moduleStreamBase.html#music21.stream.base.Stream.toWrittenPitch "music21.stream.base.Stream.toWrittenPitch") * [`transferOffsetToElements()`](moduleStreamBase.html#music21.stream.base.Stream.transferOffsetToElements "music21.stream.base.Stream.transferOffsetToElements") * [`transpose()`](moduleStreamBase.html#music21.stream.base.Stream.transpose "music21.stream.base.Stream.transpose") * [`voicesToParts()`](moduleStreamBase.html#music21.stream.base.Stream.voicesToParts "music21.stream.base.Stream.voicesToParts") * [`write()`](moduleStreamBase.html#music21.stream.base.Stream.write "music21.stream.base.Stream.write") |

Methods inherited from [`StreamCore`](moduleStreamCore.html#music21.stream.core.StreamCore "music21.stream.core.StreamCore"):

|  |  |  |
| --- | --- | --- |
| * [`asTimespans()`](moduleStreamCore.html#music21.stream.core.StreamCore.asTimespans "music21.stream.core.StreamCore.asTimespans") * [`asTree()`](moduleStreamCore.html#music21.stream.core.StreamCore.asTree "music21.stream.core.StreamCore.asTree") * [`coreAppend()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreAppend "music21.stream.core.StreamCore.coreAppend") * [`coreCopyAsDerivation()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreCopyAsDerivation "music21.stream.core.StreamCore.coreCopyAsDerivation") | * [`coreElementsChanged()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreElementsChanged "music21.stream.core.StreamCore.coreElementsChanged") * [`coreGatherMissingSpanners()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreGatherMissingSpanners "music21.stream.core.StreamCore.coreGatherMissingSpanners") * [`coreGetElementByMemoryLocation()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreGetElementByMemoryLocation "music21.stream.core.StreamCore.coreGetElementByMemoryLocation") * [`coreGuardBeforeAddElement()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreGuardBeforeAddElement "music21.stream.core.StreamCore.coreGuardBeforeAddElement") | * [`coreInsert()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreInsert "music21.stream.core.StreamCore.coreInsert") * [`coreSelfActiveSite()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreSelfActiveSite "music21.stream.core.StreamCore.coreSelfActiveSite") * [`coreSetElementOffset()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreSetElementOffset "music21.stream.core.StreamCore.coreSetElementOffset") * [`coreStoreAtEnd()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreStoreAtEnd "music21.stream.core.StreamCore.coreStoreAtEnd") |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") | * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") | * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") |

[`System`](#music21.layout.System "music21.layout.System") instance variables

Instance variables inherited from [`Stream`](moduleStreamBase.html#music21.stream.base.Stream "music21.stream.base.Stream"):

|  |  |  |
| --- | --- | --- |
| * [`autoSort`](moduleStreamBase.html#music21.stream.base.Stream.autoSort "music21.stream.base.Stream.autoSort") * [`definesExplicitPageBreaks`](moduleStreamBase.html#music21.stream.base.Stream.definesExplicitPageBreaks "music21.stream.base.Stream.definesExplicitPageBreaks") | * [`definesExplicitSystemBreaks`](moduleStreamBase.html#music21.stream.base.Stream.definesExplicitSystemBreaks "music21.stream.base.Stream.definesExplicitSystemBreaks") * [`isFlat`](moduleStreamBase.html#music21.stream.base.Stream.isFlat "music21.stream.base.Stream.isFlat") | * [`isSorted`](moduleStreamBase.html#music21.stream.base.Stream.isSorted "music21.stream.base.Stream.isSorted") * [`recursionType`](moduleStreamBase.html#music21.stream.base.Stream.recursionType "music21.stream.base.Stream.recursionType") |

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## Staff

class music21.layout.Staff(*givenElements=None*, *\*\*keywords*)[[source]](../_modules/music21/layout.html#Staff)
:   Designation that all the music in this Stream
    belongs on a single Staff.

[`Staff`](#music21.layout.Staff "music21.layout.Staff") bases

* [`Part`](moduleStreamBase.html#music21.stream.base.Part "music21.stream.base.Part")
* [`Stream`](moduleStreamBase.html#music21.stream.base.Stream "music21.stream.base.Stream")
* [`StreamCore`](moduleStreamCore.html#music21.stream.core.StreamCore "music21.stream.core.StreamCore")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`Staff`](#music21.layout.Staff "music21.layout.Staff") read-only properties

Read-only properties inherited from [`Stream`](moduleStreamBase.html#music21.stream.base.Stream "music21.stream.base.Stream"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleStreamBase.html#music21.stream.base.Stream.beat "music21.stream.base.Stream.beat") * [`beatDuration`](moduleStreamBase.html#music21.stream.base.Stream.beatDuration "music21.stream.base.Stream.beatDuration") * [`beatStr`](moduleStreamBase.html#music21.stream.base.Stream.beatStr "music21.stream.base.Stream.beatStr") * [`beatStrength`](moduleStreamBase.html#music21.stream.base.Stream.beatStrength "music21.stream.base.Stream.beatStrength") * [`highestOffset`](moduleStreamBase.html#music21.stream.base.Stream.highestOffset "music21.stream.base.Stream.highestOffset") | * [`highestTime`](moduleStreamBase.html#music21.stream.base.Stream.highestTime "music21.stream.base.Stream.highestTime") * [`isGapless`](moduleStreamBase.html#music21.stream.base.Stream.isGapless "music21.stream.base.Stream.isGapless") * [`lowestOffset`](moduleStreamBase.html#music21.stream.base.Stream.lowestOffset "music21.stream.base.Stream.lowestOffset") * [`notes`](moduleStreamBase.html#music21.stream.base.Stream.notes "music21.stream.base.Stream.notes") * [`notesAndRests`](moduleStreamBase.html#music21.stream.base.Stream.notesAndRests "music21.stream.base.Stream.notesAndRests") | * [`pitches`](moduleStreamBase.html#music21.stream.base.Stream.pitches "music21.stream.base.Stream.pitches") * [`secondsMap`](moduleStreamBase.html#music21.stream.base.Stream.secondsMap "music21.stream.base.Stream.secondsMap") * [`spanners`](moduleStreamBase.html#music21.stream.base.Stream.spanners "music21.stream.base.Stream.spanners") * [`voices`](moduleStreamBase.html#music21.stream.base.Stream.voices "music21.stream.base.Stream.voices") |

Read-only properties inherited from [`StreamCore`](moduleStreamCore.html#music21.stream.core.StreamCore "music21.stream.core.StreamCore"):

|  |  |  |
| --- | --- | --- |
| * [`spannerBundle`](moduleStreamCore.html#music21.stream.core.StreamCore.spannerBundle "music21.stream.core.StreamCore.spannerBundle") |  |  |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") | * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`Staff`](#music21.layout.Staff "music21.layout.Staff") read/write properties

Read/write properties inherited from [`Part`](moduleStreamBase.html#music21.stream.base.Part "music21.stream.base.Part"):

|  |  |  |
| --- | --- | --- |
| * [`partAbbreviation`](moduleStreamBase.html#music21.stream.base.Part.partAbbreviation "music21.stream.base.Part.partAbbreviation") | * [`partName`](moduleStreamBase.html#music21.stream.base.Part.partName "music21.stream.base.Part.partName") |  |

Read/write properties inherited from [`Stream`](moduleStreamBase.html#music21.stream.base.Stream "music21.stream.base.Stream"):

|  |  |  |
| --- | --- | --- |
| * [`atSoundingPitch`](moduleStreamBase.html#music21.stream.base.Stream.atSoundingPitch "music21.stream.base.Stream.atSoundingPitch") * [`clef`](moduleStreamBase.html#music21.stream.base.Stream.clef "music21.stream.base.Stream.clef") * [`duration`](moduleStreamBase.html#music21.stream.base.Stream.duration "music21.stream.base.Stream.duration") * [`elements`](moduleStreamBase.html#music21.stream.base.Stream.elements "music21.stream.base.Stream.elements") | * [`finalBarline`](moduleStreamBase.html#music21.stream.base.Stream.finalBarline "music21.stream.base.Stream.finalBarline") * [`keySignature`](moduleStreamBase.html#music21.stream.base.Stream.keySignature "music21.stream.base.Stream.keySignature") * [`metadata`](moduleStreamBase.html#music21.stream.base.Stream.metadata "music21.stream.base.Stream.metadata") | * [`seconds`](moduleStreamBase.html#music21.stream.base.Stream.seconds "music21.stream.base.Stream.seconds") * [`staffLines`](moduleStreamBase.html#music21.stream.base.Stream.staffLines "music21.stream.base.Stream.staffLines") * [`timeSignature`](moduleStreamBase.html#music21.stream.base.Stream.timeSignature "music21.stream.base.Stream.timeSignature") |

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`Staff`](#music21.layout.Staff "music21.layout.Staff") methods

Methods inherited from [`Part`](moduleStreamBase.html#music21.stream.base.Part "music21.stream.base.Part"):

|  |  |  |
| --- | --- | --- |
| * [`makeAccidentals()`](moduleStreamBase.html#music21.stream.base.Part.makeAccidentals "music21.stream.base.Part.makeAccidentals") | * [`mergeAttributes()`](moduleStreamBase.html#music21.stream.base.Part.mergeAttributes "music21.stream.base.Part.mergeAttributes") |  |

Methods inherited from [`Stream`](moduleStreamBase.html#music21.stream.base.Stream "music21.stream.base.Stream"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleStreamBase.html#music21.stream.base.Stream.__eq__ "music21.stream.base.Stream.__eq__") * [`__getitem__()`](moduleStreamBase.html#music21.stream.base.Stream.__getitem__ "music21.stream.base.Stream.__getitem__") * [`activateVariants()`](moduleStreamBase.html#music21.stream.base.Stream.activateVariants "music21.stream.base.Stream.activateVariants") * [`addGroupForElements()`](moduleStreamBase.html#music21.stream.base.Stream.addGroupForElements "music21.stream.base.Stream.addGroupForElements") * [`allPlayingWhileSounding()`](moduleStreamBase.html#music21.stream.base.Stream.allPlayingWhileSounding "music21.stream.base.Stream.allPlayingWhileSounding") * [`analyze()`](moduleStreamBase.html#music21.stream.base.Stream.analyze "music21.stream.base.Stream.analyze") * [`append()`](moduleStreamBase.html#music21.stream.base.Stream.append "music21.stream.base.Stream.append") * [`attachIntervalsBetweenStreams()`](moduleStreamBase.html#music21.stream.base.Stream.attachIntervalsBetweenStreams "music21.stream.base.Stream.attachIntervalsBetweenStreams") * [`attachMelodicIntervals()`](moduleStreamBase.html#music21.stream.base.Stream.attachMelodicIntervals "music21.stream.base.Stream.attachMelodicIntervals") * [`augmentOrDiminish()`](moduleStreamBase.html#music21.stream.base.Stream.augmentOrDiminish "music21.stream.base.Stream.augmentOrDiminish") * [`beatAndMeasureFromOffset()`](moduleStreamBase.html#music21.stream.base.Stream.beatAndMeasureFromOffset "music21.stream.base.Stream.beatAndMeasureFromOffset") * [`chordify()`](moduleStreamBase.html#music21.stream.base.Stream.chordify "music21.stream.base.Stream.chordify") * [`clear()`](moduleStreamBase.html#music21.stream.base.Stream.clear "music21.stream.base.Stream.clear") * [`cloneEmpty()`](moduleStreamBase.html#music21.stream.base.Stream.cloneEmpty "music21.stream.base.Stream.cloneEmpty") * [`containerInHierarchy()`](moduleStreamBase.html#music21.stream.base.Stream.containerInHierarchy "music21.stream.base.Stream.containerInHierarchy") * [`elementOffset()`](moduleStreamBase.html#music21.stream.base.Stream.elementOffset "music21.stream.base.Stream.elementOffset") * [`expandRepeats()`](moduleStreamBase.html#music21.stream.base.Stream.expandRepeats "music21.stream.base.Stream.expandRepeats") * [`explode()`](moduleStreamBase.html#music21.stream.base.Stream.explode "music21.stream.base.Stream.explode") * [`extendDuration()`](moduleStreamBase.html#music21.stream.base.Stream.extendDuration "music21.stream.base.Stream.extendDuration") * [`extendTies()`](moduleStreamBase.html#music21.stream.base.Stream.extendTies "music21.stream.base.Stream.extendTies") * [`extractContext()`](moduleStreamBase.html#music21.stream.base.Stream.extractContext "music21.stream.base.Stream.extractContext") * [`findConsecutiveNotes()`](moduleStreamBase.html#music21.stream.base.Stream.findConsecutiveNotes "music21.stream.base.Stream.findConsecutiveNotes") * [`findGaps()`](moduleStreamBase.html#music21.stream.base.Stream.findGaps "music21.stream.base.Stream.findGaps") * [`first()`](moduleStreamBase.html#music21.stream.base.Stream.first "music21.stream.base.Stream.first") * [`flatten()`](moduleStreamBase.html#music21.stream.base.Stream.flatten "music21.stream.base.Stream.flatten") * [`flattenUnnecessaryVoices()`](moduleStreamBase.html#music21.stream.base.Stream.flattenUnnecessaryVoices "music21.stream.base.Stream.flattenUnnecessaryVoices") * [`getElementAfterElement()`](moduleStreamBase.html#music21.stream.base.Stream.getElementAfterElement "music21.stream.base.Stream.getElementAfterElement") * [`getElementAtOrBefore()`](moduleStreamBase.html#music21.stream.base.Stream.getElementAtOrBefore "music21.stream.base.Stream.getElementAtOrBefore") * [`getElementBeforeOffset()`](moduleStreamBase.html#music21.stream.base.Stream.getElementBeforeOffset "music21.stream.base.Stream.getElementBeforeOffset") * [`getElementById()`](moduleStreamBase.html#music21.stream.base.Stream.getElementById "music21.stream.base.Stream.getElementById") * [`getElementsByClass()`](moduleStreamBase.html#music21.stream.base.Stream.getElementsByClass "music21.stream.base.Stream.getElementsByClass") * [`getElementsByGroup()`](moduleStreamBase.html#music21.stream.base.Stream.getElementsByGroup "music21.stream.base.Stream.getElementsByGroup") * [`getElementsByOffset()`](moduleStreamBase.html#music21.stream.base.Stream.getElementsByOffset "music21.stream.base.Stream.getElementsByOffset") * [`getElementsNotOfClass()`](moduleStreamBase.html#music21.stream.base.Stream.getElementsNotOfClass "music21.stream.base.Stream.getElementsNotOfClass") * [`getInstrument()`](moduleStreamBase.html#music21.stream.base.Stream.getInstrument "music21.stream.base.Stream.getInstrument") * [`getInstruments()`](moduleStreamBase.html#music21.stream.base.Stream.getInstruments "music21.stream.base.Stream.getInstruments") | * [`getOverlaps()`](moduleStreamBase.html#music21.stream.base.Stream.getOverlaps "music21.stream.base.Stream.getOverlaps") * [`getTimeSignatures()`](moduleStreamBase.html#music21.stream.base.Stream.getTimeSignatures "music21.stream.base.Stream.getTimeSignatures") * [`hasElement()`](moduleStreamBase.html#music21.stream.base.Stream.hasElement "music21.stream.base.Stream.hasElement") * [`hasElementOfClass()`](moduleStreamBase.html#music21.stream.base.Stream.hasElementOfClass "music21.stream.base.Stream.hasElementOfClass") * [`hasMeasures()`](moduleStreamBase.html#music21.stream.base.Stream.hasMeasures "music21.stream.base.Stream.hasMeasures") * [`hasPartLikeStreams()`](moduleStreamBase.html#music21.stream.base.Stream.hasPartLikeStreams "music21.stream.base.Stream.hasPartLikeStreams") * [`hasVoices()`](moduleStreamBase.html#music21.stream.base.Stream.hasVoices "music21.stream.base.Stream.hasVoices") * [`haveAccidentalsBeenMade()`](moduleStreamBase.html#music21.stream.base.Stream.haveAccidentalsBeenMade "music21.stream.base.Stream.haveAccidentalsBeenMade") * [`index()`](moduleStreamBase.html#music21.stream.base.Stream.index "music21.stream.base.Stream.index") * [`insert()`](moduleStreamBase.html#music21.stream.base.Stream.insert "music21.stream.base.Stream.insert") * [`insertAndShift()`](moduleStreamBase.html#music21.stream.base.Stream.insertAndShift "music21.stream.base.Stream.insertAndShift") * [`insertIntoNoteOrChord()`](moduleStreamBase.html#music21.stream.base.Stream.insertIntoNoteOrChord "music21.stream.base.Stream.insertIntoNoteOrChord") * [`invertDiatonic()`](moduleStreamBase.html#music21.stream.base.Stream.invertDiatonic "music21.stream.base.Stream.invertDiatonic") * [`isSequence()`](moduleStreamBase.html#music21.stream.base.Stream.isSequence "music21.stream.base.Stream.isSequence") * [`isTwelveTone()`](moduleStreamBase.html#music21.stream.base.Stream.isTwelveTone "music21.stream.base.Stream.isTwelveTone") * [`isWellFormedNotation()`](moduleStreamBase.html#music21.stream.base.Stream.isWellFormedNotation "music21.stream.base.Stream.isWellFormedNotation") * [`iter()`](moduleStreamBase.html#music21.stream.base.Stream.iter "music21.stream.base.Stream.iter") * [`last()`](moduleStreamBase.html#music21.stream.base.Stream.last "music21.stream.base.Stream.last") * [`lyrics()`](moduleStreamBase.html#music21.stream.base.Stream.lyrics "music21.stream.base.Stream.lyrics") * [`makeBeams()`](moduleStreamBase.html#music21.stream.base.Stream.makeBeams "music21.stream.base.Stream.makeBeams") * [`makeImmutable()`](moduleStreamBase.html#music21.stream.base.Stream.makeImmutable "music21.stream.base.Stream.makeImmutable") * [`makeMeasures()`](moduleStreamBase.html#music21.stream.base.Stream.makeMeasures "music21.stream.base.Stream.makeMeasures") * [`makeMutable()`](moduleStreamBase.html#music21.stream.base.Stream.makeMutable "music21.stream.base.Stream.makeMutable") * [`makeNotation()`](moduleStreamBase.html#music21.stream.base.Stream.makeNotation "music21.stream.base.Stream.makeNotation") * [`makeRests()`](moduleStreamBase.html#music21.stream.base.Stream.makeRests "music21.stream.base.Stream.makeRests") * [`makeTies()`](moduleStreamBase.html#music21.stream.base.Stream.makeTies "music21.stream.base.Stream.makeTies") * [`makeVoices()`](moduleStreamBase.html#music21.stream.base.Stream.makeVoices "music21.stream.base.Stream.makeVoices") * [`measure()`](moduleStreamBase.html#music21.stream.base.Stream.measure "music21.stream.base.Stream.measure") * [`measureOffsetMap()`](moduleStreamBase.html#music21.stream.base.Stream.measureOffsetMap "music21.stream.base.Stream.measureOffsetMap") * [`measures()`](moduleStreamBase.html#music21.stream.base.Stream.measures "music21.stream.base.Stream.measures") * [`melodicIntervals()`](moduleStreamBase.html#music21.stream.base.Stream.melodicIntervals "music21.stream.base.Stream.melodicIntervals") * [`mergeElements()`](moduleStreamBase.html#music21.stream.base.Stream.mergeElements "music21.stream.base.Stream.mergeElements") * [`metronomeMarkBoundaries()`](moduleStreamBase.html#music21.stream.base.Stream.metronomeMarkBoundaries "music21.stream.base.Stream.metronomeMarkBoundaries") * [`offsetMap()`](moduleStreamBase.html#music21.stream.base.Stream.offsetMap "music21.stream.base.Stream.offsetMap") * [`playingWhenAttacked()`](moduleStreamBase.html#music21.stream.base.Stream.playingWhenAttacked "music21.stream.base.Stream.playingWhenAttacked") * [`plot()`](moduleStreamBase.html#music21.stream.base.Stream.plot "music21.stream.base.Stream.plot") | * [`pop()`](moduleStreamBase.html#music21.stream.base.Stream.pop "music21.stream.base.Stream.pop") * [`quantize()`](moduleStreamBase.html#music21.stream.base.Stream.quantize "music21.stream.base.Stream.quantize") * [`recurse()`](moduleStreamBase.html#music21.stream.base.Stream.recurse "music21.stream.base.Stream.recurse") * [`recurseRepr()`](moduleStreamBase.html#music21.stream.base.Stream.recurseRepr "music21.stream.base.Stream.recurseRepr") * [`remove()`](moduleStreamBase.html#music21.stream.base.Stream.remove "music21.stream.base.Stream.remove") * [`removeByClass()`](moduleStreamBase.html#music21.stream.base.Stream.removeByClass "music21.stream.base.Stream.removeByClass") * [`removeByNotOfClass()`](moduleStreamBase.html#music21.stream.base.Stream.removeByNotOfClass "music21.stream.base.Stream.removeByNotOfClass") * [`repeatAppend()`](moduleStreamBase.html#music21.stream.base.Stream.repeatAppend "music21.stream.base.Stream.repeatAppend") * [`repeatInsert()`](moduleStreamBase.html#music21.stream.base.Stream.repeatInsert "music21.stream.base.Stream.repeatInsert") * [`replace()`](moduleStreamBase.html#music21.stream.base.Stream.replace "music21.stream.base.Stream.replace") * [`scaleDurations()`](moduleStreamBase.html#music21.stream.base.Stream.scaleDurations "music21.stream.base.Stream.scaleDurations") * [`scaleOffsets()`](moduleStreamBase.html#music21.stream.base.Stream.scaleOffsets "music21.stream.base.Stream.scaleOffsets") * [`setDerivationMethod()`](moduleStreamBase.html#music21.stream.base.Stream.setDerivationMethod "music21.stream.base.Stream.setDerivationMethod") * [`setElementOffset()`](moduleStreamBase.html#music21.stream.base.Stream.setElementOffset "music21.stream.base.Stream.setElementOffset") * [`shiftElements()`](moduleStreamBase.html#music21.stream.base.Stream.shiftElements "music21.stream.base.Stream.shiftElements") * [`show()`](moduleStreamBase.html#music21.stream.base.Stream.show "music21.stream.base.Stream.show") * [`showVariantAsOssialikePart()`](moduleStreamBase.html#music21.stream.base.Stream.showVariantAsOssialikePart "music21.stream.base.Stream.showVariantAsOssialikePart") * [`simultaneousAttacks()`](moduleStreamBase.html#music21.stream.base.Stream.simultaneousAttacks "music21.stream.base.Stream.simultaneousAttacks") * [`sliceAtOffsets()`](moduleStreamBase.html#music21.stream.base.Stream.sliceAtOffsets "music21.stream.base.Stream.sliceAtOffsets") * [`sliceByBeat()`](moduleStreamBase.html#music21.stream.base.Stream.sliceByBeat "music21.stream.base.Stream.sliceByBeat") * [`sliceByGreatestDivisor()`](moduleStreamBase.html#music21.stream.base.Stream.sliceByGreatestDivisor "music21.stream.base.Stream.sliceByGreatestDivisor") * [`sliceByQuarterLengths()`](moduleStreamBase.html#music21.stream.base.Stream.sliceByQuarterLengths "music21.stream.base.Stream.sliceByQuarterLengths") * [`sort()`](moduleStreamBase.html#music21.stream.base.Stream.sort "music21.stream.base.Stream.sort") * [`sorted()`](moduleStreamBase.html#music21.stream.base.Stream.sorted "music21.stream.base.Stream.sorted") * [`splitAtDurations()`](moduleStreamBase.html#music21.stream.base.Stream.splitAtDurations "music21.stream.base.Stream.splitAtDurations") * [`splitAtQuarterLength()`](moduleStreamBase.html#music21.stream.base.Stream.splitAtQuarterLength "music21.stream.base.Stream.splitAtQuarterLength") * [`splitByClass()`](moduleStreamBase.html#music21.stream.base.Stream.splitByClass "music21.stream.base.Stream.splitByClass") * [`storeAtEnd()`](moduleStreamBase.html#music21.stream.base.Stream.storeAtEnd "music21.stream.base.Stream.storeAtEnd") * [`stripTies()`](moduleStreamBase.html#music21.stream.base.Stream.stripTies "music21.stream.base.Stream.stripTies") * [`template()`](moduleStreamBase.html#music21.stream.base.Stream.template "music21.stream.base.Stream.template") * [`toSoundingPitch()`](moduleStreamBase.html#music21.stream.base.Stream.toSoundingPitch "music21.stream.base.Stream.toSoundingPitch") * [`toWrittenPitch()`](moduleStreamBase.html#music21.stream.base.Stream.toWrittenPitch "music21.stream.base.Stream.toWrittenPitch") * [`transferOffsetToElements()`](moduleStreamBase.html#music21.stream.base.Stream.transferOffsetToElements "music21.stream.base.Stream.transferOffsetToElements") * [`transpose()`](moduleStreamBase.html#music21.stream.base.Stream.transpose "music21.stream.base.Stream.transpose") * [`voicesToParts()`](moduleStreamBase.html#music21.stream.base.Stream.voicesToParts "music21.stream.base.Stream.voicesToParts") * [`write()`](moduleStreamBase.html#music21.stream.base.Stream.write "music21.stream.base.Stream.write") |

Methods inherited from [`StreamCore`](moduleStreamCore.html#music21.stream.core.StreamCore "music21.stream.core.StreamCore"):

|  |  |  |
| --- | --- | --- |
| * [`asTimespans()`](moduleStreamCore.html#music21.stream.core.StreamCore.asTimespans "music21.stream.core.StreamCore.asTimespans") * [`asTree()`](moduleStreamCore.html#music21.stream.core.StreamCore.asTree "music21.stream.core.StreamCore.asTree") * [`coreAppend()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreAppend "music21.stream.core.StreamCore.coreAppend") * [`coreCopyAsDerivation()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreCopyAsDerivation "music21.stream.core.StreamCore.coreCopyAsDerivation") | * [`coreElementsChanged()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreElementsChanged "music21.stream.core.StreamCore.coreElementsChanged") * [`coreGatherMissingSpanners()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreGatherMissingSpanners "music21.stream.core.StreamCore.coreGatherMissingSpanners") * [`coreGetElementByMemoryLocation()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreGetElementByMemoryLocation "music21.stream.core.StreamCore.coreGetElementByMemoryLocation") * [`coreGuardBeforeAddElement()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreGuardBeforeAddElement "music21.stream.core.StreamCore.coreGuardBeforeAddElement") | * [`coreInsert()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreInsert "music21.stream.core.StreamCore.coreInsert") * [`coreSelfActiveSite()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreSelfActiveSite "music21.stream.core.StreamCore.coreSelfActiveSite") * [`coreSetElementOffset()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreSetElementOffset "music21.stream.core.StreamCore.coreSetElementOffset") * [`coreStoreAtEnd()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreStoreAtEnd "music21.stream.core.StreamCore.coreStoreAtEnd") |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") | * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") | * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") |

[`Staff`](#music21.layout.Staff "music21.layout.Staff") instance variables

Instance variables inherited from [`Stream`](moduleStreamBase.html#music21.stream.base.Stream "music21.stream.base.Stream"):

|  |  |  |
| --- | --- | --- |
| * [`autoSort`](moduleStreamBase.html#music21.stream.base.Stream.autoSort "music21.stream.base.Stream.autoSort") * [`definesExplicitPageBreaks`](moduleStreamBase.html#music21.stream.base.Stream.definesExplicitPageBreaks "music21.stream.base.Stream.definesExplicitPageBreaks") | * [`definesExplicitSystemBreaks`](moduleStreamBase.html#music21.stream.base.Stream.definesExplicitSystemBreaks "music21.stream.base.Stream.definesExplicitSystemBreaks") * [`isFlat`](moduleStreamBase.html#music21.stream.base.Stream.isFlat "music21.stream.base.Stream.isFlat") | * [`isSorted`](moduleStreamBase.html#music21.stream.base.Stream.isSorted "music21.stream.base.Stream.isSorted") * [`recursionType`](moduleStreamBase.html#music21.stream.base.Stream.recursionType "music21.stream.base.Stream.recursionType") |

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## PageSize

class music21.layout.PageSize(*top*, *left*, *right*, *bottom*, *width*, *height*)

## StaffGroup

class music21.layout.StaffGroup(*\*spannedElements*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *barTogether: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[True, False, None, 'Mensurstrich'] = True*, *abbreviation: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *symbol: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")['bracket', 'line', 'brace', 'square'] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\*\*keywords*)[[source]](../_modules/music21/layout.html#StaffGroup)
:   A StaffGroup defines a collection of one or more
    `Part` objects,
    specifying that they should be shown together with a bracket,
    brace, or other symbol, and may have a common name.

    ```python
    >>> p1 = stream.Part()
    >>> p2 = stream.Part()
    >>> p1.append(note.Note('C5', type='whole'))
    >>> p1.append(note.Note('D5', type='whole'))
    >>> p2.append(note.Note('C3', type='whole'))
    >>> p2.append(note.Note('D3', type='whole'))
    >>> p3 = stream.Part()
    >>> p3.append(note.Note('F#4', type='whole'))
    >>> p3.append(note.Note('G#4', type='whole'))
    >>> s = stream.Score()
    >>> s.insert(0, p1)
    >>> s.insert(0, p2)
    >>> s.insert(0, p3)
    >>> staffGroup1 = layout.StaffGroup([p1, p2],
    ...      name='Marimba', abbreviation='Mba.', symbol='brace')
    >>> staffGroup1.barTogether = 'Mensurstrich'
    >>> s.insert(0, staffGroup1)
    >>> staffGroup2 = layout.StaffGroup([p3],
    ...      name='Xylophone', abbreviation='Xyl.', symbol='bracket')
    >>> s.insert(0, staffGroup2)
    >>> s.show()
    ```

    [![../_images/layout_StaffGroup_01.jpg](../_images/layout_StaffGroup_01.jpg)](../_images/layout_StaffGroup_01.jpg)

[`StaffGroup`](#music21.layout.StaffGroup "music21.layout.StaffGroup") bases

* [`Spanner`](moduleSpanner.html#music21.spanner.Spanner "music21.spanner.Spanner")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`StaffGroup`](#music21.layout.StaffGroup "music21.layout.StaffGroup") read-only properties

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`StaffGroup`](#music21.layout.StaffGroup "music21.layout.StaffGroup") read/write properties

StaffGroup.barTogether
:   Get or set the barTogether value, with either Boolean values
    or yes or no strings. Or the string ‘Mensurstrich’ which
    indicates barring between staves but not in staves.

    Currently Mensurstrich is not supported by most exporters.

    ```python
    >>> sg = layout.StaffGroup()
    >>> sg.barTogether = 'yes'
    >>> sg.barTogether
    True
    >>> sg.barTogether = 'Mensurstrich'
    >>> sg.barTogether
    'Mensurstrich'
    ```

StaffGroup.symbol
:   Get or set the symbol value, with either Boolean values or yes or no strings.

    ```python
    >>> sg = layout.StaffGroup()
    >>> sg.symbol = 'Brace'
    >>> sg.symbol
    'brace'
    ```

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`StaffGroup`](#music21.layout.StaffGroup "music21.layout.StaffGroup") methods

Methods inherited from [`Spanner`](moduleSpanner.html#music21.spanner.Spanner "music21.spanner.Spanner"):

|  |  |  |
| --- | --- | --- |
| * [`__getitem__()`](moduleSpanner.html#music21.spanner.Spanner.__getitem__ "music21.spanner.Spanner.__getitem__") * [`addSpannedElements()`](moduleSpanner.html#music21.spanner.Spanner.addSpannedElements "music21.spanner.Spanner.addSpannedElements") * [`fill()`](moduleSpanner.html#music21.spanner.Spanner.fill "music21.spanner.Spanner.fill") * [`getFirst()`](moduleSpanner.html#music21.spanner.Spanner.getFirst "music21.spanner.Spanner.getFirst") * [`getLast()`](moduleSpanner.html#music21.spanner.Spanner.getLast "music21.spanner.Spanner.getLast") | * [`getSpannedElementIds()`](moduleSpanner.html#music21.spanner.Spanner.getSpannedElementIds "music21.spanner.Spanner.getSpannedElementIds") * [`getSpannedElements()`](moduleSpanner.html#music21.spanner.Spanner.getSpannedElements "music21.spanner.Spanner.getSpannedElements") * [`getSpannedElementsByClass()`](moduleSpanner.html#music21.spanner.Spanner.getSpannedElementsByClass "music21.spanner.Spanner.getSpannedElementsByClass") * [`hasSpannedElement()`](moduleSpanner.html#music21.spanner.Spanner.hasSpannedElement "music21.spanner.Spanner.hasSpannedElement") * [`insertFirstSpannedElement()`](moduleSpanner.html#music21.spanner.Spanner.insertFirstSpannedElement "music21.spanner.Spanner.insertFirstSpannedElement") | * [`isFirst()`](moduleSpanner.html#music21.spanner.Spanner.isFirst "music21.spanner.Spanner.isFirst") * [`isLast()`](moduleSpanner.html#music21.spanner.Spanner.isLast "music21.spanner.Spanner.isLast") * [`purgeLocations()`](moduleSpanner.html#music21.spanner.Spanner.purgeLocations "music21.spanner.Spanner.purgeLocations") * [`purgeOrphans()`](moduleSpanner.html#music21.spanner.Spanner.purgeOrphans "music21.spanner.Spanner.purgeOrphans") * [`replaceSpannedElement()`](moduleSpanner.html#music21.spanner.Spanner.replaceSpannedElement "music21.spanner.Spanner.replaceSpannedElement") |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") | * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") | * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`StaffGroup`](#music21.layout.StaffGroup "music21.layout.StaffGroup") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## SystemSize

class music21.layout.SystemSize(*top*, *left*, *right*, *bottom*)

## Functions

music21.layout.divideByPages(*scoreIn: [Score](moduleStreamBase.html#music21.stream.base.Score "music21.stream.base.Score")*, *printUpdates: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *fastMeasures: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*) → [LayoutScore](#music21.layout.LayoutScore "music21.layout.LayoutScore")[[source]](../_modules/music21/layout.html#divideByPages)
:   Divides a score into a series of smaller scores according to page
    breaks. Only searches for PageLayout.isNew or SystemLayout.isNew
    on the first part. Returns a new LayoutScore object.

    If fastMeasures is True, then the newly created System objects
    do not have Clef signs, Key Signatures, or necessarily all the
    applicable spanners in them. On the other hand, the position
    (on the page) information will be just as correct with
    fastMeasures = True and it will run much faster on large scores
    (because our spanner gathering algorithm is currently O(n^2);
    something TODO: to fix.)

    ```python
    >>> lt = corpus.parse('demos/layoutTest.xml')
    >>> len(lt.parts)
    3
    >>> len(lt.parts[0].getElementsByClass(stream.Measure))
    80
    ```

    Divide the score up into layout.Page objects

    ```python
    >>> layoutScore = layout.divideByPages(lt, fastMeasures=True)
    >>> len(layoutScore.pages)
    4
    >>> lastPage = layoutScore.pages[-1]
    >>> lastPage.measureStart
    64
    >>> lastPage.measureEnd
    80
    ```

    the layoutScore is a subclass of stream.Opus:

    ```python
    >>> layoutScore
    <music21.layout.LayoutScore ...>
    >>> 'Opus' in layoutScore.classes
    True
    ```

    Pages are subclasses of Opus also, since they contain Scores

    ```python
    >>> lastPage
    <music21.layout.Page ...>
    >>> 'Opus' in lastPage.classes
    True
    ```

    Each page now has Systems not parts.

    ```python
    >>> firstPage = layoutScore.pages[0]
    >>> len(firstPage.systems)
    4
    >>> firstSystem = firstPage.systems[0]
    >>> firstSystem.measureStart
    1
    >>> firstSystem.measureEnd
    5
    ```

    Systems are a subclass of Score:

    ```python
    >>> firstSystem
    <music21.layout.System ...>
    >>> isinstance(firstSystem, stream.Score)
    True
    ```

    Each System has staves (layout.Staff objects) not parts, though Staff is a subclass of Part

    ```python
    >>> secondStaff = firstSystem.staves[1]
    >>> print(len(secondStaff.getElementsByClass(stream.Measure)))
    5
    >>> secondStaff
    <music21.layout.Staff ...>
    >>> isinstance(secondStaff, stream.Part)
    True
    ```

music21.layout.getPageRegionMeasureNumbers(*scoreIn*)[[source]](../_modules/music21/layout.html#getPageRegionMeasureNumbers)

music21.layout.getRegionMeasureNumbers(*scoreIn*, *region='Page'*)[[source]](../_modules/music21/layout.html#getRegionMeasureNumbers)
:   get a list where each entry is a 2-tuplet whose first number
    refers to the first measure on a page and whose second number
    is the last measure on the page.

music21.layout.getSystemRegionMeasureNumbers(*scoreIn*)[[source]](../_modules/music21/layout.html#getSystemRegionMeasureNumbers)
