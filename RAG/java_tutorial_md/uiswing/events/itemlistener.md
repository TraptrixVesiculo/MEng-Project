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

How to Write an Item Listener

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

[« Previous](internalframelistener.html) • [Trail](../TOC.html) • [Next »](keylistener.html)

# How to Write an Item Listener

Item events are fired
by components that implement the
[`ItemSelectable`](http://download.oracle.com/javase/7/docs/api/java/awt/ItemSelectable.html) interface.
Generally, `ItemSelectable` components maintain
on/off state for one or more items.
The Swing components that fire item events include buttons like
[check boxes](../components/button.html#checkbox),
[check menu items](../components/menu.html),
[toggle buttons](../components/button.html)
etc...and
[combo boxes](../components/combobox.html).

Here is some item-event handling code taken from
[`ComponentEventDemo.java`](../examples/events/ComponentEventDemoProject/src/events/ComponentEventDemo.java):

```

//where initialization occurs
checkbox.addItemListener(this);
...
public void itemStateChanged(ItemEvent e) {
    if (e.getStateChange() == ItemEvent.SELECTED) {
        label.setVisible(true);
        ...
    } else {
        label.setVisible(false);
    }
}

```

### The Item Listener API

> The ItemListener
> Interface
>
> *Because `ItemListener` has only one method,
> it has no corresponding adapter class.*
>
> | Method | Purpose |
> | --- | --- |
> | [itemStateChanged(ItemEvent)](http://download.oracle.com/javase/7/docs/api/java/awt/event/ItemListener.html#itemStateChanged(java.awt.event.ItemEvent)) | Called just after a state change in the listened-to component. |
>
> The ItemEvent Class
>
> | Method | Purpose |
> | --- | --- |
> | [Object getItem()](http://download.oracle.com/javase/7/docs/api/java/awt/event/ItemEvent.html#getItem()) | Returns the component-specific object associated with the item whose state changed. Often this is a `String` containing the text on the selected item. |
> | [ItemSelectable getItemSelectable()](http://download.oracle.com/javase/7/docs/api/java/awt/event/ItemEvent.html#getItemSelectable()) | Returns the component that fired the item event. You can use this instead of the `getSource` method. |
> | [int getStateChange()](http://download.oracle.com/javase/7/docs/api/java/awt/event/ItemEvent.html#getStateChange()) | Returns the new state of the item. The `ItemEvent` class defines two states: `SELECTED` and `DESELECTED`. |

### Examples that Use Item Listeners
> The following table lists some
> examples that use item listeners.
>
> | Example | Where Described | Notes |
> | --- | --- | --- |
> | [`ComponentEventDemo`](../examples/events/index.html#ComponentEventDemo) | This section and [How to Write a Component Listener](componentlistener.html) | Listens for item events on a check box, which determines whether a lable is visible. |
> | [`CheckBoxDemo`](../examples/components/index.html#CheckBoxDemo) | [How to Use Check Boxes](../components/button.html#checkbox) | Four check boxes share one item listener, which uses `getItemSelected` to determine which check box fired the event. |
> | [`MenuDemo`](../examples/components/index.html#MenuDemo) | [How to Use Menus](../components/menu.html) | Listens for item events on a check box menu item. |
> | [`MenuDemo`](../examples/components/index.html#ScrollDemo) | [How to Use Scroll Panes](../components/scrollpane.html) | Listens for item events on a toggle button. |

[« Previous](internalframelistener.html)
•
[Trail](../TOC.html)
•
[Next »](keylistener.html)

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

**Previous page:** How to Write an Internal Frame Listener
  
**Next page:** How to Write a Key Listener




A browser with JavaScript enabled is required for this page to operate properly.