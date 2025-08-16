[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Security Features in Java SE
  
**Lesson:** Signing Code and Granting It Permissions

[Signing Code and Granting It Permissions](index.html)

Steps for the Code Signer

[Download and Try the Sample Application](step1.html)

[Create a JAR File Containing the Class File](step2.html)

[Generate Keys](step3.html)

[Sign the JAR File](step4.html)

[Export the Public Key Certificate](step5.html)

[Steps for the Code Receiver](receiver.html)

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

[« Previous](index.html) • [Trail](../TOC.html) • [Next »](step1.html)

# Steps for the Code Signer

The code signer takes the following steps:

1. [Download and Try the Sample Application.](step1.html)

   - [Create a JAR File Containing the
     Class File](step2.html),
     using the `jar` tool.

     - [Generate Keys](step3.html)
       (if they don't already exist),
       using the `keytool` `-genkey` command.

       ---

       *Optional Step* Generate a certificate
       signing request (CSR) for the public key certificate,
       and import the response from the certification authority (CA).
       For simplicity (and since you are only pretending to be Susan Jones),
       this step is omitted. See
       [Generating a Certificate Signing Request (CSR) for a Public Key Certificate](../sigcert/index.html#GenCSR)
       for more information.

       ---

       - [Sign the JAR File](step4.html),
         using the `jarsigner` tool and the private key.

         - [Export the Public Key Certificate](step5.html),
           using the `keytool` `-export` command.
           Then supply the signed JAR file and the
           certificate to the receiver Ray.

These steps are shown in the following figure.

[![Signing Your Code](../../figures/security/susanSigner.gif)](../../figures/security/susanSigner.gif)  
*This figure has been reduced to fit on the page.   
 Click the image to view it at its natural size.*

[« Previous](index.html)
•
[Trail](../TOC.html)
•
[Next »](step1.html)

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

**Previous page:** Signing Code and Granting It Permissions
  
**Next page:** Download and Try the Sample Application




A browser with JavaScript enabled is required for this page to operate properly.