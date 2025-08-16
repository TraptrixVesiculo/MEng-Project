[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Deployment
  
**Lesson:** Packaging Programs in JAR Files
  
**Section:** Signing and Verifying JAR Files

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

Verifying Signed JAR Files

[Using JAR-related APIs](apiindex.html)

[The JarClassLoader Class](jarclassloader.html)

[The JarRunner Class](jarrunner.html)

[Questions and Exercises](QandE/questions.html)

[Home Page](../../index.html)
>
[Deployment](../index.html)
>
[Packaging Programs in JAR Files](index.html)

[« Previous](signing.html) • [Trail](../TOC.html) • [Next »](apiindex.html)

# Verifying Signed JAR Files

Typically, verification of signed JAR files will be the
responsibility of your JavaTM
Runtime Environment.
Your browser will verify signed applets that it downloads. Signed applications invoked with the -jar option of the interpreter will be verified by the runtime environment.

However, you can verify signed JAR files yourself by using
the Jarsigner tool. You might want to do this, for example,
to test a signed JAR file that you've prepared.

The basic command to use for verifying a signed JAR file is:

```

jarsigner -verify jar-file

```

This command will verify the JAR file's signature and ensure that
the files in the archive haven't changed since it was signed. You'll
see the following message if the verification is successful:

```

jar verified.

```

If you try to verify an unsigned JAR file, the following message results:

```

jar is unsigned. (signatures missing or not parsable)

```

If the verification fails, an appropriate message is displayed.
For example, if the contents of a JAR file have changed since
the JAR file was signed, a message similar to the following will
result if you try to verify the file:

```

jarsigner: java.lang.SecurityException: invalid SHA1 
signature file digest for test/classes/Manifest.class

```

[« Previous](signing.html)
•
[Trail](../TOC.html)
•
[Next »](apiindex.html)

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

**Previous page:** Signing JAR Files
  
**Next page:** Using JAR-related APIs




A browser with JavaScript enabled is required for this page to operate properly.