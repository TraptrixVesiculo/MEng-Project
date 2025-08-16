[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Custom Networking
  
**Lesson:** Programmatic Access to Network Parameters

[Programmatic Access to Network Parameters](index.html)

What Is a Network Interface?

[Retrieving Network Interfaces](retrieving.html)

[Listing Network Interface Addresses](listing.html)

[Network Interface Parameters](parameters.html)

[Home Page](../../index.html)
>
[Custom Networking](../index.html)
>
[Programmatic Access to Network Parameters](index.html)

[« Previous](index.html) • [Trail](../TOC.html) • [Next »](retrieving.html)

# What Is a Network Interface?

A *network interface* is the point of interconnection between a computer
and a private or public network. A network interface is generally a network
interface card (NIC), but does not have to have a physical form.
Instead, the network interface can be implemented in software. For example,
the loopback interface
(127.0.0.1 for IPv4 and ::1 for IPv6) is not a physical device but a
piece of software simulating a network interface. The loopback interface is
commonly used in test environments.

The
[`java.net.NetworkInterface`](http://download.oracle.com/javase/7/docs/api/java/net/NetworkInterface.html) class represents both types of interfaces.

NetworkInterface is useful for a multihomed system, which is a system with
multiple NICs. Using `NetworkInterface`, you can specify which
NIC to use for a particular network activity.

For example, assume you have a machine with two configured NICs,
and you want to send data to a server. You create a
socket like this:

```

  Socket soc = new java.net.Socket();
  soc.connect(new InetSocketAddress(address, port));

```

To send the data, the system determines which interface will
be used. However, if you have a preference or otherwise need to specify which
NIC to use,
you can query the system for the appropriate interfaces and find an address
on the interface you want to use. When you create the socket
and bind it to that address, the system will use the associated interface.
For example:

```

  NetworkInterface nif = NetworkInterface.getByName("bge0");
  Enumeration nifAddresses = nif.getInetAddresses();

  Socket soc = new java.net.Socket();
  soc.bind(nifAddresses.nextElement());
  soc.connect(new InetSocketAddress(address, port));

```

You can also use `NetworkInterface` to identify the local interface
on which a multicast group is to be joined. For example:

```

  NetworkInterface nif = NetworkInterface.getByName("bge0");

  MulticastSocket() ms = new MulticastSocket();
  ms.joinGroup(new InetSocketAddress(hostname, port) , nif); 

```

NetworkInterface can be used with Java APIs in many other ways beyond the
two uses described here.

[« Previous](index.html)
•
[Trail](../TOC.html)
•
[Next »](retrieving.html)

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

**Previous page:** Programmatic Access to Network Parameters
  
**Next page:** Retrieving Network Interfaces




A browser with JavaScript enabled is required for this page to operate properly.