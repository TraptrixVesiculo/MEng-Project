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

How to Use GridLayout

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

[« Previous](gridbag.html) • [Trail](../TOC.html) • [Next »](group.html)

# How to Use GridLayout

---

**Note:** This lesson covers writing layout code by hand, which can be challenging. If you are not interested in learning all the details of layout management, you might prefer to use the `GroupLayout` layout manager combined with a builder tool to lay out your GUI. One such builder tool is the
[NetBeans IDE](../learn/index.html). Otherwise, if you want to code by hand and do not want to use `GroupLayout`, then `GridBagLayout` is recommended as the next most flexible and powerful layout manager.

---

The following figure represents a snapshot of an application that uses the
[`GridLayout`](http://download.oracle.com/javase/7/docs/api/java/awt/GridLayout.html) class.

![A snapshot of GridLayoutDemo](../../figures/uiswing/layout/GridLayoutDemo.png)

Click the Launch button
to run GridLayoutDemo using
[Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp)
([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
Alternatively, to compile and run the example yourself,
consult the
[example index](../examples/layout/index.html#GridLayoutDemo).

[![Launches the GridLayoutDemo application](../../images/jws-launch-button.png)](http://download.oracle.com/javase/tutorialJWS/uiswing/layout/ex6/GridLayoutDemo.jnlp)

The complete code of this demo is in the
[`GridLayoutDemo.java`](../examples/layout/GridLayoutDemoProject/src/layout/GridLayoutDemo.java) file.

A `GridLayout` object places components in a grid of cells.
Each component takes all the available space within its cell,
and each cell is exactly the same size.
If the `GridLayoutDemo` window is resized,
the `GridLayout` object changes the cell size
so that the cells are as large as possible,
given the space available to the container.

The code snippet below creates the `GridLayout` object and the components it manages.

```


GridLayout experimentLayout = new GridLayout(0,2);

...

	compsToExperiment.setLayout(experimentLayout);

	compsToExperiment.add(new JButton("Button 1"));
	compsToExperiment.add(new JButton("Button 2"));
	compsToExperiment.add(new JButton("Button 3"));
	compsToExperiment.add(new JButton("Long-Named Button 4"));
	compsToExperiment.add(new JButton("5"));

```

The constructor of the `GridLayout` class
creates an instance that has two columns
and as many rows as necessary.

Use combo boxes to set up how much vertical or horizontal padding is put around the components. Then click the Apply gaps button. The following code snippet shows how your selection is processed by using the `setVgap` and `setHgap` methods of the `GridLayout` class:

```


applyButton.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e){
                //Get the horizontal gap value
                String horGap = (String)horGapComboBox.getSelectedItem();
                //Get the vertical gap value
                String verGap = (String)verGapComboBox.getSelectedItem();
                //Set up the horizontal gap value
                experimentLayout.setHgap(Integer.parseInt(horGap));
                //Set up the vertical gap value
                experimentLayout.setVgap(Integer.parseInt(verGap));
                //Set up the layout of the buttons
                experimentLayout.layoutContainer(compsToExperiment);
            }
        });


```

### The GridLayout API

> The following table lists constructors of the `GridLayout` class that specify the number of rows and columns.
>
> The `GridLayout` class constructors
>
> | Constructor | Purpose |
> | [`GridLayout(int rows, int cols)`](http://download.oracle.com/javase/7/docs/api/java/awt/GridLayout.html#GridLayout(int,%20int)) | Creates a grid layout with the specified number of rows and columns. All components in the layout are given equal size. One, but not both, of `rows` and `cols` can be zero, which means that any number of objects can be placed in a row or in a column. |
> | [`GridLayout(int rows, int cols, int hgap, int vgap)`](http://download.oracle.com/javase/7/docs/api/java/awt/GridLayout.html#GridLayout(int,%20int,%20int,%20int)) | Creates a grid layout with the specified number of rows and columns. In addition, the horizontal and vertical gaps are set to the specified values. Horizontal gaps are places between each of columns. Vertical gaps are placed between each of the rows. |
>
> The `GridLayout` class has two constructors:

### Examples that Use GridLayout

> The following table lists code examples that use the `GridLayout` class and
> provides links to related sections.
>
> | Example | Where Described | Notes |
> | --- | --- | --- |
> | [`GridLayoutDemo`](../examples/layout/index.html#GridLayoutDemo) | This page | Uses a 2-column grid. |
> | [`ComboBoxDemo2`](../examples/components/index.html#ComboBoxDemo2) | [How to Use Combo Boxes](../components/combobox.html) | One of many examples that use a 1x1 grid to make a component as large as possible. |
> | [`LabelDemo`](../examples/components/index.html#LabelDemo) | [How to Use Labels](../components/label.html) | Uses a 3-row grid. |

[« Previous](gridbag.html)
•
[Trail](../TOC.html)
•
[Next »](group.html)

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

**Previous page:** How to Use GridBagLayout
  
**Next page:** How to Use GroupLayout




A browser with JavaScript enabled is required for this page to operate properly.