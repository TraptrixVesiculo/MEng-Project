[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Sockets Direct Protocol
  
**Lesson:** Understanding the Sockets Direct Protocol

[Understanding the Sockets Direct Protocol](index.html)

Overview

[Creating an SDP Configuration File](file.html)

[Enabling the SDP Protocol](enable.html)

[Debugging SDP](debug.html)

[Technical Issues with SDP](issues.html)

[Solaris Support](solaris.html)

[Supported Java APIs](supported.html)

[For More Information](info.html)

[Home Page](../../index.html)
>
[Sockets Direct Protocol](../index.html)
>
[Understanding the Sockets Direct Protocol](index.html)

[« Previous](index.html) • [Trail](../TOC.html) • [Next »](file.html)

# Overview

SDP support is essentially a TCP bypass technology.

When SDP is enabled and an application attempts to open a TCP connection,
the TCP mechanism is bypassed and communication goes directly to the
IB network. For example, when your application attempts to bind to a
TCP address, the underlying software will decide,
based on information in the configuration file,
if it should be rebound to an SDP protocol.
This process can happen during the binding process or the
connecting process (but happens only once for each socket).

There are no API changes required in your code to take advantage of the
SDP protocol: the implementation is transparent and is supported by the
classic networking (`java.net`) and the New I/O
(`java.nio.channels`)
packages. See the
[Supported Java APIs](supported.html) section for a list of classes that support the SDP protocol.

SDP support is disabled by default. The steps to enable SDP support are:

* Create an SDP configuration file.* Set the system property that specifies the location of the configuration file.

[« Previous](index.html)
•
[Trail](../TOC.html)
•
[Next »](file.html)

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

**Previous page:** Understanding the Sockets Direct Protocol
  
**Next page:** Creating an SDP Configuration File




A browser with JavaScript enabled is required for this page to operate properly.