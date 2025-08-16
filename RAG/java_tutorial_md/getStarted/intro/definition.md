[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Getting Started
  
**Lesson:** The Java Technology Phenomenon

[The Java Technology Phenomenon](index.html)

About the Java Technology

[What Can Java Technology Do?](cando.html)

[How Will Java Technology Change My Life?](changemylife.html)

[Home Page](../../index.html)
>
[Getting Started](../index.html)
>
[The Java Technology Phenomenon](index.html)

[« Previous](index.html) • [Trail](../TOC.html) • [Next »](cando.html)

# About the Java Technology

Java technology is both a programming language and a platform.

## The Java Programming Language

The Java
programming language is a high-level language that can be characterized
by all of the following buzzwords:

|  |  |
| --- | --- |
| - Simple | - Architecture neutral |
| - Object oriented | - Portable |
| - Distributed | - High performance |
| - Multithreaded | - Robust |
| - Dynamic | - Secure |

Each of the preceding buzzwords is explained in
[*The Java Language Environment*](http://java.sun.com/docs/white/langenv/) , a white paper written by James Gosling and Henry McGilton.

In the Java programming language, all source code is first
written in plain text
files ending
with the `.java` extension. Those source files are then compiled
into `.class` files by the `javac`
compiler.
A `.class` file does not contain code that
is native to your processor;
it instead contains *bytecodes* — the machine language of the Java Virtual Machine[1](#FOOT) (Java VM).
The `java` launcher tool then runs your application with an instance of the Java Virtual Machine.

![Figure showing MyProgram.java, compiler, MyProgram.class, Java VM, and My Program running on a computer.](../../figures/getStarted/g1.gif)

An overview of the software development process.

Because the Java VM is
available on many different operating systems,
the same `.class` files are capable of running on Microsoft Windows, the Solaris TM
Operating System (Solaris OS), Linux, or Mac OS. Some virtual machines,
such as the
[Java HotSpot virtual machine](http://java.sun.com/products/hotspot/), perform additional steps at runtime
to give your application a performance boost. This include various
tasks such as
finding performance bottlenecks and recompiling (to native code)
frequently used sections of code.

![Figure showing source code, compiler, and Java VM's for Win32, Solaris OS/Linux, and Mac OS](../../figures/getStarted/helloWorld.gif)

Through the Java VM, the same application is capable of running on multiple platforms.

## The Java Platform

A *platform* is the hardware or software environment in which a program
runs. We've already mentioned some of the most popular platforms like Microsoft Windows,
Linux, Solaris OS, and Mac OS. Most platforms can be described as a
combination of the operating system and underlying hardware. The Java platform differs from
most other platforms in that it's a software-only platform that runs on top of
other hardware-based platforms.

The Java platform has two components:

* The *Java Virtual Machine** The *Java Application Programming Interface* (API)

You've already been introduced to the Java Virtual Machine;
it's the base for the Java
platform and is ported onto various hardware-based platforms.

The API is a large collection of ready-made software components that
provide many useful capabilities.
It is grouped into libraries of related classes and
interfaces; these libraries are known as *packages*. The next section,
[What Can Java Technology Do?](cando.html)
highlights some of the functionality provided by the API.

![Figure showing MyProgram.java, API, Java Virtual Machine, and Hardware-Based Platform](../../figures/getStarted/g3.gif)

The API and Java Virtual Machine insulate the program from the underlying hardware.

As a platform-independent environment, the Java
platform can be a bit slower than native code. However,
advances in compiler and virtual machine technologies
are bringing
performance close to that of native code without threatening portability.

The terms"Java Virtual Machine" and "JVM" mean a Virtual Machine for the Java platform.

[« Previous](index.html)
•
[Trail](../TOC.html)
•
[Next »](cando.html)

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

**Previous page:** The Java Technology Phenomenon
  
**Next page:** What Can Java Technology Do?




A browser with JavaScript enabled is required for this page to operate properly.