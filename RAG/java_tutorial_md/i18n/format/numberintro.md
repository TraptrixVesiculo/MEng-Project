[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Internationalization
  
**Lesson:** Formatting

[Formatting](index.html)

Numbers and Currencies

[Using Predefined Formats](numberFormat.html)

[Customizing Formats](decimalFormat.html)

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

[« Previous](index.html) • [Trail](../TOC.html) • [Next »](numberFormat.html)

# Numbers and Currencies

Programs store and operate on numbers in a locale-independent way.
Before displaying or printing a number, a program must convert it to a
`String` that is in a locale-sensitive format. For example,
in France the number 123456.78 should be formatted as 123 456,78, and
in Germany it should appear as 123.456,78. In this section, you will
learn how to make your programs independent of the locale conventions
for decimal points, thousands-separators, and other formatting
properties.

### [Using Predefined Formats](numberFormat.html)

> Using the factory methods provided by the
> `NumberFormat` class,
> you can get locale-specific
> formats for numbers, currencies, and percentages.

### [Formatting with Patterns](decimalFormat.html)

> With the `DecimalFormat`
> class you specify a number's format
> with a `String` pattern.
> The `DecimalFormatSymbols` class
> allows you to modify formatting symbols
> such as decimal separators and minus signs.

[« Previous](index.html)
•
[Trail](../TOC.html)
•
[Next »](numberFormat.html)

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

**Previous page:** Formatting
  
**Next page:** Using Predefined Formats




A browser with JavaScript enabled is required for this page to operate properly.