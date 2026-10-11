Source: https://music21.org/music21docs/moduleReference/moduleFeaturesOutputFormats.html

# music21.features.outputFormats

## OutputARFF

class music21.features.outputFormats.OutputARFF(*dataSet=None*)[[source]](../_modules/music21/features/outputFormats.html#OutputARFF)
:   An ARFF (Attribute-Relation File Format) file.

    See
    <https://web.archive.org/web/20160212022757/http://weka.wikispaces.com/ARFF+%28stable+version%29>
    for more details

    ```python
    >>> oa = features.outputFormats.OutputARFF()
    >>> oa.ext
    '.arff'
    ```

[`OutputARFF`](#music21.features.outputFormats.OutputARFF "music21.features.outputFormats.OutputARFF") bases

* [`OutputFormat`](#music21.features.outputFormats.OutputFormat "music21.features.outputFormats.OutputFormat")

[`OutputARFF`](#music21.features.outputFormats.OutputARFF "music21.features.outputFormats.OutputARFF") methods

OutputARFF.getHeaderLines(*includeClassLabel=True*, *includeId=True*)[[source]](../_modules/music21/features/outputFormats.html#OutputARFF.getHeaderLines)
:   Get the header as a list of lines.

    ```python
    >>> f = [features.jSymbolic.ChangesOfMeterFeature]
    >>> ds = features.DataSet(classLabel='Composer')
    >>> ds.addFeatureExtractors(f)
    >>> of = features.outputFormats.OutputARFF(ds)
    >>> for x in of.getHeaderLines(): print(x)
    @RELATION Composer
    @ATTRIBUTE Identifier STRING
    @ATTRIBUTE Changes_of_Meter NUMERIC
    @ATTRIBUTE class {}
    @DATA
    ```

OutputARFF.getString(*includeClassLabel=True*, *includeId=True*, *lineBreak=None*)[[source]](../_modules/music21/features/outputFormats.html#OutputARFF.getString)

Methods inherited from [`OutputFormat`](#music21.features.outputFormats.OutputFormat "music21.features.outputFormats.OutputFormat"):

|  |  |  |
| --- | --- | --- |
| * [`write()`](#music21.features.outputFormats.OutputFormat.write "music21.features.outputFormats.OutputFormat.write") |  |  |

## OutputCSV

class music21.features.outputFormats.OutputCSV(*dataSet=None*)[[source]](../_modules/music21/features/outputFormats.html#OutputCSV)
:   Comma-separated value list.

[`OutputCSV`](#music21.features.outputFormats.OutputCSV "music21.features.outputFormats.OutputCSV") bases

* [`OutputFormat`](#music21.features.outputFormats.OutputFormat "music21.features.outputFormats.OutputFormat")

[`OutputCSV`](#music21.features.outputFormats.OutputCSV "music21.features.outputFormats.OutputCSV") methods

OutputCSV.getHeaderLines(*includeClassLabel=True*, *includeId=True*)[[source]](../_modules/music21/features/outputFormats.html#OutputCSV.getHeaderLines)
:   Get the header as a list of lines.

    ```python
    >>> f = [features.jSymbolic.ChangesOfMeterFeature]
    >>> ds = features.DataSet(classLabel='Composer')
    >>> ds.addFeatureExtractors(f)
    >>> of = features.outputFormats.OutputCSV(ds)
    >>> of.getHeaderLines()[0]
    ['Identifier', 'Changes_of_Meter', 'Composer']
    ```

OutputCSV.getString(*includeClassLabel=True*, *includeId=True*, *lineBreak=None*)[[source]](../_modules/music21/features/outputFormats.html#OutputCSV.getString)

Methods inherited from [`OutputFormat`](#music21.features.outputFormats.OutputFormat "music21.features.outputFormats.OutputFormat"):

|  |  |  |
| --- | --- | --- |
| * [`write()`](#music21.features.outputFormats.OutputFormat.write "music21.features.outputFormats.OutputFormat.write") |  |  |

## OutputFormat

class music21.features.outputFormats.OutputFormat(*dataSet=None*)[[source]](../_modules/music21/features/outputFormats.html#OutputFormat)
:   Provide output for a DataSet, which is passed in as an initial argument.

[`OutputFormat`](#music21.features.outputFormats.OutputFormat "music21.features.outputFormats.OutputFormat") methods

OutputFormat.getHeaderLines()[[source]](../_modules/music21/features/outputFormats.html#OutputFormat.getHeaderLines)
:   Get the header as a list of lines.

OutputFormat.getString(*includeClassLabel=True*, *includeId=True*, *lineBreak=None*)[[source]](../_modules/music21/features/outputFormats.html#OutputFormat.getString)

OutputFormat.write(*fp=None*, *includeClassLabel=True*, *includeId=True*)[[source]](../_modules/music21/features/outputFormats.html#OutputFormat.write)
:   Write the file. If not file path is given, a temporary file will be written.

## OutputTabOrange

class music21.features.outputFormats.OutputTabOrange(*dataSet=None*)[[source]](../_modules/music21/features/outputFormats.html#OutputTabOrange)
:   Tab delimited file format used with Orange.

    For more information, see:

    <https://orange3.readthedocs.io/projects/orange-data-mining-library/en/latest/tutorial/data.html#saving-the-data>

[`OutputTabOrange`](#music21.features.outputFormats.OutputTabOrange "music21.features.outputFormats.OutputTabOrange") bases

* [`OutputFormat`](#music21.features.outputFormats.OutputFormat "music21.features.outputFormats.OutputFormat")

[`OutputTabOrange`](#music21.features.outputFormats.OutputTabOrange "music21.features.outputFormats.OutputTabOrange") methods

OutputTabOrange.getHeaderLines(*includeClassLabel=True*, *includeId=True*)[[source]](../_modules/music21/features/outputFormats.html#OutputTabOrange.getHeaderLines)
:   Get the header as a list of lines.

    ```python
    >>> f = [features.jSymbolic.ChangesOfMeterFeature]
    >>> ds = features.DataSet()
    >>> ds.addFeatureExtractors(f)
    >>> of = features.outputFormats.OutputTabOrange(ds)
    >>> for x in of.getHeaderLines(): print(x)
    ['Identifier', 'Changes_of_Meter']
    ['string', 'discrete']
    ['meta', '']
    ```

    ```python
    >>> ds = features.DataSet(classLabel='Composer')
    >>> ds.addFeatureExtractors(f)
    >>> of = features.outputFormats.OutputTabOrange(ds)
    >>> for x in of.getHeaderLines(): print(x)
    ['Identifier', 'Changes_of_Meter', 'Composer']
    ['string', 'discrete', 'discrete']
    ['meta', '', 'class']
    ```

OutputTabOrange.getString(*includeClassLabel=True*, *includeId=True*, *lineBreak=None*)[[source]](../_modules/music21/features/outputFormats.html#OutputTabOrange.getString)
:   Get the complete DataSet as a string with the appropriate headers.

Methods inherited from [`OutputFormat`](#music21.features.outputFormats.OutputFormat "music21.features.outputFormats.OutputFormat"):

|  |  |  |
| --- | --- | --- |
| * [`write()`](#music21.features.outputFormats.OutputFormat.write "music21.features.outputFormats.OutputFormat.write") |  |  |
