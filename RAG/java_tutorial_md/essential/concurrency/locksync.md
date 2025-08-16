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

Intrinsic Locks and Synchronization

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

[« Previous](syncmeth.html) • [Trail](../TOC.html) • [Next »](atomic.html)

# Intrinsic Locks and Synchronization

Synchronization is built around an internal entity known as the
*intrinsic lock* or *monitor lock*. (The API specification
often refers to this entity simply as a "monitor.") Intrinsic locks
play a role in both aspects of synchronization: enforcing
exclusive access to an object's state and establishing happens-before
relationships that are essential to visibility.

Every object has an intrinsic lock associated with it. By convention,
a thread that needs exclusive and consistent access to an object's
fields has to *acquire* the object's intrinsic lock
before accessing them, and then *release* the intrinsic lock
when it's done with them. A thread is said to *own* the intrinsic
lock between the time it has acquired the lock and released the lock.
As long as a thread owns an intrinsic lock, no other thread can
acquire the same lock. The other thread will block when it attempts to
acquire the lock.

When a thread releases an intrinsic lock, a happens-before
relationship is established between that action and any subsequent
acquistion of the same lock.

### Locks In Synchronized Methods

When a thread invokes a synchronized method, it automatically acquires
the intrinsic lock for that method's object and releases it when the method
returns. The lock release occurs even if the return was caused by an
uncaught exception.

You might wonder what happens when a static synchronized method is
invoked, since a static method is associated with a class, not an
object. In this case, the thread acquires the intrinsic lock for the
`Class` object associated with the class. Thus access to
class's static fields is controlled by a lock that's distinct from the lock
for any instance of the class.

### Synchronized Statements

Another way to create synchronized code is with *synchronized
statements*. Unlike synchronized methods, synchronized
statements must specify the object that provides the intrinsic lock:

```

public void addName(String name) {
    synchronized(this) {
        lastName = name;
        nameCount++;
    }
    nameList.add(name);
}

```

In this example, the `addName` method needs to synchronize
changes to `lastName` and `nameCount`, but also
needs to avoid synchronizing invocations of other objects' methods.
(Invoking other objects' methods from synchronized code can create
problems that are described in the section on [Liveness](liveness.html).) Without synchronized statements,
there would have to be a separate, unsynchronized method for the sole
purpose of invoking `nameList.add`.

Synchronized statements are also useful for improving concurrency with
fine-grained synchronization. Suppose, for example, class
`MsLunch` has two instance fields, `c1` and
`c2`, that are never used together. All updates of these
fields must be synchronized, but there's no reason to prevent an
update of c1 from being interleaved with an update of c2 — and
doing so reduces concurrency by creating unnecessary blocking. Instead
of using synchronized methods or otherwise using the lock associated
with `this`, we create two objects solely to provide locks.

```

public class MsLunch {
    private long c1 = 0;
    private long c2 = 0;
    private Object lock1 = new Object();
    private Object lock2 = new Object();

    public void inc1() {
        synchronized(lock1) {
            c1++;
        }
    }

    public void inc2() {
        synchronized(lock2) {
            c2++;
        }
    }
}

```

Use this idiom with extreme care. You must be absolutely sure that it
really is safe to interleave access of the affected fields.

### Reentrant Synchronization

Recall that a thread cannot acquire a lock owned by another thread.
But a thread *can* acquire a lock that it already owns. Allowing
a thread to acquire the same lock more than once enables *reentrant
synchronization*. This describes a situation where synchronized
code, directly or indirectly, invokes a method that also contains
synchronized code, and both sets of code use the same lock. Without
reentrant synchronization, synchronized code would have to take many
additional precautions to avoid having a thread cause itself to block.

[« Previous](syncmeth.html)
•
[Trail](../TOC.html)
•
[Next »](atomic.html)

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

**Previous page:** Synchronized Methods
  
**Next page:** Atomic Access




A browser with JavaScript enabled is required for this page to operate properly.