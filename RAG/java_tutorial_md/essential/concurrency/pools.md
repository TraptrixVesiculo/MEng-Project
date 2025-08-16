[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Essential Classes
  
**Lesson:** Concurrency
  
**Section:** High Level Concurrency Objects
  
**Subsection:** Executors

[Concurrency](index.html)

[Processes and Threads](procthread.html)

[Thread Objects](threads.html)

[Defining and Starting a Thread](runthread.html)

[Pausing Execution with Sleep](sleep.html)

[Interrupts](interrupt.html)

[Joins](join.html)

[The SimpleThreads Example](simple.html)

[Synchronization](sync.html)

[Thread Interference](interfere.html)

[Memory Consistency Errors](memconsist.html)

[Synchronized Methods](syncmeth.html)

[Intrinsic Locks and Synchronization](locksync.html)

[Atomic Access](atomic.html)

[Liveness](liveness.html)

[Deadlock](deadlock.html)

[Starvation and Livelock](starvelive.html)

[Guarded Blocks](guardmeth.html)

[Immutable Objects](immutable.html)

[A Synchronized Class Example](syncrgb.html)

[A Strategy for Defining Immutable Objects](imstrat.html)

[High Level Concurrency Objects](highlevel.html)

[Lock Objects](newlocks.html)

[Executors](executors.html)

[Executor Interfaces](exinter.html)

Thread Pools

[Fork/Join](forkjoin.html)

[Concurrent Collections](collections.html)

[Atomic Variables](atomicvars.html)

[Concurrent Random Numbers](threadlocalrandom.html)

[For Further Reading](further.html)

[Questions and Exercises](QandE/questions.html)

[Home Page](../../index.html)
>
[Essential Classes](../index.html)
>
[Concurrency](index.html)

[« Previous](exinter.html) • [Trail](../TOC.html) • [Next »](forkjoin.html)

# Thread Pools

Most of the executor implementations in
`java.util.concurrent` use *thread pools*, which
consist of *worker threads*. This kind of thread exists
separately from the `Runnable` and
`Callable` tasks it executes and is often used to execute
multiple tasks.

Using worker threads minimizes the overhead due to thread creation. Thread
objects use a significant amount of memory, and in a large-scale
application, allocating and deallocating many thread objects creates a
significant memory management overhead.

One common type of thread pool is the *fixed thread pool*. This
type of pool always has a specified number of threads running;
if a thread is somehow terminated while it is still in use, it is
automatically replaced with a new thread. Tasks are submitted to the
pool via an internal queue, which holds extra tasks whenever there are
more active tasks than threads.

An important advantage of the fixed thread pool is that applications
using it *degrade gracefully*. To understand this, consider a
web server application where each HTTP request is handled by a
separate thread. If the application simply creates a new thread for
every new HTTP request, and the system receives more requests than it
can handle immediately, the application will suddenly stop responding to
*all* requests when the overhead of all those threads exceed the
capacity of the system. With a limit on the number of the threads that
can be created, the application will not be servicing HTTP requests as
quickly as they come in, but it will be servicing them as quickly as
the system can sustain.

A simple way to create an executor that uses a fixed thread pool is to
invoke the
[`newFixedThreadPool`](http://download.oracle.com/javase/7/docs/api/java/util/concurrent/Executors.html#newFixedThreadPool(int))
factory method in
[`java.util.concurrent.Executors`](http://download.oracle.com/javase/7/docs/api/java/util/concurrent/Executors.html)
This class also provides the following factory methods:

* The
  [`newCachedThreadPool`](http://download.oracle.com/javase/7/docs/api/java/util/concurrent/Executors.html#newCachedThreadPool(int))
  method creates an executor with an expandable thread pool. This
  executor is suitable for applications that launch many short-lived
  tasks.* The
    [`newSingleThreadExecutor`](http://download.oracle.com/javase/7/docs/api/java/util/concurrent/Executors.html#newSingleThreadExecutor(int))
    method creates an executor that executes a single task at a time.* Several factory methods are
      `ScheduledExecutorService` versions of the above
      executors.

If none of the executors provided by the above factory methods meet
your needs, constructing instances of
[`java.util.concurrent.ThreadPoolExecutor`](http://download.oracle.com/javase/7/docs/api/java/util/concurrent/ThreadPoolExecutor.html)
or
[`java.util.concurrent.ScheduledThreadPoolExecutor`](http://download.oracle.com/javase/7/docs/api/java/util/concurrent/ScheduledThreadPoolExecutor.html)
will give you additional options.

[« Previous](exinter.html)
•
[Trail](../TOC.html)
•
[Next »](forkjoin.html)

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

**Previous page:** Executor Interfaces
  
**Next page:** Fork/Join




A browser with JavaScript enabled is required for this page to operate properly.