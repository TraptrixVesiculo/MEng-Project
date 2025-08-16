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

[About the BreakIterator Class](about.html)

[Character Boundaries](char.html)

[Word Boundaries](word.html)

[Sentence Boundaries](sentence.html)

Line Boundaries

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

[« Previous](sentence.html) • [Trail](../TOC.html) • [Next »](shapedDigits.html)

# Line Boundaries

Applications that format text or that perform line wrapping must locate
potential line breaks. You can find these line breaks, or boundaries,
with a `BreakIterator` that has been created with the
`getLineInstance`  method:

```

BreakIterator lineIterator =
		BreakIterator.getLineInstance(currentLocale);

```

This `BreakIterator`
determines the positions in a string where text can break to continue
on the next line. The positions detected by the
`BreakIterator` are potential line breaks. The actual line
breaks displayed on the screen may not be the same.

The two examples that follow use the
[`markBoundaries`](word.html#markBoundaries)
method of
[`BreakIteratorDemo.java`](examples/BreakIteratorDemo.java)
to show the line boundaries detected by a `BreakIterator`.
The `markBoundaries` method indicates line boundaries by
printing carets (^) beneath the target string.

According to a `BreakIterator`, a line boundary occurs after
the termination of a sequence of whitespace characters (space, tab, new
line). In the following example, note that you can break the line at
any of the boundaries detected:

```

She stopped.  She said, "Hello there," and then went on.
^   ^         ^   ^     ^      ^     ^ ^   ^    ^    ^  ^

```

Potential line breaks also occur immediately after a hyphen:

```

There are twenty-four hours in a day.
^     ^   ^      ^    ^     ^  ^ ^   ^

```

The next example breaks a long string of text into fixed-length lines
with a method called `formatLines`. This method uses a
`BreakIterator`  to locate the potential line breaks. The
`formatLines` method is short, simple, and, thanks to the
`BreakIterator`, locale-independent. Here is the source
code:

```

static void formatLines(String target, int maxLength,
			Locale currentLocale) {

    BreakIterator boundary =
	BreakIterator.getLineInstance(currentLocale);
    boundary.setText(target);
    int start = boundary.first();
    int end = boundary.next();
    int lineLength = 0;

    while (end != BreakIterator.DONE) {
	String word = target.substring(start,end);
	lineLength = lineLength + word.length();
	if (lineLength >= maxLength) {
	    System.out.println();
	    lineLength = word.length();
	}
	System.out.print(word);
	start = end;
	end = boundary.next();
    }
}

```

The `BreakIteratorDemo` program invokes the `formatLines`
method as follows:

```

String moreText = "She said, \"Hello there,\" and then " +
	 "went on down the street. When she stopped " +
	 "to look at the fur coats in a shop window, " +
	 "her dog growled._ \"Sorry Jake,\" she said. " +
	 " \"I didn't know you would take it personally.\"";

formatLines(moreText, 30, currentLocale);

```

The output from this call to `formatLines` is:

```

She said, "Hello there," and
then went on down the
street. When she stopped to
look at the fur coats in a
shop window, her dog
growled. "Sorry Jake," she
said. "I didn't know you
would take it personally."

```

[« Previous](sentence.html)
•
[Trail](../TOC.html)
•
[Next »](shapedDigits.html)

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

**Previous page:** Sentence Boundaries
  
**Next page:** Converting Latin Digits to Other Unicode Digits




A browser with JavaScript enabled is required for this page to operate properly.