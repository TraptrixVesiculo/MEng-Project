[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

Concurrency

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

[Concurrent Collections](collections.html)

[Atomic Variables](atomicvars.html)

[Concurrent Random Numbers](threadlocalrandom.html)

[For Further Reading](further.html)

[Questions and Exercises](QandE/questions.html)

**Trail:** Essential Classes

[Home Page](../../index.html)
>
[Essential Classes](../index.html)

[« Previous](../io/index.html) • [Trail](../TOC.html) • [Next »](procthread.html)

# Lesson: Concurrency

Computer users take it for granted that their systems can do more than
one thing at a time. They assume that they can continue to work in a
word processor, while other applications download files, manage the print
queue, and stream audio. Even a single application is often expected to do
more than one thing at a time. For example, that streaming audio
application must simultaneously read the digital audio off the network,
decompress it, manage playback, and update its display. Even the word
processor should always be ready to respond to keyboard and mouse
events, no matter how busy it is reformatting text or updating the
display. Software that can do such things is known as
*concurrent* software.

The Java platform is designed from the ground up to support concurrent
programming, with basic concurrency support in the Java programming
language and the Java class libraries. Since version 5.0, the Java
platform has also included high-level concurrency APIs. This lesson
introduces the platform's basic concurrency support and summarizes some
of the high-level APIs in the `java.util.concurrent`
packages.

[« Previous](../io/index.html)
•
[Trail](../TOC.html)
•
[Next »](procthread.html)

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

**Previous page:** Previous Lesson
  
**Next page:** Processes and Threads




A browser with JavaScript enabled is required for this page to operate properly.