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

Unicode

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

[« Previous](perform.html) • [Trail](../TOC.html) • [Next »](terminology.html)

# Unicode

*Unicode* is a computing industry standard designed to consistently
and uniquely encode characters used in written languages throughout the world.
The Unicode standard uses hexadecimal to express a character. For example,
the value 0x0040 represents the Latin character A.
The Unicode standard was initially designed using 16 bits to encode
characters because
the primary machines were 16-bit PCs.

When the specification for the Java language was created,
the Unicode standard was accepted and the `char` primitive
was defined as a 16-bit data type, with characters in
the hexadecimal range from 0x0000 to 0xFFFF.

Because 16-bit encoding supports 216,
(65,536) characters, which is insufficient to define
all characters in use throughout the world, the Unicode standard was
extended to 0x10FFFF, which supports over one million characters.
The definition of a character in the Java programming language could
not be changed from 16 bits to 32 bits without causing millions of Java
applications to no longer run properly. To correct the definition,
a scheme was developed to handle characters that could not be encoded
in 16 bits.

The characters with values that are outside of the 16-bit range,
and within the range from 0x10000 to 0x10FFFF,
are called *supplementary characters* and
are defined as a pair of `char` values.

This lesson includes the following sections:

* [Terminology](terminology.html) –
  Code points and other terms are explained.* [Supplementary Characters as Surrogates](supplementaryChars.html)
    – 16-bit surrogates are used to implement supplementary
    characters, which cannot be implemented as a single primitive `char`
    data type.* [Character and String API](characterClass.html)
      – A listing of related API for the `Character`,
      `String`, and related classes.* [Sample Usage](usage.html) – Several useful
        code snippets are provided.* [Design Considerations](design.html) –
          Design considerations to keep in mind to ensure that your
          application will work with any language script.* [More Information](info.html) –
            A list of further resources are provided.

[« Previous](perform.html)
•
[Trail](../TOC.html)
•
[Next »](terminology.html)

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

**Previous page:** Improving Collation Performance
  
**Next page:** Terminology




A browser with JavaScript enabled is required for this page to operate properly.