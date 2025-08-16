[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Java Naming and Directory Interface(TM).
  
**Lesson:** Advanced Topics for LDAP Users
  
**Section:** JNDI as an LDAP API

[Advanced Topics for LDAP Users](index.html)

[LDAP v3](ldap.html)

[JNDI as an LDAP API](jndi.html)

How LDAP Operations Map to JNDI APIs

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

[Search Results](result.html)

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

[« Previous](jndi.html) • [Trail](../TOC.html) • [Next »](exceptions.html)

# How LDAP Operations Map to JNDI APIs

The LDAP defines a set of operations or requests
(see
[RFC 2251](http://ietf.org/rfc/rfc2251.txt)).
In the JNDI, these map to operations on the
[DirContext](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/DirContext.html) and
[LdapContext](http://download.oracle.com/javase/7/docs/api/javax/naming/ldap/LdapContext.html) interfaces (which are sub interfaces of
[Context](http://download.oracle.com/javase/7/docs/api/javax/naming/Context.html)).
For example, when a caller invokes a DirContext method,
the LDAP service provider implements the method by sending LDAP requests
to the LDAP server.

The following table shows how operations in the LDAP correspond to
JNDI methods.

| LDAP Operation | Corresponding JNDI Methods |
| --- | --- |
| bind | The corresponding way of creating an initial connection to the LDAP server in the JNDI is the creation of an [InitialDirContext](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/InitialDirContext.html). When the application creates an initial context, it supplies client authentication information via environment properties. To change that authentication information for an existing context, use [Context.addToEnvironment()](http://download.oracle.com/javase/7/docs/api/javax/naming/Context.html#addToEnvironment(java.lang.String, java.lang.Object)) and [Context.removeFromEnvironment()](http://download.oracle.com/javase/7/docs/api/javax/naming/Context.html#removeFromEnvironment(java.lang.String)). |
| unbind | [Context.close()](http://download.oracle.com/javase/7/docs/api/javax/naming/Context.html#close) is used to free resources used by a context. It differs from the LDAP "unbind" operation in that within a given service provider implementation, resources can be shared among contexts, so closing one context won't free all of the resources if those resources are being shared with another context. Make sure to close all contexts if your intent is to free all resources. |
| search | The corresponding method in the JNDI is the overloading of [DirContext.search()](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/DirContext.html#search(java.lang.String, java.lang.String, javax.naming.directory.SearchControls)) that accepts a search filter ([RFC 2254](http://ietf.org/rfc/rfc2254.txt)). See the [filter](../../jndi/ops/filter.html)  example. |
| modify | The corresponding method in the JNDI is the overloading of [DirContext.modifyAttributes()](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/DirContext.html#modifyAttributes(java.lang.String, javax.naming.directory.ModificationItem[])) that accepts an array of [DirContext.ModificationItems](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/ModificationItem.html). See the [Modify Attributes](../../jndi/ops/modattrs.html)   section for an example. |
| add | The corresponding methods in the JNDI are [DirContext.bind()](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/DirContext.html#bind(java.lang.String, java.lang.Object, javax.naming.directory.Attributes)) and [DirContext.createSubcontext()](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/DirContext.html#createSubcontext(java.lang.String, javax.naming.directory.Attributes)). You can use either to add a new LDAP entry. Using bind(), you can specify not only a set of attributes for the new entry but also a Java object to be added along with the attributes. See the [Add, replace bindings with Attributes](../../jndi/ops/bindattr.html)   section for an example. |
| delete | The corresponding methods in the JNDI are [Context.unbind()](http://download.oracle.com/javase/7/docs/api/javax/naming/Context.html#unbind(java.lang.String)) and [Context.destroySubcontext()](http://download.oracle.com/javase/7/docs/api/javax/naming/Context.html#destroySubcontext(java.lang.String)). You can use either to remove an LDAP entry. |
| modify DN/RDN | The corresponding method in the JNDI is [Context.rename()](http://download.oracle.com/javase/7/docs/api/javax/naming/Context.html#rename(java.lang.String, java.lang.String)). See the [Renaming Objects](../../jndi/ldap/rename.html)  section for more details. |
| compare | The corresponding operation in the JNDI is a suitably constrained [DirContext.search()](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/DirContext.html#search(java.lang.String, javax.naming.directory.Attributes, java.lang.String[])). See the [LDAP Compare](../../jndi/ldap/compare.html)   section for an example. |
| abandon | When you close a context, all of its outstanding requests are abandoned. Similarly, when you close a [NamingEnumeration](http://download.oracle.com/javase/7/docs/api/javax/naming/NamingEnumeration.html), the corresponding LDAP "search" request is abandoned. |
| extended operation | The corresponding method in the JNDI is [LdapContext.extendedOperation()](http://download.oracle.com/javase/7/docs/api/javax/naming/ldap/LdapContext.html#extendedOperation(javax.naming.ldap.ExtendedRequest)). See the [JNDI Tutorial](http://java.sun.com/products/jndi/tutorial/ldap/ext/index.html)  for more details. |

[« Previous](jndi.html)
•
[Trail](../TOC.html)
•
[Next »](exceptions.html)

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

**Previous page:** JNDI as an LDAP API
  
**Next page:** How LDAP Error Codes Map to JNDI Exceptions




A browser with JavaScript enabled is required for this page to operate properly.