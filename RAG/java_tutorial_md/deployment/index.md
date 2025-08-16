[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../search.html)

[Home Page](../index.html)

[« Previous](../index.html)
•
[Trail](./TOC.html)
•
[Next »](./applet/index.html)

# Trail: Deployment

Rich internet applications (RIA) are applications that have traits similar to
desktop applications, but are deployed via the internet. RIAs may be developed
and deployed as applets or Java Web Start applications.

* Applets - Applets run in the context of a browser. The
  Java Plug-in software controls the execution and
  lifecycle of applets.
* Java Web Start applications - Java Web Start applications are
  launched via a browser the first time. They may subsequently be launched
  from a desktop shortcut.
  Once a Java Web Start application is downloaded and
  its security certificate has been accepted by the user, it behaves
  *almost* like a standalone
  application.

## Component-Based Architecture

In the past, the decision of whether to deploy a Java rich internet application
inside the browser as an applet, or outside the browser as a Java Web Start
application, could significantly impact the design of the application. With the next
generation Java Plug-in, this decision has been greatly simplified.

Traditionally, applications construct their user
interfaces, including the top-level `Frame`, in the `main` method. This programming
style prevents easy re-deployment of the application in the browser, because it
assumes that the application creates its own `Frame`. When running in the browser as
an applet, the applet is the top level container that should hold the user
interface for the application. A top-level `Frame` is not needed.

Use *component-based architecture* when designing your rich internet application.
Try to organize its
functionality into one or more components that can be composed together.
In this context, the term "component" refers to a GUI element that is a subclass of the AWT
`Component` class, the Swing `JComponent` class,
or another subclass. For example, you could have a top
level `JPanel` which contains other UI components in it
(like a combination of more nested JPanels
and text fields, combo boxes etc.). With such a design, it becomes relatively easy to deploy the
core functionality as an applet or a Java Web Start application.

To deploy as an applet, you just need
to wrap the core functionality in an `Applet` or `JApplet`
and add the browser specific functionality,
if necessary. To deploy as a Java Web Start application, wrap the functionality
in a `JFrame`.

## Choosing Between Applets and Java Web Start Applications

The
[Rich Internet Applications Decision Guide](./_riaDecisionGuide.html) contains detailed information to help you decide whether to deploy your code
as an applet or Java Web Start application.

This trail discusses the development and deployment of RIAs.

[![trail icon](../images/coreIcon.gif)
**Developing and Deploying Applets**](applet/index.html)


[![trail icon](../images/coreIcon.gif)
**Developing and Deploying Java Web Start Applications**](webstart/index.html)


[![trail icon](../images/coreIcon.gif)
**Doing More With Rich Applications**](doingMoreWithRIA/index.html)


[![trail icon](../images/coreIcon.gif)
**Deployment In-Depth**](deploymentInDepth/index.html)

Supporting Tools

[![trail icon](../images/coreIcon.gif)
**Packaging Programs in JAR Files**](jar/index.html)

[« Previous](../index.html)
•
[TOC](./TOC.html)
•
[Next »](./applet/index.html)

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
  
**Next page:** Applets




A browser with JavaScript enabled is required for this page to operate properly.