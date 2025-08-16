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

Convenience Implementations

[Summary of Implementations](summary.html)

[Questions and Exercises](QandE/questions.html)

[Home Page](../../index.html)
>
[Collections](../index.html)
>
[Implementations](index.html)

[« Previous](wrapper.html) • [Trail](../TOC.html) • [Next »](summary.html)

# Convenience Implementations

This section describes several mini-implementations that can be more
convenient and more efficient than general-purpose implementations when
you don't need their full power. All the implementations in this section are
made available via static factory methods rather than `public` classes.

### List View of an Array

> The
> [`Arrays.asList`](http://download.oracle.com/javase/7/docs/api/java/util/Arrays.html#asList(T...)) method returns a `List` view of its array argument. Changes to the
> `List` write through to the array and vice versa. The size of the
> collection is that of the array and cannot be changed. If the `add` or
> the `remove` method is called on the `List`, an
> `UnsupportedOperationException` will result.
>
> The normal use of this implementation is as a bridge between array-based and
> collection-based APIs. It allows you to pass an array to a method expecting a
> `Collection` or a `List`. However, this implementation also has
> another use. If you need a fixed-size `List`, it's more efficient than
> any general-purpose `List` implementation. This is the idiom.
>
> ```
>
> List<String> list = Arrays.asList(new String[size]);
>
> ```
>
> Note that a reference to the backing array is not retained.

### Immutable Multiple-Copy List

> Occasionally you'll need an immutable `List` consisting of multiple
> copies of the same element. The
> [`Collections.nCopies`](http://download.oracle.com/javase/7/docs/api/java/util/Collections.html#nCopies(int,%20T)) method returns such a list. This implementation has two main uses.
> The first is to initialize a newly created `List`; for example, suppose you want an `ArrayList` initially consisting of 1,000
> `null` elements. The following incantation does the trick.
>
> ```
>
> List<Type> list =
>     new ArrayList<Type>(Collections.nCopies(1000, (Type)null);
>
> ```
>
> Of course, the initial value of each element need not be `null`. The
> second main use is to grow an existing `List`. For example, suppose you want to add 69 copies of the string `"fruit bat"` to the end of a
> `List<String>`. It's not clear why you'd want to do such a
> thing, but let's just suppose you did. The following is how you'd do it.
>
> ```
>
> lovablePets.addAll(Collections.nCopies(69, "fruit bat"));
>
> ```
>
> By using the form of `addAll` that takes both an index and a
> `Collection`, you can add the new elements to the middle of a
> `List` instead of to the end of it.

### Immutable Singleton Set

> Sometimes you'll need an immutable *singleton* `Set`,
> which consists of a single, specified element. The
> [`Collections.singleton`](http://download.oracle.com/javase/7/docs/api/java/util/Collections.html#singleton(T)) method returns such a `Set`. One use of this implementation is to
> remove all occurrences of a specified element from a `Collection`.
>
> ```
>
> c.removeAll(Collections.singleton(e));
>
> ```
>
> A related idiom removes all elements that map to a
> specified value from a `Map`. For example, suppose you have a `Map` — `job` — that maps people to their line of work and suppose you want to eliminate all the lawyers. The following one-liner will do the deed.
>
> ```
>
> job.values().removeAll(Collections.singleton(LAWYER));
>
> ```
>
> One more use of this implementation is to provide a single input value to a
> method that is written to accept a collection of values.

### Empty Set, List, and Map Constants

> The
> [`Collections`](http://download.oracle.com/javase/7/docs/api/java/util/Collections.html) class provides methods to return the empty
> `Set`, `List`, and `Map` —
> [`emptySet`](http://download.oracle.com/javase/7/docs/api/java/util/Collections.html#emptySet()),
> [`emptyList`](http://download.oracle.com/javase/7/docs/api/java/util/Collections.html#emptyList()), and
> [`emptyMap`](http://download.oracle.com/javase/7/docs/api/java/util/Collections.html#emptyMap()).
> The main use of these constants is
> as input to methods that take a `Collection` of values when you don't
> want to provide any values at all, as in this example.
>
> ```
>
> tourist.declarePurchases(Collections.emptySet());
>
> ```

[« Previous](wrapper.html)
•
[Trail](../TOC.html)
•
[Next »](summary.html)

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

**Previous page:** Wrapper Implementations
  
**Next page:** Summary of Implementations




A browser with JavaScript enabled is required for this page to operate properly.