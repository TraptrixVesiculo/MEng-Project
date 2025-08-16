[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../search.html)

**Trail:** Deployment

[Home Page](../index.html)
>
[Deployment](./index.html)

[« Previous](TOC.html) • [TOC](./TOC.html)

# Rich Internet Applications Decision Guide

Both applets and Java Web Start applications are considered *Rich Internet
Applications (RIAs)*.
Evaluate the following characteristics of applets and Java Web Start
applications to decide how to deploy your RIA.

## Applets

* Applets run in the context of a browser.
* Applets have access to session cookies and persistent cookies.
* Applets can interact with the web page that they are embedded in. Applets
  can traverse and manipulate the Document Object Model of the web page and interact
  with JavaScript that is in the web page. JavaScript code can access
  public methods and variables of an applet.
* Applets can be launched using Java Network Launch Protocol (JNLP). When
  launched using JNLP, unsigned applets are allowed access to persistent storage,
  download control, file I/O, and more. Applets launched using JNLP have
  capabilities that are comparable to that of a Java Web Start application.  
  Applets can also be launched without JNLP, in which case, their capabilities
  might be limited.
* Applets can request a particular version of the Java Runtime Environment software
  for execution.

## Java Web Start applications

* Java Web Start applications are launched from a web page the first time.
  Subsequently, they may be re-launched from the web page or from a desktop shortcut.
* Java Web Start applications do not run in the context of a browser. The
  applications cannot interact with HTML and JavaScript in a web page and have access to
  persistent cookies only.
* Java Web Start applications are allowed access to persistent storage, file I/O,
  and other client related services.
* Java Web Start applications can request a particular version of the Java Runtime Environment software
  for execution.

[« Previous](TOC.html)
•
[TOC](./TOC.html)


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

**Previous page:** Table of Contents




A browser with JavaScript enabled is required for this page to operate properly.