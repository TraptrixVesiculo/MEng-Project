[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Java API for XML Processing (JAXP)
  
**Lesson:** Streaming API for XML

[Streaming API for XML](index.html)

Why StAX?

[StAX API](api.html)

[Using StAX](using.html)

[Oracle's Streaming XML Parser Implementation](parser.html)

[Example Code](example.html)

[Further Information](info.html)

[Home Page](../../index.html)
>
[Java API for XML Processing (JAXP)](../index.html)
>
[Streaming API for XML](index.html)

[« Previous](index.html) • [Trail](../TOC.html) • [Next »](api.html)

# Why StAX?

The StAX project was spearheaded by BEA with support from Sun Microsystems, and
the JSR 173 specification passed the Java Community Process final approval ballot in
March, 2004 (
<http://jcp.org/en/jsr/detail?id=173>). The primary goal of the StAX API is to
give “parsing control to the programmer by exposing a simple iterator based API.
This allows the programmer to ask for the next event (pull the event)
and allows state to be stored in procedural fashion.” StAX was created to
address limitations in the two most prevalent parsing APIs, SAX and DOM.

## Streaming versus DOM

Generally speaking, there are two programming models for working with XML infosets: **streaming**
and the **document object model** (DOM).

The DOM model involves creating in-memory objects representing an entire document tree and
the complete infoset state for an XML document. Once in memory, DOM trees
can be navigated freely and parsed arbitrarily, and as such provide maximum flexibility
for developers. However, the cost of this flexibility is a potentially large memory
footprint and significant processor requirements, because the entire representation of the document must
be held in memory as objects for the duration of the document processing.
This may not be an issue when working with small documents, but memory
and processor requirements can escalate quickly with document size.

Streaming refers to a programming model in which XML infosets are transmitted and
parsed serially at application runtime, often in real time, and often from dynamic
sources whose contents are not precisely known beforehand. Moreover, stream-based parsers can start
generating output immediately, and infoset elements can be discarded and garbage collected immediately
after they are used. While providing a smaller memory footprint, reduced processor requirements, and
higher performance in certain situations, the primary trade-off with stream processing is that
you can only see the infoset state at one location at a time
in the document. You are essentially limited to the “cardboard tube” view of
a document, the implication being that you need to know what processing you
want to do before reading the XML document.

Streaming models for XML processing are particularly useful when your application has strict
memory limitations, as with a cellphone running the Java Platform, Micro Edition (Java
ME platform), or when your application needs to process several requests simultaneously, as
with an application server. In fact, it can be argued that the majority
of XML business logic can benefit from stream processing, and does not require
the in-memory maintenance of entire DOM trees.

## Pull Parsing versus Push Parsing

Streaming **pull parsing** refers to a programming model in which a client application calls
methods on an XML parsing library when it needs to interact with an
XML infoset—that is, the client only gets (pulls) XML data when it explicitly
asks for it.

Streaming **push parsing** refers to a programming model in which an XML parser sends
(pushes) XML data to the client as the parser encounters elements in an
XML infoset—that is, the parser sends the data whether or not the client
is ready to use it at that time.

Pull parsing provides several advantages over push parsing when working with XML streams:

* With pull parsing, the client controls the application thread, and can call methods on the parser when needed. By contrast, with push processing, the parser controls the application thread, and the client can only accept invocations from the parser.
* Pull parsing libraries can be much smaller and the client code to interact with those libraries much simpler than with push libraries, even for more complex documents.
* Pull clients can read multiple documents at one time with a single thread.
* A StAX pull parser can filter XML documents such that elements unnecessary to the client can be ignored, and it can support XML views of non-XML data.

## StAX Use Cases

The StAX specification defines a number of use cases for the API:

* Data binding

  + Unmarshalling an XML document
  + Marshalling an XML document
  + Parallel document processing
  + Wireless communication
* Simple Object Access Protocol (SOAP) message processing

  + Parsing simple predictable structures
  + Parsing graph representations with forward references
  + Parsing Web Services Description Language (WSDL)
* Virtual data sources

  + Viewing as XML data stored in databases
  + Viewing data in Java objects created by XML data binding
  + Navigating a DOM tree as a stream of events
* Parsing specific XML vocabularies
* Pipelined XML processing

A complete discussion of all these use cases is beyond the scope
of this lesson. Please refer to the StAX specification for further information.

## Comparing StAX to Other JAXP APIs

As an API in the JAXP family, StAX can be compared, among
other APIs, to SAX, TrAX, and JDOM. Of the latter two, StAX is
not as powerful or flexible as TrAX or JDOM, but neither does it
require as much memory or processor load to be useful, and StAX can,
in many cases, outperform the DOM-based APIs. The same arguments outlined above, weighing
the cost/benefits of the DOM model versus the streaming model, apply here.

With this in mind, the closest comparisons can be made between StAX and
SAX, and it is here that StAX offers features that are beneficial
in many cases; some of these include:

* StAX-enabled clients are generally easier to code than SAX clients. While it can be argued that SAX parsers are marginally easier to write, StAX parser code can be smaller and the code necessary for the client to interact with the parser simpler.
* StAX is a bidirectional API, meaning that it can both read and write XML documents. SAX is read only, so another API is needed if you want to write XML documents.
* SAX is a push API, whereas StAX is pull. The trade-offs between push and pull APIs outlined above apply here.

[Table 5-1](#bnbeb) summarizes the comparative features of StAX, SAX, DOM, and TrAX (table adapted
from “Does StAX Belong in Your XML Toolbox?” at
<http://www.developer.com/xml/article.php/3397691> by Jeff Ryan).

Table 5-1 XML Parser API Feature Summary

| Feature | StAX | SAX | DOM | TrAX |
| API Type | Pull, streaming | Push, streaming | In memory tree | XSLT Rule |
| Ease of Use | High | Medium | High | Medium |
| XPath Capability | No | No | Yes | Yes |
| CPU and Memory Efficiency | Good | Good | Varies | Varies |
| Forward Only | Yes | Yes | No | No |
| Read XML | Yes | Yes | Yes | Yes |
| Write XML | Yes | No | Yes | Yes |
| Create, Read, Update, Delete | No | No | Yes | No |

[« Previous](index.html)
•
[Trail](../TOC.html)
•
[Next »](api.html)

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

**Previous page:** Streaming API for XML
  
**Next page:** StAX API




A browser with JavaScript enabled is required for this page to operate properly.