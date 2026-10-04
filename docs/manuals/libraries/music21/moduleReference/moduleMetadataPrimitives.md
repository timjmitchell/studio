Source: https://music21.org/music21docs/moduleReference/moduleMetadataPrimitives.html

# music21.metadata.primitives

## Text

class music21.metadata.primitives.Text(*data: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Text](#music21.metadata.primitives.Text "music21.metadata.primitives.Text") = ''*, *language: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *isTranslated: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *encodingScheme: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](../_modules/music21/metadata/primitives.html#Text)
:   One unit of text data: a title, a name, or some other text data. Store the
    string and a language name or code. This object can be used and/or
    subclassed for a variety for of text storage.

    ```python
    >>> td = metadata.Text('concerto in d', 'en')
    >>> str(td)
    'concerto in d'
    >>> td.language
    'en'
    ```

[`Text`](#music21.metadata.primitives.Text "music21.metadata.primitives.Text") bases

* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`Text`](#music21.metadata.primitives.Text "music21.metadata.primitives.Text") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`Text`](#music21.metadata.primitives.Text "music21.metadata.primitives.Text") read/write properties

Text.language
:   Set the language of the Text stored within.

    ```python
    >>> myText = metadata.Text('my text')
    >>> myText.language = 'en'
    >>> myText.language
    'en'
    ```

[`Text`](#music21.metadata.primitives.Text "music21.metadata.primitives.Text") methods

Text.\_\_eq\_\_(*other*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/metadata/primitives.html#Text.__eq__)
:   ```python
    >>> t1 = metadata.Text('some text')
    >>> t2 = metadata.Text('some text')
    >>> t1 == t2
    True
    ```

    Language, isTranslated, and encodingScheme must all exactly match for equality.

    ```python
    >>> t2 = metadata.Text('some text', language='en')
    >>> t1 == t2
    False
    >>> t2 = metadata.Text('some text', isTranslated=True)
    >>> t1 == t2
    False
    >>> t2 = metadata.Text('some text', encodingScheme='scheme42')
    >>> t1 == t2
    False
    ```

    Comparison with non-Text types, including bare strings,
    will always be considered unequal.

    ```python
    >>> t1 == 'some text'
    False
    ```

Text.getNormalizedArticle()[[source]](../_modules/music21/metadata/primitives.html#Text.getNormalizedArticle)
:   Return a string representation with normalized articles.

    ```python
    >>> td = metadata.Text('Ale is Dear, The', language='en')
    >>> str(td)
    'Ale is Dear, The'
    ```

    ```python
    >>> td.getNormalizedArticle()
    'The Ale is Dear'
    ```

    The language will determine whether the article is moved:

    ```python
    >>> td.language = 'de'
    >>> td.getNormalizedArticle()
    'Ale is Dear, The'
    ```

## Date

class music21.metadata.primitives.Date(*\**, *year: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *month: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *day: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *hour: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *minute: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *second: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *yearError: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *monthError: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *dayError: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *hourError: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *minuteError: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *secondError: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](../_modules/music21/metadata/primitives.html#Date)
:   A single date value, specified by year, month, day, hour, minute, and
    second. Note that this class has been created, instead of using Python’s
    datetime, to provide greater flexibility for processing unconventional
    dates, ancient dates, dates with error, and date ranges.

    The `datetime` property can be used to
    retrieve a datetime object when necessary.

    Additionally, each value can be specified as uncertain or approximate;
    if None, assumed to be certain.

    Date objects are fundamental components of
    `DateSingle` and related subclasses that represent
    single dates and date ranges.

    ```python
    >>> a = metadata.Date(year=1843, yearError='approximate')
    >>> a.year
    1843
    ```

    ```python
    >>> a.yearError
    'approximate'
    ```

    ```python
    >>> a = metadata.Date(year='1843?')
    >>> a.yearError
    'uncertain'
    ```

    ```python
    >>> d = metadata.Date(year=1805, month=3, monthError='approximate')
    >>> str(d)
    '1805/03~/--'
    ```

    Note that milliseconds are not retained, as this is a tool for musicology
    and not for file timestamps. However, unlike datetime objects, dates
    in the distant past are supported (though not currently BC/BCE dates).

[`Date`](#music21.metadata.primitives.Date "music21.metadata.primitives.Date") bases

* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`Date`](#music21.metadata.primitives.Date "music21.metadata.primitives.Date") read-only properties

Date.datetime
:   Get a datetime object from a metadata.Date() object

    ```python
    >>> a = metadata.Date(year=1843, month=3, day=3)
    >>> str(a)
    '1843/03/03'
    ```

    ```python
    >>> a.datetime
    datetime.datetime(1843, 3, 3, 0, 0)
    ```

    Lack of a required date element raises an exception:

    ```python
    >>> a = metadata.Date(year=1843, month=3)
    >>> str(a)
    '1843/03/--'
    ```

    ```python
    >>> a.datetime
    Traceback (most recent call last):
    TypeError: function missing required argument 'day' (pos 3)
    ```

Date.hasError
:   Return True if any data points have error defined:

    ```python
    >>> a = metadata.Date(
    ...     year=1843,
    ...     month=3,
    ...     day=3,
    ...     dayError='approximate',
    ...     )
    >>> a.hasError
    True
    ```

    ```python
    >>> b = metadata.Date(
    ...     year=1843,
    ...     month=3,
    ...     day=3,
    ...     minute=3,
    ...     )
    >>> b.hasError
    False
    ```

Date.hasTime
:   Return True if any time elements are defined:

    ```python
    >>> a = metadata.Date(year=1843, month=3, day=3)
    >>> a.hasTime
    False
    ```

    ```python
    >>> b = metadata.Date(year=1843, month=3, day=3, minute=3)
    >>> b.hasTime
    True
    ```

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`Date`](#music21.metadata.primitives.Date "music21.metadata.primitives.Date") methods

Date.\_\_eq\_\_(*other*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/metadata/primitives.html#Date.__eq__)
:   Return self==value.

static Date.errorToSymbol(*value*)[[source]](../_modules/music21/metadata/primitives.html#Date.errorToSymbol)
:   Convert an error string (approximate, uncertain) into a symbol.

    ```python
    >>> metadata.Date.errorToSymbol('approximate')
    '~'
    ```

    ```python
    >>> metadata.Date.errorToSymbol('uncertain')
    '?'
    ```

Date.load(*value: [Date](#music21.metadata.primitives.Date "music21.metadata.primitives.Date") | [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*)[[source]](../_modules/music21/metadata/primitives.html#Date.load)
:   Load values by string, datetime object, or Date object:

    ```python
    >>> a = metadata.Date(year=1843, month=3, day=3)
    >>> b = metadata.Date()
    >>> b.load(a)
    >>> b.year
    1843
    ```

    If there is an error, a ValueError is raised, but the
    incorrect values are retained:

    ```python
    >>> d = metadata.Date()
    >>> d.load('1999/14/32/25:60:61')
    Traceback (most recent call last):
    ValueError: Month must be between 1 and 12, not 14.
    >>> str(d)
    '1999/14/32/25:60:61'
    ```

Date.loadDatetime(*dt: [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/metadata/primitives.html#Date.loadDatetime)
:   Load time data from a datetime object:

    ```python
    >>> import datetime
    >>> dt = datetime.datetime(2005, 2, 1)
    >>> dt
    datetime.datetime(2005, 2, 1, 0, 0)
    ```

    ```python
    >>> m21mdDate = metadata.Date()
    >>> m21mdDate.loadDatetime(dt)
    >>> str(m21mdDate)
    '2005/02/01'
    ```

Date.loadOther(*other: [Date](#music21.metadata.primitives.Date "music21.metadata.primitives.Date")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/metadata/primitives.html#Date.loadOther)
:   Load values based on another Date object. (the “Other” in “loadOther”
    means another Date object, not just anything.

    ```python
    >>> a = metadata.Date(year=1843, month=3, day=3, yearError='approximate')
    >>> b = metadata.Date()
    >>> b.loadOther(a)
    >>> b.year
    1843
    >>> b.yearError
    'approximate'
    ```

Date.loadStr(*dateStr: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/metadata/primitives.html#Date.loadStr)
:   Load a string date representation, which might have approximate
    symbols.

    Assume year/month/day/hour:minute:second:

    ```python
    >>> d = metadata.Date()
    >>> d.loadStr('1030?/12~/?4')
    >>> d.month, d.monthError
    (12, 'approximate')
    ```

    ```python
    >>> d.year, d.yearError
    (1030, 'uncertain')
    ```

    ```python
    >>> d.month, d.monthError
    (12, 'approximate')
    ```

    ```python
    >>> d.day, d.dayError
    (4, 'uncertain')
    ```

    ```python
    >>> d = metadata.Date()
    >>> d.loadStr('1834/12/4/4:50:32')
    >>> d.minute, d.second
    (50, 32)
    ```

## DateSingle

class music21.metadata.primitives.DateSingle(*data: [Date](#music21.metadata.primitives.Date "music21.metadata.primitives.Date") | [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*, *relevance='certain'*)[[source]](../_modules/music21/metadata/primitives.html#DateSingle)
:   Store a date, either as certain, approximate, or uncertain relevance.

    The relevance attribute is limited within each DateSingle subclass
    depending on the design of the class. Alternative relevance types should be
    configured as other DateSingle subclasses.

    ```python
    >>> dd = metadata.DateSingle('2009/12/31', 'approximate')
    >>> dd
    <music21.metadata.primitives.DateSingle 2009/12/31>
    ```

    ```python
    >>> str(dd)
    '2009/12/31'
    ```

    ```python
    >>> dd.relevance
    'approximate'
    ```

    ```python
    >>> dd = metadata.DateSingle('1805/3/12', 'uncertain')
    >>> str(dd)
    '1805/03/12'
    ```

[`DateSingle`](#music21.metadata.primitives.DateSingle "music21.metadata.primitives.DateSingle") bases

* [`DatePrimitive`](#music21.metadata.primitives.DatePrimitive "music21.metadata.primitives.DatePrimitive")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`DateSingle`](#music21.metadata.primitives.DateSingle "music21.metadata.primitives.DateSingle") read-only properties

Read-only properties inherited from [`DatePrimitive`](#music21.metadata.primitives.DatePrimitive "music21.metadata.primitives.DatePrimitive"):

|  |  |  |
| --- | --- | --- |
| * [`datetime`](#music21.metadata.primitives.DatePrimitive.datetime "music21.metadata.primitives.DatePrimitive.datetime") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`DateSingle`](#music21.metadata.primitives.DateSingle "music21.metadata.primitives.DateSingle") read/write properties

Read/write properties inherited from [`DatePrimitive`](#music21.metadata.primitives.DatePrimitive "music21.metadata.primitives.DatePrimitive"):

|  |  |  |
| --- | --- | --- |
| * [`relevance`](#music21.metadata.primitives.DatePrimitive.relevance "music21.metadata.primitives.DatePrimitive.relevance") |  |  |

[`DateSingle`](#music21.metadata.primitives.DateSingle "music21.metadata.primitives.DateSingle") methods

Methods inherited from [`DatePrimitive`](#music21.metadata.primitives.DatePrimitive "music21.metadata.primitives.DatePrimitive"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](#music21.metadata.primitives.DatePrimitive.__eq__ "music21.metadata.primitives.DatePrimitive.__eq__") |  |  |

## DateRelative

class music21.metadata.primitives.DateRelative(*data: [Date](#music21.metadata.primitives.Date "music21.metadata.primitives.Date") | [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*, *relevance='after'*)[[source]](../_modules/music21/metadata/primitives.html#DateRelative)
:   Store a relative date, sometime prior or sometime after, onorbefore, or onorafter`.

    ```python
    >>> dd = metadata.DateRelative('2009/12/31', 'prior')
    >>> str(dd)
    'prior to 2009/12/31'
    >>> dd.relevance = 'after'
    >>> str(dd)
    'after 2009/12/31'
    ```

    ```python
    >>> dd = metadata.DateRelative('2009/12/31', 'certain')
    Traceback (most recent call last):
    music21.exceptions21.MetadataException: Relevance value is not
        supported by this object: 'certain'
    ```

[`DateRelative`](#music21.metadata.primitives.DateRelative "music21.metadata.primitives.DateRelative") bases

* [`DatePrimitive`](#music21.metadata.primitives.DatePrimitive "music21.metadata.primitives.DatePrimitive")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`DateRelative`](#music21.metadata.primitives.DateRelative "music21.metadata.primitives.DateRelative") read-only properties

Read-only properties inherited from [`DatePrimitive`](#music21.metadata.primitives.DatePrimitive "music21.metadata.primitives.DatePrimitive"):

|  |  |  |
| --- | --- | --- |
| * [`datetime`](#music21.metadata.primitives.DatePrimitive.datetime "music21.metadata.primitives.DatePrimitive.datetime") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`DateRelative`](#music21.metadata.primitives.DateRelative "music21.metadata.primitives.DateRelative") read/write properties

DateRelative.relevance
:   The relevance attribute takes one of four
    values, ‘prior’, ‘after’, or
    ‘onorbefore’ or ‘onorafter’.

[`DateRelative`](#music21.metadata.primitives.DateRelative "music21.metadata.primitives.DateRelative") methods

Methods inherited from [`DatePrimitive`](#music21.metadata.primitives.DatePrimitive "music21.metadata.primitives.DatePrimitive"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](#music21.metadata.primitives.DatePrimitive.__eq__ "music21.metadata.primitives.DatePrimitive.__eq__") |  |  |

## DateBetween

class music21.metadata.primitives.DateBetween(*data: [Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "(in Python v3.14)")[[Date](#music21.metadata.primitives.Date "music21.metadata.primitives.Date") | [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] = ()*, *relevance='between'*)[[source]](../_modules/music21/metadata/primitives.html#DateBetween)
:   Store a relative date, sometime between two dates:

    ```python
    >>> dd = metadata.DateBetween(['2009/12/31', '2010/1/28'])
    >>> str(dd)
    '2009/12/31 to 2010/01/28'
    ```

    ```python
    >>> dd = metadata.DateBetween(['2009/12/31', '2010/1/28'], 'certain')
    Traceback (most recent call last):
    music21.exceptions21.MetadataException: Relevance value is not
        supported by this object: 'certain'
    ```

    ```python
    >>> d1 = metadata.Date(year=1605)
    >>> d2 = metadata.Date(year=1608, month='11?')
    >>> dd = metadata.DateBetween([d1, d2])
    >>> str(dd)
    '1605/--/-- to 1608/11?/--'
    ```

[`DateBetween`](#music21.metadata.primitives.DateBetween "music21.metadata.primitives.DateBetween") bases

* [`DatePrimitive`](#music21.metadata.primitives.DatePrimitive "music21.metadata.primitives.DatePrimitive")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`DateBetween`](#music21.metadata.primitives.DateBetween "music21.metadata.primitives.DateBetween") read-only properties

Read-only properties inherited from [`DatePrimitive`](#music21.metadata.primitives.DatePrimitive "music21.metadata.primitives.DatePrimitive"):

|  |  |  |
| --- | --- | --- |
| * [`datetime`](#music21.metadata.primitives.DatePrimitive.datetime "music21.metadata.primitives.DatePrimitive.datetime") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`DateBetween`](#music21.metadata.primitives.DateBetween "music21.metadata.primitives.DateBetween") read/write properties

DateBetween.relevance
:   The relevance attribute takes only one value:
    ‘between’.

[`DateBetween`](#music21.metadata.primitives.DateBetween "music21.metadata.primitives.DateBetween") methods

Methods inherited from [`DatePrimitive`](#music21.metadata.primitives.DatePrimitive "music21.metadata.primitives.DatePrimitive"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](#music21.metadata.primitives.DatePrimitive.__eq__ "music21.metadata.primitives.DatePrimitive.__eq__") |  |  |

## DateSelection

class music21.metadata.primitives.DateSelection(*data: [Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "(in Python v3.14)")[[Date](#music21.metadata.primitives.Date "music21.metadata.primitives.Date") | [datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] = ()*, *relevance='or'*)[[source]](../_modules/music21/metadata/primitives.html#DateSelection)
:   Store a selection of dates, or a collection of dates that might all be
    possible

    ```python
    >>> dd = metadata.DateSelection(
    ...     ['2009/12/31', '2010/1/28', '1894/1/28'],
    ...     )
    >>> str(dd)
    '2009/12/31 or 2010/01/28 or 1894/01/28'
    ```

    ```python
    >>> dd = metadata.DateSelection(
    ...     [1750, '1775/03?'],
    ...     'and'
    ...     )
    >>> str(dd)
    '1750/--/-- and 1775/03?/--'
    ```

    ```python
    >>> dd = metadata.DateSelection(
    ...     ['2009/12/31', '2010/1/28'],
    ...     'certain',
    ...     )
    Traceback (most recent call last):
    music21.exceptions21.MetadataException: Relevance value is not
        supported by this object: 'certain'
    ```

    Note that ‘1350 or 1351 and 1375’ is not supported yet.

[`DateSelection`](#music21.metadata.primitives.DateSelection "music21.metadata.primitives.DateSelection") bases

* [`DatePrimitive`](#music21.metadata.primitives.DatePrimitive "music21.metadata.primitives.DatePrimitive")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`DateSelection`](#music21.metadata.primitives.DateSelection "music21.metadata.primitives.DateSelection") read-only properties

Read-only properties inherited from [`DatePrimitive`](#music21.metadata.primitives.DatePrimitive "music21.metadata.primitives.DatePrimitive"):

|  |  |  |
| --- | --- | --- |
| * [`datetime`](#music21.metadata.primitives.DatePrimitive.datetime "music21.metadata.primitives.DatePrimitive.datetime") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`DateSelection`](#music21.metadata.primitives.DateSelection "music21.metadata.primitives.DateSelection") read/write properties

DateSelection.relevance
:   The relevance attribute takes only two values:
    ‘or’ or ‘and’.

[`DateSelection`](#music21.metadata.primitives.DateSelection "music21.metadata.primitives.DateSelection") methods

Methods inherited from [`DatePrimitive`](#music21.metadata.primitives.DatePrimitive "music21.metadata.primitives.DatePrimitive"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](#music21.metadata.primitives.DatePrimitive.__eq__ "music21.metadata.primitives.DatePrimitive.__eq__") |  |  |

## Contributor

class music21.metadata.primitives.Contributor(*\**, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Text](#music21.metadata.primitives.Text "music21.metadata.primitives.Text") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *names: [Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Text](#music21.metadata.primitives.Text "music21.metadata.primitives.Text")] = ()*, *role: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Text](#music21.metadata.primitives.Text "music21.metadata.primitives.Text") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *birth: [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [DateSingle](#music21.metadata.primitives.DateSingle "music21.metadata.primitives.DateSingle") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = None*, *death: [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [DateSingle](#music21.metadata.primitives.DateSingle "music21.metadata.primitives.DateSingle") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = None*, *\*\*keywords*)[[source]](../_modules/music21/metadata/primitives.html#Contributor)
:   A person that contributed to a work. Can be a composer, lyricist, arranger,
    or other type of contributor. In MusicXML, these are “creator” elements.

    ```python
    >>> td = metadata.Contributor(role='composer', name='Chopin, Fryderyk')
    >>> td.role
    'composer'
    ```

    ```python
    >>> td.name
    'Chopin, Fryderyk'
    ```

    ```python
    >>> td.relevance
    'contributor'
    ```

    ```python
    >>> td
    <music21.metadata.primitives.Contributor composer:Chopin, Fryderyk>
    ```

[`Contributor`](#music21.metadata.primitives.Contributor "music21.metadata.primitives.Contributor") bases

* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`Contributor`](#music21.metadata.primitives.Contributor "music21.metadata.primitives.Contributor") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`Contributor`](#music21.metadata.primitives.Contributor "music21.metadata.primitives.Contributor") read/write properties

Contributor.name
:   Returns the text name, or the first of many names entered.

    ```python
    >>> td = metadata.Contributor(
    ...     role='composer',
    ...     names=['Chopin, Fryderyk', 'Chopin, Frederick'],
    ...     )
    >>> td.name
    'Chopin, Fryderyk'
    ```

    ```python
    >>> td.names
    ['Chopin, Fryderyk', 'Chopin, Frederick']
    ```

Contributor.names
:   Returns all names in a list.

    ```python
    >>> td = metadata.Contributor(
    ...     role='composer',
    ...     names=['Chopin, Fryderyk', 'Chopin, Frederick'],
    ...     )
    >>> td.names
    ['Chopin, Fryderyk', 'Chopin, Frederick']
    ```

    ```python
    >>> td.names = ['Czerny', 'Spohr']
    >>> td.names
    ['Czerny', 'Spohr']
    ```

Contributor.role
:   The role is what part this Contributor plays in the work. Both
    full roll strings and roll abbreviations may be used.

    ```python
    >>> td = metadata.Contributor()
    >>> td.role = 'composer'
    >>> td.role
    'composer'
    ```

    In case of a Humdrum role abbreviation, the role that is set
    is the full name:

    ```python
    >>> td.role = 'lor'
    >>> td.role
    'orchestrator'
    ```

    Roles can be created on the fly:

    ```python
    >>> td.role = 'court jester'
    >>> td.role
    'court jester'
    ```

[`Contributor`](#music21.metadata.primitives.Contributor "music21.metadata.primitives.Contributor") methods

Contributor.\_\_eq\_\_(*other*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/metadata/primitives.html#Contributor.__eq__)
:   ```python
    >>> c1 = metadata.Contributor(
    ...         role='composer',
    ...         name='The Composer',
    ...         birth='1923',
    ...         death='2013'
    ... )
    >>> c2 = metadata.Contributor(
    ...         role='composer',
    ...         name='The Composer',
    ...         birth='1923',
    ...         death='2013'
    ... )
    ```

    Names, role, birth, and death must all be identical for equality.

    ```python
    >>> c1 == c2
    True
    >>> c2.role = 'lyricist'
    >>> c1 == c2
    False
    >>> c2 = metadata.Contributor(
    ...         role='composer',
    ...         name='A Composer',
    ...         birth='1923',
    ...         death='2013'
    ... )
    >>> c1 == c2
    False
    >>> c2 = metadata.Contributor(
    ...         role='composer',
    ...         names=['A Composer', 'The Composer'],
    ...         birth='1923',
    ...         death='2013'
    ... )
    >>> c1 == c2
    False
    >>> c2 = metadata.Contributor(
    ...         role='composer',
    ...         name='The Composer',
    ...         birth='1924',
    ...         death='2013'
    ... )
    >>> c1 == c2
    False
    >>> c2 = metadata.Contributor(
    ...         role='composer',
    ...         name='The Composer',
    ...         birth='1923',
    ...         death='2012'
    ... )
    >>> c1 == c2
    False
    ```

    Comparison with a non-Contributor object always returns False.

    ```python
    >>> c1 == 'The Composer'
    False
    ```

static Contributor.abbreviationToRole(*abbreviation*)[[source]](../_modules/music21/metadata/primitives.html#Contributor.abbreviationToRole)
:   Convert abbreviation to role name:

    ```python
    >>> metadata.Contributor.abbreviationToRole('com')
    'composer'
    ```

    ```python
    >>> metadata.Contributor.abbreviationToRole('lib')
    'librettist'
    ```

Contributor.age() → [timedelta](https://docs.python.org/3/library/datetime.html#datetime.timedelta "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/metadata/primitives.html#Contributor.age)
:   Calculate the age at death of the Contributor, returning a
    datetime.timedelta object.

    ```python
    >>> a = metadata.Contributor(
    ...     name='Beethoven, Ludwig van',
    ...     role='composer',
    ...     birth='1770/12/17',
    ...     death='1827/3/26',
    ...     )
    ```

    ```python
    >>> a.birth
    <music21.metadata.primitives.DateSingle 1770/12/17>
    ```

    ```python
    >>> a.age()
    datetime.timedelta(days=20552)
    ```

    ```python
    >>> a.age().days
    20552
    ```

    ```python
    >>> years = a.age().days // 365
    >>> years
    56
    ```

    If the composer is still alive, it returns the composer’s current age.

    ```python
    >>> shaw = metadata.Contributor(
    ...     name='Shaw, Caroline',
    ...     role='composer',
    ...     birth='1982/08/01',
    ...     )
    >>> shaw_years = shaw.age().days // 365
    ```

    This test will fail in 2067:

    ```python
    >>> 36 < shaw_years < 85
    True
    ```

static Contributor.roleToAbbreviation(*roleName*)[[source]](../_modules/music21/metadata/primitives.html#Contributor.roleToAbbreviation)
:   Convert roleName to role abbreviation:

    ```python
    >>> metadata.Contributor.roleToAbbreviation('composer')
    'com'
    ```

## Copyright

class music21.metadata.primitives.Copyright(*data: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Text](#music21.metadata.primitives.Text "music21.metadata.primitives.Text") = ''*, *language: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *isTranslated: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\**, *role=None*)[[source]](../_modules/music21/metadata/primitives.html#Copyright)
:   A subclass of text that can also have a role

    ```python
    >>> c = metadata.primitives.Copyright('Copyright 1945 Florence Price')
    >>> c
    <music21.metadata.primitives.Copyright Copyright 1945 Florence Price>
    >>> c.role is None
    True
    >>> str(c)
    'Copyright 1945 Florence Price'
    ```

    The text, language, isTranslated, role, etc. must be identical for equality.

    ```python
    >>> c2 = metadata.Copyright('Copyright 1945 Florence Price')
    >>> c == c2
    True
    >>> c2 = metadata.Copyright('Copyright © 1945 Florence Price')
    >>> c == c2
    False
    >>> c2 = metadata.Copyright('Copyright 1945 Florence Price', language='en')
    >>> c == c2
    False
    >>> c2 = metadata.Copyright('Copyright 1945 Florence Price', isTranslated=True)
    >>> c == c2
    False
    >>> c2 = metadata.Copyright('Copyright 1945 Florence Price', role='other')
    >>> c == c2
    False
    ```

    Comparison against a non-Copyright object will always return False.

    ```python
    >>> c == 1945
    False
    ```

[`Copyright`](#music21.metadata.primitives.Copyright "music21.metadata.primitives.Copyright") bases

* [`Text`](#music21.metadata.primitives.Text "music21.metadata.primitives.Text")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`Copyright`](#music21.metadata.primitives.Copyright "music21.metadata.primitives.Copyright") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`Copyright`](#music21.metadata.primitives.Copyright "music21.metadata.primitives.Copyright") read/write properties

Read/write properties inherited from [`Text`](#music21.metadata.primitives.Text "music21.metadata.primitives.Text"):

|  |  |  |
| --- | --- | --- |
| * [`language`](#music21.metadata.primitives.Text.language "music21.metadata.primitives.Text.language") |  |  |

[`Copyright`](#music21.metadata.primitives.Copyright "music21.metadata.primitives.Copyright") methods

Copyright.\_\_eq\_\_(*other*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/metadata/primitives.html#Copyright.__eq__)
:   ```python
    >>> t1 = metadata.Text('some text')
    >>> t2 = metadata.Text('some text')
    >>> t1 == t2
    True
    ```

    Language, isTranslated, and encodingScheme must all exactly match for equality.

    ```python
    >>> t2 = metadata.Text('some text', language='en')
    >>> t1 == t2
    False
    >>> t2 = metadata.Text('some text', isTranslated=True)
    >>> t1 == t2
    False
    >>> t2 = metadata.Text('some text', encodingScheme='scheme42')
    >>> t1 == t2
    False
    ```

    Comparison with non-Text types, including bare strings,
    will always be considered unequal.

    ```python
    >>> t1 == 'some text'
    False
    ```

Methods inherited from [`Text`](#music21.metadata.primitives.Text "music21.metadata.primitives.Text"):

|  |  |  |
| --- | --- | --- |
| * [`getNormalizedArticle()`](#music21.metadata.primitives.Text.getNormalizedArticle "music21.metadata.primitives.Text.getNormalizedArticle") |  |  |

## Creator

class music21.metadata.primitives.Creator(*\**, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Text](#music21.metadata.primitives.Text "music21.metadata.primitives.Text") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *names: [Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Text](#music21.metadata.primitives.Text "music21.metadata.primitives.Text")] = ()*, *role: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Text](#music21.metadata.primitives.Text "music21.metadata.primitives.Text") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *birth: [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [DateSingle](#music21.metadata.primitives.DateSingle "music21.metadata.primitives.DateSingle") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = None*, *death: [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [DateSingle](#music21.metadata.primitives.DateSingle "music21.metadata.primitives.DateSingle") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = None*, *\*\*keywords*)[[source]](../_modules/music21/metadata/primitives.html#Creator)
:   A person that created a work. Can be a composer, lyricist, arranger, or
    other type of contributor.

    In MusicXML, these are “creator” elements.

    ```python
    >>> td = metadata.Creator(role='composer', name='Chopin, Fryderyk')
    >>> td.role
    'composer'
    ```

    ```python
    >>> td.name
    'Chopin, Fryderyk'
    ```

    ```python
    >>> td.relevance
    'creator'
    ```

[`Creator`](#music21.metadata.primitives.Creator "music21.metadata.primitives.Creator") bases

* [`Contributor`](#music21.metadata.primitives.Contributor "music21.metadata.primitives.Contributor")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`Creator`](#music21.metadata.primitives.Creator "music21.metadata.primitives.Creator") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`Creator`](#music21.metadata.primitives.Creator "music21.metadata.primitives.Creator") read/write properties

Read/write properties inherited from [`Contributor`](#music21.metadata.primitives.Contributor "music21.metadata.primitives.Contributor"):

|  |  |  |
| --- | --- | --- |
| * [`name`](#music21.metadata.primitives.Contributor.name "music21.metadata.primitives.Contributor.name") | * [`names`](#music21.metadata.primitives.Contributor.names "music21.metadata.primitives.Contributor.names") | * [`role`](#music21.metadata.primitives.Contributor.role "music21.metadata.primitives.Contributor.role") |

[`Creator`](#music21.metadata.primitives.Creator "music21.metadata.primitives.Creator") methods

Methods inherited from [`Contributor`](#music21.metadata.primitives.Contributor "music21.metadata.primitives.Contributor"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](#music21.metadata.primitives.Contributor.__eq__ "music21.metadata.primitives.Contributor.__eq__") * [`abbreviationToRole()`](#music21.metadata.primitives.Contributor.abbreviationToRole "music21.metadata.primitives.Contributor.abbreviationToRole") | * [`age()`](#music21.metadata.primitives.Contributor.age "music21.metadata.primitives.Contributor.age") | * [`roleToAbbreviation()`](#music21.metadata.primitives.Contributor.roleToAbbreviation "music21.metadata.primitives.Contributor.roleToAbbreviation") |

## DatePrimitive

class music21.metadata.primitives.DatePrimitive(*relevance: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = 'certain'*)[[source]](../_modules/music21/metadata/primitives.html#DatePrimitive)
:   A default class for all date objects, which can have different types
    and different “relevance” values.

    Note that the interaction between uncertainty on an entire DatePrimitive object
    vs uncertainty on a particular Date value, like month, is ill-defined
    and needs work.

[`DatePrimitive`](#music21.metadata.primitives.DatePrimitive "music21.metadata.primitives.DatePrimitive") bases

* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`DatePrimitive`](#music21.metadata.primitives.DatePrimitive "music21.metadata.primitives.DatePrimitive") read-only properties

DatePrimitive.datetime
:   Get a datetime object.

    ```python
    >>> a = metadata.DateSingle('1843/03/03')
    >>> str(a)
    '1843/03/03'
    ```

    ```python
    >>> a.datetime
    datetime.datetime(1843, 3, 3, 0, 0)
    ```

    ```python
    >>> a = metadata.DateSingle('1843/03')
    >>> str(a)
    '1843/03/--'
    ```

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`DatePrimitive`](#music21.metadata.primitives.DatePrimitive "music21.metadata.primitives.DatePrimitive") read/write properties

DatePrimitive.relevance
:   The relevance attribute takes one of three
    values, ‘certain’, ‘approximate’, or
    ‘uncertain’.

[`DatePrimitive`](#music21.metadata.primitives.DatePrimitive "music21.metadata.primitives.DatePrimitive") methods

DatePrimitive.\_\_eq\_\_(*other*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/metadata/primitives.html#DatePrimitive.__eq__)
:   ```python
    >>> dd = metadata.DateSingle('1805/3/12', 'uncertain')
    >>> dd2 = metadata.DateSingle('1805/3/12', 'uncertain')
    >>> str(dd)
    '1805/03/12'
    >>> dd == dd2
    True
    >>> dd2.relevance='certain'
    >>> dd == dd2
    False
    ```

## Imprint

class music21.metadata.primitives.Imprint(*\*\*keywords*)[[source]](../_modules/music21/metadata/primitives.html#Imprint)
:   An object representation of imprint, or publication.

[`Imprint`](#music21.metadata.primitives.Imprint "music21.metadata.primitives.Imprint") bases

* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`Imprint`](#music21.metadata.primitives.Imprint "music21.metadata.primitives.Imprint") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |
