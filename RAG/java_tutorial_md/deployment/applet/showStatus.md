[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Deployment
  
**Lesson:** Applets
  
**Section:** Doing More With Applets

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

Displaying Short Status Strings

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

[Solving Common Applet Problems](problemsindex.html)

[Questions and Exercises](QandE/questions.html)

[Home Page](../../index.html)
>
[Deployment](../index.html)
>
[Applets](index.html)

[« Previous](param.html) • [Trail](../TOC.html) • [Next »](browser.html)

# Displaying Short Status Strings

All browsers allow applets to display a short status string. All applets on the page, as well as the browser itself, share the same status line.

Never put crucial information in the status line.
If many users might need the information, display that information within the
applet area. If only a few, sophisticated users might need the information,
consider sending the information to standard output (see
[Writing Diagnostics to Standard Output and Error Streams](stdout.html)).

The status line is not usually very prominent, and it can be overwritten by
other applets or by the browser. For these reasons, it is best used for
incidental, transitory information. For example, an applet that loads several
image files might display the name of the image file it is currently loading.

Applets display status lines with the
[`showStatus`](http://download.oracle.com/javase/7/docs/api/java/applet/Applet.html#showStatus(java.lang.String)) method, inherited in the `JApplet` class from the `Applet` class.

Here is an example of its use:

```

showStatus("MyApplet: Loading image file " + file);

```

---

**Note:** 
Don't put scrolling text in the status line.
Browser users find such behavior highly annoying.

---

[« Previous](param.html)
•
[Trail](../TOC.html)
•
[Next »](browser.html)

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

**Previous page:** Defining and Using Applet Parameters
  
**Next page:** Displaying Documents in the Browser




A browser with JavaScript enabled is required for this page to operate properly.