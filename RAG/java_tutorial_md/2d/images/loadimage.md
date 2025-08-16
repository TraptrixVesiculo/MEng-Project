[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** 2D Graphics
  
**Lesson:** Working with Images

[Working with Images](index.html)

Reading/Loading an Image

[Drawing an Image](drawimage.html)

[Creating and Drawing to an Image](drawonimage.html)

[Writing/Saving an Image](saveimage.html)

[Home Page](../../index.html)
>
[2D Graphics](../index.html)
>
[Working with Images](index.html)

[« Previous](index.html) • [Trail](../TOC.html) • [Next »](drawimage.html)

# Reading/Loading an Image

When you think of digital images, you probably think of
sampled image formats such as the JPEG image format used in digital photography,
or GIF images commonly used on web pages. All programs that can use
these images must first convert them from that external format into an internal
format.

Java 2D™ supports loading these external image formats into its `BufferedImage`
format using its Image I/O API which is in the `javax.imageio` package.
Image I/O has built-in support for GIF, PNG, JPEG, BMP, and WBMP.
Image I/O is also extensible so that developers or administrators
can "plug-in" support for additional formats.
For example, plug-ins for TIFF and JPEG 2000 are separately available.

To load an image from a specific file use the following code:

```

BufferedImage img = null;
try {
    img = ImageIO.read(new File("strawberry.jpg"));
} catch (IOException e) {
}

```

Image I/O recognises the contents of the file
as a JPEG format image, and decodes it into a `BufferedImage` which
can be directly used by Java 2D.

`LoadImageApp.java` shows how to display this image.

If the code is running in an applet, then its just as easy to
obtain the image from the applet codebase :

```

try {
   URL url = new URL(getCodeBase(), "strawberry.jpg");
   img = ImageIO.read(url);
} catch (IOException e) {
}

```

The `getCodeBase` method used in this example returns the URL of the directory
containing this applet.

The following example shows how to use the `getCodeBase` method
to load the strawberry.jpg file.

---

**Note:** If you don't see the applet running, you need to install [release 6 of the Java SE Development Kit (JDK)](http://java.sun.com/javase/downloads/index.jsp).

---

[`LoadImageApp.java`](examples/LoadImageApp.java) contains the complete code for this example and this applet requires the
[`strawberry.jpg`](examples/strawberry.jpg) image file.
In addition to reading from files or URLS, Image I/O can read from other
sources, such as an InputStream.

`ImageIO.read()` is the most straightforward convenience API for most
applications, but the `javax.imageio.ImageIO` provides many more static
methods for more advanced usages of the Image I/O API.
The collection of methods on this class represent just a subset
of the rich set of APIs for discovering information about the images
and for controlling the image decoding (reading) process.

We will explore some of the other capabilities of Image I/O later
in the [Writing/saving an image](../images/saveimage.html) section. More information can be found in the
[Image I/O guide](http://java.sun.com/j2se/1.4.2/docs/guide/imageio/spec/imageio_guideTOC.fm.html).

[« Previous](index.html)
•
[Trail](../TOC.html)
•
[Next »](drawimage.html)

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

**Previous page:** Working with Images
  
**Next page:** Drawing an Image




A browser with JavaScript enabled is required for this page to operate properly.