[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Creating a GUI With JFC/Swing
  
**Lesson:** Drag and Drop and Data Transfer
  
**Section:** Choosing the Drop Action

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

Demo - ChooseDropAction

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

[« Previous](dropaction.html) • [Trail](../TOC.html) • [Next »](showdroploc.html)

# Demo - ChooseDropAction

The following demo, `ChooseDropActionDemo`, contains three
lists. As you can see in the screen shot, the list on the left,
labeled "Drag from here", is the drag source.
This list supports both move and copy but it
does not implement import — so you cannot drop into it.

On the right side are two lists that act as drop targets.
The top list, labeled "Drop to COPY here" will only allow data to be copied
to it.
The bottom list, labeled "Drop to MOVE here" will only allow data to be
moved to it. The source list only allows data to be dragged from it.

![A snapshot of the ChooseDropActionDemo demo.](../../figures/uiswing/dnd/ChooseDropActionDemo.png)

---

**Try this:**

1. Click the Launch button to run `ChooseDropActionDemo` using
   [Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp) ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
   Alternatively, to compile and run the example yourself,
   consult the
   [example index](../examples/dnd/index.html#ChooseDropAction).

   [![Launches the ChooseDropActionDemo example](../../images/jws-launch-button.png)](http://download.oracle.com/javase/tutorialJWS/uiswing/dnd/ex6/ChooseDropActionDemo.jnlp)

   - Select an item in the source list and drag to the
     upper target list. As you drag over the target, notice
     that the copy-drop mouse cursor displays, even if you are
     not holding the Control key to signify that you want a copy
     action.
     (Note that the copy cursor does not appear on the Macintosh platform,
     unless you are pressing the Option key.)- Drop the item. It is inserted into the target list but not
       removed from the source — as desired.- Drag again from the source list, but this time into the
         lower target list. Drop the item. It is inserted into the
         target list and removed from the source list.- Select another item in the source list and, while pressing
           the Control key to indicate a preference for the COPY action,
           drag the item to the lower target list.- Drop the item into the list. The item is not inserted —
             the drop is rejected. The `canImport` method for the
             transfer handler was coded to reject the COPY action,
             but it could have been implemented to return true,
             in which case the user action would prevail and a copy would occur.

---

As you might guess, the
[`ChooseDropActionDemo.java`](../examples/dnd/ChooseDropActionDemoProject/src/dnd/ChooseDropActionDemo.java) example contains two `TransferHandler` implementations:

```

/**
 * The FromTransferHandler allows dragging from the list and
 * supports both copy and move actions.  This transfer handler
 * does not support import.
 */
class FromTransferHandler extends TransferHandler {
    public int getSourceActions(JComponent comp) {
        return COPY_OR_MOVE;
    }

    private int index = 0;

    public Transferable createTransferable(JComponent comp) {
        index = dragFrom.getSelectedIndex();
        if (index < 0 || index >= from.getSize()) {
            return null;
        }

        return new StringSelection((String)dragFrom.getSelectedValue());
    }
    
    public void exportDone(JComponent comp, Transferable trans, int action) {
        if (action != MOVE) {
            return;
        }

        from.removeElementAt(index);
    }
}

/**
 * The ToTransferHandler has a constructor that specifies whether the
 * instance will support only the copy action or the move action.
 * This transfer handler does not support export.
 */
class ToTransferHandler extends TransferHandler {
    int action;
    
    public ToTransferHandler(int action) {
        this.action = action;
    }
    
    public boolean canImport(TransferHandler.TransferSupport support) {
        // for the demo, we will only support drops (not clipboard paste)
        if (!support.isDrop()) {
            return false;
        }

        // we only import Strings
        if (!support.isDataFlavorSupported(DataFlavor.stringFlavor)) {
            return false;
        }

        // check if the source actions contain the desired action -
        // either copy or move, depending on what was specified when
        // this instance was created
        boolean actionSupported = (action & support.getSourceDropActions()) == action;
        if (actionSupported) {
            support.setDropAction(action);
            return true;
        }

        // the desired action is not supported, so reject the transfer
        return false;
    }

    public boolean importData(TransferHandler.TransferSupport support) {
        // if we cannot handle the import, say so
        if (!canImport(support)) {
            return false;
        }

        // fetch the drop location
        JList.DropLocation dl = (JList.DropLocation)support.getDropLocation();

        int index = dl.getIndex();

        // fetch the data and bail if this fails
        String data;
        try {
            data = (String)support.getTransferable().getTransferData(DataFlavor.stringFlavor);
        } catch (UnsupportedFlavorException e) {
            return false;
        } catch (java.io.IOException e) {
            return false;
        }

        JList list = (JList)support.getComponent();
        DefaultListModel model = (DefaultListModel)list.getModel();
        model.insertElementAt(data, index);

        Rectangle rect = list.getCellBounds(index, index);
        list.scrollRectToVisible(rect);
        list.setSelectedIndex(index);
        list.requestFocusInWindow();

        return true;
    }  
} 

```

The `FromTransferHandler`, attached to the source list,
allows for dragging from the list and supports both copy and move actions.
If you try to drop onto this list, the drop will be rejected
because `FromTransferHandler`
has not implemented the `canImport` and `importData`
methods.

The `ToTransferHandler`, attached to *both*
the move-only and the copy-only target list, contains a constructor
that specifies whether the target list will allow only copy or only move.
An instance that supports the copy action is attached to the
copy-only list and an instance that supports the move action is attached
to the move-only list.

You might also be interested in the
[Top-Level Drop](toplevel.html) example which also illustrates choosing the drop action.

Next we look at showing the drop location.

[« Previous](dropaction.html)
•
[Trail](../TOC.html)
•
[Next »](showdroploc.html)

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

**Previous page:** Choosing the Drop Action
  
**Next page:** Showing the Drop Location




A browser with JavaScript enabled is required for this page to operate properly.