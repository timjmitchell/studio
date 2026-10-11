Source: https://music21.org/music21docs/moduleReference/moduleSearchLyrics.html

# music21.search.lyrics

Classes for searching for Lyric objects.

## LyricSearcher

class music21.search.lyrics.LyricSearcher(*s: StreamType | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\**, *wordSeparator: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ' '*)[[source]](../_modules/music21/search/lyrics.html#LyricSearcher)
:   An object that can find lyrics that match a certain regular expression
    and return relevant information about the match.

    Construct the LyricSearcher by passing in a Stream object (it can be
    a Score or Part or other nested item), and then call “.search()” on it.

    See [User’s Guide, Chapter 28, Lyric Searching](../usersGuide/usersGuide_28_lyricSearcher.html#usersguide-28-lyricsearcher) for
    full details.

    TODO: Bug that occasionally the previous note will be included; Search luca/gloria for
    :   “riam tuam.” (From Gloriam tuam). For some reason, the whole “Gloria” is included.
        Does not occur if only “iam tuam.” is searched.

    TODO: allow for all intermediate notes during a search to be found.
    :   includeIntermediateElements.

    TODO: allow for trailing melismas to also be included.

    TODO: Note that because of recursive searching w/ voices, there may be “phantom” lyrics
    :   found if a work contains multiple voices.

[`LyricSearcher`](#music21.search.lyrics.LyricSearcher "music21.search.lyrics.LyricSearcher") read-only properties

LyricSearcher.indexText
:   Returns the text that has been indexed (a la, [`assembleLyrics()`](moduleText.html#music21.text.assembleLyrics "music21.text.assembleLyrics")):

    ```python
    >>> p0 = corpus.parse('luca/gloria').parts[0]
    >>> ls = search.lyrics.LyricSearcher(p0)
    >>> ls.indexText[0:25]
    'Et in terra pax hominibus'
    ```

LyricSearcher.indexTuples

[`LyricSearcher`](#music21.search.lyrics.LyricSearcher "music21.search.lyrics.LyricSearcher") methods

LyricSearcher.index(*s=None*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[IndexedLyric](#music21.search.lyrics.IndexedLyric "music21.search.lyrics.IndexedLyric")][[source]](../_modules/music21/search/lyrics.html#LyricSearcher.index)
:   A method that indexes the Stream’s lyrics and returns the list
    of IndexedLyric objects.

    This does not actually need to be run, since calling .search() will call this if
    it hasn’t already been called.

    ```python
    >>> from pprint import pprint as pp
    ```

    ```python
    >>> p0 = corpus.parse('luca/gloria').parts[0]
    >>> ls = search.lyrics.LyricSearcher(p0)
    >>> pp(ls.index()[0:5])
    [IndexedLyric(el=<music21.note.Note C>, start=0, end=2, measure=1,
         lyric=<music21.note.Lyric number=1 syllabic=single text='Et'>, text='Et',
         identifier=1),
     IndexedLyric(el=<music21.note.Note D>, start=3, end=5, measure=2,
         lyric=<music21.note.Lyric number=1 syllabic=single text='in'>, text='in',
         identifier=1),
     IndexedLyric(el=<music21.note.Note F>, start=6, end=9, measure=2,
         lyric=<music21.note.Lyric number=1 syllabic=begin text='ter'>, text='ter',
         identifier=1),
     IndexedLyric(el=<music21.note.Note F>, start=9, end=11, measure=3,
         lyric=<music21.note.Lyric number=1 syllabic=end text='ra'>, text='ra',
         identifier=1),
     IndexedLyric(el=<music21.note.Note A>, start=12, end=15, measure=3,
         lyric=<music21.note.Lyric number=1 syllabic=single text='pax'>, text='pax',
         identifier=1)]
    ```

    * Changed in v6.7: indexed lyrics get an identifier.

LyricSearcher.search(*textOrRe*, *s=None*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[SearchMatch](#music21.search.lyrics.SearchMatch "music21.search.lyrics.SearchMatch")][[source]](../_modules/music21/search/lyrics.html#LyricSearcher.search)
:   Return a list of SearchMatch objects matching a string or regular expression.

    ```python
    >>> import re
    ```

    ```python
    >>> p0 = corpus.parse('luca/gloria').parts[0]
    >>> ls = search.lyrics.LyricSearcher(p0)
    >>> ls.search('pax')
    [SearchMatch(mStart=3, mEnd=3, matchText='pax', els=(<music21.note.Note A>,),
                    indices=[...], identifier=1)]
    ```

    Search a regular expression that takes into account non-word characters such as commas

    ```python
    >>> agnus = re.compile(r'agnus dei\W+filius patris', re.IGNORECASE)
    >>> sm = ls.search(agnus)
    >>> sm
    [SearchMatch(mStart=49, mEnd=55, matchText='Agnus Dei, Filius Patris',
                    els=(<music21.note.Note G>,...<music21.note.Note G>), indices=[...],
                    identifier=1)]
    >>> sm[0].mStart, sm[0].mEnd
    (49, 55)
    ```

## IndexedLyric

class music21.search.lyrics.IndexedLyric(*el*, *start*, *end*, *measure*, *lyric*, *text*, *identifier*, *absoluteStart*, *absoluteEnd*)[[source]](../_modules/music21/search/lyrics.html#IndexedLyric)
:   A Lyric that has been indexed to its attached element and position in a Stream.

[`IndexedLyric`](#music21.search.lyrics.IndexedLyric "music21.search.lyrics.IndexedLyric") bases

* [`IndexedLyric`](#music21.search.lyrics.IndexedLyric "music21.search.lyrics.IndexedLyric")

[`IndexedLyric`](#music21.search.lyrics.IndexedLyric "music21.search.lyrics.IndexedLyric") methods

IndexedLyric.modify(*\*\*keywords*)[[source]](../_modules/music21/search/lyrics.html#IndexedLyric.modify)
:   see docs for SortTuple for what this does

[`IndexedLyric`](#music21.search.lyrics.IndexedLyric "music21.search.lyrics.IndexedLyric") instance variables

IndexedLyric.absoluteEnd
:   the end position in all the lyrics

IndexedLyric.absoluteStart
:   the position, not in the current identifier, but in all the lyrics

IndexedLyric.el
:   the element that the lyric is attached to

IndexedLyric.end
:   Suppose that the entire lyric for the stream were a single string:
    this is the index of the position in the string that this
    lyric ends at.

IndexedLyric.identifier
:   The identifier of the lyric

IndexedLyric.lyric
:   The [`Lyric`](moduleNote.html#music21.note.Lyric "music21.note.Lyric") object itself

IndexedLyric.measure
:   The measureNumber of the measure that the element is in
    in the stream. Same as .el.measureNumber

IndexedLyric.start
:   Suppose that the entire lyric for the stream were a single string:
    this is the index of the position in the string that this
    lyric starts at.

IndexedLyric.text
:   The text of the lyric as a string.

## SearchMatch

class music21.search.lyrics.SearchMatch(*mStart*, *mEnd*, *matchText*, *els*, *indices*, *identifier*)[[source]](../_modules/music21/search/lyrics.html#SearchMatch)
:   A lightweight object representing the match (if any) for a search.

[`SearchMatch`](#music21.search.lyrics.SearchMatch "music21.search.lyrics.SearchMatch") bases

* [`SearchMatch`](#music21.search.lyrics.SearchMatch "music21.search.lyrics.SearchMatch")

[`SearchMatch`](#music21.search.lyrics.SearchMatch "music21.search.lyrics.SearchMatch") instance variables

SearchMatch.els
:   A list of all lyric-containing elements that matched this text.

SearchMatch.identifier
:   The identifier of (presumably all, but at least the first) lyric to match.

SearchMatch.indices
:   A list of IndexedLyric objects that match.

SearchMatch.mEnd
:   The measureNumber of the measure that the last matching lyric is in.

SearchMatch.mStart
:   The measureNumber of the measure that the first matching lyric is in.

SearchMatch.matchText
:   The text of the lyric that matched the search. For a
    plaintext search, this will be the same as the search
    term, but for a regular expression
    search this will be the text that matched the regular
    expression.
