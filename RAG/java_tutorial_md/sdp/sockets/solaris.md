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

[Technical Issues with SDP](issues.html)

Solaris Support

[Supported Java APIs](supported.html)

[For More Information](info.html)

[Home Page](../../index.html)
>
[Sockets Direct Protocol](../index.html)
>
[Understanding the Sockets Direct Protocol](index.html)

[« Previous](issues.html) • [Trail](../TOC.html) • [Next »](supported.html)

# Solaris Support

To test that SDP is enabled, use the `sdpadm`(1M) command:

```

% /usr/sbin/sdpadm status
SDP is Enabled

```

Other commands you might find useful are `ib`(7D),
`ibd`(7D), and `sdp`(7D).

You can use the grep command to search
the `/etc/path_to_inst` file for the string
"ibd" to view a list of IB adaptors that are supported on your network.

[« Previous](issues.html)
•
[Trail](../TOC.html)
•
[Next »](supported.html)

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

**Previous page:** Technical Issues with SDP
  
**Next page:** Supported Java APIs




A browser with JavaScript enabled is required for this page to operate properly.