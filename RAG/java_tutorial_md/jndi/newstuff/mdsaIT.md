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

Manage Referral Control

[Manipulating LdapName (Distinguished Name)](ldapname.html)

[Manipulating Relative Distringuished Name (RDN)](rdn.html)

[Setting Timeout for Ldap Operations](readtimeout.html)

[Home Page](../../index.html)
>
[Java Naming and Directory Interface(TM).](../index.html)
>
[New features in JDK 5.0 and JDK 6](index.html)

[« Previous](sort.html) • [Trail](../TOC.html) • [Next »](ldapname.html)

# Manage Referral Control

The Manage Referral control ([RFC3296](http://ietf.org/rfc/rfc3296.txt))
enables manipulation of the referral and other special
objects as normal objects when performing an LDAP operation.
In other words, Manage Referral control tells the LDAP server to
return referral entries as ordinary entries instead of returning
"referral" error responses or continuation references.
The new class in JDK 5.0 below enables you to send Manage Referral Control
along with an LDAP request:

[javax.naming.ldap.ManageReferralControl](http://download.oracle.com/javase/7/docs/api/javax/naming/ldap/ManageReferralControl.html)

The Sun LDAP service provider will send this control automatically along with any request. You can also explicitly enable it setting Context.REFERRAL
environment property to "ignore".
For more information on Referral handling check the
[Referrals in the JNDI](http://java.sun.com/products/jndi/tutorial/ldap/referral/jndi.html) section of the JNDI Tutorial.

Here is an example that sends Manage Referral control along with an
LDAP request.

```

	   // Create initial context
	    LdapContext ctx = (LdapContext) new InitialDirContext(env);
	    ctx.setRequestControl(new Control[] new ManageReferralControl());

	    // Set controls for performing subtree search
	    SearchControls ctls = new SearchControls();
	    ctls.setSearchScope(SearchControls.SUBTREE_SCOPE);

	    // Perform search
	    NamingEnumeration answer = ctx.search("", "(objectclass=*)", ctls);

	    // Print the answer
	    while (answer.hasMore()) {
		System.out.println(">>>" + ((SearchResult)answer.next()).getName());
	    }

	    // Close the context when we're done
	    ctx.close();
         
```

The complete example can be found [here](examples/ManageReferral.java).

---

**Note 1:**
The above example will require you to set up a second server using
the configuration file [refserver.ldif](../../jndi/software/config/refserver.ldif).
The server must support LDAP v3 and RFC 3296. If the server does not support
referrals in this way,
then the example won't work as shown. The configuration file contains
referrals that point to the original server that you've set up.
It assumes that the original server is on port 389 on the local machine.
If you have set up the server on another machine or port,
then you need to edit the "ref" entries in the refserver.ldif file
and replace "localhost:389" with the appropriate setting.
The second server is to be set up on port 489 on the local machine.
If you set up the second server on another machine or port, then you
need to adjust the setting of the Context.PROVIDER\_URL environment property
for the initial context accordingly.

Setting up a directory server is typically performed by the directory or
system administrator. See the [Software Setup](../../jndi/software/index.html) lesson for more information.

**Note 2:** Windows Active Directory: Because Active Directory does not support the
Manage Referral control, none of the examples in this lesson will work
against Active Directory.

---

[« Previous](sort.html)
•
[Trail](../TOC.html)
•
[Next »](ldapname.html)

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

**Previous page:** Sort Control
  
**Next page:** Manipulating LdapName (Distinguished Name)




A browser with JavaScript enabled is required for this page to operate properly.