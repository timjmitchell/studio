Source: https://music21.org/music21docs/moduleReference/moduleMidiBase.html

# music21.midi.base

Objects and tools for processing MIDI data. Converts from MIDI files to
`MidiEvent`, `MidiTrack`, and
`MidiFile` objects, and vice versa.

This module originally used routines from Will Ware’s public domain midi.py
library from 2001 which was once posted at
groups.google.com/g/alt.sources/msg/0c5fc523e050c35e

## MidiEvent

class music21.midi.base.MidiEvent(*track: [MidiTrack](#music21.midi.base.MidiTrack "music21.midi.base.MidiTrack") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *type: [ChannelVoiceMessages](#music21.midi.base.ChannelVoiceMessages "music21.midi.base.ChannelVoiceMessages") | [ChannelModeMessages](#music21.midi.base.ChannelModeMessages "music21.midi.base.ChannelModeMessages") | [MetaEvents](#music21.midi.base.MetaEvents "music21.midi.base.MetaEvents") | [SysExEvents](#music21.midi.base.SysExEvents "music21.midi.base.SysExEvents") | [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")['DeltaTime'] = <MetaEvents.UNKNOWN: 0xFF>*, *time: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*, *channel: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 1*)[[source]](../_modules/music21/midi/base.html#MidiEvent)
:   A model of a MIDI event, including note-on, note-off, program change,
    controller change, any many others.

    MidiEvent objects are paired (preceded) by `DeltaTime`
    objects in the list of events in a MidiTrack object.

    The track argument must be a `MidiTrack` object.

    The type attribute is an enumeration of a Midi event from the ChannelVoiceMessages,
    ChannelModeMessages, SysExEvents, or MetaEvents enums; if unspecified,
    defaults to MetaEvents.UNKNOWN.

    The channel attribute is an integer channel id, from 1 to 16.

    The time attribute is an integer duration of the event in ticks. This value
    can be zero. This value is not essential, as ultimate time positioning is
    determined by `DeltaTime` objects.

    The pitch attribute is only defined for note-on and note-off messages.
    The attribute stores an integer representation (0-127, with 60 = middle C).

    The velocity attribute is only defined for note-on and note-off messages.
    The attribute stores an integer representation (0-127). A note-on message with
    velocity 0 is generally assumed to be the same as a note-off message.

    The data attribute is used for storing other messages,
    such as SEQUENCE\_TRACK\_NAME string values.

    Warning

    The attributes .midiProgram and .midiChannel on [`Instrument`](moduleInstrument.html#music21.instrument.Instrument "music21.instrument.Instrument")
    objects are 0-indexed, just as they need to be in the written binary .mid.
    However, as a convenience, `MidiEvent.channel` is 1-indexed. No
    analogous convenience is provided for program change data.

    ```python
    >>> mt = midi.MidiTrack(1)
    >>> me1 = midi.MidiEvent(mt)
    >>> me1.type = midi.ChannelVoiceMessages.NOTE_ON
    >>> me1.channel = 3
    >>> me1.time = 200
    >>> me1.pitch = 60
    >>> me1.velocity = 120
    >>> me1
    <music21.midi.MidiEvent NOTE_ON, t=200, track=1, channel=3, pitch=60, velocity=120>
    ```

    ```python
    >>> me2 = midi.MidiEvent(mt)
    >>> me2.type = midi.MetaEvents.SEQUENCE_TRACK_NAME
    >>> me2.data = 'guitar'
    >>> me2
    <music21.midi.MidiEvent SEQUENCE_TRACK_NAME, track=1, data=b'guitar'>
    ```

    Changed in v9.7 - None is not a valid type anymore. Use MetaEvents.UNKNOWN instead.
    :   Channel defaults to 1.

[`MidiEvent`](#music21.midi.base.MidiEvent "music21.midi.base.MidiEvent") bases

* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`MidiEvent`](#music21.midi.base.MidiEvent "music21.midi.base.MidiEvent") read-only properties

MidiEvent.sortOrder
:   Ensure that for MidiEvents at the same “time”, that order is
    NOTE\_OFF, PITCH\_BEND, all others.

    ```python
    >>> CVM = midi.ChannelVoiceMessages
    >>> noteOn = midi.MidiEvent(type=CVM.NOTE_ON)
    >>> noteOff = midi.MidiEvent(type=CVM.NOTE_OFF)
    >>> pitchBend = midi.MidiEvent(type=CVM.PITCH_BEND)
    ```

    ```python
    >>> sorted([noteOn, noteOff, pitchBend], key=lambda me: me.sortOrder)
    [<music21.midi.MidiEvent NOTE_OFF, track=None, channel=1>,
     <music21.midi.MidiEvent PITCH_BEND, track=None, channel=1>,
     <music21.midi.MidiEvent NOTE_ON, track=None, channel=1>]
    ```

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`MidiEvent`](#music21.midi.base.MidiEvent "music21.midi.base.MidiEvent") read/write properties

MidiEvent.data
:   Read or set the data (.parameter1) for the object

    Does some automatic conversions:

    ```python
    >>> me = midi.MidiEvent(type=midi.ChannelModeMessages.LOCAL_CONTROL)
    >>> me.data = True
    >>> me.data
    b'\x01'
    ```

MidiEvent.pitch

MidiEvent.velocity

[`MidiEvent`](#music21.midi.base.MidiEvent "music21.midi.base.MidiEvent") methods

MidiEvent.getBytes() → [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")[[source]](../_modules/music21/midi/base.html#MidiEvent.getBytes)
:   Return a set of bytes for this MIDI event (used for translating from music21 to MIDI)

    ```python
    >>> noteOn = midi.MidiEvent(type=midi.ChannelVoiceMessages.NOTE_ON, channel=10)
    >>> noteOn.pitch = 60
    >>> noteOn.velocity = 127
    >>> noteOn.getBytes()
    b'\x99<\x7f'
    ```

    Changing the pitch changes the second byte (from less than to greater than):

    ```python
    >>> noteOn.pitch = 62
    >>> noteOn.getBytes()
    b'\x99>\x7f'
    >>> ord('>')
    62
    ```

    Changing the velocity changes the third byte:

    ```python
    >>> noteOn.velocity = 64
    >>> noteOn.getBytes()
    b'\x99>@'
    ```

    The third byte is x40 but it is represented by ‘@’

    ```python
    >>> ord('@')
    64
    >>> hex(64)
    '0x40'
    ```

    And changing the channel changes the first byte:

    ```python
    >>> noteOn.channel = 11
    >>> noteOn.getBytes()
    b'\x9a>@'
    ```

MidiEvent.isChannelEvent() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/midi/base.html#MidiEvent.isChannelEvent)
:   returns bool if the channel matters for this event

    ```python
    >>> me = midi.MidiEvent(type=midi.ChannelVoiceMessages.NOTE_ON, channel=4)
    >>> me.isChannelEvent()
    True
    >>> dt = midi.DeltaTime()
    >>> dt.isChannelEvent()
    False
    ```

MidiEvent.isDeltaTime() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/midi/base.html#MidiEvent.isDeltaTime)
:   Return a boolean if this is a DeltaTime subclass.

    ```python
    >>> mt = midi.MidiTrack(1)
    >>> dt = midi.DeltaTime(mt)
    >>> dt.isDeltaTime()
    True
    ```

MidiEvent.isNoteOff() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/midi/base.html#MidiEvent.isNoteOff)
:   Return a boolean if this should be interpreted as a note-off message,
    either as a real note-off or as a note-on with zero velocity.

    ```python
    >>> mt = midi.MidiTrack(1)
    >>> me1 = midi.MidiEvent(mt)
    >>> me1.type = midi.ChannelVoiceMessages.NOTE_OFF
    >>> me1.isNoteOn()
    False
    >>> me1.isNoteOff()
    True
    ```

    ```python
    >>> me2 = midi.MidiEvent(mt)
    >>> me2.type = midi.ChannelVoiceMessages.NOTE_ON
    >>> me2.velocity = 0
    >>> me2.isNoteOn()
    False
    >>> me2.isNoteOff()
    True
    ```

    See `isNoteOn()` for more examples.

MidiEvent.isNoteOn() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/midi/base.html#MidiEvent.isNoteOn)
:   Return a boolean if this is a note-on message and velocity is not zero.

    ```python
    >>> mt = midi.MidiTrack(1)
    >>> me1 = midi.MidiEvent(mt)
    >>> me1.type = midi.ChannelVoiceMessages.NOTE_ON
    >>> me1.velocity = 120
    >>> me1.isNoteOn()
    True
    >>> me1.isNoteOff()
    False
    ```

    A zero velocity note-on is treated as a note-off:

    ```python
    >>> me1.velocity = 0
    >>> me1.isNoteOn()
    False
    >>> me1.isNoteOff()
    True
    ```

    A midi event can be neither a note on or a note off.

    ```python
    >>> me1.type = midi.ChannelVoiceMessages.PROGRAM_CHANGE
    >>> me1.isNoteOn()
    False
    >>> me1.isNoteOff()
    False
    ```

MidiEvent.matchedNoteOff(*other: [MidiEvent](#music21.midi.base.MidiEvent "music21.midi.base.MidiEvent")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/midi/base.html#MidiEvent.matchedNoteOff)
:   Returns True if other is a MIDI event that specifies
    a note-off message for this message. That is, this event
    is a NOTE\_ON message, and the other is a NOTE\_OFF message
    for this pitch on this channel. Otherwise returns False

    ```python
    >>> mt = midi.MidiTrack(1)
    >>> me1 = midi.MidiEvent(mt)
    >>> me1.type = midi.ChannelVoiceMessages.NOTE_ON
    >>> me1.velocity = 120
    >>> me1.pitch = 60
    ```

    ```python
    >>> me2 = midi.MidiEvent(mt)
    >>> me2.type = midi.ChannelVoiceMessages.NOTE_ON
    >>> me2.velocity = 0
    >>> me2.pitch = 60
    ```

    me2 is a Note off for me1 because it has velocity 0 and matches
    pitch.

    ```python
    >>> me1.matchedNoteOff(me2)
    True
    ```

    Now the pitch does not match, so it does not work.

    ```python
    >>> me2.pitch = 61
    >>> me1.matchedNoteOff(me2)
    False
    ```

    ```python
    >>> me2.type = midi.ChannelVoiceMessages.NOTE_OFF
    >>> me1.matchedNoteOff(me2)
    False
    ```

    ```python
    >>> me2.pitch = 60
    >>> me1.matchedNoteOff(me2)
    True
    ```

    Channels must match also:

    ```python
    >>> me2.channel = 12
    >>> me1.matchedNoteOff(me2)
    False
    ```

    Note that this method is no longer used in MIDI Parsing
    because it is inefficient.

MidiEvent.parseChannelVoiceMessage(*midiBytes: [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")*) → [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")[[source]](../_modules/music21/midi/base.html#MidiEvent.parseChannelVoiceMessage)
:   Take a set of bytes that represent a ChannelVoiceMessage and set the
    appropriate event type and data, returning the remaining bytes.

    Channel voice messages start with a one-byte message from 0x80 to 0xEF,
    where the first nibble (8-E) is the message type and the second nibble (0-F)
    is the channel represented in hex.

    First let’s create a MidiEvent that does not know its type.

    ```python
    >>> mt = midi.MidiTrack(1)
    >>> me1 = midi.MidiEvent(mt)
    >>> me1
    <music21.midi.MidiEvent UNKNOWN, track=1>
    ```

    Now create two messages – a note on (at pitch = 60 or C4) at velocity 120

    ```python
    >>> midBytes = bytes([0x92, 60, 120])
    >>> midBytes
    b'\x92<x'
    ```

    Add a second hypothetical message (would normally be a delta time)

    ```python
    >>> midBytes += b'hello'
    >>> midBytes
    b'\x92<xhello'
    ```

    Now see how parsing this ChannelVoiceMessage changes the MidiEvent

    ```python
    >>> remainder = me1.parseChannelVoiceMessage(midBytes)
    >>> me1
    <music21.midi.MidiEvent NOTE_ON, track=1, channel=3, pitch=60, velocity=120>
    ```

    The remainder would probably contain a delta time and following
    events, but here we’ll just show that it passes whatever is left through.

    ```python
    >>> remainder
    b'hello'
    ```

    We will ignore remainders for the rest of this demo. Note that all
    attributes are set properly:

    ```python
    >>> me1.type
    <ChannelVoiceMessages.NOTE_ON: 0x90>
    >>> me1.pitch  # 60 = middle C
    60
    >>> me1.velocity
    120
    ```

    The channel is 3 because 0x90 is NOTE\_ON for channel 1, 0x91 is 2, and 0x92 is 3, etc.

    ```python
    >>> me1.channel
    3
    ```

    Now let’s make a program change on channel 16:

    ```python
    >>> me2 = midi.MidiEvent(mt)
    >>> rem = me2.parseChannelVoiceMessage(bytes([0xCF, 71]))
    >>> me2
    <music21.midi.MidiEvent PROGRAM_CHANGE, track=1, channel=16, data=71>
    >>> me2.data  # 71 = clarinet (0-127 indexed)
    71
    ```

    Program changes and channel pressures only go to 127. More than that signals an error:

    ```python
    >>> me2.parseChannelVoiceMessage(bytes([0xCF, 200]))
    Traceback (most recent call last):
    music21.midi.base.MidiException: Cannot have a
        <ChannelVoiceMessages.PROGRAM_CHANGE: 0xC0> followed by a byte > 127: 200
    ```

MidiEvent.read(*midiBytes: [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")*) → [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")[[source]](../_modules/music21/midi/base.html#MidiEvent.read)
:   Parse the bytes given and take the beginning
    section and convert it into data for this event and return the
    now truncated bytes.

    ```python
    >>> channel = 0x2
    >>> noteOnMessage = midi.ChannelVoiceMessages.NOTE_ON | channel
    >>> hex(noteOnMessage)
    '0x92'
    ```

    This is how the system reads note-on messages (0x90-0x9F) and channels

    ```python
    >>> hex(0x91 & 0xF0)  # testing message type extraction
    '0x90'
    >>> hex(0x92 & 0xF0)  # testing message type extraction
    '0x90'
    >>> (0x90 & 0x0F) + 1  # getting the channel
    1
    >>> (0x9F & 0x0F) + 1  # getting the channel
    16
    ```

MidiEvent.setPitchBend(*cents: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*, *bendRange=2*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/midi/base.html#MidiEvent.setPitchBend)
:   Treat this event as a pitch bend value, and set the .parameter1 and
    :   .parameter2 fields appropriately given a specified bend value in cents.

    Also called Pitch Wheel

    The bendRange parameter gives the number of half steps in the bend range.

    ```python
    >>> mt = midi.MidiTrack(1)
    >>> me1 = midi.MidiEvent(mt, type=midi.ChannelVoiceMessages.PITCH_BEND)
    >>> me1.setPitchBend(50)
    >>> me1.parameter1, me1.parameter2
    (0, 80)
    >>> me1.setPitchBend(100)
    >>> me1.parameter1, me1.parameter2
    (0, 96)
    ```

    Neutral is 0, 64

    ```python
    >>> me1.setPitchBend(0)
    >>> me1.parameter1, me1.parameter2
    (0, 64)
    ```

    Parameter 2 is the most significant digit, not
    parameter 1.

    ```python
    >>> me1.setPitchBend(101)
    >>> me1.parameter1, me1.parameter2
    (40, 96)
    ```

    Exceeding maximum pitch bend sets the max (127, 127)

    ```python
    >>> me1.setPitchBend(200)
    >>> me1.parameter1, me1.parameter2
    (127, 127)
    >>> me1.setPitchBend(300)
    >>> me1.parameter1, me1.parameter2
    (127, 127)
    ```

    ```python
    >>> me1.setPitchBend(-50)
    >>> me1.parameter1, me1.parameter2
    (0, 48)
    >>> me1.setPitchBend(-100)
    >>> me1.parameter1, me1.parameter2
    (0, 32)
    >>> me1.setPitchBend(-196)
    >>> me1.parameter1, me1.parameter2
    (36, 1)
    >>> me1.setPitchBend(-200)
    >>> me1.parameter1, me1.parameter2
    (0, 0)
    ```

    Again, excess trimmed

    ```python
    >>> me1.setPitchBend(-300)
    >>> me1.parameter1, me1.parameter2
    (0, 0)
    ```

    But a larger bendRange can be set in semitones for non-GM devices:

    ```python
    >>> me1.setPitchBend(-300, bendRange=4)
    >>> me1.parameter1, me1.parameter2
    (0, 16)
    >>> me1.setPitchBend(-399, bendRange=4)
    >>> me1.parameter1, me1.parameter2
    (20, 0)
    ```

## DeltaTime

class music21.midi.base.DeltaTime(*track: [MidiTrack](#music21.midi.base.MidiTrack "music21.midi.base.MidiTrack") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *time: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*, *channel: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 1*)[[source]](../_modules/music21/midi/base.html#DeltaTime)
:   A `MidiEvent` subclass that stores the
    time change (in ticks) since the start or since the last MidiEvent.

    Pairs of DeltaTime and MidiEvent objects are the basic presentation of temporal data.

    The track argument must be a `MidiTrack` object.

    Time values are in integers, representing ticks.

    The channel attribute, inherited from MidiEvent is not used and set to 1
    unless overridden (it does not do anything if set and is not written out to MIDI).

    ```python
    >>> mt = midi.MidiTrack(1)
    >>> dt = midi.DeltaTime(mt)
    >>> dt.time = 1
    >>> dt
    <music21.midi.DeltaTime t=1, track=1>
    ```

    Changed in v9.7 – DeltaTime repr no longer lists its channel (to de-emphasize it).
    :   Channel defaults to 1.

[`DeltaTime`](#music21.midi.base.DeltaTime "music21.midi.base.DeltaTime") bases

* [`MidiEvent`](#music21.midi.base.MidiEvent "music21.midi.base.MidiEvent")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`DeltaTime`](#music21.midi.base.DeltaTime "music21.midi.base.DeltaTime") read-only properties

Read-only properties inherited from [`MidiEvent`](#music21.midi.base.MidiEvent "music21.midi.base.MidiEvent"):

|  |  |  |
| --- | --- | --- |
| * [`sortOrder`](#music21.midi.base.MidiEvent.sortOrder "music21.midi.base.MidiEvent.sortOrder") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`DeltaTime`](#music21.midi.base.DeltaTime "music21.midi.base.DeltaTime") read/write properties

Read/write properties inherited from [`MidiEvent`](#music21.midi.base.MidiEvent "music21.midi.base.MidiEvent"):

|  |  |  |
| --- | --- | --- |
| * [`data`](#music21.midi.base.MidiEvent.data "music21.midi.base.MidiEvent.data") | * [`pitch`](#music21.midi.base.MidiEvent.pitch "music21.midi.base.MidiEvent.pitch") | * [`velocity`](#music21.midi.base.MidiEvent.velocity "music21.midi.base.MidiEvent.velocity") |

[`DeltaTime`](#music21.midi.base.DeltaTime "music21.midi.base.DeltaTime") methods

DeltaTime.getBytes() → [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")[[source]](../_modules/music21/midi/base.html#DeltaTime.getBytes)
:   Convert the time integer into a set of bytes.

    ```python
    >>> mt = midi.MidiTrack(1)
    >>> dt = midi.DeltaTime(mt)
    >>> dt.time = 1
    >>> dt.getBytes()
    b'\x01'
    ```

    ```python
    >>> dt.time = 128
    >>> dt.getBytes()
    b'\x81\x00'
    ```

    ```python
    >>> dt.time = 257
    >>> dt.getBytes()
    b'\x82\x01'
    ```

    ```python
    >>> dt.time = 16385
    >>> dt.getBytes()
    b'\x81\x80\x01'
    ```

DeltaTime.isChannelEvent() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/midi/base.html#DeltaTime.isChannelEvent)
:   Save processing time – is always False

DeltaTime.readUntilLowByte(*oldBytes: [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")][[source]](../_modules/music21/midi/base.html#DeltaTime.readUntilLowByte)
:   Read a byte-string until hitting a character below 0x80
    and return the converted number and the rest of the bytes.

    The first number is also stored in self.time.

    ```python
    >>> mt = midi.MidiTrack(1)
    >>> dt = midi.DeltaTime(mt)
    >>> dt.time
    0
    ```

    ```python
    >>> dt.readUntilLowByte(b'\x20')
    (32, b'')
    >>> dt.time
    32
    ```

    ```python
    >>> dt.readUntilLowByte(b'\x20hello')
    (32, b'hello')
    ```

    here the ‘x82’ is above 0x80 so the ‘h’ is read
    as part of the continuation.

    ```python
    >>> dt.readUntilLowByte(b'\x82hello')
    (360, b'ello')
    ```

    Changed in v9: had an incompatible signature with MidiEvent

Methods inherited from [`MidiEvent`](#music21.midi.base.MidiEvent "music21.midi.base.MidiEvent"):

|  |  |  |
| --- | --- | --- |
| * [`isDeltaTime()`](#music21.midi.base.MidiEvent.isDeltaTime "music21.midi.base.MidiEvent.isDeltaTime") * [`isNoteOff()`](#music21.midi.base.MidiEvent.isNoteOff "music21.midi.base.MidiEvent.isNoteOff") * [`isNoteOn()`](#music21.midi.base.MidiEvent.isNoteOn "music21.midi.base.MidiEvent.isNoteOn") | * [`matchedNoteOff()`](#music21.midi.base.MidiEvent.matchedNoteOff "music21.midi.base.MidiEvent.matchedNoteOff") * [`parseChannelVoiceMessage()`](#music21.midi.base.MidiEvent.parseChannelVoiceMessage "music21.midi.base.MidiEvent.parseChannelVoiceMessage") | * [`read()`](#music21.midi.base.MidiEvent.read "music21.midi.base.MidiEvent.read") * [`setPitchBend()`](#music21.midi.base.MidiEvent.setPitchBend "music21.midi.base.MidiEvent.setPitchBend") |

## MidiTrack

class music21.midi.base.MidiTrack(*index: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*)[[source]](../_modules/music21/midi/base.html#MidiTrack)
:   A MIDI Track. Each track contains an index and a list of events.

    All events are stored in the events list, in order.

    An index is an integer identifier for this object. It is often called
    “trackId” though technically the id for a MidiTrack is always b’MTrk’

    ```python
    >>> mt = midi.MidiTrack(index=3)
    >>> mt.events
    []
    >>> mt.index
    3
    ```

    The data consists of all the midi data after b’MTrk’

    ```python
    >>> mt.data
    b''
    ```

    And the .length is the same as the data’s length

    ```python
    >>> mt.length
    0
    ```

    After reading a string

    ```python
    >>> mt.read(b'MTrk\x00\x00\x00\x16\x00\xff\x03\x00\x00'
    ...         + b'\xe0\x00@\x00\x90CZ\x88\x00\x80C\x00\x88\x00\xff/\x00')
    b''
    ```

    The returned value is what is left over after the track is read
    (for instance the data for another track)

    ```python
    >>> mt.length
    22
    ```

    New in v9.7: len(mt) returns the same as mt.length, but more Pythonic.

    ```python
    >>> len(mt)
    22
    ```

    ```python
    >>> mt.data[:8]
    b'\x00\xff\x03\x00\x00\xe0\x00@'
    ```

    Note that the ‘x16’ got translated to ascii ‘@’.

    ```python
    >>> mt.events
    [<music21.midi.DeltaTime (empty) track=3>,
     <music21.midi.MidiEvent SEQUENCE_TRACK_NAME, track=3, data=b''>,
     <music21.midi.DeltaTime (empty) track=3>,
     <music21.midi.MidiEvent PITCH_BEND, track=3, channel=1, parameter1=0, parameter2=64>,
     <music21.midi.DeltaTime (empty) track=3>,
     <music21.midi.MidiEvent NOTE_ON, track=3, channel=1, pitch=67, velocity=90>,
     <music21.midi.DeltaTime t=1024, track=3>,
     <music21.midi.MidiEvent NOTE_OFF, track=3, channel=1, pitch=67, velocity=0>,
     <music21.midi.DeltaTime t=1024, track=3>,
     <music21.midi.MidiEvent END_OF_TRACK, track=3, data=b''>]
    ```

    ```python
    >>> mt
    <music21.midi.MidiTrack 3 -- 10 events>
    ```

    There is a class attribute of the headerId which is the same for
    all MidiTrack objects

    ```python
    >>> midi.MidiTrack.headerId
    b'MTrk'
    ```

[`MidiTrack`](#music21.midi.base.MidiTrack "music21.midi.base.MidiTrack") bases

* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`MidiTrack`](#music21.midi.base.MidiTrack "music21.midi.base.MidiTrack") read-only properties

MidiTrack.length

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`MidiTrack`](#music21.midi.base.MidiTrack "music21.midi.base.MidiTrack") methods

MidiTrack.getBytes() → [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")[[source]](../_modules/music21/midi/base.html#MidiTrack.getBytes)
:   Returns bytes of midi-data from the .events in the object.
    For conversion from music21 to MIDI.

    For example: two events, one note-on and one note-off on C4 which appears as “<”
    in the data.

    ```python
    >>> mt = midi.MidiTrack(index=2)
    >>> dt1 = midi.DeltaTime(mt, time=0)
    >>> noteOn = midi.MidiEvent(mt, type=midi.ChannelVoiceMessages.NOTE_ON, channel=3)
    >>> noteOn.pitch = 60
    >>> noteOn.velocity = 20
    >>> dt2 = midi.DeltaTime(mt, time=1030)
    >>> noteOff = midi.MidiEvent(mt, type=midi.ChannelVoiceMessages.NOTE_OFF, channel=3)
    >>> noteOff.pitch = 60
    >>> noteOff.velocity = 0
    ```

    ```python
    >>> mt.events = [dt1, noteOn, dt2, noteOff]
    >>> bytes = mt.getBytes()
    >>> bytes
    b'MTrk\x00\x00\x00\t\x00\x92<\x14\x88\x06\x82<\x00'
    ```

    Explanation:

    The first four bytes MTrk are the header for any MIDI Track

    ```python
    >>> bytes[:4]
    b'MTrk'
    ```

    The next four bytes are the length of the data in bytes, the final b’t’
    indicates there are 9 bytes to follow.

    ```python
    >>> midi.base.getNumber(bytes[4:8], 4)
    (9, b'')
    ```

    The next byte is an empty delta time event.

    ```python
    >>> bytes[8]
    0
    ```

    The next three bytes are the note-on event.

    ```python
    >>> noteOn2 = midi.MidiEvent()
    >>> _ = noteOn2.parseChannelVoiceMessage(bytes[9:12])
    >>> noteOn2
    <music21.midi.MidiEvent NOTE_ON, track=None, channel=3, pitch=60, velocity=20>
    ```

    Followed by two bytes for the DeltaTime of 1030 ticks.

    ```python
    >>> dt3 = midi.DeltaTime()
    >>> dt3.readUntilLowByte(bytes[12:14])
    (1030, b'')
    ```

    The 1030 is stored as b’x88x06’ where the first byte is 136 and the second 6,
    but MIDI stores each continuing digit as the last 7 bits of a 8-bit number with
    first bit 1, so we remove the first bit by subtracting 128: 136 - 128 = 8.
    Then we multiply 8 by 128 to get 1024 and add 6 to get 1030.

    Finally, the last three bytes are the note-off event.

    ```python
    >>> noteOff2 = midi.MidiEvent()
    >>> _ = noteOff2.parseChannelVoiceMessage(bytes[14:])
    >>> noteOff2
    <music21.midi.MidiEvent NOTE_OFF, track=None, channel=3, pitch=60, velocity=0>
    ```

MidiTrack.getChannels() → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][[source]](../_modules/music21/midi/base.html#MidiTrack.getChannels)
:   Get all channels used in this Track (sorted) excepting events like DeltaTime
    or end events where the channel does not matter

    ```python
    >>> mt = midi.MidiTrack(index=2)
    >>> noteOn = midi.MidiEvent(type=midi.ChannelVoiceMessages.NOTE_ON, channel=14)
    >>> noteOn2 = midi.MidiEvent(type=midi.ChannelVoiceMessages.NOTE_ON, channel=5)
    >>> dt = midi.DeltaTime(1000, channel=2)  # channel does not matter
    >>> noteOn3 = midi.MidiEvent(type=midi.ChannelVoiceMessages.NOTE_ON, channel=14)
    >>> noteOn4 = midi.MidiEvent(type=midi.ChannelVoiceMessages.PROGRAM_CHANGE, channel=5)
    ```

    ```python
    >>> mt.events = [noteOn, noteOn2, dt, noteOn3, noteOn4]
    >>> mt.getChannels()
    [5, 14]
    ```

MidiTrack.getProgramChanges() → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][[source]](../_modules/music21/midi/base.html#MidiTrack.getProgramChanges)
:   Get all unique program changes used in this Track, in order they appear.

    ```python
    >>> mt = midi.MidiTrack(index=2)
    >>> pc1 = midi.MidiEvent(type=midi.ChannelVoiceMessages.PROGRAM_CHANGE)
    >>> pc1.data = 14
    >>> noteOn = midi.MidiEvent(type=midi.ChannelVoiceMessages.NOTE_ON, channel=14)
    >>> pc2 = midi.MidiEvent(type=midi.ChannelVoiceMessages.PROGRAM_CHANGE)
    >>> pc2.data = 1
    ```

    ```python
    >>> mt.events = [pc1, noteOn, pc2]
    >>> mt.getProgramChanges()
    [14, 1]
    ```

MidiTrack.hasNotes() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/midi/base.html#MidiTrack.hasNotes)
:   Return True/False if this track has any note-ons defined.

    ```python
    >>> mt = midi.MidiTrack(index=2)
    >>> mt.hasNotes()
    False
    ```

    ```python
    >>> noteOn = midi.MidiEvent(type=midi.ChannelVoiceMessages.NOTE_ON, channel=1)
    >>> mt.events = [noteOn]
    ```

    ```python
    >>> mt.hasNotes()
    True
    ```

MidiTrack.processDataToEvents(*trackData: [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)") = b''*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/midi/base.html#MidiTrack.processDataToEvents)
:   Populate .events with trackData. Called by .read()

MidiTrack.read(*midiBytes: [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")*) → [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")[[source]](../_modules/music21/midi/base.html#MidiTrack.read)
:   Read as much of the bytes object (representing midi data) as necessary;
    return the remaining bytes object for reassignment and further processing.

    The string should begin with MTrk, specifying a Midi Track

    Stores the read data (after the header and length information) in self.data

    Calls processDataToEvents which creates
    `DeltaTime`
    and `MidiEvent` objects and stores them in self.events

MidiTrack.setChannel(*value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/midi/base.html#MidiTrack.setChannel)
:   Set the one-indexed channel of all events in this Track.

    ```python
    >>> mt = midi.MidiTrack(index=2)
    >>> noteOn = midi.MidiEvent(type=midi.ChannelVoiceMessages.NOTE_ON, channel=1)
    >>> mt.events = [noteOn]
    >>> mt.setChannel(11)
    >>> noteOn.channel
    11
    ```

    Channel must be a value from 1-16

    ```python
    >>> mt.setChannel(22)
    Traceback (most recent call last):
    music21.midi.base.MidiException: bad channel value: 22
    ```

MidiTrack.updateEvents() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/midi/base.html#MidiTrack.updateEvents)
:   We may attach events to this track before setting their track parameter.
    This method will move through all events and set their track to this track.

    ```python
    >>> mt = midi.MidiTrack(index=2)
    >>> noteOn = midi.MidiEvent(type=midi.ChannelVoiceMessages.NOTE_ON, channel=1)
    >>> noteOn.pitch = 60
    >>> noteOn.velocity = 20
    >>> noteOn
    <music21.midi.MidiEvent NOTE_ON, track=None, channel=1, pitch=60, velocity=20>
    ```

    ```python
    >>> mt.events = [noteOn]
    >>> mt.updateEvents()
    >>> noteOn
    <music21.midi.MidiEvent NOTE_ON, track=2, channel=1, pitch=60, velocity=20>
    >>> noteOn.track is mt
    True
    ```

## MidiFile

class music21.midi.base.MidiFile[[source]](../_modules/music21/midi/base.html#MidiFile)
:   Low-level MIDI file writing, emulating methods from normal Python files.

    For most users, do not go here, simply use:

    > score = converter.parse(‘path/to/file/in.mid’)
    > midi\_out = score.write(‘midi’, fp=’path/to/file/out.mid’)

    The ticksPerQuarterNote attribute must be set before writing. 1024 is a common value.

    This object is returned by some properties for directly writing files of midi representations.

    ```python
    >>> mf = midi.MidiFile()
    >>> mf
    <music21.midi.MidiFile 0 tracks>
    ```

    Music21 can read format 0 and format 1, and writes format 1. Format 2 files
    are not parsable.

    ```python
    >>> mf.format
    1
    ```

    After loading or before writing, tracks are stored in this list.

    ```python
    >>> mf.tracks
    []
    ```

    Most midi files store ticksPerQuarterNote and not ticksPerSecond

    ```python
    >>> mf.ticksPerQuarterNote
    10080
    >>> mf.ticksPerSecond is None
    True
    ```

    All MidiFiles have the same headerId

    ```python
    >>> midi.MidiFile.headerId
    b'MThd'
    ```

[`MidiFile`](#music21.midi.base.MidiFile "music21.midi.base.MidiFile") bases

* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`MidiFile`](#music21.midi.base.MidiFile "music21.midi.base.MidiFile") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`MidiFile`](#music21.midi.base.MidiFile "music21.midi.base.MidiFile") methods

MidiFile.close() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/midi/base.html#MidiFile.close)
:   Close the file.

MidiFile.open(*filename*, *attrib='rb'*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/midi/base.html#MidiFile.open)
:   Open a MIDI file path for reading or writing.

    For writing to a MIDI file, attrib should be “wb”.

MidiFile.openFileLike(*fileLike: [BinaryIO](https://docs.python.org/3/library/typing.html#typing.BinaryIO "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/midi/base.html#MidiFile.openFileLike)
:   Assign a file-like object, such as those provided by BytesIO, as an open file object.

    ```python
    >>> from io import BytesIO
    >>> fileLikeOpen = BytesIO()
    >>> mf = midi.MidiFile()
    >>> mf.openFileLike(fileLikeOpen)
    >>> mf.close()
    ```

MidiFile.read() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/midi/base.html#MidiFile.read)
:   Read and parse MIDI data stored in a file.

MidiFile.readstr(*midiBytes: [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/midi/base.html#MidiFile.readstr)
:   Read and parse MIDI data as a bytes, putting the
    data in .ticksPerQuarterNote and a list of
    MidiTrack objects in the attribute .tracks.

    The name readstr is a carryover from Python 2.
    It works on bytes objects, not strings

MidiFile.write() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/midi/base.html#MidiFile.write)
:   Write MIDI data as a file to the file opened with .open().

MidiFile.writeMThdStr() → [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")[[source]](../_modules/music21/midi/base.html#MidiFile.writeMThdStr)
:   Convert the information in self.ticksPerQuarterNote
    into MIDI data header and return it as bytes.

    The name writeMThdStr is a carry-over from Python 2. It works on bytes, not strings.

MidiFile.writestr() → [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")[[source]](../_modules/music21/midi/base.html#MidiFile.writestr)
:   Generate the MIDI data header and convert the list of
    MidiTrack objects in self.tracks into MIDI data and return it as bytes.

    The name writestr is a carry-over from Python 2. It works on bytes, not strings.

## ChannelModeMessages

class music21.midi.base.ChannelModeMessages(*\*values*)[[source]](../_modules/music21/midi/base.html#ChannelModeMessages)

[`ChannelModeMessages`](#music21.midi.base.ChannelModeMessages "music21.midi.base.ChannelModeMessages") bases

* [`ContainsEnum`](moduleCommonEnums.html#music21.common.enums.ContainsEnum "music21.common.enums.ContainsEnum")

## ChannelVoiceMessages

class music21.midi.base.ChannelVoiceMessages(*\*values*)[[source]](../_modules/music21/midi/base.html#ChannelVoiceMessages)
:   ChannelVoiceMessages are the main MIDI messages for channel 1-16, such as
    NOTE\_ON, NOTE\_OFF, etc.

[`ChannelVoiceMessages`](#music21.midi.base.ChannelVoiceMessages "music21.midi.base.ChannelVoiceMessages") bases

* [`ContainsEnum`](moduleCommonEnums.html#music21.common.enums.ContainsEnum "music21.common.enums.ContainsEnum")

## MetaEvents

class music21.midi.base.MetaEvents(*\*values*)[[source]](../_modules/music21/midi/base.html#MetaEvents)

[`MetaEvents`](#music21.midi.base.MetaEvents "music21.midi.base.MetaEvents") bases

* [`ContainsEnum`](moduleCommonEnums.html#music21.common.enums.ContainsEnum "music21.common.enums.ContainsEnum")

## SysExEvents

class music21.midi.base.SysExEvents(*\*values*)[[source]](../_modules/music21/midi/base.html#SysExEvents)

[`SysExEvents`](#music21.midi.base.SysExEvents "music21.midi.base.SysExEvents") bases

* [`ContainsEnum`](moduleCommonEnums.html#music21.common.enums.ContainsEnum "music21.common.enums.ContainsEnum")

## Functions

music21.midi.base.getNumber(*midiBytes: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *length: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][[source]](../_modules/music21/midi/base.html#getNumber)

music21.midi.base.getNumber(*midiBytes: [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")*, *length: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")]
:   Extract the first length bytes from a bytes object (or int)
    and return it and the remaining bytes object as a 2-tuple

    The length is the number of chars to read.
    This will sum a length greater than 1 if desired.

    Note that MIDI uses big-endian for everything.
    This is the inverse of Python’s chr() function.

    Read first two bytes from the bytes encoding of “tests” and return the remainder

    ```python
    >>> midi.getNumber(b'tests', 2)
    (29797, b'sts')
    ```

    That number comes from:

    ```python
    >>> ord('t') * 256 + ord('e')
    29797
    ```

    Demonstration of reading the whole length of a byte in:

    ```python
    >>> midi.getNumber(b'test', 4)
    (1952805748, b'')
    ```

    Reading in zero bytes leaves the midiStr unchanged:

    ```python
    >>> midi.getNumber(b'test', 0)
    (0, b'test')
    ```

    The method can also take in an integer and return an integer and the remainder part.
    This usage might be deprecated in the future and has already been replaced within
    music21 internal code.

    ```python
    >>> midi.getNumber(516, 1)   # = 2*256 + 4
    (4, 512)
    ```

    Changed in v10: remove Python 2 legacy string as input – use bytes instead.

music21.midi.base.getVariableLengthNumber(*midiBytes: [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")][[source]](../_modules/music21/midi/base.html#getVariableLengthNumber)
:   Given a string or bytes of data, strip off the first character, or all high-byte characters
    terminating with one whose ord() function is < 0x80. Thus, a variable number of bytes
    might be read.

    After finding the appropriate termination,
    return the remaining string.

    This is necessary as DeltaTime times are given with variable size,
    and thus may be of different numbers if characters are used.

    ```python
    >>> midi.getVariableLengthNumber(b'A-u')
    (65, b'-u')
    >>> midi.getVariableLengthNumber(b'-u')
    (45, b'u')
    >>> midi.getVariableLengthNumber(b'u')
    (117, b'')
    ```

    ```python
    >>> midi.getVariableLengthNumber(b'test')
    (116, b'est')
    >>> midi.getVariableLengthNumber(b'E@-E')
    (69, b'@-E')
    >>> midi.getVariableLengthNumber(b'@-E')
    (64, b'-E')
    >>> midi.getVariableLengthNumber(b'-E')
    (45, b'E')
    >>> midi.getVariableLengthNumber(b'E')
    (69, b'')
    ```

    Test that variable length characters work:

    ```python
    >>> midi.getVariableLengthNumber(b'\xff\x7f')
    (16383, b'')
    >>> midi.getVariableLengthNumber('中xy'.encode('utf-8'))
    (210638584, b'y')
    ```

    If no low-byte character is encoded, raises an IndexError

    ```python
    >>> midi.getVariableLengthNumber('中国'.encode('utf-8'))
    Traceback (most recent call last):
    IndexError: index out of range
    ```

    Up to v9.7, this method could also take a string as input and return a string. This usage is
    now removed.

music21.midi.base.putNumber(*num: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *length: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")[[source]](../_modules/music21/midi/base.html#putNumber)
:   Put a single number as a hex number at the end of a bytes object length bytes long.

    ```python
    >>> midi.putNumber(3, 4)
    b'\x00\x00\x00\x03'
    >>> midi.putNumber(0, 1)
    b'\x00'
    ```

    ```python
    >>> midi.putNumber(258, 2)
    b'\x01\x02'
    ```

    If the number is larger than the length currently only the least significant
    bytes are returned. This behavior may change in the near future to raise an
    exception instead.

    ```python
    >>> midi.putNumber(258, 1)
    b'\x02'
    ```

music21.midi.base.putNumbersAsList(*numList: [Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*) → [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")[[source]](../_modules/music21/midi/base.html#putNumbersAsList)
:   Translate a list of numbers (0-255) into bytes.
    Used for encoding data messages where each byte encodes a different discrete value.

    ```python
    >>> midi.putNumbersAsList([0, 0, 0, 3])
    b'\x00\x00\x00\x03'
    ```

    For positive numbers this method behaves the same as bytes(numList) and that
    method should be used if you are sure all numbers are positive.

    ```python
    >>> bytes([0, 0, 0, 3])
    b'\x00\x00\x00\x03'
    ```

    If a number is < 0 then it wraps around from the top. This is used in places
    like MIDI key signatures where flats are represented by 256 - flats.

    ```python
    >>> midi.putNumbersAsList([0, 0, 0, -3])
    b'\x00\x00\x00\xfd'
    >>> midi.putNumbersAsList([0, 0, 0, -1])
    b'\x00\x00\x00\xff'
    ```

    The behavior with negative numbers is different from bytes(numList)

    List can be of any length

    ```python
    >>> midi.putNumbersAsList([1, 16, 255])
    b'\x01\x10\xff'
    ```

    Any number > 255 (or less than -255) raises an exception:

    ```python
    >>> midi.putNumbersAsList([256])
    Traceback (most recent call last):
    music21.midi.base.MidiException: Cannot place a number > 255 in a list: 256
    ```

music21.midi.base.putVariableLengthNumber(*x: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")[[source]](../_modules/music21/midi/base.html#putVariableLengthNumber)
:   Turn an integer number into the smallest bytes object that can hold it for MIDI

    Numbers < 128 are encoded as single bytes and are the same as bytes([x])

    ```python
    >>> midi.putVariableLengthNumber(4)
    b'\x04'
    >>> midi.putVariableLengthNumber(127)
    b'\x7f'
    >>> bytes([127])
    b'\x7f'
    >>> midi.putVariableLengthNumber(0)
    b'\x00'
    ```

    Numbers > 7bit but < 16384 need two characters,
    with the first character set as 0x80 + n // 128
    and the second character set as n % 128:

    ```python
    >>> midi.putVariableLengthNumber(128)
    b'\x81\x00'
    >>> midi.putVariableLengthNumber(129)
    b'\x81\x01'
    >>> midi.putVariableLengthNumber(255)
    b'\x81\x7f'
    ```

    This differs from the 8-bit representation of
    bytes([x]):

    ```python
    >>> bytes([128])
    b'\x80'
    >>> bytes([255])
    b'\xff'
    ```

    This method can also deal with numbers > 255, which bytes cannot.

    ```python
    >>> midi.putVariableLengthNumber(256)
    b'\x82\x00'
    >>> bytes([256])
    Traceback (most recent call last):
    ValueError: bytes must be in range(0, 256)
    ```

    It also differs from the normal way of representing 256 in Python bytes:

    ```python
    >>> bytes([1, 0])
    b'\x01\x00'
    ```

    Here are MIDI representation of other numbers that are too large to fit in 8 bits
    but stored in two bytes in MIDI.

    ```python
    >>> midi.putVariableLengthNumber(1024)
    b'\x88\x00'
    ```

    Notice that the least significant byte is second.

    ```python
    >>> midi.putVariableLengthNumber(8192)
    b'\xc0\x00'
    >>> midi.putVariableLengthNumber(8193)
    b'\xc0\x01'
    ```

    This is the maximum normal MIDI number that can be stored in 2 bytes.

    ```python
    >>> midi.putVariableLengthNumber(16383)
    b'\xff\x7f'
    ```

    Numbers >= 16384 are not used in 2-byte classic MIDI,
    but this routine continues the basic principle from above:

    ```python
    >>> midi.putVariableLengthNumber(16384)
    b'\x81\x80\x00'
    >>> midi.putVariableLengthNumber(16384 + 128)
    b'\x81\x81\x00'
    >>> midi.putVariableLengthNumber(16384 * 2)
    b'\x82\x80\x00'
    >>> midi.putVariableLengthNumber(16384 ** 2)
    b'\x81\x80\x80\x80\x00'
    ```

    Negative numbers raise MidiException

    ```python
    >>> midi.putVariableLengthNumber(-1)
    Traceback (most recent call last):
    music21.midi.base.MidiException: cannot putVariableLengthNumber() when number is negative: -1
    ```
