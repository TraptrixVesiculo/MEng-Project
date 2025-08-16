[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** RMI
  
**Section:** Compiling and Running the Example

[An Overview of RMI Applications](overview.html)

[Writing an RMI Server](server.html)

[Designing a Remote Interface](designing.html)

[Implementing a Remote Interface](implementing.html)

[Creating a Client Program](client.html)

[Compiling and Running the Example](example.html)

Compiling the Example Programs

[Running the Example Programs](running.html)

[Home Page](../index.html)
>
[RMI](./index.html)

[« Previous](example.html) • [Trail](./TOC.html) • [Next »](running.html)

# Compiling the Example Programs

In a real-world scenario in which a service such as the compute engine is
deployed, a developer would likely create a Java Archive (JAR) file
that contains the `Compute` and `Task` interfaces
for server classes to implement and client programs to use. Next, a
developer, perhaps the same developer of the interface JAR file, would
write an implementation of the `Compute` interface and
deploy that service on a machine available to clients. Developers of
client programs can use the `Compute` and the
`Task` interfaces, contained in the JAR file, and
independently develop a task and client program that uses a
`Compute` service.

In this section, you learn how to set up the JAR file, server classes,
and client classes. You will see that the client's `Pi`
class will be downloaded to the server at runtime. Also, the
`Compute` and `Task` interfaces will be
downloaded from the server to the registry at runtime.

This example separates the interfaces, remote object implementation, and
client code into three packages:

* `compute` –
  [`Compute`](examples/compute/Compute.java)
  and
  [`Task`](examples/compute/Task.java)
  interfaces* `engine` –
    [`ComputeEngine`](examples/engine/ComputeEngine.java)
    implementation class* `client` –
      [`ComputePi`](examples/client/ComputePi.java) client code and
      [`Pi`](examples/client/Pi.java) task implementation

First, you need to build the interface JAR file to provide to server
and client developers.

### Building a JAR File of Interface Classes

> First, you need to compile the interface source files in the
> `compute` package and then build a JAR file that contains
> their class files. Assume that user `waldo` has written
> these interfaces and placed the source files in the directory
> `c:\home\waldo\src\compute` on Windows or the directory
> `/home/waldo/src/compute` on Solaris OS or Linux.
> Given these paths, you can use the following commands to compile the
> interfaces and create the JAR file:
>
> > ---
> >
> > **Microsoft Windows**:
> >
> > ```
> >
> > cd c:\home\waldo\src
> > javac compute\Compute.java compute\Task.java
> > jar cvf compute.jar compute\*.class
> >
> > ```
> >
> > **Solaris OS or Linux**:
> >
> > ```
> >
> > cd /home/waldo/src
> > javac compute/Compute.java compute/Task.java
> > jar cvf compute.jar compute/*.class
> >
> > ```
> >
> > ---

The `jar` command displays the following output due to the
`-v` option:

```

added manifest
adding: compute/Compute.class(in = 307) (out= 201)(deflated 34%)
adding: compute/Task.class(in = 217) (out= 149)(deflated 31%)

```

Now, you can distribute the `compute.jar` file to developers
of server and client applications so that they can make use of the
interfaces.

After you build either server-side or client-side classes with the
`javac` compiler, if any of those classes will need to be
dynamically downloaded by other Java virtual machines, you must
ensure that their class files are placed in a network-accessible
location. In this example, for Solaris OS or Linux this location is
`/home/user/public_html/classes` because many web servers
allow the accessing of a user's `public_html` directory through an HTTP
URL constructed as `http://host/~user/`. If your web server
does not support this convention, you could use a different location in
the web server's hierarchy, or you could use a file URL instead. The
file URLs take the form
`file:/home/user/public_html/classes/` on Solaris OS or Linux
and the form `file:/c:/home/user/public_html/classes/` on Windows.
You may also select another type of URL, as appropriate.

The network accessibility of the class files enables the RMI runtime to
download code when needed. Rather than defining its own protocol for
code downloading, RMI uses URL protocols supported by the Java platform
(for example, HTTP) to download code. Note that using a full, heavyweight
web server to serve these class files is unnecessary. For example,
a simple HTTP server that provides the functionality
needed to make classes available for downloading in RMI through HTTP can be
found at
<http://java.sun.com/javase/technologies/core/basic/rmi/class-server.zip>.

### Building the Server Classes

> The `engine` package contains only one server-side
> implementation class, `ComputeEngine`, the implementation
> of the remote interface `Compute`.
>
> Assume that user `ann`, the developer of the
> `ComputeEngine` class, has placed
> `ComputeEngine.java` in the directory
> `c:\home\ann\src\engine` on Windows or the directory
> `/home/ann/src/engine` on Solaris OS or Linux. She is
> deploying the class files for clients to download in a subdirectory of
> her `public_html` directory,
> `c:\home\ann\public_html\classes` on Windows or
> `/home/ann/public_html/classes` on Solaris OS or Linux.
> This location is accessible through some web servers as
> `http://host:port/~ann/classes/`.
>
> The `ComputeEngine` class depends on the
> `Compute` and `Task` interfaces, which are
> contained in the `compute.jar` JAR file. Therefore, you
> need the `compute.jar` file in your class path when you
> build the server classes. Assume that the `compute.jar`
> file is located in the directory
> `c:\home\ann\public_html\classes` on Windows or the
> directory `/home/ann/public_html/classes` on Solaris OS or
> Linux. Given these paths, you can use the following commands to build
> the server classes:
>
> > ---
> >
> > **Microsoft Windows**:
> >
> > ```
> >
> > cd c:\home\ann\src
> > javac -cp c:\home\ann\public_html\classes\compute.jar
> >     engine\ComputeEngine.java
> >
> > ```
> >
> > **Solaris OS or Linux**:
> >
> > ```
> >
> > cd /home/ann/src
> > javac -cp /home/ann/public_html/classes/compute.jar
> >     engine/ComputeEngine.java
> >
> > ```
> >
> > ---

The stub class for `ComputeEngine` implements the
`Compute` interface, which refers to the `Task`
interface. So, the class definitions for those two interfaces need to
be network-accessible for the stub to be received by other Java
virtual machines such as the registry's Java virtual machine. The
client Java virtual machine will already have these interfaces in its
class path, so it does not actually need to download their
definitions. The `compute.jar` file under the
`public_html` directory can serve this purpose.

Now, the compute engine is ready to deploy. You could do that now, or
you could wait until after you have built the client.

### Building the Client Classes

> The `client` package contains two classes,
> `ComputePi`, the main client program, and `Pi`,
> the client's implementation of the `Task` interface.
>
> Assume that user `jones`, the developer of the client
> classes, has placed `ComputePi.java` and
> `Pi.java` in the directory
> `c:\home\jones\src\client` on Windows or the directory
> `/home/jones/src/client` on Solaris OS or Linux. He is
> deploying the class files for the compute engine to download in a
> subdirectory of his `public_html` directory,
> `c:\home\jones\public_html\classes` on Windows or
> `/home/jones/public_html/classes` on Solaris OS or Linux.
> This location is accessible through some web servers as
> `http://host:port/~jones/classes/`.
>
> The client classes depend on the `Compute` and
> `Task` interfaces, which are contained in the
> `compute.jar` JAR file. Therefore, you need the
> `compute.jar` file in your class path when you build the
> client classes. Assume that the `compute.jar` file is
> located in the directory
> `c:\home\jones\public_html\classes` on Windows or the
> directory `/home/jones/public_html/classes` on Solaris OS
> or Linux. Given these paths, you can use the following commands to
> build the client classes:
>
> > ---
> >
> > **Microsoft Windows**:
> >
> > ```
> >
> > cd c:\home\jones\src
> > javac -cp c:\home\jones\public_html\classes\compute.jar
> >     client\ComputePi.java client\Pi.java
> > mkdir c:\home\jones\public_html\classes\client
> > cp client\Pi.class 
> >     c:\home\jones\public_html\classes\client
> >
> > ```
> >
> > **Solaris OS or Linux**:
> >
> > ```
> >
> > cd /home/jones/src
> > javac -cp /home/jones/public_html/classes/compute.jar
> >     client/ComputePi.java client/Pi.java
> > mkdir /home/jones/public_html/classes/client
> > cp client/Pi.class
> >     /home/jones/public_html/classes/client
> >
> > ```
> >
> > ---
> >
> > Only the `Pi` class needs to be placed in the directory
> > `public_html\classes\client` because only the
> > `Pi` class needs to be available for downloading to the
> > compute engine's Java virtual machine. Now, you can run the server and then
> > the client.
> >
> > [« Previous](example.html)
> > •
> > [Trail](./TOC.html)
> > •
> > [Next »](running.html)
> >
> > ---
> >
> > Problems with the examples? Try [Compiling and Running
> > the Examples: FAQs](../information/run-examples.html).
> >   
> > Complaints? Compliments? Suggestions? [Give
> > us your feedback](http://download.oracle.com/javase/feedback.html).
> >
> > Your use of this page and all the material on pages under "The Java Tutorials" banner,
> > and all the material on pages under "The Java Tutorials" banner is subject to the [Java SE Tutorial Copyright
> > and License](../information/license.html).
> > Additionally, any example code contained in any of these Java
> > Tutorials pages is licensed under the
> > [Code
> > Sample License](http://developers.sun.com/license/berkeley_license.html).
> >
> > |  |  |  |  |  |
> > | --- | --- | --- | --- | --- |
> > | |  |  | | --- | --- | | duke image | Oracle logo | | [About Oracle](http://www.oracle.com/us/corporate/index.html) | [Oracle Technology Network](http://www.oracle.com/technology/index.html) | [Terms of Service](https://www.samplecode.oracle.com/servlets/CompulsoryClickThrough?type=TermsOfService) | Copyright © 1995, 2011 Oracle and/or its affiliates. All rights reserved. |
> >
> > **Previous page:** Compiling and Running the Example
> >   
> > **Next page:** Running the Example Programs
> >
> >
> >
> >
> > A browser with JavaScript enabled is required for this page to operate properly.