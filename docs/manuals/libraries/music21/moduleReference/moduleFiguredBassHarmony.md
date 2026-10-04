Source: https://music21.org/music21docs/moduleReference/moduleFiguredBassHarmony.html

# music21.figuredBass.harmony

The FiguredBass object is a subclass of Harmony that will (eventually) be able
to represent figured bass symbols in music notation and also realize it.

BETA at this point.

Based on work by Jose Cabal-Ugaz.

## FiguredBass

class music21.figuredBass.harmony.FiguredBass(*figureString: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*, *\**, *figureStrings: [Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] = ()*, *\*\*keywords*)[[source]](../_modules/music21/figuredBass/harmony.html#FiguredBass)
:   *BETA*: FiguredBass objects are currently in beta and may change without warning.

    The FiguredBass objects store information about thorough bass figures.
    It is created as a representation for <fb> tags in MEI and <figured-bass> tags in MusicXML.
    The FiguredBass object derives from the Harmony object and can be used
    in the following way:

    ```python
    >>> fb = figuredBass.FiguredBass('#,6#')
    >>> fb
    <music21.figuredBass.harmony.FiguredBass #,6#>
    ```

    (note that the FiguredBass object can be found in either music21.figuredBass.FiguredBass
    or music21.figuredBass.harmony.FiguredBass. It is the same class)

    The single figures are stored as figuredBass.notation.Figure objects:

    ```python
    >>> fb.notation.figures[0]
    <music21.figuredBass.notation.Figure 3 <Modifier # sharp>>
    ```

    The figures can be accessed and manipulated individually by passing in figureStrings
    (plural), and extenders are allowed as with \_:

    ```python
    >>> fb2 = figuredBass.FiguredBass(figureStrings=['#_', '6#'])
    >>> fb2
    <music21.figuredBass.harmony.FiguredBass #_,6#>
    >>> fb2.notation.hasExtenders
    True
    ```

    Currently, figured bass objects do not have associated pitches. This will change.

    ```python
    >>> fb.pitches
    ()
    ```

    * New in v9.3

[`FiguredBass`](#music21.figuredBass.harmony.FiguredBass "music21.figuredBass.harmony.FiguredBass") bases

* [`Harmony`](moduleHarmony.html#music21.harmony.Harmony "music21.harmony.Harmony")
* [`Chord`](moduleChord.html#music21.chord.Chord "music21.chord.Chord")
* [`ChordBase`](moduleChord.html#music21.chord.ChordBase "music21.chord.ChordBase")
* [`NotRest`](moduleNote.html#music21.note.NotRest "music21.note.NotRest")
* [`GeneralNote`](moduleNote.html#music21.note.GeneralNote "music21.note.GeneralNote")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`FiguredBass`](#music21.figuredBass.harmony.FiguredBass "music21.figuredBass.harmony.FiguredBass") read-only properties

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

[`FiguredBass`](#music21.figuredBass.harmony.FiguredBass "music21.figuredBass.harmony.FiguredBass") read/write properties

FiguredBass.figureString
:   Get the figures as strings of the FiguresBass object.

    ```python
    >>> fb = figuredBass.FiguredBass('6,#')
    >>> fb.figureString
    '6,#'
    >>> fb.notation
    <music21.figuredBass.notation.Notation 6,#>
    ```

    When setting the figureString the notation property is updated as well:

    ```python
    >>> fb.figureString = '5,b'
    >>> fb.figureString
    '5,b'
    >>> fb.notation
    <music21.figuredBass.notation.Notation 5,b>
    ```

FiguredBass.figureStrings
:   Does the same as figureStrings but returns a list:

    ```python
    >>> fb = figuredBass.FiguredBass('6,#')
    >>> fb.figureStrings
    ['6', '#']
    ```

    Like figureString, figureStrings can be set as well and updates the notation property:

    ```python
    >>> fb.figureStrings = ['5', 'b']
    >>> fb.figureStrings
    ['5', 'b']
    >>> fb.notation
    <music21.figuredBass.notation.Notation 5,b>
    ```

FiguredBass.notation
:   Gets or sets the notation property of the FiguresBass object

    ```python
    >>> fb = figuredBass.FiguredBass('6,#')
    >>> fb.figureString
    '6,#'
    >>> fb.notation
    <music21.figuredBass.notation.Notation 6,#>
    ```

    When setting, this updates the figureString property as well.

    ```python
    >>> fb.notation = figuredBass.notation.Notation('7b,b')
    >>> fb.notation
    <music21.figuredBass.notation.Notation 7b,b>
    >>> fb.figureString
    '7b,b'
    ```

Read/write properties inherited from [`Harmony`](moduleHarmony.html#music21.harmony.Harmony "music21.harmony.Harmony"):

|  |  |  |
| --- | --- | --- |
| * [`figure`](moduleHarmony.html#music21.harmony.Harmony.figure "music21.harmony.Harmony.figure") * [`key`](moduleHarmony.html#music21.harmony.Harmony.key "music21.harmony.Harmony.key") | * [`romanNumeral`](moduleHarmony.html#music21.harmony.Harmony.romanNumeral "music21.harmony.Harmony.romanNumeral") | * [`writeAsChord`](moduleHarmony.html#music21.harmony.Harmony.writeAsChord "music21.harmony.Harmony.writeAsChord") |

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

[`FiguredBass`](#music21.figuredBass.harmony.FiguredBass "music21.figuredBass.harmony.FiguredBass") methods

Methods inherited from [`Harmony`](moduleHarmony.html#music21.harmony.Harmony "music21.harmony.Harmony"):

|  |  |  |
| --- | --- | --- |
| * [`addChordStepModification()`](moduleHarmony.html#music21.harmony.Harmony.addChordStepModification "music21.harmony.Harmony.addChordStepModification") | * [`findFigure()`](moduleHarmony.html#music21.harmony.Harmony.findFigure "music21.harmony.Harmony.findFigure") | * [`getChordStepModifications()`](moduleHarmony.html#music21.harmony.Harmony.getChordStepModifications "music21.harmony.Harmony.getChordStepModifications") |

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

[`FiguredBass`](#music21.figuredBass.harmony.FiguredBass "music21.figuredBass.harmony.FiguredBass") instance variables

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
