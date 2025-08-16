[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Custom Networking
  
**Lesson:** All About Datagrams

[All About Datagrams](index.html)

[What Is a Datagram?](definition.html)

[Writing a Datagram Client and Server](clientServer.html)

Broadcasting to Multiple Recipients

[Home Page](../../index.html)
>
[Custom Networking](../index.html)
>
[All About Datagrams](index.html)

[« Previous](clientServer.html) • [Trail](../TOC.html) • [Next »](../nifs/index.html)

# Broadcasting to Multiple Recipients

In addition to `DatagramSocket`, which lets programs send
packets to one another, java.net includes a class called
`MulticastSocket`. This kind of socket is used on the
client-side to listen for packets that the server broadcasts to
multiple clients.

Let's rewrite the quote server so that it broadcasts
`DatagramPacket`s to multiple recipients. Instead of sending
quotes to a specific client that makes a request, the new server now
needs to broadcast quotes at a regular interval. The client needs to be
modified so that it passively listens for quotes and does so on a
`MulticastSocket`.

This example is comprised of three classes which are modifications of
the three classes from the previous example:
[`MulticastServer`](examples/MulticastServer.java),
[`MulticastServerThread`](examples/MulticastServerThread.java), and
[`MulticastClient`](examples/MulticastClient.java).
This discussion highlights
the interesting parts of these classes.

Here is the new version of the server's main program.
The differences between this code and the previous version,
`QuoteServer`, are shown in bold:

```

import java.io.*;
public class MulticastServer {
    public static void main(String[] args) throws IOException {
        new MulticastServerThread().start();
    }
}

```

Basically, the server got a new name
and creates a `MulticastServerThread`
instead of a `QuoteServerThread`.
Now let's look at the `MulticastServerThread`
which contains the heart of the server. Here's its class declaration:

```

public class MulticastServerThread extends QuoteServerThread {
    ...
}

```

We've made this class a subclass of `QuoteServerThread`
so that it can use the constructor,
and inherit some member variable and the `getNextQuote` method.
Recall that `QuoteServerThread` creates a
`DatagramSocket` bound to port 4445 and opens the quote file.
The `DatagramSocket`'s port number doesn't actually matter
in this example because the client never send anything to the server.

The only method explicitly implemented in `MulticastServerThread`
is its `run` method. The differences between this `run`
method and the one in `QuoteServerThread` are shown in bold:

```

public void run() {
    while (moreQuotes) {
        try {
            byte[] buf new byte[256];
            // don't wait for request...just send a quote

            String dString = null;
            if (in == null)
                dString = new Date().toString();
            else
                dString = getNextQuote();
            buf = dString.getBytes();

            InetAddress group = InetAddress.getByName(
                                            "230.0.0.1");
            DatagramPacket packet;
            packet = new DatagramPacket(buf, buf.length, 
                                        group, 4446);
            socket.send(packet);

            try {
                sleep((long)Math.random() * FIVE_SECONDS);
            } catch (InterruptedException e) { }
        } catch (IOException e) {
            e.printStackTrace();
            moreQuotes = false;
        }
    }
    socket.close();
}

```

The interesting change is how the `DatagramPacket` is
constructed, in particular, the `InetAddress` and port used to construct
the `DatagramPacket`. Recall that the previous example
retrieved the `InetAddress` and port number from the packet sent to the
server from the client. This was because the server needed to reply
directly to the client. Now, the server needs to address multiple
clients. So this time both the `InetAddress` and the port number are
hard-coded.

The hard-coded port number is 4446 (the client must have a
`MulticastSocket` bound to this port). The hard-coded
`InetAddress` of the `DatagramPacket` is "230.0.0.1" and is a
group identifier (rather than the Internet address of the machine on
which a single client is running). This particular address was
arbitrarily chosen from the reserved for this purpose.

Created in this way, the `DatagramPacket` is destined for
all clients listening to port number 4446 who are member of the
"230.0.0.1" group.

To listen to port number 4446, the new client program just created its
`MulticastSocket` with that port number. To become a member
of the "230.0.0.1" group, the client calls the
`MulticastSocket`'s `joinGroup` method with the
`InetAddress` that identifies the group. Now, the client is set up to
receive `DatagramPacket`s destined for the port and group
specified. Here's the relevant code from the new client program (which
was also rewritten to passively receive quotes rather than actively
request them). The bold statements are the ones that interact with the
`MulticastSocket`:

```

MulticastSocket socket = new MulticastSocket(4446);
InetAddress group = InetAddress.getByName("230.0.0.1");
socket.joinGroup(group);

DatagramPacket packet;
for (int i = 0; i < 5; i++) {
    byte[] buf = new byte[256];
    packet = new DatagramPacket(buf, buf.length);
    socket.receive(packet);

    String received = new String(packet.getData());
    System.out.println("Quote of the Moment: " + received);
}
socket.leaveGroup(group);
socket.close();

```

Notice that the server uses a `DatagramSocket` to broadcast
packet received by the client over a `MulticastSocket`.
Alternatively, it could have used a `MulticastSocket`. The
socket used by the server to send the `DatagramPacket` is
not important. What's important when broadcasting packets is the
addressing information contained in the `DatagramPacket`,
and the socket used by the client to listen for it

---

**Try this:** 
Run the `MulticastServer` and several clients.
Watch how the clients all get the same quotes.

---

[« Previous](clientServer.html)
•
[Trail](../TOC.html)
•
[Next »](../nifs/index.html)

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

**Previous page:** Writing a Datagram Client and Server
  
**Next page:** Programmatic Access to Network Parameters




A browser with JavaScript enabled is required for this page to operate properly.