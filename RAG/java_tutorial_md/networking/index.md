[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../search.html)

[Home Page](../index.html)

[« Previous](../index.html)
•
[Trail](./TOC.html)
•
[Next »](./overview/index.html)

# Trail: Custom Networking

The Java platform is highly regarded in part because of its suitability
for writing programs that use and interact with the resources on the
Internet and the World Wide Web. In fact, Java-compatible browsers use
this ability of the Java platform to the extreme to transport and run
applets over the Internet.

This trail walks you through the complexities of writing Java
applications and applets that can be used on the Internet.

[![Trail icon](../images/networkingIcon.gif)
**Overview of Networking**](overview/index.html)
has two sections. The first describes the networking capabilities of
the Java platform that you may already be using without realizing that
you are using the network. The second provides a brief overview of
networking to familiarize you with terms and concepts that you should
understand before reading how to use URLs, sockets, and datagrams.

[![Trail icon](../images/networkingIcon.gif)
**Working With URLs**](urls/index.html)
discusses how your Java programs can use URLs to access information on
the Internet. A URL (Uniform Resource Locator) is the address of a
resource on the Internet. Your Java programs can use URLs to connect to
and retrieve information over a network. This lesson provides a more
complete definition of a URL and shows you how to create and parse a
URL, how to open a connection to a URL, and how to read from and write
to that connection.

[![Trail icon](../images/networkingIcon.gif)
**All About Sockets**](sockets/index.html)
explains how to use sockets so that your programs can communicate with
other programs on the network. A socket is one endpoint of a two-way
communication link between two programs running on the network. This
lesson shows you how a client can connect to a standard server, the
Echo server, and communicate with it via a socket. It then walks you
through the details of a complete client/server example, which shows
you how to implement both the client side and the server side of a
client/server pair.

[![Trail icon](../images/networkingIcon.gif)
**All About Datagrams**](datagrams/index.html)
takes you step by step through a simple client/server example that uses
datagrams to communicate. It then challenges you to rewrite the example
using multicast socket instead.

[![Trail icon](../images/networkingIcon.gif)
**Programmatic Access to Network Parameters**](nifs/index.html)
explains why you might want to access network interface parameters
and how to do so. It gives examples of how to list all the
IP addresses assigned to the machine as well as other useful
information such as whether the interface is running.

[![Trail icon](../images/networkingIcon.gif)
**Working With Cookies**](cookies/index.html)
discusses how cookies are used to create a session between a client
and server, and how you can take advantage of cookies in your
HTTP URL connections.

---

**Security considerations:** Note that communications over the network are subject to approval by
the current security manager.
[The Security Manager](../essential/environment/security.html) describes what a security manager is and how it impacts your applications.
For general information about the security features
provided by the JDK, refer to
[Security Features in Java SE](../security/index.html).

The example
programs in the following lessons that cover URLs, sockets, and
datagrams are standalone applications, which, by default, have no
security manager. If you convert these applications to applets, they
may be unable to communicate over the network, depending on the browser
or viewer in which they are running. See
[What Applets Can and Cannot Do](../deployment/applet/security.html) for information about the security
restrictions placed on applets.

---

[« Previous](../index.html)
•
[TOC](./TOC.html)
•
[Next »](./overview/index.html)

---

Problems with the examples? Try [Compiling and Running
the Examples: FAQs](../information/run-examples.html).
  
Complaints? Compliments? Suggestions? [Give
us your feedback](http://download.oracle.com/javase/feedback.html).

Your use of this page and all the material on pages under "The Java Tutorials" banner,
and all the material on pages under "The Java Tutorials" banner is subject to the [Java SE Tutorial Copyright
and License](../information/license.html).
Additionally, any example code contained in any of these Java
Tutorials pages is licensed under the
[Code
Sample License](http://developers.sun.com/license/berkeley_license.html).

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| |  |  | | --- | --- | | duke image | Oracle logo | | [About Oracle](http://www.oracle.com/us/corporate/index.html) | [Oracle Technology Network](http://www.oracle.com/technology/index.html) | [Terms of Service](https://www.samplecode.oracle.com/servlets/CompulsoryClickThrough?type=TermsOfService) | Copyright © 1995, 2011 Oracle and/or its affiliates. All rights reserved. |

**Previous page:** Beginning of Tutorial
  
**Next page:** Overview of Networking




A browser with JavaScript enabled is required for this page to operate properly.