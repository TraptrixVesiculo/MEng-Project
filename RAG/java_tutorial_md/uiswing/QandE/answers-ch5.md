[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)

**Trail:** Creating a GUI With JFC/Swing

[Home Page](../../index.html)
>
[Creating a GUI With JFC/Swing](../index.html)

[« Previous](../TOC.html) • [TOC](../TOC.html)

# Answers: Writing Event Listeners

Use this lesson’s tables, the [component
how-to sections](../components/index.html) and the [event
listeners how-to sections](../events/handling.html) to complete these questions and
exercises.

### Questions

> Question 1: What listener would
> you implement to be notified when a particular component has
> appeared on screen? What method tells you this information?  
> Answer 1: You would register a
> `ComponentListener` on the component. The
> `componentShown` method. This method is called when
> the window is first displayed or is deiconified.
>
> Question 2: What listener would
> you implement to be notified when the user has finished editing
> a text field by pressing Enter? What listener would you implement
> to be notified as each character is typed into a text field?
> Note that you should not implement a general-purpose key listener,
> but a listener specific to text.  
> Answer 2: To be notified when the user
> presses Enter, you would register an
> `ActionListener` on the text field;
> the `actionPerformed` method is called when the user types
> Enter. Note that the Enter character is not part of
> the resulting string. To be notified as each character
> is typed, you would register a `DocumentListener`
> on the text field's
> `Document`. The `insertUpdate` method
> is then called as each
> character is typed. Note that this is not the correct way
> to implement input validation. For that behavior you should
> check out the
> [Input Verification API](../misc/focus.html#inputverificationapi)
> section in
> [How to Use the Focus Subsystem](../misc/focus.html).
>
> Question 3: What listener would
> you implement to be notified when a spinner’s value has
> changed? How would you get the spinner’s new value?  
> Answer 3: To be notified when the value
> has changed, you would register a
> `ChangeListener` on the spinner. You would get
> the new value through the
> event's source in the `stateChanged` method.
> The following code snippet shows how this could be done:
>
> ```
>
> public void stateChanged(ChangeEvent e) {
>     JSpinner mySpinner = (JSpinner)(e.getSource());
>     SpinnerNumberModel model = (SpinnerNumberModel)(mySpinner.getModel());
>     Number currentValue = model.getNumber();
>     ...
> }
>
> ```
>
> Question 4: The default behavior
> for the focus subsystem is to
> consume the focus traversal keys, such as Tab and Shift Tab.
> Say you want to prevent this behavior in one of your application’s
> components. How would you accomplish this?  
> Answer 4:
> You call `setFocusTraversalKeysEnabled(false)` on that particular
> component. Note that you must then handle focus traversal manually.
> See
> [How to Write a Key Listener](../events/keylistener.html)
> and
> [How to Use the Focus Subsystem](../misc/focus.html)
> for more information.

### Exercises

> Exercise 1. Take the
> [`Beeper.java`](../examples/events/BeeperProject/src/events/Beeper.java)[![(in a .java source file)](../../images/sourceIcon.gif)](../examples/events/BeeperProject/src/events/Beeper.java)
> example and add a text field. Implement it so that when
> the user has finishing entering data, the system beeps.  
> Answer 1: See
> [`Beeper1.java`](../examples/QandE/Beeper1Project/src/QandE/Beeper1.java)[![(in a .java source file)](../../images/sourceIcon.gif)](../examples/QandE/Beeper1Project/src/QandE/Beeper1.java)
>
> Exercise 2. Take the
> [`Beeper.java`](../examples/events/BeeperProject/src/events/Beeper.java)[![(in a .java source file)](../../images/sourceIcon.gif)](../examples/events/BeeperProject/src/events/Beeper.java)
> example and add a selectable component that allows the
> user to enter a number from 1 to 10. For example, you can use
> a combo box, a set of radio buttons, or a spinner. Implement
> it so that when the user has selected the number, the system
> beeps that many times.  
> Answer 2: See
> [`Beeper2.java`](../examples/QandE/Beeper2Project/src/QandE/Beeper2.java)[![(in a .java source file)](../../images/sourceIcon.gif)](../examples/QandE/Beeper2Project/src/QandE/Beeper2.java)

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

**Previous page:** Questions and Exercises: Writing Event Listeners




A browser with JavaScript enabled is required for this page to operate properly.