[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Creating a GUI With JFC/Swing
  
**Lesson:** Concurrency in Swing

[Concurrency in Swing](index.html)

[Initial Threads](initial.html)

[The Event Dispatch Thread](dispatch.html)

Worker Threads and SwingWorker

[Simple Background Tasks](simple.html)

[Tasks that Have Interim Results](interim.html)

[Canceling Background Tasks](cancel.html)

[Bound Properties and Status Methods](bound.html)

[Home Page](../../index.html)
>
[Creating a GUI With JFC/Swing](../index.html)
>
[Concurrency in Swing](index.html)

[« Previous](dispatch.html) • [Trail](../TOC.html) • [Next »](simple.html)

# Worker Threads and SwingWorker

When a Swing program needs to execute a long-running task, it usually
uses one of the *worker threads*, also known as the *background
threads*. Each task running on a worker thread is
represented by an instance of
[`javax.swing.SwingWorker`](http://download.oracle.com/javase/7/docs/api/javax/swing/SwingWorker.html). `SwingWorker` itself is an abstract class; you must
define a subclass in order to create a `SwingWorker`
object; anonymous inner classes are often useful for creating very
simple `SwingWorker` objects.

`SwingWorker` provides a number of
communication and control features:

* The `SwingWorker` subclass can define a method,
  `done`, which is automatically invoked on the event
  dispatch thread when the background task is finished.* `SwingWorker` implements
    [`java.util.concurrent.Future`](http://download.oracle.com/javase/7/docs/api/java/util/concurrent/Future.html).
    This interface allows the background task to provide a return
    value to the other thread. Other methods in this interface allow
    cancellation of the background task and discovering whether the
    background task has finished or been cancelled.* The background task can provide intermediate results by
      invoking `SwingWorker.publish`, causing
      `SwingWorker.process` to be invoked from the event
      dispatch thread.* The background task can define bound properties. Changes
        to these properties trigger events, causing event-handling methods
        to be invoked on the event dispatch thread.

These features are discussed in the following subsections.

---

**Note:** The `javax.swing.SwingWorker` class was added to the Java
platform in Java SE 6. Prior to this, another class, also called
`SwingWorker`, was widely used for some of the same
purposes. The old `SwingWorker` was not part of the Java
platform specification, and was not provided as part of the JDK.

The new `javax.swing.SwingWorker` is a completely new
class. Its functionality is not a strict superset
of the old `SwingWorker`. Methods in the two classes that
have the same function do not have the same names. Also, instances of
the old `SwingWorker` class were reusable, while a new instance
of `javax.swing.SwingWorker` is needed for each new
background task.

Throughout the Java Tutorials, any mention of `SwingWorker`
now refers to `javax.swing.SwingWorker`.

---

[« Previous](dispatch.html)
•
[Trail](../TOC.html)
•
[Next »](simple.html)

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

**Previous page:** The Event Dispatch Thread
  
**Next page:** Simple Background Tasks




A browser with JavaScript enabled is required for this page to operate properly.