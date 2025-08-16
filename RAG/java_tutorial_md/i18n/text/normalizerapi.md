[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Internationalization
  
**Lesson:** Working with Text

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

[Character and Byte Streams](stream.html)

Normalizing Text

[Home Page](../../index.html)
>
[Internationalization](../index.html)
>
[Working with Text](index.html)

[« Previous](stream.html) • [Trail](../TOC.html) • [Next »](../network/index.html)

# Normalizing Text

*Normalization* is the process by which you can perform certain transformations of
text to make it reconcilable in a way which it may not have been before. Let's
say, you would like searching or sorting text, in this case you need to
normalize that text to account for code points that should be represented as the
same text.

What can be normalized? The normalization is applicable when you need to convert
characters with diacritical marks, change all letters case, decompose ligatures,
or convert half-width katakana characters to full-width characters and so on.

In accordance with the
[Unicode Standard Annex #15](http://www.unicode.org/reports/tr15/
) the Normalizer's API supports
all of the following four Unicode text normalization forms that are defined in
the
[`java.text.Normalizer.Form`](http://download.oracle.com/javase/7/docs/api/java/text/Normalizer.Form.html
):

* NFC – Normalization Form Composition
* NFD – Normalization Form Decomposition
* NFKC – Normalization Form Canonical Composition
* NFKD – Normalization Form Canonical Decomposition

Let's examine how the latin small letter “o” with diaeresis can be normalized by
using these normalization forms:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Original word | **NFC** | **NFD** | **NFKC** | **NFKD** |
| "schön" | "schön" | "scho\u0308n" | "schön" | "scho\u0308n" |

You can notice that an original word is left unchanged in NFC and NFKC. This is
because with NFD and NFKD, composite characters are mapped to their canonical
decompositions. But with NFC and NFKC, combining character sequences are mapped
to composites, if possible. There is no composite for diaeresis, so it is left
decomposed in NFC and NFKC.

In the code example,
[`NormSample.java`](examples/NormSample.java
), which is represented later, you can also notice another
normalization feature. The half-width and full-width katakana characters will
have the same compatibility decomposition and are thus compatibility
equivalents. However, they are not canonical equivalents.

To be sure that you really need to normalize the text you may use the
`isNormalized` method to determine if the given sequence of char values is
normalized. If this method returns false, it means that you have to normalize
this sequence and you should use the `normalize` method which normalizes a
`char` values according to the specified normalization form.
For example, to transform
text into the canonical decomposed form you will have to use the following
`normalize` method:

```

normalized_string = Normalizer.normalize(target_chars, Normalizer.Form.NFD);

```

Also, the normalize method rearranges accents into the proper canonical order,
so that you do not have to worry about accent rearrangement on your own.

The following example represents an application that enables you to select a
normalization form and a template to normalize:

---

**Note:** If you don't see the applet running, you need to install [release 6 of the Java SE Development Kit (JDK)](http://java.sun.com/javase/downloads/index.jsp).

---

[« Previous](stream.html)
•
[Trail](../TOC.html)
•
[Next »](../network/index.html)

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

**Previous page:** Character and Byte Streams
  
**Next page:** Internationalization of Network Resources




A browser with JavaScript enabled is required for this page to operate properly.