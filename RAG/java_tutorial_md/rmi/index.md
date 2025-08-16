[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../search.html)

[Home Page](../index.html)

[« Previous](../index.html)
•
[Trail](./TOC.html)
•
[Next »](overview.html)

# Trail: RMI

The Java Remote Method Invocation (RMI) system allows an object running
in one Java virtual machine to invoke methods on an object running
in another Java virtual machine. RMI provides for remote communication between
programs written in the Java programming language.

---

**Note:** If you are connecting to an existing IDL program,
you should use Java IDL rather than RMI.

---

This trail provides a brief overview of the RMI system and then walks
through a complete client/server example that uses RMI's unique
capabilities to load and to execute user-defined tasks at runtime. The
server in the example implements a generic compute engine, which the
client uses to compute the value of
![the pi symbol](../figures/rmi/pi.gif ).

[![](../images/coreIcon.gif)
**An Overview of RMI Applications**](overview.html)
describes the RMI system and lists its advantages. Additionally, this
section provides a description of a typical RMI application, composed of
a server and a client, and introduces important terms.

[![](../images/coreIcon.gif)
**Writing an RMI Server**](server.html)
walks through the code for the compute engine server. This section will
teach you how to design and to implement an RMI server.

[![](../images/coreIcon.gif)
**Creating A Client Program**](client.html)
takes a look at one possible compute engine client and uses it to
illustrate the important features of an RMI client.

[![](../images/coreIcon.gif)
**Compiling and Running the Example**](example.html)
shows you how to compile and to run both the compute engine server and
its client.

[« Previous](../index.html)
•
[TOC](./TOC.html)
•
[Next »](overview.html)

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
  
**Next page:** An Overview of RMI Applications




A browser with JavaScript enabled is required for this page to operate properly.