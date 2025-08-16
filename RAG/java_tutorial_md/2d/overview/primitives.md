[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** 2D Graphics
  
**Lesson:** Overview of the Java 2D API Concepts

[Overview of the Java 2D API Concepts](index.html)

[Coordinates](coordinate.html)

[Java 2D Rendering](rendering.html)

Geometric Primitives

[Text](text.html)

[Images](images.html)

[Printing](printing.html)

[Home Page](../../index.html)
>
[2D Graphics](../index.html)
>
[Overview of the Java 2D API Concepts](index.html)

[« Previous](rendering.html) • [Trail](../TOC.html) • [Next »](text.html)

# Geometric Primitives

The Java 2D™ API provides a useful set of standard shapes such as points, lines,
rectangles, arcs, ellipses, and curves. The most important package to define
common geometric primitives is the `java.awt.geom` package.
Arbitrary shapes can
be represented by combinations of straight geometric primitives.

The `Shape` interface represents a geometric shape, which has an
outline and an interior. This interface provides a common set of methods for describing and
inspecting two-dimensional geometric objects and supports curved line segments
and multiple sub-shapes.
The
[`Graphics`](http://download.oracle.com/javase/7/docs/api/java/awt/Graphics.html) class supports only straight line segments. The
[`Shape`](http://download.oracle.com/javase/7/docs/api/java/awt/Shape.html) interface can support curves segments.

For more details about how to draw and fill shapes, see the
[Working with Geometry](../geometry/index.html) lesson.

## Points

The `Point2D` class defines a point representing a location in (x, y)
coordinate space. The term “point” in the Java 2D API is not the same as a
pixel. A point has no area, does not contain a color, and cannot be rendered.

Points are used to create other shapes. The`Point2D` class also includes a
method for calculating the distance between two points.

## Lines

The `Line2D` class is an abstract class that represents a line.
A line’s coordinates can be retrieved as double. The `Line2D` class includes several
methods for setting a line’s endpoints.

Also, you can create a straight line segment by using the `GeneralPath` class
described below.

## Rectangular Shapes

The `Rectangle2D`, `RoundRectangle2D`,
`Arc2D`, and `Ellipse2D` primitives are all
derived from the `RectangularShape` class. This class defines methods for
`Shape` objects that can be described by a rectangular
bounding box. The geometry of a `RectangularShape` object can be
extrapolated from a rectangle that completely encloses the outline of
the `Shape`.

![Rectangular shape](../../figures/2d/2D-13.gif )

## Quadratic and Cubic Curves

The `QuadCurve2D` enables you to create quadratic parametric curve
segments. A quadratic curve is defined by two endpoints and one control point.

The `CubicCurve2D` class enables you to create cubic parametric curve
segments. A cubic curve is defined by two endpoints and two control points. The
following are examples of quadratic and cubic curves. See
[Stroking and Filling](../geometry/strokeandfill.html)
for implementations of cubic and quadratic curves.

This figure represents a quadratic curve.

![Quadratic parametric curve](../../figures/2d/2D-14.gif )

This figure represents a cubic curve.

![Cubic parametric curve](../../figures/2d/2D-15.gif )

## Arbitrary Shapes

The `GeneralPath` class enables you to construct an arbitrary shape by
specifying a series of positions along the shape’s
boundary. These positions can
be connected by line segments, quadratic curves, or cubic (Bézier) curves. The
following shape can be created with three line segments and a cubic curve. See
[Stroking and Filling](../geometry/strokeandfill.html)
for more information about the implementation of this shape.

![This figure represents a polyshape created by using the GeneralPath class](../../figures/2d/PolyShape.gif)

## Areas

With the `Area` class, you can perform boolean operations,
such as union, intersection, and subtraction, on any two
`Shape` objects. This technique, often referred to as
*constructive area geometry*, enables you to quickly create complex
`Shape`
objects without having to describe each line segment or curve.

[« Previous](rendering.html)
•
[Trail](../TOC.html)
•
[Next »](text.html)

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

**Previous page:** Java 2D Rendering
  
**Next page:** Text




A browser with JavaScript enabled is required for this page to operate properly.