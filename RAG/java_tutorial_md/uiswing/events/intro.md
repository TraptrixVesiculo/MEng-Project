[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Creating a GUI With JFC/Swing
  
**Lesson:** Writing Event Listeners

[Writing Event Listeners](index.html)

Introduction to Event Listeners

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

[« Previous](index.html) • [Trail](../TOC.html) • [Next »](generalrules.html)

# Introduction to Event Listeners

If you have read any of the component how-to pages,
you probably already know the basics of event listeners.

Let us look at one of the simplest event handling
examples possible. It is called Beeper, and it features a button
that beeps when you click it.

Click the Launch button to run Beeper using
[Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp) ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
Alternatively, to compile and run the example yourself, consult the
[example index](../examples/events/index.html#Beeper).
 [![Launches the Beeper example](../../images/jws-launch-button.png )](http://download.oracle.com/javase/tutorialJWS/uiswing/events/ex6/Beeper.jnlp) 

![A Click Me Beeper Button](../../figures/uiswing/events/Beeper.png)

You can find the entire program in
[`Beeper.java`](../examples/events/BeeperProject/src/events/Beeper.java).
Here is the code that implements the event handling
for the button:

```

public class Beeper ... implements ActionListener {
    ...
    //where initialization occurs:
        button.addActionListener(this);
    ...
    public void actionPerformed(ActionEvent e) {
        ...//Make a beep sound...
    }
}

```

The `Beeper` class implements the
[`ActionListener`](actionlistener.html)
interface, which contains one method:
`actionPerformed`.
Since `Beeper` implements `ActionListener`,
a `Beeper` object can register as a listener
for the action events that buttons fire.
Once the `Beeper` has been registered
using the `Button` `addActionListener` method,
the `Beeper`'s `actionPerformed` method
is called every time the button is clicked.
> ### A More Complex Example

The event model,
which you saw at its simplest in the preceding example,
is quite powerful and flexible.
Any number of event listener objects
can listen for all kinds of events
from any number of event source objects.
For example, a program
might create one listener per event source.
Or a program might have a single listener
for all events from all sources.
A program can even have more than one listener
for a single kind of event from a single event source.

![Event source with multiple listeners](../../figures/uiswing/events/2eventsource.gif)

#### Multiple listeners can register to be notified of events of a particular type from a particular source. Also, the same listener can listen to notifications from different objects.

Each event is represented by an object that gives
information about the event and identifies the event
source. Event sources are often components or models,
but other kinds of objects can also be event sources.

Whenever you want to detect events from a particular component,
first check the how-to section for that component. A list of the
component how-to sections is
[here](../components/componentlist.html).
The how-to sections give examples of handling the
events that you are most likely to care about. In
[How to Use Color Choosers](../components/colorchooser.html), for instance, you will find an example
of writing a change listener to track when the color
changes in the color chooser.

The following example demonstrates that event listeners
can be registered on multiple objects and that
the same event can be sent to multiple listeners.
The example contains two event sources
(`JButton` instances)
and two event listeners.
One of the event listeners
(an instance of a class called `MultiListener`)
listens for events from both buttons.
When it receives an event,
it adds the event's "action command"
(which is set to the text on the button's label)
to the top text area.
The second event listener
(an instance of a class called `Eavesdropper`)
listens for events on only one of the buttons.
When it receives an event,
it adds the action command
to the bottom text area.

![MultiListener and Eavesdropper responses to buttons](../../figures/uiswing/events/MultiListener.gif)

---

**Try this:**

1. Click the Launch button to run MultiListener using
   [Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp) ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
   Alternatively, to compile and run the example yourself, consult the
   [example index](../examples/events/index.html#MultiListener).
    [![Launches the MultiListener example](../../images/jws-launch-button.png )](http://download.oracle.com/javase/tutorialJWS/uiswing/events/ex6/MultiListener.jnlp) - Click the *Blah blah blah* button. Only the
     `MultiListener` object is
     registered to listen to this button.- Click the *You do not say!* button. Both
       the `MultiListener` object and the
       `Eavesdropper` object are registered to
       listen to this button.

       ---

You can find the entire program in
[`MultiListener.java`](../examples/events/MultiListenerProject/src/events/MultiListener.java).
Here is the code that implements the event handling
for the button:

```

public class MultiListener ... implements ActionListener {
    ...
    //where initialization occurs:
        button1.addActionListener(this);
        button2.addActionListener(this);

        button2.addActionListener(new Eavesdropper(bottomTextArea));
    }

    public void actionPerformed(ActionEvent e) {
        topTextArea.append(e.getActionCommand() + newline);
    }
}

class Eavesdropper implements ActionListener {
    ...
    public void actionPerformed(ActionEvent e) {
        myTextArea.append(e.getActionCommand() + newline);
    }
}

```

In the above code,
both `MultiListener` and `Eavesdropper`
implement the `ActionListener` interface
and register as action listeners
using the `JButton` `addActionListener` method.
Both classes' implementations of the `actionPerformed` method
are similar:
they simply add the event's action command
to a text area.

[« Previous](index.html)
•
[Trail](../TOC.html)
•
[Next »](generalrules.html)

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

**Previous page:** Writing Event Listeners
  
**Next page:** General Information about Writing Event Listeners




A browser with JavaScript enabled is required for this page to operate properly.