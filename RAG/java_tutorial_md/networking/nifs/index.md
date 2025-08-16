[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

Programmatic Access to Network Parameters

[What Is a Network Interface?](definition.html)

[Retrieving Network Interfaces](retrieving.html)

[Listing Network Interface Addresses](listing.html)

[Network Interface Parameters](parameters.html)

**Trail:** Custom Networking

[Home Page](../../index.html)
>
[Custom Networking](../index.html)

[« Previous](../datagrams/index.html) • [Trail](../TOC.html) • [Next »](definition.html)

# Lesson: Programmatic Access to Network Parameters

Systems often run with
multiple active network connections, such as wired Ethernet,
`802.11 b/g` (wireless), and bluetooth. Some applications might
need to access this information to perform the particular network
activity on a specific connection.

The
[`java.net.NetworkInterface`](http://download.oracle.com/javase/7/docs/api/java/net/NetworkInterface.html) class provides access to this information.

This lesson guides you through some of the more common uses of
this class and provides examples that list all the network interfaces
on a machine as well as their IP addresses and status.

## [What Is a Network Interface?](definition.html)

This page describes a network interface and explains why you might want to use it.

## [Retrieving Network Interfaces](retrieving.html)

This page contains an example that illustrates how a client program
can retrieve all the network interfaces on a machine.

## [Listing Network Interface Addresses](listing.html)

This page shows you how to list the IP addresses assigned to all the
network interfaces on a machine.

## [Network Interface Parameters](parameters.html)

This page shows you how to determine whether a network interface is
running or if the network interface is a loopback interface, a
point-to-point interface, or a virtual interface. You can also learn
how to determine if the interface supports multicasting.

[« Previous](../datagrams/index.html)
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
  
**Next page:** What Is a Network Interface?




A browser with JavaScript enabled is required for this page to operate properly.