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

How to Write an Internal Frame Listener

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

[« Previous](focuslistener.html) • [Trail](../TOC.html) • [Next »](itemlistener.html)

# How to Write an Internal Frame Listener

An `InternalFrameListener` is similar to a
`WindowListener`. Like the window listener,
the internal frame listener listens for events that
occur when the "window" has been shown for the first time,
disposed of, iconified, deiconified, activated, or deactivated.
Before using an internal frame listener,
please familiarize yourself with
the `WindowListener` interface in
[How to Write Window Listeners](windowlistener.html).

The application shown in the following figure
demonstrates internal frame events.
The application listens for internal frame events
from the Event Generator frame,
displaying a message that describes each event.

![A window which demonstrates internal frame events that are fired by Event Generator frame](../../figures/uiswing/events/InternalFrameEventDemo.png)

---

**Try this:**

1. Click the Launch button to run InternalFrameEventDemo using
   [Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp) ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
   Alternatively, to compile and run the example yourself, consult the
   [example index](../examples/events/index.html#InternalFrameEventDemo).
    [![Launches the InternalFrameEventDemo example](../../images/jws-launch-button.png )](http://download.oracle.com/javase/tutorialJWS/uiswing/events/ex6/InternalFrameEventDemo.jnlp) - Bring up the Event Generator internal frame
     by clicking the **Show internal frame** button.
       
     You should see an "Internal frame opened" message
     in the display area.- Try various operations to see what happens.
       For example, click the Event Generator
       so that it gets activated.
       Click the Event Watcher so that the
       Event Generator gets deactivated.
       Click the Event Generator's decorations to
       iconify, maximize, minimize, and close the window.
         
       See [How to Write Window Listeners](windowlistener.html)
       for information on what kinds of events you will see.

---

Here is the internal frame event handling code:

```

public class InternalFrameEventDemo ...
		     implements InternalFrameListener ... {
    ...

    public void internalFrameClosing(InternalFrameEvent e) {
	displayMessage("Internal frame closing", e);
    }

    public void internalFrameClosed(InternalFrameEvent e) {
	displayMessage("Internal frame closed", e);
	listenedToWindow = null;
    }

    public void internalFrameOpened(InternalFrameEvent e) {
	displayMessage("Internal frame opened", e);
    }

    public void internalFrameIconified(InternalFrameEvent e) {
	displayMessage("Internal frame iconified", e);
    }

    public void internalFrameDeiconified(InternalFrameEvent e) {
	displayMessage("Internal frame deiconified", e);
    }

    public void internalFrameActivated(InternalFrameEvent e) {
	displayMessage("Internal frame activated", e);
    }

    public void internalFrameDeactivated(InternalFrameEvent e) {
	displayMessage("Internal frame deactivated", e);
    }

    void displayMessage(String prefix, InternalFrameEvent e) {
	String s = prefix + ": " + e.getSource(); 
	display.append(s + newline);
    }

    public void actionPerformed(ActionEvent e) {
	if (SHOW.equals(e.getActionCommand())) {
	    ...
	    if (listenedToWindow == null) {
	        listenedToWindow = new JInternalFrame("Event Generator",
	        				      true,  //resizable
	        				      true,  //closable
	        				      true,  //maximizable
	        				      true); //iconifiable
                //We want to reuse the internal frame, so we need to
                //make it hide (instead of being disposed of, which is
                //the default) when the user closes it.
        	listenedToWindow.setDefaultCloseOperation(
        				WindowConstants.HIDE_ON_CLOSE);

	        listenedToWindow.addInternalFrameListener(this);
	        ...
	    }
	} 
	...
    }
}

```

### The Internal Frame Listener API

> The InternalFrameListener
> Interface
>
> *The corresponding adapter class is
> [`InternalFrameAdapter`](http://download.oracle.com/javase/7/docs/api/javax/swing/event/InternalFrameAdapter.html).*
>
> | Method | Purpose |
> | --- | --- |
> | [internalFrameOpened(InternalFrameEvent)](http://download.oracle.com/javase/7/docs/api/javax/swing/event/InternalFrameListener.html#internalFrameOpened(javax.swing.event.InternalFrameEvent)) | Called just after the listened-to internal frame has been shown for the first time. |
> | [internalFrameClosing(InternalFrameEvent)](http://download.oracle.com/javase/7/docs/api/javax/swing/event/InternalFrameListener.html#internalFrameClosing(javax.swing.event.InternalFrameEvent)) | Called in response to a user request that the listened-to internal frame be closed. By default, `JInternalFrame` hides the window when the user closes it. You can use the `JInternalFrame` `setDefaultCloseOperation` method to specify another option, which must be either `DISPOSE_ON_CLOSE` or `DO_NOTHING_ON_CLOSE` (both defined in `WindowConstants`, an interface that `JInternalFrame` implements). Or by implementing an `internalFrameClosing` method in the internal frame's listener, you can add custom behavior (such as bringing up dialogs or saving data) to internal frame closing. |
> | [internalFrameClosed(InternalFrameEvent)](http://download.oracle.com/javase/7/docs/api/javax/swing/event/InternalFrameListener.html#internalFrameClosed(javax.swing.event.InternalFrameEvent)) | Called just after the listened-to internal frame has been disposed of. |
> | [internalFrameIconified(InternalFrameEvent)](http://download.oracle.com/javase/7/docs/api/javax/swing/event/InternalFrameEvent.html#internalFrameIconified(javax.swing.event.InternalFrameEvent))  [internalFrameDeiconified(InternalFrameEvent)](http://download.oracle.com/javase/7/docs/api/javax/swing/event/InternalFrameEvent.html#internalFrameDeiconified(javax.swing.event.InternalFrameEvent)) | Called just after the listened-to internal frame is iconified or deiconified, respectively. |
> | [internalFrameActivated(InternalFrameEvent)](http://download.oracle.com/javase/7/docs/api/javax/swing/event/InternalFrameListener.html#internalFrameActivated(javax.swing.event.InternalFrameEvent))  [internalFrameDeactivated(InternalFrameEvent)](http://download.oracle.com/javase/7/docs/api/javax/swing/event/InternalFrameListener.html#internalFrameDeactivated(javax.swing.event.InternalFrameEvent)) | Called just after the listened-to internal frame is activated or deactivated, respectively. |
>
> Each internal frame event method has a single parameter: an
> [`InternalFrameEvent`](http://download.oracle.com/javase/7/docs/api/javax/swing/event/InternalFrameEvent.html) object.
> The `InternalFrameEvent` class defines no generally
> useful methods. To get the internal frame that fired the event,
> use the `getSource` method,
> which `InternalFrameEvent` inherits from
> `java.util.EventObject`.

### Examples that Use Internal Frame Listeners
> No other source files currently contain internal frame listeners.
> However, internal frame listeners are very similar to
> `WindowListener`s and several Swing programs have
> window listeners:
>
> | Example | Where Described | Notes |
> | --- | --- | --- |
> | [`InternalFrameEventDemo`](../examples/events/index.html#InternalFrameEventDemo) | This section | Reports all internal frame events that occur on one internal frame to demonstrate the circumstances under which internal frame events are fired. |
> | [`DialogDemo`](../examples/components/index.html#DialogDemo) | [Text Component Features](../components/generaltext.html) | [`CustomDialog.java`](../examples/components/DialogDemoProject/src/components/CustomDialog.java) uses `setDefaultCloseOperation` instead of a window listener to determine what action to take when the user closes the window. |
> | [`SliderDemo`](../examples/components/index.html#SliderDemo) | [How to Use Sliders](../components/slider.html) | Listens for window iconify and deiconify events, so that it can stop the animation when the window is not visible. |

[« Previous](focuslistener.html)
•
[Trail](../TOC.html)
•
[Next »](itemlistener.html)

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

**Previous page:** How to Write a Focus Listener
  
**Next page:** How to Write an Item Listener




A browser with JavaScript enabled is required for this page to operate properly.