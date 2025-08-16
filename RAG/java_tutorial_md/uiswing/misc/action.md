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

How to Use Actions

[How to Use Swing Timers](timer.html)

[How to Support Assistive Technologies](access.html)

[How to Use the Focus Subsystem](focus.html)

[How to Use Key Bindings](keybinding.html)

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

[« Previous](jlayer.html) • [Trail](../TOC.html) • [Next »](timer.html)

# How to Use Actions

An
[`Action`](http://download.oracle.com/javase/7/docs/api/javax/swing/Action.html)
can be used to separate functionality and state from a component. For
example, if you have two or more components that perform the same function,
consider using an `Action` object to implement the function.
An `Action` object is an
[action listener](../events/actionlistener.html)
that provides not only action-event handling, but also centralized handling
of the state of action-event-firing components such as
[tool bar buttons](../components/toolbar.html),
[menu items](../components/menu.html),
[common buttons](../components/button.html), and
[text fields](../components/textfield.html). The state that an action can handle includes text, icon, mnemonic, enabled,
and selected status.

You typically attach an action to a component using the
`setAction` method. Here's what happens when `setAction`
is invoked on a component:

* The component's state is updated to match the state of the
  `Action`.
  For example, if the `Action`'s text and icon values
  were set,
  the component's text and icon are set to those values.* The `Action` object is registered as an action listener
    on the component.* If the state of the `Action` changes,
      the component's state is updated to match the `Action`.
      For example, if you change the enabled status of the action,
      all components it's attached to change their enabled states
      to match the action.

Here's an example of creating a tool-bar button and menu item
that perform the same function:

```

Action leftAction = new LeftAction(); //LeftAction code is shown later
...
button = new JButton(leftAction)
...
menuItem = new JMenuItem(leftAction);

```

To create an `Action` object,
you generally create a subclass of
[`AbstractAction`](http://download.oracle.com/javase/7/docs/api/javax/swing/AbstractAction.html) and then instantiate it.
In your subclass,
you must implement the `actionPerformed` method
to react appropriately
when the action event occurs.
Here's an example of creating and instantiating
an `AbstractAction` subclass:

```

leftAction = new LeftAction("Go left", anIcon,
             "This is the left button.",
             new Integer(KeyEvent.VK_L));
...
class LeftAction extends AbstractAction {
    public LeftAction(String text, ImageIcon icon,
                      String desc, Integer mnemonic) {
        super(text, icon);
        putValue(SHORT_DESCRIPTION, desc);
        putValue(MNEMONIC_KEY, mnemonic);
    }
    public void actionPerformed(ActionEvent e) {
        displayResult("Action for first button/menu item", e);
    }
}

```

When the action created by the preceding code is attached to a
button and a menu item, the button and menu item display the
text and icon associated with the action. The `L`
character is used for mnemonics on the button and menu item, and
their tool-tip text is set to the `SHORT_DESCRIPTION`
string followed by a representation of the mnemonic key.

For example, we have provided a simple example,
[`ActionDemo.java`](../examples/misc/ActionDemoProject/src/misc/ActionDemo.java), which defines three actions. Each action is attached to a button
and a menu item.
Thanks to the mnemonic values set for each button's action, the key
sequence `Alt-L` activates the left button, `Alt-M`
the middle button, and `Alt-R` the right button. The tool tip
for the left button displays *This is the left button. Alt-L.*
All of this configuration occurs automatically, without the program making
explicit calls to set the mnemonic or tool-tip text. As we'll show
later, the program *does* make calls to set the button text,
but only to avoid using the values already set by the actions.

![A snapshot of ActionDemo, which uses actions to coordinate menus and buttons.](../../figures/uiswing/misc/ActionDemo.png)

---

**Try this:**

1. Click the Launch button to run ActionDemo using
   [Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp)
   ([download
   JDK 6](http://java.sun.com/javase/downloads/index.jsp)). Or, to compile and run the example yourself, consult
   the [example
   index](../examples/misc/index.html#ActionDemo).

   [![Launches the ActionDemo example](../../images/jws-launch-button.png)](http://download.oracle.com/javase/tutorialJWS/uiswing/misc/ex6/ActionDemo.jnlp)
2. Choose the top item from the left menu (**Menu > Go left**).
     
   The text area displays some text identifying both the event source and
   the action listener that received the event.
3. Click the leftmost button in the tool bar.
     
   The text area again displays information about the event. Note that although
   the source of the events is different, both events were detected by the same
   action listener: the `Action` object attached to the
   components.
4. Choose the top item from the **Action State** menu.
     
   This disables the "Go left" `Action` object, which in turn
   disables its associated menu item and button.

---

Here is what the user sees
when the "Go left" action is disabled:

|  |  |
| --- | --- |
| A snapshot of ActionDemo when | A snapshot of ActionDemo when |

Here's the code that disables the "Go left" action:

```

boolean selected = ...//true if the action should be enabled;
                      //false, otherwise
leftAction.setEnabled(selected);

```

After you create components using an `Action`,
you might well need to customize them.
For example, you might want to customize the
appearance of one of the components
by adding or deleting the icon or text.
For example,
[`ActionDemo.java`](../examples/misc/ActionDemoProject/src/misc/ActionDemo.java)
has no icons in its menus, and no text in its buttons.
Here's the code that accomplishes this:

```

menuItem = new JMenuItem();
menuItem.setAction(leftAction);
menuItem.setIcon(null); //arbitrarily chose not to use icon in menu
...
button = new JButton();
button.setAction(leftAction);
button.setText(""); //an icon-only button

```

We chose to create an icon-only button and
a text-only menu item from the same action by setting
the icon property to `null` and the text
to an empty string.
However, if a property of the `Action` changes, the
widget may try to reset the icon and text from the
`Action` again.

### The Action API

> The following tables list the commonly used
> `Action` constructors and methods.
> The API for using `Action` objects
> falls into three categories:
>
> * [Components that Support set/getAction](#actioncomponents)* [Creating and Using an AbstractAction](#actionapi)* [Action Properties](#properties)
>
> Components that Support set/getAction
>
> | Class | Purpose |
> | [AbstractButton](http://download.oracle.com/javase/7/docs/api/javax/swing/AbstractButton.html#setAction(javax.swing.Action))  [JComboBox](http://download.oracle.com/javase/7/docs/api/javax/swing/JComboBox.html#setAction(javax.swing.Action))  [JTextField](http://download.oracle.com/javase/7/docs/api/javax/swing/JTextField.html#setAction(javax.swing.Action)) | These components and their subclasses may have an action directly assigned to them via `setAction`. For further information about components that are often associated with actions, see the sections on [tool bar buttons](../components/toolbar.html), [menu items](../components/menu.html), [common buttons](../components/button.html), and [text fields](../components/textfield.html). For details on which properties each component takes from the `Action`, see the API documentation for the relevant class's [`configurePropertiesFromAction`](http://download.oracle.com/javase/7/docs/api/javax/swing/JMenuItem.html#configurePropertiesFromAction(javax.swing.Action)) method. Also refer to the [`buttonActions`](http://download.oracle.com/javase/7/docs/api/javax/swing/Action.html#buttonActions) table. |
>
> Creating and Using an AbstractAction
>
> | Constructor or Method | Purpose |
> | [AbstractAction()](http://download.oracle.com/javase/7/docs/api/javax/swing/AbstractAction.html#AbstractAction())   [AbstractAction(String)](http://download.oracle.com/javase/7/docs/api/javax/swing/AbstractAction.html#AbstractAction(java.lang.String))   [AbstractAction(String, Icon)](http://download.oracle.com/javase/7/docs/api/javax/swing/AbstractAction.html#AbstractAction(java.lang.String, javax.swing.Icon)) | Create an `Action` object. Through arguments, you can specify the text and icon to be used in the components that the action is attached to. |
> | [void setEnabled(boolean)](http://download.oracle.com/javase/7/docs/api/javax/swing/AbstractAction.html#setEnabled(boolean))   [boolean isEnabled()](http://download.oracle.com/javase/7/docs/api/javax/swing/AbstractAction.html#isEnabled()) | Set or get whether the components the action controls are enabled. Invoking `setEnabled(false)` disables all the components that the action controls. Similarly, invoking `setEnabled(true)` enables the action's components. |
> | [void putValue(String, Object)](http://download.oracle.com/javase/7/docs/api/javax/swing/AbstractAction.html#putValue(java.lang.String, java.lang.Object))  [Object getValue(String)](http://download.oracle.com/javase/7/docs/api/javax/swing/AbstractAction.html#getValue(java.lang.String)) | Set or get an object associated with a specified key. Used for setting and getting properties associated with an action. |
>
> Action Properties
>
> This table defines the properties that can be set on an
> action. The second column lists which components automatically
> use the properties (and what method is specifically called).
> For example,
> setting the `ACCELERATOR_KEY` on an action that
> is then attached to a menu item, means that
> `JMenuItem.setAccelerator(KeyStroke)`
> is called automatically.
>
> | Property | Auto-Applied to:  Class  *(Method Called)* | Purpose |
> | --- | --- | --- |
> | [ACCELERATOR\_KEY](http://download.oracle.com/javase/7/docs/api/javax/swing/Action.html#ACCELERATOR_KEY) | `JMenuItem`  (*setAccelerator*) | The `KeyStroke` to be used as the accelerator for the action. For a discussion of accelerators versus mnemonics, see [Enabling Keyboard Operation.](../components/menu.html#mnemonic) Introduced in 1.3. |
> | [ACTION\_COMMAND\_KEY](http://download.oracle.com/javase/7/docs/api/javax/swing/Action.html#ACTION_COMMAND_KEY) | `AbstractButton`, `JCheckBox`, `JRadioButton`  (*setActionCommand*) | The command string associated with the `ActionEvent`. |
> | [LONG\_DESCRIPTION](http://download.oracle.com/javase/7/docs/api/javax/swing/Action.html#LONG_DESCRIPTION) | None | The longer description for the action. Can be used for context-sensitive help. |
> | [MNEMONIC\_KEY](http://download.oracle.com/javase/7/docs/api/javax/swing/Action.html#MNEMONIC_KEY) | `AbstractButton`, `JMenuItem`, `JCheckBox`, `JRadioButton`  (*setMnemonic*) | The mnemonic for the action. For a discussion of accelerators versus mnemonics, see [Enabling Keyboard Operation.](../components/menu.html#mnemonic) Introduced in 1.3. |
> | [NAME](http://download.oracle.com/javase/7/docs/api/javax/swing/Action.html#NAME) | `AbstractButton`, `JMenuItem`, `JCheckBox`, `JRadioButton`  (*setText*) | The name of the action. You can set this property when creating the action using the `AbstractAction(String)` or `AbstractAction(String, Icon)` constructors. |
> | [SHORT\_DESCRIPTION](http://download.oracle.com/javase/7/docs/api/javax/swing/Action.html#SHORT_DESCRIPTION) | `AbstractButton`, `JCheckBox`, `JRadioButton`  (*setToolTipText*) | The short description of the action. |
> | [SMALL\_ICON](http://download.oracle.com/javase/7/docs/api/javax/swing/Action.html#SMALL_ICON) | `AbstractButton`, `JMenuItem`  (*setIcon*) | The icon for the action used in the tool bar or on a button. You can set this property when creating the action using the `AbstractAction(name, icon)` constructor. |

### Examples that Use Actions

> The following examples
> use `Action` objects.
>
> | Example | Where Described | Notes |
> | --- | --- | --- |
> | [`ActionDemo`](../examples/misc/index.html#ActionDemo) | This section | Uses actions to bind buttons and menu items to the same function. |
> | [`TextComponentDemo`](../examples/components/index.html#TextComponentDemo) | [Text Component Features](../components/generaltext.html) | Uses text actions to create menu items for text editing commands, such as cut, copy, and paste, and to bind key strokes to caret movement. Also implements custom `AbstractAction` subclasses to implement undo and redo. The text action discussion begins in [Concepts: About Editor Kits](../components/generaltext.html#editorkits). |

[« Previous](jlayer.html)
•
[Trail](../TOC.html)
•
[Next »](timer.html)

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

**Previous page:** How to Decorate Components with JLayer
  
**Next page:** How to Use Swing Timers




A browser with JavaScript enabled is required for this page to operate properly.