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

How to Use Text Areas

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

[« Previous](table.html) • [Trail](../TOC.html) • [Next »](textfield.html)

# How to Use Text Areas

The
[`JTextArea`](http://download.oracle.com/javase/7/docs/api/javax/swing/JTextArea.html) class
provides a component that
displays multiple lines of text and
optionally allows the user to edit the text.
If you need to obtain only one line of input from the user,
you should use a
[text field](textfield.html).
If you want the text area
to display its text using multiple fonts or other styles,
you should use an
[editor pane or text pane](editorpane.html).
If the displayed text
has a limited length and is never edited by the user,
use a
[label](label.html).

Many of the Tutorial's examples use uneditable text areas
to display program output.
Here is a picture of an example called `TextDemo`
that enables you to type text using a text field
(at the top)
and then appends the typed text to a text area
(underneath).

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
creates and initializes the text area:

```

textArea = new JTextArea(5, 20);
JScrollPane scrollPane = new JScrollPane(textArea); 
textArea.setEditable(false);

```

The two arguments to the `JTextArea` constructor
are hints as to the number of rows and columns, respectively,
that the text area should display.
The scroll pane that contains the text area
pays attention to these hints
when determining how big the scroll pane should be.

Without the creation of the scroll pane,
the text area would not automatically scroll.
The `JScrollPane` constructor
shown in the preceding snippet
sets up the text area for viewing in a scroll pane,
and specifies that the scroll pane's scroll bars
should be visible when needed.
See [How to Use Scroll Panes](scrollpane.html)
if you want further information.

Text areas are editable by default.
The code `setEditable(false)`
makes the text area uneditable.
It is still selectable
and the user can copy data from it,
but the user cannot change the text area's contents directly.

The following code adds text to the text area.
Note that the text system uses the '\n' character
internally to represent newlines;
for details,
see the API documentation for
[`DefaultEditorKit`](http://download.oracle.com/javase/7/docs/api/javax/swing/text/DefaultEditorKit.html).

```

private final static String newline = "\n";
...
textArea.append(text + newline);

```

Unless the user has moved the caret (insertion point)
by clicking or dragging in the text area,
the text area automatically scrolls so that the appended text is visible.
You can force the text area to scroll to the bottom
by moving the caret to the end of the text area
after the call to `append`:

```

textArea.setCaretPosition(textArea.getDocument().getLength());

```

### Customizing Text Areas

> You can customize text areas in several ways.
> For example, although a given text area
> can display text in only one font and color,
> you can
> set which font and color it uses.
> This customization option can be performed on any component.
> You can also determine how the text area
> wraps lines and the number of characters per tab.
> Finally, you can use the methods that the `JTextArea` class inherits
> from the `JTextComponent` class
> to set properties such as the caret,
> support for dragging,
> or color selection.
>
> The following code
> taken from
> [`TextSamplerDemo.java`](../examples/components/TextSamplerDemoProject/src/components/TextSamplerDemo.java) demonstrates
> initializing an editable text area.
> The text area uses the specified italic font,
> and wraps lines between words.
>
> ```
>
> JTextArea textArea = new JTextArea(
>     "This is an editable JTextArea. " +
>     "A text area is a \"plain\" text component, " +
>     "which means that although it can display text " +
>     "in any font, all of the text is in the same font."
> );
> textArea.setFont(new Font("Serif", Font.ITALIC, 16));
> textArea.setLineWrap(true);
> textArea.setWrapStyleWord(true);
>
> ```
>
> By default, a text area does not wrap lines
> that are too long for the display area.
> Instead, it uses one line
> for all the text between newline characters and
> —
> if the text area is within a
> [scroll pane](scrollpane.html) —
> allows itself to be scrolled horizontally.
> This example turns line wrapping on with
> a call to the `setLineWrap` method
> and then calls the `setWrapStyleWord` method
> to indicate that the text area should wrap lines
> at word boundaries rather than at character
> boundaries.
>
> To provide scrolling capability, the example
> puts the text area in a scroll pane.
>
> ```
>
> JScrollPane areaScrollPane = new JScrollPane(textArea);
> areaScrollPane.setVerticalScrollBarPolicy(
> 		JScrollPane.VERTICAL_SCROLLBAR_ALWAYS);
> areaScrollPane.setPreferredSize(new Dimension(250, 250));
>
> ```
>
> You might have noticed
> that the `JTextArea` constructor
> used in this example
> does not specify the number of rows or columns.
> Instead, the code limits the size of the text area
> by setting the scroll pane's preferred size.

### Another Example: TextAreaDemo

> The `TextAreaDemo` example
> introduces an editable text area with a special feature —
> a word completion function.
> As the user types in words, the program suggests hints to complete the word
> whenever the program's vocabulary
> contains a word that starts with what has been typed.
> Here is a picture of the `TextAreaDemo` application.
>
> ![A snapshot of TextAreaDemo](../../figures/uiswing/components/TextAreaDemo.png)
>
> Click the Launch button
> to run TextAreaDemo using
> [Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp)
> ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
> Alternatively, to compile and run the example yourself,
> consult the [example index](../examples/components/index.html#TextAreaDemo).
>
> [![Launches the TextAreaDemo Application](../../images/jws-launch-button.png)](http://download.oracle.com/javase/tutorialJWS/uiswing/components/ex6/TextAreaDemo.jnlp)
>
> You can find the entire code for this program in
> [`TextAreaDemo.java`](../examples/components/TextAreaDemoProject/src/components/TextAreaDemo.java).
>
> This example provides a scrolling capacity for the text area
> with the default scroll bar policy.
> By default, the vertical scroll bar only appears
> when the display area is entirely filled with text
> and there is no room to append new words.
> You can provide a scroll pane of this type with the following code:
>
> ```
>
>   textArea.setWrapStyleWord(true);
>   jScrollPane1 = new JScrollPane(textArea);
>
> ```
>
> As mentioned above, the text area is editable.
> You can play with the text area by typing and pasting text,
> or by deleting some parts of text or the entire content.
> Also try using standard key bindings for editing text within the text area.
>
> Now explore how the word completion function is implemented.
> Type in a word like "Swing" or "special".
> As soon as you have typed "sw" the program shows
> a possible completion "ing" highlighted in light-blue.
> Press Enter to accept the completion or continue typing.
>
> The following code adds a document listener to the text area's document:
>
> ```
>
>   textArea.getDocument().addDocumentListener(this);
>
> ```
>
> When you started typing a word, the `insertUpdate` method
> checks whether the program's vocabulary contains the typed prefix.
> Once a completion for the prefix is found, a call to the `invokeLater`
> method submits a task for changing the document later.
> It is important to remember
> that you cannot modify the document
> from within the document event notification,
> otherwise you will get an exception.
> Examine the following code below.
>
> ```
>
>   String prefix = content.substring(w + 1).toLowerCase();
>   int n = Collections.binarySearch(words, prefix);
>   if (n < 0 && -n <= words.size()) {
>       String match = words.get(-n - 1);
>       if (match.startsWith(prefix)) {
>                 // A completion is found
>                 String completion = match.substring(pos - w);
>                 // We cannot modify Document from within notification,
>                 // so we submit a task that does the change later
>                 SwingUtilities.invokeLater(
>                         new CompletionTask(completion, pos + 1));
>       }
>   } else {
>       // Nothing found
>       mode = Mode.INSERT;
>   }
>
> ```
>
> The code shown in bold illustrates how the selection is created.
> The caret is first set to the end of the complete word,
> then moved back to a position after the last character typed.
> The `moveCaretPosition` method not only moves the caret
> to a new position but also selects the text between the two positions.
> The completion task is implemented with the following code:
>
> ```
>
>   private class CompletionTask implements Runnable {
>         String completion;
>         int position;
>         
>         CompletionTask(String completion, int position) {
>             this.completion = completion;
>             this.position = position;
>         }
>         
>         public void run() {
>             textArea.insert(completion, position);
>             textArea.setCaretPosition(position + completion.length());
>             textArea.moveCaretPosition(position);
>             mode = Mode.COMPLETION;
>         }
>     }
>
> ```

### The Text Area API

> The following tables list the commonly used
> `JTextArea`
> constructors and methods.
> Other methods you are likely to call
> are defined in `JTextComponent`,
> and listed in
> [The Text Component API](textapi.html).
>
> You might also invoke methods on a
> text area
> that it inherits from its other ancestors,
> such as `setPreferredSize`,
> `setForeground`,
> `setBackground`,
> `setFont`, and so on.
> See
> [The JComponent Class](jcomponent.html)
> for tables of commonly used inherited methods.
>
> The API for using text areas
> includes the following categories:
>
> * [Setting or Obtaining Contents](#contents)* [Fine Tuning Appearance](#looks)* [Implementing Functionality](#function)
>
> **Setting or Obtaining Contents**
>
> | Method or Constructor | Purpose |
> | [JTextArea()](http://download.oracle.com/javase/7/docs/api/javax/swing/JTextArea.html#JTextArea())   [JTextArea(String)](http://download.oracle.com/javase/7/docs/api/javax/swing/JTextArea.html#JTextArea(java.lang.String))   [JTextArea(String, int, int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JTextArea.html#JTextArea(java.lang.String, int, int))   [JTextArea(int, int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JTextArea.html#JTextArea(int, int)) | Creates a text area. When present, the `String` argument contains the initial text. The `int` arguments specify the desired width in columns and height in rows, respectively. |
> | [void setText(String)](http://download.oracle.com/javase/7/docs/api/javax/swing/text/JTextComponent.html#setText(java.lang.String))   [String getText()](http://download.oracle.com/javase/7/docs/api/javax/swing/text/JTextComponent.html#getText())  *(defined in `JTextComponent`)* | Sets or obtains the text displayed by the text area. |
>
> **Fine Tuning the Text Area's Appearance**
>
> | Method | Purpose |
> | [void setEditable(boolean)](http://download.oracle.com/javase/7/docs/api/javax/swing/text/JTextComponent.html#setEditable(boolean))   [boolean isEditable()](http://download.oracle.com/javase/7/docs/api/javax/swing/text/JTextComponent.html#isEditable())  *(defined in `JTextComponent`)* | Sets or indicates whether the user can edit the text in the text area. |
> | [void setColumns(int);](http://download.oracle.com/javase/7/docs/api/javax/swing/JTextArea.html#setColumns(int))   [int getColumns()](http://download.oracle.com/javase/7/docs/api/javax/swing/JTextArea.html#getColumns()) | Sets or obtains the number of columns displayed by the text area. This is really just a hint for computing the area's preferred width. |
> | [void setRows(int);](http://download.oracle.com/javase/7/docs/api/javax/swing/JTextArea.html#setRows(int))   [int getRows()](http://download.oracle.com/javase/7/docs/api/javax/swing/JTextArea.html#getRows()) | Sets or obtains the number of rows displayed by the text area. This is a hint for computing the area's preferred height. |
> | [int setTabSize(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JTextArea.html#setTabSize(int)) | Sets the number of characters a tab is equivalent to. |
> | [int setLineWrap(boolean)](http://download.oracle.com/javase/7/docs/api/javax/swing/JTextArea.html#setLineWrap(boolean)) | Sets whether lines are wrapped if they are too long to fit within the allocated width. By default this property is false and lines are not wrapped. |
> | [int setWrapStyleWord(boolean)](http://download.oracle.com/javase/7/docs/api/javax/swing/JTextArea.html#setWrapStyleWord(boolean)) | Sets whether lines can be wrapped at white space (word boundaries) or at any character. By default this property is false, and lines can be wrapped (if line wrapping is turned on) at any character. |
>
> **Implementing the Text Area's Functionality**
>
> | Method | Purpose |
> | [void selectAll()](http://download.oracle.com/javase/7/docs/api/javax/swing/text/JTextComponent.html#selectAll())  *(defined in `JTextComponent`)* | Selects all characters in the text area. |
> | [void append(String)](http://download.oracle.com/javase/7/docs/api/javax/swing/JTextArea.html#append(java.lang.String)) | Adds the specified text to the end of the text area. |
> | [void insert(String, int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JTextArea.html#insert(java.lang.String, int)) | Inserts the specified text at the specified position. |
> | [void replaceRange(String, int, int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JTextArea.html#replaceRange(java.lang.String, int, int)) | Replaces the text between the indicated positions with the specified string. |
> | [int getLineCount()](http://download.oracle.com/javase/7/docs/api/javax/swing/JTextArea.html#getLineCount())  [int getLineOfOffset(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JTextArea.html#getLineOfOffset(int))  [int getLineStartOffset(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JTextArea.html#getLineStartOffset(int))  [int getLineEndOffset(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JTextArea.html#getLineEndOffset(int)) | Utilities for finding a line number or the position of the beginning or end of the specified line. |

### Examples That Use Text Areas

> This table lists examples that use text areas
> and points to where
> those examples are described.
>
> | Example | Where Described | Notes |
> | --- | --- | --- |
> | [TextDemo](../examples/components/index.html#TextDemo) | This section | An application that appends user-entered text to a text area. |
> | [TextAreaDemo](../examples/components/index.html#TextAreaDemo) | This section | An application that has a text area with a word completion function. |
> | [TextSamplerDemo](../examples/components/index.html#TextSamplerDemo) | [Using Text Components](text.html) | Uses one of each Swing text components. |
> | [HtmlDemo](../examples/components/index.html#HtmlDemo) | [How to Use HTML in Swing Components](html.html) | A text area that enables the user to type HTML code to be displayed in a label. |
> | [BasicDnD](../examples/dnd/index.html#BasicDnD) | [Introduction to DnD](../dnd/intro.html) | Demonstrates built-in drag-and-drop functionality of several Swing components, including text areas. |
> | [FocusConceptsDemo](../examples/misc/index.html#FocusConceptsDemo) | [How to Use the Focus Subsystem](../misc/focus.html) | Demonstrates how focus works using a few components that include a text area. |

[« Previous](table.html)
•
[Trail](../TOC.html)
•
[Next »](textfield.html)

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

**Previous page:** How to Use Tables
  
**Next page:** How to Use Text Fields




A browser with JavaScript enabled is required for this page to operate properly.