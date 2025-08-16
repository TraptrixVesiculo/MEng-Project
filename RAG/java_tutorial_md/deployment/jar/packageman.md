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

Setting Package Version Information

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

[« Previous](downman.html) • [Trail](../TOC.html) • [Next »](sealman.html)

# Setting Package Version Information

You may need to include package version information in a JAR file's manifest.
You provide this information with the following headers in the manifest:

**Headers in a manifest**

| Header | Definition |
| Name | The name of the specification. |
| Specification-Title | The title of the specification. |
| Specification-Version | The version of the specification. |
| Specification-Vendor | The vendor of the specification. |
| Implementation-Title | The title of the implementation. |
| Implementation-Version | The build number of the implementation. |
| Implementation-Vendor | The vendor of the implementation. |

One set of such headers can be assigned to each package. The versioning headers should appear directly beneath the Name header for the package. This example shows all the versioning headers:

```

Name: java/util/
Specification-Title: Java Utility Classes
Specification-Version: 1.2
Specification-Vendor: Sun Microsystems, Inc.
Implementation-Title: java.util
Implementation-Version: build57
Implementation-Vendor: Sun Microsystems, Inc.

```

For more information about package version headers, see the
[Package Versioning specification](http://java.sun.com/javase/6/docs/technotes/guides/versioning/spec/versioning2.html#wp89936) .

## An Example

We want to include the headers in the example above in the manifest of MyJar.jar.

We first create a text file named Manifest.txt with the following contents:

```

Name: java/util/
Specification-Title: Java Utility Classes
Specification-Version: 1.2
Specification-Vendor: Sun Microsystems, Inc.
Implementation-Title: java.util 
Implementation-Version: build57
Implementation-Vendor: Sun Microsystems, Inc.

```

---

**Warning:** The text file must end with a new line or carriage return.
The last line will not be parsed properly if it does not
end with a new line or carriage return.

---

We then create a JAR file named MyJar.jar by entering the following command:

```

jar cfm MyJar.jar Manifest.txt MyPackage/*.class

```

This creates the JAR file with a manifest with the following contents:

```

Manifest-Version: 1.0
Created-By: 1.6.0 (Sun Microsystems Inc.)
Name: java/util/
Specification-Title: Java Utility Classes
Specification-Version: 1.2
Specification-Vendor: Sun Microsystems, Inc.
Implementation-Title: java.util 
Implementation-Version: build57
Implementation-Vendor: Sun Microsystems, Inc.

```

[« Previous](downman.html)
•
[Trail](../TOC.html)
•
[Next »](sealman.html)

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

**Previous page:** Adding Classes to the JAR File's Classpath
  
**Next page:** Sealing Packages within a JAR File




A browser with JavaScript enabled is required for this page to operate properly.