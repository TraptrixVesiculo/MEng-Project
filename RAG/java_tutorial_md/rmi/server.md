[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** RMI

[An Overview of RMI Applications](overview.html)

Writing an RMI Server

[Designing a Remote Interface](designing.html)

[Implementing a Remote Interface](implementing.html)

[Creating a Client Program](client.html)

[Compiling and Running the Example](example.html)

[Compiling the Example Programs](compiling.html)

[Running the Example Programs](running.html)

[Home Page](../index.html)
>
[RMI](./index.html)

[« Previous](overview.html) • [Trail](./TOC.html) • [Next »](designing.html)

# Writing an RMI Server

The compute engine server accepts tasks from clients, runs the tasks,
and returns any results. The server code consists of an interface and a
class. The interface defines the methods that can
be invoked from the client. Essentially, the interface defines the
client's view of the remote object. The class provides the
implementation.

[Designing a Remote Interface](designing.html)
> This section explains the `Compute` interface, which
> provides the connection between the client and the server. You will
> also learn about the RMI API, which supports this communication.

[Implementing a Remote Interface](implementing.html)
> This section explores the class that implements the
> `Compute` interface, thereby implementing a remote object.
> This class also provides the rest of the code that makes up the server
> program, including a `main` method that creates an instance of the
> remote object, registers it with the RMI registry, and sets up a
> security manager.

[« Previous](overview.html)
•
[Trail](./TOC.html)
•
[Next »](designing.html)

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

**Previous page:** An Overview of RMI Applications
  
**Next page:** Designing a Remote Interface




A browser with JavaScript enabled is required for this page to operate properly.