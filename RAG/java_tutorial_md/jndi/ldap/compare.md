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

LDAP Compare

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

[« Previous](rename.html) • [Trail](../TOC.html) • [Next »](result.html)

# LDAP Compare

The LDAP "compare" operation allows a client to ask the server
whether the named entry has an attribute/value pair.
This allows the server to keep certain attribute/value pairs secret
(i.e., not exposed for general "search" access) while still allowing
the client limited use of them.
Some servers might use this feature for passwords, for example, although
it is insecure for the client to pass clear-text passwords in
the "compare" operation itself.

To accomplish this in the JNDI, use suitably constrained
arguments for the following methods:

* [search(Name name, String filter, SearchControls ctls)](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/DirContext.html#search(javax.naming.Name, java.lang.String, javax.naming.directory.SearchControls))* [search(Name name, String filterExpr, Object[]filterArgs, SearchControls ctls)](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/DirContext.html#search(javax.naming.Name, java.lang.String, java.lang.Object[], javax.naming.directory.SearchControls))

1. The filter must be of the form "(*name*=*value*)".
   You cannot use wild cards.
2. The search scope must be
   [SearchControls.OBJECT\_SCOPE](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/SearchControls.html#OBJECT_SCOPE).
3. You must request that no attributes be returned. If these
   criteria are not met, then these methods will use an LDAP "search"
   operation instead of an LDAP "compare" operation.

Here's [an example](examples/Compare.java) that causes an LDAP "compare"
operation to be used.

```

// Value of the attribute
byte[] key = {(byte)0x61, (byte)0x62, (byte)0x63, (byte)0x64, 
    (byte)0x65, (byte)0x66, (byte)0x67};

// Set up the search controls
SearchControls ctls = new SearchControls();
ctls.setReturningAttributes(new String[0]);       // Return no attrs
ctls.setSearchScope(SearchControls.OBJECT_SCOPE); // Search object only

// Invoke search method that will use the LDAP "compare" operation
NamingEnumeration answer = ctx.search("cn=S. User, ou=NewHires", 
    "(mySpecialKey={0})", new Object[]{key}, ctls);

```

If the compare is successful, the resulting enumeration will contain
a single item whose name is the empty name and which contains no attributes.

[« Previous](rename.html)
•
[Trail](../TOC.html)
•
[Next »](result.html)

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

**Previous page:** More LDAP Operations
  
**Next page:** Search Results




A browser with JavaScript enabled is required for this page to operate properly.