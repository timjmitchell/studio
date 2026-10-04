Source: https://music21.org/music21docs/moduleReference/moduleAudioSearchRecording.html

# music21.audioSearch.recording

modules for audio searching that directly record from the microphone.

Requires PyAudio and portaudio to be installed (<https://portaudio.com/download.html>)

Windows users will get pyaudio and portaudio with pip install pyaudio

macOS users should have Homebrew installed and run brew install portaudio
before running pip install pyaudio

There is no official support for Linux/BSD etc. in music21, but package managers like apt
tend to have libraries like portaudio19 and python3-pyaudio.

## Functions

music21.audioSearch.recording.samplesFromRecording(*seconds=10.0*, *storeFile=True*, *recordFormat=None*, *recordChannels=1*, *recordSampleRate=44100*, *recordChunkLength=1024*)[[source]](../_modules/music21/audioSearch/recording.html#samplesFromRecording)
:   records seconds length of sound in the given format (default Wave)
    and optionally stores it to disk using the filename of storeFile

    Returns a list of samples.
