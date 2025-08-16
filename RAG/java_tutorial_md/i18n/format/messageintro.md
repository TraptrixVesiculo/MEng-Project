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

[Dates and Times](dateintro.html)

[Using Predefined Formats](dateFormat.html)

[Customizing Formats](simpleDateFormat.html)

[Changing Date Format Symbols](dateFormatSymbols.html)

Messages

[Dealing with Compound Messages](messageFormat.html)

[Handling Plurals](choiceFormat.html)

[Home Page](../../index.html)
>
[Internationalization](../index.html)
>
[Formatting](index.html)

[« Previous](dateFormatSymbols.html) • [Trail](../TOC.html) • [Next »](messageFormat.html)

# Messages

We all like to use programs that let us know what's going on. Programs
that keep us informed often do so by displaying status and error
messages. Of course, these messages need to be translated so they can
be understood by end users around the world. The section [Isolating Locale-Specific
Data](../resbundle/index.html) discusses translatable text messages. Usually, you're done
after you move a message `String` into a
`ResourceBundle`. However, if you've embedded variable data
in a message, you'll have to take some extra steps to prepare it for
translation.

A *compound message* contains variable data. In the following
list of compound messages, the variable data is underlined:

```

The disk named MyDisk contains 300 files.
The current balance of account #34-09-222 is $2,745.72.
405,390 people have visited your website since January 1, 2009.
Delete all files older than 120 days.

```

You might be tempted to construct the last message in the preceding
list by concatenating phrases and variables as follows:

```

double numDays;
ResourceBundle msgBundle;
...
String message = msgBundle.getString("deleteolder" 
				     + numDays.toString()  
				     + msgBundle.getString("days"));

```

This approach works fine in English, but it won't work for languages in
which the verb appears at the end of the sentence. Because the word
order of this message is hardcoded, your localizers won't be able to
create grammatically correct translations for all languages.

How can you make your program localizable if you need to use compound
messages? You can do so by using the `MessageFormat` class,
which is the topic of this section.

---

**Caution:** 
Compound messages are difficult to translate because the message text
is fragmented. If you use compound messages, localization will take
longer and cost more. Therefore you should use compound messages only
when necessary.

---

### [Dealing with Compound Messages](messageFormat.html)

> A compound message
> may contain
> several kinds
> of variables: dates, times, strings, numbers,
> currencies, and percentages.
> To format a compound message
> in a locale-independent manner,
> you construct
> a pattern that you apply to a
> `MessageFormat` object.

### [Handling Plurals](choiceFormat.html)

> The words in a message usually vary if
> both plural and singular word forms are possible.
> With the `ChoiceFormat` class,
> you can map a number to a word or phrase,
> allowing you to
> construct messages that are
> grammatically correct.

[« Previous](dateFormatSymbols.html)
•
[Trail](../TOC.html)
•
[Next »](messageFormat.html)

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

**Previous page:** Changing Date Format Symbols
  
**Next page:** Dealing with Compound Messages




A browser with JavaScript enabled is required for this page to operate properly.