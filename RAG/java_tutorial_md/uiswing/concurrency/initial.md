[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Creating a GUI With JFC/Swing
  
**Lesson:** Concurrency in Swing

[Concurrency in Swing](index.html)

Initial Threads

[The Event Dispatch Thread](dispatch.html)

[Worker Threads and SwingWorker](worker.html)

[Simple Background Tasks](simple.html)

[Tasks that Have Interim Results](interim.html)

[Canceling Background Tasks](cancel.html)

[Bound Properties and Status Methods](bound.html)

[Home Page](../../index.html)
>
[Creating a GUI With JFC/Swing](../index.html)
>
[Concurrency in Swing](index.html)

[« Previous](index.html) • [Trail](../TOC.html) • [Next »](dispatch.html)

# Initial Threads

Every program has a set of threads where the application logic begins.
In standard programs, there's only one such thread: the thread that
invokes the `main` method of the program class. In applets
the initial threads are the ones that construct the applet object and
invoke its `init` and `start` methods; these
actions may occur on a single thread, or on two or three different
threads, depending on the Java platform implementation. In this
lesson, we call these threads the *initial threads*.

In Swing programs, the initial threads don't have a lot to do. Their
most essential job is to create a `Runnable` object that
initializes the GUI and schedule that object for execution on the
event dispatch thread. Once the GUI is created, the program is
primarily driven by GUI events, each of which causes the execution of
a short task on the event dispatch thread. Application code can
schedule additionals tasks on the event dispatch thread (if they
complete quickly, so as not to interfere with event processing) or a
worker thread (for long-running tasks).

An initial thread schedules the GUI creation task by invoking
[`javax.swing.SwingUtilities.invokeLater`](http://download.oracle.com/javase/7/docs/api/javax/swing/SwingUtilities.html#invokeLater(java.lang.Runnable))
or
[`javax.swing.SwingUtilities.invokeAndWait`](http://download.oracle.com/javase/7/docs/api/javax/swing/SwingUtilities.html#invokeAndWait(java.lang.Runnable))
. Both of these methods take a single argument: the
`Runnable` that defines the new task. Their only difference
is indicated by their names: `invokeLater` simply schedules
the task and returns; `invokeAndWait` waits for the task to
finish before returning.

You can see examples of this throughout the Swing tutorial:

```

SwingUtilities.invokeLater(new Runnable() {
    public void run() {
        createAndShowGUI();
    }
});

```

In an applet, the GUI-creation task must be launched from the
`init` method using `invokeAndWait`; otherwise,
`init` may return before the GUI is created, which may
cause problems for a web browser launching an applet. In any other
kind of program, scheduling the GUI-creation task is usually the last
thing the initial thread does, so it doesn't matter whether it
uses `invokeLater` or `invokeAndWait`.

Why does not the initial thread simply create the GUI itself? Because
almost all code that creates or interacts with Swing components must
run on the event dispatch thread. This restriction is discussed
further in the next section.

[« Previous](index.html)
•
[Trail](../TOC.html)
•
[Next »](dispatch.html)

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

**Previous page:** Concurrency in Swing
  
**Next page:** The Event Dispatch Thread




A browser with JavaScript enabled is required for this page to operate properly.