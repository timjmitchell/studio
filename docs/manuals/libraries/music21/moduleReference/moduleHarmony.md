Source: https://music21.org/music21docs/moduleReference/moduleHarmony.html

# music21.harmony

An object representation of harmony, a subclass of chord, as encountered as chord symbols or
roman numerals, or other chord representations with a defined root.

## Harmony

class music21.harmony.Harmony(*figure: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *root: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *bass: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *inversion: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *updatePitches: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *\*\*keywords*)[[source]](../_modules/music21/harmony.html#Harmony)
:   Harmony objects in music21 are a special type of chord - they retain all
    the same functionality as a chord (and inherit from chord directly),
    although they have special representations symbolically. They contain a
    figure representation, a shorthand, for the actual pitches they contain.
    This shorthand is commonly used on musical scores rather than writing out
    the chord pitches. Thus, each harmony object has an attribute,
    self.writeAsChord that dictates whether the object will be written to a
    score as a chord (with pitches realized) or with just the
    figure (as in Chord Symbols).

    Most users should start with the ChordSymbol class or the RomanNumeral
    class. The Harmony object is primarily a base object for defining other
    sorts of objects:

    ```python
    >>> c6 = harmony.ChordSymbol('C/E')
    >>> c6
    <music21.harmony.ChordSymbol C/E>
    ```

    By default, Harmony objects just float above the score and are a sort of
    analytical object. To make them also count as pitches in a score, use
    writeAsChord=True

    ```python
    >>> c6.writeAsChord = True
    >>> c6
    <music21.harmony.ChordSymbol C/E: E G C>
    ```

    Or individual components can be specified:

    ```python
    >>> c6_again = harmony.ChordSymbol(root='C', bass='E', kind='major')
    >>> c6_again
    <music21.harmony.ChordSymbol C/E>
    ```

    It is also possible to instantiate an empty Harmony object and
    then set components later, but this is an advanced and delicate operation:

    ```python
    >>> h = harmony.ChordSymbol()
    >>> h.root('B-3')
    >>> h.bass('D', allow_add=True)
    >>> h.inversion(1, transposeOnSet=False)
    >>> h.addChordStepModification(harmony.ChordStepModification('add', 4))
    >>> h
    <music21.harmony.ChordSymbol B-/D add 4>
    ```

    ```python
    >>> h = harmony.ChordSymbol('C7/E')
    >>> h.root()
    <music21.pitch.Pitch C4>
    ```

    ```python
    >>> h.bass()
    <music21.pitch.Pitch E3>
    ```

    ```python
    >>> h.inversion()
    1
    ```

    ```python
    >>> h.isSeventh()
    True
    ```

    ```python
    >>> [str(p) for p in h.pitches]
    ['E3', 'G3', 'B-3', 'C4']
    ```

    ```python
    >>> sus = harmony.ChordSymbol('Dsus4')
    >>> sus.root()
    <music21.pitch.Pitch D3>
    ```

    Accepts a keyword ‘updatePitches’. By default, it
    is True, but can be set to False to initialize faster if pitches are not needed.

    The placement attribute controls where the symbol appears relative to the staff,
    matching the MusicXML placement attribute on <harmony>. Valid values are
    `'above'`, `'below'`, or `None` (let the notation software decide):

    ```python
    >>> cs = harmony.ChordSymbol('G7')
    >>> cs.placement is None
    True
    >>> cs.placement = 'below'
    >>> cs.placement
    'below'
    ```

[`Harmony`](#music21.harmony.Harmony "music21.harmony.Harmony") bases

* [`Chord`](moduleChord.html#music21.chord.Chord "music21.chord.Chord")
* [`ChordBase`](moduleChord.html#music21.chord.ChordBase "music21.chord.ChordBase")
* [`NotRest`](moduleNote.html#music21.note.NotRest "music21.note.NotRest")
* [`GeneralNote`](moduleNote.html#music21.note.GeneralNote "music21.note.GeneralNote")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`Harmony`](#music21.harmony.Harmony "music21.harmony.Harmony") read-only properties

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

[`Harmony`](#music21.harmony.Harmony "music21.harmony.Harmony") read/write properties

Harmony.figure
:   Get or set the figure of the harmony object. The figure is the
    character (string) representation of the object. For example, ‘I’,
    ‘CM’, ‘3#’.

    When you instantiate a harmony object, if you pass in a figure it
    is stored internally and returned when you access the figure
    property. If you don’t instantiate the object with a figure, this
    property calls [`music21.harmony.Harmony.findFigure()`](#music21.harmony.Harmony.findFigure "music21.harmony.Harmony.findFigure") method which
    deduces the figure provided other information about the object,
    especially the chord.

    If the pitches of the harmony object have been modified after being
    instantiated, call [`music21.harmony.Harmony.findFigure()`](#music21.harmony.Harmony.findFigure "music21.harmony.Harmony.findFigure") to deduce the
    new figure.

    ```python
    >>> h = harmony.ChordSymbol('CM')
    >>> h.figure
    'CM'
    ```

    ```python
    >>> harmony.ChordSymbol(root='C', bass='A', kind='minor').figure
    'Cm/A'
    ```

    ```python
    >>> h.bass(note.Note('E'))
    >>> h.figure
    'CM'
    ```

Harmony.key
:   Gets or sets the current Key (or Scale object) associated with this
    Harmony object.

    For a given RomanNumeral object. Each sub-classed harmony object
    may treat this property differently, for example Roman Numeral
    objects update the pitches when the key is changed, but chord
    symbol objects do not and the key provides more information about
    the musical context from where the harmony object was extracted.

    ```python
    >>> r1 = roman.RomanNumeral('V')
    >>> r1.pitches
    (<music21.pitch.Pitch G4>, <music21.pitch.Pitch B4>, <music21.pitch.Pitch D5>)
    ```

    ```python
    >>> r1.key = key.Key('A')
    >>> r1.pitches
    (<music21.pitch.Pitch E5>, <music21.pitch.Pitch G#5>, <music21.pitch.Pitch B5>)
    ```

    Changing the key for a ChordSymbol object does nothing to its pitches, since it’s
    not dependent on key:

    ```python
    >>> h1 = harmony.ChordSymbol('D-m11')
    >>> [str(p) for p in h1.pitches]
    ['D-2', 'F-2', 'A-2', 'C-3', 'E-3', 'G-3']
    ```

    ```python
    >>> h1.key = 'CM'  # = C-Major
    >>> [str(p) for p in h1.pitches]
    ['D-2', 'F-2', 'A-2', 'C-3', 'E-3', 'G-3']
    ```

    But it should change the .romanNumeral object:

    ```python
    >>> y = harmony.ChordSymbol('F')
    >>> y.key is None
    True
    >>> y.romanNumeral
    <music21.roman.RomanNumeral I in F major>
    >>> y.key = key.Key('C')
    >>> y.romanNumeral
    <music21.roman.RomanNumeral IV in C major>
    ```

Harmony.romanNumeral
:   Get or set the romanNumeral numeral function of the Harmony as a
    `RomanNumeral` object. String
    representations accepted by RomanNumeral are also accepted.

    ```python
    >>> h = harmony.ChordSymbol('Dmaj7')
    >>> h.romanNumeral
    <music21.roman.RomanNumeral I7 in D major>
    ```

    ```python
    >>> h.romanNumeral = 'III7'
    >>> h.romanNumeral
    <music21.roman.RomanNumeral III7>
    ```

    ```python
    >>> h.romanNumeral.key = key.Key('B')
    >>> h.romanNumeral
    <music21.roman.RomanNumeral III7 in B major>
    ```

    ```python
    >>> h.romanNumeral = roman.RomanNumeral('IV7', 'A')
    >>> h.romanNumeral
    <music21.roman.RomanNumeral IV7 in A major>
    ```

    ```python
    >>> h = harmony.ChordSymbol('B-/D')
    >>> h.romanNumeral
    <music21.roman.RomanNumeral I6 in B- major>
    ```

Harmony.writeAsChord
:   Boolean attribute of all harmony objects that specifies how this
    object will be written to the rendered output (such as musicxml). If True
    (default for romanNumerals), the chord with pitches is written. If
    False (default for ChordSymbols) the harmony symbol is written.
    For NoChord objects, writeAsChord means to write as a rest.

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

[`Harmony`](#music21.harmony.Harmony "music21.harmony.Harmony") methods

Harmony.addChordStepModification(*degree*, *\**, *updatePitches=True*)[[source]](../_modules/music21/harmony.html#Harmony.addChordStepModification)
:   Add a harmony degree specification to this Harmony as a
    [`ChordStepModification`](#music21.harmony.ChordStepModification "music21.harmony.ChordStepModification") object.

    ```python
    >>> hd = harmony.ChordStepModification('add', 4)
    >>> h = harmony.ChordSymbol()
    >>> h.addChordStepModification(hd)
    >>> h.addChordStepModification('juicy')
    Traceback (most recent call last):
    music21.harmony.HarmonyException: cannot add this object as a degree: juicy
    ```

    Alteration will also impact the pitches,
    if the keyword argument updatePitches is given as True

    ```python
    >>> h = harmony.ChordSymbol('C')
    >>> mod = harmony.ChordStepModification('alter', 5, -1)
    >>> h.addChordStepModification(mod, updatePitches=True)
    >>> h.pitches
    (<music21.pitch.Pitch C3>, <music21.pitch.Pitch E3>, <music21.pitch.Pitch G-3>)
    ```

    * Changed in v7: updatePitches is True by default

Harmony.findFigure()[[source]](../_modules/music21/harmony.html#Harmony.findFigure)

Harmony.getChordStepModifications()[[source]](../_modules/music21/harmony.html#Harmony.getChordStepModifications)
:   Return all harmony degrees as a list.

Methods inherited from [`Chord`](moduleChord.html#music21.chord.Chord "music21.chord.Chord"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleChord.html#music21.chord.Chord.__eq__ "music21.chord.Chord.__eq__") * [`__getitem__()`](moduleChord.html#music21.chord.Chord.__getitem__ "music21.chord.Chord.__getitem__") * [`add()`](moduleChord.html#music21.chord.Chord.add "music21.chord.Chord.add") * [`annotateIntervals()`](moduleChord.html#music21.chord.Chord.annotateIntervals "music21.chord.Chord.annotateIntervals") * [`areZRelations()`](moduleChord.html#music21.chord.Chord.areZRelations "music21.chord.Chord.areZRelations") * [`bass()`](moduleChord.html#music21.chord.Chord.bass "music21.chord.Chord.bass") * [`canBeDominantV()`](moduleChord.html#music21.chord.Chord.canBeDominantV "music21.chord.Chord.canBeDominantV") * [`canBeTonic()`](moduleChord.html#music21.chord.Chord.canBeTonic "music21.chord.Chord.canBeTonic") * [`closedPosition()`](moduleChord.html#music21.chord.Chord.closedPosition "music21.chord.Chord.closedPosition") * [`containsSeventh()`](moduleChord.html#music21.chord.Chord.containsSeventh "music21.chord.Chord.containsSeventh") * [`containsTriad()`](moduleChord.html#music21.chord.Chord.containsTriad "music21.chord.Chord.containsTriad") * [`formatVectorString()`](moduleChord.html#music21.chord.Chord.formatVectorString "music21.chord.Chord.formatVectorString") * [`geometricNormalForm()`](moduleChord.html#music21.chord.Chord.geometricNormalForm "music21.chord.Chord.geometricNormalForm") * [`getChordStep()`](moduleChord.html#music21.chord.Chord.getChordStep "music21.chord.Chord.getChordStep") * [`getColor()`](moduleChord.html#music21.chord.Chord.getColor "music21.chord.Chord.getColor") * [`getNotehead()`](moduleChord.html#music21.chord.Chord.getNotehead "music21.chord.Chord.getNotehead") * [`getNoteheadFill()`](moduleChord.html#music21.chord.Chord.getNoteheadFill "music21.chord.Chord.getNoteheadFill") * [`getStemDirection()`](moduleChord.html#music21.chord.Chord.getStemDirection "music21.chord.Chord.getStemDirection") * [`getTie()`](moduleChord.html#music21.chord.Chord.getTie "music21.chord.Chord.getTie") * [`getVolume()`](moduleChord.html#music21.chord.Chord.getVolume "music21.chord.Chord.getVolume") * [`getZRelation()`](moduleChord.html#music21.chord.Chord.getZRelation "music21.chord.Chord.getZRelation") * [`hasAnyEnharmonicSpelledPitches()`](moduleChord.html#music21.chord.Chord.hasAnyEnharmonicSpelledPitches "music21.chord.Chord.hasAnyEnharmonicSpelledPitches") * [`hasAnyRepeatedDiatonicNote()`](moduleChord.html#music21.chord.Chord.hasAnyRepeatedDiatonicNote "music21.chord.Chord.hasAnyRepeatedDiatonicNote") | * [`hasRepeatedChordStep()`](moduleChord.html#music21.chord.Chord.hasRepeatedChordStep "music21.chord.Chord.hasRepeatedChordStep") * [`intervalFromChordStep()`](moduleChord.html#music21.chord.Chord.intervalFromChordStep "music21.chord.Chord.intervalFromChordStep") * [`inversion()`](moduleChord.html#music21.chord.Chord.inversion "music21.chord.Chord.inversion") * [`inversionName()`](moduleChord.html#music21.chord.Chord.inversionName "music21.chord.Chord.inversionName") * [`inversionText()`](moduleChord.html#music21.chord.Chord.inversionText "music21.chord.Chord.inversionText") * [`isAugmentedSixth()`](moduleChord.html#music21.chord.Chord.isAugmentedSixth "music21.chord.Chord.isAugmentedSixth") * [`isAugmentedTriad()`](moduleChord.html#music21.chord.Chord.isAugmentedTriad "music21.chord.Chord.isAugmentedTriad") * [`isConsonant()`](moduleChord.html#music21.chord.Chord.isConsonant "music21.chord.Chord.isConsonant") * [`isDiminishedSeventh()`](moduleChord.html#music21.chord.Chord.isDiminishedSeventh "music21.chord.Chord.isDiminishedSeventh") * [`isDiminishedTriad()`](moduleChord.html#music21.chord.Chord.isDiminishedTriad "music21.chord.Chord.isDiminishedTriad") * [`isDominantSeventh()`](moduleChord.html#music21.chord.Chord.isDominantSeventh "music21.chord.Chord.isDominantSeventh") * [`isFalseDiminishedSeventh()`](moduleChord.html#music21.chord.Chord.isFalseDiminishedSeventh "music21.chord.Chord.isFalseDiminishedSeventh") * [`isFrenchAugmentedSixth()`](moduleChord.html#music21.chord.Chord.isFrenchAugmentedSixth "music21.chord.Chord.isFrenchAugmentedSixth") * [`isGermanAugmentedSixth()`](moduleChord.html#music21.chord.Chord.isGermanAugmentedSixth "music21.chord.Chord.isGermanAugmentedSixth") * [`isHalfDiminishedSeventh()`](moduleChord.html#music21.chord.Chord.isHalfDiminishedSeventh "music21.chord.Chord.isHalfDiminishedSeventh") * [`isIncompleteMajorTriad()`](moduleChord.html#music21.chord.Chord.isIncompleteMajorTriad "music21.chord.Chord.isIncompleteMajorTriad") * [`isIncompleteMinorTriad()`](moduleChord.html#music21.chord.Chord.isIncompleteMinorTriad "music21.chord.Chord.isIncompleteMinorTriad") * [`isItalianAugmentedSixth()`](moduleChord.html#music21.chord.Chord.isItalianAugmentedSixth "music21.chord.Chord.isItalianAugmentedSixth") * [`isMajorTriad()`](moduleChord.html#music21.chord.Chord.isMajorTriad "music21.chord.Chord.isMajorTriad") * [`isMinorTriad()`](moduleChord.html#music21.chord.Chord.isMinorTriad "music21.chord.Chord.isMinorTriad") * [`isNinth()`](moduleChord.html#music21.chord.Chord.isNinth "music21.chord.Chord.isNinth") * [`isSeventh()`](moduleChord.html#music21.chord.Chord.isSeventh "music21.chord.Chord.isSeventh") | * [`isSeventhOfType()`](moduleChord.html#music21.chord.Chord.isSeventhOfType "music21.chord.Chord.isSeventhOfType") * [`isSwissAugmentedSixth()`](moduleChord.html#music21.chord.Chord.isSwissAugmentedSixth "music21.chord.Chord.isSwissAugmentedSixth") * [`isTranspositionallySymmetrical()`](moduleChord.html#music21.chord.Chord.isTranspositionallySymmetrical "music21.chord.Chord.isTranspositionallySymmetrical") * [`isTriad()`](moduleChord.html#music21.chord.Chord.isTriad "music21.chord.Chord.isTriad") * [`removeRedundantPitchClasses()`](moduleChord.html#music21.chord.Chord.removeRedundantPitchClasses "music21.chord.Chord.removeRedundantPitchClasses") * [`removeRedundantPitchNames()`](moduleChord.html#music21.chord.Chord.removeRedundantPitchNames "music21.chord.Chord.removeRedundantPitchNames") * [`removeRedundantPitches()`](moduleChord.html#music21.chord.Chord.removeRedundantPitches "music21.chord.Chord.removeRedundantPitches") * [`root()`](moduleChord.html#music21.chord.Chord.root "music21.chord.Chord.root") * [`semiClosedPosition()`](moduleChord.html#music21.chord.Chord.semiClosedPosition "music21.chord.Chord.semiClosedPosition") * [`semitonesFromChordStep()`](moduleChord.html#music21.chord.Chord.semitonesFromChordStep "music21.chord.Chord.semitonesFromChordStep") * [`setColor()`](moduleChord.html#music21.chord.Chord.setColor "music21.chord.Chord.setColor") * [`setNotehead()`](moduleChord.html#music21.chord.Chord.setNotehead "music21.chord.Chord.setNotehead") * [`setNoteheadFill()`](moduleChord.html#music21.chord.Chord.setNoteheadFill "music21.chord.Chord.setNoteheadFill") * [`setStemDirection()`](moduleChord.html#music21.chord.Chord.setStemDirection "music21.chord.Chord.setStemDirection") * [`setTie()`](moduleChord.html#music21.chord.Chord.setTie "music21.chord.Chord.setTie") * [`setVolume()`](moduleChord.html#music21.chord.Chord.setVolume "music21.chord.Chord.setVolume") * [`simplifyEnharmonics()`](moduleChord.html#music21.chord.Chord.simplifyEnharmonics "music21.chord.Chord.simplifyEnharmonics") * [`sortAscending()`](moduleChord.html#music21.chord.Chord.sortAscending "music21.chord.Chord.sortAscending") * [`sortChromaticAscending()`](moduleChord.html#music21.chord.Chord.sortChromaticAscending "music21.chord.Chord.sortChromaticAscending") * [`sortDiatonicAscending()`](moduleChord.html#music21.chord.Chord.sortDiatonicAscending "music21.chord.Chord.sortDiatonicAscending") * [`sortFrequencyAscending()`](moduleChord.html#music21.chord.Chord.sortFrequencyAscending "music21.chord.Chord.sortFrequencyAscending") * [`transpose()`](moduleChord.html#music21.chord.Chord.transpose "music21.chord.Chord.transpose") |

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

[`Harmony`](#music21.harmony.Harmony "music21.harmony.Harmony") instance variables

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

## ChordSymbol

class music21.harmony.ChordSymbol(*figure: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *root: [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *bass: [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *inversion: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *kind=''*, *kindStr=''*, *\*\*keywords*)[[source]](../_modules/music21/harmony.html#ChordSymbol)
:   Class representing the Chord Symbols commonly found on lead sheets.
    Chord Symbol objects can be instantiated one of two main ways:

    1. when music xml is parsed by the music21 converter, xml Chord Symbol tags
       are interpreted as Chord Symbol objects with a root and kind attribute.
       If bass is not specified, the bass is assumed to be the root
    2. by creating a chord symbol object with music21 by passing in the
       expression commonly found on leadsheets. Due to the relative diversity
       of lead sheet chord syntax, not all expressions are supported. Consult
       the examples for the supported syntax, or email us for help.

    All [`ChordSymbol`](#music21.harmony.ChordSymbol "music21.harmony.ChordSymbol") inherit from
    [`Chord`](moduleChord.html#music21.chord.Chord "music21.chord.Chord") so you can consider these objects as chords,
    although they have a unique representation in a score. ChordSymbols, unlike
    chords, by default appear as chord symbols in a score and have duration of
    0.

    To obtain the chord representation of the ChordSymbol in the score, change
    [`writeAsChord`](#music21.harmony.Harmony.writeAsChord "music21.harmony.Harmony.writeAsChord") to True. Unless otherwise
    specified, the duration of this chord object will become 1.0. If you have a
    leadsheet, run [`music21.harmony.realizeChordSymbolDurations()`](#music21.harmony.realizeChordSymbolDurations "music21.harmony.realizeChordSymbolDurations") on the
    stream to assign the correct (according to offsets) duration to each
    harmony object.)

    The music xml-based approach to instantiating Chord Symbol objects:

    ```python
    >>> cs = harmony.ChordSymbol(kind='minor', kindStr='m', root='C', bass='E-')
    >>> cs
    <music21.harmony.ChordSymbol Cm/E->
    ```

    ```python
    >>> cs.chordKind
    'minor'
    ```

    ```python
    >>> cs.root()
    <music21.pitch.Pitch C4>
    ```

    ```python
    >>> cs.bass()
    <music21.pitch.Pitch E-3>
    ```

    The second approach to creating a Chord Symbol object, by
    passing a regular expression (this list is not exhaustive):

    ```python
    >>> symbols = ['', 'm', '+', 'dim', '7',
    ...            'M7', 'm7', 'dim7', '7+', 'm7b5',  # half-diminished
    ...            'mM7', '6', 'm6', '9', 'Maj9', 'm9',
    ...            '11', 'Maj11', 'm11', '13',
    ...            'Maj13', 'm13', 'sus2', 'sus4',
    ...            'N6', 'It+6', 'Fr+6', 'Gr+6', 'pedal',
    ...            'power', 'tristan', '/E', 'm7/E-', 'add2',
    ...            '7omit3',]
    >>> for s in symbols:
    ...     chordSymbolName = 'C' + s
    ...     h = harmony.ChordSymbol(chordSymbolName)
    ...     pitchNames = [str(p) for p in h.pitches]
    ...     print(f'{chordSymbolName:<10}', end='[')
    ...     print(*pitchNames, sep=', ', end=']\n')
    C         [C3, E3, G3]
    Cm        [C3, E-3, G3]
    C+        [C3, E3, G#3]
    Cdim      [C3, E-3, G-3]
    C7        [C3, E3, G3, B-3]
    CM7       [C3, E3, G3, B3]
    Cm7       [C3, E-3, G3, B-3]
    Cdim7     [C3, E-3, G-3, B--3]
    C7+       [C3, E3, G#3, B-3]
    Cm7b5     [C3, E-3, G-3, B-3]
    CmM7      [C3, E-3, G3, B3]
    C6        [C3, E3, G3, A3]
    Cm6       [C3, E-3, G3, A3]
    C9        [C3, E3, G3, B-3, D4]
    CMaj9     [C3, E3, G3, B3, D4]
    Cm9       [C3, E-3, G3, B-3, D4]
    C11       [C2, E2, G2, B-2, D3, F3]
    CMaj11    [C2, E2, G2, B2, D3, F3]
    Cm11      [C2, E-2, G2, B-2, D3, F3]
    C13       [C2, E2, G2, B-2, D3, F3, A3]
    CMaj13    [C2, E2, G2, B2, D3, F3, A3]
    Cm13      [C2, E-2, G2, B-2, D3, F3, A3]
    Csus2     [C3, D3, G3]
    Csus4     [C3, F3, G3]
    CN6       [C3, D-3, E3, G-3]
    CIt+6     [C3, F#3, A-3]
    CFr+6     [C3, D3, F#3, A-3]
    CGr+6     [C3, E-3, F#3, A-3]
    Cpedal    [C3]
    Cpower    [C3, G3]
    Ctristan  [C3, D#3, F#3, A#3]
    C/E       [E3, G3, C4]
    Cm7/E-    [E-3, G3, B-3, C4]
    Cadd2     [C3, D3, E3, G3]
    C7omit3   [C3, G3, B-3]
    ```

    You can also create a Chord Symbol by writing out each degree,
    and any alterations to that degree:

    You must explicitly indicate EACH degree (a triad is NOT necessarily implied)

    ```python
    >>> [str(p) for p in harmony.ChordSymbol('C35b7b9#11b13').pitches]
    ['C2', 'E2', 'G2', 'D-3', 'F#3', 'A-3', 'B-3']
    ```

    ```python
    >>> [str(p) for p in harmony.ChordSymbol('C35911').pitches]
    ['C2', 'E2', 'G2', 'D3', 'F3']
    ```

    to prevent ambiguity in notation and in accordance with the rest of music21,
    if a root or bass is flat, the ‘-’ must be used, and NOT ‘b’. However, alterations and chord
    abbreviations are specified normally with the ‘b’ and ‘#’ signs.

    ```python
    >>> dFlat = harmony.ChordSymbol('D-35')
    >>> [str(p) for p in dFlat.pitches]
    ['D-3', 'F3', 'A-3']
    ```

    ```python
    >>> [str(p) for p in harmony.ChordSymbol('Db35').pitches]
    ['D3', 'F3', 'A3']
    ```

    (Note that this would be much better expressed just as ‘Dm’.)

    ```python
    >>> [str(p) for p in harmony.ChordSymbol('D,35b7b9#11b13').pitches]
    ['D2', 'F#2', 'A2', 'E-3', 'G#3', 'B-3', 'C4']
    ```

    ```python
    >>> harmony.ChordSymbol('Am').pitches
    (<music21.pitch.Pitch A2>, <music21.pitch.Pitch C3>, <music21.pitch.Pitch E3>)
    ```

    ```python
    >>> harmony.ChordSymbol('A-m').pitches
    (<music21.pitch.Pitch A-2>, <music21.pitch.Pitch C-3>, <music21.pitch.Pitch E-3>)
    ```

    ```python
    >>> harmony.ChordSymbol('A-m').pitches
    (<music21.pitch.Pitch A-2>, <music21.pitch.Pitch C-3>, <music21.pitch.Pitch E-3>)
    ```

    ```python
    >>> harmony.ChordSymbol('F-dim7').pitches
    (<music21.pitch.Pitch F-2>, <music21.pitch.Pitch A--2>,
     <music21.pitch.Pitch C--3>, <music21.pitch.Pitch E---3>)
    ```

    Thanks to David Bolton for catching the bugs tested below:

    ```python
    >>> [str(p) for p in harmony.ChordSymbol('C3579').pitches]
    ['C2', 'E2', 'G2', 'D3', 'B3']
    ```

    ```python
    >>> [str(p) for p in harmony.ChordSymbol('C35b79').pitches]
    ['C2', 'E2', 'G2', 'D3', 'B-3']
    ```

    ```python
    >>> [str(p) for p in harmony.ChordSymbol('C357b9').pitches]
    ['C2', 'E2', 'G2', 'D-3', 'B3']
    ```

    When bass is not in chord:

    ```python
    >>> cs = harmony.ChordSymbol(root='E', bass='C', kind='diminished-seventh')
    ```

    ```python
    >>> [str(p) for p in cs.pitches]
    ['C2', 'E3', 'G3', 'B-3', 'D-4']
    ```

    ```python
    >>> cs.figure
    'Eo7/C'
    ```

    And now, and example of parsing in the wild:

    ```python
    >>> s = corpus.parse('leadsheet/fosterBrownHair')
    >>> initialSymbols = s.flatten().getElementsByClass(harmony.ChordSymbol)[0:5]
    >>> [[str(c.name) for c in c.pitches] for c in initialSymbols]
    [['F', 'A', 'C'], ['B-', 'D', 'F'], ['F', 'A', 'C'], ['C', 'E', 'G'], ['F', 'A', 'C']]
    ```

    Test creating an empty chordSymbol:

    ```python
    >>> cs = harmony.ChordSymbol()
    >>> cs
    <music21.harmony.ChordSymbol>
    >>> cs.root('E-')
    >>> cs.bass('B-', allow_add=True)
    ```

    important: we are not asking for transposition, merely specifying the inversion that
    the chord should be read in (transposeOnSet = False)

    ```python
    >>> cs.inversion(2, transposeOnSet=False)
    ```

    ```python
    >>> cs.romanNumeral = 'I64'
    >>> cs.chordKind = 'major'
    >>> cs.chordKindStr = 'M'
    >>> cs
    <music21.harmony.ChordSymbol E-/B->
    ```

[`ChordSymbol`](#music21.harmony.ChordSymbol "music21.harmony.ChordSymbol") bases

* [`Harmony`](#music21.harmony.Harmony "music21.harmony.Harmony")
* [`Chord`](moduleChord.html#music21.chord.Chord "music21.chord.Chord")
* [`ChordBase`](moduleChord.html#music21.chord.ChordBase "music21.chord.ChordBase")
* [`NotRest`](moduleNote.html#music21.note.NotRest "music21.note.NotRest")
* [`GeneralNote`](moduleNote.html#music21.note.GeneralNote "music21.note.GeneralNote")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`ChordSymbol`](#music21.harmony.ChordSymbol "music21.harmony.ChordSymbol") read-only properties

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

[`ChordSymbol`](#music21.harmony.ChordSymbol "music21.harmony.ChordSymbol") read/write properties

Read/write properties inherited from [`Harmony`](#music21.harmony.Harmony "music21.harmony.Harmony"):

|  |  |  |
| --- | --- | --- |
| * [`figure`](#music21.harmony.Harmony.figure "music21.harmony.Harmony.figure") * [`key`](#music21.harmony.Harmony.key "music21.harmony.Harmony.key") | * [`romanNumeral`](#music21.harmony.Harmony.romanNumeral "music21.harmony.Harmony.romanNumeral") | * [`writeAsChord`](#music21.harmony.Harmony.writeAsChord "music21.harmony.Harmony.writeAsChord") |

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

[`ChordSymbol`](#music21.harmony.ChordSymbol "music21.harmony.ChordSymbol") methods

ChordSymbol.findFigure()[[source]](../_modules/music21/harmony.html#ChordSymbol.findFigure)
:   Return the chord symbol figure associated with this chord.

    This method tries to deduce what information it can from the provided
    pitches.

    ```python
    >>> h = harmony.ChordSymbol(root='F', bass='D-', kind='Neapolitan')
    >>> h.figure
    'FN6/D-'
    ```

    Thanks to Norman Schmidt for code sample and helping fix a bug

    ```python
    >>> foster = corpus.parse('leadsheet/fosterBrownHair.xml')
    >>> foster = foster.parts[0].getElementsByClass(stream.Measure)
    >>> for m in foster[12:17]:
    ...   c = m.getElementsByClass(harmony.ChordSymbol)
    ...   if c:
    ...     ch = c[0].figure
    ...     print(ch.replace('-', 'b'))
    ...   else:
    ...     print('n.c.')
    F
    G7
    C
    C
    C
    ```

    Thanks to David Bolton for catching the bugs tested below:

    ```python
    >>> h1 = harmony.ChordSymbol('C7 b9')
    >>> for x in h1.pitches:
    ...     x
    ...
    <music21.pitch.Pitch C3>
    <music21.pitch.Pitch E3>
    <music21.pitch.Pitch G3>
    <music21.pitch.Pitch B-3>
    <music21.pitch.Pitch D-4>
    ```

    ```python
    >>> h2 = harmony.ChordSymbol('C/B- add 2')
    >>> for x in h2.pitches:
    ...     x
    ...
    <music21.pitch.Pitch B-2>
    <music21.pitch.Pitch C3>
    <music21.pitch.Pitch D3>
    <music21.pitch.Pitch E3>
    <music21.pitch.Pitch G3>
    ```

ChordSymbol.inversionIsValid(*inversion*)[[source]](../_modules/music21/harmony.html#ChordSymbol.inversionIsValid)
:   Returns true if the provided inversion exists for the given pitches of
    the chord. If not, it returns false and the getPitches method then
    appends the bass pitch to the chord.

ChordSymbol.transpose(*value*, *\**, *inPlace=False*) → [Self](https://docs.python.org/3/library/typing.html#typing.Self "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/harmony.html#ChordSymbol.transpose)
:   Overrides [`transpose()`](moduleChord.html#music21.chord.Chord.transpose "music21.chord.Chord.transpose") so that this ChordSymbol’s
    figure is appropriately cleared afterward.

    ```python
    >>> cs = harmony.ChordSymbol('Am')
    >>> cs.figure
    'Am'
    >>> cs.transpose(1)
    <music21.harmony.ChordSymbol B-m>
    >>> cs.transpose(5, inPlace=True)
    >>> cs
    <music21.harmony.ChordSymbol Dm>
    >>> cs.figure
    'Dm'
    ```

Methods inherited from [`Harmony`](#music21.harmony.Harmony "music21.harmony.Harmony"):

|  |  |  |
| --- | --- | --- |
| * [`addChordStepModification()`](#music21.harmony.Harmony.addChordStepModification "music21.harmony.Harmony.addChordStepModification") | * [`getChordStepModifications()`](#music21.harmony.Harmony.getChordStepModifications "music21.harmony.Harmony.getChordStepModifications") |  |

Methods inherited from [`Chord`](moduleChord.html#music21.chord.Chord "music21.chord.Chord"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleChord.html#music21.chord.Chord.__eq__ "music21.chord.Chord.__eq__") * [`__getitem__()`](moduleChord.html#music21.chord.Chord.__getitem__ "music21.chord.Chord.__getitem__") * [`add()`](moduleChord.html#music21.chord.Chord.add "music21.chord.Chord.add") * [`annotateIntervals()`](moduleChord.html#music21.chord.Chord.annotateIntervals "music21.chord.Chord.annotateIntervals") * [`areZRelations()`](moduleChord.html#music21.chord.Chord.areZRelations "music21.chord.Chord.areZRelations") * [`bass()`](moduleChord.html#music21.chord.Chord.bass "music21.chord.Chord.bass") * [`canBeDominantV()`](moduleChord.html#music21.chord.Chord.canBeDominantV "music21.chord.Chord.canBeDominantV") * [`canBeTonic()`](moduleChord.html#music21.chord.Chord.canBeTonic "music21.chord.Chord.canBeTonic") * [`closedPosition()`](moduleChord.html#music21.chord.Chord.closedPosition "music21.chord.Chord.closedPosition") * [`containsSeventh()`](moduleChord.html#music21.chord.Chord.containsSeventh "music21.chord.Chord.containsSeventh") * [`containsTriad()`](moduleChord.html#music21.chord.Chord.containsTriad "music21.chord.Chord.containsTriad") * [`formatVectorString()`](moduleChord.html#music21.chord.Chord.formatVectorString "music21.chord.Chord.formatVectorString") * [`geometricNormalForm()`](moduleChord.html#music21.chord.Chord.geometricNormalForm "music21.chord.Chord.geometricNormalForm") * [`getChordStep()`](moduleChord.html#music21.chord.Chord.getChordStep "music21.chord.Chord.getChordStep") * [`getColor()`](moduleChord.html#music21.chord.Chord.getColor "music21.chord.Chord.getColor") * [`getNotehead()`](moduleChord.html#music21.chord.Chord.getNotehead "music21.chord.Chord.getNotehead") * [`getNoteheadFill()`](moduleChord.html#music21.chord.Chord.getNoteheadFill "music21.chord.Chord.getNoteheadFill") * [`getStemDirection()`](moduleChord.html#music21.chord.Chord.getStemDirection "music21.chord.Chord.getStemDirection") * [`getTie()`](moduleChord.html#music21.chord.Chord.getTie "music21.chord.Chord.getTie") * [`getVolume()`](moduleChord.html#music21.chord.Chord.getVolume "music21.chord.Chord.getVolume") * [`getZRelation()`](moduleChord.html#music21.chord.Chord.getZRelation "music21.chord.Chord.getZRelation") * [`hasAnyEnharmonicSpelledPitches()`](moduleChord.html#music21.chord.Chord.hasAnyEnharmonicSpelledPitches "music21.chord.Chord.hasAnyEnharmonicSpelledPitches") | * [`hasAnyRepeatedDiatonicNote()`](moduleChord.html#music21.chord.Chord.hasAnyRepeatedDiatonicNote "music21.chord.Chord.hasAnyRepeatedDiatonicNote") * [`hasRepeatedChordStep()`](moduleChord.html#music21.chord.Chord.hasRepeatedChordStep "music21.chord.Chord.hasRepeatedChordStep") * [`intervalFromChordStep()`](moduleChord.html#music21.chord.Chord.intervalFromChordStep "music21.chord.Chord.intervalFromChordStep") * [`inversion()`](moduleChord.html#music21.chord.Chord.inversion "music21.chord.Chord.inversion") * [`inversionName()`](moduleChord.html#music21.chord.Chord.inversionName "music21.chord.Chord.inversionName") * [`inversionText()`](moduleChord.html#music21.chord.Chord.inversionText "music21.chord.Chord.inversionText") * [`isAugmentedSixth()`](moduleChord.html#music21.chord.Chord.isAugmentedSixth "music21.chord.Chord.isAugmentedSixth") * [`isAugmentedTriad()`](moduleChord.html#music21.chord.Chord.isAugmentedTriad "music21.chord.Chord.isAugmentedTriad") * [`isConsonant()`](moduleChord.html#music21.chord.Chord.isConsonant "music21.chord.Chord.isConsonant") * [`isDiminishedSeventh()`](moduleChord.html#music21.chord.Chord.isDiminishedSeventh "music21.chord.Chord.isDiminishedSeventh") * [`isDiminishedTriad()`](moduleChord.html#music21.chord.Chord.isDiminishedTriad "music21.chord.Chord.isDiminishedTriad") * [`isDominantSeventh()`](moduleChord.html#music21.chord.Chord.isDominantSeventh "music21.chord.Chord.isDominantSeventh") * [`isFalseDiminishedSeventh()`](moduleChord.html#music21.chord.Chord.isFalseDiminishedSeventh "music21.chord.Chord.isFalseDiminishedSeventh") * [`isFrenchAugmentedSixth()`](moduleChord.html#music21.chord.Chord.isFrenchAugmentedSixth "music21.chord.Chord.isFrenchAugmentedSixth") * [`isGermanAugmentedSixth()`](moduleChord.html#music21.chord.Chord.isGermanAugmentedSixth "music21.chord.Chord.isGermanAugmentedSixth") * [`isHalfDiminishedSeventh()`](moduleChord.html#music21.chord.Chord.isHalfDiminishedSeventh "music21.chord.Chord.isHalfDiminishedSeventh") * [`isIncompleteMajorTriad()`](moduleChord.html#music21.chord.Chord.isIncompleteMajorTriad "music21.chord.Chord.isIncompleteMajorTriad") * [`isIncompleteMinorTriad()`](moduleChord.html#music21.chord.Chord.isIncompleteMinorTriad "music21.chord.Chord.isIncompleteMinorTriad") * [`isItalianAugmentedSixth()`](moduleChord.html#music21.chord.Chord.isItalianAugmentedSixth "music21.chord.Chord.isItalianAugmentedSixth") * [`isMajorTriad()`](moduleChord.html#music21.chord.Chord.isMajorTriad "music21.chord.Chord.isMajorTriad") * [`isMinorTriad()`](moduleChord.html#music21.chord.Chord.isMinorTriad "music21.chord.Chord.isMinorTriad") * [`isNinth()`](moduleChord.html#music21.chord.Chord.isNinth "music21.chord.Chord.isNinth") | * [`isSeventh()`](moduleChord.html#music21.chord.Chord.isSeventh "music21.chord.Chord.isSeventh") * [`isSeventhOfType()`](moduleChord.html#music21.chord.Chord.isSeventhOfType "music21.chord.Chord.isSeventhOfType") * [`isSwissAugmentedSixth()`](moduleChord.html#music21.chord.Chord.isSwissAugmentedSixth "music21.chord.Chord.isSwissAugmentedSixth") * [`isTranspositionallySymmetrical()`](moduleChord.html#music21.chord.Chord.isTranspositionallySymmetrical "music21.chord.Chord.isTranspositionallySymmetrical") * [`isTriad()`](moduleChord.html#music21.chord.Chord.isTriad "music21.chord.Chord.isTriad") * [`removeRedundantPitchClasses()`](moduleChord.html#music21.chord.Chord.removeRedundantPitchClasses "music21.chord.Chord.removeRedundantPitchClasses") * [`removeRedundantPitchNames()`](moduleChord.html#music21.chord.Chord.removeRedundantPitchNames "music21.chord.Chord.removeRedundantPitchNames") * [`removeRedundantPitches()`](moduleChord.html#music21.chord.Chord.removeRedundantPitches "music21.chord.Chord.removeRedundantPitches") * [`root()`](moduleChord.html#music21.chord.Chord.root "music21.chord.Chord.root") * [`semiClosedPosition()`](moduleChord.html#music21.chord.Chord.semiClosedPosition "music21.chord.Chord.semiClosedPosition") * [`semitonesFromChordStep()`](moduleChord.html#music21.chord.Chord.semitonesFromChordStep "music21.chord.Chord.semitonesFromChordStep") * [`setColor()`](moduleChord.html#music21.chord.Chord.setColor "music21.chord.Chord.setColor") * [`setNotehead()`](moduleChord.html#music21.chord.Chord.setNotehead "music21.chord.Chord.setNotehead") * [`setNoteheadFill()`](moduleChord.html#music21.chord.Chord.setNoteheadFill "music21.chord.Chord.setNoteheadFill") * [`setStemDirection()`](moduleChord.html#music21.chord.Chord.setStemDirection "music21.chord.Chord.setStemDirection") * [`setTie()`](moduleChord.html#music21.chord.Chord.setTie "music21.chord.Chord.setTie") * [`setVolume()`](moduleChord.html#music21.chord.Chord.setVolume "music21.chord.Chord.setVolume") * [`simplifyEnharmonics()`](moduleChord.html#music21.chord.Chord.simplifyEnharmonics "music21.chord.Chord.simplifyEnharmonics") * [`sortAscending()`](moduleChord.html#music21.chord.Chord.sortAscending "music21.chord.Chord.sortAscending") * [`sortChromaticAscending()`](moduleChord.html#music21.chord.Chord.sortChromaticAscending "music21.chord.Chord.sortChromaticAscending") * [`sortDiatonicAscending()`](moduleChord.html#music21.chord.Chord.sortDiatonicAscending "music21.chord.Chord.sortDiatonicAscending") * [`sortFrequencyAscending()`](moduleChord.html#music21.chord.Chord.sortFrequencyAscending "music21.chord.Chord.sortFrequencyAscending") |

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

[`ChordSymbol`](#music21.harmony.ChordSymbol "music21.harmony.ChordSymbol") instance variables

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

## ChordStepModification

class music21.harmony.ChordStepModification(*modType=None*, *degree=None*, *intervalObj=None*)[[source]](../_modules/music21/harmony.html#ChordStepModification)
:   ChordStepModification objects define the specification of harmony degree
    alterations, subtractions, or additions, used in
    [`Harmony`](#music21.harmony.Harmony "music21.harmony.Harmony") objects, which includes
    harmony.ChordSymbol objects (and will include harmony.RomanNumeral
    objects).

    * degree-value element: indicates degree in chord, positive integers only
    * degree-alter: indicates semitone alteration of degree, positive and
      negative integers only
    * degree-type: add, alter, or subtract
      :   + if add: degree-alter is relative to a dominant chord (major and
            perfect intervals except for a minor seventh)
          + if alter or subtract: degree-alter is relative to degree already in
            the chord based on its kind element

    ```python
    >>> hd = harmony.ChordStepModification('add', 4)
    >>> hd
    <music21.harmony.ChordStepModification modType=add
        degree=4 interval=<music21.interval.Interval P1>>
    ```

    ```python
    >>> hd = harmony.ChordStepModification('alter', 3, 1)
    >>> hd
    <music21.harmony.ChordStepModification modType=alter
        degree=3 interval=<music21.interval.Interval A1>>
    ```

[`ChordStepModification`](#music21.harmony.ChordStepModification "music21.harmony.ChordStepModification") bases

* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`ChordStepModification`](#music21.harmony.ChordStepModification "music21.harmony.ChordStepModification") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`ChordStepModification`](#music21.harmony.ChordStepModification "music21.harmony.ChordStepModification") read/write properties

ChordStepModification.degree
:   Returns or sets an integer specifying the scale degree
    that this ChordStepModification alters.

    ```python
    >>> hd = harmony.ChordStepModification()
    >>> hd.degree = 3
    >>> hd.degree
    3
    ```

    ```python
    >>> hd.degree = 'juicy'
    Traceback (most recent call last):
    music21.harmony.ChordStepModificationException: not a valid degree: juicy
    ```

ChordStepModification.interval
:   Get or set the alteration of this degree as a
    [`Interval`](moduleInterval.html#music21.interval.Interval "music21.interval.Interval") object, generally
    as a type of ascending or descending augmented unison.

    ```python
    >>> hd = harmony.ChordStepModification()
    >>> hd.interval = 1
    >>> hd.interval
    <music21.interval.Interval A1>
    ```

    ```python
    >>> hd.interval = -2
    >>> hd.interval
    <music21.interval.Interval AA-1>
    ```

    ```python
    >>> hd.interval = 0
    >>> hd.interval
    <music21.interval.Interval P1>
    ```

    ```python
    >>> hd.interval = interval.Interval('m3')
    >>> hd.interval
    <music21.interval.Interval m3>
    ```

    More than 3 half step alteration gets
    an interval that isn’t a prime.

    ```python
    >>> hd.interval = -4
    >>> hd.interval
    <music21.interval.Interval M-3>
    ```

ChordStepModification.modType
:   Get or set the ChordStepModification modification type, where
    permitted types are the strings add, subtract, or alter.

    ```python
    >>> hd = harmony.ChordStepModification()
    >>> hd.modType = 'add'
    >>> hd.modType
    'add'
    ```

    ```python
    >>> hd.modType = 'juicy'
    Traceback (most recent call last):
    music21.harmony.ChordStepModificationException: not a valid degree modification type: juicy
    ```

[`ChordStepModification`](#music21.harmony.ChordStepModification "music21.harmony.ChordStepModification") methods

ChordStepModification.\_\_eq\_\_(*other*)[[source]](../_modules/music21/harmony.html#ChordStepModification.__eq__)
:   Return self==value.

## NoChord

class music21.harmony.NoChord(*figure: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *kind: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = 'none'*, *kindStr: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\*\*keywords*)[[source]](../_modules/music21/harmony.html#NoChord)
:   Class representing a special ‘no chord’ ChordSymbol used to explicitly
    encode absence of chords. This is especially useful to stop a chord
    without playing another.

    ```python
    >>> from music21.harmony import ChordSymbol, NoChord
    >>> s = stream.Score()
    >>> s.repeatAppend(note.Note('C'), 4)
    >>> s.append(ChordSymbol('C'))
    >>> s.repeatAppend(note.Note('C'), 4)
    >>> s.append(NoChord())
    >>> s.repeatAppend(note.Note('C'), 4)
    >>> s = s.makeMeasures()
    ```

    See how the chordSymbol of C stops at offset 8 rather
    than continuing, thanks to the NoChord object.

    ```python
    >>> s = harmony.realizeChordSymbolDurations(s)
    >>> s.show('text', addEndTimes=True)
    {0.0 - 0.0} <music21.clef.BassClef>
    {0.0 - 0.0} <music21.meter.TimeSignature 4/4>
    {0.0 - 1.0} <music21.note.Note C>
    {1.0 - 2.0} <music21.note.Note C>
    {2.0 - 3.0} <music21.note.Note C>
    {3.0 - 4.0} <music21.note.Note C>
    {4.0 - 8.0} <music21.harmony.ChordSymbol C>
    {4.0 - 5.0} <music21.note.Note C>
    {5.0 - 6.0} <music21.note.Note C>
    {6.0 - 7.0} <music21.note.Note C>
    {7.0 - 8.0} <music21.note.Note C>
    {8.0 - 12.0} <music21.harmony.NoChord N.C.>
    {8.0 - 9.0} <music21.note.Note C>
    {9.0 - 10.0} <music21.note.Note C>
    {10.0 - 11.0} <music21.note.Note C>
    {11.0 - 12.0} <music21.note.Note C>
    {12.0 - 12.0} <music21.bar.Barline type=final>
    ```

    ```python
    >>> c_major = s.getElementsByClass(ChordSymbol).first()
    >>> c_major.duration
    <music21.duration.Duration 4.0>
    >>> c_major.offset
    4.0
    ```

    Other text than the default of ‘N.C.’ can be given:

    ```python
    >>> nc2 = NoChord('NC')
    >>> nc2
    <music21.harmony.NoChord NC>
    >>> nc2.pitches
    ()
    ```

    Note that even if the text is a valid chord abbreviation, no
    pitches are generated. This feature may be useful for adding
    the appearance of ChordSymbols in a piece without having them
    be realized.

    ```python
    >>> nc2 = NoChord('C7')
    >>> nc2
    <music21.harmony.NoChord C7>
    >>> nc2.pitches
    ()
    ```

[`NoChord`](#music21.harmony.NoChord "music21.harmony.NoChord") bases

* [`ChordSymbol`](#music21.harmony.ChordSymbol "music21.harmony.ChordSymbol")
* [`Harmony`](#music21.harmony.Harmony "music21.harmony.Harmony")
* [`Chord`](moduleChord.html#music21.chord.Chord "music21.chord.Chord")
* [`ChordBase`](moduleChord.html#music21.chord.ChordBase "music21.chord.ChordBase")
* [`NotRest`](moduleNote.html#music21.note.NotRest "music21.note.NotRest")
* [`GeneralNote`](moduleNote.html#music21.note.GeneralNote "music21.note.GeneralNote")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`NoChord`](#music21.harmony.NoChord "music21.harmony.NoChord") read-only properties

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

[`NoChord`](#music21.harmony.NoChord "music21.harmony.NoChord") read/write properties

Read/write properties inherited from [`Harmony`](#music21.harmony.Harmony "music21.harmony.Harmony"):

|  |  |  |
| --- | --- | --- |
| * [`figure`](#music21.harmony.Harmony.figure "music21.harmony.Harmony.figure") * [`key`](#music21.harmony.Harmony.key "music21.harmony.Harmony.key") | * [`romanNumeral`](#music21.harmony.Harmony.romanNumeral "music21.harmony.Harmony.romanNumeral") | * [`writeAsChord`](#music21.harmony.Harmony.writeAsChord "music21.harmony.Harmony.writeAsChord") |

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

[`NoChord`](#music21.harmony.NoChord "music21.harmony.NoChord") methods

NoChord.bass(*newbass=None*, *\**, *find=None*, *allow\_add=False*)[[source]](../_modules/music21/harmony.html#NoChord.bass)
:   Generally used to find and return the bass Pitch:

    ```python
    >>> cmaj1stInv = chord.Chord(['C4', 'E3', 'G5'])
    >>> cmaj1stInv.bass()
    <music21.pitch.Pitch E3>
    ```

    Subclasses of Chord often have basses that are harder to determine.

    ```python
    >>> cmaj = harmony.ChordSymbol('CM')
    >>> cmaj.bass()
    <music21.pitch.Pitch C3>
    ```

    ```python
    >>> cmin_inv = harmony.ChordSymbol('Cm/E-')
    >>> cmin_inv.bass()
    <music21.pitch.Pitch E-3>
    ```

    Can also be used in rare occasions to set the bass note to a new Pitch,
    so long as that note is found in the chord:

    ```python
    >>> strange_chord = chord.Chord('E##4 F-4 C5')
    >>> strange_chord.bass()
    <music21.pitch.Pitch E##4>
    >>> strange_chord.bass('F-4')
    >>> strange_chord.bass()
    <music21.pitch.Pitch F-4>
    ```

    If the note assigned to the bass is not found, it will default to raising a
    ChordException:

    ```python
    >>> strange_chord.bass('G--4')
    Traceback (most recent call last):
    music21.chord.ChordException: Pitch G--4 not found in chord
    ```

    For the purposes of initializing from a ChordSymbol and in other cases,
    a new bass can be added to the chord by setting allow\_add = True:

    ```python
    >>> strange_chord.bass('G--4', allow_add=True)
    >>> strange_chord.bass()
    <music21.pitch.Pitch G--4>
    ```

    By default, if nothing has been overridden, this method uses a
    quick algorithm to find the bass among the
    chord’s pitches, if no bass has been previously specified. If this is
    not intended, set find to False when calling this method, and ‘None’
    will be returned if no bass is specified

    ```python
    >>> em = chord.Chord(['E3', 'G3', 'B4'])
    >>> print(em.bass(find=False))
    None
    ```

    * Changed in v8: raise an exception if setting a new bass
      to a pitch not in the chord, unless new keyword allow\_add is True.

NoChord.root(*newroot=None*, *\**, *find=None*)[[source]](../_modules/music21/harmony.html#NoChord.root)
:   Returns the root of the chord. Or if given a Pitch as the
    newroot will override the algorithm and always return that Pitch.

    ```python
    >>> cmaj = chord.Chord(['E3', 'C4', 'G5'])
    >>> cmaj.root()
    <music21.pitch.Pitch C4>
    ```

    Examples:

    ```python
    >>> cmaj = chord.Chord(['E', 'G', 'C'])
    >>> cmaj.root()
    <music21.pitch.Pitch C>
    ```

    For some chords we make an exception. For instance, take this chord in
    B-flat minor:

    ```python
    >>> aDim7no3rd = chord.Chord(['A3', 'E-4', 'G4'])
    ```

    It could be considered a type of E-flat 11 chord with a 3rd, but no 5th,
    7th, or 9th, in 5th inversion. That doesn’t make sense, so we should
    call it an A dim 7th chord
    with no 3rd.

    ```python
    >>> aDim7no3rd.root()
    <music21.pitch.Pitch A3>
    ```

    ```python
    >>> aDim7no3rdInv = chord.Chord(['E-3', 'A4', 'G4'])
    >>> aDim7no3rdInv.root()
    <music21.pitch.Pitch A4>
    ```

    The root of a 13th chord (which could be any chord in any inversion) is
    designed to be the bass:

    ```python
    >>> chord.Chord('F3 A3 C4 E-4 G-4 B4 D5').root()
    <music21.pitch.Pitch F3>
    ```

    Multiple pitches in different octaves do not interfere with root.

    ```python
    >>> lotsOfNotes = chord.Chord(['E3', 'C4', 'G4', 'B-4', 'E5', 'G5'])
    >>> r = lotsOfNotes.root()
    >>> r
    <music21.pitch.Pitch C4>
    ```

    ```python
    >>> r is lotsOfNotes.pitches[1]
    True
    ```

    Setting of a root may happen for a number of reasons, such as
    in the case where music21’s idea of a root differs from the interpreter’s.

    To specify the root directly, pass the pitch to the root function:

    ```python
    >>> cSus4 = chord.Chord('C4 F4 G4')
    >>> cSus4.root()  # considered by music21 to be an F9 chord in 2nd inversion
    <music21.pitch.Pitch F4>
    ```

    Change it to be a Csus4:

    ```python
    >>> cSus4.root('C4')
    >>> cSus4.root()
    <music21.pitch.Pitch C4>
    ```

    Note that if passing in a string as the root,
    the root is set to a pitch in the chord if possible.

    ```python
    >>> cSus4.root() is cSus4.pitches[0]
    True
    ```

    You might also want to supply an “implied root.” For instance, some people
    call a diminished seventh chord (generally viio7)
    a dominant chord with an omitted root (Vo9) – here we will specify the root
    to be a note not in the chord:

    ```python
    >>> vo9 = chord.Chord(['B3', 'D4', 'F4', 'A-4'])
    >>> vo9.root()
    <music21.pitch.Pitch B3>
    ```

    ```python
    >>> vo9.root(pitch.Pitch('G3'))
    >>> vo9.root()
    <music21.pitch.Pitch G3>
    ```

    When setting a root, the pitches of the chord are left untouched:

    ```python
    >>> [p.nameWithOctave for p in vo9.pitches]
    ['B3', 'D4', 'F4', 'A-4']
    ```

    By default, this method uses an algorithm to find the root among the
    chord’s pitches, if no root has been previously specified. If a root
    has been explicitly specified, as in the Csus4 chord above, it can be
    returned to the original root() by setting find explicitly to True:

    ```python
    >>> cSus4.root(find=True)
    <music21.pitch.Pitch F4>
    ```

    Subsequent calls without find=True have also removed the overridden root:

    ```python
    >>> cSus4.root()
    <music21.pitch.Pitch F4>
    ```

    If for some reason you do not want the root-finding algorithm to be
    run (for instance, checking to see if an overridden root has been
    specified) set find=False. “None” will be returned if no root has been specified.

    ```python
    >>> c = chord.Chord(['E3', 'G3', 'B4'])
    >>> print(c.root(find=False))
    None
    ```

    Chord symbols, for instance, have their root already specified on construction:

    ```python
    >>> d = harmony.ChordSymbol('CM/E')
    >>> d.root(find=False)
    <music21.pitch.Pitch C4>
    ```

    There is no need to set find=False in this case, however, the
    algorithm will skip the slow part of finding the root if it
    has been specified (or already found and no pitches have changed).

    A chord with no pitches has no root and raises a ChordException.

    ```python
    >>> chord.Chord().root()
    Traceback (most recent call last):
    music21.chord.ChordException: no pitches in chord <music21.chord.Chord ...>
    ```

    * Changed in v5.2: find is a keyword-only parameter,
      newroot finds Pitch in Chord

NoChord.transpose(*\_value*, *\**, *inPlace=False*) → [Self](https://docs.python.org/3/library/typing.html#typing.Self "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/harmony.html#NoChord.transpose)
:   Overrides [`transpose()`](moduleChord.html#music21.chord.Chord.transpose "music21.chord.Chord.transpose") to do nothing.

    ```python
    >>> nc = harmony.NoChord()
    >>> nc.figure
    'N.C.'
    >>> nc.transpose(8, inPlace=True)
    >>> nc.figure
    'N.C.'
    ```

Methods inherited from [`ChordSymbol`](#music21.harmony.ChordSymbol "music21.harmony.ChordSymbol"):

|  |  |  |
| --- | --- | --- |
| * [`findFigure()`](#music21.harmony.ChordSymbol.findFigure "music21.harmony.ChordSymbol.findFigure") | * [`inversionIsValid()`](#music21.harmony.ChordSymbol.inversionIsValid "music21.harmony.ChordSymbol.inversionIsValid") |  |

Methods inherited from [`Harmony`](#music21.harmony.Harmony "music21.harmony.Harmony"):

|  |  |  |
| --- | --- | --- |
| * [`addChordStepModification()`](#music21.harmony.Harmony.addChordStepModification "music21.harmony.Harmony.addChordStepModification") | * [`getChordStepModifications()`](#music21.harmony.Harmony.getChordStepModifications "music21.harmony.Harmony.getChordStepModifications") |  |

Methods inherited from [`Chord`](moduleChord.html#music21.chord.Chord "music21.chord.Chord"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleChord.html#music21.chord.Chord.__eq__ "music21.chord.Chord.__eq__") * [`__getitem__()`](moduleChord.html#music21.chord.Chord.__getitem__ "music21.chord.Chord.__getitem__") * [`add()`](moduleChord.html#music21.chord.Chord.add "music21.chord.Chord.add") * [`annotateIntervals()`](moduleChord.html#music21.chord.Chord.annotateIntervals "music21.chord.Chord.annotateIntervals") * [`areZRelations()`](moduleChord.html#music21.chord.Chord.areZRelations "music21.chord.Chord.areZRelations") * [`canBeDominantV()`](moduleChord.html#music21.chord.Chord.canBeDominantV "music21.chord.Chord.canBeDominantV") * [`canBeTonic()`](moduleChord.html#music21.chord.Chord.canBeTonic "music21.chord.Chord.canBeTonic") * [`closedPosition()`](moduleChord.html#music21.chord.Chord.closedPosition "music21.chord.Chord.closedPosition") * [`containsSeventh()`](moduleChord.html#music21.chord.Chord.containsSeventh "music21.chord.Chord.containsSeventh") * [`containsTriad()`](moduleChord.html#music21.chord.Chord.containsTriad "music21.chord.Chord.containsTriad") * [`formatVectorString()`](moduleChord.html#music21.chord.Chord.formatVectorString "music21.chord.Chord.formatVectorString") * [`geometricNormalForm()`](moduleChord.html#music21.chord.Chord.geometricNormalForm "music21.chord.Chord.geometricNormalForm") * [`getChordStep()`](moduleChord.html#music21.chord.Chord.getChordStep "music21.chord.Chord.getChordStep") * [`getColor()`](moduleChord.html#music21.chord.Chord.getColor "music21.chord.Chord.getColor") * [`getNotehead()`](moduleChord.html#music21.chord.Chord.getNotehead "music21.chord.Chord.getNotehead") * [`getNoteheadFill()`](moduleChord.html#music21.chord.Chord.getNoteheadFill "music21.chord.Chord.getNoteheadFill") * [`getStemDirection()`](moduleChord.html#music21.chord.Chord.getStemDirection "music21.chord.Chord.getStemDirection") * [`getTie()`](moduleChord.html#music21.chord.Chord.getTie "music21.chord.Chord.getTie") * [`getVolume()`](moduleChord.html#music21.chord.Chord.getVolume "music21.chord.Chord.getVolume") * [`getZRelation()`](moduleChord.html#music21.chord.Chord.getZRelation "music21.chord.Chord.getZRelation") * [`hasAnyEnharmonicSpelledPitches()`](moduleChord.html#music21.chord.Chord.hasAnyEnharmonicSpelledPitches "music21.chord.Chord.hasAnyEnharmonicSpelledPitches") * [`hasAnyRepeatedDiatonicNote()`](moduleChord.html#music21.chord.Chord.hasAnyRepeatedDiatonicNote "music21.chord.Chord.hasAnyRepeatedDiatonicNote") | * [`hasRepeatedChordStep()`](moduleChord.html#music21.chord.Chord.hasRepeatedChordStep "music21.chord.Chord.hasRepeatedChordStep") * [`intervalFromChordStep()`](moduleChord.html#music21.chord.Chord.intervalFromChordStep "music21.chord.Chord.intervalFromChordStep") * [`inversion()`](moduleChord.html#music21.chord.Chord.inversion "music21.chord.Chord.inversion") * [`inversionName()`](moduleChord.html#music21.chord.Chord.inversionName "music21.chord.Chord.inversionName") * [`inversionText()`](moduleChord.html#music21.chord.Chord.inversionText "music21.chord.Chord.inversionText") * [`isAugmentedSixth()`](moduleChord.html#music21.chord.Chord.isAugmentedSixth "music21.chord.Chord.isAugmentedSixth") * [`isAugmentedTriad()`](moduleChord.html#music21.chord.Chord.isAugmentedTriad "music21.chord.Chord.isAugmentedTriad") * [`isConsonant()`](moduleChord.html#music21.chord.Chord.isConsonant "music21.chord.Chord.isConsonant") * [`isDiminishedSeventh()`](moduleChord.html#music21.chord.Chord.isDiminishedSeventh "music21.chord.Chord.isDiminishedSeventh") * [`isDiminishedTriad()`](moduleChord.html#music21.chord.Chord.isDiminishedTriad "music21.chord.Chord.isDiminishedTriad") * [`isDominantSeventh()`](moduleChord.html#music21.chord.Chord.isDominantSeventh "music21.chord.Chord.isDominantSeventh") * [`isFalseDiminishedSeventh()`](moduleChord.html#music21.chord.Chord.isFalseDiminishedSeventh "music21.chord.Chord.isFalseDiminishedSeventh") * [`isFrenchAugmentedSixth()`](moduleChord.html#music21.chord.Chord.isFrenchAugmentedSixth "music21.chord.Chord.isFrenchAugmentedSixth") * [`isGermanAugmentedSixth()`](moduleChord.html#music21.chord.Chord.isGermanAugmentedSixth "music21.chord.Chord.isGermanAugmentedSixth") * [`isHalfDiminishedSeventh()`](moduleChord.html#music21.chord.Chord.isHalfDiminishedSeventh "music21.chord.Chord.isHalfDiminishedSeventh") * [`isIncompleteMajorTriad()`](moduleChord.html#music21.chord.Chord.isIncompleteMajorTriad "music21.chord.Chord.isIncompleteMajorTriad") * [`isIncompleteMinorTriad()`](moduleChord.html#music21.chord.Chord.isIncompleteMinorTriad "music21.chord.Chord.isIncompleteMinorTriad") * [`isItalianAugmentedSixth()`](moduleChord.html#music21.chord.Chord.isItalianAugmentedSixth "music21.chord.Chord.isItalianAugmentedSixth") * [`isMajorTriad()`](moduleChord.html#music21.chord.Chord.isMajorTriad "music21.chord.Chord.isMajorTriad") * [`isMinorTriad()`](moduleChord.html#music21.chord.Chord.isMinorTriad "music21.chord.Chord.isMinorTriad") * [`isNinth()`](moduleChord.html#music21.chord.Chord.isNinth "music21.chord.Chord.isNinth") | * [`isSeventh()`](moduleChord.html#music21.chord.Chord.isSeventh "music21.chord.Chord.isSeventh") * [`isSeventhOfType()`](moduleChord.html#music21.chord.Chord.isSeventhOfType "music21.chord.Chord.isSeventhOfType") * [`isSwissAugmentedSixth()`](moduleChord.html#music21.chord.Chord.isSwissAugmentedSixth "music21.chord.Chord.isSwissAugmentedSixth") * [`isTranspositionallySymmetrical()`](moduleChord.html#music21.chord.Chord.isTranspositionallySymmetrical "music21.chord.Chord.isTranspositionallySymmetrical") * [`isTriad()`](moduleChord.html#music21.chord.Chord.isTriad "music21.chord.Chord.isTriad") * [`removeRedundantPitchClasses()`](moduleChord.html#music21.chord.Chord.removeRedundantPitchClasses "music21.chord.Chord.removeRedundantPitchClasses") * [`removeRedundantPitchNames()`](moduleChord.html#music21.chord.Chord.removeRedundantPitchNames "music21.chord.Chord.removeRedundantPitchNames") * [`removeRedundantPitches()`](moduleChord.html#music21.chord.Chord.removeRedundantPitches "music21.chord.Chord.removeRedundantPitches") * [`semiClosedPosition()`](moduleChord.html#music21.chord.Chord.semiClosedPosition "music21.chord.Chord.semiClosedPosition") * [`semitonesFromChordStep()`](moduleChord.html#music21.chord.Chord.semitonesFromChordStep "music21.chord.Chord.semitonesFromChordStep") * [`setColor()`](moduleChord.html#music21.chord.Chord.setColor "music21.chord.Chord.setColor") * [`setNotehead()`](moduleChord.html#music21.chord.Chord.setNotehead "music21.chord.Chord.setNotehead") * [`setNoteheadFill()`](moduleChord.html#music21.chord.Chord.setNoteheadFill "music21.chord.Chord.setNoteheadFill") * [`setStemDirection()`](moduleChord.html#music21.chord.Chord.setStemDirection "music21.chord.Chord.setStemDirection") * [`setTie()`](moduleChord.html#music21.chord.Chord.setTie "music21.chord.Chord.setTie") * [`setVolume()`](moduleChord.html#music21.chord.Chord.setVolume "music21.chord.Chord.setVolume") * [`simplifyEnharmonics()`](moduleChord.html#music21.chord.Chord.simplifyEnharmonics "music21.chord.Chord.simplifyEnharmonics") * [`sortAscending()`](moduleChord.html#music21.chord.Chord.sortAscending "music21.chord.Chord.sortAscending") * [`sortChromaticAscending()`](moduleChord.html#music21.chord.Chord.sortChromaticAscending "music21.chord.Chord.sortChromaticAscending") * [`sortDiatonicAscending()`](moduleChord.html#music21.chord.Chord.sortDiatonicAscending "music21.chord.Chord.sortDiatonicAscending") * [`sortFrequencyAscending()`](moduleChord.html#music21.chord.Chord.sortFrequencyAscending "music21.chord.Chord.sortFrequencyAscending") |

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

[`NoChord`](#music21.harmony.NoChord "music21.harmony.NoChord") instance variables

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

## Functions

music21.harmony.chordSymbolFigureFromChord(*inChord: [Chord](moduleChord.html#music21.chord.Chord "music21.chord.Chord")*, *includeChordType=False*)[[source]](../_modules/music21/harmony.html#chordSymbolFigureFromChord)
:   Analyze the given chord, and attempt to describe its pitches using a
    standard chord symbol figure.

    The pitches of the chord are analyzed based on intervals, and compared to
    standard triads, sevenths, ninths, elevenths, and thirteenth chords. The
    type of chord therefore is determined if it matches (given certain
    guidelines documented below) and the figure is returned. There is no
    standard “chord symbol” notation, so a typical notation is used that can be
    easily modified if desired by changing a dictionary in the source code.

    Set includeChordType to true (default is False) to return a tuple, the
    first element being the figure and the second element the identified chord
    type.

    ```python
    >>> harmony.chordSymbolFigureFromChord(chord.Chord(['C3', 'E3', 'G3']))
    'C'
    ```

    THIRDS

    ```python
    >>> c = chord.Chord(['C3', 'E3', 'G3'])
    >>> harmony.chordSymbolFigureFromChord(c, True)
    ('C', 'major')
    ```

    ```python
    >>> c = chord.Chord(['B-3', 'D-4', 'F4'])
    >>> harmony.chordSymbolFigureFromChord(c, True)
    ('B-m', 'minor')
    ```

    ```python
    >>> c = chord.Chord(['F#3', 'A#3', 'C##4'])
    >>> harmony.chordSymbolFigureFromChord(c, True)
    ('F#+', 'augmented')
    ```

    ```python
    >>> c = chord.Chord(['C3', 'E-3', 'G-3'])
    >>> harmony.chordSymbolFigureFromChord(c, True)
    ('Cdim', 'diminished')
    ```

    SEVENTHS

    ```python
    >>> c = chord.Chord(['E-3', 'G3', 'B-3', 'D-4'])
    >>> harmony.chordSymbolFigureFromChord(c, True)
    ('E-7', 'dominant-seventh')
    ```

    ```python
    >>> c = chord.Chord(['C3', 'E3', 'G3', 'B3'])
    >>> harmony.chordSymbolFigureFromChord(c, True)
    ('Cmaj7', 'major-seventh')
    ```

    ```python
    >>> c = chord.Chord(['F#3', 'A3', 'C#4', 'E#4'])
    >>> harmony.chordSymbolFigureFromChord(c, True)
    ('F#mM7', 'minor-major-seventh')
    ```

    ```python
    >>> c = chord.Chord(['F3', 'A-3', 'C4', 'E-4'])
    >>> harmony.chordSymbolFigureFromChord(c, True)
    ('Fm7', 'minor-seventh')
    ```

    ```python
    >>> c = chord.Chord(['F3', 'A3', 'C#4', 'E4'])
    >>> harmony.chordSymbolFigureFromChord(c, True)
    ('F+M7', 'augmented-major-seventh')
    ```

    ```python
    >>> c = chord.Chord(['C3', 'E3', 'G#3', 'B-3'])
    >>> harmony.chordSymbolFigureFromChord(c, True)
    ('C7+', 'augmented-seventh')
    ```

    ```python
    >>> c = chord.Chord(['G3', 'B-3', 'D-4', 'F4'])
    >>> harmony.chordSymbolFigureFromChord(c, True)
    ('Gø7', 'half-diminished-seventh')
    ```

    ```python
    >>> c = chord.Chord(['C3', 'E-3', 'G-3', 'B--3'])
    >>> harmony.chordSymbolFigureFromChord(c, True)
    ('Co7', 'diminished-seventh')
    ```

    ```python
    >>> c = chord.Chord(['B-3', 'D4', 'F-4', 'A-4'])
    >>> harmony.chordSymbolFigureFromChord(c, True)
    ('B-dom7dim5', 'seventh-flat-five')
    ```

    NINTHS

    ```python
    >>> c = chord.Chord(['C3', 'E3', 'G3', 'B3', 'D3'])
    >>> harmony.chordSymbolFigureFromChord(c, True)
    ('CM9', 'major-ninth')
    ```

    ```python
    >>> c = chord.Chord(['B-3', 'D4', 'F4', 'A-4', 'C4'])
    >>> harmony.chordSymbolFigureFromChord(c, True)
    ('B-9', 'dominant-ninth')
    ```

    ```python
    >>> c = chord.Chord(['E-3', 'G-3', 'B-3', 'D4', 'F3'])
    >>> harmony.chordSymbolFigureFromChord(c, True)
    ('E-mM9', 'minor-major-ninth')
    ```

    ```python
    >>> c = chord.Chord(['C3', 'E-3', 'G3', 'B-3', 'D3'])
    >>> harmony.chordSymbolFigureFromChord(c, True)
    ('Cm9', 'minor-ninth')
    ```

    ```python
    >>> c = chord.Chord(['F#3', 'A#3', 'C##4', 'E#4', 'G#3'])
    >>> harmony.chordSymbolFigureFromChord(c, True)
    ('F#+M9', 'augmented-major-ninth')
    ```

    ```python
    >>> c = chord.Chord(['G3', 'B3', 'D#4', 'F4', 'A3'])
    >>> harmony.chordSymbolFigureFromChord(c, True)
    ('G9#5', 'augmented-dominant-ninth')
    ```

    ```python
    >>> c = chord.Chord(['C3', 'E-3', 'G-3', 'B-3', 'D3'])
    >>> harmony.chordSymbolFigureFromChord(c, True)
    ('Cø9', 'half-diminished-ninth')
    ```

    ```python
    >>> c = chord.Chord(['B-3', 'D-4', 'F-4', 'A-4', 'C-4'])
    >>> harmony.chordSymbolFigureFromChord(c, True)
    ('B-øb9', 'half-diminished-minor-ninth')
    ```

    ```python
    >>> c = chord.Chord(['C3', 'E-3', 'G-3', 'B--3', 'D3'])
    >>> harmony.chordSymbolFigureFromChord(c, True)
    ('Co9', 'diminished-ninth')
    ```

    ```python
    >>> c = chord.Chord(['F3', 'A-3', 'C-4', 'E--4', 'G-3'])
    >>> harmony.chordSymbolFigureFromChord(c, True)
    ('Fob9', 'diminished-minor-ninth')
    ```

    This harmony can either be CmaddD or Csus2addE-. music21 prefers the former.
    Change the ordering of harmony.CHORD\_TYPES to switch the preference. From Bach BWV380

    ```python
    >>> c = chord.Chord(['C3', 'D4', 'G4', 'E-5'])
    >>> harmony.chordSymbolFigureFromChord(c, True)
    ('CmaddD', 'minor')
    ```

    ELEVENTHS

    ```python
    >>> c = chord.Chord(['E-3', 'G3', 'B-3', 'D-4', 'F3', 'A-3'] )
    >>> harmony.chordSymbolFigureFromChord(c, True)
    ('E-11', 'dominant-11th')
    ```

    ```python
    >>> c = chord.Chord(['G3', 'B3', 'D4', 'F#4', 'A3', 'C4'])
    >>> harmony.chordSymbolFigureFromChord(c, True)
    ('GM11', 'major-11th')
    ```

    ```python
    >>> c = chord.Chord(['C3', 'E-3', 'G3', 'B3', 'D3', 'F3'])
    >>> harmony.chordSymbolFigureFromChord(c, True)
    ('CmM11', 'minor-major-11th')
    ```

    ```python
    >>> c = chord.Chord(['F#3', 'A3', 'C#4', 'E4', 'G#3', 'B3'])
    >>> harmony.chordSymbolFigureFromChord(c, True)
    ('F#m11', 'minor-11th')
    ```

    ```python
    >>> c = chord.Chord(['B-3', 'D4', 'F#4', 'A4', 'C4', 'E-4'])
    >>> harmony.chordSymbolFigureFromChord(c, True)
    ('B-+M11', 'augmented-major-11th')
    ```

    ```python
    >>> c = chord.Chord(['F3', 'A3', 'C#4', 'E-4', 'G3', 'B-3'])
    >>> harmony.chordSymbolFigureFromChord(c, True)
    ('F+11', 'augmented-11th')
    ```

    ```python
    >>> c = chord.Chord(['G3', 'B-3', 'D-4', 'F4', 'A3', 'C4'])
    >>> harmony.chordSymbolFigureFromChord(c, True)
    ('Gø11', 'half-diminished-11th')
    ```

    ```python
    >>> c = chord.Chord(['E-3', 'G-3', 'B--3', 'D--4', 'F3', 'A-3'])
    >>> harmony.chordSymbolFigureFromChord(c, True)
    ('E-o11', 'diminished-11th')
    ```

    THIRTEENTHS

    These are so tricky: music21 needs to be told what the root is in these cases
    all tests here are ‘C’ chords, but any root will work:

    ```python
    >>> c = chord.Chord(['C3', 'E3', 'G3', 'B3', 'D4', 'F4', 'A4'])
    >>> c.root('C3')
    >>> harmony.chordSymbolFigureFromChord(c, True)
    ('CM13', 'major-13th')
    ```

    ```python
    >>> c = chord.Chord(['C3', 'E3', 'G3', 'B-3', 'D4', 'F4', 'A4'])
    >>> c.root('C3')
    >>> harmony.chordSymbolFigureFromChord(c, True)
    ('C13', 'dominant-13th')
    ```

    ```python
    >>> c = chord.Chord(['C3', 'E-3', 'G3', 'B3', 'D4', 'F4', 'A4'])
    >>> c.root('C3')
    >>> harmony.chordSymbolFigureFromChord(c, True)
    ('CmM13', 'minor-major-13th')
    ```

    ```python
    >>> c = chord.Chord(['C3', 'E-3', 'G3', 'B-3', 'D4', 'F4', 'A4'])
    >>> c.root('C3')
    >>> harmony.chordSymbolFigureFromChord(c, True)
    ('Cm13', 'minor-13th')
    ```

    ```python
    >>> c = chord.Chord(['C3', 'E3', 'G#3', 'B3', 'D4', 'F4', 'A4'])
    >>> c.root('C3')
    >>> harmony.chordSymbolFigureFromChord(c, True)
    ('C+M13', 'augmented-major-13th')
    ```

    ```python
    >>> c = chord.Chord(['C3', 'E3', 'G#3', 'B-3', 'D4', 'F4', 'A4'])
    >>> c.root('C3')
    >>> harmony.chordSymbolFigureFromChord(c, True)
    ('C+13', 'augmented-dominant-13th')
    ```

    ```python
    >>> c = chord.Chord(['C3', 'E-3', 'G-3', 'B-3', 'D4', 'F4', 'A4'])
    >>> c.root('C3')
    >>> harmony.chordSymbolFigureFromChord(c, True)
    ('Cø13', 'half-diminished-13th')
    ```

    Pop chords are typically not always “strictly” spelled and often certain degrees
    are omitted. Therefore, the following common chord omissions are permitted
    and the chord will still be identified correctly:

    * triads: none
    * seventh chords: none
    * ninth chords: fifth
    * eleventh chords: third and/or fifth
    * thirteenth chords: fifth, eleventh, ninth

    This chord could be minor 7th with a C4, but because this 5th is not present,
    it is not identified.

    ```python
    >>> c = chord.Chord(['F3', 'A-3', 'E-4'])
    >>> harmony.chordSymbolFigureFromChord(c)
    'Chord Symbol Cannot Be Identified'
    ```

    Removing the fifth G3 (fifth of chord)

    ```python
    >>> c = chord.Chord(['C3', 'E3',  'B3', 'D3'])
    >>> harmony.chordSymbolFigureFromChord(c, True)
    ('CM9', 'major-ninth')
    ```

    Chord with G3 and B-3 removed (3rd & 5th of chord)

    ```python
    >>> c = chord.Chord(['E-3', 'D-4', 'F3', 'A-3'] )
    ```

    Without a 3rd and 5th, root() algorithm can’t locate the root,
    so we must tell it the root (or write an algorithm that assumes the root is the
    lowest note if the root can’t be found)

    ```python
    >>> c.root('E-3')
    >>> harmony.chordSymbolFigureFromChord(c, True)
    ('E-11', 'dominant-11th')
    ```

    Inversions are supported, and indicated with a ‘/’ between the root, type-string, and bass

    ```python
    >>> c = chord.Chord([ 'G#3', 'B-3', 'C4', 'E4',])
    >>> harmony.chordSymbolFigureFromChord(c, True)
    ('C7+/G#', 'augmented-seventh')
    ```

    ```python
    >>> c = chord.Chord(['G#2', 'B2', 'F#3', 'A3', 'C#4', 'E4'])
    >>> harmony.chordSymbolFigureFromChord(c, True)
    ('F#m11/G#', 'minor-11th')
    ```

    if the algorithm matches the chord, but omissions or subtractions are present,
    the chord symbol attempts to indicate this (although there is no standard way of doing
    this so the notation might be different from what you’re familiar with).

    An example of using this algorithm for identifying chords “in the wild”:

    ```python
    >>> score = corpus.parse('bach/bwv380')
    >>> excerpt = score.measures(2, 3)
    >>> chfy = excerpt.chordify()
    >>> for c in chfy.flatten().getElementsByClass(chord.Chord):
    ...   print(harmony.chordSymbolFigureFromChord(c))
    B-7
    E-maj7/B-
    B-7
    Chord Symbol Cannot Be Identified
    B-7
    E-
    B-
    Chord Symbol Cannot Be Identified
    B-/D
    B-7
    CmaddD
    Cm/D
    E-+M7/D
    Cm/E-
    F7
    ```

    Notice, however, that this excerpt contains many embellishment and non-harmonic tones,
    so an algorithm to truly identify the chord symbols must be as complex as any harmonic
    analysis algorithm, which this is not, so innately this method is flawed.

    And for the sake of completeness, unique chords supported by musicxml that
    this method can still successfully identify. Notice that the root must
    often be specified for this method to work.

    ```python
    >>> c = chord.Chord(['C3', 'D3', 'G3'])
    >>> harmony.chordSymbolFigureFromChord(c, True)
    ('Csus2', 'suspended-second')
    >>> c.root()
    <music21.pitch.Pitch C3>
    >>> c.bass()
    <music21.pitch.Pitch C3>
    ```

    ```python
    >>> c = chord.Chord(['C3', 'F3', 'G3'])
    >>> harmony.chordSymbolFigureFromChord(c, True)
    ('Csus', 'suspended-fourth')
    >>> c.root()
    <music21.pitch.Pitch C3>
    >>> c.inversion()
    0
    ```

    ```python
    >>> c = chord.Chord(['C3', 'D-3', 'E3', 'G-3'])
    >>> harmony.chordSymbolFigureFromChord(c, True)
    ('CN6', 'Neapolitan')
    ```

    ```python
    >>> c = chord.Chord(['C3', 'F#3', 'A-3'])
    >>> c.root('C3')
    >>> harmony.chordSymbolFigureFromChord(c, True)
    ('CIt+6', 'Italian')
    ```

    ```python
    >>> c = chord.Chord(['C3', 'D3', 'F#3', 'A-3'])
    >>> c.root('C3')
    >>> harmony.chordSymbolFigureFromChord(c, True)
    ('CFr+6', 'French')
    ```

    ```python
    >>> c = chord.Chord(['C3', 'E-3', 'F#3', 'A-3'])
    >>> c.root('C3')
    >>> harmony.chordSymbolFigureFromChord(c, True)
    ('CGr+6', 'German')
    ```

    ```python
    >>> eflat = chord.Chord(['E-3'])
    >>> harmony.chordSymbolFigureFromChord(eflat, True)
    ('E-pedal', 'pedal')
    ```

    ```python
    >>> c = chord.Chord(['C3', 'G3'])
    >>> harmony.chordSymbolFigureFromChord(c, True)
    ('Cpower', 'power')
    ```

    ```python
    >>> c = chord.Chord(['F3', 'G#3', 'B3', 'D#4'] )
    >>> c.root('F3')
    >>> harmony.chordSymbolFigureFromChord(c, True)
    ('Ftristan', 'Tristan')
    ```

    This algorithm works as follows:

    1. chord is analyzed for root (using chord’s root() )
       if the root cannot be determined, error is raised
       be aware that the root() method determines the root based on which note has
       the most thirds above it
       this is not a consistent way to determine the root of 13th chords, for example
    2. a chord vector is extracted from the chord
       :   using [`music21.chord.Chord.semitonesFromChordStep()`](moduleChord.html#music21.chord.Chord.semitonesFromChordStep "music21.chord.Chord.semitonesFromChordStep")
           this vector extracts the following degrees: (2, 3, 4, 5, 6, 7, 9, 11, and 13)
    3. this vector is converted to fbNotationString (in the form of chord step,
       :   and a ‘-’ or ‘#’ to indicate semitone distance)
    4. the fbNotationString is matched against the CHORD\_TYPES dictionary in this harmony module,
       :   although certain subtractions are permitted for example a 9th chord will
           still be identified correctly even if it is missing the 5th
    5. the type with the most identical matches is used, and if no type matches,
       :   “Chord Type Cannot Be Identified” is returned
    6. the output format for the chord symbol figure is the chord’s root,
       :   the chord type’s Abbreviation (saved in CHORD\_TYPES dictionary),
           a ‘/’ if the chord is in an inversion, and the chord’s bass

    The chord symbol nomenclature is not entirely standardized. There are several
    ways to write each abbreviation.

    For example, an augmented triad might be symbolized with ‘+’ or ‘aug’.
    Thus, by default the returned symbol is the first (element 0) in the CHORD\_TYPES list.
    For example (Eb minor eleventh chord, second inversion):

    > root + chord-type-str + ‘/’ + bass = ‘E-min11/B-’

    Users who wish to change these defaults can simply change that
    entry in the CHORD\_TYPES dictionary.

    ```python
    >>> harmony.chordSymbolFigureFromChord(chord.Chord(['C2', 'E2', 'G2']))
    'C'
    ```

    ```python
    >>> harmony.changeAbbreviationFor('major', 'maj')
    >>> harmony.chordSymbolFigureFromChord(chord.Chord(['C2', 'E2', 'G2']))
    'Cmaj'
    ```

music21.harmony.addNewChordSymbol(*chordTypeName*, *fbNotationString*, *AbbreviationList*)[[source]](../_modules/music21/harmony.html#addNewChordSymbol)
:   Add a new chord symbol:

    ```python
    >>> harmony.addNewChordSymbol('BethChord', '1,3,-6,#9', ['MH', 'beth'])
    >>> [str(p) for p in harmony.ChordSymbol('BMH').pitches]
    ['B2', 'C##3', 'D#3', 'G3']
    ```

    ```python
    >>> harmony.ChordSymbol('Cbeth').pitches
    (<music21.pitch.Pitch C3>, <music21.pitch.Pitch D#3>,
     <music21.pitch.Pitch E3>, <music21.pitch.Pitch A-3>)
    ```

    ```python
    >>> harmony.ChordSymbol('C-beth').pitches
    (<music21.pitch.Pitch C-3>, <music21.pitch.Pitch D3>,
     <music21.pitch.Pitch E-3>, <music21.pitch.Pitch A--3>)
    ```

music21.harmony.changeAbbreviationFor(*chordType*, *changeTo*)[[source]](../_modules/music21/harmony.html#changeAbbreviationFor)
:   Change the current Abbreviation used for a certain
    [`music21.harmony.ChordSymbol`](#music21.harmony.ChordSymbol "music21.harmony.ChordSymbol") chord type

    ```python
    >>> harmony.getCurrentAbbreviationFor('minor')
    'm'
    ```

    ```python
    >>> harmony.changeAbbreviationFor('minor', 'min')
    >>> harmony.getCurrentAbbreviationFor('minor')
    'min'
    ```

music21.harmony.chordSymbolFromChord(*inChord: [Chord](moduleChord.html#music21.chord.Chord "music21.chord.Chord")*) → [ChordSymbol](#music21.harmony.ChordSymbol "music21.harmony.ChordSymbol")[[source]](../_modules/music21/harmony.html#chordSymbolFromChord)
:   Get the `chordSymbol` object from the chord, using
    `music21.harmony.Harmony.chordSymbolFigureFromChord()`

    ```python
    >>> c = chord.Chord(['D3', 'F3', 'A4', 'B-5'])
    >>> symbol = harmony.chordSymbolFromChord(c)
    >>> symbol
    <music21.harmony.ChordSymbol B-maj7/D>
    >>> c.pitches == symbol.pitches
    True
    ```

music21.harmony.getAbbreviationListGivenChordType(*chordType*)[[source]](../_modules/music21/harmony.html#getAbbreviationListGivenChordType)
:   Get the Abbreviation list (all allowed Abbreviations that map to this
    [`music21.harmony.ChordSymbol`](#music21.harmony.ChordSymbol "music21.harmony.ChordSymbol") object):

    ```python
    >>> harmony.getAbbreviationListGivenChordType('minor-major-13th')
    ['mM13', 'minmaj13']
    ```

music21.harmony.getCurrentAbbreviationFor(*chordType*)[[source]](../_modules/music21/harmony.html#getCurrentAbbreviationFor)
:   Return the current Abbreviation for a given
    [`music21.harmony.ChordSymbol`](#music21.harmony.ChordSymbol "music21.harmony.ChordSymbol") chordType:

    ```python
    >>> harmony.getCurrentAbbreviationFor('dominant-seventh')
    '7'
    ```

music21.harmony.getNotationStringGivenChordType(*chordType*)[[source]](../_modules/music21/harmony.html#getNotationStringGivenChordType)
:   Get the notation string (fb-notation style) associated with this
    [`music21.harmony.ChordSymbol`](#music21.harmony.ChordSymbol "music21.harmony.ChordSymbol") chordType

    ```python
    >>> harmony.getNotationStringGivenChordType('German')
    '1,-3,#4,-6'
    ```

music21.harmony.realizeChordSymbolDurations(*piece*)[[source]](../_modules/music21/harmony.html#realizeChordSymbolDurations)
:   Returns music21 stream with duration attribute of chord symbols correctly
    set. Duration of chord symbols is based on the surrounding chord symbols;
    The chord symbol continues duration until another chord symbol is located
    or the piece ends.

    ```python
    >>> s = stream.Score()
    >>> s.append(harmony.ChordSymbol('C'))
    >>> s.repeatAppend(note.Note('C'), 4)
    >>> s.append(harmony.ChordSymbol('C'))
    >>> s.repeatAppend(note.Note('C'), 4)
    >>> s = s.makeMeasures()
    ```

    ```python
    >>> harmony.realizeChordSymbolDurations(s).show('text')
    {0.0} <music21.clef.BassClef>
    {0.0} <music21.meter.TimeSignature 4/4>
    {0.0} <music21.harmony.ChordSymbol C>
    {0.0} <music21.note.Note C>
    {1.0} <music21.note.Note C>
    {2.0} <music21.note.Note C>
    {3.0} <music21.note.Note C>
    {4.0} <music21.harmony.ChordSymbol C>
    {4.0} <music21.note.Note C>
    {5.0} <music21.note.Note C>
    {6.0} <music21.note.Note C>
    {7.0} <music21.note.Note C>
    {8.0} <music21.bar.Barline type=final>
    ```

    If only one chord symbol object is present:

    ```python
    >>> s = stream.Score()
    >>> s.append(harmony.ChordSymbol('C'))
    >>> s.repeatAppend(note.Note('C'), 4)
    >>> s = s.makeMeasures()
    >>> harmony.realizeChordSymbolDurations(s).show('text')
    {0.0} <music21.clef.BassClef>
    {0.0} <music21.meter.TimeSignature 4/4>
    {0.0} <music21.harmony.ChordSymbol C>
    {0.0} <music21.note.Note C>
    {1.0} <music21.note.Note C>
    {2.0} <music21.note.Note C>
    {3.0} <music21.note.Note C>
    {4.0} <music21.bar.Barline type=final>
    ```

    If a ChordSymbol object exists followed by many notes, duration represents
    all those notes (how else can the computer know to end the chord? if
    there’s no chord following it other than end the chord at the end of the
    piece?).

    ```python
    >>> s = stream.Score()
    >>> s.repeatAppend(note.Note('C'), 4)
    >>> s.append(harmony.ChordSymbol('C'))
    >>> s.repeatAppend(note.Note('C'), 8)
    >>> s = s.makeMeasures()
    >>> harmony.realizeChordSymbolDurations(s).show('text')
    {0.0} <music21.clef.BassClef>
    {0.0} <music21.meter.TimeSignature 4/4>
    {0.0} <music21.note.Note C>
    {1.0} <music21.note.Note C>
    {2.0} <music21.note.Note C>
    {3.0} <music21.note.Note C>
    {4.0} <music21.harmony.ChordSymbol C>
    {4.0} <music21.note.Note C>
    {5.0} <music21.note.Note C>
    {6.0} <music21.note.Note C>
    {7.0} <music21.note.Note C>
    {8.0} <music21.note.Note C>
    {9.0} <music21.note.Note C>
    {10.0} <music21.note.Note C>
    {11.0} <music21.note.Note C>
    {12.0} <music21.bar.Barline type=final>
    ```

music21.harmony.removeChordSymbols(*chordType*)[[source]](../_modules/music21/harmony.html#removeChordSymbols)
:   Remove the given chord type from the CHORD\_TYPES dictionary, so it
    can no longer be identified or parsed by harmony methods.
