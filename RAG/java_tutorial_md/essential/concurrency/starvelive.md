[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Essential Classes
  
**Lesson:** Concurrency
  
**Section:** Liveness

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

Starvation and Livelock

[Guarded Blocks](guardmeth.html)

[Immutable Objects](immutable.html)

[A Synchronized Class Example](syncrgb.html)

[A Strategy for Defining Immutable Objects](imstrat.html)

[High Level Concurrency Objects](highlevel.html)

[Lock Objects](newlocks.html)

[Executors](executors.html)

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

[« Previous](deadlock.html) • [Trail](../TOC.html) • [Next »](guardmeth.html)

# Starvation and Livelock

Starvation and livelock are much less common a problem than deadlock,
but are still problems that every designer of concurrent software is
likely to encounter.

### Starvation

*Starvation* describes a situation where a thread is unable to
gain regular access to shared resources and is unable to make
progress. This happens when shared resources are made unavailable for
long periods by "greedy" threads. For example, suppose an object
provides a synchronized method that often takes a long time to return.
If one thread invokes this method frequently, other threads that also
need frequent synchronized access to the same object will often be
blocked.

### Livelock

A thread often acts in response to the action of another
thread. If the other thread's action is also a response to the action
of another thread, then *livelock* may result. As with deadlock,
livelocked threads are unable to make further progress. However, the
threads are not blocked — they are simply too busy responding to
each other to resume work. This is comparable to two people attempting to
pass each other in a corridor: Alphonse moves to his left to let
Gaston pass, while Gaston moves to his right to let Alphonse pass.
Seeing that they are still blocking each other, Alphone moves to his
right, while Gaston moves to his left. They're still blocking each
other, so...

[« Previous](deadlock.html)
•
[Trail](../TOC.html)
•
[Next »](guardmeth.html)

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

**Previous page:** Deadlock
  
**Next page:** Guarded Blocks




A browser with JavaScript enabled is required for this page to operate properly.