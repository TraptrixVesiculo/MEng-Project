[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

Creating and Using Extensions

[Installed Extensions](install.html)

[Download Extensions](download.html)

[Understanding Extension Class Loading](load.html)

**Trail:** The Extension Mechanism

[Home Page](../../index.html)
>
[The Extension Mechanism](../index.html)

[« Previous](../index.html) • [Trail](../TOC.html) • [Next »](install.html)

# Lesson: Creating and Using Extensions

Any set of packages or classes can easily be made to play the role of
an extension. The first step in turning a set of classes into an extension
is to bundle them in a JAR file. Once that's done, you can turn the software
into an extension in two ways:

* by placing the JAR file in a special location in the
  directory structure of the Java Runtime Environment, in which
  case it's called an *installed* extension.* by referencing the JAR file in a specified way from the manifest of the
    another JAR file, in which case it's called a
    *download* extension.

This lesson shows you how the extension mechanism works by using a
simple "toy" extension as an example.

### [Installed Extensions](install.html)

> In this section, you'll create a simple installed extension and see
> how extension software is treated as part of the platform by the
> runtime environment.

### [Download Extensions](download.html)

> This section will show you how modify a JAR file's manifest so that
> the JAR-bundled software can make use of download extensions.

### [Understanding Extension Class Loading](load.html)

> This section is a short detour that summarizes the Java platform's
> delegation model for loading classes, and shows how it relates to loading
> classes in extensions.

The next lesson,
[Making Extensions Secure](../security/index.html) uses the same extension to show how the Java platform controls the
security permissions that are granted to extensions.

[« Previous](../index.html)
•
[Trail](../TOC.html)
•
[Next »](install.html)

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

**Previous page:** Table of Contents
  
**Next page:** Installed Extensions




A browser with JavaScript enabled is required for this page to operate properly.