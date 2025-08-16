[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

Setting the Locale

[Creating a Locale](create.html)

[BCP 47 Extensions](extensions.html)

[Identifying Available Locales](identify.html)

[The Scope of a Locale](scope.html)

[Locale-Sensitive Services SPI](services.html)

**Trail:** Internationalization

[Home Page](../../index.html)
>
[Internationalization](../index.html)

[« Previous](../intro/index.html) • [Trail](../TOC.html) • [Next »](create.html)

# Lesson: Setting the Locale

An internationalized program can display information differently
throughout the world. For example, the program will display different
messages in Paris, Tokyo, and New York. If the localization process has
been fine-tuned, the program will display different messages in New
York and London to account for the differences between American and
British English. How does an internationalized program identify the
appropriate language and region of its end users? Easy. It references a
`Locale` object.

A `Locale` object is an identifier for a particular
combination of language and region. If a class varies its behavior
according to `Locale`, it is said to be
*locale-sensitive*. For example, the `NumberFormat`
class is locale-sensitive; the format of the number it returns depends
on the `Locale`. Thus `NumberFormat` may return a
number as 902 300 (France), or 902.300 (Germany), or 902,300 (United
States). `Locale` objects are only identifiers. The real
work, such as formatting and detecting word boundaries, is performed by
the methods of the locale-sensitive classes.

The following sections explain how to work with `Locale` objects:

### [Creating a Locale](create.html)

> When creating a `Locale` object, you usually specify a
> language code and a country code. A third parameter, the variant, is
> optional.

### [Identifying Available Locales](identify.html)

> Locale-sensitive classes support only certain `Locale`
> definitions. This section shows you how to determine which `Locale` definitions are supported.

### [The Scope of a Locale](scope.html)

> On the Java platform you do not specify a global
> `Locale` by setting an environment variable before running
> the application. Instead you either rely on the default Locale or
> assign a `Locale` to each locale-sensitive object.

### [Locale-Sensitive Services SPI](services.html)

> This section explains how to enable plug-in of locale-dependent data and services.
> These SPIs provides support of more locales in addition to the currently available locales.

[« Previous](../intro/index.html)
•
[Trail](../TOC.html)
•
[Next »](create.html)

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

**Previous page:** Previous Lesson
  
**Next page:** Creating a Locale




A browser with JavaScript enabled is required for this page to operate properly.