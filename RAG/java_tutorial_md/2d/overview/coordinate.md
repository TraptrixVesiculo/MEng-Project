[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** 2D Graphics
  
**Lesson:** Overview of the Java 2D API Concepts

[Overview of the Java 2D API Concepts](index.html)

Coordinates

[Java 2D Rendering](rendering.html)

[Geometric Primitives](primitives.html)

[Text](text.html)

[Images](images.html)

[Printing](printing.html)

[Home Page](../../index.html)
>
[2D Graphics](../index.html)
>
[Overview of the Java 2D API Concepts](index.html)

[« Previous](index.html) • [Trail](../TOC.html) • [Next »](rendering.html)

# Coordinates

The Java 2D™ API maintains two coordinate spaces.

* *User space* – The space in which
  graphics primitives are specified* *Device space* – The coordinate system of
    an output device such as a screen, window, or a printer

User space is a device-independent logical coordinate system, the
coordinate space that your program uses. All geometries passed into
Java 2D rendering routines are specified in user-space coordinates.

When the default transformation from user space to device space is
used, the origin of user space is the upper-left corner of the
component’s drawing area. The *x* coordinate
increases to the right, and the *y* coordinate
increases downward, as shown in the following figure. The top-left corner
of a window is 0,0. All coordinates are specified using integers, which is usually
sufficient. However, some cases require floating point or even
double precision which are also supported.

![This figure represents the space in which](../../figures/2d/2D-11.gif)

Device space is a device-dependent coordinate system that varies
according to the target rendering device. Although the coordinate
system for a window or screen might be very different from the coordinate system of
a printer, these differences are invisible to Java programs. The
necessary conversions between user space and device space are performed
automatically during rendering.

[« Previous](index.html)
•
[Trail](../TOC.html)
•
[Next »](rendering.html)

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

**Previous page:** Overview of the Java 2D API Concepts
  
**Next page:** Java 2D Rendering




A browser with JavaScript enabled is required for this page to operate properly.