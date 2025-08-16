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

[Extracting the Contents of a JAR File](unpack.html)

[Updating a JAR File](update.html)

Running JAR-Packaged Software

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

[« Previous](update.html) • [Trail](../TOC.html) • [Next »](manifestindex.html)

# Running JAR-Packaged Software

Now that you've learned how to create JAR files, how do you
actually run the code that you've packaged? Consider these
three scenarios:

* Your JAR file contains an applet that is to be run inside
  a browser.* Your JAR file contains an application that is to be invoked
    from the command line.* Your JAR file contains code that you want to use as an
      extension.

This section will cover the first two situations. A separate trail
in the tutorial on the
[extension mechanism](../../ext/index.html) covers the use of JAR files as extensions.

## Applets Packaged in JAR Files

To invoke any applet from an HTML file for running inside a browser,
you need to use the APPLET tag.
For more information, see the
[Applets](../applet/index.html) lesson.
If the applet is bundled as a JAR file, the only thing you need to
do differently is to use the *ARCHIVE* parameter to specify
the relative path to the JAR file.

As an example, let's use (again!) the TicTacToe demo applet that
ships with the Java™ Development Kit.
The APPLET tag in the HTML file that calls the demo looks like this:

```

<applet code=TicTacToe.class 
        width=120 height=120>
</applet>

```

If the TicTacToe demo were packaged in a JAR file named
TicTacToe.jar,
you could modify the APPLET tag with the simple addition of an
ARCHIVE parameter:

```

<applet code=TicTacToe.class 
        archive="TicTacToe.jar"
        width=120 height=120>
</applet>

```

The ARCHIVE parameter specifies the relative path to the JAR file that
contains TicTacToe.class. This example assumes that
the JAR file and the HTML file are in the same directory. If they're
not, you would need to include the JAR file's relative path in the
ARCHIVE parameter's value. For example, if the JAR file was one directory
below the HTML file in a directory called applets, the APPLET
tag would look like this:

```

<applet code=TicTacToe.class 
        archive="applets/TicTacToe.jar"
        width=120 height=120>
</applet>

```

## JAR Files as Applications

You can run JAR-packaged applications with the Java interpreter. The basic command is:

```

java -jar jar-file

```

The -jar flag tells the interpreter
that the application is packaged in the JAR file format. You can only specify one JAR file, which must contain all the application-specific code.

Before you execute this command make sure the runtime environment has an information of which class within the JAR file is the application's entry point.

To indicate which class is the application's entry point,
you must add a Main-Class header to the JAR file's
manifest.
The header takes the form:

```

Main-Class: classname

```

The header's value, classname, is the name of the class that's
the application's entry point.

For more information, see the
[Setting an Application's Entry Point](appman.html) section.

When the Main-Class is set in the manifest file, you can run the application from the command line:

```

java -jar app.jar

```

To run the application from jar file that is in other directory, we need to specify the path of that directory as below:
`java -jar path/app.jar`

where `path` is the directory path at which this `app.jar` resides.

[« Previous](update.html)
•
[Trail](../TOC.html)
•
[Next »](manifestindex.html)

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

**Previous page:** Updating a JAR File
  
**Next page:** Working with Manifest Files: The Basics




A browser with JavaScript enabled is required for this page to operate properly.