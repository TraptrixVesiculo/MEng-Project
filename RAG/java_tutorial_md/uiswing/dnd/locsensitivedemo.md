[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Creating a GUI With JFC/Swing
  
**Lesson:** Drag and Drop and Data Transfer
  
**Section:** Location Sensitive Drop

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

Demo - LocationSensitiveDemo

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

[« Previous](locsensitivedrop.html) • [Trail](../TOC.html) • [Next »](emptytable.html)

# Demo - LocationSensitiveDemo

The following demo, `LocationSensitiveDemo`, shows
a `JTree` that has been configured to support drop on
any node except for one called "names" (or its descendants).
Use the text field at the top of the frame as the drag source
(it will automatically increment the string number each time you
drag from there).

A combo box below the tree allows you to toggle the behavior
for showing the drop location. Swing's default behavior is to
show the drop location only when the area can accept the drop.
You can override this behavior to always show the drop location
(even if the area cannot accept the drop) or to never show the
drop location (even if the area can accept the drop).

![A snapshot of the LocationSensitiveDemo demo.](../../figures/uiswing/dnd/LocationSensitiveDemo.png)

---

**Try this:**

1. Click the Launch button to run `LocationSensitiveDemo` using
   [Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp) ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
   Alternatively, to compile and run the example yourself,
   consult the
   [example index](../examples/dnd/index.html#LocationSensitiveDemo).

   [![Launches the ListDemo example](../../images/jws-launch-button.png)](http://download.oracle.com/javase/tutorialJWS/uiswing/dnd/ex6/LocationSensitiveDemo.jnlp)

   - Initiate a drag by pressing on top of "String 0" in the text
     field and moving the mouse a short distance. Drag into the tree
     and move downwards. As you hover the mouse over most of the nodes,
     the drag acceptibility is indicated by both the mouse cursor and by
     the node becoming highlighted. Drop the text onto the "colors" node.
     The new item becomes a child of that node and a sibling to the
     colors listed.- Drag "String 1" from the textfield into the tree. Try to drop
       it on the "names" node. As you drag over that node or its children,
       Swing will not provide any drop location feedback and it will not accept
       the data.- Change the "Show drop location" combo box to "Always".- Repeat steps 1 and 2. The drop location now displays for the
           "names" node, but you cannot drop data into that area.- Change the "Show drop location" combo box to "Never".- Repeat steps 1 and 2. The drop location will not display for
               any part of the tree, though you can still drop data into the nodes,
               other than "names".

---

The `canImport` method for
[`LocationSensitiveDemo`](../examples/dnd/LocationSensitiveDemoProject/src/dnd/LocationSensitiveDemo.java) looks like this:

```

public boolean canImport(TransferHandler.TransferSupport info) {
    // for the demo, we will only support drops (not clipboard paste)
    if (!info.isDrop()) {
        return false;
    }

    String item = (String)indicateCombo.getSelectedItem();
                
    if (item.equals("Always")) {
        info.setShowDropLocation(true);
    } else if (item.equals("Never")) {
        info.setShowDropLocation(false);
    }

    // we only import Strings
    if (!info.isDataFlavorSupported(DataFlavor.stringFlavor)) {
        return false;
    }

    // fetch the drop location
    JTree.DropLocation dl = (JTree.DropLocation)info.getDropLocation();

    TreePath path = dl.getPath();

    // we do not support invalid paths or descendants of the names folder
    if (path == null || namesPath.isDescendant(path)) {
        return false;
    }

    return true;
}

```

The first code snippet displayed in bold modifies the drop location feedback
mechanism. If "Always", then the drop location is always shown.
If "Never", the drop location is never shown. Otherwise, the default
behavior applies.

The second code snippet displayed in bold contains the logic that determines whether
the tree will accept the data. If the path is not a valid path or
if it is not the names path (or its descendant) it will return false
and the import will not be accepted.

[« Previous](locsensitivedrop.html)
•
[Trail](../TOC.html)
•
[Next »](emptytable.html)

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

**Previous page:** Location Sensitive Drop
  
**Next page:** Empty Table Drop




A browser with JavaScript enabled is required for this page to operate properly.