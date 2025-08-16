[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Collections
  
**Lesson:** Implementations

[Implementations](index.html)

[Set Implementations](set.html)

List Implementations

[Map Implementations](map.html)

[Queue Implementations](queue.html)

[Wrapper Implementations](wrapper.html)

[Convenience Implementations](convenience.html)

[Summary of Implementations](summary.html)

[Questions and Exercises](QandE/questions.html)

[Home Page](../../index.html)
>
[Collections](../index.html)
>
[Implementations](index.html)

[« Previous](set.html) • [Trail](../TOC.html) • [Next »](map.html)

# List Implementations

`List` implementations are grouped into general-purpose
and special-purpose implementations.

### General-Purpose List Implementations

There are two general-purpose
[`List`](http://download.oracle.com/javase/7/docs/api/java/util/List.html) implementations —
[`ArrayList`](http://download.oracle.com/javase/7/docs/api/java/util/ArrayList.html) and
[`LinkedList`](http://download.oracle.com/javase/7/docs/api/java/util/LinkedList.html).
Most of the time, you'll probably use `ArrayList`, which offers constant-time positional access and is just plain fast. It does not have to allocate a node object for each element in the `List`, and it can take advantage of `System.arraycopy` when it has to move multiple elements at the same time. Think of `ArrayList` as `Vector` without the synchronization overhead.

If you frequently add elements to the beginning of the `List`
or iterate over the `List` to delete elements from its interior,
you should consider using `LinkedList`. These operations require
constant-time in a `LinkedList` and linear-time in an
`ArrayList`. But you pay a big price in performance.
Positional access requires linear-time in a `LinkedList`
and constant-time in an `ArrayList`. Furthermore, the constant
factor for `LinkedList` is much worse. If you think you
want to use a `LinkedList`, measure the performance of your
application with both `LinkedList` and `ArrayList`
before making your choice; `ArrayList` is usually faster.

`ArrayList` has one tuning parameter — the *initial
capacity*, which refers to the number of elements the
`ArrayList` can hold before it has to grow.
`LinkedList` has no tuning parameters and seven optional
operations, one of which is `clone`. The other six are
`addFirst`, `getFirst`, `removeFirst`,
`addLast`, `getLast`, and `removeLast`.
`LinkedList` also implements the `Queue` interface.

### Special-Purpose List Implementations

[`CopyOnWriteArrayList`](http://download.oracle.com/javase/7/docs/api/java/util/concurrent/CopyOnWriteArrayList.html) is a `List` implementation backed up by a copy-on-write array.
This implementation is similar in nature to `CopyOnWriteArraySet`.
No synchronization is necessary, even during iteration,
and iterators are guaranteed never to throw
`ConcurrentModificationException`. This implementation
is well suited to maintaining event-handler lists, in which change
is infrequent, and traversal is frequent and potentially time-consuming.

If you need synchronization, a `Vector` will be slightly
faster than an `ArrayList` synchronized with
`Collections.synchronizedList`. But `Vector`
has loads of legacy operations, so be careful to always manipulate the
`Vector` with the `List` interface or else you won't be
able to replace the implementation at a later time.

If your `List` is fixed in size — that is, you'll never use
`remove`, `add`, or any of the bulk operations other
than `containsAll` — you have a third option that's definitely
worth considering. See `Arrays.asList` in the
[Convenience Implementations](convenience.html) section for more information.

[« Previous](set.html)
•
[Trail](../TOC.html)
•
[Next »](map.html)

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

**Previous page:** Set Implementations
  
**Next page:** Map Implementations




A browser with JavaScript enabled is required for this page to operate properly.