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

[Geometric Primitives](primitives.html)

[Text](text.html)

Images

[Printing](printing.html)

[Home Page](../../index.html)
>
[2D Graphics](../index.html)
>
[Overview of the Java 2D API Concepts](index.html)

[« Previous](text.html) • [Trail](../TOC.html) • [Next »](printing.html)

# Images

In the Java 2D™ API an image is typically a rectangular two-dimensional array of pixels,
where each *pixel* represents the color at that position of the image
and where the dimensions represent the horizontal extent (width)
and vertical extent (height) of the image as it is displayed.

The most important image class for representing such images is
the `java.awt.image.BufferedImage` class. The Java 2D API
stores the contents of such images in memory so that they can be directly
accessed.

Applications can directly create a `BufferedImage` object
or obtain an image from an external image format such as PNG or GIF.

In either case, the application can then draw on to image by using Java 2D
API graphics calls. So, images are not limited to displaying photographic
type images. Different objects such as line art, text, and other graphics and
even other images can be drawn onto an image (as shown on the following images).

![This figure represents an images as a drawing surface](../../figures/2d/stonehenge.gif)

The Java 2D API enables you to apply image filtering operations to `BufferedImage`
and includes several built-in filters. For example, the `ConvolveOp` filter can
be used to blur or sharpen images.

The resulting image can then be drawn to a screen, sent to a
printer, or saved in a graphics format such as PNG, GIF etc.
To learn more about images see the [Working with Images lesson](../images/index.html) lesson.

[« Previous](text.html)
•
[Trail](../TOC.html)
•
[Next »](printing.html)

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

**Previous page:** Text
  
**Next page:** Printing




A browser with JavaScript enabled is required for this page to operate properly.