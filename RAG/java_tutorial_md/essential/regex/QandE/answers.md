[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../../search.html)

**Trail:** Essential Classes
  
**Lesson:** Regular Expressions

[Home Page](../../../index.html)
>
[Essential Classes](../../index.html)
>
[Regular Expressions](../index.html)

[« Previous](../QandE/questions.html) • [TOC](../../TOC.html)

# Answers to Questions and Exercises:

### Questions

> 1. Question:
>    What are the three public classes in the `java.util.regex`
>    package? Describe the purpose of each.
>
>    Answer:
>    * `Pattern` instances are compiled representations
>      of regular expressions.* `Matcher` instances are engines that interpret
>        patterns and perform match operations against input strings.* `PatternSyntaxException` defines an unchecked
>          exception indicating a syntax error in a regular expression.
>
>    - Question:
>      Consider the string literal `"foo"`. What is the
>      start index? What is the end index? Explain what these numbers
>      mean.
>
>      Answer:
>      Each character in the string resides in its own cell. Index
>      positions point between cells. The string `"foo"`
>      starts at index 0 and ends at index 3, even though the characters
>      only occupy cells 0, 1, and 2.
>
>      - Question:
>        What is the difference between an ordinary character and a
>        metacharacter? Give an example of each.
>
>        Answer:
>        An ordinary character in a regular expression matches itself. A
>        metacharacter is a special character that affects the way a
>        pattern is matched. The letter `A` is an ordinary
>        character. The punctuation mark `.` is a metacharacter
>        that matches any single character.
>
>        - Question:
>          How do you force a metacharacter to act like an ordinary
>          character?
>
>          Answer:
>          There are two ways:
>          * Precede the metacharacter with a backslash
>            (`\`);* Enclose the metacharacter within the quote expressions,
>              `\Q` (at the beginning) and `\E` (at
>              the end).
>
>          - Question:
>            What do you call a set of characters enclosed in square
>            brackets? What is it for?
>
>            Answer:
>            This is a character class. It matches any single character that
>            is in the class of characters specified by the expression between
>            the brackets.
>
>            - Question:
>              Here are three predefined character classes: `\d`,
>              `\s`, and `\w`. Describe each one, and
>              rewrite it using square brackets.
>
>              Answer:
>
>              |  |  |  |
>              | --- | --- | --- |
>              | `\d` | Matches any digit. | `[0-9]` |
>              | `\s` | Matches any white space character. | `[ \t\n-x0B\f\r]` |
>              | `\w` | Matches any word character. | `[a-zA-Z_0-9]` |
>
>              - Question:
>                For each of `\d`, `\s`, and
>                `\w`, write *two* simple expressions that match
>                the *opposite* set of characters.
>
>                Answer:
>
>                |  |  |  |
>                | --- | --- | --- |
>                | `\d` | `\D` | `[^\d]` |
>                | `\s` | `\S` | `[^\s]` |
>                | `\w` | `\W` | `[^\w]` |
>
>                - Question:
>                  Consider the regular expression `(dog){3}`. Identify
>                  the two subexpressions. What string does the expression match?
>
>                  Answer:
>                  The expression consists of a capturing group, `(dog)`,
>                  followed by a greedy quantifier `{3}`. It matches the
>                  string "dogdogdog".

### Exercises

> 1. Exercise:
>    Use a backreference to write an expression that will match a
>    person's name only if that person's first name and last name are the same.
>
>    Solution:
>    `([A-Z][a-zA-Z]*)\s\1`

[« Previous](../QandE/questions.html)
•
[TOC](../../TOC.html)


---

Problems with the examples? Try [Compiling and Running
the Examples: FAQs](../../../information/run-examples.html).
  
Complaints? Compliments? Suggestions? [Give
us your feedback](http://download.oracle.com/javase/feedback.html).

Your use of this page and all the material on pages under "The Java Tutorials" banner,
and all the material on pages under "The Java Tutorials" banner is subject to the [Java SE Tutorial Copyright
and License](../../../information/license.html).
Additionally, any example code contained in any of these Java
Tutorials pages is licensed under the
[Code
Sample License](http://developers.sun.com/license/berkeley_license.html).

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| |  |  | | --- | --- | | duke image | Oracle logo | | [About Oracle](http://www.oracle.com/us/corporate/index.html) | [Oracle Technology Network](http://www.oracle.com/technology/index.html) | [Terms of Service](https://www.samplecode.oracle.com/servlets/CompulsoryClickThrough?type=TermsOfService) | Copyright © 1995, 2011 Oracle and/or its affiliates. All rights reserved. |

**Previous page:** Questions and Exercises: Regular Expressions




A browser with JavaScript enabled is required for this page to operate properly.