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

Create and Destroy Subcontexts

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

[« Previous](rename.html) • [Trail](../TOC.html) • [Next »](attrnames.html)

# Create and Destroy Subcontexts

The Context interface contains methods for
[creating](#CREATE) and [destroying](#DESTROY)
a *subcontext*, a context that is bound in another
context of the same type.

This examples here use an object that has *attributes*
and create a subcontext in the directory.
You can use these DirContext methods to associate
attributes with the object at the time that the binding or subcontext
is added to the namespace.
For example, you might create a Person object and bind it to
the namespace and at the same time associate attributes about that
Person object.
The naming equivalent will have no attributes.

The createSubcontext() differs from bind() in that it creates a new
Object i.e a new Context to be bound to the directory while as bind()
binds the given Object in the directory.

#### Creating a Context

To create a naming context, you supply to
[createSubcontext()](http://download.oracle.com/javase/7/docs/api/javax/naming/Context.html#createSubcontext(javax.naming.Name)) the name of the context that you want to create.
To create a context that has attributes, you supply to
[DirContext.createSubcontext()](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/DirContext.html#createSubcontext(javax.naming.Name, javax.naming.directory.Attributes)) the name of the context that you want to create and its attributes.
> ---
>
> **Before you go on:**
> The examples in this lesson require that you make additions to the schema.
> You must either turn off schema-checking in the LDAP
> server or add [the schema](../../jndi/software/config/java.schema) that accompanies this tutorial to the server.
> Both of these tasks are typically performed by the directory
> server's administrator. See the
> lesson.
>
> ---

> ```
>
> // Create attributes to be associated with the new context
> Attributes attrs = new BasicAttributes(true); // case-ignore
> Attribute objclass = new BasicAttribute("objectclass");
> objclass.add("top");
> objclass.add("organizationalUnit");
> attrs.put(objclass);
>
> // Create the context
> Context result = ctx.createSubcontext("NewOu", attrs);
>
> ```

[This example](examples/Create.java) creates a new context called "ou=NewOu"
that has an attribute "objectclass" with two values,
"top" and "organizationalUnit",
in the context ctx.
> ```
>
> # java Create
> ou=Groups: javax.naming.directory.DirContext
> ou=People: javax.naming.directory.DirContext
> ou=NewOu: javax.naming.directory.DirContext
>
> ```

[This example](examples/Create.java) creates a new context, called "NewOu",
that is a child of ctx.

![Diagram shows new subcontext.](../../figures/jndi/create.gif)

#### Destroying a Context

To destroy a context, you supply to
[destroySubcontext()](http://download.oracle.com/javase/7/docs/api/javax/naming/Context.html#destroySubcontext(javax.naming.Name)) the name of the context to destroy.
> ```
>
> // Destroy the context
> ctx.destroySubcontext("NewOu");
>
> ```

[This example](examples/Destroy.java) destroys the context
"NewOu"
in the context ctx.

[« Previous](rename.html)
•
[Trail](../TOC.html)
•
[Next »](attrnames.html)

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

**Previous page:** Rename
  
**Next page:** Attribute Names




A browser with JavaScript enabled is required for this page to operate properly.