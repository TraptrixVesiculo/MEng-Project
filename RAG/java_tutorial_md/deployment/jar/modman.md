[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Deployment
  
**Lesson:** Packaging Programs in JAR Files
  
**Section:** Working with Manifest Files: The Basics

[Packaging Programs in JAR Files](index.html)

[Using JAR Files: The Basics](basicsindex.html)

[Creating a JAR File](build.html)

[Viewing the Contents of a JAR File](view.html)

[Extracting the Contents of a JAR File](unpack.html)

[Updating a JAR File](update.html)

[Running JAR-Packaged Software](run.html)

[Working with Manifest Files: The Basics](manifestindex.html)

[Understanding the Default Manifest](defman.html)

Modifying a Manifest File

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

[« Previous](defman.html) • [Trail](../TOC.html) • [Next »](appman.html)

# Modifying a Manifest File

You use the m command-line option to add custom information to the manifest during creation of a JAR file. This section describes the m option.

The Jar tool automatically puts a [default manifest](defman.html) with the pathname
META-INF/MANIFEST.MF into any JAR file you create. You can
enable special JAR file functionality, such as
[package sealing, by
modifying the default manifest.
Typically, modifying the default manifest involves adding special-purpose *headers* to the manifest that allow the JAR file to perform a particular desired function.](sealman.html)

To modify the manifest, you must first prepare a text file containing the information you wish to add to the manifest. You then use the Jar tool's m option to add the information in your file to the manifest.

---

**Warning:** 
The text file from which you are creating the manifest must end with a new line or carriage return.
The last line will not be parsed properly if it does not
end with a new line or carriage return.

---

The basic command has this format:

```

jar cfm jar-file manifest-addition input-file(s)

```

Let's look at the options and arguments used in this command:

* The c option indicates that you want to *create*
  a JAR file.* The m option indicates that you want to merge
    information from an existing file into the manifest file of the JAR file you're creating.* The f option indicates that you want the output to go to a *file* (the JAR file you're creating) rather than to standard output.* *manifest-addition* is the name (or path and name) of the existing text file whose contents you want to add to the contents of JAR file's manifest.* *jar-file* is the name that you want the resulting JAR file to have.* The *input-file(s)* argument is a space-separated list of one or more files that you want to be placed in your JAR file.

The m and f options must be in the same order as the corresponding arguments.

---

**Note:** The contents of the manifest must be encoded in UTF8.

---

The remaining sections of this lesson demonstrate specific modifications you may want to make to the manifest file.

[« Previous](defman.html)
•
[Trail](../TOC.html)
•
[Next »](appman.html)

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

**Previous page:** Understanding the Default Manifest
  
**Next page:** Setting an Application's Entry Point




A browser with JavaScript enabled is required for this page to operate properly.