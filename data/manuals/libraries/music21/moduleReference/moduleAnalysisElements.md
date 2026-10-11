Source: https://music21.org/music21docs/moduleReference/moduleAnalysisElements.html

# music21.analysis.elements

## Functions

music21.analysis.elements.attributeCount(*streamOrStreamIter*, *attrName='quarterLength'*) → [Counter](https://docs.python.org/3/library/collections.html#collections.Counter "(in Python v3.14)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")][[source]](../_modules/music21/analysis/elements.html#attributeCount)
:   Return a collections.Counter of attribute usage for elements in a stream
    or StreamIterator

    ```python
    >>> bach = corpus.parse('bach/bwv324.xml')
    >>> bachIter = bach.parts[0].recurse().getElementsByClass(note.Note)
    >>> qlCount = analysis.elements.attributeCount(bachIter, 'quarterLength')
    >>> qlCount.most_common(3)
    [(1.0, 12), (2.0, 11), (4.0, 2)]
    ```

    * Changed in v4: Returns a collections.Counter object.
