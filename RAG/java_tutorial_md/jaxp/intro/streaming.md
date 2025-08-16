[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Java API for XML Processing (JAXP)
  
**Lesson:** Introduction to JAXP

[Introduction to JAXP](index.html)

[Overview of the Packages](package.html)

[Simple API for XML APIs](simple.html)

[Document Object Model APIs](dom.html)

[Extensible Stylesheet Language Transformations APIs](extensible.html)

Streaming API for XML APIs

[Finding the JAXP Sample Programs](sample.html)

[Where Do You Go From Here?](next.html)

[Home Page](../../index.html)
>
[Java API for XML Processing (JAXP)](../index.html)
>
[Introduction to JAXP](index.html)

[« Previous](extensible.html) • [Trail](../TOC.html) • [Next »](sample.html)

# Streaming API for XML APIs

StAX is the latest API in the JAXP family, and provides an
alternative to SAX, DOM, TrAX, and DOM for developers looking to do high-performance
stream filtering, processing, and modification, particularly with low memory and limited extensibility requirements.

To summarize, StAX provides a standard, bidirectional **pull parser** interface for streaming XML
processing, offering a simpler programming model than SAX and more efficient memory management
than DOM. StAX enables developers to parse and modify XML streams as events,
and to extend XML information models to allow application-specific additions. More detailed comparisons of
StAX with several alternative APIs are provided in
[Streaming API for XML](../stax
/index.html
), in
[Comparing StAX to Other JAXP APIs](../stax
/why.html#bnbea
).

## StAX Packages

The StAX APIs are defined in the packages shown in [Table 1-4](#gfoor).

Table 1-4 StAX Packages

| Package | Description |
| javax.xml.stream | Defines the XMLStreamReader interface, which is used to iterate over the elements of an XML document. The XMLStreamWriter interface specifies how the XML should be written. |
| javax.xml.transform.stax | Provides StAX-specific transformation APIs. |

[« Previous](extensible.html)
•
[Trail](../TOC.html)
•
[Next »](sample.html)

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

**Previous page:** Extensible Stylesheet Language Transformations APIs
  
**Next page:** Finding the JAXP Sample Programs




A browser with JavaScript enabled is required for this page to operate properly.