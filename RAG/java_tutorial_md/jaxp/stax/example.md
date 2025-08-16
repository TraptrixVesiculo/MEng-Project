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

[Using StAX](using.html)

[Oracle's Streaming XML Parser Implementation](parser.html)

Example Code

[Further Information](info.html)

[Home Page](../../index.html)
>
[Java API for XML Processing (JAXP)](../index.html)
>
[Streaming API for XML](index.html)

[« Previous](parser.html) • [Trail](../TOC.html) • [Next »](info.html)

# Example Code

This section steps through the example StAX code included in the JAXP reference
implementation bundle. All example directories used in this section are located in the
*INSTALL\_DIR*/jaxp-*version*/samples/stax directory.

The topics covered in this section are as follows:

* [Example Code Organization](#bnbfm)
* [Example XML Document](#bnbfn)
* [Cursor Example](#bnbfo)
* [Cursor-to-Event Example](#bnbft)
* [Event Example](#bnbfz)
* [Filter Example](#bnbgh)
* [Read-and-Write Example](#bnbgq)
* [Writer Example](#bnbgx)

## Example Code Organization

The *INSTALL\_DIR*/jaxp-*version*/samples/stax directory contains the six StAX example directories:

* **Cursor example**: The cursor directory contains CursorParse.java, which illustrates how to use the XMLStreamReader (cursor) API to read an XML file.
* **Cursor-to-Event example**: The cursor2event directory contains CursorApproachEventObject.java, which illustrates how an application can get information as an XMLEvent object when using the cursor API.
* **Event example**: The event directory contains EventParse.java, which illustrates how to use the XMLEventReader (event iterator) API to read an XML file.
* **Filter example**: The filter directory contains MyStreamFilter.java, which illustrates how to use the StAX Stream Filter APIs. In this example, the filter accepts only StartElement and EndElement events, and filters out the remainder of the events.
* **Read-and-Write example**: The readnwrite directory contains EventProducerConsumer.java, which illustrates how the StAX producer/consumer mechanism can be used to simultaneously read and write XML streams.
* **Writer example**: The writer directory contains CursorWriter.java, which illustrates how to use XMLStreamWriter to write an XML file programatically.

All the StAX examples except for the Writer example use an example
XML document, BookCatalog.xml.

## Example XML Document

The example XML document, BookCatalog.xml, used by most of the StAX example classes,
is a simple book catalog based on the common BookCatalogue namespace. The contents
of BookCatalog.xml are listed below:

```

<?xml version="1.0" encoding="UTF-8"?>
<BookCatalogue xmlns="http://www.publishing.org">
    <Book>
        <Title>Yogasana Vijnana: the Science of Yoga</Title>
        <author>Dhirendra Brahmachari</Author>
        <Date>1966</Date>
        <ISBN>81-40-34319-4</ISBN>
        <Publisher>Dhirendra Yoga Publications</Publisher>
        <Cost currency="INR">11.50</Cost>
    </Book>
    <Book>
        <Title>The First and Last Freedom</Title>
        <Author>J. Krishnamurti</Author>
        <Date>1954</Date>
        <ISBN>0-06-064831-7</ISBN>
        <Publisher>Harper &amp; Row</Publisher>
        <Cost currency="USD">2.95</Cost>
    </Book>
</BookCatalogue>

```

## Cursor Example

Located in the *INSTALL\_DIR*/jaxp-*version*/samples/stax/cursor/ directory, CursorParse.java demonstrates using the StAX cursor API
to read an XML document. In the Cursor example, the application instructs the
parser to read the next event in the XML input stream by calling
next().

Note that next() just returns an integer constant corresponding to an underlying event
where the parser is positioned. The application needs to call the relevant function
to get more information related to the underlying event.

You can imagine this approach as a virtual cursor moving across the XML
input stream. There are various accessor methods which can be called when that
virtual cursor is at a particular event.

### Stepping through Events

In this example, the client application pulls the next event in the XML
stream by calling the next method on the parser; for example:

```

try {
    for (int i = 0 ; i < count ; i++) {
        // pass the file name.. all relative entity
        // references will be resolved against this as
        // base URI.
        XMLStreamReader xmlr =
            xmlif.createXMLStreamReader(filename,
                new FileInputStream(filename));
        // when XMLStreamReader is created, it is positioned
        // at START_DOCUMENT event.
        int eventType = xmlr.getEventType();
        printEventType(eventType);
        printStartDocument(xmlr);
        // check if there are more events in the input stream
        while(xmlr.hasNext()) {
            eventType = xmlr.next();
            printEventType(eventType);
            // these functions print the information about
            // the particular event by calling the relevant
            // function
            printStartElement(xmlr);
            printEndElement(xmlr);
            printText(xmlr);
            printPIData(xmlr);
            printComment(xmlr);
        }
    }
}

```

Note that next just returns an integer constant corresponding to the event underlying
the current cursor location. The application calls the relevant function to get more
information related to the underlying event. There are various accessor methods which can
be called when the cursor is at a particular event.

### Returning String Representations

Because the next method only returns integers corresponding to underlying event types, you
typically need to map these integers to string representations of the events; for
example:

```

public final static String getEventTypeString(int eventType) {
    switch (eventType) {
        case XMLEvent.START_ELEMENT:
            return "START_ELEMENT";
        case XMLEvent.END_ELEMENT:
            return "END_ELEMENT";
        case XMLEvent.PROCESSING_INSTRUCTION:
            return "PROCESSING_INSTRUCTION";
        case XMLEvent.CHARACTERS:
            return "CHARACTERS";
        case XMLEvent.COMMENT:
            return "COMMENT";
        case XMLEvent.START_DOCUMENT:
            return "START_DOCUMENT";
        case XMLEvent.END_DOCUMENT:
            return "END_DOCUMENT";
        case XMLEvent.ENTITY_REFERENCE:
            return "ENTITY_REFERENCE";
        case XMLEvent.ATTRIBUTE:
            return "ATTRIBUTE";
        case XMLEvent.DTD:
            return "DTD";
        case XMLEvent.CDATA:
            return "CDATA";
        case XMLEvent.SPACE:
            return "SPACE";
    }
    return "UNKNOWN_EVENT_TYPE , " + eventType;
}

```

### To Run the Cursor Example

1. **To compile and run the cursor example, in a terminal window, go to
   the *INSTALL\_DIR*/jaxp-*version*/samples/ directory and type the following:**

```

javac stax/cursor/*.java

```

2. **Run the CursorParse sample on the BookCatalogue.xml file, with the following command.**

   CursorParse will print out each element of the BookCatalogue.xml file.

```

java stax/event/CursorParse stax/data/BookCatalogue.xml

```

## Cursor-to-Event Example

Located in the *tut-install*/javaeetutorial5/examples/stax/cursor2event/ directory, CursorApproachEventObject.java demonstrates how to get information returned by
an XMLEvent object even when using the cursor API.

The idea here is that the cursor API’s XMLStreamReader returns integer constants corresponding
to particular events, while the event iterator API’s XMLEventReader returns immutable and persistent event
objects. XMLStreamReader is more efficient, but XMLEventReader is easier to use, because
all the information related to a particular event is encapsulated in a returned
XMLEvent object. However, the disadvantage of the event approach is the extra overhead
of creating objects for every event, which consumes both time and memory.

With this mind, XMLEventAllocator can be used to get event information as an
XMLEvent object, even when using the cursor API.

### Instantiating an XMLEventAllocator

The first step is to create a new XMLInputFactory and instantiate an XMLEventAllocator:

```

XMLInputFactory xmlif = XMLInputFactory.newInstance();
System.out.println("FACTORY: " + xmlif);
xmlif.setEventAllocator(new XMLEventAllocatorImpl());
allocator = xmlif.getEventAllocator();
XMLStreamReader xmlr = xmlif.createXMLStreamReader(filename,
    new FileInputStream(filename));

```

### Creating an Event Iterator

The next step is to create an event iterator:

```

int eventType = xmlr.getEventType();
while(xmlr.hasNext()){
    eventType = xmlr.next();
    //Get all "Book" elements as XMLEvent object
    if(eventType == XMLStreamConstants.START_ELEMENT &&
        xmlr.getLocalName().equals("Book")){
        //get immutable XMLEvent
        StartElement event = getXMLEvent(xmlr).asStartElement();
        System.out.println("EVENT: " + event.toString());
    }
}

```

### Creating the Allocator Method

The final step is to create the XMLEventAllocator method:

```

private static XMLEvent getXMLEvent(XMLStreamReader reader)
         throws XMLStreamException {
    return allocator.allocate(reader);
}

```

### To Run the Cursor-to-Event Example

1. **To compile and run the cursor—to—event example, in a terminal window, go to
   the *INSTALL\_DIR*/jaxp-*version*/samples/ directory and type the following:**

```

javac -classpath ../lib/jaxp-ri.jar stax/cursor2event/*.java

```

2. **Run the CursorApproachEventObject sample on the BookCatalogue.xml file, with the following command.**

```

java stax/cursor2event/CursorApproachEventObject stax/data/BookCatalogue.xml

```

CursorApproachEventObject will print out the list of events defined by the BookCatalogue.xml file.

## Event Example

Located in the *INSTALL\_DIR*/jaxp-*version*/samples/stax/event/ directory, EventParse.java demonstrates how to use the StAX
event API to read an XML document.

### Creating an Input Factory

The first step is to create a new instance of XMLInputFactory:

```

XMLInputFactory factory = XMLInputFactory.newInstance();
System.out.println("FACTORY: " + factory);

```

### Creating an Event Reader

The next step is to create an instance of XMLEventReader:

```

XMLEventReader r = factory.createXMLEventReader(filename,
     new FileInputStream(filename));

```

### Creating an Event Iterator

The third step is to create an event iterator:

```

XMLEventReader r = factory.createXMLEventReader(filename,
     new FileInputStream(filename));
while(r.hasNext()) {
    XMLEvent e = r.nextEvent();
    System.out.println(e.toString());
}

```

### Getting the Event Stream

The final step is to get the underlying event stream:

```

public final static String getEventTypeString(int eventType) {
    switch (eventType) {
        case XMLEvent.START_ELEMENT:
            return "START_ELEMENT";
        case XMLEvent.END_ELEMENT:
            return "END_ELEMENT";
        case XMLEvent.PROCESSING_INSTRUCTION:
            return "PROCESSING_INSTRUCTION";
        case XMLEvent.CHARACTERS:
            return "CHARACTERS";
        case XMLEvent.COMMENT:
            return "COMMENT";
        case XMLEvent.START_DOCUMENT:
            return "START_DOCUMENT";
        case XMLEvent.END_DOCUMENT:
            return "END_DOCUMENT";
        case XMLEvent.ENTITY_REFERENCE:
            return "ENTITY_REFERENCE";
        case XMLEvent.ATTRIBUTE:
            return "ATTRIBUTE";
        case XMLEvent.DTD:
            return "DTD";
        case XMLEvent.CDATA:
            return "CDATA";
        case XMLEvent.SPACE:
            return "SPACE";
    }
    return "UNKNOWN_EVENT_TYPE " + "," + eventType;
}

```

### Returning the Output

When you run the Event example, the EventParse class is compiled, and the
XML stream is parsed as events and returned to STDOUT. For example,
an instance of the Author element is returned as:

```

<[’http://www.publishing.org’]::Author>
    Dhirendra Brahmachari
</[’http://www.publishing.org’]::Author>

```

Note in this example that the event comprises an opening and closing tag,
both of which include the namespace. The content of the element is
returned as a string within the tags.

Similarly, an instance of the Cost element is returned as:

```

<[’http://www.publishing.org’]::Cost currency=’INR’>
    11.50
</[’http://www.publishing.org’]::Cost

```

In this case, the currency attribute and value are returned in the opening
tag for the event.

### To Run the Event Example

1. **To compile and run the event example, in a terminal window, go to
   the *INSTALL\_DIR*/jaxp-*version*/samples/ directory and type the following:**

   ```

   javac -classpath ../lib/jaxp-ri.jar stax/event/*.java

   ```
2. **Run the EventParse sample on the BookCatalogue.xml file, with the following command.**

   ```

   java stax/event/EventParse stax/data/BookCatalogue.xml

   ```

   EventParse will print out the data from all the elements defined by the
   BookCatalogue.xml file.

## Filter Example

Located in the *INSTALL\_DIR*/jaxp-*version*/samples/stax/filter/ directory, MyStreamFilter.java demonstrates how to use the StAX
stream filter API to filter out events not needed by your application. In
this example, the parser filters out all events except StartElement and EndElement.

### Implementing the StreamFilter Class

The MyStreamFilter class implements javax.xml.stream.StreamFilter:

```

public class MyStreamFilter
     implements javax.xml.stream.StreamFilter {

```

### Creating an Input Factory

The next step is to create an instance of XMLInputFactory. In this case,
various properties are also set on the factory:

```

XMLInputFactory xmlif = null ;
try {
    xmlif = XMLInputFactory.newInstance();
    xmlif.setProperty(
        XMLInputFactory.IS_REPLACING_ENTITY_REFERENCES,
        Boolean.TRUE);
    xmlif.setProperty(
        XMLInputFactory.IS_SUPPORTING_EXTERNAL_ENTITIES,
        Boolean.FALSE);
    xmlif.setProperty(XMLInputFactory.IS_NAMESPACE_AWARE,
        Boolean.TRUE);
    xmlif.setProperty(XMLInputFactory.IS_COALESCING,
        Boolean.TRUE);
} catch (Exception ex) {
    ex.printStackTrace();
}
System.out.println("FACTORY: " + xmlif);
System.out.println("filename = "+ filename);

```

### Creating the Filter

The next step is to instantiate a file input stream and create
the stream filter:

```

FileInputStream fis = new FileInputStream(filename);
                
XMLStreamReader xmlr = xmlif.createFilteredReader(
    xmlif.createXMLStreamReader(fis), new MyStreamFilter());

int eventType = xmlr.getEventType();
printEventType(eventType);
while(xmlr.hasNext()) {
    eventType = xmlr.next();
    printEventType(eventType);
    printName(xmlr,eventType);
    printText(xmlr);
    if (xmlr.isStartElement()) {
        printAttributes(xmlr);
    }
    printPIData(xmlr);
    System.out.println("-----------------------------");
}

```

### Capturing the Event Stream

The next step is to capture the event stream. This is done
in basically the same way as in the Event example.

### Filtering the Stream

The final step is to filter the stream:

```

public boolean accept(XMLStreamReader reader) {
    if (!reader.isStartElement() && !reader.isEndElement())
        return false;
    else
        return true;
}

```

### Returning the Output

When you run the Filter example, the MyStreamFilter class is compiled, and the
XML stream is parsed as events and returned to STDOUT. For example,
an Author event is returned as follows:

```

EVENT TYPE(1):START_ELEMENT
HAS NAME: Author
HAS NO TEXT
HAS NO ATTRIBUTES
-----------------------------
EVENT TYPE(2):END_ELEMENT
HAS NAME: Author
HAS NO TEXT
-----------------------------

```

Similarly, a Cost event is returned as follows:

```

EVENT TYPE(1):START_ELEMENT
HAS NAME: Cost
HAS NO TEXT

HAS ATTRIBUTES:
 ATTRIBUTE-PREFIX:
 ATTRIBUTE-NAMESP: null
ATTRIBUTE-NAME:   currency
ATTRIBUTE-VALUE: USD
ATTRIBUTE-TYPE:  CDATA

-----------------------------
EVENT TYPE(2):END_ELEMENT
HAS NAME: Cost
HAS NO TEXT
-----------------------------

```

See
[Iterator API](api.html#bnbee) and
[Reading XML Streams](using.html#bnbew) for a more detailed discussion of StAX event parsing.

### To Run the Filter Example

1. **To compile and run the Filter example, in a terminal window, go to
   the *INSTALL\_DIR*/jaxp-*version*/samples/ directory and type the following:**

   ```

   javac -classpath ../lib/jaxp-ri.jar stax/filter/*.java

   ```
2. **Run the MyStreamFilter sample on the BookCatalogue.xml file, with the following command.
   This example requires the java.endorsed.dirs system property to be set, to point
   to the samples/lib directory.** 

   ```

   java -Djava.endorsed.dirs=../lib stax/filter/MyStreamFilter -f stax/data/BookCatalogue.xml

   ```

   MyStreamFilter will print out the events defined by the BookCatalogue.xml file as an
   XML stream.

## Read-and-Write Example

Located in the *INSTALL\_DIR*/jaxp-*version*/samples/stax/readnwrite/ directory, EventProducerConsumer.java demonstrates how to use a StAX
parser simultaneously as both a producer and a consumer.

The StAX XMLEventWriter API extends from the XMLEventConsumer interface, and is referred
to as an **event consumer**. By contrast, XMLEventReader is an **event producer**. StAX supports simultaneous reading
and writing, such that it is possible to read from one XML stream
sequentially and simultaneously write to another stream.

The Read-and-Write example shows how the StAX producer/consumer mechanism can be used to
read and write simultaneously. This example also shows how a stream can be
modified and how new events can be added dynamically and then written to
a different stream.

### Creating an Event Producer/Consumer

The first step is to instantiate an event factory and then create
an instance of an event producer/consumer:

```

XMLEventFactory m_eventFactory = XMLEventFactory.newInstance();
public EventProducerConsumer() {
}
...
try {
    EventProducerConsumer ms = new EventProducerConsumer();
    
    XMLEventReader reader =
        XMLInputFactory.newInstance().createXMLEventReader(
            new java.io.FileInputStream(args[0]));
    XMLEventWriter writer =
        XMLOutputFactory.newInstance().createXMLEventWriter(
            System.out);

```

### Creating an Iterator

The next step is to create an iterator to parse the stream:

```

while(reader.hasNext()) {
    XMLEvent event = (XMLEvent)reader.next();
    if (event.getEventType() == event.CHARACTERS) {
        writer.add(ms.getNewCharactersEvent(event.asCharacters()));
    } else {
        writer.add(event);
    }
}
writer.flush();

```

### Creating a Writer

The final step is to create a stream writer in the form
of a new Character event:

```

Characters getNewCharactersEvent(Characters event) {
    if (event.getData().equalsIgnoreCase("Name1")) {
        return m_eventFactory.createCharacters(
            Calendar.getInstance().getTime().toString());
    }
    //else return the same event
    else {
        return event;
    }
}

```

### Returning the Output

When you run the Read-and-Write example, the EventProducerConsumer class is compiled, and
the XML stream is parsed as events and written back to STDOUT. The
output is the contents of the BookCatalog.xml file described in [Example XML Document](#bnbfn).

### To Run the Read-and-Write Example

1. **To compile and run the Read—and—Write example, in a terminal window, go to
   the *INSTALL\_DIR*/jaxp-*version*/samples/ directory and type the following:**

   ```

   javac -classpath ../lib/jaxp-ri.jar stax/readnwrite/*.java

   ```
2. **Run the EventProducerConsumer sample on the BookCatalogue.xml file, with the following command.**

   ```

   java stax/readnwrite/EventProducerConsumer stax/data/BookCatalogue.xml

   ```

   EventProducerConsumer will print out the content of the BookCatalogue.xml file.

## Writer Example

Located in the *INSTALL\_DIR*/jaxp-*version*/samples/stax/writer/ directory, CursorWriter.java demonstrates how to use the StAX
cursor API to write an XML stream.

### Creating the Output Factory

The first step is to create an instance of XMLOutputFactory:

```

XMLOutputFactory xof =  XMLOutputFactory.newInstance();

```

### Creating a Stream Writer

The next step is to create an instance of XMLStreamWriter:

```

XMLStreamWriter xtw = null;

```

### Writing the Stream

The final step is to write the XML stream. Note that the
stream is flushed and closed after the final EndDocument is written:

```

xtw = xof.createXMLStreamWriter(new FileWriter(fileName));
xtw.writeComment("all elements here are explicitly in the HTML namespace");
xtw.writeStartDocument("utf-8","1.0");
xtw.setPrefix("html", "http://www.w3.org/TR/REC-html40");
xtw.writeStartElement("http://www.w3.org/TR/REC-html40","html");
xtw.writeNamespace("html", "http://www.w3.org/TR/REC-html40");
xtw.writeStartElement("http://www.w3.org/TR/REC-html40","head");
xtw.writeStartElement("http://www.w3.org/TR/REC-html40","title");
xtw.writeCharacters("Frobnostication");
xtw.writeEndElement();
xtw.writeEndElement();
xtw.writeStartElement("http://www.w3.org/TR/REC-html40","body");
xtw.writeStartElement("http://www.w3.org/TR/REC-html40","p");
xtw.writeCharacters("Moved to");
xtw.writeStartElement("http://www.w3.org/TR/REC-html40","a");
xtw.writeAttribute("href","http://frob.com");
xtw.writeCharacters("here");
xtw.writeEndElement();
xtw.writeEndElement();
xtw.writeEndElement();
xtw.writeEndElement();
xtw.writeEndDocument();
xtw.flush();
xtw.close();

```

### Returning the Output

When you run the Writer example, the CursorWriter class is compiled, and the
XML stream is parsed as events and written to a file named dist/CursorWriter-Output:

```

<!--all elements here are explicitly in the HTML namespace-->
<?xml version="1.0" encoding="utf-8"?>
<html:html xmlns:html="http://www.w3.org/TR/REC-html40">
<html:head>
<html:title>Frobnostication</html:title></html:head>
<html:body>
<html:p>Moved to <html:a href="http://frob.com">here</html:a>
</html:p>
</html:body>
</html:html>

```

In the actual dist/CursorWriter-Output file, this stream is written without any line breaks;
the breaks have been added here to make the listing easier to read.
In this example, as with the object stream in the Event example, the
namespace prefix is added to both the opening and closing HTML tags. Adding
this prefix is not required by the StAX specification, but it is good
practice when the final scope of the output stream is not definitively known.

### To Run the Writer Example

1. **To compile and run the Writer example, in a terminal window, go to
   the *INSTALL\_DIR*/jaxp-*version*/samples/ directory and type the following:**

   ```

   javac -classpath ../lib/jaxp-ri.jar stax/writer/*.java

   ```
2. **Run the CursorWriter sample, specifying the name of the file the output should
   be written to.**

   ```

   java stax/writer/CursorWriter -f output_file

   ```

   CursorWriter will create an output file of the appropriate name, which contains the
   data shown in [Returning the Output](#bnbhb).

[« Previous](parser.html)
•
[Trail](../TOC.html)
•
[Next »](info.html)

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

**Previous page:** Oracle's Streaming XML Parser Implementation
  
**Next page:** Further Information




A browser with JavaScript enabled is required for this page to operate properly.