[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Security Features in Java SE
  
**Lesson:** Exchanging Files
  
**Section:** Steps for the Contract Sender

[Exchanging Files](index.html)

[Steps for the Contract Sender](sender.html)

[Create a JAR File Containing the Contract](step1.html)

[Generate Keys](step2.html)

[Sign the JAR File](step3.html)

Export the Public Key Certificate

[Steps for the Contract Receiver](receiver.html)

[Import the Certificate as a Trusted Certificate](rstep1.html)

[Verify the JAR File Signature](rstep2.html)

[Home Page](../../index.html)
>
[Security Features in Java SE](../index.html)
>
[Exchanging Files](index.html)

[« Previous](step3.html) • [Trail](../TOC.html) • [Next »](receiver.html)

# Export the Public Key Certificate

You now have a signed JAR file `sContract.jar`.
Recipients wanting to use this file will also want to authenticate your signature.
To do this, they need the public key that corresponds to the
private key you used to generate your signature. You supply your public key
by sending them a copy of the certificate that contains your public key. Copy that certificate from the keystore `stanstore`
to a file named `StanSmith.cer` via the following:

```

keytool -export -keystore stanstore -alias signLegal -file StanSmith.cer

```

You will be prompted for the store password (`balloon53`).

Once they have that certificate and the signed JAR file, your recipient can use
the `jarsigner` tool to authenticate your signature. See [**Steps for the Contract Receiver**](receiver.html).

[« Previous](step3.html)
•
[Trail](../TOC.html)
•
[Next »](receiver.html)

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

**Previous page:** Sign the JAR File
  
**Next page:** Steps for the Contract Receiver




A browser with JavaScript enabled is required for this page to operate properly.