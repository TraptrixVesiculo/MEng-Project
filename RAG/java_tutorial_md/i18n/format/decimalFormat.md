[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Internationalization
  
**Lesson:** Formatting
  
**Section:** Numbers and Currencies

[Formatting](index.html)

[Numbers and Currencies](numberintro.html)

[Using Predefined Formats](numberFormat.html)

Customizing Formats

[Dates and Times](dateintro.html)

[Using Predefined Formats](dateFormat.html)

[Customizing Formats](simpleDateFormat.html)

[Changing Date Format Symbols](dateFormatSymbols.html)

[Messages](messageintro.html)

[Dealing with Compound Messages](messageFormat.html)

[Handling Plurals](choiceFormat.html)

[Home Page](../../index.html)
>
[Internationalization](../index.html)
>
[Formatting](index.html)

[« Previous](numberFormat.html) • [Trail](../TOC.html) • [Next »](dateintro.html)

# Customizing Formats

You can use the `DecimalFormat` class to format decimal
numbers into locale-specific strings. This class allows you to control
the display of leading and trailing zeros, prefixes and suffixes,
grouping (thousands) separators, and the decimal separator. If you want
to change formatting symbols, such as the decimal separator, you can
use the `DecimalFormatSymbols`  in conjunction with the
`DecimalFormat` class. These classes offer a great deal of
flexibility in the formatting of numbers, but they can make your code
more complex.

The text that follows uses examples that demonstrate the
`DecimalFormat`  and `DecimalFormatSymbols`
classes. The code examples in this material are from a sample program
called
[`DecimalFormatDemo`](examples/DecimalFormatDemo.java).

### Constructing Patterns

> You specify the formatting properties of `DecimalFormat`
> with a pattern `String`. The pattern determines what the
> formatted number looks like. For a full description of the pattern
> syntax, see
> [`Number Format Pattern Syntax`](#numberpattern).
>
> The example that follows creates a formatter by passing a pattern
> `String` to the `DecimalFormat` constructor. The
> `format` method accepts a `double` value as an
> argument and returns the formatted number in a `String`:
>
> ```
>
> DecimalFormat myFormatter = new DecimalFormat(pattern);
> String output = myFormatter.format(value);
> System.out.println(value + " " + pattern + " " + output);
>
> ```
>
> The output for the preceding lines of code is described in the
> following table. The `value` is the number, a
> `double` , that is to be formatted. The `pattern`
> is the `String` that specifies the formatting properties.
> The `output`, which is a `String`, represents the
> formatted number.
>
> ### Output from `DecimalFormatDemo` Program
>
> | `value` | `pattern` | `output` | Explanation |
> | 123456.789 | ###,###.### | 123,456.789 | The pound sign (#) denotes a digit, the comma is a placeholder for the grouping separator, and the period is a placeholder for the decimal separator. |
> | 123456.789 | ###.## | 123456.79 | The `value` has three digits to the right of the decimal point, but the `pattern` has only two. The `format` method handles this by rounding up. |
> | 123.78 | 000000.000 | 000123.780 | The `pattern` specifies leading and trailing zeros, because the 0 character is used instead of the pound sign (#). |
> | 12345.67 | $###,###.### | $12,345.67 | The first character in the `pattern` is the dollar sign ($). Note that it immediately precedes the leftmost digit in the formatted `output`. |
> | 12345.67 | \u00A5###,###.### | ¥12,345.67 | The `pattern` specifies the currency sign for Japanese yen (¥) with the Unicode value 00A5. |

### Locale-Sensitive Formatting

> The preceding example created a `DecimalFormat` object for
> the default `Locale`. If you want a
> `DecimalFormat` object for a nondefault `Locale`,
> you instantiate a `NumberFormat` and then cast it to
> `DecimalFormat`. Here's an example:
>
> ```
>
> NumberFormat nf = NumberFormat.getNumberInstance(loc);
> DecimalFormat df = (DecimalFormat)nf;
> df.applyPattern(pattern);
> String output = df.format(value);
> System.out.println(pattern + " " + output + " " + 
> 	           loc.toString());
>
> ```
>
> Running the previous code example results in the output that follows.
> The formatted number, which is in the second column, varies with
> `Locale`:
>
> ```
>
> ###,###.###	 123,456.789	 en_US
> ###,###.###	 123.456,789	 de_DE
> ###,###.###	 123 456,789	 fr_FR
>
> ```
>
> So far the formatting patterns discussed here follow the conventions of
> U.S. English. For example, in the pattern ###,###.## the comma is the
> thousands-separator and the period represents the decimal point. This
> convention is fine, provided that your end users aren't exposed to it.
> However, some applications, such as spreadsheets and report generators,
> allow the end users to define their own formatting patterns. For these
> applications the formatting patterns specified by the end users should
> use localized notation. In these cases you'll want to invoke the
> `applyLocalizedPattern` method on the
> `DecimalFormat` object.

### Altering the Formatting Symbols

> You can use the
> [DecimalFormatSymbols](http://download.oracle.com/javase/7/docs/api/java/text/DecimalFormatSymbols.html) class to change the symbols that appear in the formatted numbers
> produced by the `format` method. These symbols include the
> decimal separator, the grouping separator, the minus sign, and the
> percent sign, among others.
>
> The next example demonstrates the `DecimalFormatSymbols`
> class by applying a strange format to a number. The unusual format is
> the result of the calls to the `setDecimalSeparator`,
> `setGroupingSeparator`, and `setGroupingSize`
> methods.
>
> ```
>
> DecimalFormatSymbols unusualSymbols =
>     new DecimalFormatSymbols(currentLocale);
> unusualSymbols.setDecimalSeparator('|');
> unusualSymbols.setGroupingSeparator('^');
>
> String strange = "#,##0.###";
> DecimalFormat weirdFormatter = 
>                new DecimalFormat(strange, unusualSymbols);
> weirdFormatter.setGroupingSize(4);
>
> String bizarre = weirdFormatter.format(12345.678);
> System.out.println(bizarre);
>
> ```
>
> When run, this example prints the number in a bizarre format:
>
> ```
>
> 1^2345|678
>
> ```
>
> ### Number Format Pattern Syntax
>
> You can design your own format patterns for numbers
> by following the rules specified by the
> following BNF diagram:
>
> ```
>
> pattern    := subpattern{;subpattern}
> subpattern := {prefix}integer{.fraction}{suffix}
> prefix     := '\\u0000'..'\\uFFFD' - specialCharacters
> suffix     := '\\u0000'..'\\uFFFD' - specialCharacters
> integer    := '#'* '0'* '0'
> fraction   := '0'* '#'*
>
> ```
>
> The notation used in the preceding diagram is explained in
> the following table:
> > Notation | Description || ``` X* ``` | 0 or more instances of X |
> > | ``` (X | Y) ``` | either X or Y |
> > | ``` X..Y ``` | any character from X up to Y, inclusive |
> > | ``` S - T ``` | characters in S, except those in T |
> > | ``` {X} ``` | X is optional |
>
> In the preceding BNF diagram, the first subpattern specifies
> the format for positive numbers.
> The second subpattern, which is optional,
> specifies the format for negative numbers.
>
> Although not noted in the BNF diagram,
> a comma may appear within the integer portion.
>
> Within the subpatterns, you specify formatting
> with special symbols. These symbols are described
> in the following table:
> > Symbol | Description || 0 | a digit |
> > | # | a digit, zero shows as absent |
> > | . | placeholder for decimal separator |
> > | , | placeholder for grouping separator |
> > | E | separates mantissa and exponent for exponential formats |
> > | ; | separates formats |
> > | - | default negative prefix |
> > | % | multiply by 100 and show as percentage |
> > | ? | multiply by 1000 and show as per mille |
> > | ¤ | currency sign; replaced by currency symbol; if doubled, replaced by international currency symbol; if present in a pattern, the monetary decimal separator is used instead of the decimal separator |
> > | X | any other characters can be used in the prefix or suffix |
> > | ' | used to quote special characters in a prefix or suffix |

[« Previous](numberFormat.html)
•
[Trail](../TOC.html)
•
[Next »](dateintro.html)

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

**Previous page:** Using Predefined Formats
  
**Next page:** Dates and Times




A browser with JavaScript enabled is required for this page to operate properly.