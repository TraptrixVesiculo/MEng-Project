[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** 2D Graphics
  
**Lesson:** Working with Text APIs
  
**Section:** Advanced Text Display

[Working with Text APIs](index.html)

[Selecting a Font](fonts.html)

[Measuring Text](measuringtext.html)

[Advanced Text Display](advanced.html)

Displaying Antialiased Text by Using Rendering Hints

[Using Text Attributes to Style Text](textattributes.html)

[Drawing Multiple Lines of Text](drawmulstring.html)

[Home Page](../../index.html)
>
[2D Graphics](../index.html)
>
[Working with Text APIs](index.html)

[« Previous](advanced.html) • [Trail](../TOC.html) • [Next »](textattributes.html)

# Displaying Antialiased Text by Using Rendering Hints

Java 2D™ text rendering can be affected by *rendering hints*.

Recall that the most important text drawing method is the following:

```
 
Graphics.drawString(String s, int x, int y);

```

Usually, this method draws each glyph in a string of text with a solid color
and each pixel that is “on” in that glyph is set to that colour. This type of drawing
produces the highest contrast text, but sometimes with jagged
(aliased) edges.

*Text antialiasing* is a technique used to smooth the edges of text on a screen.
The Java 2D API enables applications to specify whether this technique should be used and what
algorithm to use by applying a text rendering hint to the `Graphics`.

The most common rendering hint blends the foreground (text) color with the onscreen
background pixels at the edges of the text. To request this hint an application
must invoke the following:

```

graphics2D.setRenderingHint(RenderingHints.KEY_TEXT_ANTIALIASING,
                            RenderingHints.VALUE_TEXT_ANTIALIAS_ON);

```

The following figure illustrates the antialiasing capability.

![This figure represents an antialiasing hint for the Hello World string.](../../figures/2d/textaa.gif)

If used inappropriately this method can make the text appear overly fuzzy.
In such cases, a better hint to use is the following:

```

graphics2D.setRenderingHint(RenderingHints.KEY_TEXT_ANTIALIASING,
                            RenderingHints.VALUE_TEXT_ANTIALIAS_GASP);

```

This method automatically uses information in the font itself to decide
whether to use antialiasing or to use solid colors.

LCD displays have a property that the Java 2D API can use to produce text that
isn't as fuzzy as typical antialiasing but is more legible
at small sizes.
To request that text be drawn using the sub-pixel LCD text mode
for a typical LCD display, an application must invoke the following:

```

graphics2D.setRenderingHint(RenderingHints.KEY_TEXT_ANTIALIASING,
                            RenderingHints.VALUE_TEXT_ANTIALIAS_LCD_HRGB);

```

The code example represented below illustrates the antialiasing capability in the following order:

1. Antialiasing is off.
2. Antialiasing is on.
3. Antialiasing using the `TEXT_ANTIALIAS_GASP` hint.

   ---

   **Note:** Consequently the GASP table specifies to use only hinting at
   those sizes and not "smoothing". So in many cases the resulting text display
   is equivalent to `VALUE_TEXT_ANTIALIAS_OFF`.

   ---
4. Antialiasing using the `TEXT_ANTIALIAS_LCD_HRGB` hint.

---

**Note:** If you don't see the applet running, you need to install [release 6 of the Java SE Development Kit (JDK)](http://java.sun.com/javase/downloads/index.jsp).

---

The complete code for this applet is in
[`AntialiasedText.java`](examples/AntialiasedText.java).

[« Previous](advanced.html)
•
[Trail](../TOC.html)
•
[Next »](textattributes.html)

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

**Previous page:** Advanced Text Display
  
**Next page:** Using Text Attributes to Style Text




A browser with JavaScript enabled is required for this page to operate properly.