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

TransferHandler Class

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

[Putting it All Together - DnD and CCP](together.html)

[Further Information](info.html)

[Solving Common Data Transfer Problems](problems.html)

[Home Page](../../index.html)
>
[Creating a GUI With JFC/Swing](../index.html)
>
[Drag and Drop and Data Transfer](index.html)

[« Previous](basicdemo.html) • [Trail](../TOC.html) • [Next »](export.html)

# TransferHandler Class

At the heart of the data transfer mechanism is the
[`TransferHandler`](http://download.oracle.com/javase/7/docs/api/javax/swing/TransferHandler.html) class.
As its name suggests, the `TransferHandler` provides
an easy mechanism for transferring data to and from a
`JComponent` — all the details are contained in
this class and its supporting classes. Most components are provided
with a default transfer handler.
You can create and install your own transfer handler on any component.

There are three methods used to engage a
`TransferHandler` on a component:

* [`setDragEnabled(boolean)`](http://download.oracle.com/javase/7/docs/api/javax/swing/JList.html#setDragEnabled(boolean)) — turns on drag support. (The default is false.)
  This method is defined on each component that supports the drag gesture;
  the link takes you to the documentation for `JList`.

  * [`setDropMode(DropMode)`](http://download.oracle.com/javase/7/docs/api/javax/swing/JList.html#setDropMode(javax.swing.DropMode)) — configures how drop locations are determined.
    This method is defined for `JList`, `JTable`,
    and `JTree`;
    the link takes you to the documentation for `JList`.

    * [`setTransferHandler(TransferHandler)`](http://download.oracle.com/javase/7/docs/api/javax/swing/JComponent.html#setTransferHandler(javax.swing.TransferHandler)) — used to plug in custom data import and export. This method is
      defined on `JComponent`, so it is inherited by every Swing
      component.

As mentioned previously,
the default Swing transfer handlers, such as those used by text
components and the color chooser, provide the support considered
to be most useful for both importing and exporting of data.
However list, table, and tree do not support drop by default.
The reason for this is that there is no all-purpose way to handle
a drop on these components.
For example, what does it mean to drop on a particular node of a
`JTree`? Does it replace the node, insert below it,
or insert as a child of that node? Also, we do not know what type of
model is behind the tree — it might not be mutable.

While Swing cannot provide a default implementation for these components,
the framework for drop is there. You need only to provide a custom
`TransferHandler` that manages the actual import of data.

---

**Note:** If you install a custom `TransferHandler` onto a Swing
component, the default support is replaced. For example,
if you replace `JTextField`'s `TransferHandler`
with one that handles colors only, you will disable its ability to
support import and export of text.

If you must replace a default
`TransferHandler` — for example, one that handles
text — you will need to re-implement the text import and
export ability. This does not need to be as extensive as what
Swing provides — it could be as simple as supporting
the `StringFlavor` data flavor, depending on your
application's needs.

---

Next we show what `TransferHandler` methods
are required to implement data export.

[« Previous](basicdemo.html)
•
[Trail](../TOC.html)
•
[Next »](export.html)

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

**Previous page:** Demo - BasicDnD
  
**Next page:** Export Methods




A browser with JavaScript enabled is required for this page to operate properly.