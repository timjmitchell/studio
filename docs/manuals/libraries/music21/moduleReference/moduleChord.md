Source: https://music21.org/music21docs/moduleReference/moduleChord.html

# music21.chord

This module defines the Chord object, a subclass of [`GeneralNote`](moduleNote.html#music21.note.GeneralNote "music21.note.GeneralNote")
as well as other methods, functions, and objects related to chords.

## Chord

class music21.chord.Chord(*notes: [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")] | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[Note](moduleNote.html#music21.note.Note "music21.note.Note")] | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[Chord](#music21.chord.Chord "music21.chord.Chord")] | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] = None*, *\*\*keywords*)[[source]](../_modules/music21/chord.html#Chord)
:   Class representing Chords.

    A Chord functions like a Note object but has multiple pitches.

    Create chords by passing a list of strings of pitch names:

    ```python
    >>> dMaj = chord.Chord(['D', 'F#', 'A'])
    >>> dMaj
    <music21.chord.Chord D F# A>
    ```

    Pitch names can also include octaves:

    ```python
    >>> dMaj = chord.Chord(['D3', 'F#4', 'A5'])
    >>> dMaj
    <music21.chord.Chord D3 F#4 A5>
    ```

    A single string with note names separated by spaces also works:

    ```python
    >>> myChord = chord.Chord('A4 C#5 E5')
    >>> myChord
    <music21.chord.Chord A4 C#5 E5>
    ```

    Or you can combine already created Notes or Pitches:

    ```python
    >>> cNote = note.Note('C')
    >>> eNote = note.Note('E')
    >>> gNote = note.Note('G')
    ```

    And then create a chord with note objects:

    ```python
    >>> cmaj = chord.Chord([cNote, eNote, gNote])
    >>> cmaj  # default octave of 4 is used for these notes, since octave was not specified
    <music21.chord.Chord C E G>
    ```

    Or with pitches:

    ```python
    >>> cmaj2 = chord.Chord([pitch.Pitch('C'), pitch.Pitch('E'), pitch.Pitch('G')])
    >>> cmaj2
    <music21.chord.Chord C E G>
    ```

    Chord has the ability to determine the root of a chord, as well as the bass note of a chord.
    In addition, Chord is capable of determining what type of chord a particular chord is, whether
    it is a triad or a seventh, major or minor, etc., as well as what inversion the chord is in.

    A chord can also be created from pitch class numbers:

    ```python
    >>> c = chord.Chord([0, 2, 3, 5])
    >>> c.pitches
    (<music21.pitch.Pitch C>,
     <music21.pitch.Pitch D>,
     <music21.pitch.Pitch E->,
     <music21.pitch.Pitch F>)
    ```

    Or from MIDI numbers:

    ```python
    >>> c = chord.Chord([72, 76, 79])
    >>> c.pitches
    (<music21.pitch.Pitch C5>, <music21.pitch.Pitch E5>, <music21.pitch.Pitch G5>)
    ```

    (If the number is < 12, it is assumed to be an octaveless pitch-class number, if above
    12, then a MIDI number. To create chords below MIDI 12, create a Pitch object with that
    MIDI number instead and then pass that to the Chord creator).

    Duration or quarterLength also works:

    ```python
    >>> d = duration.Duration(2.0)
    >>> myChord = chord.Chord('A4 C#5 E5', duration=d)
    >>> myChord
    <music21.chord.Chord A4 C#5 E5>
    >>> myChord.duration
    <music21.duration.Duration 2.0>
    >>> myChord.duration is d
    True
    ```

    ```python
    >>> myChord = chord.Chord('A4 C#5 E5', quarterLength=3.75)
    >>> myChord.duration.type
    'half'
    >>> myChord.duration.dots
    3
    ```

[`Chord`](#music21.chord.Chord "music21.chord.Chord") bases

* [`ChordBase`](#music21.chord.ChordBase "music21.chord.ChordBase")
* [`NotRest`](moduleNote.html#music21.note.NotRest "music21.note.NotRest")
* [`GeneralNote`](moduleNote.html#music21.note.GeneralNote "music21.note.GeneralNote")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`Chord`](#music21.chord.Chord "music21.chord.Chord") read-only properties

Chord.chordTablesAddress
:   Return a four-element ChordTableAddress that represents that raw data location for
    information on the set class interpretation of this Chord as well as the original
    pitchClass

    The data format is a Forte set class cardinality, index number, and
    inversion status (where 0 is invariant, and -1 and 1 represent
    inverted or not, respectively).

    ```python
    >>> c = chord.Chord(['D4', 'F#4', 'B-4'])
    >>> c.chordTablesAddress
    ChordTableAddress(cardinality=3, forteClass=12, inversion=0, pcOriginal=2)
    ```

    ```python
    >>> c = chord.Chord('G#2 A2 D3 G3')
    >>> c.chordTablesAddress
    ChordTableAddress(cardinality=4, forteClass=6, inversion=0, pcOriginal=2)
    ```

    This method caches the result so that it does not need to be looked up again.

    One change from chord.tables.seekChordTablesAddress: the empty chord returns
    a special address instead of raising an exception:

    ```python
    >>> chord.Chord().chordTablesAddress
    ChordTableAddress(cardinality=0, forteClass=0, inversion=0, pcOriginal=0)
    ```

Chord.commonName
:   Return the most common name associated with this Chord as a string.
    Checks some common enharmonic equivalents.

    ```python
    >>> c1 = chord.Chord(['c', 'e-', 'g'])
    >>> c1.commonName
    'minor triad'
    ```

    ```python
    >>> c2 = chord.Chord(['c', 'e', 'g'])
    >>> c2.commonName
    'major triad'
    ```

    ```python
    >>> c2b = chord.Chord(['c', 'f-', 'g'])
    >>> c2b.commonName
    'enharmonic equivalent to major triad'
    ```

    ```python
    >>> c3 = chord.Chord(['c', 'd-', 'e', 'f#'])
    >>> c3.commonName
    'all-interval tetrachord'
    ```

    Chords with no common names just return the Forte Class

    ```python
    >>> c3 = chord.Chord([0, 1, 2, 3, 4, 9])
    >>> c3.commonName
    'forte class 6-36B'
    ```

    Dominant seventh and German/Swiss sixths are distinguished

    ```python
    >>> c4a = chord.Chord(['c', 'e', 'g', 'b-'])
    >>> c4a.commonName
    'dominant seventh chord'
    ```

    ```python
    >>> c4b = chord.Chord(['c', 'e', 'g', 'a#'])
    >>> c4b.commonName
    'German augmented sixth chord'
    ```

    ```python
    >>> c4c = chord.Chord(['c', 'e', 'f##', 'a#'])
    >>> c4c.commonName  # some call it Alsacian or English
    'Swiss augmented sixth chord'
    ```

    When in an unusual inversion, augmented sixth chords have their inversion added:

    ```python
    >>> c4b = chord.Chord('A#3 C4 E4 G4')
    >>> c4b.commonName
    'German augmented sixth chord in root position'
    ```

    Dyads are called by actual name:

    ```python
    >>> dyad1 = chord.Chord('C E')
    >>> dyad1.commonName
    'Major Third'
    >>> dyad2 = chord.Chord('C F-')
    >>> dyad2.commonName
    'Diminished Fourth'
    ```

    Compound intervals are given in full if there are only two distinct pitches:

    ```python
    >>> dyad1 = chord.Chord('C4 E5')
    >>> dyad1.commonName
    'Major Tenth'
    ```

    But if there are more pitches, then the interval is given in a simpler form:

    ```python
    >>> dyad1 = chord.Chord('C4 C5 E5 C6')
    >>> dyad1.commonName
    'Major Third with octave doublings'
    ```

    If there are multiple enharmonics present just the simple
    number of semitones is returned.

    ```python
    >>> dyad1 = chord.Chord('C4 E5 F-5 B#7')
    >>> dyad1.commonName
    '4 semitones'
    ```

    Special handling of one- and two-pitchClass chords:

    ```python
    >>> gAlone = chord.Chord(['G4'])
    >>> gAlone.commonName
    'note'
    >>> gAlone = chord.Chord('G4 G4')
    >>> gAlone.commonName
    'unison'
    >>> gAlone = chord.Chord('G4 G5')
    >>> gAlone.commonName
    'Perfect Octave'
    >>> gAlone = chord.Chord('G4 G6')
    >>> gAlone.commonName
    'Perfect Double-octave'
    >>> gAlone = chord.Chord('G4 G5 G6')
    >>> gAlone.commonName
    'multiple octaves'
    >>> gAlone = chord.Chord('F#4 G-4')
    >>> gAlone.commonName
    'enharmonic unison'
    ```

    ```python
    >>> chord.Chord().commonName
    'empty chord'
    ```

    Microtonal chords all have the same commonName:

    ```python
    >>> chord.Chord('C`4 D~4').commonName
    'microtonal chord'
    ```

    Enharmonic equivalents to common sevenths and ninths are clarified:

    ```python
    >>> chord.Chord('C4 E4 G4 A##4').commonName
    'enharmonic equivalent to major seventh chord'
    ```

    ```python
    >>> chord.Chord('C4 E-4 G4 A#4 D4').commonName
    'enharmonic equivalent to minor-ninth chord'
    ```

    * Changed in v5.5: special cases for checking enharmonics in some cases
    * Changed in v6.5: better handling of 0-, 1-, and 2-pitchClass and microtonal chords.
    * Changed in v7: Inversions of augmented sixth-chords are specified.
    * Changed in v7.3: Enharmonic equivalents to common seventh and ninth chords are specified.

Chord.fifth
:   Shortcut for getChordStep(5), but caches it and does not raise exceptions

    ```python
    >>> cMaj1stInv = chord.Chord(['E3', 'C4', 'G5'])
    >>> cMaj1stInv.fifth
    <music21.pitch.Pitch G5>
    ```

    ```python
    >>> cMaj1stInv.fifth.midi
    79
    ```

    ```python
    >>> chord.Chord('C4 D4').fifth is None
    True
    ```

Chord.forteClass
:   Return the Forte set class name as a string. This assumes a Tn
    formation, where inversion distinctions are represented.

    (synonym: forteClassTn)

    ```python
    >>> c1 = chord.Chord(['c', 'e-', 'g'])
    >>> c1.forteClass
    '3-11A'
    ```

    ```python
    >>> c2 = chord.Chord(['c', 'e', 'g'])
    >>> c2.forteClass
    '3-11B'
    ```

    Empty chords return ‘N/A’

    ```python
    >>> chord.Chord().forteClass
    'N/A'
    ```

    Non-twelve-tone chords return as if all microtones and non-twelve-tone
    accidentals are removed:

    ```python
    >>> chord.Chord('c~4 d`4').forteClass
    '2-2'
    ```

Chord.forteClassNumber
:   Return the number of the Forte set class within the defined set group.
    That is, if the set is 3-11, this method returns 11.

    ```python
    >>> c1 = chord.Chord(['c', 'e-', 'g'])
    >>> c1.forteClassNumber
    11
    ```

    ```python
    >>> c2 = chord.Chord(['c', 'e', 'g'])
    >>> c2.forteClassNumber
    11
    ```

Chord.forteClassTn
:   A synonym for “forteClass”

    Return the Forte Tn set class name, where inversion distinctions are
    represented:

    ```python
    >>> c1 = chord.Chord(['c', 'e-', 'g'])
    >>> c1.forteClass
    '3-11A'
    ```

    ```python
    >>> c2 = chord.Chord(['c', 'e', 'g'])
    >>> c2.forteClassTn
    '3-11B'
    ```

Chord.forteClassTnI
:   Return the Forte TnI class name, where inversion distinctions are not
    represented.

    ```python
    >>> c1 = chord.Chord(['c', 'e-', 'g'])
    >>> c1.forteClassTnI
    '3-11'
    ```

    ```python
    >>> c2 = chord.Chord(['c', 'e', 'g'])
    >>> c2.forteClassTnI
    '3-11'
    ```

    Empty chords return ‘N/A’

    ```python
    >>> chord.Chord().forteClassTnI
    'N/A'
    ```

    Non-twelve-tone chords return as if all microtones and non-twelve-tone
    accidentals are removed:

    ```python
    >>> chord.Chord('c~4 d`4').forteClassTnI
    '2-2'
    ```

Chord.fullName
:   Return the most complete representation of this Note, providing
    duration and pitch information.

    ```python
    >>> c = chord.Chord(['D', 'F#', 'A'])
    >>> c.fullName
    'Chord {D | F-sharp | A} Quarter'
    ```

    ```python
    >>> chord.Chord(['d1', 'e4-', 'b3-'], quarterLength=2/3).fullName
    'Chord {D in octave 1 | E-flat in octave 4 | B-flat in octave 3} Quarter Triplet (2/3 QL)'
    ```

Chord.hasZRelation
:   Return True or False if the Chord has a Z-relation.

    ```python
    >>> c1 = chord.Chord(['c', 'e-', 'g'])
    >>> c1.hasZRelation
    False
    ```

    ```python
    >>> c2 = chord.Chord(['c', 'c#', 'e', 'f#'])
    >>> c2.hasZRelation  # it is c, c#, e-, g
    True
    ```

Chord.intervalVector
:   Return the interval vector for this Chord as a list of integers.

    ```python
    >>> c1 = chord.Chord(['c', 'e-', 'g'])
    >>> c1.intervalVector
    [0, 0, 1, 1, 1, 0]
    ```

    ```python
    >>> c2 = chord.Chord(['c', 'c#', 'e', 'f#'])
    >>> c2.intervalVector
    [1, 1, 1, 1, 1, 1]
    ```

    ```python
    >>> c3 = chord.Chord(['c', 'c#', 'e-', 'g'])
    >>> c3.intervalVector
    [1, 1, 1, 1, 1, 1]
    ```

Chord.intervalVectorString
:   Return the interval vector as a string representation.

    ```python
    >>> c1 = chord.Chord(['c', 'e-', 'g'])
    >>> c1.intervalVectorString
    '<001110>'
    ```

Chord.isPrimeFormInversion
:   Return True or False if the Chord represents a set class inversion.

    ```python
    >>> c1 = chord.Chord(['c', 'e-', 'g'])
    >>> c1.isPrimeFormInversion
    False
    ```

    ```python
    >>> c2 = chord.Chord(['c', 'e', 'g'])
    >>> c2.isPrimeFormInversion
    True
    ```

Chord.multisetCardinality
:   Return an integer representing the cardinality of the multiset, or the
    number of pitch values.

    ```python
    >>> c1 = chord.Chord(['D4', 'A4', 'F#5', 'D6'])
    >>> c1.multisetCardinality
    4
    ```

Chord.normalOrder
:   Return the normal order/normal form of the Chord represented as a list of integers:

    ```python
    >>> c1 = chord.Chord(['c', 'e-', 'g'])
    >>> c1.normalOrder
    [0, 3, 7]
    ```

    ```python
    >>> c2 = chord.Chord(['c', 'e', 'g'])
    >>> c2.normalOrder
    [0, 4, 7]
    ```

    ```python
    >>> c3 = chord.Chord(['d', 'f#', 'a'])
    >>> c3.normalOrder
    [2, 6, 9]
    ```

    ```python
    >>> c3 = chord.Chord(['B-4', 'D5', 'F5'])
    >>> c3.normalOrder
    [10, 2, 5]
    ```

    To get normalOrder transposed to PC 0, do this:

    ```python
    >>> c3 = chord.Chord(['B-4', 'D5', 'F5'])
    >>> normalOrder = c3.normalOrder
    >>> firstPitch = normalOrder[0]
    >>> [(pc - firstPitch) % 12 for pc in normalOrder]
    [0, 4, 7]
    ```

    To get normalOrder formatted as a vectorString run .formatVectorString on it:

    ```python
    >>> c3.normalOrder
    [10, 2, 5]
    ```

    ```python
    >>> chord.Chord.formatVectorString(c3.normalOrder)
    '<A25>'
    ```

    (this is equivalent:)

    ```python
    >>> c3.formatVectorString(c3.normalOrder)
    '<A25>'
    ```

Chord.normalOrderString
:   Return the normal order/normal form of the Chord as a string representation.

    ```python
    >>> c1 = chord.Chord(['c', 'e-', 'g'])
    >>> c1.normalOrder
    [0, 3, 7]
    ```

    ```python
    >>> c1.normalOrderString
    '<037>'
    ```

Chord.orderedPitchClasses
:   Return a list of pitch class integers, ordered form lowest to highest.

    ```python
    >>> c1 = chord.Chord(['D4', 'A4', 'F#5', 'D6'])
    >>> c1.orderedPitchClasses
    [2, 6, 9]
    ```

Chord.orderedPitchClassesString
:   Return a string representation of the pitch class values.

    ```python
    >>> c1 = chord.Chord(['f#', 'e-', 'g'])
    >>> c1.orderedPitchClassesString
    '<367>'
    ```

    Redundancies are removed

    ```python
    >>> c1 = chord.Chord(['f#', 'e-', 'e-', 'g'])
    >>> c1.orderedPitchClassesString
    '<367>'
    ```

Chord.pitchClassCardinality
:   Return the cardinality of pitch classes, or the number of unique
    pitch classes, in the Chord:

    ```python
    >>> c1 = chord.Chord(['D4', 'A4', 'F#5', 'D6'])
    >>> c1.pitchClassCardinality
    3
    ```

Chord.pitchClasses
:   Return a list of all pitch classes in the chord as integers. Not sorted

    ```python
    >>> c1 = chord.Chord(['D4', 'A4', 'F#5', 'D6'])
    >>> c1.pitchClasses
    [2, 9, 6, 2]
    ```

Chord.pitchedCommonName
:   Return a common name of this Chord including a pitch identifier, if possible:

    Most common chords will use the root as the pitch name and have it at the beginning:

    ```python
    >>> c1 = chord.Chord(['c', 'e-', 'g'])
    >>> c1.pitchedCommonName
    'C-minor triad'
    ```

    ```python
    >>> c2 = chord.Chord(['c', 'e', 'g'])
    >>> c2.pitchedCommonName
    'C-major triad'
    ```

    Because the hyphen is confusing w/ music21 flat notation, flats are displayed
    as “b”:

    ```python
    >>> c2a = chord.Chord('C-2 E-2 G-2')
    >>> c2a.pitchedCommonName
    'Cb-major triad'
    ```

    Other forms might have the pitch elsewhere. Thus, this is a method for display,
    not for extracting information:

    ```python
    >>> c3 = chord.Chord('A#2 D3 F3')
    >>> c3.pitchedCommonName
    'enharmonic equivalent to major triad above A#'
    ```

    Note that in this case, the bass, not the root is used to determine the pitch name:

    ```python
    >>> c4 = chord.Chord('D3 F3 A#3')
    >>> c4.pitchedCommonName
    'enharmonic equivalent to major triad above D'
    ```

    ```python
    >>> c5 = chord.Chord([1, 2, 3, 4, 5, 10])
    >>> c5.pitchedCommonName
    'forte class 6-36B above C#'
    ```

    ```python
    >>> c4 = chord.Chord('D3 F3 A#3')
    >>> c4.pitchedCommonName
    'enharmonic equivalent to major triad above D'
    ```

    A single pitch just returns that pitch name:

    ```python
    >>> chord.Chord(['D3']).pitchedCommonName
    'D'
    ```

    Unless there is more than one octave:

    ```python
    >>> chord.Chord('D3 D4').pitchedCommonName
    'Perfect Octave above D'
    >>> chord.Chord('D3 D4 D5').pitchedCommonName
    'multiple octaves above D'
    ```

    Two different pitches give interval names:

    ```python
    >>> chord.Chord('F3 C4').pitchedCommonName
    'Perfect Fifth above F'
    ```

    Compound intervals are used unless there are multiple octaves:

    ```python
    >>> chord.Chord('E-3 C5').pitchedCommonName
    'Major Thirteenth above Eb'
    >>> chord.Chord('E-3 C5 C6').pitchedCommonName
    'Major Sixth with octave doublings above Eb'
    ```

    These one-pitch-class and two-pitch-class chords with multiple enharmonics are unusual:

    ```python
    >>> chord.Chord('D#3 E-3').pitchedCommonName
    'enharmonic unison above D#'
    >>> chord.Chord('D#3 E-3 D#4').pitchedCommonName
    'enharmonic octaves above D#'
    >>> chord.Chord('D#3 E-3 E3').pitchedCommonName
    '1 semitone above D#'
    >>> chord.Chord('D#3 E-3 F3 G--4').pitchedCommonName
    '2 semitones above D#'
    ```

    ```python
    >>> chord.Chord().pitchedCommonName
    'empty chord'
    ```

    * Changed in v5.5: octaves never included, flats are converted,
      special tools for enharmonics.
    * Changed in v6.5: special names for 0-, 1-, and 2-pitchClass chords.

Chord.primeForm
:   Return a representation of the Chord as a prime-form list of pitch
    class integers:

    ```python
    >>> c1 = chord.Chord(['c', 'e-', 'g'])
    >>> c1.primeForm
    [0, 3, 7]
    ```

    ```python
    >>> c2 = chord.Chord(['c', 'e', 'g'])
    >>> c2.primeForm
    [0, 3, 7]
    ```

Chord.primeFormString
:   Return a representation of the Chord as a prime-form set class string.

    ```python
    >>> c1 = chord.Chord(['c', 'e-', 'g'])
    >>> c1.primeFormString
    '<037>'
    ```

    ```python
    >>> c1 = chord.Chord(['c', 'e', 'g'])
    >>> c1.primeFormString
    '<037>'
    ```

Chord.quality
:   Returns the quality of the underlying triad of a triad or
    seventh, either major, minor, diminished, augmented, or other:

    ```python
    >>> a = chord.Chord(['a', 'c', 'e'])
    >>> a.quality
    'minor'
    ```

    Inversions don’t matter, nor do added tones so long as a root can be
    found:

    ```python
    >>> a = chord.Chord(['f', 'b', 'd', 'g'])
    >>> a.quality
    'major'
    ```

    ```python
    >>> a = chord.Chord(['c', 'a-', 'e'])
    >>> a.quality
    'augmented'
    ```

    ```python
    >>> a = chord.Chord(['c', 'c#', 'd'])
    >>> a.quality
    'other'
    ```

    Incomplete triads are returned as major or minor:

    ```python
    >>> a = chord.Chord(['c', 'e-'])
    >>> a.quality
    'minor'
    ```

    ```python
    >>> a = chord.Chord(['e-', 'g'])
    >>> a.quality
    'major'
    ```

    Chords that contain more than one triad return ‘other’

    ```python
    >>> chord.Chord('C C# E G').quality
    'other'
    >>> chord.Chord('C E- E G').quality
    'other'
    >>> chord.Chord('C E G- G').quality
    'other'
    ```

    Note these two edge cases:

    ```python
    >>> chord.Chord('C D E').quality  # NB! Major 9th.
    'major'
    >>> chord.Chord('C E--').quality
    'other'
    ```

    Empty chords are definitely ‘other’:

    ```python
    >>> chord.Chord().quality
    'other'
    ```

Chord.scaleDegrees
:   Returns a list of two-element tuples for each pitch in the chord where
    the first element of the tuple is the scale degree as an int and the
    second is an Accidental object that specifies the alteration from the
    scale degree (could be None if the note is not part of the scale).

    It is easiest to see the utility of this method using a chord subclass,
    [`music21.roman.RomanNumeral`](moduleRoman.html#music21.roman.RomanNumeral "music21.roman.RomanNumeral"), but it is also callable from this
    Chord object if the Chord has a Key or Scale context set for it.

    ```python
    >>> k = key.Key('f#')  # 3-sharps minor
    >>> rn = roman.RomanNumeral('V', k)
    >>> rn.key
    <music21.key.Key of f# minor>
    ```

    ```python
    >>> rn.pitches
    (<music21.pitch.Pitch C#5>, <music21.pitch.Pitch E#5>, <music21.pitch.Pitch G#5>)
    ```

    ```python
    >>> rn.scaleDegrees
    [(5, None), (7, <music21.pitch.Accidental sharp>), (2, None)]
    ```

    ```python
    >>> rn2 = roman.RomanNumeral('N6', k)
    >>> rn2.pitches
    (<music21.pitch.Pitch B4>, <music21.pitch.Pitch D5>, <music21.pitch.Pitch G5>)
    ```

    ```python
    >>> rn2.scaleDegrees  # N.B. -- natural form used for minor!
    [(4, None), (6, None), (2, <music21.pitch.Accidental flat>)]
    ```

    As mentioned above, the property can also get its scale from context if
    the chord is embedded in a Stream. Let’s create the same V in f#-minor
    again, but give it a context of c-sharp minor, and then c-minor instead:

    ```python
    >>> chord1 = chord.Chord(['C#5', 'E#5', 'G#5'])
    >>> st1 = stream.Stream()
    >>> st1.append(key.Key('c#'))  # c-sharp minor
    >>> st1.append(chord1)
    >>> chord1.scaleDegrees
    [(1, None), (3, <music21.pitch.Accidental sharp>), (5, None)]
    ```

    ```python
    >>> st2 = stream.Stream()
    >>> chord2 = chord.Chord(['C#5', 'E#5', 'G#5'])
    >>> st2.append(key.Key('c'))  # c minor
    >>> st2.append(chord2)        # same pitches as before gives different scaleDegrees
    >>> chord2.scaleDegrees
    [(1, <music21.pitch.Accidental sharp>),
     (3, <music21.pitch.Accidental double-sharp>),
     (5, <music21.pitch.Accidental sharp>)]
    ```

    ```python
    >>> st3 = stream.Stream()
    >>> st3.append(key.Key('C'))  # C major
    >>> chord2 = chord.Chord(['C4', 'C#4', 'D4', 'E-4', 'E4', 'F4'])  # 1st 1/2 of chromatic
    >>> st3.append(chord2)
    >>> chord2.scaleDegrees
    [(1, None), (1, <music21.pitch.Accidental sharp>), (2, None),
     (3, <music21.pitch.Accidental flat>), (3, None), (4, None)]
    ```

    If no context can be found, return None:

    ```python
    >>> chord.Chord('C4 E4 G4').scaleDegrees is None
    True
    ```

    * Changed in v6.5: will return None if no context can be found:

Chord.seventh
:   Shortcut for getChordStep(7), but caches the value

    ```python
    >>> bDim7_2ndInv = chord.Chord(['F2', 'A-3', 'B4', 'D5'])
    >>> bDim7_2ndInv.seventh
    <music21.pitch.Pitch A-3>
    ```

    Test whether this strange chord gets the B# not the C or something else:

    ```python
    >>> c = chord.Chord(['C4', 'E4', 'G4', 'B#4'])
    >>> c.seventh
    <music21.pitch.Pitch B#4>
    ```

    * Changed in v6.5: return None on empty chords/errors

Chord.third
:   Shortcut for getChordStep(3), but caches the value, and returns
    None on errors.

    ```python
    >>> cMaj1stInv = chord.Chord(['E3', 'C4', 'G5'])
    >>> cMaj1stInv.third
    <music21.pitch.Pitch E3>
    ```

    ```python
    >>> cMaj1stInv.third.octave
    3
    ```

    * Changed in v6.5: return None on empty chords/errors

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`Chord`](#music21.chord.Chord "music21.chord.Chord") read/write properties

Chord.duration
:   Get or set the duration of this Chord as a Duration object.

    ```python
    >>> c = chord.Chord(['a', 'c', 'e'])
    >>> c.duration
    <music21.duration.Duration 1.0>
    ```

    Durations can be overridden after the fact:

    ```python
    >>> d = duration.Duration()
    >>> d.quarterLength = 2
    >>> c.duration = d
    >>> c.duration
    <music21.duration.Duration 2.0>
    ```

    ```python
    >>> c.duration == d
    True
    ```

    ```python
    >>> c.duration is d
    True
    ```

Chord.notes
:   Return a tuple (immutable) of the notes contained in the chord.

    Generally using .pitches or iterating over the chord is the best way to work with
    the components of a chord, but in unusual cases, a chord may, for instance, consist
    of notes with independent durations, volumes, or colors, or, more often, different tie
    statuses. Chord includes methods such as .setTie() for most of these features,
    but from time to time accessing all the Note objects as a tuple can be valuable.

    ```python
    >>> c1 = chord.Chord(['c', 'e-', 'g'])
    >>> c1.duration.type = 'quarter'
    >>> c1Notes = c1.notes
    >>> c1Notes
    (<music21.note.Note C>, <music21.note.Note E->, <music21.note.Note G>)
    ```

    Note that to set duration independently, a new Duration object needs to
    be created. Internal notes for Chords created from strings or pitches
    all share a Duration object.

    ```python
    >>> c1.duration is c1Notes[0].duration
    True
    >>> c1Notes[1].duration is c1Notes[2].duration
    True
    ```

    ```python
    >>> c1Notes[2].duration = duration.Duration('half')
    >>> c1.duration.type
    'quarter'
    >>> c1[2].duration.type
    'half'
    ```

    The property can also set the notes for a chord, but it must be
    set to an iterable of literal Note objects.

    ```python
    >>> c1.notes = [note.Note('D#4'), note.Note('C#4')]
    >>> c1
    <music21.chord.Chord D#4 C#4>
    ```

    Notice that the notes set this way are not sorted – this is a property for
    power users who want complete control.

    Any incorrect assignment raises a TypeError:

    ```python
    >>> c1.notes = 'C E G'
    Traceback (most recent call last):
    TypeError: notes must be set with an iterable
    ```

    ```python
    >>> c1.notes = [pitch.Pitch('C'), pitch.Pitch('E')]
    Traceback (most recent call last):
    TypeError: every element of notes must be a note.Note object
    ```

    In case of an error, the previous notes are not changed (for this reason,
    .notes cannot take a generator expression).

    ```python
    >>> c1
    <music21.chord.Chord D#4 C#4>
    ```

    * New in v5.7

Chord.pitchNames
:   Return a list of Pitch names from each
    [`Pitch`](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") object’s
    [`name`](modulePitch.html#music21.pitch.Pitch.name "music21.pitch.Pitch.name") attribute.

    ```python
    >>> c = chord.Chord(['g#', 'd-'])
    >>> c.pitchNames
    ['G#', 'D-']
    ```

    ```python
    >>> c = chord.Chord('C4 E4 G4 C4')
    >>> c.pitchNames
    ['C', 'E', 'G', 'C']
    ```

    ```python
    >>> c.pitchNames = ['c2', 'g2']
    >>> c.pitchNames
    ['C', 'G']
    ```

Chord.pitches
:   Get or set a list or tuple of all Pitch objects in this Chord.

    ```python
    >>> c = chord.Chord(['C4', 'E4', 'G#4'])
    >>> c.pitches
    (<music21.pitch.Pitch C4>, <music21.pitch.Pitch E4>, <music21.pitch.Pitch G#4>)
    ```

    ```python
    >>> [p.midi for p in c.pitches]
    [60, 64, 68]
    ```

    ```python
    >>> d = chord.Chord()
    >>> d.pitches = c.pitches
    >>> d.pitches
    (<music21.pitch.Pitch C4>, <music21.pitch.Pitch E4>, <music21.pitch.Pitch G#4>)
    ```

    ```python
    >>> c = chord.Chord(['C4', 'A4', 'E5'])
    >>> c.bass()
    <music21.pitch.Pitch C4>
    ```

    ```python
    >>> c.root()
    <music21.pitch.Pitch A4>
    ```

    Note here that the list will be converted to a tuple:

    ```python
    >>> c.pitches = ['C#4', 'A#4', 'E#5']
    >>> c.pitches
    (<music21.pitch.Pitch C#4>, <music21.pitch.Pitch A#4>, <music21.pitch.Pitch E#5>)
    ```

    Bass and root information is also changed.

    ```python
    >>> c.bass()
    <music21.pitch.Pitch C#4>
    ```

    ```python
    >>> c.root()
    <music21.pitch.Pitch A#4>
    ```

Read/write properties inherited from [`ChordBase`](#music21.chord.ChordBase "music21.chord.ChordBase"):

|  |  |  |
| --- | --- | --- |
| * [`tie`](#music21.chord.ChordBase.tie "music21.chord.ChordBase.tie") | * [`volume`](#music21.chord.ChordBase.volume "music21.chord.ChordBase.volume") |  |

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

[`Chord`](#music21.chord.Chord "music21.chord.Chord") methods

Chord.\_\_eq\_\_(*other*)[[source]](../_modules/music21/chord.html#Chord.__eq__)
:   Define equality for Music21Objects. See main class docs.

Chord.\_\_getitem\_\_(*key: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Note](moduleNote.html#music21.note.Note "music21.note.Note") | [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")*)[[source]](../_modules/music21/chord.html#Chord.__getitem__)
:   Get item makes accessing pitch components for the Chord easier

    ```python
    >>> c = chord.Chord('C#4 D-4')
    >>> cSharp = c[0]
    >>> cSharp
    <music21.note.Note C#>
    ```

    ```python
    >>> c['0.step']
    'C'
    >>> c['3.accidental']
    Traceback (most recent call last):
    KeyError: "Cannot access component with: '3.accidental'"
    ```

    ```python
    >>> c[5]
    Traceback (most recent call last):
    KeyError: 'Cannot access component with: 5'
    ```

    ```python
    >>> c['D-4']
    <music21.note.Note D->
    ```

    ```python
    >>> c['D-4.style.color'] is None
    True
    ```

    Getting by note does not do very much:

    ```python
    >>> c[cSharp]
    <music21.note.Note C#>
    ```

    But we can get from another note

    ```python
    >>> cSharp2 = note.Note('C#4')
    >>> cSharp2.duration.quarterLength = 3.0
    >>> c[cSharp2] is cSharp
    True
    >>> c[cSharp2] is cSharp2
    False
    ```

    KeyError is raised if not in chord.

    ```python
    >>> notInChord = note.Note('G')
    >>> c[notInChord]
    Traceback (most recent call last):
    KeyError: 'Cannot access component with: <music21.note.Note G>'
    ```

    ```python
    >>> c[None]
    Traceback (most recent call last):
    KeyError: 'Cannot access component with: None'
    ```

Chord.add(*notes*, *\**, *runSort=True*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/chord.html#Chord.add)
:   Add a Note, Pitch, the .notes of another chord,
    or string representing a pitch,
    or a list of any-of-the-above types to a Chord.

    If runSort is True (default=True) then after appending, the
    chord will be sorted.

    ```python
    >>> c = chord.Chord('C4 E4 G4')
    >>> c.add('B3')
    >>> c
    <music21.chord.Chord B3 C4 E4 G4>
    >>> c.duration
    <music21.duration.Duration 1.0>
    ```

    ```python
    >>> c.add('A2', runSort=False)
    >>> c
    <music21.chord.Chord B3 C4 E4 G4 A2>
    ```

    ```python
    >>> c.add(['B5', 'C6'])
    >>> c
    <music21.chord.Chord A2 B3 C4 E4 G4 B5 C6>
    ```

    ```python
    >>> c.add(pitch.Pitch('D6'))
    >>> c
    <music21.chord.Chord A2 B3 C4 E4 G4 B5 C6 D6>
    ```

    ```python
    >>> n = note.Note('E6')
    >>> n.duration.type = 'half'
    >>> c.add(n)
    >>> c
    <music21.chord.Chord A2 B3 C4 E4 G4 B5 C6 D6 E6>
    >>> c.duration
    <music21.duration.Duration 1.0>
    >>> c[-1]
    <music21.note.Note E>
    >>> c[-1].duration
    <music21.duration.Duration 2.0>
    ```

    Overrides ChordBase.add() to permit sorting with runSort.

Chord.annotateIntervals(*\**, *inPlace: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *stripSpecifiers: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *sortPitches: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *returnList: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[True]*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")][[source]](../_modules/music21/chord.html#Chord.annotateIntervals)

Chord.annotateIntervals(*\**, *inPlace: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[True]*, *stripSpecifiers: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *sortPitches: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *returnList: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[False] = False*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")

Chord.annotateIntervals(*\**, *inPlace: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[False] = False*, *stripSpecifiers: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *sortPitches: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *returnList: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[False] = False*) → [Self](https://docs.python.org/3/library/typing.html#typing.Self "(in Python v3.14)")
:   Add lyrics to the chord that show the distance of each note from
    the bass. If returnList is True, a list of the intervals is returned instead.

    By default, we show only the generic interval:

    ```python
    >>> c1 = chord.Chord(['C2', 'E2', 'G2', 'C3'])
    >>> c2 = c1.annotateIntervals(inPlace=False)
    >>> c2.lyrics
    [<music21.note.Lyric number=1 syllabic=single text='8'>,
     <music21.note.Lyric number=2 syllabic=single text='5'>,
     <music21.note.Lyric number=3 syllabic=single text='3'>]
    ```

    ```python
    >>> [ly.text for ly in c2.lyrics]
    ['8', '5', '3']
    ```

    The stripSpecifiers parameter can be used to show only the intervals size (3, 5, etc.)
    or the complete interval specification (m3, P5, etc.)

    ```python
    >>> c3 = c1.annotateIntervals(inPlace=False, stripSpecifiers=False)
    >>> c3.lyrics
    [<music21.note.Lyric number=1 syllabic=single text='P8'>,
     <music21.note.Lyric number=2 syllabic=single text='P5'>,
     <music21.note.Lyric number=3 syllabic=single text='M3'>]
    ```

    ```python
    >>> [ly.text for ly in c3.lyrics]
    ['P8', 'P5', 'M3']
    ```

    This chord was giving us problems:

    ```python
    >>> c4 = chord.Chord(['G4', 'E4', 'B3', 'E3'])
    >>> c4.annotateIntervals(inPlace=True, stripSpecifiers=False)
    >>> [ly.text for ly in c4.lyrics]
    ['m3', 'P8', 'P5']
    >>> c4.annotateIntervals(inPlace=True, stripSpecifiers=False, returnList=True)
    ['m3', 'P8', 'P5']
    ```

    If sortPitches is false it still gives problems:

    ```python
    >>> c4 = chord.Chord(['G4', 'E4', 'B3', 'E3'])
    >>> c4.annotateIntervals(inPlace=True, stripSpecifiers=False, sortPitches=False)
    >>> [ly.text for ly in c4.lyrics]
    ['m3', 'm6', 'm3']
    ```

    ```python
    >>> c = chord.Chord(['c4', 'd-4', 'g4'])
    >>> c.annotateIntervals(inPlace=True)
    >>> [ly.text for ly in c.lyrics]
    ['5', '2']
    ```

    ```python
    >>> c = chord.Chord(['c4', 'd-4', 'g4'])
    >>> c.annotateIntervals(inPlace=True, stripSpecifiers=False)
    >>> [ly.text for ly in c.lyrics]
    ['P5', 'm2']
    ```

    ```python
    >>> c = chord.Chord(['c4', 'd---4', 'g4'])
    >>> c.annotateIntervals(inPlace=True, stripSpecifiers=False)
    >>> [ly.text for ly in c.lyrics]
    ['P5', 'dd2']
    ```

    ```python
    >>> c = chord.Chord(['c4', 'g5', 'e6'])
    >>> c.annotateIntervals(inPlace=True)
    >>> [ly.text for ly in c.lyrics]
    ['5', '3']
    ```

Chord.areZRelations(*other: [Self](https://docs.python.org/3/library/typing.html#typing.Self "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/chord.html#Chord.areZRelations)
:   Check if another Chord is a z-relation to this Chord.

    ```python
    >>> c1 = chord.Chord(['C', 'c#', 'e', 'f#'])
    >>> c2 = chord.Chord(['C', 'c#', 'e-', 'g'])
    >>> c3 = chord.Chord(['C', 'c#', 'f#', 'g'])
    >>> c1.areZRelations(c2)
    True
    ```

    ```python
    >>> c1.areZRelations(c3)
    False
    ```

    If there is no z-relation for the first chord, obviously return False:

    ```python
    >>> c4 = chord.Chord('C E G')
    >>> c4.areZRelations(c3)
    False
    ```

Chord.bass(*newbass: [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\**, *find: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *allow\_add: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*) → [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")[[source]](../_modules/music21/chord.html#Chord.bass)

Chord.bass(*newbass: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") | [Note](moduleNote.html#music21.note.Note "music21.note.Note")*, *\**, *find: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *allow\_add: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
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

Chord.canBeDominantV() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/chord.html#Chord.canBeDominantV)
:   Returns True if the chord is a Major Triad or a Dominant Seventh:

    ```python
    >>> gSeven = chord.Chord(['g', 'b', 'd', 'f'])
    >>> gSeven.canBeDominantV()
    True
    ```

    ```python
    >>> gDim = chord.Chord(['g', 'b-', 'd-'])
    >>> gDim.canBeDominantV()
    False
    ```

Chord.canBeTonic() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/chord.html#Chord.canBeTonic)
:   Returns True if the chord is a major or minor triad:

    ```python
    >>> a = chord.Chord(['g', 'b', 'd', 'f'])
    >>> a.canBeTonic()
    False
    ```

    ```python
    >>> a = chord.Chord(['g', 'b', 'd'])
    >>> a.canBeTonic()
    True
    ```

Chord.closedPosition(*\**, *forceOctave: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *inPlace: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[True]*, *leaveRedundantPitches: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/chord.html#Chord.closedPosition)

Chord.closedPosition(*\**, *forceOctave: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *inPlace: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[False] = False*, *leaveRedundantPitches: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*) → [Self](https://docs.python.org/3/library/typing.html#typing.Self "(in Python v3.14)")
:   Returns a new Chord object with the same pitch classes,
    but now in closed position.

    If forcedOctave is provided, the bass of the chord will
    be shifted to that provided octave.

    If inPlace is True then the original chord is returned with new pitches.

    ```python
    >>> chord1 = chord.Chord(['C#4', 'G5', 'E6'])
    >>> chord2 = chord1.closedPosition()
    >>> chord2
    <music21.chord.Chord C#4 E4 G4>
    ```

    Force octave changes the octave of the bass note (and all notes above it)

    ```python
    >>> c2 = chord.Chord(['C#4', 'G5', 'E6'])
    >>> c2.closedPosition(forceOctave=2)
    <music21.chord.Chord C#2 E2 G2>
    ```

    ```python
    >>> c3 = chord.Chord(['C#4', 'G5', 'E6'])
    >>> c3.closedPosition(forceOctave=6)
    <music21.chord.Chord C#6 E6 G6>
    ```

    Redundant pitches are removed by default, but can be retained:

    ```python
    >>> c4 = chord.Chord(['C#4', 'C5', 'F7', 'F8'])
    >>> c5 = c4.closedPosition(forceOctave=4, inPlace=False)
    >>> c5
    <music21.chord.Chord C#4 F4 C5>
    ```

    ```python
    >>> c6 = c4.closedPosition(forceOctave=4, inPlace=False, leaveRedundantPitches=True)
    >>> c6
    <music21.chord.Chord C#4 F4 F4 C5>
    ```

    Implicit octaves work fine:

    ```python
    >>> c7 = chord.Chord(['A4', 'B4', 'A'])
    >>> c7.closedPosition(forceOctave=4, inPlace=True)
    >>> c7
    <music21.chord.Chord A4 B4>
    ```

Chord.containsSeventh() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/chord.html#Chord.containsSeventh)
:   Returns True if the chord contains at least one of each of Third, Fifth, and Seventh.
    raises an exception if the Root can’t be determined

    A ninth chord contains a seventh:

    ```python
    >>> c9 = chord.Chord(['C4', 'E4', 'G4', 'B4', 'D5'])
    >>> c9.containsSeventh()
    True
    ```

    As does a cluster:

    ```python
    >>> cluster = chord.Chord('C D E F G A B')
    >>> cluster.containsSeventh()
    True
    ```

    But a major triad does not:

    ```python
    >>> dMaj = chord.Chord([pitch.Pitch('D4'), pitch.Pitch('F#4'), pitch.Pitch('A5')])
    >>> dMaj.containsSeventh()
    False
    ```

    Note that a seventh chord itself contains a seventh.

    ```python
    >>> cChord = chord.Chord(['C', 'E', 'G', 'B'])
    >>> cChord.containsSeventh()
    True
    ```

    Empty chord returns False

    ```python
    >>> chord.Chord().containsSeventh()
    False
    ```

Chord.containsTriad() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/chord.html#Chord.containsTriad)
:   Returns True or False if there is no triad above the root.
    “Contains vs. Is”: A dominant-seventh chord contains a triad.

    ```python
    >>> cChord = chord.Chord(['C', 'E', 'G'])
    >>> other = chord.Chord(['C', 'D', 'E', 'F', 'G'])
    >>> cChord.containsTriad()
    True
    ```

    ```python
    >>> other.containsTriad()
    True
    ```

    ```python
    >>> scale = chord.Chord(['C', 'D-', 'E', 'F#', 'G', 'A#', 'B'])
    >>> scale.containsTriad()
    True
    ```

    ```python
    >>> c = chord.Chord('C4 D4')
    >>> c.containsTriad()
    False
    ```

    ```python
    >>> chord.Chord().containsTriad()
    False
    ```

static Chord.formatVectorString(*vectorList*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](../_modules/music21/chord.html#Chord.formatVectorString)
:   Return a string representation of a vector or set

    Static method. Works on the class:

    ```python
    >>> chord.Chord.formatVectorString([0, 11])
    '<0B>'
    ```

    or an existing chord:

    ```python
    >>> c1 = chord.Chord(['D4', 'A4', 'F#5', 'D6'])
    >>> c1.formatVectorString(c1.normalOrder)
    '<269>'
    ```

    or on a list that has nothing to do with the chord

    ```python
    >>> c1.formatVectorString([10, 11, 3, 5])
    '<AB35>'
    ```

Chord.geometricNormalForm() → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][[source]](../_modules/music21/chord.html#Chord.geometricNormalForm)
:   Geometric Normal Form, as first defined by Dmitri Tymoczko, orders pitch classes
    such that the spacing is prioritized with the smallest spacing between the first and
    second pitch class first, then the smallest spacing between second and third pitch class,
    and so on. This form has unique properties that make it useful. It also transposes
    to PC0

    geometricNormalForm returns a list of pitch class integers in
    geometric normal form.

    Example 1: A major triad has geometricNormalForm of 038 not 047.

    ```python
    >>> c1 = chord.Chord('E4 C5 G6 C7')
    >>> pcList = c1.geometricNormalForm()
    >>> pcList
    [0, 3, 8]
    ```

    ```python
    >>> c2 = chord.Chord(pcList)
    >>> c2.orderedPitchClassesString
    '<038>'
    ```

    Compare this to the usual normalOrder transposed to PC0:

    ```python
    >>> normalOrder = c1.normalOrder
    >>> normalOrderFirst = normalOrder[0]
    >>> [(pc - normalOrderFirst) % 12 for pc in normalOrder]
    [0, 4, 7]
    ```

Chord.getChordStep(*chordStep: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *\**, *testRoot: [Note](moduleNote.html#music21.note.Note "music21.note.Note") | [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/chord.html#Chord.getChordStep)
:   Returns the (first) pitch at the provided scaleDegree (Thus, it’s
    exactly like semitonesFromChordStep, except it instead of the number of
    semitones.)

    Returns None if none can be found.

    ```python
    >>> cmaj = chord.Chord(['C', 'E', 'G'])
    >>> cmaj.getChordStep(3)  # will return the third of the chord
    <music21.pitch.Pitch E>
    ```

    ```python
    >>> g = cmaj.getChordStep(5)  # will return the fifth of the chord
    >>> g.name
    'G'
    ```

    ```python
    >>> cmaj.getChordStep(6) is None
    True
    ```

    Ninths can be specified with either 9 or 2. Similarly for elevenths
    and thirteenths.

    ```python
    >>> c9 = chord.Chord('C4 E4 G4 B4 D5')
    >>> c9.getChordStep(9)
    <music21.pitch.Pitch D5>
    >>> c9.getChordStep(2)
    <music21.pitch.Pitch D5>
    ```

Chord.getColor(*pitchTarget*)[[source]](../_modules/music21/chord.html#Chord.getColor)
:   For a pitch in this Chord, return the color stored in self.editorial,
    or, if set for each component, return the color assigned to this
    component.

    First checks for “is” then “equals”

    ```python
    >>> p = pitch.Pitch('C4')
    >>> n = note.Note(p)
    >>> n.style.color = 'red'
    >>> c = chord.Chord([n, 'E4'])
    >>> c.getColor(p)
    'red'
    >>> c.getColor('C4')
    'red'
    >>> c.getColor('E4') is None
    True
    ```

    The color of any pitch (even a non-existing one) is the color of the chord if
    the color of that pitch is not defined.

    ```python
    >>> c.style.color = 'pink'
    >>> c.getColor('E4')
    'pink'
    >>> c.getColor('D#7')
    'pink'
    ```

Chord.getNotehead(*p*)[[source]](../_modules/music21/chord.html#Chord.getNotehead)
:   Given a pitch in this Chord, return an associated notehead
    attribute, or return ‘normal’ if not defined for that Pitch.

    If the pitch is not found, None will be returned.

    ```python
    >>> n1 = note.Note('D4')
    >>> n2 = note.Note('G4')
    >>> n2.notehead = 'diamond'
    >>> c1 = chord.Chord([n1, n2])
    >>> c1.getNotehead(c1.pitches[1])
    'diamond'
    ```

    ```python
    >>> c1.getNotehead(c1.pitches[0])
    'normal'
    ```

    ```python
    >>> c1.getNotehead(pitch.Pitch('A#6')) is None
    True
    ```

    Will work if the two notes are equal in pitch

    ```python
    >>> c1.getNotehead(note.Note('G4'))
    'diamond'
    ```

Chord.getNoteheadFill(*p*)[[source]](../_modules/music21/chord.html#Chord.getNoteheadFill)
:   Given a pitch in this Chord, return an associated noteheadFill
    attribute, or return None if not defined for that Pitch.

    If the pitch is not found, None will also be returned.

    ```python
    >>> n1 = note.Note('D4')
    >>> n2 = note.Note('G4')
    >>> n2.noteheadFill = True
    >>> c1 = chord.Chord([n1, n2])
    >>> c1.getNoteheadFill(c1.pitches[1])
    True
    ```

    ```python
    >>> print(c1.getNoteheadFill(c1.pitches[0]))
    None
    ```

    ```python
    >>> c1.getNoteheadFill(pitch.Pitch('A#6')) is None
    True
    ```

    Will work if the two notes are equal in pitch

    ```python
    >>> c1.getNoteheadFill(note.Note('G4'))
    True
    ```

    Returns None if the pitch is not in the Chord:

Chord.getStemDirection(*p*)[[source]](../_modules/music21/chord.html#Chord.getStemDirection)
:   Given a pitch in this Chord, return an associated stem attribute, or
    return ‘unspecified’ if not defined for that Pitch or None.

    If the pitch is not found, None will be returned.

    ```python
    >>> n1 = note.Note('D4')
    >>> n2 = note.Note('G4')
    >>> n2.stemDirection = 'double'
    >>> c1 = chord.Chord([n1, n2])
    >>> c1.getStemDirection(c1.pitches[1])
    'double'
    ```

    ```python
    >>> c1.getStemDirection(c1.pitches[0])
    'unspecified'
    ```

    Will work if the two pitches are equal in pitch

    ```python
    >>> c1.getStemDirection(note.Note('G4'))
    'double'
    ```

    Returns None if a Note or Pitch is not in the Chord

    ```python
    >>> c1.getStemDirection(pitch.Pitch('A#4')) is None
    True
    ```

Chord.getTie(*p*)[[source]](../_modules/music21/chord.html#Chord.getTie)
:   Given a pitch in this Chord, return an associated Tie object, or return
    None if not defined for that Pitch.

    ```python
    >>> c1 = chord.Chord(['d', 'e-', 'b-'])
    >>> t1 = tie.Tie('start')
    >>> c1.setTie(t1, c1.pitches[2])  # just to b-
    >>> c1.getTie(c1.pitches[2]) == t1
    True
    ```

    ```python
    >>> c1.getTie(c1.pitches[0]) is None
    True
    ```

    All notes not in chord return None

    ```python
    >>> c1.getTie(pitch.Pitch('F#2')) is None
    True
    ```

    ```python
    >>> c1.getTie('B-')
    <music21.tie.Tie start>
    ```

Chord.getVolume(*p*)[[source]](../_modules/music21/chord.html#Chord.getVolume)
:   For a given Pitch in this Chord, return the
    [`Volume`](moduleVolume.html#music21.volume.Volume "music21.volume.Volume") object.

    Raises an exception if the pitch isn’t in the chord
    (TODO: consider changing to be like notehead, etc.)

    ```python
    >>> c = chord.Chord('C4 F4')
    >>> c[0].volume = 2
    >>> c.getVolume('C4')
    <music21.volume.Volume realized=0.02>
    ```

    ```python
    >>> c.getVolume('F4')  # default
    <music21.volume.Volume realized=0.71>
    ```

    ```python
    >>> c.getVolume('G4')
    Traceback (most recent call last):
    music21.chord.ChordException: the given pitch is not in the Chord: G4
    ```

Chord.getZRelation() → [Chord](#music21.chord.Chord "music21.chord.Chord") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/chord.html#Chord.getZRelation)
:   Return a Z relation if it exists, otherwise return None.

    ```python
    >>> chord.fromIntervalVector((1, 1, 1, 1, 1, 1))
    <music21.chord.Chord C C# E F#>
    ```

    ```python
    >>> chord.fromIntervalVector((1, 1, 1, 1, 1, 1)).getZRelation()
    <music21.chord.Chord C D- E- G>
    ```

    Z relation will always be zero indexed:

    ```python
    >>> c = chord.Chord('D D# F# G#')
    >>> c.getZRelation()
    <music21.chord.Chord C D- E- G>
    ```

    ```python
    >>> chord.Chord('C E G').getZRelation() is None
    True
    ```

Chord.hasAnyEnharmonicSpelledPitches() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/chord.html#Chord.hasAnyEnharmonicSpelledPitches)
:   Returns True if for any given pitchClass there is more than one spelling of the note
    in any octave (e.g., C#4 and D-5).

    ```python
    >>> cChord = chord.Chord('C4 E4 G4 C5')
    >>> cChord.hasAnyEnharmonicSpelledPitches()
    False
    ```

    Notice that having a C in two different octaves is no problem. However, this is False:

    ```python
    >>> cChord = chord.Chord('C4 E4 G4 B#4')
    >>> cChord.hasAnyEnharmonicSpelledPitches()
    True
    ```

Chord.hasAnyRepeatedDiatonicNote() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/chord.html#Chord.hasAnyRepeatedDiatonicNote)
:   Returns True if for any diatonic note (e.g., C or C# = C) there are two or more
    different notes (such as E and E-) in the chord. If there are no repeated
    scale degrees, return False.

    ```python
    >>> cChord = chord.Chord(['C', 'E', 'E-', 'G'])
    >>> cChord.hasAnyRepeatedDiatonicNote()
    True
    ```

    This routine is helpful for anything that works with Generic intervals and chord
    steps such as .third which makes sure that checking for root, second, third,
    …, seventh will actually find all the different notes.

    This following example returns False because chromatically identical notes of
    different scale degrees do not count as a repeated diatonic note.
    (See [`hasAnyEnharmonicSpelledPitches()`](#music21.chord.Chord.hasAnyEnharmonicSpelledPitches "music21.chord.Chord.hasAnyEnharmonicSpelledPitches") for that method)

    ```python
    >>> other = chord.Chord(['C', 'E', 'F-', 'G'])
    >>> other.hasAnyRepeatedDiatonicNote()
    False
    ```

Chord.hasRepeatedChordStep(*chordStep*, *\**, *testRoot=None*)[[source]](../_modules/music21/chord.html#Chord.hasRepeatedChordStep)
:   Returns True if chordStep above testRoot (or self.root()) has two
    or more different notes (such as E and E-) in it. Otherwise
    returns False.

    ```python
    >>> cChord = chord.Chord(['G2', 'E4', 'E-5', 'C6'])
    >>> cChord.hasRepeatedChordStep(3)
    True
    ```

    ```python
    >>> cChord.hasRepeatedChordStep(5)
    False
    ```

Chord.intervalFromChordStep(*chordStep*, *\**, *testRoot=None*)[[source]](../_modules/music21/chord.html#Chord.intervalFromChordStep)
:   Exactly like semitonesFromChordStep, except it returns the interval
    itself instead of the number of semitones:

    ```python
    >>> cmaj = chord.Chord(['C', 'E', 'G'])
    >>> cmaj.intervalFromChordStep(3)  # will return the interval between C and E
    <music21.interval.Interval M3>
    ```

    ```python
    >>> cmaj.intervalFromChordStep(5)  # will return the interval between C and G
    <music21.interval.Interval P5>
    ```

    ```python
    >>> print(cmaj.intervalFromChordStep(6))
    None
    ```

Chord.inversion(*newInversion: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *\**, *find: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *testRoot: [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *transposeOnSet: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/chord.html#Chord.inversion)

Chord.inversion(*newInversion: [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\**, *find: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *testRoot: [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *transposeOnSet: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")
:   Find the chord’s inversion or (if called with a number) set the chord to
    the new inversion.

    When called without a number argument, returns an integer (or None)
    representing which inversion (if any)
    the chord is in. The Chord does not have to be complete, in which case
    this function determines the inversion by looking at the relationship
    of the bass note to the root.

    Returns a maximum value of 5 for the fifth inversion of a thirteenth chord.
    Returns 0 if the bass to root interval is a unison
    or if interval is not a common inversion (1st-5th).
    The octave of the bass and root are irrelevant to this calculation of inversion.
    Returns None if the Chord has no pitches.

    ```python
    >>> g7 = chord.Chord(['g4', 'b4', 'd5', 'f5'])
    >>> g7.inversion()
    0
    >>> g7.inversion(1)
    >>> g7
    <music21.chord.Chord B4 D5 F5 G5>
    ```

    With implicit octaves, D becomes the bass (since octaves start on C):

    ```python
    >>> g7_implicit = chord.Chord(['g', 'b', 'd', 'f'])
    >>> g7_implicit.inversion()
    2
    ```

    Note that in inverting a chord with implicit octaves, some
    pitches will gain octave designations, but not necessarily all of them
    (this behavior might change in the future):

    ```python
    >>> g7_implicit.inversion(1)
    >>> g7_implicit
    <music21.chord.Chord B D5 F5 G5>
    ```

    Examples of each inversion:

    ```python
    >>> cTriad1stInversion = chord.Chord(['E1', 'G1', 'C2'])
    >>> cTriad1stInversion.inversion()
    1
    ```

    ```python
    >>> cTriad2ndInversion = chord.Chord(['G1', 'E2', 'C2'])
    >>> cTriad2ndInversion.inversion()
    2
    ```

    ```python
    >>> dSeventh3rdInversion = chord.Chord(['C4', 'B4'])
    >>> dSeventh3rdInversion.bass(pitch.Pitch('B4'))
    >>> dSeventh3rdInversion.inversion()
    3
    ```

    ```python
    >>> gNinth4thInversion = chord.Chord(['G4', 'B4', 'D5', 'F5', 'A4'])
    >>> gNinth4thInversion.bass(pitch.Pitch('A4'))
    >>> gNinth4thInversion.inversion()
    4
    ```

    ```python
    >>> bbEleventh5thInversion = chord.Chord(['B-', 'D', 'F', 'A', 'C', 'E-'])
    >>> bbEleventh5thInversion.bass(pitch.Pitch('E-4'))
    >>> bbEleventh5thInversion.inversion()
    5
    ```

    Repeated notes do not affect the inversion:

    ```python
    >>> gMajRepeats = chord.Chord(['G4', 'B5', 'G6', 'B6', 'D7'])
    >>> gMajRepeats.inversion(2)
    >>> gMajRepeats
    <music21.chord.Chord D7 G7 B7 G8 B8>
    ```

    ```python
    >>> gMajRepeats.inversion(3)
    Traceback (most recent call last):
    music21.chord.ChordException: Could not invert chord: inversion may not exist
    ```

    If testRoot is True then that temporary root is used instead of self.root().

    Get the inversion for a seventh chord showing different roots

    ```python
    >>> dim7 = chord.Chord('B4 D5 F5 A-5 C6 E6 G6')
    >>> dim7.inversion()
    0
    >>> dim7.inversion(testRoot=pitch.Pitch('D5'))
    6
    >>> dim7.inversion('six-four')
    Traceback (most recent call last):
    music21.chord.ChordException: Inversion must be an integer, got: <class 'str'>
    ```

    Chords without pitches or otherwise impossible chords return -1, indicating
    no normal inversion.

    ```python
    >>> chord.Chord().inversion(testRoot=pitch.Pitch('C5'))
    -1
    ```

    For Harmony subclasses, this method does not check to see if
    the inversion is reasonable according to the figure provided.
    see [`inversionIsValid()`](moduleHarmony.html#music21.harmony.ChordSymbol.inversionIsValid "music21.harmony.ChordSymbol.inversionIsValid")
    for checker method on ChordSymbolObjects.

    If only two pitches given, an inversion is still returned, often as
    if it were a triad:

    ```python
    >>> chord.Chord('C4 G4').inversion()
    0
    >>> chord.Chord('G4 C5').inversion()
    2
    ```

    If transposeOnSet is False then setting the inversion simply
    sets the value to be returned later, which might be useful for
    cases where the chords are poorly spelled, or there is an added note.

    * Changed in v8: deal with chords without pitches

Chord.inversionName() → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/chord.html#Chord.inversionName)
:   Returns an integer representing the common abbreviation for the
    inversion the chord is in. If chord is not in a common inversion,
    returns None.

    Third inversion sevenths return 42 not 2.

    ```python
    >>> a = chord.Chord(['G3', 'B3', 'F3', 'D3'])
    >>> a.inversionName()
    43
    ```

Chord.inversionText() → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](../_modules/music21/chord.html#Chord.inversionText)
:   A helper method to return a readable inversion text (with capitalization) for a chord:

    ```python
    >>> chord.Chord('C4 E4 G4').inversionText()
    'Root Position'
    >>> chord.Chord('E4 G4 C5').inversionText()
    'First Inversion'
    ```

    ```python
    >>> chord.Chord('B-3 C4 E4 G4').inversionText()
    'Third Inversion'
    ```

    ```python
    >>> chord.Chord().inversionText()
    'Unknown Position'
    ```

Chord.isAugmentedSixth(*\**, *permitAnyInversion=False*)[[source]](../_modules/music21/chord.html#Chord.isAugmentedSixth)
:   returns True if the chord is an Augmented 6th chord in normal inversion.
    (that is, in first inversion for Italian and German and second for French and Swiss)

    ```python
    >>> c = chord.Chord(['A-3', 'C4', 'E-4', 'F#4'])
    >>> c.isAugmentedSixth()
    True
    ```

    Spelling matters

    ```python
    >>> c.pitches[3].getEnharmonic(inPlace=True)
    >>> c
    <music21.chord.Chord A-3 C4 E-4 G-4>
    >>> c.isAugmentedSixth()
    False
    ```

    Italian:

    ```python
    >>> c = chord.Chord(['A-3', 'C4', 'F#4'])
    >>> c.isAugmentedSixth()
    True
    ```

    If permitAnyInversion is True then any inversion is allowed.

Chord.isAugmentedTriad()[[source]](../_modules/music21/chord.html#Chord.isAugmentedTriad)
:   Returns True if chord is an Augmented Triad, that is,
    if it contains only notes that are
    either in unison with the root, a major third above the root,
    or an augmented fifth above the
    root. Additionally, the Chord must contain at least one of each third and
    fifth above the root.

    The chord might not seem to need to be spelled correctly
    since incorrectly spelled Augmented Triads are
    usually augmented triads in some other inversion
    (e.g. C-E-Ab is a second-inversion augmented triad; C-Fb-Ab
    is in first inversion). However, B#-Fb-Ab does return False as it is not a
    stack of two major thirds in any inversion.

    Returns False if is not an augmented triad.

    ```python
    >>> c = chord.Chord(['C4', 'E4', 'G#4'])
    >>> c.isAugmentedTriad()
    True
    >>> c = chord.Chord(['C4', 'E4', 'G4'])
    >>> c.isAugmentedTriad()
    False
    ```

    Other spellings will give other roots!

    ```python
    >>> c = chord.Chord(['C4', 'E4', 'A-4'])
    >>> c.isAugmentedTriad()
    True
    >>> c.root()
    <music21.pitch.Pitch A-4>
    ```

    ```python
    >>> c = chord.Chord(['C4', 'F-4', 'A-4'])
    >>> c.isAugmentedTriad()
    True
    >>> c = chord.Chord(['B#4', 'F-4', 'A-4'])
    >>> c.isAugmentedTriad()
    False
    ```

    ```python
    >>> chord.Chord().isAugmentedTriad()
    False
    ```

Chord.isConsonant()[[source]](../_modules/music21/chord.html#Chord.isConsonant)
:   Returns True if the chord is:

    * one pitch (always consonant)
    * two pitches: uses [`isConsonant()`](moduleInterval.html#music21.interval.Interval.isConsonant "music21.interval.Interval.isConsonant") , which
      :   checks if the interval is a major or minor third or sixth or perfect fifth.
    * three pitches: if chord is a major or minor triad not in second inversion.

    These rules define all common-practice consonances
    (and earlier back to about 1300 all imperfect consonances)

    ```python
    >>> c1 = chord.Chord(['C3', 'E4', 'G5'])
    >>> c1.isConsonant()
    True
    ```

    ```python
    >>> c2 = chord.Chord(['G3', 'E-4', 'C5'])
    >>> c2.isConsonant()
    False
    ```

    ```python
    >>> c3 = chord.Chord(['F2', 'A2', 'C3', 'E-3'])
    >>> c3.isConsonant()
    False
    ```

    ```python
    >>> c4 = chord.Chord(['C1', 'G1', 'C2', 'G2', 'C3', 'G3'])
    >>> c4.isConsonant()
    True
    ```

    ```python
    >>> c5 = chord.Chord(['G1', 'C2', 'G2', 'C3', 'G3'])
    >>> c5.isConsonant()
    False
    ```

    ```python
    >>> c6 = chord.Chord(['F#'])
    >>> c6.isConsonant()
    True
    ```

    ```python
    >>> c7 = chord.Chord(['C1', 'C#1', 'D-1'])
    >>> c7.isConsonant()
    False
    ```

    Spelling does matter:

    ```python
    >>> c8 = chord.Chord(['D-4', 'G#4'])
    >>> c8.isConsonant()
    False
    ```

    ```python
    >>> c9 = chord.Chord(['D3', 'A2', 'D2', 'D2', 'A4'])
    >>> c9.isConsonant()
    True
    ```

    ```python
    >>> c10 = chord.Chord(['D3', 'A2', 'D2', 'D2', 'A1'])
    >>> c10.isConsonant()
    False
    ```

    ```python
    >>> c11 = chord.Chord(['F3', 'D4', 'A4'])
    >>> c11.isConsonant()
    True
    ```

    ```python
    >>> c12 = chord.Chord(['F3', 'D4', 'A4', 'E#4'])
    >>> c12.isConsonant()
    False
    ```

Chord.isDiminishedSeventh()[[source]](../_modules/music21/chord.html#Chord.isDiminishedSeventh)
:   Returns True if chord is a Diminished Seventh, that is,
    if it contains only notes that are
    either in unison with the root, a minor third above the root,
    a diminished fifth, or a minor seventh
    above the root. Additionally, must contain at least one of
    each third and fifth above the root.
    Chord must be spelled correctly. Otherwise returns false.

    ```python
    >>> a = chord.Chord(['c', 'e-', 'g-', 'b--'])
    >>> a.isDiminishedSeventh()
    True
    ```

    ```python
    >>> chord.Chord().isDiminishedSeventh()
    False
    ```

Chord.isDiminishedTriad() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/chord.html#Chord.isDiminishedTriad)
:   Returns True if chord is a Diminished Triad, that is,
    if it contains only notes that are
    either in unison with the root, a minor third above the
    root, or a diminished fifth above the
    root. Additionally, must contain at least one of each
    third and fifth above the root.
    Chord must be spelled correctly. Otherwise returns false.

    ```python
    >>> cChord = chord.Chord(['C', 'E-', 'G-'])
    >>> cChord.isDiminishedTriad()
    True
    >>> other = chord.Chord(['C', 'E-', 'F#'])
    >>> other.isDiminishedTriad()
    False
    ```

Chord.isDominantSeventh() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/chord.html#Chord.isDominantSeventh)
:   Returns True if chord is a Dominant Seventh, that is,
    if it contains only notes that are
    either in unison with the root, a major third above the root,
    a perfect fifth, or a major seventh
    above the root. Additionally, must contain at least one of
    each third and fifth above the root.
    Chord must be spelled correctly. Otherwise returns false.

    ```python
    >>> a = chord.Chord(['b', 'g', 'd', 'f'])
    >>> a.isDominantSeventh()
    True
    ```

    ```python
    >>> chord.Chord().isDominantSeventh()
    False
    ```

    ```python
    >>> c2 = chord.Chord('C4 E4 G4 A#4')
    >>> c2.isDominantSeventh()
    False
    ```

Chord.isFalseDiminishedSeventh() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/chord.html#Chord.isFalseDiminishedSeventh)
:   Returns True if chord is a Diminished Seventh, that is,
    if it contains only notes that are
    either in unison with the root, a minor third above the root,
    a diminished fifth, or a diminished seventh
    above the root. Additionally, must contain at least one of
    each third and fifth above the root.
    Chord MAY BE SPELLED INCORRECTLY. Otherwise returns False.

    ```python
    >>> c = chord.Chord('C D# G- A')
    >>> c.isFalseDiminishedSeventh()
    True
    ```

    ```python
    >>> chord.Chord().isFalseDiminishedSeventh()
    False
    ```

    ```python
    >>> chord.Chord('C4 E4 G4').isFalseDiminishedSeventh()
    False
    ```

    Correctly spelled diminished seventh chords are also false diminished sevenths.

    ```python
    >>> chord.Chord('C4 E-4 G-4 B--4').isFalseDiminishedSeventh()
    True
    ```

Chord.isFrenchAugmentedSixth(*\**, *permitAnyInversion=False*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/chord.html#Chord.isFrenchAugmentedSixth)
:   Returns True if the chord is a French augmented sixth chord
    (flat 6th scale degree in bass, tonic, second scale degree, and raised 4th).

    N.B. The root() method of music21.chord.Chord determines
    the root based on the note with
    the most thirds above it. However, under this definition, a
    1st-inversion french augmented sixth chord
    resembles a second inversion chord, not the first inversion
    subdominant chord it is based
    upon. We fix this by adjusting the root. First, however, we
    check to see if the chord is
    in second inversion to begin with, otherwise it is not
    a Fr+6 chord. This is to avoid ChordException errors.

    ```python
    >>> fr6a = chord.Chord(['A-3', 'C4', 'D4', 'F#4'])
    >>> fr6a.isFrenchAugmentedSixth()
    True
    ```

    Spelling matters:

    ```python
    >>> fr6b = chord.Chord(['A-3', 'C4', 'D4', 'G-4'])
    >>> fr6b.isFrenchAugmentedSixth()
    False
    ```

    ```python
    >>> fr6b = chord.Chord(['A-3', 'C4', 'E--4', 'F#4'])
    >>> fr6b.isFrenchAugmentedSixth()
    False
    ```

    Inversion matters:

    ```python
    >>> fr6c = chord.Chord(['C4', 'D4', 'F#4', 'A-4'])
    >>> fr6c.isFrenchAugmentedSixth()
    False
    ```

    Unless permitAnyInversion is True

    ```python
    >>> fr6c.isFrenchAugmentedSixth(permitAnyInversion=True)
    True
    ```

    * Changed in v7: permitAnyInversion added

Chord.isGermanAugmentedSixth(*\**, *permitAnyInversion=False*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/chord.html#Chord.isGermanAugmentedSixth)
:   Returns True if the chord is a German augmented sixth chord
    (flat 6th scale degree in bass, tonic, flat third scale degree, and raised 4th).

    ```python
    >>> gr6a = chord.Chord(['A-3', 'C4', 'E-4', 'F#4'])
    >>> gr6a.isGermanAugmentedSixth()
    True
    ```

    Spelling matters (see isSwissAugmentedSixth)

    ```python
    >>> gr6b = chord.Chord(['A-3', 'C4', 'D#4', 'F#4'])
    >>> gr6b.isGermanAugmentedSixth()
    False
    ```

    Inversion matters:

    ```python
    >>> gr6c = chord.Chord(['C4', 'E-4', 'F#4', 'A-4'])
    >>> gr6c.isGermanAugmentedSixth()
    False
    ```

    unless permitAnyInversion is True:

    ```python
    >>> gr6c.isGermanAugmentedSixth(permitAnyInversion=True)
    True
    ```

    * Changed in v7: permitAnyInversion added

Chord.isHalfDiminishedSeventh() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/chord.html#Chord.isHalfDiminishedSeventh)
:   Returns True if chord is a Half Diminished Seventh, that is,
    if it contains only notes that are
    either in unison with the root, a minor third above the root, a
    diminished fifth, or a major seventh
    above the root. Additionally, must contain at least one of each third,
    fifth, and seventh above the root.
    Chord must be spelled correctly. Otherwise returns false.

    ```python
    >>> c1 = chord.Chord(['C4', 'E-4', 'G-4', 'B-4'])
    >>> c1.isHalfDiminishedSeventh()
    True
    ```

    Incorrectly spelled chords are not considered half-diminished sevenths
    >>> c2 = chord.Chord([‘C4’, ‘E-4’, ‘G-4’, ‘A#4’])
    >>> c2.isHalfDiminishedSeventh()
    False

    Nor are incomplete chords
    >>> c3 = chord.Chord([‘C4’, ‘G-4’, ‘B-4’])
    >>> c3.isHalfDiminishedSeventh()
    False

    ```python
    >>> chord.Chord().isHalfDiminishedSeventh()
    False
    ```

Chord.isIncompleteMajorTriad() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/chord.html#Chord.isIncompleteMajorTriad)
:   Returns True if the chord is an incomplete Major triad, or, essentially,
    a dyad of root and major third

    ```python
    >>> c1 = chord.Chord(['C4', 'E3'])
    >>> c1.isMajorTriad()
    False
    >>> c1.isIncompleteMajorTriad()
    True
    ```

    Note that complete major triads return False:

    ```python
    >>> c2 = chord.Chord(['C4', 'E3', 'G5'])
    >>> c2.isIncompleteMajorTriad()
    False
    ```

    Remember, MAJOR Triad:

    ```python
    >>> c3 = chord.Chord(['C4', 'E-3'])
    >>> c3.isIncompleteMajorTriad()
    False
    ```

    Must be spelled properly

    ```python
    >>> c1 = chord.Chord(['C4', 'F-4'])
    >>> c1.isIncompleteMajorTriad()
    False
    ```

    Empty Chords return False

    ```python
    >>> chord.Chord().isIncompleteMajorTriad()
    False
    ```

Chord.isIncompleteMinorTriad() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/chord.html#Chord.isIncompleteMinorTriad)
:   returns True if the chord is an incomplete Minor triad, or, essentially,
    a dyad of root and minor third

    ```python
    >>> c1 = chord.Chord(['C4', 'E-3'])
    >>> c1.isMinorTriad()
    False
    >>> c1.isIncompleteMinorTriad()
    True
    >>> c2 = chord.Chord(['C4', 'E-3', 'G5'])
    >>> c2.isIncompleteMinorTriad()
    False
    ```

Chord.isItalianAugmentedSixth(*\**, *restrictDoublings=False*, *permitAnyInversion=False*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/chord.html#Chord.isItalianAugmentedSixth)
:   Returns True if the chord is a properly spelled Italian augmented sixth chord in
    first inversion. Otherwise returns False.

    If restrictDoublings is set to True then only the tonic may be doubled.

    ```python
    >>> c1 = chord.Chord(['A-4', 'C5', 'F#6'])
    >>> c1.isItalianAugmentedSixth()
    True
    ```

    Spelling matters:

    ```python
    >>> c2 = chord.Chord(['A-4', 'C5', 'G-6'])
    >>> c2.isItalianAugmentedSixth()
    False
    ```

    So does inversion:

    ```python
    >>> c3 = chord.Chord(['F#4', 'C5', 'A-6'])
    >>> c3.isItalianAugmentedSixth()
    False
    >>> c4 = chord.Chord(['C5', 'A-5', 'F#6'])
    >>> c4.isItalianAugmentedSixth()
    False
    ```

    If inversions don’t matter to you, add permitAnyInversion=True:

    ```python
    >>> c3.isItalianAugmentedSixth(permitAnyInversion=True)
    True
    >>> c4.isItalianAugmentedSixth(permitAnyInversion=True)
    True
    ```

    If doubling rules are turned on then only the tonic can be doubled:

    ```python
    >>> c4 = chord.Chord(['A-4', 'C5', 'F#6', 'C6', 'C7'])
    >>> c4.isItalianAugmentedSixth(restrictDoublings=True)
    True
    >>> c5 = chord.Chord(['A-4', 'C5', 'F#6', 'C5', 'F#7'])
    >>> c5.isItalianAugmentedSixth(restrictDoublings=True)
    False
    >>> c5.isItalianAugmentedSixth(restrictDoublings=False)
    True
    ```

    * Changed in v7: restrictDoublings is keyword only. Added permitAnyInversion.

Chord.isMajorTriad()[[source]](../_modules/music21/chord.html#Chord.isMajorTriad)
:   Returns True if chord is a Major Triad, that is, if it contains only notes that are
    either in unison with the root, a major third above the root, or a perfect fifth above the
    root. Additionally, must contain at least one of each third and fifth above the root.
    Chord must be spelled correctly. Otherwise returns false.

    Example:

    ```python
    >>> cChord = chord.Chord(['C', 'E', 'G'])
    >>> other = chord.Chord(['C', 'G'])
    >>> cChord.isMajorTriad()
    True
    >>> other.isMajorTriad()
    False
    ```

    Notice that the proper spelling of notes is crucial

    ```python
    >>> chord.Chord(['B-', 'D', 'F']).isMajorTriad()
    True
    >>> chord.Chord(['A#', 'D', 'F']).isMajorTriad()
    False
    ```

    (See: [`forteClassTn()`](#music21.chord.Chord.forteClassTn "music21.chord.Chord.forteClassTn") to catch this case; major triads
    in the forte system are 3-11B no matter how they are spelled.)

    ```python
    >>> chord.Chord(['A#', 'D', 'F']).forteClassTn == '3-11B'
    True
    ```

Chord.isMinorTriad()[[source]](../_modules/music21/chord.html#Chord.isMinorTriad)
:   Returns True if chord is a Minor Triad, that is, if it contains only notes that are
    either in unison with the root, a minor third above the root, or a perfect fifth above the
    root. Additionally, must contain at least one of each third and fifth above the root.
    Chord must be spelled correctly. Otherwise returns false.

    Example:

    ```python
    >>> cChord = chord.Chord(['C', 'E-', 'G'])
    >>> cChord.isMinorTriad()
    True
    >>> other = chord.Chord(['C', 'E', 'G'])
    >>> other.isMinorTriad()
    False
    ```

Chord.isNinth()[[source]](../_modules/music21/chord.html#Chord.isNinth)
:   Returns True if chord contains at least one of each of Third, Fifth, Seventh, and Ninth
    and every note in the chord is a Third, Fifth, Seventh, or Ninth, such that there are no
    repeated scale degrees (ex: E and E-). Else return false.

    Example:

    ```python
    >>> cChord = chord.Chord(['C', 'E', 'G', 'B', 'D'])
    >>> cChord.isNinth()
    True
    >>> other = chord.Chord(['C', 'E', 'F', 'G', 'B'])
    >>> other.isNinth()
    False
    ```

Chord.isSeventh()[[source]](../_modules/music21/chord.html#Chord.isSeventh)
:   Returns True if chord contains at least one of each of Third, Fifth, and Seventh,
    and every note in the chord is a Third, Fifth, or Seventh, such that there are no
    repeated scale degrees (ex: E and E-). Else return false.

    Example:

    ```python
    >>> cChord = chord.Chord(['C', 'E', 'G', 'B'])
    >>> cChord.isSeventh()
    True
    >>> other = chord.Chord(['C', 'D', 'E', 'F', 'G', 'B'])
    >>> other.isSeventh()
    False
    ```

Chord.isSeventhOfType(*intervalArray*)[[source]](../_modules/music21/chord.html#Chord.isSeventhOfType)
:   Returns True if chord is a seventh chord of a particular type
    as specified by intervalArray. For instance .isDiminishedSeventh()
    is just a thin wrapper around .isSeventhOfType([0, 3, 6, 9])
    and isDominantSeventh() has intervalArray([0, 4, 7, 10])

    intervalArray can be any iterable.

    Though it checks on intervalArray, it does make sure that it is a
    seventh chord, not D–, D##, G, B-

    ```python
    >>> chord.Chord('C E G B-').isSeventhOfType((0, 4, 7, 10))
    True
    >>> chord.Chord('C E G B-').isSeventhOfType((0, 3, 7, 10))
    False
    >>> chord.Chord('D-- D## G B-').isSeventhOfType((0, 4, 7, 10))
    False
    ```

Chord.isSwissAugmentedSixth(*\**, *permitAnyInversion=False*)[[source]](../_modules/music21/chord.html#Chord.isSwissAugmentedSixth)
:   Returns true if it is a respelled German augmented 6th chord with
    sharp 2 instead of flat 3. This chord has many names,
    Swiss Augmented Sixth, Alsatian Chord, English A6, Norwegian, etc.
    as well as doubly-augmented sixth, which is a bit of a misnomer since
    it is the 4th that is doubly augmented, not the sixth.

    ```python
    >>> chord.Chord('A-4 C5 D#5 F#6').isSwissAugmentedSixth()
    True
    ```

    Respelled as a German Augmented Sixth does not count:

    ```python
    >>> chord.Chord('A-4 C5 E-5 F#6').isSwissAugmentedSixth()
    False
    ```

    Inversions matter:

    ```python
    >>> ch3 = chord.Chord('F#4 D#5 C6 A-6')
    >>> ch3.isSwissAugmentedSixth()
    False
    ```

    unless permitAnyInversion is given:

    ```python
    >>> ch3.isSwissAugmentedSixth(permitAnyInversion=True)
    True
    ```

    * Changed in v7: permitAnyInversion added

Chord.isTranspositionallySymmetrical(*\**, *requireIntervallicEvenness=False*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/chord.html#Chord.isTranspositionallySymmetrical)
:   Returns True if the Chord is symmetrical under transposition
    and False otherwise. A pitch-class-based way of looking at this, is
    can all the pitch classes be transposed up some number of semitones 1-11
    and end up with the same pitch-classes. Like the dyad F-B can have each
    note transposed up 6 semitones and get another B-F = F-B dyad.

    A tonally-focused way of looking at this would be to ask, “Are we unable
    to distinguish root position vs. some inversion of the basic chord by ear alone?”
    For instance, we can see (visually) that C-Eb-Gb-Bbb is a diminished-seventh
    chord in root position, while
    Eb-Gb-Bbb-C is a diminished-seventh in first inversion.
    But if the chord were heard in isolation
    it would not be possible to tell the inversion at all, since diminished-sevenths
    are transpositionally symmetrical.

    With either way of looking at it,
    there are fourteen set classes of 2-10 pitch classes have this property,
    including the augmented triad:

    ```python
    >>> chord.Chord('C E G#').isTranspositionallySymmetrical()
    True
    ```

    But the major triad is not transpositionally symmetrical:

    ```python
    >>> chord.Chord('C E G').isTranspositionallySymmetrical()
    False
    ```

    The whole-tone scale and the Petrushka chord are both transpositionally symmetrical:

    ```python
    >>> wholeToneAsChord = chord.Chord('C D E F# G# B- C')
    >>> wholeToneAsChord.isTranspositionallySymmetrical()
    True
    ```

    ```python
    >>> petrushka = chord.Chord([0, 1, 3, 6, 7, 9])
    >>> petrushka.isTranspositionallySymmetrical()
    True
    ```

    If requireIntervallicEvenness is True then only chords that also have
    even spacing / evenly divide the octave are considered transpositionally
    symmetrical. The normal cases are the F-B (06) dyad, the augmented triad,
    the diminished-seventh chord, and the whole-tone scale collection:

    ```python
    >>> wholeToneAsChord.isTranspositionallySymmetrical(requireIntervallicEvenness=True)
    True
    ```

    ```python
    >>> petrushka.isTranspositionallySymmetrical(requireIntervallicEvenness=True)
    False
    ```

    Note that complements of these chords (except the whole-tone collection) are
    not transpositionally symmetrical if requireIntervallicEvenness is required:

    ```python
    >>> chord.Chord([0, 4, 8]).isTranspositionallySymmetrical(requireIntervallicEvenness=True)
    True
    ```

    ```python
    >>> chord.Chord([1, 2, 3, 5, 6, 7, 9, 10, 11]).isTranspositionallySymmetrical(
    ...       requireIntervallicEvenness=True)
    False
    ```

    Empty chords and the total aggregate cannot have their inversion determined by ear alone.
    So they are True with or without requireIntervallicEvenness.

    ```python
    >>> chord.Chord().isTranspositionallySymmetrical()
    True
    ```

    ```python
    >>> chord.Chord(list(range(12))).isTranspositionallySymmetrical()
    True
    ```

    Monads (single-note “chords”) cannot be transposed 1-11 semitones to recreate themselves,
    so they return False by default:

    ```python
    >>> chord.Chord('C').isTranspositionallySymmetrical()
    False
    ```

    But they are the only case where requireIntervallicEvenness actually switches from
    False to True, because they do evenly divide the octave.

    ```python
    >>> chord.Chord('C').isTranspositionallySymmetrical(requireIntervallicEvenness=True)
    True
    ```

    11-note chords return False in either case:

    ```python
    >>> chord.Chord(list(range(11))).isTranspositionallySymmetrical()
    False
    ```

Chord.isTriad() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/chord.html#Chord.isTriad)
:   Returns True if this Chord is a triad of some sort. It could even be a rather
    exotic triad so long as the chord contains at least one Third and one Fifth and
    all notes have the same name as one of the three notes.

    Note: only returns True if triad is spelled correctly.

    Note the difference of “containsTriad” vs. “isTriad”:
    A dominant-seventh chord is NOT a triad, but it contains two triads.

    ```python
    >>> cChord = chord.Chord(['C4', 'E4', 'A4'])
    >>> cChord.isTriad()
    True
    ```

    ```python
    >>> other = chord.Chord(['C', 'D', 'E', 'F', 'G'])
    >>> other.isTriad()
    False
    ```

    ```python
    >>> incorrectlySpelled = chord.Chord(['C', 'D#', 'G'])
    >>> incorrectlySpelled.isTriad()
    False
    ```

    ```python
    >>> incorrectlySpelled.pitches[1].getEnharmonic(inPlace=True)
    >>> incorrectlySpelled
    <music21.chord.Chord C E- G>
    >>> incorrectlySpelled.isTriad()
    True
    ```

Chord.removeRedundantPitchClasses(*\**, *inPlace=False*)[[source]](../_modules/music21/chord.html#Chord.removeRedundantPitchClasses)
:   Remove all but the FIRST instance of a pitch class with more than one
    instance of that pitch class.

    If inPlace is True, a copy is not made and a list of deleted pitches is returned;
    otherwise a copy is made and that copy is returned.

    ```python
    >>> c1 = chord.Chord(['c2', 'e3', 'g4', 'e3'])
    >>> removed = c1.removeRedundantPitchClasses(inPlace=True)
    >>> c1.pitches
    (<music21.pitch.Pitch C2>, <music21.pitch.Pitch E3>, <music21.pitch.Pitch G4>)
    ```

    ```python
    >>> c2 = chord.Chord(['c5', 'e3', 'g4', 'c2', 'e3', 'f-4'])
    >>> removed = c2.removeRedundantPitchClasses(inPlace=True)
    >>> c2.pitches
    (<music21.pitch.Pitch C5>, <music21.pitch.Pitch E3>, <music21.pitch.Pitch G4>)
    ```

    * Changed in v6: inPlace defaults to False.

Chord.removeRedundantPitchNames(*\**, *inPlace=False*)[[source]](../_modules/music21/chord.html#Chord.removeRedundantPitchNames)
:   Remove all but the FIRST instance of a pitch class with more than one
    instance of that pitch name regardless of octave (but note that
    spelling matters, so that in the example, the F-flat stays even
    though there is already an E.)

    If inPlace is True, a copy is not made and a list of deleted pitches is returned;
    otherwise a copy is made and that copy is returned.

    ```python
    >>> c2 = chord.Chord(['c5', 'e3', 'g4', 'c2', 'e3', 'f-4'])
    >>> c2
    <music21.chord.Chord C5 E3 G4 C2 E3 F-4>
    ```

    ```python
    >>> rem = c2.removeRedundantPitchNames(inPlace=True)
    >>> c2
    <music21.chord.Chord C5 E3 G4 F-4>
    >>> rem
    [<music21.pitch.Pitch C2>, <music21.pitch.Pitch E3>]
    ```

    * Changed in v6: inPlace defaults to False.

Chord.removeRedundantPitches(*\**, *inPlace=False*)[[source]](../_modules/music21/chord.html#Chord.removeRedundantPitches)
:   Remove all but one instance of a pitch that appears twice.

    It removes based on the name of the note and the octave, so the same
    note name in two different octaves is retained.

    If inPlace is True, a copy is not made and a list of deleted pitches is returned;
    otherwise make and return a copy.

    ```python
    >>> c1 = chord.Chord(['c2', 'e3', 'g4', 'e3'])
    >>> c1
    <music21.chord.Chord C2 E3 G4 E3>
    ```

    ```python
    >>> removedList = c1.removeRedundantPitches(inPlace=True)
    >>> c1
    <music21.chord.Chord C2 E3 G4>
    >>> removedList
    [<music21.pitch.Pitch E3>]
    ```

    ```python
    >>> c1.forteClass
    '3-11B'
    ```

    ```python
    >>> c2 = chord.Chord(['c2', 'e3', 'g4', 'c5'])
    >>> c2c = c2.removeRedundantPitches(inPlace=False)
    >>> c2c
    <music21.chord.Chord C2 E3 G4 C5>
    ```

    It is a known bug that because pitch.nameWithOctave gives
    the same value for B-flat in octave 1 as B-natural in octave
    negative 1, negative octaves can screw up this method.
    With all the things left to do for music21, it doesn’t seem
    a bug worth squashing at this moment, but FYI:

    ```python
    >>> p1 = pitch.Pitch('B-')
    >>> p1.octave = 1
    >>> p2 = pitch.Pitch('B')
    >>> p2.octave = -1
    >>> c3 = chord.Chord([p1, p2])
    >>> removedPitches = c3.removeRedundantPitches(inPlace=True)
    >>> c3.pitches
    (<music21.pitch.Pitch B-1>,)
    ```

    ```python
    >>> c3.pitches[0].name
    'B-'
    >>> c3.pitches[0].octave
    1
    >>> removedPitches
    [<music21.pitch.Pitch B-1>]
    >>> removedPitches[0].name
    'B'
    >>> removedPitches[0].octave
    -1
    ```

    The first pitch survives:

    ```python
    >>> c3.pitches[0] is p1
    True
    ```

    ```python
    >>> c3.pitches[0] is p2
    False
    ```

    * Changed in v6: inPlace defaults to False.

Chord.root(*newroot: [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\**, *find: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")[[source]](../_modules/music21/chord.html#Chord.root)

Chord.root(*newroot: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") | [Note](moduleNote.html#music21.note.Note "music21.note.Note")*, *\**, *find: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
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

Chord.semiClosedPosition(*\**, *forceOctave*, *inPlace: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[True]*, *leaveRedundantPitches=False*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/chord.html#Chord.semiClosedPosition)

Chord.semiClosedPosition(*\**, *forceOctave=None*, *inPlace: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[False] = False*, *leaveRedundantPitches=False*) → [Self](https://docs.python.org/3/library/typing.html#typing.Self "(in Python v3.14)")
:   Similar to `ClosedPosition()` in that it
    moves everything within an octave EXCEPT if there’s already
    a pitch at that step, then it puts it up an octave. It’s a
    very useful display standard for dense post-tonal chords.

    ```python
    >>> c1 = chord.Chord(['C3', 'E5', 'C#6', 'E-7', 'G8', 'C9', 'E#9'])
    >>> c2 = c1.semiClosedPosition(inPlace=False)
    >>> c2
    <music21.chord.Chord C3 E-3 G3 C#4 E4 E#5>
    ```

    leaveRedundantPitches still works, and gives them a new octave!

    ```python
    >>> c3 = c1.semiClosedPosition(
    ...     inPlace=False,
    ...     leaveRedundantPitches=True,
    ...     )
    >>> c3
    <music21.chord.Chord C3 E-3 G3 C4 E4 C#5 E#5>
    ```

    of course forceOctave still works, as does inPlace=True.

    ```python
    >>> c1.semiClosedPosition(
    ...     forceOctave=2,
    ...     inPlace=True,
    ...     leaveRedundantPitches=True,
    ...     )
    >>> c1
    <music21.chord.Chord C2 E-2 G2 C3 E3 C#4 E#4>
    ```

Chord.semitonesFromChordStep(*chordStep*, *testRoot=None*)[[source]](../_modules/music21/chord.html#Chord.semitonesFromChordStep)
:   Returns the number of semitones (mod12) above the root that the
    chordStep lies (i.e., 3 = third of the chord; 5 = fifth, etc.) if one
    exists. Or None if it does not exist.

    You can optionally specify a note.Note object to try as the root. It
    does not change the Chord.root object. We use these methods to figure
    out what the root of the triad is.

    Currently, there is a bug that in the case of a triply diminished third
    (e.g., “c” => “e—-“), this function will incorrectly claim no third
    exists. Perhaps this should be construed as a feature.

    In the case of chords such as C, E-, E, semitonesFromChordStep(3)
    will return the number for the first third, in this case 3. It
    will not return 4, nor a list object (3, 4). You probably do not
    want to be using tonal chord manipulation functions on chords such
    as these anyway. Check for such cases with
    chord.hasAnyRepeatedDiatonicNote first.

    Tools with the expression “chordStep” in them refer to the diatonic
    third, fifth, etc., of the chord. They have little to do with
    the scale degree of the scale or key that the chord is embedded
    within. See “chord.scaleDegrees” for this functionality.

    ```python
    >>> cChord = chord.Chord(['E3', 'C4', 'G5'])
    >>> cChord.semitonesFromChordStep(3)  # distance from C to E
    4
    ```

    ```python
    >>> cChord.semitonesFromChordStep(5)  # C to G
    7
    ```

    Omitted chordSteps return None

    ```python
    >>> print(cChord.semitonesFromChordStep(6))
    None
    ```

    Note that the routine returns the semitones to the FIRST third.
    This chord has two thirds, C and C#

    ```python
    >>> aChord = chord.Chord(['a2', 'c4', 'c#5', 'e#7'])
    >>> aChord.semitonesFromChordStep(3)
    3
    ```

    ```python
    >>> aChord.semitonesFromChordStep(5)
    8
    >>> print(aChord.semitonesFromChordStep(2))
    None
    ```

    Test whether this strange chord gets the B# as 0 semitones:

    ```python
    >>> c = chord.Chord(['C4', 'E4', 'G4', 'B#4'])
    >>> c.semitonesFromChordStep(7)
    0
    ```

    If testRoot is set to a Pitch object then that note is used as the root of the chord
    regardless of anything else that might be considered.

    A-minor: 1st inversion.

    ```python
    >>> aMin = chord.Chord(['C4', 'E4', 'A4'])
    >>> aMin.semitonesFromChordStep(3)
    3
    >>> aMin.semitonesFromChordStep(5)
    7
    ```

    C6 chord, jazz like, root position:

    ```python
    >>> cPitch = pitch.Pitch('C4')
    >>> c6 = aMin  # renaming for clarity
    >>> c6.semitonesFromChordStep(3, testRoot = cPitch)
    4
    >>> c6.semitonesFromChordStep(5, testRoot = cPitch) is None
    True
    >>> c6.semitonesFromChordStep(6, testRoot = cPitch)
    9
    ```

Chord.setColor(*value*, *pitchTarget=None*)[[source]](../_modules/music21/chord.html#Chord.setColor)
:   Set color for specific pitch.

    ```python
    >>> c = chord.Chord('C4 E4 G4')
    >>> c.setColor('red', 'C4')
    >>> c['0.style.color']
    'red'
    >>> c.setColor('blue')  # set for whole chord
    >>> c.style.color
    'blue'
    >>> c['E4.style.color']
    'blue'
    ```

    ```python
    >>> c.setColor('red', 'C9')
    Traceback (most recent call last):
    music21.chord.ChordException: the given pitch is not in the Chord: C9
    ```

Chord.setNotehead(*nh*, *pitchTarget*)[[source]](../_modules/music21/chord.html#Chord.setNotehead)
:   Given a notehead attribute as a string and a pitch object in this
    Chord, set the notehead attribute of that pitch to the value of that
    notehead. Valid notehead type names are found in note.noteheadTypeNames
    (see below):

    ```python
    >>> for noteheadType in note.noteheadTypeNames:
    ...    noteheadType
    ...
    'arrow down'
    'arrow up'
    'back slashed'
    'circle dot'
    'circle-x'
    'circled'
    'cluster'
    'cross'
    'diamond'
    'do'
    'fa'
    'fa up'
    'inverted triangle'
    'la'
    'left triangle'
    'mi'
    'none'
    'normal'
    'other'
    're'
    'rectangle'
    'slash'
    'slashed'
    'so'
    'square'
    'ti'
    'triangle'
    'x'
    ```

    ```python
    >>> n1 = note.Note('D4')
    >>> n2 = note.Note('G4')
    >>> c1 = chord.Chord([n1, n2])
    >>> c1.setNotehead('diamond', c1.pitches[1])  # just to g
    >>> c1.getNotehead(c1.pitches[1])
    'diamond'
    ```

    ```python
    >>> c1.getNotehead(c1.pitches[0])
    'normal'
    ```

    If a chord has two of the same pitch, but each associated with a different notehead, then
    object equality must be used to distinguish between the two.

    ```python
    >>> c2 = chord.Chord(['D4', 'D4'])
    >>> secondD4 = c2.pitches[1]
    >>> c2.setNotehead('diamond', secondD4)
    >>> for i in [0, 1]:
    ...     c2.getNotehead(c2.pitches[i])
    ...
    'normal'
    'diamond'
    ```

    By default, assigns to first pitch:

    ```python
    >>> c3 = chord.Chord('C3 F4')
    >>> c3.setNotehead('slash', None)
    >>> c3['0.notehead']
    'slash'
    ```

    Less safe to match by string, but possible:

    ```python
    >>> c3.setNotehead('so', 'F4')
    >>> c3['1.notehead']
    'so'
    ```

    Error:

    ```python
    >>> c3.setNotehead('so', 'G4')
    Traceback (most recent call last):
    music21.chord.ChordException: the given pitch is not in the Chord: G4
    ```

Chord.setNoteheadFill(*nh*, *pitchTarget*)[[source]](../_modules/music21/chord.html#Chord.setNoteheadFill)
:   Given a noteheadFill attribute as a string (or False) and a pitch object in this
    Chord, set the noteheadFill attribute of that pitch to the value of that
    notehead. Valid noteheadFill names are True, False, None (default)

    ```python
    >>> n1 = note.Note('D4')
    >>> n2 = note.Note('G4')
    >>> c1 = chord.Chord([n1, n2])
    >>> c1.setNoteheadFill(False, c1.pitches[1])  # just to g
    >>> c1.getNoteheadFill(c1.pitches[1])
    False
    ```

    ```python
    >>> c1.getNoteheadFill(c1.pitches[0]) is None
    True
    ```

    If a chord has two of the same pitch, but each associated with a different notehead, then
    object equality must be used to distinguish between the two.

    ```python
    >>> c2 = chord.Chord(['D4', 'D4'])
    >>> secondD4 = c2.pitches[1]
    >>> c2.setNoteheadFill(False, secondD4)
    >>> for i in [0, 1]:
    ...     print(c2.getNoteheadFill(c2.pitches[i]))
    ...
    None
    False
    ```

    By default, assigns to first pitch:

    ```python
    >>> c3 = chord.Chord('C3 F4')
    >>> c3.setNoteheadFill(False, None)
    >>> c3['0.noteheadFill']
    False
    ```

    Less safe to match by string, but possible:

    ```python
    >>> c3.setNoteheadFill(True, 'F4')
    >>> c3['1.noteheadFill']
    True
    ```

    Error:
    >>> c3.setNoteheadFill(True, ‘G4’)
    Traceback (most recent call last):
    music21.chord.ChordException: the given pitch is not in the Chord: G4

Chord.setStemDirection(*stem*, *pitchTarget*)[[source]](../_modules/music21/chord.html#Chord.setStemDirection)
:   Given a stem attribute as a string and a pitch object in this Chord,
    set the stem attribute of that pitch to the value of that stem. Valid
    stem directions are found note.stemDirectionNames (see below).

    ```python
    >>> for name in note.stemDirectionNames:
    ...     name
    ...
    'double'
    'down'
    'noStem'
    'none'
    'unspecified'
    'up'
    ```

    ```python
    >>> n1 = note.Note('D4')
    >>> n2 = note.Note('G4')
    >>> c1 = chord.Chord([n1, n2])
    >>> c1.setStemDirection('double', c1.pitches[1])  # just to g
    >>> c1.getStemDirection(c1.pitches[1])
    'double'
    ```

    ```python
    >>> c1.getStemDirection(c1.pitches[0])
    'unspecified'
    ```

    If a chord has two of the same pitch, but each associated with a
    different stem, then object equality must be used to distinguish
    between the two.

    ```python
    >>> c2 = chord.Chord(['D4', 'D4'])
    >>> secondD4 = c2.pitches[1]
    >>> c2.setStemDirection('double', secondD4)
    >>> for i in [0, 1]:
    ...    print(c2.getStemDirection(c2.pitches[i]))
    ...
    unspecified
    double
    ```

    By default, assigns to first pitch:

    ```python
    >>> c3 = chord.Chord('C3 F4')
    >>> c3.setStemDirection('down', None)
    >>> c3['0.stemDirection']
    'down'
    ```

    Less safe to match by string, but possible:

    ```python
    >>> c3.setStemDirection('down', 'F4')
    >>> c3['1.stemDirection']
    'down'
    ```

    Error:
    >>> c3.setStemDirection(‘up’, ‘G4’)
    Traceback (most recent call last):
    music21.chord.ChordException: the given pitch is not in the Chord: G4

Chord.setTie(*tieObjOrStr: [Tie](moduleTie.html#music21.tie.Tie "music21.tie.Tie") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *pitchTarget*)[[source]](../_modules/music21/chord.html#Chord.setTie)
:   Given a tie object (or a tie type string) and a pitch or Note in this Chord,
    set the pitch’s tie attribute in this chord to that tie type.

    ```python
    >>> c1 = chord.Chord(['d3', 'e-4', 'b-4'])
    >>> t1 = tie.Tie('start')
    >>> c1.setTie(t1, 'b-4')  # or it can be done with a pitch.Pitch object
    >>> c1.getTie(c1.pitches[2]) is t1
    True
    ```

    Setting a tie with a chord with the same pitch twice requires
    getting the exact pitch object out to be sure which one:

    ```python
    >>> c2 = chord.Chord(['D4', 'D4'])
    >>> secondD4 = c2.pitches[1]
    >>> c2.setTie('start', secondD4)
    >>> for i in [0, 1]:
    ...    print(c2.getTie(c2.pitches[i]))
    ...
    None
    <music21.tie.Tie start>
    ```

    ```python
    >>> c3 = chord.Chord('C3 F4')
    >>> c3.setTie('start', None)
    >>> c3.getTie(c3.pitches[0])
    <music21.tie.Tie start>
    ```

    Less safe to match by string, because there might be multiple
    pitches with the same name in the chord, but possible:

    ```python
    >>> c4 = chord.Chord('D4 F#4')
    >>> c4.setTie('start', 'F#4')
    >>> c4.getTie('F#4')
    <music21.tie.Tie start>
    ```

    Setting a tie on a note not in the chord is an error:

    ```python
    >>> c3.setTie('stop', 'G4')
    Traceback (most recent call last):
    music21.chord.ChordException: the given pitch is not in the Chord: G4
    ```

Chord.setVolume(*vol: [Volume](moduleVolume.html#music21.volume.Volume "music21.volume.Volume")*, *target: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Note](moduleNote.html#music21.note.Note "music21.note.Note") | [Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")*)[[source]](../_modules/music21/chord.html#Chord.setVolume)
:   Set the [`Volume`](moduleVolume.html#music21.volume.Volume "music21.volume.Volume") object of a specific Pitch.

    * Changed in v8: after appearing in ChordBase in v7, it has been properly
      :   moved back to Chord itself. The ability to change just the first note’s
          volume has been removed. Use Chord().volume = vol to change the
          volume for a whole chord.

Chord.simplifyEnharmonics(*\**, *inPlace=False*, *keyContext=None*)[[source]](../_modules/music21/chord.html#Chord.simplifyEnharmonics)
:   Calls pitch.simplifyMultipleEnharmonics on the pitches of the chord.

    Simplifies the enharmonics in the sense of making a more logical chord. Note below
    that E# is added there because C# major is simpler than C# F G#.

    ```python
    >>> c = chord.Chord('C# F G#')
    >>> c.pitches
    (<music21.pitch.Pitch C#>, <music21.pitch.Pitch F>, <music21.pitch.Pitch G#>)
    ```

    ```python
    >>> c.simplifyEnharmonics(inPlace=True)
    >>> c.pitches
    (<music21.pitch.Pitch C#>, <music21.pitch.Pitch E#>, <music21.pitch.Pitch G#>)
    ```

    If keyContext is provided the enharmonics are simplified based on the supplied
    Key or KeySignature.

    ```python
    >>> c.simplifyEnharmonics(inPlace=True, keyContext=key.Key('A-'))
    >>> c.pitches
    (<music21.pitch.Pitch D->, <music21.pitch.Pitch F>, <music21.pitch.Pitch A->)
    ```

Chord.sortAscending(*\**, *inPlace=False*)[[source]](../_modules/music21/chord.html#Chord.sortAscending)

Chord.sortChromaticAscending()[[source]](../_modules/music21/chord.html#Chord.sortChromaticAscending)
:   Same as sortAscending but notes are sorted by midi number, so F## sorts above G-.

Chord.sortDiatonicAscending(*\**, *inPlace=False*)[[source]](../_modules/music21/chord.html#Chord.sortDiatonicAscending)
:   The notes are sorted by [`diatonicNoteNum`](modulePitch.html#music21.pitch.Pitch.diatonicNoteNum "music21.pitch.Pitch.diatonicNoteNum")
    or vertical position on a grand staff (so F## sorts below G-).
    Notes that are the identical diatonicNoteNum are further sorted by
    [`ps`](modulePitch.html#music21.pitch.Pitch.ps "music21.pitch.Pitch.ps") (midi numbers that accommodate floats).

    We return a new Chord object with the notes arranged from lowest to highest
    (unless inPlace=True)

    ```python
    >>> cMajUnsorted = chord.Chord(['E4', 'C4', 'G4'])
    >>> cMajSorted = cMajUnsorted.sortDiatonicAscending()
    >>> cMajSorted.pitches[0].name
    'C'
    ```

    ```python
    >>> c2 = chord.Chord(['E4', 'C4', 'G4'])
    >>> c2.sortDiatonicAscending(inPlace=True)
    >>> c2
    <music21.chord.Chord C4 E4 G4>
    ```

    ```python
    >>> sameDNN = chord.Chord(['F#4', 'F4'])
    >>> sameDNN.sortDiatonicAscending()
    <music21.chord.Chord F4 F#4>
    ```

    * Changed in v6: if inPlace is True do not return anything.

Chord.sortFrequencyAscending()[[source]](../_modules/music21/chord.html#Chord.sortFrequencyAscending)
:   Same as above, but uses a note’s frequency to determine height; so that
    C# would be below D- in 1/4-comma meantone, equal in equal temperament,
    but below it in (most) just intonation types.

Chord.transpose(*value*, *\**, *inPlace=False*)[[source]](../_modules/music21/chord.html#Chord.transpose)
:   Transpose the Chord by the user-provided value. If the value
    is an integer, the transposition is treated in half steps and
    enharmonics might be simplified (not done yet). If the value is a
    string, any Interval string specification can be provided.

    If inPlace is set to True (default = False) then the original
    chord is changed. Otherwise a new Chord is returned.

    We take a three-note chord (G, A, C#) and transpose it up a minor
    third, getting the chord B-flat, C, E.

    ```python
    >>> a = chord.Chord(['g4', 'a3', 'c#6'])
    >>> b = a.transpose('m3')
    >>> b
    <music21.chord.Chord B-4 C4 E6>
    ```

    Here we create the interval object first (rather than giving
    a string) and specify transposing down six semitones, instead
    of saying A-4.

    ```python
    >>> aInterval = interval.Interval(-6)
    >>> b = a.transpose(aInterval)
    >>> b
    <music21.chord.Chord C#4 E-3 G5>
    ```

    If inPlace is True then rather than returning a new chord, the
    chord itself is changed.

    ```python
    >>> a.transpose(aInterval, inPlace=True)
    >>> a
    <music21.chord.Chord C#4 E-3 G5>
    ```

Methods inherited from [`ChordBase`](#music21.chord.ChordBase "music21.chord.ChordBase"):

|  |  |  |
| --- | --- | --- |
| * [`hasComponentVolumes()`](#music21.chord.ChordBase.hasComponentVolumes "music21.chord.ChordBase.hasComponentVolumes") | * [`remove()`](#music21.chord.ChordBase.remove "music21.chord.ChordBase.remove") | * [`setVolumes()`](#music21.chord.ChordBase.setVolumes "music21.chord.ChordBase.setVolumes") |

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

[`Chord`](#music21.chord.Chord "music21.chord.Chord") instance variables

Chord.beams
:   A [`Beams`](moduleBeam.html#music21.beam.Beams "music21.beam.Beams") object that contains
    information about the beaming of this note.

Chord.isChord
:   Boolean read-only value describing if this
    GeneralNote object is a Chord. Is True

Chord.isNote
:   Boolean read-only value describing if this
    GeneralNote object is a Note. Is False

Chord.isRest
:   Boolean read-only value describing if this
    GeneralNote object is a Rest. Is False

    ```python
    >>> c = chord.Chord()
    >>> c.isRest
    False
    ```

Instance variables inherited from [`ChordBase`](#music21.chord.ChordBase "music21.chord.ChordBase"):

|  |  |  |
| --- | --- | --- |
| * [`beams`](#music21.chord.ChordBase.beams "music21.chord.ChordBase.beams") | * [`isNote`](#music21.chord.ChordBase.isNote "music21.chord.ChordBase.isNote") | * [`isRest`](#music21.chord.ChordBase.isRest "music21.chord.ChordBase.isRest") |

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

## ChordBase

class music21.chord.ChordBase(*notes: [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")] | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[ChordBase](#music21.chord.ChordBase "music21.chord.ChordBase")] | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[NotRest](moduleNote.html#music21.note.NotRest "music21.note.NotRest")] | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] = None*, *\*\*keywords*)[[source]](../_modules/music21/chord.html#ChordBase)
:   A base class for NotRest objects that have multiple underlying structures
    like notes or unpitched percussion.

    As of Version 7, ChordBase lies between Chord and NotRest in the music21
    hierarchy, so that features can be shared with PercussionChord.

    ```python
    >>> cb = chord.ChordBase('C4 E4 G4')
    >>> cb.notes
    (<music21.note.Note C>, <music21.note.Note E>, <music21.note.Note G>)
    ```

    **Equality**

    Equality on ChordBase is strange, but necessary to help Chord and PercussionChord
    do meaningful equality checks themselves.

    Two ChordBase objects are equal if they pass all super()
    equality tests and the **number** of stored Notes are the same.

    ```python
    >>> cb1 = chord.ChordBase('C4 E4 G4')
    >>> cb2 = chord.ChordBase('C4 E4')
    >>> cb1 == cb2
    False
    ```

    This is surprising, but it’s necessary to make checking equality
    of Chord objects and PercussionChord objects themselves easier.

    ```python
    >>> cb3 = chord.ChordBase('A#4 A#4 A#4')
    >>> cb1 == cb3
    True
    ```

[`ChordBase`](#music21.chord.ChordBase "music21.chord.ChordBase") bases

* [`NotRest`](moduleNote.html#music21.note.NotRest "music21.note.NotRest")
* [`GeneralNote`](moduleNote.html#music21.note.GeneralNote "music21.note.GeneralNote")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`ChordBase`](#music21.chord.ChordBase "music21.chord.ChordBase") read-only properties

ChordBase.notes

Read-only properties inherited from [`GeneralNote`](moduleNote.html#music21.note.GeneralNote "music21.note.GeneralNote"):

|  |  |  |
| --- | --- | --- |
| * [`fullName`](moduleNote.html#music21.note.GeneralNote.fullName "music21.note.GeneralNote.fullName") |  |  |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`ChordBase`](#music21.chord.ChordBase "music21.chord.ChordBase") read/write properties

ChordBase.tie
:   Get or set a single tie based on all the ties in this Chord.

    This overloads the behavior of the tie attribute found in all
    NotRest classes.

    If setting a tie, tie is applied to all pitches.

    ```python
    >>> c1 = chord.Chord(['c4', 'g4'])
    >>> tie1 = tie.Tie('start')
    >>> c1.tie = tie1
    >>> c1.tie
    <music21.tie.Tie start>
    ```

    ```python
    >>> c1.getTie(c1.pitches[1])
    <music21.tie.Tie start>
    ```

ChordBase.volume
:   Get or set the [`Volume`](moduleVolume.html#music21.volume.Volume "music21.volume.Volume") object for this
    Chord.

    When setting the .volume property, all pitches are treated as
    having the same Volume object.

    ```python
    >>> c = chord.Chord(['g#', 'd-'])
    >>> c.volume
    <music21.volume.Volume realized=0.71>
    ```

    ```python
    >>> c.volume = volume.Volume(velocity=64)
    >>> c.volume.velocityIsRelative = False
    >>> c.volume
    <music21.volume.Volume realized=0.5>
    ```

    * Changed in v8: setting volume to a list of volumes is no longer supported.
      See [`setVolumes()`](#music21.chord.ChordBase.setVolumes "music21.chord.ChordBase.setVolumes") instead

Read/write properties inherited from [`NotRest`](moduleNote.html#music21.note.NotRest "music21.note.NotRest"):

|  |  |  |
| --- | --- | --- |
| * [`notehead`](moduleNote.html#music21.note.NotRest.notehead "music21.note.NotRest.notehead") * [`noteheadFill`](moduleNote.html#music21.note.NotRest.noteheadFill "music21.note.NotRest.noteheadFill") | * [`noteheadParenthesis`](moduleNote.html#music21.note.NotRest.noteheadParenthesis "music21.note.NotRest.noteheadParenthesis") * [`stemDirection`](moduleNote.html#music21.note.NotRest.stemDirection "music21.note.NotRest.stemDirection") | * [`storedInstrument`](moduleNote.html#music21.note.NotRest.storedInstrument "music21.note.NotRest.storedInstrument") |

Read/write properties inherited from [`GeneralNote`](moduleNote.html#music21.note.GeneralNote "music21.note.GeneralNote"):

|  |  |  |
| --- | --- | --- |
| * [`lyric`](moduleNote.html#music21.note.GeneralNote.lyric "music21.note.GeneralNote.lyric") | * [`pitches`](moduleNote.html#music21.note.GeneralNote.pitches "music21.note.GeneralNote.pitches") |  |

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`ChordBase`](#music21.chord.ChordBase "music21.chord.ChordBase") methods

ChordBase.\_\_eq\_\_(*other*)[[source]](../_modules/music21/chord.html#ChordBase.__eq__)
:   Define equality for Music21Objects. See main class docs.

ChordBase.add(*notes*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/chord.html#ChordBase.add)
:   Add a Note, Pitch, the .notes of another chord,
    or string representing a Pitch,
    or a list of any-of-the-above types to a Chord or PercussionChord.

    Does no sorting. That is on the Chord object.

    ```python
    >>> c = chord.Chord('C4 E4 G4')
    >>> c.add('B3')
    >>> c
    <music21.chord.Chord B3 C4 E4 G4>
    >>> c.duration
    <music21.duration.Duration 1.0>
    ```

    ```python
    >>> c.add('A2', runSort=False)
    >>> c
    <music21.chord.Chord B3 C4 E4 G4 A2>
    ```

    ```python
    >>> c.add(['B5', 'C6'])
    >>> c
    <music21.chord.Chord A2 B3 C4 E4 G4 B5 C6>
    ```

    ```python
    >>> c.add(pitch.Pitch('D6'))
    >>> c
    <music21.chord.Chord A2 B3 C4 E4 G4 B5 C6 D6>
    ```

    ```python
    >>> n = note.Note('E6')
    >>> n.duration.type = 'half'
    >>> c.add(n)
    >>> c
    <music21.chord.Chord A2 B3 C4 E4 G4 B5 C6 D6 E6>
    >>> c.duration
    <music21.duration.Duration 1.0>
    >>> c[-1]
    <music21.note.Note E>
    >>> c[-1].duration
    <music21.duration.Duration 2.0>
    ```

ChordBase.hasComponentVolumes() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/chord.html#ChordBase.hasComponentVolumes)
:   Utility method to determine if this object has component
    [`Volume`](moduleVolume.html#music21.volume.Volume "music21.volume.Volume") objects assigned to each
    note-component.

    ```python
    >>> c1 = chord.Chord(['c4', 'd-1', 'g6'])
    >>> c1.setVolumes([60, 20, 120])
    >>> [n.volume.velocity for n in c1]
    [60, 20, 120]
    ```

    ```python
    >>> c1.hasComponentVolumes()
    True
    ```

    ```python
    >>> c2 = chord.Chord(['c4', 'd-1', 'g6'])
    >>> c2.volume.velocity = 23
    >>> c2.hasComponentVolumes()
    False
    ```

    ```python
    >>> c3 = chord.Chord(['c4', 'd-1', 'g6'])
    >>> c3.setVolumes([0.2, 0.5, 0.8])
    >>> [n.volume.velocity for n in c3]
    [25, 64, 102]
    ```

    ```python
    >>> c4 = chord.Chord(['c4', 'd-1', 'g6'])
    >>> c4.volume = 89
    >>> c4.volume.velocity
    89
    ```

    ```python
    >>> c4.hasComponentVolumes()
    False
    ```

ChordBase.remove(*removeItem*)[[source]](../_modules/music21/chord.html#ChordBase.remove)
:   Removes a note or pitch from the chord. Must be a pitch
    equal to a pitch in the chord or a string specifying the pitch
    name with octave or a note from a chord. If not found,
    raises a ValueError

    ```python
    >>> c = chord.Chord('C4 E4 G4')
    >>> c.remove('E4')
    >>> c
    <music21.chord.Chord C4 G4>
    >>> c.remove('D5')
    Traceback (most recent call last):
    ValueError: Chord.remove(x), x not in chord
    ```

    ```python
    >>> c = chord.Chord('C4 E4 G4')
    >>> c.remove(pitch.Pitch('E4'))
    >>> c
    <music21.chord.Chord C4 G4>
    >>> c.remove(pitch.Pitch('F#5'))
    Traceback (most recent call last):
    ValueError: Chord.remove(x), x not in chord
    ```

    The Note also does not need to be the exact note of the
    chord, just matches on equality

    ```python
    >>> c = chord.Chord('C4 E4 G4')
    >>> c.remove(note.Note('E4'))
    >>> c
    <music21.chord.Chord C4 G4>
    ```

    ```python
    >>> c.remove(c[1])
    >>> c
    <music21.chord.Chord C4>
    ```

    ```python
    >>> c.remove(note.Note('B-2'))
    Traceback (most recent call last):
    ValueError: Chord.remove(x), x not in chord
    ```

    ```python
    >>> c.remove(4)
    Traceback (most recent call last):
    ValueError: Cannot remove 4 from a chord; try a Pitch or Note object
    ```

    Like Python’s list object, the remove method of chord does not take a list of strings.

    ```python
    >>> c = chord.Chord('C4 E4 G4')
    >>> c.remove(['C4', 'E4'])
    Traceback (most recent call last):
    ValueError: Cannot remove ['C4', 'E4'] from a chord; try a Pitch or Note object
    ```

ChordBase.setVolumes(*volumes: Sequence['music21.volume.Volume' | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")]*)[[source]](../_modules/music21/chord.html#ChordBase.setVolumes)
:   Set as many individual volumes as appear in volumes. If there are not
    enough volumes, then cycles through the list of volumes here:

    ```python
    >>> c = chord.Chord(['g#', 'd-'])
    >>> c.setVolumes([volume.Volume(velocity=96), volume.Volume(velocity=96)])
    >>> c.hasComponentVolumes()
    True
    ```

    Note that this means that the chord itself does not have a volume at this moment!

    ```python
    >>> c.hasVolumeInformation()
    False
    ```

    ```python
    >>> c.volume.velocity
    96
    ```

    But after having called the volume, now it does:

    ```python
    >>> c.hasVolumeInformation()
    True
    ```

    ```python
    >>> c.volume.velocityIsRelative = False
    >>> c.volume
    <music21.volume.Volume realized=0.76>
    ```

    * New in v8: replaces setting .volume to a list

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

[`ChordBase`](#music21.chord.ChordBase "music21.chord.ChordBase") instance variables

ChordBase.beams
:   A [`Beams`](moduleBeam.html#music21.beam.Beams "music21.beam.Beams") object that contains
    information about the beaming of this note.

ChordBase.isNote
:   Boolean read-only value describing if this
    GeneralNote object is a Note. Is False

ChordBase.isRest
:   Boolean read-only value describing if this
    GeneralNote object is a Rest. Is False

    ```python
    >>> c = chord.Chord()
    >>> c.isRest
    False
    ```

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

music21.chord.fromForteClass(*notation: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*) → [Chord](#music21.chord.Chord "music21.chord.Chord")[[source]](../_modules/music21/chord.html#fromForteClass)
:   Return a Chord given a Forte-class notation. The Forte class can be
    specified as string (e.g., 3-11) or as a list of cardinality and number
    (e.g., [8, 1]).

    If no match is available, None is returned.

    ```python
    >>> chord.fromForteClass('3-11')
    <music21.chord.Chord C E- G>
    ```

    ```python
    >>> chord.fromForteClass('3-11b')
    <music21.chord.Chord C E G>
    ```

    ```python
    >>> chord.fromForteClass('3-11a')
    <music21.chord.Chord C E- G>
    ```

    ```python
    >>> chord.fromForteClass((11, 1))
    <music21.chord.Chord C D- D E- E F G- G A- A B->
    ```

music21.chord.fromIntervalVector(*notation*, *getZRelation=False*)[[source]](../_modules/music21/chord.html#fromIntervalVector)
:   Return one or more Chords given an interval vector.

    ```python
    >>> chord.fromIntervalVector([0, 0, 0, 0, 0, 1])
    <music21.chord.Chord C F#>
    ```

    ```python
    >>> chord.fromIntervalVector((5, 5, 5, 5, 5, 5)) is None
    True
    ```

    ```python
    >>> chord.fromIntervalVector((1, 1, 1, 1, 1, 1))
    <music21.chord.Chord C C# E F#>
    ```

    ```python
    >>> chord.fromIntervalVector((1, 1, 1, 1, 1, 1), getZRelation=True)
    <music21.chord.Chord C D- E- G>
    ```

    ```python
    >>> chord.fromIntervalVector((1, 1, 1, 1, 1, 1)).getZRelation()
    <music21.chord.Chord C D- E- G>
    ```
