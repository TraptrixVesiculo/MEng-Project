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

How to Write a Tree-Will-Expand Listener

[How to Write an Undoable Edit Listener](undoableeditlistener.html)

[How to Write Window Listeners](windowlistener.html)

[Listener API Table](api.html)

[Solving Common Event-Handling Problems](problems.html)

[Home Page](../../index.html)
>
[Creating a GUI With JFC/Swing](../index.html)
>
[Writing Event Listeners](index.html)

[« Previous](treeselectionlistener.html) • [Trail](../TOC.html) • [Next »](undoableeditlistener.html)

# How to Write a Tree-Will-Expand Listener

The  *tree-will-expand* listener
prevents a
[tree](../components/tree.html) node from expanding or collapsing.
To be notified just *after* an expansion or collapse occurs,
you should use a
*tree expansion listener* instead.

This demo adds a tree-will-expand listener
to the `TreeExpandEventDemo` example
discussed in [How to
Write a Tree Expansion Listener](treeexpansionlistener.html). The code added here
demonstrates that *tree-will-expand* listeners prevent node expansions and collapses: The listener will prompt you for confirmation each time you try to expand a node.

![TreeExpandEventDemo2.html](../../figures/uiswing/events/TreeExpandEventDemo2.png)

---

**Try this:**

1. Click the Launch button to run TreeExpandEventDemo2 using
   [Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp) ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
   Alternatively, to compile and run the example yourself,
   consult the
   [example index](../examples/events/index.html#TreeExpandEventDemo2).

   [![Launches the TreeExpandEventDemo2 example](../../images/jws-launch-button.png)](http://download.oracle.com/javase/tutorialJWS/uiswing/events/ex6/TreeExpandEventDemo2.jnlp)
   - Click the graphic to the left of the **Potrero Hill**
     node. This tells the tree that you want to expand the node.
       
     A dialog appears asking you whether you really want
     to expand the node.- Click "Expand" or dismiss the dialog.
         
       Messages in the text area tell you that both a tree-will-expand event
       and a tree-expanded event have occurred.
       At the end of each message is the path to the expanded node.- Try to expand another node,
         but this time press the "Cancel Expansion" button in the dialog.
           
         The node does not expand.
         Messages in the text area tell you that a tree-will-expand event
         occurred,
         and that you cancelled a tree expansion.- Collapse the **Potrero Hill** node.
             
           The node collapses without a dialog appearing,
           because the event handler's
           `treeWillCollapse` method
           lets the collapse occur, uncontested.

---

The following snippet shows the code
that this program adds to `TreeExpandEventDemo`.
The bold line prevents the tree expansion from happening.
You can find all the demo's source code in
[`TreeExpandEventDemo2.java`](../examples/events/TreeExpandEventDemo2Project/src/events/TreeExpandEventDemo2.java).

```

public class TreeExpandEventDemo2 ... {
    ...
    class DemoArea ... implements ... TreeWillExpandListener {
        ...
        public DemoArea() {
            ...
            tree.addTreeWillExpandListener(this);
            ...
        }
        ...
        //Required by TreeWillExpandListener interface.
        public void treeWillExpand(TreeExpansionEvent e) 
                    throws ExpandVetoException {
            saySomething("Tree-will-expand event detected", e);
            //...show a dialog...
            if (/* user said to cancel the expansion */) {
                //Cancel expansion.
                saySomething("Tree expansion cancelled", e);
                throw new ExpandVetoException(e);
            }
        }

        //Required by TreeWillExpandListener interface.
        public void treeWillCollapse(TreeExpansionEvent e) {
            saySomething("Tree-will-collapse event detected", e);
        }
        ...
    }
}

```

### The Tree-Will-Expand Listener API

> The TreeWillExpandListener
> Interface
>
> *`TreeWillExpandListener` has no adapter class.*
>
> | Method | Purpose |
> | --- | --- |
> | [treeWillCollapse(TreeExpansionEvent)](http://download.oracle.com/javase/7/docs/api/javax/swing/event/TreeWillExpandListener.html#treeWillCollapse(javax.swing.event.TreeExpansionEvent)) | Called just before a tree node collapses. To prevent the collapse from occurring, your implementation of this method should throw a [`ExpandVetoException`](http://download.oracle.com/javase/7/docs/api/javax/swing/tree/ExpandVetoException.html) event. |
> | [treeWillExpand(TreeExpansionEvent)](http://download.oracle.com/javase/7/docs/api/javax/swing/event/TreeWillExpandListener.html#treeWillExpand(javax.swing.event.TreeExpansionEvent)) | Called just before a tree node expands. To prevent the expansion from occurring, your implementation of this method should throw a [`ExpandVetoException`](http://download.oracle.com/javase/7/docs/api/javax/swing/tree/ExpandVetoException.html) event. |
>
> See [The Tree Expansion
> Event API](treeexpansionlistener.html#api)
> for information about the
> [`TreeExpansionEvent`](http://download.oracle.com/javase/7/docs/api/javax/swing/event/TreeExpansionEvent.html) argument for the preceding methods.

### Examples that Use Tree-Will-Expand Listeners
> [`TreeExpandEventDemo2`](../examples/events/index.html#TreeExpandEventDemo2),
> featured in this section,
> is our only example that uses a tree-will-expand listener.

[« Previous](treeselectionlistener.html)
•
[Trail](../TOC.html)
•
[Next »](undoableeditlistener.html)

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

**Previous page:** How to Write a Tree Selection Listener
  
**Next page:** How to Write an Undoable Edit Listener




A browser with JavaScript enabled is required for this page to operate properly.