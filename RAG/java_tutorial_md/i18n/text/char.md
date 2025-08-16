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

Character Boundaries

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

[« Previous](about.html) • [Trail](../TOC.html) • [Next »](word.html)

# Character Boundaries

You need to locate character boundaries if your application allows the
end user to highlight individual characters or to move a cursor through
text one character at a time. To create a `BreakIterator` 
that locates character boundaries, you invoke the
`getCharacterInstance`  method, as follows:

```

BreakIterator characterIterator =
         BreakIterator.getCharacterInstance(currentLocale);

```

This type of `BreakIterator`
detects boundaries between user characters, not just Unicode characters.

A user character may be composed of more than one Unicode character.
For example, the user character ü can be composed by combining the
Unicode characters \u0075 (u) and \u00a8 (¨). This isn't the best
example, however, because the character ü may also be represented
by the single Unicode character \u00fc. We'll draw on the Arabic
language for a more realistic example.

In Arabic the word for house is:

![The Arabic pictograph for House](../../figures/i18n/i18n-5.gif)

This word contains three user characters, but it is composed of the
following six Unicode characters:

```

String house = "\u0628" + "\u064e" + "\u064a" + 
	       "\u0652" + "\u067a" + "\u064f";

```

The Unicode characters at positions 1, 3, and 5 in the `house`
string are diacritics. Arabic requires diacritics because they can
alter the meanings of words. The diacritics in the example are
nonspacing characters, since they appear above the base characters. In
an Arabic word processor you cannot move the cursor on the screen once
for every Unicode character in the string. Instead you must move it
once for every user character, which may be composed by more than one
Unicode character. Therefore you must use a `BreakIterator`
to scan the user characters in the string.

The sample program
[`BreakIteratorDemo`](examples/BreakIteratorDemo.java),
creates a `BreakIterator`
to scan Arabic characters. The program passes this `BreakIterator`,
along with the `String` object created previously, to a
method named `listPositions`:

```

BreakIterator arCharIterator =
		BreakIterator.getCharacterInstance(new Locale ("ar","SA"));

listPositions (house, arCharIterator);

```

The `listPositions`
method uses a `BreakIterator`
to locate the character boundaries in the string. Note that the
`BreakIteratorDemo`  assigns a particular string to the
`BreakIterator` with the `setText`
method. The program retrieves the first character boundary with the
`first`  method and then invokes the `next`
method until the constant `BreakIterator.DONE` 
is returned. The code for this routine is as follows:

```

static void listPositions(String target, BreakIterator iterator) {
		
    iterator.setText(target);
    int boundary = iterator.first();

    while (boundary != BreakIterator.DONE) {
        System.out.println (boundary);
        boundary = iterator.next();
    }
}

```

The `listPositions` method prints out the following boundary
positions for the user characters in the string `house`.
Note that the positions of the diacritics (1, 3, 5) are not listed:

```

0
2
4
6

```

[« Previous](about.html)
•
[Trail](../TOC.html)
•
[Next »](word.html)

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

**Previous page:** About the BreakIterator Class
  
**Next page:** Word Boundaries




A browser with JavaScript enabled is required for this page to operate properly.