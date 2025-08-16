[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Security Features in Java SE
  
**Lesson:** Generating and Verifying Signatures

[Generating and Verifying Signatures](index.html)

Generating a Digital Signature

[Prepare Initial Program Structure](step1.html)

[Generate Public and Private Keys](step2.html)

[Sign the Data](step3.html)

[Save the Signature and the Public Key in Files](step4.html)

[Compile and Run the Program](step5.html)

[Verifying a Digital Signature](versig.html)

[Prepare Initial Program Structure](vstep1.html)

[Input and Convert the Encoded Public Key Bytes](vstep2.html)

[Input the Signature Bytes](vstep3.html)

[Verify the Signature](vstep4.html)

[Compile and Run the Program](vstep5.html)

[Weaknesses and Alternatives](enhancements.html)

[Home Page](../../index.html)
>
[Security Features in Java SE](../index.html)
>
[Generating and Verifying Signatures](index.html)

[« Previous](index.html) • [Trail](../TOC.html) • [Next »](step1.html)

# Generating a Digital Signature

The `GenSig` program you are about to create
will use the JDK Security API to generate keys and a digital signature
for data using the private key and to export the public key and the signature to files.
The application gets the data file name from the command line.

The following steps create the `GenSig` sample program.
> 1. [Prepare Initial Program Structure](step1.html)
>
>    Create a text file named `GenSig.java`.
>    Type in the initial program
>    structure (import statements, class name, `main`
>    method, and so on).
>
>    - [Generate Public and Private Keys](step2.html)
>
>      Generate a key pair (public key and private key). The private key is
>      needed for signing the data. The public key will be used by the
>      [`VerSig`](versig.html) program for verifying the signature.
>
>      - [Sign the Data](step3.html)
>
>        Get a `Signature` object and initialize it for signing.
>        Supply it with the data to be signed, and generate the signature.
>
>        - [Save the Signature and the Public Key in Files](step4.html)
>
>          Save the signature bytes in one file and the public key bytes in another.
>
>          - [Compile and Run the Program](step5.html)

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

**Previous page:** Generating and Verifying Signatures
  
**Next page:** Prepare Initial Program Structure




A browser with JavaScript enabled is required for this page to operate properly.