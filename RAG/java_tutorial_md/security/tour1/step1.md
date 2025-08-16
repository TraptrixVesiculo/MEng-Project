[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Security Features in Java SE
  
**Lesson:** Quick Tour of Controlling Applets

[Quick Tour of Controlling Applets](index.html)

Observe Applet Restrictions

[Set up a Policy File to Grant the Required Permission](step2.html)

[Start Policy Tool](wstep1.html)

[Grant the Required Permission](wstep2.html)

[Save the Policy File](wstep3.html)

[See the Policy File Effects](step3.html)

[Home Page](../../index.html)
>
[Security Features in Java SE](../index.html)
>
[Quick Tour of Controlling Applets](index.html)

[« Previous](index.html) • [Trail](../TOC.html) • [Next »](step2.html)

# Observe Applet Restrictions

The Java Plug-in uses a Security Manager to keep viruses
from accessing your computer through an applet. No unsigned
applet is allowed to access a resource unless the Security
Manager finds that permission has been explicitly granted to
access that system resource. That permission is granted by an
entry in a policy file.

[`Here's the source code`](examples/WriteFile.java) for an applet named `WriteFile` that tries to create and
to write to a file named `writetest` in the current directory.
This applet will not be able to create the file
unless it has explicit permission in a policy file.

Type this command in your command window:

```

appletviewer http://download.oracle.com/javase/tutorial/security/tour1/examples/WriteFile.html

```

Type this command on a single line, without spaces in the URL.

You should see a message about a security exception,
as shown in the following figure. This is the expected
behavior; the system caught the applet trying to access a resource it does not have permission to access.

![WriteFile doesn't have permission to write to writetest](../../figures/security/step1.gif)

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

**Previous page:** Quick Tour of Controlling Applets
  
**Next page:** Set up a Policy File to Grant the Required Permission




A browser with JavaScript enabled is required for this page to operate properly.