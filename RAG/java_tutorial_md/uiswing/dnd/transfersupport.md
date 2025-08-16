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

TransferSupport Class

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

[« Previous](import.html) • [Trail](../TOC.html) • [Next »](dropmodes.html)

# TransferSupport Class

The
[`TransferSupport`](http://download.oracle.com/javase/7/docs/api/javax/swing/TransferHandler.TransferSupport.html) class, one of the inner classes of the `TransferHandler` class
introduced in JDK 6, serves two functions.
As the name suggests, its first function
is to support the transfer process and for that purpose it provides
several utility methods used to access the details of the data transfer.
The following list shows the methods that can be used to obtain
information from the `TransferHandler`.
Several of these methods are related
to drop actions, which will be discussed in
[Setting the Drop Mode](dropmodes.html).

* [`Component getComponent()`](http://download.oracle.com/javase/7/docs/api/javax/swing/TransferHandler.TransferSupport.html#getComponent())— This method returns the target component of the transfer.

  * [`int getDropAction()`](http://download.oracle.com/javase/7/docs/api/javax/swing/TransferHandler.TransferSupport.html#getDropAction()) — This method returns the chosen action (`COPY`,
    `MOVE` or `LINK`) when the transfer is a drop.
    If the transfer is not a drop, this method throws an exception.

    * [`int getUserDropAction()`](http://download.oracle.com/javase/7/docs/api/javax/swing/TransferHandler.TransferSupport.html#getUserDropAction()) — This method returns the user's chosen drop action.
      For example, if the user simultaneously holds Control and Shift during
      the drag gesture, this indicates an `ACTION_LINK` action.
      For more information on user drop actions, see the API for
      [`DropTargetDragEvent`](http://download.oracle.com/javase/7/docs/api/java/awt/dnd/DropTargetDragEvent.html).
      If the transfer is not a drop, this method throws an exception.

      * [`int getSourceDropActions()`](http://download.oracle.com/javase/7/docs/api/javax/swing/TransferHandler.TransferSupport.html#getSourceDropActions()) — This method returns the set of actions supported by the
        source component.
        If the transfer is not a drop, this method throws an exception.

        * [`DataFlavor[] getDataFlavors()`](http://download.oracle.com/javase/7/docs/api/javax/swing/TransferHandler.TransferSupport.html#getDataFlavors()) — This method returns all the data flavors supported by this
          component. For example, a component might support files and text,
          or text and color.
          If the transfer is not a drop, this method throws an exception.

          * [`boolean isDataFlavorSupported(DataFlavor)`](http://download.oracle.com/javase/7/docs/api/javax/swing/TransferHandler.TransferSupport.html#isDataFlavorSupported(java.awt.datatransfer.DataFlavor)) — This method returns true if the specified `DataFlavor`
            is supported.
            The
            [`DataFlavor`](http://download.oracle.com/javase/7/docs/api/java/awt/datatransfer/DataFlavor.html) indicates the type of data represented,
            such as an image (`imageFlavor`), a string
            (`stringFlavor`), a list of files (`javaFileListFlavor`),
            and so on.

            * [`Transferable getTransferable()`](http://download.oracle.com/javase/7/docs/api/javax/swing/TransferHandler.TransferSupport.html#getTransferable()) — This method returns the `Transferable` data for this
              transfer. It is more efficient to use one of these methods to query
              information about the transfer than to fetch the transferable and
              query it, so this method is not recommended
              unless you cannot get the information another way.

              * [`DropLocation getDropLocation()`](http://download.oracle.com/javase/7/docs/api/javax/swing/TransferHandler.TransferSupport.html#getDropLocation()) — This method returns the drop location in the component.
                Components with built-in drop support, such as list, table and tree,
                override this method to return more useful data. For example,
                the version of this method for the `JList` component returns
                the index in the list where the drop occurred.
                If the transfer is not a drop, this method throws an exception.

### Sample Import Methods

> Now that you are familiar with the `TransferSupport`
> utility methods, let us look at sample `canImport`
> and `importData` methods:
>
> ```
>
> public boolean canImport(TransferSupport supp) {
>     // Check for String flavor
>     if (!supp.isDataFlavorSupported(stringFlavor)) {
>         return false;
>     }
>
>     // Fetch the drop location
>     DropLocation loc = supp.getDropLocation();
>
>     // Return whether we accept the location
>     return shouldAcceptDropLocation(loc);
> }
>
> public boolean importData(TransferSupport supp) {
>     if (!canImport(sup)) {
>         return false;
>     }
>
>     // Fetch the Transferable and its data
>     Transferable t = supp.getTransferable();
>     String data = t.getTransferData(stringFlavor);
>
>     // Fetch the drop location
>     DropLocation loc = supp.getDropLocation();
>
>     // Insert the data at this location
>     insertAt(loc, data);
>
>     return true;
> }
>
> ```
>
> Next we look at how you can set the drop mode for selected
> components.

[« Previous](import.html)
•
[Trail](../TOC.html)
•
[Next »](dropmodes.html)

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

**Previous page:** Import Methods
  
**Next page:** Setting the Drop Mode




A browser with JavaScript enabled is required for this page to operate properly.