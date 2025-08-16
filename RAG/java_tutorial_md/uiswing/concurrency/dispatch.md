[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Creating a GUI With JFC/Swing
  
**Lesson:** Concurrency in Swing

[Concurrency in Swing](index.html)

[Initial Threads](initial.html)

The Event Dispatch Thread

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

[« Previous](initial.html) • [Trail](../TOC.html) • [Next »](worker.html)

# The Event Dispatch Thread

Swing event handling code runs on a special thread known as the
event dispatch thread. Most code that invokes Swing methods
also runs on this thread.
This is necessary because most Swing
object methods are not "thread safe": invoking them from multiple
threads risks
[thread interference](../../essential/concurrency/interfere.html)
or
[memory consistency errors](../../essential/concurrency/memconsist.html).
Some Swing component methods are labelled "thread safe" in the API
specification; these can be safely invoked from any thread. All other
Swing component methods must be invoked from the event
dispatch thread. Programs that ignore this rule may function
correctly most of the time, but are subject to unpredictable errors
that are difficult to reproduce.

---

**A note on thread safety:** 
It may seem strange that such an important part of the Java platform
is not thread safe. It turns out that any attempt to create a
thread-safe GUI library faces some fundamental problems. For more on
this issue, see the following entry in Graham Hamilton's blog:
[MultiThreaded toolkits: A failed dream?](http://weblogs.java.net/blog/kgh/archive/2004/10/multithreaded_t.html)

---

It's useful to think of the code running on the event dispatch thread
as a series of short tasks. Most tasks are invocations of
event-handling methods, such as
`ActionListener.actionPerformed`. Other tasks can be
scheduled by application code, using `invokeLater` or
`invokeAndWait`. Tasks on the event dispatch thread must
finish quickly; if they don't, unhandled events back up and the user
interface becomes unresponsive.

If you need to determine whether your code is running on the event
dispatch thread, invoke
[`javax.swing.SwingUtilities.isEventDispatchThread`](http://download.oracle.com/javase/7/docs/api/javax/swing/SwingUtilities.html#isEventDispatchThread()).

[« Previous](initial.html)
•
[Trail](../TOC.html)
•
[Next »](worker.html)

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

**Previous page:** Initial Threads
  
**Next page:** Worker Threads and SwingWorker




A browser with JavaScript enabled is required for this page to operate properly.