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

The Security Manager

[Miscellaneous Methods in System](sysmisc.html)

[PATH and CLASSPATH](paths.html)

[Questions and Exercises](QandE/questions.html)

[Home Page](../../index.html)
>
[Essential Classes](../index.html)
>
[The Platform Environment](index.html)

[« Previous](sysprop.html) • [Trail](../TOC.html) • [Next »](sysmisc.html)

# The Security Manager

A *security manager* is an object that defines a security policy
for an application. This policy specifies actions that are unsafe or
sensitive. Any actions not allowed by the security policy cause a
[`SecurityException`](http://download.oracle.com/javase/7/docs/api/java/lang/SecurityException.html)
to be thrown. An application can also query its security manager to
discover which actions are allowed.

Typically, a web applet runs with a security manager provided by the
browser or Java Web Start plugin. Other kinds of applications normally
run without a security manager, unless the application itself defines
one. If no security manager is present, the application has no
security policy and acts without restrictions.

This section explains how an application interacts with an existing
security manager. For more detailed information, including information
on how to design a security manager, refer to the
[Security Guide](http://download.oracle.com/javase/7/docs/technotes/guides/security/index.html).

### Interacting with the Security Manager

The security manager is an object of type
[`SecurityManager`](http://download.oracle.com/javase/7/docs/api/java/lang/SecurityManager.html); to obtain a reference to this object, invoke
`System.getSecurityManager`.

```

SecurityManager appsm = System.getSecurityManager();

```

If there is no security manager, this method returns
`null`.

Once an application has a reference to the security manager object, it
can request permission to do specific things. Many
classes in the standard libraries do this. For example,
`System.exit`, which terminates the Java virtual machine
with an exit status, invokes `SecurityManager.checkExit`
to ensure that the current thread has permission to shut down the
application.

The SecurityManager class defines many other methods used to verify
other kinds of operations. For example,
`SecurityManager.checkAccess` verifies thread accesses, and
`SecurityManager.checkPropertyAccess` verifies access to
the specified property. Each operation or group of operations has its
own `checkXXX()` method.

In addition, the set of `checkXXX()` methods
represents the set of operations that are already subject to the
protection of the security manager. Typically, an application does
not have to directly invoke any `checkXXX()`
methods.

### Recognizing a Security Violation

Many actions that are routine without a security manager can throw a
`SecurityException` when run with a security manager. This
is true even when invoking a method that isn't documented as throwing
`SecurityException`. For example, consider the following
code used to read a file:

```

reader = new FileReader("xanadu.txt");

```

In the absence of a security manager, this statement executes without
error, provided `xanadu.txt` exists and is readable. But
suppose this statement is inserted in a web applet, which typically
runs under a security manager that does not allow file input. The
following error messages might result:

```

appletviewer fileApplet.html
Exception in thread "AWT-EventQueue-1" java.security.AccessControlException: access denied (java.io.FilePermission characteroutput.txt write)
	at java.security.AccessControlContext.checkPermission(AccessControlContext.java:323)
	at java.security.AccessController.checkPermission(AccessController.java:546)
	at java.lang.SecurityManager.checkPermission(SecurityManager.java:532)
	at java.lang.SecurityManager.checkWrite(SecurityManager.java:962)
	at java.io.FileOutputStream.(FileOutputStream.java:169)
	at java.io.FileOutputStream.(FileOutputStream.java:70)
	at java.io.FileWriter.(FileWriter.java:46)
...

```

Note that the specific exception thrown in this case,
[`java.security.AccessControlException`](http://download.oracle.com/javase/7/docs/api/java/security/AccessControlException.html), is a subclass of `SecurityException`.

[« Previous](sysprop.html)
•
[Trail](../TOC.html)
•
[Next »](sysmisc.html)

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

**Previous page:** System Properties
  
**Next page:** Miscellaneous Methods in System




A browser with JavaScript enabled is required for this page to operate properly.