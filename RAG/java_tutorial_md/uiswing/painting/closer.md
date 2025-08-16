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

[Creating the Demo Application (Step 3)](step3.html)

[Refining the Design](refining.html)

A Closer Look at the Paint Mechanism

[Summary](summary.html)

[Solving Common Painting Problems](problems.html)

[Home Page](../../index.html)
>
[Creating a GUI With JFC/Swing](../index.html)
>
[Performing Custom Painting](index.html)

[« Previous](refining.html) • [Trail](../TOC.html) • [Next »](summary.html)

# A Closer Look at the Paint Mechanism

By now you know that the `paintComponent` method is where all of your
painting code should be placed.
It is true that this method will be
invoked when it is time to paint, but
painting actually begins higher up the class heirarchy, with the `paint` method (defined by `java.awt.Component`.)
This method will be executed by the painting subsystem whenever you
component needs to be rendered. Its signature is:

* `public void paint(Graphics g)`

`javax.swing.JComponent` extends this class
and further factors the `paint` method into three separate methods,
which are invoked in the following
order:

* `protected void paintComponent(Graphics g)`* `protected void paintBorder(Graphics g)`* `protected void paintChildren(Graphics g)`

The API does nothing to prevent your code from overriding `paintBorder`
and `paintChildren`, but generally speaking, there is no reason for you to do so. For all practical purposes `paintComponent` will be the
only method that you will ever need to override.

As previously mentioned, most of the standard Swing components have their look and feel
implemented by separate UI Delegates. This means that
most (or all) of the painting for the standard Swing components
proceeds as follows.

1. `paint()` invokes `paintComponent()`.- If the `ui` property is non-null, `paintComponent()` invokes `ui.update()`.- If the component's `opaque` property is true, `ui.udpate()` fills the component's background with the background color and invokes `ui.paint()`.- `ui.paint()` renders the content of the component.

This is why our `SwingPaintDemo` code invokes `super.paintComponent(g)`. We could add
an additional comment to make this more clear:

```

public void paintComponent(Graphics g) {
        // Let UI Delegate paint first, which 
        // includes background filling since 
        // this component is opaque.

        super.paintComponent(g);       
        g.drawString("This is my custom Panel!",10,20);
        redSquare.paintSquare(g);
}  

```

If you have understood all of the demo code provided in this lesson,
congratulations! You have enough practical knowledge to write efficient
painting code in your own applications.
If however
you want a closer look "under the hood", please refer to the SDN article
linked to from the first page of this lesson.

[« Previous](refining.html)
•
[Trail](../TOC.html)
•
[Next »](summary.html)

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

**Previous page:** Refining the Design
  
**Next page:** Summary




A browser with JavaScript enabled is required for this page to operate properly.