[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

Concurrency in Swing

[Initial Threads](initial.html)

[The Event Dispatch Thread](dispatch.html)

[Worker Threads and SwingWorker](worker.html)

[Simple Background Tasks](simple.html)

[Tasks that Have Interim Results](interim.html)

[Canceling Background Tasks](cancel.html)

[Bound Properties and Status Methods](bound.html)

**Trail:** Creating a GUI With JFC/Swing

[Home Page](../../index.html)
>
[Creating a GUI With JFC/Swing](../index.html)

[« Previous](../components/index.html) • [Trail](../TOC.html) • [Next »](initial.html)

# Lesson: Concurrency in Swing

[Examples Index](../examples/concurrency/index.html)

This lesson discusses concurrency as it applies to Swing programming.
It assumes that you are already familiar with the content of the
[Concurrency](../../essential/concurrency/index.html)
lesson in the
[Essential Classes](../../essential/index.html)
trail.

Careful use of concurrency is particularly important to the Swing
programmer. A well-written Swing program uses concurrency to create a
user interface that never "freezes" — the program is always
responsive to user interaction, no matter what it's doing. To create a
responsive program, the programmer must learn how the Swing framework
employs threads.

A Swing programmer deals with the following kinds of threads:

* *Initial threads*, the threads that execute initial
  application code.* The *event dispatch thread*, where all event-handling
    code is executed. Most code that interacts with the Swing
    framework must also execute on this thread.* *Worker threads*, also known as *background
      threads*, where time-consuming background tasks are
      executed.

The programmer does not need to provide code that explicitly creates
these threads: they are provided by the runtime or the Swing
framework. The programmer's job is to utilize these threads to create
a responsive, maintainable Swing program.

Like any other program running on the Java platform, a Swing program
can create additional threads and thread pools, using the tools
described in the Concurrency lesson. But for basic Swing
programs the threads described here are sufficient.

This lesson discusses each of the three kinds of threads in turn.
Worker threads require the most discussion because tasks that run
on them are created using `javax.swing.SwingWorker`.
This class has many useful features, including communication and
coordination between worker thread tasks and the tasks on other
threads.

[« Previous](../components/index.html)
•
[Trail](../TOC.html)
•
[Next »](initial.html)

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
  
**Next page:** Initial Threads




A browser with JavaScript enabled is required for this page to operate properly.