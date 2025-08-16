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

Location Sensitive Drop

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

[« Previous](showdroploc.html) • [Trail](../TOC.html) • [Next »](locsensitivedemo.html)

# Location Sensitive Drop

Sometimes you have a complex component and you want the user to be
able to drop on some parts of it, but not on others.
Perhaps it is a table that allows data to be dropped only in certain columns;
or perhaps it is a tree that allows data to be dropped only on certain nodes.
Obviously you want the cursor to provide accurate feedback —
it should only show the drop location when it is over the specific
part of the component that accepts drops.

This is simple to accomplish by installing the necessary logic in the
[`canImport(TransferHandler.TransferSupport`)](http://download.oracle.com/javase/7/docs/api/javax/swing/TransferHandler.html#canImport(javax.swing.TransferHandler.TransferSupport)) method of the `TransferHandler` class.
It works only with this particular version of `canImport`
because it is called continously while the drag gesture is over the
bounds of the component. When this method returns true, Swing shows
the drop cursor and the drop location is visually indicated;
when this method returns false, Swing shows the "no-drag" cursor and
the drop location is not displayed.

For example, imagine a table that allows drop, but not in the first
column. The `canImport` method might look something like this:

```

public boolean canImport(TransferHandler.TransferSupport info) {
    // for the demo, we will only support drops (not clipboard paste)
    if (!info.isDrop()) {
        return false;
    }

    // we only import Strings
    if (!info.isDataFlavorSupported(DataFlavor.stringFlavor)) {
        return false;
    }

    // fetch the drop location
    JTable.DropLocation dl = (JTable.DropLocation)info.getDropLocation();

    int column = dl.getColumn();

    // we do not support invalid columns or the first column
    if (column == -1 || column == 0) {
        return false;
    }

    return true;
}

```

The code displayed in bold indicates the location-sensitive drop logic:
When the user drops the data in such a way that the column
cannot be calculated (and is therefore invalid) or when
the user drops the text in the first column, the
`canImport` method returns false —
so Swing shows the "no-drag" mouse cursor.
As soon as the user moves the mouse off the first column
`canImport` returns true and Swing shows the drag cursor.

Next, we show a demo of a tree that has implemented location-sensitive
drop.

[« Previous](showdroploc.html)
•
[Trail](../TOC.html)
•
[Next »](locsensitivedemo.html)

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

**Previous page:** Showing the Drop Location
  
**Next page:** Demo - LocationSensitiveDemo




A browser with JavaScript enabled is required for this page to operate properly.