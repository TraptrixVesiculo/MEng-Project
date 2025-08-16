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

Setting an Application's Entry Point

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

[« Previous](modman.html) • [Trail](../TOC.html) • [Next »](downman.html)

# Setting an Application's Entry Point

If you have an application bundled in a JAR file, you need some
way to indicate which class within the JAR file is your application's
entry point. You provide this information with the `Main-Class`
header in the manifest, which has the general form:

```

Main-Class: classname

```

The value *`classname`* is the name of the class that
is your application's entry point.

Recall that the entry point is a class having a method with
signature `public static void main(String[] args)`.

After you have set the `Main-Class` header in the manifest,
you then run the JAR file using the following form of the `java`
command:

```

java -jar JAR-name

```

The `main` method of the class specified in the
`Main-Class` header is executed.

## An Example

We want to execute the `main` method in the class
`MyClass` in the package `MyPackage`
when we run the JAR file.

We first create a text file named `Manifest.txt`
with the following contents:

```

Main-Class: MyPackage.MyClass

```

---

**Warning:** The text file must end with a new line or carriage return.
The last line will not be parsed properly if it does not
end with a new line or carriage return.

---

We then create a JAR file named `MyJar.jar` by entering
the following command:

```

jar cfm MyJar.jar Manifest.txt MyPackage/*.class

```

This creates the JAR file with a manifest with the following contents:

```

Manifest-Version: 1.0
Created-By: 1.6.0 (Sun Microsystems Inc.)
Main-Class: MyPackage.MyClass

```

When you run the JAR file with the following command, the `main`
method of `MyClass` executes:

```

java -jar MyJar.jar

```

## Setting an Entry Point with the JAR Tool

The 'e' flag (for 'entrypoint'), introduced in JDK 6,
creates or overrides the manifest's `Main-Class` attribute.
It can be used while creating or updating a jar file.
Use it to specify the application entry point without editing or
creating the manifest file.
For example, this command creates `app.jar` where the
`Main-Class` attribute value in the manifest is set to
`MyApp`:

```

jar cfe app.jar MyApp MyApp.class

```

You can directly invoke this application by running the following command:

```

java -jar app.jar
```

If the entrypoint class name is in a package it may use a '.' (dot)
character as the delimiter.
For example, if `Main.class` is in a package called
`foo` the entry point can be specified in the following ways:

```

jar cfe Main.jar foo.Main foo/Main.class
```

[« Previous](modman.html)
•
[Trail](../TOC.html)
•
[Next »](downman.html)

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

**Previous page:** Modifying a Manifest File
  
**Next page:** Adding Classes to the JAR File's Classpath




A browser with JavaScript enabled is required for this page to operate properly.