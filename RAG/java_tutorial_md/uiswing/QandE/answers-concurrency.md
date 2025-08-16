[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)

**Trail:** Creating a GUI With JFC/Swing

[Home Page](../../index.html)
>
[Creating a GUI With JFC/Swing](../index.html)

[« Previous](../TOC.html) • [TOC](../TOC.html)

# Answers: Concurrency in Swing

### Questions

> Question 1:
> For each of the following tasks, specify which thread it should be
> executed in and why.
>   
>  Answer 1:
>
> * Initializing the GUI. The event
>   dispatch thread; most interactions with the GUI framework must
>   occur on this thread.* Loading a large file. A worker
>     thread. Executing this task on the event dispatch thread would
>     prevent GUI events from being processed, "freezing" the GUI until
>     the task is finished. Executing this task on an initial thread
>     would cause a delay in creating the GUI.* Invoking
>       [`javax.swing.JComponent.setFont`](http://download.oracle.com/javase/7/docs/api/javax/swing/JComponent.html#setFont(java.awt.Font)) to change the font of a component. The event dispatch
>       thread. As with most Swing methods, it is not safe to invoke
>       `setFont` from any other thread.* Invoking
>         [`javax.swing.text.JTextComponent.setText`](http://download.oracle.com/javase/7/docs/api/javax/swing/text/JTextComponent.html#setText(java.lang.String)) to change the text of a component. This method is
>         documented as thread-safe, so it can be invoked from any thread.
>
> Question 2:
> One thread is not the preferred thread for any of the tasks
> mentioned in the previous question. Name this thread and explain why
> its applications are so limited.
>   
>  Answer 2:
> The initial threads launch the first GUI task on the event dispatch
> thread. After that, a Swing program is primarily driven by GUI
> events, which trigger tasks on the event dispatch thread and the
> worker thread. Usually, the initial threads are left with nothing to do.
>
> Question 3:
> `SwingWorker` has two type parameters. Explain how
> these type parameters are used, and why it often doesn't matter what
> they are.
>   
>  Answer 3:
> The type parameters specify the type of the final result (also
> the return type of the `doInBackground` method) and the
> type of interim results (also the argument types for
> `publish` and `process`). Many background tasks
> do not provide final or interim results.

### Exercises

> Question 1:
> Modify the
> [`Flipper`](../examples/concurrency/FlipperProject/src/concurrency/Flipper.java) example so that it pauses 5 seconds between "coin flips." If the
> user clicks the "Cancel", the coin-flipping loop terminates
> immediately.
>   
>  Answer 1:
> See the source code for
> [`Flipper2`](../examples/QandE/Flipper2Project/src/QandE/Flipper2.java).
> The modified program adds a delay in the central
> `doInBackground` loop:
>
> ```
>
> protected Object doInBackground() {
>     long heads = 0;
>     long total = 0;
>     Random random = new Random();
>     while (!isCancelled()) {
>         try {
>             Thread.sleep(5000);
>         } catch (InterruptedException e) {
>             //Cancelled!
>             return null;
>         }
>         total++;
>         if (random.nextBoolean()) {
>             heads++;
>         }
>         publish(new FlipPair(heads, total));
>     }
>     return null;
> }
>
> ```
>
> The `try ... catch` causes `doInBackground` to
> return if an interrupt is received while the thread is sleeping.
> Invoking `cancel` with an argument of `true`
> ensures that an interrupt is sent when the task is cancelled.

[« Previous](../TOC.html)
•
[TOC](../TOC.html)


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

**Previous page:** Questions and Exercises: Concurrency in Swing




A browser with JavaScript enabled is required for this page to operate properly.