[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Security Features in Java SE
  
**Lesson:** Exchanging Files

[Exchanging Files](index.html)

[Steps for the Contract Sender](sender.html)

[Create a JAR File Containing the Contract](step1.html)

[Generate Keys](step2.html)

[Sign the JAR File](step3.html)

[Export the Public Key Certificate](step4.html)

Steps for the Contract Receiver

[Import the Certificate as a Trusted Certificate](rstep1.html)

[Verify the JAR File Signature](rstep2.html)

[Home Page](../../index.html)
>
[Security Features in Java SE](../index.html)
>
[Exchanging Files](index.html)

[« Previous](step4.html) • [Trail](../TOC.html) • [Next »](rstep1.html)

# Steps for the Contract Receiver

Now acting as Ruth, who receives the signed JAR file
and the certificate file from Stan, perform the following steps,
as shown in the figure.

1. [Import the Certificate as a Trusted Certificate](rstep1.html),
   using the `keytool` `-import` command.

   - [Verify the JAR File Signature](rstep2.html),
     using the `jarsigner` tool.

[![Steps for the Contract Receiver](../../figures/security/ruthReceiver.gif)](../../figures/security/ruthReceiver.gif)  
*This figure has been reduced to fit on the page.   
 Click the image to view it at its natural size.*

[« Previous](step4.html)
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
  
**Next page:** Import the Certificate as a Trusted Certificate




A browser with JavaScript enabled is required for this page to operate properly.