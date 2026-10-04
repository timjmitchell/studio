Source: https://music21.org/music21docs/moduleReference/moduleFiguredBassNotation.html

# music21.figuredBass.notation

## Notation

class music21.figuredBass.notation.Notation(*notationColumn: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*)[[source]](../_modules/music21/figuredBass/notation.html#Notation)
:   Breaks apart and stores the information in a figured bass notation
    column, which is a string of figures, each associated with a number
    and an optional modifier. The figures are delimited using commas.
    Examples include ‘7,5,#3’, ‘6,4’, and ‘6,4+,2’.

    Valid modifiers include those accepted by [`Accidental`](modulePitch.html#music21.pitch.Accidental "music21.pitch.Accidental"),
    such as #, -, and n, as well as those which can correspond to one, such as +,
    /, and b.

    Note

    If a figure has a modifier but no number, the number is
    assumed to be 3.

    Notation also translates many forms of shorthand notation into longhand. It understands
    all the forms of shorthand notation listed below. This is true even if a number is accompanied
    by a modifier, or if a stand-alone modifier implies a 3.

    * None, ‘’ or ‘5’ -> ‘5,3’
    * ‘6’ -> ‘6,3’
    * ‘7’ -> ‘7,5,3’
    * ‘6,5’ -> ‘6,5,3’
    * ‘4,3’ -> ‘6,4,3’
    * ‘4,2’ or ‘2’ -> ‘6,4,2’
    * ‘9’ -> ‘9,7,5,3’
    * ‘11’ -> ‘11,9,7,5,3’
    * ‘13’ -> ‘13,11,9,7,5,3’
    * ‘\_’ -> treated as an extender

    Figures are saved in order from left to right as found in the notationColumn.

    ```python
    >>> from music21.figuredBass import notation
    >>> n1 = notation.Notation('4+,2')
    >>> n1
    <music21.figuredBass.notation.Notation 4+,2>
    ```

    ```python
    >>> n1.notationColumn
    '4+,2'
    >>> n1.figureStrings
    ['4+', '2']
    >>> n1.origNumbers
    (4, 2)
    >>> n1.origModStrings
    ('+', None)
    >>> n1.numbers
    (6, 4, 2)
    >>> n1.modifierStrings
    (None, '+', None)
    >>> n1.modifiers
    (<music21.figuredBass.notation.Modifier None None>,
     <music21.figuredBass.notation.Modifier + sharp>,
     <music21.figuredBass.notation.Modifier None None>)
    >>> n1.figures[0]
    <music21.figuredBass.notation.Figure 6 <Modifier None None>>
    >>> n1.figures[1]
    <music21.figuredBass.notation.Figure 4 <Modifier + sharp>>
    >>> n1.figures[2]
    <music21.figuredBass.notation.Figure 2 <Modifier None None>>
    ```

    Here, a stand-alone ‘#’ is being passed to Notation.

    ```python
    >>> n2 = notation.Notation('#')
    >>> n2.numbers
    (5, 3)
    >>> n2.modifiers
    (<music21.figuredBass.notation.Modifier None None>,
     <music21.figuredBass.notation.Modifier # sharp>)
    >>> n2.figures[0]
    <music21.figuredBass.notation.Figure 5 <Modifier None None>>
    >>> n2.figures[1]
    <music21.figuredBass.notation.Figure 3 <Modifier # sharp>>
    ```

    Now, a stand-alone b is being passed to Notation as part of a larger notationColumn.

    ```python
    >>> n3 = notation.Notation('b6,b')
    >>> n3.numbers
    (6, 3)
    >>> n3.modifiers
    (<music21.figuredBass.notation.Modifier b flat>,
     <music21.figuredBass.notation.Modifier b flat>)
    >>> n3.figures[0]
    <music21.figuredBass.notation.Figure 6 <Modifier b flat>>
    >>> n3.figures[1]
    <music21.figuredBass.notation.Figure 3 <Modifier b flat>>
    >>> n3.extenders
    [False, False]
    >>> n3.hasExtenders
    False
    ```

    Here we will use the unicode symbol for double-flat for the extender:

    ```python
    >>> n4 = notation.Notation('b6, 𝄫_, #')
    >>> n4.figures
    [<music21.figuredBass.notation.Figure 6 <Modifier b flat>>,
     <music21.figuredBass.notation.Figure _(extender) <Modifier 𝄫 double-flat>>,
     <music21.figuredBass.notation.Figure 3 <Modifier # sharp>>]
    >>> n4.figuresFromNotationColumn
    [<music21.figuredBass.notation.Figure 6 <Modifier b flat>>,
     <music21.figuredBass.notation.Figure _ <Modifier 𝄫 double-flat>>,
     <music21.figuredBass.notation.Figure None <Modifier # sharp>>]
    >>> n4.extenders
    [False, True, False]
    >>> n4.hasExtenders
    True
    ```

[`Notation`](#music21.figuredBass.notation.Notation "music21.figuredBass.notation.Notation") bases

* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`Notation`](#music21.figuredBass.notation.Notation "music21.figuredBass.notation.Notation") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`Notation`](#music21.figuredBass.notation.Notation "music21.figuredBass.notation.Notation") instance variables

Notation.figureStrings
:   A list of figures derived from the original
    [`notationColumn`](#music21.figuredBass.notation.Notation.notationColumn "music21.figuredBass.notation.Notation.notationColumn").

Notation.figures
:   A list of [`Figure`](#music21.figuredBass.notation.Figure "music21.figuredBass.notation.Figure") objects
    associated with figures in the expanded
    [`notationColumn`](#music21.figuredBass.notation.Notation.notationColumn "music21.figuredBass.notation.Notation.notationColumn").

Notation.modifierStrings
:   The modifiers associated with the expanded
    [`notationColumn`](#music21.figuredBass.notation.Notation.notationColumn "music21.figuredBass.notation.Notation.notationColumn"), as strings.

Notation.modifiers
:   A tuple of [`Modifier`](#music21.figuredBass.notation.Modifier "music21.figuredBass.notation.Modifier")
    objects associated with the expanded
    [`notationColumn`](#music21.figuredBass.notation.Notation.notationColumn "music21.figuredBass.notation.Notation.notationColumn").

Notation.notationColumn
:   A string of figures delimited by commas,
    each associated with a number and an optional modifier.

Notation.numbers
:   The numbers associated with the expanded
    [`notationColumn`](#music21.figuredBass.notation.Notation.notationColumn "music21.figuredBass.notation.Notation.notationColumn").

Notation.origModStrings
:   The modifiers associated with the original
    [`notationColumn`](#music21.figuredBass.notation.Notation.notationColumn "music21.figuredBass.notation.Notation.notationColumn"), as strings.

Notation.origNumbers
:   The numbers associated with the original
    [`notationColumn`](#music21.figuredBass.notation.Notation.notationColumn "music21.figuredBass.notation.Notation.notationColumn").

## Figure

class music21.figuredBass.notation.Figure(*number: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = 1*, *modifierString: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = ''*, *\**, *extender: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*)[[source]](../_modules/music21/figuredBass/notation.html#Figure)
:   A Figure is created by providing a number and a modifierString. The
    modifierString is turned into a [`Modifier`](#music21.figuredBass.notation.Modifier "music21.figuredBass.notation.Modifier"),
    and a ModifierException is raised if the modifierString is not valid.

    ```python
    >>> from music21.figuredBass import notation
    >>> f1 = notation.Figure(4, '+')
    >>> f1
    <music21.figuredBass.notation.Figure 4 <Modifier + sharp>>
    ```

    ```python
    >>> f1.number
    4
    >>> f1.modifierString
    '+'
    >>> f1.modifier
    <music21.figuredBass.notation.Modifier + sharp>
    >>> f1.hasExtender
    False
    >>> f1.isPureExtender
    False
    >>> f2 = notation.Figure(6, '#', extender=True)
    >>> f2.hasExtender
    True
    >>> f2.isPureExtender
    False
    >>> f3 = notation.Figure(extender=True)
    >>> f3.isPureExtender
    True
    >>> f3.hasExtender
    True
    ```

[`Figure`](#music21.figuredBass.notation.Figure "music21.figuredBass.notation.Figure") bases

* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`Figure`](#music21.figuredBass.notation.Figure "music21.figuredBass.notation.Figure") read-only properties

Figure.isPureExtender
:   Read-only boolean property that returns True if an extender is part of the figure
    but no number is given (a number of 1 means no-number). It is a pure extender.

    ```python
    >>> from music21.figuredBass import notation
    >>> n = notation.Figure(1, '#', extender=True)
    >>> n.isPureExtender
    True
    >>> n
    <music21.figuredBass.notation.Figure pure-extender <Modifier # sharp>>
    ```

    ```python
    >>> n.number = 2
    >>> n.isPureExtender
    False
    >>> n
    <music21.figuredBass.notation.Figure 2(extender) <Modifier # sharp>>
    ```

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`Figure`](#music21.figuredBass.notation.Figure "music21.figuredBass.notation.Figure") instance variables

Figure.hasExtender
:   A bool value that indicates whether an extender is part of the figure.
    It is set by a keyword argument.

Figure.modifier
:   A [`Modifier`](#music21.figuredBass.notation.Modifier "music21.figuredBass.notation.Modifier")
    associated with an expanded
    [`notationColumn`](#music21.figuredBass.notation.Notation.notationColumn "music21.figuredBass.notation.Notation.notationColumn").

Figure.modifierString
:   A modifier string associated with an
    expanded [`notationColumn`](#music21.figuredBass.notation.Notation.notationColumn "music21.figuredBass.notation.Notation.notationColumn").

Figure.number
:   A number associated with an expanded
    [`notationColumn`](#music21.figuredBass.notation.Notation.notationColumn "music21.figuredBass.notation.Notation.notationColumn").

## Modifier

class music21.figuredBass.notation.Modifier(*modifierString=None*)[[source]](../_modules/music21/figuredBass/notation.html#Modifier)
:   Turns a modifierString (a modifier in a
    [`notationColumn`](#music21.figuredBass.notation.Notation.notationColumn "music21.figuredBass.notation.Notation.notationColumn"))
    to an [`Accidental`](modulePitch.html#music21.pitch.Accidental "music21.pitch.Accidental"). A ModifierException
    is raised if the modifierString is not valid.

    Accepted inputs are those accepted by Accidental, as well as the following:

    * ‘+’ or ‘' -> ‘#’
    * ‘b’ or ‘/’ -> ‘-’

    ```python
    >>> from music21.figuredBass import notation
    >>> m1a = notation.Modifier('#')
    >>> m1a
    <music21.figuredBass.notation.Modifier # sharp>
    >>> m1a.modifierString
    '#'
    >>> m1a.accidental
    <music21.pitch.Accidental sharp>
    ```

    Providing a + in place of a sharp, we get the same result for the accidental.

    ```python
    >>> m2a = notation.Modifier('+')
    >>> m2a
    <music21.figuredBass.notation.Modifier + sharp>
    >>> m2a.accidental
    <music21.pitch.Accidental sharp>
    ```

    If None or ‘’ is provided for modifierString, then the accidental is None.

    ```python
    >>> m3a = notation.Modifier(None)
    >>> m3a
    <music21.figuredBass.notation.Modifier None None>
    >>> m3a.accidental is None
    True
    >>> m3b = notation.Modifier('')
    >>> m3b
    <music21.figuredBass.notation.Modifier  None>
    >>> m3b.accidental is None
    True
    ```

[`Modifier`](#music21.figuredBass.notation.Modifier "music21.figuredBass.notation.Modifier") bases

* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`Modifier`](#music21.figuredBass.notation.Modifier "music21.figuredBass.notation.Modifier") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`Modifier`](#music21.figuredBass.notation.Modifier "music21.figuredBass.notation.Modifier") methods

Modifier.modifyPitch(*pitchToAlter*, *\**, *inPlace=False*)[[source]](../_modules/music21/figuredBass/notation.html#Modifier.modifyPitch)
:   Given a [`Pitch`](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch"), modify its [`accidental`](modulePitch.html#music21.pitch.Pitch.accidental "music21.pitch.Pitch.accidental")
    given the Modifier’s [`accidental`](#music21.figuredBass.notation.Modifier.accidental "music21.figuredBass.notation.Modifier.accidental").

    ```python
    >>> from music21.figuredBass import notation
    >>> m1 = notation.Modifier('#')
    >>> m2 = notation.Modifier('-')
    >>> m3 = notation.Modifier('n')
    >>> p1a = pitch.Pitch('D5')
    >>> m1.modifyPitch(p1a)  # Sharp
    <music21.pitch.Pitch D#5>
    >>> m2.modifyPitch(p1a)  # Flat
    <music21.pitch.Pitch D-5>
    >>> p1b = pitch.Pitch('D#5')
    >>> m3.modifyPitch(p1b)
    <music21.pitch.Pitch D5>
    ```

Modifier.modifyPitchName(*pitchNameToAlter*)[[source]](../_modules/music21/figuredBass/notation.html#Modifier.modifyPitchName)
:   Given a pitch name, modify its accidental given the Modifier’s
    [`accidental`](#music21.figuredBass.notation.Modifier.accidental "music21.figuredBass.notation.Modifier.accidental").

    ```python
    >>> from music21.figuredBass import notation
    >>> m1 = notation.Modifier('#')
    >>> m2 = notation.Modifier('-')
    >>> m3 = notation.Modifier('n')
    >>> m1.modifyPitchName('D')  # Sharp
    'D#'
    >>> m2.modifyPitchName('F')  # Flat
    'F-'
    >>> m3.modifyPitchName('C#')  # Natural
    'C'
    ```

[`Modifier`](#music21.figuredBass.notation.Modifier "music21.figuredBass.notation.Modifier") instance variables

Modifier.accidental
:   A [`Accidental`](modulePitch.html#music21.pitch.Accidental "music21.pitch.Accidental") corresponding to
    [`modifierString`](#music21.figuredBass.notation.Modifier.modifierString "music21.figuredBass.notation.Modifier.modifierString").

Modifier.modifierString
:   A modifier string associated with an
    expanded [`notationColumn`](#music21.figuredBass.notation.Notation.notationColumn "music21.figuredBass.notation.Notation.notationColumn").

## Functions

music21.figuredBass.notation.convertToPitch(*pitchString*)[[source]](../_modules/music21/figuredBass/notation.html#convertToPitch)
:   Converts a pitchString to a [`Pitch`](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch"), only if necessary.

    ```python
    >>> from music21.figuredBass import notation
    >>> pitchStr = 'C5'
    >>> notation.convertToPitch(pitchStr)
    <music21.pitch.Pitch C5>
    >>> notation.convertToPitch(pitch.Pitch('E4'))  # does nothing
    <music21.pitch.Pitch E4>
    ```
