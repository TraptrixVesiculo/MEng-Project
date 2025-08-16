[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

All About Datagrams

[What Is a Datagram?](definition.html)

[Writing a Datagram Client and Server](clientServer.html)

[Broadcasting to Multiple Recipients](broadcasting.html)

**Trail:** Custom Networking

[Home Page](../../index.html)
>
[Custom Networking](../index.html)

[« Previous](../sockets/index.html) • [Trail](../TOC.html) • [Next »](definition.html)

# Lesson: All About Datagrams

Some applications that you write to communicate over the network will
not require the reliable, point-to-point channel provided by TCP.
Rather, your applications might benefit from a mode of communication
that delivers independent packages of information whose arrival and
order of arrival are not guaranteed.

The UDP protocol provides a mode of network communication whereby
applications send packets of data, called datagrams, to one another. A
datagram is an independent, self-contained message sent over the
network whose arrival, arrival time, and content are not guaranteed.
The `DatagramPacket` and `DatagramSocket`
classes in the `java.net` package
implement system-independent datagram communication using UDP.

## [What Is a Datagram?](definition.html)

A datagram is an independent, self-contained message sent over
the network whose arrival, arrival time, and content are not
guaranteed.

## [Writing a Datagram Client and Server](clientServer.html)

This section walks you through an example that contains two Java
programs that use datagrams to communicate. The server side is a quote
server that listens to its `DatagramSocket` and sends a quotation to a
client whenever the client requests it. The client side is a simple
program that simply makes a request of the server.

## [Broadcasting to Multiple Recipients](broadcasting.html)

This section modifies the quote server so that
instead of sending a quotation to a single client upon request, the
quote server broadcasts a quote every minute to as many clients as are
listening. The client program must be modified accordingly.

---

**Note:** 
Many firewalls and routers are configured not to allow UDP packets. If
you have trouble connecting to a service outside your firewall, or if
clients have trouble connecting to your service, ask your system
administrator if UDP is permitted.

---

[« Previous](../sockets/index.html)
•
[Trail](../TOC.html)
•
[Next »](definition.html)

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
  
**Next page:** What Is a Datagram?




A browser with JavaScript enabled is required for this page to operate properly.