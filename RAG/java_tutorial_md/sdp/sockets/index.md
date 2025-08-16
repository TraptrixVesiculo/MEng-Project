[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

Understanding the Sockets Direct Protocol

[Overview](overview.html)

[Creating an SDP Configuration File](file.html)

[Enabling the SDP Protocol](enable.html)

[Debugging SDP](debug.html)

[Technical Issues with SDP](issues.html)

[Solaris Support](solaris.html)

[Supported Java APIs](supported.html)

[For More Information](info.html)

**Trail:** Sockets Direct Protocol

[Home Page](../../index.html)
>
[Sockets Direct Protocol](../index.html)

[« Previous](../index.html) • [Trail](../TOC.html) • [Next »](overview.html)

# Lesson: Understanding the Sockets Direct Protocol

---

 **This section was updated to reflect features and conventions of the upcoming Java SE 7 release. You can download the current [JDK7 snapshot](http://download.java.net/jdk7/binaries/) from `java.net`.** 

---

For high performance computing environments,
the capacity to move data across a network quickly and efficiently is a
requirement.
Such networks are typically described as requiring high throughput and
low latency. *High throughput* refers to an environment that can
deliver a large amount of processing capacity over a long period of time.
*Low latency* refers to the minimal delay between processing input and
providing output, such as you would expect in a real-time application.

In these environments,
conventional networking using socket streams can create bottlenecks when it
comes to moving data. Introduced in 1999 by the
[InfiniBand Trade Association](http://www.infinibandta.org/),
InfiniBand (IB) was created to address the need for high performance
computing. One of the most important features of IB is Remote Direct
Memory Access (RDMA). RDMA enables moving data directly from the memory
of one computer to another computer,
bypassing the operating system of both computers and
resulting in significant performance gains.

The Sockets Direct Protocol (SDP) is a networking protocol developed to
support stream connections over InfiniBand fabric.
SDP support was introduced to
Java Platform, Standard Edition ("Java SE Platform")
in Java SE 7 for applications deployed in
the Solaris Operating System ("Solaris OS").
The Solaris OS has supported SDP and InfiniBand since Solaris 10 5/08.

[« Previous](../index.html)
•
[Trail](../TOC.html)
•
[Next »](overview.html)

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
  
**Next page:** Overview




A browser with JavaScript enabled is required for this page to operate properly.