[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Java API for XML Processing (JAXP)
  
**Lesson:** Simple API for XML

[Simple API for XML](index.html)

[When to Use SAX](when.html)

[Parsing an XML File Using SAX](parsing.html)

[Implementing SAX Validation](validation.html)

Handling Lexical Events

[Using the DTDHandler and EntityResolver](using.html)

[Further Information](info.html)

[Home Page](../../index.html)
>
[Java API for XML Processing (JAXP)](../index.html)
>
[Simple API for XML](index.html)

[« Previous](validation.html) • [Trail](../TOC.html) • [Next »](using.html)

# Handling Lexical Events

At this point, you have digested many XML concepts, including DTDs and external
entities. You have also learned your way around the SAX parser. The remainder
of this lesson covers advanced topics that you will need to understand only
if you are writing SAX-based applications. If your primary goal is to write
DOM-based applications, you can skip ahead to
[Document Object Model](../dom
/index.html
).

You saw earlier that if you are writing text out as XML,
you need to know whether you are in a CDATA section. If you
are, then angle brackets (<) and ampersands (&) should be output unchanged. But
if you are not in a CDATA section, they should be replaced by
the predefined entities &lt; and &amp;. But how do you know whether
you are processing a CDATA section?

Then again, if you are filtering XML in some way, you want
to pass comments along. Normally the parser ignores comments. How can you get
comments so that you can echo them?

This section answers those questions. It shows you how to use org.xml.sax.ext.LexicalHandler
to identify comments, CDATA sections, and references to parsed entities.

Comments, CDATA tags, and references to parsed entities constitute lexical information-that is, information
that concerns the text of the XML itself, rather than the XML's information
content. Most applications, of course, are concerned only with the content of an
XML document. Such applications will not use the LexicalEventListener API. But applications that output
XML text will find it invaluable.

---

**Note -** Lexical event handling is an optional parser feature. Parser implementations are not required
to support it. (The reference implementation does so.) This discussion assumes that your
parser does so.

---

## How the LexicalHandler Works

To be informed when the SAX parser sees lexical information, you configure the
XmlReader that underlies the parser with a LexicalHandler. The LexicalHandler interface defines the
following event-handling methods.

comment(String comment)
:   Passes comments to the application.

startCDATA(), endCDATA()
:   Tells when a CDATA section is starting and ending, which tells your application what kind of characters to expect the next time characters() is called.

startEntity(String name), endEntity(String name)
:   Gives the name of a parsed entity.

startDTD(String name, String publicId, String systemId), endDTD()
:   Tells when a DTD is being processed, and identifies it.

To activate the Lexical Handler, your application must extend DefaultHandler and implement
the LexicalHandler interface. Then, you must configure your XMLReader instance that the parser delegates
to, and configure it to send lexical events to your lexical handler, as
shown below.

```
[...]

       SAXParser saxParser = factory.newSAXParser();
       XMLReader xmlReader = saxParser.getXMLReader();
       xmlReader.setProperty(
               "http://xml.org/sax/properties/lexical-handler",
               handler
               ); 
[...]
```

Here, you configure the XMLReader using the setProperty() method defined in the
XMLReader class. The property name, defined as part of the SAX standard, is
the URN, http://xml.org/sax/properties/lexical-handler.

Finally, add something like the following code to define the appropriate methods that
will implement the interface.

```
[...]

public void warning(SAXParseException err)

[...]
}

public void comment(char[] ch, int start, int length)
throws SAXException
{
}

public void startCDATA()
throws SAXException
{
}

pubic void endCDATA()
throws SAXException
{
}

public void startEntity(String name)
throws SAXException
{
}

public void endEntity(String name)
throws SAXException
{
}

public void startDTD(

String name, String publicId, String systemId)
throws SAXException
{
}

public void endDTD()
throws SAXException
{
}

private void echoText()

[...]
```

This code will transform your parsing application into a lexical handler. All that
remains to be done is to give each of these new methods
an action to perform.

[« Previous](validation.html)
•
[Trail](../TOC.html)
•
[Next »](using.html)

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

**Previous page:** Implementing SAX Validation
  
**Next page:** Using the DTDHandler and EntityResolver




A browser with JavaScript enabled is required for this page to operate properly.