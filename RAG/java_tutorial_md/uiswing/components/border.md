[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Creating a GUI With JFC/Swing
  
**Lesson:** Using Swing Components

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

How to Use Borders

[Solving Common Component Problems](problems.html)

[Home Page](../../index.html)
>
[Creating a GUI With JFC/Swing](../index.html)
>
[Using Swing Components](index.html)

[« Previous](icon.html) • [Trail](../TOC.html) • [Next »](problems.html)

# How to Use Borders

Every `JComponent`
can have one or more borders.
Borders are incredibly useful objects
that, while not themselves components,
know how to draw
the edges of Swing components.
Borders are useful not only for drawing lines and fancy edges,
but also for providing titles and empty space around components.

---

**Note:** 
Our examples set borders on `JPanel`s,
`JLabel`s, and custom subclasses of
`JComponent`. Although technically you can set the border
on any object that inherits from `JComponent`, the look and feel
implementation of many standard Swing components doesn't work well with
user-set borders. In general, when you want to set a border on a
standard Swing component other than `JPanel` or `JLabel`,
we recommend that you put the component in a `JPanel` and set
the border on the `JPanel`.

---

To put a border around a `JComponent`,
you use its
`setBorder` method.
You can use the
[`BorderFactory`](http://download.oracle.com/javase/7/docs/api/javax/swing/BorderFactory.html) class to create most of the borders that Swing provides.
If you need a reference to a border — say, because you
want to use it in multiple components — you can save
it in a variable of type
[`Border`](http://download.oracle.com/javase/7/docs/api/javax/swing/border/Border.html). Here is an example of code that creates a bordered container:

```

JPanel pane = new JPanel();
pane.setBorder(BorderFactory.createLineBorder(Color.black));

```

Here's a picture of the container,
which contains a label component.
The black line drawn by the border
marks the edge of the container.

![A line border](../../figures/uiswing/components/BorderDemo-line.png)

The rest of this page discusses the following topics:

* [The BorderDemo Example](#demo)* [Using the Borders Provided by Swing](#code)* [Creating Custom Borders](#custom)* [The Border API](#api)* [Examples of Using Borders](#eg)

### The BorderDemo Example

> The following pictures show an application
> called `BorderDemo` that
> displays the borders Swing provides.
> We show the code for creating these borders
> a little later,
> in [Using the Borders Provided by Swing](#code).
>
> Click the Launch button to run the BorderDemo example using
> [Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp) ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
> Alternatively, to compile and run the example yourself,
> consult the
> [example index](../examples/components/index.html#BorderDemo).
>
> [![Launches the BorderDemo example](../../images/jws-launch-button.png
> )](http://download.oracle.com/javase/tutorialJWS/uiswing/components/ex6/BorderDemo.jnlp)
>
> ![BorderDemo: Simple Borders](../../figures/uiswing/components/BorderDemo1.png)
>
> The next picture shows some matte borders.
> When creating a matte border,
> you specify how many pixels it occupies
> at the top, left, bottom, and right of a component.
> You then specify either a color or an icon
> for the matte border to draw.
> You need to be careful when choosing the icon
> and determining your component's size;
> otherwise, the icon might
> get chopped off or have mismatch at the component's corners.
>
> ![BorderDemo: Matte Borders](../../figures/uiswing/components/BorderDemo2.png)
>
> The next picture shows titled borders.
> Using a titled border,
> you can convert any border into
> one that displays a text description.
> If you don't specify a border,
> a look-and-feel-specific border is used.
> For example, the default titled border
> in the Java look and feel uses a gray line,
> and the default titled border in the Windows look and feel
> uses an etched border.
> By default, the title straddles the upper left
> of the border,
> as shown at the top of the following figure.
>
> ![BorderDemo: Titled Borders](../../figures/uiswing/components/BorderDemo3.png)
>
> The next picture shows compound borders.
> With compound borders, you can combine any two borders,
> which can themselves be compound borders.
>
> ![BorderDemo: Compound Borders](../../figures/uiswing/components/BorderDemo4.png)

### Using the Borders Provided by Swing

> The code that follows shows how to create and set the borders you
> saw in the preceding figures. You can find the program's code in
> [`BorderDemo.java`](../examples/components/BorderDemoProject/src/components/BorderDemo.java).
>
> ```
>
> //Keep references to the next few borders,
> //for use in titles and compound borders.
> Border blackline, raisedetched, loweredetched,
>        raisedbevel, loweredbevel, empty;
>
> blackline = BorderFactory.createLineBorder(Color.black);
> raisedetched = BorderFactory.createEtchedBorder(EtchedBorder.RAISED);
> loweredetched = BorderFactory.createEtchedBorder(EtchedBorder.LOWERED);
> raisedbevel = BorderFactory.createRaisedBevelBorder();
> loweredbevel = BorderFactory.createLoweredBevelBorder();
> empty = BorderFactory.createEmptyBorder();
>
> //Simple borders
> jComp1.setBorder(blackline);
> jComp2.setBorder(raisedbevel);
> jComp3.setBorder(loweredbevel);
> jComp4.setBorder(empty);
>
> //Matte borders
> ImageIcon icon = createImageIcon("images/wavy.gif",
>                                  "wavy-line border icon"); //20x22
>
> jComp5.setBorder(BorderFactory.createMatteBorder(
>                                    -1, -1, -1, -1, icon));
> jComp6.setBorder(BorderFactory.createMatteBorder(
>                                     1, 5, 1, 1, Color.red));
> jComp7.setBorder(BorderFactory.createMatteBorder(
>                                     0, 20, 0, 0, icon));
>
> //Titled borders
> TitledBorder title;
> title = BorderFactory.createTitledBorder("title");
> jComp8.setBorder(title);
>
> title = BorderFactory.createTitledBorder(
> 		       blackline, "title");
> title.setTitleJustification(TitledBorder.CENTER);
> jComp9.setBorder(title);
>
> title = BorderFactory.createTitledBorder(
> 		       loweredetched, "title");
> title.setTitleJustification(TitledBorder.RIGHT);
> jComp10.setBorder(title);
>
> title = BorderFactory.createTitledBorder(
> 		       loweredbevel, "title");
> title.setTitlePosition(TitledBorder.ABOVE_TOP);
> jComp11.setBorder(title);
>
> title = BorderFactory.createTitledBorder(
> 		       empty, "title");
> title.setTitlePosition(TitledBorder.BOTTOM);
> jComp12.setBorder(title);
>
> //Compound borders
> Border compound;
> Border redline = BorderFactory.createLineBorder(Color.red);
>
> //This creates a nice frame.
> compound = BorderFactory.createCompoundBorder(
> 			  raisedbevel, loweredbevel);
> jComp13.setBorder(compound);
>
> //Add a red outline to the frame.
> compound = BorderFactory.createCompoundBorder(
> 			  redline, compound);
> jComp14.setBorder(compound);
>
> //Add a title to the red-outlined frame.
> compound = BorderFactory.createTitledBorder(
> 			  compound, "title",
> 			  TitledBorder.CENTER,
> 			  TitledBorder.BELOW_BOTTOM);
> jComp15.setBorder(compound);
>
> ```
>
> As you probably noticed,
> the code uses the `BorderFactory` class
> to create each border.
> The `BorderFactory` class,
> which is in the `javax.swing` package,
> returns objects that implement the
> [`Border`](http://download.oracle.com/javase/7/docs/api/javax/swing/border/Border.html) interface.
>
> The `Border` interface,
> as well as its Swing-provided implementations,
> is in the
> [`javax.swing.border`](http://download.oracle.com/javase/7/docs/api/javax/swing/border/package-summary.html) package.
> You often don't need to directly use anything in the border package,
> except when specifying constants that are specific
> to a particular border class or when referring to
> the `Border` type.

### Creating Custom Borders

> If `BorderFactory` doesn't offer you enough control
> over a border's form,
> then you might need to directly use the API in the border package —
> or even define your own border.
> In addition to containing the `Border` interface,
> the border package
> contains the classes that implement the
> borders you've already seen:
> [`LineBorder`](http://download.oracle.com/javase/7/docs/api/javax/swing/border/LineBorder.html),
> [`EtchedBorder`](http://download.oracle.com/javase/7/docs/api/javax/swing/border/EtchedBorder.html),
> [`BevelBorder`](http://download.oracle.com/javase/7/docs/api/javax/swing/border/BevelBorder.html),
> [`EmptyBorder`](http://download.oracle.com/javase/7/docs/api/javax/swing/border/EmptyBorder.html),
> [`MatteBorder`](http://download.oracle.com/javase/7/docs/api/javax/swing/border/MatteBorder.html),
> [`TitledBorder`](http://download.oracle.com/javase/7/docs/api/javax/swing/border/TitledBorder.html), and
> [`CompoundBorder`](http://download.oracle.com/javase/7/docs/api/javax/swing/border/CompoundBorder.html).
> The border package also contains a class named
> [`SoftBevelBorder`](http://download.oracle.com/javase/7/docs/api/javax/swing/border/SoftBevelBorder.html), which produces a result similar to `BevelBorder`,
> but with softer edges.
>
> If none of the Swing borders
> is suitable, you can implement your own border.
> Generally, you do this by creating a subclass
> of the
> [`AbstractBorder`](http://download.oracle.com/javase/7/docs/api/javax/swing/border/AbstractBorder.html) class.
> In your subclass, you must implement at least one constructor
> and the following two methods:
>
> * `paintBorder`,
>   which contains the drawing code
>   that a `JComponent` executes
>   to draw the border.* `getBorderInsets`,
>     which specifies the amount of space the border needs
>     to draw itself.
>
> If a custom border has insets (and they typically have insets)
> you need to override both
> [`AbstractBorder.getBorderInsets(Component c)`](http://download.oracle.com/javase/7/docs/api/javax/swing/border/AbstractBorder.html#getBorderInsets(java.awt.Component)) and
> [`AbstractBorder.getBorderInsets(Component c, Insets insets)`](http://download.oracle.com/javase/7/docs/api/javax/swing/border/AbstractBorder.html#getBorderInsets(java.awt.Component,%20java.awt.Insets)) to provide the correct insets.
>
> For examples of implementing borders,
> see the source code for the classes in the
> `javax.swing.border` package.

### The Border API

> The following tables list the commonly used
> border methods.
> The API for using borders falls into two categories:
>
> * [Creating a Border with BorderFactory](#createapi)* [Setting or Getting a Component's Border](#setgetapi)
>
> Creating a Border with BorderFactory
>
> | Method | Purpose |
> | [Border createLineBorder(Color)](http://download.oracle.com/javase/7/docs/api/javax/swing/BorderFactory.html#createLineBorder(java.awt.Color))   [Border createLineBorder(Color, int)](http://download.oracle.com/javase/7/docs/api/javax/swing/BorderFactory.html#createLineBorder(java.awt.Color, int)) | Create a line border. The first argument is a `java.awt.Color` object that specifies the color of the line. The optional second argument specifies the width in pixels of the line. |
> | [Border createEtchedBorder()](http://download.oracle.com/javase/7/docs/api/javax/swing/BorderFactory.html#createEtchedBorder())   [Border createEtchedBorder(Color, Color)](http://download.oracle.com/javase/7/docs/api/javax/swing/BorderFactory.html#createEtchedBorder(java.awt.Color, java.awt.Color))   [Border createEtchedBorder(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/BorderFactory.html#createEtchedBorder(int))   [Border createEtchedBorder(int, Color, Color)](http://download.oracle.com/javase/7/docs/api/javax/swing/BorderFactory.html#createEtchedBorder(int, java.awt.Color, java.awt.Color)) | Create an etched border. The optional `Color` arguments specify the highlight and shadow colors to be used. In release 1.3, methods with `int` arguments were added that allow the border methods to be specified as either `EtchedBorder.RAISED` or `EtchedBorder.LOWERED`. The methods without the `int` arguments create a lowered etched border. |
> | [Border createLoweredBevelBorder()](http://download.oracle.com/javase/7/docs/api/javax/swing/BorderFactory.html#createLoweredBevelBorder()) | Create a border that gives the illusion of the component being lower than the surrounding area. |
> ||  |  |
> | --- | --- |
> | [Border createRaisedBevelBorder()](http://download.oracle.com/javase/7/docs/api/javax/swing/BorderFactory.html#createRaisedBevelBorder()) | Create a border that gives the illusion of the component being higher than the surrounding area. |
> | [Border createBevelBorder(int, Color, Color)](http://download.oracle.com/javase/7/docs/api/javax/swing/BorderFactory.html#createBevelBorder(int, java.awt.Color, java.awt.Color))   [Border createBevelBorder(int, Color, Color, Color, Color)](http://download.oracle.com/javase/7/docs/api/javax/swing/BorderFactory.html#createBevelBorder(int, java.awt.Color, java.awt.Color, java.awt.Color, java.awt.Color)) | Create a raised or lowered beveled border, specifying the colors to use. The integer argument can be either `BevelBorder.RAISED` or `BevelBorder.LOWERED`. With the three-argument constructor, you specify the highlight and shadow colors. With the five-argument constructor, you specify the outer highlight, inner highlight, outer shadow, and inner shadow colors, in that order. |
> | [Border createEmptyBorder()](http://download.oracle.com/javase/7/docs/api/javax/swing/BorderFactory.html#createEmptyBorder())   [Border createEmptyBorder(int, int, int, int)](http://download.oracle.com/javase/7/docs/api/javax/swing/BorderFactory.html#createEmptyBorder(int, int, int, int)) | Create an invisible border. If you specify no arguments, then the border takes no space, which is useful when creating a titled border with no visible boundary. The optional arguments specify the number of pixels that the border occupies at the top, left, bottom, and right (in that order) of whatever component uses it. This method is useful for putting empty space around your components. |
> | [MatteBorder createMatteBorder(int, int, int, int, Color)](http://download.oracle.com/javase/7/docs/api/javax/swing/BorderFactory.html#createMatteBorder(int, int, int, int, java.awt.Color))   [MatteBorder createMatteBorder(int, int, int, int, Icon)](http://download.oracle.com/javase/7/docs/api/javax/swing/BorderFactory.html#createMatteBorder(int, int, int, int, javax.swing.Icon)) | Create a matte border. The integer arguments specify the number of pixels that the border occupies at the top, left, bottom, and right (in that order) of whatever component uses it. The color argument specifies the color which with the border should fill its area. The icon argument specifies the icon which with the border should tile its area. |
> | [TitledBorder createTitledBorder(String)](http://download.oracle.com/javase/7/docs/api/javax/swing/BorderFactory.html#createTitledBorder(java.lang.String))   [TitledBorder createTitledBorder(Border)](http://download.oracle.com/javase/7/docs/api/javax/swing/BorderFactory.html#createTitledBorder(javax.swing.border.Border))   [TitledBorder createTitledBorder(Border, String)](http://download.oracle.com/javase/7/docs/api/javax/swing/BorderFactory.html#createTitledBorder(javax.swing.border.Border, java.lang.String))   [TitledBorder createTitledBorder(Border, String, int, int)](http://download.oracle.com/javase/7/docs/api/javax/swing/BorderFactory.html#createTitledBorder(javax.swing.border.Border, java.lang.String, int, int))   [TitledBorder createTitledBorder(Border, String, int, int, Font)](http://download.oracle.com/javase/7/docs/api/javax/swing/BorderFactory.html#createTitledBorder(javax.swing.border.Border, java.lang.String, int, int, java.awt.Font))   [TitledBorder createTitledBorder(Border, String, int, int, Font, Color)](http://download.oracle.com/javase/7/docs/api/javax/swing/BorderFactory.html#createTitledBorder(javax.swing.border.Border, java.lang.String, int, int, java.awt.Font, java.awt.Color)) | Create a titled border. The string argument specifies the title to be displayed. The optional font and color arguments specify the font and color to be used for the title's text. The border argument specifies the border that should be displayed along with the title. If no border is specified, then a look-and-feel-specific default border is used. By default, the title straddles the top of its companion border and is left-justified. The optional integer arguments specify the title's position and justification, in that order. [`TitledBorder`](http://download.oracle.com/javase/7/docs/api/javax/swing/border/TitledBorder.html) defines these possible positions: `ABOVE_TOP`, `TOP` (the default), `BELOW_TOP`, `ABOVE_BOTTOM`, `BOTTOM`, and `BELOW_BOTTOM`. You can specify the justification as `LEADING` (the default), `CENTER`, or `TRAILING`. In locales with Western alphabets `LEADING` is equivalent to `LEFT` and `TRAILING` is equivalent to `RIGHT`. |
> | [CompoundBorder createCompoundBorder(Border, Border)](http://download.oracle.com/javase/7/docs/api/javax/swing/BorderFactory.html#createCompoundBorder(javax.swing.border.Border, javax.swing.border.Border)) | Combine two borders into one. The first argument specifies the outer border; the second, the inner border. |
>
> Setting or Getting a Component's Border
>
> | Method | Purpose |
> | [void setBorder(Border)](http://download.oracle.com/javase/7/docs/api/javax/swing/JComponent.html#setBorder(javax.swing.border.Border))   [Border getBorder()](http://download.oracle.com/javase/7/docs/api/javax/swing/JComponent.html#getBorder()) | Set or get the border of the receiving `JComponent`. |
> | [void setBorderPainted(boolean)](http://download.oracle.com/javase/7/docs/api/javax/swing/AbstractButton.html#setBorderPainted(boolean))   [boolean isBorderPainted()](http://download.oracle.com/javase/7/docs/api/javax/swing/AbstractButton.html#isBorderPainted())   *(in `AbstractButton`, `JMenuBar`, `JPopupMenu`, `JProgressBar`, and `JToolBar`)* | Set or get whether the border of the component should be displayed. |

### Examples that Use Borders

> Many examples in this lesson use borders.
> The following table lists
> a few interesting cases.
>
> | Example | Where Described | Notes |
> | --- | --- | --- |
> | [`BorderDemo`](../examples/components/index.html#BorderDemo) | This section | Shows an example of each type of border that `BorderFactory` can create. Also uses an empty border to add breathing space between each pane and its contents. |
> | [`BoxAlignmentDemo`](../examples/layout/index.html#BoxAlignmentDemo) | [How to Use BoxLayout](../layout/box.html) | Uses titled borders. |
> | [`BoxLayoutDemo`](../examples/layout/index.html#BoxLayoutDemo) | [How to Use BoxLayout](../layout/box.html) | Uses a red line to show where the edge of a container is, so that you can see how the extra space in a box layout is distributed. |
> | [`ComboBoxDemo2`](../examples/components/index.html#ComboBoxDemo2) | [How to Use Combo Boxes](../components/combobox.html) | Uses a compound border to combine a line border with an empty border. The empty border provides space between the line and the component's innards. |

[« Previous](icon.html)
•
[Trail](../TOC.html)
•
[Next »](problems.html)

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

**Previous page:** How to Use Icons
  
**Next page:** Solving Common Component Problems




A browser with JavaScript enabled is required for this page to operate properly.