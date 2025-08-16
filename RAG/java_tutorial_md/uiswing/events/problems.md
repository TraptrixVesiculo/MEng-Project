[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Creating a GUI With JFC/Swing
  
**Lesson:** Writing Event Listeners

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

[How to Write a Tree-Will-Expand Listener](treewillexpandlistener.html)

[How to Write an Undoable Edit Listener](undoableeditlistener.html)

[How to Write Window Listeners](windowlistener.html)

[Listener API Table](api.html)

Solving Common Event-Handling Problems

[Home Page](../../index.html)
>
[Creating a GUI With JFC/Swing](../index.html)
>
[Writing Event Listeners](index.html)

[« Previous](api.html) • [Trail](../TOC.html) • [Next »](../QandE/questions-ch5.html)

# Solving Common Event-Handling Problems

This section discusses problems that you might encounter
while handling events.

**Problem:**
I'm trying to handle certain events from a component,
but the component isn't generating the events it should.

* First, make sure you registered
  the right kind of listener to detect the events.
  See whether another kind of listener
  might detect the kind of events you need.* Make sure you registered the listener on the right object.* Did you implement the event handler correctly?
      For example, if you extended an adapter class,
      then make sure you used the right method signature.
      Make sure each event-handling method is `public void`,
      that the name spelled right
      and that the argument is of the right type.* If you still think that the component
        isn't generating the events it should,
        check the
        [Java Developer Connection](http://developer.java.sun.com/) to see whether this is a known bug.

**Problem:**
My combo box isn't generating low-level events such as focus events.

* Combo boxes are compound components — components
  implemented using multiple components.
  For this reason, combo boxes don't fire the low-level events
  that simple components fire.
  For more information, see
  [Handling Events on a Combo Box](../components/combobox.html#listeners).

**Problem:**
The document for an editor pane (or text pane)
isn't firing document events.

* The document instance for an editor pane or text pane
  might change when loading text from a URL.
  Thus, your listeners might be listening for events on
  an unused document.
  For example,
  if you load an editor pane or text pane with HTML
  that was previously loaded with plain text,
  the document will change to an `HTMLDocument` instance.
  If your program dynamically loads text
  into an editor pane or text pane,
  make sure the code adjusts for possible changes
  to the document
  (re-register document listeners on the new document, and so on).

If you don't see your problem in this list, see
[Solving Common Component Problems](../components/problems.html).

[« Previous](api.html)
•
[Trail](../TOC.html)
•
[Next »](../QandE/questions-ch5.html)

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

**Previous page:** Listener API Table
  
**Next page:** Questions and Exercises: Writing Event Listeners




A browser with JavaScript enabled is required for this page to operate properly.