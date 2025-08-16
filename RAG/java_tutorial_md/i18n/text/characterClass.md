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

Character and String APIs

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

[« Previous](supplementaryChars.html) • [Trail](../TOC.html) • [Next »](usage.html)

# Character and String APIs

The `Character` class encapsulates the `char`
data type.
For the J2SE release 5, many methods were added to the
`Character` class to support supplementary characters.
This API falls into two categories: methods that convert
between `char` and code point values
and methods that verifiy the validity of or map code points.

This section describes a subset of the available methods
in the `Character` class.
For the complete list of available APIs, see the
[`Character`](http://download.oracle.com/javase/7/docs/api/java/lang/Character.html) class specification.

### Conversion Methods and the Character Class

The following table includes the most useful conversion methods,
or methods that facilitate conversion,
in the `Character` class. The `codePointAt`
and `codePointBefore` methods are included in this list because
text is generally found in a sequence, such as a `String`,
and these methods can be used to extract the desired substring.

| Method(s) | Description |
| --- | --- |
| [`toChars(int codePoint, char[] dst, int dstIndex)`](http://download.oracle.com/javase/7/docs/api/java/lang/Character.html#toChars(int, char[], int))  [`toChars(int codePoint)`](http://download.oracle.com/javase/7/docs/api/java/lang/Character.html#toChars(int)) | Converts the specified Unicode code point to its UTF-16 representation and places it in a `char` array. Sample usage: `Character.toChars(0x10400)` |
| [`toCodePoint(char high, char low)`](http://download.oracle.com/javase/7/docs/api/java/lang/Character.html#toCodePoint(char, char))  [`toCodePoint(CharSequence, int)`](http://download.oracle.com/javase/7/docs/api/java/lang/Character.html#toCodePoint(java.lang.CharSequence, int))  [`toCodePoint(char[], int, int)`](http://download.oracle.com/javase/7/docs/api/java/lang/Character.html#toCodePoint(char[], int, int)) | Converts the specified parameters to its supplementary code point value. The different methods accept different input formats. |
| [`codePointAt(char[] a, int index)`](http://download.oracle.com/javase/7/docs/api/java/lang/Character.html#codePointAt(char[], int))  [`codePointAt(char[] a, int index, int limit)`](http://download.oracle.com/javase/7/docs/api/java/lang/Character.html#codePointAt(char[], int, int)) | Returns the Unicode code point at the specified index. The third method takes a `CharSequence` and the second method enforces an upper limit on the index. |
| [`codePointBefore(char[] a, int index)`](http://download.oracle.com/javase/7/docs/api/java/lang/Character.html#codePointBefore(char[], int))  [`codePointBefore(char[] a, int index, int start)`](http://download.oracle.com/javase/7/docs/api/java/lang/Character.html#codePointBefore(char[], int, int))  [`codePointBefore(CharSequence seq, int index)`](http://download.oracle.com/javase/7/docs/api/java/lang/Character.html#codePointBefore(java.lang.CharSequence, int))  [`codePointBefore(char[], int, int)`](http://download.oracle.com/javase/7/docs/api/java/lang/Character.html#codePointBefore(char[], int, int)) | Returns the Unicode code point before the specified index. The third method accepts a `CharSequence` and the other methods accept a `char` array. The second method enforces a lower limit on the index. |
| [`charCount(int codePoint)`](http://download.oracle.com/javase/7/docs/api/java/lang/Character.html#charCount(int)) | Returns the value 1 for characters that can be represented by a single `char`. Returns the value 2 for supplementary characters that require two `char`s. |

### Verification and Mapping Methods in the Character Class

Some of the previous methods that used the `char`
primitive data type, such as `isLowerCase(char)`
and `isDigit(char)`,
were supplanted by methods that support supplementary characters,
such as `isLowerCase(int)` and `isDigit(int)`.
The previous methods are supported but do not work with
supplementary characters.
To create a global application and ensure that your code works
seamlessly with any language,
it is recommended that you use the newer forms of these methods.

Note that, for performance reasons, most methods that accept a code
point do not verify the validity of the code point parameter.
You can use the `isValidCodePoint` method for that purpose.

The following table lists some of the verification
and mapping methods in the `Character` class.

|  |  |
| --- | --- |
| [`isValidCodePoint(int codePoint)`](http://download.oracle.com/javase/7/docs/api/java/lang/Character.html#isValidCodePoint(int)) | Returns true if the code point is within the range of 0x0000 to 0x10FFFF, inclusive. |
| [`isSupplementaryCodePoint(int codePoint)`](http://download.oracle.com/javase/7/docs/api/java/lang/Character.html#isSupplementaryCodePoint(int)) | Returns true if the code point is within the range of 0x10000 to 0x10FFFF, inclusive. |
| [`isHighSurrogate(char)`](http://download.oracle.com/javase/7/docs/api/java/lang/Character.html#isHighSurrogate(char)) | Returns true if the specified `char` is within the high surrogate range of \uD800 to \uDBFF, inclusive. |
| [`isLowSurrogate(char)`](http://download.oracle.com/javase/7/docs/api/java/lang/Character.html#isLowSurrogate(char)) | Returns true if the specified `char` is within the low surrogate range of \uDC00 to \uDFFF, inclusive. |
| [`isSurrogatePair(char high, char low)`](http://download.oracle.com/javase/7/docs/api/java/lang/Character.html#isSurrogatePair(char, char)) | Returns true if the specified high and low surrogate code values represent a valid surrogate pair. |
| [`codePointCount(CharSequence, int, int)`](http://download.oracle.com/javase/7/docs/api/java/lang/Character.html#codePointCount(java.lang.CharSequence, int, int))  [`codePointCount(char[], int, int)`](http://download.oracle.com/javase/7/docs/api/java/lang/Character.html#codePointCount(char[], int, int)) | Returns the number of Unicode code points in the `CharSequence`, or `char` array. |
| [`isLowerCase(int)`](http://download.oracle.com/javase/7/docs/api/java/lang/Character.html#isLowerCase(int))  [`isUpperCase(int)`](http://download.oracle.com/javase/7/docs/api/java/lang/Character.html#isUpperCase(int)) | Returns true if the specified Unicode code point is a lowercase or uppercase character. |
| [`isDefined(int)`](http://download.oracle.com/javase/7/docs/api/java/lang/Character.html#isDefined(int)) | Returns true if the specified Unicode code point is defined in the Unicode standard. |
| [`isJavaIdentifierStart(char)`](http://download.oracle.com/javase/7/docs/api/java/lang/Character.html#isJavaIdentifierStart(char))  [`isJavaIdentifierStart(int)`](http://download.oracle.com/javase/7/docs/api/java/lang/Character.html#isJavaIdentifierStart(int)) | Returns true if the specified character or Unicode code point is permissible as the first character in a Java identifier. |
| [`isLetter(int)`](http://download.oracle.com/javase/7/docs/api/java/lang/Character.html#isLetter(int))  [`isDigit(int)`](http://download.oracle.com/javase/7/docs/api/java/lang/Character.html#isDigit(int))  [`isLetterOrDigit(int)`](http://download.oracle.com/javase/7/docs/api/java/lang/Character.html#isLetterOrDigit(int)) | Returns true if the specified Unicode code point is a letter, a digit, or a letter or digit. |
| [`getDirectionality(int)`](http://download.oracle.com/javase/7/docs/api/java/lang/Character.html#getDirectionality(int)) | Returns the Unicode directionality property for the given Unicode code point. |
| [`Character.UnicodeBlock.of(int codePoint)`](http://download.oracle.com/javase/7/docs/api/java/lang/Character.UnicodeBlock.html#of(int)) | Returns the object representing the Unicode block that contains the given Unicode code point or returns `null` if the code point is not a member of a defined block. |

### Methods in the String Classes

The `String`, `StringBuffer`, and
`StringBuilder` classes also have contructors and methods that
work with supplementary characters.
The following table lists some of the commonly used methods.
For the complete list of available APIs, see the javadoc for the
[`String`](http://download.oracle.com/javase/7/docs/api/java/lang/String.html),
[`StringBuffer`](http://download.oracle.com/javase/7/docs/api/java/lang/StringBuffer.html), and
[`StringBuilder`](http://download.oracle.com/javase/7/docs/api/java/lang/StringBuilder.html) classes.

| Constructor or Methods | Description |
| --- | --- |
| [`String(int[] codePoints, int offset, int count)`](http://download.oracle.com/javase/7/docs/api/java/lang/String.html#String(int[], int, int)) | Allocates a new `String` instance that contains characters from a subarray of a Unicode code point array. |
| [`String.codePointAt(int index)`](http://download.oracle.com/javase/7/docs/api/java/lang/String.html#codePointAt(int))  [`StringBuffer.codePointAt(int index)`](http://download.oracle.com/javase/7/docs/api/java/lang/StringBuffer.html#codePointAt(int))  [`StringBuilder.codePointAt(int index)`](http://download.oracle.com/javase/7/docs/api/java/lang/StringBuilder.html#codePointAt(int)) | Returns the Unicode code point at the specified index. |
| [`String.codePointBefore(int index)`](http://download.oracle.com/javase/7/docs/api/java/lang/String.html#codePointBefore(int))  [`StringBuffer.codePointBefore(int index)`](http://download.oracle.com/javase/7/docs/api/java/lang/StringBuffer.html#codePointBefore(int))  [`StringBuilder.codePointBefore(int index)`](http://download.oracle.com/javase/7/docs/api/java/lang/StringBuilder.html#codePointBefore(int)) | Returns the Unicode code point before the specified index. |
| [`String.codePointCount(int beginIndex, int endIndex)`](http://download.oracle.com/javase/7/docs/api/java/lang/String.html#codePointCount(int, int))  [`StringBuffer.codePointCount(int beginIndex, int endIndex)`](http://download.oracle.com/javase/7/docs/api/java/lang/StringBuffer.html#codePointCount(int, int))  [`StringBuilder.codePointCount(int beginIndex, int endIndex)`](http://download.oracle.com/javase/7/docs/api/java/lang/StringBuilder.html#codePointCount(int, int)) | Returns the number of Unicode code points in the specified range. |
| [`StringBuffer.appendCodePoint(int codePoint)`](http://download.oracle.com/javase/7/docs/api/java/lang/StringBuffer.html#appendCodePoint(int))  [`StringBuilder.appendCodePoint(int codePoint)`](http://download.oracle.com/javase/7/docs/api/java/lang/StringBuilder.html#appendCodePoint(int)) | Appends the string representation of the specified code point to the sequence. |
| [`String.offsetByCodePoints(int index, int codePointOffset)`](http://download.oracle.com/javase/7/docs/api/java/lang/String.html#offsetByCodePoints(int, int))  [`StringBuffer.offsetByCodePoints(int index, int codePointOffset)`](http://download.oracle.com/javase/7/docs/api/java/lang/StringBuffer.html#offsetByCodePoints(int, int))  [`StringBuilder.offsetByCodePoints(int index, int codePointOffset)`](http://download.oracle.com/javase/7/docs/api/java/lang/StringBuilder.html#offsetByCodePoints(int, int)) | Returns the index that is offset from the given index by the given number of code points. |

[« Previous](supplementaryChars.html)
•
[Trail](../TOC.html)
•
[Next »](usage.html)

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

**Previous page:** Supplementary Characters as Surrogates
  
**Next page:** Sample Usage




A browser with JavaScript enabled is required for this page to operate properly.