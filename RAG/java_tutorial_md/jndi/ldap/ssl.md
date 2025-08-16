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

[Digest-MD5](digest.html)

SSL and Custom Sockets

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

[« Previous](digest.html) • [Trail](../TOC.html) • [Next »](rename.html)

# SSL and Custom Sockets

In addition to SASL authentication,
most LDAP servers allow their services to be accessed through SSL.
SSL is especially useful for LDAP v2 servers because the v2 protocol
does not support SASL authentication.

An SSL-enabled server often supports SSL in two ways.
In the most basic way,
the server supports SSL ports in addition to normal (unprotected) ports.
The other way in which a server supports SSL is via the use of the
Start TLS Extension ([RFC 2830](http://ietf.org/rfc/rfc2830.txt)).
This option is available only to LDAP v3 servers and is described in
detail in the
section.
#### Using the SSL Socket Property

By default, Sun's LDAP service provider uses plain sockets when communicating
with the LDAP server. To request that SSL sockets be use, set the
[Context.SECURITY\_PROTOCOL](http://download.oracle.com/javase/7/docs/api/javax/naming/Context.html#SECURITY_PROTOCOL) property to "ssl".

In the [following example](examples/Ssl.java),
the LDAP server is offering SSL at port 636. To run this program,
you must enable SSL on port 636 on your LDAP server. This procedure is
typically carried out by the directory's administrator.
> ---
>
>
> **Server Requirements:** 
> The LDAP server must be set up with an X.509 SSL server certificate
> and have SSL enabled.
> Typically, you must first obtain a signed
> certificate for the server from a certificate authority (CA).
> Then, follow the instructions from your directory vendor on how to enable SSL.
> Different vendors have different tools for doing this.
>
> For the
> [Sun Java Directory Server, v5.2](http://www.sun.com/),
> use the Manage Certificates tool in the
> Administration Console to generate a Certificate Signing Request (CSR).
> Submit the CSR to a CA to obtain an X.509 SSL server certificate.
> Using the Administration Console, add the certificate
> to the server's list of certificates.
> Also install the CA's certificate if it is not already in the server's list
> of trusted CAs.
> Enable SSL by using the Configuration tab in the Administration
> Console. Select the server in the left pane. Select the Encryption tab
> in the right pane. Click the checkboxes for "Enable SSL for this server"
> and "Use this cipher family: RSA", ensuring that the server certificate
> you have added is in the list of certificates.
>
> **Client Requirements:** 
> You need to ensure that the client trusts the LDAP server that you'll be using.
> You must install the server's certificate (or its CA's certificate)
> in your JRE's database of trusted certificates.
> Here is an example.
>
> ```
>
> # cd JAVA_HOME/lib/security
> # keytool -import -file server_cert.cer -keystore jssecacerts
>
> ```
>
> For information on how to use the security tools, see
> the  [Security](../../security/index.html) trail.
> For information on the JSSE, see the
> [Java Secure Socket Extension (JSSE) Reference Guide](http://download.oracle.com/javase/7/docs/technotes/guides/security/jsse/JSSERefGuide.html).
>
> ---

> ```
>
> // Set up the environment for creating the initial context
> Hashtable env = new Hashtable();
> env.put(Context.INITIAL_CONTEXT_FACTORY, 
>     "com.sun.jndi.ldap.LdapCtxFactory");
> env.put(Context.PROVIDER_URL, "ldap://localhost:636/o=JNDITutorial");
>
> // Specify SSL
> env.put(Context.SECURITY_PROTOCOL, "ssl");
>
> // Authenticate as S. User and password "mysecret"
> env.put(Context.SECURITY_AUTHENTICATION, "simple");
> env.put(Context.SECURITY_PRINCIPAL, "cn=S. User, ou=NewHires, o=JNDITutorial");
> env.put(Context.SECURITY_CREDENTIALS, "mysecret");
>
> // Create the initial context
> DirContext ctx = new InitialDirContext(env);
>
> // ... do something useful with ctx
>
> ```

> ---
>
> **Note:** If you use SSL to connect to a server on a port that is
> *not* using SSL, then your program will hang. Similarly, if you use a plain
> socket to connect to a server's SSL socket, then your application will hang.
> This is a characteristic of the SSL protocol.
>
> ---

#### Using the LDAPS URL
Instead of requesting the use of SSL via the use of the
[Context.SECURITY\_PROTOCOL](http://download.oracle.com/javase/7/docs/api/javax/naming/Context.html#SECURITY_PROTOCOL) property, you can also request the use of SSL via the use of
LDAPS URLs. An LDAPS URL is similar to an LDAP URL except that the
URL scheme is "ldaps" instead of "ldap". It specifies the use of SSL
when communicating with the LDAP server.

In the [following example](examples/Ldaps.java),
the LDAP server is offering SSL at port 636. To run this program,
you must enable SSL on port 636 on your LDAP server.
> ```
>
> // Set up the environment for creating the initial context
> Hashtable env = new Hashtable();
> env.put(Context.INITIAL_CONTEXT_FACTORY, 
>     "com.sun.jndi.ldap.LdapCtxFactory");
>
> // Specify LDAPS URL
> env.put(Context.PROVIDER_URL, "ldaps://localhost:636/o=JNDITutorial");
>
> // Authenticate as S. User and password "mysecret"
> env.put(Context.SECURITY_AUTHENTICATION, "simple");
> env.put(Context.SECURITY_PRINCIPAL, "cn=S. User, ou=NewHires, o=JNDITutorial");
> env.put(Context.SECURITY_CREDENTIALS, "mysecret");
>
> // Create the initial context
> DirContext ctx = new InitialDirContext(env);
>
> // ... do something useful with ctx
>
> ```

LDAPS URLs are accepted anywhere LDAP URLs are accepted. Check out the
[JNDI Tutorial](http://java.sun.com/products/jndi/tutorial/ldap/misc/url.html)  for details on LDAP and LDAPS URLs.
#### Client Authentication: Using SSL with the External SASL Mechanism
SSL provides authentication and other security services at a lower layer
than the LDAP. If authentication has already been done at the SSL,
the LDAP layer can use that authentication information from SSL by using the
[External](http://ietf.org/rfc/rfc2222.txt)
SASL mechanism.

The [following example](examples/External.java) is like
the [previous SSL example](examples/Ssl.java),
except that instead of using simple authentication, it uses the External SASL
authentication. By using External, you do not need to supply any
principal or password information, because they get picked up from the
SSL.
> ---
>
>
> **Server Requirements:** 
> This example requires the LDAP server to allow
> certificate-based client authentication. In addition, the LDAP server must
> trust (the CAs of) the client certificates that it receives, and must
> be able to map the owner distinguished names in the client certificates
> to principals that it knows about. Follow the instructions from
> your directory vendor on how to perform these tasks.
>
> **Client Requirements:** 
> This example requires the client to have an X.509 SSL client
> certificate. Moreover, the certificate must be stored as the first
> key entry in a keystore file. If this entry is password-protected, it
> must have the same password as the keystore. For more information
> about JSSE keystores, see the
> [Java Secure Socket Extension (JSSE) Reference Guide](http://download.oracle.com/javase/7/docs/technotes/guides/security/jsse/JSSERefGuide.html).
>
> ---

> ```
>
> // Set up the environment for creating the initial context
> Hashtable env = new Hashtable(11);
> env.put(Context.INITIAL_CONTEXT_FACTORY, 
>     "com.sun.jndi.ldap.LdapCtxFactory");
> env.put(Context.PROVIDER_URL, "ldap://localhost:636/o=JNDITutorial");
>
> // Principal and credentials will be obtained from the connection
> env.put(Context.SECURITY_AUTHENTICATION, "EXTERNAL");
>
> // Specify SSL
> env.put(Context.SECURITY_PROTOCOL, "ssl");
>
> // Create the initial context
> DirContext ctx = new InitialDirContext(env);
>
> ...
>
> ```

To run this program so that the client's certificate is used for
authentication, you must provide (as system properties)
the location and password of the keystore containing
the client's certificate. Here is an example of how to run the program.
> ```
>
> java -Djavax.net.ssl.keyStore=MyKeystoreFile \
>     -Djavax.net.ssl.keyStorePassword=mysecret \
>     External
>
> ```

If you do not supply a keystore, the
program will run using anonymous authentication because no client
credential exists at the SSL.

This example shows the most basic way to accomplish certificate-based
client authentication. More advanced ways can be accomplished by
writing and using a custom socket factory that accesses the client
certificate in a more flexible manner, perhaps by using an LDAP
directory. The next section shows how to use a custom socket factory
with your JNDI application.

#### Using Custom Sockets

When using SSL, the LDAP provider will, by default, use the socket factory,
[javax.net.ssl.SSLSocketFactory](http://download.oracle.com/javase/7/docs/api/javax/net/ssl/SSLSocketFactory.html) , for creating an SSL socket to communicate with the server, using
the default JSSE configuration.
The JSSE can be customized in a variety of ways, as detailed in the
[Java Secure Socket Extension (JSSE) Reference Guide](http://download.oracle.com/javase/7/docs/technotes/guides/security/jsse/JSSERefGuide.html).
However, there are times when those customizations are not
sufficient and you need to have more control over the SSL sockets, or
sockets in general, used by the LDAP service provider. For example,
you might need sockets that can bypass firewalls, or JSSE sockets that
use nondefault caching/retrieval policies for its trust and key
stores. To set the socket factory implementation used by
the LDAP service provider, set the
"java.naming.ldap.factory.socket" property to the
fully qualified class name of the socket factory. This class must implement the
[javax.net.SocketFactory](http://download.oracle.com/javase/7/docs/api/javax/net/SocketFactory.html) abstract class and provide an implementation of the
[getDefault()](http://download.oracle.com/javase/7/docs/api/javax/net/SocketFactory.html#getDefault()) method that returns an instance of the socket factory. See the
[Java Secure Socket Extension (JSSE) Reference Guide](http://download.oracle.com/javase/7/docs/technotes/guides/security/jsse/JSSERefGuide.html).

Here is an example of a [custom
socket factory](examples/CustomSocketFactory.java) that produces plain sockets.
> ```
>
> public class CustomSocketFactory extends SocketFactory {
>     public static SocketFactory getDefault() {
>
> 	System.out.println("[acquiring the default socket factory]");
> 	return new CustomSocketFactory();
>     }
> 	...
> }
>
> ```

Note that this example creates a new instance of CustomSocketFactory
each time a new LDAP connection is created. This might be appropriate
for some applications and socket factories.
If you want to reuse the same socket factory, getDefault()
should return a singleton.

To use this custom socket factory with a JNDI program, set the
"java.naming.ldap.factory.socket" property, as shown in the
[following example](examples/UseFactory.java).
> ```
>
> // Set up the environment for creating the initial context
> Hashtable env = new Hashtable();
> env.put(Context.INITIAL_CONTEXT_FACTORY, 
>     "com.sun.jndi.ldap.LdapCtxFactory");
> env.put(Context.PROVIDER_URL, "ldap://localhost:389/o=JNDITutorial");
>
> // Specify the socket factory
> env.put("java.naming.ldap.factory.socket", "CustomSocketFactory");
>
> // Create the initial context
> DirContext ctx = new InitialDirContext(env);
>
> // ... do something useful with ctx
>
> ```

The "java.naming.ldap.factory.socket" property is
useful for setting the socket factory on a per context basis.
Another way to control the sockets used by the LDAP service provider is
to set the socket factory for all sockets used in the entire program, by using
[java.net.Socket.setSocketImplFactory()](http://download.oracle.com/javase/7/docs/api/java/net/Socket.html#setSocketImplFactory(java.net.SocketImplFactory)).
Use of this method is less flexible because it affects all socket connections,
not just LDAP connections and therefore, should be used with care.

[« Previous](digest.html)
•
[Trail](../TOC.html)
•
[Next »](rename.html)

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

**Previous page:** Digest-MD5
  
**Next page:** More LDAP Operations




A browser with JavaScript enabled is required for this page to operate properly.