Source: https://music21.org/music21docs/moduleReference/moduleMidiPercussion.html

# music21.midi.percussion

## PercussionMapper

class music21.midi.percussion.PercussionMapper[[source]](../_modules/music21/midi/percussion.html#PercussionMapper)
:   PercussionMapper provides tools to convert between 0-indexed MIDI pitches
    and music21 instruments, based on the official General MIDI Level 1 Percussion Key Map.
    This mapping is conventionally applied to MIDI channel 10;
    see <https://midi.org/general-midi-level-1> for more info.

    Give me the instrument that corresponds to MIDI note 58!

    ```python
    >>> pm = midi.percussion.PercussionMapper()
    >>> pm.reverseInstrumentMapping[58]
    <class 'music21.instrument.Vibraslap'>
    ```

    That’s right, vibraslap.

    But you’re better off using the midiPitchToInstrument() method below!

[`PercussionMapper`](#music21.midi.percussion.PercussionMapper "music21.midi.percussion.PercussionMapper") methods

PercussionMapper.midiInstrumentToPitch(*midiInstrument*)[[source]](../_modules/music21/midi/percussion.html#PercussionMapper.midiInstrumentToPitch)
:   Takes an instrument.Instrument object and returns a pitch object
    with the corresponding 1-indexed MIDI note, according to the GM Percussion Map.

    ```python
    >>> pm = midi.percussion.PercussionMapper()
    >>> myCow = instrument.Cowbell()
    >>> cowPitch = pm.midiInstrumentToPitch(myCow)
    >>> cowPitch.midi
    56
    ```

    Note that cowPitch is an actual pitch.Pitch object
    even though it’s meaningless!

    ```python
    >>> cowPitch
    <music21.pitch.Pitch G#3>
    ```

    If the instrument does not have an equivalent in the GM Percussion Map,
    return an Exception:

    ```python
    >>> myBagpipes = instrument.Bagpipes()
    >>> pipePitch = pm.midiInstrumentToPitch(myBagpipes)
    Traceback (most recent call last):
    music21.midi.percussion.MIDIPercussionException: <music21.instrument.Bagpipes 'Bagpipes'>
        is not in the GM Percussion Map!
    ```

PercussionMapper.midiPitchToInstrument(*midiPitch*)[[source]](../_modules/music21/midi/percussion.html#PercussionMapper.midiPitchToInstrument)
:   Takes a pitch.Pitch object or int ranging from 0-127 and returns
    the corresponding instrument in the GM Percussion Map.

    ```python
    >>> pm = midi.percussion.PercussionMapper()
    >>> cowPitch = pitch.Pitch(56)
    >>> cowbell = pm.midiPitchToInstrument(cowPitch)
    >>> cowbell
    <music21.instrument.Cowbell 'Cowbell'>
    ```

    Or it can just take an integer (representing MIDI note) for the pitch instead:

    ```python
    >>> moreCowbell = pm.midiPitchToInstrument(56)
    >>> moreCowbell
    <music21.instrument.Cowbell 'Cowbell'>
    ```

    The standard GM Percussion list goes from 35 to 81;
    pitches outside this range raise an exception.

    ```python
    >>> bassDrum1Pitch = pitch.Pitch('B-1')
    >>> pm.midiPitchToInstrument(bassDrum1Pitch)
    Traceback (most recent call last):
    music21.midi.percussion.MIDIPercussionException: 34 does not map to a valid instrument!
    ```

    Also, certain GM instruments do not have corresponding music21 instruments,
    so at present they also raise an exception.

    ```python
    >>> cabasaPitch = 69
    >>> pm.midiPitchToInstrument(cabasaPitch)
    Traceback (most recent call last):
    music21.midi.percussion.MIDIPercussionException: 69 does not map to a valid instrument!
    ```

    Some music21 Instruments have more than one MidiPitch. In this case you’ll
    get the same Instrument object but with a different modifier

    ```python
    >>> acousticBassDrumPitch = pitch.Pitch(35)
    >>> acousticBDInstrument = pm.midiPitchToInstrument(acousticBassDrumPitch)
    >>> acousticBDInstrument
    <music21.instrument.BassDrum 'Bass Drum'>
    >>> acousticBDInstrument.modifier
    'acoustic'
    ```

    ```python
    >>> oneBassDrumPitch = pitch.Pitch(36)
    >>> oneBDInstrument = pm.midiPitchToInstrument(oneBassDrumPitch)
    >>> oneBDInstrument
    <music21.instrument.BassDrum 'Bass Drum'>
    >>> oneBDInstrument.modifier
    '1'
    ```
