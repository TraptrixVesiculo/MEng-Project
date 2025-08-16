[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Internationalization
  
**Lesson:** Formatting
  
**Section:** Dates and Times

[Formatting](index.html)

[Numbers and Currencies](numberintro.html)

[Using Predefined Formats](numberFormat.html)

[Customizing Formats](decimalFormat.html)

[Dates and Times](dateintro.html)

[Using Predefined Formats](dateFormat.html)

[Customizing Formats](simpleDateFormat.html)

Changing Date Format Symbols

[Messages](messageintro.html)

[Dealing with Compound Messages](messageFormat.html)

[Handling Plurals](choiceFormat.html)

[Home Page](../../index.html)
>
[Internationalization](../index.html)
>
[Formatting](index.html)

[« Previous](simpleDateFormat.html) • [Trail](../TOC.html) • [Next »](messageintro.html)

# Changing Date Format Symbols

The `format` method of the `SimpleDateFormat`
class returns a `String` composed of digits and symbols. For
example, in the `String` "Friday, April 10, 2009,"
the symbols are "Friday" and "April." If the
symbols encapsulated in `SimpleDateFormat` don't meet your
needs, you can change them with the
[`DateFormatSymbols`](http://download.oracle.com/javase/7/docs/api/java/text/DateFormatSymbols.html). You can change symbols that represent names for months, days of the
week, and time zones, among others. The following table lists the
`DateFormatSymbols` methods that allow you to modify the
symbols:

### `DateFormatSymbol` Methods

| Setter Method | Example of a Symbol the Method Modifies |
| `setAmPmStrings` | PM |
| `setEras` | AD |
| `setMonths` | December |
| `setShortMonths` | Dec |
| `setShortWeekdays` | Tue |
| `setWeekdays` | Tuesday |
| `setZoneStrings` | PST |

The following example invokes `setShortWeekdays` to change
the short names of the days of the week from lowercase to uppercase
characters. The full source code for this example is in
[`DateFormatSymbolsDemo`](examples/DateFormatSymbolsDemo.java).
The first element in the array argument of
`setShortWeekdays` is a null `String`. Therefore
the array is one-based rather than zero-based. The
`SimpleDateFormat` constructor accepts the modified
`DateFormatSymbols` object as an argument. Here is the
source code:

```

Date today;
String result;
SimpleDateFormat formatter;
DateFormatSymbols symbols;
String[] defaultDays;
String[] modifiedDays;

symbols = new DateFormatSymbols(new Locale("en","US"));
defaultDays = symbols.getShortWeekdays();

for (int i = 0; i < defaultDays.length; i++) {
    System.out.print(defaultDays[i] + " ");
}
System.out.println();

String[] capitalDays = {
			"", "SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"};
symbols.setShortWeekdays(capitalDays);

modifiedDays = symbols.getShortWeekdays();
for (int i = 0; i < modifiedDays.length; i++) {
    System.out.print(modifiedDays[i] + " ");
}
System.out.println();
System.out.println();

formatter = new SimpleDateFormat("E", symbols);
today = new Date();
result = formatter.format(today);
System.out.println(result);

```

The preceding code generates this output:

```

   Sun	 Mon	 Tue	 Wed	 Thu	 Fri	 Sat
   SUN	 MON	 TUE	 WED	 THU	 FRI	 SAT

WED

```

[« Previous](simpleDateFormat.html)
•
[Trail](../TOC.html)
•
[Next »](messageintro.html)

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
  
**Next page:** Messages




A browser with JavaScript enabled is required for this page to operate properly.