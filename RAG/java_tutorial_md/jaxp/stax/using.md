[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Java API for XML Processing (JAXP)
  
**Lesson:** Streaming API for XML

[Streaming API for XML](index.html)

[Why StAX?](why.html)

[StAX API](api.html)

Using StAX

[Oracle's Streaming XML Parser Implementation](parser.html)

[Example Code](example.html)

[Further Information](info.html)

[Home Page](../../index.html)
>
[Java API for XML Processing (JAXP)](../index.html)
>
[Streaming API for XML](index.html)

[« Previous](api.html) • [Trail](../TOC.html) • [Next »](parser.html)

# Using StAX

In general, StAX programmers create XML stream readers, writers, and events by using
the XMLInputFactory, XMLOutputFactory, and XMLEventFactory classes. Configuration is done by setting properties on
the factories, whereby implementation-specific settings can be passed to the underlying implementation using
the setProperty method on the factories. Similarly, implementation-specific settings can be queried using
the getProperty factory method.

The XMLInputFactory, XMLOutputFactory, and XMLEventFactory classes are described below, followed by discussions of resource
allocation, namespace and attribute management, error handling, and then finally reading and writing
streams using the cursor and iterator APIs.

## StAX Factory Classes

The StAX factory classes. XMLInputFactory, XMLOutputFactory, and XMLEventFactory, let you define and
configure implementation instances of XML stream reader, stream writer, and event classes.

### XMLInputFactory

The XMLInputFactory class lets you configure implementation instances of XML stream reader processors
created by the factory. New instances of the abstract class XMLInputFactory are created
by calling the newInstance method on the class. The static method XMLInputFactory.newInstance is
then used to create a new factory instance.

Deriving from JAXP, the XMLInputFactory.newInstance method determines the specific XMLInputFactory implementation class to load
by using the following lookup procedure:

1. Use the javax.xml.stream.XMLInputFactory system property.
2. Use the lib/xml.stream.properties file in the Java SE platform's Java Runtime Environment (JRE) directory.
3. Use the Services API, if available, to determine the classname by looking in the META-INF/services/javax.xml.stream.XMLInputFactory files in JAR files available to the JRE.
4. Use the platform default XMLInputFactory instance.

After getting a reference to an appropriate XMLInputFactory, an application can use the
factory to configure and create stream instances. [Table 5-4](#bnbep) lists the properties supported by
XMLInputFactory. See the StAX specification for a more detailed listing.

#### Table 5-4 javax.xml.stream.XMLInputFactory Properties

| Property | Description |
| isValidating | Turns on implementation-specific validation. |
| isCoalescing | **(Required)** Requires the processor to coalesce adjacent character data. |
| isNamespaceAware | Turns off namespace support. All implementations must support namespaces. Support for non-namespace-aware documents is optional. |
| isReplacingEntityReferences | **(Required)** Requires the processor to replace internal entity references with their replacement value and report them as characters or the set of events that describe the entity. |
| isSupportingExternalEntities | **(Required)** Requires the processor to resolve external parsed entities. |
| reporter | **(Required)** Sets and gets the implementation of the XMLReporter interface. |
| resolver | **(Required)** Sets and gets the implementation of the XMLResolver interface. |
| allocator | **(Required)** Sets and gets the implementation of the XMLEventAllocator interface. |

### XMLOutputFactory

New instances of the abstract class XMLOutputFactory are created by calling the newInstance
method on the class. The static method XMLOutputFactory.newInstance is then used to create a
new factory instance. The algorithm used to obtain the instance is the same
as for XMLInputFactory but references the javax.xml.stream.XMLOutputFactory system property.

XMLOutputFactory supports only one property, javax.xml.stream.isRepairingNamespaces. This property is required, and its
purpose is to create default prefixes and associate them with Namespace URIs. See
the StAX specification for more information.

### XMLEventFactory

New instances of the abstract class XMLEventFactory are created by calling the newInstance
method on the class. The static method XMLEventFactory.newInstance is then used to create a
new factory instance. This factory references the javax.xml.stream.XMLEventFactory property to instantiate the
factory. The algorithm used to obtain the instance is the same as for
XMLInputFactory and XMLOutputFactory but references the javax.xml.stream.XMLEventFactory system property.

There are no default properties for XMLEventFactory.

## Resources, Namespaces, and Errors

The StAX specification handles resource resolution, attributes and namespace, and errors and exceptions
as described below.

### Resource Resolution

The XMLResolver interface provides a means to set the method that resolves resources
during XML processing. An application sets the interface on XMLInputFactory, which then sets
the interface on all processors created by that factory instance.

### Attributes and Namespaces

Attributes are reported by a StAX processor using lookup methods and strings in
the cursor interface, and Attribute and Namespace events in the iterator interface.
Note here that namespaces are treated as attributes, although namespaces are reported separately
from attributes in both the cursor and iterator APIs. Note also that namespace
processing is optional for StAX processors. See the StAX specification for complete information about
namespace binding and optional namespace processing.

### Error Reporting and Exception Handling

All fatal errors are reported by way of the javax.xml.stream.XMLStreamException interface. All
nonfatal errors and warnings are reported using the javax.xml.stream.XMLReporter interface.

## Reading XML Streams

As described earlier in this lesson, the way you read XML streams
with a StAX processor—and more importantly, what you get back—varies significantly depending on whether
you are using the StAX cursor API or the event iterator API. The
following two sections describe how to read XML streams with each of these
APIs.

### Using XMLStreamReader

The XMLStreamReader interface in the StAX cursor API lets you read XML streams
or documents in a forward direction only, one item in the infoset at
a time. The following methods are available for pulling data from the stream
or skipping unwanted events:

* Get the value of an attribute
* Read XML content
* Determine whether an element has content or is empty
* Get indexed access to a collection of attributes
* Get indexed access to a collection of namespaces
* Get the name of the current event (if applicable)
* Get the content of the current event (if applicable)

Instances of XMLStreamReader have at any one time a single current event on
which its methods operate. When you create an instance of XMLStreamReader on a
stream, the initial current event is the START\_DOCUMENT state. The XMLStreamReader.next method can
then be used to step to the next event in the stream.

### Reading Properties, Attributes, and Namespaces

The XMLStreamReader.next method loads the properties of the next event in the stream.
You can then access those properties by calling the XMLStreamReader.getLocalName and XMLStreamReader.getText methods.

When the XMLStreamReader cursor is over a StartElement event, it reads the
name and any attributes for the event, including the namespace. All attributes for
an event can be accessed using an index value, and can also be
looked up by namespace URI and local name. Note, however, that only the
namespaces declared on the current StartEvent are available; previously declared namespaces are not
maintained, and redeclared namespaces are not removed.

### XMLStreamReader Methods

XMLStreamReader provides the following methods for retrieving information about namespaces and attributes:

```
int getAttributeCount();
String getAttributeNamespace(int index);
String getAttributeLocalName(int index);
String getAttributePrefix(int index);
String getAttributeType(int index);
String getAttributeValue(int index);
String getAttributeValue(String namespaceUri, String localName);
boolean isAttributeSpecified(int index);
```

Namespaces can also be accessed using three additional methods:

```
int getNamespaceCount();
String getNamespacePrefix(int index);
String getNamespaceURI(int index);
```

### Instantiating an XMLStreamReader

This example, taken from the StAX specification, shows how to instantiate an input
factory, create a reader, and iterate over the elements of an XML stream:

```
XMLInputFactory f = XMLInputFactory.newInstance();
XMLStreamReader r = f.createXMLStreamReader( ... );
while(r.hasNext()) {
    r.next();
}
```

### Using XMLEventReader

The XMLEventReader API in the StAX event iterator API provides the means to
map events in an XML stream to allocated event objects that can be
freely reused, and the API itself can be extended to handle custom events.

XMLEventReader provides four methods for iteratively parsing XML streams:

* next: Returns the next event in the stream
* nextEvent: Returns the next typed XMLEvent
* hasNext: Returns true if there are more events to process in the stream
* peek: Returns the event but does not iterate to the next event

For example, the following code snippet illustrates the XMLEventReader method declarations:

```
package javax.xml.stream;
import java.util.Iterator;
public interface XMLEventReader extends Iterator {
    public Object next();
    public XMLEvent nextEvent() throws XMLStreamException;
    public boolean hasNext();
    public XMLEvent peek() throws XMLStreamException;
    ...
}
```

To read all events on a stream and then print them, you
could use the following:

```
while(stream.hasNext()) {
    XMLEvent event = stream.nextEvent();
    System.out.print(event);
}
```

### Reading Attributes

You can access attributes from their associated javax.xml.stream.StartElement, as follows:

```
public interface StartElement extends XMLEvent {
    public Attribute getAttributeByName(QName name);
    public Iterator getAttributes();
}
```

You can use the getAttributes method on the StartElement interface to use
an Iterator over all the attributes declared on that StartElement.

### Reading Namespaces

Similar to reading attributes, namespaces are read using an Iterator created by
calling the getNamespaces method on the StartElement interface. Only the namespace for the current
StartElement is returned, and an application can get the current namespace context by
using StartElement.getNamespaceContext.

## Writing XML Streams

StAX is a bidirectional API, and both the cursor and event iterator APIs
have their own set of interfaces for writing XML streams. As with
the interfaces for reading streams, there are significant differences between the writer APIs for
cursor and event iterator. The following sections describe how to write XML streams
using each of these APIs.

### Using XMLStreamWriter

The XMLStreamWriter interface in the StAX cursor API lets applications write back to
an XML stream or create entirely new streams. XMLStreamWriter has methods that let
you:

* Write well-formed XML
* Flush or close the output
* Write qualified names

Note that XMLStreamWriter implementations are not required to perform well-formedness or validity checks
on input. While some implementations may perform strict error checking, others may not.
The rules you implement are applied to properties defined in the XMLOutputFactory class.

The writeCharacters method is used to escape characters such as &, <, >, and
". Binding prefixes can be handled by either passing the actual value for
the prefix, by using the setPrefix method, or by setting the property for
defaulting namespace declarations.

The following example, taken from the StAX specification, shows how to instantiate an
output factory, create a writer, and write XML output:

```
XMLOutputFactory output = XMLOutputFactory.newInstance();
XMLStreamWriter writer = output.createXMLStreamWriter( ... );
writer.writeStartDocument();
writer.setPrefix("c","http://c");
writer.setDefaultNamespace("http://c");
writer.writeStartElement("http://c","a");
writer.writeAttribute("b","blah");
writer.writeNamespace("c","http://c");
writer.writeDefaultNamespace("http://c");
writer.setPrefix("d","http://c");
writer.writeEmptyElement("http://c","d");
writer.writeAttribute("http://c","chris","fry");
writer.writeNamespace("d","http://c");
writer.writeCharacters("Jean Arp");
writer.writeEndElement();
writer.flush();
```

This code generates the following XML (new lines are non-normative):

```
<?xml version=’1.0’ encoding=’utf-8’?>
<a b="blah" xmlns:c="http://c" xmlns="http://c">
<d:d d:chris="fry" xmlns:d="http://c"/>Jean Arp</a>
```

### Using XMLEventWriter

The XMLEventWriter interface in the StAX event iterator API lets applications write back
to an XML stream or create entirely new streams. This API can be
extended, but the main API is as follows:

```
public interface XMLEventWriter {
    public void flush() throws XMLStreamException;
    public void close() throws XMLStreamException;
    public void add(XMLEvent e) throws XMLStreamException;
    // ... other methods not shown.
}
```

Instances of XMLEventWriter are created by an instance of XMLOutputFactory. Stream events are
added iteratively, and an event cannot be modified after it has been added
to an event writer instance.

### Attributes, Escaping Characters, Binding Prefixes

StAX implementations are required to buffer the last StartElement until an event other
than Attribute or Namespace is added or encountered in the stream. This means
that when you add an Attribute or a Namespace to a stream,
it is appended the current StartElement event.

You can use the Characters method to escape characters like &, <, >, and
".

The setPrefix(...) method can be used to explicitly bind a prefix for use
during output, and the getPrefix(...) method can be used to get the current
prefix. Note that by default, XMLEventWriter adds namespace bindings to its internal
namespace map. Prefixes go out of scope after the corresponding EndElement for the event
in which they are bound.

[« Previous](api.html)
•
[Trail](../TOC.html)
•
[Next »](parser.html)

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

**Previous page:** StAX API
  
**Next page:** Oracle's Streaming XML Parser Implementation




A browser with JavaScript enabled is required for this page to operate properly.