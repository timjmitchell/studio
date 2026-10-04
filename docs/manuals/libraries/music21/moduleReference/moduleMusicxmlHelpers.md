Source: https://music21.org/music21docs/moduleReference/moduleMusicxmlHelpers.html

# music21.musicxml.helpers

## Functions

music21.musicxml.helpers.dump(*obj*)[[source]](../_modules/music21/musicxml/helpers.html#dump)
:   wrapper around xml.etree.ElementTree that prints a string
    in every case and indents tags and sorts attributes. (Prints, does not return)

    ```python
    >>> from music21.musicxml.helpers import dump
    >>> from xml.etree.ElementTree import Element
    >>> e = Element('accidental')
    ```

    ```python
    >>> dump(e)
    <accidental />
    ```

    ```python
    >>> e.text = '∆'
    >>> e.text == '∆'
    True
    >>> dump(e)
    <accidental>∆</accidental>
    ```

music21.musicxml.helpers.dumpString(*obj*, *\**, *noCopy=False*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](../_modules/music21/musicxml/helpers.html#dumpString)
:   wrapper around xml.etree.ElementTree that returns a string
    in every case and indents tags and sorts attributes.

    ```python
    >>> from music21.musicxml.m21ToXml import Element
    >>> from music21.musicxml.helpers import dumpString
    >>> e = Element('accidental')
    ```

    ```python
    >>> dumpString(e)
    '<accidental />'
    ```

    ```python
    >>> e.text = '∆'
    >>> e.text == '∆'
    True
    >>> dumpString(e)
    '<accidental>∆</accidental>'
    ```

music21.musicxml.helpers.indent(*elem*, *level=0*)[[source]](../_modules/music21/musicxml/helpers.html#indent)
:   helper method, indent an element in place:

music21.musicxml.helpers.insertBeforeElements(*root*, *insert*, *tagList=None*)[[source]](../_modules/music21/musicxml/helpers.html#insertBeforeElements)
:   Insert element insert into element root at the earliest position
    of any instance of a child tag given in tagList. Append the element
    if tagList is None.

    ```python
    >>> from xml.etree.ElementTree import fromstring as El
    >>> from music21.musicxml.helpers import insertBeforeElements, dump
    >>> root = El('<clef><sign>G</sign><line>4</line></clef>')
    >>> insert = El('<foo/>')
    ```

    ```python
    >>> insertBeforeElements(root, insert, tagList=['line'])
    >>> dump(root)
    <clef>
        <sign>G</sign>
        <foo />
        <line>4</line>
    </clef>
    ```

    Now insert another element at the end by not specifying a tag list:

    ```python
    >>> insert2 = El('<bar/>')
    >>> insertBeforeElements(root, insert2)
    >>> dump(root)
    <clef>
        <sign>G</sign>
        <foo />
        <line>4</line>
        <bar />
    </clef>
    ```

music21.musicxml.helpers.isFullMeasureRest(*r: [music21.note.Rest](moduleNote.html#music21.note.Rest "music21.note.Rest")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/musicxml/helpers.html#isFullMeasureRest)

music21.musicxml.helpers.measureNumberComesBefore(*mNum1: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *mNum2: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/musicxml/helpers.html#measureNumberComesBefore)
:   Determine whether measureNumber1 strictly precedes
    measureNumber2 given that they could involve suffixes.
    Equal values return False.

    ```python
    >>> from music21.musicxml.helpers import measureNumberComesBefore
    >>> measureNumberComesBefore('23', '24')
    True
    >>> measureNumberComesBefore('23', '23')
    False
    >>> measureNumberComesBefore('23', '23a')
    True
    >>> measureNumberComesBefore('23a', '23b')
    True
    >>> measureNumberComesBefore('23b', '23a')
    False
    >>> measureNumberComesBefore('23b', '24a')
    True
    >>> measureNumberComesBefore('23b', '23b')
    False
    ```

music21.musicxml.helpers.setM21AttributeFromAttribute(*m21El: t.Any*, *xmlEl: ET.Element*, *xmlAttributeName: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *attributeName: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *transform: Callable[[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")], t.Any] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/musicxml/helpers.html#setM21AttributeFromAttribute)
:   If xmlEl has at least one element of tag==tag with some text. If
    it does, set the attribute either with the same name (with “foo-bar” changed to
    “fooBar”) or with attributeName to the text contents.

    Pass a function or lambda function as transform to transform the value before setting it

    ```python
    >>> from xml.etree.ElementTree import fromstring as El
    >>> e = El('<page-layout new-page="yes" page-number="4" />')
    ```

    ```python
    >>> setb = musicxml.helpers.setM21AttributeFromAttribute
    >>> pl = layout.PageLayout()
    >>> setb(pl, e, 'page-number')
    >>> pl.pageNumber
    '4'
    ```

    ```python
    >>> setb(pl, e, 'new-page', 'isNew')
    >>> pl.isNew
    'yes'
    ```

    Transform the pageNumber value to an int.

    ```python
    >>> setb(pl, e, 'page-number', transform=int)
    >>> pl.pageNumber
    4
    ```

    More complex:

    ```python
    >>> convBool = musicxml.xmlObjects.yesNoToBoolean
    >>> setb(pl, e, 'new-page', 'isNew', transform=convBool)
    >>> pl.isNew
    True
    ```

music21.musicxml.helpers.setXMLAttributeFromAttribute(*m21El: t.Any*, *xmlEl: ET.Element*, *xmlAttributeName: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *attributeName: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *transform: Callable[[t.Any], t.Any] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](../_modules/music21/musicxml/helpers.html#setXMLAttributeFromAttribute)
:   If m21El has at least one element of tag==tag with some text. If
    it does, set the attribute either with the same name (with “foo-bar” changed to
    “fooBar”) or with attributeName to the text contents.

    Pass a function or lambda function as transform to transform the value before setting it

    ```python
    >>> from xml.etree.ElementTree import fromstring as El
    >>> e = El('<page-layout/>')
    ```

    ```python
    >>> setb = musicxml.helpers.setXMLAttributeFromAttribute
    >>> pl = layout.PageLayout()
    >>> pl.pageNumber = 4
    >>> pl.isNew = True
    ```

    ```python
    >>> setb(pl, e, 'page-number')
    >>> e.get('page-number')
    '4'
    ```

    ```python
    >>> XB = musicxml.m21ToXml.XMLExporterBase()
    >>> XB.dump(e)
    <page-layout page-number="4" />
    ```

    ```python
    >>> setb(pl, e, 'new-page', 'isNew')
    >>> e.get('new-page')
    'True'
    ```

    Transform the isNew value to ‘yes’.

    ```python
    >>> convBool = musicxml.xmlObjects.booleanToYesNo
    >>> setb(pl, e, 'new-page', 'isNew', transform=convBool)
    >>> e.get('new-page')
    'yes'
    ```

music21.musicxml.helpers.synchronizeIdsToM21(*element: ET.Element*, *m21Object: [Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")*)[[source]](../_modules/music21/musicxml/helpers.html#synchronizeIdsToM21)
:   MusicXML 3.1 defines the id attribute
    (%optional-unique-id)
    on many elements which is perfect for setting as .id on
    a music21 element.

    <fermata id=”hello”><id>bye</id></fermata>

    ```python
    >>> from xml.etree.ElementTree import fromstring as El
    >>> e = El('<fermata id="fermata1"/>')
    >>> f = expressions.Fermata()
    >>> musicxml.helpers.synchronizeIdsToM21(e, f)
    >>> f.id
    'fermata1'
    ```

    Does not change the id if the id is not specified:

    ```python
    >>> e = El('<fermata />')
    >>> f = expressions.Fermata()
    >>> f.id = 'doNotOverwrite'
    >>> musicxml.helpers.synchronizeIdsToM21(e, f)
    >>> f.id
    'doNotOverwrite'
    ```

music21.musicxml.helpers.synchronizeIdsToXML(*element: ET.Element*, *m21Object: [prebase.ProtoM21Object](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/musicxml/helpers.html#synchronizeIdsToXML)
:   MusicXML 3.1 defines the id attribute (entity: %optional-unique-id)
    on many elements which is perfect for getting from .id on
    a music21 element.

    ```python
    >>> from xml.etree.ElementTree import fromstring as El
    >>> e = El('<fermata />')
    >>> f = expressions.Fermata()
    >>> f.id = 'fermata1'
    >>> musicxml.helpers.synchronizeIdsToXML(e, f)
    >>> e.get('id')
    'fermata1'
    ```

    Does not set attr: id if el.id is not valid or default:

    ```python
    >>> e = El('<fermata />')
    >>> f = expressions.Fermata()
    >>> musicxml.helpers.synchronizeIdsToXML(e, f)
    >>> e.get('id', None) is None
    True
    >>> f.id = '123456'  # invalid for MusicXML id
    >>> musicxml.helpers.synchronizeIdsToXML(e, f)
    >>> e.get('id', None) is None
    True
    ```

    None can be passed in instead of a m21object.

    ```python
    >>> e = El('<fermata />')
    >>> musicxml.helpers.synchronizeIdsToXML(e, None)
    >>> e.get('id', 'no idea')
    'no idea'
    ```
