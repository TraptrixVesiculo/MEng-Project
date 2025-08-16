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

[Pooling](pool.html)

Configuration

[Frequently Asked Questions](faq.html)

[Home Page](../../index.html)
>
[Java Naming and Directory Interface(TM).](../index.html)
>
[Advanced Topics for LDAP Users](index.html)

[« Previous](pool.html) • [Trail](../TOC.html) • [Next »](faq.html)

# Configuration

Connection pooling is configured and maintained per Java runtime.
Connections are not shared across different runtimes. To use
connection pooling, no configuration is required. Configuration is
necessary only if you want to customize how pooling is done, such as
to control the size of the pools and which types of connections are pooled.

You configure connection pooling by using
a number of system properties at program startup time.
Note that these are system properties,
*not* environment properties and that they affect all connection pooling
requests.

Here is an example of a command line that
sets the maximum pool size to 20, the preferred pool size to 10,
and the idle timeout to a minute for pooled connections.

```

# java -Dcom.sun.jndi.ldap.connect.pool.maxsize=20 \
       -Dcom.sun.jndi.ldap.connect.pool.prefsize=10 \
       -Dcom.sun.jndi.ldap.connect.pool.timeout=60000 \
    UsePool

```

The following table lists the system properties for configuring
connection pooling. They are described in more detail
in the rest of this section.

| System Property Name | Description | Default |
| --- | --- | --- |
| com.sun.jndi.ldap.connect.pool.authentication | A list of space-separated authentication types of connections that may be pooled. Valid types are "none", "simple", and "DIGEST-MD5". | "none simple" |
| com.sun.jndi.ldap.connect.pool.debug | A string that indicates the level of debug output to produce. Valid values are "fine" (trace connection creation and removal) and "all" (all debugging information). |  |
| com.sun.jndi.ldap.connect.pool.initsize | The string representation of an integer that represents the number of connections per connection identity to create when initially creating a connection for the identity. | 1 |
| com.sun.jndi.ldap.connect.pool.maxsize | The string representation of an integer that represents the maximum number of connections per connection identity that can be maintained concurrently. | no maximum size |
| com.sun.jndi.ldap.connect.pool.prefsize | The string representation of an integer that represents the preferred number of connections per connection identity that should be maintained concurrently. | no preferred size |
| com.sun.jndi.ldap.connect.pool.protocol | A list of space-separated protocol types of connections that may be pooled. Valid types are "plain" and "ssl". | "plain" |
| com.sun.jndi.ldap.connect.pool.timeout | The string representation of an integer that represents the number of milliseconds that an idle connection may remain in the pool without being closed and removed from the pool. | no timeout |

## What Gets Pooled

When you request that a Context instance use connection
pooling by using the
"com.sun.jndi.ldap.connect.pool" environment property,
the connection that is used might or might not be pooled.
The default rule is that plain (non-SSL) connections that use
simple or no authentication are allowed to be pooled.
You can change this default to include SSL connections and the DIGEST-MD5
authentication type by using system properties.
To allow both plain and SSL connections to be pooled, set
the "com.sun.jndi.ldap.connect.pool.protocol" system property
to the string "plain ssl".
To allow connections of anonymous (none), simple and
DIGEST-MD5 authentication types to be pooled, set
the com.sun.jndi.ldap.connect.pool.authentication
system property to the string "none simple DIGEST-MD5".

There are a couple of environment properties that automatically
disqualify a Context instance from using
a pooled connection.
A Context instance cannot use a pooled connection if it has
its "java.naming.ldap.factory.socket" property set
to a custom socket factory class,
or its "java.naming.security.sasl.callback" property set
to a custom callback handler class,
or its "com.sun.jndi.ldap.trace.ber" property set to enable protocol
tracing.

## How Connections are Pooled

When a Context instance requests to use a pooled connection,
the LDAP provider needs to determine whether the request can be
satisfied by an existing pooled connection. It does this by
assigning a *connection identity* to each pooled connection
and checking whether the incoming request has the same connection
identity as that of one of its pooled connections.

A connection identity is the set of the parameters required to create a
possibly authenticated LDAP connection. Its composition depends on the
authentication type of the request, as shown in the following table.

| Authentication Type | Connection Identity Contents |
| --- | --- |
| none | * connection controls* host name, port number as specified in the "java.naming.provider.url"     property, referral, or URL supplied to the initial context* the contents of the following properties: ```        java.naming.security.protocol       java.naming.ldap.version        ``` |
| simple | * all of the information listed for none* the contents of following properties: ```      java.naming.security.principal     java.naming.security.credentials      ``` |
| DIGEST-MD5 | * all of the information listed for simple* the contents of following properties: ```      java.naming.security.sasl.authorizationId     java.naming.security.sasl.realm     javax.security.sasl.qop     javax.security.sasl.strength     javax.security.sasl.server.authentication     javax.security.sasl.maxbuffer     javax.security.sasl.policy.noplaintext     javax.security.sasl.policy.noactive     javax.security.sasl.policy.nodictionary     javax.security.sasl.policy.noanonymous     javax.security.sasl.policy.forward     javax.security.sasl.policy.credentials      ``` |

## Pool Sizes

The LDAP provider maintains pools of connections; each pool
holds connections (either in-use or idle)
that have the same connection identity.
There are three sizes that affect the management of each pool.
These sizes are global and affect all pools.

The *initial pool size* is the number of connections per
connection identity that the LDAP service provider creates when first
creating the pool (which corresponds to when the application first
requests a pooled connection for that connection identity).
Authentication of each connection in the pool is performed on
demand, as the connection gets used. By default, the initial pool
size is 1 and can be changed by using the system property
"com.sun.jndi.ldap.connect.pool.initsize". It is typically used at
application start-up time to prime the pool with a certain number of
connections to a server.

The *maximum pool size* is the maximum number of connections
per connection identity that can be maintained concurrently by the
LDAP service provider. Both in-use and idle connections contribute to
this number. When the pool size reaches this number, no new
connection for the corresponding connection identity may be created
until a connection in the pool has been removed (i.e., the physical
connection is closed). When the pool size reaches the maximum and all
of the connections in the pool are in use, the application's request
for a connection from that pool is blocked until a connection in the
pool either becomes idle or is removed. A maximum pool size of 0
means that there is no maximum size: A request for a pooled connection
will use an existing pooled idle connection or a newly created pooled
connection.

The *preferred pool size* is the preferred number of
connections per connection identity that the LDAP service provider
should maintain. Both in-use and idle connections contribute to this
number. When an application requests the use of a pooled connection
and the pool size is less than the preferred size, the LDAP provider
will create and use a new pooled connection regardless of whether an
idle connection is available. When an application is finished with a
pooled connection (by invoking Context.close() on all
contexts that share the connection) and the pool size is greater than
the preferred size, the LDAP provider will close and remove the pooled
connection from the pool. A preferred pool size of 0 means that there
is no preferred size: A request for a pooled connection will result in
a newly created connection only if no idle ones are available.

Note that the maximum pool size overrides both the initial and
preferred pool sizes. For example, setting the preferred pool size
greater than the maximum pool size is effectively setting it to the
maximum pool size.

## Idle Connections

When the application is finished with a pooled connection (by invoking
Context.close() on all contexts that share the connection),
the underlying pooled connection is marked as idle, waiting to be
reused. By default, idle connections remain in the pool indefinitely
until they are garbage-collected. If the
"com.sun.jndi.ldap.connect.pool.timeout" system property has
been set, the LDAP provider will automatically close and remove pooled
connections that have been idle for more than the specified period.

[« Previous](pool.html)
•
[Trail](../TOC.html)
•
[Next »](faq.html)

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

**Previous page:** Pooling
  
**Next page:** Frequently Asked Questions




A browser with JavaScript enabled is required for this page to operate properly.