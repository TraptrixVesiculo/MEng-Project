[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Essential Classes
  
**Lesson:** The Platform Environment

[The Platform Environment](../index.html)

[Configuration Utilities](../config.html)

[Properties](../properties.html)

[Command-Line Arguments](../cmdLineArgs.html)

[Environment Variables](../env.html)

[Other Configuration Utilities](../other.html)

[System Utilities](../system.html)

[Command-Line I/O Objects](../cl.html)

[System Properties](../sysprop.html)

[The Security Manager](../security.html)

[Miscellaneous Methods in System](../sysmisc.html)

[PATH and CLASSPATH](../paths.html)

Questions and Exercises

[Home Page](../../../index.html)
>
[Essential Classes](../../index.html)
>
[The Platform Environment](../index.html)

[« Previous](../paths.html) • [Trail](../../TOC.html) • [Next »](../../regex/index.html)

# Questions and Exercises: The Platform Environment

### Questions

> 1. A programmer installs a new library contained in a .jar file.
> In order to access the library from his code, he sets the CLASSPATH
> environment variable to point to the new .jar file. Now he finds
> that he gets an error message when he tries to launch simple
> applications:
>
> ```
>
> java Hello
> Exception in thread "main" java.lang.NoClassDefFoundError: Hello
>
> ```
>
> In this case, the `Hello` class is compiled into a .class
> file in the current directory — yet the `java`
> command can't seem to find it. What's going wrong?

### Exercises

> 1. Write an application, `PersistentEcho`, with the
> following features:
>
> * If `PersistentEcho` is run with command line
>   arguments, it prints out those arguments. It also saves the
>   string printed out to a property, and saves the property to a
>   file called `PersistentEcho.txt`* If `PersistentEcho` is run with no command line
>     arguments, it looks for an environment variable called
>     PERSISTENTECHO. If that variable exists,
>     `PersistentEcho` prints out its value, and also saves the
>     value in the same way it does for command line arguments.* If `PersistentEcho` is run with no command line
>       arguments, and the PERSISTENTECHO environment variable is not
>       defined, it retrieves the property value from
>       `PersistentEcho.txt` and prints that out.
>
> [Check your answers.](answers.html)

[« Previous](../paths.html)
•
[Trail](../../TOC.html)
•
[Next »](../../regex/index.html)

---

Problems with the examples? Try [Compiling and Running
the Examples: FAQs](../../../information/run-examples.html).
  
Complaints? Compliments? Suggestions? [Give
us your feedback](http://download.oracle.com/javase/feedback.html).

Your use of this page and all the material on pages under "The Java Tutorials" banner,
and all the material on pages under "The Java Tutorials" banner is subject to the [Java SE Tutorial Copyright
and License](../../../information/license.html).
Additionally, any example code contained in any of these Java
Tutorials pages is licensed under the
[Code
Sample License](http://developers.sun.com/license/berkeley_license.html).

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| |  |  | | --- | --- | | duke image | Oracle logo | | [About Oracle](http://www.oracle.com/us/corporate/index.html) | [Oracle Technology Network](http://www.oracle.com/technology/index.html) | [Terms of Service](https://www.samplecode.oracle.com/servlets/CompulsoryClickThrough?type=TermsOfService) | Copyright © 1995, 2011 Oracle and/or its affiliates. All rights reserved. |

**Previous page:** PATH and CLASSPATH
  
**Next page:** Regular Expressions




A browser with JavaScript enabled is required for this page to operate properly.