[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Essential Classes
  
**Lesson:** Regular Expressions

[Regular Expressions](index.html)

[Introduction](intro.html)

[Test Harness](test_harness.html)

[String Literals](literals.html)

[Character Classes](char_classes.html)

Predefined Character Classes

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

[« Previous](char_classes.html) • [Trail](../TOC.html) • [Next »](quant.html)

# Predefined Character Classes

The
[`Pattern`](http://download.oracle.com/javase/7/docs/api/java/util/regex/Pattern.html) API contains a number of useful *predefined character classes*, which offer convenient shorthands
for commonly used regular expressions:
> |  |  |
> | --- | --- |
> | **Predefined Character Classes** | |
> | `.` | Any character (may or may not match line terminators) |
> | `\d` | A digit: `[0-9]` |
> | `\D` | A non-digit: `[^0-9]` |
> | `\s` | A whitespace character: `[ \t\n\x0B\f\r]` |
> | `\S` | A non-whitespace character: `[^\s]` |
> | `\w` | A word character: `[a-zA-Z_0-9]` |
> | `\W` | A non-word character: `[^\w]` |

In the table above, each construct in the left-hand column
is shorthand for the character class in the right-hand column.
For example, `\d` means a range of digits (0-9), and `\w`
means a word character (any lowercase letter, any uppercase letter, the underscore character, or any digit).
Use the predefined classes whenever possible. They make your
code easier to read and eliminate errors introduced
by malformed character classes.

Constructs beginning
with a backslash are called *escaped constructs*. We previewed
escaped constructs in the
[String Literals](literals.html) section where we mentioned the use of backslash and `\Q` and `\E`
for quotation. If you are using an
escaped construct within a string literal, you must preceed
the backslash with another backslash for the string to compile.
For example:

```
 
private final String REGEX = "\\d"; // a single digit

```

In this example `\d` is the regular expression; the extra backslash
is required for the code to compile.
The test harness reads the expressions directly from the `Console`, however, so
the extra backslash is unnecessary.

The following examples demonstrate the use of predefined
character classes.

```
 
Enter your regex: .
Enter input string to search: @
I found the text "@" starting at index 0 and ending at index 1.

Enter your regex: . 
Enter input string to search: 1
I found the text "1" starting at index 0 and ending at index 1.

Enter your regex: .
Enter input string to search: a
I found the text "a" starting at index 0 and ending at index 1.

Enter your regex: \d
Enter input string to search: 1
I found the text "1" starting at index 0 and ending at index 1.

Enter your regex: \d
Enter input string to search: a
No match found.

Enter your regex: \D
Enter input string to search: 1
No match found.

Enter your regex: \D
Enter input string to search: a
I found the text "a" starting at index 0 and ending at index 1.

Enter your regex: \s
Enter input string to search:  
I found the text " " starting at index 0 and ending at index 1.

Enter your regex: \s
Enter input string to search: a
No match found.

Enter your regex: \S
Enter input string to search:  
No match found.

Enter your regex: \S
Enter input string to search: a
I found the text "a" starting at index 0 and ending at index 1.

Enter your regex: \w
Enter input string to search: a
I found the text "a" starting at index 0 and ending at index 1.

Enter your regex: \w
Enter input string to search: !
No match found.

Enter your regex: \W
Enter input string to search: a
No match found.

Enter your regex: \W
Enter input string to search: !
I found the text "!" starting at index 0 and ending at index 1.

```

In the first three examples, the regular expression is simply `.` (the "dot" metacharacter) that indicates "any character."
Therefore, the match is successful in all three cases (a randomly selected `@` character, a digit, and a letter). The remaining examples each use a single regular expression construct from the [Predefined Character Classes table](#CHART). You can refer to this table
to figure out the logic behind each match:

* `\d` matches all digits* `\s` matches spaces* `\w` matches word characters

Alternatively, a capital letter means the opposite:

* `\D` matches non-digits* `\S` matches non-spaces* `\W` matches non-word characters

[« Previous](char_classes.html)
•
[Trail](../TOC.html)
•
[Next »](quant.html)

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

**Previous page:** Character Classes
  
**Next page:** Quantifiers




A browser with JavaScript enabled is required for this page to operate properly.