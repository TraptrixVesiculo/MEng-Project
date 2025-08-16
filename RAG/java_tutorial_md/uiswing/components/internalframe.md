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

How to Use Internal Frames

[How to Use Labels](label.html)

[How to Use Layered Panes](layeredpane.html)

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

[« Previous](frame.html) • [Trail](../TOC.html) • [Next »](label.html)

# How to Use Internal Frames

With the
[`JInternalFrame`](http://download.oracle.com/javase/7/docs/api/javax/swing/JInternalFrame.html) class
you can display a
[`JFrame`](frame.html)-like window
within another window.
Usually, you add internal frames
to a desktop pane.
The desktop pane, in turn,
might be used as the content pane of a `JFrame`.
The desktop pane is an instance of
[`JDesktopPane`](http://download.oracle.com/javase/7/docs/api/javax/swing/JDesktopPane.html), which is a subclass of
[`JLayeredPane`](layeredpane.html)
that has added API for managing multiple overlapping internal frames.

You should consider carefully whether to base your program's GUI
around frames or internal frames.
Switching from internal frames to frames
or vice versa is not necessarily a simple task.
By experimenting with both frames and internal frames,
you can get an idea of the tradeoffs involved
in choosing one over the other.

Here is a picture of an application
that has two internal frames
(one of which is iconified)
inside a regular frame:

![InternalFrameDemo has multiple internal frames, managed by a desktop pane](../../figures/uiswing/components/InternalFrameDemoMetal.png)

---

**Try this:**

1. Click the Launch button to run InternalFrameDemo using
   [Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp) ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
   Alternatively, to compile and run the example yourself,
   consult the
   [example index](../examples/components/index.html#InternalFrameDemo).
   [![Launches the InternalFrameDemo example](../../images/jws-launch-button.png)](http://download.oracle.com/javase/tutorialJWS/uiswing/components/ex6/InternalFrameDemo.jnlp)

   - Create new internal frames
     using the Create item in the Document menu.
       
     Each internal frame comes up 30 pixels lower and to the right of
     the place where the previous internal frame first appeared.
     This functionality is implemented in the
     `MyInternalFrame` class,
     which is the custom subclass of `JInternalFrame`.

---

The following code,
taken from
[`InternalFrameDemo.java`](../examples/components/InternalFrameDemoProject/src/components/InternalFrameDemo.java),
creates the desktop and internal frames in the previous example.

```

...//In the constructor of InternalFrameDemo, a JFrame subclass:
    desktop = new JDesktopPane();
    createFrame(); //Create first window
    setContentPane(desktop);
    ...
    //Make dragging a little faster but perhaps uglier.
    desktop.setDragMode(JDesktopPane.OUTLINE_DRAG_MODE);
...
protected void createFrame() {
    MyInternalFrame frame = new MyInternalFrame();
    frame.setVisible(true);
    desktop.add(frame);
    try {
        frame.setSelected(true);
    } catch (java.beans.PropertyVetoException e) {}
}

...//In the constructor of MyInternalFrame, a JInternalFrame subclass:
static int openFrameCount = 0;
static final int xOffset = 30, yOffset = 30;

public MyInternalFrame() {
    super("Document #" + (++openFrameCount),
          true, //resizable
          true, //closable
          true, //maximizable
          true);//iconifiable
    //...Create the GUI and put it in the window...
    //...Then set the window size or call pack...
    ...
    //Set the window's location.
    setLocation(xOffset*openFrameCount, yOffset*openFrameCount);
}

```

### Internal Frames vs. Regular Frames

> The code for using internal frames
> is similar in many ways to the code for using regular Swing frames.
> Because internal frames have root panes,
> setting up the GUI for a `JInternalFrame`
> is very similar to setting up the GUI for a `JFrame`.
> `JInternalFrame` also provides
> other API,
> such as `pack`,
> that makes it similar to `JFrame`.
>
> ---
>
> **Note:** Just as for a regular frame,
> you must invoke `setVisible(true)` or `show()`
> on an internal frame to display it.
> The internal frame does not appear until you explicitly make it visible.
>
> ---
>
> Internal frames are not windows or top-level containers, however,
> which makes them different from frames.
> For example, you must add an internal frame
> to a container (usually a `JDesktopPane`);
> an internal frame cannot be the root of a containment hierarchy.
> Also, internal frames do not generate window events.
> Instead, the user actions that would
> cause a frame to fire window events
> cause an internal frame to fire internal frame events.
>
> Because internal frames are implemented with platform-independent code,
> they add some features that frames cannot give you.
> One such feature is that
> internal frames give you more control over
> their state and capabilities than frames do.
> You can programatically iconify or maximize an internal frame.
> You can also specify what icon goes in the internal frame's
> title bar.
> You can even specify whether the internal frame
> has the window decorations
> to support resizing, iconifying, closing, and maximizing.
>
> Another feature is that internal frames
> are designed to work within desktop panes.
> The `JInternalFrame` API
> contains methods such as `moveToFront`
> that work only if the internal frame's container
> is a layered pane such as a `JDesktopPane`.

### Rules of Using Internal Frames

> If you have built any programs using `JFrame`
> and the other Swing components,
> then you already know a lot
> about how to use internal frames.
> The following list
> summarizes the rules for using internal frames.
> For additional information, see
> [How to Make Frames](frame.html)
> and
> [The JComponent Class](jcomponent.html).
>
> **You must set the size of the internal frame.**: If you do not set the size of the internal frame, it will have zero size and thus never be visible. You can set the size using one of the following methods: `setSize`, `pack`, or `setBounds`. **As a rule, you should set the location of the internal frame.**: If you do not set the location of the internal frame, it will come up at 0,0 (the upper left of its container). You can use the `setLocation` or `setBounds` method to specify the upper left point of the internal frame, relative to its container. **To add components to an internal frame, you add them to the internal frame's content pane.**: This is exactly like the `JFrame` situation. See [Adding Components to the Content Pane](toplevel.html#contentpane) for details. **Dialogs that are internal frames should be implemented using `JOptionPane` or `JInternalFrame`, not `JDialog`.**: To create a simple dialog, you can use the `JOptionPane` `showInternalXxxDialog` methods, as described in [How to Make Dialogs](dialog.html). **You must add an internal frame to a container.**: If you do not add the internal frame to a container (usually a `JDesktopPane`), the internal frame will not appear. **You need to call `show` or `setVisible` on internal frames.**: Internal frames are invisible by default. You must invoke `setVisible(true)` or `show()` to make them visible. **Internal frames fire internal frame events, not window events.**: Handling internal frame events is almost identical to handling window events. See [How to Write an Internal Frame Listener](../events/internalframelistener.html) for more information.
>
> ---
>
> **Performance tip:**
> When a desktop has many internal frames,
> the user might notice that moving them seems slow.
> Outline dragging
> is one way to avoid this problem.
> With outline dragging,
> only the outline of the internal frame is painted
> at the current mouse position while the internal frame's being dragged.
> The internal frame's innards
> are not repainted at a new position until dragging stops.
> The default behavior (called *live* dragging)
> is to reposition and repaint some or all of internal frame continuously
> while it is being moved;
> this can be slow if the desktop has many internal frames.
>
> Use the `JDesktopPane` method
> `setDragMode`\*
> to specify outline dragging.
> For example:
>
> ```
>
> desktop.setDragMode(JDesktopPane.OUTLINE_DRAG_MODE);
>
> ```
>
> ---

### The Internal Frame API

> The following tables list the commonly used
> `JInternalFrame` constructors and methods,
> as well as a few methods that `JDesktopPane` provides.
> Besides the API listed in this section,
> `JInternalFrame` inherits useful API from
> its superclasses,
> `JComponent`,
> `Component`, and
> `Container`.
> See [The JComponent Class](jcomponent.html)
> for lists of methods from those classes.
>
> Like `JInternalFrame`,
> `JDesktopPane` descends from
> `JComponent`,
> and thus provides the methods described in
> [The JComponent Class](jcomponent.html).
> Because `JDesktopPane` extends
> `JLayeredPane`,
> it also supports the methods described in
> [The Layered Pane API](layeredpane.html#api).
>
> The API for using internal frames falls into these categories:
>
> * [Creating the internal frame](#construct)* [Adding components to the internal frame](#add)* [Specifying the internal frame's visibility, size, and location](#layout)* [Performing window operations on the internal frame](#window)* [Controlling window decorations and capabilities](#decorate)* [Using the JDesktopPane API](#JDesktopPane)
>
> Creating the Internal Frame
>
> | Constructor or Method | Purpose |
> | [JInternalFrame()](http://download.oracle.com/javase/7/docs/api/javax/swing/JInternalFrame.html#JInternalFrame())   [JInternalFrame(String)](http://download.oracle.com/javase/7/docs/api/javax/swing/JInternalFrame.html#JInternalFrame(java.lang.String))   [JInternalFrame(String, boolean)](http://download.oracle.com/javase/7/docs/api/javax/swing/JInternalFrame.html#JInternalFrame(java.lang.String, boolean))   [JInternalFrame(String, boolean, boolean)](http://download.oracle.com/javase/7/docs/api/javax/swing/JInternalFrame.html#JInternalFrame(java.lang.String, boolean, boolean))   [JInternalFrame(String, boolean, boolean, boolean)](http://download.oracle.com/javase/7/docs/api/javax/swing/JInternalFrame.html#JInternalFrame(java.lang.String, boolean, boolean, boolean))   [JInternalFrame(String, boolean, boolean, boolean, boolean)](http://download.oracle.com/javase/7/docs/api/javax/swing/JInternalFrame.html#JInternalFrame(java.lang.String, boolean, boolean, boolean, boolean)) | Create a `JInternalFrame` instance. The first argument specifies the title (if any) to be displayed by the internal frame. The rest of the arguments specify whether the internal frame should contain decorations allowing the user to resize, close, maximize, and iconify the internal frame (specified in that order). The default value for each boolean argument is `false`, which means that the operation is not allowed. |
> | [static int showInternalConfirmDialog(Component, Object)](http://download.oracle.com/javase/7/docs/api/javax/swing/JOptionPane.html#showInternalConfirmDialog(java.awt.Component, java.lang.Object))   [static String showInternalInputDialog(Component, Object)](http://download.oracle.com/javase/7/docs/api/javax/swing/JOptionPane.html#showInternalInputDialog(java.awt.Component, java.lang.Object))   [static Object showInternalMessageDialog(Component, Object)](http://download.oracle.com/javase/7/docs/api/javax/swing/JOptionPane.html#showInternalMessageDialog(java.awt.Component, java.lang.Object))   [static int showInternalOptionDialog(Component, Object, String, int, int, Icon, Object[], Object)](http://download.oracle.com/javase/7/docs/api/javax/swing/JOptionPane.html#showInternalOptionDialog(java.awt.Component, java.lang.Object, java.lang.String, int, int, javax.swing.Icon, java.lang.Object[], java.lang.Object)) | Create a `JInternalFrame` that simulates a dialog. See [How to Make Dialogs](dialog.html) for details. |
>
> Adding Components to the Internal Frame
>
> | Method | Purpose |
> | [void setContentPane(Container)](http://download.oracle.com/javase/7/docs/api/javax/swing/JInternalFrame.html#setContentPane(java.awt.Container))   [Container getContentPane()](http://download.oracle.com/javase/7/docs/api/javax/swing/JInternalFrame.html#getContentPane()) | Set or get the internal frame's content pane, which generally contains all of the internal frame's GUI, with the exception of the menu bar and window decorations. |
> | [void setJMenuBar(JMenuBar)](http://download.oracle.com/javase/7/docs/api/javax/swing/JInternalFrame.html#setJMenuBar(javax.swing.JMenuBar))   [JMenuBar getJMenuBar()](http://download.oracle.com/javase/7/docs/api/javax/swing/JInternalFrame.html#getJMenuBar()) | Set or get the internal frame's menu bar. |
> | [void setLayeredPane(JLayeredPane)](http://download.oracle.com/javase/7/docs/api/javax/swing/JInternalFrame.html#setLayeredPane(javax.swing.JLayeredPane))   [JLayeredPane getLayeredPane()](http://download.oracle.com/javase/7/docs/api/javax/swing/JInternalFrame.html#getLayeredPane()) | Set or get the internal frame's layered pane. |
>
> Specifying the Internal Frame's Visibility, Size, and Location| Method | Purpose |
> | [void setVisible(boolean)](http://download.oracle.com/javase/7/docs/api/javax/swing/JComponent.html#setVisible(boolean)) | Make the internal frame visible (if `true`) or invisible (if `false`). You should invoke `setVisible(true)` on each `JInternalFrame` before adding it to its container. (Inherited from `Component`). |
> | [void pack()](http://download.oracle.com/javase/7/docs/api/javax/swing/JInternalFrame.html#pack()) | Size the internal frame so that its components are at their preferred sizes. |
> | [void setLocation(Point)](http://download.oracle.com/javase/7/docs/api/java/awt/Component.html#setLocation(java.awt.Point))   [void setLocation(int, int)](http://download.oracle.com/javase/7/docs/api/java/awt/Component.html#setLocation(int, int)) | Set the position of the internal frame. (Inherited from `Component`). |
> | [void setBounds(Rectangle)](http://download.oracle.com/javase/7/docs/api/java/awt/Component.html#setBounds(java.awt.Rectangle))   [void setBounds(int, int, int, int)](http://download.oracle.com/javase/7/docs/api/java/awt/Component.html#setBounds(int, int, int, int)) | Explicitly set the size and location of the internal frame. (Inherited from `Component`). |
> | [void setSize(Dimension)](http://download.oracle.com/javase/7/docs/api/java/awt/Component.html#setSize(java.awt.Dimension))   [void setSize(int, int)](http://download.oracle.com/javase/7/docs/api/java/awt/Component.html#setSize(int, int)) | Explicitly set the size of the internal frame. (Inherited from `Component`). |
>
> Performing Window Operations
> on the Internal Frame
>
> | Method | Purpose |
> | [void setDefaultCloseOperation(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JInternalFrame.html#setDefaultCloseOperation(int))   [int getDefaultCloseOperation()](http://download.oracle.com/javase/7/docs/api/javax/swing/JInternalFrame.html#getDefaultCloseOperation()) | Set or get what the internal frame does when the user attempts to "close" the internal frame. The default value is `DISPOSE_ON_CLOSE`. Other possible values are `DO_NOTHING_ON_CLOSE` and `HIDE_ON_CLOSE` See [Responding to Window-Closing Events](frame.html#windowevents) for details. |
> | [void addInternalFrameListener(InternalFrameListener)](http://download.oracle.com/javase/7/docs/api/javax/swing/JInternalFrame.html#addInternalFrameListener(javax.swing.event.InternalFrameListener))   [void removeInternalFrameListener(InternalFrameListener)](http://download.oracle.com/javase/7/docs/api/javax/swing/JInternalFrame.html#removeInternalFrameListener(javax.swing.event.InternalFrameListener)) | Add or remove an internal frame listener (`JInternalFrame`'s equivalent of a window listener). See [How to Write an Internal Frame Listener](../events/internalframelistener.html) for more information. |
> | [void moveToFront()](http://download.oracle.com/javase/7/docs/api/javax/swing/JInternalFrame.html#moveToFront())   [void moveToBack()](http://download.oracle.com/javase/7/docs/api/javax/swing/JInternalFrame.html#moveToBack()) | If the internal frame's parent is a layered pane such as a desktop pane, moves the internal frame to the front or back (respectively) of its layer. |
> | [void setClosed(boolean)](http://download.oracle.com/javase/7/docs/api/javax/swing/JInternalFrame.html#setClosed(boolean))   [boolean isClosed()](http://download.oracle.com/javase/7/docs/api/javax/swing/JInternalFrame.html#isClosed()) | Set or get whether the internal frame is currently closed. The argument to `setClosed` must be `true`. When reopening a closed internal frame, you make it visible and add it to a container (usually the desktop pane you originally added it to). |
> | [void setIcon(boolean)](http://download.oracle.com/javase/7/docs/api/javax/swing/JInternalFrame.html#setIcon(boolean))   [boolean isIcon()](http://download.oracle.com/javase/7/docs/api/javax/swing/JInternalFrame.html#isIcon()) | Iconify or deiconify the internal frame, or determine whether it is currently iconified. |
> | [void setMaximum(boolean)](http://download.oracle.com/javase/7/docs/api/javax/swing/JInternalFrame.html#setMaximum(boolean))   [boolean isMaximum()](http://download.oracle.com/javase/7/docs/api/javax/swing/JInternalFrame.html#isMaximum()) | Maximize or restore the internal frame, or determine whether it is maximized. |
> | [void setSelected(boolean)](http://download.oracle.com/javase/7/docs/api/javax/swing/JInternalFrame.html#setSelected(boolean))   [boolean isSelected()](http://download.oracle.com/javase/7/docs/api/javax/swing/JInternalFrame.html#isSelected()) | Set or get whether the internal frame is the currently "selected" (activated) internal frame. |
>
> Controlling Window Decorations and Capabilities
>
> | Method | Purpose |
> | [void setFrameIcon(Icon)](http://download.oracle.com/javase/7/docs/api/javax/swing/JInternalFrame.html#setFrameIcon(javax.swing.Icon))   [Icon getFrameIcon()](http://download.oracle.com/javase/7/docs/api/javax/swing/JInternalFrame.html#getFrameIcon()) | Set or get the icon displayed in the title bar of the internal frame (usually in the top-left corner). |
> | [void setClosable(boolean)](http://download.oracle.com/javase/7/docs/api/javax/swing/JInternalFrame.html#setClosable(boolean))   [boolean isClosable()](http://download.oracle.com/javase/7/docs/api/javax/swing/JInternalFrame.html#isClosable()) | Set or get whether the user can close the internal frame. |
> | [void setIconifiable(boolean)](http://download.oracle.com/javase/7/docs/api/javax/swing/JInternalFrame.html#setIconifiable(boolean))   [boolean isIconifiable()](http://download.oracle.com/javase/7/docs/api/javax/swing/JInternalFrame.html#isIconifiable()) | Set or get whether the internal frame can be iconified. |
> | [void setMaximizable(boolean)](http://download.oracle.com/javase/7/docs/api/javax/swing/JInternalFrame.html#setMaximizable(boolean))   [boolean isMaximizable()](http://download.oracle.com/javase/7/docs/api/javax/swing/JInternalFrame.html#isMaximizable()) | Set or get whether the user can maximize this internal frame. |
> | [void setResizable(boolean)](http://download.oracle.com/javase/7/docs/api/javax/swing/JInternalFrame.html#setResizable(boolean))   [boolean isResizable()](http://download.oracle.com/javase/7/docs/api/javax/swing/JInternalFrame.html#isResizable()) | Set or get whether the internal frame can be resized. |
> | [void setTitle(String)](http://download.oracle.com/javase/7/docs/api/javax/swing/JInternalFrame.html#setTitle(java.lang.String))   [String getTitle()](http://download.oracle.com/javase/7/docs/api/javax/swing/JInternalFrame.html#getTitle()) | Set or get the window title. |
>
> Using the `JDesktopPane` API
>
> | Constructor or Method | Purpose |
> | [JDesktopPane()](http://download.oracle.com/javase/7/docs/api/javax/swing/JDesktopPane.html#JDesktopPane()) | Creates a new instance of `JDesktopPane`. |
> | [JInternalFrame[] getAllFrames()](http://download.oracle.com/javase/7/docs/api/javax/swing/JDesktopPane.html#getAllFrames()) | Returns all `JInternalFrame` objects that the desktop contains. |
> | [JInternalFrame[] getAllFramesInLayer(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JDesktopPane.html#getAllFramesInLayer(int)) | Returns all `JInternalFrame` objects that the desktop contains that are in the specified layer. See [How to Use Layered Panes](layeredpane.html) for information about layers. || [void setDragMode(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JDesktopPane.html#setDragMode(int))  [int getDragMode()](http://download.oracle.com/javase/7/docs/api/javax/swing/JDesktopPane.html#getDragMode()) | Set or get the drag mode used for internal frames in this desktop. The integer can be either `JDesktopPane.LIVE_DRAG_MODE` or `JDesktopPane.OUTLINE_DRAG_MODE`. The default for the Java look and feel is live-drag mode. |

### Examples that Use Internal Frames

> The following examples use internal frames.
> Because internal frames are similar to regular frames,
> you should also look at
> [Examples that Use Frames](frame.html#eg).
>
> | Example | Where Described | Notes |
> | --- | --- | --- |
> | [`MyInternalFrame`](../examples/components/index.html#InternalFrameDemo) | This page. | Implements an internal frame that appears at an offset to the previously created internal frame. |
> | [`InternalFrameDemo`](../examples/components/index.html#InternalFrameDemo) | This page. | Lets you create internal frames (instances of `MyInternalFrame`) that go into the application's `JDesktopPane`. |
> | [`InternalFrameEventDemo`](../examples/events/index.html#InternalFrameEventDemo) | [How to Write an Internal Frame Listener](../events/internalframelistener.html) | Demonstrates listening for internal frame events. Also demonstrates positioning internal frames within a desktop pane. |

[« Previous](frame.html)
•
[Trail](../TOC.html)
•
[Next »](label.html)

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

**Previous page:** How to Make Frames (Main Windows)
  
**Next page:** How to Use Labels




A browser with JavaScript enabled is required for this page to operate properly.