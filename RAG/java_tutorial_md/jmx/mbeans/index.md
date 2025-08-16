[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

Introducing MBeans

[Standard MBeans](standard.html)

[MXBeans](mxbeans.html)

**Trail:** Java Management Extensions (JMX)

[Home Page](../../index.html)
>
[Java Management Extensions (JMX)](../index.html)

[« Previous](../overview/index.html) • [Trail](../TOC.html) • [Next »](standard.html)

# Lesson: Introducing MBeans

This lesson introduces the fundamental concept of the JMX API, namely managed beans, or *MBeans*.

An MBean is a managed Java object, similar to a JavaBeans component, that follows the design patterns set forth in the JMX specification. An MBean can represent a device, an application, or any resource that needs to be managed. MBeans expose a management interface that consists of the following:

* A set of readable or writable attributes, or both.
* A set of invokable operations.
* A self-description.

The management interface does not change throughout the life of an MBean instance. MBeans can also emit notifications when certain predefined events occur.

The JMX specification defines five types of MBean:

* Standard MBeans
* Dynamic MBeans
* Open MBeans
* Model MBeans
* MXBeans

The examples in this trail demonstrate only the simplest types of MBean, namely standard MBeans and MXBeans.

[« Previous](../overview/index.html)
•
[Trail](../TOC.html)
•
[Next »](standard.html)

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
  
**Next page:** Standard MBeans




A browser with JavaScript enabled is required for this page to operate properly.