[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Deployment
  
**Lesson:** Packaging Programs in JAR Files
  
**Section:** Using JAR-related APIs

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

[Verifying Signed JAR Files](verify.html)

[Using JAR-related APIs](apiindex.html)

[The JarClassLoader Class](jarclassloader.html)

The JarRunner Class

[Questions and Exercises](QandE/questions.html)

[Home Page](../../index.html)
>
[Deployment](../index.html)
>
[Packaging Programs in JAR Files](index.html)

[« Previous](jarclassloader.html) • [Trail](../TOC.html) • [Next »](QandE/questions.html)

# The JarRunner Class

The JarRunner application is launched with a command of this form:

```

java JarRunner url [arguments]

```

In the previous section, we've seen how JarClassLoader
is able to identify and load the main class of a JAR-bundled
application from a given URL. To complete the JarRunner application,
therefore, we need to be able to take a URL and any arguments from the
command line, and pass them to an instance of JarClassLoader.
These tasks belong to the JarRunner class, the entry point
of the JarRunner application.

It begins by creating a java.net.URL object from the URL
specified on the command line:

```

public static void main(String[] args) {
    if (args.length < 1) {
        usage();
    }
    URL url = null;
    try {
        url = new URL(args[0]);
    } catch (MalformedURLException e) {
        fatal("Invalid URL: " + args[0]);
    }
    ...

```

If args.length < 1, that means no URL was specified
on the command line, so a usage message is printed. If the first
command-line argument is a good URL, a new URL object
is created to represent it.

Next, JarRunner creates a new instance of JarClassLoader,
passing to the constructor the URL that was specified on the
command-line:

```

JarClassLoader cl = new JarClassLoader(url);

```

As we saw in the previous section, it's through
JarClassLoader that JarRunner taps into the
JAR-handling APIs.

The URL that's passed to the JarClassLoader constructor is
the URL of the JAR-bundled application that you want to run.
JarRunner next calls the class loader's getMainClassName
method to identify the entry-point class for the application:

```

String name = null;
try {
    name = cl.getMainClassName();
} catch (IOException e) {
    System.err.println("I/O error while loading JAR file:");
    e.printStackTrace();
    System.exit(1);
}
if (name == null) {
    fatal("Specified jar file does not contain a 'Main-Class'" +
          " manifest attribute");
}

```

The key statement is highlighted in bold. The other statements
are for error handling.

Once JarRunner has identified the application's entry-point
class, only two steps remain: passing any arguments to the
application and actually launching the application. JarRunner
performs these steps with this code:

```

// Get arguments for the application
String[] newArgs = new String[args.length - 1];
System.arraycopy(args, 1, newArgs, 0, newArgs.length);
// Invoke application's main class
try {
    cl.invokeClass(name, newArgs);
} catch (ClassNotFoundException e) {
    fatal("Class not found: " + name);
} catch (NoSuchMethodException e) {
    fatal("Class does not define a 'main' method: " + name);
} catch (InvocationTargetException e) {
    e.getTargetException().printStackTrace();
    System.exit(1);
}

```

Recall that the first command-line argument was the URL of
the JAR-bundled application. Any arguments to be passed to
that application are therefore in element 1 and
beyond in the args array. JarRunner takes
those elements, and creates a new array called newArgs
to pass to the application (bold line above).
JarRunner then passes the entry-point's class name and
the new argument list to the invokeClass method of
JarClassLoader. As we saw in the previous section,
invokeClass will load the application's entry-point
class, pass it any arguments, and launch the application.

[« Previous](jarclassloader.html)
•
[Trail](../TOC.html)
•
[Next »](QandE/questions.html)

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

**Previous page:** The JarClassLoader Class
  
**Next page:** Questions and Exercises: JAR




A browser with JavaScript enabled is required for this page to operate properly.