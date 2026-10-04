Source: https://music21.org/music21docs/moduleReference/moduleMeterTools.html

# music21.meter.tools

## MeterTerminalTuple

class music21.meter.tools.MeterTerminalTuple(*numerator*, *denominator*, *division*)[[source]](../_modules/music21/meter/tools.html#MeterTerminalTuple)

## Functions

music21.meter.tools.divisionOptionsAdditiveMultiples(*n: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *d: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), ...], ...][[source]](../_modules/music21/meter/tools.html#divisionOptionsAdditiveMultiples)
:   Additive multiples with the same denominators.

    ```python
    >>> meter.tools.divisionOptionsAdditiveMultiples(4, 16)
    (('2/16', '2/16'),)
    >>> meter.tools.divisionOptionsAdditiveMultiples(6, 4)
    (('3/4', '3/4'),)
    ```

music21.meter.tools.divisionOptionsAdditiveMultiplesDownward(*n: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *d: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), ...], ...][[source]](../_modules/music21/meter/tools.html#divisionOptionsAdditiveMultiplesDownward)
:   ```python
    >>> meter.tools.divisionOptionsAdditiveMultiplesDownward(1, 16)
    (('1/32', '1/32'), ('1/64', '1/64', '1/64', '1/64'),
     ('1/128', '1/128', '1/128', '1/128', '1/128', '1/128', '1/128', '1/128'))
    ```

music21.meter.tools.divisionOptionsAdditiveMultiplesEvenDivision(*n: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *d: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), ...], ...][[source]](../_modules/music21/meter/tools.html#divisionOptionsAdditiveMultiplesEvenDivision)
:   ```python
    >>> meter.tools.divisionOptionsAdditiveMultiplesEvenDivision(4, 16)
    (('1/8', '1/8'),)
    >>> meter.tools.divisionOptionsAdditiveMultiplesEvenDivision(4, 4)
    (('1/2', '1/2'),)
    >>> meter.tools.divisionOptionsAdditiveMultiplesEvenDivision(3, 4)
    ()
    ```

music21.meter.tools.divisionOptionsAdditiveMultiplesUpward(*n: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *d: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), ...], ...][[source]](../_modules/music21/meter/tools.html#divisionOptionsAdditiveMultiplesUpward)
:   ```python
    >>> meter.tools.divisionOptionsAdditiveMultiplesUpward(4, 16)
    (('1/16', '1/16', '1/16', '1/16'),
     ('1/32', '1/32', '1/32', '1/32', '1/32', '1/32', '1/32', '1/32'),
     ('1/64', '1/64', '1/64', '1/64', '1/64', '1/64', '1/64', '1/64',
      '1/64', '1/64', '1/64', '1/64', '1/64', '1/64', '1/64', '1/64'))
    >>> meter.tools.divisionOptionsAdditiveMultiplesUpward(3, 4)
    (('1/4', '1/4', '1/4'),
     ('1/8', '1/8', '1/8', '1/8', '1/8', '1/8'),
     ('1/16', '1/16', '1/16', '1/16', '1/16', '1/16',
      '1/16', '1/16', '1/16', '1/16', '1/16', '1/16'))
    ```

music21.meter.tools.divisionOptionsFractionsDownward(*n: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *d: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), ...][[source]](../_modules/music21/meter/tools.html#divisionOptionsFractionsDownward)
:   Get restatements of the same fraction in larger units

    ```python
    >>> meter.tools.divisionOptionsFractionsDownward(2, 4)
    ('1/2',)
    >>> meter.tools.divisionOptionsFractionsDownward(12, 16)
    ('6/8', '3/4')
    ```

    Note that this returns a tuple of strings not MeterOptions

music21.meter.tools.divisionOptionsFractionsUpward(*n: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *d: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), ...][[source]](../_modules/music21/meter/tools.html#divisionOptionsFractionsUpward)
:   This simply gets restatements of the same fraction in smaller units,
    up to the largest valid denominator.

    ```python
    >>> meter.tools.divisionOptionsFractionsUpward(2, 4)
    ('4/8', '8/16', '16/32', '32/64', '64/128')
    >>> meter.tools.divisionOptionsFractionsUpward(3, 4)
    ('6/8', '12/16', '24/32', '48/64', '96/128')
    ```

    Note that this returns a tuple of strings not MeterOptions
