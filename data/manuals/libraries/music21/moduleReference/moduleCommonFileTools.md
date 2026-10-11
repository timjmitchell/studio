Source: https://music21.org/music21docs/moduleReference/moduleCommonFileTools.html

# music21.common.fileTools

Tools for working with files

## Functions

music21.common.fileTools.cd(*targetDir*)[[source]](../_modules/music21/common/fileTools.html#cd)
:   Useful for a temporary cd for use in a with statement:

    > with cd(‘/Library/’):
    > :   os.system(make)

    will switch temporarily, and then switch back when leaving.

music21.common.fileTools.preparePathClassesForUnpickling()[[source]](../_modules/music21/common/fileTools.html#preparePathClassesForUnpickling)
:   When we need to unpickle a function that might have relative paths
    (like some music21 stream options), Windows chokes if the PosixPath
    is not defined, but usually can still unpickle easily.

music21.common.fileTools.readFileEncodingSafe(*filePath*, *firstGuess='utf-8'*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](../_modules/music21/common/fileTools.html#readFileEncodingSafe)
:   Slow, but will read a file of unknown encoding as safely as possible using
    the chardet package. Mostly obsolete in the utf-8 world of today, but
    useful for older code

    Let’s try to load the music21.common.\_\_init\_\_.py file as ascii –
    it has a copyright symbol near the top, so it won’t load in Python3:

    ```python
    >>> import os
    >>> c = str(common.getSourceFilePath() / 'common' / '__init__.py')
    >>> f = open(c, encoding='ascii')
    >>> data = f.read()
    Traceback (most recent call last):
    UnicodeDecodeError: 'ascii' codec can't decode byte 0xc2 in position ...:
        ordinal not in range(128)
    ```

    That won’t do! Now I know that it is in utf-8, but maybe you don’t. Or it could
    be an old Humdrum or Noteworthy file with Windows or unknown encoding.
    This will load it as safely as possible.

    ```python
    >>> data = common.readFileEncodingSafe(c)
    >>> data[83:106]
    'Name:         common.py'
    ```

    Well, that’s nothing, since the first guess here is utf-8, and it’s right. So let’s
    give a worse first guess:

    ```python
    >>> data = common.readFileEncodingSafe(c, firstGuess='SHIFT_JIS')  # old Japanese standard
    >>> data[83:106]
    'Name:         common.py'
    ```

    It worked!

    Note that trying lots of encodings is slow enough when the first guess is wrong
    that the firstGuess should be set to something reasonable like ‘utf-8’ or ‘ascii’.

music21.common.fileTools.readPickleGzip(*filePath: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")*) → [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")[[source]](../_modules/music21/common/fileTools.html#readPickleGzip)
:   Read a gzip-compressed pickle file, uncompress it, unpickle it, and
    return the contents.

music21.common.fileTools.restorePathClassesAfterUnpickling()[[source]](../_modules/music21/common/fileTools.html#restorePathClassesAfterUnpickling)
:   After unpickling, leave pathlib alone.

music21.common.fileTools.runSubprocessCapturingStderr(*subprocessCommand*)[[source]](../_modules/music21/common/fileTools.html#runSubprocessCapturingStderr)
:   Run a subprocess command, capturing stderr and
    only show the error if an exception is raised.
