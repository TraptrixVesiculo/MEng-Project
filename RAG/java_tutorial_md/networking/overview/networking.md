[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Custom Networking
  
**Lesson:** Overview of Networking

[Overview of Networking](index.html)

[What You May Already Know About Networking in Java](alreadyknow.html)

Networking Basics

[Home Page](../../index.html)
>
[Custom Networking](../index.html)
>
[Overview of Networking](index.html)

[« Previous](alreadyknow.html) • [Trail](../TOC.html) • [Next »](../urls/index.html)

# Networking Basics

Computers running on the Internet communicate to each other using
either the Transmission Control Protocol (TCP) or the User Datagram
Protocol (UDP), as this diagram illustrates:

![Example of network communication.](../../figures/networking/1netw.gif)

When you write Java programs that communicate over the network, you are
programming at the application layer. Typically, you don't need to
concern yourself with the TCP and UDP layers. Instead, you can use the
classes in the `java.net` package. These classes provide
system-independent network communication. However, to decide which Java
classes your programs should use, you do need to understand how TCP and
UDP differ.

## TCP

When two applications want to communicate to each other reliably, they
establish a connection and send data back and forth over that
connection. This is analogous to making a telephone call. If you want
to speak to Aunt Beatrice in Kentucky, a connection is established when
you dial her phone number and she answers. You send data back and forth
over the connection by speaking to one another over the phone lines.
Like the phone company, TCP guarantees that data sent from one end of
the connection actually gets to the other end and in the same order it
was sent. Otherwise, an error is reported.

TCP provides a point-to-point channel for applications that require
reliable communications. The Hypertext Transfer Protocol (HTTP), File
Transfer Protocol (FTP), and Telnet are all examples of applications
that require a reliable communication channel. The order in which the
data is sent and received over the network is critical to the success
of these applications. When HTTP is used to read from a URL, the data
must be received in the order in which it was sent. Otherwise, you end
up with a jumbled HTML file, a corrupt zip file, or some other invalid
information.

---

**Definition:** 
*TCP* (*Transmission Control Protocol*)
is a connection-based protocol that
provides a reliable flow of data between two computers.

---

## UDP

The UDP protocol provides for communication that is not guaranteed
between two applications on the network. UDP is not connection-based
like TCP. Rather, it sends independent packets of data, called
*datagrams*, from one application to another. Sending datagrams is much
like sending a letter through the postal service: The order of delivery
is not important and is not guaranteed, and each message is independent
of any other.

---

**Definition:** 
*UDP* (*User Datagram Protocol*) is a protocol that sends
independent packets of data, called datagrams, from one computer to
another with no guarantees about arrival. UDP is not connection-based
like TCP.

---

For many applications, the guarantee of reliability is critical to the
success of the transfer of information from one end of the connection
to the other. However, other forms of communication don't require such
strict standards. In fact, they may be slowed down by the extra
overhead or the reliable connection may invalidate the service
altogether.

Consider, for example, a clock server that sends the current time to
its client when requested to do so. If the client misses a packet, it
doesn't really make sense to resend it because the time will be incorrect
when the client receives it on the second try. If the client makes two
requests and receives packets from the server out of order, it doesn't
really matter because the client can figure out that the packets are
out of order and make another request. The reliability of TCP is
unnecessary in this instance because it causes performance degradation
and may hinder the usefulness of the service.

Another example of a service that doesn't need the guarantee of a
reliable channel is the ping command. The purpose of the ping command
is to test the communication between two programs over the network. In
fact, ping needs to know about dropped or out-of-order packets to
determine how good or bad the connection is. A reliable channel would
invalidate this service altogether.

The UDP protocol provides for communication that is not guaranteed
between two applications on the network. UDP is not connection-based
like TCP. Rather, it sends independent packets of data from one
application to another. Sending datagrams is much like sending a letter
through the mail service: The order of delivery is not important and is
not guaranteed, and each message is independent of any others.

---

**Note:** 
Many firewalls and routers have been configured not to allow UDP
packets. If you're having trouble connecting to a service outside your
firewall, or if clients are having trouble connecting to your service,
ask your system administrator if UDP is permitted.

---

## Understanding Ports

Generally speaking, a computer has a single physical connection to the
network. All data destined for a particular computer arrives through
that connection. However, the data may be intended for different
applications running on the computer. So how does the computer know to
which application to forward the data? Through the use of *ports*.

Data transmitted over the Internet is accompanied by addressing
information that identifies the computer and the port for which it is
destined. The computer is identified by its 32-bit IP address, which IP
uses to deliver data to the right computer on the network. Ports are
identified by a 16-bit number, which TCP and UDP use to deliver the
data to the right application.

In connection-based communication such as TCP, a server application
binds a socket to a specific port number. This has the effect of
registering the server with the system to receive all data destined for
that port. A client can then rendezvous with the server at the server's
port, as illustrated here:

![A client communicating to a server through its port](../../figures/networking/2tcp.gif)

---

**Definition:** 
The TCP and UDP protocols use ports to map incoming data to a
particular process running on a computer.

---

In datagram-based communication such as UDP, the datagram packet
contains the port number of its destination and UDP routes the packet
to the appropriate application, as illustrated in this figure:

![Routing the packet to the appropriate application.](../../figures/networking/3tcpudp.gif)

Port numbers range from 0 to 65,535 because ports are represented by
16-bit numbers. The port numbers ranging from 0 - 1023 are restricted;
they are reserved for use by well-known services such as HTTP and FTP
and other system services. These ports are called *well-known ports*.
Your applications should not attempt to bind to them.

## Networking Classes in the JDK

Through the classes in `java.net`,
Java programs can use TCP or UDP to
communicate over the Internet.
The `URL`, `URLConnection`, `Socket`, and
`ServerSocket` classes all use TCP to communicate over the network.
The `DatagramPacket`, `DatagramSocket`,
and `MulticastSocket` classes are for use with UDP.

[« Previous](alreadyknow.html)
•
[Trail](../TOC.html)
•
[Next »](../urls/index.html)

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

**Previous page:** What You May Already Know About Networking in Java
  
**Next page:** Working with URLs




A browser with JavaScript enabled is required for this page to operate properly.