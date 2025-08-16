[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Deployment
  
**Lesson:** Java Web Start
  
**Section:** Deploying a Java Web Start Application

[Java Web Start](index.html)

[Developing a Java Web Start Application](developing.html)

[Retrieving Resources](retrievingResources.html)

[Deploying a Java Web Start Application](deploying.html)

Setting Up a Web Server

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

[« Previous](deploying.html) • [Trail](../TOC.html) • [Next »](customProgressIndicatorForAppln.html)

# Setting Up a Web Server

You might need to configure your web server to handle
Java Network Launch Protocol (JNLP) files. If the web server is not set up properly,
the Java Web Start application will not launch when you click on the link to the
JNLP file.

Configure the web server so that files with the `.jnlp` extension are
set to the `application/x-java-jnlp-file` MIME type.

The specific steps to set up the JNLP MIME type will vary depending on the
web server. As an example, to configure an Apache web server, you should add the
following line to the `mime.types` file.

```

application/x-java-jnlp-file JNLP

```

For other web servers, check the documentation for instructions on setting MIME types.

[« Previous](deploying.html)
•
[Trail](../TOC.html)
•
[Next »](customProgressIndicatorForAppln.html)

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

**Previous page:** Deploying a Java Web Start Application
  
**Next page:** Displaying a Customized Loading Progress Indicator




A browser with JavaScript enabled is required for this page to operate properly.