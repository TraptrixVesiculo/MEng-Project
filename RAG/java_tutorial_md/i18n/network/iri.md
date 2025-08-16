[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Internationalization
  
**Lesson:** Internationalization of Network Resources

[Internationalization of Network Resources](index.html)

[Internationalized Domain Name](idn.html)

Internationalized Resource Identifier

[Home Page](../../index.html)
>
[Internationalization](../index.html)
>
[Internationalization of Network Resources](index.html)

[« Previous](idn.html) • [Trail](../TOC.html) • [Next »](../end.html)

# Internationalized Resource Identifier

**Internationalized Resource Identifier** (IRI) like IDN may contain
Unicode characters, while Uniform Resource Identifier (URI) is limited to ASCII symbols
only.

According to
[RFC 3987](http://www.ietf.org/rfc/rfc3987.txt) IRIs are meant to replace URIs in identifying resources for
protocols, formats, and software components that use a UCS-based
character repertoire.

At first sight, you may consider that this task must been decided with the same
means as for IDN. But there is not so exactly.
Let's view a resource identifier structure:

![This figure represents a resource identifier structure](../../figures/i18n/URI_structure.gif)

You may notice that it has several components.

The authority component of a URI parses according to the following syntax

```

    [user-info@]host[:port] 

```

where the characters @ and : stand for themselves. The host component can be an
IP-literal, an IPv4address, or just a name.

In a case, where a host is a domain name the IDN approach, i.e. the mapping,
could be applied.

But generally the URI structure is more complicated. Applications can use URI-reference
syntax to make reference to a URI, instead of always using above generic syntax rule.
A URI-reference is either a URI or a relative reference.
If a URI-reference doesn't specifies a scheme, it is said to be a *relative reference*. Usually, a relative reference expresses a URI reference relative to the
name space of another URI.

Nevertheless, the instances the `java.net.URI` class can represent IRIs
whenever they contain non ASCII characters.

This class was enhanced by the following methods to perform the operations and
conversions according to RFC 3987:

* `toASCIIString()` - converts an IRI to a URI and returns its content
  as a US-ASCII string.
* `toString()` - returns the content of this URI as a string in its
  original Unicode form.
* `toIRIString()`Converts this URI to an IRI and returns its content
  as a string.

[« Previous](idn.html)
•
[Trail](../TOC.html)
•
[Next »](../end.html)

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

**Previous page:** Internationalized Domain Name
  
**Next page:** End of Trail




A browser with JavaScript enabled is required for this page to operate properly.