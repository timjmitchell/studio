Source: https://music21.org/music21docs/moduleReference/moduleTablature.html

# music21.tablature

Music21 representation of FretNote and FretBoard objects.

TODO:
Chord from Figure
Chord from FretBoard Object with tuning.

## BassGuitarFretBoard

class music21.tablature.BassGuitarFretBoard(*fretNotes=None*, *displayFrets=4*)[[source]](../_modules/music21/tablature.html#BassGuitarFretBoard)
:   A four-string fretboard tuned to E A D G

[`BassGuitarFretBoard`](#music21.tablature.BassGuitarFretBoard "music21.tablature.BassGuitarFretBoard") bases

* [`FretBoard`](#music21.tablature.FretBoard "music21.tablature.FretBoard")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`BassGuitarFretBoard`](#music21.tablature.BassGuitarFretBoard "music21.tablature.BassGuitarFretBoard") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`BassGuitarFretBoard`](#music21.tablature.BassGuitarFretBoard "music21.tablature.BassGuitarFretBoard") methods

Methods inherited from [`FretBoard`](#music21.tablature.FretBoard "music21.tablature.FretBoard"):

|  |  |  |
| --- | --- | --- |
| * [`fretNotesLowestFirst()`](#music21.tablature.FretBoard.fretNotesLowestFirst "music21.tablature.FretBoard.fretNotesLowestFirst") | * [`getFretNoteByString()`](#music21.tablature.FretBoard.getFretNoteByString "music21.tablature.FretBoard.getFretNoteByString") | * [`getPitches()`](#music21.tablature.FretBoard.getPitches "music21.tablature.FretBoard.getPitches") |

## ChordWithFretBoard

class music21.tablature.ChordWithFretBoard(*figure=None*, *numStrings=6*, *fretNotes=None*, *displayFrets=4*, *\*\*keywords*)[[source]](../_modules/music21/tablature.html#ChordWithFretBoard)
:   Music21Object subclass that combines a ChordSymbol with a FretBoard.
    Its tuning must be set.

    ```python
    >>> fn4 = tablature.FretNote(string=4, fret=0)
    >>> fn3 = tablature.FretNote(string=3, fret=2, fingering=2)
    >>> fn2 = tablature.FretNote(string=2, fret=3, fingering=3)
    >>> fn1 = tablature.FretNote(string=1, fret=2, fingering=4)
    >>> cwf = tablature.ChordWithFretBoard('Dm', fretNotes=[fn1, fn2, fn3, fn4])
    ```

[`ChordWithFretBoard`](#music21.tablature.ChordWithFretBoard "music21.tablature.ChordWithFretBoard") bases

* [`ChordSymbol`](moduleHarmony.html#music21.harmony.ChordSymbol "music21.harmony.ChordSymbol")
* [`Harmony`](moduleHarmony.html#music21.harmony.Harmony "music21.harmony.Harmony")
* [`Chord`](moduleChord.html#music21.chord.Chord "music21.chord.Chord")
* [`ChordBase`](moduleChord.html#music21.chord.ChordBase "music21.chord.ChordBase")
* [`NotRest`](moduleNote.html#music21.note.NotRest "music21.note.NotRest")
* [`GeneralNote`](moduleNote.html#music21.note.GeneralNote "music21.note.GeneralNote")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`FretBoard`](#music21.tablature.FretBoard "music21.tablature.FretBoard")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`ChordWithFretBoard`](#music21.tablature.ChordWithFretBoard "music21.tablature.ChordWithFretBoard") read-only properties

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

[`ChordWithFretBoard`](#music21.tablature.ChordWithFretBoard "music21.tablature.ChordWithFretBoard") read/write properties

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

[`ChordWithFretBoard`](#music21.tablature.ChordWithFretBoard "music21.tablature.ChordWithFretBoard") methods

ChordWithFretBoard.getFretNotesFromFigure()[[source]](../_modules/music21/tablature.html#ChordWithFretBoard.getFretNotesFromFigure)
:   TODO:
    Given a chord with fret Figure, getFretNotesFromFigure returns each FretNote object
    within it.

Methods inherited from [`ChordSymbol`](moduleHarmony.html#music21.harmony.ChordSymbol "music21.harmony.ChordSymbol"):

|  |  |  |
| --- | --- | --- |
| * [`findFigure()`](moduleHarmony.html#music21.harmony.ChordSymbol.findFigure "music21.harmony.ChordSymbol.findFigure") | * [`inversionIsValid()`](moduleHarmony.html#music21.harmony.ChordSymbol.inversionIsValid "music21.harmony.ChordSymbol.inversionIsValid") | * [`transpose()`](moduleHarmony.html#music21.harmony.ChordSymbol.transpose "music21.harmony.ChordSymbol.transpose") |

Methods inherited from [`Harmony`](moduleHarmony.html#music21.harmony.Harmony "music21.harmony.Harmony"):

|  |  |  |
| --- | --- | --- |
| * [`addChordStepModification()`](moduleHarmony.html#music21.harmony.Harmony.addChordStepModification "music21.harmony.Harmony.addChordStepModification") | * [`getChordStepModifications()`](moduleHarmony.html#music21.harmony.Harmony.getChordStepModifications "music21.harmony.Harmony.getChordStepModifications") |  |

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

Methods inherited from [`FretBoard`](#music21.tablature.FretBoard "music21.tablature.FretBoard"):

|  |  |  |
| --- | --- | --- |
| * [`fretNotesLowestFirst()`](#music21.tablature.FretBoard.fretNotesLowestFirst "music21.tablature.FretBoard.fretNotesLowestFirst") | * [`getFretNoteByString()`](#music21.tablature.FretBoard.getFretNoteByString "music21.tablature.FretBoard.getFretNoteByString") | * [`getPitches()`](#music21.tablature.FretBoard.getPitches "music21.tablature.FretBoard.getPitches") |

[`ChordWithFretBoard`](#music21.tablature.ChordWithFretBoard "music21.tablature.ChordWithFretBoard") instance variables

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

## FirstFret

class music21.tablature.FirstFret(*fretNum*, *location='right'*)[[source]](../_modules/music21/tablature.html#FirstFret)
:   FirstFretInfo returns the information regarding the first fret utilized in a
    given chord position.

## FretBoard

class music21.tablature.FretBoard(*numStrings: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 6*, *fretNotes: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[FretNote](#music21.tablature.FretNote "music21.tablature.FretNote")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *displayFrets: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 4*)[[source]](../_modules/music21/tablature.html#FretBoard)
:   A FretBoard represents a displayed fretboard (i.e. used in chord symbols).
    To be displayed, a fretboard requires a tuning system, defined by the fretted instrument
    classes defined.

    ```python
    >>> fn1 = tablature.FretNote(string=3, fret=2, fingering=1)
    >>> fn2 = tablature.FretNote(string=2, fret=3, fingering=3)
    >>> fn3 = tablature.FretNote(string=1, fret=2, fingering=2)
    >>> fb = tablature.FretBoard(6, fretNotes=[fn1, fn2, fn3], displayFrets=5)
    >>> fb.numStrings
    6
    >>> fb
    <music21.tablature.FretBoard 6 strings, 3 notes, 5 frets>
    >>> len(fb.fretNotes)
    3
    >>> fb.fretNotes[0]
    <music21.tablature.FretNote 3rd string, 2nd fret, 1st finger>
    ```

    ```python
    >>> fb.getFretNoteByString(2)
    <music21.tablature.FretNote 2nd string, 3rd fret, 3rd finger>
    ```

[`FretBoard`](#music21.tablature.FretBoard "music21.tablature.FretBoard") bases

* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`FretBoard`](#music21.tablature.FretBoard "music21.tablature.FretBoard") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`FretBoard`](#music21.tablature.FretBoard "music21.tablature.FretBoard") methods

FretBoard.fretNotesLowestFirst()[[source]](../_modules/music21/tablature.html#FretBoard.fretNotesLowestFirst)
:   Returns a list of FretNotes in lowest to highest string order.

    ```python
    >>> firstNote = tablature.FretNote(string=2, fret=3, fingering=4)
    >>> secondNote = tablature.FretNote(string=3, fret=3, fingering=3)
    >>> thirdNote = tablature.FretNote(string=1, fret=3, fingering=3)
    >>> myFretBoard = tablature.FretBoard(6, fretNotes=[firstNote, secondNote, thirdNote])
    >>> for thisFretNote in myFretBoard.fretNotesLowestFirst():
    ...    print(thisFretNote)
    <music21.tablature.FretNote 3rd string, 3rd fret, 3rd finger>
    <music21.tablature.FretNote 2nd string, 3rd fret, 4th finger>
    <music21.tablature.FretNote 1st string, 3rd fret, 3rd finger>
    ```

FretBoard.getFretNoteByString(*requestedString*)[[source]](../_modules/music21/tablature.html#FretBoard.getFretNoteByString)
:   Returns FretNote object on a given string or None if there are none.

    ```python
    >>> firstNote = tablature.FretNote(string=6, fret=3, fingering=4)
    >>> secondNote = tablature.FretNote(string=2, fret=3, fingering=3)
    >>> myFretBoard = tablature.FretBoard(6, fretNotes=[firstNote, secondNote])
    >>> myFretBoard.getFretNoteByString(6)
    <music21.tablature.FretNote 6th string, 3rd fret, 4th finger>
    ```

    ```python
    >>> myFretBoard.getFretNoteByString(2)
    <music21.tablature.FretNote 2nd string, 3rd fret, 3rd finger>
    ```

    ```python
    >>> myFretBoard.getFretNoteByString(9) is None
    True
    ```

FretBoard.getPitches() → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")][[source]](../_modules/music21/tablature.html#FretBoard.getPitches)
:   Returns a list of all the pitches (or None for each) given the FretNote information. This
    requires a tuning to be set.

    ```python
    >>> firstNote = tablature.FretNote(string=4, fret=3, fingering=3)
    >>> secondNote = tablature.FretNote(string=2, fret=1, fingering=1)
    >>> gfb = tablature.GuitarFretBoard(fretNotes=[firstNote, secondNote])
    >>> gfb.getPitches()
    [None, None, <music21.pitch.Pitch F3>, None, <music21.pitch.Pitch C4>, None]
    ```

    What if the User provides an empty FretBoard?
    >>> gfb2 = tablature.GuitarFretBoard(fretNotes=[])
    >>> gfb2.getPitches()
    [None, None, None, None, None, None]

    Works for other stringed instruments, as long as the tuning is included (see below).

    ```python
    >>> tablature.UkeleleFretBoard().numStrings
    4
    >>> uke = tablature.UkeleleFretBoard(fretNotes=[firstNote, secondNote])
    >>> uke.getPitches()
    [<music21.pitch.Pitch B-4>, None, <music21.pitch.Pitch F4>, None]
    ```

## FretNote

class music21.tablature.FretNote(*string: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *fret: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *fingering: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](../_modules/music21/tablature.html#FretNote)
:   A FretNote represents a note on a Fretboard, where each string should
    be fingered (or not).

    ```python
    >>> fn = tablature.FretNote(3, 4, 1)
    >>> fn
    <music21.tablature.FretNote 3rd string, 4th fret, 1st finger>
    ```

    ```python
    >>> fn.string
    3
    >>> fn.fret
    4
    >>> fn.fingering
    1
    >>> fn.displayFingerNumber
    True
    ```

    ```python
    >>> fnUnknownFinger = tablature.FretNote(1, 1)
    >>> fnUnknownFinger.fingering is None
    True
    ```

[`FretNote`](#music21.tablature.FretNote "music21.tablature.FretNote") bases

* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`FretNote`](#music21.tablature.FretNote "music21.tablature.FretNote") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

## GuitarFretBoard

class music21.tablature.GuitarFretBoard(*fretNotes=None*, *displayFrets=4*)[[source]](../_modules/music21/tablature.html#GuitarFretBoard)
:   A six-string fretboard tuned to E A D G B E.

[`GuitarFretBoard`](#music21.tablature.GuitarFretBoard "music21.tablature.GuitarFretBoard") bases

* [`FretBoard`](#music21.tablature.FretBoard "music21.tablature.FretBoard")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`GuitarFretBoard`](#music21.tablature.GuitarFretBoard "music21.tablature.GuitarFretBoard") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`GuitarFretBoard`](#music21.tablature.GuitarFretBoard "music21.tablature.GuitarFretBoard") methods

Methods inherited from [`FretBoard`](#music21.tablature.FretBoard "music21.tablature.FretBoard"):

|  |  |  |
| --- | --- | --- |
| * [`fretNotesLowestFirst()`](#music21.tablature.FretBoard.fretNotesLowestFirst "music21.tablature.FretBoard.fretNotesLowestFirst") | * [`getFretNoteByString()`](#music21.tablature.FretBoard.getFretNoteByString "music21.tablature.FretBoard.getFretNoteByString") | * [`getPitches()`](#music21.tablature.FretBoard.getPitches "music21.tablature.FretBoard.getPitches") |

## MandolinFretBoard

class music21.tablature.MandolinFretBoard(*fretNotes=None*, *displayFrets=4*)[[source]](../_modules/music21/tablature.html#MandolinFretBoard)
:   A four-string fretboard tuned to G D A E

[`MandolinFretBoard`](#music21.tablature.MandolinFretBoard "music21.tablature.MandolinFretBoard") bases

* [`FretBoard`](#music21.tablature.FretBoard "music21.tablature.FretBoard")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`MandolinFretBoard`](#music21.tablature.MandolinFretBoard "music21.tablature.MandolinFretBoard") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`MandolinFretBoard`](#music21.tablature.MandolinFretBoard "music21.tablature.MandolinFretBoard") methods

Methods inherited from [`FretBoard`](#music21.tablature.FretBoard "music21.tablature.FretBoard"):

|  |  |  |
| --- | --- | --- |
| * [`fretNotesLowestFirst()`](#music21.tablature.FretBoard.fretNotesLowestFirst "music21.tablature.FretBoard.fretNotesLowestFirst") | * [`getFretNoteByString()`](#music21.tablature.FretBoard.getFretNoteByString "music21.tablature.FretBoard.getFretNoteByString") | * [`getPitches()`](#music21.tablature.FretBoard.getPitches "music21.tablature.FretBoard.getPitches") |

## UkeleleFretBoard

class music21.tablature.UkeleleFretBoard(*fretNotes=None*, *displayFrets=4*)[[source]](../_modules/music21/tablature.html#UkeleleFretBoard)
:   A four-string fretboard tuned to G C E A

[`UkeleleFretBoard`](#music21.tablature.UkeleleFretBoard "music21.tablature.UkeleleFretBoard") bases

* [`FretBoard`](#music21.tablature.FretBoard "music21.tablature.FretBoard")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`UkeleleFretBoard`](#music21.tablature.UkeleleFretBoard "music21.tablature.UkeleleFretBoard") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`UkeleleFretBoard`](#music21.tablature.UkeleleFretBoard "music21.tablature.UkeleleFretBoard") methods

Methods inherited from [`FretBoard`](#music21.tablature.FretBoard "music21.tablature.FretBoard"):

|  |  |  |
| --- | --- | --- |
| * [`fretNotesLowestFirst()`](#music21.tablature.FretBoard.fretNotesLowestFirst "music21.tablature.FretBoard.fretNotesLowestFirst") | * [`getFretNoteByString()`](#music21.tablature.FretBoard.getFretNoteByString "music21.tablature.FretBoard.getFretNoteByString") | * [`getPitches()`](#music21.tablature.FretBoard.getPitches "music21.tablature.FretBoard.getPitches") |
