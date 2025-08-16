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

How to Write a Focus Listener

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

[« Previous](documentlistener.html) • [Trail](../TOC.html) • [Next »](internalframelistener.html)

# How to Write a Focus Listener

Focus events are fired whenever a component gains or
loses the keyboard focus.
This is true whether the change in focus occurs
through the mouse, the keyboard, or programmatically.
To get familiar with basic focus concepts or to obtain
detailed information about focus, see
[How to Use the Focus Subsystem](../misc/focus.html).

This section explains how to get focus events for a
particular component by registering a `FocusListener` instance
on it. To get focus for a window only, implement a
[`WindowFocusListener`](windowlistener.html) instance
instead. To obtain the focus status of many
components, consider implementing a `PropertyChangeListener` instance
on the `KeyboardFocusManager` class, as described in
[Tracking Focus Changes to Multiple Components](../misc/focus.html#trackingFocus) in
[How to Use the Focus Subsystem](../misc/focus.html).

The following example demonstrates focus events.
The window displays a variety of components.
A focus listener, registered on each component,
reports every focus-gained and focus-lost event.
For each event, the other component involved
in the focus change, the *opposite component*,
is reported. For example, when the focus
goes from a button to a text field, a focus-lost
event is fired by the button (with the text field as
the opposite component) and then a focus-gained
event is fired by the text field (with the button as the
opposite component).
Focus-lost as well as focus-gained events can be temporary.
For example, a temporary focus-lost event occurs when the window loses the focus.
A temporary focus-gained event occurs on popup menus.

![The Focus Event Window, which demonstrates the events that are fired when the keyboard focus changes.](../../figures/uiswing/events/FocusEventDemoWindow.png)

---

**Try this:**

1. Click the Launch button
   to run FocusEventDemo using
   [Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp)
   ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
   Alternatively, to compile and run the example yourself,
   consult the
   [example index](../examples/events/index.html#FocusEventDemo).

   [![Launches the FocusEventDemo application](../../images/jws-launch-button.png)](http://download.oracle.com/javase/tutorialJWS/uiswing/events/ex6/FocusEventDemo.jnlp)- You will see a "Focus gained: JTextField" message
     in the text area — its "opposite component" is
     null, since it is the first component to have the focus.- Click the label. Nothing happens because the label,
       by default, cannot get the focus.- Click the combo box. A focus-lost event is fired by
         the text field and a focus-gained event by the combo box.
         The combo box now shows that it has the focus, perhaps with
         a dotted line around the text — exactly how this is
         represented is look and feel dependent.
           
         Notice that when the focus changes from one component to another,
         the first component fires a focus-lost event
         before the second component fires a focus-gained event.- Select a choice from the combo box's menu. Click the
           combo box again. Notice that no focus event is
           reported. As long as the user manipulates
           the same component, the focus stays on that component.- Click the text area where the focus events are printed.
             Nothing happens because the text area has been rendered
             unclickable with `setRequestFocusEnabled(false)`.- Click the text field to return the focus to the
               initial component.- Press Tab on the keyboard. The focus moves to the combo box
                 and skips over the label.- Press Tab again. The focus moves to the button.- Click another window so that the FocusEventDemo window
                     loses the focus. A temporary focus-lost event is
                     generated for the button.- Click the top of the FocusEventDemo window.
                       A focus-gained event is fired by the button.- Press Tab on the keyboard. The focus moves to the list.- Press Tab again. The focus moves to the text area.
                             
                           Notice that even though you are not allowed to click on the text area,
                           you can tab to it. This is so users who use
                           [assistive technologies](../misc/access.html) can determine that a component is there and what it contains.
                           The demo disables click-to-focus for the text area,
                           while retaining its tab-to-focus capability,
                           by invoking `setRequestFocusEnabled(false)`
                           on the text area. The demo could use
                           `setFocusable(false)` to truly remove the
                           text area from the focus cycle, but that would have
                           the unfortunate effect of making the component
                           unavailable to those who use assistive technologies.- Press Tab again. The focus moves from the list back to
                             the text field. You have just completed a *focus
                             cycle*. See the
                             [introduction](../misc/focus.html#intro) in
                             [How to Use the Focus Subsystem](../misc/focus.html) for a discussion of focus terminology and concepts.

---

The complete code for this demo is in the
[`FocusEventDemo.java`](../examples/events/FocusEventDemoProject/src/events/FocusEventDemo.java) file.
The following code snippet represents the focus-event handling mechanism:

```

public class FocusEventDemo ... implements FocusListener ... {
    public FocusEventDemo() {
        ...
        JTextField textField = new JTextField("A TextField");
        textField.addFocusListener(this);
        ...
	JLabel label = new JLabel("A Label");
	label.addFocusListener(this);
        ...
        JComboBox comboBox = new JComboBox(vector);
        comboBox.addFocusListener(this);
        ...
        JButton button = new JButton("A Button");
        button.addFocusListener(this);
        ...
        JList list = new JList(listVector);
        list.setSelectedIndex(1); //It's easier to see the focus change
                                  //if an item is selected.
        list.addFocusListener(this);
        JScrollPane listScrollPane = new JScrollPane(list);
        
        ...

        //Set up the area that reports focus-gained and focus-lost events.
        display = new JTextArea();
        display.setEditable(false);
        //The method setRequestFocusEnabled prevents a
        //component from being clickable, but it can still
        //get the focus through the keyboard - this ensures
        //user accessibility.
        display.setRequestFocusEnabled(false);
        display.addFocusListener(this);
        JScrollPane displayScrollPane = new JScrollPane(display);

        ...
    }
    ...
    public void focusGained(FocusEvent e) {
	displayMessage("Focus gained", e);
    }

    public void focusLost(FocusEvent e) {
	displayMessage("Focus lost", e);
    }

    void displayMessage(String prefix, FocusEvent e) {
	display.append(prefix
                       + (e.isTemporary() ? " (temporary):" : ":")
                       +  e.getComponent().getClass().getName()
                       + "; Opposite component: " 
                       + (e.getOppositeComponent() != null ?
                          e.getOppositeComponent().getClass().getName() : "null")
		       + newline); 
    }
    ...
}

```

### The Focus Listener API

> The FocusListener
> Interface
>
> *The corresponding adapter class is
> [`FocusAdapter`](http://download.oracle.com/javase/7/docs/api/java/awt/event/FocusAdapter.html).*
>
> | Method | Purpose |
> | --- | --- |
> | [focusGained(FocusEvent)](http://download.oracle.com/javase/7/docs/api/java/awt/event/FocusListener.html#focusGained(java.awt.event.FocusEvent)) | Called just after the listened-to component gets the focus. |
> | [focusLost(FocusEvent)](http://download.oracle.com/javase/7/docs/api/java/awt/event/FocusListener.html#focusLost(java.awt.event.FocusEvent)) | Called just after the listened-to component loses the focus. |
>
> The FocusEvent API
>
> | Method | Purpose |
> | --- | --- |
> | [boolean isTemporary()](http://download.oracle.com/javase/7/docs/api/java/awt/event/FocusEvent.html#isTemporary()) | Returns the true value if a focus-lost or focus-gained event is temporary. |
> | [Component getComponent()](http://download.oracle.com/javase/7/docs/api/java/awt/event/ComponentEvent.html#getComponent()) (*in `java.awt.event.ComponentEvent`*) | Returns the component that fired the focus event. |
> | [Component getOppositeComponent()](http://download.oracle.com/javase/7/docs/api/java/awt/event/FocusEvent.html#getOppositeComponent()) | Returns the other component involved in the focus change. For a `FOCUS_GAINED` event, this is the component that lost the focus. For a `FOCUS_LOST` event, this is the component that gained the focus. If the focus change involves a native application, a Java application in a different VM or context, or no other component, then `null` is returned. |

### Examples that Use Focus Listeners
> The following table lists the
> examples that use focus listeners.
>
> | Example | Where Described | Notes |
> | --- | --- | --- |
> | [`FocusEventDemo`](../examples/events/index.html#FocusEventDemo) | This section | Reports all focus events that occur on several components to demonstrate the circumstances under which focus events are fired. |
> | [`TrackFocusDemo`](../examples/misc/index.html#TrackFocusDemo) | [How to Use the Focus Subsystem](../misc/focus.html) | The custom component, [`Picture`](../examples/misc/TrackFocusDemoProject/src/misc/Picture.java), implements a focus listener to draw a red border around the component when it is the current focus owner. |

[« Previous](documentlistener.html)
•
[Trail](../TOC.html)
•
[Next »](internalframelistener.html)

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

**Previous page:** How to Write a Document Listener
  
**Next page:** How to Write an Internal Frame Listener




A browser with JavaScript enabled is required for this page to operate properly.