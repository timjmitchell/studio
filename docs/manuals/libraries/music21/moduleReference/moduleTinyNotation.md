Source: https://music21.org/music21docs/moduleReference/moduleTinyNotation.html

# music21.tinyNotation

tinyNotation is a simple way of specifying single line melodies
that uses a notation somewhat similar to Lilypond but with WAY fewer
options. It was originally developed to notate trecento (medieval Italian)
music, but it is pretty useful for a lot of short examples, so we have
made it a generally supported music21 format.

N.B.: TinyNotation is not meant to expand to cover every single case. Instead,
it is meant to be subclassable to extend to the cases *your* project needs.

Here are the most important rules by default:

1. Note names are: a,b,c,d,e,f,g and r for rest
2. Flats, sharps, and naturals are notated as #,- (not b), and (if needed) n.
   If the accidental is above the staff (i.e., editorial), enclose it in
   parentheses: (#), etc. Make sure that flats in the key signatures are
   explicitly specified.
3. Note octaves are specified as follows:

   ```python
   CC to BB = from C below bass clef to second-line B in bass clef
   C to B = from bass clef C to B below middle C.
   c  to b = from middle C to the middle of treble clef
   c' to b' = from C in treble clef to B above treble clef
   ```

   Octaves below and above these are specified by further doublings of
   letter (CCC) or apostrophes (c’’) – this is one of the note name
   standards found in many music theory books.
4. After the note name, a number may be placed indicating the note
   length: 1 = whole note, 2 = half, 4 = quarter, 8 = eighth, 16 = sixteenth.
   etc. If the number is omitted then it is assumed to be the same
   as the previous note. I.e., c8 B c d is a string of eighth notes.
5. After the number, a ~ can be placed to show a tie to the next note.
   A “.” indicates a dotted note. (If you are entering
   data via Excel or other spreadsheet, be sure that “capitalize the
   first letter of sentences” is turned off under “Tools->AutoCorrect,”
   otherwise the next letter will be capitalized, and the octave will
   be screwed up.)
6. For triplets use this notation: trip{c4 d8} indicating that these
   two notes both have “3s” over them. For 4 in the place of 3,
   use quad{c16 d e8}. No other tuplets are supported.

Here is an example of TinyNotation in action.

```python
>>> stream1 = converter.parse("tinyNotation: 3/4 E4 r f# g=lastG trip{b-8 a g} c4~ c")
>>> stream1.show('text')
{0.0} <music21.stream.Measure 1 offset=0.0>
    {0.0} <music21.clef.TrebleClef>
    {0.0} <music21.meter.TimeSignature 3/4>
    {0.0} <music21.note.Note E>
    {1.0} <music21.note.Rest quarter>
    {2.0} <music21.note.Note F#>
{3.0} <music21.stream.Measure 2 offset=3.0>
    {0.0} <music21.note.Note G>
    {1.0} <music21.note.Note B->
    {1.3333} <music21.note.Note A>
    {1.6667} <music21.note.Note G>
    {2.0} <music21.note.Note C>
{6.0} <music21.stream.Measure 3 offset=6.0>
    {0.0} <music21.note.Note C>
    {1.0} <music21.bar.Barline type=final>
>>> stream1.recurse().getElementById('lastG').step
'G'
>>> stream1.flatten().notesAndRests[1].isRest
True
>>> stream1.flatten().notesAndRests[0].octave
3
>>> stream1.flatten().notes[-2].tie.type
'start'
>>> stream1.flatten().notes[-1].tie.type
'stop'
```

Changing time signatures are supported:

```python
>>> s1 = converter.parse('tinynotation: 3/4 C4 D E 2/4 F G A B 1/4 c')
>>> s1.show('t')
{0.0} <music21.stream.Measure 1 offset=0.0>
    {0.0} <music21.clef.BassClef>
    {0.0} <music21.meter.TimeSignature 3/4>
    {0.0} <music21.note.Note C>
    {1.0} <music21.note.Note D>
    {2.0} <music21.note.Note E>
{3.0} <music21.stream.Measure 2 offset=3.0>
    {0.0} <music21.meter.TimeSignature 2/4>
    {0.0} <music21.note.Note F>
    {1.0} <music21.note.Note G>
{5.0} <music21.stream.Measure 3 offset=5.0>
    {0.0} <music21.note.Note A>
    {1.0} <music21.note.Note B>
{7.0} <music21.stream.Measure 4 offset=7.0>
    {0.0} <music21.meter.TimeSignature 1/4>
    {0.0} <music21.note.Note C>
    {1.0} <music21.bar.Barline type=final>
```

Here is an equivalent way of doing the example above, but using the lower level
[`music21.tinyNotation.Converter`](#music21.tinyNotation.Converter "music21.tinyNotation.Converter") object:

```python
>>> tnc = tinyNotation.Converter('3/4 E4 r f# g=lastG trip{b-8 a g} c4~ c')
>>> stream2 = tnc.parse().stream
>>> len(stream1.recurse()) == len(stream2.recurse())
True
```

This lower level is needed in case you want to add additional features. For instance,
here we will set the “modifierStar” to change the color of notes:

```python
>>> class ColorModifier(tinyNotation.Modifier):
...     def postParse(self, m21Obj):
...         m21Obj.style.color = self.modifierData
...         return m21Obj
```

```python
>>> tnc = tinyNotation.Converter('3/4 C4*pink* D4*green* E4*blue*')
>>> tnc.modifierStar = ColorModifier
>>> s = tnc.parse().stream
>>> for n in s.recurse().getElementsByClass(note.Note):
...     print(n.step, n.style.color)
C pink
D green
E blue
```

Or more usefully, and often desired:

```python
>>> class HarmonyModifier(tinyNotation.Modifier):
...     def postParse(self, n):
...         cs = harmony.ChordSymbol(n.pitch.name + self.modifierData)
...         cs.duration = n.duration
...         return cs
>>> tnc = tinyNotation.Converter('4/4 C2_maj7 D4_m E-_sus4')
>>> tnc.modifierUnderscore = HarmonyModifier
>>> s = tnc.parse().stream
>>> s.show('text')
{0.0} <music21.stream.Measure 1 offset=0.0>
    {0.0} <music21.clef.BassClef>
    {0.0} <music21.meter.TimeSignature 4/4>
    {0.0} <music21.harmony.ChordSymbol Cmaj7>
    {2.0} <music21.harmony.ChordSymbol Dm>
    {3.0} <music21.harmony.ChordSymbol E-sus4>
    {4.0} <music21.bar.Barline type=final>
>>> for cs in s.recurse().getElementsByClass(harmony.ChordSymbol):
...     print([p.name for p in cs.pitches])
['C', 'E', 'G', 'B']
['D', 'F', 'A']
['E-', 'A-', 'B-']
```

The supported modifiers are:
:   * =data (modifierEquals, default action is to set .id)
    * \_data (modifierUnderscore, default action is to set .lyric)
    * [data] (modifierSquare, no default action)
    * <data> (modifierAngle, no default action)
    * (data) (modifierParens, no default action)
    * \*data\* (modifierStar, no default action)

Another example: TinyNotation does not support key signatures – well, no problem! Let’s
create a new Token type and add it to the tokenMap

```python
>>> class KeyToken(tinyNotation.Token):
...     def parse(self, parent):
...         keyName = self.token
...         return key.Key(keyName)
>>> keyMapping = (r'k(.*)', KeyToken)
>>> tnc = tinyNotation.Converter('4/4 kE- G1 kf# A1')
>>> tnc.tokenMap.append(keyMapping)
>>> s = tnc.parse().stream
>>> s.show('text')
{0.0} <music21.stream.Measure 1 offset=0.0>
    {0.0} <music21.clef.BassClef>
    {0.0} <music21.key.Key of E- major>
    {0.0} <music21.meter.TimeSignature 4/4>
    {0.0} <music21.note.Note G>
{4.0} <music21.stream.Measure 2 offset=4.0>
    {0.0} <music21.key.Key of f# minor>
    {0.0} <music21.note.Note A>
    {4.0} <music21.bar.Barline type=final>
```

TokenMap should be passed a string, representing a regular expression with exactly one
group (which can be the entire expression), and a subclass of [`Token`](#music21.tinyNotation.Token "music21.tinyNotation.Token")
which will handle the parsing of the string.

Tokens can take advantage of the parent variable, which is a reference to the Converter
object, to use the .stateDict dictionary to store information about state. For instance,
the NoteOrRestToken uses parent.stateDict[‘lastDuration’] to get access to the last
duration.

There is also the concept of “State” which affects multiple tokens. The best way to create
a new State is to define a subclass of the [`State`](#music21.tinyNotation.State "music21.tinyNotation.State") and add it
to bracketStateMapping of the converter. Here’s one that a lot of people have asked for
over the years:

```python
>>> class ChordState(tinyNotation.State):
...    def affectTokenAfterParse(self, n):
...        super().affectTokenAfterParse(n)
...        return None  # do not append Note object
...    def end(self):
...        ch = chord.Chord(self.affectedTokens)
...        ch.duration = self.affectedTokens[0].duration
...        return ch
>>> tnc = tinyNotation.Converter("2/4 C4 chord{C4 e g'} F.4 chord{D8 F# A}")
>>> tnc.bracketStateMapping['chord'] = ChordState
>>> s = tnc.parse().stream
>>> s.show('text')
{0.0} <music21.stream.Measure 1 offset=0.0>
    {0.0} <music21.clef.BassClef>
    {0.0} <music21.meter.TimeSignature 2/4>
    {0.0} <music21.note.Note C>
    {1.0} <music21.chord.Chord C3 E4 G5>
{2.0} <music21.stream.Measure 2 offset=2.0>
    {0.0} <music21.note.Note F>
    {1.5} <music21.chord.Chord D3 F#3 A3>
    {2.0} <music21.bar.Barline type=final>
```

If you want to create a very different dialect, you can subclass tinyNotation.Converter
and set it up once to use the mappings above. See
`TrecentoTinyConverter` (especially the code)
for details on how to do that.

## Converter

class music21.tinyNotation.Converter(*stringRep: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*, *\**, *makeNotation: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *raiseExceptions: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *\*\*\_keywords*)[[source]](../_modules/music21/tinyNotation.html#Converter)
:   Main conversion object for TinyNotation.

    Accepts keywords:

    * makeNotation=False to get “classic” TinyNotation formats without
      :   measures, Clefs, etc.
    * raiseExceptions=True to make errors become exceptions.

    Generally, users should just use the general music21 converter (lowercase c) parse
    function and do not need to be in this module at all:

    ```python
    >>> part = converter.parse('4/4 C4 D4 E2 F1', format='tinyNotation')
    >>> part.show('text')
    {0.0} <music21.stream.Measure 1 offset=0.0>
        {0.0} <music21.clef.BassClef>
        {0.0} <music21.meter.TimeSignature 4/4>
        {0.0} <music21.note.Note C>
        {1.0} <music21.note.Note D>
        {2.0} <music21.note.Note E>
    {4.0} <music21.stream.Measure 2 offset=4.0>
        {0.0} <music21.note.Note F>
        {4.0} <music21.bar.Barline type=final>
    ```

    But for advanced work, create a tinyNotation.Converter object as shown:

    ```python
    >>> tnc = tinyNotation.Converter('4/4 C##4 D e-8 f~ f f# g4 trip{f8 e d} C2=hello')
    ```

    Run the parsing routine with .parse()

    ```python
    >>> tnc.parse()
    <music21.tinyNotation.Converter object at 0x10aeefbe0>
    ```

    And now the .stream attribute of the converter object
    has the Stream (generally Part) ready to send out:

    ```python
    >>> tnc.stream
    <music21.stream.Part 0x10acee860>
    ```

    And all normal Stream methods are available on it:

    ```python
    >>> tnc.stream.show('text')
    {0.0} <music21.stream.Measure 1 offset=0.0>
        {0.0} <music21.clef.TrebleClef>
        {0.0} <music21.meter.TimeSignature 4/4>
        {0.0} <music21.note.Note C##>
        {1.0} <music21.note.Note D>
        {2.0} <music21.note.Note E->
        {2.5} <music21.note.Note F>
        {3.0} <music21.note.Note F>
        {3.5} <music21.note.Note F#>
    {4.0} <music21.stream.Measure 2 offset=4.0>
        {0.0} <music21.note.Note G>
        {1.0} <music21.note.Note F>
        {1.3333} <music21.note.Note E>
        {1.6667} <music21.note.Note D>
        {2.0} <music21.note.Note C>
        {4.0} <music21.bar.Barline type=final>
    ```

    Or, breaking down what Parse does bit by bit:

    ```python
    >>> tnc = tinyNotation.Converter('4/4 C##4 D e-8 f~ f f# g4 trip{f8 e d} C2=hello')
    >>> tnc.stream
    <music21.stream.Part 0x10acee860>
    >>> tnc.makeNotation
    True
    >>> tnc.stringRep
    '4/4 C##4 D e-8 f~ f f# g4 trip{f8 e d} C2=hello'
    >>> tnc.activeStates
    []
    >>> tnc.preTokens
    []
    >>> tnc.splitPreTokens()
    >>> tnc.preTokens
    ['4/4', 'C##4', 'D', 'e-8', 'f~', 'f', 'f#', 'g4', 'trip{f8', 'e', 'd}', 'C2=hello']
    >>> tnc.setupRegularExpressions()
    ```

    Then we parse the time signature.
    >>> tnc.parseOne(0, tnc.preTokens[0])
    >>> tnc.stream.coreElementsChanged()
    >>> tnc.stream.show(‘text’)
    {0.0} <music21.meter.TimeSignature 4/4>

    (Note that because we are calling
    show() after each note in these docs, but TinyNotation
    uses high efficiency stream.core routines, we need to set the stream
    to a stable-state by calling coreElementsChanged after each call.
    You would not need to do this in your own subclasses, since that would
    lose the O(n) efficiency when parsing)

    Then parse the first actual note:

    ```python
    >>> tnc.parseOne(1, tnc.preTokens[1])
    >>> tnc.stream.coreElementsChanged()
    >>> tnc.stream.show('text')
    {0.0} <music21.meter.TimeSignature 4/4>
    {0.0} <music21.note.Note C##>
    ```

    The next notes to ‘g4’ are pretty similar:

    ```python
    >>> for i in range(2, 8):
    ...     tnc.parseOne(i, tnc.preTokens[i])
    >>> tnc.stream.coreElementsChanged()
    >>> tnc.stream.show('text')
    {0.0} <music21.meter.TimeSignature 4/4>
    {0.0} <music21.note.Note C##>
    {1.0} <music21.note.Note D>
    {2.0} <music21.note.Note E->
    {2.5} <music21.note.Note F>
    {3.0} <music21.note.Note F>
    {3.5} <music21.note.Note F#>
    {4.0} <music21.note.Note G>
    ```

    The next note starts a “State” since it has a triplet:

    ```python
    >>> tnc.preTokens[8]
    'trip{f8'
    >>> tnc.parseOne(8, tnc.preTokens[8])
    >>> tnc.activeStates
    [<music21.tinyNotation.TripletState object at 0x10ae9dba8>]
    >>> tnc.activeStates[0].affectedTokens
    [<music21.note.Note F>]
    ```

    The state is still active for the next token:

    ```python
    >>> tnc.preTokens[9]
    'e'
    >>> tnc.parseOne(9, tnc.preTokens[9])
    >>> tnc.activeStates
    [<music21.tinyNotation.TripletState object at 0x10ae9dba8>]
    >>> tnc.activeStates[0].affectedTokens
    [<music21.note.Note F>, <music21.note.Note E>]
    ```

    The [`TripletState`](#music21.tinyNotation.TripletState "music21.tinyNotation.TripletState") state adds
    tuplets along the way, but does not set their type.

    ```python
    >>> f_starts_tuplet = tnc.activeStates[0].affectedTokens[0]
    >>> f_starts_tuplet.duration.tuplets
    (<music21.duration.Tuplet 3/2/eighth>,)
    >>> f_starts_tuplet.duration.tuplets[0].type is None
    True
    ```

    But the next token closes the state:

    ```python
    >>> tnc.preTokens[10]
    'd}'
    >>> tnc.parseOne(10, tnc.preTokens[10])
    >>> tnc.activeStates
    []
    ```

    And this sets the tupet types for the F and D properly:

    ```python
    >>> f_starts_tuplet.duration.tuplets[0].type
    'start'
    ```

    ```python
    >>> tnc.stream.coreElementsChanged()
    >>> tnc.stream.show('text')
    {0.0} <music21.meter.TimeSignature 4/4>
    ...
    {4.0} <music21.note.Note G>
    {5.0} <music21.note.Note F>
    {5.3333} <music21.note.Note E>
    {5.6667} <music21.note.Note D>
    ```

    The last token has a modifier, which is an IdModifier:

    ```python
    >>> tnc.preTokens[11]
    'C2=hello'
    >>> tnc.parseOne(11, tnc.preTokens[11])
    >>> tnc.stream.coreElementsChanged()
    >>> tnc.stream.show('text')
    {0.0} <music21.meter.TimeSignature 4/4>
    ...
    {5.6667} <music21.note.Note D>
    {6.0} <music21.note.Note C>
    >>> tnc.stream[-1].id
    'hello'
    ```

    At this point the flattened stream is ready, if Converter.makeNotation
    is False, then not much more needs to happen, but it is True by default.

    So, then calling tnc.postParse() runs the makeNotation:

    ```python
    >>> tnc.postParse()
    >>> tnc.stream.show('text')
    {0.0} <music21.stream.Measure 1 offset=0.0>
        {0.0} <music21.clef.TrebleClef>
        {0.0} <music21.meter.TimeSignature 4/4>
        {0.0} <music21.note.Note C##>
        {1.0} <music21.note.Note D>
        {2.0} <music21.note.Note E->
        {2.5} <music21.note.Note F>
        {3.0} <music21.note.Note F>
        {3.5} <music21.note.Note F#>
    {4.0} <music21.stream.Measure 2 offset=4.0>
        {0.0} <music21.note.Note G>
        {1.0} <music21.note.Note F>
        {1.3333} <music21.note.Note E>
        {1.6667} <music21.note.Note D>
        {2.0} <music21.note.Note C>
        {4.0} <music21.bar.Barline type=final>
    ```

    Let’s look at edge cases. Normally, invalid notes or
    other bad tokens pass freely by dropping the unparseable token.
    Here 3 is not a valid duration, so d3 will be dropped.

    ```python
    >>> x = converter.parse('tinyNotation: 4/4 c2 d3 e2')
    >>> x.show('text')
    {0.0} <music21.stream.Measure 1 offset=0.0>
        {0.0} <music21.clef.TrebleClef>
        {0.0} <music21.meter.TimeSignature 4/4>
        {0.0} <music21.note.Note C>
        {2.0} <music21.note.Note E>
        {4.0} <music21.bar.Barline type=final>
    ```

    But with the keyword ‘raiseExceptions=True’ a TinyNotationException
    is raised if any token cannot be parsed.

    ```python
    >>> x = converter.parse('tinyNotation: 4/4 c2 d3 e2', raiseExceptions=True)
    Traceback (most recent call last):
    music21.tinyNotation.TinyNotationException: Could not parse token: 'd3'
    ```

[`Converter`](#music21.tinyNotation.Converter "music21.tinyNotation.Converter") methods

Converter.load(*stringRep: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/tinyNotation.html#Converter.load)
:   Loads a stringRepresentation into .stringRep
    and resets the parsing state.

    ```python
    >>> tnc = tinyNotation.Converter()
    >>> tnc.load('4/4 c2 d e f')
    >>> s = tnc.parse().stream
    >>> tnc.load('4/4 f e d c')
    >>> s2 = tnc.parse().stream
    >>> ns2 = s2.flatten().notes
    ```

    Check that the duration of 2.0 from the first load did not carry over.

    ```python
    >>> ns2[0].duration.quarterLength
    1.0
    >>> len(ns2)
    4
    ```

Converter.parse()[[source]](../_modules/music21/tinyNotation.html#Converter.parse)
:   splitPreTokens, setupRegularExpressions, then runs
    through each preToken, and runs postParse.

Converter.parseEndStates(*t: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][[source]](../_modules/music21/tinyNotation.html#Converter.parseEndStates)
:   Trims the endState token (}) from the t string
    and then returns a two-tuple of the new token and number
    of states to remove:

    ```python
    >>> tnc = tinyNotation.Converter()
    >>> tnc.parseEndStates('C4')
    ('C4', 0)
    >>> tnc.parseEndStates('C4}}')
    ('C4', 2)
    ```

Converter.parseModifiers(*t*)[[source]](../_modules/music21/tinyNotation.html#Converter.parseModifiers)
:   Parses modifierEquals, modifierUnderscore, modifierStar, etc.
    for a given token and returns the modified token and a
    (possibly empty) list of activeModifiers.

    Modifiers affect only the current token. To affect
    multiple tokens, use a [`State`](#music21.tinyNotation.State "music21.tinyNotation.State") object.

Converter.parseOne(*i: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *t: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*)[[source]](../_modules/music21/tinyNotation.html#Converter.parseOne)
:   parse a single token at position i, with
    text t, possibly adding it to the stream.

    Checks for state changes, modifiers, tokens, and end-state brackets.

Converter.parseStartStates(*t: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](../_modules/music21/tinyNotation.html#Converter.parseStartStates)
:   Changes the states in self.activeStates, and starts the state given the current data.
    Returns a newly processed token.

    A contrived example:

    ```python
    >>> tnc = tinyNotation.Converter()
    >>> tnc.setupRegularExpressions()
    >>> len(tnc.activeStates)
    0
    >>> tIn = 'trip{quad{f8~'
    >>> tOut = tnc.parseStartStates(tIn)
    >>> tOut
    'f8'
    >>> len(tnc.activeStates)
    3
    >>> tripState = tnc.activeStates[0]
    >>> tripState
    <music21.tinyNotation.TripletState object at 0x10afaa630>
    ```

    ```python
    >>> quadState = tnc.activeStates[1]
    >>> quadState
    <music21.tinyNotation.QuadrupletState object at 0x10adcb0b8>
    ```

    ```python
    >>> tieState = tnc.activeStates[2]
    >>> tieState
    <music21.tinyNotation.TieState object at 0x10afab048>
    ```

    ```python
    >>> tieState.parent is tnc
    True
    >>> tieState.stateInfo
    '~'
    >>> quadState.stateInfo
    'quad{'
    ```

    Note that the affected tokens haven’t yet been added:

    ```python
    >>> tripState.affectedTokens
    []
    ```

    Unknown state gives a warning or if .raisesException=True raises a
    TinyNotationException

    ```python
    >>> tnc.raiseExceptions = True
    >>> tIn = 'blah{f8~'
    >>> tOut = tnc.parseStartStates(tIn)
    Traceback (most recent call last):
    music21.tinyNotation.TinyNotationException: Incorrect bracket state: 'blah'
    ```

Converter.postParse()[[source]](../_modules/music21/tinyNotation.html#Converter.postParse)
:   Called after all the tokens have been run.

    It currently runs .makeMeasures() on .stream unless .makeNotation is False.

Converter.setupRegularExpressions()[[source]](../_modules/music21/tinyNotation.html#Converter.setupRegularExpressions)
:   Regular expressions get compiled for faster
    usage. This is called automatically by .parse(), but can be
    called separately for testing. It is also important that it
    is not called in \_\_init\_\_ since subclasses should override the
    tokenMap, etc. for a class.

Converter.splitPreTokens()[[source]](../_modules/music21/tinyNotation.html#Converter.splitPreTokens)
:   splits the string into textual preTokens.

    Right now just splits on spaces, but might be smarter to ignore spaces in
    quotes, etc. later.

## Token

class music21.tinyNotation.Token(*token=''*)[[source]](../_modules/music21/tinyNotation.html#Token)
:   A single token made from the parser.

    Call .parse(parent) to make it work.

[`Token`](#music21.tinyNotation.Token "music21.tinyNotation.Token") methods

Token.parse(*parent*)[[source]](../_modules/music21/tinyNotation.html#Token.parse)
:   do NOT store parent – probably
    too slow

## State

class music21.tinyNotation.State(*parent: [Converter](#music21.tinyNotation.Converter "music21.tinyNotation.Converter") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *stateInfo: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](../_modules/music21/tinyNotation.html#State)
:   State tokens apply something to
    every note found within it.

    State objects can have “autoExpires” set, which is False if it does not expire
    or an integer if it expires after a certain number of tokens have been processed.

    ```python
    >>> tnc = tinyNotation.Converter()
    >>> ts = tinyNotation.TieState(tnc, '~')
    >>> isinstance(ts, tinyNotation.State)
    True
    >>> ts.autoExpires
    2
    ```

[`State`](#music21.tinyNotation.State "music21.tinyNotation.State") methods

State.affectTokenAfterParse(*m21Obj: [Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")*) → [Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")[[source]](../_modules/music21/tinyNotation.html#State.affectTokenAfterParse)
:   called to modify the tokenObj after parsing

    tokenObj may be None if another
    state has deleted it.

State.affectTokenAfterParseBeforeModifiers(*m21Obj: [Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")*) → [Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")[[source]](../_modules/music21/tinyNotation.html#State.affectTokenAfterParseBeforeModifiers)
:   called after the object has been acquired but before modifiers have been applied.

State.affectTokenBeforeParse(*tokenStr: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](../_modules/music21/tinyNotation.html#State.affectTokenBeforeParse)
:   called to modify the string of a token.

State.end() → [Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/tinyNotation.html#State.end)
:   called just after removing state

State.start()[[source]](../_modules/music21/tinyNotation.html#State.start)
:   called when the state is initiated

## Modifier

class music21.tinyNotation.Modifier(*modifierData*, *modifierString*, *parent*)[[source]](../_modules/music21/tinyNotation.html#Modifier)
:   a modifier is something that changes the current
    token, like setting the .id or Lyric.

[`Modifier`](#music21.tinyNotation.Modifier "music21.tinyNotation.Modifier") methods

Modifier.postParse(*m21Obj*)[[source]](../_modules/music21/tinyNotation.html#Modifier.postParse)
:   called after the tokenString has been
    turned into an m21Obj. m21Obj may be None

    Important: must return the m21Obj, or a different object!

Modifier.preParse(*tokenString*)[[source]](../_modules/music21/tinyNotation.html#Modifier.preParse)
:   called before the tokenString has been
    turned into an object

## IdModifier

class music21.tinyNotation.IdModifier(*modifierData*, *modifierString*, *parent*)[[source]](../_modules/music21/tinyNotation.html#IdModifier)
:   sets the .id of the m21Obj, called with = by default

[`IdModifier`](#music21.tinyNotation.IdModifier "music21.tinyNotation.IdModifier") bases

* [`Modifier`](#music21.tinyNotation.Modifier "music21.tinyNotation.Modifier")

[`IdModifier`](#music21.tinyNotation.IdModifier "music21.tinyNotation.IdModifier") methods

IdModifier.postParse(*m21Obj*)[[source]](../_modules/music21/tinyNotation.html#IdModifier.postParse)
:   called after the tokenString has been
    turned into an m21Obj. m21Obj may be None

    Important: must return the m21Obj, or a different object!

Methods inherited from [`Modifier`](#music21.tinyNotation.Modifier "music21.tinyNotation.Modifier"):

|  |  |  |
| --- | --- | --- |
| * [`preParse()`](#music21.tinyNotation.Modifier.preParse "music21.tinyNotation.Modifier.preParse") |  |  |

## LyricModifier

class music21.tinyNotation.LyricModifier(*modifierData*, *modifierString*, *parent*)[[source]](../_modules/music21/tinyNotation.html#LyricModifier)
:   sets the .lyric of the m21Obj, called with \_ by default

[`LyricModifier`](#music21.tinyNotation.LyricModifier "music21.tinyNotation.LyricModifier") bases

* [`Modifier`](#music21.tinyNotation.Modifier "music21.tinyNotation.Modifier")

[`LyricModifier`](#music21.tinyNotation.LyricModifier "music21.tinyNotation.LyricModifier") methods

LyricModifier.postParse(*m21Obj*)[[source]](../_modules/music21/tinyNotation.html#LyricModifier.postParse)
:   called after the tokenString has been
    turned into an m21Obj. m21Obj may be None

    Important: must return the m21Obj, or a different object!

Methods inherited from [`Modifier`](#music21.tinyNotation.Modifier "music21.tinyNotation.Modifier"):

|  |  |  |
| --- | --- | --- |
| * [`preParse()`](#music21.tinyNotation.Modifier.preParse "music21.tinyNotation.Modifier.preParse") |  |  |

## NoteOrRestToken

class music21.tinyNotation.NoteOrRestToken(*token=''*)[[source]](../_modules/music21/tinyNotation.html#NoteOrRestToken)
:   represents a Note or Rest. Chords are represented by Note objects

[`NoteOrRestToken`](#music21.tinyNotation.NoteOrRestToken "music21.tinyNotation.NoteOrRestToken") bases

* [`Token`](#music21.tinyNotation.Token "music21.tinyNotation.Token")

[`NoteOrRestToken`](#music21.tinyNotation.NoteOrRestToken "music21.tinyNotation.NoteOrRestToken") methods

NoteOrRestToken.applyDuration(*n*, *t*, *parent*)[[source]](../_modules/music21/tinyNotation.html#NoteOrRestToken.applyDuration)
:   takes the information in the string t and creates a Duration object for the
    note or rest n.

NoteOrRestToken.dots(*element*, *search*, *pm*, *t*, *parent*)[[source]](../_modules/music21/tinyNotation.html#NoteOrRestToken.dots)
:   adds the appropriate number of dots to the right place.

    Subclassed in TrecentoNotation where two dots has a different meaning.

NoteOrRestToken.durationType(*element*, *search*, *pm*, *t*, *parent*)[[source]](../_modules/music21/tinyNotation.html#NoteOrRestToken.durationType)
:   The result of a successful search for a duration type: puts a Duration in the right place.

Methods inherited from [`Token`](#music21.tinyNotation.Token "music21.tinyNotation.Token"):

|  |  |  |
| --- | --- | --- |
| * [`parse()`](#music21.tinyNotation.Token.parse "music21.tinyNotation.Token.parse") |  |  |

## NoteToken

class music21.tinyNotation.NoteToken(*token=''*)[[source]](../_modules/music21/tinyNotation.html#NoteToken)
:   A NoteToken represents a single Note with pitch

    ```python
    >>> c3 = tinyNotation.NoteToken('C')
    >>> c3
    <music21.tinyNotation.NoteToken object at 0x10b07bf98>
    >>> n = c3.parse()
    >>> n
    <music21.note.Note C>
    >>> n.nameWithOctave
    'C3'
    ```

    ```python
    >>> bFlat6 = tinyNotation.NoteToken("b''-")
    >>> bFlat6
    <music21.tinyNotation.NoteToken object at 0x10b07bf98>
    >>> n = bFlat6.parse()
    >>> n
    <music21.note.Note B->
    >>> n.nameWithOctave
    'B-6'
    ```

[`NoteToken`](#music21.tinyNotation.NoteToken "music21.tinyNotation.NoteToken") bases

* [`NoteOrRestToken`](#music21.tinyNotation.NoteOrRestToken "music21.tinyNotation.NoteOrRestToken")
* [`Token`](#music21.tinyNotation.Token "music21.tinyNotation.Token")

[`NoteToken`](#music21.tinyNotation.NoteToken "music21.tinyNotation.NoteToken") methods

NoteToken.editorialAccidental(*n*, *search*, *pm*, *t*)[[source]](../_modules/music21/tinyNotation.html#NoteToken.editorialAccidental)
:   indicates that the accidental is in parentheses, so set it up to be stored in ficta.

NoteToken.flats(*n*, *search*, *pm*, *t*)[[source]](../_modules/music21/tinyNotation.html#NoteToken.flats)
:   called when one or more flats have been found and calls adds
    the appropriate accidental to it.

    ```python
    >>> import re
    >>> tStr = 'BB--'
    >>> nToken = tinyNotation.NoteToken(tStr)
    >>> n = note.Note('B')
    >>> n.octave = 2
    >>> searchResult = re.search(nToken.pitchMap['flats'], tStr)
    >>> tPost = nToken.flats(n, searchResult, nToken.pitchMap['flats'], tStr)
    >>> tPost
    'BB'
    >>> n.pitch.accidental
    <music21.pitch.Accidental double-flat>
    ```

NoteToken.highOctave(*n*, *search*, *pm*, *t*)[[source]](../_modules/music21/tinyNotation.html#NoteToken.highOctave)
:   Called when a note of octave 4 or higher is encountered.

    ```python
    >>> import re
    >>> tStr = "e''"
    >>> nToken = tinyNotation.NoteToken(tStr)
    >>> n = note.Note('E')
    >>> searchResult = re.search(nToken.pitchMap['highOctave'], tStr)
    >>> tPost = nToken.highOctave(n, searchResult, nToken.pitchMap['highOctave'], tStr)
    >>> tPost
    ''
    >>> n.octave
    6
    ```

NoteToken.lowOctave(*n*, *search*, *pm*, *t*)[[source]](../_modules/music21/tinyNotation.html#NoteToken.lowOctave)
:   Called when a note of octave 3 or below is encountered.

    ```python
    >>> import re
    >>> tStr = 'BBB'
    >>> nToken = tinyNotation.NoteToken(tStr)
    >>> n = note.Note('B')
    >>> searchResult = re.search(nToken.pitchMap['lowOctave'], tStr)
    >>> tPost = nToken.lowOctave(n, searchResult, nToken.pitchMap['lowOctave'], tStr)
    >>> tPost
    ''
    >>> n.octave
    1
    ```

NoteToken.natural(*n*, *search*, *pm*, *t*)[[source]](../_modules/music21/tinyNotation.html#NoteToken.natural)
:   called when an explicit natural has been found. All pitches are natural without
    being specified, so not needed. Adds a natural accidental to it.

    ```python
    >>> import re
    >>> tStr = 'En'
    >>> nToken = tinyNotation.NoteToken(tStr)
    >>> n = note.Note('E')
    >>> n.octave = 3
    >>> searchResult = re.search(nToken.pitchMap['natural'], tStr)
    >>> tPost = nToken.natural(n, searchResult, nToken.pitchMap['natural'], tStr)
    >>> tPost
    'E'
    >>> n.pitch.accidental
    <music21.pitch.Accidental natural>
    ```

NoteToken.parse(*parent: [Converter](#music21.tinyNotation.Converter "music21.tinyNotation.Converter") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](../_modules/music21/tinyNotation.html#NoteToken.parse)
:   Extract the pitch from the note and then returns the Note.

NoteToken.processPitchMap(*n*, *t*)[[source]](../_modules/music21/tinyNotation.html#NoteToken.processPitchMap)
:   processes the pitchMap on the object.

NoteToken.sharps(*n*, *search*, *pm*, *t*)[[source]](../_modules/music21/tinyNotation.html#NoteToken.sharps)
:   called when one or more sharps have been found and adds the appropriate accidental to it.

    ```python
    >>> import re
    >>> tStr = 'C##'
    >>> nToken = tinyNotation.NoteToken(tStr)
    >>> n = note.Note('C')
    >>> n.octave = 3
    >>> searchResult = re.search(nToken.pitchMap['sharps'], tStr)
    >>> tPost = nToken.sharps(n, searchResult, nToken.pitchMap['sharps'], tStr)
    >>> tPost
    'C'
    >>> n.pitch.accidental
    <music21.pitch.Accidental double-sharp>
    ```

Methods inherited from [`NoteOrRestToken`](#music21.tinyNotation.NoteOrRestToken "music21.tinyNotation.NoteOrRestToken"):

|  |  |  |
| --- | --- | --- |
| * [`applyDuration()`](#music21.tinyNotation.NoteOrRestToken.applyDuration "music21.tinyNotation.NoteOrRestToken.applyDuration") | * [`dots()`](#music21.tinyNotation.NoteOrRestToken.dots "music21.tinyNotation.NoteOrRestToken.dots") | * [`durationType()`](#music21.tinyNotation.NoteOrRestToken.durationType "music21.tinyNotation.NoteOrRestToken.durationType") |

## QuadrupletState

class music21.tinyNotation.QuadrupletState(*parent: [Converter](#music21.tinyNotation.Converter "music21.tinyNotation.Converter") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *stateInfo: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](../_modules/music21/tinyNotation.html#QuadrupletState)
:   a 4:3 tuplet

[`QuadrupletState`](#music21.tinyNotation.QuadrupletState "music21.tinyNotation.QuadrupletState") bases

* [`TupletState`](#music21.tinyNotation.TupletState "music21.tinyNotation.TupletState")
* [`State`](#music21.tinyNotation.State "music21.tinyNotation.State")

[`QuadrupletState`](#music21.tinyNotation.QuadrupletState "music21.tinyNotation.QuadrupletState") methods

Methods inherited from [`TupletState`](#music21.tinyNotation.TupletState "music21.tinyNotation.TupletState"):

|  |  |  |
| --- | --- | --- |
| * [`affectTokenAfterParse()`](#music21.tinyNotation.TupletState.affectTokenAfterParse "music21.tinyNotation.TupletState.affectTokenAfterParse") | * [`end()`](#music21.tinyNotation.TupletState.end "music21.tinyNotation.TupletState.end") |  |

Methods inherited from [`State`](#music21.tinyNotation.State "music21.tinyNotation.State"):

|  |  |  |
| --- | --- | --- |
| * [`affectTokenAfterParseBeforeModifiers()`](#music21.tinyNotation.State.affectTokenAfterParseBeforeModifiers "music21.tinyNotation.State.affectTokenAfterParseBeforeModifiers") | * [`affectTokenBeforeParse()`](#music21.tinyNotation.State.affectTokenBeforeParse "music21.tinyNotation.State.affectTokenBeforeParse") | * [`start()`](#music21.tinyNotation.State.start "music21.tinyNotation.State.start") |

## RestToken

class music21.tinyNotation.RestToken(*token=''*)[[source]](../_modules/music21/tinyNotation.html#RestToken)
:   A token starting with ‘r’, representing a rest.

[`RestToken`](#music21.tinyNotation.RestToken "music21.tinyNotation.RestToken") bases

* [`NoteOrRestToken`](#music21.tinyNotation.NoteOrRestToken "music21.tinyNotation.NoteOrRestToken")
* [`Token`](#music21.tinyNotation.Token "music21.tinyNotation.Token")

[`RestToken`](#music21.tinyNotation.RestToken "music21.tinyNotation.RestToken") methods

RestToken.parse(*parent: [Converter](#music21.tinyNotation.Converter "music21.tinyNotation.Converter") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](../_modules/music21/tinyNotation.html#RestToken.parse)
:   do NOT store parent – probably
    too slow

Methods inherited from [`NoteOrRestToken`](#music21.tinyNotation.NoteOrRestToken "music21.tinyNotation.NoteOrRestToken"):

|  |  |  |
| --- | --- | --- |
| * [`applyDuration()`](#music21.tinyNotation.NoteOrRestToken.applyDuration "music21.tinyNotation.NoteOrRestToken.applyDuration") | * [`dots()`](#music21.tinyNotation.NoteOrRestToken.dots "music21.tinyNotation.NoteOrRestToken.dots") | * [`durationType()`](#music21.tinyNotation.NoteOrRestToken.durationType "music21.tinyNotation.NoteOrRestToken.durationType") |

## TieState

class music21.tinyNotation.TieState(*parent: [Converter](#music21.tinyNotation.Converter "music21.tinyNotation.Converter") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *stateInfo: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](../_modules/music21/tinyNotation.html#TieState)
:   A TieState is an auto-expiring state that applies a tie start to this note and a
    tie stop to the next note.

[`TieState`](#music21.tinyNotation.TieState "music21.tinyNotation.TieState") bases

* [`State`](#music21.tinyNotation.State "music21.tinyNotation.State")

[`TieState`](#music21.tinyNotation.TieState "music21.tinyNotation.TieState") methods

TieState.end()[[source]](../_modules/music21/tinyNotation.html#TieState.end)
:   end the tie state by applying tie ties to the appropriate notes

Methods inherited from [`State`](#music21.tinyNotation.State "music21.tinyNotation.State"):

|  |  |  |
| --- | --- | --- |
| * [`affectTokenAfterParse()`](#music21.tinyNotation.State.affectTokenAfterParse "music21.tinyNotation.State.affectTokenAfterParse") * [`affectTokenAfterParseBeforeModifiers()`](#music21.tinyNotation.State.affectTokenAfterParseBeforeModifiers "music21.tinyNotation.State.affectTokenAfterParseBeforeModifiers") | * [`affectTokenBeforeParse()`](#music21.tinyNotation.State.affectTokenBeforeParse "music21.tinyNotation.State.affectTokenBeforeParse") | * [`start()`](#music21.tinyNotation.State.start "music21.tinyNotation.State.start") |

## TimeSignatureToken

class music21.tinyNotation.TimeSignatureToken(*token=''*)[[source]](../_modules/music21/tinyNotation.html#TimeSignatureToken)
:   Represents a single time signature, like 1/4

[`TimeSignatureToken`](#music21.tinyNotation.TimeSignatureToken "music21.tinyNotation.TimeSignatureToken") bases

* [`Token`](#music21.tinyNotation.Token "music21.tinyNotation.Token")

[`TimeSignatureToken`](#music21.tinyNotation.TimeSignatureToken "music21.tinyNotation.TimeSignatureToken") methods

TimeSignatureToken.parse(*parent*)[[source]](../_modules/music21/tinyNotation.html#TimeSignatureToken.parse)
:   do NOT store parent – probably
    too slow

## TripletState

class music21.tinyNotation.TripletState(*parent: [Converter](#music21.tinyNotation.Converter "music21.tinyNotation.Converter") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *stateInfo: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](../_modules/music21/tinyNotation.html#TripletState)
:   a 3:2 tuplet

[`TripletState`](#music21.tinyNotation.TripletState "music21.tinyNotation.TripletState") bases

* [`TupletState`](#music21.tinyNotation.TupletState "music21.tinyNotation.TupletState")
* [`State`](#music21.tinyNotation.State "music21.tinyNotation.State")

[`TripletState`](#music21.tinyNotation.TripletState "music21.tinyNotation.TripletState") methods

Methods inherited from [`TupletState`](#music21.tinyNotation.TupletState "music21.tinyNotation.TupletState"):

|  |  |  |
| --- | --- | --- |
| * [`affectTokenAfterParse()`](#music21.tinyNotation.TupletState.affectTokenAfterParse "music21.tinyNotation.TupletState.affectTokenAfterParse") | * [`end()`](#music21.tinyNotation.TupletState.end "music21.tinyNotation.TupletState.end") |  |

Methods inherited from [`State`](#music21.tinyNotation.State "music21.tinyNotation.State"):

|  |  |  |
| --- | --- | --- |
| * [`affectTokenAfterParseBeforeModifiers()`](#music21.tinyNotation.State.affectTokenAfterParseBeforeModifiers "music21.tinyNotation.State.affectTokenAfterParseBeforeModifiers") | * [`affectTokenBeforeParse()`](#music21.tinyNotation.State.affectTokenBeforeParse "music21.tinyNotation.State.affectTokenBeforeParse") | * [`start()`](#music21.tinyNotation.State.start "music21.tinyNotation.State.start") |

## TupletState

class music21.tinyNotation.TupletState(*parent: [Converter](#music21.tinyNotation.Converter "music21.tinyNotation.Converter") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *stateInfo: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](../_modules/music21/tinyNotation.html#TupletState)
:   a tuplet state applies tuplets to notes while parsing and sets ‘start’ and ‘stop’
    on the first and last note when end is called.

[`TupletState`](#music21.tinyNotation.TupletState "music21.tinyNotation.TupletState") bases

* [`State`](#music21.tinyNotation.State "music21.tinyNotation.State")

[`TupletState`](#music21.tinyNotation.TupletState "music21.tinyNotation.TupletState") methods

TupletState.affectTokenAfterParse(*n*)[[source]](../_modules/music21/tinyNotation.html#TupletState.affectTokenAfterParse)
:   puts a tuplet on the note

TupletState.end()[[source]](../_modules/music21/tinyNotation.html#TupletState.end)
:   end a tuplet by putting start on the first note and stop on the last.

Methods inherited from [`State`](#music21.tinyNotation.State "music21.tinyNotation.State"):

|  |  |  |
| --- | --- | --- |
| * [`affectTokenAfterParseBeforeModifiers()`](#music21.tinyNotation.State.affectTokenAfterParseBeforeModifiers "music21.tinyNotation.State.affectTokenAfterParseBeforeModifiers") | * [`affectTokenBeforeParse()`](#music21.tinyNotation.State.affectTokenBeforeParse "music21.tinyNotation.State.affectTokenBeforeParse") | * [`start()`](#music21.tinyNotation.State.start "music21.tinyNotation.State.start") |
