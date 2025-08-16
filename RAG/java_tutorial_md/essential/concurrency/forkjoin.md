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

[Executor Interfaces](exinter.html)

[Thread Pools](pools.html)

Fork/Join

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

[« Previous](pools.html) • [Trail](../TOC.html) • [Next »](collections.html)

# Fork/Join

New in the Java SE 7 release, the fork/join framework is an implementation of the
`ExecutorService` interface
that helps you take advantage of multiple processors. It is designed for
work that can be broken into smaller pieces recursively. The
goal is to use all the available processing power to make your
application wicked fast.

As with any `ExecutorService`, the fork/join framework distributes
tasks to worker threads in a thread pool. The fork/join
framework is distinct because it uses a *work-stealing* algorithm. Worker
threads that run out of things to do can steal tasks from other threads that are
still busy.

The center of the fork/join framework is the
[`ForkJoinPool`](http://download.oracle.com/javase/7/docs/api/java/util/concurrent/ForkJoinPool.html)class, an extension of `AbstractExecutorService`.
`ForkJoinPool`
implements the core work-stealing algorithm and can execute
[`ForkJoinTask`](http://download.oracle.com/javase/7/docs/api/java/util/concurrent/ForkJoinTask.html)s.

### Basic Use

Using the fork/join framework is simple. The first step is to write some code that performs
a segment of the work. Your code should look similar to this:

```

if (my portion of the work is small enough)
  do the work directly
else
  split my work into two pieces
  invoke the two pieces and wait for the results

```

Wrap this code as a `ForkJoinTask` subclass, typically as one of its more
specialized types
[`RecursiveTask`](http://download.oracle.com/javase/7/docs/api/java/util/concurrent/RecursiveTask.html)(which can return a result) or
[`RecursiveAction`](http://download.oracle.com/javase/7/docs/api/java/util/concurrent/RecursiveAction.html).

After your `ForkJoinTask` is ready, create one that represents
all the work to be done and pass it to the `invoke()` method
of a `ForkJoinPool` instance.

### Blurring for Clarity

To help you understand how the fork/join framework works, consider a simple example. Suppose
you want to perform a simple blur on an image. The original *source* image
is represented by an array of integers, where each integer contains the color
values for a single pixel. The blurred *destination* image is also
represented by an integer array with the same size as the source.

Performing the blur is accomplished by working through the source array one
pixel at a time. Each pixel is averaged with its surrounding pixels (the red,
green, and blue components are averaged), and the result is placed in the
destination array. Here is one possible implementation:

```

public class ForkBlur extends RecursiveAction {
  private int[] mSource;
  private int mStart;
  private int mLength;
  private int[] mDestination;
  
  private int mBlurWidth = 15; // Processing window size, should be odd.
  
  public ForkBlur(int[] src, int start, int length, int[] dst) {
    mSource = src;
    mStart = start;
    mLength = length;
    mDestination = dst;
  }

  protected void computeDirectly() {
    int sidePixels = (mBlurWidth - 1) / 2;
    for (int index = mStart; index < mStart + mLength; index++) {
      // Calculate average.
      float rt = 0, gt = 0, bt = 0;
      for (int mi = -sidePixels; mi <= sidePixels; mi++) {
        int mindex = Math.min(Math.max(mi + index, 0), mSource.length - 1);
        int pixel = mSource[mindex];
        rt += (float)((pixel & 0x00ff0000) >> 16) / mBlurWidth;
        gt += (float)((pixel & 0x0000ff00) >>  8) / mBlurWidth;
        bt += (float)((pixel & 0x000000ff) >>  0) / mBlurWidth;
      }
      
      // Re-assemble destination pixel.
      int dpixel = (0xff000000     ) |
                   (((int)rt) << 16) |
                   (((int)gt) <<  8) |
                   (((int)bt) <<  0);
      mDestination[index] = dpixel;
    }
  }
  
  .
  .
  .

```

Now you implement the abstract `compute()`
method, which either performs the blur directly or splits it into two smaller
tasks. A simple array length threshold helps determine whether the work is
performed or split.

```

  protected static int sThreshold = 100000;

  protected void compute() {
    if (mLength < sThreshold) {
      computeDirectly();
      return;
    }
    
    int split = mLength / 2;
    
    invokeAll(new ForkBlur(mSource, mStart,         split,           mDestination),
              new ForkBlur(mSource, mStart + split, mLength - split, mDestination));
  }

```

If the previous methods are in a subclass of the `RecursiveAction` class,
setting it up to run in a `ForkJoinPool` is straightforward.

Create a task that represents all of the work to be done.

```

// source image pixels are in src
// destination image pixels are in dst
ForkBlur fb = new ForkBlur(src, 0, src.length, dst);

```

Create the `ForkJoinPool` that will run the task.

```

ForkJoinPool pool = new ForkJoinPool();

```

Run the task.

```

pool.invoke(fb);

```

For the full source code, including some extra code that shows the source
and destination images in windows, see the
[`ForkBlur`](examples/ForkBlur.java)class.

[« Previous](pools.html)
•
[Trail](../TOC.html)
•
[Next »](collections.html)

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

**Previous page:** Thread Pools
  
**Next page:** Concurrent Collections




A browser with JavaScript enabled is required for this page to operate properly.