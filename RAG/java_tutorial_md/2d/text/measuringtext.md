[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** 2D Graphics
  
**Lesson:** Working with Text APIs

[Working with Text APIs](index.html)

[Selecting a Font](fonts.html)

Measuring Text

[Advanced Text Display](advanced.html)

[Displaying Antialiased Text by Using Rendering Hints](renderinghints.html)

[Using Text Attributes to Style Text](textattributes.html)

[Drawing Multiple Lines of Text](drawmulstring.html)

[Home Page](../../index.html)
>
[2D Graphics](../index.html)
>
[Working with Text APIs](index.html)

[« Previous](fonts.html) • [Trail](../TOC.html) • [Next »](advanced.html)

# Measuring Text

To properly measure text, you need to learn a few methods and some mistakes
to avoid. Font metrics are measurements of text rendered by a
[`Font`](http://download.oracle.com/javase/7/docs/api/java/awt/Font.html) object such as the height of a line of text in the font.
The most common way to measure text is to use a
[`FontMetrics`](http://download.oracle.com/javase/7/docs/api/java/awt/FontMetrics.html) instance which encapsulates this metrics information. For example:

```

    // get metrics from the graphics
    FontMetrics metrics = graphics.getFontMetrics(font);
    // get the height of a line of text in this font and render context
    int hgt = metrics.getHeight();
    // get the advance of my text in this font and render context
    int adv = metrics.stringWidth(text);
    // calculate the size of a box to hold the text with some padding.
    Dimension size = new Dimension(adv+2, hgt+2);

```

This way is sufficient for many applications to evenly space
lines of text or to size Swing components.

Note the following:

* The metrics are obtained from the
  [`Graphics`](http://download.oracle.com/javase/7/docs/api/java/awt/Graphics.html) class, because this class encapsulates
  the `FontRenderContext`, which is needed to
  accurately measure text.
  At screen resolutions, fonts are adjusted for ease of reading.
  As text size increases, this adjustment does not scale linearly.
  So, at 20 pt, a font will not display text exactly
  twice the length as it would at 10 pt.
  Besides the text itself and the font, the other important piece of
  information needed to measure text is the `FontRenderContext`.
  This method includes the transform from user space to
  device pixels that is used in measuring text.
* The height is reported without reference to any particular string of
  text. It is useful, for example in, a text
  editor where you want the same line spacing between each line of text.
* `stringWidth()` returns the advance width of the text.
  *Advance width* is the distance from the origin of the text to the position of
  a subsequently rendered string.

When using these methods to measure text, note
that the text can extend in any direction outside of a rectangle, defined by the
font height and the advance of the string.

![This figure shows hot to measure text by using font metrics](../../figures/2d/font-metrics.GIF)

Typically, the simplest solution is to ensure that the text is not clipped,
for example, by components that surround the text.
Add padding in cases where the text might otherwise be clipped.

If this solution is insufficient, other text measurement APIs in
the Java 2D™ software can return rectangular bounding boxes. These boxes account for the height
of the specific text to be measured and for pixelization effects.

[« Previous](fonts.html)
•
[Trail](../TOC.html)
•
[Next »](advanced.html)

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

**Previous page:** Selecting a Font
  
**Next page:** Advanced Text Display




A browser with JavaScript enabled is required for this page to operate properly.