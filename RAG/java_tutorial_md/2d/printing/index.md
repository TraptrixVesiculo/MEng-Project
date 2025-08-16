[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

Printing

[A Basic Printing Program](printable.html)

[Using Print Setup Dialogs](dialog.html)

[Printing a Multiple Page Document](set.html)

[Working with Print Services and Attributes](services.html)

[Printing the Contents of a User Interface](gui.html)

[Printing Support in Swing Components](swing.html)

**Trail:** 2D Graphics

[Home Page](../../index.html)
>
[2D Graphics](../index.html)

[« Previous](../images/index.html) • [Trail](../TOC.html) • [Next »](printable.html)

# Lesson: Printing

Since the Java 2D™ API enables you to draw on any surface, a natural extension of that is
the ability to print Java 2D graphics. A printer can be considered a
graphics device just like a display.

The Java 2D printing API is not limited to printing graphics. It enables you to
print the content of an application's user interface as well. Content can be
printed by sending raw data to the printer under the formatting control of the
Java 2D printing API, or by using the Java 2D Graphics API.

In this lesson you will explore the printer and job control functions of the Java 2D printing API which
are complements to the rendering elements.
You will learn how to look up printers configured
on the system or network and discover information about these printers
such as the paper sizes it supports, and selecting these attributes for printing,
and user dialogs.

The main classes and interfaces involved in printing are represented in
the
[`java.awt.print`](http://download.oracle.com/javase/7/docs/api/java/awt/print/package-frame.html) and
[`javax.print`](http://download.oracle.com/javase/7/docs/api/javax/print/package-frame.html) packages
(the last package allows you to get access to the printing services).

The basic printing operations are represented in the following sections:

## [A Basic Printing Program](../printing/printable.html)

This section describes the `Printable` interface and presents a basic
printing program.

## [Using Print Setup Dialogs](../printing/dialog.html)

This sections explains how to display the Print Setup Dialog.

## [Printing a Multiple Page Document](../printing/set.html)

This section explains how to use pagination for printing a multiple
page document.

## [Working with Print Services and Attributes](../printing/services.html)

This section teaches you about print services, how to specify the print data format, and
how to create print job using the `javax.print` package.

## [Printing the Contents of a User Interface](../printing/gui.html)

This section explains how to print the contents of a window or a frame.

## [Printing Support in Swing Components](../printing/swing.html)

This section provides a brief description of the related printing functionality
in `Swing` and refers to specific `Swing` classes and interfaces.

[« Previous](../images/index.html)
•
[Trail](../TOC.html)
•
[Next »](printable.html)

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

**Previous page:** Previous Lesson
  
**Next page:** A Basic Printing Program




A browser with JavaScript enabled is required for this page to operate properly.