[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Creating a GUI With JFC/Swing
  
**Lesson:** Getting Started with Swing

[Getting Started with Swing](index.html)

[About the JFC and Swing](about.html)

Compiling and Running Swing Programs

[Home Page](../../index.html)
>
[Creating a GUI With JFC/Swing](../index.html)
>
[Getting Started with Swing](index.html)

[« Previous](about.html) • [Trail](../TOC.html) • [Next »](../learn/index.html)

# Compiling and Running Swing Programs

This section explains how to compile and run a Swing application
from the command line. For information on compiling and running a
Swing application using NetBeans IDE, see
[Running Tutorial Examples in NetBeans IDE](../../information/examples.html).
The compilation instructions work for all Swing programs — applets,
as well as applications. Here are the steps you need to follow:

* Install the latest release of the Java SE platform, if you haven't
  already done so.* Create a program that uses Swing components.* Compile the program.* Run the program.

### Install the Latest Release of the Java SE Platform

> You can download the latest release of the JDK for free from
> <http://java.sun.com/javase/downloads>.

### Create a Program That Uses Swing Components

> You can use a simple program we provide, called HelloWorldSwing, that brings
> up the GUI shown in the figure below. The program is in a single file,
> [`HelloWorldSwing.java`](../examples/start/HelloWorldSwingProject/src/start/HelloWorldSwing.java). When you save this file, you must match the spelling and
> capitalization of its name exactly.
>
> The `HelloWorldSwing.java` example, like all of our Swing
> tutorial examples, is created inside a package. If you look at the source code,
> you see the following line at the beginning of the file:
>
> ```
>
> package start;
>
> ```
>
> This means you must put the `HelloWorldSwing.java` file inside
> of a `start` directory. You compile and run the example from the
> directory above the `start` directory.
> The tutorial examples from the *Using Swing Components*
> lesson are inside of a `components` package and the examples
> from the *Writing Event Listeners* lesson are inside a
> `events` package, and so on.
> For more information, you might want to see the
> [`Packages`](../../java/package/index.html) lesson.
>
> ![Screen shot of HelloWorldSwing application](../../figures/uiswing/learn/1helloworldswing.png)

### Compile the Program

> Your next step is to compile the program. To compile the example, from the
> directory above the
> [`HelloWorldSwing.java`](../examples/start/HelloWorldSwingProject/src/start//HelloWorldSwing.java) file:
>
> ```
>
> javac start/HelloWorldSwing.java
>
> ```
>
> If you prefer, you may compile the example from within the
> `start` directory:
>
> ```
>
> javac HelloWorldSwing.java
>
> ```
>
> but you must remember to leave the `start` directory to
> execute the program.
>
> If you are unable to compile, make sure you are using the compiler in a
> recent release of the Java platform.
> You can verify the version of your compiler or Java Runtime Environment (JRE)
> using these commands
>
> ```
>
> javac -version
> java -version
>
> ```
>
> Once you've updated your JDK,
> you should be able to use the programs in this trail without changes.
> Another common mistake is installing the JRE
> and not the full Java Development Kit (JDK) needed to compile
> these programs. Refer to the
> [Getting Started](../../getStarted/index.html) trail to help you solve any compiling problems you encounter.
> Another resource is the
> [Troubleshooting Guide for Java™ SE 6
> Desktop Technologies](http://java.sun.com/javase/6/webnotes/trouble/TSG-Desktop/html/index.html).

### Run the Program

> After you compile the program successfully, you can run it.
> From the directory above the `start` directory:
>
> ```
>
> java start.HelloWorldSwing
>
> ```

[« Previous](about.html)
•
[Trail](../TOC.html)
•
[Next »](../learn/index.html)

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

**Previous page:** About the JFC and Swing
  
**Next page:** Learning Swing with the NetBeans IDE




A browser with JavaScript enabled is required for this page to operate properly.