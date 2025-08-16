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

Memory Consistency Errors

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

[« Previous](interfere.html) • [Trail](../TOC.html) • [Next »](syncmeth.html)

# Memory Consistency Errors

*Memory consistency errors* occur when different threads have
inconsistent views of what should be the same data. The causes of
memory consistency errors are complex and beyond the scope of this
tutorial. Fortunately, the programmer does not need a detailed
understanding of these causes. All that is needed is a strategy for
avoiding them.

The key to avoiding memory consistency errors is understanding the
*happens-before* relationship. This relationship is simply a
guarantee that memory writes by one specific statement are visible to
another specific statement. To see this, consider the following
example. Suppose a simple `int` field is defined and
initialized:

```

int counter = 0;

```

The `counter` field is shared between two threads, A and B.
Suppose thread A increments `counter`:

```

counter++;

```

Then, shortly afterwards, thread B prints out `counter`:

```

System.out.println(counter);

```

If the two statements had been executed in the same thread, it would
be safe to assume that the value printed out would be "1". But if the
two statements are executed in separate threads, the value printed out
might well be "0", because there's no guarantee that thread A's change
to `counter` will be visible to thread B — unless the
programmer has established a happens-before relationship between these
two statements.

There are several actions that create happens-before relationships.
One of them is synchronization, as we will see in the following
sections.

We've already seen two actions that create happens-before
relationships.

* When a statement invokes `Thread.start`, every
  statement that has a happens-before relationship with that
  statement also has a happens-before relationship with every
  statement executed by the new thread. The effects of the code that
  led up to the creation of the new thread are visible to the new
  thread.* When a thread terminates and causes a
    `Thread.join` in another thread to return, then all the
    statements executed by the terminated thread have a happens-before
    relationship with all the statements following the successful join.
    The effects of the code in the thread are now visible to the
    thread that performed the join.

For a list of actions that create happens-before relationships, refer
to the
[Summary page of the `java.util.concurrent` package.](http://download.oracle.com/javase/7/docs/api/java/util/concurrent/package-summary.html#MemoryVisibility).

[« Previous](interfere.html)
•
[Trail](../TOC.html)
•
[Next »](syncmeth.html)

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

**Previous page:** Thread Interference
  
**Next page:** Synchronized Methods




A browser with JavaScript enabled is required for this page to operate properly.