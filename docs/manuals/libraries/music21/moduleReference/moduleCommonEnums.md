Source: https://music21.org/music21docs/moduleReference/moduleCommonEnums.html

# music21.common.enums

## AppendSpanners

class music21.common.enums.AppendSpanners(*\*values*)[[source]](../_modules/music21/common/enums.html#AppendSpanners)
:   An enumeration for how to append related spanners when appending objects to a written file.

    AppendSpanners.NORMAL means append the spanners that start with the object, then append
    :   the object, then append the spanners that end with the object.

    AppendSpanners.RELATED\_ONLY means append the spanners that start with the object, then
    :   append the spanners that end with the object (i.e. do not append the object).

    AppendSpanners.NONE means do not append the related spanners at all (i.e. only append
    :   the object).

    * New in v9.

[`AppendSpanners`](#music21.common.enums.AppendSpanners "music21.common.enums.AppendSpanners") bases

* [`StrEnum`](#music21.common.enums.StrEnum "music21.common.enums.StrEnum")

## BooleanEnum

class music21.common.enums.BooleanEnum(*new\_class\_name*, */*, *names*, *\**, *module=None*, *qualname=None*, *type=None*, *start=1*, *boundary=None*)[[source]](../_modules/music21/common/enums.html#BooleanEnum)
:   An enum that replaces a boolean, except the “is” part, and
    allows specifying multiple values that can specify whether they
    equate to True or False.

    Useful for taking an element that was previously True/False and
    replacing it in a backwards-compatible way with an Enum.

    ```python
    >>> from music21.common.enums import BooleanEnum
    >>> class Maybe(BooleanEnum):
    ...    YES = True
    ...    NO = False
    ...    MAYBE = 0.5
    ...    NOT_A_CHANCE = (False, 'not a chance')
    ...    DEFINITELY = (True, 'of course!')
    >>> bool(Maybe.YES)
    True
    >>> bool(Maybe.NO)
    False
    >>> bool(Maybe.MAYBE)
    True
    >>> bool(Maybe.NOT_A_CHANCE)
    False
    >>> bool(Maybe.DEFINITELY)
    True
    >>> Maybe.MAYBE == 0.5
    True
    >>> Maybe.NOT_A_CHANCE == 'not a chance'
    True
    >>> Maybe.NOT_A_CHANCE == False
    True
    >>> Maybe.NOT_A_CHANCE == True
    False
    >>> Maybe.NOT_A_CHANCE == 'not any chance'
    False
    >>> Maybe.DEFINITELY == 'of course!'
    True
    >>> Maybe.NOT_A_CHANCE == (False, 'not a chance')
    True
    ```

## ContainsEnum

class music21.common.enums.ContainsEnum(*new\_class\_name*, */*, *names*, *\**, *module=None*, *qualname=None*, *type=None*, *start=1*, *boundary=None*)[[source]](../_modules/music21/common/enums.html#ContainsEnum)
:   An IntEnum that allows “in” checks against the values of the enum.

## ContainsMeta

class music21.common.enums.ContainsMeta(*cls*, *bases*, *classdict*, *\**, *boundary=None*, *\_simple=False*, *\*\*kwds*)[[source]](../_modules/music21/common/enums.html#ContainsMeta)
:   This is a backport of the Python 3.12 EnumType class’s contains method.

    This will be removed when Python 3.12 is the minimum version for music21.

## ElementSearch

class music21.common.enums.ElementSearch(*\*values*)[[source]](../_modules/music21/common/enums.html#ElementSearch)
:   An enum representing the element search directions that can be provided
    to [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass").

[`ElementSearch`](#music21.common.enums.ElementSearch "music21.common.enums.ElementSearch") bases

* [`StrEnum`](#music21.common.enums.StrEnum "music21.common.enums.StrEnum")

## GatherSpanners

class music21.common.enums.GatherSpanners(*\*values*)[[source]](../_modules/music21/common/enums.html#GatherSpanners)
:   An enumeration for how to gather missing spanners

    ```python
    >>> from music21.common.enums import GatherSpanners
    ```

    Indicates all relevant spanners will be gathered:

    ```python
    >>> GatherSpanners.ALL
    <GatherSpanners.ALL>
    >>> bool(GatherSpanners.ALL)
    True
    ```

    Indicates no relevant spanners will be gathered:

    ```python
    >>> GatherSpanners.NONE
    <GatherSpanners.NONE>
    >>> bool(GatherSpanners.NONE)
    False
    ```

    Indicates only spanners where all of their members are in the excerpt
    will be gathered:

    ```python
    >>> GatherSpanners.COMPLETE_ONLY
    <GatherSpanners.COMPLETE_ONLY>
    >>> bool(GatherSpanners.COMPLETE_ONLY)
    True
    ```

[`GatherSpanners`](#music21.common.enums.GatherSpanners "music21.common.enums.GatherSpanners") bases

* [`BooleanEnum`](#music21.common.enums.BooleanEnum "music21.common.enums.BooleanEnum")

## MeterDivision

class music21.common.enums.MeterDivision(*\*values*)[[source]](../_modules/music21/common/enums.html#MeterDivision)
:   Represents an indication of how to divide a TimeSignature

    * New in v7.

[`MeterDivision`](#music21.common.enums.MeterDivision "music21.common.enums.MeterDivision") bases

* [`StrEnum`](#music21.common.enums.StrEnum "music21.common.enums.StrEnum")

## OffsetSpecial

class music21.common.enums.OffsetSpecial(*\*values*)[[source]](../_modules/music21/common/enums.html#OffsetSpecial)
:   An enum that represents special offsets.

    The enum AT\_END is equal to the string ‘highestTime’

    ```python
    >>> from music21.common.enums import OffsetSpecial
    >>> OffsetSpecial.AT_END
    <OffsetSpecial.AT_END>
    >>> 'highestTime' == OffsetSpecial.AT_END
    True
    >>> 'crazyOffset' in OffsetSpecial
    False
    >>> 6.0 in OffsetSpecial
    False
    >>> 'lowestOffset' in OffsetSpecial
    True
    >>> str(OffsetSpecial.AT_END)
    'highestTime'
    ```

    * New in v7.
    * Note – a previous note said that the ‘highestTime’ == OffsetSpecial.AT\_END
      would be removed in v9 or an upcoming music21 release. Since then, Python has
      changed direction and in 3.11 added StrEnum to the standard library and in 3.12
      allows for containment checks of strings in StrEnum (such as
      ‘lowestOffset’ in OffsetSpecial returning True). Therefore there is no
      reason for music21 to ever remove this valuable and backwards compatible
      tool.

[`OffsetSpecial`](#music21.common.enums.OffsetSpecial "music21.common.enums.OffsetSpecial") bases

* [`StrEnum`](#music21.common.enums.StrEnum "music21.common.enums.StrEnum")

## OrnamentDelay

class music21.common.enums.OrnamentDelay(*\*values*)[[source]](../_modules/music21/common/enums.html#OrnamentDelay)
:   An enumeration for the delay in an ornament (e.g. a delayed turn). The delay for an
    ornament can be set to one of these values, or to an OffsetQL for a timed delay.

    OrnamentDelay.NO\_DELAY means there is no delay (this is equivalent to setting delay to 0.0)
    OrnamentDelay.DEFAULT\_DELAY means the delay is half the duration of the ornamented note.

    * New in v9.

[`OrnamentDelay`](#music21.common.enums.OrnamentDelay "music21.common.enums.OrnamentDelay") bases

* [`StrEnum`](#music21.common.enums.StrEnum "music21.common.enums.StrEnum")

## StrEnum

class music21.common.enums.StrEnum(*new\_class\_name*, */*, *names*, *\**, *module=None*, *qualname=None*, *type=None*, *start=1*, *boundary=None*)[[source]](../_modules/music21/common/enums.html#StrEnum)
:   An enumeration where strings can equal the value, and strings
    can be found “in” the enum.

    See [`music21.common.enums.OffsetSpecial`](#music21.common.enums.OffsetSpecial "music21.common.enums.OffsetSpecial") for an
    example of how subclassing this would work.

    * Note: This class predates the equivalent StrEnum in Python 3.11
      and the changes to Enum \_\_contains\_\_ in 3.12. Once
      Python 3.12 is the minimum version of music21, this class
      will no longer be used internally and will eventually become
      deprecated (2027?) and removed (2030?).

## StrEnumMeta

class music21.common.enums.StrEnumMeta(*cls*, *bases*, *classdict*, *\**, *boundary=None*, *\_simple=False*, *\*\*kwds*)[[source]](../_modules/music21/common/enums.html#StrEnumMeta)
