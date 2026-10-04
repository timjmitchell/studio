Source: https://music21.org/music21docs/moduleReference/moduleFiguredBassExamples.html

# music21.figuredBass.examples

Each of the example methods in this module provides a figured bass line as a
[`FiguredBassLine`](moduleFiguredBassRealizer.html#music21.figuredBass.realizer.FiguredBassLine "music21.figuredBass.realizer.FiguredBassLine") instance.
These can be realized by calling
[`realize()`](moduleFiguredBassRealizer.html#music21.figuredBass.realizer.FiguredBassLine.realize "music21.figuredBass.realizer.FiguredBassLine.realize"), which takes in an
optional [`Rules`](moduleFiguredBassRules.html#music21.figuredBass.rules.Rules "music21.figuredBass.rules.Rules") object.
The result is a [`Realization`](moduleFiguredBassRealizer.html#music21.figuredBass.realizer.Realization "music21.figuredBass.realizer.Realization")
object which can generate realizations as instances of
`Score`. These realizations can then be displayed
in external software such as MuseScore or Finale by
calling [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show").

## Functions

music21.figuredBass.examples.exampleA()[[source]](../_modules/music21/figuredBass/examples.html#exampleA)
:   This example was a homework assignment for 21M.302: Harmony & Counterpoint II
    at MIT in the fall of 2010, taught by Charles Shadle of the MIT Music Program.

    ```python
    >>> from music21.figuredBass import examples
    >>> fbLine = examples.exampleA()
    >>> fbLine.generateBassLine().show()
    ```

    [![../_images/fbExamples_bassLineA.png](../_images/fbExamples_bassLineA.png)](../_images/fbExamples_bassLineA.png)

    The following is a realization of fbLine in four parts using the default rules set.
    The soprano part is limited to stepwise motion, and the alto and tenor parts are
    limited to motions within a perfect octave.

    ```python
    >>> from music21.figuredBass import rules
    >>> fbRules = rules.Rules()
    >>> fbRules.partMovementLimits = [(1, 2), (2, 12), (3, 12)]
    >>> fbRealization1 = fbLine.realize(fbRules)
    >>> fbRealization1.getNumSolutions()
    360
    >>> fbRealization1.generateRandomRealization().show()
    ```

    [![../_images/fbExamples_sol1A.png](../_images/fbExamples_sol1A.png)](../_images/fbExamples_sol1A.png)

    Now, the restriction on upper parts being within a perfect octave of each other is
    removed, and fbLine is realized again.

    ```python
    >>> fbRules.upperPartsMaxSemitoneSeparation = None
    >>> fbRealization2 = fbLine.realize(fbRules)
    >>> fbRealization2.keyboardStyleOutput = False
    >>> fbRealization2.getNumSolutions()
    3564440
    >>> fbRealization2.generateRandomRealization().show()
    ```

    [![../_images/fbExamples_sol2A.png](../_images/fbExamples_sol2A.png)](../_images/fbExamples_sol2A.png)

music21.figuredBass.examples.exampleB()[[source]](../_modules/music21/figuredBass/examples.html#exampleB)
:   This example was retrieved from page 114 of *The Music Theory Handbook* by Marjorie Merryman.

    ```python
    >>> from music21.figuredBass import examples
    >>> fbLine = examples.exampleB()
    >>> fbLine.generateBassLine().show()
    ```

    [![../_images/fbExamples_bassLineB.png](../_images/fbExamples_bassLineB.png)](../_images/fbExamples_bassLineB.png)

    First, fbLine is realized with the default rules set.

    ```python
    >>> fbRealization1 = fbLine.realize()
    >>> fbRealization1.getNumSolutions()
    422
    >>> fbRealization1.generateRandomRealization().show()
    ```

    [![../_images/fbExamples_sol1B.png](../_images/fbExamples_sol1B.png)](../_images/fbExamples_sol1B.png)

    Now, a Rules object is created, and the restriction that the chords
    need to be complete is lifted. fbLine is realized once again.

    ```python
    >>> from music21.figuredBass import rules
    >>> fbRules = rules.Rules()
    >>> fbRules.forbidIncompletePossibilities = False
    >>> fbRealization2 = fbLine.realize(fbRules)
    >>> fbRealization2.getNumSolutions()
    159373
    >>> fbRealization2.generateRandomRealization().show()
    ```

    [![../_images/fbExamples_sol2B.png](../_images/fbExamples_sol2B.png)](../_images/fbExamples_sol2B.png)

music21.figuredBass.examples.exampleC()[[source]](../_modules/music21/figuredBass/examples.html#exampleC)
:   This example was retrieved from page 114 of *The Music Theory Handbook* by Marjorie Merryman.

    ```python
    >>> from music21.figuredBass import examples
    >>> fbLine = examples.exampleC()
    >>> fbLine.generateBassLine().show()
    ```

    [![../_images/fbExamples_bassLineC.png](../_images/fbExamples_bassLineC.png)](../_images/fbExamples_bassLineC.png)

    First, fbLine is realized with the default rules set.

    ```python
    >>> fbRealization1 = fbLine.realize()
    >>> fbRealization1.getNumSolutions()
    833
    >>> fbRealization1.generateRandomRealization().show()
    ```

    [![../_images/fbExamples_sol1C.png](../_images/fbExamples_sol1C.png)](../_images/fbExamples_sol1C.png)

    Now, parallel fifths are allowed in realizations. The image below
    shows one of them. There is a parallel fifth between the bass and
    alto parts going from the half-diminished 6,5 (B,F#) to the dominant
    seventh (C#,G#) in the second measure.

    ```python
    >>> from music21.figuredBass import rules
    >>> fbRules = rules.Rules()
    >>> fbRules.forbidParallelFifths = False
    >>> fbRealization2 = fbLine.realize(fbRules)
    >>> fbRealization2.getNumSolutions()
    2427
    >>> fbRealization2.generateRandomRealization().show()
    ```

    [![../_images/fbExamples_sol2C.png](../_images/fbExamples_sol2C.png)](../_images/fbExamples_sol2C.png)

music21.figuredBass.examples.exampleD()[[source]](../_modules/music21/figuredBass/examples.html#exampleD)
:   This example was a homework assignment for 21M.302: Harmony & Counterpoint II
    at MIT in the fall of 2010, taught by Charles Shadle of the MIT Music Program.

    ```python
    >>> from music21.figuredBass import examples
    >>> fbLine = examples.exampleD()
    >>> fbLine.generateBassLine().show()
    ```

    [![../_images/fbExamples_bassLineD.png](../_images/fbExamples_bassLineD.png)](../_images/fbExamples_bassLineD.png)

    The following is a realization of fbLine in four parts using the default rules set.
    The soprano part is limited to stepwise motion, and the alto and tenor parts are
    limited to motions within a perfect octave.

    ```python
    >>> from music21.figuredBass import rules
    >>> fbRules = rules.Rules()
    >>> fbRules.partMovementLimits = [(1, 2), (2, 12), (3, 12)]
    >>> fbRealization1 = fbLine.realize(fbRules)
    >>> fbRealization1.getNumSolutions()
    1560
    >>> fbRealization1.generateRandomRealization().show()
    ```

    [![../_images/fbExamples_sol1D.png](../_images/fbExamples_sol1D.png)](../_images/fbExamples_sol1D.png)

    Now, the restriction on voice overlap is lifted, which is common in keyboard-style
    figured bass, and fbLine is realized again. Voice overlap can be seen in the fourth
    measure.

    ```python
    >>> fbRules.forbidVoiceOverlap = False
    >>> fbRealization2 = fbLine.realize(fbRules)
    >>> fbRealization2.getNumSolutions()
    109006
    >>> fbRealization2.generateRandomRealization().show()
    ```

    [![../_images/fbExamples_sol2D.png](../_images/fbExamples_sol2D.png)](../_images/fbExamples_sol2D.png)

    Now, the restriction on voice overlap is reset, but the restriction on the upper parts
    being within a perfect octave of each other is removed. fbLine is realized again.

    ```python
    >>> fbRules.forbidVoiceOverlap = True
    >>> fbRules.upperPartsMaxSemitoneSeparation = None
    >>> fbRealization3 = fbLine.realize(fbRules)
    >>> fbRealization3.getNumSolutions()
    27445876
    >>> fbRealization3.keyboardStyleOutput = False
    >>> fbRealization3.generateRandomRealization().show()
    ```

    [![../_images/fbExamples_sol3D.png](../_images/fbExamples_sol3D.png)](../_images/fbExamples_sol3D.png)

music21.figuredBass.examples.V43ResolutionExample()[[source]](../_modules/music21/figuredBass/examples.html#V43ResolutionExample)
:   The dominant 4,3 can resolve to either the tonic 5,3 or tonic 6,3. The proper resolution
    is dependent on the bass note of the tonic, and is determined in context, as shown in the
    following figured bass realization.

    ```python
    >>> from music21.figuredBass import examples
    >>> fbLine = examples.V43ResolutionExample()
    >>> fbRealization = fbLine.realize()
    >>> fbRealization.generateRandomRealization().show()
    ```

    [![../_images/fbExamples_V43.png](../_images/fbExamples_V43.png)](../_images/fbExamples_V43.png)

music21.figuredBass.examples.viio65ResolutionExample()[[source]](../_modules/music21/figuredBass/examples.html#viio65ResolutionExample)
:   For a fully diminished seventh chord resolving to the tonic, the resolution chord
    can contain either a doubled third (standard resolution) or a doubled tonic (alternate
    resolution), depending on whether the third of the diminished chord rises or falls.
    The user can control this in a Rules object by modifying
    [`doubledRootInDim7`](moduleFiguredBassRules.html#music21.figuredBass.rules.Rules.doubledRootInDim7 "music21.figuredBass.rules.Rules.doubledRootInDim7").
    However, when resolving a diminished 6,5, the third is found in the bass and the
    proper resolution is determined in context, regardless of user preference.

    The following shows both cases involving a diminished 6,5. The resolution of the
    first diminished chord has a doubled D, while that of the second has a doubled F#.
    Notice that the resolution of the first involves a diminished fifth (E, Bb) going
    to a perfect fifth (D, A).

    ```python
    >>> from music21.figuredBass import examples
    >>> fbLine = examples.viio65ResolutionExample()
    >>> fbRealization = fbLine.realize()
    >>> fbRealization.generateRandomRealization().show()
    ```

    [![../_images/fbExamples_vii65.png](../_images/fbExamples_vii65.png)](../_images/fbExamples_vii65.png)

music21.figuredBass.examples.augmentedSixthResolutionExample()[[source]](../_modules/music21/figuredBass/examples.html#augmentedSixthResolutionExample)
:   This example was retrieved from page 61 of *The Music Theory Handbook* by Marjorie Merryman.

    Italian (8,#6,3), French (#6,4,3), German (#6,5,3), and Swiss (#6,#4,3)
    augmented sixth resolutions to
    either the major dominant or the major/minor tonic 6,4 are supported.
    The first four bars show the
    resolutions to the dominant in the order above, while the last bar
    shows the German augmented sixth
    resolving to the tonic.

    ```python
    >>> from music21.figuredBass import examples
    >>> fbLine = examples.augmentedSixthResolutionExample()
    >>> fbRealization = fbLine.realize()
    >>> fbRealization.generateRandomRealization().show()
    ```

    [![../_images/fbExamples_a6.png](../_images/fbExamples_a6.png)](../_images/fbExamples_a6.png)

music21.figuredBass.examples.italianA6ResolutionExample()[[source]](../_modules/music21/figuredBass/examples.html#italianA6ResolutionExample)
:   The Italian augmented sixth chord (It+6) is the only
    augmented sixth chord to consist of only three
    pitch names, and when represented in four parts, the
    tonic is doubled. The tonic can resolve up, down or
    stay the same, and in four parts, the two tonics always
    resolve differently, resulting in two equally
    acceptable resolutions. An alternate approach to resolving
    the It+6 chord was taken, such that an It+6
    chord could map internally to two different resolutions.
    Every other special resolution in fbRealizer
    consists of a 1:1 mapping of special chords to resolutions.

    Here, the It+6 chord is resolving to the dominant, minor tonic,
    and major tonic, respectively. In the
    dominant resolution shown, the tonics (D) are resolving inward,
    but they can resolve outward as well. In
    the minor tonic resolution, the higher tonic is resolving up to F,
    and the lower tonic remains the same.
    In the major tonic resolution, the higher tonic remains the same,
    while the lower tonic resolves up to the F#.

    ```python
    >>> from music21.figuredBass import examples
    >>> from music21.figuredBass import rules
    >>> fbLine = examples.italianA6ResolutionExample()
    >>> fbRules = rules.Rules()
    >>> fbRules.upperPartsMaxSemitoneSeparation = None
    >>> fbRules.partMovementLimits.append([1, 4])
    >>> fbRealization = fbLine.realize(fbRules)
    >>> fbRealization.keyboardStyleOutput = False
    >>> fbRealization.generateRandomRealization().show()
    ```

    [![../_images/fbExamples_it%2B6.png](../_images/fbExamples_it%2B6.png)](../_images/fbExamples_it+6.png)

music21.figuredBass.examples.twelveBarBlues()[[source]](../_modules/music21/figuredBass/examples.html#twelveBarBlues)
:   This is a progression in Bb major based on the twelve bar blues. The progression used is:

    > I | IV | I | I7
    > IV | IV | I | I7
    > V7 | IV6 | I | I

    ```python
    >>> from music21.figuredBass import examples
    >>> from music21.figuredBass import rules
    >>> bluesLine = examples.twelveBarBlues()
    >>> bluesLine.generateBassLine().show()
    ```

    [![../_images/fbExamples_bluesBassLine.png](../_images/fbExamples_bluesBassLine.png)](../_images/fbExamples_bluesBassLine.png)

    ```python
    >>> fbRules = rules.Rules()
    >>> fbRules.partMovementLimits = [(1, 4), (2, 12), (3, 12)]
    >>> fbRules.forbidVoiceOverlap = False
    >>> blRealization = bluesLine.realize(fbRules)
    >>> blRealization.getNumSolutions()
    2224978
    >>> blRealization.generateRandomRealization().show()
    ```

    [![../_images/fbExamples_twelveBarBlues.png](../_images/fbExamples_twelveBarBlues.png)](../_images/fbExamples_twelveBarBlues.png)

music21.figuredBass.examples.generateBoogieVamp(*blRealization=None*, *numRepeats=5*)[[source]](../_modules/music21/figuredBass/examples.html#generateBoogieVamp)
:   Turns whole notes in twelve bar blues bass line to blues boogie woogie bass line. Takes
    in numRepeats, which is the number of times to repeat the bass line. Also, takes in a
    realization of [`twelveBarBlues()`](#music21.figuredBass.examples.twelveBarBlues "music21.figuredBass.examples.twelveBarBlues"). If none is provided,
    a default realization with [`forbidVoiceOverlap`](moduleFiguredBassRules.html#music21.figuredBass.rules.Rules.forbidVoiceOverlap "music21.figuredBass.rules.Rules.forbidVoiceOverlap")
    set to False and [`partMovementLimits`](moduleFiguredBassRules.html#music21.figuredBass.rules.Rules.partMovementLimits "music21.figuredBass.rules.Rules.partMovementLimits") set to
    [(1, 4), (2, 12), (3, 12)] is used.

    ```python
    >>> from music21.figuredBass import examples
    >>> examples.generateBoogieVamp(numRepeats=1).show()
    ```

    [![../_images/fbExamples_boogieVamp.png](../_images/fbExamples_boogieVamp.png)](../_images/fbExamples_boogieVamp.png)

music21.figuredBass.examples.generateTripletBlues(*blRealization=None*, *numRepeats=5*)[[source]](../_modules/music21/figuredBass/examples.html#generateTripletBlues)
:   Turns whole notes in twelve bar blues bass line to triplet blues bass line. Takes
    in numRepeats, which is the number of times to repeat the bass line. Also, takes in a
    realization of [`twelveBarBlues()`](#music21.figuredBass.examples.twelveBarBlues "music21.figuredBass.examples.twelveBarBlues"). If none is provided,
    a default realization with [`forbidVoiceOverlap`](moduleFiguredBassRules.html#music21.figuredBass.rules.Rules.forbidVoiceOverlap "music21.figuredBass.rules.Rules.forbidVoiceOverlap")
    set to False and [`partMovementLimits`](moduleFiguredBassRules.html#music21.figuredBass.rules.Rules.partMovementLimits "music21.figuredBass.rules.Rules.partMovementLimits") set to
    [(1, 4), (2, 12), (3, 12)] is used.

    ```python
    >>> from music21.figuredBass import examples
    >>> examples.generateTripletBlues(numRepeats=1).show()
    ```

    [![../_images/fbExamples_tripletBlues.png](../_images/fbExamples_tripletBlues.png)](../_images/fbExamples_tripletBlues.png)
