Source: https://music21.org/music21docs/moduleReference/moduleSites.html

# music21.sites

sites.py – Objects for keeping track of relationships among Music21Objects

## SiteRef

class music21.sites.SiteRef[[source]](../_modules/music21/sites.html#SiteRef)
:   a single Site (stream, container, parent, reference, etc.) stored inside the Sites object.

    A very simple object.

    This site would be stored in the .sites.siteDict for, say a note.Note, if it were in
    st at offset 20.0

    ```python
    >>> st = stream.Stream()
    >>> st.id = 'hi'
    ```

    ```python
    >>> s = sites.SiteRef()
    >>> s.classString = st.classes[0]
    >>> s.site = st
    >>> s.isDead
    False
    ```

    If you call s.site, you always get an object out, but internally, there’s a .siteWeakref that
    stores a weakref to the site.

    ```python
    >>> s.site
    <music21.stream.Stream hi>
    >>> s.siteWeakref
    <weakref at 0x123456; to ...Stream' at 0x111111>
    ```

    If you turn sites.WEAKREF\_ACTIVE to False then .siteWeakref just stores another reference to
    the site. Bad for memory. Good for debugging pickling.

[`SiteRef`](#music21.sites.SiteRef "music21.sites.SiteRef") bases

* [`SlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.SlottedObjectMixin "music21.common.objects.SlottedObjectMixin")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`SiteRef`](#music21.sites.SiteRef "music21.sites.SiteRef") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`SiteRef`](#music21.sites.SiteRef "music21.sites.SiteRef") read/write properties

SiteRef.site

## Sites

class music21.sites.Sites[[source]](../_modules/music21/sites.html#Sites)
:   An object, stored within a Music21Object, that stores (weak) references to
    a collection of objects that may be contextually relevant to this object.

    Most of these objects are locations (also called sites), or Streams that
    contain this object.

    All defined contexts are stored as dictionaries in a dictionary. The
    outermost dictionary stores objects.

[`Sites`](#music21.sites.Sites "music21.sites.Sites") bases

* [`SlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.SlottedObjectMixin "music21.common.objects.SlottedObjectMixin")

[`Sites`](#music21.sites.Sites "music21.sites.Sites") methods

Sites.add(*obj*, *timeValue=None*, *idKey=None*, *classString=None*)[[source]](../_modules/music21/sites.html#Sites.add)
:   Add a reference to the Sites collection for this object. Automatically
    called on stream.insert(n), etc.

    idKey stores the id() of the obj. If None, then id(obj) is used.

    classString stores the class of obj. If None then obj.classes[0]
    is used.

    TODO: Tests. Including updates.

Sites.clear()[[source]](../_modules/music21/sites.html#Sites.clear)
:   Clear all stored data.

Sites.get(*\**, *sortByCreationTime=False*, *priorityTarget=None*, *excludeNone=False*)[[source]](../_modules/music21/sites.html#Sites.get)
:   Get references; order, based on dictionary keys, is from most
    recently added to least recently added.

    The sortByCreationTime option will sort objects by creation time,
    where most-recently assigned objects are returned first.
    Can be [False, other], [True, 1] or [‘reverse’, -1]

    If priorityTarget is defined, this object will be placed first in the list of objects.

    ```python
    >>> class Mock(base.Music21Object):
    ...     pass
    >>> aObj = Mock()
    >>> bObj = Mock()
    >>> cObj = Mock()
    >>> aSites = sites.Sites()
    >>> aSites.add(cObj)
    >>> aSites.add(aObj)
    >>> aSites.add(bObj)
    ```

    Arbitrary order, so we compare with sets:

    ```python
    >>> set(aSites.get()) == {None, cObj, aObj, bObj}
    True
    ```

    Particular order, with None at the end.

    ```python
    >>> aSites.get(sortByCreationTime=True) == [bObj, aObj, cObj, None]
    True
    ```

    Priority target

    ```python
    >>> begotten = aSites.get(sortByCreationTime=True, priorityTarget=cObj, excludeNone=True)
    >>> begotten == [cObj, bObj, aObj]
    True
    ```

    * Changed in v5.5: keyword only.

Sites.getAttrByName(*attrName*)[[source]](../_modules/music21/sites.html#Sites.getAttrByName)
:   Given an attribute name, search all objects and find the first that
    matches this attribute name; then return a reference to this attribute.

    Works in reverse order, so most recent site is returned first.

    ```python
    >>> class Mock(base.Music21Object):
    ...     attr1 = 234
    >>> aObj = Mock()
    >>> aObj.attr1 = 234
    >>> bObj = Mock()
    >>> bObj.attr1 = 98
    >>> aSites = sites.Sites()
    >>> len(aSites)
    1
    >>> aSites.add(aObj)
    >>> len(aSites)
    2
    ```

    ```python
    >>> aSites.getAttrByName('attr1') == 234
    True
    ```

    ```python
    >>> aSites.remove(aObj)
    >>> aSites.add(bObj)
    >>> aSites.getAttrByName('attr1') == 98
    True
    ```

    An incorrect attribute name will just give none:

    ```python
    >>> aSites.getAttrByName('blah') is None
    True
    ```

Sites.getById(*siteId*)[[source]](../_modules/music21/sites.html#Sites.getById)
:   Return the object specified by an id.
    Used for testing and debugging. Should NOT be used in production code.

    ```python
    >>> a = note.Note()
    >>> s = stream.Stream()
    >>> s.append(a)
    >>> a.sites.getById(id(s)) is s
    True
    ```

Sites.getObjByClass(*className*, *\**, *callerFirst=None*, *sortByCreationTime=False*, *priorityTarget=None*, *getElementMethod=<ElementSearch.AT\_OR\_BEFORE>*, *memo=None*)[[source]](../_modules/music21/sites.html#Sites.getObjByClass)
:   Return the most recently added reference based on className. Class
    name can be a string or the class name.

    This will recursively search the sitesDicts of objects in Site objects in
    the siteDict.

    The callerFirst parameters is simply used to pass a reference of the
    first caller; this is necessary if we are looking within a Stream for a
    flat offset position.

    If priorityTarget is specified, this location will be searched first. use
    priorityTarget=activeSite to prioritize that.

    The getElementMethod is a string that selects which Stream method is
    used to get elements for searching with getElementsByClass() calls.

    ```python
    >>> import time
    >>> class Mock(base.Music21Object):
    ...     pass
    >>> aObj = Mock()
    >>> bObj = Mock()
    >>> aSites = sites.Sites()
    >>> aSites.add(aObj)
    >>> aSites.add(bObj)
    ```

    We get the most recently added object first

    ```python
    >>> aSites.getObjByClass('Mock', sortByCreationTime=True) == bObj
    True
    ```

    ```python
    >>> aSites.getObjByClass(Mock, sortByCreationTime=True) == bObj
    True
    ```

    * Changed in v5.5: all arguments except className are keyword only.

Sites.getSiteCount()[[source]](../_modules/music21/sites.html#Sites.getSiteCount)
:   Return the number of non-dead sites, excluding the None site. This does not
    unwrap weakrefs for performance.

    ```python
    >>> a = note.Note()
    >>> a.sites.getSiteCount()
    0
    >>> s = stream.Stream()
    >>> s.append(a)
    >>> a.sites.getSiteCount()
    1
    >>> sf = s.flatten()
    >>> a.sites.getSiteCount()
    2
    ```

Sites.getSiteIds()[[source]](../_modules/music21/sites.html#Sites.getSiteIds)
:   Return a set of all site Ids.

    ```python
    >>> class Mock(base.Music21Object):
    ...     pass
    >>> aSite = Mock()
    >>> dc = sites.Sites()
    >>> dc.add(aSite)
    >>> dc.getSiteIds() == {None, id(aSite)}
    True
    ```

Sites.getSitesByClass(*className*)[[source]](../_modules/music21/sites.html#Sites.getSitesByClass)
:   Return a list of unwrapped site from siteDict.site [SiteRef.site]
    (generally a Stream)
    that matches the provided class.

    Input can be either a Class object or a string

    ```python
    >>> class Mock(base.Music21Object):
    ...     pass
    >>> aObj = Mock()
    >>> bObj = Mock()
    >>> cObj = stream.Stream()
    >>> aSites = sites.Sites()
    ```

    ```python
    >>> aSites.add(aObj)
    >>> aSites.add(bObj)
    >>> aSites.add(cObj)
    ```

    ```python
    >>> aSites.getSitesByClass(Mock) == [aObj, bObj]
    True
    ```

    ```python
    >>> aSites.getSitesByClass('Stream') == [cObj]
    True
    ```

Sites.hasSiteId(*siteId*)[[source]](../_modules/music21/sites.html#Sites.hasSiteId)
:   Return True or False if this Sites object already has this site id.

    ```python
    >>> class Mock(base.Music21Object):
    ...     pass
    >>> aSite = Mock()
    >>> bSite = Mock()
    >>> dc = sites.Sites()
    >>> dc.add(aSite)
    >>> dc.hasSiteId(id(aSite))
    True
    >>> dc.hasSiteId(id(bSite))
    False
    ```

    Note that we use ‘None’ not id(None) as a key:

    ```python
    >>> dc.hasSiteId(id(None))
    False
    >>> dc.hasSiteId(None)
    True
    ```

Sites.hasSpannerSite()[[source]](../_modules/music21/sites.html#Sites.hasSpannerSite)
:   Return True if this object is found in any Spanner. This is determined
    by looking for a SpannerStorage Stream class as a Site.

Sites.hasVariantSite()[[source]](../_modules/music21/sites.html#Sites.hasVariantSite)
:   Return True if this object is found in any Variant. This is determined
    by looking for a VariantStorage Stream class as a Site.

Sites.purgeLocations(*rescanIsDead=False*)[[source]](../_modules/music21/sites.html#Sites.purgeLocations)
:   Clean all locations that refer to objects that no longer exist.

    The removeOrphanedSites option removes sites that may have been the
    result of deepcopy: the element has the site, but the site does not
    have the element. This results b/c Sites are shallow-copied, and then
    elements are re-added.

    ```python
    >>> import gc
    >>> class Mock(base.Music21Object):
    ...     pass
    >>> aStream = stream.Stream()
    >>> bStream = stream.Stream()
    >>> mySites = sites.Sites()
    >>> len(mySites)
    1
    >>> mySites.add(aStream)
    >>> mySites.add(bStream)
    >>> del aStream
    >>> numObjectsCollected = gc.collect()  # make sure to garbage collect
    ```

    We still have 3 locations – just because aStream is gone, doesn’t
    make it disappear from sites

    ```python
    >>> len(mySites)
    3
    ```

    ```python
    >>> mySites.purgeLocations(rescanIsDead=True)
    >>> len(mySites)
    2
    ```

Sites.remove(*site*)[[source]](../_modules/music21/sites.html#Sites.remove)
:   Remove the object (a context or location site) specified from Sites.
    Object provided can be a location site (i.e., a Stream) or a pure
    context (like a Temperament).

    N.B. – like all .sites operations, this is an advanced tool not for
    standard music21 usage. Instead of:

    > elObj.remove(streamObj)

    use this command, which will take care of .sites.remove as well as
    removing elObj from streamObj.elements:

    > streamObj.remove(elObj)

    ```python
    >>> class Mock(base.Music21Object):
    ...     pass
    >>> aSite = Mock()
    >>> bSite = Mock()
    >>> cSite = Mock()
    >>> aSites = sites.Sites()
    >>> len(aSites)
    1
    >>> aSites.add(aSite)
    >>> len(aSites)
    2
    ```

    ```python
    >>> aSites.add(bSite)
    >>> len(aSites)
    3
    ```

    ```python
    >>> aSites.add(cSite)
    >>> len(aSites)
    4
    ```

    ```python
    >>> aSites.remove(aSite)
    >>> len(aSites)
    3
    ```

Sites.removeById(*idKey*)[[source]](../_modules/music21/sites.html#Sites.removeById)
:   Remove a site entry by id key,
    which is id() of the object.

Sites.setAttrByName(*attrName*, *value*)[[source]](../_modules/music21/sites.html#Sites.setAttrByName)
:   Given an attribute name, search all objects and find the first that
    matches this attribute name; then return a reference to this attribute.

    ```python
    >>> class Mock(base.Music21Object):
    ...     attr1 = 234
    >>> aObj = Mock()
    >>> bObj = Mock()
    >>> bObj.attr1 = 98
    >>> aSites = sites.Sites()
    >>> aSites.add(aObj)
    >>> aSites.add(bObj)
    >>> aSites.setAttrByName('attr1', 'test')
    >>> aSites.getAttrByName('attr1') == 'test'
    True
    ```

Sites.yieldSites(*\**, *excludeNone: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[True]*, *sortByCreationTime: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")['reverse'] = False*, *priorityTarget=None*) → Generator[stream.Stream, [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][[source]](../_modules/music21/sites.html#Sites.yieldSites)

Sites.yieldSites(*\**, *excludeNone: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *sortByCreationTime: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")['reverse'] = False*, *priorityTarget=None*) → Generator[stream.Stream | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]
:   Yield references; order, based on dictionary keys, is from least
    recently added to most recently added.

    The sortByCreationTime option if set to True will sort objects by creation time,
    where most-recently assigned objects are returned first.

    Note that priorityTarget is searched only on id – this could be dangerous if the
    target has been garbage collected and the id is reused. Unlikely since you have to
    pass in the priorityTarget itself, so therefore it still exists.

    This can be much faster than .get in the case where the sought-for site
    is earlier in the list.

    ```python
    >>> class Mock(base.Music21Object):
    ...     def __init__(self, idEl):
    ...         self.id = idEl
    >>> aObj = Mock('a')
    >>> bObj = Mock('b')
    >>> cObj = Mock('c')
    >>> aSites = sites.Sites()
    >>> aSites.add(cObj)
    >>> aSites.add(aObj)
    >>> aSites.add(bObj)
    ```

    Returns a generator:

    ```python
    >>> ys = aSites.yieldSites()
    >>> ys
    <generator object Sites.yieldSites at 0x1058085e8>
    ```

    That’s no help, so iterate over it instead:

    ```python
    >>> for s in aSites.yieldSites(sortByCreationTime=True, excludeNone=True):
    ...     print(s.id)
    b
    a
    c
    ```

    With priorityTarget

    ```python
    >>> for s in aSites.yieldSites(sortByCreationTime=True, priorityTarget=cObj,
    ...                            excludeNone=True):
    ...     print(s.id)
    c
    b
    a
    ```

    * Changed in v3: changed dramatically from previously unused version
      sortByCreationTime=’reverse’ is removed, since the ordered dict takes
      care of it and was not working.
    * Changed in v8: arguments are keyword only
