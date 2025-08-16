[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Security Features in Java SE
  
**Lesson:** Quick Tour of Controlling Applications

[Quick Tour of Controlling Applications](index.html)

Observe Application Freedom

[See How to Restrict Applications](step2.html)

[Set up the Policy File to Grant the Required Permissions](step3.html)

[Open the Policy File](wstep1.html)

[Grant the Required Permissions](wstep2.html)

[Save the Policy File](wstep3.html)

[See the Policy File Effects](step4.html)

[Home Page](../../index.html)
>
[Security Features in Java SE](../index.html)
>
[Quick Tour of Controlling Applications](index.html)

[« Previous](index.html) • [Trail](../TOC.html) • [Next »](step2.html)

# Observe Application Freedom

A security manager is *not* automatically installed when an *application* is
running. In the [next step](step3.html), you'll see
how to apply the same security policy to an application found on the local file
system as to downloaded unsigned applets. But first, let's demonstrate that a
security manager is by default not installed for an application, and thus the
application has full access to resources.

Create a file named `GetProps.java`
on your computer by either copying or downloading the
[`GetProps.java`](examples/GetProps.java)
source code.

The examples in this lesson assume that you put `GetProps.java`
in the `C:\Test` directory if you're using a Windows system or in the
`~/test` directory on UNIX.

As you can see if you examine the source file, this program tries to
get (read) the property values, whose names are
`"os.name"` , `"java.version"`,
`"user.home"`, and `"java.home"`.

Now compile and run `GetProps.java`.
You should see output like the following:

```

C:\TEST>java GetProps
    About to get os.name property value
      The name of your operating system is: Windows XP
    About to get java.version property value
      The version of the JVM you are running is: 1.6.0
    About to get user.home property value
      Your user home directory is: C:\WINDOWS
    About to get java.home property value
      Your JRE installation directory is: C:\JDK6.0.0\JRE

```

This shows that the application was allowed to access all the property
values, as shown in the following figure.

![Applicaton can read property values](../../figures/security/step2.gif)

[« Previous](index.html)
•
[Trail](../TOC.html)
•
[Next »](step2.html)

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

**Previous page:** Quick Tour of Controlling Applications
  
**Next page:** See How to Restrict Applications




A browser with JavaScript enabled is required for this page to operate properly.