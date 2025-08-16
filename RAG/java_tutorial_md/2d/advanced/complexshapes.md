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

[Controlling Rendering Quality](quality.html)

Constructing Complex Shapes from Geometry Primitives

[Supporting User Interaction](user.html)

[Home Page](../../index.html)
>
[2D Graphics](../index.html)
>
[Advanced Topics in Java2D](index.html)

[« Previous](quality.html) • [Trail](../TOC.html) • [Next »](user.html)

# Constructing Complex Shapes from Geometry Primitives

Constructive area geometry (CAG) is the process of creating new
geometric shapes by performing boolean operations on existing ones. In
the Java 2D™ API the
[`Area`](http://download.oracle.com/javase/7/docs/api/java/awt/geom/Area.html) class implements the
[`Shape`](http://download.oracle.com/javase/7/docs/api/java/awt/Shape.html) interface and supports the following boolean operations.

|  |  |  |  |
| --- | --- | --- | --- |
| Venn diagram showing Union | Union | Venn diagram showing Subtraction | Subtraction |
| Venn diagram showing Intersection | Intersection | Venn diagram showing Exclusive-or operation | Exclusive-or (`XOR`) |

## Example: Areas

In this example `Area` objects construct a pear shape from
several ellipses.

---

**Note:** If you don't see the applet running, you need to install [release 6 of the Java SE Development Kit (JDK)](http://java.sun.com/javase/downloads/index.jsp).

---

[`Pear.java`](examples/Pear.java)
contains the complete code for this applet.

The leaves are each created by performing an intersection on two overlapping circles.

```

leaf = new Ellipse2D.Double();
...
leaf1 = new Area(leaf);
leaf2 = new Area(leaf);
...
leaf.setFrame(ew-16, eh-29, 15.0, 15.0);
leaf1 = new Area(leaf);
leaf.setFrame(ew-14, eh-47, 30.0, 30.0);
leaf2 = new Area(leaf);
leaf1.intersect(leaf2);
g2.fill(leaf1);
...
leaf.setFrame(ew+1, eh-29, 15.0, 15.0);
leaf1 = new Area(leaf);
leaf2.intersect(leaf1);
g2.fill(leaf2);

```

Overlapping circles are also used to construct the stem through a subtraction operation.

```

stem = new Ellipse2D.Double();
...
stem.setFrame(ew, eh-42, 40.0, 40.0);
st1 = new Area(stem);
stem.setFrame(ew+3, eh-47, 50.0, 50.0);
st2 = new Area(stem);
st1.subtract(st2);
g2.fill(st1);

```

The body of the pear is constructed by performing a union operation on
a circle and an oval.

```

circle = new Ellipse2D.Double();
oval = new Ellipse2D.Double();
circ = new Area(circle);
ov = new Area(oval);
...
circle.setFrame(ew-25, eh, 50.0, 50.0);
oval.setFrame(ew-19, eh-20, 40.0, 70.0);
circ = new Area(circle);
ov = new Area(oval);
circ.add(ov);
g2.fill(circ);

```

[« Previous](quality.html)
•
[Trail](../TOC.html)
•
[Next »](user.html)

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

**Previous page:** Controlling Rendering Quality
  
**Next page:** Supporting User Interaction




A browser with JavaScript enabled is required for this page to operate properly.