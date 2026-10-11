Source: https://music21.org/music21docs/moduleReference/moduleCommonParallel.html

# music21.common.parallel

## Functions

music21.common.parallel.cpus()[[source]](../_modules/music21/common/parallel.html#cpus)
:   Returns the number of CPUs or if >= 3, one less (to leave something out for multiprocessing)

music21.common.parallel.runNonParallel(*iterable*, *parallelFunction*, *\**, *updateFunction=None*, *updateMultiply=3*, *unpackIterable=False*, *updateSendsIterable=False*)[[source]](../_modules/music21/common/parallel.html#runNonParallel)
:   This is intended to be a perfect drop in replacement for runParallel, except that
    it runs on one core only, and not in parallel.

    Used automatically if we’re already in a parallelized function.

music21.common.parallel.runParallel(*iterable*, *parallelFunction*, *\**, *updateFunction=None*, *updateMultiply=3*, *unpackIterable=False*, *updateSendsIterable=False*)[[source]](../_modules/music21/common/parallel.html#runParallel)
:   runs parallelFunction over iterable in parallel, optionally calling updateFunction after
    each common.cpus \* updateMultiply calls.

    Setting updateMultiply too small can make it so that cores wait around when they
    could be working if one CPU has a particularly hard task. Setting it too high
    can make it seem like the job has hung.

    updateFunction should take three arguments: the current position, the total to run,
    and the most recent results. It does not need to be pickleable, and in fact,
    a bound method might be very useful here. Or updateFunction can be “True”
    which just prints a generic message.

    If unpackIterable is True then each element in iterable is considered a list or
    tuple of different arguments to parallelFunction.

    If updateSendsIterable is True then the update function will get the iterable
    content, after the output.

    As of Python 3, partial functions are pickleable, so if you need to pass the same
    arguments to parallelFunction each time, make it a partial function before passing
    it to runParallel.

    Note that parallelFunction, iterable’s contents, and the results of calling parallelFunction
    must all be pickleable, and that if pickling the contents or
    unpickling the results takes a lot of time, you won’t get nearly the speedup
    from this function as you might expect. The big culprit here is definitely
    music21 streams.

    ```python
    >>> files = ['bach/bwv66.6', 'schoenberg/opus19', 'AcaciaReel']
    >>> def countNotes(fn):
    ...     c = corpus.parse(fn)  # this is the slow call that is good to parallelize
    ...     return len(c.recurse().notes)
    >>> outputs = common.runParallel(files, countNotes)
    >>> outputs
    [165, 50, 131]
    ```

    Set updateFunction=True to get an update every 3 \* numCpus (-1 if > 2)

    ```python
    >>> outputs = common.runParallel(files, countNotes, updateFunction=True)
    Done 0 tasks of 3
    Done 3 tasks of 3
    ```

    With a custom updateFunction that gets each output:

    ```python
    >>> def yak(position, length, output):
    ...     print(f'{position}:{length} {output} is a lot of notes!')
    >>> outputs = common.runParallel(files, countNotes, updateFunction=yak)
    0:3 165 is a lot of notes!
    1:3 50 is a lot of notes!
    2:3 131 is a lot of notes!
    ```

    Or with updateSendsIterable, we can get the original files data as well:

    ```python
    >>> def yik(position, length, output, fn):
    ...     print(f'{position}:{length} ({fn}) {output} is a lot of notes!')
    >>> outputs = common.runParallel(files, countNotes, updateFunction=yik,
    ...             updateSendsIterable=True)
    0:3 (bach/bwv66.6) 165 is a lot of notes!
    1:3 (schoenberg/opus19) 50 is a lot of notes!
    2:3 (AcaciaReel) 131 is a lot of notes!
    ```

    unpackIterable is useful for when you need to send multiple values to your function
    call as separate arguments. For instance, something like:

    ```python
    >>> def pitchesAbove(fn, minPitch):  # a two-argument function
    ...     c = corpus.parse(fn)  # again, the slow call goes in the function
    ...     return len([p for p in c.pitches if p.ps > minPitch])
    ```

    ```python
    >>> inputs = [('bach/bwv66.6', 60),
    ...           ('schoenberg/opus19', 72),
    ...           ('AcaciaReel', 66)]
    >>> outputs = common.runParallel(inputs, pitchesAbove, unpackIterable=True)
    >>> outputs
    [99, 11, 123]
    ```

music21.common.parallel.safeToParallize() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/common/parallel.html#safeToParallize)
:   Check to see if it is safe or even useful to start a parallel process.

    Will return False if we are in a multiprocessing child process or if
    there is only one CPU or if pytest’s x-dist worker flag is in the environment.

    * New in v10
