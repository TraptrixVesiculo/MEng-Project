[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

Signing Code and Granting It Permissions

[Steps for the Code Signer](signer.html)

[Download and Try the Sample Application](step1.html)

[Create a JAR File Containing the Class File](step2.html)

[Generate Keys](step3.html)

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

**Trail:** Security Features in Java SE

[Home Page](../../index.html)
>
[Security Features in Java SE](../index.html)

[« Previous](../sigcert/index.html) • [Trail](../TOC.html) • [Next »](signer.html)

# Lesson: Signing Code and Granting It Permissions

This lesson shows how to use use
`keytool`, `jarsigner`, `Policy Tool` and `jar` to place files into JAR (Java ARchive)
files for subsequent signing by the `jarsigner` tool.

This lesson has two parts. First, you will create and deploy an application. Second; you will act as the recipient of a signed application.

Here are the steps to create and deploy an application:

**Note:**  For convenience,
you pretend to be a user/developer named Susan Jones. You need to define Susan Jones when you generate the keys.

* Put Java class files comprising your application into a JAR file
* Sign the JAR file
* Export the public key certificate corresponding to the private key used to sign the JAR file

Here are the steps to grant permissions to an application

**Note:**  For convenience,
you pretend to be a user named Ray.

* You see how the signed application
  cannot normally read a file when it is run under a security manager.* * Use `keytool` to import a certificate into
      Ray's keystore in an entry aliased by `susan`
    * Use the Policy Tool to create an entry in Ray's policy file
      to permit code signed by `susan` to read the specified
      file.
    * Finally, you see how the application running under a security
      manager can now read the file, since it has been granted
      permission to do so.

For more information about digital signatures,
certificates, keystores, and the tools, see the
[API and Tools Use for Secure Code and File Exchanges](../sigcert/index.html)
lesson.
> ---
>
> **Important:** You need to
> perform the tasks in this lesson while working in the directory
> in which you store the sample application, but you should store
> the data file needed by the application in a different directory.
> All examples in this trail assume that you are working in the `C:\Test`
> directory, and that the data file is in the `C:\TestData` directory.   
>   
> If you are working on a UNIX system, substitute your own directory
> names.
>
> ---

Here are the steps:

* [Steps for the Code Signer](signer.html)

  * [Steps for the Code Receiver](receiver.html)

[« Previous](../sigcert/index.html)
•
[Trail](../TOC.html)
•
[Next »](signer.html)

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
  
**Next page:** Steps for the Code Signer




A browser with JavaScript enabled is required for this page to operate properly.