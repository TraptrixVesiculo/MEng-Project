[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Security Features in Java SE
  
**Lesson:** Quick Tour of Controlling Applets

[Quick Tour of Controlling Applets](index.html)

[Observe Applet Restrictions](step1.html)

Set up a Policy File to Grant the Required Permission

[Start Policy Tool](wstep1.html)

[Grant the Required Permission](wstep2.html)

[Save the Policy File](wstep3.html)

[See the Policy File Effects](step3.html)

[Home Page](../../index.html)
>
[Security Features in Java SE](../index.html)
>
[Quick Tour of Controlling Applets](index.html)

[« Previous](step1.html) • [Trail](../TOC.html) • [Next »](wstep1.html)

# Set up a Policy File to Grant the Required Permission

A policy file is an ASCII text file and can be composed via a text editor
or the graphical Policy Tool utility demonstrated in this section.
The Policy Tool saves you typing and eliminates the need
for you to know the required syntax of policy files, thus
reducing errors.

This lesson uses the Policy Tool to create a policy file
named **`mypolicy`**, in which you will add
a *policy entry* that grants code from the
directory where `WriteFile.class` is stored
permission to write the
`writetest` file.

Follow these steps to create and modify your new policy file:

1. [Start Policy Tool](wstep1.html)

   - [Grant the Required Permission](wstep2.html)

     - [Save the Policy File](wstep3.html)

---

**Note for UNIX Users:**  The steps illustrate creating
the policy file for a Windows system.
The steps are exactly the same if you are working on a UNIX system.
Where the text says to store the policy file in the `C:\Test` directory,
you can store it in another directory. The examples in the step
[See the Policy File Effects](step3.html)
and in the lesson
[Quick Tour of Controlling Applications](../tour2/index.html)
assume that you stored it in the `~/test` directory.

---

[« Previous](step1.html)
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

**Previous page:** Observe Applet Restrictions
  
**Next page:** Start Policy Tool




A browser with JavaScript enabled is required for this page to operate properly.