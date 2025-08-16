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

[Creating a Custom Layout Manager](custom.html)

[Doing Without a Layout Manager (Absolute Positioning)](none.html)

Solving Common Layout Problems

[Home Page](../../index.html)
>
[Creating a GUI With JFC/Swing](../index.html)
>
[Laying Out Components Within a Container](index.html)

[« Previous](none.html) • [Trail](../TOC.html) • [Next »](../QandE/questions-ch4.html)

# Solving Common Layout Problems

---

**Note:** This lesson covers writing layout code by hand, which can be challenging. If you are not interested in learning all the details of layout management, you might prefer to use the `GroupLayout` layout manager combined with a builder tool to lay out your GUI. One such builder tool is the
[NetBeans IDE](../learn/index.html). Otherwise, if you want to code by hand and do not want to use `GroupLayout`, then `GridBagLayout` is recommended as the next most flexible and powerful layout manager.

---

**Problem:**
How do I specify a component's exact size?

* A handful of the more modern layout managers provide ways to override the size set by the component. Check whether the layout manager you are using allows you to specify component sizes.

  * Make sure that you really need to set the component's exact size.
    Each Swing component has a different preferred size,
    depending on
    the font it uses
    and the look and feel.
    For this reason, it often does not make sense
    to specify a Swing component's exact size.

    * If the component is not controlled by a layout manager,
      you can set its size by
      invoking the `setSize` or `setBounds`
      method on it.
      Otherwise, you need to provide size hints
      and then make sure you are using a layout manager
      that respects the size hints.

      * If you extend a Swing component class,
        you can give size hints
        by overriding the component's
        `getMinimumSize`,
        `getPreferredSize`, and
        `getMaximumSize` methods.
        What is nice about this approach
        is that each `getXxxxSize` method
        can get the component's default size hints
        by invoking `super.getXxxxSize()`.
        Then it can adjust the size, if necessary,
        before returning it. This is particularly handy for text components, where you might want to fix the width, but have the height determined from the content. However, sometimes problems can be encountered with `GridBagLayout` and text fields, wherein if the size of the container is smaller than the preferred size, the minimum size gets used, which can cause text fields to shrink quite substantially.

        * Another way to give size hints
          is to invoke the component's `setMinimumSize`,
          `setPreferredSize`, and
          `setMaximumSize` methods.

          * If you specify new size hints for a component that is already visible,
            you then need to invoke the `revalidate` method on it,
            to make sure that its containment hierarchy is laid out again.
            Then invoke the `repaint` method.

---

**Note:** 
No matter how you specify your component's size,
be sure that your component's container uses
a layout manager that respects the requested size of the component.
The `FlowLayout` and `GridBagLayout` managers
use the component's preferred size
(the latter depending on the constraints
that you set),
but `BorderLayout` and `GridLayout` usually do not.
The `BoxLayout` manager generally
uses a component's preferred size
(although components can be larger),
and is one of the few layout managers that respects
the component's maximum size.

---

**Problem:**
My component does not appear after I have added it to the container.

* You need to invoke `revalidate` and `repaint` after adding a component before it will show up in your container.

**Problem:**
My custom component is being sized too small.

* Does the component implement the
  `getPreferredSize` and `getMinimumSize` methods?
  If so, do they return the right values?* Are you using a layout manager
    that can use as much space as is available?
    See [Tips on Choosing a Layout Manager](using.html#choosing)
    for some tips on choosing a layout manager
    and specifying that it use the maximum available space
    for a particular component.

If you do not see your problem in this list, see
[Solving Common Component Problems](../components/problems.html).

[« Previous](none.html)
•
[Trail](../TOC.html)
•
[Next »](../QandE/questions-ch4.html)

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

**Previous page:** Doing Without a Layout Manager (Absolute Positioning)
  
**Next page:** Questions and Exercises: Laying Out Components within a Container




A browser with JavaScript enabled is required for this page to operate properly.