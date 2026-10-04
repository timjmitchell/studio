Source: https://music21.org/music21docs/moduleReference/moduleBrailleExamples.html

# music21.braille.examples

The melody to the “Happy Birthday” song, in G major and 3/4 time.

```python
>>> from music21.braille import examples
>>> hb = examples.happyBirthday()
>>> hb.show('braille')
⠀⠀⠀⠀⠀⠀⠠⠃⠗⠊⠛⠓⠞⠇⠽⠲⠀⠹⠶⠼⠁⠃⠚⠀⠩⠼⠉⠲⠀⠀⠀⠀⠀⠀
⠼⠁⠀⠐⠑⠄⠵⠫⠱⠀⠳⠟⠀⠑⠄⠵⠫⠱⠀⠪⠗⠀⠑⠄⠵⠨⠱⠺⠀⠓⠄⠷⠻⠫
⠀⠀⠨⠙⠄⠽⠺⠳⠀⠪⠗⠣⠅
```

A piano reduction of Giuseppi Verdi’s famous aria from the opera
Rigoletto, “La Donna É Mobile,” in Bb major and 3/8 time.

```python
>>> verdi = corpus.parse('verdi/laDonnaEMobile')
>>> verdi.show('braille')
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠣⠣⠼⠉⠦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠁⠀⠨⠜⠄⠜⠁⠇⠇⠑⠛⠗⠑⠞⠞⠕⠜⠋⠄⠍⠀⠦⠨⠑⠦⠑⠦⠑⠀⠀
⠀⠀⠀⠸⠜⠘⠚⠸⠛⠼⠴⠛⠼⠴⠀⠀⠀⠀⠀⠀⠀⠀⠘⠚⠸⠛⠼⠴⠛⠼⠴
⠀⠉⠀⠨⠜⠨⠦⠨⠿⠄⠉⠏⠉⠹⠀⠀⠀⠀⠀⠀⠀⠨⠙⠙⠙⠀⠀⠀⠀⠀
⠀⠀⠀⠸⠜⠄⠄⠭⠸⠛⠬⠒⠛⠬⠒⠣⠜⠘⠻⠄⠀⠘⠛⠸⠛⠬⠒⠛⠬⠒
⠀⠑⠀⠨⠜⠨⠦⠨⠯⠄⠉⠕⠉⠺⠀⠀⠀⠀⠀⠀⠀⠦⠨⠑⠦⠙⠦⠚⠀⠀
⠀⠀⠀⠸⠜⠄⠄⠭⠸⠛⠼⠴⠛⠼⠴⠣⠜⠘⠻⠄⠀⠘⠛⠸⠛⠼⠴⠛⠼⠴
⠀⠛⠀⠨⠜⠐⠾⠄⠉⠎⠪⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠨⠙⠉⠚⠉⠓⠀⠀⠀
⠀⠀⠀⠸⠜⠄⠄⠭⠸⠛⠔⠒⠛⠔⠒⠣⠜⠘⠻⠄⠀⠘⠛⠸⠛⠔⠒⠛⠔⠒
⠀⠊⠀⠨⠜⠐⠷⠄⠉⠟⠻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠜⠋⠋⠄⠦⠨⠑⠦⠑⠦⠑
⠀⠀⠀⠸⠜⠄⠄⠭⠸⠛⠼⠴⠛⠼⠴⠣⠜⠘⠺⠄⠀⠘⠾⠸⠛⠾⠬⠛⠾⠬⠛⠀
⠁⠁⠀⠨⠜⠨⠦⠨⠿⠄⠉⠏⠉⠹⠀⠀⠀⠀⠀⠀⠀⠀⠨⠙⠙⠙⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠸⠜⠄⠄⠍⠸⠿⠮⠔⠿⠮⠔⠿⠣⠜⠘⠻⠄⠀⠘⠿⠸⠛⠮⠔⠛⠮⠔⠛
⠁⠉⠀⠨⠜⠨⠦⠨⠯⠄⠉⠕⠉⠺⠀⠀⠀⠀⠀⠀⠀⠀⠦⠨⠑⠉⠦⠙⠉⠦⠚⠀
⠀⠀⠀⠸⠜⠄⠄⠍⠸⠿⠾⠬⠿⠾⠬⠿⠣⠜⠘⠺⠄⠀⠘⠾⠸⠛⠾⠬⠛⠾⠬⠛
⠁⠑⠀⠨⠜⠐⠾⠄⠉⠎⠪⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠨⠙⠉⠚⠉⠓⠀⠀⠀⠀
⠀⠀⠀⠸⠜⠄⠄⠍⠸⠿⠮⠔⠿⠮⠔⠿⠣⠜⠘⠻⠄⠀⠘⠿⠸⠛⠮⠔⠛⠮⠔⠛
⠁⠛⠀⠨⠜⠐⠷⠄⠉⠟⠻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠨⠽⠄⠉⠕⠉⠙⠙⠀⠀⠀
⠀⠀⠀⠸⠜⠄⠄⠍⠸⠿⠾⠬⠿⠾⠬⠿⠣⠜⠘⠺⠄⠀⠜⠍⠋⠸⠋⠓⠬⠼⠓⠬⠼
⠁⠊⠀⠨⠜⠨⠿⠴⠍⠹⠬⠔⠀⠀⠀⠀⠀⠀⠀⠨⠵⠄⠉⠏⠉⠑⠑⠀⠀⠡⠨⠷⠴⠍⠱⠬⠔⠀⠀⠀
⠀⠀⠀⠸⠜⠄⠄⠭⠸⠊⠬⠊⠬⠣⠜⠸⠻⠄⠀⠣⠸⠓⠊⠬⠼⠊⠬⠼⠀⠭⠸⠚⠬⠚⠬⠣⠜⠸⠳⠄
⠃⠃⠀⠨⠜⠨⠿⠄⠉⠗⠉⠛⠛⠀⠜⠋⠋⠨⠳⠴⠛⠀⠦⠨⠯⠦⠿⠦⠯⠵⠍⠽⠍⠀⠀
⠀⠀⠀⠸⠜⠸⠊⠙⠬⠼⠙⠬⠼⠀⠸⠺⠄⠬⠀⠀⠀⠀⠸⠯⠬⠴⠍⠿⠼⠴⠍⠿⠬⠒⠍
⠃⠑⠀⠨⠜⠐⠺⠜⠍⠋⠨⠿⠄⠉⠰⠟⠀⠰⠻⠨⠿⠄⠉⠰⠟⠣⠜⠧⠄⠀
⠀⠀⠀⠸⠜⠸⠚⠬⠚⠬⠭⠀⠀⠀⠀⠀⠀⠭⠸⠛⠬⠔⠭⠣⠜⠸⠻⠄⠬⠔
⠃⠛⠀⠨⠜⠰⠻⠨⠿⠄⠉⠰⠟⠀⠀⠀⠀⠀⠀⠰⠯⠿⠯⠦⠵⠍⠦⠽⠍⠀⠀⠀
⠀⠀⠀⠸⠜⠄⠄⠭⠸⠚⠬⠭⠣⠜⠸⠺⠄⠬⠀⠸⠯⠬⠴⠍⠿⠼⠴⠍⠿⠬⠒⠍
⠃⠊⠀⠨⠜⠨⠺⠜⠋⠨⠿⠄⠉⠰⠟⠀⠀⠀⠰⠯⠉⠨⠮⠉⠰⠿⠉⠋⠨⠿⠄⠉⠰⠟⠣⠜⠧⠄
⠀⠀⠀⠸⠜⠘⠾⠸⠿⠼⠴⠛⠼⠴⠛⠼⠴⠀⠭⠸⠛⠬⠒⠛⠬⠒⠣⠜⠘⠻⠄⠀⠀⠀⠀⠀⠀⠀
⠉⠁⠀⠨⠜⠰⠵⠉⠨⠿⠉⠰⠿⠉⠑⠨⠿⠄⠉⠰⠟
⠀⠀⠀⠸⠜⠄⠄⠭⠸⠛⠼⠴⠛⠼⠴⠣⠜⠘⠻⠄⠀
⠉⠃⠀⠨⠜⠰⠃⠆⠰⠯⠨⠮⠰⠿⠯⠨⠮⠰⠿⠯⠨⠮⠰⠿⠀⠨⠚⠘⠆⠭⠩⠛
⠀⠀⠀⠸⠜⠘⠛⠸⠛⠔⠒⠛⠔⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠚⠬⠧⠀⠀⠀
⠉⠙⠀⠨⠜⠄⠜⠋⠋⠰⠃⠨⠦⠨⠮⠄⠗⠿⠄⠏⠵⠄⠝⠀⠐⠾⠘⠆⠍⠜⠋⠋⠋⠨⠚⠼⠴⠭⠣⠅
⠀⠀⠀⠸⠜⠄⠄⠄⠧⠸⠛⠬⠒⠣⠜⠸⠫⠄⠬⠴⠀⠀⠀⠀⠸⠾⠬⠍⠘⠚⠬⠔⠭⠣⠅⠀⠀⠀⠀⠀
```

The exposition to movement 1 of Mozart’s K545.

```python
>>> mozart = converter.parse('mozart_k545_exposition.xml')
>>> mozart.show('braille')
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠼⠙⠲⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠁⠀⠨⠜⠄⠜⠁⠇⠇⠑⠛⠗⠕⠨⠝⠫⠳⠀⠐⠺⠄⠉⠽⠉⠵⠹⠧⠀⠨⠎⠳⠰⠹⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠸⠜⠐⠙⠓⠋⠓⠙⠓⠋⠓⠀⠀⠀⠀⠀⠐⠑⠓⠛⠓⠙⠓⠋⠓⠀⠐⠙⠐⠊⠛⠊⠐⠙⠓⠋⠓
⠀⠙⠀⠨⠜⠨⠳⠛⠉⠯⠉⠿⠫⠧⠀⠀⠐⠊⠾⠽⠵⠋⠛⠓⠮⠓⠛⠋⠵⠙⠚⠊
⠀⠀⠀⠸⠜⠸⠚⠐⠓⠑⠓⠙⠓⠋⠓⠀⠐⠻⠧⠧⠸⠻⠔⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠋⠀⠨⠜⠐⠓⠮⠾⠽⠑⠋⠛⠷⠛⠋⠑⠽⠚⠊⠓⠀⠐⠛⠷⠮⠾⠙⠑⠋⠿⠋⠑⠙⠾⠊⠓⠛
⠀⠀⠀⠸⠜⠸⠫⠴⠧⠧⠫⠴⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠱⠴⠧⠧⠱⠴⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠓⠀⠨⠜⠐⠋⠿⠷⠮⠚⠙⠑⠯⠑⠙⠚⠮⠓⠛⠋⠀⠐⠑⠯⠿⠷⠊⠚⠩⠙⠵⠐⠊⠚⠙⠵⠋⠛⠓
⠀⠀⠀⠸⠜⠸⠹⠤⠧⠧⠹⠬⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠿⠬⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠁⠚⠀⠨⠜⠨⠮⠚⠙⠚⠮⠓⠛⠋⠿⠓⠊⠓⠿⠋⠑⠙
⠀⠀⠀⠸⠜⠸⠻⠄⠓⠪⠄⠩⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠁⠁⠀⠨⠜⠐⠚⠨⠓⠋⠙⠑⠓⠋⠙⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠨⠱⠳⠼⠴⠐⠳⠧⠣⠅
⠀⠀⠀⠸⠜⠘⠷⠚⠑⠓⠘⠷⠸⠙⠋⠓⠘⠷⠚⠑⠓⠘⠷⠸⠙⠋⠓⠀⠘⠳⠸⠳⠘⠳⠧⠣⠅⠀
```

```python
>>> print(braille.translate.objectToBraille(verdi.measures(1, 3), debug=True))
---begin grand segment---
<music21.braille.segment BrailleGrandSegment>
===
Measure 1 Right, Signature Grouping 1:
Key Signature 2 flat(s) ⠣⠣
Time Signature 3/8 ⠼⠉⠦

Measure 1 Left, Signature Grouping 1:
B- major
<music21.meter.TimeSignature 3/8>
====
Measure 1 Right, Note Grouping 1:
<music21.clef.TrebleClef>
Word ⠜
Text Expression Allegretto ⠁⠇⠇⠑⠛⠗⠑⠞⠞⠕
Word: ⠜
Dynamic f ⠋
Dot 3 ⠄
Rest whole ⠍

Measure 1 Left, Note Grouping 1:
<music21.clef.BassClef>
Octave 2 ⠘
B eighth ⠚
Ascending Chord:
Octave 3 ⠸
F eighth ⠛
Interval 4 ⠼
Interval 6 ⠴
Ascending Chord:
F eighth ⠛
Interval 4 ⠼
Interval 6 ⠴
** Grouping x 2 **
====
Measure 2 Right, Note Grouping 1:
Articulation staccato ⠦
Octave 5 ⠨
D eighth ⠑
Articulation staccato ⠦
D eighth ⠑
Articulation staccato ⠦
D eighth ⠑

====
Measure 3 Right, Note Grouping 1:
Articulation accent ⠨⠦
Octave 5 ⠨
F 16th ⠿
Dot ⠄
Opening single slur ⠉
E 32nd ⠏
Opening single slur ⠉
C quarter ⠹

Measure 3 Left, Inaccord Grouping 1:
Rest eighth ⠭
Ascending Chord:
Octave 3 ⠸
F eighth ⠛
Interval 3 ⠬
Interval 7 ⠒
Ascending Chord:
F eighth ⠛
Interval 3 ⠬
Interval 7 ⠒
full inaccord ⠣⠜
Octave 2 ⠘
F quarter ⠻
Dot ⠄
====

---end grand segment---
```

## Functions

music21.braille.examples.cp(*strIn*)[[source]](../_modules/music21/braille/examples.html#cp)

music21.braille.examples.happyBirthday()[[source]](../_modules/music21/braille/examples.html#happyBirthday)
:   fully copyright free!
