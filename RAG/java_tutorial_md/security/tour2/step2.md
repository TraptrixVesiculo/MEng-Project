[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Security Features in Java SE
  
**Lesson:** Quick Tour of Controlling Applications

[Quick Tour of Controlling Applications](index.html)

[Observe Application Freedom](step1.html)

See How to Restrict Applications

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

[« Previous](step1.html) • [Trail](../TOC.html) • [Next »](step3.html)

# See How to Restrict Applications

As you saw in the [previous step](step1.html), the Java runtime does *not* automatically install a Security Manager when it runs an *application*. To apply the same security policy to an application found on the local file
system as to downloaded unsigned applets, you can invoke
the interpreter with the new `-Djava.security.manager`
command line argument.

To execute the `GetProps`
application with the default security manager, type the following:

```

java -Djava.security.manager GetProps

```

Here's the output from the program:

```

C:\TEST>java -Djava.security.manager GetProps
    About to get os.name property value
      The name of your operating system is: WindowsXP
    About to get java.version property value
      The version of the JVM you are running is: JDK 1.6.0
    About to get user.home property value
    Caught exception java.security.AccessControlException:
    access denied (java.util.PropertyPermission user.home read)

```

The process is shown in the following figure.

![the application is prevented from reading the properties](../../figures/security/step3.gif)

  

### Security-Sensitive Properties

> The Java runtime loads a default policy file by default and
> grants all code permission to access some commonly useful properties
> such as `"os.name"` and `"java.version"`.
> These properties are not
> security-sensitive, so granting these permissions does not normally pose a security risk.
>
> The other properties `GetProps` tries to access,
> `"user.home"` and `"java.home"`,
> are *not* among the properties for which
> the system policy file grants read permission. Thus as soon as
> `GetProps` attempts to access the first of these properties
> (`"user.home"`),
> the security manager prevents the access and reports an
> `AccessControlException`.
> This exception indicates that the policy currently in
> effect, which consists of entries in one or more policy files, doesn't allow
> permission to read the `"user.home"` property.

### The Default Policy File

> By default, the system policy file located at:
>
> ```
>
>   Windows:
>     java.home\lib\security\java.policy  
>   UNIX:
>     java.home/lib/security/java.policy  
>
> ```
>
> Note that *java.home* represents the value of the
> `"java.home"`
> property, which is a system property specifying the
> directory into which the JRE was installed.
> Thus if the JRE was installed in the directory named `C:\jdk\jre` on
> Windows and `/jdk/jre` on UNIX,
> the system policy file is located at
>
> ```
>
>   Windows:
>     C:\jdk\jre\lib\security\java.policy  
>   UNIX:
>     /jdk/jre/lib/security/java.policy  
>
> ```
>
> [Here](examples/java.policy)
> is a copy of the default policy file.

[« Previous](step1.html)
•
[Trail](../TOC.html)
•
[Next »](step3.html)

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

**Previous page:** Observe Application Freedom
  
**Next page:** Set up the Policy File to Grant the Required Permissions




A browser with JavaScript enabled is required for this page to operate properly.