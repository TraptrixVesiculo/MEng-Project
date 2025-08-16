[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Deployment
  
**Lesson:** Packaging Programs in JAR Files

[Packaging Programs in JAR Files](index.html)

Using JAR Files: The Basics

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

[Using JAR-related APIs](apiindex.html)

[The JarClassLoader Class](jarclassloader.html)

[The JarRunner Class](jarrunner.html)

[Questions and Exercises](QandE/questions.html)

[Home Page](../../index.html)
>
[Deployment](../index.html)
>
[Packaging Programs in JAR Files](index.html)

[« Previous](index.html) • [Trail](../TOC.html) • [Next »](build.html)

# Using JAR Files: The Basics

JAR files are packaged with the ZIP file format, so you
can use them for tasks such
as lossless data compression, archiving, decompression, and
archive unpacking. These tasks are among the most common uses
of JAR files, and you can realize many JAR file benefits using
only these basic features.

Even if you want to take advantage of advanced functionality
provided by the JAR file format such as electronic signing, you'll
first need to become familiar with the fundamental operations.

To perform basic tasks with JAR files, you use the
Java Archive Tool provided as
part of the Java Development Kit.
Because the Java Archive tool is invoked by using the jar
command, this tutorial refers to it as 'the Jar tool'.

As a synopsis and preview of some of the topics to be covered in this
section, the following table summarizes common JAR file operations:

**Common JAR file operations**

| Operation | Command |
| To create a JAR file | jar cf *jar-file input-file(s)* |
| To view the contents of a JAR file | jar tf *jar-file* |
| To extract the contents of a JAR file | jar xf *jar-file* |
| To extract specific files from a JAR file | jar xf *jar-file archived-file(s)* |
| To run an application packaged as a JAR file (requires the [Main-class](appman.html) manifest header) | java -jar *app.jar* |
| To invoke an applet packaged as a JAR file | ```  <applet code=AppletClassName.class         archive="JarFileName.jar"         width=width height=height> </applet>  ``` |

This section shows you how to perform the most common
JAR-file operations, with examples for each of the basic features:

## [Creating a JAR File](build.html)

This section shows you how to use the Jar tool to package files and
directories into a JAR file.

## [Viewing the Contents of a JAR File](view.html)

You can display a JAR file's table of contents to see what it
contains without actually unpacking the JAR file.

## [Extracting the Contents of a JAR File](unpack.html)

You can use the Jar tool to unpack a JAR file. When extracting files,
the Jar tool makes copies of the desired files and writes them to the
current directory, reproducing the directory structure that the files
have in the archive.

## [Updating a JAR File](update.html)

This section shows you how to update the contents of an existing JAR file by modifying its manifest or by adding files.

## [Running JAR-Packaged Software](run.html)

This section shows you how to invoke and run applets and applications
that are packaged in JAR files.

## Additional References

The documentation for the Java Development Kit includes reference
pages for the Jar tool:

* [Jar tool reference for Windows platform](http://java.sun.com/javase/6/docs/technotes/tools/windows/jar.html)
* [Jar tool reference for Solaris platform](http://java.sun.com/javase/6/docs/technotes/tools/solaris/jar.html)

[« Previous](index.html)
•
[Trail](../TOC.html)
•
[Next »](build.html)

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

**Previous page:** Packaging Programs in JAR Files
  
**Next page:** Creating a JAR File




A browser with JavaScript enabled is required for this page to operate properly.