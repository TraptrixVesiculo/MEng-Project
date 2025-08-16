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

Canceling Background Tasks

[Bound Properties and Status Methods](bound.html)

[Home Page](../../index.html)
>
[Creating a GUI With JFC/Swing](../index.html)
>
[Concurrency in Swing](index.html)

[« Previous](interim.html) • [Trail](../TOC.html) • [Next »](bound.html)

# Canceling Background Tasks

To cancel a running background task, invoke
[`SwingWorker.cancel`](http://download.oracle.com/javase/7/docs/api/javax/swing/SwingWorker.html#cancel(boolean))
The task must cooperate with its own cancellation. There are two ways
it can do this:

* By terminating when it receives an interrupt. This procedures
  is described in
  [Interrupts](../../essential/concurrency/interrupt.html)
  in
  [Concurrency](../../essential/concurrency/index.html).* By invoking
    [`SwingWorker.isCanceled`](http://download.oracle.com/javase/7/docs/api/javax/swing/SwingWorker.html#isCanceled())
    at short intervals. This method returns `true` if
    `cancel` has been invoked for this
    `SwingWorker`.

The `cancel` method takes a single `boolean`
argument. If the argument is `true`, `cancel`
sends the background task an interrupt. Whether the argument is
`true` or `false`, invoking `cancel`
changes the cancellation status of the object to `true`.
This is the value returned by `isCanceled`. Once changed,
the cancellation status cannot be changed back.

The `Flipper` example from the previous section uses the
status-only idiom. The main loop in `doInBackground` exits
when `isCancelled` returns `true`. This will
occur when the user clicks the "Cancel" button, triggering code that
invokes `cancel` with an argument of `false`.

The status-only approach makes sense for `Flipper` because
its implementation of `SwingWorker.doInBackground` does not
include any code that might throw `InterruptedException`.
To respond to an interrupt, the background task would have to invoke
`Thread.isInterrupted` at short intervals. It's just as
easy to use `SwingWorker.isCancelled` for the same purpose

---

**Note:** If `get` is invoked on a `SwingWorker` object
after its background task has been cancelled,
[`java.util.concurrent.CancellationException`](http://download.oracle.com/javase/7/docs/api/java/util/concurrent/CancellationException.html)
is thrown.

---

[« Previous](interim.html)
•
[Trail](../TOC.html)
•
[Next »](bound.html)

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

**Previous page:** Tasks that Have Interim Results
  
**Next page:** Bound Properties and Status Methods




A browser with JavaScript enabled is required for this page to operate properly.