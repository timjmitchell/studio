Source: https://music21.org/music21docs/moduleReference/moduleCommonWeakrefTools.html

# music21.common.weakrefTools

## Functions

music21.common.weakrefTools.unwrapWeakref(*referent: ReferenceType | [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")*) → [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")[[source]](../_modules/music21/common/weakrefTools.html#unwrapWeakref)
:   Utility function that gets an object that might be an object itself
    or a weak reference to an object. It returns obj() if it’s a weakref.
    and obj if it’s not.

    ```python
    >>> class Mock:
    ...     pass
    >>> a1 = Mock()
    >>> a2 = Mock()
    >>> a2.strong = a1
    >>> a2.weak = common.wrapWeakref(a1)
    >>> common.unwrapWeakref(a2.strong) is a1
    True
    >>> common.unwrapWeakref(a2.weak) is a1
    True
    >>> common.unwrapWeakref(a2.strong) is common.unwrapWeakref(a2.weak)
    True
    ```

music21.common.weakrefTools.wrapWeakref(*referent: \_T*) → ReferenceType | \_T[[source]](../_modules/music21/common/weakrefTools.html#wrapWeakref)
:   utility function that wraps objects as weakrefs but does not wrap
    already wrapped objects; also prevents wrapping the unwrappable “None” type, etc.

    ```python
    >>> import weakref
    >>> class Mock:
    ...     pass
    >>> a1 = Mock()
    >>> ref1 = common.wrapWeakref(a1)
    >>> ref1
    <weakref at 0x101f29ae8; to ...Mock' at 0x101e45358>
    >>> ref2 = common.wrapWeakref(ref1)
    >>> ref2
    <weakref at 0x101f299af; to ...Mock' at 0x101e45358>
    >>> ref3 = common.wrapWeakref(5)
    >>> ref3
    5
    ```
