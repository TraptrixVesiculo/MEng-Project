[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

Overview of the JMX Technology

[Why Use the JMX Technology?](why.html)

[Architecture of the JMX Technology](architecture.html)

[Monitoring and Management of the Java Virtual Machine](javavm.html)

**Trail:** Java Management Extensions (JMX)

[Home Page](../../index.html)
>
[Java Management Extensions (JMX)](../index.html)

[« Previous](../index.html) • [Trail](../TOC.html) • [Next »](why.html)

# Lesson: Overview of the JMX Technology

The Java Management Extensions (JMX) technology is a standard part of the Java Platform, Standard Edition (Java SE platform). The JMX technology was added to the platform in the Java 2 Platform, Standard Edition (J2SE) 5.0 release.

The JMX technology provides a simple, standard way of managing resources such as applications, devices, and services. Because the JMX technology is dynamic, you can use it to monitor and manage resources as they are created, installed and implemented. You can also use the JMX technology to monitor and manage the Java Virtual Machine (Java VM).

The JMX specification defines the architecture, design patterns, APIs, and services in the Java programming language for management and monitoring of applications and networks.

Using the JMX technology, a given resource is instrumented by one or more Java objects known as *Managed Beans*, or *MBeans*. These MBeans are registered in a core-managed object server, known as an *MBean server*. The MBean server acts as a management agent and can run on most devices that have been enabled for the Java programming language.

The specifications define JMX agents that you use to manage any resources that have been correctly configured for management. A JMX agent consists of an MBean server, in which MBeans are registered, and a set of services for handling the MBeans. In this way, JMX agents directly control resources and make them available to remote management applications.

The way in which resources are instrumented is completely independent from the management infrastructure. Resources can therefore be rendered manageable regardless of how their management applications are implemented.

The JMX technology defines standard connectors (known as JMX connectors) that enable you to access JMX agents from remote management applications. JMX connectors using different protocols provide the same management interface. Consequently, a management application can manage resources transparently, regardless of the communication protocol used. JMX agents can also be used by systems or applications that are not compliant with the JMX specification, as long as those systems or applications support JMX agents.

[« Previous](../index.html)
•
[Trail](../TOC.html)
•
[Next »](why.html)

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
  
**Next page:** Why Use the JMX Technology?




A browser with JavaScript enabled is required for this page to operate properly.