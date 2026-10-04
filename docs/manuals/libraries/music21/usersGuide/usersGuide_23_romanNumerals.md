Source: https://music21.org/music21docs/usersGuide/usersGuide_23_romanNumerals.html

# User’s Guide, Chapter 23: Roman Numeral Analysis

F major is a chord that has the notes F, A, and usually C. Those notes,
placed in the same octave, instrument, dynamics, etc., should have
basically the same acoustical properties each time they’re played, but
human perception of this chord can seem to vary dramatically depending
on the context the chord is placed in. One of the most powerful contexts
that can give the same isolated sound remarkably different meanings
comes from its surrounding key.

Roman numeral analysis is a way to identify certain similarities in
tonal music (whether classical, folk, or popular) that have
traditionally been assigned to different chords that appear on the same
scale degrees in different keys.

Note

For a basic introduction to Roman numeral analysis, see
the strong [Wikipedia article](https://en.wikipedia.org/wiki/Roman_numeral_analysis)
or, for a quick review, the great PDF cheatsheet
at [“Learn Music Theory”](https://learnmusictheory.net/PDFs/pdffiles/01-05-02-RomanNumerals.pdf)

Let’s create an F-major chord but convert it to roman numerals in a few
different contexts by creating different key objects. First the setup:

```python
from music21 import *
f = chord.Chord('F4 C5 A5')
kf = key.Key('F')
sf = stream.Measure([kf, f])
sf.show()
```

[![../_images/usersGuide_23_romanNumerals_4_0.png](../_images/usersGuide_23_romanNumerals_4_0.png)](../_images/usersGuide_23_romanNumerals_4_0.png)

```python
kc = key.Key('C')
sc = stream.Part([kc, f])
sc.show()
```

[![../_images/usersGuide_23_romanNumerals_5_0.png](../_images/usersGuide_23_romanNumerals_5_0.png)](../_images/usersGuide_23_romanNumerals_5_0.png)

```python
kb = key.Key('B')
sb = stream.Part([kb, f])
sb.show()
```

[![../_images/usersGuide_23_romanNumerals_6_0.png](../_images/usersGuide_23_romanNumerals_6_0.png)](../_images/usersGuide_23_romanNumerals_6_0.png)

Now that we have four different keys, let’s create Roman numerals from
the F major chord and each of the keys. We will use a function from the
[music21.roman](../moduleReference/moduleRoman.html#moduleroman) module called
[`romanNumeralFromChord()`](../moduleReference/moduleRoman.html#music21.roman.romanNumeralFromChord "music21.roman.romanNumeralFromChord") (which we saw briefly in
[Chapter 10](usersGuide_10_examples1.html#usersguide-10-examples1)). We pass to this function
a `Chord` object and a `Key` object.

```python
rf = roman.romanNumeralFromChord(f, kf)
rf
```

```python
 <music21.roman.RomanNumeral I in F major>
```

```python
rc = roman.romanNumeralFromChord(f, kc)
rc
```

```python
 <music21.roman.RomanNumeral IV in C major>
```

`Music21` tries its best to find a Roman numeral for almost any
combination of chord and key, even if, like in B major:

```python
rb = roman.romanNumeralFromChord(f, kb)
rb
```

```python
 <music21.roman.RomanNumeral bV in B major>
```

Each [`RomanNumeral`](../moduleReference/moduleRoman.html#music21.roman.RomanNumeral "music21.roman.RomanNumeral") object has some common
properties, such as `.figure`, `.figureAndKey`,
`.romanNumeralAlone`, `.key`, and `.scaleDegree`:

```python
(rf.figure, rc.figure, rb.figure)
```

```python
 ('I', 'IV', 'bV')
```

```python
rf.figureAndKey
```

```python
 'I in F major'
```

```python
(rf.romanNumeralAlone, rc.romanNumeralAlone, rb.romanNumeralAlone)
```

```python
 ('I', 'IV', 'V')
```

```python
(rf.key, rc.key, rb.key)
```

```python
 (<music21.key.Key of F major>,
  <music21.key.Key of C major>,
  <music21.key.Key of B major>)
```

```python
(rf.scaleDegree, rc.scaleDegree, rb.scaleDegree)
```

```python
 (1, 4, 5)
```

Note that in the last case, the scale degree is the uninflected degree –
the flat sign isn’t included in the `.scaleDegree` tag. For that, use
`.scaleDegreeWithAlteration`

```python
rf.scaleDegreeWithAlteration
```

```python
 (1, None)
```

```python
rb.scaleDegreeWithAlteration
```

```python
 (5, <music21.pitch.Accidental flat>)
```

Or look at the `.frontAlterationString`,
`frontAlterationAccidental`, and `frontAlterationTransposeInterval`

```python
rb.frontAlterationString
```

```python
 'b'
```

```python
rb.frontAlterationAccidental
```

```python
 <music21.pitch.Accidental flat>
```

```python
rb.frontAlterationTransposeInterval
```

```python
 <music21.interval.Interval d1>
```

Of course, some RomanNumerals make more sense than others, so there’s a
`.functionalityScore` which returns a number from 0 to 100 as a rough
approximation of how “functional” this chord is:

```python
(rf.functionalityScore, rc.functionalityScore, rb.functionalityScore)
```

```python
 (100, 59, 0)
```

As I hinted at above, `RomanNumeral` objects are `Music21Objects` so
they can be put into Streams and showed:

```python
s = stream.Measure()
s.insert(0, rf)
s.show()
```

[![../_images/usersGuide_23_romanNumerals_28_0.png](../_images/usersGuide_23_romanNumerals_28_0.png)](../_images/usersGuide_23_romanNumerals_28_0.png)

Note that the spacing of the roman numeral is preserved from the chord
that it was converted from. If we create a `RomanNumeral` object
directly, then it is created in closed position above a tonic note in
octave 4:

```python
rf2 = roman.RomanNumeral('I', kf)
rf2
```

```python
 <music21.roman.RomanNumeral I in F major>
```

```python
rf2.show()
```

[![../_images/usersGuide_23_romanNumerals_31_0.png](../_images/usersGuide_23_romanNumerals_31_0.png)](../_images/usersGuide_23_romanNumerals_31_0.png)

It is possible to pass in just a roman numeral (“I”, “ii”, “iii”, “IV”,
etc.) and a string (“C” = C major, “c” = c minor) to create a
RomanNumeral object:

```python
subDom7 = roman.RomanNumeral('IV7', 'B-')
subDom7.show()
```

[![../_images/usersGuide_23_romanNumerals_33_0.png](../_images/usersGuide_23_romanNumerals_33_0.png)](../_images/usersGuide_23_romanNumerals_33_0.png)

```python
e65 = roman.RomanNumeral('ii65', 'E')
e65.show()
```

[![../_images/usersGuide_23_romanNumerals_34_0.png](../_images/usersGuide_23_romanNumerals_34_0.png)](../_images/usersGuide_23_romanNumerals_34_0.png)

For these romanNumerals, there is information after the
`.romanNumeralAlone` this can be found as a string in
`.figuresWritten`:

```python
(subDom7.figuresWritten, e65.figuresWritten)
```

```python
 ('7', '65')
```

These numbers can also be found as part of a more powerful
`figuredBass.Notation` object (to be discussed later) in the
`.figuresNotationObj` attribute:

```python
(subDom7.figuresNotationObj, e65.figuresNotationObj)
```

```python
 (<music21.figuredBass.notation.Notation 7>,
  <music21.figuredBass.notation.Notation 6,5>)
```

```python
e65.figuresNotationObj.numbers
```

```python
 (6, 5, 3)
```

Many of these properties can be changed:

```python
rf.key = key.Key('D')
rf.show()
```

[![../_images/usersGuide_23_romanNumerals_41_0.png](../_images/usersGuide_23_romanNumerals_41_0.png)](../_images/usersGuide_23_romanNumerals_41_0.png)

Changing the key removes any information about pitch spacing. You can’t
have everything. :-)

We’ll put the key of F back and the original pitches before we forget:

```python
rf = roman.romanNumeralFromChord(f, kf)
```

## RomanNumerals as Chords

A `RomanNumeral` object is a subclass of a Chord object, therefore we
can do everything with them that we could do with a chord. For instance:

```python
rf.isMajorTriad()
```

```python
 True
```

```python
rfc = rf.closedPosition()
rfc.show()
```

[![../_images/usersGuide_23_romanNumerals_47_0.png](../_images/usersGuide_23_romanNumerals_47_0.png)](../_images/usersGuide_23_romanNumerals_47_0.png)

```python
rb.lyric = rb.figure
rb.show()
```

[![../_images/usersGuide_23_romanNumerals_48_0.png](../_images/usersGuide_23_romanNumerals_48_0.png)](../_images/usersGuide_23_romanNumerals_48_0.png)

```python
(rf.quality, rc.quality, rb.quality)
```

```python
 ('major', 'major', 'major')
```

```python
e65.inversion()
```

```python
 1
```

```python
e65.primeForm
```

```python
 [0, 3, 5, 8]
```

```python
e65.semitonesFromChordStep(7)
```

```python
 10
```

That’s all we have for RomanNumerals for now – we will return to
RomanNumeral like objects later when we look at other Harmony objects
such as ChordSymbols and FiguredBass and we look at the romanText
module. But we’ll take a break from musical objects and get acquainted a
bit better with how your system works when running `music21` with a
look at [Chapter 24, Environment](usersGuide_24_environment.html#usersguide-24-environment).
