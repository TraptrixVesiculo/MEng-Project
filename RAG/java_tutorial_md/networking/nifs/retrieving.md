[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Custom Networking
  
**Lesson:** Programmatic Access to Network Parameters

[Programmatic Access to Network Parameters](index.html)

[What Is a Network Interface?](definition.html)

Retrieving Network Interfaces

[Listing Network Interface Addresses](listing.html)

[Network Interface Parameters](parameters.html)

[Home Page](../../index.html)
>
[Custom Networking](../index.html)
>
[Programmatic Access to Network Parameters](index.html)

[« Previous](definition.html) • [Trail](../TOC.html) • [Next »](listing.html)

# Retrieving Network Interfaces

The `NetworkInterface` class has no public constructor. Therefore,
you cannot just create a new instance of this class with the `new`
operator. Instead, the following static methods are
available so that you can retrieve the interface details from the system:
`getByInetAddress()`, `getByName()`, and
`getNetworkInterfaces()`. The first two methods are
used when you already know the IP address or the name of the
particular interface. The third method, `getNetworkInterfaces()`
returns the complete list of interfaces on the machine.

Network interfaces can be hierarchically organized.
The `NetworkInterface` class includes two methods,
`getParent()` and `getSubInterfaces()`, that are
pertinent to
a network interface hierarchy. The `getParent()` method returns
the parent `NetworkInterface` of an interface. If a network
interface is a subinterface, `getParent()` returns a non-null
value. The `getSubInterfaces()` method returns all the
subinterfaces of a network interface.

The following example program lists the name of all the network interfaces and
subinterfaces (if any exist) on a machine.

```


import java.io.*;
import java.net.*;
import java.util.*;
import static java.lang.System.out;

public class ListNIFs 
{
    public static void main(String args[]) throws SocketException {
        Enumeration<NetworkInterface> nets = NetworkInterface.getNetworkInterfaces();
        
        for (NetworkInterface netIf : Collections.list(nets)) {
            out.printf("Display name: %s\n", netIf.getDisplayName());
            out.printf("Name: %s\n", netIf.getName());
            displaySubInterfaces(netIf);
            out.printf("\n");
        }
    }

    static void displaySubInterfaces(NetworkInterface netIf) throws SocketException {
        Enumeration<NetworkInterface> subIfs = netIf.getSubInterfaces();
        
        for (NetworkInterface subIf : Collections.list(subIfs)) {
            out.printf("\tSub Interface Display name: %s\n", subIf.getDisplayName());
            out.printf("\tSub Interface Name: %s\n", subIf.getName());
        }
     }
}  

```

The following is sample output from the example program:

```

Display name: bge0
Name: bge0
    Sub Interface Display name: bge0:3
    Sub Interface Name: bge0:3
    Sub Interface Display name: bge0:2
    Sub Interface Name: bge0:2
    Sub Interface Display name: bge0:1
    Sub Interface Name: bge0:1

Display name: lo0
Name: lo0

```

[« Previous](definition.html)
•
[Trail](../TOC.html)
•
[Next »](listing.html)

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

**Previous page:** What Is a Network Interface?
  
**Next page:** Listing Network Interface Addresses




A browser with JavaScript enabled is required for this page to operate properly.