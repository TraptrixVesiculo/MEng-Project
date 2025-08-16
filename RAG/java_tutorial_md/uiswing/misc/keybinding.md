[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Creating a GUI With JFC/Swing
  
**Lesson:** Using Other Swing Features

[Using Other Swing Features](index.html)

[How to Integrate with the Desktop Class](desktop.html)

[How to Create Translucent and Shaped Windows](trans_shaped_windows.html)

[How to Decorate Components with JLayer](jlayer.html)

[How to Use Actions](action.html)

[How to Use Swing Timers](timer.html)

[How to Support Assistive Technologies](access.html)

[How to Use the Focus Subsystem](focus.html)

How to Use Key Bindings

[How to Use Modality in Dialogs](modality.html)

[How to Print Tables](printtable.html)

[How to Print Text](printtext.html)

[How to Create a Splash Screen](splashscreen.html)

[How to Use the System Tray](systemtray.html)

[Solving Common Problems Using Other Swing Features](problems.html)

[Home Page](../../index.html)
>
[Creating a GUI With JFC/Swing](../index.html)
>
[Using Other Swing Features](index.html)

[« Previous](focus.html) • [Trail](../TOC.html) • [Next »](modality.html)

# How to Use Key Bindings

The `JComponent` class
supports key bindings
as a way of responding to individual keys typed by a user.
Here are some examples of when
key bindings are appropriate:

* You're creating a custom component
  and want to support keyboard access to it.
    
  For example, you might want the component to react
  when it has the focus and the user presses the Space key.

  * You want to override the behavior
    of an existing key binding.
      
    For example, if your application normally reacts to presses of the F2 key
    in a particular way,
    you might want it to perform a different action or ignore the key press.

    * You want to provide a new key binding for an existing action.
        
      For example,
      you might feel strongly that
      Control-Shift-Insert should perform a paste operation.

You often don't need to use key bindings directly.
They're used behind the scenes by
mnemonics (supported by all buttons and by tabbed panes as well
as by
[`JLabel`](http://download.oracle.com/javase/7/docs/api/javax/swing/JLabel.html)) and accelerators (supported by menu items).
You can find coverage of mnemonics and accelerators in the section
[Enabling Keyboard Operation](../components/menu.html#mnemonic).

An alternative to key bindings is using
[key listeners](../events/keylistener.html).
Key listeners have their place
as a low-level interface to keyboard input,
but for responding to individual keys
key bindings are more appropriate
and tend to result in more easily maintained code. Key listeners
are also difficult if the key binding is to be active when
the component doesn't have focus.
Some of the advantages of key bindings
are they're somewhat self documenting,
take the containment hierarchy into account,
encourage reusable chunks of code (`Action` objects),
and allow actions to be easily removed, customized, or shared.
Also, they make it easy to change the key
to which an action is bound. Another advantage of Actions is
that they have an enabled state which provides
an easy way to disable the action without having
to track which component it is attached to.

The rest of this section gives you the details you need
to use key bindings:

* [How Key Bindings Work](#maps)* [How to Make and Remove Key Bindings](#howto)* [The Key Binding API](#api)* [Examples that Use Key Bindings](#eg)

### How Key Bindings Work

> The key binding support
> provided by `JComponent`
> relies on the
> [`InputMap`](http://download.oracle.com/javase/7/docs/api/javax/swing/InputMap.html) and
> [`ActionMap`](http://download.oracle.com/javase/7/docs/api/javax/swing/ActionMap.html) classes,
> which were introduced in 1.3.
> An input map binds key strokes to action names,
> and an action map specifies the
> [action](action.html) corresponding to each action name.
> Technically, you don't need to use action names in the maps;
> you can use any object as the "key" into the maps.
> By convention, however, you use a string that names an action.
>
> Each `InputMap`/`ActionMap` has a parent that
> typically comes from the UI. Any time the look and feel is changed, the
> parent is reset. In this way, any bindings specified by the developer
> are never lost on look and feel changes.
>
> ---
>
> **Version Note:**  Prior to 1.3, the `JComponent` method `registerKeyboardAction` was
> used instead of input and action maps.
> `registerKeyboardAction` is now obsolete.
> (To ensure compatibility for older programs,
> `registerKeyboardAction` was reimplemented
> to use `InputMap` and `ActionMap`.)
>
> ---
>
> Each `JComponent` has
> one action map and three input maps.
> The input maps correspond to the following focus situations:
>
> `JComponent.WHEN_FOCUSED`: The component has the keyboard focus. The `WHEN_FOCUSED` input map is typically used when the component has no children. For example, buttons bind the Space key using the `WHEN_FOCUSED` map. These bindings are only effective when the component has focus. `JComponent.WHEN_ANCESTOR_OF_FOCUSED_COMPONENT`: The component contains (or is) the component that has the focus. This input map is commonly used for a composite component — a component whose implementation depends on child components. For example, `JTable`s make all their bindings using `WHEN_ANCESTOR_OF_FOCUSED_COMPONENT` so that if the user is editing, the up-arrow key (for example) still changes the selected cell. `JComponent.WHEN_IN_FOCUSED_WINDOW`: The component's window either has the focus or contains the component that has the focus. This input map is commonly used for mnemonics or accelerators, which need to be active regardless of where focus is in the window.
>
> When the user types a key,
> the `JComponent` key event processing code
> searches through one or more input maps
> to find a valid binding for the key.
> When it finds a binding,
> it looks up the corresponding action
> in the action map.
> If the action is enabled, the binding is valid and the action is executed.
> If it's disabled, the search for a valid binding continues.
>
> If more than one binding exists for the key,
> only the first valid one found is used.
> Input maps are checked in this order:
>
> 1. The focused component's `WHEN_FOCUSED` input map.- The focused component's `WHEN_ANCESTOR_OF_FOCUSED_COMPONENT` input map.- The `WHEN_ANCESTOR_OF_FOCUSED_COMPONENT` input maps of
>        the focused component's parent,
>        and then its parent's parent, and so on,
>        continuing up the containment hierarchy.
>        Note: Input maps for disabled components are skipped.- The `WHEN_IN_FOCUSED_WINDOW` input maps of all the
>          enabled components
>          in the focused window are searched.
>          Because the order of searching the components is unpredictable,
>          **avoid duplicate `WHEN_IN_FOCUSED_WINDOW` bindings!**
>
> Let's consider what happens in two typical key binding cases:
> a button reacting to the Space key,
> and a frame with a default button
> reacting to the Enter key.
>
> In the first case, assume the user presses the Space key
> while a `JButton` has the keyboard focus.
> First, the button's key listeners are notified of the event.
> Assuming none of the key listeners *consumes* the event
> (by invoking the
> [`consume`](http://download.oracle.com/javase/7/docs/api/java/awt/event/InputEvent.html#consume()) method on the `KeyEvent`)
> the button's `WHEN_FOCUSED` input map is consulted.
> A binding is found because `JButton` uses that input map
> to bind Space to an action name.
> The action name is looked up in the button's action map,
> and the `actionPerformed` method of the action is invoked.
> The `KeyEvent` is consumed,
> and processing stops.
>
> In the second case,
> assume the Enter key is pressed
> while the focus is anywhere inside a frame that has a default button
> (set using the `JRootPane`
> [`setDefaultButton`](http://download.oracle.com/javase/7/docs/api/javax/swing/JRootPane.html#setDefaultButton(javax.swing.JButton)) method).
> Whatever the focused component is,
> its key listeners are first notified.
> Assuming none of them consumes the key event
> the focused component's `WHEN_FOCUSED` input map is consulted.
> If it has no binding for the key or
> the Action bound to the key is disabled,
> the focused component's `WHEN_ANCESTOR_OF_FOCUSED_COMPONENT`
> input map is consulted
> and then (if no binding is found or the Action bound to the key is disabled)
> the `WHEN_ANCESTOR_OF_FOCUSED_COMPONENT` input maps
> of each of the component's ancestors in the containment hierarchy.
> Eventually, the root pane's
> `WHEN_ANCESTOR_OF_FOCUSED_COMPONENT` input map
> is searched.
> Since that input map has a valid binding for Enter,
> the action is executed,
> causing the default button to be clicked.

### How to Make and Remove Key Bindings

> Here is an example of specifying that a component
> should react to the F2 key:
> > ```
> >
> > component.getInputMap().put(KeyStroke.getKeyStroke("F2"),
> >                             "doSomething");
> > component.getActionMap().put("doSomething",
> >                              anAction);
> > //where anAction is a javax.swing.Action
> >
> > ```
>
> As the preceding code shows,
> to get a component's action map
> you use the `getActionMap` method
> (inherited from `JComponent`).
> To get an input map,
> you can use the `getInputMap(int)` method,
> where the integer is one of the `JComponent.WHEN_*FOCUSED*`
> constants shown in the preceding list.
> Or, in the usual case where the constant is
> `JComponent.WHEN_FOCUSED`,
> you can just use `getInputMap` with no arguments.
>
> To add an entry to one of the maps,
> use the `put` method.
> You specify a key
> using a `KeyStroke` object,
> which you can get using the
> [`KeyStroke.getKeyStroke(String)`](http://download.oracle.com/javase/7/docs/api/javax/swing/KeyStroke.html#getKeyStroke(java.lang.String)) method.
> You can find examples of creating an `Action`
> (to put in an action map) in
> [How to Use Actions](../misc/action.html).
>
> Here's a slightly more complex example that specifies that a component
> should react to the Space key as if the user clicked the mouse.
> > ```
> >
> > component.getInputMap().put(KeyStroke.getKeyStroke("SPACE"),
> >                             "pressed");
> > component.getInputMap().put(KeyStroke.getKeyStroke("released SPACE"),
> >                             "released");
> > component.getActionMap().put("pressed",
> >                              pressedAction);
> > component.getActionMap().put("released",
> >                              releasedAction);
> > //where pressedAction and releasedAction are javax.swing.Action objects
> >
> > ```
>
> To make a component ignore a key that it normally responds to,
> you can use the special action name "none".
> For example, the following code makes a component ignore the F2 key.
>
> > ```
> >
> > component.getInputMap().put(KeyStroke.getKeyStroke("F2"),
> >                             "none");
> >
> > ```
>
> ---
>
> **Note:** The preceding code doesn't prevent
> the relevant
> `WHEN_ANCESTOR_OF_FOCUSED_COMPONENT` and
> `WHEN_IN_FOCUSED_WINDOW` input maps
> from being searched
> for an F2 key binding.
> To prevent this search,
> you must use a valid action instead of "none".
> For example:
>
> ```
>
> Action doNothing = new AbstractAction() {
>     public void actionPerformed(ActionEvent e) {
>         //do nothing
>     }
> };
> component.getInputMap().put(KeyStroke.getKeyStroke("F2"),
>                             "doNothing");
> component.getActionMap().put("doNothing",
>                              doNothing);
>
> ```
>
> ---

### The Key Binding API

> The following tables list the commonly used API
> for key bindings.
> Also see the API table
> [Creating and Using an Action](action.html#actionapi), in the section
> [How to Use Actions](action.html).
>
> * [Creating and Using InputMaps](#inputmap)* [Creating and Using ActionMaps](#actionmap)
>
> Getting and Using InputMaps
>
> | Method | Purpose |
> | [InputMap getInputMap()](http://download.oracle.com/javase/7/docs/api/javax/swing/JComponent.html#getInputMap())   [InputMap getInputMap(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JComponent.html#getInputMap(int))   *(in `JComponent`)* | Get one of the input maps for the component. The arguments can be one of these `JComponent` constants: `WHEN_FOCUSED`, `WHEN_IN_FOCUSED_WINDOW`, or `WHEN_ANCESTOR_OF_FOCUSED_COMPONENT`. The no-argument method gets the `WHEN_FOCUSED` input map. |
> | [void put(KeyStroke, Object)](http://download.oracle.com/javase/7/docs/api/javax/swing/InputMap.html#put(javax.swing.KeyStroke, java.lang.Object))   *(in `InputMap`)* | Set the action name associated with the specified key stroke. If the second argument is `null`, this method removes the binding for the key stroke. To make the key stroke be ignored, use `"none"` as the second argument. |
> | [static KeyStroke getKeyStroke(String)](http://download.oracle.com/javase/7/docs/api/javax/swing/KeyStroke.html#getKeyStroke(java.lang.String))   *(in `KeyStroke`)* | Get the object specifying a particular user keyboard activity. Typical arguments are "alt shift X", "INSERT", and "typed a". See the [`KeyStroke` API documentation](http://download.oracle.com/javase/7/docs/api/javax/swing/KeyStroke.html) for full details and for other forms of the `getKeyStroke` method. |
>
> Getting and Using ActionMaps
>
> | Method | Purpose |
> | [ActionMap getActionMap()](http://download.oracle.com/javase/7/docs/api/javax/swing/JComponent.html#getActionMap())   *(in `JComponent`)* | Get the object that maps names into actions for the component. |
> | [void put(Object, Action)](http://download.oracle.com/javase/7/docs/api/javax/swing/ActionMap.html#put(java.lang.Object, javax.swing.Action))   *(in `ActionMap`)* | Set the action associated with the specified name. If the second argument is `null`, this method removes the binding for the name. |

### Examples that Use Key Bindings

> The following table lists examples that
> use key bindings:
>
> | Example | Where Described | Notes |
> | --- | --- | --- |
> | [TableFTFEditDemo](../examples/components/index.html#TableFTFEditDemo) [How to Use Tables](../components/table.html) | The [IntegerEditor](../components/../examples/components/TableFTFEditDemoProject/src/components/IntegerEditor.java) class registers a key binding on a formatted text field to validate the input when the user presses the Enter key. | |
> | [TextComponentDemo](../examples/components/index.html#TextComponentDemo) [Text Component Features](../components/generaltext.html) | Key bindings are registered on a text pane to navigate through the text when the user presses the Control-B, Control-F, Control-P, and Control-N keys. | |

[« Previous](focus.html)
•
[Trail](../TOC.html)
•
[Next »](modality.html)

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

**Previous page:** How to Use the Focus Subsystem
  
**Next page:** How to Use Modality in Dialogs




A browser with JavaScript enabled is required for this page to operate properly.