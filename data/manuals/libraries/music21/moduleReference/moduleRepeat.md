Source: https://music21.org/music21docs/moduleReference/moduleRepeat.html

# music21.repeat

This module provides the base class for all RepeatMark objects: entities that denote repeats.

Some RepeatMark objects are Expression objects; others are Bar objects. See for instance,
the [`Repeat`](moduleBar.html#music21.bar.Repeat "music21.bar.Repeat") which represents a normal barline repeat.

## RepeatExpression

class music21.repeat.RepeatExpression(*\*\*keywords*)[[source]](../_modules/music21/repeat.html#RepeatExpression)
:   This class models any mark added to a Score to mark
    repeat start and end points that are designated by
    text expressions or symbols, such as D.S. Al Coda, etc.

    N.B. Repeat(Barline) objects are not RepeatExpression objects,
    but both are RepeatMark subclasses.

    This class stores internally a
    [`TextExpression`](moduleExpressions.html#music21.expressions.TextExpression "music21.expressions.TextExpression"). This object
    is used for rendering text output in translation. A
    properly configured TextExpression object can also be
    used to create an instance of a RepeatExpressions.

[`RepeatExpression`](#music21.repeat.RepeatExpression "music21.repeat.RepeatExpression") bases

* [`RepeatMark`](#music21.repeat.RepeatMark "music21.repeat.RepeatMark")
* [`Expression`](moduleExpressions.html#music21.expressions.Expression "music21.expressions.Expression")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`RepeatExpression`](#music21.repeat.RepeatExpression "music21.repeat.RepeatExpression") read-only properties

Read-only properties inherited from [`Expression`](moduleExpressions.html#music21.expressions.Expression "music21.expressions.Expression"):

|  |  |  |
| --- | --- | --- |
| * [`name`](moduleExpressions.html#music21.expressions.Expression.name "music21.expressions.Expression.name") |  |  |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`RepeatExpression`](#music21.repeat.RepeatExpression "music21.repeat.RepeatExpression") read/write properties

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`RepeatExpression`](#music21.repeat.RepeatExpression "music21.repeat.RepeatExpression") methods

RepeatExpression.applyTextFormatting(*te=None*)[[source]](../_modules/music21/repeat.html#RepeatExpression.applyTextFormatting)
:   Apply the default text formatting to the text expression version of this repeat

RepeatExpression.getText()[[source]](../_modules/music21/repeat.html#RepeatExpression.getText)
:   Get the text used for this expression.

RepeatExpression.getTextExpression()[[source]](../_modules/music21/repeat.html#RepeatExpression.getTextExpression)
:   Return a copy of the TextExpression stored in this object.

RepeatExpression.isValidText(*value*)[[source]](../_modules/music21/repeat.html#RepeatExpression.isValidText)
:   Return True or False if the supplied text could be used for this RepeatExpression.

RepeatExpression.setText(*value*)[[source]](../_modules/music21/repeat.html#RepeatExpression.setText)
:   Set the text of this repeat expression.
    This is also the primary way that the stored TextExpression object is created.

RepeatExpression.setTextExpression(*value*)[[source]](../_modules/music21/repeat.html#RepeatExpression.setTextExpression)
:   Directly set a TextExpression object.

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`RepeatExpression`](#music21.repeat.RepeatExpression "music21.repeat.RepeatExpression") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## RepeatExpressionMarker

class music21.repeat.RepeatExpressionMarker(*\*\*keywords*)[[source]](../_modules/music21/repeat.html#RepeatExpressionMarker)
:   Some repeat expressions are markers of positions
    in the score to jump to; these classes model those makers,
    such as Coda, Segno, and Fine, which are subclassed below.

[`RepeatExpressionMarker`](#music21.repeat.RepeatExpressionMarker "music21.repeat.RepeatExpressionMarker") bases

* [`RepeatExpression`](#music21.repeat.RepeatExpression "music21.repeat.RepeatExpression")
* [`RepeatMark`](#music21.repeat.RepeatMark "music21.repeat.RepeatMark")
* [`Expression`](moduleExpressions.html#music21.expressions.Expression "music21.expressions.Expression")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`RepeatExpressionMarker`](#music21.repeat.RepeatExpressionMarker "music21.repeat.RepeatExpressionMarker") read-only properties

Read-only properties inherited from [`Expression`](moduleExpressions.html#music21.expressions.Expression "music21.expressions.Expression"):

|  |  |  |
| --- | --- | --- |
| * [`name`](moduleExpressions.html#music21.expressions.Expression.name "music21.expressions.Expression.name") |  |  |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`RepeatExpressionMarker`](#music21.repeat.RepeatExpressionMarker "music21.repeat.RepeatExpressionMarker") read/write properties

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`RepeatExpressionMarker`](#music21.repeat.RepeatExpressionMarker "music21.repeat.RepeatExpressionMarker") methods

Methods inherited from [`RepeatExpression`](#music21.repeat.RepeatExpression "music21.repeat.RepeatExpression"):

|  |  |  |
| --- | --- | --- |
| * [`applyTextFormatting()`](#music21.repeat.RepeatExpression.applyTextFormatting "music21.repeat.RepeatExpression.applyTextFormatting") * [`getText()`](#music21.repeat.RepeatExpression.getText "music21.repeat.RepeatExpression.getText") | * [`getTextExpression()`](#music21.repeat.RepeatExpression.getTextExpression "music21.repeat.RepeatExpression.getTextExpression") * [`isValidText()`](#music21.repeat.RepeatExpression.isValidText "music21.repeat.RepeatExpression.isValidText") | * [`setText()`](#music21.repeat.RepeatExpression.setText "music21.repeat.RepeatExpression.setText") * [`setTextExpression()`](#music21.repeat.RepeatExpression.setTextExpression "music21.repeat.RepeatExpression.setTextExpression") |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`RepeatExpressionMarker`](#music21.repeat.RepeatExpressionMarker "music21.repeat.RepeatExpressionMarker") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## Coda

class music21.repeat.Coda(*text=None*, *\*\*keywords*)[[source]](../_modules/music21/repeat.html#Coda)
:   The coda symbol, or the word coda, as placed in a score.

    ```python
    >>> rm = repeat.Coda()
    ```

[`Coda`](#music21.repeat.Coda "music21.repeat.Coda") bases

* [`RepeatExpressionMarker`](#music21.repeat.RepeatExpressionMarker "music21.repeat.RepeatExpressionMarker")
* [`RepeatExpression`](#music21.repeat.RepeatExpression "music21.repeat.RepeatExpression")
* [`RepeatMark`](#music21.repeat.RepeatMark "music21.repeat.RepeatMark")
* [`Expression`](moduleExpressions.html#music21.expressions.Expression "music21.expressions.Expression")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`Coda`](#music21.repeat.Coda "music21.repeat.Coda") read-only properties

Read-only properties inherited from [`Expression`](moduleExpressions.html#music21.expressions.Expression "music21.expressions.Expression"):

|  |  |  |
| --- | --- | --- |
| * [`name`](moduleExpressions.html#music21.expressions.Expression.name "music21.expressions.Expression.name") |  |  |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`Coda`](#music21.repeat.Coda "music21.repeat.Coda") read/write properties

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`Coda`](#music21.repeat.Coda "music21.repeat.Coda") methods

Methods inherited from [`RepeatExpression`](#music21.repeat.RepeatExpression "music21.repeat.RepeatExpression"):

|  |  |  |
| --- | --- | --- |
| * [`applyTextFormatting()`](#music21.repeat.RepeatExpression.applyTextFormatting "music21.repeat.RepeatExpression.applyTextFormatting") * [`getText()`](#music21.repeat.RepeatExpression.getText "music21.repeat.RepeatExpression.getText") | * [`getTextExpression()`](#music21.repeat.RepeatExpression.getTextExpression "music21.repeat.RepeatExpression.getTextExpression") * [`isValidText()`](#music21.repeat.RepeatExpression.isValidText "music21.repeat.RepeatExpression.isValidText") | * [`setText()`](#music21.repeat.RepeatExpression.setText "music21.repeat.RepeatExpression.setText") * [`setTextExpression()`](#music21.repeat.RepeatExpression.setTextExpression "music21.repeat.RepeatExpression.setTextExpression") |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`Coda`](#music21.repeat.Coda "music21.repeat.Coda") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## Segno

class music21.repeat.Segno(*\*\*keywords*)[[source]](../_modules/music21/repeat.html#Segno)
:   The segno sign as placed in a score.

    ```python
    >>> rm = repeat.Segno()
    >>> rm.useSymbol
    True
    ```

[`Segno`](#music21.repeat.Segno "music21.repeat.Segno") bases

* [`RepeatExpressionMarker`](#music21.repeat.RepeatExpressionMarker "music21.repeat.RepeatExpressionMarker")
* [`RepeatExpression`](#music21.repeat.RepeatExpression "music21.repeat.RepeatExpression")
* [`RepeatMark`](#music21.repeat.RepeatMark "music21.repeat.RepeatMark")
* [`Expression`](moduleExpressions.html#music21.expressions.Expression "music21.expressions.Expression")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`Segno`](#music21.repeat.Segno "music21.repeat.Segno") read-only properties

Read-only properties inherited from [`Expression`](moduleExpressions.html#music21.expressions.Expression "music21.expressions.Expression"):

|  |  |  |
| --- | --- | --- |
| * [`name`](moduleExpressions.html#music21.expressions.Expression.name "music21.expressions.Expression.name") |  |  |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`Segno`](#music21.repeat.Segno "music21.repeat.Segno") read/write properties

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`Segno`](#music21.repeat.Segno "music21.repeat.Segno") methods

Methods inherited from [`RepeatExpression`](#music21.repeat.RepeatExpression "music21.repeat.RepeatExpression"):

|  |  |  |
| --- | --- | --- |
| * [`applyTextFormatting()`](#music21.repeat.RepeatExpression.applyTextFormatting "music21.repeat.RepeatExpression.applyTextFormatting") * [`getText()`](#music21.repeat.RepeatExpression.getText "music21.repeat.RepeatExpression.getText") | * [`getTextExpression()`](#music21.repeat.RepeatExpression.getTextExpression "music21.repeat.RepeatExpression.getTextExpression") * [`isValidText()`](#music21.repeat.RepeatExpression.isValidText "music21.repeat.RepeatExpression.isValidText") | * [`setText()`](#music21.repeat.RepeatExpression.setText "music21.repeat.RepeatExpression.setText") * [`setTextExpression()`](#music21.repeat.RepeatExpression.setTextExpression "music21.repeat.RepeatExpression.setTextExpression") |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`Segno`](#music21.repeat.Segno "music21.repeat.Segno") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## Fine

class music21.repeat.Fine(*\*\*keywords*)[[source]](../_modules/music21/repeat.html#Fine)
:   The fine word as placed in a score.

    ```python
    >>> rm = repeat.Fine()
    ```

[`Fine`](#music21.repeat.Fine "music21.repeat.Fine") bases

* [`RepeatExpressionMarker`](#music21.repeat.RepeatExpressionMarker "music21.repeat.RepeatExpressionMarker")
* [`RepeatExpression`](#music21.repeat.RepeatExpression "music21.repeat.RepeatExpression")
* [`RepeatMark`](#music21.repeat.RepeatMark "music21.repeat.RepeatMark")
* [`Expression`](moduleExpressions.html#music21.expressions.Expression "music21.expressions.Expression")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`Fine`](#music21.repeat.Fine "music21.repeat.Fine") read-only properties

Read-only properties inherited from [`Expression`](moduleExpressions.html#music21.expressions.Expression "music21.expressions.Expression"):

|  |  |  |
| --- | --- | --- |
| * [`name`](moduleExpressions.html#music21.expressions.Expression.name "music21.expressions.Expression.name") |  |  |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`Fine`](#music21.repeat.Fine "music21.repeat.Fine") read/write properties

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`Fine`](#music21.repeat.Fine "music21.repeat.Fine") methods

Methods inherited from [`RepeatExpression`](#music21.repeat.RepeatExpression "music21.repeat.RepeatExpression"):

|  |  |  |
| --- | --- | --- |
| * [`applyTextFormatting()`](#music21.repeat.RepeatExpression.applyTextFormatting "music21.repeat.RepeatExpression.applyTextFormatting") * [`getText()`](#music21.repeat.RepeatExpression.getText "music21.repeat.RepeatExpression.getText") | * [`getTextExpression()`](#music21.repeat.RepeatExpression.getTextExpression "music21.repeat.RepeatExpression.getTextExpression") * [`isValidText()`](#music21.repeat.RepeatExpression.isValidText "music21.repeat.RepeatExpression.isValidText") | * [`setText()`](#music21.repeat.RepeatExpression.setText "music21.repeat.RepeatExpression.setText") * [`setTextExpression()`](#music21.repeat.RepeatExpression.setTextExpression "music21.repeat.RepeatExpression.setTextExpression") |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`Fine`](#music21.repeat.Fine "music21.repeat.Fine") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## RepeatExpressionCommand

class music21.repeat.RepeatExpressionCommand(*\*\*keywords*)[[source]](../_modules/music21/repeat.html#RepeatExpressionCommand)
:   Some repeat expressions are commands, instructing
    the reader to go somewhere else. DaCapo and
    related are examples.

[`RepeatExpressionCommand`](#music21.repeat.RepeatExpressionCommand "music21.repeat.RepeatExpressionCommand") bases

* [`RepeatExpression`](#music21.repeat.RepeatExpression "music21.repeat.RepeatExpression")
* [`RepeatMark`](#music21.repeat.RepeatMark "music21.repeat.RepeatMark")
* [`Expression`](moduleExpressions.html#music21.expressions.Expression "music21.expressions.Expression")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`RepeatExpressionCommand`](#music21.repeat.RepeatExpressionCommand "music21.repeat.RepeatExpressionCommand") read-only properties

Read-only properties inherited from [`Expression`](moduleExpressions.html#music21.expressions.Expression "music21.expressions.Expression"):

|  |  |  |
| --- | --- | --- |
| * [`name`](moduleExpressions.html#music21.expressions.Expression.name "music21.expressions.Expression.name") |  |  |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`RepeatExpressionCommand`](#music21.repeat.RepeatExpressionCommand "music21.repeat.RepeatExpressionCommand") read/write properties

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`RepeatExpressionCommand`](#music21.repeat.RepeatExpressionCommand "music21.repeat.RepeatExpressionCommand") methods

Methods inherited from [`RepeatExpression`](#music21.repeat.RepeatExpression "music21.repeat.RepeatExpression"):

|  |  |  |
| --- | --- | --- |
| * [`applyTextFormatting()`](#music21.repeat.RepeatExpression.applyTextFormatting "music21.repeat.RepeatExpression.applyTextFormatting") * [`getText()`](#music21.repeat.RepeatExpression.getText "music21.repeat.RepeatExpression.getText") | * [`getTextExpression()`](#music21.repeat.RepeatExpression.getTextExpression "music21.repeat.RepeatExpression.getTextExpression") * [`isValidText()`](#music21.repeat.RepeatExpression.isValidText "music21.repeat.RepeatExpression.isValidText") | * [`setText()`](#music21.repeat.RepeatExpression.setText "music21.repeat.RepeatExpression.setText") * [`setTextExpression()`](#music21.repeat.RepeatExpression.setTextExpression "music21.repeat.RepeatExpression.setTextExpression") |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`RepeatExpressionCommand`](#music21.repeat.RepeatExpressionCommand "music21.repeat.RepeatExpressionCommand") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## DaCapo

class music21.repeat.DaCapo(*text=None*, *\*\*keywords*)[[source]](../_modules/music21/repeat.html#DaCapo)
:   The Da Capo command, indicating a return to the beginning
    and a continuation to the end. By default,
    repeatAfterJump is False, indicating that any repeats
    encountered on the Da Capo repeat not be repeated.

[`DaCapo`](#music21.repeat.DaCapo "music21.repeat.DaCapo") bases

* [`RepeatExpressionCommand`](#music21.repeat.RepeatExpressionCommand "music21.repeat.RepeatExpressionCommand")
* [`RepeatExpression`](#music21.repeat.RepeatExpression "music21.repeat.RepeatExpression")
* [`RepeatMark`](#music21.repeat.RepeatMark "music21.repeat.RepeatMark")
* [`Expression`](moduleExpressions.html#music21.expressions.Expression "music21.expressions.Expression")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`DaCapo`](#music21.repeat.DaCapo "music21.repeat.DaCapo") read-only properties

Read-only properties inherited from [`Expression`](moduleExpressions.html#music21.expressions.Expression "music21.expressions.Expression"):

|  |  |  |
| --- | --- | --- |
| * [`name`](moduleExpressions.html#music21.expressions.Expression.name "music21.expressions.Expression.name") |  |  |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`DaCapo`](#music21.repeat.DaCapo "music21.repeat.DaCapo") read/write properties

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`DaCapo`](#music21.repeat.DaCapo "music21.repeat.DaCapo") methods

Methods inherited from [`RepeatExpression`](#music21.repeat.RepeatExpression "music21.repeat.RepeatExpression"):

|  |  |  |
| --- | --- | --- |
| * [`applyTextFormatting()`](#music21.repeat.RepeatExpression.applyTextFormatting "music21.repeat.RepeatExpression.applyTextFormatting") * [`getText()`](#music21.repeat.RepeatExpression.getText "music21.repeat.RepeatExpression.getText") | * [`getTextExpression()`](#music21.repeat.RepeatExpression.getTextExpression "music21.repeat.RepeatExpression.getTextExpression") * [`isValidText()`](#music21.repeat.RepeatExpression.isValidText "music21.repeat.RepeatExpression.isValidText") | * [`setText()`](#music21.repeat.RepeatExpression.setText "music21.repeat.RepeatExpression.setText") * [`setTextExpression()`](#music21.repeat.RepeatExpression.setTextExpression "music21.repeat.RepeatExpression.setTextExpression") |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`DaCapo`](#music21.repeat.DaCapo "music21.repeat.DaCapo") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## DaCapoAlFine

class music21.repeat.DaCapoAlFine(*text=None*, *\*\*keywords*)[[source]](../_modules/music21/repeat.html#DaCapoAlFine)
:   The Da Capo al Fine command, indicating a return to
    the beginning and a continuation to the
    [`Fine`](#music21.repeat.Fine "music21.repeat.Fine") object. By default,
    repeatAfterJump is False, indicating that any
    repeats encountered on the Da Capo repeat not
    be repeated.

    ```python
    >>> rm = repeat.DaCapoAlFine()
    ```

[`DaCapoAlFine`](#music21.repeat.DaCapoAlFine "music21.repeat.DaCapoAlFine") bases

* [`RepeatExpressionCommand`](#music21.repeat.RepeatExpressionCommand "music21.repeat.RepeatExpressionCommand")
* [`RepeatExpression`](#music21.repeat.RepeatExpression "music21.repeat.RepeatExpression")
* [`RepeatMark`](#music21.repeat.RepeatMark "music21.repeat.RepeatMark")
* [`Expression`](moduleExpressions.html#music21.expressions.Expression "music21.expressions.Expression")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`DaCapoAlFine`](#music21.repeat.DaCapoAlFine "music21.repeat.DaCapoAlFine") read-only properties

Read-only properties inherited from [`Expression`](moduleExpressions.html#music21.expressions.Expression "music21.expressions.Expression"):

|  |  |  |
| --- | --- | --- |
| * [`name`](moduleExpressions.html#music21.expressions.Expression.name "music21.expressions.Expression.name") |  |  |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`DaCapoAlFine`](#music21.repeat.DaCapoAlFine "music21.repeat.DaCapoAlFine") read/write properties

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`DaCapoAlFine`](#music21.repeat.DaCapoAlFine "music21.repeat.DaCapoAlFine") methods

Methods inherited from [`RepeatExpression`](#music21.repeat.RepeatExpression "music21.repeat.RepeatExpression"):

|  |  |  |
| --- | --- | --- |
| * [`applyTextFormatting()`](#music21.repeat.RepeatExpression.applyTextFormatting "music21.repeat.RepeatExpression.applyTextFormatting") * [`getText()`](#music21.repeat.RepeatExpression.getText "music21.repeat.RepeatExpression.getText") | * [`getTextExpression()`](#music21.repeat.RepeatExpression.getTextExpression "music21.repeat.RepeatExpression.getTextExpression") * [`isValidText()`](#music21.repeat.RepeatExpression.isValidText "music21.repeat.RepeatExpression.isValidText") | * [`setText()`](#music21.repeat.RepeatExpression.setText "music21.repeat.RepeatExpression.setText") * [`setTextExpression()`](#music21.repeat.RepeatExpression.setTextExpression "music21.repeat.RepeatExpression.setTextExpression") |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`DaCapoAlFine`](#music21.repeat.DaCapoAlFine "music21.repeat.DaCapoAlFine") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## DaCapoAlCoda

class music21.repeat.DaCapoAlCoda(*text=None*, *\*\*keywords*)[[source]](../_modules/music21/repeat.html#DaCapoAlCoda)
:   The Da Capo al Coda command, indicating a return
    to the beginning and a continuation to the
    [`Coda`](#music21.repeat.Coda "music21.repeat.Coda") object. The music
    resumes at a second [`Coda`](#music21.repeat.Coda "music21.repeat.Coda")
    object. By default, repeatAfterJump is False,
    indicating that any repeats encountered on the
    Da Capo repeat not be repeated.

    ```python
    >>> rm = repeat.DaCapoAlCoda()
    ```

[`DaCapoAlCoda`](#music21.repeat.DaCapoAlCoda "music21.repeat.DaCapoAlCoda") bases

* [`RepeatExpressionCommand`](#music21.repeat.RepeatExpressionCommand "music21.repeat.RepeatExpressionCommand")
* [`RepeatExpression`](#music21.repeat.RepeatExpression "music21.repeat.RepeatExpression")
* [`RepeatMark`](#music21.repeat.RepeatMark "music21.repeat.RepeatMark")
* [`Expression`](moduleExpressions.html#music21.expressions.Expression "music21.expressions.Expression")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`DaCapoAlCoda`](#music21.repeat.DaCapoAlCoda "music21.repeat.DaCapoAlCoda") read-only properties

Read-only properties inherited from [`Expression`](moduleExpressions.html#music21.expressions.Expression "music21.expressions.Expression"):

|  |  |  |
| --- | --- | --- |
| * [`name`](moduleExpressions.html#music21.expressions.Expression.name "music21.expressions.Expression.name") |  |  |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`DaCapoAlCoda`](#music21.repeat.DaCapoAlCoda "music21.repeat.DaCapoAlCoda") read/write properties

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`DaCapoAlCoda`](#music21.repeat.DaCapoAlCoda "music21.repeat.DaCapoAlCoda") methods

Methods inherited from [`RepeatExpression`](#music21.repeat.RepeatExpression "music21.repeat.RepeatExpression"):

|  |  |  |
| --- | --- | --- |
| * [`applyTextFormatting()`](#music21.repeat.RepeatExpression.applyTextFormatting "music21.repeat.RepeatExpression.applyTextFormatting") * [`getText()`](#music21.repeat.RepeatExpression.getText "music21.repeat.RepeatExpression.getText") | * [`getTextExpression()`](#music21.repeat.RepeatExpression.getTextExpression "music21.repeat.RepeatExpression.getTextExpression") * [`isValidText()`](#music21.repeat.RepeatExpression.isValidText "music21.repeat.RepeatExpression.isValidText") | * [`setText()`](#music21.repeat.RepeatExpression.setText "music21.repeat.RepeatExpression.setText") * [`setTextExpression()`](#music21.repeat.RepeatExpression.setTextExpression "music21.repeat.RepeatExpression.setTextExpression") |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`DaCapoAlCoda`](#music21.repeat.DaCapoAlCoda "music21.repeat.DaCapoAlCoda") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## AlSegno

class music21.repeat.AlSegno(*text=None*, *\*\*keywords*)[[source]](../_modules/music21/repeat.html#AlSegno)
:   Jump to the sign. Presumably a forward jump, not a repeat.

    ```python
    >>> rm = repeat.AlSegno()
    ```

[`AlSegno`](#music21.repeat.AlSegno "music21.repeat.AlSegno") bases

* [`RepeatExpressionCommand`](#music21.repeat.RepeatExpressionCommand "music21.repeat.RepeatExpressionCommand")
* [`RepeatExpression`](#music21.repeat.RepeatExpression "music21.repeat.RepeatExpression")
* [`RepeatMark`](#music21.repeat.RepeatMark "music21.repeat.RepeatMark")
* [`Expression`](moduleExpressions.html#music21.expressions.Expression "music21.expressions.Expression")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`AlSegno`](#music21.repeat.AlSegno "music21.repeat.AlSegno") read-only properties

Read-only properties inherited from [`Expression`](moduleExpressions.html#music21.expressions.Expression "music21.expressions.Expression"):

|  |  |  |
| --- | --- | --- |
| * [`name`](moduleExpressions.html#music21.expressions.Expression.name "music21.expressions.Expression.name") |  |  |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`AlSegno`](#music21.repeat.AlSegno "music21.repeat.AlSegno") read/write properties

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`AlSegno`](#music21.repeat.AlSegno "music21.repeat.AlSegno") methods

Methods inherited from [`RepeatExpression`](#music21.repeat.RepeatExpression "music21.repeat.RepeatExpression"):

|  |  |  |
| --- | --- | --- |
| * [`applyTextFormatting()`](#music21.repeat.RepeatExpression.applyTextFormatting "music21.repeat.RepeatExpression.applyTextFormatting") * [`getText()`](#music21.repeat.RepeatExpression.getText "music21.repeat.RepeatExpression.getText") | * [`getTextExpression()`](#music21.repeat.RepeatExpression.getTextExpression "music21.repeat.RepeatExpression.getTextExpression") * [`isValidText()`](#music21.repeat.RepeatExpression.isValidText "music21.repeat.RepeatExpression.isValidText") | * [`setText()`](#music21.repeat.RepeatExpression.setText "music21.repeat.RepeatExpression.setText") * [`setTextExpression()`](#music21.repeat.RepeatExpression.setTextExpression "music21.repeat.RepeatExpression.setTextExpression") |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`AlSegno`](#music21.repeat.AlSegno "music21.repeat.AlSegno") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## DalSegno

class music21.repeat.DalSegno(*text=None*, *\*\*keywords*)[[source]](../_modules/music21/repeat.html#DalSegno)
:   The Dal Segno command, indicating a return to the segno
    and a continuation to the end. By default, repeatAfterJump
    is False, indicating that any repeats encountered on
    the Da Capo repeat not be repeated.

    ```python
    >>> rm = repeat.DaCapoAlFine()
    ```

[`DalSegno`](#music21.repeat.DalSegno "music21.repeat.DalSegno") bases

* [`RepeatExpressionCommand`](#music21.repeat.RepeatExpressionCommand "music21.repeat.RepeatExpressionCommand")
* [`RepeatExpression`](#music21.repeat.RepeatExpression "music21.repeat.RepeatExpression")
* [`RepeatMark`](#music21.repeat.RepeatMark "music21.repeat.RepeatMark")
* [`Expression`](moduleExpressions.html#music21.expressions.Expression "music21.expressions.Expression")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`DalSegno`](#music21.repeat.DalSegno "music21.repeat.DalSegno") read-only properties

Read-only properties inherited from [`Expression`](moduleExpressions.html#music21.expressions.Expression "music21.expressions.Expression"):

|  |  |  |
| --- | --- | --- |
| * [`name`](moduleExpressions.html#music21.expressions.Expression.name "music21.expressions.Expression.name") |  |  |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`DalSegno`](#music21.repeat.DalSegno "music21.repeat.DalSegno") read/write properties

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`DalSegno`](#music21.repeat.DalSegno "music21.repeat.DalSegno") methods

Methods inherited from [`RepeatExpression`](#music21.repeat.RepeatExpression "music21.repeat.RepeatExpression"):

|  |  |  |
| --- | --- | --- |
| * [`applyTextFormatting()`](#music21.repeat.RepeatExpression.applyTextFormatting "music21.repeat.RepeatExpression.applyTextFormatting") * [`getText()`](#music21.repeat.RepeatExpression.getText "music21.repeat.RepeatExpression.getText") | * [`getTextExpression()`](#music21.repeat.RepeatExpression.getTextExpression "music21.repeat.RepeatExpression.getTextExpression") * [`isValidText()`](#music21.repeat.RepeatExpression.isValidText "music21.repeat.RepeatExpression.isValidText") | * [`setText()`](#music21.repeat.RepeatExpression.setText "music21.repeat.RepeatExpression.setText") * [`setTextExpression()`](#music21.repeat.RepeatExpression.setTextExpression "music21.repeat.RepeatExpression.setTextExpression") |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`DalSegno`](#music21.repeat.DalSegno "music21.repeat.DalSegno") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## DalSegnoAlFine

class music21.repeat.DalSegnoAlFine(*text=None*, *\*\*keywords*)[[source]](../_modules/music21/repeat.html#DalSegnoAlFine)
:   The Dal Segno al Fine command, indicating a return to the
    segno and a continuation to the [`Fine`](#music21.repeat.Fine "music21.repeat.Fine")
    object. By default, repeatAfterJump is False, indicating
    that any repeats encountered on the Dal Segno repeat not
    be repeated.

    ```python
    >>> rm = repeat.DaCapoAlFine()
    ```

[`DalSegnoAlFine`](#music21.repeat.DalSegnoAlFine "music21.repeat.DalSegnoAlFine") bases

* [`RepeatExpressionCommand`](#music21.repeat.RepeatExpressionCommand "music21.repeat.RepeatExpressionCommand")
* [`RepeatExpression`](#music21.repeat.RepeatExpression "music21.repeat.RepeatExpression")
* [`RepeatMark`](#music21.repeat.RepeatMark "music21.repeat.RepeatMark")
* [`Expression`](moduleExpressions.html#music21.expressions.Expression "music21.expressions.Expression")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`DalSegnoAlFine`](#music21.repeat.DalSegnoAlFine "music21.repeat.DalSegnoAlFine") read-only properties

Read-only properties inherited from [`Expression`](moduleExpressions.html#music21.expressions.Expression "music21.expressions.Expression"):

|  |  |  |
| --- | --- | --- |
| * [`name`](moduleExpressions.html#music21.expressions.Expression.name "music21.expressions.Expression.name") |  |  |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`DalSegnoAlFine`](#music21.repeat.DalSegnoAlFine "music21.repeat.DalSegnoAlFine") read/write properties

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`DalSegnoAlFine`](#music21.repeat.DalSegnoAlFine "music21.repeat.DalSegnoAlFine") methods

Methods inherited from [`RepeatExpression`](#music21.repeat.RepeatExpression "music21.repeat.RepeatExpression"):

|  |  |  |
| --- | --- | --- |
| * [`applyTextFormatting()`](#music21.repeat.RepeatExpression.applyTextFormatting "music21.repeat.RepeatExpression.applyTextFormatting") * [`getText()`](#music21.repeat.RepeatExpression.getText "music21.repeat.RepeatExpression.getText") | * [`getTextExpression()`](#music21.repeat.RepeatExpression.getTextExpression "music21.repeat.RepeatExpression.getTextExpression") * [`isValidText()`](#music21.repeat.RepeatExpression.isValidText "music21.repeat.RepeatExpression.isValidText") | * [`setText()`](#music21.repeat.RepeatExpression.setText "music21.repeat.RepeatExpression.setText") * [`setTextExpression()`](#music21.repeat.RepeatExpression.setTextExpression "music21.repeat.RepeatExpression.setTextExpression") |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`DalSegnoAlFine`](#music21.repeat.DalSegnoAlFine "music21.repeat.DalSegnoAlFine") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## DalSegnoAlCoda

class music21.repeat.DalSegnoAlCoda(*text=None*, *\*\*keywords*)[[source]](../_modules/music21/repeat.html#DalSegnoAlCoda)
:   The Dal Segno al Coda command, indicating a return to the
    beginning and a continuation to the [`Coda`](#music21.repeat.Coda "music21.repeat.Coda")
    object. The music resumes at a second
    [`Coda`](#music21.repeat.Coda "music21.repeat.Coda") object. By default,
    repeatAfterJump is False, indicating that any repeats encountered
    on the Da Segno repeat not be repeated.

    ```python
    >>> rm = repeat.DaCapoAlCoda()
    ```

[`DalSegnoAlCoda`](#music21.repeat.DalSegnoAlCoda "music21.repeat.DalSegnoAlCoda") bases

* [`RepeatExpressionCommand`](#music21.repeat.RepeatExpressionCommand "music21.repeat.RepeatExpressionCommand")
* [`RepeatExpression`](#music21.repeat.RepeatExpression "music21.repeat.RepeatExpression")
* [`RepeatMark`](#music21.repeat.RepeatMark "music21.repeat.RepeatMark")
* [`Expression`](moduleExpressions.html#music21.expressions.Expression "music21.expressions.Expression")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`DalSegnoAlCoda`](#music21.repeat.DalSegnoAlCoda "music21.repeat.DalSegnoAlCoda") read-only properties

Read-only properties inherited from [`Expression`](moduleExpressions.html#music21.expressions.Expression "music21.expressions.Expression"):

|  |  |  |
| --- | --- | --- |
| * [`name`](moduleExpressions.html#music21.expressions.Expression.name "music21.expressions.Expression.name") |  |  |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`DalSegnoAlCoda`](#music21.repeat.DalSegnoAlCoda "music21.repeat.DalSegnoAlCoda") read/write properties

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`DalSegnoAlCoda`](#music21.repeat.DalSegnoAlCoda "music21.repeat.DalSegnoAlCoda") methods

Methods inherited from [`RepeatExpression`](#music21.repeat.RepeatExpression "music21.repeat.RepeatExpression"):

|  |  |  |
| --- | --- | --- |
| * [`applyTextFormatting()`](#music21.repeat.RepeatExpression.applyTextFormatting "music21.repeat.RepeatExpression.applyTextFormatting") * [`getText()`](#music21.repeat.RepeatExpression.getText "music21.repeat.RepeatExpression.getText") | * [`getTextExpression()`](#music21.repeat.RepeatExpression.getTextExpression "music21.repeat.RepeatExpression.getTextExpression") * [`isValidText()`](#music21.repeat.RepeatExpression.isValidText "music21.repeat.RepeatExpression.isValidText") | * [`setText()`](#music21.repeat.RepeatExpression.setText "music21.repeat.RepeatExpression.setText") * [`setTextExpression()`](#music21.repeat.RepeatExpression.setTextExpression "music21.repeat.RepeatExpression.setTextExpression") |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`DalSegnoAlCoda`](#music21.repeat.DalSegnoAlCoda "music21.repeat.DalSegnoAlCoda") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## RepeatFinder

class music21.repeat.RepeatFinder(*inpStream=None*, *defaultMeasureHashFunction=None*)[[source]](../_modules/music21/repeat.html#RepeatFinder)
:   An object for finding and simplifying repeated sections of music. Must be passed a stream
    which contains either measures or parts containing measures.

    To collapse a repeated section, call RepeatFinder.simplify() and to see
    which sections of a piece
    are repeated, call either RepeatFinder.getMeasureSimilarityList() or
    RepeatFinder.getSimilarMeasureGroups (see below for full documentation).

    If the internal stream passed to RepeatFinder is altered in any way
    (e.g. if you call simplify() with inplace=True)
    then to ensure proper functionality, you should use a new RepeatFinder object.

    Below is an example of calling simplify on a Bach chorale.

    ```python
    >>> chorale = corpus.parse('bwv117.4.mxl')
    >>> chorale.show()
    ```

    Only the first 8 bars are displayed below

    [![../_images/repeat-SimplifyExample_Chorale.PNG](../_images/repeat-SimplifyExample_Chorale.PNG)](../_images/repeat-SimplifyExample_Chorale.PNG)

    ```python
    >>> repeat.RepeatFinder(chorale).simplify().show()
    ```

    The same chorale as before, but simplified

    [![../_images/repeat-SimplifyExample_ChoraleSimplified.PNG](../_images/repeat-SimplifyExample_ChoraleSimplified.PNG)](../_images/repeat-SimplifyExample_ChoraleSimplified.PNG)

[`RepeatFinder`](#music21.repeat.RepeatFinder "music21.repeat.RepeatFinder") methods

RepeatFinder.getMeasureSimilarityList()[[source]](../_modules/music21/repeat.html#RepeatFinder.getMeasureSimilarityList)
:   Returns a list mList = [ [2, 3], [3], … ] such that measures i and j are the
    same (with i < j) if and only
    if mList[i] contains j. NOTE: this function refers to the very first measure
    as measure 0 regardless of whether
    s starts with measure 0 or 1 (i.e. treats a pickup bar as an entire measure).

    For instance, if getMeasureSimilarityList returned [[4], [5], [6], [7, 8],
    [], [], [], [8], []], we would know that the first
    four measures repeat and the 4th, 8th, and 9th measures are the same.

    Measures are considered the same if the defaultHash maps
    them to two values which are
    equal under the ‘==’ operator.

    ```python
    >>> chorale = corpus.parse('bwv154.3.mxl')
    ```

    Expand the repeats:

    ```python
    >>> chorale = repeat.Expander(chorale.parts[0]).process()
    ```

    Search for similarity:

    ```python
    >>> repeat.RepeatFinder(chorale).getMeasureSimilarityList()
    [[4, 12], [5, 13], [6], [7], [12], [13], [], [], [], [], [], [], [], [], [], []]
    ```

    ```python
    >>> chorale2 = corpus.parse('bwv153.5.mxl')
    >>> chorale2 = repeat.Expander(chorale2.parts[0]).process()
    >>> repeat.RepeatFinder(chorale2).getMeasureSimilarityList()  # bwv153.5 has a pickup
    [[5], [6], [7], [8], [9], [], [], [], [], [], [15], [], [], [], [19], [], [], [], [], []]
    >>> hashFunction = lambda m : str(len(m))
    ```

    ```python
    >>> repeat.RepeatFinder(chorale.measures(1, 8),
    ...                     defaultMeasureHashFunction=hashFunction).getMeasureSimilarityList()
    [[1, 2, 4, 5, 6, 8, 10], [2, 4, 5, 6, 8, 10], [4, 5, 6, 8, 10],
     [7, 9, 11], [5, 6, 8, 10], [6, 8, 10], [8, 10], [9, 11], [10], [11], [], []]
    ```

RepeatFinder.getQuarterLengthOfPickupMeasure()[[source]](../_modules/music21/repeat.html#RepeatFinder.getQuarterLengthOfPickupMeasure)
:   Looks at RepeatFinder’s internal stream and returns the duration of the pickup bar
    in quarterLengths. If there is no pickup, returns 0.0.

    Raises an exception if RepeatFinder’s internal stream is too short
    (i.e. fewer than 3 measures long)

    ```python
    >>> noPickup = corpus.parse('bwv10.7.mxl')
    >>> repeat.RepeatFinder(noPickup).getQuarterLengthOfPickupMeasure()
    0.0
    >>> noPickup.parts[0].measures(0, 5).show()
    ```

    [![../_images/repeat-rf_noPickup.PNG](../_images/repeat-rf_noPickup.PNG)](../_images/repeat-rf_noPickup.PNG)

    ```python
    >>> hasPickup = corpus.parse('bwv101.7.mxl')
    >>> repeat.RepeatFinder(hasPickup).getQuarterLengthOfPickupMeasure()
    1.0
    >>> hasPickup.parts[0].measures(0, 2).show()
    ```

    [![../_images/repeat-rf_hasPickup.PNG](../_images/repeat-rf_hasPickup.PNG)](../_images/repeat-rf_hasPickup.PNG)

    ```python
    >>> tooShort = noPickup.parts[0].measures(1, 2)
    >>> repeat.RepeatFinder(tooShort).getQuarterLengthOfPickupMeasure()
    Traceback (most recent call last):
    music21.repeat.InsufficientLengthException: Cannot determine length
        of pickup given fewer than 3 measures
    ```

RepeatFinder.getSimilarMeasureGroups(*threshold=1*)[[source]](../_modules/music21/repeat.html#RepeatFinder.getSimilarMeasureGroups)
:   Returns a list of tuples containing information on repeated groups of measures.

    Specifically, returns a list of tuples of the form (l1, l2)
    where l1 and l2 are lists
    of measure numbers such that measure l1[i] is the same as measure l2[i].

    ```python
    >>> chorale = corpus.parse('bwv117.4.mxl')
    ```

    Expand repeats

    ```python
    >>> chorale = repeat.Expander(chorale.parts[0]).process()
    >>> chorale.show()
    ```

    Measures 0-4 are the same as measures 5-9.

    [![../_images/repeat-SimplifyExample_Chorale.PNG](../_images/repeat-SimplifyExample_Chorale.PNG)](../_images/repeat-SimplifyExample_Chorale.PNG)

    ```python
    >>> repeat.RepeatFinder(chorale).getSimilarMeasureGroups()
    [([0, 1, 2, 3, 4], [5, 6, 7, 8, 9]), ([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]), ([0], [10])]
    ```

    Notice that although measures 2-3 are the same as measures 6-7, we
    don’t have ([2, 3], [6, 7]) in our result, since ([1, 2, 3], [5, 6, 7])
    already contains that information.

RepeatFinder.hasPickup()[[source]](../_modules/music21/repeat.html#RepeatFinder.hasPickup)
:   Returns True when the RepeatFinder’s internal stream has a pickup bar.

    Raises an exception if the internal stream is too short
    (i.e. fewer than 3 bars long).

    ```python
    >>> noPickup = corpus.parse('bwv10.7.mxl')
    >>> repeat.RepeatFinder(noPickup).hasPickup()
    False
    >>> noPickup.parts[0].measures(0, 5).show()
    ```

    [![../_images/repeat-rf_noPickup.PNG](../_images/repeat-rf_noPickup.PNG)](../_images/repeat-rf_noPickup.PNG)

    ```python
    >>> hasPickup = corpus.parse('bwv101.7.mxl')
    >>> repeat.RepeatFinder(hasPickup).hasPickup()
    True
    >>> hasPickup.parts[0].measures(0, 2).show()
    ```

    [![../_images/repeat-rf_hasPickup.PNG](../_images/repeat-rf_hasPickup.PNG)](../_images/repeat-rf_hasPickup.PNG)

RepeatFinder.simplify(*repeatThreshold=4*, *repeatEndingThreshold=3*, *\**, *inPlace=False*)[[source]](../_modules/music21/repeat.html#RepeatFinder.simplify)
:   Takes the piece stored in the RepeatFinder object and collapses repeated sections by
    replacing them with repeat signs. Includes first and second endings where appropriate.

    Only detects repeated sections which are repeatThreshold bars long and only
    detects repeat endings
    where the repeated sections is more than repeatEndingThreshold bars long.
    If inPlace is True, does not return a new music21 object, but instead alters
    the stream passed to
    the RepeatFinder object.

    In the below example, we have an 8-measure stream where the last four measures
    are identical to the
    first four.

    ```python
    >>> s = stream.Stream()
    >>> notes = [note.Note('D'), note.Note('E-'), note.Note('C'), note.Note('B3'),
    ...           note.Note('D'), note.Note('E-'), note.Note('C'), note.Note('B3')]
    >>> for i in range(8):
    ...    m = stream.Measure()
    ...    m.number = i + 1
    ...    myNote = notes[i]
    ...    myNote.duration.quarterLength = 4.0
    ...    m.append(myNote)
    ...    s.append(m)
    >>> s.show()
    ```

    [![../_images/repeat-RepeatFinderDSCH.PNG](../_images/repeat-RepeatFinderDSCH.PNG)](../_images/repeat-RepeatFinderDSCH.PNG)

    ```python
    >>> s2 = repeat.RepeatFinder(s).simplify()
    >>> s2.show()
    ```

    [![../_images/repeat-RepeatFinderDSCHsimplified.PNG](../_images/repeat-RepeatFinderDSCHsimplified.PNG)](../_images/repeat-RepeatFinderDSCHsimplified.PNG)

[`RepeatFinder`](#music21.repeat.RepeatFinder "music21.repeat.RepeatFinder") instance variables

RepeatFinder.correctMeasureNumbers
:   boolean whether measure numbers should be corrected

RepeatFinder.defaultHash
:   A function that takes a stream of notes and rests and
    returns a string or an
    integer such that two measures are equal if their
    hashes are equal under the ‘==’ operator

RepeatFinder.s
:   The internal stream which is being analyzed for repeated sections

## Expander

class music21.repeat.Expander(*streamObj: StreamType*)[[source]](../_modules/music21/repeat.html#Expander)
:   The Expander object can expand a single Part or Part-like Stream with repeats. Nested
    repeats given with [`Repeat`](moduleBar.html#music21.bar.Repeat "music21.bar.Repeat") objects, or
    repeats and sections designated with
    [`RepeatExpression`](#music21.repeat.RepeatExpression "music21.repeat.RepeatExpression") objects, are all expanded.

    This class is a utility processor. Direct usage is more commonly
    from the `expandRepeats()` method.

    To use this object directly, call [`process()`](#music21.repeat.Expander.process "music21.repeat.Expander.process") on the
    score

    ```python
    >>> s = converter.parse('tinynotation: 3/4 A2. C4 D E F2.')
    >>> s.makeMeasures(inPlace=True)
    >>> s.measure(2).leftBarline = bar.Repeat(direction='start')
    >>> s.measure(2).rightBarline = bar.Repeat(direction='end', times=3)
    >>> s.show('text')
    {0.0} <music21.stream.Measure 1 offset=0.0>
        {0.0} <music21.clef.BassClef>
        {0.0} <music21.meter.TimeSignature 3/4>
        {0.0} <music21.note.Note A>
    {3.0} <music21.stream.Measure 2 offset=3.0>
        {0.0} <music21.bar.Repeat direction=start>
        {0.0} <music21.note.Note C>
        {1.0} <music21.note.Note D>
        {2.0} <music21.note.Note E>
        {3.0} <music21.bar.Repeat direction=end times=3>
    {6.0} <music21.stream.Measure 3 offset=6.0>
        {0.0} <music21.note.Note F>
        {3.0} <music21.bar.Barline type=final>
    ```

    ```python
    >>> e = repeat.Expander(s)
    >>> e.repeatBarsAreCoherent()
    True
    >>> s2 = e.process()
    >>> s2.show('text')
    {0.0} <music21.stream.Measure 1 offset=0.0>
        {0.0} <music21.clef.BassClef>
        {0.0} <music21.meter.TimeSignature 3/4>
        {0.0} <music21.note.Note A>
    {3.0} <music21.stream.Measure 2 offset=3.0>
        {0.0} <music21.bar.Barline type=double>
        {0.0} <music21.note.Note C>
        {1.0} <music21.note.Note D>
        {2.0} <music21.note.Note E>
        {3.0} <music21.bar.Barline type=double>
    {6.0} <music21.stream.Measure 2a offset=6.0>
        {0.0} <music21.bar.Barline type=double>
        {0.0} <music21.note.Note C>
        {1.0} <music21.note.Note D>
        {2.0} <music21.note.Note E>
        {3.0} <music21.bar.Barline type=double>
    {9.0} <music21.stream.Measure 2b offset=9.0>
        {0.0} <music21.bar.Barline type=double>
        {0.0} <music21.note.Note C>
        {1.0} <music21.note.Note D>
        {2.0} <music21.note.Note E>
        {3.0} <music21.bar.Barline type=double>
    {12.0} <music21.stream.Measure 3 offset=12.0>
        {0.0} <music21.note.Note F>
        {3.0} <music21.bar.Barline type=final>
    ```

    Changed in v9: Expander must be initialized with a Stream object.

[`Expander`](#music21.repeat.Expander "music21.repeat.Expander") methods

Expander.findInnermostRepeatIndices(*streamObj*)[[source]](../_modules/music21/repeat.html#Expander.findInnermostRepeatIndices)
:   Find the innermost repeat bars. Return raw index values.
    For a single measure, this could be [2]
    For many contiguous measures, this might be [2, 3, 4, 5]

    The provided Stream must be a Stream only of Measures.

    ```python
    >>> s = converter.parse('tinynotation: 3/4 A2.  C4 D E   F2.    G4 a b   c2.')
    >>> s.makeMeasures(inPlace=True)
    >>> s.measure(2).leftBarline = bar.Repeat(direction='start')
    >>> s.measure(2).rightBarline = bar.Repeat(direction='end', times=3)
    >>> s.measure(4).leftBarline = bar.Repeat(direction='start')
    >>> s.measure(4).rightBarline = bar.Repeat(direction='end', times=2)
    >>> e = repeat.Expander(s)
    >>> e.findInnermostRepeatIndices(s)
    [1]
    ```

    ```python
    >>> s.measure(2).rightBarline = None
    >>> s.measure(4).leftBarline = None
    >>> e2 = repeat.Expander(s)
    >>> e2.findInnermostRepeatIndices(s)
    [1, 2, 3]
    ```

Expander.getRepeatExpressionIndex(*streamObj*, *target*)[[source]](../_modules/music21/repeat.html#Expander.getRepeatExpressionIndex)
:   Return a list of index positions of a Measure given a
    stream of measures. This requires the provided stream
    to only have measures.

    ```python
    >>> s = converter.parse('tinynotation: 3/4 A2. C4 D E F2.')
    >>> s.makeMeasures(inPlace=True)
    >>> s.measure(3).append(repeat.Segno())
    >>> e = repeat.Expander(s)
    ```

    getRepeatExpressionIndex returns the measureIndex not measure number

    ```python
    >>> e.getRepeatExpressionIndex(s.getElementsByClass(stream.Measure), 'Segno')
    [2]
    ```

Expander.isExpandable() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/repeat.html#Expander.isExpandable)
:   Return True or False if this Stream is expandable, that is,
    if it has balanced repeats or sensible Da Capo or Dal Segno
    indications.

    Return None if there’s nothing to expand (a third case).

Expander.measureMap(*returnType='index'*)[[source]](../_modules/music21/repeat.html#Expander.measureMap)
:   returns a list where for each measure in the expanded stream, the index of the
    measure in the original
    stream is given. if returnType = ‘measureNumber’ then the str(measureNumber)
    of the original instead of the
    index of the original is used – suffixes are important here for endings etc..

    Inefficient, because the entire stream is expanded before making this call,
    rather than just seeing
    what needs to be expanded and returning that.

    ```python
    >>> s = converter.parse('tinynotation: 3/4 A2.  C4 D E   F2.    G4 a b   c2.')
    >>> s.makeMeasures(inPlace=True)
    >>> s.measure(2).leftBarline = bar.Repeat(direction='start')
    >>> s.measure(2).rightBarline = bar.Repeat(direction='end', times=3)
    >>> s.measure(4).leftBarline = bar.Repeat(direction='start')
    >>> s.measure(4).rightBarline = bar.Repeat(direction='end', times=2)
    >>> e = repeat.Expander(s)
    >>> e.measureMap()
    [0, 1, 1, 1, 2, 3, 3, 4]
    >>> e.measureMap(returnType='measureNumber')
    ['1', '2', '2a', '2b', '3', '4', '4a', '5']
    ```

Expander.process(*deepcopy: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*) → StreamType[[source]](../_modules/music21/repeat.html#Expander.process)
:   This is the main call for Expander

    Processes all repeats. Note that this processing only
    happens for Measures contained in the given Stream.
    Other objects in that Stream are neither processed nor copied.

    if deepcopy is False then it will leave the stream in an unusual state, but acceptable if
    the source stream has already been deep-copied and will be discarded later

Expander.processInnermostRepeatBars(*streamObj*, *repeatIndices=None*, *repeatTimes=None*, *returnExpansionOnly=False*)[[source]](../_modules/music21/repeat.html#Expander.processInnermostRepeatBars)
:   Process and return a new Stream of Measures, likely a Part.

    If repeatIndices are given, only these indices will be copied.
    All the included indices must be listed, not just the start and end.

    If returnExpansionOnly is True, only the expanded portion is
    returned, the rest of the Stream is not retained.

    ```python
    >>> s = converter.parse('tinynotation: 3/4 A2.  C4 D E   F2.    G4 a b   c2.')
    >>> s.makeMeasures(inPlace=True)
    >>> s.measure(2).leftBarline = bar.Repeat(direction='start')
    >>> s.measure(2).rightBarline = bar.Repeat(direction='end', times=3)
    >>> s.measure(4).leftBarline = bar.Repeat(direction='start')
    >>> s.measure(4).rightBarline = bar.Repeat(direction='end', times=2)
    ```

    processInnermostRepeatBars only will expand the first set of repeats.

    ```python
    >>> e = repeat.Expander(s)
    >>> s2 = e.processInnermostRepeatBars(s)
    >>> s2.show('text')
    {0.0} <music21.stream.Measure 1 offset=0.0>
        {0.0} <music21.clef.BassClef>
        {0.0} <music21.meter.TimeSignature 3/4>
        {0.0} <music21.note.Note A>
    {3.0} <music21.stream.Measure 2 offset=3.0>
        {0.0} <music21.bar.Barline type=double>
        {0.0} <music21.note.Note C>
        {1.0} <music21.note.Note D>
        {2.0} <music21.note.Note E>
        {3.0} <music21.bar.Barline type=double>
    {6.0} <music21.stream.Measure 2a offset=6.0>
        {0.0} <music21.bar.Barline type=double>
        {0.0} <music21.note.Note C>
        {1.0} <music21.note.Note D>
        {2.0} <music21.note.Note E>
        {3.0} <music21.bar.Barline type=double>
    {9.0} <music21.stream.Measure 2b offset=9.0>
        {0.0} <music21.bar.Barline type=double>
        {0.0} <music21.note.Note C>
        {1.0} <music21.note.Note D>
        {2.0} <music21.note.Note E>
        {3.0} <music21.bar.Barline type=double>
    {12.0} <music21.stream.Measure 3 offset=12.0>
        {0.0} <music21.note.Note F>
    {15.0} <music21.stream.Measure 4 offset=15.0>
        {0.0} <music21.bar.Repeat direction=start>
        {0.0} <music21.note.Note G>
        {1.0} <music21.note.Note A>
        {2.0} <music21.note.Note B>
        {3.0} <music21.bar.Repeat direction=end times=2>
    {18.0} <music21.stream.Measure 5 offset=18.0>
        {0.0} <music21.note.Note C>
        {3.0} <music21.bar.Barline type=final>
    ```

    Calling it again will complete the job, as .process() does

    ```python
    >>> s3 = e.processInnermostRepeatBars(s2)
    >>> s3.show('text')
    {0.0} <music21.stream.Measure 1 offset=0.0>
    ...
    {3.0} <music21.stream.Measure 2 offset=3.0>
    ...
    {6.0} <music21.stream.Measure 2a offset=6.0>
    ...
    {9.0} <music21.stream.Measure 2b offset=9.0>
    ...
    {12.0} <music21.stream.Measure 3 offset=12.0>
    ...
    {15.0} <music21.stream.Measure 4 offset=15.0>
        {0.0} <music21.bar.Barline type=double>
        {0.0} <music21.note.Note G>
        {1.0} <music21.note.Note A>
        {2.0} <music21.note.Note B>
        {3.0} <music21.bar.Barline type=double>
    {18.0} <music21.stream.Measure 4a offset=18.0>
        {0.0} <music21.bar.Barline type=double>
        {0.0} <music21.note.Note G>
        {1.0} <music21.note.Note A>
        {2.0} <music21.note.Note B>
        {3.0} <music21.bar.Barline type=double>
    {21.0} <music21.stream.Measure 5 offset=21.0>
    ...
    ```

    Should work even if no start repeat is given:

    ```python
    >>> s = converter.parse('tinynotation: 3/4 A2.  C4 D E   F2.    G4 a b   c2.')
    >>> s.makeMeasures(inPlace=True)
    >>> s.measure(2).rightBarline = bar.Repeat(direction='end')
    >>> e = repeat.Expander(s)
    >>> s2 = e.processInnermostRepeatBars(s)
    >>> s2.show('text')
    {0.0} <music21.stream.Measure 1 offset=0.0>
    ...
    {3.0} <music21.stream.Measure 2 offset=3.0>
    ...
    {6.0} <music21.stream.Measure 1a offset=6.0>
    ...
    {9.0} <music21.stream.Measure 2a offset=9.0>
    ...
        {3.0} <music21.bar.Barline type=double>
    {12.0} <music21.stream.Measure 3 offset=12.0>
    ...
    {15.0} <music21.stream.Measure 4 offset=15.0>
    ...
    {18.0} <music21.stream.Measure 5 offset=18.0>
    ...
        {3.0} <music21.bar.Barline type=final>
    ```

Expander.repeatBarsAreCoherent()[[source]](../_modules/music21/repeat.html#Expander.repeatBarsAreCoherent)
:   Check that all repeat bars are paired properly. Returns True or False

## RepeatMark

class music21.repeat.RepeatMark[[source]](../_modules/music21/repeat.html#RepeatMark)
:   Base class of all repeat objects, including RepeatExpression objects and
    Repeat (Barline) objects.

    This object is used for multiple-inheritance of such objects and to filter by class in order
    to get all things that mark repeats.

    The RepeatMark is not itself a [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object") so you should use multiple
    inheritance to put these things in Streams.

    The following demonstration shows how a user might see if a Stream has any repeats in it.

    ```python
    >>> class PartialRepeat(repeat.RepeatMark, base.Music21Object):
    ...    def __init__(self, **keywords):
    ...        super().__init__(**keywords)
    ```

    ```python
    >>> s = stream.Stream()
    >>> s.append(note.Note())
    >>> s.append(PartialRepeat())
    >>> repeats = s.getElementsByClass('RepeatMark')  # not a Music21Object, so use quotes
    >>> if repeats:
    ...    print(f'Stream has {len(repeats)} repeat(s) in it')
    Stream has 1 repeat(s) in it
    ```

[`RepeatMark`](#music21.repeat.RepeatMark "music21.repeat.RepeatMark") bases

* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`RepeatMark`](#music21.repeat.RepeatMark "music21.repeat.RepeatMark") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

## Functions

music21.repeat.deleteMeasures(*s*, *toDelete*, *\**, *inPlace=False*, *correctMeasureNumbers=True*)[[source]](../_modules/music21/repeat.html#deleteMeasures)
:   Given a Stream s and a list of numbers, toDelete, removes each measure
    with a number corresponding to a number in toDelete and then renumbers
    the remaining measures in the Stream.

    TODO: Move to someplace more appropriate.

    ```python
    >>> from copy import deepcopy
    >>> chorale1 = corpus.parse('bwv10.7.mxl')
    >>> s = deepcopy(chorale1)
    >>> repeat.deleteMeasures(s, [6, 3, 4], inPlace=True)
    >>> m2 = search.translateStreamToString(chorale1.parts[1].measure(2).notesAndRests)
    >>> resm2 = search.translateStreamToString(s.parts[1].measure(2).notesAndRests)
    >>> m2 == resm2
    True
    >>> m5 = search.translateStreamToString(chorale1.parts[1].measure(5).notesAndRests)
    >>> resm3 = search.translateStreamToString(s.parts[1].measure(3).notesAndRests)
    >>> m5 == resm3
    True
    >>> m7 = search.translateStreamToString(chorale1.parts[1].measure(7).notesAndRests)
    >>> resm4 = search.translateStreamToString(s.parts[1].measure(4).notesAndRests)
    >>> m7 == resm4
    True
    >>> lenS = len(s.parts[0].getElementsByClass(stream.Measure))
    >>> lenChorale1 = len(chorale1.parts[0].getElementsByClass(stream.Measure))
    >>> lenS + 3 == lenChorale1
    True
    ```

music21.repeat.insertRepeat(*s*, *start*, *end*, *\**, *inPlace=False*)[[source]](../_modules/music21/repeat.html#insertRepeat)
:   Given a stream s, inserts a start-repeat at the beginning of the
    bar specified by start and inserts an end-repeat at the bar specified
    by barEnd. Only alters the stream s if inPlace=True.

    ```python
    >>> from copy import deepcopy
    >>> chorale1 = corpus.parse('bwv10.7.mxl')
    >>> s = repeat.insertRepeat(chorale1, 3, 6, inPlace=False)
    >>> m4 = search.translateStreamToString( chorale1.parts[1].measure(4).notesAndRests)
    >>> resm4 = search.translateStreamToString( s.parts[1].measure(4).notesAndRests)
    >>> m6 = search.translateStreamToString( chorale1.parts[1].measure(4).notesAndRests)
    >>> resm6 = search.translateStreamToString( s.parts[1].measure(4).notesAndRests)
    >>> m7 = search.translateStreamToString( chorale1.parts[1].measure(4).notesAndRests)
    >>> resm7 = search.translateStreamToString( s.parts[1].measure(4).notesAndRests)
    >>> m4 == resm4
    True
    >>> m6 == resm6
    True
    >>> m7 == resm7
    True
    ```

    We should have 2 repeats in each part (a start and end) for a total of 8 repeats

    ```python
    >>> len(s.parts[0].flatten().getElementsByClass(bar.Repeat))
    2
    >>> len(s[bar.Repeat])
    8
    >>> s.parts[0].measure(3).leftBarline.direction
    'start'
    >>> s.parts[0].measure(6).rightBarline.direction
    'end'
    ```

music21.repeat.insertRepeatEnding(*s*, *start*, *end*, *endingNumber: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 1*, *\**, *inPlace=False*)[[source]](../_modules/music21/repeat.html#insertRepeatEnding)
:   Designates a range of measures as being repeated endings (i.e. first and second endings)
    within a stream s, where s either contains measures,
    or contains parts which contain measures. Start and end are integers
    corresponding to the first and last measure
    number of the “repeatNum” ending. e.g. if start=6, end=7, and repeatNum=2,
    the method adds a second ending
    from measures 6 to 7.

    Does not (yet) add a [`RepeatMark`](#music21.repeat.RepeatMark "music21.repeat.RepeatMark") to the end of the first ending.

    Example: create first and second endings over measures 4-6 and measures 11-13 of a chorale,
    respectively.

    ```python
    >>> c1 = corpus.parse('bwv10.7.mxl')
    >>> repeat.insertRepeatEnding(c1,  4,  6, 1, inPlace=True)
    >>> repeat.insertRepeatEnding(c1, 11, 13, 2, inPlace=True)
    ```

    We now have 8 repeatBrackets since each part gets its own first and second ending.

    ```python
    >>> repeatBrackets = c1.flatten().getElementsByClass(spanner.RepeatBracket)
    >>> len(repeatBrackets)
    8
    >>> len(c1.parts.first().getElementsByClass(spanner.RepeatBracket))
    2
    ```
