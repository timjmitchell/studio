Source: https://music21.org/music21docs/moduleReference/moduleFiguredBassResolution.html

# music21.figuredBass.resolution

Note

The terminology, V43, viio, iv, etc. are explained elsewhere,
such as *The Music Theory Handbook* by Marjorie Merryman.

This module contains methods which can properly resolve
[dominant seventh](https://en.wikipedia.org/wiki/Dominant_seventh_chord),
[diminished seventh](https://en.wikipedia.org/wiki/Diminished_seventh_chord), and
[augmented sixth](https://en.wikipedia.org/wiki/Augmented_sixth_chord)
chords expressed as possibilities (See [`possibility`](moduleFiguredBassPossibility.html#module-music21.figuredBass.possibility "music21.figuredBass.possibility")).
Although these methods can stand alone, they are speed-enhanced for instances
of [`Segment`](moduleFiguredBassSegment.html#music21.figuredBass.segment.Segment "music21.figuredBass.segment.Segment"), where there are many
possibilities formed around the same chord. If provided with additional
arguments, the methods only [`transpose()`](modulePitch.html#music21.pitch.Pitch.transpose "music21.pitch.Pitch.transpose") each
[`Pitch`](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") in a possibility by the appropriate interval.

## Functions

music21.figuredBass.resolution.augmentedSixthToDominant(*augSixthPossib*, *augSixthType: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *augSixthChordInfo: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch"), ...][[source]](../_modules/music21/figuredBass/resolution.html#augmentedSixthToDominant)
:   Resolves French (augSixthType = 1), German (augSixthType = 2), and Swiss (augSixthType = 3)
    augmented sixth chords to the root position dominant triad.

    Proper Italian augmented sixth resolutions not supported within this method.

    ```python
    >>> from music21.figuredBass import resolution
    >>> Bb2 = pitch.Pitch('B-2')
    >>> D4 = pitch.Pitch('D4')
    >>> E4 = pitch.Pitch('E4')
    >>> Es4 = pitch.Pitch('E#4')
    >>> F4 = pitch.Pitch('F4')
    >>> G4 = pitch.Pitch('G4')
    >>> Gs4 = pitch.Pitch('G#4')
    >>> iv6 = (G4, D4, D4, Bb2)
    >>> itAug6 = (Gs4, D4, D4, Bb2)
    >>> frAug6 = (Gs4, E4, D4, Bb2)
    >>> grAug6 = (Gs4, F4, D4, Bb2)
    >>> swAug6 = (Gs4, Es4, D4, Bb2)
    ```

    ```python
    >>> frRes = resolution.augmentedSixthToDominant(frAug6)
    >>> frRes
    (<music21.pitch.Pitch A4>, <music21.pitch.Pitch E4>,
     <music21.pitch.Pitch C#4>, <music21.pitch.Pitch A2>)
    >>> [str(p) for p in frRes]
    ['A4', 'E4', 'C#4', 'A2']
    ```

    ```python
    >>> grRes = resolution.augmentedSixthToDominant(grAug6)
    >>> [str(p) for p in grRes]
    ['A4', 'E4', 'C#4', 'A2']
    ```

    ```python
    >>> swRes = resolution.augmentedSixthToDominant(swAug6)
    >>> [str(p) for p in swRes]
    ['A4', 'E4', 'C#4', 'A2']
    >>> resolution.showResolutions(frAug6, frRes, grAug6, grRes, swAug6, swRes)
    ```

    > [![../_images/fbResolution_a6toV.png](../_images/fbResolution_a6toV.png)](../_images/fbResolution_a6toV.png)

    Above: French, German, and Swiss resolutions, respectively.

music21.figuredBass.resolution.augmentedSixthToMajorTonic(*augSixthPossib*, *augSixthType: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *augSixthChordInfo: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch"), ...][[source]](../_modules/music21/figuredBass/resolution.html#augmentedSixthToMajorTonic)
:   Resolves French (augSixthType = 1), German (augSixthType = 2), and Swiss (augSixthType = 3)
    augmented sixth chords to the major tonic 6,4.

    Proper Italian augmented sixth resolutions not supported within this method.

    ```python
    >>> from music21.figuredBass import resolution
    >>> Bb2 = pitch.Pitch('B-2')
    >>> D4 = pitch.Pitch('D4')
    >>> E4 = pitch.Pitch('E4')
    >>> Es4 = pitch.Pitch('E#4')
    >>> F4 = pitch.Pitch('F4')
    >>> G4 = pitch.Pitch('G4')
    >>> Gs4 = pitch.Pitch('G#4')
    >>> iv6 = (G4, D4, D4, Bb2)
    >>> itAug6 = (Gs4, D4, D4, Bb2)
    >>> frAug6 = (Gs4, E4, D4, Bb2)
    >>> grAug6 = (Gs4, F4, D4, Bb2)
    >>> swAug6 = (Gs4, Es4, D4, Bb2)
    >>> frRes = resolution.augmentedSixthToMajorTonic(frAug6)
    >>> [str(p) for p in frRes]
    ['A4', 'F#4', 'D4', 'A2']
    >>> grRes = resolution.augmentedSixthToMajorTonic(grAug6)
    >>> [str(p) for p in grRes]
    ['A4', 'F#4', 'D4', 'A2']
    >>> swRes = resolution.augmentedSixthToMajorTonic(swAug6)
    >>> [str(p) for p in swRes]
    ['A4', 'F#4', 'D4', 'A2']
    >>> resolution.showResolutions(frAug6, frRes, grAug6, grRes, swAug6, swRes)
    ```

    > [![../_images/fbResolution_a6toI.png](../_images/fbResolution_a6toI.png)](../_images/fbResolution_a6toI.png)

    Above: French, German, and Swiss resolutions, respectively.

music21.figuredBass.resolution.augmentedSixthToMinorTonic(*augSixthPossib*, *augSixthType: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *augSixthChordInfo: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch"), ...][[source]](../_modules/music21/figuredBass/resolution.html#augmentedSixthToMinorTonic)
:   Resolves French (augSixthType = 1), German (augSixthType = 2), and Swiss (augSixthType = 3)
    augmented sixth chords to the minor tonic 6,4.

    Proper Italian augmented sixth resolutions not supported within this method.

    ```python
    >>> from music21.figuredBass import resolution
    >>> Bb2 = pitch.Pitch('B-2')
    >>> D4 = pitch.Pitch('D4')
    >>> E4 = pitch.Pitch('E4')
    >>> Es4 = pitch.Pitch('E#4')
    >>> F4 = pitch.Pitch('F4')
    >>> G4 = pitch.Pitch('G4')
    >>> Gs4 = pitch.Pitch('G#4')
    >>> iv6 = (G4, D4, D4, Bb2)
    >>> itAug6 = (Gs4, D4, D4, Bb2)
    >>> frAug6 = (Gs4, E4, D4, Bb2)
    >>> grAug6 = (Gs4, F4, D4, Bb2)
    >>> swAug6 = (Gs4, Es4, D4, Bb2)
    >>> frRes = resolution.augmentedSixthToMinorTonic(frAug6)
    >>> [str(p) for p in frRes]
    ['A4', 'F4', 'D4', 'A2']
    >>> grRes = resolution.augmentedSixthToMinorTonic(grAug6)
    >>> [str(p) for p in grRes]
    ['A4', 'F4', 'D4', 'A2']
    >>> swRes = resolution.augmentedSixthToMinorTonic(swAug6)
    >>> [str(p) for p in swRes]
    ['A4', 'F4', 'D4', 'A2']
    >>> resolution.showResolutions(frAug6, frRes, grAug6, grRes, swAug6, swRes)
    ```

    > [![../_images/fbResolution_a6toIm.png](../_images/fbResolution_a6toIm.png)](../_images/fbResolution_a6toIm.png)

    Above: French, German, and Swiss resolutions, respectively.

music21.figuredBass.resolution.dominantSeventhToMajorTonic(*domPossib*, *resolveV43toI6=False*, *domChordInfo=None*)[[source]](../_modules/music21/figuredBass/resolution.html#dominantSeventhToMajorTonic)
:   Resolves a dominant seventh chord in root position or any of its
    inversions to the major tonic, in root position or first inversion.

    The second inversion (4,3) dominant seventh chord can resolve to
    the tonic in either inversion. This is controlled by
    resolveV43toI6, and is set to True
    by [`resolveDominantSeventhSegment()`](moduleFiguredBassSegment.html#music21.figuredBass.segment.Segment.resolveDominantSeventhSegment "music21.figuredBass.segment.Segment.resolveDominantSeventhSegment")
    only when the [`segmentChord`](moduleFiguredBassSegment.html#music21.figuredBass.segment.Segment.segmentChord "music21.figuredBass.segment.Segment.segmentChord")
    of a [`Segment`](moduleFiguredBassSegment.html#music21.figuredBass.segment.Segment "music21.figuredBass.segment.Segment")
    spells out a dominant seventh chord in second inversion.

    ```python
    >>> from music21.figuredBass import resolution
    >>> G2 = pitch.Pitch('G2')
    >>> C3 = pitch.Pitch('C3')
    >>> E3 = pitch.Pitch('E3')
    >>> G3 = pitch.Pitch('G3')
    >>> Bb3 = pitch.Pitch('B-3')
    >>> B3 = pitch.Pitch('B3')
    >>> C4 = pitch.Pitch('C4')
    >>> F4 = pitch.Pitch('F4')
    >>> Bb4 = pitch.Pitch('B-4')
    >>> D5 = pitch.Pitch('D5')
    >>> E5 = pitch.Pitch('E5')
    >>> domPossibA1 = (D5, F4, B3, G2)
    >>> resPossibA1 = resolution.dominantSeventhToMajorTonic(domPossibA1)
    >>> resPossibA1
    (<music21.pitch.Pitch C5>, <music21.pitch.Pitch E4>,
     <music21.pitch.Pitch C4>, <music21.pitch.Pitch C3>)
    >>> resolution.showResolutions(domPossibA1, resPossibA1)
    ```

    [![../_images/fbResolution_V7toI_1.png](../_images/fbResolution_V7toI_1.png)](../_images/fbResolution_V7toI_1.png)

    ```python
    >>> domPossibA2 = (Bb3, G3, E3, C3)
    >>> resPossibA2 = resolution.dominantSeventhToMajorTonic(domPossibA2)
    >>> [str(p) for p in resPossibA2]
    ['A3', 'F3', 'F3', 'F3']
    >>> resolution.showResolutions(domPossibA2, resPossibA2)
    ```

    [![../_images/fbResolution_V7toI_2.png](../_images/fbResolution_V7toI_2.png)](../_images/fbResolution_V7toI_2.png)

    ```python
    >>> domPossibA3 = (E5, Bb4, C4, G3)
    >>> resPossibA3a = resolution.dominantSeventhToMajorTonic(domPossibA3, False)
    >>> [str(p) for p in resPossibA3a]
    ['F5', 'A4', 'C4', 'F3']
    >>> resPossibA3b = resolution.dominantSeventhToMajorTonic(domPossibA3, True)
    >>> [str(p) for p in resPossibA3b]
    ['F5', 'C5', 'C4', 'A3']
    >>> resolution.showResolutions(domPossibA3, resPossibA3a, domPossibA3, resPossibA3b)
    ```

    [![../_images/fbResolution_V7toI_3.png](../_images/fbResolution_V7toI_3.png)](../_images/fbResolution_V7toI_3.png)

music21.figuredBass.resolution.dominantSeventhToMinorTonic(*domPossib*, *resolveV43toi6=False*, *domChordInfo=None*)[[source]](../_modules/music21/figuredBass/resolution.html#dominantSeventhToMinorTonic)
:   Resolves a dominant seventh chord in root position or any of its
    inversions to the minor tonic, in root position or first inversion,
    accordingly.

    The second inversion (4,3) dominant seventh chord can resolve to
    the tonic in either inversion. This is controlled by
    resolveV43toi6, and is set to True by
    [`resolveDominantSeventhSegment()`](moduleFiguredBassSegment.html#music21.figuredBass.segment.Segment.resolveDominantSeventhSegment "music21.figuredBass.segment.Segment.resolveDominantSeventhSegment")
    only when the [`segmentChord`](moduleFiguredBassSegment.html#music21.figuredBass.segment.Segment.segmentChord "music21.figuredBass.segment.Segment.segmentChord")
    of a [`Segment`](moduleFiguredBassSegment.html#music21.figuredBass.segment.Segment "music21.figuredBass.segment.Segment")
    spells out a dominant seventh chord in second inversion.

    ```python
    >>> from music21.figuredBass import resolution
    >>> G2 = pitch.Pitch('G2')
    >>> C3 = pitch.Pitch('C3')
    >>> E3 = pitch.Pitch('E3')
    >>> G3 = pitch.Pitch('G3')
    >>> Bb3 = pitch.Pitch('B-3')
    >>> B3 = pitch.Pitch('B3')
    >>> C4 = pitch.Pitch('C4')
    >>> F4 = pitch.Pitch('F4')
    >>> Bb4 = pitch.Pitch('B-4')
    >>> D5 = pitch.Pitch('D5')
    >>> E5 = pitch.Pitch('E5')
    >>> domPossibA1 = (D5, F4, B3, G2)
    >>> resPossibA1 = resolution.dominantSeventhToMinorTonic(domPossibA1)
    >>> [str(p) for p in resPossibA1]
    ['C5', 'E-4', 'C4', 'C3']
    >>> resolution.showResolutions(domPossibA1, resPossibA1)
    ```

    [![../_images/fbResolution_V7toIm_1.png](../_images/fbResolution_V7toIm_1.png)](../_images/fbResolution_V7toIm_1.png)

    ```python
    >>> domPossibA2 = (Bb3, G3, E3, C3)
    >>> resPossibA2 = resolution.dominantSeventhToMinorTonic(domPossibA2)
    >>> ', '.join([str(p) for p in resPossibA2])
    'A-3, F3, F3, F3'
    >>> resolution.showResolutions(domPossibA2, resPossibA2)
    ```

    [![../_images/fbResolution_V7toIm_2.png](../_images/fbResolution_V7toIm_2.png)](../_images/fbResolution_V7toIm_2.png)

    ```python
    >>> domPossibA3 = (E5, Bb4, C4, G3)
    >>> resPossibA3a = resolution.dominantSeventhToMinorTonic(domPossibA3, False)
    >>> [str(p) for p in resPossibA3a]
    ['F5', 'A-4', 'C4', 'F3']
    >>> resPossibA3b = resolution.dominantSeventhToMinorTonic(domPossibA3, True)
    >>> [str(p) for p in resPossibA3b]
    ['F5', 'C5', 'C4', 'A-3']
    >>> resolution.showResolutions(domPossibA3, resPossibA3a, domPossibA3, resPossibA3b)
    ```

    [![../_images/fbResolution_V7toIm_3.png](../_images/fbResolution_V7toIm_3.png)](../_images/fbResolution_V7toIm_3.png)

music21.figuredBass.resolution.dominantSeventhToMajorSubmediant(*domPossib*, *domChordInfo=None*)[[source]](../_modules/music21/figuredBass/resolution.html#dominantSeventhToMajorSubmediant)
:   Resolves a dominant seventh chord in root position to the
    major submediant (VI) in root position.

    ```python
    >>> from music21.figuredBass import resolution
    >>> G2 = pitch.Pitch('G2')
    >>> B3 = pitch.Pitch('B3')
    >>> F4 = pitch.Pitch('F4')
    >>> D5 = pitch.Pitch('D5')
    >>> domPossibA1 = (D5, F4, B3, G2)
    >>> resPossibA1 = resolution.dominantSeventhToMajorSubmediant(domPossibA1)
    >>> [p.nameWithOctave for p in resPossibA1]
    ['C5', 'E-4', 'C4', 'A-2']
    >>> resolution.showResolutions(domPossibA1, resPossibA1)
    ```

    [![../_images/fbResolution_V7toVI.png](../_images/fbResolution_V7toVI.png)](../_images/fbResolution_V7toVI.png)

music21.figuredBass.resolution.dominantSeventhToMinorSubmediant(*domPossib*, *domChordInfo=None*)[[source]](../_modules/music21/figuredBass/resolution.html#dominantSeventhToMinorSubmediant)
:   Resolves a dominant seventh chord in root position to the
    minor submediant (vi) in root position.

    ```python
    >>> from music21.figuredBass import resolution
    >>> G2 = pitch.Pitch('G2')
    >>> B3 = pitch.Pitch('B3')
    >>> F4 = pitch.Pitch('F4')
    >>> D5 = pitch.Pitch('D5')
    >>> domPossibA1 = (D5, F4, B3, G2)
    >>> resPossibA1 = resolution.dominantSeventhToMinorSubmediant(domPossibA1)
    >>> [p.nameWithOctave for p in resPossibA1]
    ['C5', 'E4', 'C4', 'A2']
    >>> resolution.showResolutions(domPossibA1, resPossibA1)
    ```

    [![../_images/fbResolution_V7toVIm.png](../_images/fbResolution_V7toVIm.png)](../_images/fbResolution_V7toVIm.png)

music21.figuredBass.resolution.dominantSeventhToMajorSubdominant(*domPossib*, *domChordInfo=None*)[[source]](../_modules/music21/figuredBass/resolution.html#dominantSeventhToMajorSubdominant)
:   Resolves a dominant seventh chord in root position
    to the major subdominant (IV) in first inversion.

    ```python
    >>> from music21.figuredBass import resolution
    >>> G2 = pitch.Pitch('G2')
    >>> B3 = pitch.Pitch('B3')
    >>> F4 = pitch.Pitch('F4')
    >>> D5 = pitch.Pitch('D5')
    >>> domPossibA1 = (D5, F4, B3, G2)
    >>> resPossibA1 = resolution.dominantSeventhToMajorSubdominant(domPossibA1)
    >>> [p.nameWithOctave for p in resPossibA1]
    ['C5', 'F4', 'C4', 'A2']
    >>> resolution.showResolutions(domPossibA1, resPossibA1)
    ```

    [![../_images/fbResolution_V7toIV.png](../_images/fbResolution_V7toIV.png)](../_images/fbResolution_V7toIV.png)

music21.figuredBass.resolution.dominantSeventhToMinorSubdominant(*domPossib*, *domChordInfo=None*)[[source]](../_modules/music21/figuredBass/resolution.html#dominantSeventhToMinorSubdominant)
:   Resolves a dominant seventh chord in root position
    to the minor subdominant (iv) in first inversion.

    ```python
    >>> from music21.figuredBass import resolution
    >>> G2 = pitch.Pitch('G2')
    >>> B3 = pitch.Pitch('B3')
    >>> F4 = pitch.Pitch('F4')
    >>> D5 = pitch.Pitch('D5')
    >>> domPossibA1 = (D5, F4, B3, G2)
    >>> resPossibA1 = resolution.dominantSeventhToMinorSubdominant(domPossibA1)
    >>> [p.nameWithOctave for p in resPossibA1]
    ['C5', 'F4', 'C4', 'A-2']
    >>> resolution.showResolutions(domPossibA1, resPossibA1)
    ```

    [![../_images/fbResolution_V7toIVm.png](../_images/fbResolution_V7toIVm.png)](../_images/fbResolution_V7toIVm.png)

music21.figuredBass.resolution.diminishedSeventhToMajorTonic(*dimPossib*, *doubledRoot=False*, *dimChordInfo=None*)[[source]](../_modules/music21/figuredBass/resolution.html#diminishedSeventhToMajorTonic)
:   Resolves a fully diminished seventh chord to the major tonic,
    in root position or either inversion.

    The resolution of the diminished seventh chord can have a
    doubled third (standard resolution) or a doubled root
    (alternate resolution), because the third of the diminished
    chord can either rise or fall. The desired resolution is
    attained using doubledRoot, and is set by
    [`resolveDiminishedSeventhSegment()`](moduleFiguredBassSegment.html#music21.figuredBass.segment.Segment.resolveDiminishedSeventhSegment "music21.figuredBass.segment.Segment.resolveDiminishedSeventhSegment").

    ```python
    >>> from music21.figuredBass import resolution
    >>> Cs3 = pitch.Pitch('C#3')
    >>> G3 = pitch.Pitch('G3')
    >>> E4 = pitch.Pitch('E4')
    >>> Bb4 = pitch.Pitch('B-4')
    >>> dimPossibA = (Bb4, E4, G3, Cs3)
    >>> resPossibAa = resolution.diminishedSeventhToMajorTonic(dimPossibA, False)
    >>> [str(p) for p in resPossibAa]
    ['A4', 'F#4', 'F#3', 'D3']
    >>> resPossibAb = resolution.diminishedSeventhToMajorTonic(dimPossibA, True)
    >>> [p.nameWithOctave for p in resPossibAb]
    ['A4', 'D4', 'F#3', 'D3']
    >>> resolution.showResolutions(dimPossibA, resPossibAa, dimPossibA, resPossibAb)
    ```

    [![../_images/fbResolution_vii7toI.png](../_images/fbResolution_vii7toI.png)](../_images/fbResolution_vii7toI.png)

music21.figuredBass.resolution.diminishedSeventhToMinorTonic(*dimPossib*, *doubledRoot=False*, *dimChordInfo=None*)[[source]](../_modules/music21/figuredBass/resolution.html#diminishedSeventhToMinorTonic)
:   Resolves a fully diminished seventh chord to the minor tonic,
    in root position or either inversion.

    The resolution of the diminished seventh chord can have a
    doubled third (standard resolution) or a doubled root
    (alternate resolution), because the third of the diminished
    chord can either rise or fall. The desired resolution is
    attained using doubledRoot, and is set by
    [`resolveDiminishedSeventhSegment()`](moduleFiguredBassSegment.html#music21.figuredBass.segment.Segment.resolveDiminishedSeventhSegment "music21.figuredBass.segment.Segment.resolveDiminishedSeventhSegment").

    ```python
    >>> from music21.figuredBass import resolution
    >>> Cs3 = pitch.Pitch('C#3')
    >>> G3 = pitch.Pitch('G3')
    >>> E4 = pitch.Pitch('E4')
    >>> Bb4 = pitch.Pitch('B-4')
    >>> dimPossibA = (Bb4, E4, G3, Cs3)
    >>> resPossibAa = resolution.diminishedSeventhToMinorTonic(dimPossibA, False)
    >>> [p.nameWithOctave for p in resPossibAa]
    ['A4', 'F4', 'F3', 'D3']
    >>> resPossibAb = resolution.diminishedSeventhToMinorTonic(dimPossibA, True)
    >>> [p.nameWithOctave for p in resPossibAb]
    ['A4', 'D4', 'F3', 'D3']
    >>> resolution.showResolutions(dimPossibA, resPossibAa, dimPossibA, resPossibAb)
    ```

    [![../_images/fbResolution_vii7toIm.png](../_images/fbResolution_vii7toIm.png)](../_images/fbResolution_vii7toIm.png)

music21.figuredBass.resolution.diminishedSeventhToMajorSubdominant(*dimPossib*, *dimChordInfo=None*)[[source]](../_modules/music21/figuredBass/resolution.html#diminishedSeventhToMajorSubdominant)
:   Resolves a fully diminished seventh chord to the
    major subdominant (IV).

    ```python
    >>> from music21.figuredBass import resolution
    >>> Cs3 = pitch.Pitch('C#3')
    >>> G3 = pitch.Pitch('G3')
    >>> E4 = pitch.Pitch('E4')
    >>> Bb4 = pitch.Pitch('B-4')
    >>> dimPossibA = (Bb4, E4, G3, Cs3)
    >>> resPossibA = resolution.diminishedSeventhToMajorSubdominant(dimPossibA)
    >>> [str(p) for p in resPossibA]
    ['B4', 'D4', 'G3', 'D3']
    >>> resolution.showResolutions(dimPossibA, resPossibA)
    ```

    [![../_images/fbResolution_vii7toIV.png](../_images/fbResolution_vii7toIV.png)](../_images/fbResolution_vii7toIV.png)

music21.figuredBass.resolution.diminishedSeventhToMinorSubdominant(*dimPossib*, *dimChordInfo=None*)[[source]](../_modules/music21/figuredBass/resolution.html#diminishedSeventhToMinorSubdominant)
:   Resolves a fully diminished seventh chord to the
    minor subdominant (iv).

    ```python
    >>> from music21.figuredBass import resolution
    >>> Cs3 = pitch.Pitch('C#3')
    >>> G3 = pitch.Pitch('G3')
    >>> E4 = pitch.Pitch('E4')
    >>> Bb4 = pitch.Pitch('B-4')
    >>> dimPossibA = (Bb4, E4, G3, Cs3)
    >>> resPossibA = resolution.diminishedSeventhToMinorSubdominant(dimPossibA)
    >>> [str(p) for p in resPossibA]
    ['B-4', 'D4', 'G3', 'D3']
    >>> resolution.showResolutions(dimPossibA, resPossibA)
    ```

    [![../_images/fbResolution_vii7toIVm.png](../_images/fbResolution_vii7toIVm.png)](../_images/fbResolution_vii7toIVm.png)

music21.figuredBass.resolution.showResolutions(*\*allPossib*)[[source]](../_modules/music21/figuredBass/resolution.html#showResolutions)
:   Takes in possibilities as arguments and adds them in order
    to a `Score` which is then displayed
    in external software.
