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

[SASL](sasl.html)

Digest-MD5

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

[« Previous](sasl.html) • [Trail](../TOC.html) • [Next »](ssl.html)

# Digest-MD5

*Digest-MD5 authentication* is the required authentication
mechanism for LDAP v3 servers
([RFC 2829](http://ietf.org/rfc/rfc2829.txt)).
Because the use of SASL is part of the LDAP v3
([RFC 2251](http://ietf.org/rfc/rfc2251.txt)),
servers that support only the LDAP v2 do not support Digest-MD5.

The Digest-MD5 mechanism is described in
[RFC 2831](http://ietf.org/rfc/rfc2831.txt).
It is based on the HTTP Digest Authentication
([RFC 2617](http://ietf.org/rfc/rfc2617.txt)).
In Digest-MD5, the LDAP server sends data that includes
various authentication options that it is willing to support plus
a special token to the LDAP client.
The client responds by sending an encrypted response that indicates the
authentication options that it has selected. The response is encrypted
in such a way that proves that the client knows its password.
The LDAP server then decrypts and verifies the client's response.

To use the Digest-MD5 authentication mechanism, you must set the
authentication environment properties as follows.

[Context.SECURITY\_AUTHENTICATION](http://download.oracle.com/javase/7/docs/api/javax/naming/Context.html#SECURITY_AUTHENTICATION).: Set to the string "DIGEST-MD5".

[Context.SECURITY\_PRINCIPAL](http://download.oracle.com/javase/7/docs/api/javax/naming/Context.html#SECURITY_PRINCIPAL).: Set to the principal name. This is a server-specific format. Some servers support a login user id format, such as that defined for Unix or Windows login screens. Others accept a distinguished name. Yet others use the authorization id formats defined in [RFC 2829](http://ietf.org/rfc/rfc2829.txt). In that RFC, the name should be either the string "dn:", followed by the fully qualified DN of the entity being authenticated, or the string "u:", followed by the user id. Some servers accept multiple formats. Examples of some of these formats are "cuser", "dn: cn=C. User, ou=NewHires, o=JNDITutorial", and "u: cuser" The data type of this property must be java.lang.String.

[Context.SECURITY\_CREDENTIALS](http://download.oracle.com/javase/7/docs/api/javax/naming/Context.html#SECURITY_CREDENTIALS).: Set to the password of the principal (e.g., "mysecret"). It is of type java.lang.String, char array (char[]), or byte array (byte[]). If the password is a java.lang.String or char[], then it is encoded by using UTF-8 for transmission to the server. If the password is a byte[], then it is transmitted as is to the server.

The [following example](examples/Digest.java) shows how a
client performs authentication using Digest-MD5 to an LDAP server.

```

// Set up the environment for creating the initial context
Hashtable env = new Hashtable();
env.put(Context.INITIAL_CONTEXT_FACTORY, 
    "com.sun.jndi.ldap.LdapCtxFactory");
env.put(Context.PROVIDER_URL, "ldap://localhost:389/o=JNDITutorial");

// Authenticate as C. User and password "mysecret"
env.put(Context.SECURITY_AUTHENTICATION, "DIGEST-MD5");
env.put(Context.SECURITY_PRINCIPAL, "dn:cn=C. User, ou=NewHires, o=JNDITutorial");
env.put(Context.SECURITY_CREDENTIALS, "mysecret");

// Create the initial context
DirContext ctx = new InitialDirContext(env);

// ... do something useful with ctx

```

---

**Note:** The [Sun Java Directory Server, v5.2](http://www.oracle.com/us/sun/index.html)
supports the Digest-MD5 authentication mechanism for users that have
clear-text passwords. You must set the password encryption mode *before*
you create the user. If you have already created the user, delete it
and recreate it.
To set the password encryption mode using
the Administration Console, select the Configuration tab and the Data
node. In the Passwords pane, select the
"No encryption (CLEAR)" option for
"Password encryption."
The server accepts simple user names (that is, the value of the
"uid" attribute for entries that have one) and the "dn:" format
of user names.
See the server's documentation for detailed information.

---

## Specifying the Realm

A *realm* defines the namespace from which the authentication
entity (the value of the Context.SECURITY\_PRINCIPAL property)
is selected. A server might have multiple realms. For example, a
server for a university might be configured to have two realms, one
for its student users and another for faculty users. Realm
configuration is done by the directory administrator. Some
directories have a default single realm. For example, the Sun Java
Directory Server, v5.2, uses the fully qualified hostname of the machine
as the default realm.

In Digest-MD5 authentication, you must authenticate to a specific realm.
You may use the following authentication environment property to
specify the realm. If you do not specify a realm, then any one of the
realms offered by the server will be used.

java.naming.security.sasl.realm: Set to the realm of the principal. This is a deployment-specific and/or server-specific case-sensitive string. It identifies the realm or domain from which the principal name (Context.SECURITY\_PRINCIPAL) should be chosen. If this realm does not match one of the realms offered by the server, then the authentication fails.

The [following example](examples/DigestRealm.java) shows how to
set the environment properties for
performing authentication using Digest-MD5 and a specified realm.
To make this example work in your environment, you must change
the source code so that the realm value reflects what has been
configured on your directory server.

```

// Authenticate as C. User and password "mysecret" in realm "JNDITutorial"
env.put(Context.SECURITY_AUTHENTICATION, "DIGEST-MD5");
env.put(Context.SECURITY_PRINCIPAL, "dn:cn=C. User, ou=NewHires, o=JNDITutorial");
env.put(Context.SECURITY_CREDENTIALS, "mysecret");
env.put("java.naming.security.sasl.realm", "JNDITutorial");

```

If you need to use
[privacy protection](http://java.sun.com/products/jndi/tutorial/ldap/security/digest.html)  and other SASL properties, these are discussed in the JNDI Tutorial.

[« Previous](sasl.html)
•
[Trail](../TOC.html)
•
[Next »](ssl.html)

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

**Previous page:** SASL
  
**Next page:** SSL and Custom Sockets




A browser with JavaScript enabled is required for this page to operate properly.