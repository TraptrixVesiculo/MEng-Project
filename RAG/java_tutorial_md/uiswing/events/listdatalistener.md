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

How to Write a List Data Listener

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

[« Previous](keylistener.html) • [Trail](../TOC.html) • [Next »](listselectionlistener.html)

# How to Write a List Data Listener

List data events occur when the contents of a mutable
[list](../components/list.html) change.
Since the model — not the component — fires these events,
you have to register a list data listener with the list model.
If you have not explicitly created a list with a mutable list model,
then your list is immutable, and its model will not fire these events.

---

**Note:** [Combo box](../components/combobox.html) models also fire list data events.
However, you normally do not need to know about them
unless you are
[creating a custom combo box model](../components/combobox.html#datsun).

---

The following example demonstrates list data events on a mutable list:

![An output of the ListDataEventDemo which demonstrates list data events. ](../../figures/uiswing/events/ListDataEventDemo.png)

---

**Try this:**

1. Click the Launch button to run ListDataEventDemo using
   [Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp) ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
   Alternatively, to compile and run the example yourself, consult the
   [example index](../examples/events/index.html#ListDataEventDemo).
    [![Launches the ListDataEventDemo example](../../images/jws-launch-button.png )](http://download.oracle.com/javase/tutorialJWS/uiswing/events/ex6/ListDataEventDemo.jnlp) - Type in the name of your favorite ski resort and click the
     **Add** button. An `intervalAdded`
     event was fired.- Select a few continguous items in the list and click the
       **Delete** button. An `intervalRemoved`
       event was fired.- Select one item and move it up or down in the list with the arrow buttons.
         Two `contentsChanged` events are fired — one for
         the item that moved and one for the item that was displaced.

---

You can find the demo's code in
[`ListDataEventDemo.java`](../examples/events/ListDataEventDemoProject/src/events/ListDataEventDemo.java).
Here is the code that registers
a list data listener on the list model
and implements the listener:

```

//...where member variables are declared...
private DefaultListModel listModel;
...
//Create and populate the list model
listModel = new DefaultListModel();
...
listModel.addListDataListener(new MyListDataListener());

class MyListDataListener implements ListDataListener {
    public void contentsChanged(ListDataEvent e) {
        log.append("contentsChanged: " + e.getIndex0() +
	           ", " + e.getIndex1() + newline);
    }
    public void intervalAdded(ListDataEvent e) {
        log.append("intervalAdded: " + e.getIndex0() +
	           ", " + e.getIndex1() + newline);
    }
    public void intervalRemoved(ListDataEvent e) {
        log.append("intervalRemoved: " + e.getIndex0() +
	           ", " + e.getIndex1() + newline);
    }
} 

```

### The List Data Listener API

> The ListDataListener
> Interface
>
> *`ListDataListener` has no corresponding
> adapter class.*
>
> | Method | Purpose |
> | --- | --- |
> | [intervalAdded(ListDataEvent)](http://download.oracle.com/javase/7/docs/api/javax/swing/event/ListDataListener.html#intervalAdded(javax.swing.event.ListDataEvent)) | Called when one or more items have been added to the list. |
> | [intervalRemoved(ListDataEvent)](http://download.oracle.com/javase/7/docs/api/javax/swing/event/ListDataListener.html#intervalRemoved(javax.swing.event.ListDataEvent)) | Called when one or more items have been removed from the list. |
> | [contentsChanged(ListDataEvent)](http://download.oracle.com/javase/7/docs/api/javax/swing/event/ListDataListener.html#contentsChanged(javax.swing.event.ListDataEvent)) | Called when the contents of one or more items in the list have changed. |
>
> The ListDataEvent API
>
> | Method | Purpose |
> | --- | --- |
> | [Object getSource()](http://download.oracle.com/javase/7/docs/api/java/util/EventObject.html#getSource()) (*in `java.util.EventObject`*) | Return the object that fired the event. |
> | [int getIndex0()](http://download.oracle.com/javase/7/docs/api/javax/swing/event/ListDataEvent.html#getIndex0()) | Return the index of the first item whose value has changed. |
> | [int getIndex1()](http://download.oracle.com/javase/7/docs/api/javax/swing/event/ListDataEvent.html#getIndex1()) | Return the index of the last item whose value has changed. |
> | [int getType()](http://download.oracle.com/javase/7/docs/api/javax/swing/event/ListDataEvent.html#getType()) | Return the event type. The possible values are: `CONTENTS_CHANGED`, `INTERVAL_ADDED`, or `INTERVAL_REMOVED`. |

### Examples that Use List Data Listeners
> The following table lists the
> examples that use list data listeners.
>
> | Example | Where Described | Notes |
> | --- | --- | --- |
> | [`ListDataEventDemo`](../examples/events/index.html#ListDataEventDemo) | This section | Reports all list data events that occur on a list. |

[« Previous](keylistener.html)
•
[Trail](../TOC.html)
•
[Next »](listselectionlistener.html)

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

**Previous page:** How to Write a Key Listener
  
**Next page:** How to Write a List Selection Listener




A browser with JavaScript enabled is required for this page to operate properly.