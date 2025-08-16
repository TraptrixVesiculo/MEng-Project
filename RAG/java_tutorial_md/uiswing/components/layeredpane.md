[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Creating a GUI With JFC/Swing
  
**Lesson:** Using Swing Components
  
**Section:** How to Use Various Components

[Using Swing Components](index.html)

[Using Top-Level Containers](toplevel.html)

[The JComponent Class](jcomponent.html)

[Using Text Components](text.html)

[Text Component Features](generaltext.html)

[The Text Component API](textapi.html)

[How to Use Various Components](componentlist.html)

[How to Make Applets](applet.html)

[How to Use Buttons, Check Boxes, and Radio Buttons](button.html)

[How to Use the ButtonGroup Component](buttongroup.html)

[How to Use Color Choosers](colorchooser.html)

[How to Use Combo Boxes](combobox.html)

[How to Make Dialogs](dialog.html)

[How to Use Editor Panes and Text Panes](editorpane.html)

[How to Use File Choosers](filechooser.html)

[How to Use Formatted Text Fields](formattedtextfield.html)

[How to Make Frames (Main Windows)](frame.html)

[How to Use Internal Frames](internalframe.html)

[How to Use Labels](label.html)

How to Use Layered Panes

[How to Use Lists](list.html)

[How to Use Menus](menu.html)

[How to Use Panels](panel.html)

[How to Use Password Fields](passwordfield.html)

[How to Use Progress Bars](progress.html)

[How to Use Root Panes](rootpane.html)

[How to Use Scroll Panes](scrollpane.html)

[How to Use Separators](separator.html)

[How to Use Sliders](slider.html)

[How to Use Spinners](spinner.html)

[How to Use Split Panes](splitpane.html)

[How to Use Tabbed Panes](tabbedpane.html)

[How to Use Tables](table.html)

[How to Use Text Areas](textarea.html)

[How to Use Text Fields](textfield.html)

[How to Use Tool Bars](toolbar.html)

[How to Use Tool Tips](tooltip.html)

[How to Use Trees](tree.html)

[How to Use HTML in Swing Components](html.html)

[How to Use Models](model.html)

[How to Use Icons](icon.html)

[How to Use Borders](border.html)

[Solving Common Component Problems](problems.html)

[Home Page](../../index.html)
>
[Creating a GUI With JFC/Swing](../index.html)
>
[Using Swing Components](index.html)

[« Previous](label.html) • [Trail](../TOC.html) • [Next »](list.html)

# How to Use Layered Panes

A layered pane
is a Swing container that provides a third dimension
for positioning components:
*depth*, also known as *Z order*.
When adding a component to a layered pane,
you specify its depth as an integer.
The higher the number, closer the component is to the "top" position within the container.
If components overlap, the "closer"
components are drawn
on top of components at a lower depth.
The relationship between components at the same depth
is determined by their positions within the depth.

---

**Note:** The AWT Container has an API that allows you to manipulate component *Z order*. For
more information, see the
[AWT Focus Specification](http://java.sun.com/javase/6/docs/api/java/awt/doc-files/FocusSpec.html#ZOrder).

---

Every Swing container that has a
[root pane](rootpane.html) —
such as
[`JFrame`](frame.html),
[`JApplet`](applet.html),
[`JDialog`](dialog.html), or
[`JInternalFrame`](internalframe.html) —
automatically has a layered pane.
Most programs do not explicitly
use the root pane's layered pane,
so this section will not discuss it.
You can find information about it in
[The Root Pane](toplevel.html#rootpane),
which provides an overview, and
[The Layered Pane](rootpane.html#layeredpane),
which has further details. This section tells you how to create your own layered pane
and use it anywhere you can use a regular Swing container.

Swing provides two layered pane classes.
The first,
[`JLayeredPane`](http://download.oracle.com/javase/7/docs/api/javax/swing/JLayeredPane.html), is the class that root panes use
and is the class used by the
example in this section.
The second,
`JDesktopPane`,
is a `JLayeredPane` subclass
that is specialized for the task of holding internal frames.
For examples of using `JDesktopPane`,
see [How to Use Internal Frames](internalframe.html).

Here is a picture of an application that
creates a layered pane and places overlapping, colored
[labels](label.html) at different depths:

![A snapshot of LayeredPaneDemo](../../figures/uiswing/components/LayeredPaneDemoMetal.png)

---

**Try this::**

1. Click the Launch button to run the LayeredPane Demo using
   [Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp) ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
   Alternatively, to compile and run the example yourself,
   consult the
   [example index](../examples/components/index.html#LayeredPaneDemo).

   [![Launches the TreeDemo example](../../images/jws-launch-button.png)](http://download.oracle.com/javase/tutorialJWS/uiswing/components/ex6/LayeredPaneDemo.jnlp)

   - Move the mouse around in the lower part of the window.
     The image of Duke drags behind
     the green and red labels,
     but in front of the other three labels.- Use the combo box at the top of the window to change Duke's depth.
       Use the check box to set
       whether Duke is in the top position — position 0 — within
       the current depth.

---

Here is the code from
[`LayeredPaneDemo.java`](../examples/components/LayeredPaneDemoProject/src/components/LayeredPaneDemo.java) that creates the layered pane:

```

layeredPane = new JLayeredPane();
layeredPane.setPreferredSize(new Dimension(300, 310));
layeredPane.setBorder(BorderFactory.createTitledBorder(
                                    "Move the Mouse to Move Duke"));
layeredPane.addMouseMotionListener(new MouseMotionAdapter() {
    ...
});

```

The code uses `JLayeredPane`'s only constructor — the
no-argument constructor — to create the layered pane.
The rest of the code
uses methods inherited from superclasses
to give the layered pane a preferred size and a border,
and add a mouse-motion listener to it.
The mouse-motion listener
just moves the Duke image around in response to mouse movement.
Although we do not show the code here,
the example adds the layered pane to the frame's content pane.

As we will show you a bit later,
you add components to a layered pane using
an `add` method.
When adding a component to a layered pane,
you specify the component depth,
and optionally, its position within its depth.
The layered pane in the demo program contains
six labels — the five colored labels
and a sixth one that displays the Duke image.
As the program demonstrates,
both the depth of a component
and its position within that depth
can change dynamically.

The rest of this section covers these topics:

* [Adding Components and Setting Component Depth](#depth)* [Setting a Component Position Within Its Depth](#position)* [Laying Out Components in a Layered Pane](#layout)* [The Layered Pane API](#api)* [Examples that Use Layered Panes](#eg)

### Adding Components and Setting Component Depth
> Here is the code from the sample program that
> adds the colored labels to the layered pane:
>
> ```
>
> for (int i = 0; i < ...number of labels...; i++) {
>     JLabel label = createColoredLabel(...);
>     layeredPane.add(label, new Integer(i));
>     ...
> }
>
> ```
>
> You can find the implementation of
> the `createColoredLabel` method
> in the source code for the program.
> It just creates an opaque `JLabel`
> initialized with a background color,
> a border, some text, and a size.
>
> The example program uses a two-argument version
> of the `add` method.
> The first argument is the component to add,
> the second is an `Integer` object,
> specifying the depth.
> This program uses the `for` loop
> iteration variable to specify depths.
> The actual values do not matter much.
> What matters is the relative value of the depths
> and that you are consistent within your program
> in how you use each depth.
>
> ---
>
> **Note:** 
> If you use the root pane's layered pane,
> be sure to use its depth conventions.
> Refer to
> [The Layered Pane](rootpane.html#layeredpane)
> for details.
> That section shows you how to modify
> `LayeredPaneDemo` to use
> the root pane's layered pane.
> With the modifications,
> you can see how the dragging Duke image
> relates to the combo box in the control panel.
>
> ---
>
> As you can see from the example program,
> if components overlap,
> components at a higher depth
> are on top of components at a lower depth.
> To change a component depth dynamically,
> use the `setLayer` method.
> In the example,
> the user can change Duke's layer
> by making a selection from the combo box.
> Here is the `actionPerformed` method
> of the action listener registered on the combo box:
>
> ```
>
> public void actionPerformed(ActionEvent e) {
>     int position = onTop.isSelected() ? 0 : 1;
>     layeredPane.setLayer(dukeLabel,
>                          layerList.getSelectedIndex(),
>                          position);
> }
>
> ```
>
> The `setLayer` method used here
> takes three arguments:
> the component whose depth is to be set,
> the new depth, and the position within the depth.
> `JLayeredPane` has a two-argument version
> of `setLayer`
> that takes only the component and the new depth.
> That method puts the component at the bottom position in its depth.
>
> ---
>
> **A note of caution:** 
> When adding a component to a layered pane you specify
> the layer with an `Integer`.
> When using `setLayer` to change a component's
> layer, you use an `int`.
> You might think that
> if you use an `int`
> instead of an `Integer` with the `add`
> method, the compiler would complain
> or your program would throw an illegal argument exception.
> But the compiler says nothing, which results in a
> [common layered pane problem](problems.html#layeredpane).
> You can use the API tables at the end of this section
> to check the types of the arguments and return values
> for methods that deal with layers.
>
> ---

### Setting a Component's Position Within Its Depth
> The following code creates the label that displays Duke's image,
> and then adds the label to the layered pane.
>
> ```
>
> final ImageIcon icon = createImageIcon("images/dukeWaveRed.gif");
> ...
> dukeLabel = new JLabel(icon);
> ...
> dukeLabel.setBounds(15, 225,
>                     icon.getIconWidth(),
>                     icon.getIconHeight());
> ...
> layeredPane.add(dukeLabel, new Integer(2), 0);
>
> ```
>
> This code uses the three-argument version of the
> `add` method.
> The third argument specifies the Duke label
> position within its depth,
> which determines the component's relationship with
> other components at the same depth.
>
> Positions are specified with an `int`
> between -1 and (*n* - 1),
> where *n* is the number of components at the depth.
> Unlike layer numbers,
> the smaller the position number,
> the higher the component within its depth.
> Using -1 is the same as using *n* - 1;
> it indicates the bottom-most position.
> Using 0 specifies that the component should be
> in the top-most position within its depth.
> As the following figure shows,
> with the exception of -1,
> a lower position number indicates a higher position within a depth.
>
> ![How positions affect layering](../../figures/uiswing/components/positions.gif)
>
> A component's position within its layer can change dynamically.
> In the example, you can use the check box to
> determine whether Duke label is in the top position at its depth.
> Here's the `actionPerformed` method
> for the action listener registered on the check box:
>
> ```
>
> public void actionPerformed(ActionEvent e) {
>     if (onTop.isSelected())
>         layeredPane.moveToFront(dukeLabel);
>     else
>         layeredPane.moveToBack(dukeLabel);
> }
>
> ```
>
> When the user selects the check box,
> the `moveToFront` method moves Duke to the front (position 0).
> And when the user deselects check box,
> Duke gets moved to the back with the `moveToBack` method.
> You can also use the `setPosition` method or
> the three-argument version of `setLayer`
> to change a component's position.

### Laying Out Components in a Layered Pane
> By default a layered pane has no layout manager.
> This means that
> you typically have to write
> the code that positions and sizes the components
> you put in a layered pane.
>
> The example uses the `setBounds` method
> to set the size and position of each of the labels:
>
> ```
>
> dukeLabel.setBounds(15, 225,
>                     icon.getIconWidth(),
>                     icon.getIconHeight());
> ...
> label.setBounds(origin.x, origin.y, 140, 140);
>
> ```
>
> When the user moves the mouse around,
> the program calls `setPosition` to change Duke's position:
>
> ```
>
> dukeLabel.setLocation(e.getX()-XFUDGE, e.getY()-YFUDGE);
>
> ```
>
> Although a layered pane has no layout manager by default,
> you can still assign a layout manager to the layered pane.
> All of the layout managers provided by the Java platform
> arrange the components as if they were all on one layer.
> Here is a version of the previous demo
> that sets the layered pane's layout manager to an instance
> of `GridLayout`,
> using that layout manager to lay out six colored labels.
>
> ![A snapshot of LayeredPaneDemo2](../../figures/uiswing/components/LayeredPaneDemo2Metal.png)
>
> You can find the code for this program in
> [`LayeredPaneDemo2.java`](../examples/components/LayeredPaneDemo2Project/src/components/LayeredPaneDemo2.java).
> You can [run LayeredPaneDemo2](http://download.oracle.com/javase/tutorialJWS/uiswing/components/ex6/LayeredPaneDemo2.jnlp) (
> [download JDK 6](http://java.sun.com/javase/downloads/index.jsp)). If you want to compile the example,
> consult the
> [example index](../examples/components/index.html#LayeredPaneDemo2)
> for a list of all necessary files.
>
> Many programs use intermediate containers
> (such as panels) and their layout managers
> to lay out components on the same layer,
> but use absolute positioning to lay out components on different layers.
> For more information about absolute positioning, see
> [Doing Without a Layout Manager (Absolute Positioning)](../layout/none.html).

### The Layered Pane API

> The following tables list the commonly used
> `JLayeredPane` constructors and methods.
> Other methods you are most likely to invoke on
> a `JLayeredPane` object are those
> it inherits from its superclasses,
> such as `setBorder`, `setPreferredSize`, and so on.
> See
> [The JComponent API](jcomponent.html#api)
> for tables of commonly used inherited methods.
>
> The API for using layered pane falls into these categories:
>
> * [Creating or Getting a Layered Pane](#creating)* [Layering Components](#layers)* [Setting Component's Intra-Layer Positions](#positions)
>
> Creating or Getting a Layered Pane
>
> | Method or Constructor | Purpose |
> | [JLayeredPane()](http://download.oracle.com/javase/7/docs/api/javax/swing/JLayeredPane.html#JLayeredPane()) | Create a layered pane. |
> | [JLayeredPane getLayeredPane()](http://download.oracle.com/javase/7/docs/api/javax/swing/JApplet.html#getLayeredPane())   *(in `JApplet`, `JDialog`, `JFrame`, and `JInternalFrame`)* | Get the automatic layered pane in an applet, dialog, frame, or internal frame. |
>
> Layering Components
>
> | Method | Purpose |
> | [void add(Component)](http://download.oracle.com/javase/7/docs/api/java/awt/Container.html#add(java.awt.Component))   [void add(Component, Object)](http://download.oracle.com/javase/7/docs/api/java/awt/Container.html#add(java.awt.Component, java.lang.Object))   [void add(Component, Object, int)](http://download.oracle.com/javase/7/docs/api/java/awt/Container.html#add(java.awt.Component, java.lang.Object, int)) | Add the specified component to the layered pane. The second argument, when present, is an `Integer` that indicates the layer. The third argument, when present, indicates the component's position within its layer. If you use the one-argument version of this method, the component is added to layer 0. If you use the one- or two-argument version of this method, the component is placed underneath all other components currently in the same layer. |
> | [void setLayer(Component, int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JLayeredPane.html#setLayer(java.awt.Component, int))   [void setLayer(Component, int, int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JLayeredPane.html#setLayer(java.awt.Component, int, int)) | Change the component's layer. The second argument indicates the layer. The third argument, when present, indicates the component's position within its layer. |
> | [int getLayer(Component)](http://download.oracle.com/javase/7/docs/api/javax/swing/JLayeredPane.html#getLayer(java.awt.Component))   [int getLayer(JComponent)](http://download.oracle.com/javase/7/docs/api/javax/swing/JLayeredPane.html#getLayer(javax.swing.JComponent)) | Get the layer for the specified component. |
> | [int getComponentCountInLayer(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JLayeredPane.html#getComponentCountInLayer(int)) | Get the number of components in the specified layer. The value returned by this method can be useful for computing position values. |
> | [Component[] getComponentsInLayer(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JLayeredPane.html#getComponentsInLayer(int)) | Get an array of all the components in the specified layer. |
> | [int highestLayer()](http://download.oracle.com/javase/7/docs/api/javax/swing/JLayeredPane.html#highestLayer())   [int lowestLayer()](http://download.oracle.com/javase/7/docs/api/javax/swing/JLayeredPane.html#lowestLayer()) | Compute the highest or lowest layer currently in use. |
>
> Setting Components' Intra-Layer Positions
>
> | Method | Purpose |
> | [void setPosition(Component, int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JLayeredPane.html#setPosition(java.awt.Component, int))   [int getPosition(Component)](http://download.oracle.com/javase/7/docs/api/javax/swing/JLayeredPane.html#getPosition(java.awt.Component)) | Set or get the position for the specified component within its layer. |
> | [void moveToFront(Component)](http://download.oracle.com/javase/7/docs/api/javax/swing/JLayeredPane.html#moveToFront(java.awt.Component))   [void moveToBack(Component)](http://download.oracle.com/javase/7/docs/api/javax/swing/JLayeredPane.html#moveToBack(java.awt.Component)) | Move the specified component to the front or back of its layer. |

### Examples that Use Layered Panes

> This table shows the examples that use `JLayeredPane`
> and where those examples are described.
>
> | Example | Where Described | Notes |
> | --- | --- | --- |
> | [`LayeredPaneDemo`](../examples/components/index.html#LayeredPaneDemo) | This section | Illustrates layers and intra-layer positions of a `JLayeredPane`. |
> | [`LayeredPaneDemo2`](../examples/components/index.html#LayeredPaneDemo2) | This section | Uses a layout manager to help lay out the components in a layered pane. |
> | [`RootLayeredPaneDemo`](../examples/components/index.html#RootLayeredPaneDemo) | [The Layered Pane](rootpane.html#examplemods) | A version of [`LayeredPaneDemo`](../examples/components/index.html#LayeredPaneDemo) modified to use the root pane's layered pane. |
> | [`InternalFrameDemo`](../examples/components/index.html#InternalFrameDemo) | [How to Use Internal Frames](internalframe.html) | Uses a `JDesktopFrame` to manage internal frames. |

[« Previous](label.html)
•
[Trail](../TOC.html)
•
[Next »](list.html)

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

**Previous page:** How to Use Labels
  
**Next page:** How to Use Lists




A browser with JavaScript enabled is required for this page to operate properly.