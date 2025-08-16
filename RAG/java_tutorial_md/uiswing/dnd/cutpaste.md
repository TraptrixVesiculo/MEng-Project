[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Creating a GUI With JFC/Swing
  
**Lesson:** Drag and Drop and Data Transfer

[Drag and Drop and Data Transfer](index.html)

[Introduction to DnD](intro.html)

[Default DnD Support](defaultsupport.html)

[Demo - BasicDnD](basicdemo.html)

[TransferHandler Class](transferhandler.html)

[Export Methods](export.html)

[Import Methods](import.html)

[TransferSupport Class](transfersupport.html)

[Setting the Drop Mode](dropmodes.html)

[Demo - DropDemo](dropmodedemo.html)

[Choosing the Drop Action](dropaction.html)

[Demo - ChooseDropAction](dropactiondemo.html)

[Showing the Drop Location](showdroploc.html)

[Location Sensitive Drop](locsensitivedrop.html)

[Demo - LocationSensitiveDemo](locsensitivedemo.html)

[Empty Table Drop](emptytable.html)

[Drop Location Rendering](droplocation.html)

[Top-Level Drop](toplevel.html)

Adding Cut, Copy and Paste (CCP)

[CCP in a Text Component](textpaste.html)

[CCP in a non-Text Component](listpaste.html)

[Using and Creating a DataFlavor](dataflavor.html)

[Putting it All Together - DnD and CCP](together.html)

[Further Information](info.html)

[Solving Common Data Transfer Problems](problems.html)

[Home Page](../../index.html)
>
[Creating a GUI With JFC/Swing](../index.html)
>
[Drag and Drop and Data Transfer](index.html)

[« Previous](toplevel.html) • [Trail](../TOC.html) • [Next »](textpaste.html)

# Adding Cut, Copy and Paste (CCP)

So far our discussion has centered mostly around drag and drop support.
However, it is an easy matter to hook up cut or copy or paste (ccp)
to a transfer handler. This requires the following steps:

* Ensure a transfer handler is installed on the component.

  * Create a manner by which the `TransferHandler`'s
    ccp support can be invoked. Typically this involves
    adding bindings to the input and action maps to have the
    `TransferHandler`'s ccp actions invoked in
    response to particular keystrokes.

    * Create ccp menu items and/or buttons.
      (This step is optional but recommended.)
      This is easy to do with text components but requires a bit
      more work with other components, since you need logic to determine which
      component to fire the action on. See
      [CCP in a non-Text Component](listpaste.html) for more information.

      * Decide where you want to perform the paste. Perhaps above or below
        the current selection. Install the logic in the `importData`
        method.

Next we look at a cut and paste example that feature a text component.

[« Previous](toplevel.html)
•
[Trail](../TOC.html)
•
[Next »](textpaste.html)

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

**Previous page:** Top-Level Drop
  
**Next page:** CCP in a Text Component




A browser with JavaScript enabled is required for this page to operate properly.