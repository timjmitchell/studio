Source: https://music21.org/music21docs/moduleReference/moduleCommonStringTools.html

# music21.common.stringTools

Tools for working with strings

## ParenthesesMatch

class music21.common.stringTools.ParenthesesMatch(*start: 'int'*, *end: 'int'*, *text: 'str'*, *nested: 'list[ParenthesesMatch]'*)[[source]](../_modules/music21/common/stringTools.html#ParenthesesMatch)

[`ParenthesesMatch`](#music21.common.stringTools.ParenthesesMatch "music21.common.stringTools.ParenthesesMatch") methods

ParenthesesMatch.\_\_eq\_\_(*other*)
:   Return self==value.

## Functions

music21.common.stringTools.camelCaseToHyphen(*usrStr: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *replacement: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = '-'*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](../_modules/music21/common/stringTools.html#camelCaseToHyphen)
:   Given a camel-cased string, or a mixture of numbers and characters,
    create a space separated string.

    The replacement can be specified to be something besides a hyphen, but only
    a single character and not (for internal reasons) an uppercase character.

    code from <https://stackoverflow.com/questions/1175208/elegant-python-function-to-convert-camelcase-to-snake-case>

    ```python
    >>> common.camelCaseToHyphen('movementName')
    'movement-name'
    ```

    First letter can be uppercase as well:

    ```python
    >>> common.camelCaseToHyphen('MovementName')
    'movement-name'
    ```

    ```python
    >>> common.camelCaseToHyphen('movementNameName')
    'movement-name-name'
    ```

    ```python
    >>> common.camelCaseToHyphen('fileName', replacement='_')
    'file_name'
    ```

    Some things you cannot do:

    ```python
    >>> common.camelCaseToHyphen('fileName', replacement='NotFound')
    Traceback (most recent call last):
    ValueError: Replacement must be a single character.
    ```

    ```python
    >>> common.camelCaseToHyphen('fileName', replacement='A')
    Traceback (most recent call last):
    ValueError: Replacement cannot be an uppercase character.
    ```

music21.common.stringTools.formatStr(*msg*, *\*rest\_of\_message*, *\*\*keywords*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](../_modules/music21/common/stringTools.html#formatStr)
:   DEPRECATED: do not use. May be removed at any time.

    Format one or more data elements into string suitable for printing
    straight to stderr or other outputs

    ```python
    >>> a = common.formatStr('test', '1', 2, 3)
    >>> print(a)
    test 1 2 3
    ```

music21.common.stringTools.getMd5(*value=None*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](../_modules/music21/common/stringTools.html#getMd5)
:   Return an md5 hash from a string. If no value is given then
    the current time plus a random number is encoded.

    ```python
    >>> common.getMd5('test')
    '098f6bcd4621d373cade4e832627b4f6'
    ```

music21.common.stringTools.getNumFromStr(*usrStr: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *numbers: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = '0123456789'*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")][[source]](../_modules/music21/common/stringTools.html#getNumFromStr)
:   Given a string, extract any numbers.
    Return two strings, the numbers (as strings) and the remaining characters.

    ```python
    >>> common.getNumFromStr('23a')
    ('23', 'a')
    >>> common.getNumFromStr('23a954Hello')
    ('23954', 'aHello')
    >>> common.getNumFromStr('')
    ('', '')
    ```

music21.common.stringTools.hyphenToCamelCase(*usrStr: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *replacement: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = '-'*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](../_modules/music21/common/stringTools.html#hyphenToCamelCase)
:   Given a hyphen-connected-string, change it to
    a camelCaseConnectedString.

    The replacement can be specified to be something besides a hyphen.

    ```python
    >>> common.hyphenToCamelCase('movement-name')
    'movementName'
    ```

    ```python
    >>> common.hyphenToCamelCase('movement_name', replacement='_')
    'movementName'
    ```

    Safe to call on a string lacking the replacement character:

    ```python
    >>> common.hyphenToCamelCase('voice')
    'voice'
    ```

    And on “words” beginning with numbers:

    ```python
    >>> common.hyphenToCamelCase('music-21')
    'music21'
    ```

music21.common.stringTools.normalizeFilename(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](../_modules/music21/common/stringTools.html#normalizeFilename)
:   take a name that might contain unicode characters, punctuation,
    or spaces and
    normalize it so that it is POSIX compliant (except for the limit
    on length).

    Takes in a string or unicode string and returns a string (unicode in Py3)
    without any accented characters.

    ```python
    >>> common.normalizeFilename('03-Niccolò all’lessandra.not really.xml')
    '03-Niccolo_all_lessandra_not_really.xml'
    ```

music21.common.stringTools.parenthesesMatch(*s: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *open: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = '('*, *close: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ')'*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[ParenthesesMatch](#music21.common.stringTools.ParenthesesMatch "music21.common.stringTools.ParenthesesMatch")][[source]](../_modules/music21/common/stringTools.html#parenthesesMatch)
:   Utility tool to return a list of parentheses matches for a string using a dataclass
    called ParenthesesMatch which has indices of the start and end
    of the match, and the text of the match, and a set of nested
    ParenthesesMatch objects (which may have their own nested objects).

    ```python
    >>> st = r'Bologne wrote (a (whole) (lot) \(of\)) sym\(ph(on)ies\) concertantes.'
    >>> common.stringTools.parenthesesMatch(st)
    [ParenthesesMatch(start=15, end=37, text='a (whole) (lot) \\(of\\)',
                      nested=[ParenthesesMatch(start=18, end=23, text='whole', nested=[]),
                              ParenthesesMatch(start=26, end=29, text='lot', nested=[])]),
     ParenthesesMatch(start=47, end=49, text='on', nested=[])]
    ```

    Other brackets can be used:

    ```python
    >>> st = r'[Whammy bars] and [oboes] do [not [mix] very] [well.]'
    >>> common.stringTools.parenthesesMatch(st, open='[', close=']')
    [ParenthesesMatch(start=1, end=12, text='Whammy bars', nested=[]),
     ParenthesesMatch(start=19, end=24, text='oboes', nested=[]),
     ParenthesesMatch(start=30, end=44, text='not [mix] very',
                      nested=[ParenthesesMatch(start=35, end=38, text='mix', nested=[])]),
     ParenthesesMatch(start=47, end=52, text='well.', nested=[])]
    ```

    The open and close parameters can be multiple characters:

    ```python
    >>> st = r'Did you eat <<beans>> today <<Pythagoreas<<?>>>>'
    >>> common.stringTools.parenthesesMatch(st, open='<<', close='>>')
    [ParenthesesMatch(start=14, end=19, text='beans', nested=[]),
     ParenthesesMatch(start=30, end=46, text='Pythagoreas<<?>>',
                      nested=[ParenthesesMatch(start=43, end=44, text='?', nested=[])])]
    ```

    They cannot, however, be empty:

    ```python
    >>> common.stringTools.parenthesesMatch(st, open='', close='')
    Traceback (most recent call last):
    ValueError: Neither open nor close can be empty.
    ```

    Unmatched opening or closing parentheses will raise a ValueError:

    ```python
    >>> common.stringTools.parenthesesMatch('My (parentheses (sometimes (continue',)
    Traceback (most recent call last):
    ValueError:  Opening '(' at index 3 was never closed
    ```

    ```python
    >>> common.stringTools.parenthesesMatch('This is a <bad> example>', open='<', close='>')
    Traceback (most recent call last):
    ValueError: Closing '>' without '<' at index 23.
    ```

    Note that using multiple characters like a prefix can have unintended consequences:

    ```python
    >>> st = r'[Pitch("C4"), [Pitch("D5"), Pitch("E6")], Pitch("Pity("Z9")")]'
    >>> common.stringTools.parenthesesMatch(st, open='Pitch("', close='")')
    Traceback (most recent call last):
    ValueError: Closing '")' without 'Pitch("' at index 59.
    ```

    So to do something like this, you might need to get creative:

    ```python
    >>> out = common.stringTools.parenthesesMatch(st, open='("', close='")')
    >>> out
    [ParenthesesMatch(start=8, end=10, text='C4', nested=[]),
     ParenthesesMatch(start=22, end=24, text='D5', nested=[]),
     ParenthesesMatch(start=35, end=37, text='E6', nested=[]),
     ParenthesesMatch(start=49, end=59, text='Pity("Z9")',
                      nested=[ParenthesesMatch(start=55, end=57, text='Z9', nested=[])])]
    >>> extractedPitches = []
    >>> for match in out:
    ...     if st[match.start - 7:match.start] == 'Pitch("':
    ...          extractedPitches.append(match.text)
    >>> extractedPitches
    ['C4', 'D5', 'E6', 'Pity("Z9")']
    ```

    * New in v9.3.

music21.common.stringTools.removePunctuation(*s: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](../_modules/music21/common/stringTools.html#removePunctuation)
:   Remove all punctuation from a string.

    ```python
    >>> common.removePunctuation('This, is! my (face).')
    'This is my face'
    ```

music21.common.stringTools.spaceCamelCase(*usrStr: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *replaceUnderscore=True*, *fixMeList=None*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](../_modules/music21/common/stringTools.html#spaceCamelCase)
:   Given a camel-cased string, or a mixture of numbers and characters,
    create a space separated string.

    If replaceUnderscore is True (default) then underscores also become spaces (but without the \_)

    ```python
    >>> common.spaceCamelCase('thisIsATest')
    'this Is A Test'
    >>> common.spaceCamelCase('ThisIsATest')
    'This Is A Test'
    >>> common.spaceCamelCase('movement3')
    'movement 3'
    >>> common.spaceCamelCase('opus41no1')
    'opus 41 no 1'
    >>> common.spaceCamelCase('opus23402no219235')
    'opus 23402 no 219235'
    >>> common.spaceCamelCase('opus23402no219235').title()
    'Opus 23402 No 219235'
    ```

    There is a small list called fixMeList that can fix mistakes.

    ```python
    >>> common.spaceCamelCase('PMFC22')
    'PMFC 22'
    ```

    ```python
    >>> common.spaceCamelCase('hello_myke')
    'hello myke'
    >>> common.spaceCamelCase('hello_myke', replaceUnderscore=False)
    'hello_myke'
    ```

music21.common.stringTools.stripAccents(*inputString: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](../_modules/music21/common/stringTools.html#stripAccents)
:   removes accents from unicode strings.

    ```python
    >>> s = 'trés vite'
    >>> 'é' in s
    True
    >>> common.stripAccents(s)
    'tres vite'
    ```

    Also handles the German Eszett and smart quotes

    ```python
    >>> common.stripAccents('Muß')
    'Muss'
    >>> common.stripAccents('Süss, “êtré”')
    'Suss, "etre"'
    ```

    Note – it is still possible to have non-Ascii characters after this,
    like in this Japanese expression for music:

    ```python
    >>> common.stripAccents('音楽')
    '音楽'
    ```

music21.common.stringTools.whitespaceEqual(*a: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *b: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/common/stringTools.html#whitespaceEqual)
:   returns True if a and b are equal except for whitespace differences

    ```python
    >>> a = '    hello \n there '
    >>> b = 'hello there'
    >>> c = ' bye there '
    >>> common.whitespaceEqual(a, b)
    True
    >>> common.whitespaceEqual(a, c)
    False
    ```
