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

Anonymous

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

[« Previous](auth_mechs.html) • [Trail](../TOC.html) • [Next »](simple.html)

# Anonymous

As just stated,
the default authentication mechanism is "none"
if no authentication environment properties have been set.
If the client sets the
[Context.SECURITY\_AUTHENTICATION](http://download.oracle.com/javase/7/docs/api/javax/naming/Context.html#SECURITY_AUTHENTICATION) environment property to
"none", then the authentication mechanism is
"none" and
all other authentication environment properties are ignored.
You would want to do this explicitly only to ensure that
any other authentication properties that might have been set are
ignored.
In either case,
the client will be treated as an *anonymous* client.
This means that the server does not know or care who the client is and will
allow the client to access (read and update) any data that has been
configured to be accessible by any unauthenticated client.

Because none of the directory examples in the
[Naming and Directory Operations](../../jndi/ops/index.html)  lesson set any of the authentication environment
properties, all of them use anonymous authentication.

Here is [an example](examples/None.java) that explicitly sets the
Context.SECURITY\_AUTHENTICATION property to "none"
(even though doing this
is not strictly necessary because that is the default).

```

// Set up the environment for creating the initial context
Hashtable env = new Hashtable();
env.put(Context.INITIAL_CONTEXT_FACTORY, 
    "com.sun.jndi.ldap.LdapCtxFactory");
env.put(Context.PROVIDER_URL, "ldap://localhost:389/o=JNDITutorial");

// Use anonymous authentication
env.put(Context.SECURITY_AUTHENTICATION, "none");

// Create the initial context
DirContext ctx = new InitialDirContext(env);

// ... do something useful with ctx

```

[« Previous](auth_mechs.html)
•
[Trail](../TOC.html)
•
[Next »](simple.html)

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

**Previous page:** Authentication Mechanisms
  
**Next page:** Simple




A browser with JavaScript enabled is required for this page to operate properly.