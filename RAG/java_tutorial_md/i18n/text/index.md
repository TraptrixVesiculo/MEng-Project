[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

Working with Text

[Checking Character Properties](charintro.html)

[Comparing Strings](collationintro.html)

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

**Trail:** Internationalization

[Home Page](../../index.html)
>
[Internationalization](../index.html)

[« Previous](../format/index.html) • [Trail](../TOC.html) • [Next »](charintro.html)

# Lesson: Working with Text

Nearly all programs with user interfaces manipulate text. In an
international market the text your programs display must conform to the
rules of languages from around the world. The Java programming language
provides a number of classes that help you handle text in a
locale-independent manner.

### [Checking Character Properties](charintro.html)

> This section explains how to use the
> `Character` comparison methods
> to check character properties for all major languages.

### [Comparing Strings](collationintro.html)

> In this section you'll learn how to perform locale-independent string
> comparisons with the `Collator` class.

### [Detecting Text Boundaries](boundaryintro.html)

> This section shows how the
> `BreakIterator` class
> can detect character, word, sentence, and line boundaries.

### [Converting Non-Unicode Text](convertintro.html)

> Different computer systems around the world store text in a variety of
> encoding schemes. This section describes the classes that help you
> convert text between Unicode and other encodings.

### [Normalizer's API](normalizerapi.html)

> This section explains how to use the Normalizer's API to transform
> text applying different normalization forms.

[« Previous](../format/index.html)
•
[Trail](../TOC.html)
•
[Next »](charintro.html)

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
  
**Next page:** Checking Character Properties




A browser with JavaScript enabled is required for this page to operate properly.