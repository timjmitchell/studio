Source: https://music21.org/music21docs/moduleReference/moduleAnalysisEnharmonics.html

# music21.analysis.enharmonics

## ChordEnharmonicScoreRules

class music21.analysis.enharmonics.ChordEnharmonicScoreRules[[source]](../_modules/music21/analysis/enharmonics.html#ChordEnharmonicScoreRules)

[`ChordEnharmonicScoreRules`](#music21.analysis.enharmonics.ChordEnharmonicScoreRules "music21.analysis.enharmonics.ChordEnharmonicScoreRules") bases

* [`EnharmonicScoreRules`](#music21.analysis.enharmonics.EnharmonicScoreRules "music21.analysis.enharmonics.EnharmonicScoreRules")

## EnharmonicScoreRules

class music21.analysis.enharmonics.EnharmonicScoreRules[[source]](../_modules/music21/analysis/enharmonics.html#EnharmonicScoreRules)

## EnharmonicSimplifier

class music21.analysis.enharmonics.EnharmonicSimplifier(*pitchList*, *ruleClass=<class 'music21.analysis.enharmonics.EnharmonicScoreRules'>*)[[source]](../_modules/music21/analysis/enharmonics.html#EnharmonicSimplifier)
:   Takes any pitch list input and returns the best enharmonic respelling according to the input
    criteria and rule weightings.
    Those criteria and rule weightings are currently fixed, but in future the user should be able
    to select their own combination and weighting of rules according to preferences,
    with predefined defaults for melodic and harmonic norms.
    Note: EnharmonicSimplifier itself returns nothing.

[`EnharmonicSimplifier`](#music21.analysis.enharmonics.EnharmonicSimplifier "music21.analysis.enharmonics.EnharmonicSimplifier") methods

EnharmonicSimplifier.bestPitches()[[source]](../_modules/music21/analysis/enharmonics.html#EnharmonicSimplifier.bestPitches)
:   Returns a list of pitches in the best enharmonic
    spelling according to the input criteria.

    ```python
    >>> pList1 = [pitch.Pitch('C'), pitch.Pitch('D'), pitch.Pitch('E')]
    >>> es = analysis.enharmonics.EnharmonicSimplifier(pList1)
    >>> es.bestPitches()
    (<music21.pitch.Pitch C>, <music21.pitch.Pitch D>, <music21.pitch.Pitch E>)
    >>> pList2 = ['D--', 'E', 'F##']
    >>> es = analysis.enharmonics.EnharmonicSimplifier(pList2)
    >>> es.bestPitches()
    (<music21.pitch.Pitch C>, <music21.pitch.Pitch E>, <music21.pitch.Pitch G>)
    ```

EnharmonicSimplifier.getAlterationScore(*possibility*)[[source]](../_modules/music21/analysis/enharmonics.html#EnharmonicSimplifier.getAlterationScore)
:   Returns a score according to the number of sharps and flats in a possible spelling.
    The score is the sum of the flats and sharps + 1, multiplied by the alterationPenalty.

EnharmonicSimplifier.getAugDimScore(*possibility*)[[source]](../_modules/music21/analysis/enharmonics.html#EnharmonicSimplifier.getAugDimScore)
:   Returns a score based on the number of augmented and diminished intervals between
    successive pitches in the given spelling.

EnharmonicSimplifier.getMixSharpFlatsScore(*possibility*)[[source]](../_modules/music21/analysis/enharmonics.html#EnharmonicSimplifier.getMixSharpFlatsScore)
:   Returns a score based on the mixture of sharps and flats in a possible spelling:
    the score is given by the number of the lesser used accidental (sharps or flats)
    multiplied by the mixSharpsFlatsPenalty.

EnharmonicSimplifier.getProduct()[[source]](../_modules/music21/analysis/enharmonics.html#EnharmonicSimplifier.getProduct)

EnharmonicSimplifier.getRepresentations()[[source]](../_modules/music21/analysis/enharmonics.html#EnharmonicSimplifier.getRepresentations)
:   Takes a list of pitches or pitch names and retrieves all enharmonic spellings.
    Note: getRepresentations itself returns nothing.
