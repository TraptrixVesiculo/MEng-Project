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

[Solaris Support](solaris.html)

Supported Java APIs

[For More Information](info.html)

[Home Page](../../index.html)
>
[Sockets Direct Protocol](../index.html)
>
[Understanding the Sockets Direct Protocol](index.html)

[« Previous](solaris.html) • [Trail](../TOC.html) • [Next »](info.html)

# Supported Java APIs

All of the APIs that use TCP can use SDP,
specifically including the following classes:

* `java.net` package
  + `Socket`+ `ServerSocket`* `java.nio.channels` package:
    + `SocketChannel`+ `ServerSocketChannel`+ `AsynchronousSocketChannel`+ `AsynchronousServerSocketChannel`

When SDP support is enabled, it just works without any change
to your code. Compiling is not necessary.
However, it is important to know that a socket is bound only once.
A connection is an implicit bind. So, if the socket hasn't been
previously bound and `connect` is invoked,
the binding occurs at that time.

For example, consider the following code snippet:

```

AsynchronousSocketChannel ch = AsynchronousSocketChannel.open();
ch.bind(local);
Future result = ch.connect(remote);

```

In this snippet, the asynchronous socket channel is bound to a
local TCP address when `bind` is invoked on the socket.
Then, the code attempts to connect to a remote address by using the same socket.
If the remote address uses InfiniBand, as specified in the configuration
file, the connection will not be converted to SDP because the socket was
previously bound.

[« Previous](solaris.html)
•
[Trail](../TOC.html)
•
[Next »](info.html)

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

**Previous page:** Solaris Support
  
**Next page:** For More Information




A browser with JavaScript enabled is required for this page to operate properly.