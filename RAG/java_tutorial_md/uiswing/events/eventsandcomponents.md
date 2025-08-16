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

Listeners Supported by Swing Components

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

[« Previous](generalrules.html) • [Trail](../TOC.html) • [Next »](handling.html)

# Listeners Supported by Swing Components

You can tell
what kinds of events a component can fire by looking at the kinds
of event listeners you can register on it.
For example, the `JComboBox`
class defines these listener registration methods:

* `addActionListener`* `addItemListener`* `addPopupMenuListener`

Thus, a combo box supports action,
item, and popup menu listeners in addition to the listener
methods it inherits from `JComponent`.

Listeners supported by Swing components
fall into two categories:

* [Listeners that All Swing Components Support](#all)* [Other Listeners that Swing Components Support](#many)

### Listeners that All Swing Components Support
> Because all Swing components descend from
> the AWT `Component` class,
> you can register the following listeners on any
> Swing component:
>
> **[component listener](componentlistener.html)**: Listens for changes in the component's size, position, or visibility. **[focus listener](focuslistener.html)**: Listens for whether the component gained or lost the keyboard focus. **[key listener](keylistener.html)**: Listens for key presses; key events are fired only by the component that has the current keyboard focus. **[mouse listener](mouselistener.html)**: Listens for mouse clicks, mouse presses, mouse releases and mouse movement into or out of the component's drawing area. **[mouse-motion listener](mousemotionlistener.html)**: Listens for changes in the mouse cursor's position over the component. **[mouse-wheel listener](mousewheellistener.html)**: Listens for mouse wheel movement over the component. **[Hierarchy Listener](http://java.sun.com/javase/6/docs/api/java/awt/event/HierarchyListener.html)**: Listens for changes to a component's containment hierarchy of changed events. **[Hierarchy Bounds Listener](http://java.sun.com/javase/6/docs/api/java/awt/event/HierarchyBoundsListener.html)**: Listens for changes to a component's containment hierarchy of moved and resized events.
>
> All Swing components descend from the AWT `Container`
> class, but many of them are not used as containers.
> So, technically speaking, any Swing component can fire
> [container events](containerlistener.html),
> which notify listeners that a component
> has been added to or removed from the container.
> Realistically speaking, however, only containers
> (such as panels and frames)
> and compound components (such as combo boxes)
> typically fire container events.
>
> `JComponent`
> provides support for three more listener types.
> You can register an
> [ancestor listener](http://download.oracle.com/javase/7/docs/api/javax/swing/event/AncestorListener.html) to be notified when a component's
> containment ancestors are added to or removed from a container,
> hidden, made visible, or moved.
> This listener type is an implementation detail which predated
> hierarchy listeners.
>
> The other two listener types are part of the Swing components'
> conformance to the
> JavaBeansTM specification.
> Among other things, this means that Swing components support
> bound and constrained properties
> and notify listeners of changes to the properties.
> [Property change listeners](propertychangelistener.html)
> listen for changes to bound properties and are used by
> several Swing components, such as
> [formatted text fields](../components/formattedtextfield.html), to track changes on a component's bound properties.
> Also, property change listeners, as well as
> [vetoable change listeners](http://download.oracle.com/javase/7/docs/api/java/beans/VetoableChangeListener.html) are used by builder tools to
> listen for changes on constrained properties.
> For more information refer to the
> [Properties](../../javabeans/properties/index.html) lesson in the
> [JavaBeans](../../javabeans/) trail.

### Other Listeners that Swing Components Support
> The following table lists Swing components
> and the specialized listeners they support, not including
> listeners supported by all `Component`s,
> `Container`s, or `JComponent`s.
> In many cases, the events are fired
> directly from the component.
> In other cases, the events are fired
> from the component's data or selection model.
> To find out the details for the
> particular component and listener you are interested in,
> go first to the component how-to section,
> and then if necessary to the listener how-to section.
>
> This table lists Swing components with their specialized listeners
>
> | **Component** | **Listener** | | | | | | | | |
> | [action](actionlistener.html) | [caret](caretlistener.html) | [change](changelistener.html) | [document](documentlistener.html),  [undoable edit](undoableeditlistener.html) | [item](itemlistener.html) | [list selection](listselectionlistener.html) | [window](windowlistener.html) | other |
> | [button](../components/button.html) | checked |  | checked |  | checked |  |  |  |
> | [check box](../components/button.html#checkbox) | checked |  | checked |  | checked |  |  |  |
> | [color chooser](../components/colorchooser.html) |  |  | checked |  |  |  |  |  |
> | [combo box](../components/combobox.html) | checked |  |  |  | checked |  |  |  |
> | [dialog](../components/dialog.html) |  |  |  |  |  |  | checked |  |
> | [editor pane](../components/editorpane.html) |  | checked |  | checked |  |  |  | [hyperlink](http://download.oracle.com/javase/7/docs/api/javax/swing/event/HyperlinkListener.html) |
> | [file chooser](../components/filechooser.html) | checked |  |  |  |  |  |  |  |
> | [formatted text field](../components/formattedtextfield.html) | checked | checked |  | checked |  |  |  |  |
> | [frame](../components/frame.html) |  |  |  |  |  |  | checked |  |
> | [internal frame](../components/internalframe.html) |  |  |  |  |  |  |  | [internal frame](internalframelistener.html) |
> | [list](../components/list.html) |  |  |  |  |  | checked |  | [list data](listdatalistener.html) |
> | [menu](../components/menu.html) |  |  |  |  |  |  |  | [menu](http://download.oracle.com/javase/7/docs/api/javax/swing/event/MenuListener.html) |
> | [menu item](../components/menu.html) | checked |  | checked |  | checked |  |  | [menu key](http://download.oracle.com/javase/7/docs/api/javax/swing/event/MenuKeyListener.html)   [menu drag mouse](http://download.oracle.com/javase/7/docs/api/javax/swing/event/MenuDragMouseListener.html) |
> | [option pane](../components/dialog.html) |  |  |  |  |  |  |  |  |
> | [password field](../components/passwordfield.html) | checked | checked |  | checked |  |  |  |  |
> | [popup menu](../components/menu.html) |  |  |  |  |  |  |  | [popup menu](http://download.oracle.com/javase/7/docs/api/javax/swing/event/PopupMenuListener.html) |
> | [progress bar](../components/progress.html) |  |  | checked |  |  |  |  |  |
> | [radio button](../components/button.html#radiobutton) | checked |  | checked |  | checked |  |  |  |
> | [slider](../components/slider.html) |  |  | checked |  |  |  |  |  |
> | [spinner](../components/spinner.html) |  |  | checked |  |  |  |  |  |
> | [tabbed pane](../components/tabbedpane.html) |  |  | checked |  |  |  |  |  |
> | [table](../components/table.html) |  |  |  |  |  | checked |  | [table model](tablemodellistener.html)   [table column model](http://download.oracle.com/javase/7/docs/api/javax/swing/event/TableColumnModelListener.html)   [cell editor](http://download.oracle.com/javase/7/docs/api/javax/swing/event/CellEditorListener.html) |
> | [text area](../components/textarea.html) |  | checked |  | checked |  |  |  |  |
> | [text field](../components/textfield.html) | checked | checked |  | checked |  |  |  |  |
> | [text pane](../components/editorpane.html) |  | checked |  | checked |  |  |  | [hyperlink](http://download.oracle.com/javase/7/docs/api/javax/swing/event/HyperlinkListener.html) |
> | [toggle button](../components/button.html) | checked |  | checked |  | checked |  |  |  |
> | [tree](../components/tree.html) |  |  |  |  |  |  |  | [tree expansion](treeexpansionlistener.html)   [tree will expand](treewillexpandlistener.html)   [tree model](treemodellistener.html)   [tree selection](treeselectionlistener.html) |
> | viewport   (used by [scrollpane](../components/scrollpane.html)) |  |  | checked |  |  |  |  |  |

[« Previous](generalrules.html)
•
[Trail](../TOC.html)
•
[Next »](handling.html)

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

**Previous page:** General Information about Writing Event Listeners
  
**Next page:** Implementing Listeners for Commonly Handled Events




A browser with JavaScript enabled is required for this page to operate properly.