[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

Applets

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

[Solving Common Applet Problems](problemsindex.html)

[Questions and Exercises](QandE/questions.html)

**Trail:** Deployment

[Home Page](../../index.html)
>
[Deployment](../index.html)

[« Previous](../index.html) • [Trail](../TOC.html) • [Next »](getStarted.html)

# Lesson: Applets

This lesson discusses the basics of applets, how to develop applets that interact
richly with their environment, and how to deploy applets.

An applet is a special kind of Java program that a browser enabled with Java
technology can download from the internet and run.
An applet is typically embedded inside a web page and runs in the
context of a browser. An applet must be a subclass of the
`java.applet.Applet` class. The `Applet` class provides
the standard interface between the applet and the browser environment.

Swing provides a special subclass of the `Applet` class called
`javax.swing.JApplet`. The `JApplet` class should be used
for all applets that use Swing components to construct their graphical user
interfaces (GUIs).

The browser's Java Plug-in software manages the lifecycle of an applet.

---

**Note:** Some features of applets may not work as described on Mac OS. This is
because of the way the Java Plug-in software interfaces with browsers on Mac OS.

---

---

**Note:** Please make sure you have at least [Java SE Development Kit (JDK) 6 update 10](http://java.sun.com/javase/downloads/index.jsp) release on your client machine before proceeding further. You will need this to view the sample rich internet applications and read subsequent sections without interruptions.

---

[« Previous](../index.html)
•
[Trail](../TOC.html)
•
[Next »](getStarted.html)

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
  
**Next page:** Getting Started With Applets




A browser with JavaScript enabled is required for this page to operate properly.