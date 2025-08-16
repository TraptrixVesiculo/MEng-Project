[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** 2D Graphics
  
**Lesson:** Advanced Topics in Java2D

[Advanced Topics in Java2D](index.html)

Transforming Shapes, Text, and Images

[Clipping the Drawing Region](clipping.html)

[Compositing Graphics](compositing.html)

[Controlling Rendering Quality](quality.html)

[Constructing Complex Shapes from Geometry Primitives](complexshapes.html)

[Supporting User Interaction](user.html)

[Home Page](../../index.html)
>
[2D Graphics](../index.html)
>
[Advanced Topics in Java2D](index.html)

[« Previous](index.html) • [Trail](../TOC.html) • [Next »](clipping.html)

# Transforming Shapes, Text, and Images

You can modify the transform attribute in the `Graphics2D`
context to move, rotate, scale, and shear graphics primitives when they
are rendered. The transform attribute is defined by an instance of the
[`AffineTransform`](http://download.oracle.com/javase/7/docs/api/java/awt/geom/AffineTransform.html) class. An affine transform is a transformation
such as translate, rotate, scale, or shear in which parallel lines
remain parallel even after being transformed.

The
[`Graphics2D`](http://download.oracle.com/javase/7/docs/api/java/awt/Graphics2D.html) class provides several methods for changing the transform attribute. You can
construct a new `AffineTransform` and change the
`Graphics2D` transform attribute by calling
`transform`.

`AffineTransform` defines the following factory methods to
make it easier to construct new transforms:

* `getRotateInstance`* `getScaleInstance`* `getShearInstance`* `getTranslateInstance`

Alternatively you can use one of the `Graphics2D`
transformation methods to modify the current transform. When you call
one of these convenience methods, the resulting transform is
concatenated with the current transform and is applied during
rendering:

* `rotate`--to specify an angle of rotation in radians* `scale`--to specify a scaling factor in the *x*
    and *y* directions* `shear`--to specify a shearing factor in the *x*
      and *y* directions* `translate`--to specify a translation offset in the
        *x* and *y* directions

You can also construct an `AffineTransform` object directly and
concatenate it with the current transform by calling the
`transform`  method.

The `drawImage` method is also overloaded to allow you to
specify an `AffineTransform` that is applied to the image as
it is rendered. Specifying a transform when you call
`drawImage` does not affect the `Graphics2D`
transform attribute.

## Example: Transform

The following program is the same as `StrokeandFill`, but
also allows the user to choose a transformation to apply to the
selected object when it is rendered.

---

**Note:** If you don't see the applet running, you need to install [release 6 of the Java SE Development Kit (JDK)](http://java.sun.com/javase/downloads/index.jsp).

---

[`Transform.java`](examples/Transform.java)
contains the complete code for this applet.

When a transform is chosen from the Transform menu, the transform is
concatenated onto the `AffineTransform` `at`:

```

public void setTrans(int transIndex) {
    // Sets the AffineTransform.
    switch ( transIndex ) {
    case 0 : at.setToIdentity();
             at.translate(w/2, h/2); break;
    case 1 : at.rotate(Math.toRadians(45)); break;
    case 2 : at.scale(0.5, 0.5); break;
    case 3 : at.shear(0.5, 0.0); break;
    }
}

```

Before displaying the shape corresponding to the menu choices, the application
first retrieves the current transform from the `Graphics2D` object:

```

AffineTransform saveXform = g2.getTransform();

```

This transform will be restored to the `Graphics2D` after rendering.

After retrieving the current transform, another `AffineTransform`,
`toCenterAt`, is
created that causes shapes to be rendered in the center of the panel. The `at`
`AffineTransform` is concatenated onto `toCenterAt`:

```

AffineTransform toCenterAt = new AffineTransform();
toCenterAt.concatenate(at);
toCenterAt.translate(-(r.width/2), -(r.height/2));

```

The `toCenterAt` transform is concatenated onto the `Graphics2D` transform with the
`transform` method:

```

g2.transform(toCenterAt);

```

After rendering is completed, the original transform is restored using the
`setTransform` method:

```

g2.setTransform(saveXform);

```

---

**Note:** Never use the `setTransform` method to concatenate a coordinate transform onto
an existing transform. The `setTransform` method overwrites the
`Graphics2D`
object's current transform, which might be needed for other reasons, such
as positioning Swing and lightweight components in a window. Use these steps to perform
transformations:

1. Use the `getTransform` method to get the current transform.
2. Use `transform`, `translate`, `scale`,
   `shear`, or `rotate` to concatenate a
   transform.
3. Perform the rendering.
4. Restore the original transform using the `setTransform` method.

---

[« Previous](index.html)
•
[Trail](../TOC.html)
•
[Next »](clipping.html)

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

**Previous page:** Advanced Topics in Java2D
  
**Next page:** Clipping the Drawing Region




A browser with JavaScript enabled is required for this page to operate properly.