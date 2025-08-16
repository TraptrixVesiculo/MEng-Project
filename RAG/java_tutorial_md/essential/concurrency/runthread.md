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

Defining and Starting a Thread

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

[Home Page](../../index.html)
>
[Essential Classes](../index.html)
>
[Concurrency](index.html)

[« Previous](threads.html) • [Trail](../TOC.html) • [Next »](sleep.html)

# Defining and Starting a Thread

An application that creates an instance of `Thread` must provide
the code that will run in that thread. There are two ways to do this:

* *Provide a `Runnable` object.* The
  [`Runnable`](http://download.oracle.com/javase/7/docs/api/java/lang/Runnable.html)
  interface defines a single method, `run`, meant to
  contain the code executed in the thread. The `Runnable`
  object is passed to the `Thread` constructor, as in the
  [`HelloRunnable`](examples/HelloRunnable.java)
  example:

  ```


  public class HelloRunnable implements Runnable {

      public void run() {
          System.out.println("Hello from a thread!");
      }

      public static void main(String args[]) {
          (new Thread(new HelloRunnable())).start();
      }

  }

  ```

  * *Subclass `Thread`.* The `Thread`
    class itself implements `Runnable`, though its
    `run` method does nothing. An application can subclass
    `Thread`, providing its own implementation of
    `run`, as in the
    [`HelloThread`](examples/HelloThread.java)
    example:

    ```


    public class HelloThread extends Thread {

        public void run() {
            System.out.println("Hello from a thread!");
        }

        public static void main(String args[]) {
            (new HelloThread()).start();
        }

    }

    ```

Notice that both examples invoke `Thread.start` in order to
start the new thread.

Which of these idioms should you use? The first idiom, which employs a
`Runnable` object, is more general, because the
`Runnable` object can subclass a class other than
`Thread`. The second idiom is easier to use in simple
applications, but is limited by the fact that your task class must be
a descendant of `Thread`. This lesson focuses on the first
approach, which separates the `Runnable` task from the
`Thread` object that executes the task. Not only is this
approach more flexible, but it is applicable to the high-level thread
management APIs covered later.

The `Thread` class defines a number of methods useful for
thread management. These include `static` methods, which
provide information about, or affect the status of, the thread
invoking the method. The other methods are invoked from other threads
involved in managing the thread and `Thread` object. We'll
examine some of these methods in the following sections.

[« Previous](threads.html)
•
[Trail](../TOC.html)
•
[Next »](sleep.html)

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

**Previous page:** Thread Objects
  
**Next page:** Pausing Execution with Sleep




A browser with JavaScript enabled is required for this page to operate properly.