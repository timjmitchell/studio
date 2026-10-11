Source: https://music21.org/music21docs/moduleReference/moduleExpressions.html

# music21.expressions

This module provides object representations of expressions, that is
notational symbols such as Fermatas, Mordents, Trills, Turns, etc.
which are stored under a Music21Object’s .expressions attribute.

A sub-category of Expressions are Ornaments.

Unlike articulations, expressions can be attached to the Stream itself.
For instance, TextExpressions.

## TextExpression

class music21.expressions.TextExpression(*content=None*, *\*\*keywords*)[[source]](../_modules/music21/expressions.html#TextExpression)
:   A TextExpression is a word, phrase, or similar
    bit of text that is positioned in a Stream or Measure.
    Conventional expressive indications are text
    like “agitato” or “con fuoco.”

    ```python
    >>> te = expressions.TextExpression('Con fuoco')
    >>> te.content
    'Con fuoco'
    ```

    Most configuration of style is done
    on the .style [`TextStyle`](moduleStyle.html#music21.style.TextStyle "music21.style.TextStyle") object
    itself.

    ```python
    >>> te.style.fontSize = 24.0
    >>> te.style.fontSize
    24
    >>> te.style.fontStyle = 'italic'
    >>> te.style.fontWeight = 'bold'
    >>> te.style.letterSpacing = 0.5
    ```

[`TextExpression`](#music21.expressions.TextExpression "music21.expressions.TextExpression") bases

* [`Expression`](#music21.expressions.Expression "music21.expressions.Expression")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`TextExpression`](#music21.expressions.TextExpression "music21.expressions.TextExpression") read-only properties

Read-only properties inherited from [`Expression`](#music21.expressions.Expression "music21.expressions.Expression"):

|  |  |  |
| --- | --- | --- |
| * [`name`](#music21.expressions.Expression.name "music21.expressions.Expression.name") |  |  |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`TextExpression`](#music21.expressions.TextExpression "music21.expressions.TextExpression") read/write properties

TextExpression.content
:   Get or set the content.

    ```python
    >>> te = expressions.TextExpression('dolce')
    >>> te.content
    'dolce'
    >>> te.content = 'sweeter'
    >>> te
    <music21.expressions.TextExpression 'sweeter'>
    ```

TextExpression.enclosure
:   Returns or sets the enclosure on the Style object
    stored on .style.

    Exposed directly on the expression for backwards
    compatibility. Does not create a .style object if
    one does not exist and the value is None.

    ```python
    >>> te = expressions.TextExpression('Bridge')
    >>> te.enclosure is None
    True
    >>> te.enclosure = style.Enclosure.RECTANGLE
    >>> te.enclosure
    <Enclosure.RECTANGLE>
    ```

    Note that this is also set on .style.

    ```python
    >>> te.style.enclosure
    <Enclosure.RECTANGLE>
    ```

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`TextExpression`](#music21.expressions.TextExpression "music21.expressions.TextExpression") methods

TextExpression.getRepeatExpression()[[source]](../_modules/music21/expressions.html#TextExpression.getRepeatExpression)
:   If this TextExpression can be a RepeatExpression,
    return a new [`RepeatExpression`](moduleRepeat.html#music21.repeat.RepeatExpression "music21.repeat.RepeatExpression").
    object, otherwise, return None.

TextExpression.getTempoText()[[source]](../_modules/music21/expressions.html#TextExpression.getTempoText)

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`TextExpression`](#music21.expressions.TextExpression "music21.expressions.TextExpression") instance variables

TextExpression.placement
:   Staff placement: ‘above’, ‘below’, or None.

    A setting of None implies that the placement will be determined
    by notation software and no particular placement is demanded.

    This is not placed in the .style property, since for some
    expressions, the placement above or below an object has semantic
    meaning and is not purely presentational.

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## Appoggiatura

class music21.expressions.Appoggiatura(*\*\*keywords*)[[source]](../_modules/music21/expressions.html#Appoggiatura)

[`Appoggiatura`](#music21.expressions.Appoggiatura "music21.expressions.Appoggiatura") bases

* [`GeneralAppoggiatura`](#music21.expressions.GeneralAppoggiatura "music21.expressions.GeneralAppoggiatura")
* [`Ornament`](#music21.expressions.Ornament "music21.expressions.Ornament")
* [`Expression`](#music21.expressions.Expression "music21.expressions.Expression")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`Appoggiatura`](#music21.expressions.Appoggiatura "music21.expressions.Appoggiatura") read-only properties

Read-only properties inherited from [`Ornament`](#music21.expressions.Ornament "music21.expressions.Ornament"):

|  |  |  |
| --- | --- | --- |
| * [`ornamentalPitches`](#music21.expressions.Ornament.ornamentalPitches "music21.expressions.Ornament.ornamentalPitches") |  |  |

Read-only properties inherited from [`Expression`](#music21.expressions.Expression "music21.expressions.Expression"):

|  |  |  |
| --- | --- | --- |
| * [`name`](#music21.expressions.Expression.name "music21.expressions.Expression.name") |  |  |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`Appoggiatura`](#music21.expressions.Appoggiatura "music21.expressions.Appoggiatura") read/write properties

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`Appoggiatura`](#music21.expressions.Appoggiatura "music21.expressions.Appoggiatura") methods

Methods inherited from [`GeneralAppoggiatura`](#music21.expressions.GeneralAppoggiatura "music21.expressions.GeneralAppoggiatura"):

|  |  |  |
| --- | --- | --- |
| * [`realize()`](#music21.expressions.GeneralAppoggiatura.realize "music21.expressions.GeneralAppoggiatura.realize") |  |  |

Methods inherited from [`Ornament`](#music21.expressions.Ornament "music21.expressions.Ornament"):

|  |  |  |
| --- | --- | --- |
| * [`fillListOfRealizedNotes()`](#music21.expressions.Ornament.fillListOfRealizedNotes "music21.expressions.Ornament.fillListOfRealizedNotes") | * [`resolveOrnamentalPitches()`](#music21.expressions.Ornament.resolveOrnamentalPitches "music21.expressions.Ornament.resolveOrnamentalPitches") | * [`updateAccidentalDisplay()`](#music21.expressions.Ornament.updateAccidentalDisplay "music21.expressions.Ornament.updateAccidentalDisplay") |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`Appoggiatura`](#music21.expressions.Appoggiatura "music21.expressions.Appoggiatura") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## ArpeggioMark

class music21.expressions.ArpeggioMark(*arpeggioType: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\*\*keywords*)[[source]](../_modules/music21/expressions.html#ArpeggioMark)
:   ArpeggioMark must be applied to a Chord (not to a single Note).

    The parameter arpeggioType can be ‘normal’ (a squiggly line), ‘up’ (a squiggly line
    with an up arrow), ‘down’ (a squiggly line with a down arrow), or ‘non-arpeggio’ (a
    bracket instead of a squiggly line, used to indicate a non-arpeggiated chord
    intervening in a sequence of arpeggiated ones).

    ```python
    >>> am = expressions.ArpeggioMark('normal')
    >>> am.type
    'normal'
    ```

    ```python
    >>> am = expressions.ArpeggioMark('down')
    >>> am.type
    'down'
    ```

[`ArpeggioMark`](#music21.expressions.ArpeggioMark "music21.expressions.ArpeggioMark") bases

* [`Expression`](#music21.expressions.Expression "music21.expressions.Expression")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`ArpeggioMark`](#music21.expressions.ArpeggioMark "music21.expressions.ArpeggioMark") read-only properties

Read-only properties inherited from [`Expression`](#music21.expressions.Expression "music21.expressions.Expression"):

|  |  |  |
| --- | --- | --- |
| * [`name`](#music21.expressions.Expression.name "music21.expressions.Expression.name") |  |  |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`ArpeggioMark`](#music21.expressions.ArpeggioMark "music21.expressions.ArpeggioMark") read/write properties

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`ArpeggioMark`](#music21.expressions.ArpeggioMark "music21.expressions.ArpeggioMark") methods

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`ArpeggioMark`](#music21.expressions.ArpeggioMark "music21.expressions.ArpeggioMark") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## ArpeggioMarkSpanner

class music21.expressions.ArpeggioMarkSpanner(*\*spannedElements*, *arpeggioType: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = 'normal'*, *\*\*keywords*)[[source]](../_modules/music21/expressions.html#ArpeggioMarkSpanner)
:   ArpeggioMarkSpanner is a multi-staff or multi-voice (i.e. multi-chord) arpeggio.
    The spanner should contain all the simultaneous Chords that are to be
    arpeggiated together. If there is only one arpeggiated note in a particular staff
    or voice (i.e. the rest are in other staves/voices), then in that case only the
    spanner can contain a Note. Do not ever put a Note that is within a Chord into a
    spanner; put the Chord in instead. And do not ever put an ArpeggioMark in a note
    or chord’s .expressions.

    The parameter arpeggioType can be ‘normal’ (a squiggly line), ‘up’ (a squiggly line
    with an up arrow), ‘down’ (a squiggly line with a down arrow), or ‘non-arpeggio’ (a
    bracket instead of a squiggly line, used to indicate a non-arpeggiated multi-chord
    intervening in a sequence of arpeggiated ones).

    ```python
    >>> ams = expressions.ArpeggioMarkSpanner(arpeggioType='non-arpeggio')
    >>> c1 = chord.Chord('C3 E3 G3')
    >>> c2 = chord.Chord('C4 E4 G4')
    >>> ams.addSpannedElements([c1, c2])
    >>> ams.type
    'non-arpeggio'
    >>> ams
    <music21.expressions.ArpeggioMarkSpanner
     <music21.chord.Chord C3 E3 G3><music21.chord.Chord C4 E4 G4>>
    ```

[`ArpeggioMarkSpanner`](#music21.expressions.ArpeggioMarkSpanner "music21.expressions.ArpeggioMarkSpanner") bases

* [`Spanner`](moduleSpanner.html#music21.spanner.Spanner "music21.spanner.Spanner")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`ArpeggioMarkSpanner`](#music21.expressions.ArpeggioMarkSpanner "music21.expressions.ArpeggioMarkSpanner") read-only properties

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`ArpeggioMarkSpanner`](#music21.expressions.ArpeggioMarkSpanner "music21.expressions.ArpeggioMarkSpanner") read/write properties

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`ArpeggioMarkSpanner`](#music21.expressions.ArpeggioMarkSpanner "music21.expressions.ArpeggioMarkSpanner") methods

ArpeggioMarkSpanner.noteExtremes() → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[note.Note](moduleNote.html#music21.note.Note "music21.note.Note") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [note.Note](moduleNote.html#music21.note.Note "music21.note.Note") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][[source]](../_modules/music21/expressions.html#ArpeggioMarkSpanner.noteExtremes)
:   Return the lowest and highest note spanned by the element,
    extracting them from Chords if need be.

    ```python
    >>> ch = chord.Chord(['C4', 'E4', 'G4'])
    >>> n = note.Note('C#3')
    >>> nonArp = expressions.ArpeggioMarkSpanner([ch, n])
    >>> nonArp.noteExtremes()
    (<music21.note.Note C#>, <music21.note.Note G>)
    ```

Methods inherited from [`Spanner`](moduleSpanner.html#music21.spanner.Spanner "music21.spanner.Spanner"):

|  |  |  |
| --- | --- | --- |
| * [`__getitem__()`](moduleSpanner.html#music21.spanner.Spanner.__getitem__ "music21.spanner.Spanner.__getitem__") * [`addSpannedElements()`](moduleSpanner.html#music21.spanner.Spanner.addSpannedElements "music21.spanner.Spanner.addSpannedElements") * [`fill()`](moduleSpanner.html#music21.spanner.Spanner.fill "music21.spanner.Spanner.fill") * [`getFirst()`](moduleSpanner.html#music21.spanner.Spanner.getFirst "music21.spanner.Spanner.getFirst") * [`getLast()`](moduleSpanner.html#music21.spanner.Spanner.getLast "music21.spanner.Spanner.getLast") | * [`getSpannedElementIds()`](moduleSpanner.html#music21.spanner.Spanner.getSpannedElementIds "music21.spanner.Spanner.getSpannedElementIds") * [`getSpannedElements()`](moduleSpanner.html#music21.spanner.Spanner.getSpannedElements "music21.spanner.Spanner.getSpannedElements") * [`getSpannedElementsByClass()`](moduleSpanner.html#music21.spanner.Spanner.getSpannedElementsByClass "music21.spanner.Spanner.getSpannedElementsByClass") * [`hasSpannedElement()`](moduleSpanner.html#music21.spanner.Spanner.hasSpannedElement "music21.spanner.Spanner.hasSpannedElement") * [`insertFirstSpannedElement()`](moduleSpanner.html#music21.spanner.Spanner.insertFirstSpannedElement "music21.spanner.Spanner.insertFirstSpannedElement") | * [`isFirst()`](moduleSpanner.html#music21.spanner.Spanner.isFirst "music21.spanner.Spanner.isFirst") * [`isLast()`](moduleSpanner.html#music21.spanner.Spanner.isLast "music21.spanner.Spanner.isLast") * [`purgeLocations()`](moduleSpanner.html#music21.spanner.Spanner.purgeLocations "music21.spanner.Spanner.purgeLocations") * [`purgeOrphans()`](moduleSpanner.html#music21.spanner.Spanner.purgeOrphans "music21.spanner.Spanner.purgeOrphans") * [`replaceSpannedElement()`](moduleSpanner.html#music21.spanner.Spanner.replaceSpannedElement "music21.spanner.Spanner.replaceSpannedElement") |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") | * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") | * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`ArpeggioMarkSpanner`](#music21.expressions.ArpeggioMarkSpanner "music21.expressions.ArpeggioMarkSpanner") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## Expression

class music21.expressions.Expression(*\*\*keywords*)[[source]](../_modules/music21/expressions.html#Expression)
:   This base class is inherited by many diverse expressions.

[`Expression`](#music21.expressions.Expression "music21.expressions.Expression") bases

* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`Expression`](#music21.expressions.Expression "music21.expressions.Expression") read-only properties

Expression.name
:   returns the name of the expression, which is generally the
    class name lowercased and spaces where a new capital occurs.

    Subclasses can override this as necessary.

    ```python
    >>> sc = expressions.Schleifer()
    >>> sc.name
    'schleifer'
    ```

    ```python
    >>> iTurn = expressions.InvertedTurn()
    >>> iTurn.name
    'inverted turn'
    ```

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`Expression`](#music21.expressions.Expression "music21.expressions.Expression") read/write properties

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`Expression`](#music21.expressions.Expression "music21.expressions.Expression") methods

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`Expression`](#music21.expressions.Expression "music21.expressions.Expression") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## Fermata

class music21.expressions.Fermata(*\*\*keywords*)[[source]](../_modules/music21/expressions.html#Fermata)
:   Fermatas by default get appended to the last
    note if a note is split because of measures.

    To override this (for Fermatas or for any
    expression) set .tieAttach to ‘all’ or ‘first’
    instead of ‘last’.

    ```python
    >>> p1 = stream.Part()
    >>> p1.append(meter.TimeSignature('6/8'))
    >>> n1 = note.Note('D-2')
    >>> n1.quarterLength = 6
    >>> n1.expressions.append(expressions.Fermata())
    >>> p1.append(n1)
    >>> p1.show()
    .. image:: images/expressionsFermata.*
         :width: 193
    ```

[`Fermata`](#music21.expressions.Fermata "music21.expressions.Fermata") bases

* [`Expression`](#music21.expressions.Expression "music21.expressions.Expression")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`Fermata`](#music21.expressions.Fermata "music21.expressions.Fermata") read-only properties

Read-only properties inherited from [`Expression`](#music21.expressions.Expression "music21.expressions.Expression"):

|  |  |  |
| --- | --- | --- |
| * [`name`](#music21.expressions.Expression.name "music21.expressions.Expression.name") |  |  |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`Fermata`](#music21.expressions.Fermata "music21.expressions.Fermata") read/write properties

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`Fermata`](#music21.expressions.Fermata "music21.expressions.Fermata") methods

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`Fermata`](#music21.expressions.Fermata "music21.expressions.Fermata") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## GeneralAppoggiatura

class music21.expressions.GeneralAppoggiatura(*\*\*keywords*)[[source]](../_modules/music21/expressions.html#GeneralAppoggiatura)

[`GeneralAppoggiatura`](#music21.expressions.GeneralAppoggiatura "music21.expressions.GeneralAppoggiatura") bases

* [`Ornament`](#music21.expressions.Ornament "music21.expressions.Ornament")
* [`Expression`](#music21.expressions.Expression "music21.expressions.Expression")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`GeneralAppoggiatura`](#music21.expressions.GeneralAppoggiatura "music21.expressions.GeneralAppoggiatura") read-only properties

Read-only properties inherited from [`Ornament`](#music21.expressions.Ornament "music21.expressions.Ornament"):

|  |  |  |
| --- | --- | --- |
| * [`ornamentalPitches`](#music21.expressions.Ornament.ornamentalPitches "music21.expressions.Ornament.ornamentalPitches") |  |  |

Read-only properties inherited from [`Expression`](#music21.expressions.Expression "music21.expressions.Expression"):

|  |  |  |
| --- | --- | --- |
| * [`name`](#music21.expressions.Expression.name "music21.expressions.Expression.name") |  |  |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`GeneralAppoggiatura`](#music21.expressions.GeneralAppoggiatura "music21.expressions.GeneralAppoggiatura") read/write properties

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`GeneralAppoggiatura`](#music21.expressions.GeneralAppoggiatura "music21.expressions.GeneralAppoggiatura") methods

GeneralAppoggiatura.realize(*srcObj: [note.Note](moduleNote.html#music21.note.Note "music21.note.Note") | [note.Unpitched](moduleNote.html#music21.note.Unpitched "music21.note.Unpitched")*, *\**, *keySig: [key.KeySignature](moduleKey.html#music21.key.KeySignature "music21.key.KeySignature") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *inPlace: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[note.Note](moduleNote.html#music21.note.Note "music21.note.Note") | [note.Unpitched](moduleNote.html#music21.note.Unpitched "music21.note.Unpitched")], [note.Note](moduleNote.html#music21.note.Note "music21.note.Note") | [note.Unpitched](moduleNote.html#music21.note.Unpitched "music21.note.Unpitched") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[note.Note](moduleNote.html#music21.note.Note "music21.note.Note") | [note.Unpitched](moduleNote.html#music21.note.Unpitched "music21.note.Unpitched")]][[source]](../_modules/music21/expressions.html#GeneralAppoggiatura.realize)
:   realize an appoggiatura

    returns a three-element tuple.
    The first is the list of notes that the grace note was converted to.
    The second is the rest of the note
    The third is an empty list (since there are no notes at the end of an appoggiatura)

    ```python
    >>> n1 = note.Note('C4')
    >>> n1.quarterLength = 0.5
    >>> a1 = expressions.Appoggiatura()
    >>> a1.realize(n1)
    ([<music21.note.Note D>], <music21.note.Note C>, [])
    ```

    ```python
    >>> n2 = note.Note('C4')
    >>> n2.quarterLength = 1
    >>> a2 = expressions.HalfStepInvertedAppoggiatura()
    >>> a2.realize(n2)
    ([<music21.note.Note B>], <music21.note.Note C>, [])
    ```

Methods inherited from [`Ornament`](#music21.expressions.Ornament "music21.expressions.Ornament"):

|  |  |  |
| --- | --- | --- |
| * [`fillListOfRealizedNotes()`](#music21.expressions.Ornament.fillListOfRealizedNotes "music21.expressions.Ornament.fillListOfRealizedNotes") | * [`resolveOrnamentalPitches()`](#music21.expressions.Ornament.resolveOrnamentalPitches "music21.expressions.Ornament.resolveOrnamentalPitches") | * [`updateAccidentalDisplay()`](#music21.expressions.Ornament.updateAccidentalDisplay "music21.expressions.Ornament.updateAccidentalDisplay") |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`GeneralAppoggiatura`](#music21.expressions.GeneralAppoggiatura "music21.expressions.GeneralAppoggiatura") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## GeneralMordent

class music21.expressions.GeneralMordent(*\**, *accidental: [Accidental](modulePitch.html#music21.pitch.Accidental "music21.pitch.Accidental") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\*\*keywords*)[[source]](../_modules/music21/expressions.html#GeneralMordent)
:   Base class for all Mordent types.

[`GeneralMordent`](#music21.expressions.GeneralMordent "music21.expressions.GeneralMordent") bases

* [`Ornament`](#music21.expressions.Ornament "music21.expressions.Ornament")
* [`Expression`](#music21.expressions.Expression "music21.expressions.Expression")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`GeneralMordent`](#music21.expressions.GeneralMordent "music21.expressions.GeneralMordent") read-only properties

GeneralMordent.direction
:   The direction of the mordent’s ornamental pitch from the main note.
    Can be ‘up’ or ‘down’.

GeneralMordent.name
:   returns the name of the Mordent/InvertedMordent, which is generally
    the class name lowercased, with spaces where a new capital occurs. The
    name also will include any accidental, if it exists.

    Subclasses can override this as necessary.

    ```python
    >>> mordent = expressions.Mordent()
    >>> mordent.name
    'mordent'
    ```

    ```python
    >>> sharp = pitch.Accidental('sharp')
    >>> invertedMordent = expressions.InvertedMordent(accidental=sharp)
    >>> invertedMordent.name
    'inverted mordent (sharp)'
    ```

GeneralMordent.ornamentalPitch
:   Returns the mordent’s ornamentalPitch. If resolveOrnamentalPitches
    has not yet been called, None is returned.

GeneralMordent.ornamentalPitches
:   Returns any ornamental pitch that has been resolved (see
    resolveOrnamentalPitches, which must be called first, or an
    empty tuple will be returned).

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`GeneralMordent`](#music21.expressions.GeneralMordent "music21.expressions.GeneralMordent") read/write properties

GeneralMordent.accidental
:   This is the GeneralMordent’s accidental.

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`GeneralMordent`](#music21.expressions.GeneralMordent "music21.expressions.GeneralMordent") methods

GeneralMordent.getSize(*srcObj: [note.GeneralNote](moduleNote.html#music21.note.GeneralNote "music21.note.GeneralNote")*, *\**, *keySig: [key.KeySignature](moduleKey.html#music21.key.KeySignature "music21.key.KeySignature") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [interval.IntervalBase](moduleInterval.html#music21.interval.IntervalBase "music21.interval.IntervalBase")[[source]](../_modules/music21/expressions.html#GeneralMordent.getSize)
:   Returns the size of the mordent’s interval, given a source note and
    an optional key signature. If the key signature is not specified, the
    source note’s context is searched for the current key signature, and if
    there is no such key signature, a key signature with no sharps and no flats
    will be used. Any accidental that has been set on the mordent will also
    be taken into account. If no accidental has been set, the appropriate
    accidental from the key signature will be used.

    If keySig is specified, this can be considered to be a theoretical question:
    “If this particular mordent were to be attached to this note, in this key,
    what would the size of the mordent interval be?”

GeneralMordent.realize(*srcObj: [note.Note](moduleNote.html#music21.note.Note "music21.note.Note") | [note.Unpitched](moduleNote.html#music21.note.Unpitched "music21.note.Unpitched")*, *\**, *keySig: [key.KeySignature](moduleKey.html#music21.key.KeySignature "music21.key.KeySignature") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *inPlace: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[note.Note](moduleNote.html#music21.note.Note "music21.note.Note") | [note.Unpitched](moduleNote.html#music21.note.Unpitched "music21.note.Unpitched")], [note.Note](moduleNote.html#music21.note.Note "music21.note.Note") | [note.Unpitched](moduleNote.html#music21.note.Unpitched "music21.note.Unpitched") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[note.Note](moduleNote.html#music21.note.Note "music21.note.Note") | [note.Unpitched](moduleNote.html#music21.note.Unpitched "music21.note.Unpitched")]][[source]](../_modules/music21/expressions.html#GeneralMordent.realize)
:   Realize a mordent.

    returns a three-element tuple.
    The first is a list of the two notes that the beginning of the note were converted to.
    The second is the rest of the note.
    The third is an empty list (since there are no notes at the end of a mordent).

    ```python
    >>> n1 = note.Note('C4')
    >>> n1.quarterLength = 0.5
    >>> m1 = expressions.Mordent()
    >>> m1.realize(n1)
    ([<music21.note.Note C>, <music21.note.Note B>], <music21.note.Note C>, [])
    ```

    Note: use one of the subclasses, not the GeneralMordent class

    ```python
    >>> n2 = note.Note('C4')
    >>> n2.quarterLength = 0.125
    >>> m2 = expressions.GeneralMordent()
    >>> m2.realize(n2)
    Traceback (most recent call last):
    music21.expressions.ExpressionException: Cannot realize a mordent if I do not
        know its direction
    ```

GeneralMordent.resolveOrnamentalPitches(*srcObj: [note.GeneralNote](moduleNote.html#music21.note.GeneralNote "music21.note.GeneralNote")*, *\**, *keySig: [key.KeySignature](moduleKey.html#music21.key.KeySignature "music21.key.KeySignature") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](../_modules/music21/expressions.html#GeneralMordent.resolveOrnamentalPitches)
:   Computes and stores the ornamental pitch for a GeneralMordent, given the srcObj
    (can be any kind of ornamented GeneralNote) and an optional keySig.

    If keySig is None, srcNote’s context will be searched for a key signature.
    If no key signature is found, a key signature with no sharps and no flats
    will be used.

    A mordent on a G in a key with no sharps or flats (ornamental pitch will be F).

    ```python
    >>> noSharpsOrFlats = key.KeySignature(sharps=0)
    >>> n1 = note.Note('G4')
    >>> mordent = expressions.Mordent()
    >>> mordent.resolveOrnamentalPitches(n1, keySig=noSharpsOrFlats)
    >>> mordent.ornamentalPitches
    (<music21.pitch.Pitch F4>,)
    >>> mordent.ornamentalPitch
    <music21.pitch.Pitch F4>
    ```

    e.g. A mordent on a G in a key with one sharp (ornamental pitch will be F#).

    ```python
    >>> oneSharp = key.KeySignature(sharps=1)
    >>> mordent.resolveOrnamentalPitches(n1, keySig=oneSharp)
    >>> mordent.ornamentalPitches
    (<music21.pitch.Pitch F#4>,)
    >>> mordent.ornamentalPitch
    <music21.pitch.Pitch F#4>
    ```

    e.g. A mordent with a natural, on a G, in a key with one sharp
    (ornamental pitch will be F).

    ```python
    >>> mordent.accidental = pitch.Accidental('natural')
    >>> mordent.resolveOrnamentalPitches(n1, keySig=oneSharp)
    >>> mordent.ornamentalPitches
    (<music21.pitch.Pitch F4>,)
    >>> mordent.ornamentalPitch
    <music21.pitch.Pitch F4>
    ```

GeneralMordent.updateAccidentalDisplay(*\**, *pitchPast: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *pitchPastMeasure: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *otherSimultaneousPitches: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *alteredPitches: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *cautionaryPitchClass: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *cautionaryAll: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *overrideStatus: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *cautionaryNotImmediateRepeat: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*)[[source]](../_modules/music21/expressions.html#GeneralMordent.updateAccidentalDisplay)
:   Updates accidental display for a GeneralMordent’s ornamental pitch.
    Defined exactly like Pitch.updateAccidentalDisplay, with two changes:
    Instead of self being the pitch to update, self is a GeneralMordent whose
    ornamentalPitch is to be updated; and we pay no attention to ties,
    since ornamental notes cannot be tied.

Methods inherited from [`Ornament`](#music21.expressions.Ornament "music21.expressions.Ornament"):

|  |  |  |
| --- | --- | --- |
| * [`fillListOfRealizedNotes()`](#music21.expressions.Ornament.fillListOfRealizedNotes "music21.expressions.Ornament.fillListOfRealizedNotes") |  |  |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`GeneralMordent`](#music21.expressions.GeneralMordent "music21.expressions.GeneralMordent") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## HalfStepAppoggiatura

class music21.expressions.HalfStepAppoggiatura(*\*\*keywords*)[[source]](../_modules/music21/expressions.html#HalfStepAppoggiatura)

[`HalfStepAppoggiatura`](#music21.expressions.HalfStepAppoggiatura "music21.expressions.HalfStepAppoggiatura") bases

* [`Appoggiatura`](#music21.expressions.Appoggiatura "music21.expressions.Appoggiatura")
* [`GeneralAppoggiatura`](#music21.expressions.GeneralAppoggiatura "music21.expressions.GeneralAppoggiatura")
* [`Ornament`](#music21.expressions.Ornament "music21.expressions.Ornament")
* [`Expression`](#music21.expressions.Expression "music21.expressions.Expression")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`HalfStepAppoggiatura`](#music21.expressions.HalfStepAppoggiatura "music21.expressions.HalfStepAppoggiatura") read-only properties

Read-only properties inherited from [`Ornament`](#music21.expressions.Ornament "music21.expressions.Ornament"):

|  |  |  |
| --- | --- | --- |
| * [`ornamentalPitches`](#music21.expressions.Ornament.ornamentalPitches "music21.expressions.Ornament.ornamentalPitches") |  |  |

Read-only properties inherited from [`Expression`](#music21.expressions.Expression "music21.expressions.Expression"):

|  |  |  |
| --- | --- | --- |
| * [`name`](#music21.expressions.Expression.name "music21.expressions.Expression.name") |  |  |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`HalfStepAppoggiatura`](#music21.expressions.HalfStepAppoggiatura "music21.expressions.HalfStepAppoggiatura") read/write properties

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`HalfStepAppoggiatura`](#music21.expressions.HalfStepAppoggiatura "music21.expressions.HalfStepAppoggiatura") methods

Methods inherited from [`GeneralAppoggiatura`](#music21.expressions.GeneralAppoggiatura "music21.expressions.GeneralAppoggiatura"):

|  |  |  |
| --- | --- | --- |
| * [`realize()`](#music21.expressions.GeneralAppoggiatura.realize "music21.expressions.GeneralAppoggiatura.realize") |  |  |

Methods inherited from [`Ornament`](#music21.expressions.Ornament "music21.expressions.Ornament"):

|  |  |  |
| --- | --- | --- |
| * [`fillListOfRealizedNotes()`](#music21.expressions.Ornament.fillListOfRealizedNotes "music21.expressions.Ornament.fillListOfRealizedNotes") | * [`resolveOrnamentalPitches()`](#music21.expressions.Ornament.resolveOrnamentalPitches "music21.expressions.Ornament.resolveOrnamentalPitches") | * [`updateAccidentalDisplay()`](#music21.expressions.Ornament.updateAccidentalDisplay "music21.expressions.Ornament.updateAccidentalDisplay") |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`HalfStepAppoggiatura`](#music21.expressions.HalfStepAppoggiatura "music21.expressions.HalfStepAppoggiatura") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## HalfStepInvertedAppoggiatura

class music21.expressions.HalfStepInvertedAppoggiatura(*\*\*keywords*)[[source]](../_modules/music21/expressions.html#HalfStepInvertedAppoggiatura)

[`HalfStepInvertedAppoggiatura`](#music21.expressions.HalfStepInvertedAppoggiatura "music21.expressions.HalfStepInvertedAppoggiatura") bases

* [`InvertedAppoggiatura`](#music21.expressions.InvertedAppoggiatura "music21.expressions.InvertedAppoggiatura")
* [`GeneralAppoggiatura`](#music21.expressions.GeneralAppoggiatura "music21.expressions.GeneralAppoggiatura")
* [`Ornament`](#music21.expressions.Ornament "music21.expressions.Ornament")
* [`Expression`](#music21.expressions.Expression "music21.expressions.Expression")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`HalfStepInvertedAppoggiatura`](#music21.expressions.HalfStepInvertedAppoggiatura "music21.expressions.HalfStepInvertedAppoggiatura") read-only properties

Read-only properties inherited from [`Ornament`](#music21.expressions.Ornament "music21.expressions.Ornament"):

|  |  |  |
| --- | --- | --- |
| * [`ornamentalPitches`](#music21.expressions.Ornament.ornamentalPitches "music21.expressions.Ornament.ornamentalPitches") |  |  |

Read-only properties inherited from [`Expression`](#music21.expressions.Expression "music21.expressions.Expression"):

|  |  |  |
| --- | --- | --- |
| * [`name`](#music21.expressions.Expression.name "music21.expressions.Expression.name") |  |  |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`HalfStepInvertedAppoggiatura`](#music21.expressions.HalfStepInvertedAppoggiatura "music21.expressions.HalfStepInvertedAppoggiatura") read/write properties

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`HalfStepInvertedAppoggiatura`](#music21.expressions.HalfStepInvertedAppoggiatura "music21.expressions.HalfStepInvertedAppoggiatura") methods

Methods inherited from [`GeneralAppoggiatura`](#music21.expressions.GeneralAppoggiatura "music21.expressions.GeneralAppoggiatura"):

|  |  |  |
| --- | --- | --- |
| * [`realize()`](#music21.expressions.GeneralAppoggiatura.realize "music21.expressions.GeneralAppoggiatura.realize") |  |  |

Methods inherited from [`Ornament`](#music21.expressions.Ornament "music21.expressions.Ornament"):

|  |  |  |
| --- | --- | --- |
| * [`fillListOfRealizedNotes()`](#music21.expressions.Ornament.fillListOfRealizedNotes "music21.expressions.Ornament.fillListOfRealizedNotes") | * [`resolveOrnamentalPitches()`](#music21.expressions.Ornament.resolveOrnamentalPitches "music21.expressions.Ornament.resolveOrnamentalPitches") | * [`updateAccidentalDisplay()`](#music21.expressions.Ornament.updateAccidentalDisplay "music21.expressions.Ornament.updateAccidentalDisplay") |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`HalfStepInvertedAppoggiatura`](#music21.expressions.HalfStepInvertedAppoggiatura "music21.expressions.HalfStepInvertedAppoggiatura") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## HalfStepInvertedMordent

class music21.expressions.HalfStepInvertedMordent(*\*\*keywords*)[[source]](../_modules/music21/expressions.html#HalfStepInvertedMordent)
:   A half-step inverted Mordent.

    ```python
    >>> m = expressions.HalfStepInvertedMordent()
    >>> m.direction
    'up'
    >>> m.getSize(note.Note('C4'))
    <music21.interval.Interval m2>
    ```

[`HalfStepInvertedMordent`](#music21.expressions.HalfStepInvertedMordent "music21.expressions.HalfStepInvertedMordent") bases

* [`InvertedMordent`](#music21.expressions.InvertedMordent "music21.expressions.InvertedMordent")
* [`GeneralMordent`](#music21.expressions.GeneralMordent "music21.expressions.GeneralMordent")
* [`Ornament`](#music21.expressions.Ornament "music21.expressions.Ornament")
* [`Expression`](#music21.expressions.Expression "music21.expressions.Expression")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`HalfStepInvertedMordent`](#music21.expressions.HalfStepInvertedMordent "music21.expressions.HalfStepInvertedMordent") read-only properties

Read-only properties inherited from [`GeneralMordent`](#music21.expressions.GeneralMordent "music21.expressions.GeneralMordent"):

|  |  |  |
| --- | --- | --- |
| * [`direction`](#music21.expressions.GeneralMordent.direction "music21.expressions.GeneralMordent.direction") * [`name`](#music21.expressions.GeneralMordent.name "music21.expressions.GeneralMordent.name") | * [`ornamentalPitch`](#music21.expressions.GeneralMordent.ornamentalPitch "music21.expressions.GeneralMordent.ornamentalPitch") | * [`ornamentalPitches`](#music21.expressions.GeneralMordent.ornamentalPitches "music21.expressions.GeneralMordent.ornamentalPitches") |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`HalfStepInvertedMordent`](#music21.expressions.HalfStepInvertedMordent "music21.expressions.HalfStepInvertedMordent") read/write properties

HalfStepInvertedMordent.accidental

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`HalfStepInvertedMordent`](#music21.expressions.HalfStepInvertedMordent "music21.expressions.HalfStepInvertedMordent") methods

HalfStepInvertedMordent.getSize(*srcObj: [note.GeneralNote](moduleNote.html#music21.note.GeneralNote "music21.note.GeneralNote")*, *\**, *keySig: [key.KeySignature](moduleKey.html#music21.key.KeySignature "music21.key.KeySignature") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [interval.IntervalBase](moduleInterval.html#music21.interval.IntervalBase "music21.interval.IntervalBase")[[source]](../_modules/music21/expressions.html#HalfStepInvertedMordent.getSize)
:   Returns the size of the mordent’s interval, given a source note and
    an optional key signature. If the key signature is not specified, the
    source note’s context is searched for the current key signature, and if
    there is no such key signature, a key signature with no sharps and no flats
    will be used. Any accidental that has been set on the mordent will also
    be taken into account. If no accidental has been set, the appropriate
    accidental from the key signature will be used.

    If keySig is specified, this can be considered to be a theoretical question:
    “If this particular mordent were to be attached to this note, in this key,
    what would the size of the mordent interval be?”

Methods inherited from [`GeneralMordent`](#music21.expressions.GeneralMordent "music21.expressions.GeneralMordent"):

|  |  |  |
| --- | --- | --- |
| * [`realize()`](#music21.expressions.GeneralMordent.realize "music21.expressions.GeneralMordent.realize") | * [`resolveOrnamentalPitches()`](#music21.expressions.GeneralMordent.resolveOrnamentalPitches "music21.expressions.GeneralMordent.resolveOrnamentalPitches") | * [`updateAccidentalDisplay()`](#music21.expressions.GeneralMordent.updateAccidentalDisplay "music21.expressions.GeneralMordent.updateAccidentalDisplay") |

Methods inherited from [`Ornament`](#music21.expressions.Ornament "music21.expressions.Ornament"):

|  |  |  |
| --- | --- | --- |
| * [`fillListOfRealizedNotes()`](#music21.expressions.Ornament.fillListOfRealizedNotes "music21.expressions.Ornament.fillListOfRealizedNotes") |  |  |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`HalfStepInvertedMordent`](#music21.expressions.HalfStepInvertedMordent "music21.expressions.HalfStepInvertedMordent") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## HalfStepMordent

class music21.expressions.HalfStepMordent(*\*\*keywords*)[[source]](../_modules/music21/expressions.html#HalfStepMordent)
:   A half step normal Mordent.

    ```python
    >>> m = expressions.HalfStepMordent()
    >>> m.direction
    'down'
    >>> m.getSize(note.Note('C4'))
    <music21.interval.Interval m-2>
    ```

[`HalfStepMordent`](#music21.expressions.HalfStepMordent "music21.expressions.HalfStepMordent") bases

* [`Mordent`](#music21.expressions.Mordent "music21.expressions.Mordent")
* [`GeneralMordent`](#music21.expressions.GeneralMordent "music21.expressions.GeneralMordent")
* [`Ornament`](#music21.expressions.Ornament "music21.expressions.Ornament")
* [`Expression`](#music21.expressions.Expression "music21.expressions.Expression")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`HalfStepMordent`](#music21.expressions.HalfStepMordent "music21.expressions.HalfStepMordent") read-only properties

Read-only properties inherited from [`GeneralMordent`](#music21.expressions.GeneralMordent "music21.expressions.GeneralMordent"):

|  |  |  |
| --- | --- | --- |
| * [`direction`](#music21.expressions.GeneralMordent.direction "music21.expressions.GeneralMordent.direction") * [`name`](#music21.expressions.GeneralMordent.name "music21.expressions.GeneralMordent.name") | * [`ornamentalPitch`](#music21.expressions.GeneralMordent.ornamentalPitch "music21.expressions.GeneralMordent.ornamentalPitch") | * [`ornamentalPitches`](#music21.expressions.GeneralMordent.ornamentalPitches "music21.expressions.GeneralMordent.ornamentalPitches") |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`HalfStepMordent`](#music21.expressions.HalfStepMordent "music21.expressions.HalfStepMordent") read/write properties

HalfStepMordent.accidental

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`HalfStepMordent`](#music21.expressions.HalfStepMordent "music21.expressions.HalfStepMordent") methods

HalfStepMordent.getSize(*srcObj: [note.GeneralNote](moduleNote.html#music21.note.GeneralNote "music21.note.GeneralNote")*, *\**, *keySig: [key.KeySignature](moduleKey.html#music21.key.KeySignature "music21.key.KeySignature") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [interval.IntervalBase](moduleInterval.html#music21.interval.IntervalBase "music21.interval.IntervalBase")[[source]](../_modules/music21/expressions.html#HalfStepMordent.getSize)
:   Returns the size of the mordent’s interval, given a source note and
    an optional key signature. If the key signature is not specified, the
    source note’s context is searched for the current key signature, and if
    there is no such key signature, a key signature with no sharps and no flats
    will be used. Any accidental that has been set on the mordent will also
    be taken into account. If no accidental has been set, the appropriate
    accidental from the key signature will be used.

    If keySig is specified, this can be considered to be a theoretical question:
    “If this particular mordent were to be attached to this note, in this key,
    what would the size of the mordent interval be?”

Methods inherited from [`GeneralMordent`](#music21.expressions.GeneralMordent "music21.expressions.GeneralMordent"):

|  |  |  |
| --- | --- | --- |
| * [`realize()`](#music21.expressions.GeneralMordent.realize "music21.expressions.GeneralMordent.realize") | * [`resolveOrnamentalPitches()`](#music21.expressions.GeneralMordent.resolveOrnamentalPitches "music21.expressions.GeneralMordent.resolveOrnamentalPitches") | * [`updateAccidentalDisplay()`](#music21.expressions.GeneralMordent.updateAccidentalDisplay "music21.expressions.GeneralMordent.updateAccidentalDisplay") |

Methods inherited from [`Ornament`](#music21.expressions.Ornament "music21.expressions.Ornament"):

|  |  |  |
| --- | --- | --- |
| * [`fillListOfRealizedNotes()`](#music21.expressions.Ornament.fillListOfRealizedNotes "music21.expressions.Ornament.fillListOfRealizedNotes") |  |  |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`HalfStepMordent`](#music21.expressions.HalfStepMordent "music21.expressions.HalfStepMordent") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## HalfStepTrill

class music21.expressions.HalfStepTrill(*\*\*keywords*)[[source]](../_modules/music21/expressions.html#HalfStepTrill)
:   A trill confined to half steps.

    ```python
    >>> halfTrill = expressions.HalfStepTrill()
    >>> halfTrill.placement
    'above'
    >>> halfTrill.getSize(note.Note('C4'))
    <music21.interval.Interval m2>
    ```

    Here the key signature of 2 sharps will not affect the trill:

    ```python
    >>> n = note.Note('B4', type='eighth')
    >>> m = stream.Measure()
    >>> m.insert(0, key.KeySignature(2))
    >>> m.append(n)
    >>> halfTrill.realize(n)
    ([<music21.note.Note B>,
      <music21.note.Note C>,
      <music21.note.Note B>,
      <music21.note.Note C>], None, [])
    ```

[`HalfStepTrill`](#music21.expressions.HalfStepTrill "music21.expressions.HalfStepTrill") bases

* [`Trill`](#music21.expressions.Trill "music21.expressions.Trill")
* [`Ornament`](#music21.expressions.Ornament "music21.expressions.Ornament")
* [`Expression`](#music21.expressions.Expression "music21.expressions.Expression")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`HalfStepTrill`](#music21.expressions.HalfStepTrill "music21.expressions.HalfStepTrill") read-only properties

Read-only properties inherited from [`Trill`](#music21.expressions.Trill "music21.expressions.Trill"):

|  |  |  |
| --- | --- | --- |
| * [`direction`](#music21.expressions.Trill.direction "music21.expressions.Trill.direction") * [`name`](#music21.expressions.Trill.name "music21.expressions.Trill.name") | * [`ornamentalPitch`](#music21.expressions.Trill.ornamentalPitch "music21.expressions.Trill.ornamentalPitch") | * [`ornamentalPitches`](#music21.expressions.Trill.ornamentalPitches "music21.expressions.Trill.ornamentalPitches") |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`HalfStepTrill`](#music21.expressions.HalfStepTrill "music21.expressions.HalfStepTrill") read/write properties

HalfStepTrill.accidental

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`HalfStepTrill`](#music21.expressions.HalfStepTrill "music21.expressions.HalfStepTrill") methods

HalfStepTrill.getSize(*srcObj: [note.GeneralNote](moduleNote.html#music21.note.GeneralNote "music21.note.GeneralNote")*, *\**, *keySig: [key.KeySignature](moduleKey.html#music21.key.KeySignature "music21.key.KeySignature") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [interval.IntervalBase](moduleInterval.html#music21.interval.IntervalBase "music21.interval.IntervalBase")[[source]](../_modules/music21/expressions.html#HalfStepTrill.getSize)
:   Returns the size of the trill’s interval, given a source note and
    an optional key signature. If the key signature is not specified, the
    source note’s context is searched for the current key signature, and if
    there is no such key signature, a key signature with no sharps and no flats
    will be used. Any accidental that has been set on the trill will also
    be taken into account.

    If keySig is specified, this can be considered to be a theoretical question:
    “If this particular trill were to be attached to this note, in this key,
    what would the size of the trill interval be?”

Methods inherited from [`Trill`](#music21.expressions.Trill "music21.expressions.Trill"):

|  |  |  |
| --- | --- | --- |
| * [`realize()`](#music21.expressions.Trill.realize "music21.expressions.Trill.realize") * [`resolveOrnamentalPitches()`](#music21.expressions.Trill.resolveOrnamentalPitches "music21.expressions.Trill.resolveOrnamentalPitches") | * [`splitClient()`](#music21.expressions.Trill.splitClient "music21.expressions.Trill.splitClient") | * [`updateAccidentalDisplay()`](#music21.expressions.Trill.updateAccidentalDisplay "music21.expressions.Trill.updateAccidentalDisplay") |

Methods inherited from [`Ornament`](#music21.expressions.Ornament "music21.expressions.Ornament"):

|  |  |  |
| --- | --- | --- |
| * [`fillListOfRealizedNotes()`](#music21.expressions.Ornament.fillListOfRealizedNotes "music21.expressions.Ornament.fillListOfRealizedNotes") |  |  |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`HalfStepTrill`](#music21.expressions.HalfStepTrill "music21.expressions.HalfStepTrill") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## InvertedAppoggiatura

class music21.expressions.InvertedAppoggiatura(*\*\*keywords*)[[source]](../_modules/music21/expressions.html#InvertedAppoggiatura)

[`InvertedAppoggiatura`](#music21.expressions.InvertedAppoggiatura "music21.expressions.InvertedAppoggiatura") bases

* [`GeneralAppoggiatura`](#music21.expressions.GeneralAppoggiatura "music21.expressions.GeneralAppoggiatura")
* [`Ornament`](#music21.expressions.Ornament "music21.expressions.Ornament")
* [`Expression`](#music21.expressions.Expression "music21.expressions.Expression")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`InvertedAppoggiatura`](#music21.expressions.InvertedAppoggiatura "music21.expressions.InvertedAppoggiatura") read-only properties

Read-only properties inherited from [`Ornament`](#music21.expressions.Ornament "music21.expressions.Ornament"):

|  |  |  |
| --- | --- | --- |
| * [`ornamentalPitches`](#music21.expressions.Ornament.ornamentalPitches "music21.expressions.Ornament.ornamentalPitches") |  |  |

Read-only properties inherited from [`Expression`](#music21.expressions.Expression "music21.expressions.Expression"):

|  |  |  |
| --- | --- | --- |
| * [`name`](#music21.expressions.Expression.name "music21.expressions.Expression.name") |  |  |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`InvertedAppoggiatura`](#music21.expressions.InvertedAppoggiatura "music21.expressions.InvertedAppoggiatura") read/write properties

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`InvertedAppoggiatura`](#music21.expressions.InvertedAppoggiatura "music21.expressions.InvertedAppoggiatura") methods

Methods inherited from [`GeneralAppoggiatura`](#music21.expressions.GeneralAppoggiatura "music21.expressions.GeneralAppoggiatura"):

|  |  |  |
| --- | --- | --- |
| * [`realize()`](#music21.expressions.GeneralAppoggiatura.realize "music21.expressions.GeneralAppoggiatura.realize") |  |  |

Methods inherited from [`Ornament`](#music21.expressions.Ornament "music21.expressions.Ornament"):

|  |  |  |
| --- | --- | --- |
| * [`fillListOfRealizedNotes()`](#music21.expressions.Ornament.fillListOfRealizedNotes "music21.expressions.Ornament.fillListOfRealizedNotes") | * [`resolveOrnamentalPitches()`](#music21.expressions.Ornament.resolveOrnamentalPitches "music21.expressions.Ornament.resolveOrnamentalPitches") | * [`updateAccidentalDisplay()`](#music21.expressions.Ornament.updateAccidentalDisplay "music21.expressions.Ornament.updateAccidentalDisplay") |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`InvertedAppoggiatura`](#music21.expressions.InvertedAppoggiatura "music21.expressions.InvertedAppoggiatura") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## InvertedMordent

class music21.expressions.InvertedMordent(*\**, *accidental: [Accidental](modulePitch.html#music21.pitch.Accidental "music21.pitch.Accidental") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\*\*keywords*)[[source]](../_modules/music21/expressions.html#InvertedMordent)
:   An inverted Mordent – goes upwards and has no line through it.

    Note that some computer terminology calls this one a (normal) mordent, but this
    is a modern term. See Apel, *Harvard Dictionary of Music*,
    “Inverted Mordent”:

    ```python
    An 18th-century ornament involving alternation of the
    written note with the note immediately above it.
    ```

    An inverted mordent has the size of a second, of some form, depending on the note
    that will have the mordent, the current key signature in that note’s context, as
    well as any accidental on the mordent itself.

    ```python
    >>> m = expressions.InvertedMordent()
    >>> m.direction
    'up'
    >>> m.getSize(note.Note('C4'))
    <music21.interval.Interval M2>
    >>> m.getSize(note.Note('B3'))
    <music21.interval.Interval m2>
    ```

    ```python
    >>> mSharp = expressions.InvertedMordent(accidental=pitch.Accidental('sharp'))
    >>> mSharp.direction
    'up'
    >>> mSharp.getSize(note.Note('C4'))
    <music21.interval.Interval A2>
    >>> mSharp.getSize(note.Note('B3'))
    <music21.interval.Interval M2>
    ```

    * Changed in v7: InvertedMordent sizes are GenericIntervals – as was originally
      intended but programmed incorrectly.
    * Changed in v9: Support an accidental on InvertedMordent. This also adds the concept of
      an ornamental pitch that is processed by makeAccidentals.
      The size property has been removed and replaced with .getSize() (which requires
      a srcObj and optional keySig param). Added optional keySig param to
      .realize() as well.

[`InvertedMordent`](#music21.expressions.InvertedMordent "music21.expressions.InvertedMordent") bases

* [`GeneralMordent`](#music21.expressions.GeneralMordent "music21.expressions.GeneralMordent")
* [`Ornament`](#music21.expressions.Ornament "music21.expressions.Ornament")
* [`Expression`](#music21.expressions.Expression "music21.expressions.Expression")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`InvertedMordent`](#music21.expressions.InvertedMordent "music21.expressions.InvertedMordent") read-only properties

Read-only properties inherited from [`GeneralMordent`](#music21.expressions.GeneralMordent "music21.expressions.GeneralMordent"):

|  |  |  |
| --- | --- | --- |
| * [`direction`](#music21.expressions.GeneralMordent.direction "music21.expressions.GeneralMordent.direction") * [`name`](#music21.expressions.GeneralMordent.name "music21.expressions.GeneralMordent.name") | * [`ornamentalPitch`](#music21.expressions.GeneralMordent.ornamentalPitch "music21.expressions.GeneralMordent.ornamentalPitch") | * [`ornamentalPitches`](#music21.expressions.GeneralMordent.ornamentalPitches "music21.expressions.GeneralMordent.ornamentalPitches") |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`InvertedMordent`](#music21.expressions.InvertedMordent "music21.expressions.InvertedMordent") read/write properties

Read/write properties inherited from [`GeneralMordent`](#music21.expressions.GeneralMordent "music21.expressions.GeneralMordent"):

|  |  |  |
| --- | --- | --- |
| * [`accidental`](#music21.expressions.GeneralMordent.accidental "music21.expressions.GeneralMordent.accidental") |  |  |

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`InvertedMordent`](#music21.expressions.InvertedMordent "music21.expressions.InvertedMordent") methods

Methods inherited from [`GeneralMordent`](#music21.expressions.GeneralMordent "music21.expressions.GeneralMordent"):

|  |  |  |
| --- | --- | --- |
| * [`getSize()`](#music21.expressions.GeneralMordent.getSize "music21.expressions.GeneralMordent.getSize") * [`realize()`](#music21.expressions.GeneralMordent.realize "music21.expressions.GeneralMordent.realize") | * [`resolveOrnamentalPitches()`](#music21.expressions.GeneralMordent.resolveOrnamentalPitches "music21.expressions.GeneralMordent.resolveOrnamentalPitches") | * [`updateAccidentalDisplay()`](#music21.expressions.GeneralMordent.updateAccidentalDisplay "music21.expressions.GeneralMordent.updateAccidentalDisplay") |

Methods inherited from [`Ornament`](#music21.expressions.Ornament "music21.expressions.Ornament"):

|  |  |  |
| --- | --- | --- |
| * [`fillListOfRealizedNotes()`](#music21.expressions.Ornament.fillListOfRealizedNotes "music21.expressions.Ornament.fillListOfRealizedNotes") |  |  |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`InvertedMordent`](#music21.expressions.InvertedMordent "music21.expressions.InvertedMordent") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## InvertedTrill

class music21.expressions.InvertedTrill(*\**, *accidental: [Accidental](modulePitch.html#music21.pitch.Accidental "music21.pitch.Accidental") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\*\*keywords*)[[source]](../_modules/music21/expressions.html#InvertedTrill)

[`InvertedTrill`](#music21.expressions.InvertedTrill "music21.expressions.InvertedTrill") bases

* [`Trill`](#music21.expressions.Trill "music21.expressions.Trill")
* [`Ornament`](#music21.expressions.Ornament "music21.expressions.Ornament")
* [`Expression`](#music21.expressions.Expression "music21.expressions.Expression")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`InvertedTrill`](#music21.expressions.InvertedTrill "music21.expressions.InvertedTrill") read-only properties

Read-only properties inherited from [`Trill`](#music21.expressions.Trill "music21.expressions.Trill"):

|  |  |  |
| --- | --- | --- |
| * [`direction`](#music21.expressions.Trill.direction "music21.expressions.Trill.direction") * [`name`](#music21.expressions.Trill.name "music21.expressions.Trill.name") | * [`ornamentalPitch`](#music21.expressions.Trill.ornamentalPitch "music21.expressions.Trill.ornamentalPitch") | * [`ornamentalPitches`](#music21.expressions.Trill.ornamentalPitches "music21.expressions.Trill.ornamentalPitches") |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`InvertedTrill`](#music21.expressions.InvertedTrill "music21.expressions.InvertedTrill") read/write properties

Read/write properties inherited from [`Trill`](#music21.expressions.Trill "music21.expressions.Trill"):

|  |  |  |
| --- | --- | --- |
| * [`accidental`](#music21.expressions.Trill.accidental "music21.expressions.Trill.accidental") |  |  |

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`InvertedTrill`](#music21.expressions.InvertedTrill "music21.expressions.InvertedTrill") methods

Methods inherited from [`Trill`](#music21.expressions.Trill "music21.expressions.Trill"):

|  |  |  |
| --- | --- | --- |
| * [`getSize()`](#music21.expressions.Trill.getSize "music21.expressions.Trill.getSize") * [`realize()`](#music21.expressions.Trill.realize "music21.expressions.Trill.realize") | * [`resolveOrnamentalPitches()`](#music21.expressions.Trill.resolveOrnamentalPitches "music21.expressions.Trill.resolveOrnamentalPitches") * [`splitClient()`](#music21.expressions.Trill.splitClient "music21.expressions.Trill.splitClient") | * [`updateAccidentalDisplay()`](#music21.expressions.Trill.updateAccidentalDisplay "music21.expressions.Trill.updateAccidentalDisplay") |

Methods inherited from [`Ornament`](#music21.expressions.Ornament "music21.expressions.Ornament"):

|  |  |  |
| --- | --- | --- |
| * [`fillListOfRealizedNotes()`](#music21.expressions.Ornament.fillListOfRealizedNotes "music21.expressions.Ornament.fillListOfRealizedNotes") |  |  |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`InvertedTrill`](#music21.expressions.InvertedTrill "music21.expressions.InvertedTrill") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## InvertedTurn

class music21.expressions.InvertedTurn(*\**, *delay: [OrnamentDelay](moduleCommonEnums.html#music21.common.enums.OrnamentDelay "music21.common.enums.OrnamentDelay") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [Fraction](https://docs.python.org/3/library/fractions.html#fractions.Fraction "(in Python v3.14)") = <OrnamentDelay.NO\_DELAY>*, *upperAccidental: [Accidental](modulePitch.html#music21.pitch.Accidental "music21.pitch.Accidental") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *lowerAccidental: [Accidental](modulePitch.html#music21.pitch.Accidental "music21.pitch.Accidental") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\*\*keywords*)[[source]](../_modules/music21/expressions.html#InvertedTurn)

[`InvertedTurn`](#music21.expressions.InvertedTurn "music21.expressions.InvertedTurn") bases

* [`Turn`](#music21.expressions.Turn "music21.expressions.Turn")
* [`Ornament`](#music21.expressions.Ornament "music21.expressions.Ornament")
* [`Expression`](#music21.expressions.Expression "music21.expressions.Expression")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`InvertedTurn`](#music21.expressions.InvertedTurn "music21.expressions.InvertedTurn") read-only properties

Read-only properties inherited from [`Turn`](#music21.expressions.Turn "music21.expressions.Turn"):

|  |  |  |
| --- | --- | --- |
| * [`isDelayed`](#music21.expressions.Turn.isDelayed "music21.expressions.Turn.isDelayed") * [`lowerOrnamentalPitch`](#music21.expressions.Turn.lowerOrnamentalPitch "music21.expressions.Turn.lowerOrnamentalPitch") | * [`name`](#music21.expressions.Turn.name "music21.expressions.Turn.name") * [`ornamentalPitches`](#music21.expressions.Turn.ornamentalPitches "music21.expressions.Turn.ornamentalPitches") | * [`upperOrnamentalPitch`](#music21.expressions.Turn.upperOrnamentalPitch "music21.expressions.Turn.upperOrnamentalPitch") |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`InvertedTurn`](#music21.expressions.InvertedTurn "music21.expressions.InvertedTurn") read/write properties

Read/write properties inherited from [`Turn`](#music21.expressions.Turn "music21.expressions.Turn"):

|  |  |  |
| --- | --- | --- |
| * [`delay`](#music21.expressions.Turn.delay "music21.expressions.Turn.delay") | * [`lowerAccidental`](#music21.expressions.Turn.lowerAccidental "music21.expressions.Turn.lowerAccidental") | * [`upperAccidental`](#music21.expressions.Turn.upperAccidental "music21.expressions.Turn.upperAccidental") |

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`InvertedTurn`](#music21.expressions.InvertedTurn "music21.expressions.InvertedTurn") methods

Methods inherited from [`Turn`](#music21.expressions.Turn "music21.expressions.Turn"):

|  |  |  |
| --- | --- | --- |
| * [`getSize()`](#music21.expressions.Turn.getSize "music21.expressions.Turn.getSize") * [`realize()`](#music21.expressions.Turn.realize "music21.expressions.Turn.realize") | * [`resolveOrnamentalPitches()`](#music21.expressions.Turn.resolveOrnamentalPitches "music21.expressions.Turn.resolveOrnamentalPitches") | * [`updateAccidentalDisplay()`](#music21.expressions.Turn.updateAccidentalDisplay "music21.expressions.Turn.updateAccidentalDisplay") |

Methods inherited from [`Ornament`](#music21.expressions.Ornament "music21.expressions.Ornament"):

|  |  |  |
| --- | --- | --- |
| * [`fillListOfRealizedNotes()`](#music21.expressions.Ornament.fillListOfRealizedNotes "music21.expressions.Ornament.fillListOfRealizedNotes") |  |  |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`InvertedTurn`](#music21.expressions.InvertedTurn "music21.expressions.InvertedTurn") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## Mordent

class music21.expressions.Mordent(*\**, *accidental: [Accidental](modulePitch.html#music21.pitch.Accidental "music21.pitch.Accidental") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\*\*keywords*)[[source]](../_modules/music21/expressions.html#Mordent)
:   A normal Mordent – goes downwards and has a line through it.

    Note that some computer terminology calls this one an inverted mordent, but this
    is a modern term. See Apel, *Harvard Dictionary of Music*, “Mordent”:

    ```python
    A musical ornament consisting of the alternation of the written note
    with the note immediately below it.
    ```

    A mordent has the size of a second, of some form, depending on the note
    that will have the mordent, the current key signature in that note’s context, as
    well as any accidental on the mordent itself.

    e.g. Mordent without accidentals in default key (no flats or sharps)

    ```python
    >>> m = expressions.Mordent()
    >>> m.direction
    'down'
    >>> m.getSize(note.Note('C4'))
    <music21.interval.Interval m-2>
    >>> m.getSize(note.Note('B3'))
    <music21.interval.Interval M-2>
    ```

    e.g. Mordent with flat, in default key (no flats or sharps)

    ```python
    >>> mFlat = expressions.Mordent(accidental=pitch.Accidental('flat'))
    >>> mFlat.direction
    'down'
    >>> mFlat.getSize(note.Note('C4'))
    <music21.interval.Interval M-2>
    >>> mFlat.getSize(note.Note('B3'))
    <music21.interval.Interval A-2>
    ```

    e.g. Mordent without accidentals, in key with one flat

    ```python
    >>> oneFlat = key.KeySignature(-1)
    >>> mNotFlat = expressions.Mordent()
    >>> mNotFlat.direction
    'down'
    >>> mNotFlat.getSize(note.Note('C4'), keySig=oneFlat)
    <music21.interval.Interval M-2>
    >>> mNotFlat.getSize(note.Note('B3'), keySig=oneFlat)
    <music21.interval.Interval M-2>
    ```

    e.g. Mordent without accidentals, with a key from context with one flat (same results)

    ```python
    >>> noteC4 = note.Note('C4')
    >>> noteB3 = note.Note('B3')
    >>> measure = stream.Measure([oneFlat, noteC4, noteB3])
    >>> mNotFlatWithKeyFromContext = expressions.Mordent()
    >>> mNotFlatWithKeyFromContext.direction
    'down'
    >>> mNotFlatWithKeyFromContext.getSize(noteC4)
    <music21.interval.Interval M-2>
    >>> mNotFlatWithKeyFromContext.getSize(noteB3)
    <music21.interval.Interval M-2>
    ```

    * Changed in v7: Mordent sizes are GenericIntervals – as was originally
      intended but programmed incorrectly.
    * Changed in v9: Support an accidental on Mordent. This also adds the concept of
      an ornamental pitch that is processed by makeAccidentals.
      The size property has been removed and replaced with .getSize() (which requires
      a srcObj and optional keySig param). Added optional keySig param to
      .realize() as well.

[`Mordent`](#music21.expressions.Mordent "music21.expressions.Mordent") bases

* [`GeneralMordent`](#music21.expressions.GeneralMordent "music21.expressions.GeneralMordent")
* [`Ornament`](#music21.expressions.Ornament "music21.expressions.Ornament")
* [`Expression`](#music21.expressions.Expression "music21.expressions.Expression")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`Mordent`](#music21.expressions.Mordent "music21.expressions.Mordent") read-only properties

Read-only properties inherited from [`GeneralMordent`](#music21.expressions.GeneralMordent "music21.expressions.GeneralMordent"):

|  |  |  |
| --- | --- | --- |
| * [`direction`](#music21.expressions.GeneralMordent.direction "music21.expressions.GeneralMordent.direction") * [`name`](#music21.expressions.GeneralMordent.name "music21.expressions.GeneralMordent.name") | * [`ornamentalPitch`](#music21.expressions.GeneralMordent.ornamentalPitch "music21.expressions.GeneralMordent.ornamentalPitch") | * [`ornamentalPitches`](#music21.expressions.GeneralMordent.ornamentalPitches "music21.expressions.GeneralMordent.ornamentalPitches") |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`Mordent`](#music21.expressions.Mordent "music21.expressions.Mordent") read/write properties

Read/write properties inherited from [`GeneralMordent`](#music21.expressions.GeneralMordent "music21.expressions.GeneralMordent"):

|  |  |  |
| --- | --- | --- |
| * [`accidental`](#music21.expressions.GeneralMordent.accidental "music21.expressions.GeneralMordent.accidental") |  |  |

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`Mordent`](#music21.expressions.Mordent "music21.expressions.Mordent") methods

Methods inherited from [`GeneralMordent`](#music21.expressions.GeneralMordent "music21.expressions.GeneralMordent"):

|  |  |  |
| --- | --- | --- |
| * [`getSize()`](#music21.expressions.GeneralMordent.getSize "music21.expressions.GeneralMordent.getSize") * [`realize()`](#music21.expressions.GeneralMordent.realize "music21.expressions.GeneralMordent.realize") | * [`resolveOrnamentalPitches()`](#music21.expressions.GeneralMordent.resolveOrnamentalPitches "music21.expressions.GeneralMordent.resolveOrnamentalPitches") | * [`updateAccidentalDisplay()`](#music21.expressions.GeneralMordent.updateAccidentalDisplay "music21.expressions.GeneralMordent.updateAccidentalDisplay") |

Methods inherited from [`Ornament`](#music21.expressions.Ornament "music21.expressions.Ornament"):

|  |  |  |
| --- | --- | --- |
| * [`fillListOfRealizedNotes()`](#music21.expressions.Ornament.fillListOfRealizedNotes "music21.expressions.Ornament.fillListOfRealizedNotes") |  |  |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`Mordent`](#music21.expressions.Mordent "music21.expressions.Mordent") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## Ornament

class music21.expressions.Ornament(*\*\*keywords*)[[source]](../_modules/music21/expressions.html#Ornament)
:   An Ornament is a type of Expression that, when attached to a Note
    (in the future: Notes) can transform into the main note.

    All ornaments have an .autoScale boolean which determines
    whether to shrink (not currently to expand) the ornament if the
    note it is attached to is too short to realize.

[`Ornament`](#music21.expressions.Ornament "music21.expressions.Ornament") bases

* [`Expression`](#music21.expressions.Expression "music21.expressions.Expression")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`Ornament`](#music21.expressions.Ornament "music21.expressions.Ornament") read-only properties

Ornament.ornamentalPitches
:   Only implemented in Turn, GeneralMordent, and Trill.

Read-only properties inherited from [`Expression`](#music21.expressions.Expression "music21.expressions.Expression"):

|  |  |  |
| --- | --- | --- |
| * [`name`](#music21.expressions.Expression.name "music21.expressions.Expression.name") |  |  |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`Ornament`](#music21.expressions.Ornament "music21.expressions.Ornament") read/write properties

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`Ornament`](#music21.expressions.Ornament "music21.expressions.Ornament") methods

Ornament.fillListOfRealizedNotes(*srcObj: [note.Note](moduleNote.html#music21.note.Note "music21.note.Note") | [note.Unpitched](moduleNote.html#music21.note.Unpitched "music21.note.Unpitched")*, *fillObjects: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[note.Note](moduleNote.html#music21.note.Note "music21.note.Note") | [note.Unpitched](moduleNote.html#music21.note.Unpitched "music21.note.Unpitched")]*, *transposeInterval: [interval.IntervalBase](moduleInterval.html#music21.interval.IntervalBase "music21.interval.IntervalBase")*, *\**, *useQL: OffsetQL | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/expressions.html#Ornament.fillListOfRealizedNotes)
:   Used by trills and mordents to fill out their realization.

Ornament.realize(*srcObj: [note.Note](moduleNote.html#music21.note.Note "music21.note.Note") | [note.Unpitched](moduleNote.html#music21.note.Unpitched "music21.note.Unpitched")*, *\**, *keySig: [key.KeySignature](moduleKey.html#music21.key.KeySignature "music21.key.KeySignature") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *inPlace: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[note.Note](moduleNote.html#music21.note.Note "music21.note.Note") | [note.Unpitched](moduleNote.html#music21.note.Unpitched "music21.note.Unpitched")], [note.Note](moduleNote.html#music21.note.Note "music21.note.Note") | [note.Unpitched](moduleNote.html#music21.note.Unpitched "music21.note.Unpitched") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[note.Note](moduleNote.html#music21.note.Note "music21.note.Note") | [note.Unpitched](moduleNote.html#music21.note.Unpitched "music21.note.Unpitched")]][[source]](../_modules/music21/expressions.html#Ornament.realize)
:   subclassable method call that takes a sourceObject and optional keySig
    and returns a three-element tuple of a list of notes before the
    “main note” or the result of the expression if it gobbles up the entire note,
    the “main note” itself (or None) to keep processing for ornaments,
    and a list of notes after the “main note”.

    * New in v8: inPlace boolean; note that some ornaments
      might not return a Note in the second position at all (such as trills)
      so inPlace does nothing.
    * Changed in v9: Optional keySig can be passed in (useful in cases where there
      is no keySig in srcObj’s context, or where a different keySig is desired).

Ornament.resolveOrnamentalPitches(*srcObj: [note.GeneralNote](moduleNote.html#music21.note.GeneralNote "music21.note.GeneralNote")*, *\**, *keySig: [key.KeySignature](moduleKey.html#music21.key.KeySignature "music21.key.KeySignature") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](../_modules/music21/expressions.html#Ornament.resolveOrnamentalPitches)
:   Only implemented in Turn, GeneralMordent, and Trill.

Ornament.updateAccidentalDisplay(*\**, *pitchPast: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *pitchPastMeasure: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *otherSimultaneousPitches: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *alteredPitches: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *cautionaryPitchClass: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *cautionaryAll: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *overrideStatus: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *cautionaryNotImmediateRepeat: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/expressions.html#Ornament.updateAccidentalDisplay)
:   Only implemented in Turn, GeneralMordent, and Trill.

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`Ornament`](#music21.expressions.Ornament "music21.expressions.Ornament") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## PedalBounce

class music21.expressions.PedalBounce(*\*\*keywords*)[[source]](../_modules/music21/expressions.html#PedalBounce)
:   This object, when seen in a PedalMark spanner, represents an up/down bounce
    of the pedal.

[`PedalBounce`](#music21.expressions.PedalBounce "music21.expressions.PedalBounce") bases

* [`PedalObject`](#music21.expressions.PedalObject "music21.expressions.PedalObject")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`PedalBounce`](#music21.expressions.PedalBounce "music21.expressions.PedalBounce") read-only properties

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`PedalBounce`](#music21.expressions.PedalBounce "music21.expressions.PedalBounce") read/write properties

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`PedalBounce`](#music21.expressions.PedalBounce "music21.expressions.PedalBounce") methods

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`PedalBounce`](#music21.expressions.PedalBounce "music21.expressions.PedalBounce") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## PedalForm

class music21.expressions.PedalForm(*\*values*)[[source]](../_modules/music21/expressions.html#PedalForm)

[`PedalForm`](#music21.expressions.PedalForm "music21.expressions.PedalForm") bases

* [`StrEnum`](moduleCommonEnums.html#music21.common.enums.StrEnum "music21.common.enums.StrEnum")

## PedalGapEnd

class music21.expressions.PedalGapEnd(*\*\*keywords*)[[source]](../_modules/music21/expressions.html#PedalGapEnd)
:   This object, when seen in a PedalMark spanner, represents the reappearance of
    the pedal line.

[`PedalGapEnd`](#music21.expressions.PedalGapEnd "music21.expressions.PedalGapEnd") bases

* [`PedalObject`](#music21.expressions.PedalObject "music21.expressions.PedalObject")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`PedalGapEnd`](#music21.expressions.PedalGapEnd "music21.expressions.PedalGapEnd") read-only properties

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`PedalGapEnd`](#music21.expressions.PedalGapEnd "music21.expressions.PedalGapEnd") read/write properties

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`PedalGapEnd`](#music21.expressions.PedalGapEnd "music21.expressions.PedalGapEnd") methods

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`PedalGapEnd`](#music21.expressions.PedalGapEnd "music21.expressions.PedalGapEnd") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## PedalGapStart

class music21.expressions.PedalGapStart(*\*\*keywords*)[[source]](../_modules/music21/expressions.html#PedalGapStart)
:   This object, when seen in a PedalMark spanner, represents a disappearance of
    the pedal line, usually with a TextExpression(‘simile’). The pedaling should
    continue (similarly to before), but the line is invisible during this gap.

[`PedalGapStart`](#music21.expressions.PedalGapStart "music21.expressions.PedalGapStart") bases

* [`PedalObject`](#music21.expressions.PedalObject "music21.expressions.PedalObject")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`PedalGapStart`](#music21.expressions.PedalGapStart "music21.expressions.PedalGapStart") read-only properties

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`PedalGapStart`](#music21.expressions.PedalGapStart "music21.expressions.PedalGapStart") read/write properties

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`PedalGapStart`](#music21.expressions.PedalGapStart "music21.expressions.PedalGapStart") methods

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`PedalGapStart`](#music21.expressions.PedalGapStart "music21.expressions.PedalGapStart") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## PedalMark

class music21.expressions.PedalMark(*\*spannedElements*, *\*\*keywords*)[[source]](../_modules/music21/expressions.html#PedalMark)
:   A pedal mark spanner contains a pedaled set of notes.
    The spanner starts at the moment of down-pedal, and
    ends at the moment of up-pedal. There can be any
    number of pedal “bounces” in the middle of the spanner.

    The visual form of the pedal mark can vary. The following
    examples use a pedal mark with one “bounce” in the middle:

    ```python
    Pedal marks can be lines:            |_______^________|
    Pedal marks can be normal symbolic:  Ped.    * Ped.   *
    Pedal marks can be altered symbolic: Ped.    Ped.     *
    Pedal marks can be symbol and line:  Ped.____^________|
    ```

    Pedal marks, whether lines, symbols, or a combination, can
    represent the sustain pedal (Ped.), the sostenuto pedal
    (Sost.), the soft (una corda) pedal, or (more rarely) the
    silent (muting) pedal.

    Pedal marks that are symbolic can be abbreviated: e.g. P. instead
    of Ped., S. instead of Sost.

    Pedal marks that are lines can have non-printed portions
    (gaps) in them; these are usually started with “simile”,
    but not necessarily.

[`PedalMark`](#music21.expressions.PedalMark "music21.expressions.PedalMark") bases

* [`Spanner`](moduleSpanner.html#music21.spanner.Spanner "music21.spanner.Spanner")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`PedalMark`](#music21.expressions.PedalMark "music21.expressions.PedalMark") read-only properties

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`PedalMark`](#music21.expressions.PedalMark "music21.expressions.PedalMark") read/write properties

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`PedalMark`](#music21.expressions.PedalMark "music21.expressions.PedalMark") methods

Methods inherited from [`Spanner`](moduleSpanner.html#music21.spanner.Spanner "music21.spanner.Spanner"):

|  |  |  |
| --- | --- | --- |
| * [`__getitem__()`](moduleSpanner.html#music21.spanner.Spanner.__getitem__ "music21.spanner.Spanner.__getitem__") * [`addSpannedElements()`](moduleSpanner.html#music21.spanner.Spanner.addSpannedElements "music21.spanner.Spanner.addSpannedElements") * [`fill()`](moduleSpanner.html#music21.spanner.Spanner.fill "music21.spanner.Spanner.fill") * [`getFirst()`](moduleSpanner.html#music21.spanner.Spanner.getFirst "music21.spanner.Spanner.getFirst") * [`getLast()`](moduleSpanner.html#music21.spanner.Spanner.getLast "music21.spanner.Spanner.getLast") | * [`getSpannedElementIds()`](moduleSpanner.html#music21.spanner.Spanner.getSpannedElementIds "music21.spanner.Spanner.getSpannedElementIds") * [`getSpannedElements()`](moduleSpanner.html#music21.spanner.Spanner.getSpannedElements "music21.spanner.Spanner.getSpannedElements") * [`getSpannedElementsByClass()`](moduleSpanner.html#music21.spanner.Spanner.getSpannedElementsByClass "music21.spanner.Spanner.getSpannedElementsByClass") * [`hasSpannedElement()`](moduleSpanner.html#music21.spanner.Spanner.hasSpannedElement "music21.spanner.Spanner.hasSpannedElement") * [`insertFirstSpannedElement()`](moduleSpanner.html#music21.spanner.Spanner.insertFirstSpannedElement "music21.spanner.Spanner.insertFirstSpannedElement") | * [`isFirst()`](moduleSpanner.html#music21.spanner.Spanner.isFirst "music21.spanner.Spanner.isFirst") * [`isLast()`](moduleSpanner.html#music21.spanner.Spanner.isLast "music21.spanner.Spanner.isLast") * [`purgeLocations()`](moduleSpanner.html#music21.spanner.Spanner.purgeLocations "music21.spanner.Spanner.purgeLocations") * [`purgeOrphans()`](moduleSpanner.html#music21.spanner.Spanner.purgeOrphans "music21.spanner.Spanner.purgeOrphans") * [`replaceSpannedElement()`](moduleSpanner.html#music21.spanner.Spanner.replaceSpannedElement "music21.spanner.Spanner.replaceSpannedElement") |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") | * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") | * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`PedalMark`](#music21.expressions.PedalMark "music21.expressions.PedalMark") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## PedalObject

class music21.expressions.PedalObject(*\*\*keywords*)[[source]](../_modules/music21/expressions.html#PedalObject)
:   Base class of individual objects that mark various transitions
    in a PedalMark spanner.

[`PedalObject`](#music21.expressions.PedalObject "music21.expressions.PedalObject") bases

* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`PedalObject`](#music21.expressions.PedalObject "music21.expressions.PedalObject") read-only properties

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`PedalObject`](#music21.expressions.PedalObject "music21.expressions.PedalObject") read/write properties

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`PedalObject`](#music21.expressions.PedalObject "music21.expressions.PedalObject") methods

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`PedalObject`](#music21.expressions.PedalObject "music21.expressions.PedalObject") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## PedalType

class music21.expressions.PedalType(*\*values*)[[source]](../_modules/music21/expressions.html#PedalType)

[`PedalType`](#music21.expressions.PedalType "music21.expressions.PedalType") bases

* [`StrEnum`](moduleCommonEnums.html#music21.common.enums.StrEnum "music21.common.enums.StrEnum")

## RehearsalMark

class music21.expressions.RehearsalMark(*content=None*, *\**, *numbering=None*, *\*\*keywords*)[[source]](../_modules/music21/expressions.html#RehearsalMark)
:   A rehearsal mark is a type of Expression that designates a rehearsal
    marking, such as A., B., etc.

    Takes two inputs, content (‘B’, 5, ‘III’) and an optional numbering system which
    is helpful for getting the next rehearsal mark.

    ```python
    >>> rm = expressions.RehearsalMark('B')
    >>> rm
    <music21.expressions.RehearsalMark 'B'>
    ```

[`RehearsalMark`](#music21.expressions.RehearsalMark "music21.expressions.RehearsalMark") bases

* [`Expression`](#music21.expressions.Expression "music21.expressions.Expression")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`RehearsalMark`](#music21.expressions.RehearsalMark "music21.expressions.RehearsalMark") read-only properties

Read-only properties inherited from [`Expression`](#music21.expressions.Expression "music21.expressions.Expression"):

|  |  |  |
| --- | --- | --- |
| * [`name`](#music21.expressions.Expression.name "music21.expressions.Expression.name") |  |  |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`RehearsalMark`](#music21.expressions.RehearsalMark "music21.expressions.RehearsalMark") read/write properties

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`RehearsalMark`](#music21.expressions.RehearsalMark "music21.expressions.RehearsalMark") methods

RehearsalMark.nextContent()[[source]](../_modules/music21/expressions.html#RehearsalMark.nextContent)
:   Return the next content based on the numbering

    ```python
    >>> expressions.RehearsalMark('A').nextContent()
    'B'
    ```

    ```python
    >>> expressions.RehearsalMark('II').nextContent()
    'III'
    ```

    ```python
    >>> expressions.RehearsalMark('IV').nextContent()
    'V'
    ```

    ```python
    >>> expressions.RehearsalMark(7).nextContent()
    8
    ```

    ```python
    >>> expressions.RehearsalMark('Z').nextContent()
    'AA'
    ```

    With rehearsal mark ‘I’ default is to consider it
    as a roman numeral:

    ```python
    >>> expressions.RehearsalMark('I').nextContent()
    'II'
    ```

    Specify numbering directly to avoid problems:

    ```python
    >>> expressions.RehearsalMark('I', numbering='alphabetical').nextContent()
    'J'
    ```

RehearsalMark.nextMark()[[source]](../_modules/music21/expressions.html#RehearsalMark.nextMark)
:   Return the next rehearsal mark.

    ```python
    >>> rm = expressions.RehearsalMark('C')
    >>> rm.nextMark()
    <music21.expressions.RehearsalMark 'D'>
    ```

    ```python
    >>> rm = expressions.RehearsalMark('IV', numbering='roman')
    >>> nm = rm.nextMark()
    >>> nm.content
    'V'
    >>> nm.numbering
    'roman'
    ```

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`RehearsalMark`](#music21.expressions.RehearsalMark "music21.expressions.RehearsalMark") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## Schleifer

class music21.expressions.Schleifer(*\*\*keywords*)[[source]](../_modules/music21/expressions.html#Schleifer)
:   A slide or culee

    * Changed in v7: size is a Generic second. removed unused nachschlag component.

[`Schleifer`](#music21.expressions.Schleifer "music21.expressions.Schleifer") bases

* [`Ornament`](#music21.expressions.Ornament "music21.expressions.Ornament")
* [`Expression`](#music21.expressions.Expression "music21.expressions.Expression")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`Schleifer`](#music21.expressions.Schleifer "music21.expressions.Schleifer") read-only properties

Read-only properties inherited from [`Ornament`](#music21.expressions.Ornament "music21.expressions.Ornament"):

|  |  |  |
| --- | --- | --- |
| * [`ornamentalPitches`](#music21.expressions.Ornament.ornamentalPitches "music21.expressions.Ornament.ornamentalPitches") |  |  |

Read-only properties inherited from [`Expression`](#music21.expressions.Expression "music21.expressions.Expression"):

|  |  |  |
| --- | --- | --- |
| * [`name`](#music21.expressions.Expression.name "music21.expressions.Expression.name") |  |  |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`Schleifer`](#music21.expressions.Schleifer "music21.expressions.Schleifer") read/write properties

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`Schleifer`](#music21.expressions.Schleifer "music21.expressions.Schleifer") methods

Methods inherited from [`Ornament`](#music21.expressions.Ornament "music21.expressions.Ornament"):

|  |  |  |
| --- | --- | --- |
| * [`fillListOfRealizedNotes()`](#music21.expressions.Ornament.fillListOfRealizedNotes "music21.expressions.Ornament.fillListOfRealizedNotes") * [`realize()`](#music21.expressions.Ornament.realize "music21.expressions.Ornament.realize") | * [`resolveOrnamentalPitches()`](#music21.expressions.Ornament.resolveOrnamentalPitches "music21.expressions.Ornament.resolveOrnamentalPitches") | * [`updateAccidentalDisplay()`](#music21.expressions.Ornament.updateAccidentalDisplay "music21.expressions.Ornament.updateAccidentalDisplay") |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`Schleifer`](#music21.expressions.Schleifer "music21.expressions.Schleifer") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## Shake

class music21.expressions.Shake(*\*\*keywords*)[[source]](../_modules/music21/expressions.html#Shake)
:   A slower trill.

    ```python
    >>> shake = expressions.Shake()
    >>> shake.quarterLength
    0.25
    ```

[`Shake`](#music21.expressions.Shake "music21.expressions.Shake") bases

* [`Trill`](#music21.expressions.Trill "music21.expressions.Trill")
* [`Ornament`](#music21.expressions.Ornament "music21.expressions.Ornament")
* [`Expression`](#music21.expressions.Expression "music21.expressions.Expression")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`Shake`](#music21.expressions.Shake "music21.expressions.Shake") read-only properties

Read-only properties inherited from [`Trill`](#music21.expressions.Trill "music21.expressions.Trill"):

|  |  |  |
| --- | --- | --- |
| * [`direction`](#music21.expressions.Trill.direction "music21.expressions.Trill.direction") * [`name`](#music21.expressions.Trill.name "music21.expressions.Trill.name") | * [`ornamentalPitch`](#music21.expressions.Trill.ornamentalPitch "music21.expressions.Trill.ornamentalPitch") | * [`ornamentalPitches`](#music21.expressions.Trill.ornamentalPitches "music21.expressions.Trill.ornamentalPitches") |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`Shake`](#music21.expressions.Shake "music21.expressions.Shake") read/write properties

Read/write properties inherited from [`Trill`](#music21.expressions.Trill "music21.expressions.Trill"):

|  |  |  |
| --- | --- | --- |
| * [`accidental`](#music21.expressions.Trill.accidental "music21.expressions.Trill.accidental") |  |  |

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`Shake`](#music21.expressions.Shake "music21.expressions.Shake") methods

Methods inherited from [`Trill`](#music21.expressions.Trill "music21.expressions.Trill"):

|  |  |  |
| --- | --- | --- |
| * [`getSize()`](#music21.expressions.Trill.getSize "music21.expressions.Trill.getSize") * [`realize()`](#music21.expressions.Trill.realize "music21.expressions.Trill.realize") | * [`resolveOrnamentalPitches()`](#music21.expressions.Trill.resolveOrnamentalPitches "music21.expressions.Trill.resolveOrnamentalPitches") * [`splitClient()`](#music21.expressions.Trill.splitClient "music21.expressions.Trill.splitClient") | * [`updateAccidentalDisplay()`](#music21.expressions.Trill.updateAccidentalDisplay "music21.expressions.Trill.updateAccidentalDisplay") |

Methods inherited from [`Ornament`](#music21.expressions.Ornament "music21.expressions.Ornament"):

|  |  |  |
| --- | --- | --- |
| * [`fillListOfRealizedNotes()`](#music21.expressions.Ornament.fillListOfRealizedNotes "music21.expressions.Ornament.fillListOfRealizedNotes") |  |  |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`Shake`](#music21.expressions.Shake "music21.expressions.Shake") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## Tremolo

class music21.expressions.Tremolo(*\*\*keywords*)[[source]](../_modules/music21/expressions.html#Tremolo)
:   A tremolo ornament represents a single-note tremolo, whether measured or unmeasured.

    ```python
    >>> n = note.Note(type='quarter')
    >>> trem = expressions.Tremolo()
    >>> trem.measured = True  # default
    >>> trem.numberOfMarks = 3  # default
    ```

    ```python
    >>> trem.numberOfMarks = 'Hi'
    Traceback (most recent call last):
    music21.expressions.TremoloException: Number of marks must be a number from 0 to 8
    ```

    ```python
    >>> trem.numberOfMarks = -1
    Traceback (most recent call last):
    music21.expressions.TremoloException: Number of marks must be a number from 0 to 8
    ```

    TODO: (someday) realize triplet Tremolos, etc. differently from other tremolos.
    TODO: deal with unmeasured tremolos.

[`Tremolo`](#music21.expressions.Tremolo "music21.expressions.Tremolo") bases

* [`Ornament`](#music21.expressions.Ornament "music21.expressions.Ornament")
* [`Expression`](#music21.expressions.Expression "music21.expressions.Expression")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`Tremolo`](#music21.expressions.Tremolo "music21.expressions.Tremolo") read-only properties

Read-only properties inherited from [`Ornament`](#music21.expressions.Ornament "music21.expressions.Ornament"):

|  |  |  |
| --- | --- | --- |
| * [`ornamentalPitches`](#music21.expressions.Ornament.ornamentalPitches "music21.expressions.Ornament.ornamentalPitches") |  |  |

Read-only properties inherited from [`Expression`](#music21.expressions.Expression "music21.expressions.Expression"):

|  |  |  |
| --- | --- | --- |
| * [`name`](#music21.expressions.Expression.name "music21.expressions.Expression.name") |  |  |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`Tremolo`](#music21.expressions.Tremolo "music21.expressions.Tremolo") read/write properties

Tremolo.numberOfMarks
:   The number of marks on the note. Currently, completely controls playback.

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`Tremolo`](#music21.expressions.Tremolo "music21.expressions.Tremolo") methods

Tremolo.realize(*srcObj: [note.Note](moduleNote.html#music21.note.Note "music21.note.Note") | [note.Unpitched](moduleNote.html#music21.note.Unpitched "music21.note.Unpitched")*, *\**, *keySig: [key.KeySignature](moduleKey.html#music21.key.KeySignature "music21.key.KeySignature") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *inPlace: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[note.Note](moduleNote.html#music21.note.Note "music21.note.Note") | [note.Unpitched](moduleNote.html#music21.note.Unpitched "music21.note.Unpitched")], [note.Note](moduleNote.html#music21.note.Note "music21.note.Note") | [note.Unpitched](moduleNote.html#music21.note.Unpitched "music21.note.Unpitched") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[note.Note](moduleNote.html#music21.note.Note "music21.note.Note") | [note.Unpitched](moduleNote.html#music21.note.Unpitched "music21.note.Unpitched")]][[source]](../_modules/music21/expressions.html#Tremolo.realize)
:   Realize the ornament

    ```python
    >>> n = note.Note(type='quarter')
    >>> trem = expressions.Tremolo()
    >>> trem.measured = True  # default
    >>> trem.numberOfMarks = 3  # default
    >>> trem.realize(n)
    ([<music21.note.Note C>, <music21.note.Note C>, <music21.note.Note C>,
      <music21.note.Note C>, <music21.note.Note C>, <music21.note.Note C>,
      <music21.note.Note C>, <music21.note.Note C>], None, [])
    >>> c2 = trem.realize(n)[0]
    >>> [ts.quarterLength for ts in c2]
    [0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125]
    ```

    Same thing with Streams:

    ```python
    >>> n = note.Note(type='quarter')
    >>> trem = expressions.Tremolo()
    >>> n.expressions.append(trem)
    >>> s = stream.Stream()
    >>> s.append(n)
    >>> s.show('text')
    {0.0} <music21.note.Note C>
    ```

    ```python
    >>> y = stream.makeNotation.realizeOrnaments(s)
    >>> y.show('text')
    {0.0} <music21.note.Note C>
    {0.125} <music21.note.Note C>
    {0.25} <music21.note.Note C>
    {0.375} <music21.note.Note C>
    {0.5} <music21.note.Note C>
    {0.625} <music21.note.Note C>
    {0.75} <music21.note.Note C>
    {0.875} <music21.note.Note C>
    ```

    ```python
    >>> trem.numberOfMarks = 1
    >>> y = stream.makeNotation.realizeOrnaments(s)
    >>> y.show('text')
    {0.0} <music21.note.Note C>
    {0.5} <music21.note.Note C>
    ```

Methods inherited from [`Ornament`](#music21.expressions.Ornament "music21.expressions.Ornament"):

|  |  |  |
| --- | --- | --- |
| * [`fillListOfRealizedNotes()`](#music21.expressions.Ornament.fillListOfRealizedNotes "music21.expressions.Ornament.fillListOfRealizedNotes") | * [`resolveOrnamentalPitches()`](#music21.expressions.Ornament.resolveOrnamentalPitches "music21.expressions.Ornament.resolveOrnamentalPitches") | * [`updateAccidentalDisplay()`](#music21.expressions.Ornament.updateAccidentalDisplay "music21.expressions.Ornament.updateAccidentalDisplay") |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`Tremolo`](#music21.expressions.Tremolo "music21.expressions.Tremolo") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## TremoloSpanner

class music21.expressions.TremoloSpanner(*\*spannedElements*, *\*\*keywords*)[[source]](../_modules/music21/expressions.html#TremoloSpanner)
:   A tremolo that spans multiple notes

    ```python
    >>> ts = expressions.TremoloSpanner()
    >>> n1 = note.Note('C')
    >>> n2 = note.Note('D')
    >>> ts.addSpannedElements([n1, n2])
    >>> ts.numberOfMarks = 2
    >>> ts
    <music21.expressions.TremoloSpanner <music21.note.Note C><music21.note.Note D>>
    ```

    ```python
    >>> ts.numberOfMarks = -1
    Traceback (most recent call last):
    music21.expressions.TremoloException: Number of marks must be a number from 0 to 8
    ```

[`TremoloSpanner`](#music21.expressions.TremoloSpanner "music21.expressions.TremoloSpanner") bases

* [`Spanner`](moduleSpanner.html#music21.spanner.Spanner "music21.spanner.Spanner")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`TremoloSpanner`](#music21.expressions.TremoloSpanner "music21.expressions.TremoloSpanner") read-only properties

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`TremoloSpanner`](#music21.expressions.TremoloSpanner "music21.expressions.TremoloSpanner") read/write properties

TremoloSpanner.numberOfMarks
:   The number of marks on the note. Will eventually control playback.

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`TremoloSpanner`](#music21.expressions.TremoloSpanner "music21.expressions.TremoloSpanner") methods

Methods inherited from [`Spanner`](moduleSpanner.html#music21.spanner.Spanner "music21.spanner.Spanner"):

|  |  |  |
| --- | --- | --- |
| * [`__getitem__()`](moduleSpanner.html#music21.spanner.Spanner.__getitem__ "music21.spanner.Spanner.__getitem__") * [`addSpannedElements()`](moduleSpanner.html#music21.spanner.Spanner.addSpannedElements "music21.spanner.Spanner.addSpannedElements") * [`fill()`](moduleSpanner.html#music21.spanner.Spanner.fill "music21.spanner.Spanner.fill") * [`getFirst()`](moduleSpanner.html#music21.spanner.Spanner.getFirst "music21.spanner.Spanner.getFirst") * [`getLast()`](moduleSpanner.html#music21.spanner.Spanner.getLast "music21.spanner.Spanner.getLast") | * [`getSpannedElementIds()`](moduleSpanner.html#music21.spanner.Spanner.getSpannedElementIds "music21.spanner.Spanner.getSpannedElementIds") * [`getSpannedElements()`](moduleSpanner.html#music21.spanner.Spanner.getSpannedElements "music21.spanner.Spanner.getSpannedElements") * [`getSpannedElementsByClass()`](moduleSpanner.html#music21.spanner.Spanner.getSpannedElementsByClass "music21.spanner.Spanner.getSpannedElementsByClass") * [`hasSpannedElement()`](moduleSpanner.html#music21.spanner.Spanner.hasSpannedElement "music21.spanner.Spanner.hasSpannedElement") * [`insertFirstSpannedElement()`](moduleSpanner.html#music21.spanner.Spanner.insertFirstSpannedElement "music21.spanner.Spanner.insertFirstSpannedElement") | * [`isFirst()`](moduleSpanner.html#music21.spanner.Spanner.isFirst "music21.spanner.Spanner.isFirst") * [`isLast()`](moduleSpanner.html#music21.spanner.Spanner.isLast "music21.spanner.Spanner.isLast") * [`purgeLocations()`](moduleSpanner.html#music21.spanner.Spanner.purgeLocations "music21.spanner.Spanner.purgeLocations") * [`purgeOrphans()`](moduleSpanner.html#music21.spanner.Spanner.purgeOrphans "music21.spanner.Spanner.purgeOrphans") * [`replaceSpannedElement()`](moduleSpanner.html#music21.spanner.Spanner.replaceSpannedElement "music21.spanner.Spanner.replaceSpannedElement") |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") | * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") | * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`TremoloSpanner`](#music21.expressions.TremoloSpanner "music21.expressions.TremoloSpanner") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## Trill

class music21.expressions.Trill(*\**, *accidental: [Accidental](modulePitch.html#music21.pitch.Accidental "music21.pitch.Accidental") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\*\*keywords*)[[source]](../_modules/music21/expressions.html#Trill)
:   A basic trill marker without the trill extension

    ```python
    >>> tr = expressions.Trill()
    >>> tr.placement
    'above'
    >>> tr.getSize(note.Note('C4'))
    <music21.interval.Interval M2>
    >>> tr.getSize(note.Note('B4'))
    <music21.interval.Interval m2>
    ```

    Trills have a .nachschlag attribute which determines whether there
    should be extra gracenotes at the end of the trill.

    ```python
    >>> tr.nachschlag
    False
    >>> tr.nachschlag = True
    ```

    The Trill also has a “quarterLength” attribute that sets how long
    each trill note should be. Defaults to 32nd note:

    ```python
    >>> tr.quarterLength
    0.125
    >>> tr.quarterLength == duration.Duration('32nd').quarterLength
    True
    ```

    * Changed in v7: the size should be a generic second.
    * Changed in v9: Support an accidental on trills. This also adds the concept of
      an ornamental pitch that is processed by makeAccidentals.
      The size property has been removed and replaced with .getSize() (which requires
      a srcObj and optional keySig param). Added optional keySig param to
      .realize() as well.

[`Trill`](#music21.expressions.Trill "music21.expressions.Trill") bases

* [`Ornament`](#music21.expressions.Ornament "music21.expressions.Ornament")
* [`Expression`](#music21.expressions.Expression "music21.expressions.Expression")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`Trill`](#music21.expressions.Trill "music21.expressions.Trill") read-only properties

Trill.direction
:   The direction of the trill’s ornamental pitch from the main note.
    Can be ‘up’ or ‘down’.

Trill.name
:   returns the name of the Trill, which is generally the class name
    lowercased, with spaces where a new capital occurs. The name also
    will include the accidental, if it exists.

    Subclasses can override this as necessary.

    ```python
    >>> trill = expressions.Trill()
    >>> trill.name
    'trill'
    ```

    ```python
    >>> doubleSharpedTrill = expressions.Trill(accidental=pitch.Accidental('double-sharp'))
    >>> doubleSharpedTrill.name
    'trill (double-sharp)'
    ```

Trill.ornamentalPitch
:   Returns the trill’s ornamentalPitch. If resolveOrnamentalPitches
    has not yet been called, None is returned.

Trill.ornamentalPitches
:   Returns any ornamental pitch that has been resolved (see
    resolveOrnamentalPitches, which must be called first, or an
    empty tuple will be returned).

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`Trill`](#music21.expressions.Trill "music21.expressions.Trill") read/write properties

Trill.accidental
:   This is the Trill’s accidental. Whether or not it is visible is dictated by
    the accidental’s displayStatus.

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`Trill`](#music21.expressions.Trill "music21.expressions.Trill") methods

Trill.getSize(*srcObj: [note.GeneralNote](moduleNote.html#music21.note.GeneralNote "music21.note.GeneralNote")*, *\**, *keySig: [key.KeySignature](moduleKey.html#music21.key.KeySignature "music21.key.KeySignature") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [interval.IntervalBase](moduleInterval.html#music21.interval.IntervalBase "music21.interval.IntervalBase")[[source]](../_modules/music21/expressions.html#Trill.getSize)
:   Returns the size of the trill’s interval, given a source note and
    an optional key signature. If the key signature is not specified, the
    source note’s context is searched for the current key signature, and if
    there is no such key signature, a key signature with no sharps and no flats
    will be used. Any accidental that has been set on the trill will also
    be taken into account.

    If keySig is specified, this can be considered to be a theoretical question:
    “If this particular trill were to be attached to this note, in this key,
    what would the size of the trill interval be?”

Trill.realize(*srcObj: [note.Note](moduleNote.html#music21.note.Note "music21.note.Note") | [note.Unpitched](moduleNote.html#music21.note.Unpitched "music21.note.Unpitched")*, *\**, *keySig: [key.KeySignature](moduleKey.html#music21.key.KeySignature "music21.key.KeySignature") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *inPlace: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[note.Note](moduleNote.html#music21.note.Note "music21.note.Note") | [note.Unpitched](moduleNote.html#music21.note.Unpitched "music21.note.Unpitched")], [note.Note](moduleNote.html#music21.note.Note "music21.note.Note") | [note.Unpitched](moduleNote.html#music21.note.Unpitched "music21.note.Unpitched") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[note.Note](moduleNote.html#music21.note.Note "music21.note.Note") | [note.Unpitched](moduleNote.html#music21.note.Unpitched "music21.note.Unpitched")]][[source]](../_modules/music21/expressions.html#Trill.realize)
:   realize a trill.

    Returns a three-element tuple:

    * The first is a list of the notes that the note was converted to.
    * The second is None because the trill “eats up” the whole note.
    * The third is a list of the notes at the end if nachschlag is True,
      and empty list if False.

    ```python
    >>> n1 = note.Note('C4')
    >>> n1.duration.type = 'eighth'
    >>> t1 = expressions.Trill()
    >>> n1.expressions.append(t1)
    >>> realization = t1.realize(n1)
    >>> realization
    ([<music21.note.Note C>,
      <music21.note.Note D>,
      <music21.note.Note C>,
      <music21.note.Note D>], None, [])
    >>> realization[0][0].quarterLength
    0.125
    >>> realization[0][0].pitch.octave
    4
    ```

    When inside a stream, the realizations will consult the current key to see
    if it should be a whole-step or half-step trill:

    ```python
    >>> m = stream.Measure()
    >>> k1 = key.Key('D-')
    >>> m.insert(0, k1)
    >>> m.append(n1)
    >>> t1.realize(n1)
    ([<music21.note.Note C>,
      <music21.note.Note D->,
      <music21.note.Note C>,
      <music21.note.Note D->], None, [])
    ```

    Note that if the key contradicts the note of the trill, for instance, here
    having a C-natural rather than a C-sharp, we do not correct the C to C#.

    ```python
    >>> k2 = key.Key('A')
    >>> m.replace(k1, k2)
    >>> t1.realize(n1)
    ([<music21.note.Note C>,
      <music21.note.Note D>,
      <music21.note.Note C>,
      <music21.note.Note D>], None, [])
    ```

    This can lead to certain unusual circumstances such as augmented second trills
    which are technically correct, but probably not what a performer exprects.

    ```python
    >>> k3 = key.Key('E')
    >>> m.replace(k2, k3)
    >>> t1.realize(n1)
    ([<music21.note.Note C>,
      <music21.note.Note D#>,
      <music21.note.Note C>,
      <music21.note.Note D#>], None, [])
    ```

    To avoid this case, create a [`HalfStepTrill`](#music21.expressions.HalfStepTrill "music21.expressions.HalfStepTrill") or
    [`WholeStepTrill`](#music21.expressions.WholeStepTrill "music21.expressions.WholeStepTrill").

    If there is a nachschlag, it will appear in the third element of the list.

    ```python
    >>> n1.duration.type = 'quarter'
    >>> m.replace(k3, k1)  # back to D-flat major
    >>> t1.nachschlag = True
    >>> t1.realize(n1)
    ([<music21.note.Note C>,
      <music21.note.Note D->,
      <music21.note.Note C>,
      <music21.note.Note D->,
      <music21.note.Note C>,
      <music21.note.Note D->], None, [<music21.note.Note C>, <music21.note.Note B->])
    ```

    Some notes can be too short to realize if autoscale is off.

    ```python
    >>> n2 = note.Note('D4')
    >>> n2.duration.type = '32nd'
    >>> t2 = expressions.Trill()
    >>> t2.autoScale = False
    >>> t2.realize(n2)
    Traceback (most recent call last):
    music21.expressions.ExpressionException: The note is not long enough to realize a trill
    ```

    A quicker trill makes it possible:

    ```python
    >>> t2.quarterLength = duration.Duration('64th').quarterLength
    >>> t2.realize(n2)
    ([<music21.note.Note D>,
      <music21.note.Note E>], None, [])
    ```

    inPlace is not used for Trills.

Trill.resolveOrnamentalPitches(*srcObj: [note.GeneralNote](moduleNote.html#music21.note.GeneralNote "music21.note.GeneralNote")*, *\**, *keySig: [key.KeySignature](moduleKey.html#music21.key.KeySignature "music21.key.KeySignature") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](../_modules/music21/expressions.html#Trill.resolveOrnamentalPitches)
:   Computes and stores the ornamental pitch for a Trill, given the srcObj
    (can be any kind of ornamented GeneralNote) and an optional keySig.

    If keySig is None, srcNote’s context will be searched for a key signature.
    If no key signature is found, a key signature with no sharps and no flats
    will be used.

    e.g. A trill on a D in a key with no sharps or flats (ornamental pitch will be E).

    ```python
    >>> noSharpsOrFlats = key.KeySignature(0)
    >>> n2 = note.Note('D4')
    >>> trill = expressions.Trill()
    >>> trill.resolveOrnamentalPitches(n2, keySig=noSharpsOrFlats)
    >>> trill.ornamentalPitches
    (<music21.pitch.Pitch E4>,)
    >>> trill.ornamentalPitch
    <music21.pitch.Pitch E4>
    ```

Trill.splitClient(*noteList*)[[source]](../_modules/music21/expressions.html#Trill.splitClient)
:   splitClient is called by base.splitAtQuarterLength() to support splitting trills.

    ```python
    >>> n = note.Note(type='whole')
    >>> n.expressions.append(expressions.Trill())
    >>> st = n.splitAtQuarterLength(3.0)
    >>> n1, n2 = st
    >>> st.spannerList
    [<music21.expressions.TrillExtension <music21.note.Note C><music21.note.Note C>>]
    >>> n1.getSpannerSites()
    [<music21.expressions.TrillExtension <music21.note.Note C><music21.note.Note C>>]
    ```

Trill.updateAccidentalDisplay(*\**, *pitchPast: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *pitchPastMeasure: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *otherSimultaneousPitches: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *alteredPitches: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *cautionaryPitchClass: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *cautionaryAll: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *overrideStatus: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *cautionaryNotImmediateRepeat: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*)[[source]](../_modules/music21/expressions.html#Trill.updateAccidentalDisplay)
:   Updates accidental display for a Trill’s ornamental pitch.
    Defined exactly like Pitch.updateAccidentalDisplay, with two changes:
    Instead of self being the pitch to update, self is an Trill whose
    ornamentalPitch is to be updated; and we pay no attention to ties,
    since ornamental notes cannot be tied.

    These examples show a Trill whose main note is a G in a key with no sharps or
    flats, so the trill’s ornamental pitch is an A. We show various situations
    where the A might or might not end up with a natural accidental.

    If updateAccidentalDisplay is called with cautionaryAll, the A gets a (cautionary)
    natural accidental.

    ```python
    >>> noSharpsOrFlats = key.KeySignature(0)
    >>> trill1 = expressions.Trill()
    >>> trill1.resolveOrnamentalPitches(note.Note('g4'), keySig=noSharpsOrFlats)
    >>> trill1.ornamentalPitch
    <music21.pitch.Pitch A4>
    >>> trill1.ornamentalPitch.accidental is None
    True
    >>> past = [pitch.Pitch('a#4'), pitch.Pitch('c#4'), pitch.Pitch('c4')]
    >>> trill1.updateAccidentalDisplay(pitchPast=past, cautionaryAll=True)
    >>> trill1.ornamentalPitch.accidental, trill1.ornamentalPitch.accidental.displayStatus
    (<music21.pitch.Accidental natural>, True)
    ```

    If updateAccidentalDisplay is called without cautionaryAll, the A gets a natural
    accidental, because a previous A had a sharp accidental.

    ```python
    >>> trill2 = expressions.Trill()
    >>> trill2.resolveOrnamentalPitches(note.Note('g4'), keySig=noSharpsOrFlats)
    >>> trill2.ornamentalPitch
    <music21.pitch.Pitch A4>
    >>> trill2.ornamentalPitch.accidental is None
    True
    >>> past = [pitch.Pitch('a#4'), pitch.Pitch('c#4'), pitch.Pitch('c4')]
    >>> trill2.updateAccidentalDisplay(pitchPast=past)  # should add a natural
    >>> trill2.ornamentalPitch.accidental, trill2.ornamentalPitch.accidental.displayStatus
    (<music21.pitch.Accidental natural>, True)
    ```

    If updateAccidentalDisplay is called with cautionaryPitchClass=False, the A does
    not get a natural accidental because the previous A# was in a different octave.

    ```python
    >>> trill3 = expressions.Trill()
    >>> trill3.resolveOrnamentalPitches(note.Note('g4'), keySig=noSharpsOrFlats)
    >>> trill3.ornamentalPitch
    <music21.pitch.Pitch A4>
    >>> trill3.ornamentalPitch.accidental is None
    True
    >>> past = [pitch.Pitch('a#3'), pitch.Pitch('c#'), pitch.Pitch('c')]
    >>> trill3.updateAccidentalDisplay(pitchPast=past, cautionaryPitchClass=False)
    >>> trill3.ornamentalPitch.accidental is None
    True
    ```

    If we add a natural accidental to the trill (with displayStatus True), and then
    updateAccidentalDisplay is called with cautionaryPitchClass=False, the A gets a
    visible natural accidental because of that added natural accidental.

    ```python
    >>> trill4 = expressions.Trill()
    >>> natural = pitch.Accidental('natural')
    >>> natural.displayStatus = True
    >>> trill4.accidental = natural
    >>> trill4.resolveOrnamentalPitches(note.Note('g4'), keySig=noSharpsOrFlats)
    >>> trill4.ornamentalPitch
    <music21.pitch.Pitch A4>
    >>> trill4.ornamentalPitch.accidental
    <music21.pitch.Accidental natural>
    >>> trill4.ornamentalPitch.accidental.displayStatus
    True
    >>> past = [pitch.Pitch('a#3'), pitch.Pitch('c#'), pitch.Pitch('c')]
    >>> trill4.updateAccidentalDisplay(pitchPast=past, cautionaryPitchClass=False)
    >>> trill4.ornamentalPitch.accidental
    <music21.pitch.Accidental natural>
    >>> trill4.ornamentalPitch.accidental.displayStatus
    True
    ```

Methods inherited from [`Ornament`](#music21.expressions.Ornament "music21.expressions.Ornament"):

|  |  |  |
| --- | --- | --- |
| * [`fillListOfRealizedNotes()`](#music21.expressions.Ornament.fillListOfRealizedNotes "music21.expressions.Ornament.fillListOfRealizedNotes") |  |  |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`Trill`](#music21.expressions.Trill "music21.expressions.Trill") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## TrillExtension

class music21.expressions.TrillExtension(*\*spannedElements*, *\*\*keywords*)[[source]](../_modules/music21/expressions.html#TrillExtension)
:   A wavy line trill extension, placed between two notes. N
    ote that some MusicXML readers include a trill symbol with the wavy line.

    ```python
    >>> s = stream.Stream()
    >>> s.repeatAppend(note.Note(), 8)
    ```

    Create TrillExtension between notes 2 and 3

    ```python
    >>> te = expressions.TrillExtension(s.notes[1], s.notes[2])
    >>> s.append(te)  # spanner can go anywhere in the Stream
    >>> print(te)
    <music21.expressions.TrillExtension <music21.note.Note C><music21.note.Note C>>
    ```

[`TrillExtension`](#music21.expressions.TrillExtension "music21.expressions.TrillExtension") bases

* [`Spanner`](moduleSpanner.html#music21.spanner.Spanner "music21.spanner.Spanner")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`TrillExtension`](#music21.expressions.TrillExtension "music21.expressions.TrillExtension") read-only properties

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`TrillExtension`](#music21.expressions.TrillExtension "music21.expressions.TrillExtension") read/write properties

TrillExtension.placement
:   Get or set the placement as either above, below, or None.

    ```python
    >>> s = stream.Stream()
    >>> s.repeatAppend(note.Note(), 8)
    >>> te = expressions.TrillExtension(s.notes[1], s.notes[2])
    >>> te.placement = 'above'
    >>> te.placement
    'above'
    ```

    A setting of None implies that the placement will be determined
    by notation software and no particular placement is demanded.

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`TrillExtension`](#music21.expressions.TrillExtension "music21.expressions.TrillExtension") methods

Methods inherited from [`Spanner`](moduleSpanner.html#music21.spanner.Spanner "music21.spanner.Spanner"):

|  |  |  |
| --- | --- | --- |
| * [`__getitem__()`](moduleSpanner.html#music21.spanner.Spanner.__getitem__ "music21.spanner.Spanner.__getitem__") * [`addSpannedElements()`](moduleSpanner.html#music21.spanner.Spanner.addSpannedElements "music21.spanner.Spanner.addSpannedElements") * [`fill()`](moduleSpanner.html#music21.spanner.Spanner.fill "music21.spanner.Spanner.fill") * [`getFirst()`](moduleSpanner.html#music21.spanner.Spanner.getFirst "music21.spanner.Spanner.getFirst") * [`getLast()`](moduleSpanner.html#music21.spanner.Spanner.getLast "music21.spanner.Spanner.getLast") | * [`getSpannedElementIds()`](moduleSpanner.html#music21.spanner.Spanner.getSpannedElementIds "music21.spanner.Spanner.getSpannedElementIds") * [`getSpannedElements()`](moduleSpanner.html#music21.spanner.Spanner.getSpannedElements "music21.spanner.Spanner.getSpannedElements") * [`getSpannedElementsByClass()`](moduleSpanner.html#music21.spanner.Spanner.getSpannedElementsByClass "music21.spanner.Spanner.getSpannedElementsByClass") * [`hasSpannedElement()`](moduleSpanner.html#music21.spanner.Spanner.hasSpannedElement "music21.spanner.Spanner.hasSpannedElement") * [`insertFirstSpannedElement()`](moduleSpanner.html#music21.spanner.Spanner.insertFirstSpannedElement "music21.spanner.Spanner.insertFirstSpannedElement") | * [`isFirst()`](moduleSpanner.html#music21.spanner.Spanner.isFirst "music21.spanner.Spanner.isFirst") * [`isLast()`](moduleSpanner.html#music21.spanner.Spanner.isLast "music21.spanner.Spanner.isLast") * [`purgeLocations()`](moduleSpanner.html#music21.spanner.Spanner.purgeLocations "music21.spanner.Spanner.purgeLocations") * [`purgeOrphans()`](moduleSpanner.html#music21.spanner.Spanner.purgeOrphans "music21.spanner.Spanner.purgeOrphans") * [`replaceSpannedElement()`](moduleSpanner.html#music21.spanner.Spanner.replaceSpannedElement "music21.spanner.Spanner.replaceSpannedElement") |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") | * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") | * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`TrillExtension`](#music21.expressions.TrillExtension "music21.expressions.TrillExtension") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## Turn

class music21.expressions.Turn(*\**, *delay: [OrnamentDelay](moduleCommonEnums.html#music21.common.enums.OrnamentDelay "music21.common.enums.OrnamentDelay") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [Fraction](https://docs.python.org/3/library/fractions.html#fractions.Fraction "(in Python v3.14)") = <OrnamentDelay.NO\_DELAY>*, *upperAccidental: [Accidental](modulePitch.html#music21.pitch.Accidental "music21.pitch.Accidental") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *lowerAccidental: [Accidental](modulePitch.html#music21.pitch.Accidental "music21.pitch.Accidental") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\*\*keywords*)[[source]](../_modules/music21/expressions.html#Turn)
:   A turn or Gruppetto.

    * Changed in v7: size is a Generic second. removed unused nachschlag component.
    * Changed in v9: Added support for delayed vs non-delayed Turn.
    * Changed in v9: Support upper and lower accidentals on turns. This also adds
      the concept of ornamental pitches that are processed by makeAccidentals.
      The size property has been removed and replaced with .getSize() (which requires
      a srcObj and optional keySig param, as well as which=’upper’ or which=’lower’).
      Added optional keySig param to .realize() as well.

[`Turn`](#music21.expressions.Turn "music21.expressions.Turn") bases

* [`Ornament`](#music21.expressions.Ornament "music21.expressions.Ornament")
* [`Expression`](#music21.expressions.Expression "music21.expressions.Expression")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`Turn`](#music21.expressions.Turn "music21.expressions.Turn") read-only properties

Turn.isDelayed
:   Whether the Turn is delayed (i.e. between a specific note and the following note) or
    not (i.e. exactly on a specific note).

Turn.lowerOrnamentalPitch
:   Returns the turn’s lower ornamental pitch. If resolveOrnamentalPitches
    has not yet been called, None is returned.

Turn.name
:   returns the name of the Turn/InvertedTurn, which is generally the class
    name lowercased, with spaces where a new capital occurs, but also with
    a ‘delayed’ prefix, if the Turn/InvertedTurn is delayed. If the delay
    is of a specific duration, the prefix will include that duration. The
    name also will include upper and lower accidentals, if they exist.

    Subclasses can override this as necessary.

    ```python
    >>> nonDelayedTurn = expressions.Turn()
    >>> nonDelayedTurn.name
    'turn'
    ```

    ```python
    >>> from music21.common.enums import OrnamentDelay
    >>> delayedInvertedTurn = expressions.InvertedTurn(
    ...     delay=OrnamentDelay.DEFAULT_DELAY,
    ...     upperAccidental=pitch.Accidental('sharp'),
    ...     lowerAccidental=pitch.Accidental('natural')
    ... )
    >>> delayedInvertedTurn.name
    'delayed inverted turn (upper=sharp, lower=natural)'
    ```

    ```python
    >>> delayedBy1Turn = expressions.Turn(
    ...     delay=1.0, lowerAccidental=pitch.Accidental('double-flat'))
    >>> delayedBy1Turn.name
    'delayed(delayQL=1.0) turn (lower=double-flat)'
    ```

Turn.ornamentalPitches
:   Returns any ornamental pitches that have been resolved (see
    resolveOrnamentalPitches, which must be called first, or an
    empty tuple will be returned).

Turn.upperOrnamentalPitch
:   Returns the turn’s upper ornamental pitch. If resolveOrnamentalPitches
    has not yet been called, None is returned.

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`Turn`](#music21.expressions.Turn "music21.expressions.Turn") read/write properties

Turn.delay
:   If delay is NO\_DELAY, the turn is not delayed.

    If delay is anything else (an OffsetQL or DEFAULT\_DELAY), the turn is delayed.

    Note that if you set delay to OffsetQL(0), and then get the delay, you will
    get NO\_DELAY, not 0.

Turn.lowerAccidental
:   This is the Turn’s lowerAccidental. Whether or not it is visible is dictated by
    the upperAccidental’s displayStatus.

Turn.upperAccidental
:   This is the Turn’s upperAccidental. Whether or not it is visible is dictated by
    the upperAccidental’s displayStatus.

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`Turn`](#music21.expressions.Turn "music21.expressions.Turn") methods

Turn.getSize(*srcObj: [note.GeneralNote](moduleNote.html#music21.note.GeneralNote "music21.note.GeneralNote")*, *which: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *\**, *keySig: [key.KeySignature](moduleKey.html#music21.key.KeySignature "music21.key.KeySignature") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [interval.IntervalBase](moduleInterval.html#music21.interval.IntervalBase "music21.interval.IntervalBase")[[source]](../_modules/music21/expressions.html#Turn.getSize)
:   Returns the size of one of the turn’s two intervals (which=’upper’
    or which=’lower’), given a source note and an optional key signature.
    If the key signature is not specified, the source note’s context is
    searched for the current key signature, and if there is no such key
    signature, a key signature with no sharps and no flats will be used.
    Any upperAccidental or lowerAccidental that has been set on the
    turn will also be taken into account. If either has not been set,
    the appropriate accidental from the key signature will be used.

    If keySig is specified, this can be considered to be a theoretical
    question: “If this particular turn were to be attached to this note,
    in this key, what would the (‘upper’ or ‘lower’) size of the turn
    interval be?”

Turn.realize(*srcObj: [note.Note](moduleNote.html#music21.note.Note "music21.note.Note") | [note.Unpitched](moduleNote.html#music21.note.Unpitched "music21.note.Unpitched")*, *\**, *keySig: [key.KeySignature](moduleKey.html#music21.key.KeySignature "music21.key.KeySignature") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *inPlace: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[note.Note](moduleNote.html#music21.note.Note "music21.note.Note") | [note.Unpitched](moduleNote.html#music21.note.Unpitched "music21.note.Unpitched")], [note.Note](moduleNote.html#music21.note.Note "music21.note.Note") | [note.Unpitched](moduleNote.html#music21.note.Unpitched "music21.note.Unpitched") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[note.Note](moduleNote.html#music21.note.Note "music21.note.Note") | [note.Unpitched](moduleNote.html#music21.note.Unpitched "music21.note.Unpitched")]][[source]](../_modules/music21/expressions.html#Turn.realize)
:   realize a turn.

    returns a three-element tuple.
    The first element is an empty list because there are no notes at the start of a turn.
    The second element is the original note with a duration equal to the delay (but if there
    is no delay, the second element is None, because the turn “eats up” the entire note).
    The third element is a list of the four turn notes, adding up to the duration of the
    original note (less the delay, if there is one). The four turn notes will either be
    of equal duration, or the fourth note will be longer, to “eat up” the entire note.

    ```python
    >>> from  music21 import *
    >>> from music21.common.enums import OrnamentDelay
    >>> m1 = stream.Measure()
    >>> m1.append(key.Key('F', 'major'))
    >>> n1 = note.Note('C5')
    >>> m1.append(n1)
    >>> t1 = expressions.Turn()
    >>> t1.realize(n1)
    ([], None, [<music21.note.Note D>,
                <music21.note.Note C>,
                <music21.note.Note B->,
                <music21.note.Note C>])
    ```

    ```python
    >>> m2 = stream.Measure()
    >>> m2.append(key.KeySignature(5))
    >>> n2 = note.Note('B4', type='quarter')
    >>> m2.append(n2)
    >>> t2 = expressions.InvertedTurn(delay=OrnamentDelay.DEFAULT_DELAY)
    >>> n2.expressions.append(t2)
    >>> t2.realize(n2)
    ([], <music21.note.Note B>, [<music21.note.Note A#>,
                                 <music21.note.Note B>,
                                 <music21.note.Note C#>,
                                 <music21.note.Note B>])
    ```

    Realizing an expression leaves the original note and expression alone

    ```python
    >>> n2.duration.type
    'quarter'
    >>> n2.expressions
    [<music21.expressions.InvertedTurn>]
    ```

    If inPlace is True then the note is affected and the turn is
    removed from .expressions:

    ```python
    >>> n2 = note.Note('C4')
    >>> n2.duration.type = '32nd'
    >>> t2 = expressions.Turn(delay=OrnamentDelay.DEFAULT_DELAY)
    >>> _empty, newOrigNote, turnNotes = t2.realize(n2, inPlace=True)
    >>> for turnNote in turnNotes:
    ...     print(turnNote, turnNote.duration.type)
    <music21.note.Note D> 256th
    <music21.note.Note C> 256th
    <music21.note.Note B> 256th
    <music21.note.Note C> 256th
    >>> n2.duration.type
    '64th'
    >>> n2.expressions
    []
    >>> newOrigNote is n2
    True
    ```

    If the four turn notes (self.quarterLength each) don’t add up to the original note
    duration, the fourth turn note should be held to the length of any remaining unused
    duration. Here, for example, we have a dotted eighth note total duration, a delay
    of a 16th note, and a turn note duration of a triplet 32nd note, leaving the fourth
    turn note with a duration of a 16th note. This sort of turn is seen all over the
    music of Weber.

    ```python
    >>> from fractions import Fraction
    >>> n3 = note.Note('C4')
    >>> n3.quarterLength = 0.75
    >>> t3 = expressions.Turn(delay=0.25)
    >>> t3.quarterLength = 0.125 * Fraction(2, 3)
    >>> _empty, newOrigNote, turnNotes = t3.realize(n3, inPlace=True)
    >>> print(newOrigNote, newOrigNote.quarterLength)
    <music21.note.Note C> 0.25
    >>> for turnNote in turnNotes:
    ...     print(turnNote, turnNote.quarterLength)
    <music21.note.Note D> 1/12
    <music21.note.Note C> 1/12
    <music21.note.Note B> 1/12
    <music21.note.Note C> 0.25
    ```

    If .autoScale is off and the note is not long enough to realize 4
    32nd notes, then an exception is raised.

    ```python
    >>> n2 = note.Note('C4')
    >>> n2.duration.type = '32nd'
    >>> t2 = expressions.Turn()
    >>> t2.autoScale = False
    >>> t2.realize(n2)
    Traceback (most recent call last):
    music21.expressions.ExpressionException: The note is not long enough to realize a turn
    ```

Turn.resolveOrnamentalPitches(*srcObj: [note.GeneralNote](moduleNote.html#music21.note.GeneralNote "music21.note.GeneralNote")*, *\**, *keySig: [key.KeySignature](moduleKey.html#music21.key.KeySignature "music21.key.KeySignature") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](../_modules/music21/expressions.html#Turn.resolveOrnamentalPitches)
:   Computes and stores the ornamental pitches for a Turn, given the srcObj
    (can be any kind of ornamented GeneralNote) and an optional keySig.

    If keySig is None, srcNote’s context will be searched for a key signature.
    If no key signature is found, a key signature with no sharps and no flats
    will be used.

    e.g. A turn on a D in a key with two flats (upper ornamental pitch will be E flat,
    lower ornamental pitch will be C).

    ```python
    >>> twoFlats = key.KeySignature(sharps=-2)
    >>> n1 = note.Note('D4')
    >>> turn = expressions.Turn()
    >>> turn.resolveOrnamentalPitches(n1, keySig=twoFlats)
    >>> turn.ornamentalPitches
    (<music21.pitch.Pitch E-4>, <music21.pitch.Pitch C4>)
    >>> turn.upperOrnamentalPitch
    <music21.pitch.Pitch E-4>
    >>> turn.lowerOrnamentalPitch
    <music21.pitch.Pitch C4>
    ```

    e.g. A turn with a sharp over it and a flat under it, on a C, in a key with
    no sharps or flats (upper ornamental pitch will be D#, lower ornamental pitch
    will be B flat).

    ```python
    >>> noSharpsOrFlats = key.KeySignature(0)
    >>> n2 = note.Note('C4')
    >>> turn = expressions.Turn(
    ...     upperAccidental=pitch.Accidental('sharp'),
    ...     lowerAccidental=pitch.Accidental('flat'))
    >>> turn.resolveOrnamentalPitches(n2, keySig=noSharpsOrFlats)
    >>> turn.ornamentalPitches
    (<music21.pitch.Pitch D#4>, <music21.pitch.Pitch B-3>)
    >>> turn.upperOrnamentalPitch
    <music21.pitch.Pitch D#4>
    >>> turn.lowerOrnamentalPitch
    <music21.pitch.Pitch B-3>
    ```

Turn.updateAccidentalDisplay(*\**, *pitchPast: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *pitchPastMeasure: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *otherSimultaneousPitches: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *alteredPitches: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *cautionaryPitchClass: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *cautionaryAll: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *overrideStatus: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *cautionaryNotImmediateRepeat: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*)[[source]](../_modules/music21/expressions.html#Turn.updateAccidentalDisplay)
:   Updates accidental display for a Turn’s ornamental pitches (upper and lower).
    Defined exactly like Pitch.updateAccidentalDisplay, with two changes:
    Instead of self being the pitch to update, self is a Turn whose
    ornamentalPitches are to be updated; and we pay no attention to ties,
    since ornamental notes cannot be tied.

Methods inherited from [`Ornament`](#music21.expressions.Ornament "music21.expressions.Ornament"):

|  |  |  |
| --- | --- | --- |
| * [`fillListOfRealizedNotes()`](#music21.expressions.Ornament.fillListOfRealizedNotes "music21.expressions.Ornament.fillListOfRealizedNotes") |  |  |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`Turn`](#music21.expressions.Turn "music21.expressions.Turn") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## WholeStepAppoggiatura

class music21.expressions.WholeStepAppoggiatura(*\*\*keywords*)[[source]](../_modules/music21/expressions.html#WholeStepAppoggiatura)

[`WholeStepAppoggiatura`](#music21.expressions.WholeStepAppoggiatura "music21.expressions.WholeStepAppoggiatura") bases

* [`Appoggiatura`](#music21.expressions.Appoggiatura "music21.expressions.Appoggiatura")
* [`GeneralAppoggiatura`](#music21.expressions.GeneralAppoggiatura "music21.expressions.GeneralAppoggiatura")
* [`Ornament`](#music21.expressions.Ornament "music21.expressions.Ornament")
* [`Expression`](#music21.expressions.Expression "music21.expressions.Expression")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`WholeStepAppoggiatura`](#music21.expressions.WholeStepAppoggiatura "music21.expressions.WholeStepAppoggiatura") read-only properties

Read-only properties inherited from [`Ornament`](#music21.expressions.Ornament "music21.expressions.Ornament"):

|  |  |  |
| --- | --- | --- |
| * [`ornamentalPitches`](#music21.expressions.Ornament.ornamentalPitches "music21.expressions.Ornament.ornamentalPitches") |  |  |

Read-only properties inherited from [`Expression`](#music21.expressions.Expression "music21.expressions.Expression"):

|  |  |  |
| --- | --- | --- |
| * [`name`](#music21.expressions.Expression.name "music21.expressions.Expression.name") |  |  |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`WholeStepAppoggiatura`](#music21.expressions.WholeStepAppoggiatura "music21.expressions.WholeStepAppoggiatura") read/write properties

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`WholeStepAppoggiatura`](#music21.expressions.WholeStepAppoggiatura "music21.expressions.WholeStepAppoggiatura") methods

Methods inherited from [`GeneralAppoggiatura`](#music21.expressions.GeneralAppoggiatura "music21.expressions.GeneralAppoggiatura"):

|  |  |  |
| --- | --- | --- |
| * [`realize()`](#music21.expressions.GeneralAppoggiatura.realize "music21.expressions.GeneralAppoggiatura.realize") |  |  |

Methods inherited from [`Ornament`](#music21.expressions.Ornament "music21.expressions.Ornament"):

|  |  |  |
| --- | --- | --- |
| * [`fillListOfRealizedNotes()`](#music21.expressions.Ornament.fillListOfRealizedNotes "music21.expressions.Ornament.fillListOfRealizedNotes") | * [`resolveOrnamentalPitches()`](#music21.expressions.Ornament.resolveOrnamentalPitches "music21.expressions.Ornament.resolveOrnamentalPitches") | * [`updateAccidentalDisplay()`](#music21.expressions.Ornament.updateAccidentalDisplay "music21.expressions.Ornament.updateAccidentalDisplay") |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`WholeStepAppoggiatura`](#music21.expressions.WholeStepAppoggiatura "music21.expressions.WholeStepAppoggiatura") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## WholeStepInvertedAppoggiatura

class music21.expressions.WholeStepInvertedAppoggiatura(*\*\*keywords*)[[source]](../_modules/music21/expressions.html#WholeStepInvertedAppoggiatura)

[`WholeStepInvertedAppoggiatura`](#music21.expressions.WholeStepInvertedAppoggiatura "music21.expressions.WholeStepInvertedAppoggiatura") bases

* [`InvertedAppoggiatura`](#music21.expressions.InvertedAppoggiatura "music21.expressions.InvertedAppoggiatura")
* [`GeneralAppoggiatura`](#music21.expressions.GeneralAppoggiatura "music21.expressions.GeneralAppoggiatura")
* [`Ornament`](#music21.expressions.Ornament "music21.expressions.Ornament")
* [`Expression`](#music21.expressions.Expression "music21.expressions.Expression")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`WholeStepInvertedAppoggiatura`](#music21.expressions.WholeStepInvertedAppoggiatura "music21.expressions.WholeStepInvertedAppoggiatura") read-only properties

Read-only properties inherited from [`Ornament`](#music21.expressions.Ornament "music21.expressions.Ornament"):

|  |  |  |
| --- | --- | --- |
| * [`ornamentalPitches`](#music21.expressions.Ornament.ornamentalPitches "music21.expressions.Ornament.ornamentalPitches") |  |  |

Read-only properties inherited from [`Expression`](#music21.expressions.Expression "music21.expressions.Expression"):

|  |  |  |
| --- | --- | --- |
| * [`name`](#music21.expressions.Expression.name "music21.expressions.Expression.name") |  |  |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`WholeStepInvertedAppoggiatura`](#music21.expressions.WholeStepInvertedAppoggiatura "music21.expressions.WholeStepInvertedAppoggiatura") read/write properties

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`WholeStepInvertedAppoggiatura`](#music21.expressions.WholeStepInvertedAppoggiatura "music21.expressions.WholeStepInvertedAppoggiatura") methods

Methods inherited from [`GeneralAppoggiatura`](#music21.expressions.GeneralAppoggiatura "music21.expressions.GeneralAppoggiatura"):

|  |  |  |
| --- | --- | --- |
| * [`realize()`](#music21.expressions.GeneralAppoggiatura.realize "music21.expressions.GeneralAppoggiatura.realize") |  |  |

Methods inherited from [`Ornament`](#music21.expressions.Ornament "music21.expressions.Ornament"):

|  |  |  |
| --- | --- | --- |
| * [`fillListOfRealizedNotes()`](#music21.expressions.Ornament.fillListOfRealizedNotes "music21.expressions.Ornament.fillListOfRealizedNotes") | * [`resolveOrnamentalPitches()`](#music21.expressions.Ornament.resolveOrnamentalPitches "music21.expressions.Ornament.resolveOrnamentalPitches") | * [`updateAccidentalDisplay()`](#music21.expressions.Ornament.updateAccidentalDisplay "music21.expressions.Ornament.updateAccidentalDisplay") |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`WholeStepInvertedAppoggiatura`](#music21.expressions.WholeStepInvertedAppoggiatura "music21.expressions.WholeStepInvertedAppoggiatura") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## WholeStepInvertedMordent

class music21.expressions.WholeStepInvertedMordent(*\*\*keywords*)[[source]](../_modules/music21/expressions.html#WholeStepInvertedMordent)
:   A whole-step inverted Mordent.

    ```python
    >>> m = expressions.WholeStepInvertedMordent()
    >>> m.direction
    'up'
    >>> m.getSize(note.Note('C4'))
    <music21.interval.Interval M2>
    ```

[`WholeStepInvertedMordent`](#music21.expressions.WholeStepInvertedMordent "music21.expressions.WholeStepInvertedMordent") bases

* [`InvertedMordent`](#music21.expressions.InvertedMordent "music21.expressions.InvertedMordent")
* [`GeneralMordent`](#music21.expressions.GeneralMordent "music21.expressions.GeneralMordent")
* [`Ornament`](#music21.expressions.Ornament "music21.expressions.Ornament")
* [`Expression`](#music21.expressions.Expression "music21.expressions.Expression")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`WholeStepInvertedMordent`](#music21.expressions.WholeStepInvertedMordent "music21.expressions.WholeStepInvertedMordent") read-only properties

Read-only properties inherited from [`GeneralMordent`](#music21.expressions.GeneralMordent "music21.expressions.GeneralMordent"):

|  |  |  |
| --- | --- | --- |
| * [`direction`](#music21.expressions.GeneralMordent.direction "music21.expressions.GeneralMordent.direction") * [`name`](#music21.expressions.GeneralMordent.name "music21.expressions.GeneralMordent.name") | * [`ornamentalPitch`](#music21.expressions.GeneralMordent.ornamentalPitch "music21.expressions.GeneralMordent.ornamentalPitch") | * [`ornamentalPitches`](#music21.expressions.GeneralMordent.ornamentalPitches "music21.expressions.GeneralMordent.ornamentalPitches") |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`WholeStepInvertedMordent`](#music21.expressions.WholeStepInvertedMordent "music21.expressions.WholeStepInvertedMordent") read/write properties

WholeStepInvertedMordent.accidental

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`WholeStepInvertedMordent`](#music21.expressions.WholeStepInvertedMordent "music21.expressions.WholeStepInvertedMordent") methods

WholeStepInvertedMordent.getSize(*srcObj: [note.GeneralNote](moduleNote.html#music21.note.GeneralNote "music21.note.GeneralNote")*, *\**, *keySig: [key.KeySignature](moduleKey.html#music21.key.KeySignature "music21.key.KeySignature") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [interval.IntervalBase](moduleInterval.html#music21.interval.IntervalBase "music21.interval.IntervalBase")[[source]](../_modules/music21/expressions.html#WholeStepInvertedMordent.getSize)
:   Returns the size of the mordent’s interval, given a source note and
    an optional key signature. If the key signature is not specified, the
    source note’s context is searched for the current key signature, and if
    there is no such key signature, a key signature with no sharps and no flats
    will be used. Any accidental that has been set on the mordent will also
    be taken into account. If no accidental has been set, the appropriate
    accidental from the key signature will be used.

    If keySig is specified, this can be considered to be a theoretical question:
    “If this particular mordent were to be attached to this note, in this key,
    what would the size of the mordent interval be?”

Methods inherited from [`GeneralMordent`](#music21.expressions.GeneralMordent "music21.expressions.GeneralMordent"):

|  |  |  |
| --- | --- | --- |
| * [`realize()`](#music21.expressions.GeneralMordent.realize "music21.expressions.GeneralMordent.realize") | * [`resolveOrnamentalPitches()`](#music21.expressions.GeneralMordent.resolveOrnamentalPitches "music21.expressions.GeneralMordent.resolveOrnamentalPitches") | * [`updateAccidentalDisplay()`](#music21.expressions.GeneralMordent.updateAccidentalDisplay "music21.expressions.GeneralMordent.updateAccidentalDisplay") |

Methods inherited from [`Ornament`](#music21.expressions.Ornament "music21.expressions.Ornament"):

|  |  |  |
| --- | --- | --- |
| * [`fillListOfRealizedNotes()`](#music21.expressions.Ornament.fillListOfRealizedNotes "music21.expressions.Ornament.fillListOfRealizedNotes") |  |  |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`WholeStepInvertedMordent`](#music21.expressions.WholeStepInvertedMordent "music21.expressions.WholeStepInvertedMordent") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## WholeStepMordent

class music21.expressions.WholeStepMordent(*\*\*keywords*)[[source]](../_modules/music21/expressions.html#WholeStepMordent)
:   A whole step normal Mordent.

    ```python
    >>> m = expressions.WholeStepMordent()
    >>> m.direction
    'down'
    >>> m.getSize(note.Note('C4'))
    <music21.interval.Interval M-2>
    ```

[`WholeStepMordent`](#music21.expressions.WholeStepMordent "music21.expressions.WholeStepMordent") bases

* [`Mordent`](#music21.expressions.Mordent "music21.expressions.Mordent")
* [`GeneralMordent`](#music21.expressions.GeneralMordent "music21.expressions.GeneralMordent")
* [`Ornament`](#music21.expressions.Ornament "music21.expressions.Ornament")
* [`Expression`](#music21.expressions.Expression "music21.expressions.Expression")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`WholeStepMordent`](#music21.expressions.WholeStepMordent "music21.expressions.WholeStepMordent") read-only properties

Read-only properties inherited from [`GeneralMordent`](#music21.expressions.GeneralMordent "music21.expressions.GeneralMordent"):

|  |  |  |
| --- | --- | --- |
| * [`direction`](#music21.expressions.GeneralMordent.direction "music21.expressions.GeneralMordent.direction") * [`name`](#music21.expressions.GeneralMordent.name "music21.expressions.GeneralMordent.name") | * [`ornamentalPitch`](#music21.expressions.GeneralMordent.ornamentalPitch "music21.expressions.GeneralMordent.ornamentalPitch") | * [`ornamentalPitches`](#music21.expressions.GeneralMordent.ornamentalPitches "music21.expressions.GeneralMordent.ornamentalPitches") |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`WholeStepMordent`](#music21.expressions.WholeStepMordent "music21.expressions.WholeStepMordent") read/write properties

WholeStepMordent.accidental

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`WholeStepMordent`](#music21.expressions.WholeStepMordent "music21.expressions.WholeStepMordent") methods

WholeStepMordent.getSize(*srcObj: [note.GeneralNote](moduleNote.html#music21.note.GeneralNote "music21.note.GeneralNote")*, *\**, *keySig: [key.KeySignature](moduleKey.html#music21.key.KeySignature "music21.key.KeySignature") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [interval.IntervalBase](moduleInterval.html#music21.interval.IntervalBase "music21.interval.IntervalBase")[[source]](../_modules/music21/expressions.html#WholeStepMordent.getSize)
:   Returns the size of the mordent’s interval, given a source note and
    an optional key signature. If the key signature is not specified, the
    source note’s context is searched for the current key signature, and if
    there is no such key signature, a key signature with no sharps and no flats
    will be used. Any accidental that has been set on the mordent will also
    be taken into account. If no accidental has been set, the appropriate
    accidental from the key signature will be used.

    If keySig is specified, this can be considered to be a theoretical question:
    “If this particular mordent were to be attached to this note, in this key,
    what would the size of the mordent interval be?”

Methods inherited from [`GeneralMordent`](#music21.expressions.GeneralMordent "music21.expressions.GeneralMordent"):

|  |  |  |
| --- | --- | --- |
| * [`realize()`](#music21.expressions.GeneralMordent.realize "music21.expressions.GeneralMordent.realize") | * [`resolveOrnamentalPitches()`](#music21.expressions.GeneralMordent.resolveOrnamentalPitches "music21.expressions.GeneralMordent.resolveOrnamentalPitches") | * [`updateAccidentalDisplay()`](#music21.expressions.GeneralMordent.updateAccidentalDisplay "music21.expressions.GeneralMordent.updateAccidentalDisplay") |

Methods inherited from [`Ornament`](#music21.expressions.Ornament "music21.expressions.Ornament"):

|  |  |  |
| --- | --- | --- |
| * [`fillListOfRealizedNotes()`](#music21.expressions.Ornament.fillListOfRealizedNotes "music21.expressions.Ornament.fillListOfRealizedNotes") |  |  |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`WholeStepMordent`](#music21.expressions.WholeStepMordent "music21.expressions.WholeStepMordent") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## WholeStepTrill

class music21.expressions.WholeStepTrill(*\*\*keywords*)[[source]](../_modules/music21/expressions.html#WholeStepTrill)
:   A trill that yields whole steps no matter what.

    ```python
    >>> wholeTrill = expressions.WholeStepTrill()
    >>> wholeTrill.placement
    'above'
    >>> wholeTrill.getSize(note.Note('C4'))
    <music21.interval.Interval M2>
    ```

    Here the key signature of one sharp will not affect the trill:

    ```python
    >>> n = note.Note('B4', type='eighth')
    >>> m = stream.Measure()
    >>> m.insert(0, key.KeySignature(1))
    >>> m.append(n)
    >>> wholeTrill.realize(n)
    ([<music21.note.Note B>,
      <music21.note.Note C#>,
      <music21.note.Note B>,
      <music21.note.Note C#>], None, [])
    ```

[`WholeStepTrill`](#music21.expressions.WholeStepTrill "music21.expressions.WholeStepTrill") bases

* [`Trill`](#music21.expressions.Trill "music21.expressions.Trill")
* [`Ornament`](#music21.expressions.Ornament "music21.expressions.Ornament")
* [`Expression`](#music21.expressions.Expression "music21.expressions.Expression")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`WholeStepTrill`](#music21.expressions.WholeStepTrill "music21.expressions.WholeStepTrill") read-only properties

Read-only properties inherited from [`Trill`](#music21.expressions.Trill "music21.expressions.Trill"):

|  |  |  |
| --- | --- | --- |
| * [`direction`](#music21.expressions.Trill.direction "music21.expressions.Trill.direction") * [`name`](#music21.expressions.Trill.name "music21.expressions.Trill.name") | * [`ornamentalPitch`](#music21.expressions.Trill.ornamentalPitch "music21.expressions.Trill.ornamentalPitch") | * [`ornamentalPitches`](#music21.expressions.Trill.ornamentalPitches "music21.expressions.Trill.ornamentalPitches") |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`WholeStepTrill`](#music21.expressions.WholeStepTrill "music21.expressions.WholeStepTrill") read/write properties

WholeStepTrill.accidental

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`WholeStepTrill`](#music21.expressions.WholeStepTrill "music21.expressions.WholeStepTrill") methods

WholeStepTrill.getSize(*srcObj: [note.GeneralNote](moduleNote.html#music21.note.GeneralNote "music21.note.GeneralNote")*, *\**, *keySig: [key.KeySignature](moduleKey.html#music21.key.KeySignature "music21.key.KeySignature") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [interval.IntervalBase](moduleInterval.html#music21.interval.IntervalBase "music21.interval.IntervalBase")[[source]](../_modules/music21/expressions.html#WholeStepTrill.getSize)
:   Returns the size of the trill’s interval, given a source note and
    an optional key signature. If the key signature is not specified, the
    source note’s context is searched for the current key signature, and if
    there is no such key signature, a key signature with no sharps and no flats
    will be used. Any accidental that has been set on the trill will also
    be taken into account.

    If keySig is specified, this can be considered to be a theoretical question:
    “If this particular trill were to be attached to this note, in this key,
    what would the size of the trill interval be?”

Methods inherited from [`Trill`](#music21.expressions.Trill "music21.expressions.Trill"):

|  |  |  |
| --- | --- | --- |
| * [`realize()`](#music21.expressions.Trill.realize "music21.expressions.Trill.realize") * [`resolveOrnamentalPitches()`](#music21.expressions.Trill.resolveOrnamentalPitches "music21.expressions.Trill.resolveOrnamentalPitches") | * [`splitClient()`](#music21.expressions.Trill.splitClient "music21.expressions.Trill.splitClient") | * [`updateAccidentalDisplay()`](#music21.expressions.Trill.updateAccidentalDisplay "music21.expressions.Trill.updateAccidentalDisplay") |

Methods inherited from [`Ornament`](#music21.expressions.Ornament "music21.expressions.Ornament"):

|  |  |  |
| --- | --- | --- |
| * [`fillListOfRealizedNotes()`](#music21.expressions.Ornament.fillListOfRealizedNotes "music21.expressions.Ornament.fillListOfRealizedNotes") |  |  |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`WholeStepTrill`](#music21.expressions.WholeStepTrill "music21.expressions.WholeStepTrill") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## Functions

music21.expressions.isUnison(*intv: [IntervalBase](moduleInterval.html#music21.interval.IntervalBase "music21.interval.IntervalBase")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/expressions.html#isUnison)

music21.expressions.realizeOrnaments(*srcObj: [note.Note](moduleNote.html#music21.note.Note "music21.note.Note") | [note.Unpitched](moduleNote.html#music21.note.Unpitched "music21.note.Unpitched")*, *\**, *keySig: [key.KeySignature](moduleKey.html#music21.key.KeySignature "music21.key.KeySignature") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](../_modules/music21/expressions.html#realizeOrnaments)
:   given a Note or Unpitched with Ornament expressions,
    convert them into a list of objects that represents
    the performed version of the object:

    ```python
    >>> n1 = note.Note('D5')
    >>> n1.quarterLength = 1
    >>> n1.expressions.append(expressions.WholeStepMordent())
    >>> expList = expressions.realizeOrnaments(n1)
    >>> st1 = stream.Stream()
    >>> st1.append(expList)
    >>> st1.show()
    ```

    [![../_images/expressionsMordentRealize.png](../_images/expressionsMordentRealize.png)](../_images/expressionsMordentRealize.png)
