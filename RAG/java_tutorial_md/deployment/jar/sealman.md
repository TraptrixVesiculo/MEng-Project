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

[Modifying a Manifest File](modman.html)

[Setting an Application's Entry Point](appman.html)

[Adding Classes to the JAR File's Classpath](downman.html)

[Setting Package Version Information](packageman.html)

Sealing Packages within a JAR File

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

[« Previous](packageman.html) • [Trail](../TOC.html) • [Next »](signindex.html)

# Sealing Packages within a JAR File

Packages within JAR files can be optionally sealed, which means
that all classes defined in that package must be archived in the same JAR file. You might want to seal a package, for example, to ensure
version consistency among the classes in your software.

You seal a package in a JAR file by adding the Sealed header in the manifest, which has the general form:

```

Name: myCompany/myPackage/
Sealed: true

```

The value myCompany/myPackage/ is the name of the package to seal.

Note that the package name must end with a "/".

## An Example

We want to seal two packages firstPackage and secondPackage in the JAR file MyJar.jar.

We first create a text file named Manifest.txt with the following contents:

```

Name: myCompany/firstPackage/
Sealed: true

Name: myCompany/secondPackage/
Sealed: true

```

---

**Warning:**

The text file must end with a new line or carriage return.
The last line will not be parsed properly if it does not
end with a new line or carriage return.

---

We then create a JAR file named MyJar.jar by entering the following command:

```

jar cmf MyJar.jar Manifest.txt MyPackage/*.class

```

This creates the JAR file with a manifest with the following contents:

```

Manifest-Version: 1.0
Created-By: 1.6.0 (Sun Microsystems Inc.)
Name: myCompany/firstPackage/
Sealed: true
Name: myCompany/secondPackage/
Sealed: true

```

## Sealing JAR Files

If you want to guarantee that all classes in a package come from the same code source, use JAR sealing. A sealed JAR specifies that all packages defined by that JAR are sealed unless overridden on a per-package basis.

To seal a jar file, use the Sealed manifest header with the value true. For example,

```

Sealed: true

```

specifies that all packages in this archive are sealed unless explicitly
overridden for particular packages with the Sealed attribute
in a manifest entry.

[« Previous](packageman.html)
•
[Trail](../TOC.html)
•
[Next »](signindex.html)

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

**Previous page:** Setting Package Version Information
  
**Next page:** Signing and Verifying JAR Files




A browser with JavaScript enabled is required for this page to operate properly.