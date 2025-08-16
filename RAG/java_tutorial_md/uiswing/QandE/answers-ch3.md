[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)

**Trail:** Creating a GUI With JFC/Swing

[Home Page](../../index.html)
>
[Creating a GUI With JFC/Swing](../index.html)

[« Previous](../TOC.html) • [TOC](../TOC.html)

# Answers: Using Swing Components

> Use the information in this lesson and the component
> [how-to sections](../components/componentlist.html) to help you complete these questions and exercises.

### Questions

> Question 1: Find the component
> that best fits each of the following needs. Write down both the
> component’s common name (such as “frame”) and
> find the component's how-to page online. [*Hint:* You can
> use [A Visual Index to
> the Swing Components](../../ui/features/components.html) to help you answer this question.]
>
> > Question 1a: A component that lets the user
> > pick a color.  
> > Answer 1a: [color
> > chooser](../../uiswing/components/colorchooser.html)  
> >   
> > Question 1b: A component that displays an icon,
> > but that doesn’t react to user clicks.  
> > Answer 1b: [label](../../uiswing/components/label.html)  
> >   
> > Question 1c: A component that looks like a
> > button and that, when pressed, brings up a menu of items for the user to
> > choose from.  
> > Answer 1c: [uneditable
> > combo box](../../uiswing/components/combobox.html)  
> >   
> > Question 1d: A container that looks like a
> > frame, but that appears (usually with other, similar containers) within
> > a real frame.  
> > Answer 1d: [internal
> > frame](../../uiswing/components/internalframe.html)  
> >   
> > Question 1e: A container that lets the user
> > determine how two components share a limited amount of space.  
> > Answer 1e: [split
> > pane](../../uiswing/components/splitpane.html)
>
> Question 2: Which method do you
> use to add a menu bar to a top-level container such as a `JFrame`?  
> Answer 2: `setJMenuBar`
>
> Question 3: Which method do you
> use to specify the default button for a top-level container such
> as a `JFrame` or `JDialog`?  
> Answer 3: `JRootPane`'s `setDefaultButton`
> method. (You get the top-level container's root pane using the `getRootPane`
> method defined by the `RootPaneContainer` interface, which every
> top-level container implements.)
>
> Question 4: Which method do you
> use to enable and disable components such as `JButton`s?
> What class is it defined in?  
> Answer 4: `setEnabled`,
> which is defined in the `Component` class
>
> Question 5a: Which Swing components use `ListSelectionModel`?
> [*Hint:* The “Use” link at the top of the specification for
> each interface and class takes you to a page showing where in the API that
> interface or class is referenced.]  
> Answer 5a: `JList`
> and `JTable`
>
> > Question 5b: Do those components
> > use any other models to handle other aspects of the components’
> > state? If so, list the other models’ types.  
> > Answer 5b: `JList` also uses a `ListModel`,
> > which holds the list's data. `JTable` uses a `TableModel`
> > to hold its data and a `TableColumnModel` to manage the table's
> > columns.
>
> Question 6: Which type of model
> holds a text component’s content?  
> Answer 6: `Document`

### Exercises

> Exercise 1. Implement a program
> with a GUI that looks like the one shown below. Put the main
> method in a class named `MyDemo1`.
>
> > ![MyDemo1.png](../../figures/uiswing/QandE/MyDemo1.png)
>
> Answer 1: See [`MyDemo1.java`](../examples/QandE/MyDemo1Project/src/QandE/MyDemo1.java)[![(in a .java source file)](../../images/sourceIcon.gif)](../examples/QandE/MyDemo1Project/src/QandE/MyDemo1.java).
> Here's the code that adds the bold, italicized text:
>
> > ```
> > JLabel label = new JLabel("My Demo");
> > frame.getContentPane().add(BorderLayout.CENTER, label);
> > label.setFont(label.getFont().deriveFont(Font.ITALIC | Font.BOLD));
> > label.setHorizontalAlignment(JLabel.CENTER)
> > ```
>
> Exercise 2. Make a copy of `MyDemo1.java`
> named `MyDemo2.java`. Add a menu bar to `MyDemo2`.   
> Answer 2: See [`MyDemo2.java`](../examples/QandE/MyDemo2Project/src/QandE/MyDemo2.java)[![(in a .java source file)](../../images/sourceIcon.gif)](../examples/QandE/MyDemo2Project/src/QandE/MyDemo2.java).
> The menu bar can be implemented
> with this code:
>
> > ```
> > JMenu menu = new JMenu("Menu");
> > JMenuBar mb = new JMenuBar();
> > mb.add(menu);
> > frame.setJMenuBar(mb);
> > ```
>
> Exercise 3. Copy `MyDemo1.java`
> to `MyDemo3.java`. Add a button (`JButton`) to `MyDemo3.java`.
> Make it the default button.  
> Answer 3: See [`MyDemo3.java`](../examples/QandE/MyDemo3Project/src/QandE/MyDemo3.java)[![(in a .java source file)](../../images/sourceIcon.gif)](../examples/QandE/MyDemo3Project/src/QandE/MyDemo3.java).
> Here's the code that adds the button
> and makes it the default button:
>
> ```
>
> JButton b = new JButton("A button");
> frame.getContentPane().add(BorderLayout.PAGE_END, b);
> frame.getRootPane().setDefaultButton(b);
>
> ```

[« Previous](../TOC.html)
•
[TOC](../TOC.html)


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

**Previous page:** Questions and Exercises: Using Swing Components




A browser with JavaScript enabled is required for this page to operate properly.