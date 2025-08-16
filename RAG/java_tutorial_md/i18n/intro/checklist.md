[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Internationalization
  
**Lesson:** Introduction

[Introduction](index.html)

[A Quick Example](quick.html)

[Before Internationalization](before.html)

[After Internationalization](after.html)

[Running the Sample Program](run.html)

[Internationalizing the Sample Program](steps.html)

Checklist

[Home Page](../../index.html)
>
[Internationalization](../index.html)
>
[Introduction](index.html)

[« Previous](steps.html) • [Trail](../TOC.html) • [Next »](../locale/index.html)

# Checklist

Many programs are not internationalized when first written. These
programs may have started as prototypes, or perhaps they were not
intended for international distribution. If you must internationalize
an existing program, take the following steps:

### Identify Culturally Dependent Data

> Text messages are the most obvious form of data that varies with
> culture. However, other types of data may vary with region or language.
> The following list contains examples of culturally dependent data:
>
> * Messages* Labels on GUI components* Online help* Sounds* Colors* Graphics* Icons* Dates* Times* Numbers* Currencies* Measurements* Phone numbers* Honorifics and personal titles* Postal addresses* Page layouts

### Isolate Translatable Text in Resource Bundles

> Translation is costly. You can help reduce costs by isolating the text
> that must be translated in `ResourceBundle` objects.
> Translatable text includes status messages, error messages, log file
> entries, and GUI component labels. This text is hardcoded into programs
> that haven't been internationalized. You need to locate all occurrences
> of hardcoded text that is displayed to end users. For example, you
> should clean up code like this:
>
> ```
>
> String buttonLabel = "OK";
> ...
> JButton okButton = new JButton(buttonLabel);
>
> ```
>
> See the section
> [Isolating Locale-Specific Data](../resbundle/index.html)
> for details.

### Deal with Compound Messages

> Compound messages contain variable data. In the message "The disk
> contains 1100 files." the integer 1100 may vary. This message is
> difficult to translate because the position of the integer in the
> sentence is not the same in all languages. The following message is not
> translatable, because the order of the sentence elements is hardcoded
> by concatenation:
>
> ```
>
> Integer fileCount;
> ...
> String diskStatus = "The disk contains " + fileCount.toString() 
>                     + " files.";
>
> ```
>
> Whenever possible, you should avoid constructing compound messages,
> because they are difficult to translate. However, if your application
> requires compound messages, you can handle them with the techniques
> described in the section
> [Messages](../format/messageintro.html).

### Format Numbers and Currencies

> If your application displays numbers and currencies, you must format
> them in a locale-independent manner. The following code is not yet
> internationalized, because it will not display the number correctly in
> all countries:
>
> ```
>
> Double amount;
> TextField amountField;
> ...
> String displayAmount = amount.toString();
> amountField.setText(displayAmount);
>
> ```
>
> You should replace the preceding code with a routine that formats the
> number correctly. The Java programming language provides several
> classes that format numbers and currencies. These classes are discussed
> in the section
> [Numbers and Currencies](../format/numberintro.html).

### Format Dates and Times

> Date and time formats differ with region and language. If your code
> contains statements like the following, you need to change it:
>
> ```
>
> Date currentDate = new Date();
> TextField dateField;
> ...
> String dateString = currentDate.toString();
> dateField.setText(dateString);
>
> ```
>
> If you use the date-formatting classes, your application can display
> dates and times correctly around the world. For examples and
> instructions, see the section
> [Dates and Times](../format/dateintro.html).

### Use Unicode Character Properties

> The following code tries to verify that a character is a letter:
>
> ```
>
> char ch;
> ...
> if ((ch >= 'a' && ch <= 'z') || 
>     (ch >= 'A' && ch <= 'Z'))       // WRONG!
>
> ```
>
> Watch out for code like this, because it won't work with languages
> other than English. For example, the `if` statement misses
> the character ü in the German word Grün.
>
> The `Character` comparison methods use the Unicode standard
> to identify character properties. Thus you should replace the previous
> code with the following:
>
> ```
>
> char ch;
> ...
> if (Character.isLetter(ch))
>
> ```
>
> For more information on the `Character` comparison methods,
> see the section
> [Checking Character Properties](../text/charintro.html).

### Compare Strings Properly

> When sorting text you often compare strings. If the text is displayed,
> you shouldn't use the comparison methods of the `String`
> class. A program that hasn't been internationalized might compare
> strings as follows:
>
> ```
>
> String target;
> String candidate;
> ...
> if (target.equals(candidate)) {
> ...
> if (target.compareTo(candidate) < 0) {
> ...
>
> ```
>
> The `String.equals` and `String.compareTo`
> methods perform binary comparisons, which are ineffective when sorting
> in most languages. Instead you should use the `Collator`
> class, which is described in the section
> [Comparing Strings](../text/collationintro.html).

### Convert Non-Unicode Text

> Characters in the Java programming language are encoded in Unicode. If
> your application handles non-Unicode text, you might need to translate
> it into Unicode. For more information, see the section
> [Converting Non-Unicode Text](../text/convertintro.html).

[« Previous](steps.html)
•
[Trail](../TOC.html)
•
[Next »](../locale/index.html)

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

**Previous page:** Internationalizing the Sample Program
  
**Next page:** Setting the Locale




A browser with JavaScript enabled is required for this page to operate properly.