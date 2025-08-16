[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Creating a GUI With JFC/Swing
  
**Lesson:** Concurrency in Swing
  
**Section:** Worker Threads and SwingWorker

[Concurrency in Swing](index.html)

[Initial Threads](initial.html)

[The Event Dispatch Thread](dispatch.html)

[Worker Threads and SwingWorker](worker.html)

[Simple Background Tasks](simple.html)

[Tasks that Have Interim Results](interim.html)

[Canceling Background Tasks](cancel.html)

Bound Properties and Status Methods

[Home Page](../../index.html)
>
[Creating a GUI With JFC/Swing](../index.html)
>
[Concurrency in Swing](index.html)

[« Previous](cancel.html) • [Trail](../TOC.html) • [Next »](../QandE/questions-concurrency.html)

# Bound Properties and Status Methods

`SwingWorker` supports
[bound properties](../../javabeans/properties/bound.html), which are useful for communicating with other threads. Two bound
properties are predefined: `progress` and
`state`. As with all bound properties,
`progress` and `state` can be used to trigger
event-handling tasks on the event dispatch thread.

By implementing a property change listener, a program can track
changes to `progress`, `state`, and other bound
properties. For more information, refer to
[How to Write a Property Change Listener](../events/propertychangelistener.html)
in
[Writing Event Listeners](../events/index.html).

### The `progress` Bound Variable

The `progress` bound variable is an `int` value
that can range from 0 to 100. It has a predefined setter method (the protected
[`SwingWorker.setProgress`](http://download.oracle.com/javase/7/docs/api/javax/swing/SwingWorker.html#setProgress()))
and a predefined getter method (the public
[`SwingWorker.getProgress`](http://download.oracle.com/javase/7/docs/api/javax/swing/SwingWorker.html#getProgress(int))).

The
[`ProgressBarDemo`](../examples/components/ProgressBarDemoProject/src/components/ProgressBarDemo.java)
example uses `progress` to update a
`ProgressBar` control from a background task. For a
detailed discussion of this example, refer to
[How to Use Progress Bars](../components/progress.html)
in
[Using Swing Components](../components/index.html).

### The `state` Bound Variable

The `state` bound variable indicates where the
`SwingWorker` object is in its lifecycle.
The bound variable contains an enumeration value of type
`SwingWorker.StateValue`. Possible values are:

`PENDING`: The state during the period from the construction of the object until just before `doInBackground` is invoked. `STARTED`: The state during the period from shortly before `doInBackground` is invoked until shortly before `done` is invoked. DONE: The state for the remainder of the existence of the object.

The current value of the `state` bound variable is returned by
[`SwingWorker.getState`](http://download.oracle.com/javase/7/docs/api/javax/swing/SwingWorker.html#getState()).

### Status Methods

Two methods, part of the `Future` interface, also report on
the status of the background task. As we saw in
[Canceling Background Tasks](cancel.html), `isCancelled` returns `true` if the task has been
canceled. In addition, `isDone` returns `true` if
the task has finished, either normally, or by being cancelled.

[« Previous](cancel.html)
•
[Trail](../TOC.html)
•
[Next »](../QandE/questions-concurrency.html)

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

**Previous page:** Canceling Background Tasks
  
**Next page:** Questions and Exercises: Concurrency in Swing




A browser with JavaScript enabled is required for this page to operate properly.