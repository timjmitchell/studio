Source: https://music21.org/music21docs/moduleReference/moduleStreamEnums.html

# music21.stream.enums

## GivenElementsBehavior

class music21.stream.enums.GivenElementsBehavior(*\*values*)[[source]](../_modules/music21/stream/enums.html#GivenElementsBehavior)

[`GivenElementsBehavior`](#music21.stream.enums.GivenElementsBehavior "music21.stream.enums.GivenElementsBehavior") bases

* [`StrEnum`](moduleCommonEnums.html#music21.common.enums.StrEnum "music21.common.enums.StrEnum")

## RecursionType

class music21.stream.enums.RecursionType(*\*values*)[[source]](../_modules/music21/stream/enums.html#RecursionType)

[`RecursionType`](#music21.stream.enums.RecursionType "music21.stream.enums.RecursionType") bases

* [`StrEnum`](moduleCommonEnums.html#music21.common.enums.StrEnum "music21.common.enums.StrEnum")

## ShowNumber

class music21.stream.enums.ShowNumber(*\*values*)[[source]](../_modules/music21/stream/enums.html#ShowNumber)

[`ShowNumber`](#music21.stream.enums.ShowNumber "music21.stream.enums.ShowNumber") bases

* [`StrEnum`](moduleCommonEnums.html#music21.common.enums.StrEnum "music21.common.enums.StrEnum")

## StaffType

class music21.stream.enums.StaffType(*\*values*)[[source]](../_modules/music21/stream/enums.html#StaffType)
:   These are the same as MusicXML staff-type, except uppercase and “other”
    which reflects any other type. Probably the best way of using “other”
    is to designate what it means with a .editorial.staffTypeExplanation = ‘other’

    ```python
    >>> stream.enums.StaffType.OSSIA
    <StaffType.OSSIA: 'ossia'>
    ```

    To get the musicxml name:

    ```python
    >>> stream.enums.StaffType.OSSIA.value
    'ossia'
    ```

    ```python
    >>> stream.enums.StaffType('cue')
    <StaffType.CUE: 'cue'>
    ```

    ```python
    >>> stream.enums.StaffType('tiny')
    Traceback (most recent call last):
    ValueError: 'tiny' is not a valid StaffType
    ```
