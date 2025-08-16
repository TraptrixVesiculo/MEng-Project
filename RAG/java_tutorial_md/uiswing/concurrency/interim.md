[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Creating a GUI With JFC/Swing
  
**Lesson:** Concurrency in Swing
  
**Section:** Worker Threads and SwingWorker

[Concurrency in Swing](index.html)

[Initial Threads](initial.html)

[The Event Dispatch Thread](dispatch.html)

[Worker Threads and SwingWorker](worker.html)

[Simple Background Tasks](simple.html)

Tasks that Have Interim Results

[Canceling Background Tasks](cancel.html)

[Bound Properties and Status Methods](bound.html)

[Home Page](../../index.html)
>
[Creating a GUI With JFC/Swing](../index.html)
>
[Concurrency in Swing](index.html)

[« Previous](simple.html) • [Trail](../TOC.html) • [Next »](cancel.html)

# Tasks that Have Interim Results

It is often useful for a background task to provide interim results
while it is still working. The task can do this by invoking
[`SwingWorker.publish`](http://download.oracle.com/javase/7/docs/api/javax/swing/SwingWorker.html#publish(V...)). This method accepts a variable number of arguments. Each argument
must be of the type specified by `SwingWorker`'s second
type parameter.

To collect results provided by `publish`, override
[`SwingWorker.process`](http://download.oracle.com/javase/7/docs/api/javax/swing/SwingWorker.html#process(java.util.List))
This method will be invoked from the event dispatch thread.
Results from multiple invocations of `publish` are often
accumulated for a single invocation of `process`.

Let's look at the way the
[`Flipper.java`](../examples/concurrency/FlipperProject/src/concurrency/Flipper.java)
example uses `publish` to provide interim results. Click the Launch
button to run `Flipper` using
[Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp)
([download
JDK 6](http://java.sun.com/javase/downloads/index.jsp)). Or, to compile and run the example yourself, consult
the [example
index](../examples/concurrency/index.html#Flipper).

[![Launches the Flipper example](../../images/jws-launch-button.png)](http://download.oracle.com/javase/tutorialJWS/uiswing/concurrency/ex6/Flipper.jnlp)

This program tests the fairness of
[`java.util.Random`](http://download.oracle.com/javase/7/docs/api/java/util/Random.html)
by generating a series of random `boolean` values in a
background task. This is equivalent to flipping a coin; hence the
name `Flipper`. To report its results, the background task
uses an object of type `FlipPair`

```

private static class FlipPair {
    private final long heads, total;
    FlipPair(long heads, long total) {
        this.heads = heads;
        this.total = total;
    }
}

```

The `heads` field is the number of times the random value
has been `true`; the `total` field is the total
number of random values.

The background task is represented by an instance of
`FlipTask`:

```

private class FlipTask extends SwingWorker<Void, FlipPair> {

```

Since the task does not return a final result, it does not matter what
the first type parameter is; `Void` is used as a
placeholder. The task invokes `publish` after each "coin
flip":

```

@Override
protected Void doInBackground() {
    long heads = 0;
    long total = 0;
    Random random = new Random();
    while (!isCancelled()) {
        total++;
        if (random.nextBoolean()) {
            heads++;
        }
        publish(new FlipPair(heads, total));
    }
    return null;
}

```

(The `isCancelled` method is discussed in the next
section.) Because `publish` is invoked very frequently, a
lot of `FlipPair` values will probably be accumulated
before `process` is invoked in the event dispatch thread;
`process` is only interested in the last value reported each
time, using it to update the GUI:

```

protected void process(List<FlipPair> pairs) {
    FlipPair pair = pairs.get(pairs.size() - 1);
    headsText.setText(String.format("%d", pair.heads));
    totalText.setText(String.format("%d", pair.total));
    devText.setText(String.format("%.10g", 
            ((double) pair.heads)/((double) pair.total) - 0.5));
}

```

If `Random` is fair, the value displayed in
`devText` should get closer and closer to 0 as
`Flipper` runs.

---

**Note:** The `setText` method used in `Flipper` is
actually "thread safe" as defined in its
[specification](http://download.oracle.com/javase/7/docs/api/javax/swing/text/JTextComponent.html#setText(java.lang.String)). That means that we could dispense with `publish` and
`process` and set the text fields directly from the
worker thread. We've chosen to ignore this fact in order to
provide a simple demonstration of `SwingWorker` interim
results.

---

[« Previous](simple.html)
•
[Trail](../TOC.html)
•
[Next »](cancel.html)

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

**Previous page:** Simple Background Tasks
  
**Next page:** Canceling Background Tasks




A browser with JavaScript enabled is required for this page to operate properly.