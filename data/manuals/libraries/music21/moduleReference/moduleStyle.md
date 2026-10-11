Source: https://music21.org/music21docs/moduleReference/moduleStyle.html

# music21.style

The style module represents information about the style of a Note, Accidental,
etc. such that precise positioning information, layout, size, etc. can be specified.

## BeamStyle

class music21.style.BeamStyle[[source]](../_modules/music21/style.html#BeamStyle)
:   Style for beams

[`BeamStyle`](#music21.style.BeamStyle "music21.style.BeamStyle") bases

* [`Style`](#music21.style.Style "music21.style.Style")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`BeamStyle`](#music21.style.BeamStyle "music21.style.BeamStyle") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`BeamStyle`](#music21.style.BeamStyle "music21.style.BeamStyle") read/write properties

Read/write properties inherited from [`Style`](#music21.style.Style "music21.style.Style"):

|  |  |  |
| --- | --- | --- |
| * [`absoluteY`](#music21.style.Style.absoluteY "music21.style.Style.absoluteY") | * [`enclosure`](#music21.style.Style.enclosure "music21.style.Style.enclosure") |  |

[`BeamStyle`](#music21.style.BeamStyle "music21.style.BeamStyle") instance variables

Instance variables inherited from [`Style`](#music21.style.Style "music21.style.Style"):

|  |  |  |
| --- | --- | --- |
| * [`hideObjectOnPrint`](#music21.style.Style.hideObjectOnPrint "music21.style.Style.hideObjectOnPrint") | * [`units`](#music21.style.Style.units "music21.style.Style.units") |  |

## BezierStyle

class music21.style.BezierStyle[[source]](../_modules/music21/style.html#BezierStyle)
:   From the MusicXML Definition.

[`BezierStyle`](#music21.style.BezierStyle "music21.style.BezierStyle") bases

* [`Style`](#music21.style.Style "music21.style.Style")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`BezierStyle`](#music21.style.BezierStyle "music21.style.BezierStyle") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`BezierStyle`](#music21.style.BezierStyle "music21.style.BezierStyle") read/write properties

Read/write properties inherited from [`Style`](#music21.style.Style "music21.style.Style"):

|  |  |  |
| --- | --- | --- |
| * [`absoluteY`](#music21.style.Style.absoluteY "music21.style.Style.absoluteY") | * [`enclosure`](#music21.style.Style.enclosure "music21.style.Style.enclosure") |  |

[`BezierStyle`](#music21.style.BezierStyle "music21.style.BezierStyle") instance variables

Instance variables inherited from [`Style`](#music21.style.Style "music21.style.Style"):

|  |  |  |
| --- | --- | --- |
| * [`hideObjectOnPrint`](#music21.style.Style.hideObjectOnPrint "music21.style.Style.hideObjectOnPrint") | * [`units`](#music21.style.Style.units "music21.style.Style.units") |  |

## Enclosure

class music21.style.Enclosure(*\*values*)[[source]](../_modules/music21/style.html#Enclosure)

[`Enclosure`](#music21.style.Enclosure "music21.style.Enclosure") bases

* [`StrEnum`](moduleCommonEnums.html#music21.common.enums.StrEnum "music21.common.enums.StrEnum")

## LineStyle

class music21.style.LineStyle[[source]](../_modules/music21/style.html#LineStyle)
:   from the MusicXML Definition

    Defines lineShape (‘straight’, ‘curved’ or None)
    lineType (‘solid’, ‘dashed’, ‘dotted’, ‘wavy’ or None)
    dashLength (in tenths)
    spaceLength (in tenths)

[`LineStyle`](#music21.style.LineStyle "music21.style.LineStyle") bases

* [`Style`](#music21.style.Style "music21.style.Style")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LineStyle`](#music21.style.LineStyle "music21.style.LineStyle") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LineStyle`](#music21.style.LineStyle "music21.style.LineStyle") read/write properties

Read/write properties inherited from [`Style`](#music21.style.Style "music21.style.Style"):

|  |  |  |
| --- | --- | --- |
| * [`absoluteY`](#music21.style.Style.absoluteY "music21.style.Style.absoluteY") | * [`enclosure`](#music21.style.Style.enclosure "music21.style.Style.enclosure") |  |

[`LineStyle`](#music21.style.LineStyle "music21.style.LineStyle") instance variables

Instance variables inherited from [`Style`](#music21.style.Style "music21.style.Style"):

|  |  |  |
| --- | --- | --- |
| * [`hideObjectOnPrint`](#music21.style.Style.hideObjectOnPrint "music21.style.Style.hideObjectOnPrint") | * [`units`](#music21.style.Style.units "music21.style.Style.units") |  |

## NoteStyle

class music21.style.NoteStyle[[source]](../_modules/music21/style.html#NoteStyle)
:   A Style object that also includes stem and accidental style information.

    Beam style is stored on the Beams object. Lyric style is stored on the Lyric
    object.

[`NoteStyle`](#music21.style.NoteStyle "music21.style.NoteStyle") bases

* [`Style`](#music21.style.Style "music21.style.Style")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`NoteStyle`](#music21.style.NoteStyle "music21.style.NoteStyle") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`NoteStyle`](#music21.style.NoteStyle "music21.style.NoteStyle") read/write properties

Read/write properties inherited from [`Style`](#music21.style.Style "music21.style.Style"):

|  |  |  |
| --- | --- | --- |
| * [`absoluteY`](#music21.style.Style.absoluteY "music21.style.Style.absoluteY") | * [`enclosure`](#music21.style.Style.enclosure "music21.style.Style.enclosure") |  |

[`NoteStyle`](#music21.style.NoteStyle "music21.style.NoteStyle") instance variables

NoteStyle.accidentalStyle
:   An optional style.Style object describing what the accidental looks like.

    ```python
    >>> n = note.Note()
    >>> n.style.accidentalStyle is None
    True
    ```

    Note that accidentalStyle is not created automatically. Users must
    instantiate a [`Style`](#music21.style.Style "music21.style.Style") object.

    ```python
    >>> n.style.accidentalStyle = style.Style()
    >>> n.style.accidentalStyle.relativeX = -2.0
    ```

    Note: do not use .hideObjectOnPrint in accidentalStyle to hide the
    accidental. Set the displayType on the Accidental itself.

    This object may eventually move to Note.pitch.accidental.style.

NoteStyle.noteSize
:   An optional string representing the size of the note as a type of note.

    Valid values are None (=normal), ‘cue’, ‘grace’, ‘graceCue’, and ‘large’
    (taken from MusicXML, with “graceCue” replacing “grace-cue”).

NoteStyle.stemStyle
:   An optional style.Style object describing what the stem looks like.

    ```python
    >>> n = note.Note()
    >>> n.style.stemStyle is None
    True
    ```

    Note that stemStyle is not created automatically. Users must
    instantiate a [`Style`](#music21.style.Style "music21.style.Style") object.

    ```python
    >>> n.style.stemStyle = style.Style()
    >>> n.style.stemStyle.color = 'red'
    ```

Instance variables inherited from [`Style`](#music21.style.Style "music21.style.Style"):

|  |  |  |
| --- | --- | --- |
| * [`hideObjectOnPrint`](#music21.style.Style.hideObjectOnPrint "music21.style.Style.hideObjectOnPrint") | * [`units`](#music21.style.Style.units "music21.style.Style.units") |  |

## StreamStyle

class music21.style.StreamStyle[[source]](../_modules/music21/style.html#StreamStyle)
:   Includes several elements in the MusicXML <appearance> tag in <defaults>
    along with <music-font> and <word-font>

[`StreamStyle`](#music21.style.StreamStyle "music21.style.StreamStyle") bases

* [`Style`](#music21.style.Style "music21.style.Style")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`StreamStyle`](#music21.style.StreamStyle "music21.style.StreamStyle") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`StreamStyle`](#music21.style.StreamStyle "music21.style.StreamStyle") read/write properties

Read/write properties inherited from [`Style`](#music21.style.Style "music21.style.Style"):

|  |  |  |
| --- | --- | --- |
| * [`absoluteY`](#music21.style.Style.absoluteY "music21.style.Style.absoluteY") | * [`enclosure`](#music21.style.Style.enclosure "music21.style.Style.enclosure") |  |

[`StreamStyle`](#music21.style.StreamStyle "music21.style.StreamStyle") instance variables

Instance variables inherited from [`Style`](#music21.style.Style "music21.style.Style"):

|  |  |  |
| --- | --- | --- |
| * [`hideObjectOnPrint`](#music21.style.Style.hideObjectOnPrint "music21.style.Style.hideObjectOnPrint") | * [`units`](#music21.style.Style.units "music21.style.Style.units") |  |

## Style

class music21.style.Style[[source]](../_modules/music21/style.html#Style)
:   A style object is a lightweight object that
    keeps track of information about the look of an object.

    ```python
    >>> st = style.Style()
    >>> st.units
    'tenths'
    >>> st.absoluteX is None
    True
    ```

    ```python
    >>> st.absoluteX = 20.4
    >>> st.absoluteX
    20.4
    ```

[`Style`](#music21.style.Style "music21.style.Style") bases

* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`Style`](#music21.style.Style "music21.style.Style") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`Style`](#music21.style.Style "music21.style.Style") read/write properties

Style.absoluteY
:   Get or set the vertical position, where 0
    is the top line of the staff and units
    are whatever is defined in .units, generally “tenths”, meaning
    1/10th of a staff space.

    Other legal positions are ‘above’ and ‘below’ which
    are synonyms for 10 and -70 respectively (for 5-line
    staves; other staves are not yet implemented)
    This behavior may change in music21 v8 or after.

    ```python
    >>> te = style.Style()
    >>> te.absoluteY = 10
    >>> te.absoluteY
    10
    ```

    ```python
    >>> te.absoluteY = 'below'
    >>> te.absoluteY
    -70
    ```

    Setting an invalid position raises a TextFormatException

    ```python
    >>> te.absoluteY = 'hello'
    Traceback (most recent call last):
    music21.style.TextFormatException:
        Not a supported absoluteY position: 'hello'
    ```

Style.enclosure
:   Get or set the enclosure as a style.Enclosure enum (or
    None, which means the enclosure is left unspecified).

    Valid names are:

    * “rectangle”/style.Enclosure.RECTANGLE,
    * “square”/style.Enclosure.SQUARE,
    * “oval”/style.Enclosure.OVAL,
    * “circle”/style.Enclosure.CIRCLE,
    * “bracket”/style.Enclosure.BRACKET,
    * “inverted-bracket”/style.Enclosure.INVERTED\_BRACKET (output in musicxml 4 only)
    * “none”/style.Enclosure.NO\_ENCLOSURE
    * None (i.e. enclosure is unspecified)

    or the following other shapes with their ALLCAPS Enclosure equivalents:

    triangle, diamond, pentagon, hexagon, heptagon, octagon,
    nonagon, or decagon.

    ```python
    >>> tst = style.TextStyle()
    >>> tst.enclosure = None
    >>> tst.enclosure = style.Enclosure.RECTANGLE
    >>> tst.enclosure
    <Enclosure.RECTANGLE>
    ```

    Setting as a string is still supported, but is converted to
    an enum.

    ```python
    >>> tst.enclosure = 'octagon'
    >>> tst.enclosure
    <Enclosure.OCTAGON>
    ```

    Setting an invalid enclosure raises a TextFormatException

    ```python
    >>> tst.enclosure = 'parabola'
    Traceback (most recent call last):
    music21.style.TextFormatException:
        Not a supported enclosure: 'parabola'
    ```

[`Style`](#music21.style.Style "music21.style.Style") instance variables

Style.hideObjectOnPrint
:   If set to True, the Music21Object will not print upon output
    (only used in MusicXML output at this point and
    in Lilypond output for notes, chords, and rests).

Style.units
:   What distances are measured in. The default “tenths” is a concept
    borrowed from MusicXML which refers to 1/10th of the distance between
    two staff lines. It is currently also the only supported unit.

## StyleMixin

class music21.style.StyleMixin[[source]](../_modules/music21/style.html#StyleMixin)
:   Mixin for any class that wants to support style and editorial, since several
    non-music21 objects, such as Lyrics and Accidentals will support Style.

    Not used by Music21Objects because of the added trouble in copying etc. so
    there is code duplication with base.Music21Object

[`StyleMixin`](#music21.style.StyleMixin "music21.style.StyleMixin") bases

* [`SlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.SlottedObjectMixin "music21.common.objects.SlottedObjectMixin")

[`StyleMixin`](#music21.style.StyleMixin "music21.style.StyleMixin") read-only properties

StyleMixin.hasEditorialInformation
:   Returns True if there is a [`Editorial`](moduleEditorial.html#music21.editorial.Editorial "music21.editorial.Editorial") object
    already associated with this object, False otherwise.

    Calling .style on an object will always create a new
    Style object, so even though a new Style object isn’t too expensive
    to create, this property helps to prevent creating new Styles more than
    necessary.

    ```python
    >>> acc = pitch.Accidental('#')
    >>> acc.hasEditorialInformation
    False
    >>> acc.editorial
    <music21.editorial.Editorial {}>
    >>> acc.hasEditorialInformation
    True
    ```

StyleMixin.hasStyleInformation
:   Returns True if there is a [`Style`](#music21.style.Style "music21.style.Style") object
    already associated with this object, False otherwise.

    Calling .style on an object will always create a new
    Style object, so even though a new Style object isn’t too expensive
    to create, this property helps to prevent creating new Styles more than
    necessary.

    ```python
    >>> lObj = note.Lyric('hello')
    >>> lObj.hasStyleInformation
    False
    >>> lObj.style
    <music21.style.TextStylePlacement object at 0x10b0a2080>
    >>> lObj.hasStyleInformation
    True
    ```

[`StyleMixin`](#music21.style.StyleMixin "music21.style.StyleMixin") read/write properties

StyleMixin.editorial
:   a [`Editorial`](moduleEditorial.html#music21.editorial.Editorial "music21.editorial.Editorial") object that stores editorial information
    (comments, footnotes, harmonic information, ficta).

    Created automatically as needed:

    ```python
    >>> acc = pitch.Accidental()
    >>> acc.editorial
    <music21.editorial.Editorial {}>
    >>> acc.editorial.ficta = pitch.Accidental('sharp')
    >>> acc.editorial.ficta
    <music21.pitch.Accidental sharp>
    >>> acc.editorial
    <music21.editorial.Editorial {'ficta': <music21.pitch.Accidental sharp>}>
    ```

StyleMixin.style
:   Returns (or Creates and then Returns) the Style object
    associated with this object, or sets a new
    style object. Different classes might use
    different Style objects because they might have different
    style needs (such as text formatting or bezier positioning)

    Eventually will also query the groups to see if they have
    any styles associated with them.

    ```python
    >>> acc = pitch.Accidental()
    >>> st = acc.style
    >>> st
    <music21.style.TextStyle object at 0x10ba96208>
    >>> st.absoluteX = 20.0
    >>> st.absoluteX
    20.0
    >>> acc.style = style.TextStyle()
    >>> acc.style.absoluteX is None
    True
    ```

## TextStyle

class music21.style.TextStyle[[source]](../_modules/music21/style.html#TextStyle)
:   A Style object that also includes text formatting.

    ```python
    >>> ts = style.TextStyle()
    >>> ts.classes
    ('TextStyle', 'Style', 'ProtoM21Object', 'object')
    ```

[`TextStyle`](#music21.style.TextStyle "music21.style.TextStyle") bases

* [`Style`](#music21.style.Style "music21.style.Style")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`TextStyle`](#music21.style.TextStyle "music21.style.TextStyle") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`TextStyle`](#music21.style.TextStyle "music21.style.TextStyle") read/write properties

TextStyle.alignHorizontal
:   Get or set the horizontal alignment. Valid values are left, right, center,
    or None

    ```python
    >>> te = style.TextStyle()
    >>> te.alignHorizontal = 'right'
    >>> te.alignHorizontal
    'right'
    ```

    Invalid horizontal aligns raise a TextFormatException:

    ```python
    >>> te.alignHorizontal = 'hello'
    Traceback (most recent call last):
    music21.style.TextFormatException:
        Invalid horizontal align: 'hello'
    ```

TextStyle.alignVertical
:   Get or set the vertical align. Valid values are top, middle, bottom, baseline
    or None

    ```python
    >>> te = style.TextStyle()
    >>> te.alignVertical = 'top'
    >>> te.alignVertical
    'top'
    ```

    Invalid vertical aligns raise a TextFormatException:

    ```python
    >>> te.alignVertical = 'hello'
    Traceback (most recent call last):
    music21.style.TextFormatException:
        Invalid vertical align: 'hello'
    ```

TextStyle.fontFamily
:   Returns a list of font family names associated with
    the style, or sets the font family name list.

    If a single string is passed then it is converted to
    a list.

    ```python
    >>> ts = style.TextStyle()
    >>> ff = ts.fontFamily
    >>> ff
    []
    >>> ff.append('Times')
    >>> ts.fontFamily
    ['Times']
    >>> ts.fontFamily.append('Garamond')
    >>> ts.fontFamily
    ['Times', 'Garamond']
    >>> ts.fontFamily = 'Helvetica, sans-serif'
    >>> ts.fontFamily
    ['Helvetica', 'sans-serif']
    ```

TextStyle.fontSize
:   Get or set the size. Best, an int or float, but also a css font size

    ```python
    >>> tst = style.TextStyle()
    >>> tst.fontSize = 20
    >>> tst.fontSize
    20
    ```

TextStyle.fontStyle
:   Get or set the style, as normal, italic, bold, and bolditalic.
    None is currently an acceptable value which should be “normal”.

    ```python
    >>> tst = style.TextStyle()
    >>> tst.fontStyle = 'bold'
    >>> tst.fontStyle
    'bold'
    ```

    Invalid values raise a TextFormatException

    ```python
    >>> tst.fontStyle = 'hello'
    Traceback (most recent call last):
    music21.style.TextFormatException:
        Not a supported fontStyle: 'hello'
    ```

TextStyle.fontWeight
:   Get or set the weight, as normal, or bold.

    ```python
    >>> tst = style.TextStyle()
    >>> tst.fontWeight = 'bold'
    >>> tst.fontWeight
    'bold'
    ```

TextStyle.justify
:   Get or set the justification. Valid values are left,
    center, right, full (not supported by MusicXML), and None

    ```python
    >>> tst = style.TextStyle()
    >>> tst.justify = 'center'
    >>> tst.justify
    'center'
    ```

    Invalid values raise a TextFormatException

    ```python
    >>> tst.justify = 'hello'
    Traceback (most recent call last):
    music21.style.TextFormatException:
        Not a supported justification: 'hello'
    ```

TextStyle.letterSpacing
:   > Get or set the letter spacing.

    ```python
    >>> tst = style.TextStyle()
    >>> tst.letterSpacing = 20
    >>> tst.letterSpacing
    20.0
    >>> tst.letterSpacing = 'normal'
    ```

Read/write properties inherited from [`Style`](#music21.style.Style "music21.style.Style"):

|  |  |  |
| --- | --- | --- |
| * [`absoluteY`](#music21.style.Style.absoluteY "music21.style.Style.absoluteY") | * [`enclosure`](#music21.style.Style.enclosure "music21.style.Style.enclosure") |  |

[`TextStyle`](#music21.style.TextStyle "music21.style.TextStyle") instance variables

Instance variables inherited from [`Style`](#music21.style.Style "music21.style.Style"):

|  |  |  |
| --- | --- | --- |
| * [`hideObjectOnPrint`](#music21.style.Style.hideObjectOnPrint "music21.style.Style.hideObjectOnPrint") | * [`units`](#music21.style.Style.units "music21.style.Style.units") |  |

## TextStylePlacement

class music21.style.TextStylePlacement[[source]](../_modules/music21/style.html#TextStylePlacement)
:   TextStyle plus a placement attribute

[`TextStylePlacement`](#music21.style.TextStylePlacement "music21.style.TextStylePlacement") bases

* [`TextStyle`](#music21.style.TextStyle "music21.style.TextStyle")
* [`Style`](#music21.style.Style "music21.style.Style")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`TextStylePlacement`](#music21.style.TextStylePlacement "music21.style.TextStylePlacement") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`TextStylePlacement`](#music21.style.TextStylePlacement "music21.style.TextStylePlacement") read/write properties

Read/write properties inherited from [`TextStyle`](#music21.style.TextStyle "music21.style.TextStyle"):

|  |  |  |
| --- | --- | --- |
| * [`alignHorizontal`](#music21.style.TextStyle.alignHorizontal "music21.style.TextStyle.alignHorizontal") * [`alignVertical`](#music21.style.TextStyle.alignVertical "music21.style.TextStyle.alignVertical") * [`fontFamily`](#music21.style.TextStyle.fontFamily "music21.style.TextStyle.fontFamily") | * [`fontSize`](#music21.style.TextStyle.fontSize "music21.style.TextStyle.fontSize") * [`fontStyle`](#music21.style.TextStyle.fontStyle "music21.style.TextStyle.fontStyle") * [`fontWeight`](#music21.style.TextStyle.fontWeight "music21.style.TextStyle.fontWeight") | * [`justify`](#music21.style.TextStyle.justify "music21.style.TextStyle.justify") * [`letterSpacing`](#music21.style.TextStyle.letterSpacing "music21.style.TextStyle.letterSpacing") |

Read/write properties inherited from [`Style`](#music21.style.Style "music21.style.Style"):

|  |  |  |
| --- | --- | --- |
| * [`absoluteY`](#music21.style.Style.absoluteY "music21.style.Style.absoluteY") | * [`enclosure`](#music21.style.Style.enclosure "music21.style.Style.enclosure") |  |

[`TextStylePlacement`](#music21.style.TextStylePlacement "music21.style.TextStylePlacement") instance variables

Instance variables inherited from [`Style`](#music21.style.Style "music21.style.Style"):

|  |  |  |
| --- | --- | --- |
| * [`hideObjectOnPrint`](#music21.style.Style.hideObjectOnPrint "music21.style.Style.hideObjectOnPrint") | * [`units`](#music21.style.Style.units "music21.style.Style.units") |  |
