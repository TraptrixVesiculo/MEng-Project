[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Custom Networking
  
**Lesson:** Overview of Networking

[Overview of Networking](index.html)

What You May Already Know About Networking in Java

[Networking Basics](networking.html)

[Home Page](../../index.html)
>
[Custom Networking](../index.html)
>
[Overview of Networking](index.html)

[« Previous](index.html) • [Trail](../TOC.html) • [Next »](networking.html)

# What You May Already Know About Networking in Java

The word *networking* strikes fear in the hearts of many programmers.
Fear not! Using the networking capabilities provided in the Java
environment is quite easy. In fact, you may be using the
network already without even realizing it!

## Loading Applets from the Network

If you have access to a Java-enabled browser, you have undoubtedly
already executed many applets. The applets you've run are referenced
by a special tag in an HTML file — the `<APPLET>` tag.
Applets can be located anywhere, whether on your local machine
or somewhere out on the Internet. The location of the applet is
completely invisible to you, the user. However, the location of
the applet is encoded within the `<APPLET>` tag. The browser
decodes this information, locates the applet, and runs it. If the
applet is on some machine other than your own, the browser must
download the applet before it can be run.

This is the highest level of access that you have to the Internet
from the Java development environment. Someone else has taken the
time to write a browser that does all of the grunt work of connecting
to the network and getting data from it, thereby enabling you to
run applets from anywhere in the world.

**For more information:**  
[The "Hello World!" Application](../../getStarted/cupojava/index.html) shows you how to write your first applet and run it.

The
[Applets](../../deployment/applet/index.html) trail describes how to write Java applets from A to Z.

## Loading Images from URLs

If you've ventured into writing your own Java applets and applications,
you may have run into a class in the java.net package called URL. This
class represents a Uniform Resource Locator and is the address of some
resource on the network. Your applets and applications can use a URL
to reference and even connect to resources out on the network.
For example, to load an image from the network, your Java program must
first create a URL that contains the address to the image.

This is the next highest level of interaction you can have with the
Internet — your Java program gets an address of something it wants,
creates a URL for it, and then uses some existing function in
the Java development environment that does the grunt work of
connecting to the network and retrieving the resource.

**For more information:**  
[How to Use Icons](../../uiswing/components/icon.html) shows you how to load an image into your Java program (whether applets
or applications) when you have its URL. Before you can load the image
you must create a URL object with the address of the resource in it.

[Working with URLs](../urls/index.html), the next lesson in this trail,
provides a complete discussion about URLs, including how your programs
can connect to them and read from and write to that connection.

[« Previous](index.html)
•
[Trail](../TOC.html)
•
[Next »](networking.html)

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

**Previous page:** Overview of Networking
  
**Next page:** Networking Basics




A browser with JavaScript enabled is required for this page to operate properly.