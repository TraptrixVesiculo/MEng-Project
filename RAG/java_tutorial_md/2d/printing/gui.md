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

Printing the Contents of a User Interface

[Printing Support in Swing Components](swing.html)

[Home Page](../../index.html)
>
[2D Graphics](../index.html)
>
[Printing](index.html)

[« Previous](services.html) • [Trail](../TOC.html) • [Next »](swing.html)

# Printing the Contents of a User Interface

Another common printing task is to print the contents of a window
or a frame, either in whole, or in part.
The window may contain the following components: toolbars, buttons
sliders, text labels, scrollable text areas, images, and other
graphical content.
All of these components are printed using the following methods of the Java 2D™ printing API:

```

java.awt.Component.print(Graphics g);
java.awt.Component.printAll(Graphics g);

```

The following figure represents a simple user interface.

![Printing 12 lines in the window ](../../figures/2d/printui.png)

The code to create this UI is located in the sample program
[`PrintUIWindow.java`](examples/PrintUIWindow.java).

To print this window, modify the code in the earlier examples which printed
text or images. The resulting code should appear as follows:

```

   public int print(Graphics g, PageFormat pf, int page) throws
                                                    PrinterException {
        if (page > 0) {
            return NO_SUCH_PAGE;
        }

        Graphics2D g2d = (Graphics2D)g;
        g2d.translate(pf.getImageableX(), pf.getImageableY());

        /* Print the entire visible contents of a java.awt.Frame */
        frame.printAll(g);

        return PAGE_EXISTS;
    }

```

---

**Note:** The call to the `printAll` method is the only difference between
this example and examples to print text or image.
The `print(Graphics g)` method mirrors the `java.awt.Component.paint(Graphics g)` method used
for on-screen rendering. Use the `print()` method rather
than the `paint()` method as the `Components` class may have overridden the
`print()` method to handle the printing case differently.

---

The `printAll(Graphics g)`method prints the component and
all its subcomponents. This method is usually used to print
object such as a complete window, rather than a single component.

[« Previous](services.html)
•
[Trail](../TOC.html)
•
[Next »](swing.html)

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

**Previous page:** Working with Print Services and Attributes
  
**Next page:** Printing Support in Swing Components




A browser with JavaScript enabled is required for this page to operate properly.