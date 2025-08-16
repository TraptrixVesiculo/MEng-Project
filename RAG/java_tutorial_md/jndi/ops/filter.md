[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Java Naming and Directory Interface(TM).
  
**Lesson:** Naming and Directory Operations
  
**Section:** Search

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

[Search](search.html)

[Basic Search](basicsearch.html)

Filters

[Scope](scope.html)

[Result Count](countlimit.html)

[Time Limit](timelimit.html)

[Trouble Shooting Tips](faq.html)

[Home Page](../../index.html)
>
[Java Naming and Directory Interface(TM).](../index.html)
>
[Naming and Directory Operations](index.html)

[« Previous](basicsearch.html) • [Trail](../TOC.html) • [Next »](scope.html)

# Filters

In addition to specifying a search using a set of attributes, you can
specify a search in the form of a *search filter*.
A search filter is a search query expressed in the form
of a logical expression.
The syntax of search filters accepted by
[DirContext.search()](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/DirContext.html#search(javax.naming.Name, java.lang.String, javax.naming.directory.SearchControls)) is described in
[RFC 2254](http://ietf.org/rfc/rfc2254.txt).

The following search filter specifies that the qualifying entries must have
an "sn" attribute with a value of "Geisel"
and a "mail" attribute with any value:
> ```
>
> (&(sn=Geisel)(mail=*))
>
> ```

The following code creates a filter and default
[SearchControls](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/SearchControls.html), and uses them to perform a search.
The search is equivalent to the one presented in the
[basic search](basicsearch.html) example.
> ```
>
> // Create the default search controls
> SearchControls ctls = new SearchControls();
>
> // Specify the search filter to match
> // Ask for objects that have the attribute "sn" == "Geisel"
> // and the "mail" attribute
> String filter = "(&(sn=Geisel)(mail=*))";
>
> // Search for objects using the filter
> NamingEnumeration answer = ctx.search("ou=People", filter, ctls);
>
> ```

Running [this example](examples/SearchWithFilterRetAll.java)
produces the following result.
> ```
>
> # java SearchWithFilterRetAll
> >>>cn=Ted Geisel
> attribute: sn
> value: Geisel
> attribute: objectclass
> value: top
> value: person
> value: organizationalPerson
> value: inetOrgPerson
> attribute: jpegphoto
> value: [B@1dacd75e
> attribute: mail
> value: Ted.Geisel@JNDITutorial.com
> attribute: facsimiletelephonenumber
> value: +1 408 555 2329
> attribute: cn
> value: Ted Geisel
> attribute: telephonenumber
> value: +1 408 555 5252
>
> ```

#### Quick Overview of Search Filter Syntax

The search filter syntax is basically a logical expression
in prefix notation (that is, the logical operator appears before its
arguments).
The following table lists the symbols used for creating filters.

| Symbol | Description |
| --- | --- |
| & | conjunction (i.e., *and* -- all in list must be true) |
| | | disjunction (i.e., *or* -- one or more alternatives must be true) |
| ! | negation (i.e., *not* -- the item being negated must not be true) |
| = | equality (according to the matching rule of the attribute) |
| ~= | approximate equality (according to the matching rule of the attribute) |
| >= | greater than (according to the matching rule of the attribute) |
| <= | less than (according to the matching rule of the attribute) |
| =\* | presence (i.e., the entry must have the attribute but its value is irrelevant) |
| \* | wildcard (indicates zero or more characters can occur in that position); used when specifying attribute values to match |
| \ | escape (for escaping '\*', '(', or ')' when they occur inside an attribute value) |

Each item in the filter is composed
using an attribute identifier and either
an attribute value or symbols
denoting the attribute value.
For example, the item "sn=Geisel" means that the
"sn" attribute
must have the attribute value "Geisel"
and the item "mail=\*"
indicates that the "mail" attribute must be present.

Each item must be enclosed within a set of parentheses, as in
"(sn=Geisel)".
These items are composed using logical operators
such as "&" (conjunction) to create logical expressions,
as in "(& (sn=Geisel) (mail=\*))".

Each logical expression can be further composed of other
items that themselves are logical expressions,
as in "(| (& (sn=Geisel) (mail=\*)) (sn=L\*))".
This last example is requesting either entries that have both
a "sn" attribute of "Geisel" and the
"mail" attribute or entries
whose "sn" attribute begins with the letter "L."

For a complete description of the syntax, see
[RFC 2254](http://ietf.org/rfc/rfc2254.txt).

#### Returning Selected Attributes

The previous example returned all attributes associated with
the entries that satisfy the specified filter. You can select
the attributes to return by setting the search controls argument.
You create an array of attribute identifiers that you want to include in
the result and pass it to
[SearchControls.setReturningAttributes()](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/SearchControls.html#setReturningAttributes(java.lang.String[])).
Here's an example.
> ```
>
> // Specify the ids of the attributes to return
> String[] attrIDs = {"sn", "telephonenumber", "golfhandicap", "mail"};
> SearchControls ctls = new SearchControls();
> ctls.setReturningAttributes(attrIDs);
>
> ```

This example is equivalent to the
[Returning Selected Attributes](basicsearch.html#SELECT)
example in the Basic Search section. Running
[it](examples/SearchWithFilter.java) produces the following
results.
(The entry does not have a "golfhandicap" attribute, so
it is not returned.)
> ```
>
> # java SearchWithFilter
> >>>cn=Ted Geisel
> attribute: sn
> value: Geisel
> attribute: mail
> value: Ted.Geisel@JNDITutorial.com
> attribute: telephonenumber
> value: +1 408 555 5252
>
> ```

[« Previous](basicsearch.html)
•
[Trail](../TOC.html)
•
[Next »](scope.html)

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

**Previous page:** Basic Search
  
**Next page:** Scope




A browser with JavaScript enabled is required for this page to operate properly.