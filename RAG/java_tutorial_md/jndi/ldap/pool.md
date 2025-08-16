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

[Creation](create.html)

[Closing](close.html)

Pooling

[Configuration](config.html)

[Frequently Asked Questions](faq.html)

[Home Page](../../index.html)
>
[Java Naming and Directory Interface(TM).](../index.html)
>
[Advanced Topics for LDAP Users](index.html)

[« Previous](close.html) • [Trail](../TOC.html) • [Next »](config.html)

# Pooling

The [Connection Creation](create.html) section described when
connections are created. It described how several Context
instances can share the same connection.

Another type of connection sharing supported by the LDAP service
provider is called *connection pooling*. In this type of
sharing, the LDAP service provider maintains a pool of (possibly)
previously used connections and assigns them to a Context
instance as needed. When a Context
instance is done with a connection (closed or garbage collected), the
connection is returned to the pool for future use.
Note that this form of sharing is sequential: a connection is retrieved
from the pool, used, returned to the pool, and then, retrieved again
from the pool for another Context instance.

The pool of connections is maintained per Java runtime system.
For some situations, connection pooling can improve performance
significantly. For example, only one connection is required for
processing a search response that contains four referral
references to the same LDAP server if connection pooling is used.
Without connection pooling, such a scenario would require four
separate connections.

The rest of this lesson describes in more detail how to use connection pooling.

## How to Use Connection Pooling

You request connection pooling by adding the property,
"com.sun.jndi.ldap.connect.pool" to the environment properties
passed to the initial context constructor.
Here is [an example](examples/UsePool.java).

```

// Set up environment for creating initial context
Hashtable env = new Hashtable(11);
env.put(Context.INITIAL_CONTEXT_FACTORY, 
    "com.sun.jndi.ldap.LdapCtxFactory");
env.put(Context.PROVIDER_URL, "ldap://localhost:389/o=JNDITutorial");

// Enable connection pooling
env.put("com.sun.jndi.ldap.connect.pool", "true");

// Create one initial context (Get connection from pool)
DirContext ctx = new InitialDirContext(env);

// do something useful with ctx

// Close the context when we're done
ctx.close();   // Return connection to pool

// Create another initial context (Get connection from pool)
DirContext ctx2 = new InitialDirContext(env);

// do something useful with ctx2

// Close the context when we're done
ctx2.close();   // Return connection to pool

```

This example creates two initial contexts in succession.
The second initial context will reuse the connection used by
the first.
To run this program and observe how the connections are retrieved
and returned to the pool, use the following command line.

```

#java -Dcom.sun.jndi.ldap.connect.pool.debug=fine UsePool

```

This should produce output that looks as follows.

```

Create com.sun.jndi.ldap.LdapClient@5d173[localhost:389]
Use com.sun.jndi.ldap.LdapClient@5d173
{ou=ou: NewHires, objectclass=objectClass: top, organizationalUnit}
Release com.sun.jndi.ldap.LdapClient@5d173
Use com.sun.jndi.ldap.LdapClient@5d173
{ou=ou: People, objectclass=objectClass: top, organizationalunit}
Release com.sun.jndi.ldap.LdapClient@5d173

```

You can decide when and
where to use pooling by including or omitting the
"com.sun.jndi.ldap.connect.pool" property, and thus
control pooling on a *per-context* basis.
In the previous example, if you removed this property from the
environment properties before creating the second initial context,
the second initial context would not use a pooled connection.

The LDAP provider keeps track of whether a connection is being used
through indications from the application. It assumes that an
application that is maintaining an open context handle is using the
connection. Therefore, in order for the LDAP provider to properly
manage the pooled connections, you must be diligent about
invoking Context.close() on contexts that you no longer need.

Bad connections are automatically detected and removed from the
pool by the LDAP provider.
The probability of a context ending up with a bad connection is the
same regardless of whether connection pooling is used.
## Creation Timeout
The pool of connections maintained by the LDAP service provider may be
limited in size; this is described in detail in the [Connection Pooling Configuration](config.html) section. When
connection pooling has been enabled and no pooled connection is
available, the client application will block, waiting for an available
connection. You can use the "com.sun.jndi.ldap.connect.timeout"
environment property to specify how long to wait for a pooled connection.
If you omit this property, the application will wait indefinitely.

This same property is also used to specify a timeout period for establishment of
the LDAP connection, as described in
the [Connection Creation](create.html#TIMEOUT) section.

## When Not to Use Pooling!!

Pooled connections are intended to be reused. Therefore,
if you plan to perform operations on a Context instance that might
alter the underlying connection's state, then you should not use connection
pooling for that Context instance.
For example, if you plan to invoke the Start TLS extended operation on
a Context instance, or plan to change security-related
properties (such as "java.naming.security.principal" or
"java.naming.security.protocol") after the initial context has
been created, you should not use connection pooling for that
Context instance because the LDAP provider does not track any
such state changes.
If you use connection pooling in such situations, you might be
compromising the security of your application.

[« Previous](close.html)
•
[Trail](../TOC.html)
•
[Next »](config.html)

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

**Previous page:** Closing
  
**Next page:** Configuration




A browser with JavaScript enabled is required for this page to operate properly.