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

How to Use Tabbed Panes

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

[« Previous](splitpane.html) • [Trail](../TOC.html) • [Next »](table.html)

# How to Use Tabbed Panes

With the
[`JTabbedPane`](http://download.oracle.com/javase/7/docs/api/javax/swing/JTabbedPane.html) class,
you can have several components,
such as [panels](panel.html),
share the same space.
The user chooses which component to view
by selecting the tab corresponding to the desired component.
If you want similar functionality
without the tab interface,
you can use a
[card layout](../layout/card.html) instead of a tabbed pane.

#### To Create Tabbed Panes

To create a tabbed pane,
instantiate `JTabbedPane`,
create the components you wish it to display,
and then add the components
to the tabbed pane
using the
`addTab`
method.

The following picture introduces an application called `TabbedPaneDemo`
that has a tabbed pane
with four tabs.

![A screenshot of TabbedPaneDemo](../../figures/uiswing/components/TabbedPaneDemo.png)

---

**Try this:**

1. Click the Launch button
   to run TabbedPaneDemo
   using
   [Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp)
   ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
   Alternatively, to compile and run the example yourself,
   consult the
   [example index](../examples/components/index.html#TabbedPaneDemo).

   [![Launches the TabbedPaneDemo Application](../../images/jws-launch-button.png)](http://download.oracle.com/javase/tutorialJWS/uiswing/components/ex6/TabbedPaneDemo.jnlp)

   - Put the cursor over a tab.
       
     The tool tip associated with the tab appears.
     As a convenience,
     you can specify tool tip text
     when you add a component to the tabbed pane.- Select a tab by clicking it.
         
       The tabbed pane displays the component corresponding to the tab.- Select a tab by entering its mnemonic.
           
         For example, in the Java look and feel you can
         select the tab labeled "Tab 3" by typing
         Alt-3.- Navigate between scrollable tabs.
             
           This example provides scrollable tabs. Resize the dialog box
           by moving its left or right boundary so that tabs do not fit
           within the dialog. Scroll arrows appear next to the tabs.
             
           Click the arrow to view one of the hidden tabs.
             
           Note that clicking the arrow only reveals hidden tabs.
           It does not select a new tab.

---

As the `TabbedPaneDemo` example shows,
a tab can have a tool tip and a mnemonic,
and it can display both text and an image.

#### Tab Placement

The default tab placement is set to the `TOP` location,
as shown above.
You can change the tab placement to `LEFT`, `RIGHT`,
`TOP` or `BOTTOM`
by using the `setTabPlacement` method.

#### Code for Tabbed Panes

The following code from
[`TabbedPaneDemo.java`](../examples/components/TabbedPaneDemoProject/src/components/TabbedPaneDemo.java)
creates the tabbed pane in the previous example.
Note that no event-handling code is necessary.
The `JTabbedPane` object
takes care of mouse and keyboard events for you.

```

JTabbedPane tabbedPane = new JTabbedPane();
ImageIcon icon = createImageIcon("images/middle.gif");

JComponent panel1 = makeTextPanel("Panel #1");
tabbedPane.addTab("Tab 1", icon, panel1,
                  "Does nothing");
tabbedPane.setMnemonicAt(0, KeyEvent.VK_1);

JComponent panel2 = makeTextPanel("Panel #2");
tabbedPane.addTab("Tab 2", icon, panel2,
                  "Does twice as much nothing");
tabbedPane.setMnemonicAt(1, KeyEvent.VK_2);

JComponent panel3 = makeTextPanel("Panel #3");
tabbedPane.addTab("Tab 3", icon, panel3,
                  "Still does nothing");
tabbedPane.setMnemonicAt(2, KeyEvent.VK_3);

JComponent panel4 = makeTextPanel(
        "Panel #4 (has a preferred size of 410 x 50).");
panel4.setPreferredSize(new Dimension(410, 50));
tabbedPane.addTab("Tab 4", icon, panel4,
                      "Does nothing at all");
tabbedPane.setMnemonicAt(3, KeyEvent.VK_4);

```

As the previous code shows,
the `addTab` method
handles the bulk of the work in setting up a tab
in a tabbed pane.
The `addTab` method has several forms,
but they all use both a string title
and the component to be displayed by the tab.
Optionally, you can specify an icon and
[tool tip](tooltip.html) string.
The text or icon (or both) can be null.
Another way to create a tab is to use the
`insertTab` method,
which lets you specify the index of the tab you're adding.
Note that the `addTab` method does not allow
index specification in this step.

#### To Switch to Specific Tabs

There are three ways to switch to specific tabs using GUI.

1. **Using a mouse.**
   To switch to a specific tab,
   the user clicks it with the mouse.
2. **Using keyboard arrows.**
   When the `JTabbedPane` object has the focus,
   the keyboard arrows can be used to switch from tab to tab.
3. **Using key mnemonics.**
   The `setMnemonicAt` method
   allows the user
   to switch to a specific tab
   using the keyboard.
   For example,
   `setMnemonicAt(3, KeyEvent.VK_4)`
   makes '4' the mnemonic
   for the fourth tab
   (which is at index 3,
   since the indices start with 0);
   pressing Alt-4 makes the fourth tab's component appear.
   Often, a mnemonic
   uses a character in the tab's title
   that is then
   automatically underlined.

To switch to a specific tab programmatically,
use the
[`setSelectedIndex`](http://download.oracle.com/javase/7/docs/api/javax/swing/JTabbedPane.html#setSelectedIndex(int))
or the
[`setSelectedComponent`](http://download.oracle.com/javase/7/docs/api/javax/swing/JTabbedPane.html#setSelectedComponent(java.awt.Component))
methods.

#### Preferred Size in Tabs

When building components to
add to a tabbed pane,
keep in mind that no matter which
child of a tabbed pane is visible,
each child gets the same amount of space
in which to display itself.
The preferred size of the tabbed pane
is just big enough to display
its tallest child at its preferred height,
and its widest child at its preferred width.
Similarly,
the minimum size of the tabbed pane depends on
the biggest minimum width and height
of all its children.

In the `TabbedPaneDemo` example,
the fourth panel has a preferred width and height
that are larger than those of the other panels.
Thus, the preferred size of the tabbed pane
is just big enough to display the fourth panel
at its preferred size.
Every panel gets exactly the same amount of space —
410 pixels wide and 50 high,
assuming the tabbed pane is at its preferred size.
If you do not understand how preferred size is used,
please refer to
[How Layout Management Works](../layout/howLayoutWorks.html).

### Tabs With Custom Components

> The `TabComponentsDemo` example introduces a tabbed pane
> whose tabs contain real components.
> The use of custom components brings new features
> such as buttons, combo boxes, labels and other components
> to tabs, and allows more complex user interaction.
>
> Here is a tabbed pane
> with close buttons on its tabs.
>
> ![A screenshot of TabComponentsDemo](../../figures/uiswing/components/TabComponentsDemo.png)
>
> ---
>
> **Try this:**
>
> 1. Click the Launch button
>    to run TabComponentsDemo
>    using
>    [Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp)
>    ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
>    Alternatively, to compile and run the example yourself,
>    consult the
>    [example index](../examples/components/index.html#TabComponentsDemo).
>
>    [![Launches the TabComponentsDemo Application](../../images/jws-launch-button.png)](http://download.oracle.com/javase/tutorialJWS/uiswing/components/ex6/TabComponentsDemo.jnlp)
>
>    - Put the cursor over a tab.- Select a tab by clicking it (make sure not to hit the little cross).- Put the cursor over one of the widgets with a little cross.
>            
>          The cross turns magenta and gets enclosed in a square.
>          A tool tip associated with the close button appears.
>            
>          Click the cross with the left mouse button to close the tab.- Restore the tabs that have been removed by choosing
>            the Reset JTabbedPane item from the Options menu.- Note that tabs with custom components are displayed
>              on top of original tabbed pane tabs.
>                
>              To view the tabs underneath, open the Options menu
>              and clear the Use TabComponents checkbox.- Display the tabs with components by selecting
>                the Use TabComponents checkbox again.- Close all tabs.
>                  Now the tabbed pane is empty.
>
> ---
>
> #### To Remove Tabs
>
> The following code from
> [`ButtonTabComponent.java`](../examples/components/TabComponentsDemoProject/src/components/ButtonTabComponent.java)
> removes a tab from the tabbed pane.
> Note that event-handling code is necessary.
> Since each tab contains a real `JButton` object, you must
> attach an `ActionListener` to the close button.
> As the user clicks the button,
> the `actionPerformed` method
> determines the index of the tab it belongs to
> and removes the corresponding tab.
>
> ```
>
> public void actionPerformed(ActionEvent e) {
>     int i = pane.indexOfTabComponent(ButtonTabComponent.this);
>     if (i != -1) {
>     pane.remove(i);
>     }
> }
>
> ```
>
> #### To Give Titles to Customized Tabs
>
> The code below, taken from
> [`ButtonTabComponent.java`](../examples/components/TabComponentsDemoProject/src/components/ButtonTabComponent.java), shows how a customized tab component gets
> a title from an original tabbed pane tab.
>
> ```
>
> JLabel label = new JLabel(title) {
>     public String getText() {
>         int i = pane.indexOfTabComponent(ButtonTabComponent.this);
> 	if (i != -1) {
> 	    return pane.getTitleAt(i);
> 	}
> 	return null;
>     }
> };
>
> ```

### The Tabbed Pane API

> The following tables list the commonly used
> `JTabbedPane` constructors and methods.
> The API for using tabbed panes falls into the following categories:
>
> * [Creating and Setting Up a Tabbed Pane](#creating)* [Inserting, Removing, Finding, and Selecting Tabs](#tabapi)* [Changing Tab Appearance](#appearanceapi)* [Setting Up Custom Components on Tabs](#tabscomponents)
>
> **Creating and Setting Up a Tabbed Pane**
>
> | Method or Constructor | Purpose |
> | [JTabbedPane()](http://download.oracle.com/javase/7/docs/api/javax/swing/JTabbedPane.html#JTabbedPane())   [JTabbedPane(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JTabbedPane.html#JTabbedPane(int))   [JTabbedPane(int, int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JTabbedPane.html#JTabbedPane(int, int)) | Creates a tabbed pane. The first optional argument specifies where the tabs should appear. By default, the tabs appear at the top of the tabbed pane. You can specify these positions (defined in the `SwingConstants` interface, which `JTabbedPane` implements): `TOP`, `BOTTOM`, `LEFT`, `RIGHT`. The second optional argument specifies the tab layout policy. You can specify one of these policies (defined in `JTabbedPane`): [`WRAP_TAB_LAYOUT`](http://download.oracle.com/javase/7/docs/api/javax/swing/JTabbedPane.html#WRAP_TAB_LAYOUT) or [`SCROLL_TAB_LAYOUT`](http://download.oracle.com/javase/7/docs/api/javax/swing/JTabbedPane.html#SCROLL_TAB_LAYOUT). |
> | [addTab(String, Icon, Component, String)](http://download.oracle.com/javase/7/docs/api/javax/swing/JTabbedPane.html#addTab(java.lang.String, javax.swing.Icon, java.awt.Component, java.lang.String))   [addTab(String, Icon, Component)](http://download.oracle.com/javase/7/docs/api/javax/swing/JTabbedPane.html#addTab(java.lang.String, javax.swing.Icon, java.awt.Component))   [addTab(String, Component)](http://download.oracle.com/javase/7/docs/api/javax/swing/JTabbedPane.html#addTab(java.lang.String, java.awt.Component)) | Adds a new tab to the tabbed pane. The first argument specifies the text on the tab. The optional icon argument specifies the tab's icon. The component argument specifies the component that the tabbed pane should show when the tab is selected. The fourth argument, if present, specifies the tool tip text for the tab. |
> | [void setTabLayoutPolicy(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JTabbedPane.html#setTabLayoutPolicy(int))   [int getTabLayoutPolicy()](http://download.oracle.com/javase/7/docs/api/javax/swing/JTabbedPane.html#getTabLayoutPolicy()) | Sets or gets the policy that the tabbed pane uses in laying out tabs when all tabs do not fit within a single run. Possible values are `WRAP_TAB_LAYOUT` and `SCROLL_TAB_LAYOUT`. The default policy is `WRAP_TAB_LAYOUT`. || [void setTabPlacement(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JTabbedPane.html#setTabPlacement(int))   [int getTabPlacement()](http://download.oracle.com/javase/7/docs/api/javax/swing/JTabbedPane.html#getTabPlacement()) | Sets or gets the location where the tabs appear relative to the content. Possible values (defined in `SwingConstants`, which is implemented by `JTabbedPane`) are `TOP`, `BOTTOM`, `LEFT`, and `RIGHT`. |
>
> **Inserting, Removing, Finding, and Selecting Tabs**
>
> | Method | Purpose |
> | [insertTab(String, Icon, Component, String, int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JTabbedPane.html#insertTab(java.lang.String, javax.swing.Icon, java.awt.Component, java.lang.String, int)) | Inserts a tab at the specified index, where the first tab is at index 0. The arguments are the same as for `addTab`. |
> | [remove(Component)](http://download.oracle.com/javase/7/docs/api/javax/swing/JTabbedPane.html#remove(java.awt.Component))   [removeTabAt(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JTabbedPane.html#removeTabAt(int)) | Removes the tab corresponding to the specified component or index. |
> | [removeAll()](http://download.oracle.com/javase/7/docs/api/javax/swing/JTabbedPane.html#removeAll()) | Removes all tabs. |
> | [int indexOfComponent(Component)](http://download.oracle.com/javase/7/docs/api/javax/swing/JTabbedPane.html#indexOfComponent(java.awt.Component))   [int indexOfTab(String)](http://download.oracle.com/javase/7/docs/api/javax/swing/JTabbedPane.html#indexOfTab(java.lang.String))   [int indexOfTab(Icon)](http://download.oracle.com/javase/7/docs/api/javax/swing/JTabbedPane.html#indexOfTab(javax.swing.Icon)) | Returns the index of the tab that has the specified component, title, or icon. |
> | [void setSelectedIndex(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JTabbedPane.html#setSelectedIndex(int))   [void setSelectedComponent(Component)](http://download.oracle.com/javase/7/docs/api/javax/swing/JTabbedPane.html#setSelectedComponent(java.awt.Component)) | Selects the tab that has the specified component or index. Selecting a tab has the effect of displaying its associated component. |
> | [int getSelectedIndex()](http://download.oracle.com/javase/7/docs/api/javax/swing/JTabbedPane.html#getSelectedIndex())   [Component getSelectedComponent()](http://download.oracle.com/javase/7/docs/api/javax/swing/JTabbedPane.html#getSelectedComponent()) | Returns the index or component for the selected tab. |
>
> **Changing Tab Appearance**
>
> | Method | Purpose |
> | [void setComponentAt(int, Component)](http://download.oracle.com/javase/7/docs/api/javax/swing/JTabbedPane.html#setComponentAt(int, java.awt.Component))   [Component getComponentAt(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JTabbedPane.html#getComponentAt(int)) | Sets or gets which component is associated with the tab at the specified index. The first tab is at index 0. |
> | [void setTitleAt(int, String)](http://download.oracle.com/javase/7/docs/api/javax/swing/JTabbedPane.html#setTitleAt(int, java.lang.String))   [String getTitleAt(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JTabbedPane.html#getTitleAt(int)) | Sets or gets the title of the tab at the specified index. |
> | [void setIconAt(int, Icon)](http://download.oracle.com/javase/7/docs/api/javax/swing/JTabbedPane.html#setIconAt(int, javax.swing.Icon))   [Icon getIconAt(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JTabbedPane.html#getIconAt(int))   [void setDisabledIconAt(int, Icon)](http://download.oracle.com/javase/7/docs/api/javax/swing/JTabbedPane.html#setDisabledIconAt(int, javax.swing.Icon))   [Icon getDisabledIconAt(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JTabbedPane.html#getDisabledIconAt(int)) | Sets or gets the icon displayed by the tab at the specified index. |
> | [void setBackgroundAt(int, Color)](http://download.oracle.com/javase/7/docs/api/javax/swing/JTabbedPane.html#setBackgroundAt(int, java.awt.Color))   [Color getBackgroundAt(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JTabbedPane.html#getBackgroundAt(int))   [void setForegroundAt(int, Color)](http://download.oracle.com/javase/7/docs/api/javax/swing/JTabbedPane.html#setForegroundAt(int, java.awt.Color))   [Color getForegroundAt(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JTabbedPane.html#getForegroundAt(int)) | Sets or gets the background or foreground color used by the tab at the specified index. By default, a tab uses the tabbed pane's background and foreground colors. For example, if the tabbed pane's foreground is black, then each tab's title is black except for any tabs for which you specify another color using `setForegroundAt`. |
> | [void setEnabledAt(int, boolean)](http://download.oracle.com/javase/7/docs/api/javax/swing/JTabbedPane.html#setEnabledAt(int, boolean))   [boolean isEnabledAt(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JTabbedPane.html#isEnabledAt(int)) | Sets or gets the enabled state of the tab at the specified index. |
> | [void setMnemonicAt(int, int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JTabbedPane.html#setMnemonicAt(int, int))   [int getMnemonicAt(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JTabbedPane.html#getMnemonicAt(int)) | Sets or gets the keyboard mnemonic for accessing the specified tab. |
> | [void setDisplayedMnemonicIndexAt(int, int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JTabbedPane.html#setDisplayedMnemonicIndexAt(int, int))   [int getDisplayedMnemonicIndexAt(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JTabbedPane.html#getDisplayedMnemonicIndexAt(int)) | Sets or gets which character should be decorated to represent the mnemonic. This is useful when the mnemonic character appears multiple times in the tab's title and you don't want the first occurrence underlined. |
> | [void setToolTipTextAt(int, String)](http://download.oracle.com/javase/7/docs/api/javax/swing/JTabbedPane.html#setToolTipTextAt(int, java.lang.String))   [String getToolTipTextAt(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JTabbedPane.html#getToolTipTextAt(int)) | Sets or gets the text displayed on tool tips for the specified tab. |
>
> **Setting Up Custom Components on Tabs**
>
> | Method | Purpose |
> | [void setTabComponentAt(int, Component)](http://download.oracle.com/javase/7/docs/api/javax/swing/JTabbedPane.html#setTabComponentAt(int, java.awt.Component)) | Sets the component that is responsible for rendering the title or icon (or both) for the tab specified by the first argument. When a null value is specified, `JTabbedPane` renders the title or icon. The same component cannot be used for several tabs. |
> | [Component getTabComponentAt(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JTabbedPane.html#getTabComponentAt(int)) | Gets the tab component for the tab at the index specified by the argument. If there is no tab component for the specified tab, a null value is returned. |
> | [int indexOfTabComponent(Component)](http://download.oracle.com/javase/7/docs/api/javax/swing/JTabbedPane.html#indexOfTabComponent(java.awt.Component)) | Checks if the specified component belongs to one of the tabs. Return the index of the corresponding tab or -1 if there is no such a tab. |

### Examples That Use Tabbed Panes

> This table lists examples that use `JTabbedPane`
> and points to where those examples are described.
>
> | Example | Where Described | Notes |
> | --- | --- | --- |
> | [`TabbedPaneDemo`](../examples/components/index.html#TabbedPaneDemo) | This page | Demonstrates a few tabbed pane features, such as tool tips, icons, scrollable layout, and mnemonics. |
> | [`TabComponentsDemo`](../examples/components/index.html#TabComponentsDemo) | This page | Demonstrates custom components on tabs. Uses a tabbed pane with close buttons. |
> | [`BoxAlignmentDemo`](../examples/layout/index.html#BoxAlignmentDemo) | [How to Use BoxLayout](../layout/box.html) | Uses a `JTabbedPane` as the only child of a frame's content pane. |
> | [`BorderDemo`](../examples/components/index.html#BorderDemo) | [How to Use Borders](../components/border.html) | Uses its tabbed pane in a manner similar to `BoxAlignmentDemo`. |
> | [`DialogDemo`](../examples/components/index.html#DialogDemo) | [How to Use Dialogs](dialog.html) | Has a tabbed pane in the center of a frame's content pane, with a label below it. |

[« Previous](splitpane.html)
•
[Trail](../TOC.html)
•
[Next »](table.html)

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

**Previous page:** How to Use Split Panes
  
**Next page:** How to Use Tables




A browser with JavaScript enabled is required for this page to operate properly.