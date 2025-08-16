[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Security Features in Java SE
  
**Lesson:** Signing Code and Granting It Permissions

[Signing Code and Granting It Permissions](index.html)

[Steps for the Code Signer](signer.html)

[Download and Try the Sample Application](step1.html)

[Create a JAR File Containing the Class File](step2.html)

[Generate Keys](step3.html)

[Sign the JAR File](step4.html)

[Export the Public Key Certificate](step5.html)

Steps for the Code Receiver

[Observe the Restricted Application](rstep1.html)

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

[« Previous](step5.html) • [Trail](../TOC.html) • [Next »](rstep1.html)

# Steps for the Code Receiver

In this lesson, you will act as the receiver of the signed jar file containing the `count.class` file. It was signed by Susan. It requests access to your system resources on your system that it normally would not have permission to access.

This procedure requires you to perform the following steps listed below. See the figure below for a flowchart.

1. [Observe the Restricted Application](rstep1.html). This application will not be able to access your system resources until you import Susan's certificate and create a policy file.

   - [Import Susan's certificate as a trusted certificate](rstep2.html)
     using the `keytool -import` command, and give it the alias `susan`.

     - [Set up a policy file
       to grant permission](rstep3.html) for the `count` application signed by `susan` to read the specified file on your system.

       - [Test your reconfigured `count` application](rstep4.html) to verify that with a trusted certificate and access to your new policy file that grants it permission to read files on your system, `count` can now read your `data` file.

[![Steps for Receiving Code](../../figures/security/rayReceiver.gif)](../../figures/security/rayReceiver.gif)  
*This figure has been reduced to fit on the page.   
 Click the image to view it at its natural size.*

[« Previous](step5.html)
•
[Trail](../TOC.html)
•
[Next »](rstep1.html)

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

**Previous page:** Export the Public Key Certificate
  
**Next page:** Observe the Restricted Application




A browser with JavaScript enabled is required for this page to operate properly.