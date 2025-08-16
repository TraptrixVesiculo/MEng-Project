[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Internationalization
  
**Lesson:** Isolating Locale-Specific Data

[Isolating Locale-Specific Data](index.html)

[About the ResourceBundle Class](concept.html)

Preparing to Use a ResourceBundle

[Backing a ResourceBundle with Properties Files](propfile.html)

[Using a ListResourceBundle](list.html)

[Customizing Resource Bundle Loading](control.html)

[Home Page](../../index.html)
>
[Internationalization](../index.html)
>
[Isolating Locale-Specific Data](index.html)

[« Previous](concept.html) • [Trail](../TOC.html) • [Next »](propfile.html)

# Preparing to Use a ResourceBundle

### Identifying the Locale-Specific Objects

> If your application has a user interface, it contains many
> locale-specific objects. To get started, you should go through your
> source code and look for objects that vary with `Locale`.
> Your list might include objects instantiated from the following
> classes:
>
> * `String`* `Image`* `Color`* `AudioClip`
>
> You'll notice that this list doesn't contain objects representing
> numbers, dates, times, or currencies. The display format of these
> objects varies with `Locale`, but the objects themselves do
> not. For example, you format a `Date` according to
> `Locale`, but you use the same `Date` object
> regardless of `Locale`. Instead of isolating these objects
> in a `ResourceBundle`, you format them with special
> locale-sensitive formatting classes. You'll learn how to do this in the
> [Dates and Times](../format/dateintro.html)
> section of the
> [Formatting](../format/index.html) lesson.
>
> In general, the objects stored in a `ResourceBundle` are
> predefined and ship with the product. These objects are not modified
> while the program is running. For instance, you should store a
> `Menu` label in a `ResourceBundle` because it is
> locale-specific and will not change during the program session.
> However, you should not isolate in a `ResourceBundle` a
> `String` object the end user enters in a
> `TextField`. Data such as this `String` may vary
> from day to day. It is specific to the program session, not to the
> `Locale` in which the program runs.
>
> Usually most of the objects you need to isolate in a
> `ResourceBundle` are `String` objects. However,
> not all `String` objects are locale-specific. For example,
> if a `String` is a protocol element used by interprocess
> communication, it doesn't need to be localized, because the end users
> never see it.
>
> The decision whether to localize some `String` objects is
> not always clear. Log files are a good example. If a log file is
> written by one program and read by another, both programs are using the
> log file as a buffer for communication. Suppose that end users
> occasionally check the contents of this log file. Shouldn't the log
> file be localized? On the other hand, if end users rarely check the log
> file, the cost of translation may not be worthwhile. Your decision to
> localize this log file depends on a number of factors: program design,
> ease of use, cost of translation, and supportability.

### Organizing ResourceBundle Objects

> You can organize your `ResourceBundle` objects according to
> the category of objects they contain. For example, you might want to
> load all of the GUI labels for an order entry window into a
> `ResourceBundle` called `OrderLabelsBundle`.
> Using multiple `ResourceBundle` objects offers several
> advantages:
>
> * Your code is easier to read and to maintain.* You'll avoid huge `ResourceBundle`
>     objects, which may take too long to load into memory.* You can reduce memory usage by loading each
>       `ResourceBundle` only when needed.

[« Previous](concept.html)
•
[Trail](../TOC.html)
•
[Next »](propfile.html)

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

**Previous page:** About the ResourceBundle Class
  
**Next page:** Backing a ResourceBundle with Properties Files




A browser with JavaScript enabled is required for this page to operate properly.