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

Rename

[Create and Destroy Subcontexts](create.html)

[Attribute Names](attrnames.html)

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

[« Previous](bind.html) • [Trail](../TOC.html) • [Next »](create.html)

# Rename

You can rename an object in a context by using
[Context.rename()](http://download.oracle.com/javase/7/docs/api/javax/naming/Context.html#rename(javax.naming.Name, javax.naming.Name)).

```

// Rename to Scott S
ctx.rename("cn=Scott Seligman", "cn=Scott S");

```

![Renaming an object](../../figures/jndi/rename-leaf.gif)

[This example](examples/Rename.java) renames
the object that was bound to "cn=Scott Seligman" to
"cn=Scott S".
After verifying that the object got renamed, the program
renames it to its original name ("cn=Scott Seligman"),
as follows.

```

// Rename back to Scott Seligman
ctx.rename("cn=Scott S", "cn=Scott Seligman");

```

For more examples on renaming of LDAP entries check out the
 [Advanced Topics for LDAP users](../../jndi/ldap/rename.html) 
lesson.

[« Previous](bind.html)
•
[Trail](../TOC.html)
•
[Next »](create.html)

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

**Previous page:** Add, Replace or Remove a Binding
  
**Next page:** Create and Destroy Subcontexts




A browser with JavaScript enabled is required for this page to operate properly.