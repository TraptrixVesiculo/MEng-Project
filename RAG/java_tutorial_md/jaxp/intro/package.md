[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Java API for XML Processing (JAXP)
  
**Lesson:** Introduction to JAXP

[Introduction to JAXP](index.html)

Overview of the Packages

[Simple API for XML APIs](simple.html)

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

[« Previous](index.html) • [Trail](../TOC.html) • [Next »](simple.html)

# Overview of the Packages

The SAX and DOM APIs are defined by the XML-DEV group and
by the W3C, respectively. The libraries that define those APIs are as follows:

* javax.xml.parsers: The JAXP APIs, which provide a common interface for different vendors' SAX and DOM parsers.
* org.w3c.dom: Defines the Document class (a DOM) as well as classes for all the components of a DOM.
* org.xml.sax: Defines the basic SAX APIs.
* javax.xml.transform: Defines the XSLT APIs that let you transform XML into other forms.
* javax.xml.stream: Provides StAX-specific transformation APIs.

The Simple API for XML (SAX) is the event-driven, serial-access mechanism that does
element-by-element processing. The API for this level reads and writes XML to a
data repository or the web. For server-side and high-performance applications, you will want
to fully understand this level. But for many applications, a minimal understanding will
suffice.

The DOM API is generally an easier API to use. It provides
a familiar tree structure of objects. You can use the DOM API to
manipulate the hierarchy of application objects it encapsulates. The DOM API is ideal
for interactive applications because the entire object model is present in memory, where
it can be accessed and manipulated by the user.

On the other hand, constructing the DOM requires reading the entire XML structure
and holding the object tree in memory, so it is much more
CPU- and memory-intensive. For that reason, the SAX API tends to be preferred
for server-side applications and data filters that do not require an in-memory representation of
the data.

The XSLT APIs defined in javax.xml.transform let you write XML data to a
file or convert it into other forms. As shown in the XSLT section
of this tutorial, you can even use it in conjunction with the SAX
APIs to convert legacy data to XML.

Finally, the StAX APIs defined in javax.xml.stream provide a streaming Java technology-based, event-driven,
pull-parsing API for reading and writing XML documents. StAX offers a simpler programming
model than SAX and more efficient memory management than DOM.

[« Previous](index.html)
•
[Trail](../TOC.html)
•
[Next »](simple.html)

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

**Previous page:** Introduction to JAXP
  
**Next page:** Simple API for XML APIs




A browser with JavaScript enabled is required for this page to operate properly.