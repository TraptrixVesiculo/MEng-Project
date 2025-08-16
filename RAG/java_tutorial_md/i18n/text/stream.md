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

[Byte Encodings and Strings](string.html)

Character and Byte Streams

[Normalizing Text](normalizerapi.html)

[Home Page](../../index.html)
>
[Internationalization](../index.html)
>
[Working with Text](index.html)

[« Previous](string.html) • [Trail](../TOC.html) • [Next »](normalizerapi.html)

# Character and Byte Streams

The `java.io`
package provides classes that allow you to convert between Unicode
character streams and byte streams of non-Unicode text. With the
[`InputStreamReader`](http://download.oracle.com/javase/7/docs/api/java/io/InputStreamReader.html) class, you can convert byte streams to character streams. You use the
[`OutputStreamWriter`](http://download.oracle.com/javase/7/docs/api/java/io/OutputStreamWriter.html)class to translate character streams into byte streams. The following
figure illustrates the conversion process:

![This figure represents the conversion process](../../figures/i18n/i18n-6.gif)

When you create `InputStreamReader`
and `OutputStreamWriter` 
objects, you specify the byte encoding that you want to convert. For
example, to translate a text file in the UTF-8 encoding into Unicode,
you create an `InputStreamReader` as follows:

```

FileInputStream fis = new FileInputStream("test.txt");
InputStreamReader isr = new InputStreamReader(fis, "UTF8");

```

If you omit the encoding identifier, `InputStreamReader`
and `OutputStreamWriter`
rely on the default encoding. You can determine which encoding an
`InputStreamReader` or `OutputStreamWriter`
uses by invoking the `getEncoding` method, as follows:

```

InputStreamReader defaultReader = new InputStreamReader(fis);
String defaultEncoding = defaultReader.getEncoding();

```

The example that follows shows you how to perform character-set
conversions with the `InputStreamReader`
and `OutputStreamWriter`
classes. The full source code for this example is in
[`StreamConverter.java`](examples/StreamConverter.java).
This program displays Japanese characters. Before trying it out, verify
that the appropriate fonts have been installed on your system. If you
are using the JDK software that is compatible with version 1.1, make a
copy of the `font.properties` file and then replace it with the
`font.properties.ja` file.

The `StreamConverter`
program converts a sequence of Unicode characters from a `String`
object into a `FileOutputStream`
of bytes encoded in UTF-8. The method that performs the conversion is
called `writeOutput`:

```

static void writeOutput(String str) {

    try {
	FileOutputStream fos = new FileOutputStream("test.txt");
	Writer out = new OutputStreamWriter(fos, "UTF8");
	out.write(str);
	out.close();
    } catch (IOException e) {
	e.printStackTrace();
    }
}

```

The `readInput`
method reads the bytes encoded in UTF-8 from the file created by the
`writeOutput`
method. An `InputStreamReader` 
object converts the bytes from UTF-8 into Unicode and returns the
result in a `String`. The `readInput`
method is as follows:

```

static String readInput() {

    StringBuffer buffer = new StringBuffer();
    try {
	FileInputStream fis = new FileInputStream("test.txt");
	InputStreamReader isr = new InputStreamReader(fis,
						      "UTF8");
	Reader in = new BufferedReader(isr);
	int ch;
	while ((ch = in.read()) > -1) {
		buffer.append((char)ch);
	}
	in.close();
	return buffer.toString();
    } catch (IOException e) {
	e.printStackTrace();
	return null;
    }
}

```

The `main`
method of the `StreamConverter`
program invokes the `writeOutput`
method to create a file of bytes encoded in UTF-8. The `readInput`
method reads the same file, converting the bytes back into Unicode.
Here is the source code for the `main` method:

```

public static void main(String[] args) {

    String jaString =	
	new String("\u65e5\u672c\u8a9e\u6587\u5b57\u5217");

    writeOutput(jaString); 
    String inputString = readInput();
    String displayString = jaString + " " + inputString;
    new ShowString(displayString, "Conversion Demo");
}

```

The original string (`jaString`)
should be identical to the newly created string (`inputString`).
To show that the two strings are the same,
the program concatenates them and displays them with a `ShowString`
object. The `ShowString` class displays a string with the
`Graphics.drawString` method.
The source code for this class is in
[`ShowString.java`](examples/ShowString.java).
When the `StreamConverter` program instantiates `ShowString`,
the following window appears. The repetition of the characters
displayed verifies that the two strings are identical:

![This is a screens hot of the StreamConverter program](../../figures/i18n/conversion.gif)

[« Previous](string.html)
•
[Trail](../TOC.html)
•
[Next »](normalizerapi.html)

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

**Previous page:** Byte Encodings and Strings
  
**Next page:** Normalizing Text




A browser with JavaScript enabled is required for this page to operate properly.