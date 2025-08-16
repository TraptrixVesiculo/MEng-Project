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

Prepare Initial Program Structure

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

[« Previous](gensig.html) • [Trail](../TOC.html) • [Next »](step2.html)

# Prepare Initial Program Structure

Here's the basic structure of the `GenSig` program.
Place it in a file called `GenSig.java`.

```

import java.io.*;
import java.security.*;

class GenSig {

    public static void main(String[] args) {

        /* Generate a DSA signature */

        if (args.length != 1) {
            System.out.println("Usage: GenSig nameOfFileToSign");
            }
        else try {

        // the rest of the code goes here

        } catch (Exception e) {
            System.err.println("Caught exception " + e.toString());
        }
    }

}

```

  
Notes:

* The methods for signing data are in the `java.security`
  package, so the program imports everything from that package. The program also
  imports the `java.io` package, which
  contains the methods needed to input the file data to be signed.

  * A single argument is expected, specifying the
    data file to be signed.

    * The code written in subsequent steps
      will go between the `try` and the `catch` blocks.

[« Previous](gensig.html)
•
[Trail](../TOC.html)
•
[Next »](step2.html)

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

**Previous page:** Generating a Digital Signature
  
**Next page:** Generate Public and Private Keys




A browser with JavaScript enabled is required for this page to operate properly.