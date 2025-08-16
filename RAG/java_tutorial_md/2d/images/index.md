[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

Working with Images

[Reading/Loading an Image](loadimage.html)

[Drawing an Image](drawimage.html)

[Creating and Drawing to an Image](drawonimage.html)

[Writing/Saving an Image](saveimage.html)

**Trail:** 2D Graphics

[Home Page](../../index.html)
>
[2D Graphics](../index.html)

[« Previous](../text/index.html) • [Trail](../TOC.html) • [Next »](loadimage.html)

# Lesson: Working with Images

As you have already learned from the [Overview](../overview/images.html)
lesson, `Image`s are described by a width and a height, measured in pixels,
and have a coordinate system that is independent of the drawing surface.

There are a number of common tasks when working with images.

* Loading an external GIF, PNG JPEG image format file into Java 2D™'s internal image representation.
* Directly creating a Java 2D image and rendering to it.
* Drawing the contents of a Java 2D image on to a drawing surface.
* Saving the contents of a Java 2D image to an external GIF, PNG, or JPEG image file.

This lesson teaches you the basics of loading, displaying, and saving images.

The are two main classes that you must learn about to work with images:

* The
  [`java.awt.Image`](http://download.oracle.com/javase/7/docs/api/java/awt/Image.html) class is the superclass that
  represents graphical images as rectangular arrays of pixels.
* The
  [`java.awt.image.BufferedImage`](http://download.oracle.com/javase/7/docs/api/java/awt/image/BufferedImage.html) class, which extends the `Image` class to allow the application to operate directly with image
  data (for example, retrieving or setting up the pixel color). Applications can
  directly construct instances of this class.

The `BufferedImage` class is a cornerstone of the Java 2D immediate-mode
imaging API. It manages the image in memory and provides methods for storing, interpreting,
and obtaining pixel data.
Since `BufferedImage` is a subclass of `Image` it can be rendered by the
`Graphics` and `Graphics2D` methods that accept an `Image` parameter.

A `BufferedImage` is essentially an `Image` with an accessible data buffer.
It is therefore more efficient to work directly with `BufferedImage`.
A `BufferedImage` has a *ColorModel* and a *Raster* of image data. The ColorModel provides a color interpretation of the image's pixel data.

The Raster performs the following functions:

* Represents the rectangular coordinates of the image
* Maintains image data in memory
* Provides a mechanism for creating multiple subimages from a single image data buffer
* Provides methods for accessing specific pixels within the image

The basic operations with images are represented in the following sections:

## [Reading/Loading an image](loadimage.html)

This section explains how to load an image from an external image
format into a Java application using the Image I/O API

## [Drawing an image](drawimage.html)

This section teaches how to display images using the `drawImage`
method of the `Graphics` and `Graphics2D` classes.

## [Creating and drawing To an image](drawonimage.html)

This section describes how to create an image and how to use the
image itself as a drawing surface.

## [Writing/saving an image](saveimage.html)

This section explains how to save created images in an appropriate format.

[« Previous](../text/index.html)
•
[Trail](../TOC.html)
•
[Next »](loadimage.html)

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

**Previous page:** Previous Lesson
  
**Next page:** Reading/Loading an Image




A browser with JavaScript enabled is required for this page to operate properly.