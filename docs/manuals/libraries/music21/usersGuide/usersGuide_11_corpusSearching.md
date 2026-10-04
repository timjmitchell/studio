Source: https://music21.org/music21docs/usersGuide/usersGuide_11_corpusSearching.html

# User’s Guide, Chapter 11: Corpus Searching

One of music21’s important features is its capability to help users
examine large bodies of musical works, or *corpora*.

Music21 comes with a substantial corpus called the *core* corpus. When
you download music21 you can immediately start working with the files in
the corpus directory, including the complete chorales of Bach, many
Haydn and Beethoven string quartets, three books of madrigals by
Monteverdi, thousands of folk songs from the Essen and various ABC
databases, and many more.

To load a file from the corpus, simply call *corpus.parse* and assign
that file to a variable:

```python
from music21 import *
bach = corpus.parse('bach/bwv66.6')
```

The `music21` core corpus comes with many thousands of works. All of
them (or at least all the collections) are listed on the
[Corpus Reference](../about/referenceCorpus.html#referencecorpus).

Users can also build their own corpora to index and quickly search their
own collections on disk including multiple local corpora, for different
projects, that can be accessed individually.

This user’s guide will cover more about the corpus’s basic features.
This chapter focuses on music21’s tools for extracting useful metadata -
titles, locations, composers’ names, the key signatures used in each
piece, total durations, ambitus (range) and so forth.

This metadata is collected in *metadata bundles* for each corpus. The
*corpus* module has tools to search these bundles and persist them on
disk for later research.

## Types of corpora

Music21 works with three categories of *corpora*, made explicit via the
`corpus.Corpus` abstract class.

The first category is the *core* corpus, a large collection of musical
works packaged with most music21 installations, including many works
from the common practice era, and inumerable folk songs, in a variety of
formats:

```python
coreCorpus = corpus.corpora.CoreCorpus()
len(coreCorpus.getPaths())
```

```python
 3194
```

Note

If you’ve installed a “no corpus” version of music21, you can still access
the *core* corpus with a little work. Download the *core* corpus from
music21’s website, and install it on your system somewhere. Then, teach
music21 where you installed it like this:

```python
>>> coreCorpus = corpus.corpora.CoreCorpus()
>>> coreCorpus.manualCoreCorpusPath = 'path/to/core/corpus'
```

## Local Corpus

`Music21` also can have one or more *local* corpora–bodies of works
provided and configured by individual music21 users for their own
research. They will be covered in
[Chapter 53](usersGuide_53_advancedCorpus.html#usersguide-53-advancedcorpus). Anyone wanting to use
them can jump ahead immediately to that chapter, but for now we’ll
continue with searching in the core corpus.

```python
localCorpus = corpus.corpora.LocalCorpus()
```

You can add and remove paths from a *local* corpus with the
`addPath()` and `removePath()` methods:

```python
localCorpus.addPath('~/Desktop')
localCorpus.directoryPaths
```

```python
 ('/Users/myke/Desktop',)
```

Currently, after adding paths to a corpus, you’ll need to rebuild the
cache.

```python
corpus.cacheMetadata()
```

We hope that this won’t be necessary in the future.

To remove a path, use the `removePath()` method.

```python
localCorpus.removePath('~/Desktop')
```

```python
 /Users/cuthbert/Git/music21base/music21/corpus/corpora.py: WARNING: local metadata cache: starting processing of paths: 0
 /Users/cuthbert/Git/music21base/music21/corpus/corpora.py: WARNING: cache: filename: /var/folders/bb/bmq3z9hs3njfyvpdh88z6v340000gn/T/music21/local.p.gz
 metadata.bundles: WARNING: MetadataBundle Modification Time: 1767557364.3225255
 metadata.bundles: WARNING: Skipped 0 sources already in cache.
 /Users/cuthbert/Git/music21base/music21/corpus/corpora.py: WARNING: cache: writing time: 0.024 md items: 0

 /Users/cuthbert/Git/music21base/music21/corpus/corpora.py: WARNING: cache: filename: /var/folders/bb/bmq3z9hs3njfyvpdh88z6v340000gn/T/music21/local.p.gz
```

By default, a call to `corpus.parse` or `corpus.search` will look
for files in any corpus, core or local.

## Simple searches of the corpus

When you search the corpus, music21 examines each metadata object in the
metadata bundle for the whole corpus and attempts to match your search
string against the contents of the various search fields saved in that
metadata object.

You can use `corpus.search()` to search the metadata associated with
all known corpora, *core*, *virtual* and even each *local* corpus:

```python
sixEight = corpus.search('6/8')
sixEight
```

```python
 <music21.metadata.bundles.MetadataBundle {2164 entries}>
```

To work with all those pieces, you can treat the MetadataBundle like a
list and call `.parse()` on any element:

```python
myPiece = sixEight[0].parse()
myPiece.metadata.title
```

```python
 "I'll Touzle your Kurchy."
```

This will return a `music21.stream.Score` object which you can work
with like any other stream. Or if you just want to see it, there’s a
convenience `.show()` method you can call directly on a MetadataEntry.

You can also search against a single `Corpus` instance, like this one
which ignores anything in your local corpus:

```python
corpus.corpora.CoreCorpus().search('6/8')
```

```python
 <music21.metadata.bundles.MetadataBundle {2164 entries}>
```

Because the result of every metadata search is also a metadata bundle,
you can search your search results to do more complex searches. Remember
that `bachBundle` is a collection of all works where the composer is
Bach. Here we will limit to those pieces in 3/4 time:

```python
bachBundle = corpus.search('bach', 'composer')
bachBundle
```

```python
 <music21.metadata.bundles.MetadataBundle {363 entries}>
```

```python
bachBundle.search('3/4')
```

```python
 <music21.metadata.bundles.MetadataBundle {40 entries}>
```

## Metadata search fields

When you search metadata bundles, you can search either through every
search field in every metadata instance, or through a single, specific
search field. As we mentioned above, searching for “bach” as a composer
renders different results from searching for the word “bach” in general:

```python
corpus.search('bach', 'composer')
```

```python
 <music21.metadata.bundles.MetadataBundle {363 entries}>
```

```python
corpus.search('bach', 'title')
```

```python
 <music21.metadata.bundles.MetadataBundle {20 entries}>
```

```python
corpus.search('bach')
```

```python
 <music21.metadata.bundles.MetadataBundle {564 entries}>
```

So what fields can we actually search through? You can find out like
this (in v2, replace `corpus.manager` with `corpus.corpora.Corpus`):

```python
for field in corpus.manager.listSearchFields():
    print(field)
```

```python
 abstract
 accessRights
 accompanyingMaterialWriter
 actNumber
 adapter
 afterwordAuthor
 alternativeTitle
 ambitus
 analyst
 annotator
 arranger
 associatedWork
 attributedComposer
 audience
 bibliographicCitation
 calligrapher
 collaborator
 collectionDesignation
 collotyper
 commentaryAuthor
 commission
 commissionedBy
 compiler
 composer
 composerAlias
 composerCorporate
 conceptor
 conductor
 conformsTo
 copyright
 corpusFilePath
 countryOfComposition
 date
 dateAccepted
 dateAvailable
 dateCopyrighted
 dateCreated
 dateFirstPublished
 dateIssued
 dateModified
 dateSubmitted
 dateValid
 dedicatedTo
 dedication
 description
 dialogAuthor
 distributor
 editor
 educationLevel
 electronicEditor
 electronicEncoder
 electronicPublisher
 electronicReleaseDate
 engraver
 etcher
 extent
 fileFormat
 fileNumber
 filePath
 firstPublisher
 format
 groupTitle
 hasFormat
 hasPart
 hasVersion
 identifier
 illuminator
 illustrator
 instructionalMethod
 instrumentalist
 introductionAuthor
 isFormatOf
 isPartOf
 isReferencedBy
 isReplacedBy
 isRequiredBy
 isVersionOf
 keySignatureFirst
 keySignatures
 language
 librettist
 license
 lithographer
 localeOfComposition
 lyricist
 manuscriptAccessAcknowledgement
 manuscriptLocation
 manuscriptSourceName
 medium
 metalEngraver
 movementName
 movementNumber
 musician
 noteCount
 number
 numberOfParts
 opusNumber
 orchestrator
 originalDocumentOwner
 originalEditor
 otherContributor
 otherDate
 parentTitle
 pitchHighest
 pitchLowest
 placeFirstPublished
 platemaker
 popularTitle
 printmaker
 producer
 proofreader
 provenance
 publicationTitle
 publisher
 publishersCatalogNumber
 quotationsAuthor
 references
 relation
 replaces
 requires
 responsibleParty
 rightsHolder
 sceneNumber
 scholarlyCatalogAbbreviation
 scholarlyCatalogName
 scoreQuarterLength
 scribe
 singer
 software
 source
 sourcePath
 subject
 suspectedComposer
 tableOfContents
 tempoFirst
 tempos
 textLanguage
 textOriginalLanguage
 timeSignatureFirst
 timeSignatures
 title
 transcriber
 translator
 type
 volume
 volumeNumber
 woodCutter
 woodEngraver
```

This field has grown now that the development team is seeing how useful
this searching method can be! Now that we know what all the search
fields are, we can search through some of the more obscure corners of
the *core* corpus:

```python
corpus.search('taiwan', 'locale')
```

```python
 <music21.metadata.bundles.MetadataBundle {27 entries}>
```

What if you are not searching for an exact match? If you’re searching
for short pieces, you probably don’t want to find pieces with exactly 1
note then union that set with pieces with exactly 2 notes, etc. Or for
pieces from the 19th century, you won’t want to search for 1801, 1802,
etc. What you can do is set up a “predicate callable” which is a
function (either a full python `def` statement or a short `lambda`
function) to filter the results. Each piece will be checked against your
predicate and only those that return true. Here we’ll search for pieces
with between 400 and 500 notes, only in the `core` corpus:

```python
predicate = lambda x: 400 < x < 500
corpus.corpora.CoreCorpus().search(predicate, 'noteCount')
```

```python
 <music21.metadata.bundles.MetadataBundle {213 entries}>
```

You can also pass in compiled regular expressions into the search. In
this case we will use a regular expression likely to find Handel and
Haydn and perhaps not much else:

```python
import re
haydnOrHandel = re.compile(r'ha.d.*', re.IGNORECASE)
corpus.search(haydnOrHandel)
```

```python
 <music21.metadata.bundles.MetadataBundle {186 entries}>
```

Unfortunately this really wasn’t a good search, since we also got folk
songs with the title of “Shandy”. Best to use a ‘\*^\*’ search to match
at the beginning of the word only:

```python
haydnOrHandel = re.compile(r'^ha.d.*', re.IGNORECASE)
corpus.search(haydnOrHandel)
```

```python
 <music21.metadata.bundles.MetadataBundle {15 entries}>
```

We’ve now gone fairly high level in our searching. We will return to the
lowest level in
[Chapter 12: The Music21Object](usersGuide_12_music21object.html#usersguide-12-music21object)
