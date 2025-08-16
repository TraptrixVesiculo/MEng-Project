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

Generate Keys

[Sign the JAR File](step3.html)

[Export the Public Key Certificate](step4.html)

[Steps for the Contract Receiver](receiver.html)

[Import the Certificate as a Trusted Certificate](rstep1.html)

[Verify the JAR File Signature](rstep2.html)

[Home Page](../../index.html)
>
[Security Features in Java SE](../index.html)
>
[Exchanging Files](index.html)

[« Previous](step1.html) • [Trail](../TOC.html) • [Next »](step3.html)

# Generate Keys

Before signing the `Contract.jar` JAR file containing the
`contract` file, you need to generate keys,
if you don't already have suitable keys available.
You need to sign your JAR file using your private key, and your recipient needs your corresponding public key to verify your signature.

This lesson assumes that you don't have a key pair yet.
You are going to create a keystore named `stanstore` and
create an entry with a newly generated public/private key pair
(with the public key in a certificate).

Now pretend that you are Stan Smith and that you
work in the legal department of XYZ corporation.
Type the following in your command window to create a
keystore named `stanstore` and to
generate keys for Stan Smith:

```

keytool -genkey -alias signLegal -keystore stanstore

```

The keystore tool prompts you for a keystore password, your
distinguished-name information, and the key password.
Following are the prompts; the bold indicates
what you should type.

```

Enter keystore password:  balloon53 
What is your first and last name?
  [Unknown]:  Stan Smith 
What is the name of your organizational unit?
  [Unknown]:  Legal 
What is the name of your organization?
  [Unknown]:  XYZ 
What is the name of your City or Locality?
  [Unknown]:  New York
What is the name of your State or Province?
  [Unknown]:  NY 
What is the two-letter country code for this unit?
  [Unknown]:  US 
Is <CN=Stan Smith, OU=Legal, O=XYZ, L=New York, 
       ST=NY, C=US> correct?
  [no]:  y 
    
Enter key password for 
        (RETURN if same as keystore password):  cat876 

```

The preceding `keytool` command creates the keystore named `stanstore` in the same directory in which the command is executed (assuming that the specified keystore doesn't already exist) and assigns it the password `balloon53`.
The command generates a public/private key pair for the entity whose distinguished name has a common name of *Stan Smith* and an organizational unit of *Legal*.

The self-signed certificate you have just created
includes the public key and the distinguished-name information.
(A self-signed certificate is one signed by the private key corresponding to
the public key in the certificate.)
This certificate is valid
for 90 days. This is the default validity period if you don't specify a
*-validity* option. The certificate is associated
with the private key in a keystore entry referred to by the
alias `signLegal`. The private key is assigned the password
`cat876`.

[« Previous](step1.html)
•
[Trail](../TOC.html)
•
[Next »](step3.html)

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

**Previous page:** Create a JAR File Containing the Contract
  
**Next page:** Sign the JAR File




A browser with JavaScript enabled is required for this page to operate properly.