[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Creating a GUI With JFC/Swing
  
**Lesson:** Laying Out Components Within a Container

[Laying Out Components Within a Container](index.html)

[A Visual Guide to Layout Managers](visual.html)

[Using Layout Managers](using.html)

[How Layout Management Works](howLayoutWorks.html)

[How to Use Various Layout Managers](layoutlist.html)

[How to Use BorderLayout](border.html)

[How to Use BoxLayout](box.html)

[How to Use CardLayout](card.html)

[How to Use FlowLayout](flow.html)

[How to Use GridBagLayout](gridbag.html)

[How to Use GridLayout](grid.html)

[How to Use GroupLayout](group.html)

[A GroupLayout Example](groupExample.html)

[How to Use SpringLayout](spring.html)

[Creating a Custom Layout Manager](custom.html)

Doing Without a Layout Manager (Absolute Positioning)

[Solving Common Layout Problems](problems.html)

[Home Page](../../index.html)
>
[Creating a GUI With JFC/Swing](../index.html)
>
[Laying Out Components Within a Container](index.html)

[« Previous](custom.html) • [Trail](../TOC.html) • [Next »](problems.html)

# Doing Without a Layout Manager (Absolute Positioning)

Although it is possible to do without a layout manager,
you should use a layout manager if at all possible.
A layout manager makes it easier to
adjust to look-and-feel-dependent component appearances,
to different font sizes,
to a container's changing size,
and to different locales.
Layout managers also can be reused easily by other containers,
as well as other programs.

---

**Note:** This lesson covers writing layout code by hand, which can be challenging. If you are not interested in learning all the details of layout management, you might prefer to use the `GroupLayout` layout manager combined with a builder tool to lay out your GUI. One such builder tool is the
[NetBeans IDE](../learn/index.html). Otherwise, if you want to code by hand and do not want to use `GroupLayout`, then `GridBagLayout` is recommended as the next most flexible and powerful layout manager.

---

If a container
holds components whose size is not affected
by the container's size
or by font, look-and-feel, or language changes,
then absolute positioning might make sense.
Desktop panes,
which contain
[internal frames](../components/internalframe.html), are in this category.
The size and position of internal frames
does not depend directly on the desktop pane's size.
The programmer determines the initial size and placement
of internal frames within the desktop pane,
and then the user can move or resize the frames.
A layout manager is unnecessary in this situation.

Another situation in which absolute positioning might make sense
is that of a custom container
that performs size and position calculations
that are particular to the container,
and perhaps require knowledge
of the container's specialized state.
This is the situation with
[split panes](../components/splitpane.html).

Creating a container without a layout manager involves the following steps.

1. Set the container's layout manager to null by calling `setLayout(null)`.
2. Call the `Component` class's `setbounds` method for each of the container's children.
3. Call the `Component` class's `repaint` method.

However, creating containers with absolutely positioned containers can cause problems if the window containing the container is resized.

Here is a snapshot of a frame
whose content pane uses absolute positioning.

![A snapshot of AbsoluteLayoutDemo](../../figures/uiswing/layout/AbsoluteLayoutDemo.png)

Click the Launch button to run AbsoluteLayoutDemo using
[Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp) ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
Alternatively, to compile and run the example yourself,
consult the
[example index](../examples/layout/index.html#AbsoluteLayoutDemo).

[![Launches the AbsoluteLayoutDemo example](../../images/jws-launch-button.png)](http://download.oracle.com/javase/tutorialJWS/uiswing/layout/ex6/AbsoluteLayoutDemo.jnlp)

Its code is in
[`AbsoluteLayoutDemo.java`](../examples/layout/AbsoluteLayoutDemoProject/src/layout/AbsoluteLayoutDemo.java).
The following code snippet
shows how the components in the content pane
are created and laid out.

```

pane.setLayout(null);

JButton b1 = new JButton("one");
JButton b2 = new JButton("two");
JButton b3 = new JButton("three");

pane.add(b1);
pane.add(b2);
pane.add(b3);

Insets insets = pane.getInsets();
Dimension size = b1.getPreferredSize();
b1.setBounds(25 + insets.left, 5 + insets.top,
             size.width, size.height);
size = b2.getPreferredSize();
b2.setBounds(55 + insets.left, 40 + insets.top,
             size.width, size.height);
size = b3.getPreferredSize();
b3.setBounds(150 + insets.left, 15 + insets.top,
             size.width + 50, size.height + 20);

...//In the main method:
Insets insets = frame.getInsets();
frame.setSize(300 + insets.left + insets.right,
              125 + insets.top + insets.bottom);


```

[« Previous](custom.html)
•
[Trail](../TOC.html)
•
[Next »](problems.html)

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

**Previous page:** Creating a Custom Layout Manager
  
**Next page:** Solving Common Layout Problems




A browser with JavaScript enabled is required for this page to operate properly.