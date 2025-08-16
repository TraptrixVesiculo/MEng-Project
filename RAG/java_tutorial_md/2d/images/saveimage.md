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

[Creating and Drawing to an Image](drawonimage.html)

Writing/Saving an Image

[Home Page](../../index.html)
>
[2D Graphics](../index.html)
>
[Working with Images](index.html)

[« Previous](drawonimage.html) • [Trail](../TOC.html) • [Next »](../printing/index.html)

# Writing/Saving an Image

This lesson started with an explanation for using the
`javax.imageio` package, to load images
from an external image format into Java 2D™'s internal `BufferedImage` format.
Then it explains how to use the `Graphics.drawImage()` to draw that image, with optional
filtering.

The final stage is saving a `BufferedImage` object into an external image format.
This may be an image that was originally loaded by the `Image I/O` class
from an external image format and perhaps modified using the Java 2D APIs,
or it may be one that was created by Java 2D.

The `Image I/O` class provides a simple way to save images in a variety of image formats
in the following example:

```

static boolean ImageIO.write(RenderedImage im,
                             String formatName,
                             File output) throws IOException

```

---

**Note:** the `BufferedImage` class implements the
`RenderedImage` interface.

---

.

The `formatName` parameter selects the image format in which to save the
`BufferedImage`.

```

try {
    BufferedImage bi = getMyImage(); // retrieve image
    File outputfile = new File("saved.png");
    ImageIO.write(bi, "png", outputfile);
} catch (IOException e) {
    ...
}

```

The `ImageIO.write` method calls the code that implements PNG writing a “PNG writer plug-in”.
The term *plug-in* is used since `Image I/O` is extensible and can
support a wide range of formats.

But the following standard image format plugins :
JPEG, PNG, GIF, BMP and WBMP are always be present.

Each image format has its advantages and disadvantages:

|  |  |  |
| --- | --- | --- |
|  | Plus | Minus |
| GIF | Supports animation, and transparent pixels | Supports only 256 colors and no translucency |
| PNG | Better alternative than GIF or JPG for high colour lossless images, supports translucency | Doesn't support animation |
| JPG | Great for photographic images | Loss of compression, not good for text, screenshots, or any application where the original image must be preserved exactly |

For most applications it is sufficient to use one of these standard
plugins. They have the advantage of being readily available.
The `Image I/O` class provides a way to plug in support for additional formats
which can be used, and many such plug-ins exist.
If you are interested in what file formats are available to load
or save in your system, you may use the `getReaderFormatNames`
and `getWriterFormatNames` methods of the `ImageIO` class.
These methods return an array of strings listing all of the formats supported
in this JRE.

```

String writerNames[] = ImageIO.getWriterFormatNames();

```

The returned array of names will include any additional plug-ins that are
installed and any of these names may be used as a format name to select
an image writer.
The following code example is a simple version of a complete
image edit/touch up program which uses a revised version of the
[`ImageDrawingApplet.java`](examples/ImageDrawingApplet.java) sample program which can be used as follows :

* An image is first loaded via Image I/O* The user selects a filter from the drop down list and a new
    updated image is drawn* The user selects a save format from the drop down list* Next a file chooser appears and the user selects where to save the image* The modified image can now be viewed by other desktop applications

The complete code of this example is represented in
[`SaveImage.java`](examples/SaveImage.java).

In this lesson you have learned just the basics of `Image I/O`, which provides
extensive support for writing images, including working directly with an `ImageWriter` plug-in to achieve finer
control over the encoding process. ImageIO can write multiple images, image metadata,
and determine quality vs. size tradeoffs.
For more information see
[Java Image I/O API Guide](http://java.sun.com/javase/6/docs/technotes/guides/imageio/spec/title.fm.html).

[« Previous](drawonimage.html)
•
[Trail](../TOC.html)
•
[Next »](../printing/index.html)

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

**Previous page:** Creating and Drawing to an Image
  
**Next page:** Printing




A browser with JavaScript enabled is required for this page to operate properly.