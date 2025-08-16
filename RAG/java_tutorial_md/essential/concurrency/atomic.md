[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Essential Classes
  
**Lesson:** Concurrency
  
**Section:** Synchronization

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

Atomic Access

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

[« Previous](locksync.html) • [Trail](../TOC.html) • [Next »](liveness.html)

# Atomic Access

In programming, an *atomic* action is one that effectively
happens all at once. An atomic action cannot stop in the middle: it
either happens completely, or it doesn't happen at all. No side effects
of an atomic action are visible until the action is complete.

We have already seen that an increment expression, such as
`c++`, does not describe an atomic action. Even very simple
expressions can define complex actions that can decompose into other
actions.
However, there are actions you can specify that are atomic:

* Reads and writes are atomic for reference variables and for most
  primitive variables (all types except `long` and
  `double`).* Reads and writes are atomic for *all* variables declared
    `volatile` (*including* `long` and
    `double` variables).

Atomic actions cannot be interleaved, so they can be used without fear
of thread interference. However, this does not eliminate all need to
synchronize atomic actions, because memory consistency errors are
still possible. Using `volatile` variables reduces the risk
of memory consistency errors, because any write to a
`volatile` variable establishes a happens-before
relationship with subsequent reads of that same variable. This means
that changes to a `volatile` variable are always visible to
other threads. What's more, it also means that when a thread reads a
`volatile` variable, it sees not just the latest change to the
`volatile`, but also the side effects of the code that led
up the change.

Using simple atomic variable access is more efficient than accessing
these variables through synchronized code, but requires more care by
the programmer to avoid memory consistency errors. Whether the extra
effort is worthwhile depends on the size and complexity of the
application.

Some of the classes in the
[`java.util.concurrent`](http://download.oracle.com/javase/7/docs/api/java/util/concurrent/package-summary.html)
package provide atomic methods that do not rely on synchronization. We'll
discuss them in the section on [High Level
Concurrency Objects](highlevel.html).

[« Previous](locksync.html)
•
[Trail](../TOC.html)
•
[Next »](liveness.html)

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

**Previous page:** Intrinsic Locks and Synchronization
  
**Next page:** Liveness




A browser with JavaScript enabled is required for this page to operate properly.