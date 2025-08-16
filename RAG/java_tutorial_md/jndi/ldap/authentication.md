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

Modes of Authenticating to LDAP

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

[« Previous](security.html) • [Trail](../TOC.html) • [Next »](auth_mechs.html)

# Modes of Authenticating to LDAP

In the LDAP, authentication information is supplied in the
"bind" operation. In LDAP v2, a client initiates a connection with
the LDAP server by sending the server
a "bind" operation that contains the authentication information.

In the LDAP v3, this operation serves the same purpose, but it is optional.
A client that sends an LDAP request without doing a "bind" is
treated as an *anonymous* client (see the
[Anonymous Authentication](anonymous.html) section for details).
In the LDAP v3, the "bind" operation may be sent at any time,
possibly more than once, during the connection.
A client can send a "bind" request in the middle of a connection to
change its identity. If the request is successful, then all outstanding
requests that use the old identity on the connection are discarded
and the connection is associated with the new identity.

The authentication information supplied in the "bind" operation depends on the
*authentication mechanism* that the client chooses.
See [the next section](auth_mechs.html)
for a discussion of the authentication mechanism.

## Authenticating to the LDAP by Using the JNDI

In the JNDI, authentication information is specified in environment properties.
When you create an initial context by using the
[InitialDirContext](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/InitialDirContext.html) class (or its superclass or subclass),
you supply a set of environment properties, some of which might
contain authentication information.
You can use the following environment properties
to specify the authentication information.

* [Context.SECURITY\_AUTHENTICATION](http://download.oracle.com/javase/7/docs/api/javax/naming/Context.html#SECURITY_AUTHENTICATION) ("java.naming.security.authentication").
    
  Specifies the authentication mechanism to use.
  For the Sun LDAP service provider, this can be one of the following strings:
  "none", "simple", *sasl\_mech*,
  where *sasl\_mech* is a space-separated list of SASL mechanism names.
  See the [next section](auth_mechs.html) for a description of these strings.* [Context.SECURITY\_PRINCIPAL](http://download.oracle.com/javase/7/docs/api/javax/naming/Context.html#SECURITY_PRINCIPAL) ("java.naming.security.principal").
      
    Specifies the name of the user/program doing the authentication
    and depends on the value of the Context.SECURITY\_AUTHENTICATION
    property. See the next few sections in this lesson
    for details and examples.* [Context.SECURITY\_CREDENTIALS](http://download.oracle.com/javase/7/docs/api/javax/naming/Context.html#SECURITY_CREDENTIALS) ("java.naming.security.credentials").
        
      Specifies the credentials of the user/program doing the authentication
      and depends on the value of the Context.SECURITY\_AUTHENTICATION
      property. See the next few sections in this lesson
      for details and examples.

When the initial context is created, the underlying LDAP service provider
extracts the authentication information from these environment properties and
uses the LDAP "bind" operation to pass them to the server.

The [following example](examples/Simple.java) shows how,
by using a simple clear-text password, a client authenticates to an LDAP server.

```

// Set up the environment for creating the initial context
Hashtable env = new Hashtable();
env.put(Context.INITIAL_CONTEXT_FACTORY, 
    "com.sun.jndi.ldap.LdapCtxFactory");
env.put(Context.PROVIDER_URL, "ldap://localhost:389/o=JNDITutorial");

// Authenticate as S. User and password "mysecret"
env.put(Context.SECURITY_AUTHENTICATION, "simple");
env.put(Context.SECURITY_PRINCIPAL, "cn=S. User, ou=NewHires, o=JNDITutorial");
env.put(Context.SECURITY_CREDENTIALS, "mysecret");

// Create the initial context
DirContext ctx = new InitialDirContext(env);

// ... do something useful with ctx

```

## Using Different Authentication Information for a Context

If you want to use different authentication information for an existing
context, then you can use
[Context.addToEnvironment()](http://download.oracle.com/javase/7/docs/api/javax/naming/Context.html#addToEnvironment(java.lang.String, java.lang.Object)) and
[Context.removeFromEnvironment()](http://download.oracle.com/javase/7/docs/api/javax/naming/Context.html#removeFromEnvironment(java.lang.String)) to update the environment properties
that contain the authentication information. Subsequent invocations of methods
on the context will use the new authentication information to
communicate with the server.

The [following example](examples/UseDiff.java) shows how the
authentication information of a context is changed to "none"
after the context has been created.

```

// Authenticate as S. User and the password "mysecret"
env.put(Context.SECURITY_AUTHENTICATION, "simple");
env.put(Context.SECURITY_PRINCIPAL, "cn=S. User, ou=NewHires, o=JNDITutorial");
env.put(Context.SECURITY_CREDENTIALS, "mysecret");

// Create the initial context
DirContext ctx = new InitialDirContext(env);

// ... do something useful with ctx

// Change to using no authentication
ctx.addToEnvironment(Context.SECURITY_AUTHENTICATION, "none");

// ... do something useful with ctx

```

## Authentication Failures

Authentication can fail for a number of reasons.
For example,
if you supply incorrect authentication information, such as an incorrect
password or principal name, then an
[AuthenticationException](http://download.oracle.com/javase/7/docs/api/javax/naming/AuthenticationException.html) is thrown.

Here's [an example](examples/BadPasswd.java) that is a variation of
the previous example. This time, an incorrect password causes
the authentication to fail.

```

// Authenticate as S. User and give an incorrect password
env.put(Context.SECURITY_AUTHENTICATION, "simple");
env.put(Context.SECURITY_PRINCIPAL, "cn=S. User, ou=NewHires, o=JNDITutorial");
env.put(Context.SECURITY_CREDENTIALS, "notmysecret");

```

This produces the following output.

```

javax.naming.AuthenticationException: [LDAP: error code 49 - Invalid Credentials]
	...

```

Because different servers support different authentication mechanisms,
you might request an authentication mechanism that the server
does not support. In this case, an
[AuthenticationNotSupportedException](http://download.oracle.com/javase/7/docs/api/javax/naming/AuthenticationNotSupportedException.html) will be thrown.

Here's [an example](examples/BadAuth.java) that is a variation of
the previous example. This time, an unsupported authentication mechanism
("custom") causes the authentication to fail.

```

// Authenticate as S. User and the password "mysecret"
env.put(Context.SECURITY_AUTHENTICATION, "custom");
env.put(Context.SECURITY_PRINCIPAL, "cn=S. User, ou=NewHires, o=JNDITutorial");
env.put(Context.SECURITY_CREDENTIALS, "mysecret");

```

This produces the following output.

```

javax.naming.AuthenticationNotSupportedException: custom
	...

```

[« Previous](security.html)
•
[Trail](../TOC.html)
•
[Next »](auth_mechs.html)

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

**Previous page:** Security
  
**Next page:** Authentication Mechanisms




A browser with JavaScript enabled is required for this page to operate properly.