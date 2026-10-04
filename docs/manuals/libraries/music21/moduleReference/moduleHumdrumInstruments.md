Source: https://music21.org/music21docs/moduleReference/moduleHumdrumInstruments.html

# music21.humdrum.instruments

Instrument translations from
<https://web.archive.org/web/20100115001258/http://www.music-cog.ohio-state.edu/Humdrum/guide.append2.html>

## Functions

music21.humdrum.instruments.fromHumdrumClass(*hdClass*)[[source]](../_modules/music21/humdrum/instruments.html#fromHumdrumClass)
:   Get a music21 instrument object from a humdrum instrument class abbreviation

    ```python
    >>> humdrum.instruments.fromHumdrumClass('vox')
    <music21.instrument.Vocalist 'Voice'>
    ```

music21.humdrum.instruments.fromHumdrumInstrument(*hdInst*)[[source]](../_modules/music21/humdrum/instruments.html#fromHumdrumInstrument)
:   Get a music21 instrument object from a humdrum instrument abbreviation

    ```python
    >>> humdrum.instruments.fromHumdrumInstrument('calto')
    <music21.instrument.Alto 'Alto'>
    ```
