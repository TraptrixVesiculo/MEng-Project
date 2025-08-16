[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Essential Classes
  
**Lesson:** Concurrency
  
**Section:** Immutable Objects

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

A Strategy for Defining Immutable Objects

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

[« Previous](syncrgb.html) • [Trail](../TOC.html) • [Next »](highlevel.html)

# A Strategy for Defining Immutable Objects

The following rules define a simple strategy for creating immutable
objects. Not all classes documented as "immutable" follow these rules.
This does not necessarily mean the creators of these classes were
sloppy — they may have good reason for believing that instances
of their classes never change after construction. However, such
strategies require sophisticated analysis and are not for beginners.

1. Don't provide "setter" methods — methods that
   modify fields or objects referred to by fields.- Make all fields `final` and `private`.- Don't allow subclasses to override methods. The simplest way
       to do this is to declare the class as `final`. A more
       sophisticated approach is to make the constructor
       `private` and construct instances in factory methods.- If the instance fields include references to mutable objects,
         don't allow those objects to be changed:
         * Don't provide methods that modify the mutable objects.* Don't share references to the mutable objects. Never store
             references to external, mutable objects passed to the
             constructor; if necessary, create copies, and store references
             to the copies. Similarly, create copies of your internal
             mutable objects when necessary to avoid returning the
             originals in your methods.

Applying this strategy to `SynchronizedRGB` results in the
following steps:

1. There are two setter methods in this class. The first one,
   `set`, arbitrarily transforms the object, and has no
   place in an immutable version of the class. The second one,
   `invert`, can be adapted by having it create a new
   object instead of modifying the existing one.- All fields are already `private`; they are further
     qualified as `final`.- The class itself is declared `final`.- Only one field refers to an object, and that object is itself
         immutable. Therefore, no safeguards against changing the state of
         "contained" mutable objects are necessary.

After these changes, we have
[`ImmutableRGB`](examples/ImmutableRGB.java):

```


final public class ImmutableRGB {

    //Values must be between 0 and 255.
    final private int red;
    final private int green;
    final private int blue;
    final private String name;

    private void check(int red, int green, int blue) {
        if (red < 0 || red > 255
                || green < 0 || green > 255
                || blue < 0 || blue > 255) {
            throw new IllegalArgumentException();
        }
    }

    public ImmutableRGB(int red, int green, int blue, String name) {
        check(red, green, blue);
        this.red = red;
        this.green = green;
        this.blue = blue;
        this.name = name;
    }


    public int getRGB() {
        return ((red << 16) | (green << 8) | blue);
    }

    public String getName() {
        return name;
    }

    public ImmutableRGB invert() {
        return new ImmutableRGB(255 - red, 255 - green, 255 - blue, 
                "Inverse of " + name);
    }
}

```

[« Previous](syncrgb.html)
•
[Trail](../TOC.html)
•
[Next »](highlevel.html)

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

**Previous page:** A Synchronized Class Example
  
**Next page:** High Level Concurrency Objects




A browser with JavaScript enabled is required for this page to operate properly.