[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Internationalization
  
**Lesson:** Working with Text

[Working with Text](index.html)

[Checking Character Properties](charintro.html)

Comparing Strings

[Performing Locale-Independent Comparisons](locale.html)

[Customizing Collation Rules](rule.html)

[Improving Collation Performance](perform.html)

[Unicode](unicode.html)

[Terminology](terminology.html)

[Supplementary Characters as Surrogates](supplementaryChars.html)

[Character and String APIs](characterClass.html)

[Sample Usage](usage.html)

[Design Considerations](design.html)

[More Information](info.html)

[Detecting Text Boundaries](boundaryintro.html)

[About the BreakIterator Class](about.html)

[Character Boundaries](char.html)

[Word Boundaries](word.html)

[Sentence Boundaries](sentence.html)

[Line Boundaries](line.html)

[Converting Latin Digits to Other Unicode Digits](shapedDigits.html)

[Converting Non-Unicode Text](convertintro.html)

[Byte Encodings and Strings](string.html)

[Character and Byte Streams](stream.html)

[Normalizing Text](normalizerapi.html)

[Home Page](../../index.html)
>
[Internationalization](../index.html)
>
[Working with Text](index.html)

[« Previous](charintro.html) • [Trail](../TOC.html) • [Next »](locale.html)

# Comparing Strings

Applications that sort through text perform frequent string
comparisons. For example, a report generator performs string
comparisons when sorting a list of strings in alphabetical order.

If your application audience is limited to people who speak English,
you can probably perform string comparisons with the
`String.compareTo`  method. The
`String.compareTo` method performs a binary comparison of
the Unicode characters within the two strings. For most languages,
however, this binary comparison cannot be relied on to sort strings,
because the Unicode values do not correspond to the relative order of
the characters.

Fortunately the
[`Collator`](http://download.oracle.com/javase/7/docs/api/java/text/Collator.html) class allows your application to perform string comparisons for
different languages. In this section, you'll learn how to use the
`Collator` class when sorting text.

### [Performing Locale-Independent Comparisons](locale.html)

> Collation rules define the sort sequence of strings.
> These rules vary with locale,
> because various natural languages sort words differently.
> Using the predefined collation rules provided by the
> `Collator` class, you can sort strings
> in a locale-independent manner.

### [Customizing Collation Rules](rule.html)

> In some cases, the predefined collation rules provided by
> the `Collator` class may not work for you.
> For example, you may want to sort strings in
> a language whose locale is not supported
> by `Collator`.
> In this situation,
> you can define your own collation rules, and assign them
> to a `RuleBasedCollator` object.

### [Improving Collation Performance](perform.html)

> With the `CollationKey` class,
> you may
> increase the efficiency of string comparisons.
> This class converts `String` objects to sort keys that
> follow the rules of a given `Collator`.

[« Previous](charintro.html)
•
[Trail](../TOC.html)
•
[Next »](locale.html)

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

**Previous page:** Checking Character Properties
  
**Next page:** Performing Locale-Independent Comparisons




A browser with JavaScript enabled is required for this page to operate properly.