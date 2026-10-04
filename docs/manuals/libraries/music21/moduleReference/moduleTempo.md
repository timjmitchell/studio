Source: https://music21.org/music21docs/moduleReference/moduleTempo.html

# music21.tempo

This module defines objects for describing tempo and changes in tempo.

## MetronomeMark

class music21.tempo.MetronomeMark(*text: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *number: OffsetQLIn | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *referent: OffsetQLIn | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [duration.Duration](moduleDuration.html#music21.duration.Duration "music21.duration.Duration") | [base.Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\**, *parentheses: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *playbackOnly: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *numberSounding: OffsetQLIn | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *numberImplicit: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\*\*keywords*)[[source]](../_modules/music21/tempo.html#MetronomeMark)
:   A way of specifying a particular tempo with a text string,
    a referent (a duration) and a number.

    The referent attribute is a Duration object, or a string duration type or
    a floating-point quarter-length value used to create a Duration.

    MetronomeMarks, as Music21Object subclasses, also have .duration object
    property independent of the referent.

    ```python
    >>> a = tempo.MetronomeMark('slow', 40, note.Note(type='half'))
    >>> a.number
    40
    >>> a.referent
    <music21.duration.Duration 2.0>
    >>> a.referent.type
    'half'
    >>> print(a.text)
    slow
    ```

    Some text marks will automatically suggest a number.

    ```python
    >>> mm = tempo.MetronomeMark('adagio')
    >>> mm.number
    56
    >>> mm.numberImplicit
    True
    ```

    For certain numbers, a text value can be set implicitly

    ```python
    >>> tm2 = tempo.MetronomeMark(number=208)
    >>> print(tm2.text)
    prestissimo
    >>> tm2.referent
    <music21.duration.Duration 1.0>
    ```

    Unicode values work fine thanks to Python 3:

    ```python
    >>> marking = 'très vite'
    >>> marking
    'très vite'
    >>> print(tempo.defaultTempoValues[marking])
    144
    >>> tm2 = tempo.MetronomeMark(marking)
    >>> tm2.text.endswith('vite')
    True
    >>> tm2.number
    144
    ```

    For playback only (no score output) set numberSounding but no number:

    ```python
    >>> fast = tempo.MetronomeMark(numberSounding=168)
    >>> fast
    <music21.tempo.MetronomeMark Quarter=168 (playback only)>
    ```

[`MetronomeMark`](#music21.tempo.MetronomeMark "music21.tempo.MetronomeMark") bases

* [`TempoIndication`](#music21.tempo.TempoIndication "music21.tempo.TempoIndication")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`MetronomeMark`](#music21.tempo.MetronomeMark "music21.tempo.MetronomeMark") read-only properties

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`MetronomeMark`](#music21.tempo.MetronomeMark "music21.tempo.MetronomeMark") read/write properties

MetronomeMark.number
:   Get and set the number, or the numerical value of the Metronome.

    ```python
    >>> mm = tempo.MetronomeMark('slow')
    >>> mm.number
    56
    >>> mm.numberImplicit
    True
    >>> mm.number = 52.5
    >>> mm.number
    52.5
    >>> mm.numberImplicit
    False
    ```

MetronomeMark.numberSounding
:   Get and set the numberSounding, or the numerical value of the Metronome that
    is used for playback independent of display. If numberSounding is None, number is
    assumed to be numberSounding.

    ```python
    >>> mm = tempo.MetronomeMark('slow')
    >>> mm.number
    56
    >>> mm.numberImplicit
    True
    >>> mm.numberSounding is None
    True
    >>> mm.numberSounding = 120
    >>> mm.numberSounding
    120
    ```

MetronomeMark.referent
:   Get or set the referent, or the Duration object that is the
    reference for the tempo value in BPM.

MetronomeMark.text
:   Get or set a text string for this MetronomeMark. Internally implemented as a
    [`TempoText`](#music21.tempo.TempoText "music21.tempo.TempoText") object, which stores the text in
    a `TextExpression` object.

    ```python
    >>> mm = tempo.MetronomeMark(number=123)
    >>> mm.text == None
    True
    >>> mm.text = 'medium fast'
    >>> print(mm.text)
    medium fast
    ```

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`MetronomeMark`](#music21.tempo.MetronomeMark "music21.tempo.MetronomeMark") methods

MetronomeMark.durationToSeconds(*durationOrQuarterLength*)[[source]](../_modules/music21/tempo.html#MetronomeMark.durationToSeconds)
:   Given a duration specified as a [`Duration`](moduleDuration.html#music21.duration.Duration "music21.duration.Duration") object or a
    quarter length, return the resultant time in seconds at the tempo specified by
    this MetronomeMark.

    ```python
    >>> mm1 = tempo.MetronomeMark(referent=1.0, number=60.0)
    >>> mm1.durationToSeconds(60)
    60.0
    >>> mm1.durationToSeconds(duration.Duration('16th'))
    0.25
    ```

MetronomeMark.getEquivalentByReferent(*referent*)[[source]](../_modules/music21/tempo.html#MetronomeMark.getEquivalentByReferent)
:   Return a new MetronomeMark object that has an equivalent speed but
    different number and referent values based on a supplied referent
    (given as a Duration type, quarterLength, or Duration object).

    ```python
    >>> mm1 = tempo.MetronomeMark(number=60, referent=1.0)
    >>> mm1.getEquivalentByReferent(0.5)
    <music21.tempo.MetronomeMark larghetto Eighth=120>
    >>> mm1.getEquivalentByReferent(duration.Duration('half'))
    <music21.tempo.MetronomeMark larghetto Half=30>
    ```

    ```python
    >>> mm1.getEquivalentByReferent('longa')
    <music21.tempo.MetronomeMark larghetto Imperfect Longa=3.75>
    ```

MetronomeMark.getMaintainedNumberWithReferent(*referent*)[[source]](../_modules/music21/tempo.html#MetronomeMark.getMaintainedNumberWithReferent)
:   Return a new MetronomeMark object that has an equivalent number but a new referent.

MetronomeMark.getQuarterBPM(*useNumberSounding=True*) → [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/tempo.html#MetronomeMark.getQuarterBPM)
:   Get a BPM value where the beat is a quarter; must convert from the
    defined beat to a quarter beat. Will return None if no beat number is defined.

    This mostly used for generating MusicXML <sound> tags when necessary.

    ```python
    >>> mm = tempo.MetronomeMark(number=60, referent='half')
    >>> mm.getQuarterBPM()
    120.0
    >>> mm.referent = 'quarter'
    >>> mm.getQuarterBPM()
    60.0
    ```

MetronomeMark.getTextExpression(*returnImplicit=False*)[[source]](../_modules/music21/tempo.html#MetronomeMark.getTextExpression)
:   If there is a TextExpression available that is not implicit, return it;
    otherwise, return None.

    ```python
    >>> mm = tempo.MetronomeMark('presto')
    >>> mm.number
    184
    >>> mm.numberImplicit
    True
    >>> mm.getTextExpression()
    <music21.expressions.TextExpression 'presto'>
    >>> mm.textImplicit
    False
    ```

    ```python
    >>> mm = tempo.MetronomeMark(number=90)
    >>> mm.numberImplicit
    False
    >>> mm.textImplicit
    True
    >>> mm.getTextExpression() is None
    True
    >>> mm.getTextExpression(returnImplicit=True)
    <music21.expressions.TextExpression 'maestoso'>
    ```

MetronomeMark.secondsPerQuarter()[[source]](../_modules/music21/tempo.html#MetronomeMark.secondsPerQuarter)
:   Return the duration in seconds for each quarter length
    (not necessarily the referent) of this MetronomeMark.

    ```python
    >>> mm1 = tempo.MetronomeMark(referent=1.0, number=60.0)
    >>> mm1.secondsPerQuarter()
    1.0
    >>> mm1 = tempo.MetronomeMark(referent=2.0, number=60.0)
    >>> mm1.secondsPerQuarter()
    0.5
    >>> mm1 = tempo.MetronomeMark(referent=2.0, number=30.0)
    >>> mm1.secondsPerQuarter()
    1.0
    ```

MetronomeMark.secondsToDuration(*seconds*)[[source]](../_modules/music21/tempo.html#MetronomeMark.secondsToDuration)
:   Given a duration in seconds,
    return a [`Duration`](moduleDuration.html#music21.duration.Duration "music21.duration.Duration") object equal to that time.

    ```python
    >>> mm1 = tempo.MetronomeMark(referent=1.0, number=60.0)
    >>> mm1.secondsToDuration(0.25)
    <music21.duration.Duration 0.25>
    >>> mm1.secondsToDuration(0.5).type
    'eighth'
    >>> mm1.secondsToDuration(1)
    <music21.duration.Duration 1.0>
    ```

MetronomeMark.setQuarterBPM(*value*, *setNumber=True*)[[source]](../_modules/music21/tempo.html#MetronomeMark.setQuarterBPM)
:   Given a value in BPM, use it to set the value of this MetronomeMark.
    BPM values are assumed to refer only to quarter notes; different beat values,
    if defined here, will be scaled

    ```python
    >>> mm = tempo.MetronomeMark(number=60, referent='half')
    >>> mm.setQuarterBPM(240)  # set to 240 for a quarter
    >>> mm.number  # a half is half as fast
    120
    ```

Methods inherited from [`TempoIndication`](#music21.tempo.TempoIndication "music21.tempo.TempoIndication"):

|  |  |  |
| --- | --- | --- |
| * [`getPreviousMetronomeMark()`](#music21.tempo.TempoIndication.getPreviousMetronomeMark "music21.tempo.TempoIndication.getPreviousMetronomeMark") | * [`getSoundingMetronomeMark()`](#music21.tempo.TempoIndication.getSoundingMetronomeMark "music21.tempo.TempoIndication.getSoundingMetronomeMark") |  |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`MetronomeMark`](#music21.tempo.MetronomeMark "music21.tempo.MetronomeMark") instance variables

MetronomeMark.placement
:   Staff placement: ‘above’, ‘below’, or None.

    A setting of None implies that the placement will be determined
    by notation software and no particular placement is demanded.

    This is not placed in the .style property, since for some expressions,
    the placement above or below an object has semantic
    meaning and is not purely presentational.

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## TempoText

class music21.tempo.TempoText(*text=None*, *\*\*keywords*)[[source]](../_modules/music21/tempo.html#TempoText)
:   ```python
    >>> import music21
    >>> tm = music21.tempo.TempoText('adagio')
    >>> tm
    <music21.tempo.TempoText 'adagio'>
    >>> print(tm.text)
    adagio
    ```

[`TempoText`](#music21.tempo.TempoText "music21.tempo.TempoText") bases

* [`TempoIndication`](#music21.tempo.TempoIndication "music21.tempo.TempoIndication")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`TempoText`](#music21.tempo.TempoText "music21.tempo.TempoText") read-only properties

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`TempoText`](#music21.tempo.TempoText "music21.tempo.TempoText") read/write properties

TempoText.text
:   Get or set the text as a string.

    ```python
    >>> import music21
    >>> tm = music21.tempo.TempoText('adagio')
    >>> tm.text
    'adagio'
    >>> tm.getTextExpression()
    <music21.expressions.TextExpression 'adagio'>
    ```

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`TempoText`](#music21.tempo.TempoText "music21.tempo.TempoText") methods

TempoText.applyTextFormatting(*te=None*, *numberImplicit=False*)[[source]](../_modules/music21/tempo.html#TempoText.applyTextFormatting)
:   Apply the default text formatting to the text expression version of this tempo mark

TempoText.getMetronomeMark()[[source]](../_modules/music21/tempo.html#TempoText.getMetronomeMark)
:   Return a MetronomeMark object that is configured from this objects Text.

    ```python
    >>> tt = tempo.TempoText('slow')
    >>> mm = tt.getMetronomeMark()
    >>> mm.number
    56
    ```

TempoText.getTextExpression(*numberImplicit=False*)[[source]](../_modules/music21/tempo.html#TempoText.getTextExpression)
:   Return a TextExpression object for this text.

    What is this a deepcopy and not the actual one?

TempoText.isCommonTempoText(*value=None*)[[source]](../_modules/music21/tempo.html#TempoText.isCommonTempoText)
:   Return True or False if the supplied text seems like a
    plausible Tempo indications be used for this TempoText.

    ```python
    >>> tt = tempo.TempoText('adagio')
    >>> tt.isCommonTempoText()
    True
    ```

    ```python
    >>> tt = tempo.TempoText('Largo e piano')
    >>> tt.isCommonTempoText()
    True
    ```

    ```python
    >>> tt = tempo.TempoText('undulating')
    >>> tt.isCommonTempoText()
    False
    ```

TempoText.setTextExpression(*value*)[[source]](../_modules/music21/tempo.html#TempoText.setTextExpression)
:   Given a TextExpression, set it in this object.

Methods inherited from [`TempoIndication`](#music21.tempo.TempoIndication "music21.tempo.TempoIndication"):

|  |  |  |
| --- | --- | --- |
| * [`getPreviousMetronomeMark()`](#music21.tempo.TempoIndication.getPreviousMetronomeMark "music21.tempo.TempoIndication.getPreviousMetronomeMark") | * [`getSoundingMetronomeMark()`](#music21.tempo.TempoIndication.getSoundingMetronomeMark "music21.tempo.TempoIndication.getSoundingMetronomeMark") |  |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`TempoText`](#music21.tempo.TempoText "music21.tempo.TempoText") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## MetricModulation

class music21.tempo.MetricModulation(*\*\*keywords*)[[source]](../_modules/music21/tempo.html#MetricModulation)
:   A class for representing the relationship between two MetronomeMarks.
    Generally this relationship is one of equality, where the number is maintained but
    the referent that number is applied to each change.

    The basic definition of a MetricModulation is given by supplying two MetronomeMarks,
    one for the oldMetronome, the other for the newMetronome. High level properties,
    oldReferent and newReferent, and convenience methods permit only setting the referent.

    The classicalStyle attribute determines of the first MetronomeMark describes the
    new tempo, not the old (the reverse of expected usage).

    The maintainBeat attribute determines if, after an equality statement,
    the beat is maintained. This is relevant for moving from 3/4 to 6/8, for example.

    ```python
    >>> s = stream.Stream()
    >>> mm1 = tempo.MetronomeMark(number=60)
    >>> s.append(mm1)
    >>> s.repeatAppend(note.Note(quarterLength=1), 2)
    >>> s.repeatAppend(note.Note(quarterLength=0.5), 4)
    ```

    ```python
    >>> mmod1 = tempo.MetricModulation()
    >>> mmod1.oldReferent = 0.5  # can use Duration objects
    >>> mmod1.newReferent = 'quarter'  # can use Duration objects
    >>> s.append(mmod1)
    >>> mmod1.updateByContext()  # get number from last MetronomeMark on Stream
    >>> mmod1.newMetronome
    <music21.tempo.MetronomeMark animato Quarter=120>
    ```

    ```python
    >>> s.append(note.Note())
    >>> s.repeatAppend(note.Note(quarterLength=1.5), 2)
    ```

    ```python
    >>> mmod2 = tempo.MetricModulation()
    >>> s.append(mmod2)  # if the obj is added to Stream, can set referents
    >>> mmod2.oldReferent = 1.5  # will get number from previous MetronomeMark
    >>> mmod2.newReferent = 'quarter'
    >>> mmod2.newMetronome
    <music21.tempo.MetronomeMark animato Quarter=80>
    ```

    Note that an initial metric modulation can set old and new referents and get None as
    tempo numbers:

    ```python
    >>> mmod3 = tempo.MetricModulation()
    >>> mmod3.oldReferent = 'half'
    >>> mmod3.newReferent = '16th'
    >>> mmod3
    <music21.tempo.MetricModulation
        <music21.tempo.MetronomeMark
            Half=None>=<music21.tempo.MetronomeMark 16th=None>>
    ```

    test w/ more sane referents that either the old or the new can change without a tempo number

    ```python
    >>> mmod3.oldReferent = 'quarter'
    >>> mmod3.newReferent = 'eighth'
    >>> mmod3
    <music21.tempo.MetricModulation
        <music21.tempo.MetronomeMark
            Quarter=None>=<music21.tempo.MetronomeMark Eighth=None>>
    >>> mmod3.oldMetronome
    <music21.tempo.MetronomeMark Quarter=None>
    >>> mmod3.oldMetronome.number = 60
    ```

    New number automatically updates:

    ```python
    >>> mmod3
    <music21.tempo.MetricModulation
        <music21.tempo.MetronomeMark larghetto
            Quarter=60>=<music21.tempo.MetronomeMark larghetto Eighth=60>>
    ```

[`MetricModulation`](#music21.tempo.MetricModulation "music21.tempo.MetricModulation") bases

* [`TempoIndication`](#music21.tempo.TempoIndication "music21.tempo.TempoIndication")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`MetricModulation`](#music21.tempo.MetricModulation "music21.tempo.MetricModulation") read-only properties

MetricModulation.number
:   Get and the number of the MetricModulation, or the number
    assigned to the new MetronomeMark.

    ```python
    >>> s = stream.Stream()
    >>> mm1 = tempo.MetronomeMark(number=60)
    >>> s.append(mm1)
    >>> s.repeatAppend(note.Note(quarterLength=1), 2)
    >>> s.repeatAppend(note.Note(quarterLength=0.5), 4)
    ```

    ```python
    >>> mmod1 = tempo.MetricModulation()
    >>> mmod1.oldReferent = 0.5  # can use Duration objects
    >>> mmod1.newReferent = 'quarter'
    >>> s.append(mmod1)
    >>> mmod1.updateByContext()
    >>> mmod1.newMetronome
    <music21.tempo.MetronomeMark animato Quarter=120>
    >>> mmod1.number
    120
    ```

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`MetricModulation`](#music21.tempo.MetricModulation "music21.tempo.MetricModulation") read/write properties

MetricModulation.newMetronome
:   Get or set the right [`MetronomeMark`](#music21.tempo.MetronomeMark "music21.tempo.MetronomeMark")
    object for the new, or following value.

    ```python
    >>> mm1 = tempo.MetronomeMark(number=60, referent=1)
    >>> mm1
    <music21.tempo.MetronomeMark larghetto Quarter=60>
    >>> mmod1 = tempo.MetricModulation()
    >>> mmod1.newMetronome = mm1
    >>> mmod1.newMetronome = 'junk'
    Traceback (most recent call last):
    music21.tempo.MetricModulationException: newMetronome property must be
        set with a MetronomeMark instance
    ```

MetricModulation.newReferent
:   Get or set the referent of the new MetronomeMark.

    ```python
    >>> mm1 = tempo.MetronomeMark(number=60, referent=1)
    >>> mmod1 = tempo.MetricModulation()
    >>> mmod1.newMetronome = mm1
    >>> mmod1.newMetronome
    <music21.tempo.MetronomeMark larghetto Quarter=60>
    >>> mmod1.newReferent = 0.25
    >>> mmod1.newMetronome
    <music21.tempo.MetronomeMark larghetto 16th=240>
    ```

MetricModulation.oldMetronome
:   Get or set the left [`MetronomeMark`](#music21.tempo.MetronomeMark "music21.tempo.MetronomeMark") object
    for the old, or previous value.

    ```python
    >>> mm1 = tempo.MetronomeMark(number=60, referent=1)
    >>> mm1
    <music21.tempo.MetronomeMark larghetto Quarter=60>
    >>> mmod1 = tempo.MetricModulation()
    >>> mmod1.oldMetronome = mm1
    ```

    Note that we do need to have a proper MetronomeMark instance to figure this out:

    ```python
    >>> mmod1.oldMetronome = 'junk'
    Traceback (most recent call last):
    music21.tempo.MetricModulationException: oldMetronome property
        must be set with a MetronomeMark instance
    ```

MetricModulation.oldReferent
:   Get or set the referent of the old MetronomeMark.

    ```python
    >>> mm1 = tempo.MetronomeMark(number=60, referent=1)
    >>> mmod1 = tempo.MetricModulation()
    >>> mmod1.oldMetronome = mm1
    >>> mmod1.oldMetronome
    <music21.tempo.MetronomeMark larghetto Quarter=60>
    >>> mmod1.oldReferent = 0.25
    >>> mmod1.oldMetronome
    <music21.tempo.MetronomeMark larghetto 16th=240>
    ```

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`MetricModulation`](#music21.tempo.MetricModulation "music21.tempo.MetricModulation") methods

MetricModulation.setEqualityByReferent(*side=None*, *referent=1.0*)[[source]](../_modules/music21/tempo.html#MetricModulation.setEqualityByReferent)
:   Set the other side of the metric modulation to
    an equality; side can be specified, or if one side
    is None, that side will be set.

    ```python
    >>> mm1 = tempo.MetronomeMark(number=60, referent=1)
    >>> mmod1 = tempo.MetricModulation()
    >>> mmod1.newMetronome = mm1
    >>> mmod1.setEqualityByReferent(None, 2)
    >>> mmod1
    <music21.tempo.MetricModulation
         <music21.tempo.MetronomeMark larghetto
               Half=30>=<music21.tempo.MetronomeMark larghetto Quarter=60>>
    ```

MetricModulation.setOtherByReferent(*side: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *referent: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") = 1.0*)[[source]](../_modules/music21/tempo.html#MetricModulation.setOtherByReferent)
:   Set the other side of the metric modulation not based on equality,
    but on a direct translation of the tempo value.

    referent can be a string type or an int/float quarter length

MetricModulation.updateByContext()[[source]](../_modules/music21/tempo.html#MetricModulation.updateByContext)
:   Update this metric modulation based on the context,
    or the surrounding MetronomeMarks or MetricModulations.
    The object needs to reside in a Stream for this to be effective.

Methods inherited from [`TempoIndication`](#music21.tempo.TempoIndication "music21.tempo.TempoIndication"):

|  |  |  |
| --- | --- | --- |
| * [`getPreviousMetronomeMark()`](#music21.tempo.TempoIndication.getPreviousMetronomeMark "music21.tempo.TempoIndication.getPreviousMetronomeMark") | * [`getSoundingMetronomeMark()`](#music21.tempo.TempoIndication.getSoundingMetronomeMark "music21.tempo.TempoIndication.getSoundingMetronomeMark") |  |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`MetricModulation`](#music21.tempo.MetricModulation "music21.tempo.MetricModulation") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## TempoIndication

class music21.tempo.TempoIndication(*id: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *groups: [Groups](moduleBase.html#music21.base.Groups "music21.base.Groups") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *sites: [Sites](moduleSites.html#music21.sites.Sites "music21.sites.Sites") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *duration: [Duration](moduleDuration.html#music21.duration.Duration "music21.duration.Duration") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *activeSite: stream.Stream | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *style: [Style](moduleStyle.html#music21.style.Style "music21.style.Style") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *editorial: [Editorial](moduleEditorial.html#music21.editorial.Editorial "music21.editorial.Editorial") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *offset: OffsetQL = 0.0*, *quarterLength: OffsetQLIn | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\*\*keywords*)[[source]](../_modules/music21/tempo.html#TempoIndication)
:   A generic base class for all tempo indications to inherit.
    Can be used to filter out all types of tempo indications.

[`TempoIndication`](#music21.tempo.TempoIndication "music21.tempo.TempoIndication") bases

* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`TempoIndication`](#music21.tempo.TempoIndication "music21.tempo.TempoIndication") read-only properties

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`TempoIndication`](#music21.tempo.TempoIndication "music21.tempo.TempoIndication") read/write properties

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`TempoIndication`](#music21.tempo.TempoIndication "music21.tempo.TempoIndication") methods

TempoIndication.getPreviousMetronomeMark()[[source]](../_modules/music21/tempo.html#TempoIndication.getPreviousMetronomeMark)
:   Do activeSite and context searches to try to find the last relevant
    MetronomeMark or MetricModulation object. If a MetricModulation mark is found,
    return the new MetronomeMark, or the last relevant.

    ```python
    >>> s = stream.Stream()
    >>> s.insert(0, tempo.MetronomeMark(number=120))
    >>> mm1 = tempo.MetronomeMark(number=90)
    >>> s.insert(20, mm1)
    >>> mm1.getPreviousMetronomeMark()
    <music21.tempo.MetronomeMark animato Quarter=120>
    ```

TempoIndication.getSoundingMetronomeMark(*found=None*)[[source]](../_modules/music21/tempo.html#TempoIndication.getSoundingMetronomeMark)
:   Get the appropriate MetronomeMark from any sort of TempoIndication, regardless of class.

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`TempoIndication`](#music21.tempo.TempoIndication "music21.tempo.TempoIndication") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## AccelerandoSpanner

class music21.tempo.AccelerandoSpanner(*\*spannedElements: [Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object") | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")]*, *\*\*keywords*)[[source]](../_modules/music21/tempo.html#AccelerandoSpanner)
:   Spanner representing a speeding up.

[`AccelerandoSpanner`](#music21.tempo.AccelerandoSpanner "music21.tempo.AccelerandoSpanner") bases

* [`TempoChangeSpanner`](#music21.tempo.TempoChangeSpanner "music21.tempo.TempoChangeSpanner")
* [`Spanner`](moduleSpanner.html#music21.spanner.Spanner "music21.spanner.Spanner")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`AccelerandoSpanner`](#music21.tempo.AccelerandoSpanner "music21.tempo.AccelerandoSpanner") read-only properties

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`AccelerandoSpanner`](#music21.tempo.AccelerandoSpanner "music21.tempo.AccelerandoSpanner") read/write properties

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`AccelerandoSpanner`](#music21.tempo.AccelerandoSpanner "music21.tempo.AccelerandoSpanner") methods

Methods inherited from [`Spanner`](moduleSpanner.html#music21.spanner.Spanner "music21.spanner.Spanner"):

|  |  |  |
| --- | --- | --- |
| * [`__getitem__()`](moduleSpanner.html#music21.spanner.Spanner.__getitem__ "music21.spanner.Spanner.__getitem__") * [`addSpannedElements()`](moduleSpanner.html#music21.spanner.Spanner.addSpannedElements "music21.spanner.Spanner.addSpannedElements") * [`fill()`](moduleSpanner.html#music21.spanner.Spanner.fill "music21.spanner.Spanner.fill") * [`getFirst()`](moduleSpanner.html#music21.spanner.Spanner.getFirst "music21.spanner.Spanner.getFirst") * [`getLast()`](moduleSpanner.html#music21.spanner.Spanner.getLast "music21.spanner.Spanner.getLast") | * [`getSpannedElementIds()`](moduleSpanner.html#music21.spanner.Spanner.getSpannedElementIds "music21.spanner.Spanner.getSpannedElementIds") * [`getSpannedElements()`](moduleSpanner.html#music21.spanner.Spanner.getSpannedElements "music21.spanner.Spanner.getSpannedElements") * [`getSpannedElementsByClass()`](moduleSpanner.html#music21.spanner.Spanner.getSpannedElementsByClass "music21.spanner.Spanner.getSpannedElementsByClass") * [`hasSpannedElement()`](moduleSpanner.html#music21.spanner.Spanner.hasSpannedElement "music21.spanner.Spanner.hasSpannedElement") * [`insertFirstSpannedElement()`](moduleSpanner.html#music21.spanner.Spanner.insertFirstSpannedElement "music21.spanner.Spanner.insertFirstSpannedElement") | * [`isFirst()`](moduleSpanner.html#music21.spanner.Spanner.isFirst "music21.spanner.Spanner.isFirst") * [`isLast()`](moduleSpanner.html#music21.spanner.Spanner.isLast "music21.spanner.Spanner.isLast") * [`purgeLocations()`](moduleSpanner.html#music21.spanner.Spanner.purgeLocations "music21.spanner.Spanner.purgeLocations") * [`purgeOrphans()`](moduleSpanner.html#music21.spanner.Spanner.purgeOrphans "music21.spanner.Spanner.purgeOrphans") * [`replaceSpannedElement()`](moduleSpanner.html#music21.spanner.Spanner.replaceSpannedElement "music21.spanner.Spanner.replaceSpannedElement") |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") | * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") | * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`AccelerandoSpanner`](#music21.tempo.AccelerandoSpanner "music21.tempo.AccelerandoSpanner") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## RitardandoSpanner

class music21.tempo.RitardandoSpanner(*\*spannedElements: [Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object") | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")]*, *\*\*keywords*)[[source]](../_modules/music21/tempo.html#RitardandoSpanner)
:   Spanner representing a slowing down.

[`RitardandoSpanner`](#music21.tempo.RitardandoSpanner "music21.tempo.RitardandoSpanner") bases

* [`TempoChangeSpanner`](#music21.tempo.TempoChangeSpanner "music21.tempo.TempoChangeSpanner")
* [`Spanner`](moduleSpanner.html#music21.spanner.Spanner "music21.spanner.Spanner")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`RitardandoSpanner`](#music21.tempo.RitardandoSpanner "music21.tempo.RitardandoSpanner") read-only properties

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`RitardandoSpanner`](#music21.tempo.RitardandoSpanner "music21.tempo.RitardandoSpanner") read/write properties

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`RitardandoSpanner`](#music21.tempo.RitardandoSpanner "music21.tempo.RitardandoSpanner") methods

Methods inherited from [`Spanner`](moduleSpanner.html#music21.spanner.Spanner "music21.spanner.Spanner"):

|  |  |  |
| --- | --- | --- |
| * [`__getitem__()`](moduleSpanner.html#music21.spanner.Spanner.__getitem__ "music21.spanner.Spanner.__getitem__") * [`addSpannedElements()`](moduleSpanner.html#music21.spanner.Spanner.addSpannedElements "music21.spanner.Spanner.addSpannedElements") * [`fill()`](moduleSpanner.html#music21.spanner.Spanner.fill "music21.spanner.Spanner.fill") * [`getFirst()`](moduleSpanner.html#music21.spanner.Spanner.getFirst "music21.spanner.Spanner.getFirst") * [`getLast()`](moduleSpanner.html#music21.spanner.Spanner.getLast "music21.spanner.Spanner.getLast") | * [`getSpannedElementIds()`](moduleSpanner.html#music21.spanner.Spanner.getSpannedElementIds "music21.spanner.Spanner.getSpannedElementIds") * [`getSpannedElements()`](moduleSpanner.html#music21.spanner.Spanner.getSpannedElements "music21.spanner.Spanner.getSpannedElements") * [`getSpannedElementsByClass()`](moduleSpanner.html#music21.spanner.Spanner.getSpannedElementsByClass "music21.spanner.Spanner.getSpannedElementsByClass") * [`hasSpannedElement()`](moduleSpanner.html#music21.spanner.Spanner.hasSpannedElement "music21.spanner.Spanner.hasSpannedElement") * [`insertFirstSpannedElement()`](moduleSpanner.html#music21.spanner.Spanner.insertFirstSpannedElement "music21.spanner.Spanner.insertFirstSpannedElement") | * [`isFirst()`](moduleSpanner.html#music21.spanner.Spanner.isFirst "music21.spanner.Spanner.isFirst") * [`isLast()`](moduleSpanner.html#music21.spanner.Spanner.isLast "music21.spanner.Spanner.isLast") * [`purgeLocations()`](moduleSpanner.html#music21.spanner.Spanner.purgeLocations "music21.spanner.Spanner.purgeLocations") * [`purgeOrphans()`](moduleSpanner.html#music21.spanner.Spanner.purgeOrphans "music21.spanner.Spanner.purgeOrphans") * [`replaceSpannedElement()`](moduleSpanner.html#music21.spanner.Spanner.replaceSpannedElement "music21.spanner.Spanner.replaceSpannedElement") |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") | * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") | * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`RitardandoSpanner`](#music21.tempo.RitardandoSpanner "music21.tempo.RitardandoSpanner") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## TempoChangeSpanner

class music21.tempo.TempoChangeSpanner(*\*spannedElements: [Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object") | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")]*, *\*\*keywords*)[[source]](../_modules/music21/tempo.html#TempoChangeSpanner)
:   Spanners showing tempo-change. They do nothing right now.

[`TempoChangeSpanner`](#music21.tempo.TempoChangeSpanner "music21.tempo.TempoChangeSpanner") bases

* [`Spanner`](moduleSpanner.html#music21.spanner.Spanner "music21.spanner.Spanner")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`TempoChangeSpanner`](#music21.tempo.TempoChangeSpanner "music21.tempo.TempoChangeSpanner") read-only properties

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`TempoChangeSpanner`](#music21.tempo.TempoChangeSpanner "music21.tempo.TempoChangeSpanner") read/write properties

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`TempoChangeSpanner`](#music21.tempo.TempoChangeSpanner "music21.tempo.TempoChangeSpanner") methods

Methods inherited from [`Spanner`](moduleSpanner.html#music21.spanner.Spanner "music21.spanner.Spanner"):

|  |  |  |
| --- | --- | --- |
| * [`__getitem__()`](moduleSpanner.html#music21.spanner.Spanner.__getitem__ "music21.spanner.Spanner.__getitem__") * [`addSpannedElements()`](moduleSpanner.html#music21.spanner.Spanner.addSpannedElements "music21.spanner.Spanner.addSpannedElements") * [`fill()`](moduleSpanner.html#music21.spanner.Spanner.fill "music21.spanner.Spanner.fill") * [`getFirst()`](moduleSpanner.html#music21.spanner.Spanner.getFirst "music21.spanner.Spanner.getFirst") * [`getLast()`](moduleSpanner.html#music21.spanner.Spanner.getLast "music21.spanner.Spanner.getLast") | * [`getSpannedElementIds()`](moduleSpanner.html#music21.spanner.Spanner.getSpannedElementIds "music21.spanner.Spanner.getSpannedElementIds") * [`getSpannedElements()`](moduleSpanner.html#music21.spanner.Spanner.getSpannedElements "music21.spanner.Spanner.getSpannedElements") * [`getSpannedElementsByClass()`](moduleSpanner.html#music21.spanner.Spanner.getSpannedElementsByClass "music21.spanner.Spanner.getSpannedElementsByClass") * [`hasSpannedElement()`](moduleSpanner.html#music21.spanner.Spanner.hasSpannedElement "music21.spanner.Spanner.hasSpannedElement") * [`insertFirstSpannedElement()`](moduleSpanner.html#music21.spanner.Spanner.insertFirstSpannedElement "music21.spanner.Spanner.insertFirstSpannedElement") | * [`isFirst()`](moduleSpanner.html#music21.spanner.Spanner.isFirst "music21.spanner.Spanner.isFirst") * [`isLast()`](moduleSpanner.html#music21.spanner.Spanner.isLast "music21.spanner.Spanner.isLast") * [`purgeLocations()`](moduleSpanner.html#music21.spanner.Spanner.purgeLocations "music21.spanner.Spanner.purgeLocations") * [`purgeOrphans()`](moduleSpanner.html#music21.spanner.Spanner.purgeOrphans "music21.spanner.Spanner.purgeOrphans") * [`replaceSpannedElement()`](moduleSpanner.html#music21.spanner.Spanner.replaceSpannedElement "music21.spanner.Spanner.replaceSpannedElement") |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") | * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") | * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`TempoChangeSpanner`](#music21.tempo.TempoChangeSpanner "music21.tempo.TempoChangeSpanner") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## Functions

music21.tempo.interpolateElements(*element1*, *element2*, *sourceStream*, *destinationStream*, *autoAdd=True*)[[source]](../_modules/music21/tempo.html#interpolateElements)
:   Assume that element1 and element2 are two elements in sourceStream
    and destinationStream with other elements (say eA, eB, eC) between
    them. For instance, element1 could be the downbeat at offset 10
    in sourceStream (a Stream representing a score) and offset 20.5
    in destinationStream (which might be a Stream representing the
    timing of notes in particular recording at approximately but not
    exactly qtr = 30). Element2 could be the following downbeat in 4/4,
    at offset 14 in source but offset 25.0 in the recording:

    ```python
    >>> sourceStream = stream.Stream()
    >>> destinationStream = stream.Stream()
    >>> element1 = note.Note('C4', type='quarter')
    >>> element2 = note.Note('G4', type='quarter')
    >>> sourceStream.insert(10, element1)
    >>> destinationStream.insert(20.5, element1)
    >>> sourceStream.insert(14, element2)
    >>> destinationStream.insert(25.0, element2)
    ```

    Suppose eA, eB, and eC are three quarter notes that lie
    between element1 and element2 in sourceStream
    and destinationStream, as in:

    ```python
    >>> eA = note.Note('D4', type='quarter')
    >>> eB = note.Note('E4', type='quarter')
    >>> eC = note.Note('F4', type='quarter')
    >>> sourceStream.insert(11, eA)
    >>> sourceStream.insert(12, eB)
    >>> sourceStream.insert(13, eC)
    >>> destinationStream.append([eA, eB, eC])  # not needed if autoAdd were true
    ```

    then running this function will cause eA, eB, and eC
    to have offsets 21.625, 22.75, and 23.875 respectively
    in destinationStream:

    ```python
    >>> tempo.interpolateElements(element1, element2,
    ...         sourceStream, destinationStream, autoAdd=False)
    >>> for el in [eA, eB, eC]:
    ...    print(el.getOffsetBySite(destinationStream))
    21.625
    22.75
    23.875
    ```

    if the elements between element1 and element2 do not yet
    appear in destinationStream, they are automatically added
    unless autoAdd is False.

    (with the default autoAdd, elements are automatically added to new streams):

    ```python
    >>> destStream2 = stream.Stream()
    >>> destStream2.insert(10.1, element1)
    >>> destStream2.insert(50.5, element2)
    >>> tempo.interpolateElements(element1, element2, sourceStream, destStream2)
    >>> for el in [eA, eB, eC]:
    ...    offset = float(el.getOffsetBySite(destStream2))
    ...    print(f'{offset:.1f}')
    20.2
    30.3
    40.4
    ```

    (unless autoAdd is set to False, in which case a Tempo Exception arises:)

    ```python
    >>> destStream3 = stream.Stream()
    >>> destStream3.insert(100, element1)
    >>> destStream3.insert(500, element2)
    >>> eA.id = 'blah'
    >>> tempo.interpolateElements(element1, element2, sourceStream, destStream3, autoAdd=False)
    Traceback (most recent call last):
    music21.tempo.TempoException: Could not find element <music21.note.Note D> with id ...
    ```

music21.tempo.convertTempoByReferent(*numberSrc: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*, *quarterLengthBeatSrc: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*, *quarterLengthBeatDst=1.0*) → [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")[[source]](../_modules/music21/tempo.html#convertTempoByReferent)
:   Convert between equivalent tempi, where the speed stays the
    same but the beat referent and number change.

    60 bpm at quarter, going to half

    ```python
    >>> tempo.convertTempoByReferent(60, 1, 2)
    30.0
    ```

    60 bpm at quarter, going to 16th

    ```python
    >>> tempo.convertTempoByReferent(60, 1, 0.25)
    240.0
    ```

    60 at dotted quarter, get quarter

    ```python
    >>> tempo.convertTempoByReferent(60, 1.5, 1)
    90.0
    ```

    60 at dotted quarter, get half

    ```python
    >>> tempo.convertTempoByReferent(60, 1.5, 2)
    45.0
    ```

    60 at dotted quarter, get trip

    ```python
    >>> tempo.convertTempoByReferent(60, 1.5, 1/3)
    270.0
    ```

    A Fraction instance can also be used:

    ```python
    >>> tempo.convertTempoByReferent(60, 1.5, common.opFrac(1/3))
    270.0
    ```
