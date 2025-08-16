[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Java Naming and Directory Interface(TM).
  
**Lesson:** Advanced Topics for LDAP Users

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

More LDAP Operations

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

[« Previous](ssl.html) • [Trail](../TOC.html) • [Next »](compare.html)

# More LDAP Operations

The rest of the LDAP lesson covers how the JNDI provides ability to
perform certain interesting LDAP operations.

## Renaming Objects

You use
[Context.rename()](http://download.oracle.com/javase/7/docs/api/javax/naming/Context.html#rename(javax.naming.Name, javax.naming.Name)) to rename an object in the directory.
In the
[LDAP v2](http://ietf.org/rfc/rfc1777.txt),
this corresponds to the "modify RDN" operation that renames an entry
within the same context (that is, renaming a sibling).
In the
[LDAP v3](http://ietf.org/rfc/rfc2251.txt),
this corresponds to the "modify DN" operation, which is like "modify RDN,"
except that the old and new entries need not be in the same context.
You can use Context.rename() to rename a leaf entry or an interior node.
The example shown in the
[Naming and Directory Operations](../../jndi/ops/rename.html )  lesson renames a leaf entry.
The following [code](examples/RenameInterior.java)
renames an interior node from "ou=NewHires" to "ou=OldHires":

```

ctx.rename("ou=NewHires", "ou=OldHires");

```

---

**Note:** The [Sun Java Directory Server v5.2](http://www.oracle.com/us/sun/index.html)
does not support renaming interior nodes. If you run this example,
then you will get a
[ContextNotEmptyException](http://download.oracle.com/javase/7/docs/api/javax/naming/ContextNotEmptyException.html).

---

### Renaming to a Different Part of the DIT

With the LDAP v3, you can rename an entry to a different part of the DIT.
To do this by using Context.rename(), you must use a context
that is the common ancestor for both the new and the old entries.
For example, to rename
"cn=C. User, ou=NewHires, o=JNDITutorial" to
"cn=C. User, ou=People, o=JNDITutorial",
you must use the context named by "o=JNDITutorial".
Following is [an example](examples/RenameDiffParent.java) that demonstrates
this. If you try to run this example against an LDAP v2 server,
then you will get an
[InvalidNameException](http://download.oracle.com/javase/7/docs/api/javax/naming/InvalidNameException.html) because version 2 does not support this feature.

```

ctx.rename("cn=C. User, ou=NewHires", "cn=C. User, ou=People");

```

---

**Note:** The [Sun Java Directory Server v5.2](http://www.sun.com/)
does not support renaming with different parent nodes.
If you run this example by using that server,
then you will get a
[OperationNotSupportedException](http://download.oracle.com/javase/7/docs/api/javax/naming/OperationNotSupportedException.html) (indicating a "protocol error").

---

### Keeping the Old Name Attributes

In the LDAP, when you rename an entry, you have the option of keeping
the entry's old RDN as an attribute
of the updated entry. For example,
if you rename the entry "cn=C. User" to
"cn=Claude User",
you can specify whether you want the old RDN
"cn=C. User" to be kept
as an attribute.

To specify whether you want to keep the old name attribute
when you use Context.rename(),
use the "java.naming.ldap.deleteRDN" environment property.
If this property's value is "true" (the default), the old RDN is removed.
If its value is "false", then
the old RDN is kept as an attribute of the updated entry.
The complete example is [here](examples/RenameKeepRDN.java).

```

// Set the property to keep RDN
env.put("java.naming.ldap.deleteRDN", "false");

// Create the initial context
DirContext ctx = new InitialDirContext(env);

// Perform the rename
ctx.rename("cn=C. User, ou=NewHires", "cn=Claude User,ou=NewHires");

```

[« Previous](ssl.html)
•
[Trail](../TOC.html)
•
[Next »](compare.html)

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

**Previous page:** SSL and Custom Sockets
  
**Next page:** LDAP Compare




A browser with JavaScript enabled is required for this page to operate properly.