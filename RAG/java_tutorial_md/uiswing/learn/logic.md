[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Creating a GUI With JFC/Swing
  
**Lesson:** Learning Swing with the NetBeans IDE

[Learning Swing with the NetBeans IDE](index.html)

[Setting up the CelsiusConverter Project](settingup.html)

[NetBeans IDE Basics](netbeansbasics.html)

[Creating the CelsiusConverter GUI](creatinggui.html)

[Adjusting the CelsiusConverter GUI](adjustinggui.html)

Adding the Application Logic

[Home Page](../../index.html)
>
[Creating a GUI With JFC/Swing](../index.html)
>
[Learning Swing with the NetBeans IDE](index.html)

[« Previous](adjustinggui.html) • [Trail](../TOC.html) • [Next »](../QandE/questions-learn.html)

# Adding the Application Logic

It is now time to
add in the application logic.

### Step 1: Change the Default Variable Names

The figure below shows the default variable names as they
currently appear within the Inspector. For each component, the variable name appears first,
followed by the object's type in square brackets. For example, `jTextField1 [JTextField]`
means that "jTextField1" is the variable name
and "JTextField" is its type.

![Default Variable Names](../../figures/uiswing/learn/nb-swing-20.png)

Default Variable Names

The default names are not very relevant in the context of this application, so it makes
sense to change them from their defaults to something that is more meaningful. Right-click each
variable name and choose "Change variable name." When you are finished, the variable names
should appear as follows:

![New Variable Names ](../../figures/uiswing/learn/nb-swing-21.png)

New Variable Names

The new variable names are "tempTextField", "celsiusLabel", "convertButton", and "fahrenheitLabel."
Each change that you make in the Inspector will automatically
propagate its way back into the source code. You can rest assured that compilation
will not fail due to typos or mistakes of that nature — mistakes that are common
when editing by hand.

### Step 2: Register the Event Listeners

When an end-user interacts with a Swing GUI component
(such as clicking the Convert button), that component will generate a special kind of object —
called an *event
object* — which it will then broadcast to any other objects that have previously registered themselves as
*listeners* for that event.
The NetBeans IDE makes event listener registration extremely simple:

[![using the NetBeans GUI to connect the actionPerformed method to the object](../../figures/uiswing/learn/nb-swing-22.png)](../../figures/uiswing/learn/nb-swing-22.png)  
*This figure has been reduced to fit on the page.   
 Click the image to view it at its natural size.*

In the Design Area, click on the Convert button to select it. Make sure that
*only* the Convert button is selected (if the JFrame itself is also selected, this step will not work.)
Right-click the Convert button and choose Events -> Action -> ActionPerformed. This will generate the
required event-handling code, leaving you with empty method bodies in which to add your
own functionality:

[![the actionPerformed method in the source code tab](../../figures/uiswing/learn/nb-swing-23.png)](../../figures/uiswing/learn/nb-swing-23.png)  
*This figure has been reduced to fit on the page.   
 Click the image to view it at its natural size.*

There are many different event types representing
the various kinds of actions that an end-user can take (clicking the mouse triggers one type of event, typing
at the keyboard triggers another, moving the mouse yet another, and so on.)
Our application is only concerned with the ActionEvent; for more information about event handling, see
[Writing Event Listeners](../events/index.html).

### Step 3: Add the Temperature Conversion Code

The final step is to simply paste the temperature conversion code into the
empty method body.
The following code is all that is necessary to
convert a temperature from Celsius to Fahrenheit:

---

**Note:** This example is not localizable because the `parseDouble`
method is not localizable. This code snippet is for illustration purposes only.
A more robust implementation would use the
[Scanner](http://download.oracle.com/javase/7/docs/api/java/util/Scanner.html) class to parse the user input.

---

```

    //Parse degrees Celsius as a double and convert to Fahrenheit.
    int tempFahr = (int)((Double.parseDouble(tempTextField.getText()))
            * 1.8 + 32);
    fahrenheitLabel.setText(tempFahr + " Fahrenheit");

```

Simply copy this code and paste it into the convertButtonActionPerformed method
as shown below:

[![](../../figures/uiswing/learn/nb-swing-24.png)](../../figures/uiswing/learn/nb-swing-24.png)  
*This figure has been reduced to fit on the page.   
 Click the image to view it at its natural size.*

With the conversion code in place, the application is now complete.

### Step 4: Run the Application

Running the application is simply a matter of choosing Run -> Run Main Project
within the NetBeans IDE. The
first time you run this application, you will be prompted with a dialog asking to set
`CelsiusConverterGUI` as the main class for this project. Click the OK button,
and when the program finishes compiling, you should see the application running in
its own window.

Congratulations! You have completed your first Swing application!

[« Previous](adjustinggui.html)
•
[Trail](../TOC.html)
•
[Next »](../QandE/questions-learn.html)

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

**Previous page:** Adjusting the CelsiusConverter GUI
  
**Next page:** Questions and Exercises: Learning Swing with the NetBeans IDE




A browser with JavaScript enabled is required for this page to operate properly.