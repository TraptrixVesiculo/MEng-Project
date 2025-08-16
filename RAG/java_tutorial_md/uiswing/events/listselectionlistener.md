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

How to Write a List Selection Listener

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

[« Previous](listdatalistener.html) • [Trail](../TOC.html) • [Next »](mouselistener.html)

# How to Write a List Selection Listener

List selection events
occur when the selection in a
[list](../components/list.html) or
[table](../components/table.html) is either changing or has just changed.
List selection events are fired from an object
that implements the
[`ListSelectionModel`](http://download.oracle.com/javase/7/docs/api/javax/swing/ListSelectionModel.html) interface.
To get a table's list selection model object,
you can use either `getSelectionModel` method or getColumnModel().getSelectionModel().

To detect list selection events,
you register a listener
on the appropriate list selection model object.
The `JList` class also gives you the option of
registering a listener
on the list itself,
rather than directly on the list selection model.

This section looks at two examples
that show how to listen to list selection events
on a selection model.
[Examples that Use List Selection Listeners](#eg)
lists examples that listen on the list directly.

In these two examples, you can dynamically change the selection mode
to any of the three supported modes:

* single selection mode* single interval selection mode* multiple interval selection mode

Here is a picture of ListSelectionDemo example running in a List :

![A snapshot of ListSelectionDemo, which demonstrates selection modes and list selection model.](../../figures/uiswing/events/ListSelectionDemo.gif)

---

**Try this:**

1. Click the Launch button to run ListSelectionDemo using
   [Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp) ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
   Alternatively, to compile and run the example yourself, consult the
   [example index](../examples/events/index.html#ListSelectionDemo).
    [![Launches the ListSelectionDemo example](../../images/jws-launch-button.png )](http://download.oracle.com/javase/tutorialJWS/uiswing/events/ex6/ListSelectionDemo.jnlp) - Select and deselect items in the list.
     The mouse and keyboard commands required to select items
     depends on the look and feel.
     For the Java look and feel,
     click the left mouse button to begin a selection,
     use the shift key to extend a selection contiguously, and
     use the control key to extend a selection discontiguously. Note that there are two types of selections: Lead and Anchor. Lead is the focused item
     and Anchor is the highlighted item. When you press ctrl key and move up and down, the lead selection causes the events being fired even though the
     actual selection has not changed.
     Dragging the mouse moves or extends the selection,
     depending on the list selection mode.

---

Here is a picture of TableListSelectionDemo example running in a Table:

![A snapshot of TableListSelectionDemo, which demonstrates selection modes and list selection model.](../../figures/uiswing/events/TableListSelectionDemo.gif)

---

**Try this:**

1. Click the Launch button to run TableListSelectionDemo using
   [Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp) ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
   Alternatively, to compile and run the example yourself, consult the
   [example index](../examples/events/index.html#TableListSelectionDemo).
    [![Launches the TableListSelectionDemo example](../../images/jws-launch-button.png )](http://download.oracle.com/javase/tutorialJWS/uiswing/events/ex6/TableListSelectionDemo.jnlp) - Select and deselect items in the table.
     The mouse and keyboard commands required to select items
     depends on the look and feel.
     For the Java look and feel,
     click the left mouse button to begin a selection,
     use the shift key to extend a selection contiguously, and
     use the control key to extend a selection discontiguously. Note that there are two types of selections: Lead and Anchor. Lead is the focused item
     and Anchor is the highlighted item. When you press ctrl key and move up or down, the lead selection causes the events being fired even though the
     actual selection has not changed.
     Dragging the mouse moves or extends the selection,
     depending on the list selection mode.

---

You can find the entire program of ListSelectionDemo in
[`ListSelectionDemo.java`](../examples/events/ListSelectionDemoProject/src/events/ListSelectionDemo.java) and the entire program of TableListSelectionDemo in
[`TableListSelectionDemo.java`](../examples/events/TableListSelectionDemoProject/src/events/TableListSelectionDemo.java).

Here is the code from `ListSelectionDemo` that
sets up the selection model and adds a listener to it:

```

...//where the member variables are defined
JList list;
    ...//in the init method:
    listSelectionModel = list.getSelectionModel();
    listSelectionModel.addListSelectionListener(
                            new SharedListSelectionHandler());
    ...

```

And here is the code for the listener,
which works for all the possible selection modes:

```

class SharedListSelectionHandler implements ListSelectionListener {
    public void valueChanged(ListSelectionEvent e) {
        ListSelectionModel lsm = (ListSelectionModel)e.getSource();

        int firstIndex = e.getFirstIndex();
        int lastIndex = e.getLastIndex();
        boolean isAdjusting = e.getValueIsAdjusting();
        output.append("Event for indexes "
                      + firstIndex + " - " + lastIndex
                      + "; isAdjusting is " + isAdjusting
                      + "; selected indexes:");

        if (lsm.isSelectionEmpty()) {
            output.append(" <none>");
        } else {
            // Find out which indexes are selected.
            int minIndex = lsm.getMinSelectionIndex();
            int maxIndex = lsm.getMaxSelectionIndex();
            for (int i = minIndex; i <= maxIndex; i++) {
                if (lsm.isSelectedIndex(i)) {
                    output.append(" " + i);
                }
            }
        }
        output.append(newline);
    }
}


```

This `valueChanged` method displays the
first and last indices reported by the event,
the value of the event's `isAdjusting` flag,
and the indices currently selected.

Note that the first and last indices reported by the event
indicate the inclusive range of items
for which the selection has changed.
If the selection mode is multiple interval selection
some items within the range might not have changed.
The `isAdjusting` flag is `true` if
the user is still manipulating the selection,
and `false` if the user has finished changing the selection.

The `ListSelectionEvent` object
passed into `valueChanged` indicates
only that the selection has changed.
The event contains no information about the current selection.
So, this method queries the selection model to
figure out the current selection.

### The List Selection Listener API

> The ListSelectionListener
> Interface
>
> *Because `ListSelectionListener` has only one method,
> it has no corresponding adapter class.*
>
> | Method | Purpose |
> | --- | --- |
> | [valueChanged(ListSelectionEvent)](http://download.oracle.com/javase/7/docs/api/javax/swing/event/ListSelectionListener.html#valueChanged(javax.swing.ListSelectionEvent)) | Called in response to selection changes. |
>
> The ListSelectionEvent API
>
> | Method | Purpose |
> | --- | --- |
> | [Object getSource()](http://download.oracle.com/javase/7/docs/api/java/util/EventObject.html#getSource()) (*in `java.util.EventObject`*) | Return the object that fired the event. If you register a list selection listener on a list directly, then the source for each event is the list. Otherwise, the source is the selection model. |
> | [int getFirstIndex()](http://download.oracle.com/javase/7/docs/api/javax/swing/event/ListSelectionEvent.html#getFirstIndex()) | Return the index of the first item whose selection value has changed. Note that for multiple interval selection, the first and last items are guaranteed to have changed but items between them might not have. However, when you press ctrl key and move up or down, the lead selection causes the events being fired even though the actual selection has not changed. |
> | [int getLastIndex()](http://download.oracle.com/javase/7/docs/api/javax/swing/event/ListSelectionEvent.html#getLastIndex()) | Return the index of the last item whose selection value has changed. Note that for multiple interval selection, the first and last items are guaranteed to have changed but items between them might not have. However, when you press ctrl key and move up and down, the lead selection causes the events being fired even though the actual selection has not changed. |
> | [boolean getValueIsAdjusting()](http://download.oracle.com/javase/7/docs/api/javax/swing/event/ListSelectionEvent.html#getValueIsAdjusting()) | Return `true` if the selection is still changing. Many list selection listeners are interested only in the final state of the selection and can ignore list selection events when this method returns `true`. |

### Examples that Use List Selection Listeners
> The following table lists the
> examples that use list selection listeners.
>
> | Example | Where Described | Notes |
> | --- | --- | --- |
> | [`ListSelectionDemo`](../examples/events/index.html#ListSelectionDemo) | This section | Reports all list selection events that occur on a list. Lets the user dynamically change the selection mode. |
> | [`TableListSelectionDemo`](../examples/events/index.html#TableListSelectionDemo) | This section | Reports all list selection events that occur on a table. Lets the user dynamically change the selection mode. |
> | [`ListDemo`](../examples/components/index.html#ListDemo) | [How to Use Lists](../components/list.html) | Listens to events on a single-selection list (not on its selection model). Enables and disables a button depending on whether any items are selected in the list. |
> | [`SplitPaneDemo`](../examples/components/index.html#SplitPaneDemo) | [How to Use Lists](../components/list.html) | Listens to events on a single-selection list (not on its selection model). |
> | [`SimpleTableSelectionDemo`](../examples/components/index.html#SimpleTableSelectionDemo) | [How to Use Tables](../components/table.html) | Uses two different list selection listeners on one table. One listener listens to list selection events on table columns, the other listens to list selection events on table rows. |

[« Previous](listdatalistener.html)
•
[Trail](../TOC.html)
•
[Next »](mouselistener.html)

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

**Previous page:** How to Write a List Data Listener
  
**Next page:** How to Write a Mouse Listener




A browser with JavaScript enabled is required for this page to operate properly.