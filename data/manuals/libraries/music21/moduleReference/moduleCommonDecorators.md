Source: https://music21.org/music21docs/moduleReference/moduleCommonDecorators.html

# music21.common.decorators

## Functions

music21.common.decorators.cacheMethod(*method*)[[source]](../_modules/music21/common/decorators.html#cacheMethod)
:   A decorator for music21Objects or other objects that
    assumes that there is a .\_cache Dictionary in the instance
    and returns or sets that value if it exists, otherwise calls the method
    and stores the value.

    To be used ONLY with zero-arg calls. Like properties. Well, can be
    used by others but will not store per-value caches.

    Not a generic memorize, because by storing in one .\_cache place,
    a .clearCache() method can eliminate them.

    Uses the name of the function as the cache key.

    * New in v6: helps to make all the caches easier to work with.

music21.common.decorators.deprecated(*method*, *startDate=None*, *removeDate=None*, *message=None*)[[source]](../_modules/music21/common/decorators.html#deprecated)
:   Decorator that marks a function as deprecated and should not be called.

    Because we’re all developers, it does not use DeprecationWarning, which no
    one would ever see, but UserWarning.

    Warns once per session and never again.

    Use without arguments for a simple case:

    For demonstrating I need to screw with stderr:

    ```python
    >>> import sys
    >>> saveStdErr = sys.stderr
    >>> sys.stderr = sys.stdout
    ```

    ```python
    >>> @common.deprecated
    ... def hi(msg):
    ...     print(msg)
    ```

    (I’m printing “/” at the beginning because the message begins with the filepath which is
    different on each system, but you can’t use ellipses at the beginning of a doctest)

    ```python
    >>> print('/'); hi('myke')
    /...Music21DeprecationWarning: hi was deprecated
            and will disappear soon. Find alternative methods.
    ...
     myke
    ```

    A second call raises no warning:

    ```python
    >>> hi('myke')
    myke
    ```

    Now a new function demonstrating the argument form.

    ```python
    >>> @common.deprecated('February 1972', 'September 2099', 'You should be okay.')
    ... def bye(msg):
    ...     print(msg)
    ```

    ```python
    >>> print('/'); bye('world')
    /...Music21DeprecationWarning: bye was deprecated on February 1972
            and will disappear at or after September 2099. You should be okay.
    ...
    world
    ```

    Restore stderr at the end.

    ```python
    >>> sys.stderr = saveStdErr
    ```

music21.common.decorators.optional\_arg\_decorator(*fn*)[[source]](../_modules/music21/common/decorators.html#optional_arg_decorator)
:   a decorator for decorators. Allows them to either have or not have arguments.
