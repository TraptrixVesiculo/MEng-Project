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

How to Write a Table Model Listener

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

[« Previous](propertychangelistener.html) • [Trail](../TOC.html) • [Next »](treeexpansionlistener.html)

# How to Write a Table Model Listener

Upon instantiation, each
[`JTable`](../components/table.html) object is passed a table model object that manages the data it displays. By default, a `JTable` object inherits a `DefaultTable` object if no custom `TableModel` object is specified, but by default, this model only manages strings. To handle objects, perform calculations, or to retrieve data from databases or other programs, you must design your own custom `TableModel` object, which implements the `TableModel` interface.
See [Creating a Table Model](../components/table.html#data) for details.

To detect changes to the data managed by a table model object, the `JTable` class needs to implement the `TableModelListener` interface, call `addTableModelListener()` to catch events, and then override `tableChanged()` to respond to listener events.
See [Listening for Data Changes](../components/table.html#modelchange) for details.

### The Table Model Listener API

> The TableModelListener
> Interface
>
> *Because `TableModelListener` has only one method,
> it has no corresponding adapter class.*
>
> | Method | Purpose |
> | --- | --- |
> | [tableChanged(TableModelEvent)](http://download.oracle.com/javase/7/docs/api/javax/swing/event/TableModelListener.html#tableChanged(javax.swing.event.TableModelEvent)) | Called when the structure of or data in the table has changed. |
>
> The TableModelEvent API
>
> | Method | Purpose |
> | --- | --- |
> | [Object getSource()](http://download.oracle.com/javase/7/docs/api/java/util/EventObject.html#getSource()) (*in `java.util.EventObject`*) | Return the object that fired the event. |
> | [int getFirstRow()](http://download.oracle.com/javase/7/docs/api/javax/swing/event/TableModelEvent.html#getFirstRow()) | Return the index of the first row that changed. `TableModelEvent.HEADER_ROW` specifies the table header. |
> | [int getLastRow()](http://download.oracle.com/javase/7/docs/api/javax/swing/event/TableModelEvent.html#getLastRow()) | The last row that changed. Again, `HEADER_ROW` is a possible value. |
> | [int getColumn()](http://download.oracle.com/javase/7/docs/api/javax/swing/event/TableModelEvent.html#getColumn()) | Return the index of the column that changed. The constant `TableModelEvent.ALL_COLUMNS` specifies that all the columns might have changed. |
> | [int getType()](http://download.oracle.com/javase/7/docs/api/javax/swing/event/TableModelEvent.html#getType()) | What happened to the changed cells. The returned value is one of the following: `TableModelEvent.INSERT`, `TableModelEvent.DELETE`, or `TableModelEvent.UPDATE`. |

[« Previous](propertychangelistener.html)
•
[Trail](../TOC.html)
•
[Next »](treeexpansionlistener.html)

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

**Previous page:** How to Write a Property Change Listener
  
**Next page:** How to Write a Tree Expansion Listener




A browser with JavaScript enabled is required for this page to operate properly.