[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../search.html)

[Home Page](../index.html)

[« Previous](../index.html)
•
[Trail](./TOC.html)
•
[Next »](./overview/index.html)

# Trail: Security Features in Java SE

In this trail you'll learn how the built-in
Java™ security features protect you
from malevolent programs. You'll see how to use tools to control access to
resources, to generate and to check digital signatures,
and to create and to manage
keys needed for signature generation and checking. You'll also see how to
incorporate cryptography services, such as digital signature generation
and checking, into your programs.

The security features provided by the Java Development Kit
(JDK™)
are intended for a variety of audiences:

* **Users running programs**:
  > Built-in security functionality protects you from malevolent
  > programs (including viruses),
  > maintains the privacy of your files and information about you,
  > and authenticates the identity of each code provider.
  > You can subject applications and applets to security
  > controls when you need to.

  * **Developers**:

    > You can use API methods to incorporate security functionality into
    > your programs, including cryptography services and
    > security checks.
    > The API framework enables you to define and integrate your own
    > permissions (controlling access to specific resources),
    > cryptography service implementations, security manager implementations,
    > and policy implementations.
    > In addition, classes are provided for management of your
    > public/private key pairs and
    > public key certificates from people you trust.

    * **Systems administrators, developers, and users**:
      > JDK tools manage your keystore (database of keys and certificates);
      > generate digital signatures for JAR files,
      > and verify the authenticity of such signatures
      > and the integrity of the signed contents; and
      > create and modify the policy
      > files that define your installation's security policy.

## Trail Lessons

> [![](../images/coreIcon.gif)
> **Quick Tour of Controlling Applets**](tour1/index.html)
> shows how resource accesses,
> such as reading or writing a file,
> are not permitted for unsigned applets unless
> explicitly allowed by a permission in a policy file.
>
> [![](../images/coreIcon.gif)
> **Quick Tour of Controlling Applications**](tour2/index.html)
> builds on the previous lesson, showing that when applications
> are run under a security manager, resource accesses may be
> controlled in exactly the same way as for unsigned applets.
>
> [![](../images/coreIcon.gif)
> **API and Tools Use for Secure Code and File Exchanges**](sigcert/index.html)
> defines digital signatures, certificates, and keystores and discusses why they are needed.
> It also reviews information applicable to the next three lessons
> regarding the steps commonly needed for using the tools or the API to generate
> signatures, export/import certificates, and so on.
>
> [![](../images/coreIcon.gif)
> **Signing Code and Granting It Permissions**](toolsign/index.html)
> illustrates the use of all the security-related tools.
> It shows the steps that a developer would take
> to sign and to distribute code for others
> to run. The lesson also shows how someone
> who will run the code (or a system administrator)
> could add an entry in a policy file
> to grant the code permission for the resource accesses it needs.
>
> [![](../images/coreIcon.gif)
> **Exchanging Files**](toolfilex/index.html)
> shows use of the tools by one person to sign an important document, such as a
> contract, and to export the public key certificate for the public key
> corresponding to the private key used to sign the contract.
> Then the lesson shows how another person,
> who receives the contract, the signature, and
> the public key certificate, can import the
> certificate and verify the signature.
>
> [![](../images/coreIcon.gif)
> **Generating and Verifying Signatures**](apisign/index.html)
> walks you step by step through an example of writing a Java
> program using the JDK Security API to generate keys, to generate a digital signature for data using the private key, and to export the public key and the signature to files.
> Then the example shows writing a second program, which may be expected to run on a different person's computer, that imports the public key and verifies the authenticity of the signature.
> Finally, the example discusses potential weaknesses of the
> approach used by the basic programs and demonstrates possible alternative approaches and methods of supplying and importing keys, including in certificates.
>
> [![](../images/coreIcon.gif)
> **Implementing Your Own Permission**](userperm/index.html)
> demonstrates how to write a class that defines its
> own special permission.

## For More Information

> JDK security release documentation can be found at
> [http://java.sun.com/javase/6/docs/technotes/guides/security/index.html](http://download.oracle.com/javase/7/docs/technotes/guides/security/index.html) . This index page lists Specifications which present detailed information about latest security features, including architecture specifications, usage guides, API documentation, and tool documentation.
> .
>
> Information on use of the Java Plug-in to download the latest
> Java Runtime Environment compatible with JDK 6 can be found here:
> <http://java.sun.com/products/plugin/index.html> .

[« Previous](../index.html)
•
[TOC](./TOC.html)
•
[Next »](./overview/index.html)

---

Problems with the examples? Try [Compiling and Running
the Examples: FAQs](../information/run-examples.html).
  
Complaints? Compliments? Suggestions? [Give
us your feedback](http://download.oracle.com/javase/feedback.html).

Your use of this page and all the material on pages under "The Java Tutorials" banner,
and all the material on pages under "The Java Tutorials" banner is subject to the [Java SE Tutorial Copyright
and License](../information/license.html).
Additionally, any example code contained in any of these Java
Tutorials pages is licensed under the
[Code
Sample License](http://developers.sun.com/license/berkeley_license.html).

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| |  |  | | --- | --- | | duke image | Oracle logo | | [About Oracle](http://www.oracle.com/us/corporate/index.html) | [Oracle Technology Network](http://www.oracle.com/technology/index.html) | [Terms of Service](https://www.samplecode.oracle.com/servlets/CompulsoryClickThrough?type=TermsOfService) | Copyright © 1995, 2011 Oracle and/or its affiliates. All rights reserved. |

**Previous page:** Beginning of Tutorial
  
**Next page:** Security Features Overview




A browser with JavaScript enabled is required for this page to operate properly.