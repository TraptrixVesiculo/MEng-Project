[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** 2D Graphics
  
**Lesson:** Printing

[Printing](index.html)

A Basic Printing Program

[Using Print Setup Dialogs](dialog.html)

[Printing a Multiple Page Document](set.html)

[Working with Print Services and Attributes](services.html)

[Printing the Contents of a User Interface](gui.html)

[Printing Support in Swing Components](swing.html)

[Home Page](../../index.html)
>
[2D Graphics](../index.html)
>
[Printing](index.html)

[« Previous](index.html) • [Trail](../TOC.html) • [Next »](dialog.html)

# A Basic Printing Program

This section explains how to create a basic printing program
that displays a print dialog and prints the text "Hello World" to the
selected printer.

Printing task usually consists of two parts:

* Job control — Creating a print job, associating it with a
  printer, specifying the number of copies, and user print dialog
  interaction.* Page Imaging — Drawing content to a page, and managing content that spans
    pages (pagination).

First create the printer job.
The class representing a printer job and most other related
classes is located in the
[`java.awt.print`](http://download.oracle.com/javase/7/docs/api/java/awt/print/package-summary.html) package.

```

import java.awt.print.*;

PrinterJob job = PrinterJob.getPrinterJob();

```

Next provide code that renders the content
to the page by implementing the
[`Printable`](http://download.oracle.com/javase/7/docs/api/java/awt/print/Printable.html) interface.

```

class HelloWorldPrinter implements Printable  { ... }
..
job.setPrintable(new HelloWorldPrinter());

```

An application typically displays a print dialog
so that the user can adjust various options such as number of copies,
page orientation, or the destination printer.

```

boolean doPrint = job.printDialog();

```

This dialog appears until the user either approves or cancels printing.
The `doPrint` variable will be true if the user gave a command to go ahead and print.
If the `doPrint` variable is false, the user cancelled the print job.
Since displaying the dialog at all is optional, the returned value is purely
informational.

If the `doPrint` variable is true, then the application will request that
the job be printed by calling the `PrinterJob.print` method.

```

if (doPrint) {
  try {
       job.print();
  } catch (PrinterException e) {
   /* The job did not successfully complete */
  }
}

```

The `PrinterException` will be thrown if there is
problem sending the job to the printer. However, since the
`PrinterJob.print` method returns as soon as the job is
sent to the printer, the user application cannot detect paper jams or paper out problems.
This job control boilerplate is sufficient for basic printing uses.

The `Printable` interface has only one method:

```

public int print(Graphics graphics, PageFormat pf, int page)
            throws PrinterException;

```

The
[`PageFormat`](http://download.oracle.com/javase/7/docs/api/java/awt/print/PageFormat.html) class describes the page orientation
(portrait or landscape) and its size and imageable area in units of 1/72nd of an inch.
Imageable area accounts for the margin limits of most printers (hardware margin).
The imageable area is the space inside these margins, and
in practice if is often further limited to leave space
for headers or footers.

A `page` parameter is the zero-based page number
that will be rendered.

The following code represents the full `Printable` implementation:

```

import java.awt.print.*;
import java.awt.*;

public class HelloWorldPrinter implements Printable {

  public int print(Graphics g, PageFormat pf, int page) throws
                                                        PrinterException {

    if (page > 0) { /* We have only one page, and 'page' is zero-based */
         return NO_SUCH_PAGE;
    }

    /* User (0,0) is typically outside the imageable area, so we must
     * translate by the X and Y values in the PageFormat to avoid clipping
     */
    Graphics2D g2d = (Graphics2D)g;
    g2d.translate(pf.getImageableX(), pf.getImageableY());

    /* Now we perform our rendering */
    g.drawString("Hello world!", 100, 100);

    /* tell the caller that this page is part of the printed document */
    return PAGE_EXISTS;
  }
}

```

The complete code for this example is in
[`HelloWorldPrinter.java`](examples/HelloWorldPrinter.java).

Sending a
[`Graphics`](http://download.oracle.com/javase/7/docs/api/java/awt/Graphics.html) instance to the printer is
essentially the same as rendering it to the screen. In both cases you need to perform
the following steps:

* To draw a test string is as easy as the other operations
  that were described for drawing to a `Graphics2D`.* Printer graphics have a higher resolution, which should
    be transparent to most code.* The `Printable.print()` method is called by the printing system,
      just as the `Component.paint()` method is called to paint a
      Component on the display. The printing system will call the `Printable.print()`
      method for page 0, 1,.. etc until the `print()` method returns
      `NO_SUCH_PAGE`.* The `print()` method may be called with the same page index multiple
        times until the document is completed. This feature is applied when the
        user specifies attributes such as multiple copies with collate option.* The PageFormat's imageable area determines the clip area.
          Imageable area is also important in calculating pagination,
          or how to span content across printed pages,
          since page breaks are determined by how much can fit on each page.

          ---

          **Note:** A call to the `print()` method may be skipped for certain page
          indices if the user has specified a different page range that
          does not involve a particular page index.

          ---

[« Previous](index.html)
•
[Trail](../TOC.html)
•
[Next »](dialog.html)

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

**Previous page:** Printing
  
**Next page:** Using Print Setup Dialogs




A browser with JavaScript enabled is required for this page to operate properly.