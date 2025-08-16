[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** 2D Graphics
  
**Lesson:** Printing

[Printing](index.html)

[A Basic Printing Program](printable.html)

Using Print Setup Dialogs

[Printing a Multiple Page Document](set.html)

[Working with Print Services and Attributes](services.html)

[Printing the Contents of a User Interface](gui.html)

[Printing Support in Swing Components](swing.html)

[Home Page](../../index.html)
>
[2D Graphics](../index.html)
>
[Printing](index.html)

[« Previous](printable.html) • [Trail](../TOC.html) • [Next »](set.html)

# Using Print Setup Dialogs

Traditionally, the user wants to see the page setup and print dialog boxes.
From the print dialog you can select a printer, specify pages to print, and set the number of copies.

![This figures represents a print dialog](../../figures/2d/print-dialog.gif)

An application displays a print dialog when the user presses
a button related to the print command, or chooses an item from the print menu.
To display this dialog, call the
[`printDialog`](http://download.oracle.com/javase/7/docs/api/java/awt/print/PrinterJob.html#printDialog()) method of the
[`PrinterJob`](http://download.oracle.com/javase/7/docs/api/java/awt/print/PrinterJob.html) class:

```

 PrinterJob pj = PrinterJob.getPrinterJob();
 ...
     if (pj.printDialog()) {
         try {pj.print();}
	 catch (PrinterException exc) {
	   System.out.println(exc);
	  }
      }	  
  ...    

```

This method returns `true` if the user
clicked OK to leave the dialog, and `false` otherwise.
The user's choices in the dialog are constrained based on the number and format of
the pages that have been set to the `PrinterJob`.

The `printDialog` method in the above code snippet opens
a native print dialog. The
[`PrintDialogExample.java`](examples/PrintDialogExample.java) code example shows how to display a cross-platform print dialog.

You can change the page setup information contained in the
[`PageFormat`](http://download.oracle.com/javase/7/docs/api/java/awt/print/PageFormat.html) object by using the page setup dialog.

![This figure represents a page setup dialod window ](../../figures/2d/page-setup-dialog.gif)

To display the page setup dialog, call the `pageDialog` method of the
`PrinterJob` class.

```

   PrinterJob pj = PrinterJob.getPrinterJob();
   PageFormat pf = pj.pageDialog(pj.defaultPage());

```

The page setup dialog is initialized using the parameter passed
to `pageDialog`. If the user clicks the OK button in the dialog,
the `PageFormat` instance will be created in accordance with the users
selections, and then returned. If the user cancels the dialog, `pageDialog`
returns the original unchanged PageFormat.

Usually the Java 2D™ Printing API requires an application to display a print dialog, but in sometimes
it's possible to print without showing any dialog at all. This type of printing is called
*silent printing*. It may be useful in specific cases,
such as, when you need to print a particular database weekly report. In the other cases
it is always recommended to inform the user when a print process is starting.

[« Previous](printable.html)
•
[Trail](../TOC.html)
•
[Next »](set.html)

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

**Previous page:** A Basic Printing Program
  
**Next page:** Printing a Multiple Page Document




A browser with JavaScript enabled is required for this page to operate properly.