[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Security Features in Java SE
  
**Lesson:** Exchanging Files
  
**Section:** Steps for the Contract Receiver

[Exchanging Files](index.html)

[Steps for the Contract Sender](sender.html)

[Create a JAR File Containing the Contract](step1.html)

[Generate Keys](step2.html)

[Sign the JAR File](step3.html)

[Export the Public Key Certificate](step4.html)

[Steps for the Contract Receiver](receiver.html)

Import the Certificate as a Trusted Certificate

[Verify the JAR File Signature](rstep2.html)

[Home Page](../../index.html)
>
[Security Features in Java SE](../index.html)
>
[Exchanging Files](index.html)

[« Previous](receiver.html) • [Trail](../TOC.html) • [Next »](rstep2.html)

# Import the Certificate as a Trusted Certificate

W

Suppose that you are Ruth and have received
from Stan Smith

* The signed JAR file `sContract.jar`
  containing a contract

  * The file `StanSmith.cer`
    containing the public key certificate for the public key corresponding
    to the private key used to sign the JAR file

Before you can use the `jarsigner` tool
to check the authenticity of the JAR file's signature, you need to
import Stan's certificate into your keystore.

Even though you (acting as Stan) created these files and they haven't
actually been transported anywhere, you can simulate
being someone other than the creater and sender, Stan.
Acting as Ruth, type the following command to create a keystore named
`ruthstore` and import the certificate
into an entry with an alias of `stan`.

```

keytool -import -alias stan -file StanSmith.cer -keystore ruthstore

```

Since the keystore doesn't yet exist, `keytool` will create it for you. It will prompt you for a keystore password.

The `keytool` prints the certificate information
and asks you to verify it; For example, by comparing the displayed certificate
fingerprints with those obtained from another (trusted)
source of information. (Each fingerprint is a relatively short number
that uniquely and
reliably identifies the certificate.) For example, in the real world you can phone Stan and ask him what the fingerprints should be. He can get the
fingerprints of the `StanSmith.cer` file he
created by executing the command

```

keytool -printcert -file StanSmith.cer

```

If the fingerprints he sees are the same as the ones reported to you by `keytool`, then you both can assume that
the certificate has not been modified
in transit. You can safely let `keytool` procede to place a "trusted certificate" entry into your keystore.
This entry contains the public key certificate
data from the file `StanSmith.cer`. `keytool`assigns the alias
`stan` to this new entry.

[« Previous](receiver.html)
•
[Trail](../TOC.html)
•
[Next »](rstep2.html)

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

**Previous page:** Steps for the Contract Receiver
  
**Next page:** Verify the JAR File Signature




A browser with JavaScript enabled is required for this page to operate properly.