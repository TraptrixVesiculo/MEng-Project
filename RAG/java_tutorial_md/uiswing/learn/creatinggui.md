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

Creating the CelsiusConverter GUI

[Adjusting the CelsiusConverter GUI](adjustinggui.html)

[Adding the Application Logic](logic.html)

[Home Page](../../index.html)
>
[Creating a GUI With JFC/Swing](../index.html)
>
[Learning Swing with the NetBeans IDE](index.html)

[« Previous](netbeansbasics.html) • [Trail](../TOC.html) • [Next »](adjustinggui.html)

# Creating the CelsiusConverter GUI

This section explains how to use the NetBeans IDE to create the application's GUI.
As you drag each component from the Palette to the Design Area,
the IDE auto-generates the appropriate source code.

### Step 1: Set the Title

First, set the title of the application's `JFrame` to "Celsius Converter", by
single-clicking the `JFrame` in the Inspector:

![Selecting the JFrame](../../figures/uiswing/learn/nb-swing-8a.png)

Selecting the JFrame

Then, set its title with the Property Editor:

![Setting the Title](../../figures/uiswing/learn/nb-swing-8b.png)

Setting the Title

You can set the title by either double-clicking the title property
and entering the new text directly, or by clicking the
![](../../figures/uiswing/learn/nb-swing-11b.png)
button and entering the
title in the provided field. Or, as a shortcut, you could single-click the
`JFrame` of the inspector and enter its new text directly without
using the property editor.

### Step 2: Add a JTextField

Next, drag a `JTextField` from
the Palette to the upper left corner of the Design Area. As you approach
the upper left corner, the GUI builder provides
visual cues (dashed lines) that suggest the appropriate spacing. Using
these cues as a guide, drop a `JTextField` into the upper left hand
corner of the window as shown below:

![Adding a JTextField](../../figures/uiswing/learn/nb-swing-12.png)

Adding a JTextField

You may be tempted to erase the default text "JTextField1", but just
leave it in place for now. We will replace it later in this lesson as we make the
final adjustments to each component.
For more information about this component, see
[How to Use Text Fields](../components/textfield.html).

### Step 3: Add a JLabel

Next, drag a `JLabel` onto the Design Area. Place it to the right of the
`JTextField`, again watching for visual cues that suggest
an appropriate amount of spacing. Make sure that text base for this component
is aligned with that of the `JTextField`.
The visual cues provided by the IDE should make this easy to determine.

![Adding a JLabel](../../figures/uiswing/learn/nb-swing-13.png)

Adding a JLabel

For more information about this component, see
[How to Use Labels](../components/label.html).

### Step 4: Add a JButton

Next, drag a `JButton` from the Palette and position it to the left and underneath the `JTextField`.
Again, the visual cues help guide it into place.

![Adding a JButton](../../figures/uiswing/learn/nb-swing-14.png)

Adding a JButton

You may be tempted to manually adjust the width of the `JButton`
and `JTextField`, but just leave them as they are for now. You will learn
how to correctly adjust these components later in this lesson.
For more information about this component, see
[How to Use Buttons](../components/button.html).

### Step 5: Add a Second JLabel

![Adding a Second JLabel](../../figures/uiswing/learn/nb-swing-15.png)

Adding a Second JLabel

Finally, add a second `JLabel`, repeating the process in step 2. Place this
second label to the right of the `JButton`, as shown above.

[« Previous](netbeansbasics.html)
•
[Trail](../TOC.html)
•
[Next »](adjustinggui.html)

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

**Previous page:** NetBeans IDE Basics
  
**Next page:** Adjusting the CelsiusConverter GUI




A browser with JavaScript enabled is required for this page to operate properly.