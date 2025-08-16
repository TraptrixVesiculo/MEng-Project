[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Security Features in Java SE
  
**Lesson:** Quick Tour of Controlling Applets
  
**Section:** Set up a Policy File to Grant the Required Permission

[Quick Tour of Controlling Applets](index.html)

[Observe Applet Restrictions](step1.html)

[Set up a Policy File to Grant the Required Permission](step2.html)

[Start Policy Tool](wstep1.html)

Grant the Required Permission

[Save the Policy File](wstep3.html)

[See the Policy File Effects](step3.html)

[Home Page](../../index.html)
>
[Security Features in Java SE](../index.html)
>
[Quick Tour of Controlling Applets](index.html)

[« Previous](wstep1.html) • [Trail](../TOC.html) • [Next »](wstep3.html)

# Grant the Required Permission

To grant the `WriteFile` applet permission to
create and to write to the `writetest` file,
you must create a policy entry granting this permission.
To create a new entry, click on
the **Add Policy Entry** button
in the main Policy Tool window.
This displays the Policy Entry dialog box
as shown in the following figure.

[![the Policy Entry dialog](../../figures/security/AddEntryBlank1.gif)](../../figures/security/AddEntryBlank1.gif)  
*This figure has been reduced to fit on the page.   
 Click the image to view it at its natural size.*

A policy entry specifies one or more permissions for code from a particular
*code source* - code from a particular location (URL),
code signed by a
particular entity, or both.

The **CodeBase** and the **SignedBy** text boxes
specify which code you want to grant the permission(s) you
will be adding in the file.

* A **CodeBase** value indicates the code source location;
  you grant the permission(s)
  to code from that location.
  An empty **CodeBase** entry signifies
  "any code" -- it does not matter where the code originates.

  * A **SignedBy**
    value indicates the alias for a certificate stored in a keystore.
    The public key within that certificate is used to verify the digital
    signature on the code. You grant permission to code signed by the private key corresponding
    to the public key in the keystore entry specified by the alias.
    The **SignedBy** entry is optional; omitting it
    signifies "any signer" -- it does not matter whether
    the code is signed, or by whom.

If you have both a **CodeBase** and a **SignedBy**
entry, the permission(s) are granted
only to code that is both from the specified location *and* signed by the named alias.

To grant `WriteFile` the permission it needs, you can grant permission to all code from the location (URL) where
`WriteFile.class` is stored.

Type the following URL
into the **CodeBase** text box of the Policy Entry dialog box:

```

http://download.oracle.com/javase/tutorial/security/tour1/examples/

```

**Note:** This is a URL. Therefore, it must always use slashes as separators, not backslashes.

Leave the **SignedBy** text box blank, since you aren't requiring the code to be signed.

---

**Note:** To grant the permission to any code
(`.class` file) not just from the directory specified previously
but from the `security` directory
*and its subdirectories*, type the
following URL into the **CodeBase** box:

```

http://download.oracle.com/javase/tutorial/security/-

```

---

You have specified where the code comes from (the
**CodeBase**), and that the code does not have to be signed
(since there is no **SignedBy**
value). Now you are ready to grant permissions to that code.

Click on the **Add Permission** button to
display the Permissions dialog box.

[![the Permissions dialog](../../figures/security/AddPermBlank.gif)](../../figures/security/AddPermBlank.gif)  
*This figure has been reduced to fit on the page.   
 Click the image to view it at its natural size.*

Follow these steps
to grant code from the specified **CodeBase**
permission to write (and thus also to create) the file named
`writetest`.

1. Choose **File Permission** from the Permission drop-down list. The
   complete permission type name (`java.io.FilePermission`)
   now displays in the text box to the right of the drop-down list.

   - Type the following in the text box to the right of the list labeled
     *Target Name* to specify the file named `writetest`:

     ```

     writetest

     ```

     - Specify write access by choosing the `write` option from the *Actions* drop-down list.

The Permissions dialog box now looks like the following.

[![the Permissions dialog, with fields filled in](../../figures/security/WQ1addFilePerm.gif)](../../figures/security/WQ1addFilePerm.gif)  
*This figure has been reduced to fit on the page.   
 Click the image to view it at its natural size.*

Click on the
**OK** button. The new permission displays in a line
in the Policy Entry dialog. So now the policy entry window looks like this.

[![the new permission, listed in the Policy Entry dialog](../../figures/security/WQ1addEntry1.gif)](../../figures/security/WQ1addEntry1.gif)  
*This figure has been reduced to fit on the page.   
 Click the image to view it at its natural size.*

You have now specified this policy entry, so click on the **Done**
button in the Policy Entry dialog. The Policy Tool window now contains a line
representing the policy entry, showing the
`CodeBase` value.

[![the PolicyTool window, showing the new policy entry](../../figures/security/WQ1ptOneCB1.gif)](../../figures/security/WQ1ptOneCB1.gif)  
*This figure has been reduced to fit on the page.   
 Click the image to view it at its natural size.*

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
  
**Next page:** Save the Policy File




A browser with JavaScript enabled is required for this page to operate properly.