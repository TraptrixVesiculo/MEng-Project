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

How to Use Models

[How to Use Icons](icon.html)

[How to Use Borders](border.html)

[Solving Common Component Problems](problems.html)

[Home Page](../../index.html)
>
[Creating a GUI With JFC/Swing](../index.html)
>
[Using Swing Components](index.html)

[« Previous](html.html) • [Trail](../TOC.html) • [Next »](icon.html)

# How to Use Models

Most Swing components have models.
A button (`JButton`), for example,
has a model (a `ButtonModel` object)
that stores the button's state —
what its keyboard mnemonic is,
whether it's enabled, selected, or pressed,
and so on.
Some components have multiple models.
A list (`JList`), for example,
uses a `ListModel`
to hold the list's contents,
and a `ListSelectionModel`
to track the list's current selection.

You often don't need to know about the models
that a component uses.
For example, programs that use buttons
usually deal directly with the `JButton` object,
and don't deal at all with the `ButtonModel` object.

Why then do models exist?
The biggest reason is that they give you
flexibility in determining how data is stored and retrieved.
For example,
if you're designing a spreadsheet application
that displays data in a sparsely populated table,
you can create your own table model
that is optimized for such use.

Models have other benefits, too.
They mean that data isn't copied between
a program's data structures
and those of the Swing components.
Also, models automatically
propagate changes to all interested listeners,
making it easy for the GUI to stay in sync with the data.
For example, to add items to a list
you can invoke methods on the list model.
When the model's data changes,
the model fires events to
the `JList` and any other registered listeners,
and the GUI is updated accordingly.

Although Swing's model architecture
is sometimes referred to as a
Model-View-Controller (MVC) design,
it really isn't.
Swing components are generally implemented
so that the view and controller are indivisible,
implemented by a single UI object
provided by the look and feel.
The Swing model architecture is more accurately described as a
*separable model architecture*.
If you're interested in learning more about the Swing model architecture, see
[A Swing Architecture Overview](http://java.sun.com/products/jfc/tsc/articles/architecture/), an article in
*The Swing Connection*.

### An Example: Converter

> This section features an example called Converter,
> which is an application that continuously converts distance measurements
> between metric and U.S. units.
> You can
> [**run Converter**](http://download.oracle.com/javase/tutorialJWS/uiswing/components/ex6/Converter.jnlp) (
> [download JDK 6](http://java.sun.com/javase/downloads/index.jsp)). Or, to compile and run the example yourself,
> consult the
> [example index](../examples/components/index.html#Converter).
>
> As the following picture shows,
> Converter features two sliders,
> each tied to a text field.
> The sliders and text fields all display the same data
> — a distance — but using two different units of measure.
>
> ![Converter screenshot in the Metal look and feel](../../figures/uiswing/components/ConverterMetal.png)
>
> The important thing for this program
> is ensuring that only one model
> controls the value of the data.
> There are various ways to achieve this;
> we did it by deferring to the top slider's model.
> The bottom slider's model
> (an instance of a custom class called `FollowerRangeModel`)
> forwards all data queries to the top slider's model
> (an instance of a custom class called `ConverterRangeModel`).
> Each text field is kept in sync with its slider,
> and vice versa,
> by event handlers that listen for changes in value.
> Care is taken to ensure that the top slider's model
> has the final say about what distance is displayed.
>
> When we started implementing the custom slider models,
> we first looked at
> the API section of
> [How to Use Sliders](../components/slider.html). It informed us that all slider data models must
> implement the `BoundedRangeModel` interface.
> The
> [`BoundedRangeModel` API documentation](http://download.oracle.com/javase/7/docs/api/javax/swing/BoundedRangeModel.html) tells us
> that the interface has an implementing class named
> `DefaultBoundedRangeModel`.
> The
> [API documentation for `DefaultBoundedRangeModel`](http://download.oracle.com/javase/7/docs/api/javax/swing/DefaultBoundedRangeModel.html) shows that it's a general-purpose implementation
> of `BoundedRangeModel`.
>
> We didn't use `DefaultBoundedRangeModel`
> directly because it stores data as integers,
> and Converter uses floating-point data.
> Thus, we implemented
> `ConverterRangeModel` as a subclass of
> `Object`.
> We then implemented `FollowerRangeModel`
> as a subclass of `ConverterRangeModel`.

### For Further Information

> To find out about the models for individual components,
> see the
> ["How to"](componentlist.html) pages
> and API documentation
> for individual components.
> Here are some of our examples that use models directly:
>
> * All but the simplest of the
>   [table examples](table.html#eg)
>   implement custom table data models.* The [color chooser demos](colorchooser.html#eg)
>     have change listeners on the color chooser's selection model
>     so they can be notified when the user selects a new color.
>     In ColorChooserDemo2, the `CrayonPanel` class
>     directly uses the color selection model
>     to set the current color.* The
>       [DynamicTreeDemo](../examples/components/index.html#DynamicTreeDemo)
>       example sets the tree model
>       (to an instance of `DefaultTreeModel`),
>       interacts directly with it,
>       and listens for changes to it.* [ListDemo](../examples/components/index.html#ListDemo)
>         sets the list data model
>         (to an instance of `DefaultListModel`)
>         and interacts directly with it.* [SharedModelDemo](../examples/components/index.html#SharedModelDemo)
>           defines a `SharedDataModel` class that extends
>           `DefaultListModel` and implements
>           `TableModel`.
>           A `JList` and `JTable`
>           share an instance of `SharedDataModel`,
>           providing different views of the model's data.* In the event listener examples,
>             [ListDataEventDemo](../events/../examples/events/index.html#ListDataEventDemo) creates and uses a `DefaultListModel` directly.* Our [spinner examples](spinner.html#eg)
>               create spinner models.* As you've already seen, the
>                 [Converter](../examples/components/index.html#Converter)
>                 example defines
>                 two custom slider models.

[« Previous](html.html)
•
[Trail](../TOC.html)
•
[Next »](icon.html)

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

**Previous page:** How to Use HTML in Swing Components
  
**Next page:** How to Use Icons




A browser with JavaScript enabled is required for this page to operate properly.