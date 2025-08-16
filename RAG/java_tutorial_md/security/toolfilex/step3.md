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

Sign the JAR File

[Export the Public Key Certificate](step4.html)

[Steps for the Contract Receiver](receiver.html)

[Import the Certificate as a Trusted Certificate](rstep1.html)

[Verify the JAR File Signature](rstep2.html)

[Home Page](../../index.html)
>
[Security Features in Java SE](../index.html)
>
[Exchanging Files](index.html)

[« Previous](step2.html) • [Trail](../TOC.html) • [Next »](step4.html)

# Sign the JAR File

Now you are ready to sign the JAR file.

Type the following in your command window to
sign the JAR file `Contract.jar`, using
the private key in the keystore entry aliased by `signLegal`, and
to name the resulting signed JAR file `sContract.jar`:

```

jarsigner -keystore stanstore -signedjar sContract.jar 
    Contract.jar signLegal 

```

(Type all that on one line.)

You will be prompted for the store password (`balloon53`)
and the private key password (`cat876`).

The `jarsigner` tool extracts the certificate
from the keystore entry whose alias
is `signLegal` and attaches it to the generated signature of the
signed JAR file.

[« Previous](step2.html)
•
[Trail](../TOC.html)
•
[Next »](step4.html)

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

**Previous page:** Generate Keys
  
**Next page:** Export the Public Key Certificate




A browser with JavaScript enabled is required for this page to operate properly.