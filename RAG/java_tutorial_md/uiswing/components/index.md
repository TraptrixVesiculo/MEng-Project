[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

Using Swing Components

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

[Solving Common Component Problems](problems.html)

**Trail:** Creating a GUI With JFC/Swing

[Home Page](../../index.html)
>
[Creating a GUI With JFC/Swing](../index.html)

[« Previous](../learn/index.html) • [Trail](../TOC.html) • [Next »](toplevel.html)

# Lesson: Using Swing Components

[Examples Index](../examples/components/index.html)

This lesson gives you the background information
you need to use the Swing components,
and then describes every Swing component.
It assumes that you have successfully
compiled and run a program that uses Swing components,
and that you are familiar with basic Swing concepts.
These prerequisites are covered in
[Getting Started with Swing](../start/index.html) and
[Learning Swing with the NetBeans IDE](../learn/index.html).

### [A Visual Index to the Swing Components (Java Look and Feel)](../../ui/features/components.html) [A Visual Index to the Swing Components (Windows Look and Feel)](../../ui/features/compWin.html)

> Before you get started, you may want to check out these pages
> (from the
> [Graphical User Interfaces](../../ui/index.html) lesson in the Core trail)
> which have pictures of all the standard Swing components, from
> top-level containers to scroll panes to buttons. To find the section
> that discusses a particular component, just click the component's picture.

### [Using Top-Level Containers](toplevel.html)

> Discusses how to use the features shared by the
> `JFrame`,
> `JDialog`, and
> `JApplet` classes —
> content panes, menu bars, and root panes.
> It also discusses the
> *containment hierarchy*,
> which refers to the tree of components
> contained by a top-level container.

### [The JComponent Class](jcomponent.html)

> Tells you about the features `JComponent`
> provides to its subclasses —
> which include almost all Swing components —
> and gives tips on how to take advantage of these features.
> This section ends with API tables
> describing the commonly used API
> defined by
> `JComponent` and its superclasses,
> `Container` and
> `Component`.

### [Using Text Components](text.html)

> Describes the features and API shared by
> all components that descend from
> `JTextComponent`.
> You probably do not need to read this section
> if you are just using text fields (formatted or not)
> or text areas.

### [How to...](componentlist.html)

> Sections on how to use each Swing component,
> in alphabetical order.
> We do not expect you to read these sections in order.
> Instead,
> we recommend reading the relevant "How to" sections
> once you are ready to start using Swing components
> in your own programs.
> For example,
> if your program needs a frame, a label, a button, and a color chooser,
> you should read
> [How to Make Frames](frame.html),
> [How to Use Labels](label.html),
> [How to Use Buttons](button.html), and
> [How to Use Color Choosers](colorchooser.html).

### [Using HTML in Swing Components](html.html)

> Describes how to vary the font, color, or other formatting of text
> displayed by Swing components
> by using HTML tags.

### [Using Models](model.html)

> Tells you about the Swing model architecture.
> This variation on Model-View-Controller (MVC)
> means that you can, if you wish,
> specify how the data and state of a Swing component
> are stored and retrieved.
> The benefits are the ability to share data and state between components,
> and to greatly improve the performance of components
> such as tables
> that display large amounts of data.

### [Using Borders](border.html)

> Borders are very handy for drawing lines, titles, and empty space
> around the edges of components. (You might have noticed that the
> examples in this trail use a lot of borders.) This section tells you
> how to add a border to any `JComponent`.

### [Using Icons](icon.html)

> Many Swing components can display icons. Usually, icons are
> implemented as instances of the `ImageIcon` class.

### [Solving Common Component Problems](problems.html)

> This section discusses solutions to common component-related problems.

### [Questions and Exercises](../QandE/questions-ch3.html)

> Try these questions and exercises to test what you have learned in
> this lesson.

[« Previous](../learn/index.html)
•
[Trail](../TOC.html)
•
[Next »](toplevel.html)

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

**Previous page:** Previous Lesson
  
**Next page:** Using Top-Level Containers




A browser with JavaScript enabled is required for this page to operate properly.