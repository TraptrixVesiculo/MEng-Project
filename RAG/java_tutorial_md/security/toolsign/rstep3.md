[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Security Features in Java SE
  
**Lesson:** Signing Code and Granting It Permissions
  
**Section:** Steps for the Code Receiver

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

Set Up a Policy File to Grant the Required Permission

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

[« Previous](rstep2.html) • [Trail](../TOC.html) • [Next »](wstep1.html)

# Set Up a Policy File to Grant the Required Permission

Next, you will use the Policy Tool to
create a policy file named **`raypolicy`**
and in it grant a permission to code from
a signed JAR file.

The JAR file must have been signed using the
private key corresponding to the public key imported into Ray's
keystore (`raystore`) in the previous step.
The certificate containing the public key is aliased by `susan` in
the keystore. We will grant such code permission to read any file in the
`C:\TestData\` directory.

The steps are:

1. [Start Policy Tool](wstep1.html)

   - [Specify the Keystore](wstep2.html)

     - [Add a Policy Entry with a SignedBy Alias](wstep3.html)

       - [Save the Policy File](wstep4.html)

[« Previous](rstep2.html)
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

**Previous page:** Import the Certificate as a Trusted Certificate
  
**Next page:** Start Policy Tool




A browser with JavaScript enabled is required for this page to operate properly.