[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Deployment
  
**Lesson:** Applets
  
**Section:** Getting Started With Applets

[Applets](index.html)

[Getting Started With Applets](getStarted.html)

[Defining an Applet Subclass](subclass.html)

[Methods for Milestones](appletMethods.html)

[Life Cycle of an Applet](lifeCycle.html)

Applet's Execution Environment

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

[Solving Common Applet Problems](problemsindex.html)

[Questions and Exercises](QandE/questions.html)

[Home Page](../../index.html)
>
[Deployment](../index.html)
>
[Applets](index.html)

[« Previous](lifeCycle.html) • [Trail](../TOC.html) • [Next »](developingApplet.html)

# Applet's Execution Environment

An applet runs in the context of a browser. The Java Plug-in software in the browser controls
the launch and execution of applets. The browser also has a JavaScript interpreter, which runs
the JavaScript code on a web page. This topic describes the behavior of the
new Java Plug-in software released in Java Platform, Standard Edition 6 update 10.

## Java Plug-in

The Java Plug-in software creates a worker thread for every applet. It launches an applet
in an instance of the Java Runtime Environment (JRE) software.
Normally, all applets run in the same instance of the JRE. The
Java Plug-in software starts a new
instance of the JRE in the following cases:

* When an applet requests to be executed in a specific version of the JRE.
* When an applet specifies its own JRE startup parameters,
  for example, the heap size.
  A new applet uses an existing JRE if its requirements are a subset of an
  existing JRE, otherwise, a new JRE instance is started.

An applet will run in an existing JRE if the following conditions are met:

* The JRE version required by the applet matches an existing JRE.
* The JRE's startup parameters satisfy the applet's requirements.

The following diagram shows how applets are executed in the JRE.

![This is a picture of the Java Plug-in running applets on different JRE versions.](../../figures/deployment/applet/jre_and_browser.png)

## Java Plug-in and JavaScript Interpreter Interaction

Applets can invoke JavaScript functions present in the web page.
JavaScript functions are also
allowed to invoke methods of an applet embedded on the same web page.
The Java Plug-in software and
the JavaScript interpreter orchestrate calls from Java code to JavaScript code
and calls from JavaScript code to Java code.

The Java Plug-in software is multi-threaded, while the JavaScript interpreter
runs on a single thread. Hence, to
avoid thread-related issues, especially when multiple applets are running
simultaneously, keep the calls between
Java code and JavaScript code short, and avoid round trips, if possible.
See the following topics to find out more about interactions between Java code
and JavaScript code:

* [Invoking JavaScript Code From an Applet](../../deployment/applet/invokingJavaScriptFromApplet.html)
* [Invoking Applet Methods From JavaScript Code](../../deployment/applet/invokingAppletMethodsFromJavaScript.html)

[« Previous](lifeCycle.html)
•
[Trail](../TOC.html)
•
[Next »](developingApplet.html)

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

**Previous page:** Life Cycle of an Applet
  
**Next page:** Developing an Applet




A browser with JavaScript enabled is required for this page to operate properly.