[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Creating a GUI With JFC/Swing
  
**Lesson:** Drag and Drop and Data Transfer
  
**Section:** Default DnD Support

[Drag and Drop and Data Transfer](index.html)

[Introduction to DnD](intro.html)

[Default DnD Support](defaultsupport.html)

Demo - BasicDnD

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

[Putting it All Together - DnD and CCP](together.html)

[Further Information](info.html)

[Solving Common Data Transfer Problems](problems.html)

[Home Page](../../index.html)
>
[Creating a GUI With JFC/Swing](../index.html)
>
[Drag and Drop and Data Transfer](index.html)

[« Previous](defaultsupport.html) • [Trail](../TOC.html) • [Next »](transferhandler.html)

# Demo - BasicDnD

Now we will look at a simple demo, called `BasicDnD`, that shows
you what you get for free.
As you see from the screen shot, BasicDnD contains a table, a list,
a tree, a color chooser, a text area, and a text field.

All of these components are standard out-of-the-box components
*except* for the list. This list has been customized to bring up
a dialog showing where the drop would occur, if it accepted drops.

The following areas accept drops:

* Text field* Text area* The color chooser accepts drops of type color, but in order
      to try this, you need to run two copies of the demo (or another
      demo that contains a color chooser)

By default, none of the objects has default drag and drop
enabled.
At startup, you can check the "Turn on Drag and Drop" check box
to see what drag and drop behavior you get for free.

[![Basic Drag and Drop behavior](../../figures/uiswing/../../figures/uiswing/dnd/BasicDND.png)](../../figures/uiswing/../../figures/uiswing/dnd/BasicDND.png)  
*This figure has been reduced to fit on the page.   
 Click the image to view it at its natural size.*

---

**Try this:**

1. Click the Launch button to run BasicDnD using
   [Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp) ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
   Alternatively, to compile and run the example yourself,
   consult the
   [example index](../examples/dnd/index.html#BasicDnD).

   [![Launches the BasicDnD example](../../images/jws-launch-button.png)](http://download.oracle.com/javase/tutorialJWS/uiswing/dnd/ex6/BasicDnD.jnlp)

   - Select an item in the list and, while holding down the
     mouse button, begin to drag. Nothing happens because
     the drag has not yet been enabled on the list.- Select the "Turn on Drag and Drop" check box.- Press the selected item in the list and begin to drag.
         Drop the text back onto the list. A dialog shows where the text
         would appear if the list actually accepted drops.
         (The default behavior for a list would be to
         show a "does not accept data" cursor.)- Drag the selected text over a text area. The insertion
           point for the text is indicated by a blinking caret.
           Also, the cursor changes to indicate that the text area
           will accept the text as a copy.- Release the mouse and watch the text appear in the text area.- Select some text in one of the text areas.- Press the mouse button while the cursor is
                 over the selected text and begin to drag.- Note that this time, the cursor for a drag action appears.
                   Successfully dropping this text into another component will
                   cause the text to be removed from the original component.- Hold the Control key down and press again on the selected
                     text. Begin dragging and the copy cursor now appears.
                     Move the cursor over the text area and drop. The text
                     appears in the new location but is not removed from the
                     original location.
                     The Control key can be used to change any Move to a Copy.- Select a color from the color chooser. The selected color
                       appears in the Preview panel. Press and hold the mouse button
                       over the color in the Preview panel and drag it over the
                       other components. Note that none of these components
                       accepts color.- Try dropping text, color, and even files, onto the list.
                         A dialog will report the attempted action. The actual drop
                         can be implemented with an additional six lines of code that
                         have been commented out in the
                         [`BasicDnD.java`](../examples/dnd/BasicDnDProject/src/dnd/BasicDnD.java ) source file.

---

Next we will look at the `TransferHandler` class, the
workhorse of the drag and drop mechanism.

[« Previous](defaultsupport.html)
•
[Trail](../TOC.html)
•
[Next »](transferhandler.html)

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

**Previous page:** Default DnD Support
  
**Next page:** TransferHandler Class




A browser with JavaScript enabled is required for this page to operate properly.