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

[Executors](executors.html)

[Executor Interfaces](exinter.html)

[Thread Pools](pools.html)

[Fork/Join](forkjoin.html)

Concurrent Collections

[Atomic Variables](atomicvars.html)

[Concurrent Random Numbers](threadlocalrandom.html)

[For Further Reading](further.html)

[Questions and Exercises](QandE/questions.html)

[Home Page](../../index.html)
>
[Essential Classes](../index.html)
>
[Concurrency](index.html)

[« Previous](forkjoin.html) • [Trail](../TOC.html) • [Next »](atomicvars.html)

# Concurrent Collections

The `java.util.concurrent` package includes a number of
additions to the Java Collections Framework. These are most easily
categorized by the collection interfaces provided:

* [`BlockingQueue`](http://download.oracle.com/javase/7/docs/api/java/util/concurrent/BlockingQueue.html)
  defines a first-in-first-out data structure that blocks or times out
  when you attempt to add to a full queue, or retrieve from an empty
  queue.* [`ConcurrentMap`](http://download.oracle.com/javase/7/docs/api/java/util/concurrent/ConcurrentMap.html)
    is a subinterface of
    [`java.util.Map`](http://download.oracle.com/javase/7/docs/api/java/util/Map.html)
    that defines useful atomic operations. These operations remove or
    replace a key-value pair only if the key is present, or add a
    key-value pair only if the key is absent. Making these operations
    atomic helps avoid synchronization.
    The standard general-purpose implementation of
    `ConcurrentMap` is
    [`ConcurrentHashMap`](http://download.oracle.com/javase/7/docs/api/java/util/concurrent/ConcurrentHashMap.html), which is a concurrent analog of
    [`HashMap`](http://download.oracle.com/javase/7/docs/api/java/util/HashMap.html).* [`ConcurrentNavigableMap`](http://download.oracle.com/javase/7/docs/api/java/util/concurrent/ConcurrentNavigableMap.html)
      is a subinterface of `ConcurrentMap` that supports
      approximate matches.
      The standard general-purpose implementation of
      `ConcurrentNavigableMap` is
      [`ConcurrentSkipListMap`](http://download.oracle.com/javase/7/docs/api/java/util/concurrent/ConcurrentSkipListMap.html), which is a concurrent analog of
      [`TreeMap`](http://download.oracle.com/javase/7/docs/api/java/util/TreeMap.html).

All of these collections help avoid [Memory
Consistency Errors](memconsist.html) by defining a happens-before relationship
between an operation that adds an object to the collection with
subsequent operations that access or remove that object.

[« Previous](forkjoin.html)
•
[Trail](../TOC.html)
•
[Next »](atomicvars.html)

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

**Previous page:** Fork/Join
  
**Next page:** Atomic Variables




A browser with JavaScript enabled is required for this page to operate properly.