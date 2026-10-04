Source: https://music21.org/music21docs/moduleReference/moduleMusicxmlXmlSoundParser.html

# music21.musicxml.xmlSoundParser

Functions that convert <sound> tag to the many music21
objects that this tag might represent.

Pulled out because xmlToM21 is getting way too big.

## SoundTagMixin

class music21.musicxml.xmlSoundParser.SoundTagMixin[[source]](../_modules/music21/musicxml/xmlSoundParser.html#SoundTagMixin)
:   This Mixin is applied to MeasureParser – it is moved
    out from there because there is still a lot to write
    here and xmlToM21.py is getting too big.

[`SoundTagMixin`](#music21.musicxml.xmlSoundParser.SoundTagMixin "music21.musicxml.xmlSoundParser.SoundTagMixin") methods

SoundTagMixin.setSound(*mxSound: [Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")*, *mxDir: [Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *staffKey: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *totalOffset: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/musicxml/xmlSoundParser.html#SoundTagMixin.setSound)
:   Takes a <sound> tag and creates objects from it.
    Presently only handles <sound tempo=’x’> events and inserts them as MetronomeMarks.
    If the <sound> tag is a child of a <direction> tag, the direction information
    is used to set the placement of the MetronomeMark.

SoundTagMixin.setSoundTempo(*mxSound: [Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")*, *mxDir: [Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*, *staffKey: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *totalOffset: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/musicxml/xmlSoundParser.html#SoundTagMixin.setSoundTempo)
:   Add a metronome mark from the tempo attribute of a <sound> tag.

SoundTagMixin.xmlSound(*mxSound: [Element](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/musicxml/xmlSoundParser.html#SoundTagMixin.xmlSound)
:   Convert a <sound> tag to one or more relevant objects
    (presently just MetronomeMark),
    and add it or them to the core and staffReference.
