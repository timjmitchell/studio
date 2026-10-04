Source: https://music21.org/music21docs/moduleReference/moduleLilyLilyObjects.html

# music21.lily.lilyObjects

music21 translates to Lilypond format and if Lilypond is installed on the
local computer, can automatically generate .pdf, .png, and .svg versions
of musical files using Lilypond.

The Grammar for Lilypond comes from
<http://lilypond.org/doc/v2.14/Documentation/notation/lilypond-grammar>

## LyAlternativeMusic

class music21.lily.lilyObjects.LyAlternativeMusic(*musicList=None*)[[source]](../_modules/music21/lily/lilyObjects.html#LyAlternativeMusic)

[`LyAlternativeMusic`](#music21.lily.lilyObjects.LyAlternativeMusic "music21.lily.lilyObjects.LyAlternativeMusic") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyAlternativeMusic`](#music21.lily.lilyObjects.LyAlternativeMusic "music21.lily.lilyObjects.LyAlternativeMusic") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyAlternativeMusic`](#music21.lily.lilyObjects.LyAlternativeMusic "music21.lily.lilyObjects.LyAlternativeMusic") methods

LyAlternativeMusic.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyAlternativeMusic.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LyAssignment

class music21.lily.lilyObjects.LyAssignment(*assignmentId=None*, *identifierInit=None*, *propertyPath=None*, *embeddedScm=None*)[[source]](../_modules/music21/lily/lilyObjects.html#LyAssignment)
:   one of three forms of assignment:

    > assignment\_id ‘=’ identifier\_init
    > assignment\_id property\_path ‘=’ identifier\_init
    > embedded\_scm

    if self.embeddedScm is not None, uses type 3
    if self.propertyPath is not None, uses type 2
    else uses type 1 or raises an exception.

    ```python
    >>> lyIdInit = lily.lilyObjects.LyIdentifierInit(string='hi')
    >>> lya = lily.lilyObjects.LyAssignment(assignmentId='title', identifierInit=lyIdInit)
    >>> print(lya)
    title = "hi"
    ```

    Note that you could also pass assignmentId a LyAssignmentId object,
    but that’s overkill for a lot of things.

[`LyAssignment`](#music21.lily.lilyObjects.LyAssignment "music21.lily.lilyObjects.LyAssignment") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyAssignment`](#music21.lily.lilyObjects.LyAssignment "music21.lily.lilyObjects.LyAssignment") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyAssignment`](#music21.lily.lilyObjects.LyAssignment "music21.lily.lilyObjects.LyAssignment") methods

LyAssignment.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyAssignment.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LyAssignmentId

class music21.lily.lilyObjects.LyAssignmentId(*content=None*, *isLyricString=False*)[[source]](../_modules/music21/lily/lilyObjects.html#LyAssignmentId)
:   ```python
    >>> lyAssignmentId = lily.lilyObjects.LyAssignmentId('title', isLyricString=False)
    >>> str(lyAssignmentId)
    'title'
    ```

[`LyAssignmentId`](#music21.lily.lilyObjects.LyAssignmentId "music21.lily.lilyObjects.LyAssignmentId") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyAssignmentId`](#music21.lily.lilyObjects.LyAssignmentId "music21.lily.lilyObjects.LyAssignmentId") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyAssignmentId`](#music21.lily.lilyObjects.LyAssignmentId "music21.lily.lilyObjects.LyAssignmentId") methods

LyAssignmentId.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyAssignmentId.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LyBookBlock

class music21.lily.lilyObjects.LyBookBlock(*bookBody=None*)[[source]](../_modules/music21/lily/lilyObjects.html#LyBookBlock)

[`LyBookBlock`](#music21.lily.lilyObjects.LyBookBlock "music21.lily.lilyObjects.LyBookBlock") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyBookBlock`](#music21.lily.lilyObjects.LyBookBlock "music21.lily.lilyObjects.LyBookBlock") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyBookBlock`](#music21.lily.lilyObjects.LyBookBlock "music21.lily.lilyObjects.LyBookBlock") methods

LyBookBlock.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyBookBlock.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LyBookBody

class music21.lily.lilyObjects.LyBookBody(*contents=None*, *bookIdentifier=None*)[[source]](../_modules/music21/lily/lilyObjects.html#LyBookBody)
:   Contains None, bookIdentifier (string?) or one or more of the following:

    > paperBlock
    > bookPartBlock
    > scoreBlock
    > compositeMusic
    > fullMarkup
    > fullMarkupList
    > lilypondHeader
    > error

    ```python
    >>> lyBookBody = lily.lilyObjects.LyBookBody(bookIdentifier='bookId')
    >>> lyBookBody.stringOutput()
    'bookId'
    ```

    ```python
    >>> lyBookBody = lily.lilyObjects.LyBookBody()
    >>> lyBookBody.stringOutput() is None
    True
    ```

    ```python
    >>> lyBookBody = lily.lilyObjects.LyBookBody(contents=['a', 'b', 'c'])
    >>> print(lyBookBody.stringOutput())
    a
    b
    c
    ```

[`LyBookBody`](#music21.lily.lilyObjects.LyBookBody "music21.lily.lilyObjects.LyBookBody") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyBookBody`](#music21.lily.lilyObjects.LyBookBody "music21.lily.lilyObjects.LyBookBody") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyBookBody`](#music21.lily.lilyObjects.LyBookBody "music21.lily.lilyObjects.LyBookBody") methods

LyBookBody.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyBookBody.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LyBookpartBlock

class music21.lily.lilyObjects.LyBookpartBlock(*bookpartBody=None*)[[source]](../_modules/music21/lily/lilyObjects.html#LyBookpartBlock)
:   ```python
    >>> lbb = lily.lilyObjects.LyBookpartBlock()
    >>> lbb.stringOutput()
    '\\bookpart  { \n\n } \n'
    ```

[`LyBookpartBlock`](#music21.lily.lilyObjects.LyBookpartBlock "music21.lily.lilyObjects.LyBookpartBlock") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyBookpartBlock`](#music21.lily.lilyObjects.LyBookpartBlock "music21.lily.lilyObjects.LyBookpartBlock") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyBookpartBlock`](#music21.lily.lilyObjects.LyBookpartBlock "music21.lily.lilyObjects.LyBookpartBlock") methods

LyBookpartBlock.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyBookpartBlock.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LyBookpartBody

class music21.lily.lilyObjects.LyBookpartBody(*contents=None*, *bookIdentifier=None*)[[source]](../_modules/music21/lily/lilyObjects.html#LyBookpartBody)
:   Contains None, bookIdentifier (string?) or one or more of the following:

    > paperBlock
    > scoreBlock
    > compositeMusic
    > fullMarkup
    > fullMarkupList
    > lilypondHeader
    > error

    ```python
    >>> lyBookpartBody = lily.lilyObjects.LyBookpartBody(bookIdentifier='bookId')
    >>> lyBookpartBody.stringOutput()
    'bookId'
    ```

    ```python
    >>> lyBookpartBody = lily.lilyObjects.LyBookpartBody()
    >>> lyBookpartBody.stringOutput() is None
    True
    ```

    ```python
    >>> lyBookpartBody = lily.lilyObjects.LyBookpartBody(contents=['a', 'b', 'c'])
    >>> print(lyBookpartBody.stringOutput())
    a
    b
    c
    ```

[`LyBookpartBody`](#music21.lily.lilyObjects.LyBookpartBody "music21.lily.lilyObjects.LyBookpartBody") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyBookpartBody`](#music21.lily.lilyObjects.LyBookpartBody "music21.lily.lilyObjects.LyBookpartBody") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyBookpartBody`](#music21.lily.lilyObjects.LyBookpartBody "music21.lily.lilyObjects.LyBookpartBody") methods

LyBookpartBody.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyBookpartBody.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LyChordBody

class music21.lily.lilyObjects.LyChordBody(*chordBodyElements=None*)[[source]](../_modules/music21/lily/lilyObjects.html#LyChordBody)

[`LyChordBody`](#music21.lily.lilyObjects.LyChordBody "music21.lily.lilyObjects.LyChordBody") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyChordBody`](#music21.lily.lilyObjects.LyChordBody "music21.lily.lilyObjects.LyChordBody") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyChordBody`](#music21.lily.lilyObjects.LyChordBody "music21.lily.lilyObjects.LyChordBody") methods

LyChordBody.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyChordBody.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LyChordBodyElement

class music21.lily.lilyObjects.LyChordBodyElement(*parts=None*)[[source]](../_modules/music21/lily/lilyObjects.html#LyChordBodyElement)
:   Contains a note or a drum pitch or a music function:

    ```python
    chord_body_element: pitch
                          exclamations (a string of zero or more ! marks)
                          questions (a string of zero or more ? marks)
                          octave_check
                          post_events
                     | DRUM_PITCH post_events
                     | music_function_chord_body
    ```

    TODO: only the first form is currently supported in creation

[`LyChordBodyElement`](#music21.lily.lilyObjects.LyChordBodyElement "music21.lily.lilyObjects.LyChordBodyElement") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyChordBodyElement`](#music21.lily.lilyObjects.LyChordBodyElement "music21.lily.lilyObjects.LyChordBodyElement") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyChordBodyElement`](#music21.lily.lilyObjects.LyChordBodyElement "music21.lily.lilyObjects.LyChordBodyElement") methods

LyChordBodyElement.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyChordBodyElement.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LyCommandElement

class music21.lily.lilyObjects.LyCommandElement(*commandType=None*, *argument=None*)[[source]](../_modules/music21/lily/lilyObjects.html#LyCommandElement)

[`LyCommandElement`](#music21.lily.lilyObjects.LyCommandElement "music21.lily.lilyObjects.LyCommandElement") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyCommandElement`](#music21.lily.lilyObjects.LyCommandElement "music21.lily.lilyObjects.LyCommandElement") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyCommandElement`](#music21.lily.lilyObjects.LyCommandElement "music21.lily.lilyObjects.LyCommandElement") methods

LyCommandElement.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyCommandElement.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LyCommandEvent

class music21.lily.lilyObjects.LyCommandEvent(*commandType=None*, *argument1=None*, *argument2=None*)[[source]](../_modules/music21/lily/lilyObjects.html#LyCommandEvent)

[`LyCommandEvent`](#music21.lily.lilyObjects.LyCommandEvent "music21.lily.lilyObjects.LyCommandEvent") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyCommandEvent`](#music21.lily.lilyObjects.LyCommandEvent "music21.lily.lilyObjects.LyCommandEvent") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyCommandEvent`](#music21.lily.lilyObjects.LyCommandEvent "music21.lily.lilyObjects.LyCommandEvent") methods

LyCommandEvent.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyCommandEvent.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LyCompositeMusic

class music21.lily.lilyObjects.LyCompositeMusic(*prefixCompositeMusic=None*, *groupedMusicList=None*, *newLyrics=None*)[[source]](../_modules/music21/lily/lilyObjects.html#LyCompositeMusic)
:   one of LyPrefixCompositeMusic or LyGroupedMusicList stored in self.contents

[`LyCompositeMusic`](#music21.lily.lilyObjects.LyCompositeMusic "music21.lily.lilyObjects.LyCompositeMusic") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyCompositeMusic`](#music21.lily.lilyObjects.LyCompositeMusic "music21.lily.lilyObjects.LyCompositeMusic") read-only properties

LyCompositeMusic.contents

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyCompositeMusic`](#music21.lily.lilyObjects.LyCompositeMusic "music21.lily.lilyObjects.LyCompositeMusic") methods

LyCompositeMusic.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyCompositeMusic.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LyContextChange

class music21.lily.lilyObjects.LyContextChange(*before=None*, *after=None*)[[source]](../_modules/music21/lily/lilyObjects.html#LyContextChange)
:   ```python
    >>> lcc = lily.lilyObjects.LyContextChange('x', 'y')
    >>> str(lcc)
    '\\change x = y '
    ```

[`LyContextChange`](#music21.lily.lilyObjects.LyContextChange "music21.lily.lilyObjects.LyContextChange") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyContextChange`](#music21.lily.lilyObjects.LyContextChange "music21.lily.lilyObjects.LyContextChange") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyContextChange`](#music21.lily.lilyObjects.LyContextChange "music21.lily.lilyObjects.LyContextChange") methods

LyContextChange.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyContextChange.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LyContextDefMod

class music21.lily.lilyObjects.LyContextDefMod(*contextDef=None*)[[source]](../_modules/music21/lily/lilyObjects.html#LyContextDefMod)
:   one of consists, remove, accepts, defaultchild, denies, alias, type, description, name

[`LyContextDefMod`](#music21.lily.lilyObjects.LyContextDefMod "music21.lily.lilyObjects.LyContextDefMod") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyContextDefMod`](#music21.lily.lilyObjects.LyContextDefMod "music21.lily.lilyObjects.LyContextDefMod") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyContextDefMod`](#music21.lily.lilyObjects.LyContextDefMod "music21.lily.lilyObjects.LyContextDefMod") methods

LyContextDefMod.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyContextDefMod.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LyContextDefSpecBlock

class music21.lily.lilyObjects.LyContextDefSpecBlock(*contextDefSpecBody=None*)[[source]](../_modules/music21/lily/lilyObjects.html#LyContextDefSpecBlock)

[`LyContextDefSpecBlock`](#music21.lily.lilyObjects.LyContextDefSpecBlock "music21.lily.lilyObjects.LyContextDefSpecBlock") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyContextDefSpecBlock`](#music21.lily.lilyObjects.LyContextDefSpecBlock "music21.lily.lilyObjects.LyContextDefSpecBlock") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyContextDefSpecBlock`](#music21.lily.lilyObjects.LyContextDefSpecBlock "music21.lily.lilyObjects.LyContextDefSpecBlock") methods

LyContextDefSpecBlock.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyContextDefSpecBlock.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LyContextDefSpecBody

class music21.lily.lilyObjects.LyContextDefSpecBody(*contextDefIdentifier=None*, *contextDefSpecBody=None*, *embeddedScm=None*, *contextMod=None*, *contextModification=None*)[[source]](../_modules/music21/lily/lilyObjects.html#LyContextDefSpecBody)
:   None or one of four forms:

    > CONTEXT\_DEF\_IDENTIFIER
    > context\_def\_spec\_body “grobdescriptions” embedded\_scm
    > context\_def\_spec\_body context\_mod
    > context\_def\_spec\_body context\_modification

    ```python
    >>> lyContextBody = lily.lilyObjects.LyContextDefSpecBody(contextDefIdentifier='cdi')
    >>> lyContextBody.stringOutput()
    'cdi'
    ```

    ```python
    >>> embedScm = lily.lilyObjects.LyEmbeddedScm('#t')
    >>> lyContextBody = lily.lilyObjects.LyContextDefSpecBody(
    ...                 contextDefSpecBody='body', embeddedScm=embedScm)
    >>> lyContextBody.stringOutput()
    'body \\grobdescriptions #t'
    ```

[`LyContextDefSpecBody`](#music21.lily.lilyObjects.LyContextDefSpecBody "music21.lily.lilyObjects.LyContextDefSpecBody") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyContextDefSpecBody`](#music21.lily.lilyObjects.LyContextDefSpecBody "music21.lily.lilyObjects.LyContextDefSpecBody") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyContextDefSpecBody`](#music21.lily.lilyObjects.LyContextDefSpecBody "music21.lily.lilyObjects.LyContextDefSpecBody") methods

LyContextDefSpecBody.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyContextDefSpecBody.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LyContextMod

class music21.lily.lilyObjects.LyContextMod(*contextDefOrProperty=None*, *scalar=None*)[[source]](../_modules/music21/lily/lilyObjects.html#LyContextMod)

[`LyContextMod`](#music21.lily.lilyObjects.LyContextMod "music21.lily.lilyObjects.LyContextMod") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyContextMod`](#music21.lily.lilyObjects.LyContextMod "music21.lily.lilyObjects.LyContextMod") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyContextMod`](#music21.lily.lilyObjects.LyContextMod "music21.lily.lilyObjects.LyContextMod") methods

LyContextMod.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyContextMod.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LyContextModList

class music21.lily.lilyObjects.LyContextModList(*contents=None*, *contextModIdentifier=None*)[[source]](../_modules/music21/lily/lilyObjects.html#LyContextModList)
:   contains zero or more LyContextMod objects and an optional contextModIdentifier

[`LyContextModList`](#music21.lily.lilyObjects.LyContextModList "music21.lily.lilyObjects.LyContextModList") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyContextModList`](#music21.lily.lilyObjects.LyContextModList "music21.lily.lilyObjects.LyContextModList") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyContextModList`](#music21.lily.lilyObjects.LyContextModList "music21.lily.lilyObjects.LyContextModList") methods

LyContextModList.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyContextModList.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LyContextModification

class music21.lily.lilyObjects.LyContextModification(*contextModList=None*, *contextModIdentifier=None*, *displayWith=True*)[[source]](../_modules/music21/lily/lilyObjects.html#LyContextModification)
:   represents both context\_modification and optional\_context\_mod

    but not context\_mod!!!!!

[`LyContextModification`](#music21.lily.lilyObjects.LyContextModification "music21.lily.lilyObjects.LyContextModification") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyContextModification`](#music21.lily.lilyObjects.LyContextModification "music21.lily.lilyObjects.LyContextModification") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyContextModification`](#music21.lily.lilyObjects.LyContextModification "music21.lily.lilyObjects.LyContextModification") methods

LyContextModification.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyContextModification.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LyDirectionLessEvent

class music21.lily.lilyObjects.LyDirectionLessEvent(*event=None*)[[source]](../_modules/music21/lily/lilyObjects.html#LyDirectionLessEvent)
:   represents [‘[’, ‘]’, ‘~’, ‘(’, ‘)’, ‘!’, ‘(’, ‘)’, ‘>’, ‘<’]
    or an EVENT\_IDENTIFIER or a tremolo\_type

[`LyDirectionLessEvent`](#music21.lily.lilyObjects.LyDirectionLessEvent "music21.lily.lilyObjects.LyDirectionLessEvent") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyDirectionLessEvent`](#music21.lily.lilyObjects.LyDirectionLessEvent "music21.lily.lilyObjects.LyDirectionLessEvent") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyDirectionLessEvent`](#music21.lily.lilyObjects.LyDirectionLessEvent "music21.lily.lilyObjects.LyDirectionLessEvent") methods

LyDirectionLessEvent.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyDirectionLessEvent.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LyDirectionReqdEvent

class music21.lily.lilyObjects.LyDirectionReqdEvent(*event=None*)[[source]](../_modules/music21/lily/lilyObjects.html#LyDirectionReqdEvent)

[`LyDirectionReqdEvent`](#music21.lily.lilyObjects.LyDirectionReqdEvent "music21.lily.lilyObjects.LyDirectionReqdEvent") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyDirectionReqdEvent`](#music21.lily.lilyObjects.LyDirectionReqdEvent "music21.lily.lilyObjects.LyDirectionReqdEvent") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyDirectionReqdEvent`](#music21.lily.lilyObjects.LyDirectionReqdEvent "music21.lily.lilyObjects.LyDirectionReqdEvent") methods

LyDirectionReqdEvent.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyDirectionReqdEvent.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LyEmbeddedScm

class music21.lily.lilyObjects.LyEmbeddedScm(*content=None*)[[source]](../_modules/music21/lily/lilyObjects.html#LyEmbeddedScm)
:   represents Scheme embedded in Lilypond code.

    Can be either an SCM\_TOKEN (Scheme Token) or SCM\_IDENTIFIER String stored in self.content

    Note that if any LyEmbeddedScm is found in an output then the output SHOULD be marked as unsafe.
    But a lot of standard lilypond functions are actually embedded scheme.
    For instance, clef, which
    as <http://lilypond.org/doc/v2.12/input/lsr/lilypond-snippets/Pitches#Tweaking-clef-properties>
    shows is a macro to run a lot of set commands.

    ```python
    >>> lyScheme = lily.lilyObjects.LyEmbeddedScm('##t')
    >>> str(lyScheme)
    '##t'
    ```

[`LyEmbeddedScm`](#music21.lily.lilyObjects.LyEmbeddedScm "music21.lily.lilyObjects.LyEmbeddedScm") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyEmbeddedScm`](#music21.lily.lilyObjects.LyEmbeddedScm "music21.lily.lilyObjects.LyEmbeddedScm") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyEmbeddedScm`](#music21.lily.lilyObjects.LyEmbeddedScm "music21.lily.lilyObjects.LyEmbeddedScm") methods

LyEmbeddedScm.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyEmbeddedScm.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LyEventChord

class music21.lily.lilyObjects.LyEventChord(*simpleChordElements=None*, *postEvents=None*, *chordRepetition=None*, *multiMeasureRest=None*, *duration=None*, *commandElement=None*, *noteChordElement=None*)[[source]](../_modules/music21/lily/lilyObjects.html#LyEventChord)
:   takes all the parts as a list of up to three elements:

    ```python
    event_chord: simple_chord_elements post_events
           | CHORD_REPETITION optional_notemode_duration post_events
           | MULTI_MEASURE_REST optional_notemode_duration post_events
           | command_element
           | note_chord_element
    ```

    simple\_chord\_elements can be a LySimpleElement object. Or it can be a
    LyNewChord or LyFigureSpec + Duration
    once that is done. But there is no LySimpleChordElements object yet.

[`LyEventChord`](#music21.lily.lilyObjects.LyEventChord "music21.lily.lilyObjects.LyEventChord") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyEventChord`](#music21.lily.lilyObjects.LyEventChord "music21.lily.lilyObjects.LyEventChord") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyEventChord`](#music21.lily.lilyObjects.LyEventChord "music21.lily.lilyObjects.LyEventChord") methods

LyEventChord.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyEventChord.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LyFullMarkup

class music21.lily.lilyObjects.LyFullMarkup(*markupTopOrIdentifier=None*)[[source]](../_modules/music21/lily/lilyObjects.html#LyFullMarkup)

[`LyFullMarkup`](#music21.lily.lilyObjects.LyFullMarkup "music21.lily.lilyObjects.LyFullMarkup") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyFullMarkup`](#music21.lily.lilyObjects.LyFullMarkup "music21.lily.lilyObjects.LyFullMarkup") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyFullMarkup`](#music21.lily.lilyObjects.LyFullMarkup "music21.lily.lilyObjects.LyFullMarkup") methods

LyFullMarkup.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyFullMarkup.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LyFullMarkupList

class music21.lily.lilyObjects.LyFullMarkupList(*markupListOrIdentifier=None*)[[source]](../_modules/music21/lily/lilyObjects.html#LyFullMarkupList)

[`LyFullMarkupList`](#music21.lily.lilyObjects.LyFullMarkupList "music21.lily.lilyObjects.LyFullMarkupList") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyFullMarkupList`](#music21.lily.lilyObjects.LyFullMarkupList "music21.lily.lilyObjects.LyFullMarkupList") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyFullMarkupList`](#music21.lily.lilyObjects.LyFullMarkupList "music21.lily.lilyObjects.LyFullMarkupList") methods

LyFullMarkupList.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyFullMarkupList.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LyGenTextDef

class music21.lily.lilyObjects.LyGenTextDef(*value=None*)[[source]](../_modules/music21/lily/lilyObjects.html#LyGenTextDef)
:   holds either full\_markup, string, or DIGIT

[`LyGenTextDef`](#music21.lily.lilyObjects.LyGenTextDef "music21.lily.lilyObjects.LyGenTextDef") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyGenTextDef`](#music21.lily.lilyObjects.LyGenTextDef "music21.lily.lilyObjects.LyGenTextDef") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyGenTextDef`](#music21.lily.lilyObjects.LyGenTextDef "music21.lily.lilyObjects.LyGenTextDef") methods

LyGenTextDef.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyGenTextDef.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LyGroupedMusicList

class music21.lily.lilyObjects.LyGroupedMusicList(*simultaneousMusic=None*, *sequentialMusic=None*)[[source]](../_modules/music21/lily/lilyObjects.html#LyGroupedMusicList)
:   one of LySimultaneousMusic or LySequentialMusic

[`LyGroupedMusicList`](#music21.lily.lilyObjects.LyGroupedMusicList "music21.lily.lilyObjects.LyGroupedMusicList") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyGroupedMusicList`](#music21.lily.lilyObjects.LyGroupedMusicList "music21.lily.lilyObjects.LyGroupedMusicList") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyGroupedMusicList`](#music21.lily.lilyObjects.LyGroupedMusicList "music21.lily.lilyObjects.LyGroupedMusicList") methods

LyGroupedMusicList.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyGroupedMusicList.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LyIdentifierInit

class music21.lily.lilyObjects.LyIdentifierInit(*scoreBlock=None*, *bookBlock=None*, *bookPartBlock=None*, *outputDef=None*, *contextDefSpecBlock=None*, *music=None*, *postEvent=None*, *numberExpression=None*, *string=None*, *embeddedScm=None*, *fullMarkup=None*, *fullMarkupList=None*, *digit=None*, *contextModification=None*)[[source]](../_modules/music21/lily/lilyObjects.html#LyIdentifierInit)
:   ```python
    >>> lyIdInit = lily.lilyObjects.LyIdentifierInit(string='hello')
    >>> print(lyIdInit)
    "hello"
    ```

[`LyIdentifierInit`](#music21.lily.lilyObjects.LyIdentifierInit "music21.lily.lilyObjects.LyIdentifierInit") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyIdentifierInit`](#music21.lily.lilyObjects.LyIdentifierInit "music21.lily.lilyObjects.LyIdentifierInit") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyIdentifierInit`](#music21.lily.lilyObjects.LyIdentifierInit "music21.lily.lilyObjects.LyIdentifierInit") methods

LyIdentifierInit.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyIdentifierInit.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LyLayout

class music21.lily.lilyObjects.LyLayout[[source]](../_modules/music21/lily/lilyObjects.html#LyLayout)

[`LyLayout`](#music21.lily.lilyObjects.LyLayout "music21.lily.lilyObjects.LyLayout") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyLayout`](#music21.lily.lilyObjects.LyLayout "music21.lily.lilyObjects.LyLayout") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyLayout`](#music21.lily.lilyObjects.LyLayout "music21.lily.lilyObjects.LyLayout") methods

LyLayout.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyLayout.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LyLilypondHeader

class music21.lily.lilyObjects.LyLilypondHeader(*lilypondHeaderBody=None*)[[source]](../_modules/music21/lily/lilyObjects.html#LyLilypondHeader)
:   A header object with a LyHeaderBody

    ```python
    >>> lyh = lily.lilyObjects.LyLilypondHeader()
    >>> str(lyh)
    '\\header { } '
    ```

[`LyLilypondHeader`](#music21.lily.lilyObjects.LyLilypondHeader "music21.lily.lilyObjects.LyLilypondHeader") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyLilypondHeader`](#music21.lily.lilyObjects.LyLilypondHeader "music21.lily.lilyObjects.LyLilypondHeader") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyLilypondHeader`](#music21.lily.lilyObjects.LyLilypondHeader "music21.lily.lilyObjects.LyLilypondHeader") methods

LyLilypondHeader.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyLilypondHeader.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LyLilypondHeaderBody

class music21.lily.lilyObjects.LyLilypondHeaderBody(*assignments=None*)[[source]](../_modules/music21/lily/lilyObjects.html#LyLilypondHeaderBody)

[`LyLilypondHeaderBody`](#music21.lily.lilyObjects.LyLilypondHeaderBody "music21.lily.lilyObjects.LyLilypondHeaderBody") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyLilypondHeaderBody`](#music21.lily.lilyObjects.LyLilypondHeaderBody "music21.lily.lilyObjects.LyLilypondHeaderBody") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyLilypondHeaderBody`](#music21.lily.lilyObjects.LyLilypondHeaderBody "music21.lily.lilyObjects.LyLilypondHeaderBody") methods

LyLilypondHeaderBody.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyLilypondHeaderBody.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LyLilypondTop

class music21.lily.lilyObjects.LyLilypondTop(*contents=None*)[[source]](../_modules/music21/lily/lilyObjects.html#LyLilypondTop)
:   corresponds to the highest level lilypond object in Appendix C:

    ```python
    `lilypond: /* empty */
           | lilypond toplevel_expression
           | lilypond assignment
           | lilypond error
           | lilypond "\invalid"`
    ```

    error and invalid are not defined by music21

[`LyLilypondTop`](#music21.lily.lilyObjects.LyLilypondTop "music21.lily.lilyObjects.LyLilypondTop") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyLilypondTop`](#music21.lily.lilyObjects.LyLilypondTop "music21.lily.lilyObjects.LyLilypondTop") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyLilypondTop`](#music21.lily.lilyObjects.LyLilypondTop "music21.lily.lilyObjects.LyLilypondTop") methods

LyLilypondTop.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyLilypondTop.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LyLyricElement

class music21.lily.lilyObjects.LyLyricElement(*lyMarkupOrString=None*)[[source]](../_modules/music21/lily/lilyObjects.html#LyLyricElement)
:   Object represents a single Lyric in lilypond.

    ```python
    >>> lle = lily.lilyObjects.LyLyricElement('hel_')
    >>> lle
    <music21.lily.lilyObjects.LyLyricElement hel_>
    >>> print(lle)
    hel_
    ```

[`LyLyricElement`](#music21.lily.lilyObjects.LyLyricElement "music21.lily.lilyObjects.LyLyricElement") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyLyricElement`](#music21.lily.lilyObjects.LyLyricElement "music21.lily.lilyObjects.LyLyricElement") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyLyricElement`](#music21.lily.lilyObjects.LyLyricElement "music21.lily.lilyObjects.LyLyricElement") methods

LyLyricElement.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyLyricElement.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LyLyricMarkup

class music21.lily.lilyObjects.LyLyricMarkup(*lyricMarkupOrIdentifier=None*, *markupTop=None*)[[source]](../_modules/music21/lily/lilyObjects.html#LyLyricMarkup)

[`LyLyricMarkup`](#music21.lily.lilyObjects.LyLyricMarkup "music21.lily.lilyObjects.LyLyricMarkup") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyLyricMarkup`](#music21.lily.lilyObjects.LyLyricMarkup "music21.lily.lilyObjects.LyLyricMarkup") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyLyricMarkup`](#music21.lily.lilyObjects.LyLyricMarkup "music21.lily.lilyObjects.LyLyricMarkup") methods

LyLyricMarkup.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyLyricMarkup.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LyMarkup

class music21.lily.lilyObjects.LyMarkup(*simpleMarkup=None*, *optionalMarkupHeadList=None*)[[source]](../_modules/music21/lily/lilyObjects.html#LyMarkup)

[`LyMarkup`](#music21.lily.lilyObjects.LyMarkup "music21.lily.lilyObjects.LyMarkup") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyMarkup`](#music21.lily.lilyObjects.LyMarkup "music21.lily.lilyObjects.LyMarkup") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyMarkup`](#music21.lily.lilyObjects.LyMarkup "music21.lily.lilyObjects.LyMarkup") methods

LyMarkup.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyMarkup.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LyMarkupBracedList

class music21.lily.lilyObjects.LyMarkupBracedList(*listBody=None*)[[source]](../_modules/music21/lily/lilyObjects.html#LyMarkupBracedList)

[`LyMarkupBracedList`](#music21.lily.lilyObjects.LyMarkupBracedList "music21.lily.lilyObjects.LyMarkupBracedList") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyMarkupBracedList`](#music21.lily.lilyObjects.LyMarkupBracedList "music21.lily.lilyObjects.LyMarkupBracedList") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyMarkupBracedList`](#music21.lily.lilyObjects.LyMarkupBracedList "music21.lily.lilyObjects.LyMarkupBracedList") methods

LyMarkupBracedList.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyMarkupBracedList.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LyMarkupBracedListBody

class music21.lily.lilyObjects.LyMarkupBracedListBody(*markupOrMarkupList=None*)[[source]](../_modules/music21/lily/lilyObjects.html#LyMarkupBracedListBody)

[`LyMarkupBracedListBody`](#music21.lily.lilyObjects.LyMarkupBracedListBody "music21.lily.lilyObjects.LyMarkupBracedListBody") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyMarkupBracedListBody`](#music21.lily.lilyObjects.LyMarkupBracedListBody "music21.lily.lilyObjects.LyMarkupBracedListBody") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyMarkupBracedListBody`](#music21.lily.lilyObjects.LyMarkupBracedListBody "music21.lily.lilyObjects.LyMarkupBracedListBody") methods

LyMarkupBracedListBody.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyMarkupBracedListBody.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LyMarkupComposedList

class music21.lily.lilyObjects.LyMarkupComposedList(*markupHeadList=None*, *markupBracedList=None*)[[source]](../_modules/music21/lily/lilyObjects.html#LyMarkupComposedList)

[`LyMarkupComposedList`](#music21.lily.lilyObjects.LyMarkupComposedList "music21.lily.lilyObjects.LyMarkupComposedList") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyMarkupComposedList`](#music21.lily.lilyObjects.LyMarkupComposedList "music21.lily.lilyObjects.LyMarkupComposedList") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyMarkupComposedList`](#music21.lily.lilyObjects.LyMarkupComposedList "music21.lily.lilyObjects.LyMarkupComposedList") methods

LyMarkupComposedList.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyMarkupComposedList.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LyMarkupList

class music21.lily.lilyObjects.LyMarkupList(*markupIdentifierOrList=None*)[[source]](../_modules/music21/lily/lilyObjects.html#LyMarkupList)

[`LyMarkupList`](#music21.lily.lilyObjects.LyMarkupList "music21.lily.lilyObjects.LyMarkupList") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyMarkupList`](#music21.lily.lilyObjects.LyMarkupList "music21.lily.lilyObjects.LyMarkupList") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyMarkupList`](#music21.lily.lilyObjects.LyMarkupList "music21.lily.lilyObjects.LyMarkupList") methods

LyMarkupList.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyMarkupList.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LyMarkupTop

class music21.lily.lilyObjects.LyMarkupTop(*argument1=None*, *argument2=None*)[[source]](../_modules/music21/lily/lilyObjects.html#LyMarkupTop)

[`LyMarkupTop`](#music21.lily.lilyObjects.LyMarkupTop "music21.lily.lilyObjects.LyMarkupTop") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyMarkupTop`](#music21.lily.lilyObjects.LyMarkupTop "music21.lily.lilyObjects.LyMarkupTop") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyMarkupTop`](#music21.lily.lilyObjects.LyMarkupTop "music21.lily.lilyObjects.LyMarkupTop") methods

LyMarkupTop.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyMarkupTop.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LyMock

class music21.lily.lilyObjects.LyMock[[source]](../_modules/music21/lily/lilyObjects.html#LyMock)
:   A test object for trying various music21 to Lily conversions

[`LyMock`](#music21.lily.lilyObjects.LyMock "music21.lily.lilyObjects.LyMock") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyMock`](#music21.lily.lilyObjects.LyMock "music21.lily.lilyObjects.LyMock") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyMock`](#music21.lily.lilyObjects.LyMock "music21.lily.lilyObjects.LyMock") methods

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") * [`stringOutput()`](#music21.lily.lilyObjects.LyObject.stringOutput "music21.lily.lilyObjects.LyObject.stringOutput") |

## LyModeChangingHead

class music21.lily.lilyObjects.LyModeChangingHead(*hasContext=False*, *mode=None*)[[source]](../_modules/music21/lily/lilyObjects.html#LyModeChangingHead)
:   represents both mode\_changing\_head and mode\_changing\_head\_with\_context

    .hasContext = False
    .mode = [‘note’, ‘drum’, ‘figure’, ‘chord’, ‘lyric’]

    ```python
    >>> l = lily.lilyObjects.LyModeChangingHead(hasContext=True, mode='drum')
    >>> print(l.stringOutput())
    \drummode
    >>> l2 = lily.lilyObjects.LyModeChangingHead(hasContext=False, mode='chord')
    >>> print(l2.stringOutput())
    \chords
    ```

[`LyModeChangingHead`](#music21.lily.lilyObjects.LyModeChangingHead "music21.lily.lilyObjects.LyModeChangingHead") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyModeChangingHead`](#music21.lily.lilyObjects.LyModeChangingHead "music21.lily.lilyObjects.LyModeChangingHead") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyModeChangingHead`](#music21.lily.lilyObjects.LyModeChangingHead "music21.lily.lilyObjects.LyModeChangingHead") methods

LyModeChangingHead.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyModeChangingHead.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LyMultipliedDuration

class music21.lily.lilyObjects.LyMultipliedDuration(*stenoDur=None*, *multiply=None*)[[source]](../_modules/music21/lily/lilyObjects.html#LyMultipliedDuration)
:   represents either a simple LyStenoDuration or a list of things that
    the steno duration should be multiplied by.

    if stenoDur is None then output is None – thus also represents
    optional\_notemode\_duration

[`LyMultipliedDuration`](#music21.lily.lilyObjects.LyMultipliedDuration "music21.lily.lilyObjects.LyMultipliedDuration") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyMultipliedDuration`](#music21.lily.lilyObjects.LyMultipliedDuration "music21.lily.lilyObjects.LyMultipliedDuration") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyMultipliedDuration`](#music21.lily.lilyObjects.LyMultipliedDuration "music21.lily.lilyObjects.LyMultipliedDuration") methods

LyMultipliedDuration.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyMultipliedDuration.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LyMusic

class music21.lily.lilyObjects.LyMusic(*simpleMusic=None*, *compositeMusic=None*)[[source]](../_modules/music21/lily/lilyObjects.html#LyMusic)

[`LyMusic`](#music21.lily.lilyObjects.LyMusic "music21.lily.lilyObjects.LyMusic") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyMusic`](#music21.lily.lilyObjects.LyMusic "music21.lily.lilyObjects.LyMusic") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyMusic`](#music21.lily.lilyObjects.LyMusic "music21.lily.lilyObjects.LyMusic") methods

LyMusic.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyMusic.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LyMusicList

class music21.lily.lilyObjects.LyMusicList(*contents=None*)[[source]](../_modules/music21/lily/lilyObjects.html#LyMusicList)
:   can take any number of LyMusic, LyEmbeddedScm, or LyError objects

[`LyMusicList`](#music21.lily.lilyObjects.LyMusicList "music21.lily.lilyObjects.LyMusicList") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyMusicList`](#music21.lily.lilyObjects.LyMusicList "music21.lily.lilyObjects.LyMusicList") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyMusicList`](#music21.lily.lilyObjects.LyMusicList "music21.lily.lilyObjects.LyMusicList") methods

LyMusicList.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyMusicList.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LyMusicPropertyDef

class music21.lily.lilyObjects.LyMusicPropertyDef(*isOnce=False*, *propertyDef=None*)[[source]](../_modules/music21/lily/lilyObjects.html#LyMusicPropertyDef)

[`LyMusicPropertyDef`](#music21.lily.lilyObjects.LyMusicPropertyDef "music21.lily.lilyObjects.LyMusicPropertyDef") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyMusicPropertyDef`](#music21.lily.lilyObjects.LyMusicPropertyDef "music21.lily.lilyObjects.LyMusicPropertyDef") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyMusicPropertyDef`](#music21.lily.lilyObjects.LyMusicPropertyDef "music21.lily.lilyObjects.LyMusicPropertyDef") methods

LyMusicPropertyDef.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyMusicPropertyDef.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LyNewLyrics

class music21.lily.lilyObjects.LyNewLyrics(*groupedMusicLists=None*)[[source]](../_modules/music21/lily/lilyObjects.html#LyNewLyrics)
:   contains a list of LyGroupedMusicList objects or identifiers

[`LyNewLyrics`](#music21.lily.lilyObjects.LyNewLyrics "music21.lily.lilyObjects.LyNewLyrics") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyNewLyrics`](#music21.lily.lilyObjects.LyNewLyrics "music21.lily.lilyObjects.LyNewLyrics") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyNewLyrics`](#music21.lily.lilyObjects.LyNewLyrics "music21.lily.lilyObjects.LyNewLyrics") methods

LyNewLyrics.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyNewLyrics.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LyNoteChordElement

class music21.lily.lilyObjects.LyNoteChordElement(*chordBody=None*, *optionalNoteModeDuration=None*, *postEvents=None*)[[source]](../_modules/music21/lily/lilyObjects.html#LyNoteChordElement)

[`LyNoteChordElement`](#music21.lily.lilyObjects.LyNoteChordElement "music21.lily.lilyObjects.LyNoteChordElement") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyNoteChordElement`](#music21.lily.lilyObjects.LyNoteChordElement "music21.lily.lilyObjects.LyNoteChordElement") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyNoteChordElement`](#music21.lily.lilyObjects.LyNoteChordElement "music21.lily.lilyObjects.LyNoteChordElement") methods

LyNoteChordElement.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyNoteChordElement.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LyNumberExpression

class music21.lily.lilyObjects.LyNumberExpression(*numberAndSepList=None*)[[source]](../_modules/music21/lily/lilyObjects.html#LyNumberExpression)
:   any list of numbers or LyNumberTerms separated by ‘+’ or ‘-’ objects.

[`LyNumberExpression`](#music21.lily.lilyObjects.LyNumberExpression "music21.lily.lilyObjects.LyNumberExpression") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyNumberExpression`](#music21.lily.lilyObjects.LyNumberExpression "music21.lily.lilyObjects.LyNumberExpression") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyNumberExpression`](#music21.lily.lilyObjects.LyNumberExpression "music21.lily.lilyObjects.LyNumberExpression") methods

LyNumberExpression.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyNumberExpression.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LyNumberTerm

class music21.lily.lilyObjects.LyNumberTerm(*numberAndSepList=None*)[[source]](../_modules/music21/lily/lilyObjects.html#LyNumberTerm)
:   any list of numbers separated by ‘\*’ or ‘/’ strings.

[`LyNumberTerm`](#music21.lily.lilyObjects.LyNumberTerm "music21.lily.lilyObjects.LyNumberTerm") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyNumberTerm`](#music21.lily.lilyObjects.LyNumberTerm "music21.lily.lilyObjects.LyNumberTerm") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyNumberTerm`](#music21.lily.lilyObjects.LyNumberTerm "music21.lily.lilyObjects.LyNumberTerm") methods

LyNumberTerm.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyNumberTerm.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LyObject

class music21.lily.lilyObjects.LyObject[[source]](../_modules/music21/lily/lilyObjects.html#LyObject)
:   LyObject is the base class of all other Lily Objects

    ```python
    >>> lyo = lily.lilyObjects.LyObject()
    >>> lyo.stringOutput()
    ''
    ```

[`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject") bases

* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject") read-only properties

LyObject.newlineIndent

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject") methods

LyObject.ancestorList()[[source]](../_modules/music21/lily/lilyObjects.html#LyObject.ancestorList)
:   returns a list of all unwrapped parent objects for the current object

LyObject.comment(*stringIn: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](../_modules/music21/lily/lilyObjects.html#LyObject.comment)
:   returns a comment that is %{ stringIn.strip() %}

    (Don’t put %} etc. in comments – it will break the system.)

LyObject.encloseCurly(*arg*)[[source]](../_modules/music21/lily/lilyObjects.html#LyObject.encloseCurly)

LyObject.getAncestorByClass(*classObj*, *getAncestorNumber=1*)[[source]](../_modules/music21/lily/lilyObjects.html#LyObject.getAncestorByClass)

LyObject.getFirstNonNoneAttribute(*attributeList*)[[source]](../_modules/music21/lily/lilyObjects.html#LyObject.getFirstNonNoneAttribute)

LyObject.getParent()[[source]](../_modules/music21/lily/lilyObjects.html#LyObject.getParent)

LyObject.newlineSeparateStringOutputIfNotNone(*contents*)[[source]](../_modules/music21/lily/lilyObjects.html#LyObject.newlineSeparateStringOutputIfNotNone)

LyObject.quoteString(*stringIn*)[[source]](../_modules/music21/lily/lilyObjects.html#LyObject.quoteString)
:   returns a string that is quoted with
    internal quotation marks backslash’d out
    and an extra space at the end.

    ```python
    >>> m = lily.lilyObjects.LyObject()
    >>> print(m.quoteString(r'Hello "there"!'))
    "Hello \"there\"!"
    ```

LyObject.setAttributes(*m21Object*)[[source]](../_modules/music21/lily/lilyObjects.html#LyObject.setAttributes)
:   Returns a dictionary and sets self.lilyAttributes to that dictionary, for a m21Object
    of class classLookup using the mapping of self.m21toLy[classLookup]

    ```python
    >>> class Mock(base.Music21Object):
    ...     pass
    >>> m = Mock()
    >>> m.mockAttribute = 32
    >>> m.mockAttribute2 = None
    ```

    ```python
    >>> lm = lily.lilyObjects.LyMock()
    ```

    LyMock (our test class) defines mappings for two classes:
    to LyMock.lilyAttributes:

    ```python
    >>> print(lm.supportedClasses)
    [...'Mock', ...'Mocker']
    ```

    Thus, we can get attributes from the Mock class (see setAttributesFromClassObject):

    ```python
    >>> lilyAttributes = lm.setAttributes(m)
    >>> for x in sorted(lilyAttributes.keys()):
    ...    print(f'{x}: {lilyAttributes[x]}')
    mock-attribute: 32
    mock-attribute-2: None
    ```

    ```python
    >>> lilyAttributes is lm.lilyAttributes
    True
    ```

LyObject.setAttributesFromClassObject(*classLookup*, *m21Object*)[[source]](../_modules/music21/lily/lilyObjects.html#LyObject.setAttributesFromClassObject)
:   Returns a dictionary and sets self.lilyAttributes to that dictionary, for a m21Object
    of class classLookup using the mapping of self.m21toLy[classLookup]

    ```python
    >>> class Mock(base.Music21Object): pass
    >>> m = Mock()
    >>> lm = lily.lilyObjects.LyMock()
    ```

    LyMock (our test class) defines certain mappings from the m21 Mock class
    to LyMock.lilyAttributes:

    ```python
    >>> for x in sorted(lm.m21toLy['Mock'].keys()):
    ...    print(f"{x}: {lm.m21toLy['Mock'][x]}")
    mockAttribute: mock-attribute
    mockAttribute2: mock-attribute-2
    ```

    Some of these attributes have defaults:

    ```python
    >>> for x in sorted(lm.defaultAttributes.keys()):
    ...    print(f'{x}: {lm.defaultAttributes[x]}')
    mockAttribute2: 7
    ```

    ```python
    >>> m.mockAttribute = 'hello'
    >>> lilyAttributes = lm.setAttributesFromClassObject('Mock', m)
    >>> for x in sorted(lilyAttributes.keys()):
    ...    print(f'{x}: {lilyAttributes[x]}')
    mock-attribute: hello
    mock-attribute-2: 7
    ```

    ```python
    >>> lilyAttributes is lm.lilyAttributes
    True
    ```

LyObject.setParent(*parentObject*)[[source]](../_modules/music21/lily/lilyObjects.html#LyObject.setParent)

LyObject.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyObject.stringOutput)

## LyOctaveCheck

class music21.lily.lilyObjects.LyOctaveCheck(*equalOrQuotesOrNone=None*)[[source]](../_modules/music21/lily/lilyObjects.html#LyOctaveCheck)

[`LyOctaveCheck`](#music21.lily.lilyObjects.LyOctaveCheck "music21.lily.lilyObjects.LyOctaveCheck") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyOctaveCheck`](#music21.lily.lilyObjects.LyOctaveCheck "music21.lily.lilyObjects.LyOctaveCheck") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyOctaveCheck`](#music21.lily.lilyObjects.LyOctaveCheck "music21.lily.lilyObjects.LyOctaveCheck") methods

LyOctaveCheck.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyOctaveCheck.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LyOptionalId

class music21.lily.lilyObjects.LyOptionalId(*content=None*)[[source]](../_modules/music21/lily/lilyObjects.html#LyOptionalId)
:   an optional id setting

[`LyOptionalId`](#music21.lily.lilyObjects.LyOptionalId "music21.lily.lilyObjects.LyOptionalId") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyOptionalId`](#music21.lily.lilyObjects.LyOptionalId "music21.lily.lilyObjects.LyOptionalId") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyOptionalId`](#music21.lily.lilyObjects.LyOptionalId "music21.lily.lilyObjects.LyOptionalId") methods

LyOptionalId.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyOptionalId.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LyOptionalRest

class music21.lily.lilyObjects.LyOptionalRest(*rest=False*)[[source]](../_modules/music21/lily/lilyObjects.html#LyOptionalRest)

[`LyOptionalRest`](#music21.lily.lilyObjects.LyOptionalRest "music21.lily.lilyObjects.LyOptionalRest") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyOptionalRest`](#music21.lily.lilyObjects.LyOptionalRest "music21.lily.lilyObjects.LyOptionalRest") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyOptionalRest`](#music21.lily.lilyObjects.LyOptionalRest "music21.lily.lilyObjects.LyOptionalRest") methods

LyOptionalRest.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyOptionalRest.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LyOssiaMusic

class music21.lily.lilyObjects.LyOssiaMusic(*musicList=None*, *startstop=True*)[[source]](../_modules/music21/lily/lilyObjects.html#LyOssiaMusic)
:   represents ossia music.

    Can be tagged with startStaff and stopStaff if startstop is True

[`LyOssiaMusic`](#music21.lily.lilyObjects.LyOssiaMusic "music21.lily.lilyObjects.LyOssiaMusic") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyOssiaMusic`](#music21.lily.lilyObjects.LyOssiaMusic "music21.lily.lilyObjects.LyOssiaMusic") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyOssiaMusic`](#music21.lily.lilyObjects.LyOssiaMusic "music21.lily.lilyObjects.LyOssiaMusic") methods

LyOssiaMusic.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyOssiaMusic.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LyOutputDef

class music21.lily.lilyObjects.LyOutputDef(*outputDefBody=None*)[[source]](../_modules/music21/lily/lilyObjects.html#LyOutputDef)
:   This is an ugly grammar, since it does not close the curly bracket.

[`LyOutputDef`](#music21.lily.lilyObjects.LyOutputDef "music21.lily.lilyObjects.LyOutputDef") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyOutputDef`](#music21.lily.lilyObjects.LyOutputDef "music21.lily.lilyObjects.LyOutputDef") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyOutputDef`](#music21.lily.lilyObjects.LyOutputDef "music21.lily.lilyObjects.LyOutputDef") methods

LyOutputDef.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyOutputDef.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LyOutputDefBody

class music21.lily.lilyObjects.LyOutputDefBody(*outputDefHead=None*, *outputDefIdentifier=None*, *outputDefBody=None*, *assignment=None*, *contextDefSpecBlock=None*, *error=None*)[[source]](../_modules/music21/lily/lilyObjects.html#LyOutputDefBody)
:   output\_def\_body: output\_def\_head\_with\_mode\_switch ‘{’
    :   output\_def\_head\_with\_mode\_switch
        ‘{’
        OUTPUT\_DEF\_IDENTIFIER

        output\_def\_body assignment

        output\_def\_body context\_def\_spec\_block

        output\_def\_body error

[`LyOutputDefBody`](#music21.lily.lilyObjects.LyOutputDefBody "music21.lily.lilyObjects.LyOutputDefBody") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyOutputDefBody`](#music21.lily.lilyObjects.LyOutputDefBody "music21.lily.lilyObjects.LyOutputDefBody") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyOutputDefBody`](#music21.lily.lilyObjects.LyOutputDefBody "music21.lily.lilyObjects.LyOutputDefBody") methods

LyOutputDefBody.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyOutputDefBody.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LyOutputDefHead

class music21.lily.lilyObjects.LyOutputDefHead(*defType=None*)[[source]](../_modules/music21/lily/lilyObjects.html#LyOutputDefHead)
:   defType can be paper, midi, or layout.

    ```python
    >>> lyODH = lily.lilyObjects.LyOutputDefHead()
    >>> lyODH.defType = 'midi'
    >>> print(lyODH.stringOutput())
    \midi
    ```

    According to Appendix C, is the same as LyOutputDefHeadWithModeSwitch

[`LyOutputDefHead`](#music21.lily.lilyObjects.LyOutputDefHead "music21.lily.lilyObjects.LyOutputDefHead") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyOutputDefHead`](#music21.lily.lilyObjects.LyOutputDefHead "music21.lily.lilyObjects.LyOutputDefHead") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyOutputDefHead`](#music21.lily.lilyObjects.LyOutputDefHead "music21.lily.lilyObjects.LyOutputDefHead") methods

LyOutputDefHead.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyOutputDefHead.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LyPaperBlock

class music21.lily.lilyObjects.LyPaperBlock(*outputDef=None*)[[source]](../_modules/music21/lily/lilyObjects.html#LyPaperBlock)

[`LyPaperBlock`](#music21.lily.lilyObjects.LyPaperBlock "music21.lily.lilyObjects.LyPaperBlock") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyPaperBlock`](#music21.lily.lilyObjects.LyPaperBlock "music21.lily.lilyObjects.LyPaperBlock") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyPaperBlock`](#music21.lily.lilyObjects.LyPaperBlock "music21.lily.lilyObjects.LyPaperBlock") methods

LyPaperBlock.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyPaperBlock.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LyPitch

class music21.lily.lilyObjects.LyPitch(*noteNamePitch=None*, *quotes=None*)[[source]](../_modules/music21/lily/lilyObjects.html#LyPitch)
:   represents a pitch name and zero or more sup or sub quotes
    also used for steno\_pitch and steno\_tonic\_pitch

[`LyPitch`](#music21.lily.lilyObjects.LyPitch "music21.lily.lilyObjects.LyPitch") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyPitch`](#music21.lily.lilyObjects.LyPitch "music21.lily.lilyObjects.LyPitch") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyPitch`](#music21.lily.lilyObjects.LyPitch "music21.lily.lilyObjects.LyPitch") methods

LyPitch.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyPitch.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LyPostEvent

class music21.lily.lilyObjects.LyPostEvent(*arg1=None*, *arg2=None*)[[source]](../_modules/music21/lily/lilyObjects.html#LyPostEvent)

[`LyPostEvent`](#music21.lily.lilyObjects.LyPostEvent "music21.lily.lilyObjects.LyPostEvent") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyPostEvent`](#music21.lily.lilyObjects.LyPostEvent "music21.lily.lilyObjects.LyPostEvent") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyPostEvent`](#music21.lily.lilyObjects.LyPostEvent "music21.lily.lilyObjects.LyPostEvent") methods

LyPostEvent.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyPostEvent.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LyPostEvents

class music21.lily.lilyObjects.LyPostEvents(*eventList=None*)[[source]](../_modules/music21/lily/lilyObjects.html#LyPostEvents)

[`LyPostEvents`](#music21.lily.lilyObjects.LyPostEvents "music21.lily.lilyObjects.LyPostEvents") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyPostEvents`](#music21.lily.lilyObjects.LyPostEvents "music21.lily.lilyObjects.LyPostEvents") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyPostEvents`](#music21.lily.lilyObjects.LyPostEvents "music21.lily.lilyObjects.LyPostEvents") methods

LyPostEvents.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyPostEvents.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LyPrefixCompositeMusic

class music21.lily.lilyObjects.LyPrefixCompositeMusic(*type=None*, *genericPrefixMusicScm=None*, *simpleString=None*, *optionalId=None*, *optionalContextMod=None*, *music=None*, *fraction=None*, *repeatedMusic=None*, *pitchAlsoInChords1=None*, *pitchAlsoInChords2=None*, *modeChangingHead=None*, *groupedMusicList=None*, *modeChangingHeadWithContext=None*, *relativeMusic=None*, *reRhythmedMusic=None*)[[source]](../_modules/music21/lily/lilyObjects.html#LyPrefixCompositeMusic)
:   type must be specified. Should be one of:

    scheme, context, new, times, repeated, transpose,
    modeChanging, modeChangingWith, relative,
    rhythmed

    prefix\_composite\_music: generic\_prefix\_music\_scm
    :   “context”
        simple\_string
        optional\_id
        optional\_context\_mod
        music

        “new”
        simple\_string
        optional\_id
        optional\_context\_mod
        music

        “times” fraction music

        repeated\_music

        “transpose”
        pitch\_also\_in\_chords
        pitch\_also\_in\_chords
        music

        mode\_changing\_head grouped\_music\_list

        mode\_changing\_head\_with\_context
        optional\_context\_mod
        grouped\_music\_list

        relative\_music

        re\_rhythmed\_music

[`LyPrefixCompositeMusic`](#music21.lily.lilyObjects.LyPrefixCompositeMusic "music21.lily.lilyObjects.LyPrefixCompositeMusic") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyPrefixCompositeMusic`](#music21.lily.lilyObjects.LyPrefixCompositeMusic "music21.lily.lilyObjects.LyPrefixCompositeMusic") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyPrefixCompositeMusic`](#music21.lily.lilyObjects.LyPrefixCompositeMusic "music21.lily.lilyObjects.LyPrefixCompositeMusic") methods

LyPrefixCompositeMusic.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyPrefixCompositeMusic.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LyPropertyOperation

class music21.lily.lilyObjects.LyPropertyOperation(*mode=None*, *value1=None*, *value2=None*, *value3=None*)[[source]](../_modules/music21/lily/lilyObjects.html#LyPropertyOperation)
:   Represents:

    > property\_operation: STRING ‘=’ scalar
    > :   “unset” simple\_string
    >
    >     “override” simple\_string property\_path ‘=’ scalar
    >
    >     “revert” simple\_string embedded\_scm

    mandatory mode in [‘set’, ‘unset’, ‘override’, ‘revert’]

    also represents simple\_music\_property\_def which has the same forms

    ```python
    >>> lpo = lily.lilyObjects.LyPropertyOperation('unset', 'simple')
    >>> str(lpo)
    '\\unset simple '
    ```

    ```python
    >>> lpo = lily.lilyObjects.LyPropertyOperation('override', 'simple', 'x', 'y')
    >>> str(lpo)
    '\\override simple.x = y '
    ```

    ```python
    >>> lpo = lily.lilyObjects.LyPropertyOperation('revert', 'x', 'y')
    >>> str(lpo)
    '\\revert x.y '
    ```

    TODO: should set be given?

[`LyPropertyOperation`](#music21.lily.lilyObjects.LyPropertyOperation "music21.lily.lilyObjects.LyPropertyOperation") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyPropertyOperation`](#music21.lily.lilyObjects.LyPropertyOperation "music21.lily.lilyObjects.LyPropertyOperation") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyPropertyOperation`](#music21.lily.lilyObjects.LyPropertyOperation "music21.lily.lilyObjects.LyPropertyOperation") methods

LyPropertyOperation.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyPropertyOperation.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LyPropertyPath

class music21.lily.lilyObjects.LyPropertyPath(*embeddedScheme=None*)[[source]](../_modules/music21/lily/lilyObjects.html#LyPropertyPath)
:   represents both property\_path and property\_path\_revved

    has one or more of LyEmbeddedScm objects

[`LyPropertyPath`](#music21.lily.lilyObjects.LyPropertyPath "music21.lily.lilyObjects.LyPropertyPath") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyPropertyPath`](#music21.lily.lilyObjects.LyPropertyPath "music21.lily.lilyObjects.LyPropertyPath") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyPropertyPath`](#music21.lily.lilyObjects.LyPropertyPath "music21.lily.lilyObjects.LyPropertyPath") methods

LyPropertyPath.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyPropertyPath.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LyReRhythmedMusic

class music21.lily.lilyObjects.LyReRhythmedMusic(*groupedMusic=None*, *newLyrics=None*)[[source]](../_modules/music21/lily/lilyObjects.html#LyReRhythmedMusic)

[`LyReRhythmedMusic`](#music21.lily.lilyObjects.LyReRhythmedMusic "music21.lily.lilyObjects.LyReRhythmedMusic") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyReRhythmedMusic`](#music21.lily.lilyObjects.LyReRhythmedMusic "music21.lily.lilyObjects.LyReRhythmedMusic") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyReRhythmedMusic`](#music21.lily.lilyObjects.LyReRhythmedMusic "music21.lily.lilyObjects.LyReRhythmedMusic") methods

LyReRhythmedMusic.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyReRhythmedMusic.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LyRelativeMusic

class music21.lily.lilyObjects.LyRelativeMusic(*content=None*)[[source]](../_modules/music21/lily/lilyObjects.html#LyRelativeMusic)
:   relative music

[`LyRelativeMusic`](#music21.lily.lilyObjects.LyRelativeMusic "music21.lily.lilyObjects.LyRelativeMusic") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyRelativeMusic`](#music21.lily.lilyObjects.LyRelativeMusic "music21.lily.lilyObjects.LyRelativeMusic") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyRelativeMusic`](#music21.lily.lilyObjects.LyRelativeMusic "music21.lily.lilyObjects.LyRelativeMusic") methods

LyRelativeMusic.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyRelativeMusic.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LyRepeatedMusic

class music21.lily.lilyObjects.LyRepeatedMusic(*simpleString=None*, *unsignedNumber=None*, *music=None*, *alternativeMusic=None*)[[source]](../_modules/music21/lily/lilyObjects.html#LyRepeatedMusic)

[`LyRepeatedMusic`](#music21.lily.lilyObjects.LyRepeatedMusic "music21.lily.lilyObjects.LyRepeatedMusic") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyRepeatedMusic`](#music21.lily.lilyObjects.LyRepeatedMusic "music21.lily.lilyObjects.LyRepeatedMusic") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyRepeatedMusic`](#music21.lily.lilyObjects.LyRepeatedMusic "music21.lily.lilyObjects.LyRepeatedMusic") methods

LyRepeatedMusic.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyRepeatedMusic.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LySchemeFunction

class music21.lily.lilyObjects.LySchemeFunction(*content=None*)[[source]](../_modules/music21/lily/lilyObjects.html#LySchemeFunction)
:   Unsupported for now, represents all of:

    ```python
    function_scm_argument: embedded_scm
      116                      | simple_string

      117 function_arglist_music_last: EXPECT_MUSIC function_arglist music

      118 function_arglist_nonmusic_last: EXPECT_MARKUP
                                            function_arglist
                                            full_markup
      119                               | EXPECT_MARKUP
                                            function_arglist
                                            simple_string
      120                               | EXPECT_SCM
                                            function_arglist
                                            function_scm_argument

      121 function_arglist_nonmusic: EXPECT_NO_MORE_ARGS
      122                          | EXPECT_MARKUP
                                       function_arglist_nonmusic
                                       full_markup
      123                          | EXPECT_MARKUP
                                       function_arglist_nonmusic
                                       simple_string
      124                          | EXPECT_SCM
                                       function_arglist_nonmusic
                                       function_scm_argument

      125 function_arglist: EXPECT_NO_MORE_ARGS
      126                 | function_arglist_music_last
      127                 | function_arglist_nonmusic_last

      128 generic_prefix_music_scm: MUSIC_FUNCTION function_arglist
    ```

    We have usually been using LyEmbeddedScm for this

[`LySchemeFunction`](#music21.lily.lilyObjects.LySchemeFunction "music21.lily.lilyObjects.LySchemeFunction") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LySchemeFunction`](#music21.lily.lilyObjects.LySchemeFunction "music21.lily.lilyObjects.LySchemeFunction") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LySchemeFunction`](#music21.lily.lilyObjects.LySchemeFunction "music21.lily.lilyObjects.LySchemeFunction") methods

LySchemeFunction.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LySchemeFunction.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LyScoreBlock

class music21.lily.lilyObjects.LyScoreBlock(*scoreBody=None*)[[source]](../_modules/music21/lily/lilyObjects.html#LyScoreBlock)
:   represents the container for a score ( score { … } )

    with all the real stuff being in self.scoreBody

    ```python
    >>> lyScoreBlock = lily.lilyObjects.LyScoreBlock(scoreBody='hello')
    >>> print(lyScoreBlock)
    \score { hello }
    ```

[`LyScoreBlock`](#music21.lily.lilyObjects.LyScoreBlock "music21.lily.lilyObjects.LyScoreBlock") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyScoreBlock`](#music21.lily.lilyObjects.LyScoreBlock "music21.lily.lilyObjects.LyScoreBlock") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyScoreBlock`](#music21.lily.lilyObjects.LyScoreBlock "music21.lily.lilyObjects.LyScoreBlock") methods

LyScoreBlock.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyScoreBlock.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LyScoreBody

class music21.lily.lilyObjects.LyScoreBody(*music=None*, *scoreIdentifier=None*, *scoreBody=None*, *lilypondHeader=None*, *outputDef=None*, *error=None*)[[source]](../_modules/music21/lily/lilyObjects.html#LyScoreBody)
:   represents the contents of a score { contents }
    block

    can take one of the following attributes:
    music, scoreIdentifier, scoreBody, lilypondHeader, outputDef, error

    ```python
    >>> lsb = lily.lilyObjects.LyScoreBody(scoreIdentifier='score')
    >>> str(lsb)
    'score'
    ```

[`LyScoreBody`](#music21.lily.lilyObjects.LyScoreBody "music21.lily.lilyObjects.LyScoreBody") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyScoreBody`](#music21.lily.lilyObjects.LyScoreBody "music21.lily.lilyObjects.LyScoreBody") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyScoreBody`](#music21.lily.lilyObjects.LyScoreBody "music21.lily.lilyObjects.LyScoreBody") methods

LyScoreBody.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyScoreBody.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LyScriptAbbreviation

class music21.lily.lilyObjects.LyScriptAbbreviation(*value=None*)[[source]](../_modules/music21/lily/lilyObjects.html#LyScriptAbbreviation)
:   Holds a script abbreviation (for articulations etc.), one of:

    ```python
    ^ + - | > . _
    ```

[`LyScriptAbbreviation`](#music21.lily.lilyObjects.LyScriptAbbreviation "music21.lily.lilyObjects.LyScriptAbbreviation") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyScriptAbbreviation`](#music21.lily.lilyObjects.LyScriptAbbreviation "music21.lily.lilyObjects.LyScriptAbbreviation") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyScriptAbbreviation`](#music21.lily.lilyObjects.LyScriptAbbreviation "music21.lily.lilyObjects.LyScriptAbbreviation") methods

LyScriptAbbreviation.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyScriptAbbreviation.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LyScriptDir

class music21.lily.lilyObjects.LyScriptDir(*value=None*)[[source]](../_modules/music21/lily/lilyObjects.html#LyScriptDir)
:   Holds a script direction abbreviation (above below etc), one of:

    ```python
    _ ^ -
    ```

[`LyScriptDir`](#music21.lily.lilyObjects.LyScriptDir "music21.lily.lilyObjects.LyScriptDir") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyScriptDir`](#music21.lily.lilyObjects.LyScriptDir "music21.lily.lilyObjects.LyScriptDir") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyScriptDir`](#music21.lily.lilyObjects.LyScriptDir "music21.lily.lilyObjects.LyScriptDir") methods

LyScriptDir.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyScriptDir.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LySequentialMusic

class music21.lily.lilyObjects.LySequentialMusic(*musicList=None*, *displayTag=False*, *beforeMatter=None*)[[source]](../_modules/music21/lily/lilyObjects.html#LySequentialMusic)
:   represents sequential music.

    Can be explicitly tagged with “sequential” if displayTag is True

[`LySequentialMusic`](#music21.lily.lilyObjects.LySequentialMusic "music21.lily.lilyObjects.LySequentialMusic") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LySequentialMusic`](#music21.lily.lilyObjects.LySequentialMusic "music21.lily.lilyObjects.LySequentialMusic") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LySequentialMusic`](#music21.lily.lilyObjects.LySequentialMusic "music21.lily.lilyObjects.LySequentialMusic") methods

LySequentialMusic.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LySequentialMusic.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LySimpleElement

class music21.lily.lilyObjects.LySimpleElement(*parts=None*)[[source]](../_modules/music21/lily/lilyObjects.html#LySimpleElement)
:   A single note, lyric element, drum pitch or hidden rest:

    ```python
    simple_element: pitch
                    exclamations (a string of zero or more ! marks)
                    questions (a string of zero or more ? marks)
                    octave_check
                    optional_notemode_duration
                    optional_rest
                | DRUM_PITCH optional_notemode_duration
                | RESTNAME optional_notemode_duration
                | lyric_element optional_notemode_duration
    ```

[`LySimpleElement`](#music21.lily.lilyObjects.LySimpleElement "music21.lily.lilyObjects.LySimpleElement") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LySimpleElement`](#music21.lily.lilyObjects.LySimpleElement "music21.lily.lilyObjects.LySimpleElement") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LySimpleElement`](#music21.lily.lilyObjects.LySimpleElement "music21.lily.lilyObjects.LySimpleElement") methods

LySimpleElement.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LySimpleElement.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LySimpleMarkup

class music21.lily.lilyObjects.LySimpleMarkup(*simpleType='string'*, *argument1=None*, *argument2=None*)[[source]](../_modules/music21/lily/lilyObjects.html#LySimpleMarkup)
:   simpleType can be ‘string’ (or markup identifier or lyric markup identifier, etc.) or
    ‘score-body’ or ‘markup-function’

    takes 1 required arg, 2nd for markup\_function

[`LySimpleMarkup`](#music21.lily.lilyObjects.LySimpleMarkup "music21.lily.lilyObjects.LySimpleMarkup") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LySimpleMarkup`](#music21.lily.lilyObjects.LySimpleMarkup "music21.lily.lilyObjects.LySimpleMarkup") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LySimpleMarkup`](#music21.lily.lilyObjects.LySimpleMarkup "music21.lily.lilyObjects.LySimpleMarkup") methods

LySimpleMarkup.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LySimpleMarkup.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LySimpleMusic

class music21.lily.lilyObjects.LySimpleMusic(*eventChord=None*, *musicIdentifier=None*, *musicPropertyDef=None*, *contextChange=None*)[[source]](../_modules/music21/lily/lilyObjects.html#LySimpleMusic)

[`LySimpleMusic`](#music21.lily.lilyObjects.LySimpleMusic "music21.lily.lilyObjects.LySimpleMusic") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LySimpleMusic`](#music21.lily.lilyObjects.LySimpleMusic "music21.lily.lilyObjects.LySimpleMusic") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LySimpleMusic`](#music21.lily.lilyObjects.LySimpleMusic "music21.lily.lilyObjects.LySimpleMusic") methods

LySimpleMusic.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LySimpleMusic.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LySimultaneousMusic

class music21.lily.lilyObjects.LySimultaneousMusic(*musicList=None*, *displayTag=False*)[[source]](../_modules/music21/lily/lilyObjects.html#LySimultaneousMusic)
:   represents simultaneous music.

    Can be explicitly tagged with ‘simultaneous’ if displayTag is True
    otherwise encloses in double angle brackets

[`LySimultaneousMusic`](#music21.lily.lilyObjects.LySimultaneousMusic "music21.lily.lilyObjects.LySimultaneousMusic") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LySimultaneousMusic`](#music21.lily.lilyObjects.LySimultaneousMusic "music21.lily.lilyObjects.LySimultaneousMusic") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LySimultaneousMusic`](#music21.lily.lilyObjects.LySimultaneousMusic "music21.lily.lilyObjects.LySimultaneousMusic") methods

LySimultaneousMusic.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LySimultaneousMusic.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LyStenoDuration

class music21.lily.lilyObjects.LyStenoDuration(*durationNumber=None*, *numDots=0*)[[source]](../_modules/music21/lily/lilyObjects.html#LyStenoDuration)
:   the main thing that we think of as non-tuplet duration.

    a duration number followed by one or more dots

    ```python
    >>> lsd = lily.lilyObjects.LyStenoDuration('2', 2)
    >>> print(lsd)
    2..
    ```

[`LyStenoDuration`](#music21.lily.lilyObjects.LyStenoDuration "music21.lily.lilyObjects.LyStenoDuration") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyStenoDuration`](#music21.lily.lilyObjects.LyStenoDuration "music21.lily.lilyObjects.LyStenoDuration") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyStenoDuration`](#music21.lily.lilyObjects.LyStenoDuration "music21.lily.lilyObjects.LyStenoDuration") methods

LyStenoDuration.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyStenoDuration.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LyTempoEvent

class music21.lily.lilyObjects.LyTempoEvent(*tempoRange=None*, *stenoDuration=None*, *scalar=None*)[[source]](../_modules/music21/lily/lilyObjects.html#LyTempoEvent)
:   tempo\_event: “tempo” steno\_duration ‘=’ tempo\_range
    :   “tempo” scalar steno\_duration ‘=’ tempo\_range

        “tempo” scalar

    ```python
    >>> lte = lily.lilyObjects.LyTempoEvent(scalar='40')
    >>> str(lte)
    '\\tempo 40'
    ```

    More complex:

    ```python
    >>> steno = lily.lilyObjects.LyStenoDuration('quarter')
    >>> tempoRange = lily.lilyObjects.LyTempoRange(70, 100)
    >>> lte = lily.lilyObjects.LyTempoEvent(tempoRange=tempoRange, stenoDuration=steno)
    >>> str(lte)
    '\\tempo quarter  = 70~100 '
    ```

    ```python
    >>> lte.scalar = 85
    >>> str(lte)
    '\\tempo 85 quarter  = 70~100 '
    ```

[`LyTempoEvent`](#music21.lily.lilyObjects.LyTempoEvent "music21.lily.lilyObjects.LyTempoEvent") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyTempoEvent`](#music21.lily.lilyObjects.LyTempoEvent "music21.lily.lilyObjects.LyTempoEvent") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyTempoEvent`](#music21.lily.lilyObjects.LyTempoEvent "music21.lily.lilyObjects.LyTempoEvent") methods

LyTempoEvent.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyTempoEvent.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LyTempoRange

class music21.lily.lilyObjects.LyTempoRange(*lowestOrOnlyTempo=None*, *highestTempoOrNone=None*)[[source]](../_modules/music21/lily/lilyObjects.html#LyTempoRange)
:   defines either a single tempo or a range

[`LyTempoRange`](#music21.lily.lilyObjects.LyTempoRange "music21.lily.lilyObjects.LyTempoRange") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyTempoRange`](#music21.lily.lilyObjects.LyTempoRange "music21.lily.lilyObjects.LyTempoRange") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyTempoRange`](#music21.lily.lilyObjects.LyTempoRange "music21.lily.lilyObjects.LyTempoRange") methods

LyTempoRange.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyTempoRange.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LyTopLevelExpression

class music21.lily.lilyObjects.LyTopLevelExpression(*lilypondHeader=None*, *bookBlock=None*, *bookPartBlock=None*, *scoreBlock=None*, *compositeMusic=None*, *fullMarkup=None*, *fullMarkupList=None*, *outputDef=None*)[[source]](../_modules/music21/lily/lilyObjects.html#LyTopLevelExpression)
:   can contain one of:

    > lilypondHeader
    > bookBlock
    > bookPartBlock
    > scoreBlock
    > compositeMusic
    > fullMarkup
    > fullMarkupList
    > outputDef

    ```python
    >>> bookBlock = lily.lilyObjects.LyBookBlock()
    >>> lyTopLevel = lily.lilyObjects.LyTopLevelExpression(bookBlock=bookBlock)
    >>> str(lyTopLevel)
    '\\book  { } '
    ```

[`LyTopLevelExpression`](#music21.lily.lilyObjects.LyTopLevelExpression "music21.lily.lilyObjects.LyTopLevelExpression") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyTopLevelExpression`](#music21.lily.lilyObjects.LyTopLevelExpression "music21.lily.lilyObjects.LyTopLevelExpression") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyTopLevelExpression`](#music21.lily.lilyObjects.LyTopLevelExpression "music21.lily.lilyObjects.LyTopLevelExpression") methods

LyTopLevelExpression.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyTopLevelExpression.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |

## LyTremoloType

class music21.lily.lilyObjects.LyTremoloType(*tremTypeOrNone=None*)[[source]](../_modules/music21/lily/lilyObjects.html#LyTremoloType)

[`LyTremoloType`](#music21.lily.lilyObjects.LyTremoloType "music21.lily.lilyObjects.LyTremoloType") bases

* [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`LyTremoloType`](#music21.lily.lilyObjects.LyTremoloType "music21.lily.lilyObjects.LyTremoloType") read-only properties

Read-only properties inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`newlineIndent`](#music21.lily.lilyObjects.LyObject.newlineIndent "music21.lily.lilyObjects.LyObject.newlineIndent") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`LyTremoloType`](#music21.lily.lilyObjects.LyTremoloType "music21.lily.lilyObjects.LyTremoloType") methods

LyTremoloType.stringOutput()[[source]](../_modules/music21/lily/lilyObjects.html#LyTremoloType.stringOutput)

Methods inherited from [`LyObject`](#music21.lily.lilyObjects.LyObject "music21.lily.lilyObjects.LyObject"):

|  |  |  |
| --- | --- | --- |
| * [`ancestorList()`](#music21.lily.lilyObjects.LyObject.ancestorList "music21.lily.lilyObjects.LyObject.ancestorList") * [`comment()`](#music21.lily.lilyObjects.LyObject.comment "music21.lily.lilyObjects.LyObject.comment") * [`encloseCurly()`](#music21.lily.lilyObjects.LyObject.encloseCurly "music21.lily.lilyObjects.LyObject.encloseCurly") * [`getAncestorByClass()`](#music21.lily.lilyObjects.LyObject.getAncestorByClass "music21.lily.lilyObjects.LyObject.getAncestorByClass") | * [`getFirstNonNoneAttribute()`](#music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute "music21.lily.lilyObjects.LyObject.getFirstNonNoneAttribute") * [`getParent()`](#music21.lily.lilyObjects.LyObject.getParent "music21.lily.lilyObjects.LyObject.getParent") * [`newlineSeparateStringOutputIfNotNone()`](#music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone "music21.lily.lilyObjects.LyObject.newlineSeparateStringOutputIfNotNone") * [`quoteString()`](#music21.lily.lilyObjects.LyObject.quoteString "music21.lily.lilyObjects.LyObject.quoteString") | * [`setAttributes()`](#music21.lily.lilyObjects.LyObject.setAttributes "music21.lily.lilyObjects.LyObject.setAttributes") * [`setAttributesFromClassObject()`](#music21.lily.lilyObjects.LyObject.setAttributesFromClassObject "music21.lily.lilyObjects.LyObject.setAttributesFromClassObject") * [`setParent()`](#music21.lily.lilyObjects.LyObject.setParent "music21.lily.lilyObjects.LyObject.setParent") |
