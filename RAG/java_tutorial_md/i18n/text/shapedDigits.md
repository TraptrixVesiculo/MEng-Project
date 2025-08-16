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

Converting Latin Digits to Other Unicode Digits

[Converting Non-Unicode Text](convertintro.html)

[Byte Encodings and Strings](string.html)

[Character and Byte Streams](stream.html)

[Normalizing Text](normalizerapi.html)

[Home Page](../../index.html)
>
[Internationalization](../index.html)
>
[Working with Text](index.html)

[« Previous](line.html) • [Trail](../TOC.html) • [Next »](convertintro.html)

# Converting Latin Digits to Other Unicode Digits

By default, when text contains numeric values, those values are
displayed using Latin (European) digits. When other Unicode digit
shapes are preferred, use the
[`java.awt.font.NumericShaper`](/java/awt/font/NumericShaper.html) class. The `NumericShaper` API enables you to
display a numeric value represented internally as an ASCII value
in any Unicode digit shape.

The following code snippet, from the
[`ArabicDigits`](examples/ArabicDigits.java) example, shows how to use a `NumericShaper`
instance to convert Latin digits to Arabic digits.
The line that determines the shaping action is bolded.

```

    ArabicDigitsPanel(String fontname) {
        HashMap map = new HashMap();
        Font font = new Font(fontname, Font.PLAIN, 60);
        map.put(TextAttribute.FONT, font);
        map.put(TextAttribute.NUMERIC_SHAPING,
      	    NumericShaper.getShaper(NumericShaper.ARABIC));
        FontRenderContext frc = new FontRenderContext(null, false, false);
        layout = new TextLayout(text, map, frc);
    }

   ...

   public void paint(Graphics g) {
       Graphics2D g2d = (Graphics2D)g;
       layout.draw(g2d, 10, 50);
    }

```

The `NumericShaper` instance for Arabic digits is fetched
and placed into a `HashMap` for the
[`TextLayout.NUMERIC_SHAPING`](/java/awt/font/TextAttribute.html#NUMERIC_SHAPING) attribute key. The hash map is passed to the `TextLayout` instance.
After rendering the text in the `paint`
method, the digits are displayed in the desired script. In this example,
the Latin digits, 0 through 9, are drawn as Arabic digits.

![ArabicDigits example output showing Arabic digits from 0 through 9](../../figures/i18n/ArabicDigits.png)

The previous example uses the `NumericShaper.ARABIC` constant
to retrieve the desired shaper, but the
[`NumericShaper`](/java/awt/font/NumericShaper.html#field_summary) class provides constants for many languages. These constants are
defined as bit masks and are referred to as the
`NumericShaper` *bit mask-based constants*.

### Enum-Based Range Constants

An alternative way to specify a particular set of digits is to use the
[`NumericShaper.Range`](/java/awt/font/NumericShaper.Range.html) enumerated type (enum). This enum, introduced in the Java SE 7 release,
also provides a set of
[constants](/java/awt/font/NumericShaper.Range.html#field_summary). Although these constants are defined using different mechanisms,
the `NumericShaper.ARABIC` bit mask is functionally equivalent
to the `NumericShaper.Range.ARABIC` enum, and
there is a corresponding `getShaper` method for each constant type:

* [`getShaper(int singleRange)`](http://download.oracle.com/javase/7/docs/api/java/awt/font/NumericShaper.html#getShaper(int))* [`getShaper(NumericShaper.Range singleRange)`](http://download.oracle.com/javase/7/docs/api/java/awt/font/NumericShaper.html#getShaper(java.awt.font.NumericShaper.Range))

The
[`ArabicDigitsEnum`](examples/ArabicDigitsEnum.java) example is identical to the ArabicDigits example, except it uses
the `NumericShaper.Range` enum to specify the language script:

```

        ArabicDigitsEnumPanel(String fontname) {
            HashMap map = new HashMap();
            Font font = new Font(fontname, Font.PLAIN, 60);
            map.put(TextAttribute.FONT, font);
            map.put(TextAttribute.NUMERIC_SHAPING,
		NumericShaper.getShaper(NumericShaper.Range.ARABIC));
            FontRenderContext frc = new FontRenderContext(null, false, false);
            layout = new TextLayout(text, map, frc);
	}


```

Both `getShaper` methods accept a `singleRange` parameter.
With either constant type, you can specify a range of script-specific digits.
The bit mask-based constants can be combined using the
`OR` operand, or you can create a set of
`NumericShaper.Range` enums.
The following shows how to define a range using each constant type:

```

NumericShaper.MONGOLIAN | NumericShaper.THAI | NumericShaper.TIBETAN
EnumSet.of(NumericShaper.Range.MONGOLIAN, 
           NumericShaper.Range.THAI,
           NumericShaper.Range.TIBETAN)

```

You can query the `NumericShaper` object to determine which ranges
it supports using either the
[`getRanges`](http://download.oracle.com/javase/7/docs/api/java/awt/font/NumericShaper.html#getRanges()) method for bit mask-based shapers or the
[`getRangeSet`](http://download.oracle.com/javase/7/docs/api/java/awt/font/NumericShaper.html#getRangeSet()) method for enum-based shapers.

---

**Note:** You can use either the traditional bit masked-based constants or
the `Range` enum-based constants.
Here are some considerations when deciding which to use:

* The `Range` API requires JDK 7 or later.* The `Range` API covers more Unicode ranges than the
    bit-masked API.* The bit-mask API is a bit faster than the `Range` API.

---

### Rendering Digits According to Language Context

The
[`ArabicDigits`](examples/ArabicDigits.java) example was designed to use the shaper for a specific
language, but sometimes the digits must be rendered
according to the language context. For example, if the text that
precedes the digits uses the Thai script, Thai digits are preferred.
If the text is displayed in Tibetan, Tibetan digits are preferred.

You can accomplish this using one of the `getContextualShaper`
methods:

* [getContextualShaper(int ranges)](http://download.oracle.com/javase/7/docs/api/java/awt/font/NumericShaper.html#getContextualShaper(int))* [getContextualShaper(int ranges, int defaultContext)](http://download.oracle.com/javase/7/docs/api/java/awt/font/NumericShaper.html#getContextualShaper(int,%20int))* [getContextualShaper(Set<NumericShaper.Range> ranges)](http://download.oracle.com/javase/7/docs/api/java/awt/font/NumericShaper.html#getContextualShaper(java.util.Set))* [getContextualShaper(Set<NumericShaper.Range> ranges, NumericShaper.Range defaultContext)](http://download.oracle.com/javase/7/docs/api/java/awt/font/NumericShaper.html#getContextualShaper(java.util.Set,%20java.awt.font.NumericShaper.Range))

The first two methods use the bit-mask constants, and the
last two use the enum constants. The methods that accept a
`defaultContext` parameter enable you to specify the
initial shaper that is used when numeric values are displayed before
text. When no default context is defined, any leading
digits are displayed using Latin shapes.

The
[`ShapedDigits`](examples/ShapedDigits.java) example shows how shapers work. Five text layouts are displayed:

1. The first layout uses no shaper; all digits are displayed as Latin.- The second layout shapes all digits as Arabic digits,
     regardless of language context.- The third layout employs a contextual shaper that uses Arabic digits.
       The default context is defined to be Arabic.- The fourth layout employs a contextual shaper that uses Arabic digits,
         but the shaper does not specify a default context.- The fifth layout employs a contextual shaper that uses the
           `ALL_RANGES` bit mask,
           but the shaper does not specify a default context.

![ShapedDigits example output illustrating how contextual shapers work](../../figures/i18n/ShapedDigits.png)

The following lines of code show how the shapers, if used, are defined:

1. No shaper is used.- `NumericShaper arabic = NumericShaper.getShaper(NumericShaper.ARABIC);`- `NumericShaper contextualArabic = NumericShaper.getContextualShaper(NumericShaper.ARABIC, NumericShaper.ARABIC);`- `NumericShaper contextualArabicASCII = NumericShaper.getContextualShaper(NumericShaper.ARABIC);`- `NumericShaper contextualAll = NumericShaper.getContextualShaper(NumericShaper.ALL_RANGES);`

See the
[`ShapedDigits.java`](examples/ShapedDigits.java) example for further implementation details.

[« Previous](line.html)
•
[Trail](../TOC.html)
•
[Next »](convertintro.html)

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

**Previous page:** Line Boundaries
  
**Next page:** Converting Non-Unicode Text




A browser with JavaScript enabled is required for this page to operate properly.