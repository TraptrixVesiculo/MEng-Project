[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Deployment
  
**Lesson:** Packaging Programs in JAR Files
  
**Section:** Signing and Verifying JAR Files

[Packaging Programs in JAR Files](index.html)

[Using JAR Files: The Basics](basicsindex.html)

[Creating a JAR File](build.html)

[Viewing the Contents of a JAR File](view.html)

[Extracting the Contents of a JAR File](unpack.html)

[Updating a JAR File](update.html)

[Running JAR-Packaged Software](run.html)

[Working with Manifest Files: The Basics](manifestindex.html)

[Understanding the Default Manifest](defman.html)

[Modifying a Manifest File](modman.html)

[Setting an Application's Entry Point](appman.html)

[Adding Classes to the JAR File's Classpath](downman.html)

[Setting Package Version Information](packageman.html)

[Sealing Packages within a JAR File](sealman.html)

[Signing and Verifying JAR Files](signindex.html)

[Understanding Signing and Verification](intro.html)

Signing JAR Files

[Verifying Signed JAR Files](verify.html)

[Using JAR-related APIs](apiindex.html)

[The JarClassLoader Class](jarclassloader.html)

[The JarRunner Class](jarrunner.html)

[Questions and Exercises](QandE/questions.html)

[Home Page](../../index.html)
>
[Deployment](../index.html)
>
[Packaging Programs in JAR Files](index.html)

[« Previous](intro.html) • [Trail](../TOC.html) • [Next »](verify.html)

# Signing JAR Files

You use the JAR Signing and Verification Tool to sign JAR files.
You invoke the JAR Signing and Verification Tool by using the jarsigner command, so we'll refer to it as "Jarsigner" for short.

To sign a JAR file, you must first have a private key.
Private keys and their associated public-key certificates are stored
in password-protected databases called *keystores*. A keystore
can hold the keys of many potential signers. Each key in the
keystore can be identified by an *alias* which is typically the name of the
signer who owns the key. The key belonging to Rita Jones might have the alias "rita", for example.

The basic form of the command for signing a JAR file is

```

jarsigner jar-file alias

```

In this command:

* jar-file is the pathname of the JAR file that's to
  be signed.* alias is the alias identifying the private key
    that's to be used to sign the JAR file, and the key's associated certificate.

The Jarsigner tool will prompt you for the passwords for the keystore
and alias.

This basic form of the command assumes that the keystore to be used
is in a file named .keystore in your home directory. It
will create signature and signature block files with names x.SF
and x.DSA respectively, where x is the first eight
letters of the alias, all converted to upper case. This basic command
will *overwrite* the original JAR file with the signed JAR file.

In practice, you may want to use this command in conjunction with
one or more of these options, which must precede the jar-file
pathname:
  

**Jarsigner Command Options**

| Option | Description |
| -keystore *url* | Specifies a keystore to be used if you don't want to use the .keystore default database. |
| -storepass *password* | Allows you to enter the keystore's password on the command line rather than be prompted for it. |
| -keypass *password* | Allows you to enter your alias's password on the command line rather than be prompted for it. |
| -sigfile *file* | Specifies the base name for the .SF and .DSA files if you don't want the base name to be taken from your alias. *file* must be composed only of upper case letters (A-Z), numerals (0-9), hyphen (-), and underscore (\_). |
| -signedjar *file* | Specifies the name of the signed JAR file to be generated if you don't want the original unsigned file to be overwritten with the signed file. |

## Example

Let's look at a couple of examples of signing a JAR file with the
Jarsigner tool. In these examples we will assume:

* your alias is "johndoe".* the keystore you want to use is in a file named "mykeys" in the current
    working directory.* the keystore's password is "abc123".* the password for your alias is "mypass".

Under these assumptions, you could use this command to sign a JAR file named app.jar:

```

jarsigner -keystore mykeys -storepass abc123 
          -keypass mypass app.jar johndoe

```

Because this command doesn't make use of the -sigfile option,
the .SF and .DSA files it creates would be named JOHNDOE.SF and
JOHNDOE.DSA. Because the command doesn't use the -signedjar
option, the resulting signed file will overwrite the original version
of app.jar.

Let's look at what would happen if you used a different combination
of options:

```

jarsigner -keystore mykeys -sigfile SIG 
          -signedjar SignedApp.jar app.jar johndoe

```

This time, you would be prompted to enter the passwords for both the
keystore and your alias because the passwords aren't specified on the
command line. The signature and
signature block files would be named SIG.SF and
SIG.DSA, respectively, and the signed JAR file
SignedApp.jar would be placed in the current directory. The
original unsigned JAR file would remain unchanged.

## Additional Information

Complete reference pages for the JAR Signing and Verification Tool are
on-line:
[Summary of Security Tools](http://java.sun.com/javase/6/docs/technotes/guides/security/SecurityToolsSummary.html)

[« Previous](intro.html)
•
[Trail](../TOC.html)
•
[Next »](verify.html)

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

**Previous page:** Understanding Signing and Verification
  
**Next page:** Verifying Signed JAR Files




A browser with JavaScript enabled is required for this page to operate properly.