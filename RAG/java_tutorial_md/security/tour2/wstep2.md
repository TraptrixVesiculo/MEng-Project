[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Security Features in Java SE
  
**Lesson:** Quick Tour of Controlling Applications
  
**Section:** Set up the Policy File to Grant the Required Permissions

[Quick Tour of Controlling Applications](index.html)

[Observe Application Freedom](step1.html)

[See How to Restrict Applications](step2.html)

[Set up the Policy File to Grant the Required Permissions](step3.html)

[Open the Policy File](wstep1.html)

Grant the Required Permissions

[Save the Policy File](wstep3.html)

[See the Policy File Effects](step4.html)

[Home Page](../../index.html)
>
[Security Features in Java SE](../index.html)
>
[Quick Tour of Controlling Applications](index.html)

[« Previous](wstep1.html) • [Trail](../TOC.html) • [Next »](wstep3.html)

# Grant the Required Permissions

To grant the `GetProps` application permission to
read the `"user.home"` and `"java.home"`
property values, you must create a policy entry granting those permissions.
Choose the **Add Policy Entry** button
in the main Policy Tool window.
This brings up the Policy Entry dialog box,
as shown in the following figure.

[![the Policy Entry dialog](../../figures/security/AddEntryBlank1.gif)](../../figures/security/AddEntryBlank1.gif)  
*This figure has been reduced to fit on the page.   
 Click the image to view it at its natural size.*

Type the following file URL
into the **CodeBase** text box to indicate that you are going to be granting a
permission to code from the specified directory, which is the directory in which
`GetProps.class` is stored.

```

file:/C:/Test/

```

(Note, this is a URL and thus must always have
slashes, not backslashes.)

Leave the **SignedBy** text box blank, since you aren't requiring the code
to be signed.

To add permission to read the `"user.home"` property value,
choose the **Add Permission** button.
This brings up the Permissions dialog box.

[![the Permissions dialog](../../figures/security/AddPermBlank.gif)](../../figures/security/AddPermBlank.gif)  
*This figure has been reduced to fit on the page.   
 Click the image to view it at its natural size.*

Do the following.

1. Choose **Property Permission** from the Permission drop-down list. The
   complete permission type name (`java.util.PropertyPermission`)
   now appears in the text box to the right of the drop-down list.

   - Type the following in the text box to the right of the list labeled
     Target Name to specify the `"user.home"` property:

     ```

     user.home

     ```

     - Specify permission to read this property by selecting the **read**
       option from the
       Actions drop-down list.

Now the Permissions dialog box looks like the following.

[![the Permissions dialog with the text fields filled in](../../figures/security/WQ2addPropPerm1.gif)](../../figures/security/WQ2addPropPerm1.gif)  
*This figure has been reduced to fit on the page.   
 Click the image to view it at its natural size.*

Choose the
**OK** button. The new permission appears in a line
in the policy entry window.

[![the new permission in the Policy Entry window](../../figures/security/WQ2addEntry1.gif)](../../figures/security/WQ2addEntry1.gif)  
*This figure has been reduced to fit on the page.   
 Click the image to view it at its natural size.*

To add permission to read the `"java.home"` property value,
choose the **Add Permission** button again.
In the Permissions dialog box, do the following:

1. Choose **Property Permission** from the Permission drop-down list.

   - Type the following in the text box to the right of the list labeled
     Target Name to specify the `"java.home"` property:

     ```

     java.home

     ```

     - Specify permission to read this property by choosing the **read**
       option from the
       Actions drop-down list.

Now the Permissions dialog box looks like the following.

[![the Permissions dialog with the java home property set to read](../../figures/security/WQ2addPropPerm2.gif)](../../figures/security/WQ2addPropPerm2.gif)  
*This figure has been reduced to fit on the page.   
 Click the image to view it at its natural size.*

Choose the
**OK** button. The new permission and the previously added
permission appear in lines
in the policy entry window,
as shown in the following figure.

[![the new permission appears in the Policy Entry dialog](../../figures/security/WQ2addEntry2.gif)](../../figures/security/WQ2addEntry2.gif)  
*This figure has been reduced to fit on the page.   
 Click the image to view it at its natural size.*

You are now done specifying this policy entry, so choose the **Done**
button in the Policy Entry dialog. The Policy Tool window now includes a line
representing the new policy entry, showing the
**CodeBase** value.

[![the new policy entry appears in the PolicyTool window](../../figures/security/WQ2ptTwoCBandFilename1.gif)](../../figures/security/WQ2ptTwoCBandFilename1.gif)  
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

**Previous page:** Open the Policy File
  
**Next page:** Save the Policy File




A browser with JavaScript enabled is required for this page to operate properly.