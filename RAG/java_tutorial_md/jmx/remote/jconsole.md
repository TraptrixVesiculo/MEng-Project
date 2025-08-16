[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Java Management Extensions (JMX)
  
**Lesson:** Remote Management

[Remote Management](index.html)

Exposing a Resource for Remote Management By JConsole

[Creating a Custom JMX Client](custom.html)

[Home Page](../../index.html)
>
[Java Management Extensions (JMX)](../index.html)
>
[Remote Management](index.html)

[« Previous](index.html) • [Trail](../TOC.html) • [Next »](custom.html)

# Exposing a Resource for Remote Management By JConsole

Exposing your Java applications for remote management by using the JMX API can be extremely simple, if you use the out-of-the-box remote management agent and an existing monitoring and management tool such as JConsole.

To expose your application for remote management, you need to start it with the correct properties. This example shows how to expose the
[`Main`](../examples/Main.java)
JMX agent for remote management.

---

**Security consideration:** 
For the sake of simplicity, the authentication and encryption security mechanisms are disabled in this example. However, you should implement these security mechanisms when implementing remote management in real-world environments.
[What Next?](../../jmx/end.html) provides pointers to other JMX technology documentation that shows how to activate security.

---

This example requires version 6 of the Java SE platform. To monitor the `Main` JMX agent remotely, follow these steps:

1. If you have not done so already, save
   [`jmx_examples.zip`](../examples/jmx_examples.zip) into your `work_dir` directory.
2. Unzip the bundle of sample classes by using the following command in a terminal window.

   ```

   unzip jmx_examples.zip

   ```
3. Compile the example Java classes from within the
   `work_dir` directory.

   ```

   javac com/example/*.java

   ```
4. Start the `Main` application, specifying the properties that expose `Main` for remote management:

   ```

   java -Dcom.sun.management.jmxremote.port=9999 \  

        -Dcom.sun.management.jmxremote.authenticate=false \  

        -Dcom.sun.management.jmxremote.ssl=false \  

        com.example.Main

   ```

   A confirmation that `Main` is waiting for something to happen is generated.
5. Start JConsole in a different terminal window on a **different machine**:

   ```

   jconsole

   ```

   The New Connection dialog box is displayed, presenting a list of running JMX agents that you can connect to locally.
6. Select Remote Process, and type the following in the Remote Process field:

   ```

   hostname:9999

   ```

   In this address, `hostname` is the name of the remote machine on which the `Main` application is running and 9999 is the number of the port on which the out-of-the-box JMX connector will be connected.
7. Click Connect.

   A summary of the current activity of the Java Virtual Machine (Java VM) in which `Main` is running is displayed.
8. Click the MBeans tab.

   This panel shows all the MBeans that are currently registered in the remote MBean server.
9. In the left-hand frame, expand the `com.example` node in the MBean tree.

   You see the example MBean `Hello` that was created and registered by `Main`. If you click `Hello`, you see its associated Attributes and Operations nodes in the MBean tree, even though it is running on a different machine.
10. To close JConsole, select Connection -> Exit.

[« Previous](index.html)
•
[Trail](../TOC.html)
•
[Next »](custom.html)

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

**Previous page:** Remote Management
  
**Next page:** Creating a Custom JMX Client




A browser with JavaScript enabled is required for this page to operate properly.