[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Bonus
  
**Lesson:** Generics

[Generics](index.html)

Introduction

[Defining Simple Generics](simple.html)

[Generics and Subtyping](subtype.html)

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

[« Previous](index.html) • [Trail](../TOC.html) • [Next »](simple.html)

# Introduction

JDK 5.0 introduces several new extensions to the Java programming language.
One of these is the introduction of *generics*.

This trail is an introduction to generics.
You may be familiar with similar constructs from other languages, most
notably C++ templates. If so, you'll see that there are both similarities
and important differences. If you are unfamiliar with look-a-alike
constructs from elsewhere, all the better; you can start fresh,
without having to unlearn any misconceptions.

Generics allow you to abstract over types. The most common examples are
container types, such as those in the Collections hierarchy.

Here is a typical usage of that sort:

```

List myIntList = new LinkedList(); // 1
myIntList.add(new Integer(0)); // 2
Integer x = (Integer) myIntList.iterator().next();  // 3        

```

The cast on line 3 is slightly annoying. Typically, the programmer knows what
kind of data has been placed into a particular list.
However, the cast is essential. The
compiler can only guarantee that an `Object` will be returned by the
iterator. To ensure the assignment to a variable of type `Integer` is
type safe, the cast is required.

Of course, the cast not only introduces clutter. It also introduces the
possibility of a run time error, since the programmer may be
mistaken.

What if programmers could actually express their intent, and mark
a list as being restricted to contain a particular data type? This is
the core idea behind generics. Here is a version of the program fragment given
above using generics:

```

List<Integer> myIntList = new LinkedList<Integer>(); // 1'
myIntList.add(new Integer(0)); // 2'
Integer x = myIntList.iterator().next(); // 3'

```

Notice the type declaration for the variable `myIntList`. It specifies
that this is not just an arbitrary `List`, but a `List` of
`Integer`,
written `List<Integer>`. We say that `List` is a generic
interface that
takes a *type parameter*--in this case, `Integer`. We also specify
a type parameter when creating the list object.

Note, too, that the cast on line 3' is gone.

Now, you might think that all we've accomplished is to move the clutter
around. Instead of a cast to `Integer` on line 3, we have
`Integer` as
a type parameter on line 1'. However, there is a very big difference
here. The compiler can now check the type correctness of the program
at compile-time. When we say that `myIntList` is declared with
type `List<Integer>`,
this tells us something about the variable `myIntList`, which holds true
wherever and whenever it is used, and the compiler will guarantee it.
In contrast, the cast tells us something the programmer thinks is true
at a single point in the code.

The net effect, especially in large programs, is improved readability and
robustness.

[« Previous](index.html)
•
[Trail](../TOC.html)
•
[Next »](simple.html)

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

**Previous page:** Generics
  
**Next page:** Defining Simple Generics




A browser with JavaScript enabled is required for this page to operate properly.