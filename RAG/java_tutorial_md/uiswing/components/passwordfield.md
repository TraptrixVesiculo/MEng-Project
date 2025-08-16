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

How to Use Password Fields

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

[« Previous](panel.html) • [Trail](../TOC.html) • [Next »](progress.html)

# How to Use Password Fields

The
[`JPasswordField`](http://download.oracle.com/javase/7/docs/api/javax/swing/JPasswordField.html) class, a subclass of `JTextField`,
provides specialized text fields for password entry.
For security reasons,
a password field does not show the characters that the user types.
Instead, the field displays a character different
from the one typed, such as an asterisk '\*'.
As another security precaution,
a password field stores its value
as an array of characters,
rather than as a string.
Like an ordinary [text field](textfield.html),
a password field fires an
[action event](../events/actionlistener.html) when the user indicates that text entry is complete,
for example by pressing the Enter button.

Here is a picture of a demo
that opens a small window
and prompts the user to type in a password.

![A snapshot of PasswordDemo, which uses a password field](../../figures/uiswing/components/PasswordDemo.png)

Click the Launch button
to run PasswordDemo
using
[Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp ) 
([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
Alternatively, to compile and run the example yourself,
consult the [example index](../examples/components/index.html#PasswordDemo).

[![Launches the PasswordDemo Application](../../images/jws-launch-button.png)](http://download.oracle.com/javase/tutorialJWS/uiswing/components/ex6/PasswordDemo.jnlp)

The password is "bugaboo".
You can find the entire code for this program in
[`PasswordDemo.java`](../examples/components/PasswordDemoProject/src/components/PasswordDemo.java).
Here is the code that creates
and sets up the password field:

```

passwordField = new JPasswordField(10);
passwordField.setActionCommand(OK);
passwordField.addActionListener(this);

```

The argument passed into the `JPasswordField` constructor
indicates the preferred size of the field,
which is at least 10 columns wide in this case.
By default a password field displays a dot for
each character typed.
If you want to change the echo character,
call the `setEchoChar` method.
The code then adds an action listener to the password field,
which checks the value typed in by the user.
Here is the implementation of the action listener's
`actionPerformed` method:

```

public void actionPerformed(ActionEvent e) {
    String cmd = e.getActionCommand();

    if (OK.equals(cmd)) { //Process the password.
        char[] input = passwordField.getPassword();
        if (isPasswordCorrect(input)) {
            JOptionPane.showMessageDialog(controllingFrame,
                "Success! You typed the right password.");
        } else {
            JOptionPane.showMessageDialog(controllingFrame,
                "Invalid password. Try again.",
                "Error Message",
                JOptionPane.ERROR_MESSAGE);
        }

        //Zero out the possible password, for security.
        Arrays.fill(input, '0');

        passwordField.selectAll();
        resetFocus();
    } else ...//handle the Help button...
}

```

---

**Security note:** Although the `JPasswordField` class
inherits the `getText` method,
you should use the `getPassword` method instead.
Not only is `getText` less secure,
but in the future it might return the visible string
(for example, `"******"`)
instead of the typed string.

To further enhance security,
once you are finished with the character array returned by
the `getPassword` method,
you should set each of its elements to zero.
The preceding code snippet shows how to do this.

---

A program that uses a password field typically
validates the password before completing any actions
that require the password.
This program calls a private method,
`isPasswordCorrect`,
that compares the value returned by the `getPassword` method
to a value stored in a character array.
Here is its code:

```

private static boolean isPasswordCorrect(char[] input) {
    boolean isCorrect = true;
    char[] correctPassword = { 'b', 'u', 'g', 'a', 'b', 'o', 'o' };

    if (input.length != correctPassword.length) {
        isCorrect = false;
    } else {
        isCorrect = Arrays.equals (input, correctPassword);
    }

    //Zero out the password.
    Arrays.fill(correctPassword,'0');

    return isCorrect;
}

```

### The Password Field API

> The following tables list the commonly used
> `JPasswordField`
> constructors and methods.
> For information on the API
> that password fields inherit,
> see
> [How to Use Text Fields](textfield.html).
>
> **Commonly Used JPasswordField Constructors
> and Methods**
>
> | Constructor or Method | Purpose |
> | [JPasswordField()](http://download.oracle.com/javase/7/docs/api/javax/swing/JPasswordField.html#JPasswordField())   [JPasswordField(String)](http://download.oracle.com/javase/7/docs/api/javax/swing/JPasswordField.html#JPasswordField(java.lang.String))   [JPasswordField(String, int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JPasswordField.html#JPasswordField(java.lang.String, int))   [JPasswordField(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JPasswordField.html#JPasswordField(int))   [JPasswordField(Document, String, int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JPasswordField.html#JPasswordField(javax.swing.text.Document, java.lang.String, int)) | Creates a password field. When present, the `int` argument specifies the desired width in columns. The `String` argument contains the field's initial text. The `Document` argument provides a custom model for the field. |
> | [char[] getPassword()](http://download.oracle.com/javase/7/docs/api/javax/swing/JPasswordField.html#getPassword()) | Returns the password as an array of characters. |
> | [void setEchoChar(char)](http://download.oracle.com/javase/7/docs/api/javax/swing/JPasswordField.html#setEchoChar(char))   [char getEchoChar()](http://download.oracle.com/javase/7/docs/api/javax/swing/JPasswordField.html#getEchoChar()) | Sets or gets the echo character which is displayed instead of the actual characters typed by the user. |
> | [void addActionListener(ActionListener)](http://download.oracle.com/javase/7/docs/api/javax/swing/JTextField.html#addActionListener(java.awt.event.ActionListener))   [void removeActionListener(ActionListener)](http://download.oracle.com/javase/7/docs/api/javax/swing/JTextField.html#removeActionListener(java.awt.event.ActionListener))   *(defined in `JTextField`)* | Adds or removes an action listener. |
> | [void selectAll()](http://download.oracle.com/javase/7/docs/api/javax/swing/text/JTextComponent.html#selectAll())  *(defined in `JTextComponent`)* | Selects all characters in the password field. |

### Examples That Use Password Fields

> [PasswordDemo](../examples/components/index.html#PasswordDemo)
> is the Tutorial's only example that uses
> a `JPasswordField` object.
> However, the Tutorial has many examples that use
> `JTextField` objects,
> whose API is inherited by `JPasswordField`.
> See [Examples That Use Text Fields](textfield.html#eg)
> for further information.

[« Previous](panel.html)
•
[Trail](../TOC.html)
•
[Next »](progress.html)

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

**Previous page:** How to Use Panels
  
**Next page:** How to Use Progress Bars




A browser with JavaScript enabled is required for this page to operate properly.