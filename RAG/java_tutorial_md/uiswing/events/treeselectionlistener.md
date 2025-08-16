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

How to Write a Tree Selection Listener

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

[« Previous](treemodellistener.html) • [Trail](../TOC.html) • [Next »](treewillexpandlistener.html)

# How to Write a Tree Selection Listener

To detect when the user selects a node in a
[tree](../components/tree.html), you need to register a tree selection listener.
Here is an example, taken from
the `TreeDemo` example discussed in
[Responding to Node Selection](../components/tree.html#select), of detecting node selection
in a tree that can have at most one node
selected at a time:

```

tree.addTreeSelectionListener(new TreeSelectionListener() {
    public void valueChanged(TreeSelectionEvent e) {
        DefaultMutableTreeNode node = (DefaultMutableTreeNode)
                           tree.getLastSelectedPathComponent();

    /* if nothing is selected */ 
        if (node == null) return;

    /* retrieve the node that was selected */ 
        Object nodeInfo = node.getUserObject();
	...
    /* React to the node selection. */
	...
    }
});

```

To specify that the tree should support single selection,
the program uses this code:

```

tree.getSelectionModel().setSelectionMode
        (TreeSelectionModel.SINGLE_TREE_SELECTION);

```

The `TreeSelectionModel` interface
defines three values for the selection mode:

**`DISCONTIGUOUS_TREE_SELECTION`**: This is the default mode for the default tree selection model. With this mode, any combination of nodes can be selected. **`SINGLE_TREE_SELECTION`**: This is the mode used by the preceding example. At most one node can be selected at a time. **`CONTIGUOUS_TREE_SELECTION`**: With this mode, only nodes in adjoining rows can be selected.

### The Tree Selection Listener API

> The TreeSelectionListener
> Interface
>
> *Because `TreeSelectionListener` has only one method,
> it has no corresponding adapter class.*
>
> | Method | Purpose |
> | --- | --- |
> | [valueChanged(TreeSelectionEvent)](http://download.oracle.com/javase/7/docs/api/javax/swing/event/TreeSelectionListener.html#valueChanged(javax.swing.event.TreeSelectionEvent)) | Called whenever the selection changes. |
>
> The TreeSelectionEvent API
>
> | Method | Purpose |
> | --- | --- |
> | [Object getSource()](http://download.oracle.com/javase/7/docs/api/java/util/EventObject.html#getSource()) (*in `java.util.EventObject`*) | Return the object that fired the event. |
> | [TreePath getNewLeadSelectionPath()](http://download.oracle.com/javase/7/docs/api/javax/swing/event/TreeSelectionEvent.html#getNewLeadSelectionPath()) | Return the current lead path. |
> | [TreePath getOldLeadSelectionPath()](http://download.oracle.com/javase/7/docs/api/javax/swing/event/TreeSelectionEvent.html#getOldLeadSelectionPath()) | Return the path that was previously the lead path. |
> | [TreePath getPath()](http://download.oracle.com/javase/7/docs/api/javax/swing/event/TreeSelectionEvent.html#getPath()) | Return the first path element. |
> | [TreePath[] getPaths()](http://download.oracle.com/javase/7/docs/api/javax/swing/event/TreeSelectionEvent.html#getPaths()) | Return the paths that have been added or removed from the selection. |
> | [boolean isAddedPath()](http://download.oracle.com/javase/7/docs/api/javax/swing/event/TreeSelectionEvent.html#isAddedPath()) | Return true if the first path element has been added to the selection. Returns false if the first path has been removed from the selection. |
> | [boolean isAddedPath(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/event/TreeSelectionEvent.html#isAddedPath(int)) | Return true if the path specified by the index was added to the selection. |
> | [boolean isAddedPath(TreePath)](http://download.oracle.com/javase/7/docs/api/javax/swing/event/TreeSelectionEvent.html#isAddedPath(javax.swing.tree.TreePath)) | Return true if the specified path was added to the selection. |
> | [Object getLastSelectedPathComponent()](http://download.oracle.com/javase/7/docs/api/javax/swing/JTree.html#getLastSelectedPathComponent()) | Return the last path component in the first node of the current selection. |
> | [TreePath getLeadSelectionPath()](http://download.oracle.com/javase/7/docs/api/javax/swing/JTree.html#getLeadSelectionPath()) (*in `JTree`*) | Return the current lead path. |

### Examples that Use Tree Selection Listeners
> The following table lists the
> examples that use tree selection listeners.
>
> | Example | Where Described | Notes |
> | --- | --- | --- |
> | [`TreeDemo`](../examples/components/index.html#TreeDemo) | [How to Use Trees](../components/tree.html) | The tree listener responds to node clicks by showing the appropriate HTML document. |

[« Previous](treemodellistener.html)
•
[Trail](../TOC.html)
•
[Next »](treewillexpandlistener.html)

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

**Previous page:** How to Write a Tree Model Listener
  
**Next page:** How to Write a Tree-Will-Expand Listener




A browser with JavaScript enabled is required for this page to operate properly.