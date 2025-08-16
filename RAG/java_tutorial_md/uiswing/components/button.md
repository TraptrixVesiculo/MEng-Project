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

How to Use Buttons, Check Boxes, and Radio Buttons

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

[How to Use Menus](menu.html)

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

[« Previous](applet.html) • [Trail](../TOC.html) • [Next »](buttongroup.html)

# How to Use Buttons, Check Boxes, and Radio Buttons

To create a button,
you can instantiate one of the many classes that descend from the
[`AbstractButton`](http://download.oracle.com/javase/7/docs/api/javax/swing/AbstractButton.html) class.
The following table shows the Swing-defined
`AbstractButton` subclasses
that you might want to use:

| Class Summary Where Described | | |
| --- | --- | --- |
| [`JButton`](http://download.oracle.com/javase/7/docs/api/javax/swing/JButton.html) | A common button. | [How to Use the Common Button API](#abstractbutton) and [How to Use JButton Features](#jbutton) |
| [`JCheckBox`](http://download.oracle.com/javase/7/docs/api/javax/swing/JCheckBox.html) | A check box button. | [How to Use Check Boxes](#checkbox) |
| [`JRadioButton`](http://download.oracle.com/javase/7/docs/api/javax/swing/JRadioButton.html) | One of a group of radio buttons. | [How to Use Radio Buttons](#radiobutton) |
| [`JMenuItem`](http://download.oracle.com/javase/7/docs/api/javax/swing/JMenuItem.html) | An item in a menu. | [How to Use Menus](menu.html) |
| [`JCheckBoxMenuItem`](http://download.oracle.com/javase/7/docs/api/javax/swing/JCheckBoxMenuItem.html) | A menu item that has a check box. | [How to Use Menus](menu.html) and [How to Use Check Boxes](#checkbox) |
| [`JRadioButtonMenuItem`](http://download.oracle.com/javase/7/docs/api/javax/swing/JRadioButtonMenuItem.html) | A menu item that has a radio button. | [How to Use Menus](menu.html) and [How to Use Radio Buttons](#radiobutton) |
| [`JToggleButton`](http://download.oracle.com/javase/7/docs/api/javax/swing/JToggleButton.html) | Implements toggle functionality inherited by `JCheckBox` and `JRadioButton`. Can be instantiated or subclassed to create two-state buttons. | Used in some [examples](#tbeg) |

---

**Note:** If you want to collect a group of buttons into a row or column,
then you should check out
[tool bars](toolbar.html).

---

First, this section explains the basic button API
that `AbstractButton` defines —
and thus all Swing buttons have in common.
Next, it describes the small amount of API that
`JButton` adds to `AbstractButton`.
After that, this section shows you how to use specialized API
to implement check boxes and radio buttons.

### How to Use the Common Button API

> Here is a picture of an application that displays three buttons:
>
> ![A snapshot of ButtonDemo](../../figures/uiswing/components/ButtonDemoMetal.png)
>
> ---
>
> **Try this:**
>
> 1. Click the Launch button to run the Button Demo using
>    [Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp) ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
>    Alternatively, to compile and run the example yourself,
>    consult the
>    [example index](../examples/components/index.html#ButtonDemo).
>
>    [![Launches the ButtonDemo example](../../images/jws-launch-button.png)](http://download.oracle.com/javase/tutorialJWS/uiswing/components/ex6/ButtonDemo.jnlp)
>
>    - Click the left button.
>        
>      It disables the middle button
>      (and itself, since it is no longer useful)
>      and enables the right button.- Click the right button.
>          
>        It enables the middle button
>        and the left button,
>        and disables itself.
>
> ---
>
> As the `ButtonDemo` example shows,
> a Swing button can display both text and an image.
> In `ButtonDemo`,
> each button has its text in a different place,
> relative to its image.
> The underlined letter in each button's text
> shows the *mnemonic* — the keyboard alternative —
> for each button.
> In most look and feels,
> the user can click a button by pressing the Alt key and the mnemonic.
> For example, Alt-M would click the Middle button in ButtonDemo.
>
> When a button is disabled,
> the look and feel automatically generates
> the button's disabled appearance.
> However, you could provide an image to be substituted for the normal image.
> For example, you could provide
> gray versions of the images used in the left and right buttons.
>
> How you implement event handling
> depends on the type of button you use
> and how you use it.
> Generally, you implement an
> [action listener](../events/actionlistener.html),
> which is notified every time the user clicks the button.
> For [check boxes](#checkbox)
> you usually use an
> [item listener](../events/itemlistener.html),
> which is notified when the check box is selected or deselected.
>
> Below is the code from
> [`ButtonDemo.java`](../examples/components/ButtonDemoProject/src/components/ButtonDemo.java)
> that creates the buttons in the previous example
> and reacts to button clicks.
> The bold code is the code
> that would remain if the buttons had no images.
>
> ```
>
> //In initialization code:
>     ImageIcon leftButtonIcon = createImageIcon("images/right.gif");
>     ImageIcon middleButtonIcon = createImageIcon("images/middle.gif");
>     ImageIcon rightButtonIcon = createImageIcon("images/left.gif");
>
>     b1 = new JButton("Disable middle button", leftButtonIcon);
>     b1.setVerticalTextPosition(AbstractButton.CENTER);
>     b1.setHorizontalTextPosition(AbstractButton.LEADING); //aka LEFT, for left-to-right locales
>     b1.setMnemonic(KeyEvent.VK_D);
>     b1.setActionCommand("disable");
>
>     b2 = new JButton("Middle button", middleButtonIcon);
>     b2.setVerticalTextPosition(AbstractButton.BOTTOM);
>     b2.setHorizontalTextPosition(AbstractButton.CENTER);
>     b2.setMnemonic(KeyEvent.VK_M);
>
>     b3 = new JButton("Enable middle button", rightButtonIcon);
>     //Use the default text position of CENTER, TRAILING (RIGHT).
>     b3.setMnemonic(KeyEvent.VK_E);
>     b3.setActionCommand("enable");
>     b3.setEnabled(false);
>
>     //Listen for actions on buttons 1 and 3.
>     b1.addActionListener(this);
>     b3.addActionListener(this);
>
>     b1.setToolTipText("Click this button to disable "
>                       + "the middle button.");
>     b2.setToolTipText("This middle button does nothing "
>                       + "when you click it.");
>     b3.setToolTipText("Click this button to enable the "
>                       + "middle button.");
>     ...
> }
>
> public void actionPerformed(ActionEvent e) {
>     if ("disable".equals(e.getActionCommand())) {
>         b2.setEnabled(false);
>         b1.setEnabled(false);
>         b3.setEnabled(true);
>     } else {
>         b2.setEnabled(true);
>         b1.setEnabled(true);
>         b3.setEnabled(false);
>     }
> } 
>
> protected static ImageIcon createImageIcon(String path) {
>     java.net.URL imgURL = ButtonDemo.class.getResource(path);
>     ...//error handling omitted for clarity...
>     return new ImageIcon(imgURL);
> }
>
> ```

### How to Use JButton Features

> Ordinary buttons —
> `JButton` objects —
> have just a bit more functionality
> than the `AbstractButton` class provides:
> You can make a `JButton`
> be the default button.
>
> At most one button in a top-level container
> can be the default button.
> The default button typically has a highlighted appearance
> and acts clicked whenever the
> top-level container has the keyboard focus
> and the user presses the Return or Enter key.
> Here is a picture of a dialog, implemented in the
> [ListDialog](../examples/components/index.html#ListDialog) example,
> in which the **Set** button
> is the default button:
>
> ![In the Java Look & Feel, the default button has a heavy border](../../figures/uiswing/components/NameChooserMetal.png)
>
> You set the default button
> by invoking the `setDefaultButton` method
> on a top-level container's root pane.
> Here is the code that sets up the default button
> for the `ListDialog` example:
>
> ```
>
> //In the constructor for a JDialog subclass:
> getRootPane().setDefaultButton(setButton);
>
> ```
>
> The exact implementation of the default button feature
> depends on the look and feel.
> For example, in the Windows look and feel,
> the default button changes to whichever button has the focus,
> so that pressing Enter
> clicks the focused button.
> When no button has the focus,
> the button you originally specified
> as the default button becomes the default button again.

### How to Use Check Boxes
> The
> [`JCheckBox`](http://download.oracle.com/javase/7/docs/api/javax/swing/JCheckBox.html) class provides support for check box buttons.
> You can also put check boxes in [menus](menu.html),
> using the
> [`JCheckBoxMenuItem`](http://download.oracle.com/javase/7/docs/api/javax/swing/JCheckBoxMenuItem.html) class.
> Because
> `JCheckBox`
> and
> `JCheckBoxMenuItem`
> inherit from `AbstractButton`,
> Swing check boxes have all the usual button characteristics,
> as discussed earlier in this section.
> For example, you can specify images
> to be used in check boxes.
>
> Check boxes are similar to [radio buttons](#radiobutton)
> but their selection model is different, by convention.
> Any number of check boxes in a group
> — none, some, or all —
> can be selected.
> A group of radio buttons, on the other hand,
> can have only one button selected.
>
> Here is a picture of an application that uses four check boxes
> to customize a cartoon:
>
> ![NOT a tutorial reader!](../../figures/uiswing/components/CheckBoxDemoMetal.png)
>
> ---
>
> **Try this:** 
>
> 1. Click the Launch button to run the CheckBox Demo using
>    [Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp) ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
>    Alternatively, to compile and run the example yourself,
>    consult the
>    [example index](../examples/components/index.html#CheckBoxDemo).
>
>    [![Launches the ButtonDemo example](../../images/jws-launch-button.png)](http://download.oracle.com/javase/tutorialJWS/uiswing/components/ex6/CheckBoxDemo.jnlp)
>
>    - Click the **Chin** button or press Alt-c.
>        
>      The **Chin** check box becomes unselected,
>      and the chin disappears from the picture.
>      The other check boxes remain selected.
>      This application has one item listener
>      that listens to all the check boxes.
>      Each time the item listener receives an event,
>      the application loads a new picture that reflects
>      the current state of the check boxes.
>
> ---
>
> A check box generates one item event and one action event
> per click.
> Usually, you listen only for item events,
> since they let you determine
> whether the click selected or deselected the check box.
> Below is the code from
> [`CheckBoxDemo.java`](../examples/components/CheckBoxDemoProject/src/components/CheckBoxDemo.java)
> that creates the check boxes in the previous example
> and reacts to clicks.
>
> ```
>
> //In initialization code:
>     chinButton = new JCheckBox("Chin");
>     chinButton.setMnemonic(KeyEvent.VK_C); 
>     chinButton.setSelected(true);
>
>     glassesButton = new JCheckBox("Glasses");
>     glassesButton.setMnemonic(KeyEvent.VK_G); 
>     glassesButton.setSelected(true);
>
>     hairButton = new JCheckBox("Hair");
>     hairButton.setMnemonic(KeyEvent.VK_H); 
>     hairButton.setSelected(true);
>
>     teethButton = new JCheckBox("Teeth");
>     teethButton.setMnemonic(KeyEvent.VK_T); 
>     teethButton.setSelected(true);
>
>     //Register a listener for the check boxes.
>     chinButton.addItemListener(this);
>     glassesButton.addItemListener(this);
>     hairButton.addItemListener(this);
>     teethButton.addItemListener(this);
> ...
> public void itemStateChanged(ItemEvent e) {
>     ...
>     Object source = e.getItemSelectable();
>
>     if (source == chinButton) {
>         //...make a note of it...
>     } else if (source == glassesButton) {
>         //...make a note of it...
>     } else if (source == hairButton) {
>         //...make a note of it...
>     } else if (source == teethButton) {
>         //...make a note of it...
>     }
>
>     if (e.getStateChange() == ItemEvent.DESELECTED)
>         //...make a note of it...
>     ...
>     updatePicture();
> }
>
> ```

### How to Use Radio Buttons
> Radio buttons are groups of buttons
> in which,
> by convention,
> only one button at a time can be selected.
> The Swing release supports radio buttons with the
> [`JRadioButton`](http://download.oracle.com/javase/7/docs/api/javax/swing/JRadioButton.html) and
> [`ButtonGroup`](http://download.oracle.com/javase/7/docs/api/javax/swing/ButtonGroup.html) classes.
> To put a radio button in a
> [menu](menu.html), use the
> [`JRadioButtonMenuItem`](http://download.oracle.com/javase/7/docs/api/javax/swing/JRadioButtonMenuItem.html) class.
> Other ways of displaying one-of-many choices are
> [combo boxes](combobox.html) and
> [lists](list.html).
> Radio buttons look similar to
> [check boxes](#checkbox),
> but, by convention,
> check boxes place no limits on how many items
> can be selected at a time.
>
> Because `JRadioButton` inherits from `AbstractButton`,
> Swing radio buttons have all the usual button characteristics,
> as discussed earlier in this section.
> For example,
> you can specify the image displayed in a radio button.
>
> Here is a picture of an application that uses five radio buttons
> to let you choose which kind of pet is displayed:
>
> ![A snapshot of RadioButtonDemo](../../figures/uiswing/components/RadioButtonDemoMetal.png)
>
> ---
>
> **Try this:**
>
> 1. Click the Launch button to run the RadioButton Demo using
>    [Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp) ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
>    Alternatively, to compile and run the example yourself,
>    consult the
>    [example index](../examples/components/index.html#RadioButtonDemo).
>
>    [![Launches the ButtonDemo example](../../images/jws-launch-button.png)](http://download.oracle.com/javase/tutorialJWS/uiswing/components/ex6/RadioButtonDemo.jnlp)
>
>    - Click the **Dog** button or press Alt-d.
>        
>      The **Dog** button becomes selected,
>      which makes the **Bird** button become unselected.
>      The picture switches from a bird to a dog.
>      This application has one action listener
>      that listens to all the radio buttons.
>      Each time the action listener receives an event,
>      the application displays the picture
>      for the radio button
>      that was just clicked.
>
> ---
>
> Each time the user clicks a radio button
> (even if it was already selected),
> the button fires an
> [action event](../events/actionlistener.html).
> One or two
> [item events](../events/itemlistener.html) also occur —
> one from the button that was just selected,
> and another from the button that lost the selection (if any).
> Usually, you handle radio button clicks using an action listener.
>
> Below is the code from
> [`RadioButtonDemo.java`](../examples/components/RadioButtonDemoProject/src/components/RadioButtonDemo.java)
> that creates the radio buttons in the previous example
> and reacts to clicks.
>
> ```
>
> //In initialization code:
>     //Create the radio buttons.
>     JRadioButton birdButton = new JRadioButton(birdString);
>     birdButton.setMnemonic(KeyEvent.VK_B);
>     birdButton.setActionCommand(birdString);
>     birdButton.setSelected(true);
>
>     JRadioButton catButton = new JRadioButton(catString);
>     catButton.setMnemonic(KeyEvent.VK_C);
>     catButton.setActionCommand(catString);
>
>     JRadioButton dogButton = new JRadioButton(dogString);
>     dogButton.setMnemonic(KeyEvent.VK_D);
>     dogButton.setActionCommand(dogString);
>
>     JRadioButton rabbitButton = new JRadioButton(rabbitString);
>     rabbitButton.setMnemonic(KeyEvent.VK_R);
>     rabbitButton.setActionCommand(rabbitString);
>
>     JRadioButton pigButton = new JRadioButton(pigString);
>     pigButton.setMnemonic(KeyEvent.VK_P);
>     pigButton.setActionCommand(pigString);
>
>     //Group the radio buttons.
>     ButtonGroup group = new ButtonGroup();
>     group.add(birdButton);
>     group.add(catButton);
>     group.add(dogButton);
>     group.add(rabbitButton);
>     group.add(pigButton);
>
>     //Register a listener for the radio buttons.
>     birdButton.addActionListener(this);
>     catButton.addActionListener(this);
>     dogButton.addActionListener(this);
>     rabbitButton.addActionListener(this);
>     pigButton.addActionListener(this);
> ...
> public void actionPerformed(ActionEvent e) {
>     picture.setIcon(new ImageIcon("images/" 
>                                   + e.getActionCommand() 
>                                   + ".gif"));
> }
>
> ```
>
> For each group of radio buttons,
> you need to create a `ButtonGroup` instance
> and add each radio button to it.
> The `ButtonGroup`
> takes care of unselecting the previously selected button
> when the user selects another button in the group.
>
> You should generally initialize a group of radio buttons
> so that one is selected.
> However, the API doesn't enforce this rule —
> a group of radio buttons can have no initial selection.
> Once the user has made a selection,
> exactly one button is selected from then on.

### The Button API

> The following tables list the commonly used
> button-related API.
> Other methods you might call,
> such as `setFont` and `setForeground`,
> are listed in the API tables in
> [The JComponent Class](jcomponent.html#api).
>
> The API for using buttons falls into these categories:
>
> * [Setting or Getting the Button's Contents](#contents)* [Fine Tuning the Button's Appearance](#looks)* [Implementing the Button's Functionality](#acts)* [Check Box Constructors](#checkboxapi)* [Radio Button Constructors](#radiobuttonapi)* [Toggle Button Constructors](#togglebuttonapi)* [Commonly Used Button Group Constructors/Methods](#buttongroup)
>
> Setting or Getting the Button's Contents
>
> | Method or Constructor | Purpose |
> | [JButton(Action)](http://download.oracle.com/javase/7/docs/api/javax/swing/JButton.html#JButton(javax.swing.Action))   [JButton(String, Icon)](http://download.oracle.com/javase/7/docs/api/javax/swing/JButton.html#JButton(java.lang.String, javax.swing.Icon))   [JButton(String)](http://download.oracle.com/javase/7/docs/api/javax/swing/JButton.html#JButton(java.lang.String))   [JButton(Icon)](http://download.oracle.com/javase/7/docs/api/javax/swing/JButton.html#JButton(javax.swing.Icon))   [JButton()](http://download.oracle.com/javase/7/docs/api/javax/swing/JButton.html#JButton()) | Create a `JButton` instance, initializing it to have the specified text/image/action. |
> | [void setAction(Action)](http://download.oracle.com/javase/7/docs/api/javax/swing/AbstractButton.html#setAction(javax.swing.Action))   [Action getAction()](http://download.oracle.com/javase/7/docs/api/javax/swing/AbstractButton.html#getAction()) | Set or get the button's properties according to values from the `Action` instance. |
> | [void setText(String)](http://download.oracle.com/javase/7/docs/api/javax/swing/AbstractButton.html#setText(java.lang.String))   [String getText()](http://download.oracle.com/javase/7/docs/api/javax/swing/AbstractButton.html#getText()) | Set or get the text displayed by the button. You can use HTML formatting, as described in [Using HTML in Swing Components](html.html). |
> | [void setIcon(Icon)](http://download.oracle.com/javase/7/docs/api/javax/swing/AbstractButton.html#setIcon(javax.swing.Icon))   [Icon getIcon()](http://download.oracle.com/javase/7/docs/api/javax/swing/AbstractButton.html#getIcon()) | Set or get the image displayed by the button when the button isn't selected or pressed. |
> | [void setDisabledIcon(Icon)](http://download.oracle.com/javase/7/docs/api/javax/swing/AbstractButton.html#setDisabledIcon(javax.swing.Icon))   [Icon getDisabledIcon()](http://download.oracle.com/javase/7/docs/api/javax/swing/AbstractButton.html#getDisabledIcon()) | Set or get the image displayed by the button when it is disabled. If you do not specify a disabled image, then the look and feel creates one by manipulating the default image. |
> | [void setPressedIcon(Icon)](http://download.oracle.com/javase/7/docs/api/javax/swing/AbstractButton.html#setPressedIcon(javax.swing.Icon))   [Icon getPressedIcon()](http://download.oracle.com/javase/7/docs/api/javax/swing/AbstractButton.html#getPressedIcon()) | Set or get the image displayed by the button when it is being pressed. |
> | [void setSelectedIcon(Icon)](http://download.oracle.com/javase/7/docs/api/javax/swing/AbstractButton.html#setSelectedIcon(javax.swing.Icon))   [Icon getSelectedIcon()](http://download.oracle.com/javase/7/docs/api/javax/swing/AbstractButton.html#getSelectedIcon())   [void setDisabledSelectedIcon(Icon)](http://download.oracle.com/javase/7/docs/api/javax/swing/AbstractButton.html#setDisabledSelectedIcon(javax.swing.Icon))   [Icon getDisabledSelectedIcon()](http://download.oracle.com/javase/7/docs/api/javax/swing/AbstractButton.html#getDisabledSelectedIcon()) | Set or get the image displayed by the button when it is selected. If you do not specify a disabled selected image, then the look and feel creates one by manipulating the selected image. |
> | [setRolloverEnabled(boolean)](http://download.oracle.com/javase/7/docs/api/javax/swing/AbstractButton.html#setRolloverEnabled(boolean))   [boolean isRolloverEnabled()](http://download.oracle.com/javase/7/docs/api/javax/swing/AbstractButton.html#isRolloverEnabled())   [void setRolloverIcon(Icon)](http://download.oracle.com/javase/7/docs/api/javax/swing/AbstractButton.html#setRolloverIcon(javax.swing.Icon))   [Icon getRolloverIcon()](http://download.oracle.com/javase/7/docs/api/javax/swing/AbstractButton.html#getRolloverIcon())   [void setRolloverSelectedIcon(Icon)](http://download.oracle.com/javase/7/docs/api/javax/swing/AbstractButton.html#setRolloverSelectedIcon(javax.swing.Icon))   [Icon getRolloverSelectedIcon()](http://download.oracle.com/javase/7/docs/api/javax/swing/AbstractButton.html#getRolloverSelectedIcon()) | Use `setRolloverIcon(someIcon)` to make the button display the specified icon when the cursor passes over it. The `setRolloverSelectedIcon` method lets you specify the rollover icon when the button is selected — this is useful for two-state buttons such as toggle buttons. Setting the rollover icon automatically calls `setRollover(true)`, enabling rollover. |
>
> Fine Tuning the Button's Appearance
>
> | Method or Constructor | Purpose |
> | [void setHorizontalAlignment(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/AbstractButton.html#setHorizontalAlignment(int))   [void setVerticalAlignment(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/AbstractButton.html#setVerticalAlignment(int))   [int getHorizontalAlignment()](http://download.oracle.com/javase/7/docs/api/javax/swing/AbstractButton.html#getHorizontalAlignment())   [int getVerticalAlignment()](http://download.oracle.com/javase/7/docs/api/javax/swing/AbstractButton.html#getVerticalAlignment()) | Set or get where in the button its contents should be placed. The `AbstractButton` class allows any one of the following values for horizontal alignment: `RIGHT`, `LEFT`, `CENTER` (the default), `LEADING`, and `TRAILING`. For vertical alignment: `TOP`, `CENTER` (the default), and `BOTTOM`. |
> | [void setHorizontalTextPosition(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/AbstractButton.html#setHorizontalTextPosition(int))   [void setVerticalTextPosition(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/AbstractButton.html#setVerticalTextPosition(int))   [int getHorizontalTextPosition()](http://download.oracle.com/javase/7/docs/api/javax/swing/AbstractButton.html#getHorizontalTextPosition())   [int getVerticalTextPosition()](http://download.oracle.com/javase/7/docs/api/javax/swing/AbstractButton.html#getVerticalTextPosition()) | Set or get where the button's text should be placed, relative to the button's image. The `AbstractButton` class allows any one of the following values for horizontal position: `LEFT`, `CENTER`, `RIGHT`, `LEADING`, and `TRAILING` (the default). For vertical position: `TOP`, `CENTER` (the default), and `BOTTOM`. |
> | [void setMargin(Insets)](http://download.oracle.com/javase/7/docs/api/javax/swing/AbstractButton.html#setMargin(java.awt.Insets))   [Insets getMargin()](http://download.oracle.com/javase/7/docs/api/javax/swing/AbstractButton.html#getMargin()) | Set or get the number of pixels between the button's border and its contents. |
> | [void setFocusPainted(boolean)](http://download.oracle.com/javase/7/docs/api/javax/swing/AbstractButton.html#setFocusPainted(boolean))   [boolean isFocusPainted()](http://download.oracle.com/javase/7/docs/api/javax/swing/AbstractButton.html#isFocusPainted()) | Set or get whether the button should look different when it has the focus. |
> | [void setBorderPainted(boolean)](http://download.oracle.com/javase/7/docs/api/javax/swing/AbstractButton.html#setBorderPainted(boolean))   [boolean isBorderPainted()](http://download.oracle.com/javase/7/docs/api/javax/swing/AbstractButton.html#isBorderPainted()) | Set or get whether the border of the button should be painted. |
> | [void setIconTextGap(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/AbstractButton.html#setIconTextGap(int))   [int getIconTextGap()](http://download.oracle.com/javase/7/docs/api/javax/swing/AbstractButton.html#getIconTextGap()) | Set or get the amount of space between the text and the icon displayed in this button. |
>
> Implementing the Button's Functionality
>
> | Method or Constructor | Purpose |
> | [void setMnemonic(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/AbstractButton.html#setMnemonic(int))   [char getMnemonic()](http://download.oracle.com/javase/7/docs/api/javax/swing/AbstractButton.html#getMnemonic()) | Set or get the keyboard alternative to clicking the button. One form of the `setMnemonic` method accepts a character argument; however, the Swing team recommends that you use an `int` argument instead, specifying a `KeyEvent.VK_X` constant. |
> | [void setDisplayedMnemonicIndex(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/AbstractButton.html#setDisplayedMnemonicIndex(int))   [int getDisplayedMnemonicIndex()](http://download.oracle.com/javase/7/docs/api/javax/swing/AbstractButton.html#getDisplayedMnemonicIndex()) | Set or get a hint as to which character in the text should be decorated to represent the mnemonic. Note that not all look and feels may support this. |
> | [void setActionCommand(String)](http://download.oracle.com/javase/7/docs/api/javax/swing/AbstractButton.html#setActionCommand(java.lang.String))   [String getActionCommand()](http://download.oracle.com/javase/7/docs/api/javax/swing/AbstractButton.html#getActionCommand()) | Set or get the name of the action performed by the button. |
> | [void addActionListener(ActionListener)](http://download.oracle.com/javase/7/docs/api/javax/swing/AbstractButton.html#addActionListener(java.awt.event.ActionListener))   [ActionListener removeActionListener()](http://download.oracle.com/javase/7/docs/api/javax/swing/AbstractButton.html#removeActionListener()) | Add or remove an object that listens for action events fired by the button. |
> | [void addItemListener(ItemListener)](http://download.oracle.com/javase/7/docs/api/javax/swing/AbstractButton.html#addItemListener(java.awt.event.ItemListener))   [ItemListener removeItemListener()](http://download.oracle.com/javase/7/docs/api/javax/swing/AbstractButton.html#removeItemListener()) | Add or remove an object that listens for item events fired by the button. |
> | [void setSelected(boolean)](http://download.oracle.com/javase/7/docs/api/javax/swing/AbstractButton.html#setSelected(boolean))   [boolean isSelected()](http://download.oracle.com/javase/7/docs/api/javax/swing/AbstractButton.html#isSelected()) | Set or get whether the button is selected. Makes sense only for buttons that have on/off state, such as check boxes. |
> | [void doClick()](http://download.oracle.com/javase/7/docs/api/javax/swing/AbstractButton.html#doClick())   [void doClick(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/AbstractButton.html#doClick(int)) | Programmatically perform a "click". The optional argument specifies the amount of time (in milliseconds) that the button should look pressed. |
> | [void setMultiClickThreshhold(long)](http://download.oracle.com/javase/7/docs/api/javax/swing/AbstractButton.html#setMultiClickThreshhold(long))   [long getMultiClickThreshhold()](http://download.oracle.com/javase/7/docs/api/javax/swing/AbstractButton.html#getMultiClickThreshhold()) | Set or get the amount of time (in milliseconds) required between mouse press events for the button to generate corresponding action events. |
>
> Check Box Constructors
>
> | Constructor | Purpose |
> | [JCheckBox(Action)](http://download.oracle.com/javase/7/docs/api/javax/swing/JCheckBox.html#JCheckBox(javax.swing.Action))   [JCheckBox(String)](http://download.oracle.com/javase/7/docs/api/javax/swing/JCheckBox.html#JCheckBox(java.lang.String))   [JCheckBox(String, boolean)](http://download.oracle.com/javase/7/docs/api/javax/swing/JCheckBox.html#JCheckBox(java.lang.String, boolean))   [JCheckBox(Icon)](http://download.oracle.com/javase/7/docs/api/javax/swing/JCheckBox.html#JCheckBox(javax.swing.Icon))   [JCheckBox(Icon, boolean)](http://download.oracle.com/javase/7/docs/api/javax/swing/JCheckBox.html#JCheckBox(javax.swing.Icon, boolean))   [JCheckBox(String, Icon)](http://download.oracle.com/javase/7/docs/api/javax/swing/JCheckBox.html#JCheckBox(java.lang.String, javax.swing.Icon))   [JCheckBox(String, Icon, boolean)](http://download.oracle.com/javase/7/docs/api/javax/swing/JCheckBox.html#JCheckBox(java.lang.String, javax.swing.Icon, boolean))   [JCheckBox()](http://download.oracle.com/javase/7/docs/api/javax/swing/JCheckBox.html#JCheckBox()) | Create a `JCheckBox` instance. The string argument specifies the text, if any, that the check box should display. Similarly, the `Icon` argument specifies the image that should be used instead of the look and feel's default check box image. Specifying the boolean argument as `true` initializes the check box to be selected. If the boolean argument is absent or `false`, then the check box is initially unselected. |
> | [JCheckBoxMenuItem(Action)](http://download.oracle.com/javase/7/docs/api/javax/swing/JCheckBoxMenuItem.html#JCheckBoxMenuItem(javax.swing.Action))   [JCheckBoxMenuItem(String)](http://download.oracle.com/javase/7/docs/api/javax/swing/JCheckBoxMenuItem.html#JCheckBoxMenuItem(java.lang.String))   [JCheckBoxMenuItem(String, boolean)](http://download.oracle.com/javase/7/docs/api/javax/swing/JCheckBoxMenuItem.html#JCheckBoxMenuItem(java.lang.String, boolean))   [JCheckBoxMenuItem(Icon)](http://download.oracle.com/javase/7/docs/api/javax/swing/JCheckBoxMenuItem.html#JCheckBoxMenuItem(javax.swing.Icon))   [JCheckBoxMenuItem(String, Icon)](http://download.oracle.com/javase/7/docs/api/javax/swing/JCheckBoxMenuItem.html#JCheckBoxMenuItem(java.lang.String, javax.swing.Icon))   [JCheckBoxMenuItem(String, Icon, boolean)](http://download.oracle.com/javase/7/docs/api/javax/swing/JCheckBoxMenuItem.html#JCheckBoxMenuItem(java.lang.String, javax.swing.Icon, boolean))   [JCheckBoxMenuItem()](http://download.oracle.com/javase/7/docs/api/javax/swing/JCheckBoxMenuItem.html#JCheckBoxMenuItem()) | Create a `JCheckBoxMenuItem` instance. The arguments are interpreted in the same way as the arguments to the `JCheckBox` constructors, except that any specified icon is shown in addition to the normal check box icon. |
>
> Radio Button Constructors
>
> | Constructor | Purpose |
> | [JRadioButton(Action)](http://download.oracle.com/javase/7/docs/api/javax/swing/JRadioButton.html#JRadioButton(javax.swing.Action))   [JRadioButton(String)](http://download.oracle.com/javase/7/docs/api/javax/swing/JRadioButton.html#JRadioButton(java.lang.String))   [JRadioButton(String, boolean)](http://download.oracle.com/javase/7/docs/api/javax/swing/JRadioButton.html#JRadioButton(java.lang.String, boolean))   [JRadioButton(Icon)](http://download.oracle.com/javase/7/docs/api/javax/swing/JRadioButton.html#JRadioButton(javax.swing.Icon))   [JRadioButton(Icon, boolean)](http://download.oracle.com/javase/7/docs/api/javax/swing/JRadioButton.html#JRadioButton(javax.swing.Icon, boolean))   [JRadioButton(String, Icon)](http://download.oracle.com/javase/7/docs/api/javax/swing/JRadioButton.html#JRadioButton(java.lang.String, javax.swing.Icon))   [JRadioButton(String, Icon, boolean)](http://download.oracle.com/javase/7/docs/api/javax/swing/JRadioButton.html#JRadioButton(java.lang.String, javax.swing.Icon, boolean))   [JRadioButton()](http://download.oracle.com/javase/7/docs/api/javax/swing/JRadioButton.html#JRadioButton()) | Create a `JRadioButton` instance. The string argument specifies the text, if any, that the radio button should display. Similarly, the `Icon` argument specifies the image that should be used instead of the look and feel's default radio button image. Specifying the boolean argument as `true` initializes the radio button to be selected, subject to the approval of the `ButtonGroup` object. If the boolean argument is absent or `false`, then the radio button is initially unselected. |
> | [JRadioButtonMenuItem(Action)](http://download.oracle.com/javase/7/docs/api/javax/swing/JRadioButtonMenuItem.html#JRadioButtonMenuItem(javax.swing.Action))   [JRadioButtonMenuItem(String)](http://download.oracle.com/javase/7/docs/api/javax/swing/JRadioButtonMenuItem.html#JRadioButtonMenuItem(java.lang.String))   [JRadioButtonMenuItem(Icon)](http://download.oracle.com/javase/7/docs/api/javax/swing/JRadioButtonMenuItem.html#JRadioButtonMenuItem(javax.swing.Icon))   [JRadioButtonMenuItem(String, Icon)](http://download.oracle.com/javase/7/docs/api/javax/swing/JRadioButtonMenuItem.html#JRadioButtonMenuItem(java.lang.String, javax.swing.Icon))   [JRadioButtonMenuItem()](http://download.oracle.com/javase/7/docs/api/javax/swing/JRadioButtonMenuItem.html#JRadioButtonMenuItem()) | Create a `JRadioButtonMenuItem` instance. The arguments are interpreted in the same way as the arguments to the `JRadioButton` constructors, except that any specified icon is shown in addition to the normal radio button icon. |
>
> Toggle Button Constructors
>
> | Constructor | Purpose |
> | [JToggleButton(Action)](http://download.oracle.com/javase/7/docs/api/javax/swing/JToggleButton.html#JToggleButton(javax.swing.Action))   [JToggleButton(String)](http://download.oracle.com/javase/7/docs/api/javax/swing/JToggleButton.html#JToggleButton(java.lang.String))   [JToggleButton(String, boolean)](http://download.oracle.com/javase/7/docs/api/javax/swing/JToggleButton.html#JToggleButton(java.lang.String, boolean))   [JToggleButton(Icon)](http://download.oracle.com/javase/7/docs/api/javax/swing/JToggleButton.html#JToggleButton(javax.swing.Icon))   [JToggleButton(Icon, boolean)](http://download.oracle.com/javase/7/docs/api/javax/swing/JToggleButton.html#JToggleButton(javax.swing.Icon, boolean))   [JToggleButton(String, Icon)](http://download.oracle.com/javase/7/docs/api/javax/swing/JToggleButton.html#JToggleButton(java.lang.String, javax.swing.Icon))   [JToggleButton(String, Icon, boolean)](http://download.oracle.com/javase/7/docs/api/javax/swing/JToggleButton.html#JToggleButton(java.lang.String, javax.swing.Icon, boolean))   [JToggleButton()](http://download.oracle.com/javase/7/docs/api/javax/swing/JToggleButton.html#JToggleButton()) | Create a `JToggleButton` instance, which is similar to a `JButton`, but with two states. Normally, you use a `JRadioButton` or `JCheckBox` instead of directly instantiating `JToggleButton`, but `JToggleButton` can be useful when you do not want the typical radio button or check box appearance. The string argument specifies the text, if any, that the toggle button should display. Similarly, the `Icon` argument specifies the image that should be used. Specifying the boolean argument as `true` initializes the toggle button to be selected. If the boolean argument is absent or `false`, then the toggle button is initially unselected. |
>
> Commonly Used Button Group Constructors/Methods
>
> | Constructor or Method | Purpose |
> | [ButtonGroup()](http://download.oracle.com/javase/7/docs/api/javax/swing/ButtonGroup.html#ButtonGroup()) | Create a `ButtonGroup` instance. |
> | [void add(AbstractButton)](http://download.oracle.com/javase/7/docs/api/javax/swing/ButtonGroup.html#add(javax.swing.AbstractButton))   [void remove(AbstractButton)](http://download.oracle.com/javase/7/docs/api/javax/swing/ButtonGroup.html#remove(javax.swing.AbstractButton)) | Add a button to the group, or remove a button from the group. |
> | [public ButtonGroup getGroup()](http://download.oracle.com/javase/7/docs/api/javax/swing/DefaultButtonModel.html#getGroup())   *(in `DefaultButtonModel`)* | Get the `ButtonGroup`, if any, that controls a button. For example:   `ButtonGroup group = ((DefaultButtonModel)button.getModel()).getGroup();` |
> | [public ButtonGroup clearSelection()](http://download.oracle.com/javase/7/docs/api/javax/swing/ButtonGroup.html#ButtonGroup()) | Clears the state of selected buttons in the ButtonGroup. None of the buttons in the ButtonGroup are selected . |

### Examples that Use Various Kinds of Buttons

> The following examples use buttons.
> Also see [Examples that Use Tool Bars](toolbar.html#eg),
> which lists programs that add `JButton` objects
> to `JToolBar`s.
>
> | Example | Where Described | Notes |
> | --- | --- | --- |
> | [`ButtonDemo`](../examples/components/index.html#ButtonDemo) | [How to Use the Common Button API](#abstractbutton) | Uses mnemonics and icons. Specifies the button text position, relative to the button icon. Uses action commands. |
> | [`ButtonHtmlDemo`](../examples/components/index.html#ButtonHtmlDemo) | [Using HTML in Swing Components](html.html) | A version of ButtonDemo that uses HTML formatting in its buttons. |
> | [`ListDialog`](../examples/components/index.html#ListDialog) | [How to Use JButton Features](#jbutton) | Implements a dialog with two buttons, one of which is the default button. |
> | [`DialogDemo`](../examples/components/index.html#DialogDemo) | [How to Make Dialogs](dialog.html) | Has "Show it" buttons whose behavior is tied to the state of radio buttons. Uses sizable, though anonymous, inner classes to implement the action listeners. |
> | [`ProgressBarDemo`](../examples/components/index.html#ProgressBarDemo) | [How to Monitor Progress](progress.html) | Implements a button's action listener with a named inner class. |
> | [`CheckBoxDemo`](../examples/components/index.html#CheckBoxDemo) | [How to Use Check Boxes](#checkbox) | Uses check box buttons to determine which of 16 images it should display. |
> | [`ActionDemo`](../examples/misc/index.html#ActionDemo) | [How to Use Actions](../misc/action.html) | Uses check box menu items to set the state of the program. |
> | [`RadioButtonDemo`](../examples/components/index.html#RadioButtonDemo) | [How to Use Radio Buttons](#radiobutton) | Uses radio buttons to determine which of five images it should display. |
> | [`DialogDemo`](../examples/components/index.html#DialogDemo) | [How to Make Dialogs](dialog.html) | Contains several sets of radio buttons, which it uses to determine which dialog to bring up. |
> | [`MenuDemo`](../examples/components/index.html#MenuDemo) | [How to Use Menus](menu.html) | Contains radio button menu items and check box menu items. |
> | [`ColorChooserDemo2`](../examples/components/index.html#ColorChooserDemo2) | [How to Use Color Choosers](colorchooser.html) The crayons in `CrayonPanel` are implemented as toggle buttons. | |
> | [`ScrollDemo`](../examples/components/index.html#ScrollDemo) | [How to Use Scroll Panes](scrollpane.html) The **cm** button is a toggle button. | |

[« Previous](applet.html)
•
[Trail](../TOC.html)
•
[Next »](buttongroup.html)

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

**Previous page:** How to Make Applets
  
**Next page:** How to Use the ButtonGroup Component




A browser with JavaScript enabled is required for this page to operate properly.