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

How to Use Color Choosers

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

[How to Use Borders](border.html)

[Solving Common Component Problems](problems.html)

[Home Page](../../index.html)
>
[Creating a GUI With JFC/Swing](../index.html)
>
[Using Swing Components](index.html)

[« Previous](buttongroup.html) • [Trail](../TOC.html) • [Next »](combobox.html)

# How to Use Color Choosers

Use the
[`JColorChooser`](http://download.oracle.com/javase/7/docs/api/javax/swing/JColorChooser.html) class to provide users with a palette of colors to choose from.
A color chooser is a component that you can place
anywhere within your program GUI.
The `JColorChooser` API also makes it easy
to bring up a [dialog](dialog.html)
(modal or not) that contains a color chooser.

Here is a picture
of an application that uses a color chooser to set
the text color in a banner:

![A snapshot of ColorChooserDemo, which contains a standard color chooser.](../../figures/uiswing/components/ColorChooserDemoMetal.png)

---

**Try this:**

* Click the Launch button to run the ColorChooser Demo using
  [Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp) ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
  Alternatively, to compile and run the example yourself,
  consult the
  [example index](../examples/components/index.html#ColorChooserDemo).

  [![Launches the ButtonDemo example](../../images/jws-launch-button.png)](http://download.oracle.com/javase/tutorialJWS/uiswing/components/ex6/ColorChooserDemo.jnlp)

---


The source code for the program is in
[`ColorChooserDemo.java`](../examples/components/ColorChooserDemoProject/src/components/ColorChooserDemo.java).

The color chooser consists of everything within the
box labeled **Choose Text Color**.
This is what a standard color chooser looks like
in the Java Look & Feel.
It contains two parts, a tabbed pane and a preview panel.
The three tabs in the tabbed pane
select *chooser panels*.
The *preview panel*
below the tabbed pane
displays the currently selected color.

Here is the code from the example that creates
a `JColorChooser` instance
and adds it to a container:

```

public class ColorChooserDemo extends JPanel ... {
    public ColorChooserDemo() {
        super(new BorderLayout());
        banner = new JLabel("Welcome to the Tutorial Zone!",
                            JLabel.CENTER);
        banner.setForeground(Color.yellow);
        . . .
        tcc = new JColorChooser(banner.getForeground());
        . . .
        add(tcc, BorderLayout.PAGE_END);
    }

```

The `JColorChooser` constructor in the previous code snippet
takes a `Color` argument,
which specifies the chooser's initially selected color.
If you do not specify the initial color,
then the color chooser displays
`Color.white`.
See the
[`Color` API documentation](http://download.oracle.com/javase/7/docs/api/java/awt/Color.html) for a list of color constants you can use.

A color chooser uses an instance of
[`ColorSelectionModel`](http://download.oracle.com/javase/7/docs/api/javax/swing/colorchooser/ColorSelectionModel.html) to contain and manage the current selection.
The color selection model fires a change event
whenever the user changes the color in the color chooser.
The example program registers a change listener with the
color selection model so that it can update the
banner at the top of the window.
The following code registers and implements the change listener:

```

tcc.getSelectionModel().addChangeListener(this);
. . .
public void stateChanged(ChangeEvent e) {
    Color newColor = tcc.getColor();
    banner.setForeground(newColor);
}

```

See
[How to Write a Change Listener](../events/changelistener.html)
for general information about change listeners and change events.

A basic color chooser,
like the one used in the example program,
is sufficient for many programs.
However,
the color chooser API allows you to customize a color chooser
by providing it with a preview panel of your own design,
by adding your own chooser panels to it, or
by removing existing chooser panels from the color chooser.
Additionally, the `JColorChooser` class provides two
methods that make it easy to use a color chooser within a dialog.

The rest of this section discusses these topics:

* [Another Example: ColorChooserDemo2](#advancedexample)* [Showing a Color Chooser in a Dialog](#dialog)* [Removing or Replacing the Preview Panel](#previewpanel)* [Creating a Custom Chooser Panel](#chooserpanel)* [The Color Chooser API](#api)* [Examples that Use Color Choosers](#eg)

### Another Example: ColorChooserDemo2
> Now let's turn our attention to
> [ColorChooserDemo2](../examples/components/index.html#ColorChooserDemo2),
> a modified version of the previous demo program that
> uses more of the `JColorChooser` API.
>
> ---
>
> **Try this:**
>
> * Click the Launch button to run the ColorChooser Demo using
>   [Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp) ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
>   Alternatively, to compile and run the example yourself,
>   consult the
>   [example index](../examples/components/index.html#ColorChooserDemo2).
>
>   [![Launches the ButtonDemo example](../../images/jws-launch-button.png)](http://download.oracle.com/javase/tutorialJWS/uiswing/components/ex6/ColorChooserDemo2.jnlp)
>
> ---
>
>
> Here is a picture of ColorChooserDemo2:
>
> ![A snapshot of ColorChooserDemo, which contains a custom color chooser.](../../figures/uiswing/components/ColorChooserDemo2Metal.png)
>
> This program customizes the banner
> text color chooser in these ways:
>
> * Removes the preview panel* Removes all of the default chooser panels* Adds a custom chooser panel
>
> [Removing or Replacing the Preview Panel](#previewpanel)
> covers the first customization.
> [Creating a Custom Chooser Panel](#chooserpanel)
> discusses the last two.
>
> This program also adds a button that brings up
> a color chooser in a dialog,
> which you can use to set the banner background color.

### Showing a Color Chooser in a Dialog
> The `JColorChooser` class provides
> two class methods to make it easy to use a color chooser in a
> dialog.
> ColorChooserDemo2 uses one of these methods,
> `showDialog`,
> to display the background color chooser when the user
> clicks the **Show Color Chooser...** button.
> Here is the single line of code from the example
> that brings up the background color chooser in a dialog:
>
> ```
>
> Color newColor = JColorChooser.showDialog(
>                      ColorChooserDemo2.this,
>                      "Choose Background Color",
>                      banner.getBackground());
>
> ```
>
> The first argument is the parent for the dialog,
> the second is the dialog title, and
> the third is the initially selected color.
>
> The dialog disappears under three conditions:
> the user chooses a color and clicks the **OK** button,
> the user cancels the operation with the **Cancel** button,
> or the user dismisses the dialog with a frame control.
> If the user chooses a color,
> the `showDialog` method returns the new color.
> If the user cancels the operation or dismisses the window,
> the method returns `null`.
> Here is the code from the example that updates
> the banner background color
> according to the value returned by `showDialog`:
>
> ```
>
> if (newColor != null) {
>     banner.setBackground(newColor);
> }
>
> ```
>
> The dialog created by `showDialog` is modal.
> If you want a non-modal dialog,
> you can use `JColorChooser`'s
> `createDialog` method to create the dialog.
> This method also lets you specify action listeners for the
> **OK** and **Cancel**
> buttons in the dialog window.
> Use `JDialog`'s `show` method
> to display the dialog created by this method.
> For an example that uses this method, see
> [Specifying Other Editors](table.html#editor)
> in the
> [How to Use Tables](table.html) section.

### Removing or Replacing the Preview Panel
> By default, the color chooser displays a preview panel.
> ColorChooserDemo2
> removes the text color chooser's
> preview panel with this line of code:
>
> ```
>
> tcc.setPreviewPanel(new JPanel());
>
> ```
>
> This effectively removes the preview panel because
> a plain `JPanel` has no size and no default view.
> To set the preview panel back to the default,
> use `null` as the argument to `setPreviewPanel`.
>
> To provide a custom preview panel,
> you also use `setPreviewPanel`.
> The component you pass into the method should
> inherit from `JComponent`,
> specify a reasonable size,
> and provide a customized view of the current color.
> To get notified when the user changes the color
> in the color chooser,
> the preview panel must register
> as a change listener on the color chooser's color selection model
> as described [previously](#changelistener).

### Creating a Custom Chooser Panel
> The default color chooser provides three chooser panels:
>
> * Swatches — for choosing a color from a collection of swatches.* HSB — for choosing a color using the Hue-Saturation-Brightness
>     color model.* RGB — for choosing a color using the Red-Green-Blue
>       color model.
>
> You can extend the default color chooser
> by adding chooser panels of your own design with
> `addChooserPanel`,
> or you can limit it by removing chooser panels
> with `removeChooserPanel`.
>
> If you want to remove all of the default chooser panels
> and add one or more of your own, you can do this with a single
> call to `setChooserPanels`.
> ColorChooserDemo2
> uses this method to replace the default chooser panels
> with an instance of
> [`CrayonPanel`](../examples/components/ColorChooserDemo2Project/src/components/CrayonPanel.java),
> a custom chooser panel.
> Here is the call to `setChooserPanels` from
> that example:
>
> ```
>
> //Override the chooser panels with our own.
> AbstractColorChooserPanel panels[] = { new CrayonPanel() };
> tcc.setChooserPanels(panels);
>
> ```
>
> The code is straighforward:
> it creates an array containing the `CrayonPanel`.
> Next the code calls `setChooserPanels` to
> set the contents of the array as the color chooser's
> chooser panels.
>
> `CrayonPanel` is a subclass of
> [`AbstractColorChooserPanel`](http://download.oracle.com/javase/7/docs/api/javax/swing/colorchooser/AbstractColorChooserPanel.html) and overrides the five abstract methods defined in its superclass:
>
> **`void buildChooser()`**: Creates the GUI that comprises the chooser panel. The example creates four toggle buttons — one for each crayon — and adds them to the chooser panel. **`void updateChooser()`**: This method is called whenever the chooser panel is displayed. The implementation of this method selects the toggle button that represents the currently selected color. ``` public void updateChooser() { Color color = getColorFromModel(); if (Color.red.equals(color)) { redCrayon.setSelected(true); } else if (Color.yellow.equals(color)) { yellowCrayon.setSelected(true); } else if (Color.green.equals(color)) { greenCrayon.setSelected(true); } else if (Color.blue.equals(color)) { blueCrayon.setSelected(true); } } ``` **`String getDisplayName()`**: Returns the display name of the chooser panel. The name is used on the tab for the chooser panel. Here is the example `getDisplayName` method: ``` public String getDisplayName() { return "Crayons"; } ``` **`Icon getSmallDisplayIcon()`**: Returns a small icon to represent this chooser panel. This is currently unused. Future versions of the color chooser might use this icon or the large one to represent this chooser panel in the display. The example implementation of this method returns `null`. **`Icon getLargeDisplayIcon()`**: Returns a large icon to represent this chooser panel. This is currently unused. Future versions of the color chooser might use this icon or the small one to represent this chooser panel in the display. The example implementation of this method returns `null`.

### The Color Chooser API

> The following tables list the commonly used
> `JColorChooser` constructors and methods.
> Other methods you might call
> are listed in the API tables in
> [The JComponent Class](jcomponent.html).
> The API for using color choosers falls into these categories:
>
> * [Creating and Displaying the Color Chooser](#creating)* [Customizing the Color Chooser GUI](#customizing)* [Setting or Getting the Current Color](#selection)
>
> Creating and Displaying the Color Chooser
>
> | Method or Constructor | Purpose |
> | [JColorChooser()](http://download.oracle.com/javase/7/docs/api/javax/swing/JColorChooser.html#JColorChooser())   [JColorChooser(Color)](http://download.oracle.com/javase/7/docs/api/javax/swing/JColorChooser.html#JColorChooser(java.awt.Color))   [JColorChooser(ColorSelectionModel)](http://download.oracle.com/javase/7/docs/api/javax/swing/JColorChooser.html#JColorChooser(javax.swing.colorchooser.ColorSelectionModel)) | Create a color chooser. The default constructor creates a color chooser with an initial color of `Color.white`. Use the second constructor to specify a different initial color. The `ColorSelectionModel` argument, when present, provides the color chooser with a color selection model. |
> | [Color showDialog(Component, String, Color)](http://download.oracle.com/javase/7/docs/api/javax/swing/JColorChooser.html#showDialog(java.awt.Component, java.lang.String, java.awt.Color)) | Create and show a color chooser in a modal dialog. The `Component` argument is the parent of the dialog, the `String` argument specifies the dialog title, and the `Color` argument specifies the chooser's initial color. |
> | [JDialog createDialog(Component, String,  boolean, JColorChooser, ActionListener,  ActionListener)](http://download.oracle.com/javase/7/docs/api/javax/swing/JColorChooser.html#createDialog(java.awt.Component, java.lang.String, boolean, javax.swing.JColorChooser, java.awt.event.ActionListener, java.awt.event.ActionListener)) | Create a dialog for the specified color chooser. As with `showDialog`, the `Component` argument is the parent of the dialog and the `String` argument specifies the dialog title. The other arguments are as follows: the `boolean` specifies whether the dialog is modal, the `JColorChooser` is the color chooser to display in the dialog, the first `ActionListener` is for the **OK** button, and the second is for the **Cancel** button. |
>
> Customizing the Color Chooser's GUI
>
> | Method | Purpose |
> | [void setPreviewPanel(JComponent)](http://download.oracle.com/javase/7/docs/api/javax/swing/JColorChooser.html#setPreviewPanel(javax.swing.JComponent))   [JComponent getPreviewPanel()](http://download.oracle.com/javase/7/docs/api/javax/swing/JColorChooser.html#getPreviewPanel()) | Set or get the component used to preview the color selection. To remove the preview panel, use `new JPanel()` as an argument. To specify the default preview panel, use `null`. |
> | [void setChooserPanels(AbstractColorChooserPanel[])](http://download.oracle.com/javase/7/docs/api/javax/swing/JColorChooser.html#setChooserPanels(javax.swing.colorchooser.AbstractColorChooserPanel[]))   [AbstractColorChooserPanel[] getChooserPanels()](http://download.oracle.com/javase/7/docs/api/javax/swing/JColorChooser.html#getChooserPanels()) | Set or get the chooser panels in the color chooser. |
> | [void addChooserPanel(AbstractColorChooserPanel)](http://download.oracle.com/javase/7/docs/api/javax/swing/JColorChooser.html#addChooserPanel(javax.swing.colorchooser.AbstractColorChooserPanel))   [AbstractColorChooserPanel removeChooserPanel(AbstractColorChooserPanel)](http://download.oracle.com/javase/7/docs/api/javax/swing/JColorChooser.html#removeChooserPanel(javax.swing.colorchooser.AbstractColorChooserPanel)) | Add a chooser panel to the color chooser or remove a chooser panel from it. |
> | [void setDragEnabled(boolean)](http://download.oracle.com/javase/7/docs/api/javax/swing/JColorChooser.html#setDragEnabled(boolean))   [boolean getDragEnabled()](http://download.oracle.com/javase/7/docs/api/javax/swing/JColorChooser.html#getDragEnabled()) | Set or get the `dragEnabled` property, which must be true to enable drag handling on this component. The default value is false. See [Drag and Drop and Data Transfer](../dnd/index.html) for more details. |
>
> Setting or Getting the Current Color
>
> | Method | Purpose |
> | [void setColor(Color)](http://download.oracle.com/javase/7/docs/api/javax/swing/JColorChooser.html#setColor(java.awt.Color))   [void setColor(int, int, int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JColorChooser.html#setColor(int, int, int))   [void setColor(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JColorChooser.html#setColor(int))   [Color getColor()](http://download.oracle.com/javase/7/docs/api/javax/swing/JColorChooser.html#getColor()) | Set or get the currently selected color. The three integer version of the `setColor` method interprets the three integers together as an RGB color. The single integer version of the `setColor` method divides the integer into four 8-bit bytes and interprets the integer as an RGB color as follows: How color chooser interprets an int as an RGB value. |
> | [void setSelectionModel(ColorSelectionModel)](http://download.oracle.com/javase/7/docs/api/javax/swing/JColorChooser.html#setSelectionModel(javax.swing.colorchooser.ColorSelectionModel))   [ColorSelectionModel getSelectionModel()](http://download.oracle.com/javase/7/docs/api/javax/swing/JColorChooser.html#getSelectionModel()) | Set or get the selection model for the color chooser. This object contains the current selection and fires change events to registered listeners whenever the selection changes. |

### Examples that Use Color Choosers

> This table shows the examples that use `JColorChooser`
> and where those examples are described.
>
> | Example | Where Described | Notes |
> | --- | --- | --- |
> | [ColorChooserDemo](../examples/components/index.html#ColorChooserDemo) | This section | Uses a standard color chooser. |
> | [ColorChooserDemo2](../examples/components/index.html#ColorChooserDemo2) | This section | Uses one customized color chooser and one standard color chooser in a dialog created with `showDialog`. |
> | [TableDialogEditDemo](../examples/components/index.html#TableDialogEditDemo) | [How to Use Tables](table.html) | Shows how to use a color chooser as a custom cell editor in a table. The color chooser used by this example is created with `createDialog`. |
> | [BasicDnD](../misc/../examples/dnd/index.html#BasicDnD) | [Introduction to DnD](../dnd/intro.html) | Uses a color chooser that is not in a dialog; demonstrates default drag-and-drop capabilities of Swing components, including color choosers. |

[« Previous](buttongroup.html)
•
[Trail](../TOC.html)
•
[Next »](combobox.html)

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

**Previous page:** How to Use the ButtonGroup Component
  
**Next page:** How to Use Combo Boxes




A browser with JavaScript enabled is required for this page to operate properly.