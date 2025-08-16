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

[Compositing Graphics](compositing.html)

Controlling Rendering Quality

[Constructing Complex Shapes from Geometry Primitives](complexshapes.html)

[Supporting User Interaction](user.html)

[Home Page](../../index.html)
>
[2D Graphics](../index.html)
>
[Advanced Topics in Java2D](index.html)

[« Previous](compositing.html) • [Trail](../TOC.html) • [Next »](complexshapes.html)

# Controlling Rendering Quality

Use the
[`Graphics2D`](http://download.oracle.com/javase/7/docs/api/java/awt/Graphics2D.html) class rendering hints attribute to
specify whether you want objects to be rendered as quickly as possible
or whether you prefer that the rendering quality be as high as
possible.

To set or change the rendering hints attribute in the `Graphics2D`
context, construct a
[`RenderingHints`](http://download.oracle.com/javase/7/docs/api/java/awt/RenderingHints.html) object and
pass it into `Graphics2D` by using the `setRenderingHints` method.
If you just want to set one hint, you can call `Graphics2D`
`setRenderingHint` and specify the key-value pair for the
hint you want to set. (The key-value pairs are defined in the
`RenderingHints` class.)

For example, to set a preference for antialiasing to be used if
possible, you could use `setRenderingHint`:

```


   public void paint (graphics g){
   	Graphics2D g2 = (Graphics2D)g;
	RenderingHints rh = new RenderingHints(
		RenderingHints.KEY_TEXT_ANTIALIASING,
		RenderingHints.VALUE_TEXT_ANTIALIAS_ON);
	g2.setRenderingHints(rh);
   ...
   }
	

```

---

**Note:** 
Not all platforms support modification of the rendering mode, so
specifying rendering hints does not guarantee that they will be
used.

---

`RenderingHints` supports the following types of hints:

| Hint | Key | Values |
| --- | --- | --- |
| **Antialiasing** | `KEY_ANTIALIASING` | `VALUE_ANTIALIAS_ON`  `VALUE_ANTIALIAS_OFF`   `VALUE_ANTIALIAS_DEFAULT` |
| **Alpha Interpolation** | `KEY_ALPHA_INTERPOLATION` | `VALUE_ALPHA_INTERPOLATION_QUALITY`  `VALUE_ALPHA_INTERPOLATION_SPEED`  `VALUE_ALPHA_INTERPOLATION_DEFAULT` |
| **Color Rendering** | `KEY_COLOR_RENDERING` | `VALUE_COLOR_RENDER_QUALITY`  `VALUE_COLOR_RENDER_SPEED`  `VALUE_COLOR_RENDER_DEFAULT` |
| **Dithering** | `KEY_DITHERING` | `VALUE_DITHER_DISABLE`  `VALUE_DITHER_ENABLE`   `VALUE_DITHER_DEFAULT` |
| **Fractional Text Metrics** | `KEY_FRACTIONALMETRICS` | `VALUE_FRACTIONALMETRICS_ON`  `VALUE_FRACTIONALMETRICS_OFF`  `VALUE_FRACTIONALMETRICS_DEFAULT` |
| **Image Interpolation** | `KEY_INTERPOLATION` | `VALUE_INTERPOLATION_BICUBIC`  `VALUE_INTERPOLATION_BILINEAR`  `VALUE_INTERPOLATION_NEAREST_NEIGHBOR` |
| **Rendering** | `KEY_RENDERING` | `VALUE_RENDER_QUALITY`  `VALUE_RENDER_SPEED`  `VALUE_RENDER_DEFAULT` |
| **Stroke Normalization Control** | `KEY_STROKE_CONTROL` | `VALUE_STROKE_NORMALIZE`  `VALUE_STROKE_DEFAULT`  `VALUE_STROKE_PURE` |
| **Text Antialiasing** | `KEY_TEXT_ANTIALIASING` | `VALUE_TEXT_ANTIALIAS_ON`  `VALUE_TEXT_ANTIALIAS_OFF`  `VALUE_TEXT_ANTIALIAS_DEFAULT`  `VALUE_TEXT_ANTIALIAS_GASP`  `VALUE_TEXT_ANTIALIAS_LCD_HRGB`  `VALUE_TEXT_ANTIALIAS_LCD_HBGR`  `VALUE_TEXT_ANTIALIAS_LCD_VRGB`  `VALUE_TEXT_ANTIALIAS_LCD_VBGR` |
| **LCD Text Contrast** | `KEY_TEXT_LCD_CONTRAST` | Values should be a positive integer in the range 100 to 250. A lower value (eg 100) corresponds to higher contrast text when displaying dark text on a light background. A higher value (eg 200) corresponds to lower contrast text when displaying dark text on a light background. A typical useful value is in the narrow range 140-180. If no value is specified, a system or implementation default value will be applied. |

When a hint is set to default, the platform rendering default is used.

[« Previous](compositing.html)
•
[Trail](../TOC.html)
•
[Next »](complexshapes.html)

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

**Previous page:** Compositing Graphics
  
**Next page:** Constructing Complex Shapes from Geometry Primitives




A browser with JavaScript enabled is required for this page to operate properly.