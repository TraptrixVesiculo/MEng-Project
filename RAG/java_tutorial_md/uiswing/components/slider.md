[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Creating a GUI With JFC/Swing
  
**Lesson:** Using Swing Components
  
**Section:** How to Use Various Components

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

How to Use Sliders

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

[How to Use Borders](border.html)

[Solving Common Component Problems](problems.html)

[Home Page](../../index.html)
>
[Creating a GUI With JFC/Swing](../index.html)
>
[Using Swing Components](index.html)

[« Previous](separator.html) • [Trail](../TOC.html) • [Next »](spinner.html)

# How to Use Sliders

A
[`JSlider`](http://download.oracle.com/javase/7/docs/api/javax/swing/JSlider.html) component is intended to let the user easily enter a numeric value bounded
by a minimum and maximum value.
If space is limited,
a [spinner](spinner.html)
is a possible alternative to a slider.

The following picture shows an application that uses
a slider to control animation speed:

![A snapshot of SliderDemo, which uses a slider](../../figures/uiswing/components/SliderDemo.png)

---

**Try this:**

1. Click the Launch button
   to run SliderDemo using
   [Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp)
   ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
   Alternatively, to compile and run the example yourself,
   consult the
   [example index](../examples/components/index.html#SliderDemo).

   [![Launches the SliderDemo application](../../images/jws-launch-button.png)](http://download.oracle.com/javase/tutorialJWS/uiswing/components/ex6/SliderDemo.jnlp)
2. Use the slider to adjust the animation speed.- Push the slider to 0 to stop the animation.

---

Below is the code from the
[`SliderDemo.java`](../examples/components/SliderDemoProject/src/components/SliderDemo.java) file that creates the slider in the previous example.

```

static final int FPS_MIN = 0;
static final int FPS_MAX = 30;
static final int FPS_INIT = 15;    //initial frames per second
. . .
JSlider framesPerSecond = new JSlider(JSlider.HORIZONTAL,
                                      FPS_MIN, FPS_MAX, FPS_INIT);
framesPerSecond.addChangeListener(this);

//Turn on labels at major tick marks.
framesPerSecond.setMajorTickSpacing(10);
framesPerSecond.setMinorTickSpacing(1);
framesPerSecond.setPaintTicks(true);
framesPerSecond.setPaintLabels(true);

```

By default, spacing for major and minor tick marks is zero.
To see tick marks, you must explicitly set the spacing for either
major or minor tick marks (or both) to a non-zero value
and call the `setPaintTicks(true)` method.
However, you also need labels for your tick marks.
To display standard, numeric labels at major tick mark locations,
set the major tick spacing, then call the `setPaintLabels(true)` method.
The example program provides labels for its slider in this way.
But you are not constrained to using only these labels.
[Customizing Labels on a Slider](#labels)
shows you how to customize slider labels.
In addition, a new slider feature available in JDK 6 allows you to set
a font for the `JSlider` component.

```

Font font = new Font("Serif", Font.ITALIC, 15);
framesPerSecond.setFont(font);

```

When you move the slider's knob, the `stateChanged` method of the
slider's `ChangeListener` is called.
For information about change listeners,
refer to [How to Write a Change Listener](../events/changelistener.html).
Here is the change listener code that reacts to slider value changes:

```

public void stateChanged(ChangeEvent e) {
    JSlider source = (JSlider)e.getSource();
    if (!source.getValueIsAdjusting()) {
        int fps = (int)source.getValue();
        if (fps == 0) {
            if (!frozen) stopAnimation();
        } else {
            delay = 1000 / fps;
            timer.setDelay(delay);
            timer.setInitialDelay(delay * 10);
            if (frozen) startAnimation();
        }
    }
}

```

Notice that the `stateChanged` method
changes the animation speed only if the `getValueIsAdjusting` method
returns `false`.
Many change events are fired
as the user moves the slider knob.
This program is interested only
in the final result of the user's action.

### Customizing Labels on a Slider

> The demo below is a modified version of the SliderDemo
> that uses a slider with custom labels:
>
> ![A snapshot of SliderDemo2, which uses a slider with custom labels](../../figures/uiswing/components/SliderDemo2.png)
>
> The source for this program can be found in
> [`SliderDemo2.java`](../examples/components/SliderDemo2Project/src/components/SliderDemo2.java).
> Click the Launch button
> to run SliderDemo2 using
> [Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp)
> ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
> Alternatively, to compile and run the example yourself,
> consult the
> [example index](../examples/components/index.html#SliderDemo2).
>
> [![Launches the SliderDemo2 application](../../images/jws-launch-button.png)](http://download.oracle.com/javase/tutorialJWS/uiswing/components/ex6/SliderDemo2.jnlp)
>
> The following code creates the slider and customizes its labels:
>
> ```
>
> //Create the slider
> JSlider framesPerSecond = new JSlider(JSlider.VERTICAL,
>                                       FPS_MIN, FPS_MAX, FPS_INIT);
> framesPerSecond.addChangeListener(this);
> framesPerSecond.setMajorTickSpacing(10);
> framesPerSecond.setPaintTicks(true);
>
> //Create the label table
> Hashtable labelTable = new Hashtable();
> labelTable.put( new Integer( 0 ), new JLabel("Stop") );
> labelTable.put( new Integer( FPS_MAX/10 ), new JLabel("Slow") );
> labelTable.put( new Integer( FPS_MAX ), new JLabel("Fast") );
> framesPerSecond.setLabelTable( labelTable );
>
> framesPerSecond.setPaintLabels(true);
>
> ```
>
> Each key-value pair in the hashtable
> specified with the `setLabelTable` method
> gives the position and the value of one label.
> The hashtable key must be of an `Integer` type
> and must have a value within the slider's range at which to place the label.
> The hashtable value
> associated with each key
> must be a `Component` object.
> This demo uses `JLabel` instances with text only.
> An interesting modification would be to use
> `JLabel` instances with icons
> or buttons that move the knob to the label's position.
>
> Use the `createStandardLabels` method of the `JSlider`
> class to create a set of numeric labels positioned
> at a specific interval.
> You can also modify the table returned
> by the `createStandardLabels` method in order to customize it.

### The Slider API

> The following tables list the commonly used
> `JSlider` constructors and methods.
> See
> [The JComponent Class](jcomponent.html)
> for tables of commonly used inherited methods.
>
> The API for using sliders is divided into these categories:
>
> * [Creating the Slider](#creating)* [Fine Tuning the Slider's Appearance](#looks)* [Watching the Slider Operate](#operation)* [Working Directly with the Data Model](#modelapi)
>
> Creating the Slider
>
> | Constructor | Purpose |
> | [JSlider()](http://download.oracle.com/javase/7/docs/api/javax/swing/JSlider.html#JSlider()) | Creates a horizontal slider with the range 0 to 100 and an initial value of 50. |
> | [JSlider(int min, int max)](http://download.oracle.com/javase/7/docs/api/javax/swing/JSlider.html#JSlider(int, int))   [JSlider(int min, int max, int value)](http://download.oracle.com/javase/7/docs/api/javax/swing/JSlider.html#JSlider(int, int, int)) | Creates a horizontal slider with the specified minimum and maximum values. The third `int` argument, when present, specifies the slider's initial value. |
> | [JSlider(int orientation)](http://download.oracle.com/javase/7/docs/api/javax/swing/JSlider.html#JSlider(int))   [JSlider(int orientation, int min, int max, int value)](http://download.oracle.com/javase/7/docs/api/javax/swing/JSlider.html#JSlider(int, int, int, int)) | Creates a slider with the specified orientation, which must be either `JSlider.HORIZONTAL` or `JSlider.VERTICAL`. The last three `int` arguments, when present, specify the slider's minimum, maximum, and initial values, respectively. |
> | [JSlider(BoundedRangeModel)](http://download.oracle.com/javase/7/docs/api/javax/swing/JSlider.html#JSlider(javax.swing.BoundedRangeModel)) | Creates a horizontal slider with the specified model, which manages the slider's minimum, maximum, and current values and their relationships. |
>
> Fine Tuning the Slider's Appearance
>
> | Method | Purpose |
> | [void setValue(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JSlider.html#setValue(int))   [int getValue()](http://download.oracle.com/javase/7/docs/api/javax/swing/JSlider.html#getValue()) | Sets or gets the slider's current value. The set method also positions the slider's knob. |
> | [void setOrientation(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JSlider.html#setOrientation(int))   [int getOrientation()](http://download.oracle.com/javase/7/docs/api/javax/swing/JSlider.html#getOrientation()) | Sets or gets the orientation of the slider. Possible values are `JSlider.HORIZONTAL` or `JSlider.VERTICAL`. |
> | [void setInverted(boolean)](http://download.oracle.com/javase/7/docs/api/javax/swing/JSlider.html#setInverted(boolean))   [boolean getInverted()](http://download.oracle.com/javase/7/docs/api/javax/swing/JSlider.html#getInverted()) | Sets or gets whether the maximum is shown at the left of a horizontal slider or at the bottom of a vertical one, thereby inverting the slider's range. |
> | [void setMinimum(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JSlider.html#setMinimum(int))   [int getMinimum()](http://download.oracle.com/javase/7/docs/api/javax/swing/JSlider.html#getMinimum())   [void setMaximum(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JSlider.html#setMaximum(int))   [int getMaximum()](http://download.oracle.com/javase/7/docs/api/javax/swing/JSlider.html#getMaximum()) | Sets or gets the minimum or maximum values of the slider. Together, these methods set or get the slider's range. |
> | [void setMajorTickSpacing(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JSlider.html#setMajorTickSpacing(int))   [int getMajorTickSpacing()](http://download.oracle.com/javase/7/docs/api/javax/swing/JSlider.html#getMajorTickSpacing())   [void setMinorTickSpacing(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JSlider.html#setMinorTickSpacing(int))   [int getMinorTickSpacing()](http://download.oracle.com/javase/7/docs/api/javax/swing/JSlider.html#getMinorTickSpacing()) | Sets or gets the range between major and minor ticks. You must call `setPaintTicks(true)` for the tick marks to appear. |
> | [void setPaintTicks(boolean)](http://download.oracle.com/javase/7/docs/api/javax/swing/JSlider.html#setPaintTicks(boolean))   [boolean getPaintTicks()](http://download.oracle.com/javase/7/docs/api/javax/swing/JSlider.html#getPaintTicks()) | Sets or gets whether tick marks are painted on the slider. |
> | [void setPaintLabels(boolean)](http://download.oracle.com/javase/7/docs/api/javax/swing/JSlider.html#setPaintLabels(boolean))   [boolean getPaintLabels()](http://download.oracle.com/javase/7/docs/api/javax/swing/JSlider.html#getPaintLabels()) | Sets or gets whether labels are painted on the slider. You can provide custom labels with `setLabelTable` or get automatic labels by setting the major tick spacing to a non-zero value. |
> | [void setLabelTable(Dictionary)](http://download.oracle.com/javase/7/docs/api/javax/swing/JSlider.html#setLabelTable(java.util.Dictionary))   [Dictionary getLabelTable()](http://download.oracle.com/javase/7/docs/api/javax/swing/JSlider.html#getLabelTable()) | Sets or gets the labels for the slider. You must call `setPaintLabels(true)` for the labels to appear. |
> | [Hashtable createStandardLabels(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JSlider.html#createStandardLabels(int))   [Hashtable createStandardLabels(int, int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JSlider.html#createStandardLabels(int, int)) | Creates a standard set of numeric labels. The first `int` argument specifies the increment, the second `int` argument specifies the starting point. When left unspecified, the starting point is set to the slider's minimum number. |
> | [setFont(java.awt.Font)](http://download.oracle.com/javase/7/docs/api/javax/swing/JSlider.html#setFont(java.awt.Font)) | Sets the font for slider labels . |
>
> Watching the Slider Operate
>
> | Method | Purpose |
> | [void addChangeListener(ChangeListener)](http://download.oracle.com/javase/7/docs/api/javax/swing/JSlider.html#addChangeListener(javax.swing.event.ChangeListener)) | Registers a change listener with the slider. |
> | [boolean getValueIsAdjusting()](http://download.oracle.com/javase/7/docs/api/javax/swing/JSlider.html#getValueIsAdjusting()) | Determines whether the user gesture to move the slider's knob is complete. |
>
> Working Directly with the Data Model
>
> | Class, Interface, or Method | Purpose |
> | [BoundedRangeModel](http://download.oracle.com/javase/7/docs/api/javax/swing/BoundedRangeModel.html) | The interface required for the slider's data model. |
> | [DefaultBoundedRangeModel](http://download.oracle.com/javase/7/docs/api/javax/swing/DefaultBoundedRangeModel.html) | An implementation of the `BoundedRangeModel` interface. |
> | [void setModel()](http://download.oracle.com/javase/7/docs/api/javax/swing/JSlider.html#setModel(javax.swing.BoundedRangeModel))  [getModel()](http://download.oracle.com/javase/7/docs/api/javax/swing/JSlider.html#getModel())  *(in `JSlider`)* | Sets or gets the data model used by the slider. You can also set the model by using the constructor that takes a single argument of type `BoundedRangeModel`. |

### Examples that Use Sliders

> This table shows the examples that use `JSlider`
> and where those examples are described.
>
> | Example | Where Described | Notes |
> | --- | --- | --- |
> | [`SliderDemo`](../examples/components/index.html#SliderDemo) | This section | Shows a slider with labels at major tick marks. |
> | [`SliderDemo2`](../examples/components/index.html#SliderDemo2) | This section | Shows a vertical slider with custom labels. |
> | [`Converter`](../examples/components/index.html#Converter) | [Using Models](model.html), [How to Use Panels](panel.html) | A measurement conversion application featuring two sliders that share data and have custom `BoundedRangeModel`s. |

[« Previous](separator.html)
•
[Trail](../TOC.html)
•
[Next »](spinner.html)

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

**Previous page:** How to Use Separators
  
**Next page:** How to Use Spinners




A browser with JavaScript enabled is required for this page to operate properly.