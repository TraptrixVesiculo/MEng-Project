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

Word Boundaries

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

[« Previous](char.html) • [Trail](../TOC.html) • [Next »](sentence.html)

# Word Boundaries

You invoke the `getWordIterator`
method to instantiate a `BreakIterator`
that detects word boundaries:

```

BreakIterator wordIterator =
    BreakIterator.getWordInstance(currentLocale);

```

You'll want to create such a `BreakIterator`
when your application needs to perform operations on individual words.
These operations might be common word- processing functions, such as
selecting, cutting, pasting, and copying. Or, your application may
search for words, and it must be able to distinguish entire words from
simple strings.

When a `BreakIterator`
analyzes word boundaries, it differentiates between words and
characters that are not part of words. These characters, which include
spaces, tabs, punctuation marks, and most symbols, have word boundaries
on both sides.

The example that follows, which is from the program
[`BreakIteratorDemo`](examples/BreakIteratorDemo.java),
marks the word boundaries in some text. The program creates the
`BreakIterator` 
and then calls the `markBoundaries` method:

```

Locale currentLocale = new Locale ("en","US");

BreakIterator wordIterator =
    BreakIterator.getWordInstance(currentLocale);

String someText = "She stopped. " +
		  "She said, \"Hello there,\" and then went on.";

markBoundaries(someText, wordIterator);

```

The `markBoundaries`
method is defined in `BreakIteratorDemo.java`.
This method marks boundaries by printing carets (^) beneath the target
string. In the code that follows, notice the `while` loop
where `markBoundaries` scans the string by calling the
`next` method:

```

static void markBoundaries(String target, BreakIterator iterator) {

    StringBuffer markers = new StringBuffer();
    markers.setLength(target.length() + 1);
    for (int k = 0; k < markers.length(); k++) {
	markers.setCharAt(k,' ');
    }

    iterator.setText(target);
    int boundary = iterator.first();

    while (boundary != BreakIterator.DONE) {
	markers.setCharAt(boundary,'^');
	boundary = iterator.next();
    }

    System.out.println(target);
    System.out.println(markers);
}

```

The output of the `markBoundaries`
method follows. Note where the carets (^) occur in relation to the
punctuation marks and spaces:

```

She stopped.  She said, "Hello there," and then went on.
^  ^^      ^^ ^  ^^   ^^^^    ^^    ^^^^  ^^   ^^   ^^ ^^

```

The `BreakIterator`
class makes it easy to select words from within text. You don't have to
write your own routines to handle the punctuation rules of various
languages; the `BreakIterator`
class does this for you.

The `extractWords`
method in the following example extracts and prints words for a given
string. Note that this method uses
`Character.isLetterOrDigit`
to avoid printing "words" that contain space characters.

```

static void extractWords(String target, BreakIterator wordIterator) {

    wordIterator.setText(target);
    int start = wordIterator.first();
    int end = wordIterator.next();

    while (end != BreakIterator.DONE) {
	String word = target.substring(start,end);
	if (Character.isLetterOrDigit(word.charAt(0))) {
	    System.out.println(word);
	}
	start = end;
	end = wordIterator.next();
    }
}

```

The `BreakIteratorDemo`
program invokes `extractWords`,
passing it the same target string used in the previous example.
The `extractWords`  method prints out the following list of words:

```

She
stopped
She
said
Hello
there
and
then
went
on

```

[« Previous](char.html)
•
[Trail](../TOC.html)
•
[Next »](sentence.html)

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

**Previous page:** Character Boundaries
  
**Next page:** Sentence Boundaries




A browser with JavaScript enabled is required for this page to operate properly.