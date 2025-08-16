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

[Using a ListResourceBundle](list.html)

Customizing Resource Bundle Loading

[Home Page](../../index.html)
>
[Internationalization](../index.html)
>
[Isolating Locale-Specific Data](index.html)

[« Previous](list.html) • [Trail](../TOC.html) • [Next »](../format/index.html)

# Customizing Resource Bundle Loading

Earlier in this lesson you have learned how to create and access objects of the
`ResourceBundle` class. This section extents your knowledge and explains
how to take an advantage from the
[`ResourceBundle.Control`](http://download.oracle.com/javase/7/docs/api/java/util/ResourceBundle.Control.html)class capabilities.

The `ResourceBundle.Control` was created to specify how to locate and instantiate resource bundles.
It defines a set of callback methods that are invoked by the
[`ResourceBundle.getBundle`](http://download.oracle.com/javase/7/docs/api/java/util/ResourceBundle.html#getBundle(java.lang.String,%20java.util.Locale,%20java.util.ResourceBundle.Control))factory methods during the bundle loading process.

Unlike a
[`ResourceBundle.getBundle`](http://download.oracle.com/javase/7/docs/api/java/util/ResourceBundle.html#getBundle(java.lang.String,%20java.util.Locale))method described earlier, this `ResourceBundle.getBundle` method defines a resource bundle using the specified base name, the
default locale and the specified control.

```
public static final ResourceBundle getBundle(String baseName, 
                           ResourceBundle.Control cont
                           ...

```

The specified control provide information for the resource bundle loading process.

The following sample program called
[`RBControl.java`](examples/RBControl.java)illustrates how to define your own search paths for Chinese locales.

### 1. Create the `properties` Files.

As it was described before you can load your resources either from classes or
from `properties` files. These files contain descriptions for the
following locales:

* `RBControl.properties` – Global
* `RBControl_zh.properties` – Language only: Simplified Chinese
* `RBControl_zh_cn.properties` – Region only: China
* `RBControl_zh_hk.properties` – Region only: Hong Kong
* `RBControl_zh_tw.properties` – Taiwan

In this example an application creates a new locale for the Hong Kong region.

### 2. Create a `ResourceBundle` instance.

As in the example in the previous section, this application creates a
`ResourceBundle` instance by invoking the `getBundle`
method:

```

   private static void test(Locale locale) {
       ResourceBundle rb = ResourceBundle.getBundle("RBControl", locale,
	        new ResourceBundle.Control() {
		...

```

The `getBundle` method searches for `properties` files
with the RBControl prefix. However, this method contains a `Control`
parameter, which drives the process of searching the Chineese locales.

### 3. Invoke the `getCandidateLocales` method

The `getCandidateLocales` method returns a list of the `Locales`
objects as candidate locales for the base name and locale.

```

  new ResourceBundle.Control() {
		 @Override
		 public List<Locale> getCandidateLocales(String baseName, 
		                                         Locale locale) {
		 ...					    

```

The default implementation returns a list of the `Locale` objects
as follows: Locale(language, country).

However, this method is overriden to implement the following
specific behavior:

```

                     {
                     if (baseName == null)
			 throw new NullPointerException();
		     if (locale.equals(new Locale("zh", "HK"))) {
			 return Arrays.asList(
			     locale,
			     Locale.TAIWAN,
			     // no Locale.CHINESE here
			     Locale.ROOT);
		     } else if (locale.equals(Locale.TAIWAN)) {
			 return Arrays.asList(
			     locale,
			     // no Locale.CHINESE here
			     Locale.ROOT);
		     }

```

Note, that the last element of the sequence of candidate locales must be a root
locale.

### 4. Call the `test` class

Call the `test` class for the following four different locales:

```

   public static void main(String[] args) {
	test(Locale.CHINA);
	test(new Locale("zh", "HK"));
	test(Locale.TAIWAN);
	test(Locale.CANADA);
    }

```

### 5. Run the Sample Program

You will see the program output as follows:

```

locale: zh_CN
	region: China
	language: Simplified Chinese
locale: zh_HK
	region: Hong Kong
	language: Traditional Chinese
locale: zh_TW
	region: Taiwan
	language: Traditional Chinese
locale: en_CA
	region: global
	language: English

```

Note that the newly created was assigned the Hong Kong region, because it was
specified in an appropriate `properties` file. Traditional Chinese was assigned
as the language for the Taiwan locale.

Two other interesting methods of the `ResourceBundle.Control` class were not
used in the `RBControl` example, but they deserved to be mentioned.
The `getTimeToLive` method is used to determine how long the
resource bundle can exist in the cache. If the time limit for a
resource bundle in the cache has expired, the `needsReload` method is
invoked to determine whether the resource bundle needs to be reloaded.

[« Previous](list.html)
•
[Trail](../TOC.html)
•
[Next »](../format/index.html)

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

**Previous page:** Using a ListResourceBundle
  
**Next page:** Formatting




A browser with JavaScript enabled is required for this page to operate properly.