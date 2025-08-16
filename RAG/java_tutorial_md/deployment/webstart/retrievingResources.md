[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Deployment
  
**Lesson:** Java Web Start
  
**Section:** Developing a Java Web Start Application

[Java Web Start](index.html)

[Developing a Java Web Start Application](developing.html)

Retrieving Resources

[Deploying a Java Web Start Application](deploying.html)

[Setting Up a Web Server](settingUpWebServerMimeType.html)

[Displaying a Customized Loading Progress Indicator](customProgressIndicatorForAppln.html)

[Running a Java Web Start Application](running.html)

[Java Web Start and Security](security.html)

[Common Java Web Start Problems](problems.html)

[Questions and Exercises](QandE/questions.html)

[Home Page](../../index.html)
>
[Deployment](../index.html)
>
[Java Web Start](index.html)

[« Previous](developing.html) • [Trail](../TOC.html) • [Next »](deploying.html)

# Retrieving Resources

Use the `getResource` method to read resources from a JAR file.
For example, the following code retrieves images from a JAR file.

```

// Get current classloader
ClassLoader cl = this.getClass().getClassLoader();
// Create icons
Icon saveIcon  = new ImageIcon(cl.getResource("images/save.gif"));
Icon cutIcon   = new ImageIcon(cl.getResource("images/cut.gif"));

```

The example assumes that the following entries exist in the application's JAR file:

* images/save.gif
* images/cut.gif

[« Previous](developing.html)
•
[Trail](../TOC.html)
•
[Next »](deploying.html)

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

**Previous page:** Developing a Java Web Start Application
  
**Next page:** Deploying a Java Web Start Application




A browser with JavaScript enabled is required for this page to operate properly.