Source: https://music21.org/music21docs/moduleReference/moduleFeaturesNative.html

# music21.features.native

Original music21 feature extractors.

## ChordBassMotionFeature

class music21.features.native.ChordBassMotionFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/native.html#ChordBassMotionFeature)
:   A twelve element feature that reports the fraction
    of all chord motion of music21.harmony.Harmony objects
    that move up by i-half-steps. (a half-step motion down would
    be stored in i = 11). i = 0 is always 0.0 since consecutive
    chords on the same pitch are ignored (unless there are 0 or 1 harmonies, in which case it is 1)

    Sample test on Dylan’s Blowing In The Wind (not included), showing all
    motion is 3rds, 6ths, or especially 4ths and 5ths.

    s = corpus.parse(‘demos/BlowinInTheWind’)
    fe = features.native.ChordBassMotionFeature(s)
    fe.extract().vector

    [0.0, 0.0, 0.0, 0.0416…, 0.0416…, 0.166…, 0.0, 0.54166…, 0.0, 0.0, 0.2083… 0.0]

    For comparison, the Beatles Here Comes the Sun has more tone motion

    [0.0, 0.05…, 0.14…, 0.03…, 0.06…, 0.3…, 0.008…, 0.303…,
    :   0.0, 0.0, 0.07…, 0.008…]

    Post 1990s music has a lot more semitone motion.

[`ChordBassMotionFeature`](#music21.features.native.ChordBassMotionFeature "music21.features.native.ChordBassMotionFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`ChordBassMotionFeature`](#music21.features.native.ChordBassMotionFeature "music21.features.native.ChordBassMotionFeature") methods

ChordBassMotionFeature.process()[[source]](../_modules/music21/features/native.html#ChordBassMotionFeature.process)
:   Do processing necessary, storing result in feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## ComposerPopularity

class music21.features.native.ComposerPopularity(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/native.html#ComposerPopularity)
:   REMOVED in v7 because Google’s repsonse no longer includes result counts.
    Empty class still here so that id won’t be reused, but it’s been removed
    from this module’s list of features.

[`ComposerPopularity`](#music21.features.native.ComposerPopularity "music21.features.native.ComposerPopularity") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`ComposerPopularity`](#music21.features.native.ComposerPopularity "music21.features.native.ComposerPopularity") methods

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") | * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") | * [`process()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.process "music21.features.base.FeatureExtractor.process") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## DiminishedSeventhSimultaneityPrevalence

class music21.features.native.DiminishedSeventhSimultaneityPrevalence(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/native.html#DiminishedSeventhSimultaneityPrevalence)
:   Percentage of all simultaneities that are diminished seventh chords.

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> fe = features.native.DiminishedSeventhSimultaneityPrevalence(s)
    >>> fe.extract().vector
    [0.0]
    ```

[`DiminishedSeventhSimultaneityPrevalence`](#music21.features.native.DiminishedSeventhSimultaneityPrevalence "music21.features.native.DiminishedSeventhSimultaneityPrevalence") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`DiminishedSeventhSimultaneityPrevalence`](#music21.features.native.DiminishedSeventhSimultaneityPrevalence "music21.features.native.DiminishedSeventhSimultaneityPrevalence") methods

DiminishedSeventhSimultaneityPrevalence.process()[[source]](../_modules/music21/features/native.html#DiminishedSeventhSimultaneityPrevalence.process)
:   Do processing necessary, storing result in feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## DiminishedTriadSimultaneityPrevalence

class music21.features.native.DiminishedTriadSimultaneityPrevalence(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/native.html#DiminishedTriadSimultaneityPrevalence)
:   Percentage of all simultaneities that are diminished triads.

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> fe = features.native.DiminishedTriadSimultaneityPrevalence(s)
    >>> fe.extract().vector
    [0.019...]
    ```

[`DiminishedTriadSimultaneityPrevalence`](#music21.features.native.DiminishedTriadSimultaneityPrevalence "music21.features.native.DiminishedTriadSimultaneityPrevalence") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`DiminishedTriadSimultaneityPrevalence`](#music21.features.native.DiminishedTriadSimultaneityPrevalence "music21.features.native.DiminishedTriadSimultaneityPrevalence") methods

DiminishedTriadSimultaneityPrevalence.process()[[source]](../_modules/music21/features/native.html#DiminishedTriadSimultaneityPrevalence.process)
:   Do processing necessary, storing result in feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## DominantSeventhSimultaneityPrevalence

class music21.features.native.DominantSeventhSimultaneityPrevalence(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/native.html#DominantSeventhSimultaneityPrevalence)
:   Percentage of all simultaneities that are dominant seventh.

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> fe = features.native.DominantSeventhSimultaneityPrevalence(s)
    >>> fe.extract().vector
    [0.076...]
    ```

[`DominantSeventhSimultaneityPrevalence`](#music21.features.native.DominantSeventhSimultaneityPrevalence "music21.features.native.DominantSeventhSimultaneityPrevalence") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`DominantSeventhSimultaneityPrevalence`](#music21.features.native.DominantSeventhSimultaneityPrevalence "music21.features.native.DominantSeventhSimultaneityPrevalence") methods

DominantSeventhSimultaneityPrevalence.process()[[source]](../_modules/music21/features/native.html#DominantSeventhSimultaneityPrevalence.process)
:   Do processing necessary, storing result in feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## FirstBeatAttackPrevalence

class music21.features.native.FirstBeatAttackPrevalence(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/native.html#FirstBeatAttackPrevalence)
:   NOT IMPLEMENTED!

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> fe = features.native.FirstBeatAttackPrevalence(s)
    >>> f = fe.extract()
    >>> f.vector
    [0]
    ```

    TODO: Implement!

[`FirstBeatAttackPrevalence`](#music21.features.native.FirstBeatAttackPrevalence "music21.features.native.FirstBeatAttackPrevalence") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`FirstBeatAttackPrevalence`](#music21.features.native.FirstBeatAttackPrevalence "music21.features.native.FirstBeatAttackPrevalence") methods

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") | * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") | * [`process()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.process "music21.features.base.FeatureExtractor.process") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## IncorrectlySpelledTriadPrevalence

class music21.features.native.IncorrectlySpelledTriadPrevalence(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/native.html#IncorrectlySpelledTriadPrevalence)
:   Percentage of all triads that are spelled incorrectly.

    example:

    Mozart k155 movement 2 has a single instance of an incorrectly spelled
    triad (m. 17, where the C# of an A-major chord has a lower neighbor B#
    thus temporarily creating an incorrectly spelled A-minor chord).

    We would expect highly chromatic music such as Reger or Wagner to have
    a higher percentage, or automatically rendered MIDI
    transcriptions (which don’t distinguish between D# and Eb).

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> fe = features.native.IncorrectlySpelledTriadPrevalence(s)
    >>> fe.extract().vector
    [0.02...]
    ```

[`IncorrectlySpelledTriadPrevalence`](#music21.features.native.IncorrectlySpelledTriadPrevalence "music21.features.native.IncorrectlySpelledTriadPrevalence") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`IncorrectlySpelledTriadPrevalence`](#music21.features.native.IncorrectlySpelledTriadPrevalence "music21.features.native.IncorrectlySpelledTriadPrevalence") methods

IncorrectlySpelledTriadPrevalence.process()[[source]](../_modules/music21/features/native.html#IncorrectlySpelledTriadPrevalence.process)
:   Do processing necessary, storing result in feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## LandiniCadence

class music21.features.native.LandiniCadence(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/native.html#LandiniCadence)
:   Return a boolean if one or more Parts end with a Landini-like cadential figure.

[`LandiniCadence`](#music21.features.native.LandiniCadence "music21.features.native.LandiniCadence") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`LandiniCadence`](#music21.features.native.LandiniCadence "music21.features.native.LandiniCadence") methods

LandiniCadence.process()[[source]](../_modules/music21/features/native.html#LandiniCadence.process)
:   Do processing necessary, storing result in feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## LanguageFeature

class music21.features.native.LanguageFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/native.html#LanguageFeature)
:   language of text as a number
    the number is the index of text.LanguageDetector.languageCodes + 1
    or 0 if there is no language.

    Detect that the language of a Handel aria is Italian.

    ```python
    >>> s = corpus.parse('handel/rinaldo/lascia_chio_pianga')
    >>> fe = features.native.LanguageFeature(s)
    >>> fe.extract().vector
    [3]
    ```

[`LanguageFeature`](#music21.features.native.LanguageFeature "music21.features.native.LanguageFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`LanguageFeature`](#music21.features.native.LanguageFeature "music21.features.native.LanguageFeature") methods

LanguageFeature.process()[[source]](../_modules/music21/features/native.html#LanguageFeature.process)
:   Do processing necessary, storing result in feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## MajorTriadSimultaneityPrevalence

class music21.features.native.MajorTriadSimultaneityPrevalence(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/native.html#MajorTriadSimultaneityPrevalence)
:   Percentage of all simultaneities that are major triads.

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> fe = features.native.MajorTriadSimultaneityPrevalence(s)
    >>> fe.extract().vector
    [0.46...]
    ```

[`MajorTriadSimultaneityPrevalence`](#music21.features.native.MajorTriadSimultaneityPrevalence "music21.features.native.MajorTriadSimultaneityPrevalence") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`MajorTriadSimultaneityPrevalence`](#music21.features.native.MajorTriadSimultaneityPrevalence "music21.features.native.MajorTriadSimultaneityPrevalence") methods

MajorTriadSimultaneityPrevalence.process()[[source]](../_modules/music21/features/native.html#MajorTriadSimultaneityPrevalence.process)
:   Do processing necessary, storing result in feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## MinorTriadSimultaneityPrevalence

class music21.features.native.MinorTriadSimultaneityPrevalence(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/native.html#MinorTriadSimultaneityPrevalence)
:   Percentage of all simultaneities that are minor triads.

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> fe = features.native.MinorTriadSimultaneityPrevalence(s)
    >>> fe.extract().vector  # same as major in this work
    [0.211...]
    ```

[`MinorTriadSimultaneityPrevalence`](#music21.features.native.MinorTriadSimultaneityPrevalence "music21.features.native.MinorTriadSimultaneityPrevalence") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`MinorTriadSimultaneityPrevalence`](#music21.features.native.MinorTriadSimultaneityPrevalence "music21.features.native.MinorTriadSimultaneityPrevalence") methods

MinorTriadSimultaneityPrevalence.process()[[source]](../_modules/music21/features/native.html#MinorTriadSimultaneityPrevalence.process)
:   Do processing necessary, storing result in feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## MostCommonNoteQuarterLength

class music21.features.native.MostCommonNoteQuarterLength(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/native.html#MostCommonNoteQuarterLength)
:   ```python
    >>> s = corpus.parse('bwv66.6')
    >>> fe = features.native.MostCommonNoteQuarterLength(s)
    >>> fe.extract().vector
    [1.0]
    ```

[`MostCommonNoteQuarterLength`](#music21.features.native.MostCommonNoteQuarterLength "music21.features.native.MostCommonNoteQuarterLength") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`MostCommonNoteQuarterLength`](#music21.features.native.MostCommonNoteQuarterLength "music21.features.native.MostCommonNoteQuarterLength") methods

MostCommonNoteQuarterLength.process()[[source]](../_modules/music21/features/native.html#MostCommonNoteQuarterLength.process)
:   Do processing necessary, storing result in feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## MostCommonNoteQuarterLengthPrevalence

class music21.features.native.MostCommonNoteQuarterLengthPrevalence(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/native.html#MostCommonNoteQuarterLengthPrevalence)
:   Fraction of notes that have the most common quarter length.

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> fe = features.native.MostCommonNoteQuarterLengthPrevalence(s)
    >>> fe.extract().vector
    [0.60...]
    ```

[`MostCommonNoteQuarterLengthPrevalence`](#music21.features.native.MostCommonNoteQuarterLengthPrevalence "music21.features.native.MostCommonNoteQuarterLengthPrevalence") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`MostCommonNoteQuarterLengthPrevalence`](#music21.features.native.MostCommonNoteQuarterLengthPrevalence "music21.features.native.MostCommonNoteQuarterLengthPrevalence") methods

MostCommonNoteQuarterLengthPrevalence.process()[[source]](../_modules/music21/features/native.html#MostCommonNoteQuarterLengthPrevalence.process)
:   Do processing necessary, storing result in feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## MostCommonPitchClassSetSimultaneityPrevalence

class music21.features.native.MostCommonPitchClassSetSimultaneityPrevalence(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/native.html#MostCommonPitchClassSetSimultaneityPrevalence)
:   Fraction of all pitch class simultaneities that are the most common simultaneity.

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> fe = features.native.MostCommonPitchClassSetSimultaneityPrevalence(s)
    >>> fe.extract().vector
    [0.134...]
    ```

[`MostCommonPitchClassSetSimultaneityPrevalence`](#music21.features.native.MostCommonPitchClassSetSimultaneityPrevalence "music21.features.native.MostCommonPitchClassSetSimultaneityPrevalence") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`MostCommonPitchClassSetSimultaneityPrevalence`](#music21.features.native.MostCommonPitchClassSetSimultaneityPrevalence "music21.features.native.MostCommonPitchClassSetSimultaneityPrevalence") methods

MostCommonPitchClassSetSimultaneityPrevalence.process()[[source]](../_modules/music21/features/native.html#MostCommonPitchClassSetSimultaneityPrevalence.process)
:   Do processing necessary, storing result in feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## MostCommonSetClassSimultaneityPrevalence

class music21.features.native.MostCommonSetClassSimultaneityPrevalence(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/native.html#MostCommonSetClassSimultaneityPrevalence)
:   Fraction of all set class simultaneities that the most common simultaneity
    occupies.

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> fe = features.native.MostCommonSetClassSimultaneityPrevalence(s)
    >>> fe.extract().vector
    [0.653...]
    >>> s2 = corpus.parse('schoenberg/opus19', 6)
    >>> fe2 = features.native.MostCommonSetClassSimultaneityPrevalence(s2)
    >>> fe2.extract().vector
    [0.235...]
    ```

[`MostCommonSetClassSimultaneityPrevalence`](#music21.features.native.MostCommonSetClassSimultaneityPrevalence "music21.features.native.MostCommonSetClassSimultaneityPrevalence") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`MostCommonSetClassSimultaneityPrevalence`](#music21.features.native.MostCommonSetClassSimultaneityPrevalence "music21.features.native.MostCommonSetClassSimultaneityPrevalence") methods

MostCommonSetClassSimultaneityPrevalence.process()[[source]](../_modules/music21/features/native.html#MostCommonSetClassSimultaneityPrevalence.process)
:   Do processing necessary, storing result in feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## QualityFeature

class music21.features.native.QualityFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/native.html#QualityFeature)
:   Extends the jSymbolic QualityFeature to automatically find mode.

    Set to 0 if the key signature indicates that
    a recording is major, set to 1 if it indicates
    that it is minor. A Music21
    addition: if no key mode is found in the piece, or conflicting modes in the keys,
    analyze the piece to discover what mode it is most likely in.

    Example: Handel, Rinaldo Aria (musicxml) is explicitly encoded as being in Major:

    ```python
    >>> s = corpus.parse('handel/rinaldo/lascia_chio_pianga')
    >>> fe = features.native.QualityFeature(s)
    >>> f = fe.extract()
    >>> f.vector
    [0]
    ```

    now we will try it with the last movement of Schoenberg’s opus 19 which has
    no mode explicitly encoded in the musicxml but which our analysis routines
    believe (having very little to go on) fits the profile of e minor best.

    ```python
    >>> schoenberg19mvmt6 = corpus.parse('schoenberg/opus19', 6)
    >>> fe2 = features.native.QualityFeature(schoenberg19mvmt6)
    >>> f2 = fe2.extract()
    >>> f2.vector
    [1]
    ```

[`QualityFeature`](#music21.features.native.QualityFeature "music21.features.native.QualityFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`QualityFeature`](#music21.features.native.QualityFeature "music21.features.native.QualityFeature") methods

QualityFeature.process() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/features/native.html#QualityFeature.process)
:   Do processing necessary, storing result in feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## RangeOfNoteQuarterLengths

class music21.features.native.RangeOfNoteQuarterLengths(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/native.html#RangeOfNoteQuarterLengths)
:   Difference between the longest and shortest quarter lengths.

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> fe = features.native.RangeOfNoteQuarterLengths(s)
    >>> fe.extract().vector
    [1.5]
    ```

[`RangeOfNoteQuarterLengths`](#music21.features.native.RangeOfNoteQuarterLengths "music21.features.native.RangeOfNoteQuarterLengths") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`RangeOfNoteQuarterLengths`](#music21.features.native.RangeOfNoteQuarterLengths "music21.features.native.RangeOfNoteQuarterLengths") methods

RangeOfNoteQuarterLengths.process()[[source]](../_modules/music21/features/native.html#RangeOfNoteQuarterLengths.process)
:   Do processing necessary, storing result in feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## TonalCertainty

class music21.features.native.TonalCertainty(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/native.html#TonalCertainty)
:   ```python
    >>> s = corpus.parse('bwv66.6')
    >>> fe = features.native.TonalCertainty(s)
    >>> f = fe.extract()
    >>> f.vector
    [1.26...]
    ```

    ```python
    >>> pitches = [56, 55, 56, 57, 58, 57, 58, 59, 60, 59, 60, 61, 62, 61,
    ...            62, 63, 64, 63, 64, 65, 66, 65, 66, 67]
    >>> s = stream.Stream()
    >>> for pitch in pitches:
    ...   s.append(note.Note(pitch))
    >>> features.native.TonalCertainty(s).extract().vector
    [0.0]
    ```

[`TonalCertainty`](#music21.features.native.TonalCertainty "music21.features.native.TonalCertainty") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`TonalCertainty`](#music21.features.native.TonalCertainty "music21.features.native.TonalCertainty") methods

TonalCertainty.process()[[source]](../_modules/music21/features/native.html#TonalCertainty.process)
:   Do processing necessary, storing result in feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## TriadSimultaneityPrevalence

class music21.features.native.TriadSimultaneityPrevalence(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/native.html#TriadSimultaneityPrevalence)
:   Gives the proportion of all simultaneities which form triads (major,
    minor, diminished, or augmented)

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> fe = features.native.TriadSimultaneityPrevalence(s)
    >>> fe.extract().vector
    [0.692...]
    >>> s2 = corpus.parse('schoenberg/opus19', 2)
    >>> fe2 = features.native.TriadSimultaneityPrevalence(s2)
    >>> fe2.extract().vector
    [0.02272727...]
    ```

[`TriadSimultaneityPrevalence`](#music21.features.native.TriadSimultaneityPrevalence "music21.features.native.TriadSimultaneityPrevalence") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`TriadSimultaneityPrevalence`](#music21.features.native.TriadSimultaneityPrevalence "music21.features.native.TriadSimultaneityPrevalence") methods

TriadSimultaneityPrevalence.process()[[source]](../_modules/music21/features/native.html#TriadSimultaneityPrevalence.process)
:   Do processing necessary, storing result in feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## UniqueNoteQuarterLengths

class music21.features.native.UniqueNoteQuarterLengths(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/native.html#UniqueNoteQuarterLengths)
:   ```python
    >>> s = corpus.parse('bwv66.6')
    >>> fe = features.native.UniqueNoteQuarterLengths(s)
    >>> fe.extract().vector
    [3]
    ```

[`UniqueNoteQuarterLengths`](#music21.features.native.UniqueNoteQuarterLengths "music21.features.native.UniqueNoteQuarterLengths") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`UniqueNoteQuarterLengths`](#music21.features.native.UniqueNoteQuarterLengths "music21.features.native.UniqueNoteQuarterLengths") methods

UniqueNoteQuarterLengths.process()[[source]](../_modules/music21/features/native.html#UniqueNoteQuarterLengths.process)
:   Do processing necessary, storing result in feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## UniquePitchClassSetSimultaneities

class music21.features.native.UniquePitchClassSetSimultaneities(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/native.html#UniquePitchClassSetSimultaneities)
:   Number of unique pitch class simultaneities.

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> fe = features.native.UniquePitchClassSetSimultaneities(s)
    >>> fe.extract().vector
    [27]
    ```

[`UniquePitchClassSetSimultaneities`](#music21.features.native.UniquePitchClassSetSimultaneities "music21.features.native.UniquePitchClassSetSimultaneities") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`UniquePitchClassSetSimultaneities`](#music21.features.native.UniquePitchClassSetSimultaneities "music21.features.native.UniquePitchClassSetSimultaneities") methods

UniquePitchClassSetSimultaneities.process()[[source]](../_modules/music21/features/native.html#UniquePitchClassSetSimultaneities.process)
:   Do processing necessary, storing result in feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## UniqueSetClassSimultaneities

class music21.features.native.UniqueSetClassSimultaneities(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/native.html#UniqueSetClassSimultaneities)
:   Number of unique set class simultaneities.

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> fe = features.native.UniqueSetClassSimultaneities(s)
    >>> fe.extract().vector
    [14]
    ```

[`UniqueSetClassSimultaneities`](#music21.features.native.UniqueSetClassSimultaneities "music21.features.native.UniqueSetClassSimultaneities") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`UniqueSetClassSimultaneities`](#music21.features.native.UniqueSetClassSimultaneities "music21.features.native.UniqueSetClassSimultaneities") methods

UniqueSetClassSimultaneities.process()[[source]](../_modules/music21/features/native.html#UniqueSetClassSimultaneities.process)
:   Do processing necessary, storing result in feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |
