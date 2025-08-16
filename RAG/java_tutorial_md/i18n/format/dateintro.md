[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Internationalization
  
**Lesson:** Formatting

[Formatting](index.html)

[Numbers and Currencies](numberintro.html)

[Using Predefined Formats](numberFormat.html)

[Customizing Formats](decimalFormat.html)

Dates and Times

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

[« Previous](decimalFormat.html) • [Trail](../TOC.html) • [Next »](dateFormat.html)

# Dates and Times

`Date` objects represent dates and times. You cannot display
or print a `Date` object without first converting it to a
`String` that is in the proper format. Just what is the
"proper" format? First, the format should conform to the
conventions of the end user's `Locale`. For example, Germans
recognize `20.4.09` as a valid date, but Americans expect
that same date to appear as `4/20/09`. Second, the format
should include the necessary information. For instance, a program that
measures network performance may report on elapsed milliseconds. An
online appointment calendar probably won't display milliseconds, but it
will show the days of the week.

This section explains how to format dates and times in various ways and
in a locale-sensitive manner. If you follow these techniques your
programs will display dates and times in the appropriate
`Locale`, but your source code will remain independent of
any specific `Locale`.

### [Using Predefined Formats](dateFormat.html)

> The `DateFormat` class provides predefined
> formatting styles that are locale-specific and easy to use.

### [Customizing Formats](simpleDateFormat.html)

> With the `SimpleDateFormat` class, you can create customized,
> locale-specific formats.

### [Changing Date Format Symbols](dateFormatSymbols.html)

> Using the `DateFormatSymbols` class, you can change the symbols
> that represent the names of months, days of the week, and other
> formatting elements.

[« Previous](decimalFormat.html)
•
[Trail](../TOC.html)
•
[Next »](dateFormat.html)

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

**Previous page:** Customizing Formats
  
**Next page:** Using Predefined Formats




A browser with JavaScript enabled is required for this page to operate properly.