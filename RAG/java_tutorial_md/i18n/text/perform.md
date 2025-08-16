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

[Performing Locale-Independent Comparisons](locale.html)

[Customizing Collation Rules](rule.html)

Improving Collation Performance

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

[« Previous](rule.html) • [Trail](../TOC.html) • [Next »](unicode.html)

# Improving Collation Performance

Sorting long lists of strings is often time consuming. If your sort
algorithm compares strings repeatedly, you can speed up the process by
using the `CollationKey` class.

A
[`CollationKey`](http://download.oracle.com/javase/7/docs/api/java/text/CollationKey.html) object represents a sort key for a given `String` and
`Collator`. Comparing two `CollationKey` objects
involves a bitwise comparison of sort keys and is faster than
comparing `String` objects with the
`Collator.compare` method. However, generating
`CollationKey`  objects requires time. Therefore if a
`String` is to be compared just once,
`Collator.compare` offers better performance.

The example that follows uses a `CollationKey` object to sort an array of words. Source code for this example is in
[`KeysDemo.java`](examples/KeysDemo.java).

The `KeysDemo` program creates an array of
`CollationKey` objects in the `main` method. To
create a `CollationKey`, you invoke the
`getCollationKey` method on a `Collator` object.
You cannot compare two `CollationKey` objects unless they
originate from the same `Collator`. The `main`
method is as follows:

```

static public void main(String[] args) {
    Collator enUSCollator = 
              Collator.getInstance (new Locale("en","US"));
    String [] words = {
	"peach",
	"apricot",
	"grape",
	"lemon"
    };

    CollationKey[] keys = new CollationKey[words.length];

    for (int k = 0; k < keys.length; k ++) {
	keys[k] = enUSCollator.getCollationKey(words[k]);
    }

    sortArray(keys);
    printArray(keys);
}

```

The `sortArray` method invokes the
`CollationKey.compareTo` method. The `compareTo`
method returns an integer less than, equal to, or greater than zero if
the `keys[i]` object is less than, equal to, or greater than
the `keys[j]` object. Note that the program compares the
`CollationKey` objects, not the `String` objects
from the original array of words. Here is the code for the
`sortArray` method:

```

public static void sortArray(CollationKey[] keys) {
		
    CollationKey tmp;
    for (int i = 0; i < keys.length; i++) {
	for (int j = i + 1; j < keys.length; j++) {
	    if (keys[i].compareTo(keys[j]) > 0) {
		tmp = keys[i];
		keys[i] = keys[j];
		keys[j] = tmp; 
	    }
	}
    }
}

```

The `KeysDemo` program sorts an array of
`CollationKey` objects, but the original goal was to sort an
array of `String` objects. To retrieve the
`String` representation of each `CollationKey`,
the program invokes `getSourceString` in the
`displayWords` method, as follows:

```

static void displayWords(CollationKey[] keys) {

    for (int i = 0; i < keys.length; i++) {
	System.out.println(keys[i].getSourceString());
    }
}

```

The `displayWords`
method prints the following lines:

```

apricot
grape
lemon
peach

```

[« Previous](rule.html)
•
[Trail](../TOC.html)
•
[Next »](unicode.html)

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

**Previous page:** Customizing Collation Rules
  
**Next page:** Unicode




A browser with JavaScript enabled is required for this page to operate properly.