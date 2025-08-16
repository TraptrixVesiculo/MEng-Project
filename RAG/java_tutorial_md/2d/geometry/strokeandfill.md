[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** 2D Graphics
  
**Lesson:** Working with Geometry

[Working with Geometry](index.html)

[Drawing Geometric Primitives](primitives.html)

[Drawing Arbitrary Shapes](arbitrary.html)

Stroking and Filling Graphics Primitives

[Home Page](../../index.html)
>
[2D Graphics](../index.html)
>
[Working with Geometry](index.html)

[« Previous](arbitrary.html) • [Trail](../TOC.html) • [Next »](../text/index.html)

# Stroking and Filling Graphics Primitives

You already know how to create different geometric
primitives and more complicated shapes. This lesson teaches how to add some color and fancy outlines
to your graphics and represents filling and stroking:

* *Filling* – is a process of painting the shape’s interior
  with solid color or a color gradient, or a texture pattern
* *Stroking* – is a process of drawing a
  shape’s outline applying stroke width, line style, and color attribute

To apply fancy line styles and fill patterns to geometric primitives change
the stroke and paint attributes in the
[`Graphics2D`](http://download.oracle.com/javase/7/docs/api/java/awt/Graphics2D.html) context before rendering. For
example, draw a dashed line by creating an appropriate
[`Stroke`](http://download.oracle.com/javase/7/docs/api/java/awt/Stroke.html) object. To add this stroke to the `Graphics2D` context before
you render the line call the `setStroke` method .
Similarly, you apply a gradient fill to a `Shape` object by
creating a `GradientPaint` object and adding it to the
`Graphics2D` context.

The following code lines enrich geometric primitives with
filling and stroking context:

```

// draw RoundRectangle2D.Double

final static float dash1[] = {10.0f};
    final static BasicStroke dashed = new BasicStroke(1.0f,
                                          BasicStroke.CAP_BUTT,
                                          BasicStroke.JOIN_MITER,
                                          10.0f, dash1, 0.0f);
g2.setStroke(dashed);
g2.draw(new RoundRectangle2D.Double(x, y,
                                   rectWidth,
                                   rectHeight,
                                   10, 10));

```

![Dashed rounded rectangle](../../figures/2d/2D-18.gif)

```

// fill Ellipse2D.Double
redtowhite = new GradientPaint(0,0,color.RED,100, 0,color.WHITE);
g2.setPaint(redtowhite);
g2.fill (new Ellipse2D.Double(0, 0, 100, 50));

```

![Polygon filled with gradient color](../../figures/2d/2D-26.gif)

The
[`ShapesDemo2D.java`](examples/ShapesDemo2D.java) code example represents additional implementations of stoking and filling.

## Defining Fancy Line Styles and Fill Patterns

Using the Java 2D™ `Stroke` and `Paint` classes, you can define fancy line styles and fill patterns.

### Line Styles

Line styles are defined by the stroke attribute in the
`Graphics2D` rendering context. To set the stroke attribute,
you create a `BasicStroke` object and pass it into the
`Graphics2D` `setStroke` method.

A `BasicStroke` object holds information about the line
width, join style, end-cap style, and dash style. This information is
used when a `Shape` is rendered with the `draw`
method.

The *line width*
is the thickness of the line measured perpendicular to its trajectory.
The line width is specified as a `float` value in user
coordinate units, which are roughly equivalent to 1/72 of an inch when the
default transform is used.

The *join style*
is the decoration that is applied where two line segments meet.
`BasicStroke` supports the following three join styles:

![Join bevel stroke style](../../figures/2d/2D-28.gif)`JOIN_BEVEL`

![Join miter stroke style](../../figures/2d/2D-29.gif)`JOIN_MITER`

![Join round stroke style](../../figures/2d/2D-30.gif) `JOIN_ROUND`

The *end-cap style*
is the decoration that is applied where a line segment ends.
`BasicStroke` supports the following three end-cap styles:

![Butt end-cap style](../../figures/2d/2D-31.gif)`CAP_BUTT`

![Round end-cap style](../../figures/2d/2D-32.gif)`CAP_ROUND`

![Square end-cap style](../../figures/2d/2D-33.gif)`CAP_SQUARE`

The *dash style*
defines the pattern of opaque and transparent sections applied along
the length of the line. The dash style is defined by a dash array and
a dash phase. The *dash array*
defines the dash pattern. Alternating elements in the array represent
the dash length and the length of the space between dashes in user
coordinate units. Element 0 represents the first dash, element 1 the
first space, and so on. The *dash phase*
is an offset into the dash pattern, also specified in user coordinate
units. The dash phase indicates what part of the dash pattern is
applied to the beginning of the line.

### Fill Patterns

Fill patterns are defined by the paint attribute in the
`Graphics2D` rendering context. To set the paint attribute,
you create an instance of an object that implements the
`Paint` interface and pass it into the
`Graphics2D` `setPaint` method.

The following three classes implement the `Paint` interface:
`Color`, `GradientPaint`, and
`TexturePaint`.

To create a `GradientPaint`,
you specify a beginning position and color and an ending position and
color. The gradient changes proportionally from one color to the other color
along the line connecting the two positions. For example:

![Gradient filling](../../figures/2d/2D-34.gif)

The pattern for a `TexturePaint` class
is defined by a `BufferedImage` class.
To create a `TexturePaint` object,
you specify the image that contains the pattern and a rectangle that
is used to replicate and anchor the pattern.
The following image represents this feature:

![Using a texture to fill a rectangle](../../figures/2d/2D-35.gif)

[« Previous](arbitrary.html)
•
[Trail](../TOC.html)
•
[Next »](../text/index.html)

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

**Previous page:** Drawing Arbitrary Shapes
  
**Next page:** Working with Text APIs




A browser with JavaScript enabled is required for this page to operate properly.