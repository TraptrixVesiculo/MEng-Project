[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Java Naming and Directory Interface(TM).
  
**Lesson:** Advanced Topics for LDAP Users
  
**Section:** More LDAP Operations

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

LDAP Unsolicited Notifications

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

[« Previous](result.html) • [Trail](../TOC.html) • [Next »](connect.html)

# LDAP Unsolicited Notifications

The LDAP v3
([RFC 2251](http://ietf.org/rfc/rfc2251.txt))
defines an *unsolicited notification*, a message
that is sent by an LDAP server to the client without any provocation
from the client.
An unsolicited notification is represented in the JNDI by the
[UnsolicitedNotification](http://download.oracle.com/javase/7/docs/api/javax/naming/ldap/UnsolicitedNotification.html) interface.

Because unsolicited notifications are sent asynchronously by the server,
you can use the same
[event model](http://java.sun.com/products/jndi/tutorial/beyond/event/index.html) 
used for receiving notifications about
namespace changes and object content changes.
You register interest in receiving unsolicited notifications by registering an
[UnsolicitedNotificationListener](http://download.oracle.com/javase/7/docs/api/javax/naming/ldap/UnsolicitedNotificationListener.html) with an
[EventContext](http://download.oracle.com/javase/7/docs/api/javax/naming/event/EventContext.html) or
[EventDirContext](http://download.oracle.com/javase/7/docs/api/javax/naming/event/EventDirContext.html).

Here is [an example](examples/RegUnsol.java) of an
UnsolicitedNotificationListener.
> ```
>
> public class UnsolListener implements UnsolicitedNotificationListener {
>     public void notificationReceived(UnsolicitedNotificationEvent evt) {
>         System.out.println("received: " + evt);
>     }
>
>     public void namingExceptionThrown(NamingExceptionEvent evt) {
>         System.out.println(">>> UnsolListener got an exception");
> 	    evt.getException().printStackTrace();
>     }
> }
>
> ```

Following is an example
that registers an implementation of
UnsolicitedNotificationListener with an event source.
Note that only the listener argument to
[EventContext.addNamingListener()](http://download.oracle.com/javase/7/docs/api/javax/naming/event/EventContext.html#addNamingListener(javax.naming.Name, int, javax.naming.event.NamingListener)) is relevant. The name and scope parameters are not relevant
to unsolicited notifications.

> ```
>
> // Get the event context for registering the listener
> EventContext ctx = (EventContext)
>     (new InitialContext(env).lookup("ou=People"));
>
> // Create the listener
> NamingListener listener = new UnsolListener();
>
> // Register the listener with the context (all targets equivalent)
> ctx.addNamingListener("", EventContext.ONELEVEL_SCOPE, listener);
>
> ```

When running this program, you need to point it at an LDAP server
that can generate unsolicited notifications and prod the server
to emit the notification. Otherwise, after one minute
the program will exit silently.

A listener that implements
UnsolicitedNotificationListener can also implement other
[NamingListener](http://download.oracle.com/javase/7/docs/api/javax/naming/event/NamingListener.html) interfaces, such as
[NamespaceChangeListener](http://download.oracle.com/javase/7/docs/api/javax/naming/event/NamespaceChangeListener.html) and
[ObjectChangeListener](http://download.oracle.com/javase/7/docs/api/javax/naming/event/ObjectChangeListener.html).

[« Previous](result.html)
•
[Trail](../TOC.html)
•
[Next »](connect.html)

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

**Previous page:** Search Results
  
**Next page:** Connection Management




A browser with JavaScript enabled is required for this page to operate properly.