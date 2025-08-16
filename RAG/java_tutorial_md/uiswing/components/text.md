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

Using Text Components

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

[How to Use Borders](border.html)

[Solving Common Component Problems](problems.html)

[Home Page](../../index.html)
>
[Creating a GUI With JFC/Swing](../index.html)
>
[Using Swing Components](index.html)

[« Previous](jcomponent.html) • [Trail](../TOC.html) • [Next »](generaltext.html)

# Using Text Components

This section provides background information
you might need when using
Swing text components.
If you intend to use an unstyled text component
—
a [text field](textfield.html),
[password field](passwordfield.html),
[formatted text field](formattedtextfield.html), or
[text area](textarea.html)
—
go to its how-to page
and return here only if necessary.
If you intend to use a styled text component,
see
[How to Use Editor Panes and Text Panes](editorpane.html),
and read this section as well.
If you do not know which component you need,
read on.

Swing text components display text and
optionally allow the user to edit the text.
Programs need text components for tasks
ranging from the straightforward
(enter a word and press Enter)
to the complex
(display and edit styled text with
embedded images in an Asian language).

Swing provides six text components,
along with supporting classes and interfaces
that meet even the most complex text requirements.
In spite of their different uses and capabilities,
all Swing text components inherit from
the same superclass,
[`JTextComponent`](http://download.oracle.com/javase/7/docs/api/javax/swing/text/JTextComponent.html), which provides a highly-configurable
and powerful foundation for text manipulation.

The following figure shows the `JTextComponent` hierarchy.

![Swing's hierarchy of text components](../../figures/uiswing/components/10jtextcomp.png)

The following picture shows an application
called `TextSamplerDemo` that uses
each Swing text component.

![An application that provides a sample of each Swing text component](../../figures/uiswing/components/TextSamplerDemoMetal.png)

---

**Try this:**

1. Click the Launch button
   to run TextSamplerDemo using
   [Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp ) 
   ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
   Alternatively, to compile and run the example yourself,
   consult the [example index](../examples/components/index.html#TextSamplerDemo).

[![Launches the TextSamplerDemo Application](../../images/jws-launch-button.png)](http://download.oracle.com/javase/tutorialJWS/uiswing/components/ex6/TextSamplerDemo.jnlp)

2. Type some text in the text field and press Enter.
   Do the same in the password field.
   The label beneath the fields is updated when you press Enter.- Try entering valid and invalid dates into the formatted text field.
     Note that
     when you press Enter
     the label beneath the fields is updated
     only if the date is valid.- Select and edit text in the text area and the text pane.
       Use keyboard bindings, Ctrl-X, Ctrl-C, and Ctrl-V,
       to cut, copy, and paste text, respectively.- Try to edit the text in the editor pane,
         which has been made uneditable with a call to `setEditable`.- Look in the text pane to find an example
           of an embedded component and an embedded icon.

---

The `TextSamplerDemo` example uses the text components
in very basic ways.
The following table tells you more about
what you can do with each
kind of text component.

| Group | Description | Swing Classes |
| --- | --- | --- |
| Text Controls | Also known simply as text fields, text controls can display only one line of editable text. Like buttons, they generate action events. Use them to get a small amount of textual information from the user and perform an action after the text entry is complete. | [`JTextField`](http://download.oracle.com/javase/7/docs/api/javax/swing/JTextField.html) and its subclasses [`JPasswordField`](http://download.oracle.com/javase/7/docs/api/javax/swing/JPasswordField.html) and [`JFormattedTextField`](http://download.oracle.com/javase/7/docs/api/javax/swing/JFormattedTextField.html) |
| Plain Text Areas | `JTextArea` can display multiple lines of editable text. Although a text area can display text in any font, all of the text is in the same font. Use a text area to allow the user to enter unformatted text of any length or to display unformatted help information. | [`JTextArea`](http://download.oracle.com/javase/7/docs/api/javax/swing/JTextArea.html) |
| Styled Text Areas | A styled text component can display editable text using more than one font. Some styled text components allow embedded images and even embedded components. Styled text components are powerful and multi-faceted components suitable for high-end needs, and offer more avenues for customization than the other text components. Because they are so powerful and flexible, styled text components typically require more initial programming to set up and use. One exception is that editor panes can be easily loaded with formatted text from a URL, which makes them useful for displaying uneditable help information. | [`JEditorPane`](http://download.oracle.com/javase/7/docs/api/javax/swing/JEditorPane.html)  and its subclass   [`JTextPane`](http://download.oracle.com/javase/7/docs/api/javax/swing/JTextPane.html) |

This Tutorial provides information
about the foundation laid by the `JTextComponent` class
and tells you how to accomplish
some common text-related tasks.
Because the `JTextComponent` class and its subclasses
have too many features
to be completely described in this Tutorial,
please visit the
[Swing
and AWT forum](http://forums.java.net/jive/forum.jspa?forumID=74&start=0) at [java.net](http://java.net/)
for help and information.

[« Previous](jcomponent.html)
•
[Trail](../TOC.html)
•
[Next »](generaltext.html)

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

**Previous page:** The JComponent Class
  
**Next page:** Text Component Features




A browser with JavaScript enabled is required for this page to operate properly.