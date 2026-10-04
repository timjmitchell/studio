Source: https://music21.org/music21docs/moduleReference/moduleMidiRealtime.html

# music21.midi.realtime

Objects for realtime playback of Music21 Streams as MIDI.

From an idea of Joe “Codeswell”:

<https://joecodeswell.wordpress.com/2012/06/13/how-to-produce-python-controlled-audio-output-from-music-made-with-music21>

<https://stackoverflow.com/questions/10983462/how-can-i-produce-real-time-audio-output-from-music-made-with-music21>

Requires pygame 2 (or 1.9) install with: pip3 install pygame

## StreamPlayer

class music21.midi.realtime.StreamPlayer(*streamIn: [Stream](moduleStreamBase.html#music21.stream.base.Stream "music21.stream.base.Stream")*, *reinitMixer: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *mixerFreq: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 44100*, *mixerBitSize: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = -16*, *mixerChannels: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 2*, *mixerBuffer: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 1024*)[[source]](../_modules/music21/midi/realtime.html#StreamPlayer)
:   Create a player for a stream that plays its midi version in realtime using pygame.

    Set up a detuned piano (where each key has a random but
    consistent detuning from 30 cents flat to sharp)
    and play a Bach Chorale on it in real time.

    ```python
    >>> import random
    >>> keyDetune = []
    >>> for i in range(127):
    ...    keyDetune.append(random.randint(-30, 30))
    ```

    ```python
    >>> b = corpus.parse('bwv66.6')
    >>> for n in b.flatten().notes:
    ...    n.pitch.microtone = keyDetune[n.pitch.midi]
    >>> sp = midi.realtime.StreamPlayer(b)
    >>> sp.play()
    ```

    The stream is stored (unaltered) in StreamPlayer.streamIn, and can be changed any time the
    midi file is not playing.

    A number of mixer controls can be passed in with keywords:

    * mixerFreq (default 44100 – CD quality)
    * mixerBitSize (default -16 (=unsigned 16bit) –
      :   really, are you going to do 24bit audio with Python?? :-) )
    * mixerChannels (default 2 = stereo)
    * mixerBuffer (default 1024 = number of samples)

[`StreamPlayer`](#music21.midi.realtime.StreamPlayer "music21.midi.realtime.StreamPlayer") methods

StreamPlayer.getStringOrBytesIOFile()[[source]](../_modules/music21/midi/realtime.html#StreamPlayer.getStringOrBytesIOFile)

StreamPlayer.play(*busyFunction=None*, *busyArgs=None*, *endFunction=None*, *endArgs=None*, *busyWaitMilliseconds=50*, *\**, *playForMilliseconds=inf*, *blocked=True*)[[source]](../_modules/music21/midi/realtime.html#StreamPlayer.play)
:   busyFunction is a function that is called with busyArgs when the music is busy every
    busyWaitMilliseconds.

    endFunction is a function that is called with endArgs when the music finishes playing.

    playForMilliseconds is the amount of time in milliseconds after which
    the playback will be automatically stopped.

    If blocked is False, the method will finish before ending the stream, allowing
    you to completely control whether to stop it. Ignore every other arguments

StreamPlayer.playStringIOFile(*stringIOFile*, *busyFunction=None*, *busyArgs=None*, *endFunction=None*, *endArgs=None*, *busyWaitMilliseconds=50*, *\**, *playForMilliseconds=inf*, *blocked=True*)[[source]](../_modules/music21/midi/realtime.html#StreamPlayer.playStringIOFile)
:   busyFunction is a function that is called with busyArgs when the music is busy every
    busyWaitMilliseconds.

    endFunction is a function that is called with endArgs when the music finishes playing.

    playForMilliseconds is the amount of time in milliseconds after which the
    playback will be automatically stopped.

    If blocked is False, the method will finish before ending the stream, allowing you to
    completely control whether to stop it. Ignore every other arguments but for stringIOFile

StreamPlayer.stop()[[source]](../_modules/music21/midi/realtime.html#StreamPlayer.stop)
