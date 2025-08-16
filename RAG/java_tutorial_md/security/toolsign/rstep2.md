[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Security Features in Java SE
  
**Lesson:** Signing Code and Granting It Permissions
  
**Section:** Steps for the Code Receiver

[Signing Code and Granting It Permissions](index.html)

[Steps for the Code Signer](signer.html)

[Download and Try the Sample Application](step1.html)

[Create a JAR File Containing the Class File](step2.html)

[Generate Keys](step3.html)

[Sign the JAR File](step4.html)

[Export the Public Key Certificate](step5.html)

[Steps for the Code Receiver](receiver.html)

[Observe the Restricted Application](rstep1.html)

Import the Certificate as a Trusted Certificate

[Set Up a Policy File to Grant the Required Permission](rstep3.html)

[Start Policy Tool](wstep1.html)

[Specify the Keystore](wstep2.html)

[Add a Policy Entry with a SignedBy Alias](wstep3.html)

[Save the Policy File](wstep4.html)

[See the Policy File Effects](rstep4.html)

[Home Page](../../index.html)
>
[Security Features in Java SE](../index.html)
>
[Signing Code and Granting It Permissions](index.html)

[« Previous](rstep1.html) • [Trail](../TOC.html) • [Next »](rstep3.html)

# Import the Certificate as a Trusted Certificate

Before you can grant the signed code permission to read a specified
file, you need to import Susan's certificate as a trusted certificate
in your keystore.

Suppose that you have received
from Susan

* the signed JAR file `sCount.jar`, which
  contains the `Count.class` file, and

  * the file `SusanJones.cer`, which
    contains the public key certificate for the public key corresponding
    to the private key used to sign the JAR file.

Even though you created these files and they haven't
actually been transported anywhere, you can simulate
being someone other than the creater and sender, Susan.
Pretend that you are now Ray.
Acting as Ray, you will create a keystore named
`raystore` and will use it to import the certificate
into an entry with an alias of `susan`.

A keystore is created whenever you use a `keytool`
command specifying a keystore that doesn't yet exist.
Thus we can create the `raystore` and import the
certificate via a single `keytool` command. Do the following
in your command window.

1. Go to the directory containing the
   public key certificate file `SusanJones.cer`. (You should
   actually already be there, since this lesson assumes that you stay
   in a single directory throughout.)

   - Type the following command on one line:

     ```

     keytool -import -alias susan
        -file SusanJones.cer -keystore raystore

     ```

Since the keystore doesn't yet exist, it will be created, and you will
be prompted for a keystore password; type whatever password you want.

The `keytool` command will print out the certificate information
and ask you to verify it, for example, by comparing the displayed certificate
fingerprints with those obtained from another (trusted)
source of information. (Each fingerprint is a relatively short number
that uniquely and
reliably identifies the certificate.) For example, in the real world you might
call up Susan and ask her what the fingerprints should be. She can get the
fingerprints of the `SusanJones.cer` file she created by
executing the command

```

keytool -printcert -file SusanJones.cer

```

If the fingerprints she sees are the same as the ones reported to you by
`keytool`, the certificate has not been modified
in transit. In that case you let `keytool` proceed with placing
a trusted certificate entry in the keystore.
The entry contains the public key certificate
data from the file `SusanJones.cer` and is assigned the alias
`susan`.

[« Previous](rstep1.html)
•
[Trail](../TOC.html)
•
[Next »](rstep3.html)

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

**Previous page:** Observe the Restricted Application
  
**Next page:** Set Up a Policy File to Grant the Required Permission




A browser with JavaScript enabled is required for this page to operate properly.