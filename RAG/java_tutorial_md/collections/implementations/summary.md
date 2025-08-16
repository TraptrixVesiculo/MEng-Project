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

[Queue Implementations](queue.html)

[Wrapper Implementations](wrapper.html)

[Convenience Implementations](convenience.html)

Summary of Implementations

[Questions and Exercises](QandE/questions.html)

[Home Page](../../index.html)
>
[Collections](../index.html)
>
[Implementations](index.html)

[« Previous](convenience.html) • [Trail](../TOC.html) • [Next »](QandE/questions.html)

# Summary of Implementations

Implementations are the data objects used to store collections, which
implement the interfaces described in the
[Interfaces lesson](../interfaces/index.html).

The Java Collections Framework provides several general-purpose implementations of the core interfaces:

* For the `Set` interface, `HashSet` is the most commonly used implementation.
* For the `List` interface, `ArrayList` is the most commonly used implementation.
* For the `Map` interface, `HashMap` is the most commonly used implementation.
* For the `Queue` interface, `LinkedList` is the most commonly used implementation.

Each of the general-purpose implementations provides all optional operations contained in its interface.

The Java Collections Framework also provides several special-purpose implementations for situations that require nonstandard performance, usage restrictions, or other unusual behavior.

The `java.util.concurrent` package contains several collections implementations, which are thread-safe but not governed by a single exclusion lock.

The `Collections` class (as opposed to the `Collection` interface), provides static methods that operate on or return collections, which are known as Wrapper implementations.

Finally, there are several Convenience implementations, which can be more efficient than general-purpose implementations when you don't need their full power. The Convenience implementations are made available through static factory methods.

[« Previous](convenience.html)
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

**Previous page:** Convenience Implementations
  
**Next page:** Questions and Exercises: Implementations




A browser with JavaScript enabled is required for this page to operate properly.