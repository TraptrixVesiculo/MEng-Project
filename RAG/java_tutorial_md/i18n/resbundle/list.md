[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Internationalization
  
**Lesson:** Isolating Locale-Specific Data

[Isolating Locale-Specific Data](index.html)

[About the ResourceBundle Class](concept.html)

[Preparing to Use a ResourceBundle](prepare.html)

[Backing a ResourceBundle with Properties Files](propfile.html)

Using a ListResourceBundle

[Customizing Resource Bundle Loading](control.html)

[Home Page](../../index.html)
>
[Internationalization](../index.html)
>
[Isolating Locale-Specific Data](index.html)

[« Previous](propfile.html) • [Trail](../TOC.html) • [Next »](control.html)

# Using a ListResourceBundle

This section illustrates the use of a `ListResourceBundle`
object with a sample program called
[`ListDemo`](examples/ListDemo.java).
The text
that follows explains each step involved in creating the
`ListDemo` program, along with the
`ListResourceBundle` subclasses that support it.

### 1. Create the ListResourceBundle Subclasses

> A `ListResourceBundle` is backed up by a class file.
> Therefore the first step is to create a class file for every supported
> `Locale`. In the `ListDemo` program the base name
> of the `ListResourceBundle`  is `StatsBundle`.
> Since `ListDemo` supports three `Locale` objects,
> it requires the following three class files:
>
> ```
>
> StatsBundle_en_CA.class
> StatsBundle_fr_FR.class
> StatsBundle_ja_JP.class
>
> ```
>
> The `StatsBundle` class for Japan is defined in the source
> code that follows. Note that the class name is constructed by appending
> the language and country codes to the base name of the
> `ListResourceBundle`. Inside the class the two-dimensional
> `contents` array is initialized with the key-value pairs.
> The keys are the first element in each pair: `GDP`,
> `Population`, and `Literacy`. The keys must be
> `String` objects and they must be the same in every class in
> the `StatsBundle` set. The values can be any type of object.
> In this example the values are two `Integer` objects and a
> `Double` object.
>
> ```
>
> import java.util.*;
> public class StatsBundle_ja_JP extends ListResourceBundle {
>     public Object[][] getContents() {
> 	return contents;
>     }
>     private Object[][] contents = {
> 	{ "GDP", new Integer(21300) },
> 	{ "Population", new Integer(125449703) },
> 	{ "Literacy", new Double(0.99) },
>     };
> }
>
> ```

### 2. Specify the Locale

> The `ListDemo` program defines the `Locale`
> objects as follows:
>
> ```
>
> Locale[] supportedLocales = {
>     new Locale("en", "CA"),
>     new Locale("ja", "JP"),
>     new Locale("fr", "FR")
> };
>
> ```
>
> Each `Locale` object corresponds to one of the
> `StatsBundle`  classes. For example, the Japanese
> `Locale`, which was defined with the `ja` and
> `JP` codes, matches `StatsBundle_ja_JP.class`.

### 3. Create the ResourceBundle

> To create the `ListResourceBundle`, invoke the
> `getBundle`  method. The following line of code specifies
> the base name of the class (`StatsBundle`) and the
> `Locale`:
>
> ```
>
> ResourceBundle stats =
> 		ResourceBundle.getBundle("StatsBundle", currentLocale);
>
> ```
>
> The `getBundle` method searches for a class whose name
> begins with `StatsBundle` and is followed by the language
> and country codes of the specified `Locale`. If the
> `currentLocale` is created with the  `ja` and
> `JP` codes, `getBundle` returns a
> `ListResourceBundle` corresponding to the class
> `StatsBundle_ja_JP`, for example.

### 4. Fetch the Localized Objects

> Now that the program has a `ListResourceBundle` for the
> appropriate `Locale`, it can fetch the localized objects by
> their keys. The following line of code retrieves the literacy rate by
> invoking `getObject` with the `Literacy` key
> parameter. Since `getObject` returns an object, cast it to a
> `Double`:
>
> ```
>
> Double lit = (Double)stats.getObject("Literacy");
>
> ```

### 5. Run the Demo Program

> `ListDemo` program prints the data it fetched with the
> `getBundle`  method:
>
> ```
>
> Locale = en_CA
> GDP = 24400
> Population = 28802671
> Literacy = 0.97
>
> Locale = ja_JP
> GDP = 21300
> Population = 125449703
> Literacy = 0.99
>
> Locale = fr_FR
> GDP = 20200
> Population = 58317450
> Literacy = 0.99
>
> ```

[« Previous](propfile.html)
•
[Trail](../TOC.html)
•
[Next »](control.html)

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

**Previous page:** Backing a ResourceBundle with Properties Files
  
**Next page:** Customizing Resource Bundle Loading




A browser with JavaScript enabled is required for this page to operate properly.