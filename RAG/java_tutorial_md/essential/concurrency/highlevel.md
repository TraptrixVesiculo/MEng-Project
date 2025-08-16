[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Essential Classes
  
**Lesson:** Concurrency

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

High Level Concurrency Objects

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

[« Previous](imstrat.html) • [Trail](../TOC.html) • [Next »](newlocks.html)

# High Level Concurrency Objects

So far, this lesson has focused on the low-level APIs that have been
part of the Java platform from the very beginning. These APIs are
adequate for very basic tasks, but higher-level building blocks are
needed for more advanced tasks. This is especially true for massively
concurrent applications that fully exploit today's
multiprocessor and multi-core systems.

In this section we'll look at some of the high-level concurrency
features introduced with version 5.0 of the Java platform. Most of
these features are implemented in the new
`java.util.concurrent` packages. There are also new
concurrent data structures in the Java Collections Framework.

* [Lock objects](newlocks.html) support locking
  idioms that simplify many concurrent applications.
* [Executors](executors.html) define a high-level API
  for launching and managing threads. Executor implementations
  provided by `java.util.concurrent` provide thread pool
  management suitable for large-scale applications.
* [Concurrent collections](collections.html) make it
  easier to manage large collections of data, and can greatly reduce
  the need for synchronization.
* [Atomic variables](atomicvars.html) have features
  that minimize synchronization and help avoid memory consistency
  errors.
* [`ThreadLocalRandom`](threadlocalrandom.html) (in
  JDK 7) provides
  efficient generation of pseudorandom numbers from multiple threads.

[« Previous](imstrat.html)
•
[Trail](../TOC.html)
•
[Next »](newlocks.html)

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

**Previous page:** A Strategy for Defining Immutable Objects
  
**Next page:** Lock Objects




A browser with JavaScript enabled is required for this page to operate properly.