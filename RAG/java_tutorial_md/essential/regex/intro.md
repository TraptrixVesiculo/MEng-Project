[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Essential Classes
  
**Lesson:** Regular Expressions

[Regular Expressions](index.html)

Introduction

[Test Harness](test_harness.html)

[String Literals](literals.html)

[Character Classes](char_classes.html)

[Predefined Character Classes](pre_char_classes.html)

[Quantifiers](quant.html)

[Capturing Groups](groups.html)

[Boundary Matchers](bounds.html)

[Methods of the Pattern Class](pattern.html)

[Methods of the Matcher Class](matcher.html)

[Methods of the PatternSyntaxException Class](pse.html)

[Unicode Support](unicode.html)

[Additional Resources](resources.html)

[Questions and Exercises](QandE/questions.html)

[Home Page](../../index.html)
>
[Essential Classes](../index.html)
>
[Regular Expressions](index.html)

[« Previous](index.html) • [Trail](../TOC.html) • [Next »](test_harness.html)

# Introduction

### What Are Regular Expressions?

*Regular expressions* are a way to describe a set of strings
based on common characteristics shared by each string in the set. They
can be used to search, edit, or manipulate text and data.
You must learn a specific syntax to create regular expressions — one that
goes beyond the normal syntax of the Java programming language.
Regular expressions vary in complexity,
but once you understand the basics of how they're constructed, you'll be able to decipher (or create) any regular expression.

This trail teaches the regular expression syntax supported by the
[`java.util.regex`](http://download.oracle.com/javase/7/docs/api/java/util/regex/package-summary.html) API and presents several working examples to illustrate
how the various objects interact.
In the world of regular expressions, there are
many different flavors to choose from, such as
grep, Perl, Tcl, Python, PHP, and awk. The regular expression syntax in
the `java.util.regex` API is most similar to that found in Perl.

### How Are Regular Expressions Represented in This Package?

The `java.util.regex` package primarily consists of three classes:
[`Pattern`](http://download.oracle.com/javase/7/docs/api/java/util/regex/Pattern.html),
[`Matcher`](http://download.oracle.com/javase/7/docs/api/java/util/regex/Matcher.html), and
[`PatternSyntaxException`](http://download.oracle.com/javase/7/docs/api/java/util/regex/PatternSyntaxException.html).

* A `Pattern` object is a compiled representation of a regular expression.
  The `Pattern` class provides no public constructors.
  To create a pattern, you must first invoke one of its `public static
  compile` methods, which will then return a `Pattern` object. These methods accept a regular expression as the first argument;
  the first few lessons of this trail will teach you the required syntax.

  * A `Matcher` object is the engine that interprets the
    pattern and performs match operations against an input string.
    Like the `Pattern` class, `Matcher` defines no public constructors. You obtain a `Matcher` object by invoking
    the `matcher` method on a `Pattern` object.

    * A `PatternSyntaxException` object is an unchecked exception that indicates a syntax error in a regular expression pattern.

The last few lessons of this trail explore each class in
detail. But first, you must understand
how regular expressions are actually constructed. Therefore,
the next section introduces a simple test harness that will be used
repeatedly to
explore their syntax.

[« Previous](index.html)
•
[Trail](../TOC.html)
•
[Next »](test_harness.html)

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

**Previous page:** Regular Expressions
  
**Next page:** Test Harness




A browser with JavaScript enabled is required for this page to operate properly.