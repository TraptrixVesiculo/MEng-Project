[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

The Platform Environment

[Configuration Utilities](config.html)

[Properties](properties.html)

[Command-Line Arguments](cmdLineArgs.html)

[Environment Variables](env.html)

[Other Configuration Utilities](other.html)

[System Utilities](system.html)

[Command-Line I/O Objects](cl.html)

[System Properties](sysprop.html)

[The Security Manager](security.html)

[Miscellaneous Methods in System](sysmisc.html)

[PATH and CLASSPATH](paths.html)

[Questions and Exercises](QandE/questions.html)

**Trail:** Essential Classes

[Home Page](../../index.html)
>
[Essential Classes](../index.html)

[« Previous](../concurrency/index.html) • [Trail](../TOC.html) • [Next »](config.html)

# Lesson: The Platform Environment

An application runs in a *platform environment*, defined by the
underlying operating system, the Java virtual machine, the class
libraries, and various configuration data supplied when the
application is launched. This lesson describes some of the APIs an
application uses to examine and configure its platform environment.
The lesson consists of three sections:

* [Configuration Utilities](config.html) describes APIs
  used to access configuration data supplied when the application is
  deployed, or by the application's user.* [System Utilities](system.html) describes
    miscellaneous APIs defined in the `System` and
    `Runtime` classes.* [PATH and CLASSPATH](paths.html) describes
      environment variables used to configure JDK development tools and
      other applications.

[« Previous](../concurrency/index.html)
•
[Trail](../TOC.html)
•
[Next »](config.html)

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

**Previous page:** Previous Lesson
  
**Next page:** Configuration Utilities




A browser with JavaScript enabled is required for this page to operate properly.