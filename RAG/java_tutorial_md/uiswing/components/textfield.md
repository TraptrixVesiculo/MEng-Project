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

[How to Use Sliders](slider.html)

[How to Use Spinners](spinner.html)

[How to Use Split Panes](splitpane.html)

[How to Use Tabbed Panes](tabbedpane.html)

[How to Use Tables](table.html)

[How to Use Text Areas](textarea.html)

How to Use Text Fields

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

[« Previous](textarea.html) • [Trail](../TOC.html) • [Next »](toolbar.html)

# How to Use Text Fields

A text field is a basic text control
that enables the user to type a small amount of text.
When the user indicates that text entry is complete
(usually by pressing Enter),
the text field fires an
[action event](../events/actionlistener.html).
If you need to obtain more than one line of input from the user,
use a
[text area](textarea.html).

The Swing API provides several classes for
components that are either varieties of text fields
or that include text fields.

|  |  |
| --- | --- |
| [`JTextField`](http://download.oracle.com/javase/7/docs/api/javax/swing/JTextField.html) What this section covers: basic text fields. | |
| `JFormattedTextField` A `JTextField` subclass that allows you to specify the legal set of characters that the user can enter. See [How to Use Formatted Text Fields](formattedtextfield.html). | |
| `JPasswordField` A `JTextField` subclass that does not show the characters that the user types. See [How to Use Password Fields](passwordfield.html). | |
| `JComboBox` Can be edited, and provides a menu of strings to choose from. See [How to Use Combo Boxes](combobox.html). | |
| `JSpinner` Combines a formatted text field with a couple of small buttons that enables the user to choose the previous or next available value. See [How to Use Spinners](spinner.html). | |

The following example displays a basic text field and a text area.
The text field is editable. The text area is not editable.
When the user presses Enter
in the text field,
the program copies the text field's
contents to the text area,
and then selects all the text in the text field.

![A snapshot of TextDemo](../../figures/uiswing/components/TextDemo.png)

Click the Launch button
to run TextDemo using
[Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp)
([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
Alternatively, to compile and run the example yourself,
consult the
[example index](../examples/components/index.html#TextDemo).

[![Launches the TextDemo application](../../images/jws-launch-button.png)](http://download.oracle.com/javase/tutorialJWS/uiswing/components/ex6/TextDemo.jnlp)

You can find the entire code for this program in
[`TextDemo.java`](../examples/components/TextDemoProject/src/components/TextDemo.java).
The following code
creates and sets up the text field:

```

textField = new JTextField(20);

```

The integer argument passed
to the `JTextField` constructor,
`20` in the example,
indicates the number of columns in the field.
This number is used along with metrics provided by
the field's current font
to calculate the field's preferred width.
It does not limit the number of characters the user
can enter.
To do that, you can either use a
[formatted text field](formattedtextfield.html)
or a
document listener,
as described in
[Text Component Features](generaltext.html).

---

**Note:** We encourage you to specify the number of columns
for each text field.
If you do not specify the number of columns or a preferred size,
then the field's preferred size changes whenever the text changes,
which can result in unwanted layout updates.

---

The next line of code
registers a `TextDemo` object
as an action listener for the text field.

```

textField.addActionListener(this);

```

The `actionPerformed` method
handles action events from the text field:

```

private final static String newline = "\n";
...
public void actionPerformed(ActionEvent evt) {
    String text = textField.getText();
    textArea.append(text + newline);
    textField.selectAll();
}

```

Notice the use of `JTextField`'s `getText`
method to retrieve the text currently contained by the text field.
The text returned by this method
does *not* include a newline character
for the Enter key that fired the action event.

You have seen how a basic text field can be used.
Because the `JTextField` class inherits from
the `JTextComponent` class,
text fields are very flexible and can be customized almost
any way you like.
For example, you can add a document listener
or a document filter
to be notified when the text changes, and
in the filter case you can
modify the text field accordingly.
Information on text components can be found in
[Text Component Features](generaltext.html).
Before customizing a `JTextField`,
however,
make sure that one of the other
[components based on text fields](#varieties)
will not do the job for you.

Often text fields are paired with
labels that describe the text fields.
See [Examples That Use Text Fields](#eg)
for pointers on creating these pairs.

### Another Example: TextFieldDemo

> The `TextFieldDemo` example
> introduces a text field and a text area.
> You can find the entire code for this program in
> [`TextFieldDemo.java`](../examples/components/TextFieldDemoProject/src/components/TextFieldDemo.java).
>
> As you type characters in the text field the program searches for the typed text
> in the text area. If the entry is found it gets highlighted.
> If the program fails to find the entry then
> the text field's background becomes pink.
> A status bar below the text area displays a message
> whether text is found or not.
> The Escape key is used to start a new search or to finish the current one.
> Here is a picture of the `TextFieldDemo` application.
>
> ![A snapshot of TextFieldDemo](../../figures/uiswing/components/TextFieldDemo.png)
>
> Click the Launch button
> ro run TextFieldDemo using
> [Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp)
> ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
> Alternatively, to compile and run the example yourself,
> consult the [example index](../examples/components/index.html#TextFieldDemo).
>
> [![Launches the TextFieldDemo Application](../../images/jws-launch-button.png)](http://download.oracle.com/javase/tutorialJWS/uiswing/components/ex6/TextFieldDemo.jnlp)
>
> To highlight text, this example uses
> a highlighter and a painter.
> The code below creates and sets up the highlighter and the painter
> for the text area.
>
> ```
>
> final Highlighter hilit;
> final Highlighter.HighlightPainter painter;
> ...
> hilit = new DefaultHighlighter();
> painter = new DefaultHighlighter.DefaultHighlightPainter(HILIT_COLOR);
> textArea.setHighlighter(hilit);
>
> ```
>
> This code adds a document listener to the text field's document.
>
> ```
>
> entry.getDocument().addDocumentListener(this);
>
> ```
>
> Document listener's `insertUpdate`
> and `removeUpdate` methods call the `search` method,
> which not only performs a search in the text area
> but also handles highlighting.
> The following code highlights the found text,
> sets the caret to the end of the found match,
> sets the default background for the text field,
> and displays a message in the status bar.
>
> ```
>
> hilit.addHighlight(index, end, painter);
> textArea.setCaretPosition(end);
> entry.setBackground(entryBg);
> message("'" + s + "' found. Press ESC to end search");
>
> ```
>
> The status bar is a `JLabel` object.
> The code below shows how the `message` method is implemented.
>
> ```
>
> private JLabel status;
> ...
> void message(String msg) {
>     status.setText(msg);
> }
>
> ```
>
> If there is no match in the text area, the following code
> changes the text field's background to pink
> and displays a proper information message.
>
> ```
>
> entry.setBackground(ERROR_COLOR);
> message("'" + s + "' not found. Press ESC to start a new search");
>
> ```
>
> The `CancelAction` class is responsible
> for handling the Escape key as follows.
>
> ```
>
>    class CancelAction extends AbstractAction {
>        public void actionPerformed(ActionEvent ev) {
>                hilit.removeAllHighlights();
>                entry.setText("");
>                entry.setBackground(entryBg);
>            }
>    }
>
> ```

### The Text Field API

> The following tables list the commonly used
> `JTextField`
> constructors and methods.
> Other methods you are likely to call
> are defined in the `JTextComponent` class.
> Refer to
> [The Text Component API](textapi.html).
>
> You might also invoke methods on a
> text field
> inherited from the text field's other ancestors,
> such as `setPreferredSize`,
> `setForeground`,
> `setBackground`,
> `setFont`, and so on.
> See
> [The JComponent Class](jcomponent.html)
> for tables of commonly used inherited methods.
>
> The API for using text fields
> falls into these categories:
>
> * [Setting or Obtaining the Field's Contents](#contents)* [Fine Tuning the Field's Appearance](#looks)* [Implementing the Field's Functionality](#function)
>
> **Setting or Obtaining the Field's Contents**
>
> | Method or Constructor | Purpose |
> | [JTextField()](http://download.oracle.com/javase/7/docs/api/javax/swing/JTextField.html#JTextField())   [JTextField(String)](http://download.oracle.com/javase/7/docs/api/javax/swing/JTextField.html#JTextField(java.lang.String))   [JTextField(String, int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JTextField.html#JTextField(java.lang.String, int))   [JTextField(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JTextField.html#JTextField(int)) | Creates a text field. When present, the `int` argument specifies the desired width in columns. The `String` argument contains the field's initial text. |
> | [void setText(String)](http://download.oracle.com/javase/7/docs/api/javax/swing/text/JTextComponent.html#setText(java.lang.String))   [String getText()](http://download.oracle.com/javase/7/docs/api/javax/swing/text/JTextComponent.html#getText())  *(defined in `JTextComponent`)* | Sets or obtains the text displayed by the text field. |
>
> **Fine Tuning the Field's Appearance**
>
> | Method | Purpose |
> | [void setEditable(boolean)](http://download.oracle.com/javase/7/docs/api/javax/swing/text/JTextComponent.html#setEditable(boolean))   [boolean isEditable()](http://download.oracle.com/javase/7/docs/api/javax/swing/text/JTextComponent.html#isEditable())  *(defined in `JTextComponent`)* | Sets or indicates whether the user can edit the text in the text field. |
> | [void setColumns(int);](http://download.oracle.com/javase/7/docs/api/javax/swing/JTextField.html#setColumns(int))   [int getColumns()](http://download.oracle.com/javase/7/docs/api/javax/swing/JTextField.html#getColumns()) | Sets or obtains the number of columns displayed by the text field. This is really just a hint for computing the field's preferred width. |
> | [void setHorizontalAlignment(int);](http://download.oracle.com/javase/7/docs/api/javax/swing/JTextField.html#setHorizontalAlignment(int))   [int getHorizontalAlignment()](http://download.oracle.com/javase/7/docs/api/javax/swing/JTextField.html#getHorizontalAlignment()) | Sets or obtains how the text is aligned horizontally within its area. You can use `JTextField.LEADING`, `JTextField.CENTER`, and `JTextField.TRAILING` for arguments. |
>
> **Implementing the Field's Functionality**
>
> | Method | Purpose |
> | [void addActionListener(ActionListener)](http://download.oracle.com/javase/7/docs/api/javax/swing/JTextField.html#addActionListener(java.awt.event.ActionListener))   [void removeActionListener(ActionListener)](http://download.oracle.com/javase/7/docs/api/javax/swing/JTextField.html#removeActionListener(java.awt.event.ActionListener)) | Adds or removes an action listener. |
> | [void selectAll()](http://download.oracle.com/javase/7/docs/api/javax/swing/text/JTextComponent.html#selectAll())  *(defined in `JTextComponent`)* | Selects all characters in the text field. |

### Examples That Use Text Fields

> This table shows a few of the examples that use text fields
> and points to where those examples are described.
> For examples of code that are similar among all varieties of text fields
> such as dealing with layout,
> look at the example lists for related components such as
> [formatted text fields](formattedtextfield.html#eg) and
> [spinners](spinner.html#eg).
>
> | Example | Where Described | Notes |
> | --- | --- | --- |
> | [TextDemo](../examples/components/index.html#TextDemo) | This section | An application that uses a basic text field with an action listener. |
> | [TextFieldDemo](../examples/components/index.html#TextFieldDemo) | This section | An application that uses a text field and a text area. A search is made in the text area to find an entry from the text field. |
> | [DialogDemo](../examples/components/index.html#DialogDemo) | [How to Make Dialogs](dialog.html) | `CustomDialog.java` includes a text field whose value is checked. You can bring up the dialog by clicking the More Dialogs tab, selecting the Input-validating dialog option, and then clicking the Show it! button. |
> | [TextSamplerDemo](../examples/components/index.html#TextSamplerDemo) | [Using Text Components](text.html) | Lays out label-text field pairs using a `GridBagLayout` and a convenience method:  ```  addLabelTextRows(JLabel[] labels, 		 JTextField[] textFields, 		 GridBagLayout gridbag, 		 Container container) ```  | [TextInputDemo](../examples/components/index.html#TextInputDemo) | [How to Use Formatted Text Fields](formattedtextfield.html) | Lays out label-text field pairs using a `SpringLayout` and a `SpringUtilities` convenience method:  ```  makeCompactGrid(Container parent,                 int rows, int cols,                 int initialX, int initialY,                 int xPad, int yPad) ``` | |

[« Previous](textarea.html)
•
[Trail](../TOC.html)
•
[Next »](toolbar.html)

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

**Previous page:** How to Use Text Areas
  
**Next page:** How to Use Tool Bars




A browser with JavaScript enabled is required for this page to operate properly.