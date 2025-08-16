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

Basic Search

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

[« Previous](search.html) • [Trail](../TOC.html) • [Next »](filter.html)

# Basic Search

The simplest form of search requires that you specify the set of attributes
that an entry must have and the name of the target context in which to perform the search.

The following code
creates an attribute set matchAttrs,
which has two attributes "sn" and
"mail".
It specifies that the qualifying entries must have
a surname ("sn") attribute with a value of
"Geisel"
and a "mail" attribute with any value.
It then invokes
[DirContext.search()](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/DirContext.html#search(javax.naming.Name, javax.naming.directory.Attributes)) to search the
context "ou=People" for entries that have the attributes
specified by matchAttrs.
> ```
>
> // Specify the attributes to match
> // Ask for objects that has a surname ("sn") attribute with 
> // the value "Geisel" and the "mail" attribute
> Attributes matchAttrs = new BasicAttributes(true); // ignore attribute name case
> matchAttrs.put(new BasicAttribute("sn", "Geisel"));
> matchAttrs.put(new BasicAttribute("mail"));
>
> // Search for objects that have those matching attributes
> NamingEnumeration answer = ctx.search("ou=People", matchAttrs);
>
> ```

You can then print the results as follows.
> ```
>
> while (answer.hasMore()) {
>     SearchResult sr = (SearchResult)answer.next();
>     System.out.println(">>>" + sr.getName());
>     printAttrs(sr.getAttributes());
> }
>
> ```

printAttrs()is similar to the code
in [the getAttributes()](getattrs.html) example
that prints an attribute set.

Running [this example](examples/SearchRetAll.java) produces
the following result.
> ```
>
> # java SearchRetAll
> >>>cn=Ted Geisel
> attribute: sn
> value: Geisel
> attribute: objectclass
> value: top
> value: person
> value: organizationalPerson
> value: inetOrgPerson
> attribute: jpegphoto
> value: [B@1dacd78b
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

#### Returning Selected Attributes

The previous example returned all attributes associated with
the entries that satisfy the specified query. You can select
the attributes to return by passing search()
an array of attribute identifiers that you want to include in
the result. After creating the matchAttrs as shown previously,
you also need to create the array of attribute identifiers,
as shown next.
> ```
>
> // Specify the ids of the attributes to return
> String[] attrIDs = {"sn", "telephonenumber", "golfhandicap", "mail"};
>
> // Search for objects that have those matching attributes
> NamingEnumeration answer = ctx.search("ou=People", matchAttrs, attrIDs);
>
> ```

[This example](examples/Search.java) returns the attributes
"sn", "telephonenumber",
"golfhandicap", and "mail" of entries that
have an attribute "mail" and have a "sn" attribute with the
value "Geisel".
This example produces the following result.
(The entry does not have a
"golfhandicap" attribute,
so it is not returned.)
> ```
>
> # java Search 
> >>>cn=Ted Geisel
> attribute: sn
> value: Geisel
> attribute: mail
> value: Ted.Geisel@JNDITutorial.com
> attribute: telephonenumber
> value: +1 408 555 5252
>
> ```

[« Previous](search.html)
•
[Trail](../TOC.html)
•
[Next »](filter.html)

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

**Previous page:** Search
  
**Next page:** Filters




A browser with JavaScript enabled is required for this page to operate properly.