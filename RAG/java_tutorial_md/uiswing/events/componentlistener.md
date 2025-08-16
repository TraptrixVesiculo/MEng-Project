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

How to Write a Component Listener

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

[« Previous](changelistener.html) • [Trail](../TOC.html) • [Next »](containerlistener.html)

# How to Write a Component Listener

The Component listener is a listener interface for receiving component events. A component is an object having a graphical representation that can be displayed on the screen and that can interact with the user. Some of the examples of components are the buttons, checkboxes, and scrollbars of a typical graphical user interface.

The class that is interested in processing a component event either implements this interface and all the methods it contains, or extends the abstract ComponentAdapter class overriding only the methods of interest. The listener object created from that class is then registered with a component using the component's addComponentListener method. When the component's size, location, or visibility changes, the relevant method in the listener object is invoked, and the ComponentEvent is passed to it.

One or more component events are fired
by a `Component` object
just after the component is hidden, made visible, moved, or resized.

The component-hidden and component-shown events
occur only as the result of calls to a `Component` 's
`setVisible` method.
For example, a window might be miniaturized into an icon (iconified)
without a component-hidden event being fired.

To write a simple Component listener program, follow the steps mentioned below:

* Declare a class which implements Component listener. For example:

  ```

  public class ComponentEventDemo ... implements ComponentListener

  ```

  * Identify the components that you would like to catch the events for. For example: pane, label, checkbox, etc.
  * Add the Component Listener to the identified components. For example:

    ```

    ....
    label.addComponentListener(this);
    .....
    checkbox.addComponentListener(this);
    ....
    panel.addComponentListener(this);
    ...
    frame.addComponentListener(this);

    ```
  * Finally, catch the different events of these components by using four methods of Component Listener as shown below:

    ```

    public void componentHidden(ComponentEvent e) {
            displayMessage(e.getComponent().getClass().getName() + " --- Hidden");
        }

        public void componentMoved(ComponentEvent e) {
            displayMessage(e.getComponent().getClass().getName() + " --- Moved");
        }

        public void componentResized(ComponentEvent e) {
            displayMessage(e.getComponent().getClass().getName() + " --- Resized ");            
        }

        public void componentShown(ComponentEvent e) {
            displayMessage(e.getComponent().getClass().getName() + " --- Shown");

        }

    ```

  The following example demonstrates component events.
  The window contains a panel that has a label and a check box.
  The check box controls whether the label is visible.
  A text area displays a message every time
  the window, panel, label, or check box
  fires a component event.

  ![A window demonstrating component events](../../figures/uiswing/events/ComponentEventDemo.png)

  ---

  **Try this:**
  1. Click the Launch button to run ComponentEventDemo using
     [Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp) ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
     Alternatively, to compile and run the example yourself, consult the
     [example index](../examples/events/index.html#Beeper).
      [![Launches the ComponentEventDemo example](../../images/jws-launch-button.png )](http://download.oracle.com/javase/tutorialJWS/uiswing/events/ex6/ComponentEventDemo.jnlp) 

     * When the window appears, one or more component-shown
       events have been fired.* Click the check box to hide the label.
           
         The label fires a component-hidden event.
         The panel fires component-moved and component-resized events.
         The check box fires a component-moved event.* Click the check box again to show the label.
             
           The label fires a component-shown event.
           The panel fires component-moved and component-resized events.
           The check box fires a component-moved event.* Iconify and then deiconify the window.
               
             You do *not* get component-hidden or -shown events.
             If you want to be notified of iconification events,
             you should use a window listener or a window state listener.* Resize the window.
                 
               You will see component-resized
               (and possibly component-moved) events
               from all four components — label, check box, panel, and frame.
               If the frame and panel's layout manager did not make every component
               as wide as possible,
               the panel, label, and check box would not have been resized.

  ---

  You can find the demo's code in
  [`ComponentEventDemo.java`](../examples/events/ComponentEventDemoProject/src/events/ComponentEventDemo.java).
  Here is just the code related to handling component events:

  ```

  public class ComponentEventDemo ... implements ComponentListener {
      static JFrame frame;
      JLabel label;
      ...
      public ComponentEventDemo() {
          ...
          JPanel panel = new JPanel(new BorderLayout());
          label = new JLabel("This is a label", JLabel.CENTER);
          label.addComponentListener(this);
          panel.add(label, BorderLayout.CENTER);

          JCheckBox checkbox = new JCheckBox("Label visible", true);
          checkbox.addComponentListener(this);
          panel.add(checkbox, BorderLayout.PAGE_END);
          panel.addComponentListener(this);
          ...
          frame.addComponentListener(this);
      }
      ...
       public void componentHidden(ComponentEvent e) {
          displayMessage(e.getComponent().getClass().getName() + " --- Hidden");
      }

      public void componentMoved(ComponentEvent e) {
          displayMessage(e.getComponent().getClass().getName() + " --- Moved");
      }

      public void componentResized(ComponentEvent e) {
          displayMessage(e.getComponent().getClass().getName() + " --- Resized ");            
      }

      public void componentShown(ComponentEvent e) {
          displayMessage(e.getComponent().getClass().getName() + " --- Shown");

      }

      public static void main(String[] args) {
          ...
          //Create and set up the window.
          frame = new JFrame("ComponentEventDemo");
          ...
          JComponent newContentPane = new ComponentEventDemo();
          frame.setContentPane(newContentPane);
          ...
      }
  }

  ```

  ### The Component Listener API

  > The ComponentListener
  > Interface
  >
  > *All of these methods are also in the adapter class,
  > [`ComponentAdapter`](http://download.oracle.com/javase/7/docs/api/java/awt/event/ComponentAdapter.html).*
  >
  > | Method | Purpose |
  > | --- | --- |
  > | [componentHidden(ComponentEvent)](http://download.oracle.com/javase/7/docs/api/java/awt/event/ComponentListener.html#componentHidden(java.awt.event.ComponentEvent)) | Called after the listened-to component is hidden as the result of the `setVisible` method being called. |
  > | [componentMoved(ComponentEvent)](http://download.oracle.com/javase/7/docs/api/java/awt/event/ComponentListener.html#componentMoved(java.awt.event.ComponentEvent)) | Called after the listened-to component moves, relative to its container. For example, if a window is moved, the window fires a component-moved event, but the components it contains do not. |
  > | [componentResized(ComponentEvent)](http://download.oracle.com/javase/7/docs/api/java/awt/event/ComponentListener.html#componentResized(java.awt.event.ComponentEvent)) | Called after the listened-to component's size (rectangular bounds) changes. |
  > | [componentShown(ComponentEvent)](http://download.oracle.com/javase/7/docs/api/java/awt/event/ComponentListener.html#componentShown(java.awt.event.ComponentEvent)) | Called after the listened-to component becomes visible as the result of the `setVisible` method being called. |
  >
  > The ComponentEvent
  > Class
  >
  > | Method | Purpose |
  > | --- | --- |
  > | [Component getComponent()](http://download.oracle.com/javase/7/docs/api/java/awt/event/ComponentEvent.html#getComponent()) | Returns the component that fired the event. You can use this instead of the `getSource` method. |

  ### Examples that Use Component Listeners
  > The following table lists the
  > examples that use component listeners.
  >
  > | Example | Where Described | Notes |
  > | --- | --- | --- |
  > | [`ComponentEventDemo`](../examples/events/index.html#ComponentEventDemo) | This section | Reports all component events that occur on several components to demonstrate the circumstances under which component events are fired. |

[« Previous](changelistener.html)
•
[Trail](../TOC.html)
•
[Next »](containerlistener.html)

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

**Previous page:** How to Write a Change Listener
  
**Next page:** How to Write a Container Listener




A browser with JavaScript enabled is required for this page to operate properly.