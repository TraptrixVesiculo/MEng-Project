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

[Predefined Character Classes](pre_char_classes.html)

[Quantifiers](quant.html)

[Capturing Groups](groups.html)

[Boundary Matchers](bounds.html)

[Methods of the Pattern Class](pattern.html)

[Methods of the Matcher Class](matcher.html)

[Methods of the PatternSyntaxException Class](pse.html)

Unicode Support

[Additional Resources](resources.html)

[Questions and Exercises](QandE/questions.html)

[Home Page](../../index.html)
>
[Essential Classes](../index.html)
>
[Regular Expressions](index.html)

[« Previous](pse.html) • [Trail](../TOC.html) • [Next »](resources.html)

# Unicode Support

As of the JDK 7 release, Regular Expression pattern matching has expanded
functionality to support Unicode 6.0.

* [Matching a Specific Code Point](#matchingSpecific)* [Unicode Character Properties](#properties)

## Matching a Specific Code Point

You can match a specific Unicode code point using an escape sequence
of the form `\uFFFF`, where `FFFF` is the
hexidecimal value of the code point you want to match. For example,
`\u6771` matches the Han character for east.

Alternatively, you can specify a code point using Perl-style hex notation,
`\x{...}`. For example:

```

String hexPattern = "\x{" + Integer.toHexString(codePoint) + "}";

```

## Unicode Character Properties

Each Unicode character, in addition to its value, has certain attributes,
or properties.
You can match a single character belonging to a particular category
with the expression `\p{prop}`.
You can match a single character *not* belonging to a particular
category with the expression `\P{prop}`.

The three supported property types are scripts, blocks,
and a "general" category.

### Scripts

To determine if a code point belongs to a specific script,
you can either use the `script` keyword, or the
`sc` short form, for example, `\p{script=Hiragana}`.
Alternatively, you can prefix the script name with the string
`Is`, such as `\p{IsHiragana}`.

Valid script names supported by `Pattern`
are those accepted by
[`UnicodeScript.forName`](http://download.oracle.com/javase/7/docs/api/java/lang/Character.UnicodeScript.html#forName(java.lang.String)).

### Blocks

A block can be specified using the `block` keyword, or
the `blk` short form, for example, `\p{block=Mongolian}`.
Alternatively, you can prefix the block name with the string
`In`, such as `\p{InMongolian}`.

Valid block names supported by `Pattern` are those
accepted by
[`UnicodeBlock.forName`](http://download.oracle.com/javase/7/docs/api/java/lang/Character.UnicodeBlock.html#forName(java.lang.String)).

### General Category

Categories can be specified with optional prefix `Is`.
For example, `IsL` matches the category of Unicode letters.
Categories can also be specified by using the
`general_category` keyword, or the short form `gc`.
For example, an uppercase letter can be matched using
`general_category=Lu` or `gc=Lu`.

Supported categories are those of
[The Unicode Standard](http://www.unicode.org/unicode/standard/standard.html) in the version specified by the
[`Character`](http://download.oracle.com/javase/7/docs/api/java/lang/Character.html) class.

[« Previous](pse.html)
•
[Trail](../TOC.html)
•
[Next »](resources.html)

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

**Previous page:** Methods of the PatternSyntaxException Class
  
**Next page:** Additional Resources




A browser with JavaScript enabled is required for this page to operate properly.