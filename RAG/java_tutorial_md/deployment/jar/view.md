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

Viewing the Contents of a JAR File

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

[« Previous](build.html) • [Trail](../TOC.html) • [Next »](unpack.html)

# Viewing the Contents of a JAR File

The basic format of the command for viewing the contents of a JAR file is:

```

jar tf jar-file

```

Let's look at the options and argument used in this command:

* The t option indicates that you want to view the
  *table* of contents of the JAR file.* The f option indicates that the JAR file whose
    contents are to be viewed is specified on the command line.* The jar-file argument is the path and name of the JAR file whose contents you want to view.

The t and f options can appear in either
order, but there must not be any space between them.

This command will display the JAR file's table of contents to stdout.

You can optionally add the verbose option, v, to produce
additional information about file sizes and last-modified dates
in the output.

## An Example

Let's use the Jar tool to list the contents of the
TicTacToe.jar file we created in the previous section:

```

jar tf TicTacToe.jar

```

This command displays the contents of the JAR file to stdout:

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

The JAR file contains the TicTacToe class file and the audio and
images directory, as expected. The output also shows that JAR file
contains a default manifest file, META-INF/MANIFEST.MF, which was automatically placed in the archive by the JAR tool. For more information, see the
[Understanding the Default Manifest](defman.html) section.

All pathnames are displayed with forward slashes, regardless of
the platform or operating system you're using. Paths in JAR files
are always relative; you'll never see a path
beginning with C:, for example.

The JAR tool will display additional information
if you use the v option:

```

jar tvf TicTacToe.jar

```

For example, the verbose output for the TicTacToe JAR file would look similar to this:

```

 256 Mon Apr 18 10:50:28 PDT 2005 META-INF/MANIFEST.MF
3885 Mon Apr 18 10:49:50 PDT 2005 TicTacToe.class
   0 Wed Apr 20 16:39:32 PDT 2005 audio/
4032 Wed Apr 20 16:39:32 PDT 2005 audio/beep.au
2566 Wed Apr 20 16:39:32 PDT 2005 audio/ding.au
6558 Wed Apr 20 16:39:32 PDT 2005 audio/return.au
7834 Wed Apr 20 16:39:32 PDT 2005 audio/yahoo1.au
7463 Wed Apr 20 16:39:32 PDT 2005 audio/yahoo2.au
   0 Wed Apr 20 16:39:44 PDT 2005 images/
 157 Wed Apr 20 16:39:44 PDT 2005 images/cross.gif
 158 Wed Apr 20 16:39:44 PDT 2005 images/not.gif

```

[« Previous](build.html)
•
[Trail](../TOC.html)
•
[Next »](unpack.html)

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

**Previous page:** Creating a JAR File
  
**Next page:** Extracting the Contents of a JAR File




A browser with JavaScript enabled is required for this page to operate properly.