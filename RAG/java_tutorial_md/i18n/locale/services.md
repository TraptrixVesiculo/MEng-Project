[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Internationalization
  
**Lesson:** Setting the Locale

[Setting the Locale](index.html)

[Creating a Locale](create.html)

[BCP 47 Extensions](extensions.html)

[Identifying Available Locales](identify.html)

[The Scope of a Locale](scope.html)

Locale-Sensitive Services SPI

[Home Page](../../index.html)
>
[Internationalization](../index.html)
>
[Setting the Locale](index.html)

[« Previous](scope.html) • [Trail](../TOC.html) • [Next »](../resbundle/index.html)

# Locale-Sensitive Services SPI

This feature enables the plug-in of locale-dependent data and services. In this
way, third parties are able to provide implementations of most locale-sensitive
classes in the `java.text` and `java.util` packages.

The implementation of SPIs *(Service Provider Interface)*
is based on abstract classes and Java interfaces that are implemented by the service provider. At
runtime the Java class loading mechanism is used to dynamically locate and load
classes that implement the SPI.  

You can use the locale-sensitive services SPI to provide the following locale
sensitive implementations:

* `BreakIterator` objects
* `Collator` objects
* Language code, Country code, and Variant name for the `Locale` class
* Time Zone names
* Currency symbols
* `DateFormat` objects
* `DateFormatSymbol` objects
* `NumberFormat` objects
* `DecimalFormatSymbols` objects

The corresponding SPIs are contained both in `java.text.spi`
and in `java.util.spi` packages:

|  |  |
| --- | --- |
| `java.util.spi` | `java.text.spi` |
| * `CurrencyNameProvider` * `LocaleServiceProvider` * `TimeZoneNameProvider` | * `BreakIteratorProvider` * `CollatorProvider` * `DateFormatProvider` * `DateFormatSymbolsProvider` * `DecimalFormatSymbolsProvider` * `NumberFormatProvider` |

For example, if you would like to provide a `NumberFormat` object for a new
locale, you have to implement the `java.text.spi.NumberFormatProvider`
class. You need to extend this class and implement its methods:

* `getCurrencyInstance(Locale locale)`
* `getIntegerInstance(Locale locale)`
* `getNumberInstance(Locale locale)`
* `getPercentInstance(Locale locale)`

```

  Locale loc = new Locale("da", "DK");
  NumberFormat nf = NumberFormatProvider.getNumberInstance(loc);

These methods first check whether the Java runtime environment supports the 
requested locale; if so, they use that support. 
Otherwise, the methods call the getAvailableLocales() methods of 
installed providers for the appropriate interface to find a provider 
that supports the requested locale.


```

[« Previous](scope.html)
•
[Trail](../TOC.html)
•
[Next »](../resbundle/index.html)

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

**Previous page:** The Scope of a Locale
  
**Next page:** Isolating Locale-Specific Data




A browser with JavaScript enabled is required for this page to operate properly.