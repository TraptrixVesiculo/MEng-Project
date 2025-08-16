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

How to Use Panels

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

[« Previous](menu.html) • [Trail](../TOC.html) • [Next »](passwordfield.html)

# How to Use Panels

The
[`JPanel`](http://download.oracle.com/javase/7/docs/api/javax/swing/JPanel.html) class provides general-purpose containers for lightweight components.
By default, panels do not add colors to anything except their own background;
however, you can easily add borders to them
and otherwise customize their painting.
Details can be found in
[Performing Custom Painting](../painting/index.html).

In many types of look and feel, panels are opaque by default.
Opaque panels work well as content panes
and can help with painting efficiently,
as described in
[Using Top-Level Containers](toplevel.html).
You can change a panel's transparency
by invoking the `setOpaque` method.
A transparent panel draws no background,
so that any components underneath show through.

### An Example

> The following picture
> shows a colored version of the `Converter` application,
> which is discussed in more detail in
> [Using Models](model.html).
>
> ![Colorful Converter](../../figures/uiswing/components/ConverterColored.png)
>
> The `Converter` example uses panels in several ways:
>
> * One `JPanel` instance
>   — colored **red**
>   in the preceding snapshot —
>   serves as a content pane
>   for the application's frame.
>   This content pane uses a top-to-bottom
>   [`BoxLayout`](../layout/box.html) to lay out its contents,
>   and an empty border
>   to put 5 pixels of space around them.
>   See [Using Top-Level Containers](toplevel.html)
>   for information about content panes.* Two instances of a custom `JPanel` subclass
>     named `ConversionPanel` —
>     colored **cyan** —
>     are used to contain components
>     and coordinate communication between components.
>     These `ConversionPanel` panels also have titled borders,
>     which describe their contents and enclose the contents with a line.
>     Each `ConversionPanel` panel uses a left-to-right
>     `BoxLayout`
>     object to lay out its contents.* In each `ConversionPanel`,
>       a `JPanel` instance —
>       colored **magenta** —
>       is used to ensure the proper size and position of the combo box.
>       Each of these `JPanel` instances uses a top-to-bottom
>       `BoxLayout`
>       object
>       (helped by an invisible space-filling component)
>       to lay out the combo box.* In each `ConversionPanel`,
>         an instance of an unnamed `JPanel` subclass —
>         colored **blue** —
>         groups two components (a text field and a slider)
>         and restricts their size.
>         Each of these `JPanel` instances uses a top-to-bottom
>         `BoxLayout`
>         object to lay out its contents.
>
> Here is what the `Converter` application normally looks like.
>
> ![Normal Converter](../../figures/uiswing/components/ConverterMetal.png)
>
> As the `Converter` example demonstrates, panels are useful for
> grouping components,
> simplifying component layout,
> and putting borders around groups of components.
> The rest of this section gives hints on
> grouping and laying out components.
> For information about using borders, see
> [How to Use Borders](../components/border.html).

### Setting the Layout Manager

> Like other containers, a panel uses a layout manager
> to position and size its components.
> By default, a panel's layout manager
> is an instance of
> [`FlowLayout`](../layout/flow.html),
> which places the panel's contents in a row.
> You can easily make a panel use any other layout manager
> by invoking the `setLayout` method
> or by specifying a layout manager when creating the panel.
> The latter approach is preferable for performance reasons,
> since it avoids the unnecessary creation
> of a `FlowLayout` object.
>
> Here is an example of how to set the layout manager
> when creating the panel.
>
> ```
>
> JPanel p = new JPanel(new BorderLayout()); //PREFERRED!
>
> ```
>
> This approach does not work with `BoxLayout`,
> since the `BoxLayout` constructor requires
> a pre-existing container.
> Here is an example that uses `BoxLayout`.
>
> ```
>
> JPanel p = new JPanel();
> p.setLayout(new BoxLayout(p, BoxLayout.PAGE_AXIS));
>
> ```

### Adding Components

> When you add components to a panel,
> you use the `add` method.
> Exactly which arguments you specify to the `add` method
> depend on which layout manager the panel uses.
> When the layout manager is `FlowLayout`, `BoxLayout`,
> `GridLayout`,
> or `SpringLayout`,
> you will typically use the one-argument `add` method, like this:
>
> ```
>
> aFlowPanel.add(aComponent);
> aFlowPanel.add(anotherComponent);
>
> ```
>
> When the layout manager is `BorderLayout`,
> you need to provide an argument
> specifying the added component's position within the panel.
> For example:
>
> ```
>
> aBorderPanel.add(aComponent, BorderLayout.CENTER);
> aBorderPanel.add(anotherComponent, BorderLayout.PAGE_END);
>
> ```
>
> With `GridBagLayout`
> you can use either `add` method,
> but you must somehow specify
> [grid bag constraints](../layout/gridbag.html#gridbagConstraints) for each component.
>
> For information about choosing and using
> the standard layout managers, see
> [Using Layout Managers](../layout/using.html).

### The Panel API

> The API in the `JPanel` class itself is minimal.
> The methods you are most likely to invoke on
> a `JPanel` object are those it inherits from its superclasses —
> [`JComponent`](http://download.oracle.com/javase/7/docs/api/javax/swing/JComponent.html),
> [`Container`](http://download.oracle.com/javase/7/docs/api/java/awt/Container.html), and
> [`Component`](http://download.oracle.com/javase/7/docs/api/java/awt/Component.html).
> The following tables list the API
> you are most likely to use,
> with the exception of methods
> related to
> [borders](../components/border.html) and
> [layout hints](jcomponent.html#layoutapi).
> For more information about the API that all `JComponent` objects
> can use, see
> [The JComponent Class](jcomponent.html).
>
> * [Creating a `JPanel`](#creating)* [Managing a Container's Components](#contents)* [Setting or Getting the Layout Manager](#layoutapi)
>
> **Creating a `JPanel`**
>
> | Constructor | Purpose |
> | [JPanel()](http://download.oracle.com/javase/7/docs/api/javax/swing/JPanel.html#JPanel())   [JPanel(LayoutManager)](http://download.oracle.com/javase/7/docs/api/javax/swing/JPanel.html#JPanel(java.awt.LayoutManager)) | Creates a panel. The `LayoutManager` parameter provides a layout manager for the new panel. By default, a panel uses a `FlowLayout` to lay out its components. |
>
> **Managing a Container's Components**
>
> | Method | Purpose |
> | [void add(Component)](http://download.oracle.com/javase/7/docs/api/java/awt/Container.html#add(java.awt.Component))   [void add(Component, int)](http://download.oracle.com/javase/7/docs/api/java/awt/Container.html#add(java.awt.Component, int))   [void add(Component, Object)](http://download.oracle.com/javase/7/docs/api/java/awt/Container.html#add(java.awt.Component, java.lang.Object))   [void add(Component, Object, int)](http://download.oracle.com/javase/7/docs/api/java/awt/Container.html#add(java.awt.Component, java.lang.Object, int))   [void add(String, Component)](http://download.oracle.com/javase/7/docs/api/java/awt/Container.html#add(java.lang.String, java.awt.Component)) | Adds the specified component to the panel. When present, the `int` parameter is the index of the component within the container. By default, the first component added is at index 0, the second is at index 1, and so on. The `Object` parameter is layout manager dependent and typically provides information to the layout manager regarding positioning and other layout constraints for the added component. The `String` parameter is similar to the `Object` parameter. |
> | [int getComponentCount()](http://download.oracle.com/javase/7/docs/api/java/awt/Container.html#getComponentCount()) | Gets the number of components in this panel. |
> | [Component getComponent(int)](http://download.oracle.com/javase/7/docs/api/java/awt/Container.html#getComponent(int))   [Component getComponentAt(int, int)](http://download.oracle.com/javase/7/docs/api/java/awt/Container.html#getComponentAt(int, int))   [Component getComponentAt(Point)](http://download.oracle.com/javase/7/docs/api/java/awt/Container.html#getComponentAt(java.awt.Point))   [Component[] getComponents()](http://download.oracle.com/javase/7/docs/api/java/awt/Container.html#getComponents()) | Gets the specified component or components. You can get a component based on its index or *x, y* position. |
> | [void remove(Component)](http://download.oracle.com/javase/7/docs/api/java/awt/Container.html#remove(java.awt.Component))   [void remove(int)](http://download.oracle.com/javase/7/docs/api/java/awt/Container.html#remove(int))   [void removeAll()](http://download.oracle.com/javase/7/docs/api/java/awt/Container.html#removeAll()) | Removes the specified component(s). |
>
> **Setting or Getting the Layout Manager**
>
> | Method | Purpose |
> | [void setLayout(LayoutManager)](http://download.oracle.com/javase/7/docs/api/java/awt/Container.html#setLayout(java.awt.LayoutManager))   [LayoutManager getLayout()](http://download.oracle.com/javase/7/docs/api/java/awt/Container.html#getLayout()) | Sets or gets the layout manager for this panel. The layout manager is responsible for positioning the panel's components within the panel's bounds according to some philosophy. |

### Examples That Use Panels

> Many examples contained in this lesson use `JPanel` objects.
> The following table lists a few.
>
> | Example | Where Described | Notes |
> | --- | --- | --- |
> | [`Converter`](../examples/components/index.html#Converter) | This section | Uses five panels, four of which use `BoxLayout` and one of which uses `GridLayout`. The panels use borders and, as necessary, size and alignment hints to affect layout. |
> | [`ListDemo`](../examples/components/index.html#ListDemo) | [How to Use Lists](list.html) | Uses a panel, with its default `FlowLayout` manager, to center three components in a row. |
> | [`ToolBarDemo`](../examples/components/index.html#ToolBarDemo) | [How to Use Tool Bars](toolbar.html) | Uses a panel as a content pane. The panel contains three components, laid out by `BorderLayout`. |
> | [`BorderDemo`](../examples/components/index.html#BorderDemo) | [How to Use Borders](border.html) | Contains many panels that have various kinds of borders. Several panels use `BoxLayout`. |
> | [`BoxLayoutDemo`](../examples/layout/index.html#BoxLayoutDemo) | [How to Use BoxLayout](../layout/box.html) | Illustrates the use of a panel with Swing's `BoxLayout` manager. |

[« Previous](menu.html)
•
[Trail](../TOC.html)
•
[Next »](passwordfield.html)

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

**Previous page:** How to Use Menus
  
**Next page:** How to Use Password Fields




A browser with JavaScript enabled is required for this page to operate properly.