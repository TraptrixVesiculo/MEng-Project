[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Creating a GUI With JFC/Swing
  
**Lesson:** Laying Out Components Within a Container

[Laying Out Components Within a Container](index.html)

A Visual Guide to Layout Managers

[Using Layout Managers](using.html)

[How Layout Management Works](howLayoutWorks.html)

[How to Use Various Layout Managers](layoutlist.html)

[How to Use BorderLayout](border.html)

[How to Use BoxLayout](box.html)

[How to Use CardLayout](card.html)

[How to Use FlowLayout](flow.html)

[How to Use GridBagLayout](gridbag.html)

[How to Use GridLayout](grid.html)

[How to Use GroupLayout](group.html)

[A GroupLayout Example](groupExample.html)

[How to Use SpringLayout](spring.html)

[Creating a Custom Layout Manager](custom.html)

[Doing Without a Layout Manager (Absolute Positioning)](none.html)

[Solving Common Layout Problems](problems.html)

[Home Page](../../index.html)
>
[Creating a GUI With JFC/Swing](../index.html)
>
[Laying Out Components Within a Container](index.html)

[« Previous](index.html) • [Trail](../TOC.html) • [Next »](using.html)

# A Visual Guide to Layout Managers

Several AWT and Swing classes provide layout managers for general use:

* [`BorderLayout`](#border)* [`BoxLayout`](#box)* [`CardLayout`](#card)* [`FlowLayout`](#flow)* [`GridBagLayout`](#gridbag)* [`GridLayout`](#grid)* [`GroupLayout`](#group)* [`SpringLayout`](#spring)

This section shows example GUIs
that use these layout managers,
and tells you where to find the how-to page for each layout manager.
You can find links for running the examples
in the how-to pages and in the
[example index](../examples/layout/index.html).

---

**Note:** This lesson covers writing layout code by hand, which can be challenging. If you are not interested in learning all the details of layout management, you might prefer to use the `GroupLayout` layout manager combined with a builder tool to lay out your GUI. One such builder tool is the
[NetBeans IDE](../learn/index.html). Otherwise, if you want to code by hand and do not want to use `GroupLayout`, then `GridBagLayout` is recommended as the next most flexible and powerful layout manager.

---

### BorderLayout
> ![A picture of a GUI that uses BorderLayout](../../figures/uiswing/layout/BorderLayoutDemo.png)
>
> Every content pane
> is initialized to use a `BorderLayout`.
> (As
> [Using Top-Level Containers](../components/toplevel.html) explains,
> the content pane is the main container in all frames, applets, and dialogs.)
> A `BorderLayout`
> places components in up to five areas:
> top, bottom, left, right, and center.
> All extra space is placed in the center area. Tool bars that are created using
> [JToolBar](../components/toolbar.html)
> must be created within a `BorderLayout` container, if you want to be able to drag and drop the bars away from their starting positions.
> For further details, see
> [How to Use BorderLayout](border.html).

### BoxLayout

> ![A picture of a GUI that uses BoxLayout](../../figures/uiswing/layout/BoxLayoutDemo.png)
>
> The `BoxLayout` class puts components
> in a single row or column.
> It respects the components' requested
> maximum sizes
> and also lets you align components.
> For further details, see
> [How to Use BoxLayout](box.html).

### CardLayout

> ![A picture of a GUI that uses CardLayout](../../figures/uiswing/layout/CardLayoutDemo.png)
> ![Another picture of the same layout](../../figures/uiswing/layout/CardLayoutDemo-2.png)
>
> The `CardLayout` class lets you implement an area
> that contains different components at different times.
> A `CardLayout` is often controlled by a combo box,
> with the state of the combo box determining
> which panel (group of components)
> the `CardLayout` displays.
> An alternative to using `CardLayout` is using a
> [tabbed pane](../components/tabbedpane.html), which provides similar functionality
> but with a pre-defined GUI.
> For further details, see
> [How to Use CardLayout](card.html).

### FlowLayout

> ![A picture of a GUI that uses FlowLayout](../../figures/uiswing/layout/FlowLayoutDemo.png)
>
> `FlowLayout` is the default layout manager for
> every `JPanel`.
> It simply lays out components
> in a single row,
> starting a new row if its container is not sufficiently wide.
> Both panels in CardLayoutDemo,
> shown [previously](#card),
> use `FlowLayout`.
> For further details, see
> [How to Use FlowLayout](flow.html).

### GridBagLayout

> ![A picture of a GUI that uses GridBagLayout](../../figures/uiswing/layout/GridBagLayoutDemo.png)
>
> `GridBagLayout` is a sophisticated,
> flexible layout manager.
> It aligns components by placing them within a grid of cells,
> allowing components to span more than one cell.
> The rows in the grid can have different heights,
> and grid columns can have different widths.
> For further details, see
> [How to Use GridBagLayout](gridbag.html).

### GridLayout

> ![A picture of a GUI that uses GridLayout](../../figures/uiswing/layout/GridLayoutDemo.png)
>
> `GridLayout` simply makes a bunch of components equal in size
> and displays them in the requested number of rows and columns.
> For further details, see
> [How to Use GridLayout](grid.html).

### GroupLayout

> ![A picture of a GUI that uses GroupLayout](../../figures/uiswing/layout/find.png)
>
> `GroupLayout` is a layout manager that was developed for use by GUI builder tools, but it can also be used manually. `GroupLayout` works with the horizontal and vertical layouts separately. The layout is defined for each dimension independently. Consequently, however, each component needs to be defined twice in the layout. The Find window shown above is an example of a `GroupLayout`.
> For further details, see
> [How to Use GroupLayout](group.html).

### SpringLayout

> ![A picture of a GUI that uses SpringLayout](../../figures/uiswing/layout/SpringBox.png)
>
> ![Another GUI that uses SpringLayout](../../figures/uiswing/layout/SpringForm.png)
>
> `SpringLayout` is a flexible layout manager
> designed for use by GUI builders.
> It lets you specify precise relationships
> between the edges of components under its control.
> For example, you might define that
> the left edge of one component is a certain distance
> (which can be dynamically calculated)
> from the right edge of a second component. `SpringLayout` lays out the children of its associated container according to a set of constraints, as shall be seen in
> [How to Use SpringLayout](spring.html).

[« Previous](index.html)
•
[Trail](../TOC.html)
•
[Next »](using.html)

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

**Previous page:** Laying Out Components Within a Container
  
**Next page:** Using Layout Managers




A browser with JavaScript enabled is required for this page to operate properly.