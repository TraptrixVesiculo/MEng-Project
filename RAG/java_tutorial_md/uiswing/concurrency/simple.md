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

Simple Background Tasks

[Tasks that Have Interim Results](interim.html)

[Canceling Background Tasks](cancel.html)

[Bound Properties and Status Methods](bound.html)

[Home Page](../../index.html)
>
[Creating a GUI With JFC/Swing](../index.html)
>
[Concurrency in Swing](index.html)

[« Previous](worker.html) • [Trail](../TOC.html) • [Next »](interim.html)

# Simple Background Tasks

Let's start with a task that is very simple, but potentially
time-consuming. The
[`TumbleItem`](../examples/components/TumbleItemProject/src/components/TumbleItem.java)
applet loads a set of graphic files used in
an animation. If the graphic files are loaded from an
initial thread, there may be a delay before the GUI
appears. If the graphic files are loaded from the event dispatch
thread, the GUI may be temporarily unresponsive.

To avoid these problems, `TumbleItem` creates and executes
an instance of `SwingWorker` from its initial threads. The
object's `doInBackground` method, executing in a worker thread,
loads the images into an `ImageIcon` array, and returns a
reference to it.
Then the `done` method, executing in the event
dispatch thread, invokes `get` to retrieve this reference,
which it assigns to an applet class field named `imgs`.
This
allows `TumbleItem` to construct the GUI immediately,
without waiting for the images to finish loading.

Here is the code that defines and executes the
`SwingWorker` object.

```

SwingWorker worker = new SwingWorker<ImageIcon[], Void>() {
    @Override
    public ImageIcon[] doInBackground() {
        final ImageIcon[] innerImgs = new ImageIcon[nimgs];
        for (int i = 0; i < nimgs; i++) {
            innerImgs[i] = loadImage(i+1);
        }
        return innerImgs;
    }

    @Override
    public void done() {
        //Remove the "Loading images" label.
        animator.removeAll();
        loopslot = -1;
        try {
            imgs = get();
        } catch (InterruptedException ignore) {}
        catch (java.util.concurrent.ExecutionException e) {
            String why = null;
            Throwable cause = e.getCause();
            if (cause != null) {
                why = cause.getMessage();
            } else {
                why = e.getMessage();
            }
            System.err.println("Error retrieving file: " + why);
        }
    }
};


```

All concrete subclasses of `SwingWorker` implement
`doInBackground`; implementation of `done` is
optional.

Notice that `SwingWorker` is a generic class, with two type
parameters. The first type parameter specifies a return type for
`doInBackground`, and also for the `get` method,
which is invoked by other threads to retrieve the object returned by
`doInBackground`.
`SwingWorker`'s second type parameter specifies a type for
interim results returned while the background task is still active.
Since this example doesn't return interim results,
[`Void`](http://download.oracle.com/javase/7/docs/api/java/lang/Void.html) 
is used as a placeholder.

You may wonder if the code that sets `imgs` is
unnecessarily complicated. Why make `doInBackground` return
an object and use `done` to retrieve it? Why not just have
`doInBackground` set `imgs` directly? The
problem is that the object `imgs` refers to is created in
the worker thread and used in the event dispatch thread. When objects
are shared between threads in this way, you must make sure that
changes made in one thread are visible to the other. Using
`get` guarantees this, because using `get`
creates a *happens before* relationship between the code that
creates `imgs` and the code that uses it. For more on the
happens before relationship, refer to
[Memory Consistency Errors](../../essential/concurrency/memconsist.html)
in the
[Concurrency](../../essential/concurrency/index.html)
lesson.

There are actually two ways to retrieve the object returned by
`doInBackground`.

* Invoke
  [`SwingWorker.get` with no arguments](http://download.oracle.com/javase/7/docs/api/javax/swing/SwingWorker.html#get()). If the background task is not finished,
  `get` blocks until it is.* Invoke
    [`SwingWorker.get` with arguments indicating a timeout](http://download.oracle.com/javase/7/docs/api/javax/swing/SwingWorker.html#get(long,%20java.util.concurrent.TimeUnit)). If the background task is not finished,
    `get` blocks until it is — unless the timeout
    expires first, in which case `get` throws
    `java.util.concurrent.TimeoutException`.

Be careful when invoking either overload of `get` from the
event dispatch thread; until `get` returns, no GUI events
are being processed, and the GUI is "frozen". Don't invoke
`get` without arguments unless you are confident that the
background task is complete or close to completion.

For more on the `TumbleItem` example, refer to
[How to Use Swing Timers](../misc/timer.html)
in the lesson
[Using Other Swing Features](../misc/index.html).

[« Previous](worker.html)
•
[Trail](../TOC.html)
•
[Next »](interim.html)

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

**Previous page:** Worker Threads and SwingWorker
  
**Next page:** Tasks that Have Interim Results




A browser with JavaScript enabled is required for this page to operate properly.