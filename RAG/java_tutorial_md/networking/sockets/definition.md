[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Custom Networking
  
**Lesson:** All About Sockets

[All About Sockets](index.html)

What Is a Socket?

[Reading from and Writing to a Socket](readingWriting.html)

[Writing the Server Side of a Socket](clientServer.html)

[Home Page](../../index.html)
>
[Custom Networking](../index.html)
>
[All About Sockets](index.html)

[« Previous](index.html) • [Trail](../TOC.html) • [Next »](readingWriting.html)

# What Is a Socket?

Normally, a server runs on a specific computer and has a socket that is
bound to a specific port number. The server just waits, listening to
the socket for a client to make a connection request.

On the client-side: The client knows the hostname of the machine on
which the server is running and the port number on which the server is
listening. To make a connection request, the client tries to rendezvous
with the server on the server's machine and port. The client also needs to
identify itself to the server so it binds to a local port number that it will
use during this connection. This is usually assigned by the system.

![A client's connection request](../../figures/networking/5connect.gif)

If everything goes well, the server accepts the connection. Upon
acceptance, the server gets a new socket bound to the same local
port and also has its remote endpoint set to the address and port
of the client. It needs a new socket so that
it can continue to listen to the original socket for connection
requests while tending to the needs of the connected client.

![The connection is made](../../figures/networking/6connect.gif)

On the client side, if the connection is accepted, a socket is
successfully created and the client can use the socket to communicate
with the server.

The client and server can now communicate by writing to or reading from
their sockets.

---

**Definition:**  A *socket* is one endpoint of a two-way
communication link between two programs running on the network. A
socket is bound to a port number so that the TCP layer can identify the
application that data is destined to be sent.

---

An endpoint is a combination of an IP address and a port number. Every TCP
connection can be uniquely identified by its two endpoints. That way you can have
multiple connections between your host and the server.

The `java.net` package in the Java platform provides a
class, `Socket`, that implements one side of a two-way
connection between your Java program and another program on the
network. The `Socket` class sits on top of a
platform-dependent implementation, hiding the details of any particular
system from your Java program. By using the
`java.net.Socket` class instead of relying on native code,
your Java programs can communicate over the network in a
platform-independent fashion.

Additionally, `java.net` includes the
`ServerSocket` class, which implements a socket that servers
can use to listen for and accept connections to clients. This lesson
shows you how to use the `Socket` and
`ServerSocket` classes.

If you are trying to connect to the Web, the `URL` class and related
classes (`URLConnection`, `URLEncoder`)
are probably more appropriate than
the socket classes. In fact, URLs are a relatively high-level
connection to the Web and use sockets as part of the underlying
implementation. See
[Working with URLs](../urls/index.html)
for information about
connecting to the Web via URLs.

[« Previous](index.html)
•
[Trail](../TOC.html)
•
[Next »](readingWriting.html)

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

**Previous page:** All About Sockets
  
**Next page:** Reading from and Writing to a Socket




A browser with JavaScript enabled is required for this page to operate properly.