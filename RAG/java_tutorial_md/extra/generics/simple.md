[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Bonus
  
**Lesson:** Generics

[Generics](index.html)

[Introduction](intro.html)

Defining Simple Generics

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

[« Previous](intro.html) • [Trail](../TOC.html) • [Next »](subtype.html)

# Defining Simple Generics

Here is
a small excerpt from the definitions of the interfaces
`List` and `Iterator` in package
`java.util`:

```

public interface List <E>{
    void add(E x);
    Iterator<E> iterator();
}

public interface Iterator<E>{
    E next();
    boolean hasNext();
}

```

This code should all be familiar, except for the stuff in angle brackets.
Those are the declarations of the
*formal type parameters* of the interfaces `List` and
`Iterator`.

Type parameters can be used throughout the generic declaration,
pretty much where you would use ordinary types (though there are some
important restrictions; see the section
[The Fine Print](fineprint.html).

In the introduction, we saw *invocations* of the generic type declaration
`List`,
such as `List<Integer>`. In the invocation (usually called
a *parameterized type*), all occurrences of the formal type parameter
(`E` in this case) are replaced by the *actual type argument*
(in this case, `Integer`).

You might imagine that `List<Integer>` stands for
a version of `List` where `E` has been uniformly replaced
by `Integer`:

```

public interface IntegerList {
    void add(Integer x);
    Iterator<Integer> iterator();
}

```

This intuition can be helpful, but it's also misleading.

It is helpful, because the parameterized type `List<Integer>`
does indeed have methods that look just like this expansion.

It is misleading, because the declaration
of a generic is never actually expanded in this way.
There aren't multiple copies
of the code--not in source, not in binary, not on disk and not in memory.
If you are a C++ programmer, you'll understand that this is very different
than a C++ template.

A generic type declaration is compiled once and for all, and turned into
a single class file, just like an ordinary class or interface
declaration.

Type parameters are analogous to the ordinary parameters used in methods or
constructors.
Much like a method has *formal value parameters* that describe the
kinds of values it operates on, a generic declaration has formal
type parameters. When a method is invoked, *actual arguments* are
substituted for the formal parameters, and the method body is evaluated.
When a generic declaration is invoked, the actual type arguments are
substituted for the formal type parameters.

A note on naming conventions. We recommend that you use pithy
(single character if possible) yet evocative names for formal
type parameters. It's best to avoid lower case characters in those names,
making it easy to distinguish formal type parameters from ordinary classes
and interfaces.
Many container types
use `E`, for element, as in the examples above. We'll see some
additional conventions in later examples.

[« Previous](intro.html)
•
[Trail](../TOC.html)
•
[Next »](subtype.html)

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

**Previous page:** Introduction
  
**Next page:** Generics and Subtyping




A browser with JavaScript enabled is required for this page to operate properly.