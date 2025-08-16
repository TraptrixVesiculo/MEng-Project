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

Setting the Drop Mode

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

[« Previous](transfersupport.html) • [Trail](../TOC.html) • [Next »](dropmodedemo.html)

# Setting the Drop Mode

When enabling drop on a component, such as a list,
you need to decide how you want the drop location to be
interpreted.
For example, do you want to restrict the user to replacing
existing entries?
Do you want to only allow adding or inserting new entries?
Do you want to allow both? To configure this behavior, the
[`JList`](http://download.oracle.com/javase/7/docs/api/javax/swing/JList.html) class provides the
[`setDropMode`](http://download.oracle.com/javase/7/docs/api/javax/swing/JList.html#setDropMode(javax.swing.DropMode)) method which supports the following drop modes.
> * The default drop mode for `JList` is
>   `DropMode.USE_SELECTION`.
>   When dragging in this mode, the selected item in the list
>   moves to echo the potential drop point. On a drop the
>   selected item shifts to the drop location.
>   This mode is provided for backwards compatibility
>   but is otherwise not recommended.
>
>   * In `DropMode.ON`, the selected item
>     in the list moves to echo the potential drop point, but the
>     selected item is not affected on the drop. This mode
>     can be used to drop on top of existing list items.
>
>     * In `DropMode.INSERT`, the user is restricted to
>       selecting the space between existing list items,
>       or before the first item
>       or after the last item in the list. Selecting existing
>       list items is not allowed.
>
>       * `DropMode.ON_OR_INSERT` is a combination
>         of the `ON` and `INSERT` modes.

The `JTree` class provides the same set of
[drop modes](http://download.oracle.com/javase/7/docs/api/javax/swing/JTree.html#setDropMode(javax.swing.DropMode)) and the `JTable` class has
[several more](http://download.oracle.com/javase/7/docs/api/javax/swing/JTable.html#setDropMode(javax.swing.DropMode)) specific to adding rows or columns.

To obtain the location of the drop, the
`TransferSupport` class provides the
[`getDropLocation`](http://download.oracle.com/javase/7/docs/api/javax/swing/TransferHandler.TransferSupport.html#getDropLocation()) method that returns the precise point
where the drop has occurred. But for a list component, the index of
the drop is more useful than a pixel location, so
`JList` provides a special subclass, called
[`JList.DropLocation`](http://download.oracle.com/javase/7/docs/api/javax/swing/JList.DropLocation.html). This class provides the
[`getIndex`](http://download.oracle.com/javase/7/docs/api/javax/swing/JList.DropLocation.html#getIndex()) and
[`isInsert`](http://download.oracle.com/javase/7/docs/api/javax/swing/JList.DropLocation.html#isInsert()) methods, which handle the math for you.

The table, tree, and text components each provide an implementation
of `DropLocation` with methods that make the most sense for
each component.
The
[`JTable.setDropMode`](http://download.oracle.com/javase/7/docs/api/javax/swing/JTable.html#setDropMode(javax.swing.DropMode)) method has the most choices.
The following table shows the methods for all four classes:

**DropLocation Methods for JList,
JTree, JTable and JTextComponent**

| [`JList.DropLocation`](http://download.oracle.com/javase/7/docs/api/javax/swing/JList.DropLocation.html) [`JTree.DropLocation`](http://download.oracle.com/javase/7/docs/api/javax/swing/JTree.DropLocation.html) [`JTable.DropLocation`](http://download.oracle.com/javase/7/docs/api/javax/swing/JTable.DropLocation.html) [`JTextComponent.DropLocation`](http://download.oracle.com/javase/7/docs/api/javax/swing/text/JTextComponent.DropLocation.html) | | | |
| [`isInsert`](http://download.oracle.com/javase/7/docs/api/javax/swing/JList.DropLocation.html#isInsert()) [`getChildIndex`](http://download.oracle.com/javase/7/docs/api/javax/swing/JTree.DropLocation.html#getChildIndex()) [`isInsertRow`](http://download.oracle.com/javase/7/docs/api/javax/swing/JTable.DropLocation.html#isInsertRow()) [`getIndex`](http://download.oracle.com/javase/7/docs/api/javax/swing/text/JTextComponent.DropLocation.html#getIndex()) | | | |
| [`getIndex`](http://download.oracle.com/javase/7/docs/api/javax/swing/JList.DropLocation.html#getIndex()) [`getPath`](http://download.oracle.com/javase/7/docs/api/javax/swing/JTree.DropLocation.html#getPath()) [`isInsertColumn`](http://download.oracle.com/javase/7/docs/api/javax/swing/JTable.DropLocation.html#isInsertColumn()) [`getBias`](http://download.oracle.com/javase/7/docs/api/javax/swing/text/JTextComponent.DropLocation.html#getBias()) | | | |
| [`getRow`](http://download.oracle.com/javase/7/docs/api/javax/swing/JTable.DropLocation.html#getRow())  | | | |
| [`getColumn`](http://download.oracle.com/javase/7/docs/api/javax/swing/JTable.DropLocation.html#getColumn())  | | | |

Next is a demo that implements a custom transfer handler for
a list component so that it fully participates in drag and drop.

[« Previous](transfersupport.html)
•
[Trail](../TOC.html)
•
[Next »](dropmodedemo.html)

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

**Previous page:** TransferSupport Class
  
**Next page:** Demo - DropDemo




A browser with JavaScript enabled is required for this page to operate properly.