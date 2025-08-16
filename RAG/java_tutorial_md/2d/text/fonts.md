[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** 2D Graphics
  
**Lesson:** Working with Text APIs

[Working with Text APIs](index.html)

Selecting a Font

[Measuring Text](measuringtext.html)

[Advanced Text Display](advanced.html)

[Displaying Antialiased Text by Using Rendering Hints](renderinghints.html)

[Using Text Attributes to Style Text](textattributes.html)

[Drawing Multiple Lines of Text](drawmulstring.html)

[Home Page](../../index.html)
>
[2D Graphics](../index.html)
>
[Working with Text APIs](index.html)

[« Previous](index.html) • [Trail](../TOC.html) • [Next »](measuringtext.html)

# Selecting a Font

Java 2D™ defines the following five logical font families:

* `Dialog`
* `DialogInput`
* `Monospaced`
* `Serif`
* `SansSerif`

These fonts are available on any Java platform and can be
thought of as aliases for some underlying font that has the
properties implied by its name. A Serif font is a font similar to
Times New Roman, which is commonly used in print. A Sans Serif font is
more typical for onscreen use.

These fonts can be customized for the locale of
the user. In addition these fonts support the widest range of code points (unicode characters).

Apart from the family, fonts have other attributes, the
most important of which are *style* and
*size*. Styles are **Bold** and
*Italic*.

The default Java 2D font is 12 pt Dialog. This font is a typical point size for
reading text on a normal 72–120 DPI display device.
An application can create an instance of this font directly by specifying the following:

```

Font font = new Font("Dialog", Font.PLAIN, 12);

```

In addition to the logical fonts, Java software provides access to other
fonts that are installed on your system. The names of all available font families
can be found by calling the following:

```

GraphicsEnvironment ge = GraphicsEnvironment.getLocalGraphicsEnvironment();
String []fontFamilies = ge.getAvailableFontFamilyNames();

```

The FontSelector sample program (available in
[`FontSelector.java`](examples/FontSelector.java))
illustrates how to locate and select these
fonts. You can use this example to view how Sans Serif appears on your system.
These other fonts are called *physical* fonts.

---

**Note:** Applications should not assume that any particular physical font is
present. However, the logical fonts are a safe choice because they are always present.

---

---

**Note:** If you don't see the applet running, you need to install [release 6 of the Java SE Development Kit (JDK)](http://java.sun.com/javase/downloads/index.jsp).

---

Sometimes, an application cannot depend on a font being installed on the system,
usually because the font is a custom font that is not otherwise available.
In this case, the application must include the font.
This lesson shows how to obtain a `TrueType` font, the most commonly
used font type on modern operating systems, to a `java.awt.Font` object.

You can use either of these methods:

```

Font java.awt.Font.createFont(int fontFormat, InputStream in);
Font java.awt.Font.createFont(int fontFormat, File fontFile);

```

To identify a TrueType font, `fontFormat` must be the constant `Font.TRUETYPE_FONT`.

```

Font font = Font.createFont(Font.TRUETYPE_FONT, new File("A.ttf"));

```

Accessing the font directly from a file must be more convenient for some cases.
However, an `InputStream` might be needed if your code is unable to access file
system resources, or if the font is packaged in a Java Archive (JAR) file along with
the rest of the application or applet.

The returned `Font` instance can then be used with the `Font.deriveFont(..)`
methods to derive a version that is the required size. For example:

```

try {
     /* Returned font is of pt size 1 */
     Font font = Font.createFont(Font.TRUETYPE_FONT, new File("A.ttf"));

     /* derive and return a 12 pt version : need to use float otherwise
      * it would be interpreted as style
      */
     return font.deriveFont(12f);

} catch (IOException ioe);
} catch (FontFormatException ffe);
}

```

It is important to use `deriveFont()` because fonts which are created by application
are not part of the set of fonts known to the underlying font system.
Because `deriveFont` works from the original created font it does not have
this limitation.

The solution for this problem is to register the created font with the graphics
environment. For example:

```

try {
     GraphicsEnvironment ge = GraphicsEnvironment.getLocalGraphicsEnvironment();
     ge.registerFont(Font.createFont(Font.TRUETYPE_FONT, new File("A.ttf"));
} catch (IOException ioe);
} catch (FontFormatException ffe);
}

```

After this step is done, the font is available in calls to `getAvailableFontFamilyNames()`
and can be used in font constructors.

[« Previous](index.html)
•
[Trail](../TOC.html)
•
[Next »](measuringtext.html)

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

**Previous page:** Working with Text APIs
  
**Next page:** Measuring Text




A browser with JavaScript enabled is required for this page to operate properly.