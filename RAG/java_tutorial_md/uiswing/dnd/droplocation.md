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

Drop Location Rendering

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

[« Previous](emptytable.html) • [Trail](../TOC.html) • [Next »](toplevel.html)

# Drop Location Rendering

This is a more advanced topic and most people do not need to worry about it.
However, if you have a custom component you will need to handle
the drop location rendering yourself.

You can register to be notified whenever the
`dropLocation` property changes.
You would listen for this change and
do your own rendering of the drop location in a custom renderer
for the component or in the `paintComponent` method,
using the `getDropLocation` method.

Here is an example of listening for the `dropLocation`
property:

```

class Repainter extends PropertyChangeListener {
    public void propertyChange(PropertyChangeEvent pce) {
        repaintDropLocation(pce.getOldValue());
        repaintDropLocation(pce.getNewValue());
    }
}

comp.addPropertyChangeListener("dropLocation", newRepainter());

```

Here is an example of the `paintComponent` approach:

```

public void paintComponent(Graphics g) {
    super.paintComponent(g);

    DropLocation loc= getDropLocation();
    if (loc == null) {
        return;
    }

    renderPrettyIndicatorAt(loc);
}

```

[« Previous](emptytable.html)
•
[Trail](../TOC.html)
•
[Next »](toplevel.html)

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

**Previous page:** Empty Table Drop
  
**Next page:** Top-Level Drop




A browser with JavaScript enabled is required for this page to operate properly.