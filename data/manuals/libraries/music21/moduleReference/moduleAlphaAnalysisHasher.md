Source: https://music21.org/music21docs/moduleReference/moduleAlphaAnalysisHasher.html

# music21.alpha.analysis.hasher

## Hasher

class music21.alpha.analysis.hasher.Hasher[[source]](../_modules/music21/alpha/analysis/hasher.html#Hasher)
:   This is a modular hashing object that can hash notes, chords, and rests, and some of their
    properties. Steps to using and calling the hasher:

    1. Initialize a hasher object
    2. Set the properties that you want to hash. There are 4 main groups of properties/settings:

       ```python
       a) self.validTypes should be some combination of notes, chords, rests

       b) general hashing settings include self.includeReference. if
          self.includeReference is True, a reference to the original note/rest/chord is created
          and kept track of during the hashing process.

       c) note properties are things like pitch, duration, offset, and some slightly fancier
          properties

       d) self.stateVars is a dictionary of things you might want to hash that require some memory
          e.g. current key signature, interval from the last note
       ```
    3. call the hashStream() function on the stream you want to hash.

    This is what the Hasher object does the in background once hashStream() is called:

    1) It runs self.setupValidTypesAndStateVars() and sets up properties from (a) and (d) from
    above based on your settings

    2. It runs self.preprocessStream() and based on settings from (d)
    3. It determines which objects in the passed-in stream should be hashed

    4) It runs self.setupTupleList() and sets up self.tupleList, self.hashingFunctions
    and self.tupleClass, all related to each other. self.tupleList is a list of all the
    properties that are hashed. self.hashingFunctions is a dictionary of which hashing function
    should be used for each property (there are multiple ways of hashing a note’s pitch, for
    example, by MIDI number, or by a string representation). self.tupleClass is a NamedTuple
    that is constructed ad hoc based on which properties are to be hashed.

    5) For all the elements from the stream that are to be hashed, the hasher hashes every one of
    its properties that are to be hashed using the hashing function listed in
    self.hashingFunctions. It creates a single NamedTuple called a NoteHash for each element
    from the stream. However, if self.includeReference is set to True, a NoteHashWithReference
    tuple is created instead.

[`Hasher`](#music21.alpha.analysis.hasher.Hasher "music21.alpha.analysis.hasher.Hasher") methods

Hasher.addHashToFinalHash(*singleNoteHash*, *finalHash*, *reference*)[[source]](../_modules/music21/alpha/analysis/hasher.html#Hasher.addHashToFinalHash)

Hasher.addNoteHashToFinalHash(*finalHash*, *tupleHash*)[[source]](../_modules/music21/alpha/analysis/hasher.html#Hasher.addNoteHashToFinalHash)
:   creates a NoteHash object from tupleHash and adds the NoteHash
    object to the end of finalHash

    ```python
    >>> from collections import namedtuple
    >>> n = note.Note('C4')
    >>> NoteHash = namedtuple('NoteHash', ['Pitch', 'Duration'])
    >>> nh = NoteHash(n.pitch, n.duration)
    >>> finalHash = []
    >>> h = alpha.analysis.hasher.Hasher()
    >>> h.addNoteHashToFinalHash(finalHash, nh)
    >>> finalHash
    [(<music21.pitch.Pitch C4>, <music21.duration.Duration 1.0>)]
    ```

Hasher.addNoteHashWithReferenceToFinalHash(*finalHash*, *tupleHash*, *reference*)[[source]](../_modules/music21/alpha/analysis/hasher.html#Hasher.addNoteHashWithReferenceToFinalHash)
:   creates a NoteHashWithReference object from tupleHash and with the reference pass in
    and adds the NoteHashWithReference object to the end of finalHash

    ```python
    >>> from collections import namedtuple
    >>> n = note.Note('C4')
    >>> NoteHash = namedtuple('NoteHash', ['Pitch', 'Duration'])
    >>> nh = NoteHash(n.pitch, n.duration)
    >>> finalHash = []
    >>> h = alpha.analysis.hasher.Hasher()
    >>> h.addNoteHashWithReferenceToFinalHash(finalHash, nh, n)
    >>> finalHash
    [NoteHashWithReference(Pitch=C4, Duration=<music21.duration.Duration 1.0>)]
    ```

    ```python
    >>> finalHash[0].reference.id == n.id
    True
    ```

Hasher.hashMeasures(*s*)[[source]](../_modules/music21/alpha/analysis/hasher.html#Hasher.hashMeasures)
:   lightweight hasher. only hashes number of notes, first and last pitch

Hasher.hashStream(*s*)[[source]](../_modules/music21/alpha/analysis/hasher.html#Hasher.hashStream)
:   This method is the meat of the program. It goes through all the elements that are left
    to be hashed and individually hashes them by looking up which hashing functions ought
    to be used on each element and passing off the element to the method
    self.addSingleNoteHashToFinalHash, which creates the appropriate hash for that element
    and adds it to self.finalHash

Hasher.setupTupleList()[[source]](../_modules/music21/alpha/analysis/hasher.html#Hasher.setupTupleList)
:   Sets up self.hashingFunctions, a dictionary of which properties of self.validTypes should
    be hashed and which hashing functions should be used for those properties. Creates a
    tupleList of all the properties that are hashed and uses that to create a named tuple
    NoteHash with those properties. This is how we can generate a malleable named tuple
    NoteHash that is different depending upon which properties a particular instance of
    Hasher object hashes.

Hasher.setupValidTypesAndStateVars()[[source]](../_modules/music21/alpha/analysis/hasher.html#Hasher.setupValidTypesAndStateVars)
:   Sets up the self.stateVars dictionary depending on how the flags for
    self.hashIntervalFromLastNote and self.hashIsAccidental are set.

    ```python
    >>> h = alpha.analysis.hasher.Hasher()
    >>> h.hashIntervalFromLastNote = True
    >>> h.setupValidTypesAndStateVars()
    >>> h.stateVars
    {'IntervalFromLastNote': None}
    ```

    ```python
    >>> h2 = alpha.analysis.hasher.Hasher()
    >>> h2.hashIsAccidental = True
    >>> h2.setupValidTypesAndStateVars()
    >>> h2.stateVars
    {'KeySignature': None}
    ```

    ```python
    >>> key.KeySignature in h2.validTypes
    True
    ```

## NoteHash

class music21.alpha.analysis.hasher.NoteHash(*tupEls*)[[source]](../_modules/music21/alpha/analysis/hasher.html#NoteHash)
:   ```python
    >>> note1 = note.Note('C4')
    >>> nh = alpha.analysis.hasher.NoteHash((1, 2))
    >>> nh
    (1, 2)
    >>> a, b = nh
    >>> a
    1
    >>> b
    2
    >>> nh.__class__
    <... 'music21.alpha.analysis.hasher.NoteHash'>
    ```

## NoteHashWithReference

class music21.alpha.analysis.hasher.NoteHashWithReference(*hashItemsNT*)[[source]](../_modules/music21/alpha/analysis/hasher.html#NoteHashWithReference)
:   returns tuple with reference to original note or chord or rest

    ```python
    >>> from collections import namedtuple
    >>> NoteHash = namedtuple('NoteHash', ['Pitch', 'Duration'])
    >>> nh = NoteHash(60, 4)
    >>> nhwr = alpha.analysis.hasher.NoteHashWithReference(nh)
    >>> nhwr.reference = note.Note('C4')
    >>> nhwr
    NoteHashWithReference(Pitch=60, Duration=4)
    ```

    ```python
    >>> nhwr.Pitch
    60
    >>> nhwr.Duration
    4
    ```

    ```python
    >>> nhwr.hashItemsKeys
    ('Pitch', 'Duration')
    ```

    ```python
    >>> for val in nhwr:
    ...     print(val)
    60
    4
    ```

    ```python
    >>> nhwr.reference
    <music21.note.Note C>
    ```
