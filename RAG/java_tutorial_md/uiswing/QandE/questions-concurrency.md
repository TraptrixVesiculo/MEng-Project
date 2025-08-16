[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Creating a GUI With JFC/Swing

[Home Page](../../index.html)
>
[Creating a GUI With JFC/Swing](../index.html)

[« Previous](../TOC.html) • [Trail](../TOC.html) • [Next »](../misc/index.html)

# Questions and Exercises: Concurrency in Swing

### Questions

1. For each of the following tasks, specify which thread it should be
   executed in and why.
   * Initializing the GUI.* Loading a large file.* Invoking
         [`javax.swing.JComponent.setFont`](http://download.oracle.com/javase/7/docs/api/javax/swing/JComponent.html#setFont(java.awt.Font)) to change the font of a component.* Invoking
           [`javax.swing.text.JTextComponent.setText`](http://download.oracle.com/javase/7/docs/api/javax/swing/text/JTextComponent.html#setText(java.lang.String)) to change the text of a component.- One set of threads is not used for any of the
     tasks mentioned in the previous question. Name this thread and
     explain why its applications are so limited.- `SwingWorker` has two type parameters. Explain how
       these type parameters are used, and why it often doesn't matter what
       they are.

### Exercises

1. Modify the
   [`Flipper`](../examples/concurrency/FlipperProject/src/concurrency/Flipper.java) example so that it pauses 5 seconds between "coin flips." If the
   user clicks the "Cancel", the coin-flipping loop terminates
   immediately.

[Check your answers.](answers-concurrency.html)

[« Previous](../TOC.html)
•
[Trail](../TOC.html)
•
[Next »](../misc/index.html)

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

**Previous page:** Bound Properties and Status Methods
  
**Next page:** Using Other Swing Features




A browser with JavaScript enabled is required for this page to operate properly.