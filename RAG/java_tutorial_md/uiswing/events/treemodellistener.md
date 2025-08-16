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

How to Write a Tree Model Listener

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

[« Previous](treeexpansionlistener.html) • [Trail](../TOC.html) • [Next »](treeselectionlistener.html)

# How to Write a Tree Model Listener

By implementing a tree model listener,
you can detect when the data displayed by a
[tree](../components/tree.html)
changes.
You can use a tree model listener
to detect when the user edits tree nodes. All notifications describe changes relative to a node in the tree.
For details,
read
[Dynamically Changing a Tree](../components/tree.html#dynamic).

### The Tree Model Listener API

> The TreeModelListener
> Interface
>
> *`TreeModelListener` has no adapter class.*
>
> | Method | Purpose |
> | --- | --- |
> | [treeNodesChanged(TreeModelEvent)](http://download.oracle.com/javase/7/docs/api/javax/swing/event/TreeModelListener.html#treeNodesChanged(javax.swing.event.TreeModelEvent)) | Called when one or more sibling nodes have changed in some way. |
> | [treeNodesInserted(TreeModelEvent)](http://download.oracle.com/javase/7/docs/api/javax/swing/event/TreeModelListener.html#treeNodesInserted(javax.swing.event.TreeModelEvent)) | Called after nodes have been inserted into the tree. |
> | [treeNodesRemoved(TreeModelEvent)](http://download.oracle.com/javase/7/docs/api/javax/swing/event/TreeModelListener.html#treeNodesRemoved(javax.swing.event.TreeModelEvent)) | Called after nodes have been removed from the tree. |
> | [treeStructureChanged(TreeModelEvent)](http://download.oracle.com/javase/7/docs/api/javax/swing/event/TreeModelListener.html#treeStructureChanged(javax.swing.event.TreeModelEvent)) | Called after the tree's structure has drastically changed from the current node on down. This event applies to all nodes connected to this node. |
>
> The TreeModelEvent API
>
> | Method | Purpose |
> | --- | --- |
> | [Object getSource()](http://download.oracle.com/javase/7/docs/api/java/util/EventObject.html#getSource()) (*in `java.util.EventObject`*) | Return the object that fired the event. |
> | [int[] getChildIndices()](http://download.oracle.com/javase/7/docs/api/javax/swing/event/TreeModelEvent.html#getChildIndices()) | For `treeNodesChanged`, `treeNodesInserted`, and `treeNodesRemoved`, returns the indices of the changed, inserted, or deleted nodes, respectively. Returns nothing useful for `treeStructureChanged`. |
> | [Object[] getChildren()](http://download.oracle.com/javase/7/docs/api/javax/swing/event/TreeModelEvent.html#getChildren()) | Returns the objects corresponding to the child indices. |
> | [Object[] getPath()](http://download.oracle.com/javase/7/docs/api/javax/swing/event/TreeModelEvent.html#getPath()) | Returns the path to the parent of the changed, inserted, or deleted nodes. For `treeStructureChanged`, returns the path to the node beneath which the structure has changed. |
> | [TreePath getTreePath()](http://download.oracle.com/javase/7/docs/api/javax/swing/event/TreeModelEvent.html#getTreePath()) | Returns the same thing as `getPath`, but as a [`TreePath`](http://download.oracle.com/javase/7/docs/api/javax/swing/tree/TreePath.html) object. |

### Examples that Use Tree Model Listeners
> The following table lists the
> examples that use tree expansion listeners.
>
> | Example | Where Described | Notes |
> | --- | --- | --- |
> | [`DynamicTreeDemo`](../examples/components/index.html#DynamicTreeDemo) | [How to Use Trees](../components/tree.html#dynamic) | The `DynamicTree` class implements a tree model listener to detect when the user has edited a node's data. |

[« Previous](treeexpansionlistener.html)
•
[Trail](../TOC.html)
•
[Next »](treeselectionlistener.html)

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

**Previous page:** How to Write a Tree Expansion Listener
  
**Next page:** How to Write a Tree Selection Listener




A browser with JavaScript enabled is required for this page to operate properly.