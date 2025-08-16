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

How to Use FlowLayout

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

[« Previous](card.html) • [Trail](../TOC.html) • [Next »](gridbag.html)

# How to Use FlowLayout

---

**Note:** This lesson covers writing layout code by hand, which can be challenging. If you are not interested in learning all the details of layout management, you might prefer to use the `GroupLayout` layout manager combined with a builder tool to lay out your GUI. One such builder tool is the
[NetBeans IDE](../learn/index.html). Otherwise, if you want to code by hand and do not want to use `GroupLayout`, then `GridBagLayout` is recommended as the next most flexible and powerful layout manager.

---

The
[`FlowLayout`](http://download.oracle.com/javase/7/docs/api/java/awt/FlowLayout.html) class
provides a very simple layout manager
that is used, by default, by the `JPanel` objects.
The following figure represents a snapshot of an application that uses the flow layout:

![A snapshot of FlowLayoutDemo](../../figures/uiswing/layout/FlowLayoutDemo1.png)

Click the Launch button
to run FlowLayoutDemo using
[Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp)
([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
Alternatively, to compile and run the example yourself,
consult the
[example index](../examples/layout/index.html#FlowLayoutDemo).

[![Launches the FlowLayoutDemo application](../../images/jws-launch-button.png)](http://download.oracle.com/javase/tutorialJWS/uiswing/layout/ex6/FlowLayoutDemo.jnlp)

The complete code of this demo is in the
[`FlowLayoutDemo.java`](../examples/layout/FlowLayoutDemoProject/src/layout/FlowLayoutDemo.java) file.

The `FlowLayout` class puts components in a row,
sized at their preferred size.
If the horizontal space in the container
is too small to put all the components in one row,
the `FlowLayout` class uses multiple rows.
If the container is wider than necessary
for a row of components,
the row is, by default, centered horizontally within the container.
To specify that the row is to aligned either to the left or right, use
a `FlowLayout` constructor that takes an alignment argument.
Another constructor of the `FlowLayout` class specifies
how much vertical or horizontal padding
is put around the components.

The code snippet below creates a `FlowLayout` object and the components it manages.

```

FlowLayout experimentLayout = new FlowLayout();

...

	compsToExperiment.setLayout(experimentLayout);

	compsToExperiment.add(new JButton("Button 1"));
	compsToExperiment.add(new JButton("Button 2"));
	compsToExperiment.add(new JButton("Button 3"));
	compsToExperiment.add(new JButton("Long-Named Button 4"));
	compsToExperiment.add(new JButton("5"));

```

Select either the Left to Right or Right to Left option and click the Apply orientation button to set up the component's orientation.
The following code snippet applies the Left to Right components orientation to the `experimentLayout`.

```

	compsToExperiment.setComponentOrientation(
		ComponentOrientation.LEFT_TO_RIGHT);

```

### The FlowLayout API

> The following table lists constructors of the `FlowLayout` class.
>
> | Constructor | Purpose |
> | --- | --- |
> | [`FlowLayout()`](http://download.oracle.com/javase/7/docs/api/java/awt/FlowLayout.html#FlowLayout()) | Constructs a new `FlowLayout` object with a centered alignment and horizontal and vertical gaps with the default size of 5 pixels. |
> | [`FlowLayout(int align)`](http://download.oracle.com/javase/7/docs/api/java/awt/FlowLayout.html#FlowLayout(int)) | Creates a new flow layout manager with the indicated alignment and horizontal and vertical gaps with the default size of 5 pixels. The alignment argument can be `FlowLayout.LEADING`, `FlowLayout.CENTER`, or `FlowLayout.TRAILING`. When the `FlowLayout` object controls a container with a left-to right component orientation (the default), the `LEADING` value specifies the components to be left-aligned and the `TRAILING` value specifies the components to be right-aligned. |
> | [`FlowLayout (int align, int hgap, int vgap)`](http://download.oracle.com/javase/7/docs/api/java/awt/FlowLayout.html#FlowLayout(int,%20int,%20int)) | Creates a new flow layout manager with the indicated alignment and the indicated horizontal and vertical gaps. The `hgap` and `vgap` arguments specify the number of pixels to put between components. |

### Examples that Use FlowLayout

> The following table lists code examples that use the `FlowLayout` class and
> provides links to related sections.
>
> | Example | Where Described | Notes |
> | --- | --- | --- |
> | [`FlowLayoutDemo`](../examples/layout/index.html#FlowLayoutDemo) | This page | Sets up a content pane to use `FlowLayout`. If you set the `RIGHT_TO_LEFT` constant to `true` and recompile, you can see how `FlowLayout` handles a container that has a right-to-left component orientation. |
> | [`CardLayoutDemo`](../examples/layout/index.html#CardLayoutDemo) | [How to Use CardLayout](card.html) | Centers a component nicely in the top part of a `BorderLayout`, and puts the component in a `JPanel` that uses a `FlowLayout`. |
> | [`ButtonDemo`](../examples/components/index.html#ButtonDemo) | [How to Use Buttons, Check Boxes, and Radio Buttons](../components/button.html) | Uses the default `FlowLayout` of a `JPanel`. |
> | [`TextInputDemo`](../examples/components/index.html#TextInputDemo) | [How to Use Formatted Text Fields](../components/formattedtextfield.html) | Uses a panel with a right-aligned `FlowLayout` presenting two buttons. |

[« Previous](card.html)
•
[Trail](../TOC.html)
•
[Next »](gridbag.html)

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

**Previous page:** How to Use CardLayout
  
**Next page:** How to Use GridBagLayout




A browser with JavaScript enabled is required for this page to operate properly.