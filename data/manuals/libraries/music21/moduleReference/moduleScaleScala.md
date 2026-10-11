Source: https://music21.org/music21docs/moduleReference/moduleScaleScala.html

# music21.scale.scala

This module defines classes for representing Scala scale data,
including Scala pitch representations, storage, and files.

The Scala format is defined at the following URL:
<https://www.huygens-fokker.org/scala/scl_format.html>

We thank Manuel Op de Coul for allowing us to include
the repository (as of May 11, 2011) with music21

Scala files are encoded as latin-1 (ISO-8859) text

Utility functions are also provided to search and find
scales in the Scala scale archive. File names can be found
with the `search()` function.

To create a [`ScalaScale`](moduleScale.html#music21.scale.ScalaScale "music21.scale.ScalaScale") instance, simply
provide a root pitch and the name of the scale. Scale names are given as
the scala .scl filename.

```python
>>> mbiraScales = scale.scala.search('mbira')
>>> mbiraScales
['mbira_banda.scl', 'mbira_banda2.scl', 'mbira_gondo.scl', 'mbira_kunaka.scl',
 'mbira_kunaka2.scl', 'mbira_mude.scl', 'mbira_mujuru.scl', 'mbira_zimb.scl']
```

For most people you’ll want to do something like this:

```python
>>> sc = scale.ScalaScale('a4', 'mbira_banda.scl')
>>> [str(p) for p in sc.pitches]
['A4', 'B4(-15c)', 'C#5(-11c)', 'E-5(-7c)', 'E~5(+6c)', 'F#5(+14c)', 'G~5(+1c)', 'B-5(+2c)']
```

## ScalaData

class music21.scale.scala.ScalaData(*sourceString=None*, *fileName=None*)[[source]](../_modules/music21/scale/scala.html#ScalaData)
:   Object representation of data stored in a Scala scale file. This object is used to
    access Scala information stored in a file. To create a music21 scale with a Scala file,
    use [`ScalaScale`](moduleScale.html#music21.scale.ScalaScale "music21.scale.ScalaScale").

    This is not called ScalaScale, as this name clashes with the
    [`ScalaScale`](moduleScale.html#music21.scale.ScalaScale "music21.scale.ScalaScale") that uses this object.

    ```python
    >>> import os
    >>> sf = scale.scala.ScalaFile()
    >>> fp = common.getSourceFilePath() / 'scale' / 'scala' / 'scl' / 'tanaka.scl'
    >>> sf.open(fp)
    >>> sd = sf.read()
    ```

    ScaleFile descriptions are converted to unicode.

    ```python
    >>> print(sd.description)
    26-note choice system of Shohé Tanaka, Studien i.G.d. reinen Stimmung (1890)
    >>> sd.pitchCount
    26
    ```

    Distances from the tonic:

    ```python
    >>> cat = sd.getCentsAboveTonic()
    >>> len(cat)
    26
    >>> list(int(round(x)) for x in cat[0:4])
    [71, 92, 112, 182]
    >>> sd.pitchValues[0]
    <music21.scale.scala.ScalaPitch object at 0x10b16fac8>
    >>> sd.pitchValues[0].cents
    70.6724...
    ```

    This will not add up with centsAboveTonic above, due to rounding

    ```python
    >>> adj = sd.getAdjacentCents()
    >>> list(int(round(x)) for x in adj[0:4])
    [71, 22, 20, 71]
    ```

    Interval Sequences

    ```python
    >>> intSeq = sd.getIntervalSequence()
    >>> intSeq[0:4]
    [<music21.interval.Interval m2 (-29c)>,
     <music21.interval.Interval P1 (+22c)>,
     <music21.interval.Interval P1 (+20c)>,
     <music21.interval.Interval m2 (-29c)>]
    ```

    Tweak the file and be ready to write it back out:

    ```python
    >>> sd.pitchValues[0].cents = 73.25
    >>> sd.fileName = 'tanaka2.scl'
    >>> sd.description = 'Tweaked version of tanaka.scl'
    >>> fs = sd.getFileString()
    >>> print(fs)
    ! tanaka2.scl
    !
    Tweaked version of tanaka.scl
    26
    !
    73.25
    92.17...
    111.73...
    182.40...
    ```

    Be sure to reencode fs as latin-1 before writing to disk.

    ```python
    >>> sf.close()
    ```

[`ScalaData`](#music21.scale.scala.ScalaData "music21.scale.scala.ScalaData") methods

ScalaData.getAdjacentCents()[[source]](../_modules/music21/scale/scala.html#ScalaData.getAdjacentCents)
:   Get cents values between adjacent intervals.

ScalaData.getCentsAboveTonic()[[source]](../_modules/music21/scale/scala.html#ScalaData.getCentsAboveTonic)
:   Return a list of cent values above the implied tonic.

ScalaData.getFileString()[[source]](../_modules/music21/scale/scala.html#ScalaData.getFileString)
:   Return a unicode-string suitable for writing a Scala file

    The unicode string should be encoded in Latin-1 for maximum
    Scala compatibility.

ScalaData.getIntervalSequence()[[source]](../_modules/music21/scale/scala.html#ScalaData.getIntervalSequence)
:   Get the scale as a list of Interval objects.

ScalaData.parse()[[source]](../_modules/music21/scale/scala.html#ScalaData.parse)
:   Parse a scala file delivered as a long string with line breaks

ScalaData.setAdjacentCents(*centList*)[[source]](../_modules/music21/scale/scala.html#ScalaData.setAdjacentCents)
:   Given a list of adjacent cent values, create the necessary ScalaPitch
    objects and update them

ScalaData.setIntervalSequence(*iList*)[[source]](../_modules/music21/scale/scala.html#ScalaData.setIntervalSequence)
:   Set the scale from a list of Interval objects.

## ScalaFile

class music21.scale.scala.ScalaFile(*data=None*)[[source]](../_modules/music21/scale/scala.html#ScalaFile)
:   Interface for reading and writing scala files.
    On reading, returns a `ScalaData` object.

    ```python
    >>> import os
    >>> sf = scale.scala.ScalaFile()
    >>> fp = common.getSourceFilePath() / 'scale' / 'scala' / 'scl' / 'tanaka.scl'
    >>> sf.open(fp)
    >>> sd = sf.read()
    >>> sd
    <music21.scale.scala.ScalaData object at 0x10b170e10>
    >>> sd is sf.data
    True
    >>> sf.fileName.endswith('tanaka.scl')
    True
    >>> sd.pitchCount
    26
    >>> sf.close()
    ```

[`ScalaFile`](#music21.scale.scala.ScalaFile "music21.scale.scala.ScalaFile") methods

ScalaFile.close()[[source]](../_modules/music21/scale/scala.html#ScalaFile.close)

ScalaFile.open(*fp*, *mode='r'*)[[source]](../_modules/music21/scale/scala.html#ScalaFile.open)
:   Open a file for reading

ScalaFile.openFileLike(*fileLike*)[[source]](../_modules/music21/scale/scala.html#ScalaFile.openFileLike)
:   Assign a file-like object, such as those provided by StringIO, as an open file object.

ScalaFile.read()[[source]](../_modules/music21/scale/scala.html#ScalaFile.read)
:   Read a file. Note that this calls readstr, which processes all tokens.

    If number is given, a work number will be extracted if possible.

ScalaFile.readstr(*strSrc*)[[source]](../_modules/music21/scale/scala.html#ScalaFile.readstr)
:   Read a string and process all Tokens. Returns a ABCHandler instance.

ScalaFile.write()[[source]](../_modules/music21/scale/scala.html#ScalaFile.write)

ScalaFile.writestr() → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](../_modules/music21/scale/scala.html#ScalaFile.writestr)

## ScalaPitch

class music21.scale.scala.ScalaPitch(*sourceString=None*)[[source]](../_modules/music21/scale/scala.html#ScalaPitch)
:   Representation of a scala pitch notation

    ```python
    >>> sp = scale.scala.ScalaPitch(' 1066.667 cents')
    >>> print(sp.parse())
    1066.667
    ```

    ```python
    >>> sp = scale.scala.ScalaPitch(' 2/1')
    >>> sp.parse()
    1200.0
    >>> sp.parse('100.0 C#')
    100.0
    >>> [sp.parse(x) for x in ['89/84', '55/49', '44/37', '63/50', '4/3', '99/70', '442/295',
    ...     '27/17', '37/22', '98/55', '15/8', '2/1']]
    [100.0992..., 199.9798..., 299.9739..., 400.10848..., 498.04499...,
     600.0883..., 699.9976..., 800.9095..., 900.0260...,
     1000.0201..., 1088.2687..., 1200.0]
    ```

[`ScalaPitch`](#music21.scale.scala.ScalaPitch "music21.scale.scala.ScalaPitch") methods

ScalaPitch.parse(*sourceString=None*)[[source]](../_modules/music21/scale/scala.html#ScalaPitch.parse)
:   Parse the source string and set self.cents.

## Functions

music21.scale.scala.parse(*target*)[[source]](../_modules/music21/scale/scala.html#parse)
:   Get a `ScalaData` object from
    the bundled SCL archive or a file path.

    ```python
    >>> ss = scale.scala.parse('balafon6')
    >>> ss.description
    'Observed balafon tuning from Burma, Helmholtz/Ellis p. 518, nr.84'
    >>> [str(i) for i in ss.getIntervalSequence()]
    ['<music21.interval.Interval m2 (+14c)>', '<music21.interval.Interval M2 (+36c)>',
    '<music21.interval.Interval M2>', '<music21.interval.Interval m2 (+37c)>',
    '<music21.interval.Interval M2 (-49c)>', '<music21.interval.Interval M2 (-6c)>',
    '<music21.interval.Interval M2 (-36c)>']
    ```

    ```python
    >>> scale.scala.parse('incorrectFileName.scl') is None
    True
    ```

    ```python
    >>> ss = scale.scala.parse('barbourChrom1')
    >>> print(ss.description)
    Barbour's #1 Chromatic
    >>> ss.fileName
    'barbour_chrom1.scl'
    ```

    ```python
    >>> ss = scale.scala.parse('blackj_gws.scl')
    >>> ss.description
    'Detempered Blackjack in 1/4 kleismic marvel tuning'
    ```

music21.scale.scala.search(*target*)[[source]](../_modules/music21/scale/scala.html#search)
:   Search the scala archive for matches based on a string

    ```python
    >>> mbiraScales = scale.scala.search('mbira')
    >>> mbiraScales
    ['mbira_banda.scl', 'mbira_banda2.scl', 'mbira_gondo.scl', 'mbira_kunaka.scl',
     'mbira_kunaka2.scl', 'mbira_mude.scl', 'mbira_mujuru.scl', 'mbira_zimb.scl']
    ```

music21.scale.scala.getPaths()[[source]](../_modules/music21/scale/scala.html#getPaths)
:   Get all scala scale paths. This is called once or the module and
    cached as SCALA\_PATHS, which should be used instead of calls to this function.

    ```python
    >>> a = scale.scala.getPaths()
    >>> len(a) >= 3800
    True
    ```
