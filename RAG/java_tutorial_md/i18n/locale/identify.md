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

Identifying Available Locales

[The Scope of a Locale](scope.html)

[Locale-Sensitive Services SPI](services.html)

[Home Page](../../index.html)
>
[Internationalization](../index.html)
>
[Setting the Locale](index.html)

[« Previous](extensions.html) • [Trail](../TOC.html) • [Next »](scope.html)

# Identifying Available Locales

You can create a `Locale` with any combination of valid
language and country codes, but that doesn't mean that you can use it.
Remember, a `Locale` object is only an identifier. You pass
the `Locale`  object to other objects, which then do the
real work. These other objects, which we call locale-sensitive, do not
know how to deal with all possible `Locale` definitions.

To find out which types of `Locale` definitions a
locale-sensitive class recognizes, you invoke the
`getAvailableLocales` method. For example, to find out which
`Locale` definitions are supported by the
`DateFormat` class, you could write a routine such as the
following:

```

import java.util.*;
import java.text.*;

public class Available {
    static public void main(String[] args) {
	Locale list[] = DateFormat.getAvailableLocales();
	for (Locale aLocale : list) {
	    System.out.println(aLocale.toString());
	}
    }
}

```

Note that the
`String` returned by `toString` contains the
language and country codes, separated by an underscore:

```

ar_EG
be_BY
bg_BG
ca_ES
cs_CZ
da_DK
de_DE
.
.
.

```

If you want to display a list of `Locale` names to end
users, you should show them something easier to understand than the
language and country codes returned by `toString`. Instead
you can invoke the `Locale.getDisplayName` method, which
retrieves a localized `String` of a `Locale`
object. For example, when `toString` is replaced by
`getDisplayName` in the preceding code, the program prints
the following lines:

```

Arabic (Egypt)
Belarussian (Belarus)
Bulgarian (Bulgaria)
Catalan (Spain)
Czech (Czech Republic)
Danish (Denmark)
German (Germany)
.
.
.

```

You may see different locale lists depending on the Java Platform implementations.

[« Previous](extensions.html)
•
[Trail](../TOC.html)
•
[Next »](scope.html)

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

**Previous page:** BCP 47 Extensions
  
**Next page:** The Scope of a Locale




A browser with JavaScript enabled is required for this page to operate properly.