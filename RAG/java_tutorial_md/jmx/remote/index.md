[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

Remote Management

[Exposing a Resource for Remote Management By JConsole](jconsole.html)

[Creating a Custom JMX Client](custom.html)

**Trail:** Java Management Extensions (JMX)

[Home Page](../../index.html)
>
[Java Management Extensions (JMX)](../index.html)

[« Previous](../notifs/index.html) • [Trail](../TOC.html) • [Next »](jconsole.html)

# Lesson: Remote Management

The JMX API enables you to perform remote management of your resources by using JMX technology-based connectors (JMX connectors). A JMX connector makes an MBean server accessible to remote Java technology-based clients. The client end of a connector exports essentially the same interface as the MBean server.

A JMX connector consists of a connector client and a connector server. A *connector server* is attached to an MBean server and listens for connection requests from clients. A *connector client* is responsible for establishing a connection with the connector server. A connector client is usually in a different Java Virtual Machine (Java VM) from the connector server and is often running on a different machine. The JMX API defines a standard connection protocol based on Remote Method Invocation (RMI). This protocol enables you to connect a JMX client to an MBean in an MBean server from a remote location and perform operations on the MBean, exactly as if the operations were being performed locally.

The Java SE platform provides an out-of-the-box means to monitor applications remotely by using the JMX API's standard RMI connector. The out-of-the-box RMI connector automatically exposes applications for remote management, without requiring you to create a dedicated remote connector server yourself. The out-of-the-box remote management agent is activated by starting your Java application with the correct properties. Monitoring and management applications that are compatible with the JMX technology can then connect to these applications and monitor them remotely.

[« Previous](../notifs/index.html)
•
[Trail](../TOC.html)
•
[Next »](jconsole.html)

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

**Previous page:** Previous Lesson
  
**Next page:** Exposing a Resource for Remote Management By JConsole




A browser with JavaScript enabled is required for this page to operate properly.