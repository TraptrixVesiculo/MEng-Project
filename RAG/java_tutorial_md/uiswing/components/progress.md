[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Creating a GUI With JFC/Swing
  
**Lesson:** Using Swing Components
  
**Section:** How to Use Various Components

[Using Swing Components](index.html)

[Using Top-Level Containers](toplevel.html)

[The JComponent Class](jcomponent.html)

[Using Text Components](text.html)

[Text Component Features](generaltext.html)

[The Text Component API](textapi.html)

[How to Use Various Components](componentlist.html)

[How to Make Applets](applet.html)

[How to Use Buttons, Check Boxes, and Radio Buttons](button.html)

[How to Use the ButtonGroup Component](buttongroup.html)

[How to Use Color Choosers](colorchooser.html)

[How to Use Combo Boxes](combobox.html)

[How to Make Dialogs](dialog.html)

[How to Use Editor Panes and Text Panes](editorpane.html)

[How to Use File Choosers](filechooser.html)

[How to Use Formatted Text Fields](formattedtextfield.html)

[How to Make Frames (Main Windows)](frame.html)

[How to Use Internal Frames](internalframe.html)

[How to Use Labels](label.html)

[How to Use Layered Panes](layeredpane.html)

[How to Use Lists](list.html)

[How to Use Menus](menu.html)

[How to Use Panels](panel.html)

[How to Use Password Fields](passwordfield.html)

How to Use Progress Bars

[How to Use Root Panes](rootpane.html)

[How to Use Scroll Panes](scrollpane.html)

[How to Use Separators](separator.html)

[How to Use Sliders](slider.html)

[How to Use Spinners](spinner.html)

[How to Use Split Panes](splitpane.html)

[How to Use Tabbed Panes](tabbedpane.html)

[How to Use Tables](table.html)

[How to Use Text Areas](textarea.html)

[How to Use Text Fields](textfield.html)

[How to Use Tool Bars](toolbar.html)

[How to Use Tool Tips](tooltip.html)

[How to Use Trees](tree.html)

[How to Use HTML in Swing Components](html.html)

[How to Use Models](model.html)

[How to Use Icons](icon.html)

[How to Use Borders](border.html)

[Solving Common Component Problems](problems.html)

[Home Page](../../index.html)
>
[Creating a GUI With JFC/Swing](../index.html)
>
[Using Swing Components](index.html)

[« Previous](passwordfield.html) • [Trail](../TOC.html) • [Next »](rootpane.html)

# How to Use Progress Bars

Sometimes a task running within a program
might take a while to complete.
A user-friendly program provides some
indication to the user
that the task is occurring,
how long the task might take, and
how much work has already been done.
One way of indicating work,
and perhaps the amount of progress,
is to use an animated image.

Another way of indicating work
is to set the wait cursor,
using the
[`Cursor`](http://download.oracle.com/javase/7/docs/api/java/awt/Cursor.html) class
and the `Component`-defined
[`setCursor`](http://download.oracle.com/javase/7/docs/api/java/awt/Component.html#setCursor(java.awt.Cursor)) method. For example, the following code
makes the wait cursor be displayed
when the cursor is over `container`
(including any components it contains
that have no cursor specified):

```

container.setCursor(Cursor.getPredefinedCursor(Cursor.WAIT_CURSOR));

```

To convey how complete a task is,
you can use a progress bar
like this one:
-->

![A typical progress bar](../../figures/uiswing/components/progressbar.png)

Sometimes you can't immediately determine
the length of a long-running task,
or the task might stay stuck at the same state of completion
for a long time. You can show work without measurable progress
by putting the progress bar in
*indeterminate mode.*
A progress bar in indeterminate mode displays animation
to indicate that work is occurring.
As soon as the progress bar can display more meaningful information,
you should switch it back into its default, determinate mode.
In the Java look and feel,
indeterminate progress bars
look like this:

![An indeterminate progress bar](../../figures/uiswing/components/indprogressbar.gif)

Swing provides three classes to help you
use progress bars:

[**`JProgressBar`**](http://download.oracle.com/javase/7/docs/api/javax/swing/JProgressBar.html): A visible component to graphically display how much of a total task has completed. See [Using Determinate Progress Bars](#bars) for information and an example of using a typical progress bar. The section [Using Indeterminate Mode](#indeterminate) tells you how to animate a progress bar to show activity before the task's scope is known. [**`ProgressMonitor`**](http://download.oracle.com/javase/7/docs/api/javax/swing/ProgressMonitor.html): *Not* a visible component. Instead, an instance of this class monitors the progress of a task and pops up a [dialog](dialog.html) if necessary. See [How to Use Progress Monitors](#monitors) for details and an example of using a progress monitor. [**`ProgressMonitorInputStream`**](http://download.oracle.com/javase/7/docs/api/javax/swing/ProgressMonitorInputStream.html): An input stream with an attached progress monitor, which monitors reading from the stream. You use an instance of this stream like any of the other input streams described in [Basic I/O](../../essential/io/index.html). You can get the stream's progress monitor with a call to `getProgressMonitor` and configure it as described in [How to Use Progress Monitors](#monitors).

After you see a progress bar and a progress monitor in action,
[Deciding Whether to Use a Progress Bar or a Progress Monitor](#deciding)
can help you figure out which is appropriate for your application.
### Using Determinate Progress Bars
> Here's a picture of a small demo application that
> uses a progress bar to measure the progress of a task
> that runs in its own thread:
>
> ![A snapshot of ProgressBarDemo, which uses a progress bar](../../figures/uiswing/components/ProgressBarDemo.png)
>
> ---
>
> **Try this:**
>
> * Click the Launch button to run the ProgressBar Demo using
>   [Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp) ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
>   Alternatively, to compile and run the example yourself,
>   consult the
>   [example index](../examples/components/index.html#ProgressBarDemo).
>
>   [![Launches the ProgressBar Demo example](../../images/jws-launch-button.png)](http://download.oracle.com/javase/tutorialJWS/uiswing/components/ex6/ProgressBarDemo.jnlp)
>
> ---


Below is the code from
[`ProgressBarDemo.java`](../examples/components/ProgressBarDemoProject/src/components/ProgressBarDemo.java  )
that creates and sets up the progress bar:

```

//Where member variables are declared:
JProgressBar progressBar;
...
//Where the GUI is constructed:
progressBar = new JProgressBar(0, task.getLengthOfTask());
progressBar.setValue(0);
progressBar.setStringPainted(true);

```

The constructor that creates the progress bar
sets the progress bar's minimum and maximum values.
You can also set these values with `setMinimum`
and `setMaximum`.
The minimum and maximum values used in this program are 0 and the
length of the task, which is typical of many programs and tasks.
However, a progress bar's minimum and maximum
values can be any value, even negative.
The code snippet also sets the progress bar's current value to 0.

The call to `setStringPainted`
causes the progress bar to display, within its bounds,
a textual indication of the percentage of the task that has completed.
By default, the progress bar displays the value
returned by its `getPercentComplete` method
formatted as a percent, such as **33%**.
Alternatively, you can replace the default with a different
string by calling `setString`. For example,

```

if (/*...half way done...*/)
    progressBar.setString("Half way there!");

```

When the user clicks **Start**, an instance of the inner class
`Task` is created and executed.

```

public void actionPerformed(ActionEvent evt) {
    startButton.setEnabled(false);
    setCursor(Cursor.getPredefinedCursor(Cursor.WAIT_CURSOR));
    done = false;
    task = new Task();
    task.addPropertyChangeListener(this);
    task.execute();
}

```

`Task` is a
subclass of
[`javax.swing.SwingWorker`](http://download.oracle.com/javase/7/docs/api/javax/swing/SwingWorker.html). The `Task` instance does three important things for
`ProgressBarDemo`:

1. The instance invokes the `doInBackground` in a
   separate thread. This is where the long-running task is actually
   executed. Using a background thread instead of the
   event-dispatching thread prevents the user interface from freezing
   while the task is running.- When the background task is complete, the instance invokes the
     `done` method in the event-dispatching thread.- The instance maintains a bound property,
       `progress`, that is updated to indicate the progress of
       the task. The `propertyChange` method is invoked each
       time `progress` changes.

See
[Worker Threads and SwingWorker](../concurrency/worker.html)
in
[Concurrency in Swing](../concurrency/index.html)
for more information about `SwingWorker`.

The background task in `ProgressBarDemo` simulates a real
task by reporting random amounts of progress at random intervals. The
`propertyChange` method responds to changes in the the
task's `progress` property by updating the progress bar:

```

public void propertyChange(PropertyChangeEvent evt) {
    if (!done) {
        int progress = task.getProgress();
        progressBar.setValue(progress);
        taskOutput.append(String.format(
                "Completed %d%% of task.\n", progress));
    }

```

When the background task is complete, the task's `done`
method resets the progress bar:

```

public void done() {
    //Tell progress listener to stop updating progress bar.
    done = true;
    Toolkit.getDefaultToolkit().beep();
    startButton.setEnabled(true);
    setCursor(null); //turn off the wait cursor
    progressBar.setValue(progressBar.getMinimum());
    taskOutput.append("Done!\n");
}

```

Note that the `done` method sets the `done`
field to `true`, preventing `propertyChange`
from making further updates to the progress bar. This is necessary
because the final updates to the `progress` property may
occcur after `done` is invoked.
### Using Indeterminate Mode
> In `ProgressBarDemo2` indeterminate mode is set until
> actual progress begins:
>
> ```
>
> public void propertyChange(PropertyChangeEvent evt) {
>     if (!done) {
>         int progress = task.getProgress();
>         if (progress == 0) {
>             progressBar.setIndeterminate(true);
>             taskOutput.append("No progress yet\n");
>         } else {
>             progressBar.setIndeterminate(false); 
>             progressBar.setString(null);
>             progressBar.setValue(progress);
>             taskOutput.append(String.format(
>                     "Completed %d%% of task.\n", progress));
>         }
>     }
> }
>
> ```
>
> The other changes in the code are related to string display.
> A progress bar that displays a string is likely to be taller
> than one that doesn't,
> and, as the demo designers, we've arbitarily decided that this progress bar
> should display a string only when it's in the default, determinate mode.
> However, we want to avoid the layout ugliness
> that might result if the progress bar changed height
> when it changed modes.
> Thus, the code leaves in the call to
> `setStringPainted(true)`
> but adds a call to `setString("")`
> so that no text will be displayed.
> Later, when the progress bar switches from indeterminate to determinate mode,
> invoking `setString(null)`
> makes the progress bar display its default string.
>
> One change we did *not* make
> was removing the call to `progressBar.setValue`
> from the `progress` event handler.
> The call doesn't do any harm because an indeterminate progress bar
> doesn't use its value property,
> except perhaps to display it in the status string.
> In fact, keeping the progress bar's data
> as up-to-date as possible is a good practice,
> since some look and feels might not support indeterminate mode.
>
> ---
>
> **Try this:**
>
> 1. Click the Launch button to run the ProgressBar2 Demo using
>    [Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp) ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
>    Alternatively, to compile and run the example yourself,
>    consult the
>    [example index](../examples/components/index.html#ProgressBarDemo2).
>
>    [![Launches the ProgressBar2 Demo example](../../images/jws-launch-button.png)](http://download.oracle.com/javase/tutorialJWS/uiswing/components/ex6/ProgressBarDemo2.jnlp)
>    - Push the **Start** button.
>      Note that the progress bar starts animating as soon as
>      the button is pressed,
>      and then switches back into
>      determinate mode (like ProgressBarDemo).
>
> ---


### How to Use Progress Monitors
> Now let's rewrite ProgressBarDemo to use a progress
> monitor instead of a progress bar.
> Here's a picture of the new demo program,
> ProgressMonitorDemo:
>
> ![A snapshot of ProgressMonitorDemo and a dialog brought up by a progress monitor](../../figures/uiswing/components/ProgressMonitorDemo.png)
>
>
>
> ---
>
> **Try this:**
>
> 1. Click the Launch button to run the ProgressMonitor Demo using
>    [Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp) ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
>    Alternatively, to compile and run the example yourself,
>    consult the
>    [example index](../examples/components/index.html#ProgressMonitorDemo).
>
>    [![Launches the ProgressMonitor Demo example](../../images/jws-launch-button.png)](http://download.oracle.com/javase/tutorialJWS/uiswing/components/ex6/ProgressMonitorDemo.jnlp)
>    - Push the **Start** button.
>      After a certain amount of time, the program displays a progress dialog.- Click the **OK** button.
>        Note that the task continues even though the dialog is gone.- Start another task. After the dialog pops up,
>          click the **Cancel** button.
>          The dialog goes away and the task stops.
>
> ---


A progress monitor cannot be used again, so a new
one must be created each time a new task is started.
This program creates a progress monitor each time the
user starts a new task with the **Start** button.

Here's the statement that creates the progress monitor:

```

progressMonitor = new ProgressMonitor(ProgressMonitorDemo.this,
                                      "Running a Long Task",
                                      "", 0, task.getLengthOfTask());

```

This code uses `ProgressMonitor`'s only constructor
to create the monitor and
initialize several arguments:

* The first argument provides the parent component to
  the dialog popped up by the progress monitor.* The second argument is a string that describes
    the nature of the task being monitored.
    This string is displayed on the dialog.
    see [The Progress Monitoring API](#api)
    for details about this argument.* The third argument is another string
      that provides a changeable status note.
      The example uses an empty string to indicate that
      the dialog should make space for a changeable status note,
      but that the note is initially empty.
      If you provide `null` for this argument,
      the note is omitted from the dialog.
      The example updates the note
      each time the `progress` property changes.
      It updates the monitor's current value at the same time:

      ```

      int progress = task.getProgress();
      String message = String.format("Completed %d%%.\n", progress);
      progressMonitor.setNote(message);
      progressMonitor.setProgress(progress);
      taskOutput.append(message);

      ```

      * The last two arguments provide the minimum and maximum
        values, respectively, for the progress bar displayed in the dialog.

By default, a progress monitor waits a minium of 500 milliseconds
before deciding whether to pop up the dialog. It also waits for the
progress to become more than the minimum value. If it calculates that
the task will take more than 2000 milliseconds to complete, the
progress dialog appears. To adjust the minimum waiting period, invoke
`setMillisToDecidedToPopup`. To adjust the minimum progress
time required for a dialog to appear, invoke
`setMillisToPopup`.

By the simple fact that this example uses a progress monitor,
it adds a feature that wasn't present in the version of the
program that uses a progress bar:
The user can cancel the task by clicking the **Cancel**
button on the dialog.
Here's the code in the example that checks
to see if the user canceled the task or if the task exited normally:

```

if (progressMonitor.isCanceled() || task.isDone()) {
    progressMonitor.close();
    Toolkit.getDefaultToolkit().beep();
    if (progressMonitor.isCanceled()) {
        task.cancel(true);
        taskOutput.append("Task canceled.\n");
    } else {
        taskOutput.append("Task completed.\n");
    }
    startButton.setEnabled(true);
}

```

Note that the progress monitor doesn't itself cancel the task.
It provides the GUI and API to allow the program to do so easily.
### Deciding Whether to Use a Progress Bar or a Progress Monitor
> Use a *progress bar* if:
>
> * You want more control over the configuration of the progress bar.
>   If you are working directly with a progress bar,
>   you can
>   set it to be indeterminate,
>   make it display vertically,
>   provide a string for it to display,
>   register change listeners on it, and
>   provide it with a bounded range model to control
>   the progress bar's minimum, maximum, and current values.* The program needs to display other components
>     along with the progress bar.* You need more than one progress bar.
>       With some tasks, you need to monitor more than one parameter.
>       For example, an installation program might monitor
>       disk space usage in addition to how many files
>       have been successfully installed.* You need to reuse the progress bar.
>         A progress bar can be reused; a progress monitor cannot.
>         Once the progress monitor has decided to display a dialog (or not),
>         the progress monitor cannot do it again.
>
> Use a *progress monitor* if:
>
> * You want an easy way to display progress
>   in a [dialog](dialog.html).* The running task is secondary and
>     the user might not be interested in the progress of the task.
>     Progress monitor provides a way for the user to
>     dismiss the dialog while the task is still running.* You want an easy way for the task to be cancelled.
>       Progress monitor provides a GUI for the user to cancel the task.
>       All you have to do is
>       call progress monitor's `isCanceled` method to find out
>       if the user pressed the **Cancel** button.* Your task displays a short message periodically while running.
>         The progress monitor dialog provides the `setNote`
>         method so that the task can provide further information about what
>         it's doing. For example, an installation task might report the
>         name of each file as it's installed.* The task might not take a long time to complete.
>           You decide at what point a running task is taking
>           long enough to warrant letting the user know about it.
>           Progress monitor won't pop up a dialog if the task completes
>           within the timeframe you set.
>
> If you decide to use a progress monitor *and*
> the task you are monitoring is reading from an input stream,
> use the
> [**`ProgressMonitorInputStream`**](http://download.oracle.com/javase/7/docs/api/javax/swing/ProgressMonitorInputStream.html) class.

### The Progress Monitoring API

> The following tables list the commonly used
> API for using progress bars and progress monitors.
> Because `JProgressBar` is a subclass of
> `JComponent`,
> other methods you are likely to call on a
> `JProgressBar`
> are listed in
> [The JComponent Class](jcomponent.html).
> Note that
> `ProgressMonitor` is a subclass of `Object`
> and is not a visual component.
>
> The API for monitoring progress
> falls into these categories:
>
> * [Creating the Progress Bar](#progressbarapi)* [Setting or Getting the Progress Bar's Constraints/Values](#contentsapi)* [Controlling the Progress Bar's Appearance](#looksapi)* [Creating the Progress Monitor](#progressmonapi)* [Configuring the Progress Monitor](#monitorapi)* [Terminating the Progress Monitor](#terminateapi)
>
> Creating the Progress Bar
>
> | Constructor | Purpose |
> | [JProgressBar()](http://download.oracle.com/javase/7/docs/api/javax/swing/JProgressBar.html#JProgressBar())   [JProgressBar(int, int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JProgressBar.html#JProgressBar(int, int)) | Create a horizontal progress bar. The no-argument constructor initializes the progress bar with a minimum and initial value of 0 and a maximum of 100. The constructor with two integer arguments specifies the minimum and maximum values. |
> | [JProgressBar(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JProgressBar.html#JProgressBar(int))   [JProgressBar(int, int, int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JProgressBar.html#JProgressBar(int, int, int)) | Create a progress bar with the specified orientation, which can be either `JProgressBar.HORIZONTAL` or `JProgressBar.VERTICAL`. The optional second and third arguments specify minimum and maximum values. |
> | [JProgressBar(BoundedRangeModel)](http://download.oracle.com/javase/7/docs/api/javax/swing/JProgressBar.html#JProgressBar(javax.swing.BoundedRangeModel)) | Create a horizontal progress bar with the specified range model. |
>
> Setting or Getting the Progress Bar's Constraints/Values
>
> | Method | Purpose |
> | [void setValue(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JProgressBar.html#setValue(int))   [int getValue()](http://download.oracle.com/javase/7/docs/api/javax/swing/JProgressBar.html#getValue()) | Set or get the current value of the progress bar. The value is constrained by the minimum and maximum values. |
> | [double getPercentComplete()](http://download.oracle.com/javase/7/docs/api/javax/swing/JProgressBar.html#getPercentComplete()) | Get the percent complete for the progress bar. |
> | [void setMinimum(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JProgressBar.html#setMinimum(int))   [int getMinimum()](http://download.oracle.com/javase/7/docs/api/javax/swing/JProgressBar.html#getMinimum()) | Set or get the minimum value of the progress bar. |
> | [void setMaximum(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JProgressBar.html#setMaximum(int))   [int getMaximum()](http://download.oracle.com/javase/7/docs/api/javax/swing/JProgressBar.html#getMaximum()) | Set or get the maximum value of the progress bar. |
> | [void setModel(BoundedRangeModel)](http://download.oracle.com/javase/7/docs/api/javax/swing/JProgressBar.html#setModel(javax.swing.BoundedRangeModel))   [BoundedRangeModel getModel()](http://download.oracle.com/javase/7/docs/api/javax/swing/JProgressBar.html#getModel()) | Set or get the model used by the progress bar. The model establishes the progress bar's constraints and values, so you can use it directly as an alternative to using the individual set/get methods listed above. |
>
> Controlling the Progress Bar's Appearance
>
> | Method | Purpose |
> | [void setIndeterminate(boolean)](http://download.oracle.com/javase/7/docs/api/javax/swing/JProgressBar.html#setIndeterminate(boolean)) | By specifying `true`, put the progress bar into indeterminate mode. Specifying `false` puts the progress bar back into its default, determinate mode. |
> | [void setOrientation(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JProgressBar.html#setOrientation(int))   [int getOrientation()](http://download.oracle.com/javase/7/docs/api/javax/swing/JProgressBar.html#getOrientation()) | Set or get whether the progress bar is vertical or horizontal. Acceptable values are `JProgressBar.VERTICAL` or `JProgressBar.HORIZONTAL`. |
> | [void setBorderPainted(boolean)](http://download.oracle.com/javase/7/docs/api/javax/swing/JProgressBar.html#setBorderPainted(boolean))   [boolean isBorderPainted()](http://download.oracle.com/javase/7/docs/api/javax/swing/JProgressBar.html#isBorderPainted()) | Set or get whether the progress bar has a border. |
> | [void setStringPainted(boolean)](http://download.oracle.com/javase/7/docs/api/javax/swing/JProgressBar.html#setStringPainted(boolean))   [boolean isStringPainted()](http://download.oracle.com/javase/7/docs/api/javax/swing/JProgressBar.html#isStringPainted()) | Set or get whether the progress bar displays a percent string. By default, the value of the percent string is the value returned by `getPercentComplete` formatted as a percent. You can set the string to be displayed with `setString`. |
> | [void setString(String)](http://download.oracle.com/javase/7/docs/api/javax/swing/JProgressBar.html#setString(java.lang.String))   [String getString()](http://download.oracle.com/javase/7/docs/api/javax/swing/JProgressBar.html#getString()) | Set or get the percent string. |
>
> Creating the Progress Monitor
>
> | Method or Constructor | Purpose |
> | [ProgressMonitor(Component, Object, String, int, int)](http://download.oracle.com/javase/7/docs/api/javax/swing/ProgressMonitor.html#ProgressMonitor(java.awt.Component, java.lang.Object, java.lang.String, int, int)) | Create a progress monitor. The `Component` argument is the parent for the monitor's dialog. The `Object` argument is a message to put on the [option pane](dialog.html) within the dialog. The value of this object is typically a `String`. The `String` argument is a changeable status note. The final two `int` arguments set the minimum and maximum values, respectively, for the progress bar used in the dialog. |
> | [ProgressMonitor getProgressMonitor()](http://download.oracle.com/javase/7/docs/api/javax/swing/ProgressMonitorInputStream.html#getProgressMonitor())  *(in `ProgressMonitorInputStream`)* | Gets a progress monitor that monitors reading from an input stream. |
>
> Configuring the Progress Monitor
>
> | Method | Purpose |
> | [void setMinimum(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JProgressBar.html#setMinimum(int))   [int getMinimum()](http://download.oracle.com/javase/7/docs/api/javax/swing/JProgressBar.html#getMinimum()) | Set or get the minimum value of the progress monitor. This value is used by the monitor to set up the progress bar in the dialog. |
> | [void setMaximum(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/JProgressBar.html#setMaximum(int))   [int getMaximum()](http://download.oracle.com/javase/7/docs/api/javax/swing/JProgressBar.html#getMaximum()) | Set or get the maximum value of the progress monitor. This value is used by the monitor to set up the progress bar in the dialog. |
> | [void setProgress(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/ProgressMonitor.html#setProgress(int)) | Update the monitor's progress. |
> | [`void setNote(String)`](http://download.oracle.com/javase/7/docs/api/javax/swing/ProgressMonitor.html#setNote(java.lang.String))   [String getNote()](http://download.oracle.com/javase/7/docs/api/javax/swing/ProgressMonitor.html#getNote()) | Set or get the status note. This note is displayed on the dialog. To omit the status note from the dialog, provide `null` as the third argument to the monitor's constructor. |
> | [void setMillisToDecideToPopup(int)](http://download.oracle.com/javase/7/docs/api/javax/swing/ProgressMonitor.html#setMillisToDecideToPopup(int))   [int getMillisToDecideToPopup()](http://download.oracle.com/javase/7/docs/api/javax/swing/ProgressMonitor.html#getMillisToDecideToPopup()) | Set or get the time after which the monitor should decide whether to popup a dialog. |
>
> Terminating the Progress Monitor
>
> | Method | Purpose |
> | [void close()](http://download.oracle.com/javase/7/docs/api/javax/swing/ProgressMonitor.html#close()) | Close the progress monitor. This disposes of the dialog. |
> | [boolean isCanceled()](http://download.oracle.com/javase/7/docs/api/javax/swing/ProgressMonitor.html#isCanceled()) | Determine whether the user pressed the **Cancel** button. |

### Examples that Monitor Progress

> This following examples use `JProgressBar` or
> `ProgressMonitor`.
>
> | Example | Where Described | Notes |
> | --- | --- | --- |
> | [`ProgressBarDemo`](../examples/components/index.html#ProgressBarDemo) | This section | Uses a basic progress bar to show progress on a task running in a separate thread. |
> | [`ProgressBarDemo2`](../examples/components/index.html#ProgressBarDemo2) | This section | Uses a basic progress bar to show progress on a task running in a separate thread. |
> | [`ProgressMonitorDemo`](../examples/components/index.html#ProgressMonitorDemo) | This section | Modification of the previous example that uses a progress monitor instead of a progress bar. |

[« Previous](passwordfield.html)
•
[Trail](../TOC.html)
•
[Next »](rootpane.html)

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

**Previous page:** How to Use Password Fields
  
**Next page:** How to Use Root Panes




A browser with JavaScript enabled is required for this page to operate properly.