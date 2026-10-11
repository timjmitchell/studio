Source: https://music21.org/music21docs/moduleReference/moduleAudioSearchTranscriber.html

# music21.audioSearch.transcriber

## Functions

music21.audioSearch.transcriber.monophonicStreamFromFile(*fileName*, *useScale=None*)[[source]](../_modules/music21/audioSearch/transcriber.html#monophonicStreamFromFile)
:   Reads in a .wav file and returns a stream representing the transcribed, monophonic audio.

    fileName should be the complete path to a file on the disk.

    A different scale than the chromatic scale can be specified by setting useScale.
    See [music21.scale](moduleScale.html#modulescale) for a list of allowable scales. (or a custom one can be given).
    Microtonal scales are totally accepted, as are retuned scales where A != 440hz.

    We demonstrate with an audio file beginning with an ascending scale.

    ```python
    >>> waveFile = 'test_audio.wav'
    >>> p = audioSearch.transcriber.monophonicStreamFromFile(waveFile)
    >>> p
    <music21.stream.Part ...>
    >>> p.show('text')
    {0.0} <music21.note.Note C>
    {0.25} <music21.note.Note C>
    {0.75} <music21.note.Note D>
    {1.75} <music21.note.Note E>
    {2.75} <music21.note.Note F>
    {4.25} <music21.note.Note G>
    {5.25} <music21.note.Note A>
    {6.25} <music21.note.Note B>
    {7.25} <music21.note.Note C>
    ...
    ```

music21.audioSearch.transcriber.runTranscribe(*show=True*, *plot=True*, *useMic=True*, *seconds=20.0*, *useScale=None*, *saveFile=True*)[[source]](../_modules/music21/audioSearch/transcriber.html#runTranscribe)
:   runs all the methods to record from audio for seconds length (default 10.0)
    and transcribe the resulting melody returning a music21.Score object

    if show is True, show the stream.

    if plot is True, then a Tk graph of the frequencies will be displayed.

    if useMic is True then use the microphone. If False it will load the file of saveFile
    or the default temp file to run transcriptions from.

    a different scale than the chromatic scale can be specified by setting useScale.
    See [music21.scale](moduleScale.html#modulescale) for a list of allowable scales. (or a custom one can be given).
    Microtonal scales are totally accepted, as are retuned scales where A != 440hz.

    if saveFile is False, then the recorded audio is saved to disk. If
    set to True then environLocal.getRootTempDir() / ‘ex.wav’ is
    used as the filename. If set to anything else then it will use that as the
    filename.
