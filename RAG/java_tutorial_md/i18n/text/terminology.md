[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Internationalization
  
**Lesson:** Working with Text
  
**Section:** Unicode

[Working with Text](index.html)

[Checking Character Properties](charintro.html)

[Comparing Strings](collationintro.html)

[Performing Locale-Independent Comparisons](locale.html)

[Customizing Collation Rules](rule.html)

[Improving Collation Performance](perform.html)

[Unicode](unicode.html)

Terminology

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

[« Previous](unicode.html) • [Trail](../TOC.html) • [Next »](supplementaryChars.html)

# Terminology

A *character* is a minimal unit of text with no shape or value.

A *character set* is a collection of characters that might
be used by multiple languages. For example, the Latin character set
is used by English and most European languages, though the Greek character
set is used only by the Greek language.

A *coded character set* is a character set where each character
is assigned a unique number.

A *code point* is a value that can be used in a
coded character set. A code point is a 32-bit `int` datat type,
where the lower 21 bits represent a valid code point value and the
upper 11 bits are 0.

A Unicode *code unit* is a 16-bit `char` value.
For example, imagine a `String` that contains the letters
"abc" followed by the Deseret LONG I, which is represented
with two `char` values. That string contains four
characters, four code points, but five code units.

To express a character in Unicode, the hexadecimal value is prefixed
with the string U+.
The valid code point range for the Unicode standard is U+0000
to U+10FFFF, inclusive.
The code point value for the Latin character A is U+0040.
The character € which represents the Euro currency,
has the code point value U+20AC.
The first letter in the Deseret alphabet, the LONG I,
has the code point value U+10400.

The following table shows code point values for several characters:

| Character | Unicode Code Point | Glyph |
| --- | --- | --- |
| Latin A | U+0041 | The Latin character A |
| Latin sharp S | U+00DF | The Latin small letter sharp S |
| Han for East | U+6771 | The Han character for east, eastern or eastward |
| Deseret, LONG I | U+10400 | The Deseret capital letter long I |

As previously described, characters that are in the range U+10000
to U+10FFFF are called supplementary characters.
The set of characters from U+0000 to U+FFFF are sometimes referred to
as the *Basic Multilingual Plane (BMP)*.

More terminology can be found in the *Glossary of Unicode Terms*,
listed on the [More Information](info.html) page.

[« Previous](unicode.html)
•
[Trail](../TOC.html)
•
[Next »](supplementaryChars.html)

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

**Previous page:** Unicode
  
**Next page:** Supplementary Characters as Surrogates




A browser with JavaScript enabled is required for this page to operate properly.