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

[How to Write a Mouse-Wheel Listener](mousewheellistener.html)

How to Write a Property Change Listener

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

[« Previous](mousewheellistener.html) • [Trail](../TOC.html) • [Next »](tablemodellistener.html)

# How to Write a Property Change Listener

Property-change events occur whenever the value of a
*bound property* changes
for a *bean* —
a component that conforms to the
JavaBeansTM specification.
You can find out more about beans from the
[JavaBeans](../../javabeans/) trail of the
Java Tutorial. All Swing components are also beans.

A JavaBeans property is accessed through its
*get* and *set* methods.
For example, `JComponent` has the
property *font* which is accessible
through the `getFont` and
`setFont` methods.

Besides the *get* and *set*
methods, a bound property fires a property-change event
when its value changes.
For more information, see the
[Bound Properties](../../javabeans/properties/bound.html) page in the JavaBeans trail.

Some scenarios that commonly require property-change listeners
include:

* You have implemented a formatted text field and need
  a way to detect when the user has entered a new value.
  You can register a property-change listener on
  the formatted text field to listen to
  changes on the *value* property.
  See `FormattedTextFieldDemo` in
  [How to Use Formatted Text Fields](../components/formattedtextfield.html#value) for an example of this.

  * You have implemented a dialog and need to
    know when a user has clicked one of the dialog's
    buttons or changed a selection in the dialog.
    See `DialogDemo` in
    [How to Make Dialogs](../components/dialog.html#stayup) for an example of registering a property-change
    listener on an option pane to listen to changes to
    the *value* property. You can also check
    out `FileChooserDemo2` in
    [How to Use File Choosers](../components/filechooser.html#advancedexample) for an example of how to register a property-change
    listener to listen to changes to the
    *directoryChanged* and
    *selectedFileChanged* properties.

    * You need to be notified when the component that has
      the focus changes. You can register a property-change
      listener on the keyboard focus manager to listen to
      changes to the *focusOwner* property.
      See `TrackFocusDemo` and `DragPictureDemo` in
      [How to Use the Focus Subsystem](../misc/focus.html#trackingFocus) for examples of this.

Although these are some of the more common uses for
property-change listeners, you can register a property-change
listener on the bound property of any component that conforms
to the JavaBeans specification.

You can register a property change listener in two ways.
The first uses the method
`addPropertyChangeListener(PropertyChangeListener)`.
When you register a listener this way, you are notified
of every change to every bound property for that object.
In the `propertyChange` method, you can get the name
of the property that has changed using the
`PropertyChangeEvent` `getPropertyName`
method, as in the following code snippet:

```

KeyboardFocusManager focusManager =
   KeyboardFocusManager.getCurrentKeyboardFocusManager();
focusManager.addPropertyChangeListener(new FocusManagerListener());
...
public FocusManagerListener implements PropertyChangeListener {
    public void propertyChange(PropertyChangeEvent e) {
        String propertyName = e.getPropertyName();
        if ("focusOwner".equals(propertyName) {
            ...
        } else if ("focusedWindow".equals(propertyName) {
            ...
        }
    }
    ...
}

```

The second way to register a property change listener uses the method
`addPropertyChangeListener(String, PropertyChangeListener)`.
The `String` argument is the name of a property. Using this
method means that you only receive notification when
a change occurs to that particular property. So, for example,
if you registered a property change listener like this:

```

aComponent.addPropertyChangeListener("font",
                                     new FontListener());

```

`FontListener` only receives notification when the
value of the component's
*font* property changes. It does *not*
receive notification when the value changes for *transferHandler*,
*opaque*, *border*, or any other property.

The following example shows how to register a property
change listener on the *value* property of a
formatted text field using the two-argument version of
`addPropertyChangeListener`:

```

//...where initialization occurs:
double amount;
JFormattedTextField amountField;
...
amountField.addPropertyChangeListener("value",
                                      new FormattedTextFieldListener());
...
class FormattedTextFieldListener implements PropertyChangeListener {
    public void propertyChanged(PropertyChangeEvent e) {
        Object source = e.getSource();
        if (source == amountField) {
            amount = ((Number)amountField.getValue()).doubleValue();
            ...
        }
        ...//re-compute payment and update field...
    }
}

```

### The Property Change Listener API

> Registering
> a PropertyChangeListener
>
> | Method | Purpose |
> | --- | --- |
> | [addPropertyChangeListener(PropertyChangeListener)](http://download.oracle.com/javase/7/docs/api/java/awt/Component.html#addPropertyChangeListener(java.beans.PropertyChangeListener)) | Add a property-change listener to the listener list. |
> | [addPropertyChangeListener(String, PropertyChangeListener)](http://download.oracle.com/javase/7/docs/api/java/awt/Component.html#addPropertyChangeListener(java.lang.String, java.beans.PropertyChangeListener)) | Add a property-change listener for a specific property. The listener is called only when there is a change to the specified property. |
>
> The
> PropertyChangeListener Interface
>
> *Because `PropertyChangeListener`
> has only one method, it has no corresponding
> adapter class.*
>
> | Method | Purpose |
> | --- | --- |
> | [propertyChange(PropertyChangeEvent)](http://download.oracle.com/javase/7/docs/api/java/beans/PropertyChangeListener.html#propertyChange(java.beans.PropertyChangeEvent)) | Called when the listened-to bean changes a bound property. |
>
> The PropertyChangeEvent Class
>
> | Method | Purpose |
> | --- | --- |
> | [Object getNewValue()](http://download.oracle.com/javase/7/docs/api/java/beans/PropertyChangeEvent.html#getNewValue())  [Object getOldValue()](http://download.oracle.com/javase/7/docs/api/java/beans/PropertyChangeEvent.html#getOldValue()) | Return the new, or old, value of the property, respectively. |
> | [String getPropertyName()](http://download.oracle.com/javase/7/docs/api/java/beans/PropertyChangeEvent.html#getPropertyName()) | Return the name of the property that was changed. |
> | [void setPropagationId()](http://download.oracle.com/javase/7/docs/api/java/beans/PropertyChangeEvent.html#setPropagationId()) | Get or set the propagation ID value. Reserved for future use. |

### Examples that Use Property Change Listeners
> The following table lists the
> examples that use property-change listeners.
>
> | Example | Where Described | Notes |
> | --- | --- | --- |
> | [`FormattedTextFieldDemo`](../examples/components/index.html#FormattedTextFieldDemo) | [How to Use Formatted Text Fields](../components/formattedtextfield.html#value) | A property-change listener is registered on several formatted text fields to track changes to the *value* property. |
> | [`DialogDemo`](../examples/components/index.html#DialogDemo) | [How to Make Dialogs](../components/dialog.html#stayup) | The [`CustomDialog`](../examples/components/DialogDemoProject/src/components/CustomDialog.java) class registers a property-change listener on an option pane to listen to the *value* and *inputValue* properties. |
> | [`FileChooserDemo2`](../examples/components/index.html#FileChooserDemo2) | [How to Use File Choosers](../components/filechooser.html#advancedexample) | The [`ImagePreview`](../examples/components/FileChooserDemo2Project/src/components/ImagePreview.java) class registers a property-change listener on the file chooser to listen to the *directoryChanged* and *selectedFileChanged* properties. |
> | [`TrackFocusDemo`](../examples/misc/index.html#TrackFocusDemo) | [How to Use the Focus Subsystem](../misc/focus.html#trackingFocus) | A property-change listener is registered on the keyboard focus manager to track changes to the *focusOwner* property. |

[« Previous](mousewheellistener.html)
•
[Trail](../TOC.html)
•
[Next »](tablemodellistener.html)

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

**Previous page:** How to Write a Mouse-Wheel Listener
  
**Next page:** How to Write a Table Model Listener




A browser with JavaScript enabled is required for this page to operate properly.