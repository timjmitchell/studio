Source: https://music21.org/music21docs/moduleReference/moduleCorpusWork.html

# music21.corpus.work

This is a lightweight module that stores information about individual corpus works.

## CorpusFile

class music21.corpus.work.CorpusFile(*path*, *title*, *filename*, *format*, *ext*)

## CorpusWork

class music21.corpus.work.CorpusWork(*title*, *files*, *virtual*)

## DirectoryInformation

class music21.corpus.work.DirectoryInformation(*dirName=''*, *dirTitle=''*, *isComposer=True*, *corpusObject=None*)[[source]](../_modules/music21/corpus/work.html#DirectoryInformation)
:   returns information about a directory in a Corpus. Called from corpus.corpora.Corpus

    only tested with CoreCorpus so far.

[`DirectoryInformation`](#music21.corpus.work.DirectoryInformation "music21.corpus.work.DirectoryInformation") bases

* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`DirectoryInformation`](#music21.corpus.work.DirectoryInformation "music21.corpus.work.DirectoryInformation") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`DirectoryInformation`](#music21.corpus.work.DirectoryInformation "music21.corpus.work.DirectoryInformation") methods

DirectoryInformation.findWorks()[[source]](../_modules/music21/corpus/work.html#DirectoryInformation.findWorks)
:   Populate other information about the directory such as
    files and filenames.

    ```python
    >>> di = corpus.work.DirectoryInformation('schoenberg',
    ...             corpusObject=corpus.corpora.CoreCorpus())
    >>> di.findWorks()
    OrderedDict([('opus19', CorpusWork(title='Opus 19',
                                files=[CorpusFile(path='schoenberg...opus19...movement2.mxl',
                                                    title='Movement 2',
                                                    filename='movement2.mxl',
                                                    format='musicxml',
                                                    ext='.mxl'),
                                        CorpusFile(path='schoenberg...opus19...movement6.mxl',
                                                    title='Movement 6',
                                                    filename='movement6.mxl',
                                                    format='musicxml',
                                                    ext='.mxl')],
                                virtual=False))])
    ```

    (The ellipses in the documentation above represent ‘/’ on Mac/Unix systems and
    ‘' on Windows.)
