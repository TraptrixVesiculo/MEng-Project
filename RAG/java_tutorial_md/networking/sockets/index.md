[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

All About Sockets

[What Is a Socket?](definition.html)

[Reading from and Writing to a Socket](readingWriting.html)

[Writing the Server Side of a Socket](clientServer.html)

**Trail:** Custom Networking

[Home Page](../../index.html)
>
[Custom Networking](../index.html)

[« Previous](../urls/index.html) • [Trail](../TOC.html) • [Next »](definition.html)

# Lesson: All About Sockets

`URL`s and `URLConnection`s provide
a relatively high-level mechanism for
accessing resources on the Internet. Sometimes your programs require
lower-level network communication, for example, when you want to write
a client-server application.

In client-server applications, the server provides some service,
such as processing database queries or sending out current stock prices.
The client uses the service provided by the server, either displaying
database query results to the user or making stock purchase
recommendations to an investor. The communication that occurs between
the client and the server must be reliable. That is, no data can be
dropped and it must arrive on the client side in the same order in
which the server sent it.

TCP provides a reliable, point-to-point communication channel that
client-server applications on the Internet use to communicate with each
other. To communicate over TCP, a client program and a server program
establish a connection to one another. Each program binds a socket to
its end of the connection. To communicate, the client and the server
each reads from and writes to the socket bound to the connection.

## [What Is a Socket?](definition.html)

A socket is one end-point of a two-way communication link between two
programs running on the network. Socket classes are used to represent the
connection between a client program and a server program. The java.net
package provides two classes--Socket and ServerSocket--that implement the
client side of the connection and the server side of the connection,
respectively.

## [Reading from and Writing to a Socket](readingWriting.html)

This page contains a small example that illustrates how a client program
can read from and write to a socket.

## [Writing a Client/Server Pair](clientServer.html)

The previous page showed an example of how to write a client program
that interacts with an existing server via a Socket object. This
page shows you how to write a program that implements the other
side of the connection--a server program.

[« Previous](../urls/index.html)
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
  
**Next page:** What Is a Socket?




A browser with JavaScript enabled is required for this page to operate properly.