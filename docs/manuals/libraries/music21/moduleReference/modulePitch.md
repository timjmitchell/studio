Source: https://music21.org/music21docs/moduleReference/modulePitch.html

# music21.pitch

Classes for representing and manipulating pitches, pitch-space, and accidentals.

Each [`Note`](moduleNote.html#music21.note.Note "music21.note.Note") object has a Pitch object embedded in it.
Some methods below, such as Pitch.name, Pitch.step, etc. are
made available directly in the Note object, so they will seem familiar.

## Pitch

class music21.pitch.Pitch(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\**, *step: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")['C', 'D', 'E', 'F', 'G', 'A', 'B'] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *octave: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *accidental: [Accidental](#music21.pitch.Accidental "music21.pitch.Accidental") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *microtone: [Microtone](#music21.pitch.Microtone "music21.pitch.Microtone") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *pitchClass: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")['a', 'A', 't', 'T', 'b', 'B', 'e', 'E'] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *midi: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *ps: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *fundamental: [Pitch](#music21.pitch.Pitch "music21.pitch.Pitch") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\*\*keywords*)[[source]](../_modules/music21/pitch.html#Pitch)
:   A fundamental object that represents a single pitch.

    Pitch objects are most often created by passing in a note name
    (C, D, E, F, G, A, B), an optional accidental (one or more “#”s or “-“s,
    where “-” means flat), and an optional octave number:

    ```python
    >>> highEflat = pitch.Pitch('E-6')
    >>> highEflat.name
    'E-'
    >>> highEflat.step
    'E'
    >>> highEflat.accidental
    <music21.pitch.Accidental flat>
    >>> highEflat.octave
    6
    ```

    The .nameWithOctave property gives back what we put in, ‘E-6’:

    ```python
    >>> highEflat.nameWithOctave
    'E-6'
    ```

    Pitch objects represent themselves as the class name followed
    by the .nameWithOctave:

    ```python
    >>> p1 = pitch.Pitch('a#4')
    >>> p1
    <music21.pitch.Pitch A#4>
    ```

    Printing a pitch.Pitch object or converting it
    to a string gives a more compact form:

    ```python
    >>> print(p1)
    A#4
    >>> str(p1)
    'A#4'
    ```

    Warning

    A Pitch without an accidental has a .accidental of None,
    not Natural. This can lead to problems if you assume that every
    Pitch or Note has a .accidental that you can call .alter
    or something like that on:

    ```python
    >>> c = pitch.Pitch('C4')
    >>> c.accidental is None
    True
    ```

    ```python
    >>> alters = []
    >>> for pName in ['G#5', 'B-5', 'C6']:
    ...     p = pitch.Pitch(pName)
    ...     alters.append(p.accidental.alter)
    Traceback (most recent call last):
    AttributeError: 'NoneType' object has no attribute 'alter'
    >>> alters
    [1.0, -1.0]
    ```

    If a Pitch doesn’t have an associated octave, then its
    .octave value is None. This means that it represents
    any G#, regardless of octave. Transposing this note up
    an octave doesn’t change anything.

    ```python
    >>> anyGSharp = pitch.Pitch('G#')
    >>> anyGSharp.octave is None
    True
    >>> print(anyGSharp.transpose('P8'))
    G#
    ```

    Sometimes we need an octave for a Pitch even if it’s not
    specified. For instance, we can’t play an octave-less Pitch
    in MIDI or display it on a staff. So there is an .implicitOctave
    tag to deal with these situations; by default it’s always 4 (unless
    defaults.pitchOctave is changed)

    ```python
    >>> anyGSharp.implicitOctave
    4
    ```

    If a Pitch has its .octave explicitly set, then .implicitOctave
    always equals .octave.

    ```python
    >>> highEflat.implicitOctave
    6
    ```

    If an integer or float >= 12 is passed to the constructor then it is
    used as the .ps attribute, which is for most common piano notes, the
    same as a MIDI number:

    ```python
    >>> pitch.Pitch(65)
    <music21.pitch.Pitch F4>
    ```

    ```python
    >>> pitch.Pitch(65.5).accidental
    <music21.pitch.Accidental half-sharp>
    ```

    A pitch.Pitch object can also be created using only a number
    from 0-11, that number is taken to be a pitchClass, where
    0 = C, 1 = C#/D-, etc. and no octave is set.

    ```python
    >>> p2 = pitch.Pitch(3)
    >>> p2
    <music21.pitch.Pitch E->
    >>> p2.octave is None
    True
    ```

    Since in instantiating pitches from numbers,
    pitch.Pitch(3) could be either a D# or an E-flat,
    this Pitch object has an attribute called .spellingIsInferred that
    is set to True. That means that when it is transposed or
    displayed, other functions or programs should feel free to substitute an
    enharmonically equivalent pitch in its place:

    ```python
    >>> p2.spellingIsInferred
    True
    >>> p1.spellingIsInferred
    False
    ```

    As MIDI numbers < 12 are almost unheard of in actual music,
    there is unlikely to be confusion between
    a pitchClass instantiation and a MIDI number instantiation, but if one must be
    clear, use midi= in the constructor:

    ```python
    >>> lowE = pitch.Pitch(midi=3)
    >>> lowE.name, lowE.octave
    ('E-', -1)
    ```

    Instead of using a single string or integer for creating the object, a succession
    of named keywords can be used instead:

    ```python
    >>> p3 = pitch.Pitch(name='C', accidental='#', octave=7, microtone=-30)
    >>> p3.fullName
    'C-sharp in octave 7 (-30c)'
    ```

    The full list of supported keywords are: name, accidental (which
    can be a string or an [`Accidental`](#music21.pitch.Accidental "music21.pitch.Accidental") object), octave,
    microtone (which can be a number or a [`Microtone`](#music21.pitch.Microtone "music21.pitch.Microtone") object),
    pitchClass (0-11), fundamental (another Pitch object representing the
    fundamental for this harmonic; harmonic is not yet supported, but should be),
    and midi or ps (two ways of specifying nearly the same thing, see below).

    Using keywords to create Pitch objects is especially important if
    extreme pitches might be found. For instance, the first Pitch is B-double flat
    in octave 3, not B-flat in octave -3. The second object creates that low Pitch
    properly:

    ```python
    >>> p4 = pitch.Pitch('B--3')
    >>> p4.accidental
    <music21.pitch.Accidental double-flat>
    >>> p4.octave
    3
    ```

    ```python
    >>> p5 = pitch.Pitch(step='B', accidental='-', octave=-3)
    >>> p5.accidental
    <music21.pitch.Accidental flat>
    >>> p5.octave
    -3
    ```

    Internally, pitches are represented by their
    scale step (self.step), their octave, and their
    accidental. Pitch objects use these three elements to figure out their
    pitch space representation (self.ps); altering any
    of the first three changes the pitch space (ps) representation.
    Similarly, altering the .ps representation
    alters the first three.

    ```python
    >>> aSharp = pitch.Pitch('A#5')
    >>> aSharp.ps
    82.0
    ```

    ```python
    >>> aSharp.octave = 4
    >>> aSharp.ps
    70.0
    ```

    ```python
    >>> aSharp.ps = 60.0
    >>> aSharp.nameWithOctave
    'C4'
    ```

    Two Pitches are equal if they represent the same
    pitch and are spelled the same (enharmonics do not count).
    A Pitch is greater than another Pitch if its .ps is greater than
    the other. Thus, C##4 > D-4.

    ```python
    >>> pitch.Pitch('C#5') == pitch.Pitch('C#5')
    True
    >>> pitch.Pitch('C#5') == pitch.Pitch('D-5')
    False
    >>> pitch.Pitch('C##5') > pitch.Pitch('D-5')
    True
    ```

    A consequence of comparing enharmonics for equality but .ps for comparisons
    is that a Pitch can be neither less than
    nor greater than another Pitch without being equal:

    ```python
    >>> pitch.Pitch('C#5') == pitch.Pitch('D-5')
    False
    >>> pitch.Pitch('C#5') > pitch.Pitch('D-5')
    False
    >>> pitch.Pitch('C#5') < pitch.Pitch('D-5')
    False
    ```

    To check for enharmonic equality, use the .ps attribute:

    ```python
    >>> pitch.Pitch('C#5').ps == pitch.Pitch('D-5').ps
    True
    ```

    Advanced construction of pitch with keywords:

    ```python
    >>> pitch.Pitch(name='D', accidental=pitch.Accidental('double-flat'))
    <music21.pitch.Pitch D-->
    >>> f = pitch.Pitch(pitchClass=5, octave=4,
    ...                 microtone=pitch.Microtone(30), fundamental=pitch.Pitch('B-2'))
    >>> f
    <music21.pitch.Pitch F4(+30c)>
    >>> f.fundamental
    <music21.pitch.Pitch B-2>
    ```

    If contradictory keyword attributes (like name=’E-’, accidental=’#’) are passed in,
    behavior is not defined, but unlikely to make you happy.

    Pitches are ProtoM21Objects, so they retain some attributes there
    such as .classes and .groups, but they don’t have Duration or Sites objects
    and cannot be put into Streams

[`Pitch`](#music21.pitch.Pitch "music21.pitch.Pitch") bases

* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`Pitch`](#music21.pitch.Pitch "music21.pitch.Pitch") read-only properties

Pitch.alter
:   Get the number of half-steps shifted
    by this pitch, such as 1.0 for a sharp, -1.0 for a flat,
    0.0 for a natural, 2.0 for a double sharp,
    and -0.5 for a quarter tone flat.

    Thus, the alter value combines the pitch change
    suggested by the Accidental and the Microtone combined.

    ```python
    >>> p = pitch.Pitch('g#4')
    >>> p.alter
    1.0
    >>> p.microtone = -25  # in cents
    >>> p.alter
    0.75
    ```

    To change the alter value, change either the accidental
    or the microtone.

Pitch.french
:   Read-only attribute. Returns the name
    of a Pitch in the French system
    (where A = la, B = si, B-flat = si bémol, C-sharp = do dièse, etc.)
    (Microtones and Quarter tones raise an error). Note that
    do is used instead of the also acceptable ut.

    ```python
    >>> print(pitch.Pitch('B-').french)
    si bémol
    ```

    ```python
    >>> print(pitch.Pitch('B').french)
    si
    ```

    ```python
    >>> print(pitch.Pitch('E-').french)
    mi bémol
    ```

    ```python
    >>> print(pitch.Pitch('C#').french)
    do dièse
    ```

    ```python
    >>> print(pitch.Pitch('A--').french)
    la double bémol
    ```

    ```python
    >>> p1 = pitch.Pitch('C')
    >>> p1.accidental = pitch.Accidental('half-sharp')
    >>> p1.french
    Traceback (most recent call last):
    music21.pitch.PitchException: On ne peut pas utiliser les microtones avec "french."
        Quelle Dommage!
    ```

Pitch.fullName
:   Return the most complete representation of this Pitch,
    providing name, octave, accidental, and any
    microtonal adjustments.

    ```python
    >>> p = pitch.Pitch('A-3')
    >>> p.microtone = 33.33
    >>> p.fullName
    'A-flat in octave 3 (+33c)'
    ```

    ```python
    >>> p = pitch.Pitch('A`7')
    >>> p.fullName
    'A-half-flat in octave 7'
    ```

Pitch.german
:   Read-only property. Returns a unicode string of the name
    of a Pitch in the German system
    (where B-flat = B, B = H, etc.)
    (Microtones and Quarter tones raise an error). Note that
    Ases is used instead of the also acceptable Asas.

    ```python
    >>> print(pitch.Pitch('B-').german)
    B
    >>> print(pitch.Pitch('B').german)
    H
    >>> print(pitch.Pitch('E-').german)
    Es
    >>> print(pitch.Pitch('C#').german)
    Cis
    >>> print(pitch.Pitch('A--').german)
    Ases
    >>> p1 = pitch.Pitch('C')
    >>> p1.accidental = pitch.Accidental('half-sharp')
    >>> p1.german
    Traceback (most recent call last):
    music21.pitch.PitchException:
        Es geht nicht "german" zu benutzen mit Microtönen.  Schade!
    ```

    Note these rarely used pitches:

    ```python
    >>> print(pitch.Pitch('B--').german)
    Heses
    >>> print(pitch.Pitch('B#').german)
    His
    ```

Pitch.implicitOctave
:   Returns the octave of the Pitch, or defaultOctave if
    octave was never set. To set an octave, use .octave.
    Default octave is usually 4.

    ```python
    >>> p = pitch.Pitch('C#')
    >>> p.octave is None
    True
    >>> p.implicitOctave
    4
    ```

    Cannot be set. Instead, just change the .octave of the pitch

Pitch.italian
:   Read-only attribute. Returns the name
    of a Pitch in the Italian system
    (F-sharp is fa diesis, C-flat is do bemolle, etc.)
    (Microtones and Quarter tones raise an error).

    ```python
    >>> print(pitch.Pitch('B-').italian)
    si bemolle
    >>> print(pitch.Pitch('B').italian)
    si
    >>> print(pitch.Pitch('E-9').italian)
    mi bemolle
    >>> print(pitch.Pitch('C#').italian)
    do diesis
    >>> print(pitch.Pitch('A--4').italian)
    la doppio bemolle
    >>> p1 = pitch.Pitch('C')
    >>> p1.accidental = pitch.Accidental('half-sharp')
    >>> p1.italian
    Traceback (most recent call last):
    music21.pitch.PitchException: Non si puo usare `italian` con microtoni
    ```

    Note these rarely used pitches:

    ```python
    >>> print(pitch.Pitch('E####').italian)
    mi quadruplo diesis
    >>> print(pitch.Pitch('D---').italian)
    re triplo bemolle
    ```

Pitch.spanish
:   Read-only attribute. Returns the name
    of a Pitch in Spanish
    (Microtones and Quarter tones raise an error).

    ```python
    >>> print(pitch.Pitch('B-').spanish)
    si bemol
    >>> print(pitch.Pitch('E-').spanish)
    mi bemol
    >>> print(pitch.Pitch('C#').spanish)
    do sostenido
    >>> print(pitch.Pitch('A--').spanish)
    la doble bemol
    >>> p1 = pitch.Pitch('C')
    >>> p1.accidental = pitch.Accidental('half-sharp')
    >>> p1.spanish
    Traceback (most recent call last):
    music21.pitch.PitchException: Unsupported accidental type.
    ```

    Note these rarely used pitches:

    ```python
    >>> print(pitch.Pitch('B--').spanish)
    si doble bemol
    >>> print(pitch.Pitch('B#').spanish)
    si sostenido
    ```

Pitch.unicodeName
:   Name presently returns pitch name and accidental without octave.

    ```python
    >>> a = pitch.Pitch('G#')
    >>> a.unicodeName
    'G♯'
    ```

Pitch.unicodeNameWithOctave
:   Return the pitch name with octave with unicode accidental symbols,
    if available.

    Read-only property.

    ```python
    >>> p = pitch.Pitch('C#4')
    >>> p.unicodeNameWithOctave
    'C♯4'
    ```

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`Pitch`](#music21.pitch.Pitch "music21.pitch.Pitch") read/write properties

Pitch.accidental
:   Stores an optional accidental object contained within the
    Pitch object. This might return None, which is different
    from a natural accidental:

    ```python
    >>> a = pitch.Pitch('E-')
    >>> a.accidental.alter
    -1.0
    >>> a.accidental.modifier
    '-'
    ```

    ```python
    >>> b = pitch.Pitch('C4')
    >>> b.accidental is None
    True
    >>> b.accidental = pitch.Accidental('natural')
    >>> b.accidental is None
    False
    >>> b.accidental
    <music21.pitch.Accidental natural>
    ```

Pitch.diatonicNoteNum
:   Returns (or takes) an integer that uniquely identifies the
    diatonic version of a note, that is ignoring accidentals.
    The number returned is the diatonic interval above C0 (the lowest C on
    a Bösendorfer Imperial Grand), so G0 = 5, C1 = 8, etc.
    Numbers can be negative for very low notes.

    C4 (middleC) = 29, C#4 = 29, C##4 = 29, D-4 = 30, D4 = 30, etc.

    ```python
    >>> c = pitch.Pitch('c4')
    >>> c.diatonicNoteNum
    29
    ```

    Unlike MIDI numbers (or .ps), C and C# has the same diatonicNoteNum:

    ```python
    >>> c = pitch.Pitch('c#4')
    >>> c.diatonicNoteNum
    29
    ```

    But D-double-flat has a different diatonicNoteNum than C.

    ```python
    >>> d = pitch.Pitch('d--4')
    >>> d.accidental.name
    'double-flat'
    >>> d.diatonicNoteNum
    30
    ```

    ```python
    >>> lowC = pitch.Pitch('c1')
    >>> lowC.diatonicNoteNum
    8
    ```

    ```python
    >>> b = pitch.Pitch()
    >>> b.step = 'B'
    >>> b.octave = -1
    >>> b.diatonicNoteNum
    0
    ```

    An implicitOctave of 4 is used if octave is not set:

    ```python
    >>> c = pitch.Pitch('C')
    >>> c.diatonicNoteNum
    29
    ```

    diatonicNoteNum can also be set. Changing it
    does not change the Accidental associated with the Pitch.

    ```python
    >>> lowDSharp = pitch.Pitch('C#7')  # start high !!!
    >>> lowDSharp.diatonicNoteNum = 9  # move low
    >>> lowDSharp.octave
    1
    >>> lowDSharp.name
    'D#'
    ```

    Negative diatonicNoteNums are possible,
    in case, like John Luther Adams, you want
    to notate the sounds of sub-sonic Earth rumblings.

    ```python
    >>> lowLowA = pitch.Pitch('A')
    >>> lowLowA.octave = -1
    >>> lowLowA.diatonicNoteNum
    -1
    ```

    ```python
    >>> lowLowLowD = pitch.Pitch('D')
    >>> lowLowLowD.octave = -3
    >>> lowLowLowD.diatonicNoteNum
    -19
    ```

Pitch.freq440
:   Gets the frequency of the note as if it’s in an equal temperament
    context where A4 = 440hz. The same as .frequency so long
    as no other temperaments are currently being used.

    Since we don’t have any other temperament objects at present,
    this is the same as .frequency always.

    ```python
    >>> a = pitch.Pitch('A4')
    >>> a.freq440
    440.0
    ```

Pitch.frequency
:   The frequency property gets or sets the frequency of
    the pitch in hertz.

    If the frequency has not been overridden, then
    it is computed based on A440Hz and equal temperament

    ```python
    >>> a = pitch.Pitch()
    >>> a.frequency = 440.0
    >>> a.frequency
    440.0
    >>> a.name
    'A'
    >>> a.octave
    4
    ```

    Microtones are captured if the frequency doesn’t correspond to any standard note.

    ```python
    >>> a.frequency = 450.0
    >>> a
    <music21.pitch.Pitch A~4(-11c)>
    ```

Pitch.groups
:   Similar to Groups on music21 object, returns or sets a Groups object.

Pitch.microtone
:   Returns or sets the microtone object contained within the
    Pitch object. Microtones must be supplied in cents.

    ```python
    >>> p = pitch.Pitch('E-4')
    >>> p.microtone.cents == 0
    True
    >>> p.ps
    63.0
    >>> p.microtone = 33  # adjustment in cents
    >>> str(p)
    'E-4(+33c)'
    >>> p.microtone
    <music21.pitch.Microtone (+33c)>
    ```

    ```python
    >>> (p.name, p.nameWithOctave)  # these representations are unchanged
    ('E-', 'E-4')
    >>> p.microtone = '(-12c'  # adjustment in cents
    >>> p
    <music21.pitch.Pitch E-4(-12c)>
    >>> p.microtone = pitch.Microtone(-30)
    >>> p
    <music21.pitch.Pitch E-4(-30c)>
    ```

Pitch.midi
:   Get or set a pitch value in MIDI.
    MIDI pitch values are like ps values (pitchSpace) rounded to
    the nearest integer; while the ps attribute will accommodate floats.

    ```python
    >>> c = pitch.Pitch('C4')
    >>> c.midi
    60
    >>> c.midi =  23.5
    >>> c.midi
    24
    ```

    Note that like ps (pitchSpace), MIDI notes do not distinguish between
    sharps and flats, etc.

    ```python
    >>> dSharp = pitch.Pitch('D#4')
    >>> dSharp.midi
    63
    >>> eFlat = pitch.Pitch('E-4')
    >>> eFlat.midi
    63
    ```

    Midi values are constrained to the space 0-127. Higher or lower
    values will be transposed octaves to fit in this space.

    ```python
    >>> veryHighFHalfFlat = pitch.Pitch('F')
    >>> veryHighFHalfFlat.octave = 12
    >>> veryHighFHalfFlat.accidental = pitch.Accidental('half-flat')
    >>> veryHighFHalfFlat
    <music21.pitch.Pitch F`12>
    >>> veryHighFHalfFlat.ps
    160.5
    >>> veryHighFHalfFlat.midi
    125
    >>> veryHighFHalfFlat.octave = 9
    >>> veryHighFHalfFlat.midi
    125
    ```

    ```python
    >>> notAsHighNote = pitch.Pitch()
    >>> notAsHighNote.ps = veryHighFHalfFlat.midi
    >>> notAsHighNote
    <music21.pitch.Pitch F9>
    ```

    Note that the conversion of improper midi values to proper
    midi values is done before assigning .ps:

    ```python
    >>> a = pitch.Pitch()
    >>> a.midi = -10
    >>> a.midi
    2
    >>> a.ps
    2.0
    >>> a.spellingIsInferred
    True
    ```

    More absurd octaves:

    ```python
    >>> p = pitch.Pitch('c~4')
    >>> p.octave = -1
    >>> p.ps
    0.5
    >>> p.midi
    1
    >>> p.octave = -2
    >>> p.ps
    -11.5
    >>> p.midi
    1
    ```

Pitch.name
:   Gets or sets the name (pitch name with accidental but
    without octave) of the Pitch.

    ```python
    >>> p = pitch.Pitch('D#5')
    >>> p.name
    'D#'
    ```

    ```python
    >>> p.name = 'C#'
    >>> p.name
    'C#'
    ```

    ```python
    >>> a = pitch.Pitch('G#')
    >>> a.name
    'G#'
    ```

    Does not simplify enharmonics

    ```python
    >>> a = pitch.Pitch('B---')
    >>> a.name
    'B---'
    ```

Pitch.nameWithOctave
:   Return or set the pitch name with an octave designation.
    If no octave as been set, no octave value is returned.

    ```python
    >>> gSharp = pitch.Pitch('G#4')
    >>> gSharp.nameWithOctave
    'G#4'
    ```

    ```python
    >>> dFlatFive = pitch.Pitch()
    >>> dFlatFive.step = 'D'
    >>> dFlatFive.accidental = pitch.Accidental('flat')
    >>> dFlatFive.octave = 5
    >>> dFlatFive.nameWithOctave
    'D-5'
    >>> dFlatFive.nameWithOctave = 'C#6'
    >>> dFlatFive.name
    'C#'
    >>> dFlatFive.octave
    6
    ```

    N.B. – it’s generally better to set the name and octave separately, especially
    since you may at some point encounter very low pitches such as “A octave -1”, which
    will be interpreted as “A-flat, octave 1”. Our crude setting algorithm also does
    not support octaves above 9.

    ```python
    >>> lowA = pitch.Pitch()
    >>> lowA.name = 'A'
    >>> lowA.octave = -1
    >>> lowA.nameWithOctave
    'A-1'
    >>> lowA.nameWithOctave = lowA.nameWithOctave
    >>> lowA.name
    'A-'
    >>> lowA.octave
    1
    ```

    Octave must be included in nameWithOctave or an exception is raised:

    ```python
    >>> a = pitch.Pitch()
    >>> a.nameWithOctave = 'C#9'
    >>> a.nameWithOctave = 'C#'
    Traceback (most recent call last):
    music21.pitch.PitchException: Cannot set a nameWithOctave with 'C#'
    ```

    Set octave to None explicitly instead.

Pitch.octave
:   Returns or sets the octave of the note.
    Setting the octave updates the pitchSpace attribute.

    ```python
    >>> a = pitch.Pitch('g')
    >>> a.octave is None
    True
    >>> a.implicitOctave
    4
    >>> a.ps  ## will use implicitOctave
    67.0
    >>> a.name
    'G'
    ```

    ```python
    >>> a.octave = 14
    >>> a.octave
    14
    >>> a.implicitOctave
    14
    >>> a.name
    'G'
    >>> a.ps
    187.0
    ```

Pitch.pitchClass
:   Returns or sets the integer value for the pitch, 0-11, where C=0,
    C#=1, D=2, etc. to B=11. Can be set using integers (0-11) or ‘A’ or ‘B’
    for 10 or 11.

    ```python
    >>> a = pitch.Pitch('a3')
    >>> a.pitchClass
    9
    >>> dis = pitch.Pitch('d3')
    >>> dis.pitchClass
    2
    >>> dis.accidental = pitch.Accidental('#')
    >>> dis.pitchClass
    3
    ```

    If a string “A” or “B” is given to pitchClass, it is
    still returned as an int.

    ```python
    >>> dis.pitchClass = 'A'
    >>> dis.pitchClass
    10
    >>> dis.name
    'B-'
    ```

    Extreme octaves will not affect pitchClass

    ```python
    >>> dis.octave = -10
    >>> dis.pitchClass
    10
    ```

    In the past, certain microtones and/or octaves were returning pc 12!
    This is now fixed.

    ```python
    >>> flattedC = pitch.Pitch('C4')
    >>> flattedC.microtone = -4
    >>> print(flattedC)
    C4(-4c)
    >>> flattedC.pitchClass
    0
    >>> print(flattedC.ps)
    59.96
    >>> flattedC.octave = -3
    >>> print(flattedC.ps)
    -24.04
    >>> flattedC.pitchClass
    0
    ```

    Note that the pitchClass of a microtonally altered pitch is the pitch class of
    the nearest pitch. Python 3 uses the “round-to-even” method so C~4 (C half sharp 4)
    is pitchClass 0, since 60.5 rounds to 60.0

    ```python
    >>> p = pitch.Pitch('C~4')
    >>> p.ps
    60.5
    >>> p.pitchClass
    0
    ```

    However, for backwards compatability, the MIDI number of a microtone
    is created by using “schoolyard” rounding which always rounds 0.5 upwards, which
    can cause some unusual behavior:

    ```python
    >>> p.midi
    61
    >>> pitch.Pitch(midi=p.midi).pitchClass
    1
    ```

    This means that pitchClass + microtone is NOT a good way to estimate the frequency
    of a pitch. For instance, if we take a pitch that is 90% of the way between pitchClass
    0 (C) and pitchClass 1 (C#/D-flat), this formula gives an inaccurate answer of 1.9, not
    0.9:

    ```python
    >>> p = pitch.Pitch('C4')
    >>> p.microtone = 90
    >>> p
    <music21.pitch.Pitch C4(+90c)>
    >>> p.pitchClass + (p.microtone.cents / 100.0)
    1.9
    ```

    More examples of setting the pitchClass.

    ```python
    >>> a = pitch.Pitch('a3')
    >>> a.pitchClass = 3
    >>> a
    <music21.pitch.Pitch E-3>
    >>> a.spellingIsInferred
    True
    >>> a.pitchClass = 'A'
    >>> a
    <music21.pitch.Pitch B-3>
    ```

    Changing pitchClass does not remove microtones.

    ```python
    >>> a.microtone = 20
    >>> a.pitchClass = 1
    >>> a
    <music21.pitch.Pitch C#3(+20c)>
    ```

Pitch.pitchClassString
:   Returns or sets a string representation of the pitch class,
    where integers greater than 10 are replaced by A and B,
    respectively. Can be used to set pitch class by a
    string representation as well (though this is also
    possible with [`pitchClass`](#music21.pitch.Pitch.pitchClass "music21.pitch.Pitch.pitchClass")).

    ```python
    >>> a = pitch.Pitch('a#3')
    >>> a.pitchClass
    10
    >>> a.pitchClassString
    'A'
    ```

    We can set the pitchClassString as well:

    ```python
    >>> a.pitchClassString = 'B'
    >>> a.pitchClass
    11
    ```

Pitch.ps
:   The ps property permits getting and setting
    a pitch space value, a floating point number
    representing pitch space, where 60.0 is C4, middle C,
    61.0 is C#4 or D-4, and floating point values are
    microtonal tunings (0.01 is equal to one cent), so
    a quarter-tone sharp above C5 is 72.5.

    Note that the choice of 60.0 for C4 makes it identical
    to the integer value of 60 for .midi, but .midi
    does not allow for microtones and is limited to 0-127
    while .ps allows for notes before midi 0 or above midi 127.

    ```python
    >>> a = pitch.Pitch('C4')
    >>> a.ps
    60.0
    ```

    Changing the ps value for a will change the step and octave:

    ```python
    >>> a.ps = 45
    >>> a
    <music21.pitch.Pitch A2>
    >>> a.ps
    45.0
    ```

    Notice that ps 61 represents both
    C# and D-flat. Thus, “spellingIsInferred”
    will be true after setting our pitch to 61:

    ```python
    >>> a.ps = 61
    >>> a
    <music21.pitch.Pitch C#4>
    >>> a.ps
    61.0
    >>> a.spellingIsInferred
    True
    ```

    Microtonal accidentals and pure Microtones are allowed, as are extreme ranges:

    ```python
    >>> b = pitch.Pitch('B9')
    >>> b.accidental = pitch.Accidental('half-flat')
    >>> b
    <music21.pitch.Pitch B`9>
    >>> b.ps
    130.5
    ```

    ```python
    >>> p = pitch.Pitch('c4')
    >>> p.microtone = 20
    >>> print(f'{p.ps:.1f}')
    60.2
    ```

    Octaveless pitches use their .implicitOctave attributes:

    ```python
    >>> d = pitch.Pitch('D#')
    >>> d.octave is None
    True
    >>> d.implicitOctave
    4
    >>> d.ps
    63.0
    ```

    ```python
    >>> d.octave = 5
    >>> d.ps
    75.0
    ```

    Setting with microtones

    ```python
    >>> p = pitch.Pitch()
    >>> p.ps = 61
    >>> p.ps
    61.0
    >>> p.spellingIsInferred
    True
    >>> p.ps = 61.5  # get a quarter tone
    >>> p
    <music21.pitch.Pitch C#~4>
    >>> p.ps = 61.7  # set a microtone
    >>> print(p)
    C#~4(+20c)
    >>> p.ps = 61.4  # set a microtone
    >>> print(p)
    C#~4(-10c)
    ```

    The property is called when self.step, self.octave
    or self.accidental are changed.

Pitch.step
:   The diatonic name of the note; i.e. does not give the
    accidental or octave.

    ```python
    >>> a = pitch.Pitch('B-3')
    >>> a.step
    'B'
    ```

    Upper-case or lower-case names can be given to .step – they
    will be converted to upper-case

    ```python
    >>> b = pitch.Pitch()
    >>> b.step = 'c'
    >>> b.step
    'C'
    ```

    Changing the .step does not change the .accidental or
    .octave:

    ```python
    >>> a = pitch.Pitch('F#5')
    >>> a.step = 'D'
    >>> a.nameWithOctave
    'D#5'
    ```

    Giving a value that includes an accidental raises a PitchException.
    Use .name instead to change that.

    ```python
    >>> b = pitch.Pitch('E4')
    >>> b.step = 'B-'
    Traceback (most recent call last):
    music21.pitch.PitchException: Cannot make a step out of 'B-'
    ```

    This is okay though:

    ```python
    >>> b.name = 'B-'
    ```

    Note that if spelling is inferred, setting the step does NOT
    give that enharmonic. Perhaps it should, but best to make people use
    .getLowerEnharmonic or .getHigherEnharmonic instead.

    ```python
    >>> b.ps = 60
    >>> b.nameWithOctave
    'C4'
    >>> b.spellingIsInferred
    True
    >>> b.step = 'B'
    >>> b.accidental is None  # maybe this should set to B#? But that could be screwy.
    True
    >>> b.spellingIsInferred
    False
    ```

[`Pitch`](#music21.pitch.Pitch "music21.pitch.Pitch") methods

Pitch.\_\_eq\_\_(*other: [object](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")*)[[source]](../_modules/music21/pitch.html#Pitch.__eq__)
:   Are two pitches equal?

    They must both sound the same and be spelled the same.
    Enharmonic equivalence is not equality, nor is impliedOctave
    or is a pitch without an accidental equal to a pitch with a
    natural accidental. (See :meth:`~music21.pitch.Pitch.isEnharmonic for
    a method that does not require spelling equivalence, and for an example
    of how to compare notes without accidentals to notes with natural
    accidentals.)

    ```python
    >>> c = pitch.Pitch('C2')
    >>> c.octave
    2
    >>> cs = pitch.Pitch('C#4')
    >>> cs.octave
    4
    >>> c == cs
    False
    >>> c != cs
    True
    ```

    ```python
    >>> seven = 7
    >>> c == seven
    False
    ```

    ```python
    >>> c != seven
    True
    ```

    ```python
    >>> df = pitch.Pitch('D-4')
    >>> cs == df
    False
    ```

    Implied octaves do not equal explicit octaves

    ```python
    >>> c4 = pitch.Pitch('C4')
    >>> cImplied = pitch.Pitch('C')
    >>> c4 == cImplied
    False
    >>> c4.ps == cImplied.ps
    True
    ```

    Note: currently spellingIsInferred and fundamental
    are not checked – this behavior may change in the future.

Pitch.convertMicrotonesToQuarterTones(*\**, *inPlace=False*)[[source]](../_modules/music21/pitch.html#Pitch.convertMicrotonesToQuarterTones)
:   Convert any Microtones available to quarter tones, if possible.

    ```python
    >>> p = pitch.Pitch('g3')
    >>> p.microtone = 78
    >>> str(p)
    'G3(+78c)'
    >>> p.convertMicrotonesToQuarterTones(inPlace=True)
    >>> str(p)
    'G#3(-22c)'
    ```

    ```python
    >>> p = pitch.Pitch('d#3')
    >>> p.microtone = 46
    >>> p
    <music21.pitch.Pitch D#3(+46c)>
    >>> p.convertMicrotonesToQuarterTones(inPlace=True)
    >>> p
    <music21.pitch.Pitch D#~3(-4c)>
    ```

    ```python
    >>> p = pitch.Pitch('f#2')
    >>> p.microtone = -38
    >>> p.convertMicrotonesToQuarterTones(inPlace=True)
    >>> str(p)
    'F~2(+12c)'
    ```

Pitch.convertQuarterTonesToMicrotones(*\**, *inPlace=False*)[[source]](../_modules/music21/pitch.html#Pitch.convertQuarterTonesToMicrotones)
:   Convert any quarter tone Accidentals to Microtones.

    tilde is the symbol for half-sharp, so G#~ is G three-quarters sharp.

    ```python
    >>> p = pitch.Pitch('G#~')
    >>> str(p), p.microtone
    ('G#~', <music21.pitch.Microtone (+0c)>)
    >>> p.convertQuarterTonesToMicrotones(inPlace=True)
    >>> p.ps
    68.5
    >>> str(p), p.microtone
    ('G#(+50c)', <music21.pitch.Microtone (+50c)>)
    ```

    ```python
    >>> p = pitch.Pitch('A')
    >>> p.accidental = pitch.Accidental('half-flat')  # back-tick
    >>> str(p), p.microtone
    ('A`', <music21.pitch.Microtone (+0c)>)
    >>> x = p.convertQuarterTonesToMicrotones(inPlace=False)
    >>> str(x), x.microtone
    ('A(-50c)', <music21.pitch.Microtone (-50c)>)
    >>> str(p), p.microtone
    ('A`', <music21.pitch.Microtone (+0c)>)
    ```

Pitch.getAllCommonEnharmonics(*alterLimit: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 2*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Self](https://docs.python.org/3/library/typing.html#typing.Self "(in Python v3.14)")][[source]](../_modules/music21/pitch.html#Pitch.getAllCommonEnharmonics)
:   Return all common unique enharmonics for a pitch,
    or those that do not involve more than two accidentals.

    ```python
    >>> p = pitch.Pitch('c#3')
    >>> p.getAllCommonEnharmonics()
    [<music21.pitch.Pitch D-3>, <music21.pitch.Pitch B##2>]
    ```

    “Higher” enharmonics are listed before “Lower”:

    ```python
    >>> p = pitch.Pitch('G4')
    >>> p.getAllCommonEnharmonics()
    [<music21.pitch.Pitch A--4>, <music21.pitch.Pitch F##4>]
    ```

    By setting alterLimit to a higher or lower number we
    can limit the maximum number of notes to return:

    ```python
    >>> p = pitch.Pitch('G-6')
    >>> p.getAllCommonEnharmonics(alterLimit=1)
    [<music21.pitch.Pitch F#6>]
    ```

    If you set alterLimit to 3 or 4, you’re stretching the name of
    the method; some of these are certainly not *common* enharmonics:

    ```python
    >>> p = pitch.Pitch('G-6')
    >>> enharmonics = p.getAllCommonEnharmonics(alterLimit=3)
    >>> [str(enh) for enh in enharmonics]
    ['A---6', 'F#6', 'E##6']
    ```

    Music21 does not support accidentals beyond quadruple sharp/flat, so
    alterLimit = 4 is the most you can use. (Thank goodness!)

Pitch.getCentShiftFromMidi() → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](../_modules/music21/pitch.html#Pitch.getCentShiftFromMidi)
:   Get cent deviation of this pitch from MIDI pitch.

    ```python
    >>> p = pitch.Pitch('c~4')
    >>> p.ps
    60.5
    >>> p.midi  # midi values automatically round up at 0.5
    61
    >>> p.getCentShiftFromMidi()
    -50
    >>> p.microtone = -25
    >>> p.ps
    60.25
    >>> p.midi
    60
    >>> p.getCentShiftFromMidi()
    25
    ```

    ```python
    >>> p = pitch.Pitch('c#4')
    >>> p.microtone = -25
    >>> p.ps
    60.75
    >>> p.midi
    61
    >>> p.getCentShiftFromMidi()
    -25
    ```

    ```python
    >>> p = pitch.Pitch('c#~4')
    >>> p.ps
    61.5
    >>> p.midi
    62
    >>> p.getCentShiftFromMidi()
    -50
    >>> p.microtone = -3
    >>> p.ps
    61.47
    >>> p.midi
    61
    >>> p.getCentShiftFromMidi()
    47
    >>> p.microtone = 3
    >>> p.ps
    61.53
    >>> p.midi
    62
    >>> p.accidental
    <music21.pitch.Accidental one-and-a-half-sharp>
    >>> p.getCentShiftFromMidi()
    -47
    ```

    ```python
    >>> p = pitch.Pitch('c`4')  # quarter tone flat
    >>> p.getCentShiftFromMidi()
    -50
    >>> p.microtone = 3
    >>> p.getCentShiftFromMidi()
    -47
    ```

    Absurd octaves that MIDI can’t handle will still give the right sounding pitch
    out of octave:

    ```python
    >>> p = pitch.Pitch('c~4')
    >>> p.octave = 10
    >>> p.ps
    132.5
    >>> p.midi
    121
    >>> p.getCentShiftFromMidi()
    -50
    >>> p.octave = -1
    >>> p.getCentShiftFromMidi()
    -50
    >>> p.octave = -2
    >>> p.getCentShiftFromMidi()
    -50
    ```

Pitch.getEnharmonic(*\**, *inPlace=False*) → [Self](https://docs.python.org/3/library/typing.html#typing.Self "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/pitch.html#Pitch.getEnharmonic)
:   Returns a new Pitch that is the(/an) enharmonic equivalent of this Pitch.
    Can be thought of as flipEnharmonic or something like that.

    N.B.: n1.name == getEnharmonic(getEnharmonic(n1)).name is not necessarily true.
    For instance:

    > getEnharmonic(E##) => F#
    > getEnharmonic(F#) => G-
    > getEnharmonic(A–) => G
    > getEnharmonic(G) => F##

    However, for all cases not involving double sharps or flats
    (and even many that do), getEnharmonic(getEnharmonic(n)) = n

    For the most ambiguous cases, it’s good to know that these are the enharmonics:

    > C <-> B#, D <-> C##, E <-> F-; F <-> E#, G <-> F##, A <-> B–, B <-> C-

    However, isEnharmonic() for A## and B certainly returns True.

    ```python
    >>> p = pitch.Pitch('d#')
    >>> print(p.getEnharmonic())
    E-
    >>> p = pitch.Pitch('e-8')
    >>> print(p.getEnharmonic())
    D#8
    ```

    Other tests:

    ```python
    >>> print(pitch.Pitch('c-3').getEnharmonic())
    B2
    >>> print(pitch.Pitch('e#2').getEnharmonic())
    F2
    >>> print(pitch.Pitch('f#2').getEnharmonic())
    G-2
    >>> print(pitch.Pitch('c##5').getEnharmonic())
    D5
    >>> print(pitch.Pitch('g3').getEnharmonic())
    F##3
    >>> print(pitch.Pitch('B7').getEnharmonic())
    C-8
    ```

    Octaveless Pitches remain octaveless:

    ```python
    >>> p = pitch.Pitch('a-')
    >>> p.getEnharmonic()
    <music21.pitch.Pitch G#>
    >>> p = pitch.Pitch('B#')
    >>> p.getEnharmonic()
    <music21.pitch.Pitch C>
    ```

    Works with half-sharps, but converts them to microtones:

    ```python
    >>> dHalfSharp = pitch.Pitch('D~')
    >>> print(dHalfSharp.getEnharmonic())
    E-(-50c)
    ```

Pitch.getHarmonic(*number: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [Pitch](#music21.pitch.Pitch "music21.pitch.Pitch")[[source]](../_modules/music21/pitch.html#Pitch.getHarmonic)
:   Return a Pitch object representing the harmonic found above this Pitch.

    ```python
    >>> p = pitch.Pitch('a4')
    >>> print(p.getHarmonic(2))
    A5
    >>> print(p.getHarmonic(3))
    E6(+2c)
    >>> print(p.getHarmonic(4))
    A6
    >>> print(p.getHarmonic(5))
    C#7(-14c)
    >>> print(p.getHarmonic(6))
    E7(+2c)
    >>> print(p.getHarmonic(7))
    F#~7(+19c)
    >>> print(p.getHarmonic(8))
    A7
    ```

    ```python
    >>> p2 = p.getHarmonic(2)
    >>> p2
    <music21.pitch.Pitch A5>
    >>> p2.fundamental
    <music21.pitch.Pitch A4>
    >>> p2.transpose('p5', inPlace=True)
    >>> p2
    <music21.pitch.Pitch E6>
    >>> p2.fundamental
    <music21.pitch.Pitch E5>
    ```

    Or we can iterate over a list of the next 8 odd harmonics:

    ```python
    >>> allHarmonics = ''
    >>> for i in [9, 11, 13, 15, 17, 19, 21, 23]:
    ...     allHarmonics += ' ' + str(p.getHarmonic(i))
    >>> print(allHarmonics)
    B7(+4c) D~8(+1c) F~8(-9c) G#8(-12c) B-8(+5c) C9(-2c) C#~9(+21c) E`9(-22c)
    ```

    Microtonally adjusted notes also generate harmonics:

    ```python
    >>> q = pitch.Pitch('C4')
    >>> q.microtone = 10
    >>> q.getHarmonic(2)
    <music21.pitch.Pitch C5(+10c)>
    >>> q.getHarmonic(3)
    <music21.pitch.Pitch G5(+12c)>
    ```

    The fundamental is stored with the harmonic.

    ```python
    >>> h7 = pitch.Pitch('A4').getHarmonic(7)
    >>> print(h7)
    F#~7(+19c)
    >>> h7.fundamental
    <music21.pitch.Pitch A4>
    >>> h7.harmonicString()
    '7thH/A4'
    >>> h7.harmonicString('A3')
    '14thH/A3'
    ```

    ```python
    >>> h2 = h7.getHarmonic(2)
    >>> h2
    <music21.pitch.Pitch F#~8(+19c)>
    >>> h2.fundamental
    <music21.pitch.Pitch F#~7(+19c)>
    >>> h2.fundamental.fundamental
    <music21.pitch.Pitch A4>
    >>> h2.transpose(-24, inPlace=True)
    >>> h2
    <music21.pitch.Pitch F#~6(+19c)>
    >>> h2.fundamental.fundamental
    <music21.pitch.Pitch A2>
    ```

Pitch.getHigherEnharmonic(*\**, *inPlace: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[False]*) → [Self](https://docs.python.org/3/library/typing.html#typing.Self "(in Python v3.14)")[[source]](../_modules/music21/pitch.html#Pitch.getHigherEnharmonic)

Pitch.getHigherEnharmonic(*\**, *inPlace: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[True]*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
:   Returns an enharmonic Pitch object that is a higher
    enharmonic. That is, the Pitch a diminished-second above
    the current Pitch.

    ```python
    >>> p1 = pitch.Pitch('C#3')
    >>> p2 = p1.getHigherEnharmonic()
    >>> print(p2)
    D-3
    ```

    We can also set it in place (in which case it returns None):

    ```python
    >>> p1 = pitch.Pitch('C#3')
    >>> p1.getHigherEnharmonic(inPlace=True)
    >>> print(p1)
    D-3
    ```

    The method even works for certain CRAZY enharmonics

    ```python
    >>> p3 = pitch.Pitch('D--3')
    >>> p4 = p3.getHigherEnharmonic()
    >>> print(p4)
    E----3
    ```

    But not for things that are just utterly insane:

    ```python
    >>> p4.getHigherEnharmonic()
    Traceback (most recent call last):
    music21.pitch.AccidentalException: -5 is not a supported accidental type
    ```

    Note that half accidentals (~ = half-sharp, ` = half-flat)
    get converted to microtones:

    ```python
    >>> pHalfSharp = pitch.Pitch('D~4')
    >>> p3QuartersFlat = pHalfSharp.getHigherEnharmonic()
    >>> print(p3QuartersFlat)
    E-4(-50c)
    ```

Pitch.getLowerEnharmonic(*\**, *inPlace: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[False]*) → [Self](https://docs.python.org/3/library/typing.html#typing.Self "(in Python v3.14)")[[source]](../_modules/music21/pitch.html#Pitch.getLowerEnharmonic)

Pitch.getLowerEnharmonic(*\**, *inPlace: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[True]*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
:   returns a Pitch enharmonic that is a diminished second
    below the current note

    If inPlace is set to true, changes the current Pitch and returns None.

    ```python
    >>> p1 = pitch.Pitch('E-')
    >>> p2 = p1.getLowerEnharmonic()
    >>> print(p2)
    D#
    ```

    The lower enharmonic can have a different octave than
    the original.

    ```python
    >>> p1 = pitch.Pitch('C-3')
    >>> p2 = p1.getLowerEnharmonic()
    >>> print(p2)
    B2
    ```

    ```python
    >>> p1 = pitch.Pitch('C#3')
    >>> p1.getLowerEnharmonic(inPlace=True)
    >>> print(p1)
    B##2
    ```

Pitch.getStringHarmonic(*chordIn*)[[source]](../_modules/music21/pitch.html#Pitch.getStringHarmonic)
:   Given a chord, determines whether the chord constitutes a string
    harmonic and then returns a new chord with the proper sounding pitch
    added.

    ```python
    >>> n1 = note.Note('d3')
    >>> n2 = note.Note('g3')
    >>> n2.notehead = 'diamond'
    >>> n2.noteheadFill = False
    >>> p1 = pitch.Pitch('d3')
    >>> harmChord = chord.Chord([n1, n2])
    >>> harmChord.quarterLength = 1
    >>> newChord = p1.getStringHarmonic(harmChord)
    >>> newChord.quarterLength = 1
    >>> pitchList = newChord.pitches
    >>> pitchList
    (<music21.pitch.Pitch D3>, <music21.pitch.Pitch G3>, <music21.pitch.Pitch D5>)
    ```

    otherwise returns False

Pitch.harmonicAndFundamentalFromPitch(*target: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Pitch](#music21.pitch.Pitch "music21.pitch.Pitch")*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [Pitch](#music21.pitch.Pitch "music21.pitch.Pitch")][[source]](../_modules/music21/pitch.html#Pitch.harmonicAndFundamentalFromPitch)
:   Given a Pitch that is a plausible target for a fundamental,
    return the harmonic number and a potentially shifted fundamental
    that describes this Pitch.

    ```python
    >>> g4 = pitch.Pitch('g4')
    >>> g4.harmonicAndFundamentalFromPitch('c3')
    (3, <music21.pitch.Pitch C3(-2c)>)
    ```

Pitch.harmonicAndFundamentalStringFromPitch(*fundamental: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Pitch](#music21.pitch.Pitch "music21.pitch.Pitch")*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](../_modules/music21/pitch.html#Pitch.harmonicAndFundamentalStringFromPitch)
:   Given a Pitch that is a plausible target for a fundamental,
    find the harmonic number and a potentially shifted fundamental
    that describes this Pitch. Return a string representation.

    ```python
    >>> pitch.Pitch('g4').harmonicAndFundamentalStringFromPitch('c3')
    '3rdH/C3(-2c)'
    ```

    ```python
    >>> pitch.Pitch('c4').harmonicAndFundamentalStringFromPitch('c3')
    '2ndH/C3'
    ```

    ```python
    >>> p = pitch.Pitch('c4')
    >>> p.microtone = 20  # raise 20
    >>> p.harmonicAndFundamentalStringFromPitch('c3')
    '2ndH/C3(+20c)'
    ```

    ```python
    >>> p.microtone = -20  # lower 20
    >>> p.harmonicAndFundamentalStringFromPitch('c3')
    '2ndH/C3(-20c)'
    ```

    ```python
    >>> p = pitch.Pitch('c4')
    >>> f = pitch.Pitch('c3')
    >>> f.microtone = -20
    >>> p.harmonicAndFundamentalStringFromPitch(f)
    '2ndH/C3'
    >>> f.microtone = +20
    >>> p.harmonicAndFundamentalStringFromPitch(f)
    '2ndH/C3'
    ```

    ```python
    >>> p = pitch.Pitch('A4')
    >>> p.microtone = 69
    >>> p.harmonicAndFundamentalStringFromPitch('c2')
    '7thH/C2'
    ```

    ```python
    >>> p = pitch.Pitch('A4')
    >>> p.harmonicAndFundamentalStringFromPitch('c2')
    '7thH/C2(-69c)'
    ```

Pitch.harmonicFromFundamental(*fundamental: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Pitch](#music21.pitch.Pitch "music21.pitch.Pitch")*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")][[source]](../_modules/music21/pitch.html#Pitch.harmonicFromFundamental)
:   Given another Pitch as a fundamental, find the harmonic
    of that pitch that is equal to this Pitch.

    Returns a tuple of harmonic number and the number of cents that
    the first Pitch object would have to be shifted to be the exact
    harmonic of this fundamental.

    Microtones applied to the fundamental are irrelevant,
    as the fundamental may be microtonally shifted to find a match to this Pitch.

    Example: G4 is the third harmonic of C3, albeit 2 cents flatter than
    the true 3rd harmonic.

    ```python
    >>> p = pitch.Pitch('g4')
    >>> f = pitch.Pitch('c3')
    >>> p.harmonicFromFundamental(f)
    (3, 2.0)
    >>> p.microtone = p.harmonicFromFundamental(f)[1]  # adjust microtone
    >>> int(f.getHarmonic(3).frequency) == int(p.frequency)
    True
    ```

    The shift from B-5 to the 7th harmonic of C3 is more substantial
    and likely to be noticed by the audience. To make p the 7th harmonic
    it’d have to be lowered by 31 cents. Note that the
    second argument is a float, but because the default rounding of
    music21 is to the nearest cent, the 0.0 is not a significant digit.
    I.e. it might be more like 31.3 cents.

    ```python
    >>> p = pitch.Pitch('B-5')
    >>> f = pitch.Pitch('C3')
    >>> p.harmonicFromFundamental(f)
    (7, -31.0)
    ```

Pitch.harmonicString(*fundamental: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Pitch](#music21.pitch.Pitch "music21.pitch.Pitch") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](../_modules/music21/pitch.html#Pitch.harmonicString)
:   Return a string representation of a harmonic equivalence.

    N.B. this has nothing to do with what string a string player
    would use to play the harmonic on. (Perhaps should be
    renamed).

    ```python
    >>> pitch.Pitch('g4').harmonicString('c3')
    '3rdH(-2c)/C3'
    ```

    ```python
    >>> pitch.Pitch('c4').harmonicString('c3')
    '2ndH/C3'
    ```

    ```python
    >>> p = pitch.Pitch('c4')
    >>> p.microtone = 20  # raise 20
    >>> p.harmonicString('c3')
    '2ndH(+20c)/C3'
    ```

    ```python
    >>> p.microtone = -20  # lower 20
    >>> p.harmonicString('c3')
    '2ndH(-20c)/C3'
    ```

    ```python
    >>> p = pitch.Pitch('c4')
    >>> f = pitch.Pitch('c3')
    >>> f.microtone = -20
    >>> p.harmonicString(f)
    '2ndH(+20c)/C3(-20c)'
    >>> f.microtone = +20
    >>> p.harmonicString(f)
    '2ndH(-20c)/C3(+20c)'
    ```

    ```python
    >>> p = pitch.Pitch('A4')
    >>> p.microtone = 69
    >>> p.harmonicString('c2')
    '7thH/C2'
    ```

    ```python
    >>> p = pitch.Pitch('A4')
    >>> p.harmonicString('c2')
    '7thH(-69c)/C2'
    ```

Pitch.informClient()[[source]](../_modules/music21/pitch.html#Pitch.informClient)
:   if this pitch is attached to a note, then let it know that it has changed.

Pitch.isEnharmonic(*other: [Pitch](#music21.pitch.Pitch "music21.pitch.Pitch")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/pitch.html#Pitch.isEnharmonic)
:   Return True if another Pitch is an enharmonic equivalent of this Pitch.

    ```python
    >>> p1 = pitch.Pitch('C#3')
    >>> p2 = pitch.Pitch('D-3')
    >>> p3 = pitch.Pitch('D#3')
    >>> p1.isEnharmonic(p2)
    True
    >>> p2.isEnharmonic(p1)
    True
    >>> p3.isEnharmonic(p1)
    False
    ```

    Pitches are enharmonics of themselves:

    ```python
    >>> pC = pitch.Pitch('C4')
    >>> pC.isEnharmonic(pC)
    True
    ```

    Notes that sound in different octaves are not enharmonics:

    ```python
    >>> pitch.Pitch('C#4').isEnharmonic( pitch.Pitch('D-5') )
    False
    ```

    However, different octave numbers can be the same enharmonic,
    because octave number is relative to the step (natural form) of the pitch.

    ```python
    >>> pitch.Pitch('C4').isEnharmonic( pitch.Pitch('B#3') )
    True
    >>> pitch.Pitch('C4').isEnharmonic( pitch.Pitch('B#4') )
    False
    ```

    If either pitch is octaveless, then a pitch in any octave will match:

    ```python
    >>> pitch.Pitch('C#').isEnharmonic( pitch.Pitch('D-9') )
    True
    >>> pitch.Pitch('C#4').isEnharmonic( pitch.Pitch('D-') )
    True
    ```

    Quarter tone enharmonics work as well:

    ```python
    >>> pC.accidental = pitch.Accidental('one-and-a-half-sharp')
    >>> pC
    <music21.pitch.Pitch C#~4>
    >>> pD = pitch.Pitch('D4')
    >>> pD.accidental = pitch.Accidental('half-flat')
    >>> pD
    <music21.pitch.Pitch D`4>
    >>> pC.isEnharmonic(pD)
    True
    ```

    Microtonally altered pitches do not return True unless the microtones are the same:

    ```python
    >>> pSharp = pitch.Pitch('C#4')
    >>> pSharp.microtone = 20
    >>> pFlat = pitch.Pitch('D-4')
    >>> pSharp.isEnharmonic(pFlat)
    False
    ```

    ```python
    >>> pFlat.microtone = 20
    >>> pSharp.isEnharmonic(pFlat)
    True
    ```

    Extreme enharmonics also work:

    ```python
    >>> p4 = pitch.Pitch('B##3')
    >>> p5 = pitch.Pitch('E---4')
    >>> p4.isEnharmonic(p5)
    True
    ```

    If either pitch has no octave then the comparison is done without
    regard to octave:

    ```python
    >>> pSharp4 = pitch.Pitch('C#4')
    >>> pFlatNoOctave = pitch.Pitch('D-')
    >>> pSharp4.isEnharmonic(pFlatNoOctave)
    True
    >>> pFlatNoOctave.isEnharmonic(pSharp4)
    True
    ```

    isEnharmonic can be combined with a test to see if two pitches have the
    same step to ensure that they both sound the same and are written
    the same, without regard to the presence or absence of an accidental
    (this is used in :meth:~music21.stream.base.Stream.stripTies):

    ```python
    >>> pD4 = pitch.Pitch('D4')
    >>> pDNatural4 = pitch.Pitch('D4', accidental=pitch.Accidental('natural'))
    >>> pD4 == pDNatural4
    False
    >>> pD4.isEnharmonic(pDNatural4) and pD4.step == pDNatural4.step
    True
    >>> pEbb4 = pitch.Pitch('E--4')
    >>> pD4.isEnharmonic(pEbb4) and pD4.step == pEbb4.step
    False
    ```

Pitch.isTwelveTone() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/pitch.html#Pitch.isTwelveTone)
:   Return True if this Pitch is
    one of the twelve tones available on a piano
    keyboard. Returns False if it instead
    has a non-zero microtonal adjustment or
    has a quarter tone accidental.

    ```python
    >>> p = pitch.Pitch('g4')
    >>> p.isTwelveTone()
    True
    >>> p.microtone = -20
    >>> p.isTwelveTone()
    False
    ```

    ```python
    >>> p2 = pitch.Pitch('g~4')
    >>> p2.isTwelveTone()
    False
    ```

Pitch.simplifyEnharmonic(*\**, *inPlace=False*, *mostCommon=False*) → [Self](https://docs.python.org/3/library/typing.html#typing.Self "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/pitch.html#Pitch.simplifyEnharmonic)
:   Returns a new Pitch (or sets the current one if inPlace is True)
    that is either the same as the current pitch or has fewer
    sharps or flats if possible. For instance, E# returns F,
    while A# remains A# (i.e., does not take into account that B- is
    more common than A#). Useful to call if you ever have an
    algorithm that might take your piece far into the realm of
    double or triple flats or sharps.

    If mostCommon is set to True, then the most commonly used
    enharmonic spelling is chosen (that is, the one that appears
    first in key signatures as you move away from C on the circle
    of fifths). Thus, G-flat becomes F#, A# becomes B-flat,
    D# becomes E-flat, D-flat becomes C#, G# and A-flat are left
    alone.

    ```python
    >>> p1 = pitch.Pitch('B#5')
    >>> p1.simplifyEnharmonic().nameWithOctave
    'C6'
    ```

    ```python
    >>> p2 = pitch.Pitch('A#2')
    >>> p2.simplifyEnharmonic(inPlace=True)
    >>> p2
    <music21.pitch.Pitch A#2>
    ```

    ```python
    >>> p3 = pitch.Pitch('E--3')
    >>> p4 = p3.transpose(interval.Interval('-A5'))
    >>> p4.simplifyEnharmonic()
    <music21.pitch.Pitch F#2>
    ```

    Setting mostCommon = True simplifies enharmonics
    even further.

    ```python
    >>> pList = [pitch.Pitch('A#4'), pitch.Pitch('B-4'),
    ...          pitch.Pitch('G-4'), pitch.Pitch('F#4')]
    >>> [str(p.simplifyEnharmonic(mostCommon=True)) for p in pList]
    ['B-4', 'B-4', 'F#4', 'F#4']
    ```

    Note that pitches with implicit octaves retain their implicit octaves.
    This might change the pitch space for B#s and C-s.

    ```python
    >>> pList = [pitch.Pitch('B'), pitch.Pitch('C#'), pitch.Pitch('G'), pitch.Pitch('A--')]
    >>> [str(p.simplifyEnharmonic()) for p in pList]
    ['B', 'C#', 'G', 'G']
    ```

    ```python
    >>> pList = [pitch.Pitch('C-'), pitch.Pitch('B#')]
    >>> [p.ps for p in pList]
    [59.0, 72.0]
    >>> [p.simplifyEnharmonic().ps for p in pList]
    [71.0, 60.0]
    ```

Pitch.transpose(*value: [IntervalBase](moduleInterval.html#music21.interval.IntervalBase "music21.interval.IntervalBase") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *\**, *inPlace: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[True]*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/pitch.html#Pitch.transpose)

Pitch.transpose(*value: [IntervalBase](moduleInterval.html#music21.interval.IntervalBase "music21.interval.IntervalBase") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *\**, *inPlace: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[False] = False*) → [Self](https://docs.python.org/3/library/typing.html#typing.Self "(in Python v3.14)")
:   Transpose the pitch by the user-provided value. If the value is an
    integer, the transposition is treated in half steps. If the value is a
    string, any Interval string specification can be provided.
    Alternatively, a [`music21.interval.Interval`](moduleInterval.html#music21.interval.Interval "music21.interval.Interval") object can be
    supplied.

    ```python
    >>> aPitch = pitch.Pitch('g4')
    >>> bPitch = aPitch.transpose('m3')
    >>> bPitch
    <music21.pitch.Pitch B-4>
    >>> cPitch = bPitch.transpose(interval.GenericInterval(2))
    >>> cPitch
    <music21.pitch.Pitch C-5>
    ```

    An interval object can also be a certain number of semitones,
    in which case, the spelling of the resulting note (sharp or flat, etc.)
    is up to the system to choose.

    ```python
    >>> aInterval = interval.Interval(-6)
    >>> bPitch = aPitch.transpose(aInterval)
    >>> bPitch
    <music21.pitch.Pitch C#4>
    ```

    Transpose fFlat down 5 semitones – sort of like a Perfect 4th, but
    should be respelled:

    ```python
    >>> fFlat = pitch.Pitch('F-4')
    >>> newPitch = fFlat.transpose(-5)
    >>> newPitch
    <music21.pitch.Pitch B3>
    ```

    ```python
    >>> aPitch
    <music21.pitch.Pitch G4>
    ```

    ```python
    >>> aPitch.transpose(aInterval, inPlace=True)
    >>> aPitch
    <music21.pitch.Pitch C#4>
    ```

    Implicit octaves remain implicit:

    ```python
    >>> anyGSharp = pitch.Pitch('G#')
    >>> print(anyGSharp.transpose('P8'))
    G#
    >>> print(anyGSharp.transpose('P5'))
    D#
    ```

    If the accidental of a pitch is chosen by music21, not
    given by the user, then after transposing, music21 will
    simplify the spelling again:

    ```python
    >>> pc6 = pitch.Pitch(6)
    >>> pc6
    <music21.pitch.Pitch F#>
    >>> pc6.spellingIsInferred
    True
    >>> pc6.transpose('-m2')
    <music21.pitch.Pitch F>
    ```

Pitch.transposeAboveTarget(*target*, *\**, *minimize=False*, *inPlace=False*) → [Self](https://docs.python.org/3/library/typing.html#typing.Self "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/pitch.html#Pitch.transposeAboveTarget)
:   Given a source Pitch, shift it up octaves until it is above the target.

    If minimize is True, a pitch above the target will move down to the
    nearest octave.

    ```python
    >>> pitch.Pitch('d2').transposeAboveTarget(pitch.Pitch('e4'))
    <music21.pitch.Pitch D5>
    ```

    To change the pitch itself, set inPlace to True:

    ```python
    >>> p = pitch.Pitch('d2')
    >>> p.transposeAboveTarget(pitch.Pitch('e4'), inPlace=True)
    >>> p
    <music21.pitch.Pitch D5>
    ```

    If already above the target, make no change:

    ```python
    >>> pitch.Pitch('d7').transposeAboveTarget(pitch.Pitch('e2'))
    <music21.pitch.Pitch D7>
    ```

    Accept the same pitch:

    ```python
    >>> pitch.Pitch('d2').transposeAboveTarget(pitch.Pitch('d8'))
    <music21.pitch.Pitch D8>
    ```

    If minimize is True, we go the closest position:

    ```python
    >>> pitch.Pitch('d#8').transposeAboveTarget(pitch.Pitch('d2'), minimize=True)
    <music21.pitch.Pitch D#2>
    ```

    ```python
    >>> pitch.Pitch('d7').transposeAboveTarget(pitch.Pitch('e2'), minimize=True)
    <music21.pitch.Pitch D3>
    ```

    ```python
    >>> pitch.Pitch('d0').transposeAboveTarget(pitch.Pitch('e2'), minimize=True)
    <music21.pitch.Pitch D3>
    ```

    If the original pitch is octaveless, raises a PitchException:

    ```python
    >>> pitch.Pitch('d').transposeAboveTarget(pitch.Pitch('e2'), minimize=True)
    Traceback (most recent call last):
    music21.pitch.PitchException: Cannot call transposeAboveTarget with an octaveless Pitch.
    ```

    If the target pitch is octaveless, assumes it has the default of octave 4.
    (The reason for this asymmetry is that the target pitch is never altered
    while the original pitch (or its copy) is).

    ```python
    >>> pitch.Pitch('d4').transposeAboveTarget(pitch.Pitch('e'), minimize=True)
    <music21.pitch.Pitch D5>
    ```

    * Changed in v3: default for inPlace=False.

Pitch.transposeBelowTarget(*target*, *\**, *minimize=False*, *inPlace=False*) → [Self](https://docs.python.org/3/library/typing.html#typing.Self "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/pitch.html#Pitch.transposeBelowTarget)
:   Given a source Pitch, shift it down some number of octaves until it is below the
    target.

    If minimize is True, a pitch below the target will move up to the
    nearest octave.

    ```python
    >>> higherG = pitch.Pitch('G5')
    >>> lowerG = higherG.transposeBelowTarget(pitch.Pitch('C#4'))
    >>> lowerG
    <music21.pitch.Pitch G3>
    >>> higherG
    <music21.pitch.Pitch G5>
    ```

    To change the pitch itself, set inPlace to True:

    ```python
    >>> p = pitch.Pitch('G5')
    >>> p.transposeBelowTarget(pitch.Pitch('C#4'), inPlace=True)
    >>> p
    <music21.pitch.Pitch G3>
    ```

    If already below the target, make no change:

    ```python
    >>> pitch.Pitch('G#3').transposeBelowTarget(pitch.Pitch('C#6'))
    <music21.pitch.Pitch G#3>
    ```

    Below target includes being the same as the target

    ```python
    >>> pitch.Pitch('g#8').transposeBelowTarget(pitch.Pitch('g#1'))
    <music21.pitch.Pitch G#1>
    ```

    This does nothing because it is already low enough:

    ```python
    >>> pitch.Pitch('g#2').transposeBelowTarget(pitch.Pitch('f#8'))
    <music21.pitch.Pitch G#2>
    ```

    But with minimize=True, it will actually RAISE the pitch so that it is the closest
    pitch to the target

    ```python
    >>> target = pitch.Pitch('f#8')
    >>> pitch.Pitch('g#2').transposeBelowTarget(target, minimize=True)
    <music21.pitch.Pitch G#7>
    ```

    ```python
    >>> pitch.Pitch('f#2').transposeBelowTarget(target, minimize=True)
    <music21.pitch.Pitch F#8>
    ```

    If the original pitch is octaveless, raises a PitchException:

    ```python
    >>> pitch.Pitch('d').transposeBelowTarget(pitch.Pitch('e2'), minimize=True)
    Traceback (most recent call last):
    music21.pitch.PitchException: Cannot call transposeBelowTarget with an octaveless Pitch.
    ```

    If the target pitch is octaveless, assumes it has the default of octave 4.
    (The reason for this asymmetry is that the target pitch is never altered
    while the original pitch (or its copy) is).

    ```python
    >>> pitch.Pitch('f4').transposeBelowTarget(pitch.Pitch('e'), minimize=True)
    <music21.pitch.Pitch F3>
    ```

    * Changed in v3: default for inPlace=False.

Pitch.updateAccidentalDisplay(*\**, *pitchPast: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Pitch](#music21.pitch.Pitch "music21.pitch.Pitch")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *pitchPastMeasure: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Pitch](#music21.pitch.Pitch "music21.pitch.Pitch")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *otherSimultaneousPitches: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Pitch](#music21.pitch.Pitch "music21.pitch.Pitch")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *alteredPitches: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Pitch](#music21.pitch.Pitch "music21.pitch.Pitch")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *cautionaryPitchClass: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *cautionaryAll: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *overrideStatus: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *cautionaryNotImmediateRepeat: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *lastNoteWasTied: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*)[[source]](../_modules/music21/pitch.html#Pitch.updateAccidentalDisplay)
:   Given an ordered list of Pitch objects in pitchPast, determine if
    this pitch’s Accidental object needs to be created or updated with a
    natural or other cautionary accidental.

    Changes to this Pitch object’s Accidental object are made in-place.

    pitchPast is a list of pitches preceding this pitch in the same measure.
    If None, a new list will be made.

    pitchPastMeasure is a list of pitches preceding this pitch but in a
    previous measure. If None, a new list will be made.

    otherSimultaneousPitches is a list of other pitches in this simultaneity, for use
    when cautionaryPitchClass is True.

    The alteredPitches list supplies pitches from a [`KeySignature`](moduleKey.html#music21.key.KeySignature "music21.key.KeySignature")
    object using the [`alteredPitches`](moduleKey.html#music21.key.KeySignature.alteredPitches "music21.key.KeySignature.alteredPitches") property.
    If None, a new list will be made.

    If cautionaryPitchClass is True, comparisons to past accidentals are
    made regardless of register. That is, if a past sharp is found two
    octaves above a present natural, a natural sign is still displayed.
    Note that this has nothing to do with whether a sharp (not in the key
    signature) is found in a different octave from the same note in a
    different octave. The sharp must always be displayed. Notes
    with displayType = ‘if-absolutely-necessary’ will ignore the True
    setting.

    If overrideStatus is True, this method will ignore any current
    displayStatus setting found on the Accidental. By default, this does
    not happen. If displayStatus is set to None, the Accidental’s
    displayStatus is set.

    If cautionaryNotImmediateRepeat is True, cautionary accidentals will
    be displayed for an altered pitch even if that pitch had already been
    displayed as altered (unless it’s an immediate repetition). Notes
    with displayType = ‘if-absolutely-necessary’ will ignore the True
    setting.

    If lastNoteWasTied is True then this note will be treated as
    immediately following a tie.

    ```python
    >>> a = pitch.Pitch('a')
    >>> past = [pitch.Pitch('a#'), pitch.Pitch('c#'), pitch.Pitch('c')]
    >>> a.updateAccidentalDisplay(pitchPast=past, cautionaryAll=True)
    >>> a.accidental, a.accidental.displayStatus
    (<music21.pitch.Accidental natural>, True)
    ```

    ```python
    >>> b = pitch.Pitch('a')
    >>> past = [pitch.Pitch('a#'), pitch.Pitch('c#'), pitch.Pitch('c')]
    >>> b.updateAccidentalDisplay(pitchPast=past)  # should add a natural
    >>> b.accidental, b.accidental.displayStatus
    (<music21.pitch.Accidental natural>, True)
    ```

    In this example, the method will not add a natural because the match is
    pitchSpace and our octave is different.

    ```python
    >>> a4 = pitch.Pitch('a4')
    >>> past = [pitch.Pitch('a#3'), pitch.Pitch('c#'), pitch.Pitch('c')]
    >>> a4.updateAccidentalDisplay(pitchPast=past, cautionaryPitchClass=False)
    >>> a4.accidental is None
    True
    ```

    v8 – made keyword-only and added otherSimultaneousPitches.

[`Pitch`](#music21.pitch.Pitch "music21.pitch.Pitch") instance variables

Pitch.spellingIsInferred
:   Returns True or False about whether enharmonic spelling
    Has been inferred on pitch creation or whether it has
    been specified directly.

    MIDI 61 is C# or D- equally.

    ```python
    >>> p = pitch.Pitch('C4')
    >>> p.spellingIsInferred
    False
    >>> p.ps = 61
    >>> p.spellingIsInferred
    True
    >>> p.name
    'C#'
    >>> p.name = 'C#'
    >>> p.spellingIsInferred
    False
    ```

    This makes a difference in transposing. For instance:

    ```python
    >>> pInferred = pitch.Pitch(61)
    >>> pNotInferred = pitch.Pitch('C#4')
    >>> pInferred.nameWithOctave, pNotInferred.nameWithOctave
    ('C#4', 'C#4')
    >>> pInferred.spellingIsInferred, pNotInferred.spellingIsInferred
    (True, False)
    ```

    ```python
    >>> inferredTransposed = pInferred.transpose('A1')
    >>> inferredTransposed.nameWithOctave
    'D4'
    >>> notInferredTransposed = pNotInferred.transpose('A1')
    >>> notInferredTransposed.nameWithOctave
    'C##4'
    ```

    An operation like diatonic transposition should retain the spelling is inferred
    for the resulting object

    ```python
    >>> inferredTransposed.spellingIsInferred, notInferredTransposed.spellingIsInferred
    (True, False)
    ```

    But Chromatic transposition can change an object to inferred spelling:

    ```python
    >>> p3 = notInferredTransposed.transpose(1)  # C## -> E- not to C###
    >>> p3.nameWithOctave
    'E-4'
    >>> p3.spellingIsInferred
    True
    ```

## Accidental

class music21.pitch.Accidental(*specifier: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") = 'natural'*)[[source]](../_modules/music21/pitch.html#Accidental)
:   Accidental class, representing the symbolic and numerical representation of
    pitch deviation from a pitch name (e.g., G, B).

    Two accidentals are considered equal if their names are equal.

    Accidentals have three defining attributes: a name, a modifier, and an
    alter. For microtonal specifications, the name and modifier are the same
    except in the case of half-sharp, half-flat, one-and-a-half-flat, and
    one-and-a-half-sharp.

    Accidentals up to quadruple-sharp and quadruple-flat are allowed.

    Natural-sharp etc. (for canceling a previous flat) are not yet supported officially.

    ```python
    >>> a = pitch.Accidental('sharp')
    >>> a.name, a.alter, a.modifier
    ('sharp', 1.0, '#')
    >>> a.style.color = 'red'
    ```

    ```python
    >>> import copy
    >>> b = copy.deepcopy(a)
    >>> b.style.color
    'red'
    ```

[`Accidental`](#music21.pitch.Accidental "music21.pitch.Accidental") bases

* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")
* [`StyleMixin`](moduleStyle.html#music21.style.StyleMixin "music21.style.StyleMixin")
* [`SlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.SlottedObjectMixin "music21.common.objects.SlottedObjectMixin")

[`Accidental`](#music21.pitch.Accidental "music21.pitch.Accidental") read-only properties

Accidental.fullName
:   Return the most complete representation of this Accidental.

    ```python
    >>> a = pitch.Accidental('double-flat')
    >>> a.fullName
    'double-flat'
    ```

    Note that non-standard microtone names are converted to standard ones:

    ```python
    >>> a = pitch.Accidental('quarter-flat')
    >>> a.fullName
    'half-flat'
    ```

    For now this is the same as .name.

Accidental.unicode
:   Return a unicode representation of this accidental
    or the best unicode representation if that is not possible.

    ```python
    >>> flat = pitch.Accidental('flat')
    >>> flat.unicode
    '♭'
    ```

    Compare:

    ```python
    >>> sharp = pitch.Accidental('sharp')
    >>> sharp.modifier
    '#'
    >>> sharp.unicode
    '♯'
    ```

    Some accidentals, such as double sharps, produce code points outside
    the 2-byte set (so called “astral plane” unicode) and thus cannot be
    used in every circumnstance.

    ```python
    >>> sharp = pitch.Accidental('quadruple-flat')
    >>> sharp.unicode
    '𝄫𝄫'
    ```

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

Read-only properties inherited from [`StyleMixin`](moduleStyle.html#music21.style.StyleMixin "music21.style.StyleMixin"):

|  |  |  |
| --- | --- | --- |
| * [`hasEditorialInformation`](moduleStyle.html#music21.style.StyleMixin.hasEditorialInformation "music21.style.StyleMixin.hasEditorialInformation") | * [`hasStyleInformation`](moduleStyle.html#music21.style.StyleMixin.hasStyleInformation "music21.style.StyleMixin.hasStyleInformation") |  |

[`Accidental`](#music21.pitch.Accidental "music21.pitch.Accidental") read/write properties

Accidental.alter
:   Get or set the alter of the Accidental,
    or the semitone shift caused by the Accidental where 1.0
    is a shift up of one semitone, and -1.0 is the shift down of
    one semitone.

    ```python
    >>> sharp = pitch.Accidental('sharp')
    >>> sharp.alter
    1.0
    ```

    ```python
    >>> sharp.alter = -1
    ```

    After changing alter to a known other value, name changes:

    ```python
    >>> sharp.name
    'flat'
    ```

    But changing it to an unusual value does not change the name:

    ```python
    >>> notSoFlat = pitch.Accidental('flat')
    >>> notSoFlat.alter = -0.9
    >>> notSoFlat.name
    'flat'
    ```

    * Changed in v5: changing the alter here changes other values, conditionally

Accidental.displayStatus
:   Determines if this Accidental is to be displayed;
    can be None (for not set), True, or False. In general do not
    set this, set .displayType instead. Music21 will change displayStatus
    at any time without warning.

    While .displayType gives general rules about when this accidental
    should be displayed or not, displayStatus determines whether after
    applying those rules this accidental will be displayed.

    In general, a displayStatus of None means that no high-level
    processing of accidentals has happened.

    Can be set to True or False (or None) directly for contexts where
    the next program down the line cannot evaluate displayType. See
    stream.makeAccidentals() for more information.

    Example:

    ```python
    >>> n0 = note.Note('C#4')
    >>> n1 = note.Note('C#4')
    >>> print(n0.pitch.accidental.displayStatus)
    None
    >>> print(n1.pitch.accidental.displayStatus)
    None
    >>> s = stream.Stream()
    >>> s.append([n0, n1])
    >>> s.makeAccidentals(inPlace=True)
    >>> n0.pitch.accidental.displayStatus
    True
    >>> n1.pitch.accidental.displayStatus
    False
    ```

    ```python
    >>> n1.pitch.accidental.displayStatus = 2
    Traceback (most recent call last):
    music21.pitch.AccidentalException: Supplied display status is not supported: 2
    ```

Accidental.displayType
:   Returns or sets the display type of the accidental

    “normal” (default) displays it if it is the first in measure,
    or is needed to contradict a previous accidental, etc.

    other valid terms:

    * “always”
    * “never”
    * “unless-repeated” (show always unless
      the immediately preceding note is the same)
    * “even-tied” (stronger than always: shows even
      if it is tied to the previous note)
    * “if-absolutely-necessary” (display only if it is absolutely necessary,
      like an F-natural after an F-sharp in the same measure, but not an
      F-natural following an F-sharp directly across a barline. Nor an
      F-natural in a different octave immediately following an F-sharp).
      This is not yet implemented.

    ```python
    >>> a = pitch.Accidental('flat')
    >>> a.displayType = 'unless-repeated'
    >>> a.displayType
    'unless-repeated'
    >>> a.displayType = 'underwater'
    Traceback (most recent call last):
    music21.pitch.AccidentalException: Supplied display type is not supported: 'underwater'
    ```

Accidental.modifier
:   Get or set the alter of the modifier, or the string symbol
    used to modify the pitch name, such as “#” or
    “-” for sharp and flat, respectively. For a representation
    likely to be read by non-music21 users, see .unicode.

    ```python
    >>> f = pitch.Accidental('flat')
    >>> f.modifier
    '-'
    >>> f.modifier = '#'
    >>> f.name
    'sharp'
    ```

    However, an unknown modifier does not change anything but is preserved:

    ```python
    >>> f.modifier = '&'
    >>> f.modifier
    '&'
    >>> f.name
    'sharp'
    ```

    * Changed in v5: changing the modifier here changes
      other values, conditionally

Accidental.name
:   Get or set the name of the Accidental, like ‘sharp’ or ‘double-flat’

    If the name is set to a standard name then it changes alter and modifier.

    If set to a non-standard name, then it does not change them:

    ```python
    >>> a = pitch.Accidental()
    >>> a.name = 'flat'
    >>> a.alter
    -1.0
    >>> a.modifier
    '-'
    >>> a.name = 'flat-flat-up'
    >>> a.alter
    -1.0
    ```

    * Changed in v5: changing the name here changes other values, conditionally

Read/write properties inherited from [`StyleMixin`](moduleStyle.html#music21.style.StyleMixin "music21.style.StyleMixin"):

|  |  |  |
| --- | --- | --- |
| * [`editorial`](moduleStyle.html#music21.style.StyleMixin.editorial "music21.style.StyleMixin.editorial") | * [`style`](moduleStyle.html#music21.style.StyleMixin.style "music21.style.StyleMixin.style") |  |

[`Accidental`](#music21.pitch.Accidental "music21.pitch.Accidental") methods

Accidental.\_\_eq\_\_(*other*)[[source]](../_modules/music21/pitch.html#Accidental.__eq__)
:   Equality. Needed for pitch comparisons.

    ```python
    >>> a = pitch.Accidental('double-flat')
    >>> b = pitch.Accidental('double-flat')
    >>> c = pitch.Accidental('double-sharp')
    >>> a == b
    True
    ```

    ```python
    >>> a == c
    False
    ```

Accidental.inheritDisplay(*other*)[[source]](../_modules/music21/pitch.html#Accidental.inheritDisplay)
:   Given another Accidental object, inherit all the display properties
    of that object.

    This is needed when transposing Pitches: we need to retain accidental display properties.

    ```python
    >>> a = pitch.Accidental('double-flat')
    >>> a.displayType = 'always'
    >>> b = pitch.Accidental('sharp')
    >>> b.inheritDisplay(a)
    >>> b.displayType
    'always'
    ```

Accidental.isTwelveTone()[[source]](../_modules/music21/pitch.html#Accidental.isTwelveTone)
:   Return a boolean if this Accidental describes a twelve-tone, non-microtonal pitch.

    ```python
    >>> a = pitch.Accidental('half-flat')
    >>> a.isTwelveTone()
    False
    ```

    ```python
    >>> a = pitch.Accidental('###')
    >>> a.isTwelveTone()
    True
    ```

classmethod Accidental.listNames()[[source]](../_modules/music21/pitch.html#Accidental.listNames)
:   Returns a list of accidental names that have any sort of
    semantic importance in music21.

    You may choose a name not from this list (1/7th-sharp) but
    if it’s not on this list don’t expect it to do anything for you.

    This is a class method, so you may call it directly on the class:

    Listed in alphabetical order. (TODO: maybe from lowest to highest
    or something implying importance?)

    ```python
    >>> pitch.Accidental.listNames()
     ['double-flat', 'double-sharp', 'flat', 'half-flat',
      'half-sharp', 'natural', 'one-and-a-half-flat', 'one-and-a-half-sharp',
      'quadruple-flat', 'quadruple-sharp', 'sharp', 'triple-flat', 'triple-sharp']
    ```

    Or call on an instance of an accidental:

    ```python
    >>> f = pitch.Accidental('flat')
    >>> f.listNames()
     ['double-flat', 'double-sharp', 'flat', 'half-flat', 'half-sharp', 'natural',
      'one-and-a-half-flat', 'one-and-a-half-sharp', 'quadruple-flat', 'quadruple-sharp',
      'sharp', 'triple-flat', 'triple-sharp']
    ```

Accidental.set(*name*, *\**, *allowNonStandardValue=False*)[[source]](../_modules/music21/pitch.html#Accidental.set)
:   Change the type of the Accidental. Strings, numbers, and Lilypond (German-like)
    abbreviations are all accepted. All other values will change
    after setting.

    ```python
    >>> a = pitch.Accidental()
    >>> a.set('sharp')
    >>> a.alter
    1.0
    ```

    ```python
    >>> a = pitch.Accidental()
    >>> a.set(2)
    >>> a.modifier == '##'
    True
    ```

    ```python
    >>> a = pitch.Accidental()
    >>> a.set(2.0)
    >>> a.modifier == '##'
    True
    ```

    ```python
    >>> a = pitch.Accidental('--')
    >>> a.alter
    -2.0
    >>> a.set('half-sharp')
    >>> a.alter
    0.5
    >>> a.name
    'half-sharp'
    ```

    Setting an illegal name is generally an error:

    ```python
    >>> a.set('flat-flat-up')
    Traceback (most recent call last):
    music21.pitch.AccidentalException: flat-flat-up is not a supported accidental type
    ```

    But if ‘allowNonStandardValue’ is True then other names (if strings) or alters (if numbers)
    are allowed:

    ```python
    >>> a.set('quintuple-sharp', allowNonStandardValue=True)
    >>> a.set(5.0, allowNonStandardValue=True)
    >>> a.name
    'quintuple-sharp'
    >>> a.alter
    5.0
    ```

    This is the argument that .name and .alter use to allow non-standard names

    * Changed in v5: added allowNonStandardValue

Accidental.setAttributeIndependently(*attribute*, *value*)[[source]](../_modules/music21/pitch.html#Accidental.setAttributeIndependently)
:   Set an attribute of ‘name’, ‘alter’, and ‘modifier’, independently
    of the other attributes.

    ```python
    >>> a = pitch.Accidental('natural')
    >>> a.setAttributeIndependently('alter', 1.0)
    >>> a.alter
    1.0
    >>> a.name
    'natural'
    ```

    ```python
    >>> a.setAttributeIndependently('name', 'sori')
    >>> a.setAttributeIndependently('modifier', '$')
    >>> a.modifier
    '$'
    >>> a.name
    'sori'
    >>> a.alter
    1.0
    ```

    Only ‘name’, ‘alter’, and ‘modifier’ can be set independently:

    ```python
    >>> a.setAttributeIndependently('color', 'red')
    Traceback (most recent call last):
    music21.pitch.AccidentalException: Cannot set attribute color independently of other parts.
    ```

    * New in v5: needed because .name, .alter, and .modifier run .set()

[`Accidental`](#music21.pitch.Accidental "music21.pitch.Accidental") instance variables

Accidental.displayLocation
:   Location of accidental: “normal”, “above”, “below”.

Accidental.displaySize
:   Size in display: “cue”, “large”, or a percentage.

Accidental.displayStyle
:   Style of display: “parentheses”, “bracket”, “both”.

## Microtone

class music21.pitch.Microtone(*centsOrString: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") = 0*, *harmonicShift=1*)[[source]](../_modules/music21/pitch.html#Microtone)
:   The Microtone object defines a pitch transformation above or below a
    standard Pitch and its Accidental.

    ```python
    >>> m = pitch.Microtone(20)
    >>> m.cents
    20
    ```

    ```python
    >>> m.alter
    0.2...
    ```

    ```python
    >>> print(m)
    (+20c)
    >>> m
    <music21.pitch.Microtone (+20c)>
    ```

    Microtones can be shifted according to the harmonic. Here we take the 3rd
    harmonic of the previous microtone

    ```python
    >>> m.harmonicShift = 3
    >>> m.harmonicShift
    3
    >>> m
    <music21.pitch.Microtone (+20c+3rdH)>
    ```

    ```python
    >>> m.cents
    1922
    ```

    ```python
    >>> m.alter
    19.2...
    ```

    Microtonal changes can be positive or negative. Both Positive and negative
    numbers can optionally be placed in parentheses Negative numbers in
    parentheses still need the minus sign.

    ```python
    >>> m = pitch.Microtone('(-33.333333)')
    >>> m
    <music21.pitch.Microtone (-33c)>
    ```

    ```python
    >>> m = pitch.Microtone('33.333333')
    >>> m
    <music21.pitch.Microtone (+33c)>
    ```

    Note that we round the display of microtones to the nearest cent, but we
    keep the exact alteration in both .cents and .alter:

    ```python
    >>> m.cents
    33.333...
    ```

    ```python
    >>> m.alter
    0.3333...
    ```

[`Microtone`](#music21.pitch.Microtone "music21.pitch.Microtone") bases

* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")
* [`SlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.SlottedObjectMixin "music21.common.objects.SlottedObjectMixin")

[`Microtone`](#music21.pitch.Microtone "music21.pitch.Microtone") read-only properties

Microtone.alter
:   Return the microtone value in accidental alter values.

    ```python
    >>> pitch.Microtone(20).alter
    0.2
    ```

Microtone.cents
:   Return the microtone value in cents. This is not a settable property.
    To set the value in cents, simply use that value as a creation
    argument.

    ```python
    >>> pitch.Microtone(20).cents
    20
    ```

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`Microtone`](#music21.pitch.Microtone "music21.pitch.Microtone") read/write properties

Microtone.harmonicShift
:   Set or get the harmonic shift, altering the microtone

[`Microtone`](#music21.pitch.Microtone "music21.pitch.Microtone") methods

Microtone.\_\_eq\_\_(*other*)[[source]](../_modules/music21/pitch.html#Microtone.__eq__)
:   Compare cents (including harmonicShift)

    ```python
    >>> m1 = pitch.Microtone(20)
    >>> m2 = pitch.Microtone(20)
    >>> m3 = pitch.Microtone(21)
    >>> m1 == m2
    True
    >>> m1 == m3
    False
    ```

    ```python
    >>> m2.harmonicShift = 3
    >>> m1 == m2
    False
    ```

    Cannot compare True to a non-Microtone:

    ```python
    >>> m1 == pitch.Accidental(1)
    False
    ```

## Functions

music21.pitch.convertPitchClassToStr(*pc: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](../_modules/music21/pitch.html#convertPitchClassToStr)
:   Given a pitch class number, return a string.

    ```python
    >>> pitch.convertPitchClassToStr(3)
    '3'
    >>> pitch.convertPitchClassToStr(10)
    'A'
    ```

music21.pitch.isValidAccidentalName(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/pitch.html#isValidAccidentalName)
:   Check if name is a valid accidental name string that can
    be used to initialize an Accidental.

    Standard accidental names are valid:

    ```python
    >>> pitch.isValidAccidentalName('double-flat')
    True
    ```

    Accidental modifiers are valid:

    ```python
    >>> pitch.isValidAccidentalName('--')
    True
    ```

    Alternate accidental names are valid:

    ```python
    >>> pitch.isValidAccidentalName('eses')
    True
    ```

    Anything else is not valid:

    ```python
    >>> pitch.isValidAccidentalName('two flats')
    False
    ```

music21.pitch.simplifyMultipleEnharmonics(*pitches*, *criterion=<function \_dissonanceScore>*, *keyContext=None*)[[source]](../_modules/music21/pitch.html#simplifyMultipleEnharmonics)
:   Tries to simplify the enharmonic spelling of a list of pitches, pitch-
    or pitch-class numbers according to a given criterion.

    A function can be passed as an argument to criterion, that is tried to be
    minimized in a greedy left-to-right fashion.

    ```python
    >>> pitch.simplifyMultipleEnharmonics([11, 3, 6])
    [<music21.pitch.Pitch B>, <music21.pitch.Pitch D#>, <music21.pitch.Pitch F#>]
    ```

    ```python
    >>> pitch.simplifyMultipleEnharmonics([3, 8, 0])
    [<music21.pitch.Pitch E->, <music21.pitch.Pitch A->, <music21.pitch.Pitch C>]
    ```

    ```python
    >>> pitch.simplifyMultipleEnharmonics([pitch.Pitch('G3'),
    ...                                    pitch.Pitch('C-4'),
    ...                                    pitch.Pitch('D4')])
    [<music21.pitch.Pitch G3>, <music21.pitch.Pitch B3>, <music21.pitch.Pitch D4>]
    ```

    ```python
    >>> pitch.simplifyMultipleEnharmonics([pitch.Pitch('A3'),
    ...                                    pitch.Pitch('B#3'),
    ...                                    pitch.Pitch('E4')])
    [<music21.pitch.Pitch A3>, <music21.pitch.Pitch C4>, <music21.pitch.Pitch E4>]
    ```

    The attribute keyContext is for supplying a KeySignature or a Key
    which is used in the simplification:

    ```python
    >>> pitch.simplifyMultipleEnharmonics([6, 10, 1], keyContext=key.Key('B'))
    [<music21.pitch.Pitch F#>, <music21.pitch.Pitch A#>, <music21.pitch.Pitch C#>]
    ```

    ```python
    >>> pitch.simplifyMultipleEnharmonics([6, 10, 1], keyContext=key.Key('C-'))
    [<music21.pitch.Pitch G->, <music21.pitch.Pitch B->, <music21.pitch.Pitch D->]
    ```

    Note that if there’s no key context, then we won’t simplify everything (at least
    for now; this behavior may change, ).

    ```python
    >>> pitch.simplifyMultipleEnharmonics([pitch.Pitch('D--3'),
    ...                                    pitch.Pitch('F-3'),
    ...                                    pitch.Pitch('A--3')])
    [<music21.pitch.Pitch D--3>, <music21.pitch.Pitch F-3>, <music21.pitch.Pitch A--3>]
    ```

    ```python
    >>> pitch.simplifyMultipleEnharmonics([pitch.Pitch('D--3'),
    ...                                    pitch.Pitch('F-3'),
    ...                                    pitch.Pitch('A--3')],
    ...                                    keyContext=key.Key('C'))
    [<music21.pitch.Pitch C3>, <music21.pitch.Pitch E3>, <music21.pitch.Pitch G3>]
    ```

    * Changed in v7.3: fixed a bug with compound intervals (such as formed against
      the tonic of a KeySignature defaulting to octave 4):

    ```python
    >>> pitch.simplifyMultipleEnharmonics([pitch.Pitch('B5')], keyContext=key.Key('D'))
    [<music21.pitch.Pitch B5>]
    ```

music21.pitch.standardizeAccidentalName(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](../_modules/music21/pitch.html#standardizeAccidentalName)
:   Convert a valid accidental name to the standard accidental name.
    Raises AccidentalException if name is not a valid accidental name.

    ```python
    >>> pitch.standardizeAccidentalName('double-flat')
    'double-flat'
    ```

    ```python
    >>> pitch.standardizeAccidentalName('--')
    'double-flat'
    ```

    ```python
    >>> pitch.standardizeAccidentalName('eses')
    'double-flat'
    ```

    ```python
    >>> pitch.standardizeAccidentalName('two flats')
    Traceback (most recent call last):
    music21.pitch.AccidentalException: 'two flats' is not a supported accidental type
    ```
