[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Internationalization
  
**Lesson:** Working with Text
  
**Section:** Converting Non-Unicode Text

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

[Converting Non-Unicode Text](convertintro.html)

Byte Encodings and Strings

[Character and Byte Streams](stream.html)

[Normalizing Text](normalizerapi.html)

[Home Page](../../index.html)
>
[Internationalization](../index.html)
>
[Working with Text](index.html)

[« Previous](convertintro.html) • [Trail](../TOC.html) • [Next »](stream.html)

# Byte Encodings and Strings

If a byte array contains non-Unicode text, you can convert the text to
Unicode with one of the `String` constructor methods.
Conversely, you can convert a `String` object into a byte
array of non-Unicode characters with the `String.getBytes`
method. When invoking either of these methods, you specify the encoding
identifier as one of the parameters.

The example that follows converts characters between UTF-8 and Unicode.
UTF-8 is a transmission format for Unicode that is safe for UNIX file
systems. The full source code for the example is in the file
[`StringConverter.java`](examples/StringConverter.java).

The `StringConverter`
program starts by creating a `String`
containing Unicode characters:

```

String original = new String("A" + "\u00ea" + "\u00f1" + 
			     "\u00fc" + "C");

```

When printed, the `String` named `original`
appears as:

```

AêñüC

```

To convert the `String`
object to UTF-8, invoke the `getBytes` 
method and specify the appropriate encoding identifier as a parameter.
The `getBytes`
method returns an array of bytes in UTF-8 format. To create a `String`
object from an array of non-Unicode bytes, invoke the `String`
constructor with the encoding parameter.
The code that makes these calls is enclosed in a `try` block,
in case the specified encoding is unsupported:

```

try {
    byte[] utf8Bytes = original.getBytes("UTF8");
    byte[] defaultBytes = original.getBytes();

    String roundTrip = new String(utf8Bytes, "UTF8");
    System.out.println("roundTrip = " + roundTrip);
    System.out.println();
    printBytes(utf8Bytes, "utf8Bytes");
    System.out.println();
    printBytes(defaultBytes, "defaultBytes");
} catch (UnsupportedEncodingException e) {
    e.printStackTrace();
}

```

The `StringConverter`
program prints out the values in the `utf8Bytes`
and `defaultBytes`
arrays to demonstrate an important point: The length of the converted
text might not be the same as the length of the source text. Some
Unicode characters translate into single bytes, others into pairs or
triplets of bytes.

The `printBytes` method displays the byte arrays by invoking
the `byteToHex` method, which is defined in the source file,
[`UnicodeFormatter.java`](examples/UnicodeFormatter.java).
Here is the `printBytes` method:

```

public static void printBytes(byte[] array, String name) {
    for (int k = 0; k < array.length; k++) {
	System.out.println(name + "[" + k + "] = " + "0x" +
			   UnicodeFormatter.byteToHex(array[k]));
    }
}

```

The output of the `printBytes`
method follows. Note that only the first and last bytes, the A and C
characters, are the same in both arrays:

```

utf8Bytes[0] = 0x41
utf8Bytes[1] = 0xc3
utf8Bytes[2] = 0xaa
utf8Bytes[3] = 0xc3
utf8Bytes[4] = 0xb1
utf8Bytes[5] = 0xc3
utf8Bytes[6] = 0xbc
utf8Bytes[7] = 0x43
defaultBytes[0] = 0x41
defaultBytes[1] = 0xea
defaultBytes[2] = 0xf1
defaultBytes[3] = 0xfc
defaultBytes[4] = 0x43

```

[« Previous](convertintro.html)
•
[Trail](../TOC.html)
•
[Next »](stream.html)

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

**Previous page:** Converting Non-Unicode Text
  
**Next page:** Character and Byte Streams




A browser with JavaScript enabled is required for this page to operate properly.