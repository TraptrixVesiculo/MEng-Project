[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

Laying Out Components Within a Container

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

[Creating a Custom Layout Manager](custom.html)

[Doing Without a Layout Manager (Absolute Positioning)](none.html)

[Solving Common Layout Problems](problems.html)

**Trail:** Creating a GUI With JFC/Swing

[Home Page](../../index.html)
>
[Creating a GUI With JFC/Swing](../index.html)

[« Previous](../misc/index.html) • [Trail](../TOC.html) • [Next »](visual.html)

# Lesson: Laying Out Components Within a Container

[Examples Index](../examples/layout/index.html)

This lesson tells you how to use the layout managers
provided by the Java platform. It also tells you how to use absolute positioning (no layout manager)
and gives an example of writing a custom layout manager.
For each layout manager (or lack thereof),
this
lesson
points to an example
that you can run using JavaTM Web Start.
By resizing an example's window,
you can see how size changes affect the layout.

---

**Note:** This lesson covers writing layout code by hand, which can be challenging. If you are not interested in learning all the details of layout management, you might prefer to use the `GroupLayout` layout manager combined with a builder tool to lay out your GUI. One such builder tool is the
[NetBeans IDE](../learn/index.html). Otherwise, if you want to code by hand and do not want to use `GroupLayout`, then `GridBagLayout` is recommended as the next most flexible and powerful layout manager.

---

### [A Visual Guide to Layout Managers](visual.html)

> This section shows examples of the standard layout managers
> and points to the how-to section for each one.

### [Using Layout Managers](using.html)

> This section gives general rules
> on using the standard layout managers.
> It includes how to set the layout manager,
> add components to a container,
> provide size and alignment hints,
> put space between components,
> and set the orientation of the container's layout
> so that it is appropriate for the locale
> in which the program is running.
> It also has some tips for choosing the right layout manager.

### [How Layout Management Works](howLayoutWorks.html)

> This section goes through a typical layout sequence
> and then describes what happens when a component's size changes.

### [How to Use ...](layoutlist.html)

> This series of sections tells you how to use
> each of the general-purpose layout managers
> that the Java platform provides.

### [Creating a Custom Layout Manager](custom.html)

> Instead of using one of the Java platform's layout managers,
> you can write your own.
> Layout managers must implement the `LayoutManager` interface,
> which specifies the five methods every layout manager must define.
> Optionally, layout managers can implement `LayoutManager2`,
> which is a subinterface of `LayoutManager`.

### [Doing Without a Layout Manager (Absolute Positioning)](none.html)

> If necessary, you can position components
> without using a layout manager.
> Generally, this solution is used to specify absolute sizes and positions
> for components.

### [Solving Common Layout Problems](problems.html)

> Some of the most common layout problems
> involve components that are displayed too small —
> or not at all.
> This section
> tells you how to fix these and
> other common layout problems.

### [Questions and Exercises](../QandE/questions-ch4.html)

> Try these questions and exercises to test what you have learned in this lesson.

[« Previous](../misc/index.html)
•
[Trail](../TOC.html)
•
[Next »](visual.html)

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
  
**Next page:** A Visual Guide to Layout Managers




A browser with JavaScript enabled is required for this page to operate properly.