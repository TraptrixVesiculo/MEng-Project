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

How to Use Labels

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

[How to Use Borders](border.html)

[Solving Common Component Problems](problems.html)

[Home Page](../../index.html)
>
[Creating a GUI With JFC/Swing](../index.html)
>
[Using Swing Components](index.html)

[« Previous](internalframe.html) • [Trail](../TOC.html) • [Next »](layeredpane.html)

# How to Use Labels

With the
[`JLabel`](http://download.oracle.com/javase/7/docs/api/javax/swing/JLabel.html) class,
you can display unselectable text and images.
If you need to create a component
that displays a string, an image, or both,
you can do so by using or extending `JLabel`.
If the component is interactive and has a certain state,
use a
[button](button.html)
instead of a label.

By specifying HTML code in a label's text,
you can give the label various characteristics such as
multiple lines, multiple fonts or
multiple colors.
If the label uses just a single color or font,
you can avoid the overhead of HTML processing by using
the `setForeground` or `setFont` method instead.
See
[Using HTML in Swing Components](html.html)
for details.

Note that labels are not opaque by default. If you need to paint the label's
background, it is recommended that you turn its opacity property to "true".
The following code snippet shows how to do this.

```

label.setOpaque(true);

```

The following picture introduces an application
that displays three labels.
The window is divided into three rows of equal height;
the label in each row is as wide as possible.

![A snapshot of LabelDemo, which uses labels with text and icons.](../../figures/uiswing/components/LabelDemoMetal.png)

---

**Try this:**

1. Click the Launch button 
   to run LabelDemo using
   [Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp )
   ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
   Alternatively, to compile and run the example yourself,
   consult the
   [example index](../examples/components/index.html#LabelDemo).

[![Launches the LabelDemo Application](../../images/jws-launch-button.png)](http://download.oracle.com/javase/tutorialJWS/uiswing/components/ex6/LabelDemo.jnlp)

2. Resize the window so you can see
   how the labels' contents are placed
   within the labels' drawing area.
     
   All the label contents have default vertical alignment —
   that is, the label contents are centered vertically
   in the label's drawing area.
   The top label,
   which contains both an image and text,
   has horizontal center alignment.
   The second label, which contains just text,
   has left (leading) alignment,
   which is the default for text-only labels
   in left-to-right languages.
   The third label, which contains just an image,
   has horizontal center alignment,
   which is the default for image-only labels.

---

Below is the code from
[`LabelDemo.java`](../examples/components/LabelDemoProject/src/components/LabelDemo.java)
that creates the labels in the previous example.

```

ImageIcon icon = createImageIcon("images/middle.gif");
. . .
label1 = new JLabel("Image and Text",
                    icon,
                    JLabel.CENTER);
//Set the position of the text, relative to the icon:
label1.setVerticalTextPosition(JLabel.BOTTOM);
label1.setHorizontalTextPosition(JLabel.CENTER);

label2 = new JLabel("Text-Only Label");
label3 = new JLabel(icon);

```

The code for the `createImageIcon` method
is similar to that used throughout this tutorial.
You can find it in
[How to Use Icons](../components/icon.html).

Often, a label describes another component.
When this occurs,
you can improve your program's accessibility
by using the `setLabelFor` method
to identify the component that the label describes.
For example:

```

amountLabel.setLabelFor(amountField);

```

The preceding code,
taken from the `FormattedTextFieldDemo` example
discussed in
[How to Use Formatted Text Fields](formattedtextfield.html),
lets assistive technologies know
that the label (`amountLabel`)
provides information about the formatted text field (`amountField`).
For more information about assistive technologies, see
[How to Support Assistive Technologies](../misc/access.html).

### The Label API

> The following tables list the commonly used
> `JLabel` constructors and methods.
> Other methods you are likely to call
> are defined by the
> `Component`
> and
> `JComponent` classes.
> They include `setFont`,
> `setForeground`,
> `setBorder`,
> `setOpaque`, and
> `setBackground`.
> See [The JComponent Class](jcomponent.html)
> for details.
> The API for using labels falls into three categories:
>
> * [Setting or Getting the Label's Contents](#contentsapi)* [Fine Tuning the Label's Appearance](#looksapi)* [Supporting Accessibility](#accessapi)
>
> ---
>
> **Note:** In the following API, do not confuse label alignment with
> X and Y alignment.
> X and Y alignment are used by layout managers
> and can affect the way any component — not just a label —
> is sized or positioned.
> Label alignment, on the other hand,
> has no effect on a label's size or position.
> Label alignment simply determines where,
> inside the label's painting area,
> the label's contents are positioned.
> Typically,
> the label's painting area is exactly the size needed
> to paint on the label
> and thus label alignment is irrelevant.
> For more information about X and Y alignment, see
> [How to Use BoxLayout](../layout/box.html).
>
> ---
>
> **Setting or Getting the Label's Contents**
>
> | Method or Constructor | Purpose |
> | [JLabel(Icon)](http://download.oracle.com/javase/7/docs/api/javax/swing/JLabel.html#JLabel(javax.swing.Icon))   [JLabel(Icon, int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JLabel.html#JLabel(javax.swing.Icon, int))   [JLabel(String)](http://download.oracle.com/javase/7/docs/api/javax/swing/JLabel.html#JLabel(java.lang.String))   [JLabel(String, Icon, int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JLabel.html#JLabel(java.lang.String, javax.swing.Icon, int))   [JLabel(String, int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JLabel.html#JLabel(java.lang.String, int))   [JLabel()](http://download.oracle.com/javase/7/docs/api/javax/swing/JLabel.html#JLabel()) | Creates a `JLabel` instance, initializing it to have the specified text/image/alignment. The `int` argument specifies the horizontal alignment of the label's contents within its drawing area. The horizontal alignment must be one of the following constants defined in the [`SwingConstants`](http://download.oracle.com/javase/7/docs/api/javax/swing/SwingConstants.html) interface (which `JLabel` implements): `LEFT`, `CENTER`, `RIGHT`, `LEADING`, or `TRAILING`. For ease of localization, we strongly recommend using `LEADING` and `TRAILING`, rather than `LEFT` and `RIGHT`. |
> | [void setText(String)](http://download.oracle.com/javase/7/docs/api/javax/swing/JLabel.html#setText(java.lang.String))   [String getText()](http://download.oracle.com/javase/7/docs/api/javax/swing/JLabel.html#getText()) | Sets or gets the text displayed by the label. You can use HTML tags to format the text, as described in [Using HTML in Swing Components](html.html). |
> | [void setIcon(Icon)](http://download.oracle.com/javase/7/docs/api/javax/swing/JLabel.html#setIcon(javax.swing.Icon))   [Icon getIcon()](http://download.oracle.com/javase/7/docs/api/javax/swing/JLabel.html#getIcon()) | Sets or gets the image displayed by the label. |
> | [void setDisplayedMnemonic(char)](http://download.oracle.com/javase/7/docs/api/javax/swing/JLabel.html#setDisplayedMnemonic(char))   [char getDisplayedMnemonic()](http://download.oracle.com/javase/7/docs/api/javax/swing/JLabel.html#getDisplayedMnemonic()) | Sets or gets the letter that should look like a keyboard alternative. This is helpful when a label describes a component (such as a text field) that has a keyboard alternative but cannot display it. If the labelFor property is also set (using `setLabelFor`), then when the user activates the mnemonic, the keyboard focus is transferred to the component specified by the labelFor property. |
> | [void setDisplayedMnemonicIndex(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JLabel.html#setDisplayedMnemonicIndex(int))   [int getDisplayedMnemonicIndex()](http://download.oracle.com/javase/7/docs/api/javax/swing/JLabel.html#getDisplayedMnemonicIndex()) | Sets or gets a hint as to which character in the text should be decorated to represent the mnemonic. This is useful when you have two instances of the same character and wish to decorate the second instance. For example, `setDisplayedMnemonicIndex(5)` decorates the character that is at position 5 (that is, the 6th character in the text). Not all types of look and feel may support this feature. |
> | [void setDisabledIcon(Icon)](http://download.oracle.com/javase/7/docs/api/javax/swing/JLabel.html#setDisabledIcon(javax.swing.Icon))   [Icon getDisabledIcon()](http://download.oracle.com/javase/7/docs/api/javax/swing/JLabel.html#getDisabledIcon()) | Sets or gets the image displayed by the label when it is disabled. If you do not specify a disabled image, then the look and feel creates one by manipulating the default image. |
>
> **Fine Tuning the Label's Appearance**
>
> | Method | Purpose |
> | [void setHorizontalAlignment(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JLabel.html#setHorizontalAlignment(int))   [void setVerticalAlignment(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JLabel.html#setVerticalAlignment(int))   [int getHorizontalAlignment()](http://download.oracle.com/javase/7/docs/api/javax/swing/JLabel.html#getHorizontalAlignment())   [int getVerticalAlignment()](http://download.oracle.com/javase/7/docs/api/javax/swing/JLabel.html#getVerticalAlignment()) | Sets or gets the area on the label where its contents should be placed. The [`SwingConstants`](http://download.oracle.com/javase/7/docs/api/javax/swing/SwingConstants.html) interface defines five possible values for horizontal alignment: `LEFT`, `CENTER` (the default for image-only labels), `RIGHT`, `LEADING` (the default for text-only labels), `TRAILING`. For vertical alignment: `TOP`, `CENTER` (the default), and `BOTTOM`. |
> | [void setHorizontalTextPosition(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JLabel.html#setHorizontalTextPosition(int))   [void setVerticalTextPosition(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JLabel.html#setVerticalTextPosition(int))   [int getHorizontalTextPosition()](http://download.oracle.com/javase/7/docs/api/javax/swing/JLabel.html#getHorizontalTextPosition())   [int getVerticalTextPosition()](http://download.oracle.com/javase/7/docs/api/javax/swing/JLabel.html#getVerticalTextPosition()) | Sets or gets the location where the label's text will be placed, relative to the label's image. The [`SwingConstants`](http://download.oracle.com/javase/7/docs/api/javax/swing/SwingConstants.html) interface defines five possible values for horizontal position: `LEADING`, `LEFT`, `CENTER`, `RIGHT`, and `TRAILING` (the default). For vertical position: `TOP`, `CENTER` (the default), and `BOTTOM`. |
> | [void setIconTextGap(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JLabel.html#setIconTextGap(int))   [int getIconTextGap()](http://download.oracle.com/javase/7/docs/api/javax/swing/JLabel.html#getIconTextGap()) | Sets or gets the number of pixels between the label's text and its image. |
>
> **Supporting Accessibility**
>
> | Method | Purpose |
> | [void setLabelFor(Component)](http://download.oracle.com/javase/7/docs/api/javax/swing/JLabel.html#setLabelFor(java.awt.Component))   [Component getLabelFor()](http://download.oracle.com/javase/7/docs/api/javax/swing/JLabel.html#getLabelFor()) | Sets or gets which component the label describes. |

### Examples That Use Labels

> The following table lists some of the many
> examples that use labels.
>
> | Example | Where Described | Notes |
> | --- | --- | --- |
> | [`LabelDemo`](../examples/components/index.html#LabelDemo) | This section | Shows how to specify horizontal and vertical alignment as well as how to align a label's text and image. |
> | [`HtmlDemo`](../examples/components/index.html#HtmlDemo) | [Using HTML in Swing Components](html.html) | Lets you experiment with specifying HTML text for a label. |
> | [`BoxAlignmentDemo`](../examples/layout/index.html#BoxAlignmentDemo) | [Fixing Alignment Problems](../layout/box.html#alignment) | Demonstrates possible alignment problems when using a label in a vertical box layout. Shows how to solve the problem. |
> | [`DialogDemo`](../examples/components/index.html#DialogDemo) | [How to Use Dialogs](dialog.html) | Uses a changeable label to display instructions and provide feedback. |
> | [`SplitPaneDemo`](../examples/components/index.html#SplitPaneDemo) | [How to Use Split Panes](splitpane.html) and [How to Use Lists](list.html) | Displays an image using a label inside of a scroll pane. |
> | [`SliderDemo2`](../examples/components/index.html#SliderDemo2) | [How to Use Sliders](slider.html) | Uses `JLabel` to provide labels for a slider. |
> | [`TableDialogEditDemo`](../examples/components/index.html#TableDialogEditDemo) | [How to Use Tables](table.html) | Implements a label subclass, `ColorRenderer`, to display colors in table cells. |
> | [`FormattedTextFieldDemo`](../examples/components/index.html#FormattedTextFieldDemo) | [How to Use Formatted Text Fields](formattedtextfield.html) | Has four rows, each containing a label and the formatted text field it describes. |
> | [`TextComponentDemo`](../examples/components/index.html#TextComponentDemo) | [Text Component Features](generaltext.html) | `TextComponentDemo` has an inner class (`CaretListenerLabel`) that extends `JLabel` to provide a label that listens for events, updating itself based on the events. |
> | [`ColorChooserDemo`](../examples/components/index.html#ColorChooserDemo) | [How to Use Color Choosers](colorchooser.html) | Uses an opaque label to display the currently chosen color against a fixed-color background. |

[« Previous](internalframe.html)
•
[Trail](../TOC.html)
•
[Next »](layeredpane.html)

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

**Previous page:** How to Use Internal Frames
  
**Next page:** How to Use Layered Panes




A browser with JavaScript enabled is required for this page to operate properly.