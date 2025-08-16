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

Printing a Multiple Page Document

[Working with Print Services and Attributes](services.html)

[Printing the Contents of a User Interface](gui.html)

[Printing Support in Swing Components](swing.html)

[Home Page](../../index.html)
>
[2D Graphics](../index.html)
>
[Printing](index.html)

[« Previous](dialog.html) • [Trail](../TOC.html) • [Next »](services.html)

# Printing a Multiple Page Document

You have already learned how to use the
[`Printable`](http://download.oracle.com/javase/7/docs/api/java/awt/print/Printable.html)
interface to print a single page document.
However, documents are usually more than one physical page in length.
*Pagination* is the process of identifying the location in a document where
page breaks and printing accordingly.

In case of printing several graphics images, one per page, use the page
index to iterate through these pages and print one on
each page.
For example, if several images are represented in the following array:

```

BufferedImage[] images = new BufferedImage[10];

```

then use the `print()` method as shown in the following code
fragment:

```

public int print(Graphics graphics, PageFormat pageFormat, int pageIndex)
            throws PrinterException {

    if (pageIndex < images.length) {
        graphics.drawImage(images[pageIndex], 100, 100, null);
        return PAGE_EXISTS;
    } else {
        return NO_SUCH_PAGE:
    }
}

```

If the document is continuous, the application must calculate how much content
can fit on each page, and break the page at that point.
If text document consists of many lines, then an application must calculate how many of these lines can fit entirely on
a page.
The
[`Point`](http://download.oracle.com/javase/7/docs/api/java/awt/Point.html) class creates a point representing a location in (x,y)

To calculate the height of a single line of text, use the
[`FontMetrics`](http://download.oracle.com/javase/7/docs/api/java/awt/FontMetrics.html)
class.

```

Font font = new Font("Serif", Font.PLAIN, 10);
FontMetrics metrics = graphics.getFontMetrics(font);
int lineHeight = metrics.getHeight();

```

The `PageFormat` parameter describes the
printable area of the page. In particular, to find the vertical
span of the page use the following code fragment:

```

double pageHeight = pageFormat.getImageableHeight();

```

Use the following code fragment to calculate the number of lines that fit
on a page and the number of page breaks:

```

int linesPerPage = ((int)pageHeight)/lineHeight);
int numBreaks = (textLines.length-1)/linesPerPage;
int[] pageBreaks = new int[numBreaks];
for (int b=0; b < numBreaks; b++) {
    pageBreaks[b] = (b+1)*linesPerPage; 
}

```

Use the `print()` method to calculate the printable area for the
following reasons:

* Text measurement depends on the `FontRenderContext`
  and this is implicit in the `FontMetrics` object returned by
  the printer graphics which is not available except inside the
  `print()` method.
* The page format may not be disclosured until printing occurs. Since if
  the user selected a landscape mode in the print dialog, then this setting
  needs to be accounted for. The `PageFormat` object passed into
  the `print()` method provides this information.

The page break positions are used as represented in the following code
fragment:

```

/* Draw each line that is on this page.
 * Increment 'y' position by lineHeight for each line.
 */
int y = 0; 
int start = (pageIndex == 0) ? 0 : pageBreaks[pageIndex-1];
int end   = (pageIndex == pageBreaks.length)
                 ? textLines.length : pageBreaks[pageIndex];
for (int line=start; line<end; line++) {
    y += lineHeight;
    g.drawString(textLines[line], 0, y);
}

```

If a document contains 100 lines and only 48 lines fit on a page,
then an application prints 3 pages with page breaks after
48 and 96 lines of text. The remaining 4 lines are printed on the last page.
The complete code for this example is in
[`PaginationExample.java`](examples/PaginationExample.java).

The following simplifying factors are used in the `PaginationExample` code:

* Each page has the same height.
* The same font is used.

[« Previous](dialog.html)
•
[Trail](../TOC.html)
•
[Next »](services.html)

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

**Previous page:** Using Print Setup Dialogs
  
**Next page:** Working with Print Services and Attributes




A browser with JavaScript enabled is required for this page to operate properly.