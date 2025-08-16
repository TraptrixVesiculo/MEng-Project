[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Java API for XML Processing (JAXP)
  
**Lesson:** Introduction to JAXP

[Introduction to JAXP](index.html)

[Overview of the Packages](package.html)

Simple API for XML APIs

[Document Object Model APIs](dom.html)

[Extensible Stylesheet Language Transformations APIs](extensible.html)

[Streaming API for XML APIs](streaming.html)

[Finding the JAXP Sample Programs](sample.html)

[Where Do You Go From Here?](next.html)

[Home Page](../../index.html)
>
[Java API for XML Processing (JAXP)](../index.html)
>
[Introduction to JAXP](index.html)

[« Previous](package.html) • [Trail](../TOC.html) • [Next »](dom.html)

# Simple API for XML APIs

The basic outline of the SAX parsing APIs is shown in [Figure 1-1](#gcezl).
To start the process, an instance of the SAXParserFactory class is used to
generate an instance of the parser.

Figure 1-1 SAX APIs

![The SAX APIs](../../figures/jaxp/intro/jaxpintro-saxApi.gif)

The parser wraps a SAXReader object. When the parser's parse() method is invoked,
the reader invokes one of several callback methods implemented in the application. Those
methods are defined by the interfaces ContentHandler, ErrorHandler, DTDHandler, and EntityResolver.

Here is a summary of the key SAX APIs:

SAXParserFactory
:   A SAXParserFactory object creates an instance of the parser determined by the system property, javax.xml.parsers.SAXParserFactory.

SAXParser
:   The SAXParser interface defines several kinds of parse() methods. In general, you pass an XML data source and a DefaultHandler object to the parser, which processes the XML and invokes the appropriate methods in the handler object.

SAXReader
:   The SAXParser wraps a SAXReader. Typically, you do not care about that, but every once in a while you need to get hold of it using SAXParser's getXMLReader() so that you can configure it. It is the SAXReader that carries on the conversation with the SAX event handlers you define.

DefaultHandler
:   Not shown in the diagram, a DefaultHandler implements the ContentHandler, ErrorHandler, DTDHandler, and EntityResolver interfaces (with null methods), so you can override only the ones you are interested in.

ContentHandler
:   Methods such as startDocument, endDocument, startElement, and endElement are invoked when an XML tag is recognized. This interface also defines the methods characters() and processingInstruction(), which are invoked when the parser encounters the text in an XML element or an inline processing instruction, respectively.

ErrorHandler
:   Methods error(), fatalError(), and warning() are invoked in response to various parsing errors. The default error handler throws an exception for fatal errors and ignores other errors (including validation errors). This is one reason you need to know something about the SAX parser, even if you are using the DOM. Sometimes, the application may be able to recover from a validation error. Other times, it may need to generate an exception. To ensure the correct handling, you will need to supply your own error handler to the parser.

DTDHandler
:   Defines methods you will generally never be called upon to use. Used when processing a DTD to recognize and act on declarations for an unparsed entity.

EntityResolver
:   The resolveEntity method is invoked when the parser must identify data identified by a URI. In most cases, a URI is simply a URL, which specifies the location of a document, but in some cases the document may be identified by a URN - a public identifier, or name, that is unique in the web space. The public identifier may be specified in addition to the URL. The EntityResolver can then use the public identifier instead of the URL to find the document-for example, to access a local copy of the document if one exists.

A typical application implements most of the ContentHandler methods, at a minimum. Because
the default implementations of the interfaces ignore all inputs except for fatal errors,
a robust implementation may also want to implement the ErrorHandler methods.

## SAX Packages

The SAX parser is defined in the packages listed in [Table 1-1](#gceyy).

Table 1-1 SAX Packages

| Packages | Description |
| org.xml.sax | Defines the SAX interfaces. The name org.xml is the package prefix that was settled on by the group that defined the SAX API. |
| org.xml.sax.ext | Defines SAX extensions that are used for doing more sophisticated SAX processing-for example, to process a document type definition (DTD) or to see the detailed syntax for a file. |
| org.xml.sax.helpers | Contains helper classes that make it easier to use SAX-for example, by defining a default handler that has null methods for all the interfaces, so that you only need to override the ones you actually want to implement. |
| javax.xml.parsers | Defines the SAXParserFactory class, which returns the SAXParser. Also defines exception classes for reporting errors. |

[« Previous](package.html)
•
[Trail](../TOC.html)
•
[Next »](dom.html)

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

**Previous page:** Overview of the Packages
  
**Next page:** Document Object Model APIs




A browser with JavaScript enabled is required for this page to operate properly.