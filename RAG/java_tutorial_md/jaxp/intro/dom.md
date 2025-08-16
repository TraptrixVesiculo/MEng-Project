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

Document Object Model APIs

[Extensible Stylesheet Language Transformations APIs](extensible.html)

[Streaming API for XML APIs](streaming.html)

[Finding the JAXP Sample Programs](sample.html)

[Where Do You Go From Here?](next.html)

[Home Page](../../index.html)
>
[Java API for XML Processing (JAXP)](../index.html)
>
[Introduction to JAXP](index.html)

[« Previous](simple.html) • [Trail](../TOC.html) • [Next »](extensible.html)

# Document Object Model APIs

[Figure 1-2](#gceza) shows the DOM APIs in action.

Figure 1-2 DOM APIs

![DOM APIs](../../figures/jaxp/intro/jaxpintro-domApi.gif)

You use the javax.xml.parsers.DocumentBuilderFactory class to get a DocumentBuilder instance, and you use
that instance to produce a Document object that conforms to the DOM specification. The
builder you get, in fact, is determined by the system property javax.xml.parsers.DocumentBuilderFactory, which selects
the factory implementation that is used to produce the builder. (The platform's default
value can be overridden from the command line.)

You can also use the DocumentBuilder newDocument() method to create an empty
Document that implements the org.w3c.dom.Document interface. Alternatively, you can use one of the builder's
parse methods to create a Document from existing XML data. The result is
a DOM tree like that shown in [Figure 1-2](#gceza).

---

**Note -** Although they are called objects, the entries in the DOM tree are actually
fairly low-level data structures. For example, consider this structure: <color>blue</color>. There is an
element node for the color tag, and under that there is a text
node that contains the data, blue! This issue will be explored at length
in the DOM lesson of this tutorial, but developers who are expecting objects
are usually surprised to find that invoking getNodeValue() on the element node returns nothing.
For a truly object-oriented tree, see the JDOM API at
[http://www.jdom.org](http://www.jdom.org
).

---

## DOM Packages

The Document Object Model implementation is defined in the packages listed in [Table 1-2](#gcezo).

Table 1-2 DOM Packages

| Package | Description |
| org.w3c.dom | Defines the DOM programming interfaces for XML (and, optionally, HTML) documents, as specified by the W3C. |
| javax.xml.parsers | Defines the DocumentBuilderFactory class and the DocumentBuilder class, which returns an object that implements the W3C Document interface. The factory that is used to create the builder is determined by the javax.xml.parsers system property, which can be set from the command line or overridden when invoking the new Instance method. This package also defines the ParserConfigurationException class for reporting errors. |

[« Previous](simple.html)
•
[Trail](../TOC.html)
•
[Next »](extensible.html)

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

**Previous page:** Simple API for XML APIs
  
**Next page:** Extensible Stylesheet Language Transformations APIs




A browser with JavaScript enabled is required for this page to operate properly.