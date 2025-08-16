[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Essential Classes
  
**Lesson:** The Platform Environment
  
**Section:** System Utilities

[The Platform Environment](index.html)

[Configuration Utilities](config.html)

[Properties](properties.html)

[Command-Line Arguments](cmdLineArgs.html)

[Environment Variables](env.html)

[Other Configuration Utilities](other.html)

[System Utilities](system.html)

[Command-Line I/O Objects](cl.html)

[System Properties](sysprop.html)

[The Security Manager](security.html)

Miscellaneous Methods in System

[PATH and CLASSPATH](paths.html)

[Questions and Exercises](QandE/questions.html)

[Home Page](../../index.html)
>
[Essential Classes](../index.html)
>
[The Platform Environment](index.html)

[« Previous](security.html) • [Trail](../TOC.html) • [Next »](paths.html)

# Miscellaneous Methods in System

This section describes some of the methods in `System` that
aren't covered in the previous sections.

The `arrayCopy` method efficiently copies data between
arrays. For more information, refer to
[Arrays](../../java/nutsandbolts/arrays.html)
in the
[Language Basics](../../java/nutsandbolts/index.html)
lesson.

The
[`currentTimeMillis`](http://download.oracle.com/javase/7/docs/api/java/lang/System.html#currentTimeMillis())
and
[`nanoTime`](http://download.oracle.com/javase/7/docs/api/java/lang/System.html#nanoTime())
methods are useful for measuring time intervals during execution of an
application. To measure a time interval in milliseconds, invoke
`currentTimeMillis` twice, at the beginning and end of the
interval, and subtract the first value returned from the second.
Similarly, invoking `nanoTime` twice measures an interval
in nanoseconds.

---

**NOTE:** The accuracy of both `currentTimeMillis` and
`nanoTime` is limited by the time services provided by the
operating system. Do not assume that
`currentTimeMillis` is accurate to the nearest millisecond
or that `nanoTime` is accurate to the nearest nanosecond.
Also, neither `currentTimeMillis` nor `nanoTime`
should be used to determine the current time. Use a high-level
method, such as
[`java.util.Calendar.getInstance`](http://download.oracle.com/javase/7/docs/api/java/util/Calendar.html#getInstance()).

---

The
[`exit`](http://download.oracle.com/javase/7/docs/api/java/lang/System.html#exit(int))
method causes the Java virtual machine to shut down, with an integer exit
status specified by the argument. The exit status is available to the
process that launched the application. By convention, an exit status of
`0` indicates normal termination of the application, while
any other value is an error code.

[« Previous](security.html)
•
[Trail](../TOC.html)
•
[Next »](paths.html)

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

**Previous page:** The Security Manager
  
**Next page:** PATH and CLASSPATH




A browser with JavaScript enabled is required for this page to operate properly.