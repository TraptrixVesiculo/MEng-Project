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

[Simple](simple.html)

SASL

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

[« Previous](simple.html) • [Trail](../TOC.html) • [Next »](digest.html)

# SASL

The LDAP v3 protocol uses the
[SASL](http://ietf.org/rfc/rfc2222.txt)
to support *pluggable* authentication.
This means that the LDAP client and server can be configured
to negotiate and use possibly nonstandard and/or customized mechanisms
for authentication, depending on the level of protection
desired by the client and the server.
The LDAP v2 protocol does not support the SASL.

Several SASL mechanisms are currently defined:

* Anonymous ([RFC 2245](http://ietf.org/rfc/rfc2245.txt))* CRAM-MD5 ([RFC 2195](http://ietf.org/rfc/rfc2195.txt))* Digest-MD5
      ([RFC 2831](http://ietf.org/rfc/rfc2831.txt))* External ([RFC 2222](http://ietf.org/rfc/rfc2222.txt))* Kerberos V4 ([RFC 2222](http://ietf.org/rfc/rfc2222.txt))* Kerberos V5 ([RFC 2222](http://ietf.org/rfc/rfc2222.txt))* SecurID ([RFC 2808](http://ietf.org/rfc/rfc2808.txt))* S/Key ([RFC 2222](http://ietf.org/rfc/rfc2222.txt))

## SASL Mechanisms Supported by LDAP Servers

Of the mechanisms on the previous list, popular LDAP servers (such as those from
[Sun](http://www.sun.com),
[OpenLDAP](http://www.openldap.com),
and
[Microsoft](http://www.microsoft.com))
support External, Digest-MD5, and Kerberos V5.
[RFC 2829](http://ietf.org/rfc/rfc2829.txt) proposes the use of Digest-MD5
as the mandatory default mechanism for LDAP v3 servers.

Here is a [simple program](examples/ServerSasl.java) for finding
out the list of SASL mechanisms that an LDAP server supports.

```

// Create initial context
DirContext ctx = new InitialDirContext();

// Read supportedSASLMechanisms from root DSE
Attributes attrs = ctx.getAttributes(
    "ldap://localhost:389", new String[]{"supportedSASLMechanisms"});

```

Here is the output produced by running this program
against a server that supports the External SASL mechanism.

```

{supportedsaslmechanisms=supportedSASLMechanisms: EXTERNAL, GSSAPI, DIGEST-MD5}

```

## Specifying the Authentication Mechanism

To use a particular SASL mechanism, you specify its
Internet Assigned Numbers Authority (IANA)-registered
mechanism name in the
[Context.SECURITY\_AUTHENTICATION](http://download.oracle.com/javase/7/docs/api/javax/naming/Context.html#SECURITY_AUTHENTICATION) environment property.
You can also specify a list of mechanisms
for the LDAP provider to try.
This is done
by specifying an ordered list of space-separated mechanism names.
The LDAP provider will use the first
mechanism for which it finds an implementation.

Here's an example that asks the LDAP provider to try to get
the implementation for the
DIGEST-MD5 mechanism and if that's not available,
use the one for GSSAPI.

```

env.put(Context.SECURITY_AUTHENTICATION, "DIGEST-MD5 GSSAPI");

```

You might get this list of authentication mechanisms from
the user of your application. Or you might get it
by asking the LDAP server, via a call similar to that shown previously.
The LDAP provider itself does not consult the server for this
information. It simply attempts to locate and use the implementation
of the specified mechanisms.

The LDAP provider in the platform
has built-in support for the
External, Digest-MD5, and GSSAPI (Kerberos v5) SASL mechanisms.
You can add support for additional mechanisms.

## Specifying Input for the Authentication Mechanism

Some mechanisms, such as External, require no additional
input--the mechanism name alone is sufficient for the authentication
to proceed.
The [External example](ssl.html#EXTERNAL) shows how to use
the External SASL mechanism.

Most other mechanisms require some additional input.
Depending on the mechanism, the type of input might vary.
Following are some common inputs required by mechanisms.

* **Authentication id**. The identity of the entity
  performing the authentication.* **Authorization id**. The identity of the entity
    for which access control checks should be made if the authentication
    succeeds.* **Authentication credentials**. For example, a password or a key.

The authentication and authorization ids might differ
if the program (such as a proxy server) is authenticating on behalf
of another entity.
The authentication id is specified by using the
[Context.SECURITY\_PRINCIPAL](http://download.oracle.com/javase/7/docs/api/javax/naming/Context.html#SECURITY_PRINCIPAL) environment property.
It is of type java.lang.String.

The password/key of the authentication id is specified by using the
[Context.SECURITY\_CREDENTIALS](http://download.oracle.com/javase/7/docs/api/javax/naming/Context.html#SECURITY_CREDENTIALS) environment property.
It is of type java.lang.String, char array (char[]),
or byte array (byte[]).
If the password is a byte array, then it is transformed into a char
array by using an UTF-8 encoding.

If the
"java.naming.security.sasl.authorizationId"
property has been set, then its value is used as the authorization ID.
Its value must be of type java.lang.String.
By default, the empty string is used as the authorization ID, which
directs the server to derive an authorization ID from the
client's authentication credentials.

The [Digest-MD5 example](digest.html) shows how to use the
Context.SECURITY\_PRINCIPAL and Context.SECURITY\_CREDENTIALS
properties for Digest-MD5 authentication.

If a mechanism requires input other than those already described,
then you need to define a *callback* object for the mechanism
to use, you can check out the callback example in the
[JNDI Tutorial](http://java.sun.com/products/jndi/tutorial/ldap/security/callback.html) .
The next part of this lesson discusses how to use SASL Digest-MD5
authentication mechanism. The
[SASL Policies](http://java.sun.com/products/jndi/tutorial/ldap/security/sasl.html)  ,
[GSS API (Kerberos v5)](http://java.sun.com/products/jndi/tutorial/ldap/security/gssapi.html)  and
[CRAM-MD5](http://java.sun.com/products/jndi/tutorial/ldap/security/crammd5.html)  mechanisms are covered in the JNDI Tutorial.

[« Previous](simple.html)
•
[Trail](../TOC.html)
•
[Next »](digest.html)

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

**Previous page:** Simple
  
**Next page:** Digest-MD5




A browser with JavaScript enabled is required for this page to operate properly.