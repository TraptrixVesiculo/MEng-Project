[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Internationalization
  
**Lesson:** Formatting
  
**Section:** Messages

[Formatting](index.html)

[Numbers and Currencies](numberintro.html)

[Using Predefined Formats](numberFormat.html)

[Customizing Formats](decimalFormat.html)

[Dates and Times](dateintro.html)

[Using Predefined Formats](dateFormat.html)

[Customizing Formats](simpleDateFormat.html)

[Changing Date Format Symbols](dateFormatSymbols.html)

[Messages](messageintro.html)

Dealing with Compound Messages

[Handling Plurals](choiceFormat.html)

[Home Page](../../index.html)
>
[Internationalization](../index.html)
>
[Formatting](index.html)

[« Previous](messageintro.html) • [Trail](../TOC.html) • [Next »](choiceFormat.html)

# Dealing with Compound Messages

A compound message may contain several kinds of variables: dates,
times, strings, numbers, currencies, and percentages. To format a
compound message in a locale-independent manner, you construct a
pattern that you apply to a `MessageFormat` object, and
store this pattern in a `ResourceBundle`.

By stepping through a sample program, this section demonstrates how to
internationalize a compound message. The sample program makes use of
the
[`MessageFormat`](http://download.oracle.com/javase/7/docs/api/java/text/MessageFormat.html) class.
The full source code for this program is in the file called
[`MessageFormatDemo.java`](examples/MessageFormatDemo.java).
The German locale properties are in the file called
[`MessageBundle_de_DE.properties`](examples/MessageBundle_de_DE.properties).

### 1. Identify the Variables in the Message

> Suppose that you want to internationalize the following message:
>
> ![The following line of text: At 1:15 on April 13, 1998, we detected 7 spaceships on the planet Mars.  The variable data (1:15, April 13,1998, 7, and Mars) have been underlined.](../../figures/i18n/i18n-2.gif)
>
> Notice that we've underlined the variable data and have identified what
> kind of objects will represent this data.

### 2. Isolate the Message Pattern in a ResourceBundle

> Store the message in a `ResourceBundle` named
> `MessageBundle`, as follows:
>
> ```
>
> ResourceBundle messages =
>    ResourceBundle.getBundle("MessageBundle", currentLocale);
>
> ```
>
> This `ResourceBundle` is backed by a properties file for
> each `Locale`. Since the `ResourceBundle` is
> called `MessageBundle`, the properties file for U.S. English
> is named `MessageBundle_en_US.properties`. The contents of
> this file is as follows:
>
> ```
>
> template = At {2,time,short} on {2,date,long}, we detected \
> 	      {1,number,integer} spaceships on the planet {0}.
> planet = Mars
>
> ```
>
> The first line of the properties file contains the message pattern. If
> you compare this pattern with the message text shown in step 1, you'll
> see that an argument enclosed in braces replaces each variable in the
> message text. Each argument starts with a digit called the argument
> number, which matches the index of an element in an `Object`
> array that holds the argument values. Note that in the pattern the
> argument numbers are not in any particular order. You can place the
> arguments anywhere in the pattern. The only requirement is that the
> argument number have a matching element in the array of argument
> values.
>
> The next step discusses the argument value array, but first let's look
> at each of the arguments in the pattern. The following table provides
> some details about the arguments:
>
> ### Arguments for `template` in `MessageBundle_en_US.properties`
>
> | Argument | Description |
> | `{2,time,short}` | The time portion of a `Date` object. The `short` style specifies the `DateFormat.SHORT` formatting style. |
> | `{2,date,long}` | The date portion of a `Date` object. The same `Date` object is used for both the date and time variables. In the `Object` array of arguments the index of the element holding the `Date` object is 2. (This is described in the next step.) |
> | `{1,number,integer}` | A `Number` object, further qualified with the `integer` number style. |
> | `{0}` | The `String` in the `ResourceBundle` that corresponds to the `planet` key. |
>
> For a full description of the argument syntax, see the API documentation for the
> [`MessageFormat`](http://download.oracle.com/javase/7/docs/api/java/text/MessageFormat.html) class.

### 3. Set the Message Arguments

> The following lines of code assign values to each argument in the
> pattern. The indexes of the elements in the
> `messageArguments` array match the argument numbers in the
> pattern. For example, the `Integer`  element at index 1
> corresponds to the `{1,number,integer}` argument in the
> pattern. Because it must be translated, the `String` object
> at element 0 will be fetched from the `ResourceBundle` with
> the `getString` method. Here is the code that defines the
> array of message arguments:
>
> ```
>
> Object[] messageArguments = {
>     messages.getString("planet"),
>     new Integer(7),
>     new Date()
> };
>
> ```

### 4. Create the Formatter

> Next, create a `MessageFormat` object. You set the
> `Locale` because the message contains `Date` and
> `Number` objects, which should be formatted in a
> locale-sensitive manner.
>
> ```
>
> MessageFormat formatter = new MessageFormat("");
> formatter.setLocale(currentLocale);
>
> ```

### 5. Format the Message Using the Pattern and the Arguments

> This step shows how the pattern, message arguments, and formatter all
> work together. First, fetch the pattern `String` from the
> `ResourceBundle`  with the `getString` method.
> The key to the pattern is `template`. Pass the pattern
> `String` to the formatter with the `applyPattern` method. Then format the message using the array of message
> arguments, by invoking the `format` method. The
> `String` returned by the `format` method is ready
> to be displayed. All of this is accomplished with just two lines of
> code:
>
> ```
>
> formatter.applyPattern(messages.getString("template"));
> String output = formatter.format(messageArguments);
>
> ```

### 6. Run the Demo Program

> The demo program prints the translated messages for the English and
> German locales and properly formats the date and time variables. Note
> that the English and German verbs ("detected" and
> "entdeckt") are in different locations relative to the
> variables:
>
> ```
>
> currentLocale = en_US
> At 10:16 AM on July 31, 2009, we detected 7 spaceships on the planet Mars.
> currentLocale = de_DE
> Um 10:16 am 31. Juli 2009 haben wir 7 Raumschiffe auf dem Planeten Mars entdeckt.
>
> ```

[« Previous](messageintro.html)
•
[Trail](../TOC.html)
•
[Next »](choiceFormat.html)

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

**Previous page:** Messages
  
**Next page:** Handling Plurals




A browser with JavaScript enabled is required for this page to operate properly.