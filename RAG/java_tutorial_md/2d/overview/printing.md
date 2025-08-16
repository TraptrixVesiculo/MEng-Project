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

[Images](images.html)

Printing

[Home Page](../../index.html)
>
[2D Graphics](../index.html)
>
[Overview of the Java 2D API Concepts](index.html)

[« Previous](images.html) • [Trail](../TOC.html) • [Next »](../basic2d/index.html)

# Printing

All of the Swing and Java 2D™ graphics, including composited graphics and
images, can be rendered to a printer by using the Java 2D Printing API.
This API also provides document composition features that enable you to
perform such operations as changing the order in which pages are
printed.

Rendering to a printer is like rendering to a screen. The printing
system controls when pages are rendered, just like the drawing system
controls when a component is painted on the screen.

The Java 2D Printing API is based on a *callback* model in which the
printing system, not the application, controls when pages are printed.
The application provides the printing system with information about
the document to be printed, and the printing system determines when
each page needs to be imaged.

The following two features are important to support printing:

* **Job control** – Initiating and managing the print job including displaying the standard
  print and setup dialog boxes
* **Pagination** – Rendering each page when the printing system requests it

When pages need to be imaged, the
printing system calls the application’s `print` method with
an appropriate `Graphics` context. To use Java 2D API
features when you print, you cast the `Graphics` object to a
`Graphics2D` class, just like you do when you are rendering to the
screen.

[« Previous](images.html)
•
[Trail](../TOC.html)
•
[Next »](../basic2d/index.html)

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

**Previous page:** Images
  
**Next page:** Getting Started with Graphics




A browser with JavaScript enabled is required for this page to operate properly.