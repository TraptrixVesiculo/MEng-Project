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

Sample Usage

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

[« Previous](characterClass.html) • [Trail](../TOC.html) • [Next »](design.html)

# Sample Usage

This page contains some code snippets that show you several commono
scenarios.

### Creating a `String` from a Code Point

```

String newString(int codePoint) {
    return new String(Character.toChars(codePoint));
}

```

### Creating a `String` from a Code Point - Optimized for BMP Characters

The `Character.toChars` method creates an temporary array
that is used once and then discarded.
If this negatively affects performance, you
can use the following approach that is optimizied for BMP characters
(characters that are represented by a single `char` value).
In this method, `toChars` is invoked only for
supplementary characters.

```

String newString(int codePoint) {
    if (Character.charCount(codePoint) == 1) {
        return String.valueOf(codePoint);
    } else {
        return new String(Character.toChars(codePoint));
    }
}

```

### Creating `String` Objects in Bulk

To create a large number of strings, the bulk version of the previous
snippet reuses the array used by the `toChars`
method. This method creates a separate `String`
instance for each code point and is optimized for BMP characters.

```

String[] newStrings(int[] codePoints) {
    String[] result = new String[codePoints.length];
    char[] codeUnits = new char[2];
    for (int i = 0; i < codePoints.length; i++) {
        int count = Character.toChars(codePoints[i], codeUnits, 0);
        result[i] = new String(codeUnits, 0, count);
    }
    return result;
}

```

### Generating Messages

The formatting API supports supplementary characters. The following example
is a simple way to generate a message.

```

System.out.printf("Character %c is invalid.%n", codePoint); //recommended

```

This following approach is simple and avoids concatenation, which makes
the text more difficult to localize as not all languages insert numeric
values into a string in the same order as English.

```

System.out.println("Character " + String.valueOf(char) + " is invalid."); //not recommended

```

[« Previous](characterClass.html)
•
[Trail](../TOC.html)
•
[Next »](design.html)

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

**Previous page:** Character and String APIs
  
**Next page:** Design Considerations




A browser with JavaScript enabled is required for this page to operate properly.