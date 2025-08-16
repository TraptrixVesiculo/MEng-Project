[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Java Naming and Directory Interface(TM).
  
**Lesson:** New features in JDK 5.0 and JDK 6

[New features in JDK 5.0 and JDK 6](index.html)

[Retrieving Distinguished Name](dn.html)

[Standard LDAP Controls](controls-std.html)

[Paged Results Control](paged-results.html)

[Sort Control](sort.html)

[Manage Referral Control](mdsaIT.html)

[Manipulating LdapName (Distinguished Name)](ldapname.html)

[Manipulating Relative Distringuished Name (RDN)](rdn.html)

Setting Timeout for Ldap Operations

[Home Page](../../index.html)
>
[Java Naming and Directory Interface(TM).](../index.html)
>
[New features in JDK 5.0 and JDK 6](index.html)

[« Previous](rdn.html) • [Trail](../TOC.html) • [Next »](../end.html)

# Setting Timeout for Ldap Operations

When an LDAP request is made by a client to a server and the server
does not respond for some reason, the client waits forever for the
server to respond until the TCP timeouts.
On the client-side what the user experiences is esentially a process
hang. In order to control the LDAP request in a timely manner, a read
timeout can be configured for the Sun JNDI/LDAP Service Provider
since Java SE 6.

The new environment property:

```

 com.sun.jndi.ldap.read.timeout
 
```

can be used to specify the read timeout for an LDAP operation.
The value of this property is the string
representation of an integer representing the read timeout in
milliseconds for LDAP operations.
If the LDAP provider doesn't get an LDAP response within the specified
period, it aborts the read attempt. The integer should be greater than zero.
An integer less than or equal to zero means no read timeout is specified
which is equivalent to waiting for the response infinitely until it is
received which defaults to the original behavior.

If this property is not specified, the default is to wait for the
response until it is received.
  
For example,

```

    env.put("com.sun.jndi.ldap.read.timeout", "5000");
    
```

causes the LDAP service provider to abort the read attempt if the server
does not respond with a reply within 5 seconds.

Here is an [example](examples/ReadTimeoutTest.java) that uses
a dummy server which does not respond to
LDAP requests to show how this property behaves when set to a non-zero
value.

```

    
	env.put(Context.INITIAL_CONTEXT_FACTORY,
     		"com.sun.jndi.ldap.LdapCtxFactory");
	env.put("com.sun.jndi.ldap.read.timeout", "1000");
	env.put(Context.PROVIDER_URL, "ldap://localhost:2001");

	Server s = new Server();

	try {

     	    // start the server
     	    s.start();

           // Create initial context
           DirContext ctx = new InitialDirContext(env);
           System.out.println("LDAP Client: Connected to the Server");
		:
	        :
 	} catch (NamingException e) {
     	   e.printStackTrace();
	}

    
```

The above program prints the stack trace below, as the server does not even
respond to the LDAP bind request when an InitialDirContext is created.
The client times out waiting for the server's response.

```

    
	Server: Connection accepted
	javax.naming.NamingException: LDAP response read timed out, timeout used:1000ms.
	:
	:

        at javax.naming.directory.InitialDirContext.(InitialDirContext.java:82)
        at ReadTimeoutTest.main(ReadTimeoutTest.java:32)
    
```

Note that this property is different from the another environment property com.sun.jndi.ldap.connect.timeout that sets the timeout for
connecting to the server. The read timeout applies to the LDAP response
from the server after the initial connection is established with the server.

[« Previous](rdn.html)
•
[Trail](../TOC.html)
•
[Next »](../end.html)

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

**Previous page:** Manipulating Relative Distringuished Name (RDN)
  
**Next page:** End of Trail




A browser with JavaScript enabled is required for this page to operate properly.