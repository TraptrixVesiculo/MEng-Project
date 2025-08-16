[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Custom Networking
  
**Lesson:** All About Datagrams

[All About Datagrams](index.html)

What Is a Datagram?

[Writing a Datagram Client and Server](clientServer.html)

[Broadcasting to Multiple Recipients](broadcasting.html)

[Home Page](../../index.html)
>
[Custom Networking](../index.html)
>
[All About Datagrams](index.html)

[« Previous](index.html) • [Trail](../TOC.html) • [Next »](clientServer.html)

# What Is a Datagram?

Clients and servers that communicate via a reliable channel, such as a
TCP socket, have a dedicated point-to-point channel between
themselves, or at least the illusion of one. To communicate, they
establish a connection, transmit the data, and then close the
connection. All data sent over the channel is received in the same
order in which it was sent. This is guaranteed by the channel.

In contrast, applications that communicate via datagrams send and
receive completely independent packets of information. These clients
and servers do not have and do not need a dedicated point-to-point
channel. The delivery of datagrams to their destinations is not
guaranteed. Nor is the order of their arrival.

---

**Definition:**  A *datagram* is an independent,
self-contained message sent over the network whose arrival, arrival
time, and content are not guaranteed.

---

The `java.net` package contains three classes
to help you write Java programs that use datagrams
to send and receive packets over the network:
[`DatagramSocket`](http://download.oracle.com/javase/7/docs/api/java/net/DatagramSocket.html),
[`DatagramPacket`](http://download.oracle.com/javase/7/docs/api/java/net/DatagramPacket.html), and
[`MulticastSocket`](http://download.oracle.com/javase/7/docs/api/java/net/MulticastSocket.html)An application can send and receive `DatagramPacket`s
through a `DatagramSocket`.
In addition, `DatagramPacket`s can be broadcast
to multiple recipients all listening to a `MulticastSocket`.

[« Previous](index.html)
•
[Trail](../TOC.html)
•
[Next »](clientServer.html)

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

**Previous page:** All About Datagrams
  
**Next page:** Writing a Datagram Client and Server




A browser with JavaScript enabled is required for this page to operate properly.