[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Java API for XML Processing (JAXP)
  
**Lesson:** Simple API for XML

[Simple API for XML](index.html)

When to Use SAX

[Parsing an XML File Using SAX](parsing.html)

[Implementing SAX Validation](validation.html)

[Handling Lexical Events](events.html)

[Using the DTDHandler and EntityResolver](using.html)

[Further Information](info.html)

[Home Page](../../index.html)
>
[Java API for XML Processing (JAXP)](../index.html)
>
[Simple API for XML](index.html)

[« Previous](index.html) • [Trail](../TOC.html) • [Next »](parsing.html)

# When to Use SAX

It is helpful to understand the SAX event model when you want
to convert existing data to XML. The key to the conversion process is
to modify an existing application to deliver SAX events as it reads the
data.

SAX is fast and efficient, but its event model makes it most
useful for such state-independent filtering. For example, a SAX parser calls one method in
your application when an element tag is encountered and calls a different method
when text is found. If the processing you are doing is state-independent (meaning
that it does not depend on the elements that have come before),
then SAX works fine.

On the other hand, for state-dependent processing, where the program needs to do
one thing with the data under element A but something different with the
data under element B, then a pull parser such as the Streaming
API for XML (StAX) would be a better choice. With a pull parser,
you get the next node, whatever it happens to be, at any point
in the code that you ask for it. So it is easy to
vary the way you process text (for example), because you can process it
multiple places in the program (for more detail, see
[Further Information](info.html
)).

SAX requires much less memory than DOM, because SAX does not construct an
internal representation (tree structure) of the XML data, as a DOM does. Instead,
SAX simply sends data to the application as it is read; your
application can then do whatever it wants to do with the data it
sees.

Pull parsers and the SAX API both act like a serial I/O
stream. You see the data as it streams in, but you cannot go
back to an earlier position or leap ahead to a different position. In
general, such parsers work well when you simply want to read data and
have the application act on it.

But when you need to modify an XML structure - especially when
you need to modify it interactively - an in-memory structure makes more sense.
DOM is one such model. However, although DOM provides many powerful capabilities for large-scale
documents (like books and articles), it also requires a lot of complex coding.
The details of that process are highlighted in
[When to Use DOM](../dom
/when.html
) in the next
lesson.

For simpler applications, that complexity may well be unnecessary. For faster development and
simpler applications, one of the object-oriented XML-programming standards, such as JDOM (
[http://www.jdom.org](http://www.jdom.org
)) and DOM4J
(
[http://dom4j.org/](http://dom4j.org/
)), might make more sense.

[« Previous](index.html)
•
[Trail](../TOC.html)
•
[Next »](parsing.html)

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

**Previous page:** Simple API for XML
  
**Next page:** Parsing an XML File Using SAX




A browser with JavaScript enabled is required for this page to operate properly.