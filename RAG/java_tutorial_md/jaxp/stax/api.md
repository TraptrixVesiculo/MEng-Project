[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Java API for XML Processing (JAXP)
  
**Lesson:** Streaming API for XML

[Streaming API for XML](index.html)

[Why StAX?](why.html)

StAX API

[Using StAX](using.html)

[Oracle's Streaming XML Parser Implementation](parser.html)

[Example Code](example.html)

[Further Information](info.html)

[Home Page](../../index.html)
>
[Java API for XML Processing (JAXP)](../index.html)
>
[Streaming API for XML](index.html)

[« Previous](why.html) • [Trail](../TOC.html) • [Next »](using.html)

# StAX API

The StAX API exposes methods for iterative, event-based processing of XML documents. XML
documents are treated as a filtered series of events, and infoset states can
be stored in a procedural fashion. Moreover, unlike SAX, the StAX API is
bidirectional, enabling both reading and writing of XML documents.

The StAX API is really two distinct API sets: a **cursor** API and
an **iterator** API. These two API sets are explained in greater detail later
in this lesson, but their main features are briefly described below.

## Cursor API

As the name implies, the StAX **cursor** API represents a cursor with which
you can walk an XML document from beginning to end. This cursor can
point to one thing at a time, and always moves forward, never
backward, usually one infoset element at a time.

The two main cursor interfaces are XMLStreamReader and XMLStreamWriter. XMLStreamReader includes accessor methods
for all possible information retrievable from the XML Information model, including document encoding,
element names, attributes, namespaces, text nodes, start tags, comments, processing instructions, document boundaries, and
so forth; for example:

```
public interface XMLStreamReader {
    public int next() throws XMLStreamException;
    public boolean hasNext() throws XMLStreamException;
    public String getText();
    public String getLocalName();
    public String getNamespaceURI();
    // ... other methods not shown
}
```

You can call methods on XMLStreamReader, such as getText and getName, to
get data at the current cursor location. XMLStreamWriter provides methods that correspond to StartElement
and EndElement event types; for example:

```
public interface XMLStreamWriter {
    public void writeStartElement(String localName) 
        throws XMLStreamException;
    public void writeEndElement() 
        throws XMLStreamException;
    public void writeCharacters(String text) 
        throws XMLStreamException;
// ... other methods not shown
}
```

The cursor API mirrors SAX in many ways. For example, methods are
available for directly accessing string and character information, and integer indexes can be used
to access attribute and namespace information. As with SAX, the cursor API methods
return XML information as strings, which minimizes object allocation requirements.

## Iterator API

The StAX **iterator** API represents an XML document stream as a set of
discrete event objects. These events are pulled by the application and provided by
the parser in the order in which they are read in the source
XML document.

The base iterator interface is called XMLEvent, and there are subinterfaces for each
event type listed in [Table 5-2](#bnbeg). The primary parser interface for reading iterator
events is XMLEventReader, and the primary interface for writing iterator events is XMLEventWriter. The
XMLEventReader interface contains five methods, the most important of which is nextEvent,
which returns the next event in an XML stream. XMLEventReader implements java.util.Iterator,
which means that returns from XMLEventReader can be cached or passed into routines that
can work with the standard Java Iterator; for example:

```
public interface XMLEventReader extends Iterator {
    public XMLEvent nextEvent() throws XMLStreamException;
    public boolean hasNext();
    public XMLEvent peek() throws XMLStreamException;
    ...
}
```

Similarly, on the output side of the iterator API, you have:

```
public interface XMLEventWriter {
    public void flush() throws XMLStreamException;
    public void close() throws XMLStreamException;
    public void add(XMLEvent e) throws XMLStreamException;
    public void add(Attribute attribute) throws XMLStreamException;
    ...
}
```

### Iterator Event Types

[Table 5-2](#bnbeg) lists the XMLEvent types defined in the event iterator API.

#### Table 5-2 XMLEvent Types

| Event Type | Description |
| StartDocument | Reports the beginning of a set of XML events, including encoding, XML version, and standalone properties. |
| StartElement | Reports the start of an element, including any attributes and namespace declarations; also provides access to the prefix, namespace URI, and local name of the start tag. |
| EndElement | Reports the end tag of an element. Namespaces that have gone out of scope can be recalled here if they have been explicitly set on their corresponding StartElement. |
| Characters | Corresponds to XML CData sections and CharacterData entities. Note that ignorable white space and significant white space are also reported as Character events. |
| EntityReference | Character entities can be reported as discrete events, which an application developer can then choose to resolve or pass through unresolved. By default, entities are resolved. Alternatively, if you do not want to report the entity as an event, replacement text can be substituted and reported as Characters. |
| ProcessingInstruction | Reports the target and data for an underlying processing instruction. |
| Comment | Returns the text of a comment. |
| EndDocument | Reports the end of a set of XML events. |
| DTD | Reports as java.lang.String information about the DTD, if any, associated with the stream, and provides a method for returning custom objects found in the DTD. |
| Attribute | Attributes are generally reported as part of a StartElement event. However, there are times when it is desirable to return an attribute as a standalone Attribute event; for example, when a namespace is returned as the result of an XQuery or XPath expression. |
| Namespace | As with attributes, namespaces are usually reported as part of a StartElement, but there are times when it is desirable to report a namespace as a discrete Namespace event. |

Note that the DTD, EntityDeclaration, EntityReference, NotationDeclaration, and ProcessingInstruction events are only
created if the document being processed contains a DTD.

### Example of Event Mapping

As an example of how the event iterator API maps an XML
stream, consider the following XML document:

```
<?xml version="1.0"?>
<BookCatalogue xmlns="http://www.publishing.org">
    <Book>
        <Title>Yogasana Vijnana: the Science of Yoga</Title>
        <ISBN>81-40-34319-4</ISBN>
        <Cost currency="INR">11.50</Cost>
    </Book>
</BookCatalogue>
```

This document would be parsed into eighteen primary and secondary events, as shown
in [Table 5-3](#bnbei). Note that secondary events, shown in curly braces ({}), are typically
accessed from a primary event rather than directly.

#### Table 5-3 Example of Iterator API Event Mapping

| # | Element/Attribute | Event |
| 1 | ``` version="1.0" ``` | StartDocument |
| 2 | ``` isCData = false data = "\n" IsWhiteSpace = true ``` | Characters |
| 3 | ``` qname = BookCatalogue:http://www.publishing.org attributes = null namespaces = {BookCatalogue" -> http://www.publishing.org"} ``` | StartElement |
| 4 | ``` qname = Book attributes = null namespaces = null ``` | StartElement |
| 5 | ``` qname = Title attributes = null namespaces = null ``` | StartElement |
| 6 | ``` isCData = false data = "Yogasana Vijnana: the Science of Yoga\n\t" IsWhiteSpace = false ``` | Characters |
| 7 | ``` qname = Title namespaces = null ``` | EndElement |
| 8 | ``` qname = ISBN attributes = null namespaces = null ``` | StartElement |
| 9 | ``` isCData = false data = "81-40-34319-4\n\t" IsWhiteSpace = false ``` | Characters |
| 10 | ``` qname = ISBN namespaces = null ``` | EndElement |
| 11 | ``` qname = Cost attributes = {"currency" -> INR} namespaces = null ``` | StartElement |
| 12 | ``` isCData = false data = "11.50\n\t" IsWhiteSpace = false ``` | Characters |
| 13 | ``` qname = Cost namespaces = null ``` | EndElement |
| 14 | ``` isCData = false data = "\n" IsWhiteSpace = true ``` | Characters |
| 15 | ``` qname = Book namespaces = null ``` | EndElement |
| 16 | ``` isCData = false data = "\n" IsWhiteSpace = true ``` | Characters |
| 17 | ``` qname = BookCatalogue:http://www.publishing.org namespaces = {BookCatalogue" -> http://www.publishing.org"} ``` | EndElement |
| 18 |  | EndDocument |

There are several important things to note in this example:

* The events are created in the order in which the corresponding XML elements are encountered in the document, including nesting of elements, opening and closing of elements, attribute order, document start and document end, and so forth.
* As with proper XML syntax, all container elements have corresponding start and end events; for example, every StartElement has a corresponding EndElement, even for empty elements.
* Attribute events are treated as secondary events, and are accessed from their corresponding StartElement event.
* Similar to Attribute events, Namespace events are treated as secondary, but appear twice and are accessible twice in the event stream, first from their corresponding StartElement and then from their corresponding EndElement.
* Character events are specified for all elements, even if those elements have no character data. Similarly, Character events can be split across events.
* The StAX parser maintains a namespace stack, which holds information about all XML namespaces defined for the current element and its ancestors. The namespace stack, which is exposed through the javax.xml.namespace.NamespaceContext interface, can be accessed by namespace prefix or URI.

## Choosing between Cursor and Iterator APIs

It is reasonable to ask at this point, “What API should I
choose? Should I create instances of XMLStreamReader or XMLEventReader? Why are there two
kinds of APIs anyway?”

### Development Goals

The authors of the StAX specification targeted three types of developers:

* **Library and infrastructure developers**: Create application servers, JAXM, JAXB, JAX-RPC and similar implementations; need highly efficient, low-level APIs with minimal extensibility requirements.
* **Java ME developers**: Need small, simple, pull-parsing libraries, and have minimal extensibility needs.
* **Java Platform, Enterprise Edition (Java EE) and Java Platform, Standard Edition (Java SE) developers**: Need clean, efficient pull-parsing libraries, plus need the flexibility to both read and write XML streams, create new event types, and extend XML document elements and attributes.

Given these wide-ranging development categories, the StAX authors felt it was more useful
to define two small, efficient APIs rather than overloading one larger and necessarily
more complex API.

### Comparing Cursor and Iterator APIs

Before choosing between the cursor and iterator APIs, you should note a few
things that you can do with the iterator API that you cannot
do with the cursor API:

* Objects created from the XMLEvent subclasses are immutable, and can be used in arrays, lists, and maps, and can be passed through your applications even after the parser has moved on to subsequent events.
* You can create subtypes of XMLEvent that are either completely new information items or extensions of existing items but with additional methods.
* You can add and remove events from an XML event stream in much simpler ways than with the cursor API.

Similarly, keep some general recommendations in mind when making your choice:

* If you are programming for a particularly memory-constrained environment, like Java ME, you can make smaller, more efficient code with the cursor API.
* If performance is your highest priority—for example, when creating low-level libraries or infrastructure—the cursor API is more efficient.
* If you want to create XML processing pipelines, use the iterator API.
* If you want to modify the event stream, use the iterator API.
* If you want your application to be able to handle pluggable processing of the event stream, use the iterator API.
* In general, if you do not have a strong preference one way or the other, using the iterator API is recommended because it is more flexible and extensible, thereby “future-proofing” your applications.

[« Previous](why.html)
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

**Previous page:** Why StAX?
  
**Next page:** Using StAX




A browser with JavaScript enabled is required for this page to operate properly.