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

How to Write a Tree Expansion Listener

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

[« Previous](tablemodellistener.html) • [Trail](../TOC.html) • [Next »](treemodellistener.html)

# How to Write a Tree Expansion Listener

Sometimes when using a
[tree](../components/tree.html), you might need to react when a branch becomes expanded or collapsed.
For example, you might need to load or save data.

Two kinds of listeners report expansion and collapse occurrences:
*tree expansion* listeners and *tree-will-expand* listeners.
This page discusses *tree expansion* listeners.
See
[How to Write a Tree-Will-Expand
Listener](treewillexpandlistener.html) for a description of Tree-Will-Expand listeners.

A tree expansion listener detects when an expansion or collapse
has already occured.
In general, you should implement a tree expansion listener
unless you need to prevent an expansion or collapse from ocurring
.

This example demonstrates a simple tree expansion listener.
The text area at the bottom of the window
displays a message every time a tree expansion event occurs.
It's a straightforward, simple demo.
To see a more interesting version that can veto expansions, see
[How to Write a Tree-Will-Expand
Listener](treewillexpandlistener.html).

![TreeExpandEventDemo.html](../../figures/uiswing/events/TreeExpandEventDemo.png)

---

**Try this:**

1. Click the Launch button to run TreeExpandEventDemo using
   [Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp) ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
   Alternatively, to compile and run the example yourself,
   consult the
   [example index](../examples/events/index.html#TreeExpandEventDemo).

   [![Launches the TreeExpandEventDemo example](../../images/jws-launch-button.png)](http://download.oracle.com/javase/tutorialJWS/uiswing/events/ex6/TreeExpandEventDemo.jnlp)
   - Expand a node. A tree-expanded event is fired.- Collapse the node. A tree-collapsed event is fired.

---

The following code shows how the program handles expansion events.
You can find the source code for this example in
[`TreeExpandEventDemo.java`](../examples/events/TreeExpandEventDemoProject/src/events/TreeExpandEventDemo.java).

```

public class TreeExpandEventDemo ... {
    ...
    void saySomething(String eventDescription, TreeExpansionEvent e) {
        textArea.append(eventDescription + "; "
                        + "path = " + e.getPath()
                        + newline);
    }

    class DemoArea ... implements TreeExpansionListener {
        ...
        public DemoArea() {
            ...
            tree.addTreeExpansionListener(this);
            ...
        }
        ...
        // Required by TreeExpansionListener interface.
        public void treeExpanded(TreeExpansionEvent e) {
            saySomething("Tree-expanded event detected", e);
        }

        // Required by TreeExpansionListener interface.
        public void treeCollapsed(TreeExpansionEvent e) {
            saySomething("Tree-collapsed event detected", e);
        }
    }
}

```

### The Tree Expansion Listener API

> The TreeExpansionListener
> Interface
>
> *`TreeExpansionListener` has no adapter class.*
>
> | Method | Purpose |
> | --- | --- |
> | [treeCollapsed(TreeExpansionEvent)](http://download.oracle.com/javase/7/docs/api/javax/swing/event/TreeExpansionListener.html#treeCollapsed(javax.swing.event.TreeExpansionEvent)) | Called just after a tree node collapses. |
> | [treeExpanded(TreeExpansionEvent)](http://download.oracle.com/javase/7/docs/api/javax/swing/event/TreeExpansionListener.html#treeExpanded(javax.swing.event.TreeExpansionEvent)) | Called just after a tree node expands. |
>
> The TreeExpansionEvent API
>
> | Method | Purpose |
> | --- | --- |
> | [Object getSource()](http://download.oracle.com/javase/7/docs/api/java/util/EventObject.html#getSource()) | Return the object that fired the event. |
> | [TreePath getPath()](http://download.oracle.com/javase/7/docs/api/javax/swing/event/TreeExpansionEvent.html#getPath()) | Returns a [`TreePath`](http://download.oracle.com/javase/7/docs/api/javax/swing/tree/TreePath.html) object that identifies each node from the root of the tree to the collapsed/expanded node, inclusive. |

### Examples that Use Tree Expansion Listeners
> The following table lists the
> examples that use tree expansion listeners.
>
> | Example | Where Described | Notes |
> | --- | --- | --- |
> | [`TreeExpandEventDemo`](../examples/events/index.html#TreeExpandEventDemo) | This section | Displays a message whenever a tree expansion event occurs. |
> | [`TreeExpandEventDemo2`](../examples/events/index.html#TreeExpandEventDemo2) | [How to Write a Tree-Will-Expand Listener](treewillexpandlistener.html) | Adds a tree-will-expand listener to `TreeExpandEventDemo`. |

[« Previous](tablemodellistener.html)
•
[Trail](../TOC.html)
•
[Next »](treemodellistener.html)

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

**Previous page:** How to Write a Table Model Listener
  
**Next page:** How to Write a Tree Model Listener




A browser with JavaScript enabled is required for this page to operate properly.