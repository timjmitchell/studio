Source: https://music21.org/music21docs/moduleReference/moduleMusedataTranslate.html

# music21.musedata.translate

**N.B. in Dec. 2014 MuseData access was removed from music21 because the rights conflicted with
access computationally from music21. This module is retained for anyone who has such access,
however it is completely untested now and errors cannot and will not be fixed.**

Functions for translating music21 objects and
`MuseDataHandler` instances. Mostly,
these functions are for advanced, low level usage. For basic importing of MuseData
files from a file or URL to a `Stream`, use the music21
converter module’s [`parse()`](moduleConverter.html#music21.converter.parse "music21.converter.parse") function.

## Functions

music21.musedata.translate.museDataWorkToStreamScore(*museDataWork*, *inputM21=None*)[[source]](../_modules/music21/musedata/translate.html#museDataWorkToStreamScore)
:   Given an museDataWork object, build into a multi-part
    `Score` with metadata.

    This assumes that this MuseDataHandler defines a single work
    (with 1 or fewer reference numbers).

    if the optional parameter inputM21 is given a music21 Stream subclass,
    it will use that object
    as the outermost object. However, inner parts will always be
    made `Part` objects.

music21.musedata.translate.musedataPartToStreamPart(*museDataPart*, *inputM21=None*)[[source]](../_modules/music21/musedata/translate.html#musedataPartToStreamPart)
:   Translate a musedata part to a `Part`.
