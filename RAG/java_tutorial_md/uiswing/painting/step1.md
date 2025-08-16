[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Creating a GUI With JFC/Swing
  
**Lesson:** Performing Custom Painting

[Performing Custom Painting](index.html)

Creating the Demo Application (Step 1)

[Creating the Demo Application (Step 2)](step2.html)

[Creating the Demo Application (Step 3)](step3.html)

[Refining the Design](refining.html)

[A Closer Look at the Paint Mechanism](closer.html)

[Summary](summary.html)

[Solving Common Painting Problems](problems.html)

[Home Page](../../index.html)
>
[Creating a GUI With JFC/Swing](../index.html)
>
[Performing Custom Painting](index.html)

[« Previous](index.html) • [Trail](../TOC.html) • [Next »](step2.html)

# Creating the Demo Application (Step 1)

All Graphical User Interfaces require some kind of main application frame in
which to display. In Swing, this is an instance
of `javax.swing.JFrame`. Therefore, our first step is to instantiate
this class and make sure that everything works as expected.
Note that when programming in Swing, your GUI creation code should be
placed on
the Event Dispatch Thread (EDT). This will prevent potential race conditions
that could lead to deadlock.
The following code listing shows how this is done.

![Figure of an empty JFrame with Swing Paint Demo as the title ](../../figures/uiswing/painting/swing1.png)

An Instance of javax.swing.JFrame

Click the Launch button to run SwingPaintDemo1 using
[Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp) ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
Alternatively, to compile and run the example yourself, consult the
[example index](../examples/painting/index.html#SwingPaintDemo1).
 [![Launches the SwingPaintDemo1 example](../../images/jws-launch-button.png )](http://download.oracle.com/javase/tutorialJWS/uiswing/painting/ex6/SwingPaintDemo1.jnlp)

```

package painting;

import javax.swing.SwingUtilities;
import javax.swing.JFrame;

public class SwingPaintDemo1 {
    
    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                createAndShowGUI();
            }
        });
    }
    
    private static void createAndShowGUI() {
        System.out.println("Created GUI on EDT? "+
                SwingUtilities.isEventDispatchThread());
        JFrame f = new JFrame("Swing Paint Demo");
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        f.setSize(250,250);
        f.setVisible(true);
    }
}

```

This creates the frame, sets its title, and makes everything visible.
We have used the `SwingUtilities` helper class to construct this GUI
on the Event Dispatch Thread.
Note that by default, a `JFrame` does not exit the application when the user clicks its "close" button. We provide this behavior
by invoking the `setDefaultCloseOperation` method, passing in the appropriate argument.
Also, we are explicity setting the
frame's size to 250 x 250 pixels. This step will not
be necessary once we start adding components to the frame.

Exercises:

1. Compile and run the application.- Test the minimize and maximize buttons.- Click the close button (the application should exit.)

[« Previous](index.html)
•
[Trail](../TOC.html)
•
[Next »](step2.html)

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

**Previous page:** Performing Custom Painting
  
**Next page:** Creating the Demo Application (Step 2)




A browser with JavaScript enabled is required for this page to operate properly.