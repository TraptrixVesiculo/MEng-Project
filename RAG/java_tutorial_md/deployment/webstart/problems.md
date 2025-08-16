[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Deployment
  
**Lesson:** Java Web Start

[Java Web Start](index.html)

[Developing a Java Web Start Application](developing.html)

[Retrieving Resources](retrievingResources.html)

[Deploying a Java Web Start Application](deploying.html)

[Setting Up a Web Server](settingUpWebServerMimeType.html)

[Displaying a Customized Loading Progress Indicator](customProgressIndicatorForAppln.html)

[Running a Java Web Start Application](running.html)

[Java Web Start and Security](security.html)

Common Java Web Start Problems

[Questions and Exercises](QandE/questions.html)

[Home Page](../../index.html)
>
[Deployment](../index.html)
>
[Java Web Start](index.html)

[« Previous](security.html) • [Trail](../TOC.html) • [Next »](QandE/questions.html)

# Common Java Web Start Problems

This section covers some common problems that you might encounter
when developing and deploying Java Web Start applications. After each problem is a list
of possible reasons and solutions.

**Problem:**
My browser shows the Java Network Launch Protocol (JNLP) file for my
application as plain text.

Most likely, your web server is not aware of the proper MIME type for JNLP files. See the
[Setting up the web server](settingUpWebServerMimeType.html) section for more information.

Furthermore, if you are using a proxy server, ensure that the update versions of the files are returned, by updating the time stamp of the resources on the web server such that the proxies will update their caches.

**Problem:** When I try to launch my JNLP
file, I get the following error:

```

MissingFieldException[ The following required field is missing from the
launch file: (<application-desc>|<applet-desc>|<installer-desc>|<component-desc>)]
    at com.sun.javaws.jnl.XMLFormat.parse(Unknown Source)
    at com.sun.javaws.jnl.LaunchDescFactory.buildDescriptor(Unknown Source)
    at com.sun.javaws.jnl.LaunchDescFactory.buildDescriptor(Unknown Source)
    at com.sun.javaws.jnl.LaunchDescFactory.buildDescriptor(Unknown Source)
    at com.sun.javaws.Main.launchApp(Unknown Source)
    at com.sun.javaws.Main.continueInSecureThread(Unknown Source)
    at com.sun.javaws.Main.run(Unknown Source)
    at java.lang.Thread.run(Unknown Source)

```

Often this error occurs when your XML is malformed.
You can stare at the code until you figure it out but it is easier
to run an XML syntax checker over the file. (NetBeans IDE and
jEdit both provide XML syntax checkers.)

However, this error can occur in a other situations and the above was caused
by the following line in an otherwise well-formed XML file:

```

<description kind="short">Demonstrates choosing the drop location in the target <code>TransferHandler</code></description>

```

The error was caused by the illegal embedded `code` tags.

[« Previous](security.html)
•
[Trail](../TOC.html)
•
[Next »](QandE/questions.html)

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

**Previous page:** Java Web Start and Security
  
**Next page:** Questions and Exercises: Java Web Start




A browser with JavaScript enabled is required for this page to operate properly.