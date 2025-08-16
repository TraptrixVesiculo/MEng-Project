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

Oracle's Streaming XML Parser Implementation

[Example Code](example.html)

[Further Information](info.html)

[Home Page](../../index.html)
>
[Java API for XML Processing (JAXP)](../index.html)
>
[Streaming API for XML](index.html)

[« Previous](using.html) • [Trail](../TOC.html) • [Next »](example.html)

# Oracle's Streaming XML Parser Implementation

Application Server 9.1 includes Sun Microsystems’ JSR 173 (StAX) implementation, called the Sun
Java Streaming XML Parser (referred to as Streaming XML Parser). The Streaming XML
Parser is a high-speed, non-validating, W3C XML 1.0 and Namespace 1.0-compliant streaming XML
pull parser built upon the Xerces2 codebase.

In Sun’s Streaming XML Parser implementation, the Xerces2 lower layers, particularly the Scanner
and related classes, have been redesigned to behave in a pull fashion. In
addition to the changes in the lower layers, the Streaming XML Parser includes
additional StAX-related functionality and many performance-enhancing improvements. The Streaming XML Parser is implemented in
the appserv-ws.jar and javaee.jar files, both of which are located in the *install\_dir*/lib/
directory.

Included with the JAXP reference implementation are StAX code examples, located in the
*INSTALL\_DIR*/jaxp-*version*/samples/stax directory, that illustrate how Sun’s Streaming XML Parser implementation works. These examples
are described in
[Example Code](example.html).

Before you proceed with the example code, there are two aspects of
the Streaming XML Parser of which you should be aware:

* [Reporting CDATA Events](#bnbfj)
* [Streaming XML Parser Factories Implementation](#bnbfk)

These topics are discussed below.

## Reporting CDATA Events

The javax.xml.stream.XMLStreamReader implemented in the Streaming XML Parser does not report CDATA events.
If you have an application that needs to receive such events, configure the
XMLInputFactory to set the following implementation-specific report-cdata-event property:

```

XMLInputFactory factory = XMLInptuFactory.newInstance();
factory.setProperty("report-cdata-event", Boolean.TRUE);

```

## Streaming XML Parser Factories Implementation

Most applications do not need to know the factory implementation class name. Just
adding the javaee.jar and appserv-ws.jar files to the classpath is sufficient for
most applications because these two jars supply the factory implementation classname for various
Streaming XML Parser properties under the META-INF/services directory—for example, javax.xml.stream.XMLInputFactory, javax.xml.stream.XMLOutputFactory, and javax.xml.stream.XMLEventFactory—which is the
third step of a lookup operation when an application asks for the
factory instance. See the Javadoc for the XMLInputFactory.newInstance method for more information about the
lookup mechanism.

However, there may be scenarios when an application would like to know about
the factory implementation class name and set the property explicitly. These scenarios could
include cases where there are multiple JSR 173 implementations in the classpath and
the application wants to choose one, perhaps one that has superior performance, contains
a crucial bug fix, or suchlike.

If an application sets the SystemProperty, it is the first step in a
lookup operation, and so obtaining the factory instance would be fast compared to
other options; for example:

```

javax.xml.stream.XMLInputFactory -->
     com.sun.xml.stream.ZephyrParserFactory
javax.xml.stream.XMLOutputFactory -->
     com.sun.xml.stream.ZephyrWriterFactor
javax.xml.stream.XMLEventFactory -->
     com.sun.xml.stream.events.ZephyrEventFactory

```

[« Previous](using.html)
•
[Trail](../TOC.html)
•
[Next »](example.html)

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

**Previous page:** Using StAX
  
**Next page:** Example Code




A browser with JavaScript enabled is required for this page to operate properly.