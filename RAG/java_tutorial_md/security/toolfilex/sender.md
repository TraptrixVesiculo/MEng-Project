[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Security Features in Java SE
  
**Lesson:** Exchanging Files

[Exchanging Files](index.html)

Steps for the Contract Sender

[Create a JAR File Containing the Contract](step1.html)

[Generate Keys](step2.html)

[Sign the JAR File](step3.html)

[Export the Public Key Certificate](step4.html)

[Steps for the Contract Receiver](receiver.html)

[Import the Certificate as a Trusted Certificate](rstep1.html)

[Verify the JAR File Signature](rstep2.html)

[Home Page](../../index.html)
>
[Security Features in Java SE](../index.html)
>
[Exchanging Files](index.html)

[« Previous](index.html) • [Trail](../TOC.html) • [Next »](step1.html)

# Steps for the Contract Sender

The steps outlined here for the contract
sender are *basically the same*
as those listed for a code signer in the
[Signing Code and Granting It Permissions](../toolsign/index.html)
lesson. Here, however, you are pretending to be Stan Smith
rather than Susan Jones and are storing a data file
rather than a class file in the JAR file to be signed.

The steps you take as the contract sender are as follows.

1. [Create a JAR File Containing the Contract](step1.html),
   using the `jar` tool.

   - [Generate Keys](step2.html)
     (if they don't already exist),
     using the `keytool` `-genkey` command.

     *Optional Step*: Generate a certificate
     signing request (CSR) for the public key certificate,
     and import the response from the certification authority.
     For simplicity and since you are only pretending to be Stan Smith,
     this step is omitted. See
     [Generating a Certificate Signing Request (CSR) for a Public Key Certificate](../sigcert/index.html#GenCSR)
     for more information.

     - [Sign the JAR File](step3.html),
       using the `jarsigner` tool and the private key generated in step 2.

       - [Export the Public Key Certificate](step4.html),
         using the `keytool` `-export` command.
         Then supply the signed JAR file and the
         certificate to the receiver, Ruth.

[![Steps for the Contract Sender](../../figures/security/stanSender.gif)](../../figures/security/stanSender.gif)  
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

**Previous page:** Exchanging Files
  
**Next page:** Create a JAR File Containing the Contract




A browser with JavaScript enabled is required for this page to operate properly.