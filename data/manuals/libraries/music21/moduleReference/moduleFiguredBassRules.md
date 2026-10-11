Source: https://music21.org/music21docs/moduleReference/moduleFiguredBassRules.html

# music21.figuredBass.rules

## Rules

class music21.figuredBass.rules.Rules[[source]](../_modules/music21/figuredBass/rules.html#Rules)
:   A Rules object is provided as an input to a [`Segment`](moduleFiguredBassSegment.html#music21.figuredBass.segment.Segment "music21.figuredBass.segment.Segment"),
    and controls the application of methods designed to filter out undesired possibilities in
    a single Segment or undesired progressions between two consecutive Segments.

    The rules are categorized in an identical manner to methods
    in [`possibility`](moduleFiguredBassPossibility.html#module-music21.figuredBass.possibility "music21.figuredBass.possibility"):

    1) Single Possibility Rules. These rules apply to any possibility within a
    single Segment (possibA), and
    are applied in finding correct possibilities for a Segment
    in [`allCorrectSinglePossibilities()`](moduleFiguredBassSegment.html#music21.figuredBass.segment.Segment.allCorrectSinglePossibilities "music21.figuredBass.segment.Segment.allCorrectSinglePossibilities").

    2) Consecutive Possibility Rules. These rules apply between any correct
    single possibility in segmentA
    (possibA) and any correct single possibility in segmentB (possibB),
    segmentB coming directly after segmentA.
    They are applied in finding correct (possibA, possibB) pairs between
    two Segments
    in [`allCorrectConsecutivePossibilities()`](moduleFiguredBassSegment.html#music21.figuredBass.segment.Segment.allCorrectConsecutivePossibilities "music21.figuredBass.segment.Segment.allCorrectConsecutivePossibilities").

    3) Special Resolution Rules. These rules apply to Segments
    whose [`segmentChord`](moduleFiguredBassSegment.html#music21.figuredBass.segment.Segment.segmentChord "music21.figuredBass.segment.Segment.segmentChord") is an
    augmented sixth, dominant seventh, or diminished seventh chord, and are
    applied as necessary in
    [`allCorrectConsecutivePossibilities()`](moduleFiguredBassSegment.html#music21.figuredBass.segment.Segment.allCorrectConsecutivePossibilities "music21.figuredBass.segment.Segment.allCorrectConsecutivePossibilities").

    ```python
    >>> from music21.figuredBass import rules
    >>> fbRules = rules.Rules()
    >>> fbRules
    <music21.figuredBass.rules.Rules>
    >>> fbRules.forbidParallelFifths = False
    >>> fbRules.upperPartsMaxSemitoneSeparation = None
    ```

[`Rules`](#music21.figuredBass.rules.Rules "music21.figuredBass.rules.Rules") bases

* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`Rules`](#music21.figuredBass.rules.Rules "music21.figuredBass.rules.Rules") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`Rules`](#music21.figuredBass.rules.Rules "music21.figuredBass.rules.Rules") instance variables

Rules.applyConsecutivePossibRulesToResolution
:   False by default. If True, consecutive possibility rules are applied
    between (specialPossib, resPossib) pairs.

Rules.applySinglePossibRulesToResolution
:   False by default. If True, single possibility rules are applied to
    resolution possibilities.

Rules.doubledRootInDim7
:   False by default. If True, Diminished seventh resolutions to the
    tonic will contain a doubled *root*, as opposed to a doubled *third*.
    Rule is ignored (determined in context)
    if [`segmentChord`](moduleFiguredBassSegment.html#music21.figuredBass.segment.Segment.segmentChord "music21.figuredBass.segment.Segment.segmentChord") is in first inversion.

Rules.forbidHiddenFifths
:   True by default. If True,
    [`hiddenFifth()`](moduleFiguredBassPossibility.html#music21.figuredBass.possibility.hiddenFifth "music21.figuredBass.possibility.hiddenFifth") is applied to all
    (possibA, possibB) pairs, and all those pairs for which the method returns
    False are retained.

Rules.forbidHiddenOctaves
:   True by default. If True,
    [`hiddenOctave()`](moduleFiguredBassPossibility.html#music21.figuredBass.possibility.hiddenOctave "music21.figuredBass.possibility.hiddenOctave") is applied to all
    (possibA, possibB) pairs, and all those pairs for which the method returns
    False are retained.

Rules.forbidIncompletePossibilities
:   True by default. If True,
    [`isIncomplete()`](moduleFiguredBassPossibility.html#music21.figuredBass.possibility.isIncomplete "music21.figuredBass.possibility.isIncomplete") is applied to all possibA,
    and all those possibilities for which the method returns False are retained.

Rules.forbidParallelFifths
:   True by default. If True,
    [`parallelFifths()`](moduleFiguredBassPossibility.html#music21.figuredBass.possibility.parallelFifths "music21.figuredBass.possibility.parallelFifths") is applied to all
    (possibA, possibB) pairs, and all those pairs for which the method returns
    False are retained.

Rules.forbidParallelOctaves
:   True by default. If True,
    [`parallelOctaves()`](moduleFiguredBassPossibility.html#music21.figuredBass.possibility.parallelOctaves "music21.figuredBass.possibility.parallelOctaves") is applied to all
    (possibA, possibB) pairs, and all those pairs for which the method returns
    False are retained.

Rules.forbidVoiceCrossing
:   True by default. If True,
    [`voiceCrossing()`](moduleFiguredBassPossibility.html#music21.figuredBass.possibility.voiceCrossing "music21.figuredBass.possibility.voiceCrossing") is applied to all possibA,
    and all those possibilities for which the method returns False are retained.

Rules.forbidVoiceOverlap
:   True by default. If True,
    [`voiceOverlap()`](moduleFiguredBassPossibility.html#music21.figuredBass.possibility.voiceOverlap "music21.figuredBass.possibility.voiceOverlap") is applied to all
    (possibA, possibB) pairs, and all those pairs for which the method returns
    False are retained.

Rules.partMovementLimits
:   [] (empty list) by default. Contains (partNumber, maxSeparation)
    pairs provided as arguments
    to [`partMovementsWithinLimits()`](moduleFiguredBassPossibility.html#music21.figuredBass.possibility.partMovementsWithinLimits "music21.figuredBass.possibility.partMovementsWithinLimits").
    Method is applied to all (possibA, possibB) pairs, and all those pairs
    for which the method returns True are retained.

Rules.resolveAugmentedSixthProperly
:   True by default. If True, Segments
    whose [`segmentChord`](moduleFiguredBassSegment.html#music21.figuredBass.segment.Segment.segmentChord "music21.figuredBass.segment.Segment.segmentChord") spells out an
    augmented sixth chord are resolved properly by
    using [`resolveAugmentedSixthSegment()`](moduleFiguredBassSegment.html#music21.figuredBass.segment.Segment.resolveAugmentedSixthSegment "music21.figuredBass.segment.Segment.resolveAugmentedSixthSegment").

Rules.resolveDiminishedSeventhProperly
:   True by default. If True, Segments
    whose [`segmentChord`](moduleFiguredBassSegment.html#music21.figuredBass.segment.Segment.segmentChord "music21.figuredBass.segment.Segment.segmentChord") spells out
    a fully-diminished seventh chord are resolved properly by
    using [`resolveDiminishedSeventhSegment()`](moduleFiguredBassSegment.html#music21.figuredBass.segment.Segment.resolveDiminishedSeventhSegment "music21.figuredBass.segment.Segment.resolveDiminishedSeventhSegment").

Rules.resolveDominantSeventhProperly
:   True by default. If True, Segments
    whose [`segmentChord`](moduleFiguredBassSegment.html#music21.figuredBass.segment.Segment.segmentChord "music21.figuredBass.segment.Segment.segmentChord") spells out a
    dominant seventh chord are resolved properly by
    using [`resolveDominantSeventhSegment()`](moduleFiguredBassSegment.html#music21.figuredBass.segment.Segment.resolveDominantSeventhSegment "music21.figuredBass.segment.Segment.resolveDominantSeventhSegment").

Rules.restrictDoublingsInItalianA6Resolution
:   True by default. If True, then doublings in the It+6 chord are limited to the
    tonic, or fifth. Setting this to False allows doubling of the root or third, most likely
    through parallel unisons if [`forbidParallelOctaves`](#music21.figuredBass.rules.Rules.forbidParallelOctaves "music21.figuredBass.rules.Rules.forbidParallelOctaves")
    is set to True.

Rules.upperPartsMaxSemitoneSeparation
:   12 by default. A number, in semitones,
    representing the maxSemitoneSeparation argument provided to
    [`upperPartsWithinLimit()`](moduleFiguredBassPossibility.html#music21.figuredBass.possibility.upperPartsWithinLimit "music21.figuredBass.possibility.upperPartsWithinLimit").
    Method is applied to all possibA, and all those possibilities for which the method returns
    True are retained.
