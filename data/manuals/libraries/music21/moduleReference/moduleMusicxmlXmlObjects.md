Source: https://music21.org/music21docs/moduleReference/moduleMusicxmlXmlObjects.html

# music21.musicxml.xmlObjects

## Functions

music21.musicxml.xmlObjects.booleanToYesNo(*value*)[[source]](../_modules/music21/musicxml/xmlObjects.html#booleanToYesNo)
:   Convert a True, False bool to ‘yes’ or ‘no’

    ```python
    >>> musicxml.xmlObjects.booleanToYesNo(True)
    'yes'
    >>> musicxml.xmlObjects.booleanToYesNo(False)
    'no'
    ```

    anything that evaluates to True becomes ‘yes’

    ```python
    >>> musicxml.xmlObjects.booleanToYesNo(5)
    'yes'
    ```

music21.musicxml.xmlObjects.fractionToPercent(*value*)[[source]](../_modules/music21/musicxml/xmlObjects.html#fractionToPercent)
:   Turns a fraction into a string percent

    ```python
    >>> musicxml.xmlObjects.fractionToPercent(0.25)
    '25'
    ```

    Only does whole numbers for now:

    ```python
    >>> musicxml.xmlObjects.fractionToPercent(0.251)
    '25'
    ```

music21.musicxml.xmlObjects.isValidXSDID(*text*)[[source]](../_modules/music21/musicxml/xmlObjects.html#isValidXSDID)
:   Returns True or False if text is a valid xsd:id, that is, an NCName

    From <http://www.datypic.com/sc/xsd/t-xsd_NCName.html>:

    > The type xsd:NCName represents an XML non-colonized name,
    > which is simply a name that does not contain colons. An xsd:NCName value must
    > start with either a letter or underscore (\_) and may contain only letters,
    > digits, underscores (\_), hyphens (-), and periods (.). This is equivalent
    > to the Name type, except that colons are not permitted.

    ```python
    >>> musicxml.xmlObjects.isValidXSDID('hel_lo')
    True
    ```

    Names cannot begin with digits:

    ```python
    >>> musicxml.xmlObjects.isValidXSDID('4sad')
    False
    ```

    Names must be strings:

    ```python
    >>> musicxml.xmlObjects.isValidXSDID(12345)
    False
    ```

music21.musicxml.xmlObjects.yesNoToBoolean(*value*)[[source]](../_modules/music21/musicxml/xmlObjects.html#yesNoToBoolean)
