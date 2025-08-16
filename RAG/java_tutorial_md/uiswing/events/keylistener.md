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

How to Write a Key Listener

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

[« Previous](itemlistener.html) • [Trail](../TOC.html) • [Next »](listdatalistener.html)

# How to Write a Key Listener

Key events indicate when the user is typing at the keyboard.
Specifically, key events are fired
by the component with the keyboard focus
when the user presses or releases keyboard keys.
For detailed information about focus, see
[How to Use the Focus Subsystem](../misc/focus.html).

---

**Note:** To define special reactions to particular keys,
use key bindings instead of a key listener.
For further information, see
[How to Use Key Bindings](../misc/keybinding.html).

---

Notifications are sent about
two basic kinds of key events:

* The typing of a Unicode character* The pressing or releasing of a key on the keyboard

The first kind of event is called a *key-typed* event.
The second kind is either a *key-pressed* or
*key-released* event.

In general, you react to only key-typed events
unless you need to know when the user presses keys
that do not correspond to characters.
For example, to know when the user types a
Unicode character — whether by pressing
one key such as 'a' or by pressing several keys in sequence —
you handle key-typed events. On the other hand,
to know when the user presses the F1 key,
or whether the user pressed the '3' key on the number pad,
you handle key-pressed events.

---

**Note:** 
To fire keyboard events,
a component *must* have the keyboard focus.

---

To make a component get the keyboard focus,
follow these steps:

1. Make sure the component's
   `isFocusable` method returns `true`.
   This state allows the component to receive the focus.
   For example, you can enable keyboard focus for a
   `JLabel` component by calling the `setFocusable(true)` method
   on the label.- Make sure the component requests the focus
     when appropriate. For custom components, implement a mouse listener
     that calls the `requestFocusInWindow` method
     when the component is clicked.

---

**Version note:** This page reflects the focus API introduced in JDK release 1.4.
As of that release, the focus subsystem consumes focus traversal
keys, such as Tab and Shift Tab. If you need to prevent the focus
traversal keys from being consumed, you can call

```

component.setFocusTraversalKeysEnabled(false)

```

on the component that is firing the key events. Your program
must then handle focus traversal on its own. Alternatively,
you can use the
[`KeyEventDispatcher`](http://download.oracle.com/javase/7/docs/api/java/awt/KeyEventDispatcher.html) class to pre-listen
to all key events. The
[focus page](../misc/focus.html) has detailed information on the focus subsystem.

---

You can obtain detailed information about a
particular key-pressed event.
For example, you can query a key-pressed event to
determine if it was fired from an action key. Examples of action keys
include Copy, Paste, Page Up, Undo, and the arrow and function keys.
As of JDK release 1.4,
you can also query a key-pressed or key-released event to determine
the location of the key that fired the event. Most key events are fired from
the standard keyboard, but the events for some keys, such as
Shift, have information on whether the user pressed the Shift key on
the left or the right side of the keyboard. Likewise, the number
'2' can be typed from either the standard keyboard or from the number pad.

For key-typed events you can obtain the key character value as well
as any modifiers used.

---

**Note:** You should not rely on the key character value returned
from `getKeyChar` unless it is involved in a
key-typed event.

---

The following example demonstrates key events.
It consists of a text field that you can type into,
followed by a text area that displays a message every time
the text field fires a key event.
A button at the bottom of the window
lets you clear both the text field and text area.

![KeyEventDemo.html](../../figures/uiswing/events/KeyEventDemo.png)

---

**Try this:**

1. Click the Launch button
   to run KeyEventDemo using
   [Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp)
   ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
   Alternatively, to compile and run the example yourself,
   consult the
   [example index](../examples/events/index.html#KeyEventDemo).

   [![Launches the KeyEventDemo application](../../images/jws-launch-button.png)](http://download.oracle.com/javase/tutorialJWS/uiswing/events/ex6/KeyEventDemo.jnlp)- Type a lowercase 'a' by pressing and releasing
     the A key on the keyboard.
       
     The text field fires three events:
     a key-pressed event, a key-typed event, and a key-released event.
     Note that the key-typed event doesn't have key code information,
     and key-pressed and key-released events don't have key character
     information. None of the events so far are from modifier or action keys
     and the key location, reported on the key-pressed and key-released
     events, is most likely standard.- Press the Clear button.
         
       You might want to do this after each of the following steps.- Press and release the Shift key.
           
         The text field fires two events:
         a key-pressed and a key-released.
         The text field doesn't fire a key-typed event
         because Shift, by itself,
         doesn't correspond to any character.- Type an uppercase 'A' by pressing the Shift and A keys.
             
           You'll see the following events,
           although perhaps not in this order:
           key-pressed (Shift), key-pressed (A), key typed ('A'),
           key-released (A), key-released (Shift).
           Note that Shift is listed as the modifier key for
           the key-typed and key-pressed events.- Type an uppercase 'A' by pressing and releasing
             the Caps Lock key, and then pressing the A key.
               
             You should see the following events:
             key-pressed (Caps Lock), key-pressed (A), key typed ('A'),
             key-released (A).
             Note that Caps Lock is *not* listed as a modifier key.- Press the Tab key. No Tab key-pressed or key-released
               events are received by the key event listener. This is
               because the focus subsystem consumes focus traversal keys,
               such as Tab and Shift Tab. Press Tab twice more to return
               the focus to the text area.- Press a function key, such as F3. You'll see that
                 the function key is an action key.- Press the left Shift key, followed by the right Shift key.
                   The key-pressed and key-released events indicate which
                   Shift key was typed.- Press the Num Lock key if your keyboard has a number pad.
                       
                     As for Caps Lock, there is a key-pressed event, but no
                     key-released event.- Press the '2' key on the number pad. You see the key-pressed,
                       key-typed, and key-released events for the number '2'.- Press the '2' key on the standard keyboard. Again, you see
                         the three event messages. The key-typed events for both
                         number 2 keys are identical. But the key-pressed and key-released
                         events indicate different key codes and different key locations.- Press the Num Lock key again. A key-released event is fired.

---

You can find the example's code in
[`KeyEventDemo.java`](../examples/events/KeyEventDemoProject/src/events/KeyEventDemo.java).
Here is the demo's key event handling code:

```

public class KeyEventDemo ...  implements KeyListener ... {
    ...//where initialization occurs:
	typingArea = new JTextField(20);
	typingArea.addKeyListener(this);

        //Uncomment this if you wish to turn off focus
        //traversal.  The focus subsystem consumes
        //focus traversal keys, such as Tab and Shift Tab.
        //If you uncomment the following line of code, this
        //disables focus traversal and the Tab events 
        //become available to the key event listener.
        //typingArea.setFocusTraversalKeysEnabled(false);
    ...
    /** Handle the key typed event from the text field. */
    public void keyTyped(KeyEvent e) {
	displayInfo(e, "KEY TYPED: ");
    }

    /** Handle the key-pressed event from the text field. */
    public void keyPressed(KeyEvent e) {
	displayInfo(e, "KEY PRESSED: ");
    }

    /** Handle the key-released event from the text field. */
    public void keyReleased(KeyEvent e) {
	displayInfo(e, "KEY RELEASED: ");
    }
    ...
    private void displayInfo(KeyEvent e, String keyStatus){
        
        //You should only rely on the key char if the event
        //is a key typed event.
        int id = e.getID();
        String keyString;
        if (id == KeyEvent.KEY_TYPED) {
            char c = e.getKeyChar();
            keyString = "key character = '" + c + "'";
        } else {
            int keyCode = e.getKeyCode();
            keyString = "key code = " + keyCode
                    + " ("
                    + KeyEvent.getKeyText(keyCode)
                    + ")";
        }
        
        int modifiersEx = e.getModifiersEx();
        String modString = "extended modifiers = " + modifiersEx;
        String tmpString = KeyEvent.getModifiersExText(modifiersEx);
        if (tmpString.length() > 0) {
            modString += " (" + tmpString + ")";
        } else {
            modString += " (no extended modifiers)";
        }
        
        String actionString = "action key? ";
        if (e.isActionKey()) {
            actionString += "YES";
        } else {
            actionString += "NO";
        }
        
        String locationString = "key location: ";
        int location = e.getKeyLocation();
        if (location == KeyEvent.KEY_LOCATION_STANDARD) {
            locationString += "standard";
        } else if (location == KeyEvent.KEY_LOCATION_LEFT) {
            locationString += "left";
        } else if (location == KeyEvent.KEY_LOCATION_RIGHT) {
            locationString += "right";
        } else if (location == KeyEvent.KEY_LOCATION_NUMPAD) {
            locationString += "numpad";
        } else { // (location == KeyEvent.KEY_LOCATION_UNKNOWN)
            locationString += "unknown";
        }
        
        ...//Display information about the KeyEvent...
    }
}

```

### The Key Listener API

> The KeyListener
> Interface
>
> *The corresponding adapter class is
> [`KeyAdapter`](http://download.oracle.com/javase/7/docs/api/java/awt/event/KeyAdapter.html).*
>
> | Method | Purpose |
> | --- | --- |
> | [keyTyped(KeyEvent)](http://download.oracle.com/javase/7/docs/api/java/awt/event/KeyListener.html#keyTyped(java.awt.event.KeyEvent)) | Called just after the user types a Unicode character into the listened-to component. |
> | [keyPressed(KeyEvent)](http://download.oracle.com/javase/7/docs/api/java/awt/event/KeyListener.html#keyPressed(java.awt.event.keyPressed)) | Called just after the user presses a key while the listened-to component has the focus. |
> | [keyReleased(KeyEvent)](http://download.oracle.com/javase/7/docs/api/java/awt/event/KeyListener.html#keyReleased(java.awt.event.KeyEvent)) | Called just after the user releases a key while the listened-to component has the focus. |
>
> The KeyEvent Class
>
> The `KeyEvent` class inherits many useful
> methods from the
> [`InputEvent`](http://download.oracle.com/javase/7/docs/api/java/awt/event/InputEvent.html) class, such as `getModifiersEx`, and a couple of
> useful methods from the
> [`ComponentEvent`](http://download.oracle.com/javase/7/docs/api/java/awt/event/ComponentEvent.html) and
> [`AWTEvent`](http://download.oracle.com/javase/7/docs/api/java/awt/AWTEvent.html) classes. See the
> [InputEvent Class](mouselistener.html#inputevent)
> table in the
> [mouse listener](mouselistener.html) page for
> a complete list.
>
> | Method | Purpose |
> | --- | --- |
> | [int getKeyChar()](http://download.oracle.com/javase/7/docs/api/java/awt/event/KeyEvent.html#getKeyChar()) | Obtains the Unicode character associated with this event. Only rely on this value for key-typed events. |
> | [int getKeyCode()](http://download.oracle.com/javase/7/docs/api/java/awt/event/KeyEvent.html#getKeyCode()) | Obtains the key code associated with this event. The key code identifies the particular key on the keyboard that the user pressed or released. The `KeyEvent` class defines many key code constants for commonly seen keys. For example, `VK_A` specifies the key labeled **A**, and `VK_ESCAPE` specifies the Escape key. |
> | [String getKeyText(int)](http://download.oracle.com/javase/7/docs/api/java/awt/event/KeyEvent.html#getKeyText(int))  [String getKeyModifiersText(int)](http://download.oracle.com/javase/7/docs/api/java/awt/event/KeyEvent.html#getKeyModifiersText(int)) | Return text descriptions of the event's key code and modifier keys, respectively. |
> | [int getModifiersEx()](http://download.oracle.com/javase/7/docs/api/java/awt/event/InputEvent.html#getModifiersEx())   [String getModifiersExText(int modifiers)](http://download.oracle.com/javase/7/docs/api/java/awt/event/InputEvent.html#getModifiersExText(int)) | Return the extended modifiers mask for this event. There are methods inherited from the `InputEvent` class. Extended modifiers represent the state of all modal keys. The `getModifiersExText` method returns a string describing the extended modifier keys and mouse buttons. Since the `getModifiersEx` and `getModifiersExText` methods provide more information about key events, they are preferred over the `getKeyText` or `getKeyModifiersText` methods. |
> | [boolean isActionKey()](http://download.oracle.com/javase/7/docs/api/java/awt/event/KeyEvent.html#isActionKey()) | Returns true if the key firing the event is an action key. Examples of action keys include Cut, Copy, Paste, Page Up, Caps Lock, the arrow and function keys. This information is valid only for key-pressed and key-released events. |
> | [int getKeyLocation()](http://download.oracle.com/javase/7/docs/api/java/awt/event/KeyEvent.html#getKeyLocation()) | Returns the location of the key that fired this event. This provides a way to distinguish keys that occur more than once on a keyboard, such as the two shift keys, for example. The possible values are `KEY_LOCATION_STANDARD`, `KEY_LOCATION_LEFT`, `KEY_LOCATION_RIGHT`, `KEY_LOCATION_NUMPAD`, or `KEY_LOCATION_UNKNOWN`. This method always returns `KEY_LOCATION_UNKNOWN` for key-typed events. Introduced in JDK release 1.4. |

### Examples that Use Key Listeners
> The following table lists the
> examples that use key listeners.
>
> | Example | Where Described | Notes |
> | --- | --- | --- |
> | [`KeyEventDemo`](../examples/events/index.html#KeyEventDemo) | This section | Reports all key events that occur on a text field to demonstrate the circumstances under which key events are fired. |

[« Previous](itemlistener.html)
•
[Trail](../TOC.html)
•
[Next »](listdatalistener.html)

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

**Previous page:** How to Write an Item Listener
  
**Next page:** How to Write a List Data Listener




A browser with JavaScript enabled is required for this page to operate properly.