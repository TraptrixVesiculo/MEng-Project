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

Thread Interference

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

[« Previous](sync.html) • [Trail](../TOC.html) • [Next »](memconsist.html)

# Thread Interference

Consider a simple class called
[`Counter`](examples/Counter.java)

```


class Counter {
    private int c = 0;

    public void increment() {
        c++;
    }

    public void decrement() {
        c--;
    }

    public int value() {
        return c;
    }

}

```

`Counter` is designed so that each invocation of
`increment` will add 1 to `c`, and each
invocation of `decrement` will subtract 1 from
`c`. However, if a `Counter` object is
referenced from multiple threads, interference between threads may
prevent this from happening as expected.

Interference happens when two operations, running in different threads,
but acting on the same data, *interleave*. This means that the two
operations consist of multiple steps, and the sequences of steps
overlap.

It might not seem possible for operations on instances of
`Counter` to interleave, since both operations on
`c` are single, simple statements. However, even simple
statements can translate to multiple steps by the virtual machine.
We won't examine the specific steps the virtual machine takes —
it is enough to know that the single expression `c++` can
be decomposed into three steps:

1. Retrieve the current value of `c`.- Increment the retrieved value by 1.- Store the incremented value back in `c`.

The expression `c--` can be decomposed the same way, except
that the second step decrements instead of increments.

Suppose Thread A invokes `increment` at about the same
time Thread B invokes `decrement`. If the initial value of
`c` is `0`, their interleaved
actions might follow this sequence:

1. Thread A: Retrieve c.- Thread B: Retrieve c.- Thread A: Increment retrieved value; result is 1.- Thread B: Decrement retrieved value; result is -1.- Thread A: Store result in c; c is now 1.- Thread B: Store result in c; c is now -1.

Thread A's result is lost, overwritten by Thread B. This particular
interleaving is only one possibility. Under different circumstances it
might be Thread B's result that gets lost, or there could be no error
at all. Because they are unpredictable, thread interference bugs can
be difficult to detect and fix.

[« Previous](sync.html)
•
[Trail](../TOC.html)
•
[Next »](memconsist.html)

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

**Previous page:** Synchronization
  
**Next page:** Memory Consistency Errors




A browser with JavaScript enabled is required for this page to operate properly.