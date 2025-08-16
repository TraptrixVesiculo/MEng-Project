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

CCP in a Text Component

[CCP in a non-Text Component](listpaste.html)

[Using and Creating a DataFlavor](dataflavor.html)

[Putting it All Together - DnD and CCP](together.html)

[Further Information](info.html)

[Solving Common Data Transfer Problems](problems.html)

[Home Page](../../index.html)
>
[Creating a GUI With JFC/Swing](../index.html)
>
[Drag and Drop and Data Transfer](index.html)

[« Previous](cutpaste.html) • [Trail](../TOC.html) • [Next »](listpaste.html)

# CCP in a Text Component

If you are implementing cut, copy and paste using one of the Swing
text components (text field, password field, formatted text field,
or text area) your work is very straightforward. These text components utilize the
[`DefaultEditorKit`](http://download.oracle.com/javase/7/docs/api/javax/swing/text/DefaultEditorKit.html) which provides built-in actions for cut, copy and paste. The default
editor kit also handles the work of remembering which component last had the focus.
This means that if the user initiates one of these actions using the menu
or a keyboard equivalent, the correct component receives the action —
no additional code is required.

The following demo, `TextCutPaste`, contains three text fields.
As you can see in the screen shot, you can cut, copy, and paste to or from
any of these text fields. They also support drag and drop.

![A snapshot of the TextCutPaste demo.](../../figures/uiswing/dnd/TextCutPaste.png)

---

**Try this:**

1. Click the Launch button to run `TextCutPaste` using
   [Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp) ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
   Alternatively, to compile and run the example yourself,
   consult the
   [example index](../examples/dnd/index.html#TextCutPaste).

   [![Launches the TextCutPaste example](../../images/jws-launch-button.png)](http://download.oracle.com/javase/tutorialJWS/uiswing/dnd/ex6/TextCutPaste.jnlp)

   - Select text in one of the text fields. Use the Edit menu or the keyboard
     equivalent to cut or copy the text from the source.- Position the caret where you want the text to be pasted.- Paste the text using the menu or the keyboard equivalent.- Perform the same operation using drag and drop.

---

Here is the code that creates the Edit menu by hooking up the built-in cut, copy,
and paste actions defined in `DefaultEditorKit` to the menu items.
This works with any component that descends from `JComponent`:

```

    /**
     * Create an Edit menu to support cut/copy/paste.
     */
    public JMenuBar createMenuBar () {
        JMenuItem menuItem = null;
        JMenuBar menuBar = new JMenuBar();
        JMenu mainMenu = new JMenu("Edit");
        mainMenu.setMnemonic(KeyEvent.VK_E);

        menuItem = new JMenuItem(new DefaultEditorKit.CutAction());
        menuItem.setText("Cut");
        menuItem.setMnemonic(KeyEvent.VK_T);
        mainMenu.add(menuItem);

        menuItem = new JMenuItem(new DefaultEditorKit.CopyAction());
        menuItem.setText("Copy");
        menuItem.setMnemonic(KeyEvent.VK_C);
        mainMenu.add(menuItem);

        menuItem = new JMenuItem(new DefaultEditorKit.PasteAction());
        menuItem.setText("Paste");
        menuItem.setMnemonic(KeyEvent.VK_P);
        mainMenu.add(menuItem);

        menuBar.add(mainMenu);
        return menuBar;
    }

```

Next we will look at how to accomplish the same functionality using a component
that does not have the built-in support of the `DefaultEditorKit`.

[« Previous](cutpaste.html)
•
[Trail](../TOC.html)
•
[Next »](listpaste.html)

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

**Previous page:** Adding Cut, Copy and Paste (CCP)
  
**Next page:** CCP in a non-Text Component




A browser with JavaScript enabled is required for this page to operate properly.