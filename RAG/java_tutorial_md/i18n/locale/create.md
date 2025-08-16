[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Internationalization
  
**Lesson:** Setting the Locale

[Setting the Locale](index.html)

Creating a Locale

[BCP 47 Extensions](extensions.html)

[Identifying Available Locales](identify.html)

[The Scope of a Locale](scope.html)

[Locale-Sensitive Services SPI](services.html)

[Home Page](../../index.html)
>
[Internationalization](../index.html)
>
[Setting the Locale](index.html)

[« Previous](index.html) • [Trail](../TOC.html) • [Next »](extensions.html)

# Creating a Locale

There are several ways to create a `Locale` object.
Regardless of the technique used,
creation can be as simple as specifying the language code. However,
you can further distinguish the locale by setting the region
(also referred to as "country") and variant codes.
If you are using the Java SE 7 release or later,
you can also specify the script code and Unicode locale extensions.

The four ways to create a `Locale` object are:

* [`Locale.Builder` Class](#builder)* [`Locale` Constructors](#constructors)* [`Locale.forLanguageTag` Factory Method](#factory)* [`Locale` Constants](#constants)

---

**Version Note:** The `Locale.Builder` class and the `forLanguageTag`
method were added in the Java SE 7 release.

---

### `LocaleBuilder` Class

The
[`Locale.Builder`](http://download.oracle.com/javase/7/docs/api/java/util/Locale.Builder.html) utility class can be used to construct a `Locale` object that
conforms to the IETF BCP 47 syntax.
For example, to specify the French language and the country of Canada,
you could invoke the `Locale.Builder` constructor and then chain
the setter methods as follows:

```

Locale aLocale = new Locale.Builder().setLanguage("fr").setRegion("CA").build();

```

The next example creates `Locale`
objects for the English language in the United States and Great Britain:

```

Locale bLocale = new Locale.Builder().setLanguage("en").setRegion("US").build();
Locale cLocale = new Locale.Builder().setLanguage("en").setRegion("GB").build();

```

The final example creates a `Locale` object
for the Russian language:

```

Locale dLocale = new Locale.Builder().setLanguage("ru").setScript("Cyrl").build();

```

### `Locale` Constructors

There are three constructors available in the `Locale`
class for creating a `Locale` object:

* [`Locale(String language)`](http://download.oracle.com/javase/7/docs/api/java/util/Locale.html#Locale(java.lang.String))* [`Locale(String language, String country)`](http://download.oracle.com/javase/7/docs/api/java/util/Locale.html#Locale(java.lang.String, java.lang.String))* [`Locale(String language, String country, String variant)`](http://download.oracle.com/javase/7/docs/api/java/util/Locale.html#Locale(java.lang.String, java.lang.String, java.lang.String))

The following examples create `Locale` objects for the French
language in Canada, the English language in the U.S. and Great Britain, and
the Russian language.

```

aLocale = new Locale("fr", "CA");
bLocale = new Locale("en", "US");
cLocale = new Locale("en", "GB");
dLocale = new Locale("ru");

```

It is not possible to set a script code on a `Locale`
object in a release earlier than JDK 7.
### `forLanguageTag` Factory Method

If you have a language tag string that conforms to the IETF BCP 47
standard, you can use the
[`forLanguageTag(String)`](http://download.oracle.com/javase/7/docs/api/java/util/Locale.html#forLanguageTag(java.lang.String)) factory method, which was introduced in the Java SE 7 release. For example:

```

Locale aLocale = Locale.forLanguageTag("en-US");
Locale bLocale = Locale.forLanguageTag("ja-JP-u-ca-japanese");

```

### `Locale` Constants
For your convenience the `Locale` class provides
[constants](http://download.oracle.com/javase/7/docs/api/java/util/Locale.html#field_summary) for some languages and countries. For example:

```

cLocale = Locale.JAPAN;
dLocale = Locale.CANADA_FRENCH;

```

When you specify a language constant, the region portion of the
`Locale` is undefined. The next three statements create
equivalent `Locale` objects:

```

j1Locale = Locale.JAPANESE;
j2Locale = new Locale.Builder().setLanguage("ja").build();
j3Locale = new Locale("ja");

```

The `Locale` objects created
by the following three statements are also equivalent:

```

j4Locale = Locale.JAPAN;
j5Locale = new Locale.Builder().setLanguage("ja").setRegion("JP").build();
j6Locale = new Locale("ja", "JP");

```

### Codes

The following sections discuss the language code and the optional
script, region, and variant codes.

#### Language Code

The language code is either two or three lowercase letters that
conform to the ISO 639 standard.
You can find a full list of the ISO 639 codes at
<http://www.loc.gov/standards/iso639-2/php/code_list.php>.

The following table lists a few of the language codes.

> Sample Language Codes
>
> | Language Code | Description |
> | --- | --- |
> | `de` | German |
> | `en` | English |
> | `fr` | French |
> | `ru` | Russian |
> | `ja` | Japanese |
> | `jv` | Javanese |
> | `ko` | Korean |
> | `zh` | Chinese |

#### Script Code

The script code begins with an uppercase letter followed by three
lowercase letters and conforms to the ISO 15924 standard.
You can find a full list of the ISO 15924 codes at
<http://unicode.org/iso15924/iso15924-codes.html>.

The following table lists a few of the script codes.

> Sample Script Codes
>
> | Script Code | Description |
> | --- | --- |
> | `Arab` | Arabic |
> | `Cyrl` | Cyrillic |
> | `Kana` | Katakana |
> | `Latn` | Latin |

There are three methods for retrieving the script information for a
`Locale`.

* [`getScript()`](http://download.oracle.com/javase/7/docs/api/java/util/Locale.html#getScript()) – returns the 4-letter script code for a `Locale` object.
  If no script is defined for the locale, an empty string is returned.* [`getDisplayScript()`](http://download.oracle.com/javase/7/docs/api/java/util/Locale.html#getDisplayScript()) – returns a name for the locale's script that is appropriate
    for display to the user. If possible, the name will be localized for
    the default locale. So, for example, if the script code is "Latn," the
    diplay script name returned would be the string "Latin" for an English
    language locale.* [`getDisplayScript(Locale)`](http://download.oracle.com/javase/7/docs/api/java/util/Locale.html#getDisplayScript(java.util.Locale)) – returns the display name of the specified `Locale`
      localized, if possible, for the locale.

#### Region Code

The region (country) code consists of either two or three uppercase
letters that conform to the ISO 3166 standard,
or three numbers that conform to the UN M.49 standard.
A copy of the codes can be found at
<http://www.chemie.fu-berlin.de/diverse/doc/ISO_3166.html>.

The following table
contains several sample country and region codes.

> Sample Region Codes
>
> | A-2 Code | A-3 Code | Numeric Code | Description |
> | `AU` | `AUS` | `036` | Australia |
> | `BR` | `BRA` | `076` | Brazil |
> | `CA` | `CAN` | `124` | Canada |
> | `CN` | `CHN` | `156` | China |
> | `DE` | `DEU` | `276` | Germany |
> | `FR` | `FRA` | `250` | France |
> | `IN` | `IND` | `356` | India |
> | `RU` | `RUS` | `643` | Russian Federation |
> | `US` | `USA` | `840` | United States |

#### Variant Code

The optional `variant` code can be used to further distinguish your
`Locale`. For example, the variant code can be used to
indicate dialectical differences that are not covered by the region code.

---

**Version Note:** Prior to the Java SE 7 release, the variant code was sometimes used
to identify differences that were not specific to the language
or region.
For example, it might have been used to identify differences between
computing platforms, such as Windows or UNIX.
Under the IETF BCP 47 standard, this use is discouraged.

To define non-language-specific variations relevant to your environment,
use the extensions mechanism, as explained in
[BCP 47 Extensions](extensions.html).

---

As of the Java SE 7 release, which conforms to the IETF BCP 47 standard,
the variant code is used specifically to indicate additional variations
that define a language or its dialects. The IETF BCP 47 standard imposes
syntactic restrictions on the variant subtag. You can see a list of
variant codes (search for *variant*) at
<http://www.iana.org/assignments/language-subtag-registry>.

[« Previous](index.html)
•
[Trail](../TOC.html)
•
[Next »](extensions.html)

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

**Previous page:** Setting the Locale
  
**Next page:** BCP 47 Extensions




A browser with JavaScript enabled is required for this page to operate properly.