[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Internationalization
  
**Lesson:** Working with Text
  
**Section:** Detecting Text Boundaries

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

[Detecting Text Boundaries](boundaryintro.html)

About the BreakIterator Class

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

[« Previous](boundaryintro.html) • [Trail](../TOC.html) • [Next »](char.html)

# About the BreakIterator Class

The `BreakIterator` class is locale-sensitive, because text
boundaries vary with language. For example, the syntax rules for line
breaks are not the same for all languages. To determine which locales
the `BreakIterator` class supports, invoke the
`getAvailableLocales` method, as follows:

```

Locale[] locales = BreakIterator.getAvailableLocales();

```

You can analyze four kinds of boundaries with the
`BreakIterator` class: character, word, sentence, and
potential line break. When instantiating a `BreakIterator`,
you invoke the appropriate factory method:

* `getCharacterInstance`* `getWordInstance`* `getSentenceInstance`* `getLineInstance`

Each instance of `BreakIterator` can detect just one type of
boundary. If you want to locate both character and word boundaries, for
example, you create two separate instances.

A `BreakIterator`
has an imaginary cursor that points to the current boundary in a string
of text. You can move this cursor within the text with the `previous`
and the `next` methods. For example, if you've created a
`BreakIterator`
with `getWordInstance`, the cursor moves to the next word
boundary in the text every time you invoke the `next`
method. The cursor-movement methods return an integer indicating the
position of the boundary. This position is the index of the character
in the text string that would follow the boundary. Like string indexes,
the boundaries are zero-based. The first boundary is at 0, and the last
boundary is the length of the string. The following figure shows the
word boundaries detected by the `next` and `previous`
methods in a line of text:

[![The text ](../../figures/i18n/i18n-4.gif)](../../figures/i18n/i18n-4.gif)  
*This figure has been reduced to fit on the page.   
 Click the image to view it at its natural size.*

You should use the `BreakIterator`
class only with natural-language text. To tokenize a programming
language, use the `StreamTokenizer` class.

The sections that follow give examples for each type of boundary
analysis. The coding examples are from the source code file named
[`BreakIteratorDemo.java`](examples/BreakIteratorDemo.java).

[« Previous](boundaryintro.html)
•
[Trail](../TOC.html)
•
[Next »](char.html)

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

**Previous page:** Detecting Text Boundaries
  
**Next page:** Character Boundaries




A browser with JavaScript enabled is required for this page to operate properly.