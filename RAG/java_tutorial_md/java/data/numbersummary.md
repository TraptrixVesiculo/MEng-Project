[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Learning the Java Language
  
**Lesson:** Numbers and Strings
  
**Section:** Numbers

[Numbers and Strings](index.html)

[Numbers](numbers.html)

[The Numbers Classes](numberclasses.html)

[Formatting Numeric Print Output](numberformat.html)

[Beyond Basic Arithmetic](beyondmath.html)

Summary of Numbers

[Questions and Exercises](QandE/numbers-questions.html)

[Characters](characters.html)

[Strings](strings.html)

[Converting Between Numbers and Strings](converting.html)

[Manipulating Characters in a String](manipstrings.html)

[Comparing Strings and Portions of Strings](comparestrings.html)

[The StringBuilder Class](buffers.html)

[Summary of Characters and Strings](stringsummary.html)

[Questions and Exercises](QandE/characters-questions.html)

[Home Page](../../index.html)
>
[Learning the Java Language](../index.html)
>
[Numbers and Strings](index.html)

[« Previous](beyondmath.html) • [Trail](../TOC.html) • [Next »](QandE/numbers-questions.html)

# Summary of Numbers

You use one of the wrapper classes –
`Byte`, `Double`, `Float`,
`Integer`, `Long`, or `Short` –
to wrap a number of primitive type in an object. The Java compiler automatically
wraps (boxes) primitives for you when necessary and unboxes them, again when necessary.

The `Number` classes include constants and useful class methods. The `MIN_VALUE` and
`MAX_VALUE` constants contain the smallest and largest values
that can be contained by an object of that type.
The `byteValue`, `shortValue`,
and similar methods convert one numeric type to another.
The `valueOf` method converts a string to a number,
and the `toString` method converts a number to a string.

To format a string containing numbers for output, you can use the
`printf()` or `format()` methods in the
`PrintStream` class. Alternatively, you can use the `NumberFormat`
class to customize numerical formats using patterns.

The `Math` class contains a variety of class methods
for performing mathematical functions, including exponential, logarithmic,
and trigonometric methods. `Math` also includes basic arithmetic functions, such as
absolute value and rounding, and a method, `random()`,
for generating random numbers.

[« Previous](beyondmath.html)
•
[Trail](../TOC.html)
•
[Next »](QandE/numbers-questions.html)

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

**Previous page:** Beyond Basic Arithmetic
  
**Next page:** Questions and Exercises: Numbers




A browser with JavaScript enabled is required for this page to operate properly.