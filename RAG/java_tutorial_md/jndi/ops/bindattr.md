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

Add, Replace Bindings with Attributes

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

[« Previous](modattrs.html) • [Trail](../TOC.html) • [Next »](search.html)

# Add, Replace Bindings with Attributes

The naming examples discussed how you can use
[bind(), rebind()](bind.html),
The
[DirContext](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/DirContext.html) interface contains overloaded versions
of these methods that accept attributes.
You can use these DirContext methods to associate
attributes with the object at the time that the binding or subcontext
is added to the namespace.
For example, you might create a Person object and bind it to
the namespace and at the same time associate attributes about that
Person object.

#### Adding a Binding That Has Attributes

[DirContext.bind()](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/DirContext.html#bind(javax.naming.Name, java.lang.Object, javax.naming.directory.Attributes)) is used to add a binding
that has attributes to a context.
It accepts as arguments the name of the object, the object
to be bound, and a set of attributes.
> ```
>
> // Create the object to be bound
> Fruit fruit = new Fruit("orange");
>
> // Create attributes to be associated with the object
> Attributes attrs = new BasicAttributes(true); // case-ignore
> Attribute objclass = new BasicAttribute("objectclass");
> objclass.add("top");
> objclass.add("organizationalUnit");
> attrs.put(objclass);
>
> // Perform bind
> ctx.bind("ou=favorite, ou=Fruits", fruit, attrs);
>
> ```

[This example](examples/Bind.java) creates an object of class
[Fruit](examples/Fruit.java)
and binds it to the name "ou=favorite" into the context named "ou=Fruits",
relative to ctx.
This binding has the "objectclass" attribute.
If you subsequently looked up the name
"ou=favorite, ou=Fruits" in
ctx, then you would get the fruit object.
If you then got the attributes of "ou=favorite, ou=Fruits",
you would get those attributes with which the object was created.
Following is this example's output.
> ```
>
> # java Bind
> orange
> attribute: objectclass
> value: top
> value: organizationalUnit
> value: javaObject
> value: javaNamingReference
> attribute: javaclassname
> value: Fruit
> attribute: javafactory
> value: FruitFactory
> attribute: javareferenceaddress
> value: #0#fruit#orange
> attribute: ou
> value: favorite
>
> ```

The extra attributes and attribute values shown are
used to store information about the object (fruit).
These extra attributes are discussed in more detail in the
trail.

If you were to run this example twice, then the second attempt would fail with a
[NameAlreadyBoundException](http://download.oracle.com/javase/7/docs/api/javax/naming/NameAlreadyBoundException.html). This is because the name "ou=favorite" is already bound in the "ou=Fruits" context.
For the second attempt to succeed, you would have to use
rebind().

#### Replacing a Binding That Has Attributes

[DirContext.rebind()](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/DirContext.html#rebind(javax.naming.Name, java.lang.Object, javax.naming.directory.Attributes)) is used to add or replace a binding
and its attributes.
It accepts the same arguments as bind().
However, rebind()'s semantics require that
if the name is already bound, then
it will be unbound and the newly given object and attributes
will be bound.
> ```
>
> // Create the object to be bound
> Fruit fruit = new Fruit("lemon");
>
> // Create attributes to be associated with the object
> Attributes attrs = new BasicAttributes(true); // case-ignore
> Attribute objclass = new BasicAttribute("objectclass");
> objclass.add("top");
> objclass.add("organizationalUnit");
> attrs.put(objclass);
>
> // Perform bind
> ctx.rebind("ou=favorite, ou=Fruits", fruit, attrs);
>
> ```

When you run [this example](examples/Rebind.java), it
replaces the binding that the [bind()](examples/Bind.java)
example created.
> ```
>
> # java Rebind
> lemon
> attribute: objectclass
> value: top
> value: organizationalUnit
> value: javaObject
> value: javaNamingReference
> attribute: javaclassname
> value: Fruit
> attribute: javafactory
> value: FruitFactory
> attribute: javareferenceaddress
> value: #0#fruit#lemon
> attribute: ou
> value: favorite
>
> ```

[« Previous](modattrs.html)
•
[Trail](../TOC.html)
•
[Next »](search.html)

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

**Previous page:** Modify Attributes
  
**Next page:** Search




A browser with JavaScript enabled is required for this page to operate properly.