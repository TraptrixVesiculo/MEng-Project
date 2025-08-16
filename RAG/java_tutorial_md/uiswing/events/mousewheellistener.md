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

How to Write a Mouse-Wheel Listener

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

[« Previous](mousemotionlistener.html) • [Trail](../TOC.html) • [Next »](propertychangelistener.html)

# How to Write a Mouse-Wheel Listener

Mouse-wheel events notify when the wheel on the mouse rotates.
For information on listening to other mouse
events, such as clicks, see [How
to Write a Mouse Listener](mouselistener.html). For information on listening
to mouse-dragged events, see
[How to Write a Mouse-Motion
Listener](mousemotionlistener.html).
Not all mice have wheels and, in that case, mouse-wheel events are never generated.
There is no way to programmatically detect whether the mouse
is equipped with a mouse wheel.

Alternatively, use the corresponding
[`MouseAdapter`](http://download.oracle.com/javase/7/docs/api/java/awt/event/MouseAdapter.html) AWT class, which implements the `MouseWheelListener` interface, to create a `MouseWheelEvent` and override the methods for the specific events.

Usually it is not necessary to implement a mouse-wheel listener because
the mouse wheel is used primarily for scrolling.
Scroll panes automatically register mouse-wheel listeners
that react to the mouse wheel appropriately.

However, to create a custom component to be used inside a
scroll pane you may need to customize
its scrolling behavior — specifically you might
need to set the unit and block increments.
For a text area, for example, scrolling one
unit means scrolling by one line of text.
A block increment typically scrolls an entire "page",
or the size of the viewport.
For more information, see
[Implementing a Scrolling-Savvy Client](../components/scrollpane.html#scrollable) in the
[How to Use Scroll Panes](../components/scrollpane.html) page.

To generate mouse-wheel events, the
cursor must be *over* the component registered to
listen for mouse-wheel events. The type of scrolling that occurs,
either `WHEEL_UNIT_SCROLL` or
`WHEEL_BLOCK_SCROLL`,
is platform dependent. The amount that the mouse wheel scrolls
is also platform dependent. Both the type and amount of scrolling
can be set via the mouse control panel for the platform.

The following example demonstrates mouse-wheel events.

![](../../figures/uiswing/events/MouseWheelEventDemo.png)

---

**Try this:**

1. Click the Launch button
   to run MouseWheelEventDemo using
   [Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp)
   ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
   Alternatively, to compile and run the example yourself,
   consult the
   [example index](../examples/events/index.html#MouseWheelEventDemo).

   [![Launches the MouseWheelEventDemo application](../../images/jws-launch-button.png)](http://download.oracle.com/javase/tutorialJWS/uiswing/events/ex6/MouseWheelEventDemo.jnlp)- Move the cursor over the text area.- Rotate the mouse wheel away from you.
       You will see one or more mouse-wheel events in
       the *up* direction.- Rotate the mouse wheel in the opposite direction.
         You will see mouse-wheel events in the *down*
         direction.- Try changing your mouse wheel's scrolling
           behavior your system's mouse control panel to see how
           the output changes. You should not need to restart the demo
           to see the changes take effect.

---

The output from MouseWheelEventDemo for a
system that uses unit increments for its mouse wheel
might look as follows:

```

javax.swing.JTextArea: Mouse wheel moved UP 1 notch(es)
    Scroll type: WHEEL_UNIT_SCROLL
    Scroll amount: 3 unit increments per notch
    Units to scroll: -3 unit increments
    Vertical unit increment: 16 pixels

```

The scroll amount, returned by the `getScrollAmount` method,
indicates how many units will be scrolled and always presents a positive
number. The units to scroll, returned by the `getUnitsToScroll` method,
are positive when scrolling down and negative when scrolling up.
The number of pixels for the vertical unit is obtained from the
vertical scroll bar using the `getUnitIncrement` method.
In the preceding example, rolling the mouse wheel one notch upward
should result in the text area scrolling upward 48 pixels (3x16).

For a system that uses block increments for mouse-wheel scrolling, for
the same movement of the mouse wheel the output might look as follows:

```

javax.swing.JTextArea: Mouse wheel moved UP 1 notch(es)
    Scroll type: WHEEL_BLOCK_SCROLL
    Vertical block increment: 307 pixels

```

The vertical block increment is obtained from the vertical
scroll bar using the `getBlockIncrement` method.
In this case, rolling the mouse wheel upward one notch means
that the text area should scroll upward 307 pixels.

Find the demo's code in the
[`MouseWheelEventDemo.java`](../examples/events/MouseWheelEventDemoProject/src/events/MouseWheelEventDemo.java) file. The following code snippet is related to the mouse-wheel event
handling:

```

public class MouseWheelEventDemo ... implements MouseWheelListener ... {
    public MouseWheelEventDemo() {
        //where initialization occurs:
        //Register for mouse-wheel events on the text area.
        textArea.addMouseWheelListener(this);
        ...
    }

    public void mouseWheelMoved(MouseWheelEvent e) {
       String message;
       int notches = e.getWheelRotation();
       if (notches < 0) {
           message = "Mouse wheel moved UP "
                        + -notches + " notch(es)" + newline;
       } else {
           message = "Mouse wheel moved DOWN "
                        + notches + " notch(es)" + newline;
       }
       if (e.getScrollType() == MouseWheelEvent.WHEEL_UNIT_SCROLL) {
           message += "    Scroll type: WHEEL_UNIT_SCROLL" + newline;
           message += "    Scroll amount: " + e.getScrollAmount()
                   + " unit increments per notch" + newline;
           message += "    Units to scroll: " + e.getUnitsToScroll()
                   + " unit increments" + newline;
           message += "    Vertical unit increment: "
               + scrollPane.getVerticalScrollBar().getUnitIncrement(1)
               + " pixels" + newline;
       } else { //scroll type == MouseWheelEvent.WHEEL_BLOCK_SCROLL
           message += "    Scroll type: WHEEL_BLOCK_SCROLL" + newline;
           message += "    Vertical block increment: "
               + scrollPane.getVerticalScrollBar().getBlockIncrement(1)
               + " pixels" + newline;
       }
       saySomething(message, e);
    }
    ...
}

```

### The Mouse Wheel Listener API

> The MouseWheelListener
> Interface
>
> *Although `MouseWheelListener` has only one method,
> it has the corresponding adapter class — `MouseAdapter`.
> This capability enables an application to have only one adapter class instance for the component to manage all types of events from the mouse pointer.*
>
> | Method | Purpose |
> | --- | --- |
> | [mouseWheelMoved(MouseWheelEvent)](http://download.oracle.com/javase/7/docs/api/java/awt/event/MouseWheelListener.html#mouseWheelMoved(java.awt.event.MouseWheelEvent)) | Called when the mouse wheel is rotated. |
>
> The MouseWheelEvent Class
>
> | Method | Purpose |
> | --- | --- |
> | [int getScrollType()](http://download.oracle.com/javase/7/docs/api/java/awt/event/MouseWheelEvent.html#getScrollType()) | Returns the type of scrolling to be used. Possible values are `WHEEL_BLOCK_SCROLL` and `WHEEL_UNIT_SCROLL`, and are determined by the native platform. |
> | [int getWheelRotation()](http://download.oracle.com/javase/7/docs/api/java/awt/event/MouseWheelEvent.html#getWheelRotation()) | Returns the number of notches the mouse wheel was rotated. If the mouse wheel rotated towards the user (down) the value is positive. If the mouse wheel rotated away from the user (up) the value is negative. |
> | [int getScrollAmount()](http://download.oracle.com/javase/7/docs/api/java/awt/event/MouseWheelEvent.html#getScrollAmount()) | Returns the number of units that should be scrolled per notch. This is always a positive number and is only valid if the scroll type is `MouseWheelEvent.WHEEL_UNIT_SCROLL`. |
> | [int getUnitsToScroll()](http://download.oracle.com/javase/7/docs/api/java/awt/event/MouseWheelEvent.html#getUnitsToScroll()) | Returns the positive or negative units to scroll for the current event. This is only valid when the scroll type is `MouseWheelEvent.WHEEL_UNIT_SCROLL`. |

### Examples That Use Mouse Wheel Listeners
> The following table lists the
> examples that use mouse-wheel listeners.
>
> | Example | Where Described | Notes |
> | --- | --- | --- |
> | [`MouseWheelEventDemo`](../examples/events/index.html#MouseWheelEventDemo) | This section | Reports all mouse wheel events that occur within a text area to demonstrate the circumstances under which mouse wheel events are fired. |

[« Previous](mousemotionlistener.html)
•
[Trail](../TOC.html)
•
[Next »](propertychangelistener.html)

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

**Previous page:** How to Write a Mouse-Motion Listener
  
**Next page:** How to Write a Property Change Listener




A browser with JavaScript enabled is required for this page to operate properly.