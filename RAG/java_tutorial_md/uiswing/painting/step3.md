[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Creating a GUI With JFC/Swing
  
**Lesson:** Performing Custom Painting

[Performing Custom Painting](index.html)

[Creating the Demo Application (Step 1)](step1.html)

[Creating the Demo Application (Step 2)](step2.html)

Creating the Demo Application (Step 3)

[Refining the Design](refining.html)

[A Closer Look at the Paint Mechanism](closer.html)

[Summary](summary.html)

[Solving Common Painting Problems](problems.html)

[Home Page](../../index.html)
>
[Creating a GUI With JFC/Swing](../index.html)
>
[Performing Custom Painting](index.html)

[« Previous](step2.html) • [Trail](../TOC.html) • [Next »](refining.html)

# Creating the Demo Application (Step 3)

Finally, we will add the event-handling code to programatically
repaint the component whenever the user clicks or drags the mouse. To
keep our custom painting as efficient as possible, we will track the mouse
coordinates and repaint only the areas of the screen that have changed.
This is a recommended best practice that will keep your application running as
efficiently as possible.

![The completed application, showing a red square with black border](../../figures/uiswing/painting/swing3.png)

The Completed Application

Figure 3: The Completed Application

Click the Launch button to run SwingPaintDemo3 using
[Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp) ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
Alternatively, to compile and run the example yourself, consult the
[example index](../examples/painting/index.html#SwingPaintDemo3).
 [![Launches the SwingPaintDemo3 example](../../images/jws-launch-button.png )](http://download.oracle.com/javase/tutorialJWS/uiswing/painting/ex6/SwingPaintDemo3.jnlp)

```

package painting;

import javax.swing.SwingUtilities;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.BorderFactory;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics; 
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseMotionListener;
import java.awt.event.MouseMotionAdapter; 

public class SwingPaintDemo3 {
    
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
        f.add(new MyPanel());
        f.pack();
        f.setVisible(true);
    } 
}

class MyPanel extends JPanel {

    private int squareX = 50;
    private int squareY = 50;
    private int squareW = 20;
    private int squareH = 20;

    public MyPanel() {

        setBorder(BorderFactory.createLineBorder(Color.black));
        
        addMouseListener(new MouseAdapter() {
            public void mousePressed(MouseEvent e) {
                moveSquare(e.getX(),e.getY());
            }
        });

        addMouseMotionListener(new MouseAdapter() {
            public void mouseDragged(MouseEvent e) {
                moveSquare(e.getX(),e.getY());
            }
        });
        
    }
    
    private void moveSquare(int x, int y) {
        int OFFSET = 1;
        if ((squareX!=x) || (squareY!=y)) {
            repaint(squareX,squareY,squareW+OFFSET,squareH+OFFSET);
            squareX=x;
            squareY=y;
            repaint(squareX,squareY,squareW+OFFSET,squareH+OFFSET);
        } 
    }
    

    public Dimension getPreferredSize() {
        return new Dimension(250,200);
    }
    
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);       
        g.drawString("This is my custom Panel!",10,20);
        g.setColor(Color.RED);
        g.fillRect(squareX,squareY,squareW,squareH);
        g.setColor(Color.BLACK);
        g.drawRect(squareX,squareY,squareW,squareH);
    }  
}

```

This change first imports the various mouse classes
from the `java.awt.event` package, making the application
capable of responding to the user's mouse activity.
The constructor has been updated to register
event listeners for
mouse presses and drags. Whenever a `MouseEvent` received, it
is forwarded to the `moveSquare` method, which updates
the square's coordinates and repaints the component in an intelligent manner.
Note that by default, any code that is placed within these event handlers will be
executed on the Event Dispatch Thread.

But the most important change is the invocation of the `repaint` method. This method is defined by `java.awt.Component` and is the
mechanism that allows you to programatically repaint the surface of any
given component.
It has a no-arg version (which repaints the entire component) and a multi-arg version (which repaints only the specified area.) This area
is also known as the *clip*.
Invoking the multi-arg version
of `repaint` takes a little extra effort,
but guarantees that your painting code will not waste cycles repainting areas of the screen that have not changed.

Because we are manually setting the clip, our `moveSquare` method invokes the repaint method not once, but twice. The first invocation tells Swing to repaint the area of the component where the square *previously* was (the inherited behavior uses the UI Delegate to fill that area with the current background color.) The second invocation paints the area of the component where the square *currently* is. An important point worth noting is that although we have invoked repaint twice in a row in the same event handler, Swing is smart enough to take that information and repaint those sections of the screen all in one single paint operation. In other words, Swing will not repaint the component twice in a row, even if that is what the code appears to be doing.

Exercises:

1. Comment out the first invocation of repaint and note what happens when you click or drag the mouse. Because that line is responsible for filling in the background, you should notice that all squares remain on screen after they are painted.

   - With multiple squares on screen, minimize and restore the application frame. What happens? You should notice that the act of maximizing the screen causes the system to entirely repaint the components surface, which will erase all squares except the current one.

     - Comment out both invocations of repaint, and add a line at the end of the paintComponent method to invoke the zero-arg version of repaint instead. The application will appear to be restored to its original behavior, but painting will now be less efficient since the entire surface area of the component is now being painted. You may notice slower performace, especially if the application is maximized.

[« Previous](step2.html)
•
[Trail](../TOC.html)
•
[Next »](refining.html)

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

**Previous page:** Creating the Demo Application (Step 2)
  
**Next page:** Refining the Design




A browser with JavaScript enabled is required for this page to operate properly.