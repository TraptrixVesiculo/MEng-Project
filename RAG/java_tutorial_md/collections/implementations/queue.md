[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Collections
  
**Lesson:** Implementations

[Implementations](index.html)

[Set Implementations](set.html)

[List Implementations](list.html)

[Map Implementations](map.html)

Queue Implementations

[Wrapper Implementations](wrapper.html)

[Convenience Implementations](convenience.html)

[Summary of Implementations](summary.html)

[Questions and Exercises](QandE/questions.html)

[Home Page](../../index.html)
>
[Collections](../index.html)
>
[Implementations](index.html)

[« Previous](map.html) • [Trail](../TOC.html) • [Next »](wrapper.html)

# Queue Implementations

The `Queue` implementations are grouped into
general-purpose and concurrent implementations.

### General-Purpose Queue Implementations

As mentioned in the previous section, `LinkedList`
implements the `Queue` interface, providing
first in, first out (FIFO)
queue operations for `add`, `poll`, and so on.

The
[`PriorityQueue`](http://download.oracle.com/javase/7/docs/api/java/util/PriorityQueue.html) class is a priority queue based on the *heap* data structure.
This queue orders elements according to the order specified at
construction time, which can be the elements' natural ordering or the ordering
imposed by an explicit `Comparator`.

The queue retrieval operations — `poll`, `remove`, `peek`, and `element` — access the element at the head of the queue. The *head of the queue* is the least element with
respect to the specified ordering. If multiple elements are tied
for least value, the head is one of those elements; ties are
broken arbitrarily.

`PriorityQueue` and its iterator implement all of the
optional methods of the `Collection` and `Iterator`
interfaces. The iterator provided in method `iterator`
is not guaranteed to traverse the elements of the `PriorityQueue`
in any particular order. For ordered traversal,
consider using `Arrays.sort(pq.toArray())`.

### Concurrent Queue Implementations

The `java.util.concurrent` package contains a set of synchronized
`Queue` interfaces and classes.
[`BlockingQueue`](http://download.oracle.com/javase/7/docs/api/java/util/concurrent/BlockingQueue.html) extends `Queue` with operations that wait for the queue to become
nonempty when retrieving an element and for space to become
available in the queue when storing an element. This interface is
implemented by the following classes:

* [`LinkedBlockingQueue`](http://download.oracle.com/javase/7/docs/api/java/util/concurrent/LinkedBlockingQueue.html) — an optionally bounded FIFO blocking queue backed by linked nodes
* [`ArrayBlockingQueue`](http://download.oracle.com/javase/7/docs/api/java/util/concurrent/ArrayBlockingQueue.html) — a bounded FIFO blocking queue backed by an array
* [`PriorityBlockingQueue`](http://download.oracle.com/javase/7/docs/api/java/util/concurrent/PriorityBlockingQueue.html) — an unbounded blocking priority queue backed by a heap
* [`DelayQueue`](http://download.oracle.com/javase/7/docs/api/java/util/concurrent/DelayQueue.html) — a time-based scheduling queue backed by a heap
* [`SynchronousQueue`](http://download.oracle.com/javase/7/docs/api/java/util/concurrent/SynchronousQueue.html) — a simple rendezvous mechanism that uses the `BlockingQueue`
  interface

In JDK 7,
[`TransferQueue`](http://download.oracle.com/javase/7/docs/api/java/util/concurrent/TransferQueue.html) is a specialized `BlockingQueue` in which code that adds an element to the
queue has the option of waiting (blocking) for code in another thread to
retrieve the element. `TransferQueue` has a single implementation:

* [`LinkedTransferQueue`](http://download.oracle.com/javase/7/docs/api/java/util/concurrent/LinkedTransferQueue.html) — an unbounded `TransferQueue` based on linked nodes

[« Previous](map.html)
•
[Trail](../TOC.html)
•
[Next »](wrapper.html)

---

Problems with the examples? Try [Compiling and Running
the Examples: FAQs](../../information/run-examples.html).
  
Complaints? Compliments? Suggestions? [Give
us your feedback](http://download.oracle.com/javase/feedback.html).

Your use of this page and all the material on pages under "The Java Tutorials" banner,
and all the material on pages under "The Java Tutorials" banner is subject to the [Java SE Tutorial Copyright
and License](../../information/license.html).
Additionally, any example code contained in any of these Java
Tutorials pages is licensed under the
[Code
Sample License](http://developers.sun.com/license/berkeley_license.html).

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| |  |  | | --- | --- | | duke image | Oracle logo | | [About Oracle](http://www.oracle.com/us/corporate/index.html) | [Oracle Technology Network](http://www.oracle.com/technology/index.html) | [Terms of Service](https://www.samplecode.oracle.com/servlets/CompulsoryClickThrough?type=TermsOfService) | Copyright © 1995, 2011 Oracle and/or its affiliates. All rights reserved. |

**Previous page:** Map Implementations
  
**Next page:** Wrapper Implementations




A browser with JavaScript enabled is required for this page to operate properly.