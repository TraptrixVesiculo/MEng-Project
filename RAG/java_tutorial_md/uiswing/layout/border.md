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

How to Use BorderLayout

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

[« Previous](layoutlist.html) • [Trail](../TOC.html) • [Next »](box.html)

# How to Use BorderLayout

---

**Note:** This lesson covers writing layout code by hand, which can be challenging. If you are not interested in learning all the details of layout management, you might prefer to use the `GroupLayout` layout manager combined with a builder tool to lay out your GUI. One such builder tool is the
[NetBeans IDE](../learn/index.html). Otherwise, if you want to code by hand and do not want to use `GroupLayout`, then `GridBagLayout` is recommended as the next most flexible and powerful layout manager.

---

The following figure represents a snapshot of an application that uses the
[`BorderLayout`](http://download.oracle.com/javase/7/docs/api/java/awt/BorderLayout.html) class.

![A snapshot of BorderLayoutDemo](../../figures/uiswing/layout/BorderLayoutDemo.png)

Click the Launch button
to run BorderLayoutDemo using
[Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp)
([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
Alternatively, to compile and run the example yourself,
consult the
[example index](../examples/layout/index.html#BorderLayoutDemo).

[![Launches the BorderLayoutDemo application](../../images/jws-launch-button.png)](http://download.oracle.com/javase/tutorialJWS/uiswing/layout/ex6/BorderLayoutDemo.jnlp)

The complete code of this demo is in the
[`BorderLayoutDemo.java`](../examples/layout/BorderLayoutDemoProject/src/layout/BorderLayoutDemo.java) file.

As the preceding picture shows,
a `BorderLayout` object has five areas.
These areas are specified by the `BorderLayout` constants:

* `PAGE_START`
* `PAGE_END`
* `LINE_START`
* `LINE_END`
* `CENTER`

---

**Version note:** Before JDK release 1.4, the preferred names for the various areas were different,
ranging from points of the compass
(for example, `BorderLayout.NORTH`
for the top area)
to wordier versions of the constants we use in our examples.
The constants our examples use are preferred
because they are standard and enable programs to adjust
to languages that have different orientations.

---

If the window is enlarged,
the center area
gets as much of the available space as possible.
The other areas expand only as much as necessary
to fill all available space.
Often a container uses only one or two of the
areas of the `BorderLayout` object —
just the center,
or the center and the bottom.

The following code adds components to a frame's content pane.
Because content panes use the `BorderLayout` class by default,
the code does not need to set the layout manager.
The complete program is in the
[`BorderLayoutDemo.java`](../examples/layout/BorderLayoutDemoProject/src/layout/BorderLayoutDemo.java) file.

```

...//Container pane = aFrame.getContentPane()...
JButton button = new JButton("Button 1 (PAGE_START)");
pane.add(button, BorderLayout.PAGE_START);

//Make the center component big, since that's the
//typical usage of BorderLayout.
button = new JButton("Button 2 (CENTER)");
button.setPreferredSize(new Dimension(200, 100));
pane.add(button, BorderLayout.CENTER);

button = new JButton("Button 3 (LINE_START)");
pane.add(button, BorderLayout.LINE_START);

button = new JButton("Long-Named Button 4 (PAGE_END)");
pane.add(button, BorderLayout.PAGE_END);

button = new JButton("5 (LINE_END)");
pane.add(button, BorderLayout.LINE_END);

```

Specify the component's location
(for example, `BorderLayout.LINE_END`)
as one of the arguments to the `add` method.
If this component is missing
from a container controlled by a `BorderLayout` object,
make sure that the component's location was specified
and no another component was placed in the same location.

All tutorial examples that use the `BorderLayout` class
specify the component as the first argument to the
`add` method.
For example:

```

add(component, BorderLayout.CENTER)  //preferred

```

However, the code in other programs
specifies the component as the second argument.
For example, here are alternate ways
of writing the preceding code:

```

add(BorderLayout.CENTER, component)  //valid but old fashioned
    or
add("Center", component)             //valid but error prone

```

### The BorderLayout API

> The following table lists constructors and methods to specify gaps (in pixels).
>
> Specifying gaps
>
> | Constructor or Method | Purpose |
> | [`BorderLayout(int horizontalGap, int verticalGap)`](http://download.oracle.com/javase/7/docs/api/java/awt/BorderLayout.html#BorderLayout(int,%20int)) | Defines a border layout with specified gaps between components. |
> | [`setHgap(int)`](http://download.oracle.com/javase/7/docs/api/java/awt/BorderLayout.html#setHgap(int)) | Sets the horizontal gap between components. |
> | [`setVgap(int)`](http://download.oracle.com/javase/7/docs/api/java/awt/BorderLayout.html#setVgap(int)) | Sets the vertical gap between components. |

### Examples that Use BorderLayout

> The following table lists code examples that use the `BorderLayout` class and
> provides links to related sections.
>
> | Example | Where Described | Notes |
> | --- | --- | --- |
> | [`BorderLayoutDemo`](../examples/layout/index.html#BorderLayoutDemo) | This page | Puts a component in each of the five possible locations. |
> | [`TabbedPaneDemo`](../examples/components/index.html#TabbedPaneDemo) | [How to Use Tabbed Panes](../components/tabbedpane.html) | One of many examples that puts a single component in the center of a content pane, so that the component is as large as possible. |
> | [`CheckBoxDemo`](../examples/components/index.html#CheckBoxDemo) | [How to Use Check Boxes](../components/button.html#checkbox) | Creates a `JPanel` object that uses the `BorderLayout` class. Puts components into the left (actually, `LINE_START`) and center locations. |

[« Previous](layoutlist.html)
•
[Trail](../TOC.html)
•
[Next »](box.html)

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

**Previous page:** How to Use Various Layout Managers
  
**Next page:** How to Use BoxLayout




A browser with JavaScript enabled is required for this page to operate properly.