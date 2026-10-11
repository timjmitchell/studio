Source: https://music21.org/music21docs/moduleReference/moduleFeaturesJSymbolic.html

# music21.features.jSymbolic

The features implemented here are based on those found in jSymbolic and
defined in Cory McKay’s MA Thesis, “Automatic Genre Classification of MIDI Recordings”

## AcousticGuitarFractionFeature

class music21.features.jSymbolic.AcousticGuitarFractionFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#AcousticGuitarFractionFeature)
:   A feature extractor that extracts the fraction of all Note Ons belonging to
    acoustic guitar patches (General MIDI patches 25 and 26).

    ```python
    >>> s1 = stream.Stream()
    >>> s1.append(instrument.AcousticGuitar())
    >>> s1.repeatAppend(note.Note(), 3)
    >>> s1.append(instrument.Tuba())
    >>> s1.append(note.Note())
    >>> fe = features.jSymbolic.AcousticGuitarFractionFeature(s1)
    >>> fe.extract().vector
    [0.75]
    ```

[`AcousticGuitarFractionFeature`](#music21.features.jSymbolic.AcousticGuitarFractionFeature "music21.features.jSymbolic.AcousticGuitarFractionFeature") bases

* [`InstrumentFractionFeature`](#music21.features.jSymbolic.InstrumentFractionFeature "music21.features.jSymbolic.InstrumentFractionFeature")
* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`AcousticGuitarFractionFeature`](#music21.features.jSymbolic.AcousticGuitarFractionFeature "music21.features.jSymbolic.AcousticGuitarFractionFeature") methods

Methods inherited from [`InstrumentFractionFeature`](#music21.features.jSymbolic.InstrumentFractionFeature "music21.features.jSymbolic.InstrumentFractionFeature"):

|  |  |  |
| --- | --- | --- |
| * [`process()`](#music21.features.jSymbolic.InstrumentFractionFeature.process "music21.features.jSymbolic.InstrumentFractionFeature.process") |  |  |

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## AmountOfArpeggiationFeature

class music21.features.jSymbolic.AmountOfArpeggiationFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#AmountOfArpeggiationFeature)
:   Fraction of horizontal intervals that are repeated notes, minor thirds, major thirds,
    perfect fifths, minor sevenths, major sevenths, octaves, minor tenths or major tenths.

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> fe = features.jSymbolic.AmountOfArpeggiationFeature(s)
    >>> f = fe.extract()
    >>> f.name
    'Amount of Arpeggiation'
    >>> f.vector
    [0.333...]
    ```

[`AmountOfArpeggiationFeature`](#music21.features.jSymbolic.AmountOfArpeggiationFeature "music21.features.jSymbolic.AmountOfArpeggiationFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`AmountOfArpeggiationFeature`](#music21.features.jSymbolic.AmountOfArpeggiationFeature "music21.features.jSymbolic.AmountOfArpeggiationFeature") methods

AmountOfArpeggiationFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#AmountOfArpeggiationFeature.process)
:   Do processing necessary, storing result in feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## AverageMelodicIntervalFeature

class music21.features.jSymbolic.AverageMelodicIntervalFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#AverageMelodicIntervalFeature)
:   Average melodic interval (in semitones).

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> fe = features.jSymbolic.AverageMelodicIntervalFeature(s)
    >>> f = fe.extract()
    >>> f.vector
    [2.44...]
    ```

[`AverageMelodicIntervalFeature`](#music21.features.jSymbolic.AverageMelodicIntervalFeature "music21.features.jSymbolic.AverageMelodicIntervalFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`AverageMelodicIntervalFeature`](#music21.features.jSymbolic.AverageMelodicIntervalFeature "music21.features.jSymbolic.AverageMelodicIntervalFeature") methods

AverageMelodicIntervalFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#AverageMelodicIntervalFeature.process)
:   Do processing necessary, storing result in feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## AverageNoteDurationFeature

class music21.features.jSymbolic.AverageNoteDurationFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#AverageNoteDurationFeature)
:   Average duration of notes in seconds.

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> fe = features.jSymbolic.AverageNoteDurationFeature(s)
    >>> f = fe.extract()
    >>> f.vector
    [0.552...]
    ```

    ```python
    >>> s.insert(0, tempo.MetronomeMark(number=240))
    >>> fe = features.jSymbolic.AverageNoteDurationFeature(s)
    >>> f = fe.extract()
    >>> f.vector
    [0.220858...]
    ```

[`AverageNoteDurationFeature`](#music21.features.jSymbolic.AverageNoteDurationFeature "music21.features.jSymbolic.AverageNoteDurationFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`AverageNoteDurationFeature`](#music21.features.jSymbolic.AverageNoteDurationFeature "music21.features.jSymbolic.AverageNoteDurationFeature") methods

AverageNoteDurationFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#AverageNoteDurationFeature.process)
:   Do processing necessary, storing result in \_feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## AverageNoteToNoteDynamicsChangeFeature

class music21.features.jSymbolic.AverageNoteToNoteDynamicsChangeFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#AverageNoteToNoteDynamicsChangeFeature)
:   Not implemented

    Average change of loudness from one note to the next note in the
    same channel (in MIDI velocity units).

    TODO: implement

[`AverageNoteToNoteDynamicsChangeFeature`](#music21.features.jSymbolic.AverageNoteToNoteDynamicsChangeFeature "music21.features.jSymbolic.AverageNoteToNoteDynamicsChangeFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`AverageNoteToNoteDynamicsChangeFeature`](#music21.features.jSymbolic.AverageNoteToNoteDynamicsChangeFeature "music21.features.jSymbolic.AverageNoteToNoteDynamicsChangeFeature") methods

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") | * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") | * [`process()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.process "music21.features.base.FeatureExtractor.process") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## AverageNumberOfIndependentVoicesFeature

class music21.features.jSymbolic.AverageNumberOfIndependentVoicesFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#AverageNumberOfIndependentVoicesFeature)
:   Average number of different channels in which notes have sounded simultaneously.
    Rests are not included in this calculation. Here, Parts are treated as voices

    ```python
    >>> s = corpus.parse('handel/rinaldo/lascia_chio_pianga')
    >>> fe = features.jSymbolic.AverageNumberOfIndependentVoicesFeature(s)
    >>> f = fe.extract()
    >>> f.vector
    [1.528...]
    ```

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> fe = features.jSymbolic.AverageNumberOfIndependentVoicesFeature(s)
    >>> f = fe.extract()
    >>> f.vector
    [3.90...]
    ```

[`AverageNumberOfIndependentVoicesFeature`](#music21.features.jSymbolic.AverageNumberOfIndependentVoicesFeature "music21.features.jSymbolic.AverageNumberOfIndependentVoicesFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`AverageNumberOfIndependentVoicesFeature`](#music21.features.jSymbolic.AverageNumberOfIndependentVoicesFeature "music21.features.jSymbolic.AverageNumberOfIndependentVoicesFeature") methods

AverageNumberOfIndependentVoicesFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#AverageNumberOfIndependentVoicesFeature.process)
:   Do processing necessary, storing result in \_feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## AverageRangeOfGlissandosFeature

class music21.features.jSymbolic.AverageRangeOfGlissandosFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#AverageRangeOfGlissandosFeature)
:   Not yet implemented in music21

    Average range of MIDI Pitch Bends, where “range” is defined
    as the greatest value of the absolute difference between 64 and the
    second data byte of all MIDI Pitch Bend messages falling between the
    Note On and Note Off messages of any note

[`AverageRangeOfGlissandosFeature`](#music21.features.jSymbolic.AverageRangeOfGlissandosFeature "music21.features.jSymbolic.AverageRangeOfGlissandosFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`AverageRangeOfGlissandosFeature`](#music21.features.jSymbolic.AverageRangeOfGlissandosFeature "music21.features.jSymbolic.AverageRangeOfGlissandosFeature") methods

AverageRangeOfGlissandosFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#AverageRangeOfGlissandosFeature.process)
:   Do processing necessary, storing result in \_feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## AverageTimeBetweenAttacksFeature

class music21.features.jSymbolic.AverageTimeBetweenAttacksFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#AverageTimeBetweenAttacksFeature)
:   Average time in seconds between Note On events (regardless of channel).

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> for p in s.parts:
    ...     p.insert(0, tempo.MetronomeMark(number=120))
    >>> fe = features.jSymbolic.AverageTimeBetweenAttacksFeature(s)
    >>> f = fe.extract()
    >>> print(f.vector)
    [0.35]
    ```

[`AverageTimeBetweenAttacksFeature`](#music21.features.jSymbolic.AverageTimeBetweenAttacksFeature "music21.features.jSymbolic.AverageTimeBetweenAttacksFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`AverageTimeBetweenAttacksFeature`](#music21.features.jSymbolic.AverageTimeBetweenAttacksFeature "music21.features.jSymbolic.AverageTimeBetweenAttacksFeature") methods

AverageTimeBetweenAttacksFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#AverageTimeBetweenAttacksFeature.process)
:   Do processing necessary, storing result in \_feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## AverageTimeBetweenAttacksForEachVoiceFeature

class music21.features.jSymbolic.AverageTimeBetweenAttacksForEachVoiceFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#AverageTimeBetweenAttacksForEachVoiceFeature)
:   Average of average times in seconds between Note On events on individual channels
    that contain at least one note.

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> for p in s.parts:
    ...     p.insert(0, tempo.MetronomeMark(number=120))
    >>> fe = features.jSymbolic.AverageTimeBetweenAttacksForEachVoiceFeature(s)
    >>> f = fe.extract()
    >>> print(f.vector[0])
    0.442...
    ```

[`AverageTimeBetweenAttacksForEachVoiceFeature`](#music21.features.jSymbolic.AverageTimeBetweenAttacksForEachVoiceFeature "music21.features.jSymbolic.AverageTimeBetweenAttacksForEachVoiceFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`AverageTimeBetweenAttacksForEachVoiceFeature`](#music21.features.jSymbolic.AverageTimeBetweenAttacksForEachVoiceFeature "music21.features.jSymbolic.AverageTimeBetweenAttacksForEachVoiceFeature") methods

AverageTimeBetweenAttacksForEachVoiceFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#AverageTimeBetweenAttacksForEachVoiceFeature.process)
:   Do processing necessary, storing result in \_feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## AverageVariabilityOfTimeBetweenAttacksForEachVoiceFeature

class music21.features.jSymbolic.AverageVariabilityOfTimeBetweenAttacksForEachVoiceFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#AverageVariabilityOfTimeBetweenAttacksForEachVoiceFeature)
:   Average standard deviation, in seconds, of time between Note On events on individual
    channels that contain at least one note.

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> for p in s.parts:
    ...     p.insert(0, tempo.MetronomeMark(number=120))
    >>> fe = features.jSymbolic.AverageVariabilityOfTimeBetweenAttacksForEachVoiceFeature(s)
    >>> f = fe.extract()
    >>> f.vector
    [0.177...]
    ```

[`AverageVariabilityOfTimeBetweenAttacksForEachVoiceFeature`](#music21.features.jSymbolic.AverageVariabilityOfTimeBetweenAttacksForEachVoiceFeature "music21.features.jSymbolic.AverageVariabilityOfTimeBetweenAttacksForEachVoiceFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`AverageVariabilityOfTimeBetweenAttacksForEachVoiceFeature`](#music21.features.jSymbolic.AverageVariabilityOfTimeBetweenAttacksForEachVoiceFeature "music21.features.jSymbolic.AverageVariabilityOfTimeBetweenAttacksForEachVoiceFeature") methods

AverageVariabilityOfTimeBetweenAttacksForEachVoiceFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#AverageVariabilityOfTimeBetweenAttacksForEachVoiceFeature.process)
:   Do processing necessary, storing result in \_feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## BasicPitchHistogramFeature

class music21.features.jSymbolic.BasicPitchHistogramFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#BasicPitchHistogramFeature)
:   A feature extractor that finds a features array with bins corresponding
    to the values of the basic pitch histogram.

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> fe = features.jSymbolic.BasicPitchHistogramFeature(s)
    >>> f = fe.extract()
    >>> f.vector
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
     0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
     0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
     0.0, 0.0, 0.0, 0.006..., 0.0, 0.0, 0.006..., 0.006..., 0.030...,
     0.0, 0.036..., 0.012..., 0.0, 0.006..., 0.018..., 0.061..., 0.0,
     0.042..., 0.073..., 0.012..., 0.092..., 0.0, 0.116..., 0.061...,
     0.006..., 0.085..., 0.018..., 0.110..., 0.0, 0.042..., 0.055...,
     0.0, 0.049..., 0.0, 0.042..., 0.0, 0.0, 0.006..., 0.0, 0.0, 0.0,
     0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
     0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
     0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
     0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    ```

[`BasicPitchHistogramFeature`](#music21.features.jSymbolic.BasicPitchHistogramFeature "music21.features.jSymbolic.BasicPitchHistogramFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`BasicPitchHistogramFeature`](#music21.features.jSymbolic.BasicPitchHistogramFeature "music21.features.jSymbolic.BasicPitchHistogramFeature") methods

BasicPitchHistogramFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#BasicPitchHistogramFeature.process)
:   Do processing necessary, storing result in feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## BeatHistogramFeature

class music21.features.jSymbolic.BeatHistogramFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#BeatHistogramFeature)
:   Not yet implemented

    A feature extractor that finds a feature array with entries corresponding to the frequency
    values of each of the bins of the beat histogram (except the first 40 empty ones).

[`BeatHistogramFeature`](#music21.features.jSymbolic.BeatHistogramFeature "music21.features.jSymbolic.BeatHistogramFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`BeatHistogramFeature`](#music21.features.jSymbolic.BeatHistogramFeature "music21.features.jSymbolic.BeatHistogramFeature") methods

BeatHistogramFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#BeatHistogramFeature.process)
:   Do processing necessary, storing result in \_feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## BrassFractionFeature

class music21.features.jSymbolic.BrassFractionFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#BrassFractionFeature)
:   A feature extractor that extracts the fraction of all Note Ons
    belonging to brass patches (General MIDI patches 57 through 68).

    TODO: Conflict in source: only does 57-62?

    ```python
    >>> s1 = stream.Stream()
    >>> s1.append(instrument.SopranoSaxophone())
    >>> s1.repeatAppend(note.Note(), 6)
    >>> s1.append(instrument.Tuba())
    >>> s1.repeatAppend(note.Note(), 4)
    >>> fe = features.jSymbolic.BrassFractionFeature(s1)
    >>> print(fe.extract().vector[0])
    0.4
    ```

[`BrassFractionFeature`](#music21.features.jSymbolic.BrassFractionFeature "music21.features.jSymbolic.BrassFractionFeature") bases

* [`InstrumentFractionFeature`](#music21.features.jSymbolic.InstrumentFractionFeature "music21.features.jSymbolic.InstrumentFractionFeature")
* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`BrassFractionFeature`](#music21.features.jSymbolic.BrassFractionFeature "music21.features.jSymbolic.BrassFractionFeature") methods

Methods inherited from [`InstrumentFractionFeature`](#music21.features.jSymbolic.InstrumentFractionFeature "music21.features.jSymbolic.InstrumentFractionFeature"):

|  |  |  |
| --- | --- | --- |
| * [`process()`](#music21.features.jSymbolic.InstrumentFractionFeature.process "music21.features.jSymbolic.InstrumentFractionFeature.process") |  |  |

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## ChangesOfMeterFeature

class music21.features.jSymbolic.ChangesOfMeterFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#ChangesOfMeterFeature)
:   Returns 1 if the time signature is changed one or more
    times during the recording.

    ```python
    >>> s1 = stream.Stream()
    >>> s1.append(meter.TimeSignature('3/4'))
    >>> fe = features.jSymbolic.ChangesOfMeterFeature(s1)
    >>> fe.extract().vector
    [0]
    ```

    ```python
    >>> s2 = stream.Stream()
    >>> s2.append(meter.TimeSignature('3/4'))
    >>> s2.append(meter.TimeSignature('4/4'))
    >>> fe.setData(s2)  # change the data
    >>> fe.extract().vector
    [1]
    ```

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> fe = features.jSymbolic.ChangesOfMeterFeature(s)
    >>> f = fe.extract()
    >>> f.vector
    [0]
    ```

[`ChangesOfMeterFeature`](#music21.features.jSymbolic.ChangesOfMeterFeature "music21.features.jSymbolic.ChangesOfMeterFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`ChangesOfMeterFeature`](#music21.features.jSymbolic.ChangesOfMeterFeature "music21.features.jSymbolic.ChangesOfMeterFeature") methods

ChangesOfMeterFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#ChangesOfMeterFeature.process)
:   Do processing necessary, storing result in \_feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## ChromaticMotionFeature

class music21.features.jSymbolic.ChromaticMotionFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#ChromaticMotionFeature)
:   Fraction of melodic intervals corresponding to a semitone.

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> fe = features.jSymbolic.ChromaticMotionFeature(s)
    >>> f = fe.extract()
    >>> f.vector
    [0.220...]
    ```

[`ChromaticMotionFeature`](#music21.features.jSymbolic.ChromaticMotionFeature "music21.features.jSymbolic.ChromaticMotionFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`ChromaticMotionFeature`](#music21.features.jSymbolic.ChromaticMotionFeature "music21.features.jSymbolic.ChromaticMotionFeature") methods

ChromaticMotionFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#ChromaticMotionFeature.process)
:   Do processing necessary, storing result in feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## CombinedStrengthOfTwoStrongestRhythmicPulsesFeature

class music21.features.jSymbolic.CombinedStrengthOfTwoStrongestRhythmicPulsesFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#CombinedStrengthOfTwoStrongestRhythmicPulsesFeature)
:   The sum of the frequencies of the two beat bins of the peaks with the highest frequencies.

    ```python
    >>> sch = corpus.parse('schoenberg/opus19', 2)
    >>> for p in sch.parts:
    ...     p.insert(0, tempo.MetronomeMark('Langsam', 70))
    >>> fe = features.jSymbolic.CombinedStrengthOfTwoStrongestRhythmicPulsesFeature(sch)
    >>> fe.extract().vector[0]
    0.975...
    ```

[`CombinedStrengthOfTwoStrongestRhythmicPulsesFeature`](#music21.features.jSymbolic.CombinedStrengthOfTwoStrongestRhythmicPulsesFeature "music21.features.jSymbolic.CombinedStrengthOfTwoStrongestRhythmicPulsesFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`CombinedStrengthOfTwoStrongestRhythmicPulsesFeature`](#music21.features.jSymbolic.CombinedStrengthOfTwoStrongestRhythmicPulsesFeature "music21.features.jSymbolic.CombinedStrengthOfTwoStrongestRhythmicPulsesFeature") methods

CombinedStrengthOfTwoStrongestRhythmicPulsesFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#CombinedStrengthOfTwoStrongestRhythmicPulsesFeature.process)
:   Do processing necessary, storing result in \_feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## CompoundOrSimpleMeterFeature

class music21.features.jSymbolic.CompoundOrSimpleMeterFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#CompoundOrSimpleMeterFeature)
:   Set to 1 if the initial meter is compound (numerator of time signature
    is greater than or equal to 6 and is evenly divisible by 3) and to 0 if it is simple
    (if the above condition is not fulfilled).

    ```python
    >>> s1 = stream.Stream()
    >>> s1.append(meter.TimeSignature('3/4'))
    >>> fe = features.jSymbolic.CompoundOrSimpleMeterFeature(s1)
    >>> fe.extract().vector
    [0]
    ```

    ```python
    >>> s2 = stream.Stream()
    >>> s2.append(meter.TimeSignature('9/8'))
    >>> fe.setData(s2)  # change the data
    >>> fe.extract().vector
    [1]
    ```

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> fe = features.jSymbolic.CompoundOrSimpleMeterFeature(s)
    >>> f = fe.extract()
    >>> f.vector
    [0]
    ```

[`CompoundOrSimpleMeterFeature`](#music21.features.jSymbolic.CompoundOrSimpleMeterFeature "music21.features.jSymbolic.CompoundOrSimpleMeterFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`CompoundOrSimpleMeterFeature`](#music21.features.jSymbolic.CompoundOrSimpleMeterFeature "music21.features.jSymbolic.CompoundOrSimpleMeterFeature") methods

CompoundOrSimpleMeterFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#CompoundOrSimpleMeterFeature.process)
:   Do processing necessary, storing result in \_feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## DirectionOfMotionFeature

class music21.features.jSymbolic.DirectionOfMotionFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#DirectionOfMotionFeature)
:   Returns the fraction of melodic intervals that are rising rather than falling.
    Unisons are omitted.

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> fe = features.jSymbolic.DirectionOfMotionFeature(s)
    >>> f = fe.extract()
    >>> f.vector
    [0.470...]
    ```

[`DirectionOfMotionFeature`](#music21.features.jSymbolic.DirectionOfMotionFeature "music21.features.jSymbolic.DirectionOfMotionFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`DirectionOfMotionFeature`](#music21.features.jSymbolic.DirectionOfMotionFeature "music21.features.jSymbolic.DirectionOfMotionFeature") methods

DirectionOfMotionFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#DirectionOfMotionFeature.process)
:   Do processing necessary, storing result in feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## DistanceBetweenMostCommonMelodicIntervalsFeature

class music21.features.jSymbolic.DistanceBetweenMostCommonMelodicIntervalsFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#DistanceBetweenMostCommonMelodicIntervalsFeature)
:   ```python
    >>> s = corpus.parse('bwv66.6')
    >>> fe = features.jSymbolic.DistanceBetweenMostCommonMelodicIntervalsFeature(s)
    >>> f = fe.extract()
    >>> f.vector
    [1]
    ```

[`DistanceBetweenMostCommonMelodicIntervalsFeature`](#music21.features.jSymbolic.DistanceBetweenMostCommonMelodicIntervalsFeature "music21.features.jSymbolic.DistanceBetweenMostCommonMelodicIntervalsFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`DistanceBetweenMostCommonMelodicIntervalsFeature`](#music21.features.jSymbolic.DistanceBetweenMostCommonMelodicIntervalsFeature "music21.features.jSymbolic.DistanceBetweenMostCommonMelodicIntervalsFeature") methods

DistanceBetweenMostCommonMelodicIntervalsFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#DistanceBetweenMostCommonMelodicIntervalsFeature.process)
:   Do processing necessary, storing result in feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## DominantSpreadFeature

class music21.features.jSymbolic.DominantSpreadFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#DominantSpreadFeature)
:   Not implemented

    Largest number of consecutive pitch classes separated by perfect
    5ths that accounted for at least 9% each of the notes.

[`DominantSpreadFeature`](#music21.features.jSymbolic.DominantSpreadFeature "music21.features.jSymbolic.DominantSpreadFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`DominantSpreadFeature`](#music21.features.jSymbolic.DominantSpreadFeature "music21.features.jSymbolic.DominantSpreadFeature") methods

DominantSpreadFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#DominantSpreadFeature.process)
:   Do processing necessary, storing result in \_feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## DurationFeature

class music21.features.jSymbolic.DurationFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#DurationFeature)
:   A feature extractor that extracts the duration of the piece in seconds.

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> for p in s.parts:
    ...     p.insert(0, tempo.MetronomeMark(number=120))
    >>> fe = features.jSymbolic.DurationFeature(s)
    >>> f = fe.extract()
    >>> f.vector[0]
    18.0
    ```

[`DurationFeature`](#music21.features.jSymbolic.DurationFeature "music21.features.jSymbolic.DurationFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`DurationFeature`](#music21.features.jSymbolic.DurationFeature "music21.features.jSymbolic.DurationFeature") methods

DurationFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#DurationFeature.process)
:   Do processing necessary, storing result in \_feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## DurationOfMelodicArcsFeature

class music21.features.jSymbolic.DurationOfMelodicArcsFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#DurationOfMelodicArcsFeature)
:   Average number of notes that separate melodic peaks and troughs
    in any part. This is calculated as the total number of intervals
    (not counting unisons) divided by the number of times the melody
    changes direction.

    Example: C D E D C D E C C
    Intervals: [0] 2 2 -2 -2 2 2 -4 0
    Changes direction (equivalent to +/- sign) three times.
    There are seven non-unison (nonzero) intervals.
    Thus, the duration of arcs is 7/3 ~= 2.333…

    ```python
    >>> s = converter.parse("tinyNotation: c' d' e' d' c' d' e'2 c'2 c'2")
    >>> fe = features.jSymbolic.DurationOfMelodicArcsFeature(s)
    >>> fe.extract().vector
    [2.333...]
    ```

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> fe = features.jSymbolic.DurationOfMelodicArcsFeature(s)
    >>> fe.extract().vector
    [1.74...]
    ```

[`DurationOfMelodicArcsFeature`](#music21.features.jSymbolic.DurationOfMelodicArcsFeature "music21.features.jSymbolic.DurationOfMelodicArcsFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`DurationOfMelodicArcsFeature`](#music21.features.jSymbolic.DurationOfMelodicArcsFeature "music21.features.jSymbolic.DurationOfMelodicArcsFeature") methods

DurationOfMelodicArcsFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#DurationOfMelodicArcsFeature.process)
:   Do processing necessary, storing result in feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## ElectricGuitarFractionFeature

class music21.features.jSymbolic.ElectricGuitarFractionFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#ElectricGuitarFractionFeature)
:   ```python
    >>> s1 = stream.Stream()
    >>> s1.append(instrument.ElectricGuitar())
    >>> s1.repeatAppend(note.Note(), 4)
    >>> s1.append(instrument.Tuba())
    >>> s1.repeatAppend(note.Note(), 4)
    >>> fe = features.jSymbolic.ElectricGuitarFractionFeature(s1)
    >>> fe.extract().vector
    [0.5]
    ```

[`ElectricGuitarFractionFeature`](#music21.features.jSymbolic.ElectricGuitarFractionFeature "music21.features.jSymbolic.ElectricGuitarFractionFeature") bases

* [`InstrumentFractionFeature`](#music21.features.jSymbolic.InstrumentFractionFeature "music21.features.jSymbolic.InstrumentFractionFeature")
* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`ElectricGuitarFractionFeature`](#music21.features.jSymbolic.ElectricGuitarFractionFeature "music21.features.jSymbolic.ElectricGuitarFractionFeature") methods

Methods inherited from [`InstrumentFractionFeature`](#music21.features.jSymbolic.InstrumentFractionFeature "music21.features.jSymbolic.InstrumentFractionFeature"):

|  |  |  |
| --- | --- | --- |
| * [`process()`](#music21.features.jSymbolic.InstrumentFractionFeature.process "music21.features.jSymbolic.InstrumentFractionFeature.process") |  |  |

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## ElectricInstrumentFractionFeature

class music21.features.jSymbolic.ElectricInstrumentFractionFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#ElectricInstrumentFractionFeature)
:   Fraction of all Note Ons belonging to electric instrument patches
    (General MIDI patches 5, 6, 17, 19, 27 through 32, 24 through 40).

    ```python
    >>> s1 = stream.Stream()
    >>> s1.append(instrument.ElectricOrgan())
    >>> s1.repeatAppend(note.Note(), 8)
    >>> s1.append(instrument.Tuba())
    >>> s1.repeatAppend(note.Note(), 2)
    >>> fe = features.jSymbolic.ElectricInstrumentFractionFeature(s1)
    >>> print(fe.extract().vector[0])
    0.8
    ```

[`ElectricInstrumentFractionFeature`](#music21.features.jSymbolic.ElectricInstrumentFractionFeature "music21.features.jSymbolic.ElectricInstrumentFractionFeature") bases

* [`InstrumentFractionFeature`](#music21.features.jSymbolic.InstrumentFractionFeature "music21.features.jSymbolic.InstrumentFractionFeature")
* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`ElectricInstrumentFractionFeature`](#music21.features.jSymbolic.ElectricInstrumentFractionFeature "music21.features.jSymbolic.ElectricInstrumentFractionFeature") methods

Methods inherited from [`InstrumentFractionFeature`](#music21.features.jSymbolic.InstrumentFractionFeature "music21.features.jSymbolic.InstrumentFractionFeature"):

|  |  |  |
| --- | --- | --- |
| * [`process()`](#music21.features.jSymbolic.InstrumentFractionFeature.process "music21.features.jSymbolic.InstrumentFractionFeature.process") |  |  |

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## FifthsPitchHistogramFeature

class music21.features.jSymbolic.FifthsPitchHistogramFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#FifthsPitchHistogramFeature)
:   A feature array with bins corresponding to the values of the 5ths pitch class
    histogram. Instead of the bins being arranged according to semitones –
    [C, C#, D, etc.] – they are arranged according to the circle of fifths:
    [C, G, D, A, E, B, F#, C#, G#, D#, A#, F]. Viewing such a histogram
    may draw attention to the prevalence of a tonal center, including the
    prevalence of dominant relationships in the piece.

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> fe = features.jSymbolic.FifthsPitchHistogramFeature(s)
    >>> f = fe.extract()
    >>> f.vector
    [0.0, 0.0, 0.073..., 0.134..., 0.098..., 0.171..., 0.177..., 0.196...,
     0.085..., 0.006..., 0.018..., 0.036...]
    ```

[`FifthsPitchHistogramFeature`](#music21.features.jSymbolic.FifthsPitchHistogramFeature "music21.features.jSymbolic.FifthsPitchHistogramFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`FifthsPitchHistogramFeature`](#music21.features.jSymbolic.FifthsPitchHistogramFeature "music21.features.jSymbolic.FifthsPitchHistogramFeature") methods

FifthsPitchHistogramFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#FifthsPitchHistogramFeature.process)
:   Do processing necessary, storing result in feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## GlissandoPrevalenceFeature

class music21.features.jSymbolic.GlissandoPrevalenceFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#GlissandoPrevalenceFeature)
:   Not yet implemented in music21

    Number of Note Ons that have at least one MIDI Pitch Bend associated
    with them divided by total number of pitched Note Ons.

[`GlissandoPrevalenceFeature`](#music21.features.jSymbolic.GlissandoPrevalenceFeature "music21.features.jSymbolic.GlissandoPrevalenceFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`GlissandoPrevalenceFeature`](#music21.features.jSymbolic.GlissandoPrevalenceFeature "music21.features.jSymbolic.GlissandoPrevalenceFeature") methods

GlissandoPrevalenceFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#GlissandoPrevalenceFeature.process)
:   Do processing necessary, storing result in \_feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## HarmonicityOfTwoStrongestRhythmicPulsesFeature

class music21.features.jSymbolic.HarmonicityOfTwoStrongestRhythmicPulsesFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#HarmonicityOfTwoStrongestRhythmicPulsesFeature)
:   The bin label of the higher (in terms of bin label) of the two beat bins of the
    peaks with the highest frequency divided by the bin label of the lower.

    ```python
    >>> sch = corpus.parse('schoenberg/opus19', 2)
    >>> for p in sch.parts:
    ...     p.insert(0, tempo.MetronomeMark('Langsam', 70))
    >>> fe = features.jSymbolic.HarmonicityOfTwoStrongestRhythmicPulsesFeature(sch)
    >>> f = fe.extract()
    >>> f.vector[0]
    2.0
    ```

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> fe = features.jSymbolic.HarmonicityOfTwoStrongestRhythmicPulsesFeature(s)
    >>> f = fe.extract()
    >>> f.vector
    [0.5]
    ```

[`HarmonicityOfTwoStrongestRhythmicPulsesFeature`](#music21.features.jSymbolic.HarmonicityOfTwoStrongestRhythmicPulsesFeature "music21.features.jSymbolic.HarmonicityOfTwoStrongestRhythmicPulsesFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`HarmonicityOfTwoStrongestRhythmicPulsesFeature`](#music21.features.jSymbolic.HarmonicityOfTwoStrongestRhythmicPulsesFeature "music21.features.jSymbolic.HarmonicityOfTwoStrongestRhythmicPulsesFeature") methods

HarmonicityOfTwoStrongestRhythmicPulsesFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#HarmonicityOfTwoStrongestRhythmicPulsesFeature.process)
:   Do processing necessary, storing result in \_feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## ImportanceOfBassRegisterFeature

class music21.features.jSymbolic.ImportanceOfBassRegisterFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#ImportanceOfBassRegisterFeature)
:   Fraction of Notes between MIDI pitches 0 and 54.

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> fe = features.jSymbolic.ImportanceOfBassRegisterFeature(s)
    >>> fe.extract().vector
    [0.184...]
    ```

[`ImportanceOfBassRegisterFeature`](#music21.features.jSymbolic.ImportanceOfBassRegisterFeature "music21.features.jSymbolic.ImportanceOfBassRegisterFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`ImportanceOfBassRegisterFeature`](#music21.features.jSymbolic.ImportanceOfBassRegisterFeature "music21.features.jSymbolic.ImportanceOfBassRegisterFeature") methods

ImportanceOfBassRegisterFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#ImportanceOfBassRegisterFeature.process)
:   Do processing necessary, storing result in feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## ImportanceOfHighRegisterFeature

class music21.features.jSymbolic.ImportanceOfHighRegisterFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#ImportanceOfHighRegisterFeature)
:   Fraction of Notes between MIDI pitches 73 and 127.

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> fe = features.jSymbolic.ImportanceOfHighRegisterFeature(s)
    >>> fe.extract().vector
    [0.049...]
    ```

[`ImportanceOfHighRegisterFeature`](#music21.features.jSymbolic.ImportanceOfHighRegisterFeature "music21.features.jSymbolic.ImportanceOfHighRegisterFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`ImportanceOfHighRegisterFeature`](#music21.features.jSymbolic.ImportanceOfHighRegisterFeature "music21.features.jSymbolic.ImportanceOfHighRegisterFeature") methods

ImportanceOfHighRegisterFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#ImportanceOfHighRegisterFeature.process)
:   Do processing necessary, storing result in feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## ImportanceOfLoudestVoiceFeature

class music21.features.jSymbolic.ImportanceOfLoudestVoiceFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#ImportanceOfLoudestVoiceFeature)
:   Not implemented

    TODO: implement

[`ImportanceOfLoudestVoiceFeature`](#music21.features.jSymbolic.ImportanceOfLoudestVoiceFeature "music21.features.jSymbolic.ImportanceOfLoudestVoiceFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`ImportanceOfLoudestVoiceFeature`](#music21.features.jSymbolic.ImportanceOfLoudestVoiceFeature "music21.features.jSymbolic.ImportanceOfLoudestVoiceFeature") methods

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") | * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") | * [`process()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.process "music21.features.base.FeatureExtractor.process") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## ImportanceOfMiddleRegisterFeature

class music21.features.jSymbolic.ImportanceOfMiddleRegisterFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#ImportanceOfMiddleRegisterFeature)
:   Fraction of Notes between MIDI pitches 55 and 72

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> fe = features.jSymbolic.ImportanceOfMiddleRegisterFeature(s)
    >>> fe.extract().vector
    [0.766...]
    ```

[`ImportanceOfMiddleRegisterFeature`](#music21.features.jSymbolic.ImportanceOfMiddleRegisterFeature "music21.features.jSymbolic.ImportanceOfMiddleRegisterFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`ImportanceOfMiddleRegisterFeature`](#music21.features.jSymbolic.ImportanceOfMiddleRegisterFeature "music21.features.jSymbolic.ImportanceOfMiddleRegisterFeature") methods

ImportanceOfMiddleRegisterFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#ImportanceOfMiddleRegisterFeature.process)
:   Do processing necessary, storing result in feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## InitialTempoFeature

class music21.features.jSymbolic.InitialTempoFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#InitialTempoFeature)
:   Tempo in beats per minute at the start of the recording.

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> fe = features.jSymbolic.InitialTempoFeature(s)
    >>> f = fe.extract()
    >>> f.vector  # a default
    [96.0]
    ```

[`InitialTempoFeature`](#music21.features.jSymbolic.InitialTempoFeature "music21.features.jSymbolic.InitialTempoFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`InitialTempoFeature`](#music21.features.jSymbolic.InitialTempoFeature "music21.features.jSymbolic.InitialTempoFeature") methods

InitialTempoFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#InitialTempoFeature.process)
:   Do processing necessary, storing result in \_feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## InitialTimeSignatureFeature

class music21.features.jSymbolic.InitialTimeSignatureFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#InitialTimeSignatureFeature)
:   A feature array with two elements. The first is the numerator of the first occurring
    time signature and the second is the denominator of the first occurring time signature.
    Both are set to 0 if no time signature is present.

    ```python
    >>> s1 = stream.Stream()
    >>> s1.append(meter.TimeSignature('3/4'))
    >>> fe = features.jSymbolic.InitialTimeSignatureFeature(s1)
    >>> fe.extract().vector
    [3, 4]
    ```

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> fe = features.jSymbolic.InitialTimeSignatureFeature(s)
    >>> f = fe.extract()
    >>> f.vector
    [4, 4]
    ```

[`InitialTimeSignatureFeature`](#music21.features.jSymbolic.InitialTimeSignatureFeature "music21.features.jSymbolic.InitialTimeSignatureFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`InitialTimeSignatureFeature`](#music21.features.jSymbolic.InitialTimeSignatureFeature "music21.features.jSymbolic.InitialTimeSignatureFeature") methods

InitialTimeSignatureFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#InitialTimeSignatureFeature.process)
:   Do processing necessary, storing result in \_feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## InstrumentFractionFeature

class music21.features.jSymbolic.InstrumentFractionFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#InstrumentFractionFeature)
:   TODO: Add description of feature

    This subclass is in-turn subclassed by all FeatureExtractors that
    look at the proportional usage of an Instrument

[`InstrumentFractionFeature`](#music21.features.jSymbolic.InstrumentFractionFeature "music21.features.jSymbolic.InstrumentFractionFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`InstrumentFractionFeature`](#music21.features.jSymbolic.InstrumentFractionFeature "music21.features.jSymbolic.InstrumentFractionFeature") methods

InstrumentFractionFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#InstrumentFractionFeature.process)
:   Do processing necessary, storing result in feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## IntervalBetweenStrongestPitchClassesFeature

class music21.features.jSymbolic.IntervalBetweenStrongestPitchClassesFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#IntervalBetweenStrongestPitchClassesFeature)
:   ```python
    >>> s = corpus.parse('bwv66.6')
    >>> fe = features.jSymbolic.IntervalBetweenStrongestPitchClassesFeature(s)
    >>> fe.extract().vector
    [5]
    ```

[`IntervalBetweenStrongestPitchClassesFeature`](#music21.features.jSymbolic.IntervalBetweenStrongestPitchClassesFeature "music21.features.jSymbolic.IntervalBetweenStrongestPitchClassesFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`IntervalBetweenStrongestPitchClassesFeature`](#music21.features.jSymbolic.IntervalBetweenStrongestPitchClassesFeature "music21.features.jSymbolic.IntervalBetweenStrongestPitchClassesFeature") methods

IntervalBetweenStrongestPitchClassesFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#IntervalBetweenStrongestPitchClassesFeature.process)
:   Do processing necessary, storing result in feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## IntervalBetweenStrongestPitchesFeature

class music21.features.jSymbolic.IntervalBetweenStrongestPitchesFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#IntervalBetweenStrongestPitchesFeature)
:   Absolute value of the difference between the pitches of the two most common MIDI pitches.

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> fe = features.jSymbolic.IntervalBetweenStrongestPitchesFeature(s)
    >>> fe.extract().vector
    [5]
    ```

[`IntervalBetweenStrongestPitchesFeature`](#music21.features.jSymbolic.IntervalBetweenStrongestPitchesFeature "music21.features.jSymbolic.IntervalBetweenStrongestPitchesFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`IntervalBetweenStrongestPitchesFeature`](#music21.features.jSymbolic.IntervalBetweenStrongestPitchesFeature "music21.features.jSymbolic.IntervalBetweenStrongestPitchesFeature") methods

IntervalBetweenStrongestPitchesFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#IntervalBetweenStrongestPitchesFeature.process)
:   Do processing necessary, storing result in feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## MaximumNoteDurationFeature

class music21.features.jSymbolic.MaximumNoteDurationFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#MaximumNoteDurationFeature)
:   Duration of the longest note (in seconds).

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> fe = features.jSymbolic.MaximumNoteDurationFeature(s)
    >>> f = fe.extract()
    >>> f.vector
    [1.25]
    ```

[`MaximumNoteDurationFeature`](#music21.features.jSymbolic.MaximumNoteDurationFeature "music21.features.jSymbolic.MaximumNoteDurationFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`MaximumNoteDurationFeature`](#music21.features.jSymbolic.MaximumNoteDurationFeature "music21.features.jSymbolic.MaximumNoteDurationFeature") methods

MaximumNoteDurationFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#MaximumNoteDurationFeature.process)
:   Do processing necessary, storing result in \_feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## MaximumNumberOfIndependentVoicesFeature

class music21.features.jSymbolic.MaximumNumberOfIndependentVoicesFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#MaximumNumberOfIndependentVoicesFeature)
:   Maximum number of different channels in which notes have sounded simultaneously.
    Here, Parts are treated as channels.

    ```python
    >>> s = corpus.parse('handel/rinaldo/lascia_chio_pianga')
    >>> fe = features.jSymbolic.MaximumNumberOfIndependentVoicesFeature(s)
    >>> f = fe.extract()
    >>> f.vector
    [3]
    ```

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> fe = features.jSymbolic.MaximumNumberOfIndependentVoicesFeature(s)
    >>> f = fe.extract()
    >>> f.vector
    [4]
    ```

[`MaximumNumberOfIndependentVoicesFeature`](#music21.features.jSymbolic.MaximumNumberOfIndependentVoicesFeature "music21.features.jSymbolic.MaximumNumberOfIndependentVoicesFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`MaximumNumberOfIndependentVoicesFeature`](#music21.features.jSymbolic.MaximumNumberOfIndependentVoicesFeature "music21.features.jSymbolic.MaximumNumberOfIndependentVoicesFeature") methods

MaximumNumberOfIndependentVoicesFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#MaximumNumberOfIndependentVoicesFeature.process)
:   Do processing necessary, storing result in \_feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## MelodicFifthsFeature

class music21.features.jSymbolic.MelodicFifthsFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#MelodicFifthsFeature)
:   Fraction of melodic intervals that are perfect fifths

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> fe = features.jSymbolic.MelodicFifthsFeature(s)
    >>> f = fe.extract()
    >>> f.vector
    [0.056...]
    ```

[`MelodicFifthsFeature`](#music21.features.jSymbolic.MelodicFifthsFeature "music21.features.jSymbolic.MelodicFifthsFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`MelodicFifthsFeature`](#music21.features.jSymbolic.MelodicFifthsFeature "music21.features.jSymbolic.MelodicFifthsFeature") methods

MelodicFifthsFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#MelodicFifthsFeature.process)
:   Do processing necessary, storing result in feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## MelodicIntervalHistogramFeature

class music21.features.jSymbolic.MelodicIntervalHistogramFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#MelodicIntervalHistogramFeature)
:   A features array with bins corresponding to the values of the melodic interval histogram.

    128 dimensions

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> fe = features.jSymbolic.MelodicIntervalHistogramFeature(s)
    >>> f = fe.extract()
    >>> f.vector[0:5]
    [0.144..., 0.220..., 0.364..., 0.062..., 0.050...]
    ```

[`MelodicIntervalHistogramFeature`](#music21.features.jSymbolic.MelodicIntervalHistogramFeature "music21.features.jSymbolic.MelodicIntervalHistogramFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`MelodicIntervalHistogramFeature`](#music21.features.jSymbolic.MelodicIntervalHistogramFeature "music21.features.jSymbolic.MelodicIntervalHistogramFeature") methods

MelodicIntervalHistogramFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#MelodicIntervalHistogramFeature.process)
:   Do processing necessary, storing result in feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## MelodicIntervalsInLowestLineFeature

class music21.features.jSymbolic.MelodicIntervalsInLowestLineFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#MelodicIntervalsInLowestLineFeature)
:   Not implemented

    TODO: implement

[`MelodicIntervalsInLowestLineFeature`](#music21.features.jSymbolic.MelodicIntervalsInLowestLineFeature "music21.features.jSymbolic.MelodicIntervalsInLowestLineFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`MelodicIntervalsInLowestLineFeature`](#music21.features.jSymbolic.MelodicIntervalsInLowestLineFeature "music21.features.jSymbolic.MelodicIntervalsInLowestLineFeature") methods

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") | * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") | * [`process()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.process "music21.features.base.FeatureExtractor.process") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## MelodicOctavesFeature

class music21.features.jSymbolic.MelodicOctavesFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#MelodicOctavesFeature)
:   Fraction of melodic intervals that are octaves

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> fe = features.jSymbolic.MelodicOctavesFeature(s)
    >>> f = fe.extract()
    >>> f.vector
    [0.018...]
    ```

[`MelodicOctavesFeature`](#music21.features.jSymbolic.MelodicOctavesFeature "music21.features.jSymbolic.MelodicOctavesFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`MelodicOctavesFeature`](#music21.features.jSymbolic.MelodicOctavesFeature "music21.features.jSymbolic.MelodicOctavesFeature") methods

MelodicOctavesFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#MelodicOctavesFeature.process)
:   Do processing necessary, storing result in feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## MelodicThirdsFeature

class music21.features.jSymbolic.MelodicThirdsFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#MelodicThirdsFeature)
:   Fraction of melodic intervals that are major or minor thirds

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> fe = features.jSymbolic.MelodicThirdsFeature(s)
    >>> f = fe.extract()
    >>> f.vector
    [0.113...]
    ```

[`MelodicThirdsFeature`](#music21.features.jSymbolic.MelodicThirdsFeature "music21.features.jSymbolic.MelodicThirdsFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`MelodicThirdsFeature`](#music21.features.jSymbolic.MelodicThirdsFeature "music21.features.jSymbolic.MelodicThirdsFeature") methods

MelodicThirdsFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#MelodicThirdsFeature.process)
:   Do processing necessary, storing result in feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## MelodicTritonesFeature

class music21.features.jSymbolic.MelodicTritonesFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#MelodicTritonesFeature)
:   Fraction of melodic intervals that are tritones

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> fe = features.jSymbolic.MelodicTritonesFeature(s)
    >>> f = fe.extract()
    >>> f.vector
    [0.012...]
    ```

[`MelodicTritonesFeature`](#music21.features.jSymbolic.MelodicTritonesFeature "music21.features.jSymbolic.MelodicTritonesFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`MelodicTritonesFeature`](#music21.features.jSymbolic.MelodicTritonesFeature "music21.features.jSymbolic.MelodicTritonesFeature") methods

MelodicTritonesFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#MelodicTritonesFeature.process)
:   Do processing necessary, storing result in feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## MinimumNoteDurationFeature

class music21.features.jSymbolic.MinimumNoteDurationFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#MinimumNoteDurationFeature)
:   Duration of the shortest note (in seconds).

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> fe = features.jSymbolic.MinimumNoteDurationFeature(s)
    >>> f = fe.extract()
    >>> f.vector
    [0.3125]
    ```

[`MinimumNoteDurationFeature`](#music21.features.jSymbolic.MinimumNoteDurationFeature "music21.features.jSymbolic.MinimumNoteDurationFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`MinimumNoteDurationFeature`](#music21.features.jSymbolic.MinimumNoteDurationFeature "music21.features.jSymbolic.MinimumNoteDurationFeature") methods

MinimumNoteDurationFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#MinimumNoteDurationFeature.process)
:   Do processing necessary, storing result in \_feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## MostCommonMelodicIntervalFeature

class music21.features.jSymbolic.MostCommonMelodicIntervalFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#MostCommonMelodicIntervalFeature)
:   ```python
    >>> s = corpus.parse('bwv66.6')
    >>> fe = features.jSymbolic.MostCommonMelodicIntervalFeature(s)
    >>> f = fe.extract()
    >>> f.vector
    [2]
    ```

[`MostCommonMelodicIntervalFeature`](#music21.features.jSymbolic.MostCommonMelodicIntervalFeature "music21.features.jSymbolic.MostCommonMelodicIntervalFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`MostCommonMelodicIntervalFeature`](#music21.features.jSymbolic.MostCommonMelodicIntervalFeature "music21.features.jSymbolic.MostCommonMelodicIntervalFeature") methods

MostCommonMelodicIntervalFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#MostCommonMelodicIntervalFeature.process)
:   Do processing necessary, storing result in feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## MostCommonMelodicIntervalPrevalenceFeature

class music21.features.jSymbolic.MostCommonMelodicIntervalPrevalenceFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#MostCommonMelodicIntervalPrevalenceFeature)
:   Fraction of melodic intervals that belong to the most common interval.

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> fe = features.jSymbolic.MostCommonMelodicIntervalPrevalenceFeature(s)
    >>> f = fe.extract()
    >>> f.vector
    [0.364...]
    ```

[`MostCommonMelodicIntervalPrevalenceFeature`](#music21.features.jSymbolic.MostCommonMelodicIntervalPrevalenceFeature "music21.features.jSymbolic.MostCommonMelodicIntervalPrevalenceFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`MostCommonMelodicIntervalPrevalenceFeature`](#music21.features.jSymbolic.MostCommonMelodicIntervalPrevalenceFeature "music21.features.jSymbolic.MostCommonMelodicIntervalPrevalenceFeature") methods

MostCommonMelodicIntervalPrevalenceFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#MostCommonMelodicIntervalPrevalenceFeature.process)
:   Do processing necessary, storing result in feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## MostCommonPitchClassFeature

class music21.features.jSymbolic.MostCommonPitchClassFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#MostCommonPitchClassFeature)
:   Bin label of the most common pitch class.

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> fe = features.jSymbolic.MostCommonPitchClassFeature(s)
    >>> fe.extract().vector
    [1]
    ```

[`MostCommonPitchClassFeature`](#music21.features.jSymbolic.MostCommonPitchClassFeature "music21.features.jSymbolic.MostCommonPitchClassFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`MostCommonPitchClassFeature`](#music21.features.jSymbolic.MostCommonPitchClassFeature "music21.features.jSymbolic.MostCommonPitchClassFeature") methods

MostCommonPitchClassFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#MostCommonPitchClassFeature.process)
:   Do processing necessary, storing result in feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## MostCommonPitchClassPrevalenceFeature

class music21.features.jSymbolic.MostCommonPitchClassPrevalenceFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#MostCommonPitchClassPrevalenceFeature)
:   Fraction of Notes corresponding to the most common pitch class.

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> fe = features.jSymbolic.MostCommonPitchClassPrevalenceFeature(s)
    >>> fe.extract().vector
    [0.196...]
    ```

[`MostCommonPitchClassPrevalenceFeature`](#music21.features.jSymbolic.MostCommonPitchClassPrevalenceFeature "music21.features.jSymbolic.MostCommonPitchClassPrevalenceFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`MostCommonPitchClassPrevalenceFeature`](#music21.features.jSymbolic.MostCommonPitchClassPrevalenceFeature "music21.features.jSymbolic.MostCommonPitchClassPrevalenceFeature") methods

MostCommonPitchClassPrevalenceFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#MostCommonPitchClassPrevalenceFeature.process)
:   Do processing necessary, storing result in feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## MostCommonPitchFeature

class music21.features.jSymbolic.MostCommonPitchFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#MostCommonPitchFeature)
:   Bin label of the most common pitch.

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> fe = features.jSymbolic.MostCommonPitchFeature(s)
    >>> fe.extract().vector
    [61]
    ```

[`MostCommonPitchFeature`](#music21.features.jSymbolic.MostCommonPitchFeature "music21.features.jSymbolic.MostCommonPitchFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`MostCommonPitchFeature`](#music21.features.jSymbolic.MostCommonPitchFeature "music21.features.jSymbolic.MostCommonPitchFeature") methods

MostCommonPitchFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#MostCommonPitchFeature.process)
:   Do processing necessary, storing result in feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## MostCommonPitchPrevalenceFeature

class music21.features.jSymbolic.MostCommonPitchPrevalenceFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#MostCommonPitchPrevalenceFeature)
:   Fraction of Notes corresponding to the most common pitch.

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> fe = features.jSymbolic.MostCommonPitchPrevalenceFeature(s)
    >>> fe.extract().vector[0]
    0.116...
    ```

[`MostCommonPitchPrevalenceFeature`](#music21.features.jSymbolic.MostCommonPitchPrevalenceFeature "music21.features.jSymbolic.MostCommonPitchPrevalenceFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`MostCommonPitchPrevalenceFeature`](#music21.features.jSymbolic.MostCommonPitchPrevalenceFeature "music21.features.jSymbolic.MostCommonPitchPrevalenceFeature") methods

MostCommonPitchPrevalenceFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#MostCommonPitchPrevalenceFeature.process)
:   Do processing necessary, storing result in feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## NoteDensityFeature

class music21.features.jSymbolic.NoteDensityFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#NoteDensityFeature)
:   Gives the average number of notes per second, taking into account
    the tempo at any moment in the piece. Unlike jSymbolic, music21
    quantizes notes from MIDI somewhat before running this test; this
    function is meant to be run on encoded MIDI scores rather than
    recorded MIDI performances.

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> fe = features.jSymbolic.NoteDensityFeature(s)
    >>> f = fe.extract()
    >>> f.vector
    [7.244...]
    ```

[`NoteDensityFeature`](#music21.features.jSymbolic.NoteDensityFeature "music21.features.jSymbolic.NoteDensityFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`NoteDensityFeature`](#music21.features.jSymbolic.NoteDensityFeature "music21.features.jSymbolic.NoteDensityFeature") methods

NoteDensityFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#NoteDensityFeature.process)
:   Do processing necessary, storing result in \_feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## NotePrevalenceOfPitchedInstrumentsFeature

class music21.features.jSymbolic.NotePrevalenceOfPitchedInstrumentsFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#NotePrevalenceOfPitchedInstrumentsFeature)
:   ```python
    >>> s1 = stream.Stream()
    >>> s1.append(instrument.AcousticGuitar())
    >>> s1.repeatAppend(note.Note(), 4)
    >>> s1.append(instrument.Tuba())
    >>> s1.append(note.Note())
    >>> fe = features.jSymbolic.NotePrevalenceOfPitchedInstrumentsFeature(s1)
    >>> fe.extract().vector
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0.8..., 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.2...,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ```

    .midiProgram cannot be None:

    ```python
    >>> s1.getInstruments().first().midiProgram = None
    >>> fe2 = features.jSymbolic.NotePrevalenceOfPitchedInstrumentsFeature(s1)
    >>> fe2.extract()
    Traceback (most recent call last):
    music21.features.jSymbolic.JSymbolicFeatureException: Acoustic Guitar lacks a midiProgram
    ```

[`NotePrevalenceOfPitchedInstrumentsFeature`](#music21.features.jSymbolic.NotePrevalenceOfPitchedInstrumentsFeature "music21.features.jSymbolic.NotePrevalenceOfPitchedInstrumentsFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`NotePrevalenceOfPitchedInstrumentsFeature`](#music21.features.jSymbolic.NotePrevalenceOfPitchedInstrumentsFeature "music21.features.jSymbolic.NotePrevalenceOfPitchedInstrumentsFeature") methods

NotePrevalenceOfPitchedInstrumentsFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#NotePrevalenceOfPitchedInstrumentsFeature.process)
:   Do processing necessary, storing result in feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## NotePrevalenceOfUnpitchedInstrumentsFeature

class music21.features.jSymbolic.NotePrevalenceOfUnpitchedInstrumentsFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#NotePrevalenceOfUnpitchedInstrumentsFeature)
:   Not implemented

    TODO: implement

[`NotePrevalenceOfUnpitchedInstrumentsFeature`](#music21.features.jSymbolic.NotePrevalenceOfUnpitchedInstrumentsFeature "music21.features.jSymbolic.NotePrevalenceOfUnpitchedInstrumentsFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`NotePrevalenceOfUnpitchedInstrumentsFeature`](#music21.features.jSymbolic.NotePrevalenceOfUnpitchedInstrumentsFeature "music21.features.jSymbolic.NotePrevalenceOfUnpitchedInstrumentsFeature") methods

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") | * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") | * [`process()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.process "music21.features.base.FeatureExtractor.process") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## NumberOfCommonMelodicIntervalsFeature

class music21.features.jSymbolic.NumberOfCommonMelodicIntervalsFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#NumberOfCommonMelodicIntervalsFeature)
:   Number of melodic intervals that represent at least 9% of all melodic intervals.

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> fe = features.jSymbolic.NumberOfCommonMelodicIntervalsFeature(s)
    >>> f = fe.extract()
    >>> f.vector
    [3]
    ```

[`NumberOfCommonMelodicIntervalsFeature`](#music21.features.jSymbolic.NumberOfCommonMelodicIntervalsFeature "music21.features.jSymbolic.NumberOfCommonMelodicIntervalsFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`NumberOfCommonMelodicIntervalsFeature`](#music21.features.jSymbolic.NumberOfCommonMelodicIntervalsFeature "music21.features.jSymbolic.NumberOfCommonMelodicIntervalsFeature") methods

NumberOfCommonMelodicIntervalsFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#NumberOfCommonMelodicIntervalsFeature.process)
:   Do processing necessary, storing result in feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## NumberOfCommonPitchesFeature

class music21.features.jSymbolic.NumberOfCommonPitchesFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#NumberOfCommonPitchesFeature)
:   Number of pitches that account individually for at least 9% of all notes.

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> fe = features.jSymbolic.NumberOfCommonPitchesFeature(s)
    >>> fe.extract().vector
    [3]
    ```

[`NumberOfCommonPitchesFeature`](#music21.features.jSymbolic.NumberOfCommonPitchesFeature "music21.features.jSymbolic.NumberOfCommonPitchesFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`NumberOfCommonPitchesFeature`](#music21.features.jSymbolic.NumberOfCommonPitchesFeature "music21.features.jSymbolic.NumberOfCommonPitchesFeature") methods

NumberOfCommonPitchesFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#NumberOfCommonPitchesFeature.process)
:   Do processing necessary, storing result in feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## NumberOfModeratePulsesFeature

class music21.features.jSymbolic.NumberOfModeratePulsesFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#NumberOfModeratePulsesFeature)
:   Not yet implemented

    Number of beat peaks with normalized frequencies over 0.01.

[`NumberOfModeratePulsesFeature`](#music21.features.jSymbolic.NumberOfModeratePulsesFeature "music21.features.jSymbolic.NumberOfModeratePulsesFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`NumberOfModeratePulsesFeature`](#music21.features.jSymbolic.NumberOfModeratePulsesFeature "music21.features.jSymbolic.NumberOfModeratePulsesFeature") methods

NumberOfModeratePulsesFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#NumberOfModeratePulsesFeature.process)
:   Do processing necessary, storing result in \_feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## NumberOfPitchedInstrumentsFeature

class music21.features.jSymbolic.NumberOfPitchedInstrumentsFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#NumberOfPitchedInstrumentsFeature)
:   Total number of General MIDI patches that are used to play at least one note.

    ```python
    >>> s1 = stream.Stream()
    >>> s1.append(instrument.AcousticGuitar())
    >>> s1.append(note.Note())
    >>> s1.append(instrument.Tuba())
    >>> s1.append(note.Note())
    >>> fe = features.jSymbolic.NumberOfPitchedInstrumentsFeature(s1)
    >>> fe.extract().vector
    [2]
    ```

[`NumberOfPitchedInstrumentsFeature`](#music21.features.jSymbolic.NumberOfPitchedInstrumentsFeature "music21.features.jSymbolic.NumberOfPitchedInstrumentsFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`NumberOfPitchedInstrumentsFeature`](#music21.features.jSymbolic.NumberOfPitchedInstrumentsFeature "music21.features.jSymbolic.NumberOfPitchedInstrumentsFeature") methods

NumberOfPitchedInstrumentsFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#NumberOfPitchedInstrumentsFeature.process)
:   Do processing necessary, storing result in feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## NumberOfRelativelyStrongPulsesFeature

class music21.features.jSymbolic.NumberOfRelativelyStrongPulsesFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#NumberOfRelativelyStrongPulsesFeature)
:   not yet implemented

    Number of beat peaks with frequencies at least 30% as high as the
    frequency of the bin with the highest frequency.

[`NumberOfRelativelyStrongPulsesFeature`](#music21.features.jSymbolic.NumberOfRelativelyStrongPulsesFeature "music21.features.jSymbolic.NumberOfRelativelyStrongPulsesFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`NumberOfRelativelyStrongPulsesFeature`](#music21.features.jSymbolic.NumberOfRelativelyStrongPulsesFeature "music21.features.jSymbolic.NumberOfRelativelyStrongPulsesFeature") methods

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") | * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") | * [`process()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.process "music21.features.base.FeatureExtractor.process") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## NumberOfStrongPulsesFeature

class music21.features.jSymbolic.NumberOfStrongPulsesFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#NumberOfStrongPulsesFeature)
:   Not yet implemented

    Number of beat peaks with normalized frequencies over 0.1.

[`NumberOfStrongPulsesFeature`](#music21.features.jSymbolic.NumberOfStrongPulsesFeature "music21.features.jSymbolic.NumberOfStrongPulsesFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`NumberOfStrongPulsesFeature`](#music21.features.jSymbolic.NumberOfStrongPulsesFeature "music21.features.jSymbolic.NumberOfStrongPulsesFeature") methods

NumberOfStrongPulsesFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#NumberOfStrongPulsesFeature.process)
:   Do processing necessary, storing result in \_feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## NumberOfUnpitchedInstrumentsFeature

class music21.features.jSymbolic.NumberOfUnpitchedInstrumentsFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#NumberOfUnpitchedInstrumentsFeature)
:   Not implemented

    Number of distinct MIDI Percussion Key Map patches that were used to play at
    least one note. It should be noted that only instruments 35 to 81 are
    included here, as they are the ones that are included in the official standard.

    TODO: implement

[`NumberOfUnpitchedInstrumentsFeature`](#music21.features.jSymbolic.NumberOfUnpitchedInstrumentsFeature "music21.features.jSymbolic.NumberOfUnpitchedInstrumentsFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`NumberOfUnpitchedInstrumentsFeature`](#music21.features.jSymbolic.NumberOfUnpitchedInstrumentsFeature "music21.features.jSymbolic.NumberOfUnpitchedInstrumentsFeature") methods

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") | * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") | * [`process()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.process "music21.features.base.FeatureExtractor.process") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## OrchestralStringsFractionFeature

class music21.features.jSymbolic.OrchestralStringsFractionFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#OrchestralStringsFractionFeature)
:   Fraction of all Note Ons belonging to orchestral strings patches
    (General MIDI patches 41 or 47).

    ```python
    >>> s1 = stream.Stream()
    >>> s1.append(instrument.Violoncello())
    >>> s1.repeatAppend(note.Note(), 4)
    >>> s1.append(instrument.Tuba())
    >>> s1.repeatAppend(note.Note(), 6)
    >>> fe = features.jSymbolic.OrchestralStringsFractionFeature(s1)
    >>> print(fe.extract().vector[0])
    0.4
    ```

[`OrchestralStringsFractionFeature`](#music21.features.jSymbolic.OrchestralStringsFractionFeature "music21.features.jSymbolic.OrchestralStringsFractionFeature") bases

* [`InstrumentFractionFeature`](#music21.features.jSymbolic.InstrumentFractionFeature "music21.features.jSymbolic.InstrumentFractionFeature")
* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`OrchestralStringsFractionFeature`](#music21.features.jSymbolic.OrchestralStringsFractionFeature "music21.features.jSymbolic.OrchestralStringsFractionFeature") methods

Methods inherited from [`InstrumentFractionFeature`](#music21.features.jSymbolic.InstrumentFractionFeature "music21.features.jSymbolic.InstrumentFractionFeature"):

|  |  |  |
| --- | --- | --- |
| * [`process()`](#music21.features.jSymbolic.InstrumentFractionFeature.process "music21.features.jSymbolic.InstrumentFractionFeature.process") |  |  |

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## OverallDynamicRangeFeature

class music21.features.jSymbolic.OverallDynamicRangeFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#OverallDynamicRangeFeature)
:   Not implemented

    The maximum loudness minus the minimum loudness value.

    TODO: implement

[`OverallDynamicRangeFeature`](#music21.features.jSymbolic.OverallDynamicRangeFeature "music21.features.jSymbolic.OverallDynamicRangeFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`OverallDynamicRangeFeature`](#music21.features.jSymbolic.OverallDynamicRangeFeature "music21.features.jSymbolic.OverallDynamicRangeFeature") methods

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") | * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") | * [`process()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.process "music21.features.base.FeatureExtractor.process") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## PercussionPrevalenceFeature

class music21.features.jSymbolic.PercussionPrevalenceFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#PercussionPrevalenceFeature)
:   Not implemented

    Total number of Note Ons corresponding to unpitched percussion instruments
    divided by the total number of Note Ons in the recording.

[`PercussionPrevalenceFeature`](#music21.features.jSymbolic.PercussionPrevalenceFeature "music21.features.jSymbolic.PercussionPrevalenceFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`PercussionPrevalenceFeature`](#music21.features.jSymbolic.PercussionPrevalenceFeature "music21.features.jSymbolic.PercussionPrevalenceFeature") methods

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") | * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") | * [`process()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.process "music21.features.base.FeatureExtractor.process") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## PitchClassDistributionFeature

class music21.features.jSymbolic.PitchClassDistributionFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#PitchClassDistributionFeature)
:   A feature array with 12 entries where the first holds the frequency
    of the bin of the pitch class histogram with the highest frequency,
    and the following entries holding the successive bins of the histogram,
    wrapping around if necessary.

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> fe = features.jSymbolic.PitchClassDistributionFeature(s)
    >>> f = fe.extract()
    >>> f.vector
    [0.196..., 0.073..., 0.006..., 0.098..., 0.036..., 0.177..., 0.0,
     0.085..., 0.134..., 0.018..., 0.171..., 0.0]
    ```

[`PitchClassDistributionFeature`](#music21.features.jSymbolic.PitchClassDistributionFeature "music21.features.jSymbolic.PitchClassDistributionFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`PitchClassDistributionFeature`](#music21.features.jSymbolic.PitchClassDistributionFeature "music21.features.jSymbolic.PitchClassDistributionFeature") methods

PitchClassDistributionFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#PitchClassDistributionFeature.process)
:   Do processing necessary, storing result in feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## PitchClassVarietyFeature

class music21.features.jSymbolic.PitchClassVarietyFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#PitchClassVarietyFeature)
:   Number of pitch classes used at least once.

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> fe = features.jSymbolic.PitchClassVarietyFeature(s)
    >>> fe.extract().vector
    [10]
    ```

[`PitchClassVarietyFeature`](#music21.features.jSymbolic.PitchClassVarietyFeature "music21.features.jSymbolic.PitchClassVarietyFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`PitchClassVarietyFeature`](#music21.features.jSymbolic.PitchClassVarietyFeature "music21.features.jSymbolic.PitchClassVarietyFeature") methods

PitchClassVarietyFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#PitchClassVarietyFeature.process)
:   Do processing necessary, storing result in feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## PitchVarietyFeature

class music21.features.jSymbolic.PitchVarietyFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#PitchVarietyFeature)
:   Number of pitches used at least once.

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> fe = features.jSymbolic.PitchVarietyFeature(s)
    >>> fe.extract().vector
    [24]
    ```

[`PitchVarietyFeature`](#music21.features.jSymbolic.PitchVarietyFeature "music21.features.jSymbolic.PitchVarietyFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`PitchVarietyFeature`](#music21.features.jSymbolic.PitchVarietyFeature "music21.features.jSymbolic.PitchVarietyFeature") methods

PitchVarietyFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#PitchVarietyFeature.process)
:   Do processing necessary, storing result in feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## PitchedInstrumentsPresentFeature

class music21.features.jSymbolic.PitchedInstrumentsPresentFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#PitchedInstrumentsPresentFeature)
:   Which pitched General MIDI Instruments are present. There is one entry
    for each instrument, which is set to 1.0 if there is at least one Note On
    in the recording corresponding to the instrument and to 0.0 if there is not.

    ```python
    >>> s1 = stream.Stream()
    >>> s1.append(instrument.AcousticGuitar())
    >>> s1.append(note.Note())
    >>> s1.append(instrument.Tuba())
    >>> s1.append(note.Note())
    >>> fe = features.jSymbolic.PitchedInstrumentsPresentFeature(s1)
    >>> fe.extract().vector
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ```

    Default instruments will lack a .midiProgram, so they raise exceptions:

    ```python
    >>> i = instrument.Instrument()
    >>> i.midiProgram is None
    True
    >>> s2 = stream.Stream()
    >>> s2.append(i)
    >>> s2.append(note.Note())
    >>> fe2 = features.jSymbolic.PitchedInstrumentsPresentFeature(s2)
    >>> fe2.extract()
    Traceback (most recent call last):
    music21.features.jSymbolic.JSymbolicFeatureException:
    <music21.instrument.Instrument ''> lacks a midiProgram
    ```

[`PitchedInstrumentsPresentFeature`](#music21.features.jSymbolic.PitchedInstrumentsPresentFeature "music21.features.jSymbolic.PitchedInstrumentsPresentFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`PitchedInstrumentsPresentFeature`](#music21.features.jSymbolic.PitchedInstrumentsPresentFeature "music21.features.jSymbolic.PitchedInstrumentsPresentFeature") methods

PitchedInstrumentsPresentFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#PitchedInstrumentsPresentFeature.process)
:   Do processing necessary, storing result in feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## PolyrhythmsFeature

class music21.features.jSymbolic.PolyrhythmsFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#PolyrhythmsFeature)
:   Not yet implemented

    Number of beat peaks with frequencies at least 30% of the highest frequency
    whose bin labels are not integer multiples or factors
    (using only multipliers of 1, 2, 3, 4, 6 and 8) (with an accepted
    error of +/- 3 bins) of the bin label of the peak with the highest frequency.
    This number is then divided by the total number of beat bins with frequencies
    over 30% of the highest frequency.

[`PolyrhythmsFeature`](#music21.features.jSymbolic.PolyrhythmsFeature "music21.features.jSymbolic.PolyrhythmsFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`PolyrhythmsFeature`](#music21.features.jSymbolic.PolyrhythmsFeature "music21.features.jSymbolic.PolyrhythmsFeature") methods

PolyrhythmsFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#PolyrhythmsFeature.process)
:   Do processing necessary, storing result in \_feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## PrevalenceOfMicrotonesFeature

class music21.features.jSymbolic.PrevalenceOfMicrotonesFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#PrevalenceOfMicrotonesFeature)
:   not yet implemented

    Number of Note Ons that are preceded by isolated MIDI Pitch Bend
    messages as a fraction of the total number of Note Ons.’

[`PrevalenceOfMicrotonesFeature`](#music21.features.jSymbolic.PrevalenceOfMicrotonesFeature "music21.features.jSymbolic.PrevalenceOfMicrotonesFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`PrevalenceOfMicrotonesFeature`](#music21.features.jSymbolic.PrevalenceOfMicrotonesFeature "music21.features.jSymbolic.PrevalenceOfMicrotonesFeature") methods

PrevalenceOfMicrotonesFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#PrevalenceOfMicrotonesFeature.process)
:   Do processing necessary, storing result in \_feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## PrimaryRegisterFeature

class music21.features.jSymbolic.PrimaryRegisterFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#PrimaryRegisterFeature)
:   Average MIDI pitch.

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> fe = features.jSymbolic.PrimaryRegisterFeature(s)
    >>> fe.extract().vector
    [61.12...]
    ```

[`PrimaryRegisterFeature`](#music21.features.jSymbolic.PrimaryRegisterFeature "music21.features.jSymbolic.PrimaryRegisterFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`PrimaryRegisterFeature`](#music21.features.jSymbolic.PrimaryRegisterFeature "music21.features.jSymbolic.PrimaryRegisterFeature") methods

PrimaryRegisterFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#PrimaryRegisterFeature.process)
:   Do processing necessary, storing result in feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## QualityFeature

class music21.features.jSymbolic.QualityFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#QualityFeature)
:   Set to 0 if the key signature indicates that
    a recording is major, set to 1 if it indicates
    that it is minor. In jSymbolic, this is set to 0 if key signature is unknown.

    See features.native.QualityFeature for a music21 improvement on this method

    Example: Handel, Rinaldo Aria (musicxml) is explicitly encoded as being in Major:

    ```python
    >>> s = corpus.parse('handel/rinaldo/lascia_chio_pianga')
    >>> fe = features.jSymbolic.QualityFeature(s)
    >>> f = fe.extract()
    >>> f.vector
    [0]
    ```

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> fe = features.jSymbolic.QualityFeature(s)
    >>> f = fe.extract()
    >>> f.vector
    [1]
    ```

[`QualityFeature`](#music21.features.jSymbolic.QualityFeature "music21.features.jSymbolic.QualityFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`QualityFeature`](#music21.features.jSymbolic.QualityFeature "music21.features.jSymbolic.QualityFeature") methods

QualityFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#QualityFeature.process)
:   Do processing necessary, storing result in feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## QuintupleMeterFeature

class music21.features.jSymbolic.QuintupleMeterFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#QuintupleMeterFeature)
:   Set to 1 if numerator of initial time signature is 5, set to 0 otherwise.

    ```python
    >>> s1 = stream.Stream()
    >>> s1.append(meter.TimeSignature('5/4'))
    >>> fe = features.jSymbolic.QuintupleMeterFeature(s1)
    >>> fe.extract().vector
    [1]
    ```

    ```python
    >>> s2 = stream.Stream()
    >>> s2.append(meter.TimeSignature('3/4'))
    >>> fe.setData(s2)  # change the data
    >>> fe.extract().vector
    [0]
    ```

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> fe = features.jSymbolic.QuintupleMeterFeature(s)
    >>> f = fe.extract()
    >>> f.vector
    [0]
    ```

[`QuintupleMeterFeature`](#music21.features.jSymbolic.QuintupleMeterFeature "music21.features.jSymbolic.QuintupleMeterFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`QuintupleMeterFeature`](#music21.features.jSymbolic.QuintupleMeterFeature "music21.features.jSymbolic.QuintupleMeterFeature") methods

QuintupleMeterFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#QuintupleMeterFeature.process)
:   Do processing necessary, storing result in \_feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## RangeFeature

class music21.features.jSymbolic.RangeFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#RangeFeature)
:   Difference between highest and lowest pitches. In semitones

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> fe = features.jSymbolic.RangeFeature(s)
    >>> fe.extract().vector
    [34]
    ```

[`RangeFeature`](#music21.features.jSymbolic.RangeFeature "music21.features.jSymbolic.RangeFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`RangeFeature`](#music21.features.jSymbolic.RangeFeature "music21.features.jSymbolic.RangeFeature") methods

RangeFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#RangeFeature.process)
:   Do processing necessary, storing result in feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## RangeOfHighestLineFeature

class music21.features.jSymbolic.RangeOfHighestLineFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#RangeOfHighestLineFeature)
:   Not implemented

    TODO: implement

[`RangeOfHighestLineFeature`](#music21.features.jSymbolic.RangeOfHighestLineFeature "music21.features.jSymbolic.RangeOfHighestLineFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`RangeOfHighestLineFeature`](#music21.features.jSymbolic.RangeOfHighestLineFeature "music21.features.jSymbolic.RangeOfHighestLineFeature") methods

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") | * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") | * [`process()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.process "music21.features.base.FeatureExtractor.process") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## RelativeNoteDensityOfHighestLineFeature

class music21.features.jSymbolic.RelativeNoteDensityOfHighestLineFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#RelativeNoteDensityOfHighestLineFeature)
:   Not implemented

    TODO: implement

[`RelativeNoteDensityOfHighestLineFeature`](#music21.features.jSymbolic.RelativeNoteDensityOfHighestLineFeature "music21.features.jSymbolic.RelativeNoteDensityOfHighestLineFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`RelativeNoteDensityOfHighestLineFeature`](#music21.features.jSymbolic.RelativeNoteDensityOfHighestLineFeature "music21.features.jSymbolic.RelativeNoteDensityOfHighestLineFeature") methods

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") | * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") | * [`process()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.process "music21.features.base.FeatureExtractor.process") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## RelativeRangeOfLoudestVoiceFeature

class music21.features.jSymbolic.RelativeRangeOfLoudestVoiceFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#RelativeRangeOfLoudestVoiceFeature)
:   Not implemented

    TODO: implement

[`RelativeRangeOfLoudestVoiceFeature`](#music21.features.jSymbolic.RelativeRangeOfLoudestVoiceFeature "music21.features.jSymbolic.RelativeRangeOfLoudestVoiceFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`RelativeRangeOfLoudestVoiceFeature`](#music21.features.jSymbolic.RelativeRangeOfLoudestVoiceFeature "music21.features.jSymbolic.RelativeRangeOfLoudestVoiceFeature") methods

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") | * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") | * [`process()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.process "music21.features.base.FeatureExtractor.process") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## RelativeStrengthOfMostCommonIntervalsFeature

class music21.features.jSymbolic.RelativeStrengthOfMostCommonIntervalsFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#RelativeStrengthOfMostCommonIntervalsFeature)
:   ```python
    >>> s = corpus.parse('bwv66.6')
    >>> fe = features.jSymbolic.RelativeStrengthOfMostCommonIntervalsFeature(s)
    >>> f = fe.extract()
    >>> f.vector
    [0.603...]
    ```

[`RelativeStrengthOfMostCommonIntervalsFeature`](#music21.features.jSymbolic.RelativeStrengthOfMostCommonIntervalsFeature "music21.features.jSymbolic.RelativeStrengthOfMostCommonIntervalsFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`RelativeStrengthOfMostCommonIntervalsFeature`](#music21.features.jSymbolic.RelativeStrengthOfMostCommonIntervalsFeature "music21.features.jSymbolic.RelativeStrengthOfMostCommonIntervalsFeature") methods

RelativeStrengthOfMostCommonIntervalsFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#RelativeStrengthOfMostCommonIntervalsFeature.process)
:   Do processing necessary, storing result in feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## RelativeStrengthOfTopPitchClassesFeature

class music21.features.jSymbolic.RelativeStrengthOfTopPitchClassesFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#RelativeStrengthOfTopPitchClassesFeature)
:   ```python
    >>> s = corpus.parse('bwv66.6')
    >>> fe = features.jSymbolic.RelativeStrengthOfTopPitchClassesFeature(s)
    >>> fe.extract().vector
    [0.906...]
    ```

[`RelativeStrengthOfTopPitchClassesFeature`](#music21.features.jSymbolic.RelativeStrengthOfTopPitchClassesFeature "music21.features.jSymbolic.RelativeStrengthOfTopPitchClassesFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`RelativeStrengthOfTopPitchClassesFeature`](#music21.features.jSymbolic.RelativeStrengthOfTopPitchClassesFeature "music21.features.jSymbolic.RelativeStrengthOfTopPitchClassesFeature") methods

RelativeStrengthOfTopPitchClassesFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#RelativeStrengthOfTopPitchClassesFeature.process)
:   Do processing necessary, storing result in feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## RelativeStrengthOfTopPitchesFeature

class music21.features.jSymbolic.RelativeStrengthOfTopPitchesFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#RelativeStrengthOfTopPitchesFeature)
:   The frequency of the 2nd most common pitch divided by the frequency of the most common pitch.

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> fe = features.jSymbolic.RelativeStrengthOfTopPitchesFeature(s)
    >>> fe.extract().vector
    [0.947...]
    ```

[`RelativeStrengthOfTopPitchesFeature`](#music21.features.jSymbolic.RelativeStrengthOfTopPitchesFeature "music21.features.jSymbolic.RelativeStrengthOfTopPitchesFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`RelativeStrengthOfTopPitchesFeature`](#music21.features.jSymbolic.RelativeStrengthOfTopPitchesFeature "music21.features.jSymbolic.RelativeStrengthOfTopPitchesFeature") methods

RelativeStrengthOfTopPitchesFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#RelativeStrengthOfTopPitchesFeature.process)
:   Do processing necessary, storing result in feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## RepeatedNotesFeature

class music21.features.jSymbolic.RepeatedNotesFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#RepeatedNotesFeature)
:   Fraction of notes that are repeated melodically

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> fe = features.jSymbolic.RepeatedNotesFeature(s)
    >>> f = fe.extract()
    >>> f.vector
    [0.144...]
    ```

[`RepeatedNotesFeature`](#music21.features.jSymbolic.RepeatedNotesFeature "music21.features.jSymbolic.RepeatedNotesFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`RepeatedNotesFeature`](#music21.features.jSymbolic.RepeatedNotesFeature "music21.features.jSymbolic.RepeatedNotesFeature") methods

RepeatedNotesFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#RepeatedNotesFeature.process)
:   Do processing necessary, storing result in feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## RhythmicLoosenessFeature

class music21.features.jSymbolic.RhythmicLoosenessFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#RhythmicLoosenessFeature)
:   not yet implemented

    Average width of beat histogram peaks (in beats per minute).
    Width is measured for all peaks with frequencies at least 30% as high as the highest peak,
    and is defined by the distance between the points on the peak in question that are
    30% of the height of the peak.

[`RhythmicLoosenessFeature`](#music21.features.jSymbolic.RhythmicLoosenessFeature "music21.features.jSymbolic.RhythmicLoosenessFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`RhythmicLoosenessFeature`](#music21.features.jSymbolic.RhythmicLoosenessFeature "music21.features.jSymbolic.RhythmicLoosenessFeature") methods

RhythmicLoosenessFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#RhythmicLoosenessFeature.process)
:   Do processing necessary, storing result in \_feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## RhythmicVariabilityFeature

class music21.features.jSymbolic.RhythmicVariabilityFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#RhythmicVariabilityFeature)
:   Not yet implemented

    Standard deviation of the bin values (except the first 40 empty ones).

[`RhythmicVariabilityFeature`](#music21.features.jSymbolic.RhythmicVariabilityFeature "music21.features.jSymbolic.RhythmicVariabilityFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`RhythmicVariabilityFeature`](#music21.features.jSymbolic.RhythmicVariabilityFeature "music21.features.jSymbolic.RhythmicVariabilityFeature") methods

RhythmicVariabilityFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#RhythmicVariabilityFeature.process)
:   Do processing necessary, storing result in \_feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## SaxophoneFractionFeature

class music21.features.jSymbolic.SaxophoneFractionFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#SaxophoneFractionFeature)
:   Fraction of all Note Ons belonging to saxophone patches (General MIDI
    patches 65 through 68).
    # NOTE: incorrect

    ```python
    >>> s1 = stream.Stream()
    >>> s1.append(instrument.SopranoSaxophone())
    >>> s1.repeatAppend(note.Note(), 6)
    >>> s1.append(instrument.Tuba())
    >>> s1.repeatAppend(note.Note(), 4)
    >>> fe = features.jSymbolic.SaxophoneFractionFeature(s1)
    >>> print(fe.extract().vector[0])
    0.6
    ```

[`SaxophoneFractionFeature`](#music21.features.jSymbolic.SaxophoneFractionFeature "music21.features.jSymbolic.SaxophoneFractionFeature") bases

* [`InstrumentFractionFeature`](#music21.features.jSymbolic.InstrumentFractionFeature "music21.features.jSymbolic.InstrumentFractionFeature")
* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`SaxophoneFractionFeature`](#music21.features.jSymbolic.SaxophoneFractionFeature "music21.features.jSymbolic.SaxophoneFractionFeature") methods

Methods inherited from [`InstrumentFractionFeature`](#music21.features.jSymbolic.InstrumentFractionFeature "music21.features.jSymbolic.InstrumentFractionFeature"):

|  |  |  |
| --- | --- | --- |
| * [`process()`](#music21.features.jSymbolic.InstrumentFractionFeature.process "music21.features.jSymbolic.InstrumentFractionFeature.process") |  |  |

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## SecondStrongestRhythmicPulseFeature

class music21.features.jSymbolic.SecondStrongestRhythmicPulseFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#SecondStrongestRhythmicPulseFeature)
:   Bin label of the beat bin of the peak with the second-highest frequency.

    ```python
    >>> sch = corpus.parse('schoenberg/opus19', 2)
    >>> for p in sch.parts:
    ...     p.insert(0, tempo.MetronomeMark('Langsam', 70))
    >>> fe = features.jSymbolic.SecondStrongestRhythmicPulseFeature(sch)
    >>> f = fe.extract()
    >>> f.vector[0]
    70
    ```

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> fe = features.jSymbolic.SecondStrongestRhythmicPulseFeature(s)
    >>> f = fe.extract()
    >>> f.vector
    [192]
    ```

[`SecondStrongestRhythmicPulseFeature`](#music21.features.jSymbolic.SecondStrongestRhythmicPulseFeature "music21.features.jSymbolic.SecondStrongestRhythmicPulseFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`SecondStrongestRhythmicPulseFeature`](#music21.features.jSymbolic.SecondStrongestRhythmicPulseFeature "music21.features.jSymbolic.SecondStrongestRhythmicPulseFeature") methods

SecondStrongestRhythmicPulseFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#SecondStrongestRhythmicPulseFeature.process)
:   Do processing necessary, storing result in \_feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## SizeOfMelodicArcsFeature

class music21.features.jSymbolic.SizeOfMelodicArcsFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#SizeOfMelodicArcsFeature)
:   Average span (in semitones) between melodic peaks and troughs
    in any part. Each time the melody changes direction begins a
    new arc. The average size of melodic arcs is defined as the
    total size of melodic intervals between changes of directions -
    or between the start of the melody and the first change of
    direction - divided by the number of direction changes.

    Example: C D E D C E D C C
    Intervals: [0] 2 2 -2 -2 2 2 -4 0
    Changes direction (equivalent to +/- sign) three times.
    The total sum of interval distance up to the last change
    of direction is 12. We don’t count the last interval,
    the descending major third, because it is not between
    changes of direction.
    Thus, the average size of melodic arcs is 12/3 = 4.

    ```python
    >>> s = converter.parse("tinyNotation: c' d' e' d' c' d' e'2 c'2 c'2")
    >>> fe = features.jSymbolic.SizeOfMelodicArcsFeature(s)
    >>> fe.extract().vector
    [4.0]
    ```

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> fe = features.jSymbolic.SizeOfMelodicArcsFeature(s)
    >>> fe.extract().vector
    [4.84...]
    ```

[`SizeOfMelodicArcsFeature`](#music21.features.jSymbolic.SizeOfMelodicArcsFeature "music21.features.jSymbolic.SizeOfMelodicArcsFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`SizeOfMelodicArcsFeature`](#music21.features.jSymbolic.SizeOfMelodicArcsFeature "music21.features.jSymbolic.SizeOfMelodicArcsFeature") methods

SizeOfMelodicArcsFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#SizeOfMelodicArcsFeature.process)
:   Do processing necessary, storing result in feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## StaccatoIncidenceFeature

class music21.features.jSymbolic.StaccatoIncidenceFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#StaccatoIncidenceFeature)
:   Number of notes with durations of less than a 10th of a second divided by
    the total number of notes in the recording.

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> fe = features.jSymbolic.StaccatoIncidenceFeature(s)
    >>> f = fe.extract()
    >>> f.vector
    [0.0]
    ```

[`StaccatoIncidenceFeature`](#music21.features.jSymbolic.StaccatoIncidenceFeature "music21.features.jSymbolic.StaccatoIncidenceFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`StaccatoIncidenceFeature`](#music21.features.jSymbolic.StaccatoIncidenceFeature "music21.features.jSymbolic.StaccatoIncidenceFeature") methods

StaccatoIncidenceFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#StaccatoIncidenceFeature.process)
:   Do processing necessary, storing result in \_feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## StepwiseMotionFeature

class music21.features.jSymbolic.StepwiseMotionFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#StepwiseMotionFeature)
:   Fraction of melodic intervals that corresponded to a minor or major second

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> fe = features.jSymbolic.StepwiseMotionFeature(s)
    >>> f = fe.extract()
    >>> f.vector
    [0.584...]
    ```

[`StepwiseMotionFeature`](#music21.features.jSymbolic.StepwiseMotionFeature "music21.features.jSymbolic.StepwiseMotionFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`StepwiseMotionFeature`](#music21.features.jSymbolic.StepwiseMotionFeature "music21.features.jSymbolic.StepwiseMotionFeature") methods

StepwiseMotionFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#StepwiseMotionFeature.process)
:   Do processing necessary, storing result in feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## StrengthOfSecondStrongestRhythmicPulseFeature

class music21.features.jSymbolic.StrengthOfSecondStrongestRhythmicPulseFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#StrengthOfSecondStrongestRhythmicPulseFeature)
:   Frequency of the beat bin of the peak with the second-highest frequency.

    ```python
    >>> sch = corpus.parse('schoenberg/opus19', 2)
    >>> for p in sch.parts:
    ...     p.insert(0, tempo.MetronomeMark('Langsam', 70))
    >>> fe = features.jSymbolic.StrengthOfSecondStrongestRhythmicPulseFeature(sch)
    >>> fe.extract().vector[0]
    0.121...
    ```

[`StrengthOfSecondStrongestRhythmicPulseFeature`](#music21.features.jSymbolic.StrengthOfSecondStrongestRhythmicPulseFeature "music21.features.jSymbolic.StrengthOfSecondStrongestRhythmicPulseFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`StrengthOfSecondStrongestRhythmicPulseFeature`](#music21.features.jSymbolic.StrengthOfSecondStrongestRhythmicPulseFeature "music21.features.jSymbolic.StrengthOfSecondStrongestRhythmicPulseFeature") methods

StrengthOfSecondStrongestRhythmicPulseFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#StrengthOfSecondStrongestRhythmicPulseFeature.process)
:   Do processing necessary, storing result in \_feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## StrengthOfStrongestRhythmicPulseFeature

class music21.features.jSymbolic.StrengthOfStrongestRhythmicPulseFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#StrengthOfStrongestRhythmicPulseFeature)
:   Frequency of the beat bin with the highest frequency.

    ```python
    >>> sch = corpus.parse('schoenberg/opus19', 2)
    >>> for p in sch.parts:
    ...     p.insert(0, tempo.MetronomeMark('Langsam', 70))
    >>> fe = features.jSymbolic.StrengthOfStrongestRhythmicPulseFeature(sch)
    >>> fe.extract().vector[0]
    0.853...
    ```

[`StrengthOfStrongestRhythmicPulseFeature`](#music21.features.jSymbolic.StrengthOfStrongestRhythmicPulseFeature "music21.features.jSymbolic.StrengthOfStrongestRhythmicPulseFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`StrengthOfStrongestRhythmicPulseFeature`](#music21.features.jSymbolic.StrengthOfStrongestRhythmicPulseFeature "music21.features.jSymbolic.StrengthOfStrongestRhythmicPulseFeature") methods

StrengthOfStrongestRhythmicPulseFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#StrengthOfStrongestRhythmicPulseFeature.process)
:   Do processing necessary, storing result in \_feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## StrengthRatioOfTwoStrongestRhythmicPulsesFeature

class music21.features.jSymbolic.StrengthRatioOfTwoStrongestRhythmicPulsesFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#StrengthRatioOfTwoStrongestRhythmicPulsesFeature)
:   The frequency of the higher (in terms of frequency) of the two beat bins
    corresponding to the peaks with the highest frequency divided by the frequency of the lower.

    ```python
    >>> sch = corpus.parse('schoenberg/opus19', 2)
    >>> for p in sch.parts:
    ...     p.insert(0, tempo.MetronomeMark('Langsam', 70))
    >>> fe = features.jSymbolic.StrengthRatioOfTwoStrongestRhythmicPulsesFeature(sch)
    >>> fe.extract().vector[0]
    7.0
    ```

[`StrengthRatioOfTwoStrongestRhythmicPulsesFeature`](#music21.features.jSymbolic.StrengthRatioOfTwoStrongestRhythmicPulsesFeature "music21.features.jSymbolic.StrengthRatioOfTwoStrongestRhythmicPulsesFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`StrengthRatioOfTwoStrongestRhythmicPulsesFeature`](#music21.features.jSymbolic.StrengthRatioOfTwoStrongestRhythmicPulsesFeature "music21.features.jSymbolic.StrengthRatioOfTwoStrongestRhythmicPulsesFeature") methods

StrengthRatioOfTwoStrongestRhythmicPulsesFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#StrengthRatioOfTwoStrongestRhythmicPulsesFeature.process)
:   Do processing necessary, storing result in \_feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## StringEnsembleFractionFeature

class music21.features.jSymbolic.StringEnsembleFractionFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#StringEnsembleFractionFeature)
:   Not implemented

    Fraction of all Note Ons belonging to string ensemble patches
    (General MIDI patches 49 to 52).

[`StringEnsembleFractionFeature`](#music21.features.jSymbolic.StringEnsembleFractionFeature "music21.features.jSymbolic.StringEnsembleFractionFeature") bases

* [`InstrumentFractionFeature`](#music21.features.jSymbolic.InstrumentFractionFeature "music21.features.jSymbolic.InstrumentFractionFeature")
* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`StringEnsembleFractionFeature`](#music21.features.jSymbolic.StringEnsembleFractionFeature "music21.features.jSymbolic.StringEnsembleFractionFeature") methods

Methods inherited from [`InstrumentFractionFeature`](#music21.features.jSymbolic.InstrumentFractionFeature "music21.features.jSymbolic.InstrumentFractionFeature"):

|  |  |  |
| --- | --- | --- |
| * [`process()`](#music21.features.jSymbolic.InstrumentFractionFeature.process "music21.features.jSymbolic.InstrumentFractionFeature.process") |  |  |

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## StringKeyboardFractionFeature

class music21.features.jSymbolic.StringKeyboardFractionFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#StringKeyboardFractionFeature)
:   Fraction of all Note Ons belonging to string keyboard patches
    (General MIDI patches 1 to 8).

    ```python
    >>> s1 = stream.Stream()
    >>> s1.append(instrument.Piano())
    >>> s1.repeatAppend(note.Note(), 9)
    >>> s1.append(instrument.Tuba())
    >>> s1.append(note.Note())
    >>> fe = features.jSymbolic.StringKeyboardFractionFeature(s1)
    >>> fe.extract().vector
    [0.9...]
    ```

[`StringKeyboardFractionFeature`](#music21.features.jSymbolic.StringKeyboardFractionFeature "music21.features.jSymbolic.StringKeyboardFractionFeature") bases

* [`InstrumentFractionFeature`](#music21.features.jSymbolic.InstrumentFractionFeature "music21.features.jSymbolic.InstrumentFractionFeature")
* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`StringKeyboardFractionFeature`](#music21.features.jSymbolic.StringKeyboardFractionFeature "music21.features.jSymbolic.StringKeyboardFractionFeature") methods

Methods inherited from [`InstrumentFractionFeature`](#music21.features.jSymbolic.InstrumentFractionFeature "music21.features.jSymbolic.InstrumentFractionFeature"):

|  |  |  |
| --- | --- | --- |
| * [`process()`](#music21.features.jSymbolic.InstrumentFractionFeature.process "music21.features.jSymbolic.InstrumentFractionFeature.process") |  |  |

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## StrongTonalCentresFeature

class music21.features.jSymbolic.StrongTonalCentresFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#StrongTonalCentresFeature)
:   Not implemented

    Number of peaks in the fifths pitch histogram that each account
    for at least 9% of all Note Ons.

[`StrongTonalCentresFeature`](#music21.features.jSymbolic.StrongTonalCentresFeature "music21.features.jSymbolic.StrongTonalCentresFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`StrongTonalCentresFeature`](#music21.features.jSymbolic.StrongTonalCentresFeature "music21.features.jSymbolic.StrongTonalCentresFeature") methods

StrongTonalCentresFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#StrongTonalCentresFeature.process)
:   Do processing necessary, storing result in \_feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## StrongestRhythmicPulseFeature

class music21.features.jSymbolic.StrongestRhythmicPulseFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#StrongestRhythmicPulseFeature)
:   Bin label of the beat bin of the peak with the highest frequency.

    ```python
    >>> sch = corpus.parse('schoenberg/opus19', 2)
    >>> for p in sch.parts:
    ...     p.insert(0, tempo.MetronomeMark('Langsam', 70))
    >>> fe = features.jSymbolic.StrongestRhythmicPulseFeature(sch)
    >>> f = fe.extract()
    >>> f.vector[0]
    140
    ```

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> fe = features.jSymbolic.StrongestRhythmicPulseFeature(s)
    >>> f = fe.extract()
    >>> f.vector
    [96]
    ```

[`StrongestRhythmicPulseFeature`](#music21.features.jSymbolic.StrongestRhythmicPulseFeature "music21.features.jSymbolic.StrongestRhythmicPulseFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`StrongestRhythmicPulseFeature`](#music21.features.jSymbolic.StrongestRhythmicPulseFeature "music21.features.jSymbolic.StrongestRhythmicPulseFeature") methods

StrongestRhythmicPulseFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#StrongestRhythmicPulseFeature.process)
:   Do processing necessary, storing result in \_feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## TimePrevalenceOfPitchedInstrumentsFeature

class music21.features.jSymbolic.TimePrevalenceOfPitchedInstrumentsFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#TimePrevalenceOfPitchedInstrumentsFeature)
:   Not implemented

    The fraction of the total time of the recording in
    which a note was sounding for each (pitched) General
    MIDI Instrument. There is one entry for each instrument,
    which is set to the total time in seconds during which a
    given instrument was sounding one or more notes divided by the total length
    in seconds of the piece.’

    TODO: implement

[`TimePrevalenceOfPitchedInstrumentsFeature`](#music21.features.jSymbolic.TimePrevalenceOfPitchedInstrumentsFeature "music21.features.jSymbolic.TimePrevalenceOfPitchedInstrumentsFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`TimePrevalenceOfPitchedInstrumentsFeature`](#music21.features.jSymbolic.TimePrevalenceOfPitchedInstrumentsFeature "music21.features.jSymbolic.TimePrevalenceOfPitchedInstrumentsFeature") methods

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") | * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") | * [`process()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.process "music21.features.base.FeatureExtractor.process") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## TripleMeterFeature

class music21.features.jSymbolic.TripleMeterFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#TripleMeterFeature)
:   Set to 1 if numerator of initial time signature is 3, set to 0 otherwise.

    ```python
    >>> s1 = stream.Stream()
    >>> s1.append(meter.TimeSignature('5/4'))
    >>> fe = features.jSymbolic.TripleMeterFeature(s1)
    >>> fe.extract().vector
    [0]
    ```

    ```python
    >>> s2 = stream.Stream()
    >>> s2.append(meter.TimeSignature('3/4'))
    >>> fe.setData(s2)  # change the data
    >>> fe.extract().vector
    [1]
    ```

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> fe = features.jSymbolic.TripleMeterFeature(s)
    >>> f = fe.extract()
    >>> f.vector
    [0]
    ```

[`TripleMeterFeature`](#music21.features.jSymbolic.TripleMeterFeature "music21.features.jSymbolic.TripleMeterFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`TripleMeterFeature`](#music21.features.jSymbolic.TripleMeterFeature "music21.features.jSymbolic.TripleMeterFeature") methods

TripleMeterFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#TripleMeterFeature.process)
:   Do processing necessary, storing result in \_feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## UnpitchedInstrumentsPresentFeature

class music21.features.jSymbolic.UnpitchedInstrumentsPresentFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#UnpitchedInstrumentsPresentFeature)
:   Not yet implemented

    Which unpitched MIDI Percussion Key Map instruments are present.
    There is one entry for each instrument, which is set to 1.0 if there is
    at least one Note On in the recording corresponding to the instrument and to
    0.0 if there is not. It should be noted that only instruments 35 to 81 are included here,
    as they are the ones that meet the official standard. They are numbered in this
    array from 0 to 46.

[`UnpitchedInstrumentsPresentFeature`](#music21.features.jSymbolic.UnpitchedInstrumentsPresentFeature "music21.features.jSymbolic.UnpitchedInstrumentsPresentFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`UnpitchedInstrumentsPresentFeature`](#music21.features.jSymbolic.UnpitchedInstrumentsPresentFeature "music21.features.jSymbolic.UnpitchedInstrumentsPresentFeature") methods

UnpitchedInstrumentsPresentFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#UnpitchedInstrumentsPresentFeature.process)
:   Do processing necessary, storing result in \_feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## VariabilityOfNoteDurationFeature

class music21.features.jSymbolic.VariabilityOfNoteDurationFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#VariabilityOfNoteDurationFeature)
:   Standard deviation of note durations in seconds.

    # In this piece, we have:
    # 9 half notes or tied pair of quarters
    # 98 untied quarters or tied pair of eighths
    # 56 untied eighths
    # BPM = 120 means a half note is a second.
    # Mean duration should thus be 0.44171779141104295
    # and standard deviation should be 0.17854763448902145

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> for p in s.parts:
    ...     p.insert(0, tempo.MetronomeMark(number=120))
    >>> fe = features.jSymbolic.VariabilityOfNoteDurationFeature(s)
    >>> f = fe.extract()
    >>> f.vector[0]
    0.178...
    ```

[`VariabilityOfNoteDurationFeature`](#music21.features.jSymbolic.VariabilityOfNoteDurationFeature "music21.features.jSymbolic.VariabilityOfNoteDurationFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`VariabilityOfNoteDurationFeature`](#music21.features.jSymbolic.VariabilityOfNoteDurationFeature "music21.features.jSymbolic.VariabilityOfNoteDurationFeature") methods

VariabilityOfNoteDurationFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#VariabilityOfNoteDurationFeature.process)
:   Do processing necessary, storing result in \_feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## VariabilityOfNotePrevalenceOfPitchedInstrumentsFeature

class music21.features.jSymbolic.VariabilityOfNotePrevalenceOfPitchedInstrumentsFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#VariabilityOfNotePrevalenceOfPitchedInstrumentsFeature)
:   Standard deviation of the fraction of Note Ons played
    by each (pitched) General MIDI instrument that is
    used to play at least one note.

    ```python
    >>> s1 = stream.Stream()
    >>> s1.append(instrument.AcousticGuitar())
    >>> s1.repeatAppend(note.Note(), 5)
    >>> s1.append(instrument.Tuba())
    >>> s1.append(note.Note())
    >>> fe = features.jSymbolic.VariabilityOfNotePrevalenceOfPitchedInstrumentsFeature(s1)
    >>> fe.extract().vector
    [0.33333...]
    ```

[`VariabilityOfNotePrevalenceOfPitchedInstrumentsFeature`](#music21.features.jSymbolic.VariabilityOfNotePrevalenceOfPitchedInstrumentsFeature "music21.features.jSymbolic.VariabilityOfNotePrevalenceOfPitchedInstrumentsFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`VariabilityOfNotePrevalenceOfPitchedInstrumentsFeature`](#music21.features.jSymbolic.VariabilityOfNotePrevalenceOfPitchedInstrumentsFeature "music21.features.jSymbolic.VariabilityOfNotePrevalenceOfPitchedInstrumentsFeature") methods

VariabilityOfNotePrevalenceOfPitchedInstrumentsFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#VariabilityOfNotePrevalenceOfPitchedInstrumentsFeature.process)
:   Do processing necessary, storing result in \_feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## VariabilityOfNotePrevalenceOfUnpitchedInstrumentsFeature

class music21.features.jSymbolic.VariabilityOfNotePrevalenceOfUnpitchedInstrumentsFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#VariabilityOfNotePrevalenceOfUnpitchedInstrumentsFeature)
:   Not implemented

    Standard deviation of the fraction of Note Ons played by each (unpitched) MIDI Percussion Key
    Map instrument that is used to play at least one note. It should be noted that only
    instruments 35 to 81 are included here, as they are the ones that are included in the
    official standard.

    TODO: implement

[`VariabilityOfNotePrevalenceOfUnpitchedInstrumentsFeature`](#music21.features.jSymbolic.VariabilityOfNotePrevalenceOfUnpitchedInstrumentsFeature "music21.features.jSymbolic.VariabilityOfNotePrevalenceOfUnpitchedInstrumentsFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`VariabilityOfNotePrevalenceOfUnpitchedInstrumentsFeature`](#music21.features.jSymbolic.VariabilityOfNotePrevalenceOfUnpitchedInstrumentsFeature "music21.features.jSymbolic.VariabilityOfNotePrevalenceOfUnpitchedInstrumentsFeature") methods

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") | * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") | * [`process()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.process "music21.features.base.FeatureExtractor.process") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## VariabilityOfNumberOfIndependentVoicesFeature

class music21.features.jSymbolic.VariabilityOfNumberOfIndependentVoicesFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#VariabilityOfNumberOfIndependentVoicesFeature)
:   Standard deviation of number of different channels in which notes have sounded simultaneously.
    Rests are not included in this calculation.

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> fe = features.jSymbolic.VariabilityOfNumberOfIndependentVoicesFeature(s)
    >>> f = fe.extract()
    >>> f.vector
    [0.449...]
    ```

[`VariabilityOfNumberOfIndependentVoicesFeature`](#music21.features.jSymbolic.VariabilityOfNumberOfIndependentVoicesFeature "music21.features.jSymbolic.VariabilityOfNumberOfIndependentVoicesFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`VariabilityOfNumberOfIndependentVoicesFeature`](#music21.features.jSymbolic.VariabilityOfNumberOfIndependentVoicesFeature "music21.features.jSymbolic.VariabilityOfNumberOfIndependentVoicesFeature") methods

VariabilityOfNumberOfIndependentVoicesFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#VariabilityOfNumberOfIndependentVoicesFeature.process)
:   Do processing necessary, storing result in \_feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## VariabilityOfTimeBetweenAttacksFeature

class music21.features.jSymbolic.VariabilityOfTimeBetweenAttacksFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#VariabilityOfTimeBetweenAttacksFeature)
:   Standard deviation of the times, in seconds, between Note On events (regardless of channel).

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> fe = features.jSymbolic.VariabilityOfTimeBetweenAttacksFeature(s)
    >>> f = fe.extract()
    >>> print(f.vector)
    [0.1875]
    ```

[`VariabilityOfTimeBetweenAttacksFeature`](#music21.features.jSymbolic.VariabilityOfTimeBetweenAttacksFeature "music21.features.jSymbolic.VariabilityOfTimeBetweenAttacksFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`VariabilityOfTimeBetweenAttacksFeature`](#music21.features.jSymbolic.VariabilityOfTimeBetweenAttacksFeature "music21.features.jSymbolic.VariabilityOfTimeBetweenAttacksFeature") methods

VariabilityOfTimeBetweenAttacksFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#VariabilityOfTimeBetweenAttacksFeature.process)
:   Do processing necessary, storing result in \_feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## VariationOfDynamicsFeature

class music21.features.jSymbolic.VariationOfDynamicsFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#VariationOfDynamicsFeature)
:   Not implemented

    Standard deviation of loudness levels of all notes.

    TODO: implement

[`VariationOfDynamicsFeature`](#music21.features.jSymbolic.VariationOfDynamicsFeature "music21.features.jSymbolic.VariationOfDynamicsFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`VariationOfDynamicsFeature`](#music21.features.jSymbolic.VariationOfDynamicsFeature "music21.features.jSymbolic.VariationOfDynamicsFeature") methods

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") | * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") | * [`process()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.process "music21.features.base.FeatureExtractor.process") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## VariationOfDynamicsInEachVoiceFeature

class music21.features.jSymbolic.VariationOfDynamicsInEachVoiceFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#VariationOfDynamicsInEachVoiceFeature)
:   Not implemented

    The average of the standard deviations of loudness levels within each
    channel that contains at least one note.

    TODO: implement

[`VariationOfDynamicsInEachVoiceFeature`](#music21.features.jSymbolic.VariationOfDynamicsInEachVoiceFeature "music21.features.jSymbolic.VariationOfDynamicsInEachVoiceFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`VariationOfDynamicsInEachVoiceFeature`](#music21.features.jSymbolic.VariationOfDynamicsInEachVoiceFeature "music21.features.jSymbolic.VariationOfDynamicsInEachVoiceFeature") methods

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") | * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") | * [`process()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.process "music21.features.base.FeatureExtractor.process") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## VibratoPrevalenceFeature

class music21.features.jSymbolic.VibratoPrevalenceFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#VibratoPrevalenceFeature)
:   Not yet implemented in music21

    Number of notes for which Pitch Bend messages change direction at least twice divided by
    total number of notes that have Pitch Bend messages associated with them.

[`VibratoPrevalenceFeature`](#music21.features.jSymbolic.VibratoPrevalenceFeature "music21.features.jSymbolic.VibratoPrevalenceFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`VibratoPrevalenceFeature`](#music21.features.jSymbolic.VibratoPrevalenceFeature "music21.features.jSymbolic.VibratoPrevalenceFeature") methods

VibratoPrevalenceFeature.process()[[source]](../_modules/music21/features/jSymbolic.html#VibratoPrevalenceFeature.process)
:   Do processing necessary, storing result in \_feature.

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## ViolinFractionFeature

class music21.features.jSymbolic.ViolinFractionFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#ViolinFractionFeature)
:   Fraction of all Note Ons belonging to violin patches (General MIDI
    patches 41 or 111).

    ```python
    >>> s1 = stream.Stream()
    >>> s1.append(instrument.Violin())
    >>> s1.repeatAppend(note.Note(), 2)
    >>> s1.append(instrument.Tuba())
    >>> s1.repeatAppend(note.Note(), 8)
    >>> fe = features.jSymbolic.ViolinFractionFeature(s1)
    >>> fe.extract().vector
    [0.2...]
    ```

[`ViolinFractionFeature`](#music21.features.jSymbolic.ViolinFractionFeature "music21.features.jSymbolic.ViolinFractionFeature") bases

* [`InstrumentFractionFeature`](#music21.features.jSymbolic.InstrumentFractionFeature "music21.features.jSymbolic.InstrumentFractionFeature")
* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`ViolinFractionFeature`](#music21.features.jSymbolic.ViolinFractionFeature "music21.features.jSymbolic.ViolinFractionFeature") methods

Methods inherited from [`InstrumentFractionFeature`](#music21.features.jSymbolic.InstrumentFractionFeature "music21.features.jSymbolic.InstrumentFractionFeature"):

|  |  |  |
| --- | --- | --- |
| * [`process()`](#music21.features.jSymbolic.InstrumentFractionFeature.process "music21.features.jSymbolic.InstrumentFractionFeature.process") |  |  |

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## VoiceEqualityDynamicsFeature

class music21.features.jSymbolic.VoiceEqualityDynamicsFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#VoiceEqualityDynamicsFeature)
:   Not implemented

    TODO: implement

[`VoiceEqualityDynamicsFeature`](#music21.features.jSymbolic.VoiceEqualityDynamicsFeature "music21.features.jSymbolic.VoiceEqualityDynamicsFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`VoiceEqualityDynamicsFeature`](#music21.features.jSymbolic.VoiceEqualityDynamicsFeature "music21.features.jSymbolic.VoiceEqualityDynamicsFeature") methods

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") | * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") | * [`process()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.process "music21.features.base.FeatureExtractor.process") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## VoiceEqualityMelodicLeapsFeature

class music21.features.jSymbolic.VoiceEqualityMelodicLeapsFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#VoiceEqualityMelodicLeapsFeature)
:   Not implemented

    TODO: implement

[`VoiceEqualityMelodicLeapsFeature`](#music21.features.jSymbolic.VoiceEqualityMelodicLeapsFeature "music21.features.jSymbolic.VoiceEqualityMelodicLeapsFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`VoiceEqualityMelodicLeapsFeature`](#music21.features.jSymbolic.VoiceEqualityMelodicLeapsFeature "music21.features.jSymbolic.VoiceEqualityMelodicLeapsFeature") methods

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") | * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") | * [`process()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.process "music21.features.base.FeatureExtractor.process") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## VoiceEqualityNoteDurationFeature

class music21.features.jSymbolic.VoiceEqualityNoteDurationFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#VoiceEqualityNoteDurationFeature)
:   Not implemented

    TODO: implement

[`VoiceEqualityNoteDurationFeature`](#music21.features.jSymbolic.VoiceEqualityNoteDurationFeature "music21.features.jSymbolic.VoiceEqualityNoteDurationFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`VoiceEqualityNoteDurationFeature`](#music21.features.jSymbolic.VoiceEqualityNoteDurationFeature "music21.features.jSymbolic.VoiceEqualityNoteDurationFeature") methods

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") | * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") | * [`process()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.process "music21.features.base.FeatureExtractor.process") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## VoiceEqualityNumberOfNotesFeature

class music21.features.jSymbolic.VoiceEqualityNumberOfNotesFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#VoiceEqualityNumberOfNotesFeature)
:   Not implemented

    TODO: implement

    Standard deviation of the total number of Note Ons in each channel
    that contains at least one note.

[`VoiceEqualityNumberOfNotesFeature`](#music21.features.jSymbolic.VoiceEqualityNumberOfNotesFeature "music21.features.jSymbolic.VoiceEqualityNumberOfNotesFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`VoiceEqualityNumberOfNotesFeature`](#music21.features.jSymbolic.VoiceEqualityNumberOfNotesFeature "music21.features.jSymbolic.VoiceEqualityNumberOfNotesFeature") methods

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") | * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") | * [`process()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.process "music21.features.base.FeatureExtractor.process") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## VoiceEqualityRangeFeature

class music21.features.jSymbolic.VoiceEqualityRangeFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#VoiceEqualityRangeFeature)
:   Not implemented

    Standard deviation of the differences between the highest and lowest
    pitches in each channel that contains at least one note.

[`VoiceEqualityRangeFeature`](#music21.features.jSymbolic.VoiceEqualityRangeFeature "music21.features.jSymbolic.VoiceEqualityRangeFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`VoiceEqualityRangeFeature`](#music21.features.jSymbolic.VoiceEqualityRangeFeature "music21.features.jSymbolic.VoiceEqualityRangeFeature") methods

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") | * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") | * [`process()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.process "music21.features.base.FeatureExtractor.process") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## VoiceSeparationFeature

class music21.features.jSymbolic.VoiceSeparationFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#VoiceSeparationFeature)
:   Not implemented

    Average separation in semitones between the average pitches of consecutive
    channels (after sorting based/non-average pitch) that contain at least one note.

[`VoiceSeparationFeature`](#music21.features.jSymbolic.VoiceSeparationFeature "music21.features.jSymbolic.VoiceSeparationFeature") bases

* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`VoiceSeparationFeature`](#music21.features.jSymbolic.VoiceSeparationFeature "music21.features.jSymbolic.VoiceSeparationFeature") methods

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") | * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") | * [`process()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.process "music21.features.base.FeatureExtractor.process") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## WoodwindsFractionFeature

class music21.features.jSymbolic.WoodwindsFractionFeature(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/jSymbolic.html#WoodwindsFractionFeature)
:   Fraction of all Note Ons belonging to woodwind patches
    (General MIDI patches 69 through 76).

    TODO: Conflict in source: does 69-79?

    ```python
    >>> s1 = stream.Stream()
    >>> s1.append(instrument.Flute())
    >>> s1.repeatAppend(note.Note(), 3)
    >>> s1.append(instrument.Tuba())
    >>> s1.repeatAppend(note.Note(), 7)
    >>> fe = features.jSymbolic.WoodwindsFractionFeature(s1)
    >>> print(fe.extract().vector[0])
    0.3
    ```

[`WoodwindsFractionFeature`](#music21.features.jSymbolic.WoodwindsFractionFeature "music21.features.jSymbolic.WoodwindsFractionFeature") bases

* [`InstrumentFractionFeature`](#music21.features.jSymbolic.InstrumentFractionFeature "music21.features.jSymbolic.InstrumentFractionFeature")
* [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor")

[`WoodwindsFractionFeature`](#music21.features.jSymbolic.WoodwindsFractionFeature "music21.features.jSymbolic.WoodwindsFractionFeature") methods

Methods inherited from [`InstrumentFractionFeature`](#music21.features.jSymbolic.InstrumentFractionFeature "music21.features.jSymbolic.InstrumentFractionFeature"):

|  |  |  |
| --- | --- | --- |
| * [`process()`](#music21.features.jSymbolic.InstrumentFractionFeature.process "music21.features.jSymbolic.InstrumentFractionFeature.process") |  |  |

Methods inherited from [`FeatureExtractor`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor"):

|  |  |  |
| --- | --- | --- |
| * [`extract()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.extract "music21.features.base.FeatureExtractor.extract") * [`fillFeatureAttributes()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.fillFeatureAttributes "music21.features.base.FeatureExtractor.fillFeatureAttributes") | * [`getAttributeLabels()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getAttributeLabels "music21.features.base.FeatureExtractor.getAttributeLabels") * [`getBlankFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.getBlankFeature "music21.features.base.FeatureExtractor.getBlankFeature") | * [`prepareFeature()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.prepareFeature "music21.features.base.FeatureExtractor.prepareFeature") * [`setData()`](moduleFeaturesBase.html#music21.features.base.FeatureExtractor.setData "music21.features.base.FeatureExtractor.setData") |

## Functions

music21.features.jSymbolic.getCompletionStats()[[source]](../_modules/music21/features/jSymbolic.html#getCompletionStats)
:   ```python
    >>> features.jSymbolic.getCompletionStats()
    completion stats: 72/112 (0.6428...)
    ```

music21.features.jSymbolic.getExtractorByTypeAndNumber(*extractorType*, *number*)[[source]](../_modules/music21/features/jSymbolic.html#getExtractorByTypeAndNumber)
:   Typical usage:

    ```python
    >>> t5 = features.jSymbolic.getExtractorByTypeAndNumber('T', 5)
    >>> t5.__name__
    'VoiceEqualityNoteDurationFeature'
    >>> bachExample = corpus.parse('bach/bwv66.6')
    >>> fe = t5(bachExample)
    ```

    Features unimplemented in jSymbolic but documented in the dissertation return None

    ```python
    >>> features.jSymbolic.getExtractorByTypeAndNumber('C', 20) is None
    True
    ```

    Totally unknown features return an exception:

    ```python
    >>> features.jSymbolic.getExtractorByTypeAndNumber('L', 900)
    Traceback (most recent call last):
    music21.features.jSymbolic.JSymbolicFeatureException: Could not find
        any jSymbolic features of type L
    ```

    ```python
    >>> features.jSymbolic.getExtractorByTypeAndNumber('C', 200)
    Traceback (most recent call last):
    music21.features.jSymbolic.JSymbolicFeatureException: jSymbolic
        features of type C do not have number 200
    ```

    You could also find all the feature extractors this way:

    ```python
    >>> fs = features.jSymbolic.extractorsById
    >>> for k in fs:
    ...     for i in range(len(fs[k])):
    ...       if fs[k][i] is not None:
    ...         n = fs[k][i].__name__
    ...         if fs[k][i] not in features.jSymbolic.featureExtractors:
    ...            n += ' (not implemented)'
    ...         print(f'{k} {i} {n}')
    D 1 OverallDynamicRangeFeature (not implemented)
    D 2 VariationOfDynamicsFeature (not implemented)
    D 3 VariationOfDynamicsInEachVoiceFeature (not implemented)
    D 4 AverageNoteToNoteDynamicsChangeFeature (not implemented)
    I 1 PitchedInstrumentsPresentFeature
    I 2 UnpitchedInstrumentsPresentFeature (not implemented)
    I 3 NotePrevalenceOfPitchedInstrumentsFeature
    I 4 NotePrevalenceOfUnpitchedInstrumentsFeature (not implemented)
    I 5 TimePrevalenceOfPitchedInstrumentsFeature (not implemented)
    I 6 VariabilityOfNotePrevalenceOfPitchedInstrumentsFeature
    I 7 VariabilityOfNotePrevalenceOfUnpitchedInstrumentsFeature (not implemented)
    I 8 NumberOfPitchedInstrumentsFeature
    I 9 NumberOfUnpitchedInstrumentsFeature (not implemented)
    I 10 PercussionPrevalenceFeature (not implemented)
    I 11 StringKeyboardFractionFeature
    I 12 AcousticGuitarFractionFeature
    I 13 ElectricGuitarFractionFeature
    I 14 ViolinFractionFeature
    I 15 SaxophoneFractionFeature
    I 16 BrassFractionFeature
    I 17 WoodwindsFractionFeature
    I 18 OrchestralStringsFractionFeature
    I 19 StringEnsembleFractionFeature
    I 20 ElectricInstrumentFractionFeature
    M 1 MelodicIntervalHistogramFeature
    M 2 AverageMelodicIntervalFeature
    M 3 MostCommonMelodicIntervalFeature
    M 4 DistanceBetweenMostCommonMelodicIntervalsFeature
    M 5 MostCommonMelodicIntervalPrevalenceFeature
    M 6 RelativeStrengthOfMostCommonIntervalsFeature
    M 7 NumberOfCommonMelodicIntervalsFeature
    M 8 AmountOfArpeggiationFeature
    M 9 RepeatedNotesFeature
    M 10 ChromaticMotionFeature
    M 11 StepwiseMotionFeature
    M 12 MelodicThirdsFeature
    M 13 MelodicFifthsFeature
    M 14 MelodicTritonesFeature
    M 15 MelodicOctavesFeature
    M 17 DirectionOfMotionFeature
    M 18 DurationOfMelodicArcsFeature
    M 19 SizeOfMelodicArcsFeature
    P 1 MostCommonPitchPrevalenceFeature
    P 2 MostCommonPitchClassPrevalenceFeature
    P 3 RelativeStrengthOfTopPitchesFeature
    P 4 RelativeStrengthOfTopPitchClassesFeature
    P 5 IntervalBetweenStrongestPitchesFeature
    P 6 IntervalBetweenStrongestPitchClassesFeature
    P 7 NumberOfCommonPitchesFeature
    P 8 PitchVarietyFeature
    P 9 PitchClassVarietyFeature
    P 10 RangeFeature
    P 11 MostCommonPitchFeature
    P 12 PrimaryRegisterFeature
    P 13 ImportanceOfBassRegisterFeature
    P 14 ImportanceOfMiddleRegisterFeature
    P 15 ImportanceOfHighRegisterFeature
    P 16 MostCommonPitchClassFeature
    P 17 DominantSpreadFeature (not implemented)
    P 18 StrongTonalCentresFeature (not implemented)
    P 19 BasicPitchHistogramFeature
    P 20 PitchClassDistributionFeature
    P 21 FifthsPitchHistogramFeature
    P 22 QualityFeature
    P 23 GlissandoPrevalenceFeature (not implemented)
    P 24 AverageRangeOfGlissandosFeature (not implemented)
    P 25 VibratoPrevalenceFeature (not implemented)
    R 1 StrongestRhythmicPulseFeature (not implemented)
    R 2 SecondStrongestRhythmicPulseFeature (not implemented)
    R 3 HarmonicityOfTwoStrongestRhythmicPulsesFeature (not implemented)
    R 4 StrengthOfStrongestRhythmicPulseFeature (not implemented)
    R 5 StrengthOfSecondStrongestRhythmicPulseFeature (not implemented)
    R 6 StrengthRatioOfTwoStrongestRhythmicPulsesFeature (not implemented)
    R 7 CombinedStrengthOfTwoStrongestRhythmicPulsesFeature (not implemented)
    R 8 NumberOfStrongPulsesFeature (not implemented)
    R 9 NumberOfModeratePulsesFeature (not implemented)
    R 10 NumberOfRelativelyStrongPulsesFeature (not implemented)
    R 11 RhythmicLoosenessFeature (not implemented)
    R 12 PolyrhythmsFeature (not implemented)
    R 13 RhythmicVariabilityFeature (not implemented)
    R 14 BeatHistogramFeature (not implemented)
    R 15 NoteDensityFeature
    R 17 AverageNoteDurationFeature
    R 18 VariabilityOfNoteDurationFeature
    R 19 MaximumNoteDurationFeature
    R 20 MinimumNoteDurationFeature
    R 21 StaccatoIncidenceFeature
    R 22 AverageTimeBetweenAttacksFeature
    R 23 VariabilityOfTimeBetweenAttacksFeature
    R 24 AverageTimeBetweenAttacksForEachVoiceFeature
    R 25 AverageVariabilityOfTimeBetweenAttacksForEachVoiceFeature
    R 30 InitialTempoFeature
    R 31 InitialTimeSignatureFeature
    R 32 CompoundOrSimpleMeterFeature
    R 33 TripleMeterFeature
    R 34 QuintupleMeterFeature
    R 35 ChangesOfMeterFeature
    R 36 DurationFeature
    T 1 MaximumNumberOfIndependentVoicesFeature
    T 2 AverageNumberOfIndependentVoicesFeature
    T 3 VariabilityOfNumberOfIndependentVoicesFeature
    T 4 VoiceEqualityNumberOfNotesFeature (not implemented)
    T 5 VoiceEqualityNoteDurationFeature (not implemented)
    T 6 VoiceEqualityDynamicsFeature (not implemented)
    T 7 VoiceEqualityMelodicLeapsFeature (not implemented)
    T 8 VoiceEqualityRangeFeature (not implemented)
    T 9 ImportanceOfLoudestVoiceFeature (not implemented)
    T 10 RelativeRangeOfLoudestVoiceFeature (not implemented)
    T 12 RangeOfHighestLineFeature (not implemented)
    T 13 RelativeNoteDensityOfHighestLineFeature (not implemented)
    T 15 MelodicIntervalsInLowestLineFeature (not implemented)
    T 20 VoiceSeparationFeature (not implemented)
    ```
