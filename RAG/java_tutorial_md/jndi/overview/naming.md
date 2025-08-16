[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Java Naming and Directory Interface(TM).
  
**Lesson:** Overview of JNDI

[Overview of JNDI](index.html)

Naming Package

[Directory and LDAP Packages](dir.html)

[Event and Service Provider Packages](event.html)

[Home Page](../../index.html)
>
[Java Naming and Directory Interface(TM).](../index.html)
>
[Overview of JNDI](index.html)

[« Previous](index.html) • [Trail](../TOC.html) • [Next »](dir.html)

# Naming Package

The
[javax.naming](http://download.oracle.com/javase/7/docs/api/javax/naming/package-summary.html) package contains classes and interfaces for accessing naming
services.

## Context

The javax.naming package defines a
[Context](http://download.oracle.com/javase/7/docs/api/javax/naming/Context.html) interface, which is the core interface for looking up, binding/unbinding,
renaming objects and creating and destroying subcontexts.

Lookup
:   The most commonly used operation is
    [lookup()](http://download.oracle.com/javase/7/docs/api/javax/naming/Context.html#lookup(javax.naming.Name)).
    You supply lookup()
    the name of the object you want
    to look up, and it returns the object bound to that name.

Bindings
:   [listBindings()](http://download.oracle.com/javase/7/docs/api/javax/naming/Context.html#listBindings(javax.naming.Name)) returns an enumeration of name-to-object bindings.
    A binding is a tuple containing the name of the bound object,
    the name of the object's class, and the object itself.

    List
    :   [list()](http://download.oracle.com/javase/7/docs/api/javax/naming/Context.html#list(javax.naming.Name))is similar to listBindings(),
        except that it returns an enumeration of names containing an
        object's name and the name of the object's class.
        list() is useful for applications such
        as browsers that want to discover information about the objects
        bound within a context but that don't need all of the actual objects.
        Although listBindings() provides all of the same information,
        it is potentially a much more expensive operation.

    Name
    :   Name is an interface that represents a generic
        name--an ordered sequence of zero or more components.
        The Naming Systems use this interface to define the names that follow
        its conventions as described in the  [Naming and Directory Concepts](../concepts/index.html) lesson.

    References
    :   Objects are stored in naming and directory services in different ways.
        A reference might be a very compact representation
        of an object.

        The JNDI defines the
        [Reference](http://download.oracle.com/javase/7/docs/api/javax/naming/Reference.html) class
        to represent reference.
        A reference contains information on how to construct a copy of the object.
        The JNDI will attempt to turn references looked up from the directory
        into the Java objects that they represent so that
        JNDI clients have the illusion that what
        is stored in the directory are Java objects.

## The Initial Context

In the JNDI, all naming and directory operations are performed relative
to a context. There are no absolute roots.
Therefore the JNDI defines an
[InitialContext](http://download.oracle.com/javase/7/docs/api/javax/naming/InitialContext.html), which provides a starting point for naming and directory operations.
Once you have an initial context, you can use it to
look up other contexts and objects.

## Exceptions

The JNDI defines a class hierarchy for exceptions that can be thrown in
the course of performing naming and directory operations. The root of
this class hierarchy is
[NamingException](http://download.oracle.com/javase/7/docs/api/javax/naming/NamingException.html).
Programs interested in dealing with a particular exception
can catch the corresponding subclass of the exception.
Otherwise, they should catch NamingException.

[« Previous](index.html)
•
[Trail](../TOC.html)
•
[Next »](dir.html)

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

**Previous page:** Overview of JNDI
  
**Next page:** Directory and LDAP Packages




A browser with JavaScript enabled is required for this page to operate properly.