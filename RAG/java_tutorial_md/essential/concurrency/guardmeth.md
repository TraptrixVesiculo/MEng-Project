[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Essential Classes
  
**Lesson:** Concurrency

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

Guarded Blocks

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

[« Previous](starvelive.html) • [Trail](../TOC.html) • [Next »](immutable.html)

# Guarded Blocks

Threads often have to coordinate their actions. The most common
coordination idiom is the *guarded block*. Such a block begins
by polling a condition that must be true before the block can
proceed. There are a number of steps to follow in order to do this
correctly.

Suppose, for example `guardedJoy` is a method that must not
proceed until a shared variable `joy` has been set by
another thread. Such a method could, in theory, simply loop until the
condition is satisfied, but that loop is wasteful, since it executes
continuously while waiting.

```

public void guardedJoy() {
    //Simple loop guard. Wastes processor time. Don't do this!
    while(!joy) {}
    System.out.println("Joy has been achieved!");
}

```

A more efficient guard invokes
[`Object.wait`](http://download.oracle.com/javase/7/docs/api/java/lang/Object.html#wait())
to suspend the current thread. The invocation of `wait`
does not return until another thread has issued a notification that
some special event may have occurred — though not necessarily
the event this thread is waiting for:

```

public synchronized guardedJoy() {
    //This guard only loops once for each special event, which may not
    //be the event we're waiting for.
    while(!joy) {
        try {
            wait();
        } catch (InterruptedException e) {}
    }
    System.out.println("Joy and efficiency have been achieved!");
}

```

---

**Note:** Always invoke `wait` inside a loop that tests for the
condition being waited for. Don't assume that the interrupt was for
the particular condition you were waiting for, or that the condition
is still true.

---

Like many methods that suspend execution, `wait` can throw
`InterruptedException`. In this example, we can just ignore
that exception — we only care about the value of
`joy`.

Why is this version of `guardedJoy` synchronized? Suppose
`d` is the object we're using to invoke `wait`.
When a thread invokes `d.wait`, it must own the intrinsic
lock for `d` — otherwise an error is thrown. Invoking
`wait` inside a synchronized method is a simple way to
acquire the intrinsic lock.

When `wait` is invoked, the thread releases the lock and
suspends execution. At some future time, another thread will acquire
the same lock and invoke
[`Object.notifyAll`](http://download.oracle.com/javase/7/docs/api/java/lang/Object.html#notifyAll()), informing all threads waiting on that lock that something important
has happened:

```

public synchronized notifyJoy() {
    joy = true;
    notifyAll();
}

```

Some time after the second thread has released the lock, the first
thread reacquires the lock and resumes by returning from the
invocation of `wait`.

---

**Note:** There is a second notification method, `notify`, which
wakes up a single thread. Because `notify` doesn't allow
you to specify the thread that is woken up, it is useful only in
massively parallel applications — that is, programs with a large
number of threads, all doing similar chores. In such an application,
you don't care which thread gets woken up.

---

Let's use guarded blocks to create a *Producer-Consumer*
application. This kind of application shares data between two
threads: the *producer*, that creates the data, and the
*consumer*, that does something with it. The two threads
communicate using a shared object. Coordination is essential: the
consumer thread must not attempt to retrieve the data before the
producer thread has delivered it, and the producer thread must not
attempt to deliver new data if the consumer hasn't retrieved the old
data.

In this example, the data is a series of text messages, which are
shared through an object of type
[`Drop`](examples/Drop.java):

```


public class Drop {
    //Message sent from producer to consumer.
    private String message;
    //True if consumer should wait for producer to send message, false
    //if producer should wait for consumer to retrieve message.
    private boolean empty = true;

    public synchronized String take() {
        //Wait until message is available.
        while (empty) {
            try {
                wait();
            } catch (InterruptedException e) {}
        }
        //Toggle status.
        empty = true;
        //Notify producer that status has changed.
        notifyAll();
        return message;
    }

    public synchronized void put(String message) {
        //Wait until message has been retrieved.
        while (!empty) {
            try { 
                wait();
            } catch (InterruptedException e) {}
        }
        //Toggle status.
        empty = false;
        //Store message.
        this.message = message;
        //Notify consumer that status has changed.
        notifyAll();
    }
}

```

The producer thread, defined in
[`Producer`](examples/Producer.java), sends a series of familiar messages. The string "DONE" indicates
that all messages have been sent. To simulate the unpredictable nature
of real-world applications, the producer thread pauses for random
intervals between messages.

```


import java.util.Random;

public class Producer implements Runnable {
    private Drop drop;

    public Producer(Drop drop) {
        this.drop = drop;
    }

    public void run() {
        String importantInfo[] = {
            "Mares eat oats",
            "Does eat oats",
            "Little lambs eat ivy",
            "A kid will eat ivy too"
        };
        Random random = new Random();

        for (int i = 0; i < importantInfo.length; i++) {
            drop.put(importantInfo[i]);
            try {
                Thread.sleep(random.nextInt(5000));
            } catch (InterruptedException e) {}
        }
        drop.put("DONE");
    }
}


```

The consumer thread, defined in
[`Consumer`](examples/Consumer.java),
simply retrieves the messages and prints them out, until it retrieves
the "DONE" string. This thread also pauses for random intervals.

```


import java.util.Random;

public class Consumer implements Runnable {
    private Drop drop;

    public Consumer(Drop drop) {
        this.drop = drop;
    }

    public void run() {
        Random random = new Random();
        for (String message = drop.take(); ! message.equals("DONE");
                message = drop.take()) {
            System.out.format("MESSAGE RECEIVED: %s%n", message);
            try {
                Thread.sleep(random.nextInt(5000));
            } catch (InterruptedException e) {}
        }
    }
}
                


```

Finally, here is the main thread, defined in
[`ProducerConsumerExample`](examples/ProducerConsumerExample.java),
that launches the producer and consumer threads.

```


public class ProducerConsumerExample {
    public static void main(String[] args) {
        Drop drop = new Drop();
        (new Thread(new Producer(drop))).start();
        (new Thread(new Consumer(drop))).start();
    }
}

```

---

**Note:** The `Drop` class was written in order to demonstrate
guarded blocks. To avoid re-inventing the wheel, examine the existing
data structures in the
[Java Collections Framework](../../collections/index.html)
before trying to code your own data-sharing objects. For more
information, refer to the [Questions and
Exercises](QandE/questions.html) section.

---

[« Previous](starvelive.html)
•
[Trail](../TOC.html)
•
[Next »](immutable.html)

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

**Previous page:** Starvation and Livelock
  
**Next page:** Immutable Objects




A browser with JavaScript enabled is required for this page to operate properly.