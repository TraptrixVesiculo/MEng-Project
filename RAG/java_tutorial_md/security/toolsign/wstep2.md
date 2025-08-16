[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Security Features in Java SE
  
**Lesson:** Signing Code and Granting It Permissions
  
**Section:** Steps for the Code Receiver
  
**Subsection:** Set Up a Policy File to Grant the Required Permission

[Signing Code and Granting It Permissions](index.html)

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

Specify the Keystore

[Add a Policy Entry with a SignedBy Alias](wstep3.html)

[Save the Policy File](wstep4.html)

[See the Policy File Effects](rstep4.html)

[Home Page](../../index.html)
>
[Security Features in Java SE](../index.html)
>
[Signing Code and Granting It Permissions](index.html)

[« Previous](wstep1.html) • [Trail](../TOC.html) • [Next »](wstep3.html)

# Specify the Keystore

For this lesson you will grant all code in JAR files
signed by the alias susan
read access to all files in the `C:\TestData\` directory.
You need to

1. Specify the keystore containing the certificate information
   aliased by susan

   - Create the policy entry granting the permission

The keystore is the one named `raystore` created in
the [Import the Certificate as a Trusted Certificate](rstep2.html)
step.

To specify the keystore,
choose the **Change Keystore** command in the
**Edit** menu of the main Policy Tool window.
This brings up a dialog box in which you can specify the
keystore URL and the keystore type.

To specify the keystore named `raystore` in the
`Test` directory on the `C:` drive, type the following
`file` URL into the text box labeled New KeyStore URL

```

file:/C:/Test/raystore

```

You can leave the text box labeled New KeyStore Type blank
if the keystore type is the default one, as specified in the
security properties file.
Your keystore will be the default type, so leave the text box blank.
The result is shown in the following figure.

[![the Keystore text field has been left blank](../../figures/security/WTaddKeystore.gif)](../../figures/security/WTaddKeystore.gif)  
*This figure has been reduced to fit on the page.   
 Click the image to view it at its natural size.*

> ---
>
> Note: The New KeyStore URL value is a URL and thus should always use
> slashes (never backslashes) as the directory separator.
>
> ---

When you are done specifying the keystore URL, choose **OK**.
The text box labeled Keystore is now
filled in with the URL:

[![the Keystore text field is now filled in with the URL](../../figures/security/WTptKeystore.gif)](../../figures/security/WTptKeystore.gif)  
*This figure has been reduced to fit on the page.   
 Click the image to view it at its natural size.*

Next, you need to specify the new policy entry.

[« Previous](wstep1.html)
•
[Trail](../TOC.html)
•
[Next »](wstep3.html)

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

**Previous page:** Start Policy Tool
  
**Next page:** Add a Policy Entry with a SignedBy Alias




A browser with JavaScript enabled is required for this page to operate properly.