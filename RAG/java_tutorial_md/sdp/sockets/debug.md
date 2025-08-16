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

Debugging SDP

[Technical Issues with SDP](issues.html)

[Solaris Support](solaris.html)

[Supported Java APIs](supported.html)

[For More Information](info.html)

[Home Page](../../index.html)
>
[Sockets Direct Protocol](../index.html)
>
[Understanding the Sockets Direct Protocol](index.html)

[« Previous](enable.html) • [Trail](../TOC.html) • [Next »](issues.html)

# Debugging SDP

You can enable debugging messages by using the
`-Dcom.sun.sdp.debug` flag.
If you specify a file, the messages will be output to that file.
Otherwise, the messages will be printed to standard output.

This first example shows sample messages printed to standard output:

```

% java -Dcom.sun.sdp.conf=sdp.conf -Dcom.sun.sdp.debug MyApplicaton
BIND to 192.168.0.1:5000 (socket converted to SDP protocol)
CONNECT to 129.156.232.160:80 (no match)
CONNECT to 192.168.0.2:80 (socket converted to SDP protocol)

```

This second example shows the output redirected to a file named `debug.log`:

```

% java -Dcom.sun.sdp.conf=sdp.conf -Dcom.sun.sdp.debug=debug.log MyApplication &
[1] 27310
% tail -f debug.log
BIND to 192.168.0.1:5000 (socket converted to SDP protocol)

```

[« Previous](enable.html)
•
[Trail](../TOC.html)
•
[Next »](issues.html)

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

**Previous page:** Enabling the SDP Protocol
  
**Next page:** Technical Issues with SDP




A browser with JavaScript enabled is required for this page to operate properly.