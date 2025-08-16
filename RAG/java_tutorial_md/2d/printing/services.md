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

Working with Print Services and Attributes

[Printing the Contents of a User Interface](gui.html)

[Printing Support in Swing Components](swing.html)

[Home Page](../../index.html)
>
[2D Graphics](../index.html)
>
[Printing](index.html)

[« Previous](set.html) • [Trail](../TOC.html) • [Next »](gui.html)

# Working with Print Services and Attributes

From the previous lessons you have learned that the Java 2D ™ printing API supports
page imaging, displays print and page setup dialogs, and
specifies printing attributes. Printing services is another key component
of any printing subsystem.

The **Java™ Print Service (JPS) API** extends the current Java 2D printing
features to offer the following functionality:

* Application discovers printers that cater to
  its needs by dynamically querying the printer capabilities.
* Application extends the attributes included with the JPS API.
* Third parties can plug in their own print services with the Service Provider Interface,
  which print different formats, including Postscript, PDF, and SVG.

The Java Print Service API consists of four packages:

![This figure represents four packages necessary for printing](../../figures/2d/JPS.gif)

The
[`javax.print`](http://download.oracle.com/javase/7/docs/api/javax/print/package-summary.html) package provides the principal classes and interfaces
for the Java™ Print Service API. It enables client and server applications to:

* Discover and select print services based on their capabilities.
* Specify the format of print data.
* Submit print jobs to services that support the document type to be printed.

## Document Type Specification

The
[`DocFlavor`](http://download.oracle.com/javase/7/docs/api/javax/print/DocFlavor.html) class represents format of the print data, such as JPEG or PostScript.
The `DocFlavor` format consists of two parts: a MIME type and a representation class name.
A MIME type describes the format, and a document
representation class name indicates how the document is delivered to the printer or output stream.
An application uses the `DocFlavor` and an attribute set to find printers
with the capabilities specified by the attribute set. This code sample
demonstrates obtaining an array of `StreamPrintServiceFactory` objects that
can return `StreamPrintService` objects able to convert a GIF image into
PostScript:

```

    DocFlavor flavor = DocFlavor.INPUT_STREAM.GIF;
    String psMimeType = DocFlavor.BYTE_ARRAY.POSTSCRIPT.getMimeType();
    StreamPrintServiceFactory[] psfactories =
    	StreamPrintServiceFactory.lookupStreamPrintServiceFactories(
    		flavor, psMimeType);

```

## Attribute Definitions

The
[`javax.print.attribute`](http://download.oracle.com/javase/7/docs/api/javax/print/attribute/package-frame.html) and
[`javax.print.attribute.standard`](http://download.oracle.com/javase/7/docs/api/javax/print/attribute/standard/package-frame.html) packages define print attributes which describe the capabilities of a print service, specify
the requirements of a print job, and track the progress of the print job.

For example, if you would like to use A4 paper format and print three copies of your
document you will have to create a set of the following attributes implementing
the `PrintRequestAttributeSet` interface:

```

    PrintRequestAttributeSet attr_set = new HashPrintRequestAttributeSet();
    attr_set.add(MediaSize.ISO_A4); 
    attr_set.add(new Copies(3)); 

```

Then you must pass the attribute set to the print job's `print` method, along with the `DocFlavor`.

## Print Service Discovery

An application invokes the static methods of the abstract class `PrintServiceLookup`
to locate print services that have the capabilities to satisfy the application's print request.
For example, in order to print two copies of a double-sided document, the application first needs to find printers that have double-sided printing capability:

```

   DocFlavor doc_flavor = DocFlavor.INPUT_STREAM.PDF;
   PrintRequestAttributeSet attr_set = new HashPrintRequestAttributeSet();
   attr_set.add(new Copies(2));
   attr_set.add(Sides.DUPLEX);
   PrintService[] service = PrintServiceLookup.lookupPrintServices(doc_flavor, attr_set);

```

## Common Use of the API

In conclusion, the Java Print Service API performs the following
steps to process a print request:

1. Chooses a `DocFlavor`.
2. Creates a set of attributes.
3. Locates a print service that can handle the print request as specified by
   the `DocFlavor` and the attribute set.
4. Creates a `Doc` object encapsulating the `DocFlavor`
   and the actual print data.
5. Gets a print job, represented by `DocPrintJob`, from the print service.
6. Calls the `print` method of the print job.

For more information about Java Print Service, see
[Java 2D™ Print Service API User Guide](http://download.oracle.com/javase/7/docs/technotes/guides/jps/spec/JPSTOC.fm.html).

[« Previous](set.html)
•
[Trail](../TOC.html)
•
[Next »](gui.html)

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

**Previous page:** Printing a Multiple Page Document
  
**Next page:** Printing the Contents of a User Interface




A browser with JavaScript enabled is required for this page to operate properly.