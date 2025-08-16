[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Creating a GUI With JFC/Swing
  
**Lesson:** Modifying the Look and Feel
  
**Section:** Nimbus Look and Feel

[Modifying the Look and Feel](index.html)

[How to Set the Look and Feel](plaf.html)

[The Synth Look and Feel](synth.html)

[A Synth Example](synthExample.html)

[Nimbus Look and Feel](nimbus.html)

[Changing the Look of Nimbus](custom.html)

Resizing a Component

[Changing the Color Theme](color.html)

[For More Information](info.html)

[Home Page](../../index.html)
>
[Creating a GUI With JFC/Swing](../index.html)
>
[Modifying the Look and Feel](index.html)

[« Previous](custom.html) • [Trail](../TOC.html) • [Next »](color.html)

# Resizing a Component

Have you ever needed a smaller version of a component to place
on a tool palette or tool bar, or in a status bar?
You can resize a component by setting a client property on the component.
Three sizes are supported
in addition to the "regular" size: mini, small, and large.
The following screen capture, taken from
[Laffy](info.html#laffy), shows the four sizes side by side.

![Laffy screen capture showing all four size variants side by side.](../../figures/uiswing/lookandfeel/laffy.png)

The one component that does not support the size variants property is
`JLabel`. However, you can change the size of a label
by changing the size of its font.

---

**Note:** Other look and feel implementations, such as Apple's Aqua,
might also honor the size variants client property.
Nimbus is currently the only Sun look and feel that supports size
variants.

---

You can set the size of a component with one line of code, before
the component is displayed. The following snippet shows
how to use each size:

```

// mini
myButton.putClientProperty("JComponent.sizeVariant", "mini");
// small
mySlider.putClientProperty("JComponent.sizeVariant", "small");
// large
myTextField.putClientProperty("JComponent.sizeVariant", "large");

```

If you have set the size variants property correctly but the
component displays in its "regular" size,
you might need to force an update to the UI.
You can do so by invoking the
[`SwingUtilities.updateComponentTreeUI(Component)`](http://download.oracle.com/javase/7/docs/api/javax/swing/SwingUtilities.html#updateComponentTreeUI(java.awt.Component)) method before the window is displayed. The following code
snippet updates the window and all the components it contains:

```

JFrame frame = ...;

SwingUtilities.updateComponentTreeUI(frame);

frame.pack();
frame.setVisible(true);

```

[« Previous](custom.html)
•
[Trail](../TOC.html)
•
[Next »](color.html)

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

**Previous page:** Changing the Look of Nimbus
  
**Next page:** Changing the Color Theme




A browser with JavaScript enabled is required for this page to operate properly.