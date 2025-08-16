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

How to Write a Mouse-Motion Listener

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

[« Previous](mouselistener.html) • [Trail](../TOC.html) • [Next »](mousewheellistener.html)

# How to Write a Mouse-Motion Listener

Mouse-motion events notify when the user uses the mouse
(or a similar input device) to move the onscreen cursor.
For information on listening for other kinds of mouse events,
such as clicks,
see [How to Write a Mouse Listener](mouselistener.html).
For information on listening for mouse-wheel events,
see [How to Write a Mouse
Wheel Listener](mousewheellistener.html).

If an application requires the detection of both mouse events
and mouse-motion events,
use the
[`MouseInputAdapter`](http://download.oracle.com/javase/7/docs/api/javax/swing/event/MouseInputAdapter.html) class, which implements the
[`MouseInputListener`](http://download.oracle.com/javase/7/docs/api/javax/swing/event/MouseInputListener.html) a convenient interface that
implements both the `MouseListener` and
`MouseMotionListener` interfaces.

Alternatively, use the corresponding
[`MouseAdapter`](http://download.oracle.com/javase/7/docs/api/java/awt/event/MouseAdapter.html) AWT class, which implements the `MouseMotionListener interface, to create a MouseMotionEvent and override the methods for the specific events.

The following demo code contains a mouse-motion listener.
This demo is exactly the same as the demo described in the
How to Write a Mouse Listener section,
except for substituting the MouseMotionListener interface
for the MouseListener interface.
Additionally, MouseMotionEventDemo implements the mouseDragged and
mouseMoved methods
instead of the mouse listener methods,
and displays coordinates instead of numbers of clicks.

![MouseMotionEventDemo screen shot](../../figures/uiswing/events/MouseMotionEventDemo.png)

---

Try this:

1. Click the Launch button
   to run MouseMotionEventDemo using
   Java™ Web Start
   (download JDK 6).
   Alternatively, to compile and run the example yourself,
   consult the
   example index.

   ![Launches the MouseMotionEventDemo application](../../images/jws-launch-button.png)- Move the cursor into the yellow rectangle
     at the top of the window.
       
     You will see one or more mouse-moved events.- Press and hold the mouse button,
       and then move the mouse so that the cursor
       is outside the yellow rectangle.
         
       You will see mouse-dragged events.

---

You can find the demo's code in
MouseMotionEventDemo.java
and
BlankArea.java.
The following code snippet from MouseMotionEventDemo
implements the mouse-motion event handling:

```

public class MouseMotionEventDemo extends JPanel 
                                  implements MouseMotionListener {
    //...in initialization code:
        //Register for mouse events on blankArea and panel.
        blankArea.addMouseMotionListener(this);
        addMouseMotionListener(this);
        ...
    }

    public void mouseMoved(MouseEvent e) {
       saySomething("Mouse moved", e);
    }

    public void mouseDragged(MouseEvent e) {
       saySomething("Mouse dragged", e);
    }

    void saySomething(String eventDescription, MouseEvent e) {
        textArea.append(eventDescription 
                        + " (" + e.getX() + "," + e.getY() + ")"
                        + " detected on "
                        + e.getComponent().getClass().getName()
                        + newline);
    }
}

```

The SelectionDemo example,
draws a rectangle illustrating the user's current dragging.
To draw the rectangle, the application must implement an event handler for three kinds of mouse events:
mouse presses, mouse drags, and mouse releases.
To be informed of all these events,
the handler must implement both the
MouseListener and
MouseMotionListener interfaces,
and be registered as both a mouse listener and
a mouse-motion listener.
To avoid having to define empty methods,
the handler doesn't implement either listener interface directly.
Instead, it extends MouseInputAdapter,
as the following code snippet shows.

```

...//where initialization occurs:
    MyListener myListener = new MyListener();
    addMouseListener(myListener);
    addMouseMotionListener(myListener);
...
private class MyListener extends MouseInputAdapter {
    public void mousePressed(MouseEvent e) {
        int x = e.getX();
        int y = e.getY();
        currentRect = new Rectangle(x, y, 0, 0);
        updateDrawableRect(getWidth(), getHeight());
        repaint();
    }

    public void mouseDragged(MouseEvent e) {
        updateSize(e);
    }

    public void mouseReleased(MouseEvent e) {
        updateSize(e);
    }

    void updateSize(MouseEvent e) {
        int x = e.getX();
        int y = e.getY();
        currentRect.setSize(x - currentRect.x,
                            y - currentRect.y);
        updateDrawableRect(getWidth(), getHeight());
        Rectangle totalRepaint = rectToDraw.union(previouseRectDrawn); 
        repaint(totalRepaint.x, totalRepaint.y,
                totalRepaint.width, totalRepaint.height);
    }
}

```

### The Mouse-Motion Listener API

> The MouseMotionListener
> Interface
>
> The corresponding adapter classes are
> MouseMotionAdapter and
> MouseAdapter.
>
> | Method | Purpose |
> | --- | --- |
> | mouseDragged(MouseEvent) | Called in response to the user moving the mouse while holding a mouse button down. This event is fired by the component that fired the most recent mouse-pressed event, even if the cursor is no longer over that component. |
> | mouseMoved(MouseEvent) | Called in response to the user moving the mouse with no mouse buttons pressed. This event is fired by the component that's currently under the cursor. |
>
> Each mouse-motion event method has a single parameter —
> and it's not called MouseMotionEvent!
> Instead, each mouse-motion event method uses a
> MouseEvent argument.
> See The MouseEvent API
> for information about using MouseEvent objects.

### Examples That Use Mouse-Motion Listeners

> The following table lists the
> examples that use mouse-motion listeners.
>
> | Example | Where Described | Notes |
> | --- | --- | --- |
> | MouseMotionEventDemo | This section | Reports all mouse motion events that occur within a blank panel to demonstrate the circumstances under which mouse motion events are fired. |
> | LayeredPaneDemo and   LayeredPaneDemo2 | How to Use Layered Panes | Moves an image of Duke around within a layered pane in response to mouse motion events. |
> | SelectionDemo |  | Lets the user drag a rectangle to select a portion of an image. Uses a subclass of MouseInputAdapter to listen to both mouse events and mouse-motion events. |
> | GlassPaneDemo | How to Use Root Panes | Uses a subclass of MouseInputAdapter to listen to mouse events and mouse-motion events on the root pane's glass pane. Redispatches the events to underlying components. |
> | ScrollDemo | How to Use Scroll Panes | The label subclass, ScrollablePicture, uses a mouse-motion listener to allow the user to scroll the picture even when the user drags the cursor outside the window. |`

[« Previous](mouselistener.html)
•
[Trail](../TOC.html)
•
[Next »](mousewheellistener.html)

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

**Previous page:** How to Write a Mouse Listener
  
**Next page:** How to Write a Mouse-Wheel Listener




A browser with JavaScript enabled is required for this page to operate properly.