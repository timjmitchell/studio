Source: https://music21.org/music21docs/moduleReference/moduleMetadata.html

# music21.metadata

Classes and functions for creating and processing metadata associated with
scores, works, and fragments, such as titles, movements, authors, publishers,
and regions.

The [`Metadata`](#music21.metadata.Metadata "music21.metadata.Metadata") object is the main public interface to
metadata components. A Metadata object can be added to a Stream and used to set
common score attributes, such as title and composer. A Metadata object found at
offset zero can be accessed through a Stream’s
`metadata` property.

The following example creates a `Stream` object, adds a
[`Note`](moduleNote.html#music21.note.Note "music21.note.Note") object, and configures and adds the
[`title`](#music21.metadata.Metadata.title "music21.metadata.Metadata.title") and
[`composer`](#music21.metadata.Metadata.composer "music21.metadata.Metadata.composer") properties of a Metadata object.

```python
>>> s = stream.Score()
>>> p = stream.Part()
>>> m = stream.Measure()
>>> m.append(note.Note())
>>> p.append(m)
>>> s.append(p)
>>> s.insert(0, metadata.Metadata())
>>> s.metadata.title = 'title'
>>> s.metadata.composer = 'composer'
>>> s.show()
```

[![../_images/moduleMetadata-01.png](../_images/moduleMetadata-01.png)](../_images/moduleMetadata-01.png)

A guide to the v8+ Dublin Core implementation:

The class Metadata has been completely rewritten in music21 v8 to support
significant new functionality.

The previous Metadata implementation had a list of supported workIds, and also
a list of standard contributor roles. More than one of each contributor role
could exist, but only one of each workId. And while there was some support for
custom contributor roles, there was no support for other custom metadata, only
the specified list of workIds.

In the v8 implementation, contributor roles are treated the same as other
non-contributor metadata. Music21 includes a list of supported property terms,
which are pulled from Dublin Core (namespace = ‘dcterms’), MARC Relator codes
(namespace = ‘marcrel’), and Humdrum (namespace = ‘humdrum’). Each property
term is assigned a unique name (e.g. ‘composer’, ‘alternativeTitle’, etc.).

Each metadata property can be specified by ‘uniqueName’ or by ‘namespace:name’.
For example: md[‘composer’] and md[‘marcrel:CMP’] are equivalent, as are
md[‘alternativeTitle’] and md[‘dcterms:alternative’]. There can be more than
one of any such item (not just contributors). And you can also have metadata
items with custom names.

For simple metadata items, like a single title, there is an easy way to get/set
them: use an attribute-style get operation (e.g. t = md.title). This will always
return a single string. If there is more than one item of that name, a summary
string will be returned. To see the full list of metadata items in their native
value type, use a dictionary-style get operation (e.g. titles = md[‘title’]).
If an item or list of items is set (whether attribute-style or dictionary-style),
any existing items of that name are deleted. To add an item or list of items
without deleting existing items, use the md.add() API. See the examples below:

Set a title (overwrites any existing titles):

```python
>>> md = metadata.Metadata()
>>> md.title = 'A Title'
>>> md.title
'A Title'
>>> md['title']
(<music21.metadata.primitives.Text A Title>,)
```

Set two titles (overwrites any existing titles):

```python
>>> md['title'] = ['The Title', 'A Second Title']
>>> md['title']
(<music21.metadata.primitives.Text The Title>,
<music21.metadata.primitives.Text A Second Title>)
>>> md.title
'The Title, A Second Title'
```

Add a third title (leaves any existing titles in place):

```python
>>> md.add('title', 'Third Title, A')
>>> md['title']
(<music21.metadata.primitives.Text The Title>,
<music21.metadata.primitives.Text A Second Title>,
<music21.metadata.primitives.Text Third Title, A>)
>>> md.title
'The Title, A Second Title, A Third Title'
```

You can also set/add/get free-form custom metadata items:

```python
>>> md.setCustom('modification description', 'added missing sharp in measure 27')
>>> md.getCustom('modification description')
(<music21.metadata.primitives.Text added missing sharp in measure 27>,)
```

Adding another custom element for the same description creates a second
entry.

```python
>>> md.addCustom('modification description', 'deleted redundant natural in measure 28')
>>> md.getCustom('modification description')
(<music21.metadata.primitives.Text added missing sharp in measure 27>,
 <music21.metadata.primitives.Text deleted redundant natural in measure 28>)
```

Metadata does not explicitly support client-specified namespaces, but by using
getCustom/addCustom/setCustom, clients can set anything they want. For instance, to
embed the old SoundTracker .MOD format’s sample name, a .MOD file parser could use
md.addCustom(‘soundtracker:SampleName’, ‘Bassoon’), and a .MOD file writer that
understood ‘soundtracker:’ metadata could then write it back accurately to one of
those files. Custom metadata (whether namespaced this way, or free form) can also
be written to various other file formats without interpretation, as long as there
is a place for it (e.g. in the ‘<miscellaneous>’ tag in MusicXML).

In music21 v8, primitives.Text has been updated to add isTranslated to keep track of
whether the text has been translated,
as well as an encoding scheme, that specifies which standard should be used to parse
the string. See metadata/primitives.py for more information.

## Metadata

class music21.metadata.Metadata(*\*\*keywords*)[[source]](../_modules/music21/metadata.html#Metadata)
:   Metadata objects contain information about a work, including title, composer,
    dates, and other relevant information. Metadata objects can also cover a fragment
    of a Score such as individual parts or a range of measures.

    Metadata is a [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object") subclass, meaning that it
    can be positioned on a Stream by offset and have a
    [`Duration`](moduleDuration.html#music21.duration.Duration "music21.duration.Duration").

    In many cases, each Stream will have a single Metadata object at the zero-offset
    position.

    To get a simple string, use attribute-style access by unique name.
    Some workIds from music21 v7 have been renamed (e.g. ‘date’ has been renamed
    to ‘dateCreated’). The old music21 v7 name in these cases is still supported
    when you use attribute-style access.

    ```python
    >>> md = metadata.Metadata(title='Concerto in F')
    >>> md.title
    'Concerto in F'
    ```

    Attribute access also works with three-letter workId abbreviations (these are
    grandfathered in from music21 v7; abbreviations have not been added for
    new-in-v8 metadata items):

    ```python
    >>> md = metadata.Metadata(otl='Concerto in F')
    >>> md.otl
    'Concerto in F'
    >>> md.title
    'Concerto in F'
    ```

    It is also possible to set a list/tuple of values or get a tuple full of
    (richer-typed) values using dictionary-style access.

    ```python
    >>> md = metadata.Metadata()
    >>> md['composer'] = ['Billy Strayhorn', 'Duke Ellington']
    >>> md['composer']
    (<music21.metadata.primitives.Contributor composer:Billy Strayhorn>,
     <music21.metadata.primitives.Contributor composer:Duke Ellington>)
    >>> md.composer
    'Billy Strayhorn and Duke Ellington'
    >>> md.contributors
    (<music21.metadata.primitives.Contributor composer:Billy Strayhorn>,
     <music21.metadata.primitives.Contributor composer:Duke Ellington>)
    ```

    Here is the list of grandfathered v7 synonyms, which may disappear in a
    future version:

    ```python
    >>> sorted(metadata.properties.ALL_MUSIC21_WORK_IDS)
    ['commission', 'date', 'dedication', 'volume']
    ```

    And here are their new v8 standard unique names:

    ```python
    >>> sorted(metadata.properties.MUSIC21_WORK_ID_TO_UNIQUE_NAME.values())
    ['commissionedBy', 'dateCreated', 'dedicatedTo', 'volumeNumber']
    ```

[`Metadata`](#music21.metadata.Metadata "music21.metadata.Metadata") bases

* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`Metadata`](#music21.metadata.Metadata "music21.metadata.Metadata") read-only properties

Metadata.bestTitle
:   Get the title of the work, or the next-matched title string
    available from a related parameter fields.

    ```python
    >>> md = metadata.Metadata(title='Third Symphony')
    >>> md.bestTitle
    'Third Symphony'
    ```

    ```python
    >>> md = metadata.Metadata(popularTitle='Eroica')
    >>> md.bestTitle
    'Eroica'
    ```

    ```python
    >>> md = metadata.Metadata(
    ...     title='Third Symphony',
    ...     popularTitle='Eroica',
    ...     )
    >>> md.bestTitle
    'Third Symphony'
    ```

    ```python
    >>> md.popularTitle
    'Eroica'
    ```

    ```python
    >>> md.otp
    'Eroica'
    ```

    bestTitle cannot be set:

    ```python
    >>> md.bestTitle = 'Bonaparte'
    Traceback (most recent call last):
    AttributeError: property 'bestTitle' of 'Metadata' object has no setter
    ```

Metadata.contributors
:   Returns a tuple of all the Contributors found in the metadata.
    Returns an empty tuple if no Contributors exist.

    ```python
    >>> md = metadata.Metadata()
    >>> md.composer = 'Richard Strauss'
    >>> md.librettist = 'Oscar Wilde'
    ```

    When we add something that is not a person, such as a title
    (whether through .attribute setting, [item] setting,
    or the [`add()`](#music21.metadata.Metadata.add "music21.metadata.Metadata.add") method), it will not show up
    in the list of contributors.

    ```python
    >>> md.add('title', 'Salome')
    >>> contribs = md.contributors
    >>> contribs
    (<music21.metadata.primitives.Contributor composer:Richard Strauss>,
     <music21.metadata.primitives.Contributor librettist:Oscar Wilde>)
    ```

    Note that .contributors cannot be set. Add them separately via
    specific setters or the .addContributor() method.

Metadata.software
:   Returns a tuple of software names/versions.

    Returns an empty tuple if no software names/versions exist,
    but this is rare, since music21 adds its own version when
    initializing a Metadata object.

    ```python
    >>> md = metadata.Metadata()
    >>> md.software
    ('music21 v...',)
    >>> md.add('software', 'Finale for Macintosh')
    >>> md.software
    ('music21 v...',
     'Finale for Macintosh')
    >>> md['software']
    (<music21.metadata.primitives.Text music21 v...>,
     <music21.metadata.primitives.Text Finale for Macintosh>)
    ```

    Note that .software is an exception to the general rule that
    singular looking properties return a string. In fact, it is always
    plural and returns a tuple of strings. There is no singular version

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`Metadata`](#music21.metadata.Metadata "music21.metadata.Metadata") read/write properties

Metadata.alternativeTitle
:   Get or set the alternative title.

    ```python
    >>> md = metadata.Metadata(popularTitle='Eroica')
    >>> md.alternativeTitle = 'Heroic Symphony'
    >>> md.alternativeTitle
    'Heroic Symphony'
    ```

Metadata.composer
:   Get or set the composer of this work. Only the first composer can be
    got or set via properties.

    The composer attribute does not live in Metadata, but creates a
    `Contributor` object in the .contributors
    object.

    ```python
    >>> md = metadata.Metadata(
    ...     title='...(Iphigenia)',
    ...     )
    >>> md.composer = 'Shorter, Wayne'
    ```

    You can set multiple composers by setting them dictionary-style
    or by using md.add.
    >>> md.add(‘composer’, ‘Spalding, Esperanza’)

    The Metadata.composer attribute returns a summary string if there is
    more than one composer.

    ```python
    >>> md.composer
    'Shorter, Wayne and Spalding, Esperanza'
    ```

Metadata.composers
:   Get a tuple or set an iterable of strings of all composer roles.

    ```python
    >>> md = metadata.Metadata(title='Yellow River Concerto')
    >>> md.composers = ['Xian Xinghai', 'Yin Chengzong']
    ```

    (Yin Chengzong might be better called “Arranger” but this is for
    illustrative purposes)

    ```python
    >>> md.composers
    ('Xian Xinghai', 'Yin Chengzong')
    ```

    Might as well add a third composer to the concerto committee?

    ```python
    >>> contrib3 = metadata.Contributor(role='composer', name='Chu Wanghua')
    >>> md.add('composer', contrib3)
    >>> md.composers
    ('Xian Xinghai', 'Yin Chengzong', 'Chu Wanghua')
    ```

    If there are no composers, returns an empty list:

    ```python
    >>> md = metadata.Metadata(title='Sentient Algorithmic Composition')
    >>> md.composers
    ()
    ```

Metadata.copyright
:   Returns the copyright as a str.
    Returns None if no copyright exists in the metadata.
    Returns all the copyright values in one string (with ‘, ‘ between them)
    if multiple copyrights exist in the metadata. Use md[‘copyright’] to
    get all the copyrights as Copyright objects.

    ```python
    >>> md = metadata.Metadata()
    >>> md.copyright is None
    True
    >>> md.copyright = 'Copyright © 1896, Éditions Durand (expired)'
    >>> md.copyright
    'Copyright © 1896, Éditions Durand (expired)'
    ```

    Using dictionary-style access, you can use either the uniqueName (‘copyright’)
    or the namespaceName (‘dcterms:rights’). Here you can see how multiple
    copyrights are handled.

    ```python
    >>> md.copyright = 'Copyright © 1984 All Rights Reserved'
    >>> md.copyright
    'Copyright © 1984 All Rights Reserved'
    ```

    To add another copyright to the list, call md.add().

    ```python
    >>> md.add('copyright', 'Lyrics copyright © 1987 All Rights Reserved')
    ```

    md.copyright will now return both copyrights in one string

    ```python
    >>> md.copyright
    'Copyright © 1984 All Rights Reserved, Lyrics copyright © 1987 All Rights Reserved'
    ```

    md[‘copyright’] will return a tuple containing both Copyright objects.

    ```python
    >>> md['copyright']
    (<music21.metadata.primitives.Copyright Copyright © 1984 All Rights Reserved>,
     <music21.metadata.primitives.Copyright Lyrics copyright © 1987 All Rights Reserved>)
    ```

    You can set str, Text, or Copyright values, and they will be converted to
    Copyright automatically if necessary. Note that ‘dcterms:rights’
    is Dublin Core terminology for ‘copyright’, and can be used interchangeably
    with ‘copyright’ as a metadata dictionary-style key.

    ```python
    >>> md.copyright = metadata.Text('Copyright © 1984')
    >>> md['copyright']
    (<music21.metadata.primitives.Copyright Copyright © 1984>,)
    >>> md.copyright = metadata.Copyright('Copyright © 1985', role='something')
    >>> md['dcterms:rights']
    (<music21.metadata.primitives.Copyright Copyright © 1985>,)
    ```

Metadata.corpusFilePath
:   Get or set the path within the corpus that was parsed.

Metadata.dateCreated
:   Get or set the creation date of this work as one of the following date
    objects:

    `DateSingle`,
    `DateRelative`,
    `DateBetween`,
    `DateSelection`,

    ```python
    >>> md = metadata.Metadata(
    ...     title='Third Symphony',
    ...     popularTitle='Eroica',
    ...     composer='Beethoven, Ludwig van',
    ...     )
    >>> md.dateCreated = '1805'
    >>> md.dateCreated
    '1805/--/--'
    ```

    ```python
    >>> md.dateCreated = metadata.DateBetween(['1803/01/01', '1805/04/07'])
    >>> md.dateCreated
    '1803/01/01 to 1805/04/07'
    ```

Metadata.fileFormat
:   Get or set the file format that was parsed.

Metadata.fileNumber
:   Get or set the file number that was parsed.

Metadata.filePath
:   Get or set the file path that was parsed. This returns a string, not a Path object
    that is deliberate for caching.

Metadata.librettist
:   Gets or sets a single librettist for this work:

    ```python
    >>> md = metadata.Metadata(title='Death of Klinghoffer, The')
    >>> md.librettist = 'Goodman, Alice'
    >>> md.librettist
    'Goodman, Alice'
    ```

    To preserve continuity with Humdrum, library catalogues, etc.,
    librettists should be distinguished from lyricists etc., but sometimes
    the line is not 100% clear.

Metadata.librettists
:   Gets a tuple or sets an iterable of librettists for this work:

    ```python
    >>> md = metadata.Metadata(title='Madama Butterfly')
    >>> md.librettists = ['Illica, Luigi', 'Giacosa, Giuseppe']
    >>> md.librettists
    ('Illica, Luigi', 'Giacosa, Giuseppe')
    ```

    Should be distinguished from lyricists etc.

Metadata.localeOfComposition
:   Get or set the locale of composition, or origin, of the work.

    ```python
    >>> md = metadata.Metadata(popularTitle='Eroica')
    >>> md.localeOfComposition = 'Paris, France'
    >>> md.localeOfComposition
    'Paris, France'
    ```

Metadata.lyricist
:   Gets or sets a single lyricist for this work:

    ```python
    >>> md = metadata.Metadata(title='Girlfriend')
    >>> md.lyricist = 'Keys, Alicia'
    ```

    To preserve continuity with Humdrum, library catalogues, etc.,
    lyricists should be distinguished from librettists etc., but sometimes
    the line is not 100% clear:

    ```python
    >>> md = metadata.Metadata(title='West Side Story')
    >>> md.lyricist = 'Sondheim, Stephen'
    >>> md.lyricist
    'Sondheim, Stephen'
    ```

Metadata.lyricists
:   Gets a tuple or sets an iterable of lyricists for this work:

    ```python
    >>> md = metadata.Metadata(title='Rumors')
    >>> md.lyricists = ['Buckingham, Lindsey', 'McVie, Christine', 'Nicks, Stevie']
    >>> md.lyricists
    ('Buckingham, Lindsey', 'McVie, Christine', 'Nicks, Stevie')
    ```

    Should be distinguished from librettists etc.

Metadata.movementName
:   Get or set the movement title.

    ```python
    >>> md = metadata.Metadata()
    >>> md.movementName = 'Vivace'
    >>> md.movementName
    'Vivace'
    ```

    Note that a number of pieces from various MusicXML datasets have
    the piece title as the movement title. For instance, the Bach
    Chorales, since they are technically movements of larger cantatas.

Metadata.movementNumber
:   Get or set the movement number as a string (or None)

    ```python
    >>> md = metadata.Metadata(title='Ode to Joy')
    >>> md.movementNumber = 4
    ```

    Note that movement numbers are always returned as strings! This may
    change in the future.

    ```python
    >>> md.movementNumber
    '4'
    ```

Metadata.number
:   Get or set the number of the work within a collection of pieces,
    as a string. (for instance, the number within a collection of ABC files)

    ```python
    >>> md = metadata.Metadata()
    >>> md.number = '4'
    ```

    Note that numbers are always returned as strings! This may
    change in the future.

    ```python
    >>> md.number
    '4'
    ```

    However, it is acceptable to set it as an int:

    ```python
    >>> md.number = 2
    >>> md.number
    '2'
    ```

Metadata.opusNumber
:   Get or set the opus number.

    ```python
    >>> md = metadata.Metadata()
    >>> md.opusNumber = 56
    ```

    Note that opusNumbers are always returned as strings! This may
    change in the future, however, it is less likely to change
    than .number or .movementNumber since Opus numbers such as
    18a are common.

    ```python
    >>> md.opusNumber
    '56'
    ```

    There is no enforcement that only numbers actually called “opus”
    are used, and it could be used for other catalogue numbers.

    ```python
    >>> md.opusNumber = 'K.622'
    ```

Metadata.title
:   Get the title of the work.

    ```python
    >>> md = metadata.Metadata(title='Third Symphony')
    >>> md.title
    'Third Symphony'
    ```

    ```python
    >>> md = metadata.Metadata(popularTitle='Eroica')
    >>> md.title is None
    True
    ```

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`Metadata`](#music21.metadata.Metadata "music21.metadata.Metadata") methods

Metadata.\_\_getitem\_\_(*key: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")['movementName', 'movementNumber', 'title']*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[Text](moduleMetadataPrimitives.html#music21.metadata.primitives.Text "music21.metadata.primitives.Text"), ...][[source]](../_modules/music21/metadata.html#Metadata.__getitem__)

Metadata.\_\_getitem\_\_(*key: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")['copyright']*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[Copyright](moduleMetadataPrimitives.html#music21.metadata.primitives.Copyright "music21.metadata.primitives.Copyright"), ...]

Metadata.\_\_getitem\_\_(*key: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[Text](moduleMetadataPrimitives.html#music21.metadata.primitives.Text "music21.metadata.primitives.Text"), ...]
:   “Dictionary key” access for all standard uniqueNames and
    standard keys of the form ‘namespace:name’.

    These always return tuple[ValueType, …], which may be empty.

    If key is not a standard uniqueName or standard ‘namespace:name’,
    then KeyError is raised.

    ```python
    >>> md = metadata.Metadata()
    >>> md['average duration']
    Traceback (most recent call last):
    KeyError: "Name='average duration' is not a standard metadata name...
    ```

    Example: setting, then getting (dictionary style) a single value. Note that
    it must be set as a single element list/tuple, and is always returned as a
    single element tuple.

    ```python
    >>> md['description'] = [
    ...     metadata.Text('For the coronation of Catherine the Great.', language='en')
    ... ]
    >>> descs = md['description']
    >>> descs
    (<music21.metadata.primitives.Text For the coronation of Catherine the Great.>,)
    ```

    A second description can also be added.

    ```python
    >>> md.add('description', 'In five sections, unique for its time.')
    >>> descs = md['description']
    >>> isinstance(descs, tuple)
    True
    >>> len(descs)
    2
    >>> descs
    (<music21.metadata.primitives.Text For the coronation of Catherine the Great.>,
     <music21.metadata.primitives.Text In five sections, unique for its time.>)
    >>> descs[0].language
    'en'
    >>> descs[1].language is None
    True
    ```

Metadata.add(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *value: [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)") | [Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "(in Python v3.14)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")]*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/metadata.html#Metadata.add)
:   Adds a single item or multiple items with this name, leaving any existing
    items with this name in place.

    The name can be the item’s uniqueName or ‘namespace:name’. If it is
    not the uniqueName or namespaceName of one of the standard metadata
    properties, KeyError will be raised.

    ```python
    >>> md = metadata.Metadata()
    >>> md.add('average duration', '180 minutes')
    Traceback (most recent call last):
    KeyError: "Name='average duration' is not a standard metadata name...
    ```

    Example of adding a composer and two titles:

    ```python
    >>> md.add('composer', 'Houcine Slaoui')
    >>> md['composer']
    (<music21.metadata.primitives.Contributor composer:Houcine Slaoui>,)
    ```

    ```python
    >>> md.add('title', metadata.Text('الماريكان', language='ar'))
    >>> md.add('title', metadata.Text('The Americans',  language='en'))
    >>> titles = md['title']
    >>> titles
    (<music21.metadata.primitives.Text الماريكان>,
     <music21.metadata.primitives.Text The Americans>)
    >>> titles[0].language
    'ar'
    >>> titles[1].language
    'en'
    ```

    If you do in fact want to overwrite any existing items with this name,
    you can use dictionary-style or attribute-style setting instead.
    See `__setitem__()` and
    `__setattr__()` for details.

Metadata.addContributor(*c: [Contributor](moduleMetadataPrimitives.html#music21.metadata.primitives.Contributor "music21.metadata.primitives.Contributor")*)[[source]](../_modules/music21/metadata.html#Metadata.addContributor)
:   Assign a `Contributor` object to this
    Metadata.

    ```python
    >>> md = metadata.Metadata(title='Gaelic Symphony')
    >>> c = metadata.Contributor()
    >>> c.name = 'Beach, Amy'
    >>> c.role = 'composer'
    >>> md.addContributor(c)
    >>> md.composer
    'Beach, Amy'
    ```

    Add maiden name as an alternative composer name:

    ```python
    >>> c_alt = metadata.Contributor()
    >>> c_alt.name = 'Cheney, Amy Marcy'
    >>> c_alt.role = 'composer'
    >>> md.addContributor(c_alt)
    >>> md.composers
    ('Beach, Amy', 'Cheney, Amy Marcy')
    ```

    ```python
    >>> md.search('Beach')
    (True, 'composer')
    >>> md.search('Cheney')
    (True, 'composer')
    ```

    Note that in this case, a “composerAlias” would probably be a more
    appropriate role than a second composer.

    All contributor roles are searchable, even if they are not standard roles:

    ```python
    >>> dancer = metadata.Contributor()
    >>> dancer.names = ['Merce Cunningham', 'Martha Graham']
    >>> dancer.role = 'interpretive dancer'
    >>> md.addContributor(dancer)
    >>> md.search('Cunningham')
    (True, 'interpretive dancer')
    ```

Metadata.addCustom(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *value: [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)") | [Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "(in Python v3.14)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")]*)[[source]](../_modules/music21/metadata.html#Metadata.addCustom)
:   Adds any custom-named metadata items. The name can be free-form,
    or it can be a custom ‘namespace:name’.

    addCustom takes a single object of any type, or a list/tuple of
    objects of any type. The object(s) will be converted to Text.

    ```python
    >>> md = metadata.Metadata()
    >>> md.addCustom('measure with 2nd ending', 'measure 128')
    >>> md.getCustom('measure with 2nd ending')
    (<music21.metadata.primitives.Text measure 128>,)
    ```

    An item list can also be added.

    ```python
    >>> md.addCustom('measure with 2nd ending', ['measure 192', 'measure 256'])
    >>> measures = md.getCustom('measure with 2nd ending')
    ```

    ```python
    >>> isinstance(measures, tuple)
    True
    >>> len(measures)
    3
    >>> measures
    (<music21.metadata.primitives.Text measure 128>,
     <music21.metadata.primitives.Text measure 192>,
     <music21.metadata.primitives.Text measure 256>)
    ```

Metadata.all(*\**, *skipContributors: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *skipNonContributors: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *returnPrimitives: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *returnSorted: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")], ...][[source]](../_modules/music21/metadata.html#Metadata.all)
:   Returns the values stored in this metadata as a Tuple of (uniqueName, value) pairs.
    There are four bool options. The three that are new in v8 (skipNonContributors,
    returnPrimitives, returnSorted) are defaulted to behave like v7.

    If skipContributors is True, only non-contributor metadata will be returned. If
    skipNonContributors is True, only contributor metadata will be returned. If both
    of these are True, the returned Tuple will be empty. If returnPrimitives is False
    (default), values are all converted to str. If returnPrimitives is True, the values
    will retain their original ValueType (e.g. Text, Contributor, Copyright, etc.). If
    returnSorted is False, the returned Tuple will not be sorted by uniqueName (the
    default behavior is to sort).

    Note that we cannot properly type-hint the return value, since derived classes (such
    as RichMetadata) are allowed to return their own typed values that might not be str
    or ValueType.

    ```python
    >>> c = corpus.parse('corelli/opus3no1/1grave')
    >>> c.metadata.all()
    (('arranger', 'Michael Scott Cuthbert'),
     ('composer', 'Arcangelo Corelli'),
     ('copyright', '© 2014, Creative Commons License (CC-BY)'),
     ('corpusFilePath', 'corelli/opus3no1/1grave.xml'),
     ('fileFormat', 'musicxml'),
     ('filePath', '...corpus/corelli/opus3no1/1grave.xml'),
     ('movementName', 'Sonata da Chiesa, No. I (opus 3, no. 1)'),
     ('software', 'Dolet...'),
     ('software', 'Finale...'),
     ('software', 'music21 v...'))
    ```

    ```python
    >>> c.metadata.date = metadata.DateRelative('1689', 'onOrBefore')
    >>> c.metadata.localeOfComposition = 'Rome'
    >>> c.metadata.all(skipContributors=True)
    (('copyright', '© 2014, Creative Commons License (CC-BY)'),
     ('corpusFilePath', 'corelli/opus3no1/1grave.xml'),
     ('dateCreated', '1689/--/-- or earlier'),
     ('fileFormat', 'musicxml'),
     ('filePath', '...corpus/corelli/opus3no1/1grave.xml'),
     ('localeOfComposition', 'Rome'),
     ('movementName', 'Sonata da Chiesa, No. I (opus 3, no. 1)'),
     ('software', 'Dolet...'),
     ('software', 'Finale...'),
     ('software', 'music21 v...'))
    ```

    ```python
    >>> c.metadata.all(returnPrimitives=True, returnSorted=False)
    (('software', <music21.metadata.primitives.Text music21 v...>),
     ('software', <music21.metadata.primitives.Text Finale ...>),
     ('software', <music21.metadata.primitives.Text Dolet Light...>),
     ('movementName', <...Text Sonata da Chiesa, No. I (opus 3, no. 1)>),
     ('composer', <music21.metadata.primitives.Contributor composer:Arcangelo Corelli>),
     ...
     ('dateCreated', <music21.metadata.primitives.DateRelative 1689/--/-- or earlier>),
     ('localeOfComposition', <music21.metadata.primitives.Text Rome>))
    ```

    ```python
    >>> c.metadata.all(skipNonContributors=True, returnPrimitives=True, returnSorted=True)
    (('arranger', <music21.metadata.primitives.Contributor arranger:Michael Scott Cuthbert>),
     ('composer', <music21.metadata.primitives.Contributor composer:Arcangelo Corelli>))
    ```

static Metadata.convertValue(*uniqueName: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *value: [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")*) → [DatePrimitive](moduleMetadataPrimitives.html#music21.metadata.primitives.DatePrimitive "music21.metadata.primitives.DatePrimitive") | [Text](moduleMetadataPrimitives.html#music21.metadata.primitives.Text "music21.metadata.primitives.Text") | [Contributor](moduleMetadataPrimitives.html#music21.metadata.primitives.Contributor "music21.metadata.primitives.Contributor") | [Copyright](moduleMetadataPrimitives.html#music21.metadata.primitives.Copyright "music21.metadata.primitives.Copyright") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](../_modules/music21/metadata.html#Metadata.convertValue)
:   Converts a value (string, date, etc.) to the appropriate ValueType
    (defined by uniqueName and metadata.proporties.UNIQUE\_NAME\_TO\_VALUE\_TYPE).

    Converts certain named values to Text:

    ```python
    >>> metadata.Metadata.convertValue('title', 'Density 21.5')
    <music21.metadata.primitives.Text Density 21.5>
    ```

    Non-string values can often be converted automatically

    ```python
    >>> metadata.Metadata.convertValue('title', 21.5)
    <music21.metadata.primitives.Text 21.5>
    ```

    If it is already the appropriate type, no change is made

    ```python
    >>> md_text = metadata.Text('The Desert Music')
    >>> metadata.Metadata.convertValue('title', md_text)
    <music21.metadata.primitives.Text The Desert Music>
    >>> metadata.Metadata.convertValue('title', md_text) is md_text
    True
    ```

    Converts copyright named values to Copyright:

    ```python
    >>> metadata.Metadata.convertValue('copyright', 'copyright-as-string')
    <music21.metadata.primitives.Copyright copyright-as-string>
    >>> metadata.Metadata.convertValue('copyright', metadata.Text('copyright-as-text'))
    <music21.metadata.primitives.Copyright copyright-as-text>
    >>> metadata.Metadata.convertValue('copyright', metadata.Copyright('2025 Ariadne Press'))
    <music21.metadata.primitives.Copyright 2025 Ariadne Press>
    ```

    Converts composer or other named values to Contributors:

    ```python
    >>> metadata.Metadata.convertValue('composer', 'Kayleigh Rose Amstutz')
    <music21.metadata.primitives.Contributor composer:Kayleigh Rose Amstutz>
    >>> metadata.Metadata.convertValue('librettist', metadata.Text('Da Ponte'))
    <music21.metadata.primitives.Contributor librettist:Da Ponte>
    ```

    Unusual roles need to be passed with “otherContributor” and role already defined.
    (Essentially, make your own)

    ```python
    >>> metadata.Metadata.convertValue('otherContributor',
    ...     metadata.Contributor(role='conceptual-artist', name='Robert Wilson'))
    <music21.metadata.primitives.Contributor conceptual-artist:Robert Wilson>
    ```

    Converts certain named values to DateSingle:

    ```python
    >>> metadata.Metadata.convertValue('dateCreated', '1938')
    <music21.metadata.primitives.DateSingle 1938/--/-->
    >>> metadata.Metadata.convertValue('dateCreated', metadata.Text('1938/02'))
    <music21.metadata.primitives.DateSingle 1938/02/-->
    ```

    Datetime objects, like this one for the Rite of Spring riot, also get converted.

    ```python
    >>> from datetime import datetime
    >>> dt = datetime(1913, 5, 29)
    >>> metadata.Metadata.convertValue('dateCreated', dt)
    <music21.metadata.primitives.DateSingle 1913/05/29>
    ```

    For DateBetween objects one must pass their own already created primitive
    (so no need to use this)

    ```python
    >>> metadata.Metadata.convertValue('dateCreated',
    ...     metadata.DateBetween(['1938', '1939']))
    <music21.metadata.primitives.DateBetween 1938/--/-- to 1939/--/-->
    ```

    * Added in v10 – newly exposed as a public function (was private)

Metadata.getContributorsByRole(*role: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[Contributor](moduleMetadataPrimitives.html#music21.metadata.primitives.Contributor "music21.metadata.primitives.Contributor"), ...][[source]](../_modules/music21/metadata.html#Metadata.getContributorsByRole)
:   Return a `Contributor` if defined for a
    provided role.

    We allow role == None, since None is a valid custom contributor role.

    ```python
    >>> md = metadata.Metadata(title='Violin Concerto')
    ```

    ```python
    >>> c = metadata.Contributor()
    >>> c.name = 'Price, Florence'
    >>> c.role = 'composer'
    >>> md.addContributor(c)
    >>> cTuple = md.getContributorsByRole('composer')
    >>> cTuple
    (<music21.metadata.primitives.Contributor composer:Price, Florence>,)
    ```

    ```python
    >>> cTuple[0].name
    'Price, Florence'
    ```

    Some musicxml files have contributors with no role defined. To get
    these contributors, search for getContributorsByRole(None). N.B. upon
    output to MusicXML, music21 gives these contributors the generic role
    of “creator”

    ```python
    >>> c2 = metadata.Contributor()
    >>> c2.name = 'Baron van Swieten'
    >>> md.add('otherContributor', c2)
    >>> noRoleTuple = md.getContributorsByRole(None)
    >>> len(noRoleTuple)
    1
    >>> noRoleTuple[0].role is None
    True
    >>> noRoleTuple[0].name
    'Baron van Swieten'
    ```

Metadata.getCustom(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[DatePrimitive](moduleMetadataPrimitives.html#music21.metadata.primitives.DatePrimitive "music21.metadata.primitives.DatePrimitive") | [Text](moduleMetadataPrimitives.html#music21.metadata.primitives.Text "music21.metadata.primitives.Text") | [Contributor](moduleMetadataPrimitives.html#music21.metadata.primitives.Contributor "music21.metadata.primitives.Contributor") | [Copyright](moduleMetadataPrimitives.html#music21.metadata.primitives.Copyright "music21.metadata.primitives.Copyright") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), ...][[source]](../_modules/music21/metadata.html#Metadata.getCustom)
:   Gets any custom-named metadata items. The name can be free-form,
    or it can be a custom ‘namespace:name’.

    getCustom always returns tuple[Text, …], which may be empty.

    ```python
    >>> md = metadata.Metadata()
    >>> md.setCustom('measure with 2nd ending', 'measure 128')
    >>> md.getCustom('measure with 2nd ending')
    (<music21.metadata.primitives.Text measure 128>,)
    ```

    A second item can also be added.

    ```python
    >>> md.addCustom('measure with 2nd ending', 'measure 192')
    >>> measures = md.getCustom('measure with 2nd ending')
    ```

    ```python
    >>> isinstance(measures, tuple)
    True
    >>> len(measures)
    2
    >>> measures
    (<music21.metadata.primitives.Text measure 128>,
     <music21.metadata.primitives.Text measure 192>)
    ```

static Metadata.isContributorUniqueName(*uniqueName: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/metadata.html#Metadata.isContributorUniqueName)
:   Determines if a unique name is associated with a standard contributor
    property. Returns False if no such associated standard contributor
    property can be found.

    We allow uniqueName == None, since None is a valid custom contributor role.

    Example: ‘librettist’ and ‘otherContributor’ are unique names of standard
    contributors.

    ```python
    >>> metadata.Metadata.isContributorUniqueName('librettist')
    True
    >>> metadata.Metadata.isContributorUniqueName('otherContributor')
    True
    ```

    Example: ‘alternativeTitle’ is the unique name of a standard property,
    but it is not a contributor.

    ```python
    >>> metadata.Metadata.isContributorUniqueName('alternativeTitle')
    False
    ```

    Example: ‘average duration’ is not the unique name of a standard property.

    ```python
    >>> metadata.Metadata.isContributorUniqueName('average duration')
    False
    ```

Metadata.isStandardName(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/metadata.html#Metadata.isStandardName)
:   Determines if name is either a ‘namespace:name’ or a ‘uniqueName’
    associated with a standard property.

    Returns False if no such associated standard property can be found.

    ```python
    >>> md = metadata.Metadata()
    >>> md.isStandardName('librettist')
    True
    ```

    ‘marcrel:LBT’ is the namespace name of ‘librettist’

    ```python
    >>> md.isStandardName('marcrel:LBT')
    True
    ```

    Some examples of non-standard (custom) names.

    ```python
    >>> md.isStandardName('average duration')
    False
    >>> md.isStandardName('soundtracker:SampleName')
    False
    ```

static Metadata.namespaceNameToUniqueName(*namespaceName: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/metadata.html#Metadata.namespaceNameToUniqueName)
:   Translates a standard property namespace name (‘namespace:name’) to that
    standard property’s uniqueName.

    An example from the MARC Relators namespace: the unique name of
    ‘marcrel:LBT’ is ‘librettist’.

    ```python
    >>> metadata.Metadata.namespaceNameToUniqueName('marcrel:LBT')
    'librettist'
    ```

    Returns None if no such standard property exists.

    ```python
    >>> metadata.Metadata.namespaceNameToUniqueName('soundtracker:SampleName') is None
    True
    ```

    An example from the Dublin Core namespace: the unique name of
    ‘dcterms:alternative’ is ‘alternativeTitle’.

    ```python
    >>> metadata.Metadata.namespaceNameToUniqueName('dcterms:alternative')
    'alternativeTitle'
    ```

Metadata.search(*query: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Pattern](https://docs.python.org/3/library/typing.html#typing.Pattern "(in Python v3.14)") | [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")], [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *field: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\*\*keywords*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][[source]](../_modules/music21/metadata.html#Metadata.search)
:   Search one or all fields with a query, given either as a string or a
    regular expression match.

    ```python
    >>> md = metadata.Metadata()
    >>> md.composer = 'Joplin, Scott'
    >>> md.title = 'Maple Leaf Rag'
    ```

    ```python
    >>> md.search(
    ...     'joplin',
    ...     field='composer',
    ...     )
    (True, 'composer')
    ```

    Note how the incomplete field name in the following example is still
    matched:

    ```python
    >>> md.search(
    ...     'joplin',
    ...     field='compos',
    ...     )
    (True, 'composer')
    ```

    These don’t work (Richard didn’t have the sense of rhythm to write this!)

    ```python
    >>> md.search(
    ...     'Wagner',
    ...     field='composer',
    ...     )
    (False, None)
    ```

    ```python
    >>> md.search('Wagner')
    (False, None)
    ```

    ```python
    >>> md.search('leaf')
    (True, 'title')
    ```

    ```python
    >>> md.search(
    ...     'leaf',
    ...     field='composer',
    ...     )
    (False, None)
    ```

    ```python
    >>> md.search(
    ...     'leaf',
    ...     field='title',
    ...     )
    (True, 'title')
    ```

    ```python
    >>> md.search('leaf|entertainer')
    (True, 'title')
    ```

    ```python
    >>> md.search('opl(.*)cott')
    (True, 'composer')
    ```

    * New in v4: use a keyword argument to search
      that field directly:

    ```python
    >>> md.search(composer='Joplin')
    (True, 'composer')
    ```

Metadata.setCustom(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *value: [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)") | [Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "(in Python v3.14)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")]*)[[source]](../_modules/music21/metadata.html#Metadata.setCustom)
:   Sets any custom-named metadata items (deleting any existing such items).
    The name can be free-form, or it can be a custom ‘namespace:name’.

    setCustom takes a single object of any type, or a list/tuple of
    objects of any type. The object(s) will be converted to Text.

    ```python
    >>> md = metadata.Metadata()
    >>> md.setCustom('measure with 2nd ending', 'measure 128')
    >>> md.getCustom('measure with 2nd ending')
    (<music21.metadata.primitives.Text measure 128>,)
    ```

    An item list can also be set.

    ```python
    >>> md.setCustom('measure with 2nd ending', ['measure 192', 'measure 256'])
    >>> measures = md.getCustom('measure with 2nd ending')
    ```

    ```python
    >>> isinstance(measures, tuple)
    True
    >>> len(measures)
    2
    >>> measures
    (<music21.metadata.primitives.Text measure 192>,
     <music21.metadata.primitives.Text measure 256>)
    ```

static Metadata.uniqueNameToNamespaceName(*uniqueName: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/metadata.html#Metadata.uniqueNameToNamespaceName)
:   Translates a unique name to the associated standard property’s
    namespace name (i.e. the property’s name in the form ‘namespace:name’).

    An example from the MARC Relators namespace: the namespace name of
    ‘librettist’ is ‘marcrel:LBT’.

    ```python
    >>> metadata.Metadata.uniqueNameToNamespaceName('librettist')
    'marcrel:LBT'
    ```

    Returns None if no such associated standard property can be found.

    ```python
    >>> metadata.Metadata.uniqueNameToNamespaceName('average duration') is None
    True
    ```

    An example from the Dublin Core namespace: the namespace name of
    ‘alternativeTitle’ is ‘dcterms:alternative’.

    ```python
    >>> metadata.Metadata.uniqueNameToNamespaceName('alternativeTitle')
    'dcterms:alternative'
    ```

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`Metadata`](#music21.metadata.Metadata "music21.metadata.Metadata") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## RichMetadata

class music21.metadata.RichMetadata(*\*\*keywords*)[[source]](../_modules/music21/metadata.html#RichMetadata)
:   RichMetadata adds to Metadata information about the contents of the Score
    it is attached to. TimeSignature, KeySignature and related analytical is
    stored. RichMetadata are generally only created in the process of creating
    stored JSON metadata.

    ```python
    >>> richMetadata = metadata.RichMetadata(title='Concerto in F')
    >>> richMetadata.title
    'Concerto in F'
    ```

    ```python
    >>> richMetadata.keySignatureFirst = key.KeySignature(-1)
    >>> 'keySignatureFirst' in richMetadata.additionalRichMetadataAttributes
    True
    ```

    RichMetadata objects contain all the usual Metadata items, plus some observed
    musical information analyzed from the score. Here is a list of what information
    is added:

    ```python
    >>> richMetadata.additionalRichMetadataAttributes
    ('ambitus', 'keySignatureFirst', 'keySignatures', 'noteCount', 'numberOfParts',
     'pitchHighest', 'pitchLowest', 'scoreQuarterLength', 'sourcePath', 'tempoFirst',
     'tempos', 'timeSignatureFirst', 'timeSignatures')
    ```

    Changed in v10: renamed quarterLength to scoreQuarterLength.
    :   Because RichMetadata is a Music21Object, quarterLength is a property that must
        return the length of the RichMetadata object itself and should not have been
        ovewritten

[`RichMetadata`](#music21.metadata.RichMetadata "music21.metadata.RichMetadata") bases

* [`Metadata`](#music21.metadata.Metadata "music21.metadata.Metadata")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`RichMetadata`](#music21.metadata.RichMetadata "music21.metadata.RichMetadata") read-only properties

Read-only properties inherited from [`Metadata`](#music21.metadata.Metadata "music21.metadata.Metadata"):

|  |  |  |
| --- | --- | --- |
| * [`bestTitle`](#music21.metadata.Metadata.bestTitle "music21.metadata.Metadata.bestTitle") | * [`contributors`](#music21.metadata.Metadata.contributors "music21.metadata.Metadata.contributors") | * [`software`](#music21.metadata.Metadata.software "music21.metadata.Metadata.software") |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`RichMetadata`](#music21.metadata.RichMetadata "music21.metadata.RichMetadata") read/write properties

Read/write properties inherited from [`Metadata`](#music21.metadata.Metadata "music21.metadata.Metadata"):

|  |  |  |
| --- | --- | --- |
| * [`alternativeTitle`](#music21.metadata.Metadata.alternativeTitle "music21.metadata.Metadata.alternativeTitle") * [`composer`](#music21.metadata.Metadata.composer "music21.metadata.Metadata.composer") * [`composers`](#music21.metadata.Metadata.composers "music21.metadata.Metadata.composers") * [`copyright`](#music21.metadata.Metadata.copyright "music21.metadata.Metadata.copyright") * [`corpusFilePath`](#music21.metadata.Metadata.corpusFilePath "music21.metadata.Metadata.corpusFilePath") * [`dateCreated`](#music21.metadata.Metadata.dateCreated "music21.metadata.Metadata.dateCreated") * [`fileFormat`](#music21.metadata.Metadata.fileFormat "music21.metadata.Metadata.fileFormat") | * [`fileNumber`](#music21.metadata.Metadata.fileNumber "music21.metadata.Metadata.fileNumber") * [`filePath`](#music21.metadata.Metadata.filePath "music21.metadata.Metadata.filePath") * [`librettist`](#music21.metadata.Metadata.librettist "music21.metadata.Metadata.librettist") * [`librettists`](#music21.metadata.Metadata.librettists "music21.metadata.Metadata.librettists") * [`localeOfComposition`](#music21.metadata.Metadata.localeOfComposition "music21.metadata.Metadata.localeOfComposition") * [`lyricist`](#music21.metadata.Metadata.lyricist "music21.metadata.Metadata.lyricist") | * [`lyricists`](#music21.metadata.Metadata.lyricists "music21.metadata.Metadata.lyricists") * [`movementName`](#music21.metadata.Metadata.movementName "music21.metadata.Metadata.movementName") * [`movementNumber`](#music21.metadata.Metadata.movementNumber "music21.metadata.Metadata.movementNumber") * [`number`](#music21.metadata.Metadata.number "music21.metadata.Metadata.number") * [`opusNumber`](#music21.metadata.Metadata.opusNumber "music21.metadata.Metadata.opusNumber") * [`title`](#music21.metadata.Metadata.title "music21.metadata.Metadata.title") |

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`RichMetadata`](#music21.metadata.RichMetadata "music21.metadata.RichMetadata") methods

RichMetadata.all(*\**, *skipContributors: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *skipNonContributors: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *returnPrimitives: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *returnSorted: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")], ...][[source]](../_modules/music21/metadata.html#RichMetadata.all)
:   Returns all values stored in this RichMetadata as a Tuple of Tuples.
    Each individual Metadata Tuple is (uniqueName, value) and each additional
    RichMetadata tuple is (name, richAttributeValue).

    ```python
    >>> rmd = metadata.RichMetadata()
    >>> c = corpus.parse('corelli/opus3no1/1grave')
    >>> rmd.merge(c.metadata)
    >>> rmd.update(c)
    >>> rmd.all()
    (('ambitus',
        AmbitusShort(semitones=48, diatonic='P1', pitchLowest='C2', pitchHighest='C6')),
     ('arranger', 'Michael Scott Cuthbert'),
     ('composer', 'Arcangelo Corelli'),
     ...
     ('sourcePath', 'corelli/opus3no1/1grave.xml'),
     ('tempoFirst', '<music21.tempo.MetronomeMark Quarter=60 (playback only)>'),
     ('tempos', ['<music21.tempo.MetronomeMark Quarter=60 (playback only)>']),
     ('timeSignatureFirst', '4/4'),
     ('timeSignatures', ['4/4']))
    ```

    ```python
    >>> rmd.dateCreated = metadata.DateRelative('1689', 'onOrBefore')
    >>> rmd.localeOfComposition = 'Rome'
    >>> rmd.all(skipContributors=True)
    (('ambitus',
        AmbitusShort(semitones=48, diatonic='P1', pitchLowest='C2', pitchHighest='C6')),
     ('copyright', '© 2014, Creative Commons License (CC-BY)'),
     ('corpusFilePath', 'corelli/opus3no1/1grave.xml'),
     ('dateCreated', '1689/--/-- or earlier'),
     ('fileFormat', 'musicxml'),
     ...
     ('keySignatures', [-1]),
     ('localeOfComposition', 'Rome'),
     ('movementName', 'Sonata da Chiesa, No. I (opus 3, no. 1)'),
     ...
     ('timeSignatures', ['4/4']))
    ```

    ```python
    >>> rmd.all(returnPrimitives=True, returnSorted=False)
    (('software', <music21.metadata.primitives.Text music21 ...>),
     ('software', <music21.metadata.primitives.Text Finale 2014 for Mac>),
     ('software', <music21.metadata.primitives.Text Dolet Light for Finale 2014>),
     ('movementName', <...Text Sonata da Chiesa, No. I (opus 3, no. 1)>),
     ('composer', <music21.metadata.primitives.Contributor composer:Arcangelo Corelli>),
     ...
     ('timeSignatures', ['4/4']))
    ```

    ```python
    >>> rmd.all(skipNonContributors=True, returnPrimitives=True, returnSorted=True)
    (('arranger', <music21.metadata.primitives.Contributor arranger:Michael Scott Cuthbert>),
     ('composer', <music21.metadata.primitives.Contributor composer:Arcangelo Corelli>))
    ```

RichMetadata.getSourcePath(*streamObj*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](../_modules/music21/metadata.html#RichMetadata.getSourcePath)
:   Get a string of the path after the corpus for the piece. Useful for
    searching on corpus items without proper composer data.

    ```python
    >>> rmd = metadata.RichMetadata()
    >>> b = corpus.parse('bwv66.6')
    >>> rmd.getSourcePath(b)
    'bach/bwv66.6.mxl'
    ```

RichMetadata.merge(*other*, *favorSelf=False*)[[source]](../_modules/music21/metadata.html#RichMetadata.merge)
:   Given another Metadata or RichMetadata object, combine
    all attributes and return a new object.

    ```python
    >>> md = metadata.Metadata(title='Concerto in F')
    >>> md.title
    'Concerto in F'
    ```

    ```python
    >>> richMetadata = metadata.RichMetadata()
    >>> richMetadata.merge(md)
    >>> richMetadata.title
    'Concerto in F'
    ```

RichMetadata.update(*streamObj*)[[source]](../_modules/music21/metadata.html#RichMetadata.update)
:   Given a Stream object, update attributes with stored objects.

    ```python
    >>> rmd = metadata.RichMetadata()
    >>> rmd.keySignatureFirst is None
    True
    >>> rmd.sourcePath
    ''
    ```

    ```python
    >>> b = corpus.parse('bwv66.6')
    >>> rmd.update(b)
    >>> rmd.keySignatureFirst
    3
    >>> rmd.sourcePath
    'bach/bwv66.6.mxl'
    >>> rmd.numberOfParts
    4
    ```

Methods inherited from [`Metadata`](#music21.metadata.Metadata "music21.metadata.Metadata"):

|  |  |  |
| --- | --- | --- |
| * [`__getitem__()`](#music21.metadata.Metadata.__getitem__ "music21.metadata.Metadata.__getitem__") * [`add()`](#music21.metadata.Metadata.add "music21.metadata.Metadata.add") * [`addContributor()`](#music21.metadata.Metadata.addContributor "music21.metadata.Metadata.addContributor") * [`addCustom()`](#music21.metadata.Metadata.addCustom "music21.metadata.Metadata.addCustom") * [`convertValue()`](#music21.metadata.Metadata.convertValue "music21.metadata.Metadata.convertValue") | * [`getContributorsByRole()`](#music21.metadata.Metadata.getContributorsByRole "music21.metadata.Metadata.getContributorsByRole") * [`getCustom()`](#music21.metadata.Metadata.getCustom "music21.metadata.Metadata.getCustom") * [`isContributorUniqueName()`](#music21.metadata.Metadata.isContributorUniqueName "music21.metadata.Metadata.isContributorUniqueName") * [`isStandardName()`](#music21.metadata.Metadata.isStandardName "music21.metadata.Metadata.isStandardName") | * [`namespaceNameToUniqueName()`](#music21.metadata.Metadata.namespaceNameToUniqueName "music21.metadata.Metadata.namespaceNameToUniqueName") * [`search()`](#music21.metadata.Metadata.search "music21.metadata.Metadata.search") * [`setCustom()`](#music21.metadata.Metadata.setCustom "music21.metadata.Metadata.setCustom") * [`uniqueNameToNamespaceName()`](#music21.metadata.Metadata.uniqueNameToNamespaceName "music21.metadata.Metadata.uniqueNameToNamespaceName") |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`RichMetadata`](#music21.metadata.RichMetadata "music21.metadata.RichMetadata") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## AmbitusShort

class music21.metadata.AmbitusShort(*semitones: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *diatonic: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *pitchLowest: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *pitchHighest: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*)[[source]](../_modules/music21/metadata.html#AmbitusShort)
:   A namedtuple representing the ambitus (range) using ints and strings

    ```python
    >>> metadata.AmbitusShort(7, 'P5', 'B3', 'F#4')
    AmbitusShort(semitones=7, diatonic='P5', pitchLowest='B3', pitchHighest='F#4')
    ```
