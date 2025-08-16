[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Creating a GUI With JFC/Swing
  
**Lesson:** Writing Event Listeners
  
**Section:** Implementing Listeners for Commonly Handled Events

[Writing Event Listeners](index.html)

[Introduction to Event Listeners](intro.html)

[General Information about Writing Event Listeners](generalrules.html)

[Listeners Supported by Swing Components](eventsandcomponents.html)

[Implementing Listeners for Commonly Handled Events](handling.html)

[How to Write an Action Listener](actionlistener.html)

[How to Write a Caret Listener](caretlistener.html)

[How to Write a Change Listener](changelistener.html)

[How to Write a Component Listener](componentlistener.html)

[How to Write a Container Listener](containerlistener.html)

How to Write a Document Listener

[How to Write a Focus Listener](focuslistener.html)

[How to Write an Internal Frame Listener](internalframelistener.html)

[How to Write an Item Listener](itemlistener.html)

[How to Write a Key Listener](keylistener.html)

[How to Write a List Data Listener](listdatalistener.html)

[How to Write a List Selection Listener](listselectionlistener.html)

[How to Write a Mouse Listener](mouselistener.html)

[How to Write a Mouse-Motion Listener](mousemotionlistener.html)

[How to Write a Mouse-Wheel Listener](mousewheellistener.html)

[How to Write a Property Change Listener](propertychangelistener.html)

[How to Write a Table Model Listener](tablemodellistener.html)

[How to Write a Tree Expansion Listener](treeexpansionlistener.html)

[How to Write a Tree Model Listener](treemodellistener.html)

[How to Write a Tree Selection Listener](treeselectionlistener.html)

[How to Write a Tree-Will-Expand Listener](treewillexpandlistener.html)

[How to Write an Undoable Edit Listener](undoableeditlistener.html)

[How to Write Window Listeners](windowlistener.html)

[Listener API Table](api.html)

[Solving Common Event-Handling Problems](problems.html)

[Home Page](../../index.html)
>
[Creating a GUI With JFC/Swing](../index.html)
>
[Writing Event Listeners](index.html)

[« Previous](containerlistener.html) • [Trail](../TOC.html) • [Next »](focuslistener.html)

# How to Write a Document Listener

A Swing text component uses a
[`Document`](http://download.oracle.com/javase/7/docs/api/javax/swing/text/Document.html) to represent its content.
Document events occur when the content of a document changes in any way.
You attach a document listener to a text component's document,
rather than to the text component itself.
See
[Implementing a Document Filter](../components/generaltext.html#filter)for more information.

The following example demonstrates document events on
two plain text components.

![This screenshot demonstrates the output of DocumentEventDemo example.](../../figures/uiswing/events/DocumentEventDemo.png)

---

**Try this:**

1. Click the Launch button to run DocumentEventDemo using
   [Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp) ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
   Alternatively, to compile and run the example yourself, consult the
   [example index](../examples/events/index.html#Beeper).
    [![Launches the DocumentEventDemo example](../../images/jws-launch-button.png )](http://download.oracle.com/javase/tutorialJWS/uiswing/events/ex6/DocumentEventDemo.jnlp) - Type in the text field at the upper left of the window
     or the text area beneath the text field.
       
     One document event is fired for each character typed.- Delete text with the backspace key.
         
       One document event is fired for each backspace key typed.- Select text and then delete it by typing backspace
         or by using a keyboard command such as `CTRL-X` (cut).
           
         One document event is fired for the entire deletion.- Copy text from one text component into the other
           using keyboard commands such as `CTRL-C` (copy) and
           `CTRL-V` (paste).
             
           One document event is fired for the entire paste
           operation regardless
           of the length of the text pasted.
           If text is selected in the target text component
           before the paste command is issued,
           an additional document event is fired
           because the selected text is deleted first.

---

You can find the demo's code in
[`DocumentEventDemo.java`](../examples/events/DocumentEventDemoProject/src/events/DocumentEventDemo.java).
Here is the demo's document event handling code:

```

public class DocumentEventDemo ... {
    ...//where initialization occurs:
    textField = new JTextField(20);
    textField.addActionListener(new MyTextActionListener());
    textField.getDocument().addDocumentListener(new MyDocumentListener());
    textField.getDocument().putProperty("name", "Text Field");

    textArea = new JTextArea();
    textArea.getDocument().addDocumentListener(new MyDocumentListener());
    textArea.getDocument().putProperty("name", "Text Area");
    ...

class MyDocumentListener implements DocumentListener {
    String newline = "\n";
 
    public void insertUpdate(DocumentEvent e) {
        updateLog(e, "inserted into");
    }
    public void removeUpdate(DocumentEvent e) {
        updateLog(e, "removed from");
    }
    public void changedUpdate(DocumentEvent e) {
        //Plain text components do not fire these events
    }

    public void updateLog(DocumentEvent e, String action) {
        Document doc = (Document)e.getDocument();
        int changeLength = e.getLength();
        displayArea.append(
            changeLength + " character" +
            ((changeLength == 1) ? " " : "s ") +
            action + doc.getProperty("name") + "." + newline +
            "  Text length = " + doc.getLength() + newline);
    }
}

```

Document listeners should not modify the contents of the document;
The change is already complete
by the time the listener is notified of the change.
Instead, write a custom document that overrides the
`insertString` or `remove` methods, or both.
See
[Listening for Changes on a Document](../components/generaltext.html#doclisteners) for details.

### The Document Listener API

> The DocumentListener
> Interface
>
> *`DocumentListener` has no adapter class.*
>
> | Method | Purpose |
> | --- | --- |
> | [changedUpdate(DocumentEvent)](http://download.oracle.com/javase/7/docs/api/javax/swing/event/DocumentListener.html#changedUpdate(javax.swing.event.DocumentEvent)) | Called when the style of some of the text in the listened-to document changes. This sort of event is fired only from a `StyledDocument` — a `PlainDocument` does not fire these events. |
> | [insertUpdate(DocumentEvent)](http://download.oracle.com/javase/7/docs/api/javax/swing/event/DocumentListener.html#insertUpdate(javax.swing.event.DocumentEvent)) | Called when text is inserted into the listened-to document. |
> | [removeUpdate(DocumentEvent)](http://download.oracle.com/javase/7/docs/api/javax/swing/event/DocumentListener.html#removeUpdate(javax.swing.event.DocumentEvent)) | Called when text is removed from the listened-to document. |
>
> The DocumentEvent Interface
>
> Each document event method is passed an object that implements
> the `DocumentEvent` interface. Typically, this is an
> instance of
> [`DefaultDocumentEvent`](http://download.oracle.com/javase/7/docs/api/javax/swing/text/AbstractDocument.DefaultDocumentEvent.html), defined in `AbstractDocument`.
>
> | Method | Purpose |
> | --- | --- |
> | [Document getDocument()](http://download.oracle.com/javase/7/docs/api/javax/swing/event/DocumentEvent.html#getDocument()) | Returns the document that fired the event. Note that the `DocumentEvent` interface does not inherit from `EventObject`. Therefore, it does not inherit the `getSource` method. |
> | [int getLength()](http://download.oracle.com/javase/7/docs/api/javax/swing/event/DocumentEvent.html#getLength()) | Returns the length of the change. |
> | [int getOffset()](http://download.oracle.com/javase/7/docs/api/javax/swing/event/DocumentEvent.html#getOffset()) | Returns the location within the document of the first character changed. |
> | [ElementChange getChange(Element)](http://download.oracle.com/javase/7/docs/api/javax/swing/event/DocumentEvent.html#getChange(javax.swing.text.Element)) | Returns details about what elements in the document have changed and how. [`ElementChange`](http://download.oracle.com/javase/7/docs/api/javax/swing/event/DocumentEvent.ElementChange.html) is an interface defined within the `DocumentEvent` interface. || [EventType getType()](http://download.oracle.com/javase/7/docs/api/javax/swing/event/DocumentEvent.html#getType()) | Returns the type of change that occurred. [`EventType`](http://download.oracle.com/javase/7/docs/api/javax/swing/event/DocumentEvent.EventType.html) is a class defined within the `DocumentEvent` interface that enumerates the possible changes that can occur on a document: insert text, remove text, and change text style. |

### Examples that Use Document Listeners
> The following table lists the
> examples that use document listeners.
>
> | Example | Where Described | Notes |
> | --- | --- | --- |
> | [`DocumentEventDemo`](../examples/events/index.html#DocumentEventDemo) | This section | Reports all document events that occur on the documents for both a text field and a text area. One listener listens to both text components and uses a client property on the document to determine which component fired the event. |
> | [`TextComponentDemo`](../examples/components/index.html#TextComponentDemo) | [Listening for Changes on a Document](../components/generaltext.html#doclisteners) | Updates a change log every time text in the listened-to document changes. The document in this example supports styled text, so `changedUpdate` gets called in this example. Requires this additional source file: [`DocumentSizeFilter`](../examples/components/index.html#DocumentSizeFilter) |

[« Previous](containerlistener.html)
•
[Trail](../TOC.html)
•
[Next »](focuslistener.html)

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

**Previous page:** How to Write a Container Listener
  
**Next page:** How to Write a Focus Listener




A browser with JavaScript enabled is required for this page to operate properly.