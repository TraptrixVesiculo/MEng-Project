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

Input and Convert the Encoded Public Key Bytes

[Input the Signature Bytes](vstep3.html)

[Verify the Signature](vstep4.html)

[Compile and Run the Program](vstep5.html)

[Weaknesses and Alternatives](enhancements.html)

[Home Page](../../index.html)
>
[Security Features in Java SE](../index.html)
>
[Generating and Verifying Signatures](index.html)

[« Previous](vstep1.html) • [Trail](../TOC.html) • [Next »](vstep3.html)

# Input and Convert the Encoded Public Key Bytes

Next, `VerSig` needs to import the encoded public key bytes
from the file specified
as the first command line argument and to convert them to a `PublicKey`.
A `PublicKey` is needed because that is what the
`Signature` `initVerify`
method requires in order to initialize the `Signature` object for verification.

First, read in the encoded public key bytes.

```

        FileInputStream keyfis = new FileInputStream(args[0]);
        byte[] encKey = new byte[keyfis.available()];  
        keyfis.read(encKey);

        keyfis.close();

```

Now the byte array `encKey` contains the encoded public key bytes.

You can use a `KeyFactory` class in order to instantiate a DSA public key
from its encoding. The `KeyFactory` class provides conversions between
opaque keys
(of type `Key`) and key specifications, which are
transparent representations of the underlying key material.
With an opaque key you can obtain the algorithm name,
format name, and encoded key bytes, but not the key material,
which, for example, may consist of the key itself and the algorithm
parameters used to calculate the key.
(Note that `PublicKey`, because it extends `Key`, is
itself a `Key`.)

So, first you need a key specification.
You can obtain one via the following, assuming that the key was encoded according to
the X.509 standard, which is the case, for example, if the key was generated
with the built-in DSA key-pair generator supplied by the SUN provider:

```

        X509EncodedKeySpec pubKeySpec = new X509EncodedKeySpec(encKey);

```

Now you need a `KeyFactory` object to do the conversion.
That object must be one that works with DSA keys.

```

        KeyFactory keyFactory = KeyFactory.getInstance("DSA", "SUN");

```

Finally, you can use the `KeyFactory` object to generate a
`PublicKey` from the key specification.

```

        PublicKey pubKey = keyFactory.generatePublic(pubKeySpec);

```

[« Previous](vstep1.html)
•
[Trail](../TOC.html)
•
[Next »](vstep3.html)

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

**Previous page:** Prepare Initial Program Structure
  
**Next page:** Input the Signature Bytes




A browser with JavaScript enabled is required for this page to operate properly.