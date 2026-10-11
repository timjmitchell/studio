Source: https://music21.org/music21docs/moduleReference/modulePrebase.html

# music21.prebase

Classes for pseudo-m21 objects to inherit from. The most import attributes that nearly
everything in music21 – not just things that live in streams –
should inherit from are given below.

Concept borrowed from m21j.

## ProtoM21Object

class music21.prebase.ProtoM21Object[[source]](../_modules/music21/prebase.html#ProtoM21Object)
:   A class for pseudo-m21 objects to inherit from. Any object can inherit from
    ProtoM21Object, and it makes sense for anything a user is likely to encounter
    to inherit from it. Certain translators, etc. can choose to skip it.

    ```python
    >>> class PitchCounter(prebase.ProtoM21Object):
    ...     def _reprInternal(self):
    ...         return 'no pitches'
    ```

    ```python
    >>> pc = PitchCounter()
    >>> pc.classes
    ('PitchCounter', 'ProtoM21Object', 'object')
    >>> PitchCounter in pc.classSet
    True
    >>> 'Note' in pc.classSet
    False
    ```

    For a True/False intersection check against an iterable, use classSet.isdisjoint:

    ```python
    >>> classList = ('music21.note.Note', 'music21.note.Rest')
    >>> pc.classSet.isdisjoint(classList)
    True
    >>> repr(pc)
    '<...PitchCounter no pitches>'
    ```

    ProtoM21Objects, like other Python primitives, cannot be put into streams –
    this is what base.Music21Object does.

    A ProtoM21Object defines several methods relating to unified representation
    and keeping track of the classes of the object. It has no instance attributes
    or properties, and thus adds a very small creation time impact: recent
    tests show that an empty object with an empty \_\_init\_\_() method can
    be created in about 175ns while an empty object that subclasses ProtoM21Object
    with the same empty \_\_init\_\_() takes only 180ns, or a 5ns impact. On
    real objects, the creation time percentage hit is usually much smaller.

    ProtoM21Objects have no \_\_init\_\_() defined, so do not call super().\_\_init\_\_() on
    objects that only inherit from ProtoM21Object unless you like wasting 200ns.

[`ProtoM21Object`](#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object") read-only properties

ProtoM21Object.classSet
:   Returns a set (that is, unordered, but indexed) of all classes that
    this class belongs to, including
    string names, fullyQualified string names, and objects themselves.

    It’s cached on a per-class basis, so makes for a really fast way of checking to
    see if something belongs
    to a particular class when you don’t know if the user has given a string,
    a fully qualified string name, or an object.

    Did I mention it’s fast? It’s not as fast as x in n.classes or isinstance(n, x)
    if you know whether it’s a string or class, but this is good and safe to take
    in either a string or a class.

    ```python
    >>> n = note.Note()
    >>> 'Note' in n.classSet
    True
    >>> 'music21.note.Note' in n.classSet
    True
    >>> note.Note in n.classSet
    True
    ```

    ```python
    >>> 'Rest' in n.classSet
    False
    >>> note.Rest in n.classSet
    False
    ```

    For checking if an object is part of any number of objects use not
    with isdisjoint. A little unwiedly but works super fast:

    ```python
    >>> checkClasses = (spanner.Slur, note.NotRest)
    >>> not n.classSet.isdisjoint(checkClasses)
    True
    ```

    ```python
    >>> object in n.classSet
    True
    ```

    ```python
    >>> sorted([s for s in n.classSet if isinstance(s, str)])
    ['GeneralNote',
     'Music21Object',
     'NotRest',
     'Note',
     'ProtoM21Object',
     'base.Music21Object',
     'builtins.object',
     'music21.base.Music21Object',
     'music21.note.GeneralNote',
     'music21.note.NotRest',
     'music21.note.Note',
     'music21.prebase.ProtoM21Object',
     'note.GeneralNote',
     'note.NotRest',
     'note.Note',
     'object',
     'prebase.ProtoM21Object']
    ```

    ```python
    >>> sorted([s for s in n.classSet if not isinstance(s, str)], key=lambda x: x.__name__)
    [<class 'music21.note.GeneralNote'>,
     <class 'music21.base.Music21Object'>,
     <class 'music21.note.NotRest'>,
     <class 'music21.note.Note'>,
     <class 'music21.prebase.ProtoM21Object'>,
     <class 'object'>]
    ```

    * Changed in v8: partially qualified objects such as ‘note.Note’ have been added.

ProtoM21Object.classes
:   Returns a tuple containing the names (strings, not objects) of classes that this
    object belongs to – starting with the object’s class name and going up the mro()
    for the object.

    Notes are Music21Objects:

    ```python
    >>> n = note.Note('C#')
    >>> n.classes
    ('Note', 'NotRest', 'GeneralNote', 'Music21Object', 'ProtoM21Object', 'object')
    ```

    Durations are not, but they inherit from ProtoM21Object

    ```python
    >>> d = duration.Duration('half')
    >>> d.classes
    ('Duration', 'ProtoM21Object', 'SlottedObjectMixin', 'object')
    ```

    Having quick access to these things as strings makes it easier to do comparisons:

    Example: find GClefs that are not Treble clefs (or treble 8vb, etc.):

    ```python
    >>> s = stream.Stream()
    >>> s.insert(10, clef.GClef())
    >>> s.insert(20, clef.TrebleClef())
    >>> s.insert(30, clef.FrenchViolinClef())
    >>> s.insert(40, clef.Treble8vbClef())
    >>> s.insert(50, clef.BassClef())
    >>> s2 = stream.Stream()
    >>> for thing in s:
    ...    if isinstance(thing, clef.GClef) and not isinstance(thing, clef.TrebleClef):
    ...        s2.insert(thing)
    >>> s2.show('text')
    {10.0} <music21.clef.GClef>
    {30.0} <music21.clef.FrenchViolinClef>
    ```

    Changed in v2: returns a tuple, not a list.
