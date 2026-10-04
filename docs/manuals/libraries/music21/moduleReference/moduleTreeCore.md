Source: https://music21.org/music21docs/moduleReference/moduleTreeCore.html

# music21.tree.core

These are the lowest level tools for working with self-balancing AVL trees.

There’s an overhead to creating an AVL tree, but for a large score it is
absolutely balanced by having O(log n) search times.

## AVLNode

class music21.tree.core.AVLNode(*position*, *payload=None*)[[source]](../_modules/music21/tree/core.html#AVLNode)
:   An AVL Tree Node, not specialized in any way, just contains positions.

    ```python
    >>> position = 1.0
    >>> node = tree.core.AVLNode(position)
    >>> node
    <AVLNode: Start:1.0 Height:0 L:None R:None>
    >>> n2 = tree.core.AVLNode(2.0)
    >>> node.rightChild = n2
    >>> node.update()
    >>> node
    <AVLNode: Start:1.0 Height:1 L:None R:0>
    ```

    Nodes can rebalance themselves, but they work best in a Tree.

    Please consult the Wikipedia entry on AVL trees
    (<https://en.wikipedia.org/wiki/AVL_tree>) for a very detailed
    description of how this data structure works.

[`AVLNode`](#music21.tree.core.AVLNode "music21.tree.core.AVLNode") bases

* [`SlottedObjectMixin`](moduleCommonObjects.html#music21.common.objects.SlottedObjectMixin "music21.common.objects.SlottedObjectMixin")

[`AVLNode`](#music21.tree.core.AVLNode "music21.tree.core.AVLNode") methods

AVLNode.debug()[[source]](../_modules/music21/tree/core.html#AVLNode.debug)
:   Get a debug of the Node:

    ```python
    >>> score = tree.examples.makeExampleScore()
    >>> scoreTree = tree.fromStream.asTimespans(score, flatten=True,
    ...              classList=(note.Note, chord.Chord))
    >>> rn = scoreTree.rootNode
    >>> print(rn.debug())
    <OffsetNode 3.0 Indices:0,5,6,12 Length:1>
        L: <OffsetNode 1.0 Indices:0,2,3,5 Length:1>
            L: <OffsetNode 0.0 Indices:0,0,2,2 Length:2>
            R: <OffsetNode 2.0 Indices:3,3,5,5 Length:2>
        R: <OffsetNode 5.0 Indices:6,8,9,12 Length:1>
            L: <OffsetNode 4.0 Indices:6,6,8,8 Length:2>
            R: <OffsetNode 6.0 Indices:9,9,11,12 Length:2>
                R: <OffsetNode 7.0 Indices:11,11,12,12 Length:1>
    ```

AVLNode.moveAttributes(*other*)[[source]](../_modules/music21/tree/core.html#AVLNode.moveAttributes)
:   move attributes from this node to another in case “removal” actually
    means substituting one node for another in the tree.

    Subclass this in derived classes

    Do not copy anything about height, balance, left or right
    children, etc. By default just moves position and payload.

AVLNode.rebalance()[[source]](../_modules/music21/tree/core.html#AVLNode.rebalance)
:   Rebalances the subtree rooted on this node.

    Returns the new central node.

AVLNode.rotateLeftLeft()[[source]](../_modules/music21/tree/core.html#AVLNode.rotateLeftLeft)
:   Rotates a node left twice.

    Makes this node the rightChild of
    the former leftChild and makes the former leftChild’s rightChild
    be the leftChild of this node.

    Used during tree rebalancing.

    Returns the prior leftChild node as the new central node.

AVLNode.rotateLeftRight()[[source]](../_modules/music21/tree/core.html#AVLNode.rotateLeftRight)
:   Rotates a node left, then right.

    Makes this note the rightChild of the former rightChild of the former leftChild node

    Used during tree rebalancing.

    Returns the former rightChild of the former leftChild node as the new central node.

AVLNode.rotateRightLeft()[[source]](../_modules/music21/tree/core.html#AVLNode.rotateRightLeft)
:   Rotates a node right, then left.

    Makes this note the leftChild of the former leftChild of the former rightChild node

    Used during tree rebalancing.

    Returns the former leftChild of the former rightChild node as the new central node.

AVLNode.rotateRightRight()[[source]](../_modules/music21/tree/core.html#AVLNode.rotateRightRight)
:   Rotates a node right twice.

    Makes this node the leftChild of
    the former rightChild and makes the former rightChild’s leftChild
    be the rightChild of this node.

    Used during tree rebalancing.

    Returns the prior rightChild node as the new central node.

AVLNode.update()[[source]](../_modules/music21/tree/core.html#AVLNode.update)
:   Updates the height and balance attributes of the nodes.

    Must be called whenever .leftChild or .rightChild are changed.

    Used for the next balancing operation – does not rebalance itself.

    Note that it only looks at its children’s height and balance attributes
    not their children’s. So if they are wrong, this will be too.

    Returns None

    We create a score with everything correct.

    ```python
    >>> score = tree.examples.makeExampleScore()
    >>> scoreTree = tree.fromStream.asTimespans(score, flatten=True,
    ...             classList=(note.Note, chord.Chord))
    >>> n = scoreTree.rootNode
    >>> n
    <OffsetNode 3.0 Indices:0,5,6,12 Length:1>
    >>> n.height, n.balance
    (3, 1)
    ```

    Now let’s screw up the height and balance

    ```python
    >>> n.height = 100
    >>> n.balance = -2
    >>> n.height, n.balance
    (100, -2)
    ```

    But we can fix it with .update()

    ```python
    >>> n.update()
    >>> n.height, n.balance
    (3, 1)
    ```

    Note that if we were to screw up the balance/height of one of the
    child notes of n then this would not fix that node’s balance/height.
    This method assumes that children have the correct information and only
    updates the information for this node.

[`AVLNode`](#music21.tree.core.AVLNode "music21.tree.core.AVLNode") instance variables

AVLNode.balance
:   Returns the current state of the difference in heights of the
    two subtrees rooted on this node.

    This attribute is used to help balance the AVL tree.

    ```python
    >>> score = tree.examples.makeExampleScore()
    >>> scoreTree = tree.fromStream.asTimespans(score, flatten=True,
    ...                    classList=(note.Note, chord.Chord))
    >>> print(scoreTree.debug())
    <OffsetNode 3.0 Indices:0,5,6,12 Length:1>
    L: <OffsetNode 1.0 Indices:0,2,3,5 Length:1>
    L: <OffsetNode 0.0 Indices:0,0,2,2 Length:2>
    R: <OffsetNode 2.0 Indices:3,3,5,5 Length:2>
    R: <OffsetNode 5.0 Indices:6,8,9,12 Length:1>
    L: <OffsetNode 4.0 Indices:6,6,8,8 Length:2>
    R: <OffsetNode 6.0 Indices:9,9,11,12 Length:2>
    R: <OffsetNode 7.0 Indices:11,11,12,12 Length:1>
    ```

    This tree has one more depth on the right than on the left

    ```python
    >>> scoreTree.rootNode.balance
    1
    ```

    The leftChild of the rootNote is perfectly balanced, while the rightChild is off by
    one (acceptable).

    ```python
    >>> scoreTree.rootNode.leftChild.balance
    0
    >>> scoreTree.rootNode.rightChild.balance
    1
    ```

    The rightChild’s children are also (acceptably) unbalanced:

    ```python
    >>> scoreTree.rootNode.rightChild.leftChild.balance
    0
    >>> scoreTree.rootNode.rightChild.rightChild.balance
    1
    ```

    You should never see a balance other than 1, -1, or 0. If you do then
    something has gone wrong.

AVLNode.height
:   The height of the subtree rooted on this node.

    This property is used to help balance the AVL tree.

    ```python
    >>> score = tree.examples.makeExampleScore()
    >>> scoreTree = tree.fromStream.asTimespans(score, flatten=True,
    ...              classList=(note.Note, chord.Chord))
    >>> print(scoreTree.debug())
    <OffsetNode 3.0 Indices:0,5,6,12 Length:1>
    L: <OffsetNode 1.0 Indices:0,2,3,5 Length:1>
    L: <OffsetNode 0.0 Indices:0,0,2,2 Length:2>
    R: <OffsetNode 2.0 Indices:3,3,5,5 Length:2>
    R: <OffsetNode 5.0 Indices:6,8,9,12 Length:1>
    L: <OffsetNode 4.0 Indices:6,6,8,8 Length:2>
    R: <OffsetNode 6.0 Indices:9,9,11,12 Length:2>
    R: <OffsetNode 7.0 Indices:11,11,12,12 Length:1>
    ```

    ```python
    >>> scoreTree.rootNode.height
    3
    ```

    ```python
    >>> scoreTree.rootNode.rightChild.height
    2
    ```

    ```python
    >>> scoreTree.rootNode.rightChild.rightChild.height
    1
    ```

    ```python
    >>> scoreTree.rootNode.rightChild.rightChild.rightChild.height
    0
    ```

    Once you hit a height of zero, then the next child on either size should be None

    ```python
    >>> print(scoreTree.rootNode.rightChild.rightChild.rightChild.rightChild)
    None
    ```

AVLNode.leftChild
:   The left child of this node.

    After setting the left child you need to do a node update. with node.update()

    ```python
    >>> score = tree.examples.makeExampleScore()
    >>> scoreTree = tree.fromStream.asTimespans(score, flatten=True,
    ...           classList=(note.Note, chord.Chord))
    >>> print(scoreTree.rootNode.debug())
    <OffsetNode 3.0 Indices:0,5,6,12 Length:1>
    L: <OffsetNode 1.0 Indices:0,2,3,5 Length:1>
    L: <OffsetNode 0.0 Indices:0,0,2,2 Length:2>
    R: <OffsetNode 2.0 Indices:3,3,5,5 Length:2>
    R: <OffsetNode 5.0 Indices:6,8,9,12 Length:1>
    L: <OffsetNode 4.0 Indices:6,6,8,8 Length:2>
    R: <OffsetNode 6.0 Indices:9,9,11,12 Length:2>
    R: <OffsetNode 7.0 Indices:11,11,12,12 Length:1>
    ```

    ```python
    >>> print(scoreTree.rootNode.leftChild.debug())
    <OffsetNode 1.0 Indices:0,2,3,5 Length:1>
    L: <OffsetNode 0.0 Indices:0,0,2,2 Length:2>
    R: <OffsetNode 2.0 Indices:3,3,5,5 Length:2>
    ```

AVLNode.payload
:   The content of the node at this point. Usually a Music21Object.

AVLNode.position
:   The position of this node – this is often the same as the offset of
    the node in a containing score, but does not need to be. It could be the .sortTuple

    ```python
    >>> score = tree.examples.makeExampleScore()
    >>> scoreTree = tree.fromStream.asTimespans(score, flatten=True,
    ...            classList=(note.Note, chord.Chord))
    >>> print(scoreTree.rootNode.debug())
    <OffsetNode 3.0 Indices:0,5,6,12 Length:1>
    L: <OffsetNode 1.0 Indices:0,2,3,5 Length:1>
    L: <OffsetNode 0.0 Indices:0,0,2,2 Length:2>
    R: <OffsetNode 2.0 Indices:3,3,5,5 Length:2>
    R: <OffsetNode 5.0 Indices:6,8,9,12 Length:1>
    L: <OffsetNode 4.0 Indices:6,6,8,8 Length:2>
    R: <OffsetNode 6.0 Indices:9,9,11,12 Length:2>
    R: <OffsetNode 7.0 Indices:11,11,12,12 Length:1>
    ```

    ```python
    >>> scoreTree.rootNode.position
    3.0
    ```

    ```python
    >>> scoreTree.rootNode.leftChild.position
    1.0
    ```

    ```python
    >>> scoreTree.rootNode.rightChild.position
    5.0
    ```

AVLNode.rightChild
:   The right child of this node.

    After setting the right child you need to do a node update. with node.update()

    ```python
    >>> score = tree.examples.makeExampleScore()
    >>> scoreTree = tree.fromStream.asTimespans(score, flatten=True,
    ...             classList=(note.Note, chord.Chord))
    >>> print(scoreTree.rootNode.debug())
    <OffsetNode 3.0 Indices:0,5,6,12 Length:1>
    L: <OffsetNode 1.0 Indices:0,2,3,5 Length:1>
    L: <OffsetNode 0.0 Indices:0,0,2,2 Length:2>
    R: <OffsetNode 2.0 Indices:3,3,5,5 Length:2>
    R: <OffsetNode 5.0 Indices:6,8,9,12 Length:1>
    L: <OffsetNode 4.0 Indices:6,6,8,8 Length:2>
    R: <OffsetNode 6.0 Indices:9,9,11,12 Length:2>
    R: <OffsetNode 7.0 Indices:11,11,12,12 Length:1>
    ```

    ```python
    >>> print(scoreTree.rootNode.rightChild.debug())
    <OffsetNode 5.0 Indices:6,8,9,12 Length:1>
    L: <OffsetNode 4.0 Indices:6,6,8,8 Length:2>
    R: <OffsetNode 6.0 Indices:9,9,11,12 Length:2>
    R: <OffsetNode 7.0 Indices:11,11,12,12 Length:1>
    ```

    ```python
    >>> print(scoreTree.rootNode.rightChild.rightChild.debug())
    <OffsetNode 6.0 Indices:9,9,11,12 Length:2>
    R: <OffsetNode 7.0 Indices:11,11,12,12 Length:1>
    ```

    ```python
    >>> print(scoreTree.rootNode.rightChild.rightChild.rightChild.debug())
    <OffsetNode 7.0 Indices:11,11,12,12 Length:1>
    ```

## AVLTree

class music21.tree.core.AVLTree[[source]](../_modules/music21/tree/core.html#AVLTree)
:   Data structure for working with tree.node.AVLNode objects.

    To be subclassed in order to do anything useful with music21 objects.

[`AVLTree`](#music21.tree.core.AVLTree "music21.tree.core.AVLTree") bases

* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`AVLTree`](#music21.tree.core.AVLTree "music21.tree.core.AVLTree") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`AVLTree`](#music21.tree.core.AVLTree "music21.tree.core.AVLTree") methods

AVLTree.createNodeAtPosition(*position*)[[source]](../_modules/music21/tree/core.html#AVLTree.createNodeAtPosition)
:   creates a new node at position and sets the rootNode
    appropriately

    ```python
    >>> avl = tree.core.AVLTree()
    >>> avl.createNodeAtPosition(20)
    >>> avl.rootNode
    <AVLNode: Start:20 Height:0 L:None R:None>
    ```

    ```python
    >>> avl.createNodeAtPosition(10)
    >>> avl.rootNode
    <AVLNode: Start:20 Height:1 L:0 R:None>
    ```

    ```python
    >>> avl.createNodeAtPosition(5)
    >>> avl.rootNode
    <AVLNode: Start:10 Height:1 L:0 R:0>
    ```

    ```python
    >>> avl.createNodeAtPosition(30)
    >>> avl.rootNode
    <AVLNode: Start:10 Height:2 L:0 R:1>
    >>> avl.rootNode.leftChild
    <AVLNode: Start:5 Height:0 L:None R:None>
    >>> avl.rootNode.rightChild
    <AVLNode: Start:20 Height:1 L:None R:0>
    ```

    ```python
    >>> avl.rootNode.rightChild.rightChild
    <AVLNode: Start:30 Height:0 L:None R:None>
    ```

AVLTree.debug()[[source]](../_modules/music21/tree/core.html#AVLTree.debug)
:   Gets string representation of the node tree.

    Useful only for debugging its internal node structure.

    ```python
    >>> tsList = [(0, 2), (0, 9), (1, 1), (2, 3), (3, 4),
    ...           (4, 9), (5, 6), (5, 8), (6, 8), (7, 7)]
    >>> tss = [tree.spans.Timespan(x, y) for x, y in tsList]
    >>> tsTree = tree.timespanTree.TimespanTree()
    >>> tsTree.insert(tss)
    ```

    ```python
    >>> print(tsTree.debug())
    <OffsetNode 3.0 Indices:0,4,5,10 Length:1>
        L: <OffsetNode 1.0 Indices:0,2,3,4 Length:1>
            L: <OffsetNode 0.0 Indices:0,0,2,2 Length:2>
            R: <OffsetNode 2.0 Indices:3,3,4,4 Length:1>
        R: <OffsetNode 5.0 Indices:5,6,8,10 Length:2>
            L: <OffsetNode 4.0 Indices:5,5,6,6 Length:1>
            R: <OffsetNode 6.0 Indices:8,8,9,10 Length:1>
                R: <OffsetNode 7.0 Indices:9,9,10,10 Length:1>
    ```

AVLTree.getNodeAfter(*position*)[[source]](../_modules/music21/tree/core.html#AVLTree.getNodeAfter)
:   Gets the first node after position.

    ```python
    >>> score = corpus.parse('bwv66.6')
    >>> scoreTree = score.asTree(flatten=True)
    >>> node1 = scoreTree.getNodeAfter(0.5)
    >>> node1
    <ElementNode: Start:1.0 <0.20...> Indices:(l:27 *29* r:33) Payload:<music21.note.Note A>>
    >>> node2 = scoreTree.getNodeAfter(0.6)
    >>> node2 is node1
    True
    ```

    ```python
    >>> endNode = scoreTree.getNodeAfter(9999)
    >>> endNode
    <ElementNode: Start:End <0.-5...> Indices:(l:191 *195* r:199)
           Payload:<music21.bar.Barline type=final>>
    ```

    ```python
    >>> while endNode is not None:
    ...     print(endNode)
    ...     endNodePosition = endNode.position
    ...     endNode = scoreTree.getNodeAfter(endNodePosition)
    <ElementNode: Start:End <0.-5...> Indices:(l:191 *195* r:199)
        Payload:<music21.bar.Barline type=final>>
    <ElementNode: Start:End <0.-5...> Indices:(l:196 *196* r:197)
        Payload:<music21.bar.Barline type=final>>
    <ElementNode: Start:End <0.-5...> Indices:(l:196 *197* r:199)
        Payload:<music21.bar.Barline type=final>>
    <ElementNode: Start:End <0.-5...> Indices:(l:198 *198* r:199)
        Payload:<music21.bar.Barline type=final>>
    ```

    ```python
    >>> note1 = score.flatten().notes[30]
    ```

    Works with sortTuple positions as well:

    ```python
    >>> st = note1.sortTuple()
    >>> st
    SortTuple(atEnd=0, offset=6.0, priority=0, classSortOrder=20, isNotGrace=1, insertIndex=...)
    ```

    ```python
    >>> scoreTree.getNodeAfter(st)
    <ElementNode: Start:6.5 <0.20...> Indices:(l:55 *56* r:57)
        Payload:<music21.note.Note D>>
    ```

AVLTree.getNodeBefore(*position*)[[source]](../_modules/music21/tree/core.html#AVLTree.getNodeBefore)
:   Finds the node immediately before position.

    ```python
    >>> score = corpus.parse('bwv66.6')
    >>> scoreTree = score.asTimespans()
    ```

    100 is beyond the end, so it will get the last node in piece.

    ```python
    >>> scoreTree.getNodeBefore(100)
    <OffsetNode 36.0 Indices:195,195,199,199 Length:4>
    ```

    ```python
    >>> scoreTree.getNodeBefore(0) is None
    True
    ```

AVLTree.getNodeByPosition(*position*)[[source]](../_modules/music21/tree/core.html#AVLTree.getNodeByPosition)
:   Searches for a node whose position is position in the subtree
    rooted on node.

    Returns a Node object or None

AVLTree.getPositionAfter(*position*)[[source]](../_modules/music21/tree/core.html#AVLTree.getPositionAfter)
:   Gets start position after position.

    ```python
    >>> score = corpus.parse('bwv66.6')
    >>> scoreTree = score.asTree(flatten=True)
    >>> scoreTree.getPositionAfter(0.5).offset
    1.0
    ```

    Returns None if no succeeding position exists.

    ```python
    >>> endPosition = scoreTree.getPositionAfter(9999)
    >>> while endPosition is not None:
    ...     print(endPosition)
    ...     endPosition = scoreTree.getPositionAfter(endPosition)
    SortTuple(atEnd=1, offset=36.0, priority=0, classSortOrder=-5, ...)
    SortTuple(atEnd=1, offset=36.0, priority=0, classSortOrder=-5, ...)
    SortTuple(atEnd=1, offset=36.0, priority=0, classSortOrder=-5, ...)
    SortTuple(atEnd=1, offset=36.0, priority=0, classSortOrder=-5, ...)
    ```

    Generally speaking, negative positions will usually return 0.0

    ```python
    >>> scoreTree.getPositionAfter(-999).offset
    0.0
    ```

    Unless the Tree is empty in which case, None is returned:

    ```python
    >>> at = tree.core.AVLTree()
    >>> at.getPositionAfter(-999) is None
    True
    ```

AVLTree.getPositionBefore(*position*)[[source]](../_modules/music21/tree/core.html#AVLTree.getPositionBefore)
:   Gets the start position immediately preceding position in this
    position-tree.

    ```python
    >>> score = corpus.parse('bwv66.6')
    >>> scoreTree = score.asTimespans()
    >>> scoreTree.getPositionBefore(100)
    36.0
    ```

    Return None if no preceding position exists.

    ```python
    >>> scoreTree.getPositionBefore(0) is None
    True
    ```

AVLTree.populateFromSortedList(*listOfTuples*)[[source]](../_modules/music21/tree/core.html#AVLTree.populateFromSortedList)
:   Populate this tree from a sorted list of two-tuples of (position, payload).

    This is about an order of magnitude faster (3ms vs 21ms for 1000 items;
    31 vs. 300ms for 10,000 items) than running createNodeAtPosition()
    for each element in a list if it is
    already sorted. Thus, it should be used when converting a
    Stream where .isSorted is True into a tree.

    This method assumes that the current tree is empty (or will be wiped) and
    that listOfTuples is a non-empty
    list where the first element is a unique position to insert,
    and the second is the complete payload for that node, and
    that the positions are strictly increasing in order.

    If any of the conditions is not true, expect to get a dangerously
    badly sorted tree that will be useless.

    ```python
    >>> listOfTuples = [(i, str(i)) for i in range(1000)]
    >>> listOfTuples[10]
    (10, '10')
    >>> avlTree = tree.core.AVLTree()
    >>> avlTree.rootNode is None
    True
    >>> avlTree.populateFromSortedList(listOfTuples)
    >>> avlTree.rootNode
    <AVLNode: Start:500 Height:9 L:8 R:8>
    ```

    ```python
    >>> n = avlTree.rootNode
    >>> while n is not None:
    ...    print(n, repr(n.payload))
    ...    n = n.leftChild
    <AVLNode: Start:500 Height:9 L:8 R:8> '500'
    <AVLNode: Start:250 Height:8 L:7 R:7> '250'
    <AVLNode: Start:125 Height:7 L:6 R:6> '125'
    <AVLNode: Start:62 Height:6 L:5 R:5> '62'
    <AVLNode: Start:31 Height:5 L:4 R:4> '31'
    <AVLNode: Start:15 Height:4 L:3 R:3> '15'
    <AVLNode: Start:7 Height:3 L:2 R:2> '7'
    <AVLNode: Start:3 Height:2 L:1 R:1> '3'
    <AVLNode: Start:1 Height:1 L:0 R:0> '1'
    <AVLNode: Start:0 Height:0 L:None R:None> '0'
    ```

AVLTree.removeNode(*position*)[[source]](../_modules/music21/tree/core.html#AVLTree.removeNode)
:   Removes a node at position and rebalances the tree

    Used internally by TimespanTree.

    ```python
    >>> avl = tree.core.AVLTree()
    >>> avl.createNodeAtPosition(20)
    >>> avl.createNodeAtPosition(10)
    >>> avl.createNodeAtPosition(5)
    >>> avl.createNodeAtPosition(30)
    >>> avl.rootNode
    <AVLNode: Start:10 Height:2 L:0 R:1>
    ```

    Remove node at 30

    ```python
    >>> avl.removeNode(30)
    >>> avl.rootNode
    <AVLNode: Start:10 Height:1 L:0 R:0>
    ```

    Removing a node eliminates its payload:

    ```python
    >>> ten = avl.getNodeByPosition(10)
    >>> ten.payload = 'ten'
    >>> twenty = avl.getNodeByPosition(20)
    >>> twenty.payload = 'twenty'
    ```

    ```python
    >>> avl.removeNode(10)
    >>> avl.rootNode
    <AVLNode: Start:20 Height:1 L:0 R:None>
    >>> avl.rootNode.payload
    'twenty'
    ```

    Removing a non-existent node does nothing.

    ```python
    >>> avl.removeNode(9.5)
    >>> avl.rootNode
    <AVLNode: Start:20 Height:1 L:0 R:None>
    ```

    ```python
    >>> for n in avl:
    ...     print(n, n.payload)
    <AVLNode: Start:5 Height:0 L:None R:None> None
    <AVLNode: Start:20 Height:1 L:0 R:None> twenty
    ```
