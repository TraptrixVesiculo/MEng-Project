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

How to Use Separators

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

[« Previous](scrollpane.html) • [Trail](../TOC.html) • [Next »](slider.html)

# How to Use Separators

The
[`JSeparator`](http://download.oracle.com/javase/7/docs/api/javax/swing/JSeparator.html) class provides a horizontal or vertical dividing line
or empty space.
It's most commonly used in menus and tool bars.
In fact, you can use separators
without even knowing that a `JSeparator` class exists,
since [menus](menu.html)
and [tool bars](toolbar.html)
provide convenience methods
that create and add separators
customized for their containers.
Separators are somewhat similar to
[borders](../components/border.html), except that they are genuine components
and, as such,
are drawn inside a container,
rather than around the edges of a particular component.

Here is a picture of a menu that has three separators,
used to divide the menu into four groups of items:

![A menu with 4 parts, as indicated by 3 separators](../../figures/uiswing/components/MenuWithSeparators.png)

The code to add the menu items and separators to the menu
is extremely simple,
boiling down to something like this:

```

menu.add(menuItem1);
menu.add(menuItem2);
menu.add(menuItem3);
menu.addSeparator();
menu.add(rbMenuItem1);
menu.add(rbMenuItem2);
menu.addSeparator();
menu.add(cbMenuItem1);
menu.add(cbMenuItem2);
menu.addSeparator();
menu.add(submenu);

```

Adding separators to a tool bar is similar.
You can find the full code explained in the
how-to sections for
[menus](menu.html)
and [tool bars](toolbar.html).
If you want more control over separators in menus and tool bars,
you can directly use the
`JSeparator` subclasses that implement them:
[JPopupMenu.Separator](http://download.oracle.com/javase/7/docs/api/javax/swing/JPopupMenu.Separator.html) and
[JToolBar.Separator](http://download.oracle.com/javase/7/docs/api/javax/swing/JToolBar.Separator.html).
In particular, `JToolBar.Separator`
has API for specifying the separator's size.

### Using JSeparator

> You can use the `JSeparator` class directly
> to provide a dividing line in any container.
> The following picture shows a GUI
> that has a separator to the right of the button
> labeled Fire.
>
> ![A snapshot of ListDemo](../../figures/uiswing/components/ListDemo.png)
>
> Separators have almost no API and are extremely easy to use
> as long as you keep one thing in mind:
> In most implementations,
> a vertical separator has a preferred height of 0,
> and a horizontal separator has a preferred width of 0.
> This means a separator
> **is not visible**
> unless you either set its preferred size
> or put it in under the control of a layout manager
> such as `BorderLayout` or `BoxLayout`
> that stretches it to fill its available display area.
>
> The vertical separator does have a bit of width
> (and the horizontal a bit of height),
> so you should see some space where the separator is.
> However, the actual dividing line isn't drawn
> unless the width and height are both non-zero.
>
> The following code snippet
> shows how ListDemo puts together
> the panel that contains the vertical separator.
> You can find the full source code for ListDemo in
> [`ListDemo.java`](../examples/components/ListDemoProject/src/components/ListDemo.java).
>
> ```
>
> JPanel buttonPane = new JPanel();
> buttonPane.setLayout(new BoxLayout(buttonPane,
>                                    BoxLayout.LINE_AXIS));
> buttonPane.add(fireButton);
> buttonPane.add(Box.createHorizontalStrut(5));
> buttonPane.add(new JSeparator(SwingConstants.VERTICAL));
> buttonPane.add(Box.createHorizontalStrut(5));
> buttonPane.add(employeeName);
> buttonPane.add(hireButton);
> buttonPane.setBorder(BorderFactory.createEmptyBorder(5,5,5,5));
>
> ```
>
> As the code shows,
> the buttons, separator, and text field
> all share a single container —
> a `JPanel` instance
> that uses a left-to-right
> [box layout](../layout/box.html).
> Thanks to the layout manager
> (and to the fact that separators have unlimited maximum sizes),
> the separator is automatically made as tall
> as its available display area.
>
> In the preceding code,
> the horizontal struts are
> invisible components used to provide space
> around the separator.
> A 5-pixel empty border
> provides a cushion around the panel,
> and also serves to prevent the separator from extending
> all the way to the component above it
> and the window's edge below it.
>
> Here's a picture of another GUI
> that uses a separator,
> this time to put a dividing line
> between a group of controls
> and a display area.
>
> ![A snapshot of TextInputDemo](../../figures/uiswing/components/TextInputDemo.png)
>
> You can find the code in the
> [example index](../examples/components/index.html#TextInputDemo).
> Here is the code that sets up the separator's container:
>
> ```
>
> JPanel panel = new JPanel(new BorderLayout());
> ...
> panel.setBorder(BorderFactory.createEmptyBorder(
>                         GAP/2, //top
>                         0,     //left
>                         GAP/2, //bottom
>                         0));   //right
> panel.add(new JSeparator(JSeparator.VERTICAL),
>           BorderLayout.LINE_START);
> panel.add(addressDisplay,
>           BorderLayout.CENTER);
>
> ```
>
> As in the last example, the panel uses an empty border
> so that the separator doesn't
> extend all the way to the edges of its container.
> Placing the separator in the leftmost area of the
> `BorderLayout`-controlled container
> makes the separator as tall as the
> address-display component
> that's in the center of the container.
> See
> [How to Use BorderLayout](../layout/border.html) for details on how border layouts work.

### The Separator API

> The API for using separators is minimal,
> since they have no contents
> and don't respond to user input.
>
> Creating and Initializing Separators
>
> | Constructor or Method | Purpose |
> | [void addSeparator()](http://download.oracle.com/javase/7/docs/api/javax/swing/JToolBar.html#addSeparator())  [void addSeparator(Dimension)](http://download.oracle.com/javase/7/docs/api/javax/swing/JToolBar.html#addSeparator(java.awt.Dimension))   *(in `JToolBar`)* | Append a tool bar separator (which is invisible in most, if not all, look and feels) to the current end of the tool bar. The optional argument specifies the size of the separator. The no-argument version of this method uses a separator with a default size, as determined by the current look and feel. |
> | [void addSeparator()](http://download.oracle.com/javase/7/docs/api/javax/swing/JMenu.html#addSeparator())  [void insertSeparator(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JMenu.html#insertSeparator(int))   *(in `JMenu`)* | Put a separator in the menu. The `addSeparator` method puts the separator at the current end of the menu. The `insertSeparator` method inserts the separator into the menu at the specified position. |
> | [void addSeparator()](http://download.oracle.com/javase/7/docs/api/javax/swing/JPopupMenu.html#addSeparator())  *(in `JPopupMenu`)* | Put a separator at the current end of the popup menu. |
> | [JSeparator()](http://download.oracle.com/javase/7/docs/api/javax/swing/JSeparator.html#JSeparator())   [JSeparator(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JSeparator.html#JSeparator(int)) | Create a separator. If you don't specify an argument, the separator is horizontal. The argument can be either `SwingConstants.HORIZONTAL` or `SwingConstants.VERTICAL`. |
> | [void setOrientation(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JSeparator.html#setOrientation(int))   [int getOrientation()](http://download.oracle.com/javase/7/docs/api/javax/swing/JSeparator.html#getOrientation())  *(in `JSeparator`)* | Get or set the separator's orientation, which can be either `SwingConstants.HORIZONTAL` or `SwingConstants.VERTICAL`. |
> | [JToolBar.Separator()](http://download.oracle.com/javase/7/docs/api/javax/swing/JToolBar.Separator.html#JToolBar.Separator())  [JToolBar.Separator(Dimension)](http://download.oracle.com/javase/7/docs/api/javax/swing/JToolBar.Separator.html#JToolBar.Separator(java.awt.Dimension)) | Create a separator for use in a tool bar. The optional argument specifies the separator's size. |
> | [setSeparatorSize(Dimension)](http://download.oracle.com/javase/7/docs/api/javax/swing/JToolBar.Separator.html#setSeparatorSize(java.awt.Dimension))  *(in `JToolBar.Separator`)* | Specify the separator's size. More specifically, the specified `Dimension` is used as the separator's minimum, preferred, and maximum sizes. |
> | [JPopupMenu.Separator()](http://download.oracle.com/javase/7/docs/api/javax/swing/JPopupMenu.Separator.html#JPopupMenu.Separator()) | Create a separator for use in a menu. |

### Examples that Use Separators

> Several of this lesson's examples use separators,
> usually in menus.
> Here is a list of some of the more interesting examples.
>
> | Example | Where Described | Notes |
> | --- | --- | --- |
> | [`ListDemo`](../examples/components/index.html#ListDemo) | This section and [How to Use Lists](list.html) | Uses a vertical separator in a panel controlled by a horizontal box layout. |
> | [`TextInputDemo`](../examples/components/index.html#TextInputDemo) | This section and [How to Use Formatted Text Fields](formattedtextfield.html) | Uses a vertical separator at the left of a panel controlled by a border layout. |
> | [`MenuDemo`](../examples/components/index.html#MenuDemo) | This section and [How to Use Menus](menu.html) | Uses the `JMenu` method `addSeparator` to put separators in a menu. |
> | [`ToolBarDemo2`](../examples/components/index.html#ToolBarDemo2) | [How to Use Tool Bars](toolbar.html) | Uses the `JToolBar` method `addSeparator` to put space between two kinds of buttons. |

[« Previous](scrollpane.html)
•
[Trail](../TOC.html)
•
[Next »](slider.html)

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

**Previous page:** How to Use Scroll Panes
  
**Next page:** How to Use Sliders




A browser with JavaScript enabled is required for this page to operate properly.