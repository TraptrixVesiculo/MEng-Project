[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Essential Classes
  
**Lesson:** The Platform Environment
  
**Section:** Configuration Utilities

[The Platform Environment](index.html)

[Configuration Utilities](config.html)

[Properties](properties.html)

[Command-Line Arguments](cmdLineArgs.html)

[Environment Variables](env.html)

Other Configuration Utilities

[System Utilities](system.html)

[Command-Line I/O Objects](cl.html)

[System Properties](sysprop.html)

[The Security Manager](security.html)

[Miscellaneous Methods in System](sysmisc.html)

[PATH and CLASSPATH](paths.html)

[Questions and Exercises](QandE/questions.html)

[Home Page](../../index.html)
>
[Essential Classes](../index.html)
>
[The Platform Environment](index.html)

[« Previous](env.html) • [Trail](../TOC.html) • [Next »](system.html)

# Other Configuration Utilities

Here is a summary of some other configuration utilities.

The *Preferences API* allows applications to store and retrieve
configuration data in an implementation-dependent backing store.
Asynchronous updates are supported, and the same set of preferences
can be safely updated by multiple threads and even multiple
applications. For more information, refer to the
[Preferences API Guide](http://java.sun.com/javase/6/docs/technotes/guides/preferences/index.html).

An application deployed in a *JAR archive* uses a *manifest*
to describe the contents of the archive. For more information, refer to
the
[Packaging Programs in JAR Files](../../deployment/jar/index.html)
lesson.

The configuration of a *Java Web Start application* is contained in a
*JNLP file*. For more information, refer to the
[Java Web Start](../../deployment/webstart/index.html)
lesson.

The configuration of a *Java Plug-in applet* is partially
determined by the HTML tags used to embed the applet in the web page.
Depending on the applet and the browser, these tags can include
`<applet>`, `<object>`,
`<embed>`, and `<param>`. For more
information, refer to the
[Applets](../../deployment/applet/index.html)
lesson.

The class
[`java.util.ServiceLoader`](http://download.oracle.com/javase/7/docs/api/java/util/ServiceLoader.html)
provides a simple *service provider* facility. A service
provider is an implementation of a *service* — a well-known set
of interfaces and (usually abstract) classes. The classes in a service
provider typically implement the interfaces and
subclass the classes defined in the service. Service providers
can be installed as extensions (see
[The Extension Mechanism](../../ext/index.html)).
Providers can also be made available by adding
them to the class path or by some other
platform-specific means.

[« Previous](env.html)
•
[Trail](../TOC.html)
•
[Next »](system.html)

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

**Previous page:** Environment Variables
  
**Next page:** System Utilities




A browser with JavaScript enabled is required for this page to operate properly.