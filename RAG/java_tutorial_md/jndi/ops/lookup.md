[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Java Naming and Directory Interface(TM).
  
**Lesson:** Naming and Directory Operations

[Naming and Directory Operations](index.html)

[Naming Exceptions](exception.html)

Lookup an Object

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

[« Previous](exception.html) • [Trail](../TOC.html) • [Next »](list.html)

# Lookup an Object

To look up an object from the naming service, use
[Context.lookup()](http://download.oracle.com/javase/7/docs/api/javax/naming/Context.html#lookup(javax.naming.Name)) and pass it the name of the object that you want to retrieve.
Suppose that there is an object in the naming service with
the name cn=Rosanna Lee,ou=People.
To retrieve the object, you would write

```

Object obj = ctx.lookup("cn=Rosanna Lee,ou=People");

```

The type of object that is returned by lookup()
depends both on the underlying naming system and on
the data associated with the object itself.
A naming system can contain many different types of objects,
and a lookup of an object in different parts of the system might
yield objects of different types.
In this example, "cn=Rosanna Lee,ou=People" happens to be
bound to a context object (javax.naming.ldap.LdapContext).
You can cast the result of lookup() to its target class.

For example, the following code looks up the object
"cn=Rosanna Lee,ou=People"
and casts it to LdapContext.

```

import javax.naming.ldap.LdapContext;
...
LdapContext ctx = (LdapContext) ctx.lookup("cn=Rosanna Lee,ou=People");

```

The complete example is in the file
[Lookup.java](examples/Lookup.java).

![Diagram of Lookup example](../../figures/jndi/lookup.gif)

There are two new static methods available in Java SE 6 to lookup a name:

* [InitialContext.doLookup(Name name)](http://download.oracle.com/javase/7/docs/api/javax/naming/InitialContext.html#doLookup(javax.naming.Name))
* [InitialContext.doLookup(String name)](http://download.oracle.com/javase/7/docs/api/javax/naming/InitialContext.html#doLookup(java.lang.String))

These methods provide a shortcut way of looking up a name without instantiating
an InitialContext.

[« Previous](exception.html)
•
[Trail](../TOC.html)
•
[Next »](list.html)

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

**Previous page:** Naming Exceptions
  
**Next page:** List the Context




A browser with JavaScript enabled is required for this page to operate properly.