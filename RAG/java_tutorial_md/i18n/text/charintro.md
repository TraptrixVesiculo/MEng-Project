[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Internationalization
  
**Lesson:** Working with Text

[Working with Text](index.html)

Checking Character Properties

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

[Home Page](../../index.html)
>
[Internationalization](../index.html)
>
[Working with Text](index.html)

[« Previous](index.html) • [Trail](../TOC.html) • [Next »](collationintro.html)

# Checking Character Properties

You can categorize characters according to their properties. For
instance, X is an uppercase letter and 4 is a decimal digit. Checking
character properties is a common way to verify the data entered by end
users. If you are selling books online, for example, your order entry
screen should verify that the characters in the quantity field are all
digits.

Developers who aren't used to writing global software might determine a
character's properties by comparing it with character constants. For
instance, they might write code like this:

```

char ch;
...

// This code is WRONG!

if ((ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z'))
  // ch is a letter
...
if (ch >= '0' && ch <= '9')
  // ch is a digit
...
if ((ch == ' ') || (ch =='\n') || (ch == '\t'))
  // ch is a whitespace

```

The preceding code is *wrong* because it works only with English
and a few other languages. To internationalize the previous example,
replace it with the following statements:

```

char ch;
...

// This code is OK!

if (Character.isLetter(ch))
...
if (Character.isDigit(ch))
...
if (Character.isSpaceChar(ch))

```

The
[`Character`](http://download.oracle.com/javase/7/docs/api/java/lang/Character.html) methods rely on the Unicode Standard for determining the properties of
a character. Unicode is a 16-bit character encoding that supports the
world's major languages. In the Java programming language
`char` values represent Unicode characters. If you check
the properties of a `char` with the appropriate
`Character` method, your code will work with all major
languages. For example, the `Character.isLetter` method
returns `true` if the character is a letter in Chinese,
German, Arabic, or another language.

The following list gives some of the most useful `Character`
comparison methods. The `Character` API documentation fully
specifies the methods.

* `isDigit`* `isLetter`* `isLetterOrDigit`* `isLowerCase`* `isUpperCase`* `isSpaceChar`* `isDefined`

The `Character.getType` method returns the Unicode category
of a character. Each category corresponds to a constant defined in the
`Character` class. For instance, `getType`
returns the `Character.UPPERCASE_LETTER` constant for the
character A. For a complete list of the category constants returned by
`getType`, see the
[`Character`](http://download.oracle.com/javase/7/docs/api/java/lang/Character.html) API documentation. The following example shows how to use `getType` and the `Character` category constants. All
of the expressions in these `if` statements are
`true`:

```

if (Character.getType('a') == Character.LOWERCASE_LETTER)
...
if (Character.getType('R') == Character.UPPERCASE_LETTER)
...
if (Character.getType('>') == Character.MATH_SYMBOL)
...
if (Character.getType('_') == Character.CONNECTOR_PUNCTUATION)

```

[« Previous](index.html)
•
[Trail](../TOC.html)
•
[Next »](collationintro.html)

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

**Previous page:** Working with Text
  
**Next page:** Comparing Strings




A browser with JavaScript enabled is required for this page to operate properly.