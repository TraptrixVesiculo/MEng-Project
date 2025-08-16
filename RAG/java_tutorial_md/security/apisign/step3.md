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

Sign the Data

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

[« Previous](step2.html) • [Trail](../TOC.html) • [Next »](step4.html)

# Sign the Data

Now that you have created a
public key and a private key, you are ready to sign the data.
In this example you will sign the data contained in a file.
`GenSig` gets the file name from the command line.
A digital signature is created (or verified) using an instance of
the `Signature` class.

Signing data, generating a digital signature for that data,
is done with the following steps.

**Get a Signature Object**:
> The following gets a `Signature` object for generating or verifying
> signatures using the DSA algorithm, the same
> algorithm for which the program generated keys in the previous step,
> [Generate Public and Private Keys](step2.html).
>
> ```
>
> Signature dsa = Signature.getInstance("SHA1withDSA", "SUN"); 
>
> ```
>
> Note: When specifying the signature algorithm name,
> you should also include the name of the message digest algorithm used
> by the signature algorithm. SHA1withDSA is a way of specifying
> the DSA signature algorithm, using the SHA-1 message digest algorithm.

**Initialize the Signature Object**
> Before a `Signature` object can be used for signing or
> verifying, it must be initialized. The initialization
> method for signing requires a private key.
> Use the private key placed into the
> `PrivateKey` object named `priv` in the previous step.
>
> ```
>
> dsa.initSign(priv);
>
> ```

**Supply the Signature Object the Data to Be Signed**
> This program will use the data from the file whose name is
> specified as the first (and only) command line argument.
> The program will read in the data a buffer at a time and will supply it to
> the `Signature` object by calling the `update` method.
>
> ```
>
> FileInputStream fis = new FileInputStream(args[0]);
> BufferedInputStream bufin = new BufferedInputStream(fis);
> byte[] buffer = new byte[1024];
> int len;
> while ((len = bufin.read(buffer)) >= 0) {
>     dsa.update(buffer, 0, len);
> };
> bufin.close();
>
> ```

**Generate the Signature**
> Once all of the data has been supplied to the `Signature` object,
> you can generate the digital signature of that data.
>
> ```
>
> byte[] realSig = dsa.sign();
>
> ```

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

**Previous page:** Generate Public and Private Keys
  
**Next page:** Save the Signature and the Public Key in Files




A browser with JavaScript enabled is required for this page to operate properly.