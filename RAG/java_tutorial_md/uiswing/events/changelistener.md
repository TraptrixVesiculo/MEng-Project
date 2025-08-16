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

How to Write a Change Listener

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

[« Previous](caretlistener.html) • [Trail](../TOC.html) • [Next »](componentlistener.html)

# How to Write a Change Listener

A change listener is similar to a
[property change listener](propertychangelistener.html).
A change listener is registered on an object — typically
a component, but it could be another object, like a model —
and the listener is notified when the object has changed.
The big difference from a property change listener is that a
change listener is not notified of *what* has changed,
but simply that the source object *has* changed.
Therefore, a change listener is most useful when
it is only necessary to know when an object has changed in any way.

Several Swing components (including
[JTabbedPane](../components/tabbedpane.html), JViewPort) rely on change events for basic functionality
— sliders, color choosers and spinners.
To learn when the value in a
[slider](../components/slider.html) changes,
you need to register a change listener.
Similarly, you need to register a change listener on a
[color chooser](../components/colorchooser.html) to be informed when the user chooses a new color.
You register a change listener on a
[spinner](../components/spinner.html), a component introduced in release 1.4,
to be notified when the spinner's value changes.

Here is an example of change event handling code for a slider:

```

//...where initialization occurs:
framesPerSecond.addChangeListener(new SliderListener());
...
class SliderListener implements ChangeListener {
    public void stateChanged(ChangeEvent e) {
        JSlider source = (JSlider)e.getSource();
        if (!source.getValueIsAdjusting()) {
            int fps = (int)source.getValue();
	    ...
        }    
    }
}

```

You can find the source file for `SliderDemo` in the
[example index for Using Swing Components](../examples/components/index.html#SliderDemo).

### The Change Listener API

> The ChangeListener
> Interface
>
> *Because `ChangeListener` has only one method,
> it has no corresponding adapter class.*
>
> | Method | Purpose |
> | --- | --- |
> | [stateChanged(ChangeEvent)](http://download.oracle.com/javase/7/docs/api/javax/swing/event/ChangeListener.html#stateChanged(javax.swing.event.ChangeEvent)) | Called when the listened-to component changes state. |
>
> The ChangeEvent Class
>
> | Method | Purpose |
> | --- | --- |
> | [Object getSource()](http://download.oracle.com/javase/7/docs/api/java/util/EventObject.html#getSource()) (*in `java.util.EventObject`*) | Returns the object that fired the event. |

### Examples that Use Change Listeners
> The following table lists the
> examples that use change listeners.
>
> | Example | Where Described | Notes |
> | --- | --- | --- |
> | [`SliderDemo`](../examples/components/index.html#SliderDemo) and   [`SliderDemo2`](../examples/components/index.html#SliderDemo2) | [How to Use Sliders](../components/slider.html) | Registers a change listener on a slider that controls animation speed. The change listener ignores the change events until the user releases the slider. |
> | [`ColorChooserDemo`](../examples/components/index.html#ColorChooserDemo) and   [`ColorChooserDemo2`](../examples/components/index.html#ColorChooserDemo2) | [How to Use Color Choosers](../components/colorchooser.html  ) | Uses a change listener on the selection model of a color chooser to learn when the user changes the current color. |
> | [`SpinnerDemo3`](../examples/components/index.html#SpinnerDemo3) | [Detecting Spinner Value Changes](../components/spinner.html#change) in [How to Use Spinners](../components/spinner.html). | Uses a change listener on a date-field spinner to change the color of the text as the spinner's date changes. |
> | [`SpinnerDemo4`](../examples/components/index.html#SpinnerDemo4) | [Detecting Spinner Value Changes](../components/spinner.html#change) in [How to Use Spinners](../components/spinner.html). | Uses a change listener on a spinner to cycle through the gray scale as the spinner's value changes. |
> | [`ConverterRangeModel`](../examples/components/ConverterProject/src/components/ConverterRangeModel.java)  and its subclass,   [`FollowerRangeModel`](../examples/components/ConverterProject/src/components/FollowerRangeModel.java) | [How to Use Models](../components/model.html) | Implement custom models for the sliders used in the [`Converter`](../examples/components/index.html#Converter) demo. Both models explicitly fire change events when necessary. |

[« Previous](caretlistener.html)
•
[Trail](../TOC.html)
•
[Next »](componentlistener.html)

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

**Previous page:** How to Write a Caret Listener
  
**Next page:** How to Write a Component Listener




A browser with JavaScript enabled is required for this page to operate properly.