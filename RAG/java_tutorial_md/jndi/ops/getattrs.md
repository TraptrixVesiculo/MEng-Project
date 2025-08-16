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

Read Attributes

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

[« Previous](attrnames.html) • [Trail](../TOC.html) • [Next »](modattrs.html)

# Read Attributes

To read the attributes of an object from the directory, use
[DirContext.getAttributes()](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/DirContext.html#getAttributes(javax.naming.Name)) and pass it the name of
the object for which you want the attributes.
Suppose that an object in the naming service has
the name "cn=Ted Geisel, ou=People".
To retrieve this object's attributes, you'll need
[code](examples/GetAllAttrs.java) that looks like this:
> ```
>
> Attributes answer = ctx.getAttributes("cn=Ted Geisel, ou=People");
>
> ```

You can then print the contents of this answer as follows.
> ```
>
> for (NamingEnumeration ae = answer.getAll(); ae.hasMore();) {
>     Attribute attr = (Attribute)ae.next();
>     System.out.println("attribute: " + attr.getID());
>     /* Print each value */
>     for (NamingEnumeration e = attr.getAll(); e.hasMore();
> 	 System.out.println("value: " + e.next()))
> 	;
> }
>
> ```

This produces the following output.
> ```
>
> # java GetattrsAll
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
> attribute: telephonenumber
> value: +1 408 555 5252
> attribute: cn
> value: Ted Geisel
>
> ```

#### Returning Selected Attributes

To read a selective subset of attributes, you supply an array
of strings that are attribute identifiers of the attributes
that you
want to retrieve.
> ```
>
> // Specify the ids of the attributes to return
> String[] attrIDs = {"sn", "telephonenumber", "golfhandicap", "mail"};
>
> // Get the attributes requested
> Attributes answer = ctx.getAttributes("cn=Ted Geisel, ou=People", attrIDs);
>
> ```

[This example](examples/GetAttrs.java)
asks for the "sn", "telephonenumber",
"golfhandicap" and "mail" attributes of the object
"cn=Ted Geisel, ou=People".
This object has all but the "golfhandicap" attribute,
and so three attributes are returned in the answer.
Following is the output of the example.
> ```
>
> # java Getattrs
> attribute: sn
> value: Geisel
> attribute: mail
> value: Ted.Geisel@JNDITutorial.com
> attribute: telephonenumber
> value: +1 408 555 5252
>
> ```

[« Previous](attrnames.html)
•
[Trail](../TOC.html)
•
[Next »](modattrs.html)

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

**Previous page:** Attribute Names
  
**Next page:** Modify Attributes




A browser with JavaScript enabled is required for this page to operate properly.