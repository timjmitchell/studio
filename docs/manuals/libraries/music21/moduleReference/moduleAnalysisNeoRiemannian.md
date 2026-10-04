Source: https://music21.org/music21docs/moduleReference/moduleAnalysisNeoRiemannian.html

# music21.analysis.neoRiemannian

This module defines the L, P, and R objects and their
related transformations as called on a [`Chord`](moduleChord.html#music21.chord.Chord "music21.chord.Chord"),
according to Neo-Riemannian theory.

## Functions

music21.analysis.neoRiemannian.L(*c*, *raiseException=True*)[[source]](../_modules/music21/analysis/neoRiemannian.html#L)
:   L transforms a major or minor triad through the ‘Leading-Tone exchange’.
    A C major chord, under L, will return an E minor chord, by transforming the root
    to its leading tone, B.

    ```python
    >>> c1 = chord.Chord('C4 E4 G4')
    >>> c2 = analysis.neoRiemannian.L(c1)
    >>> c2.pitches
    (<music21.pitch.Pitch B3>, <music21.pitch.Pitch E4>, <music21.pitch.Pitch G4>)
    ```

    Chords must be major or minor triads:

    ```python
    >>> c3 = chord.Chord('C4 D4 E4')
    >>> analysis.neoRiemannian.L(c3)
    Traceback (most recent call last):
    music21.analysis.neoRiemannian.LRPException: Cannot perform L on this chord:
        not a major or minor triad
    ```

    If raiseException is False then the original chord is returned.

    ```python
    >>> c4 = analysis.neoRiemannian.L(c3, raiseException=False)
    >>> c4 is c3
    True
    ```

    Accepts any music21 chord, with or without octave specified:

    ```python
    >>> noOctaveChord = chord.Chord([0, 3, 7])
    >>> chordL = analysis.neoRiemannian.L(noOctaveChord)
    >>> chordL.pitches
    (<music21.pitch.Pitch C>, <music21.pitch.Pitch E->, <music21.pitch.Pitch A->)
    ```

music21.analysis.neoRiemannian.R(*c*, *raiseException=True*)[[source]](../_modules/music21/analysis/neoRiemannian.html#R)
:   R transforms a major or minor triad to its relative, i.e. if
    major, to its relative minor and if minor, to its relative major.

    Example 1: A C major chord, under R, will return an A minor chord

    ```python
    >>> c1 = chord.Chord('C4 E4 G4')
    >>> c2 = analysis.neoRiemannian.R(c1)
    >>> c2.pitches
    (<music21.pitch.Pitch C4>, <music21.pitch.Pitch E4>, <music21.pitch.Pitch A4>)
    ```

    See [`L()`](#music21.analysis.neoRiemannian.L "music21.analysis.neoRiemannian.L") for further details about error handling.

music21.analysis.neoRiemannian.P(*c*, *raiseException=True*)[[source]](../_modules/music21/analysis/neoRiemannian.html#P)
:   P transforms a major or minor triad chord to its ‘parallel’:
    i.e. to the chord of the same diatonic name but opposite model.

    Example: A C major chord, under P, will return an C minor chord

    ```python
    >>> c2 = chord.Chord('C4 E4 G4')
    >>> c3 = analysis.neoRiemannian.P(c2)
    >>> c3.pitches
    (<music21.pitch.Pitch C4>, <music21.pitch.Pitch E-4>, <music21.pitch.Pitch G4>)
    ```

    See [`L()`](#music21.analysis.neoRiemannian.L "music21.analysis.neoRiemannian.L") for further details about error handling.

music21.analysis.neoRiemannian.S(*c*)[[source]](../_modules/music21/analysis/neoRiemannian.html#S)
:   Slide transform connecting major and minor triads with the third as the single common tone
    (i.e. with the major triad root a semi-tone below the minor). So:
    root motion by a semi-tone;
    mode-change;
    one common-tones.
    Slide is equivalent to ‘LPR’.

    ```python
    >>> cMaj = chord.Chord('C5 E5 G5')
    >>> slideUp = analysis.neoRiemannian.S(cMaj)
    >>> [x.name for x in slideUp.pitches]
    ['C#', 'E', 'G#']
    ```

    ```python
    >>> aMin = chord.Chord('A4 C5 E5')
    >>> slideDown = analysis.neoRiemannian.S(aMin)
    >>> [x.name for x in slideDown.pitches]
    ['A-', 'C', 'E-']
    ```

music21.analysis.neoRiemannian.N(*c*)[[source]](../_modules/music21/analysis/neoRiemannian.html#N)
:   The ‘Neberverwandt’ (‘fifth-change’) transform connects
    a minor triad with its major dominant, and so also
    a major triad with its minor sub-dominant,
    with one common tone in each case.
    This is equivalent to ‘RLP’.

    ```python
    >>> cMaj = chord.Chord('C5 E5 G5')
    >>> n1 = analysis.neoRiemannian.N(cMaj)
    >>> [x.name for x in n1.pitches]
    ['C', 'F', 'A-']
    ```

    ```python
    >>> aMin = chord.Chord('A4 C5 E5')
    >>> n2 = analysis.neoRiemannian.N(aMin)
    >>> [x.name for x in n2.pitches]
    ['G#', 'B', 'E']
    ```

music21.analysis.neoRiemannian.isNeoR(*c1*, *c2*, *transforms='LRP'*)[[source]](../_modules/music21/analysis/neoRiemannian.html#isNeoR)
:   Tests if two chords are related by a single L, P, R transformation,
    and returns that transform if so (otherwise, False).

    ```python
    >>> c1 = chord.Chord('C4 E4 G4')
    >>> c2 = chord.Chord('B3 E4 G4')
    >>> analysis.neoRiemannian.isNeoR(c1, c2)
    'L'
    ```

    ```python
    >>> c1 = chord.Chord('C4 E4 G4')
    >>> c2 = chord.Chord('C4 E-4 G4')
    >>> analysis.neoRiemannian.isNeoR(c1, c2)
    'P'
    ```

    ```python
    >>> c1 = chord.Chord('C4 E4 G4')
    >>> c2 = chord.Chord('C4 E4 A4')
    >>> analysis.neoRiemannian.isNeoR(c1, c2)
    'R'
    ```

    ```python
    >>> c1 = chord.Chord('C4 E4 G4')
    >>> c2 = chord.Chord('C-4 E-4 A-4')
    >>> analysis.neoRiemannian.isNeoR(c1, c2)
    False
    ```

    Option to limit to the search to only 1-2 transforms (‘L’, ‘R’, ‘P’, ‘LR’, ‘LP’, ‘RP’). So:

    ```python
    >>> c3 = chord.Chord('C4 E-4 G4')
    >>> analysis.neoRiemannian.isNeoR(c1, c3)
    'P'
    ```

    … but not if P is excluded …

    ```python
    >>> analysis.neoRiemannian.isNeoR(c1, c3, transforms='LR')
    False
    ```

music21.analysis.neoRiemannian.LRP\_combinations(*c*, *transformationString*, *raiseException=True*, *leftOrdered=False*, *simplifyEnharmonics=False*, *eachOne=False*)[[source]](../_modules/music21/analysis/neoRiemannian.html#LRP_combinations)
:   LRP\_combinations takes a major or minor triad, transforms it according to the
    list of L, R, and P transformations in the given transformationString, and
    returns the result in triad.
    Certain combinations, such as LPLPLP, are cyclical, and therefore
    will return a copy of the original chord if simplifyEnharmonics = True (see
    [`completeHexatonic()`](#music21.analysis.neoRiemannian.completeHexatonic "music21.analysis.neoRiemannian.completeHexatonic"), below).

    leftOrdered allows a user to work with their preferred function notation (left or right
    orthography).

    By default, leftOrdered is False, so transformations progress towards the right.
    Thus, ‘LPR’ will start by transforming the chord by L, then P, then R.

    If leftOrdered is True, the operations work in the opposite direction (right to left), so
    ‘LPR’ indicates the result of the chord transformed by R, then P, then L.

    simplifyEnharmonics replaces multiple sharps and flats where they arise from
    combined transformations with the simpler enharmonic equivalent (e.g. C for D–).
    If simplifyEnharmonics is True, the resulting chord will be simplified
    to a collection of notes with at most 1 flat or 1 sharp, in their most common form.

    ```python
    >>> c1 = chord.Chord('C4 E4 G4')
    >>> c2 = analysis.neoRiemannian.LRP_combinations(c1, 'LP')
    >>> c2
    <music21.chord.Chord B3 E4 G#4>
    ```

    ```python
    >>> c2b = analysis.neoRiemannian.LRP_combinations(c1, 'LP', leftOrdered=True)
    >>> c2b
    <music21.chord.Chord C4 E-4 A-4>
    ```

    ```python
    >>> c3 = chord.Chord('C4 E4 G4 C5 E5')
    >>> c4 = analysis.neoRiemannian.LRP_combinations(c3, 'RLP')
    >>> c4
    <music21.chord.Chord C4 F4 A-4 C5 F5>
    ```

    ```python
    >>> c5 = chord.Chord('B4 D#5 F#5')
    >>> c6 = analysis.neoRiemannian.LRP_combinations(c5,
    ...                        'LPLPLP', leftOrdered=True, simplifyEnharmonics=True)
    >>> c6
    <music21.chord.Chord B4 D#5 F#5>
    >>> c5 = chord.Chord('C4 E4 G4')
    >>> c6 = analysis.neoRiemannian.LRP_combinations(c5, 'LPLPLP', leftOrdered=True)
    >>> c6
    <music21.chord.Chord D--4 F-4 A--4>
    >>> c5 = chord.Chord('A-4 C4 E-5')
    >>> c6 = analysis.neoRiemannian.LRP_combinations(c5, 'LPLPLP')
    >>> c6
    <music21.chord.Chord G#4 B#3 D#5>
    ```

    Optionally: return all chords creating by the given string in order.

    ```python
    >>> c7 = chord.Chord('C4 E4 G4')
    >>> c8 = analysis.neoRiemannian.LRP_combinations(
    ...            c7, 'LPLPLP', simplifyEnharmonics=True, eachOne=True)
    >>> c8
    [<music21.chord.Chord B3 E4 G4>,
    <music21.chord.Chord B3 E4 G#4>,
    <music21.chord.Chord B3 D#4 G#4>,
    <music21.chord.Chord C4 E-4 A-4>,
    <music21.chord.Chord C4 E-4 G4>,
    <music21.chord.Chord C4 E4 G4>]
    ```

    On that particular case of LPLPLP, see more in
    [`completeHexatonic()`](#music21.analysis.neoRiemannian.completeHexatonic "music21.analysis.neoRiemannian.completeHexatonic").

music21.analysis.neoRiemannian.completeHexatonic(*c*, *simplifyEnharmonics=False*, *raiseException=True*)[[source]](../_modules/music21/analysis/neoRiemannian.html#completeHexatonic)
:   completeHexatonic returns the list of six triads generated by the operation PLPLPL.
    This six-part operation cycles between major and minor triads, ultimately returning to the
    input triad (or its enharmonic equivalent).
    This functions returns those six triads, ending with the original triad.

    simplifyEnharmonics is False, by default, giving double flats at the end.

    ```python
    >>> c1 = chord.Chord('C4 E4 G4')
    >>> analysis.neoRiemannian.completeHexatonic(c1)
    [<music21.chord.Chord C4 E-4 G4>,
     <music21.chord.Chord C4 E-4 A-4>,
     <music21.chord.Chord C-4 E-4 A-4>,
     <music21.chord.Chord C-4 F-4 A-4>,
     <music21.chord.Chord C-4 F-4 A--4>,
     <music21.chord.Chord D--4 F-4 A--4>]
    ```

    simplifyEnharmonics can be set to True in order to avoid this.

    ```python
    >>> c2 = chord.Chord('C4 E4 G4')
    >>> analysis.neoRiemannian.completeHexatonic(c2, simplifyEnharmonics=True)
    [<music21.chord.Chord C4 E-4 G4>,
     <music21.chord.Chord C4 E-4 A-4>,
     <music21.chord.Chord B3 D#4 G#4>,
     <music21.chord.Chord B3 E4 G#4>,
     <music21.chord.Chord B3 E4 G4>,
     <music21.chord.Chord C4 E4 G4>]
    ```

music21.analysis.neoRiemannian.hexatonicSystem(*c*)[[source]](../_modules/music21/analysis/neoRiemannian.html#hexatonicSystem)
:   Returns a lowercase string representing the
    “hexatonic system” that the chord c belongs to
    as classified by Richard Cohn, “Maximally Smooth Cycles,
    Hexatonic Systems, and the Analysis of Late-Romantic
    Triadic Progressions,” *Music Analysis*, 15.1 (1996), 9-40,
    at p. 17. Possible values are ‘northern’, ‘western’, ‘eastern’, or ‘southern’

    ```python
    >>> cMaj = chord.Chord('C E G')
    >>> analysis.neoRiemannian.hexatonicSystem(cMaj)
    'northern'
    ```

    ```python
    >>> gMin = chord.Chord('G B- D')
    >>> analysis.neoRiemannian.hexatonicSystem(gMin)
    'western'
    ```

    Each chord in the [`completeHexatonic()`](#music21.analysis.neoRiemannian.completeHexatonic "music21.analysis.neoRiemannian.completeHexatonic") of that chord
    is in the same hexatonic system, by definition or tautology.

    ```python
    >>> for ch in analysis.neoRiemannian.completeHexatonic(cMaj):
    ...     print(analysis.neoRiemannian.hexatonicSystem(ch))
    northern
    northern
    northern
    northern
    northern
    northern
    ```

    Note that the classification looks only at the
    pitch class of the root of the chord. Seventh chords,
    diminished triads, etc. will also be classified.

    ```python
    >>> dDom65 = chord.Chord('F#4 D5 A5 C6')
    >>> analysis.neoRiemannian.hexatonicSystem(dDom65)
    'southern'
    ```

music21.analysis.neoRiemannian.chromaticMediants(*c*, *transformation='UFM'*)[[source]](../_modules/music21/analysis/neoRiemannian.html#chromaticMediants)
:   Transforms a chord into the given chromatic mediant. Options:
    UFM = Upper Flat Mediant;
    USM = Upper Sharp Mediant;
    LFM = Lower Flat Mediant ;
    LSM = Lower Sharp Mediant;

    Each of these transformations
    is mode-preserving;
    involves root motion by a third;
    entails exactly one common-tone.

    ```python
    >>> cMaj = chord.Chord('C5 E5 G5')
    >>> UFMcMaj = analysis.neoRiemannian.chromaticMediants(cMaj, transformation='UFM')
    >>> UFMcMaj.normalOrder
    [3, 7, 10]
    ```

    ```python
    >>> USMcMaj = analysis.neoRiemannian.chromaticMediants(cMaj, transformation='USM')
    >>> USMcMaj.normalOrder
    [4, 8, 11]
    ```

    ```python
    >>> LFMcMaj = analysis.neoRiemannian.chromaticMediants(cMaj, transformation='LFM')
    >>> [x.nameWithOctave for x in LFMcMaj.pitches]
    ['C5', 'E-5', 'A-5']
    ```

    ```python
    >>> LSMcMaj = analysis.neoRiemannian.chromaticMediants(cMaj, transformation='LSM')
    >>> [x.nameWithOctave for x in LSMcMaj.pitches]
    ['C#5', 'E5', 'A5']
    ```

    Fine to call on a chord with multiple enharmonics,
    but will always simplify the output chromatic mediant.

    ```python
    >>> cMajEnh = chord.Chord('D--5 F-5 A--5')
    >>> USM = analysis.neoRiemannian.chromaticMediants(cMaj, transformation='USM')
    >>> [x.nameWithOctave for x in USM.pitches]
    ['B4', 'E5', 'G#5']
    >>> USM.normalOrder == USMcMaj.normalOrder
    True
    ```

music21.analysis.neoRiemannian.isChromaticMediant(*c1*, *c2*)[[source]](../_modules/music21/analysis/neoRiemannian.html#isChromaticMediant)
:   Tests if there is a chromatic mediant relation between two chords
    and returns the type if so (otherwise, False).

    ```python
    >>> c1 = chord.Chord('C4 E4 G4')
    >>> c2 = chord.Chord('A-3 C4 E-4')
    >>> analysis.neoRiemannian.isChromaticMediant(c1, c2)
    'LFM'
    ```

    ```python
    >>> c3 = chord.Chord('C4 E4 G4')
    >>> c4 = chord.Chord('C-4 E-4 A-4')
    >>> analysis.neoRiemannian.isChromaticMediant(c3, c4)
    False
    ```

music21.analysis.neoRiemannian.disjunctMediants(*c*, *upperOrLower='upper'*)[[source]](../_modules/music21/analysis/neoRiemannian.html#disjunctMediants)
:   Transforms a chord into the upper or lower disjunct mediant.
    These transformations involve:
    root motion by a non-diatonic third;
    mode-change;
    no common-tones.

    ```python
    >>> cMaj = chord.Chord('C5 E5 G5')
    >>> upr = analysis.neoRiemannian.disjunctMediants(cMaj, upperOrLower='upper')
    >>> [x.name for x in upr.pitches]
    ['B-', 'E-', 'G-']
    >>> lwr = analysis.neoRiemannian.disjunctMediants(cMaj, upperOrLower='lower')
    >>> [x.name for x in lwr.pitches]
    ['B', 'D#', 'G#']
    ```
