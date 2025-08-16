[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Deployment
  
**Lesson:** Packaging Programs in JAR Files
  
**Section:** Using JAR Files: The Basics

[Packaging Programs in JAR Files](index.html)

[Using JAR Files: The Basics](basicsindex.html)

[Creating a JAR File](build.html)

[Viewing the Contents of a JAR File](view.html)

Extracting the Contents of a JAR File

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

[« Previous](view.html) • [Trail](../TOC.html) • [Next »](update.html)

# Extracting the Contents of a JAR File

The basic command to use for extracting the contents of a JAR file is:

```

jar xf jar-file [archived-file(s)]

```

Let's look at the options and arguments in this command:

* The x option indicates that you want to *extract*
  files from the JAR archive.* The f options indicates that the JAR *file* from
    which files are to be extracted is specified on the command line,
    rather than through stdin.* The jar-file argument is the filename (or path and filename)
      of the JAR file from which to extract files.* archived-file(s) is an optional argument consisting of
        a space-separated list of the files to be extracted from the archive.
        If this argument is not present, the Jar tool will extract all the files
        in the archive.

As usual, the order in which the x and f options appear
in the command doesn't matter, but there must not be a space between them.

When extracting files, the Jar tool makes copies of the desired files and
writes them to the current directory, reproducing the directory structure
that the files have in the archive. The original JAR file remains unchanged.

---

**Caution:** When it extracts files, the Jar tool
will overwrite any existing files having the same pathname as the
extracted files.

---

## An Example

Let's extract some files from the TicTacToe JAR file we've been using
in previous sections. Recall that the contents of TicTacToe.jar
are:

```

META-INF/MANIFEST.MF
TicTacToe.class
audio/
audio/beep.au
audio/ding.au
audio/return.au
audio/yahoo1.au
audio/yahoo2.au
images/
images/cross.gif
images/not.gif

```

Suppose you want to extract the TicTacToe class file and
the cross.gif image file. To do so, you can use this command:

```

jar xf TicTacToe.jar TicTacToe.class images/cross.gif

```

This command does two things:

* It places a copy of TicTacToe.class in the current
  directory.* It creates the directory images, if it doesn't already
    exist, and places a copy of cross.gif within it.

The original TicTacToe JAR file remains unchanged.

As many files as desired can be extracted from the JAR file in the
same way. When the command doesn't specify which files to extract, the
Jar tool extracts all files in the archive. For example, you can extract
all the files in the TicTacToe archive by using this command:

```

jar xf TicTacToe.jar

```

[« Previous](view.html)
•
[Trail](../TOC.html)
•
[Next »](update.html)

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

**Previous page:** Viewing the Contents of a JAR File
  
**Next page:** Updating a JAR File




A browser with JavaScript enabled is required for this page to operate properly.