[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Creating a GUI With JFC/Swing
  
**Lesson:** Using Swing Components
  
**Section:** How to Use Various Components

[Using Swing Components](index.html)

[Using Top-Level Containers](toplevel.html)

[The JComponent Class](jcomponent.html)

[Using Text Components](text.html)

[Text Component Features](generaltext.html)

[The Text Component API](textapi.html)

[How to Use Various Components](componentlist.html)

[How to Make Applets](applet.html)

[How to Use Buttons, Check Boxes, and Radio Buttons](button.html)

[How to Use the ButtonGroup Component](buttongroup.html)

[How to Use Color Choosers](colorchooser.html)

[How to Use Combo Boxes](combobox.html)

[How to Make Dialogs](dialog.html)

[How to Use Editor Panes and Text Panes](editorpane.html)

[How to Use File Choosers](filechooser.html)

[How to Use Formatted Text Fields](formattedtextfield.html)

[How to Make Frames (Main Windows)](frame.html)

[How to Use Internal Frames](internalframe.html)

[How to Use Labels](label.html)

[How to Use Layered Panes](layeredpane.html)

[How to Use Lists](list.html)

How to Use Menus

[How to Use Panels](panel.html)

[How to Use Password Fields](passwordfield.html)

[How to Use Progress Bars](progress.html)

[How to Use Root Panes](rootpane.html)

[How to Use Scroll Panes](scrollpane.html)

[How to Use Separators](separator.html)

[How to Use Sliders](slider.html)

[How to Use Spinners](spinner.html)

[How to Use Split Panes](splitpane.html)

[How to Use Tabbed Panes](tabbedpane.html)

[How to Use Tables](table.html)

[How to Use Text Areas](textarea.html)

[How to Use Text Fields](textfield.html)

[How to Use Tool Bars](toolbar.html)

[How to Use Tool Tips](tooltip.html)

[How to Use Trees](tree.html)

[How to Use HTML in Swing Components](html.html)

[How to Use Models](model.html)

[How to Use Icons](icon.html)

[How to Use Borders](border.html)

[Solving Common Component Problems](problems.html)

[Home Page](../../index.html)
>
[Creating a GUI With JFC/Swing](../index.html)
>
[Using Swing Components](index.html)

[« Previous](list.html) • [Trail](../TOC.html) • [Next »](panel.html)

# How to Use Menus

A menu provides a space-saving way to let the user
choose one of several options.
Other components with which the user can make a one-of-many choice
include
[combo boxes](combobox.html),
[lists](list.html),
[radio buttons](button.html#radiobutton),
[spinners](spinner.html), and
[tool bars](toolbar.html).
If any of your menu items performs an action that is duplicated
by another menu item or by a tool-bar button,
then in addition to this section you should read
[How to Use Actions](../misc/action.html).

Menus are unique in that, by convention,
they aren't placed with the other components in the UI.
Instead, a menu usually appears either in a *menu bar*
or as a *popup menu*.
A menu bar contains one or more menus
and has a customary, platform-dependent location —
usually along the top of a window.
A popup menu is a menu that is invisible
until the user makes a platform-specific mouse action,
such as pressing the right mouse button,
over a popup-enabled component.
The popup menu then appears under the cursor.

The following figure shows many menu-related components:
a menu bar,
menus, menu items,
radio button menu items, check box menu items,
and separators.
As you can see, a menu item can have either an image or text, or both.
You can also specify other properties, such as font and color.

![MenuLookDemo](../../figures/uiswing/components/MenuLookDemo.png)

The rest of this section teaches you about the menu components
and tells you how to use
various menu features:

* [The menu component hierarchy](#hierarchy)* [Creating menus](#create)* [Handling events from menu items](#event)* [Enabling keyboard operation](#mnemonic)* [Bringing up a popup menu](#popup)* [Customizing menu layout](#custom)* [The Menu API](#api)* [Examples that use menus](#eg)

### The Menu Component Hierarchy

> Here is a picture of the inheritance hierarchy for the menu-related classes:
>
> ![The inheritance hierarchy for menu classes](../../figures/uiswing/components/object.gif)
>
> As the figure shows, menu items (including menus) are simply
> [buttons](button.html).
> You might be wondering how a menu,
> if it's only a button, shows its menu items.
> The answer is that when a menu is activated,
> it automatically brings up a popup menu
> that displays the menu items.

### Creating Menus

> The following code
> creates the menus shown near the beginning of this menu section.
> The bold lines of code create and connect the menu objects;
> the other code sets up or customizes the menu objects.
> You can find the entire program in
> [`MenuLookDemo.java`](../examples/components/MenuLookDemoProject/src/components/MenuLookDemo.java).
> Other required files are listed in the
> [example index](../examples/components/index.html#MenuLookDemo).
>
> ---
>
> **Try this:**
>
> * Click the Launch button to run the MenuLook Demo using
>   [Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp) ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
>   Alternatively, to compile and run the example yourself,
>   consult the
>   [example index](../examples/components/index.html#MenuLookDemo).
>
>   [![Launches the ButtonDemo example](../../images/jws-launch-button.png)](http://download.oracle.com/javase/tutorialJWS/uiswing/components/ex6/MenuLookDemo.jnlp)
>
> ---


Because this code has no event handling,
the menus do nothing useful
except to look as they should.
If you run the example,
you'll notice that despite the lack of custom event handling,
menus and submenus appear when they should,
and the check boxes and radio buttons
respond appropriately when the user chooses them.

```

//Where the GUI is created:
JMenuBar menuBar;
JMenu menu, submenu;
JMenuItem menuItem;
JRadioButtonMenuItem rbMenuItem;
JCheckBoxMenuItem cbMenuItem;

//Create the menu bar.
menuBar = new JMenuBar();

//Build the first menu.
menu = new JMenu("A Menu");
menu.setMnemonic(KeyEvent.VK_A);
menu.getAccessibleContext().setAccessibleDescription(
        "The only menu in this program that has menu items");
menuBar.add(menu);

//a group of JMenuItems
menuItem = new JMenuItem("A text-only menu item",
                         KeyEvent.VK_T);
menuItem.setAccelerator(KeyStroke.getKeyStroke(
        KeyEvent.VK_1, ActionEvent.ALT_MASK));
menuItem.getAccessibleContext().setAccessibleDescription(
        "This doesn't really do anything");
menu.add(menuItem);

menuItem = new JMenuItem("Both text and icon",
                         new ImageIcon("images/middle.gif"));
menuItem.setMnemonic(KeyEvent.VK_B);
menu.add(menuItem);

menuItem = new JMenuItem(new ImageIcon("images/middle.gif"));
menuItem.setMnemonic(KeyEvent.VK_D);
menu.add(menuItem);

//a group of radio button menu items
menu.addSeparator();
ButtonGroup group = new ButtonGroup();
rbMenuItem = new JRadioButtonMenuItem("A radio button menu item");
rbMenuItem.setSelected(true);
rbMenuItem.setMnemonic(KeyEvent.VK_R);
group.add(rbMenuItem);
menu.add(rbMenuItem);

rbMenuItem = new JRadioButtonMenuItem("Another one");
rbMenuItem.setMnemonic(KeyEvent.VK_O);
group.add(rbMenuItem);
menu.add(rbMenuItem);

//a group of check box menu items
menu.addSeparator();
cbMenuItem = new JCheckBoxMenuItem("A check box menu item");
cbMenuItem.setMnemonic(KeyEvent.VK_C);
menu.add(cbMenuItem);

cbMenuItem = new JCheckBoxMenuItem("Another one");
cbMenuItem.setMnemonic(KeyEvent.VK_H);
menu.add(cbMenuItem);

//a submenu
menu.addSeparator();
submenu = new JMenu("A submenu");
submenu.setMnemonic(KeyEvent.VK_S);

menuItem = new JMenuItem("An item in the submenu");
menuItem.setAccelerator(KeyStroke.getKeyStroke(
        KeyEvent.VK_2, ActionEvent.ALT_MASK));
submenu.add(menuItem);

menuItem = new JMenuItem("Another item");
submenu.add(menuItem);
menu.add(submenu);

//Build second menu in the menu bar.
menu = new JMenu("Another Menu");
menu.setMnemonic(KeyEvent.VK_N);
menu.getAccessibleContext().setAccessibleDescription(
        "This menu does nothing");
menuBar.add(menu);

...
frame.setJMenuBar(theJMenuBar);

```

As the code shows,
to set the menu bar for a `JFrame`,
you use the `setJMenuBar` method.
To add a `JMenu` to a `JMenuBar`,
you use the `add(JMenu)` method.
To add menu items and submenus to a `JMenu`,
you use the `add(JMenuItem)` method.

---

**Note:** Menu items, like other components,
can be in at most one container.
If you try to add a menu item to a second menu,
the menu item will be removed from the first menu
before being added to the second.
For a way of implementing multiple components that do the same thing,
see
[How to Use Actions](../misc/action.html).

---

Other methods
in the preceding code include `setAccelerator` and
`setMnemonic`,
which are discussed a little later in
[Enabling Keyboard Operation](#mnemonic).
The `setAccessibleDescription` method
is discussed in
[How to Support Assistive Technologies](../misc/access.html).

### Handling Events from Menu Items

> To detect when the user chooses a `JMenuItem`,
> you can listen for action events
> (just as you would for a
> [`JButton`](button.html)).
> To detect when the user chooses a `JRadioButtonMenuItem`,
> you can listen for either action events or
> item events,
> as described in
> [How to Use Radio Buttons](button.html#radiobutton).
> For `JCheckBoxMenuItem`s,
> you generally listen for item events,
> as described in
> [How to Use Check Boxes](button.html#checkbox).
>
> ---
>
> **Try this:**
>
> * Click the Launch button to run the Menu Demo using
>   [Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp) ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
>   Alternatively, to compile and run the example yourself,
>   consult the
>   [example index](../examples/components/index.html#MenuDemo).
>
>   [![Launches the ButtonDemo example](../../images/jws-launch-button.png)](http://download.oracle.com/javase/tutorialJWS/uiswing/components/ex6/MenuDemo.jnlp)
>
> ---



![The text area shows the action and item events our listeners detected.](../../figures/uiswing/components/MenuDemo.png)

Here is the code that implements
the event handling:

```

public class MenuDemo ... implements ActionListener,
                                     ItemListener {
    ...
    public MenuDemo() {
        //...for each JMenuItem instance:
        menuItem.addActionListener(this);
        ...
        //for each JRadioButtonMenuItem: 
        rbMenuItem.addActionListener(this);
        ...
        //for each JCheckBoxMenuItem: 
        cbMenuItem.addItemListener(this);
        ...
    }

    public void actionPerformed(ActionEvent e) {
        //...Get information from the action event...
        //...Display it in the text area...
    }

    public void itemStateChanged(ItemEvent e) {
        //...Get information from the item event...
        //...Display it in the text area...
    }

```

For examples of handling action and item events,
see the [button](button.html),
[radio button](button.html#radiobutton), and
[check box](button.html#checkbox) sections,
as well as the [list of examples](#eg)
at the end of this section.

### Enabling Keyboard Operation

> Menus support two kinds of keyboard alternatives:
> mnemonics and accelerators.
> *Mnemonics* offer a way to use the keyboard to navigate
> the menu hierarchy,
> increasing the accessibility of programs.
> *Accelerators*, on the other hand,
> offer keyboard shortcuts to *bypass* navigating
> the menu hierarchy.
> Mnemonics are for all users;
> accelerators are for power users.
>
> A mnemonic is a key that
> makes an already visible menu item be chosen.
> For example, in `MenuDemo`
> the first menu has the mnemonic A,
> and its second menu item has the mnemonic B.
> This means that, when you run `MenuDemo`
> with the Java look and feel,
> pressing the Alt and A keys makes
> the first menu appear.
> While the first menu is visible,
> pressing the B key (with or without Alt)
> makes the second menu item be chosen.
> A menu item generally displays its mnemonic
> by underlining the first occurrence of the mnemonic character
> in the menu item's text,
> as the following snapshot shows.
>
> ![B is the mnemonic character for this menu item](../../figures/uiswing/components/Menu-mnemonic.png)
>
> An accelerator is a key combination
> that causes a menu item to be chosen,
> whether or not it's visible.
> For example, pressing the Alt and 2 keys in `MenuDemo`
> makes the first item in the first menu's submenu be chosen,
> without bringing up any menus.
> Only leaf menu items — menus that don't bring up other menus —
> can have accelerators.
> The following snapshot shows how the Java look and feel
> displays a menu item that has an accelerator.
>
> ![Alt+2 advertises this menu item's accelerator](../../figures/uiswing/components/Menu-accel.png)
>
> You can specify a mnemonic either when constructing the menu item
> or with the `setMnemonic` method.
> To specify an accelerator,
> use the `setAccelerator` method.
> Here are examples of setting mnemonics and accelerators:
>
> ```
>
> //Setting the mnemonic when constructing a menu item:
> menuItem = new JMenuItem("A text-only menu item",
>                          KeyEvent.VK_T);
>
> //Setting the mnemonic after creation time:
> menuItem.setMnemonic(KeyEvent.VK_T);
>
> //Setting the accelerator:
> menuItem.setAccelerator(KeyStroke.getKeyStroke(
>         KeyEvent.VK_T, ActionEvent.ALT_MASK));
>
> ```
>
> As you can see,
> you set a mnemonic
> by specifying the
> [`KeyEvent`](http://download.oracle.com/javase/7/docs/api/java/awt/event/KeyEvent.html) constant corresponding to the key the user should press.
> To specify an accelerator you must use a
> [`KeyStroke`](http://download.oracle.com/javase/7/docs/api/javax/swing/KeyStroke.html) object,
> which combines a key
> (specified by a `KeyEvent` constant)
> and a modifier-key mask
> (specified by an
> [`ActionEvent`](http://download.oracle.com/javase/7/docs/api/java/awt/event/ActionEvent.html) constant).
>
> ---
>
> **Note:** Because popup menus, unlike regular menus,
> aren't always contained by a component,
> accelerators in popup menu items
> don't work unless the popup menu is visible.
>
> ---

### Bringing Up a Popup Menu

> To bring up a popup menu
> (
> [`JPopupMenu`](http://download.oracle.com/javase/7/docs/api/javax/swing/JPopupMenu.html)), you must register a mouse listener
> on each component
> that the popup menu should be associated with.
> The mouse listener must detect
> user requests that the popup menu be brought up.
>
> The exact gesture that should bring up a popup menu varies
> by look and feel.
> In Microsoft Windows,
> the user by convention brings up a popup menu
> by releasing the right mouse button
> while the cursor is over a component
> that is popup-enabled.
> In the Java look and feel, the customary trigger
> is either pressing the right mouse button
> (for a popup that goes away when the button is released)
> or clicking it
> (for a popup that stays up).
>
> ---
>
> **Try this:**
>
> * Click the Launch button to run the PopupMenu Demo using
>   [Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp) ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
>   Alternatively, to compile and run the example yourself,
>   consult the
>   [example index](../examples/components/index.html#PopupMenuDemo).
>
>   [![Launches the PopupMenuDemo example](../../images/jws-launch-button.png)](http://download.oracle.com/javase/tutorialJWS/uiswing/components/ex6/PopupMenuDemo.jnlp)
>
> ---




```

//...where instance variables are declared:
JPopupMenu popup;

    //...where the GUI is constructed:
    //Create the popup menu.
    popup = new JPopupMenu();
    menuItem = new JMenuItem("A popup menu item");
    menuItem.addActionListener(this);
    popup.add(menuItem);
    menuItem = new JMenuItem("Another popup menu item");
    menuItem.addActionListener(this);
    popup.add(menuItem);

    //Add listener to components that can bring up popup menus.
    MouseListener popupListener = new PopupListener();
    output.addMouseListener(popupListener);
    menuBar.addMouseListener(popupListener);
...
class PopupListener extends MouseAdapter {
    public void mousePressed(MouseEvent e) {
        maybeShowPopup(e);
    }

    public void mouseReleased(MouseEvent e) {
        maybeShowPopup(e);
    }

    private void maybeShowPopup(MouseEvent e) {
        if (e.isPopupTrigger()) {
            popup.show(e.getComponent(),
                       e.getX(), e.getY());
        }
    }
}

```

Popup menus have a few
interesting implementation details.
One is that
every menu has an associated popup menu.
When the menu
is activated,
it uses its associated popup menu
to show its menu items.

Another detail is that a popup menu itself
uses another component
to implement the window containing the menu items.
Depending on the circumstances under which
the popup menu is displayed,
the popup menu might implement its "window" using
a lightweight component (such as a `JPanel`),
a "mediumweight" component (such as a
[`Panel`](http://download.oracle.com/javase/7/docs/api/java/awt/Panel.html)),
or a heavyweight window (something that inherits from
[`Window`](http://download.oracle.com/javase/7/docs/api/java/awt/Window.html)).

Lightweight popup windows are more efficient than
heavyweight windows but, prior to the
Java SE Platform 6 Update 12 release, they didn't work well
if you had any heavyweight components inside your GUI.
Specifically, when the lightweight popup's display area
intersects the heavyweight component's display area,
the heavyweight component is drawn on top.
This is one of the reasons that, prior to the 6u12 release,
we recommended against mixing heavyweight and lightweight components.
If you are using an older release and absolutely need to use a heavyweight
component in your GUI, then you can invoke
`JPopupMenu.setLightWeightPopupEnabled(false)`
to disable lightweight popup windows.
For information on mixing components in the 6u12 release and later, please see
[Mixing Heavyweight and Lightweight Components](http://java.sun.com/developer/technicalArticles/GUI/mixing_components/index.html).

### Customizing Menu Layout

Because menus are made up of ordinary Swing components,
you can easily customize them.
For example,
you can add any lightweight component
to a `JMenu` or `JMenuBar`.
And because `JMenuBar` uses
[`BoxLayout`](../layout/box.html),
you can customize a menu bar's layout
just by adding invisible components to it.
Here is an example
of adding a [glue](../layout/box.html#filler) component to a menu bar,
so that
the last menu is at the right edge of the menu bar:

```

//...create and add some menus...
menuBar.add(Box.createHorizontalGlue());
//...create the rightmost menu...
menuBar.add(rightMenu);

```

---

**Try this:**

* Click the Launch button to run the MenuGlue Demo using
  [Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp) ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
  Alternatively, to compile and run the example yourself,
  consult the
  [example index](../examples/components/index.html#MenuGlueDemo).

  [![Launches the ButtonDemo example](../../images/jws-launch-button.png)](http://download.oracle.com/javase/tutorialJWS/uiswing/components/ex6/MenuGlueDemo.jnlp)

---

Here's the modified menu layout that MenuGlueDemo displays:

![MenuGlueDemo](../../figures/uiswing/components/MenuGlueDemo.png)

Another way of changing the look of menus
is to change the layout managers used to control them.
For example, you can change a menu bar's layout manager
from the default left-to-right `BoxLayout`
to something such as `GridLayout`.

---

**Try this:**

* Click the Launch button to run the MenuLayout Demo using
  [Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp) ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
  Alternatively, to compile and run the example yourself,
  consult the
  [example index](../examples/components/index.html#MenuLayoutDemo).

  [![Launches the MenuLayoutDemo example](../../images/jws-launch-button.png)](http://download.oracle.com/javase/tutorialJWS/uiswing/components/ex6/MenuLayoutDemo.jnlp)

---



Here's a picture of the menu layout that `MenuLayoutDemo` creates:

![MenuLayoutDemo](../../figures/uiswing/components/MenuLayoutDemo.png)

### The Menu API

> The following tables list the commonly used
> menu constructors and methods.
> The API for using menus falls into these categories:
>
> * [Creating and Setting Up Menu Bars](#menubarapi)* [Creating and Populating Menus](#menuapi)* [Creating, Populating, and Controlling Popup Menus](#popupapi)* [Implementing Menu Items](#itemapi)
>
> Creating and Setting Up Menu Bars
>
> | Constructor or Method | Purpose |
> | [JMenuBar()](http://download.oracle.com/javase/7/docs/api/javax/swing/JMenuBar.html#JMenuBar()) | Creates a menu bar. |
> | [JMenu add(JMenu)](http://download.oracle.com/javase/7/docs/api/javax/swing/JMenuBar.html#add(javax.swing.JMenu)) | Adds the menu to the end of the menu bar. |
> | [void setJMenuBar(JMenuBar)](http://download.oracle.com/javase/7/docs/api/javax/swing/JFrame.html#setJMenuBar(javax.swing.JMenuBar))   [JMenuBar getJMenuBar()](http://download.oracle.com/javase/7/docs/api/javax/swing/JFrame.html#getJMenuBar())   *(in `JApplet`, `JDialog`, `JFrame`, `JInternalFrame`, `JRootPane`)* | Sets or gets the menu bar of an [applet](applet.html), [dialog](dialog.html), [frame](frame.html), [internal frame](internalframe.html), or [root pane](rootpane.html). |
>
> Creating and Populating Menus
>
> | Constructor or Method | Purpose |
> | [JMenu()](http://download.oracle.com/javase/7/docs/api/javax/swing/JMenu.html#JMenu())   [JMenu(String)](http://download.oracle.com/javase/7/docs/api/javax/swing/JMenu.html#JMenu(java.lang.String))   [JMenu(Action)](http://download.oracle.com/javase/7/docs/api/javax/swing/JMenu.html#JMenu(javax.swing.Action)) | Creates a menu. The string specifies the text to display for the menu. The `Action` specifies the text and other properties of the menu (see [How to Use Actions](../misc/action.html)). |
> | [JMenuItem add(JMenuItem)](http://download.oracle.com/javase/7/docs/api/javax/swing/JMenu.html#add(javax.swing.JMenuItem))   [JMenuItem add(String)](http://download.oracle.com/javase/7/docs/api/javax/swing/JMenu.html#add(java.lang.String)) | Adds a menu item to the current end of the menu. If the argument is a string, then the menu automatically creates a `JMenuItem` object that displays the specified text. **Version Note:**  Before 1.3, the only way to associate an `Action` with a menu item was to use menu's `add(Action)` method to create the menu item and add it to the menu. As of 1.3, that method is no longer recommended. You can instead associate a menu item with an `Action` using the `setAction` method. |
> | [void addSeparator()](http://download.oracle.com/javase/7/docs/api/javax/swing/JMenu.html#addSeparator()) | Adds a separator to the current end of the menu. |
> | [JMenuItem insert(JMenuItem, int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JMenu.html#insert(javax.swing.JMenuItem, int))   [void insert(String, int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JMenu.html#insert(java.lang.String, int))   [void insertSeparator(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JMenu.html#insertSeparator(int)) | Inserts a menu item or separator into the menu at the specified position. The first menu item is at position 0, the second at position 1, and so on. The `JMenuItem` and `String` arguments are treated the same as in the corresponding `add` methods. |
> | [void remove(JMenuItem)](http://download.oracle.com/javase/7/docs/api/javax/swing/JMenu.html#remove(javax.swing.JMenuItem))   [void remove(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JMenu.html#remove(int))   [void removeAll()](http://download.oracle.com/javase/7/docs/api/javax/swing/JMenu.html#removeAll()) | Removes the specified item(s) from the menu. If the argument is an integer, then it specifies the position of the menu item to be removed. |
>
> Creating, Populating, and Controlling Popup Menus
>
> | Constructor or Method | Purpose |
> | [JPopupMenu()](http://download.oracle.com/javase/7/docs/api/javax/swing/JPopupMenu.html#JPopupMenu())   [JPopupMenu(String)](http://download.oracle.com/javase/7/docs/api/javax/swing/JPopupMenu.html#JPopupMenu(java.lang.String)) | Creates a popup menu. The optional string argument specifies the title that a look and feel might display as part of the popup window. |
> | [JMenuItem add(JMenuItem)](http://download.oracle.com/javase/7/docs/api/javax/swing/JPopupMenu.html#add(javax.swing.JMenuItem))   [JMenuItem add(String)](http://download.oracle.com/javase/7/docs/api/javax/swing/JPopupMenu.html#add(java.lang.String)) | Adds a menu item to the current end of the popup menu. If the argument is a string, then the menu automatically creates a `JMenuItem` object that displays the specified text. **Version Note:**  Before 1.3, the only way to associate an `Action` with an item in a popup menu was to use the popup menu's `add(Action)` method to create the menu item and add it to the popup menu. As of 1.3, that method is no longer recommended. You can instead associate a menu item with an `Action` using the `setAction` method. |
> | [void addSeparator()](http://download.oracle.com/javase/7/docs/api/javax/swing/JPopupMenu.html#addSeparator()) | Adds a separator to the current end of the popup menu. |
> | [void insert(Component, int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JPopupMenu.html#insert(java.awt.Component, int)) | Inserts a menu item into the menu at the specified position. The first menu item is at position 0, the second at position 1, and so on. The `Component` argument specifies the menu item to add. |
> | [void remove(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JPopupMenu.html#remove(int))   [void removeAll()](http://download.oracle.com/javase/7/docs/api/java/awt/Container.html#removeAll()) | Removes the specified item(s) from the menu. If the argument is an integer, then it specifies the position of the menu item to be removed. |
> | [static void setLightWeightPopupEnabled(boolean)](http://download.oracle.com/javase/7/docs/api/javax/swing/JPopupMenu.html#setLightWeightPopupEnabled(boolean)) | By default, Swing implements a menu's window using a lightweight component. This can cause problems if you use any heavyweight components in your Swing program, as described in [Bringing Up a Popup Menu](#popup). (This is one of several reasons to avoid using heavyweight components.) As a workaround, invoke `JPopupMenu.setLightWeightPopupEnabled(false)`. |
> | [void show(Component, int, int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JPopupMenu.html#show(java.awt.Component, int, int)) | Display the popup menu at the specified *x,y* position (specified in that order by the integer arguments) in the coordinate system of the specified component. |
>
> Implementing Menu Items
>
> | Constructor or Method | Purpose |
> | [JMenuItem()](http://download.oracle.com/javase/7/docs/api/javax/swing/JMenuItem.html#JMenuItem())   [JMenuItem(String)](http://download.oracle.com/javase/7/docs/api/javax/swing/JMenuItem.html#JMenuItem(java.lang.String))   [JMenuItem(Icon)](http://download.oracle.com/javase/7/docs/api/javax/swing/JMenuItem.html#JMenuItem(javax.swing.Icon))   [JMenuItem(String, Icon)](http://download.oracle.com/javase/7/docs/api/javax/swing/JMenuItem.html#JMenuItem(java.lang.String, javax.swing.Icon))   [JMenuItem(String, int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JMenuItem.html#JMenuItem(java.lang.String, int))   [JMenuItem(Action)](http://download.oracle.com/javase/7/docs/api/javax/swing/JMenuItem.html#JMenuItem(javax.swing.Action)) | Creates an ordinary menu item. The icon argument, if present, specifies the icon that the menu item should display. Similarly, the string argument specifies the text that the menu item should display. The integer argument specifies the keyboard mnemonic to use. You can specify any of the relevant VK constants defined in the [KeyEvent](http://download.oracle.com/javase/7/docs/api/java/awt/event/KeyEvent.html) class. For example, to specify the A key, use `KeyEvent.VK_A`. The constructor with the `Action` parameter, which was introduced in 1.3, sets the menu item's `Action`, causing the menu item's properties to be initialized from the `Action`. See [How to Use Actions](../misc/action.html) for details. |
> | [JCheckBoxMenuItem()](http://download.oracle.com/javase/7/docs/api/javax/swing/JCheckBoxMenuItem.html#JCheckBoxMenuItem())   [JCheckBoxMenuItem(String)](http://download.oracle.com/javase/7/docs/api/javax/swing/JCheckBoxMenuItem.html#JCheckBoxMenuItem(java.lang.String))   [JCheckBoxMenuItem(Icon)](http://download.oracle.com/javase/7/docs/api/javax/swing/JCheckBoxMenuItem.html#JCheckBoxMenuItem(javax.swing.Icon))   [JCheckBoxMenuItem(String, Icon)](http://download.oracle.com/javase/7/docs/api/javax/swing/JCheckBoxMenuItem.html#JCheckBoxMenuItem(java.lang.String, javax.swing.Icon))   [JCheckBoxMenuItem(String, boolean)](http://download.oracle.com/javase/7/docs/api/javax/swing/JCheckBoxMenuItem.html#JCheckBoxMenuItem(java.lang.String, boolean))   [JCheckBoxMenuItem(String, Icon, boolean)](http://download.oracle.com/javase/7/docs/api/javax/swing/JCheckBoxMenuItem.html#JCheckBoxMenuItem(java.lang.String, javax.swing.Icon, boolean)) | Creates a menu item that looks and acts like a check box. The string argument, if any, specifies the text that the menu item should display. If you specify `true` for the boolean argument, then the menu item is initially selected (checked). Otherwise, the menu item is initially unselected. |
> | [JRadioButtonMenuItem()](http://download.oracle.com/javase/7/docs/api/javax/swing/JRadioButtonMenuItem.html#JRadioButtonMenuItem())   [JRadioButtonMenuItem(String)](http://download.oracle.com/javase/7/docs/api/javax/swing/JRadioButtonMenuItem.html#JRadioButtonMenuItem(java.lang.String))   [JRadioButtonMenuItem(Icon)](http://download.oracle.com/javase/7/docs/api/javax/swing/JRadioButtonMenuItem.html#JRadioButtonMenuItem(javax.swing.Icon))   [JRadioButtonMenuItem(String, Icon)](http://download.oracle.com/javase/7/docs/api/javax/swing/JRadioButtonMenuItem.html#JRadioButtonMenuItem(java.lang.String, javax.swing.Icon))   [JRadioButtonMenuItem(String, boolean)](http://download.oracle.com/javase/7/docs/api/javax/swing/JRadioButtonMenuItem.html#JRadioButtonMenuItem(java.lang.String, boolean))   [JRadioButtonMenuItem(Icon, boolean)](http://download.oracle.com/javase/7/docs/api/javax/swing/JRadioButtonMenuItem.html#JRadioButtonMenuItem(javax.swing.Icon, boolean))   [JRadioButtonMenuItem(String, Icon, boolean)](http://download.oracle.com/javase/7/docs/api/javax/swing/JRadioButtonMenuItem.html#JRadioButtonMenuItem(java.lang.String, javax.swing.Icon, boolean)) | Creates a menu item that looks and acts like a radio button. The string argument, if any, specifies the text that the menu item should display. If you specify `true` for the boolean argument, then the menu item is initially selected. Otherwise, the menu item is initially unselected. |
> | [void setState(boolean)](http://download.oracle.com/javase/7/docs/api/javax/swing/JCheckBoxMenuItem.html#setState(boolean))   [boolean getState()](http://download.oracle.com/javase/7/docs/api/javax/swing/JCheckBoxMenuItem.html#getState())   *(in `JCheckBoxMenuItem`)* | Set or get the selection state of a check box menu item. |
> | [void setEnabled(boolean)](http://download.oracle.com/javase/7/docs/api/javax/swing/AbstractButton.html#setEnabled(boolean)) | If the argument is true, enable the menu item. Otherwise, disable the menu item. |
> | [void setMnemonic(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/AbstractButton.html#setMnemonic(int)) | Set the mnemonic that enables keyboard navigation to the menu or menu item. Use one of the VK constants defined in the `KeyEvent` class. |
> | [void setAccelerator(KeyStroke)](http://download.oracle.com/javase/7/docs/api/javax/swing/JMenuItem.html#setAccelerator(javax.swing.KeyStroke)) | Set the accelerator that activates the menu item. |
> | [void setActionCommand(String)](http://download.oracle.com/javase/7/docs/api/javax/swing/AbstractButton.html#setActionCommand(java.lang.String)) | Set the name of the action performed by the menu item. |
> | [void addActionListener(ActionListener)](http://download.oracle.com/javase/7/docs/api/javax/swing/AbstractButton.html#addActionListener(java.awt.event.ActionListener))   [void addItemListener(ItemListener)](http://download.oracle.com/javase/7/docs/api/javax/swing/AbstractButton.html#addItemListener(java.awt.event.ItemListener)) | Add an event listener to the menu item. See [Handling Events from Menu Items](#event) for details. |
> | [void setAction(Action)](http://download.oracle.com/javase/7/docs/api/javax/swing/AbstractButton.html#setAction(javax.swing.Action)) | Set the `Action` associated with the menu item. See [How to Use Actions](../misc/action.html) for details. |
> | Many of the preceding methods are inherited from `AbstractButton`. See [The Button API](button.html#api) for information about other useful methods that `AbstractButton` provides. | |

### Examples that Use Menus

> Menus are used in a few of our examples.
>
> | Example | Where Described | Notes |
> | --- | --- | --- |
> | [`MenuLookDemo`](../examples/components/index.html#MenuLookDemo) | This section ([Creating Menus](#create)) | A simple example that creates all kinds of menus except popup menus, but doesn't handle events from the menu items. |
> | [`MenuDemo`](../examples/components/index.html#MenuDemo) | This section ([Handling Events from Menu Items](#event)) | Adds event handling to `MenuLookDemo`. |
> | [`PopupMenuDemo`](../examples/components/index.html#PopupMenuDemo) | This section ([Bringing Up a Popup Menu](#popup)) | Adds popup menus to `MenuDemo`. |
> | [`MenuGlueDemo`](../examples/components/index.html#MenuGlueDemo) | This section ([Customizing Menu Layout](#custom)) | Demonstrates affecting menu layout by adding an invisible components to the menu bar. |
> | [`MenuLayoutDemo`](../examples/components/index.html#MenuLayoutDemo) | This section ([Customizing Menu Layout](#custom)) | Implements sideways-opening menus arranged in a vertical menu bar. |
> | [`MenuSelectionManagerDemo`](../examples/components/index.html#MenuSelectionManagerDemo) | — | Adds highlight detection to MenuDemo. To see this feature, click a menu and then move the mouse over any menu item or submenu. Once per second, the text area will be updated with information about the currently highlighted menu item, not to be confused with the menu item that the user eventually chooses. This demo uses the default [`MenuSelectionManager`](http://download.oracle.com/javase/7/docs/api/javax/swing/MenuSelectionManager.html), which tracks the state of the menu hierarchy. |
> | [`ActionDemo`](../examples/misc/index.html#ActionDemo) | [How to Use Actions](../misc/action.html) | Uses `Action` objects to implement menu items that duplicate functionality provided by tool bar buttons. |
> | [`Framework`](../examples/components/index.html#Framework) | — | Brings up multiple identical frames, each with a menu in its menu bar. |
> | [`InternalFrameDemo`](../examples/components/index.html#InternalFrameDemo) | [How to Use Internal Frames](internalframe.html) | Uses a menu item to create windows. |

[« Previous](list.html)
•
[Trail](../TOC.html)
•
[Next »](panel.html)

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

**Previous page:** How to Use Lists
  
**Next page:** How to Use Panels




A browser with JavaScript enabled is required for this page to operate properly.