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

How Layout Management Works

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

[« Previous](using.html) • [Trail](../TOC.html) • [Next »](layoutlist.html)

# How Layout Management Works

---

**Note:** This lesson covers writing layout code by hand, which can be challenging. If you are not interested in learning all the details of layout management, you might prefer to use the `GroupLayout` layout manager combined with a builder tool to lay out your GUI. One such builder tool is the
[NetBeans IDE](../learn/index.html). Otherwise, if you want to code by hand and do not want to use `GroupLayout`, then `GridBagLayout` is recommended as the next most flexible and powerful layout manager.

---

Here is an example of a layout management sequence for a container using
[`LayoutManager2`](http://download.oracle.com/javase/7/docs/api/java/awt/LayoutManager2.html).

1. Layout managers basically do two things:
   * Calculate the minimum/preferred/maximum sizes for a container.
   * Lay out the container's children.

   Layout managers do this based on the provided constraints, the container's properties (such as insets) and on the children's minimum/preferred/maximum sizes. If a child is itself a container then its own layout manger is used to get its minimum/preferred/maximum sizes and to lay it out.

   - A container can be *valid* (namely, `isValid()` returns true) or *invalid*. For a container to be valid, all the container's children must be laid out already and must all be valid also. The
     [`Container.validate`](http://download.oracle.com/javase/7/docs/api/java/awt/Container.html#validate())
     method can be used to validate an invalid container. This method triggers the layout for the container and all the child containers down the component hierarchy and marks this container as valid.

     - After a component is created it is in the invalid state by default. The
       [`Window.pack`](http://download.oracle.com/javase/7/docs/api/java/awt/Window.html) method validates the window and lays out the window's component hierarchy for the first time.

The end result is that to determine the best size for the container,
the system determines the sizes of
the containers at the bottom of the containment hierarchy.
These sizes then percolate up the containment hierarchy, eventually determining the container's total size.

If the size of a component changes,
for example following a change of font, the component must be resized and repainted by calling the `revalidate` and `repaint` methods on that component.
Both `revalidate` and `repaint` are
[thread-safe](../concurrency/index.html) — you need not invoke them from the event-dispatching thread.

When you invoke `revalidate` on a component,
a request is passed up the containment hierarchy
until it encounters a container,
such as a scroll pane or top-level container,
that should not be affected by the component's resizing.
(This is determined by calling the container's
`isValidateRoot` method.)
The container is then laid out,
which has the effect of adjusting the revalidated component's
size and the size of all affected components.

[« Previous](using.html)
•
[Trail](../TOC.html)
•
[Next »](layoutlist.html)

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

**Previous page:** Using Layout Managers
  
**Next page:** How to Use Various Layout Managers




A browser with JavaScript enabled is required for this page to operate properly.