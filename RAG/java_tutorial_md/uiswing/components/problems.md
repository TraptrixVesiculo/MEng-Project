[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Creating a GUI With JFC/Swing
  
**Lesson:** Using Swing Components

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

[How to Use Tool Tips](tooltip.html)

[How to Use Trees](tree.html)

[How to Use HTML in Swing Components](html.html)

[How to Use Models](model.html)

[How to Use Icons](icon.html)

[How to Use Borders](border.html)

Solving Common Component Problems

[Home Page](../../index.html)
>
[Creating a GUI With JFC/Swing](../index.html)
>
[Using Swing Components](index.html)

[« Previous](border.html) • [Trail](../TOC.html) • [Next »](../QandE/questions-ch3.html)

# Solving Common Component Problems

This section discusses problems that you might encounter
while using components.
If you do not find your problem in this section,
consult
the following sections:

* [Solving Common Problems Using Other Swing Features](../misc/problems.html)* [Solving Common Layout Problems](../layout/problems.html)* [Solving Common Event-Handling Problems](../events/problems.html)* [Solving Common Painting Problems](../painting/problems.html)

**Problem:**
I am having trouble implementing a model
(or some other code that is similar to something
already in Java SE Platform, Standard Edition).

* Look at the Java SE source code.
  It is distributed with the JDK,
  and it is a great resource for finding code examples
  of implementing models, firing events, and the like.

**Problem:**
Whenever the text in my text field updates,
the text field's size changes.

* You should specify the preferred width
  of the text field
  by specifying the number of columns it should have room to display.
  To do this, you can use either an `int` argument
  to the `JTextField` constructor
  or the `setColumns` method.

**Problem:**
Certain areas of the content pane look weird when they are repainted.

* If you set the content pane,
  make sure it is opaque.
  You can do this by invoking
  `setOpaque(true)` on your content pane.
  Note that although `JPanel`s are opaque in most look and feels,
  that is not true in the GTK+ look and feel.
  See [Adding Components
  to the Content Pane](toplevel.html#contentpane) for details.* If one or more of your components performs custom painting,
    make sure you implemented it correctly.
    See
    [Solving Common Painting Problems](../painting/problems.html) for help.* You might have a thread safety problem.
      See the next entry.

**Problem:**
My program is exhibiting weird symptoms
that sometimes seem to be related to timing.

* Make sure your code is thread-safe. See
  [Concurrency in Swing](../concurrency/index.html) for details.

**Problem:**
My modal dialog gets lost behind other windows.

* If the dialog has a null parent component,
  try setting it to a valid frame or component when you create it.* This bug was fixed in the 6.0 release. For more information, see
    [4255200](http://developer.java.sun.com/developer/bugParade/bugs/4255200.html).

**Problem:**
The scroll bar policies do not seem to be working as advertised.

* Some Swing releases contain bugs in the implementations for
  the `VERTICAL_SCROLLBAR_AS_NEEDED`
  and the `HORIZONTAL_SCROLLBAR_AS_NEEDED` policies.
  If feasible for your project,
  use the most recent release of Swing.* If the scroll pane's client can change size dynamically,
    the program should set the client's preferred size
    and then call `revalidate` on the client.* Make sure you specified the policy you intended
      for the orientation you intended.

**Problem:**
My scroll pane has no scroll bars.

* If you want a scroll bar to appear all the time,
  specify either `VERTICAL_SCROLLBAR_ALWAYS` or
  `HORIZONTAL_SCROLLBAR_ALWAYS` for the scroll bar
  policy as appropriate.* If you want the scroll bars to appear as needed,
    and you want to force the scroll bars to be needed
    when the scroll pane is created, you have two choices:
    either set the preferred size of scroll pane or its container,
    or implement a scroll-savvy class and return a value
    smaller than the component's standard preferred size
    from the `getPreferredScrollableViewportSize` method.
    Refer to
    [Sizing a Scroll Pane](scrollpane.html#sizing)
    for information.

**Problem:**
The divider in my split pane does not move!

* You need to set the minimum size of at least
  one of the components in the split pane.
  Refer to
  [Positioning the Divider
  and Restricting Its Range](splitpane.html#divider)
  for information.

**Problem:**
The `setDividerLocation` method
of `JSplitPane`
does not work.

* The `setDividerLocation(double)` method
  has no effect if the split pane has no size
  (typically true if it is not onscreen yet).
  You can either use `setDividerLocation(int)`
  or specify the preferred sizes of
  the split pane's contained components
  and the split pane's resize weight instead.
  Refer to
  [Positioning the Divider
  and Restricting Its Range](splitpane.html#divider)
  for information.

**Problem:**
The borders on nested split panes look too wide.

* If you nest split panes,
  the borders accumulate — the border of the inner split
  panes display next to the border of the outer split pane
  causing borders that look extra wide.
  The problem is particularly noticeable
  when nesting many split panes.
  The workaround is to set the border to null on any split
  pane that is placed within another split pane.
  For information,
  see bug #
  [4131528](http://developer.java.sun.com/developer/bugParade/bugs/4131528.html) in the Bug Database at the Sun Developer Network (SDN).
**Problem:**
The buttons in my tool bar are too big.

* Try reducing the margin for the buttons.
  For example:

  ```

  button.setMargin(new Insets(0,0,0,0));

  ```

**Problem:**
The components in my layered pane
are not layered correctly.
In fact, the layers seem to be inversed — the
lower the depth the higher the component.

* This can happen if you use an `int`
  instead of an `Integer`
  when adding components to a layered pane.
  To see what happens,
  make the following change to `LayeredPaneDemo`:

  | Change this... | to this... |
  | --- | --- |
  | `layeredPane.add(label, new Integer(i));` | `layeredPane.add(label, i);` |

**Problem:**
The method call
`colorChooser.setPreviewPanel(null)`
does not remove the color chooser's preview panel as expected.

* A `null` argument specifies the default preview panel.
  To remove the preview panel, specify a standard panel with no
  size, like this:
  `colorChooser.setPreviewPanel(new JPanel());`

[« Previous](border.html)
•
[Trail](../TOC.html)
•
[Next »](../QandE/questions-ch3.html)

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

**Previous page:** How to Use Borders
  
**Next page:** Questions and Exercises: Using Swing Components




A browser with JavaScript enabled is required for this page to operate properly.