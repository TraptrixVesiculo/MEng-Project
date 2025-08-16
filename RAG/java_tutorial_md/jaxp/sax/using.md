[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Java API for XML Processing (JAXP)
  
**Lesson:** Simple API for XML

[Simple API for XML](index.html)

[When to Use SAX](when.html)

[Parsing an XML File Using SAX](parsing.html)

[Implementing SAX Validation](validation.html)

[Handling Lexical Events](events.html)

Using the DTDHandler and EntityResolver

[Further Information](info.html)

[Home Page](../../index.html)
>
[Java API for XML Processing (JAXP)](../index.html)
>
[Simple API for XML](index.html)

[« Previous](events.html) • [Trail](../TOC.html) • [Next »](info.html)

# Using the DTDHandler and EntityResolver

This section presents the two remaining SAX event handlers: DTDHandler and EntityResolver.
The DTDHandler is invoked when the DTD encounters an unparsed entity or
a notation declaration. The EntityResolver comes into play when a URN (public ID) must
be resolved to a URL (system ID).

## The DTDHandler API

[Choosing the Parser Implementation](validation.html
) showed a method for referencing a file that contains binary data, such
as an image file, using MIME data types. That is the simplest, most
extensible mechanism. For compatibility with older SGML-style data, though, it is also possible
to define an unparsed entity.

The NDATA keyword defines an unparsed entity:

```
<!ENTITY myEntity SYSTEM "..URL.." NDATA gif>
```

The NDATA keyword says that the data in this entity is not parseable
XML data but instead is data that uses some other notation. In this
case, the notation is named gif. The DTD must then include a declaration
for that notation, which would look something like the following.

```
<!NOTATION gif SYSTEM "..URL..">
```

When the parser sees an unparsed entity or a notation declaration, it does
nothing with the information except to pass it along to the application using
the DTDHandler interface. That interface defines two methods.

* notationDecl(String name, String publicId, String systemId)
* unparsedEntityDecl(String name, String publicId, String systemId, String notationName

The notationDecl method is passed the name of the notation and either the
public or the system identifier, or both, depending on which is declared in
the DTD. The unparsedEntityDecl method is passed the name of the entity, the
appropriate identifiers, and the name of the notation it uses.

---

**Note -** The DTDHandler interface is implemented by the DefaultHandler class.

---

Notations can also be used in attribute declarations. For example, the following declaration
requires notations for the GIF and PNG image-file formats.

```
<!ENTITY image EMPTY>
<!ATTLIST image 

...

type  NOTATION  (gif | png) "gif"
>
```

Here, the type is declared as being either gif or png. The
default, if neither is specified, is gif.

Whether the notation reference is used to describe an unparsed entity or an
attribute, it is up to the application to do the appropriate processing. The
parser knows nothing at all about the semantics of the notations. It
only passes on the declarations.

## The EntityResolver API

The EntityResolver API lets you convert a public ID (URN) into a system
ID (URL). Your application may need to do that, for example, to convert
something like href="urn:/someName" into "http://someURL".

The EntityResolver interface defines a single method:

```
resolveEntity(String publicId, String systemId)
```

This method returns an InputSource object, which can be used to access the
entity's contents. Converting a URL into an InputSource is easy enough. But
the URL that is passed as the system ID will be the location
of the original document which is, as likely as not, somewhere out on
the web. To access a local copy, if there is one, you must
maintain a catalog somewhere on the system that maps names (public IDs) into
local URLs.

[« Previous](events.html)
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

**Previous page:** Handling Lexical Events
  
**Next page:** Further Information




A browser with JavaScript enabled is required for this page to operate properly.