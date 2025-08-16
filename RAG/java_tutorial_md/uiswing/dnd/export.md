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

Export Methods

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

[« Previous](transferhandler.html) • [Trail](../TOC.html) • [Next »](import.html)

# Export Methods

The first set of methods we will examine are used for exporting
data from a component. These methods are invoked for the drag gesture,
or the cut/copy action, when the component in question is the source
of the operation.
The `TransferHandler` methods for exporting data are:

* [`getSourceActions(JComponent)`](http://download.oracle.com/javase/7/docs/api/javax/swing/TransferHandler.html#getSourceActions(javax.swing.JComponent)) — This method is used to query what actions are supported
  by the source component, such as
  `COPY`, `MOVE`, or `LINK`, in any combination.
  For example, a customer list might not support moving a customer name
  out of the list, but it would very likely support copying the customer name.
  Most of our examples support both `COPY` and `MOVE`.

  * [`createTransferable(JComponent)`](http://download.oracle.com/javase/7/docs/api/javax/swing/TransferHandler.html#createTransferable(javax.swing.JComponent)) — This method bundles up the data to be exported into a
    [`Transferable`](http://download.oracle.com/javase/7/docs/api/java/awt/datatransfer/Transferable.html) object in preparation for the transfer.

    * [`exportDone(JComponent, Transferable, int)`](http://download.oracle.com/javase/7/docs/api/javax/swing/TransferHandler.html#exportDone(javax.swing.JComponent, java.awt.datatransfer.Transferable, int)) — This method is invoked after the export is complete.
      When the action is a `MOVE`, the data needs to be removed
      from the source after the transfer is complete — this method is
      where any necessary cleanup occurs.

### Sample Export Methods

> Here are some sample implementations of the export methods:
>
> ```
>
> int getSourceActions(JComponent c) {
>     return COPY_OR_MOVE;
> }
>
> Transferable createTransferable(JComponent c) {
>     return new StringSelection(c.getSelection());
> }
>
> void exportDone(JComponent c, Transferable t, int action) {
>     if (action == MOVE) {
>         c.removeSelection();
>     }
> }
>
> ```
>
> Next we will look at the `TransferHandler` methods
> required for data import.

[« Previous](transferhandler.html)
•
[Trail](../TOC.html)
•
[Next »](import.html)

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

**Previous page:** TransferHandler Class
  
**Next page:** Import Methods




A browser with JavaScript enabled is required for this page to operate properly.