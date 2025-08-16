[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

Advanced Topics for LDAP Users

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

[Frequently Asked Questions](faq.html)

**Trail:** Java Naming and Directory Interface(TM).

[Home Page](../../index.html)
>
[Java Naming and Directory Interface(TM).](../index.html)

[« Previous](../ops/index.html) • [Trail](../TOC.html) • [Next »](ldap.html)

# Lesson: Advanced Topics for LDAP Users

The lessons in the **LDAP** trail provide details on
the mapping between the LDAP and the JNDI.
They also give hints and tips for accessing the LDAP service
through the JNDI.

## LDAP

[X.500](http://java.sun.com/products/jndi/tutorial/ldap/models/x500.html),
is a CCITT standard for directory services that is part of the OSI suite of services.
X.500 standard defines a protocol (among others) for a
client application to access the X.500 directory called the
*Directory Access Protocol* (DAP). It is layered on top of the Open
Systems Interconnection (OSI) protocol stack.

The Internet community, recognizing the need for an X.500-like service but faced with
different underlying network infrastructure (TCP/IP instead of OSI),
designed a new protocol based on the X.500 DAP protocol, called
*Lightweight* DAP, or LDAP.
[RFC 2251](http://ietf.org/rfc/rfc2251.txt)
defines what is now called *version 3* of the LDAP (or LDAP v3),
an improved version of its predecessor
[LDAP v2](http://java.sun.com/products/jndi/tutorial/ldap/models/v2.html) specified in
[RFC 1777](http://ietf.org/rfc/rfc1777.txt).

The goal of the LDAP was a protocol that could be easily
implemented, with special focus on being able to build small and
simple clients. One way that it attempted to achieve
simplification was to use a lot of strings and to minimize wherever possible
the use of structures. DNs, for example, are
represented in the protocol as strings, as are attribute type names
and many attribute values.

The protocol consists of the client's
sending requests to the server, to which the server responds, though
not necessarily in the same order in which the requests were
sent. Each request is tagged with an ID so that requests and
responses can be matched. The protocol works over either
TCP or UDP, although the TCP version is most commonly used.

Because of the focus on clients, the LDAP community also defined standards
for the string representation of DNs
([RFC 2553](http://ietf.org/rfc/rfc2553.txt)),
search filters
([RFC 1960](http://ietf.org/rfc/rfc1960.txt)),
and attribute syntaxes
([RFC 1778](http://ietf.org/rfc/rfc1778.txt)),
for a C language based API
([RFC 1823](http://ietf.org/rfc/rfc1823.txt)),
and for the format of URLs for accessing LDAP services
([RFC 1959](http://ietf.org/rfc/rfc1959.txt)).

LDAP v3 supports internationalization, various authentication mechanisms,
referrals, and a generic deployment mechanism.
It allows new features to be added to the protocol
without also requiring changes to the protocol by using
*extensions* and *controls*.

[« Previous](../ops/index.html)
•
[Trail](../TOC.html)
•
[Next »](ldap.html)

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

**Previous page:** Previous Lesson
  
**Next page:** LDAP v3




A browser with JavaScript enabled is required for this page to operate properly.