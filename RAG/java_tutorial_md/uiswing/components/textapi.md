[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Creating a GUI With JFC/Swing
  
**Lesson:** Using Swing Components
  
**Section:** Using Text Components

[Using Swing Components](index.html)

[Using Top-Level Containers](toplevel.html)

[The JComponent Class](jcomponent.html)

[Using Text Components](text.html)

[Text Component Features](generaltext.html)

The Text Component API

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

[« Previous](generaltext.html) • [Trail](../TOC.html) • [Next »](componentlist.html)

# The Text Component API

This section lists commonly used parts
of the API that are shared by text components.
Much of this API is defined by the
[`JTextComponent`](http://download.oracle.com/javase/7/docs/api/javax/swing/text/JTextComponent.html) class.
[Text Component Features](generaltext.html)
discusses how to use some of this API.

[The JComponent Class](jcomponent.html)
describes the API that text components
inherit from `JComponent`.
For information about the API
related to specific text components,
see the how-to page for that component:
[text field](textfield.html),
[password field](passwordfield.html),
[formatted text field](formattedtextfield.html),
[text area](textarea.html), or
[editor pane and text pane](editorpane.html).

For complete details about the text API,
see the API documentation for
[`JTextComponent`](http://download.oracle.com/javase/7/docs/api/javax/swing/text/JTextComponent.html) and for the various classes and
interfaces in the
[text package](http://download.oracle.com/javase/7/docs/api/javax/swing/text/package-summary.html).

The API listed in this section includes the following categories:

* [Setting Attributes](#appearance)* [Manipulating the Selection](#selection)* [Converting Positions Between the Model and the View](#conversions)* [Text Editing Commands](#apiforcommands)* [Classes and Interfaces That Represent Documents](#docclasses)* [Working With Documents](#docmethods)* [Manipulating Carets and Selection Highlighters](#carrots)* [Reading and Writing Text](#io)

**Setting Attributes**
  
*These methods are defined in the `JTextComponent` class.*

| Method | Description |
| [void setEditable(boolean)](http://download.oracle.com/javase/7/docs/api/javax/swing/text/JTextComponent.html#setEditable(boolean))   [boolean isEditable()](http://download.oracle.com/javase/7/docs/api/javax/swing/text/JTextComponent.html#isEditable()) | Sets or indicates whether the user can edit the text in the text component. |
| [void setDragEnabled(boolean)](http://download.oracle.com/javase/7/docs/api/javax/swing/text/JTextComponent.html#setDragEnabled(boolean))   [boolean getDragEnabled()](http://download.oracle.com/javase/7/docs/api/javax/swing/text/JTextComponent.html#getDragEnabled()) | Sets or gets the `dragEnabled` property, which must be true to enable drag handling on this component. The default value is false. See [Drag and Drop and Data Transfer](../dnd/index.html) for more details. |
| [void setDisabledTextColor(Color)](http://download.oracle.com/javase/7/docs/api/javax/swing/text/JTextComponent.html#setDisabledTextColor(java.awt.Color))   [Color getDisabledTextColor()](http://download.oracle.com/javase/7/docs/api/javax/swing/text/JTextComponent.html#getDisabledTextColor()) | Sets or gets the color used to display text when the text component is disabled. |
| [void setMargin(Insets)](http://download.oracle.com/javase/7/docs/api/javax/swing/text/JTextComponent.html#setMargin(java.awt.Insets))   [Insets getMargin()](http://download.oracle.com/javase/7/docs/api/javax/swing/text/JTextComponent.html#getMargin()) | Sets or gets the margin between the text and the text component's border. |

**Manipulating the Selection**
  
*These methods are defined in the `JTextComponent` class.*

| Method | Description |
| [String getSelectedText()](http://download.oracle.com/javase/7/docs/api/javax/swing/text/JTextComponent.html#getSelectedText()) | Gets the currently selected text. |
| [void selectAll()](http://download.oracle.com/javase/7/docs/api/javax/swing/text/JTextComponent.html#selectAll())   [void select(int, int)](http://download.oracle.com/javase/7/docs/api/javax/swing/text/JTextComponent.html#select(int, int)) | Selects all text or selects text within a start and end range. |
| [void setSelectionStart(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/text/JTextComponent.html#setSelectionStart(int))   [void setSelectionEnd(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/text/JTextComponent.html#setSelectionEnd(int))   [int getSelectionStart()](http://download.oracle.com/javase/7/docs/api/javax/swing/text/JTextComponent.html#getSelectionStart())   [int getSelectionEnd()](http://download.oracle.com/javase/7/docs/api/javax/swing/text/JTextComponent.html#getSelectionEnd()) | Sets or gets the extent of the current selection by index. |
| [void setSelectedTextColor(Color)](http://download.oracle.com/javase/7/docs/api/javax/swing/text/JTextComponent.html#setSelectedTextColor(java.awt.Color))   [Color getSelectedTextColor()](http://download.oracle.com/javase/7/docs/api/javax/swing/text/JTextComponent.html#getSelectedTextColor()) | Sets or gets the color of selected text. |
| [void setSelectionColor(Color)](http://download.oracle.com/javase/7/docs/api/javax/swing/text/JTextComponent.html#setSelectionColor(java.awt.Color))   [Color getSelectionColor()](http://download.oracle.com/javase/7/docs/api/javax/swing/text/JTextComponent.html#getSelectionColor()) | Sets or gets the background color of selected text. |

**Converting Positions Between the Model and the View**
  
*These methods are defined in the `JTextComponent` class.*

| Method | Description |
| [int viewToModel(Point)](http://download.oracle.com/javase/7/docs/api/javax/swing/text/JTextComponent.html#viewToModel(java.awt.Point)) | Converts the specified point in the view coordinate system to a position within the text. |
| [Rectangle modelToView(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/text/JTextComponent.html#modelToView(int)) | Converts the specified position within the text to a rectangle in the view coordinate system. |

**Text Editing Commands**

| Class or Method | Description |
| [void cut()](http://download.oracle.com/javase/7/docs/api/javax/swing/text/JTextComponent.html#cut())   [void copy()](http://download.oracle.com/javase/7/docs/api/javax/swing/text/JTextComponent.html#copy())   [void paste()](http://download.oracle.com/javase/7/docs/api/javax/swing/text/JTextComponent.html#paste())   [void replaceSelection(String)](http://download.oracle.com/javase/7/docs/api/javax/swing/text/JTextComponent.html#replaceSelection(java.lang.String))  *(in `JTextComponent`)* | Cuts, copies, and pastes text using the system clipboard, or replaces the selected text with the string specified by an argument, respectively. |
| [EditorKit](http://download.oracle.com/javase/7/docs/api/javax/swing/text/EditorKit.html) | Provides a text component's view factory, document, caret, and actions, as well as reading and writing documents of a particular format. |
| [DefaultEditorKit](http://download.oracle.com/javase/7/docs/api/javax/swing/text/DefaultEditorKit.html) | A concrete subclass of `EditorKit` that provides the basic text editing capabilities. |
| [StyledEditorKit](http://download.oracle.com/javase/7/docs/api/javax/swing/text/StyledEditorKit.html) | A subclass of `Default EditorKit` that provides additional editing capabilities for styled text. |
| [String *xxxx*Action](http://download.oracle.com/javase/7/docs/api/javax/swing/text/DefaultEditorKit.html#field_summary)  *(in `DefaultEditorKit`)* | The names of all the actions supported by the default editor kit. See [Associating Text Actions with Menus and Buttons](generaltext.html#commands). |
| [BeepAction](http://download.oracle.com/javase/7/docs/api/javax/swing/text/DefaultEditorKit.BeepAction.html)   [CopyAction](http://download.oracle.com/javase/7/docs/api/javax/swing/text/DefaultEditorKit.CopyAction.html)   [CutAction](http://download.oracle.com/javase/7/docs/api/javax/swing/text/DefaultEditorKit.CutAction.html)   [DefaultKeyTypedAction](http://download.oracle.com/javase/7/docs/api/javax/swing/text/DefaultEditorKit.DefaultKeyTypedAction.html)   [InsertBreakAction](http://download.oracle.com/javase/7/docs/api/javax/swing/text/DefaultEditorKit.InsertBreakAction.html)   [InsertContentAction](http://download.oracle.com/javase/7/docs/api/javax/swing/text/DefaultEditorKit.InsertContentAction.html)   [InsertTabAction](http://download.oracle.com/javase/7/docs/api/javax/swing/text/DefaultEditorKit.InsertTabAction.html)   [PasteAction](http://download.oracle.com/javase/7/docs/api/javax/swing/text/DefaultEditorKit.PasteAction.html)  *(in `DefaultEditorKit`)* | Inner classes that implement various text editing commands. |
| [AlignmentAction](http://download.oracle.com/javase/7/docs/api/javax/swing/text/StyledEditorKit.AlignmentAction.html)   [BoldAction](http://download.oracle.com/javase/7/docs/api/javax/swing/text/StyledEditorKit.BoldAction.html)   [FontFamilyAction](http://download.oracle.com/javase/7/docs/api/javax/swing/text/StyledEditorKit.FontFamilyAction.html)   [FontSizeAction](http://download.oracle.com/javase/7/docs/api/javax/swing/text/StyledEditorKit.FontSizeAction.html)   [ForegroundAction](http://download.oracle.com/javase/7/docs/api/javax/swing/text/StyledEditorKit.ForegroundAction.html)   [ItalicAction](http://download.oracle.com/javase/7/docs/api/javax/swing/text/StyledEditorKit.ItalicAction.html)   [StyledTextAction](http://download.oracle.com/javase/7/docs/api/javax/swing/text/StyledEditorKit.StyledTextAction.html)   [UnderlineAction](http://download.oracle.com/javase/7/docs/api/javax/swing/text/StyledEditorKit.UnderlineAction.html)  *(in `StyledEditorKit`)* | Inner classes that implement various editing commands for styled text. |
| [Action[] getActions()](http://download.oracle.com/javase/7/docs/api/javax/swing/text/JTextComponent.html#getActions())  *(in `JTextComponent`)* | Gets the actions supported by this component. This method gets the array of actions from the editor kit if one is used by the component. |
| [InputMap getInputMap()](http://download.oracle.com/javase/7/docs/api/javax/swing/JComponent.html#getInputMap())  *(in `JComponent`)* | Gets the input map that binds key strokes to actions. See [Associating Text Actions with Key Strokes](generaltext.html#bindingkeystrokes). |
| [void put(KeyStroke, Object)](http://download.oracle.com/javase/7/docs/api/javax/swing/InputMap.html#put(javax.swing.KeyStroke, java.lang.Object))  *(in `InputMap`)* | Binds the specified key to the specified action. You generally specify the action by its name, which for standard editing actions is represented by a string constant such as `DefaultEditorKit.backwardAction`. |

**Classes and Interfaces That Represent Documents**

| Interface or Class | Description |
| [Document](http://download.oracle.com/javase/7/docs/api/javax/swing/text/Document.html) | An interface that defines the API that must be implemented by all documents. |
| [AbstractDocument](http://download.oracle.com/javase/7/docs/api/javax/swing/text/AbstractDocument.html) | An abstract superclass implementation of the `Document` interface. This is the superclass for all documents provided by the Swing text package. |
| [PlainDocument](http://download.oracle.com/javase/7/docs/api/javax/swing/text/PlainDocument.html) | A class that implements the `Document` interface. This is the default document for the plain text components (text field, password field, and text area). Additionally, this class is used by the editor panes and text panes when loading plain text or text of an unknown format. |
| [StyledDocument](http://download.oracle.com/javase/7/docs/api/javax/swing/text/StyledDocument.html) | A `Document` subinterface. Defines the API that must be implemented by documents that support styled text. `JTextPane` requires that its document be of this type. |
| [DefaultStyledDocument](http://download.oracle.com/javase/7/docs/api/javax/swing/text/DefaultStyledDocument.html) | A class that implements the `StyledDocument` interface. The default document for `JTextPane`. |

**Working With Documents**

| Class or Method | Description |
| [DocumentFilter](http://download.oracle.com/javase/7/docs/api/javax/swing/text/DocumentFilter.html) | The superclass of all document filters. You can use a document filter to change what gets inserted or removed from a document, without having to implement a document yourself. See [Implementing a Document Filter](generaltext.html#filter). |
| [void setDocumentFilter(DocumentFilter)](http://download.oracle.com/javase/7/docs/api/javax/swing/text/AbstractDocument.html#setDocumentFilter(javax.swing.text.DocumentFilter))  *(in `AbstractDocument`)* | Sets the document filter. |
 [void setDocument(Document)](http://download.oracle.com/javase/7/docs/api/javax/swing/text/JTextComponent.html#setDocument(javax.swing.text.Document))   [Document getDocument()](http://download.oracle.com/javase/7/docs/api/javax/swing/text/JTextComponent.html#getDocument())  *(in `JTextComponent`)* | Sets or gets the document for a text component. || [Document createDefaultModel()](http://download.oracle.com/javase/7/docs/api/javax/swing/JTextField.html#createDefaultModel())  *(in `JTextField`)* | Creates a default PlainDocument model. Override this method to create a custom document instead of the default `PlainDocument`. |
| [void addDocumentListener(DocumentListener)](http://download.oracle.com/javase/7/docs/api/javax/swing/text/Document.html#addDocumentListener(javax.swing.event.DocumentListener))   [void removeDocumentListener(DocumentListener)](http://download.oracle.com/javase/7/docs/api/javax/swing/text/Document.html#removeDocumentListener(javax.swing.event.DocumentListener))  *(in `Document`)* | Adds or removes a document listener. See [Listening for Changes on a Document](generaltext.html#doclisteners). |
| [void addUndoableEditListener(UndoableEditListener)](http://download.oracle.com/javase/7/docs/api/javax/swing/text/Document.html#addUndoableEditListener(javax.swing.event.UndoableEditListener))   [void removeUndoableEditListener(UndoableEditlistener)](http://download.oracle.com/javase/7/docs/api/javax/swing/text/Document.html#removeUndoableEditListener(javax.swing.event.UndoableEditListener))  *(in `Document`)* | Adds or removes an undoable edit listener. Undoable edit listeners are used in [Implementing Undo and Redo](generaltext.html#undo). |
| [int getLength()](http://download.oracle.com/javase/7/docs/api/javax/swing/text/Document.html#getLength())   [Position getStartPosition()](http://download.oracle.com/javase/7/docs/api/javax/swing/text/Document.html#getStartPosition())   [Position getEndPosition()](http://download.oracle.com/javase/7/docs/api/javax/swing/text/Document.html#getEndPosition())   [String getText(int, int)](http://download.oracle.com/javase/7/docs/api/javax/swing/text/Document.html#getText(int, int))  *(in `Document`)* | `Document` methods that return various descriptive information about the document. |
| [Object getProperty(Object)](http://download.oracle.com/javase/7/docs/api/javax/swing/text/Document.html#getProperty(java.lang.Object))   [void putProperty(Object, Object)](http://download.oracle.com/javase/7/docs/api/javax/swing/text/Document.html#putProperty(java.lang.Object, java.lang.Object))  *(in `Document`)*   [void setDocumentProperties(Dictionary)](http://download.oracle.com/javase/7/docs/api/javax/swing/text/AbstractDocument.html#setDocumentProperties(java.util.Dictionary))   [Dictionary getDocumentProperties()](http://download.oracle.com/javase/7/docs/api/javax/swing/text/AbstractDocument.html#getDocumentProperties())  *(in `AbstractDocument`)* | A `Document` maintains a set of properties that you can manipulate with these methods. |

**Manipulating Carets and Selection Highlighters**
  
*These methods are defined in the `JTextComponent` class.*

| Interface, Class, or Method | Description |
| [Caret](http://download.oracle.com/javase/7/docs/api/javax/swing/text/Caret.html) | An interface that defines the API for objects that represent an insertion point within documents. |
| [DefaultCaret](http://download.oracle.com/javase/7/docs/api/javax/swing/text/DefaultCaret.html) | The default caret used by all text components. |
| [void setCaret(Caret)](http://download.oracle.com/javase/7/docs/api/javax/swing/text/JTextComponent.html#setCaret(javax.swing.text.Caret))   [Caret getCaret()](http://download.oracle.com/javase/7/docs/api/javax/swing/text/JTextComponent.html#getCaret()) | Sets or gets the caret object used by a text component. |
| [void setCaretColor(Color)](http://download.oracle.com/javase/7/docs/api/javax/swing/text/JTextComponent.html#setCaretColor(java.awt.Color))   [Color getCaretColor()](http://download.oracle.com/javase/7/docs/api/javax/swing/text/JTextComponent.html#getCaretColor()) | Sets or gets the color of the caret. |
| [void setCaretPosition(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/text/JTextComponent.html#setCaretPosition(int))   [void moveCaretPosition(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/text/JTextComponent.html#moveCaretPosition(int))   [int getCaretPosition()](http://download.oracle.com/javase/7/docs/api/javax/swing/text/JTextComponent.html#getCaretPosition()) | Sets or gets the current position of the caret within the document. |
| [void addCaretListener(CaretListener)](http://download.oracle.com/javase/7/docs/api/javax/swing/text/JTextComponent.html#addCaretListener(javax.swing.event.CaretListener))   [void removeCaretListener(CaretListener)](http://download.oracle.com/javase/7/docs/api/javax/swing/text/JTextComponent.html#removeCaretListener(javax.swing.event.CaretListener)) | Adds or removes a caret listener from a text component. |
| [NavigationFilter](http://download.oracle.com/javase/7/docs/api/javax/swing/text/NavigationFilter.html) | The superclass for all navigation filters. A navigation filter lets you modify caret changes that are about to occur for a text component. |
| [void setNavigationFilter(NavigationFilter)](http://download.oracle.com/javase/7/docs/api/javax/swing/text/JTextComponent.html#setNavigationFilter(javax.swing.text.NavigationFilter)) | Attaches a navigation filter to a text component. |
| [Highlighter](http://download.oracle.com/javase/7/docs/api/javax/swing/text/Highlighter.html) | An interface that defines the API for objects used to highlight the current selection. |
| [DefaultHighlighter](http://download.oracle.com/javase/7/docs/api/javax/swing/text/DefaultHighlighter.html) | The default highlighter used by all text components. |
| [void setHighlighter(Highlighter)](http://download.oracle.com/javase/7/docs/api/javax/swing/text/JTextComponent.html#setHighlighter(javax.swing.text.Highlighter))   [Highlighter getHighlighter()](http://download.oracle.com/javase/7/docs/api/javax/swing/text/JTextComponent.html#getHighlighter()) | Sets or gets the highlighter used by a text component. |

**Reading and Writing Text**

| Method | Description |
| [void read(Reader, Object)](http://download.oracle.com/javase/7/docs/api/javax/swing/text/JTextComponent.html#read(java.io.Reader, java.lang.Object))   [void write(Writer)](http://download.oracle.com/javase/7/docs/api/javax/swing/text/JTextComponent.html#write(java.io.Writer))  *(in `JTextComponent`)* | Reads or writes text. |
| [void read(Reader, Document, int)](http://download.oracle.com/javase/7/docs/api/javax/swing/text/EditorKit.html#read(java.io.Reader, javax.swing.text.Document, int))   [void read(InputStream, Document, int)](http://download.oracle.com/javase/7/docs/api/javax/swing/text/EditorKit.html#read(java.io.InputStream, javax.swing.text.Document, int))  *(in `EditorKit`)* | Reads text from a stream into a document. |
| [void write(Writer, Document, int, int)](http://download.oracle.com/javase/7/docs/api/javax/swing/text/EditorKit.html#write(java.io.Writer, javax.swing.text.Document, int, int))   [void write(OutputStream, Document, int, int)](http://download.oracle.com/javase/7/docs/api/javax/swing/text/EditorKit.html#write(java.io.OutputStream, javax.swing.text.Document, int, int))  *(in `EditorKit`)* | Writes text from a document to a stream. |

[« Previous](generaltext.html)
•
[Trail](../TOC.html)
•
[Next »](componentlist.html)

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

**Previous page:** Text Component Features
  
**Next page:** How to Use Various Components




A browser with JavaScript enabled is required for this page to operate properly.