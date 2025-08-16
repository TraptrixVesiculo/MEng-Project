[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** 2D Graphics
  
**Lesson:** Working with Geometry

[Working with Geometry](index.html)

Drawing Geometric Primitives

[Drawing Arbitrary Shapes](arbitrary.html)

[Stroking and Filling Graphics Primitives](strokeandfill.html)

[Home Page](../../index.html)
>
[2D Graphics](../index.html)
>
[Working with Geometry](index.html)

[« Previous](index.html) • [Trail](../TOC.html) • [Next »](arbitrary.html)

# Drawing Geometric Primitives

The Java 2D™ API provides several classes that define common geometric objects such as points,
lines, curves, and rectangles. These geometry classes are part of the
[`java.awt.geom`](http://download.oracle.com/javase/7/docs/api/java/awt/geom/package-frame.html) package.  
The
[`PathIterator`](http://download.oracle.com/javase/7/docs/api/java/awt/geom/PathIterator.html) interface defines methods for retrieving elements from a path.  
The
[`Shape`](http://download.oracle.com/javase/7/docs/api/java/awt/Shape.html) interface provides a set of methods for describing and inspecting
geometric path objects. This interface is implemented by the
[`GeneralPath`](http://download.oracle.com/javase/7/docs/api/java/awt/geom/GeneralPath.html) class and other geometry classes.

All examples represented in this section create geometries by using `java.awt.geom` and then render them
by using the
[`Graphics2D`](http://download.oracle.com/javase/7/docs/api/java/awt/Graphics2D.html) class.
To begin you obtain a `Graphics2D` object, for example
by casting the `Graphics` parameter of the `paint()` method.

```

public void paint (Graphics g) {
    Graphics2D g2 = (Graphics2D) g;
    ...
}

```

## Point

The
[`Point`](http://download.oracle.com/javase/7/docs/api/java/awt/Point.html) class creates a point representing a location in (x,y)
[coordinate space](../overview/coordinate.html).
The subclasses `Point2D.Float` and `Point2D.Double` provide correspondingly float and double precision
for storing the coordinates of the point.

```

//Create Point2D.Double
Point2D.Double point = new Point2D.Double(x, y);

```

To create a point with the coordinates 0,0 you use the default constructor, `Point2D.Double()`.  
You can use the `setLocation` method to set the position of the point as follows:

* `setLocation(double x, double y)` – To set the location of the point-
  defining coordinates as double values
* `setLocation(Point2D p)` – To set the location of the point using the coordinates of another point.

Also, the `Point2D` class has methods to calculate the distance between the current point and a point with
given coordinates, or the distance between two points.

## Line

The
[`Line2D`](http://download.oracle.com/javase/7/docs/api/java/awt/geom/Line2D.html) class represents a line segment in (x, y) coordinate space.
The `Line2D.Float` and `Line2D.Double` subclasses specify lines in float and double precision.
For example:

```

// draw Line2D.Double
g2.draw(new Line2D.Double(x1, y1, x2, y2));

```

![Line](../../figures/2d/2D-16.gif)

This class includes several `setLine()` methods to define the endpoints of the line.  
Aternatively, the endpoints of the line could be specified by using the constructor for the `Line2D.Float` class as follows:

* `Line2D.Float(float X1, float Y1, float X2, float Y2)`
* `Line2D.Float(Point2D p1, Point2D p2)`

Use the [`Stroke`](strokeandfill.html) object in the
`Graphics2D` class to define the stroke for the line path.

## Curves

The `java.awt.geom` package enables you to create a quadratic or cubic curve segment.

### Quadratic Curve Segment

The
[`QuadCurve2D`](http://download.oracle.com/javase/7/docs/api/java/awt/geom/QuadCurve2D.html) class implements the `Shape` interface.
This class represents a quadratic parametric curve segment in (x, y) coordinate space.
The `QuadCurve2D.Float` and `QuadCurve2D.Double` subclasses specify a quadratic curve
in float and double precision.

Several `setCurve` methods are used to specify two endpoints and a control point of the curve,
whose coordinates can be defined directly, by the coordinates of other points and by using a given array.  
A very useful method,  `setCurve(QuadCurve2D c)`, sets the quadratic curve with
the same endpoints and the control point as a supplied curve. For example:

```

// create new QuadCurve2D.Float
QuadCurve2D q = new QuadCurve2D.Float();
// draw QuadCurve2D.Float with set coordinates
q.setCurve(x1, y1, ctrlx, ctrly, x2, y2);
g2.draw(q);

```

![Quadratic parametric curve segment](../../figures/2d/quadCurve.gif)

### Cubic Curve Segment

The
[`CubicCurve2D`](http://download.oracle.com/javase/7/docs/api/java/awt/geom/CubicCurve2D.html) class also implements the
[`Shape`](http://download.oracle.com/javase/7/docs/api/java/awt/Shape.html) interface.
This class represents a cubic parametric curve segment in (x, y) coordinate space.
`CubicCurve2D.Float` and `CubicCurve2D.Double` subclasses specify a cubic curve
in float and double precision.

The `CubicCurve2D` class has similar methods for setting the curve as the
`QuadraticCurve2D`class, except with a second control point. For example:

```

// create new CubicCurve2D.Double
CubicCurve2D c = new CubicCurve2D.Double();
// draw CubicCurve2D.Double with set coordinates
c.setCurve(x1, y1, ctrlx1,
		  ctrly1, ctrlx2, ctrly2, x2, y2);
g2.draw(c);

```

![Cubic Curve Segment](../../figures/2d/cubicCurve.gif)

## Rectangle

Classes that specify primitives represented in the following example extend the `RectangularShape` class, which
implements the `Shape` interface and adds a few methods of its own.

These methods enables you to get information about a shape’s location and size, to examine the center point of a rectangle,
and to set the bounds of the shape.

The
[`Rectangle2D`](http://download.oracle.com/javase/7/docs/api/java/awt/geom/Rectangle2D.html) class represents a rectangle defined by a location (x, y) and dimension (w x h).
The `Rectangle2D.Float` and `Rectangle2D.Double` subclasses specify a rectangle
in float and double precision. For example:

```

// draw Rectangle2D.Double
g2.draw(new Rectangle2D.Double(x, y,
                               rectwidth,
                               rectheight));

```

![Rectangle](../../figures/2d/2D-17.gif)

The
[`RoundRectangle2D`](http://download.oracle.com/javase/7/docs/api/java/awt/geom/RoundRectangle2D.html) class represents a rectangle with rounded
corners defined by a location (x, y), a dimension (w x h), and the width
and height of the corner arc. The `RoundRectangle2D.Float` and `RoundRectangle2D.Double` subclasses
specify a round rectangle in float and double precision.

The rounded rectangle is specified with following parameters:

* Location
* Width
* Height
* Width of the corner arc
* Height of the corner arc

To set the location, size, and arcs of a `RoundRectangle2D` object, use the method `setRoundRect(double a, double y, double w, double h, double arcWidth, double arcHeight)`. For example:

```

// draw RoundRectangle2D.Double
g2.draw(new RoundRectangle2D.Double(x, y,
                                   rectwidth,
                                   rectheight,
                                   10, 10));

```

![Rounded Rectangle](../../figures/2d/2D-18.gif)

## Ellipse

The
[`Ellipse2D`](http://download.oracle.com/javase/7/docs/api/java/awt/geom/Ellipse2D.html) class represents an ellipse defined by a bounding rectangle.
The `Ellipse2D.Float` and `Ellipse2D.Double` subclasses
specify an ellipse in float and double precision.

Ellipse is fully defined by a location, a width and a height. For example:

```

// draw Ellipse2D.Double
g2.draw(new Ellipse2D.Double(x, y,
                             rectwidth,
                             rectheight));

```

![Ellipse](../../figures/2d/2D-20.gif)

## Arc

To draw a piece of an ellipse, you use the
[`Arc2D`](http://download.oracle.com/javase/7/docs/api/java/awt/geom/Arc2D.html) class. This class represents an arc defined
by a bounding rectangle, a start angle, an angular extent, and a closure type.
The `Arc2D.Float` and `Arc2D.Double` subclasses
specify an ellipse in float and double precision.

The `Arc2D` class defines the following three types of arcs,
represented by corresponding constants in this class: OPEN, PIE and CHORD.

![Arc](../../figures/2d/2D-19.gif)

Several methods set the size and parameters of the arc:

* Directly, by coordinates
* By supplied `Point2D` and `Dimension2D`
* By copying an existing `Arc2D`

Also, you can use the `setArcByCenter` method to specify an arc from a center point,
given by its coordinates and a radius.

```

// draw Arc2D.Double
g2.draw(new Arc2D.Double(x, y,
                         rectwidth,
                         rectheight,
                         90, 135,
                         Arc2D.OPEN));

```

![Arc](../../figures/2d/2D-19.gif)

The
[`ShapesDemo2D.java`](examples/ShapesDemo2D.java) code example contains implementations off all described
geometric primitives.
For more information about classes and methods represented in this section see the
[`java.awt.geom`](http://download.oracle.com/javase/7/docs/api/java/awt/geom/package-summary.html) specification.

[« Previous](index.html)
•
[Trail](../TOC.html)
•
[Next »](arbitrary.html)

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

**Previous page:** Working with Geometry
  
**Next page:** Drawing Arbitrary Shapes




A browser with JavaScript enabled is required for this page to operate properly.