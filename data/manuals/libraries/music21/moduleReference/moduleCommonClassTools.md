Source: https://music21.org/music21docs/moduleReference/moduleCommonClassTools.html

# music21.common.classTools

## Functions

music21.common.classTools.classToClassStr(*classObj: [type](moduleBar.html#music21.bar.Barline.type "music21.bar.Barline.type")*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](../_modules/music21/common/classTools.html#classToClassStr)
:   Convert a class object to a class string.

    ```python
    >>> common.classToClassStr(note.Note)
    'Note'
    >>> common.classToClassStr(chord.Chord)
    'Chord'
    ```

music21.common.classTools.getClassSet(*instance*, *classNameTuple=None*)[[source]](../_modules/music21/common/classTools.html#getClassSet)
:   Return the classSet for an instance (whether a Music21Object or something else).
    See base.Music21Object.classSet for more details.

    ```python
    >>> p = pitch.Pitch()
    >>> cs = common.classTools.getClassSet(p)
    >>> cs
     frozenset(...)
    >>> pitch.Pitch in cs
    True
    >>> 'music21.pitch.Pitch' in cs
    True
    >>> 'Pitch' in cs
    True
    >>> object in cs
    True
    >>> 'object' in cs
    True
    >>> note.Note in cs
    False
    ```

    To save time (this IS a performance-critical operation), classNameTuple
    can be passed a tuple of names such as (‘Pitch’, ‘object’) that
    will save the creation time of this set.

    ```python
    >>> cs2 = common.classTools.getClassSet(p, classNameTuple=('Pitch', 'ProtoM21Object'))
    >>> 'Pitch' in cs2
    True
    ```

    Use base.Music21Object.classSet in general for music21Objects since it
    not only caches the result for each object, it caches the result for the
    whole class the first time it is run.

music21.common.classTools.holdsType(*usrData: [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")*, *checkType: [type](moduleBar.html#music21.bar.Barline.type "music21.bar.Barline.type")[\_T]*) → [TypeGuard](https://docs.python.org/3/library/typing.html#typing.TypeGuard "(in Python v3.14)")[[Collection](https://docs.python.org/3/library/collections.abc.html#collections.abc.Collection "(in Python v3.14)")[\_T]][[source]](../_modules/music21/common/classTools.html#holdsType)
:   Returns True if usrData is a Collection of type checkType.

    This reads an item from usrData, so don’t use it on something
    where iterating destroys the type.

    ```python
    >>> y = [1, 2, 3]
    >>> common.classTools.holdsType(y, int)
    True
    >>> common.classTools.holdsType(5, int)
    False
    >>> common.classTools.holdsType(['hello'], str)
    True
    ```

    Empty iterators hold the type:

    ```python
    >>> common.classTools.holdsType([], float)
    True
    ```

    Note that a mixed collection holds whatever is first

    ```python
    >>> common.classTools.holdsType((4, 'hello'), int)
    True
    >>> common.classTools.holdsType((4, 'hello'), str)
    False
    ```

    Works on sets with arbitrary order:

    ```python
    >>> common.classTools.holdsType({2, 10}, int)
    True
    ```

    Intelligent collections will not have their position affected.

    ```python
    >>> m = stream.Measure([note.Note('C'), note.Rest()])
    >>> common.classTools.holdsType(m, note.GeneralNote)
    True
    >>> next(iter(m))
    <music21.note.Note C>
    ```

    ```python
    >>> r = range(1, 100)
    >>> common.classTools.holdsType(r, int)
    True
    >>> next(iter(r))
    1
    ```

    * New in v9.

music21.common.classTools.isInt(*usrData: [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")*) → [TypeGuard](https://docs.python.org/3/library/typing.html#typing.TypeGuard "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][[source]](../_modules/music21/common/classTools.html#isInt)
:   Check if usrData is an integer and not True or False.

    ```python
    >>> common.isInt(3)
    True
    >>> common.isInt(False)
    False
    >>> common.isInt(2.0)
    False
    ```

music21.common.classTools.isIterable(*usrData: [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")*) → [TypeGuard](https://docs.python.org/3/library/typing.html#typing.TypeGuard "(in Python v3.14)")[[Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "(in Python v3.14)")][[source]](../_modules/music21/common/classTools.html#isIterable)
:   Returns True if is the object can be iter’d over
    and is NOT a string. Marks it as an Iterable for type checking.

    ```python
    >>> common.isIterable([5, 10])
    True
    >>> common.isIterable('sharp')
    False
    >>> common.isIterable((None, None))
    True
    >>> common.isIterable(stream.Stream())
    True
    ```

    Ranges are not iterators by python 3, but return True

    ```python
    >>> common.isIterable(range(20))
    True
    ```

    Classes are not iterable even if their instances are:

    ```python
    >>> common.isIterable(stream.Stream)
    False
    >>> common.isIterable(list)
    False
    ```

    * Changed in v7.3: Classes (not instances) are not iterable

music21.common.classTools.isListLike(*usrData: [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")*) → [TypeGuard](https://docs.python.org/3/library/typing.html#typing.TypeGuard "(in Python v3.14)")[[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)") | [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")][[source]](../_modules/music21/common/classTools.html#isListLike)
:   Returns True if is a List or Tuple or their subclasses.

    Formerly allowed for set here, but that does not allow for
    subscripting (set([1, 2, 3])[0] is undefined).

    Differs from isinstance(collections.abc.Sequence()) in that
    we do not want Streams included even if \_\_contains\_\_, \_\_reversed\_\_,
    and count are added, and we do not want to include str or bytes.

    ```python
    >>> common.isListLike([])
    True
    >>> common.isListLike('sharp')
    False
    >>> common.isListLike((None, None))
    True
    >>> common.isListLike({'a', 'b', 'c', 'c'})
    False
    >>> common.isListLike(stream.Stream())
    False
    ```

music21.common.classTools.isNum(*usrData: t.Any*) → t.TypeGuard[t.Union[[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), Fraction]][[source]](../_modules/music21/common/classTools.html#isNum)
:   check if usrData is a music21 number (float, int, Fraction),
    return boolean and if True casts the value as a float, int, or Fraction number

    Differs from isinstance(usrData, Rational) primarily in that this function
    does not return True for True, False. See below for other differences.

    ```python
    >>> common.isNum(3.0)
    True
    >>> common.isNum(3)
    True
    >>> common.isNum('three')
    False
    >>> common.isNum([2, 3, 4])
    False
    ```

    True and False are not considered numbers by isNum.

    ```python
    >>> common.isNum(True)
    False
    >>> common.isNum(False)
    False
    ```

    None is also not a number:

    ```python
    >>> common.isNum(None)
    False
    ```

    This function does not use isinstance(usrData, Rational) which is 2-6 times slower
    than calling this function (except in the case of Fraction, when
    it’s 6 times faster, but that’s rarer). (6 times slower on Py3.4, now
    only 2x slower in Python 3.10)

    Runs by adding 0 to the “number” – so anything that implements
    adding with a scalar will pass. Thus, this Decimal number is technically incorrectly typed
    as being a float, int, or Fraction. However, since Decimals are not used in
    music21 it is not really a problem.

    ```python
    >>> from decimal import Decimal
    >>> common.isNum(Decimal('2.0'))
    True
    ```

music21.common.classTools.saveAttributes(*obj*, *\*attributeList: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [Generator](https://docs.python.org/3/library/typing.html#typing.Generator "(in Python v3.14)")[[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][[source]](../_modules/music21/common/classTools.html#saveAttributes)
:   Save a number of attributes in an object and then restore them afterwards.

    ```python
    >>> p = pitch.Pitch('C#2')
    >>> with common.classTools.saveAttributes(p, 'name', 'accidental'):
    ...     p.step = 'E'
    ...     p.accidental = pitch.Accidental('flat')
    ...     p.nameWithOctave
    'E-2'
    >>> p.nameWithOctave
    'C#2'
    ```

    For storing and setting a value on a single attribute see
    `tempAttribute()`.

    * New in v7.

music21.common.classTools.tempAttribute(*obj*, *attribute: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *new\_val=<object object>*)[[source]](../_modules/music21/common/classTools.html#tempAttribute)
:   Temporarily set an attribute in an object to another value
    and then restore it afterwards.

    ```python
    >>> p = pitch.Pitch('C4')
    >>> p.midi
    60
    >>> with common.classTools.tempAttribute(p, 'nameWithOctave', 'D#5'):
    ...     p.midi
    75
    >>> p.nameWithOctave
    'C4'
    ```

    Setting to a new value is optional.

    For working with multiple attributes see `saveAttributes()`.

    * New in v7.
