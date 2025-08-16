[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Deployment
  
**Lesson:** Applets

[Applets](index.html)

[Getting Started With Applets](getStarted.html)

[Defining an Applet Subclass](subclass.html)

[Methods for Milestones](appletMethods.html)

[Life Cycle of an Applet](lifeCycle.html)

[Applet's Execution Environment](appletExecutionEnv.html)

[Developing an Applet](developingApplet.html)

[Deploying an Applet](deployingApplet.html)

[Deploying With the Applet Tag](html.html)

[Doing More With Applets](doingMoreWithApplets.html)

[Finding and Loading Data Files](data.html)

[Defining and Using Applet Parameters](param.html)

[Displaying Short Status Strings](showStatus.html)

[Displaying Documents in the Browser](browser.html)

[Invoking JavaScript Code From an Applet](invokingJavaScriptFromApplet.html)

[Invoking Applet Methods From JavaScript Code](invokingAppletMethodsFromJavaScript.html)

[Manipulating DOM of Applet's Web Page](manipulatingDOMFromApplet.html)

[Displaying a Customized Loading Progress Indicator](customProgressIndicatorForApplet.html)

[Writing Diagnostics to Standard Output and Error Streams](stdout.html)

[Developing Draggable Applets](draggableApplet.html)

[Communicating With Other Applets](iac.html)

[Working With a Server-Side Application](server.html)

[Network Client Applet Example](clientExample.html)

[What Applets Can and Cannot Do](security.html)

Solving Common Applet Problems

[Questions and Exercises](QandE/questions.html)

[Home Page](../../index.html)
>
[Deployment](../index.html)
>
[Applets](index.html)

[« Previous](security.html) • [Trail](../TOC.html) • [Next »](QandE/questions.html)

# Solving Common Applet Problems

This section covers some common problems that you might encounter
when writing Java applets. After each problem is a list
of possible reasons and solutions.

**Problem:** My applet does not display.

* Check the Java Console log for errors.
* Check the syntax of the applet's Java Network Launch Protocol (JNLP) file.
  Incorrect JNLP files are the most common reason for failures without obvious errors.
* Check the JavaScript syntax if deploying using the `runApplet`
  function of the Deployment Toolkit. See
  [Deploying an Applet](../../deployment/deploymentInDepth/runAppletFunction.html) for details.

**Problem:** The Java Console log displays java.lang.ClassNotFoundException.

* Make sure your Java source files compiled correctly.
* If deploying using the `<applet>` tag, check that the path
  to the applet JAR file is specified accurately in the `archive` attribute.
* If launching using a JNLP file, check the path in the `jar` tag in the JNLP file.
* Make sure the applet's JAR file, JNLP file, and web page are located in the correct
  directory and reference each other accurately.

**Problem:** I was able to build the code once, but now the build fails
even though there are no compilation errors.

* Close your browser and run the build again. The browser most likely has
  a lock on the JAR file, because of which the build process is unable to regenerate
  the JAR file.

**Problem:** When I try to load a web page that has an applet,
my browser redirects me to `www.java.com` without any warning

* The applet on the web page is most likely deployed using
  the Deployment Toolkit script.
  The applet may require a later version of the Java Runtime Environment software
  than the version that currently exists on the client.
  Check the `minimumVersion` parameter of the `runApplet` function
  in the applet's web page. See
  [Deploying an Applet](../../deployment/deploymentInDepth/runAppletFunction.html) for details.

**Problem:** I fixed some bugs and re-built my applet's source code. When I
reload the applet's web page, my fixes are not showing up.

* You may be viewing a previously cached version of the applet. Close the browser.
  Open the Java Control Panel and delete temporary internet files. This will remove your
  applet from cache. Try viewing your applet again.

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

**Previous page:** What Applets Can and Cannot Do
  
**Next page:** Questions and Exercises: Applets




A browser with JavaScript enabled is required for this page to operate properly.