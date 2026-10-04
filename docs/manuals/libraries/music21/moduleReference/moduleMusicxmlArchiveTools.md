Source: https://music21.org/music21docs/moduleReference/moduleMusicxmlArchiveTools.html

# music21.musicxml.archiveTools

Tools for compressing and decompressing musicxml files.

## Functions

music21.musicxml.archiveTools.compressAllXMLFiles(*\**, *deleteOriginal=False*)[[source]](../_modules/music21/musicxml/archiveTools.html#compressAllXMLFiles)
:   Takes all filenames in corpus.paths and runs
    [`music21.musicxml.archiveTools.compressXML()`](#music21.musicxml.archiveTools.compressXML "music21.musicxml.archiveTools.compressXML") on each. If the musicXML files are
    compressed, the originals are deleted from the system.

music21.musicxml.archiveTools.compressXML(*filename: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")*, *\**, *deleteOriginal=False*, *silent=False*, *strictMxlCheck=True*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/musicxml/archiveTools.html#compressXML)
:   Takes a filename, and if the filename corresponds to a musicXML file with
    an .musicxml or .xml extension, creates a corresponding compressed .mxl file in the same
    directory.

    If deleteOriginal is set to True, the original musicXML file is deleted
    from the system.

    If strictMxlCheck is False then any suffix will do.

    Returns bool if successful.

music21.musicxml.archiveTools.uncompressMXL(*filename: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")*, *\**, *deleteOriginal=False*, *silent=False*, *strictMxlCheck=True*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/musicxml/archiveTools.html#uncompressMXL)
:   Takes a filename, and if the filename corresponds to a compressed musicXML
    file with an .mxl extension, creates a corresponding uncompressed .musicxml file
    in the same directory.

    If deleteOriginal is set to True, the original compressed musicXML file is
    deleted from the system.

    If strictMxlCheck is False then any type of file will attempt to be extracted.

    Returns bool if successful.
