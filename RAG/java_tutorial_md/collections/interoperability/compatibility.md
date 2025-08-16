[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Collections
  
**Lesson:** Interoperability

[Interoperability](index.html)

Compatibility

[API Design](api-design.html)

[Home Page](../../index.html)
>
[Collections](../index.html)
>
[Interoperability](index.html)

[« Previous](index.html) • [Trail](../TOC.html) • [Next »](api-design.html)

# Compatibility

The Java Collections Framework was designed to ensure complete
interoperability between the core
[collection interfaces](../interfaces/index.html) and the types that were used to represent collections in the early
versions of the Java platform:
[`Vector`](http://download.oracle.com/javase/7/docs/api/java/util/Vector.html),
[`Hashtable`](http://download.oracle.com/javase/7/docs/api/java/util/Hashtable.html),
[array](../../java/nutsandbolts/arrays.html), and
[`Enumeration`](http://download.oracle.com/javase/7/docs/api/java/util/Enumeration.html). In this section, you'll learn how to transform old collections to the Java
Collections Framework collections and vice versa.

### Upward Compatibility

> Suppose that you're using an API that returns legacy collections in
> tandem with another API that requires objects implementing the
> collection interfaces. To make the two APIs interoperate smoothly,
> you'll have to transform the legacy collections into modern collections.
> Luckily, the Java Collections Framework makes this easy.
>
> Suppose the old API returns an array of objects and the new
> API requires a `Collection`. The Collections Framework
> has a convenience implementation that allows an array of objects
> to be viewed as a `List`. You use
> [`Arrays.asList`](http://download.oracle.com/javase/7/docs/api/java/util/Arrays.html#asList(T...)) to pass an array to any method requiring a `Collection`
> or a `List`.
>
> ```
>
> Foo[] result = oldMethod(arg);
> newMethod(Arrays.asList(result));
>
> ```
>
> If the old API returns a `Vector` or a `Hashtable`,
> you have no work to do at all because `Vector` was retrofitted
> to implement the `List` interface, and `Hashtable`
> was retrofitted to implement `Map`. Therefore, a `Vector`
> may be passed directly to any method calling for a `Collection`
> or a `List`.
>
> ```
>
> Vector result = oldMethod(arg);
> newMethod(result);
>
> ```
>
> Similarly, a `Hashtable` may be passed directly to any method
> calling for a `Map`.
>
> ```
>
> Hashtable result = oldMethod(arg);
> newMethod(result);
>
> ```
>
> Less frequently, an API may return an `Enumeration`
> that represents a collection of objects. The `Collections.list`
> method translates an `Enumeration` into a `Collection`.
>
> ```
>
> Enumeration e = oldMethod(arg);
> newMethod(Collections.list(e));
>
> ```

### Backward Compatibility

> Suppose you're using an API that returns modern collections in
> tandem with another API that requires you to pass in legacy collections.
> To make the two APIs interoperate smoothly, you have to transform modern collections into old collections. Again, the Java Collections
> Framework makes this easy.
>
> Suppose the new API returns a `Collection`,
> and the old API requires an array of `Object`.
> As you're probably aware, the `Collection` interface
> contains a `toArray` method designed expressly for this situation.
>
> ```
>
> Collection c = newMethod();
> oldMethod(c.toArray());
>
> ```
>
> What if the old API requires an array of `String`
> (or another type) instead of an array of `Object`?
> You just use the other form of `toArray` — the one that
> takes an array on input.
>
> ```
>
> Collection c = newMethod();
> oldMethod((String[]) c.toArray(new String[0]));
>
> ```
>
> If the old API requires a `Vector`, the standard collection
> constructor comes in handy.
>
> ```
>
> Collection c = newMethod();
> oldMethod(new Vector(c));
>
> ```
>
> The case where the old API requires a `Hashtable`
> is handled analogously.
>
> ```
>
> Map m = newMethod();
> oldMethod(new Hashtable(m));
>
> ```
>
> Finally, what do you do if the old API requires an `Enumeration`?
> This case isn't common, but it does happen from time to time, and the
> [`Collections.enumeration`](http://download.oracle.com/javase/7/docs/api/java/util/Collections.html#enumeration(java.util.Collection)) method was provided to handle it. This is a static factory method that takes a `Collection` and returns an `Enumeration`
> over the elements of the `Collection`.
>
> ```
>
> Collection c = newMethod();
> oldMethod(Collections.enumeration(c));
>
> ```

[« Previous](index.html)
•
[Trail](../TOC.html)
•
[Next »](api-design.html)

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

**Previous page:** Interoperability
  
**Next page:** API Design




A browser with JavaScript enabled is required for this page to operate properly.