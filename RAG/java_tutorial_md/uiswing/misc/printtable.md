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

How to Print Tables

[How to Print Text](printtext.html)

[How to Create a Splash Screen](splashscreen.html)

[How to Use the System Tray](systemtray.html)

[Solving Common Problems Using Other Swing Features](problems.html)

[Home Page](../../index.html)
>
[Creating a GUI With JFC/Swing](../index.html)
>
[Using Other Swing Features](index.html)

[« Previous](modality.html) • [Trail](../TOC.html) • [Next »](printtext.html)

# How to Print Tables

The `JTable` class provides support
for printing tables.
The `JTable` printing API includes methods
that allow you to implement
both basic and advanced printing tasks.
For common printing tasks, when you need to simply print a table,
use the `print` method directly.
The `print` method
has several forms with various argument sets.
This method prepares your table, gets a corresponding `Printable` object,
and sends it to a printer.

If the default implementation of the `Printable` object
does not meet your needs, you
can customize the printing layout
by overriding the `getPrintable` method
to wrap the default `Printable`
or even replace it altogether.

The easiest way to print your table is to call the `print` method
without parameters. See the code example below.

```

try {
    boolean complete = table.print();
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
with no parameters, a print dialog is displayed, and then your table
is printed interactively in the `FIT_WIDTH` mode
without a header or a footer.
The code example below shows the `print` method signature
with the complete set of arguments.

```

boolean complete = table.print(JTable.PrintMode printMode,
                               MessageFormat headerFormat,
          		       MessageFormat footerFormat, 
                               boolean showPrintDialog,
                               PrintRequestAttributeSet attr,
                               boolean interactive,
                               PrintService service);

```

When you call the `print` method with all arguments,
you explicitly choose printing features such as a printing mode,
a header and a footer text, printing attributes, a destination print service,
and also whether to show a print dialog or not,
and whether to print interactively or non-interactively.
To decide which parameters suit your needs best,
see the description of available features below.

The `JTable` printing API provides the following features:

* [Printing Interactively or Non-interactively](#interactively)* [Displaying a Print Dialog](#dialog)* [Adding a Header or a Footer (or Both) to a Printing Layout](#header)* [Selecting a Printing Mode](#mode)* [Automatic Layout and Pagination](#layout)

### Printing Interactively or Non-interactively

> In interactive mode
> a progress dialog with an abort option
> is shown for the duration of printing.
> Here is a sample of a progress dialog.
>
> ![A screenshot of a printing progress dialog](../../figures/uiswing/misc/PrintingProgress.png)
>
> This dialog enables the user to keep track of printing progress.
> The progress dialog is modal, which means that
> while it is shown on the screen,
> the user cannot interact with the table.
> It is important that your table remain unchanged while it is being printed,
> otherwise the printing behavior will be undefined.
> Nevertheless, printing interactively does not block other developer's code from
> changing the table. For example, there is another thread that posts updates using
> the `SwingUtilities.invokeLater` method.
> Therefore, to ensure correct printing behavior,
> you should be sure that your own code
> refrains from modifying the table during printing.
>
> Alternatively, you can print your table non-interactively.
> In this mode, printing begins immediately on the event dispatch thread
> and completely blocks any events to be processed.
> On the one hand, this mode securely keeps the table against any changes
> until printing is done. On the other hand,
> this mode completely deprives the user of any interaction with the GUI.
> That is why printing non-interactively can only be recommended
> when printing from applications with non-visible GUI.

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
> the table printing implementation uses the `Printable` API
> and the total number of pages is not known ahead of printing time.

### Adding a Header or a Footer (or Both) to a Printing Layout

> Headers and footers are provided by
> [`MessageFormat`](http://download.oracle.com/javase/7/docs/api/java/text/MessageFormat.html) parameters. These parameters allow the header and footer to be localized.
> Read the documentation for the
> [`MessageFormat`](http://download.oracle.com/javase/7/docs/api/java/text/MessageFormat.html) class, as some characters, such as single quotes, are special
> and need to be avoided.
> Both headers and footers are centered.
> You can insert a page number by using {0}.
>
> `MessageFormat footer = new MessageFormat("Page - {0}");`
>
> Since the total number of pages in the output is not known
> before printing time,
> there is no way to specify a numbering format
> like "Page 1 of 5".

### Printing Modes

> Printing modes are responsible for scaling the output
> and spreading it across pages.
> You can print your table in one of the following modes:
>
> * `PrintMode.NORMAL`* `PrintMode.FIT_WIDTH`
>
> In the `NORMAL` mode
> a table is printed at its current size. If columns do not fit a page, they
> spread across additional pages according to the table's
> `ComponentOrientation`.
> In the `FIT_WIDTH` mode a table has a smaller size, if necessary,
> to fit all columns on each page. Note that both width and height are scaled
> to provide an output of the same aspect ratio.
> In both modes rows spread across multiple pages sequentially with as many
> rows on a page as possible.

### Automatic Layout and Pagination

> With the use of the `JTable` printing API you do not need
> to take care of layout and pagination. You only need to specify appropriate parameters
> to the `print` method such as printing mode and footer text format
> (if you want to insert the page number in the footer).
> As demonstrated earlier, you can specify the page number in your footer by including
> `"{0}"` in the string given to the `MessageFormat`
> footer parameter. In the printed output,
> {0} will be replaced by the current page number.

### Table Printing Examples

> Let us look at an example called `TablePrintDemo1`.
> The entire code for this program can be found in
> [`TablePrintDemo1.java`](../examples/misc/TablePrintDemo1Project/src/misc/TablePrintDemo1.java).
> This demo's rich GUI is built automatically by the
> [NetBeans IDE GUI builder](http://netbeans.org/kb/docs/java/quickstart-gui.html).
> Here is a picture of the `TablePrintDemo1` application.
>
> ![A screenshot of TablePrintDemo1](../../figures/uiswing/misc/TablePrintDemo1.png)
>
> ---
>
> **Try this:**
>
> 1. Click the Launch button
>    to run TablePrintDemo1
>    using
>    [Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp ) 
>    ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
>    Alternatively, to compile and run the example yourself,
>    consult the [example index](../examples/misc/index.html#TablePrintDemo1).
>
>    [![Launches the TablePrintDemo1 Application](../../images/jws-launch-button.png)](http://download.oracle.com/javase/tutorialJWS/uiswing/misc/ex6/TablePrintDemo1.jnlp)
>
>    - Each checkbox in the bottom part of the application window has a tool tip.
>      Hold the cursor over
>      a checkbox to find out its purpose.- Edit the text in the Header or Footer checkboxes or both
>        to provide a different header or footer.- Clear the Header or Footer checkboxes or both to turn the header or footer off.- Clear the Show print dialog checkbox to turn the print dialog off.- Clear the Fit width to printed page checkbox
>              to select printing in the `NORMAL` mode.- Clear the Interactive (Show status dialog) checkbox to turn the print dialog off.- Click the Print button to print the table according to the selected options.
>
> Whenever a web-launched application tries to print, Java Web Start
> pops up a security dialog asking the user for permission to print.
> To proceed with printing, the user has to accept the request.
>
> Note when you clear the Interactive checkbox, a message appears that warns the user
> about the disadvantage of printing non-interactively.
> You can find the printing code in the `PrintGradesTable` method.
> When called, this method first obtains the set of selected options
> from the GUI components and then calls the `print` method as follows.
>
> ```
>
> boolean complete = gradesTable.print(mode, header, footer,
>                                      showPrintDialog, null,
>                                      interactive, null);
>
> ```
>
> The value returned by the `print` method is then used to show either
> the success message or the message saying that the user cancelled printing.
>
> Another important feature is
> the table printing API's use of table renderers.
> By using the table's renderers,
> the API provides a printed output
> that looks like the table on the screen.
> Look at the last column of the table on the screen.
> It contains custom images denoting the passed or failed status of each student.
> Now look at the printed result.
> You can see that the check and X marks look the same.
>
> Here is a picture of the TablePrintDemo1 printed result in the `FIT_WIDTH` mode.
>
> [![Printed output from the TablePrintDemo1 example](../../figures/uiswing/../../figures/uiswing/misc/TablePrintDemo1_out.png)](../../figures/uiswing/../../figures/uiswing/misc/TablePrintDemo1_out.png)  
> *This figure has been reduced to fit on the page.   
>  Click the image to view it at its natural size.*

#### TablePrintDemo2 Example

> The `TablePrintDemo2` example is based on the previous demo
> and has an identical interface. The only difference is in the printed output.
> If you look at the TablePrintDemo1's printed result more attentively,
> you may notice that the check and X marks are fuzzy.
> The `TablePrintDemo2` example shows
> how to customize the table
> to make the images more distinguishable in the table printout.
> In this demo, the overridden `getTableCellRendererComponent` method
> finds out whether the table is being printed
> and returns clearer black and white images.
> If the table is not being printed,
> it returns colored images that you can see on the screen.
>
> Click the Launch button
> to run TablePrintDemo2
> using
> [Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp ) 
> ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
> Alternatively, to compile and run the example yourself,
> consult the [example index](../examples/misc/index.html#TablePrintDemo2).
>
> [![Launches the TablePrintDemo2 Application](../../images/jws-launch-button.png)](http://download.oracle.com/javase/tutorialJWS/uiswing/misc/ex6/TablePrintDemo2.jnlp)
>
> The
> [`isPaintingForPrint`](http://download.oracle.com/javase/7/docs/api/javax/swing/JComponent.html#isPaintingForPrint())
> method defined in the `JComponent` class
> allows us to customize what we print
> compared with what we see on the screen.
> The code of the custom cell renderer, taken from
> [`TablePrintDemo2.java`](../examples/misc/TablePrintDemo2Project/src/misc/TablePrintDemo2.java), is listed below. This code chooses which images to use
> depending on the value returned by the `isPaintingForPrint` method.
>
> ```
>
>     /**
>      * A custom cell renderer that extends TablePrinteDemo1's renderer, to instead
>      * use clearer black and white versions of the icons when printing.
>      */
>     protected static class BWPassedColumnRenderer extends PassedColumnRenderer {
>             public Component getTableCellRendererComponent(JTable table,
>                                                            Object value,
>                                                            boolean isSelected,
>                                                            boolean hasFocus,
>                                                            int row,
>                                                            int column) {
>
>             super.getTableCellRendererComponent(table, value, isSelected,
>                                                 hasFocus, row, column);
>
>             /* if we're currently printing, use the black and white icons */
>             if (table.isPaintingForPrint()) {
>                 boolean status = (Boolean)value;
>                 setIcon(status ? passedIconBW : failedIconBW);
>             } /* otherwise, the superclass (colored) icons are used */
>
>             return this;
>         }
>     }
>
> ```
>
> Here is a picture of the TablePrintDemo2 printed result in the `FIT_WIDTH` mode.
>
> [![Printed output of the TablePrintDemo2 example](../../figures/uiswing/../../figures/uiswing/misc/TablePrintDemo2_out.png)](../../figures/uiswing/../../figures/uiswing/misc/TablePrintDemo2_out.png)  
> *This figure has been reduced to fit on the page.   
>  Click the image to view it at its natural size.*

#### TablePrintDemo3 Example

> The `TablePrintDemo3` example is based on the two previous demos.
> This example shows how to provide a customized `Printable` implementation
> by wrapping the default `Printable` with extra decoration.
> This demo has a similar interface but the Header and Footer checkboxes
> are disabled since the customized printable object
> will provide its own header and footer.
>
> Click the Launch button
> to run TablePrintDemo3
> using
> [Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp ) 
> ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
> Alternatively, to compile and run the example yourself,
> consult the [example index](../examples/misc/index.html#TablePrintDemo3).
>
> [![Launches the TablePrintDemo3 Application](../../images/jws-launch-button.png)](http://download.oracle.com/javase/tutorialJWS/uiswing/misc/ex6/TablePrintDemo3.jnlp)
>
> This example prints the table inside an image of a clipboard.
> Here is a picture of the printed result in the `FIT_WIDTH` mode.
>
> [![Printed output of the TablePrintDemo3 example](../../figures/uiswing/../../figures/uiswing/misc/TablePrintDemo3_out.png)](../../figures/uiswing/../../figures/uiswing/misc/TablePrintDemo3_out.png)  
> *This figure has been reduced to fit on the page.   
>  Click the image to view it at its natural size.*
>
> The entire code for this program can be found in
> [`TablePrintDemo3.java`](../examples/misc/TablePrintDemo3Project/src/misc/TablePrintDemo3.java).
> In this demo, a custom subclass
> of the `JTable` class is used
> called `FancyPrintingJTable`.
> This `FancyPrintingJTable` class overrides
> the `getPrintable` method
> to return a custom printable object that wraps the default printable
> with its own decorations and header and footer.
> Here is the implementation
> of the `getPrintable` method.
>
> ```
>
> public Printable getPrintable(PrintMode printMode,
>                               MessageFormat headerFormat,
>                               MessageFormat footerFormat) {
>
>      MessageFormat pageNumber = new MessageFormat("- {0} -");
>
>      /* Fetch the default printable */
>      Printable delegate = super.getPrintable(printMode, null, pageNumber);
>
>      /* Return a fancy printable that wraps the default */
>      return new FancyPrintable(delegate);
> }
>
> ```
>
> The `FancyPrintable` class is responsible
> for wrapping the default printable object into another printable object
> and setting up the clipboard image.
> When an instance of this class is instantiated, it loads the images
> needed to assemble the clipboard image,
> calculates the area required for the clipboard image,
> calculates the shrunken area for the table,
> prints the table into the smaller area, and assembles and prints the clipboard image.
>
> Pay attention to the flexibility of the code that assembles
> the clipboard image with respect to the page size.
> The code takes into account the actual page dimensions and
> puts together the auxiliary images, stretching
> some of them as necessary so that the final clipboard image
> fits the actual page size.
> The picture below shows the auxiliary images
> and indicates how those images form the final output.
>
> [![Diagram showing how the auxiliary images were used in the printed output](../../figures/uiswing/../../figures/uiswing/misc/TablePrintDemo3_clipboard.png)](../../figures/uiswing/../../figures/uiswing/misc/TablePrintDemo3_clipboard.png)  
> *This figure has been reduced to fit on the page.   
>  Click the image to view it at its natural size.*

### The Table Printing API

> This section lists methods defined in the `JTable` class
> that allow you to print tables.
>
> | Method | Purpose |
> | --- | --- |
> | [boolean print()](http://download.oracle.com/javase/7/docs/api/javax/swing/JTable.html#print())   [boolean print(printMode)](http://download.oracle.com/javase/7/docs/api/javax/swing/JTable.html#print(javax.swing.JTable.PrintMode))   [boolean print(printMode, MessageFormat, MessageFormat)](http://download.oracle.com/javase/7/docs/api/javax/swing/JTable.html#print(javax.swing.JTable.PrintMode, java.text.MessageFormat, java.text.MessageFormat))   [boolean print(printMode, MessageFormat, MessageFormat, boolean, PrintRequestAttributeSet, boolean)](http://download.oracle.com/javase/7/docs/api/javax/swing/JTable.html#print(javax.swing.JTable.PrintMode, java.text.MessageFormat, java.text.MessageFormat, boolean, javax.print.attribute.PrintRequestAttributeSet, boolean))   [boolean print(printMode, MessageFormat, MessageFormat, boolean, PrintRequestAttributeSet, boolean, PrintService)](http://download.oracle.com/javase/7/docs/api/javax/swing/JTable.html#print(javax.swing.JTable.PrintMode, java.text.MessageFormat, java.text.MessageFormat, boolean, javax.print.attribute.PrintRequestAttributeSet, boolean, javax.print.PrintService)) | When called without arguments, displays a print dialog, and then prints this table interactively in the `FIT_WIDTH` mode without a header or a footer text. Returns `true` if the user continued printing and `false` if the user cancelled printing.   When called with a full set of arguments, prints this table according to the specified arguments. The first argument specifies the printing mode. Two `MessageFormat` arguments specify header and footer text. The first boolean argument defines whether to show a print dialog or not. Another boolean argument specifies whether to print interactively or not. With two other arguments you can specify printing attributes and a print service.   Whenever a `PrintService` argument is omitted, the default printer will be used. |
> | [Printable getPrintable(PrintMode, MessageFormat, MessageFormat)](http://download.oracle.com/javase/7/docs/api/javax/swing/JTable.html#getPrintable(javax.swing.JTable.PrintMode, java.text.MessageFormat, java.text.MessageFormat)) | Returns a `Printable` for printing a table. Override this method to get a customized `Printable` object. You can wrap one `Printable` object into another to get various layouts. |

### Examples That Use Table Printing

> This table lists examples that use table printing
> and points to where those examples are described.
>
> | Example | Where Described | Notes |
> | --- | --- | --- |
> | [`TablePrintDemo`](../examples/components/index.html#TablePrintDemo) | [How to Use Tables](../components/table.html#printing) | Demonstrates basic features in table printing such as displaying a print dialogue, and then printing interactively in the `FIT_WIDTH` mode with a page number as a header. |
> | [`TablePrintDemo1`](../examples/misc/index.html#TablePrintDemo1) | This page | Demostrates the basics of table printing and provides a rich GUI. Allows the user to specify a header or a footer text, select the printing mode, turn the print dialog on or off, and select printing interactively or non-interactively. |
> | [`TablePrintDemo2`](../examples/misc/index.html#TablePrintDemo2) This page | Based on the TablePrintDemo1, this example has an identical interface. This demo shows how to customize the table so that the printed result looks differently compared to the table being shown on the screen. | |
> | [`TablePrintDemo3`](../examples/misc/index.html#TablePrintDemo3) | This page | This demo shows advanced table printing features such as wrapping the default table printable into another printable to get a different layout. |

[« Previous](modality.html)
•
[Trail](../TOC.html)
•
[Next »](printtext.html)

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

**Previous page:** How to Use Modality in Dialogs
  
**Next page:** How to Print Text




A browser with JavaScript enabled is required for this page to operate properly.