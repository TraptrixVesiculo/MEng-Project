[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

Exchanging Files

[Steps for the Contract Sender](sender.html)

[Create a JAR File Containing the Contract](step1.html)

[Generate Keys](step2.html)

[Sign the JAR File](step3.html)

[Export the Public Key Certificate](step4.html)

[Steps for the Contract Receiver](receiver.html)

[Import the Certificate as a Trusted Certificate](rstep1.html)

[Verify the JAR File Signature](rstep2.html)

**Trail:** Security Features in Java SE

[Home Page](../../index.html)
>
[Security Features in Java SE](../index.html)

[« Previous](../toolsign/index.html) • [Trail](../TOC.html) • [Next »](sender.html)

# Lesson: Exchanging Files

If you want to electronically send an important document, (like a Contract) to someone else, it is a good idea to digitally "sign" the
document, so your recipient can check that the document
indeed came from you and was not altered in transit.

This lesson shows you how to use Security tools
for the exchange of an important document, in this case a contract.

You first pretend that you are the contract sender, Stan Smith.
This lesson shows the steps Stan would use to put the
contract in a JAR file, sign it,
and export the public key certificate for the public key
corresponding to the private key used to sign the JAR file.

Then you pretend that you are Ruth, who has received
the signed JAR file and the certificate.
You'll use `keytool` to import the certificate into
Ruth's keystore in an entry aliased by `stan`,
and use the `jarsigner` tool to verify the
signature.

For further information about digital signatures,
certificates, keystores, and the tools, see the
[API and Tools Use for Secure Code and File Exchanges](../sigcert/index.html)
lesson.
> ---
>
> **Note:** This lesson assumes that you execute all commands from within the same directory.
>
> ---

Here are the steps:

* [Steps for the Contract Sender](sender.html)

  * [Steps for the Contract Receiver](receiver.html)

[« Previous](../toolsign/index.html)
•
[Trail](../TOC.html)
•
[Next »](sender.html)

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

**Previous page:** Previous Lesson
  
**Next page:** Steps for the Contract Sender




A browser with JavaScript enabled is required for this page to operate properly.