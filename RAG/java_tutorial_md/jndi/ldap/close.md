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

Closing

[Pooling](pool.html)

[Configuration](config.html)

[Frequently Asked Questions](faq.html)

[Home Page](../../index.html)
>
[Java Naming and Directory Interface(TM).](../index.html)
>
[Advanced Topics for LDAP Users](index.html)

[« Previous](create.html) • [Trail](../TOC.html) • [Next »](pool.html)

# Closing

Normal garbage collection takes care of removing Context
instances when they are no longer in use. Connections used by
Context instances being garbage collected will be closed
automatically. Therefore, you do not need to explicitly close
connections. Network connections, however, are limited resources and
for certain programs, you might want to have control over their
proliferation and usage. This section contains information on how to
close connections and how to get notified if the server closes the
connection.

## Explicit Closures

You invoke
[Context.close()](http://download.oracle.com/javase/7/docs/api/javax/naming/Context.html#close()) on a Context instance to indicate that you no longer need to use it.
If the Context instance being closed is using a dedicated
connection, the connection is also closed. If the Context
instance is sharing a connection with other Context
and unterminated NamingEnumeration instances,
the connection will not be closed
until close() has been invoked on all such Context and
NamingEnumeration instances.

In the [example](examples/Shared.java)
from the [Connection Creation](create.html#SHARE) section,
all three Context instances must be closed before the underlying
connection is closed.

```

// Create initial context
DirContext ctx = new InitialDirContext(env);

// Get a copy of the same context
Context ctx2 = (Context)ctx.lookup("");

// Get a child context
Context ctx3 = (Context) ctx.lookup("ou=NewHires");

// do something useful with ctx, ctx2, ctx3

// Close the contexts when we're done
ctx.close();
ctx2.close();
ctx3.close();

```

## Forced Implicit Closures

As mentioned previously,
for those Context and NamingEnumeration
instances that are no longer in scope,
the Java runtime system will eventually garbage collect them, thus
cleaning up the state that a close() would have done.
To force the garbage collection, you can use the following code.

```

Runtime.getRuntime().gc();
Runtime.getRuntime().runFinalization();

```

Depending on the state of the program, performing this procedure can
cause serious (temporary) performance degradation. If you need to
ensure that connections are closed, track Context instances
and close them explicitly.

## Detecting Connection Closures

LDAP servers often have an idle timeout period after which they will
close connections no longer being used.
When you subsequently invoke a method on
a Context instance that is using such a connection,
the method will throw a
[CommunicationException](http://download.oracle.com/javase/7/docs/api/javax/naming/CommunicationException.html).
To detect when the server closes the connection that a
Context instance is using, you register an
[UnsolicitedNotificationListener](http://download.oracle.com/javase/7/docs/api/javax/naming/ldap/UnsolicitedNotificationListener.html) with the Context instance.
[An example](examples/RegUnsol.java) is shown in the LDAP Unsolicited
Notifications section.
Although the example is designed for receiving unsolicited
notification from the server, it can also be used to detect connection
closures by the server. After starting the program, stop the LDAP
server and observe that the listener's
[namingExceptionThrown()](http://download.oracle.com/javase/7/docs/api/javax/naming/event/NamingListener.html#namingExceptionThrown(javax.naming.event.NamingExceptionEvent)) method gets called.

[« Previous](create.html)
•
[Trail](../TOC.html)
•
[Next »](pool.html)

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

**Previous page:** Creation
  
**Next page:** Pooling




A browser with JavaScript enabled is required for this page to operate properly.