Source: https://music21.org/music21docs/moduleReference/moduleEditorial.html

# music21.editorial

Editorial objects store comments and other metadata associated with specific
[`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object") elements such as Notes.

Some aspects of [`Editorial`](#music21.editorial.Editorial "music21.editorial.Editorial") objects
represent very early (pre-v0.1) versions of music21. Thus, some
pre-defined aspects might be removed from documentation in the future.

Access an editorial object by calling .editorial on any music21 object:

```python
>>> c = clef.TrebleClef()
>>> ed = c.editorial
>>> ed
<music21.editorial.Editorial {}>
```

The object is lazily created on first access.
To see if there is any existing editorial information without creating
the object, call .hasEditorialInformation

```python
>>> n = note.Note('C#4')
>>> n.hasEditorialInformation
False
```

```python
>>> n.editorial.unedited = True
>>> n.hasEditorialInformation
True
```

## Editorial

class music21.editorial.Editorial[[source]](../_modules/music21/editorial.html#Editorial)
:   Editorial comments and special effects that can be applied to music21 objects.

    ```python
    >>> ed1 = editorial.Editorial()
    >>> ed1.backgroundHighlight = 'yellow'  # non-standard.
    >>> ed1.backgroundHighlight
    'yellow'
    >>> list(ed1.keys())
    ['backgroundHighlight']
    >>> ed1
     <music21.editorial.Editorial {'backgroundHighlight': 'yellow'}>
    ```

    Every GeneralNote object already has a NoteEditorial object attached to it
    at object.editorial. Normally you will just change that object instead.

    For instance, take the case where a scribe wrote F in the score, knowing
    that a good singer would automatically sing F-sharp instead. We can store
    the editorial suggestion to sing F-sharp as a “musica ficta” accidental
    object:

    ```python
    >>> fictaSharp = pitch.Accidental('sharp')
    >>> n = note.Note('F')
    >>> n.editorial.ficta = fictaSharp
    >>> n.show('lily.png')  # only Lilypond currently supports musica ficta
    ```

    [![../_images/noteEditorialFictaSharp.png](../_images/noteEditorialFictaSharp.png)](../_images/noteEditorialFictaSharp.png)

[`Editorial`](#music21.editorial.Editorial "music21.editorial.Editorial") bases

* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`Editorial`](#music21.editorial.Editorial "music21.editorial.Editorial") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`Editorial`](#music21.editorial.Editorial "music21.editorial.Editorial") instance variables

Editorial.comments
:   a list of [`Comment`](#music21.editorial.Comment "music21.editorial.Comment") objects that represent any comments
    about the object.

Editorial.ficta
:   a [`Accidental`](modulePitch.html#music21.pitch.Accidental "music21.pitch.Accidental") object that specifies musica
    ficta for the note. Will only be displayed in LilyPond and then only if
    there is no Accidental object on the note itself

Editorial.footnotes
:   a list of [`Comment`](#music21.editorial.Comment "music21.editorial.Comment") objects that represent annotations
    for the object. These have specific meanings in MusicXML.

Editorial.harmonicInterval
:   an [`Interval`](moduleInterval.html#music21.interval.Interval "music21.interval.Interval") object that specifies
    the harmonic interval between this object and a single other object, or None
    (useful for storing information post analysis)

Editorial.melodicInterval
:   an [`Interval`](moduleInterval.html#music21.interval.Interval "music21.interval.Interval") object that specifies
    the melodic interval to the next object in this Part/Voice/Stream, etc.

## Comment

class music21.editorial.Comment(*text=None*)[[source]](../_modules/music21/editorial.html#Comment)
:   A comment or footnote or something else attached to a note.

    ```python
    >>> c = editorial.Comment('presented as C natural in the 1660 print.')
    >>> c
    <music21.editorial.Comment 'presented as C na...'>
    ```

    Note that the text is truncated in representation, but it is all there in .text:

    ```python
    >>> c.text
    'presented as C natural in the 1660 print.'
    ```

    ```python
    >>> c.isFootnote = True
    >>> c.levelInformation = 'musicological'
    ```

    ```python
    >>> n = note.Note('C#4')
    >>> n.editorial.footnotes.append(c)
    >>> n.editorial.footnotes[0]
    <music21.editorial.Comment 'presented as C na...'>
    ```

    Comments have style information:

    ```python
    >>> c.style.color = 'red'
    >>> c.style.color
    'red'
    ```

[`Comment`](#music21.editorial.Comment "music21.editorial.Comment") bases

* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")
* [`StyleMixin`](moduleStyle.html#music21.style.StyleMixin "music21.style.StyleMixin")
* [`SlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.SlottedObjectMixin "music21.common.objects.SlottedObjectMixin")

[`Comment`](#music21.editorial.Comment "music21.editorial.Comment") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

Read-only properties inherited from [`StyleMixin`](moduleStyle.html#music21.style.StyleMixin "music21.style.StyleMixin"):

|  |  |  |
| --- | --- | --- |
| * [`hasEditorialInformation`](moduleStyle.html#music21.style.StyleMixin.hasEditorialInformation "music21.style.StyleMixin.hasEditorialInformation") | * [`hasStyleInformation`](moduleStyle.html#music21.style.StyleMixin.hasStyleInformation "music21.style.StyleMixin.hasStyleInformation") |  |

[`Comment`](#music21.editorial.Comment "music21.editorial.Comment") read/write properties

Read/write properties inherited from [`StyleMixin`](moduleStyle.html#music21.style.StyleMixin "music21.style.StyleMixin"):

|  |  |  |
| --- | --- | --- |
| * [`editorial`](moduleStyle.html#music21.style.StyleMixin.editorial "music21.style.StyleMixin.editorial") | * [`style`](moduleStyle.html#music21.style.StyleMixin.style "music21.style.StyleMixin.style") |  |
