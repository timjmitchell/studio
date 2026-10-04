Source: https://music21.org/music21docs/moduleReference/moduleBar.html

# music21.bar

Object models of barlines, including repeat barlines.

## Barline

class music21.bar.Barline(*type=None*, *location=None*, *\*\*keywords*)[[source]](../_modules/music21/bar.html#Barline)
:   A representation of a barline.
    Barlines are conventionally assigned to Measure objects
    using the leftBarline and rightBarline attributes.

    ```python
    >>> bl = bar.Barline('double')
    >>> bl
    <music21.bar.Barline type=double>
    ```

    The type can also just be set via a keyword of “type”. Or if no type is specified,
    a regular barline is returned. Location can also be explicitly stored, but it’s not
    needed except for musicxml translation:

    ```python
    >>> bl2 = bar.Barline(type='dashed')
    >>> bl2
    <music21.bar.Barline type=dashed>
    >>> bl3 = bar.Barline()
    >>> bl3
    <music21.bar.Barline type=regular>
    >>> bl4 = bar.Barline(type='final', location='right')
    >>> bl4
    <music21.bar.Barline type=final>
    >>> bl4.type
    'final'
    ```

    Note that the barline type ‘ticked’ only is displayed correctly in Finale and Finale Notepad.

    N.B. for backwards compatibility reasons, currently
    Bar objects do not use the style.Style class since
    the phrase “style” was already used.

[`Barline`](#music21.bar.Barline "music21.bar.Barline") bases

* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`Barline`](#music21.bar.Barline "music21.bar.Barline") read-only properties

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`Barline`](#music21.bar.Barline "music21.bar.Barline") read/write properties

Barline.type
:   Get and set the Barline type property.

    ```python
    >>> b = bar.Barline()
    >>> b.type = 'tick'
    >>> b.type
    'tick'
    ```

    Synonyms are given for some types, based on
    musicxml styles:

    ```python
    >>> b.type = 'light-light'
    >>> b.type
    'double'
    ```

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`Barline`](#music21.bar.Barline "music21.bar.Barline") methods

Barline.musicXMLBarStyle()[[source]](../_modules/music21/bar.html#Barline.musicXMLBarStyle)
:   returns the musicxml style for the bar. most are the same as
    .type but “double” and “final” are different.

    ```python
    >>> b = bar.Barline('tick')
    >>> b.musicXMLBarStyle()
    'tick'
    ```

    ```python
    >>> b.type = 'double'
    >>> b.musicXMLBarStyle()
    'light-light'
    ```

    ```python
    >>> b.type = 'final'
    >>> b.musicXMLBarStyle()
    'light-heavy'
    ```

    * Changed in v5.7: was a property before.

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`Barline`](#music21.bar.Barline "music21.bar.Barline") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## Repeat

class music21.bar.Repeat(*direction: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = 'start'*, *times: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\*\*keywords*)[[source]](../_modules/music21/bar.html#Repeat)
:   A Repeat barline.

    The direction parameter can be one of start or end.
    An end followed by a start
    should be encoded as two bar.Repeat signs.

    ```python
    >>> rep = bar.Repeat(direction='end', times=3)
    >>> rep
    <music21.bar.Repeat direction=end times=3>
    ```

    To apply a repeat barline assign it to either the .leftBarline or
    .rightBarline attribute
    of a measure.

    ```python
    >>> m = stream.Measure()
    >>> m.leftBarline = bar.Repeat(direction='start')
    >>> m.rightBarline = bar.Repeat(direction='end')
    >>> m.insert(0.0, meter.TimeSignature('4/4'))
    >>> m.repeatAppend(note.Note('D--5'), 4)
    >>> p = stream.Part()
    >>> p.insert(0.0, m)
    >>> p.show('text')
    {0.0} <music21.stream.Measure 0 offset=0.0>
        {0.0} <music21.bar.Repeat direction=start>
        {0.0} <music21.meter.TimeSignature 4/4>
        {0.0} <music21.note.Note D-->
        {1.0} <music21.note.Note D-->
        {2.0} <music21.note.Note D-->
        {3.0} <music21.note.Note D-->
        {4.0} <music21.bar.Repeat direction=end>
    ```

    The method `expandRepeats()` on a
    `Part` object expands the repeats, but
    does not update measure numbers

    ```python
    >>> q = p.expandRepeats()
    >>> q.show('text')
    {0.0} <music21.stream.Measure 0 offset=0.0>
        {0.0} <music21.bar.Barline type=double>
        {0.0} <music21.meter.TimeSignature 4/4>
        {0.0} <music21.note.Note D-->
        {1.0} <music21.note.Note D-->
        {2.0} <music21.note.Note D-->
        {3.0} <music21.note.Note D-->
        {4.0} <music21.bar.Barline type=double>
    {4.0} <music21.stream.Measure 0a offset=4.0>
        {0.0} <music21.bar.Barline type=double>
        {0.0} <music21.meter.TimeSignature 4/4>
        {0.0} <music21.note.Note D-->
        {1.0} <music21.note.Note D-->
        {2.0} <music21.note.Note D-->
        {3.0} <music21.note.Note D-->
        {4.0} <music21.bar.Barline type=double>
    ```

[`Repeat`](#music21.bar.Repeat "music21.bar.Repeat") bases

* [`RepeatMark`](moduleRepeat.html#music21.repeat.RepeatMark "music21.repeat.RepeatMark")
* [`Barline`](#music21.bar.Barline "music21.bar.Barline")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`Repeat`](#music21.bar.Repeat "music21.bar.Repeat") read-only properties

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`Repeat`](#music21.bar.Repeat "music21.bar.Repeat") read/write properties

Repeat.direction
:   Get or set the direction of this Repeat barline. Can be start or end.

    TODO: show how changing direction changes type.

Repeat.times
:   Get or set the “times” property of this barline. This
    defines how many times the repeat happens. A standard repeat
    repeats 2 times; values equal to or greater than 0 are permitted.
    A repeat of 0 skips the repeated passage.

    ```python
    >>> lb = bar.Repeat(direction='start')
    >>> rb = bar.Repeat(direction='end')
    ```

    Only end expressions can have times:

    ```python
    >>> lb.times = 3
    Traceback (most recent call last):
    music21.bar.BarException: cannot set repeat times on a start Repeat
    ```

    ```python
    >>> rb.times = 3
    >>> rb.times = -3
    Traceback (most recent call last):
    music21.bar.BarException: cannot set repeat times to a value less than zero: -3
    ```

Read/write properties inherited from [`Barline`](#music21.bar.Barline "music21.bar.Barline"):

|  |  |  |
| --- | --- | --- |
| * [`type`](#music21.bar.Barline.type "music21.bar.Barline.type") |  |  |

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`Repeat`](#music21.bar.Repeat "music21.bar.Repeat") methods

Repeat.getTextExpression(*prefix=''*, *postfix='x'*)[[source]](../_modules/music21/bar.html#Repeat.getTextExpression)
:   Return a configured `TextExpressions`
    object describing the repeat times. Append this to the stream
    for annotation of repeat times.

    ```python
    >>> rb = bar.Repeat(direction='end')
    >>> rb.times = 3
    >>> rb.getTextExpression()
    <music21.expressions.TextExpression '3x'>
    ```

    ```python
    >>> rb.getTextExpression(prefix='repeat ', postfix=' times')
    <music21.expressions.TextExpression 'repeat 3 t...'>
    ```

Methods inherited from [`Barline`](#music21.bar.Barline "music21.bar.Barline"):

|  |  |  |
| --- | --- | --- |
| * [`musicXMLBarStyle()`](#music21.bar.Barline.musicXMLBarStyle "music21.bar.Barline.musicXMLBarStyle") |  |  |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`Repeat`](#music21.bar.Repeat "music21.bar.Repeat") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## Functions

music21.bar.standardizeBarType(*value*)[[source]](../_modules/music21/bar.html#standardizeBarType)
:   Standardizes bar type names.

    converts all names to lower case, None to ‘regular’,
    and ‘light-light’ to ‘double’ and ‘light-heavy’ to ‘final’,
    raises an error for unknown styles.

music21.bar.typeToMusicXMLBarStyle(*value*)[[source]](../_modules/music21/bar.html#typeToMusicXMLBarStyle)
:   Convert a music21 barline name into the musicxml name –
    essentially just changes the names of ‘double’ and ‘final’
    to ‘light-light’ and ‘light-heavy’

    Does not do error checking to make sure it’s a valid name,
    since setting the style on a Barline object already does that.

    ```python
    >>> bar.typeToMusicXMLBarStyle('final')
    'light-heavy'
    >>> bar.typeToMusicXMLBarStyle('regular')
    'regular'
    ```
