[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Deployment
  
**Lesson:** Packaging Programs in JAR Files

[Packaging Programs in JAR Files](index.html)

[Using JAR Files: The Basics](basicsindex.html)

[Creating a JAR File](build.html)

[Viewing the Contents of a JAR File](view.html)

[Extracting the Contents of a JAR File](unpack.html)

[Updating a JAR File](update.html)

[Running JAR-Packaged Software](run.html)

[Working with Manifest Files: The Basics](manifestindex.html)

[Understanding the Default Manifest](defman.html)

[Modifying a Manifest File](modman.html)

[Setting an Application's Entry Point](appman.html)

[Adding Classes to the JAR File's Classpath](downman.html)

[Setting Package Version Information](packageman.html)

[Sealing Packages within a JAR File](sealman.html)

[Signing and Verifying JAR Files](signindex.html)

[Understanding Signing and Verification](intro.html)

[Signing JAR Files](signing.html)

[Verifying Signed JAR Files](verify.html)

Using JAR-related APIs

[The JarClassLoader Class](jarclassloader.html)

[The JarRunner Class](jarrunner.html)

[Questions and Exercises](QandE/questions.html)

[Home Page](../../index.html)
>
[Deployment](../index.html)
>
[Packaging Programs in JAR Files](index.html)

[« Previous](verify.html) • [Trail](../TOC.html) • [Next »](jarclassloader.html)

# Using JAR-related APIs

The Java platform contains several classes for use with JAR files. Some of these APIs are:

* [The **java.util.jar** package](http://download.oracle.com/javase/7/docs/api/java/util/jar/package-summary.html)* [The **java.net.JarURLConnection** class](http://download.oracle.com/javase/7/docs/api/java/net/JarURLConnection.html)* [The **java.net.URLClassLoader** class](http://download.oracle.com/javase/7/docs/api/java/net/URLClassLoader.html)

To give you an idea of the possibilities that are opened up
by these new APIs, this lesson guides you through the inner workings of
a sample application called JarRunner.

## An Example - The JarRunner Application

JarRunner enables you to run an application that's bundled in a JAR
file by specifying the JAR file's URL on the command line. For example,
if an application called TargetApp were bundled in a JAR file at
http://www.xxx.yyy/TargetApp.jar, you could run
the application using this command:

```

java JarRunner http://www.xxx.yyy/TargetApp.jar

```

In order for JarRunner to work, it must be able to perform the following
tasks, all of which are accomplished by using the new APIs:

* Access the remote JAR file and establish a communications
  link with it.* Inspect the JAR file's manifest to see which of the classes in the
    archive is the main class.* Load the classes in the JAR file.

The JarRunner application consists of two classes, JarRunner
and JarClassLoader. JarRunner delegates most of the JAR-handling
tasks to the JarClassLoader class. JarClassLoader extends
the java.net.URLClassLoader class. You can browse the source code for
the JarRunner and JarClassLoader classes
before proceeding with the lesson:

* [`JarRunner.java`](examples/JarRunner.java)* [`JarClassLoader.java`](examples/JarClassLoader.java)

This lesson has two parts:

## [The JarClassLoader Class](jarclassloader.html)

This section shows you how JarClassLoader uses some of the new APIs
to perform tasks required for the JarRunner application to work.

## [The JarRunner Class](jarrunner.html)

This section summarizes the JarRunner class that comprises the
JarRunner application.

[« Previous](verify.html)
•
[Trail](../TOC.html)
•
[Next »](jarclassloader.html)

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

**Previous page:** Verifying Signed JAR Files
  
**Next page:** The JarClassLoader Class




A browser with JavaScript enabled is required for this page to operate properly.