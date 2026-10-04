Source: https://music21.org/music21docs/moduleReference/moduleCommonObjects.html

# music21.common.objects

## EqualSlottedObjectMixin

class music21.common.objects.EqualSlottedObjectMixin[[source]](../_modules/music21/common/objects.html#EqualSlottedObjectMixin)
:   Same as above, but \_\_eq\_\_ and \_\_ne\_\_ functions are defined based on the slots.

    Slots are the only things compared, so do not mix with a \_\_dict\_\_ based object.

    The equal comparison ignores differences in .id

[`EqualSlottedObjectMixin`](#music21.common.objects.EqualSlottedObjectMixin "music21.common.objects.EqualSlottedObjectMixin") bases

* [`SlottedObjectMixin`](#music21.common.objects.SlottedObjectMixin "music21.common.objects.SlottedObjectMixin")

[`EqualSlottedObjectMixin`](#music21.common.objects.EqualSlottedObjectMixin "music21.common.objects.EqualSlottedObjectMixin") methods

EqualSlottedObjectMixin.\_\_eq\_\_(*other*)[[source]](../_modules/music21/common/objects.html#EqualSlottedObjectMixin.__eq__)
:   Return self==value.

## FrozenObject

class music21.common.objects.FrozenObject[[source]](../_modules/music21/common/objects.html#FrozenObject)

[`FrozenObject`](#music21.common.objects.FrozenObject "music21.common.objects.FrozenObject") bases

* [`EqualSlottedObjectMixin`](#music21.common.objects.EqualSlottedObjectMixin "music21.common.objects.EqualSlottedObjectMixin")
* [`SlottedObjectMixin`](#music21.common.objects.SlottedObjectMixin "music21.common.objects.SlottedObjectMixin")

[`FrozenObject`](#music21.common.objects.FrozenObject "music21.common.objects.FrozenObject") methods

Methods inherited from [`EqualSlottedObjectMixin`](#music21.common.objects.EqualSlottedObjectMixin "music21.common.objects.EqualSlottedObjectMixin"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](#music21.common.objects.EqualSlottedObjectMixin.__eq__ "music21.common.objects.EqualSlottedObjectMixin.__eq__") |  |  |

## RelativeCounter

class music21.common.objects.RelativeCounter(*iterable=None*, */*, *\*\*kwds*)[[source]](../_modules/music21/common/objects.html#RelativeCounter)
:   A counter that iterates from most common to least common
    and can return new RelativeCounters that adjust for proportion or percentage.

    ```python
    >>> l = ['b', 'b', 'a', 'a', 'a', 'a', 'c', 'd', 'd', 'd'] + ['e'] * 10
    >>> rc = common.RelativeCounter(l)
    >>> for k in rc:
    ...     print(k, rc[k])
    e 10
    a 4
    d 3
    b 2
    c 1
    ```

    Ties are iterated according to which appeared first in the generated list.

    ```python
    >>> rcProportion = rc.asProportion()
    >>> rcProportion['b']
    0.1
    >>> rcProportion['e']
    0.5
    >>> rcPercentage = rc.asPercentage()
    >>> rcPercentage['b']
    10.0
    >>> rcPercentage['e']
    50.0
    ```

    ```python
    >>> for k, perc in rcPercentage.items():
    ...     print(k, perc)
    e 50.0
    a 20.0
    d 15.0
    b 10.0
    c 5.0
    ```

[`RelativeCounter`](#music21.common.objects.RelativeCounter "music21.common.objects.RelativeCounter") methods

RelativeCounter.asPercentage()[[source]](../_modules/music21/common/objects.html#RelativeCounter.asPercentage)

RelativeCounter.asProportion()[[source]](../_modules/music21/common/objects.html#RelativeCounter.asProportion)

RelativeCounter.items()[[source]](../_modules/music21/common/objects.html#RelativeCounter.items)
:   Return a set-like object providing a view on the dict’s items.

## SingletonCounter

class music21.common.objects.SingletonCounter[[source]](../_modules/music21/common/objects.html#SingletonCounter)
:   A simple counter that can produce unique numbers (in ascending order)
    regardless of how many instances exist.

    Instantiate and then call it.

    ```python
    >>> sc = common.SingletonCounter()
    >>> v0 = sc()
    >>> v1 = sc()
    >>> v1 > v0
    True
    >>> sc2 = common.SingletonCounter()
    >>> v2 = sc2()
    >>> v2 > v1
    True
    ```

## SlottedObjectMixin

class music21.common.objects.SlottedObjectMixin[[source]](../_modules/music21/common/objects.html#SlottedObjectMixin)
:   Provides template for classes implementing slots allowing it to be pickled
    properly, even if there are weakrefs in the slots, or it is subclassed
    by something that does not define slots.

    Only use SlottedObjectMixins for objects that we expect to make so many of
    that memory storage and speed become an issue. Thus, unless you are Xenakis,
    Glissdata is probably not the best example:

    ```python
    >>> import pickle
    >>> class Glissdata(common.SlottedObjectMixin):
    ...     __slots__ = ('time', 'frequency')
    >>> s = Glissdata()
    >>> s.time = 0.125
    >>> s.frequency = 440.0
    >>> out = pickle.dumps(s)
    >>> pickleLoad = pickle.loads(out)
    >>> pickleLoad.time, pickleLoad.frequency
    (0.125, 440.0)
    ```

## Timer

class music21.common.objects.Timer[[source]](../_modules/music21/common/objects.html#Timer)
:   An object for timing. Call it to get the current time since starting.

    ```python
    >>> timer = common.Timer()
    >>> now = timer()
    >>> nowNow = timer()
    >>> nowNow > now
    True
    ```

    Call stop to stop it. Calling start again will reset the number

    ```python
    >>> timer.stop()
    >>> stopTime = timer()
    >>> stopNow = timer()
    >>> stopTime == stopNow
    True
    ```

    All this had better take less than one second!

    ```python
    >>> stopTime < 1
    True
    ```

[`Timer`](#music21.common.objects.Timer "music21.common.objects.Timer") methods

Timer.clear()[[source]](../_modules/music21/common/objects.html#Timer.clear)

Timer.start()[[source]](../_modules/music21/common/objects.html#Timer.start)
:   Explicit start method; will clear previous values.

    Start always happens on initialization.

Timer.stop()[[source]](../_modules/music21/common/objects.html#Timer.stop)

## defaultlist

class music21.common.objects.defaultlist(*fx*)[[source]](../_modules/music21/common/objects.html#defaultlist)
:   Call a function for every time something is missing:

    ```python
    >>> a = common.defaultlist(lambda:True)
    >>> a[5]
    True
    ```

[`defaultlist`](#music21.common.objects.defaultlist "music21.common.objects.defaultlist") methods

defaultlist.\_\_getitem\_\_(*index*)[[source]](../_modules/music21/common/objects.html#defaultlist.__getitem__)
:   Return self[index].
