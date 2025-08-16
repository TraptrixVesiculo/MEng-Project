[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Creating a GUI With JFC/Swing
  
**Lesson:** Drag and Drop and Data Transfer
  
**Section:** TransferHandler Class

[Drag and Drop and Data Transfer](index.html)

[Introduction to DnD](intro.html)

[Default DnD Support](defaultsupport.html)

[Demo - BasicDnD](basicdemo.html)

[TransferHandler Class](transferhandler.html)

[Export Methods](export.html)

Import Methods

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

[Adding Cut, Copy and Paste (CCP)](cutpaste.html)

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

[« Previous](export.html) • [Trail](../TOC.html) • [Next »](transfersupport.html)

# Import Methods

Now we will look at the methods used for importing data into a component.
These methods are invoked for the drop gesture, or the paste action,
when the component is the target of the operation.
The `TransferHandler` methods for importing data are:

* [`canImport(TransferHandler.TransferSupport)`](http://download.oracle.com/javase/7/docs/api/javax/swing/TransferHandler.html#canImport(javax.swing.TransferHandler.TransferSupport)) — This method is called repeatedly during a drag gesture and
  returns true if the area below the cursor can accept the transfer,
  or false if the transfer will be rejected.
  For example, if a user drags a color over a component that accepts only text,
  the `canImport` method for that component's
  `TransferHandler` should return false.

  * [`importData(TransferHandler.TransferSupport)`](http://download.oracle.com/javase/7/docs/api/javax/swing/TransferHandler.html#importData(javax.swing.TransferHandler.TransferSupport)) — This method is called on a successful drop (or paste) and
    initiates the transfer of data to the target component.
    This method returns true if the import was successful and false
    otherwise.

---

**Version note:** These methods replace older versions that do not use the
`TransferSupport` class, introduced in JDK 6.
Unlike its replacement method,
`canImport(JComponent, DataFlavor[])`
is not called continuously.

---

You will notice that these import methods take a
`TransferHandler.TransferSupport` argument.
Next we look at the `TransferSupport` class
and then some sample import methods.

[« Previous](export.html)
•
[Trail](../TOC.html)
•
[Next »](transfersupport.html)

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

**Previous page:** Export Methods
  
**Next page:** TransferSupport Class




A browser with JavaScript enabled is required for this page to operate properly.