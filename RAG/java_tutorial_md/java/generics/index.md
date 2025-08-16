[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

Generics

[Introduction](generics.html)

[Generic Types](gentypes.html)

[Generic Methods and Constructors](genmethods.html)

[Type Inference](gentypeinference.html)

[Bounded Type Parameters](bounded.html)

[Subtyping](subtyping.html)

[Wildcards](wildcards.html)

[Type Erasure](erasure.html)

[Using Non-Reifiable Parameters with Varargs Methods](non-reifiable-varargs-type.html)

[Summary of Generics](summarygenerics.html)

[Questions and Exercises](QandE/generics-questions.html)

**Trail:** Learning the Java Language

[Home Page](../../index.html)
>
[Learning the Java Language](../index.html)

[« Previous](../data/index.html) • [Trail](../TOC.html) • [Next »](generics.html)

# Lesson: Generics

*Generics* are a built-in language feature that will make your
software more reliable. This lesson discusses the following topics:

### [Introduction](generics.html)

> This section explains some common shortcomings associated with non-generic code.
> Specifically, it shows how certain kinds of bugs will crash an application at runtime, since they are not detectable by the compiler.

### [Generic Types](gentypes.html)

> This section explains generic type declarations, type variables, type parameters, and type arguments. It also describes the naming conventions that are specific to generics.

### [Generic Methods and Constructors](genmethods.html)

> This section shows how type parameters can be used to define generic methods and constructors.

### [Type Inference](gentypeinference.html)

> This section describes type inference, which enables you to invoke a generic method as you would an ordinary method, without specifying a type between angle brackets.

### [Bounded Type Parameters](bounded.html)

> This section describes how type parameters can specify an upper bound that limits the kind of types that can be passed in.

### [Subtyping](subtyping.html)

> This section describes how generic subtyping differs from non-generic subtyping.

### [Wildcards](wildcards.html)

> This section continues the discussion of subtyping by describing bounded and unbounded wildcards.

### [Type Erasure](erasure.html)

> This section describes type erasure, raw types, and unchecked warnings.

### [Using Non-Reifiable Parameters with Varargs Methods](non-reifiable-varargs-type.html)

> This section describes the consequences type erasure has that are related to variable arguments (also known as varargs) methods that use generic types as parameters.

[« Previous](../data/index.html)
•
[Trail](../TOC.html)
•
[Next »](generics.html)

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

**Previous page:** Previous Lesson
  
**Next page:** Introduction




A browser with JavaScript enabled is required for this page to operate properly.