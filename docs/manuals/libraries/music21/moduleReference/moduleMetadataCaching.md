Source: https://music21.org/music21docs/moduleReference/moduleMetadataCaching.html

# music21.metadata.caching

## JobProcessor

class music21.metadata.caching.JobProcessor[[source]](../_modules/music21/metadata/caching.html#JobProcessor)
:   Processes metadata-caching jobs, either serially (e.g. single-threaded) or
    in parallel, as a generator.

    Yields a dictionary of:

    * MetadataEntry instances
    * failed file paths
    * the last processed file path
    * the number of remaining jobs

    ```python
    >>> jobs = []
    >>> mdb = corpus.corpora.CoreCorpus().search('monteverdi')[:3]
    >>> paths = [x.sourcePath for x in mdb]
    ```

    ```python
    >>> for corpusPath in paths:
    ...     job = metadata.caching.MetadataCachingJob(
    ...         corpusPath,
    ...         parseUsingCorpus=True,
    ...         corpusName='core',
    ...         )
    ...     jobs.append(job)
    >>> jobGenerator = metadata.caching.JobProcessor.process_serial(jobs)
    >>> for result in jobGenerator:
    ...     print(result['remainingJobs'])
    ...
    2
    1
    0
    ```

[`JobProcessor`](#music21.metadata.caching.JobProcessor "music21.metadata.caching.JobProcessor") methods

static JobProcessor.process\_parallel(*jobs*, *processCount=None*)[[source]](../_modules/music21/metadata/caching.html#JobProcessor.process_parallel)
:   Process jobs in parallel, with processCount processes.

    If processCount is none, use 1 fewer process than the number of
    available cores.

    jobs is a list of `MetadataCachingJob` objects.

static JobProcessor.process\_serial(*jobs: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[MetadataCachingJob](#music21.metadata.caching.MetadataCachingJob "music21.metadata.caching.MetadataCachingJob")]*)[[source]](../_modules/music21/metadata/caching.html#JobProcessor.process_serial)
:   Process jobs serially.

## MetadataCachingJob

class music21.metadata.caching.MetadataCachingJob(*filePath*, *jobNumber=0*, *parseUsingCorpus=True*, *corpusName=None*)[[source]](../_modules/music21/metadata/caching.html#MetadataCachingJob)
:   Parses one corpus path, and attempts to extract metadata from it:

    ```python
    >>> job = metadata.caching.MetadataCachingJob(
    ...     'bach/bwv66.6',
    ...     parseUsingCorpus=True,
    ...     corpusName='core',
    ...     )
    >>> job.jobNumber
    0
    >>> job.corpusName
    'core'
    >>> job.run()
    ((<music21.metadata.bundles.MetadataEntry 'bach_bwv66_6'>,), ())
    >>> results = job.getResults()
    >>> errors = job.getErrors()
    ```

    TODO: error list, not just numbers needs to be reported back up.

[`MetadataCachingJob`](#music21.metadata.caching.MetadataCachingJob "music21.metadata.caching.MetadataCachingJob") read-only properties

MetadataCachingJob.cleanFilePath

[`MetadataCachingJob`](#music21.metadata.caching.MetadataCachingJob "music21.metadata.caching.MetadataCachingJob") methods

MetadataCachingJob.getErrors()[[source]](../_modules/music21/metadata/caching.html#MetadataCachingJob.getErrors)

MetadataCachingJob.getResults()[[source]](../_modules/music21/metadata/caching.html#MetadataCachingJob.getResults)

MetadataCachingJob.parseFilePath()[[source]](../_modules/music21/metadata/caching.html#MetadataCachingJob.parseFilePath)

MetadataCachingJob.parseNonOpus(*parsedObject*)[[source]](../_modules/music21/metadata/caching.html#MetadataCachingJob.parseNonOpus)

MetadataCachingJob.parseOpus(*parsedObject*)[[source]](../_modules/music21/metadata/caching.html#MetadataCachingJob.parseOpus)

MetadataCachingJob.parseScoreInsideOpus(*score*, *scoreNumber*)[[source]](../_modules/music21/metadata/caching.html#MetadataCachingJob.parseScoreInsideOpus)

MetadataCachingJob.run()[[source]](../_modules/music21/metadata/caching.html#MetadataCachingJob.run)

## WorkerProcess

class music21.metadata.caching.WorkerProcess(*job\_queue*, *result\_queue*)[[source]](../_modules/music21/metadata/caching.html#WorkerProcess)
:   A worker process for use by the multithreaded metadata-caching job
    processor.

[`WorkerProcess`](#music21.metadata.caching.WorkerProcess "music21.metadata.caching.WorkerProcess") methods

WorkerProcess.run()[[source]](../_modules/music21/metadata/caching.html#WorkerProcess.run)
:   Method to be run in sub-process; can be overridden in sub-class

## Functions

music21.metadata.caching.cacheMetadata(*corpusNames=None*, *useMultiprocessing=True*, *verbose=False*)[[source]](../_modules/music21/metadata/caching.html#cacheMetadata)
:   Cache metadata from corpora in corpusNames as local cache files.

    Call as `metadata.cacheMetadata()`
