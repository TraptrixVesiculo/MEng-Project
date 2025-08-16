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

[Detecting Text Boundaries](boundaryintro.html)

[About the BreakIterator Class](about.html)

[Character Boundaries](char.html)

[Word Boundaries](word.html)

[Sentence Boundaries](sentence.html)

[Line Boundaries](line.html)

[Converting Latin Digits to Other Unicode Digits](shapedDigits.html)

Converting Non-Unicode Text

[Byte Encodings and Strings](string.html)

[Character and Byte Streams](stream.html)

[Normalizing Text](normalizerapi.html)

[Home Page](../../index.html)
>
[Internationalization](../index.html)
>
[Working with Text](index.html)

[« Previous](shapedDigits.html) • [Trail](../TOC.html) • [Next »](string.html)

# Converting Non-Unicode Text

In the Java programming language `char`
values represent Unicode characters. Unicode is a 16-bit character
encoding that supports the world's major languages. You can learn more
about the Unicode standard at the
[Unicode Consortium Web site](http://www.unicode.org/index.html) .

Few text editors currently support Unicode text entry. The text editor
we used to write this section's code examples supports only ASCII
characters, which are limited to 7 bits. To indicate Unicode characters
that cannot be represented in ASCII, such as ö, we used the
`\uXXXX` escape sequence. Each `X`
in the escape sequence is a hexadecimal digit. The following example
shows how to indicate the ö character with an escape sequence:

```

String str = "\u00F6";
char c = '\u00F6';
Character letter = new Character('\u00F6');

```

A variety of character encodings are used by systems around the world.
Currently few of these encodings conform to Unicode. Because your
program expects characters in Unicode, the text data it gets from the
system must be converted into Unicode, and vice versa. Data in text
files is automatically converted to Unicode when its encoding matches
the default file encoding of the Java Virtual Machine. You can identify
the default file encoding by creating an
`OutputStreamWriter` using it and asking for its
canonical name:

```

OutputStreamWriter out = new OutputStreamWriter(new ByteArrayOutputStream());
System.out.println(out.getEncoding());

```

If the default file encoding
differs from the encoding of the text data you want to
process, then you must perform the conversion yourself. You might need
to do this when processing text from another country or computing
platform.

This section discusses the APIs you use to translate non-Unicode text
into Unicode. Before using these APIs, you should verify that the
character encoding you wish to convert into Unicode is supported. The
list of supported character encodings is not part of the Java
programming language specification. Therefore the character encodings
supported by the APIs may vary with platform. To see which encodings
the Java Development Kit supports, see the
[Supported Encodings](http://download.oracle.com/javase/7/docs/technotes/guides/intl/encoding.doc.html) document.

The material that follows describes two techniques for converting
non-Unicode text to Unicode. You can convert non-Unicode byte arrays
into `String` objects, and vice versa. Or you can translate
between streams of Unicode characters and byte streams of non-Unicode
text.

### [Byte Encodings and Strings](string.html)

> This section shows you how to convert non-Unicode
> byte arrays into `String` objects, and vice versa.

### [Character and Byte Streams](stream.html)

> In this section you'll learn how to
> translate between streams of Unicode characters and
> byte streams of non-Unicode text.

[« Previous](shapedDigits.html)
•
[Trail](../TOC.html)
•
[Next »](string.html)

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

**Previous page:** Converting Latin Digits to Other Unicode Digits
  
**Next page:** Byte Encodings and Strings




A browser with JavaScript enabled is required for this page to operate properly.