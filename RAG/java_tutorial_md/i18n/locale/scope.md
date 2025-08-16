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

The Scope of a Locale

[Locale-Sensitive Services SPI](services.html)

[Home Page](../../index.html)
>
[Internationalization](../index.html)
>
[Setting the Locale](index.html)

[« Previous](identify.html) • [Trail](../TOC.html) • [Next »](services.html)

# The Scope of a Locale

The Java platform does not require you to use the same
`Locale` throughout your program. If you wish, you can
assign a different `Locale` to every locale-sensitive object
in your program. This flexibility allows you to develop multilingual
applications, which can display information in multiple languages.

However, most applications are not multi-lingual and their
locale-sensitive objects rely on the default `Locale`. Set
by the Java Virtual Machine when it starts up, the default
`Locale` corresponds to the locale of the host platform.
To determine the default `Locale` of your Java Virtual Machine,
invoke the `Locale.getDefault` method.

---

**Note:** It is possible to independently set the default locale for two types of uses:
the *format* setting is used for formatting resources,
and the *display* setting is used in menus and dialogs.
Introduced in the Java SE 7 release, the
[`Locale.getDefault(Locale.Category)`](http://download.oracle.com/javase/7/docs/api/java/util/Locale.html#getDefault(java.util.Locale.Category)) method takes a
[`Locale.Category`](http://download.oracle.com/javase/7/docs/api/java/util/Locale.Category.html) parameter. Passing the `FORMAT` enum to the
`getDefault(Locale.Category)` method returns the default
locale for formatting resources.
Similiarly, passing the `DISPLAY` enum
returns the default locale used by the UI. The corresponding
[`setDefault(Locale.Category, Locale)`](http://download.oracle.com/javase/7/docs/api/java/util/Locale.html#setDefault%28java.util.Locale.Category,%20java.util.Locale%29) method allows setting the locale for the desired category.
The no-argument `getDefault` method returns the
`DISPLAY` default value.

On the Windows platform, these default values are initialized
according to the "Standards and Formats" and "Display Language"
settings in the Windows control panel.

---

You should not set
the default `Locale` programmatically because it is shared
by all locale-sensitive classes.

Distributed computing raises some interesting issues. For example,
suppose you are designing an application server that will receive
requests from clients in various countries. If the `Locale`
for each client is different, what should be the `Locale` of
the server? Perhaps the server is multithreaded, with each thread set
to the `Locale`  of the client it services. Or perhaps all
data passed between the server and the clients should be
locale-independent.

Which design approach should you take? If possible, the data passed
between the server and the clients should be locale-independent. This
simplifies the design of the server by making the clients responsible
for displaying the data in a locale-sensitive manner. However, this
approach won't work if the server must store the data in a
locale-specific form. For example, the server might store Spanish,
English, and French versions of the same data in different database
columns. In this case, the server might want to query the client for
its `Locale`, since the `Locale` may have changed
since the last request.

[« Previous](identify.html)
•
[Trail](../TOC.html)
•
[Next »](services.html)

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

**Previous page:** Identifying Available Locales
  
**Next page:** Locale-Sensitive Services SPI




A browser with JavaScript enabled is required for this page to operate properly.