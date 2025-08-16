[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

Regular Expressions

[Introduction](intro.html)

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

**Trail:** Essential Classes

[Home Page](../../index.html)
>
[Essential Classes](../index.html)

[« Previous](../environment/index.html) • [Trail](../TOC.html) • [Next »](intro.html)

# Lesson: Regular Expressions

> This lesson explains how to use the
> `java.util.regex`
> API for pattern matching with regular expressions.
> Although the syntax accepted by this package
> is similar to the
> [Perl](http://www.perl.com)
> programming language,
> knowledge of Perl
> is not a prerequisite.
> This lesson starts with the basics, and
> gradually builds to cover more advanced techniques.
>
> **[Introduction](intro.html)**
> :   Provides a general overview of regular expressions. It
>     also introduces the core classes that comprise this API.
>
> **[Test Harness](test_harness.html)**
> :   Defines a simple application for testing pattern matching with regular expressions.
>
> **[String Literals](literals.html)**
> :   Introduces basic pattern matching, metacharacters,
>     and quoting.
>
> **[Character Classes](char_classes.html)**
> :   Describes simple character classes, negation,
>     ranges, unions, intersections, and subtraction.
>
> **[Predefined Character Classes](pre_char_classes.html)**
> :   Describes the basic predefined character
>     classes for whitespace, word, and digit characters.
>
> **[Quantifiers](quant.html)**
> :   Explains greedy, reluctant, and possessive
>     quantifiers for matching a specified
>     expression *x* number of times.
>
> **[Capturing Groups](groups.html)**
> :   Explains how to treat
>     multiple characters as a single unit.
>
> **[Boundary Matchers](bounds.html)**
> :   Describes line, word, and input boundaries.
>
> **[Methods of the Pattern Class](pattern.html)**
> :   Examines other useful methods of the
>     `Pattern` class, and explores advanced features such
>     as compiling with flags and using embedded flag expressions.
>
> **[Methods of the Matcher Class](matcher.html)**
> :   Describes the commonly-used methods of
>     the `Matcher` class.
>
> **[Methods of the PatternSyntaxException Class](pse.html)**
> :   Describes how to examine a
>     `PatternSyntaxException`.
>
> **[Additional Resources](resources.html)**
> :   To read more about regular expressions,
>     consult this section for additional resources.

[« Previous](../environment/index.html)
•
[Trail](../TOC.html)
•
[Next »](intro.html)

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