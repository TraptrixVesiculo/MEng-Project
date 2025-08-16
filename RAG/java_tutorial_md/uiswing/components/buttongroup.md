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

How to Use the ButtonGroup Component

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

[« Previous](button.html) • [Trail](../TOC.html) • [Next »](colorchooser.html)

# How to Use the ButtonGroup Component

The `ButtonGroup` component manages the selected/unselected state for a set of buttons. For the group, the `ButtonGroup` instance guarantees that only one button can be selected at a time.

Initially, all buttons managed by a `ButtonGroup` instance are unselected.

### How to Use ButtonGroup Features

You can use `ButtonGroup` with any set of objects that inherit from `AbstractButton`. Typically a button group contains instances of `JRadioButton, JRadioButtonMenuItem`, or `JToggleButton`. It would not make sense to put an instance of `JButton` or `JMenuItem` in a button group because `JButton` and `JMenuItem` do not implement the select/deselect button state.

In general, you will typically follow these steps to write code that uses a `ButtonGroup` component.

1. Subclass `JFrame`
2. Call `ContextPane` together with a layout manager
3. Declare and configure a set of radio buttons or toggle buttons
4. Instantiate a `ButtonGroup` object
5. Call the `add` method on that buttongroup object in order to add each button to the group.

For details and a code example, see
[How to Use Radio Buttons](button.html#radiobutton).
It shows how to use a `ButtonGroup` component to group a
set of RadioButtons set into a JPanel.

### The ButtonGroup API

Commonly Used Button Group Constructors/Methods

| Constructor or Method | Purpose |
| [ButtonGroup()](http://download.oracle.com/javase/7/docs/api/javax/swing/ButtonGroup.html#ButtonGroup()) | Create a `ButtonGroup` instance. |
| [void add(AbstractButton)](http://download.oracle.com/javase/7/docs/api/javax/swing/ButtonGroup.html#add(javax.swing.AbstractButton))   [void remove(AbstractButton)](http://download.oracle.com/javase/7/docs/api/javax/swing/ButtonGroup.html#remove(javax.swing.AbstractButton)) | Add a button to the group, or remove a button from the group. |
| [public ButtonGroup getGroup()](http://download.oracle.com/javase/7/docs/api/javax/swing/DefaultButtonModel.html#getGroup())   *(in `DefaultButtonModel`)* | Get the `ButtonGroup`, if any, that controls a button. For example:   `ButtonGroup group = ((DefaultButtonModel)button.getModel()).getGroup();` |
| [public ButtonGroup clearSelection()](http://download.oracle.com/javase/7/docs/api/javax/swing/ButtonGroup.html#ButtonGroup()) | Clears the state of selected buttons in the ButtonGroup. None of the buttons in the ButtonGroup are selected . |

### ButtonGroup Examples

The following demonstration application uses the ButtonGroup component to group radio buttons displaying on a Window.

| Example | Where Described | Notes |
| --- | --- | --- |
| [`RadioButtonDemo`](../examples/components/index.html#RadioButtonDemo) | [How to Use Radio Buttons](button.html#radiobutton) | Uses radio buttons to determine which of five images it should display. |

[« Previous](button.html)
•
[Trail](../TOC.html)
•
[Next »](colorchooser.html)

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

**Previous page:** How to Use Buttons, Check Boxes, and Radio Buttons
  
**Next page:** How to Use Color Choosers




A browser with JavaScript enabled is required for this page to operate properly.