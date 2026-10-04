Source: https://music21.org/music21docs/moduleReference/moduleTie.html

# music21.tie

The tie module contains a single class, Tie that represents the visual and
conceptual idea of tied notes. They can be start or stop ties.

## Tie

class music21.tie.Tie(*type='start'*)[[source]](../_modules/music21/tie.html#Tie)
:   An object added to Notes that are tied to other notes. The type value is one
    of start, stop, or continue.

    ```python
    >>> note1 = note.Note()
    >>> note1.tie = tie.Tie('start')  # start, stop, or continue
    >>> note1.tie.style = 'normal'  # default; could also be 'dotted' or 'dashed' or 'hidden'
    >>> note1.tie.type
    'start'
    ```

    ```python
    >>> note1.tie
    <music21.tie.Tie start>
    ```

    Generally Ties have a placement of None, but if they are defined
    as ‘above’ or ‘below’ this will be retained. (see: [this discussion](https://web.archive.org/web/20210302051136/https://forums.makemusic.com/viewtopic.php?f=12&t=2179&start=0)
    for how orientation and placement in musicxml are essentially the same
    content).

    ```python
    >>> note1.tie.placement is None
    True
    ```

    Differences from MusicXML:

    * notes do not need to know if they are tied from a
      previous note. i.e., you can tie n1 to n2 just with
      a tie start on n1. However, if you want proper musicXML output
      you need a tie stop on n2.
    * one tie with “continue” implies tied from and tied to.

    The tie.style only applies to Tie objects of type ‘start’ or ‘continue’ (and then
    only to the next part of the tie). For instance, if there are two
    tied notes, and the first note has a ‘dotted’-start tie, and the
    second note has a ‘dashed’-stop tie, the graphical tie itself will be dotted.

    A type of tie that is unknown raises a ValueError:

    ```python
    >>> tie.Tie('hello')
    Traceback (most recent call last):
    music21.tie.TieException: Type must be one of
    ('start', 'stop', 'continue', 'let-ring', 'continue-let-ring'), not hello
    ```

[`Tie`](#music21.tie.Tie "music21.tie.Tie") bases

* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")
* [`SlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.SlottedObjectMixin "music21.common.objects.SlottedObjectMixin")

[`Tie`](#music21.tie.Tie "music21.tie.Tie") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`Tie`](#music21.tie.Tie "music21.tie.Tie") methods

Tie.\_\_eq\_\_(*other*)[[source]](../_modules/music21/tie.html#Tie.__eq__)
:   Equality. Based entirely on Tie.type.

    ```python
    >>> t1 = tie.Tie('start')
    >>> t2 = tie.Tie('start')
    >>> t3 = tie.Tie('stop')
    >>> t1 == t2
    True
    ```

    ```python
    >>> t2 == t3, t3 == t1
    (False, False)
    ```

    ```python
    >>> t2 == None
    False
    ```

[`Tie`](#music21.tie.Tie "music21.tie.Tie") instance variables

Tie.placement
:   Whether the tie should go up or down. Can be None, meaning
    it is unknown or should be determined from context, or ‘above’ or ‘below.

Tie.style
:   The style of the tie. Currently can be ‘normal’, ‘dotted’, ‘dashed’ or ‘hidden’

Tie.type
:   The tie type, can be ‘start’, ‘stop’, ‘continue’, ‘let-ring’, or ‘continue-let-ring’.
