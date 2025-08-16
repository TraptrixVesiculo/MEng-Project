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

[Specify the Keystore](wstep2.html)

Add a Policy Entry with a SignedBy Alias

[Save the Policy File](wstep4.html)

[See the Policy File Effects](rstep4.html)

[Home Page](../../index.html)
>
[Security Features in Java SE](../index.html)
>
[Signing Code and Granting It Permissions](index.html)

[« Previous](wstep2.html) • [Trail](../TOC.html) • [Next »](wstep4.html)

# Add a Policy Entry with a SignedBy Alias

To grant code signed by `susan` permission to
read any files in the `C:\TestData` directory, you
need to create a policy entry granting this permission.
Note that "Code signed by `susan`"
is an abbreviated way of saying
"Code in a class file contained in a JAR file, where the JAR
file was signed using the private key corresponding to the
public key that appears in a keystore certificate in an entry
aliased by `susan`."

Choose the **Add Policy Entry** button
in the main Policy Tool window.
This brings up the Policy Entry dialog box:

[![the Policy Entry dialog](../../figures/security/AddEntryBlank1.gif)](../../figures/security/AddEntryBlank1.gif)  
*This figure has been reduced to fit on the page.   
 Click the image to view it at its natural size.*

Using this dialog box, type the following alias
into the **SignedBy** text box:

```

susan

```

Leave the **CodeBase** text box blank, to grant
*all* code signed by `susan` the permission,
no matter where it comes from.

> Note: If you wanted to restrict the permission to just code signed by
> `susan` that comes from the `C:\Test\` directory,
> you would type the following URL
> into the **CodeBase** text box:
>
> ```
>
> file:/C:/Test/*
>
> ```

To add the permission, choose the **Add Permission** button.
This brings up the Permissions dialog box.

[![the Permission dialog](../../figures/security/AddPermBlank.gif)](../../figures/security/AddPermBlank.gif)  
*This figure has been reduced to fit on the page.   
 Click the image to view it at its natural size.*

Do the following.

1. Choose **File Permission** from the Permission drop-down list. The
   complete permission type name (`java.io.FilePermission`)
   now appears in the text box to the right of the drop-down list.

   - Type the following in the text box to the right of the list labeled
     Target Name to specify all files in the `C:\TestData\` directory:

     ```

     C:\TestData\*

     ```

     - Specify read access by choosing the **read** option from the
       Actions drop-down list.

Now the Permissions dialog box looks like the following.

[![the Permission dialog, with fields filled in](../../figures/security/WTaddFilePerm.gif)](../../figures/security/WTaddFilePerm.gif)  
*This figure has been reduced to fit on the page.   
 Click the image to view it at its natural size.*

Choose the
**OK** button. The new permission appears in a line
in the Policy Entry dialog, as follows.

[![the new Permission appears in the Policy Entry dialog](../../figures/security/WTaddEntry.gif)](../../figures/security/WTaddEntry.gif)  
*This figure has been reduced to fit on the page.   
 Click the image to view it at its natural size.*

> ---
>
> **Note:** Each backslash in the file path you typed has been replaced
> with two backslashes, for your convenience. Strings in a policy file
> are processed by a tokenizer that allows \ to be used as an
> escape character (for example, `\n` to indicate a new line), so the policy file
> requires *two* backslashes to indicate a single backslash.
> If you use single backslashes as your directory separators,
> Policy Tool automatically converts them to double backslashes for you.
>
> ---

You are now done specifying this policy entry, so choose the **Done**
button in the Policy Entry dialog. The Policy Tool window now contains a line
representing the policy entry, showing the
**SignedBy** value, as shown in the following figure.

[![the Policy Entry appears in the PolicyTool dialog](../../figures/security/WTptOneSB.gif)](../../figures/security/WTptOneSB.gif)  
*This figure has been reduced to fit on the page.   
 Click the image to view it at its natural size.*

[« Previous](wstep2.html)
•
[Trail](../TOC.html)
•
[Next »](wstep4.html)

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

**Previous page:** Specify the Keystore
  
**Next page:** Save the Policy File




A browser with JavaScript enabled is required for this page to operate properly.