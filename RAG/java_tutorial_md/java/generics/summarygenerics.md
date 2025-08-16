[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Learning the Java Language
  
**Lesson:** Generics

[Generics](index.html)

[Introduction](generics.html)

[Generic Types](gentypes.html)

[Generic Methods and Constructors](genmethods.html)

[Type Inference](gentypeinference.html)

[Bounded Type Parameters](bounded.html)

[Subtyping](subtyping.html)

[Wildcards](wildcards.html)

[Type Erasure](erasure.html)

[Using Non-Reifiable Parameters with Varargs Methods](non-reifiable-varargs-type.html)

Summary of Generics

[Questions and Exercises](QandE/generics-questions.html)

[Home Page](../../index.html)
>
[Learning the Java Language](../index.html)
>
[Generics](index.html)

[« Previous](non-reifiable-varargs-type.html) • [Trail](../TOC.html) • [Next »](QandE/generics-questions.html)

# Summary of Generics

This chapter described the following problem: We have a `Box` class, written to be generally useful
so it deals with `Object`s. We need an instance that takes only
`Integer`s. The comments say that only `Integer`s go in, so the programmer
knows this (or should know it), but the compiler doesn't know it.
This means that the compiler can't catch someone erroneously adding a
`String`. When we read the value and cast it to an `Integer` we'll get an
exception, but that's not ideal since the exception may be far removed
from the bug in both space and time:

1. Debugging may be difficult, as the point in the code where the
   exception is thrown may be far removed from the point in the code where
   the error is located.

   - It's always better to catch bugs when compiling than when running.

Specifically, you learned that generic type declarations can include one or more type parameters;
you supply one type argument for each type parameter when you use the generic type.
You also learned that type parameters can be used to define generic methods and constructors. Bounded type parameters limit the kinds of types that can be passed into a type parameter; they can specify an upper bound only. Wildcards
represent unknown types, and they can specify an upper or lower bound.
During compilation, type erasure removes all generic information from a generic class or interface, leaving behind only its raw type. It is possible for generic code and legacy code to interact, but in many cases the compiler will emit a warning telling you to recompile with special flags for more details.

For additional information on this topic, see
[Generics](../../extra/generics/index.html) by Gilad Bracha.

[« Previous](non-reifiable-varargs-type.html)
•
[Trail](../TOC.html)
•
[Next »](QandE/generics-questions.html)

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

**Previous page:** Using Non-Reifiable Parameters with Varargs Methods
  
**Next page:** Questions and Exercises: Generics




A browser with JavaScript enabled is required for this page to operate properly.