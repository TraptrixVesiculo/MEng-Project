[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

Implementations

[Set Implementations](set.html)

[List Implementations](list.html)

[Map Implementations](map.html)

[Queue Implementations](queue.html)

[Wrapper Implementations](wrapper.html)

[Convenience Implementations](convenience.html)

[Summary of Implementations](summary.html)

[Questions and Exercises](QandE/questions.html)

**Trail:** Collections

[Home Page](../../index.html)
>
[Collections](../index.html)

[« Previous](../interfaces/index.html) • [Trail](../TOC.html) • [Next »](set.html)

# Lesson: Implementations

Implementations are the data objects used to store collections, which
implement the interfaces described in
[the Interfaces section.](../interfaces/index.html).
This lesson describes the following kinds of implementations:

* **General-purpose implementations** are the most commonly used
  implementations, designed for everyday use.
They are summarized in the table below.* **Special-purpose implementations** are designed for use in
  special situations and display nonstandard performance characteristics,
  usage restrictions, or behavior.
* **Concurrent implementations** are designed to support high
  concurrency, typically at the expense of single-threaded performance.
  These implementations are part of the `java.util.concurrent` package.
* **Wrapper implementations** are used in combination with other
  types of implementations, often the general-purpose ones,
  to provide added or restricted functionality.
* **Convenience implementations** are mini-implementations, typically
  made available via static factory methods, that provide convenient,
  efficient alternatives to general-purpose implementations for special
  collections (for example, singleton sets).
* **Abstract implementations** are skeletal implementations that
  facilitate the construction of custom implementations —
  described later in the
  [Custom Collection Implementations](../custom-implementations/index.html) section. An advanced topic, it's not particularly difficult,
  but relatively few people will need to do it.

The general-purpose implementations are summarized in the
following table.

**General-purpose Implementations**

| Interfaces | Implementations | | | | |
|  | **Hash table** | **Resizable array** | **Tree** | **Linked list** | **Hash table + Linked list** |
| `Set` | `HashSet` |  | `TreeSet` |  | `LinkedHashSet` |
| `List` |  | `ArrayList` |  | `LinkedList` |  |
| `Queue` |  |  |  |  |  |
| `Map` | `HashMap` |  | `TreeMap` |  | `LinkedHashMap` |

As you can see from the table, the Java Collections Framework provides
several general-purpose implementations of the
[`Set`](http://download.oracle.com/javase/7/docs/api/java/util/Set.html),
[`List`](http://download.oracle.com/javase/7/docs/api/java/util/List.html)
, and
[`Map`](http://download.oracle.com/javase/7/docs/api/java/util/Map.html) interfaces. In each case, one implementation —
[`HashSet`](http://download.oracle.com/javase/7/docs/api/java/util/HashSet.html),
[`ArrayList`](http://download.oracle.com/javase/7/docs/api/java/util/ArrayList.html), and
[`HashMap`](http://download.oracle.com/javase/7/docs/api/java/util/HashMap.html) — is clearly the one to use for most applications,
all other things being equal. Note that the
[`SortedSet`](http://download.oracle.com/javase/7/docs/api/java/util/SortedSet.html) and the
[`SortedMap`](http://download.oracle.com/javase/7/docs/api/java/util/SortedMap.html) interfaces do not have rows in the table.
Each of those interfaces has one implementation (
[`TreeSet`](http://download.oracle.com/javase/7/docs/api/java/util/TreeSet.html) and
[`TreeMap`](http://download.oracle.com/javase/7/docs/api/java/util/TreeMap.html)) and is listed in the `Set` and the `Map` rows.
There are two general-purpose `Queue` implementations —
[`LinkedList`](http://download.oracle.com/javase/7/docs/api/java/util/LinkedList.html), which is also a `List` implementation, and
[`PriorityQueue`](http://download.oracle.com/javase/7/docs/api/java/util/PriorityQueue.html), which is omitted from the table. These two implementations provide
very different semantics: `LinkedList` provides
FIFO semantics, while `PriorityQueue`
orders its elements according to their values.

Each of the general-purpose implementations provides all optional operations contained in its interface. All permit `null` elements,
keys, and values. None are synchronized (thread-safe). All have
*fail-fast iterators*, which detect illegal concurrent
modification during iteration and fail quickly and cleanly rather
than risking arbitrary, nondeterministic behavior at an undetermined
time in the future. All are `Serializable` and all support
a public `clone` method.

The fact that these implementations are unsynchronized represents a
break with the past: The legacy collections `Vector` and
`Hashtable` are synchronized. The present approach was taken
because collections are frequently used when the synchronization is
of no benefit. Such uses include single-threaded use, read-only use,
and use as part of a larger data object that does its own synchronization.
In general, it is good API design practice not to make users pay
for a feature they don't use. Furthermore, unnecessary synchronization
can result in deadlock under certain circumstances.

If you need thread-safe collections, the synchronization wrappers,
described in the
[Wrapper Implementations](wrapper.html) section, allow *any* collection to be transformed into a
synchronized collection. Thus, synchronization is optional for
general-purpose implementations, whereas it is mandatory for
legacy implementations. Moreover, the `java.util.concurrent`
package provides concurrent implementations of the `BlockingQueue`
interface, which extends `Queue`, and of the `ConcurrentMap`
interface, which extends `Map`. These implementations offer
much higher concurrency than mere synchronized implementations.

As a rule, you should be thinking about the interfaces,
*not* the implementations. That is why there are no programming examples
in this section. For the most part, the choice of implementation
affects only performance. The preferred style, as mentioned in the
[Interfaces](../interfaces/index.html) section, is to choose an implementation when a `Collection` is created and
to immediately assign the new collection to a variable of the
corresponding interface type (or to pass the collection to a
method expecting an argument of the interface type). In this way,
the program does not become dependent on any added methods in a given
implementation, leaving the programmer free to change implementations
anytime that it is warranted by performance concerns or behavioral details.

The sections that follow briefly discuss the implementations. The performance of
the implementations is described using words such as
*constant-time*, *log*, *linear*,
*n log(n)*, and *quadratic* to refer
to the asymptotic upper-bound on the time complexity of performing
the operation. All this is quite a mouthful, and it doesn't matter
much if you don't know what it means. If you're interested in knowing more,
refer to any good algorithms textbook. One thing to keep in mind
is that this sort of performance metric has its limitations.
Sometimes, the nominally slower implementation may be faster.
When in doubt, measure the performance!

[« Previous](../interfaces/index.html)
•
[Trail](../TOC.html)
•
[Next »](set.html)

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

**Previous page:** Previous Lesson
  
**Next page:** Set Implementations




A browser with JavaScript enabled is required for this page to operate properly.