[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** 2D Graphics
  
**Lesson:** Advanced Topics in Java2D

[Advanced Topics in Java2D](index.html)

[Transforming Shapes, Text, and Images](transforming.html)

Clipping the Drawing Region

[Compositing Graphics](compositing.html)

[Controlling Rendering Quality](quality.html)

[Constructing Complex Shapes from Geometry Primitives](complexshapes.html)

[Supporting User Interaction](user.html)

[Home Page](../../index.html)
>
[2D Graphics](../index.html)
>
[Advanced Topics in Java2D](index.html)

[« Previous](transforming.html) • [Trail](../TOC.html) • [Next »](compositing.html)

# Clipping the Drawing Region

Any
[`Shape`](http://download.oracle.com/javase/7/docs/api/java/awt/Shape.html) object can be used as a clipping path that restricts
the portion of the drawing area that will be rendered. The clipping path
is part of the
[`Graphics2D`](http://download.oracle.com/javase/7/docs/api/java/awt/Graphics2D.html) context; to set the clip
attribute, you call `Graphics2D.setClip` and pass in the
`Shape` that defines the clipping path you want to use. You
can shrink the clipping path by calling the `clip` method
and passing in another `Shape`; the clip is set to the
intersection of the current clip and the specified `Shape`.

## Example: ClipImage

This example animates a clipping path to reveal different portions of an image.

---

**Note:** If you don't see the applet running, you need to install [release 6 of the Java SE Development Kit (JDK)](http://java.sun.com/javase/downloads/index.jsp).

---

[`ClipImage.java`](examples/ClipImage.java)
contains the complete code for this applet.
The applet requires the
[`clouds.jpg`](examples/images/clouds.jpg)
image file.

The clipping path is defined by the intersection of an ellipse and a
rectangle whose dimensions are set randomly. The ellipse is passed to
the `setClip` method, and then `clip`
is called to set the clipping path to the intersection of the ellipse
and the rectangle.

```

private Ellipse2D ellipse = new Ellipse2D.Float();
private Rectangle2D rect = new Rectangle2D.Float();
...
ellipse.setFrame(x, y, ew, eh);
g2.setClip(ellipse);
rect.setRect(x+5, y+5, ew-10, eh-10);
g2.clip(rect);

```

## Example: Starry

A clipping area can also be created from a text string. The
following example creates a `TextLayout` with the string *The
Starry Night*. Then, it gets the outline of the
`TextLayout`. The
[`TextLayout.getOutline`](http://download.oracle.com/javase/7/docs/api/java/awt/font/TextLayout.html#getOutline(java.awt.geom.AffineTransform)) method
returns a `Shape` object and a `Rectangle` is
created from the bounds of this `Shape` object. The bounds
contain all the pixels the layout can draw. The color in the graphics
context is set to blue and the outline shape is drawn, as illustrated by
the following image and code snippet.

![The Starry Night text (outline)](../../figures/2d/starryOutline.gif)

```

FontRenderContext frc = g2.getFontRenderContext();
Font f = new Font("Helvetica", 1, w/10);
String s = new String("The Starry Night");
TextLayout textTl = new TextLayout(s, f, frc);
AffineTransform transform = new AffineTransform();
Shape outline = textTl.getOutline(null);
Rectangle r = outline.getBounds();
transform = g2.getTransform();
transform.translate(w/2-(r.width/2), h/2+(r.height/2));
g2.transform(transform);
g2.setColor(Color.blue);
g2.draw(outline);   

```

Next, a clipping area is set on the graphics context using the
`Shape` object created from `getOutline`. The
`starry.gif` image,
which is Van Gogh's famous painting, *The Starry
Night*, is drawn into this clipping area starting at the lower left
corner of the `Rectangle` object.

```

g2.setClip(outline);
g2.drawImage(img, r.x, r.y, r.width, r.height, this);

```



---

**Note:** If you don't see the applet running, you need to install [release 6 of the Java SE Development Kit (JDK)](http://java.sun.com/javase/downloads/index.jsp).

---

[`Starry.java`](examples/Starry.java)
contains the complete code for this program.
This applet requires the
[`Starry.gif`](examples/images/Starry.gif)
image file.

[« Previous](transforming.html)
•
[Trail](../TOC.html)
•
[Next »](compositing.html)

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

**Previous page:** Transforming Shapes, Text, and Images
  
**Next page:** Compositing Graphics




A browser with JavaScript enabled is required for this page to operate properly.