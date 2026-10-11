Source: https://music21.org/music21docs/moduleReference/moduleCommonMisc.html

# music21.common.misc

If it doesn’t fit anywhere else in the common directory, you’ll find it here!

## Functions

music21.common.misc.cleanedFlatNotation(*music\_str: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](../_modules/music21/common/misc.html#cleanedFlatNotation)
:   Returns a copy of the given string where each occurrence of a flat note
    specified with a ‘b’ is replaced by a ‘-‘.

    music\_str is a string containing a note specified (for example in a chord)

    Returns a new string with flats only specified with ‘-‘.

    ```python
    >>> common.cleanedFlatNotation('Cb')
    'C-'
    ```

music21.common.misc.defaultDeepcopy(*obj: [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")*, *memo=None*, *\**, *ignoreAttributes: [Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] = ()*)[[source]](../_modules/music21/common/misc.html#defaultDeepcopy)
:   Unfortunately, it is not possible to do something like:

    ```python
    def __deepcopy__(self, memo):
        if self._noDeepcopy:
            return self.__class__()
        else:
            copy.deepcopy(self, memo, ignore__deepcopy__=True)
    ```

    Or, else: return NotImplemented

    so that’s what this is for:

    ```python
    def __deepcopy__(self, memo):
        if self._noDeepcopy:
            return self.__class__()
        else:
            return common.defaultDeepcopy(self, memo)
    ```

    Does a deepcopy of the state returned by \_\_reduce\_ex\_\_ for protocol 4.

    * Changed in v9: callInit is removed, replaced with ignoreAttributes.
      uses \_\_reduce\_ex\_\_ internally.

music21.common.misc.flattenList(*originalList: Iterable[Iterable[\_T]]*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[\_T][[source]](../_modules/music21/common/misc.html#flattenList)
:   Flatten a list of lists into a flat list:

    ```python
    >>> l = [[1, 2, 3], [4, 5], [6]]
    >>> common.flattenList(l)
    [1, 2, 3, 4, 5, 6]
    ```

    But not a list of lists-of-lists!

    ```python
    >>> l2 = [[1, 2, 3], [4, 5], [6, [7, 8]]]
    >>> common.flattenList(l2)
    [1, 2, 3, 4, 5, 6, [7, 8]]
    ```

music21.common.misc.getMissingImportStr(*modNameList*)[[source]](../_modules/music21/common/misc.html#getMissingImportStr)
:   Given a list of missing module names, returns a nicely-formatted message to the user
    that gives instructions on how to expand music21 with optional packages.

    ```python
    >>> print(common.getMissingImportStr(['matplotlib']))
    Certain music21 functions might need the optional package matplotlib;
    if you run into errors, install it by following the instructions at
    https://www.music21.org/music21docs/installing/installAdditional.html
    ```

    ```python
    >>> print(common.getMissingImportStr(['matplotlib', 'numpy']))
    Certain music21 functions might need these optional packages: matplotlib, numpy;
    if you run into errors, install them by following the instructions at
    https://www.music21.org/music21docs/installing/installAdditional.html
    ```

music21.common.misc.getPlatform() → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](../_modules/music21/common/misc.html#getPlatform)
:   Return the name of the platform, where platforms are divided
    between ‘win’ (for Windows), ‘darwin’ (for MacOS X), and ‘nix’ for
    (GNU/Linux and other variants).

    Does not discern between Linux/FreeBSD, etc.

    Lowercase names are for backwards compatibility – this existed before
    the platform module.

music21.common.misc.macOSVersion() → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][[source]](../_modules/music21/common/misc.html#macOSVersion)
:   On a Mac returns the current version as a tuple of (currently 3) ints,
    such as: (10, 5, 6) for 10.5.6.

    On other systems, returns (0, 0, 0)

music21.common.misc.pitchList(*pitchL*)[[source]](../_modules/music21/common/misc.html#pitchList)
:   utility method that replicates the previous behavior of
    lists of pitches.

    May be moved in v8 or later to a common.testing or test.X module.

music21.common.misc.runningInNotebook() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/common/misc.html#runningInNotebook)
:   return bool if we are running under Jupyter Notebook (not IPython terminal)
    or Google Colabatory (colab).

    Methods based on:

    <https://stackoverflow.com/questions/15411967/how-can-i-check-if-code-is-executed-in-the-ipython-notebook>

    (No tests provided here, since results will differ depending on environment)

music21.common.misc.sortModules(*moduleList: [Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "(in Python v3.14)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")]*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[object](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")][[source]](../_modules/music21/common/misc.html#sortModules)
:   Sort a list of imported module names such that most recently modified is
    first. In ties, last access time is used then module name

    Will return a different order each time depending on the last mod time

music21.common.misc.unique(*originalList: [Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "(in Python v3.14)")*, *\**, *key: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[source]](../_modules/music21/common/misc.html#unique)
:   Return a List of unique items from an iterable, preserving order.
    (unlike casting to a set and back)

    (And why is this not already in Python?)

    ```python
    >>> common.misc.unique([3, 2, 4, 3, 2, 5])
    [3, 2, 4, 5]
    ```

    Works on any iterable, but order might not be preserved for sets, etc.

    ```python
    >>> common.misc.unique(range(5))
    [0, 1, 2, 3, 4]
    ```

    If key is a function then use that to get the value:

    ```python
    >>> s = converter.parse('tinyNotation: c4 E d C f# e a')
    >>> common.misc.unique(s.recurse().notes, key=lambda n: n.name)
     [<music21.note.Note C>,
      <music21.note.Note E>,
      <music21.note.Note D>,
      <music21.note.Note F#>,
      <music21.note.Note A>]
    ```
