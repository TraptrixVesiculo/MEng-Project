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

Executor Interfaces

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

[« Previous](executors.html) • [Trail](../TOC.html) • [Next »](pools.html)

# Executor Interfaces

The `java.util.concurrent` package defines three executor
interfaces:

* `Executor`, a simple interface that supports
  launching new tasks.* `ExecutorService`, a subinterface of
    `Executor`, which adds features that help manage the
    lifecycle, both of the individual tasks and of the executor
    itself.* `ScheduledExecutorService`, a subinterface of
      `ExecutorService`, supports future and/or periodic
      execution of tasks.

Typically, variables that refer to executor objects are declared as
one of these three interface types, not with an executor class type.

### The `Executor` Interface

The
[`Executor`](http://download.oracle.com/javase/7/docs/api/java/util/concurrent/Executor.html)
interface provides a single method, `execute`, designed to
be a drop-in replacement for a common thread-creation idiom. If
`r` is a `Runnable` object, and `e`
is an `Executor` object you can replace

```

(new Thread(r)).start();

```

with

```

e.execute(r);

```

However, the definition of `execute` is less specific. The
low-level idiom creates a new thread and launches it immediately.
Depending on the `Executor` implementation,
`execute` may do the same thing, but is more likely to use
an existing worker thread to run `r`, or to place
`r` in a queue to wait for a worker thread to become
available. (We'll describe worker threads in the section on [Thread Pools](pools.html).)

The executor implementations in `java.util.concurrent` are
designed to make full use of the more advanced
`ExecutorService` and `ScheduledExecutorService`
interfaces, although they also work with the base
`Executor` interface.

### The `ExecutorService` Interface

The
[`ExecutorService`](http://download.oracle.com/javase/7/docs/api/java/util/concurrent/ExecutorService.html)
interface supplements `execute` with a similar, but more
versatile `submit` method. Like `execute`,
`submit` accepts `Runnable` objects, but also
accepts
[`Callable`](http://download.oracle.com/javase/7/docs/api/java/util/concurrent/Callable.html)
objects, which allow the task to return a value. The
`submit` method returns a
[`Future`](http://download.oracle.com/javase/7/docs/api/java/util/concurrent/Future.html)
object, which is used to retrieve the `Callable` return
value and to manage the status of both `Callable` and
`Runnable` tasks.

`ExecutorService` also provides methods for submitting
large collections of `Callable` objects. Finally,
`ExecutorService` provides a number of methods for managing
the shutdown of the executor. To support immediate shutdown, tasks
should handle [interrupts](interrupt.html) correctly.

### The `ScheduledExecutorService` Interface

The
[`ScheduledExecutorService`](http://download.oracle.com/javase/7/docs/api/java/util/concurrent/ScheduledExecutorService.html)
interface supplements the methods of its parent
`ExecutorService` with `schedule`, which
executes a `Runnable` or `Callable` task after a
specified delay. In addition, the interface defines
`scheduleAtFixedRate` and
`scheduleWithFixedDelay`, which executes specified tasks
repeatedly, at defined intervals.

[« Previous](executors.html)
•
[Trail](../TOC.html)
•
[Next »](pools.html)

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

**Previous page:** Executors
  
**Next page:** Thread Pools




A browser with JavaScript enabled is required for this page to operate properly.