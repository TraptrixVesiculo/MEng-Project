[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../search.html)

[Home Page](../index.html)

[« Previous](../index.html)
•
[Trail](./TOC.html)
•
[Next »](./basics/index.html)

# Trail: The Extension Mechanism

The extension mechanism was introduced as a new feature in the
JavaTM 1.2 platform.
The extension mechanism provides a standard, scalable way to make
custom APIs available to all applications running on the Java platform.
As of the
Java 1.3 platform release, *Java
extensions* are also referred to as *optional packages*. This
trail may use both terms interchangeably.

*Extensions* are groups of packages and classes that augment the Java
platform through the extension mechanism. The extension mechanism
enables the runtime environment to find and load extension classes without
the extension classes having to be named on the class path.
In that respect, extension classes are similar to the Java platform's
core classes. That's also where extensions get their name -- they,
in effect, extend the platform's core API.

Since this mechanism extends the platform's core API, its use
should be judiciously applied. Most commonly it is used for well standarized
interfaces such as those defined by the
Java Community ProcessSM,
although it may also be
appropriate for site wide interfaces.

![This figure shows the relationships between Application, Java Platform, and Extensions.](../figures/ext/exta.gif)

As the diagram indicates, extensions act as
"add-on" modules to the Java platform. Their classes and public APIs are
automatically available to any applications running on the platform.

The extension mechanism also provides a means for extension classes to be
downloaded from remote locations for use by applets.

Extensions are bundled as Java Archive (JAR) files, and this trail
assumes that you are familiar with the JAR file format. If you're not
up to speed on JAR files, you might want to review some JAR-file documentation
before proceeding with the lessons in this trail:

* The
  [Packaging Programs in JAR Files](../deployment/jar/index.html) lesson in this tutorial.* The
    [JAR Guide](http://download.oracle.com/javase/7/docs/technotes/guides/jar/jarGuide.html) in the JDKTM documentation.

This trail has two lessons:

### [Creating and Using Extensions](./basics/index.html)

> This section
> shows you what you need to do to add an extension to your Java platform
> and how applets can benefit from the extension mechanism by
> downloading remote extension classes.

### [Making Extensions Secure](./security/index.html)

> This section describes
> security privileges and
> permissions that are granted to extensions on your platform. You'll
> see how to use the Java platform's security architecture if you're writing
> extensions classes of your own.

### Additional Documentation

You can find further information about extensions in the
[The Java Extensions Mechanism](http://download.oracle.com/javase/7/docs/technotes/guides/extensions/) section of the JDK documentation.

[« Previous](../index.html)
•
[TOC](./TOC.html)
•
[Next »](./basics/index.html)

---

Problems with the examples? Try [Compiling and Running
the Examples: FAQs](../information/run-examples.html).
  
Complaints? Compliments? Suggestions? [Give
us your feedback](http://download.oracle.com/javase/feedback.html).

Your use of this page and all the material on pages under "The Java Tutorials" banner,
and all the material on pages under "The Java Tutorials" banner is subject to the [Java SE Tutorial Copyright
and License](../information/license.html).
Additionally, any example code contained in any of these Java
Tutorials pages is licensed under the
[Code
Sample License](http://developers.sun.com/license/berkeley_license.html).

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| |  |  | | --- | --- | | duke image | Oracle logo | | [About Oracle](http://www.oracle.com/us/corporate/index.html) | [Oracle Technology Network](http://www.oracle.com/technology/index.html) | [Terms of Service](https://www.samplecode.oracle.com/servlets/CompulsoryClickThrough?type=TermsOfService) | Copyright © 1995, 2011 Oracle and/or its affiliates. All rights reserved. |

**Previous page:** Beginning of Tutorial
  
**Next page:** Creating and Using Extensions




A browser with JavaScript enabled is required for this page to operate properly.