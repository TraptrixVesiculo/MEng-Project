[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Creating a GUI With JFC/Swing
  
**Lesson:** Learning Swing with the NetBeans IDE

[Learning Swing with the NetBeans IDE](index.html)

Setting up the CelsiusConverter Project

[NetBeans IDE Basics](netbeansbasics.html)

[Creating the CelsiusConverter GUI](creatinggui.html)

[Adjusting the CelsiusConverter GUI](adjustinggui.html)

[Adding the Application Logic](logic.html)

[Home Page](../../index.html)
>
[Creating a GUI With JFC/Swing](../index.html)
>
[Learning Swing with the NetBeans IDE](index.html)

[« Previous](index.html) • [Trail](../TOC.html) • [Next »](netbeansbasics.html)

# Setting up the CelsiusConverter Project

If you have worked with the NetBeans IDE in the past,
much of this section will look familiar, since
the initial steps are similar for most projects.
Still, the following steps describe settings that are specific to
this application, so take care to follow them closely.

### Step 1: Create a New Project

To create a new project, launch the NetBeans IDE and
choose New Project from the File menu:

![Creating a New Project within the GUI](../../figures/uiswing/learn/nb-swing-2-thumb.png)

Creating a New Project

Keyboard shortcuts for each
command appear on the far right of each menu item. The look and feel
of the NetBeans IDE may vary across platforms, but the functionality will
remain the same.

### Step 2: Choose General -> Java Application

Next, select General from the Categories column, and Java Application
from the Projects column:

[![screen shot from NetBeans application](../../figures/uiswing/learn/nb-swing-3.png)](../../figures/uiswing/learn/nb-swing-3.png)  
*This figure has been reduced to fit on the page.   
 Click the image to view it at its natural size.*

You may notice mention of "J2SE" in the description pane;
that is the old name
for what is now known as the "Java SE" platform.
Press the button labeled "Next" to proceed.

### Step 3: Set a Project Name

Now enter "CelsiusConverterProject" as the project name. You can leave the
Project Location and Project Folder fields set to their default values, or click the Browse button to
choose an alternate location on your system.

[![screen shot from NetBeans](../../figures/uiswing/learn/nb-swing-4.png)](../../figures/uiswing/learn/nb-swing-4.png)  
*This figure has been reduced to fit on the page.   
 Click the image to view it at its natural size.*

Make sure to deselect the "Create Main Class" checkbox; leaving this option selected
generates a new class as the main entry point for the application, but our main GUI
window (created in the next step) will serve that purpose, so checking this box
is not necessary.
Click the "Finish" button when you are done.

[![screen shot from NetBeans](../../figures/uiswing/learn/nb-swing-5.png)](../../figures/uiswing/learn/nb-swing-5.png)  
*This figure has been reduced to fit on the page.   
 Click the image to view it at its natural size.*

When the IDE finishes loading, you will see a screen similar to the above. All panes will be empty
except for the Projects pane in the upper left hand corner, which shows the
newly created project.

### Step 4: Add a JFrame Form

[![screen shot from NetBeans](../../figures/uiswing/learn/nb-swing-6.png)](../../figures/uiswing/learn/nb-swing-6.png)  
*This figure has been reduced to fit on the page.   
 Click the image to view it at its natural size.*

Now right-click the CelsiusConverterProject name and
choose New -> JFrame Form (`JFrame` is the Swing
class responsible for the main frame for your application.) You will learn how to designate
this class as the application's entry point later in this lesson.

### Step 5: Name the GUI Class

Next, type `CelsiusConverterGUI` as the class name, and
`learn` as the package name. You can actually name this package anything you want,
but here we are following the tutorial convention of naming the package after
the lesson in which is resides.

[![Screen shot from NetBeans](../../figures/uiswing/learn/nb-swing-7.png)](../../figures/uiswing/learn/nb-swing-7.png)  
*This figure has been reduced to fit on the page.   
 Click the image to view it at its natural size.*

The remainder of the fields
should automatically be filled in, as shown above.
Click the Finish button when you are done.

[![Screen shot from NetBeans](../../figures/uiswing/learn/nb-swing-8.png)](../../figures/uiswing/learn/nb-swing-8.png)  
*This figure has been reduced to fit on the page.   
 Click the image to view it at its natural size.*

When the IDE finishes loading, the right pane will display a
design-time, graphical view of the `CelsiusConverterGUI`.
It is on this screen that you will visually drag, drop, and manipulate
the various Swing components.

[« Previous](index.html)
•
[Trail](../TOC.html)
•
[Next »](netbeansbasics.html)

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

**Previous page:** Learning Swing with the NetBeans IDE
  
**Next page:** NetBeans IDE Basics




A browser with JavaScript enabled is required for this page to operate properly.