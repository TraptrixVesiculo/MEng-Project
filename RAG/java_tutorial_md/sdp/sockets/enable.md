[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Sockets Direct Protocol
  
**Lesson:** Understanding the Sockets Direct Protocol

[Understanding the Sockets Direct Protocol](index.html)

[Overview](overview.html)

[Creating an SDP Configuration File](file.html)

Enabling the SDP Protocol

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

[« Previous](file.html) • [Trail](../TOC.html) • [Next »](debug.html)

# Enabling the SDP Protocol

SDP support is disabled by default.
To enable SDP support, set the `com.sun.sdp.conf`
system property by providing the location of the configuration file.
The following example starts an application using a configuration
file named `sdp.conf`:

```

% java -Dcom.sun.sdp.conf=sdp.conf -Djava.net.preferIPv4Stack=true  MyApplication

```

*MyApplication* refers to the client application that is attempting to
connect to the IB adaptor.

Note that this example specifies another system property,
`java.net.preferIPv4Stack`. See the
[Issues](issues.html) section for more information about why this property is used.

[« Previous](file.html)
•
[Trail](../TOC.html)
•
[Next »](debug.html)

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

**Previous page:** Creating an SDP Configuration File
  
**Next page:** Debugging SDP




A browser with JavaScript enabled is required for this page to operate properly.