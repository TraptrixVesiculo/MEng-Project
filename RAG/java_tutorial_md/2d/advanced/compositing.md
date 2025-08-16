[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** 2D Graphics
  
**Lesson:** Advanced Topics in Java2D

[Advanced Topics in Java2D](index.html)

[Transforming Shapes, Text, and Images](transforming.html)

[Clipping the Drawing Region](clipping.html)

Compositing Graphics

[Controlling Rendering Quality](quality.html)

[Constructing Complex Shapes from Geometry Primitives](complexshapes.html)

[Supporting User Interaction](user.html)

[Home Page](../../index.html)
>
[2D Graphics](../index.html)
>
[Advanced Topics in Java2D](index.html)

[« Previous](clipping.html) • [Trail](../TOC.html) • [Next »](quality.html)

# Compositing Graphics

The
[`AlphaComposite`](http://download.oracle.com/javase/7/docs/api/java/awt/AlphaComposite.html) class encapsulates various compositing
styles, which determine how overlapping objects are rendered. An
`AlphaComposite` can also have an alpha value that specifies
the degree of transparency: alpha = 1.0 is totally opaque,
alpha = 0.0 totally transparent (clear).
`AlphaComposite` supports most of the standard Porter-Duff
compositing rules shown in the following table.

| Compositing Rule | Description |
| --- | --- |
| Source-over (`SRC_OVER`)  Source-over compositing | If pixels in the object being rendered (the source) have the same location as previously rendered pixels (the destination), the source pixels are rendered over the destination pixels. |
| Source-in (`SRC_IN`)  Source-in compositing | If pixels in the source and the destination overlap, only the source pixels in the overlapping area are rendered. |
| Source-out (`SRC_OUT`)  Source-out compositing | If pixels in the source and the destination overlap, only the source pixels outside of the overlapping area are rendered. The pixels in the overlapping area are cleared. |
| Destination-over (`DST_OVER`)  Destination-over compositing | If pixels in the source and the destination overlap, only the source pixels outside of the overlapping area are rendered. The pixels in the overlapping area are not changed. |
| Destination-in (`DST_IN`)  Destination-in compositing | If pixels in the source and the destination overlap, the alpha from the source is applied to the destination pixels in the overlapping area. If the alpha = 1.0, the pixels in the overlapping area are unchanged; if the alpha is 0.0, pixels in the overlapping area are cleared. |
| Destination-out (`DST_OUT`)  Destination-out compositing | If pixels in the source and the destination overlap, the alpha from the source is applied to the destination pixels in the overlapping area. If the alpha = 1.0, the pixels in the overlapping area are cleared; if the alpha is 0.0, the pixels in the overlapping area are unchanged. |
| Clear (`CLEAR`)  Clear with overlap compositing | If the pixels in the source and the destination overlap, the pixels in the overlapping area are cleared. |

To change the compositing style used by the
[`Graphics2D`](http://download.oracle.com/javase/7/docs/api/java/awt/Graphics2D.html) class, create an `AlphaComposite` object and pass it into the
`setComposite` method.

## Example: Composite

This program illustrates the effects of various compositing style and
alpha combinations.

---

**Note:** If you don't see the applet running, you need to install [release 6 of the Java SE Development Kit (JDK)](http://java.sun.com/javase/downloads/index.jsp).

---

[`Composite.java`](examples/Composite.java).
contains the full code for this applet.

A new `AlphaComposite` object *ac*
is constructed by calling `AlphaComposite.getInstance`
and specifying the desired compositing rule.

```

AlphaComposite ac =
               AlphaComposite.getInstance(AlphaComposite.SRC);

```

When a different compositing rule or alpha value is selected,
`AlphaComposite.getInstance` is called again, and the new
`AlphaComposite` is assigned to *ac*. The selected alpha is applied in addition to
the per-pixel alpha value and is passed as a second parameter to
`AlphaComposite`.`getInstance`.

```

ac = AlphaComposite.getInstance(getRule(rule), alpha);

```

The composite attribute is modified by passing the
`AlphaComposite` object to `Graphics 2D`
`setComposite`. The objects are rendered into a
`BufferedImage` and are later copied to the screen, so the
composite attribute is set on the `Graphics2D` context for
the `BufferedImage`:

```

BufferedImage buffImg = new BufferedImage(w, h,
                            BufferedImage.TYPE_INT_ARGB);
Graphics2D gbi = buffImg.createGraphics();
...
gbi.setComposite(ac);

```

[« Previous](clipping.html)
•
[Trail](../TOC.html)
•
[Next »](quality.html)

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

**Previous page:** Clipping the Drawing Region
  
**Next page:** Controlling Rendering Quality




A browser with JavaScript enabled is required for this page to operate properly.