[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Internationalization
  
**Lesson:** Setting the Locale

[Setting the Locale](index.html)

[Creating a Locale](create.html)

BCP 47 Extensions

[Identifying Available Locales](identify.html)

[The Scope of a Locale](scope.html)

[Locale-Sensitive Services SPI](services.html)

[Home Page](../../index.html)
>
[Internationalization](../index.html)
>
[Setting the Locale](index.html)

[« Previous](create.html) • [Trail](../TOC.html) • [Next »](identify.html)

# BCP 47 Extensions

The Java SE 7 release conforms to the IETF BCP 47 standard, which supports
adding extensions to a `Locale`.
Any single character can be used to denote an extension, but there
are two predefined extension codes:
`'u'` specifies a *Unicode locale extension*,
and `'x'` specifies a *private use extension*.

Unicode locale extensions are defined by the Unicode
[Common Locale Data Repository
(CLDR)](http://cldr.unicode.org/) project. They are used to specify information that is
non-language-specific such as calendars or currency.
A private use extension may be used to specify
any other information, such as platform (for example, Windows, UNIX,
or Linux),
or release information (for example, 6u23 or JDK 7).

An extension is specified as a key/value pair, where the key
is a single character (typically `'u'` or `'x'`).
A well-formed value has the following format:

```

SUBTAG ('-' SUBTAG)*

```

In this format:

```

SUBTAG = [0-9a-zA-Z]{2,8}    For key='u'
SUBTAG = [0-9a-zA-Z]{1,8}    For key='x'

```

Note that a single-character value is allowed for the private
use extension. However, there is a 2-character minimum for values
in the Unicode locale extension.

Extension strings are case-insensitive, but the `Locale`
class maps all keys and values to lowercase.

The
[`getExtensionKeys()`](http://download.oracle.com/javase/7/docs/api/java/util/Locale.html#getExtensionKeys()) method returns the set of extension keys, if any, for a
`Locale`. The
[`getExtension(key)`](http://download.oracle.com/javase/7/docs/api/java/util/Locale.html#getExtension(char)) method returns the value string for the specified key, if any.
### Unicode Locale Extensions
As previously mentioned, a Unicode locale extension is specified by
the `'u'` key code or the `UNICODE_LOCALE_EXTENSION`
constant. The value itself is also specified by a key/type pair.
Legal values are defined in the
[Key/Type
Definitions](http://www.unicode.org/reports/tr35/#Key_Type_Definitions) table on the [Unicode](http://www.unicode.org)
website. A key code is specified by two alphabetic characters.
The following table lists the Unicode locale extension keys:

| Key Code | Description |
| --- | --- |
| ca | calendar algorithm |
| co | collation type |
| ka | collation parameters |
| cu | currency type |
| nu | number type |
| va | common variant type |

---

**Note:** Specifying a Unicode locale extension, such as number format,
does not guarantee that the locale services for the underlying platform
will honor that request.

---

The following table shows some examples of key/type pairs for a
Unicode locale extension.

| Key/Type pair | Description |
| --- | --- |
| ca-buddhist | Thai Buddhist calendar |
| co-pinyin | Pinyin ordering for Latin |
| cu-usd | U.S. dollars |
| nu-jpanfin | Japanese financial numerals |
| tz-aldav | Europe/Andorra |

The following string represents
the German language locale for the country of Germany using a phonebook
style of ordering for the Linux platform. This example also contains
an attribute named `"email"`.

```

de-DE-u-email-co-phonebk-x-linux

```

The following `Locale` methods can be used to access
information about the Unicode locale extensionss. These methods
are described using the previous German locale example.

* [`getUnicodeLocaleKeys()`](http://download.oracle.com/javase/7/docs/api/java/util/Locale.html#getUnicodeLocaleKeys()) – Returns the Unicode locale key codes or an empty set if the
  locale has none. For the German example, this would return
  a set containing the single string `"co"`.* [`getUnicodeLocaleType(String)`](http://download.oracle.com/javase/7/docs/api/java/util/Locale.html#getUnicodeLocaleType(java.lang.String)) – Returns the Unicode locale type associated with the Unicode locale
    key code.
    Invoking `getUnicodeLocaleType("co")`
    for the German example would return the string `"phonebk"`.* [`getUnicodeLocaleAttributes()`](http://download.oracle.com/javase/7/docs/api/java/util/Locale.html#getUnicodeLocaleAttributes()) – Returns the set of Unicode locale attributes associated
      with this locale, if any. In the German example, this would return a set
      containing the single string `"email"`.

### Private Use Extensions
The private use extension, specified by the `'x'` key code or
the `PRIVATE_USE_EXTENSION` constant, can be
anything, as long as the value is well formed.

The following are examples of possible private use extensions:

```

x-jdk-1-7
x-linux

```

[« Previous](create.html)
•
[Trail](../TOC.html)
•
[Next »](identify.html)

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

**Previous page:** Creating a Locale
  
**Next page:** Identifying Available Locales




A browser with JavaScript enabled is required for this page to operate properly.