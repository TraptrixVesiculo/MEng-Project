[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Creating a GUI With JFC/Swing
  
**Lesson:** Using Other Swing Features

[Using Other Swing Features](index.html)

[How to Integrate with the Desktop Class](desktop.html)

[How to Create Translucent and Shaped Windows](trans_shaped_windows.html)

[How to Decorate Components with JLayer](jlayer.html)

[How to Use Actions](action.html)

[How to Use Swing Timers](timer.html)

[How to Support Assistive Technologies](access.html)

[How to Use the Focus Subsystem](focus.html)

[How to Use Key Bindings](keybinding.html)

[How to Use Modality in Dialogs](modality.html)

[How to Print Tables](printtable.html)

How to Print Text

[How to Create a Splash Screen](splashscreen.html)

[How to Use the System Tray](systemtray.html)

[Solving Common Problems Using Other Swing Features](problems.html)

[Home Page](../../index.html)
>
[Creating a GUI With JFC/Swing](../index.html)
>
[Using Other Swing Features](index.html)

[« Previous](printtable.html) • [Trail](../TOC.html) • [Next »](splashscreen.html)

# How to Print Text

The `JTextComponent` class provides support
for printing text documents.
The `JTextComponent` API includes methods that
allow you to implement both basic and advanced printing tasks.
Supported formats include HTML, RTF, and plain text.
For common printing tasks such as simply printing a text document,
use the `print` method directly.
The `print` method
has several forms with various argument sets.
This method prepares your text document,
gets a corresponding `Printable` object,
and sends it to a printer.

If the default implementation of the `Printable` object
does not meet your needs, you
can customize the printing layout
by overriding the `getPrintable` method
to wrap the default `Printable`
or even replace it altogether.

The easiest way to print your text component is to call
the `print` method
without parameters. See the code example below.

```

try {
    boolean complete = textComponent.print();
    if (complete) {
        /* show a success message  */
        ...
    } else {
        /*show a message indicating that printing was cancelled */
        ...
    }
} catch (PrinterException pe) {
    /* Printing failed, report to the user */
    ...
}

```

When you call the `print` method
with no parameters, a print dialog is displayed, and then your text component
is printed interactively without a header or a footer.
The code example below shows the `print` method signature
with the complete set of arguments.

```

boolean complete = textComponent.print(MessageFormat headerFormat,
          		               MessageFormat footerFormat, 
                                       boolean showPrintDialog,
                                       PrintService service
			               PrintRequestAttributeSet attributes,
                                       boolean interactive);

```

When you call the `print` method with all arguments,
you explicitly choose printing features such as
header and footer text, printing attributes, a destination print service,
and also whether to show a print dialog or not,
and whether to print interactively or non-interactively.
To decide which parameters suit your needs best,
see the description of available features below.

The `JTextComponent` printing API provides the following features:

* [Printing Interactively or Non-interactively](#interactively)* [Displaying a Print Dialog](#dialog)* [Adding a Header or a Footer (or Both) to a Printing Layout](#header)* [Automatic Layout and Pagination](#layout)

### Printing Interactively or Non-interactively

> In interactive mode
> a progress dialog with an abort option
> is shown for the duration of printing.
> Here is a sample of a progress dialog.
>
> ![A screenshot of a printing progress dialog](../../figures/uiswing/misc/PrintingProgress.png)
>
> This dialog allows the user to keep track of printing progress.
> The progress dialog is modal when the `print` method is called
> on the event dispatch thread and non-modal otherwise.
> It is important that your document
> remain unchanged while being printed, otherwise
> the printing behavior is undefined.
> The `print` method
> ensures that your document will not be changed and
> disables the component for the duration of printing.
>
> If you call the `print` method on the event dispatch thread
> in non-interactive mode, then all events including repaints will be blocked.
> That is why printing non-interactively on EDT is only recommended
> for applications with non-visible GUI.

### Print Dialog

> You can display a standard print dialog
> which allows the user to do the following:
>
> * Select a printer* Specify number of copies* Change printing attributes* Cancel printing before it has been started* Start printing
>
> ![A screenshot of a printing dialog](../../figures/uiswing/misc/PrintingDialog.png)
>
> You may notice that the print dialog does not specify
> the total number of pages in the printout. This is because
> the text printing implementation uses the `Printable` API
> and the total number of pages is not known before printing time.

### Adding a Header or a Footer (or Both) to a Printing Layout

> Headers and footers are provided by
> [`MessageFormat`](http://download.oracle.com/javase/7/docs/api/java/text/MessageFormat.html) parameters. These parameters allow the header and footer to be localized.
> Read the documentation for the
> [`MessageFormat`](http://download.oracle.com/javase/7/docs/api/java/text/MessageFormat.html) class as characters such as single quotes are special
> and need to be avoided.
> Both headers and footers are centered.
> You can insert a page number by using `{0}`.
>
> `MessageFormat footer = new MessageFormat("Page - {0}");`
>
> Since the total number of pages in the output is not known
> before printing time,
> there is no way to specify a numbering format
> like "Page 1 of 5".

### Automatic Layout and Pagination

> With the use of the `JTextComponent` printing API you do not need
> to take care of layout and pagination.
> Both layout and pagination are done automatically.
> The document content is formatted to fit the page size
> and spreads across multiple pages.
> You only need to specify an appropriate footer text format
> to the `print` method
> if you want to insert a page number in the footer.
> As demonstrated earlier, you can specify the page number in your footer by including
> `"{0}"` in the string given to the `MessageFormat`
> footer parameter. In the printed output,
> {0} will be replaced by the current page number.

### Text Area Printing Example

> Let us look at an example called `TextAreaPrintingDemo`.
> The main feature of this demo is printing a text document
> either on the event dispatch thread
> or on a background thread depending on the user's choice.
> This demo displays a text area, allows to select several printing features,
> and prints the text area's content
> according to the selected options.
> The entire code for this program can be found in
> [`TextAreaPrintingDemo.java`](../examples/misc/TextAreaPrintingDemoProject/src/misc/TextAreaPrintingDemo.java).
> This demo's rich GUI is built in the
> [NetBeans IDE GUI builder](http://netbeans.org/kb/docs/java/quickstart-gui.html).
> Here is a picture of the `TextAreaPrintingDemo` application.
>
> ![A screenshot of TextAreaPrintingDemo](../../figures/uiswing/misc/TextAreaPrintingDemo.png)
>
> ---
>
> **Try this:**
>
> 1. Click the Launch button
>    to run TextAreaPrintingDemo
>    using
>    [Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp ) 
>    ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
>    Alternatively, to compile and run the example yourself,
>    consult the [example index](../examples/misc/index.html#TextAreaPrintingDemo).
>
>    [![Launches the TextAreaPrintingDemo Application](../../images/jws-launch-button.png)](http://download.oracle.com/javase/tutorialJWS/uiswing/misc/ex6/TextAreaPrintingDemo.jnlp)
>
>    - Edit the text in the Header or Footer checkboxes or both
>      to provide a different header or footer.- Clear the Show Progress Dialog checkbox if you want
>        to print without displaying a progress dialog,
>        which means printing non-interactively. Note that
>        you will not be able to cancel printing once it has been started.- Clear the Print in Background checkbox to select printing
>          on the event dispatch thread. Note that printing on EDT non-interactively
>          will make your application unresponsive — interaction with
>          your application will be blocked for the duration of the printing process.- Click the Print button to print the text area's content
>            according to the selected options.
>
> Whenever a web-launched application tries to print,
> Java Web Start opens up a security dialog
> asking the user for permission to print
> unless this permission has already been granted in the system settings.
> To proceed with printing the user has to accept the request.
>
> An action listener is registered for the Print button.
> As the user clicks the Print button the `actionPerformed` method
> calls the `print` method, which
> initiates a printing task.
> The printing task is a `SwingWorker` object.
> The code example below shows how the `PrintingTask` class is implemented.
>
> ```
>
> private class PrintingTask extends SwingWorker {
>         private final MessageFormat headerFormat;
>         private final MessageFormat footerFormat;
>         private final boolean interactive;
>         private volatile boolean complete = false;
>         private volatile String message;
>         
>         public PrintingTask(MessageFormat header, MessageFormat footer,
>                             boolean interactive) {
>             this.headerFormat = header;
>             this.footerFormat = footer;
>             this.interactive = interactive;
>         }
>         
>         @Override
>         protected Object doInBackground() {
>             try {
>                 complete = text.print(headerFormat, footerFormat,
>                         true, null, null, interactive);
>                 message = "Printing " + (complete ? "complete" : "canceled");
>             } catch (PrinterException ex) {
>                 message = "Sorry, a printer error occurred";
>             } catch (SecurityException ex) {
>                 message =
>                     "Sorry, cannot access the printer due to security reasons";
>             }
>             return null;
>         }
>         
>         @Override
>         protected void done() {
>             message(!complete, message);
>         }
>     }
>
> ```
>
> The code example below shows how the `print` method
> obtains the set of selected options from the GUI components,
> then creates an instance of the `PrintingTask` class,
> and performs printing.
>
> ```
>
> private void print(java.awt.event.ActionEvent evt) {
>         MessageFormat header = createFormat(headerField);
>         MessageFormat footer = createFormat(footerField);
>         boolean interactive = interactiveCheck.isSelected();
>         boolean background = backgroundCheck.isSelected();
>
>         PrintingTask task = new PrintingTask(header, footer, interactive);
> 	if (background) {
>             task.execute();
>         } else {
>             task.run()
>         }
>     }
>
> ```
>
> The code in bold illustrates how `PrintingTask`'s methods are invoked
> depending on the `background` parameter's value.
> Whenever the user prefers to print on a background thread,
> the `execute` method is called, which schedules the printing task
> for the execution on a background thread.
> Otherwise the `run` method
> performs the printing task on EDT.
>
> Since printing large documents is a time-consuming task,
> it is recommended to perform printing on a background thread.

### Text Batch Printing Example

> The `TextBatchPrintingDemo` example illustrates printing non-visible
> HTML text documents on background threads.
> When launched, this demo displays a page with a list of URLs.
> You can visit an HTML page, add the displayed page to the print list,
> and once you select all pages that you need,
> you can print them all at once on background threads.
> The entire code for this program can be found in
> [`TextBatchPrintingDemo.java`](../examples/misc/TextBatchPrintingDemoProject/src/misc/TextBatchPrintingDemo.java).
> Here is a picture of the `TextBatchPrintingDemo` application.
>
> ![A screenshot of TextBatchPrintingDemo](../../figures/uiswing/misc/TextBatchPrintingDemo.png)
>
> ---
>
> **Try this:**
>
> 1. Click the Launch button
>    to run TextBatchPrintingDemo
>    using
>    [Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp ) 
>    ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
>    Alternatively, to compile and run the example yourself,
>    consult the [example index](../examples/misc/index.html#TextBatchPrintingDemo).
>
>    [![Launches the TextBatchPrintingDemo Application](../../images/jws-launch-button.png)](http://download.oracle.com/javase/tutorialJWS/uiswing/misc/ex6/TextBatchPrintingDemo.jnlp)
>
>    - Click on any link to view the corresponding HTML page.- Press ALT+A or choose File > Add Page menu item
>        to add the displayed page to a print list shown on the right.- Press ALT+H or choose File > Home Page menu item
>          to return to the demo's home page.- Add as many pages to the print list as you need.- Press ALT+C or choose File > Clear Selected menu item
>              if you need to clear the print list and build at again.- Press ALT+P or choose File > Print Selected menu item
>                to print the selected pages.- Press ALT+Q or choose File > Quit menu item
>                  to quit the application.
>
> You can find the printing code in the `printSelectedPages` method.
> When called, this method first obtains the amount of pages selected for printing.
> The code example below shows how
> the `printSelectedPages` method
> creates a `Runnable` object for each page and then prints
> the current page on a separate thread.
>
> ```
>
> for (int i = 0; i < n; i++) {
>     final PageItem item = (PageItem) pages.getElementAt(i);
>     // This method is called from EDT.  Printing is a time-consuming
>     // task, so it should be done outside EDT, in a separate thread.
>     Runnable printTask = new Runnable() {
>         public void run() {
>             try {
>                 item.print(
>                         // Two "false" args mean "no print dialog" and
>                         // "non-interactive" (ie, batch-mode printing).
>                                 null, null, false, printService, null, false);
>             } catch (PrinterException pe) {
>                 JOptionPane.showMessageDialog(null,
>                         "Error printing " + item.getPage() + "\n" + pe,
>                         "Print Error", JOptionPane.WARNING_MESSAGE);
>             }
>         }
>     };
>     new Thread(printTask).start();
>
> ```

### Text Printing API

> This section lists methods defined in the `JTextComponent` class
> that allow you to print text documents.
>
> | Method | Purpose |
> | --- | --- |
> | [boolean print()](http://download.oracle.com/javase/7/docs/api/javax/swing/text/JTextComponent.html#print())   [boolean print(MessageFormat, MessageFormat)](http://download.oracle.com/javase/7/docs/api/javax/swing/text/JTextComponent.html#print(java.text.MessageFormat, java.text.MessageFormat))   [boolean print(MessageFormat, MessageFormat, boolean, PrintRequestAttributeSet, boolean, PrintService)](http://download.oracle.com/javase/7/docs/api/javax/swing/text/JTextComponent.html#print(java.text.MessageFormat, java.text.MessageFormat, boolean, javax.print.PrintService, javax.print.attribute.PrintRequestAttributeSet, boolean)) | When called without arguments, displays a print dialog, and then prints this text component interactively without a header or a footer text. Returns `true` if the user continued printing and `false` if the user cancelled printing.   When called with the two `MessageFormat` arguments, displays a print dialog, and then prints this text component interactively with the specified header and footer text.   When called with a full set of arguments, prints this text component according to the specified arguments. The two `MessageFormat` arguments specify header and footer text. The first boolean argument defines whether to show a print dialog or not. Another boolean argument specifies whether to print interactively or not. With two other arguments you can specify printing attributes and a print service.   Whenever a `PrintService` argument is omitted, the default printer will be used. |
> | [Printable getPrintable(MessageFormat, MessageFormat)](http://download.oracle.com/javase/7/docs/api/javax/swing/text/JTextComponent.html#getPrintable(java.text.MessageFormat, java.text.MessageFormat)) | Returns a `Printable` object for printing your text component. Override this method to get a customized Printable object. You can wrap one Printable object into another in order to obtain complex reports and documents. |

### Examples That Use Text Printing

> This table lists examples that use text printing
> and points to where those examples are described.
>
> | Example | Where Described | Notes |
> | --- | --- | --- |
> | [`TextAreaPrintingDemo`](../examples/misc/index.html#TextAreaPrintingDemo) | This page | Demonstrates the basics of text printing and provides a rich GUI. Allows the user to specify header or footer text, turn the print dialog on or off, select printing interactively or non-interactively, and then print according to the selected options. |
> | [`TextBatchPrintingDemo`](../examples/misc/index.html#TextBatchPrintingDemo) This page | This demo displays a text component with a list of URLs, allows the user to view HTML pages, add them to the print list, and print all selected pages at once on background threads. | |

[« Previous](printtable.html)
•
[Trail](../TOC.html)
•
[Next »](splashscreen.html)

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

**Previous page:** How to Print Tables
  
**Next page:** How to Create a Splash Screen




A browser with JavaScript enabled is required for this page to operate properly.