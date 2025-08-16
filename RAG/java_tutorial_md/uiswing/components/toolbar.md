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

How to Use Tool Bars

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

[« Previous](textfield.html) • [Trail](../TOC.html) • [Next »](tooltip.html)

# How to Use Tool Bars

A
[`JToolBar`](http://download.oracle.com/javase/7/docs/api/javax/swing/JToolBar.html) is a container that groups several components —
usually [buttons](button.html) with icons —
into a row or column.
Often, tool bars provide
easy access to functionality that is also in
[menus](menu.html).
[How to Use Actions](../misc/action.html)
describes how to provide the same functionality
in menu items and tool bar buttons.

The following images show an application
named `ToolBarDemo`
that contains a tool bar above a text area.
Click the Launch button
to run ToolBarDemo
using
[Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp )
([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
Alternatively, to compile and run it yourself, consult the
[example index](../examples/components/index.html#ToolBarDemo).

[![Launches the ToolBarDemo Application](../../images/jws-launch-button.png)](http://download.oracle.com/javase/tutorialJWS/uiswing/components/ex6/ToolBarDemo.jnlp)

![ToolBarDemo, with the tool bar in an initial north position](../../figures/uiswing/components/ToolBarDemo.png)

By default,
the user can drag the tool bar to another edge of its container
or out into a window of its own.
The next figure shows how the application looks
after the user has dragged the tool bar
to the right edge of its container.

![ToolBarDemo, after the tool bar is dragged to the east](../../figures/uiswing/components/ToolBarDemo-2.png)

For the drag behavior to work correctly,
the tool bar must be in a container
that uses the
[`BorderLayout`](../layout/border.html) layout manager. The component that the tool bar affects
is generally in the center of the container.
The tool bar must be the only other component in the container,
and it must not be in the center.

The next figure shows how the application looks
after the user has dragged the tool bar
outside its window.

![ToolBarDemo, after the tool bar is dragged out into its own window](../../figures/uiswing/components/ToolBarDemo-3.png)

The following code creates the tool bar
and adds it to a container.
You can find the entire program in
[`ToolBarDemo.java`](../examples/components/ToolBarDemoProject/src/components/ToolBarDemo.java).

```

public class ToolBarDemo extends JPanel
                         implements ActionListener {
    ...
    public ToolBarDemo() {
        super(new BorderLayout());
        ...
        JToolBar toolBar = new JToolBar("Still draggable");
        addButtons(toolBar);
        ...
        setPreferredSize(new Dimension(450, 130));
        add(toolBar, BorderLayout.PAGE_START);
        add(scrollPane, BorderLayout.CENTER);
    }
    ...
}

```

This code positions the tool bar above the scroll pane
by placing both components
in a panel controlled by a border layout,
with the
tool bar in the `PAGE_START` position and the
scroll pane in the `CENTER` position.
Because the scroll pane is in the center
and no other components except the tool bar are in the container,
by default the tool bar can be dragged
to other edges of the container.
The tool bar
can also be dragged out into its own window,
in which case the window
has the title "Still draggable",
as specified by the `JToolBar` constructor.

### Creating Tool Bar Buttons

> The buttons in the tool bar are ordinary
> `JButton` instances that use images
> from the
> Java Look and Feel Graphics Repository.
> Use images from the
> [Java Look and Feel Graphics Repository](http://java.sun.com/developer/techDocs/hi/repository/) if your tool bar
> has the Java look and feel.
>
> Here is the code that creates the buttons
> and adds them to the tool bar.
>
> ```
>
> protected void addButtons(JToolBar toolBar) {
>     JButton button = null;
>
>     //first button
>     button = makeNavigationButton("Back24", PREVIOUS,
>                                   "Back to previous something-or-other",
>                                   "Previous");
>     toolBar.add(button);
>
>     //second button
>     button = makeNavigationButton("Up24", UP,
>                                   "Up to something-or-other",
>                                   "Up");
>     toolBar.add(button);
>
>     ...//similar code for creating and adding the third button...
> }
>
> protected JButton makeNavigationButton(String imageName,
>                                        String actionCommand,
>                                        String toolTipText,
>                                        String altText) {
>     //Look for the image.
>     String imgLocation = "images/"
>                          + imageName
>                          + ".gif";
>     URL imageURL = ToolBarDemo.class.getResource(imgLocation);
>
>     //Create and initialize the button.
>     JButton button = new JButton();
>     button.setActionCommand(actionCommand);
>     button.setToolTipText(toolTipText);
>     button.addActionListener(this);
>
>     if (imageURL != null) {                      //image found
>         button.setIcon(new ImageIcon(imageURL, altText));
>     } else {                                     //no image found
>         button.setText(altText);
>         System.err.println("Resource not found: " + imgLocation);
>     }
>
>     return button;
> }
>
> ```
>
> The first call to `makeNavigationButton`
> creates the image for the first button,
> using the 24x24 "Back" navigation image
> in the graphics repository.
>
> Besides finding the image for the button,
> the `makeNavigationButton` method
> also creates the button,
> sets the strings for its action command and tool tip text,
> and adds the action listener for the button.
> If the image is missing,
> the method prints an error message
> and adds text to the button,
> so that the button is still usable.
>
> ---
>
> **Note:** If any buttons in your tool bar duplicate the functionality
> of other components, such as menu items,
> you should probably create and add the tool bar buttons
> as described in
> [How to Use Actions](../misc/action.html).
>
> ---

### Customizing Tool Bars

> By adding a few lines of code to the preceding example,
> we can demonstrate some more tool bar features:
>
> * Using `setFloatable(false)`
>   to make a tool bar immovable.* Using `setRollover(true)`
>     to visually indicate tool bar buttons
>     when the user passes over them with the cursor.* Adding a separator to a tool bar.* Adding a non-button component to a tool bar.
>
> You can see these features by running ToolBarDemo2.
> Click the Launch button
> to run ToolBarDemo2
> using
> [Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp )
> ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
> Alternatively, to compile and run it yourself, consult the
> [example index](../examples/components/index.html#ToolBarDemo2).
>
> [![Launches the ToolBarDemo2 Application](../../images/jws-launch-button.png)](http://download.oracle.com/javase/tutorialJWS/uiswing/components/ex6/ToolBarDemo2.jnlp)
>
> You can find the entire code for this program in
> [`ToolBarDemo2.java`](../examples/components/ToolBarDemo2Project/src/components/ToolBarDemo2.java). Below you can see a picture of a new UI using these customized features.
>
> ![ToolBarDemo2 shows a tool bar with a variety of components](../../figures/uiswing/components/ToolBarDemo2.png)
>
> Because the tool bar can no longer be dragged,
> it no longer has bumps at its left edge.
> Here is the code that turns off dragging:
>
> ```
>
> toolBar.setFloatable(false);
>
> ```
>
> The tool bar is in rollover mode,
> so the button under the cursor has a visual indicator.
> The kind of visual indicator depends on the look and feel.
> For example, the Metal look and feel uses a gradient effect
> to indicate the button under the cursor while
> other types of look and feel use borders for this purpose.
> Here is the code that sets rollover mode:
>
> ```
>
> toolBar.setRollover(true);
>
> ```
>
> Another visible difference in the example above
> is that the tool bar contains two new components,
> which are preceded by a blank space called a
> [separator](separator.html).
> Here is the code that adds the separator:
>
> ```
>
> toolBar.addSeparator();
>
> ```
>
> Here is the code that adds the new components:
>
> ```
>
> //fourth button
> button = new JButton("Another button");
> ...
> toolBar.add(button);
>
> //fifth component is NOT a button!
> JTextField textField = new JTextField("A text field");
> ...
> toolBar.add(textField);
>
> ```
>
> You can easily make the tool bar components
> either top-aligned or bottom-aligned
> instead of centered
> by invoking the `setAlignmentY` method.
> For example, to align the tops of all the components in a tool bar,
> invoke `setAlignmentY(TOP_ALIGNMENT)`
> on each component.
> Similarly, you can use the `setAlignmentX` method
> to specify the alignment of components when the tool bar is vertical.
> This layout flexibility is possible
> because tool bars use `BoxLayout`
> to position their components.
> For more information, see
> [How to Use BoxLayout](../layout/box.html).

### The Tool Bar API

> The following table lists the commonly used
> [`JToolBar`](http://download.oracle.com/javase/7/docs/api/javax/swing/JToolBar.html) constructors and methods.
> Other methods you might call
> are listed in the API tables in
> [The JComponent Class](jcomponent.html).
>
> | Method or Constructor | Purpose |
> | --- | --- |
> | [JToolBar()](http://download.oracle.com/javase/7/docs/api/javax/swing/JToolBar.html#JToolBar())   [JToolBar(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JToolBar.html#JToolBar(int))   [JToolBar(String)](http://download.oracle.com/javase/7/docs/api/javax/swing/JToolBar.html#JToolBar(java.lang.String))   [JToolBar(String, int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JToolBar.html#JToolBar(java.lang.String, int)) | Creates a tool bar. The optional int parameter lets you specify the orientation; the default is `HORIZONTAL`. The optional `String` parameter allows you to specify the title of the tool bar's window if it is dragged outside of its container. |
> | [Component add(Component)](http://download.oracle.com/javase/7/docs/api/java/awt/Container.html#add(java.awt.Component)) | Adds a component to the tool bar. You can associate a button with an `Action` using the `setAction(Action)` method defined by the `AbstractButton`. |
> | [void addSeparator()](http://download.oracle.com/javase/7/docs/api/javax/swing/JToolBar.html#addSeparator()) | Adds a separator to the end of the tool bar. |
> | [void setFloatable(boolean)](http://download.oracle.com/javase/7/docs/api/javax/swing/JToolBar.html#setFloatable(boolean))   [boolean isFloatable()](http://download.oracle.com/javase/7/docs/api/javax/swing/JToolBar.html#isFloatable()) | The floatable property is true by default, and indicates that the user can drag the tool bar out into a separate window. To turn off tool bar dragging, use `toolBar.setFloatable(false)`. Some types of look and feel might ignore this property. |
> | [void setRollover(boolean)](http://download.oracle.com/javase/7/docs/api/javax/swing/JToolBar.html#setRollover(boolean))   [boolean isRollover()](http://download.oracle.com/javase/7/docs/api/javax/swing/JToolBar.html#isRollover()) | The rollover property is false by default. To make tool bar buttons be indicated visually when the user passes over them with the cursor, set this property to true. Some types of look and feel might ignore this property. |

### Examples That Use Tool Bars

> This table lists examples that use `JToolBar`
> and points to where those examples are described.
>
> | Example | Where Described | Notes |
> | --- | --- | --- |
> | [`ToolBarDemo`](../examples/components/index.html#ToolBarDemo) | This page | A basic tool bar with icon-only buttons. |
> | [`ToolBarDemo2`](../examples/components/index.html#ToolBarDemo2) | This page | Demonstrates a non-floatable tool bar in rollover mode that contains a separator and a non-button component. |
> | [`ActionDemo`](../examples/misc/index.html#ActionDemo) | [How to Use Actions](../misc/action.html) | Implements a tool bar using `Action` objects. |

[« Previous](textfield.html)
•
[Trail](../TOC.html)
•
[Next »](tooltip.html)

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

**Previous page:** How to Use Text Fields
  
**Next page:** How to Use Tool Tips




A browser with JavaScript enabled is required for this page to operate properly.