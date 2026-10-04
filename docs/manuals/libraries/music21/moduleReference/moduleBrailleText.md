Source: https://music21.org/music21docs/moduleReference/moduleBrailleText.html

# music21.braille.text

## BrailleKeyboard

class music21.braille.text.BrailleKeyboard(*lineLength=40*)[[source]](../_modules/music21/braille/text.html#BrailleKeyboard)
:   A subclass of BrailleText that handles both hands at once.

[`BrailleKeyboard`](#music21.braille.text.BrailleKeyboard "music21.braille.text.BrailleKeyboard") bases

* [`BrailleText`](#music21.braille.text.BrailleText "music21.braille.text.BrailleText")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`BrailleKeyboard`](#music21.braille.text.BrailleKeyboard "music21.braille.text.BrailleKeyboard") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`BrailleKeyboard`](#music21.braille.text.BrailleKeyboard "music21.braille.text.BrailleKeyboard") read/write properties

Read/write properties inherited from [`BrailleText`](#music21.braille.text.BrailleText "music21.braille.text.BrailleText"):

|  |  |  |
| --- | --- | --- |
| * [`showHand`](#music21.braille.text.BrailleText.showHand "music21.braille.text.BrailleText.showHand") |  |  |

[`BrailleKeyboard`](#music21.braille.text.BrailleKeyboard "music21.braille.text.BrailleKeyboard") methods

BrailleKeyboard.addNoteGroupings(*measureNumber*, *noteGroupingR*, *noteGroupingL*)[[source]](../_modules/music21/braille/text.html#BrailleKeyboard.addNoteGroupings)

BrailleKeyboard.makeNewLines()[[source]](../_modules/music21/braille/text.html#BrailleKeyboard.makeNewLines)

Methods inherited from [`BrailleText`](#music21.braille.text.BrailleText "music21.braille.text.BrailleText"):

|  |  |  |
| --- | --- | --- |
| * [`addHeading()`](#music21.braille.text.BrailleText.addHeading "music21.braille.text.BrailleText.addHeading") * [`addInaccord()`](#music21.braille.text.BrailleText.addInaccord "music21.braille.text.BrailleText.addInaccord") * [`addLongExpression()`](#music21.braille.text.BrailleText.addLongExpression "music21.braille.text.BrailleText.addLongExpression") * [`addMeasureNumber()`](#music21.braille.text.BrailleText.addMeasureNumber "music21.braille.text.BrailleText.addMeasureNumber") | * [`addSignatures()`](#music21.braille.text.BrailleText.addSignatures "music21.braille.text.BrailleText.addSignatures") * [`addToNewLine()`](#music21.braille.text.BrailleText.addToNewLine "music21.braille.text.BrailleText.addToNewLine") * [`appendOrInsertCurrent()`](#music21.braille.text.BrailleText.appendOrInsertCurrent "music21.braille.text.BrailleText.appendOrInsertCurrent") | * [`makeNewLine()`](#music21.braille.text.BrailleText.makeNewLine "music21.braille.text.BrailleText.makeNewLine") * [`optionalAddKeyboardSymbolsAndDots()`](#music21.braille.text.BrailleText.optionalAddKeyboardSymbolsAndDots "music21.braille.text.BrailleText.optionalAddKeyboardSymbolsAndDots") * [`recenterHeadings()`](#music21.braille.text.BrailleText.recenterHeadings "music21.braille.text.BrailleText.recenterHeadings") |

## BrailleText

class music21.braille.text.BrailleText(*lineLength=40*, *showHand=None*)[[source]](../_modules/music21/braille/text.html#BrailleText)
:   Object that handles all the formatting associated with braille music notation on multiple lines.

    ```python
    >>> bt = braille.text.BrailleText(lineLength=10, showHand='right')
    >>> bt
    <music21.braille.text.BrailleText 1 line, 0 headings, 10 cols>
    >>> bt.lineLength
    10
    >>> bt.allLines
    [<music21.braille.text.BrailleTextLine '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀'>]
    >>> bt.rightHandSymbol
    True
    >>> bt.leftHandSymbol
    False
    >>> bt.allHeadings
    []
    ```

[`BrailleText`](#music21.braille.text.BrailleText "music21.braille.text.BrailleText") bases

* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`BrailleText`](#music21.braille.text.BrailleText "music21.braille.text.BrailleText") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`BrailleText`](#music21.braille.text.BrailleText "music21.braille.text.BrailleText") read/write properties

BrailleText.showHand

[`BrailleText`](#music21.braille.text.BrailleText "music21.braille.text.BrailleText") methods

BrailleText.addHeading(*heading*)[[source]](../_modules/music21/braille/text.html#BrailleText.addHeading)
:   adds a heading to the BrailleText. Heading can be a single or multiple line
    Unicode string representing a heading.

    These headings are not stored in allHeadings, but instead in .allLines,
    what .allHeadings stores is the index of the start of a heading section
    and the index of the end of a heading section.

    (since each BrailleTextLine knows whether it is a heading or not, storing
    the index of headings might be overkill)

    ```python
    >>> bt = braille.text.BrailleText(lineLength=10)
    >>> headingText = braille.basic.timeSigToBraille(meter.TimeSignature('4/8'))
    >>> bt.addHeading(headingText)
    >>> len(bt.allLines)
    2
    >>> bt.allLines[0].isHeading
    True
    >>> print(str(bt.allLines[0]))
    ⠼⠙⠦
    >>> bt.allHeadings
    [(0, 1)]
    >>> bt.addMeasureNumber(7)
    >>> headingText = braille.basic.timeSigToBraille(meter.TimeSignature('3/4'))
    >>> bt.addHeading(headingText)
    >>> len(bt.allLines)
    4
    >>> bt.allHeadings
    [(0, 1), (2, 3)]
    ```

BrailleText.addInaccord(*inaccord*)[[source]](../_modules/music21/braille/text.html#BrailleText.addInaccord)

BrailleText.addLongExpression(*longExpr*)[[source]](../_modules/music21/braille/text.html#BrailleText.addLongExpression)
:   Adds an expression long enough that it is split at
    each space symbol such that line wrapping could occur.

BrailleText.addMeasureNumber(*measureNumber*)[[source]](../_modules/music21/braille/text.html#BrailleText.addMeasureNumber)
:   Add a measure number (either a braille number or an int).

    ```python
    >>> bt = braille.text.BrailleText(lineLength=10)
    >>> bt
    <music21.braille.text.BrailleText 1 line, 0 headings, 10 cols>
    >>> bt.allLines
    [<music21.braille.text.BrailleTextLine '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀'>]
    >>> bt.addMeasureNumber(4)
    >>> print(str(bt.allLines[0]))
    ⠼⠙
    >>> bt.currentLine.textLocation
    2
    ```

    If there are already lines, then add a new one:

    ```python
    >>> bt.addMeasureNumber(5)
    >>> bt.allLines
    [<music21.braille.text.BrailleTextLine '⠼⠙⠀⠀⠀⠀⠀⠀⠀⠀'>,
     <music21.braille.text.BrailleTextLine '⠼⠑⠀⠀⠀⠀⠀⠀⠀⠀'>]
    >>> print(str(bt.allLines[-1]))
    ⠼⠑
    ```

BrailleText.addSignatures(*signatures*)[[source]](../_modules/music21/braille/text.html#BrailleText.addSignatures)
:   Appends signatures to the current location if there is space, otherwise appends to
    a new line:

    ```python
    >>> bt = braille.text.BrailleText(lineLength=5)
    >>> bt.addSignatures(braille.basic.timeSigToBraille(meter.TimeSignature('4/8')))
    >>> print(str(bt.currentLine))
    ⠼⠙⠦
    >>> bt.addSignatures(braille.basic.timeSigToBraille(meter.TimeSignature('3/4')))
    >>> print(str(bt.currentLine))
    ⠀⠀⠼⠉⠲
    >>> len(bt.allLines)
    2
    ```

BrailleText.addToNewLine(*brailleNoteGrouping*)[[source]](../_modules/music21/braille/text.html#BrailleText.addToNewLine)
:   Adds a NoteGrouping to a new line, prefacing that new line
    with the appropriate spaces or keyboard symbols and dots.

    ```python
    >>> bt = braille.text.BrailleText(10)
    >>> bt.currentLine.append('hi', addSpace=False)
    >>> print(str(bt))
    hi
    >>> c = braille.lookup.pitchNameToNotes['C']['quarter']  # dots 1456
    >>> bt.addToNewLine(c + c + c)
    >>> print(str(bt))
    hi
    ⠀⠀⠹⠹⠹
    ```

    It is done differently if there are hand symbols involved:

    ```python
    >>> bt = braille.text.BrailleText(10)
    >>> bt.showHand = 'right'
    >>> bt.currentLine.append('hi', addSpace=False)
    >>> bt.addToNewLine(c + c + c)
    >>> print(str(bt))
    hi
    ⠨⠜⠄⠹⠹⠹
    ```

BrailleText.appendOrInsertCurrent(*brailleExpr*, *addSpace=True*)[[source]](../_modules/music21/braille/text.html#BrailleText.appendOrInsertCurrent)
:   append expression to the current line if it is possible,
    or make a new line and insert it there:

    ```python
    >>> bt = braille.text.BrailleText(lineLength=10)
    >>> bt.appendOrInsertCurrent('hello', addSpace=False)
    >>> print(str(bt))
    hello
    >>> bt.appendOrInsertCurrent(braille.lookup.symbols['space'] + 'hi')
    >>> print(str(bt))
    hello⠀⠀hi
    >>> bt.appendOrInsertCurrent(braille.lookup.symbols['space'] + 'there')
    >>> print(str(bt))
    hello⠀⠀hi
    ⠀⠀⠀there
    ```

BrailleText.makeNewLine()[[source]](../_modules/music21/braille/text.html#BrailleText.makeNewLine)
:   Add a newline to the BrailleText

    ```python
    >>> bt = braille.text.BrailleText(lineLength=10)
    >>> len(bt.allLines)
    1
    >>> bt.makeNewLine()
    >>> len(bt.allLines)
    2
    >>> bt.makeNewLine()
    >>> len(bt.allLines)
    3
    ```

BrailleText.optionalAddKeyboardSymbolsAndDots(*noteGrouping=None*)[[source]](../_modules/music21/braille/text.html#BrailleText.optionalAddKeyboardSymbolsAndDots)
:   Adds symbols for rh\_keyboard or lh\_keyboard depending on what
    is appropriate

    returns a boolean indicating whether a space needs to be added
    before the next symbol is needed.

BrailleText.recenterHeadings()[[source]](../_modules/music21/braille/text.html#BrailleText.recenterHeadings)
:   Recenter each of the headings so that they exactly align
    with the text beneath them.

    Demonstration with non braille text:

    ```python
    >>> heading1 = 'hello'
    >>> body1 = 'anyoneHome?' + braille.lookup.symbols['space'] + 'yup!'
    >>> bt = braille.text.BrailleText(lineLength=12)
    >>> bt.addHeading(heading1)
    >>> bt.addLongExpression(body1)
    >>> bt.allHeadings
    [(0, 1)]
    >>> bt.recenterHeadings()
    >>> print(str(bt))
    ⠀⠀⠀hello⠀⠀⠀⠀
    ⠀anyoneHome?
    ⠀⠀yup!
    ```

    Each heading is aligned with its own text

    ```python
    >>> heading2 = 'buh'
    >>> body2 = 'short' + braille.lookup.symbols['space'] + 'court'
    >>> bt.addHeading(heading2)
    >>> bt.addLongExpression(body2)
    >>> bt.allHeadings
    [(0, 1), (3, 4)]
    >>> bt.recenterHeadings()
    >>> print(str(bt))
    ⠀⠀⠀hello⠀⠀⠀⠀
    ⠀anyoneHome?
    ⠀⠀yup!
    ⠀⠀⠀⠀buh⠀⠀⠀⠀⠀
    ⠀short⠀court
    ```

## BrailleTextLine

class music21.braille.text.BrailleTextLine(*lineLength: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 40*)[[source]](../_modules/music21/braille/text.html#BrailleTextLine)
:   An object representing a single line of braille text:

    The initial value is the length of the line:

    ```python
    >>> btl = braille.text.BrailleTextLine(40)
    >>> btl
    <music21.braille.text.BrailleTextLine '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀'>
    >>> btl.isHeading
    False
    >>> btl.containsNoteGrouping
    False
    >>> btl.lineLength
    40
    >>> btl.textLocation
    0
    >>> btl.highestUsedLocation
    0
    >>> btl.allChars == 40 * [braille.lookup.symbols['space']]
    True
    ```

    ```python
    >>> btl.append(braille.lookup.symbols['tie'])
    >>> btl
    <music21.braille.text.BrailleTextLine '⠀⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀'>
    >>> print(str(btl))
    ⠀⠈⠉
    ```

[`BrailleTextLine`](#music21.braille.text.BrailleTextLine "music21.braille.text.BrailleTextLine") bases

* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`BrailleTextLine`](#music21.braille.text.BrailleTextLine "music21.braille.text.BrailleTextLine") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`BrailleTextLine`](#music21.braille.text.BrailleTextLine "music21.braille.text.BrailleTextLine") methods

BrailleTextLine.append(*text*, *addSpace=True*)[[source]](../_modules/music21/braille/text.html#BrailleTextLine.append)
:   Appends text (with optional space at the beginning) or raises an
    exception if it cannot be appended.

    ```python
    >>> btl = braille.text.BrailleTextLine(6)
    >>> btl.append(braille.lookup.symbols['tie'], addSpace=False)
    >>> print(str(btl))
    ⠈⠉
    >>> btl.textLocation
    2
    >>> btl.highestUsedLocation
    2
    ```

    Default is to add a space:

    ```python
    >>> btl.append(braille.lookup.symbols['tie'])
    >>> print(str(btl))
    ⠈⠉⠀⠈⠉
    ```

    Out of room:

    ```python
    >>> btl.append(braille.lookup.symbols['tie'])
    Traceback (most recent call last):
    music21.braille.text.BrailleTextException: Text does not fit at end of braille text line.
    ```

    Text is appended at textLocation, overwriting other text that might be there.

    ```python
    >>> btl.textLocation = btl.highestUsedLocation = 0
    >>> btl.append('hi', addSpace=False)
    >>> btl.textLocation = btl.highestUsedLocation = 5
    >>> print(str(btl))
    hi⠀⠈⠉
    ```

BrailleTextLine.canAppend(*text*, *addSpace=True*)[[source]](../_modules/music21/braille/text.html#BrailleTextLine.canAppend)
:   Returns True if there is enough space in this line to append the text, or False
    if not:

    ```python
    >>> btl = braille.text.BrailleTextLine(10)
    >>> btl.canAppend('1234567890', addSpace=False)
    True
    >>> btl.canAppend('12345678901', addSpace=False)
    False
    >>> btl.canAppend('1234567890', addSpace=True)
    False
    >>> btl.textLocation
    0
    >>> btl.textLocation = 5
    >>> btl.canAppend('12345', addSpace=False)
    True
    >>> btl.canAppend('123456', addSpace=False)
    False
    ```

    If highestUsedLocation > textLocation, highestUsedLocation is used instead:

    ```python
    >>> btl.highestUsedLocation = 7
    >>> btl.canAppend('123', addSpace=False)
    True
    >>> btl.canAppend('1234', addSpace=False)
    False
    ```

BrailleTextLine.canInsert(*textLocation*, *text*)[[source]](../_modules/music21/braille/text.html#BrailleTextLine.canInsert)
:   Returns True if there is enough space starting at textLocation to append
    the text. False otherwise:

    ```python
    >>> btl = braille.text.BrailleTextLine(10)
    >>> btl.canInsert(4, '123456')
    True
    >>> btl.canInsert(5, '123456')
    False
    ```

BrailleTextLine.insert(*textLocation*, *text*)[[source]](../_modules/music21/braille/text.html#BrailleTextLine.insert)
:   Inserts text at a certain location, updating textLocation and possibly
    highestUsedLocation:

    ```python
    >>> btl = braille.text.BrailleTextLine(6)
    >>> btl.insert(2, braille.lookup.symbols['tie'])
    >>> print(str(btl))
    ⠀⠀⠈⠉
    >>> btl.textLocation
    4
    >>> btl.highestUsedLocation
    4
    ```

    ```python
    >>> btl.insert(0, braille.lookup.symbols['tie'])
    ```

    It looks like we have deleted the previous tie:

    ```python
    >>> print(str(btl))
    ⠈⠉
    ```

    But that’s because only characters up to .textLocation are printed
    (this may change later)

    ```python
    >>> btl.textLocation
    2
    >>> btl.highestUsedLocation
    4
    ```

    Let’s change textLocation and now see:

    ```python
    >>> btl.textLocation = btl.highestUsedLocation
    >>> print(str(btl))
    ⠈⠉⠈⠉
    ```

    Inserting beyond the end creates an error:

    ```python
    >>> btl.insert(5, braille.lookup.symbols['tie'])
    Traceback (most recent call last):
    music21.braille.text.BrailleTextException: Text cannot be inserted at specified location.
    ```

    Unlike list inserts, this insert overwrites the previous text:

    ```python
    >>> btl.insert(0, 'hi')
    >>> btl.textLocation = btl.highestUsedLocation
    >>> print(str(btl))
    hi⠈⠉
    ```

BrailleTextLine.lastHyphenToSpace()[[source]](../_modules/music21/braille/text.html#BrailleTextLine.lastHyphenToSpace)
:   Occasionally a line ends with a hyphen because
    the last appender thought it would be helpful, such as
    to put more characters into a line. But in case it
    is not, then this method will change that last character
    to a space and set textLocation back one character,
    so it is not printed.

    ```python
    >>> bt = braille.text.BrailleTextLine(10)
    >>> bt.append('hi', addSpace=False)
    >>> bt.append(braille.lookup.symbols['music_hyphen'], addSpace=False)
    >>> print(str(bt))
    hi⠐
    >>> bt.textLocation
    3
    >>> print(bt.allChars[2])
    ⠐
    >>> bt.lastHyphenToSpace()
    >>> print(str(bt))
    hi
    >>> bt.allChars[2] == braille.lookup.symbols['space']
    True
    >>> bt.textLocation
    2
    ```
