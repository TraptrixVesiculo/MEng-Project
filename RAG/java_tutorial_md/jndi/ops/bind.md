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

Add, Replace or Remove a Binding

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

[« Previous](list.html) • [Trail](../TOC.html) • [Next »](rename.html)

# Add, Replace or Remove a Binding

The Context interface contains methods for
[adding](#BIND),
[replacing](#REBIND), and
[removing](#UNBIND) a binding in a context.

#### Adding a Binding

[Context.bind()](http://download.oracle.com/javase/7/docs/api/javax/naming/Context.html#bind(javax.naming.Name, java.lang.Object)) is used to add a binding to a context.
It accepts as arguments the name of the object and the object
to be bound.
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
> // Create the object to be bound
> Fruit fruit = new Fruit("orange");
>
> // Perform the bind
> ctx.bind("cn=Favorite Fruit", fruit);
>
> ```

[This example](examples/Bind.java) creates an object of class
[Fruit](examples/Fruit.java)
and binds it to the name "cn=Favorite Fruit" in the context ctx.
If you subsequently looked up the name "cn=Favorite Fruit" in
ctx, then you would get the fruit object.
Note that to compile the Fruit class, you need the
[FruitFactory](examples/FruitFactory.java) class.

If you were to run this example twice, then the second attempt would fail with
a
[NameAlreadyBoundException](http://download.oracle.com/javase/7/docs/api/javax/naming/NameAlreadyBoundException.html). This is because the name "cn=Favorite Fruit" is already bound.
For the second attempt to succeed, you would have to use
[rebind()](http://download.oracle.com/javase/7/docs/api/javax/naming/Context.html#rebind(javax.naming.Name, java.lang.Object)).

#### Adding or Replacing a Binding

rebind() is used to add or replace a binding.
It accepts the same arguments as bind(), but the semantics
are such that if the name is already bound,
then it will be unbound and the newly given object will be bound.
> ```
>
> // Create the object to be bound
> Fruit fruit = new Fruit("lemon");
>
> // Perform the bind
> ctx.rebind("cn=Favorite Fruit", fruit);
>
> ```

When you run [this example](examples/Rebind.java), it will
replace the binding created by the [bind()](examples/Bind.java)
example.

![The binding to lemon is being replaced by a bind to orange.](../../figures/jndi/rebind.gif)

#### Removing a Binding

To remove a binding, you use
[unbind()](http://download.oracle.com/javase/7/docs/api/javax/naming/Context.html#unbind(javax.naming.Name)).
> ```
>
> // Remove the binding
> ctx.unbind("cn=Favorite Fruit");
>
> ```

[This example](examples/Unbind.java), when run, removes
the binding that was created by the
[bind()](examples/Bind.java) or
[rebind()](examples/Rebind.java)
example.

[« Previous](list.html)
•
[Trail](../TOC.html)
•
[Next »](rename.html)

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

**Previous page:** List the Context
  
**Next page:** Rename




A browser with JavaScript enabled is required for this page to operate properly.