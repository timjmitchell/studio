Source: https://music21.org/music21docs/moduleReference/moduleAnalysisHarmonicFunction.html

# music21.analysis.harmonicFunction

## HarmonicFunction

class music21.analysis.harmonicFunction.HarmonicFunction(*\*values*)[[source]](../_modules/music21/analysis/harmonicFunction.html#HarmonicFunction)

[`HarmonicFunction`](#music21.analysis.harmonicFunction.HarmonicFunction "music21.analysis.harmonicFunction.HarmonicFunction") bases

* [`StrEnum`](moduleCommonEnums.html#music21.common.enums.StrEnum "music21.common.enums.StrEnum")

## Functions

music21.analysis.harmonicFunction.functionToRoman(*thisHarmonicFunction: [HarmonicFunction](#music21.analysis.harmonicFunction.HarmonicFunction "music21.analysis.harmonicFunction.HarmonicFunction")*, *keyOrScale: [Key](moduleKey.html#music21.key.Key "music21.key.Key") | [ConcreteScale](moduleScale.html#music21.scale.ConcreteScale "music21.scale.ConcreteScale") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = 'C'*) → [RomanNumeral](moduleRoman.html#music21.roman.RomanNumeral "music21.roman.RomanNumeral") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/analysis/harmonicFunction.html#functionToRoman)
:   Takes harmonic function labels (such as ‘T’ for major tonic)
    with a key (keyOrScale, default = ‘C’) and
    returns the corresponding [`RomanNumeral`](moduleRoman.html#music21.roman.RomanNumeral "music21.roman.RomanNumeral") object.

    ```python
    >>> analysis.harmonicFunction.functionToRoman('T')
    <music21.roman.RomanNumeral I in C major>
    ```

    The harmonicFunction argument can be a string (as shown),
    though strictly speaking, it’s handled through a special HarmonicFunction enum object.

    ```python
    >>> fn = analysis.harmonicFunction.HarmonicFunction.TONIC_MAJOR
    >>> str(fn)
    'T'
    ```

    ```python
    >>> analysis.harmonicFunction.functionToRoman(fn).figure
    'I'
    ```

    As with Roman numerals, this is case sensitive.
    For instance, ‘t’ indicates a minor tonic
    as distinct from the major tonic, ‘T’.

    ```python
    >>> analysis.harmonicFunction.functionToRoman('t').figure
    'i'
    ```

    There are 18 main functional labels supported in all, for
    the three functional categories
    (T for tonic, S for subdominant, and D for dominant) and
    three relevant transformation types (none, P, and G)
    all in upper and lower case (for major/minor):
    T, Tp, Tg, t, tP, tG,
    S, Sp, Sg, s, sP, sG,
    D, Dp, Dg, d, dP, dG.

    Note that this module uses terminology from modern German music theory
    where Functional notation (‘HarmonicFunctionstheorie’) is typically used
    throughout the curriculum in preference over Roman numerals (‘Stufentheorie’).

    First, note the false friend: here ‘P’ for ‘Parallel’
    connects a major triad with the minor triad a minor third below (e.g. C-a).
    (in English-speaking traditions this would usually be ‘relative’).

    Second, note that this module uses
    ‘G’ (and ‘g’), standing for
    ‘Gegenklänge’ or ‘Gegenparallelen’.
    ‘L’ (and ‘l’) for Leittonwechselklänge is equivalent to this.
    (Again, ‘G’ is more common in modern German-language music theory).

    Use the keyOrScale argement to specify a key.
    This makes a difference where 6th and 7th degrees of minor are involved.

    ```python
    >>> analysis.harmonicFunction.functionToRoman('sP', keyOrScale='C').figure
    'bVI'
    ```

    ```python
    >>> analysis.harmonicFunction.functionToRoman('sP', keyOrScale='a').figure
    'VI'
    ```

    Some of the 18 main functions overlap, with two functional labels
    referring to the same Roman numeral figure.
    For instance both ‘Tg’ and ‘Dp’ simply map to ‘iii’:

    ```python
    >>> analysis.harmonicFunction.functionToRoman('Tp').figure
    'vi'
    ```

    ```python
    >>> analysis.harmonicFunction.functionToRoman('Sg').figure
    'vi'
    ```

    The reverse operation is handled by the complementary
    [`romanToFunction()`](#music21.analysis.harmonicFunction.romanToFunction "music21.analysis.harmonicFunction.romanToFunction").
    In this case, [`romanToFunction()`](#music21.analysis.harmonicFunction.romanToFunction "music21.analysis.harmonicFunction.romanToFunction")
    follows the convention of preferring the P-version over alternatives.

    ```python
    >>> rn = roman.RomanNumeral('vi')
    >>> str(analysis.harmonicFunction.romanToFunction(rn))
    'Tp'
    ```

music21.analysis.harmonicFunction.romanToFunction(*rn: [RomanNumeral](moduleRoman.html#music21.roman.RomanNumeral "music21.roman.RomanNumeral")*, *onlyHauptHarmonicFunction: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*) → [HarmonicFunction](#music21.analysis.harmonicFunction.HarmonicFunction "music21.analysis.harmonicFunction.HarmonicFunction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/analysis/harmonicFunction.html#romanToFunction)
:   Takes a Roman numeral and returns a corresponding harmonic function label.

    ```python
    >>> rn1 = roman.RomanNumeral('VI', 'a')
    >>> fn1 = analysis.harmonicFunction.romanToFunction(rn1)
    >>> fn1
    <HarmonicFunction.SUBDOMINANT_MINOR_PARALLELKLANG_MAJOR>
    ```

    This can be converted into a string:

    ```python
    >>> str(fn1)
    'sP'
    ```

    Optionally, set onlyHauptHarmonicFunction to True to return
    a simplified version with only the HauptHarmonicFunction
    (one of t, T, s, S, d, D: major and minor forms of the tonic, subdominant and dominant).

    ```python
    >>> fn1 = analysis.harmonicFunction.romanToFunction(rn1, onlyHauptHarmonicFunction=True)
    >>> fn1
    <HarmonicFunction.SUBDOMINANT_MINOR>
    ```

    ```python
    >>> str(fn1)
    's'
    ```

    Inversions are not currently considered (they may be in a future version of this).
    This function simply uses the romanNumeral attribute of the roman.RomanNumeral object.
    This excludes inversions, but
    includes, where applicable, the frontAlterationAccidental.modifier.

    ```python
    >>> rn2 = roman.RomanNumeral('bII6', 'g')
    >>> fn2 = analysis.harmonicFunction.romanToFunction(rn2)
    >>> fn2
    <HarmonicFunction.SUBDOMINANT_MINOR_GEGENKLANG_MAJOR>
    ```

    ```python
    >>> str(fn2)
    'sG'
    ```

    See further notes on the complementary
    [`functionToRoman()`](#music21.analysis.harmonicFunction.functionToRoman "music21.analysis.harmonicFunction.functionToRoman").
