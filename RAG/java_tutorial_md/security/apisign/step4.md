[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Security Features in Java SE
  
**Lesson:** Generating and Verifying Signatures
  
**Section:** Generating a Digital Signature

[Generating and Verifying Signatures](index.html)

[Generating a Digital Signature](gensig.html)

[Prepare Initial Program Structure](step1.html)

[Generate Public and Private Keys](step2.html)

[Sign the Data](step3.html)

Save the Signature and the Public Key in Files

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

[« Previous](step3.html) • [Trail](../TOC.html) • [Next »](step5.html)

# Save the Signature and the Public Key in Files

Now that you have generated a signature for some data,
you need to save the signature bytes in one file and the public key bytes in another
so you can send (via modem, floppy, mail, and so on) someone else

* the data for which the signature was generated,

  * the signature, and

    * the public key

The receiver can verify that the data came from you and
was not modified in transit by running the `VerSig` program
you will generate in the upcoming
[Verifying a Digital Signature](versig.html)
steps. That program uses the public key
to verify that the signature received is the true signature for the
data received.

Recall that the signature was placed in a byte array named `realSig`.
You can save the signature bytes in a file named `sig` via the following.

```

        /* save the signature in a file */
        FileOutputStream sigfos = new FileOutputStream("sig");
        sigfos.write(realSig);
        sigfos.close();

```

Recall from the [Generate Public and Private Keys](step2.html) step that the
public key was placed in a PublicKey object
named `pub`.
You can get the encoded key bytes by calling the `getEncoded`
method and then store the encoded bytes in a file. You can name the file
whatever you want. If, for example, your name is Susan, you might
name it something like `suepk` (for "Sue's public key"),
as in the following:

```

        /* save the public key in a file */
        byte[] key = pub.getEncoded();
        FileOutputStream keyfos = new FileOutputStream("suepk");
        keyfos.write(key);
        keyfos.close();

```

[« Previous](step3.html)
•
[Trail](../TOC.html)
•
[Next »](step5.html)

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

**Previous page:** Sign the Data
  
**Next page:** Compile and Run the Program




A browser with JavaScript enabled is required for this page to operate properly.