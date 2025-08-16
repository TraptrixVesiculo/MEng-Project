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

[Import the Certificate as a Trusted Certificate](rstep1.html)

Verify the JAR File Signature

[Home Page](../../index.html)
>
[Security Features in Java SE](../index.html)
>
[Exchanging Files](index.html)

[« Previous](rstep1.html) • [Trail](../TOC.html) • [Next »](../apisign/index.html)

# Verify the JAR File Signature

Acting as Ruth, you have now imported Stan's public key certificate
into the `ruthstore` keystore as a
"trusted certificate." You can now use the `jarsigner`
tool to verify the authenticity of the JAR file signature.

When you verify a signed JAR file, you verify that the signature is valid and that the
JAR file has not been tampered with. You can do this for the `sContract.jar` file
via the following command:

```

jarsigner -verify -verbose -keystore ruthstore sContract.jar 

```

You should see something like the following:

```

       183 Fri Jul 31 10:49:54 PDT 1998 META-INF/SIGNLEGAL.SF
       1542 Fri Jul 31 10:49:54 PDT 1998 META-INF/SIGNLEGAL.DSA
       0 Fri Jul 31 10:49:18 PDT 1998 META-INF/
smk    1147 Wed Jul 29 16:06:12 PDT 1998 contract

 s = signature was verified 
 m = entry is listed in manifest
 k = at least one certificate was found in keystore
 i = at least one certificate was found in identity scope

jar verified.

```

Be sure to run the command with the `-verbose`  option to get
enough information to ensure the following:

* the contract file is among the files in the JAR file that were signed
  and its signature was verified (that's what the `s` signifies)

  * the public key used to verify the signature is in the specified keystore
    and thus trusted by you (that's what the `k` signifies).

[« Previous](rstep1.html)
•
[Trail](../TOC.html)
•
[Next »](../apisign/index.html)

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
  
**Next page:** Generating and Verifying Signatures




A browser with JavaScript enabled is required for this page to operate properly.