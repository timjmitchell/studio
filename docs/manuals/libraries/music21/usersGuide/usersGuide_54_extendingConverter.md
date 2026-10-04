Source: https://music21.org/music21docs/usersGuide/usersGuide_54_extendingConverter.html

# User’s Guide, Chapter 54: Extending Converter with New Formats

For this example, rather than importing \* from music21, we’ll just
import the modules we need. If you’re developing a new SubConverter
class just for yourself you can import everything, but if you’re
thinking that you’d like to contribute your module back to music21
someday, it is important not to import \* since that will create
circular imports.

```python
from music21 import converter, note, stream, meter
```

We’ll create a dummy file format, ‘.sb’ or the ‘singlebeat’ format which
consists solely of a string of letters A-G in groups of any length
separated by spaces. A-G represents the pitch name (no accidentals),
while all notes written conjunctly in a group are interpreted as evenly
fitting within a quarter note.

```python
class SingleBeat(converter.subConverters.SubConverter):
    registerFormats = ('singlebeat',)  # note the comma after the string
    registerInputExtensions = ('sb',)  # these are single element tuples.

    # we will just define parseData for now and let the SubConverter base class
    # deal with loading data from files of type .sb and URLs ending in .sb for us.

    def parseData(self, strData, number=None):  # movement number is ignored...
        '''  'AB C' -> A-8th, B-8th, C-qtr '''
        strDataList = strData.split()
        s = stream.Part()
        m = meter.TimeSignature('4/4')
        s.insert(0, m)
        for beat in strDataList:
            ql = 1.0/len(beat)
            for n in beat:
                nObj = note.Note(n)
                nObj.duration.quarterLength = ql
                s.append(nObj)
        self.stream = s.makeMeasures()
```

Next we tell the converter module that our subConverter exists and can
handle ‘singlebeat’/‘singleBeat’/‘.sb’ files.

```python
converter.registerSubConverter(SingleBeat)
```

Now the format is ready to be used through converter.parse() on string
data:

```python
s = converter.parse('CDC DE F GAGB GE C DEFED C', format='singleBeat')
s.show('text')
```

```python
 {0.0} <music21.stream.Measure 1 offset=0.0>
     {0.0} <music21.clef.TrebleClef>
     {0.0} <music21.meter.TimeSignature 4/4>
     {0.0} <music21.note.Note C>
     {0.3333} <music21.note.Note D>
     {0.6667} <music21.note.Note C>
     {1.0} <music21.note.Note D>
     {1.5} <music21.note.Note E>
     {2.0} <music21.note.Note F>
     {3.0} <music21.note.Note G>
     {3.25} <music21.note.Note A>
     {3.5} <music21.note.Note G>
     {3.75} <music21.note.Note B>
 {4.0} <music21.stream.Measure 2 offset=4.0>
     {0.0} <music21.note.Note G>
     {0.5} <music21.note.Note E>
     {1.0} <music21.note.Note C>
     {2.0} <music21.note.Note D>
     {2.2} <music21.note.Note E>
     {2.4} <music21.note.Note F>
     {2.6} <music21.note.Note E>
     {2.8} <music21.note.Note D>
     {3.0} <music21.note.Note C>
     {4.0} <music21.bar.Barline type=final>
```

Or, singleBeat is now a custom header for parse:

```python
s = converter.parse('singleBeat: CDC DE F GAGB GE C DEFED C')
s[-1][0]
```

```python
 <music21.note.Note G>
```

Or we can write out a file and read it in:

```python
from music21 import environment
e = environment.Environment()
fp = e.getTempFile('.sb')
with open(fp, 'w') as f:
    f.write('CDC DE F GAGB GE C DEFED C')

print(fp)
```

```python
 /var/folders/qg/klchy5t14bb2ty9pswk6c2bw0000gn/T/music21/tmpowosgwxt.sb
```

```python
s2 = converter.parse(fp)
s2.show('text')
```

```python
 {0.0} <music21.metadata.Metadata object at 0x114aeb490>
 {0.0} <music21.stream.Measure 1 offset=0.0>
     {0.0} <music21.clef.TrebleClef>
     {0.0} <music21.meter.TimeSignature 4/4>
     {0.0} <music21.note.Note C>
     {0.3333} <music21.note.Note D>
     {0.6667} <music21.note.Note C>
     {1.0} <music21.note.Note D>
     {1.5} <music21.note.Note E>
     {2.0} <music21.note.Note F>
     {3.0} <music21.note.Note G>
     {3.25} <music21.note.Note A>
     {3.5} <music21.note.Note G>
     {3.75} <music21.note.Note B>
 {4.0} <music21.stream.Measure 2 offset=4.0>
     {0.0} <music21.note.Note G>
     {0.5} <music21.note.Note E>
     {1.0} <music21.note.Note C>
     {2.0} <music21.note.Note D>
     {2.2} <music21.note.Note E>
     {2.4} <music21.note.Note F>
     {2.6} <music21.note.Note E>
     {2.8} <music21.note.Note D>
     {3.0} <music21.note.Note C>
     {4.0} <music21.bar.Barline type=final>
```

If you want to be extra-safe, pass the format in with the parse

```python
s3 = converter.parse(fp, format='singleBeat')
s3
```

```python
 <music21.stream.Part 0x114855720>
```

SingleBeat will now appear in all places where fileformats are listed:

```python
from music21 import common
common.findFormat('singleBeat')
```

```python
 ('singlebeat', '.sb')
```

We can cleanup what we’ve done (always be a good citizen) by calling
`converter.resetSubConverters`.

```python
converter.resetSubConverters()
```

A demonstration of the singleBeat type (simplified a bit), but including
a `.write()` call, can be found in the `converter` directory under
the filename `qmConverter.py`.

Now that you have a system that can take in just about any format you
can write a converter for, it’s time to get back to understanding the
music that you have available to you. Meter is a concept that is far
deeper than simple concepts like 4/4 or 6/8 would let on. To learn more
about how to do metrical analysis, turn to
[Chapter 55: Advanced Meter Topics](usersGuide_55_advancedMeter.html#usersguide-55-advancedmeter)
