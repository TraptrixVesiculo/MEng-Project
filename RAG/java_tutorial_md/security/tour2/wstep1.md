[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Security Features in Java SE
  
**Lesson:** Quick Tour of Controlling Applications
  
**Section:** Set up the Policy File to Grant the Required Permissions

[Quick Tour of Controlling Applications](index.html)

[Observe Application Freedom](step1.html)

[See How to Restrict Applications](step2.html)

[Set up the Policy File to Grant the Required Permissions](step3.html)

Open the Policy File

[Grant the Required Permissions](wstep2.html)

[Save the Policy File](wstep3.html)

[See the Policy File Effects](step4.html)

[Home Page](../../index.html)
>
[Security Features in Java SE](../index.html)
>
[Quick Tour of Controlling Applications](index.html)

[« Previous](step3.html) • [Trail](../TOC.html) • [Next »](wstep2.html)

# Open the Policy File

Start Policy Tool by typing the following at the command line:

```

policytool

```

This brings up the Policy Tool window.
To open the `mypolicy` policy file, use
the **Open** command in the **File** menu.
This will present you with an Open dialog, which you can use
to navigate the directory structure until you get to the
directory containing the policy file
(that is, the `C:\Test\` directory).

Choose the `mypolicy` file in that directory and then select
the **Open** button.

This will fill in the Policy Tool window with information
from the `mypolicy` policy file, including the policy file name
and the **CodeBase** part of the policy entry created by the
[Quick Tour of Controlling Applets](../tour1/index.html)
lesson.

[![the PolicyTool window populated with policy file and policy entry](../../figures/security/WQ1ptWithFilename1.gif)](../../figures/security/WQ1ptWithFilename1.gif)  
*This figure has been reduced to fit on the page.   
 Click the image to view it at its natural size.*

[« Previous](step3.html)
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

**Previous page:** Set up the Policy File to Grant the Required Permissions
  
**Next page:** Grant the Required Permissions




A browser with JavaScript enabled is required for this page to operate properly.