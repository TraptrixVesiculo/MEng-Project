[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Security Features in Java SE
  
**Lesson:** Generating and Verifying Signatures
  
**Section:** Verifying a Digital Signature

[Generating and Verifying Signatures](index.html)

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

Compile and Run the Program

[Weaknesses and Alternatives](enhancements.html)

[Home Page](../../index.html)
>
[Security Features in Java SE](../index.html)
>
[Generating and Verifying Signatures](index.html)

[« Previous](vstep4.html) • [Trail](../TOC.html) • [Next »](enhancements.html)

# Compile and Run the Program

[`Here`](examples/VerSig.java)
is the complete source code for the `VerSig.java` program,
with some comments added.

Compile and run the program. Remember, you need to
specify three arguments on the command line:

* The name of the file containing the encoded public key bytes

  * The name of the file containing the signature bytes

    * The name of the data file (the one for which the signature was generated)

Since you will be testing the output of the `GenSig`
program, the file names you should use are

* `suepk`

  * `sig`

    * `data`

Here's a sample run; the bold indicates what you type.

```

%java VerSig suepk sig data
signature verifies: true

```

[« Previous](vstep4.html)
•
[Trail](../TOC.html)
•
[Next »](enhancements.html)

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

**Previous page:** Verify the Signature
  
**Next page:** Weaknesses and Alternatives




A browser with JavaScript enabled is required for this page to operate properly.