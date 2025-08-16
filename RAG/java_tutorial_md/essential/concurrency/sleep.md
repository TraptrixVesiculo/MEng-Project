[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Essential Classes
  
**Lesson:** Concurrency
  
**Section:** Thread Objects

[Concurrency](index.html)

[Processes and Threads](procthread.html)

[Thread Objects](threads.html)

[Defining and Starting a Thread](runthread.html)

Pausing Execution with Sleep

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

[« Previous](runthread.html) • [Trail](../TOC.html) • [Next »](interrupt.html)

# Pausing Execution with Sleep

`Thread.sleep` causes the current thread to suspend
execution for a specified period. This is an efficient means of
making processor time available to the other threads of an application
or other applications that might be running on a computer system. The
`sleep` method can also be used for pacing, as shown in the
example that follows, and waiting for another thread with duties that are
understood to have time requirements, as with the
`SimpleThreads` example in a later section.

Two overloaded versions of `sleep` are provided: one
that specifies the sleep time to the millisecond and one that
specifies the sleep time to the nanosecond. However, these sleep times
are not guaranteed to be precise, because they are limited by the
facilities provided by the underlying OS. Also, the sleep period can
be terminated by interrupts, as we'll see in a later section.
In any case, you cannot assume that invoking `sleep` will
suspend the thread for precisely the time period specified.

The
[`SleepMessages`](examples/SleepMessages.java)
example uses `sleep` to print messages at four-second
intervals:

```


public class SleepMessages {
    public static void main(String args[]) throws InterruptedException {
        String importantInfo[] = {
            "Mares eat oats",
            "Does eat oats",
            "Little lambs eat ivy",
            "A kid will eat ivy too"
        };

        for (int i = 0; i < importantInfo.length; i++) {
            //Pause for 4 seconds
            Thread.sleep(4000);
            //Print a message
            System.out.println(importantInfo[i]);
        }
    }
}


```

Notice that `main` declares that it `throws
InterruptedException`. This is an exception that
`sleep` throws when another thread interrupts the current
thread while `sleep` is active. Since this application has
not defined another thread to cause the interrupt, it doesn't bother
to catch `InterruptedException`.

[« Previous](runthread.html)
•
[Trail](../TOC.html)
•
[Next »](interrupt.html)

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

**Previous page:** Defining and Starting a Thread
  
**Next page:** Interrupts




A browser with JavaScript enabled is required for this page to operate properly.