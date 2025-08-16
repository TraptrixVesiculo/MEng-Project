[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Creating a GUI With JFC/Swing
  
**Lesson:** Drag and Drop and Data Transfer

[Drag and Drop and Data Transfer](index.html)

[Introduction to DnD](intro.html)

[Default DnD Support](defaultsupport.html)

[Demo - BasicDnD](basicdemo.html)

[TransferHandler Class](transferhandler.html)

[Export Methods](export.html)

[Import Methods](import.html)

[TransferSupport Class](transfersupport.html)

[Setting the Drop Mode](dropmodes.html)

[Demo - DropDemo](dropmodedemo.html)

[Choosing the Drop Action](dropaction.html)

[Demo - ChooseDropAction](dropactiondemo.html)

[Showing the Drop Location](showdroploc.html)

[Location Sensitive Drop](locsensitivedrop.html)

[Demo - LocationSensitiveDemo](locsensitivedemo.html)

[Empty Table Drop](emptytable.html)

[Drop Location Rendering](droplocation.html)

[Top-Level Drop](toplevel.html)

[Adding Cut, Copy and Paste (CCP)](cutpaste.html)

[CCP in a Text Component](textpaste.html)

CCP in a non-Text Component

[Using and Creating a DataFlavor](dataflavor.html)

[Putting it All Together - DnD and CCP](together.html)

[Further Information](info.html)

[Solving Common Data Transfer Problems](problems.html)

[Home Page](../../index.html)
>
[Creating a GUI With JFC/Swing](../index.html)
>
[Drag and Drop and Data Transfer](index.html)

[« Previous](textpaste.html) • [Trail](../TOC.html) • [Next »](dataflavor.html)

# CCP in a non-Text Component

If you are implementing cut, copy and paste using one of the Swing components
that is *not* one of the text components you have to do some additional setup.
First, you need to install the cut, copy, and paste actions in the action
map. The following method shows how to do this:

```

    private void setMappings(JList list) { 
        ActionMap map = list.getActionMap();
        map.put(TransferHandler.getCutAction().getValue(Action.NAME),
                TransferHandler.getCutAction());
        map.put(TransferHandler.getCopyAction().getValue(Action.NAME),
                TransferHandler.getCopyAction());
        map.put(TransferHandler.getPasteAction().getValue(Action.NAME),
                TransferHandler.getPasteAction());

```

When you set up the Edit menu, you can also choose to add menu accelerators,
so that the user can type Control-C to initiate a copy, for example.
In the following code snippet, the bolded text shows how to set the menu
accelerator for the cut action:

```

    menuItem = new JMenuItem("Cut");
    menuItem.setActionCommand((String)TransferHandler.getCutAction().
             getValue(Action.NAME));
    menuItem.addActionListener(actionListener);
    menuItem.setAccelerator(
      KeyStroke.getKeyStroke(KeyEvent.VK_X, ActionEvent.CTRL_MASK));
    menuItem.setMnemonic(KeyEvent.VK_T);
    mainMenu.add(menuItem);

```

If you have set the menu accelerators for the CCP actions,
this next step is redundant.
If you have not set the menu accelerators, you need to add the CCP bindings
to the input map. The following code snippet shows how this is done:

```

    // only required if you have not set the menu accelerators
    InputMap imap = this.getInputMap();
    imap.put(KeyStroke.getKeyStroke("ctrl X"),
        TransferHandler.getCutAction().getValue(Action.NAME));
    imap.put(KeyStroke.getKeyStroke("ctrl C"),
        TransferHandler.getCopyAction().getValue(Action.NAME));
    imap.put(KeyStroke.getKeyStroke("ctrl V"),
        TransferHandler.getPasteAction().getValue(Action.NAME));

```

Once the bindings have been installed and the Edit menu has been
set up, there is another issue to be addressed:
When the user initiates a cut, copy or a paste,
which component should receive the action?
In the case of a text component, the `DefaultEditorKit`
remembers which component last had the focus and forwards the
action to that component. The following class, `TransferActionListener`,
performs the same function for non-text Swing components.
This class can be dropped into most any application:

```

public class TransferActionListener implements ActionListener,
                                              PropertyChangeListener {
    private JComponent focusOwner = null;

    public TransferActionListener() {
        KeyboardFocusManager manager = KeyboardFocusManager.
           getCurrentKeyboardFocusManager();
        manager.addPropertyChangeListener("permanentFocusOwner", this);
    }

    public void propertyChange(PropertyChangeEvent e) {
        Object o = e.getNewValue();
        if (o instanceof JComponent) {
            focusOwner = (JComponent)o;
        } else {
            focusOwner = null;
        }
    }

    public void actionPerformed(ActionEvent e) {
        if (focusOwner == null)
            return;
        String action = (String)e.getActionCommand();
        Action a = focusOwner.getActionMap().get(action);
        if (a != null) {
            a.actionPerformed(new ActionEvent(focusOwner,
                                              ActionEvent.ACTION_PERFORMED,
                                              null));
        }
    }
}

```

Finally, you have to decide how to handle the paste. In the case of a
drag and drop, you insert the data at the drop location. In the case of
a paste, you do not have the benefit of the user pointing to the desired
paste location. You need to decide what makes sense for your application —
inserting the data before or after the current selection might be the best solution.

The following demo, ListCutPaste, shows how to implement CCP in an instance
of `JList`.
As you can see in the screen shot there are three lists and you can cut,
copy, and paste to or from any of these lists. They also support drag and drop.
For this demo, the pasted data is inserted after the current selection. If there
is no current selection, the data is appended to the end of the list.

![A snapshot of the ListCutPaste demo.](../../figures/uiswing/dnd/ListCutPaste.png)

---

**Try this:**

1. Click the Launch button to run ListCutPaste using
   [Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp) ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
   Alternatively, to compile and run the example yourself,
   consult the
   [example index](../examples/dnd/index.html#ListCutPaste).

   [![Launches the ListCutPaste example](../../images/jws-launch-button.png)](http://download.oracle.com/javase/tutorialJWS/uiswing/dnd/ex6/ListCutPaste.jnlp)

   - Select an item in one of the lists. Use the Edit menu or the keyboard
     equivalent to cut or copy the list item from the source.- Select the list item where you want the item to be pasted.- Paste the text using the menu or the keyboard equivalent.
         The item is pasted after the current selection.- Perform the same operation using drag and drop.

---

[« Previous](textpaste.html)
•
[Trail](../TOC.html)
•
[Next »](dataflavor.html)

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

**Previous page:** CCP in a Text Component
  
**Next page:** Using and Creating a DataFlavor




A browser with JavaScript enabled is required for this page to operate properly.