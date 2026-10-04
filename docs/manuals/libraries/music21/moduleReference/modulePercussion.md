Source: https://music21.org/music21docs/moduleReference/modulePercussion.html

# music21.percussion

This module contains classes for representing unpitched events such as percussion.
For backwards compatibility reasons, the module does not contain the actual
[`Unpitched`](moduleNote.html#music21.note.Unpitched "music21.note.Unpitched") which is in the note module.

## PercussionChord

class music21.percussion.PercussionChord(*notes: [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")] | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[ChordBase](moduleChord.html#music21.chord.ChordBase "music21.chord.ChordBase")] | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[NotRest](moduleNote.html#music21.note.NotRest "music21.note.NotRest")] | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] = None*, *\*\*keywords*)[[source]](../_modules/music21/percussion.html#PercussionChord)
:   A representation of one or (normally) more than one unpitched object sharing a stem
    and treated like a “chord.” It may also contain standard notes (pitches) for cases
    such as a percussionist playing a cymbal and marimba at the same time.

    It is a [`ChordBase`](moduleChord.html#music21.chord.ChordBase "music21.chord.ChordBase") and :class:`~music21.note.NotRest subclass
    that is NOT a [`Chord`](moduleChord.html#music21.chord.Chord "music21.chord.Chord") because one or more
    notes is an [`Unpitched`](moduleNote.html#music21.note.Unpitched "music21.note.Unpitched")
    object.

    ```python
    >>> vibraslapNote = note.Unpitched(displayName='D4', storedInstrument=instrument.Vibraslap())
    >>> pChord = percussion.PercussionChord([vibraslapNote, note.Note('E5')])
    >>> pChord
    <music21.percussion.PercussionChord [Vibraslap E5]>
    ```

    ```python
    >>> pChord.isChord
    False
    ```

    A PercussionChord has “notes,” just like anything deriving from ChordBase. Some of these
    are Unpitched objects.

    ```python
    >>> pChord.notes
    (<music21.note.Unpitched 'Vibraslap'>, <music21.note.Note E>)
    ```

    The same notes can also be assigned to another PercussionChord:

    ```python
    >>> pChord2 = percussion.PercussionChord()
    >>> pChord2.notes = pChord.notes
    >>> pChord2.notes
    (<music21.note.Unpitched 'Vibraslap'>, <music21.note.Note E>)
    ```

    Don’t attempt setting anything but Note or Unpitched objects as notes:

    ```python
    >>> pChord2.notes = [note.Rest()]
    Traceback (most recent call last):
    TypeError: every element of notes must be a note.Note or note.Unpitched object
    ```

    **Equality**

    Two PercussionChord objects are equal if their notes are equal *and in the same
    order* (this is different from Chord, but necessary because we cannot compare
    based just on pitch equality)

    ```python
    >>> pChord == pChord2
    True
    >>> pChord3 = percussion.PercussionChord([note.Unpitched('D4')])
    >>> pChord == pChord3
    False
    ```

[`PercussionChord`](#music21.percussion.PercussionChord "music21.percussion.PercussionChord") bases

* [`ChordBase`](moduleChord.html#music21.chord.ChordBase "music21.chord.ChordBase")
* [`NotRest`](moduleNote.html#music21.note.NotRest "music21.note.NotRest")
* [`GeneralNote`](moduleNote.html#music21.note.GeneralNote "music21.note.GeneralNote")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`PercussionChord`](#music21.percussion.PercussionChord "music21.percussion.PercussionChord") read-only properties

Read-only properties inherited from [`GeneralNote`](moduleNote.html#music21.note.GeneralNote "music21.note.GeneralNote"):

|  |  |  |
| --- | --- | --- |
| * [`fullName`](moduleNote.html#music21.note.GeneralNote.fullName "music21.note.GeneralNote.fullName") |  |  |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`PercussionChord`](#music21.percussion.PercussionChord "music21.percussion.PercussionChord") read/write properties

PercussionChord.notes

PercussionChord.pitches
:   Get or set a list or tuple of all Pitch objects in this PercussionChord.

    Unpitched members (that at most have only display pitches) are ignored.

    ```python
    >>> pChord = percussion.PercussionChord([note.Unpitched(displayName='D4'), note.Note('E5')])
    >>> pChord.pitches
    (<music21.pitch.Pitch E5>,)
    ```

    ```python
    >>> pChord.pitches = [60]
    >>> pChord.pitches
    (<music21.pitch.Pitch C4>,)
    ```

    Notice that setting pitches has now just cleared any existing notes, pitched or unpitched:

    ```python
    >>> pChord.notes
    (<music21.note.Note C>,)
    ```

Read/write properties inherited from [`ChordBase`](moduleChord.html#music21.chord.ChordBase "music21.chord.ChordBase"):

|  |  |  |
| --- | --- | --- |
| * [`tie`](moduleChord.html#music21.chord.ChordBase.tie "music21.chord.ChordBase.tie") | * [`volume`](moduleChord.html#music21.chord.ChordBase.volume "music21.chord.ChordBase.volume") |  |

Read/write properties inherited from [`NotRest`](moduleNote.html#music21.note.NotRest "music21.note.NotRest"):

|  |  |  |
| --- | --- | --- |
| * [`notehead`](moduleNote.html#music21.note.NotRest.notehead "music21.note.NotRest.notehead") * [`noteheadFill`](moduleNote.html#music21.note.NotRest.noteheadFill "music21.note.NotRest.noteheadFill") | * [`noteheadParenthesis`](moduleNote.html#music21.note.NotRest.noteheadParenthesis "music21.note.NotRest.noteheadParenthesis") * [`stemDirection`](moduleNote.html#music21.note.NotRest.stemDirection "music21.note.NotRest.stemDirection") | * [`storedInstrument`](moduleNote.html#music21.note.NotRest.storedInstrument "music21.note.NotRest.storedInstrument") |

Read/write properties inherited from [`GeneralNote`](moduleNote.html#music21.note.GeneralNote "music21.note.GeneralNote"):

|  |  |  |
| --- | --- | --- |
| * [`lyric`](moduleNote.html#music21.note.GeneralNote.lyric "music21.note.GeneralNote.lyric") |  |  |

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`PercussionChord`](#music21.percussion.PercussionChord "music21.percussion.PercussionChord") methods

PercussionChord.\_\_eq\_\_(*other*)[[source]](../_modules/music21/percussion.html#PercussionChord.__eq__)
:   Returns True if all the notes are equal and in the same order.

Methods inherited from [`ChordBase`](moduleChord.html#music21.chord.ChordBase "music21.chord.ChordBase"):

|  |  |  |
| --- | --- | --- |
| * [`add()`](moduleChord.html#music21.chord.ChordBase.add "music21.chord.ChordBase.add") * [`hasComponentVolumes()`](moduleChord.html#music21.chord.ChordBase.hasComponentVolumes "music21.chord.ChordBase.hasComponentVolumes") | * [`remove()`](moduleChord.html#music21.chord.ChordBase.remove "music21.chord.ChordBase.remove") | * [`setVolumes()`](moduleChord.html#music21.chord.ChordBase.setVolumes "music21.chord.ChordBase.setVolumes") |

Methods inherited from [`NotRest`](moduleNote.html#music21.note.NotRest "music21.note.NotRest"):

|  |  |  |
| --- | --- | --- |
| * [`getInstrument()`](moduleNote.html#music21.note.NotRest.getInstrument "music21.note.NotRest.getInstrument") | * [`hasVolumeInformation()`](moduleNote.html#music21.note.NotRest.hasVolumeInformation "music21.note.NotRest.hasVolumeInformation") |  |

Methods inherited from [`GeneralNote`](moduleNote.html#music21.note.GeneralNote "music21.note.GeneralNote"):

|  |  |  |
| --- | --- | --- |
| * [`addLyric()`](moduleNote.html#music21.note.GeneralNote.addLyric "music21.note.GeneralNote.addLyric") * [`augmentOrDiminish()`](moduleNote.html#music21.note.GeneralNote.augmentOrDiminish "music21.note.GeneralNote.augmentOrDiminish") | * [`getGrace()`](moduleNote.html#music21.note.GeneralNote.getGrace "music21.note.GeneralNote.getGrace") | * [`insertLyric()`](moduleNote.html#music21.note.GeneralNote.insertLyric "music21.note.GeneralNote.insertLyric") |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`PercussionChord`](#music21.percussion.PercussionChord "music21.percussion.PercussionChord") instance variables

Instance variables inherited from [`ChordBase`](moduleChord.html#music21.chord.ChordBase "music21.chord.ChordBase"):

|  |  |  |
| --- | --- | --- |
| * [`beams`](moduleChord.html#music21.chord.ChordBase.beams "music21.chord.ChordBase.beams") | * [`isNote`](moduleChord.html#music21.chord.ChordBase.isNote "music21.chord.ChordBase.isNote") | * [`isRest`](moduleChord.html#music21.chord.ChordBase.isRest "music21.chord.ChordBase.isRest") |

Instance variables inherited from [`NotRest`](moduleNote.html#music21.note.NotRest "music21.note.NotRest"):

|  |  |  |
| --- | --- | --- |
| * [`beams`](moduleNote.html#music21.note.NotRest.beams "music21.note.NotRest.beams") |  |  |

Instance variables inherited from [`GeneralNote`](moduleNote.html#music21.note.GeneralNote "music21.note.GeneralNote"):

|  |  |  |
| --- | --- | --- |
| * [`articulations`](moduleNote.html#music21.note.GeneralNote.articulations "music21.note.GeneralNote.articulations") * [`expressions`](moduleNote.html#music21.note.GeneralNote.expressions "music21.note.GeneralNote.expressions") | * [`isChord`](moduleNote.html#music21.note.GeneralNote.isChord "music21.note.GeneralNote.isChord") | * [`lyrics`](moduleNote.html#music21.note.GeneralNote.lyrics "music21.note.GeneralNote.lyrics") |

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |
