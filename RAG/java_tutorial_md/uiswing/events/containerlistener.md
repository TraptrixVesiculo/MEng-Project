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

How to Write a Container Listener

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

[« Previous](componentlistener.html) • [Trail](../TOC.html) • [Next »](documentlistener.html)

# How to Write a Container Listener

Container events are fired
by a `Container`
just after a component
is added to or removed from the container.
These events are for notification only —
no container listener need be present
for components to be successfully added or removed.

The following example demonstrates container events.
By clicking **Add a button** or **Remove a button**,
you can add buttons to or remove them from
a panel at the bottom of the window.
Each time a button is added to or removed from the panel,
the panel fires a container event,
and the panel's container listener is notified.
The listener displays descriptive messages
in the text area at the top of the window.

![A screenshot which demonstrates container events](../../figures/uiswing/events/ContainerEventDemo.png)

---

**Try this:**

1. Click the Launch button to run ContainerEventDemo using
   [Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp) ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
   Alternatively, to compile and run the example yourself, consult the
   [example index](../examples/events/index.html#ContainerEventDemo).
    [![Launches the ContainerEventDemo example](../../images/jws-launch-button.png )](http://download.oracle.com/javase/tutorialJWS/uiswing/events/ex6/ContainerEventDemo.jnlp) - Click the button labeled **Add a button**.
       
     You will see a button appear near the bottom of the window.
     The container listener reacts to the resulting component-added event
     by displaying "JButton #1 was added to javax.swing.JPanel"
     at the top of the window.- Click the button labeled **Remove a button**.
         
       This removes the most recently added button
       from the panel,
       causing the container listener
       to receive a component-removed event.

---

You can find the demo's code in
[`ContainerEventDemo.java`](../examples/events/ContainerEventDemoProject/src/events/ContainerEventDemo.java).
Here is the demo's container event handling code:

```

public class ContainerEventDemo ... implements ContainerListener ... {
    ...//where initialization occurs:
	buttonPanel = new JPanel(new GridLayout(1,1));
	buttonPanel.addContainerListener(this);
    ...
    public void componentAdded(ContainerEvent e) {
	displayMessage(" added to ", e);
    }

    public void componentRemoved(ContainerEvent e) {
	displayMessage(" removed from ", e);
    }

    void displayMessage(String action, ContainerEvent e) {
	display.append(((JButton)e.getChild()).getText()
		       + " was"
		       + action
		       + e.getContainer().getClass().getName()
		       + newline);
    }
    ...
}

```

### The Container Listener API

> The ContainerListener
> Interface
>
> *The corresponding adapter class is
> [`ContainerAdapter`](http://download.oracle.com/javase/7/docs/api/java/awt/event/ContainerAdapter.html).*
>
> | Method | Purpose |
> | --- | --- |
> | [componentAdded(ContainerEvent)](http://download.oracle.com/javase/7/docs/api/java/awt/event/ContainerListener.html#componentAdded(java.awt.event.ContainerEvent)) | Called just after a component is added to the listened-to container. |
> | [componentRemoved(ContainerEvent)](http://download.oracle.com/javase/7/docs/api/java/awt/event/ContainerListener.html#componentRemoved(java.awt.event.ContainerEvent)) | Called just after a component is removed from the listened-to container. |
>
> The ContainerEvent Class
>
> | Method | Purpose |
> | --- | --- |
> | [Component getChild()](http://download.oracle.com/javase/7/docs/api/java/awt/event/ContainerEvent.html#getChild()) | Returns the component whose addition or removal triggered this event. |
> | [Container getContainer()](http://download.oracle.com/javase/7/docs/api/java/awt/event/ContainerEvent.html#getContainer()) | Returns the container that fired this event. You can use this instead of the `getSource` method. |

### Examples that Use Container Listeners
> The following table lists the
> examples that use container listeners.
>
> | Example | Where Described | Notes |
> | --- | --- | --- |
> | [`ContainerEventDemo`](../examples/events/index.html#ContainerEventDemo) | This section | Reports all container events that occur on a single panel to demonstrate the circumstances under which container events are fired. |

[« Previous](componentlistener.html)
•
[Trail](../TOC.html)
•
[Next »](documentlistener.html)

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

**Previous page:** How to Write a Component Listener
  
**Next page:** How to Write a Document Listener




A browser with JavaScript enabled is required for this page to operate properly.