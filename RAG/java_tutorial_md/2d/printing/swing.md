[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** 2D Graphics
  
**Lesson:** Printing

[Printing](index.html)

[A Basic Printing Program](printable.html)

[Using Print Setup Dialogs](dialog.html)

[Printing a Multiple Page Document](set.html)

[Working with Print Services and Attributes](services.html)

[Printing the Contents of a User Interface](gui.html)

Printing Support in Swing Components

[Home Page](../../index.html)
>
[2D Graphics](../index.html)
>
[Printing](index.html)

[« Previous](gui.html) • [Trail](../TOC.html) • [Next »](../advanced/index.html)

# Printing Support in Swing Components

The
[`PrintUIWindow.java`](examples/PrintUIWindow.java) example represented in the previous section demonstrates that the
printout is exactly the same you saw on the screen.
This appearance seems reasonable.
However, if a window is scrollable, then the contents that are
currently scrolled out of view are not included in the printout.
This creates a dump effect on the printer.
This becomes a particular problem when printing large
components such as a Swing table or text components.
Components may contain many lines of text which cannot all be entirely
visible on the screen. In this case, print the contents displayed by the
component in a manner consistent with the screen display.

To solve this problem, the Swing table and all text components are printing aware.
The following methods directly provide the use of the Java 2D™ printing:

* [`javax.swing.JTable.print();`](http://download.oracle.com/javase/7/docs/api/javax/swing/JTable.html#print())
* [`javax.swing.text.JTextComponent.print();`](http://download.oracle.com/javase/7/docs/api/javax/swing/text/JTextComponent.html#print())

These methods provide a full implementation of printing
for their contents. An application doesn't need directly create a
`PrinterJob` object and implement the `Printable` interface.
The call of these methods displays a print dialog and prints the component's
data in accordance with the user's selections.
There are also additional methods which provide more options.

[« Previous](gui.html)
•
[Trail](../TOC.html)
•
[Next »](../advanced/index.html)

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

**Previous page:** Printing the Contents of a User Interface
  
**Next page:** Advanced Topics in Java2D




A browser with JavaScript enabled is required for this page to operate properly.