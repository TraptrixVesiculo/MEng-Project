[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Custom Networking
  
**Lesson:** All About Sockets

[All About Sockets](index.html)

[What Is a Socket?](definition.html)

Reading from and Writing to a Socket

[Writing the Server Side of a Socket](clientServer.html)

[Home Page](../../index.html)
>
[Custom Networking](../index.html)
>
[All About Sockets](index.html)

[« Previous](definition.html) • [Trail](../TOC.html) • [Next »](clientServer.html)

# Reading from and Writing to a Socket

Let's look at a simple example that illustrates how a program can
establish a connection to a server program using the `Socket` class and
then, how the client can send data to and receive data from the server
through the socket.

The example program implements a client, `EchoClient`, that
connects to the Echo server. The Echo server simply receives data from
its client and echoes it back. The Echo server is a well-known service
that clients can rendezvous with on port 7.

`EchoClient` creates a socket thereby getting a connection
to the Echo server. It reads input from the user on the standard input
stream, and then forwards that text to the Echo server by writing the
text to the socket. The server echoes the input back through the socket
to the client. The client program reads and displays the data passed
back to it from the server:

```


import java.io.*;
import java.net.*;

public class EchoClient {
    public static void main(String[] args) throws IOException {

        Socket echoSocket = null;
        PrintWriter out = null;
        BufferedReader in = null;

        try {
            echoSocket = new Socket("taranis", 7);
            out = new PrintWriter(echoSocket.getOutputStream(), true);
            in = new BufferedReader(new InputStreamReader(
                                        echoSocket.getInputStream()));
        } catch (UnknownHostException e) {
            System.err.println("Don't know about host: taranis.");
            System.exit(1);
        } catch (IOException e) {
            System.err.println("Couldn't get I/O for "
                               + "the connection to: taranis.");
            System.exit(1);
        }

	BufferedReader stdIn = new BufferedReader(
                                   new InputStreamReader(System.in));
	String userInput;

	while ((userInput = stdIn.readLine()) != null) {
	    out.println(userInput);
	    System.out.println("echo: " + in.readLine());
	}

	out.close();
	in.close();
	stdIn.close();
	echoSocket.close();
    }
}

```

Note that `EchoClient` both writes to and reads from its
socket, thereby sending data to and receiving data from the Echo
server.

Let's walk through the program and investigate the interesting parts.
The three statements in the `try` block
of the `main` method are critical.
These lines establish the socket connection between the client and the
server and open a `PrintWriter`
and a `BufferedReader` on the socket:

```

echoSocket = new Socket("taranis", 7);
out = new PrintWriter(echoSocket.getOutputStream(), true);
in = new BufferedReader(new InputStreamReader(
                             echoSocket.getInputStream()));

```

The first statement in this sequence creates a new `Socket`
object and names it `echoSocket`. The `Socket` constructor
used here requires the name of the machine and the port number to which
you want to connect. The example program uses the host name `taranis`.
This is the name of a hypothetical machine on our local network. When
you type in and run this program on your machine, change the host name
to the name of a machine on your network. Make sure that the name you
use is the fully qualified IP name of the machine to which you want to
connect. The second argument is the port number. Port number 7 is the
port on which the Echo server listens.

The second statement gets the socket's output stream and opens a
`PrintWriter` on it. Similarly, the third statement gets the socket's
input stream and opens a `BufferedReader` on it. The example uses readers
and writers so that it can write Unicode characters over the socket.

To send data through the socket to the server, `EchoClient`
simply needs to write to the `PrintWriter`. To get the server's response,
`EchoClient` reads from the `BufferedReader`.
The rest of the program achieves this. If you are not yet familiar with the Java
platform's I/O classes, you may wish to read
[Basic I/O](../../essential/io/index.html).

The next interesting part of the program is the `while`
loop. The loop reads a line at a time from the standard input stream
and immediately sends it to the server by writing it to the `PrintWriter`
connected to the socket:

```

String userInput;

while ((userInput = stdIn.readLine()) != null) {
    out.println(userInput);
    System.out.println("echo: " + in.readLine());
}

```

The last statement in the `while` loop reads a line of
information from the `BufferedReader` connected to the
socket. The `readLine` method waits until the server echoes
the information back to `EchoClient`. When `readline` returns,
`EchoClient` prints the information to the standard output.

The `while` loop continues until the user types an end-of-input
character. That is, `EchoClient` reads input from the user,
sends it to the Echo server, gets a response from the server, and
displays it, until it reaches the end-of-input. The `while` loop then
terminates and the program continues, executing the next four lines of
code:

```

out.close();
in.close();
stdIn.close();
echoSocket.close();

```

These lines of code fall into the category of housekeeping. A
well-behaved program always cleans up after itself, and this program is
well-behaved. These statements close the readers and writers connected
to the socket and to the standard input stream, and close the socket
connection to the server. The order here is important. You should close
any streams connected to a socket before you close the socket itself.

This client program is straightforward and simple because the Echo
server implements a simple protocol. The client sends text to the
server, and the server echoes it back. When your client programs are
talking to a more complicated server such as an HTTP server, your
client program will also be more complicated. However, the basics are
much the same as they are in this program:

1. Open a socket.- Open an input stream and output stream to the socket.- Read from and write to the stream according to the server's protocol.- Close the streams.- Close the socket.

Only step 3 differs from client to client, depending on the server.
The other steps remain largely the same.

[« Previous](definition.html)
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

**Previous page:** What Is a Socket?
  
**Next page:** Writing the Server Side of a Socket




A browser with JavaScript enabled is required for this page to operate properly.