[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Learning the Java Language
  
**Lesson:** Packages
  
**Section:** Creating and Using Packages

[Packages](index.html)

[Creating and Using Packages](packages.html)

[Creating a Package](createpkgs.html)

[Naming a Package](namingpkgs.html)

[Using Package Members](usepkgs.html)

Managing Source and Class Files

[Summary of Creating and Using Packages](summary-package.html)

[Questions and Exercises](QandE/packages-questions.html)

[Home Page](../../index.html)
>
[Learning the Java Language](../index.html)
>
[Packages](index.html)

[« Previous](usepkgs.html) • [Trail](../TOC.html) • [Next »](summary-package.html)

# Managing Source and Class Files

Many implementations of the Java platform rely on hierarchical
file systems to manage source and class files, although *The
Java Language Specification* does not require this. The strategy
is as follows.

Put the source code for a class, interface, enumeration, or annotation type
in a text
file whose name is the simple name of the type
and whose extension is `.java`. For example:

```

//in the Rectangle.java file 
package graphics;
public class Rectangle {
   . . . 
}

```

Then, put the source file in a directory whose name reflects the name of the package
to which the type belongs:

```

.....\graphics\Rectangle.java

```

The qualified name of the package member and the path name to
the file are parallel, assuming the Microsoft Windows file name separator
backslash (for Unix, use the forward slash).

|  |  |
| --- | --- |
| **class name** | `graphics.Rectangle` |
| **pathname to file** | `graphics\Rectangle.java` |

As you should recall, by convention a company uses its reversed
Internet domain name for its package names. The Example company,
whose Internet domain name is `example.com`, would
precede all its package names with `com.example`.
Each component of the package name corresponds to a subdirectory.
So, if the Example company had a `com.example.graphics` package that contained
a `Rectangle.java`
source file, it would be contained in a series of subdirectories like this:

```

....\com\example\graphics\Rectangle.java

```

When you compile a source file, the compiler creates a different
output file for each type defined in it. The base
name of the output file is the name of the type,
and its extension is `.class`. For example, if the source file is like this

```

//in the Rectangle.java file
package com.example.graphics;
public class Rectangle {
      . . . 
}

class Helper{
      . . . 
}

```

then the compiled files will be located at:

```

<path to the parent directory of the output files>\com\example\graphics\Rectangle.class
<path to the parent directory of the output files>\com\example\graphics\Helper.class

```

Like the `.java` source files, the compiled `.class` files should
be in a series of directories that reflect the package name.
However, the path to the `.class` files does not have to be the same as the path to
the `.java` source files. You can arrange your source and class directories separately,
as:

```

<path_one>\sources\com\example\graphics\Rectangle.java

<path_two>\classes\com\example\graphics\Rectangle.class

```

By doing this, you can give the `classes` directory to other programmers
without revealing your sources.
You also need to manage source and class files in this manner so that
the compiler and the Java Virtual Machine (JVM) can find all
the types your program uses.

The full path to the `classes` directory, `<path_two>\classes`,
is called the *class path*, and is set with
the `CLASSPATH` system variable.
Both the compiler and the JVM construct the path to your `.class` files by adding the package name
to the class path. For example, if

```

<path_two>\classes

```

is your class path, and the package name is

```

com.example.graphics,

```

then the compiler and JVM look for `.class files` in

```

<path_two>\classes\com\example\graphics.

```

A class path may include several paths, separated by a semicolon (Windows) or colon (Unix). By default,
the compiler and the JVM search the current directory and the JAR file
containing the Java platform classes so that these directories are automatically in your class path.

### Setting the CLASSPATH System Variable

To display the current `CLASSPATH` variable, use these commands in Windows and Unix (Bourne shell):

```

In Windows:   C:\> set CLASSPATH
In Unix:      % echo &#36CLASSPATH

```

To delete the current contents of the `CLASSPATH` variable, use these commands:

```

In Windows:   C:\> set CLASSPATH=
In Unix:      % unset CLASSPATH; export CLASSPATH

```

To set the `CLASSPATH` variable, use these commands (for example):

```

In Windows:   C:\> set CLASSPATH=C:\users\george\java\classes
In Unix:      % CLASSPATH=/home/george/java/classes; export CLASSPATH

```

[« Previous](usepkgs.html)
•
[Trail](../TOC.html)
•
[Next »](summary-package.html)

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

**Previous page:** Using Package Members
  
**Next page:** Summary of Creating and Using Packages




A browser with JavaScript enabled is required for this page to operate properly.