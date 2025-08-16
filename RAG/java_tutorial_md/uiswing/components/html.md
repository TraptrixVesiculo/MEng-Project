[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Creating a GUI With JFC/Swing
  
**Lesson:** Using Swing Components

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

[How to Use Tabbed Panes](tabbedpane.html)

[How to Use Tables](table.html)

[How to Use Text Areas](textarea.html)

[How to Use Text Fields](textfield.html)

[How to Use Tool Bars](toolbar.html)

[How to Use Tool Tips](tooltip.html)

[How to Use Trees](tree.html)

How to Use HTML in Swing Components

[How to Use Models](model.html)

[How to Use Icons](icon.html)

[How to Use Borders](border.html)

[Solving Common Component Problems](problems.html)

[Home Page](../../index.html)
>
[Creating a GUI With JFC/Swing](../index.html)
>
[Using Swing Components](index.html)

[« Previous](tree.html) • [Trail](../TOC.html) • [Next »](model.html)

# How to Use HTML in Swing Components

Many Swing components display a text string
as part of their GUI.
By default, a component's text is displayed
in a single font and color,
all on one line.
You can determine the font and color of a component's text
by invoking the component's `setFont` and `setForeground`
methods, respectively.
For example, the following code
creates a label and then sets its font and color:

```

label = new JLabel("A label");
label.setFont(new Font("Serif", Font.PLAIN, 14));
label.setForeground(new Color(0xffffdd));

```

If you want to mix fonts or colors within the text,
or if you want formatting such as multiple lines,
you can use HTML.
HTML formatting can be used in all Swing buttons, menu items,
labels, tool tips, and tabbed panes,
as well as in components such as trees and tables
that use labels to render text.

To specify that a component's text has HTML formatting,
just put the `<html>` tag at the beginning of the text,
then use any valid HTML in the remainder.
Here is an example of using HTML in a button's text:

```

button = new JButton("<html><b><u>T</u>wo</b><br>lines</html>");

```

Here is the resulting button.
![Screenshot of a button that shows HTML in the Metal look and feel.](../../figures/uiswing/components/HtmlButtonMetal.png)

### An Example: HtmlDemo

> An application called `HtmlDemo`
> lets you play with HTML formatting
> by setting the text on a label. You can find the entire code for this program in
> [`HtmlDemo.java`](../examples/components/HtmlDemoProject/src/components/HtmlDemo.java).
> Here is a picture of the `HtmlDemo`
> example.
>
> ![Screenshot of HtmlDemo in the Metal look and feel.](../../figures/uiswing/components/HtmlDemoMetal.png)
>
> ---
>
> **Try This:**
>
> 1. Click the Launch button
>    to run HtmlDemo using
>    [Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp ) 
>    ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
>    Alternatively, to compile and run the example yourself,
>    consult the [example index](../examples/components/index.html#HtmlDemo).
>
> [![Launches the HtmlDemo Application](../../images/jws-launch-button.png)](http://download.oracle.com/javase/tutorialJWS/uiswing/components/ex6/HtmlDemo.jnlp)
>
> 2. Edit the HTML formatting in the text area at the left
>    and click the "Change the label" button. The
>    label at the right shows the result.
> 3. Remove the <html> tag from the text area on the left.
>    The label's text is no longer parsed as HTML.
>
> ---

### Example 2: ButtonHtmlDemo

> Let us look at another example that uses HTML.
> `ButtonHtmlDemo` adds font, color, and other text formatting
> to three buttons. You can find the entire code for this program in
> [`ButtonHtmlDemo.java`](../examples/components/ButtonHtmlDemoProject/src/components/ButtonHtmlDemo.java). Here is a picture of the `ButtonHtmlDemo`
> example.
>
> ![Screenshot of ButtonHtmlDemo in the Metal look and feel.](../../figures/uiswing/components/ButtonHtmlDemoMetal.png)
>
> Click the Launch button
> to run ButtonHtmlDemo
> using
> [Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp)
> ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
> Alternatively, to compile and run the example yourself, consult the
> [example index](../examples/components/index.html#ButtonHtmlDemo).
>
> [![Launches the ButtonHtmlDemo Application](../../images/jws-launch-button.png)](http://download.oracle.com/javase/tutorialJWS/uiswing/components/ex6/ButtonHtmlDemo.jnlp)
>
> The left and right buttons have multiple lines and text styles
> and are implemented using
> HTML. The middle button, on the other hand,
> uses just one line, font, and color, so it does not
> require HTML.
> Here is the code that specifies
> the text formatting for these three buttons:
>
> ```
>
> b1 = new JButton("<html><center><b><u>D</u>isable</b><br>"
>                  + "<font color=#ffffdd>middle button</font>",
>                  leftButtonIcon);
> Font font = b1.getFont().deriveFont(Font.PLAIN);
> b1.setFont(font);
> ...
> b2 = new JButton("middle button", middleButtonIcon);
> b2.setFont(font);
> b2.setForeground(new Color(0xffffdd));
> ...
> b3 = new JButton("<html><center><b><u>E</u>nable</b><br>"
>                  + "<font color=#ffffdd>middle button</font>",
>                  rightButtonIcon);
> b3.setFont(font);
>
> ```
>
> Note that we have to use a `<u>` tag to cause
> the mnemonic characters "D" and "E" to be underlined in
> the buttons that use HTML. Note also that when
> a button is disabled, its HTML text unfortunately
> remains black, instead of becoming gray.
> (Refer to
> [bug #4783068](http://developer.java.sun.com/developer/bugParade/bugs/4783068.html) to see if this situation changes.)
>
> This section discussed how to use HTML in ordinary,
> non-text components.
> For information on components whose primary purpose is formatting text,
> see
> [Using Text Components](text.html).

[« Previous](tree.html)
•
[Trail](../TOC.html)
•
[Next »](model.html)

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

**Previous page:** How to Use Trees
  
**Next page:** How to Use Models




A browser with JavaScript enabled is required for this page to operate properly.