[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Java Naming and Directory Interface(TM).
  
**Lesson:** Advanced Topics for LDAP Users
  
**Section:** More LDAP Operations

[Advanced Topics for LDAP Users](index.html)

[LDAP v3](ldap.html)

[JNDI as an LDAP API](jndi.html)

[How LDAP Operations Map to JNDI APIs](operations.html)

[How LDAP Error Codes Map to JNDI Exceptions](exceptions.html)

[Security](security.html)

[Modes of Authenticating to LDAP](authentication.html)

[Authentication Mechanisms](auth_mechs.html)

[Anonymous](anonymous.html)

[Simple](simple.html)

[SASL](sasl.html)

[Digest-MD5](digest.html)

[SSL and Custom Sockets](ssl.html)

[More LDAP Operations](rename.html)

[LDAP Compare](compare.html)

Search Results

[LDAP Unsolicited Notifications](unsol.html)

[Connection Management](connect.html)

[Creation](create.html)

[Closing](close.html)

[Pooling](pool.html)

[Configuration](config.html)

[Frequently Asked Questions](faq.html)

[Home Page](../../index.html)
>
[Java Naming and Directory Interface(TM).](../index.html)
>
[Advanced Topics for LDAP Users](index.html)

[« Previous](compare.html) • [Trail](../TOC.html) • [Next »](unsol.html)

# Search Results

When you use the search methods in the
[DirContext](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/DirContext.html) interface,
you get back a
[NamingEnumeration](http://download.oracle.com/javase/7/docs/api/javax/naming/NamingEnumeration.html).
Each item in NamingEnumeration is a
[SearchResult](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/SearchResult.html), which contains the following information:

* [Name](#NAME)* [Object](#OBJ)* [Class name](#CLASS)* [Attributes](#ATTRS)

## Name
Each SearchResult contains the name of the LDAP entry that satisfied
the search filter. You obtain the name of the entry by using
[getName()](http://download.oracle.com/javase/7/docs/api/javax/naming/NameClassPair.html#getName()).
This method returns the
[composite name](http://download.oracle.com/javase/7/docs/api/javax/naming/CompositeName.html) of the LDAP entry *relative* to
the *target context*. The target context is the context
to which the
name parameter resolves.
In LDAP parlance, the target context is the *base object* for the search.
Here's an example.

```

NamingEnumeration answer = ctx.search("ou=NewHires", 
    "(&(mySpecialKey={0}) (cn=*{1}))",      // Filter expression
    new Object[]{key, name},                // Filter arguments
    null);				    // Default search controls

```

The target context in this example is that named by
"ou=NewHires".
The names in SearchResults in answer
are relative to "ou=NewHires".
For example, if getName() returns "cn=J. Duke",
then its name relative to ctx will be
"cn=J. Duke, ou=NewHires".

If you performed the search by using
[SearchControls.SUBTREE\_SCOPE](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/SearchControls.html#SUBTREE_SCOPE) or
[SearchControls.OBJECT\_SCOPE](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/SearchControls.html#OBJECT_SCOPE) and the target context itself satisfied the search filter,
then the name returned will be "" (the empty name) because that is
the name relative to the target context.

This isn't the whole story. If the search involves referrals
(see the
[JNDI Tutorial](http://java.sun.com/products/jndi/tutorial/ldap/referral/index.html)  )
or dereferencing aliases (see the
[JNDI Tutorial](http://java.sun.com/products/jndi/tutorial/ldap/misc/aliases.html) ), then the corresponding SearchResults will have names
that are not relative to the target context.
Instead, they will be URLs that refer directly to the entry.
To determine whether the name returned by getName() is relative
or absolute, use
[isRelative()](http://download.oracle.com/javase/7/docs/api/javax/naming/NameClassPair.html#isRelative()). If this method returns true, then the name is relative
to the target context; if it returns false, the name is a URL.

If the name is a URL and you need to use that URL, then you can pass it to the
initial context, which understands URLs (see the
[JNDI Tutorial](http://java.sun.com/products/jndi/tutorial/ldap/misc/url.html) ).

If you need to get the entry's full DN,
you can use
[NameClassPair.getNameInNamespace()](http://download.oracle.com/javase/7/docs/api/javax/naming/NameClassPair.html#getNameInNamespace()).
## Object
If the search was conducted requesting that the entry's object be returned
[(SearchControls.setReturningObjFlag()](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/SearchControls.html#setReturningObjFlag(boolean)) was invoked with true),
then SearchResult will contain an object that represents the entry.
To retrieve this object, you invoke
[getObject()](http://download.oracle.com/javase/7/docs/api/javax/naming/Binding.html#getObject()).
If a java.io.Serializable,
[Referenceable](http://download.oracle.com/javase/7/docs/api/javax/naming/Referenceable.html), or
[Reference](http://download.oracle.com/javase/7/docs/api/javax/naming/Reference.html) object was previously bound to that LDAP name,
then the attributes from the entry are used to reconstruct that object
(see the example in the
[JNDI Tutorial](http://java.sun.com/products/jndi/tutorial/objects/reading/search.html) ).
Otherwise, the attributes from the entry are used to create
a DirContext instance that represents the LDAP entry.
In either case,
the LDAP provider invokes
[DirectoryManager.getObjectInstance()](http://download.oracle.com/javase/7/docs/api/javax/naming/spi/DirectoryManager.html#getObjectInstance(java.lang.Object, javax.naming.Name, javax.naming.Context, java.util.Hashtable, javax.naming.directory.Attributes)) on the object and returns the results.
## Class Name
If the search was conducted requesting that the entry's object be returned,
then the class name is derived from the returned object.
If the search requested attributes that included the retrieval
of the "javaClassName" attribute of the LDAP entry, then the
class name is the value of that attribute.
Otherwise, the class name is "javax.naming.directory.DirContext".
The class name is obtained from
[getClassName()](http://download.oracle.com/javase/7/docs/api/javax/naming/NameClassPair.html#getClassName()).
## Attributes
When you perform a search, you can select the return attributes
either by supplying a parameter to one of the
[search()](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/DirContext.html#search(javax.naming.Name, javax.naming.directory.Attributes, java.lang.String[])) methods or by setting the search controls using
[SearchControls.setReturningAttributes()](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/SearchControls.html#setReturningAttributes(java.lang.String[])).
If no attributes have been specified explicitly,
then all of the LDAP entry's attributes
are returned. To specify that no attributes be returned, you must
pass an empty array (new String[0]).

To retrieve the LDAP entry's attributes, you invoke
[getAttributes()](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/SearchResult.html#getAttributes()) on the SearchResult.

## Response Controls

See the
[Controls and Extensions](http://java.sun.com/products/jndi/tutorial/ldap/ext/response.html)lesson of the JNDI Tutorial for details on how to retrieve a search result's response controls.

[« Previous](compare.html)
•
[Trail](../TOC.html)
•
[Next »](unsol.html)

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

**Previous page:** LDAP Compare
  
**Next page:** LDAP Unsolicited Notifications




A browser with JavaScript enabled is required for this page to operate properly.