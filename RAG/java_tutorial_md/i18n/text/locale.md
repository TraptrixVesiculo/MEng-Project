[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Internationalization
  
**Lesson:** Working with Text
  
**Section:** Comparing Strings

[Working with Text](index.html)

[Checking Character Properties](charintro.html)

[Comparing Strings](collationintro.html)

Performing Locale-Independent Comparisons

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

[« Previous](collationintro.html) • [Trail](../TOC.html) • [Next »](rule.html)

# Performing Locale-Independent Comparisons

Collation rules define the sort sequence of strings. These rules vary
with locale, because various natural languages sort words differently.
You can use the predefined collation rules provided by the
`Collator` class to sort strings in a locale-independent
manner.

To instantiate the `Collator` class invoke the
`getInstance` method. Usually, you create a
`Collator` for the default `Locale`, as in the
following example:

```

Collator myDefaultCollator = Collator.getInstance();

```

You can also specify a particular `Locale` when you create a
`Collator`, as follows:

```

Collator myFrenchCollator = Collator.getInstance(Locale.FRENCH);

```

The `getInstance` method returns a
`RuleBasedCollator`, which is a concrete subclass of
`Collator`. The `RuleBasedCollator` contains a
set of rules that determine the sort order of strings for the locale
you specify. These rules are predefined for each locale. Because the
rules are encapsulated within the `RuleBasedCollator`, your
program won't need special routines to deal with the way collation
rules vary with language.

You invoke the `Collator.compare` method to perform a
locale-independent string comparison. The `compare` method
returns an integer less than, equal to, or greater than zero when the
first string argument is less than, equal to, or greater than the
second string argument. The following table contains some sample calls
to `Collator.compare`:

### `Collator.compare` Examples

| Example | Return Value | Explanation |
| `myCollator.compare("abc", "def")` | `-1` | `"abc"` is less than "def" |
| `myCollator.compare("rtf", "rtf")` | `0` | the two strings are equal |
| `myCollator.compare("xyz", "abc")` | `1` | "xyz" is greater than "abc" |

You use the `compare` method when performing sort operations.
The sample program called
[`CollatorDemo`](examples/CollatorDemo.java)
uses the `compare` method to sort an array of English and
French words. This program shows what can happen when you sort the same
list of words with two different collators:

```

Collator fr_FRCollator = Collator.getInstance(new Locale("fr","FR"));

Collator en_USCollator = Collator.getInstance(new Locale("en","US"));

```

The method for sorting, called `sortStrings`, can be used
with any `Collator`. Notice that the
`sortStrings` method invokes the `compare`
method:

```

public static void sortStrings(Collator collator, 
                               String[] words) {
    String tmp;
    for (int i = 0; i < words.length; i++) {
	for (int j = i + 1; j < words.length; j++) { 
	    if (collator.compare(words[i], words[j]) > 0) {
		tmp = words[i];
		words[i] = words[j];
		words[j] = tmp;
	    }
	}
    }
}

```

The English `Collator` sorts the words as follows:

```

peach
péché
pêche
sin

```

According to the collation rules of the French language, the preceding
list is in the wrong order. In French péché should follow
pêche in a sorted list. The French `Collator` sorts
the array of words correctly, as follows:

```

peach
pêche
péché
sin

```

[« Previous](collationintro.html)
•
[Trail](../TOC.html)
•
[Next »](rule.html)

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

**Previous page:** Comparing Strings
  
**Next page:** Customizing Collation Rules




A browser with JavaScript enabled is required for this page to operate properly.