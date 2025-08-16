[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Java API for XML Processing (JAXP)
  
**Lesson:** Extensible Stylesheet Language Transformations

[Extensible Stylesheet Language Transformations](index.html)

Introducing XSL, XSLT, and XPath

[How XPath Works](xpath.html)

[Writing Out a DOM as an XML File](writingDom.html)

[Generating XML from an Arbitrary Data Structure](generatingXML.html)

[Transforming XML Data with XSLT](transformingXML.html)

[Home Page](../../index.html)
>
[Java API for XML Processing (JAXP)](../index.html)
>
[Extensible Stylesheet Language Transformations](index.html)

[« Previous](index.html) • [Trail](../TOC.html) • [Next »](xpath.html)

# Introducing XSL, XSLT, and XPath

The Extensible Stylesheet Language (XSL) has three major subcomponents:

XSL-FO
:   The Formatting Objects standard. By far the largest subcomponent, this standard gives mechanisms for describing font sizes, page layouts, and other aspects of object rendering. This subcomponent is not covered by JAXP, nor is it included in this tutorial.

XSLT
:   This is the transformation language, which lets you define a transformation from XML into some other format. For example, you might use XSLT to produce HTML or a different XML structure. You could even use it to produce plain text or to put the information in some other document format. (And as you will see in
    [Generating XML from an Arbitrary Data Structure](generatingXML.html), a clever application can press it into service to manipulate non-XML data as well).

XPath
:   At bottom, XSLT is a language that lets you specify what sorts of things to do when a particular element is encountered. But to write a program for different parts of an XML data structure, you need to specify the part of the structure you are talking about at any given time. XPath is that specification language. It is an addressing mechanism that lets you specify a path to an element so that, for example, <article><title> can be distinguished from <person><title>. In that way, you can describe different kinds of translations for the different <title> elements.

The remainder of this section describes the packages that make up the JAXP
Transformation APIs.

## JAXP Transformation Packages

Here is a description of the packages that make up the JAXP
Transformation APIs:

javax.xml.transform
:   This package defines the factory class you use to get a Transformer object. You then configure the transformer with input (source) and output (result) objects, and invoke its transform() method to make the transformation happen. The source and result objects are created using classes from one of the other three packages.

javax.xml.transform.dom
:   Defines the DOMSource and DOMResult classes, which let you use a DOM as an input to or output from a transformation.

javax.xml.transform.sax
:   Defines the SAXSource and SAXResult classes, which let you use a SAX event generator as input to a transformation, or deliver SAX events as output to a SAX event processor.

javax.xml.transform.stream
:   Defines the StreamSource and StreamResult classes, which let you use an I/O stream as an input to or output from a transformation.

## XSLT Sample Programs

Unlike for the other lessons in this tutorial, the sample programs used in
this lesson are not included in the *install-dir*/jaxp-1\_4\_2-*release-date*/samples directory provided with the JAXP
1.4.2 Reference Implementation. However you can [download a ZIP file of the XSLT samples here](../examples/xslt_samples.zip).

[« Previous](index.html)
•
[Trail](../TOC.html)
•
[Next »](xpath.html)

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

**Previous page:** Extensible Stylesheet Language Transformations
  
**Next page:** How XPath Works




A browser with JavaScript enabled is required for this page to operate properly.