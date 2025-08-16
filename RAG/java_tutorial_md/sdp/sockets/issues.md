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

[Enabling the SDP Protocol](enable.html)

[Debugging SDP](debug.html)

Technical Issues with SDP

[Solaris Support](solaris.html)

[Supported Java APIs](supported.html)

[For More Information](info.html)

[Home Page](../../index.html)
>
[Sockets Direct Protocol](../index.html)
>
[Understanding the Sockets Direct Protocol](index.html)

[« Previous](debug.html) • [Trail](../TOC.html) • [Next »](solaris.html)

# Technical Issues with SDP

* IPv4 and IPv6 incompatibility

  Internet Protocol version 4 (IPv4) has long been the industry
  standard version of the Internet Protocol (IP) for delivering
  data over the Internet. Internet Protocol version 6 (IPv6)
  is the next generation Internet layer protocol.
  Both versions of IP are in use today.

  IPv4 addresses are 32-bits long, written in decimal format,
  and separated by periods.
  IPv6 addresses are 128-bits long, written in hexadecimal format,
  and separated by colons.
  IPv4 addresses cannot be used as is in IPv6, but IPv6 does support
  a special class of addresses:
  the IPv4-mapped address. In an IPv4-mapped address,
  the first 80 bits are set to zero, the next 16 bits are set to 1,
  and the last 32 bits represent the IPv4 address.

  For example, here is the same IP address expressed in both formats:

  ```

  IPv4 address                  IPv4-mapped address (for use in IPv6)
  192.168.0.1                   ::ffff:192.168.0.1

  ```

  By default, if IPv6 is enabled on any of the IB adaptors,
  the Java platform uses IPv6. However, IPv4-mapped addresses are not currently
  available in the Solaris OS (see RFE #6622184). For this reason,
  if you want to use the IPv4 address format, you must specify the
  `java.net.preferIPv4Stack` property, as shown in this example:

  ```

  % java -Dcom.sun.sdp.conf=sdp.conf -Djava.net.preferIPv4Stack=true  MyApplication

  ```

  * Bugs

    A few bugs were found in the early InfiniBand implementation.
    These bugs are fixed in the Solaris 10 10/09 release.
    Make sure that you are using at least this release.

[« Previous](debug.html)
•
[Trail](../TOC.html)
•
[Next »](solaris.html)

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

**Previous page:** Debugging SDP
  
**Next page:** Solaris Support




A browser with JavaScript enabled is required for this page to operate properly.