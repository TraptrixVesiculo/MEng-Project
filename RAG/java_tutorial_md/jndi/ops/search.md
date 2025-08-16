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

[Attribute Names](attrnames.html)

[Read Attributes](getattrs.html)

[Modify Attributes](modattrs.html)

[Add, Replace Bindings with Attributes](bindattr.html)

Search

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

[« Previous](bindattr.html) • [Trail](../TOC.html) • [Next »](basicsearch.html)

# Search

One of the most useful features that a directory offers is its
*yellow pages*, or *search*, service.
You can compose a query consisting of attributes
of entries that you are seeking and submit that query
to the directory.
The directory then returns a list of entries that
satisfy the query.
For example, you could ask the directory for all entries with a bowling
average greater than 200 or all entries that represent a person
with a surname beginning with "Sch."

The
[DirContext](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/DirContext.html) interface provides several methods
for searching the directory, with progressive degrees of complexity and power.
The various aspects of searching the directory are covered
in the following sections:

* [Basic Search](basicsearch.html)* [Search Filters](filter.html)* [Search Controls](scope.html)

[« Previous](bindattr.html)
•
[Trail](../TOC.html)
•
[Next »](basicsearch.html)

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

**Previous page:** Add, Replace Bindings with Attributes
  
**Next page:** Basic Search




A browser with JavaScript enabled is required for this page to operate properly.