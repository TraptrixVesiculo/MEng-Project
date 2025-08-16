[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** 2D Graphics
  
**Lesson:** Overview of the Java 2D API Concepts

[Overview of the Java 2D API Concepts](index.html)

[Coordinates](coordinate.html)

Java 2D Rendering

[Geometric Primitives](primitives.html)

[Text](text.html)

[Images](images.html)

[Printing](printing.html)

[Home Page](../../index.html)
>
[2D Graphics](../index.html)
>
[Overview of the Java 2D API Concepts](index.html)

[« Previous](coordinate.html) • [Trail](../TOC.html) • [Next »](primitives.html)

# Java 2D Rendering

The Java 2D™ API provides a uniform rendering model across different types of devices.
At the application level, the rendering process is the same whether the target
rendering device is a screen or a printer. When a component needs to be displayed, its `paint` or
`update` method is automatically invoked with the appropriate
`Graphics` context.

The Java 2D API includes the
[`java.awt.Graphics2D`](http://download.oracle.com/javase/7/docs/api/java/awt/Graphics2D.html) class, which extends the
[`Graphics`](http://download.oracle.com/javase/7/docs/api/java/awt/Graphics.html) class to provide access to the enhanced graphics and rendering
features of the Java 2D API. These features include:

* Rendering the outline of any geometric primitive,
  using the stroke and paint attributes (`draw` method).* Rendering any geometric primitive by filling its
    interior with the color or pattern specified by the paint attributes
    (`fill` method).* Rendering any text string (the `drawString` method). The font
      attribute is used to convert the string to glyphs, which are then
      filled with the color or pattern specified by the paint attributes.* Rendering the specified image (the `drawImage` method).

In addition, the `Graphics2D` class supports the `Graphics`
rendering methods for particular shapes, such as `drawOval`
and `fillRect`. All methods that are represented above can be divided into two groups:

1. Methods to draw a shape
2. Methods that affect rendering

The second group of the methods uses the state attributes that form the `Graphics2D`
context for following purposes:

* To vary the stroke width
* To change how strokes are joined together
* To set a clipping path to limit the area that is rendered
* To translate, rotate, scale, or shear objects when they are rendered
* To define colors and patterns to fill shapes with
* To specify how to compose multiple graphics objects

To employ Java 2D API features in the application, cast the `Graphics` object
passed into a component’s rendering method to a `Graphics2D` object. For example:

```

public void paint (Graphics g) {
    Graphics2D g2 = (Graphics2D) g;
    ...
}

```

As the following figure shows, the `Graphics2D` class rendering context contains several attributes.

|  |  |
| --- | --- |
| This figure represents a stroke to outline the shape | The *pen attribute* is applied to the outline of a shape. This stroke attribute enables you to draw lines with any point size and dashing pattern and apply end-cap and join decorations to a line. |
| This figure shows how to fill a shape with solid color | The *fill attribute* is applied to a shape's interior. This paint attribute enables you to fill shapes with solid colors, gradients, and patterns. |
| This figure shows how to composite an existing image and a graphic primitives | The *compositing attribute* is used when rendered objects overlap existing objects. |
| This figure represents shearing transform | The *transform* attribute is applied during rendering to convert the rendered object from user space to device-space coordinates. Optional translation, rotation, scaling, or shearing transforms can also be applied through this attribute. |
| This figure represents how to define the clipping path by using the Shape object | The *clip*, type restricts rendering to the area within the outline of the `Shape` object used to define the clipping path. Any `Shape` object that is used to define the clip. |
| This figure demonstrates a sample of glyphs | The *font* attribute is used to convert text strings to glyphs. |
| This figure represents antialiasing | *Rendering hints* specify preferences in the trade-offs between speed and quality. For example, you can specify whether antialiasing should be used, if this feature available. See also [Controlling Rendering Quality](../advanced/quality.html). |

To learn more about transforming and compositing see the
[Advanced Topics in Java2D](../advanced/index.html) lesson.

When an attribute is set, the appropriate attribute object is passed.
As the following example shows, to change the paint attribute to a blue-green
gradient fill, you construct a `GradientPaint` object
and then call the `setPaint` method.

```

gp = new GradientPaint(0f,0f,blue,0f,30f,green);
g2.setPaint(gp);

```

[« Previous](coordinate.html)
•
[Trail](../TOC.html)
•
[Next »](primitives.html)

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

**Previous page:** Coordinates
  
**Next page:** Geometric Primitives




A browser with JavaScript enabled is required for this page to operate properly.