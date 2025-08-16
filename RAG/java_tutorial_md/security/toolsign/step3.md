[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Security Features in Java SE
  
**Lesson:** Signing Code and Granting It Permissions
  
**Section:** Steps for the Code Signer

[Signing Code and Granting It Permissions](index.html)

[Steps for the Code Signer](signer.html)

[Download and Try the Sample Application](step1.html)

[Create a JAR File Containing the Class File](step2.html)

Generate Keys

[Sign the JAR File](step4.html)

[Export the Public Key Certificate](step5.html)

[Steps for the Code Receiver](receiver.html)

[Observe the Restricted Application](rstep1.html)

[Import the Certificate as a Trusted Certificate](rstep2.html)

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

[« Previous](step2.html) • [Trail](../TOC.html) • [Next »](step4.html)

# Generate Keys

If a code signer does not yet have a suitable private key for
signing the code, the key must first be generated, along with a
corresponding public key that can be used by the
code receiver's runtime system to verify the signature.

Since this lesson assumes that you don't yet have such keys,
you are going to create a keystore named `susanstore` and
create an entry with a newly generated public/private key pair
(with the public key in a certificate).

Now pretend that you are Susan Jones and that you
work in company ABC's purchasing department.
Type the following command in your command window to create a
keystore named `susanstore` and to
generate keys for Susan Jones:

```

keytool -genkey -alias signFiles -keypass kpi135 
 -keystore susanstore -storepass ab987c

```

**Note:**   You must type this command on a single line.

## Subparts of the keytool Command

Let's look at what each of the `keytool` subparts mean.

* The command for generating keys is *-genkey*.* The *-alias signFiles* subpart indicates the alias to be used in the future to refer to the
    keystore entry containing the keys that will be generated.* The *-keypass kpi135* subpart specifies a password for the private key about to be
      generated. You will always need this password in order to access the
      keystore entry containing that key. The entry doesn't have to have its
      own password. If you don't include a *-keypass* option, you will be prompted for the key password and given the option of letting it be the same as the keystore
      password.* The *-keystore susanstore* subpart indicates the name (and optionally path)
        of the keystore you are creating or already using.* The *-storepass ab987c* subpart indicates the keystore password.
          If you don't include a `-storepass` option, you will be prompted
          for the keystore password.

**Note:**  For security reasons you should not normally set your
key or keystore passwords on the command line, because they can be intercepted more easily that way. Instead you should
leave off the `-keypass` and the `-storepass`
options and type your passwords when you are prompted for them.

## Distinguished-Name Information

> If you use the preceding `keystore`command, you will be prompted for your
> distinguished-name information.
> Following are the prompts; the bold indicates
> what you should type.
>
> ```
>
> What is your first and last name?
>   [Unknown]:  Susan Jones 
> What is the name of your organizational unit?
>   [Unknown]:  Purchasing 
> What is the name of your organization?
>   [Unknown]:  ABC 
> What is the name of your City or Locality?
>   [Unknown]:  Cupertino 
> What is the name of your State or Province?
>   [Unknown]:  CA 
> What is the two-letter country code for this unit?
>   [Unknown]:  US 
> Is <CN=Susan Jones, OU=Purchasing, O=ABC,
>     L=Cupertino, ST=CA, C=US> correct?
>   [no]:  y 
>
> ```

## Command Results

> The `keytool` command creates the keystore named `susanstore`
> (if it doesn't already exist) in the
> same directory in which the command is executed and assigns it the password
> `ab987c`.
> The command generates a public/private key pair for the entity whose distinguished
> name has a
> common name of Susan Jones and the organizational unit of Purchasing.
>
> The command creates a self-signed certificate that includes
> the public key and the distinguished-name information.
> (The distinguised name you supply will be used as the "subject" field in the certificate.)
> This certificate will be valid
> for 90 days, the default validity period if you don't specify a
> *-validity* option. The certificate is associated
> with the private key in a keystore entry referred to by the
> alias `signFiles`. The private key is assigned
> the password `kpi135`.
>
> **Note:**  The command could be shorter if option defaults
> are accepted or you wish to be prompted for various values.
> Whenever you execute a `keytool` command, defaults are used for
> unspecified options that have default values, and you are prompted for any
> required values. For the `genkey` command, options with default
> values include *alias* (whose default is `mykey`), *validity* (90 days), and
> *keystore* (the file named `.keystore` in your home directory).
> Required values include *dname*, *storepass*, and *keypass*.

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

**Previous page:** Create a JAR File Containing the Class File
  
**Next page:** Sign the JAR File




A browser with JavaScript enabled is required for this page to operate properly.