[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Security Features in Java SE
  
**Lesson:** Quick Tour of Controlling Applications

[Quick Tour of Controlling Applications](index.html)

[Observe Application Freedom](step1.html)

[See How to Restrict Applications](step2.html)

Set up the Policy File to Grant the Required Permissions

[Open the Policy File](wstep1.html)

[Grant the Required Permissions](wstep2.html)

[Save the Policy File](wstep3.html)

[See the Policy File Effects](step4.html)

[Home Page](../../index.html)
>
[Security Features in Java SE](../index.html)
>
[Quick Tour of Controlling Applications](index.html)

[« Previous](step2.html) • [Trail](../TOC.html) • [Next »](wstep1.html)

# Set up the Policy File to Grant the Required Permissions

This step uses the Policy Tool utility to open the policy file
named **`mypolicy`** created in the
[Quick Tour of Controlling Applets](../tour1/index.html)
lesson. You will add a new policy entry
granting permission for code from the
directory where `GetProps.class` is stored
to read the `"user.home"` and the
`"java.home"` property values,
as shown in the following figure.

![The mypolicy policy file grants WriteFile and GetProps the permissions they need  ](../../figures/security/step4.gif)

The steps are as follows.

1. [Open the Policy File](wstep1.html)

   - [Grant the Required Permissions](wstep2.html)

     - [Save the Policy File](wstep3.html)

---

**Note for UNIX Users:**  The instructions illustrate creating
the policy file for a Windows system.
The steps are exactly the same if you are working on a UNIX system,
with the following differences.

* You
  retrieve the `mypolicy` file from the `test` directory in your
  home directory.

  * For the **CodeBase** URL in the step for granting the
    required permissions, you can substitute
    `file:${user.home}/test/` for
    `file:/C:/Test/`.
    Alternatively you could directly specify your home directory
    rather than referring to the `"user.home"` property,
    as in `file:/home/susanj/test/`.

---

[« Previous](step2.html)
•
[Trail](../TOC.html)
•
[Next »](wstep1.html)

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

**Previous page:** See How to Restrict Applications
  
**Next page:** Open the Policy File




A browser with JavaScript enabled is required for this page to operate properly.