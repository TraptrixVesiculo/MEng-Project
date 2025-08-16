[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Security Features in Java SE
  
**Lesson:** Quick Tour of Controlling Applets
  
**Section:** Set up a Policy File to Grant the Required Permission

[Quick Tour of Controlling Applets](index.html)

[Observe Applet Restrictions](step1.html)

[Set up a Policy File to Grant the Required Permission](step2.html)

Start Policy Tool

[Grant the Required Permission](wstep2.html)

[Save the Policy File](wstep3.html)

[See the Policy File Effects](step3.html)

[Home Page](../../index.html)
>
[Security Features in Java SE](../index.html)
>
[Quick Tour of Controlling Applets](index.html)

[« Previous](step2.html) • [Trail](../TOC.html) • [Next »](wstep2.html)

# Start Policy Tool

To start Policy Tool, simply type the following at the command line:

```

policytool

```

This brings up the Policy Tool window.

Whenever Policy Tool
is started, it attempts to
fill in this window with policy information from the *user policy file.*
The user policy file is named `.java.policy` by default in your
home directory. If Policy Tool cannot find the user policy file, it issues a warning and displays a blank Policy Tool window
(a window with headings and buttons but no data in it),
as shown in the following figure.

[![the PolicyTool window](../../figures/security/ptBlank1.gif)](../../figures/security/ptBlank1.gif)  
*This figure has been reduced to fit on the page.   
 Click the image to view it at its natural size.*

You can then proceed to either
open an existing policy file
or to create a new policy file.

The first time you run the Policy Tool,
you will see the blank Policy Tool window, since a user
policy file does not yet exist.
You can immediately proceed to create a new policy file,
as described in the next step.

[« Previous](step2.html)
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

**Previous page:** Set up a Policy File to Grant the Required Permission
  
**Next page:** Grant the Required Permission




A browser with JavaScript enabled is required for this page to operate properly.