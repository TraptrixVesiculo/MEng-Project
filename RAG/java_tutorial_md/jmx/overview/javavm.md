[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Java Management Extensions (JMX)
  
**Lesson:** Overview of the JMX Technology

[Overview of the JMX Technology](index.html)

[Why Use the JMX Technology?](why.html)

[Architecture of the JMX Technology](architecture.html)

Monitoring and Management of the Java Virtual Machine

[Home Page](../../index.html)
>
[Java Management Extensions (JMX)](../index.html)
>
[Overview of the JMX Technology](index.html)

[« Previous](architecture.html) • [Trail](../TOC.html) • [Next »](../mbeans/index.html)

# Monitoring and Management of the Java Virtual Machine

The JMX technology can also be used to monitor and manage the Java virtual machine (Java VM).

The Java VM has built-in instrumentation that enables you to monitor and manage it by using the JMX technology. These built-in management utilities are often referred to as *out-of-the-box* management tools for the Java VM. To monitor and manage different aspects of the Java VM, the Java VM includes a platform MBean server and special MXBeans for use by management applications that conform to the JMX specification.

## Platform MXBeans and the Platform MBean Server

The *platform MXBeans* are a set of MXBeans that is provided with the Java SE platform for monitoring and managing the Java VM and other components of the Java Runtime Environment (JRE). Each platform MXBean encapsulates a part of Java VM functionality, such as the class-loading system, just-in-time (JIT) compilation system, garbage collector, and so on. These MXBeans can be displayed and interacted with by using a monitoring and management tool that complies with the JMX specification, to enable you to monitor and manage these different VM functionalities. One such monitoring and management tool is the Java SE platform's JConsole graphical user interface (GUI).

The Java SE platform provides a standard *platform MBean server* in which these platform MXBeans are registered. The platform MBean server can also register any other MBeans you wish to create.

## JConsole

The Java SE platform includes the JConsole monitoring and management tool, which complies with the JMX specification. JConsole uses the extensive instrumentation of the Java VM (the platform MXBeans) to provide information about the performance and resource consumption of applications that are running on the Java platform.

## Out-of-the-Box Management in Action

Because standard monitoring and management utilities that implement the JMX technology are built into the Java SE platform, you can see the out-of-the-box JMX technology in action without having to write a single line of JMX API code. You can do so by launching a Java application and then monitoring it by using JConsole.

## Monitoring an Application by Using JConsole

This procedure shows how to monitor the Notepad Java application. Under releases of the Java SE platform prior to version 6, applications that you want to monitor with JConsole need to be started with the following option.

```

-Dcom.sun.management.jmxremote

```

However, the version of JConsole provided with the Java SE 6 platform can attach to any local application that supports the Attach API. In other words, any application that is started in the Java SE 6 HotSpot VM is detected automatically by JConsole, and does not need to be started using the above command-line option.

1. Start the Notepad Java application, by using the following command in a terminal window:

   ```

   java -jar jdk_home/demo/jfc/Notepad/Notepad.jar

   ```

   Where `jdk_home` is the directory in which the Java Development Kit (JDK) is installed. If you are not running version 6 of the Java SE platform, you will need to use the following command:

```

java -Dcom.sun.management.jmxremote -jar jdk_home/demo/jfc/Notepad/Notepad.jar

```

2. Once Notepad has opened, in a different terminal window, start JConsole by using the following command:

   ```

   jconsole

   ```

   A New Connection dialog box is displayed.
3. In the New Connection dialog box, select `Notepad.jar` from the Local Process list, and click the Connect button.

   JConsole opens and connects itself to the `Notepad.jar` process. When JConsole opens, you are presented with an overview of monitoring and management information related to Notepad. For example, you can view the amount of heap memory the application is consuming, the number of threads the application is currently running, and how much central procesing unit (CPU) capacity the application is consuming.
4. Click the different JConsole tabs.

   Each tab presents more detailed information about the different areas of functionality of the Java VM in which Notepad is running. All the information presented is obtained from the various JMX technology MXBeans mentioned in this trail. All the platform MXBeans can be displayed in the MBeans tab. The MBeans tab is examined in the next section of this trail.
5. To close JConsole, select Connection -> Exit.

[« Previous](architecture.html)
•
[Trail](../TOC.html)
•
[Next »](../mbeans/index.html)

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

**Previous page:** Architecture of the JMX Technology
  
**Next page:** Introducing MBeans




A browser with JavaScript enabled is required for this page to operate properly.