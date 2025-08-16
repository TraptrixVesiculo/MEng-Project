[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Collections
  
**Lesson:** Interfaces

[Interfaces](index.html)

[The Collection Interface](collection.html)

[The Set Interface](set.html)

[The List Interface](list.html)

[The Queue Interface](queue.html)

[The Map Interface](map.html)

[Object Ordering](order.html)

[The SortedSet Interface](sorted-set.html)

[The SortedMap Interface](sorted-map.html)

Summary of Interfaces

[Questions and Exercises](QandE/questions.html)

[Home Page](../../index.html)
>
[Collections](../index.html)
>
[Interfaces](index.html)

[« Previous](sorted-map.html) • [Trail](../TOC.html) • [Next »](QandE/questions.html)

# Summary of Interfaces

The core collection interfaces are the foundation of the Java Collections Framework.

The Java Collections Framework hierarchy consists of two distinct interface trees:

* The first tree starts with the `Collection` interface, which provides for the basic functionality used by all collections, such as `add` and `remove` methods. Its subinterfaces — `Set`, `List`, and `Queue` — provide for more specialized collections.

  The `Set` interface does not allow duplicate elements. This can be useful for storing collections such as a deck of cards or student records. The `Set` interface has a subinterface, `SortedSet`, that provides for ordering of elements in the set.

  The `List` interface provides for an ordered collection, for situations in which you need precise control over where each element is inserted. You can retrieve elements from a `List` by their exact position.

  The `Queue` interface enables additional insertion, extraction, and inspection operations. Elements in a `Queue` are typically ordered in on a FIFO basis.
* The second tree starts with the `Map` interface, which maps keys and values similar to a `Hashtable`.

  `Map`'s subinterface, `SortedMap`, maintains its key-value pairs in ascending order or in an order specified by a `Comparator`.

These interfaces allow collections to be manipulated independently of the details of their representation.

[« Previous](sorted-map.html)
•
[Trail](../TOC.html)
•
[Next »](QandE/questions.html)

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

**Previous page:** The SortedMap Interface
  
**Next page:** Questions and Exercises: Interfaces




A browser with JavaScript enabled is required for this page to operate properly.