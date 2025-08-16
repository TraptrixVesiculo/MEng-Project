[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Java Naming and Directory Interface(TM).
  
**Lesson:** Advanced Topics for LDAP Users

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

[Search Results](result.html)

[LDAP Unsolicited Notifications](unsol.html)

[Connection Management](connect.html)

[Creation](create.html)

[Closing](close.html)

[Pooling](pool.html)

[Configuration](config.html)

Frequently Asked Questions

[Home Page](../../index.html)
>
[Java Naming and Directory Interface(TM).](../index.html)
>
[Advanced Topics for LDAP Users](index.html)

[« Previous](config.html) • [Trail](../TOC.html) • [Next »](../objects/index.html)

# Frequently Asked Questions

This lesson answers the frequently asked questions
users often have when using the JNDI to access LDAP services.
Some of the common problems are answered in the
[Trouble Shooting Tips](../../jndi/ops/faq.html)  of the Naming and Directory Operations lesson.

---

## Contexts:

1. [Is the context safe for multithreaded access?](#1)- [Why does the LDAP provider ignore my security environment properties?](#2) - [Why do I keep getting a CommunicationException?](#3)- [How can I get a trace of LDAP messages?](#4)- [How do I use a different authentication mechanism such as Kerberos?](#5)- [Should I enable ssl when changing the password?](#6)

           ## Attributes:

           - [When I ask for one attribute, I get back another. Why?](#7)- [How do I know the type of an attribute's value?](#8)- [How do I get back an attribute's value in a form other than a String
                 or byte array?](#9)- [Why does putting an "\*" as an attribute value not work as expected
                   in my search?](#10)

                 ## Searches:

                 - [Why don't wildcards in search filters always work?](#11)- [Why do I get back only *n* number of entries when I know
                     there are more in the directory?](#12)- [How do I pass controls with my search?](#13)- [How do I find out how many search results I got back?](#14)

                       ## Names:

                       - [Why do I get an empty string as a name in my SearchResult?](#15)- [Why do I get a URL string as a name in my SearchResult?](#16)- [What type is the Name argument passed to the context methods?](#17)- [Can I pass the name I got back from NameParser to the Context methods?](#18)- [What's the relationship between the name I use for the
                                 Context.SECURITY\_PRINCIPAL property and the directory?](#19)- [Why are there strange quotation marks and escapes in the names
                                   that I read from the directory?](#20)- [How do I get an LDAP entry's full DN?](#21)

---

**1. Is the context safe for multithreaded access,
or do I need to lock/synchronize access to a context?**

The answer depends on the implementation.
This is because the
[Context](http://download.oracle.com/javase/7/docs/api/javax/naming/Context.html) and
[DirContext](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/DirContext.html) interfaces do not specify synchronization requirements.
Sun's LDAP implementation is optimized for single-threaded access.
If you have multiple threads accessing the same
Context instance, then each thread needs to
lock the Context instance when using it.
This also applies to any NamingEnumeration that is derived from the
same Context instance.
However, multiple threads can access *different*
Context instances
(even those derived from the same initial context) concurrently
without locks.

**2. Why does the LDAP provider ignore my security environment properties
if I do not set the
[Context.SECURITY\_CREDENTIALS](http://download.oracle.com/javase/7/docs/api/javax/naming/Context.html#SECURITY_CREDENTIALS) ("java.naming.security.credentials") property or set it to the empty string?**

If you supply an empty string, an empty byte/char array, or null to the
Context.SECURITY\_CREDENTIALS environment property,
then an anonymous bind will occur even if the
Context.SECURITY\_AUTHENTICATION property
was set to "simple".
This is because for simple authentication,
the LDAP requires the password to be nonempty.
If a password is not supplied,
then the protocol automatically converts the authentication to "none".

**3. Why do I keep getting a
[CommunicationException](http://download.oracle.com/javase/7/docs/api/javax/naming/CommunicationException.html) when I try to create an initial context?**

You might be talking to a server that supports only the LDAP v2.
See the Miscellaneous lesson of the
[JNDI Tutorial](http://java.sun.com/products/jndi/tutorial/ldap/misc/version.html)  for an example of how to set the version number.

**4. How can I trace the LDAP message?**

Try using the "com.sun.jndi.ldap.trace.ber" environment
property. If the value of this property is an instance of
java.io.OutputStream, then trace information about BER buffers
sent and received by the LDAP provider is written to that stream. If
the property's value is null, then no trace output is written.

For example, the following code will send the trace output to System.err.

```

env.put("com.sun.jndi.ldap.trace.ber", System.err);

```

**5. How do I use a different authentication mechanism such as
Kerberos?**

Follow the instructions in the GSS-API/Kerberos v5 Authentication
of the
[JNDI Tutorial](http://java.sun.com/products/jndi/tutorial/ldap/security/gssapi.html)  for information on how to use Kerberos authentication.
To use other authentication mechanisms, see the
Using Arbitrary SASL Mechanisms section of the
[JNDI tutorial](http://java.sun.com/products/jndi/tutorial/ldap/security/mechanism.html) .

**6. Should I enable SSL when changing the password?**
/

It really depends on the directory server you are using. Some directory
servers won't allow you to change the password if SSL is not enabled but
some do allow it.
It's good to have SSL enabled to have your password secured in the
communication channel.

**7. When I ask for one attribute, I get back another. Why?**

The attribute name that you are using might be a synonym for another attribute.
In this case, the LDAP server might return the canonical attribute name instead
of the one that you supplied.
When you look in the Attributes returned by
the server, you need to use the canonical name instead
of the synonym.

For example, "fax" might be a synonym for the canonical
attribute name "facsimiletelephonenumber".
If you ask for "fax", the server will return the attribute
named "facsimiletelephonenumber".
See the
[Naming and Directory Operations](../../jndi/ops/attrnames.html)  lesson for details on synonyms and other issues regarding
attribute names.

**8. How do I know the type of an attribute's value?**

An attribute's value can be either java.lang.String or byte[].
See the Miscellaneous section of the
[JNDI Tutorial](http://java.sun.com/products/jndi/tutorial/ldap/misc/attrs.html)  for information on which attributes' values are returned
as byte[].
To do this programmatically,
you can use the instanceof operator to examine
the attribute value that you get back from the LDAP provider.

**9. How do I get back an attribute's value in a form
other than a String or byte array?**

Currently you can't. The LDAP provider returns only attribute values
that are either java.lang.String or byte[].
See the Miscellaneous section of the
[JNDI Tutorial](http://java.sun.com/products/jndi/tutorial/ldap/misc/attrs.html)  .

**10. Why does putting an "\*" as an attribute value not work as expected
in my search?**

When you use the following form of search(),
the attribute values are treated as literals; that is, the
attribute in the directory entry is expected to contain exactly that value:
[search(Name name, Attributes matchingAttrs)](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/DirContext.html#search(javax.naming.Name, javax.naming.directory.Attributes))
To use wildcards, you should use the string filter forms of
search(), as follows.
[search(Name name, String filter, SearchControls ctls)](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/DirContext.html#search(javax.naming.Name, java.lang.String, javax.naming.directory.SearchControls))  
[search(Name name, String filterExpr, Object[]filterArgs, SearchControls ctls)](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/DirContext.html#search(javax.naming.Name, java.lang.String, java.lang.Object[], javax.naming.directory.SearchControls))

For the last form, the wildcard characters must appear in the filterExpr
argument, and not in filterArgs.
The values in filterArgs are also treated as literals.

**11. Why don't wildcards in search filters always work?**

A wildcard that appears before or after the attribute value (such as
in "attr=\*I\*") indicates that the server is to search for matching
attribute values by using the attribute's substring matching rule. If
the attribute's definition does not have a substring matching rule,
then the server cannot find the attribute. You'll have to search
by using an equality or "present" filter instead.

**12. Why do I get back only *n* number of entries when I know
there are more in the directory?**
Some servers are configured to limit the number
of entries that can be returned. Others also limit the number
of entries that can be examined during a search.
Check your server configuration.

**13. How do I pass controls with my search?**

Controls are not explained in this tutorial.
Check out the
[JNDI Tutorial](http://java.sun.com/products/jndi/tutorial/ldap/ext/context.html)  .

**14. How do I find out how many search results I got back?**

You must keep count as you enumerate
through the results. The LDAP does not provide this information.

**15. Why do I get an empty string as a name in my
[SearchResult](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/SearchResult.html)?**

[getName()](http://download.oracle.com/javase/7/docs/api/javax/naming/NameClassPair.html#getName()) always returns a name *relative* to the *target context*
of the search.
So, if the target context satisfies the search filter,
then the name returned will be "" (the empty name) because that is
the name relative to the target context.
See the
[Search Results](result.html)  section for details.

**16. Why do I get a URL string as a name in my
[SearchResult](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/SearchResult.html)?**

The LDAP entry was retrieved by following either an alias or
a referral, so its name is a URL.
See the
[Search Results](result.html)  lesson for details.

**17. What type is the
[Name](http://download.oracle.com/javase/7/docs/api/javax/naming/Name.html) argument passed to the
[Context](http://download.oracle.com/javase/7/docs/api/javax/naming/Context.html) and
[DirContext](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/DirContext.html) methods? - a
[CompoundName](http://download.oracle.com/javase/7/docs/api/javax/naming/CompoundName.html) or a
[CompositeName](http://download.oracle.com/javase/7/docs/api/javax/naming/CompositeName.html)?**

The string forms accept the string representation of a composite name.
That is, using a string name is equivalent to calling
new CompositeName(stringName) and passing the results
to the Context/DirContext method.
The Name argument can be any object that implements the
Name interface.
If it is an instance of CompositeName,
then the name is treated as a composite name; otherwise, it is treated
as a compound name.

**18. Can I pass the name I got back from
[NameParser](http://download.oracle.com/javase/7/docs/api/javax/naming/NameParser.html) to
[Context](http://download.oracle.com/javase/7/docs/api/javax/naming/Context.html) methods?**

This is related to the previous question.
Yes, you can.
[NameParser.parse()](http://download.oracle.com/javase/7/docs/api/javax/naming/NameParser.html#parse(java.lang.String)) returns a compound name that implements the Name interface.
This name can be passed to the Context methods, which will
interpret it as a compound name.

**19. What's the relationship between the name I use for the
[Context.SECURITY\_PRINCIPAL](http://download.oracle.com/javase/7/docs/api/javax/naming/Context.html#SECURITY_PRINCIPAL) property and the directory?**You can think of the principal name
as coming from a different namespace than the directory.
See
[RFC 2829](http://ietf.org/rfc/rfc2829.txt)
and the
[Security](../../jndi/ldap/security.html)  section for details on LDAP authentication mechanisms.
Sun's LDAP service provider accepts a string principal name, which
it passes directly to the LDAP server.
Some LDAP servers accept DNs, whereas
others support the schemes proposed by
[RFC 2829](http://ietf.org/rfc/rfc2829.txt).

**20. Why are there strange quotation marks and escapes in the names
that I read from the directory?**

Sun's LDAP name parser is conservative with respect to quoting
rules,
but it nevertheless produces "correct" names.
Also, remember that the names of entries returned by
[NamingEnumerations](http://download.oracle.com/javase/7/docs/api/javax/naming/NamingEnumeration.html) are
composite names
that can be passed back to the Context and DirContext
methods. So, if the name contains a character that conflicts with
the composite name syntax (such as the forward slash character "/"),
then the LDAP provider will provide an encoding to ensure that the
slash character will be treated as part of the LDAP name rather than as a composite
name separator.

Start using the
[LdapName](http://download.oracle.com/javase/7/docs/api/javax/naming/ldap/LdapName.html) and
[Rdn](http://download.oracle.com/javase/7/docs/api/javax/naming/ldap/Rdn.html) classes that enable easy name manipulation.

**21. How do I get an LDAP entry's full DN?**You can use
[NameClassPair.getNameInNamespace()](http://download.oracle.com/javase/7/docs/api/javax/naming/NameClassPair.html#getNameInNamespace()).

---

[« Previous](config.html)
•
[Trail](../TOC.html)
•
[Next »](../objects/index.html)

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

**Previous page:** Configuration
  
**Next page:** Java Objects in the Directory




A browser with JavaScript enabled is required for this page to operate properly.