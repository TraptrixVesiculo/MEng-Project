[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** 2D Graphics
  
**Lesson:** Working with Images

[Working with Images](index.html)

[Reading/Loading an Image](loadimage.html)

[Drawing an Image](drawimage.html)

Creating and Drawing to an Image

[Writing/Saving an Image](saveimage.html)

[Home Page](../../index.html)
>
[2D Graphics](../index.html)
>
[Working with Images](index.html)

[« Previous](drawimage.html) • [Trail](../TOC.html) • [Next »](saveimage.html)

# Creating and Drawing to an Image

We already know how to load an existing image, which was created and
stored in your system or in any network location. But, you probably would like also to create an
new image as a pixel data buffer.

In this case, you can create a `BufferedImage` object manually, using three constructors of this class:

* new BufferedImage(width, height, type) - constructs a `BufferedImage`
  of one of the predefined image types.
* new BufferedImage(width, height, type, colorModel) - constructs a `BufferedImage` of one of the predefined image types: `TYPE_BYTE_BINARY`
  or `TYPE_BYTE_INDEXED`.
* `new BufferedImage(colorModel, raster, premultiplied, properties)` - constructs a
  new `BufferedImage` with a specified `ColorModel` and `Raster`.

On the other hand, we can use methods of the `Component` class.
These methods can analyze the display resolution for the given `Component` or
`GraphicsConfiguration` and create an image of an appropriate type.

* `Component.createImage(width, height)`
* `GraphicsConfiguration.createCompatibleImage(width, height)`
* `GraphicsConfiguration.createCompatibleImage(width, height, transparency)`

GraphicsConfiguration returns an object of BufferedImage type, but the Component
returns an object of `Image type`, if you need a BufferedImage object instead
then you can perform an `instanceof` and cast to a `BufferedImage`
in your code.

As was already mentioned in the previous lessons, we can render images not only
on screen. An images itself can be considered as a drawing surface.
You can use a `createGraphics()` method of the `BufferedImage`
class for this purpose:

```

...

BufferedImage off_Image = 
	new BufferedImage(100, 50, BufferedImage.TYPE_INT_ARGB);

Graphics2D g2 = off_Image.createGraphics();

```

Another interesting use of offscreen images is an automatic*double buffering*. This feature allows to avoid flicker in animated images
by drawing an image to a back buffer and then copying that buffer onto the screen
instead of drawing directly to the screen.

Java 2D™ also allows access to hardware acceleration for offscreen images,
which can provide the better performance of rendering to and copying from these images.
You can get the benefit of this functionality by using the following methods of
the `Image` class:

* The `getCapabilities` method allows you to determine whether the image is currently accelerated.
* The `setAccelerationPriority` method lets you set a hint about how important acceleration is for the image.
* The `getAccelerationPriority` method gets a hint about the acceleration importance.

[« Previous](drawimage.html)
•
[Trail](../TOC.html)
•
[Next »](saveimage.html)

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

**Previous page:** Drawing an Image
  
**Next page:** Writing/Saving an Image




A browser with JavaScript enabled is required for this page to operate properly.