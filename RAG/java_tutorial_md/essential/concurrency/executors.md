[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Essential Classes
  
**Lesson:** Concurrency
  
**Section:** High Level Concurrency Objects

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

Executors

[Executor Interfaces](exinter.html)

[Thread Pools](pools.html)

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

[« Previous](newlocks.html) • [Trail](../TOC.html) • [Next »](exinter.html)

# Executors

In all of the previous examples, there's a close connection between the
task being done by a new thread, as defined by its
`Runnable` object, and the thread itself, as
defined by a `Thread` object. This works well for small
applications, but in large-scale applications, it makes sense to
separate thread management and creation from the rest of the
application. Objects that encapsulate these functions are known as
*executors*. The following subsections describe executors in
detail.

* [Executor Interfaces](exinter.html) define the three
  executor object types.
* [Thread Pools](pools.html) are the most common kind
  of executor implementation.
* [Fork/Join](forkjoin.html) is a framework (new in JDK 7)
  for taking advantage of multiple processors.

[« Previous](newlocks.html)
•
[Trail](../TOC.html)
•
[Next »](exinter.html)

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

**Previous page:** Lock Objects
  
**Next page:** Executor Interfaces




A browser with JavaScript enabled is required for this page to operate properly.