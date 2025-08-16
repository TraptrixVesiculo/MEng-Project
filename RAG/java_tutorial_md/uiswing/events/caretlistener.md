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

How to Write a Caret Listener

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

[How to Write an Undoable Edit Listener](undoableeditlistener.html)

[How to Write Window Listeners](windowlistener.html)

[Listener API Table](api.html)

[Solving Common Event-Handling Problems](problems.html)

[Home Page](../../index.html)
>
[Creating a GUI With JFC/Swing](../index.html)
>
[Writing Event Listeners](index.html)

[« Previous](actionlistener.html) • [Trail](../TOC.html) • [Next »](changelistener.html)

# How to Write a Caret Listener

Caret events occur when the *caret* — the cursor
indicating the insertion
point — in a text component moves
or when the selection in a text component changes.
The text component's document can initiate caret events
when it inserts or removes text, for example.
You can attach a caret listener to an instance of any
`JTextComponent` subclass with the
`addCaretListener` method.

---

**Note:** An alternate way of detecting caret changes is to attach a
listener directly to the caret object itself rather than to
the text component that manages the caret.
A caret fires change events (*not*
caret events), so you would need to write a
[change listener](changelistener.html)
rather than a caret listener.

---

Here is the caret event handling code from an application
called `TextComponentDemo`:

```

...
//where initialization occurs
CaretListenerLabel caretListenerLabel =
    new CaretListenerLabel("Caret Status");
...
textPane.addCaretListener(caretListenerLabel);
...
protected class CaretListenerLabel extends JLabel
                                   implements CaretListener
{
    ...
    //Might not be invoked from the event dispatching thread.
    public void caretUpdate(CaretEvent e) {
        displaySelectionInfo(e.getDot(), e.getMark());
    }

    //This method can be invoked from any thread.  It 
    //invokes the setText and modelToView methods, which 
    //must run in the event dispatching thread. We use
    //invokeLater to schedule the code for execution
    //in the event dispatching thread.
    protected void displaySelectionInfo(final int dot,
                                        final int mark) {
        SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                if (dot == mark) {  // no selection
                    ...
                }
            });
        }
    }
}

```

---

**Note:** The `caretUpdate` method is not guaranteed
to be called in the event-dispatching thread.
To use any methods inside of `caretUpdate`
that update the GUI special
handling is required to ensure they are executed on
the event-dispatching thread. You can do this by wrapping
the code inside a `Runnable` and calling
`SwingUtilities.invokeLater` on that
`Runnable`.

---

You can find a link to the source file for
`TextComponentDemo` in the
[example index for using Swing Components](../examples/components/index.html#TextComponentDemo). For a discussion about the caret listener aspect
of the program see
[Listening for Caret and Selection Changes](../components/generaltext.html#caret) in
[Text Component Features](../components/generaltext.html).

### The Caret Listener API

> The CaretListener
> Interface
>
> *Because `CaretListener` has only one method,
> it has no corresponding adapter class.*
>
> | Method | Purpose |
> | --- | --- |
> | [caretUpdate(CaretEvent)](http://download.oracle.com/javase/7/docs/api/javax/swing/event/CaretListener.html#caretUpdate(javax.swing.event.CaretEvent)) | Called when the caret in the listened-to component moves or when the selection in the listened-to component changes. |
>
> The CaretEvent Class
>
> | Method | Purpose |
> | --- | --- |
> | [int getDot()](http://download.oracle.com/javase/7/docs/api/javax/swing/event/CaretEvent.html#getDot()) | Returns the current location of the caret. If text is selected, the caret marks one end of the selection. |
> | [int getMark()](http://download.oracle.com/javase/7/docs/api/javax/swing/event/CaretEvent.html#getMark()) | Returns the other end of the selection. If nothing is selected, the value returned by this method is equal to the value returned by `getDot`. Note that the dot is not guaranteed to be less than the mark. |
> | [Object getSource()](http://download.oracle.com/javase/7/docs/api/java/util/EventObject.html#getSource()) (*in `java.util.EventObject`*) | Returns the object that fired the event. |

### Examples that Use Caret Listeners
> The following table lists the
> examples that use caret listeners.
>
> | Example | Where Described | Notes |
> | --- | --- | --- |
> | [`TextComponentDemo`](../examples/components/index.html#TextComponentDemo) | [Listening for Caret and Selection Changes](../components/generaltext.html#caret) | Uses a listener label to display caret and selection status. [Listening for Caret and Selection Changes](../components/generaltext.html#caret) | Uses a listener label to display caret and selection status. [Listening for Caret and Selection Changes](../components/generaltext.html#caret) | Uses a listener label to display caret and selection status. | | |

[« Previous](actionlistener.html)
•
[Trail](../TOC.html)
•
[Next »](changelistener.html)

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

**Previous page:** How to Write an Action Listener
  
**Next page:** How to Write a Change Listener




A browser with JavaScript enabled is required for this page to operate properly.