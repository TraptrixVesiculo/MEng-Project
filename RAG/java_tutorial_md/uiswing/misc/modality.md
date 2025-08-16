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

[How to Use Key Bindings](keybinding.html)

How to Use Modality in Dialogs

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

[« Previous](keybinding.html) • [Trail](../TOC.html) • [Next »](printtable.html)

# How to Use Modality in Dialogs

Java™ SE 6 has resolved modality issues that arose in earlier versions of the platform.
The new modality model enables the developer to scope, or limit, a dialog box's modality blocking.

Before proceding with the new modality model, review the following terms:

* Dialog box — A top-level pop-up window with a title and a border that
  typically takes some form of input from the user. A dialog box can be modal or modeless.
  For more information about dialog boxes, see
  [An Overview of Dialogs](../components/dialog.html#overview) in the
  [How to Make Dialogs](../components/dialog.html) page.
* Modal dialog box — A dialog box that blocks input to some other top-level windows
  in the application, except for windows created with the dialog box as their owner.
  The modal dialog box captures the window focus until it is closed, usually in response to a button press.
* Modeless dialog box — A dialog box that enables you to operate with other windows while this dialog box is shown.

In Java SE 6 the behavior of both modal and modeless dialog boxes has
been changed so that they always appear on top of both not only of their parent windows and of all blocked windows as well.

The following modality types are supported in Java SE 6:

* **Modeless type** — A modeless dialog box does not block any other window while it is visible.
* **Document-modal type** — A document-modal dialog box blocks all windows from the
  same document, except windows from its child hierarchy. In this context, a document
  is a hierarchy of windows that share a common ancestor, called the document root, which is the closest
  ancestor window without an owner.
* **Application-modal type** — An application-modal dialog box blocks
  all windows from the same application, except windows from its child hierarchy.
  If several applets are launched in a browser environment, the browser is allowed
  to treat them either as separate applications or as a single application.
  This behavior is implementation-dependent.
* **Toolkit-modal type** — A toolkit-modal dialog box blocks all windows
  that run in the same toolkit, except windows from its child hierarchy. If several
  applets are launched, all of them run with the same toolkit. Hence, a toolkit-modal
  dialog box shown from an applet may affect other applets and all windows of the browser
  instance that embeds the Java runtime environment for this toolkit.

Additionally, you can set up the modality exclusion mode:

* **Exclusion mode** — Any top-level window can be marked not to be blocked by modal dialogs. This property enables you to set up the *modal exclusion* mode. The `Dialog.ModalExclusionType` enum specifies the possible modal exclusion types.

---

**Note :** The new modality model does not implement a system modality, which blocks
all applications (including Java applications) that are displayed on the desktop while a modal dialog box is active.

---

The ModalityDemo example demonstrates the first three of the four modality types mentioned above.

[![Four frames to demonstrate different modality types ](../../figures/uiswing/misc/modalityDemo.png)](../../figures/uiswing/misc/modalityDemo.png)  
*This figure has been reduced to fit on the page.   
 Click the image to view it at its natural size.*

---

**Try this:**

1. Click the Launch button
   to run ModalityDemo using
   [Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp)
   ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
   Alternatively, to compile and run the example yourself,
   consult the
   [example index](../examples/misc/index.html#ModalityDemo).

   [![Launches the ModalityDemo application](../../images/jws-launch-button.png)](http://download.oracle.com/javase/tutorialJWS/uiswing/misc/ex6/ModalityDemo.jnlp)

   - The following dialog boxes will appear:
     * Book 1 (parent frame)
     * Book 2 (parent frame)
     * Feedback (parent frame)
     * Classics (excluded frame)- Switch to the Book 1 frame and choose the Biography title for the book,
       then select OK.
     - The Biography title will be displayed in the title of the dialog box.
       Enter the name, for example - “John”, into the text field.
     - Switch to the Book 1 frame and change the title to Funny Tale, then select OK.
       Since the dialog box for entering the name is *modeless*, you can easily switch to
       its *parent* frame.

     ---

     **Note :** The modeless dialog box title has been changed to Funny Tale.

     ---

     - Select OK in the modeless dialog box.
     - The Funny tale document-modal dialog box appears.
     - Type some text in the
       text field. Notice that it is signed by the name you entered in the modeless dialog box.
     - Switch to the modeless dialog box and try to change your name. You will not be able
       to do so, because the document-modal dialog box
       blocks all windows in its parent hierarchy.
     - Perform the same sequence of operations (steps 3 - 9) for the Book 2 parent frame.
     - Try switching to different dialog boxes. You will notice that you can
       switch either to the Classics frame or to the Feedback frame as well as to the
       dialog box of either the Book 1 frame or the Book 2 frame.
     - Switch to the Feedback parent frame. Select Rate Yourself.
     - The confirmation dialog box will appear. Try switching to different dialog boxes.
       You are only enabled to switch to the Classics dialog box because the standard confirmation dialog box
       is an application-modal dialog box and it blocks all windows from the same application.
       However, you will notice that you can select your favorite classical author in the
       Classics frame. This frame has been created by using the `APPLICATION_EXCLUDE`
       modality exclusion type, which prevents all top-level windows from being blocked by any application-modal
       dialog boxes.

---

The following code snippet shows how to create dialog boxes of different modality
types:

```

//The Book 1 parent frame
f1 = new JFrame("Book 1 (parent frame)");

...

//The modeless dialog box
d2 = new JDialog(f1);

...
	
//The document-modal dialog box
d3 = new JDialog(d2, "", Dialog.ModalityType.DOCUMENT_MODAL);

...

	//The Book2 parent frame
f4 = new JFrame("Book 2 (parent frame)");

...

//The modeless dialog box
d5 = new JDialog(f4);

...

//The document-modality dialog box
d6 = new JDialog(d5, "", Dialog.ModalityType.DOCUMENT_MODAL);
	
...

//The excluded frame
f7 = new JFrame("Classics (excluded frame)");
f7.setModalityExclusionType(Dialog.ModalExclusionType.APPLICATION_EXCLUDED);
	
...

//The Feedback parent frame and Confirm Dialog box
f8 = new JFrame("Feedback (parent frame)");
...

JButton b8 = new JButton("Rate yourself");
b8.addActionListener(new ActionListener() {
    public void actionPerformed(ActionEvent e) {
        JOptionPane.showConfirmationDialog(null,
                                           "I really like my book",
                                           "Question (application-modal dialog)", 
                                           JOptionPane.Yes_NO_OPTION,
                                           JOptionPane.QUESTION_MESSAGE); 
    }
});


```

Find the demo's complete code in the
[`ModalityDemo.java`](../examples/misc/ModalityDemoProject/src/misc/ModalityDemo.java) file.

In Java SE 6 you can create a document-modal dialog box without a parent.
Because the `Dialog` class is a subclass of the `Window` class,
a `Dialog` instance automatically becomes the root of the document if it has no owner.
Thus, if such a dialog box is document-modal, its scope of blocking is empty, and it behaves as if it were
a modeless dialog box.

### The Modality API

> The `JDialog` class constructors enable you to create dialog boxes of various modality types.
>
> | Constructor | Purpose |
> | --- | --- |
> | [JDialog(Dialog owner)](http://download.oracle.com/javase/7/docs/api/javax/swing/JDialog.html#JDialog(java.awt.Dialog)) | Creates a modeless dialog box with the specified `Dialog` owner but without a title. |
> | [JDialog(Dialog owner, boolean modal)](http://download.oracle.com/javase/7/docs/api/javax/swing/JDialog.html#JDialog(java.awt.Dialog,%20boolean)) | Creates a dialog box with the specified `Dialog` owner and modality. |
> | [JDialog(Dialog owner, String title)](http://download.oracle.com/javase/7/docs/api/javax/swing/JDialog.html#JDialog(java.awt.Dialog,%20java.lang.String)) | Creates a modeless dialog box with the specified `Dialog` owner and title. |
> | [JDialog(Dialog owner, String title, boolean modal)](http://download.oracle.com/javase/7/docs/api/javax/swing/JDialog.html#JDialog(java.awt.Dialog,%20java.lang.String,%20boolean)) | Creates a dialog box with the specified `Dialog` owner, title, and modality. |
> | [JDialog(Dialog owner, String title, boolean modal, GraphicsConfiguration gc)](http://download.oracle.com/javase/7/docs/api/javax/swing/JDialog.html#JDialog(java.awt.Dialog,%20java.lang.String,%20boolean,%20java.awt.GraphicsConfiguration)) | Creates a dialog box with the specified `Dialog` owner, title, modality, and graphics configuration. |
> | [JDialog(Frame owner)](http://download.oracle.com/javase/7/docs/api/javax/swing/JDialog.html#JDialog(java.awt.Frame)) | Creates a modeless dialog box without a title with the specified `Frame` owner. If the value for the owner is null, a shared, hidden frame will be set as the owner of the dialog box. |
> | [JDialog(Window owner, String title, Dialog.ModalityType modalityType)](http://download.oracle.com/javase/7/docs/api/javax/swing/JDialog.html#JDialog(java.awt.Window,%20java.lang.String,%20java.awt.Dialog.ModalityType)) | Creates a dialog box with the specified `Window` owner, title, and modality. |
>
> The following table lists methods inherited from the
> [`java.awt.Dialog`](http://download.oracle.com/javase/7/docs/api/java/awt/Dialog.html) class.
>
> | Method | Purpose |
> | --- | --- |
> | [getModalityType](http://download.oracle.com/javase/7/docs/api/java/awt/Dialog.html#getModalityType()) | Returns the modality type for this dialog box. |
> | [setModalityType](http://download.oracle.com/javase/7/docs/api/java/awt/Dialog.html#setModalityType(java.awt.Dialog.ModalityType)) | Sets the modality type for this dialog box. See [ModalityType](http://download.oracle.com/javase/7/docs/api/java/awt/Dialog.ModalityType.html) for possible modality types. If the given modality type is not supported, then the `MODELESS` type is used. To ensure that the modality type has been set, call the `getModalityType()` method after calling this method. |

### Examples That Use Modality API
> The following table lists the
> example that uses modality in dialogs.
>
> | Example | Where Described | Notes |
> | --- | --- | --- |
> | [`ModalityDemo`](../examples/misc/index.html#ModalityDemo) | This section | Creates dialog boxes of different modality types, demonstrates scope blocking for those types. |

[« Previous](keybinding.html)
•
[Trail](../TOC.html)
•
[Next »](printtable.html)

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

**Previous page:** How to Use Key Bindings
  
**Next page:** How to Print Tables




A browser with JavaScript enabled is required for this page to operate properly.