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

[Authentication Mechanisms](auth_mechs.html)

[Anonymous](anonymous.html)

Simple

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

[« Previous](anonymous.html) • [Trail](../TOC.html) • [Next »](sasl.html)

# Simple

*Simple* authentication consists of sending the LDAP server the
fully qualified DN of the client (user) and the client's
clear-text password
(see [RFC 2251](http://ietf.org/rfc/rfc2251.txt) and
[RFC 2829](http://ietf.org/rfc/rfc2829.txt)).
This mechanism has security problems because the
password can be read from the network.
To avoid exposing the password in this way,
you can use the simple authentication mechanism
within an encrypted channel (such as SSL), provided that this is supported
by the LDAP server.

Both the LDAP v2 and v3 support simple authentication.

To use the simple authentication mechanism, you must set the three
authentication environment properties as follows.

[Context.SECURITY\_AUTHENTICATION](http://download.oracle.com/javase/7/docs/api/javax/naming/Context.html#SECURITY_AUTHENTICATION).: Set to "simple".

[Context.SECURITY\_PRINCIPAL](http://download.oracle.com/javase/7/docs/api/javax/naming/Context.html#SECURITY_PRINCIPAL).: Set to the fully qualified DN of the entity that is being authenticated (e.g., "cn=S. User, ou=NewHires, o=JNDITutorial"). It is of type java.lang.String.

[Context.SECURITY\_CREDENTIALS](http://download.oracle.com/javase/7/docs/api/javax/naming/Context.html#SECURITY_CREDENTIALS).: Set to the password of the principal (e.g., "mysecret"). It is of type java.lang.String, char array (char[]), or byte array (byte[]). If the password is a java.lang.String or a char array, then it is encoded using UTF-8 for the LDAP v3 and using ISO-Latin-1 for the LDAP v2 for transmission to the server. If the password is a byte[], then it is transmitted as is to the server.

See the [example](authentication.html#SIMPLE) earlier in this section
that illustrates how to use simple authentication.
> ---
>
> **Note:** 
> If you supply an empty string, an empty byte/char array, or null to the
> Context.SECURITY\_CREDENTIALS environment property,
> then the authentication mechanism will be "none".
> This is because the LDAP requires the password to be nonempty
> for simple authentication. The protocol automatically converts
> the authentication to "none" if a password is not supplied.

[« Previous](anonymous.html)
•
[Trail](../TOC.html)
•
[Next »](sasl.html)

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

**Previous page:** Anonymous
  
**Next page:** SASL




A browser with JavaScript enabled is required for this page to operate properly.