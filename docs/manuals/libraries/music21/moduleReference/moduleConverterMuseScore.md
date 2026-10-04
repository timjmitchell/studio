Source: https://music21.org/music21docs/moduleReference/moduleConverterMuseScore.html

# music21.converter.museScore

This module contains tools for using MuseScore to do conversions
from music21. It was formerly mostly in subConverters.

## Functions

music21.converter.museScore.findLastPNGPath(*inputFp: [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")*) → [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")[[source]](../_modules/music21/converter/museScore.html#findLastPNGPath)
:   Find the last numbered file path corresponding to the provided NUMBERED file path
    ending in “.png”. Raises an exception if no file can be found.

    For instance, if there was a file named abc-01.png it might find abc-22.png.

music21.converter.museScore.findNumberedPNGPath(*inputFp: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")*) → [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")[[source]](../_modules/music21/converter/museScore.html#findNumberedPNGPath)
:   Find the first numbered file path corresponding to the provided unnumbered file path
    ending in “.png”. Raises an exception if no file can be found.

    Renamed in v7. Returns a pathlib.Path

music21.converter.museScore.findPNGRange(*firstFp: [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")*, *lastFp: [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][[source]](../_modules/music21/converter/museScore.html#findPNGRange)
:   Return a 2-tuple of the maximum PNG number and the number of digits used to
    specify the PNG (for MuseScore generated PNGs, for use in the widget)

music21.converter.museScore.runThroughMuseScore(*fp*, *subformats=()*, *\**, *dpi: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *trimEdges: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *leaveMargin: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*, *\*\*keywords*) → [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")[[source]](../_modules/music21/converter/museScore.html#runThroughMuseScore)
:   Take the output of the conversion process and run it through MuseScore to convert it
    to a png.

    * dpi: specifies the dpi of the output file. If None, then the default is used.
    * trimEdges: if True (default) the image is trimmed to the edges of the music.
    * leaveMargin: if trimEdges is True, then this number of pixels is left around the
      trimmed image.
