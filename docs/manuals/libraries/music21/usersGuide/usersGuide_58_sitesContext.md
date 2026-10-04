Source: https://music21.org/music21docs/usersGuide/usersGuide_58_sitesContext.html

# User’s Guide, Chapter 58: Understanding Sites and Contexts

`Music21` contains a powerful context and hierarchy system that lets
users find analytical information in a single place that actually
requires looking at many pieces of information scattered throughout a
score. Take for instance, a fragment of code that we use a lot such as:

```python
>>> n.beat
4
```

It’s great when it works, but then there are times when it doesn’t and
it’s just frustrating. Avoiding those times is what this chapter is
about. And to do so, we’ll need to start asking some “how” questions.

How does a note know what beat it is on? It might help to think about
when we read a printed score, how do we know what beat a note is on? We
have to look at the note, then look up the score to find the most recent
time signature, then find the note again and look at the measure it is
in, count everything preceding it in the measure, and then calculate the
beat. At least three different musical objects need to be consulted: the
note itself, the surrounding measure, and the time signature that
provides an interpretation of how note durations translate to beats.
`Music21` needs to do the same search, and it does all that just on a
little call to the `.beat` property.

(*In the early days of ``music21``, I did not know about the convention
that properties should be fast and easily computable so that the user
does not even realize it is something more complex than an attribute
lookup. The property ``.beat`` is none of the above. If I were starting
over, it would be a method, ``.beat()``, but it is too late to change
now.*)

To understand how this lookup works, we will need to understand better
how `Sites` and `Contexts` work. Advanced users and beginners alike
(and occasionally even the `music21` developers) are frequently
confused by `music21`’s context and hierarchy system. When it works,
it works great, it’s just magic. But, when it doesn’t, it appears to be
a random bug, and it is probably the most common type of bug mention on
the `music21` GitHub tracker that gets “not a bug” as a response.
Magic is fickle that way.

Let’s start by looking at a simple example. We will create a measure and
add a single E-flat to it:

```python
from music21 import *

m = stream.Measure(number=1)
es = note.Note('E-4')
m.insert(2, es)
m.show('text')
```

```python
 {2.0} <music21.note.Note E->
```

At this point, there’s obviously a connection made between the Measure
and the Note.

```python
m[0]
```

```python
 <music21.note.Note E->
```

```python
es.activeSite
```

```python
 <music21.stream.Measure 1 offset=0.0>
```

```python
es.offset
```

```python
 2.0
```

```python
m.elementOffset(es)
```

```python
 2.0
```

But we need to know, what is the nature of this connection? It has
changed several times as `music21` has developed but has been stable
since at least v.4, and it looks to stay that way. The measure (or any
`Stream`) contains an ordered list of the elements in it, and it also
contains a mapping of each element in it to its offset.

The element in a stream (such as a Note) does not however, have a direct
list of what stream or streams it is in. Instead elements have a
property `.sites` that is itself a rather complex object called
`Sites` that keeps track of this information for
it:

```python
es.sites
```

```python
 <music21.sites.Sites at 0x10c806488>
```

## Working with Sites

The `Sites` object keeps track of how many and which streams an
element has been placed in:

```python
es.sites.getSiteCount()
```

```python
 1
```

```python
v = stream.Voice(id=1)
v.append(es)
es.sites.getSiteCount()
```

```python
 2
```

If we need to figure out a particular attribute based on context, the
`Sites` object comes in very handy. For instance, the
`.measureNumber` on a Note or other element, finds a container that is
a Measure and has a `.number` attribute:

```python
es.measureNumber
```

```python
 1
```

We can do the same sort of thing, by calling the `Sites` object
directly with the `getAttrByName` method:

```python
es.sites.getAttrByName('number')
```

```python
 1
```

Or we can just get a list of sites that match a certain class:

```python
es.sites.getSitesByClass(stream.Voice)
```

```python
 [<music21.stream.Voice 1>]
```

Or with a string:

```python
es.sites.getSitesByClass('Measure')
```

```python
 [<music21.stream.Measure 1 offset=0.0>]
```

Notice that what is returned is a list, because an element can appear in
multiple sites, even multiple sites of the same class, so long as those
sites don’t belong to the same hierarchy (that is, those streams are not
both in the same stream or have a common stream somewhere in their
Sites). Let’s put the note in another `Measure` object:

```python
m10 = stream.Measure(number=10)
m10.insert(20, es)
```

```python
es.sites.getSitesByClass('Measure')
```

```python
 [<music21.stream.Measure 1 offset=0.0>, <music21.stream.Measure 10 offset=0.0>]
```

Users can iterate through all sites in a Stream using `.yieldSites()`:

```python
for site in es.sites.yieldSites():
    print(site)
```

```python
 None
 <music21.stream.Measure 1 offset=0.0>
 <music21.stream.Voice 1>
 <music21.stream.Measure 10 offset=0.0>
```

Note two things: (1) each element has a special site called “None” that
stores information about the element when it is not in any Stream (it
used to be used much more, but is not used as much anymore, and is not
counted in the number of sites an element is in), and (2) the sites are
yielded from earliest added to latest. We can reverse it and eliminate
None, with a few parameters:

```python
for site in es.sites.yieldSites(excludeNone=True, sortByCreationTime=True):
    print(site)
```

```python
 <music21.stream.Measure 10 offset=0.0>
 <music21.stream.Voice 1>
 <music21.stream.Measure 1 offset=0.0>
```

So effectively a `Note` or other `Music21Object` can always get its
position in the streams that it is in via `.sites`:

```python
for site in es.sites.yieldSites(excludeNone=True):
    print(site.elementOffset(es), site)
```

```python
 2.0 <music21.stream.Measure 1 offset=0.0>
 0.0 <music21.stream.Voice 1>
 20.0 <music21.stream.Measure 10 offset=0.0>
```

The `Sites` object keeps track of the order of insertion through an
attribute called `.siteDict`

```python
es.sites.siteDict
```

```python
 OrderedDict([(None, <music21.sites.SiteRef Global None Index>),
              (4504830192,
               <music21.sites.SiteRef 0/0 to <music21.stream.Measure 1 offset=0.0>>),
              (4518082656,
               <music21.sites.SiteRef 1/1 to <music21.stream.Voice 1>>),
              (4518134560,
               <music21.sites.SiteRef 2/2 to <music21.stream.Measure 10 offset=0.0>>)])
```

Each element has as its index the memory location of the site and a
lightweight wrapper object around the site (i.e., stream) called a
[`SiteRef`](../moduleReference/moduleSites.html#music21.sites.SiteRef "music21.sites.SiteRef").

*(all sites except “None” are currently “Stream” objects – it was our
intention at the beginning to have other types of site contexts, such as
interpretative contexts (“baroque”, “meantone tuning”) and we might
still someday add those, but for now, a site is a Stream)*

Let’s look at the last one:

```python
lastSiteRef = list(es.sites.siteDict.items())[-1][1]
lastSiteRef
```

```python
 <music21.sites.SiteRef 2/2 to <music21.stream.Measure 10 offset=0.0>>
```

```python
lastSiteRef.siteIndex
```

```python
 2
```

```python
lastSiteRef.siteIndex
```

```python
 2
```

```python
lastSiteRef.globalSiteIndex
```

```python
 2
```

This item allows `music21` to find sites by class without needing to
unwrap the site

```python
lastSiteRef.classString
```

```python
 'Measure'
```

```python
lastSiteRef.site
```

```python
 <music21.stream.Measure 10 offset=0.0>
```

## From weakness I get strength of memory

From what has been shown so far, it appears that effectively the
relationship between a stream and its containing element is a mirror or
two-way: streams know what notes they contain and notes know what
streams they are contained in. But it is a bit more complicated and it
comes from the type of reference each holds to each other.

Streams hold elements with a standard or “strong” reference. As long as
the Stream exists in the computer’s memory, all notes contained in it
will also continue to exist. You never need to worry about streams
losing notes.

The `.sites` object, does not, however, contain strong references to
Streams. Instead it contains what are called “weak references” to
streams. A weak reference allows notes and their `Sites` object to get
access to the stream, **as long as it is still in use somewhere else**,
but once the stream is no longer in use it is allowed to disappear
anytime.

As a demonstration, let’s delete that pesky voice:

```python
del v
```

Now whenever Python determines that it needs some extra space, the Note
object will no longer have reference to the voice in its sites. Note
that, this might not happen immediately. The removal of dead weak
references, part of Python’s garbage collection, takes place at odd
times, dependent on the amount of memory currently used and many other
factors. So one cannot predict whether the `Voice` object would still
be in the note’s sites or not by the time you finish reading this
paragraph. `Music21` uses weak references in a number of other
situations, such as
[derivation objects](usersGuide_17_derivations.html#usersguide-17-derivations), though we are
reducing the number of places where they are used as the version of
Python supported by `music21` gets a smarter and smarter garbage
collector.

You might be thinking that it’s been years since the last time you
called `del` on a variable, so this doesn’t really apply to you. But
look at this code, which represents pretty typical music21 usage:

```python
p = stream.Part()
m = stream.Measure()
p.insert(0, m)
m.insert(1, note.Note('D'))
firstNote = p.recurse().notes.first()
m.insert(0, note.Note('C'))
newFirstNote = p.recurse().notes.first()
(firstNote, newFirstNote)
```

```python
 (<music21.note.Note D>, <music21.note.Note C>)
```

```python
for n in p.flatten():
    if n is firstNote:
        print('Yup, there is a D in the part')
```

```python
 Yup, there is a D in the part
```

Did you see where we created an extra stream only to immediately discard
it? The expression `p.flatten()` creates a new stream that exists just
for long enough to get the first note from it. (We actually store it in
a cache on `p` so that it’s faster the next time we need it, but once
we add another note to `m` the cache is invalidated). The creation of
another stream is one reason to generally prefer `.recurse()` over
`.flatten()`.

Prior to `music21` v.3, the `.notes` call would have created yet
another Stream, but we’ve optimized this out.

The reason why `music21` uses weak references instead of normal
(strong) references to sites is to save some memory because how
frequently objects, such as notes and streams, are copied. When you run
certain analytical or manipulation routines such as
`toSoundingPitch()` or `stripTies()` or even common operations such
as `.flatten()` and `show()`, copies of streams need to be made,
often only to be discarded in a single line of code. If every one of
those streams, with all of their contents, persisted forever just
because a single note from that stream stayed in memory, then the memory
usage of `music21` would be much higher.

Also note that the `Sites` object cleans up “dead” sites from time to
time, and certain context-dependent calls, such as `.next(note.Rest)`
or `.getContextByClass('Measure')` need to search every living site.
Over time, these calls would get slower and slower if otherwise
long-forgotten streams created as byproducts of `.show()` or
`.flatten()` stuck around.

Here’s an example adapted from actual code that caused a problem. The
user was trying to figure out the beat for each note that was not the
continuation of a tie, and he wrote:

```python
bach = corpus.parse('bach/bwv66.6')
allNotes = list(bach.stripTies().recurse().notes)
firstNote = allNotes[0]
```

Problems quickly arose though when he tried to figure out the note’s
beat via `firstNote.beat` – it said that it was on beat 1, even though
this piece in 4/4 began with a one-beat pickup, and should be on beat 4.

What happened? Again, it’s a problem with confusions from disappearing
streams and sites. The `.stripTies()` method creates a new score
hierarchy, where each note in the score hierarchy is a copy derived from
the previous one:

```python
firstNoteOriginal = bach.recurse().notes[0]
firstNoteStripped = bach.stripTies().recurse().notes[0]
(firstNoteOriginal, firstNoteStripped)
```

```python
 (<music21.note.Note C#>, <music21.note.Note C#>)
```

```python
firstNoteOriginal is firstNoteStripped
```

```python
 False
```

```python
firstNoteStripped.derivation
```

```python
 <Derivation of <music21.note.Note C#> from <music21.note.Note C#> via 'stripTies'>
```

```python
firstNoteStripped.derivation.origin is firstNoteOriginal
```

```python
 True
```

So the Note object obtained from `.stripTies()` is not to be found in
the original `bach` score:

```python
bach.containerInHierarchy(firstNoteStripped) is None
```

```python
 True
```

```python
bach.containerInHierarchy(firstNoteOriginal)
```

```python
 <music21.stream.Measure 0 offset=0.0>
```

in fact, firstNoteStripped’s entire containerHierarchy is generally
empty if garbage collection has run. Why? Because firstNoteStripped only
directly belongs to the hierarchy created by the unnamed and unsaved
stream created by `stripTies()`. So how to solve this? In code that
needs access to the hierarchy, make sure that it is preserved by saving
it to a variable. Here we will break up the code calling `stripTies()`
and save it as a variable, `st_bach`. Not only does this solve our
problems, but it makes the code more readable:

```python
bach = corpus.parse('bach/bwv66.6')
st_bach = bach.stripTies()
allNotes = list(st_bach.recurse().notes)
firstNote = allNotes[0]
firstNote.beat
```

```python
 4.0
```

Doing this also fixes another thing that looked like a bug, but is
expected behavior – that `getContextByClass('Measure')` was needing to
follow the derivation chain to find a measure that `firstNote` was not
in. Here it works as expected:

```python
firstNote.getContextByClass('Measure').elementOffset(firstNote)
```

```python
 0.0
```

This was a pretty dense chapter, I know, and it barely scratches the
surface of the complexities of the Context system, so we’ll move to
something lighter if even more distant, and look at Medieval and
Renaissance extensions in `music21` – as soon as that chapter is
completed. Until then, jump ahead to
[Chapter 61: TimespanTrees and Verticalities](usersGuide_61_trees.html#usersguide-61-trees).
