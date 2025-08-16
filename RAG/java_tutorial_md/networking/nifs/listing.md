[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Custom Networking
  
**Lesson:** Programmatic Access to Network Parameters

[Programmatic Access to Network Parameters](index.html)

[What Is a Network Interface?](definition.html)

[Retrieving Network Interfaces](retrieving.html)

Listing Network Interface Addresses

[Network Interface Parameters](parameters.html)

[Home Page](../../index.html)
>
[Custom Networking](../index.html)
>
[Programmatic Access to Network Parameters](index.html)

[« Previous](retrieving.html) • [Trail](../TOC.html) • [Next »](parameters.html)

# Listing Network Interface Addresses

One of the most useful pieces of information you can get from a
network interface is the list of IP addresses that are assigned to it.
You can obtain this information from a `NetworkInterface`
instance by using one of two methods. The first method,
`getInetAddresses()`, returns an `Enumeration` of
`InetAddress`. The other method,
`getInterfaceAddresses()`, returns a list of
[`java.net.InterfaceAddress`](http://download.oracle.com/javase/7/docs/api/java/net/InterfaceAddress.html) instances. This method is used when you need more
information about an interface address beyond its IP address. For
example, you might need additional information about the subnet mask and
broadcast address when the address is an IPv4 address, and
a network prefix length in the case of an IPv6 address.

The following example program lists all the network interfaces and their addresses
on a machine:

```


import java.io.*;
import java.net.*;
import java.util.*;
import static java.lang.System.out;

public class ListNets 
{
    public static void main(String args[]) throws SocketException {
        Enumeration<NetworkInterface> nets = NetworkInterface.getNetworkInterfaces();
        for (NetworkInterface netint : Collections.list(nets))
            displayInterfaceInformation(netint);
    }

    static void displayInterfaceInformation(NetworkInterface netint) throws SocketException {
        out.printf("Display name: %s\n", netint.getDisplayName());
        out.printf("Name: %s\n", netint.getName());
        Enumeration<InetAddress> inetAddresses = netint.getInetAddresses();
        for (InetAddress inetAddress : Collections.list(inetAddresses)) {
            out.printf("InetAddress: %s\n", inetAddress);
        }
        out.printf("\n");
     }
}  

```

The following is sample output from the example program:

```

Display name: bge0
Name: bge0
InetAddress: /fe80:0:0:0:203:baff:fef2:e99d%2
InetAddress: /121.153.225.59

Display name: lo0
Name: lo0
InetAddress: /0:0:0:0:0:0:0:1%1
InetAddress: /127.0.0.1

```

[« Previous](retrieving.html)
•
[Trail](../TOC.html)
•
[Next »](parameters.html)

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

**Previous page:** Retrieving Network Interfaces
  
**Next page:** Network Interface Parameters




A browser with JavaScript enabled is required for this page to operate properly.