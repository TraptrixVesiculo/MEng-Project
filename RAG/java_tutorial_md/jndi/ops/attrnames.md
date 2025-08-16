[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Java Naming and Directory Interface(TM).
  
**Lesson:** Naming and Directory Operations

[Naming and Directory Operations](index.html)

[Naming Exceptions](exception.html)

[Lookup an Object](lookup.html)

[List the Context](list.html)

[Add, Replace or Remove a Binding](bind.html)

[Rename](rename.html)

[Create and Destroy Subcontexts](create.html)

Attribute Names

[Read Attributes](getattrs.html)

[Modify Attributes](modattrs.html)

[Add, Replace Bindings with Attributes](bindattr.html)

[Search](search.html)

[Basic Search](basicsearch.html)

[Filters](filter.html)

[Scope](scope.html)

[Result Count](countlimit.html)

[Time Limit](timelimit.html)

[Trouble Shooting Tips](faq.html)

[Home Page](../../index.html)
>
[Java Naming and Directory Interface(TM).](../index.html)
>
[Naming and Directory Operations](index.html)

[« Previous](create.html) • [Trail](../TOC.html) • [Next »](getattrs.html)

# Attribute Names

An attribute consists of an *attribute identifier* and a
set of *attribute values*.
The *attribute identifier*, also called *attribute name*,
is a string that identifies an attribute.
An *attribute value* is the content of the attribute and its type
is not restricted to that of string.
You use an attribute name when you want to
specify a particular attribute for either retrieval,
searches, or modification. Names are also returned by operations
that return attributes (such as when you perform reads or searches
in the directory).

When using attribute names,
you need to be aware of certain directory server features
so that you won't be surprised by the result.
These features are described in the next subsections.

#### Attribute Type

In directories such as the LDAP, the attribute's name identifies the
attribute's type and is often called the *attribute type
name*. For example, the attribute name
"cn" is also called the
attribute type name. An attribute's type definition specifies the
syntax that the attribute's value is to have, whether it can have
multiple values, and equality and ordering rules to use when
performing comparison and ordering operations on the attribute's values.

#### Attribute Subclassing

Some directory implementations support *attribute subclassing*,
in which the server allows attribute types to be defined in
terms of other attribute types. For example,
a "name" attribute might be the superclass of all name-related
attributes: "commonName" might be a subclass of
"name".
For directory implementations that support this,
asking for the "name" attribute might return the
"commonName" attribute.

When accessing directories that support attribute subclassing,
you have to be aware that the server might return
attributes that have names different from those that
you requested.
To minimize the chance of this, use the most derived subclass.

#### Attribute Name Synonyms

Some directory implementations support synonyms for attribute
names. For example,
"cn" might be a synonym for "commonName".
Thus a request for the "cn" attribute might
return the "commonName" attribute.

When accessing directories that support synonyms for attribute names,
you must be aware that the server might return
attributes that have names different from those you requested.
To help prevent this from happening, use the canonical
attribute name instead of one of its synonyms.
The *canonical attribute name* is the name used in the attribute's definition;
a synonym is the name that refers to the canonical attribute name in its
definition.

#### Language Preferences

An extension to the LDAP v3
([RFC 2596](http://ietf.org/rfc/rfc2596.txt))
allows you to specify a language code along with an attribute name.
This resembles attribute subclassing in that
one attribute name can represent several different attributes.
An example is a "description" attribute that has two
language variations:
> ```
>
> description: software
> description;lang-en: software products
> description;lang-de: Softwareprodukte
>
> ```

A request for the "description" attribute would return all three attributes.

When accessing directories that support this feature,
you must be aware that the server might return
attributes that have names different from those
that you requested.

[« Previous](create.html)
•
[Trail](../TOC.html)
•
[Next »](getattrs.html)

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

**Previous page:** Create and Destroy Subcontexts
  
**Next page:** Read Attributes




A browser with JavaScript enabled is required for this page to operate properly.