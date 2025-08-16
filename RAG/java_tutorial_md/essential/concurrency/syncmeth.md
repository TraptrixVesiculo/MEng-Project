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

Synchronized Methods

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

[« Previous](memconsist.html) • [Trail](../TOC.html) • [Next »](locksync.html)

# Synchronized Methods

The Java programming language provides two basic synchronization
idioms: *synchronized methods* and *synchronized
statements*. The more complex of the two, synchronized
statements, are described in the next section. This section is about
synchronized methods.

To make a method synchronized, simply add the
`synchronized` keyword to its declaration:

```

public class SynchronizedCounter {
    private int c = 0;

    public synchronized void increment() {
        c++;
    }

    public synchronized void decrement() {
        c--;
    }

    public synchronized int value() {
        return c;
    }
}

```

If `count` is an instance of `SynchronizedCounter`, then
making these methods synchronized has two effects:

* First, it is not possible for two invocations of synchronized
  methods on the same object to interleave. When one thread is
  executing a synchronized method for an object, all other threads
  that invoke synchronized methods for the same object block
  (suspend execution) until the first thread is done with the
  object.* Second, when a synchronized method exits, it automatically
    establishes a happens-before relationship with *any subsequent
    invocation* of a synchronized method for the same object.
    This guarantees that changes to the state of the object are
    visible to all threads.

Note that constructors cannot be synchronized — using the
`synchronized` keyword with a constructor is a syntax
error. Synchronizing constructors doesn't make sense, because only the
thread that creates an object should have access to it while it is
being constructed.

---

**Warning:** 
When constructing an object that will be shared between threads, be very
careful that a reference to the object does not "leak" prematurely.
For example, suppose you want to maintain a `List` called
`instances` containing every instance of class. You might
be tempted to add the line

```

instances.add(this);

```

to your constructor. But then other threads can use
`instances` to access the object before construction of the
object is complete.

---

Synchronized methods enable a simple strategy for preventing thread
interference and memory consistency errors: if an object is visible to
more than one thread, all reads or writes to that object's variables
are done through `synchronized` methods. (An important
exception: `final` fields, which cannot be modified after
the object is constructed, can be safely read through non-synchronized
methods, once the object is constructed) This strategy is effective,
but can present problems with [liveness](liveness.html), as
we'll see later in this lesson.

[« Previous](memconsist.html)
•
[Trail](../TOC.html)
•
[Next »](locksync.html)

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

**Previous page:** Memory Consistency Errors
  
**Next page:** Intrinsic Locks and Synchronization




A browser with JavaScript enabled is required for this page to operate properly.