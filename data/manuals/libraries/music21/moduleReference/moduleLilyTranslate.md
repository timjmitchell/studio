Source: https://music21.org/music21docs/moduleReference/moduleLilyTranslate.html

# music21.lily.translate

music21 translates to Lilypond format and if Lilypond is installed on the
local computer, can automatically generate .pdf, .png, and .svg versions
of musical files using Lilypond.

## LilypondConverter

class music21.lily.translate.LilypondConverter[[source]](../_modules/music21/lily/translate.html#LilypondConverter)

[`LilypondConverter`](#music21.lily.translate.LilypondConverter "music21.lily.translate.LilypondConverter") methods

LilypondConverter.appendBeamCode(*noteOrChord*)[[source]](../_modules/music21/lily/translate.html#LilypondConverter.appendBeamCode)
:   Adds an LyEmbeddedScm object to the context’s contents if the object’s has a .beams
    attribute.

    ```python
    >>> lpc = lily.translate.LilypondConverter()
    >>> lpMusicList = lily.lilyObjects.LyMusicList()
    >>> lpc.context = lpMusicList
    >>> lpc.context.contents
    []
    >>> n1 = note.Note(quarterLength=0.25)
    >>> n2 = note.Note(quarterLength=0.25)
    >>> n1.beams.fill(2, 'start')
    >>> n2.beams.fill(2, 'stop')
    ```

    ```python
    >>> lpc.appendBeamCode(n1)
    >>> print(lpc.context.contents)
    [<music21.lily.lilyObjects.LyEmbeddedScm \set stemR...>]
    >>> print(lpc.context)
    \set stemRightBeamCount = #2
    ```

    ```python
    >>> lpc = lily.translate.LilypondConverter()
    >>> lpMusicList = lily.lilyObjects.LyMusicList()
    >>> lpc.context = lpMusicList
    >>> lpc.context.contents
    []
    >>> lpc.appendBeamCode(n2)
    >>> print(lpc.context.contents)
    [<music21.lily.lilyObjects.LyEmbeddedScm \set stemL...>]
    >>> print(lpc.context)
    \set stemLeftBeamCount = #2
    ```

LilypondConverter.appendContextFromChord(*chord*)[[source]](../_modules/music21/lily/translate.html#LilypondConverter.appendContextFromChord)
:   appends lySimpleMusicFromChord to the
    current context.

    ```python
    >>> c = chord.Chord(['C4', 'E4', 'G4'])
    >>> lpc = lily.translate.LilypondConverter()
    >>> lpMusicList = lily.lilyObjects.LyMusicList()
    >>> lpc.context = lpMusicList
    >>> lpc.appendContextFromChord(c)
    >>> print(lpMusicList)
    < c' e' g'  > 4
    ```

    ```python
    >>> c2 = chord.Chord(['D4', 'F#4', 'A4'])
    >>> c2.duration.quarterLength = 1/3
    >>> c2.duration.tuplets[0].type = 'start'
    >>> c3 = chord.Chord(['D4', 'F4', 'G4'])
    >>> c3.duration.quarterLength = 1/3
    >>> c4 = chord.Chord(['C4', 'E4', 'G4', 'C5'])
    >>> c4.duration.quarterLength = 1/3
    >>> c4.duration.tuplets[0].type = 'stop'
    ```

    ```python
    >>> c5 = chord.Chord(['C4', 'F4', 'A-4'])
    ```

    ```python
    >>> lpc.appendContextFromChord(c2)
    >>> lpc.appendContextFromChord(c3)
    >>> lpc.appendContextFromChord(c4)
    >>> lpc.appendContextFromChord(c5)
    ```

    ```python
    >>> print(lpc.context)
    < c'  e'  g'  > 4
    \times 2/3 { < d'  fis'  a'  > 8
       < d'  f'  g'  > 8
       < c'  e'  g'  c''  > 8
        }

    < c'  f'  aes'  > 4
    ```

LilypondConverter.appendContextFromNoteOrRest(*noteOrRest*)[[source]](../_modules/music21/lily/translate.html#LilypondConverter.appendContextFromNoteOrRest)
:   appends lySimpleMusicFromNoteOrRest to the
    current context.

    ```python
    >>> n = note.Note('C#4')
    >>> lpc = lily.translate.LilypondConverter()
    >>> lpMusicList = lily.lilyObjects.LyMusicList()
    >>> lpc.context = lpMusicList
    >>> lpc.appendContextFromNoteOrRest(n)
    >>> print(lpMusicList)
    cis' 4
    ```

    ```python
    >>> n2 = note.Note('D#4')
    >>> n2.duration.quarterLength = 1/3
    >>> n2.duration.tuplets[0].type = 'start'
    >>> n3 = note.Note('E4')
    >>> n3.duration.quarterLength = 1/3
    >>> n4 = note.Note('F4')
    >>> n4.duration.quarterLength = 1/3
    >>> n4.duration.tuplets[0].type = 'stop'
    ```

    ```python
    >>> n5 = note.Note('F#4')
    ```

    ```python
    >>> lpc.appendContextFromNoteOrRest(n2)
    >>> lpc.appendContextFromNoteOrRest(n3)
    >>> lpc.appendContextFromNoteOrRest(n4)
    >>> lpc.appendContextFromNoteOrRest(n5)
    ```

    ```python
    >>> print(lpc.context)
    cis' 4
    \times 2/3 { dis' 8
       e' 8
       f' 8
        }

    fis' 4
    ```

LilypondConverter.appendContextFromVariant(*variantObjectOrList*, *activeSite=None*, *coloredVariants=False*)[[source]](../_modules/music21/lily/translate.html#LilypondConverter.appendContextFromVariant)
:   Create a new context from the variant object or a list of variants and append.

LilypondConverter.appendM21ObjectToContext(*thisObject*)[[source]](../_modules/music21/lily/translate.html#LilypondConverter.appendM21ObjectToContext)
:   converts any type of object into a lilyObject of LyMusic (
    LySimpleMusic, LyEmbeddedScm etc.) type

LilypondConverter.appendObjectsToContextFromStream(*streamObject*)[[source]](../_modules/music21/lily/translate.html#LilypondConverter.appendObjectsToContextFromStream)
:   takes a Stream and appends all the elements in it to the current
    context’s .contents list, and deals with creating Voices in it. It also deals with
    variants in it.

    (should eventually replace the main Score parts finding tools)

    ```python
    >>> lpc = lily.translate.LilypondConverter()
    >>> lpMusicList = lily.lilyObjects.LyMusicList()
    >>> lpc.context = lpMusicList
    >>> lpc.context.contents
    []
    >>> c = converter.parse('tinynotation: 3/4 b4 d- e#')
    >>> lpc.appendObjectsToContextFromStream(c)
    >>> print(lpc.context.contents)
    [<music21.lily.lilyObjects.LyEmbeddedScm...>,
     <music21.lily.lilyObjects.LySimpleMusic...>,
     <music21.lily.lilyObjects.LySimpleMusic...>,
     <music21.lily.lilyObjects.LySimpleMusic...]
    >>> print(lpc.context)
    \clef "treble"
    \time 3/4
    b' 4
    des' 4
    eis' 4
    ```

    ```python
    >>> v1 = stream.Voice()
    >>> v1.append(note.Note('C5', quarterLength = 4.0))
    >>> v2 = stream.Voice()
    >>> v2.append(note.Note('C#5', quarterLength = 4.0))
    >>> m = stream.Measure()
    >>> m.insert(0, v1)
    >>> m.insert(0, v2)
    >>> lpMusicList = lily.lilyObjects.LyMusicList()
    >>> lpc.context = lpMusicList
    >>> lpc.appendObjectsToContextFromStream(m)
    >>> print(lpc.context)  # internal spaces removed
      << \new Voice { c'' 1
                \bar "|."  %{ end measure 1 %}
              }
       \new Voice { cis'' 1
              }
        >>
    ```

LilypondConverter.appendStemCode(*noteOrChord*)[[source]](../_modules/music21/lily/translate.html#LilypondConverter.appendStemCode)
:   Adds an LyEmbeddedScm object to the context’s contents if the object’s stem direction
    is set (currently, only “up” and “down” are supported).

    ```python
    >>> lpc = lily.translate.LilypondConverter()
    >>> lpMusicList = lily.lilyObjects.LyMusicList()
    >>> lpc.context = lpMusicList
    >>> lpc.context.contents
    []
    >>> n = note.Note()
    >>> n.stemDirection = 'up'
    >>> lpc.appendStemCode(n)
    >>> print(lpc.context.contents)
    [<music21.lily.lilyObjects.LyEmbeddedScm \once \ove...>]
    >>> print(lpc.context.contents[0])
    \once \override Stem.direction = #UP
    ```

LilypondConverter.baseNameFromPitch(*pitch*)[[source]](../_modules/music21/lily/translate.html#LilypondConverter.baseNameFromPitch)
:   returns a string of the base name (including accidental)
    for a music21 pitch

LilypondConverter.closeMeasure(*barChecksOnly=False*)[[source]](../_modules/music21/lily/translate.html#LilypondConverter.closeMeasure)
:   return a LyObject or None for the end of the previous Measure

    uses self.currentMeasure

    ```python
    >>> lpc = lily.translate.LilypondConverter()
    >>> m = stream.Measure()
    >>> m.number = 2
    >>> m.rightBarline = 'double'
    >>> lpc.currentMeasure = m
    >>> lyObj = lpc.closeMeasure()
    >>> lpc.currentMeasure is None
    True
    >>> print(lyObj)
    \bar "||"  %{ end measure 2 %}
    ```

LilypondConverter.createPDF(*fileName=None*)[[source]](../_modules/music21/lily/translate.html#LilypondConverter.createPDF)
:   create a PDF file from self.topLevelObject and return the filepath of the file.

    most users will just call stream.write(‘lily.pdf’) on a stream.

LilypondConverter.createPNG(*fileName=None*)[[source]](../_modules/music21/lily/translate.html#LilypondConverter.createPNG)
:   create a PNG file from self.topLevelObject and return the filepath of the file.

    most users will just call stream.write(‘lily.png’) on a stream.

    if PIL is installed then a small white border is created around the score

LilypondConverter.createSVG(*fileName=None*)[[source]](../_modules/music21/lily/translate.html#LilypondConverter.createSVG)
:   create an SVG file from self.topLevelObject and return the filepath of the file.

    most users will just call stream.Stream.write(‘lily.svg’) on a stream.

LilypondConverter.findLilyExec()[[source]](../_modules/music21/lily/translate.html#LilypondConverter.findLilyExec)

LilypondConverter.getLySpacersFromStream(*streamIn*, *measuresOnly=True*)[[source]](../_modules/music21/lily/translate.html#LilypondConverter.getLySpacersFromStream)
:   Creates a series of Spacer objects for the measures in a Stream Part.

    ```python
    >>> m1 = stream.Measure(converter.parse('tinynotation: 3/4 a2.'))
    >>> m2 = stream.Measure(converter.parse('tinynotation: 3/4 b2.'))
    >>> m3 = stream.Measure(converter.parse('tinynotation: 4/4 a1'))
    >>> m4 = stream.Measure(converter.parse('tinynotation: 4/4 b1'))
    >>> m5 = stream.Measure(converter.parse('tinynotation: 4/4 c1'))
    >>> m6 = stream.Measure(converter.parse('tinynotation: 5/4 a4 b1'))
    >>> streamIn = stream.Stream([m1, m2, m3, m4, m5, m6])
    >>> lpc = lily.translate.LilypondConverter()
    >>> print(lpc.getLySpacersFromStream(streamIn))
    s2. s2. s1 s1 s1 s1 s4
    ```

    TODO: Low-priority: rare, but possible: tuplet time signatures (3/10), etc.

LilypondConverter.getSchemeForPadding(*measureObject*)[[source]](../_modules/music21/lily/translate.html#LilypondConverter.getSchemeForPadding)
:   lilypond partial durations are very strange and are really of
    type LyMultipliedDuration. You notate how many
    notes are left in the measure, for a quarter note, write “4”
    for an eighth, write “8”, but for 3 eighths, write “8\*3” !
    so we will measure in 32nd notes always. It won’t work for tuplets
    of course.

    Returns a scheme object or None if not needed.

    ```python
    >>> m = stream.Measure()
    >>> m.append(meter.TimeSignature('3/4'))
    >>> m.paddingLeft = 2.0
    >>> lpc = lily.translate.LilypondConverter()
    >>> outScheme = lpc.getSchemeForPadding(m)
    >>> print(outScheme)
    \partial 32*8
    ```

LilypondConverter.loadFromMusic21Object(*m21ObjectIn*)[[source]](../_modules/music21/lily/translate.html#LilypondConverter.loadFromMusic21Object)
:   Create a Lilypond object hierarchy in self.topLevelObject from an
    arbitrary music21 object.

    TODO: make lilypond automatically run makeNotation.makeTupletBrackets(s)
    TODO: Add tests.

LilypondConverter.loadObjectFromOpus(*opusIn=None*, *makeNotation=True*)[[source]](../_modules/music21/lily/translate.html#LilypondConverter.loadObjectFromOpus)
:   creates a filled topLevelObject (lily.lilyObjects.LyLilypondTop)
    whose string representation accurately reflects all the Score objects
    in this Opus object.

    ```python
    >>> fifeOpus = corpus.parse('miscFolk/americanfifeopus.abc')
    >>> lpc = lily.translate.LilypondConverter()
    >>> lpc.loadObjectFromOpus(fifeOpus, makeNotation=False)
    >>> lpc.showPDF()
    ```

LilypondConverter.loadObjectFromScore(*scoreIn=None*, *makeNotation=True*)[[source]](../_modules/music21/lily/translate.html#LilypondConverter.loadObjectFromScore)
:   creates a filled topLevelObject (lily.lilyObjects.LyLilypondTop)
    whose string representation accurately reflects this Score object.

    ```python
    >>> lpc = lily.translate.LilypondConverter()
    >>> b = corpus.parse('bach/bwv66.6')
    >>> lpc.loadObjectFromScore(b)
    ```

LilypondConverter.lyEmbeddedScmFromClef(*clefObj*)[[source]](../_modules/music21/lily/translate.html#LilypondConverter.lyEmbeddedScmFromClef)
:   converts a Clef object to a
    lilyObjects.LyEmbeddedScm object

    ```python
    >>> tc = clef.TrebleClef()
    >>> conv = lily.translate.LilypondConverter()
    >>> lpEmbeddedScm = conv.lyEmbeddedScmFromClef(tc)
    >>> print(lpEmbeddedScm)
    \clef "treble"
    ```

    ```python
    >>> t8c = clef.Treble8vbClef()
    >>> lpEmbeddedScm = conv.lyEmbeddedScmFromClef(t8c)
    >>> print(lpEmbeddedScm)
    \clef "treble_8"
    ```

LilypondConverter.lyEmbeddedScmFromKeySignature(*keyObj*)[[source]](../_modules/music21/lily/translate.html#LilypondConverter.lyEmbeddedScmFromKeySignature)
:   converts a Key or KeySignature object
    to a lilyObjects.LyEmbeddedScm object

    ```python
    >>> d = key.Key('d')
    >>> conv = lily.translate.LilypondConverter()
    >>> lpEmbeddedScm = conv.lyEmbeddedScmFromKeySignature(d)
    >>> print(lpEmbeddedScm)
    \key d \minor
    ```

    Major is assumed:

    ```python
    >>> fSharp = key.KeySignature(6)
    >>> print(conv.lyEmbeddedScmFromKeySignature(fSharp))
    \key fis \major
    ```

LilypondConverter.lyEmbeddedScmFromTimeSignature(*ts*)[[source]](../_modules/music21/lily/translate.html#LilypondConverter.lyEmbeddedScmFromTimeSignature)
:   convert a `TimeSignature` object
    to a lilyObjects.LyEmbeddedScm object

    ```python
    >>> ts = meter.TimeSignature('3/4')
    >>> conv = lily.translate.LilypondConverter()
    >>> print(conv.lyEmbeddedScmFromTimeSignature(ts))
    \time 3/4
    ```

LilypondConverter.lyGroupedMusicListFromScoreWithParts(*scoreIn*, *scoreInit=None*)[[source]](../_modules/music21/lily/translate.html#LilypondConverter.lyGroupedMusicListFromScoreWithParts)
:   More complex example showing how the score can be set up with ossia parts:

    ```python
    >>> lpc = lily.translate.LilypondConverter()
    >>> b = corpus.parse('bach/bwv66.6')
    >>> lpPartsAndOssiaInit = lpc.lyPartsAndOssiaInitFromScore(b)
    >>> lpGroupedMusicList = lpc.lyGroupedMusicListFromScoreWithParts(b,
    ...                scoreInit=lpPartsAndOssiaInit)
    >>> print(lpGroupedMusicList)

     << \new Staff  = Soprano { \stopStaff s4 s1 s1 s1 s1 s1 s1 s1 s1 s2. }
       \new Staff  = Alto { \stopStaff s4 s1 s1 s1 s1 s1 s1 s1 s1 s2. }
       \new Staff  = Tenor { \stopStaff s4 s1 s1 s1 s1 s1 s1 s1 s1 s2. }
       \new Staff  = Bass { \stopStaff s4 s1 s1 s1 s1 s1 s1 s1 s1 s2. }

      \context Staff  = Soprano \with {
          \autoBeamOff
      }
      { \startStaff \partial 32*8
            \clef "treble"
            \key fis \minor
            \time 4/4
            \set stemRightBeamCount = #1
            \once \override Stem.direction = #DOWN
            cis'' 8 [
            \set stemLeftBeamCount = #1
            \once \override Stem.direction = #DOWN
            b... 8 ]
            \bar "|"  %{ end measure 0 %}
            \once \override Stem.direction = #UP
            a' 4
            \once \override Stem.direction = #DOWN
            b... 4
            \once \override Stem.direction = #DOWN
            cis'' 4  \fermata
            \once \override Stem.direction = #DOWN
            e'' 4
            \bar "|"  %{ end measure 1 %}
            \once \override Stem.direction = #DOWN
            cis'' 4
            ...
    }

    \context Staff  = Alto \with  {
        \autoBeamOff
     }
     { \startStaff \partial 32*8
        \clef "treble"...
        \once \override Stem.direction = #UP
        e' 4
        \bar "|"  %{ end measure 0 %}
        \once \override Stem.direction = #UP
        fis' 4
        \once \override Stem.direction = #UP
        e' 4
    ...
    }

    >>
    ```

LilypondConverter.lyLyricElementFromM21Lyric(*m21Lyric*)[[source]](../_modules/music21/lily/translate.html#LilypondConverter.lyLyricElementFromM21Lyric)
:   Returns a [`LyLyricElement`](moduleLilyLilyObjects.html#music21.lily.lilyObjects.LyLyricElement "music21.lily.lilyObjects.LyLyricElement") object
    from a [`Lyric`](moduleNote.html#music21.note.Lyric "music21.note.Lyric") object.

    Uses self.inWord to keep track of whether we’re in the middle of
    a word.

    ```python
    >>> s = converter.parse('tinyNotation: 4/4 c4_hel- d4_-lo r2 e2 f2_world')
    >>> s.makeMeasures(inPlace=True)
    >>> lyrics = s.lyrics()[1]  # get first verse (yes, 1 = first, not 0!)
    ```

    ```python
    >>> lpc = lily.translate.LilypondConverter()
    >>> lpc.lyLyricElementFromM21Lyric(lyrics[0])
    <music21.lily.lilyObjects.LyLyricElement "hel" -->
    >>> lpc.inWord
    True
    >>> lpc.lyLyricElementFromM21Lyric(lyrics[1])
    <music21.lily.lilyObjects.LyLyricElement "lo"__>
    >>> lpc.lyLyricElementFromM21Lyric(lyrics[2])
    <music21.lily.lilyObjects.LyLyricElement _>
    >>> lpc.lyLyricElementFromM21Lyric(lyrics[3])
    <music21.lily.lilyObjects.LyLyricElement "world">
    >>> lpc.inWord
    False
    ```

LilypondConverter.lyMultipliedDurationFromDuration(*durationObj: [Duration](moduleDuration.html#music21.duration.Duration "music21.duration.Duration") | [DurationTuple](moduleDuration.html#music21.duration.DurationTuple "music21.duration.DurationTuple")*)[[source]](../_modules/music21/lily/translate.html#LilypondConverter.lyMultipliedDurationFromDuration)
:   take a simple Duration (that is, one with one DurationTuple)
    object and return a LyMultipliedDuration object:

    ```python
    >>> d = duration.Duration(3)
    >>> lpc = lily.translate.LilypondConverter()
    >>> lyMultipliedDuration = lpc.lyMultipliedDurationFromDuration(d)
    >>> str(lyMultipliedDuration)
    '2. '
    ```

    ```python
    >>> str(lpc.lyMultipliedDurationFromDuration(duration.Duration(8.0)))
    '\\breve '
    >>> str(lpc.lyMultipliedDurationFromDuration(duration.Duration(16.0)))
    '\\longa '
    ```

    Does not work with zero duration notes:

    ```python
    >>> d = duration.Duration(0.0)
    >>> str(lpc.lyMultipliedDurationFromDuration(d))
    Traceback (most recent call last):
    music21.lily.translate.LilyTranslateException: Cannot translate an object of
        zero duration <music21.duration.Duration 0.0>
    ```

    Does not work with complex durations:

    ```python
    >>> d = duration.Duration(5.0)
    >>> str(lpc.lyMultipliedDurationFromDuration(d))
    Traceback (most recent call last):
    music21.lily.translate.LilyTranslateException: DurationException for durationObject
        <music21.duration.Duration 5.0>: Could not determine durationNumber from complex
    ```

    Instead, split by components:

    ```python
    >>> components = d.components
    >>> [str(lpc.lyMultipliedDurationFromDuration(c)) for c in components]
    ['1 ', '4 ']
    ```

LilypondConverter.lyNewLyricsFromStream(*streamIn*, *streamId=None*, *alignment='alignBelowContext'*)[[source]](../_modules/music21/lily/translate.html#LilypondConverter.lyNewLyricsFromStream)
:   returns a LyNewLyrics object

    This is a bit of a hack. This should be switched over to using a
    prefixed context thing with new Lyric = “id” with { } {}

    ```python
    >>> s = converter.parse('tinyNotation: 4/4 c4_hel- d4_-lo r4 e4_world')
    >>> s.makeMeasures(inPlace=True)
    >>> s.id = 'helloWorld'
    ```

    ```python
    >>> lpc = lily.translate.LilypondConverter()
    >>> lyNewLyrics = lpc.lyNewLyricsFromStream(s)
    >>> print(lyNewLyrics)
    \addlyrics { \set alignBelowContext = #"helloWorld"
       "hel" --
       "lo"__
       "world"
        }
    ```

LilypondConverter.lyOssiaMusicFromVariant(*variantIn*)[[source]](../_modules/music21/lily/translate.html#LilypondConverter.lyOssiaMusicFromVariant)
:   returns a LyOssiaMusic object from a stream

    ```python
    >>> c = converter.parse('tinynotation: 3/4 C4 D E F2.')
    >>> v = variant.Variant(c.elements)
    >>> lpc = lily.translate.LilypondConverter()
    >>> lySequentialMusicOut = lpc.lySequentialMusicFromStream(v)
    >>> lySequentialMusicOut
    <music21.lily.lilyObjects.LySequentialMusic { \clef "b...>
    >>> print(lySequentialMusicOut)
    { \clef "bass"
     \time 3/4
     c 4
     d 4
     e 4
     \bar "|"  %{ end measure 1 %}
     f 2.
     \bar "|."  %{ end measure 2 %}
      }
    ```

LilypondConverter.lyPartsAndOssiaInitFromScore(*scoreIn*)[[source]](../_modules/music21/lily/translate.html#LilypondConverter.lyPartsAndOssiaInitFromScore)
:   Takes in a score and returns a block that starts each part context and variant context
    with an identifier and {stopStaff s1\*n} (or s, whatever is needed for the duration)
    where n is the number of measures in the score.

    ```python
    >>> import copy
    ```

    Set up score:

    ```python
    >>> s = stream.Score()
    >>> p1,p2 = stream.Part(), stream.Part()
    >>> p1.insert(0, meter.TimeSignature('4/4'))
    >>> p2.insert(0, meter.TimeSignature('4/4'))
    >>> p1.append(variant.Variant(name='london'))
    >>> p2.append(variant.Variant(name='london'))
    >>> p1.append(variant.Variant(name='rome'))
    >>> p2.append(variant.Variant(name='rome'))
    >>> for i in range(4):
    ...    m = stream.Measure()
    ...    n = note.Note('D4', type='whole')
    ...    m.append(n)
    ...    p1.append(m)
    ...    p2.append(copy.deepcopy(m))
    >>> p1.id = 'pa'
    >>> p2.id = 'pb'
    >>> s.append(p1)
    >>> s.append(p2)
    ```

    Run method

    ```python
    >>> lpc = lily.translate.LilypondConverter()
    >>> print(lpc.lyPartsAndOssiaInitFromScore(s))
    \new Staff  = pa { \stopStaff s1 s1 s1 s1 }
    \new Staff  = londonpa
                \with {
                      \remove "Time_signature_engraver"
                      alignAboveContext = #"pa"
                      fontSize = #-3
                      \override StaffSymbol.staff-space = #(magstep -3)
                      \override StaffSymbol.thickness = #(magstep -3)
                      \override TupletBracket.bracket-visibility = ##f
                      \override TupletNumber.stencil = ##f
                      \override Clef.transparent = ##t
                      \override OctavateEight.transparent = ##t
                      \consists "Default_bar_line_engraver"
                    }
             { \stopStaff s1 s1 s1 s1 }
    \new Staff  = romepa
                \with {
                      \remove "Time_signature_engraver"
                      alignAboveContext = #"pa"
                      fontSize = #-3
                      \override StaffSymbol.staff-space = #(magstep -3)
                      \override StaffSymbol.thickness = #(magstep -3)
                      \override TupletBracket.bracket-visibility = ##f
                      \override TupletNumber.stencil = ##f
                      \override Clef.transparent = ##t
                      \override OctavateEight.transparent = ##t
                      \consists "Default_bar_line_engraver"
                    }
             { \stopStaff s1 s1 s1 s1 }
    \new Staff  = pb { \stopStaff s1 s1 s1 s1 }
    \new Staff  = londonpb
                \with {
                      \remove "Time_signature_engraver"
                      alignAboveContext = #"pb...
                      fontSize = #-3
                      \override StaffSymbol.staff-space = #(magstep -3)
                      \override StaffSymbol.thickness = #(magstep -3)
                      \override TupletBracket.bracket-visibility = ##f
                      \override TupletNumber.stencil = ##f
                      \override Clef.transparent = ##t
                      \override OctavateEight.transparent = ##t
                      \consists "Default_bar_line_engraver"
                    }
             { \stopStaff s1 s1 s1 s1 }
    \new Staff  = romepb
                \with {
                      \remove "Time_signature_engraver"
                      alignAboveContext = #"pb...
                      fontSize = #-3
                      \override StaffSymbol.staff-space = #(magstep -3)
                      \override StaffSymbol.thickness = #(magstep -3)
                      \override TupletBracket.bracket-visibility = ##f
                      \override TupletNumber.stencil = ##f
                      \override Clef.transparent = ##t
                      \override OctavateEight.transparent = ##t
                      \consists "Default_bar_line_engraver"
                    }
             { \stopStaff s1 s1 s1 s1 }
    ```

LilypondConverter.lyPitchFromPitch(*pitch*)[[source]](../_modules/music21/lily/translate.html#LilypondConverter.lyPitchFromPitch)
:   converts a music21.pitch.Pitch object to a lily.lilyObjects.LyPitch
    object.

LilypondConverter.lyPrefixCompositeMusicFromRelatedVariants(*variantList*, *activeSite=None*, *coloredVariants=False*)[[source]](../_modules/music21/lily/translate.html#LilypondConverter.lyPrefixCompositeMusicFromRelatedVariants)
:   ```python
    >>> s1 = converter.parse('tinynotation: 4/4 a4 a a a  a1')
    >>> s2 = converter.parse('tinynotation: 4/4 b4 b b b')
    >>> s3 = converter.parse('tinynotation: 4/4 c4 c c c')
    >>> s4 = converter.parse('tinynotation: 4/4 d4 d d d')
    >>> s5 = converter.parse('tinynotation: 4/4 e4 e e e  f f f f  g g g g  a a a a  b b b b')
    ```

    ```python
    >>> for s in [ s1, s2, s3, s4, s5]:
    ...     s.makeMeasures(inPlace=True)
    ```

    ```python
    >>> activeSite = stream.Part(s5.elements)
    ```

    ```python
    >>> v1 = variant.Variant()
    >>> for el in s1:
    ...     v1.append(el)
    >>> v1.replacementDuration = 4.0
    ```

    ```python
    >>> v2 = variant.Variant()
    >>> sp2 = note.Rest()
    >>> sp2.style.hideObjectOnPrint = True
    >>> sp2.duration.quarterLength = 4.0
    >>> v2.replacementDuration = 4.0
    >>> v2.append(sp2)
    >>> for el in s2:
    ...     v2.append(el)
    ```

    ```python
    >>> v3 = variant.Variant()
    >>> sp3 = note.Rest()
    >>> sp3.style.hideObjectOnPrint = True
    >>> sp3.duration.quarterLength = 8.0
    >>> v3.replacementDuration = 4.0
    >>> v3.append(sp3)
    >>> for el in s3:
    ...     v3.append(el)
    ```

    ```python
    >>> v4 = variant.Variant()
    >>> sp4 = note.Rest()
    >>> sp4.style.hideObjectOnPrint = True
    >>> sp4.duration.quarterLength = 16.0
    >>> v4.replacementDuration = 4.0
    >>> v4.append(sp4)
    >>> for el in s4:
    ...     v4.append(el)
    ```

    ```python
    >>> variantList = [v4, v1, v3, v2]
    >>> for v in variantList :
    ...     v.groups = ['london']
    ...     activeSite.insert(0.0, v)
    ```

    ```python
    >>> lpc = lily.translate.LilypondConverter()
    ```

    ```python
    >>> print(lpc.lyPrefixCompositeMusicFromRelatedVariants(variantList,
    ...                activeSite=activeSite)[0])
    \new Staff  = london... { { \times 1/2 {\startStaff \clef "treble"
          a' 4
          a' 4
          a' 4
          a' 4
          \clef "treble"
          | %{ end measure 1 %}
          a' 1
          | %{ end measure 2 %}
           \stopStaff}
           }

      {\startStaff \clef "treble"
        b... 4
        b... 4
        b... 4
        b... 4
        | %{ end measure 1 %}
         \stopStaff}

      {\startStaff \clef "treble"
        c' 4
        c' 4
        c' 4
        c' 4
        | %{ end measure 1 %}
         \stopStaff}

      s 1
      {\startStaff \clef "treble"
        d' 4
        d' 4
        d' 4
        d' 4
        | %{ end measure 1 %}
         \stopStaff}

       }
    ```

LilypondConverter.lyPrefixCompositeMusicFromStream(*streamIn*, *contextType=None*, *type=None*, *beforeMatter=None*)[[source]](../_modules/music21/lily/translate.html#LilypondConverter.lyPrefixCompositeMusicFromStream)
:   returns an LyPrefixCompositeMusic object from
    a stream (generally a part, but who knows!)

    ```python
    >>> c = converter.parse('tinynotation: 3/4 C4 D E F2.')
    >>> c.staffLines = 4
    ```

    ```python
    >>> lpc = lily.translate.LilypondConverter()
    >>> lyPrefixCompositeMusicOut = lpc.lyPrefixCompositeMusicFromStream(c, contextType='Staff')
    >>> lyPrefixCompositeMusicOut
    <music21.lily.lilyObjects.LyPrefixCompositeMusic \new Staff...>
    >>> print(lyPrefixCompositeMusicOut)
    \new Staff = ... \with {
     \override StaffSymbol.line-count = #4
    }
    { \clef "bass"
         \time 3/4
         c 4
         d 4
         e 4
         \bar "|"  %{ end measure 1 %}
         f 2.
         \bar "|."  %{ end measure 2 %}
          }
    ```

LilypondConverter.lyPrefixCompositeMusicFromVariant(*variantObject*, *replacedElements*, *coloredVariants=False*)[[source]](../_modules/music21/lily/translate.html#LilypondConverter.lyPrefixCompositeMusicFromVariant)
:   ```python
    >>> pStream = converter.parse('tinynotation: 4/4 a4 b c d   e4 f g a')
    >>> pStream.makeMeasures(inPlace=True)
    >>> p = stream.Part(pStream.elements)
    >>> p.id = 'p1'
    >>> vStream = converter.parse('tinynotation: 4/4 a4. b8 c4 d')
    >>> vStream.makeMeasures(inPlace=True)
    >>> v = variant.Variant(vStream.elements)
    >>> v.groups = ['london']
    >>> p.insert(0.0, v)
    >>> lpc = lily.translate.LilypondConverter()
    >>> replacedElements = v.replacedElements()
    >>> lpPrefixCompositeMusicVariant = lpc.lyPrefixCompositeMusicFromVariant(v,
    ...                                                            replacedElements)
    >>> print(lpPrefixCompositeMusicVariant)  # ellipses are for non-byte fix-ups
    \new Staff  = londonpx { {\startStaff \clef "treble"
        a' 4.
        b...
        c' 4
        d' 4
        | %{ end measure 1 %}
         \stopStaff}
       }
    ```

    ```python
    >>> replacedElements.show('text')
    {0.0} <music21.stream.Measure 1 offset=0.0>
        {0.0} <music21.clef.TrebleClef>
        {0.0} <music21.meter.TimeSignature 4/4>
        {0.0} <music21.note.Note A>
        {1.0} <music21.note.Note B>
        {2.0} <music21.note.Note C>
        {3.0} <music21.note.Note D>
    ```

    ```python
    >>> print(lpc.addedVariants)
    ['london']
    ```

LilypondConverter.lyScoreBlockFromScore(*scoreIn*)[[source]](../_modules/music21/lily/translate.html#LilypondConverter.lyScoreBlockFromScore)

LilypondConverter.lySequentialMusicFromStream(*streamIn*, *beforeMatter=None*)[[source]](../_modules/music21/lily/translate.html#LilypondConverter.lySequentialMusicFromStream)
:   returns a LySequentialMusic object from a stream

    ```python
    >>> c = converter.parse('tinynotation: 3/4 C4 D E F2.')
    >>> lpc = lily.translate.LilypondConverter()
    >>> lySequentialMusicOut = lpc.lySequentialMusicFromStream(c)
    >>> lySequentialMusicOut
    <music21.lily.lilyObjects.LySequentialMusic { \clef "b...>
    >>> print(lySequentialMusicOut)
    { \clef "bass"
     \time 3/4
     c 4
     d 4
     e 4
     \bar "|"  %{ end measure 1 %}
     f 2.
     \bar "|."  %{ end measure 2 %}
      }
    ```

LilypondConverter.lySimpleMusicFromChord(*chordObj*)[[source]](../_modules/music21/lily/translate.html#LilypondConverter.lySimpleMusicFromChord)
:   ```python
    >>> conv = lily.translate.LilypondConverter()
    >>> c1 = chord.Chord(['C#2', 'E4', 'D#5'])
    >>> c1.quarterLength = 3.5
    >>> c1.pitches[2].accidental.displayType = 'always'
    >>> print(conv.lySimpleMusicFromChord(c1))
     < cis, e' dis''  !  > 2..
    ```

    test hidden chord:

    ```python
    >>> c1.style.hideObjectOnPrint = True
    >>> print(conv.lySimpleMusicFromChord(c1))
    s 2..
    ```

LilypondConverter.lySimpleMusicFromNoteOrRest(*noteOrRest*)[[source]](../_modules/music21/lily/translate.html#LilypondConverter.lySimpleMusicFromNoteOrRest)
:   returns a lilyObjects.LySimpleMusic object for the generalNote containing this hierarchy:

    ```python
    LyEventChord   containing
    LySimpleChordElements containing
    LySimpleElement containing
    LyPitch  AND
    LyMultipliedDuration containing:

        LyMultipliedDuration containing
        LyStenoDuration
    ```

    does not check for tuplets. That’s in
    appendContextFromNoteOrRest

    read-only property that returns a string of the lilypond representation of
    a note (or via subclassing, rest or chord)

    ```python
    >>> conv = lily.translate.LilypondConverter()
    ```

    ```python
    >>> n0 = note.Note('D#5')
    >>> n0.pitch.accidental.displayType = 'always'
    >>> n0.pitch.accidental.displayStyle = 'parentheses'
    >>> n0.style.color = 'blue'
    >>> sm = conv.lySimpleMusicFromNoteOrRest(n0)
    >>> print(sm)
    \override NoteHead.color = "blue"
    \override Stem.color = "blue"
    dis'' ! ? 4
    ```

    Now make the note disappear:

    ```python
    >>> n0.style.hideObjectOnPrint = True
    >>> sm = conv.lySimpleMusicFromNoteOrRest(n0)
    >>> print(sm)
    s 4
    ```

LilypondConverter.newContext(*newContext*)[[source]](../_modules/music21/lily/translate.html#LilypondConverter.newContext)

LilypondConverter.octaveCharactersFromPitch(*pitch*)[[source]](../_modules/music21/lily/translate.html#LilypondConverter.octaveCharactersFromPitch)
:   returns a string of single-quotes or commas or ‘’ representing
    the octave of a [`Pitch`](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch") object

LilypondConverter.postEventsFromObject(*generalNote*)[[source]](../_modules/music21/lily/translate.html#LilypondConverter.postEventsFromObject)
:   attaches events that apply to notes and chords (and some other things) equally

LilypondConverter.restoreContext()[[source]](../_modules/music21/lily/translate.html#LilypondConverter.restoreContext)

LilypondConverter.runThroughLily(*format=None*, *backend=None*, *fileName=None*, *skipWriting=False*)[[source]](../_modules/music21/lily/translate.html#LilypondConverter.runThroughLily)
:   creates a .ly file from self.topLevelObject via .writeLyFile
    then runs the file through Lilypond.

    Returns the full path of the file produced by lilypond including the format extension.

    If skipWriting is True and a fileName is given then it will run
    that file through lilypond instead

LilypondConverter.setContextForTimeFraction(*numerator*, *denominator*)[[source]](../_modules/music21/lily/translate.html#LilypondConverter.setContextForTimeFraction)
:   Explicitly starts a new context for scaled music (tuplets, etc.)
    for the given numerator and denominator (either an int or a string or unicode)

    Returns an lpMusicList object contained in an lpSequentialMusic object
    in an lpPrefixCompositeMusic object which sets the times object to a particular
    fraction.

    ```python
    >>> lpc = lily.translate.LilypondConverter()
    >>> lpc.context
    <music21.lily.lilyObjects.LyLilypondTop>
    >>> lyTop = lpc.context
    >>> lyoMusicList = lpc.setContextForTimeFraction(5, 4)
    >>> lyoMusicList
    <music21.lily.lilyObjects.LyMusicList>
    >>> lpc.context
    <music21.lily.lilyObjects.LyMusicList>
    >>> lpc.context is lyoMusicList
    True
    >>> lpc.context.getParent()
    <music21.lily.lilyObjects.LySequentialMusic {  }>
    >>> lpc.context.getParent().getParent()
    <music21.lily.lilyObjects.LyPrefixCompositeMusic \times 5/4...>
    >>> lpc.context.getParent().getParent().fraction
    '5/4'
    >>> lpc.context.getParent().getParent().type
    'times'
    >>> lpc.context.getParent().getParent().getParent()
    <music21.lily.lilyObjects.LyLilypondTop \times 5/4...>
    >>> lpc.context.getParent().getParent().getParent() is lyTop
    True
    ```

LilypondConverter.setContextForTupletStart(*inObj*)[[source]](../_modules/music21/lily/translate.html#LilypondConverter.setContextForTupletStart)
:   if the inObj has tuplets then we set a new context
    for the tuplets and anything up till a tuplet stop.

    Note that a broken tuplet (à la Michael Gordon)
    will not work.

    If there are no tuplets, this routine does
    nothing. If there are tuplets, and they have type “start”, then
    it returns an lpMusicList object, which is the new context

    For now, no support for nested tuplets. They’re an
    easy extension, but there’s too much
    else that is missing to do it now.

LilypondConverter.setContextForTupletStop(*inObj*)[[source]](../_modules/music21/lily/translate.html#LilypondConverter.setContextForTupletStop)
:   Reverse of setContextForTupletStart

LilypondConverter.setHeaderFromMetadata(*metadataObject=None*, *lpHeader=None*)[[source]](../_modules/music21/lily/translate.html#LilypondConverter.setHeaderFromMetadata)
:   Returns a lilypond.lilyObjects.LyLilypondHeader object
    set with data from the metadata object

    ```python
    >>> md = metadata.Metadata()
    >>> md.title = 'My Title'
    >>> md.alternativeTitle = 'My "sub"-title'
    ```

    ```python
    >>> lpc = lily.translate.LilypondConverter()
    >>> lpHeader = lpc.setHeaderFromMetadata(md)
    >>> print(lpHeader)
    \header { title = "My Title"
    subtitle = "My \"sub\"-title"
    }
    ```

LilypondConverter.setupTools()[[source]](../_modules/music21/lily/translate.html#LilypondConverter.setupTools)

LilypondConverter.showPDF()[[source]](../_modules/music21/lily/translate.html#LilypondConverter.showPDF)
:   create an SVG file from self.topLevelObject, show it with your pdf reader
    (often Adobe Acrobat/Adobe Reader or Apple Preview)
    and return the filepath of the file.

    most users will just call stream.Stream.show(‘lily.pdf’) on a stream.

LilypondConverter.showPNG()[[source]](../_modules/music21/lily/translate.html#LilypondConverter.showPNG)
:   Take the object, run it through LilyPond, and then show it as a PNG file.
    On Windows, the PNG file will not be deleted, so you will need to clean out
    TEMP every once in a while.

    Most users will just want to call stream.Stream.show(‘lily.png’) instead.

LilypondConverter.showSVG(*fileName=None*)[[source]](../_modules/music21/lily/translate.html#LilypondConverter.showSVG)
:   create an SVG file from self.topLevelObject, show it with your
    svg reader (often Internet Explorer on PC)
    and return the filepath of the file.

    most users will just call stream.Stream.show(‘lily.png’) on a stream.

LilypondConverter.textFromMusic21Object(*m21ObjectIn*)[[source]](../_modules/music21/lily/translate.html#LilypondConverter.textFromMusic21Object)
:   get a proper lilypond text file for writing from a music21 object

    ```python
    >>> n = note.Note()
    >>> print(lily.translate.LilypondConverter().textFromMusic21Object(n))
    \version "2..."
    \include "lilypond-book-preamble.ly"
    color = #(define-music-function (parser location color) (string?) #{
            \once \override NoteHead.color = #(x11-color color)
            \once \override Stem.color = #(x11-color color)
            \once \override Rest.color = #(x11-color color)
            \once \override Beam.color = #(x11-color color)
         #})
    \header { }
    \score  {
          << \new Staff  = ... { c' 4
                  }
            >>
      }
    \paper { }
    ...
    ```

LilypondConverter.writeLyFile(*ext=''*, *fp=None*)[[source]](../_modules/music21/lily/translate.html#LilypondConverter.writeLyFile)
:   writes the contents of the self.topLevelObject to a file.

    The extension should be ly. If fp is None then a named temporary
    file is created by environment.getTempFile.

## Functions

music21.lily.translate.makeLettersOnlyId(*inputString*)[[source]](../_modules/music21/lily/translate.html#makeLettersOnlyId)
:   Takes an id and makes it purely letters by substituting
    letters for all other characters.

    ```python
    >>> print(lily.translate.makeLettersOnlyId('rainbow123@@dfas'))
    rainbowxyzmmdfas
    ```
