Source: https://music21.org/music21docs/moduleReference/moduleGraphUtilities.html

# music21.graph.utilities

Functions for finding external modules, converting colors to Matplotlib colors, etc.

## ExtendedModules

class music21.graph.utilities.ExtendedModules(*matplotlib*, *Axes3D*, *collections*, *patches*, *plt*)

## Functions

music21.graph.utilities.accidentalLabelToUnicode(*label*)[[source]](../_modules/music21/graph/utilities.html#accidentalLabelToUnicode)
:   Changes a label possibly containing a modifier such as “-” or “#” into
    a unicode string.

    ```python
    >>> graph.utilities.accidentalLabelToUnicode('B-4')
    'B♭4'
    ```

    Since matplotlib’s default fonts do not support double sharps or double flats,
    etc. these are converted as best we can.

    ```python
    >>> graph.utilities.accidentalLabelToUnicode('B--4')
    'B♭♭4'
    ```

music21.graph.utilities.getColor(*color*)[[source]](../_modules/music21/graph/utilities.html#getColor)
:   Convert any specification of a color to a hexadecimal color used by matplotlib.

    ```python
    >>> graph.utilities.getColor('red')
    '#ff0000'
    >>> graph.utilities.getColor('r')
    '#ff0000'
    >>> graph.utilities.getColor('Steel Blue')
    '#4682b4'
    >>> graph.utilities.getColor('#f50')
    '#ff5500'
    >>> graph.utilities.getColor([0.5, 0.5, 0.5])
    '#808080'
    >>> graph.utilities.getColor(0.8)
    '#cccccc'
    >>> graph.utilities.getColor([0.8])
    '#cccccc'
    >>> graph.utilities.getColor([255, 255, 255])
    '#ffffff'
    ```

    Invalid colors raise GraphExceptions:

    ```python
    >>> graph.utilities.getColor('l')
    Traceback (most recent call last):
    music21.graph.utilities.GraphException: invalid color abbreviation: l
    ```

    ```python
    >>> graph.utilities.getColor('chalkywhitebutsortofgreenish')
    Traceback (most recent call last):
    music21.graph.utilities.GraphException: invalid color name: chalkywhitebutsortofgreenish
    ```

    ```python
    >>> graph.utilities.getColor(True)
    Traceback (most recent call last):
    music21.graph.utilities.GraphException: invalid color specification: True
    ```

music21.graph.utilities.getExtendedModules()[[source]](../_modules/music21/graph/utilities.html#getExtendedModules)
:   this is done inside a function, so that the slow import of matplotlib is not done
    in `from music21 import *` unless it’s actually needed.

    Returns a namedtuple: (matplotlib, Axes3D, collections, patches, plt)
