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

How to Write an Action Listener

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

[« Previous](handling.html) • [Trail](../TOC.html) • [Next »](caretlistener.html)

# How to Write an Action Listener

Action listeners are probably the easiest — and most
common — event handlers to implement.
You implement an action listener to define what should be done when an user performs certain operation.

An action event occurs, whenever an action is performed by the user. Examples: When the user clicks a
[button](../components/button.html), chooses a
[menu item](../components/menu.html), presses Enter in a
[text field](../components/textfield.html). The result is that an `actionPerformed` message is sent to all action listeners that are registered on the relevant component.

To write an Action Listener, follow the steps given below:

1. Declare an event handler class and specify that the class either implements an ActionListener interface or extends a class that implements an ActionListener interface. For example:

   ```

             public class MyClass implements ActionListener { 

   ```

   - Register an instance of the event handler class as a listener on one or more components. For example:

     ```

               someComponent.addActionListener(instanceOfMyClass);

     ```

     - Include code that implements the methods in listener interface. For example:

       ```

                 public void actionPerformed(ActionEvent e) { 
                     ...//code that reacts to the action... 
                 }

       ```

In general, to detect when the user clicks an onscreen button (or does the keyboard equivalent), a program must have an object that implements the ActionListener interface. The program must register this object as an action listener on the button (the event source), using the addActionListener method. When the user clicks the onscreen button, the button fires an action event. This results in the invocation of the action listener's actionPerformed method (the only method in the ActionListener interface). The single argument to the method is an ActionEvent object that gives information about the event and its source.

Let us write a simple program which displays how many number of times a button is clicked by the user. First, here is the code that sets up the TextField , button and numClicks variable:

```

public class AL extends Frame implements WindowListener,ActionListener {
TextField text = new TextField(20);
Button b;
private int numClicks = 0;

```

In the above example, the event handler class is AL which implements ActionListener.

We would like to handle the button-click event, so we add an action listener to the button b as below:

```

b = new Button("Click me");
b.addActionListener(this); 

```

In the above code, Button b is a component upon which an instance of event handler class AL is registered.

Now, we want to display the text as to how many number of times a user clicked button. We can do this by writing the code as below:

```

public void actionPerformed(ActionEvent e) {
	 numClicks++;
	 text.setText("Button Clicked " + numClicks + " times");

```

Now, when the user clicks the Button b, the button fires an action event which invokes the action listener's actionPerformed method. Each time the user presses the button, numClicks variable is appended and the message is displayed in the text field.

Here is the complete program(AL.java):

```


import java.awt.*;
import java.awt.event.*;

public class AL extends Frame implements WindowListener,ActionListener {
	TextField text = new TextField(20);
	Button b;
	private int numClicks = 0;

	public static void main(String[] args) {
		AL myWindow = new AL("My first window");
		myWindow.setSize(350,100);
		myWindow.setVisible(true);
	}

	public AL(String title) {

		super(title);
		setLayout(new FlowLayout());
		addWindowListener(this);
		b = new Button("Click me");
		add(b);
		add(text);
		b.addActionListener(this);
	}

	public void actionPerformed(ActionEvent e) {
		numClicks++;
		text.setText("Button Clicked " + numClicks + " times");
	}

	public void windowClosing(WindowEvent e) {
		dispose();
		System.exit(0);
	}

	public void windowOpened(WindowEvent e) {}
	public void windowActivated(WindowEvent e) {}
	public void windowIconified(WindowEvent e) {}
	public void windowDeiconified(WindowEvent e) {}
	public void windowDeactivated(WindowEvent e) {}
	public void windowClosed(WindowEvent e) {}

}


```

More Examples:
`Beeper` program example is available in this trail's introduction to events,
[Introduction to Event Listeners](intro.html).
You can find the entire program in
[`Beeper.java`](../examples/events/BeeperProject/src/events/Beeper.java).
The other example described in that section,
[`MultiListener.java`](../examples/events/MultiListenerProject/src/events/MultiListener.java),
has two action sources and two action listeners,
with one listener listening to both sources
and the other listening to just one.

### The Action Listener API

> The ActionListener
> Interface
>
> *Because `ActionListener` has only one method,
> it has no corresponding adapter class.*
>
> | Method | Purpose |
> | --- | --- |
> | [actionPerformed(actionEvent)](http://download.oracle.com/javase/7/docs/api/java/awt/event/ActionListener.html#actionPerformed(java.awt.event.ActionEvent)) | Called just after the user performs an action. |
>
> The ActionEvent Class
>
> | Method | Purpose |
> | --- | --- |
> | [String getActionCommand()](http://download.oracle.com/javase/7/docs/api/java/awt/event/ActionEvent.html#getActionCommand()) | Returns the string associated with this action. Most objects that can fire action events support a method called `setActionCommand` that lets you set this string. |
> | [int getModifiers()](http://download.oracle.com/javase/7/docs/api/java/awt/event/ActionEvent.html#getModifiers()) | Returns an integer representing the modifier keys the user was pressing when the action event occurred. You can use the `ActionEvent`-defined constants `SHIFT_MASK`, `CTRL_MASK`, `META_MASK`, and `ALT_MASK` to determine which keys were pressed. For example, if the user Shift-selects a menu item, then the following expression is nonzero: ```  actionEvent.getModifiers() & ActionEvent.SHIFT_MASK      ``` |
> | [Object getSource()](http://download.oracle.com/javase/7/docs/api/java/util/EventObject.html#getSource())  (*in `java.util.EventObject`*) | Returns the object that fired the event. |

### Examples that Use Action Listeners

> The following table lists some of the many
> examples that use action listeners.
>
> | Example | Where Described | Notes |
> | --- | --- | --- |
> | [`Beeper`](../examples/events/index.html#Beeper) | This section and [Introduction to Event Listeners](intro.html) | Contains one button with one action listener that beeps when you click the button. |
> | [`MultiListener`](../examples/events/index.html#MultiListener) | [Introduction to Event Listeners](intro.html) | Registers two different action listeners on one button. Also registers the same action listener on two different buttons. |
> | [`RadioButtonDemo`](../examples/components/index.html#RadioButtonDemo) | [How to Use Radio Buttons](../components/button.html#radiobutton) | Registers the same action listener on five radio buttons. The listener uses the `getActionCommand` method to determine which radio button fired the event. |
> | [`MenuDemo`](../examples/components/index.html#MenuDemo) | [How to Use Menus](../components/menu.html) | Shows how to listen for action events on menu items. |
> | [`TextDemo`](../examples/components/index.html#TextDemo) | [How to Use Icons](../components/icon.html) | Loads an image in an action listener. Because loading an image can take a while, this program uses a `SwingWorker` to load the image in a background thread. |
> | [`TableDialogEditDemo`](../examples/components/index.html#TableDialogEditDemo) | [How to Use Tables](../components/table.html) | Registers an action listener through a factory method on the OK button of a color chooser dialog. |
> | [`SliderDemo`](../examples/components/index.html#SliderDemo) | [How to Use Sliders](../components/slider.html) | Registers an action listener on a timer that controls an animation loop. |

[« Previous](handling.html)
•
[Trail](../TOC.html)
•
[Next »](caretlistener.html)

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

**Previous page:** Implementing Listeners for Commonly Handled Events
  
**Next page:** How to Write a Caret Listener




A browser with JavaScript enabled is required for this page to operate properly.