[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

Generating and Verifying Signatures

[Generating a Digital Signature](gensig.html)

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

**Trail:** Security Features in Java SE

[Home Page](../../index.html)
>
[Security Features in Java SE](../index.html)

[« Previous](../toolfilex/index.html) • [Trail](../TOC.html) • [Next »](gensig.html)

# Lesson: Generating and Verifying Signatures

This lesson walks you through the steps necessary to use
the JDK Security API to generate a digital signature for
data and to verify that a signature is authentic.
This lesson is meant for developers who wish to incorporate
security functionality into their programs,
including cryptography services.

This lesson demonstrates the use of the JDK Security API with respect
to signing documents. The lesson shows what one program, executed by the
person who has the original document, would do to
generate keys, generate a digital signature for the document using the private key, and
export the public key and the signature to files.

Then it shows an example of another program, executed by
the receiver of the document, signature, and public key. It shows how the
program could import the public key and
verify the authenticity of the signature.
The lesson also discusses and demonstrates possible alternative
approaches and methods of supplying and importing keys, including
in certificates.

For further information about the concepts and
terminology (digital signatures,
certificates, keystores), see the
[API and Tools Use for Secure Code and File Exchanges](../sigcert/index.html)
lesson.

In this lesson you create two basic applications, one for the
digital signature generation and the other for the verification.
This is followed by a discussion and demonstration of
potential enhancements. The lesson contains three sections.

* [Generating a Digital Signature](gensig.html)
  shows using the API to generate
  keys and a digital signature
  for data using the private key and to export the public key and the signature to files.
  The application gets the data file name from the command line.

  * [Verifying a Digital Signature](versig.html)
    shows using the API to import a public key and a signature that is alleged
    to be the signature of a specified data file and to verify
    the authenticity of the signature. The data, public key, and
    signature file names are specified on the command line.

    * [Weaknesses and
      Alternatives](enhancements.html) discusses potential weaknesses of the
      approach used by the basic
      programs. It then presents and demonstrates possible alternative
      approaches and methods of supplying and importing keys, including
      the use of files containing encoded key bytes and the use
      of certificates containing public keys.

[« Previous](../toolfilex/index.html)
•
[Trail](../TOC.html)
•
[Next »](gensig.html)

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
  
**Next page:** Generating a Digital Signature




A browser with JavaScript enabled is required for this page to operate properly.