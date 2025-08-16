[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Java Naming and Directory Interface(TM).
  
**Lesson:** Advanced Topics for LDAP Users
  
**Section:** Security

[Advanced Topics for LDAP Users](index.html)

[LDAP v3](ldap.html)

[JNDI as an LDAP API](jndi.html)

[How LDAP Operations Map to JNDI APIs](operations.html)

[How LDAP Error Codes Map to JNDI Exceptions](exceptions.html)

[Security](security.html)

[Modes of Authenticating to LDAP](authentication.html)

Authentication Mechanisms

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

[« Previous](authentication.html) • [Trail](../TOC.html) • [Next »](anonymous.html)

# Authentication Mechanisms

Different versions of the LDAP
support different types of authentication.
The LDAP v2 defines three types of authentication: anonymous, simple
(clear-text password), and Kerberos v4.

The LDAP v3 supports anonymous, simple, and SASL authentication.
SASL is the Simple Authentication
and Security Layer ([RFC 2222](http://ietf.org/rfc/rfc2222.txt)).
It specifies a challenge-response protocol in which data is
exchanged between the client and the server for the purposes of
authentication and establishment of a security layer on which to
carry out subsequent communication.
By using SASL, the LDAP can support any type of
authentication agreed upon by the LDAP client and server.

This lesson contains descriptions of how to authenticate by using
[anonymous](anonymous.html), [simple](simple.html),
and [SASL](sasl.html) authentication.

## Specifying the Authentication Mechanism

The authentication mechanism is specified by using the
[Context.SECURITY\_AUTHENTICATION](http://download.oracle.com/javase/7/docs/api/javax/naming/Context.html#SECURITY_AUTHENTICATION) environment property.
The property may have one of the following values.

|  |  |
| --- | --- |
| *sasl\_mech* | A space-separated list of SASL mechanism names. Use one of the SASL mechanisms listed (e.g., "CRAM-MD5" means to use the CRAM-MD5 SASL mechanism described in [RFC 2195](http://ietf.org/rfc/rfc2195.txt)). |
| none | Use no authentication (anonymous) |
| simple | Use weak authentication (clear-text password) |

## The Default Mechanism

If the client does not specify any authentication environment properties,
then the default authentication mechanism is "none".
The client will then be treated as an anonymous client.

If the client specifies authentication information without explicitly specifying
the Context.SECURITY\_AUTHENTICATION property, then the default
authentication mechanism is "simple".

[« Previous](authentication.html)
•
[Trail](../TOC.html)
•
[Next »](anonymous.html)

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

**Previous page:** Modes of Authenticating to LDAP
  
**Next page:** Anonymous




A browser with JavaScript enabled is required for this page to operate properly.