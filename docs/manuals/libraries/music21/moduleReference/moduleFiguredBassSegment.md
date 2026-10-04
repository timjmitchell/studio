Source: https://music21.org/music21docs/moduleReference/moduleFiguredBassSegment.html

# music21.figuredBass.segment

## OverlaidSegment

class music21.figuredBass.segment.OverlaidSegment(*bassNote: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Note](moduleNote.html#music21.note.Note "music21.note.Note") = 'C3'*, *notationString: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *fbScale: [FiguredBassScale](moduleFiguredBassRealizerScale.html#music21.figuredBass.realizerScale.FiguredBassScale "music21.figuredBass.realizerScale.FiguredBassScale") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *fbRules: [Rules](moduleFiguredBassRules.html#music21.figuredBass.rules.Rules "music21.figuredBass.rules.Rules") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *numParts=4*, *maxPitch: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") = 'B5'*, *listOfPitches=None*)[[source]](../_modules/music21/figuredBass/segment.html#OverlaidSegment)
:   Class to allow Segments to be overlaid with non-chord notes.

[`OverlaidSegment`](#music21.figuredBass.segment.OverlaidSegment "music21.figuredBass.segment.OverlaidSegment") bases

* [`Segment`](#music21.figuredBass.segment.Segment "music21.figuredBass.segment.Segment")

[`OverlaidSegment`](#music21.figuredBass.segment.OverlaidSegment "music21.figuredBass.segment.OverlaidSegment") methods

OverlaidSegment.allSinglePossibilities()[[source]](../_modules/music21/figuredBass/segment.html#OverlaidSegment.allSinglePossibilities)
:   Returns an iterator through a set of naive possibilities for
    a Segment, using [`numParts`](#music21.figuredBass.segment.Segment.numParts "music21.figuredBass.segment.Segment.numParts"),
    the pitch of [`bassNote`](#music21.figuredBass.segment.Segment.bassNote "music21.figuredBass.segment.Segment.bassNote"), and
    [`allPitchesAboveBass`](#music21.figuredBass.segment.Segment.allPitchesAboveBass "music21.figuredBass.segment.Segment.allPitchesAboveBass").

    ```python
    >>> from music21.figuredBass import segment
    >>> segmentA = segment.Segment()
    >>> allPossib = segmentA.allSinglePossibilities()
    >>> allPossib.__class__
    <... 'itertools.product'>
    ```

    The number of naive possibilities is always the length of
    [`allPitchesAboveBass`](#music21.figuredBass.segment.Segment.allPitchesAboveBass "music21.figuredBass.segment.Segment.allPitchesAboveBass")
    raised to the ([`numParts`](#music21.figuredBass.segment.Segment.numParts "music21.figuredBass.segment.Segment.numParts") - 1)
    power. The power is 1 less than the number of parts because
    the bass pitch is constant.

    ```python
    >>> allPossibList = list(allPossib)
    >>> len(segmentA.allPitchesAboveBass)
    9
    >>> segmentA.numParts
    4
    >>> len(segmentA.allPitchesAboveBass) ** (segmentA.numParts-1)
    729
    >>> len(allPossibList)
    729
    ```

    ```python
    >>> for i in (81, 275, 426):
    ...    [str(p) for p in allPossibList[i]]
    ['E3', 'C3', 'C3', 'C3']
    ['C4', 'C4', 'G4', 'C3']
    ['G4', 'G3', 'C4', 'C3']
    ```

Methods inherited from [`Segment`](#music21.figuredBass.segment.Segment "music21.figuredBass.segment.Segment"):

|  |  |  |
| --- | --- | --- |
| * [`allCorrectConsecutivePossibilities()`](#music21.figuredBass.segment.Segment.allCorrectConsecutivePossibilities "music21.figuredBass.segment.Segment.allCorrectConsecutivePossibilities") * [`allCorrectSinglePossibilities()`](#music21.figuredBass.segment.Segment.allCorrectSinglePossibilities "music21.figuredBass.segment.Segment.allCorrectSinglePossibilities") * [`consecutivePossibilityRules()`](#music21.figuredBass.segment.Segment.consecutivePossibilityRules "music21.figuredBass.segment.Segment.consecutivePossibilityRules") | * [`resolveAugmentedSixthSegment()`](#music21.figuredBass.segment.Segment.resolveAugmentedSixthSegment "music21.figuredBass.segment.Segment.resolveAugmentedSixthSegment") * [`resolveDiminishedSeventhSegment()`](#music21.figuredBass.segment.Segment.resolveDiminishedSeventhSegment "music21.figuredBass.segment.Segment.resolveDiminishedSeventhSegment") * [`resolveDominantSeventhSegment()`](#music21.figuredBass.segment.Segment.resolveDominantSeventhSegment "music21.figuredBass.segment.Segment.resolveDominantSeventhSegment") | * [`singlePossibilityRules()`](#music21.figuredBass.segment.Segment.singlePossibilityRules "music21.figuredBass.segment.Segment.singlePossibilityRules") * [`specialResolutionRules()`](#music21.figuredBass.segment.Segment.specialResolutionRules "music21.figuredBass.segment.Segment.specialResolutionRules") |

[`OverlaidSegment`](#music21.figuredBass.segment.OverlaidSegment "music21.figuredBass.segment.OverlaidSegment") instance variables

Instance variables inherited from [`Segment`](#music21.figuredBass.segment.Segment "music21.figuredBass.segment.Segment"):

|  |  |  |
| --- | --- | --- |
| * [`allPitchesAboveBass`](#music21.figuredBass.segment.Segment.allPitchesAboveBass "music21.figuredBass.segment.Segment.allPitchesAboveBass") * [`bassNote`](#music21.figuredBass.segment.Segment.bassNote "music21.figuredBass.segment.Segment.bassNote") | * [`fbRules`](#music21.figuredBass.segment.Segment.fbRules "music21.figuredBass.segment.Segment.fbRules") * [`numParts`](#music21.figuredBass.segment.Segment.numParts "music21.figuredBass.segment.Segment.numParts") | * [`pitchNamesInChord`](#music21.figuredBass.segment.Segment.pitchNamesInChord "music21.figuredBass.segment.Segment.pitchNamesInChord") * [`segmentChord`](#music21.figuredBass.segment.Segment.segmentChord "music21.figuredBass.segment.Segment.segmentChord") |

## Segment

class music21.figuredBass.segment.Segment(*bassNote: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Note](moduleNote.html#music21.note.Note "music21.note.Note") = 'C3'*, *notationString: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *fbScale: [FiguredBassScale](moduleFiguredBassRealizerScale.html#music21.figuredBass.realizerScale.FiguredBassScale "music21.figuredBass.realizerScale.FiguredBassScale") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *fbRules: [Rules](moduleFiguredBassRules.html#music21.figuredBass.rules.Rules "music21.figuredBass.rules.Rules") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *numParts=4*, *maxPitch: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") = 'B5'*, *listOfPitches=None*)[[source]](../_modules/music21/figuredBass/segment.html#Segment)

[`Segment`](#music21.figuredBass.segment.Segment "music21.figuredBass.segment.Segment") methods

Segment.allCorrectConsecutivePossibilities(*segmentB*)[[source]](../_modules/music21/figuredBass/segment.html#Segment.allCorrectConsecutivePossibilities)
:   Returns an iterator through correct (possibA, possibB) pairs.

    * If segmentA (self) is a special Segment, meaning that one of the Segment
      resolution methods in [`specialResolutionRules()`](#music21.figuredBass.segment.Segment.specialResolutionRules "music21.figuredBass.segment.Segment.specialResolutionRules")
      needs to be applied, then this method returns every correct possibility of segmentA
      matched up with exactly one resolution possibility.
    * If segmentA is an ordinary, non-special Segment, then this method returns every
      combination of correct possibilities of segmentA and correct possibilities of segmentB
      which passes all filters
      in [`consecutivePossibilityRules()`](#music21.figuredBass.segment.Segment.consecutivePossibilityRules "music21.figuredBass.segment.Segment.consecutivePossibilityRules").

    Two notes on segmentA being a special Segment:

    1. By default, resolution possibilities are not filtered
       using [`singlePossibilityRules()`](#music21.figuredBass.segment.Segment.singlePossibilityRules "music21.figuredBass.segment.Segment.singlePossibilityRules")
       rules of segmentB. Filter by setting
       [`applySinglePossibRulesToResolution`](moduleFiguredBassRules.html#music21.figuredBass.rules.Rules.applySinglePossibRulesToResolution "music21.figuredBass.rules.Rules.applySinglePossibRulesToResolution") to True.
    2. By default, (possibA, possibB) pairs are not filtered
       using [`consecutivePossibilityRules()`](#music21.figuredBass.segment.Segment.consecutivePossibilityRules "music21.figuredBass.segment.Segment.consecutivePossibilityRules")
       rules of segmentA. Filter by setting
       [`applyConsecutivePossibRulesToResolution`](moduleFiguredBassRules.html#music21.figuredBass.rules.Rules.applyConsecutivePossibRulesToResolution "music21.figuredBass.rules.Rules.applyConsecutivePossibRulesToResolution")
       to True.

    ```python
    >>> from music21.figuredBass import segment
    >>> segmentA = segment.Segment(bassNote=note.Note('C3'), notationString='')
    >>> segmentB = segment.Segment(bassNote=note.Note('D3'), notationString='4,3')
    ```

    Here, an ordinary resolution is being executed, because segmentA is an ordinary Segment.

    ```python
    >>> consecutivePairs1 = segmentA.allCorrectConsecutivePossibilities(segmentB)
    >>> consecutivePairsList1 = list(consecutivePairs1)
    >>> len(consecutivePairsList1)
    31
    >>> consecutivePairsList1[29]
    ((<...G5>, <...G5>, <...E5>, <...C3>), (<...G5>, <...F5>, <...B4>, <...D3>))
    ```

    Here, a special resolution is being executed, because segmentA below is a
    special Segment.

    ```python
    >>> segmentA = segment.Segment(bassNote=note.Note('D3'), notationString='4,3')
    >>> segmentB = segment.Segment(bassNote=note.Note('C3'), notationString='')
    >>> consecutivePairs2 = segmentA.allCorrectConsecutivePossibilities(segmentB)
    >>> consecutivePairsList2 = list(consecutivePairs2)
    >>> len(consecutivePairsList2)
    6
    >>> consecutivePairsList2[5]
    ((<...G5>, <...F5>, <...B4>, <...D3>), (<...G5>, <...E5>, <...C5>, <...C3>))
    ```

Segment.allCorrectSinglePossibilities()[[source]](../_modules/music21/figuredBass/segment.html#Segment.allCorrectSinglePossibilities)
:   Uses [`allSinglePossibilities()`](#music21.figuredBass.segment.Segment.allSinglePossibilities "music21.figuredBass.segment.Segment.allSinglePossibilities") and
    returns an iterator through a set of correct possibilities for
    a Segment, all possibilities which pass all filters in
    [`singlePossibilityRules()`](#music21.figuredBass.segment.Segment.singlePossibilityRules "music21.figuredBass.segment.Segment.singlePossibilityRules").

    ```python
    >>> from music21.figuredBass import segment
    >>> segmentA = segment.Segment()
    >>> allPossib = segmentA.allSinglePossibilities()
    >>> allCorrectPossib = segmentA.allCorrectSinglePossibilities()
    ```

    Most of the 729 naive possibilities were filtered out using the default rules set,
    leaving only 21.

    ```python
    >>> allPossibList = list(allPossib)
    >>> len(allPossibList)
    729
    >>> allCorrectPossibList = list(allCorrectPossib)
    >>> len(allCorrectPossibList)
    21
    ```

    ```python
    >>> for i in (5, 12, 20):
    ...   [str(p) for p in allCorrectPossibList[i]]
    ['E4', 'G3', 'G3', 'C3']
    ['C5', 'G4', 'E4', 'C3']
    ['G5', 'G5', 'E5', 'C3']
    ```

Segment.allSinglePossibilities()[[source]](../_modules/music21/figuredBass/segment.html#Segment.allSinglePossibilities)
:   Returns an iterator through a set of naive possibilities for
    a Segment, using [`numParts`](#music21.figuredBass.segment.Segment.numParts "music21.figuredBass.segment.Segment.numParts"),
    the pitch of [`bassNote`](#music21.figuredBass.segment.Segment.bassNote "music21.figuredBass.segment.Segment.bassNote"), and
    [`allPitchesAboveBass`](#music21.figuredBass.segment.Segment.allPitchesAboveBass "music21.figuredBass.segment.Segment.allPitchesAboveBass").

    ```python
    >>> from music21.figuredBass import segment
    >>> segmentA = segment.Segment()
    >>> allPossib = segmentA.allSinglePossibilities()
    >>> allPossib.__class__
    <... 'itertools.product'>
    ```

    The number of naive possibilities is always the length of
    [`allPitchesAboveBass`](#music21.figuredBass.segment.Segment.allPitchesAboveBass "music21.figuredBass.segment.Segment.allPitchesAboveBass")
    raised to the ([`numParts`](#music21.figuredBass.segment.Segment.numParts "music21.figuredBass.segment.Segment.numParts") - 1)
    power. The power is 1 less than the number of parts because
    the bass pitch is constant.

    ```python
    >>> allPossibList = list(allPossib)
    >>> len(segmentA.allPitchesAboveBass)
    9
    >>> segmentA.numParts
    4
    >>> len(segmentA.allPitchesAboveBass) ** (segmentA.numParts-1)
    729
    >>> len(allPossibList)
    729
    ```

    ```python
    >>> for i in (81, 275, 426):
    ...    [str(p) for p in allPossibList[i]]
    ['E3', 'C3', 'C3', 'C3']
    ['C4', 'C4', 'G4', 'C3']
    ['G4', 'G3', 'C4', 'C3']
    ```

Segment.consecutivePossibilityRules(*fbRules=None*)[[source]](../_modules/music21/figuredBass/segment.html#Segment.consecutivePossibilityRules)
:   A framework for storing consecutive possibility rules and methods to be applied
    in [`allCorrectConsecutivePossibilities()`](#music21.figuredBass.segment.Segment.allCorrectConsecutivePossibilities "music21.figuredBass.segment.Segment.allCorrectConsecutivePossibilities").
    Takes in a [`Rules`](moduleFiguredBassRules.html#music21.figuredBass.rules.Rules "music21.figuredBass.rules.Rules") object, fbRules; if None
    then a new rules.Rules() object is created.

    Items are added within this method in the following form:

    > (willRunOnlyIfTrue, methodToRun, keepSolutionsWhichReturn, optionalArgs)

    These items are compiled internally when
    [`allCorrectConsecutivePossibilities()`](#music21.figuredBass.segment.Segment.allCorrectConsecutivePossibilities "music21.figuredBass.segment.Segment.allCorrectConsecutivePossibilities")
    is called on a Segment. Here, the compilation of rules and methods
    bases on a default fbRules is shown.

    ```python
    >>> from music21.figuredBass import segment
    >>> segmentA = segment.Segment()
    >>> allConsecutiveRules = segmentA.consecutivePossibilityRules()
    ```

    ```python
    >>> segment.printRules(allConsecutiveRules)
    Will run:  Method:                       Keep solutions which return:  Arguments:
    True       partsSame                     True                          []
    False      upperPartsSame                True                          None
    True       voiceOverlap                  False                         None
    True       partMovementsWithinLimits     True                          []
    True       parallelFifths                False                         None
    True       parallelOctaves               False                         None
    True       hiddenFifth                   False                         None
    True       hiddenOctave                  False                         None
    False      couldBeItalianA6Resolution    True           [<music21.pitch.Pitch C3>,
                                                             <music21.pitch.Pitch C3>,
                                                             <music21.pitch.Pitch E3>,
                                                             <music21.pitch.Pitch G3>], True
    ```

    Now, a modified fbRules is provided, allowing hidden octaves and
    voice overlap, and limiting the soprano line to stepwise motion.

    ```python
    >>> from music21.figuredBass import rules
    >>> fbRules = rules.Rules()
    >>> fbRules.forbidVoiceOverlap = False
    >>> fbRules.forbidHiddenOctaves = False
    >>> fbRules.partMovementLimits.append((1, 2))
    >>> allConsecutiveRules = segmentA.consecutivePossibilityRules(fbRules)
    >>> segment.printRules(allConsecutiveRules)
    Will run:  Method:                       Keep solutions which return:  Arguments:
    True       partsSame                     True                          []
    False      upperPartsSame                True                          None
    False      voiceOverlap                  False                         None
    True       partMovementsWithinLimits     True                          [(1, 2)]
    True       parallelFifths                False                         None
    True       parallelOctaves               False                         None
    True       hiddenFifth                   False                         None
    False      hiddenOctave                  False                         None
    False      couldBeItalianA6Resolution    True           [<music21.pitch.Pitch C3>,
                                                             <music21.pitch.Pitch C3>,
                                                             <music21.pitch.Pitch E3>,
                                                             <music21.pitch.Pitch G3>], True
    ```

Segment.resolveAugmentedSixthSegment(*segmentB*)[[source]](../_modules/music21/figuredBass/segment.html#Segment.resolveAugmentedSixthSegment)
:   Can resolve a Segment whose [`segmentChord`](#music21.figuredBass.segment.Segment.segmentChord "music21.figuredBass.segment.Segment.segmentChord")
    spells out a
    French, German, or Swiss augmented sixth chord. Italian augmented sixth Segments
    are solved as an
    ordinary Segment using [`couldBeItalianA6Resolution()`](moduleFiguredBassPossibility.html#music21.figuredBass.possibility.couldBeItalianA6Resolution "music21.figuredBass.possibility.couldBeItalianA6Resolution").
    If no
    applicable method in [`resolution`](moduleFiguredBassResolution.html#module-music21.figuredBass.resolution "music21.figuredBass.resolution") can be used, the Segment
    is resolved
    as an ordinary Segment.

    ```python
    >>> from music21.figuredBass import segment
    >>> segmentA = segment.Segment(bassNote=note.Note('A-2'), notationString='#6,b5,3')
    >>> segmentA.pitchNamesInChord  # spell out a Gr+6 chord
    ['A-', 'C', 'E-', 'F#']
    >>> allAugSixthPossib = segmentA.allCorrectSinglePossibilities()
    >>> allAugSixthPossibList = list(allAugSixthPossib)
    >>> len(allAugSixthPossibList)
    7
    ```

    ```python
    >>> allAugSixthPossibList[1]
    (<music21.pitch.Pitch C4>, <music21.pitch.Pitch F#3>, <...E-3>, <...A-2>)
    >>> allAugSixthPossibList[4]
    (<music21.pitch.Pitch C5>, <music21.pitch.Pitch F#4>, <...E-4>, <...A-2>)
    ```

    ```python
    >>> segmentB = segment.Segment(bassNote=note.Note('G2'), notationString='')
    >>> allAugResPossibPairs = segmentA.resolveAugmentedSixthSegment(segmentB)
    >>> allAugResPossibPairsList = list(allAugResPossibPairs)
    >>> len(allAugResPossibPairsList)
    7
    >>> allAugResPossibPairsList[1]
    ((<...C4>, <...F#3>, <...E-3>, <...A-2>), (<...B3>, <...G3>, <...D3>, <...G2>))
    >>> allAugResPossibPairsList[4]
    ((<...C5>, <...F#4>, <...E-4>, <...A-2>), (<...B4>, <...G4>, <...D4>, <...G2>))
    ```

Segment.resolveDiminishedSeventhSegment(*segmentB*, *doubledRoot=False*)[[source]](../_modules/music21/figuredBass/segment.html#Segment.resolveDiminishedSeventhSegment)
:   Can resolve a Segment whose [`segmentChord`](#music21.figuredBass.segment.Segment.segmentChord "music21.figuredBass.segment.Segment.segmentChord")
    spells out a diminished seventh chord. If no applicable method in
    [`resolution`](moduleFiguredBassResolution.html#module-music21.figuredBass.resolution "music21.figuredBass.resolution") can be used, the Segment is resolved
    as an ordinary Segment.

    ```python
    >>> from music21.figuredBass import segment
    >>> segmentA = segment.Segment(bassNote=note.Note('B2'), notationString='b7')
    >>> allDimPossib = segmentA.allCorrectSinglePossibilities()
    >>> allDimPossibList = list(allDimPossib)
    >>> len(allDimPossibList)
    7
    >>> [p.nameWithOctave for p in allDimPossibList[4]]
    ['D5', 'A-4', 'F4', 'B2']
    >>> [p.nameWithOctave for p in allDimPossibList[6]]
    ['A-5', 'F5', 'D5', 'B2']
    ```

    ```python
    >>> segmentB = segment.Segment(bassNote=note.Note('C3'), notationString='')
    >>> dimResPairs = segmentA.resolveDiminishedSeventhSegment(segmentB)
    >>> dimResPairsList = list(dimResPairs)
    >>> len(dimResPairsList)
    7
    >>> dimResPairsList[4]
    ((<...D5>, <...A-4>, <...F4>, <...B2>), (<...E5>, <...G4>, <...E4>, <...C3>))
    >>> dimResPairsList[6]
    ((<...A-5>, <...F5>, <...D5>, <...B2>), (<...G5>, <...E5>, <...E5>, <...C3>))
    ```

Segment.resolveDominantSeventhSegment(*segmentB*)[[source]](../_modules/music21/figuredBass/segment.html#Segment.resolveDominantSeventhSegment)
:   Can resolve a Segment whose [`segmentChord`](#music21.figuredBass.segment.Segment.segmentChord "music21.figuredBass.segment.Segment.segmentChord")
    spells out a dominant seventh chord. If no applicable method in
    [`resolution`](moduleFiguredBassResolution.html#module-music21.figuredBass.resolution "music21.figuredBass.resolution") can be used, the Segment is resolved
    as an ordinary Segment.

    ```python
    >>> from music21.figuredBass import segment
    >>> segmentA = segment.Segment(bassNote=note.Note('G2'), notationString='7')
    >>> allDomPossib = segmentA.allCorrectSinglePossibilities()
    >>> allDomPossibList = list(allDomPossib)
    >>> len(allDomPossibList)
    8
    >>> allDomPossibList[2]
    (<music21.pitch.Pitch D4>, <music21.pitch.Pitch B3>,
     <music21.pitch.Pitch F3>, <music21.pitch.Pitch G2>)
    >>> allDomPossibList[5]
    (<music21.pitch.Pitch D5>, <music21.pitch.Pitch B4>,
     <music21.pitch.Pitch F4>, <music21.pitch.Pitch G2>)
    ```

    Here, the Soprano pitch of resolution (C6) exceeds default maxPitch of B5, so
    it’s filtered out.

    ```python
    >>> [p.nameWithOctave for p in allDomPossibList[7]]
    ['B5', 'F5', 'D5', 'G2']
    ```

    ```python
    >>> segmentB = segment.Segment(bassNote=note.Note('C3'), notationString='')
    >>> domResPairs = segmentA.resolveDominantSeventhSegment(segmentB)
    >>> domResPairsList = list(domResPairs)
    >>> len(domResPairsList)
    7
    >>> domResPairsList[2]
    ((<music21.pitch.Pitch D4>, <...B3>, <...F3>, <...G2>),
     (<...C4>, <...C4>, <...E3>, <...C3>))
    >>> domResPairsList[5]
    ((<...D5>, <...B4>, <...F4>, <...G2>), (<...C5>, <...C5>, <...E4>, <...C3>))
    ```

Segment.singlePossibilityRules(*fbRules=None*)[[source]](../_modules/music21/figuredBass/segment.html#Segment.singlePossibilityRules)
:   A framework for storing single possibility rules and methods to be applied
    in [`allCorrectSinglePossibilities()`](#music21.figuredBass.segment.Segment.allCorrectSinglePossibilities "music21.figuredBass.segment.Segment.allCorrectSinglePossibilities").
    Takes in a [`Rules`](moduleFiguredBassRules.html#music21.figuredBass.rules.Rules "music21.figuredBass.rules.Rules") object, fbRules.
    If None then a new rules object is created.

    Items are added within this method in the following form:

    (willRunOnlyIfTrue, methodToRun, keepSolutionsWhichReturn, optionalArgs)

    These items are compiled internally when
    [`allCorrectSinglePossibilities()`](#music21.figuredBass.segment.Segment.allCorrectSinglePossibilities "music21.figuredBass.segment.Segment.allCorrectSinglePossibilities")
    is called on a Segment. Here, the compilation of rules and
    methods bases on a default fbRules is shown.

    ```python
    >>> from music21.figuredBass import segment
    >>> segmentA = segment.Segment()
    >>> allSingleRules = segmentA.singlePossibilityRules()
    >>> segment.printRules(allSingleRules)
    Will run:  Method:                       Keep solutions which return:  Arguments:
    True       isIncomplete                  False                         ['C', 'E', 'G']
    True       upperPartsWithinLimit         True                          12
    True       voiceCrossing                 False                         None
    ```

    Here, a modified fbRules is provided, which allows for incomplete possibilities.

    ```python
    >>> from music21.figuredBass import rules
    >>> fbRules = rules.Rules()
    >>> fbRules.forbidIncompletePossibilities = False
    >>> allSingleRules = segmentA.singlePossibilityRules(fbRules)
    >>> segment.printRules(allSingleRules)
    Will run:  Method:                       Keep solutions which return:  Arguments:
    False      isIncomplete                  False                         ['C', 'E', 'G']
    True       upperPartsWithinLimit         True                          12
    True       voiceCrossing                 False                         None
    ```

Segment.specialResolutionRules(*fbRules=None*)[[source]](../_modules/music21/figuredBass/segment.html#Segment.specialResolutionRules)
:   A framework for storing methods which perform special resolutions
    on Segments. Unlike the methods in
    [`singlePossibilityRules()`](#music21.figuredBass.segment.Segment.singlePossibilityRules "music21.figuredBass.segment.Segment.singlePossibilityRules") and
    [`consecutivePossibilityRules()`](#music21.figuredBass.segment.Segment.consecutivePossibilityRules "music21.figuredBass.segment.Segment.consecutivePossibilityRules"),
    these methods deal with the Segment itself, and rely on submethods
    to resolve the individual possibilities accordingly depending on what
    the resolution Segment is.

    If fbRules is None, then a new rules.Rules() object is created.

    Items are added within this method in the following form:

    (willRunOnlyIfTrue, methodToRun, optionalArgs)

    These items are compiled internally
    when [`allCorrectConsecutivePossibilities()`](#music21.figuredBass.segment.Segment.allCorrectConsecutivePossibilities "music21.figuredBass.segment.Segment.allCorrectConsecutivePossibilities")
    is called on a Segment. Here, the compilation of rules and methods
    based on a default fbRules is shown.

    ```python
    >>> from music21.figuredBass import segment
    >>> segmentA = segment.Segment()
    >>> allSpecialResRules = segmentA.specialResolutionRules()
    >>> segment.printRules(allSpecialResRules, maxLength=3)
    Will run:  Method:                          Arguments:
    False      resolveDominantSeventhSegment    None
    False      resolveDiminishedSeventhSegment  False
    False      resolveAugmentedSixthSegment     None
    ```

    Dominant Seventh Segment:

    ```python
    >>> segmentA = segment.Segment(bassNote=note.Note('B2'), notationString='6,5')
    >>> allSpecialResRules = segmentA.specialResolutionRules()
    >>> segment.printRules(allSpecialResRules, maxLength=3)
    Will run:  Method:                          Arguments:
    True       resolveDominantSeventhSegment    None
    False      resolveDiminishedSeventhSegment  False
    False      resolveAugmentedSixthSegment     None
    ```

    Fully-Diminished Seventh Segment:

    ```python
    >>> segmentA = segment.Segment(bassNote=note.Note('B2'), notationString='-7')
    >>> allSpecialResRules = segmentA.specialResolutionRules()
    >>> segment.printRules(allSpecialResRules, maxLength=3)
    Will run:  Method:                          Arguments:
    False      resolveDominantSeventhSegment    None
    True       resolveDiminishedSeventhSegment  False
    False      resolveAugmentedSixthSegment     None
    ```

    Augmented Sixth Segment:

    ```python
    >>> segmentA = segment.Segment(bassNote=note.Note('A-2'), notationString='#6,b5')
    >>> allSpecialResRules = segmentA.specialResolutionRules()
    >>> segment.printRules(allSpecialResRules, maxLength=3)
    Will run:  Method:                          Arguments:
    False      resolveDominantSeventhSegment    None
    False      resolveDiminishedSeventhSegment  False
    True       resolveAugmentedSixthSegment     None
    ```

[`Segment`](#music21.figuredBass.segment.Segment "music21.figuredBass.segment.Segment") instance variables

Segment.allPitchesAboveBass
:   A list of allowable pitches in the upper parts of a possibility.
    This is derived using
    [`getPitches()`](#music21.figuredBass.segment.getPitches "music21.figuredBass.segment.getPitches"), providing bassNote.pitch,
    `maxPitch`
    from the Rules object, and
    [`pitchNamesInChord`](#music21.figuredBass.segment.Segment.pitchNamesInChord "music21.figuredBass.segment.Segment.pitchNamesInChord") as arguments.

Segment.bassNote
:   A [`Note`](moduleNote.html#music21.note.Note "music21.note.Note") whose pitch
    forms the bass of each possibility.

Segment.fbRules
:   A deepcopy of the [`Rules`](moduleFiguredBassRules.html#music21.figuredBass.rules.Rules "music21.figuredBass.rules.Rules") object provided.

Segment.numParts
:   The number of parts (including the bass) that possibilities
    should contain, which
    comes directly from `numParts`
    in the Rules object.

Segment.pitchNamesInChord
:   A list of allowable pitch names.
    This is derived from bassNote.pitch and notationString
    using [`getPitchNames()`](moduleFiguredBassRealizerScale.html#music21.figuredBass.realizerScale.FiguredBassScale.getPitchNames "music21.figuredBass.realizerScale.FiguredBassScale.getPitchNames").

Segment.segmentChord
:   [`allPitchesAboveBass`](#music21.figuredBass.segment.Segment.allPitchesAboveBass "music21.figuredBass.segment.Segment.allPitchesAboveBass")
    represented as a [`Chord`](moduleChord.html#music21.chord.Chord "music21.chord.Chord").

## Functions

music21.figuredBass.segment.getPitches(*pitchNames=('C', 'E', 'G')*, *bassPitch: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") = 'C3'*, *maxPitch: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") = 'C8'*)[[source]](../_modules/music21/figuredBass/segment.html#getPitches)
:   Given a list of pitchNames, a bassPitch, and a maxPitch, returns a sorted list of
    pitches between the two limits (inclusive) which correspond to items in pitchNames.

    ```python
    >>> from music21.figuredBass import segment
    >>> pitches = segment.getPitches()
    >>> print(', '.join([p.nameWithOctave for p in pitches]))
    C3, E3, G3, C4, E4, G4, C5, E5, G5, C6, E6, G6, C7, E7, G7, C8
    ```

    ```python
    >>> pitches = segment.getPitches(['G', 'B', 'D', 'F'], bassPitch=pitch.Pitch('B2'))
    >>> print(', '.join([p.nameWithOctave for p in pitches]))
    B2, D3, F3, G3, B3, D4, F4, G4, B4, D5, F5, G5, B5, D6, F6, G6, B6, D7, F7, G7, B7
    ```

    ```python
    >>> pitches = segment.getPitches(['F##', 'A#', 'C#'], bassPitch=pitch.Pitch('A#3'))
    >>> print(', '.join([p.nameWithOctave for p in pitches]))
    A#3, C#4, F##4, A#4, C#5, F##5, A#5, C#6, F##6, A#6, C#7, F##7, A#7
    ```

    The maxPitch must have an octave:

    ```python
    >>> segment.getPitches(maxPitch=pitch.Pitch('E'))
    Traceback (most recent call last):
    ValueError: maxPitch must be given an octave
    ```

music21.figuredBass.segment.printRules(*rulesList*, *maxLength=4*)[[source]](../_modules/music21/figuredBass/segment.html#printRules)
:   Method which can print to the console rules inputted into
    [`singlePossibilityRules()`](#music21.figuredBass.segment.Segment.singlePossibilityRules "music21.figuredBass.segment.Segment.singlePossibilityRules"),
    [`consecutivePossibilityRules()`](#music21.figuredBass.segment.Segment.consecutivePossibilityRules "music21.figuredBass.segment.Segment.consecutivePossibilityRules"), and
    [`specialResolutionRules()`](#music21.figuredBass.segment.Segment.specialResolutionRules "music21.figuredBass.segment.Segment.specialResolutionRules").
    For the first two methods, maxLength is 4. For the third method, maxLength is 3.
