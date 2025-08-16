[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Java Naming and Directory Interface(TM).
  
**Lesson:** Advanced Topics for LDAP Users

[Advanced Topics for LDAP Users](index.html)

[LDAP v3](ldap.html)

[JNDI as an LDAP API](jndi.html)

[How LDAP Operations Map to JNDI APIs](operations.html)

[How LDAP Error Codes Map to JNDI Exceptions](exceptions.html)

[Security](security.html)

[Modes of Authenticating to LDAP](authentication.html)

[Authentication Mechanisms](auth_mechs.html)

[Anonymous](anonymous.html)

[Simple](simple.html)

[SASL](sasl.html)

[Digest-MD5](digest.html)

[SSL and Custom Sockets](ssl.html)

[More LDAP Operations](rename.html)

[LDAP Compare](compare.html)

[Search Results](result.html)

[LDAP Unsolicited Notifications](unsol.html)

Connection Management

[Creation](create.html)

[Closing](close.html)

[Pooling](pool.html)

[Configuration](config.html)

[Frequently Asked Questions](faq.html)

[Home Page](../../index.html)
>
[Java Naming and Directory Interface(TM).](../index.html)
>
[Advanced Topics for LDAP Users](index.html)

[« Previous](unsol.html) • [Trail](../TOC.html) • [Next »](create.html)

# Connection Management

JNDI provides a high-level interface for accessing naming and
directory services. The mapping between a JNDI
[`Context`](http://download.oracle.com/javase/7/docs/api/javax/naming/Context.html) instance and an underlying network connection might not be one-to-one.
The service provider is free to share and reuse connections as long
as the interface semantics are preserved.
The application developer usually does not need to know
the details of how Context instances create and use connections.
These details are useful when the developer needs to tune his program.

This lesson describes how the LDAP service provider uses connections.
It describes [when connections are created](create.html)
and how to specify special connection
parameters, such as multiple servers and connection timeouts.
This lesson also shows how to dynamically discover and
use LDAP servers in network environments that support it.

A connection that is created must eventually be closed.
This lesson contains a section that describes
[connection closures](close.html)
by the client and the server.

Finally, this lesson shows you how to use [connection
pooling](pool.html) to make applications that use many short-lived connections
more efficient.

---

**Note:** Information presented in this lesson are specific to Sun's LDAP
service provider. LDAP service providers from other vendors might
not use the same policies for managing connections.

---

[« Previous](unsol.html)
•
[Trail](../TOC.html)
•
[Next »](create.html)

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

**Previous page:** LDAP Unsolicited Notifications
  
**Next page:** Creation




A browser with JavaScript enabled is required for this page to operate properly.