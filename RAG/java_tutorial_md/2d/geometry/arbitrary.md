[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** 2D Graphics
  
**Lesson:** Working with Geometry

[Working with Geometry](index.html)

[Drawing Geometric Primitives](primitives.html)

Drawing Arbitrary Shapes

[Stroking and Filling Graphics Primitives](strokeandfill.html)

[Home Page](../../index.html)
>
[2D Graphics](../index.html)
>
[Working with Geometry](index.html)

[« Previous](primitives.html) • [Trail](../TOC.html) • [Next »](strokeandfill.html)

# Drawing Arbitrary Shapes

You have already learned how to draw most of shapes represented in the `java.awt.geom`
package.
To create more complicated geometry, such as polygons, polylines, or stars
you use another class from this package, `GeneralPath`.

This class implements the
[`Shape`](http://download.oracle.com/javase/7/docs/api/java/awt/Shape.html) interface and represents a geometric path
constructed from lines, and quadratic and cubic curves. The three constructors in this class
can create the
[`GeneralPath`](http://download.oracle.com/javase/7/docs/api/java/awt/geom/GeneralPath.html) object with the default winding rule (`WIND_NON_ZERO`),
the given winding rule (`WIND_NON_ZERO` or `WIND_EVEN_ODD`), or the specified
initial coordinate capacity. The winding rule specifies how the interior of a path is determined.

```

public void Paint (Graphics g) {
    Graphics2D g2 = (Graphics2D) g;
    ...
}

```

To create an empty `GeneralPath` instance call
`new GeneralPath()` and then add segments to the
shape by using the following methods:

* `moveTo(float x, float y)` – Moves the current point of the path to the given point
* `lineTo(float x, float y)` – Adds a line segment to the current path
* `quadTo(float ctrlx, float ctrly, float x2, floaty2)` – Adds a quadratic curve segment to the current path
* `curveTo(float ctrlx1, float ctrly1, float ctrlx2, float ctrly2, float x3, floaty3)`
  – Adds a cubic curve segment to the current path
* `closePath()` – Closes the current path

The following example illustrates how to draw a polyline by using `GeneralPath`:

|  |  |
| --- | --- |
| ```  // draw GeneralPath (polyline) int x2Points[] = {0, 100, 0, 100}; int y2Points[] = {0, 50, 50, 0}; GeneralPath polyline =  	new GeneralPath(GeneralPath.WIND_EVEN_ODD, x2Points.length);  polyline.moveTo (x2Points[0], y2Points[0]);  for (int index = 1; index < x2Points.length; index++) {  	 polyline.lineTo(x2Points[index], y2Points[index]); };  g2.draw(polyline);  ``` | This image represents a polyline |

This example illustrates how to draw a polygon by using `GeneralPath`:

|  |  |
| --- | --- |
| ```  // draw GeneralPath (polygon) int x1Points[] = {0, 100, 0, 100}; int y1Points[] = {0, 50, 50, 0}; GeneralPath polygon =  	new GeneralPath(GeneralPath.WIND_EVEN_ODD, x1Points.length); polygon.moveTo(x1Points[0], y1Points[0]);  for (int index = 1; index < x1Points.length; index++) {         polygon.lineTo(x1Points[index], y1Points[index]); };  polygon.closePath(); g2.draw(polygon);  ``` | This image represents a polygon |

Note that the only difference between two last code examples is the `closePath()`
method. This method makes a polygon from a polyline by drawing a straight line back to the
coordinates of the last `moveTo`.

To add a specific path to the end of your `GeneralPath` object you use
one of the `append()` methods.
The
[`ShapesDemo2D.java`](examples/ShapesDemo2D.java) code example contains additional implementations of arbitrary shapes.

[« Previous](primitives.html)
•
[Trail](../TOC.html)
•
[Next »](strokeandfill.html)

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

**Previous page:** Drawing Geometric Primitives
  
**Next page:** Stroking and Filling Graphics Primitives




A browser with JavaScript enabled is required for this page to operate properly.