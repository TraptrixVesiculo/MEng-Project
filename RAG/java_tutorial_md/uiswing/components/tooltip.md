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

[How to Use Tool Bars](toolbar.html)

How to Use Tool Tips

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

[« Previous](toolbar.html) • [Trail](../TOC.html) • [Next »](tree.html)

# How to Use Tool Tips

Creating a tool tip for any `JComponent`
object is easy.
Use the `setToolTipText` method
to set up a tool tip for the component.
For example, to add tool tips to three buttons,
you add only three lines of code:

```

b1.setToolTipText("Click this button to disable the middle button.");
b2.setToolTipText("This middle button does not react when you click it.");
b3.setToolTipText("Click this button to enable the middle button.");

```

When the user of the program
pauses with the cursor over any of the program's buttons,
the tool tip for the button comes up.
You can see this by running the `ButtonDemo` example,
which is explained in
[How to Use Buttons, Check Boxes, and Radio Buttons](button.html).
Here is a picture of the tool tip
that appears when the cursor pauses over the left button
in the `ButtonDemo` example.

![ButtonDemo showing a tool tip.](../../figures/uiswing/components/ButtonDemo-TT.png)

For components
such as tabbed panes
that have multiple parts,
it often makes sense to vary the tool tip text
to reflect the part of the component
under the cursor.
For example,
a tabbed pane might use this feature
to explain what will happen when you click the tab
under the cursor.
When you implement a tabbed pane,
you can specify the tab-specific tool tip text in an argument passed to
the `addTab` or `setToolTipTextAt` method.

Even in components that have no API for setting part-specific tool tip text,
you can generally do the job yourself.
If the component supports renderers,
then you can set the tool tip text on a custom renderer.
The
[table](table.html) and
[tree](tree.html) sections
provide examples of tool tip text
determined by a custom renderer.
An alternative that works for all `JComponent`s
is creating a subclass of the component
and overriding its
`getToolTipText(MouseEvent)` method.

### The Tool Tip API

> Most of the API you need in order to set up tool tips
> belongs to the `JComponent` class,
> and thus is inherited by most Swing components.
> More tool tip API can be found in individual classes
> such as `JTabbedPane`.
> In general, those APIs are sufficient
> for specifying and displaying tool tips;
> you usually do not need to deal directly with the implementing classes
> [`JToolTip`](http://download.oracle.com/javase/7/docs/api/javax/swing/JToolTip.html) and
> [`ToolTipManager`](http://download.oracle.com/javase/7/docs/api/javax/swing/ToolTipManager.html).
>
> The following table lists
> the tool tip API in the `JComponent` class.
> For information on individual components' support
> for tool tips,
> see the how-to section for the component in question.
>
> **Tool Tip API in the `JComponent` class**
>
> | Method | Purpose |
> | [setToolTipText(String)](http://download.oracle.com/javase/7/docs/api/javax/swing/JComponent.html#setToolTipText(java.lang.String)) | If the specified string is not null, then this method registers the component as having a tool tip and, when displayed, gives the tool tip the specified text. If the argument is null, then this method turns off the tool tip for this component. |
> | [String getToolTipText()](http://download.oracle.com/javase/7/docs/api/javax/swing/JComponent.html#getToolTipText()) | Returns the string that was previously specified with `setToolTipText`. |
> | [String getToolTipText(MouseEvent)](http://download.oracle.com/javase/7/docs/api/javax/swing/JComponent.html#getToolTipText(java.awt.event.MouseEvent)) | By default, returns the same value returned by `getToolTipText()`. Multi-part components such as [`JTabbedPane`](tabbedpane.html), [`JTable`](table.html), and [`JTree`](tree.html) override this method to return a string associated with the mouse event location. For example, each tab in a tabbed pane can have different tool tip text. |
> | [Point getToolTipLocation(MouseEvent)](http://download.oracle.com/javase/7/docs/api/javax/swing/JComponent.html#getToolTipLocation(java.awt.event.MouseEvent)) | Returns the location (in the receiving component's coordinate system) where the upper left corner of the component's tool tip appears. The argument is the event that caused the tool tip to be shown. The default return value is null, which tells the Swing system to choose a location. |

### Examples That Use Tool Tips

> This table lists some examples that use tool tips
> and points to where those examples are described.
>
> | Example | Where Described | Notes |
> | --- | --- | --- |
> | [`ButtonDemo`](../examples/components/index.html#ButtonDemo) | This section and [How to Use Buttons, Check Boxes, and Radio Buttons](button.html) | Uses a tool tip to provide instructions for a button. |
> | [`IconDemo`](../examples/components/index.html#IconDemo) | [How to Use Icons](../components/icon.html) | Uses a tool tip in a label to provide name and size information for an image. |
> | [`TabbedPaneDemo`](../examples/components/index.html#TabbedPaneDemo) | [How to Use Tabbed Panes](tabbedpane.html) | Uses tab-specific tool tip text specified in an argument to the `addTab` method. |
> | [`TableRenderDemo`](../examples/components/index.html#TableRenderDemo) | [Specifying Tool Tips for Cells](table.html#celltooltip) | Adds tool tips to a table using a renderer. |
> | [`TableToolTipsDemo`](../examples/components/index.html#TableToolTipsDemo) | [Specifying Tool Tips for Cells](table.html#celltooltip), [Specifying Tool Tips for Column Headers](table.html#headertooltip) | Adds tool tips to a table using various techniques. |
> | [`TreeIconDemo2`](../examples/components/index.html#TreeIconDemo2) | [Customizing a Tree's Display](tree.html#display) | Adds tool tips to a tree using a custom renderer. |
> | [`ActionDemo`](../examples/misc/index.html#ActionDemo) | [How to Use Actions](../misc/action.html) | Adds tool tips to buttons that have been created using `Action`s. |

[« Previous](toolbar.html)
•
[Trail](../TOC.html)
•
[Next »](tree.html)

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

**Previous page:** How to Use Tool Bars
  
**Next page:** How to Use Trees




A browser with JavaScript enabled is required for this page to operate properly.