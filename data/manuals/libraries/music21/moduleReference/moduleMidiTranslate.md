Source: https://music21.org/music21docs/moduleReference/moduleMidiTranslate.html

# music21.midi.translate

Module to translate MIDI data to music21 Streams and vice versa. Note that quantization of
notes takes place in the `quantize()` method not here.

## TimedNoteEvent

class music21.midi.translate.TimedNoteEvent(*onTime*, *offTime*, *event*)[[source]](../_modules/music21/midi/translate.html#TimedNoteEvent)

## Functions

music21.midi.translate.streamToMidiFile(*inputM21: [Stream](moduleStreamBase.html#music21.stream.base.Stream "music21.stream.base.Stream")*, *\**, *addStartDelay: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *acceptableChannelList: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *encoding: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = 'utf-8'*) → [MidiFile](moduleMidiBase.html#music21.midi.base.MidiFile "music21.midi.base.MidiFile")[[source]](../_modules/music21/midi/translate.html#streamToMidiFile)
:   Converts a Stream hierarchy into a `MidiFile` object.

    ```python
    >>> s = stream.Stream()
    >>> n = note.Note('g#')
    >>> n.quarterLength = 0.5
    >>> s.repeatAppend(n, 4)
    >>> mf = midi.translate.streamToMidiFile(s)
    >>> mf.tracks[0].index  # Track 0: conductor track
    0
    >>> len(mf.tracks[1].events)  # Track 1: music track
    22
    ```

    From here, you can call mf.writestr() to get the actual file info.

    ```python
    >>> sc = scale.PhrygianScale('g')
    >>> s = stream.Stream()
    >>> x=[s.append(note.Note(sc.pitchFromDegree(i % 11), quarterLength=0.25)) for i in range(60)]
    >>> mf = midi.translate.streamToMidiFile(s)
    >>> mf.open('/Volumes/disc/_scratch/midi.mid', 'wb')
    >>> mf.write()
    >>> mf.close()
    ```

    See [`channelInstrumentData()`](#music21.midi.translate.channelInstrumentData "music21.midi.translate.channelInstrumentData") for documentation on acceptableChannelList.

music21.midi.translate.midiFileToStream(*mf: [MidiFile](moduleMidiBase.html#music21.midi.base.MidiFile "music21.midi.base.MidiFile")*, *\**, *inputM21=None*, *quantizePost=True*, *encoding: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = 'utf-8'*, *\*\*keywords*)[[source]](../_modules/music21/midi/translate.html#midiFileToStream)
:   Note: this is NOT the normal way to read a MIDI file. The best way is generally:

    > score = converter.parse(‘path/to/file.mid’)

    Convert a `MidiFile` object to a
    `Stream` object.

    The inputM21 object can specify an existing Stream (or Stream subclass) to fill.

    Keywords to control quantization:
    quantizePost controls whether to quantize the output. (Default: True)
    quarterLengthDivisors allows for overriding the default quantization units
    in defaults.quantizationQuarterLengthDivisors. (Default: (4, 3)).

    ```python
    >>> import os
    >>> fp = common.getSourceFilePath() / 'midi' / 'testPrimitive' / 'test05.mid'
    >>> mf = midi.MidiFile()
    >>> mf.open(fp)
    >>> mf.read()
    >>> mf.close()
    >>> len(mf.tracks)
    1
    >>> s = midi.translate.midiFileToStream(mf)
    >>> s
    <music21.stream.Score ...>
    >>> len(s.flatten().notesAndRests)
    14
    ```

    * Changed in v8: inputM21 and quantizePost are keyword only.

music21.midi.translate.assignPacketsToChannels(*packets*, *channelByInstrument=None*, *channelsDynamic=None*, *initTrackIdToChannelMap=None*)[[source]](../_modules/music21/midi/translate.html#assignPacketsToChannels)
:   Given a list of packets, assign each to a channel.

    Do each track one at time, based on the track id.

    Shift to different channels if a pitch bend is necessary.

    Keep track of which channels are available.
    Need to insert a program change in the empty channel
    too, based on last instrument.

    Insert pitch bend messages as well,
    one for start of event, one for end of event.

    packets is a list of packets.
    channelByInstrument should be a dictionary.
    channelsDynamic should be a list.
    initTrackIdToChannelMap should be a dictionary.

music21.midi.translate.channelInstrumentData(*s: [Stream](moduleStreamBase.html#music21.stream.base.Stream "music21.stream.base.Stream")*, *acceptableChannelList: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")], [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]][[source]](../_modules/music21/midi/translate.html#channelInstrumentData)
:   Read through Stream s and finding instruments in it, return a 2-tuple,
    the first a dictionary mapping MIDI program numbers to channel numbers,
    and the second, a list of unassigned channels that can be used for dynamic
    allocation. One channel is always left unassigned for dynamic allocation.
    If the number of needed channels exceeds the number of available ones,
    any further MIDI program numbers are assigned to channel 1.

    Substreams without notes or rests (e.g. representing a conductor track)
    will not consume a channel.

    Only necessarily works if [`prepareStreamForMidi()`](#music21.midi.translate.prepareStreamForMidi "music21.midi.translate.prepareStreamForMidi")
    has been run before calling this routine.

    An instrument’s .midiChannel attribute is observed.
    None is the default .midiChannel for all instruments except
    [`UnpitchedPercussion`](moduleInstrument.html#music21.instrument.UnpitchedPercussion "music21.instrument.UnpitchedPercussion")
    subclasses. Put another way, the priority is:

    * Instrument instance .midiChannel (set by user or imported from MIDI)
    * UnpitchedPercussion subclasses receive MIDI Channel 10 (9 in music21)
    * The channel mappings produced by reading from acceptableChannelList,
      or the default range 1-16. (More precisely, 1-15, since one dynamic channel
      is always reserved.)

    Warning

    The attribute .midiChannel on [`Instrument`](moduleInstrument.html#music21.instrument.Instrument "music21.instrument.Instrument")
    is 0-indexed, but .channel on `MidiEvent` is 1-indexed,
    as are all references to channels in this function.

music21.midi.translate.chordToMidiEvents(*inputM21: [ChordBase](moduleChord.html#music21.chord.ChordBase "music21.chord.ChordBase")*, *\**, *includeDeltaTime: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *channel: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 1*, *encoding: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = 'utf-8'*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[DeltaTime](moduleMidiBase.html#music21.midi.base.DeltaTime "music21.midi.base.DeltaTime") | [MidiEvent](moduleMidiBase.html#music21.midi.base.MidiEvent "music21.midi.base.MidiEvent")][[source]](../_modules/music21/midi/translate.html#chordToMidiEvents)
:   Translates a [`Chord`](moduleChord.html#music21.chord.Chord "music21.chord.Chord") object to a
    list of base.DeltaTime and base.MidiEvents objects.

    The channel can be specified, otherwise channel 1 is assumed.

    See noteToMidiEvents above for more details.

    ```python
    >>> c = chord.Chord(['c3', 'g#4', 'b5'])
    >>> c.volume = volume.Volume(velocity=90)
    >>> c.volume.velocityIsRelative = False
    >>> eventList = midi.translate.chordToMidiEvents(c)
    >>> eventList
    [<music21.midi.DeltaTime (empty) track=None>,
     <music21.midi.MidiEvent NOTE_ON, track=None, channel=1, pitch=48, velocity=90>,
     <music21.midi.DeltaTime (empty) track=None>,
     <music21.midi.MidiEvent NOTE_ON, track=None, channel=1, pitch=68, velocity=90>,
     <music21.midi.DeltaTime (empty) track=None>,
     <music21.midi.MidiEvent NOTE_ON, track=None, channel=1, pitch=83, velocity=90>,
     <music21.midi.DeltaTime t=10080, track=None>,
     <music21.midi.MidiEvent NOTE_OFF, track=None, channel=1, pitch=48, velocity=0>,
     <music21.midi.DeltaTime (empty) track=None>,
     <music21.midi.MidiEvent NOTE_OFF, track=None, channel=1, pitch=68, velocity=0>,
     <music21.midi.DeltaTime (empty) track=None>,
     <music21.midi.MidiEvent NOTE_OFF, track=None, channel=1, pitch=83, velocity=0>]
    ```

    * Changed in v7: made keyword-only.
    * Changed in v8: added support for [`PercussionChord`](modulePercussion.html#music21.percussion.PercussionChord "music21.percussion.PercussionChord")

music21.midi.translate.conductorStream(*s: [Stream](moduleStreamBase.html#music21.stream.base.Stream "music21.stream.base.Stream")*) → [Part](moduleStreamBase.html#music21.stream.base.Part "music21.stream.base.Part")[[source]](../_modules/music21/midi/translate.html#conductorStream)
:   Strip the given stream of any events that belong in a conductor track
    rather than in a music track, and returns a `Part`
    containing just those events, without duplicates, suitable for being a
    Part to turn into a conductor track.

    Sets a default MetronomeMark of 120 if no MetronomeMarks are present
    and a TimeSignature of 4/4 if not present.

    Ensures that the conductor track always sorts before other parts.

    Here we purposely use nested generic streams instead of Scores, Parts, etc.
    to show that this still works. But you should use Score, Part, Measure instead.

    ```python
    >>> s = stream.Stream(id='scoreLike')
    >>> p = stream.Stream(id='partLike')
    >>> p.priority = -2
    >>> m = stream.Stream(id='measureLike')
    >>> m.append(tempo.MetronomeMark(100))
    >>> m.append(note.Note('C4'))
    >>> p.append(m)
    >>> s.insert(0, p)
    >>> conductor = midi.translate.conductorStream(s)
    >>> conductor.priority
    -3
    ```

    The MetronomeMark is moved and a default TimeSignature is added:

    ```python
    >>> conductor.show('text')
    {0.0} <music21.instrument.Conductor 'Conductor'>
    {0.0} <music21.tempo.MetronomeMark Quarter=100>
    {0.0} <music21.meter.TimeSignature 4/4>
    ```

    The original stream still has the note:

    ```python
    >>> s.show('text')
    {0.0} <music21.stream.Stream partLike>
        {0.0} <music21.stream.Stream measureLike>
            {0.0} <music21.note.Note C>
    ```

music21.midi.translate.durationToMidiTicks(*d: [Duration](moduleDuration.html#music21.duration.Duration "music21.duration.Duration")*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](../_modules/music21/midi/translate.html#durationToMidiTicks)
:   Converts a [`Duration`](moduleDuration.html#music21.duration.Duration "music21.duration.Duration") object to midi ticks.

    Depends on *defaults.ticksPerQuarter*, Returns an int.
    Does not use defaults.ticksAtStart

    ```python
    >>> n = note.Note()
    >>> n.duration.type = 'half'
    >>> midi.translate.durationToMidiTicks(n.duration)
    20160
    ```

    ```python
    >>> d = duration.Duration('quarter')
    >>> dReference = midi.translate.ticksToDuration(10080, inputM21DurationObject=d)
    >>> dReference is d
    True
    >>> d.type
    'quarter'
    >>> d.type = '16th'
    >>> d.quarterLength
    0.25
    >>> midi.translate.durationToMidiTicks(d)
    2520
    ```

music21.midi.translate.elementToMidiEventList(*el: [base.Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")*, *encoding: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = 'utf-8'*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[MidiEvent](moduleMidiBase.html#music21.midi.base.MidiEvent "music21.midi.base.MidiEvent") | [DeltaTime](moduleMidiBase.html#music21.midi.base.DeltaTime "music21.midi.base.DeltaTime")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/midi/translate.html#elementToMidiEventList)
:   Return a list of MidiEvents (or None) from a Music21Object,
    assuming that dynamics have already been applied, etc.
    Does not include DeltaTime objects.

    Channel (1-indexed) is set to the default, 1.
    Track is not set.

    ```python
    >>> n = note.Note('C4')
    >>> midiEvents = midi.translate.elementToMidiEventList(n)
    >>> midiEvents
    [<music21.midi.MidiEvent NOTE_ON, track=None, channel=1, pitch=60, velocity=90>,
     <music21.midi.MidiEvent NOTE_OFF, track=None, channel=1, pitch=60, velocity=0>]
    ```

music21.midi.translate.filterPacketsByTrackId(*packetsSrc: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")]]*, *trackIdFilter: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")]][[source]](../_modules/music21/midi/translate.html#filterPacketsByTrackId)
:   Given a list of Packet dictionaries, return a list of
    only those whose trackId matches the filter.

    ```python
    >>> packets = [
    ...     {'trackId': 1, 'name': 'hello'},
    ...     {'trackId': 2, 'name': 'bye'},
    ...     {'trackId': 1, 'name': 'hi'},
    ... ]
    >>> midi.translate.filterPacketsByTrackId(packets, 1)
    [{'trackId': 1, 'name': 'hello'},
     {'trackId': 1, 'name': 'hi'}]
    >>> midi.translate.filterPacketsByTrackId(packets, 2)
    [{'trackId': 2, 'name': 'bye'}]
    ```

    If no trackIdFilter is passed, the original list is returned:

    ```python
    >>> midi.translate.filterPacketsByTrackId(packets) is packets
    True
    ```

music21.midi.translate.getEndEvents(*midiTrack: [MidiTrack](moduleMidiBase.html#music21.midi.base.MidiTrack "music21.midi.base.MidiTrack") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[MidiEvent](moduleMidiBase.html#music21.midi.base.MidiEvent "music21.midi.base.MidiEvent") | [DeltaTime](moduleMidiBase.html#music21.midi.base.DeltaTime "music21.midi.base.DeltaTime")][[source]](../_modules/music21/midi/translate.html#getEndEvents)
:   Returns a list of midi.MidiEvent objects found at the end of a track.

    ```python
    >>> midi.translate.getEndEvents()
    [<music21.midi.DeltaTime t=10080, track=None>,
     <music21.midi.MidiEvent END_OF_TRACK, track=None, data=b''>]
    ```

    Changed in v10 - getEndEvents does not take a channel

music21.midi.translate.getMetaEvents(*events: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [MidiEvent](moduleMidiBase.html#music21.midi.base.MidiEvent "music21.midi.base.MidiEvent")]]*, *\**, *encoding: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = 'utf-8'*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [base.Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")]][[source]](../_modules/music21/midi/translate.html#getMetaEvents)
:   Translate MidiEvents whose type is a MetaEvent into Music21Objects.

    Note: this does not translate MetaEvent.LYRIC, since that becomes a
    bare string.

    New in 9.7: add encoding

music21.midi.translate.getNotesFromEvents(*timedEvents: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [MidiEvent](moduleMidiBase.html#music21.midi.base.MidiEvent "music21.midi.base.MidiEvent")]]*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[TimedNoteEvent](#music21.midi.translate.TimedNoteEvent "music21.midi.translate.TimedNoteEvent")][[source]](../_modules/music21/midi/translate.html#getNotesFromEvents)
:   Takes in a list of tuples of (tickTime, MidiEvent) and returns a list of
    TimedNoteEvent objects which contain the note on time, the note off time,
    and the MidiEvent of the note on. (The note off MidiEvent is not included)

    If timedEvents is sorted in non-decreasing order of tickTime, then the
    output here will also be sorted in non-decreasing order of note on time.

    Example: here are two pitches, represented as note on and note off events:

    ```python
    >>> CVM = midi.ChannelVoiceMessages
    >>> ev1on = midi.MidiEvent(type=CVM.NOTE_ON)
    >>> ev1on.pitch = 60
    >>> ev2on = midi.MidiEvent(type=CVM.NOTE_ON)
    >>> ev2on.pitch = 62
    >>> ev1off = midi.MidiEvent(type=CVM.NOTE_OFF)
    >>> ev1off.pitch = 60
    >>> ev2off = midi.MidiEvent(type=CVM.NOTE_OFF)
    >>> ev2off.pitch = 62
    ```

    ```python
    >>> events = [(0, ev1on), (1, ev2on), (2, ev2off), (3, ev1off)]
    ```

    ```python
    >>> notes = midi.translate.getNotesFromEvents(events)
    >>> len(notes)
    2
    >>> notes
    [TimedNoteEvent(onTime=0, offTime=3, event=<music21.midi.MidiEvent NOTE_ON...>),
     TimedNoteEvent(onTime=1, offTime=2, event=<music21.midi.MidiEvent NOTE_ON...>)]
    >>> (notes[0].event.pitch, notes[1].event.pitch)
    (60, 62)
    ```

music21.midi.translate.getPacketFromMidiEvent(*trackId: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *midiEvent: [MidiEvent](moduleMidiBase.html#music21.midi.base.MidiEvent "music21.midi.base.MidiEvent")*, *obj: [base.Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *lastInstrument: [instrument.Instrument](moduleInstrument.html#music21.instrument.Instrument "music21.instrument.Instrument") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), t.Any][[source]](../_modules/music21/midi/translate.html#getPacketFromMidiEvent)
:   Pack a dictionary of parameters for each event.
    Packets are used for sorting and configuring all note events.
    Includes offset, any cent shift, the midi event, and the source object.

    Offset and duration values stored here are MIDI ticks, not quarter lengths.

    ```python
    >>> n = note.Note('C4')
    >>> midiEvents = midi.translate.elementToMidiEventList(n)
    >>> getPacket = midi.translate.getPacketFromMidiEvent
    >>> getPacket(trackId=1, offset=0, midiEvent=midiEvents[0], obj=n)
    {'trackId': 1,
     'offset': 0,
     'midiEvent': <music21.midi.MidiEvent NOTE_ON, track=None, channel=1, pitch=60, velocity=90>,
     'obj': <music21.note.Note C>,
     'centShift': None,
     'duration': 10080,
     'lastInstrument': None}
    >>> inst = instrument.Harpsichord()
    >>> getPacket(trackId=1, offset=0, midiEvent=midiEvents[1], obj=n, lastInstrument=inst)
    {'trackId': 1,
     'offset': 0,
     'midiEvent': <music21.midi.MidiEvent NOTE_OFF, track=None, channel=1, pitch=60, velocity=0>,
     'obj': <music21.note.Note C>,
     'centShift': None,
     'duration': 0,
     'lastInstrument': <music21.instrument.Harpsichord 'Harpsichord'>}
    ```

music21.midi.translate.getStartEvents(*midiTrack: [MidiTrack](moduleMidiBase.html#music21.midi.base.MidiTrack "music21.midi.base.MidiTrack") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *channel: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 1*, *instrumentObj: [Instrument](moduleInstrument.html#music21.instrument.Instrument "music21.instrument.Instrument") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\**, *encoding: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = 'utf-8'*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[DeltaTime](moduleMidiBase.html#music21.midi.base.DeltaTime "music21.midi.base.DeltaTime") | [MidiEvent](moduleMidiBase.html#music21.midi.base.MidiEvent "music21.midi.base.MidiEvent")][[source]](../_modules/music21/midi/translate.html#getStartEvents)
:   Returns a list of midi.MidiEvent objects found at the beginning of a track.

    A MidiTrack reference can be provided via the mt parameter.

    ```python
    >>> startEvents = midi.translate.getStartEvents()
    >>> startEvents
    [<music21.midi.DeltaTime (empty) track=None>,
     <music21.midi.MidiEvent SEQUENCE_TRACK_NAME, track=None, data=b''>]
    ```

    (Music21 DeltaTime events get assigned to the given channel, but this is not written out)

    ```python
    >>> startEvents[0].channel
    1
    ```

    ```python
    >>> mt = midi.MidiTrack(3)
    >>> midi.translate.getStartEvents(mt, channel=2, instrumentObj=instrument.Harpsichord())
    [<music21.midi.DeltaTime (empty) track=3>,
     <music21.midi.MidiEvent SEQUENCE_TRACK_NAME, track=3, data=b'Harpsichord'>,
     <music21.midi.DeltaTime (empty) track=3>,
     <music21.midi.MidiEvent PROGRAM_CHANGE, track=3, channel=2, data=6>]
    ```

    Bug fixed in v9.6 – the program change and delta time are written to the given track.

music21.midi.translate.getTimeForEvents(*mt: [MidiTrack](moduleMidiBase.html#music21.midi.base.MidiTrack "music21.midi.base.MidiTrack")*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [MidiEvent](moduleMidiBase.html#music21.midi.base.MidiEvent "music21.midi.base.MidiEvent")]][[source]](../_modules/music21/midi/translate.html#getTimeForEvents)
:   Get a list of tuples of (tickTime, MidiEvent) from the events with time deltas.

music21.midi.translate.insertConductorEvents(*conductorPart: [Part](moduleStreamBase.html#music21.stream.base.Part "music21.stream.base.Part")*, *target: [Part](moduleStreamBase.html#music21.stream.base.Part "music21.stream.base.Part")*, *\**, *isFirst: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*)[[source]](../_modules/music21/midi/translate.html#insertConductorEvents)
:   Insert a deepcopy of any TimeSignature, KeySignature, or MetronomeMark
    found in the conductorPart into the target Part at the same offset.

    Obligatory to do this before making measures. New in v7.

music21.midi.translate.instrumentToMidiEvents(*inputM21: [Instrument](moduleInstrument.html#music21.instrument.Instrument "music21.instrument.Instrument")*, *includeDeltaTime: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *midiTrack: [MidiTrack](moduleMidiBase.html#music21.midi.base.MidiTrack "music21.midi.base.MidiTrack") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *channel: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 1*)[[source]](../_modules/music21/midi/translate.html#instrumentToMidiEvents)
:   Converts a [`Instrument`](moduleInstrument.html#music21.instrument.Instrument "music21.instrument.Instrument") object to a list of MidiEvents

    TODO: DOCS and TESTS

music21.midi.translate.keySignatureToMidiEvents(*ks: [KeySignature](moduleKey.html#music21.key.KeySignature "music21.key.KeySignature")*, *includeDeltaTime=True*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[DeltaTime](moduleMidiBase.html#music21.midi.base.DeltaTime "music21.midi.base.DeltaTime") | [MidiEvent](moduleMidiBase.html#music21.midi.base.MidiEvent "music21.midi.base.MidiEvent")][[source]](../_modules/music21/midi/translate.html#keySignatureToMidiEvents)
:   Convert a single [`Key`](moduleKey.html#music21.key.Key "music21.key.Key") or
    [`KeySignature`](moduleKey.html#music21.key.KeySignature "music21.key.KeySignature") object to
    a two-element list of midi events,
    where the first is an empty DeltaTime (unless includeDeltaTime is False) and the second
    is a KEY\_SIGNATURE `MidiEvent`

    ```python
    >>> ks = key.KeySignature(2)
    >>> ks
    <music21.key.KeySignature of 2 sharps>
    >>> eventList = midi.translate.keySignatureToMidiEvents(ks)
    >>> eventList
    [<music21.midi.DeltaTime (empty) track=None>,
     <music21.midi.MidiEvent KEY_SIGNATURE, track=None, data=b'\x02\x00'>]
    ```

    Note that MIDI Key Signatures are connected to tracks but not to channels.

    MIDI Key Signatures store sharps or flats as the first number, and mode (0 = major
    1 = minor) as the second number.

    Flats are encoded as offsets at 0xff (=1 flat) or below (0xfe = 2 flats … etc.,
    through 0xfb = 5 flats, below).

    ```python
    >>> k = key.Key('b-')
    >>> k
    <music21.key.Key of b- minor>
    >>> eventList = midi.translate.keySignatureToMidiEvents(k, includeDeltaTime=False)
    >>> eventList
    [<music21.midi.MidiEvent KEY_SIGNATURE, track=None, data=b'\xfb\x01'>]
    ```

music21.midi.translate.lyricTimingsFromEvents(*events: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [MidiEvent](moduleMidiBase.html#music21.midi.base.MidiEvent "music21.midi.base.MidiEvent")]]*, *\**, *encoding: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = 'utf-8'*) → [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")][[source]](../_modules/music21/midi/translate.html#lyricTimingsFromEvents)
:   From a list of timed events, that is a tuple of a tick time and a MidiEvent
    Return a dictionary mapping a tick time to a string representing a lyric.

    If more than one lyric is found at a given tick time, the last one found is
    stored.

music21.midi.translate.midiAsciiStringToBinaryString(*midiFormat=1*, *ticksPerQuarterNote=960*, *tracksEventsList=None*) → [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")[[source]](../_modules/music21/midi/translate.html#midiAsciiStringToBinaryString)
:   Convert Ascii midi data to a bytes object (formerly binary midi string).

    tracksEventsList contains a list of tracks which contain also a list of events.

    > asciiMidiEventList = [‘0 90 27 66’, ‘0 90 3e 60’, ‘3840 80 27 00’, ‘0 80 3e 00’]

    The format of one event is : ‘aa bb cc dd’:

    ```python
    aa = delta time to last event (integer)
    bb = Midi event type
    cc = Note number (hex)
    dd = Velocity (integer)
    ```

    Example:

    ```python
    >>> asciiMidiEventList = []
    >>> asciiMidiEventList.append('0 90 31 15')
    >>> midiTrack = []
    >>> midiTrack.append(asciiMidiEventList)
    >>> midiBinaryBytes = midi.translate.midiAsciiStringToBinaryString(tracksEventsList=midiTrack)
    >>> midiBinaryBytes
    b'MThd\x00\x00\x00\x06\x00\x01\x00\x01\x03\xc0MTrk\x00\x00\x00\x04\x00\x901\x0f'
    ```

    Note that the name is from pre-Python 3. There is now in fact nothing called a “binary string”
    it is in fact a bytes object.

music21.midi.translate.midiEventToInstrument(*event: [MidiEvent](moduleMidiBase.html#music21.midi.base.MidiEvent "music21.midi.base.MidiEvent")*, *\**, *encoding: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = 'utf-8'*) → [Instrument](moduleInstrument.html#music21.instrument.Instrument "music21.instrument.Instrument")[[source]](../_modules/music21/midi/translate.html#midiEventToInstrument)
:   Convert a single MIDI event into a music21 Instrument object.

    MIDI Events that can be properly read are PROGRAM\_CHANGE, INSTRUMENT\_NAME
    and SEQUENCE\_TRACK\_NAME

    ```python
    >>> me = midi.MidiEvent(channel=2)
    >>> me.type = midi.ChannelVoiceMessages.PROGRAM_CHANGE
    >>> me.data = 53  # MIDI program 54: Voice Oohs
    >>> midi.translate.midiEventToInstrument(me)
    <music21.instrument.Vocalist 'Voice'>
    ```

    The percussion map will be used if the channel is 10:

    ```python
    >>> me.channel = 10
    >>> instrumentObj = midi.translate.midiEventToInstrument(me)
    >>> instrumentObj
    <music21.instrument.UnpitchedPercussion 'Percussion'>
    >>> instrumentObj.midiChannel  # 0-indexed in music21
    9
    >>> instrumentObj.midiProgram  # 0-indexed in music21
    53
    ```

    Get from instrument name with particular encodings

    ```python
    >>> encoded_flute = 'flöte'.encode('latin-1')
    >>> me = midi.MidiEvent(channel=4)
    >>> me.type = midi.MetaEvents.SEQUENCE_TRACK_NAME
    >>> me.data = encoded_flute
    >>> fl = midi.translate.midiEventToInstrument(me, encoding='latin-1')
    >>> fl
    <music21.instrument.Flute 'flöte'>
    ```

music21.midi.translate.midiEventsToChord(*timedNoteList: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[TimedNoteEvent](#music21.midi.translate.TimedNoteEvent "music21.midi.translate.TimedNoteEvent")]*, *ticksPerQuarter: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 10080*) → [ChordBase](moduleChord.html#music21.chord.ChordBase "music21.chord.ChordBase")[[source]](../_modules/music21/midi/translate.html#midiEventsToChord)
:   Creates a Chord from a list of TimedNoteEvents which
    store the noteOn tick, noteOff tick, and Note-On MidiEvent for each note.

    Timings of all objects except the first (for the first note on)
    and last (for the last note off) are ignored.

    ```python
    >>> mt = midi.MidiTrack(1)
    ```

    ```python
    >>> dt1 = midi.DeltaTime(mt)
    >>> me1 = midi.MidiEvent(mt)
    >>> me1.type = midi.ChannelVoiceMessages.NOTE_ON
    >>> me1.pitch = 45
    >>> me1.velocity = 94
    ```

    Note that only the times of the first NOTE\_ON and last NOTE\_OFF matter, so
    we don’t even bother setting the time of dt3 and dt4.

    ```python
    >>> dt3 = midi.DeltaTime(mt)
    >>> me3 = midi.MidiEvent(mt)
    >>> me3.type = midi.ChannelVoiceMessages.NOTE_OFF
    ```

    The pitches of the NOTE\_OFF events are not checked by this function. They
    are assumed to have been aligned by the previous parser.

    ```python
    >>> me3.pitch = 45
    >>> me3.velocity = 0
    ```

    ```python
    >>> dt2 = midi.DeltaTime(mt)
    >>> me2 = midi.MidiEvent(mt)
    >>> me2.type = midi.ChannelVoiceMessages.NOTE_ON
    >>> me2.pitch = 46
    >>> me2.velocity = 94
    ```

    ```python
    >>> dt4 = midi.DeltaTime(mt)
    >>> dt4.time = 20160
    ```

    ```python
    >>> me4 = midi.MidiEvent(mt)
    >>> me4.type = midi.ChannelVoiceMessages.NOTE_OFF
    >>> me4.pitch = 46
    >>> me4.velocity = 0
    ```

    ```python
    >>> tne1 = midi.translate.TimedNoteEvent(dt1.time, dt3.time, me1)
    >>> tne2 = midi.translate.TimedNoteEvent(dt2.time, dt4.time, me2)
    ```

    ```python
    >>> c = midi.translate.midiEventsToChord([tne1, tne2])
    >>> c
    <music21.chord.Chord A2 B-2>
    >>> c.duration.quarterLength
    2.0
    ```

    If the channel of the last element is set to 10, then a PercussionChord is returned:

    ```python
    >>> me2.channel = 10
    >>> midi.translate.midiEventsToChord([tne1, tne2])
    <music21.percussion.PercussionChord [Tom-Tom Hi-Hat Cymbal]>
    ```

    * Changed in v7: Uses the last DeltaTime in the list to get the end time.
    * Changed in v7.3: Returns a [`PercussionChord`](modulePercussion.html#music21.percussion.PercussionChord "music21.percussion.PercussionChord") if
      any event is on channel 10.
    * Changed in v8: inputM21 is no longer supported. Flat list format is removed.
    * Changed in v9.7: expects a list of TimedNoteEvents

music21.midi.translate.midiEventsToInstrument(*eventList: [MidiEvent](moduleMidiBase.html#music21.midi.base.MidiEvent "music21.midi.base.MidiEvent") | [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [MidiEvent](moduleMidiBase.html#music21.midi.base.MidiEvent "music21.midi.base.MidiEvent")]*, *\**, *encoding: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = 'utf-8'*) → [Instrument](moduleInstrument.html#music21.instrument.Instrument "music21.instrument.Instrument")[[source]](../_modules/music21/midi/translate.html#midiEventsToInstrument)

music21.midi.translate.midiEventsToKey(*eventList*) → [Key](moduleKey.html#music21.key.Key "music21.key.Key")[[source]](../_modules/music21/midi/translate.html#midiEventsToKey)
:   Convert a single MIDI event into a [`KeySignature`](moduleKey.html#music21.key.KeySignature "music21.key.KeySignature") object.

    ```python
    >>> mt = midi.MidiTrack(1)
    >>> me1 = midi.MidiEvent(mt)
    >>> me1.type = midi.MetaEvents.KEY_SIGNATURE
    >>> me1.data = midi.putNumbersAsList([2, 0])  # d major
    >>> ks = midi.translate.midiEventsToKey(me1)
    >>> ks
    <music21.key.Key of D major>
    >>> ks.mode
    'major'
    ```

    ```python
    >>> me2 = midi.MidiEvent(mt)
    >>> me2.type = midi.MetaEvents.KEY_SIGNATURE
    >>> me2.data = midi.putNumbersAsList([-2, 1])  # g minor
    >>> me2.data
    b'\xfe\x01'
    >>> list(me2.data)
    [254, 1]
    >>> ks = midi.translate.midiEventsToKey(me2)
    >>> ks
    <music21.key.Key of g minor>
    >>> ks.sharps
    -2
    >>> ks.mode
    'minor'
    ```

music21.midi.translate.midiEventsToNote(*timedNoteEvent: [TimedNoteEvent](#music21.midi.translate.TimedNoteEvent "music21.midi.translate.TimedNoteEvent")*, *ticksPerQuarter: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 10080*) → [Note](moduleNote.html#music21.note.Note "music21.note.Note") | [Unpitched](moduleNote.html#music21.note.Unpitched "music21.note.Unpitched")[[source]](../_modules/music21/midi/translate.html#midiEventsToNote)
:   Convert a TimedNoteEvent to a music21.note.Note or a music21.note.Unpitched.
    A timed note event is a tuple of (onTime, offTime, MidiEvent) where the
    MidiEvent is the Note On. (The Note Off event is not used).

    This method is called as part of the midiToStream() conversion.

    In this example, we start a NOTE\_ON event at offset 1.0 (at the standard 10080 to quarter)

    ```python
    >>> mt = midi.MidiTrack(1)
    >>> dt1 = midi.DeltaTime(mt)
    >>> dt1.time = 10080
    ```

    ```python
    >>> me1 = midi.MidiEvent(mt)
    >>> me1.type = midi.ChannelVoiceMessages.NOTE_ON
    >>> me1.pitch = 45
    >>> me1.velocity = 94
    ```

    This lasts until we send a NOTE\_OFF event at offset 2.0.

    ```python
    >>> dt2 = midi.DeltaTime(mt)
    >>> dt2.time = 20160
    >>> me2 = midi.MidiEvent(mt)
    >>> me2.type = midi.ChannelVoiceMessages.NOTE_ON
    >>> me2.pitch = 45
    >>> me2.velocity = 0
    ```

    Another system will package dt1, dt2 and me1 into a TimedNoteEvent tuple.
    In this example, me2 is not used.

    ```python
    >>> tne1 = midi.translate.TimedNoteEvent(dt1.time, dt2.time, me1)
    >>> n = midi.translate.midiEventsToNote(tne1)
    >>> n.pitch
    <music21.pitch.Pitch A2>
    >>> n.duration.quarterLength
    1.0
    >>> n.volume.velocity
    94
    ```

    If the channel is 10, an Unpitched element is returned.

    ```python
    >>> me1.channel = 10
    >>> unp = midi.translate.midiEventsToNote(tne1)
    >>> unp
    <music21.note.Unpitched 'Tom-Tom'>
    ```

    Access the storedInstrument:

    ```python
    >>> unp.storedInstrument
    <music21.instrument.TomTom 'Tom-Tom'>
    ```

    And with values that cannot be translated, a generic
    [`UnpitchedPercussion`](moduleInstrument.html#music21.instrument.UnpitchedPercussion "music21.instrument.UnpitchedPercussion") instance is given:

    ```python
    >>> me1.pitch = 1
    >>> unp = midi.translate.midiEventsToNote(tne1)
    >>> unp.storedInstrument
    <music21.instrument.UnpitchedPercussion 'Percussion'>
    ```

    * Changed in v7.3: Returns None if inputM21 is provided. Returns a
      :   [`Unpitched`](moduleNote.html#music21.note.Unpitched "music21.note.Unpitched") instance if the event is on Channel 10.
    * Changed in v8: inputM21 is no longer supported.
      :   The only supported usage now is two tuples.
    * Changed in v9.7: Expects a single TimedNoteEvent

music21.midi.translate.midiEventsToTempo(*eventList*)[[source]](../_modules/music21/midi/translate.html#midiEventsToTempo)
:   Convert a single MIDI event into a music21 Tempo object.

    TODO: Need Tests

music21.midi.translate.midiEventsToTimeSignature(*eventList*)[[source]](../_modules/music21/midi/translate.html#midiEventsToTimeSignature)
:   Convert a single MIDI event into a music21 TimeSignature object.

    ```python
    >>> mt = midi.MidiTrack(1)
    >>> me1 = midi.MidiEvent(mt)
    >>> me1.type = midi.MetaEvents.TIME_SIGNATURE
    >>> me1.data = midi.putNumbersAsList([3, 1, 24, 8])  # 3/2 time
    >>> ts = midi.translate.midiEventsToTimeSignature(me1)
    >>> ts
    <music21.meter.TimeSignature 3/2>
    ```

    ```python
    >>> me2 = midi.MidiEvent(mt)
    >>> me2.type = midi.MetaEvents.TIME_SIGNATURE
    >>> me2.data = midi.putNumbersAsList([3, 4])  # 3/16 time
    >>> ts = midi.translate.midiEventsToTimeSignature(me2)
    >>> ts
    <music21.meter.TimeSignature 3/16>
    ```

music21.midi.translate.midiFilePathToStream(*filePath*, *\**, *inputM21=None*, *encoding: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = 'utf-8'*, *\*\*keywords*)[[source]](../_modules/music21/midi/translate.html#midiFilePathToStream)
:   Used by music21.converter:

    Take in a file path (name of a file on disk) and using midiFileToStream,

    return a `Score` object (or if inputM21 is passed in,
    use that object instead).

    Keywords to control quantization:
    quantizePost controls whether to quantize the output. (Default: True)
    quarterLengthDivisors allows for overriding the default quantization units
    in defaults.quantizationQuarterLengthDivisors. (Default: (4, 3)).

    ```python
    >>> fp = '/Users/test/music21/midi/testPrimitive/test05.mid'
    >>> streamScore = midi.translate.midiFilePathToStream(fp)
    >>> streamScore
    <music21.stream.Score ...>
    ```

    * Changed in v8: inputM21 is keyword only.

music21.midi.translate.midiStringToStream(*strData*, *\*\*keywords*)[[source]](../_modules/music21/midi/translate.html#midiStringToStream)
:   Convert a string of binary midi data to a Music21 stream.Score object.

    Keywords to control quantization:
    quantizePost controls whether to quantize the output. (Default: True)
    quarterLengthDivisors allows for overriding the default quantization units
    in defaults.quantizationQuarterLengthDivisors. (Default: (4, 3)).

    N.B. – this has been somewhat problematic, so use at your own risk.

    ```python
    >>> midiBinStr = (b'MThd\x00\x00\x00\x06\x00\x01\x00\x01\x04\x00'
    ...               + b'MTrk\x00\x00\x00\x16\x00\xff\x03\x00\x00\xe0\x00@\x00'
    ...               + b'\x90CZ\x88\x00\x80C\x00\x88\x00\xff/\x00')
    >>> s = midi.translate.midiStringToStream(midiBinStr)
    >>> s.show('text')
    {0.0} <music21.stream.Part 0x108aa94f0>
        {0.0} <music21.stream.Measure 1 offset=0.0>
            {0.0} <music21.instrument.Instrument ''>
            {0.0} <music21.clef.TrebleClef>
            {0.0} <music21.meter.TimeSignature 4/4>
            {0.0} <music21.note.Note G>
            {1.0} <music21.note.Rest dotted-half>
            {4.0} <music21.bar.Barline type=final>
    ```

music21.midi.translate.midiTrackToStream(*mt*, *\**, *ticksPerQuarter: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 10080*, *quantizePost=True*, *inputM21=None*, *conductorPart: [Part](moduleStreamBase.html#music21.stream.base.Part "music21.stream.base.Part") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *isFirst: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *quarterLengthDivisors: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] = ()*, *encoding: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = 'utf-8'*, *\*\*keywords*) → [Part](moduleStreamBase.html#music21.stream.base.Part "music21.stream.base.Part")[[source]](../_modules/music21/midi/translate.html#midiTrackToStream)
:   Note that quantization takes place in stream.py since it’s useful not just for MIDI.

    ```python
    >>> fp = common.getSourceFilePath() / 'midi' / 'testPrimitive' / 'test05.mid'
    >>> mf = midi.MidiFile()
    >>> mf.open(fp)
    >>> mf.read()
    >>> mf.close()
    >>> mf
    <music21.midi.MidiFile 1 track>
    >>> len(mf.tracks)
    1
    >>> mt = mf.tracks[0]
    >>> mt
    <music21.midi.MidiTrack 0 -- 56 events>
    >>> mt.events
    [<music21.midi.DeltaTime ...>,
     <music21.midi.MidiEvent SEQUENCE_TRACK_NAME...>,
     <music21.midi.DeltaTime ...>,
     <music21.midi.MidiEvent NOTE_ON, track=0, channel=1, pitch=36, velocity=90>,
     ...]
    >>> p = midi.translate.midiTrackToStream(mt, ticksPerQuarter=mf.ticksPerQuarterNote)
    >>> p
    <music21.stream.Part ...>
    >>> len(p.recurse().notesAndRests)
    14
    >>> p.recurse().notes.first().pitch.midi
    36
    >>> p.recurse().notes.first().volume.velocity
    90
    ```

    Note that as of music21 v7, the Part object already has measures made:

    ```python
    >>> p.show('text')
    {0.0} <music21.stream.Measure 1 offset=0.0>
        {0.0} <music21.instrument.Instrument ''>
        {0.0} <music21.clef.TrebleClef>
        {0.0} <music21.meter.TimeSignature 4/4>
        {0.0} <music21.note.Note C>
        {1.0} <music21.note.Rest quarter>
        {2.0} <music21.chord.Chord F3 G#4 C5>
        {3.0} <music21.note.Rest quarter>
    {4.0} <music21.stream.Measure 2 offset=4.0>
        {0.0} <music21.note.Rest eighth>
        {0.5} <music21.note.Note B->
        {1.5} <music21.note.Rest half>
        {3.5} <music21.chord.Chord D2 A4>
    {8.0} <music21.stream.Measure 3 offset=8.0>
        {0.0} <music21.note.Rest eighth>
        {0.5} <music21.chord.Chord C#2 B-3 G#6>
        {1.0} <music21.note.Rest dotted-quarter>
        {2.5} <music21.chord.Chord F#3 A4 C#5>
    {12.0} <music21.stream.Measure 4 offset=12.0>
        {0.0} <music21.chord.Chord F#3 A4 C#5>
        {2.5} <music21.note.Rest dotted-quarter>
        {4.0} <music21.bar.Barline type=final>
    ```

    * Changed in v7: Now makes measures.
    * Changed in v8: all but the first attribute are keyword only.

music21.midi.translate.midiTracksToStreams(*midiTracks: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[MidiTrack](moduleMidiBase.html#music21.midi.base.MidiTrack "music21.midi.base.MidiTrack")]*, *ticksPerQuarter: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 10080*, *quantizePost=True*, *inputM21: [Score](moduleStreamBase.html#music21.stream.base.Score "music21.stream.base.Score") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\**, *encoding: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = 'utf-8'*, *\*\*keywords*) → [Score](moduleStreamBase.html#music21.stream.base.Score "music21.stream.base.Score")[[source]](../_modules/music21/midi/translate.html#midiTracksToStreams)
:   Given a list of midiTracks, populate either a new stream.Score or inputM21
    with a Part for each track.

music21.midi.translate.music21ObjectToMidiFile(*music21Object: [base.Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")*, *\**, *addStartDelay=False*, *encoding: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = 'utf-8'*) → [MidiFile](moduleMidiBase.html#music21.midi.base.MidiFile "music21.midi.base.MidiFile")[[source]](../_modules/music21/midi/translate.html#music21ObjectToMidiFile)
:   Either calls streamToMidiFile on the music21Object or
    puts a copy of that object into a Stream (so as
    not to change activeSites, etc.) and calls streamToMidiFile on
    that object.

music21.midi.translate.noteToMidiEvents(*inputM21: [Note](moduleNote.html#music21.note.Note "music21.note.Note") | [Unpitched](moduleNote.html#music21.note.Unpitched "music21.note.Unpitched")*, *\**, *includeDeltaTime: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *channel: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 1*, *encoding: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = 'utf-8'*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[DeltaTime](moduleMidiBase.html#music21.midi.base.DeltaTime "music21.midi.base.DeltaTime") | [MidiEvent](moduleMidiBase.html#music21.midi.base.MidiEvent "music21.midi.base.MidiEvent")][[source]](../_modules/music21/midi/translate.html#noteToMidiEvents)
:   Translate a music21 Note to a list of four MIDI events –
    the DeltaTime for the start of the note (0), the NOTE\_ON event, the
    DeltaTime to the end of the note, and the NOTE\_OFF event.

    If includeDeltaTime is not True then the DeltaTime events
    aren’t returned, thus only two events are returned.

    The initial deltaTime object is always 0. It will be changed when
    processing Notes from a Stream.

    The channel can be specified, otherwise channel 1 is assumed.

    ```python
    >>> n1 = note.Note('C#4')
    >>> eventList = midi.translate.noteToMidiEvents(n1)
    >>> eventList
    [<music21.midi.DeltaTime (empty) track=None>,
     <music21.midi.MidiEvent NOTE_ON, track=None, channel=1, pitch=61, velocity=90>,
     <music21.midi.DeltaTime t=10080, track=None>,
     <music21.midi.MidiEvent NOTE_OFF, track=None, channel=1, pitch=61, velocity=0>]
    ```

    ```python
    >>> n1.duration.quarterLength = 2.5
    >>> eventList = midi.translate.noteToMidiEvents(n1)
    >>> eventList
    [<music21.midi.DeltaTime (empty) track=None>,
     <music21.midi.MidiEvent NOTE_ON, track=None, channel=1, pitch=61, velocity=90>,
     <music21.midi.DeltaTime t=25200, track=None>,
     <music21.midi.MidiEvent NOTE_OFF, track=None, channel=1, pitch=61, velocity=0>]
    ```

    Omitting DeltaTimes:

    ```python
    >>> eventList2 = midi.translate.noteToMidiEvents(n1, includeDeltaTime=False, channel=9)
    >>> eventList2
    [<music21.midi.MidiEvent NOTE_ON, track=None, channel=9, pitch=61, velocity=90>,
     <music21.midi.MidiEvent NOTE_OFF, track=None, channel=9, pitch=61, velocity=0>]
    ```

    * Changed in v7: made keyword-only.
    * Changed in v8: added support for [`Unpitched`](moduleNote.html#music21.note.Unpitched "music21.note.Unpitched")

music21.midi.translate.offsetToMidiTicks(*o: OffsetQLIn*, *addStartDelay: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](../_modules/music21/midi/translate.html#offsetToMidiTicks)
:   Helper function to convert a music21 offset value to MIDI ticks,
    depends on *defaults.ticksPerQuarter* and *defaults.ticksAtStart*.

    Returns an int.

    ```python
    >>> defaults.ticksPerQuarter
    10080
    >>> defaults.ticksAtStart
    10080
    ```

    ```python
    >>> midi.translate.offsetToMidiTicks(0)
    0
    >>> midi.translate.offsetToMidiTicks(0, addStartDelay=True)
    10080
    ```

    ```python
    >>> midi.translate.offsetToMidiTicks(1)
    10080
    ```

    ```python
    >>> midi.translate.offsetToMidiTicks(20.5)
    206640
    ```

music21.midi.translate.packetStorageFromSubstreamList(*substreamList: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Part](moduleStreamBase.html#music21.stream.base.Part "music21.stream.base.Part")]*, *\**, *addStartDelay=False*, *encoding: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = 'utf-8'*) → [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")]][[source]](../_modules/music21/midi/translate.html#packetStorageFromSubstreamList)
:   Make a dictionary of raw packets and the initial instrument for each
    subStream.

    If the first Part in the list of parts is empty then a new
    [`Conductor`](moduleInstrument.html#music21.instrument.Conductor "music21.instrument.Conductor") object will be given as the instrument.

    ```python
    >>> s = stream.Score()
    >>> p = stream.Part()
    >>> m = stream.Measure(number=1)
    >>> m.append(tempo.MetronomeMark(100))
    >>> m.append(instrument.Oboe())
    >>> m.append(note.Note('C4', type='whole'))  # MIDI 60
    >>> p.append(m)
    >>> s.append(p)
    >>> sOut = midi.translate.prepareStreamForMidi(s)
    >>> partList = list(sOut.parts)
    >>> packetStorage = midi.translate.packetStorageFromSubstreamList(partList)
    >>> list(sorted(packetStorage.keys()))
    [0, 1]
    >>> list(sorted(packetStorage[0].keys()))
    ['initInstrument', 'rawPackets']
    ```

    ```python
    >>> from pprint import pprint
    >>> pprint(packetStorage)
    {0: {'initInstrument': <music21.instrument.Conductor 'Conductor'>,
         'rawPackets': [{'centShift': None,
                         'duration': 0,
                         'lastInstrument': <music21.instrument.Conductor 'Conductor'>,
                         'midiEvent': <music21.midi.MidiEvent SET_TEMPO, ...>,
                         'obj': <music21.tempo.MetronomeMark Quarter=100>,
                         'offset': 0,
                         'trackId': 0},
                        {'centShift': None,
                         'duration': 0,
                         'lastInstrument': <music21.instrument.Conductor 'Conductor'>,
                         'midiEvent': <music21.midi.MidiEvent TIME_SIGNATURE, ...>,
                         'obj': <music21.meter.TimeSignature 4/4>,
                         'offset': 0,
                         'trackId': 0}]},
     1: {'initInstrument': <music21.instrument.Oboe 'Oboe'>,
         'rawPackets': [{'centShift': None,
                         'duration': 0,
                         'lastInstrument': <music21.instrument.Oboe 'Oboe'>,
                         'midiEvent': <music21.midi.MidiEvent PROGRAM_CHANGE,
                                          track=None, channel=1, data=68>,
                         'obj': <music21.instrument.Oboe 'Oboe'>,
                         'offset': 0,
                         'trackId': 1},
                        {'centShift': None,
                         'duration': 40320,
                         'lastInstrument': <music21.instrument.Oboe 'Oboe'>,
                         'midiEvent': <music21.midi.MidiEvent NOTE_ON,
                                          track=None, channel=1, pitch=60, velocity=90>,
                         'obj': <music21.note.Note C>,
                         'offset': 0,
                         'trackId': 1},
                        {'centShift': None,
                         'duration': 0,
                         'lastInstrument': <music21.instrument.Oboe 'Oboe'>,
                         'midiEvent': <music21.midi.MidiEvent NOTE_OFF,
                                           track=None, channel=1, pitch=60, velocity=0>,
                         'obj': <music21.note.Note C>,
                         'offset': 40320,
                         'trackId': 1}]}}
    ```

music21.midi.translate.packetsToDeltaSeparatedEvents(*packets: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")]]*, *midiTrack: [MidiTrack](moduleMidiBase.html#music21.midi.base.MidiTrack "music21.midi.base.MidiTrack")*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[MidiEvent](moduleMidiBase.html#music21.midi.base.MidiEvent "music21.midi.base.MidiEvent") | [DeltaTime](moduleMidiBase.html#music21.midi.base.DeltaTime "music21.midi.base.DeltaTime")][[source]](../_modules/music21/midi/translate.html#packetsToDeltaSeparatedEvents)
:   Given a list of packets (which already contain MidiEvent objects)
    return a list of those Events with proper delta times between them.

    At this stage MIDI event objects have been created.
    The key process here is finding the adjacent time
    between events and adding DeltaTime events before each MIDI event.

    Delta time channel values are derived from the previous midi event.

music21.midi.translate.packetsToMidiTrack(*packets*, *trackId=1*, *channel=1*, *instrumentObj=None*)[[source]](../_modules/music21/midi/translate.html#packetsToMidiTrack)
:   Given packets already allocated with channel
    and/or instrument assignments, place these in a MidiTrack.

    Note that all packets can be sent; only those with
    matching trackIds will be collected into the resulting track

    The channel defines the channel that startEvents and endEvents
    will be assigned to

    Use streamToPackets to convert the Stream to the packets

music21.midi.translate.prepareStreamForMidi(*s*) → [Stream](moduleStreamBase.html#music21.stream.base.Stream "music21.stream.base.Stream")[[source]](../_modules/music21/midi/translate.html#prepareStreamForMidi)
:   Given a score, prepare it for MIDI processing, and return a new Stream:

    1. Expand repeats.

    2. Make changes that will let us later create a conductor (tempo) track
    by placing MetronomeMark, TimeSignature, and KeySignature
    objects into a new Part, and remove them from other parts.

    3. Ensure that the resulting Stream always has part-like substreams.

    Note: will make a deepcopy() of the stream.

    ```python
    >>> s = stream.Score()
    >>> p = stream.Part()
    >>> m = stream.Measure(number=1)
    >>> m.append(tempo.MetronomeMark(100))
    >>> m.append(note.Note('C4', type='whole'))  # MIDI 60
    >>> p.append(m)
    >>> s.append(p)
    >>> sOut = midi.translate.prepareStreamForMidi(s)
    >>> sOut.show('text')
    {0.0} <music21.stream.Part 0x10b0439a0>
        {0.0} <music21.tempo.MetronomeMark Quarter=100>
        {0.0} <music21.meter.TimeSignature 4/4>
    {0.0} <music21.stream.Part 0x10b043c10>
        {0.0} <music21.stream.Measure 1 offset=0.0>
            {0.0} <music21.note.Note C>
    ```

music21.midi.translate.streamHierarchyToMidiTracks(*inputM21*, *\**, *acceptableChannelList=None*, *addStartDelay=False*, *encoding='utf-8'*)[[source]](../_modules/music21/midi/translate.html#streamHierarchyToMidiTracks)
:   Given a Stream, Score, Part, etc., that may have substreams (i.e.,
    a hierarchy), return a list of `MidiTrack` objects.

    acceptableChannelList is a list of MIDI Channel numbers that can be used or None.
    If None, then 1-9, 11-16 are used (10 being reserved for percussion).

    In addition, if an [`Instrument`](moduleInstrument.html#music21.instrument.Instrument "music21.instrument.Instrument") object in the stream
    has a .midiChannel that is not None, that channel is observed, and
    also treated as reserved. Only subclasses of [`UnpitchedPercussion`](moduleInstrument.html#music21.instrument.UnpitchedPercussion "music21.instrument.UnpitchedPercussion")
    have a default .midiChannel, but users may manipulate this.
    See [`channelInstrumentData()`](#music21.midi.translate.channelInstrumentData "music21.midi.translate.channelInstrumentData") for more, and for documentation on acceptableChannelList.

    Called by streamToMidiFile()

    The process:

    1. makes a deepcopy of the Stream (Developer TODO: could this
       be done with a shallow copy? Not if ties are stripped and volume realized.)
    2. we make a list of all instruments that are being used in the piece.

    * Changed in v6: acceptableChannelList is keyword only. addStartDelay is new.
    * Changed in v6.5: Track 0 (tempo/conductor track) always exported.

music21.midi.translate.streamToPackets(*s: [Stream](moduleStreamBase.html#music21.stream.base.Stream "music21.stream.base.Stream")*, *trackId: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 1*, *addStartDelay: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *encoding: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = 'utf-8'*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")]][[source]](../_modules/music21/midi/translate.html#streamToPackets)
:   Convert a flattened, sorted Stream to MIDI Packets.

    This assumes that the Stream has already been flattened,
    ties have been stripped, and instruments,
    if necessary, have been added.

    In converting from a Stream to MIDI, this is called first,
    resulting in a collection of packets by offset.
    Then, getPacketFromMidiEvent is called.

music21.midi.translate.tempoToMidiEvents(*tempoIndication: [MetronomeMark](moduleTempo.html#music21.tempo.MetronomeMark "music21.tempo.MetronomeMark")*, *includeDeltaTime=True*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[DeltaTime](moduleMidiBase.html#music21.midi.base.DeltaTime "music21.midi.base.DeltaTime") | [MidiEvent](moduleMidiBase.html#music21.midi.base.MidiEvent "music21.midi.base.MidiEvent")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/midi/translate.html#tempoToMidiEvents)
:   Given any TempoIndication, convert it to list of `MidiEvent`
    objects that signifies a MIDI tempo indication.

    ```python
    >>> mm = tempo.MetronomeMark(number=90)
    >>> events = midi.translate.tempoToMidiEvents(mm)
    >>> events
    [<music21.midi.DeltaTime ...>, <music21.midi.MidiEvent SET_TEMPO...>]
    >>> len(events)
    2
    ```

    ```python
    >>> events[0]
    <music21.midi.DeltaTime (empty) track=None>
    ```

    ```python
    >>> evt1 = events[1]
    >>> evt1
    <music21.midi.MidiEvent SET_TEMPO, track=None, data=b'\n,+'>
    >>> evt1.data
    b'\n,+'
    >>> microSecondsPerQuarterNote = midi.getNumber(evt1.data, len(evt1.data))[0]
    >>> microSecondsPerQuarterNote
    666667
    ```

    ```python
    >>> round(60_000_000 / microSecondsPerQuarterNote, 1)
    90.0
    ```

    If includeDeltaTime is False then the DeltaTime object is omitted:

    ```python
    >>> midi.translate.tempoToMidiEvents(mm, includeDeltaTime=False)
    [<music21.midi.MidiEvent SET_TEMPO...>]
    ```

    Test round-trip. Note that for pure tempo numbers, by default
    we create a text name if there’s an appropriate one:

    ```python
    >>> midi.translate.midiEventsToTempo(events)
    <music21.tempo.MetronomeMark maestoso Quarter=90>
    ```

    None is returned if the MetronomeMark lacks a number, which can
    happen with metric modulation marks.

    ```python
    >>> midi.translate.tempoToMidiEvents(tempo.MetronomeMark(number=None)) is None
    True
    ```

    Sounding numbers also translate even if number is None

    ```python
    >>> mm = tempo.MetronomeMark(numberSounding=80)
    >>> midi.translate.tempoToMidiEvents(mm)
    [<music21.midi.DeltaTime ...>, <music21.midi.MidiEvent SET_TEMPO...>]
    ```

music21.midi.translate.ticksToDuration(*ticks: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *ticksPerQuarter: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 10080*, *inputM21DurationObject: [Duration](moduleDuration.html#music21.duration.Duration "music21.duration.Duration") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [Duration](moduleDuration.html#music21.duration.Duration "music21.duration.Duration")[[source]](../_modules/music21/midi/translate.html#ticksToDuration)
:   Converts a number of MIDI Ticks to a music21 duration.Duration() object.

    Optional parameters include ticksPerQuarter – in case something other
    than the default.ticksPerQuarter (10080) is used in this file. And
    it can take a [`Duration`](moduleDuration.html#music21.duration.Duration "music21.duration.Duration") object to modify, specified
    as *inputM21DurationObject*

    ```python
    >>> d = midi.translate.ticksToDuration(10080)
    >>> d
    <music21.duration.Duration 1.0>
    >>> d.type
    'quarter'
    ```

    ```python
    >>> n = note.Note()
    >>> midi.translate.ticksToDuration(30240, inputM21DurationObject=n.duration)
    <music21.duration.Duration 3.0>
    >>> n.duration.type
    'half'
    >>> n.duration.dots
    1
    ```

    More complex rhythms can also be set automatically:

    ```python
    >>> d2 = duration.Duration()
    >>> d2reference = midi.translate.ticksToDuration(23625, inputM21DurationObject=d2)
    >>> d2 is d2reference
    True
    >>> d2.quarterLength
    2.34375
    >>> d2.type
    'complex'
    >>> d2.components
    (DurationTuple(type='half', dots=0, quarterLength=2.0),
     DurationTuple(type='16th', dots=0, quarterLength=0.25),
     DurationTuple(type='64th', dots=1, quarterLength=0.09375))
    >>> d2.components[2].type
    '64th'
    >>> d2.components[2].dots
    1
    ```

music21.midi.translate.timeSignatureToMidiEvents(*ts*, *includeDeltaTime=True*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[DeltaTime](moduleMidiBase.html#music21.midi.base.DeltaTime "music21.midi.base.DeltaTime") | [MidiEvent](moduleMidiBase.html#music21.midi.base.MidiEvent "music21.midi.base.MidiEvent")][[source]](../_modules/music21/midi/translate.html#timeSignatureToMidiEvents)
:   Translate a `TimeSignature` to a pair of events: a DeltaTime and
    a MidiEvent TIME\_SIGNATURE.

    Returns a two-element list unless there is an error.

    ```python
    >>> ts = meter.TimeSignature('5/4')
    >>> eventList = midi.translate.timeSignatureToMidiEvents(ts)
    >>> eventList[0]
    <music21.midi.DeltaTime (empty) track=None>
    >>> eventList[1]
    <music21.midi.MidiEvent TIME_SIGNATURE, track=None, data=b'\x05\x02\x18\x08'>
    ```

    Note that time signatures with numerators above 255 cannot be stored in MIDI.
    (A feature?) They will not be stored and an empty list will be returned.
    A warning will be issued.

    ```python
    >>> ts = meter.TimeSignature('267/32')  # found on music21 list
    >>> out = midi.translate.timeSignatureToMidiEvents(ts)
    >>> out
    []
    ```

music21.midi.translate.updatePacketStorageWithChannelInfo(*packetStorage: [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")]]*, *channelByInstrument: [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/midi/translate.html#updatePacketStorageWithChannelInfo)
:   Take the packetStorage dictionary and using information
    from ‘initInstrument’ and channelByInstrument, add an ‘initChannel’ key to each
    packetStorage bundle and to each rawPacket in the bundle[‘rawPackets’]
