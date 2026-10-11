Source: https://music21.org/music21docs/moduleReference/moduleCommonNumberTools.html

# music21.common.numberTools

## Functions

music21.common.numberTools.fromRoman(*num: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *\**, *strictModern=False*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](../_modules/music21/common/numberTools.html#fromRoman)
:   Convert a Roman numeral (upper or lower) to an int

    <https://code.activestate.com/recipes/81611-roman-numerals/>

    ```python
    >>> common.fromRoman('ii')
    2
    >>> common.fromRoman('vii')
    7
    ```

    Works with both IIII and IV forms:

    ```python
    >>> common.fromRoman('MCCCCLXXXIX')
    1489
    >>> common.fromRoman('MCDLXXXIX')
    1489
    ```

    Some people consider this an error, but you see it in medieval and ancient roman documents:

    ```python
    >>> common.fromRoman('ic')
    99
    ```

    unless strictModern is True

    ```python
    >>> common.fromRoman('ic', strictModern=True)
    Traceback (most recent call last):
    ValueError: input contains an invalid subtraction element (modern interpretation): ic
    ```

    But things like this are never seen, and thus cause an error:

    ```python
    >>> common.fromRoman('vx')
    Traceback (most recent call last):
    ValueError: input contains an invalid subtraction element: vx
    ```

music21.common.numberTools.toRoman(*num: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](../_modules/music21/common/numberTools.html#toRoman)
:   Convert a number from 1 to 3999 to a roman numeral

    ```python
    >>> common.toRoman(2)
    'II'
    >>> common.toRoman(7)
    'VII'
    >>> common.toRoman(1999)
    'MCMXCIX'
    ```

    ```python
    >>> common.toRoman('hi')
    Traceback (most recent call last):
    TypeError: expected integer, got <... 'str'>
    ```

    ```python
    >>> common.toRoman(0)
    Traceback (most recent call last):
    ValueError: Argument must be between 1 and 3999
    ```

music21.common.numberTools.addFloatPrecision(*x*, *grain=0.01*) → [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [Fraction](https://docs.python.org/3/library/fractions.html#fractions.Fraction "(in Python v3.14)")[[source]](../_modules/music21/common/numberTools.html#addFloatPrecision)
:   Given a value that suggests a floating point fraction, like 0.33,
    return a Fraction or float that provides greater specification, such as Fraction(1, 3)

    ```python
    >>> import fractions
    >>> common.addFloatPrecision(0.333)
    Fraction(1, 3)
    >>> common.addFloatPrecision(0.33)
    Fraction(1, 3)
    >>> common.addFloatPrecision(0.35) == fractions.Fraction(1, 3)
    False
    >>> common.addFloatPrecision(0.2) == 0.2
    True
    >>> common.addFloatPrecision(0.125)
    0.125
    >>> common.addFloatPrecision(1/7) == 1/7
    True
    ```

music21.common.numberTools.approximateGCD(*values: Collection[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | Fraction]*, *grain: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") = 0.0001*) → [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")[[source]](../_modules/music21/common/numberTools.html#approximateGCD)
:   Given a list of values, find the lowest common divisor of floating point values.

    ```python
    >>> common.approximateGCD([2.5, 10, 0.25])
    0.25
    >>> common.approximateGCD([2.5, 10])
    2.5
    >>> common.approximateGCD([2, 10])
    2.0
    >>> common.approximateGCD([1.5, 5, 2, 7])
    0.5
    >>> common.approximateGCD([2, 5, 10])
    1.0
    >>> common.approximateGCD([2, 5, 10, 0.25])
    0.25
    >>> common.strTrimFloat(common.approximateGCD([1/3, 2/3]))
    '0.3333'
    >>> common.strTrimFloat(common.approximateGCD([5/3, 2/3, 4]))
    '0.3333'
    >>> common.strTrimFloat(common.approximateGCD([5/3, 2/3, 5]))
    '0.3333'
    >>> common.strTrimFloat(common.approximateGCD([5/3, 2/3, 5/6, 3/6]))
    '0.1667'
    ```

music21.common.numberTools.contiguousList(*inputListOrTuple*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/common/numberTools.html#contiguousList)
:   returns bool True or False if a list containing ints
    contains only contiguous (increasing) values

    requires the list to be sorted first

    ```python
    >>> l = [3, 4, 5, 6]
    >>> common.contiguousList(l)
    True
    >>> l.append(8)
    >>> common.contiguousList(l)
    False
    ```

    Sorting matters

    ```python
    >>> l.append(7)
    >>> common.contiguousList(l)
    False
    >>> common.contiguousList(sorted(l))
    True
    ```

music21.common.numberTools.decimalToTuplet(*decNum: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][[source]](../_modules/music21/common/numberTools.html#decimalToTuplet)
:   For simple decimals (usually > 1), a quick way to figure out the
    fraction in lowest terms that gives a valid tuplet.

    No it does not work really fast. No it does not return tuplets with
    denominators over 100. Too bad, math geeks. This is real life. :-)

    returns (numerator, denominator)

    ```python
    >>> common.decimalToTuplet(1.5)
    (3, 2)
    >>> common.decimalToTuplet(1.25)
    (5, 4)
    ```

    If decNum is < 1, the denominator will be greater than the numerator:

    ```python
    >>> common.decimalToTuplet(0.8)
    (4, 5)
    ```

    If decNum is <= 0, returns a ZeroDivisionError:

    ```python
    >>> common.decimalToTuplet(-.02)
    Traceback (most recent call last):
    ZeroDivisionError: number must be greater than zero
    ```

music21.common.numberTools.dotMultiplier(*dots: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")[[source]](../_modules/music21/common/numberTools.html#dotMultiplier)
:   dotMultiplier(dots) returns how long to multiply the note
    length of a note in order to get the note length with n dots

    Since dotMultiplier always returns a power of two in the denominator,
    the float will be exact.

    ```python
    >>> from fractions import Fraction
    >>> Fraction(common.dotMultiplier(1))
    Fraction(3, 2)
    >>> Fraction(common.dotMultiplier(2))
    Fraction(7, 4)
    >>> Fraction(common.dotMultiplier(3))
    Fraction(15, 8)
    ```

    ```python
    >>> common.dotMultiplier(0)
    1.0
    ```

music21.common.numberTools.groupContiguousIntegers(*src: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]][[source]](../_modules/music21/common/numberTools.html#groupContiguousIntegers)
:   Given a list of integers, group contiguous values into sub lists

    ```python
    >>> common.groupContiguousIntegers([3, 5, 6])
    [[3], [5, 6]]
    >>> common.groupContiguousIntegers([3, 4, 6])
    [[3, 4], [6]]
    >>> common.groupContiguousIntegers([3, 4, 6, 7])
    [[3, 4], [6, 7]]
    >>> common.groupContiguousIntegers([3, 4, 6, 7, 20])
    [[3, 4], [6, 7], [20]]
    >>> common.groupContiguousIntegers([3, 4, 5, 6, 7])
    [[3, 4, 5, 6, 7]]
    >>> common.groupContiguousIntegers([3])
    [[3]]
    >>> common.groupContiguousIntegers([3, 200])
    [[3], [200]]
    ```

music21.common.numberTools.mixedNumeral(*expr: [Real](https://docs.python.org/3/library/numbers.html#numbers.Real "(in Python v3.14)")*, *limitDenominator=65535*)[[source]](../_modules/music21/common/numberTools.html#mixedNumeral)
:   Returns a string representing a mixedNumeral form of a number

    ```python
    >>> common.mixedNumeral(1.333333)
    '1 1/3'
    >>> common.mixedNumeral(0.333333)
    '1/3'
    >>> common.mixedNumeral(-1.333333)
    '-1 1/3'
    >>> common.mixedNumeral(-0.333333)
    '-1/3'
    ```

    ```python
    >>> common.mixedNumeral(0)
    '0'
    >>> common.mixedNumeral(-0)
    '0'
    ```

    Works with Fraction objects too

    ```python
    >>> from fractions import Fraction
    >>> common.mixedNumeral(Fraction(31, 7))
    '4 3/7'
    >>> common.mixedNumeral(Fraction(1, 5))
    '1/5'
    >>> common.mixedNumeral(Fraction(-1, 5))
    '-1/5'
    >>> common.mixedNumeral(Fraction(-4, 5))
    '-4/5'
    >>> common.mixedNumeral(Fraction(-31, 7))
    '-4 3/7'
    ```

    Denominator is limited by default but can be changed.

    ```python
    >>> common.mixedNumeral(2.0000001)
    '2'
    >>> common.mixedNumeral(2.0000001, limitDenominator=10000000)
    '2 1/10000000'
    ```

music21.common.numberTools.nearestMultiple(*n: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*, *unit: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)"), [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)"), [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")][[source]](../_modules/music21/common/numberTools.html#nearestMultiple)
:   Given a positive value n, return the nearest multiple of the supplied unit as well as
    the absolute difference (error) to seven significant digits and the signed difference.

    ```python
    >>> print(common.nearestMultiple(0.25, 0.25))
    (0.25, 0.0, 0.0)
    >>> print(common.nearestMultiple(0.35, 0.25))
    (0.25, 0.1..., 0.1...)
    >>> print(common.nearestMultiple(0.20, 0.25))
    (0.25, 0.05..., -0.05...)
    ```

    Note that this one also has an error of 0.1, but it’s a positive error off of 0.5

    ```python
    >>> print(common.nearestMultiple(0.4, 0.25))
    (0.5, 0.1..., -0.1...)
    ```

    ```python
    >>> common.nearestMultiple(0.4, 0.25)[0]
    0.5
    >>> common.nearestMultiple(23404.001, 0.125)[0]
    23404.0
    >>> common.nearestMultiple(23404.134, 0.125)[0]
    23404.125
    ```

    Error is always positive, but signed difference can be negative.

    ```python
    >>> common.nearestMultiple(23404 - 0.0625, 0.125)
    (23403.875, 0.0625, 0.0625)
    ```

    ```python
    >>> common.nearestMultiple(0.001, 0.125)[0]
    0.0
    ```

    ```python
    >>> from math import isclose
    >>> isclose(common.nearestMultiple(0.25, 1 / 3)[0], 0.33333333, abs_tol=1e-7)
    True
    >>> isclose(common.nearestMultiple(0.55, 1 / 3)[0], 0.66666666, abs_tol=1e-7)
    True
    >>> isclose(common.nearestMultiple(234.69, 1 / 3)[0], 234.6666666, abs_tol=1e-7)
    True
    >>> isclose(common.nearestMultiple(18.123, 1 / 6)[0], 18.16666666, abs_tol=1e-7)
    True
    ```

    ```python
    >>> common.nearestMultiple(-0.5, 0.125)
    Traceback (most recent call last):
    ValueError: n (-0.5) is less than zero. Thus, cannot find the nearest
        multiple for a value less than the unit, 0.125
    ```

music21.common.numberTools.numToIntOrFloat(*value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [Fraction](https://docs.python.org/3/library/fractions.html#fractions.Fraction "(in Python v3.14)")*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")[[source]](../_modules/music21/common/numberTools.html#numToIntOrFloat)
:   Given a number, return an integer if it is very close to an integer,
    otherwise, return a float.

    This routine is very important for conversion of
    [`Accidental`](modulePitch.html#music21.pitch.Accidental "music21.pitch.Accidental") objects’ .alter attribute
    in musicXML must be 1 (not 1.0) for sharp and -1 (not -1.0) for flat,
    but allows for 0.5 for half-sharp.

    ```python
    >>> common.numToIntOrFloat(1.0)
    1
    >>> common.numToIntOrFloat(1.00003)
    1.00003
    >>> common.numToIntOrFloat(1.5)
    1.5
    >>> common.numToIntOrFloat(2)
    2
    >>> common.numToIntOrFloat(-5)
    -5
    >>> common.numToIntOrFloat(1.0000000005)
    1
    >>> common.numToIntOrFloat(0.999999999)
    1
    ```

    ```python
    >>> sharp = pitch.Accidental('sharp')
    >>> common.numToIntOrFloat(sharp.alter)
    1
    >>> halfFlat = pitch.Accidental('half-flat')
    >>> common.numToIntOrFloat(halfFlat.alter)
    -0.5
    ```

    Can also take in a string representing an int or float

    ```python
    >>> common.numToIntOrFloat('1.0')
    1
    >>> common.numToIntOrFloat('1')
    1
    >>> common.numToIntOrFloat('1.25')
    1.25
    ```

    Others raise a ValueError

    ```python
    >>> common.numToIntOrFloat('one')
    Traceback (most recent call last):
    ValueError: could not convert string to float: 'one'
    ```

    Fractions also become ints or floats

    ```python
    >>> from fractions import Fraction
    >>> common.numToIntOrFloat(Fraction(1, 2))
    0.5
    >>> common.numToIntOrFloat(Fraction(4, 3))
    1.333333333...
    ```

    Note: Decimal objects are not supported.

music21.common.numberTools.opFrac(*num: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")[[source]](../_modules/music21/common/numberTools.html#opFrac)

music21.common.numberTools.opFrac(*num: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [Fraction](https://docs.python.org/3/library/fractions.html#fractions.Fraction "(in Python v3.14)")*) → [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [Fraction](https://docs.python.org/3/library/fractions.html#fractions.Fraction "(in Python v3.14)")
:   opFrac -> optionally convert a number to a fraction or back.

    Important music21 function for working with offsets and quarterLengths

    Takes in a number and converts it to a Fraction with denominator
    less than limitDenominator if it is not binary expressible; otherwise return a float.
    Or if the Fraction can be converted back to a binary expressible
    float then do so.

    This function should be called often to ensure that values being passed around are floats
    and ints wherever possible and fractions where needed.

    The naming of this method violates music21’s general rule of no abbreviations, but it
    is important to make it short enough so that no one will be afraid of calling it often.
    It also doesn’t have a setting for maxDenominator so that it will expand in
    Code Completion easily. That is to say, this function has been set up to be used, so please
    use it.

    This is a performance-critical operation. Do not alter it in any way without running
    many timing tests.

    ```python
    >>> from fractions import Fraction
    >>> defaults.limitOffsetDenominator
    65535
    >>> common.opFrac(3)
    3.0
    >>> common.opFrac(1/3)
    Fraction(1, 3)
    >>> common.opFrac(1/4)
    0.25
    >>> f = Fraction(1, 3)
    >>> common.opFrac(f + f + f)
    1.0
    >>> common.opFrac(0.99999999842)
    1.0
    >>> common.opFrac(0.123456789)
    Fraction(10, 81)
    >>> common.opFrac(0.000001)
    0.0
    ```

    Please check against None before calling, but None is changed to 0.0

    ```python
    >>> common.opFrac(None)
    0.0
    ```

    * Changed in v9.3: opFrac(None) should not be called. If it is called,
      it now returns 0.0

music21.common.numberTools.ordinalAbbreviation(*value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *plural=False*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](../_modules/music21/common/numberTools.html#ordinalAbbreviation)
:   Return the ordinal abbreviations for integers

    ```python
    >>> common.ordinalAbbreviation(3)
    'rd'
    >>> common.ordinalAbbreviation(255)
    'th'
    >>> common.ordinalAbbreviation(255, plural=True)
    'ths'
    ```

music21.common.numberTools.roundToHalfInteger(*num: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](../_modules/music21/common/numberTools.html#roundToHalfInteger)
:   Given a floating-point number, round to the nearest half-integer. Returns int or float

    ```python
    >>> common.roundToHalfInteger(1.2)
    1
    >>> common.roundToHalfInteger(1.35)
    1.5
    >>> common.roundToHalfInteger(1.8)
    2
    >>> common.roundToHalfInteger(1.6234)
    1.5
    ```

    0.25 rounds up:

    ```python
    >>> common.roundToHalfInteger(0.25)
    0.5
    ```

    as does 0.75

    ```python
    >>> common.roundToHalfInteger(0.75)
    1
    ```

    unlike python round function, does the same for 1.25 and 1.75

    ```python
    >>> common.roundToHalfInteger(1.25)
    1.5
    >>> common.roundToHalfInteger(1.75)
    2
    ```

    negative numbers however, round up on the boundaries

    ```python
    >>> common.roundToHalfInteger(-0.26)
    -0.5
    >>> common.roundToHalfInteger(-0.25)
    0
    ```

music21.common.numberTools.strTrimFloat(*floatNum: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*, *maxNum: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 4*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](../_modules/music21/common/numberTools.html#strTrimFloat)
:   returns a string from a float that is at most maxNum of
    decimal digits long, but never less than 1.

    ```python
    >>> common.strTrimFloat(42.3333333333)
    '42.3333'
    >>> common.strTrimFloat(42.3333333333, 2)
    '42.33'
    >>> common.strTrimFloat(6.66666666666666, 2)
    '6.67'
    >>> common.strTrimFloat(2.0)
    '2.0'
    >>> common.strTrimFloat(-5)
    '-5.0'
    ```

music21.common.numberTools.unitBoundaryProportion(*series: Sequence[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")]*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)"), [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")]][[source]](../_modules/music21/common/numberTools.html#unitBoundaryProportion)
:   Take a series of parts with an implied sum, and create
    unit-interval boundaries proportional to the series components.

    ```python
    >>> common.unitBoundaryProportion([1, 1, 2])
    [(0.0, 0.25), (0.25, 0.5), (0.5, 1.0)]
    >>> common.unitBoundaryProportion([9, 1, 1])
    [(0.0, 0.8...), (0.8..., 0.9...), (0.9..., 1.0)]
    ```

music21.common.numberTools.unitNormalizeProportion(*values: Sequence[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")]*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")][[source]](../_modules/music21/common/numberTools.html#unitNormalizeProportion)
:   Normalize values within the unit interval, where max is determined by the sum of the series.

    ```python
    >>> common.unitNormalizeProportion([0, 3, 4])
    [0.0, 0.42857142857142855, 0.5714285714285714]
    >>> common.unitNormalizeProportion([1, 1, 1])
    [0.3333333..., 0.333333..., 0.333333...]
    ```

    Works fine with a mix of ints and floats:

    ```python
    >>> common.unitNormalizeProportion([1.0, 1, 1.0])
    [0.3333333..., 0.333333..., 0.333333...]
    ```

    On 32-bit computers this number may be inexact even for small floats.
    On 64-bit it works fine. This is the 32-bit output for this result.

    > common.unitNormalizeProportion([0.2, 0.6, 0.2])
    > [0.20000000000000001, 0.59999999999999998, 0.20000000000000001]

    Negative values should be shifted to positive region first:

    ```python
    >>> common.unitNormalizeProportion([0, -2, -8])
    Traceback (most recent call last):
    ValueError: value members must be positive
    ```

music21.common.numberTools.weightedSelection(*values: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*, *weights: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")]*, *randomGenerator=None*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](../_modules/music21/common/numberTools.html#weightedSelection)
:   Given a list of values and an equal-sized list of weights,
    return a randomly selected value using the weight.

    Example: sum -1 and 1 for 100 values; should be
    around 0 or at least between -50 and 50 (99.99999% of the time)

    ```python
    >>> -50 < sum([common.weightedSelection([-1, 1], [1, 1]) for x in range(100)]) < 50
    True
    ```
