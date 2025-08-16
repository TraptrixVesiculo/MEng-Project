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

[How to Write a Document Listener](documentlistener.html)

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

How to Write an Undoable Edit Listener

[How to Write Window Listeners](windowlistener.html)

[Listener API Table](api.html)

[Solving Common Event-Handling Problems](problems.html)

[Home Page](../../index.html)
>
[Creating a GUI With JFC/Swing](../index.html)
>
[Writing Event Listeners](index.html)

[« Previous](treewillexpandlistener.html) • [Trail](../TOC.html) • [Next »](windowlistener.html)

# How to Write an Undoable Edit Listener

Undoable edit events occur when an operation that can be undone
occurs on a component.
Currently, only text components fire undoable edit events,
and then only indirectly.
The text component's document fires the events.
For text components,
undoable operations include inserting characters,
deleting characters,
and modifying the style of text.
Programs typically listen to undoable edit events to
assist in the implementation of undo and redo commands.

Here is the undoable edit event handling code from an application
called `TextComponentDemo`.

```

...
//where initialization occurs
document.addUndoableEditListener(new MyUndoableEditListener());
...
protected class MyUndoableEditListener implements UndoableEditListener {
    public void undoableEditHappened(UndoableEditEvent e) {
        //Remember the edit and update the menus
        undo.addEdit(e.getEdit());
        undoAction.updateUndoState();
        redoAction.updateRedoState();
    }
}  

```

You can find a link to the source file for
`TextComponentDemo` in the
[example index for Using Swing Components](../examples/components/index.html#TextComponentDemo). For a discussion about the undoable edit listener aspect
of the program see
[Implementing Undo and Redo](../components/generaltext.html#undo)

### The Undoable Edit Listener API

> The UndoableEditListener
> Interface
>
> *Because `UndoableEditListener` has only one method,
> it has no corresponding adapter class.*
>
> | Method | Purpose |
> | --- | --- |
> | [undoableEditHappened(UndoableEditEvent)](http://download.oracle.com/javase/7/docs/api/javax/swing/event/UndoableEditListener.html#undoableEditHappened(javax.swing.event.UndoableEditEvent)) | Called when an undoable event occurs on the listened-to component. |
>
> The UndoableEditEvent Class
>
> | Method | Purpose |
> | --- | --- |
> | [Object getSource()](http://download.oracle.com/javase/7/docs/api/java/util/EventObject.html#getSource()) (*in `java.util.EventObject`*) | Return the object that fired the event. |
> | [UndoableEdit getEdit()](http://download.oracle.com/javase/7/docs/api/javax/swing/event/UndoableEditEvent.html#getEdit()) | Returns an [`UndoableEdit`](http://download.oracle.com/javase/7/docs/api/javax/swing/undo/UndoableEdit.html) object that represents the edit that occurred and contains information about and commands for undoing or redoing the edit. |

### Examples that Use Undoable Edit Listeners
> The following table lists the
> examples that use undoable edit listeners.
>
> | Example | Where Described | Notes |
> | --- | --- | --- |
> | [`TextComponentDemo`](../examples/components/index.html#TextComponentDemo) | [Implementing Undo and Redo](../components/generaltext.html#undo) | Implements undo and redo on a text pane with help from an undoable edit listener. |

[« Previous](treewillexpandlistener.html)
•
[Trail](../TOC.html)
•
[Next »](windowlistener.html)

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

**Previous page:** How to Write a Tree-Will-Expand Listener
  
**Next page:** How to Write Window Listeners




A browser with JavaScript enabled is required for this page to operate properly.