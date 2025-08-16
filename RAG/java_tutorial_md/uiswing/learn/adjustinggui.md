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

Adjusting the CelsiusConverter GUI

[Adding the Application Logic](logic.html)

[Home Page](../../index.html)
>
[Creating a GUI With JFC/Swing](../index.html)
>
[Learning Swing with the NetBeans IDE](index.html)

[« Previous](creatinggui.html) • [Trail](../TOC.html) • [Next »](logic.html)

# Adjusting the CelsiusConverter GUI

With the GUI components now in place, it is time to make the final adjustments.
There are a few different ways to do this; the order suggested
here is just one possible approach.

### Step 1: Set the Component Text

First, double-click the `JTextField` and `JButton` to change
the default text that was inserted by the IDE. When you erase the text from the
`JTextField`, it will shrink in size as shown below. Change the text of
the `JButton` from "JButton1" to "Convert." Also change the top
`JLabel` text to "Celsius" and the bottom to "Fahrenheit."

![Setting the Component Text](../../figures/uiswing/learn/nb-swing-16.png)

Setting the Component Text



### Step 2: Set the Component Size

Next, shift-click the `JTextField` and `JButton` components. This will
highlight each showing that they are selected. Right-click
(control-click for mac users) Same Size -> Same Width. The
components will now be the same width, as shown below. When you
perform this step, make sure that `JFrame` itself is not also selected. If it is, the Same Size menu will not be active.

![Setting the JTextField and JButton Sizes](../../figures/uiswing/learn/nb-swing-17.png)

Setting the JTextField and JButton Sizes

### Step 3: Remove Extra Space

Finally, grab the lower right-hand corner of the `JFrame` and adjust its size to
eliminate any extra whitespace. Note that if you eliminate all of the extra space (as shown below)
the title (which only appears at runtime) may not show completely. The end-user is free to resize
the application as desired, but you may want to leave some extra space on the right side
to make sure that everything fits correctly. Experiment, and use the screenshot of the finished GUI
as a guide.

![The Completed GUI](../../figures/uiswing/learn/nb-swing-18.png)

The Completed GUI

  
The GUI portion of this application is now complete! If the NetBeans IDE has done its job,
you should feel that creating this GUI was a simple, if not trivial, task. But take a minute
to click on the source tab; you might be surprised at the amount of
code that has been generated.

[![the contents of the NetBeans source tab for the simple GUI example](../../figures/uiswing/learn/nb-swing-19.png)](../../figures/uiswing/learn/nb-swing-19.png)  
*This figure has been reduced to fit on the page.   
 Click the image to view it at its natural size.*

To see the code in its
entirety, scroll up and down within the IDE as necessary. You can expand or collapse certain
blocks
of code (such as method bodies) by clicking the + or - symbol on the left-hand side of the source editor.

[« Previous](creatinggui.html)
•
[Trail](../TOC.html)
•
[Next »](logic.html)

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

**Previous page:** Creating the CelsiusConverter GUI
  
**Next page:** Adding the Application Logic




A browser with JavaScript enabled is required for this page to operate properly.