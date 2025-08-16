[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Internationalization
  
**Lesson:** Working with Text

[Working with Text](index.html)

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

Detecting Text Boundaries

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

[« Previous](info.html) • [Trail](../TOC.html) • [Next »](about.html)

# Detecting Text Boundaries

Applications that manipulate text need to locate boundaries within the
text. For example, consider some of the common functions of a word
processor: highlighting a character, cutting a word, moving the cursor
to the next sentence, and wrapping a word at a line ending. To perform
each of these functions, the word processor must be able to detect the
logical boundaries in the text. Fortunately you don't have to write
your own routines to perform boundary analysis. Instead, you can take
advantage of the methods provided by the
[`BreakIterator`](http://download.oracle.com/javase/7/docs/api/java/text/BreakIterator.html)  class.

### [About the BreakIterator Class](about.html)

> This section
> discusses the instantiation methods and
> the imaginary cursor of the
> `BreakIterator` class.

### [Character Boundaries](char.html)

> In this section you'll learn
> about the difference between user and
> Unicode characters,
> and how to locate user characters
> with a `BreakIterator`.

### [Word Boundaries](word.html)

> If your application needs to select or locate words within text,
> you'll find it helpful to use a `BreakIterator`.

### [Sentence Boundaries](sentence.html)

> Determining sentence boundaries can be
> problematic,
> because of the ambiguous use of
> sentence terminators in many written languages.
> This section examines some of the problems
> you may encounter, and how
> the `BreakIterator` deals with them.

### [Line Boundaries](line.html)

> This section describes how to
> locate potential line breaks
> in a text string
> with a `BreakIterator`.

[« Previous](info.html)
•
[Trail](../TOC.html)
•
[Next »](about.html)

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

**Previous page:** More Information
  
**Next page:** About the BreakIterator Class




A browser with JavaScript enabled is required for this page to operate properly.