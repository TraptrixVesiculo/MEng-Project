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

[Terminology](terminology.html)

[Supplementary Characters as Surrogates](supplementaryChars.html)

[Character and String APIs](characterClass.html)

[Sample Usage](usage.html)

Design Considerations

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

[« Previous](usage.html) • [Trail](../TOC.html) • [Next »](info.html)

# Design Considerations

To write code that works seamlessly for any language using any script,
there are a few things to keep in mind.

| Consideration | Reason |
| --- | --- |
| Avoid methods that use the `char` data type. | Avoid using the `char` primitive data type or methods that use the `char` data type, because code that uses that data type does not work for supplementary characters. For methods that take a `char` type parameter, use the corresponding `int` method, where available. For example, use the `Character.isDigit(int)` method rather than `Character.isDigit(char)` method. |
| Use the `isValidCodePoint` method to verify code point values. | A code point is defined as an `int` data type, which allows for values outside of the valid range of code point values from 0x0000 to 0x10FFFF. For performance reasons, the methods that take a code point value as a parameter do not check the validity of the parameter, but you can use the `isValidCodePoint` method to check the value. |
| Use the `codePointCount` method to count characters. | The `String.length()` method returns the number of code units, or 16-bit `char` values, in the string. If the string contains supplementary characters, the count can be misleading because it will not reflect the true number of code points. To get an accurate count of the number of characters (including supplementary characters), use the `codePointCount` method. |
| Use the `String.toUpperCase(int codePoint)` and `String.toLowerCase(int codePoint)` methods rather than the `Character.toUpperCase(int codePoint)` or `Character.toLowerCase(int codePoint)` methods. | While the `Character.toUpperCase(int)` and `Character.toLowerCase(int)` methods do work with code point values, there are some characters that cannot be converted on a one-to-one basis. The lowercase German character ß, for example, becomes two characters, SS, when converted to uppercase. Likewise, the small Greek Sigma character is different depending on the position in the string. The `Character.toUpperCase(int)` and `Character.toLowerCase(int)` methods cannot handle these types of cases; however, the `String.toUpperCase` and `String.toLowerCase` methods handle these cases correctly. |
| Be careful when deleting characters. | When invoking the `StringBuilder.deleteCharAt(int index)` or `StringBuffer.deleteCharAt(int index)` methods where the index points to a supplementary character, only the first half of that character (the first `char` value) is removed. First, invoke the `Character.charCount` method on the character to determine if one or two `char` values must be removed. |
| Be careful when reversing characters in a sequence. | When invoking the `StringBuffer.reverse()` or `StringBuilder.reverse()` methods on text that contains supplementary characters, the high and low surrogate pairs are reversed which results in incorrect and possibly invalid surrogate pairs. |

[« Previous](usage.html)
•
[Trail](../TOC.html)
•
[Next »](info.html)

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

**Previous page:** Sample Usage
  
**Next page:** More Information




A browser with JavaScript enabled is required for this page to operate properly.