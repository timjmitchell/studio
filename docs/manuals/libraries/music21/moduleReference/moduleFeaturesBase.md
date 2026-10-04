Source: https://music21.org/music21docs/moduleReference/moduleFeaturesBase.html

# music21.features.base

## DataSet

class music21.features.base.DataSet(*classLabel=None*, *featureExtractors=()*)[[source]](../_modules/music21/features/base.html#DataSet)
:   A set of features, as well as a collection of data to operate on.

    Comprises multiple DataInstance objects, a FeatureSet, and an OutputFormat.

    ```python
    >>> ds = features.DataSet(classLabel='Composer')
    >>> f = [features.jSymbolic.PitchClassDistributionFeature,
    ...      features.jSymbolic.ChangesOfMeterFeature,
    ...      features.jSymbolic.InitialTimeSignatureFeature]
    >>> ds.addFeatureExtractors(f)
    >>> ds.addData('bwv66.6', classValue='Bach')
    >>> ds.addData('bach/bwv324.xml', classValue='Bach')
    >>> ds.process()
    >>> ds.getFeaturesAsList()[0]
    ['bwv66.6', 0.196..., 0.0736..., 0.006..., 0.098..., 0.0368..., 0.177..., 0.0,
     0.085..., 0.134..., 0.018..., 0.171..., 0.0, 0, 4, 4, 'Bach']
    >>> ds.getFeaturesAsList()[1]
    ['bach/bwv324.xml', 0.25, 0.0288..., 0.125, 0.0, 0.144..., 0.125, 0.0, 0.163..., 0.0, 0.134...,
    0.0288..., 0.0, 0, 4, 4, 'Bach']
    ```

    ```python
    >>> ds = ds.getString()
    ```

    By default, all exceptions are caught and printed if debug mode is on.

    Set ds.failFast = True to not catch them.

    Set ds.quiet = False to print them regardless of debug mode.

[`DataSet`](#music21.features.base.DataSet "music21.features.base.DataSet") methods

DataSet.addData(*dataOrStreamOrPath*, *classValue=None*, *id=None*)[[source]](../_modules/music21/features/base.html#DataSet.addData)
:   Add a Stream, DataInstance, MetadataEntry, or path (Posix or str)
    to a corpus or local file to this data set.

    The class value passed here is assumed to be the same as
    the classLabel assigned at startup.

DataSet.addFeatureExtractors(*values*)[[source]](../_modules/music21/features/base.html#DataSet.addFeatureExtractors)
:   Add one or more FeatureExtractor objects, either as a list or as an individual object.

DataSet.addMultipleData(*dataList*, *classValues*, *ids=None*)[[source]](../_modules/music21/features/base.html#DataSet.addMultipleData)
:   add multiple data points at the same time.

    Requires an iterable (including MetadataBundle) for dataList holding
    types that can be passed to addData, and an equally sized list of dataValues
    and an equally sized list of ids (or None)

    classValues can also be a pickleable function that will be called on
    each instance after parsing, as can ids.

DataSet.getAttributeLabels(*includeClassLabel=True*, *includeId=True*)[[source]](../_modules/music21/features/base.html#DataSet.getAttributeLabels)
:   Return a list of all attribute labels. Optionally add a class
    label field and/or an id field.

    ```python
    >>> f = [features.jSymbolic.PitchClassDistributionFeature,
    ...      features.jSymbolic.ChangesOfMeterFeature]
    >>> ds = features.DataSet(classLabel='Composer', featureExtractors=f)
    >>> ds.getAttributeLabels(includeId=False)
    ['Pitch_Class_Distribution_0',
     'Pitch_Class_Distribution_1',
     ...
     ...
     'Pitch_Class_Distribution_11',
     'Changes_of_Meter',
     'Composer']
    ```

DataSet.getClassLabel()[[source]](../_modules/music21/features/base.html#DataSet.getClassLabel)

DataSet.getClassPositionLabels(*includeId=True*)[[source]](../_modules/music21/features/base.html#DataSet.getClassPositionLabels)
:   Return column labels for the presence of a class definition

    ```python
    >>> f = [features.jSymbolic.PitchClassDistributionFeature,
    ...      features.jSymbolic.ChangesOfMeterFeature]
    >>> ds = features.DataSet(classLabel='Composer', featureExtractors=f)
    >>> ds.getClassPositionLabels()
    [None, False, False, False, False, False, False, False, False,
     False, False, False, False, False, True]
    ```

DataSet.getDiscreteLabels(*includeClassLabel=True*, *includeId=True*)[[source]](../_modules/music21/features/base.html#DataSet.getDiscreteLabels)
:   Return column labels for discrete status.

    ```python
    >>> f = [features.jSymbolic.PitchClassDistributionFeature,
    ...      features.jSymbolic.ChangesOfMeterFeature]
    >>> ds = features.DataSet(classLabel='Composer', featureExtractors=f)
    >>> ds.getDiscreteLabels()
    [None, False, False, False, False, False, False, False, False, False,
     False, False, False, True, True]
    ```

DataSet.getFeaturesAsList(*includeClassLabel=True*, *includeId=True*, *concatenateLists=True*)[[source]](../_modules/music21/features/base.html#DataSet.getFeaturesAsList)
:   Get processed data as a list of lists, merging any sub-lists
    in multidimensional features.

DataSet.getString(*outputFmt='tab'*)[[source]](../_modules/music21/features/base.html#DataSet.getString)
:   Get a string representation of the data set in a specific format.

DataSet.getUniqueClassValues()[[source]](../_modules/music21/features/base.html#DataSet.getUniqueClassValues)
:   Return a list of unique class values.

DataSet.process()[[source]](../_modules/music21/features/base.html#DataSet.process)
:   Process all Data with all FeatureExtractors.
    Processed data is stored internally as numerous Feature objects.

DataSet.write(*fp=None*, *format=None*, *includeClassLabel=True*)[[source]](../_modules/music21/features/base.html#DataSet.write)
:   Set the output format object.

## Feature

class music21.features.base.Feature[[source]](../_modules/music21/features/base.html#Feature)
:   An object representation of a feature, capable of presentation in a variety of formats,
    and returned from FeatureExtractor objects.

    Feature objects are simple. It is FeatureExtractors that store all metadata and processing
    routines for creating Feature objects. Normally you wouldn’t create one of these yourself.

    ```python
    >>> myFeature = features.Feature()
    >>> myFeature.dimensions = 3
    >>> myFeature.name = 'Random arguments'
    >>> myFeature.isSequential = True
    ```

    This is a continuous Feature, so we will set discrete to false.

    ```python
    >>> myFeature.discrete = False
    ```

    The .vector is the most important part of the feature, and it starts out as None.

    ```python
    >>> myFeature.vector is None
    True
    ```

    Calling .prepareVector() gives it a list of Zeros of the length of dimensions.

    ```python
    >>> myFeature.prepareVectors()
    ```

    ```python
    >>> myFeature.vector
    [0, 0, 0]
    ```

    Now we can set the vector parts:

    ```python
    >>> myFeature.vector[0] = 4
    >>> myFeature.vector[1] = 2
    >>> myFeature.vector[2] = 1
    ```

    It’s okay just to assign a new list to .vector itself.

    There is a “normalize()” method which normalizes the values
    of a histogram to sum to 1.

    ```python
    >>> myFeature.normalize()
    >>> myFeature.vector
    [0.571..., 0.285..., 0.142...]
    ```

    And that’s it! FeatureExtractors are much more interesting.

[`Feature`](#music21.features.base.Feature "music21.features.base.Feature") methods

Feature.normalize()[[source]](../_modules/music21/features/base.html#Feature.normalize)
:   Normalizes the vector so that the sum of its elements is 1.

Feature.prepareVectors()[[source]](../_modules/music21/features/base.html#Feature.prepareVectors)
:   Prepare the vector stored in this feature.

## FeatureExtractor

class music21.features.base.FeatureExtractor(*dataOrStream=None*, *\*\*keywords*)[[source]](../_modules/music21/features/base.html#FeatureExtractor)
:   A model of process that extracts a feature from a Music21 Stream.
    The main public interface is the extract() method.

    The extractor can be passed a Stream or a reference to a DataInstance.
    All Streams are internally converted to a DataInstance if necessary.
    Usage of a DataInstance offers significant performance advantages, as common forms of
    the Stream are cached for easy processing.

[`FeatureExtractor`](#music21.features.base.FeatureExtractor "music21.features.base.FeatureExtractor") methods

FeatureExtractor.extract(*source=None*)[[source]](../_modules/music21/features/base.html#FeatureExtractor.extract)
:   Extract the feature and return the result.

FeatureExtractor.fillFeatureAttributes(*feature=None*)[[source]](../_modules/music21/features/base.html#FeatureExtractor.fillFeatureAttributes)
:   Fill the attributes of a Feature with the descriptors in the FeatureExtractor.

FeatureExtractor.getAttributeLabels()[[source]](../_modules/music21/features/base.html#FeatureExtractor.getAttributeLabels)
:   Return a list of string in a form that is appropriate for data storage.

    ```python
    >>> fe = features.jSymbolic.AmountOfArpeggiationFeature()
    >>> fe.getAttributeLabels()
    ['Amount_of_Arpeggiation']
    ```

    ```python
    >>> fe = features.jSymbolic.FifthsPitchHistogramFeature()
    >>> fe.getAttributeLabels()
    ['Fifths_Pitch_Histogram_0', 'Fifths_Pitch_Histogram_1', 'Fifths_Pitch_Histogram_2',
     'Fifths_Pitch_Histogram_3', 'Fifths_Pitch_Histogram_4', 'Fifths_Pitch_Histogram_5',
     'Fifths_Pitch_Histogram_6', 'Fifths_Pitch_Histogram_7', 'Fifths_Pitch_Histogram_8',
     'Fifths_Pitch_Histogram_9', 'Fifths_Pitch_Histogram_10', 'Fifths_Pitch_Histogram_11']
    ```

FeatureExtractor.getBlankFeature()[[source]](../_modules/music21/features/base.html#FeatureExtractor.getBlankFeature)
:   Return a properly configured plain feature as a placeholder

    ```python
    >>> fe = features.jSymbolic.InitialTimeSignatureFeature()
    >>> fe.name
    'Initial Time Signature'
    ```

    ```python
    >>> blankF = fe.getBlankFeature()
    >>> blankF.vector
    [0, 0]
    >>> blankF.name
    'Initial Time Signature'
    ```

FeatureExtractor.prepareFeature()[[source]](../_modules/music21/features/base.html#FeatureExtractor.prepareFeature)
:   Prepare a new Feature object for data acquisition.

    ```python
    >>> s = stream.Stream()
    >>> fe = features.jSymbolic.InitialTimeSignatureFeature(s)
    >>> fe.prepareFeature()
    >>> fe.feature.name
    'Initial Time Signature'
    >>> fe.feature.dimensions
    2
    >>> fe.feature.vector
    [0, 0]
    ```

FeatureExtractor.process()[[source]](../_modules/music21/features/base.html#FeatureExtractor.process)
:   Do processing necessary, storing result in \_feature.

FeatureExtractor.setData(*dataOrStream*)[[source]](../_modules/music21/features/base.html#FeatureExtractor.setData)
:   Set the data that this FeatureExtractor will process.
    Either a Stream or a DataInstance object can be provided.

## DataInstance

class music21.features.base.DataInstance(*streamOrPath=None*, *id=None*)[[source]](../_modules/music21/features/base.html#DataInstance)
:   A data instance for analysis. This object prepares a Stream
    (by stripping ties, etc.) and stores
    multiple commonly-used stream representations once, providing rapid processing.

[`DataInstance`](#music21.features.base.DataInstance "music21.features.base.DataInstance") methods

DataInstance.\_\_getitem\_\_(*key*)[[source]](../_modules/music21/features/base.html#DataInstance.__getitem__)
:   Get a form of this Stream, using a cached version if available.

    ```python
    >>> di = features.DataInstance('bach/bwv66.6')
    >>> len(di['flat'])
    197
    >>> len(di['flat.pitches'])
    163
    >>> len(di['flat.notes'])
    163
    >>> len(di['getElementsByClass(Measure)'])
    40
    >>> len(di['flat.getElementsByClass(TimeSignature)'])
    4
    ```

DataInstance.getClassValue()[[source]](../_modules/music21/features/base.html#DataInstance.getClassValue)

DataInstance.getId()[[source]](../_modules/music21/features/base.html#DataInstance.getId)

DataInstance.parseStream()[[source]](../_modules/music21/features/base.html#DataInstance.parseStream)
:   If a path to a Stream has been passed in at creation,
    then this will parse it (whether it’s a corpus string,
    a converter string (url or filepath), a pathlib.Path,
    or a metadata.bundles.MetadataEntry).

DataInstance.setClassLabel(*classLabel*, *classValue=None*)[[source]](../_modules/music21/features/base.html#DataInstance.setClassLabel)
:   Set the class label, as well as the class value if known.
    The class label is the attribute name used to define the class of this data instance.

    ```python
    >>> s = corpus.parse('bwv66.6')
    >>> di = features.DataInstance(s)
    >>> di.setClassLabel('Composer', 'Bach')
    ```

DataInstance.setupPostStreamParse()[[source]](../_modules/music21/features/base.html#DataInstance.setupPostStreamParse)
:   Set up the StreamForms objects and other things that
    need to be done after a Stream is passed in but before
    feature extracting is run.

    Run automatically at instantiation if a Stream is passed in.

## StreamForms

class music21.features.base.StreamForms(*streamObj: [Stream](moduleStreamBase.html#music21.stream.base.Stream "music21.stream.base.Stream")*, *prepareStream=True*)[[source]](../_modules/music21/features/base.html#StreamForms)
:   A dictionary-like wrapper of a Stream, providing
    numerous representations, generated on-demand, and cached.

    A single StreamForms object can be created for an
    entire Score, as well as one for each Part and/or Voice.

    A DataSet object manages one or more StreamForms
    objects, and exposes them to FeatureExtractors for usage.

    The streamObj is stored as self.stream and if “prepared” then
    the prepared form is stored as .prepared

    A dictionary .forms stores various intermediary representations
    of the stream which is the main power of this routine, making
    it simple to add additional feature extractors at low additional
    time cost.

[`StreamForms`](#music21.features.base.StreamForms "music21.features.base.StreamForms") methods

StreamForms.\_\_getitem\_\_(*key: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [Stream](moduleStreamBase.html#music21.stream.base.Stream "music21.stream.base.Stream")[[source]](../_modules/music21/features/base.html#StreamForms.__getitem__)
:   Get a form of this Stream, using a cached version if available.

StreamForms.formBeatHistogram(*secondsMap*)[[source]](../_modules/music21/features/base.html#StreamForms.formBeatHistogram)

StreamForms.formChordify(*prepared*)[[source]](../_modules/music21/features/base.html#StreamForms.formChordify)

StreamForms.formContourList(*prepared*)[[source]](../_modules/music21/features/base.html#StreamForms.formContourList)

StreamForms.formGetElementsByClassMeasure(*prepared*)[[source]](../_modules/music21/features/base.html#StreamForms.formGetElementsByClassMeasure)

StreamForms.formMidiIntervalHistogram(*unused*)[[source]](../_modules/music21/features/base.html#StreamForms.formMidiIntervalHistogram)

StreamForms.formMidiPitchHistogram(*pitches*)[[source]](../_modules/music21/features/base.html#StreamForms.formMidiPitchHistogram)

StreamForms.formPartitionByInstrument(*prepared: [Stream](moduleStreamBase.html#music21.stream.base.Stream "music21.stream.base.Stream")*)[[source]](../_modules/music21/features/base.html#StreamForms.formPartitionByInstrument)

StreamForms.formPitchClassHistogram(*pitches*)[[source]](../_modules/music21/features/base.html#StreamForms.formPitchClassHistogram)

StreamForms.formPitchClassSetHistogram(*prepared*)[[source]](../_modules/music21/features/base.html#StreamForms.formPitchClassSetHistogram)

StreamForms.formQuarterLengthHistogram(*prepared*)[[source]](../_modules/music21/features/base.html#StreamForms.formQuarterLengthHistogram)

StreamForms.formSecondsMap(*prepared*)[[source]](../_modules/music21/features/base.html#StreamForms.formSecondsMap)

StreamForms.formSetClassHistogram(*prepared*)[[source]](../_modules/music21/features/base.html#StreamForms.formSetClassHistogram)

StreamForms.formTypesHistogram(*prepared*)[[source]](../_modules/music21/features/base.html#StreamForms.formTypesHistogram)

StreamForms.keys() → [KeysView](https://docs.python.org/3/library/collections.abc.html#collections.abc.KeysView "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")][[source]](../_modules/music21/features/base.html#StreamForms.keys)

## Functions

music21.features.base.allFeaturesAsList(*streamInput*)[[source]](../_modules/music21/features/base.html#allFeaturesAsList)
:   returns a list containing ALL currently implemented feature extractors

    streamInput can be a Stream, DataInstance, or path to a corpus or local
    file to this data set.

    ```python
    >>> s = converter.parse('tinynotation: 4/4 c4 d e2')
    >>> f = features.allFeaturesAsList(s)
    >>> f[2:5]
    [[2], [2], [1.0]]
    >>> len(f) > 85
    True
    ```

music21.features.base.extractorById(*idOrList*, *library=('jSymbolic', 'native')*)[[source]](../_modules/music21/features/base.html#extractorById)
:   Get the first feature matched by extractorsById().

    ```python
    >>> s = stream.Stream()
    >>> s.append(note.Note('A4'))
    >>> fe = features.extractorById('p20')(s)  # call class
    >>> fe.extract().vector
    [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    ```

music21.features.base.extractorsById(*idOrList*, *library=('jSymbolic', 'native')*)[[source]](../_modules/music21/features/base.html#extractorsById)
:   Given one or more `FeatureExtractor` ids, return the
    appropriate subclass. An optional library argument can be added to define which
    module is used. Current options are jSymbolic and native.

    ```python
    >>> features.extractorsById('p20')
    [<class 'music21.features.jSymbolic.PitchClassDistributionFeature'>]
    ```

    ```python
    >>> [x.id for x in features.extractorsById('p20')]
    ['P20']
    >>> [x.id for x in features.extractorsById(['p19', 'p20'])]
    ['P19', 'P20']
    ```

    Normalizes case:

    ```python
    >>> [x.id for x in features.extractorsById(['r31', 'r32', 'r33', 'r34', 'r35', 'p1', 'p2'])]
    ['R31', 'R32', 'R33', 'R34', 'R35', 'P1', 'P2']
    ```

    Get all feature extractors from all libraries:

    ```python
    >>> y = [x.id for x in features.extractorsById('all')]
    >>> y[0:3], y[-3:-1]
    (['M1', 'M2', 'M3'], ['CS12', 'MC1'])
    ```

music21.features.base.getIndex(*featureString*, *extractorType=None*)[[source]](../_modules/music21/features/base.html#getIndex)
:   Returns the list index of the given feature extractor and the feature extractor
    category (jsymbolic or native). If feature extractor string is not in either
    jsymbolic or native feature extractors, returns None

    optionally include the extractorType (‘jsymbolic’ or ‘native’) if known
    and searching will be made more efficient

    ```python
    >>> features.getIndex('Range')
    (61, 'jsymbolic')
    >>> features.getIndex('Ends With Landini Melodic Contour')
    (18, 'native')
    >>> features.getIndex('aBrandNewFeature!') is None
    True
    >>> features.getIndex('Fifths Pitch Histogram', 'jsymbolic')
    (70, 'jsymbolic')
    >>> features.getIndex('Tonal Certainty', 'native')
    (1, 'native')
    ```

music21.features.base.vectorById(*streamObj*, *vectorId*, *library=('jSymbolic', 'native')*)[[source]](../_modules/music21/features/base.html#vectorById)
:   Utility function to get a vector from an extractor

    ```python
    >>> s = stream.Stream()
    >>> s.append(note.Note('A4'))
    >>> features.vectorById(s, 'p20')
    [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    ```
