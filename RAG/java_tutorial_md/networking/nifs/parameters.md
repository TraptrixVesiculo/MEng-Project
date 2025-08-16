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

[Listing Network Interface Addresses](listing.html)

Network Interface Parameters

[Home Page](../../index.html)
>
[Custom Networking](../index.html)
>
[Programmatic Access to Network Parameters](index.html)

[« Previous](listing.html) • [Trail](../TOC.html) • [Next »](../cookies/index.html)

# Network Interface Parameters

You can access network parameters about a network interface beyond the
name and IP addresses assigned to it

You can discover if a network interface is “up” (that is,
running) with the `isUP()` method. The following methods
indicate the network interface type:

* `isLoopback()` indicates if the network interface is a loopback interface.
* `isPointToPoint()` indicates if the interface is a point-to-point interface.
* `isVirtual()` indicates if the interface is a virtual interface.

The `supportsMulticast()` method indicates whether the network interface supports multicasting.
The `getHardwareAddress()` method returns the network interface's
physical hardware address, usually called MAC address, when it is available. The
`getMTU()` method returns the Maximum Transmission Unit (MTU), which is
the largest packet size.

The following example expands on the example in
[Listing Network Interface Addresses](listing.html) by adding the additional network parameters described on this page:

```


import java.io.*;
import java.net.*;
import java.util.*;
import static java.lang.System.out;

public class ListNetsEx
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
       
        out.printf("Up? %s\n", netint.isUp());
        out.printf("Loopback? %s\n", netint.isLoopback());
        out.printf("PointToPoint? %s\n", netint.isPointToPoint());
        out.printf("Supports multicast? %s\n", netint.supportsMulticast());
        out.printf("Virtual? %s\n", netint.isVirtual());
        out.printf("Hardware address: %s\n",
                    Arrays.toString(netint.getHardwareAddress()));
        out.printf("MTU: %s\n", netint.getMTU());
        
        out.printf("\n");

     }
}  

```

The following is sample output from the example program:

```

Display name: bge0
Name: bge0
InetAddress: /fe80:0:0:0:203:baff:fef2:e99d%2
InetAddress: /129.156.225.59
Up? true
Loopback? false
PointToPoint? false
Supports multicast? false
Virtual? false
Hardware address: [0, 3, 4, 5, 6, 7]
MTU: 1500

Display name: lo0
Name: lo0
InetAddress: /0:0:0:0:0:0:0:1%1
InetAddress: /127.0.0.1
Up? true
Loopback? true
PointToPoint? false
Supports multicast? false
Virtual? false
Hardware address: null
MTU: 8232

```

[« Previous](listing.html)
•
[Trail](../TOC.html)
•
[Next »](../cookies/index.html)

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

**Previous page:** Listing Network Interface Addresses
  
**Next page:** Working With Cookies




A browser with JavaScript enabled is required for this page to operate properly.