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

[Adding Cut, Copy and Paste (CCP)](cutpaste.html)

[CCP in a Text Component](textpaste.html)

[CCP in a non-Text Component](listpaste.html)

[Using and Creating a DataFlavor](dataflavor.html)

Putting it All Together - DnD and CCP

[Further Information](info.html)

[Solving Common Data Transfer Problems](problems.html)

[Home Page](../../index.html)
>
[Creating a GUI With JFC/Swing](../index.html)
>
[Drag and Drop and Data Transfer](index.html)

[« Previous](dataflavor.html) • [Trail](../TOC.html) • [Next »](info.html)

# Putting it All Together - DnD and CCP

We have shown how to implement drag and drop support and how to implement
cut, copy, paste support. How do you combine both in one component?

You implement both within the `TransferHandler`'s
`importData` method, like this:

```

if (transferSupport.isDrop()) {
    // put data in transferSupport.getDropLocation()
} else {
    // determine where you want the paste to go (ex: after current selection)
    // put data there
}

```

The `ListCutPaste` example, discussed on the
[CCP in a non-Text Component](listpaste.html) page, supports both dnd and ccp.
Here is its `importData` method
(the `if`-`else` drop logic is bolded):

```

    public boolean importData(TransferHandler.TransferSupport info) {
        String data = null;

        //If we cannot handle the import, bail now.
        if (!canImport(info)) {
            return false;
        }

        JList list = (JList)info.getComponent();
        DefaultListModel model = (DefaultListModel)list.getModel();
        //Fetch the data -- bail if this fails
        try {
            data = (String)info.getTransferable().getTransferData(DataFlavor.stringFlavor);
        } catch (UnsupportedFlavorException ufe) {
            System.out.println("importData: unsupported data flavor");
            return false;
        } catch (IOException ioe) {
            System.out.println("importData: I/O exception");
            return false;
        }

        if (info.isDrop()) { //This is a drop
            JList.DropLocation dl = (JList.DropLocation)info.getDropLocation();
            int index = dl.getIndex();
            if (dl.isInsert()) {
                model.add(index, data);
                return true;
            } else {
                model.set(index, data);
                return true;
            }
        } else { //This is a paste
            int index = list.getSelectedIndex();
            // if there is a valid selection,
            // insert data after the selection
            if (index >= 0) {
                model.add(list.getSelectedIndex()+1, data);
            // else append to the end of the list
            } else {
                model.addElement(data);
            }
            return true;
        }
    }

```

This is the only place where you need to install `if`-`else`
logic to distinguish between dnd and ccp.

[« Previous](dataflavor.html)
•
[Trail](../TOC.html)
•
[Next »](info.html)

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

**Previous page:** Using and Creating a DataFlavor
  
**Next page:** Further Information




A browser with JavaScript enabled is required for this page to operate properly.