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

Generics and Subtyping

[Wildcards](wildcards.html)

[Generic Methods](methods.html)

[Interoperating with Legacy Code](legacy.html)

[The Fine Print](fineprint.html)

[Class Literals as Runtime-Type Tokens](literals.html)

[More Fun with Wildcards](morefun.html)

[Converting Legacy Code to Use Generics](convert.html)

[Acknowledgements](acknowledgements.html)

[Home Page](../../index.html)
>
[Bonus](../index.html)
>
[Generics](index.html)

[« Previous](simple.html) • [Trail](../TOC.html) • [Next »](wildcards.html)

# Generics and Subtyping

Let's test your understanding of generics.
Is the following code snippet legal?

```

List<String> ls = new ArrayList<String>(); // 1
List<Object> lo = ls; // 2 

```

Line 1 is certainly legal. The trickier part of the question is line 2.
This boils down to the question: is a `List` of
`String` a `List` of
`Object`. Most people instinctively answer, "Sure!"

Well, take a look at the next few lines:

```

lo.add(new Object()); // 3
String s = ls.get(0); // 4: Attempts to assign an Object to a String!

```

Here we've aliased `ls` and `lo`.
Accessing `ls`, a list of `String`,
through the alias `lo`, we can insert arbitrary objects into it. As
a result `ls` does not hold just `String`s anymore,
and when we try and
get something out of it, we get a rude surprise.

The Java compiler will prevent this from happening of course. Line 2
will cause a compile time error.

In general, if `Foo` is a subtype (subclass or subinterface) of
`Bar`,
and `G` is some generic type declaration, it is **not** the case
that `G<Foo>` is a subtype of `G<Bar>`.
This is probably the hardest thing
you need to learn about generics, because it goes against our deeply
held intuitions.

We should not assume that collections don't change. Our instinct
may lead us to think of these things as immutable.

For example, if the department of motor vehicles supplies a list
of drivers to the census bureau, this seems reasonable. We think
that a `List<Driver>` is a `List<Person>`, assuming that
`Driver` is a subtype of
`Person`.
In fact, what is being passed is a **copy** of the registry
of drivers. Otherwise, the census bureau could add new people who
are not drivers into the list, corrupting the DMV's records.

To cope with this sort of situation, it's useful to consider
more flexible generic types. The rules we've seen so far are quite restrictive.

[« Previous](simple.html)
•
[Trail](../TOC.html)
•
[Next »](wildcards.html)

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

**Previous page:** Defining Simple Generics
  
**Next page:** Wildcards




A browser with JavaScript enabled is required for this page to operate properly.