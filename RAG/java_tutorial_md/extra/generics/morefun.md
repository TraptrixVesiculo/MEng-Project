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

More Fun with Wildcards

[Converting Legacy Code to Use Generics](convert.html)

[Acknowledgements](acknowledgements.html)

[Home Page](../../index.html)
>
[Bonus](../index.html)
>
[Generics](index.html)

[« Previous](literals.html) • [Trail](../TOC.html) • [Next »](convert.html)

# More Fun with Wildcards

In this section, we'll consider some of the more advanced uses of
wildcards. We've seen several examples where bounded wildcards were useful
when reading from a data structure. Now consider the inverse, a write-only
data structure.
The interface `Sink` is a simple example of this sort.

```

interface Sink<T> {
    flush(T t);
}

```

We can imagine using it as demonstrated by the code below. The method
`writeAll()` is designed to flush all elements of the collection
`coll` to the sink `snk`, and return the last element
flushed.

```

public static <T> T writeAll(Collection<T> coll, Sink<T> snk) {
    T last;
    for (T t : coll) {
        last = t;
        snk.flush(last);
    }
    return last;
}
...
Sink<Object> s;
Collection<String> cs;
String str = writeAll(cs, s); // Illegal call.

```

As written, the call to `writeAll()` is illegal, as no valid type
argument can be inferred; neither `String` nor `Object` are
appropriate types for `T`, because the `Collection`
element and the `Sink` element must be of the same type.

We can fix this error by modifying the signature of `writeAll()` as
shown below, using a wildcard.

```

public static <T> T writeAll(Collection<? extends T>, Sink<T>) {...}
...
String str = writeAll(cs, s); // Call is OK, but wrong return type. 

```

The call is now legal, but the assignment is erroneous, since
the return type inferred is `Object` because `T`
matches the element type of `s`, which
is `Object`.

The solution is to use
a form of bounded wildcard we haven't seen yet: wildcards with a
*lower bound*. The syntax `? super T` denotes an unknown type
that is a supertype of `T` (or `T` itself; remember that
the supertype relation is reflexive). It is the dual of the bounded
wildcards we've been using, where we use `? extends T` to
denote an unknown type that is a subtype of `T`.

```

public static <T> T writeAll(Collection<T> coll, Sink<? super T> snk) {
    ...
}
String str = writeAll(cs, s); // Yes! 

```

Using this syntax, the call is legal, and the inferred type is
`String`, as desired.

Now let's turn to a more realistic example. A `java.util.TreeSet<E>`
represents a tree of elements of type `E` that are
ordered. One way to construct a
`TreeSet` is to pass a `Comparator` object to the constructor.
That comparator will be used to sort the elements of the `TreeSet` according to
a desired ordering.

```

TreeSet(Comparator<E> c) 

```

The `Comparator` interface is essentially:

```

interface Comparator<T> {
    int compare(T fst, T snd);
}

```

Suppose we want to create a `TreeSet<String>` and pass in a suitable
comparator, We need to pass it a `Comparator` that can compare
`String`s.
This can be done by a `Comparator<String>`, but a
`Comparator<Object>` will do just as well. However, we won't be able
to invoke the constructor given above on a `Comparator<Object>`.
We can use a lower bounded wildcard to get the flexibility we want:

```

TreeSet(Comparator<? super E> c) 

```

This code allows any applicable comparator to be used.

As a final example of using lower bounded wildcards, lets look at
the method `Collections.max()`, which returns the maximal element
in a collection passed to it as an argument.
Now, in order for `max()` to work, all elements of the collection
being passed in must implement `Comparable`. Furthermore,
they must all be comparable to *each other*.

A first attempt at generifying this method signature yields:

```

public static <T extends Comparable<T>> 
        T max(Collection<T> coll)

```

That is, the method takes a collection of some type `T` that is comparable
to itself, and returns an element of that type.
However, this code turns out to be too restrictive.
To see why, consider a type that is comparable to arbitrary objects:

```

class Foo implements Comparable<Object> {
    ...
}
Collection<Foo> cf = ... ;
Collections.max(cf); // Should work.

```

Every element of `cf` is comparable to every other element in `cf`,
since every such element is a `Foo`, which is comparable to any
object, and in particular to another `Foo`. However, using the
signature above, we find that the call is rejected. The inferred type
must be `Foo`, but `Foo` does not
implement `Comparable<Foo>`.

It isn't necessary that `T` be comparable
to **exactly** itself. All that's required is that `T` be comparable to
one of its supertypes. This give us:

```

public static <T extends Comparable<? super T>> 
        T max(Collection<T> coll)

```

Note that the actual signature of `Collections.max()` is more involved. We return
to it in the next section,
[Converting Legacy Code to Use Generics](convert.html).
This reasoning applies to almost any usage of `Comparable` that
is intended to work for arbitrary types:
You always want to use `Comparable<? super T>`.

In general, if you have an API that only uses a type parameter `T`
as an argument,
its uses should take advantage of lower bounded wildcards (`? super T`).
Conversely, if
the API only returns `T`, you'll give your clients
more flexibility by using
upper bounded wildcards (`? extends T`).

#### Wildcard Capture

It should be pretty clear by now that given:

```

Set<?> unknownSet = new HashSet<String>();
...
/** Add an element  t to a Set s. */ 
public static <T> void addToSet(Set<T> s, T t) {
    ...
}

```

The call below is illegal.

```

addToSet(unknownSet, "abc"); // Illegal.

```

It makes no difference that the actual set being passed is a set of strings;
what matters is that the expression being passed as an argument is a set of
an unknown type, which cannot be guaranteed to be a set of strings, or of
any type in particular.

Now, consider the following code:

```

class Collections {
    ...
    <T> public static Set<T> unmodifiableSet(Set<T> set) {
        ...
    }
}
...
Set<?> s = Collections.unmodifiableSet(unknownSet); // This works! Why?

```

It seems this should not be allowed; yet, looking at this specific call,
it is perfectly
safe to permit it. After all, `unmodifiableSet()` does work for any
kind of `Set`, regardless of its element type.

Because this situation arises relatively frequently, there is a special
rule that allows such code under very specific circumstances in which
the code can be proven to be safe. This rule, known as
*wildcard capture*, allows the compiler
to infer the unknown type of a wildcard as a type argument to a generic method.

[« Previous](literals.html)
•
[Trail](../TOC.html)
•
[Next »](convert.html)

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

**Previous page:** Class Literals as Runtime-Type Tokens
  
**Next page:** Converting Legacy Code to Use Generics




A browser with JavaScript enabled is required for this page to operate properly.