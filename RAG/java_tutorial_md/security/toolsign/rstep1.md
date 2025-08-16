[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Security Features in Java SE
  
**Lesson:** Signing Code and Granting It Permissions
  
**Section:** Steps for the Code Receiver

[Signing Code and Granting It Permissions](index.html)

[Steps for the Code Signer](signer.html)

[Download and Try the Sample Application](step1.html)

[Create a JAR File Containing the Class File](step2.html)

[Generate Keys](step3.html)

[Sign the JAR File](step4.html)

[Export the Public Key Certificate](step5.html)

[Steps for the Code Receiver](receiver.html)

Observe the Restricted Application

[Import the Certificate as a Trusted Certificate](rstep2.html)

[Set Up a Policy File to Grant the Required Permission](rstep3.html)

[Start Policy Tool](wstep1.html)

[Specify the Keystore](wstep2.html)

[Add a Policy Entry with a SignedBy Alias](wstep3.html)

[Save the Policy File](wstep4.html)

[See the Policy File Effects](rstep4.html)

[Home Page](../../index.html)
>
[Security Features in Java SE](../index.html)
>
[Signing Code and Granting It Permissions](index.html)

[« Previous](receiver.html) • [Trail](../TOC.html) • [Next »](rstep2.html)

# Observe the Restricted Application

The last part of the
[Quick Tour of Controlling Applications](../tour2/index.html)
lesson shows how an application
can be run under a security manager by
invoking the interpreter with the new
`-Djava.security.manager` command-line argument.
But what if the application to be invoked resides inside a JAR file?

One of the interpreter options is the `-cp`
(for class path) option,
that lets you specify a search path for application classes and resources.
Therefore, to execute the `Count` application inside the
`sCount.jar` JAR file, specifying the file
`C:\TestData\data` as its argument, you can type
the following command while in the directory containing
`sCount.jar`:

```

java -cp sCount.jar Count C:\TestData\data

```

To execute the application with a security manager, add
`-Djava.security.manager`, as shown below:

```

java -Djava.security.manager -cp sCount.jar Count C:\TestData\data

```

---

**Important:**  When you run this command, your Java interpreter will throw an exception shown below:

```

Exception in thread "main" java.security.AccessControlException:
access denied (java.io.FilePermission C:\TestData\data read)
    at java.security.AccessControlContext.checkPermission(Compiled Code)
    at java.security.AccessController.checkPermission(Compiled Code)
    at java.lang.SecurityManager.checkPermission(Compiled Code)
    at java.lang.SecurityManager.checkRead(Compiled Code)
    at java.io.FileInputStream.(Compiled Code)
    at Count.main(Compiled Code)

```

In this example, `AccessControlException` reported that
the `count` application does not have permission to
read the file `C:\TestData\data`. Your interpreter raised this exception because it will not allow any application running under a security manager to
read a file or to access other resources unless it has explicit permission to do so -- usually specified in a `grant` statement contained in a `policy` file.

---

[« Previous](receiver.html)
•
[Trail](../TOC.html)
•
[Next »](rstep2.html)

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

**Previous page:** Steps for the Code Receiver
  
**Next page:** Import the Certificate as a Trusted Certificate




A browser with JavaScript enabled is required for this page to operate properly.