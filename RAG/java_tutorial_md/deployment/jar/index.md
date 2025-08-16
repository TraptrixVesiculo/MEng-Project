[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

Packaging Programs in JAR Files

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

[Using JAR-related APIs](apiindex.html)

[The JarClassLoader Class](jarclassloader.html)

[The JarRunner Class](jarrunner.html)

[Questions and Exercises](QandE/questions.html)

**Trail:** Deployment

[Home Page](../../index.html)
>
[Deployment](../index.html)

[« Previous](../deploymentInDepth/index.html) • [Trail](../TOC.html) • [Next »](basicsindex.html)

# Lesson: Packaging Programs in JAR Files

The Java™ Archive (JAR) file format
enables you to bundle multiple files into a single archive file.
Typically a JAR file contains the class files and auxiliary resources
associated with applets and applications.

The JAR file format provides many benefits:

* *Security*: You can digitally sign the contents of a JAR
  file. Users who recognize your signature can then optionally grant
  your software security privileges it wouldn't otherwise have.* *Decreased download time*: If your applet is bundled in a
    JAR file, the applet's class files and associated resources can be downloaded
    to a browser in a single HTTP transaction without the need for opening a new
    connection for each file.* *Compression*: The JAR format allows you to compress
      your files for efficient storage.* *Packaging for extensions*: The extensions framework provides a
        means by which you can add functionality to the Java core platform, and
        the JAR file format defines the packaging for extensions.
        [Java 3D™](http://java.sun.com/products/java-media/3D) and
        [JavaMail™](http://java.sun.com/products/javamail/index.html) are examples of extensions developed by Sun™.
        By using the JAR file format,
        you can turn your software into extensions as well.* *Package Sealing*: Packages stored in JAR files can
          be optionally sealed so that the package can enforce version consistency.
          Sealing a package within a JAR file means that all classes defined
          in that package must be found in the same JAR file.* *Package Versioning*: A JAR file can hold
            data about the files it contains, such as
            vendor and version information.* *Portability*: The mechanism for handling JAR files is a
              standard part of the Java platform's core API.

This lesson has four sections:

## [Using JAR Files: The Basics](basicsindex.html)

This section shows you how to perform basic JAR-file operations, and how
to run software that is bundled in JAR files.

## [Working with Manifest Files: The Basics](manifestindex.html)

This section explains manifest files and how to customize them so you can do such things as seal packages and set an application's entry point.

## [Signing and Verifying JAR Files](signindex.html)

This section shows you how to digitally sign JAR files and verify the signatures of signed JAR files.

## [Using JAR-related APIs](apiindex.html)

This section introduces you to some of the JAR-handling features of
the Java platform.
The JAR file format is an important part of the
Java platform's extension mechanism. You can learn more about
that aspect of JAR
files in the
[The Extension Mechanism](../../ext/index.html)
trail of this tutorial.

## [Questions and Exercises: JAR](QandE/questions.html)

Test what you've learned about JAR.

## Additional References

The documentation for the Java Development Kit includes information about the Jar tool:

* [Java Archive (JAR) Files Guide](http://java.sun.com/javase/6/docs/technotes/guides/jar/index.html)
* [JAR File Specification](http://java.sun.com/javase/6/docs/technotes/guides/jar/jar.html)

[« Previous](../deploymentInDepth/index.html)
•
[Trail](../TOC.html)
•
[Next »](basicsindex.html)

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

**Previous page:** Previous Lesson
  
**Next page:** Using JAR Files: The Basics




A browser with JavaScript enabled is required for this page to operate properly.