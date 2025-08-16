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

Extensible Stylesheet Language Transformations APIs

[Streaming API for XML APIs](streaming.html)

[Finding the JAXP Sample Programs](sample.html)

[Where Do You Go From Here?](next.html)

[Home Page](../../index.html)
>
[Java API for XML Processing (JAXP)](../index.html)
>
[Introduction to JAXP](index.html)

[« Previous](dom.html) • [Trail](../TOC.html) • [Next »](streaming.html)

# Extensible Stylesheet Language Transformations APIs

[Figure 1-3](#gceys) shows the XSLT APIs in action.

Figure 1-3 XSLT APIs

![XSLT APIs](../../figures/jaxp/intro/jaxpintro-xsltApi.gif)

A TransformerFactory object is instantiated and used to create a Transformer. The source
object is the input to the transformation process. A source object can be
created from a SAX reader, from a DOM, or from an input stream.

Similarly, the result object is the result of the transformation process. That object
can be a SAX event handler, a DOM, or an output stream.

When the transformer is created, it can be created from a set
of transformation instructions, in which case the specified transformations are carried out. If it
is created without any specific instructions, then the transformer object simply copies the
source to the result.

## XSLT Packages

The XSLT APIs are defined in the packages shown in [Table 1-3](#gcfbf).

Table 1-3 XSLT Packages

| Package | Description |
| javax.xml.transform | Defines the TransformerFactory and Transformer classes, which you use to get an object capable of doing transformations. After creating a transformer object, you invoke its transform() method, providing it with an input (source) and output (result). |
| javax.xml.transform.dom | Classes to create input (source) and output (result) objects from a DOM. |
| javax.xml.transform.sax | Classes to create input (source) objects from a SAX parser and output (result) objects from a SAX event handler. |
| javax.xml.transform.stream | Classes to create input (source) objects and output (result) objects from an I/O stream. |

[« Previous](dom.html)
•
[Trail](../TOC.html)
•
[Next »](streaming.html)

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

**Previous page:** Document Object Model APIs
  
**Next page:** Streaming API for XML APIs




A browser with JavaScript enabled is required for this page to operate properly.