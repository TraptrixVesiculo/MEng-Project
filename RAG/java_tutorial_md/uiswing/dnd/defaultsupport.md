[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Creating a GUI With JFC/Swing
  
**Lesson:** Drag and Drop and Data Transfer

[Drag and Drop and Data Transfer](index.html)

[Introduction to DnD](intro.html)

Default DnD Support

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

[Putting it All Together - DnD and CCP](together.html)

[Further Information](info.html)

[Solving Common Data Transfer Problems](problems.html)

[Home Page](../../index.html)
>
[Creating a GUI With JFC/Swing](../index.html)
>
[Drag and Drop and Data Transfer](index.html)

[« Previous](intro.html) • [Trail](../TOC.html) • [Next »](basicdemo.html)

# Default DnD Support

Technically speaking, the framework for drag and drop supports
all Swing components — the data transfer mechanism is built
into every `JComponent`. If you wanted,
you could implement drop support for a `JSlider`
so that it could fully participate in data transfer.
While `JSlider` does not support drop by default,
the components you would want (and expect) to support
drag and drop do provide specialized built-in support.

The following components recognize the drag gesture
once the `setDragEnabled(true)` method is
invoked on the component. For example, once you invoke
`myColorChooser.setDragEnabled(true)` you can drag colors
from your color chooser:

* `JColorChooser`* `JEditorPane`* `JFileChooser`* `JFormattedTextField`* `JList`* `JTable`* `JTextArea`* `JTextField`* `JTextPane`* `JTree`

The following components support drop out of the box.
If you are using one of these components, your work is done.

* `JEditorPane`* `JFormattedTextField`* `JPasswordField`* `JTextArea`* `JTextField`* `JTextPane`* `JColorChooser`

The framework for drop is in place for the following components,
but you need to plug in a small amount of code to customize the
support for your needs.

* `JList`* `JTable`* `JTree`

For these critical components, Swing performs the drop location
calculations and rendering; it allows you to specify a drop mode;
and it handles component specific details, such as tree expansions.
Your work is fairly minimal.

---

**Note:** You can also install drop support on top-level containers, such
as `JFrame` and `JDialog`. You can learn
more about this in
[Top-Level Drop](toplevel.html).

---

[« Previous](intro.html)
•
[Trail](../TOC.html)
•
[Next »](basicdemo.html)

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

**Previous page:** Introduction to DnD
  
**Next page:** Demo - BasicDnD




A browser with JavaScript enabled is required for this page to operate properly.