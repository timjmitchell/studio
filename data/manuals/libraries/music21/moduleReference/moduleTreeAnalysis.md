Source: https://music21.org/music21docs/moduleReference/moduleTreeAnalysis.html

# music21.tree.analysis

Tools for performing voice-leading analysis with trees.

## Horizontality

class music21.tree.analysis.Horizontality(*timespans=None*)[[source]](../_modules/music21/tree/analysis.html#Horizontality)
:   A horizontality of consecutive PitchedTimespan objects.

    It must be initiated with a list or tuple of Timespan objects.

[`Horizontality`](#music21.tree.analysis.Horizontality "music21.tree.analysis.Horizontality") read-only properties

Horizontality.hasNeighborTone
:   Is true if the Horizontality contains a neighbor tone.

Horizontality.hasNoMotion
:   Is true if the Horizontality contains no motion (including enharmonic restatements)

Horizontality.hasPassingTone
:   Is true if the Horizontality contains a passing tone; currently defined as three tones in
    one direction.

    (TODO: better check)

[`Horizontality`](#music21.tree.analysis.Horizontality "music21.tree.analysis.Horizontality") methods

Horizontality.\_\_getitem\_\_(*item*)[[source]](../_modules/music21/tree/analysis.html#Horizontality.__getitem__)
