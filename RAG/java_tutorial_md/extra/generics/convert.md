[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Bonus
  
**Lesson:** Generics

[Generics](index.html)

[Introduction](intro.html)

[Defining Simple Generics](simple.html)

[Generics and Subtyping](subtype.html)

[Wildcards](wildcards.html)

[Generic Methods](methods.html)

[Interoperating with Legacy Code](legacy.html)

[The Fine Print](fineprint.html)

[Class Literals as Runtime-Type Tokens](literals.html)

[More Fun with Wildcards](morefun.html)

Converting Legacy Code to Use Generics

[Acknowledgements](acknowledgements.html)

[Home Page](../../index.html)
>
[Bonus](../index.html)
>
[Generics](index.html)

[« Previous](morefun.html) • [Trail](../TOC.html) • [Next »](acknowledgements.html)

# Converting Legacy Code to Use Generics

Earlier, we showed how new and legacy code can interoperate. Now, it's
time to look at the harder problem of "generifying" old code.

If you decide to convert old code to use generics, you need to think
carefully about how you modify the API.

You need to make certain that the generic API is not unduly restrictive;
it must continue to support the original contract of the API.
Consider again some examples from `java.util.Collection`. The pre-generic
API looks like:

```

interface Collection {
    public boolean containsAll(Collection c);
    public boolean addAll(Collection c);
}

```

A naive attempt to generify it would be the following:

```

interface Collection<E> {

    public boolean containsAll(Collection<E> c);
    public boolean addAll(Collection<E> c);
}

```

While this is certainly type safe, it doesn't live up to the API's original
contract. The `containsAll()` method works with any kind of
incoming collection. It will only succeed if the incoming collection
really contains only instances of `E`, but:

* The static type of the incoming collection might differ, perhaps because
  the caller doesn't know the precise type of the collection being passed in,
  or perhaps because it is a `Collection<S>`,where `S` is a
  subtype of
  `E`.* It's perfectly legitimate to call `containsAll()` with a
    collection of a different type. The routine should work, returning
    `false`.

In the case of `addAll()`, we should be able to add any collection
that consists of instances of a subtype of `E`. We saw how to
handle this situation correctly in section
[Generic Methods](methods.html).

You also need to ensure that the revised
API retains binary compatibility with old clients. This implies that the
erasure of the API must be the same as the original, ungenerified API. In most
cases, this falls out naturally, but there are some subtle cases. We'll
examine one of the subtlest cases we've encountered,
the method `Collections.max()`.
As we saw in section
[More Fun with Wildcards](morefun.html), a plausible signature for `max()` is:

```

public static <T extends Comparable<? super T>> 
        T max(Collection<T> coll)

```

This is fine, except that the erasure of this signature is:

```

public static Comparable max(Collection coll)

```

which is different than the original signature of `max()`:

```

public static Object max(Collection coll)

```

One could
certainly have specified this signature for `max()`, but it was not
done, and all the old binary class files that call `Collections.max()`
depend on a signature that returns `Object`.

We can force the erasure to be different, by explicitly specifying a
superclass in the bound for the formal type parameter `T`.

```

public static <T extends Object & Comparable<? super T>> 
        T max(Collection<T> coll)

```

This is an example of giving *multiple bounds* for a type parameter, using the syntax
`T1 & T2 ... & Tn`. A type variable with multiple bounds is known to be a subtype of all
of the types listed in the bound. When a multiple bound is used, the first type mentioned in
the bound is used as the erasure of the type variable.

Finally, we should recall that `max` only reads from its input
collection, and so is applicable to collections of any subtype of `T`.

This brings
us to the actual signature used in the JDK:

```

public static <T extends Object & Comparable<? super T>> 
        T max(Collection<? extends T> coll)

```

It's very rare that anything so involved comes up in practice, but expert
library designers should be prepared to think very carefully when
converting existing APIs.

Another issue to watch out for is *covariant returns*, that is, refining
the return type of a method in a subclass. You should not take advantage
of this feature in an old API. To see why, let's look at an example.

Assume your original API was of the form:

```

public class Foo {
    public Foo create() {
        ...
    } // Factory. Should create an instance of whatever class it is declared in.
}

public class Bar extends Foo {
    public Foo create() {
        ...
    } // Actually creates a Bar.
}

```

Taking advantage of covariant returns, you modify it to:

```

public class Foo {
    public Foo create() {
        ...
    } // Factory. Should create an instance of whatever class it is declared in.
}

public class Bar extends Foo {
    public Bar create() {
        ...
    } // Actually creates a Bar.
}

```

Now, assume a third party client of your code wrote the following:

```

public class Baz extends Bar {
    public Foo create() {
        ...
    } // Actually creates a Baz.
}

```

The Java virtual machine does not directly support overriding of methods
with different return types. This feature is supported by the compiler.
Consequently, unless the class `Baz` is recompiled,
it will not properly override the `create()` method of
`Bar`. Furthermore, `Baz` will
have to be modified, since the code will be rejected as written--the
return type of `create()`
in `Baz` is not a subtype of the return type of `create()`
in `Bar`.

[« Previous](morefun.html)
•
[Trail](../TOC.html)
•
[Next »](acknowledgements.html)

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

**Previous page:** More Fun with Wildcards
  
**Next page:** Acknowledgements




A browser with JavaScript enabled is required for this page to operate properly.