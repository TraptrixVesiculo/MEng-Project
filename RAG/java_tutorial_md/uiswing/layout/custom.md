[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Creating a GUI With JFC/Swing
  
**Lesson:** Laying Out Components Within a Container

[Laying Out Components Within a Container](index.html)

[A Visual Guide to Layout Managers](visual.html)

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

Creating a Custom Layout Manager

[Doing Without a Layout Manager (Absolute Positioning)](none.html)

[Solving Common Layout Problems](problems.html)

[Home Page](../../index.html)
>
[Creating a GUI With JFC/Swing](../index.html)
>
[Laying Out Components Within a Container](index.html)

[« Previous](spring.html) • [Trail](../TOC.html) • [Next »](none.html)

# Creating a Custom Layout Manager

Before you start creating a custom layout manager,
make sure that no existing layout manager meets your requirements.
In particular, layout managers such as
[`GridBagLayout`](gridbag.html),
[`SpringLayout`](spring.html), and
[`BoxLayout`](box.html)
are flexible enough to work in many cases.
You can also find layout managers from other sources,
such as from the Internet.
Finally, you can simplify layout
by grouping components into containers
such as
[panels](../components/panel.html).

---

**Note:** This lesson covers writing layout code by hand, which can be challenging. If you are not interested in learning all the details of layout management, you might prefer to use the `GroupLayout` layout manager combined with a builder tool to lay out your GUI. One such builder tool is the
[NetBeans IDE](../learn/index.html). Otherwise, if you want to code by hand and do not want to use `GroupLayout`, then `GridBagLayout` is recommended as the next most flexible and powerful layout manager.

---

To create a custom layout manager,
you must create a class that implements the
[`LayoutManager`](http://download.oracle.com/javase/7/docs/api/java/awt/LayoutManager.html) interface.
You can either implement it directly,
or implement its subinterface,
[`LayoutManager2`](http://download.oracle.com/javase/7/docs/api/java/awt/LayoutManager2.html).

Every layout manager must implement at least
the following five methods,
which are required by the `LayoutManager` interface:

**`void addLayoutComponent(String, Component)`**: Called by the `Container` class's `add` methods. Layout managers that do not associate strings with their components generally do nothing in this method. **`void removeLayoutComponent(Component)`**: Called by the `Container` methods `remove` and `removeAll`. Layout managers override this method to clear an internal state they may have associated with the `Component`. **`Dimension preferredLayoutSize(Container)`**: Called by the `Container` class's `getPreferredSize` method, which is itself called under a variety of circumstances. This method should calculate and return the ideal size of the container, assuming that the components it contains will be at or above their preferred sizes. This method must take into account the container's internal borders, which are returned by the [`getInsets`](http://download.oracle.com/javase/7/docs/api/java/awt/Container.html#getInsets()) method. **`Dimension minimumLayoutSize(Container)`**: Called by the `Container` `getMinimumSize` method, which is itself called under a variety of circumstances. This method should calculate and return the minimum size of the container, assuming that the components it contains will be at or above their minimum sizes. This method must take into account the container's internal borders, which are returned by the `getInsets` method. **`void layoutContainer(Container)`**: Called to position and size each of the components in the container. A layout manager's `layoutContainer` method does not actually draw components. It simply invokes one or more of each component's `setSize`, `setLocation`, and `setBounds` methods to set the component's size and position. This method must take into account the container's internal borders, which are returned by the `getInsets` method. If appropriate, it should also take the container's orientation (returned by the [`getComponentOrientation`](http://download.oracle.com/javase/7/docs/api/java/awt/Component.html#getComponentOrientation()) method) into account. You cannot assume that the `preferredLayoutSize` or `minimumLayoutSize` methods will be called before `layoutContainer` is called.

Besides implementing the preceding five methods,
layout managers generally implement at least one public constructor
and the
`toString`
method.

If you wish to support component
constraints, maximum sizes, or alignment,
then your layout manager should implement the
`LayoutManager2` interface. In fact, for these reasons among many others, nearly all modern layout managers will need to implement `LayoutManager2`.
That interface adds five methods to those
required by `LayoutManager`:

* `addLayoutComponent(Component, Object)`* `getLayoutAlignmentX(Container)`* `getLayoutAlignmentY(Container)`* `invalidateLayout(Container)`* `maximumLayoutSize(Container)`

Of these methods, the most important are `addLayoutComponent(Component, Object)` and `invalidateLayout(Container)`. The `addLayoutComponent`
method is used to add components to the layout, using the specified constraint object. The `invalidateLayout` method is used to invalidate the layout, so that if the
layout manager has cached information, this should be discarded. For more information about `LayoutManager2`,
see the
[`LayoutManager2`](http://download.oracle.com/javase/7/docs/api/java/awt/LayoutManager2.html)  API documentation.

Finally, whenever you create custom layout managers, you should be careful of keeping references to `Component` instances that are no longer children of the `Container`. Namely, layout managers should override `removeLayoutComponent` to clear any cached state related to the `Component`.

### Example of a Custom Layout

The example `CustomLayoutDemo`
uses a custom layout manager called `DiagonalLayout`.
You can find the layout manager's source code in
[`DiagonalLayout.java`](../examples/layout/CustomLayoutDemoProject/src/layout/DiagonalLayout.java).
`DialogLayout` lays out components diagonally,
from left to right,
with one component per row.
Here is a picture of CustomLayoutDemo using
`DialogLayout` to lay out five buttons.

![A snapshot of CustomLayoutDemo](../../figures/uiswing/layout/CustomLayoutDemo.png)

Click the Launch button to run `CustomLayoutDemo` using
[Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp) ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
Alternatively, to compile and run the example yourself, consult the
[example index](../examples/layout/index.html#CustomLayoutDemo).
 [![Launches the CustomLayoutDemo example](../../images/jws-launch-button.png )](http://download.oracle.com/javase/tutorialJWS/uiswing/layout/ex6/CustomLayoutDemo.jnlp)

[« Previous](spring.html)
•
[Trail](../TOC.html)
•
[Next »](none.html)

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

**Previous page:** How to Use SpringLayout
  
**Next page:** Doing Without a Layout Manager (Absolute Positioning)




A browser with JavaScript enabled is required for this page to operate properly.