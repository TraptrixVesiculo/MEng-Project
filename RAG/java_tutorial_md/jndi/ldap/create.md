[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Java Naming and Directory Interface(TM).
  
**Lesson:** Advanced Topics for LDAP Users
  
**Section:** Connection Management

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

Creation

[Closing](close.html)

[Pooling](pool.html)

[Configuration](config.html)

[Frequently Asked Questions](faq.html)

[Home Page](../../index.html)
>
[Java Naming and Directory Interface(TM).](../index.html)
>
[Advanced Topics for LDAP Users](index.html)

[« Previous](connect.html) • [Trail](../TOC.html) • [Next »](close.html)

# Creation

There are several ways in which a connection is created. The most
common way is from the creation of an initial context.
When you create an
[InitialContext](http://download.oracle.com/javase/7/docs/api/javax/naming/InitialContext.html),
[InitialDirContext](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/InitialDirContext.html), or
[InitialLdapContext](http://download.oracle.com/javase/7/docs/api/javax/naming/ldap/InitialLdapContext.html) by using the LDAP service provider, a connection is set up immediately with
the target LDAP server named in the
[Context.PROVIDER\_URL](http://download.oracle.com/javase/7/docs/api/javax/naming/Context.html#PROVIDER_URL) property.
Each time an initial context is created, a new LDAP
connection is created.
See the [Connection Pooling](pool.html) section for information on
how to change this behavior.

If the property value contains more than one URL, then each URL is tried
in turn until one is used to create a successful connection.
The property value is then updated to be the successful URL.
See the
[JNDI Tutorial](http://java.sun.com/products/jndi/tutorial/ldap/misc/url.html#MULTI) for an example of how to create an initial context using a list of URLs.

There are three other direct ways in which a connection is
created.

1. By passing a URL as the name argument to
   the initial context. When an LDAP or LDAPS URL is pass as a name
   parameter to the initial context, the information in the URL is used
   to create a new connection to the LDAP server, regardless of whether
   the initial context instance itself has a connection to an LDAP
   server. In fact, the initial context might not be connected to any
   server. See the
   [JNDI Tutorial](http://java.sun.com/products/jndi/tutorial/beyond/url/initctx.html)  for more information on how URLs are used as names.
2. Another way that a connection is created is by use of a Reference.
   When a
   [Reference](http://download.oracle.com/javase/7/docs/api/javax/naming/Reference.html)  containing an LDAP or LDAPS URL is passed to
   [NamingManager.getObjectInstance()](http://download.oracle.com/javase/7/docs/api/javax/naming/spi/NamingManager.html#getObjectInstance(java.lang.Object, javax.naming.Name, javax.naming.Context, java.util.Hashtable)) or
   [DirectoryManager.getObjectInstance()](http://download.oracle.com/javase/7/docs/api/javax/naming/spi/DirectoryManager.html#getObjectInstance(java.lang.Object, javax.naming.Name, javax.naming.Context, java.util.Hashtable, javax.naming.directory.Attributes)), a new connection is created using information specified in the URL.
3. Finally, when a referral is followed manually or automatically, the information in
   the referral is used to create a new connection.
   See the
   [JNDI Tutorial](http://java.sun.com/products/jndi/tutorial/ldap/referral/index.html)  for information on referrals.

## Shared Connections

Context instances and
[NamingEnumerations](http://download.oracle.com/javase/7/docs/api/javax/naming/NamingEnumeration.html) that are derived from one Context instance
share the same connection until changes to one of the
Context instances make sharing no longer possible.
For example, if you invoke
[Context.lookup()](http://download.oracle.com/javase/7/docs/api/javax/naming/Context.html#lookup(javax.naming.Name)),
[Context.listBindings()](http://download.oracle.com/javase/7/docs/api/javax/naming/Context.html#listBindings(javax.naming.Name)) or
[DirContext.search()](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/DirContext.html#search(javax.naming.Name, java.lang.String, javax.naming.directory.SearchControls)) from the initial context and get back other Context instances,
then all of those Context instances will share the same connection.

Here is [an example](examples/Shared.java).

```

// Create initial context
DirContext ctx = new InitialDirContext(env);

// Get a copy of the same context
Context ctx2 = (Context)ctx.lookup("");

// Get a child context
Context ctx3 = (Context) ctx.lookup("ou=NewHires");

```

In this example, ctx, ctx2, and ctx3
will share the same connection.

Sharing is done regardless of how the Context instance came
into existence. For example, a Context instance obtained by following
a referral will share the same connection as the referral.

When you change a Context instance's environment properties
that are related to
a connection,
such as the principal name or credentials of the user, the Context
instance on which you make these changes will get its own connection
(if the connection is shared). Context instances that are derived
from this Context instance in the future will share this new connection.
Context instances that previously shared the old connection
are not affected (that is, they continue to use the old connection).

Here is [an example](examples/NewConn.java) that uses two connections.

```

// Create initial context (first connection)
DirContext ctx = new InitialDirContext(env);

// Get a copy of the same context
DirContext ctx2 = (DirContext)ctx.lookup("");

// Change authentication properties in ctx2
ctx2.addToEnvironment(Context.SECURITY_PRINCIPAL, 
    "cn=C. User, ou=NewHires, o=JNDITutorial");
ctx2.addToEnvironment(Context.SECURITY_CREDENTIALS, "mysecret");

// Method on ctx2 will use new connection
System.out.println(ctx2.getAttributes("ou=NewHires"));

```

ctx2 initially shares the same connection with ctx.
But when its principal and password properties are changed,
it can no longer use ctx's connection.
The LDAP provider will automatically create a new connection for
ctx2.

Similarly, if you use
[LdapContext.reconnect()](http://download.oracle.com/javase/7/docs/api/javax/naming/ldap/LdapContext.html#reconnect(javax.naming.ldap.Control[])) to change the Context instance's connection controls,
the Context instance will get its own connection
if the connection was being shared.

If the Context instance's connection was not being shared
(i.e., no Contexts have been derived from it),
then changes to its environment or connection controls will not cause
a new connection to be created. Instead, any changes relevant to the
connection will be applied to the existing connection.
## Creation Timeouts
Not all connection creations are successful. If the LDAP provider
cannot establish a connection within a certain timeout period, it
aborts the connection attempt. By default, this timeout period is the
network (TCP) timeout value, which is in the order of a few minutes.
To change the timeout period, you use the
"com.sun.jndi.ldap.connect.timeout" environment property.
The value of this property is the string representation of an integer
representing the connection timeout in milliseconds.

Here is [an example](examples/Timeout.java).

```

// Set up environment for creating initial context
Hashtable env = new Hashtable(11);
env.put(Context.INITIAL_CONTEXT_FACTORY, 
    "com.sun.jndi.ldap.LdapCtxFactory");
env.put(Context.PROVIDER_URL, "ldap://localhost:389/o=JNDITutorial");

// Specify timeout to be 5 seconds
env.put("com.sun.jndi.ldap.connect.timeout", "5000");

// Create initial context
DirContext ctx = new InitialDirContext(env);

// do something useful with ctx

```

In this example, if a connection cannot be created within 5 seconds,
an exception will be thrown.

If the Context.PROVIDER\_URL property contains more than one
URL, the provider will use the timeout for each URL. For
example, if there are 3 URLs and the timeout has been specified to be
5 seconds, then the provider will wait for a maximum of 15 seconds in
total.

See the [Connection Pooling](pool.html#TIMEOUT) section
for information on how this property affects connection pooling.

[« Previous](connect.html)
•
[Trail](../TOC.html)
•
[Next »](close.html)

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

**Previous page:** Connection Management
  
**Next page:** Closing




A browser with JavaScript enabled is required for this page to operate properly.