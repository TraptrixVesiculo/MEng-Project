[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Java Naming and Directory Interface(TM).
  
**Lesson:** Overview of JNDI

[Overview of JNDI](index.html)

[Naming Package](naming.html)

Directory and LDAP Packages

[Event and Service Provider Packages](event.html)

[Home Page](../../index.html)
>
[Java Naming and Directory Interface(TM).](../index.html)
>
[Overview of JNDI](index.html)

[« Previous](naming.html) • [Trail](../TOC.html) • [Next »](event.html)

# Directory and LDAP Packages

## Directory Package

The
[javax.naming](http://download.oracle.com/javase/7/docs/api/javax/naming/package-summary.html) 
package to provide functionality for accessing directory services
in addition to naming services.
This package allows applications to retrieve  *associated with
objects stored in the directory and to search for objects using specified
attributes.

### The Directory Context

The
[DirContext](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/DirContext.html )interface represents a *directory context*.
DirContext also behaves as a naming context by extending the
[getAttributes()](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/DirContext.html#getAttributes(javax.naming.Name) )to retrieve the attributes associated with a directory entry
(for which you supply the name). Attributes are modified using
[modifyAttributes()](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/DirContext.html#search(javax.naming.Name, javax.naming.directory.Attributes))method. Other overloaded forms of
[search()](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/DirContext.html#search(javax.naming.Name, java.lang.String, javax.naming.directory.SearchControls))support more sophisticated search filters.

## LDAP Package

The
[javax.naming.ldap](http://download.oracle.com/javase/7/docs/api/javax/naming/ldap/package-summary.html ) package contains classes and interfaces for using features that are
specific to the [LDAP v3](http://ietf.org/rfc/rfc2251.txt) that are not already
covered by the more generic
[javax.naming.directory](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/package-summary.html) package.
In fact, most JNDI applications that use the LDAP will find the `javax.naming.directory`
package sufficient and will not need to use the javax.naming.ldap
package at all. This package is primarily for those applications that need
to use "extended" operations, controls, or unsolicited notifications.

"Extended" Operation
:   In addition to specifying well defined operations such as search and
    modify, the [LDAP v3 (RFC 2251)](http://ietf.org/rfc/rfc2251.txt) specifies
    a way to transmit yet-to-be defined operations between the LDAP client and
    the server. These operations are called *"extended" operations*. An
    "extended" operation may be defined by a standards organization such as the
    Internet Engineering Task Force (IETF) or by a vendor.

Controls
:   The [LDAP v3](http://ietf.org/rfc/rfc2251.txt) allows any request or
    response to be augmented by yet-to-be defined modifiers, called *controls*
    . A control sent with a request is a *request control* and a control
    sent with a response is a *response control* . A control may be defined
    by a standards organization such as the IETF or by a vendor. Request controls
    and response controls are not necessarily paired, that is, there need not
    be a response control for each request control sent, and vice versa.

Unsolicited Notifications
:   In addition to the normal request/response style of interaction between
    the client and server, the [LDAP v3](http://ietf.org/rfc/rfc2251.txt) also specifies
    *unsolicited notifications*--messages that are sent from the
    server to the client asynchronously and not in response to any client request.

### The LDAP Context

The
[LdapContext](http://download.oracle.com/javase/7/docs/api/javax/naming/ldap/LdapContext.html )interface represents a *context* for performing "extended"
operations, sending request controls, and receiving response controls. Examples
of how to use these features are described in the JNDI Tutorial's
[Controls and Extensions](http://java.sun.com/products/jndi/tutorial/ldap/ext/index.html ) lesson.*

[« Previous](naming.html)
•
[Trail](../TOC.html)
•
[Next »](event.html)

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

**Previous page:** Naming Package
  
**Next page:** Event and Service Provider Packages




A browser with JavaScript enabled is required for this page to operate properly.