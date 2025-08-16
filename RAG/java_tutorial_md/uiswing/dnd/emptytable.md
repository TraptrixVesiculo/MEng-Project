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

Empty Table Drop

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

[« Previous](locsensitivedemo.html) • [Trail](../TOC.html) • [Next »](droplocation.html)

# Empty Table Drop

Dragging and dropping into an empty table presents a unique challenge.
When adhering to the proper steps:

* Creating the empty table.* Creating and attaching a `TransferHandler`.* Enabling data transfer by calling `setDragEnabled(true)`.* Creating a scroll pane and adding the table to the scroll pane.

You run the application and try to drag valid data into the table
but it rejects the drop.
What gives?

The reason is that the empty table (unlike an empty list or
an empty tree) does not occupy any space in the scroll pane.
The `JTable` does not automatically stretch to fill the
height of a `JScrollPane`'s viewport — it only
takes up as much vertical room as needed for the rows that it contains.
So, when you drag over the empty table, you are not actually over the table
and the drop fails.

You can configure the table to allow drop anywhere in the view port
by calling
[`JTable.setFillsViewportHeight(boolean)`](http://download.oracle.com/javase/7/docs/api/javax/swing/JTable.html#setFillsViewportHeight(boolean)). The default for this property is false to ensure backwards compatibility.

The following example, `FillViewportHeightDemo`, allows you
to experiment with dropping onto an empty table. The demo contains
an empty table with five columns that has its drop mode set to
insert rows and a drag source that provides five comma-delimited
values that autoincrement.

![A snapshot of the FillViewportHeightDemo.](../../figures/uiswing/dnd/FillViewportHeightDemo.png)

---

**Try this:**

1. Click the Launch button to run `FillViewportHeightDemo` using
   [Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp) ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
   Alternatively, to compile and run the example yourself,
   consult the
   [example index](../examples/dnd/index.html#FillViewportHeightDemo).

   [![Launches the FillViewportHeightDemo example](../../images/jws-launch-button.png)](http://download.oracle.com/javase/tutorialJWS/uiswing/dnd/ex6/FillViewportHeightDemo.jnlp)

   - Drag from the text field labeled "Drag from here" to the table.- Drop onto the table. The drop is rejected.- Double-click on the drag source. It deposits the current
         values (0, 0, 0, 0, 0) into the table and increments the
         values in the text field.- Once again, drag from the text field to the table. You can
           insert above or below the row, but not in the area
           underneath.- From the Options menu, choose "Fill Viewport Height" to enable
             the "fillsViewportHeight" property.- From the Options menu, choose "Reset" to empty the table.- Drag from the text component to the table. You can now drop
                 anywhere on the view port and it inserts the data at row 0.

---

You can examine the source for
[`FillViewportHeightDemo.java`](../examples/dnd/FillViewportHeightDemoProject/src/dnd/FillViewportHeightDemo.java), but the primary point to remember is that you should
generally invoke `setFillsViewportHeight(true)` on any
table that will accept dropped data.

[« Previous](locsensitivedemo.html)
•
[Trail](../TOC.html)
•
[Next »](droplocation.html)

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

**Previous page:** Demo - LocationSensitiveDemo
  
**Next page:** Drop Location Rendering




A browser with JavaScript enabled is required for this page to operate properly.