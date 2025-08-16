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

How to Make Frames (Main Windows)

[How to Use Internal Frames](internalframe.html)

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

[« Previous](formattedtextfield.html) • [Trail](../TOC.html) • [Next »](internalframe.html)

# How to Make Frames (Main Windows)

A Frame is a top-level window with a title and a border. The size of the frame includes any area designated for the border. The dimensions of the border area may be obtained using the `getInsets` method. Since the border area is included in the overall size of the frame, the border effectively obscures a portion of the frame, constraining the area available for rendering and/or displaying subcomponents to the rectangle which has an upper-left corner location of `(insets.left`, `insets.top)`, and has a size of `width - (insets.left + insets.right)` by `height - (insets.top + insets.bottom)`.

A frame, implemented as an instance of the
[`JFrame`](http://download.oracle.com/javase/7/docs/api/javax/swing/JFrame.html) class,
is a window that has decorations such as a border, a title,
and supports button components that close or iconify the window.
Applications with a GUI usually include at least one frame.
Applets sometimes use frames, as well.

To make a window that is dependent on another window —
disappearing when the other window is iconified, for example —
use a [`dialog`](dialog.html)
instead of `frame.`.
To make a window that appears within another window,
use an [internal frame](internalframe.html).
### Creating and Showing Frames
> Here is a picture of the extremely plain window
> created by the `FrameDemo` demonstration application.
> You can find the source code in
> [`FrameDemo.java`](../examples/components/FrameDemoProject/src/components/FrameDemo.java).
> You can
> [run FrameDemo](http://download.oracle.com/javase/tutorialJWS/uiswing/components/ex6/FrameDemo.jnlp) (
> [download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
>
> ![A very boring frame](../../figures/uiswing/components/FrameDemoMetal.png)
>
> The following `FrameDemo` code shows how to create and set up a frame.
>
> ```
>
>
> //1. Create the frame.
> JFrame frame = new JFrame("FrameDemo");
>
> //2. Optional: What happens when the frame closes?
> frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
>
> //3. Create components and put them in the frame.
> //...create emptyLabel...
> frame.getContentPane().add(emptyLabel, BorderLayout.CENTER);
>
> //4. Size the frame.
> frame.pack();
>
> //5. Show it.
> frame.setVisible(true);
>
> ```
>
> Here are some details about the code:
>
> 1. The first line of code creates a frame using a
>    constructor that lets you set the frame title.
>    The other frequently used `JFrame` constructor
>    is the no-argument constructor.
>
>    - Next the code specifies
>      what happens when your user closes the frame.
>      The `EXIT_ON_CLOSE` operation exits the program when your user closes the frame.
>      This behavior is appropriate for this program
>      because the program has only one frame,
>      and closing the frame makes the program useless.
>
>      See [Responding to Window-Closing Events](#windowevents)
>      for more information.
>
>      - The next bit of code adds a blank label to the frame content pane.
>        If you're not already familiar with content panes
>        and how to add components to them,
>        please read
>        [Adding Components to the Content Pane](toplevel.html#contentpane).
>
>        For frames that have menus,
>        you'd typically add the menu bar to the frame here
>        using the `setJMenuBar` method.
>        See [How to Use Menus](menu.html) for details.
>
>        - The `pack` method sizes the frame
>          so that all its contents are at
>          or above their preferred sizes.
>          An alternative to `pack`
>          is to establish a frame size explicitly
>          by calling `setSize`
>          or `setBounds`
>          (which also sets the frame location).
>          In general, using `pack`
>          is preferable to calling `setSize`,
>          since `pack`
>          leaves the frame layout manager in charge of the frame size,
>          and layout managers are good at adjusting to platform dependencies
>          and other factors that affect component size.
>
>          This example does not set the frame location,
>          but it is easy to do so
>          using either the `setLocationRelativeTo`
>          or `setLocation` method.
>          For example, the following code
>          centers a frame onscreen:
>          > ```
>          >
>          > frame.setLocationRelativeTo(null);
>          >
>          > ```
>
>          - Calling `setVisible(true)`
>            makes the frame appear onscreen.
>            Sometimes you might see the `show` method used instead.
>            The two usages are equivalent,
>            but we use `setVisible(true)` for consistency's sake.

### Specifying Window Decorations

> By default, window decorations are supplied by the native window system.
> However, you can request that the look-and-feel
> provide the decorations for a frame.
> You can also specify
> that the frame have no window decorations at all,
> a feature that can be used
> on its own,
> or to provide your own decorations,
> or with
> [full-screen exclusive mode](../../extra/fullscreen/index.html).
>
> Besides specifying who provides the window decorations,
> you can also specify which icon is used to represent the window.
> Exactly how this icon is used depends on the window system
> or look and feel that provides the window decorations.
> If the window system supports minimization,
> then the icon is used to represent the minimized window.
> Most window systems or look and feels
> also display the icon in the window decorations.
> A typical icon size is 16x16 pixels,
> but some window systems use other sizes.
>
> The following snapshots show three frames
> that are identical
> except for their window decorations.
> As you can tell by the appearance of the
> button in each frame,
> all three use the Java look and feel.
> The first uses decorations provided by the window system, which happen
> to be Microsoft Windows, but could as easily be any other system running
> the Java platform.The
> second and third use window decorations
> provided by the Java look and feel.
> The third frame uses Java look and feel window decorations,
> but has a custom icon.
> > |  |  |  |
> > | --- | --- | --- |
> > | A frame with decorations provided by the window system | A frame with decorations provided by the look and feel | A frame with a custom icon |
> > | Window decorations provided by the look and feel | Window decorations provided by the window system | Custom icon; window decorations provided by the look and feel |
>
> Here is an example of
> creating a frame with a custom icon
> and with window decorations provided by the look and feel:
>
> ```
>
> //Ask for window decorations provided by the look and feel.
> JFrame.setDefaultLookAndFeelDecorated(true);
>
> //Create the frame.
> JFrame frame = new JFrame("A window");
>
> //Set the frame icon to an image loaded from a file.
> frame.setIconImage(new ImageIcon(imgURL).getImage());
>
> ```
>
> As the preceding code snippet implies,
> you must invoke the `setDefaultLookAndFeelDecorated` method
> *before* creating the frame
> whose decorations you wish to affect.
> The value you set with `setDefaultLookAndFeelDecorated`
> is used for all subsequently created `JFrame`s.
> You can switch back to using window system decorations
> by invoking `JFrame.setDefaultLookAndFeelDecorated(false)`.
> Some look and feels might not support window decorations;
> in this case, the window system decorations are used.
>
> The full source code for the application
> that creates the frames pictured above is in
> [`FrameDemo2.java`](../examples/components/FrameDemo2Project/src/components/FrameDemo2.java).
> Besides showing how to choose window decorations,
> FrameDemo2 also shows how to disable all window decorations
> and gives an example of positioning windows.
> It includes two methods that create the `Image` objects
> used as icons —
> one is loaded from a file,
> and the other is painted from scratch.
>
> ---
>
> **Try this::**
>
> 1. Click the Launch button to run the Frame Demo using
>    [Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp) ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
>    Alternatively, to compile and run the example yourself,
>    consult the
>    [example index](../examples/components/index.html#FrameDemo2).
>
>    [![Launches the FrameDemo2 example](../../images/jws-launch-button.png)](http://download.oracle.com/javase/tutorialJWS/uiswing/components/ex6/FrameDemo2.jnlp)
>
>    - Bring up two windows, both with look-and-feel-provided decorations,
>      but with different icons.
>        
>      The Java look and feel displays the icons
>      in its window decorations.
>      Depending on your window system,
>      the icon may be used elsewhere to represent the window,
>      especially when the window is minimized.- Bring up one or more windows with window system decorations.
>          
>        See if your window system treats these icons differently.- Bring up one or more windows with no window decorations.
>            
>          Play with the various types of windows
>          to see how the window decorations,
>          window system, and frame icons interact.
>
> ---

### Responding to Window-Closing Events
> By default,
> when the user closes a frame onscreen,
> the frame is hidden.
> Although invisible,
> the frame still exists and the program can make it visible again.
> If you want different behavior,
> then you need to either
> register a window listener
> that handles window-closing events,
> or you need to specify default close behavior using
> the `setDefaultCloseOperation` method.
> You can even do both.
>
> The argument to `setDefaultCloseOperation`
> must be one of the following values,
> the first three of which are defined in the
> [`WindowConstants`](http://download.oracle.com/javase/7/docs/api/javax/swing/WindowConstants.html) interface
> (implemented by `JFrame`,
> `JInternalPane`,
> and `JDialog`):
>
> `DO_NOTHING_ON_CLOSE`: Do not do anything when the user requests that the window close. Instead, the program should probably use a window listener that performs some other action in its `windowClosing` method. `HIDE_ON_CLOSE` (the default for `JDialog` and `JFrame`): Hide the window when the user closes it. This removes the window from the screen but leaves it displayable. `DISPOSE_ON_CLOSE` (the default for `JInternalFrame`): Hide and dispose of the window when the user closes it. This removes the window from the screen and frees up any resources used by it. `EXIT_ON_CLOSE` (defined in the [`JFrame`](http://download.oracle.com/javase/7/docs/api/javax/swing/JFrame.html) class): Exit the application, using `System.exit(0)`. This is recommended for applications only. If used within an applet, a `SecurityException` may be thrown.
>
> ---
>
> **Note:**
> `DISPOSE_ON_CLOSE` can have results similar to
> `EXIT_ON_CLOSE` if only one window is onscreen.
> More precisely, when the last displayable window
> within the Java virtual machine (VM) is disposed of,
> the VM may terminate.
> See
> [AWT Threading Issues](http://download.oracle.com/javase/7/docs/api/java/awt/doc-files/AWTThreadIssues.html) for details.
>
> ---

The default close operation is executed after any
window listeners handle the window-closing event.
So, for example, assume that you specify that the default close
operation is to dispose of a frame.
You also implement a window listener
that tests whether the frame is the last one visible
and, if so, saves some data and exits the application.
Under these conditions,
when the user closes a frame,
the window listener will be called first.
If it does not exit the application,
then the default close operation —
disposing of the frame —
will then be performed.

For more information about handling window-closing events,
see
[How to Write Window Listeners](../events/windowlistener.html).
Besides handling window-closing events,
window listeners can also react to
other window state changes,
such as iconification and activation.

### The Frame API

> The following tables list the commonly used
> `JFrame` constructors and methods.
> Other methods you might want to call
> are defined by the
> [`java.awt.Frame`](http://download.oracle.com/javase/7/docs/api/java/awt/Frame.html),
> [`java.awt.Window`](http://download.oracle.com/javase/7/docs/api/java/awt/Window.html), and
> [`java.awt.Component`](http://download.oracle.com/javase/7/docs/api/java/awt/Component.html) classes,
> from which `JFrame` descends.
>
> Because each `JFrame` object has a root pane,
> frames have support for interposing input and painting behavior
> in front of the frame children, placing children on different "layers",
> and for Swing menu bars.
> These topics are introduced in
> [Using Top-Level Containers](toplevel.html)
> and explained in detail in
> [How to Use Root Panes](rootpane.html).
>
> The API for using frames falls into these categories:
>
> * [Creating and Setting Up a Frame](#creating)* [Setting the Window Size and Location](#sizeplace)* [Methods Related to the Root Pane](#rootpane)
>
> Creating and Setting Up a Frame
>
> | Method or Constructor | Purpose |
> | [JFrame()](http://download.oracle.com/javase/7/docs/api/javax/swing/JFrame.html#JFrame())   [JFrame(String)](http://download.oracle.com/javase/7/docs/api/javax/swing/JFrame.html#JFrame(java.lang.String)) | Create a frame that is initially invisible. The `String` argument provides a title for the frame. To make the frame visible, invoke `setVisible(true)` on it. |
> | [void setDefaultCloseOperation(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JFrame.html#setDefaultCloseOperation(int))   [int getDefaultCloseOperation()](http://download.oracle.com/javase/7/docs/api/javax/swing/JFrame.html#getDefaultCloseOperation()) | Set or get the operation that occurs when the user pushes the close button on this frame. Possible choices are:  * `DO_NOTHING_ON_CLOSE`* `HIDE_ON_CLOSE`* `DISPOSE_ON_CLOSE`* `EXIT_ON_CLOSE`  The first three constants are defined in the [`WindowConstants`](http://download.oracle.com/javase/7/docs/api/javax/swing/WindowConstants.html) interface, which `JFrame` implements. The `EXIT_ON_CLOSE` constant is defined in the [`JFrame`](http://download.oracle.com/javase/7/docs/api/javax/swing/JFrame.html) class. |
> | [void setIconImage(Image)](http://download.oracle.com/javase/7/docs/api/java/awt/Frame.html#setIconImage(java.awt.Image))   [Image getIconImage()](http://download.oracle.com/javase/7/docs/api/java/awt/Frame.html#getIconImage())  *(in `Frame`)* | Set or get the icon that represents the frame. Note that the argument is a [java.awt.Image](http://download.oracle.com/javase/7/docs/api/java/awt/Image.html) object, not a `javax.swing.ImageIcon` (or any other `javax.swing.Icon` implementation). |
> | [void setTitle(String)](http://download.oracle.com/javase/7/docs/api/java/awt/Frame.html#setTitle(java.lang.String))   [String getTitle()](http://download.oracle.com/javase/7/docs/api/java/awt/Frame.html#getTitle())  *(in `Frame`)* | Set or get the frame title. |
> | [void setUndecorated(boolean)](http://download.oracle.com/javase/7/docs/api/java/awt/Frame.html#setUndecorated(boolean))   [boolean isUndecorated()](http://download.oracle.com/javase/7/docs/api/java/awt/Frame.html#isUndecorated())  *(in `Frame`)* | Set or get whether this frame should be decorated. Works only if the frame is not yet displayable (has not been packed or shown). Typically used with [full-screen exclusive mode](../../extra/fullscreen/index.html) or to enable custom window decorations. |
> | [static void setDefaultLookAndFeelDecorated(boolean)](http://download.oracle.com/javase/7/docs/api/javax/swing/JFrame.html#setDefaultLookAndFeelDecorated(boolean))   [static boolean isDefaultLookAndFeelDecorated()](http://download.oracle.com/javase/7/docs/api/javax/swing/JFrame.html#isDefaultLookAndFeelDecorated()) | Determine whether subsequently created `JFrame`s should have their Window decorations (such as borders, and widgets for closing the window) provided by the current look-and-feel. Note that this is only a hint, as some look and feels may not support this feature. |
>
> Setting the Window Size and Location
>
> | Method | Purpose |
> | [void pack()](http://download.oracle.com/javase/7/docs/api/java/awt/Window.html#pack())  *(in `Window`)* | Size the window so that all its contents are at or above their preferred sizes. |
> | [void setSize(int, int)](http://download.oracle.com/javase/7/docs/api/java/awt/Component.html#setSize(int,%20int))  [void setSize(Dimension)](http://download.oracle.com/javase/7/docs/api/java/awt/Component.html#setSize(java.awt.Dimension))  [Dimension getSize()](http://download.oracle.com/javase/7/docs/api/java/awt/Component.html#getSize())  *(in `Component`)* | Set or get the total size of the window. The integer arguments to `setSize` specify the width and height, respectively. |
> | [void setBounds(int, int, int, int)](http://download.oracle.com/javase/7/docs/api/java/awt/Component.html#setBounds(int,%20int,%20int,%20int))  [void setBounds(Rectangle)](http://download.oracle.com/javase/7/docs/api/java/awt/Component.html#setBounds(java.awt.Rectangle))  [Rectangle getBounds()](http://download.oracle.com/javase/7/docs/api/java/awt/Component.html#getBounds())  *(in `Component`)* | Set or get the size and position of the window. For the integer version of `setBounds`, the window upper left corner is at the *x, y* location specified by the first two arguments, and has the width and height specified by the last two arguments. |
> | [void setLocation(int, int)](http://download.oracle.com/javase/7/docs/api/java/awt/Component.html#setLocation(int,%20int))  [Point getLocation()](http://download.oracle.com/javase/7/docs/api/java/awt/Component.html#getLocation())  *(in `Component`)* | Set or get the location of the upper left corner of the window. The parameters are the *x* and *y* values, respectively. |
> | [void setLocationRelativeTo(Component)](http://download.oracle.com/javase/7/docs/api/java/awt/Window.html#setLocationRelativeTo(java.awt.Component))  *(in `Window`)* | Position the window so that it is centered over the specified component. If the argument is `null`, the window is centered onscreen. To properly center the window, you should invoke this method after the window size has been set. |
>
> Methods Related to the Root Pane
>
> | Method | Purpose |
> | [void setContentPane(Container)](http://download.oracle.com/javase/7/docs/api/javax/swing/JFrame.html#setContentPane(java.awt.Container))   [Container getContentPane()](http://download.oracle.com/javase/7/docs/api/javax/swing/JFrame.html#getContentPane()) | Set or get the frame content pane. The content pane contains the visible GUI components within the frame. |
> | [JRootPane createRootPane()](http://download.oracle.com/javase/7/docs/api/javax/swing/JFrame.html#createRootPane())   [void setRootPane(JRootPane)](http://download.oracle.com/javase/7/docs/api/javax/swing/JFrame.html#setRootPane(javax.swing.JRootPane))   [JRootPane getRootPane()](http://download.oracle.com/javase/7/docs/api/javax/swing/JFrame.html#getRootPane()) | Create, set, or get the frame root pane. The root pane manages the interior of the frame including the content pane, the glass pane, and so on. |
> | [void setJMenuBar(JMenuBar)](http://download.oracle.com/javase/7/docs/api/javax/swing/JFrame.html#setJMenuBar(javax.swing.JMenuBar))   [JMenuBar getJMenuBar()](http://download.oracle.com/javase/7/docs/api/javax/swing/JFrame.html#getJMenuBar()) | Set or get the frame menu bar to manage a set of menus for the frame. |
> | [void setGlassPane(Component)](http://download.oracle.com/javase/7/docs/api/javax/swing/JFrame.html#setGlassPane(java.awt.Component))   [Component getGlassPane()](http://download.oracle.com/javase/7/docs/api/javax/swing/JFrame.html#getGlassPane()) | Set or get the frame glass pane. You can use the glass pane to intercept mouse events or paint on top of your program GUI. |
> | [void setLayeredPane(JLayeredPane)](http://download.oracle.com/javase/7/docs/api/javax/swing/JFrame.html#setLayeredPane(javax.swing.JLayeredPane))   [JLayeredPane getLayeredPane()](http://download.oracle.com/javase/7/docs/api/javax/swing/JFrame.html#getLayeredPane()) | Set or get the frame layered pane. You can use the frame layered pane to put components on top of or behind other components. |

### Examples that Use Frames

> All of the standalone applications in this trail
> use `JFrame`.
> The following table lists a few
> and tells you where each is discussed.
>
> | Example | Where Described | Notes |
> | --- | --- | --- |
> | [`FrameDemo`](../examples/components/index.html#FrameDemo) | [The Example Explained](#anexample) | Displays a basic frame with one component. |
> | [`FrameDemo2`](../examples/components/index.html#FrameDemo2) | [Specifying Window Decorations](#setDefaultLookAndFeelDecorated) | Lets you create frames with various window decorations. |
> | [`Framework`](../examples/components/index.html#Framework) | — | A study in creating and destroying windows, in implementing a menu bar, and in exiting an application. |
> | [`LayeredPaneDemo`](../examples/components/index.html#LayeredPaneDemo) | [How to Use Layered Panes](layeredpane.html) | Illustrates how to use a layered pane (but not the frame layered pane). |
> | [`GlassPaneDemo`](../examples/components/index.html#GlassPaneDemo) | [The Glass Pane](rootpane.html#glasspane) | Illustrates the use of a frame glass pane. |
> | [`MenuDemo`](../examples/components/index.html#MenuDemo) | [How to Use Menus](menu.html) | Shows how to put a `JMenuBar` in a `JFrame`. |

[« Previous](formattedtextfield.html)
•
[Trail](../TOC.html)
•
[Next »](internalframe.html)

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

**Previous page:** How to Use Formatted Text Fields
  
**Next page:** How to Use Internal Frames




A browser with JavaScript enabled is required for this page to operate properly.