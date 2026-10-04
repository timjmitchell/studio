Source: https://music21.org/music21docs/moduleReference/moduleRoman.html

# music21.roman

Music21 class for dealing with Roman Numeral analysis

## RomanNumeral

class music21.roman.RomanNumeral(*figure: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = ''*, *keyOrScale: [Key](moduleKey.html#music21.key.Key "music21.key.Key") | [ConcreteScale](moduleScale.html#music21.scale.ConcreteScale "music21.scale.ConcreteScale") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\**, *caseMatters=True*, *updatePitches=True*, *sixthMinor=Minor67Default.QUALITY*, *seventhMinor=Minor67Default.QUALITY*, *\*\*keywords*)[[source]](../_modules/music21/roman.html#RomanNumeral)
:   A RomanNumeral object is a specialized type of
    [`Harmony`](moduleHarmony.html#music21.harmony.Harmony "music21.harmony.Harmony") object that stores the function and scale
    degree of a chord within a [`Key`](moduleKey.html#music21.key.Key "music21.key.Key").

    ```python
    >>> ivInE = roman.RomanNumeral('IV', key.Key('E'))
    >>> ivInE.pitches
    (<music21.pitch.Pitch A4>, <music21.pitch.Pitch C#5>, <music21.pitch.Pitch E5>)
    ```

    Octaves assigned are arbitrary (generally C-4 or above) and just exist
    to keep the pitches properly sorted.

    Major and minor are written with capital and lowercase numerals respectively.
    Inversions and seventh-, ninth-, etc. chords are specified by putting the
    figured bass symbols directly after the chord. Keys can be specified with
    Key objects or (less efficiently) a string.

    Dominant-seventh chord in c minor.

    ```python
    >>> roman.RomanNumeral('V7', 'c').pitches
    (<music21.pitch.Pitch G4>, <music21.pitch.Pitch B4>,
     <music21.pitch.Pitch D5>, <music21.pitch.Pitch F5>)
    ```

    Minor chord on the fifth scale degree, in second inversion:

    ```python
    >>> roman.RomanNumeral('v64', 'c').pitches
    (<music21.pitch.Pitch D4>, <music21.pitch.Pitch G4>, <music21.pitch.Pitch B-4>)
    ```

    If no Key is given then it exists as a theoretical, keyless RomanNumeral;
    e.g., V in any key. But when realized, keyless RomanNumerals are
    treated as if they are in C major.

    ```python
    >>> V = roman.RomanNumeral('V')
    >>> V.quality
    'major'
    ```

    ```python
    >>> V.inversion()
    0
    ```

    ```python
    >>> V.forteClass
    '3-11B'
    ```

    ```python
    >>> V.scaleDegree
    5
    ```

    Default key is C Major

    ```python
    >>> for p in V.pitches:
    ...     p
    <music21.pitch.Pitch G4>
    <music21.pitch.Pitch B4>
    <music21.pitch.Pitch D5>
    ```

    Neapolitan chords can be written as ‘N6’, ‘bII6’, or simply ‘N’

    ```python
    >>> neapolitan = roman.RomanNumeral('N6', 'c#')
    >>> neapolitan.key
    <music21.key.Key of c# minor>
    ```

    ```python
    >>> neapolitan.isMajorTriad()
    True
    ```

    ```python
    >>> neapolitan.scaleDegreeWithAlteration
    (2, <music21.pitch.Accidental flat>)
    ```

    ```python
    >>> for p in neapolitan.pitches:
    ...     p
    <music21.pitch.Pitch F#4>
    <music21.pitch.Pitch A4>
    <music21.pitch.Pitch D5>
    ```

    ```python
    >>> neapolitan2 = roman.RomanNumeral('bII6', 'g#')
    >>> [str(p) for p in neapolitan2.pitches]
    ['C#5', 'E5', 'A5']
    ```

    ```python
    >>> neapolitan2.scaleDegree
    2
    ```

    Here’s another dominant seventh chord in minor:

    ```python
    >>> em = key.Key('e')
    >>> dominantV = roman.RomanNumeral('V7', em)
    >>> [str(p) for p in dominantV.pitches]
    ['B4', 'D#5', 'F#5', 'A5']
    ```

    Now using the older terminology where the case does not determine the
    quality, it becomes a minor-seventh chord:

    ```python
    >>> minorV = roman.RomanNumeral('V43', em, caseMatters=False)
    >>> [str(p) for p in minorV.pitches]
    ['F#4', 'A4', 'B4', 'D5']
    ```

    (We will do this str(p) for p in thing enough that let’s make a helper function:)

    ```python
    >>> def cp(rn_in):  # cp = chord pitches
    ...     return [str(p) for p in rn_in.pitches]
    >>> cp(minorV)
    ['F#4', 'A4', 'B4', 'D5']
    ```

    In minor – VII and VI are assumed to refer to the flattened scale degree, while
    vii, viio, viio7, viiø7 and vi, vio, vio7, and viø7 all refer to the sharpened scale
    degree. To get a minor triad on lowered 6 for instance, you will need to use ‘bvi’
    while to get a major triad on raised 6, use ‘#VI’.

    The actual rule is that if the chord implies minor, diminished, or half-diminished,
    an implied “#” is read before the figure. Anything else does not add the sharp.
    The lowered (natural minor) is the assumed basic chord.

    ```python
    >>> majorFlatSeven = roman.RomanNumeral('VII', em)
    >>> cp(majorFlatSeven)
    ['D5', 'F#5', 'A5']
    ```

    ```python
    >>> minorSharpSeven = roman.RomanNumeral('vii', em)
    >>> cp(minorSharpSeven)
    ['D#5', 'F#5', 'A#5']
    ```

    ```python
    >>> majorFlatSix = roman.RomanNumeral('VI', em)
    >>> cp(majorFlatSix)
    ['C5', 'E5', 'G5']
    ```

    ```python
    >>> minorSharpSix = roman.RomanNumeral('vi', em)
    >>> cp(minorSharpSix)
    ['C#5', 'E5', 'G#5']
    ```

    These rules can be changed by passing in a sixthMinor or seventhMinor parameter set to
    a member of [`music21.roman.Minor67Default`](#music21.roman.Minor67Default "music21.roman.Minor67Default"):

    ```python
    >>> majorSharpSeven = roman.RomanNumeral('VII', em, seventhMinor=roman.Minor67Default.SHARP)
    >>> cp(majorSharpSeven)
    ['D#5', 'F##5', 'A#5']
    ```

    For instance, if you prefer a harmonic minor context where VI (or vi) always refers
    to the lowered 6 and viio (or VII) always refers to the raised 7, send along
    sixthMinor=roman.Minor67Default.FLAT and seventhMinor=roman.Minor67Default.SHARP

    ```python
    >>> dimHarmonicSeven = roman.RomanNumeral('viio', em, seventhMinor=roman.Minor67Default.SHARP)
    >>> cp(dimHarmonicSeven)
    ['D#5', 'F#5', 'A5']
    ```

    ```python
    >>> majHarmonicSeven = roman.RomanNumeral('bVII', em, seventhMinor=roman.Minor67Default.SHARP)
    >>> cp(majHarmonicSeven)
    ['D5', 'F#5', 'A5']
    ```

    ```python
    >>> majHarmonicSix = roman.RomanNumeral('VI', em, sixthMinor=roman.Minor67Default.FLAT)
    >>> cp(majHarmonicSix)
    ['C5', 'E5', 'G5']
    >>> minHarmonicSix = roman.RomanNumeral('#vi', em, sixthMinor=roman.Minor67Default.FLAT)
    >>> cp(minHarmonicSix)
    ['C#5', 'E5', 'G#5']
    ```

    See the docs for [`Minor67Default`](#music21.roman.Minor67Default "music21.roman.Minor67Default") for more information on
    configuring sixth and seventh interpretation in minor
    along with the useful CAUTIONARY setting where CAUTIONARY sharp and flat accidentals
    are allowed but not required.

    Either of these is the same way of getting a minor iii in a minor key:

    ```python
    >>> minoriii = roman.RomanNumeral('iii', em, caseMatters=True)
    >>> cp(minoriii)
    ['G4', 'B-4', 'D5']
    ```

    ```python
    >>> minoriiiB = roman.RomanNumeral('IIIb', em, caseMatters=False)
    >>> cp(minoriiiB)
    ['G4', 'B-4', 'D5']
    ```

    caseMatters=False will prevent sixthMinor or seventhMinor from having effect.

    ```python
    >>> vii = roman.RomanNumeral('viio', 'a', caseMatters=False,
    ...                           seventhMinor=roman.Minor67Default.QUALITY)
    >>> cp(vii)
    ['G5', 'B-5', 'D-6']
    ```

    Can also take a scale object, here we build a first-inversion chord
    on the raised-three degree of D-flat major, that is, F#-major (late
    Schubert would be proud.)

    ```python
    >>> sharp3 = roman.RomanNumeral('#III6', scale.MajorScale('D-'))
    >>> sharp3.scaleDegreeWithAlteration
    (3, <music21.pitch.Accidental sharp>)
    ```

    ```python
    >>> cp(sharp3)
    ['A#4', 'C#5', 'F#5']
    ```

    ```python
    >>> sharp3.figure
    '#III6'
    ```

    Figures can be changed and pitches will change. (Caution: there are still some bugs on this
    for extreme edge cases).

    ```python
    >>> sharp3.figure = 'V'
    >>> cp(sharp3)
    ['A-4', 'C5', 'E-5']
    ```

    A diminished chord is specified with an o (the letter-O) or ° symbol:

    ```python
    >>> leadingToneSeventh = roman.RomanNumeral(
    ...     'viio', scale.MajorScale('F'))
    >>> cp(leadingToneSeventh)
    ['E5', 'G5', 'B-5']
    >>> cp(roman.RomanNumeral('vii°7', 'F'))
    ['E5', 'G5', 'B-5', 'D-6']
    ```

    Note in the above example we passed in a Scale object not a Key. This can be used
    in the theoretical case of applying roman numerals in 7-note scales that are not
    major or minor. (see the documentation for the
    [`scaleCardinality`](#music21.roman.RomanNumeral.scaleCardinality "music21.roman.RomanNumeral.scaleCardinality") attribute for scales other than
    7-note scales).

    Half-diminished seventh chords can be written with either ø or /o symbol:

    ```python
    >>> cp(roman.RomanNumeral('viiø7', 'F'))
    ['E5', 'G5', 'B-5', 'D6']
    >>> cp(roman.RomanNumeral('vii/o7', 'F'))
    ['E5', 'G5', 'B-5', 'D6']
    ```

    RomanNumeral objects can also be created with an int (number)
    for the scale degree:

    ```python
    >>> majorKeyObj = key.Key('C')
    >>> roman.RomanNumeral(1, majorKeyObj)
    <music21.roman.RomanNumeral I in C major>
    ```

    ```python
    >>> minorKeyObj = key.Key('c')
    >>> roman.RomanNumeral(1, minorKeyObj)
    <music21.roman.RomanNumeral i in c minor>
    ```

    A little modal mixture:

    ```python
    >>> lessObviousDiminished = roman.RomanNumeral(
    ...     'vio', scale.MajorScale('c'))
    >>> for p in lessObviousDiminished.pitches:
    ...     p
    <music21.pitch.Pitch A4>
    <music21.pitch.Pitch C5>
    <music21.pitch.Pitch E-5>
    ```

    ```python
    >>> diminished7th = roman.RomanNumeral(
    ...     'vio7', scale.MajorScale('c'))
    >>> for p in diminished7th.pitches:
    ...     p
    <music21.pitch.Pitch A4>
    <music21.pitch.Pitch C5>
    <music21.pitch.Pitch E-5>
    <music21.pitch.Pitch G-5>
    ```

    ```python
    >>> diminished7th1stInv = roman.RomanNumeral(
    ...     'vio65', scale.MajorScale('c'))
    >>> for p in diminished7th1stInv.pitches:
    ...     p
    <music21.pitch.Pitch C4>
    <music21.pitch.Pitch E-4>
    <music21.pitch.Pitch G-4>
    <music21.pitch.Pitch A4>
    ```

    ```python
    >>> halfDim7th2ndInv = roman.RomanNumeral(
    ...     'ivø43', scale.MajorScale('F'))
    >>> for p in halfDim7th2ndInv.pitches:
    ...     p
    <music21.pitch.Pitch F-4>
    <music21.pitch.Pitch A-4>
    <music21.pitch.Pitch B-4>
    <music21.pitch.Pitch D-5>
    ```

    ```python
    >>> alteredChordHalfDim3rdInv = roman.RomanNumeral(
    ...     'biiø42', scale.MajorScale('F'))
    >>> cp(alteredChordHalfDim3rdInv)
    ['F-4', 'G-4', 'B--4', 'D--5']
    ```

    ```python
    >>> alteredChordHalfDim3rdInv.intervalVector
    [0, 1, 2, 1, 1, 1]
    ```

    ```python
    >>> alteredChordHalfDim3rdInv.commonName
    'half-diminished seventh chord'
    ```

    ```python
    >>> alteredChordHalfDim3rdInv.romanNumeral
    'bii'
    ```

    ```python
    >>> alteredChordHalfDim3rdInv.romanNumeralAlone
    'ii'
    ```

    Tones may be omitted by putting the number in a bracketed [noX] clause.
    These numbers refer to the note above the root, not above the bass:

    ```python
    >>> openFifth = roman.RomanNumeral('V[no3]', key.Key('F'))
    >>> openFifth.pitches
    (<music21.pitch.Pitch C5>, <music21.pitch.Pitch G5>)
    >>> openFifthInv = roman.RomanNumeral('V64[no3]', key.Key('F'))
    >>> openFifthInv.pitches
    (<music21.pitch.Pitch G4>, <music21.pitch.Pitch C5>)
    ```

    Some theoretical traditions express a viio7 as a V9 chord with omitted
    root. Music21 allows that:

    ```python
    >>> fiveOhNine = roman.RomanNumeral('V9[no1]', key.Key('g'))
    >>> cp(fiveOhNine)
    ['F#5', 'A5', 'C6', 'E-6']
    ```

    Putting [no] or [add] should never change the root

    ```python
    >>> fiveOhNine.root()
    <music21.pitch.Pitch D5>
    ```

    Tones may be added by putting a number (with an optional accidental) in
    a bracketed [addX] clause:

    ```python
    >>> susChord = roman.RomanNumeral('I[add4][no3]', key.Key('C'))
    >>> susChord.pitches
    (<music21.pitch.Pitch C4>, <music21.pitch.Pitch F4>, <music21.pitch.Pitch G4>)
    >>> susChord.root()
    <music21.pitch.Pitch C4>
    ```

    Figures such as ‘V54’ give the same result:

    ```python
    >>> anotherSus = roman.RomanNumeral('V54', key.Key('C'))
    >>> anotherSus.pitches
    (<music21.pitch.Pitch G4>, <music21.pitch.Pitch C5>, <music21.pitch.Pitch D5>)
    ```

    Putting it all together:

    ```python
    >>> weirdChord = roman.RomanNumeral('V65[no5][add#6][b3]', key.Key('C'))
    >>> cp(weirdChord)
    ['B-4', 'E#5', 'F5', 'G5']
    >>> weirdChord.root()
    <music21.pitch.Pitch G5>
    ```

    Other scales besides major and minor can be used.
    Just for kicks (no worries if this is goobley-gook):

    ```python
    >>> ots = scale.OctatonicScale('C2')
    >>> rn_I9 = roman.RomanNumeral('I9', ots, caseMatters=False)
    >>> cp(rn_I9)
    ['C2', 'E-2', 'G-2', 'A2', 'C3']
    ```

    ```python
    >>> romanNumeral2 = roman.RomanNumeral(
    ...     'V7#5b3', ots, caseMatters=False)
    >>> cp(romanNumeral2)
    ['G-2', 'A-2', 'C#3', 'E-3']
    ```

    ```python
    >>> rn_minor_64_secondary = roman.RomanNumeral('v64/V', key.Key('e'))
    >>> rn_minor_64_secondary
    <music21.roman.RomanNumeral v64/V in e minor>
    ```

    ```python
    >>> rn_minor_64_secondary.figure
    'v64/V'
    ```

    ```python
    >>> cp(rn_minor_64_secondary)
    ['C#5', 'F#5', 'A5']
    ```

    ```python
    >>> rn_minor_64_secondary.secondaryRomanNumeral
    <music21.roman.RomanNumeral V in e minor>
    ```

    Dominant 7ths can be specified by the character ‘d’ followed by the figure
    indicating the inversion of the chord:

    ```python
    >>> r = roman.RomanNumeral('bVIId7', key.Key('B-'))
    >>> r.figure
    'bVIId7'
    ```

    ```python
    >>> cp(r)
    ['A-5', 'C6', 'E-6', 'G-6']
    ```

    ```python
    >>> r = roman.RomanNumeral('VId42')
    >>> r.figure
    'VId42'
    ```

    ```python
    >>> r.key = key.Key('B-')
    >>> cp(r)
    ['F5', 'G5', 'B5', 'D6']
    ```

    ```python
    >>> r = roman.RomanNumeral('IVd43', key.Key('B-'))
    >>> r.figure
    'IVd43'
    ```

    ```python
    >>> cp(r)
    ['B-4', 'D-5', 'E-5', 'G5']
    ```

    ```python
    >>> r2 = roman.RomanNumeral('V42/V7/vi', key.Key('C'))
    >>> cp(r2)
    ['A4', 'B4', 'D#5', 'F#5']
    ```

    ```python
    >>> r2.secondaryRomanNumeral
    <music21.roman.RomanNumeral V7/vi in C major>
    ```

    ```python
    >>> r2.secondaryRomanNumeral.secondaryRomanNumeral
    <music21.roman.RomanNumeral vi in C major>
    ```

    The I64 chord can also be specified as Cad64, which
    simply parses as I64:

    ```python
    >>> r = roman.RomanNumeral('Cad64', key.Key('C'))
    >>> r
    <music21.roman.RomanNumeral Cad64 in C major>
    >>> cp(r)
    ['G4', 'C5', 'E5']
    ```

    ```python
    >>> r = roman.RomanNumeral('Cad64', key.Key('c'))
    >>> r
    <music21.roman.RomanNumeral Cad64 in c minor>
    >>> cp(r)
    ['G4', 'C5', 'E-5']
    ```

    Works also for secondary romans:

    ```python
    >>> r = roman.RomanNumeral('Cad64/V', key.Key('c'))
    >>> r
    <music21.roman.RomanNumeral Cad64/V in c minor>
    >>> cp(r)
    ['D5', 'G5', 'B5']
    ```

    In a major context, i7 and iv7 and their inversions are treated as minor-7th
    chords:

    ```python
    >>> r = roman.RomanNumeral('i7', 'C')
    >>> r
    <music21.roman.RomanNumeral i7 in C major>
    >>> cp(r)
    ['C4', 'E-4', 'G4', 'B-4']
    ```

    ```python
    >>> r = roman.RomanNumeral('iv42', 'C')
    >>> cp(r)
    ['E-4', 'F4', 'A-4', 'C5']
    ```

    For a minor-Major 7th chord in major, write it as i[add7] or i7[#7] or another inversion:

    ```python
    >>> minorMajor = roman.RomanNumeral('i[add7]', 'C')
    >>> minorMajor
    <music21.roman.RomanNumeral i[add7] in C major>
    >>> cp(minorMajor)
    ['C4', 'E-4', 'G4', 'B4']
    >>> cp(roman.RomanNumeral('i7[#7]', 'C'))
    ['C4', 'E-4', 'G4', 'B4']
    ```

    Note that this is not the same as i#7, which gives a rather unusual chord in major.

    ```python
    >>> cp(roman.RomanNumeral('i#7', 'C'))
    ['C4', 'E-4', 'G4', 'B#4']
    ```

    In minor, it’s just fine. I mean, just as fine:

    ```python
    >>> cp(roman.RomanNumeral('i#7', 'c'))
    ['C4', 'E-4', 'G4', 'B4']
    ```

    ```python
    >>> cp(roman.RomanNumeral('i42[#7]', 'C'))
    ['B4', 'C5', 'E-5', 'G5']
    ```

    As noted above, Minor-Major 7th chords in minor have a different form in root position:

    ```python
    >>> cp(roman.RomanNumeral('i#7', 'c'))
    ['C4', 'E-4', 'G4', 'B4']
    ```

    (these are both the same)

    ```python
    >>> cp(roman.RomanNumeral('i#753', 'c'))
    ['C4', 'E-4', 'G4', 'B4']
    >>> cp(roman.RomanNumeral('i7[#7]', 'c'))
    ['C4', 'E-4', 'G4', 'B4']
    ```

    Other inversions are the same as with major keys:

    ```python
    >>> cp(roman.RomanNumeral('i65[#7]', 'c'))
    ['E-4', 'G4', 'B4', 'C5']
    >>> cp(roman.RomanNumeral('i43[#7]', 'c'))
    ['G4', 'B4', 'C5', 'E-5']
    ```

    The RomanNumeral constructor accepts a keyword ‘updatePitches’ which is
    passed to harmony.Harmony. By default, it
    is True, but can be set to False to initialize faster if pitches are not needed.

    ```python
    >>> r = roman.RomanNumeral('vio', em, updatePitches=False)
    >>> r.pitches
    ()
    ```

    **Equality**

    Two RomanNumerals compare equal if their NotRest components
    (noteheads, beams, expressions, articulations, etc.) are equal
    and if their figures and keys are equal:

    ```python
    >>> c1 = chord.Chord('C4 E4 G4 C5')
    >>> c2 = chord.Chord('C3 E4 G4')
    >>> rn1 = roman.romanNumeralFromChord(c1, 'C')
    >>> rn2 = roman.romanNumeralFromChord(c2, 'C')
    >>> rn1 == rn2
    True
    >>> rn1.duration.type = 'half'
    >>> rn1 == rn2
    False
    >>> rn3 = roman.RomanNumeral('I', 'd')
    >>> rn2 == rn3
    False
    >>> rn3.key = key.Key('C')
    >>> rn2 == rn3
    True
    >>> rn4 = roman.RomanNumeral('ii', 'C')
    >>> rn2 == rn4
    False
    >>> rn4.figure = 'I'
    >>> rn2 == rn4
    True
    ```

    ```python
    >>> rn5 = roman.RomanNumeral('bII6', 'c')
    >>> rn6 = roman.RomanNumeral('bII6', 'c')
    >>> rn5 == rn6
    True
    >>> rn7 = roman.RomanNumeral('N6', 'c')
    >>> rn5 == rn7
    False
    ```

    * Changed in v6.5: caseMatters is keyword only. It along with sixthMinor and
      seventhMinor are now the only allowable keywords to pass in.
    * Changed in v7: RomanNumeral.romanNumeral will always give a “b” for a flattened
      degree (i.e., ‘-II’ becomes ‘bII’) as this is what people expect in looking at
      the figure.
    * Changed in v7.3: figures that are not normally used to indicate inversion
      such as V54 (a suspension) no longer give strange inversions.
    * Changed in v8: Figures are now validated as alphanumeric or containing one of
      the following symbols (after the example “V”):

    ```python
    >>> specialCharacterFigure = roman.RomanNumeral('V#+-/[]')
    >>> specialCharacterFigure
    <music21.roman.RomanNumeral V#+-/[]>
    ```

    And degree symbols (°) convert to o:

    ```python
    >>> dimSeventh = roman.RomanNumeral('vii°7', 'c')
    >>> dimSeventh
    <music21.roman.RomanNumeral viio7 in c minor>
    ```

    Otherwise, an invalid figure raises RomanNumeralException:

    ```python
    >>> roman.RomanNumeral("V64==53")
    Traceback (most recent call last):
    music21.roman.RomanNumeralException: Invalid figure: V64==53
    ```

[`RomanNumeral`](#music21.roman.RomanNumeral "music21.roman.RomanNumeral") bases

* [`Harmony`](moduleHarmony.html#music21.harmony.Harmony "music21.harmony.Harmony")
* [`Chord`](moduleChord.html#music21.chord.Chord "music21.chord.Chord")
* [`ChordBase`](moduleChord.html#music21.chord.ChordBase "music21.chord.ChordBase")
* [`NotRest`](moduleNote.html#music21.note.NotRest "music21.note.NotRest")
* [`GeneralNote`](moduleNote.html#music21.note.GeneralNote "music21.note.GeneralNote")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`RomanNumeral`](#music21.roman.RomanNumeral "music21.roman.RomanNumeral") read-only properties

RomanNumeral.figureAndKey
:   Returns the figure and the key and mode as a string

    ```python
    >>> rn = roman.RomanNumeral('V65/V', 'e')
    >>> rn.figureAndKey
    'V65/V in e minor'
    ```

    Without a key, it is the same as figure:

    ```python
    >>> roman.RomanNumeral('V7').figureAndKey
    'V7'
    ```

RomanNumeral.scaleDegreeWithAlteration
:   Returns a two element tuple of the scale degree and the
    accidental that alters the scale degree for things such as #ii or
    bV.

    Note that vi and vii in minor have a frontAlterationAccidental of
    <sharp> even if it is not preceded by a # sign.

    Has the same effect as setting .scaleDegree and
    .frontAlterationAccidental separately

    ```python
    >>> v = roman.RomanNumeral('V', 'C')
    >>> v.scaleDegreeWithAlteration
    (5, None)
    ```

    ```python
    >>> neapolitan = roman.RomanNumeral('N6', 'c#')
    >>> neapolitan.scaleDegreeWithAlteration
    (2, <music21.pitch.Accidental flat>)
    ```

Read-only properties inherited from [`Chord`](moduleChord.html#music21.chord.Chord "music21.chord.Chord"):

|  |  |  |
| --- | --- | --- |
| * [`chordTablesAddress`](moduleChord.html#music21.chord.Chord.chordTablesAddress "music21.chord.Chord.chordTablesAddress") * [`commonName`](moduleChord.html#music21.chord.Chord.commonName "music21.chord.Chord.commonName") * [`fifth`](moduleChord.html#music21.chord.Chord.fifth "music21.chord.Chord.fifth") * [`forteClass`](moduleChord.html#music21.chord.Chord.forteClass "music21.chord.Chord.forteClass") * [`forteClassNumber`](moduleChord.html#music21.chord.Chord.forteClassNumber "music21.chord.Chord.forteClassNumber") * [`forteClassTn`](moduleChord.html#music21.chord.Chord.forteClassTn "music21.chord.Chord.forteClassTn") * [`forteClassTnI`](moduleChord.html#music21.chord.Chord.forteClassTnI "music21.chord.Chord.forteClassTnI") * [`fullName`](moduleChord.html#music21.chord.Chord.fullName "music21.chord.Chord.fullName") * [`hasZRelation`](moduleChord.html#music21.chord.Chord.hasZRelation "music21.chord.Chord.hasZRelation") | * [`intervalVector`](moduleChord.html#music21.chord.Chord.intervalVector "music21.chord.Chord.intervalVector") * [`intervalVectorString`](moduleChord.html#music21.chord.Chord.intervalVectorString "music21.chord.Chord.intervalVectorString") * [`isPrimeFormInversion`](moduleChord.html#music21.chord.Chord.isPrimeFormInversion "music21.chord.Chord.isPrimeFormInversion") * [`multisetCardinality`](moduleChord.html#music21.chord.Chord.multisetCardinality "music21.chord.Chord.multisetCardinality") * [`normalOrder`](moduleChord.html#music21.chord.Chord.normalOrder "music21.chord.Chord.normalOrder") * [`normalOrderString`](moduleChord.html#music21.chord.Chord.normalOrderString "music21.chord.Chord.normalOrderString") * [`orderedPitchClasses`](moduleChord.html#music21.chord.Chord.orderedPitchClasses "music21.chord.Chord.orderedPitchClasses") * [`orderedPitchClassesString`](moduleChord.html#music21.chord.Chord.orderedPitchClassesString "music21.chord.Chord.orderedPitchClassesString") * [`pitchClassCardinality`](moduleChord.html#music21.chord.Chord.pitchClassCardinality "music21.chord.Chord.pitchClassCardinality") | * [`pitchClasses`](moduleChord.html#music21.chord.Chord.pitchClasses "music21.chord.Chord.pitchClasses") * [`pitchedCommonName`](moduleChord.html#music21.chord.Chord.pitchedCommonName "music21.chord.Chord.pitchedCommonName") * [`primeForm`](moduleChord.html#music21.chord.Chord.primeForm "music21.chord.Chord.primeForm") * [`primeFormString`](moduleChord.html#music21.chord.Chord.primeFormString "music21.chord.Chord.primeFormString") * [`quality`](moduleChord.html#music21.chord.Chord.quality "music21.chord.Chord.quality") * [`scaleDegrees`](moduleChord.html#music21.chord.Chord.scaleDegrees "music21.chord.Chord.scaleDegrees") * [`seventh`](moduleChord.html#music21.chord.Chord.seventh "music21.chord.Chord.seventh") * [`third`](moduleChord.html#music21.chord.Chord.third "music21.chord.Chord.third") |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`RomanNumeral`](#music21.roman.RomanNumeral "music21.roman.RomanNumeral") read/write properties

RomanNumeral.figure
:   Gives a string representation of the roman numeral, which
    is usually the same as what you passed in as a string:

    ```python
    >>> roman.RomanNumeral('bVII65/V', 'C').figure
    'bVII65/V'
    ```

    There are a few exceptions. If the RomanNumeral is initialized
    with an int, then it is converted to a string:

    ```python
    >>> roman.RomanNumeral(2).figure
    'II'
    ```

    A 0 used for o in a diminished seventh chord is converted to o,
    and the /o form of half-diminished is converted to ø:

    ```python
    >>> roman.RomanNumeral('vii07').figure
    'viio7'
    >>> roman.RomanNumeral('vii/o7').figure
    'viiø7'
    ```

    Changing this value will not change existing pitches.

    * Changed in v6.5: empty RomanNumerals now have figure of ‘’ not None

RomanNumeral.functionalityScore
:   Return or set a number from 1 to 100 representing the relative
    functionality of this RN.figure (possibly given the mode, etc.).

    Numbers are ordinal, not cardinal.

    ```python
    >>> rn1 = roman.RomanNumeral('V7')
    >>> rn1.functionalityScore
    80
    ```

    ```python
    >>> rn2 = roman.RomanNumeral('vi6')
    >>> rn2.functionalityScore
    10
    ```

    ```python
    >>> rn2.functionalityScore = 99
    >>> rn2.functionalityScore
    99
    ```

    For secondary dominants, the functionality scores are multiplied, reducing
    all but the first by 1/100th:

    ```python
    >>> rn3 = roman.RomanNumeral('V')
    >>> rn3.functionalityScore
    70
    ```

    ```python
    >>> rn4 = roman.RomanNumeral('vi')
    >>> rn4.functionalityScore
    40
    ```

    ```python
    >>> rn5 = roman.RomanNumeral('V/vi')
    >>> rn5.functionalityScore
    28
    ```

RomanNumeral.key
:   Gets or Sets the current Key (or Scale object) for a given
    RomanNumeral object.

    If a new key is set, then the pitches will probably change:

    ```python
    >>> r1 = roman.RomanNumeral('V')
    ```

    (No key means an implicit C-major)

    ```python
    >>> r1.key is None
    True
    ```

    ```python
    >>> [str(p) for p in r1.pitches]
    ['G4', 'B4', 'D5']
    ```

    Change to A major

    ```python
    >>> r1.key = key.Key('A')
    >>> [str(p) for p in r1.pitches]
    ['E5', 'G#5', 'B5']
    ```

    ```python
    >>> r1
    <music21.roman.RomanNumeral V in A major>
    ```

    ```python
    >>> r1.key
    <music21.key.Key of A major>
    ```

    ```python
    >>> r1.key = key.Key('e')
    >>> [str(p) for p in r1.pitches]
    ['B4', 'D#5', 'F#5']
    ```

    ```python
    >>> r1
    <music21.roman.RomanNumeral V in e minor>
    ```

RomanNumeral.romanNumeral
:   Read-only property that returns either the romanNumeralAlone (e.g. just
    II) or the frontAlterationAccidental.modifier (with ‘b’ for ‘-’) + romanNumeralAlone
    (e.g. #II, bII)

    ```python
    >>> rn = roman.RomanNumeral('#II7')
    >>> rn.romanNumeral
    '#II'
    ```

    ```python
    >>> rn = roman.RomanNumeral('Ger+6')
    >>> rn.romanNumeral
    'Ger'
    ```

    ```python
    >>> rn = roman.RomanNumeral('bbII/V')
    >>> rn.romanNumeral
    'bbII'
    >>> rn = roman.RomanNumeral('--II/V')
    >>> rn.romanNumeral
    'bbII'
    ```

Read/write properties inherited from [`Harmony`](moduleHarmony.html#music21.harmony.Harmony "music21.harmony.Harmony"):

|  |  |  |
| --- | --- | --- |
| * [`writeAsChord`](moduleHarmony.html#music21.harmony.Harmony.writeAsChord "music21.harmony.Harmony.writeAsChord") |  |  |

Read/write properties inherited from [`Chord`](moduleChord.html#music21.chord.Chord "music21.chord.Chord"):

|  |  |  |
| --- | --- | --- |
| * [`duration`](moduleChord.html#music21.chord.Chord.duration "music21.chord.Chord.duration") * [`notes`](moduleChord.html#music21.chord.Chord.notes "music21.chord.Chord.notes") | * [`pitchNames`](moduleChord.html#music21.chord.Chord.pitchNames "music21.chord.Chord.pitchNames") | * [`pitches`](moduleChord.html#music21.chord.Chord.pitches "music21.chord.Chord.pitches") |

Read/write properties inherited from [`ChordBase`](moduleChord.html#music21.chord.ChordBase "music21.chord.ChordBase"):

|  |  |  |
| --- | --- | --- |
| * [`tie`](moduleChord.html#music21.chord.ChordBase.tie "music21.chord.ChordBase.tie") | * [`volume`](moduleChord.html#music21.chord.ChordBase.volume "music21.chord.ChordBase.volume") |  |

Read/write properties inherited from [`NotRest`](moduleNote.html#music21.note.NotRest "music21.note.NotRest"):

|  |  |  |
| --- | --- | --- |
| * [`notehead`](moduleNote.html#music21.note.NotRest.notehead "music21.note.NotRest.notehead") * [`noteheadFill`](moduleNote.html#music21.note.NotRest.noteheadFill "music21.note.NotRest.noteheadFill") | * [`noteheadParenthesis`](moduleNote.html#music21.note.NotRest.noteheadParenthesis "music21.note.NotRest.noteheadParenthesis") * [`stemDirection`](moduleNote.html#music21.note.NotRest.stemDirection "music21.note.NotRest.stemDirection") | * [`storedInstrument`](moduleNote.html#music21.note.NotRest.storedInstrument "music21.note.NotRest.storedInstrument") |

Read/write properties inherited from [`GeneralNote`](moduleNote.html#music21.note.GeneralNote "music21.note.GeneralNote"):

|  |  |  |
| --- | --- | --- |
| * [`lyric`](moduleNote.html#music21.note.GeneralNote.lyric "music21.note.GeneralNote.lyric") |  |  |

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`RomanNumeral`](#music21.roman.RomanNumeral "music21.roman.RomanNumeral") methods

RomanNumeral.\_\_eq\_\_(*other*)[[source]](../_modules/music21/roman.html#RomanNumeral.__eq__)
:   Compare equality, just based on NotRest and on figure and key

RomanNumeral.adjustMinorVIandVIIByQuality(*useScale: [Key](moduleKey.html#music21.key.Key "music21.key.Key") | [ConcreteScale](moduleScale.html#music21.scale.ConcreteScale "music21.scale.ConcreteScale")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/roman.html#RomanNumeral.adjustMinorVIandVIIByQuality)
:   Fix minor vi and vii to always be #vi and #vii if .caseMatters.

    ```python
    >>> rn = roman.RomanNumeral()
    >>> rn.scaleDegree = 6
    >>> rn.impliedQuality = 'minor'
    >>> rn.adjustMinorVIandVIIByQuality(key.Key('c'))
    >>> rn.frontAlterationTransposeInterval
    <music21.interval.Interval A1>
    ```

    ```python
    >>> rn.frontAlterationAccidental
    <music21.pitch.Accidental sharp>
    ```

    ```python
    >>> rn = roman.RomanNumeral()
    >>> rn.scaleDegree = 6
    >>> rn.impliedQuality = 'major'
    >>> rn.adjustMinorVIandVIIByQuality(key.Key('c'))
    >>> rn.frontAlterationTransposeInterval is None
    True
    >>> rn.frontAlterationAccidental is None
    True
    ```

    Note that this function is not called in parsing, but a private function having the
    guts of this function is called.

    * Changed in v6.4: public function became hook to private function having the actual guts

RomanNumeral.bassScaleDegreeFromNotation(*notationObject: [Notation](moduleFiguredBassNotation.html#music21.figuredBass.notation.Notation "music21.figuredBass.notation.Notation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](../_modules/music21/roman.html#RomanNumeral.bassScaleDegreeFromNotation)
:   Given a notationObject from
    [`music21.figuredBass.notation.Notation`](moduleFiguredBassNotation.html#music21.figuredBass.notation.Notation "music21.figuredBass.notation.Notation")
    return the scaleDegree of the bass.

    ```python
    >>> fbn = figuredBass.notation.Notation('6,3')
    >>> V = roman.RomanNumeral('V')
    >>> V.bassScaleDegreeFromNotation(fbn)
    7
    ```

    ```python
    >>> fbn2 = figuredBass.notation.Notation('#6,4')
    >>> vi = roman.RomanNumeral('vi')
    >>> vi.bassScaleDegreeFromNotation(fbn2)
    3
    ```

    Can figure it out directly from an existing RomanNumeral:

    ```python
    >>> ii65 = roman.RomanNumeral('ii65', 'C')
    >>> ii65.bassScaleDegreeFromNotation()
    4
    ```

    Simple test:

    ```python
    >>> I = roman.RomanNumeral('I')
    >>> I.bassScaleDegreeFromNotation()
    1
    ```

    Figures that do not imply a bass like 54 just return the instance
    [`scaleDegree`](#music21.roman.RomanNumeral.scaleDegree "music21.roman.RomanNumeral.scaleDegree"):

    ```python
    >>> V = roman.RomanNumeral('V54')
    >>> V.bassScaleDegreeFromNotation()
    5
    ```

RomanNumeral.isMixture(*evaluateSecondaryNumeral: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*)[[source]](../_modules/music21/roman.html#RomanNumeral.isMixture)
:   Checks if a RomanNumeral is an instance of ‘modal mixture’ in which the chord is
    not diatonic in the key specified, but
    would be in the parallel (German: variant) major / minor
    and can therefore be thought of as a ‘mixture’ of major and minor modes, or
    as a ‘borrowing’ from the one to the other.

    Examples include “i” in major or “I” in minor (*sic*).

    Specifically, this method returns True for all and only the following cases in any
    inversion:

    Major context (example of C major):

    * scale degree 1 and triad quality minor (minor tonic chord, c);
    * scale degree 2 and triad quality diminished (covers both iio and iiø7);
    * scale degree b3 and triad quality major (Eb);
    * scale degree 4 and triad quality minor (f);
    * scale degree 5 and triad quality minor (g, NB: potentially controversial);
    * scale degree b6 and triad quality major (Ab);
    * scale degree b7 and triad quality major (Bb); and
    * scale degree 7, and it is a diminished seventh (specifically b-d-f-ab).

    Minor context (example of c minor):

    * scale degree 1 and triad quality major (major tonic chord, C);
    * scale degree 2 and triad quality minor (d, not diminished);
    * scale degree #3 and triad quality minor (e);
    * scale degree 4 and triad quality major (F);
    * scale degree #6 and triad quality minor (a); and
    * scale degree 7, and it is a half-diminished seventh (specifically b-d-f-a).

    This list is broadly consistent with (and limited to) borrowing between the major and
    natural minor, except for excluding V (G-B-D) and viio (B-D-F) in minor.
    There are several borderline caes and this in-/exclusion is all open to debate, of course.
    The choices here reflect this method’s primarily goal to aid anthologizing and
    pointing to clear cases of mixture in common practice Classical music.
    At least in that context, V and viio are not generally regarded as mixure.

    By way of example usage, here are both major and minor versions of the
    tonic and subdominant triads in the major context.

    ```python
    >>> roman.RomanNumeral('I', 'D-').isMixture()
    False
    ```

    ```python
    >>> roman.RomanNumeral('i', 'D-').isMixture()
    True
    ```

    ```python
    >>> roman.RomanNumeral('IV', 'F').isMixture()
    False
    ```

    ```python
    >>> roman.RomanNumeral('iv', 'F').isMixture()
    True
    ```

    For any cases extending beyond triad/seventh chords, major/minor keys,
    and the like, this method simply returns False.

    So when the mode is not major or minor (including when it’s undefined), that’s False.

    ```python
    >>> rn = roman.RomanNumeral('iv', 'C')
    >>> rn.key.mode
    'major'
    ```

    ```python
    >>> rn.isMixture()
    True
    ```

    ```python
    >>> rn.key.mode = 'hypomixolydian'
    >>> rn.isMixture()
    False
    ```

    A scale for a key never returns True for mixture.

    ```python
    >>> rn = roman.RomanNumeral('i', scale.MajorScale('D'))  # mode undefined
    >>> rn.isMixture()
    False
    ```

    Likewise, anything that’s not a triad or seventh will return False:

    ```python
    >>> rn = roman.romanNumeralFromChord(chord.Chord("C D E"))
    >>> rn.isMixture()
    False
    ```

    Note that Augmented sixth chords do count as sevenths but never indicate modal mixture
    (not least because those augmented sixths are the same in both major and minor).

    ```python
    >>> rn = roman.RomanNumeral('Ger65')
    >>> rn.isSeventh()
    True
    ```

    ```python
    >>> rn.isMixture()
    False
    ```

    False is also returned for any case in which the triad quality is not
    diminished, minor, or major:

    ```python
    >>> rn = roman.RomanNumeral('bIII+')
    >>> rn.quality
    'augmented'
    ```

    ```python
    >>> rn.isMixture()
    False
    ```

    (That specific example of bIII+ in major is a borderline case that
    arguably ought to be included and may be added later without a deprecation cycle.)

    Naturally, really extended usages such as scale degrees beyond 7 (in the
    Octatonic mode, for instance) also return False.

    The evaluateSecondaryNumeral parameter allows users to choose whether to consider
    secondary Roman numerals (like V/vi) or to ignore them.
    When considered, exactly the same rules apply but recasting the comparison on
    the secondaryRomanNumeral.
    This is an extended usage that is open to debate and liable to change.

    ```python
    >>> roman.RomanNumeral('V/bVI', 'E-').isMixture()
    False
    ```

    ```python
    >>> roman.RomanNumeral('V/bVI', 'E-').isMixture(evaluateSecondaryNumeral=True)
    True
    ```

    In case of secondary numeral chains, read the last one for mixture.

    ```python
    >>> roman.RomanNumeral('V/V/bVI', 'E-').isMixture(evaluateSecondaryNumeral=True)
    True
    ```

RomanNumeral.isNeapolitan(*require1stInversion: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*)[[source]](../_modules/music21/roman.html#RomanNumeral.isNeapolitan)
:   Music21’s Chord class contains methods for identifying chords of a particular type,
    such as [`isAugmentedSixth()`](moduleChord.html#music21.chord.Chord.isAugmentedSixth "music21.chord.Chord.isAugmentedSixth").

    Some similar chord types are defined not only by the structure of a chord but
    by its relation to a key.
    The Neapolitan sixth is a notable example.
    A chord is a Neapolitan sixth if it is a major triad, in first inversion, and
    (here’s the key-dependent part) rooted on the flattened second scale degree.

    ```python
    >>> chd = chord.Chord(['F4', 'Ab4', 'Db5'])
    >>> rn = roman.romanNumeralFromChord(chd, 'C')
    >>> rn.isNeapolitan()
    True
    ```

    As this is key-dependent, changing the key changes the outcome.

    ```python
    >>> rn = roman.romanNumeralFromChord(chd, 'Db')
    >>> rn.isNeapolitan()
    False
    ```

    The ‘N’, ‘N6’ and ‘N53’ shorthand forms are accepted.

    ```python
    >>> rn = roman.RomanNumeral('N')
    >>> rn.isNeapolitan()
    True
    ```

    ```python
    >>> rn = roman.RomanNumeral('N6')
    >>> rn.isNeapolitan()
    True
    ```

    Requiring first inversion is optional.

    ```python
    >>> rn = roman.RomanNumeral('bII')
    >>> rn.isNeapolitan(require1stInversion=False)
    True
    ```

    ```python
    >>> rn = roman.RomanNumeral('N53')
    >>> rn.isNeapolitan(require1stInversion=False)
    True
    ```

RomanNumeral.transpose(*value*, *\**, *inPlace=False*) → [Self](https://docs.python.org/3/library/typing.html#typing.Self "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/roman.html#RomanNumeral.transpose)
:   Overrides `transpose()` so that key
    attribute is transposed as well.

    ```python
    >>> rn = roman.RomanNumeral('I', 'C')
    >>> rn
    <music21.roman.RomanNumeral I in C major>
    >>> rn.transpose(4)
    <music21.roman.RomanNumeral I in E major>
    >>> rn.transpose(-4, inPlace=True)
    >>> rn
    <music21.roman.RomanNumeral I in A- major>
    ```

Methods inherited from [`Harmony`](moduleHarmony.html#music21.harmony.Harmony "music21.harmony.Harmony"):

|  |  |  |
| --- | --- | --- |
| * [`addChordStepModification()`](moduleHarmony.html#music21.harmony.Harmony.addChordStepModification "music21.harmony.Harmony.addChordStepModification") | * [`findFigure()`](moduleHarmony.html#music21.harmony.Harmony.findFigure "music21.harmony.Harmony.findFigure") | * [`getChordStepModifications()`](moduleHarmony.html#music21.harmony.Harmony.getChordStepModifications "music21.harmony.Harmony.getChordStepModifications") |

Methods inherited from [`Chord`](moduleChord.html#music21.chord.Chord "music21.chord.Chord"):

|  |  |  |
| --- | --- | --- |
| * [`__getitem__()`](moduleChord.html#music21.chord.Chord.__getitem__ "music21.chord.Chord.__getitem__") * [`add()`](moduleChord.html#music21.chord.Chord.add "music21.chord.Chord.add") * [`annotateIntervals()`](moduleChord.html#music21.chord.Chord.annotateIntervals "music21.chord.Chord.annotateIntervals") * [`areZRelations()`](moduleChord.html#music21.chord.Chord.areZRelations "music21.chord.Chord.areZRelations") * [`bass()`](moduleChord.html#music21.chord.Chord.bass "music21.chord.Chord.bass") * [`canBeDominantV()`](moduleChord.html#music21.chord.Chord.canBeDominantV "music21.chord.Chord.canBeDominantV") * [`canBeTonic()`](moduleChord.html#music21.chord.Chord.canBeTonic "music21.chord.Chord.canBeTonic") * [`closedPosition()`](moduleChord.html#music21.chord.Chord.closedPosition "music21.chord.Chord.closedPosition") * [`containsSeventh()`](moduleChord.html#music21.chord.Chord.containsSeventh "music21.chord.Chord.containsSeventh") * [`containsTriad()`](moduleChord.html#music21.chord.Chord.containsTriad "music21.chord.Chord.containsTriad") * [`formatVectorString()`](moduleChord.html#music21.chord.Chord.formatVectorString "music21.chord.Chord.formatVectorString") * [`geometricNormalForm()`](moduleChord.html#music21.chord.Chord.geometricNormalForm "music21.chord.Chord.geometricNormalForm") * [`getChordStep()`](moduleChord.html#music21.chord.Chord.getChordStep "music21.chord.Chord.getChordStep") * [`getColor()`](moduleChord.html#music21.chord.Chord.getColor "music21.chord.Chord.getColor") * [`getNotehead()`](moduleChord.html#music21.chord.Chord.getNotehead "music21.chord.Chord.getNotehead") * [`getNoteheadFill()`](moduleChord.html#music21.chord.Chord.getNoteheadFill "music21.chord.Chord.getNoteheadFill") * [`getStemDirection()`](moduleChord.html#music21.chord.Chord.getStemDirection "music21.chord.Chord.getStemDirection") * [`getTie()`](moduleChord.html#music21.chord.Chord.getTie "music21.chord.Chord.getTie") * [`getVolume()`](moduleChord.html#music21.chord.Chord.getVolume "music21.chord.Chord.getVolume") * [`getZRelation()`](moduleChord.html#music21.chord.Chord.getZRelation "music21.chord.Chord.getZRelation") * [`hasAnyEnharmonicSpelledPitches()`](moduleChord.html#music21.chord.Chord.hasAnyEnharmonicSpelledPitches "music21.chord.Chord.hasAnyEnharmonicSpelledPitches") * [`hasAnyRepeatedDiatonicNote()`](moduleChord.html#music21.chord.Chord.hasAnyRepeatedDiatonicNote "music21.chord.Chord.hasAnyRepeatedDiatonicNote") | * [`hasRepeatedChordStep()`](moduleChord.html#music21.chord.Chord.hasRepeatedChordStep "music21.chord.Chord.hasRepeatedChordStep") * [`intervalFromChordStep()`](moduleChord.html#music21.chord.Chord.intervalFromChordStep "music21.chord.Chord.intervalFromChordStep") * [`inversion()`](moduleChord.html#music21.chord.Chord.inversion "music21.chord.Chord.inversion") * [`inversionName()`](moduleChord.html#music21.chord.Chord.inversionName "music21.chord.Chord.inversionName") * [`inversionText()`](moduleChord.html#music21.chord.Chord.inversionText "music21.chord.Chord.inversionText") * [`isAugmentedSixth()`](moduleChord.html#music21.chord.Chord.isAugmentedSixth "music21.chord.Chord.isAugmentedSixth") * [`isAugmentedTriad()`](moduleChord.html#music21.chord.Chord.isAugmentedTriad "music21.chord.Chord.isAugmentedTriad") * [`isConsonant()`](moduleChord.html#music21.chord.Chord.isConsonant "music21.chord.Chord.isConsonant") * [`isDiminishedSeventh()`](moduleChord.html#music21.chord.Chord.isDiminishedSeventh "music21.chord.Chord.isDiminishedSeventh") * [`isDiminishedTriad()`](moduleChord.html#music21.chord.Chord.isDiminishedTriad "music21.chord.Chord.isDiminishedTriad") * [`isDominantSeventh()`](moduleChord.html#music21.chord.Chord.isDominantSeventh "music21.chord.Chord.isDominantSeventh") * [`isFalseDiminishedSeventh()`](moduleChord.html#music21.chord.Chord.isFalseDiminishedSeventh "music21.chord.Chord.isFalseDiminishedSeventh") * [`isFrenchAugmentedSixth()`](moduleChord.html#music21.chord.Chord.isFrenchAugmentedSixth "music21.chord.Chord.isFrenchAugmentedSixth") * [`isGermanAugmentedSixth()`](moduleChord.html#music21.chord.Chord.isGermanAugmentedSixth "music21.chord.Chord.isGermanAugmentedSixth") * [`isHalfDiminishedSeventh()`](moduleChord.html#music21.chord.Chord.isHalfDiminishedSeventh "music21.chord.Chord.isHalfDiminishedSeventh") * [`isIncompleteMajorTriad()`](moduleChord.html#music21.chord.Chord.isIncompleteMajorTriad "music21.chord.Chord.isIncompleteMajorTriad") * [`isIncompleteMinorTriad()`](moduleChord.html#music21.chord.Chord.isIncompleteMinorTriad "music21.chord.Chord.isIncompleteMinorTriad") * [`isItalianAugmentedSixth()`](moduleChord.html#music21.chord.Chord.isItalianAugmentedSixth "music21.chord.Chord.isItalianAugmentedSixth") * [`isMajorTriad()`](moduleChord.html#music21.chord.Chord.isMajorTriad "music21.chord.Chord.isMajorTriad") * [`isMinorTriad()`](moduleChord.html#music21.chord.Chord.isMinorTriad "music21.chord.Chord.isMinorTriad") * [`isNinth()`](moduleChord.html#music21.chord.Chord.isNinth "music21.chord.Chord.isNinth") * [`isSeventh()`](moduleChord.html#music21.chord.Chord.isSeventh "music21.chord.Chord.isSeventh") | * [`isSeventhOfType()`](moduleChord.html#music21.chord.Chord.isSeventhOfType "music21.chord.Chord.isSeventhOfType") * [`isSwissAugmentedSixth()`](moduleChord.html#music21.chord.Chord.isSwissAugmentedSixth "music21.chord.Chord.isSwissAugmentedSixth") * [`isTranspositionallySymmetrical()`](moduleChord.html#music21.chord.Chord.isTranspositionallySymmetrical "music21.chord.Chord.isTranspositionallySymmetrical") * [`isTriad()`](moduleChord.html#music21.chord.Chord.isTriad "music21.chord.Chord.isTriad") * [`removeRedundantPitchClasses()`](moduleChord.html#music21.chord.Chord.removeRedundantPitchClasses "music21.chord.Chord.removeRedundantPitchClasses") * [`removeRedundantPitchNames()`](moduleChord.html#music21.chord.Chord.removeRedundantPitchNames "music21.chord.Chord.removeRedundantPitchNames") * [`removeRedundantPitches()`](moduleChord.html#music21.chord.Chord.removeRedundantPitches "music21.chord.Chord.removeRedundantPitches") * [`root()`](moduleChord.html#music21.chord.Chord.root "music21.chord.Chord.root") * [`semiClosedPosition()`](moduleChord.html#music21.chord.Chord.semiClosedPosition "music21.chord.Chord.semiClosedPosition") * [`semitonesFromChordStep()`](moduleChord.html#music21.chord.Chord.semitonesFromChordStep "music21.chord.Chord.semitonesFromChordStep") * [`setColor()`](moduleChord.html#music21.chord.Chord.setColor "music21.chord.Chord.setColor") * [`setNotehead()`](moduleChord.html#music21.chord.Chord.setNotehead "music21.chord.Chord.setNotehead") * [`setNoteheadFill()`](moduleChord.html#music21.chord.Chord.setNoteheadFill "music21.chord.Chord.setNoteheadFill") * [`setStemDirection()`](moduleChord.html#music21.chord.Chord.setStemDirection "music21.chord.Chord.setStemDirection") * [`setTie()`](moduleChord.html#music21.chord.Chord.setTie "music21.chord.Chord.setTie") * [`setVolume()`](moduleChord.html#music21.chord.Chord.setVolume "music21.chord.Chord.setVolume") * [`simplifyEnharmonics()`](moduleChord.html#music21.chord.Chord.simplifyEnharmonics "music21.chord.Chord.simplifyEnharmonics") * [`sortAscending()`](moduleChord.html#music21.chord.Chord.sortAscending "music21.chord.Chord.sortAscending") * [`sortChromaticAscending()`](moduleChord.html#music21.chord.Chord.sortChromaticAscending "music21.chord.Chord.sortChromaticAscending") * [`sortDiatonicAscending()`](moduleChord.html#music21.chord.Chord.sortDiatonicAscending "music21.chord.Chord.sortDiatonicAscending") * [`sortFrequencyAscending()`](moduleChord.html#music21.chord.Chord.sortFrequencyAscending "music21.chord.Chord.sortFrequencyAscending") |

Methods inherited from [`ChordBase`](moduleChord.html#music21.chord.ChordBase "music21.chord.ChordBase"):

|  |  |  |
| --- | --- | --- |
| * [`hasComponentVolumes()`](moduleChord.html#music21.chord.ChordBase.hasComponentVolumes "music21.chord.ChordBase.hasComponentVolumes") | * [`remove()`](moduleChord.html#music21.chord.ChordBase.remove "music21.chord.ChordBase.remove") | * [`setVolumes()`](moduleChord.html#music21.chord.ChordBase.setVolumes "music21.chord.ChordBase.setVolumes") |

Methods inherited from [`NotRest`](moduleNote.html#music21.note.NotRest "music21.note.NotRest"):

|  |  |  |
| --- | --- | --- |
| * [`getInstrument()`](moduleNote.html#music21.note.NotRest.getInstrument "music21.note.NotRest.getInstrument") | * [`hasVolumeInformation()`](moduleNote.html#music21.note.NotRest.hasVolumeInformation "music21.note.NotRest.hasVolumeInformation") |  |

Methods inherited from [`GeneralNote`](moduleNote.html#music21.note.GeneralNote "music21.note.GeneralNote"):

|  |  |  |
| --- | --- | --- |
| * [`addLyric()`](moduleNote.html#music21.note.GeneralNote.addLyric "music21.note.GeneralNote.addLyric") * [`augmentOrDiminish()`](moduleNote.html#music21.note.GeneralNote.augmentOrDiminish "music21.note.GeneralNote.augmentOrDiminish") | * [`getGrace()`](moduleNote.html#music21.note.GeneralNote.getGrace "music21.note.GeneralNote.getGrace") | * [`insertLyric()`](moduleNote.html#music21.note.GeneralNote.insertLyric "music21.note.GeneralNote.insertLyric") |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`RomanNumeral`](#music21.roman.RomanNumeral "music21.roman.RomanNumeral") instance variables

RomanNumeral.addedSteps
:   Returns a list of the added steps, each as a tuple of
    modifier as a string (which might be empty) and a chord factor as an int.

    ```python
    >>> rn = roman.RomanNumeral('V7[addb6]', 'C')
    >>> rn.addedSteps
    [('-', 6)]
    >>> rn.pitches
    (<music21.pitch.Pitch G4>,
    <music21.pitch.Pitch B4>,
    <music21.pitch.Pitch D5>,
    <music21.pitch.Pitch E-5>,
    <music21.pitch.Pitch F5>)
    ```

    You can add multiple added steps:

    ```python
    >>> strange = roman.RomanNumeral('V7[addb6][add#6][add-8]')
    >>> strange.addedSteps
    [('-', 6), ('#', 6), ('-', 8)]
    >>> ' '.join([p.nameWithOctave for p in strange.pitches])
    'G4 B4 D5 E-5 E#5 F5 G-5'
    ```

    NOTE: The modifier name is currently changed from ‘b’ to ‘-’, but
    this might change in a future version to match bracketedAlteration.

RomanNumeral.bracketedAlterations
:   Returns a list of the bracketed alterations, each as a tuple of
    modifier as a string and a chord factor as an int.

    ```python
    >>> rn = roman.RomanNumeral('V7[b5]')
    >>> rn.bracketedAlterations
    [('b', 5)]
    >>> rn.pitches
    (<music21.pitch.Pitch G4>,
    <music21.pitch.Pitch B4>,
    <music21.pitch.Pitch D-5>,
    <music21.pitch.Pitch F5>)
    ```

    NOTE: The bracketed alteration name is currently left as ‘b’, but
    this might change in a future version to match addedSteps.

    The difference between a bracketed alteration and just
    putting b5 in is that, a bracketed alteration changes
    notes already present in a chord and does not imply that
    the normally present notes would be missing. Here, the
    presence of 7 and b5 means that no 3rd should appear.

    ```python
    >>> rn2 = roman.RomanNumeral('V7b5')
    >>> rn2.bracketedAlterations
    []
    >>> len(rn2.pitches)
    3
    >>> [p.name for p in rn2.pitches]
    ['G', 'D-', 'F']
    ```

    * Changed in v6.5: always returns a list, even if it is empty.

RomanNumeral.caseMatters
:   Boolean to determine whether the case (upper or lowercase) of the
    figure determines whether it is major or minor. Defaults to True;
    not everything has been tested with False yet.

    ```python
    >>> roman.RomanNumeral('viiø7', 'd').caseMatters
    True
    ```

RomanNumeral.figuresNotationObj
:   Returns a [`Notation`](moduleFiguredBassNotation.html#music21.figuredBass.notation.Notation "music21.figuredBass.notation.Notation") object
    that represents the figures in a RomanNumeral

    ```python
    >>> rn = roman.RomanNumeral('V65')
    >>> notationObj = rn.figuresNotationObj
    >>> notationObj
    <music21.figuredBass.notation.Notation 6,5>
    >>> notationObj.numbers
    (6, 5, 3)
    ```

    ```python
    >>> rn = roman.RomanNumeral('Ib75#3')
    >>> notationObj = rn.figuresNotationObj
    >>> notationObj.numbers
    (7, 5, 3)
    >>> notationObj.modifiers
    (<music21.figuredBass.notation.Modifier b flat>,
    <music21.figuredBass.notation.Modifier None None>,
    <music21.figuredBass.notation.Modifier # sharp>)
    ```

RomanNumeral.figuresWritten
:   Returns a string containing any figured-bass figures as passed in:

    ```python
    >>> roman.RomanNumeral('V65').figuresWritten
    '65'
    >>> roman.RomanNumeral('V').figuresWritten
    ''
    >>> roman.RomanNumeral('Fr43', 'c').figuresWritten
    '43'
    >>> roman.RomanNumeral('I7#5b3').figuresWritten
    '7#5b3'
    ```

    Note that the o and ø symbols are quality designations and not
    figures:

    ```python
    >>> roman.RomanNumeral('viio6').figuresWritten
    '6'
    >>> roman.RomanNumeral('viiø7').figuresWritten
    '7'
    ```

RomanNumeral.frontAlterationAccidental
:   An optional [`Accidental`](modulePitch.html#music21.pitch.Accidental "music21.pitch.Accidental") object
    representing the chromatic alteration of a RomanNumeral, if any

    ```python
    >>> roman.RomanNumeral('bII43/vi', 'C').frontAlterationAccidental
    <music21.pitch.Accidental flat>
    ```

    ```python
    >>> roman.RomanNumeral('##IV').frontAlterationAccidental
    <music21.pitch.Accidental double-sharp>
    ```

    For most roman numerals this will be None:

    ```python
    >>> roman.RomanNumeral('V', 'f#').frontAlterationAccidental
    ```

    Changing this value will not change existing pitches.

    * Changed in v6.5: always returns a string, never None

RomanNumeral.frontAlterationString
:   A string representing the chromatic alteration of a RomanNumeral, if any

    ```python
    >>> roman.RomanNumeral('bII43/vi', 'C').frontAlterationString
    'b'
    >>> roman.RomanNumeral('V', 'f#').frontAlterationString
    ''
    ```

    Changing this value will not change existing pitches.

    * Changed in v6.5: always returns a string, never None

RomanNumeral.frontAlterationTransposeInterval
:   An optional [`Interval`](moduleInterval.html#music21.interval.Interval "music21.interval.Interval") object
    representing the transposition of a chromatically altered chord from
    the normal scale degree:

    ```python
    >>> sharpFour = roman.RomanNumeral('#IV', 'C')
    >>> sharpFour.frontAlterationTransposeInterval
    <music21.interval.Interval A1>
    >>> sharpFour.frontAlterationTransposeInterval.niceName
    'Augmented Unison'
    ```

    Flats, as in this Neapolitan (bII6) chord, are given as diminished unisons:

    ```python
    >>> roman.RomanNumeral('N6', 'C').frontAlterationTransposeInterval
    <music21.interval.Interval d1>
    ```

    Most RomanNumerals will have None and not a perfect unison for this value
    (this is for the speed of creating objects)

    ```python
    >>> intv = roman.RomanNumeral('V', 'e-').frontAlterationTransposeInterval
    >>> intv is None
    True
    ```

    Changing this value will not change existing pitches.

RomanNumeral.impliedQuality
:   The quality of the chord implied by the figure:

    ```python
    >>> roman.RomanNumeral('V', 'C').impliedQuality
    'major'
    >>> roman.RomanNumeral('ii65', 'C').impliedQuality
    'minor'
    >>> roman.RomanNumeral('viio7', 'C').impliedQuality
    'diminished'
    ```

    The impliedQuality can differ from the actual quality
    if there are not enough notes to satisfy the implied quality,
    as in this half-diminished chord on vii which does not also
    have a seventh:

    ```python
    >>> incorrectSeventh = roman.RomanNumeral('vii/o', 'C')
    >>> incorrectSeventh.impliedQuality
    'half-diminished'
    >>> incorrectSeventh.quality
    'diminished'
    ```

    ```python
    >>> powerChordMinor = roman.RomanNumeral('v[no3]', 'C')
    >>> powerChordMinor.impliedQuality
    'minor'
    >>> powerChordMinor.quality
    'other'
    ```

    If case does not matter then an empty quality is implied:

    ```python
    >>> roman.RomanNumeral('II', 'C', caseMatters=False).impliedQuality
    ''
    ```

RomanNumeral.impliedScale
:   If no key or scale is passed in as the second object, then
    impliedScale will be set to C major:

    ```python
    >>> roman.RomanNumeral('V').impliedScale
    <music21.scale.MajorScale C major>
    ```

    Otherwise this will be empty:

    ```python
    >>> roman.RomanNumeral('V', key.Key('D')).impliedScale
    ```

RomanNumeral.omittedSteps
:   A list of integers showing chord factors that have been
    specifically omitted:

    ```python
    >>> emptyNinth = roman.RomanNumeral('V9[no7][no5]', 'C')
    >>> emptyNinth.omittedSteps
    [7, 5]
    >>> emptyNinth.pitches
    (<music21.pitch.Pitch G4>,
    <music21.pitch.Pitch B4>,
    <music21.pitch.Pitch A5>)
    ```

    Usually an empty list:

    ```python
    >>> roman.RomanNumeral('IV6').omittedSteps
    []
    ```

RomanNumeral.pivotChord
:   Defaults to None; if not None, stores another interpretation of the
    same RN in a different key; stores a RomanNumeral object.

    While not enforced, for consistency the pivotChord should be
    the new interpretation going forward (to the right on the staff)

    ```python
    >>> rn = roman.RomanNumeral('V7/IV', 'C')
    >>> rn.pivotChord is None
    True
    >>> rn.pivotChord = roman.RomanNumeral('V7', 'F')
    ```

RomanNumeral.primaryFigure
:   A string representing everything before the slash
    in a RomanNumeral with applied chords. In other roman numerals
    it is the same as figure:

    ```python
    >>> rn = roman.RomanNumeral('bII43/vi', 'C')
    >>> rn.primaryFigure
    'bII43'
    ```

    ```python
    >>> rnSimple = roman.RomanNumeral('V6', 'a')
    >>> rnSimple.primaryFigure
    'V6'
    ```

    Changing this value will not change existing pitches.

RomanNumeral.romanNumeralAlone
:   Returns a string of just the roman numeral part (I-VII or i-vii) of
    the figure:

    ```python
    >>> roman.RomanNumeral('V6').romanNumeralAlone
    'V'
    ```

    Chromatic alterations and secondary numerals are omitted:

    ```python
    >>> rn = roman.RomanNumeral('#II7/vi', 'C')
    >>> rn.romanNumeralAlone
    'II'
    ```

    Neapolitan chords are changed to ‘II’:

    ```python
    >>> roman.RomanNumeral('N6').romanNumeralAlone
    'II'
    ```

    Currently augmented-sixth chords return the “national” base. But this
    behavior may change in future versions:

    ```python
    >>> roman.RomanNumeral('It6').romanNumeralAlone
    'It'
    >>> roman.RomanNumeral('Ger65').romanNumeralAlone
    'Ger'
    ```

    This will be controversial in some circles, but it’s based on a root in
    isolation, and does not imply tonic quality:

    ```python
    >>> roman.RomanNumeral('Cad64').romanNumeralAlone
    'I'
    ```

RomanNumeral.scaleCardinality
:   Stores how many notes are in the scale; defaults to 7 for diatonic, obviously.

    ```python
    >>> roman.RomanNumeral('IV', 'a').scaleCardinality
    7
    ```

    Probably you should not need to change this. And most code is untested
    with other cardinalities. But it is (in theory) possible to create
    roman numerals on octatonic scales, etc.

    Changing this value will not change existing pitches.

RomanNumeral.scaleDegree
:   An int representing what degree of the scale the figure
    (or primary figure in the case of secondary/applied numerals)
    is on. Discounts any front alterations:

    ```python
    >>> roman.RomanNumeral('vi', 'E').scaleDegree
    6
    ```

    Note that this is 2, not 1.5 or 6 or 6.5 or something like that:

    ```python
    >>> roman.RomanNumeral('bII43/vi', 'C').scaleDegree
    2
    ```

    Empty RomanNumeral objects have the special scaleDegree of 0:

    ```python
    >>> roman.RomanNumeral().scaleDegree
    0
    ```

    Changing this value will not change existing pitches.

    * Changed in v6.5: empty RomanNumeral objects get scaleDegree 0, not None.

RomanNumeral.secondaryRomanNumeral
:   An optional roman.RomanNumeral object that represents the part
    after the slash in a secondary/applied RomanNumeral object. For instance,
    in the roman numeral, C: V7/vi, the secondaryRomanNumeral would be
    the roman numeral C: vi. The key of the secondaryRomanNumeral
    is the key of the original RomanNumeral. In cases such as
    V/V/V, the secondaryRomanNumeral can itself have a
    secondaryRomanNumeral.

    ```python
    >>> rn = roman.RomanNumeral('V7/vi', 'C')
    >>> rn.secondaryRomanNumeral
    <music21.roman.RomanNumeral vi in C major>
    ```

RomanNumeral.secondaryRomanNumeralKey
:   An optional key.Key object for secondary/applied RomanNumeral that
    represents the key that the part of the figure *before* the slash
    will be interpreted in. For instance in the roman numeral,
    C: V7/vi, the secondaryRomanNumeralKey would be a minor, since
    the vi (submediant) refers to an a-minor triad, and thus the V7
    part is to be read as the dominant seventh in a minor.

    ```python
    >>> rn = roman.RomanNumeral('V7/vi', 'C')
    >>> rn.secondaryRomanNumeralKey
    <music21.key.Key of a minor>
    ```

RomanNumeral.seventhMinor
:   How should vii, viio, and VII be parsed in minor?
    Defaults to Minor67Default.QUALITY.

    This value should be passed into the constructor initially.
    Changing it after construction will not change the pitches.

RomanNumeral.sixthMinor
:   How should vi, vio and VI be parsed in minor?
    Defaults to Minor67Default.QUALITY.

    This value should be passed into the constructor initially.
    Changing it after construction will not change the pitches.

RomanNumeral.useImpliedScale
:   A boolean indicating whether an implied scale is being used:

    ```python
    >>> roman.RomanNumeral('V').useImpliedScale
    True
    >>> roman.RomanNumeral('V', 'A').useImpliedScale
    False
    ```

Instance variables inherited from [`Chord`](moduleChord.html#music21.chord.Chord "music21.chord.Chord"):

|  |  |  |
| --- | --- | --- |
| * [`beams`](moduleChord.html#music21.chord.Chord.beams "music21.chord.Chord.beams") * [`isChord`](moduleChord.html#music21.chord.Chord.isChord "music21.chord.Chord.isChord") | * [`isNote`](moduleChord.html#music21.chord.Chord.isNote "music21.chord.Chord.isNote") | * [`isRest`](moduleChord.html#music21.chord.Chord.isRest "music21.chord.Chord.isRest") |

Instance variables inherited from [`ChordBase`](moduleChord.html#music21.chord.ChordBase "music21.chord.ChordBase"):

|  |  |  |
| --- | --- | --- |
| * [`beams`](moduleChord.html#music21.chord.ChordBase.beams "music21.chord.ChordBase.beams") | * [`isNote`](moduleChord.html#music21.chord.ChordBase.isNote "music21.chord.ChordBase.isNote") | * [`isRest`](moduleChord.html#music21.chord.ChordBase.isRest "music21.chord.ChordBase.isRest") |

Instance variables inherited from [`NotRest`](moduleNote.html#music21.note.NotRest "music21.note.NotRest"):

|  |  |  |
| --- | --- | --- |
| * [`beams`](moduleNote.html#music21.note.NotRest.beams "music21.note.NotRest.beams") |  |  |

Instance variables inherited from [`GeneralNote`](moduleNote.html#music21.note.GeneralNote "music21.note.GeneralNote"):

|  |  |  |
| --- | --- | --- |
| * [`articulations`](moduleNote.html#music21.note.GeneralNote.articulations "music21.note.GeneralNote.articulations") * [`expressions`](moduleNote.html#music21.note.GeneralNote.expressions "music21.note.GeneralNote.expressions") | * [`isChord`](moduleNote.html#music21.note.GeneralNote.isChord "music21.note.GeneralNote.isChord") | * [`lyrics`](moduleNote.html#music21.note.GeneralNote.lyrics "music21.note.GeneralNote.lyrics") |

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## ChordFigureTuple

class music21.roman.ChordFigureTuple(*aboveBass*, *alter*, *prefix*, *pitch*)

## FigureTuple

class music21.roman.FigureTuple(*aboveBass*, *alter*, *prefix*)

## Minor67Default

class music21.roman.Minor67Default(*\*values*)[[source]](../_modules/music21/roman.html#Minor67Default)
:   Enumeration that can be passed into [`RomanNumeral`](#music21.roman.RomanNumeral "music21.roman.RomanNumeral")’s
    keyword arguments sixthMinor and seventhMinor to define how Roman numerals
    on the sixth and seventh scale degrees are parsed in minor.

    Here is a little helper function that creates the chord in c-minor with the given
    sixthMinor interpretation in order to show how Minor67Default affects the
    interpretation of vi.

    ```python
    >>> vi = lambda sixChord, quality: ' '.join(p.name for p in roman.RomanNumeral(
    ...                                            sixChord,
    ...                                            'c',
    ...                                            sixthMinor=quality).pitches)
    ```

    The default for new chords is QUALITY, which means that the chord quality
    (major, minor, diminished) determines what note is the root, lowered ^6
    or raised ^6:

    ```python
    >>> vi('vi', roman.Minor67Default.QUALITY)
    'A C E'
    >>> vi('VI', roman.Minor67Default.QUALITY)
    'A- C E-'
    ```

    The enumeration FLAT means that lowered ^6 is used for the root no matter what.
    (Note that FLAT does not mean that the root will have a flat sign on it,
    for instance, in f-sharp minor, lowered ^6 is D natural. and in a-sharp minor,
    lowered ^6 is F#.)

    ```python
    >>> vi('vi', roman.Minor67Default.FLAT)
    'A- C- E-'
    >>> vi('VI', roman.Minor67Default.FLAT)
    'A- C E-'
    ```

    Conversely, SHARP implies that raised ^6 is used no matter what.

    ```python
    >>> vi('vi', roman.Minor67Default.SHARP)
    'A C E'
    >>> vi('VI', roman.Minor67Default.SHARP)
    'A C# E'
    ```

    Since FLAT assumes lowered ^6 whether the chord is major or minor (or anything else),
    to get a raised ^6 with the FLAT enumeration add a sharp before the name:

    ```python
    >>> vi('#vi', roman.Minor67Default.FLAT)
    'A C E'
    ```

    Likewise, with SHARP, a flat sign is needed to get lowered ^6:

    ```python
    >>> vi('bVI', roman.Minor67Default.SHARP)
    'A- C E-'
    ```

    The enumeration of CAUTIONARY is identical to QUALITY except that it
    ignores the # in #vi and the b in bVI, allowing users to write these
    chords in two different ways. CAUTIONARY is recommended in the case where
    users from different systems of training are working together, and no
    exotic chords (such as major triads on raised ^6) are used.

    ```python
    >>> vi('#vi', roman.Minor67Default.CAUTIONARY)
    'A C E'
    >>> vi('vi', roman.Minor67Default.CAUTIONARY)
    'A C E'
    >>> vi('bVI', roman.Minor67Default.CAUTIONARY)
    'A- C E-'
    >>> vi('VI', roman.Minor67Default.CAUTIONARY)
    'A- C E-'
    ```

    Whereas QUALITY follows a strict interpretation of what preceding sharp and flat
    signs mean. With QUALITY, since vi is already sharpened, #vi raises it even more.
    And since VI is already flattened, bVI lowers it even further:

    ```python
    >>> vi('vi', roman.Minor67Default.QUALITY)
    'A C E'
    >>> vi('#vi', roman.Minor67Default.QUALITY)
    'A# C# E#'
    >>> vi('VI', roman.Minor67Default.QUALITY)
    'A- C E-'
    >>> vi('bVI', roman.Minor67Default.QUALITY)
    'A-- C- E--'
    ```

    If you are using the CAUTIONARY enum, these odd chords can still be created, but
    an additional sharp or flat should be used.

    ```python
    >>> vi('##vi', roman.Minor67Default.CAUTIONARY)
    'A# C# E#'
    >>> vi('bbVI', roman.Minor67Default.CAUTIONARY)
    'A-- C- E--'
    ```

    For other odd chords that are contrary to the standard minor interpretation
    in the “wrong” direction, the interpretation is the same as QUALITY.

    For instance, here is a major triad on raised ^6 (what might be generally
    conceived of as V/ii), in the QUALITY and CAUTIONARY systems:

    ```python
    >>> vi('#VI', roman.Minor67Default.QUALITY)
    'A C# E'
    >>> vi('#VI', roman.Minor67Default.CAUTIONARY)
    'A C# E'
    ```

    And a minor triad on lowered ^6.

    ```python
    >>> vi('bvi', roman.Minor67Default.QUALITY)
    'A- C- E-'
    >>> vi('bvi', roman.Minor67Default.CAUTIONARY)
    'A- C- E-'
    ```

    All these examples use ^6, but the same concepts apply to ^7 using
    seventhMinor instead.

    This enumeration applies to secondary chords built on ^6 or ^7:

    ```python
    >>> vi('V/vi', roman.Minor67Default.QUALITY)
    'E G# B'
    >>> vi('V/VI', roman.Minor67Default.QUALITY)
    'E- G B-'
    ```

    ```python
    >>> vi('V/vi', roman.Minor67Default.FLAT)
    'E- G B-'
    >>> vi('V/VI', roman.Minor67Default.FLAT)
    'E- G B-'
    ```

    * Changed in v8: previously sixthMinor and seventhMinor did
      not carry over to secondary roman numerals.

## Functions

music21.roman.correctRNAlterationForMinor(*figureTuple: [FigureTuple](#music21.roman.FigureTuple "music21.roman.FigureTuple")*, *keyObj: [Key](moduleKey.html#music21.key.Key "music21.key.Key")*) → [FigureTuple](#music21.roman.FigureTuple "music21.roman.FigureTuple")[[source]](../_modules/music21/roman.html#correctRNAlterationForMinor)
:   (This will become a private function in version 10)

    Takes in a FigureTuple and a Key object and returns the same or a
    new FigureTuple correcting for the fact that, for instance, Ab in c minor
    is VI not vi. Works properly only if the note is the root of the chord.

    Used in RomanNumeralFromChord

    These return new FigureTuple objects

    ```python
    >>> ft5 = roman.FigureTuple(aboveBass=6, alter=-1, prefix='')
    >>> ft5a = roman.correctRNAlterationForMinor(ft5, key.Key('c'))
    >>> ft5a
    FigureTuple(aboveBass=6, alter=-1, prefix='b')
    >>> ft5a is ft5
    False
    ```

    ```python
    >>> ft6 = roman.FigureTuple(aboveBass=6, alter=0, prefix='')
    >>> roman.correctRNAlterationForMinor(ft6, key.Key('c'))
    FigureTuple(aboveBass=6, alter=0, prefix='b')
    ```

    ```python
    >>> ft7 = roman.FigureTuple(aboveBass=7, alter=1, prefix='#')
    >>> roman.correctRNAlterationForMinor(ft7, key.Key('c'))
    FigureTuple(aboveBass=7, alter=0, prefix='')
    ```

    Does nothing for major and passes in the original Figure Tuple unchanged:

    ```python
    >>> ft1 = roman.FigureTuple(aboveBass=6, alter=-1, prefix='b')
    >>> ft2 = roman.correctRNAlterationForMinor(ft1, key.Key('C'))
    >>> ft2
    FigureTuple(aboveBass=6, alter=-1, prefix='b')
    >>> ft1 is ft2
    True
    ```

    Does nothing for steps other than 6 or 7:

    ```python
    >>> ft3 = roman.FigureTuple(aboveBass=4, alter=-1, prefix='b')
    >>> ft4 = roman.correctRNAlterationForMinor(ft3, key.Key('c'))
    >>> ft4
    FigureTuple(aboveBass=4, alter=-1, prefix='b')
    >>> ft3 is ft4
    True
    ```

music21.roman.correctSuffixForChordQuality(*chordObj*, *inversionString*)[[source]](../_modules/music21/roman.html#correctSuffixForChordQuality)
:   Correct a given inversionString suffix given a chord of various qualities.

    ```python
    >>> c = chord.Chord('E3 C4 G4')
    >>> roman.correctSuffixForChordQuality(c, '6')
    '6'
    ```

    ```python
    >>> c = chord.Chord('E3 C4 G-4')
    >>> roman.correctSuffixForChordQuality(c, '6')
    'o6'
    ```

music21.roman.expandShortHand(*shorthand*)[[source]](../_modules/music21/roman.html#expandShortHand)
:   Expands shorthand notation into a list with all figures expanded:

    ```python
    >>> roman.expandShortHand('64')
    ['6', '4']
    >>> roman.expandShortHand('973')
    ['9', '7', '3']
    >>> roman.expandShortHand('11b3')
    ['11', 'b3']
    >>> roman.expandShortHand('b13#9-6')
    ['b13', '#9', '-6']
    >>> roman.expandShortHand('-')
    ['5', '-3']
    ```

    Slashes don’t matter:

    ```python
    >>> roman.expandShortHand('6/4')
    ['6', '4']
    ```

    Note that this is not where abbreviations get expanded:

    ```python
    >>> roman.expandShortHand('')
    []
    >>> roman.expandShortHand('7')  # not 7, 5, 3
    ['7']
    >>> roman.expandShortHand('4/3')  # not 6, 4, 3
    ['4', '3']
    ```

    Note that this is [‘6’] not [‘6’, ‘3’]:

    ```python
    >>> roman.expandShortHand('6')
    ['6']
    ```

    Returns a list of individual shorthands.

music21.roman.figureTupleSolo(*pitchObj: [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")*, *keyObj: [Key](moduleKey.html#music21.key.Key "music21.key.Key")*, *bass: [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")*) → [FigureTuple](#music21.roman.FigureTuple "music21.roman.FigureTuple")[[source]](../_modules/music21/roman.html#figureTupleSolo)
:   Return a single tuple for a pitch and key showing the interval above
    the bass, its alteration from a step in the given key, an alteration
    string, and the pitch object.

    For instance, in C major, an A-3 above an F# bass would be:

    ```python
    >>> roman.figureTupleSolo(
    ...     pitch.Pitch('A-3'),
    ...     key.Key('C'),
    ...     pitch.Pitch('F#2'),
    ...     )
    FigureTuple(aboveBass=3, alter=-1.0, prefix='b')
    ```

    These figures can be more complex in minor, so this is a good reference, showing
    that natural minor is always used.

    ```python
    >>> c = key.Key('c')
    >>> c_as_bass = pitch.Pitch('C3')
    >>> for name in ('E--', 'E-', 'E', 'E#', 'A--', 'A-', 'A', 'A#', 'B--', 'B-', 'B', 'B#'):
    ...     ft = roman.figureTupleSolo(pitch.Pitch(name + '4'), c, c_as_bass)
    ...     print(f'{name:4s} {ft}')
    E--  FigureTuple(aboveBass=3, alter=-1.0, prefix='b')
    E-   FigureTuple(aboveBass=3, alter=0.0, prefix='')
    E    FigureTuple(aboveBass=3, alter=1.0, prefix='#')
    E#   FigureTuple(aboveBass=3, alter=2.0, prefix='##')
    A--  FigureTuple(aboveBass=6, alter=-1.0, prefix='b')
    A-   FigureTuple(aboveBass=6, alter=0.0, prefix='')
    A    FigureTuple(aboveBass=6, alter=1.0, prefix='#')
    A#   FigureTuple(aboveBass=6, alter=2.0, prefix='##')
    B--  FigureTuple(aboveBass=7, alter=-1.0, prefix='b')
    B-   FigureTuple(aboveBass=7, alter=0.0, prefix='')
    B    FigureTuple(aboveBass=7, alter=1.0, prefix='#')
    B#   FigureTuple(aboveBass=7, alter=2.0, prefix='##')
    ```

    Returns a namedtuple called a FigureTuple.

music21.roman.figureTuples(*chordObject: [Chord](moduleChord.html#music21.chord.Chord "music21.chord.Chord")*, *keyObject: [Key](moduleKey.html#music21.key.Key "music21.key.Key")*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[ChordFigureTuple](#music21.roman.ChordFigureTuple "music21.roman.ChordFigureTuple")][[source]](../_modules/music21/roman.html#figureTuples)
:   Return a set of tuplets for each pitch showing the presence of a note, its
    interval above the bass its alteration (float) from a step in the given
    key, an alterationString, and the pitch object.

    Note though that for roman numerals, the applicable key is almost always
    the root.

    For instance, in C major, F# D A- C# would be:

    ```python
    >>> roman.figureTuples(
    ...     chord.Chord(['F#2', 'D3', 'A-3', 'C#4']),
    ...     key.Key('C'),
    ...     )
    [ChordFigureTuple(aboveBass=1, alter=1.0, prefix='#', pitch=<music21.pitch.Pitch F#2>),
     ChordFigureTuple(aboveBass=6, alter=0.0, prefix='', pitch=<music21.pitch.Pitch D3>),
     ChordFigureTuple(aboveBass=3, alter=-1.0, prefix='b', pitch=<music21.pitch.Pitch A-3>),
     ChordFigureTuple(aboveBass=5, alter=1.0, prefix='#', pitch=<music21.pitch.Pitch C#4>)]
    ```

    In c-minor, the A- is a normal note, so the prefix is ‘’ not ‘b’. The natural minor is used
    exclusively.

    ```python
    >>> roman.figureTuples(
    ...     chord.Chord(['F#2', 'D3', 'A-3', 'C#4']),
    ...     key.Key('c'),
    ...     )
    [ChordFigureTuple(aboveBass=1, alter=1.0, prefix='#', pitch=<music21.pitch.Pitch F#2>),
     ChordFigureTuple(aboveBass=6, alter=0.0, prefix='', pitch=<music21.pitch.Pitch D3>),
     ChordFigureTuple(aboveBass=3, alter=0.0, prefix='', pitch=<music21.pitch.Pitch A-3>),
     ChordFigureTuple(aboveBass=5, alter=1.0, prefix='#', pitch=<music21.pitch.Pitch C#4>)]
    ```

    A C dominant-seventh chord in c minor alters the bass but not the 7th degree

    ```python
    >>> roman.figureTuples(
    ...     chord.Chord(['E3', 'C4', 'G4', 'B-5']),
    ...     key.Key('c'),
    ...     )
    [ChordFigureTuple(aboveBass=1, alter=1.0, prefix='#', pitch=<music21.pitch.Pitch E3>),
     ChordFigureTuple(aboveBass=6, alter=0.0, prefix='', pitch=<music21.pitch.Pitch C4>),
     ChordFigureTuple(aboveBass=3, alter=0.0, prefix='', pitch=<music21.pitch.Pitch G4>),
     ChordFigureTuple(aboveBass=5, alter=0.0, prefix='', pitch=<music21.pitch.Pitch B-5>)]
    ```

    ```python
    >>> roman.figureTuples(
    ...     chord.Chord(['C4', 'E4', 'G4', 'C#4']),
    ...     key.Key('C'),
    ...     )
    [ChordFigureTuple(aboveBass=1, alter=0.0, prefix='', pitch=<music21.pitch.Pitch C4>),
     ChordFigureTuple(aboveBass=3, alter=0.0, prefix='', pitch=<music21.pitch.Pitch E4>),
     ChordFigureTuple(aboveBass=5, alter=0.0, prefix='', pitch=<music21.pitch.Pitch G4>),
     ChordFigureTuple(aboveBass=1, alter=1.0, prefix='#', pitch=<music21.pitch.Pitch C#4>)]
    ```

music21.roman.identifyAsTonicOrDominant(*inChord: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)") | [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)") | [Chord](moduleChord.html#music21.chord.Chord "music21.chord.Chord")*, *inKey: [Key](moduleKey.html#music21.key.Key "music21.key.Key")*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[False][[source]](../_modules/music21/roman.html#identifyAsTonicOrDominant)
:   Returns the roman numeral string expression (either tonic or dominant) that
    best matches the inChord. Useful when you know inChord is either tonic or
    dominant, but only two pitches are provided in the chord. If neither tonic
    nor dominant is possibly correct, False is returned

    ```python
    >>> roman.identifyAsTonicOrDominant(['B2', 'F5'], key.Key('C'))
    'V65'
    ```

    ```python
    >>> roman.identifyAsTonicOrDominant(['B3', 'G4'], key.Key('g'))
    'i6'
    ```

    ```python
    >>> roman.identifyAsTonicOrDominant(['C3', 'B-4'], key.Key('f'))
    'V7'
    ```

    Notice that this – with B-natural is also identified as V7 because
    it is returning the roman numeral root and the inversion name, not yet
    checking for correctness.

    ```python
    >>> roman.identifyAsTonicOrDominant(['C3', 'B4'], key.Key('f'))
    'V7'
    ```

    ```python
    >>> roman.identifyAsTonicOrDominant(['D3'], key.Key('f'))
    False
    ```

music21.roman.romanInversionName(*inChord: [Chord](moduleChord.html#music21.chord.Chord "music21.chord.Chord")*, *inv: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](../_modules/music21/roman.html#romanInversionName)
:   Extremely similar to Chord’s inversionName() method, but returns string
    values and allows incomplete triads.

    ```python
    >>> roman.romanInversionName(chord.Chord('E4 G4 C5'))
    '6'
    ```

    ```python
    >>> roman.romanInversionName(chord.Chord('G4 B4 C5 E5'))
    '43'
    ```

    Manually set the inversion to see what would happen.

    ```python
    >>> roman.romanInversionName(chord.Chord('C5 E5 G5'), inv=2)
    '64'
    ```

    ```python
    >>> roman.romanInversionName(chord.Chord('C5 E5 G5'), inv=0)
    ''
    ```

    Uncommon/unusual chords return an empty string

    ```python
    >>> roman.romanInversionName(chord.Chord('C5 C#4'))
    ''
    ```

    Does not return ninth or eleventh chord figures.

music21.roman.romanNumeralFromChord(*chordObj: [Chord](moduleChord.html#music21.chord.Chord "music21.chord.Chord")*, *keyObj: [Key](moduleKey.html#music21.key.Key "music21.key.Key") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *preferSecondaryDominants: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*) → [RomanNumeral](#music21.roman.RomanNumeral "music21.roman.RomanNumeral")[[source]](../_modules/music21/roman.html#romanNumeralFromChord)
:   Takes a chord object and returns an appropriate chord name. If keyObj is
    omitted, the root of the chord is considered the key (if the chord has a
    major third, it’s major; otherwise it’s minor).

    ```python
    >>> rn = roman.romanNumeralFromChord(
    ...     chord.Chord(['E-3', 'C4', 'G-6']),
    ...     key.Key('g#'),
    ...     )
    >>> rn
    <music21.roman.RomanNumeral bivo6 in g# minor>
    ```

    The pitches remain the same with the same octaves:

    ```python
    >>> for p in rn.pitches:
    ...     p
    <music21.pitch.Pitch E-3>
    <music21.pitch.Pitch C4>
    <music21.pitch.Pitch G-6>
    ```

    ```python
    >>> romanNumeral2 = roman.romanNumeralFromChord(
    ...     chord.Chord(['E3', 'C4', 'G4', 'B-4', 'E5', 'G5']),
    ...     key.Key('F'),
    ...     )
    >>> romanNumeral2
    <music21.roman.RomanNumeral V65 in F major>
    ```

    Note that vi and vii in minor, by default, signifies what you might think of
    alternatively as #vi and #vii:

    ```python
    >>> romanNumeral3 = roman.romanNumeralFromChord(
    ...     chord.Chord(['A4', 'C5', 'E-5']),
    ...     key.Key('c'),
    ...     )
    >>> romanNumeral3
    <music21.roman.RomanNumeral vio in c minor>
    ```

    ```python
    >>> romanNumeral4 = roman.romanNumeralFromChord(
    ...     chord.Chord(['A-4', 'C5', 'E-5']),
    ...     key.Key('c'),
    ...     )
    >>> romanNumeral4
    <music21.roman.RomanNumeral bVI in c minor>
    >>> romanNumeral4.sixthMinor
    <Minor67Default.CAUTIONARY: 2>
    ```

    ```python
    >>> romanNumeral5 = roman.romanNumeralFromChord(
    ...     chord.Chord(['B4', 'D5', 'F5']),
    ...     key.Key('c'),
    ...     )
    >>> romanNumeral5
    <music21.roman.RomanNumeral viio in c minor>
    ```

    ```python
    >>> romanNumeral6 = roman.romanNumeralFromChord(
    ...     chord.Chord(['B-4', 'D5', 'F5']),
    ...     key.Key('c'),
    ...     )
    >>> romanNumeral6
    <music21.roman.RomanNumeral bVII in c minor>
    ```

    Diminished and half-diminished seventh chords can omit the third and still
    be diminished: (n.b. we also demonstrate that chords can be created from a
    string):

    ```python
    >>> romanNumeralDim7 = roman.romanNumeralFromChord(
    ...     chord.Chord('A3 E-4 G-4'),
    ...     key.Key('b-'),
    ...     )
    >>> romanNumeralDim7
    <music21.roman.RomanNumeral viio7 in b- minor>
    ```

    For reference, odder notes:

    ```python
    >>> romanNumeral7 = roman.romanNumeralFromChord(
    ...     chord.Chord(['A--4', 'C-5', 'E--5']),
    ...     key.Key('c'),
    ...     )
    >>> romanNumeral7
    <music21.roman.RomanNumeral bbVI in c minor>
    ```

    ```python
    >>> romanNumeral8 = roman.romanNumeralFromChord(
    ...     chord.Chord(['A#4', 'C#5', 'E#5']),
    ...     key.Key('c'),
    ...     )
    >>> romanNumeral8
    <music21.roman.RomanNumeral #vi in c minor>
    ```

    ```python
    >>> romanNumeral10 = roman.romanNumeralFromChord(
    ...     chord.Chord(['F#3', 'A3', 'E4', 'C5']),
    ...     key.Key('d'),
    ...     )
    >>> romanNumeral10
    <music21.roman.RomanNumeral #iiiø7 in d minor>
    ```

    Augmented 6ths without key context

    ```python
    >>> roman.romanNumeralFromChord(
    ...     chord.Chord('E-4 G4 C#5'),
    ...     )
    <music21.roman.RomanNumeral It6 in g minor>
    ```

    ```python
    >>> roman.romanNumeralFromChord(
    ...     chord.Chord('E-4 G4 B-4 C#5'),
    ...     )
    <music21.roman.RomanNumeral Ger65 in g minor>
    ```

    ```python
    >>> roman.romanNumeralFromChord(
    ...     chord.Chord('E-4 G4 A4 C#5'),
    ...     )
    <music21.roman.RomanNumeral Fr43 in g minor>
    ```

    ```python
    >>> roman.romanNumeralFromChord(
    ...     chord.Chord('E-4 G4 A#4 C#5'),
    ...     )
    <music21.roman.RomanNumeral Sw43 in g minor>
    ```

    With correct key context:

    ```python
    >>> roman.romanNumeralFromChord(
    ...     chord.Chord('E-4 G4 C#5'),
    ...     key.Key('G')
    ...     )
    <music21.roman.RomanNumeral It6 in G major>
    ```

    With incorrect key context does not find an augmented 6th chord:

    ```python
    >>> roman.romanNumeralFromChord(
    ...     chord.Chord('E-4 G4 C#5'),
    ...     key.Key('C')
    ...     )
    <music21.roman.RomanNumeral #io6b3 in C major>
    ```

    Empty chords, including [`NoChord`](moduleHarmony.html#music21.harmony.NoChord "music21.harmony.NoChord") objects, give empty RomanNumerals:

    ```python
    >>> roman.romanNumeralFromChord(harmony.NoChord())
    <music21.roman.RomanNumeral>
    ```

    Augmented 6th chords in other inversions do not currently find correct roman numerals

    * Changed in v7: i7 is given for a tonic or subdominant minor-seventh chord in major:

    ```python
    >>> roman.romanNumeralFromChord(
    ...     chord.Chord('C4 E-4 G4 B-4'),
    ...     key.Key('C'))
    <music21.roman.RomanNumeral i7 in C major>
    ```

    ```python
    >>> roman.romanNumeralFromChord(
    ...     chord.Chord('E-4 G4 B-4 C5'),
    ...     key.Key('G'))
    <music21.roman.RomanNumeral iv65 in G major>
    ```

    minor-Major chords are written with a [#7] modifier afterwards:

    ```python
    >>> roman.romanNumeralFromChord(
    ...     chord.Chord('C4 E-4 G4 B4'),
    ...     key.Key('C'))
    <music21.roman.RomanNumeral i7[#7] in C major>
    >>> roman.romanNumeralFromChord(
    ...     chord.Chord('E-4 G4 B4 C5'),
    ...     key.Key('C'))
    <music21.roman.RomanNumeral i65[#7] in C major>
    ```

    Former bugs that are now fixed:

    ```python
    >>> romanNumeral11 = roman.romanNumeralFromChord(
    ...     chord.Chord(['E4', 'G4', 'B4', 'D5']),
    ...     key.Key('C'),
    ...     )
    >>> romanNumeral11
    <music21.roman.RomanNumeral iii7 in C major>
    ```

    ```python
    >>> roman.romanNumeralFromChord(chord.Chord('A3 C4 E-4 G4'), key.Key('c'))
    <music21.roman.RomanNumeral viø7 in c minor>
    ```

    ```python
    >>> roman.romanNumeralFromChord(chord.Chord('A3 C4 E-4 G4'), key.Key('B-'))
    <music21.roman.RomanNumeral viiø7 in B- major>
    ```

    ```python
    >>> romanNumeral9 = roman.romanNumeralFromChord(
    ...     chord.Chord(['C4', 'E5', 'G5', 'C#6']),
    ...     key.Key('C'),
    ...     )
    >>> romanNumeral9
    <music21.roman.RomanNumeral I#853 in C major>
    ```

    Not an augmented 6th:

    ```python
    >>> roman.romanNumeralFromChord(
    ...     chord.Chord('E4 G4 B-4 C#5')
    ...     )
    <music21.roman.RomanNumeral io6b5b3 in c# minor>
    ```

    The preferSecondaryDominants option defaults to False, but if set to True,
    then certain rare figures are swapped with their
    more common secondary dominant equivalent to produce
    Roman numerals like ‘V/V’ instead of ‘II’.

    This has no effect on most chords.
    A change is triggered if and only if:

    * the chord is a major triad or dominant seventh
    * the chord is not diatonic to the primary key (i.e., chromatically altered)
    * the root of secondary key is diatonic to the primary key.

    So first without setting preferSecondaryDominants:

    ```python
    >>> cd = chord.Chord('D F# A')
    >>> rn = roman.romanNumeralFromChord(cd, 'C')
    >>> rn.figure
    'II'
    ```

    And now with preferSecondaryDominants=True:

    ```python
    >>> rn = roman.romanNumeralFromChord(cd, 'C', preferSecondaryDominants=True)
    >>> rn.figure
    'V/V'
    ```

    Dominant sevenths must be spelt correctly
    (see conditions at [`isDominantSeventh()`](moduleChord.html#music21.chord.Chord.isDominantSeventh "music21.chord.Chord.isDominantSeventh")).

    So let’s try D dominant seventh in various contexts.

    ```python
    >>> cd = chord.Chord('F#4 A4 C5 D5')
    ```

    In G major this still comes out without recourse to a secondary,
    whether preferSecondaryDominants is True or False.

    ```python
    >>> rn = roman.romanNumeralFromChord(cd, 'G')
    >>> rn.figure
    'V65'
    ```

    ```python
    >>> rn = roman.romanNumeralFromChord(cd, 'G', preferSecondaryDominants=True)
    >>> rn.figure
    'V65'
    ```

    In C major it does come through as a secondary

    ```python
    >>> rn = roman.romanNumeralFromChord(cd, 'C', preferSecondaryDominants=True)
    >>> rn.figure
    'V65/V'
    ```

    “German Augmented sixth” chords are left intact, without change.
    This is thanks to the constraints on
    spelling and on the root of the secondary degree.

    ```python
    >>> cd = chord.Chord('Ab4 C5 Eb5 F#5')
    >>> rn = roman.romanNumeralFromChord(cd, 'C', preferSecondaryDominants=True)
    >>> rn.figure
    'Ger65'
    ```

    Let’s check that with a dominant seventh spelling and minor key context:

    ```python
    >>> cd = chord.Chord('Ab4 C5 Eb5 Gb5')
    >>> rn = roman.romanNumeralFromChord(cd, 'c', preferSecondaryDominants=True)
    >>> rn.figure
    'bVIb753'
    ```

    So that’s a context in which the root is diatonic,
    but the possible secondary root is not.
    Now let’s do the opposite case with a root that is not diatonic
    and a secondary that is.

    ```python
    >>> cd = chord.Chord('Ab4 C5 Eb5 Gb5')
    >>> rn = roman.romanNumeralFromChord(cd, 'c', preferSecondaryDominants=True)
    >>> rn.figure
    'bVIb753'
    ```

    Watch out, because there are still a lot of chords that
    preferSecondaryDominants will alter.
    This is deliberate: this option defaults to false
    so it does not run unless a user specifically initiates it
    and actively wants to make modifications.
    Power users could create more specific conditions in which to call it,
    e.g., before/after specific chords,
    and they can only do so if it errs on the side of more changes.

    For example, in minor, ‘I’ will be mapped to ‘V/iv’.

    ```python
    >>> cd = chord.Chord('F4 A4 C5')
    >>> rn = roman.romanNumeralFromChord(cd, 'f')
    >>> rn.figure
    'I'
    ```

    ```python
    >>> cd = chord.Chord('F4 A4 C5')
    >>> rn = roman.romanNumeralFromChord(cd, 'f', preferSecondaryDominants=True)
    >>> rn.figure
    'V/iv'
    ```

    This might be appropriate in the middle of a progression like
    i, V/iv, iv.
    By contrast, it’s probably not wanted for a tierce de picardie at the end
    iv6, V, I.
    This kind of context-sensitivity is not currently included.
