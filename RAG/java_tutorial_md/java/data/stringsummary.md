[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Learning the Java Language
  
**Lesson:** Numbers and Strings
  
**Section:** Strings

[Numbers and Strings](index.html)

[Numbers](numbers.html)

[The Numbers Classes](numberclasses.html)

[Formatting Numeric Print Output](numberformat.html)

[Beyond Basic Arithmetic](beyondmath.html)

[Summary of Numbers](numbersummary.html)

[Questions and Exercises](QandE/numbers-questions.html)

[Characters](characters.html)

[Strings](strings.html)

[Converting Between Numbers and Strings](converting.html)

[Manipulating Characters in a String](manipstrings.html)

[Comparing Strings and Portions of Strings](comparestrings.html)

[The StringBuilder Class](buffers.html)

Summary of Characters and Strings

[Questions and Exercises](QandE/characters-questions.html)

[Home Page](../../index.html)
>
[Learning the Java Language](../index.html)
>
[Numbers and Strings](index.html)

[« Previous](buffers.html) • [Trail](../TOC.html) • [Next »](QandE/characters-questions.html)

# Summary of Characters and Strings

Most of the time, if you are using a single character value, you will
use the primitive `char` type. There are times, however, when
you need to use a char as an object—for example, as a
method argument where an object is expected. The Java programming
language provides a *wrapper* class that "wraps" the `char`
in a `Character` object for this purpose. An object of type `Character` contains a single field
whose type is `char`.
This
[`Character`](http://download.oracle.com/javase/7/docs/api/java/lang/Character.html) class also offers a number of useful class (i.e., static) methods for manipulating characters.

Strings are a sequence of characters and are widely used in Java programming.
In the Java programming language, strings are objects. The
[`String`](http://download.oracle.com/javase/7/docs/api/java/lang/String.html)  class has over 60 methods and 13 constructors.

Most commonly, you create a string with a statement like

```

String s = "Hello world!";

```

rather than using one of the `String` constructors.

The `String` class has many methods to find and retrieve substrings; these can then
be easily reassembled into new strings using the `+` concatenation operator.

The `String` class also includes a number of utility methods,
among them `split()`, `toLowerCase()`,
`toUpperCase()`, and `valueOf()`.
The latter method is indispensable in converting user input strings to numbers. The `Number`
subclasses also have methods for converting strings to numbers and vice versa.

In addition to the `String` class, there is also a
[`StringBuilder`](http://download.oracle.com/javase/7/docs/api/java/lang/StringBuilder.html)  class. Working with `StringBuilder` objects can sometimes be more efficient than
working with strings. The `StringBuilder` class
offers a few methods that can be useful for strings, among them `reverse()`.
In general, however, the `String` class has a wider variety of methods.

A string can be converted to a string builder using a `StringBuilder` constructor.
A string builder can be converted to a string with the `toString()` method.

[« Previous](buffers.html)
•
[Trail](../TOC.html)
•
[Next »](QandE/characters-questions.html)

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

**Previous page:** The StringBuilder Class
  
**Next page:** Questions and Exercises: Characters and Strings




A browser with JavaScript enabled is required for this page to operate properly.