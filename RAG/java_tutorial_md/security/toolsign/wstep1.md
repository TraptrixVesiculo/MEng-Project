[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Security Features in Java SE
  
**Lesson:** Signing Code and Granting It Permissions
  
**Section:** Steps for the Code Receiver
  
**Subsection:** Set Up a Policy File to Grant the Required Permission

[Signing Code and Granting It Permissions](index.html)

[Steps for the Code Signer](signer.html)

[Download and Try the Sample Application](step1.html)

[Create a JAR File Containing the Class File](step2.html)

[Generate Keys](step3.html)

[Sign the JAR File](step4.html)

[Export the Public Key Certificate](step5.html)

[Steps for the Code Receiver](receiver.html)

[Observe the Restricted Application](rstep1.html)

[Import the Certificate as a Trusted Certificate](rstep2.html)

[Set Up a Policy File to Grant the Required Permission](rstep3.html)

Start Policy Tool

[Specify the Keystore](wstep2.html)

[Add a Policy Entry with a SignedBy Alias](wstep3.html)

[Save the Policy File](wstep4.html)

[See the Policy File Effects](rstep4.html)

[Home Page](../../index.html)
>
[Security Features in Java SE](../index.html)
>
[Signing Code and Granting It Permissions](index.html)

[« Previous](rstep3.html) • [Trail](../TOC.html) • [Next »](wstep2.html)

# Start Policy Tool

To start Policy Tool, simply type the following at the command line:

```

policytool

```

This brings up the Policy Tool window. Whenever Policy Tool
is started, it tries to
fill in this window with policy information from what is sometimes referred to
as the "user policy file," which by default is a
file named `.java.policy` in your
home directory. If Policy Tool cannot find the user policy file, it reports
the situation and displays a blank Policy Tool window
(that is, a window with headings and buttons but no data in it, as
shown in the following figure.

[![a blank Policy Tool window](../../figures/security/ptBlank1.gif)](../../figures/security/ptBlank1.gif)  
*This figure has been reduced to fit on the page.   
 Click the image to view it at its natural size.*

You will create and work on a policy file other than the user policy file,
since the lessons of this trail don't expect modifications to be made to your
official user policy file.

Assuming that you see the blank Policy Tool window (if not, select
**New** in the **File** menu), you can immediately
proceed to create a new policy file.

[« Previous](rstep3.html)
•
[Trail](../TOC.html)
•
[Next »](wstep2.html)

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

**Previous page:** Set Up a Policy File to Grant the Required Permission
  
**Next page:** Specify the Keystore




A browser with JavaScript enabled is required for this page to operate properly.