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

Working with Manifest Files: The Basics

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

[« Previous](run.html) • [Trail](../TOC.html) • [Next »](defman.html)

# Working with Manifest Files: The Basics

JAR files support a wide range of functionality, including electronic signing, version control, package sealing, and others. What gives a JAR file this versatility? The answer is the JAR file's *manifest*.

The manifest is a special file that can contain information about the files packaged in a JAR file. By tailoring this "meta" information that the manifest contains, you enable the JAR file to serve a variety of purposes.

This lesson will explain the contents of the manifest file and show you how to work with it, with examples for the basic features:

## [Understanding the Default Manifest](defman.html)

When you create a JAR file, a default manifest is created automatically. This section describes the default manifest.

## [Modifying a Manifest File](modman.html)

This section shows you the basic method of modifying a manifest file. The later sections demonstrate specific modifications you may want to make.

## [Setting an Application's Entry Point](appman.html)

This section describes how to use the Main-Class header in the manifest file to set an application's entry point.

## [Adding Classes to the JAR File's Classpath](downman.html)

This section describes how to use the Class-Path header in the manifest file to add classes in other JAR files to the classpath when running an applet or application.

## [Setting Package Version Information](packageman.html)

This section describes how to use the package version headers in the manifest file.

## [Sealing Packages within a JAR File](sealman.html)

This section describes how to seal packages within a JAR file by modifying the manifest file.

## Additional Information

A
[specification](http://java.sun.com/javase/6/docs/technotes/guides/jar/jar.html#JAR%20Manifest) of the manifest format is part of the on-line JDK documentation.

[« Previous](run.html)
•
[Trail](../TOC.html)
•
[Next »](defman.html)

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

**Previous page:** Running JAR-Packaged Software
  
**Next page:** Understanding the Default Manifest




A browser with JavaScript enabled is required for this page to operate properly.