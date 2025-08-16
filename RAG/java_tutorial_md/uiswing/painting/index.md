[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

Performing Custom Painting

[Creating the Demo Application (Step 1)](step1.html)

[Creating the Demo Application (Step 2)](step2.html)

[Creating the Demo Application (Step 3)](step3.html)

[Refining the Design](refining.html)

[A Closer Look at the Paint Mechanism](closer.html)

[Summary](summary.html)

[Solving Common Painting Problems](problems.html)

**Trail:** Creating a GUI With JFC/Swing

[Home Page](../../index.html)
>
[Creating a GUI With JFC/Swing](../index.html)

[« Previous](../events/index.html) • [Trail](../TOC.html) • [Next »](step1.html)

# Lesson: Performing Custom Painting

This lesson describes custom painting in Swing.
Many programs will get by just fine
without writing their own painting code; they will simply use the
standard GUI components that are already available in the Swing API. But if you need specific control
over how your graphics are drawn, then this lesson is for you.
We will explore custom painting by creating
a simple GUI application that draws a shape
in response to the user's mouse activity.
By intentionally
keeping its design simple, we can focus on the underlying
painting concepts, which in turn will relate to other GUI applications
that you develop in the future.

This lesson explains
each concept in steps as you construct the demo application.
It presents the code as soon as possible with a minimum amount
of background reading.
Custom painting in
Swing is similar to custom painting in AWT, but since we do not recommend
writing
your applications entirely with the AWT, its painting mechanism is not specifically
discussed here. You may find it useful to read this lesson
followed by the
in-depth discussion of
[Painting in AWT and Swing](http://java.sun.com/products/jfc/tsc/articles/painting/)
on the Sun Developer Network (SDN).

[« Previous](../events/index.html)
•
[Trail](../TOC.html)
•
[Next »](step1.html)

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

**Previous page:** Previous Lesson
  
**Next page:** Creating the Demo Application (Step 1)




A browser with JavaScript enabled is required for this page to operate properly.