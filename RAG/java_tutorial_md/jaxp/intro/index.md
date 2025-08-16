[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

Introduction to JAXP

[Overview of the Packages](package.html)

[Simple API for XML APIs](simple.html)

[Document Object Model APIs](dom.html)

[Extensible Stylesheet Language Transformations APIs](extensible.html)

[Streaming API for XML APIs](streaming.html)

[Finding the JAXP Sample Programs](sample.html)

[Where Do You Go From Here?](next.html)

**Trail:** Java API for XML Processing (JAXP)

[Home Page](../../index.html)
>
[Java API for XML Processing (JAXP)](../index.html)

[« Previous](../index.html) • [Trail](../TOC.html) • [Next »](package.html)

# Lesson: Introduction to JAXP

The Java API for XML Processing (JAXP) is for processing XML data
using applications written in the Java programming language. JAXP leverages the parser standards Simple
API for XML Parsing (SAX) and Document Object Model (DOM) so that you
can choose to parse your data as a stream of events or
to build an object representation of it. JAXP also supports the Extensible Stylesheet Language
Transformations (XSLT) standard, giving you control over the presentation of the data and
enabling you to convert the data to other XML documents or to other
formats, such as HTML. JAXP also provides namespace support, allowing you to work
with DTDs that might otherwise have naming conflicts. Finally, as of version 1.4,
JAXP implements the Streaming API for XML (StAX) standard.

Designed to be flexible, JAXP allows you to use any XML-compliant parser from
within your application. It does this with what is called a pluggability layer,
which lets you plug in an implementation of the SAX or DOM
API. The pluggability layer also allows you to plug in an XSL processor,
letting you control how your XML data is displayed.

[« Previous](../index.html)
•
[Trail](../TOC.html)
•
[Next »](package.html)

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

**Previous page:** Table of Contents
  
**Next page:** Overview of the Packages




A browser with JavaScript enabled is required for this page to operate properly.