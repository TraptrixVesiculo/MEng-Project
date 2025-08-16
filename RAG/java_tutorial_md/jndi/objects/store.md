[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Java Naming and Directory Interface(TM).
  
**Lesson:** Java Objects in the Directory

[Java Objects in the Directory](index.html)

Storing and Reading Objects

[Serializable Objects](serial.html)

[Home Page](../../index.html)
>
[Java Naming and Directory Interface(TM).](../index.html)
>
[Java Objects in the Directory](index.html)

[« Previous](index.html) • [Trail](../TOC.html) • [Next »](serial.html)

# Storing and Reading Objects

Applications and services can use
the directory in different ways to store and locate objects:

* Store (a copy of) the object itself.
* Store a reference to an object.
* Store attributes that describe the object.

In general terms,
a JavaTM
object's serialized form contains the object's state
and an object's reference in a compact representation of
addressing information that can be used to contact the object.
Some examples are given in the
[Naming and Directory Operations](../../jndi/ops/lookup.html)  lesson.
An object's attributes are properties that are used to describe the
object; attributes
might include addressing and/or state information.

Which of these three ways to use depends on the application/system
that is being built and how it needs to interoperate with other
applications and systems that will share the objects stored in
the directory.
Another factor is the support provided by the service provider
and the underlying directory service.

Programmatically, all applications use one of the following methods
when storing objects in the directory:

* [Context.bind()](http://download.oracle.com/javase/7/docs/api/javax/naming/Context.html#bind(javax.naming.Name, java.lang.Object))* [DirContext.bind()](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/DirContext.html#bind(javax.naming.Name, java.lang.Object, javax.naming.directory.Attributes))* [Context.rebind()](http://download.oracle.com/javase/7/docs/api/javax/naming/Context.html#rebind(javax.naming.Name, java.lang.Object))* [DirContext.rebind()](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/DirContext.html#rebind(javax.naming.Name, java.lang.Object, javax.naming.directory.Attributes))

The application passes the object that it wants to store to one
of these methods.
Then, depending on the types of objects that the
service provider supports, the object will be transformed into a representation
acceptable to the underlying directory service.

This lesson shows how to store serializable objects in the directory
once the object is stored, you can simply use
[lookup()](http://download.oracle.com/javase/7/docs/api/javax/naming/Context.html#lookup(javax.naming.Name))to get a copy of the object back from the directory,
regardless of what type of information was actually stored.

You can get the object back not only by using lookup(),
but also when you
[list](http://download.oracle.com/javase/7/docs/api/javax/naming/Context.html#list(javax.naming.Name)) a context and
when you
[search](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/DirContext.html#search(javax.naming.Name)) a context or its subtree.
In all of these cases, *object factories*
might be involved. Object factories are discussed in detail in the
[JNDI Tutorial](http://java.sun.com/products/jndi/tutorial/objects/factory/index.html) 

For storing below objects types, please refer to the JNDI Tutorial

* [Referenceable objects and JNDI
  References](http://java.sun.com/products/jndi/tutorial/objects/storing/reference.html)  
  The bind() examples in the
  [Naming and Directory Operations](../../jndi/ops/bind.html)  lesson use Referenceable objects.* [Objects with attributes (DirContext)](http://java.sun.com/products/jndi/tutorial/objects/storing/dircontext.html)* [RMI (Java Remote Method Invocation) objects
      (including those that use IIOP)](http://java.sun.com/products/jndi/tutorial/objects/storing/remote.html)* [CORBA objects](http://java.sun.com/products/jndi/tutorial/objects/storing/corba.html)

> ---
>
> **Before you go on:**
> To run these examples successfully,
> you must either turn off schema-checking in the
> server or add [the Java schema](../../jndi/software/config/java.schema)
> that accompany this tutorial to the server.
> This task is typically performed by the directory
> server's administrator. See the
> [Software Setup](../../jndi/software/content.html#SCHEMA)  lesson for more information.
>
> **Windows Active Directory:**
> [Context.rebind()](http://download.oracle.com/javase/7/docs/api/javax/naming/Context.html#rebind(javax.naming.Name, java.lang.Object)) and
> [DirContext.rebind()](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/DirContext.html#rebind(javax.naming.Name, java.lang.Object, javax.naming.directory.Attributes)) do not work against Active Directory because these methods work by
> reading the attributes of the entry to be updated, removing the entry,
> and then adding a new entry that contains the modified attributes.
> Active Directory returns some attributes that cannot be set by the user,
> causing the final addition step to fail.
> The workaround for this problem is to use
> [DirContext.getAttributes()](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/DirContext.html#getAttributes(javax.naming.Name)) to obtain and save the attributes that you want to keep.
> Then, remove the entry and add it back with the saved attributes (and
> any others that you want to add) using
> [DirContext.bind()](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/DirContext.html#bind(javax.naming.Name, java.lang.Object, javax.naming.directory.Attributes)).

[« Previous](index.html)
•
[Trail](../TOC.html)
•
[Next »](serial.html)

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

**Previous page:** Java Objects in the Directory
  
**Next page:** Serializable Objects




A browser with JavaScript enabled is required for this page to operate properly.